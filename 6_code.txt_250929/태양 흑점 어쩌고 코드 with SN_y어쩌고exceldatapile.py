import numpy as np
import matplotlib.pyplot as plt

year, nspots, sd, n1, n2 = np.loadtxt('C:/Users/user/Documents/929/SN_y_tot_V2.0.csv', \
                                      delimiter=';', unpack=True)

plt.plot(year, nspots)
plt.show()