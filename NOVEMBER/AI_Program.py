# Exported from AI_Program (1).ipynb

# # Python Programs – Complete Explanation and Code
#
# **Combined practical study notebook**
#
# This notebook contains all 11 uploaded programs. Each topic includes:
# - Purpose and concept
# - Important terms and formulas
# - Step-by-step explanation
# - Original uploaded Python program in an executable code cell
# - A short interpretation or study note
#
# Run the code cells in order. Some programs require packages such as `numpy`, `matplotlib`, `scipy`, and `pgmpy`.
#
# ## Installation (if required)
#
# ```python
# %pip install numpy matplotlib scipy pgmpy
# ```
#
# For graph plots, run the notebook in Jupyter Notebook, JupyterLab, or Google Colab.

# ## Contents
#
# 1. Breadth-First Search (BFS)
# 2. Depth-First Search (DFS)
# 3. Uniform Cost Search (UCS)
# 4. A* Search
# 5. Bernoulli Distribution
# 6. Binomial Distribution
# 7. Continuous Uniform Distribution
# 8. Bayesian Network – Traffic Example
# 9. Bayesian Inference – Burglary, Earthquake and Alarm
# 10. Enumeration Algorithm
# 11. Hidden Markov Model – Forward and Backward

# ## 1. Breadth-First Search (BFS)
#
# **Purpose:** BFS explores a graph level by level. It visits nearer nodes before deeper nodes.
#
# **Key concepts**
# - **Queue (FIFO):** First In, First Out. `pop(0)` removes the oldest path.
# - **Frontier:** Paths waiting to be explored.
# - **Visited:** Nodes already expanded.
# - With equal edge costs, BFS finds a path with the fewest edges.
#
# **Step-by-step**
# 1. `graph` stores each node and its neighbours.
# 2. `queue = [[start]]` begins with the path `['A']`.
# 3. The oldest path is removed using `pop(0)`.
# 4. `path[-1]` identifies the current node.
# 5. If the node is the goal, the path and its edge count are printed.
# 6. Otherwise, paths extended by each unvisited neighbour are added to the queue.
# 7. `len(path) - 1` counts the edges in the path.
#
# > **Important note:** BFS is suitable for finding a minimum-edge path when all edges have equal cost.

# In[4]
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

# ## 2. Depth-First Search (DFS)
#
# **Purpose:** DFS follows one branch as deeply as possible before backtracking.
#
# **Key concepts**
# - **Stack (LIFO):** Last In, First Out. `pop()` removes the most recently added path.
# - **Frontier:** Paths waiting on the stack.
# - **Visited:** Nodes already expanded.
# - DFS does not generally guarantee the shortest path.
#
# **Step-by-step**
# 1. `stack = [['A']]` initializes the search.
# 2. `pop()` selects the most recently added path.
# 3. The last node in the path becomes the current node.
# 4. The node is added to `visited` if it has not been expanded.
# 5. If it is the goal `I`, the path and path cost are printed.
# 6. Otherwise, paths through unvisited neighbours are pushed onto the stack.
# 7. The next path explored is the one most recently added.
#
# > **Important note:** The visit order depends on the order in which neighbours are appended to the stack.

# In[6]

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

# ## 3. Uniform Cost Search (UCS)
#
# **Purpose:** UCS selects the path with the lowest accumulated edge cost.
#
# **Key concepts**
# - Each edge has a numerical weight.
# - `cost` is the sum of the edge weights in the current path.
# - The queue is sorted by cost; the cheapest candidate is selected first.
#
# **Step-by-step**
# 1. The graph stores neighbours together with edge costs.
# 2. The queue starts with `(0, ['A'])`.
# 3. `queue.sort()` orders candidate paths by cost.
# 4. `pop(0)` selects the lowest-cost path.
# 5. Each neighbour is added with `cost + weight`.
# 6. When the goal is selected, the program prints the path and total cost.
#
# > **Important note:** In the supplied graph, A → B → C costs 2 + 1 = 3, which is cheaper than direct A → C at cost 5. This is the small example's expected least-cost route.

# In[8]

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

# ## 4. A* Search
#
# **Purpose:** A* combines the cost already travelled with an estimate of the remaining cost.
#
# **Important formula**
#
# `f(n) = g(n) + h(n)`
#
# - `g(n)`: actual cost from the start to node `n`.
# - `h(n)`: heuristic estimate from node `n` to the goal.
# - `f(n)`: estimated total path cost through `n`.
#
# **Step-by-step**
# 1. The weighted graph defines the edge costs.
# 2. The `h` dictionary stores heuristic values; the goal `I` has heuristic 0.
# 3. The queue stores `(f, g, path)`.
# 4. The candidate with the smallest `f` is selected.
# 5. For each neighbour, `new_g = g + edge_cost`.
# 6. Then `new_f = new_g + h[child]`.
# 7. The program prints the costs, frontier and explored nodes, and stops when the goal is found.
#
# > **Important note:** UCS uses accumulated cost g(n). A* uses g(n) + h(n). If all heuristic values are zero, A* behaves like UCS.

# In[10]

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

# ## 5. Bernoulli Distribution
#
# **Purpose:** The Bernoulli distribution models one experiment with two possible outcomes: success (1) and failure (0).
#
# **Formula**
# - `P(X = 1) = p`
# - `P(X = 0) = 1 - p`
#
# For this program, `p = 0.3`.
#
# **Step-by-step**
# 1. `p = 0.3` sets the probability of success.
# 2. `x = [0, 1]` defines the two possible outcomes.
# 3. `probability = [(1-p), p]` calculates the probabilities `[0.7, 0.3]`.
# 4. The values are printed.
# 5. `plt.bar()` plots the probability mass function (PMF).
#
# **Expected output values:** Failure = 0.7; Success = 0.3.
#
# > **Important note:** The two probabilities must add up to 1. Mean = p and variance = p(1-p).

# In[12]
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

# ## 6. Binomial Distribution
#
# **Purpose:** The binomial distribution gives the probability of obtaining `x` successes in `n` independent trials, with the same success probability `p` on every trial.
#
# **Formula**
#
# `P(X=x) = C(n,x) p^x (1-p)^(n-x)`
#
# **Program values**
# - `n = 8`: number of trials.
# - `p = 0.5`: probability of success in each trial.
# - `x` ranges from 0 to 8.
#
# **Step-by-step**
# 1. `np.arange(n + 1)` creates the possible success counts.
# 2. `binom.pmf(x, n, p)` calculates the probability for each count.
# 3. `plt.bar()` draws the PMF.
# 4. `plt.plot()` overlays points joined by a line.
# 5. Axis labels and title describe the graph.
#
# > **Important note:** For n=8 and p=0.5, the distribution is symmetric around 4 successes. Mean = np = 4; variance = np(1-p) = 2.

# In[14]
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

# ## 7. Continuous Uniform Distribution
#
# **Purpose:** A continuous uniform random variable has constant probability density over a specified interval.
#
# **Program values**
# - `loc = 0.01`: lower endpoint.
# - `scale = 0.99`: interval width.
# - Upper endpoint = `0.01 + 0.99 = 1.00`.
# - `size = 100`: number of random samples.
#
# **Step-by-step**
# 1. `uniform.rvs()` generates 100 random values.
# 2. `uniform.pdf()` calculates the density at the first sample.
# 3. `plt.hist(..., density=True)` draws a normalized histogram.
# 4. `plt.axhline(1/0.99)` draws the theoretical density level.
# 5. Labels and title describe the graph.
#
# For this interval, the PDF height is `1/0.99`, approximately 1.0101.
#
# > **Important note:** For a continuous random variable, probability at one exact point is zero; probabilities are measured over intervals. The total area under the PDF is 1.

# In[16]
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

# ## 8. Bayesian Network: Traffic Example
#
# **Purpose:** This program builds a Bayesian network in which Rain, Accident and Heavy-Vehicle are parent variables that influence Traffic.
#
# **Key concepts**
# - A Bayesian network is a directed acyclic graph (DAG) representing probabilistic relationships.
# - Nodes represent random variables; arrows represent dependencies.
# - A CPD (Conditional Probability Distribution) stores probabilities for a variable given its parent variables.
# - `check_model()` checks whether the network and CPDs are consistent.
#
# **Step-by-step**
# 1. `DiscreteBayesianNetwork` defines three arrows into `Traffic`.
# 2. `R`, `A` and `V` define prior distributions for Rain, Accident and Heavy-Vehicle.
# 3. `T` defines the Traffic probabilities conditional on all three parents.
# 4. `evidence` lists the parent variables of Traffic.
# 5. `evidence_card=[2,2,2]` indicates that each parent has two states.
# 6. `add_cpds()` attaches the probability tables.
# 7. `check_model()` validates the model.
# 8. Matplotlib draws the nodes and arrows.
#
# > **Important note:** Three binary parent variables produce 2 × 2 × 2 = 8 parent-state combinations, so the Traffic CPD has 8 columns. Each column should sum to 1. Interpret row/state order according to the state encoding used in the model.

# In[18]
pip install pgmpy

# In[19]
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

# ## 9. Bayesian Inference: Burglary–Earthquake–Alarm
#
# **Purpose:** This program calculates the posterior probability of Burglary (B) given that John and Mary both call (J=True, M=True).
#
# **Variables**
# - `B`: Burglary
# - `E`: Earthquake
# - `A`: Alarm
# - `J`: John calls
# - `M`: Mary calls
#
# **Step-by-step**
# 1. The dictionaries store prior and conditional probabilities.
# 2. `F[B,E]` sums over both possible alarm states.
# 3. For each alarm state, the code uses either `P(A|B,E)` or its complement.
# 4. It multiplies the alarm probability by the likelihoods of the two calls.
# 5. `Q[B]` combines the two earthquake cases, weighted by the earthquake prior.
# 6. The false-burglary branch is adjusted by `(1-P_B)/P_B`.
# 7. The two values are normalized by their sum to obtain posterior probabilities.
#
# > **Important note:** The printed target is P(B | J=True, M=True), an updated probability after observing both calls.

# In[21]
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
#
# **Purpose:** Enumeration calculates a Bayesian query by checking all possible assignments of the network variables and summing the joint probabilities consistent with the evidence.
#
# **Key concepts**
# - There are five binary variables: B, E, A, J and M.
# - Total assignments = `2^5 = 32`.
# - `Q[1]` collects matching joint probabilities when B=True.
# - `Q[0]` collects matching joint probabilities when B=False.
# - Normalization divides each bucket by the total probability of the evidence.
#
# **Step-by-step**
# 1. `product([1,0], repeat=5)` generates all 32 assignments.
# 2. The `if` statement filters assignments to `J == 1 and M == 1`.
# 3. For each variable, the code selects its probability or complementary probability.
# 4. `joint` multiplies the probabilities for the full assignment.
# 5. The joint probability is added to the bucket for the value of B.
# 6. The final normalization produces the posterior probabilities.
#
# **Source-code note:** The comment in the uploaded file says `J=True, M=False`, but the actual condition is `if J == 1 and M == 1`. This notebook preserves the code and explains what it actually calculates.
#
# > **Important note:** Enumeration explicitly checks complete assignments. The el(1).py program instead groups and sums hidden-variable cases using nested loops.

# In[23]
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
#
# **Purpose:** This program implements Forward and Backward procedures for a two-state Hidden Markov Model using the observation sequence `[0, 1, 0]`.
#
# **Key concepts**
# - **Hidden states:** States that are not directly observed.
# - **Transition matrix T:** Probabilities of moving between hidden states.
# - **Observation/emission matrix O:** Probability of an observation given a hidden state.
# - **Forward:** Processes observations from left to right.
# - **Backward:** Processes observations from right to left.
#
# **Step-by-step**
# 1. `T` defines transitions between the two hidden states.
# 2. `O` defines emission probabilities for observations 0 and 1.
# 3. `obs = [0, 1, 0]` stores the observed sequence.
# 4. `forward()` starts with `[0.5, 0.5]`.
# 5. For each observation, it predicts the next-state probabilities using `T.T @ f`, then applies the observation likelihood `O[:, x]`.
# 6. The forward vector is normalized at each step.
# 7. `backward()` starts with `[1.0, 1.0]` and processes observations in reverse.
# 8. The program prints both vectors and plots them.
#
# **Note:** `H = 3` is defined in the supplied code but is not used later.
#
# > **Important note:** The final forward and backward vectors are not, by themselves, the smoothed posterior at every time step. To obtain a state posterior at a particular time, combine the corresponding forward and backward messages and normalize.

# In[25]
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

# # Quick Revision and Viva
#
# ## Search algorithm comparison
#
# | Algorithm | Main data structure / priority | Main idea |
# |---|---|---|
# | BFS | FIFO queue | Explores level by level |
# | DFS | LIFO stack | Explores deeply before backtracking |
# | UCS | Lowest accumulated cost `g` | Selects the cheapest path so far |
# | A* | Lowest `f = g + h` | Combines path cost and heuristic |
#
# ## Probability and AI terms
#
# - **PMF:** Probability Mass Function; gives probabilities for discrete outcomes.
# - **PDF:** Probability Density Function; describes density for continuous variables.
# - **Prior:** Probability before observing new evidence.
# - **Likelihood:** Probability of evidence under a particular hypothesis or state.
# - **Posterior:** Updated probability after considering evidence.
# - **CPD/CPT:** Conditional Probability Distribution/Table.
# - **Heuristic:** An estimate used by informed search, such as A*.
# - **HMM:** A model with hidden states, transition probabilities, observations and emission probabilities.
#
# ## Short viva questions
#
# 1. **What is BFS?** A graph search method that explores level by level using a FIFO queue.
# 2. **What is DFS?** A graph search method that explores deeply using a LIFO stack.
# 3. **Which search selects the lowest path cost?** Uniform Cost Search.
# 4. **What is the A* formula?** `f(n) = g(n) + h(n)`.
# 5. **What is a Bernoulli trial?** One experiment with two possible outcomes, often success and failure.
# 6. **Difference between Bernoulli and Binomial?** Bernoulli models one trial; Binomial models the number of successes in `n` independent trials.
# 7. **What is a continuous uniform distribution?** A distribution with constant density over a specified interval.
# 8. **What does a Bayesian network represent?** Probabilistic relationships using a directed acyclic graph and conditional probability tables.
# 9. **What is enumeration in Bayesian inference?** Summing joint probabilities over assignments consistent with the evidence.
# 10. **What does the Forward algorithm do?** Processes HMM observations from left to right.
# 11. **What does the Backward algorithm do?** Processes HMM observations from right to left.
#
# ## Exam preparation tip
#
# For every program, practise four things:
# 1. State the purpose of the algorithm, distribution or model.
# 2. Explain the important variables.
# 3. Describe the main loop, data structure or formula.
# 4. Interpret the output or graph.
