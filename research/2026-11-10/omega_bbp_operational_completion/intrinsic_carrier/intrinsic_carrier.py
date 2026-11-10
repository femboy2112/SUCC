"""Source-independent arithmetic-carrier Hamiltonians and reversible radix lifts.

Research prototype. No claim of RH, pi normality, or efficient quantum advantage.
All finite matrices use exact fractions; the lambda/carry compiler remains a separate gate.
"""
from __future__ import annotations
from fractions import Fraction


def matmul(a,b):
    assert len(a)>0 and len(b)>0 and len(a[0])==len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Fraction())
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matplus(a,b,sign=1):
    return [[a[i][j]+sign*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def block_matrices(p):
    """Unit-basis block |p m + a>, a=0,...,p-1, m>=1.

    B is Haar low-pass onto equal block amplitude; Q is prime-divisibility
    hub projection; C=BQ-QB is real skew, and H=iC is Hermitian.
    """
    if not isinstance(p, int) or p<2: raise ValueError('p>=2')
    B=[[Fraction(1,p) for _ in range(p)] for _ in range(p)]
    Q=zero(p);Q[0][0]=Fraction(1)
    C=matplus(matmul(B,Q),matmul(Q,B),sign=-1)
    H2=[[-a for a in row] for row in matmul(C,C)]
    return B,Q,C,H2


def arithmetic_edge(p,m,a):
    """The source-free, oriented prime/digit edge from p*m to p*m+a."""
    if type(p)!=int or p<2 or type(m)!=int or m<1 or type(a)!=int or not (1<=a<p):
        raise ValueError('p>=2,m>=1,1<=a<p')
    return p*m,p*m+a


def affines(p,m,a):
    """Check Vp S=S^p Vp in the N>=1 carrier, and return child address."""
    if not (isinstance(p,int) and p>=2 and isinstance(m,int) and m>=1 and isinstance(a,int) and 0<=a<p):
        raise ValueError('bad arguments')
    assert p*(m+1)==p*m+p
    return p*m+a


def invert_affine(p,n):
    """Inverse child address for n>=p; boundary n=1,...,p-1 is absent."""
    if type(p)!=int or p<2 or type(n)!=int or n<1: raise ValueError('bad arguments')
    if n<p: return None
    return divmod(n,p)


def sigma_square(p):
    if type(p)!=int or p<2: raise ValueError('p>=2')
    return Fraction(p-1,p*p)


def check_operator(p):
    B,Q,C,H2=block_matrices(p)
    z=zero(p)
    assert matmul(B,B)==B and matmul(Q,Q)==Q
    assert transpose(B)==B and transpose(Q)==Q
    assert transpose(C)==matplus(z,C,sign=-1)
    assert matmul(matmul(C,C),C)==[[ -sigma_square(p)*x for x in row] for row in C]
    assert H2[0][0]==sigma_square(p)
    for a in range(1,p):
        assert H2[a][a]==Fraction(1,p*p)
        assert C[a][0]==Fraction(1,p) and C[0][a]==-Fraction(1,p)
    assert sum((H2[i][i] for i in range(p)),Fraction())==2*sigma_square(p)
    return True


def thermal_trace_finite(p,beta,blocks):
    """Exact Tr(e^{-beta log N} H_p^2) across full p-blocks m=1..blocks.

    H_p vanishes on boundary 1<=n<p. Integer beta>=2 keeps rational data.
    """
    if type(beta)!=int or beta<2 or type(blocks)!=int or blocks<1:
        raise ValueError('integer beta>=2, blocks>=1')
    return sum((Fraction(p-1,p*p*(p*m)**beta) +
                sum((Fraction(1,p*p*(p*m+a)**beta) for a in range(1,p)),Fraction())
               for m in range(1,blocks+1)),Fraction())


def thermal_trace_rearranged(p,beta,zeta_beta):
    """Exact symbolic rearrangement valid for beta>1 and actual zeta(beta)."""
    h=sum((Fraction(1,a**beta) for a in range(1,p)),Fraction())
    return (zeta_beta*(1+Fraction(p-2,p**beta))-h)/p**2


def prime_mixed_norm_sum_bound(sigma,upper):
    """Absolute operator norm bound for finite prime-weighted H_sigma.

    For Re sigma>1/2, infinite bound by sum_{n>=2} log(n)/n^(sigma+1/2).
    This is a sufficient convergence region, not an RH or continuation result.
    """
    from math import log,sqrt
    def prime(k): return k>=2 and all(k%d for d in range(2,int(sqrt(k))+1))
    return sum(log(p)*p**(-sigma)*sqrt(p-1)/p for p in range(2,upper+1) if prime(p))


def branch_parity_twist(p):
    """An actual (-1) character of cyclic branch increment exists iff p even."""
    if type(p)!=int or p<2: raise ValueError('p>=2')
    sign=[(-1)**k for k in range(p)]
    shifted=[sign[(k-1)%p] for k in range(p)]
    return sign, shifted, shifted==[-x for x in sign]


def original_source_R(n):
    if type(n)!=int or n<0: raise ValueError('n>=0')
    return (Fraction(4,8*n+1)-Fraction(2,8*n+4)
            -Fraction(1,8*n+5)-Fraction(1,8*n+6))


def source_prefix(L):
    if type(L)!=int or L<0: raise ValueError('L>=0')
    return sum((original_source_R(j)/16**(j+1) for j in range(L)),Fraction())


def source_phase_bound(n,L):
    """Rigorous upper bound for 16^n * (pi/16 - source_prefix(L)).

    Uses the factored positive Mellin polynomial, not decimal pi evaluation.
    """
    if type(n)!=int or n<0 or type(L)!=int or L<1: raise ValueError('n>=0,L>=1')
    return Fraction(16**n,16**L*(8*L+1)*(8*L+2))


def conditional_phase_horizon(A,h,epsilon):
    """Sufficient source clock L for worst-case epoch phase displacement <=epsilon/(2pi).

    Finite rational bound only. It DOES NOT bound the Weyl mean itself.
    """
    if A<1 or type(h)!=int or epsilon<=0: raise ValueError('bad params')
    L=2*A
    while 16**(2*A-1)*abs(h)*Fraction(1,1)/ (16**L*(8*L+1)*(8*L+2)) >epsilon:
        L+=1
    return L


if __name__=='__main__':
    for p in (2,3,4,5,7,16):assert check_operator(p)
    print('Exact carrier block checks passed')


def whole_carrier_haar_projection(p,N):
    """Exact truncation on |n> for 1<=n<=N, omitting incomplete p-blocks."""
    if type(N)!=int or N<1 or type(p)!=int or p<2:raise ValueError('p,N invalid')
    P=zero(N)
    for first in range(p,N+1,p):
        if first+p-1>N:break
        for a in range(first,first+p):
            for b in range(first,first+p):P[a-1][b-1]=Fraction(1,p)
    return P


def boundary_bulk_two_three(M):
    """(B2,B3) on N=6M+5; leaves finite 1..5 boundary plus M bulk 6-blocks."""
    if type(M)!=int or M<1:raise ValueError('M>=1')
    N=6*M+5
    P=whole_carrier_haar_projection(2,N)
    Q=whole_carrier_haar_projection(3,N)
    return matplus(matmul(P,Q),matmul(Q,P),-1)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Fraction())


def omega_haar_source_area(n):
    """Exact six-window oriented bilinear pairing, independent of the seed."""
    if type(n)!=int or n<0:raise ValueError('n>=0')
    P=zero(6);Q=zero(6)
    for j in range(0,6,2):
        for a in range(j,j+2):
            for b in range(j,j+2):P[a][b]=Fraction(1,2)
    for j in range(0,6,3):
        for a in range(j,j+3):
            for b in range(j,j+3):Q[a][b]=Fraction(1,3)
    C=matplus(matmul(P,Q),matmul(Q,P),-1)
    v=[original_source_R(n+j) for j in range(6)]
    w=[original_source_R(n+j+1) for j in range(6)]
    Cw=[dot(row,w) for row in C]
    return dot(v,Cw)
