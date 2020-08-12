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

with open('/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_transport_r={}'.format(r), 'wb') as f:
    f.write(U_bin)
    
    
with open('/home/rabab/opt/detran/source/src/solvers/test/fission_density_core0_transport_r={}'.format(r), 'wb') as f:
    f.write(U_fd_bin)
    
    
    
### energyIndependent operator #############
    
    
    
fname = '/home/rabab/opt/detran/build/solvers/energyIndependent_operator'
with open(fname, "rb") as g:
    data = np.fromfile(g, dtype='>f8', count=-1)
    
size = data.shape[0]
n = 140
A = data[size - n*n:].reshape(n, n)

eigs, vecs = np.linalg.eig(A)

keff_err = []
vec_err = []

vecs_rom = []

        
if np.any(np.sign(vecs[:, 0])):
    vecs[:, 0] *= -1

for r in range(2, 20):
    
    U_fd, S, V = np.linalg.svd(fission_density) 
    U_fd = U_fd[:, :r]
    
    A_r = U_fd.T.dot(A).dot(U_fd)
    eigs_r, vecs_r = np.linalg.eig(A_r)  
    vecs_recons = U_fd.dot(vecs_r[:, 0])
    if np.sign( sum(vecs_recons)) ==-1:
        vecs_recons *= -1
  
    keff_err.append(abs(eigs[0] - eigs_r[0]))
    vec_err.append(np.linalg.norm(vecs[:, 0] - vecs_recons))
    



#%% Energy Dependent ############
fname_A = '/home/rabab/opt/detran/build/solvers/A_EnergyDependent_Operator'
fname_B = '/home/rabab/opt/detran/build/solvers/B_EnergyDependent_Operator'

with open(fname_A, "rb") as g:
    A = np.fromfile(g, dtype='>f8', count=-1)

with open(fname_B, "rb") as g:
    B = np.fromfile(g, dtype='>f8', count=-1)
    
    
size = A.shape[0]
 
A = A[size - 4*n*n:].reshape(2*n, 2*n)   
B = B[size - 4*n*n:].reshape(2*n, 2*n)   

C = B.dot(np.linalg.inv(A))


eigs, vecs = np.linalg.eig(C)


U1, S1, V = np.linalg.svd(flux0) 


U2, S2, V = np.linalg.svd(flux1) 



n = flux0.shape[0]

keff_err = []
vec_err = []

for r in range(2, 20):
    U11 = U1[:, :r]
    U22 = U2[:, :r]
    U_r = np.zeros((n*2, 2*r))
    U_r[:n, :r] = U11[:, :r]
    U_r[n: , r:] = U22[:, :r]
    Ar = U_r.T.dot(A).dot(U_r)
    Br = U_r.T.dot(B).dot(U_r)
    eigs_r, vecs_r = np.linalg.eig(Br.dot(np.linalg.inv(Ar)))
    recons_vecs = U_r.dot(vecs_r[:, 0])
    keff_err.append(abs(eigs_r[0] - eigs[0]))
    




#%% diffusion
    

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


with open('/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_diff_r={}'.format(r), 'wb') as f:
    f.write(U_bin)