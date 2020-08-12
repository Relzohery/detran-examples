#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:04:58 2020

@author: rabab
"""
import numpy as np
import pickle
import os

s_setting = r'''
/*
 * projection_fixture.hh
 *
 *  Created on: Jul 7, 2020
 *      Author: rabab
 */


#include "Mesh1D.hh"
#include "Material.hh"
#include "callow/vector/Vector.hh"
#include "callow/matrix/Matrix.hh"
#include "callow/matrix/MatrixDense.hh"
#include "callow/vector/Vector.hh"
#include "utilities/InputDB.hh"
#include "Definitions.hh"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace detran_material;
using namespace detran_geometry;
using namespace detran_utilities;
using namespace std;
using std::cout;
using std::endl;


Material::SP_material get_mat()
{{

  Material::SP_material mat = Material::Create(4, 2, "slabreactor");
  // Material 0: Water
  // Total
  mat->set_sigma_t(0, 0, {0});
  mat->set_sigma_t(0, 1, {1});

  // Fission
  mat->set_sigma_f(0, 0, 0);
  mat->set_sigma_f(0, 1, 0);
  mat->set_chi(0, 0, 0.0);
  mat->set_chi(0, 1, 0.0);

  // Scattering
  mat->set_sigma_s(0, 0, 0, {2});
  mat->set_sigma_s(0, 0, 1, 0.000);
  mat->set_sigma_s(0, 1, 0, {3});
  mat->set_sigma_s(0, 1, 1, {4});
  mat->compute_sigma_a();
  mat->compute_diff_coef();


  // Material 1: Fuel I
  // Total
  mat->set_sigma_t(1, 0, {5});
  mat->set_sigma_t(1, 1, {6});

  // Fission
  mat->set_sigma_f(1, 0, {7});
  mat->set_sigma_f(1, 1, {8});
  mat->set_chi(1, 0, 1.0);
  mat->set_chi(1, 1, 0.0);

  // Scattering
  mat->set_sigma_s(1, 0, 0, {9});
  mat->set_sigma_s(1, 0, 1, 0.0000);
  mat->set_sigma_s(1, 1, 0, {10});
  mat->set_sigma_s(1, 1, 1, {11});
  mat->compute_sigma_a();
  mat->compute_diff_coef();                   ;


  // Material 3: Fuel II

  // Total
  mat->set_sigma_t(2, 0, {12});
  mat->set_sigma_t(2, 1, {13});

  // Fission
  mat->set_sigma_f(2, 0, {14});
  mat->set_sigma_f(2, 1, {15});
  mat->set_chi(2, 0, 1.0);
  mat->set_chi(2, 1, 0.0);

  // Scattering
  mat->set_sigma_s(2, 0, 0, {16});
  mat->set_sigma_s(2, 0, 1, 0.0000);
  mat->set_sigma_s(2, 1, 0, {17});
  mat->set_sigma_s(2, 1, 1, {18});
  mat->compute_sigma_a();
  mat->compute_diff_coef();                   ;

  // Material 4: Fuel II + Gd

 // Total
  mat->set_sigma_t(3, 0, {19});
  mat->set_sigma_t(3, 1, {20});

  // Fission
  mat->set_sigma_f(3, 0, {21});
  mat->set_sigma_f(3, 1, {22});
  mat->set_chi(3, 0, 1.0);
  mat->set_chi(3, 1, 0.0);

   // Scattering
  mat->set_sigma_s(3, 0, 0, {23});
  mat->set_sigma_s(3, 0, 1, 0.0000);
  mat->set_sigma_s(3, 1, 0, {24});
  mat->set_sigma_s(3, 1, 1, {25});
  mat->compute_sigma_a();
  mat->compute_diff_coef();                   ;

  mat->finalize();

  return mat;
}}

Mesh1D::SP_mesh get_mesh(int fmm = 1, std::string id="assembly")
{{
  vec_dbl cm_assembly(7, 0.0);
  cm_assembly[0] = 0.0;
  cm_assembly[1] = 1.1580;
  cm_assembly[2] = 4.4790;
  cm_assembly[3] = 7.8000;
  cm_assembly[4] = 11.1210;
  cm_assembly[5] = 14.4420;
  cm_assembly[6] = 15.6000;

  vec_int fm_assembly(6, 0);

  fm_assembly[0] = 2;
  fm_assembly[1] = 4;
  fm_assembly[2] = 4;
  fm_assembly[3] = 4;
  fm_assembly[4] = 4;
  fm_assembly[5] = 2;

  // a core is composed of 7 adjacent assemblies
  vec_dbl cm_core (43, 0);
  vec_int fm_core(7*6);

  for (int i=0; i <7; i++)
   for (int j=0; j<6; j++)
	 {{

      cm_core[j+(6*i) + 1] = cm_assembly[j +1] + 15.6 *i;

	  fm_core[j+(6*i)] = fm_assembly[j];
	 }}
  cm_core [0] = 0.0;

  //cm_core.assign(0.0 ,0.0);

  Mesh1D::vec_int mt_0(6);
  mt_0[0] = 0; mt_0[1] = 1;
  mt_0[2] = 2; mt_0[3] = 2;
  mt_0[4] = 1; mt_0[5] = 0;

  Mesh1D::vec_int mt_1(6);
  mt_1[0] = 0; mt_1[1] =1;
  mt_1[2] = 1; mt_1[3] = 1;
  mt_1[4] = 1; mt_1[5] = 0;

  Mesh1D::vec_int mt_2(6);
  mt_2[0] = 0; mt_2[1] =1;
  mt_2[2] = 3; mt_2[3] = 3;
  mt_2[4] = 1; mt_2[5] = 0;

  Mesh1D::vec_int mt_3(6);
  mt_3[0] = 0; mt_3[1] = 3;
  mt_3[2] = 3; mt_3[3] = 3;
  mt_3[4] = 3; mt_3[5] = 0;


  Mesh1D::vec_int mt_core0(42);
  mt_core0[0] = 0; mt_core0[1] = 1;
  mt_core0[2] = 2; mt_core0[3] = 2;
  mt_core0[4] = 1; mt_core0[5] = 0;

  mt_core0[6] = 0; mt_core0[7] = 1;
  mt_core0[8] = 1; mt_core0[9] = 1;
  mt_core0[10] = 1; mt_core0[11] = 0;

  mt_core0[12] = 0; mt_core0[13] = 1;
  mt_core0[14] = 2; mt_core0[15] = 2;
  mt_core0[16] = 1; mt_core0[17] = 0;

  mt_core0[18] = 0; mt_core0[19] = 1;
  mt_core0[20] = 1; mt_core0[21] = 1;
  mt_core0[22] = 1; mt_core0[23] = 0;

  mt_core0[24] = 0; mt_core0[25] = 1;
  mt_core0[26] = 2; mt_core0[27] = 2;
  mt_core0[28] = 1; mt_core0[29] = 0;

  mt_core0[30] = 0; mt_core0[31] = 1;
  mt_core0[32] = 1; mt_core0[33] = 1;
  mt_core0[34] = 1; mt_core0[35] = 0;

  mt_core0[36] = 0; mt_core0[37] = 1;
  mt_core0[38] = 2; mt_core0[39] = 2;
  mt_core0[40] = 1; mt_core0[41] = 0;

  if (id == "assembly")
  {{
  Mesh1D::SP_mesh mesh = Mesh1D::Create(fm_assembly, cm_assembly, mt_0);
  return mesh;
  }}
  else if (id == "core")
  {{
   Mesh1D::SP_mesh mesh = Mesh1D::Create(fm_core, cm_core, mt_core0);

   return mesh;
  }}

}}

InputDB::SP_input get_input()
{{
  InputDB::SP_input inp(new InputDB("Slab Reactor"));
  inp->put<std::string>("problem_type", "eigenvalue");
  inp->put<int>("number_groups",                  2);
  inp->put<std::string>("inner_solver",           "SI");
  inp->put<int>("inner_max_iters",            1000);
  inp->put<int>("inner_max_iters",            1000);
  inp->put<double>("inner_tolerance",            1e-7);
  inp->put<int>("inner_print_level",          0);
  inp->put<std::string>("outer_solver",              "GS");
  inp->put<int>("outer_max_iters",            1000);
  inp->put<double>("outer_tolerance",            1e-7);
  inp->put<int>("inner_print_level",          0);
  inp->put<int>("outer_print_level",          1);
 // inp->put<std::string>("eigen_solver",       "arnoldi");
  inp->put<int>("eigen_max_iters",            200);
  inp->put<double>("eigen_tolerance",            1e-7);
  inp->put<std::string>("bc_west",                    "vacuum");
  inp->put<std::string>("bc_east",                    "vacuum");
  inp->put<int>("quad_number_polar_octant",   16);

  InputDB::SP_input db(new InputDB("callow dp"));
  db->put<double>("linear_solver_atol",              1e-12);
  db->put<double>("linear_solver_rtol",              1e-12);
  db->put<std::string>("linear_solver_type",              "petsc");
  db->put<int>("linear_solver_maxit",             5000);
  db->put<int>("linear_solver_gmres_restart",     30);
  db->put<int>("linear_solver_monitor_level",     0);
  db->put<std::string>("pc_type",                         "petsc_pc");
  db->put<std::string>("petsc_pc_type",                   "lu");
  db->put<std::string>("eigen_solver_type",               "slepc");
  db->put<int>("eigen_solver_monitor_level",      2);
  db->put<InputDB::SP_input>("inner_solver_db",               db);
  db->put<InputDB::SP_input>("inner_pc_db",                   db);
  db->put<InputDB::SP_input>("outer_solver_db",               db);
  db->put<InputDB::SP_input>("eigen_solver_db",               db);


  return inp;
}}


'''

xs_data = {'mat1': {'sigma_t': [0.1890, 1.4633], 'sigma_f': [0.0, 0.0], 'chi':[0, 0], 'sigma_s':[0.1507, 0.0000, 0.0161, 1.4536]},
           'mat2': {'sigma_t': [ 0.2263, 1.0119 ], 'sigma_f': [0.0067  , 0.1241 ], 'chi':[1,0], 'sigma_s':[0.2006, 0.0, 0.0161,0.9355]}, 
           'mat3': {'sigma_t': [0.2252, 0.9915], 'sigma_f': [0.0078, 0.1241], 'chi':[1, 0], 'sigma_s':[0.1995, 0.0, 0.0156,0.9014]}, 
           'mat4': {'sigma_t': [ 0.2173, 1.0606], 'sigma_f': [ 0.0056, 0.0187 ], 'chi':[1,0 ], 'sigma_s':[ 0.1902,0.0,0.0136 ,0.5733]}
           }


s_test = r'''
/*
 * test_ROMSolver.cc
 *
 *  Created on: Jul 9, 2020
 *      Author: rabab
 */


#define TEST_LIST \
        FUNC(test_ROM_diffusion)\
		FUNC(test_ROM_EnergyIndependent)\
		FUNC(test_ROM_EnergyDependent)


#include "TestDriver.hh"
#include "callow/utils/Initialization.hh"
#include "utilities/MathUtilities.hh"
#include "projection_fixture.hh"
#include "callow/matrix/MatrixBase.hh"
#include "callow/matrix/MatrixDense.hh"
#include "solvers/EigenvalueManager.hh"
#include "callow/vector/Vector.hh"
#include "solvers/rom/ROMSolver.hh"
#include "solvers/rom/ROMBasis.hh"

using namespace detran_test;
using namespace detran;
using namespace detran_utilities;
using namespace std;

typedef callow::MatrixDense::SP_matrix SP_matrix;
typedef callow::Vector::SP_vector      SP_vector;



int main(int argc, char *argv[])
{{
  callow_initialize(argc, argv);
  RUN(argc, argv);
  callow_finalize();
}}

int test_ROM_diffusion(int argc, char *argv[])
{{
 Mesh1D::SP_mesh mesh = get_mesh(1, "core");
 Material::SP_material mat = get_mat();
 InputDB::SP_input input = get_input();
 input->put<std::string>("equation", "diffusion");

 int n = mesh->number_cells();
 int r = 6;

// get the basis
 SP_matrix U;
 U = new callow::MatrixDense(2*n, 2*r);
 std::cout << n << "\n";
 ROMBasis::GetBasis("/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_diff_r=6", U);

 // ROM
 ROMSolver<_1D> ROM(input, mesh, mat);
 SP_vector  ROM_flux;
 ROM_flux = new callow::Vector(2*n, 0.0);
 ROM.Solve(U, ROM_flux);
 double keff_rom = ROM.keff();

 std::cout << keff_rom << "$$$$$$$$$$" << "\n";
 // FOM
 EigenvalueManager<_1D> manager(input, mat, mesh);
 manager.solve();
 double keff_fom = manager.state()->eigenvalue();

// error and testing
 callow::Vector phi0_fom(n, 0.0);
 callow::Vector phi1_fom(n, 0.0);

 callow::Vector phi0_rom(n, 0.0);
 callow::Vector phi1_rom(n, 0.0);

 for (int i = 0; i < n; ++i)
{{
  phi0_fom[i] = manager.state()->phi(0)[i];
  phi1_fom[i] = manager.state()->phi(1)[i];
  phi0_rom[i] = (*ROM_flux)[i];
  phi1_rom[i] = (*ROM_flux)[i + n];
}}
 vec_dbl error1 (n, 0);
 vec_dbl error2 (n, 0);

 for (int i = 0; i < n; ++i)
 {{
   error1[i] = phi0_fom[i]/phi0_fom.norm() - phi0_rom[i]/phi0_rom.norm();

   error2[i] = phi1_fom[i]/phi1_fom.norm() - phi1_rom[i]/phi1_rom.norm();
 }}

 std::cout << "The error in group 1 is " << detran_utilities::norm(error1, "L2") << "\n";
 std::cout << "The error in group 2 is " << detran_utilities::norm(error2, "L2") << "\n";
 std::cout << "The absolute error in the eigenvalue  " << abs(keff_rom - keff_fom) << "\n";

 TEST(soft_equiv(manager.state()->eigenvalue(), ROM.keff(), 1E-6));

 return 0;
}}


int test_ROM_EnergyIndependent(int argc, char *argv[])
{{
  Mesh1D::SP_mesh mesh = get_mesh(1, "core");
  Material::SP_material mat = get_mat();
  InputDB::SP_input input = get_input();
  input->put<std::string>("equation", "dd");

  ROMSolver<_1D> ROM(input, mesh, mat);
  int n = mesh->number_cells();
  int r = {0};

  // get the basis
  SP_matrix U;
  U = new callow::MatrixDense(n, r);
  ROMBasis::GetBasis("{1}", U);
  SP_vector  fd_rom;

  std::cout << "########################################################" << "\n";
  std::cout << "################### Reduced Order Model  ##################" << "\n";
  std::cout << "########################################################" << "\n";
  // ROM
  fd_rom = new callow::Vector(n, 0.0);
  ROM.Solve(U, fd_rom);
  double keff_rom = ROM.keff();


 //FOM
  std::cout << "\n########################################################" << "\n";
  std::cout << "################### Full Order Model  ##################" << "\n";
  std::cout << "########################################################" << "\n";
  EigenvalueManager<_1D> manager(input, mat, mesh);
  manager.solve();
  double keff_fom = manager.state()->eigenvalue();

  // error and testing
  callow::Vector fd_fom(n, 0.0);
  for (int i = 0; i < n; ++i)
  {{
	fd_fom[i] = manager.fissionsource()->density()[i];
  }}

  callow::Vector error(n, 0.0);

  for (int i = 0; i < n; ++i)
  {{
    error[i] = fd_fom[i]/fd_fom.norm() - (*fd_rom)[i]/fd_rom->norm();
  }}

  std::cout << "the error norm in the fission density =   " << error.norm()<<  "\n";
  std::cout << "The absolute error in the eigenvalue = " << abs(keff_rom - keff_fom) << "\n";

  TEST(soft_equiv(manager.state()->eigenvalue(), ROM.keff(), 1E-6));

 return 0;
}}

int test_ROM_EnergyDependent(int argc, char *argv[])
{{
  Mesh1D::SP_mesh mesh = get_mesh(1, "core");
  Material::SP_material mat = get_mat();
  InputDB::SP_input input = get_input();

  int n = mesh->number_cells();
  int r = 6;

  // get the basis
  SP_matrix U;
  U = new callow::MatrixDense(2*n, 2*r);
  ROMBasis::GetBasis("/home/rabab/opt/detran/source/src/solvers/test/flux_basis_core0_transport_r=6", U);

  // ROM
  ROMSolver<_1D> ROM(input, mesh, mat);
  SP_vector  ROM_flux;
  ROM_flux = new callow::Vector(2*n, 0.0);
  ROM.Solve(U, ROM_flux);
  double keff_rom = ROM.keff();

  // FOM
  EigenvalueManager<_1D> manager(input, mat, mesh);
  manager.solve();
  double keff_fom = manager.state()->eigenvalue();

  // error and testing
  callow::Vector phi0_fom(n, 0.0);
  callow::Vector phi1_fom(n, 0.0);

  callow::Vector phi0_rom(n, 0.0);
  callow::Vector phi1_rom(n, 0.0);

  for (int i = 0; i < n; ++i)
  {{
   phi0_fom[i] = manager.state()->phi(0)[i];
   phi1_fom[i] = manager.state()->phi(1)[i];
   phi0_rom[i] = (*ROM_flux)[i];
   phi1_rom[i] = (*ROM_flux)[i + n];
  }}
  vec_dbl error1 (n, 0);
  vec_dbl error2 (n, 0);

  for (int i = 0; i < n; ++i)
  {{
    error1[i] = phi0_fom[i]/phi0_fom.norm() - phi0_rom[i]/phi0_rom.norm();

    error2[i] = phi1_fom[i]/phi1_fom.norm() - phi1_rom[i]/phi1_rom.norm();
  }}

  std::cout << "The error in group 1 is " << detran_utilities::norm(error1, "L2") << "\n";
  std::cout << "The error in group 2 is " << detran_utilities::norm(error2, "L2") << "\n";
  std::cout << "The absolute error in the eigenvalue  " << abs(keff_rom - keff_fom) << "\n";


 TEST(soft_equiv(manager.state()->eigenvalue(), ROM.keff(), 1E-6))

 return 0;
}}
'''
