#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:19:04 2020

@author: rabab
"""


import numpy as np
import matplotlib.pylab as plt

import pickle

tr_results_core0 = pickle.load(open( "c5g7_assem0_transport.p", "rb"))




flux0 = tr_results_core0['flux_0'].T
flux1 = tr_results_core0['flux_1'].T
flux2 = tr_results_core0['flux_2'].T
flux3 = tr_results_core0['flux_3'].T
flux4 = tr_results_core0['flux_4'].T
flux5 = tr_results_core0['flux_5'].T
flux6 = tr_results_core0['flux_6'].T

fission_density = tr_results_core0['fission_density'].T


r = 20

U1, S1, V = np.linalg.svd(flux0) 
U1 = U1[:, :r]


U2, S2, V = np.linalg.svd(flux1) 
U2 = U2[:, :r]


U3, S3, V3 = np.linalg.svd(flux2) 
U3 = U3[:, :r]


U4, S4, V = np.linalg.svd(flux3) 
U4 = U4[:, :r]

U5, S5, V = np.linalg.svd(flux4) 
U5 = U5[:, :r]

U6, S6, V = np.linalg.svd(flux5) 
U6 = U6[:, :r]

U7, S7, V = np.linalg.svd(flux6) 
U7 = U7[:, :r]



G = 7
n = flux0.shape[0]
U_r = np.zeros((n*G, G*r))

U_r[:n, :r] = U1
U_r[n:2*n , r:2*r] = U2
U_r[2*n:3*n , 2*r:3*r] = U3
U_r[3*n:4*n , 3*r:4*r] = U4
U_r[4*n:5*n , 4*r:5*r] = U5
U_r[5*n:6*n, 5*r:6*r] = U6
U_r[6*n:7*n , 6*r:7*r] = U7





U_fd, S, V = np.linalg.svd(fission_density) 
U_fd = U_fd[:, :r]


U_bin = bytearray(U_r)

U_fd_bin = bytearray(U_fd)

with open('/home/rabab/opt/detran/source/src/solvers/test/flux_basis_assem0_transport_c5g7_r=20', 'wb') as f:
    f.write(U_bin)
    
    
with open('/home/rabab/opt/detran/source/src/solvers/test/fission_density_assem0_transport_c5g7_r=20', 'wb') as f:
    f.write(U_fd_bin)


