import numpy as np

# 计算方差的均值和方差
def GV_estimate(datas):
    var = []
    for data in datas:
        var.append(np.var(data, axis=0))

    # calculate vm and vv
    vm = np.mean(np.array(var), axis=0)
    vv = np.var(np.array(var), axis=0)
    gvstats = np.r_[vm, vv]
    gvstats = gvstats.reshape(2, len(vm))
    return gvstats

def generate_statistics_feature(files):
    
    f0s = []
    mceps = []
    for file in files:
        feature = np.load(file,allow_pickle=True).item()
        f0s.append(feature["f0"])
        mceps.append(feature["mcep"])
   
    # 进行f0 的统计
    for i, f0 in enumerate(f0s):
        nonzero_indices = np.nonzero(f0)
        if i == 0:
            f0s = np.log(f0[nonzero_indices])
        else:
            f0s = np.r_[f0s, np.log(f0[nonzero_indices])]
        f0stats = np.array([np.mean(f0s), np.std(f0s)])
    
    # 计算 mcep特征方差的均值与方差  
    gvstats = GV_estimate(mceps)
    
    return f0stats,gvstats
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        