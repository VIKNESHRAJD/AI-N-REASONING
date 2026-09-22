class BayesNode:
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def probability(self, value, evidence):
        """Return P(self=value | parent values in evidence)."""
        key = tuple(evidence[parent] for parent in self.parents)
        probability_true = self.cpt[key]
        return probability_true if value else 1 - probability_true


class BayesNet:
    def __init__(self, nodes):
        self.nodes = {node.name: node for node in nodes}
        self.variables = [node.name for node in nodes]


def normalize(distribution):
    total = sum(distribution.values())
    if total == 0:
        raise ValueError("Cannot normalize a distribution with a zero total.")
    return {key: value / total for key, value in distribution.items()}


def enumerate_all(variables, evidence, bayes_net):
    """Compute the probability of the evidence by enumeration."""
    if not variables:
        return 1.0

    variable, rest = variables[0], variables[1:]
    node = bayes_net.nodes[variable]

    if variable in evidence:
        return node.probability(evidence[variable], evidence) * enumerate_all(
            rest, evidence, bayes_net
        )

    total = 0.0
    for value in (True, False):
        extended_evidence = evidence.copy()
        extended_evidence[variable] = value
        total += node.probability(value, extended_evidence) * enumerate_all(
            rest, extended_evidence, bayes_net
        )

    return total


def enumerate_ask(variable, evidence, bayes_net):
    """Return the normalized posterior distribution for a Boolean variable."""
    distribution = {}

    for value in (True, False):
        extended_evidence = evidence.copy()
        extended_evidence[variable] = value
        distribution[value] = enumerate_all(
            bayes_net.variables, extended_evidence, bayes_net
        )

    return normalize(distribution)


if __name__ == "__main__":
    B = BayesNode("B", [], {(): 0.001})
    E = BayesNode("E", [], {(): 0.002})
    A = BayesNode(
        "A",
        ["B", "E"],
        {
            (True, True): 0.95,
            (True, False): 0.94,
            (False, True): 0.29,
            (False, False): 0.001,
        },
    )
    J = BayesNode("J", ["A"], {(True,): 0.90, (False,): 0.05})
    M = BayesNode("M", ["A"], {(True,): 0.70, (False,): 0.01})

    bayes_net = BayesNet([B, E, A, J, M])
    result = enumerate_ask("B", {"J": True, "M": True}, bayes_net)

    print("P(B | J=True, M=True)")
    print(f"B=True:  {result[True]:.4f}")
    print(f"B=False: {result[False]:.4f}")
