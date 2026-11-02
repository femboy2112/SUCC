"""Independently coded exact pole-path checks, no import of main model."""
from fractions import Fraction as F
from math import factorial, comb
from itertools import permutations


def combined_rational(n):
    if n<1: raise ValueError('n positive')
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def polynomial_expansion_x():
    """Independent product polynomial Q(x) via repeated root evaluation."""
    roots=(2,3,4,7)
    # explicit e1,e2,e3,e4 from subset combinatorics
    from itertools import combinations
    v=[]
    for k in (4,3,2,1,0):
        # coefficients ascending for x^k: (-1)^(4-k) e_(4-k)
        j=4-k
        v.append((-1)**j * sum(
            __import__('math').prod(z) for z in combinations(roots,j)))
    return tuple(v)  # descending x^4...x^0


def direct_signed_atom_moment(k):
    return 4*7**k-2*4**k-3**k-2**k


def permutation_determinant(mat):
    n=len(mat)
    total=F(0)
    for indices in permutations(range(n)):
        inv=sum(indices[i]>indices[j] for i in range(n) for j in range(i+1,n))
        term=F((-1)**inv)
        for i,j in enumerate(indices):term*=mat[i][j]
        total+=term
    return total


def independent_hausdorff_k(n,k):
    """Integrate t^(8n-8)(1-t^8)^k (4-2t^3-t^4-t^5)."""
    if n<1 or k<0:raise ValueError('n>=1 k>=0')
    out=F(0)
    for j in range(k+1):
        a=8*n+8*j-7
        out+=(-1)**j*comb(k,j)*(F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5))
    return out


def gamma_beta8n9(n):
    """Gamma(8n)*Gamma(9)/Gamma(8n+9)."""
    if n<1:raise ValueError('n>=1')
    return F(factorial(8)*factorial(8*n-1),factorial(8*n+8))


def counterfeit_character_histogram(p):
    """Independent linear-algebra generator of all p^2 counterexample paths."""
    if p<3 or p%2==0:raise ValueError('p odd')
    x=list(range(p));
    marginal=[]
    for v in ((1,0),(0,1),(-2,-1)):
        c=[0]*p
        for a in x:
            for b in x:c[(v[0]*a+v[1]*b)%p]+=1
        marginal.append(c)
    return marginal
