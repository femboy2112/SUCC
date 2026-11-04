"""RIGOROUS FINITE Gamma-Haar certificates using only exact rational arithmetic.

No preloaded pi digits; no floating trigonometry in any verdict.
Finite successes do NOT establish an all-horizon Weyl theorem.
"""
import importlib.util
from fractions import Fraction
from pathlib import Path
from math import factorial

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('succak_gamma_haar_exact', HERE/'gamma_haar.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

GRID = 10**12
TERMS_ATAN = 18
TERMS_TRIG = 19


def atan_inv_interval(q, terms=TERMS_ATAN):
    """Alternating rational arctan(1/q) lower/upper limits."""
    assert q > 1 and terms > 0
    s = sum((Fraction((-1)**k, (2*k+1)*q**(2*k+1))
             for k in range(terms)), Fraction())
    nxt = Fraction((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return s+min(0, nxt), s+max(0, nxt)


def pi_interval():
    """Machin pi=16 atan(1/5)-4 atan(1/239), with rigorous rational enclosure."""
    a, b = atan_inv_interval(5)
    c, d = atan_inv_interval(239)
    return 16*a-4*d, 16*b-4*c


def rational_trig_approx(phase):
    """Return (re,im,complex-absolute-error-upper) for exp(2*pi*i*phase).

    All returned quantities are Fractions. The last entry bounds the
    absolute COMPLEX error, not a floating decimal estimate.
    """
    x = phase % 1
    if x > Fraction(1, 2):
        x -= 1
    pi_lo, pi_hi = pi_interval()
    if not (Fraction(3) < pi_lo <= pi_hi < Fraction(22, 7)):
        raise ArithmeticError("invalid pi interval")
    pi_g = Fraction(round(((pi_lo+pi_hi)/2)*GRID), GRID)
    x_g = Fraction(round(x*GRID), GRID)
    pi_err = max(abs(pi_lo-pi_g), abs(pi_hi-pi_g))
    x_err = Fraction(1, 2*GRID)
    theta = 2*pi_g*x_g
    theta_err = pi_err + 2*Fraction(22, 7)*x_err
    bound = Fraction(22, 7)
    if abs(theta) > bound:
        raise ArithmeticError("centered angle exceeds analytic bound")

    y = theta*theta
    ct = Fraction(1)
    st = theta
    re = ct
    im = st
    for k in range(1, TERMS_TRIG):
        ct = -ct*y / ((2*k-1)*(2*k))
        st = -st*y / ((2*k)*(2*k+1))
        re += ct
        im += st

    cos_rem = bound**(2*TERMS_TRIG-1)/factorial(2*TERMS_TRIG-1)
    sin_rem = bound**(2*TERMS_TRIG)/factorial(2*TERMS_TRIG)
    return re, im, theta_err+cos_rem+sin_rem


def phase_packet(h, M):
    """Rational complex packet and full honest error to e(h 16^n pi/16)."""
    alpha = g.bbp_alpha_partial(M)
    z = []
    maxeps = Fraction()
    for n in range(1, M+1):
        phase = (h*16**n*alpha) % 1
        re, im, eps = rational_trig_approx(phase)
        z.append((re, im))
        maxeps = max(maxeps, eps)
    gamma_err = g.gamma_tail_l1_fourier_error_upper(h, M)*Fraction(22, 7)
    return z, gamma_err + M*maxeps


def sq(z):
    return z[0]**2 + z[1]**2


def sumvec(v):
    return (sum((z[0] for z in v), Fraction()),
            sum((z[1] for z in v), Fraction()))


def level_packet(z, L):
    """Exact rational Haar energy for the computed rational complex packet."""
    M = len(z)
    if 2*L > M or M % (2*L):
        raise ValueError("2L must divide M")
    E = W = P = Fraction()
    for i in range(0, M, 2*L):
        a = sumvec(z[i:i+L])
        b = sumvec(z[i+L:i+2*L])
        E += sq(a) + sq(b)
        W += sq((a[0]-b[0], a[1]-b[1]))
        P += sq((a[0]+b[0], a[1]+b[1]))
    assert P == 2*E-W
    return E, W, P


def check_gamma_haar(h, M, delta=Fraction(1, 100), lowest=16):
    """Each Boolean verdict uses an exact rational strict inequality."""
    z, eps = phase_packet(h, M)
    levels = []
    L = lowest
    while 2*L <= M:
        E, W, _ = level_packet(z, L)
        Eerr = 2*L*eps+eps*eps
        Werr = 4*L*eps+eps*eps
        margin = W-Werr-delta*(E+Eerr)
        levels.append({
            "L": L,
            "pass": margin > 0,
            "ratio_approx": float(W/E) if E else None,
            "cert_margin_lower_approx": float(margin),
            "eps_upper_approx": float(eps)
        })
        L *= 2
    return {"h": h, "M": M, "delta": str(delta),
            "gamma_and_taylor_l1_bound_approx": float(eps),
            "pass_all": all(t["pass"] for t in levels), "levels": levels}


if __name__ == "__main__":
    import json
    cases = ((64,1),(128,2),(128,9),(128,11),
             (256,1),(256,3),(256,5),(256,7))
    print(json.dumps([check_gamma_haar(h,M) for M,h in cases], indent=2))
