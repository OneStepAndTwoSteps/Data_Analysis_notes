from feature import featureExtractor
import numpy as np
from tqdm import tqdm
import os 
from config import config_all
from statistics import generate_statistics_feature,GV_estimate
from jointfeature import gen_join_features,static_delta
import joblib
from model import GMMTrainer,GMMConvertor,f0_convert,GV_postfilter,synthesis
from scipy.io import wavfile


def feature_collect(spk, files, config,feature_path):
    for file in tqdm(files, total = len(files)):
        # 计算WAV的特征
        f0, mcep, npow ,ap = featureExtractor(file,config)
        # 以字典的形式保存
        feature = {}
        feature["f0"] = f0
        feature["mcep"] = mcep
        feature["npow"] = npow
        file_name = spk + "_" +file.split("/")[-1].split(".")[0] + ".npy"
        np.save(os.path.join(feature_path,file_name),feature)
        
# 测试程序    
if __name__ == "__main__":        
    
    # 读取 训练语音对
    pair_scp = "scp/train_pair_0.scp"
    with open(pair_scp,'r') as f:
        lines = f.read().splitlines()
    lines = [line.split() for line in lines]
        
    spk1 = np.unique(np.array([line[0] for line in lines]))[0]
    spk2 = np.unique(np.array([line[2] for line in lines]))[0]
    print(spk1)
    print(spk2)
    files_spk1 = [line[1] for line in lines]
    files_spk2 = [line[3] for line in lines]
    
    
    ''' 第一步 进行数据特征采集'''
    print("step 1 feature collect")
    feature_path = config_all["path_fea"]
    os.makedirs(feature_path,exist_ok=True)
    # 对spk1的特征进行采集 
    feature_collect(spk1, files_spk1,config_all["Feature"],feature_path)
    # 对spk2的特征进行采集
    feature_collect(spk2, files_spk2,config_all["Feature"],feature_path)
  
    ''' 第二步  对spk进行统计特征计算 '''
    print("step 2 compute static information")
    static_path = config_all["path_model"]
    os.makedirs(static_path,exist_ok=True)
    spks = [spk1, spk2]
    files_spks = [files_spk1,files_spk2]
    feature_path = config_all["path_fea"]
    for spk,files in zip(spks,files_spks):
        list_fea = [os.path.join(feature_path,spk + "_" +file.split("/")[-1].split(".")[0] + ".npy") for file in files]
        f0stats,gvstats = generate_statistics_feature(list_fea)
        fea_static = {}
        fea_static["f0stats"] = f0stats
        fea_static["gvstats"] = gvstats
        save_name = os.path.join(static_path,spk+'.npy')
        np.save(save_name,fea_static)
     
    ''' 第三步 进行特征的强制对齐生成mecp特征对 '''
    print("step 3 get joint mcep feature")
    fea_file_list_spk1 = [spk1 + "_" +file.split("/")[-1].split(".")[0] + ".npy" for file in files_spk1]
    fea_file_list_spk2 = [spk2 + "_" +file.split("/")[-1].split(".")[0] + ".npy" for file in files_spk2]
        
    feature_path = config_all["path_fea"]
    jnt_mcep_data = gen_join_features(fea_file_list_spk1,
                                      fea_file_list_spk2,
                                      feature_path, 
                                      config_all["GMM-mcep"])
    
    np.save(os.path.join(feature_path,"jnt_mecp_data.npy"),jnt_mcep_data)
    
    ''' 第四步 利用获取的对齐特征训练 mcep GMM  并保存 '''
    print("step 4 train GMM model")
    # 加载联合特征
    feature_path = config_all["path_fea"]
    jnt_mcep_data = np.load(os.path.join(feature_path,"jnt_mecp_data.npy"))
    
    model_path = config_all["path_model"]
    os.makedirs(model_path,exist_ok=True)
    
    # 利用联合特征训练GMM 并保存
    mecp_GMM_config = config_all["GMM-mcep"]
    gmm_mecp = GMMTrainer(n_mix=mecp_GMM_config["n_mix"] ,
                          n_iter=mecp_GMM_config["n_iter"])
    gmm_mecp.train(jnt_mcep_data)
    joblib.dump(gmm_mecp.param, os.path.join(model_path,"gmm_mecp.pkl"))
    print("Save gmm_mecp")
    

    ''' 第5步 利用训练好的 GMM 构建特征转换器 GMMConvertor
        对训练用的源特征进行进行转换，并计算转换后的特征的方差的统计特征
    '''
    print("step 5 computr static information of trained convered features")
    
    # 创建 GMM特征转换器
    mecp_GMM_config = config_all["GMM-mcep"]
    mecp_convertor = GMMConvertor(n_mix=mecp_GMM_config["n_mix"])
    
    # 载入训练好的 GMM
    model_path = config_all["path_model"]
    param = joblib.load(os.path.join(model_path,"gmm_mecp.pkl"))
    mecp_convertor.open_from_param(param)
    
    # 对源特征进行逐一转换
    fea_file_list_spk1 = [spk1 + "_" +file.split("/")[-1].split(".")[0] + ".npy" for file in files_spk1]
    sd = mecp_GMM_config["sd"]
    cv_mceps =[]
    feature_path = config_all["path_fea"]
    for file in fea_file_list_spk1:
        feature = np.load(os.path.join(feature_path,file),allow_pickle=True).item()
        mcep = feature["mcep"]
        mcep_0th = mcep[:, 0]
        cvmcep = mecp_convertor.convert(static_delta(mcep[:, sd:]),
                               cvtype=mecp_GMM_config["cvtype"])
        cvmcep = np.c_[mcep_0th, cvmcep]
        cv_mceps.append(cvmcep)
    
    # 获取转换特征的方差的统计量，并保存   
    cvgvstats = GV_estimate(cv_mceps)
    model_path = config_all["path_model"]
    save_name = os.path.join(model_path,spk1+"2"+spk2+"_cvgvstats"+".npy")
    np.save(save_name,cvgvstats)
    
    '''
        第六步 进行语音转换
    '''
    print("step 6 conver a wav file")
   # 创建 GMM特征转换器
    mecp_GMM_config = config_all["GMM-mcep"]
    mecp_convertor = GMMConvertor(n_mix=mecp_GMM_config["n_mix"])
    
    # 载入训练好的 GMM
    model_path = config_all["path_model"]
    param = joblib.load(os.path.join(model_path,"gmm_mecp.pkl"))
    mecp_convertor.open_from_param(param)
    
    static_path = config_all["path_model"]
    # 加载源语音的f0统计信息
    org_static = np.load(os.path.join(static_path,spk1+".npy"),allow_pickle=True).item()
    orgf0stats = org_static["f0stats"]
   
    # 记载目标语音f0的统计信息
    tar_static = np.load(os.path.join(static_path,spk2+".npy"),allow_pickle=True).item()
    tarf0stats = tar_static["f0stats"]
    targvsats = tar_static["gvstats"]
    
    # 加载转换语音的GV信息
    cvgvstats = np.load(os.path.join(static_path,spk1+"2"+spk2+"_cvgvstats"+".npy"))
    
    # 需要转换的音频文件
    org_wav = "/home/sdh/dataset/vcc2018/vcc2018_dev/VCC2SF1/10080.wav"
    # 进行特征提取
    f0, mcep, npow ,ap = featureExtractor(org_wav,config_all["Feature"])
    mcep_0th = mcep[:, 0]
    
    # 进行F0的转换 F0
    cvf0 = f0_convert(f0, orgf0stats, tarf0stats)
    
    # 进行 mcep 的转换
    cvmcep_wopow = mecp_convertor.convert(static_delta(mcep[:, 1:]),
                                           cvtype=mecp_GMM_config["cvtype"])
    cvmcep = np.c_[mcep_0th, cvmcep_wopow]
    
    # 利用GV 修正 mcep
    cvmcep_wGV = GV_postfilter(cvmcep,
                               targvsats,
                               cvgvstats=cvgvstats,
                               alpha=config_all["GV_morph_coeff"],
                               startdim=1)
                                   
    # 语音合成
    wav = synthesis(cvf0,cvmcep_wGV,ap,config_all["Feature"])
    
    wav = np.clip(wav, -32768, 32767)
    wavfile.write("conv.wav", config_all["Feature"]["fs"], wav.astype(np.int16))
  
    
        
    
    
    
    
    
    
    
    
    