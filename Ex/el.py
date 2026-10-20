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