"""Source-anchored divisor fibers and Oily two-channel transfer (exact finite core).

This module implements *arithmetic models*, not relativistic physics, the
physical Planck constant, or a factor of SUCC's selected zero-seeded BBP
carry orbit. All matrix and occupation coefficients use exact Fraction.

Relevant existing SUCC sources: WOC-01..04 and RSFP-01..05; source versions
and matrix/readout are deliberately kept distinct from global zeta states.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt, log

SOURCE = "origin-locked-prime-fiber-oily-v1"


def _fraction(x):
    if type(x) not in (int, F):
        raise TypeError("exact int/Fraction inputs only")
    return F(x)


def _matmul(A, B):
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in (0, 1)), F(0))
                       for j in (0, 1)) for i in (0, 1))


def _matinv(A):
    a,b=A[0];c,d=A[1]; det=a*d-b*c
    if det == 0:
        raise ValueError("frame must be invertible")
    return ((d/det,-b/det),(-c/det,a/det))


def _matpow(M, n: int):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative matrix exponent")
    res=((F(1),F(0)),(F(0),F(1)))
    while n:
        if n&1: res=_matmul(res,M)
        M=_matmul(M,M)
        n>>=1
    return res


def oily_rates(x):
    x=_fraction(x)
    if not (0 <= x <= 1):
        raise ValueError("authentic Oily x in [0,1]")
    u=x-x*x/2
    v=x*x/2
    return u,v


def upper_two_mode(q1,q2,c=1):
    q1,q2,c=map(_fraction,(q1,q2,c))
    return ((q1,c),(F(0),q2))


def transfer_source_response(q1,q2,j,c=1):
    """ell M^(j+1) b with b=e2, ell=e1^T, exact; j>=0."""
    if type(j) is not int or j<0:
        raise ValueError("nonnegative grade")
    return _matpow(upper_two_mode(q1,q2,c),j+1)[0][1]


def symmetric_character(q1,q2,j):
    q1,q2=map(_fraction,(q1,q2))
    if type(j) is not int or j<0:
        raise ValueError("nonnegative grade")
    return sum((q1**a*q2**(j-a) for a in range(j+1)),F(0))


def oily_packet(x,j):
    x=_fraction(x)
    u,v=oily_rates(x)
    return (1-x)*transfer_source_response(u,v,j)/4


def frame_transform(M,b,ell,G):
    """New-frame representation, with ALL source/input/output maps transported.

    v_new=G^-1 v_old; output is invariant: ell M^j b.
    """
    m=_matmul(_matmul(_matinv(G),M),G)
    inv=_matinv(G)
    bb=tuple(sum((inv[i][k]*b[k] for k in (0,1)),F(0)) for i in (0,1))
    ll=tuple(sum((ell[k]*G[k][j] for k in (0,1)),F(0)) for j in (0,1))
    return m,bb,ll


def readout(M,b,ell,k):
    A=_matpow(M,k)
    return sum((ell[i]*A[i][j]*b[j] for i in (0,1) for j in (0,1)),F(0))


def anchored_gauge_lower_shear(c):
    """Most general GL2 frame fixing literal e2 input and e1 readout."""
    c=_fraction(c)
    return ((F(1),F(0)),(c,F(1)))


def is_anchored_upper_labeled(M, u,v):
    """Retains specified upper triangle AND literal diagonal source labels."""
    u,v=map(_fraction,(u,v))
    return M[1][0]==0 and M[0][0]==u and M[1][1]==v


def divisors(n):
    if type(n) is not int or n<1:
        raise ValueError("source index is a positive integer")
    ans=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            ans.append(d)
            if d*d!=n:
                ans.append(n//d)
    return tuple(sorted(ans))


def origin_fiber(n):
    """All ordered a*b=n source-preserving virtual paths."""
    return tuple((d,n//d) for d in divisors(n))


def divisor_multiplicity(n):
    return len(origin_fiber(n))


def prime_exponents(n):
    if type(n) is not int or n<1:
        raise ValueError("positive source index required")
    cur=n; out=[];d=2
    while d*d<=cur:
        if cur%d==0:
            exp=0
            while cur%d==0:
                cur//=d;exp+=1
            out.append((d,exp))
        d+=1 if d==2 else 2
    if cur>1:out.append((cur,1))
    return tuple(out)


def fiber_dimension_by_prime(n):
    out=1
    for _,exp in prime_exponents(n):out*=exp+1
    return out


def conditional_imbalance_variance_coefficients(n):
    """Var(log(a/b)|ab=n) = sum_p coeff[p]*log(p)^2 exactly.

    Uniform over all d(n) factor-pairs, not a product zeta^2 prior.
    """
    return {p:F(j*(j+2),3) for p,j in prime_exponents(n)}


def conditional_imbalance_variance_numeric(n):
    return sum(float(k)*log(p)**2 for p,k in
               conditional_imbalance_variance_coefficients(n).items())


def prime_split_even_moment(j):
    if type(j) is not int or j<0:
        raise ValueError("nonnegative prime power")
    return sum(((2*a-j)**2 for a in range(j+1)),0)


def conditional_path_character_numeric(n,t):
    """Uniform divisor-fiber phase (not a BBP digit character)."""
    from cmath import exp
    if not isinstance(t,(int,float)):
        raise TypeError("finite numerical t only")
    paths=origin_fiber(n)
    return sum((exp(1j*t*log(a/b)) for a,b in paths),0j)/len(paths)


def exact_source_gibbs_marginal(n, beta, cutoff):
    """Finite N≤cutoff isometric zeta lift mass, exactly n^-beta/Z_cutoff."""
    if type(beta) is not int or beta<2 or type(cutoff) is not int or cutoff<n or n<1:
        raise ValueError("integer beta>=2; 1<=n<=cutoff")
    z=sum((F(1,k**beta) for k in range(1,cutoff+1)),F(0))
    return F(1,n**beta)/z


def exact_source_gibbs_pair_mass(a,b,beta,cutoff):
    """One pair's squared amplitude in J|psi>, with J uniform per n.

    Sum all pairs ab=n and recover n^-beta / Z exactly.
    """
    if type(a) is not int or type(b) is not int or min(a,b)<1:
        raise ValueError("positive factor labels")
    n=a*b
    return exact_source_gibbs_marginal(n,beta,cutoff)/divisor_multiplicity(n)


def exact_two_mode_pair_mass(a,b,beta,cutoff):
    """Two-channel unconditioned Gibbs pair mass with product ab<=cutoff."""
    if type(a) is not int or type(b) is not int or min(a,b)<1 or a*b>cutoff:
        raise ValueError("1<=ab<=cutoff")
    z=sum((F(divisor_multiplicity(k),k**beta) for k in range(1,cutoff+1)),F(0))
    return F(1,(a*b)**beta)/z


def prime_local_oily_coefficient(p, beta, j):
    """The unnormalized balanced TWO-mode prime-local coefficient.

    The single prime p=2,beta=1 is valid locally even though ζ(1) diverges.
    """
    if type(beta) is not int or beta<1 or type(p) is not int or p<2 or type(j) is not int or j<0:
        raise ValueError("integer beta>=1, p>=2, j>=0")
    if len(prime_exponents(p))!=1 or prime_exponents(p)[0]!=(p,1):
        raise ValueError("genuine prime required")
    q=F(1,p**beta)
    return transfer_source_response(q,q,j)


def counterfeit_character_same_source_different_coupling(q1,q2,j,c1=1,c2=0):
    """Trace/symmetric character agrees, while marked readout changes."""
    a=transfer_source_response(q1,q2,j,c1)
    b=transfer_source_response(q1,q2,j,c2)
    character=symmetric_character(q1,q2,j)
    return character,a,b


def naive_prime_one_channel_fidelity_squared(n,p):
    """Exactly |<omega_(pn), A_p omega_n>|^2, A_p|(a,b)>=|(pa,b)>.

    A_p is an isometry of pair space but does NOT transport the coherent
    uniform arithmetic fiber to the next coherent fiber.
    """
    if type(p) is not int or p<2 or prime_exponents(p)!=((p,1),):
        raise ValueError("genuine prime required")
    j=dict(prime_exponents(n)).get(p,0)
    return F(j+1,j+2)


def naive_prime_compressed_shift_sq(n,p):
    """Squared coefficient of J* A_p J on |n> = fidelity squared."""
    return naive_prime_one_channel_fidelity_squared(n,p)


def cumulative_prime_recoherence_fidelity_squared(p,j):
    """Product of sequential coherent-projection overlaps at p^0..p^j."""
    if type(j) is not int or j<0:
        raise ValueError("nonnegative occupation")
    out=F(1)
    for k in range(j):
        out*=naive_prime_one_channel_fidelity_squared(p**k,p)
    return out


def harmonic_recoherence_budget(j):
    """Exact rational harmonic budget H_j; logarithmic cost log(j+1) separately."""
    if type(j) is not int or j<0:
        raise ValueError("nonnegative depth")
    return sum((F(1,k) for k in range(1,j+1)),F(0))
