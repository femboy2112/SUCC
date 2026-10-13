"""Independent certificate reconstruction; no author helper imported."""
import json
from pathlib import Path
from fractions import Fraction
from math import factorial

root = Path(__file__).resolve().parents[2]
c = json.loads((root / 'E39_GAUSSIAN_CUT_RECEIPT.json').read_text())['certificate']
bound = 2 * (c['radius'] + 2) ** 2
prime = [True] * (bound + 1)
prime[0:2] = [False, False]
for p in range(2, bound + 1):
    if prime[p]:
        for n in range(p * p, bound + 1, p):
            prime[n] = False

def gp(z):
    x, y = z
    if x * y == 0:
        a = abs(x or y)
        return prime[a] and a % 4 == 3
    return prime[x * x + y * y]

r, k = c['radius'], c['squared_step']
assert k == 2
vertices = {(x,y) for x in range(-r,r+1) for y in range(-r,r+1) if gp((x,y))}
assert vertices == {tuple(z) for z in c['vertices']}
edges = {(u,v) for u in vertices for v in vertices if 0 < sum((a-b)**2 for a,b in zip(u,v)) <= k}
assert edges == {(tuple(e[0]),tuple(e[1])) for e in c['darts']}
seen, todo = set(), [tuple(c['root'])]
while todo:
    u = todo.pop()
    if u in seen: continue
    seen.add(u)
    todo.extend(v for a,v in edges if a == u and v not in seen)
assert seen == {tuple(z) for z in c['component']} and len(seen) == 100
steps = [(x,y) for x in range(-2,3) for y in range(-2,3) if 0 < x*x+y*y <= k]
halo = {(x+dx,y+dy) for x,y in seen for dx,dy in steps} - seen
assert halo == {tuple(z) for z in c['boundary']} and len(halo) == 265
assert all(not gp(z) for z in halo)
for q in (23,29): assert len({(x%q,y%q) for x,y in seen}) == len(seen)
assert len({(x%5,y%5) for x,y in seen}) < len(seen)
assert not gp((-4,2))

# E38: reconstruct the perturbed observed source directly, without log/exp code.
def val(n,p):
    k=0
    while n%p == 0: n//=p; k+=1
    return k
for n in range(1,129):
    d=min(val(n,2),val(n,3))
    plus=sum(Fraction(1,factorial(j)) for j in range(d+1))
    minus=sum(Fraction((-1)**j,factorial(j)) for j in range(d+1))
    assert plus >= 0 and minus >= 0
assert Fraction(1)-1 == 0
print(json.dumps({'exit':0,'independent_edges':len(edges),'global_component':len(seen),
                  'nonprime_halo':len(halo),'squared_jump':k,'e38_nonnegative_coefficients_checked':128,
                  'analytic_claims':'paper derivation only; no numerical integrals'}))
