"""Exact ADDITIVE circle-method interface for the Goldbach-weighted representation
R_Lambda(N) = sum_{a+b=N} Lambda(a)Lambda(b)  (Operation Rigidity Forge, Part VII,
section 7).

Everything here is EXACT (sympy-symbolic for Lambda = log p, Fraction-exact for
the singular series).  It is the additive circle-method skeleton:

  GC-01  (CLASSICAL; PROVED LOCAL, exact finite identity).  With e(x)=e^{2 pi i x}
      and the ADDITIVE Fourier carrier  F_N(theta) = sum_{n=1}^{N-1} Lambda(n) e(n theta),
          R_Lambda(N) = integral_0^1 F_N(theta)^2 e(-N theta) dtheta
                      = [z^N] F_N(z)^2                               (polynomial route)
                      = (1/Q) sum_{j=0}^{Q-1} F_N(w^j)^2 w^{-Nj},  w=e(1/Q), Q>=N.
      This is F^2, NOT |F|^2.  The |F|^2 ("positive-definite autocorrelation")
      object extracts the DIFFERENCE diagonal sum_{a-b=N} Lambda(a)Lambda(b),
      which is identically 0 on the window 1<=a,b<=N-1 -- so no positive-definite
      |F|^2 route reaches the SUM problem (the BS-G1 firewall, here made exact and
      cross-checked against the direct additive convolution).

  GC-02  (singular series: CLASSICAL object + CONJECTURED asymptotic).  The
      Hardy-Littlewood singular series
          S(N) = prod_p  S_p(N),   S_p(N) = 1 + 1/(p-1)   if p | N,
                                            1 - 1/(p-1)^2  if p does not divide N,
      is a convergent Euler product (S(N) = 0 for N odd, from the p = 2 factor
      1 - 1/(2-1)^2 = 0).  We compute S(N) as a CERTIFIED rational two-sided
      enclosure.  The major-arc contribution to R_Lambda(N) is S(N)*N*(1+o(1))
      (CLASSICAL, via Siegel-Walfisz prime equidistribution in APs).  The claim
      that the FULL R_Lambda(N) is asymptotic to S(N)*N is the binary-Goldbach-
      type statement: the minor-arc smallness is OPEN for the binary problem
      (ternary is Vinogradov's theorem).  We expose the major/minor-arc Farey
      structure and compare R_Lambda(N)/N to S(N) as EVIDENCE only.

Binary Goldbach is OPEN.  This module makes NO Goldbach claim: it recovers
classical exact identities and the classical singular-series object, and keeps
the open asymptotic clearly labelled CONJECTURED.

FIREWALL (AGENTS.md).  R_Lambda is the ADDITIVE convolution (Lambda *+ Lambda);
its generating object is F_N^2 (additive Fourier), never |F_N|^2 and never the
MULTIPLICATIVE (-zeta'/zeta)^2.  See arithmetic_interactions.illegal_interchange_witness
(returns N = 5) for the executable receipt of that distinction.

RH PROVED: NO.  No zeta-zero ordinate is used anywhere.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Tuple

import sympy as sp

from .abc_clock_families import prime, prime_factors
from .arithmetic_interactions import (
    goldbach_representation_R_Lambda,
    is_prime_power,
    von_mangoldt,
)


class GoldbachCircleError(ValueError):
    pass


# --------------------------------------------------------------------------
# GC-01 : exact finite additive Fourier identity (three agreeing routes).
# --------------------------------------------------------------------------
def fourier_generating_poly(M: int, z=None):
    """F_M(z) = sum_{n=1}^{M} Lambda(n) z^n as an exact sympy expression in z."""
    if type(M) is not int or M < 1:
        raise GoldbachCircleError("fourier_generating_poly needs integer M >= 1")
    if z is None:
        z = sp.symbols("z")
    return sum((von_mangoldt(n) * z ** n for n in range(1, M + 1)), sp.Integer(0)), z


def R_Lambda_from_fourier_poly(N: int):
    """R_Lambda(N) = [z^N] F_{N-1}(z)^2, the exact additive Fourier coefficient.

    Extracting the z^N coefficient IS the integral_0^1 (...) e(-N theta) dtheta by
    orthogonality of {e(n theta)}.  Exact (sympy).  Uses the window M = N-1 (the
    largest a with a + b = N, a, b >= 1).
    """
    if type(N) is not int or N < 2:
        raise GoldbachCircleError("R_Lambda_from_fourier_poly needs integer N >= 2")
    expr, z = fourier_generating_poly(N - 1)
    return sp.expand(expr ** 2).coeff(z, N)


def R_Lambda_from_dft(N: int, Q: int = 0):
    """R_Lambda(N) via the exact discrete orthogonality sum over Q-th roots of 1.

        R_Lambda(N) = (1/Q) sum_{j=0}^{Q-1} F_{N-1}(w^j)^2 w^{-Nj},  w = e(1/Q).
    Requires Q >= N so no aliasing of the shift a+b-N (which lies in [2-N, N-2]).
    Exact via sympy roots of unity; use small N (symbolic, slow).
    """
    if type(N) is not int or N < 2:
        raise GoldbachCircleError("R_Lambda_from_dft needs integer N >= 2")
    if Q == 0:
        Q = 2 * N
    if type(Q) is not int or Q < N:
        raise GoldbachCircleError("need Q >= N to avoid additive aliasing")
    w = sp.exp(2 * sp.pi * sp.I / Q)
    lam = [von_mangoldt(n) for n in range(0, N)]
    total = sp.Integer(0)
    for j in range(Q):
        wj = w ** j
        F = sum((lam[n] * wj ** n for n in range(1, N)), sp.Integer(0))
        total += F * F * w ** (-N * j)
    return sp.simplify(sp.expand_complex(total / Q))


def difference_diagonal(N: int):
    """The |F|^2 object's shift-N coefficient:  sum_{a-b=N, 1<=a,b<=N-1} Lambda(a)Lambda(b).

    Identically 0 on the window (a - b <= (N-1) - 1 = N-2 < N).  Returned exactly
    to witness the F^2 vs |F|^2 firewall: the SUM problem needs F^2.
    """
    if type(N) is not int or N < 2:
        raise GoldbachCircleError("difference_diagonal needs integer N >= 2")
    M = N - 1
    return sum((von_mangoldt(a) * von_mangoldt(b)
                for a in range(1, M + 1) for b in range(1, M + 1) if a - b == N),
               sp.Integer(0))


def fourier_identity_check(N: int, with_dft: bool = False) -> Dict[str, object]:
    """Exact GC-01 receipt: all routes agree with the direct additive convolution.

    Returns the direct R_Lambda(N), the polynomial-coefficient value, (optionally)
    the roots-of-unity value, the difference diagonal (must be 0), and booleans.
    """
    direct = goldbach_representation_R_Lambda(N)
    poly = R_Lambda_from_fourier_poly(N)
    out = {
        "N": N,
        "direct": direct,
        "poly_coeff": poly,
        "poly_matches": sp.simplify(sp.sympify(poly) - direct) == 0,
        "difference_diagonal": difference_diagonal(N),
        "difference_is_zero": sp.simplify(difference_diagonal(N)) == 0,
    }
    if with_dft:
        dft = R_Lambda_from_dft(N)
        out["dft"] = dft
        out["dft_matches"] = sp.simplify(dft - direct) == 0
    return out


# --------------------------------------------------------------------------
# Prime support vs higher-prime-power contamination (exact bookkeeping).
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class GoldbachSupportSplit:
    N: int
    prime_pair_mass: object          # sum_{p+q=N, p,q prime} log p log q
    contamination_mass: object       # terms with a=p^k or b=q^l, some exponent >= 2
    total: object                    # == R_Lambda(N)
    n_true_prime_pairs: int          # ordered count of (p, q) prime, p+q=N
    contamination_terms: Tuple[Tuple[int, int], ...]   # (a, b) with a prime-power, exponent>=2

    @property
    def decomposition_exact(self) -> bool:
        return sp.simplify(sp.sympify(self.prime_pair_mass)
                           + sp.sympify(self.contamination_mass)
                           - sp.sympify(self.total)) == 0


def support_split(N: int) -> GoldbachSupportSplit:
    """Exact split of R_Lambda(N) into genuine prime-pair mass and higher-prime-
    power contamination (a or b equal to p^k with k >= 2).

    R_Lambda(N) = sum_{p+q=N} log p log q  +  sum_{mixed/pure prime-power terms}.
    Both pieces exact; their sum equals R_Lambda(N) (``decomposition_exact``).
    """
    if type(N) is not int or N < 4:
        raise GoldbachCircleError("support_split needs integer N >= 4")
    pair_mass = sp.Integer(0)
    contam = sp.Integer(0)
    n_pairs = 0
    contam_terms: List[Tuple[int, int]] = []
    for a in range(2, N - 1):
        b = N - a
        la = von_mangoldt(a)
        lb = von_mangoldt(b)
        if la == 0 or lb == 0:
            continue
        a_prime = prime(a)
        b_prime = prime(b)
        if a_prime and b_prime:
            pair_mass += la * lb
            n_pairs += 1
        else:
            contam += la * lb
            contam_terms.append((a, b))
    return GoldbachSupportSplit(
        N=N, prime_pair_mass=sp.simplify(pair_mass),
        contamination_mass=sp.simplify(contam),
        total=goldbach_representation_R_Lambda(N),
        n_true_prime_pairs=n_pairs, contamination_terms=tuple(contam_terms),
    )


# --------------------------------------------------------------------------
# GC-02 : the Hardy-Littlewood singular series (exact rational enclosure).
# --------------------------------------------------------------------------
def singular_series_local_factor(p: int, N: int) -> Fraction:
    """Exact local factor S_p(N):  1 + 1/(p-1) if p | N, else 1 - 1/(p-1)^2.

    For p = 2 and N odd this is 1 - 1 = 0, which annihilates S(N): the local
    obstruction to representing an odd number as a sum of two (odd) primes.
    """
    if not prime(p):
        raise GoldbachCircleError("p must be an actual prime")
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("N must be a positive integer")
    if N % p == 0:
        return Fraction(1) + Fraction(1, p - 1)
    return Fraction(1) - Fraction(1, (p - 1) ** 2)


def _primes_upto(P: int) -> List[int]:
    if type(P) is not int or P < 2:
        return []
    sieve = bytearray([1]) * (P + 1)
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i <= P:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [i for i in range(2, P + 1) if sieve[i]]


def singular_series_truncated(N: int, P: int) -> Fraction:
    """Exact rational truncated product  prod_{p <= P} S_p(N).

    For the truncation to contain every p | N (the factors > 1) require P to be
    at least the largest prime factor of N; otherwise raises.
    """
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("N must be a positive integer")
    largest_pf = max((p for p, _ in prime_factors(N)), default=1)
    if P < largest_pf:
        raise GoldbachCircleError(
            f"P={P} must be >= largest prime factor {largest_pf} of N to capture all p|N")
    val = Fraction(1)
    for p in _primes_upto(P):
        val *= singular_series_local_factor(p, N)
    return val


def singular_series_enclosure(N: int, P: int) -> Tuple[Fraction, Fraction]:
    """Certified rational [lo, hi] with lo <= S(N) <= hi.

    For N even, the tail prod_{p>P} (1 - 1/(p-1)^2) lies in [1 - 1/(P-1), 1]:
        prod_{p>P}(1 - 1/(p-1)^2) >= 1 - sum_{p>P} 1/(p-1)^2
                                   >= 1 - sum_{n>P} 1/(n-1)^2 >= 1 - 1/(P-1),
    and is <= 1.  Hence S(N) in [S_{<=P}(N)*(1 - 1/(P-1)), S_{<=P}(N)].
    For N odd S(N) = 0 exactly (returned as [0, 0]).
    """
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("N must be a positive integer")
    if N % 2 == 1:
        return Fraction(0), Fraction(0)
    if P < 2:
        raise GoldbachCircleError("P must be >= 2")
    trunc = singular_series_truncated(N, P)
    tail_lo = Fraction(1) - Fraction(1, P - 1)
    return trunc * tail_lo, trunc


def twin_prime_constant_enclosure(P: int) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for 2*C_2, C_2 = prod_{p>2}(1 - 1/(p-1)^2) ~ 0.6601618.

    This is the BASE constant of the Goldbach singular series (2*C_2 ~ 1.3203236),
    the q -> infinity limit of S(2q).  It is NOT itself equal to S(N) for any
    finite even N that has an odd prime divisor.

    CORRECTION (do not confuse the base constant with the series).  For N = 2q
    with q an odd prime,
        S(2q) = 2*C_2 * (q-1)/(q-2)   (NOT 2*C_2),
    e.g. q=3 -> factor 2, q=5 -> 4/3, q=7 -> 6/5.  More generally, for even N,
        S(N) = 2*C_2 * prod_{p | N, p odd} (p-1)/(p-2).
    The odd-prime factors p | N each multiply the base constant by (p-1)/(p-2) > 1
    (``odd_prime_transport_factor``); 2*C_2 is recovered only in the limit as the
    odd prime(s) dividing N tend to infinity.  Keep this constant DISTINCT from the
    full singular series; see ``singular_series_via_transport`` for the exact finite
    transport S_{<=P}(N) = 2*T(P) * prod_{p|N, odd}(p-1)/(p-2).

    Enclosure:  T(P) = prod_{2<p<=P}(1 - 1/(p-1)^2);
        hi = 2*T(P)  (>= 2*C_2, the partial product decreases to C_2 from above),
        lo = 2*T(P) * (1 - 1/(P-1))  (tail bound prod_{p>P}(1-1/(p-1)^2) >= 1-1/(P-1)).
    """
    if type(P) is not int or P < 3:
        raise GoldbachCircleError("P must be an integer >= 3")
    prod = Fraction(1)
    for p in _primes_upto(P):
        if p > 2:
            prod *= Fraction(1) - Fraction(1, (p - 1) ** 2)
    base = 2 * prod
    return base * (Fraction(1) - Fraction(1, P - 1)), base


# --------------------------------------------------------------------------
# GC-03 : finite singular-series TRANSPORT lemma (CLASSICAL; exact identity +
#         certified tail).  Transports the base constant 2*C_2 to S(N).
# --------------------------------------------------------------------------
def odd_prime_transport_factor(N: int) -> Fraction:
    """Exact rational transport factor  K(N) = prod_{p | N, p odd} (p-1)/(p-2).

    This is the factor by which each distinct odd prime divisor of N multiplies
    the base constant 2*C_2 in the Hardy-Littlewood singular series.  Depends only
    on the DISTINCT odd primes dividing N (the local factor S_p(N) = 1 + 1/(p-1)
    is insensitive to the exponent of p in N), so K(6) = K(18) = 2.  Empty product
    (N a power of 2) gives K(N) = 1.  EXACT (Fraction); no RH, no zeta zeros.
    """
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("odd_prime_transport_factor needs integer N >= 1")
    k = Fraction(1)
    for p, _e in prime_factors(N):
        if p % 2 == 1:
            # p >= 3 is an odd prime, so p - 2 >= 1: the factor is a well-defined
            # positive rational (never a division by zero).
            k *= Fraction(p - 1, p - 2)
    return k


def singular_series_via_transport(N: int, P: int) -> Fraction:
    """Finite singular-series TRANSPORT (GC-03; CLASSICAL, EXACT finite identity).

    LEMMA.  Let N be even and let P >= largest prime factor of N.  With
        T(P)  = prod_{2<p<=P} (1 - 1/(p-1)^2)        (2*T(P) = twin upper value)
        K(N)  = prod_{p | N, p odd} (p-1)/(p-2)       (odd_prime_transport_factor)
    the truncated Goldbach singular series factorises EXACTLY as
        S_{<=P}(N) := prod_{p<=P} S_p(N) = 2 * T(P) * K(N).

    PROOF (pure finite Euler-product algebra).  S_2(N) = 2 (N even).  For an odd
    prime p: if p | N then S_p = 1 + 1/(p-1) = p/(p-1); else S_p = 1 - 1/(p-1)^2
    = p(p-2)/(p-1)^2.  Multiply the base product prod_{2<p<=P}(1-1/(p-1)^2) = T(P)
    and, for each odd p | N (all <= P by hypothesis), replace its (1-1/(p-1)^2)
    factor by (1+1/(p-1)); the per-prime ratio is
        [p/(p-1)] / [p(p-2)/(p-1)^2] = (p-1)/(p-2),
    whose product over odd p | N is K(N).  Hence S_{<=P}(N) = 2*T(P)*K(N). QED.

    APPROXIMATION ERROR: ZERO (exact Fraction identity).  Equals
    ``singular_series_truncated(N, P)`` exactly (an independent route; the two are
    cross-checked in the tests).  Hypothesis P >= largest prime factor is REQUIRED:
    if some odd p | N exceeds P its enhanced factor S_p > 1 is simply missing from
    the base product and the identity fails.  For N odd, S(N) = 0 (p=2 local
    obstruction): returned as 0 to match ``singular_series_truncated``.
    """
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("singular_series_via_transport needs integer N >= 1")
    if N % 2 == 1:
        return Fraction(0)
    largest_pf = max((p for p, _ in prime_factors(N)), default=1)
    if P < largest_pf:
        raise GoldbachCircleError(
            f"P={P} must be >= largest prime factor {largest_pf} of N for the transport "
            "identity (else an enhanced odd-prime factor S_p>1 is missing)")
    _lo_twin, hi_twin = twin_prime_constant_enclosure(max(P, 3))   # hi_twin = 2*T(P)
    return hi_twin * odd_prime_transport_factor(N)


def singular_series_transport_enclosure(N: int, P: int) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for the FULL S(N) (even N) via the GC-03 transport lemma.

        lo = 2*T(P) * (1 - 1/(P-1)) * K(N),    hi = 2*T(P) * K(N),
    with T(P), K(N) as in ``singular_series_via_transport``.  The identity part is
    EXACT; the only inexactness is the Euler tail prod_{p>P}(1-1/(p-1)^2), bounded
    in [1 - 1/(P-1), 1] (so the relative width hi/lo - 1 <= 1/(P-2)).  Equals
    ``singular_series_enclosure(N, P)`` exactly -- an independent second route to
    the same certified bracket (cross-checked in the tests).  For N odd: (0, 0).

    IMPORTED DEPENDENCIES: none beyond elementary analysis (finite Euler-product
    algebra + the convergent-tail comparison sum_{n>P} 1/(n-1)^2 <= 1/(P-1)).  NO
    Siegel-Walfisz, NO RH, NO zeta zeros.  This bounds the singular-series CONSTANT
    only; it is NOT a claim about R_Lambda(N) (that needs the open minor arcs).
    """
    if type(N) is not int or N < 1:
        raise GoldbachCircleError("singular_series_transport_enclosure needs integer N >= 1")
    if N % 2 == 1:
        return Fraction(0), Fraction(0)
    hi = singular_series_via_transport(N, P)
    return hi * (Fraction(1) - Fraction(1, P - 1)), hi


def major_arc_benchmark(N: int, P: int, A: int = 2) -> Dict[str, object]:
    """Structural MAJOR-ARC benchmark under IMPORTED Siegel-Walfisz (NOT a certificate).

    Assembles -- with explicit, honest labels -- the ingredients of the circle-method
    major-arc estimate for R_Lambda(N) = integral_0^1 F_N(theta)^2 e(-N theta) dtheta,
    F_N(theta) = sum_{n=1}^{N-1} Lambda(n) e(n theta), on R/Z (period-1 wraparound).

    IMPORTED THEOREM (Siegel-Walfisz).  Fix A > 0.  Uniformly for moduli q <= (log N)^A
    and residues (a, q) = 1,
        psi(x; q, a) = x/phi(q) + O_A( x * exp(-c_A sqrt(log x)) ),
    where psi(x; q, a) = sum_{n<=x, n == a (q)} Lambda(n).  CRITICAL HONESTY: the
    implied constant c_A is INEFFECTIVE (it depends on a possible Siegel zero), so
    this estimate yields NO computable numerical error bound -- it is NOT a
    certificate (AGENTS.md discipline 8).

    BOUNDED UNIFORMITY.  Siegel-Walfisz controls ONLY q <= Q_SW := floor((log N)^A).
    One MUST NOT infer a uniform arbitrary-Q major-arc asymptotic from it: the
    major arcs with (log N)^A < q <= N^{1/2} and the entire minor-arc set are
    NOT controlled by Siegel-Walfisz.  This is exactly why Siegel-Walfisz alone
    does not prove binary Goldbach.

    WHAT IS ACTUALLY CERTIFIED (exact, no imported analytic input): the singular
    series S(N) itself, via ``singular_series_transport_enclosure(N, P)`` (GC-03).
    The returned ``singular_series_bracket`` is that exact two-sided enclosure; the
    truncation error (S - S_{<=P}) is the certified relative tail <= 1/(P-2).

    Returns a labelled dict; all analytic-asymptotic fields are strings, never a
    float masquerading as a bound.  Binary Goldbach: OPEN.
    """
    if type(N) is not int or N < 4 or N % 2 == 1:
        raise GoldbachCircleError("major_arc_benchmark needs an even integer N >= 4")
    if type(A) is not int or A < 1:
        raise GoldbachCircleError("A must be an integer >= 1")
    from math import log
    q_sw = int(log(N) ** A)                      # Siegel-Walfisz admissible modulus cutoff
    s_lo, s_hi = singular_series_transport_enclosure(N, P)
    return {
        "N": N,
        "P_truncation": P,
        "A": A,
        "siegel_walfisz_modulus_cutoff_Q_SW": q_sw,
        "carrier": "F_N(theta) = sum_{n=1}^{N-1} Lambda(n) e(n theta) on R/Z (period 1)",
        "target": "R_Lambda(N) = integral_0^1 F_N(theta)^2 e(-N theta) dtheta  (F^2, not |F|^2)",
        "imported_theorem": "Siegel-Walfisz: psi(x;q,a)=x/phi(q)+O_A(x exp(-c_A sqrt(log x))), q<=(log x)^A",
        "imported_constant_status": "INEFFECTIVE (possible Siegel zero) -- NOT a numerical certificate",
        "uniformity_bound": f"Siegel-Walfisz controls ONLY q <= Q_SW = {q_sw}; larger q uncontrolled",
        "singular_series_bracket": (s_lo, s_hi),          # EXACT certified (GC-03), no imported input
        "singular_series_truncation_rel_error_upper": Fraction(1, P - 2),
        "predicted_major_arc_main_term": "S(N)*N*(1+o(1))  (CONJECTURED shape; ineffective o(1))",
        "major_arc_status": "CLASSICAL asymptotic SHAPE; error term ineffective -> not certified",
        "minor_arc_status": "OPEN for binary Goldbach (ternary = Vinogradov); the open difficulty",
        "binary_goldbach": "OPEN",
        "rh_used": False,
    }


def goldbach_main_term_enclosure(N: int, P: int) -> Tuple[Fraction, Fraction]:
    """CONJECTURED (OPEN) Hardy-Littlewood main term S(N)*N, as a certified bracket.

    This is the PREDICTED major-arc main term for R_Lambda(N); the claim that the
    full R_Lambda(N) is asymptotic to it is binary-Goldbach-type and OPEN.  No
    Goldbach claim is made -- this returns the prediction only.
    """
    lo, hi = singular_series_enclosure(N, P)
    return lo * N, hi * N


def singular_series_comparison_evidence(Ns: Tuple[int, ...], P: int = 2000
                                        ) -> Tuple[Dict[str, float], ...]:
    """EVIDENCE (float, NOT a certificate): R_Lambda(N)/N vs the exact S(N) bracket.

    Illustrates (never proves) the CONJECTURED asymptotic R_Lambda(N) ~ S(N)*N.
    The ratio approaches S(N) slowly; small-N rows are far from the limit.  This
    is finite-sample evidence only; binary Goldbach stays OPEN.
    """
    rows = []
    for N in Ns:
        rl = goldbach_representation_R_Lambda(N)
        ratio = float(rl) / N
        lo, hi = singular_series_enclosure(N, P)
        rows.append({"N": float(N), "R_Lambda_over_N": ratio,
                     "S_lo": float(lo), "S_hi": float(hi)})
    return tuple(rows)


# --------------------------------------------------------------------------
# Major/minor-arc Farey structure (exposed, not asymptotically evaluated).
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class MajorArc:
    a: int        # numerator of the rational centre a/q
    q: int        # denominator (<= Q), gcd(a, q) = 1
    half_width: Fraction   # 1/(q*N): the arc is [a/q - 1/(qN), a/q + 1/(qN)]


def farey_major_arcs(Q: int, N: int) -> Tuple[MajorArc, ...]:
    """Exact major-arc centres/radii for the circle method at level Q, modulus N.

    Major arcs  M = union over q<=Q, (a,q)=1, 0<=a<q  of {theta: |theta - a/q| <= 1/(qN)}.
    This EXPOSES the decomposition structure; the major-arc integral gives the
    S(N)*N main term (CLASSICAL under Siegel-Walfisz).  The minor arcs are the
    complement; the minor-arc bound for the BINARY problem is OPEN.
    """
    if type(Q) is not int or Q < 1 or type(N) is not int or N < 2:
        raise GoldbachCircleError("farey_major_arcs needs Q >= 1 and N >= 2")
    from math import gcd as _gcd
    arcs: List[MajorArc] = []
    for q in range(1, Q + 1):
        for a in range(0, q):
            if _gcd(a, q) == 1:
                arcs.append(MajorArc(a=a, q=q, half_width=Fraction(1, q * N)))
    return tuple(arcs)


def arc_decomposition_summary(Q: int, N: int) -> Dict[str, object]:
    """Structural summary of the major/minor-arc split (no asymptotics evaluated)."""
    arcs = farey_major_arcs(Q, N)
    total_major_measure = sum((2 * a.half_width for a in arcs), Fraction(0))
    return {
        "Q": Q, "N": N, "num_major_arcs": len(arcs),
        "total_major_measure_upper": total_major_measure,  # ignores overlaps; upper bound
        "major_arc_status": "CLASSICAL main term S(N)*N (Siegel-Walfisz)",
        "minor_arc_status": "OPEN for binary Goldbach (ternary = Vinogradov)",
        "goldbach_claim": "NONE; binary Goldbach is OPEN",
    }
