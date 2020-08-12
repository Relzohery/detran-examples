# pyexamples/slab_reactor/slab_reactor_materials.py
#
# This implements the materials for the test cases published 
# in Scott Mosher's Ph.D. thesis, "A Variational Coarse Mesh 
# Transport Method". All data and reference values are from 
# Appendix A of that work.

from detran import *


def get_materials(data) :
    # Two-group data from 1-d coarse mesh benchmarks (Mosher, Ilas etc.)
        
    # Create the Materials object.
    mat = Material.Create(4, 2, "slabreactor");

    # ---------------------------
    # Material 0: Water           
    # ---------------------------

    # Total
    mat.set_sigma_t(0, 0, data[0]);       # (obj, matid, g, value);
    mat.set_sigma_t(0, 1,  data[1]);       

    # Fission 
    mat.set_sigma_f(0, 0, 0.0);         # Note, default is zero
    mat.set_sigma_f(0, 1, 0.0);   
    mat.set_chi(0, 0, 0.0); 
    mat.set_chi(0, 1, 0.0);        

    # Scattering
    mat.set_sigma_s(0, 0, 0,  data[2]);    # 1 <- 1
    mat.set_sigma_s(0, 0, 1, 0.0000);    # 1 <- 2
    mat.set_sigma_s(0, 1, 0,  data[3]);    # 2 <- 1
    mat.set_sigma_s(0, 1, 1,  data[4]);    # 2 <- 2
    mat.compute_diff_coef();

    # ---------------------------
    # Material 1: Fuel I           
    # ---------------------------

    # Total
    mat.set_sigma_t(1, 0,  data[5]);       # (obj, matid, g, value);
    mat.set_sigma_t(1, 1,  data[6]);       

    # Fission 
    mat.set_sigma_f(1, 0,  data[7]);
    mat.set_sigma_f(1, 1,  data[8]);   
    mat.set_chi(1, 0, 1.0); 
    mat.set_chi(1, 1, 0.0);        

    # Scattering
    mat.set_sigma_s(1, 0, 0,  data[9]);    # 1 <- 1
    mat.set_sigma_s(1, 0, 1, 0.0000);    # 1 <- 2
    mat.set_sigma_s(1, 1, 0,  data[10]);    # 2 <- 1
    mat.set_sigma_s(1, 1, 1,  data[11]);    # 2 <- 2
    mat.compute_diff_coef();

    # ---------------------------
    # Material 3: Fuel II          
    # ---------------------------

    # Total
    mat.set_sigma_t(2, 0,  data[12]);       # (obj, matid, g, value);
    mat.set_sigma_t(2, 1,  data[13]);       

    # Fission 
    mat.set_sigma_f(2, 0,  data[14]);
    mat.set_sigma_f(2, 1,  data[15]);   
    mat.set_chi(2, 0, 1.0); 
    mat.set_chi(2, 1, 0.0); 

    # Scattering
    mat.set_sigma_s(2, 0, 0,  data[16]);    # 1 <- 1
    mat.set_sigma_s(2, 0, 1, 0.0000);    # 1 <- 2
    mat.set_sigma_s(2, 1, 0,  data[17]);    # 2 <- 1
    mat.set_sigma_s(2, 1, 1,  data[18]);    # 2 <- 2
    mat.compute_diff_coef();       


    # ---------------------------
    # Material 4: Fuel II + Gd          
    # ---------------------------
    
    # Total
    mat.set_sigma_t(3, 0,  data[19]);       # (obj, matid, g, value);
    mat.set_sigma_t(3, 1,  data[20]);       

    # Fission 
    mat.set_sigma_f(3, 0,  data[21]);
    mat.set_sigma_f(3, 1,  data[22]);   
    mat.set_chi(3, 0, 1.0); 
    mat.set_chi(3, 1, 0.0);        

    # Scattering
    mat.set_sigma_s(3, 0, 0,  data[23]);	  # 1 <- 1
    mat.set_sigma_s(3, 0, 1, 0.0000);    # 1 <- 2
    mat.set_sigma_s(3, 1, 0,  data[24]);    # 2 <- 1
    mat.set_sigma_s(3, 1, 1,  data[25]);    # 2 <- 2
    mat.compute_diff_coef();       


    # ---------------------------
    # FINALIZE     
    # ---------------------------

    mat.finalize();

    return mat