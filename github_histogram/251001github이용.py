import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("hist.csv")
n, bins, p=plt.hist(data, bins=40, color="k")
plt.xlim(0,12)
plt.title("Energy Spectrum")
plt.xlabel("Energy(keV)")
plt.ylabel("Intensity #")
plt.grid()
plt.show()