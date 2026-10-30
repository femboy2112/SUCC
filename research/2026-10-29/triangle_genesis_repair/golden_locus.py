"""Golden fixed-point locus of the operational-triangle endpoint PGF (Operation Main XVI).

Research-only. Not a pi digit sampler and not a proof of normality or RH. Python >= 3.10.

The declared offspring/endpoint generating function of the Gamma--Poisson emergence class
(THEOREMS.md TG-04) is

    G_{r,theta}(z) = [1 + theta (1 - z)]^{-r},   r > 0, theta > 0, z in [0, 1].

G is increasing and convex on [0, 1] with G(1) = 1, G(0) = (1+theta)^{-r} in (0, 1), and mean
G'(1) = r*theta. When r*theta > 1 (supercritical) it has a unique interior fixed point
q_{r,theta} in (0, 1) -- the least fixed point / Galton--Watson extinction root -- and otherwise
the only fixed point in [0, 1] is 1.

This module computes q_{r,theta} by the operational route (monotone fixed-point iteration from 0)
and proves/checks, against the fixed-golden mark lambda^r (lambda = phi^{-1} = (sqrt5-1)/2), the

    GOLDEN LOCUS:   q_{r,theta} = lambda^r   <=>   theta = lambda / (1 - lambda^r),   r > 0.

The independent symbolic/Newton route lives in independent_oracle_xvi.py.
"""
from __future__ import annotations
import mpmath as mp
import sympy as sp

# --- exact golden constants (sympy) ---
LAMBDA_SYM = (sp.sqrt(5) - 1) / 2          # lambda = phi^{-1}
PHI_SYM = (sp.sqrt(5) + 1) / 2             # phi


def _lam(ctx=mp):
    return (ctx.sqrt(5) - 1) / 2


def theta_locus_sym(r):
    """Exact locus clock theta(r) = lambda/(1-lambda^r) as a sympy expression."""
    r = sp.sympify(r)
    return LAMBDA_SYM / (1 - LAMBDA_SYM**r)


def theta_locus(r, dps: int = 50):
    """Numeric locus clock theta(r) = lambda/(1-lambda^r)."""
    with mp.workdps(dps):
        lam = _lam()
        return +(lam / (1 - lam ** mp.mpf(r)))


def pgf(r, theta, z, dps: int = 50):
    """Endpoint PGF G_{r,theta}(z) = [1+theta(1-z)]^{-r}."""
    with mp.workdps(dps):
        return +((1 + mp.mpf(theta) * (1 - mp.mpf(z))) ** (-mp.mpf(r)))


def mean(r, theta):
    """Offspring mean G'(1) = r*theta (supercritical iff > 1)."""
    return mp.mpf(r) * mp.mpf(theta)


def least_fixed_point(r, theta, dps: int = 50, iters: int = 4000):
    """Operational route: monotone fixed-point iteration q_{k+1}=G(q_k) from q_0=0.

    For a convex increasing G with G(1)=1 this converges upward to the least fixed point.
    """
    with mp.workdps(dps + 10):
        r_, th = mp.mpf(r), mp.mpf(theta)
        q = mp.mpf(0)
        for _ in range(iters):
            q_new = (1 + th * (1 - q)) ** (-r_)
            if abs(q_new - q) < mp.mpf(10) ** (-(dps + 5)):
                q = q_new
                break
            q = q_new
        return +q


def golden_point(r, dps: int = 50):
    """The fixed-golden mark lambda^r."""
    with mp.workdps(dps):
        return +(_lam() ** mp.mpf(r))


def on_locus(r, dps: int = 50):
    """(theta, q_iter, lambda^r) at the locus clock -- q_iter should equal lambda^r."""
    th = theta_locus(r, dps)
    return th, least_fixed_point(r, th, dps), golden_point(r, dps)


def laplace_rate_on_locus(r, dps: int = 50):
    """theta*(1-q) along the locus -- the constant invariant (= lambda for every r)."""
    with mp.workdps(dps):
        th = theta_locus(r, dps)
        q = golden_point(r, dps)
        return +(th * (1 - q))


def is_supercritical_on_locus(r, dps: int = 50) -> bool:
    """r*theta(r) > 1 on the locus (proved for all r>0; checked numerically here)."""
    return mean(r, theta_locus(r, dps)) > 1


def gamma_laplace(r, rate, dps: int = 50):
    """E e^{-rate * Y}, Y ~ Gamma(r,1), = (1+rate)^{-r}."""
    with mp.workdps(dps):
        return +((1 + mp.mpf(rate)) ** (-mp.mpf(r)))


# --- exact symbolic certificate of the locus and of the (2,1) specialization ---

def locus_symbolic_certificate():
    """Return (is_fixed_point, factor_at_(2,1)) proving the locus and the golden factorisation.

    is_fixed_point: sympy 0 iff G_{r, theta(r)}(lambda^r) - lambda^r simplifies to 0 identically.
    factor_at_(2,1): the factorisation of q(2-q)^2 - 1 exhibiting q=phi^{-2} as the interior root.
    """
    r, z, q = sp.symbols('r z q', positive=True)
    th = theta_locus_sym(r)
    G = (1 + th * (1 - z)) ** (-r)
    is_fp = sp.simplify(G.subs(z, LAMBDA_SYM**r) - LAMBDA_SYM**r)
    # at (r,theta)=(2,1): fixed-point equation q = (2-q)^{-2}  <=>  q(2-q)^2 - 1 = 0
    factored = sp.factor(q * (2 - q) ** 2 - 1)
    return is_fp, factored


if __name__ == '__main__':
    mp.mp.dps = 50
    print('golden locus q_{r,theta}=lambda^r  <=>  theta=lambda/(1-lambda^r)\n')
    print(f"{'r':>6} {'theta(r)':>22} {'q_iter':>22} {'lambda^r':>22} {'|diff|':>10} {'r*theta':>10} {'theta(1-q)':>14}")
    for r in (0.5, 1, 2, 3, 4, 5, 10):
        th, qi, gp = on_locus(r)
        inv = laplace_rate_on_locus(r)
        print(f"{r:>6} {mp.nstr(th,16):>22} {mp.nstr(qi,16):>22} {mp.nstr(gp,16):>22} "
              f"{mp.nstr(abs(qi-gp),3):>10} {mp.nstr(mean(r,th),8):>10} {mp.nstr(inv,12):>14}")
    is_fp, factored = locus_symbolic_certificate()
    print('\nsymbolic G(lambda^r)-lambda^r on locus =', is_fp, ' (0 == identity holds)')
    print('q(2-q)^2 - 1 factors as', factored, ' => interior root q=phi^{-2}')
