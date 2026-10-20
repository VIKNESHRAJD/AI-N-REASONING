import numpy as np
import matplotlib.pyplot as plt

p = 0.3
x = [0, 1]

probability = [(1-p), p]

print("Outcomes:", x)
print("Probabilities:", probability)

plt.bar(x, probability, label="PMF")
plt.title("Bernoulli Distribution")
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.xticks(x, ["Failure(0)", "Success(1)"])
plt.legend()
plt.show()