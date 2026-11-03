#BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

start = 'A'
goal = 'I'

queue = [[start]]
visited = []

while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)

        visited.append(node)

        if node == goal:
            print("Frontier:", [p for p in queue])
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Cost:", len(path) - 1)
            break

        for child in graph[node]:
            if child not in visited:
                queue.append(path + [child])

        print("Frontier:", queue)
        print("Explored:", visited)

else:

    print("No path exists")



#  2. Depth-First Search (DFS)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

stack = [['A']]
visited = []

while stack:
    path = stack.pop()
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)

        visited.append(node)


        if node == 'I':
            print("Frontier:", stack)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", len(path) - 1)
            break

        for child in graph[node]:
            if child not in visited:
                stack.append(path + [child])

        print("Frontier:", stack)
        print("Explored:", visited)

else:
    print("No path exists")


#3. Uniform Cost Search (UCS)


graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 5), ('B', 1)]
}

start = 'A'
goal = 'C'

queue = [(0, [start])]
visited = []

while queue:
    queue.sort()
    cost, path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)
        print("Current Cost:", cost)

        visited.append(node)

        if node == goal:
            print("Frontier:", queue)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", cost)
            break

        for child, weight in graph[node]:
            if child not in visited:
                queue.append((cost + weight, path + [child]))

        print("Frontier:", queue)
        print("Explored:", visited)

else:
    print("No path exists")

#  4. A* Search

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3), ('E', 5)],
    'C': [('A', 4), ('F', 2), ('G', 4)],
    'D': [('B', 3)],
    'E': [('B', 5), ('H', 3)],
    'F': [('C', 2)],
    'G': [('C', 4), ('I', 2)],
    'H': [('E', 3)],
    'I': [('G', 2)]
}

h = {
    'A': 6, 'B': 5, 'C': 4, 'D': 7,
    'E': 4, 'F': 4, 'G': 2, 'H': 3, 'I': 0
}

start = 'A'
goal = 'I'

queue = [(h[start], 0, [start])]
visited = []

while queue:
    queue.sort()
    f, g, path = queue.pop(0)
    node = path[-1]

    if node not in visited:
        print("\nExpanding Node:", node)
        print("Current Path:", path)
        print("G Cost:", g)
        print("H Cost:", h[node])
        print("F Cost:", f)

        visited.append(node)

        if node == goal:
            print("Frontier:", queue)
            print("Explored:", visited)
            print("Goal Found!")
            print("Path:", path)
            print("Path Cost:", g)
            break

        for child, cost in graph[node]:
            if child not in visited:
                new_g = g + cost
                new_f = new_g + h[child]
                queue.append((new_f, new_g, path + [child]))

        print("Frontier:", queue)
        print("Explored:", visited)

else:
    print("No path exists")


print("Probabilities:", probability)

plt.bar(x, probability, label="PMF")
plt.title("Bernoulli Distribution")
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.xticks(x, ["Failure(0)", "Success(1)"])
plt.legend()
plt.show()


## Joint Probability
#join prob
#JOINT PROBABILITY IN BAYESIAN NETWORK
from itertools import product

# CPTs (same as enumeration program; True=1, False=0)
P_B = 0.001
P_E = 0.002
P_A = {(1, 1): 0.95, (1, 0): 0.94, (0, 1): 0.29, (0, 0): 0.001}   # P(A=T | B,E)
P_J = {1: 0.90, 0: 0.05}                                           # P(J=T | A)
P_M = {1: 0.70, 0: 0.01}                                           # P(M=T | A)

def joint_probability(B, E, A, J, M):
    # P(B,E,A,J,M) = P(B) * P(E) * P(A|B,E) * P(J|A) * P(M|A)
    b_p = P_B if B else 1 - P_B
    e_p = P_E if E else 1 - P_E
    a_p = P_A[(B, E)] if A else 1 - P_A[(B, E)]
    j_p = P_J[A] if J else 1 - P_J[A]
    m_p = P_M[A] if M else 1 - P_M[A]
    return b_p * e_p * a_p * j_p * m_p

# 1. Joint probability of ONE specific combination
# Example: J=True, M=True, A=True, B=False, E=False
p = joint_probability(B=0, E=0, A=1, J=1, M=1)
print("P(J=T, M=T, A=T, B=F, E=F) =", p)

# Full joint distribution table (all 32 combinations)
print("\n B E A J M | Joint Probability")
print("-" * 35)
total = 0
for B, E, A, J, M in product([1, 0], repeat=5):
    jp = joint_probability(B, E, A, J, M)
    total += jp
    print(f" {B} {E} {A} {J} {M} | {jp:.8f}")

# Check: all joint probabilities must add up to 1
print("\nSum of all joint probabilities =", round(total, 6))


#  8. Bayesian Network: Traffic Example

pip install pgmpy

import matplotlib.pyplot as plt
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD

H = DiscreteBayesianNetwork([
    ('Rain','Traffic'), ('Accident','Traffic'),
    ('Heavy-Vehicle','Traffic')
])

R = TabularCPD('Rain', 2, [[0.2],[0.8]])
A = TabularCPD('Accident', 2, [[0.95],[0.05]])
V = TabularCPD('Heavy-Vehicle', 2, [[0.25],[0.75]])
T = TabularCPD('Traffic', 2,
    [[0,0.25,0.95,0.9625,0.2,0.4,0.06,0.07],
     [1,0.75,0.05,0.0375,0.8,0.6,0.94,0.93]],
    evidence=['Rain','Accident','Heavy-Vehicle'],
    evidence_card=[2,2,2])

H.add_cpds(R,A,V,T)
print("Model is valid:", H.check_model())

for c in H.get_cpds():
    print(c)

p = [(1,3),(3,3),(5,3),(3,1)]
n = ['Rain','Accident','Heavy-Vehicle','Traffic']

fig, ax = plt.subplots()
for i in range(4):
    ax.text(p[i][0],p[i][1],n[i],ha='center',
            bbox=dict(boxstyle='round',fc='lightgreen'))

for i in range(3):
    ax.annotate('',xy=(3,1.2),xytext=(p[i][0],2.8),
                arrowprops=dict(arrowstyle='->'))

ax.set_xlim(0,6)
ax.set_ylim(0,4)
ax.axis('off')
plt.show()

# 9. Bayesian Inference: Burglary–Earthquake–Alarm

P_B, P_E = 0.001, 0.002
P_A = {(1,1):0.95, (1,0):0.94, (0,1):0.29, (0,0):0.001}
P_J, P_M = {1:0.90, 0:0.05}, {1:0.70, 0:0.01}

F = {}
for B in [1,0]:
    for E in [1,0]:
        F[B,E] = 0
        for A in [1,0]:
            p = P_A[B,E] if A else 1-P_A[B,E]
            F[B,E] += p * P_J[A] * P_M[A]

Q = {}
for B in [1,0]:
    Q[B] = P_B * (F[B,1]*P_E + F[B,0]*(1-P_E))
Q[0] = Q[0] * (1-P_B) / P_B

s = Q[1] + Q[0]
print("P(B | J=True, M=True)")
print("B=True :", Q[1]/s)
print("B=False:", Q[0]/s)

# ## 10. Enumeration Algorithm

from itertools import product

# 1, 2, 3, 4. Simple Flat CPT mapping (True=1, False=0 for shorthand)
# Format: P(B), P(E), P(A|B,E), P(J|A), P(M|A)
P_B = {(): 0.001}
P_E = {(): 0.002}
P_A = {(1, 1): 0.95, (1, 0): 0.94, (0, 1): 0.29, (0, 0): 0.001}
P_J = {(1,): 0.90, (0,): 0.05}
P_M = {(1,): 0.70, (0,): 0.01}

# Buckets to collect matching probabilities for B=True (1) and B=False (0)
Q = {1: 0.0, 0: 0.0}

# 5. Flat Loop Enumeration (Checks all 32 combinations of B, E, A, J, M)
for B, E, A, J, M in product([1, 0], repeat=5):

    # Filter: Only process rows that match our Evidence (J=True, M=False)
    if J == 1 and M == 1:

        # Calculate individual node probabilities (p if true, 1-p if false)
        b_p = P_B[() ] if B else 1 - P_B[() ]
        e_p = P_E[() ] if E else 1 - P_E[() ]
        a_p = P_A[(B, E)] if A else 1 - P_A[(B, E)]
        j_p = P_J[(A,)] if J else 1 - P_J[(A,)]
        m_p = P_M[(A,)] if M else 1 - P_M[(A,)]

        # Joint Probability = Product of all nodes
        joint = b_p * e_p * a_p * j_p * m_p

        # Add to the respective B bucket (True or False)
        Q[B] += joint

# Normalization Step
s = sum(Q.values())
print(f"B=True : {round(Q[1]/s, 4)}")
print(f"B=False: {round(Q[0]/s, 4)}")

# ## 11. Hidden Markov Model (HMM): Forward and Backward

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

# # Quick Revisio
import numpy as np
import matplotlib.pyplot as plt

T = np.array([[.7,.3],[.3,.7]])
O = {1:np.diag([.9,.2]), 0:np.diag([.1,.8])}
N,d = 20,3
r = np.random.default_rng(12)

h,o = [],[]
s = r.choice(2,p=[.5,.5])

for i in range(N):
    s = r.choice(2,p=T[s])
    h.append(s)
    o.append(int(r.random()<[.9,.2][s]))

print("observation:",o)

def step(F,e):
    F = O[e] @ T.T @ F
    return F/F.sum()

F = np.array([.5,.5])
filtered = []

for e in o:
    F = step(F,e)
    filtered.append(F.copy())

filtered = np.array(filtered)

def back(k,t):
    b = np.ones(2)
    for i in range(t-1,k-1,-1):
        b = T @ O[o[i]] @ b
    return b

F,k,t = filtered[0].copy(),1,4
B = np.eye(2)

for i in range(k,t):
    B = B @ T @ O[o[i]]

smoothed = np.full((N,2),np.nan)
errors = []

print("In current Day | Smoothed P(Rainy) | Not Rainy | Error")
print("-"*60)

while True:
    S = F*(B @ np.ones(2))
    S /= S.sum()
    smoothed[k-1] = S

    D = F*back(k,t)
    D /= D.sum()
    errors.append(np.max(np.abs(S-D)))

    print(f"{t:11} | {k:12} | {S[0]:.4f} | {S[1]:.4f} | {errors[-1]:.2e}")

    if t == N: break

    B = np.linalg.solve(O[o[k]],np.linalg.solve(T,B)) @ T @ O[o[t]]
    F = step(F,o[k])
    k,t = k+1,t+1

print("\nMaximum verification error:",max(errors))

days = np.arange(1,N+1)
v = ~np.isnan(smoothed[:,0])

fig,ax = plt.subplots(3,1,figsize=(11,10),sharex=True)

ax[0].step(days,1-np.array(h),where="mid",label="Actual Rain state")
ax[0].scatter(days,o,marker='x',color="red",s=60,label="umbrella observation")
ax[0].set_ylabel("state / observation")
ax[0].set_title("Hidden state and observation")
ax[0].set_yticks([0,1])
ax[0].legend()
ax[0].grid(True,alpha=.3)

ax[1].plot(days,filtered[:,0],"o-",label="Filtering P(Rainy)")
ax[1].plot(days[v],smoothed[v,0],"s-",label=f"Fixed - Lag smoothing (d={d})")
ax[1].set_ylabel("Probability")
ax[1].set_title("Filtering vs Fixed-Lag smoothing")
ax[1].set_ylim(0,1)
ax[1].legend()
ax[1].grid(True,alpha=.3)

ax[2].semilogy(days[v],np.maximum(errors,1e-17),"o-")
ax[2].set_xlabel("Day")
ax[2].set_ylabel("Absolute Error")
ax[2].set_title("Incremental vs Direct Backward smoothing")
ax[2].grid(True,alpha=.3)

plt.tight_layout()
plt.savefig("HMM_fixed_Lag_smoothing.png",dpi=300)
plt.show()

