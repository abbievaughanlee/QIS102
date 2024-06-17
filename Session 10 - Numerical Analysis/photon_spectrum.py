# photon_spectrum.py
# treating cancer tumors via radiation of photon beams requires carefully tuning the emitter
    # only photos within a specific energy range will penetrate the tissue and break up the tumor
    # also important that the beam shines only for a specific duration
    # how could we calculate the percentage of photons from the emitter that fall in the range [2.12...3.14] MeV?
        # we need to interpolate to fit a series of smooth curves between the discrete data points and then integrate them
        # the ratio of the integral of the energy density curve within the desired range divided by the area of the entire curve will yield the percentage

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d


# one dimensional interpolation: interp1d
def main():
    file_name = "photon_spectrum.txt" # calls text file
    file_path = Path(__file__).parent / file_name
    # Note: this is NOT a CSV file and has no header row
    samples = np.genfromtxt(file_path, delimiter=" ") # generate from text file separated by a space
    energy, density = samples.T # transpose data so that it is two rows with 18 columns

    min_energy, max_energy = np.min(energy), np.max(energy) # find min and max values of energy and create linspace
    energy_est = np.linspace(min_energy, max_energy, 1000)

    # interp1d() returns an "interpolation object" which  can then act as a callable function that is vector aware
    density_f = interp1d(energy, density, kind="cubic") 
    density_est = density_f(energy_est)

    min_window, max_window = 2.12, 3.45  # MeV
    window_energy = quad(density_f, min_window, max_window)[0] # psuedo-function used to find area under curve; [0] indicates that the first element in the result is the answer
    total_energy = quad(density_f, min_energy, max_energy)[0]
    print(f"{window_energy/total_energy:.4%}", end=" ")
    print("of the beam photons are within the energy window")

    #plot the data
    plt.figure(Path(__file__).name)
    plt.scatter(energy, density, zorder=3) # zorder: want data points to be on top of everything

    plt.plot(energy_est, density_est)
    # color the area of a curve
    plt.fill_between(
        energy_est,
        density_est,
        where=(energy_est >= min_window) * (energy_est <= max_window), # * acts as "and"
        color="orange", #dangling comma at the end allows someone to come add more parameters later
    )

    plt.xlabel("Photon Energy [MeV]")
    plt.ylabel(r"Density of photons ($\;J/m^3\;x\;10^7$)")
    plt.title("Photon Spectrum")
    plt.axhline(0, c="k")
    plt.show()


main()
