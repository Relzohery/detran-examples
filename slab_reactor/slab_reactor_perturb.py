# pyexamples/slab_reactor/slab_reactor.py
#
# This implements the test cases published in Scott Mosher's
# Ph.D. thesis, "A Variational Coarse Mesh Transport Method".
# All data and reference values are from Appendix A of that 
# work.
#
#   Core     keff
#   =====   =========
#     1     1.258247 
#     2     1.007066 
#     3     0.805372
#
# These results are based on a 32-point Gauss-Legendre,
# 2 meshes per water region, 4 meshes per fuel region.
#
# Note, the assembly kinf's were found using the same
# parameters to be 
#
#   Assembly     kinf
#   ========   =========
#      A       1.329576914
#      B       1.298737436
#      C       0.681362819
#      D       0.191909997

from detran import *
import slab_reactor_materials
import slab_reactor_geometry
import time
import pickle
np.random.seed(1234)


def run(data, equation = 'transport') :

  #------------------------------------------------------------------------------#
  # Initialize
  #------------------------------------------------------------------------------#

  Manager.initialize(sys.argv)

  #------------------------------------------------------------------------------#
  # Input
  #------------------------------------------------------------------------------#

  inp = InputDB.Create()
  inp.put_str("problem_type",               "eigenvalue")
  inp.put_int("number_groups",              2)
  inp.put_str("equation",                   "dd")
  inp.put_str("inner_solver",               "SI")
  inp.put_int("inner_max_iters",            1000)
  inp.put_dbl("inner_tolerance",            1e-7)
  inp.put_int("inner_print_level",          0)
  inp.put_str("outer_solver",               "GMRES")
  inp.put_int("outer_max_iters",            1000)
  inp.put_dbl("outer_tolerance",            1e-7)
  inp.put_int("outer_print_level",          0)
  inp.put_str("eigen_solver",               "arnoldi")
  inp.put_int("eigen_max_iters",            200)
  inp.put_dbl("eigen_tolerance",            1e-7)
  inp.put_str("bc_west",                    "vacuum")
  inp.put_str("bc_east",                    "vacuum")
  inp.put_str("quad_type",                  "gl")
  inp.put_int("quad_number_polar_octant",   16)

  
  # Mesh
  #------------------------------------------------------------------------------#

  # Options are: assemblyX for X=0,1,2,3 or coreX for X=0,1,2
  mesh = slab_reactor_geometry.get_mesh("core0")


  if equation == "transport":  
      fname = "results_core0_transport";
          
  elif equation == "diffusion":
      inp.put_str("equation",                   "diffusion")
      fname = "results_core0_diff"
        

  mat = slab_reactor_materials.get_materials(data)
  mat.display()
             
    
  #------------------------------------------------------------------------------#
    
  #------------------------------------------------------------------------------#
  # Solve
  #------------------------------------------------------------------------------#
    
  start = time.time()
  solver = Eigen1D(inp, mat, mesh)
  solver.solve()
  elapsed = (time.time() - start)
  print elapsed, " seconds"
  
  keff = solver.state().eigenvalue()
  
  fission_den = solver.fissionsource().density()
  fission_density_sample = []
          
  flux_0 = solver.state().phi(0)
  flux_0_sample = []
          
  flux_1 = solver.state().phi(1)
  flux_1_sample = []
  
          
  for i in range(len(fission_den)):
      fission_density_sample.append(fission_den[i])          
          
  for i in range(len(flux_0)):
      flux_0_sample.append(flux_0[i])
      flux_1_sample.append(flux_1[i])
              
 
   
           
  return keff, fission_density_sample, flux_0_sample, flux_1_sample
  


if __name__ == "__main__":
  values = [0.1890, 1.4633, 0.1507, 0.0161, 1.4536, 0.2263,  1.0119, 0.0067, 0.1241, 0.2006, 0.0161,0.9355, 0.2252, 0.9915, 0.0078 ,
          0.1241,0.1995, 0.0156,0.9014, 0.2173, 1.0606, 0.0056, 0.018, 0.1902,0.0136 ,0.5733 ]
  Manager.initialize(sys.argv)
  run(values,  equation = 'diffusion')