import matplotlib.pyplot as plt
import numpy as np
import os

file_path = os.path.join("data", "asu_unlimited.txt")

data = np.genfromtxt(file_path, delimiter=";", usecols=(1, 2, 3), dtype=np.float32, filling_values=np.nan)

data_clean = data[~np.isnan(data).any(axis=1)]
data_clean = data_clean[data_clean[:, 1] > 0]

apparent_magnitude = data_clean[:, 0]
parallex = data_clean[:, 1]
bv_index = data_clean[:, 2]

absolute_magnitude = apparent_magnitude - 5 * np.log10(1 / (parallex / 1000)) + 5

plt.grid()
plt.scatter(bv_index, absolute_magnitude, s=0.1)
plt.gca().invert_yaxis()
plt.gca().set_axisbelow(True)
plt.title("The Hipparcos and Tycho Catalogues (ESA 1997)")
plt.xlabel("B-V Index")
plt.ylabel("Absolute Magnitude")
plt.savefig("asu_unlimited.svg", bbox_inches='tight')
plt.savefig("asu_unlimited.png", bbox_inches='tight')