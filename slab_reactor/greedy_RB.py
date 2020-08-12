#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:00:07 2020

@author: rabab
"""

from detran_test import s_setting, s_test
import numpy as np
from slab_reactor_perturb import run
import pickle
import scipy
import os



 
fname = '/home/rabab/opt/detran/source/src/solvers/test/projection_fixture.hh'


# refernce point
values = [0.1890, 1.4633, 0.1507, 0.0161, 1.4536, 0.2263,  1.0119, 0.0067, 0.1241, 0.2006, 0.0161,0.9355, 0.2252, 0.9915, 0.0078 ,
          0.1241,0.1995, 0.0156,0.9014, 0.2173, 1.0606, 0.0056, 0.018, 0.1902,0.0136 ,0.5733 ]

k_ref, fd_ref, flux0_ref, flux1_ref = run(values,  equation = 'transport')



# material perturbation
data_samples = pickle.load(open('material_samples.p', 'rb'))


# 1- get 50 samples for training
samples = 100

keff_samples = []   
fd_samples = []
for sample in range(samples):
    data = data_samples[sample]
    k, fd, flux0, flux1 = run(data,  equation = 'transport')
    fd_samples.append(fd)
    keff_samples.append(k)
    
def run_detran ():

    os.chdir("/home/rabab/opt/detran/build/solvers/test")
    os.system("make test_ROMSolver")
    os.chdir("/home/rabab/opt/detran/build/solvers")
    os.system("./test/test_ROMSolver 1 > '/home/rabab/Desktop/results'")
    lines = open('/home/rabab/Desktop/results').readlines()
    for line in lines:
        if 'the error norm in the fission density = ' in line:
         error = float(line.split('=')[1])
    return error

def  write_test(data):
    g = s_setting.format(*data)
    with open (fname, 'w') as f:
        f.write(g)
    

samples  = {'data' : data_samples, 'fission_density': fd_samples}   
with open('fission_density_samples.p', 'wr') as f:
    pickle.dump(samples, f)

#%% greedy 
    
N = 10
tol = 1E-3
samples = 50
# initilize the reduced space with two vectors and orthonormalize
U = fd_samples[: 2]
U = np.array(U).T
U_ortho = np.linalg.qr(U)[0]

taken = []
for i in range(2, N):
    # compute the error at th referenc point       
    U_bin = bytearray(U_ortho)
    basis_fname = '/home/rabab/opt/detran/source/src/solvers/test/fission_density_RB_basis_core0_transport_r={}'.format(i)
    with open(basis_fname, 'wb') as f:
        f.write(U_bin)

    g_test = s_test.format(i, basis_fname)
    with open('/home/rabab/opt/detran/source/src/solvers/test/test_ROMSolver.cc', 'w') as f:
        f.write(g_test)
    write_test(values)
    error = run_detran()
    print error
        
    if error > tol:
        sample_errs = []
        for i in range(samples):
            write_test(data_samples[i])
            sample_errs.append(run_detran())
        worst = sample_errs.index(max(sample_errs))
        print worst
        worst_fd =  np.array(fd_samples[worst])[:, None]
        taken.append(worst)
            
        U_ortho = np.hstack((U_ortho, worst_fd))
        U_ortho = np.linalg.qr(U_ortho)[0]

    





    
    