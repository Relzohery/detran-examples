#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:56:39 2020

@author: rabab
"""

import numpy as np
import pickle

np.random.seed(1000)

xs_data = {'mat1': {'sigma_t': [0.1890, 1.4633], 'sigma_f': [0.0, 0.0], 'chi':[0, 0], 'sigma_s':[0.1507, 0.0000, 0.0161, 1.4536]},
           'mat2': {'sigma_t': [ 0.2263, 1.0119 ], 'sigma_f': [0.0067  , 0.1241 ], 'chi':[1,0], 'sigma_s':[0.2006, 0.0, 0.0161,0.9355]}, 
           'mat3': {'sigma_t': [0.2252, 0.9915], 'sigma_f': [0.0078, 0.1241], 'chi':[1, 0], 'sigma_s':[0.1995, 0.0, 0.0156,0.9014]}, 
           'mat4': {'sigma_t': [ 0.2173, 1.0606], 'sigma_f': [ 0.0056, 0.0187 ], 'chi':[1,0 ], 'sigma_s':[ 0.1902,0.0,0.0136 ,0.5733]}
           }




values = [0.1890, 1.4633, 0.1507, 0.0161, 1.4536, 0.2263,  1.0119, 0.0067, 0.1241, 0.2006, 0.0161,0.9355, 0.2252, 0.9915, 0.0078 ,
          0.1241,0.1995, 0.0156,0.9014, 0.2173, 1.0606, 0.0056, 0.018, 0.1902,0.0136 ,0.5733 ]

samples = {}

#perturn all cross section, assuming 2% uniform random distribution
for i in range(100):
    samples[i] = []
    for v in values:
        samples[i].append(np.random.uniform(v*(1-0.02), v*(1+0.02)))
        
        
with open('material_samples.p', 'wb') as f:
    pickle.dump(samples, f)
        
    


