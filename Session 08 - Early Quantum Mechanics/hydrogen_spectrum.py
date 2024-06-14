# hydrogen_spectrum.py

# calculate and display the wavelengths for the Pfund and Humphreys high energy spectral series of Hydrogen
# use both the Rydberg and Bohr formulas

#constants:
e_charge = 1.602e-19
e_mass = 9.109e-31
permittivity = 8.854e-12
h_plank = 6.626e-34
speed_light = 2.998e8
rydberg_constant = 1.0967757e7

#formulas
e_0 = pow(e_charge, 4) * e_mass / (8 * pow(permittivity, 2) * pow(h_plank, 2))

#wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9