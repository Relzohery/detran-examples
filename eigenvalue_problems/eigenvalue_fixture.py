from material_fixture import *

def get_eigenvalue_data(dim, ng):

    # get input
    inp = InputDB.Create()
    inp.put_str("problem_type",               "eigenvalue")
    inp.put_int("number_groups",              ng)
    #inp.put_str("equation",                   "dd")
   # inp.put_str("inner_solver",               "SI")
    inp.put_int("inner_max_iters",            1000000)
    inp.put_dbl("inner_tolerance",            1e-18)
    inp.put_int("inner_print_level",          0)
    inp.put_str("outer_solver",               "GS")
    inp.put_int("outer_max_iters",            1000000)
    inp.put_dbl("outer_tolerance",            1e-7)
    inp.put_int("outer_print_level",          0)
    inp.put_str("eigen_solver",               "PI")
    inp.put_int("eigen_max_iters",            200)
    inp.put_dbl("eigen_tolerance",            1e-16)
    inp.put_str("bc_west",                    "reflect")
    inp.put_str("bc_east",                    "reflect")
    inp.put_int("quad_number_polar_octant",   16)
    
    # mesh
    cm = [0, 2, 0.0]
    cm[1] = 5.0;
    fm = [1, 5];
    mt = [1, 2];
    if (dim == 1):
      mesh = Mesh1D.Create(fm, cm, mt);
    elif (dim == 2):
     mesh = Mesh2D.Create(fm, fm, cm, cm, mt);
    elif (dim == 3):
     mesh = Mesh3D.Create(fm, fm, fm, cm, cm, cm, mt);
     
    # material
    if ng == 1:
        mat = get_materials_1g();
        
    elif ng == 2:
        mat = material_fixture_2g()
        
    elif ng==7:
        mat = material_fixture_7g()
        

   
    return inp, mesh, mat
        
    
