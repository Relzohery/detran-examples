#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:26:02 2020

@author: rabab
"""


import numpy as np
from pod import U_fd, U_r
import matplotlib.pyplot as plt
fname = '/home/rabab/opt/detran/build/solvers/energyIndependent_operator'



with open(fname, "rb") as g:
    data = np.fromfile(g, dtype='>f8', count=-1)
    

size = data.shape[0]
n = 140
A = data[size - n*n:].reshape(n, n)

eigs, vecs = np.linalg.eig(A)


# projection

A_r = U_fd.T.dot(A).dot(U_fd)
eigs_r, vecs_r = np.linalg.eig(A_r)

vecs_recons = U_fd.dot(vecs_r)

#%%


fname2 = '/home/rabab/opt/detran/build/solvers/EnergyDependent_Operator'

mat2 = np.fromfile(fname2)

offset = mat.shape[0] - 140*140
#mat = mat[offset :].reshape(140, 140)

mat = mat[ :140*140].reshape(140,140)


Ar = U_fd.T.dot(mat.dot(U_fd))



offset2 = mat2.shape[0] - 280*280
mat2 = mat2[offset2 :].reshape(2*140, 2*140)


Ar2 = U_r.T.dot(mat2.dot(U_r))


fname3 = '/home/rabab/opt/detran/build/solvers/A_diffusion_Operator'
mat3 = np.fromfile(fname3)
offset = mat3.shape[0] - 2*2*140*140
mat3 = mat3[offset :].reshape(2*140, 2*140)

Ar3 = U_r.T.dot(mat3.dot(U_r))


fname4 = '/home/rabab/opt/detran/build/solvers/B_diffusion_Operator'
mat4 = np.fromfile(fname4)
offset = mat4.shape[0] - 2*2*140*140
mat4 = mat4[offset :].reshape(2*140, 2*140)

Ar4 = U_r.T.dot(mat4.dot(U_r))


#%%

fname5 = '/home/rabab/opt/detran/build/solvers/test/EnergyIndependentEigenOperator'
mat5 = np.fromfile(fname5)
offset = mat5.shape[0] - 20*20
mat4 = mat5[offset :].reshape(20,20)


with open(fname5, "rb") as g:
    data = np.fromfile(g, dtype='>f8', count=-1)
    
    
size = data.shape[0]
A = data[size - 20*20:].reshape(20, 20)