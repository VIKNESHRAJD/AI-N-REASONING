#BFS

from collections import deque

def breadth_first_search(graph, initial_state, goal_state):
    initial_node = {"state": initial_state, "path": [initial_state], "path_cost": 0}

    if initial_state == goal_state:
        return initial_node["path"]

    frontier = deque([initial_node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        current_state = node["state"]
        current_path = node["path"]
        current_cost = node["path_cost"]

        print(f"\n Expanding node: {current_state}")
        print(f"Current path: {current_path}")

        explored.add(current_state)

        for child_state in graph.get(current_state, []):
            frontier_states = {frontier_node["state"] for frontier_node in frontier}

            if child_state not in explored and child_state not in frontier_states:
                child_node = {
                    "state": child_state,
                    "path": current_path + [child_state],
                    "path_cost": current_cost + 1,
                }
                print(f"Generated Child: {child_state}")

                if child_state == goal_state:
                    print(f"Goal State {goal_state} found")
                    return child_node["path"]

                frontier.append(child_node)

        print("Frontier:", [frontier_node["state"] for frontier_node in frontier])
        print("Explored:", explored)

    return None


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C", "I"],
    "H": ["E"],
    "I": ["G"],
}

initial_state = "A"
goal_state = "I"

solution = breadth_first_search(graph, initial_state, goal_state)

if solution is not None:
    print("\n Solution Path:")
    print("-->".join(solution))
    print("Path cost:", len(solution) - 1)
else:
    print("\n Failure: No Path Exists.")



#dfs
def depth_first_search(graph, initial_state, goal_state):

    initial_node = {
        'state': initial_state,
        'path': [initial_state],
        'path_cost': 0
    }

    if initial_state == goal_state:
        return initial_node['path']

    frontier = [initial_node]
    explored = set()

    while frontier:

        node = frontier.pop()

        current_state = node['state']
        current_path = node['path']
        current_cost = node['path_cost']

        print("\nExpanding Node:", current_state)
        print("Current Path:", current_path)

        if current_state in explored:
            continue

        if current_state == goal_state:
            print(f"\nGoal State {goal_state} found")
            return current_path

        explored.add(current_state)

        frontier_states = {
            frontier_node['state']
            for frontier_node in frontier
        }

        for child_state in graph.get(current_state, []):

            if (
                child_state not in explored
                and child_state not in frontier_states
            ):

                child_node = {
                    'state': child_state,
                    'path': current_path + [child_state],
                    'path_cost': current_cost + 1
                }

                print("Generated Child:", child_state)

                frontier.append(child_node)

                frontier_states.add(child_state)

        print("Frontier:",
              [frontier_node['state'] for frontier_node in frontier])

        print("Explored:", explored)

    return None
graph = {
    "A": ["C", "B"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C", "I"],
    "H": ["E"],
    "I": ["G"],
}

initial_state = "A"
goal_state = "I"

solution = depth_first_search(graph, initial_state, goal_state)

if solution is not None:
    print("\n Solution Path:")
    print("-->".join(solution))
    print("Path cost:", len(solution) - 1)
else:
    print("\n Failure: No Path Exists.")


#ucs
import heapq
def uniform_cost_search(graph,initial_state,goal_state):
    initial_node={
        "state":initial_state,
        "path":[initial_state],
        "path_cost":0
    }
    frontier=[]
    insertion_number=0
    heapq.heappush(frontier,
                   (initial_node["path_cost"],
                    insertion_number,
                    initial_node))
    explored=set()
    frontier_costs={initial_state:0}
    while frontier:
        current_cost,_,node=heapq.heappop(frontier)
        current_state=node['state']
        current_path=node['path']
        if current_state in explored:
            continue
        if current_cost!=frontier_costs.get(current_state,float("inf")):
            continue
        del frontier_costs[current_state]
        print("\n Expanding node :",current_state)
        print("current path:", current_path)
        print("current path cost:", current_cost)
        if current_state==goal_state:
            print("\n Goal State found")
            return current_path, current_cost
        explored.add(current_state)
        for child_state,step_cost in graph.get(current_state,[]):
            new_cost=current_cost+step_cost
            child_node={
                "state":child_state,
                "path":current_path+[child_state],
                "path_cost":new_cost
            }
            if( child_state not in explored and child_state not in frontier_costs):
                insertion_number+=1
                heapq.heappush(frontier,(new_cost,insertion_number,child_node))
                frontier_costs[child_state]=new_cost
                print(f"Added {child_state} "f" with cost {new_cost}")
            elif(child_state in frontier_costs and new_cost<frontier_costs[child_state]):
                insertion_number+=1
                heapq.heappush(frontier, (new_cost, insertion_number, child_node))
                frontier_costs[child_state]=new_cost
                print(f"Replace Path to {child_state}" f"with cheaper cost{new_cost}")
            print("explored:",explored)
            print("Frontier:",{state:cost for state, cost in frontier_costs.items()})
    return None

graph={"A":[("B",2),("C",5)],
       "B":[("A",2),("C",1)],
       "C":[("A",5),("B",1)]}
initial_state="A"
goal_state="C"

result=uniform_cost_search(graph, initial_state,goal_state)

if result is not None:
    solution_path,total_cost=result
    print("\n Solution Path:")
    print("-->".join(solution_path))
    print("Total Path Cost:",total_cost)
else:
    print("\n Failure: No Path Exists")
                      

#A STAR

import heapq

def a_star_search(graph, heuristic, initial_state, goal_state):
    # Initialize the starting node
    initial_node = {
        'state': initial_state,
        'path': [initial_state],
        'g': 0,
        'h': heuristic[initial_state],
        'f': heuristic[initial_state]
    }
    
    if initial_state == goal_state:
        return initial_node['path']
        
    frontier = []
    counter = 0
    # Push: (f_score, unique_counter, node_dict)
    heapq.heappush(frontier, (initial_node['f'], counter, initial_node))
    explored = set()
    
    while frontier:
        _, _, node = heapq.heappop(frontier)
        current_state = node['state']
        current_path = node['path']
        current_g = node['g']
        current_h = node['h']
        
        # If already visited with a shorter path, skip
        if current_state in explored:
            continue
            
        print(f"\nExpanding node {current_state}")
        print(f"current_path: {current_path}")
        print(f"g={current_g}, h={current_h}, f={current_g + current_h}")
        
        if current_state == goal_state:
            print(f"\nGoal State {goal_state} found!")
            return current_path
            
        explored.add(current_state)
        
        # Expand neighbors
        for child_state, cost in graph.get(current_state, []):
            if child_state not in explored:
                child_g = current_g + cost
                child_h = heuristic[child_state]
                child_f = child_g + child_h
                
                child_node = {
                    'state': child_state, 
                    'path': current_path + [child_state], 
                    'g': child_g, 
                    'h': child_h, 
                    'f': child_f
                }
                print(f"Generated child: {child_state} (g={child_g}, h={child_h}, f={child_f})")
                
                counter += 1
                heapq.heappush(frontier, (child_f, counter, child_node))
                
        print("frontier:", [(f_node['state'], f_score) for f_score, _, f_node in frontier])
        print("Explored:", explored)
        
    return None

# Graph Definition
graph = {
    'A': [('B', 2), ('C', 4)], 
    'B': [('A', 2), ('D', 3), ('E', 5)], 
    'C': [('A', 4), ('F', 2), ('G', 5)], 
    'D': [('B', 3)], 
    'E': [('B', 5), ('H', 3)], 
    'F': [('C', 2)], 
    'G': [('C', 4), ('I', 2)], 
    'I': [('G', 2)]
}

heuristic = {'A': 6, 'B': 5, 'C': 4, 'D': 7, 'E': 4, 'F': 4, 'G': 2, 'H': 3, 'I': 0}
initial_state = 'A'
goal_state = 'I'

solution = a_star_search(graph, heuristic, initial_state, goal_state)

if solution is not None:
    print('\nSolution path:')
    print('-->'.join(solution))
else:
    print('\nFailure: No path exists')


#ENUMERATION
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

#ELIMINATION
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

#hmm

import numpy as np
import matplotlib.pyplot as plt

#define hmm parameters
T=np.array([[0.7,0.3],[0.3,0.7]])
o={
    1:np.diag([0.9,0.2]),
    0:np.diag([0.1,0.8])
}
N,d=20,3
rng=np.random.default_rng(12)

#generate random hiddent states and observations
hidden=[]
observations=[]
state=rng.choice(2,p=[0.5,0.5])
for i in range(N):
    state=rng.choice(2,p=T[state])
    umbrella=int(rng.random()<[0.9,0.2][state])
    hidden.append(state)
    observations.append(umbrella)
print('observations',observations)

#FILTERING
def filter_step(f,e):
    f=o[e]@T.T@f
    return f/f.sum()
f=np.array([0.5,0.5])
filtered=[]
for obs in observations:
    f=filter_step(f,obs)
    filtered.append(f.copy())
filtered=np.array(filtered)

#direct backward recursion for verification
def backward(k,t):
    b=np.ones(2)
    for i in range(t-1,k-1,-1):
        b=T@o[observations[i]]@b
    return b

#incremeatl fixed lag smoothing
k=1
t=k+1
B=np.eye(2)
for i in range(k,t):
    B=B@T@o[observations[i]]
smoothed=np.full((N,2),np.nan)
errors=[]
print('\n Current Day|Smoothed Day|Rainy|Not Rainy|Error')
print('_'*60)
while True:
    # ALTERED: Fetch stable f directly from your filtered array to stop drift accumulation
    f_stable = filtered[k-1] 
    
    #compute smoothed distribution
    b=B@np.ones(2)
    smooth=f_stable*b
    smooth=smooth/smooth.sum()
    smoothed[k-1]=smooth
    #verify using direct backward recursion
    b_direct=backward(k,t)
    direct=f_stable*b_direct
    direct=direct/direct.sum()
    error=np.max(np.abs(smooth-direct))
    errors.append(error)
    print(f'{t:11}|{k:12}|{smooth[0]:.4f}|{smooth[1]:.4f}|{error:.2e}')
    if t==N:
        break
    #Equation(14.16):
    #B_new=O_old^(-1) T^(-1) B_old T O_new
    B=np.linalg.solve(
        o[observations[k]],
        np.linalg.solve(T,B)
    )@T@o[observations[t]]
    
    # ALTERED: Normalize matrix B to prevent inversion numerical scaling blow-ups
    B = B / np.linalg.norm(B) 
    
    k+=1
    t+=1
print('\n Maximum Veification Error:',max(errors))

#6.plot filtering and smoothing results
days=np.arange(1,N+1)
valid=~np.isnan(smoothed[:,0])
fig,ax=plt.subplots(3,1,figsize=(11,10),
                    sharex=True)
#PLOT 1:Actual Hidden States and observations 
actual_rain=1-np.array(hidden)
ax[0].step(days,actual_rain,where='mid',label='Actual Rain State',linewidth=2)
ax[0].scatter(days,observations,marker='x',color='red',s=60,label='Actual Rain State',linewidth=2)
ax[0].set_ylabel('state/observations')
ax[0].set_title('Hidden States and Observations')
ax[0].set_yticks([0,1])
ax[0].grid(True,alpha=0.3)
#Plot 2:Filtering and Fixed lag smoothing
ax[1].plot(days,filtered[:,0],'o-',label='Filtering P(Rainy)',alpha=0.8)
ax[1].plot(days[valid],smoothed[valid,0],'s-',label=f'fixed_lag smoothing(d={d})',linewidth=2)
ax[1].set_ylabel('Probability')
ax[1].set_title('Filtering vs Fixed Lag Smoothing')
ax[1].set_ylim(0,1)
ax[1].legend()
ax[1].grid(True,alpha=0.3)
#plot 3 Verification error
ax[2].semilogy(days[valid],
               np.maximum(errors,1e-17),'o-')
ax[2].set_xlabel('Day')
ax[2].set_ylabel('Absolute error')
ax[2].set_title('Incremental vs Direct Backward Smoothing')
ax[2].grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('HMM_FIXED_LAG_SMOOTHING.png',dpi=300)
plt.show()


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

# 2. Full joint distribution table (all 32 combinations)
print("\n B E A J M | Joint Probability")
print("-" * 35)
total = 0
for B, E, A, J, M in product([1, 0], repeat=5):
    jp = joint_probability(B, E, A, J, M)
    total += jp
    print(f" {B} {E} {A} {J} {M} | {jp:.8f}")

# 3. Check: all joint probabilities must add up to 1
print("\nSum of all joint probabilities =", round(total, 6))