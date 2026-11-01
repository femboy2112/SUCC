"""Exact four-pole BBP path interactions and adversarial source diagnostics.

Pure stdlib rationals. Finite arithmetic; analytic claims proved in PROOFS.md.
Main XVIII original four signed poles and literal U0=0 are unchanged.
"""
from fractions import Fraction as F
from math import comb

SHIFTS = (7, 4, 3, 2)
WEIGHTS = (4, -2, -1, -1)
EDGES = ((3, 2), (4, 1), (5, 1))


def _pos(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive integer required')


def four_pole_source(n):
    _pos(n)
    return sum((F(w, 8*n-c) for c,w in zip(SHIFTS,WEIGHTS)), F(0))


def edge_source(n, length):
    _pos(n)
    if length not in (3,4,5):
        raise ValueError('only the original three BBP edge lengths')
    a=8*n-7
    return F(1,a)-F(1,a+length)


def three_edge_source(n):
    return sum((weight*edge_source(n,m) for m,weight in EDGES),F(0))


def channel_states(N):
    """Exact zero-boundary states U_3,U_4,U_5; U=2 U_3+U_4+U_5."""
    if type(N) is not int or N<0: raise ValueError('N >= 0')
    u={m:F(0) for m,_ in EDGES}
    outputs={m:[F(0)] for m,_ in EDGES}
    for n in range(1,N+1):
        for m,_ in EDGES:
            u[m]=16*u[m]+edge_source(n,m)
            outputs[m].append(u[m])
    return {m:tuple(rows) for m,rows in outputs.items()}


def combined_states(N):
    v=channel_states(N)
    return tuple(sum((w*v[m][i] for m,w in EDGES),F(0)) for i in range(N+1))


def laurent_moment(j):
    if type(j) is not int or j<0:raise ValueError('moment index nonnegative')
    return sum(w*c**j for c,w in zip(SHIFTS,WEIGHTS))


def edge_moment(j):
    """M_j=int_0^5 W(s)(7-s)^j ds; (j+1)M_j = m_(j+1)."""
    if type(j) is not int or j<0:raise ValueError('j>=0')
    return sum((F(w*(7**(j+1)-(7-m)**(j+1)),j+1) for m,w in EDGES),F(0))


def laurent_prefix(n,J):
    """Positive ascending source Laurent path + certified all-J real tail upper."""
    _pos(n)
    if type(J) is not int or J<0:raise ValueError('J nonnegative')
    x=8*n
    partial=sum((F(laurent_moment(j),x**(j+1)) for j in range(J+1)),F(0))
    # 0<m_j<4*7^j for j>=1; geometric positive remainder bound.
    upper=F(4*7**(J+1), x**(J+2))*F(x,x-7)
    return {'partial':partial,'positive_remainder':four_pole_source(n)-partial,
            'tail_upper':upper}


def pole_poly():
    """Q(x)=(x-7)(x-4)(x-3)(x-2) ascending coefficients."""
    q=[1]
    for c in SHIFTS:
        nxt=[0]*(len(q)+1)
        for i,a in enumerate(q):
            nxt[i]-=c*a
            nxt[i+1]+=a
        q=nxt
    return tuple(q)


def atomic_hankel(d):
    _pos(d)
    return tuple(tuple(laurent_moment(i+j) for j in range(d)) for i in range(d))


def rational_det(matrix):
    """Independent Laplace expansion for small matrices, exact.
    Deliberately not Bareiss/Prony elimination to vary implementation route.
    """
    A=[[F(x) for x in row] for row in matrix]
    n=len(A)
    if not n:return F(1)
    if any(len(row)!=n for row in A):raise ValueError('square matrix')
    if n==1:return A[0][0]
    return sum(((-1)**j*A[0][j]*rational_det([row[:j]+row[j+1:] for row in A[1:]])
                for j in range(n)),F(0))


def solve_exact(A,b):
    """RREF using rational Gaussian elimination; fails closed if singular."""
    if len(A)!=len(b) or any(len(row)!=len(b) for row in A):
        raise ValueError('square system')
    n=len(b);rows=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if rows[i][j]),None)
        if pivot is None:raise ValueError('singular matrix')
        rows[j],rows[pivot]=rows[pivot],rows[j]
        p=rows[j][j]
        rows[j]=[x/p for x in rows[j]]
        for i in range(n):
            if i==j:continue
            f=rows[i][j]
            if f: rows[i]=[x-f*y for x,y in zip(rows[i],rows[j])]
    return tuple(rows[i][-1] for i in range(n))


def prony_recover():
    """Recover monic Q from only the first 8 SIGNED moments m_0..m_7.

    Unique only among <=4 DISTINCT finite atomic poles, not arbitrary sources.
    """
    H=atomic_hankel(4)
    q=solve_exact(H, tuple(-laurent_moment(i+4) for i in range(4)))
    return q+(F(1),)


def prony_weights(shifts=SHIFTS):
    """Given roots of recovered Q, first 4 moments determine all weights."""
    if len(shifts)!=4 or len(set(shifts))!=4:raise ValueError('4 distinct roots')
    return solve_exact(tuple(tuple(c**j for c in shifts) for j in range(4)),
                       tuple(laurent_moment(j) for j in range(4)))


def continuous_hankel(n,d):
    """Moment Gram G_ij=r(n+i+j), exact positive for any n>=1, d>=1."""
    _pos(n);_pos(d)
    return tuple(tuple(four_pole_source(n+i+j) for j in range(d)) for i in range(d))


def discrete_hausdorff_difference(n,k):
    """Positive (-1)^k Delta^k r(n) for all n>=1,k>=0."""
    _pos(n)
    if type(k) is not int or k<0:raise ValueError('k>=0')
    return sum(((-1)**j*comb(k,j)*four_pole_source(n+j) for j in range(k+1)),F(0))


def finite_difference_null(n,order=8):
    """Positive N(n)=B(8n,order+1) with first `order` Laurent moments 0."""
    _pos(n)
    if type(order) is not int or order<1:raise ValueError('order positive')
    return sum((F((-1)**j*comb(order,j),8*n+j)
                for j in range(order+1)),F(0))


def finite_difference_null_closed(n,order=8):
    _pos(n)
    if type(order) is not int or order<1:raise ValueError('positive order')
    from math import factorial
    d=1
    for j in range(order+1):d*=8*n+j
    return F(factorial(order),d)


def null_moment(j,order=8):
    if type(j) is not int or j<0 or type(order) is not int or order<1:
        raise ValueError('nonnegative j, positive order')
    return sum((-1)**i*comb(order,i)*(-i)**j for i in range(order+1))


def pairwise_balanced_conspiracy(p):
    """Exact finite 3-channel counterfeit with pairwise Haar, triple lock.

    For every (a,b) mod p, define x=a, y=b, z=-2a-b.
    All three pair projections cover p^2 pairs exactly once if p odd.
    Yet 2*x+y+z=0 mod p for every path.
    NOT an original-source BBP orbit; source-attestation negative control.
    """
    if type(p) is not int or p<3 or p%2==0:
        raise ValueError('odd modulus p>=3')
    paths=tuple((a,b,(-2*a-b)%p) for a in range(p) for b in range(p))
    pairs=[]
    for i,j in ((0,1),(0,2),(1,2)):
        hist={}
        for x in paths:
            key=(x[i],x[j]);hist[key]=hist.get(key,0)+1
        pairs.append(hist)
    return {'p':p,'count':len(paths),'pair_histograms':tuple(pairs),
            'marginal_perfect':all(len(v)==p*p and all(t==1 for t in v.values()) for v in pairs),
            'triple_coherent':all((2*x+y+z)%p==0 for x,y,z in paths)}


def continuous_alias_certificate(h=1,q=F(1,5)):
    """Rational universal bounds for a NONZERO seed and coherent alias witness.

    Analytic source interpolation, monotone phase and Poisson are proved
    in PROOFS.md. No numerical integral is claimed to have been evaluated.
    q>=3/16 is required; q=1/5 gives complete 16-power phase coherence.
    """
    if type(h) is not int or not h or type(q) not in (int,F) or F(q)<F(3,16):
        raise ValueError('nonzero integer h and rational q>=3/16')
    q=F(q)
    # π>3, log16>2, |Z_N|<1/(5πq log16 |h|) <1/(30q|h|)
    zero_alias_upper=F(1,30*q*abs(h))
    return {'q':q,'h':h,'smooth_zero_alias_upper':zero_alias_upper,
            'coherent_completed_orbit':q==F(1,5),
            'coherent_integer_sum_error_upper':F(11*abs(h),56) if q==F(1,5) else None,
            'nonzero_alias_lower_at_N':
                (lambda N:F(N)-F(11*abs(h),56)-zero_alias_upper) if q==F(1,5) else None}


def mutant_completion_prefix(K,epsilon=F(1)):
    """Exact ε*Σ_(j=1)^K 16^-j B(8j,9) and strict future upper.

    The completed (infinite) BBP-style source constant shifts by a positive
    value for ε>0 although its first eight Laurent moments are UNCHANGED.
    """
    _pos(K)
    if type(epsilon) not in (int,F) or F(epsilon)<=0:
        raise ValueError('positive rational mutation strength')
    epsilon=F(epsilon)
    partial=epsilon*sum((F(1,16**j)*finite_difference_null(j) for j in range(1,K+1)),F(0))
    # b_j decreasing, 16^-j geometric tail => < 16^-K b_(K+1)/15.
    future_upper=epsilon*F(1,15*16**K)*finite_difference_null(K+1)
    return {'prefix':partial,'tail_upper':future_upper,
            'completed_strictly_positive':True}


def mutant_states(N,epsilon=F(1)):
    """A 13-pole-mutation at source forcing, BUT literal U0=0 retained.

    This is a COUNTERMODEL; original source is never replaced silently.
    """
    if type(N) is not int or N<0 or type(epsilon) not in (int,F):
        raise ValueError('N>=0 and exact rational epsilon')
    u=F(0);out=[u]
    for n in range(1,N+1):
        u=16*u+four_pole_source(n)+F(epsilon)*finite_difference_null(n)
        out.append(u)
    return tuple(out)


def prime_clock_laurent(j,n):
    """Signed Laurent moments' exact prime clocks and Q2 divergence receipt.

    j>=1, n>=1: m_j is ODD, x=8n has v2>=3; the real
    term m_j/x^(j+1) has v2=-(j+1)*(3+v2(n)). Thus terms do not
    even tend to zero in Q2 although the summed rational r(n) lies in Z2.
    """
    _pos(j);_pos(n)
    k=n;v=0
    while k%2==0:
        v+=1;k//=2
    m=laurent_moment(j)
    assert m%2==1
    return {'j':j,'n':n,'moment':m,'v2_term':-(j+1)*(3+v),
            'm_mod3':m%3,'m_mod5':m%5,
            'predicted_mod3':(2-(-1)**j)%3}
