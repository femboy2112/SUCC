"""Completed-theta dual channels, positive Pascal/Laguerre extrusion and signed Li gate.

Research instrument only. The source is the ORIGINAL completed Riemann xi,
with Jacobi theta, Gamma(s/2), the zeta pole and reflection s<->1-s.
No zero locations are used as construction inputs; RH remains open.

The mpmath evaluations are FINITE NUMERICAL CALIBRATIONS, not interval proofs.
Theorem proofs and positive coefficients follow from algebra/integral bounds.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def _grade(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("grade must be a positive integer")
    return n


def _degree(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("degree must be a nonnegative integer")
    return n


def pascal_laguerre_weights(n: int) -> tuple[Fraction, ...]:
    """Exact coefficients binom(n,j+1)/j!, 0<=j<n, for L^(1)_(n-1)."""
    n = _grade(n)
    return tuple(Fraction(comb(n, j+1), factorial(j)) for j in range(n))


def laguerre_signed_value(n: int, t: Fraction | int, sign: int) -> Fraction:
    """Evaluate L^(1)_(n-1)(+t) for sign=+1, or L(-t) for sign=-1."""
    if sign not in (-1, 1) or type(sign) is not int:
        raise ValueError("Laguerre sign must be +1 or -1")
    if not isinstance(t, (int, Fraction)) or type(t) is bool:
        raise ValueError("exact rational parameter required")
    q = Fraction(t)
    return sum((w * (-sign*q)**j for j,w in enumerate(pascal_laguerre_weights(n))), Fraction(0))


def triangle_moments_from_a(a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Inverse binomial transform of b_n=a_n/n; return c_0,..,c_(N-1).

    Input is a_1..a_N (not an arbitrary Xi claim). The inverse is
    c_k = sum_(i=0)^k (-1)^(k-i) C(k,i)*a_(i+1)/(i+1).
    """
    if not isinstance(a, tuple) or not a:
        raise ValueError("nonempty tuple of exact coefficients required")
    if not all(isinstance(v, (int, Fraction)) and type(v) is not bool for v in a):
        raise ValueError("coefficients must be exact ints/Fractions")
    b = [Fraction(v, i+1) for i,v in enumerate(a)]
    return tuple(sum(((-1)**(k-i)*comb(k,i)*b[i] for i in range(k+1)),Fraction(0))
                 for k in range(len(a)))


def a_from_triangle_moments(c: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Exact Pascal extrusion: a_n=n*sum_j C(n-1,j)c_j."""
    if not isinstance(c, tuple) or not c:
        raise ValueError("nonempty exact moment tuple required")
    if not all(isinstance(x, (int, Fraction)) and type(x) is not bool for x in c):
        raise ValueError("moment tuple must be exact int/Fraction")
    return tuple(n*sum((comb(n-1,j)*Fraction(c[j]) for j in range(n)),Fraction(0))
                 for n in range(1,len(c)+1))


def li_from_completed_coefficients(a: tuple) -> tuple:
    """Signed formal recurrence: lambda_n=n a_n-sum_{j=1}^{n-1}lambda_j*a_(n-j).

    a is (a_1,...,a_N), not a constant term. Operates with Fractions or
    mpmath numbers, but never inserts zero locations or assumes positivity.
    """
    if not isinstance(a, tuple) or not a:
        raise ValueError("nonempty coefficient tuple required")
    li = []
    for n in range(1,len(a)+1):
        li.append(n*a[n-1]-sum((li[j-1]*a[n-j-1] for j in range(1,n)),0))
    return tuple(li)


def fake_atomic_triangle_coefficients(n: int, *, amplitude: float = 2., t: float = 1.) -> float:
    """Changed-source positive atom a=k*delta_t, NOT the Riemann theta source."""
    import math
    n=_grade(n)
    if amplitude <= 0 or t <= 0:
        raise ValueError("positive fake amplitude and time required")
    return amplitude*sum(float(w)*t**j*(math.exp(t)+(-1)**j)
                         for j,w in enumerate(pascal_laguerre_weights(n)))


def fake_atomic_completed(s, *, amplitude: float = 2., t: float = 1.):
    """Reflection-symmetric entire synthetic source 1+A s(s-1)(e^(st)+e^((1-s)t))."""
    import mpmath as mp
    if amplitude <= 0 or t <= 0:
        raise ValueError("positive fake amplitude and time required")
    return 1+amplitude*s*(s-1)*(mp.exp(s*t)+mp.exp((1-s)*t))


def _mp():
    import mpmath as mp
    return mp


def theta_kernel(t, *, source_terms: int = 8):
    """k(t)=theta(exp(2t))-1, truncated at original integer n<=source_terms."""
    mp = _mp()
    if type(source_terms) is not int or source_terms < 1 or t < 0:
        raise ValueError("positive source cutoff and t>=0 required")
    e2 = mp.exp(2*t)
    return 2*mp.fsum(mp.exp(-mp.pi*m*m*e2) for m in range(1,source_terms+1))


def theta_phi(t, *, source_terms: int = 8):
    """Positive completed Xi Fourier kernel from theta modular contact removal."""
    mp = _mp()
    if t < 0 or type(source_terms) is not int or source_terms < 1:
        raise ValueError("positive source cutoff and t>=0 required")
    e2=mp.exp(2*t)
    return 4*mp.exp(t/2)*mp.fsum(
        mp.exp(-a)*(2*a*a-3*a) for a in
        (mp.pi*m*m*e2 for m in range(1,source_terms+1)))


def theta_I(s, *, source_terms: int = 8):
    """I(s)=sum_{m>=1}(pi m^2)^(-s/2)*Gamma(s/2,pi m^2).

    Finite integer cutoff only; theta tail has explicit analytic bound.
    """
    mp=_mp()
    if type(source_terms) is not int or source_terms < 1:
        raise ValueError("positive integer source cutoff required")
    return mp.fsum(mp.gammainc(s/2, mp.pi*m*m, mp.inf)/
                   (mp.pi*m*m)**(s/2) for m in range(1,source_terms+1))


def xi_theta_dual(s, *, source_terms: int = 8):
    """Exactly completed two theta channels, numerically truncated in m."""
    return _mp().mpf('0.5')+s*(s-1)/2*(theta_I(s,source_terms=source_terms)+
                                     theta_I(1-s,source_terms=source_terms))


def theta_reflected_channels(u, *, source_terms: int = 8):
    """E(u),E#(u) with s=1/2+i*u; E+E# = Xi, exact at full source."""
    mp=_mp()
    s=mp.mpf('0.5')+mp.j*u
    factor=s*(s-1)/2
    return (mp.mpf('0.25')+factor*theta_I(s,source_terms=source_terms),
            mp.mpf('0.25')+factor*theta_I(1-s,source_terms=source_terms))


def completed_xi_direct(s):
    """Independent full Gamma/zeta evaluation except removable s=0,1."""
    mp=_mp()
    if s in (0,1):
        return mp.mpf('0.5')
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2


def laguerre_theta_coefficient(n: int, *, source_terms: int = 8,
                               time_cutoff: str = '2.7'):
    """Numerical calibration of the exact positive integral for a_n.

    This is NOT rigorous quadrature; use tail functions for SOURCE truncation.
    """
    mp=_mp()
    weights=pascal_laguerre_weights(n)
    T=mp.mpf(time_cutoff)
    partitions=[mp.mpf('0'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('1.5'),mp.mpf('2'),T]
    partitions=sorted(set(x for x in partitions if x<=T))
    def integrand(t):
        return theta_kernel(t,source_terms=source_terms)*mp.fsum(
            mp.mpf(w.numerator)/w.denominator*t**j*(mp.exp(t)+(-1)**j)
            for j,w in enumerate(weights))
    return mp.quad(integrand,partitions)


def first_li_gamma():
    """Exact expression in Euler's constant and completed Gamma half-density."""
    mp=_mp()
    return 1+mp.euler/2-mp.log(4*mp.pi)/2


def rigorous_integer_tail_bound(n: int, *, source_terms: int = 8):
    """PROVED absolute upper bound on the omitted n>source_terms theta sources.

    Does not include quadrature/time-cutoff error. Uses m² spacing and
    exp(2t)>=1+2t for t>=0. Valid for every fixed finite Laguerre n.
    """
    mp=_mp()
    n=_grade(n)
    if type(source_terms) is not int or source_terms < 1:
        raise ValueError("positive integer cutoff required")
    M=source_terms
    alpha=2*mp.pi*(M+1)**2
    pref=2*mp.exp(-mp.pi*(M+1)**2)/(1-mp.exp(-mp.pi*(2*M+3)))
    return pref*mp.fsum(mp.binomial(n,j+1)*(
        1/(alpha-1)**(j+1)+1/alpha**(j+1)) for j in range(n))


def rigorous_time_tail_bound(n: int, *, time_cutoff: str = '2.7'):
    """PROVED upper bound on time-integral t>=T for FULL theta source.

    Used together with rigorous_integer_tail_bound; quadrature in [0,T]
    still needs a separate validated enclosure before numerical certificates.
    """
    mp=_mp();n=_grade(n);T=mp.mpf(time_cutoff)
    if T<0:
        raise ValueError("T must be nonnegative")
    alpha=2*mp.pi*mp.exp(2*T)
    if alpha<=1:
        raise ValueError("time cutoff requires alpha>1")
    pref=2*mp.exp(-mp.pi*mp.exp(2*T))/(1-mp.exp(-3*mp.pi*mp.exp(2*T)))
    out=mp.mpf('0')
    for j in range(n):
        inner=mp.fsum(mp.binomial(j,q)*T**(j-q)*mp.factorial(q)*(
            mp.exp(T)/(alpha-1)**(q+1)+1/alpha**(q+1)) for q in range(j+1))
        out+=mp.binomial(n,j+1)*inner/mp.factorial(j)
    return pref*out


def completed_phi_halves(u, *, source_terms: int = 8, time_cutoff: str = '2.7'):
    """Numerical half-Fourier decomposition of Xi; no HB claim or certification."""
    mp=_mp()
    T=mp.mpf(time_cutoff)
    cuts=sorted(set(x for x in [mp.mpf('0'),mp.mpf('.3'),mp.mpf('.6'),mp.mpf('1'),mp.mpf('1.6'),T] if x<=T))
    neg=mp.quad(lambda t:theta_phi(t,source_terms=source_terms)*mp.exp(-mp.j*u*t),cuts)
    pos=mp.quad(lambda t:theta_phi(t,source_terms=source_terms)*mp.exp(mp.j*u*t),cuts)
    return neg,pos


def theta_moment_upper_bound(j: int):
    """PROVED elementary bound on M_j=int k*t^j*(e^t+(-1)^j)dt.

    Uses theta tail m^2>=1+3(m-1), exp(2t)>=1+2t. Never a
    proof of ALL-degree Li positivity; bounds grow with j factorially.
    """
    mp=_mp();j=_degree(j)
    alpha=2*mp.pi
    return (2*mp.exp(-mp.pi)/(1-mp.exp(-3*mp.pi)))*mp.factorial(j)*(
        1/(alpha-1)**(j+1)+1/alpha**(j+1))


def first_four_li_from_moments(moments: tuple) -> tuple:
    """Exact low-degree source-moment → completed Li triangular contraction.

    moments=(M0,M1,M2,M3) where Mj=int k(t)t^j(e^t+(-1)^j)dt.
    Works over rational, real, or multiprecision scalar rings.
    """
    if not isinstance(moments,tuple) or len(moments)!=4:
        raise ValueError('need precisely four source moments')
    m0,m1,m2,m3=moments
    a=(m0,2*m0+m1,3*m0+3*m1+m2/2,4*m0+6*m1+2*m2+m3/6)
    return li_from_completed_coefficients(a)


def signed_log_clock_kernel(t, v, x, y):
    """Exact symmetrized two-time Mellin current kernel (excluding Phi factors).

    P(x+iy)=(1/4)*integral Phi(t)Phi(v)*[ (t-v)sinh(y(t-v))cos(x(t+v))
              +(t+v)sinh(y(t+v))cos(x(t-v)) ] dt dv.
    The integrand is >=0 at x=0 and y>0, not for arbitrary x.
    """
    mp=_mp()
    if t<0 or v<0 or y<=0:
        raise ValueError('require nonnegative theta times and y>0')
    return ((t-v)*mp.sinh(y*(t-v))*mp.cos(x*(t+v))+
            (t+v)*mp.sinh(y*(t+v))*mp.cos(x*(t-v)))/4


def finite_log_clock_current(atoms: tuple, u):
    """Finite exact-structure oracle for the positive-Phi derivative current.

    atoms=((t0,weight0), ...), with all t>=0, weight>0.
    This is a finite proxy, not the original theta source.
    """
    mp=_mp()
    if not isinstance(atoms,tuple) or not atoms:
        raise ValueError('nonempty atomic measure tuple required')
    if any(t<0 or w<=0 for t,w in atoms):
        raise ValueError('nonnegative times, strictly positive weights required')
    xi=mp.fsum(w*mp.cos(u*t) for t,w in atoms)
    derivative=-mp.fsum(w*t*mp.sin(u*t) for t,w in atoms)
    p=-mp.im(derivative*mp.conj(xi))
    q=mp.fsum(w*v*signed_log_clock_kernel(t,r,mp.re(u),mp.im(u))
              for t,w in atoms for r,v in atoms)
    return p,q


def completed_xi_log_clock_current(u):
    """Independent full-Gamma/Zeta Xi derivative current; numerical only.

    P(u)=-Im(Xi'(u)*conj(Xi(u))). Strict P>0 for all Im u>0
    is RH-equivalent, NOT established by this evaluator.
    """
    mp=_mp()
    f=lambda v:completed_xi_direct(mp.mpf('0.5')+mp.j*v)
    return -mp.im(mp.diff(f,u)*mp.conj(f(u)))


def composite_six_mutation_delta(s, *, strength=1):
    """Changed-source xi delta from mutating the integer Gaussian m=6 only.

    Delta k(t)=2*strength*exp(-36*pi*exp(2t)). The entire correction
    is source-authenticated as a MUTATION, never the original zeta.
    """
    mp=_mp()
    a=36*mp.pi
    delta_I=lambda v:strength*mp.gammainc(v/2,a,mp.inf)/a**(v/2)
    return s*(s-1)/2*(delta_I(s)+delta_I(1-s))


def wrong_gamma_completed(s):
    """Deliberately incorrect Archimedean Gamma(s/2+1/2) comparator."""
    mp=_mp()
    if s in (0,1):
        raise ValueError('wrong-Gamma comparator not evaluated at removable endpoints')
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma((s+1)/2)*mp.zeta(s)/2
