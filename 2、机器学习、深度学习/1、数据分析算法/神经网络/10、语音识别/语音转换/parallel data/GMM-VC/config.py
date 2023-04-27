config_all={
    "path_fea":"data/",
    "path_model":"model/",
    
    "Feature":{   
    "fs": 22050,
    "minf0":40,
    "maxf0":700, 
    "shiftms":4.988662131519274,
    "fftl":1024,
    # mecp 部分
    "dim_mcep":34, 
    "alpha" :0.455   
    },
    
    "GMM-mcep":{
    "sd":1,
    "n_mix": 32,
    "n_iter": 100,
    "cvtype": "mlpg",
    },
   
    "GV_morph_coeff": 1.0
}