"""Independent exact-oracle implementations for selected finite claims.

Same mathematical source; distinct arithmetic decomposition; not an external referee.
"""
from fractions import Fraction as F
from math import gcd


def bbp_combined(n):
    return F((120*n*n-89*n+16), (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def reconstructed_state(n):
    # Different form: rational finite convolution rather than iterative update.
    return sum((16**(n-j)*bbp_combined(j) for j in range(1,n+1)), F(0))


def fraction_mod_2power(frac,level):
    q=1<<(4*level)
    x=F(frac)
    if x.denominator & 1 == 0:
        raise ValueError("odd denominator needed")
    # Extended Euclid rather than Python modular inverse.
    t,nt,r,nr=0,1,q,x.denominator
    while nr:
        k=r//nr
        t,nt=nt,t-k*nt
        r,nr=nr,r-k*nr
    if r!=1:raise ArithmeticError("denominator not a local unit")
    return (x.numerator*t)%q


def beta_matrix_square_via_composition():
    a,b=2,1
    # (a+b√2)^2 = (a²+2b²) + 2ab√2 = 6+4√2
    return ((a*a+2*b*b,4*a*b),(2*a*b,a*a+2*b*b))


def pisot_quotient_two_grid():
    # beta² L=2 L, so quotient is two independent parity coordinates.
    return {(a%2,b%2) for a in range(4) for b in range(4)}


def signed_root_histogram(q,k):
    # For Z/qZ, counts residue class of character exponents k*x.
    from collections import Counter
    return dict(Counter((k*x)%q for x in range(q)))


def kinetic_apply_to_linear_combination(q,vec,stride):
    d={}
    for x,a in vec.items():
        for pos,c in ((x,2),((x+stride)%q,-1),((x-stride)%q,-1)):
            d[pos]=d.get(pos,0)+a*c
    return {x:a for x,a in d.items() if a}
