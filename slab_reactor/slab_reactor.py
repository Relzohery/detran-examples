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


def run(perturb=0, equation = 'transport') :

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
    

      
      
  
  
  if perturb:
      samples = 100
      k = []
      flux_0_samples = np.zeros((140, samples))
      flux_1_samples = np.zeros((140, samples))
      fission_density_samples = np.zeros((140, samples))

      if equation == "transport":  
          fname = "results_core0_transport";
          
      elif equation == "diffusion":
        inp.put_str("equation",                   "diffusion")
        fname = "results_core0_diff"
        

      for sample in range(samples):
          print 'sample {}'.format(sample)
          mat = slab_reactor_materials.get_materials(perturb=perturb)
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
          print "***************************"
      
          
          k.append(solver.state().eigenvalue())
          fission_den = solver.fissionsource().density()
          fission_density_sample = []
          
    
          
          flux_0 = solver.state().phi(0)
          flux_0_sample = []
          
          flux_1 = solver.state().phi(1)
          flux_1_sample = []
          
          print len(flux_0)
    
          
          for i in range(len(fission_den)):
              fission_density_sample.append(fission_den[i])          
          
          for i in range(len(flux_0)):
              flux_0_sample.append(flux_0[i])
              flux_1_sample.append(flux_1[i])
              
          fission_density_samples[:, sample] = fission_density_sample
          flux_0_samples[:, sample] = flux_0_sample
          flux_1_samples[:, sample] = flux_1_sample
              
      data = {'fission_density' : fission_density_samples, 
              'flux_0': flux_0_samples,
              'flux_1': flux_1_samples,
              'k_eff': np.array(k)}
    
          
      pickle.dump(data, open(fname + '.p', 'wb'))
  


if __name__ == "__main__":
  Manager.initialize(sys.argv)
  run(perturb=1,  equation = 'diffusion')