"""Authentic theta/Gamma dual completion and signed Pascal/Li observer.

Research-only. This is a compact repo-facing implementation of the locally
tested 26-probe source package; it does NOT certify RH. No nontrivial
zeta zeros are fed to any constructor. Fake controls are explicit.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial


def laguerre_pascal(n: int) -> tuple[Fraction, ...]:
    """L_(n-1)^(1)(x) = sum_j row[j]*(-x)^j."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer grade required")
    return tuple(Fraction(comb(n, j + 1), factorial(j)) for j in range(n))


def inverse_pascal(a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Recover c_j=M_j/(j+1)! from a_n=[z^n]2xi(1/(1-z))."""
    if not isinstance(a, tuple) or not a:
        raise ValueError("nonempty coefficient tuple required")
    if not all(isinstance(x, (int, Fraction)) and type(x) is not bool for x in a):
        raise ValueError("exact coefficients required")
    b = [Fraction(v, i + 1) for i, v in enumerate(a)]
    return tuple(sum(((-1)**(k-i)*comb(k, i)*b[i]
                      for i in range(k+1)), Fraction(0)) for k in range(len(a)))


def pascal_extrude(c: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    if not isinstance(c, tuple) or not c:
        raise ValueError("nonempty moment tuple required")
    if not all(isinstance(x, (int, Fraction)) and type(x) is not bool for x in c):
        raise ValueError("exact rational moments required")
    return tuple(n*sum((comb(n-1, j)*Fraction(c[j]) for j in range(n)),
                       Fraction(0)) for n in range(1, len(c)+1))


def signed_li(a: tuple):
    """Exact formal-log recurrence. Positivity of a does not force Li signs."""
    if not isinstance(a, tuple) or not a:
        raise ValueError("nonempty coefficient tuple required")
    out = []
    for n in range(1, len(a)+1):
        out.append(n*a[n-1]-sum(out[j-1]*a[n-j-1] for j in range(1, n)))
    return tuple(out)


def _mp():
    import mpmath as mp
    return mp


def theta_k(t, cutoff: int = 8):
    mp = _mp()
    if t < 0 or type(cutoff) is not int or cutoff < 1:
        raise ValueError("t>=0 and positive integer source cutoff")
    q = mp.exp(2*t)
    return 2*mp.fsum(mp.exp(-mp.pi*j*j*q) for j in range(1, cutoff+1))


def I_theta(s, cutoff: int = 8):
    """Entire I(s): upper-incomplete-Gamma source, integer modes 1..cutoff."""
    mp = _mp()
    if type(cutoff) is not int or cutoff < 1:
        raise ValueError("positive integer source cutoff")
    return mp.fsum(mp.gammainc(s/2, mp.pi*j*j, mp.inf)/
                   (mp.pi*j*j)**(s/2) for j in range(1, cutoff+1))


def xi_theta(s, cutoff: int = 8):
    """Numerical theta split, source truncated; full original completion."""
    mp = _mp()
    return mp.mpf("0.5")+s*(s-1)*(I_theta(s, cutoff)+I_theta(1-s, cutoff))/2


def xi_original(s):
    """Independent completed Gamma+zeta reference (not a zero constructor)."""
    mp = _mp()
    if s == 0 or s == 1:
        return mp.mpf("0.5")
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2


def theta_triangle_a(n: int, cutoff: int = 8):
    """Finite numerical theta-Laguerre coefficient a_n; not interval certified."""
    mp = _mp()
    row = laguerre_pascal(n)
    def integrand(t):
        s = mp.fsum(mp.mpf(w.numerator)/w.denominator*t**j*
                    (mp.exp(t)+(-1)**j) for j, w in enumerate(row))
        return theta_k(t, cutoff)*s
    return mp.quad(integrand, [0, .5, 1, 1.5, 2, mp.mpf("2.7")])


def gamma_first_vertex():
    mp = _mp()
    return 1+mp.euler/2-mp.log(4*mp.pi)/2


def fake_atom(s):
    """Changed positive source 2 delta_1, off-critical real zero witness."""
    mp = _mp()
    return 1+2*s*(s-1)*(mp.exp(s)+mp.exp(1-s))


def phi_theta(t, cutoff: int = 8):
    """Original completed Xi kernel: 4e^(t/2) sum e^-a(2a^2-3a)>0."""
    mp = _mp()
    if t < 0:
        raise ValueError("t must be nonnegative")
    q = mp.exp(2*t)
    return 4*mp.exp(t/2)*mp.fsum(
        mp.exp(-a)*(2*a*a-3*a) for a in
        (mp.pi*j*j*q for j in range(1, cutoff+1)))


def dual_theta_halves(u, cutoff: int = 8):
    mp = _mp()
    s = mp.mpf("0.5")+mp.j*u
    return (mp.mpf("0.25")+s*(s-1)*I_theta(s, cutoff)/2,
            mp.mpf("0.25")+s*(s-1)*I_theta(1-s, cutoff)/2)


def signed_log_clock_kernel(t, v, x, y):
    """Double Mellin kernel for -Im(Xi'(x+iy)*conj(Xi(x+iy)))."""
    mp = _mp()
    if t < 0 or v < 0 or y <= 0:
        raise ValueError("nonnegative times, positive imaginary height")
    return ((t-v)*mp.sinh(y*(t-v))*mp.cos(x*(t+v))+
            (t+v)*mp.sinh(y*(t+v))*mp.cos(x*(t-v)))/4


def finite_source_log_current(atoms: tuple, u):
    """Finite-source check: direct phase derivative versus two-time kernel."""
    mp = _mp()
    if not isinstance(atoms, tuple) or not atoms:
        raise ValueError("nonempty positive atomic source")
    if any(t < 0 or mass <= 0 for t, mass in atoms):
        raise ValueError("nonnegative times, positive masses")
    a = mp.fsum(mass*mp.cos(u*t) for t, mass in atoms)
    d = -mp.fsum(mass*t*mp.sin(u*t) for t, mass in atoms)
    direct = -mp.im(d*mp.conj(a))
    double = mp.fsum(m*n*signed_log_clock_kernel(t, v, mp.re(u), mp.im(u))
                     for t, m in atoms for v, n in atoms)
    return direct, double


def xi_derivative_current(u):
    """RH-equivalent global sign target, evaluated at a *single* finite u."""
    mp = _mp()
    f = lambda z: xi_original(mp.mpf("0.5")+mp.j*z)
    return -mp.im(mp.diff(f, u)*mp.conj(f(u)))
