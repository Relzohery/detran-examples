from detran import *
    
def get_materials_1g():
    print("***** 1g *****")
    mat = Material.Create(3, 1, "fixture_1g")
    # ---------------------------
    # Material 0: strong scatter
    # ---------------------------

    # Total
    mat.set_sigma_t(0, 0, 1.0);
    # Fission (none)
    mat.set_sigma_f(0, 0, 0.0);
    mat.set_chi(0, 0, 0.0);
    # Scattering
    mat.set_sigma_s(0, 0, 0, 0.9); # 1 <- 1

    # ---------------------------
    # Material 1: pure absorber
    # ---------------------------
    # Total
    mat.set_sigma_t(1, 0,    1.0);
    # Fission (none)
    mat.set_sigma_f(1, 0, 0.0);
    mat.set_chi(1, 0,        0.0);
    # Scattering
    mat.set_sigma_s(1, 0, 0, 0.0); # 1 <- 1

    # ---------------------------
    # Material 2: kinf = 1
    # ---------------------------
    # Total
    mat.set_sigma_t(2, 0, 1.0);
    # Fission (none)
    mat.set_sigma_f(2, 0, 0.5);
    mat.set_chi(2, 0, 1.0);
    # Scattering (=0.5 so sigma_a = 0.5, and kinf = 1.0)
    mat.set_sigma_s(2, 0, 0, 0.5); # 1 <- 1
    mat.finalize();
    
    return mat;

def material_fixture_2g():
   print("***** 2g *****")
   # 2 groups, 4 materials, and we don't turn off upscatter explicitly
   # (though there happens to be no upscatter in this data)
   mat = Material.Create(4, 2, "fixture_2g");

   # ---------------------------
   # Material 0: Water
   # ---------------------------

   # Total
   mat.set_sigma_t(0, 0, 0.1890); # (obj, matid, g, value);
   mat.set_sigma_t(0, 1, 1.4633);

   # Fission
   mat.set_sigma_f(0, 0, 0.0); # Note, default is zero
   mat.set_sigma_f(0, 1, 0.0);
   mat.set_chi(0, 0, 0.0);
   mat.set_chi(0, 1, 0.0);

   # Scattering
   mat.set_sigma_s(0, 0, 0, 0.1507); # 1 <- 1
   mat.set_sigma_s(0, 0, 1, 0.0000); # 1 <- 2
   mat.set_sigma_s(0, 1, 0, 0.0380); # 2 <- 1
   mat.set_sigma_s(0, 1, 1, 1.4536); # 2 <- 2

   # ---------------------------
   # Material 1: Fuel I
   # ---------------------------

   # Total
   mat.set_sigma_t(1, 0, 0.2263); # (matid, g, value);
   mat.set_sigma_t(1, 1, 1.0119);

   # Fission
   mat.set_sigma_f(1, 0, 0.0067);
   mat.set_sigma_f(1, 1, 0.1241);
   mat.set_chi(1, 0, 1.0);
   mat.set_chi(1, 1, 0.0);

   # Scattering
   mat.set_sigma_s(1, 0, 0, 0.2006); # 1 <- 1
   mat.set_sigma_s(1, 0, 1, 0.0000); # 1 <- 2
   mat.set_sigma_s(1, 1, 0, 0.0161); # 2 <- 1
   mat.set_sigma_s(1, 1, 1, 0.9355); # 2 <- 2

   # sa(0) =  .2263- .2006-0.0161 = 0.0096
   # sa(1) = 1.0119- .9355 = 0.0764

   # ---------------------------
   # Material 2: Fuel II
   # ---------------------------

   # Total
   mat.set_sigma_t(2, 0, 0.2252); # (obj, matid, g, value);
   mat.set_sigma_t(2, 1, 0.9915);

   # Fission
   mat.set_sigma_f(2, 0, 0.0078);
   mat.set_sigma_f(2, 1, 0.1542);
   mat.set_chi(2, 0, 1.0);
   mat.set_chi(2, 1, 0.0);

   # Scattering
   mat.set_sigma_s(2, 0, 0, 0.1995); # 1 <- 1
   mat.set_sigma_s(2, 0, 1, 0.0000); # 1 <- 1
   mat.set_sigma_s(2, 1, 0, 0.0156); # 1 <- 1
   mat.set_sigma_s(2, 1, 1, 0.9014); # 1 <- 1

   # ---------------------------
   # Material 3: Fuel II + Gd
   # ---------------------------

   # Total
   mat.set_sigma_t(3, 0, 0.2173); # (obj, matid, g, value);
   mat.set_sigma_t(3, 1, 1.0606);

   # Fission
   mat.set_sigma_f(3, 0, 0.0056);
   mat.set_sigma_f(3, 1, 0.0187);
   mat.set_chi(3, 0, 1.0);
   mat.set_chi(3, 1, 0.0);

   # Scattering
   mat.set_sigma_s(3, 0, 0, 0.1902); # 1 <- 1
   mat.set_sigma_s(3, 0, 1, 0.0000); # 1 <- 1
   mat.set_sigma_s(3, 1, 0, 0.0136); # 1 <- 1
   mat.set_sigma_s(3, 1, 1, 0.5733); # 1 <- 1

   # ---------------------------
   # FINALIZE
   # ---------------------------

   # This mat.sets the scattering bounds, which can eliminate a few operations.
   mat.compute_diff_coef();
   mat.compute_sigma_a();
   mat.finalize();

   # Return the fixture.
   return mat;


def material_fixture_7g():
   # Create the new database.
   print("***** 7g *****")
   # 7 groups, 7 materials
   mat = Material.Create(7, 7, "fixture_7g");

   # --------------------------------------------
   # Material 0: UO2 fuel-clad
   # --------------------------------------------
   m = 0;
   # Transport cross section
   mat.set_sigma_t(m, 0, 1.77949E-01);
   mat.set_sigma_t(m, 1, 3.29805E-01);
   mat.set_sigma_t(m, 2, 4.80388E-01);
   mat.set_sigma_t(m, 3, 5.54367E-01);
   mat.set_sigma_t(m, 4, 3.11801E-01);
   mat.set_sigma_t(m, 5, 3.95168E-01);
   mat.set_sigma_t(m, 6, 5.64406E-01);
   # Absorption cross section
   mat.set_sigma_a(m, 0, 8.02480E-03);
   mat.set_sigma_a(m, 1, 3.71740E-03);
   mat.set_sigma_a(m, 2, 2.67690E-02);
   mat.set_sigma_a(m, 3, 9.62360E-02);
   mat.set_sigma_a(m, 4, 3.00200E-02);
   mat.set_sigma_a(m, 5, 1.11260E-01);
   mat.set_sigma_a(m, 6, 2.82780E-01);
   # Fission times nu
   mat.set_sigma_f(m, 0, 7.21206E-03*2.78145E+00);
   mat.set_sigma_f(m, 1, 8.19301E-04*2.47443E+00);
   mat.set_sigma_f(m, 2, 6.45320E-03*2.43383E+00);
   mat.set_sigma_f(m, 3, 1.85648E-02*2.43380E+00);
   mat.set_sigma_f(m, 4, 1.78084E-02*2.43380E+00);
   mat.set_sigma_f(m, 5, 8.30348E-02*2.43380E+00);
   mat.set_sigma_f(m, 6, 2.16004E-01*2.43380E+00);
   # Fission spectrum
   mat.set_chi(m, 0, 5.87819E-01);
   mat.set_chi(m, 1, 4.11760E-01);
   mat.set_chi(m, 2, 3.39060E-04);
   mat.set_chi(m, 3, 1.17610E-07);
   mat.set_chi(m, 4, 0.00000E+00);
   mat.set_chi(m, 5, 0.00000E+00);
   mat.set_chi(m, 6, 0.00000E+00);
   # Scattering
   #   1 <- g'
   mat.set_sigma_s(m, 0, 0, 1.27537E-01);
   #   2 <- g'
   mat.set_sigma_s(m, 1, 0, 4.23780E-02);
   mat.set_sigma_s(m, 1, 1, 3.24456E-01);
   #   3 <- g'
   mat.set_sigma_s(m, 2, 0, 9.43740E-06);
   mat.set_sigma_s(m, 2, 1, 1.63140E-03);
   mat.set_sigma_s(m, 2, 2, 4.50940E-01);
   #   4 <- g'
   mat.set_sigma_s(m, 3, 0, 5.51630E-09);
   mat.set_sigma_s(m, 3, 1, 3.14270E-09);
   mat.set_sigma_s(m, 3, 2, 2.67920E-03);
   mat.set_sigma_s(m, 3, 3, 4.52565E-01);
   mat.set_sigma_s(m, 3, 4, 1.25250E-04);
   #   5 <- g'
   mat.set_sigma_s(m, 4, 3, 5.56640E-03);
   mat.set_sigma_s(m, 4, 4, 2.71401E-01);
   mat.set_sigma_s(m, 4, 5, 1.29680E-03);
   #   6 <- g'
   mat.set_sigma_s(m, 5, 4, 1.02550E-02);
   mat.set_sigma_s(m, 5, 5, 2.65802E-01);
   mat.set_sigma_s(m, 5, 6, 8.54580E-03);
   #   7 <- g'
   mat.set_sigma_s(m, 6, 4, 1.00210E-08);
   mat.set_sigma_s(m, 6, 5, 1.68090E-02);
   mat.set_sigma_s(m, 6, 6, 2.73080E-01);

   # --------------------------------------------
   # Material 1: 4.3w/o MOX fuel-clad
   # --------------------------------------------
   m = 1;
   # Transport cross section
   mat.set_sigma_t(m, 0, 1.78731E-01);
   mat.set_sigma_t(m, 1, 3.30849E-01);
   mat.set_sigma_t(m, 2, 4.83772E-01);
   mat.set_sigma_t(m, 3, 5.66922E-01);
   mat.set_sigma_t(m, 4, 4.26227E-01);
   mat.set_sigma_t(m, 5, 6.78997E-01);
   mat.set_sigma_t(m, 6, 6.82852E-01);
   # Absorption cross section
   mat.set_sigma_a(m, 0, 8.43390E-03);
   mat.set_sigma_a(m, 1, 3.75770E-03);
   mat.set_sigma_a(m, 2, 2.79700E-02);
   mat.set_sigma_a(m, 3, 1.04210E-01);
   mat.set_sigma_a(m, 4, 1.39940E-01);
   mat.set_sigma_a(m, 5, 4.09180E-01);
   mat.set_sigma_a(m, 6, 4.09350E-01);
   # Fission times nu
   mat.set_sigma_f(m, 0, 7.62704E-03*2.85209E+00);
   mat.set_sigma_f(m, 1, 8.76898E-04*2.89099E+00);
   mat.set_sigma_f(m, 2, 5.69835E-03*2.85486E+00);
   mat.set_sigma_f(m, 3, 2.28872E-02*2.86073E+00);
   mat.set_sigma_f(m, 4, 1.07635E-02*2.85447E+00);
   mat.set_sigma_f(m, 5, 2.32757E-01*2.86415E+00);
   mat.set_sigma_f(m, 6, 2.48968E-01*2.86780E+00);
   # Fission spectrum
   mat.set_chi(m, 0, 5.87819E-01);
   mat.set_chi(m, 1, 4.11760E-01);
   mat.set_chi(m, 2, 3.39060E-04);
   mat.set_chi(m, 3, 1.17610E-07);
   mat.set_chi(m, 4, 0.00000E+00);
   mat.set_chi(m, 5, 0.00000E+00);
   mat.set_chi(m, 6, 0.00000E+00);
   # Scattering
   #   1 <- g'
   mat.set_sigma_s(m, 0, 0, 1.28876E-01);
   #   2 <- g'
   mat.set_sigma_s(m, 1, 0, 4.14130E-02);
   mat.set_sigma_s(m, 1, 1, 3.25452E-01);
   #   3 <- g'
   mat.set_sigma_s(m, 2, 0, 8.22900E-06);
   mat.set_sigma_s(m, 2, 1, 1.63950E-03);
   mat.set_sigma_s(m, 2, 2, 4.53188E-01);
   #   4 <- g'
   mat.set_sigma_s(m, 3, 0, 5.04050E-09);
   mat.set_sigma_s(m, 3, 1, 1.59820E-09);
   mat.set_sigma_s(m, 3, 2, 2.61420E-03);
   mat.set_sigma_s(m, 3, 3, 4.57173E-01);
   mat.set_sigma_s(m, 3, 4, 1.60460E-04);
   #   5 <- g'
   mat.set_sigma_s(m, 4, 3, 5.53940E-03);
   mat.set_sigma_s(m, 4, 4, 2.76814E-01);
   mat.set_sigma_s(m, 4, 5, 2.00510E-03);
   #   6 <- g'
   mat.set_sigma_s(m, 5, 4, 9.31270E-03);
   mat.set_sigma_s(m, 5, 5, 2.52962E-01);
   mat.set_sigma_s(m, 5, 6, 8.49480E-03);
   #   7 <- g'
   mat.set_sigma_s(m, 6, 4, 9.16560E-09);
   mat.set_sigma_s(m, 6, 5, 1.48500E-02);
   mat.set_sigma_s(m, 6, 6, 2.65007E-01);
   
   
   return mat
