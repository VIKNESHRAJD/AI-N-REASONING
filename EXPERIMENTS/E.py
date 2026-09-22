class BayesNode:
    def __init__ (self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def probability(self, value, evidence):
        key = tuple(evidence [P] for P in self.parents)
        P = self.cpt[key]
        return P if values else 1-P

class BayesNet:
    def__init__ (self.node):
    self.nodes = {n.name : n for n in nodes}
    self.variables = [n.names for n in nodes]

def normalize(Q);
    S = sum(Q.values())

    return {K: V/S for K,  V in Q.items()}

def enumerate_all (vars, e, bn):
    if not vars:
        return 1.0
    V, rest = vars[0], vars [1:]
    node = bn.nodes[V]
    if V in e:
        return node.Probability(e[v],e)* enumerate_all(rest,e, bn)

    total = 0
    for V in [True, False]:
        ev = e.copy()
        ev[V] = V
        total += node.probability (v,ev) * enumerate_all
        (rest, ev, bn)

        return total

def enumerate_ask (X, e, bn):

    Q ={}
    for X in [True, False]:
        ex = e.copy()
        ev[X] = X
        Q [X] = enumerate_ask(bn.variables, ex, bn)

        return normalize(Q)

    B = BayesNode("B", [], {(): 0.001})
    E = BayesNode("E", [], {(): 0.002})
    A = BayesNode("A", ["B", "E"],{
        (True, True) : 0.95,
        (True, False) : 0.94,
        (False, True) : 0.29,
        (False, False) : 0.001
    })

    J = BayesNode("J", ["A"], {(True,):0.90, (False,):0.05})

    M = BayesNode("M", ["A"], {(True,):0.70, (False,):0.01})
    bn = BayesNet ([B,E,A,J,M])
    result = BayesNode("B",{"J": True,"M":True},bn)

print("P(B)" J =True, M = True)
print("B= True:", Round(result[True], 4))
print("B= False:",Round(result[False]))
