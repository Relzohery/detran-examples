#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:19:04 2020

@author: rabab
"""


import numpy as np
import matplotlib.pylab as plt

import pickle

tr_results_core0 = pickle.load(open("results_core0_transport.p", "rb"))


flux0 = tr_results_core0['flux_0']
flux1 = tr_results_core0['flux_1']

fission_density = tr_results_core0['fission_density']


r = 12

U1, S1, V = np.linalg.svd(flux0) 
U1 = U1[:, :r]



U2, S2, V = np.linalg.svd(flux1) 
U2 = U2[:, :r]


n = flux0.shape[0]
U_r = np.zeros((n*2, 2*r))

U_r[:n, :r] = U1[:, :r]
U_r[n: , r:] = U2[:, :r]

U_fd, S, V = np.linalg.svd(fission_density) 
U_fd = U_fd[:, :r]


U_bin = bytearray(U_r)

U_fd_bin = bytearray(U_fd)

with open('/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_transport_r=12', 'wb') as f:
    f.write(U_bin)
    
    
with open('/home/rabab/opt/detran/source/src/solvers/test/fission_density_core0_transport_r=12', 'wb') as f:
    f.write(U_fd_bin)


#%% diffusion
    
r = 12
diff_results_core0 = pickle.load(open("results_core0_diff.p", "rb"))


flux0 = diff_results_core0['flux_0']
flux1 = diff_results_core0['flux_1']

fission_density = diff_results_core0['fission_density']



U1, S1, V = np.linalg.svd(flux0) 
U1 = U1[:, :r]



U2, S2, V = np.linalg.svd(flux1) 
U2 = U2[:, :r]


n = flux0.shape[0]
U_r = np.zeros((n*2, 2*r))

U_r[:n, :r] = U1[:, :r]
U_r[n: , r:] = U2[:, :r]

U_bin = bytearray(U_r)


with open('/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_diff_r=12', 'wb') as f:
    f.write(U_bin)