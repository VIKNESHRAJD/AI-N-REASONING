class BayesNode:
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def probability(self, value, evidence):
        key = tuple(evidence[P] for P in self.parents)
        P = self.cpt[key]
        return P if value else 1 - P


class BayesNet:
    def __init__(self, nodes):
        self.nodes = {n.name: n for n in nodes}
        self.variables = [n.name for n in nodes]


def normalize(Q):
    S = sum(Q.values())
    return {k: v / S for k, v in Q.items()}


def enumerate_all(vars, e, bn):
    if not vars:
        return 1.0

    v, rest = vars[0], vars[1:]
    node = bn.nodes[v]

    if v in e:
        return node.probability(e[v], e) * enumerate_all(rest, e, bn)

    total = 0
    for V in (True, False):
        ev = e.copy()
        ev[v] = V
        total += node.probability(V, ev) * enumerate_all(rest, ev, bn)

    return total


def enumerate_ask(x, e, bn):
    Q = {}
    for X in (True, False):
        ex = e.copy()
        ex[x] = X
        Q[X] = enumerate_all(bn.variables, ex, bn)

    return normalize(Q)


B = BayesNode("B", [], {(): 0.001})
E = BayesNode("E", [], {(): 0.002})

A = BayesNode("A", ["B", "E"], {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001,
})

J = BayesNode("J", ["A"], {(True,): 0.90, (False,): 0.05})
M = BayesNode("M", ["A"], {(True,): 0.70, (False,): 0.01})

bn = BayesNet([B, E, A, J, M])
result = enumerate_ask("B", {"J": True, "M": True}, bn)

print("P(B | J=True, M=True)")
print("B=True:", round(result[True], 4))
print("B=False:", round(result[False], 4))