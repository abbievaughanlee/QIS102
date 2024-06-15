# bessel_correction.py
# generate a full population set containing 7000 random natural numbers <1000 (full population data)
    #calculate the population variance for the full set
# create 20,000 random samples of size n taken from that full population set.
# find the mean biased sample variance for all 20,000 of the sample sets (goal: validate Bessel's correction)
# display a table with one row for each of the sample sizes from 2 to 20 columns showing the sample size, the mean BSV, the true PV and a ratio of BSV to PV
# plot the ratio of BSV/PV for increasing sample sizes from 2 to 20, and superimpose a plot of the hyperbola (n-1) / n

# python pickle: helps with data structure: pickle.dump(), pickle.load() compresses and stores data structures then undoes it
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from numba import njit
from numpy.random import choice, randint


# create biased sample variance
@njit
def get_bsv(arr):
    mean = np.mean(arr)
    bsv = float(np.sum((arr - mean) ** 2) / len(arr))
    return bsv


@njit
def get_sample_bsv(population, sample_size):
    num_trials = 20_000
    total_bsv = 0.0
    for _ in range(num_trials):
        #no number can get picked twice from the population
        samples = choice(population, sample_size, replace=False)
        total_bsv += get_bsv(samples)
    mean_bsv = total_bsv / num_trials
    return mean_bsv


def run_trials():
    population = randint(0, 1000, 7000)
    pop_var = get_bsv(population)

    max_sample_size = 20

    print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^18}{'Ratio':^8}")

    results = []
    for sample_size in range(2, max_sample_size + 1):
        sample_bsv = get_sample_bsv(population, sample_size)
        ratio = sample_bsv / pop_var
        results.append((sample_size, sample_bsv, pop_var, ratio))
        print(
            f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}", f"{ratio:^15.4f}"
        )
    return results


def plot_ratio(ax, results):
    x1 = [r[0] for r in results]  # 1st column in results table
    y1 = [r[3] for r in results]  # 4th column in results table
    ax.plot(x1, y1, label="BSV/PV")

    x2 = np.linspace(2, 20)
    y2 = (x2 - 1) / x2
    ax.plot(x2, y2, label=r"$\frac{n-1}{n}$")

    ax.set_title(r"$\frac{BSV}{PV}$ compared to Hyperbola $\frac{(n-1)}{n}$")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Biased Sample Var / Population Var")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.legend(loc="center right")


def plot_ubsv(ax, results):
    x = [r[0] for r in results]  # 1st column in results table
    y = [r[2] for r in results]  # 3rd column in results table
    ax.plot(x, y, label="Pop Var")

    y = [r[1] for r in results]
    ax.plot(x, y, label="BSV")

    for i, _ in enumerate(y):
        y[i] = y[i] * x[i] / (x[i] - 1)
    ax.plot(x, y, label="UBSV")

    ax.set_title("Variance: Population v. Biased Sample v. Unbiased Sample")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Variance")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend(loc="center right")


def main():
    plt.figure(Path(__file__).name)
    #saves as bessel.pickle
    file_name = "bessel.pickle"
    #saves as a path under the parent file
    data_file = Path(__file__).parent / file_name
    #if the data file does not exist, then run the trials and create the file
    if not data_file.exists():
        results = run_trials()
        with open(data_file, "wb") as file_out:
            #put results in the pickle file
            pickle.dump(results, file_out, pickle.HIGHEST_PROTOCOL)
        #plot the results  
        plot_ratio(plt.gca(), results)
    #if the pickle file already exists
    else:
        with open(data_file, "rb") as file_in:
            #load pickle file
            results = pickle.load(file_in)
        print(f"{'Sample Size':^11}{'Sample Var':^21}{'Pop Var':^16}{'UBSV':^12}")
        #apply Bessel's correction and compare how BPV compares to PV as determined by Bessel
        for r in results:
            #r is a tuple. Only pay attention to sample size, sample bsv, pop var and ignore the rest
            sample_size, sample_bsv, pop_var, _ = r
            #add the projected estimate for PV to the graph
            ubsv = sample_bsv * sample_size / (sample_size - 1)
            print(
                f"{sample_size:^11}{sample_bsv:>16,.4f}{pop_var:>18,.4f}",
                f"{ubsv:^18,.4f}",
            )
        plot_ubsv(plt.gca(), results)

    plt.show()


main()
