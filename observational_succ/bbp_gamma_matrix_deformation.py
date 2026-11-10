"""Original BBP source Gamma deformation; research observer, NOT pi normality.

The source Gamma constant is an exact analytic identity. The matrix functional
calculus is a *defined observer* applied to P-H; no normality or mixing law is
inferred from it. mpmath precision is local; the original four-pole source is
imported from duck_bbp rather than rewritten.
"""
from __future__ import annotations

from fractions import Fraction

from observational_succ.duck_bbp import forcing

POLE_SHIFTS = (Fraction(1, 8), Fraction(1, 2), Fraction(5, 8), Fraction(3, 4))
POLE_WEIGHTS = (Fraction(28, 64), Fraction(-8, 64), Fraction(-3, 64), Fraction(-2, 64))
A = Fraction(15, 64)


def weighted_harmonic_step(n: int) -> Fraction:
    """n*r(n) exact, for integer n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return n * forcing(n)


def rational_pole_step(n: int) -> Fraction:
    """Independent partial fractions: sum_i w_i/(n-1+a_i)."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be positive")
    return sum((w/(Fraction(n-1)+a) for w,a in zip(POLE_WEIGHTS,POLE_SHIFTS)), Fraction())


def partial_finite_part(n: int) -> Fraction:
    """Exactly sum_{j<=n}(j*r(j)-15/(64*j)), no logs or roundoff."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be positive")
    return sum((weighted_harmonic_step(j)-A/j for j in range(1,n+1)), Fraction())


def bbp_gamma_digamma(dps: int = 60):
    """-sum_i w_i*digamma(a_i), the BBP source finite harmonic part."""
    import mpmath as mp
    if type(dps) is not int or dps < 20:
        raise ValueError("decimal precision must be >=20")
    with mp.workdps(dps):
        return +(-sum(mp.mpf(w.numerator)/w.denominator *
                     mp.digamma(mp.mpf(a.numerator)/a.denominator)
                     for w,a in zip(POLE_WEIGHTS,POLE_SHIFTS)))


def bbp_gamma_closed(dps: int = 60):
    """Exact elementary closed form, numerically evaluated at scoped precision."""
    import mpmath as mp
    if type(dps) is not int or dps < 20:
        raise ValueError("decimal precision must be >=20")
    with mp.workdps(dps):
        s=mp.sqrt(2)
        return +(mp.mpf(15)/64*mp.euler +(27+31*s)*mp.pi/128
                 +mp.mpf(39)/32*mp.log(2)+31*s/64*mp.log(1+s))


def pole_gamma_coordinate(x, dps: int = 60):
    """Scalar C(x)=-sum_i w_i digamma(a_i+x), x> -1/8 (real)."""
    import mpmath as mp
    with mp.workdps(dps):
        xx=mp.mpf(x)
        if xx <= -mp.mpf(1)/8:
            raise ValueError("x must exceed -1/8")
        return +(-sum(mp.mpf(w.numerator)/w.denominator *
                     mp.digamma(xx+mp.mpf(a.numerator)/a.denominator)
                     for w,a in zip(POLE_WEIGHTS,POLE_SHIFTS)))


def source_gamma_coefficient(m: int, dps: int = 70):
    """c_m=sum_i w_i*zeta(m+1,a_i), m>=1; signed coefficients alternating."""
    import mpmath as mp
    if type(m) is not int or m < 1:
        raise ValueError("m>=1 required")
    with mp.workdps(dps):
        return +(sum(mp.mpf(w.numerator)/w.denominator *
                     mp.zeta(m+1,mp.mpf(a.numerator)/a.denominator)
                     for w,a in zip(POLE_WEIGHTS,POLE_SHIFTS)))


def q_euler_constant(q, dps: int = 60):
    """Classical -psi_q(1), not the BBP source finite part. 0<q<1."""
    import mpmath as mp
    with mp.workdps(dps):
        q=(mp.mpf(q.numerator)/q.denominator if isinstance(q,Fraction) else mp.mpf(q))
        if not 0 < q < 1:
            raise ValueError("0<q<1 required")
        total=mp.nsum(lambda n: q**n/(1-q**n), [1,mp.inf])
        return +(mp.log(1-q)-mp.log(q)*total)


def matrix_source_gamma(transition, terms: int = 24, dps: int = 70):
    """C(P-H) by the convergent Hurwitz-zeta analytic functional calculus.

    P is a row-stochastic 16x16 matrix. Let X=P-H. Requires ||X||_2<1/8,
    the distance to the first digamma pole. Returns (matrix, rigorous series
    truncation upper bound for the mathematically exact Taylor series. It does
    NOT include floating-point rounding in coefficient or matrix operations.
    Numeric matrix values are diagnostics, not interval certificates.
    """
    import numpy as np
    if type(terms) is not int or terms < 1:
        raise ValueError("terms>=1 required")
    P=np.asarray(transition,dtype=np.float64)
    if P.shape!=(16,16) or not np.all(np.isfinite(P)):
        raise ValueError("16x16 finite matrix required")
    if np.any(P<0) or np.max(np.abs(P.sum(axis=1)-1))>1e-11:
        raise ValueError("P must be row stochastic")
    X=P-np.full((16,16),1/16)
    x=float(np.linalg.norm(X,2))
    if x>=1/8:
        raise ValueError("BBP Gamma Taylor series requires ||P-H||_2<1/8")
    C=float(bbp_gamma_digamma(dps))
    out=C*np.eye(16)
    power=np.eye(16)
    for m in range(1,terms+1):
        power=power@X
        out+=((-1)**m)*float(source_gamma_coefficient(m,dps))*power
    # |sum_i w_i zeta(m+1,a_i)| <=(41/64)(8^(m+1)+2), m>=1.
    # Valid by |w|-sum=41/64 and Hurwitz zeta(s,a)<=8^s+zeta(s)<=8^s+2.
    upper=(41/64)*(8*(8*x)**(terms+1)/(1-8*x)+2*x**(terms+1)/(1-x))
    return out, upper


def transition_counts(digits: str):
    """Genuine *linear* 16x16 adjacent pair counts, not cyclic wrapping."""
    if not isinstance(digits,str) or len(digits)<2:
        raise ValueError(">=2 hexadecimal digits required")
    vals=[int(d,16) for d in digits]
    M=[[0]*16 for _ in range(16)]
    for a,b in zip(vals,vals[1:]):M[a][b]+=1
    return tuple(tuple(row) for row in M)


def row_normalized(counts):
    """P(a,b)=count(a,b)/sum_b count(a,b), fail closed on unseen row."""
    if len(counts)!=16 or any(len(row)!=16 for row in counts):
        raise ValueError("16x16 counts required")
    if any(sum(row)<=0 for row in counts):
        raise ValueError("all rows must be observed")
    return tuple(tuple(v/sum(row) for v in row) for row in counts)


def blocking_kernel(block_length: int, u: Fraction) -> Fraction:
    """Exact K_g(u)=sum_{j=0}^{g-1}16^(g-1-j)u^(8j)."""
    if type(block_length) is not int or block_length < 1:
        raise ValueError("block_length>=1 required")
    if not isinstance(u,Fraction) or not 0<=u<=1:
        raise ValueError("exact Fraction u in [0,1] required")
    return sum((16**(block_length-1-j)*u**(8*j)
                for j in range(block_length)), Fraction(0))


def matched_leading_mutation_shift(dps: int = 60):
    """Exact change in gamma_BBP from an authentic-pole same-leading mutation.

    Mutate c by (1,-2,-1,2)/10. The first two pole moments vanish,
    so a=15/64 and its gamma normalization stay unchanged. This shift is
    a source-specific finite part, NOT a normality certificate.
    """
    import mpmath as mp
    with mp.workdps(dps):
        s=mp.sqrt(2)
        return +(mp.mpf(3)/160*mp.log(2)
                 +s/64*mp.log(1+s)+s*mp.pi/128)
