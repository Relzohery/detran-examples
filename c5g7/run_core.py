# pyexamples/run_core.py
#
# Solves the 2-D C5G7 benchmark problem.
#
# Using 7x7 volume-conserving pin cell, DD SN, and a 3x6 QR quadrature,
# the reference keff is 1.186572165.

import numpy as np
import time
import sys
from detran import *
from core_c5g7 import get_core
from assemblies_c5g7 import get_assemblies
from pins_c5g7 import get_pins
from material_c5g7 import get_materials

def run(perturb =1) :
  #-----------------------------------------------------------------------------#
  # Input 
  #-----------------------------------------------------------------------------#
  inp = InputDB.Create()
  inp.put_str("equation",                       "dd")
  inp.put_str("problem_type",                   "eigenvalue")
  inp.put_int("number_groups",                  7)
  #
  inp.put_str("inner_solver",                   "GMRES")
  inp.put_int("inner_max_iters",                1)
  inp.put_dbl("inner_tolerance",                1e-3)
  inp.put_int("inner_print_level",              0)
  inp.put_int("inner_print_interval",           10)
  #
  inp.put_str("outer_solver",                   "GMRES")
  inp.put_int("outer_max_iters",                0)
  inp.put_dbl("outer_tolerance",                1e-4)
  inp.put_int("outer_print_level",              0)
  inp.put_int("outer_print_interval",           1)
  #
  inp.put_str("eigen_solver",                   "PI")
  inp.put_int("eigen_max_iters",                1000)
  inp.put_dbl("eigen_tolerance",                1e-6)
  inp.put_int("eigen_print_level",              2)
  inp.put_int("eigen_print_interval",           1)
  #
  inp.put_str("bc_west",                        "reflect")
  inp.put_str("bc_east",                        "vacuum")
  inp.put_str("bc_south",                       "reflect")
  inp.put_str("bc_north",                       "vacuum")
  #
 # inp.put_str("quad_type",                      "quadruplerange")
  inp.put_int("quad_number_polar_octant",       3)
  inp.put_int("quad_number_azimuth_octant",     3)
  #
  db = InputDB.Create("callow_db")
  db.put_dbl("linear_solver_atol",              1e-9);
  db.put_dbl("linear_solver_rtol",              1e-9);
  db.put_str("linear_solver_type",              "petsc");
  db.put_int("linear_solver_maxit",             100);
  db.put_int("linear_solver_gmres_restart",     30);
  db.put_int("linear_solver_monitor_level",     0);
  db.put_str("pc_type",                         "petsc_pc");
  db.put_str("petsc_pc_type",                   "lu");
  db.put_str("eigen_solver_type",               "slepc");
  db.put_int("eigen_solver_monitor_level",      2);
  inp.put_spdb("inner_solver_db",               db)
  inp.put_spdb("inner_pc_db",                   db)
  inp.put_spdb("outer_solver_db",               db)
  inp.put_spdb("eigen_solver_db",               db)
  
  # Geometry
  #-----------------------------------------------------------------------------#
  core = get_core(3, True)
  mesh = core.mesh()

  #-----------------------------------------------------------------------------#
  # Material
  #-----------------------------------------------------------------------------#
  
  samples  = 1
  if perturb:
      samples = 2
  k = []
  #flux_0_samples = np.zeros((14161, samples))
  #flux_1_samples = np.zeros((14161, samples))
  #fission_density_samples = np.zeros((14161, samples))
  flux_0_samples = []
  flux_1_samples = []
  flux_2_samples = []
  flux_3_samples = []
  flux_4_samples = []
  flux_5_samples = []
  flux_6_samples = []
  fission_density_samples = []
  
  fname = "c5g7_core0_transport"

  for sample in range(samples):
       mat = get_materials()
    
       # Solve
       #-----------------------------------------------------------------------------#
       start = time.time()
       solver = Eigen2D(inp, mat, mesh)
       solver.solve()
       print "elapsed = ", time.time() - start
       k.append(solver.state().eigenvalue())
       fission_den = solver.fissionsource().density()
       fission_density_sample = []
      
       flux_0 = solver.state().phi(0)
       flux_0_sample = []
        
       flux_1 = solver.state().phi(1)
       flux_1_sample = []
       
       flux_2 = solver.state().phi(1)
       flux_2_sample = []
       
       flux_3 = solver.state().phi(1)
       flux_3_sample = []
       
       flux_4 = solver.state().phi(1)
       flux_4_sample = []
       
       flux_5 = solver.state().phi(1)
       flux_5_sample = []
       
       flux_6 = solver.state().phi(1)
       flux_6_sample = []
        
       print len(flux_0)
        
       for i in range(len(fission_den)):
           fission_density_sample.append(fission_den[i])          
        
       for i in range(len(flux_0)):
           flux_0_sample.append(flux_0[i])
           flux_1_sample.append(flux_1[i])
           flux_2_sample.append(flux_2[i])
           flux_3_sample.append(flux_3[i])
           flux_4_sample.append(flux_4[i])
           flux_5_sample.append(flux_5[i])
           flux_6_sample.append(flux_6[i])
        
       #fission_density_samples[:, sample] = fission_density_sample
       #flux_0_samples[:, sample] = flux_0_sample
       #flux_1_samples[:, sample] = flux_1_sample
       
       fission_density_samples.append(fission_density_sample)
       flux_0_samples.append(flux_0_sample)
       flux_1_samples.append(flux_1_sample)
       flux_2_samples.append(flux_2_sample)
       flux_3_samples.append(flux_3_sample)
       flux_4_samples.append(flux_4_sample)
       flux_5_samples.append(flux_5_sample)
       flux_6_samples.append(flux_6_sample)
       
  fission_density_samples = np.array(fission_density_samples)
  flux_0_samples = np.array(flux_0_samples)
  flux_1_samples = np.array(flux_1_samples)
  flux_2_samples = np.array(flux_2_samples)
  flux_3_samples = np.array(flux_3_samples)
  flux_4_samples = np.array(flux_4_samples)
  flux_5_samples = np.array(flux_5_samples)
  flux_6_samples = np.array(flux_6_samples)
       
        
  data = {'fission_density' : fission_density_samples, 
        'flux_0': flux_0_samples,
        'flux_1': flux_1_samples,
        'flux_2': flux_2_samples,
        'flux_3': flux_3_samples,
        'flux_4': flux_4_samples,
        'flux_5': flux_5_samples,
        'flux_6': flux_6_samples,
        'k_eff': np.array(k)}
  if perturb: 
    
     pickle.dump(data, open(fname + '.p', 'wb'))



if __name__ == "__main__":
  Manager.initialize(sys.argv)
  run()
  Manager.finalize()
  