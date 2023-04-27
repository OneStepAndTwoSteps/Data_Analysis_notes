import pysptk
import pyworld
import numpy as np
from scipy.io import wavfile
from config import config_all
from scipy.signal import firwin, lfilter

# 高通滤波 去掉70hz以下的部分
def low_cut_filter(x, fs, cutoff=70):
   
    nyquist = fs // 2
    norm_cutoff = cutoff / nyquist

    # low cut filter
    fil = firwin(255, norm_cutoff, pass_zero=False)
    lcf_x = lfilter(fil, 1, x)

    return lcf_x
    
# 计算能量
def spc2npow(spectrogram):
    # frame based processing
    npow = np.apply_along_axis(_spvec2pow, 1, spectrogram)
    meanpow = np.mean(npow)
    npow = 10.0 * np.log10(npow / meanpow)
    return npow

# 计算每一帧的能量
def _spvec2pow(specvec):
    # set FFT length
    fftl2 = len(specvec) - 1
    fftl = fftl2 * 2

    # specvec is not amplitude spectral |H(w)| but power spectral |H(w)|^2
    power = specvec[0] + specvec[fftl2]
    for k in range(1, fftl2):
        power += 2.0 * specvec[k]
    power /= fftl
    return power

def featureExtractor(wav_file,config):
    # 读取音频文件
    fs, x = wavfile.read(wav_file)
    if not fs==config["fs"]:
        print("WARNING: fs values are not ",config["fs"])
    
    x = np.array(x, dtype=np.float)
    # 进行高通滤波，去掉70hz以下的成分
    x = low_cut_filter(x, fs, cutoff=70)
    
    # 利用Pyworld 提取f0 spc ap 特征
    f0, time_axis = pyworld.harvest(x, fs, f0_floor=config["minf0"],
                                    f0_ceil=config["maxf0"], 
                                    frame_period=config["shiftms"])
    spc = pyworld.cheaptrick(x, f0, time_axis, fs,
                             fft_size=config["fftl"])
    ap = pyworld.d4c(x, f0, time_axis, fs, fft_size=config["fftl"])
    
    # 对 f0 进行分析
    f0[f0 < 0] = 0
    if np.sum(f0) == 0.0:
        print("WARNING: F0 values are all zero.")
    
    # 获取MFCC特征cd 
    mcep = pysptk.sp2mc(spc, config["dim_mcep"], config["alpha"])

    # 获取能量特征
    npow = spc2npow(spc)
    return f0, mcep, npow ,ap

# 测试程序    
if __name__ == "__main__":
    wav_file = "/home/sdh/dataset/vcc2018/vcc2018_train/VCC2SF1/10001.wav"
    f0, mcep, npow ,codeap =featureExtractor(wav_file,config_all["Feature"])
    print(f0.shape)
    print(mcep.shape)
    print(npow.shape)
    print(codeap.shape)
    


    
    


    
    
    