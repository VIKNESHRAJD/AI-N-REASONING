import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 8
p = 0.5
x = np.arange(n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y, label="PMF")
plt.plot(x, y, 'o-')
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.legend()
plt.show()