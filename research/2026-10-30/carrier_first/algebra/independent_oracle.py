"""Separate subset-incidence and SymPy reference: no carrier API imports.

Finite calibration is not an independent external referee or an analytic proof.
"""
import itertools as it
import json
import math
import sympy as S

rows = {}
# Three-color Vandermonde bijection reconstructed by actual subset intersections.
three_blocks = 0
for sizes in ((2,3,4),(1,4,2),(3,1,3)):
    a,b,c = sizes
    for k in range(a+b+c+1):
        tally = {}
        for subset in it.combinations(range(a+b+c), k):
            grades = (sum(x<a for x in subset),sum(a<=x<a+b for x in subset),sum(x>=a+b for x in subset))
            tally[grades] = tally.get(grades, 0)+1
        for grades,count in tally.items():
            assert count == math.prod(math.comb(n,j) for n,j in zip(sizes,grades))
            three_blocks += 1
rows['three_coloured_subset_fibers'] = three_blocks

# Reconstruct Newton coefficients from forward differences of ordinary
# polynomial matrix products, not the implementation's overlap formula.
x=S.symbols('x')
fall=lambda k:S.prod(x-j for j in range(k))/S.factorial(k)
L=[S.Matrix([[i-2,S.Rational(2,i+3)],[i*i+1,3-i]]) for i in range(5)]
R=[S.Matrix([[2*i+1,1-i],[S.Rational(3,i+2),i+4]]) for i in range(4)]
f=sum((m*fall(i) for i,m in enumerate(L)),S.zeros(2))
g=sum((m*fall(i) for i,m in enumerate(R)),S.zeros(2))
product_polynomial=S.simplify(f*g)
overlap_rows=0
for k in range(8):
    finite_difference=sum(((-1)**(k-j)*math.comb(k,j)*product_polynomial.subs(x,j) for j in range(k+1)),S.zeros(2))
    count_coeff=S.zeros(2)
    for i,a in enumerate(L):
        for j,b in enumerate(R):
            r=i+j-k
            if 0<=r<=min(i,j):
                count_coeff += a*b*S.factorial(k)/(S.factorial(r)*S.factorial(i-r)*S.factorial(j-r))
    assert S.simplify(finite_difference-count_coeff)==S.zeros(2)
    overlap_rows+=1
rows['matrix_product_grades'] = overlap_rows

# Fresh matrix path construction through dynamic endpoint dictionaries.
edge=lambda n,k,b:S.Matrix([[n+3,b+k+1],[n-k+2,2*b+n+1]])
states={(0,0):[S.eye(2)]}
checked=0
for depth in range(8):
    for (n,k),matrices in states.items():
        d=edge(n+1,k,1)*edge(n,k,0)-edge(n+1,k+1,0)*edge(n,k,1)
        for pre in matrices:
            # Compare two literal one-step extensions with the local defect.
            a=edge(n+1,k,1)*(edge(n,k,0)*pre)
            b=edge(n+1,k+1,0)*(edge(n,k,1)*pre)
            assert a-b==d*pre
            checked+=1
    nxt={}
    for (n,k),matrices in states.items():
        for bit in (0,1):
            nxt.setdefault((n+1,k+bit),[]).extend(edge(n,k,bit)*m for m in matrices)
    states=nxt
rows['fresh_reachable_diamond_cases']=checked

# Original pole law combined symbolically; strict derivative decomposition.
n=S.symbols('n',positive=True)
r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
a=8*n-7
grouped=6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5))
assert S.factor(r-grouped)==0
numeric_r=lambda k:r.subs(n,k)
native=sum(16**(8-j)*numeric_r(j) for j in range(1,9))
reversal=sum(16**(8-j)*numeric_r(9-j) for j in range(1,9))
orders=((2,1,3,4,5,6,7,8),(8,2,6,4,5,3,7,1),(3,4,1,2,7,8,5,6))
for p in orders:
    lift=sum(16**(7-j)*numeric_r(k) for j,k in enumerate(p))
    assert reversal<lift<native
rows['fresh_bbp_source_orders']=len(orders)
rows['exact_native_minus_reverse_N8']=str(native-reversal)
rows['symbolic_four_pole_identity']=True
rows['status']='PASS'
rows['sympy_version']=S.__version__
rows['authority']='distinct implementation; shared theorem/source and model lineage'
print(json.dumps(rows,indent=2))
