import numpy as np
import matplotlib.pyplot as plt

T = np.array([[0.7, 0.3], [0.3, 0.7]])
O = np.array([[0.9, 0.1], [0.1, 0.9]])
H = 3
obs = [0, 1, 0]

def forward(obs):
    f = np.array([0.5, 0.5])
    for x in obs:
        f = O[:, x] * (T.T @ f)
        f = f / (f[0] + f[1])
    return f

def backward(obs):
    b = np.array([1.0, 1.0])
    for x in obs[::-1]:
        b = T @ (O[:, x] * b)
        b = b / (b[0] + b[1])
    return b

f = forward(obs)
b = backward(obs)
print("Forward:", f)
print("Backward:", b)

plt.plot(f, label="Forward")
plt.plot(b, label="Backward")
plt.legend()
plt.show()