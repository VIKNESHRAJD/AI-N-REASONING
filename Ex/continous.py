import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

x = uniform.rvs(loc=0.01, scale=0.99, size=100)

print("PDF =", uniform.pdf(x[0], loc=0.01, scale=0.99))

plt.hist(x, bins=10, density=True, alpha=0.7)
plt.axhline(1/0.99, color='black', label="PDF")
plt.xlabel("X")
plt.ylabel("Density")
plt.title("Continuous Uniform Distribution")
plt.legend()
plt.show()