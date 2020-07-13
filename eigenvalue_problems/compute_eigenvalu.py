from eigenvalue_fixture import get_eigenvalue_data

from detran import *


def eigen_7g():

    inp, mesh, mat = get_eigenvalue_data(1, 2)
    
    mat.display()
    
    #mesh.display()
    #mat.compute_diff_coef()
    solver = Eigen1D(inp, mat, mesh)
    solver.solve()


eigen_7g()
    
