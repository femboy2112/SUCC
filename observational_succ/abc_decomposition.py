"""Exact prime-power ANATOMY of the abc ris-moment, and the exact obstruction to
pushing the Cauchy-Schwarz moment bound past t = 1/2 (Operation Rigidity Forge,
Part VII, section 6).

This module is a DIFFERENT METHOD, not a rewrite of the Cauchy-Schwarz argument
in ``abc_triple_moment.py`` (ABC-TMB-01).  Where that module bounds the second
moment by a diagonal Cauchy-Schwarz + ABC-CLK-02 averaging lemma, this module
decomposes ``ris(n)`` EXACTLY over its prime-power exponent layers -- the exact,
epsilon-free specialisation of the "anatomy" decomposition (Lemma 2.2) of
Bernert-Browning-Lichtman-Teraevaeinen, arXiv:2410.12234v2 (May 2026) -- and
uses the decomposition to LOCALISE the obstruction.  The headline findings:

  ABC-DEC-01  (exact layer anatomy; PROVED LOCAL -- exact algebraic identity).
      With the exponent-layer radical  m_j(n) = prod_{p : v_p(n)=j} p,
          n       = prod_{j>=1} m_j(n)^j          (exact)
          rad(n)  = prod_{j>=1} m_j(n)             (exact)
          ris(n)  = prod_{j>=2} m_j(n)^(j-1)       (exact)   => ris(n)^t = prod m_j^{t(j-1)}
      the m_j are pairwise coprime, and if max_p v_p(n) = E then every product
      truncates at j <= E with NO tail (the n0 = 1, eps0 = 0 case of BBLT
      Lemma 2.2).  Machine-checked exactly on [1, N].

  ABC-DEC-02  (uniform per-layer threshold; PROVED LOCAL conditional on ABC-CLK-02).
      Each exponent layer j>=2 contributes to the theta-moment mean a per-prime
      term of exact size  (p-1) * p^{(j-1)theta - j - 1} ~ p^{(j-1)theta - j},
      whose Euler product over p converges iff  (j-1)theta - j < -1  <=>  theta < 1,
      INDEPENDENT of the layer index j.  Consequences:
        (a) the ris^theta averaging constant is finite iff theta < 1 (every layer
            hits the SAME theta = 1 wall; the square layer j=2 is merely the
            first to appear, not the only obstruction);
        (b) restricting to a bounded-exponent class {max v_p <= E} truncates the
            layers -- bounding the constant to M_E(theta) <= M(theta) -- but does
            NOT move the threshold theta < 1;
        (c) therefore the Cauchy-Schwarz moment ceiling t < 1/2 (which needs the
            inner exponent theta = 2t < 1) is NOT liftable by bounding the
            exponent or by deleting any single layer.  This is a decisive NO-GO
            for the elementary (diagonal) route.

  ABC-DEC-03  (the machinery boundary; the gap statement IS the result).
      To pass t = 1/2 one must bound the ADDITIVE correlation
          I(c) = sum_{a+b=c, (a,b)=1} ris(a)^t ris(b)^t
      BELOW its diagonal Cauchy-Schwarz value, i.e. exploit cancellation from the
      constraint a+b=c.  The circle-method HEURISTIC predicts I(c) asymptotic to
      c (so S_t ~ X^2) for all t < 1, but a rigorous bound requires the Fourier
      second/fourth-moment exponential-sum bounds (BBLT Prop. 3.1) and the
      Heath-Brown geometry-of-numbers integer-point count on the linear slice
      (BBLT Prop. 4.1).  SUCC's Euler-product toolkit supplies NEITHER.  A finite
      census is consistent with -- but cannot establish -- an X^2 bound for
      1/2 <= t < 1 (the ratio S_t/X^2 grows slowly even for PROVEN t < 1/2, so
      the census cannot decide).  The abc conjecture stays OPEN.

EXACTNESS DISCIPLINE (AGENTS.md item 8).  Census/moment objects are integer- or
Fraction-exact; rational powers are returned as CERTIFIED two-sided rational
enclosures (sound interval arithmetic, never a float).  The only float appears in
functions whose name ends ``_evidence`` and whose docstring says EVIDENCE; those
are illustrations, never certificates.

RH PROVED: NO.  No zeta-zero ordinate is used anywhere.  abc stays OPEN;
no new exceptional-set exponent, no uniform bound past the proven t < 1/2.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Tuple

from .abc_clock_families import ABCClockError, prime, prime_factors, radical, ris
from .abc_triple_moment import (
    integer_moment,
    power_enclosure,
    primitive_triples,
    ris_spectrum,
)


# --------------------------------------------------------------------------
# ABC-DEC-01 : exact prime-power exponent anatomy (BBLT Lemma 2.2, eps0 = 0).
# --------------------------------------------------------------------------
def exponent_layers(n: int) -> Dict[int, int]:
    """Exact layer map  {j : m_j(n)}  with  m_j(n) = prod_{p : v_p(n)=j} p.

    Returns only the occupied layers (j with at least one prime at exactly that
    valuation).  n = 1 gives the empty map.  Pure integer arithmetic.
    """
    if type(n) is not int or n < 1:
        raise ABCClockError("exponent_layers needs an integer n >= 1")
    layers: Dict[int, int] = {}
    for p, k in prime_factors(n):
        layers[k] = layers.get(k, 1) * p
    return layers


def max_exponent(n: int) -> int:
    """Largest prime valuation E = max_p v_p(n); 0 for n = 1."""
    layers = exponent_layers(n)
    return max(layers) if layers else 0


@dataclass(frozen=True)
class LayerAnatomy:
    """Exact reconstruction certificate for one integer n (ABC-DEC-01)."""
    n: int
    layers: Tuple[Tuple[int, int], ...]   # sorted ((j, m_j), ...)
    n_reconstructed: int
    radical_reconstructed: int
    ris_reconstructed: int
    pairwise_coprime: bool
    max_exponent: int

    @property
    def identity_holds(self) -> bool:
        return (
            self.n_reconstructed == self.n
            and self.radical_reconstructed == radical(self.n)
            and self.ris_reconstructed == ris(self.n)
            and self.pairwise_coprime
        )


def layer_anatomy(n: int) -> LayerAnatomy:
    """Exact ABC-DEC-01 certificate: rebuild n, rad(n), ris(n) from the layers.

    Verifies  n = prod m_j^j,  rad = prod m_j,  ris = prod m_j^{j-1},  and that
    the m_j are pairwise coprime.  ``identity_holds`` must be True for every
    n >= 1; this is the executable receipt for the exact anatomy identity.
    """
    layers = exponent_layers(n)
    items = tuple(sorted(layers.items()))
    n_rec = 1
    rad_rec = 1
    ris_rec = 1
    for j, m in items:
        n_rec *= m ** j
        rad_rec *= m
        ris_rec *= m ** (j - 1)
    ms = [m for _, m in items]
    coprime = all(gcd(ms[i], ms[k]) == 1 for i in range(len(ms)) for k in range(i + 1, len(ms)))
    return LayerAnatomy(
        n=n, layers=items, n_reconstructed=n_rec,
        radical_reconstructed=rad_rec, ris_reconstructed=ris_rec,
        pairwise_coprime=coprime, max_exponent=(max(layers) if layers else 0),
    )


def ris_power_layer_factorization(n: int, t) -> Tuple[Tuple[int, int, Fraction], ...]:
    """Exact factorisation of ris(n)^t over layers:  ris(n)^t = prod m_j^{t(j-1)}.

    Returns a tuple of (j, m_j, t*(j-1)) for the j >= 2 layers (j=1 contributes
    the trivial factor m_1^0 = 1 and is omitted).  The product of m_j^{exponent}
    equals ris(n)^t exactly.  t may be any rational (Fraction/int).
    """
    tf = t if isinstance(t, Fraction) else Fraction(t)
    out: List[Tuple[int, int, Fraction]] = []
    for j, m in sorted(exponent_layers(n).items()):
        if j >= 2:
            out.append((j, m, tf * (j - 1)))
    return tuple(out)


def bblt_anatomy(n: int, d: int) -> Dict[str, object]:
    """BBLT Lemma 2.2 form:  n = n0 * prod_{j=1}^{d} m_j^j  with the tail in n0.

    n0 = prod_{j>d} m_j^j collects the primes with valuation > d.  BBLT make n0
    small (<= n^{eps0}) by choosing d ~ 1/eps0; HERE we observe the EXACT fact
    that n0 = 1 exactly iff max_p v_p(n) <= d (the eps0 = 0 specialisation).
    Returns {'n0', 'truncated_layers', 'exact_when_bounded'} with
    exact_when_bounded = (n0 == 1) == (max_exponent(n) <= d).
    """
    if type(d) is not int or d < 1:
        raise ABCClockError("bblt_anatomy needs an integer d >= 1")
    layers = exponent_layers(n)
    n0 = 1
    trunc: Dict[int, int] = {}
    for j, m in layers.items():
        if j <= d:
            trunc[j] = m
        else:
            n0 *= m ** j
    return {
        "n0": n0,
        "truncated_layers": tuple(sorted(trunc.items())),
        "exact_when_bounded": (n0 == 1) == (max_exponent(n) <= d),
    }


# --------------------------------------------------------------------------
# Reproduce the census anchor (independent radical route cross-check).
# --------------------------------------------------------------------------
def _radical_sympy(n: int) -> int:
    """Independent radical via prime_factors (same source), kept for the anchor
    cross-check through a different code path (layer product vs direct)."""
    r = 1
    for p, _ in prime_factors(n):
        r *= p
    return r


def census_anchor_S1(X: int = 24) -> Dict[str, int]:
    """Reproduce S_1(X) two independent ways and confirm they agree.

    Route A: ``integer_moment(X, 1)`` from abc_triple_moment (ris-spectrum sum).
    Route B: direct enumeration with a layer-product ris recomputed here.
    For X = 24 both must equal the documented anchor 557 (ordered count).
    """
    route_a = integer_moment(X, 1, ordered=True)
    route_b = 0
    for c in range(2, X + 1):
        for a in range(1, c):
            b = c - a
            if gcd(a, b) == 1:
                # ris via the exact layer product (ABC-DEC-01), independent path
                rsum = 1
                for m, mm in ((a, 0), (b, 0), (c, 0)):
                    for j, lm in exponent_layers(m).items():
                        rsum *= lm ** (j - 1)
                route_b += rsum
    return {"X": X, "route_a_integer_moment": route_a, "route_b_layer_product": route_b,
            "agree": route_a == route_b}


# --------------------------------------------------------------------------
# ABC-DEC-02 : the uniform per-layer convergence threshold (the obstruction).
# --------------------------------------------------------------------------
def layer_mean_leading_exponent(j: int, theta) -> Fraction:
    """Exact leading per-prime exponent of the layer-j contribution: (j-1)*theta - j.

    The layer-j (v_p = j exactly) Haar density is (p-1)/p^{j+1} and its ris value
    is ris(p^j)^theta = p^{(j-1)theta}, so the per-prime contribution is
    (p-1) * p^{(j-1)theta - j - 1}, with leading exponent (j-1)theta - j.
    """
    if type(j) is not int or j < 1:
        raise ABCClockError("layer index j must be an integer >= 1")
    tf = theta if isinstance(theta, Fraction) else Fraction(theta)
    return (j - 1) * tf - j


def layer_euler_product_converges(j: int, theta) -> bool:
    """Does the layer-j Euler product sum_p (p-1)p^{(j-1)theta-j-1} converge?

    True iff the leading exponent (j-1)theta - j < -1, i.e. (for j >= 2)
    iff theta < 1.  For j = 1 (squarefree layer, exponent -1) the term is ~1/p,
    which diverges logarithmically -- but that layer carries ris = 1, so it does
    not enter the ris^theta moment at all (its factor is m_1^0 = 1).
    """
    return layer_mean_leading_exponent(j, theta) < -1


def uniform_layer_threshold(max_layer: int = 12) -> Dict[str, object]:
    """ABC-DEC-02(a): every layer j = 2..max_layer has the SAME threshold theta<1.

    Returns {'threshold', 'per_layer'} where per_layer[j] is the exact theta*
    solving (j-1)theta* - j = -1, i.e. theta* = (j-1)/(j-1) = 1 for all j >= 2.
    The point is that this is INDEPENDENT of j: bounding the exponent (dropping
    layers above E) never changes the common wall theta = 1.
    """
    per_layer = {}
    for j in range(2, max_layer + 1):
        # solve (j-1)theta - j = -1  ->  theta = (j-1)/(j-1) = 1
        per_layer[j] = Fraction(j - 1, j - 1)
    return {"threshold": Fraction(1), "per_layer": per_layer,
            "uniform": all(v == Fraction(1) for v in per_layer.values())}


def local_ris_mean_factor_enclosure(p: int, theta, precision: int = 10 ** 9
                                    ) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] rational bracket for the exact p-adic Haar local mean
        E_p(theta) = (p-1)/p * (1 + p^{-theta}/(p^{1-theta} - 1)),   theta < 1.

    This is the conditional p-adic Haar mean of ris_p^theta (ABC-CLK discipline:
    a Haar proportion, NOT an independence claim for bounded integers).  Its
    Euler product over p converges iff theta < 1 -- the SAME threshold as the
    rigorously-established ABC-CLK-02 constant M(theta), cross-confirmed here by
    an independent (Haar-local) route.  Exactness: theta = num/den with num<den,
    brackets p^theta and p^{1-theta} with ``power_enclosure``.
    """
    tf = theta if isinstance(theta, Fraction) else Fraction(theta)
    num, den = tf.numerator, tf.denominator
    if not (0 <= num < den):
        raise ABCClockError("local_ris_mean_factor needs 0 <= theta < 1 rational")
    if not prime(p):
        raise ABCClockError("p must be an actual prime")
    lo_pt, hi_pt = power_enclosure(p, num, den, precision)          # p^theta
    lo_p1, hi_p1 = power_enclosure(p, den - num, den, precision)    # p^{1-theta}
    if lo_p1 <= 1:
        raise ABCClockError("precision too low: need lo(p^{1-theta}) > 1")
    pref = Fraction(p - 1, p)
    # term = p^{-theta}/(p^{1-theta}-1):  lower uses (1/hi_pt)/(hi_p1-1); upper (1/lo_pt)/(lo_p1-1)
    term_lo = (1 / hi_pt) / (hi_p1 - 1)
    term_hi = (1 / lo_pt) / (lo_p1 - 1)
    return pref * (1 + term_lo), pref * (1 + term_hi)


def cauchy_schwarz_ceiling() -> Dict[str, object]:
    """ABC-DEC-02(c): the exact ceiling of the diagonal moment method.

    The inner Cauchy-Schwarz needs the inner exponent theta = 2t to satisfy the
    layer threshold theta < 1, i.e. t < 1/2.  Returns the exact ceiling and the
    binding constraint, flagged as a METHOD limit, not a growth threshold.
    """
    return {"ceiling_t": Fraction(1, 2),
            "binding_constraint": "inner exponent theta = 2t < 1 (layer threshold)",
            "nature": "Cauchy-Schwarz METHOD limit, not a growth threshold of S_t",
            "bounded_exponent_helps": False}


# --------------------------------------------------------------------------
# ABC-DEC-03 : the additive-correlation route and the machinery boundary.
# --------------------------------------------------------------------------
def inner_correlation_enclosure(c: int, t, precision: int = 10 ** 9
                                ) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for  I(c) = sum_{a+b=c,(a,b)=1} ris(a)^t ris(b)^t.

    For a coprime pair, ris(a)^t ris(b)^t = (ris(a)ris(b))^t exactly, so each
    term is one certified power bracket.  Exact for integer t (lo == hi).
    """
    if type(c) is not int or c < 2:
        raise ABCClockError("inner_correlation needs integer c >= 2")
    tf = t if isinstance(t, Fraction) else Fraction(t)
    num, den = tf.numerator, tf.denominator
    if num < 0:
        raise ABCClockError("t must be >= 0")
    lo = Fraction(0)
    hi = Fraction(0)
    for a in range(1, c):
        b = c - a
        if gcd(a, b) == 1:
            rlo, rhi = power_enclosure(ris(a) * ris(b), num, den, precision)
            lo += rlo
            hi += rhi
    return lo, hi


def additive_vs_diagonal_evidence(c: int, t: float) -> Dict[str, float]:
    """EVIDENCE (float, NOT a certificate): compare the true additive correlation
    I(c) to its Cauchy-Schwarz diagonal majorant D(c) = sum_{n<c} ris(n)^{2t}.

    The diagonal bound I(c) <= D(c) is what forces 2t < 1.  The circle-method
    heuristic predicts the TRUE I(c) is order c (much smaller than D(c) once the
    moment is heavy), i.e. the diagonal bound is lossy and the real threshold is
    t < 1.  Returns ratios as floats for illustration only.
    """
    I = 0.0
    for a in range(1, c):
        b = c - a
        if gcd(a, b) == 1:
            I += (ris(a) ** t) * (ris(b) ** t)
    D = sum(ris(n) ** (2 * t) for n in range(1, c))
    return {"c": float(c), "t": t, "I_c": I, "diagonal_D_c": D,
            "I_over_c": I / c, "I_over_D": I / D if D else 0.0}


def moment_ratio_growth_evidence(t: float, Xs: Tuple[int, ...] = (64, 128, 256, 512)
                                 ) -> Tuple[Dict[str, float], ...]:
    """EVIDENCE (float, NOT a certificate): the ratio S_t(X)/X^2 across X.

    Illustrates ABC-DEC-03's honesty clause: the ratio drifts upward even for
    PROVEN t < 1/2 (it approaches its finite limiting constant from below), so a
    finite census CANNOT distinguish a bounded X^2 ratio from a slowly growing
    one.  Hence the census is consistent with -- never a proof of -- an X^2 bound
    for 1/2 <= t < 1.
    """
    rows = []
    for X in Xs:
        S = 0.0
        for c in range(2, X + 1):
            rc = ris(c) ** t
            for a in range(1, c):
                b = c - a
                if gcd(a, b) == 1:
                    S += rc * (ris(a) ** t) * (ris(b) ** t)
        rows.append({"X": float(X), "t": t, "S_t": S, "ratio": S / (X * X)})
    return tuple(rows)


def machinery_boundary() -> Dict[str, object]:
    """ABC-DEC-03: what is elementary here vs what needs serious machinery.

    Returns a structured ledger so the division is explicit and testable.
    """
    return {
        "elementary_in_SUCC": (
            "ABC-DEC-01 exact layer anatomy (algebraic identity); "
            "ABC-DEC-02 per-layer exponents (j-1)theta-j and the uniform "
            "threshold theta<1; the Cauchy-Schwarz ceiling t<1/2; the "
            "bounded-exponent truncation M_E(theta) <= M(theta)."
        ),
        "needs_machinery_not_in_SUCC": (
            "passing t=1/2 requires cancellation in I(c)=sum_{a+b=c} ris^t ris^t "
            "below the diagonal: BBLT Prop. 3.1 Fourier 2nd/4th-moment "
            "exponential-sum bounds, and BBLT Prop. 4.1 Heath-Brown "
            "geometry-of-numbers integer-point counts on the linear slice."
        ),
        "beats_half_rigorously": False,
        "heuristic_true_threshold": Fraction(1),   # circle method predicts t<1
        "abc_status": "OPEN",
    }
