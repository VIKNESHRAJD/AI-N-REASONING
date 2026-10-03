from itertools import product

class Factor:
    def __init__(self, vars, table):
        self.vars, self.table = vars, table

def make_factor(v, e, bn):
    node = bn[v]
    vars = [p for p in node["parents"] if p not in e]
    if v not in e:
        vars.append(v)
    table = {}
    for values in product([True, False], repeat=len(vars)):
        a = dict(zip(vars, values))
        a.update(e)
        p = node["cpt"][tuple(a[x] for x in node["parents"])]
        table[values] = p if a[v] else 1 - p
    return Factor(vars, table)

def multiply(f1, f2):
    vars = list(dict.fromkeys(f1.vars + f2.vars))
    table = {}
    for values in product([True, False], repeat=len(vars)):
        a = dict(zip(vars, values))
        k1 = tuple(a[x] for x in f1.vars)
        k2 = tuple(a[x] for x in f2.vars)
        table[values] = f1.table[k1] * f2.table[k2]
    return Factor(vars, table)

def sum_out(v, factors):
    fs = [f for f in factors if v in f.vars]
    # FIX 1: Filter from f.vars instead of factors list
    others = [f for f in factors if v not in f.vars] 
    
    if not fs:
        return factors
        
    f = fs[0]
    for g in fs[1:]:
        f = multiply(f, g)
        
    vars = [x for x in f.vars if x != v]
    table = {}
    for values in product([True, False], repeat=len(vars)):
        a = dict(zip(vars, values))

        table[values] = sum(
            f.table[tuple((val if x == v else a[x]) for x in f.vars)] 
            for val in [True, False]
        )
    return others + [Factor(vars, table)]

def elimination_ask(x, e, bn, order):
    factors = []
    for v in order:
        factors.insert(0, make_factor(v, e, bn))
        if v != x and v not in e:
            factors = sum_out(v, factors)
            
    f = factors[0]
    for g in factors[1:]:
        f = multiply(f, g)
        
    result = {}

    for val in [True, False]:
        result[val] = f.table[tuple(val if v == x else e[v] for v in f.vars)]
        
    s = sum(result.values())
    return {k: v / s for k, v in result.items()}

bn = {
    "R": {"parents": [], "cpt": {(): 0.30}},
    "A": {"parents": [], "cpt": {(): 0.05}},
    "T": {"parents": ["R", "A"], "cpt": {
        (True, True): 0.90,
        (True, False): 0.70,
        (False, True): 0.60,
        (False, False): 0.10}},
    "D": {"parents": ["T"], "cpt": {(True,): 0.80, (False,): 0.20}},
    "M": {"parents": ["T"], "cpt": {(True,): 0.50, (False,): 0.05}}
}

result = elimination_ask("R", {"D": True, "M": True}, bn, ["M", "D", "T", "A", "R"])
print("P(R|D=TRUE,M=TRUE)")
print("R=TRUE:", round(result[True], 4))
print("R=FALSE:", round(result[False], 4))


# OUTPUT

P(R|D=TRUE,M=TRUE)
R=TRUE: 0.6767
R=FALSE: 0.3233


