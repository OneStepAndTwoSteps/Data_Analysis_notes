import numpy as np
from dtw import dtw
from fastdtw import fastdtw
from dtw_c import dtw_c
from model import GMMTrainer,GMMConvertor
import os
from tqdm import tqdm

def align_data(org_data, tar_data, twf):
    jdata = np.c_[org_data[twf[0]], tar_data[twf[1]]]
    return jdata

def delta(data, win=[-1.0, 1.0, 0]):

    if data.ndim == 1:
        # change vector into 1d-array
        T = len(data)
        dim = data.ndim
        data = data.reshape(T, dim)
    else:
        T, dim = data.shape

    win = np.array(win, dtype=np.float64)
    delta = np.zeros((T, dim))

    delta[0] = win[0] * data[0] + win[1] * data[1]
    delta[-1] = win[0] * data[-2] + win[1] * data[-1]

    for i in range(len(win)):
        delta[1:T - 1] += win[i] * data[i:T - 2 + i]

    return delta
    
def static_delta(data, win=[-1.0, 1.0, 0]):
    sddata = np.c_[data, delta(data, win)]
    return sddata
    
# 对输入特征加上delta成分，并利用能量阈值对特征进行筛选
def extsddata(data, npow, power_threshold=-20):
    # 将输入特征加入delta成分
    data =static_delta(data)
    T = data.shape[0]
    if T != len(npow):
        raise("Length of two vectors is different.")
    # 根据能量消除静音帧
    valid_index = np.where(npow > power_threshold)
    extdata = data[valid_index]
    assert extdata.shape[0] <= T

    return extdata
    
    
# 距离函数
def melcd(array1, array2):
    if array1.shape != array2.shape:
        raise ValueError(
            "The shapes of both arrays are different \
            : {} / {}".format(array1.shape, array2.shape))

    if array1.ndim == 2:
        # array based melcd calculation
        diff = array1 - array2
        mcd = 10.0 / np.log(10) \
            * np.mean(np.sqrt(2.0 * np.sum(diff ** 2, axis=1)))
    elif array1.ndim == 1:
        diff = array1 - array2
        mcd = 10.0 / np.log(10) * np.sqrt(2.0 * np.sum(diff ** 2))
    else:
        raise ValueError("Dimension mismatch")

    return mcd


# 对两个特征序列进行dwt配准利用 melcd 作为度量距离
def estimate_twf(orgdata, tardata, distance='melcd'):
   
    if distance == 'melcd':
        def distance_func(x, y): return melcd(x, y)
    else:
        raise ValueError('other distance metrics than melcd does not support.')
    
    _, path = fastdtw(orgdata, tardata, dist=distance_func)
    twf = np.array(path).T
    
    return twf


# 对一对语音的特征进行配准
# odata  tdata 源特征 以及目标特征
# onpow  tnpow opow=-20, tpow=-20  源能量 以及 目标能量 利用其对源/目标特征进行筛选，去掉静音帧
# sd 特征的起始位置 例如： sd=1 表示去掉第0维， 根据其他维进行配准
# cvdata 进行了转换后的源特征  当进行第二轮配准时用其与目标特征进行配准
# 
def get_alignment(odata, onpow, tdata, tnpow, opow=-20, tpow=-20,
                  sd=0, cvdata=None,distance='melcd'):

    # 根据源特征进行处理（去掉第一维度，增加delta，根据能量去静音）
    oexdata = extsddata(odata[:, sd:], onpow,
                        power_threshold=opow)
    # 根据能量阈值对目标特征进行筛选                    
    texdata = extsddata(tdata[:, sd:], tnpow,
                        power_threshold=tpow)
    
    # 源特征的的转换特征不存在则用源特征进行配准
    # 源特征的的转换特征 存在 则用源特征的转换特征 进行配准
    if cvdata is None:
        align_odata = oexdata
    else:
        cvexdata = extsddata(cvdata, onpow,
                             power_threshold=opow)
        align_odata = cvexdata
    
    twf = estimate_twf(align_odata, texdata,distance=distance)
    
    # 利用配准关系获取联合特征
    # 注意配准的时候可能使用的使用源转换特征（cvexdata）
    # 但是这里得到的联合特征是源（oexdata）特征与目标特征的联合特征
    jdata = align_data(oexdata, texdata, twf)
    
    # 计算匹配效果 即匹配特征之间的距离
    mcd = melcd(align_odata[twf[0]], texdata[twf[1]])

    return jdata, twf, mcd


def gen_join_features(fea_list1,fea_list2,fea_path,config):
    # 获取 源语音的 mecp 与npow 特征
    org_mceps = []
    org_npows = []
    for fea in fea_list1:
        feature = np.load(os.path.join(fea_path,fea),allow_pickle=True).item()
        org_mceps.append(feature["mcep"])
        org_npows.append(feature["npow"])
       
    # 获取 目标语音的mecp 与 npower 特征    
    tar_mceps = []
    tar_npows = []
    for fea in fea_list2:
        feature = np.load(os.path.join(fea_path,fea),allow_pickle=True).item()
        tar_mceps.append(feature["mcep"])
        tar_npows.append(feature["npow"])
    
    '''进行第一次配准 获取联合特征jnt_data'''
    sd = config["sd"]
    twfs, jfvs = [], []
    print("The first DTW")
    for omcep,onpow,tmcep,tnpow in tqdm(zip(org_mceps,org_npows,tar_mceps,tar_npows),total = len(org_mceps)): 
        # 进行配准
        jdata, twf, mcd = get_alignment(omcep, onpow, tmcep, tnpow, opow=-20, tpow=-20,
                  sd=sd, cvdata=None)
        twfs.append(twf)
        jfvs.append(jdata)
    jnt_data = np.concatenate(jfvs,axis=0)
    
    # 利用联合特征训练一个GMM
    datagmm1 = GMMTrainer(n_mix=config["n_mix"],n_iter=config["n_iter"])
    datagmm1.train(jnt_data)
    
    # 利用这个GMM推导一个特征转换器 这里使用的是较为简单的 Normal JD-GMM
    cvgmm1 = GMMConvertor(n_mix=config["n_mix"])
    cvgmm1.open_from_param(datagmm1.param)
    
    
    ''' 进行第二次配准，这次使用上一次配准获取的cvgmm对源特征进行转换 然后再进行配准 '''
    print("The second DTW")
    twfs, jfvs = [], []
    for omcep,onpow,tmcep,tnpow in tqdm(zip(org_mceps,org_npows,tar_mceps,tar_npows),total = len(org_mceps)):
        # 先进行转换再进行配准
        cvdata = cvgmm1.convert(static_delta(omcep[:, sd:]),cvtype=config["cvtype"])
        
        jdata, twf, mcd = get_alignment(omcep, onpow, tmcep, tnpow, opow=-20, tpow=-20,
                  sd=sd, cvdata=cvdata,distance='melcd')
        twfs.append(twf)
        jfvs.append(jdata)
    
    jnt_data = np.concatenate(jfvs,axis=0)
    
    # 利用联合特征训练一个GMM
    datagmm2 = GMMTrainer(n_mix=config["n_mix"],n_iter=config["n_iter"])
    datagmm2.train(jnt_data)
    
    # 利用这个GMM推导一个特征转换器
    cvgmm2 = GMMConvertor(n_mix=config["n_mix"])
    cvgmm2.open_from_param(datagmm2.param)
    
    
    ''' 进行第三次配准，这次使用上一次配准获取的cvgmm对源特征进行转换 然后再进行配准 '''
    print("The third DTW")
    twfs, jfvs = [], []
    for omcep,onpow,tmcep,tnpow in tqdm(zip(org_mceps,org_npows,tar_mceps,tar_npows),total=len(org_mceps)):
        
        # 先进行转换再进行配准
        cvdata = cvgmm2.convert(static_delta(omcep[:, sd:]),cvtype=config["cvtype"])
        
        jdata, twf, mcd = get_alignment(omcep, onpow, tmcep, tnpow, opow=-20, tpow=-20,
                  sd=sd, cvdata=cvdata, distance='melcd')
       
        twfs.append(twf)
        jfvs.append(jdata)
    
    # 得到最终的 jnt_mcep 特征
    jnt_mcep_data = np.concatenate(jfvs,axis=0)
    
    return jnt_mcep_data
    
    
        
        

    
    
    
    
    