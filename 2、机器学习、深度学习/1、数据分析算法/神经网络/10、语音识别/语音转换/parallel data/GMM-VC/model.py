# -*- coding: utf-8 -*-

import numpy as np
import scipy.sparse
import sklearn.mixture
from sklearn.mixture._gaussian_mixture import _compute_precision_cholesky
import pysptk
import pyworld

def synthesis(f0, mcep, ap,config):

    # mcep into spc
    spc = pysptk.mc2sp(mcep, config["alpha"], config["fftl"])
 
    wav = pyworld.synthesize(f0, spc, ap,
                             config["fs"], frame_period=config["shiftms"])

    return wav

def f0_convert(f0, orgf0stats, tarf0stats):        
    # get length and dimension
    T = len(f0)
    # perform f0 conversion
    cvf0 = np.zeros(T)
    nonzero_indices = f0 > 0
    cvf0[nonzero_indices] = np.exp((tarf0stats[1] / orgf0stats[1]) *
                                   (np.log(f0[nonzero_indices]) -
                                    orgf0stats[0]) + tarf0stats[0])
    return cvf0


def GV_postfilter(data, gvstats, cvgvstats=None, alpha=1.0, startdim=1):
 
        # get length and dimension
        T, dim = data.shape
        assert gvstats is not None
        assert dim == gvstats.shape[1]

        # calculate statics of input data
        datamean = np.mean(data, axis=0)

        if cvgvstats is None:
            # use variance of the given data
            datavar = np.var(data, axis=0)
        else:
            # use variance of trained gv stats
            datavar = cvgvstats[0]

        # perform GV postfilter
        filtered = np.sqrt(gvstats[0, startdim:] / datavar[startdim:]) * \
            (data[:, startdim:] - datamean[startdim:]) + datamean[startdim:]

        filtered_data = np.c_[data[:, :startdim], filtered]

        return alpha * filtered_data + (1 - alpha) * data


def construct_static_and_delta_matrix(T, D, win=[-1.0, 1.0, 0]):
    """Calculate static and delta transformation matrix

    Parameters
    ----------
    T : scala, `T`
        Scala of time length
    D : scala, `D`
        Scala of the number of dimentsion
    win: array, optional, shape (`3`)
        The shape of window matrix for delta.
        Default set to [-1.0, 1.0, 0].

    Returns
    -------
    W : array, shape (`2 * D * T`, `D * T`)
        Array of static and delta transformation matrix.

    """

    static = [0, 1, 0]
    delta = win
    assert len(static) == len(delta)

    # generate full W
    DT = D * T
    ones = np.ones(DT)
    row = np.arange(2 * DT).reshape(2 * T, D)
    static_row = row[::2]
    delta_row = row[1::2]
    col = np.arange(DT)

    data = np.array([ones * static[0], ones * static[1],
                     ones * static[2], ones * delta[0],
                     ones * delta[1], ones * delta[2]]).flatten()
    row = np.array([[static_row] * 3,  [delta_row] * 3]).flatten()
    col = np.array([[col - D, col, col + D] * 2]).flatten()

    # remove component at first and end frame
    valid_idx = np.logical_not(np.logical_or(col < 0, col >= DT))

    W = scipy.sparse.csr_matrix(
        (data[valid_idx], (row[valid_idx], col[valid_idx])), shape=(2 * DT, DT))
    W.eliminate_zeros()

    return W

class GMMTrainer(object):
    def __init__(self, n_mix=32, n_iter=100):
        self.n_mix = n_mix
        self.n_iter = n_iter

        self.random_state = np.random.mtrand._rand
        self.param = sklearn.mixture.GaussianMixture(
            n_components=self.n_mix,
            covariance_type="full",
            max_iter=self.n_iter,
        )

    def open_from_param(self, param):
        self.param = param
        return

    def train(self, jnt):
        self.param.fit(jnt)

    

class GMMConvertor(object):
   
    def __init__(self, n_mix=32, covtype="full"):
        self.n_mix = n_mix
        
    def open_from_param(self, param):
        self.param = param
        self._deploy_parameters()
        return

    def convert(self, data, cvtype="mlpg"):
      
        # estimate parameter sequence
        cseq, wseq, mseq, covseq = self._gmmmap(data)

        if cvtype == "mlpg":
            # maximum likelihood parameter generation
            odata = self._mlpg(mseq, covseq)
        elif cvtype == "mmse":
            # minimum mean square error based parameter generation
            odata = self._mmse(wseq, data)
        else:
            raise ValueError("please choose conversion mode in `mlpg`, `mmse`")

        return odata

    def _gmmmap(self, sddata):
        # parameter for sequencial data
        T, sddim = sddata.shape

        # estimate posterior sequence
        wseq = self.pX.predict_proba(sddata)

        # estimate mixture sequence
        cseq = np.argmax(wseq, axis=1)

        mseq = np.zeros((T, sddim))
        covseq = np.zeros((T, sddim, sddim))
        for t in range(T):
            # read maximum likelihood mixture component in frame t
            m = cseq[t]

            # conditional mean vector sequence
            mseq[t] = self.meanY[m] + self.A[m] @ (sddata[t] - self.meanX[m])

            # conditional covariance sequence
            covseq[t] = self.cond_cov_inv[m]

        return cseq, wseq, mseq, covseq

    def _mmse(self, wseq, sddata):
        # parameter for sequencial data
        T, sddim = sddata.shape

        odata = np.zeros((T, sddim))
        for t in range(T):
            for m in range(self.n_mix):
                odata[t] += wseq[t, m] * (
                    self.meanY[m] + self.A[m] @ (sddata[t] - self.meanX[m])
                )

        # retern static and throw away delta component
        return odata[:, : sddim // 2]

    def _mlpg(self, mseq, covseq):
        # parameter for sequencial data
        T, sddim = mseq.shape

        # prepare W
        W = construct_static_and_delta_matrix(T, sddim // 2)

        # prepare D
        D = get_diagonal_precision_matrix(T, sddim, covseq)

        # calculate W'D
        WD = W.T @ D

        # W'DW
        WDW = WD @ W

        # W'Um
        WDm = WD @ mseq.flatten()

        # estimate y = (W'DW)^-1 * W'Dm
        odata = scipy.sparse.linalg.spsolve(WDW, WDm, use_umfpack=False).reshape(
            T, sddim // 2
        )

        # return odata
        return odata

    def _deploy_parameters(self):
        # read JD-GMM parameters from self.param
        self.w = self.param.weights_
        self.jmean = self.param.means_
        self.jcov = self.param.covariances_

        # devide GMM parameters into source and target parameters
        sddim = self.jmean.shape[1] // 2
        self.meanX = self.jmean[:, 0:sddim]
        self.meanY = self.jmean[:, sddim:]
        self.covXX = self.jcov[:, :sddim, :sddim]
        self.covXY = self.jcov[:, :sddim, sddim:]
        self.covYX = self.jcov[:, sddim:, :sddim]
        self.covYY = self.jcov[:, sddim:, sddim:]

        
        # estimate parameters for conversion
        self._set_Ab()
        self._set_pX()

        return

    def _set_Ab(self):
        # calculate A and b from self.jmean, self.jcov
        sddim = self.jmean.shape[1] // 2

        # calculate inverse covariance for covariance XX in each mixture
        self.covXXinv = np.zeros((self.n_mix, sddim, sddim))
        for m in range(self.n_mix):
            self.covXXinv[m] = np.linalg.inv(self.covXX[m])

        # calculate A, b, and conditional covariance given X
        self.A = np.zeros((self.n_mix, sddim, sddim))
        self.b = np.zeros((self.n_mix, sddim))
        self.cond_cov_inv = np.zeros((self.n_mix, sddim, sddim))
        for m in range(self.n_mix):
            # calculate A (i.e., A = yxcov_m * xxcov_m^-1)
            self.A[m] = self.covYX[m] @ self.covXXinv[m]

            # calculate b (i.e., b = mean^Y - A * mean^X)
            self.b[m] = self.meanY[m] - self.A[m] @ self.meanX[m]

            # calculate conditional covariance
            # (i.e., cov^(Y|X)^-1 = (yycov - A * xycov)^-1)
            self.cond_cov_inv[m] = np.linalg.inv(
                self.covYY[m] - self.A[m] @ self.covXY[m]
            )

        return

    def _set_pX(self):
        # probability density function of X
        self.pX = sklearn.mixture.GaussianMixture(
            n_components=self.n_mix, covariance_type="full"
        )
        self.pX.weights_ = self.w
        self.pX.means_ = self.meanX
        self.pX.covariances_ = self.covXX

        # following function is required to estimate porsterior
        self.pX.precisions_cholesky_ = _compute_precision_cholesky(self.covXX, "full")
        return


def get_diagonal_precision_matrix(T, D, covseq):
    return scipy.sparse.block_diag(covseq, format="csr")
