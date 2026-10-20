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
      INDEPENDENT of the layer index j >= 2.  Consequences:
        (a) the ris^theta averaging constant is finite iff theta < 1 (every layer
            j >= 2 hits the SAME theta = 1 wall; the square layer j=2 is merely the
            first to appear, not the only obstruction);
        (b) QUALIFIED (Part V repair -- the earlier unqualified claim was too broad).
            Restricting to the bounded-exponent class {max_p v_p <= E} truncates the
            layers to j <= E; the effect on the theta = 1 wall DEPENDS ON E:
              * E = 1 (squarefree class): ris(n) = 1 identically, so the only
                surviving local factor is  E_p^{(1)}(theta) = (p-1)/p (1 + 1/p)
                = 1 - 1/p^2,  INDEPENDENT of theta.  The class mean is
                prod_p (1 - 1/p^2) = 6/pi^2 for EVERY theta (including theta >= 1):
                the theta = 1 wall is ABSENT in this layer.  (But ris = 1 makes it
                vacuous for abc.)
              * E >= 2: the exponent-two layer alone already carries the term
                (1 - 1/p) p^{theta-2}, whose Euler product sum_p p^{theta-2}
                diverges at theta = 1, so the wall PERSISTS with threshold
                theta < 1 and the truncated constant obeys M_E(theta) <= M(theta).
            So "bounded exponent does not move the threshold" is TRUE only for
            E >= 2; for E = 1 the wall vanishes (vacuously).  [ABC-DEC-02q]
        (c) therefore the Cauchy-Schwarz moment ceiling t < 1/2 (which needs the
            inner exponent theta = 2t < 1) is NOT liftable by bounding the
            exponent to any E >= 2 or by deleting any single layer j >= 2.  This
            is a decisive NO-GO for the elementary (diagonal) route.

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

PART V (Proof Forge III -- repair + advance the moment frontier; 2026-10-20).
  ABC-DEC-02q   qualified bounded-exponent statement: E=1 squarefree class has NO
                theta=1 wall (ris==1, mean 6/pi^2 for all theta) but is vacuous;
                E>=2 retains the wall via the exponent-two layer alone.  See the
                revised consequence (b) above, ``squarefree_class_moment`` and
                ``bounded_exponent_local_factor_enclosure``.
  ABC-FM        a four-failure-mode ledger (``failure_mode_ledger``) recording which
                failures are ESTABLISHED here -- only (a) diagonal/Cauchy-Schwarz and
                (b) a particular Euler-product majorant -- and which are NOT: (c) an
                entire proof class, (d) the theorem itself.  Correctness guard
                against over-claiming a method no-go as a mathematics no-go.
  ABC-COR-01/02/03  a Part-IV residue-box additive-correlation attempt on
                I_t(c) = sum_{a+b=c,(a,b)=1} ris(a)^t ris(b)^t.  The powerful-part
                residue decomposition has main term (X^2/2) G(t)^2 with
                G(t)=sum_{d powerful} ris(d)^t/d finite iff t < 1 (STRICTLY past the
                diagonal t < 1/2); but the residue-box error bound summed over the
                majorant is >> X^2 for every t >= 0, so it yields NO rigorous bound.
                Genuine partial theorem: the bounded-powerful-part truncation bound
                (explicit G_Q/A_Q/B_Q, all t).  Isolated missing estimate: a
                power-saving AP integer-point count uniform to modulus q ~ X.

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
from enum import Enum
from fractions import Fraction
from math import gcd, lcm
from typing import Dict, List, Tuple

from .abc_clock_families import ABCClockError, prime, prime_factors, radical, ris
from .abc_triple_moment import (
    integer_moment,
    power_enclosure,
    primitive_triples,
    ris_spectrum,
)
from .residue_box_counting import (
    error_bound as _rb_error_bound,
    main_term as _rb_main_term,
    residue_box_count,
    residues_from_predicate,
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
            "bounded_exponent_helps": False,
            # Part V qualification: "helps" = False means bounding to E >= 2 does not
            # lift t < 1/2 (the j=2 layer retains the wall).  The E = 1 squarefree
            # class trivially has no wall but is VACUOUS (ris(abc) = 1), so it is not
            # a lift of the real problem.
            "bounded_exponent_helps_for_E_ge_2": False,
            "E1_squarefree_is_vacuous": True}


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


# ==========================================================================
# PART V (Proof Forge III, 2026-10-20): repair + advance the moment frontier.
# ==========================================================================

# --------------------------------------------------------------------------
# Powerful-number primitives (ris depends only on the powerful part).
# --------------------------------------------------------------------------
def is_powerful(n: int) -> bool:
    """True iff every prime dividing n divides it to exponent >= 2 (n=1 powerful)."""
    if type(n) is not int or n < 1:
        raise ABCClockError("is_powerful needs an integer n >= 1")
    return all(k >= 2 for _, k in prime_factors(n))


def powerful_part(n: int) -> int:
    """P(n) = prod_{p : v_p(n) >= 2} p^{v_p(n)}.  Then ris(n) = ris(P(n)) exactly,
    and P(n) is a powerful number (the unique maximal powerful divisor d with
    the property that n/d is coprime to d and squarefree-complemented)."""
    if type(n) is not int or n < 1:
        raise ABCClockError("powerful_part needs an integer n >= 1")
    P = 1
    for p, k in prime_factors(n):
        if k >= 2:
            P *= p ** k
    return P


def powerful_numbers_up_to(Q: int) -> Tuple[int, ...]:
    """Exact ascending tuple of powerful numbers in [1, Q] via d = a^2 b^3
    (b squarefree) -- the classical bijective parametrisation, O(sqrt(Q))."""
    if type(Q) is not int or Q < 1:
        raise ABCClockError("powerful_numbers_up_to needs an integer Q >= 1")
    out = set()
    b = 1
    while b ** 3 <= Q:
        # b squarefree?
        if all(k < 2 for _, k in prime_factors(b)):
            a = 1
            while a * a * b ** 3 <= Q:
                out.add(a * a * b ** 3)
                a += 1
        b += 1
    return tuple(sorted(out))


# --------------------------------------------------------------------------
# TASK 1 -- ABC-DEC-02q : the QUALIFIED bounded-exponent statement (E=1 vs E>=2).
# --------------------------------------------------------------------------
def squarefree_class_moment(X: int, theta=None) -> Dict[str, object]:
    """ABC-DEC-02q, E = 1 half (EXACT, theta-independent).

    On the squarefree class {n <= X : max_p v_p(n) <= 1} every ris(n) = 1, so for
    EVERY theta (including theta >= 1)
        sum_{n <= X, n squarefree} ris(n)^theta = #{squarefree n <= X} <= X.
    The moment equals the squarefree count with NO theta dependence -- there is no
    theta = 1 wall in this layer.  Returned exactly as an integer (theta is accepted
    only to document that the value does not depend on it)."""
    if type(X) is not int or X < 1:
        raise ABCClockError("squarefree_class_moment needs an integer X >= 1")
    count = sum(1 for n in range(1, X + 1) if max_exponent(n) <= 1)
    return {"X": X, "squarefree_count": count,
            "moment_value": count, "moment_equals_count": True,
            "theta_independent": True, "bounded_by_X": count <= X,
            "wall_present": False}


def bounded_exponent_local_factor_enclosure(p: int, E: int, theta,
                                            precision: int = 10 ** 9
                                            ) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for the layer-truncated p-adic Haar factor
        E_p^{(E)}(theta) = (p-1)/p * (1 + sum_{j=1}^{E} p^{(j-1)theta - j}).

    This is ``local_ris_mean_factor_enclosure`` TRUNCATED to layers j <= E.
      * E = 1 returns the EXACT rational 1 - 1/p^2 (lo == hi), theta-INDEPENDENT.
      * E >= 2, integer theta returns an exact rational (lo == hi).
      * E >= 2, non-integer rational theta: each j >= 2 term p^{(j-1)theta - j} is
        a certified reciprocal power bracket (the exponent is negative since
        0 <= theta and (j-1)theta < j), summed into [lo, hi].
    The j = 2 term is (1-1/p) p^{theta-2}; its Euler product diverges at theta = 1,
    which is why the wall persists for E >= 2 but is absent for E = 1."""
    if type(E) is not int or E < 1:
        raise ABCClockError("bounded_exponent_local_factor needs integer E >= 1")
    if not prime(p):
        raise ABCClockError("p must be an actual prime")
    tf = theta if isinstance(theta, Fraction) else Fraction(theta)
    if tf < 0 or tf >= 1 and tf.denominator != 1:
        # allow integer theta >= 1 (exact); forbid non-integer theta >= 1 as the
        # geometric local series is only used for theta < 1 in the enclosure path.
        if not (tf.denominator == 1 and tf >= 0):
            raise ABCClockError("need 0 <= theta < 1 rational (or integer theta)")
    num, den = tf.numerator, tf.denominator
    lo_sum = Fraction(0)
    hi_sum = Fraction(0)
    for j in range(1, E + 1):
        # exponent (j-1)*theta - j = ((j-1)num - j*den)/den, which is <= -1 < 0.
        # term = p^{-e_num/den}; reduce the fraction so integer exponents stay EXACT
        # (e.g. the j=1 term is always p^{-1}; any e_num/den that lands on an integer).
        exp_f = Fraction(j * den - (j - 1) * num, den)    # = -(exponent) > 0, reduced
        e2n, e2d = exp_f.numerator, exp_f.denominator
        if e2d == 1:                              # exact rational term p^{-e2n}
            val = Fraction(1, p ** e2n)
            lo_sum += val
            hi_sum += val
        else:
            lo_pw, hi_pw = power_enclosure(p, e2n, e2d, precision)   # p^{e2n/e2d}
            lo_sum += 1 / hi_pw                   # p^{-e2n/e2d} lower
            hi_sum += 1 / lo_pw                   # upper
    pref = Fraction(p - 1, p)
    return pref * (1 + lo_sum), pref * (1 + hi_sum)


def bounded_exponent_threshold(E: int):
    """Qualified ABC-DEC-02q threshold for the class {max_p v_p <= E}:
      * E <= 1  -> None  (NO theta = 1 wall; the class mean prod_p(1-1/p^2) = 6/pi^2
                   is finite for every theta, because ris == 1 there);
      * E >= 2  -> Fraction(1)  (wall at theta = 1, retained by the j = 2 layer)."""
    if type(E) is not int or E < 0:
        raise ABCClockError("bounded_exponent_threshold needs integer E >= 0")
    return None if E <= 1 else Fraction(1)


def bounded_exponent_mean_converges(E: int, theta) -> bool:
    """Does the bounded-exponent class mean prod_p E_p^{(E)}(theta) converge?
      * E <= 1: True for EVERY theta (deviation is exactly -1/p^2, summable);
      * E >= 2: True iff theta < 1 (the j = 2 term (1-1/p)p^{theta-2} forces it)."""
    tf = theta if isinstance(theta, Fraction) else Fraction(theta)
    if E <= 1:
        return True
    return tf < 1


def qualified_bounded_exponent_statement() -> Dict[str, object]:
    """ABC-DEC-02q as a structured, testable ledger entry (the Part V repair of the
    over-broad consequence (b))."""
    return {
        "claim": "ABC-DEC-02q",
        "E_equals_1": {
            "ris": "identically 1 (squarefree class)",
            "local_factor": "E_p^{(1)}(theta) = 1 - 1/p^2 (theta-independent)",
            "class_mean": "prod_p (1 - 1/p^2) = 6/pi^2 for EVERY theta",
            "wall_at_theta_1": False,
            "vacuous_for_abc": True,
        },
        "E_ge_2": {
            "surviving_term": "j=2 layer carries (1-1/p) p^{theta-2}",
            "euler_product": "sum_p p^{theta-2} converges iff theta < 1",
            "wall_at_theta_1": True,
            "threshold": Fraction(1),
        },
        "repair": ("the earlier unqualified 'bounded exponent does not move the "
                   "threshold' is TRUE only for E >= 2; for E = 1 the wall vanishes "
                   "(but ris == 1 makes that layer vacuous for abc)"),
        "status": "PROVED LOCAL (E=1 exact; E>=2 conditional on ABC-CLK-02 constant)",
    }


# --------------------------------------------------------------------------
# TASK 2 -- ABC-FM : the four-failure-mode ledger (honest status; anti-overclaim).
# --------------------------------------------------------------------------
class FailureStatus(Enum):
    ESTABLISHED = "ESTABLISHED"
    NOT_ESTABLISHED = "NOT_ESTABLISHED"


@dataclass(frozen=True)
class FailureMode:
    """One of the four distinct things that could 'fail' when a bound stalls at
    t = 1/2.  ``status`` records whether THIS repository has actually established
    the failure; ``receipt`` points at the in-repo evidence (or says why absent)."""
    tag: str
    name: str
    description: str
    status: FailureStatus
    receipt: str


def failure_mode_ledger() -> Tuple[FailureMode, ...]:
    """ABC-FM.  Distinguish (a) a strategy failing, (b) a particular majorant
    failing, (c) an entire proof CLASS failing, (d) the THEOREM itself failing.
    ONLY (a) and (b) are established here.  Marking (c)/(d) proved would upgrade a
    method no-go into a mathematics no-go -- forbidden (AGENTS.md items 4, 5)."""
    return (
        FailureMode(
            tag="a",
            name="diagonal / Cauchy-Schwarz strategy",
            description=("the inner diagonal bound I(c) <= sum_{n<c} ris(n)^{2t} "
                         "needs 2t < 1, so the diagonal strategy cannot reach "
                         "t >= 1/2"),
            status=FailureStatus.ESTABLISHED,
            receipt="cauchy_schwarz_ceiling(); ABC-DEC-02(c); ABC-TMB-01 derivation",
        ),
        FailureMode(
            tag="b",
            name="particular local Euler-product majorant",
            description=("the specific majorant M(t)M(2t) uses the Euler product "
                         "M(theta) = prod_p E_p(theta), which diverges at theta = 1 "
                         "(the j=2 layer term p^{theta-2}); so this majorant blows "
                         "up at the inner exponent theta = 2t = 1, i.e. t = 1/2"),
            status=FailureStatus.ESTABLISHED,
            receipt=("local_ris_mean_factor_enclosure(); layer_euler_product_"
                     "converges(2, 1) is False; ABC-DEC-02(a)"),
        ),
        FailureMode(
            tag="c",
            name="entire proof CLASS",
            description=("that NO elementary / multiplicative / sieve-free approach "
                         "can bound S_t for 1/2 <= t < 1.  NOT shown: only two "
                         "specific strategies (a, b) are ruled out; the residue-box "
                         "main term (ABC-COR-01) already reaches t < 1, so the class "
                         "is NOT excluded"),
            status=FailureStatus.NOT_ESTABLISHED,
            receipt=("no proof of class-wide impossibility exists in this repo; "
                     "ABC-COR-01 main term reaches t < 1"),
        ),
        FailureMode(
            tag="d",
            name="the desired THEOREM itself",
            description=("that S_t(X)/X^2 is actually unbounded for some 1/2 <= t < 1 "
                         "(or that abc is false).  NOT shown -- the OPPOSITE is "
                         "expected: the circle-method heuristic predicts an X^2 "
                         "average bound up to t < 1, and abc is believed TRUE"),
            status=FailureStatus.NOT_ESTABLISHED,
            receipt=("ABC-TMB-03 dyadic tower shows only NO uniform POINTWISE bound; "
                     "mass is o(X^2); machinery_boundary()['heuristic_true_threshold']"
                     " = 1"),
        ),
    )


def failure_mode_overclaim_guard() -> Dict[str, object]:
    """Executable guard: exactly the first two modes are ESTABLISHED; (c) and (d)
    must stay NOT_ESTABLISHED.  A regression that flips (c) or (d) is an overclaim."""
    led = failure_mode_ledger()
    est = tuple(m.tag for m in led if m.status is FailureStatus.ESTABLISHED)
    not_est = tuple(m.tag for m in led if m.status is FailureStatus.NOT_ESTABLISHED)
    return {"established": est, "not_established": not_est,
            "correct": est == ("a", "b") and not_est == ("c", "d")}


# --------------------------------------------------------------------------
# TASK 3 -- ABC-COR : residue-box (Part IV) additive-correlation attempt.
# --------------------------------------------------------------------------
def ris_powerful_majorant_terms(a: int, t) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for the powerful-divisor majorant
        M_t(a) = sum_{d | a, d powerful} ris(d)^t   (>= ris(a)^t for all t >= 0).

    EXACT KEY INEQUALITY (proved):  ris(a)^t <= M_t(a).  Because ris and the sum are
    multiplicative and at each prime p || a to power v the powerful divisors are
    {1} U {p^2,...,p^v}, so the local factor 1 + sum_{i=2}^{v} p^{(i-1)t} >=
    p^{(v-1)t} = ris(p^v)^t (the top term alone).  Exact for integer t (lo == hi)."""
    if type(a) is not int or a < 1:
        raise ABCClockError("ris_powerful_majorant_terms needs integer a >= 1")
    tf = t if isinstance(t, Fraction) else Fraction(t)
    num, den = tf.numerator, tf.denominator
    if num < 0:
        raise ABCClockError("t must be >= 0")
    lo = Fraction(0)
    hi = Fraction(0)
    for d in range(1, a + 1):
        if a % d == 0 and is_powerful(d):
            rlo, rhi = power_enclosure(ris(d), num, den, 10 ** 9)
            lo += rlo
            hi += rhi
    return lo, hi


def joint_divisibility_count(d: int, dp: int, X: int) -> Dict[str, object]:
    """Encode the joint prime-power occupation 'd | a and d' | b' as a residue
    constraint mod W = lcm(d, d') and count #{(a,b): a,b>=1, a+b<=X, d|a, d'|b}
    with the Part IV residue-box theorem.  Returns the exact count, the main term
    |R|/W^2 * X^2/2 = X^2/(2 d d'), the proved error bound, and whether residue-box
    is informative (error < main) for this (d, d', X)."""
    if any(type(v) is not int or v < 1 for v in (d, dp, X)):
        raise ABCClockError("joint_divisibility_count needs integers d, d', X >= 1")
    W = lcm(d, dp)
    R = residues_from_predicate(W, lambda r, s: r % d == 0 and s % dp == 0)
    count = residue_box_count(X, W, R)
    mt = _rb_main_term(X, W, R)
    bnd = _rb_error_bound(X, W, R)
    return {"d": d, "dp": dp, "X": X, "W": W, "count": count,
            "main_term": mt, "error_bound": bnd,
            "informative": bnd < mt}


def powerful_main_term_leading_exponent(t) -> Fraction:
    """ABC-COR-01.  The per-prime leading exponent of the residue-box main-term
    constant G(t) = sum_{d powerful} ris(d)^t/d = prod_p (1 + p^{t-2}/(1-p^{t-1})).
    The dominant local deviation is the j=2 (p^2) term p^{t-2}, exponent t - 2."""
    tf = t if isinstance(t, Fraction) else Fraction(t)
    return tf - 2


def powerful_main_term_converges(t) -> bool:
    """ABC-COR-01.  G(t) = sum_{d powerful} ris(d)^t/d converges iff t < 1 (the
    per-prime term ~ p^{t-2} is summable iff t-2 < -1).  NOTE: this is the main-term
    threshold of the JOINT residue-box decomposition -- STRICTLY past the diagonal
    Cauchy-Schwarz ceiling t < 1/2.  It is a convergent HEURISTIC main term, not a
    rigorous bound (see ``residue_box_correlation_obstruction``)."""
    tf = t if isinstance(t, Fraction) else Fraction(t)
    return tf < 1


def powerful_main_constant_truncated_enclosure(t, Pmax: int,
                                               precision: int = 10 ** 9
                                               ) -> Tuple[Fraction, Fraction]:
    """Certified [lo, hi] for the truncated main-term constant
        G_{<=Pmax}(t) = sum_{d powerful, d <= Pmax} ris(d)^t / d.
    Monotone increasing in Pmax; its limit G(t) is finite iff t < 1."""
    tf = t if isinstance(t, Fraction) else Fraction(t)
    num, den = tf.numerator, tf.denominator
    if num < 0:
        raise ABCClockError("t must be >= 0")
    lo = Fraction(0)
    hi = Fraction(0)
    for d in powerful_numbers_up_to(Pmax):
        rlo, rhi = power_enclosure(ris(d), num, den, precision)
        lo += rlo / d
        hi += rhi / d
    return lo, hi


@dataclass(frozen=True)
class BoundedPowerfulPartBound:
    """ABC-COR-02 certificate: a GENUINE X^2 upper bound, valid for EVERY t >= 0,
    on the bounded-powerful-part part of the correlation moment."""
    X: int
    Q: int
    t: Fraction
    G_Q: Tuple[Fraction, Fraction]        # sum ris(d)^t/d  over powerful d<=Q
    A_Q: Tuple[Fraction, Fraction]        # sum ris(d)^t
    B_Q: Tuple[Fraction, Fraction]        # sum ris(d)^t * d
    bound: Fraction                       # (X^2/2)G_Q^2 + 5X A_Q^2 + 5 B_Q^2 (upper)
    main_term: Fraction                   # (X^2/2) G_Q^2 (upper)
    error_part: Fraction                  # 5X A_Q^2 + 5 B_Q^2 (upper)
    dominance_threshold_X: int            # smallest X making main_term > error_part
    informative: bool                     # main_term > error_part at this X


def bounded_powerful_part_bound(X: int, Q: int, t) -> BoundedPowerfulPartBound:
    """ABC-COR-02 (PROVED LOCAL; genuine theorem with explicit constants, ALL t).

    Let J_t^{(Q)}(X) = sum over (a,b): a+b<=X, gcd(a,b)=1, powerful_part(a)<=Q,
    powerful_part(b)<=Q  of  ris(a)^t ris(b)^t.  Via the powerful-divisor majorant
    (``ris_powerful_majorant_terms``) and the Part IV residue-box count
    #{a+b<=X: d|a, d'|b} <= X^2/(2 d d') + 5(X + d d'):

        J_t^{(Q)}(X)  <=  (X^2/2) G_Q(t)^2  +  5 X A_Q(t)^2  +  5 B_Q(t)^2,

    with G_Q = sum_{d powerful<=Q} ris(d)^t/d, A_Q = sum ris(d)^t, B_Q = sum ris(d)^t d
    -- all FINITE for every t (Q fixed), so this is an X^2 bound with explicit
    constant G_Q(t)^2 for ALL t >= 0, including t >= 1/2.  The main term dominates
    the (residue-box) error once X exceeds 10 A_Q^2/G_Q^2 (B_Q part amortised),
    the direct inheritor of Part IV's X > 10 W boundary.  Returns the UPPER value of
    each enclosure so ``bound`` is a certified upper bound."""
    if type(X) is not int or X < 1 or type(Q) is not int or Q < 1:
        raise ABCClockError("bounded_powerful_part_bound needs integers X, Q >= 1")
    tf = t if isinstance(t, Fraction) else Fraction(t)
    num, den = tf.numerator, tf.denominator
    if num < 0:
        raise ABCClockError("t must be >= 0")
    g_lo = g_hi = Fraction(0)
    a_lo = a_hi = Fraction(0)
    b_lo = b_hi = Fraction(0)
    for d in powerful_numbers_up_to(Q):
        rlo, rhi = power_enclosure(ris(d), num, den, 10 ** 9)
        g_lo += rlo / d; g_hi += rhi / d
        a_lo += rlo;     a_hi += rhi
        b_lo += rlo * d; b_hi += rhi * d
    main = Fraction(X * X, 2) * g_hi * g_hi
    err = 5 * X * a_hi * a_hi + 5 * b_hi * b_hi
    # smallest X0 with (X0^2/2) g_hi^2 > 5 X0 a_hi^2 + 5 b_hi^2.  Use the asymptotic
    # binding term 5 X a_hi^2: X0 > 10 a_hi^2 / g_hi^2.
    if g_hi > 0:
        ratio = 10 * a_hi * a_hi / (g_hi * g_hi)
        thr = int(ratio) + 1
    else:
        thr = 0
    return BoundedPowerfulPartBound(
        X=X, Q=Q, t=tf, G_Q=(g_lo, g_hi), A_Q=(a_lo, a_hi), B_Q=(b_lo, b_hi),
        bound=main + err, main_term=main, error_part=err,
        dominance_threshold_X=thr, informative=main > err)


def bounded_powerful_part_census(X: int, Q: int, t) -> Fraction:
    """Exact J_t^{(Q)}(X) by direct enumeration (the quantity ABC-COR-02 bounds).
    Exact Fraction for integer t; a certified value otherwise is NOT returned here
    (use it with integer t as the test oracle)."""
    if type(X) is not int or X < 2 or type(Q) is not int or Q < 1:
        raise ABCClockError("bounded_powerful_part_census needs X>=2, Q>=1")
    tf = t if isinstance(t, Fraction) else Fraction(t)
    if tf.denominator != 1:
        raise ABCClockError("census oracle is exact only for integer t")
    k = tf.numerator
    total = Fraction(0)
    for c in range(2, X + 1):
        for a in range(1, c):
            b = c - a
            if gcd(a, b) == 1 and powerful_part(a) <= Q and powerful_part(b) <= Q:
                total += Fraction(ris(a) ** k * ris(b) ** k)
    return total


def coprimality_joint_occupation(p: int, X: int) -> Dict[str, object]:
    """Finding on how coprimality + a+b<=X restrict joint prime-power occupation.

    SAME prime p in both a and b (p|a AND p|b) is FORBIDDEN by gcd(a,b)=1 (it would
    give p | gcd), and under a+b=c also forces p | c.  DIFFERENT primes are NOT
    restricted by coprimality.  Returns the exact counts witnessing this: the
    coprime same-prime count is 0; a coprime different-prime count is positive."""
    if not prime(p) or type(X) is not int or X < 2:
        raise ABCClockError("coprimality_joint_occupation needs a prime p and X>=2")
    q = next(r for r in range(2, 100) if prime(r) and r != p)   # a different prime
    same = 0
    diff = 0
    for a in range(1, X):
        for b in range(1, X - a + 1):
            if gcd(a, b) == 1:
                if a % p == 0 and b % p == 0:
                    same += 1
                if a % p == 0 and b % q == 0:
                    diff += 1
    return {"p": p, "q_other": q, "X": X,
            "coprime_same_prime_count": same,          # must be 0
            "coprime_different_prime_count": diff,      # > 0
            "coprimality_kills_same_prime": same == 0,
            "coprimality_spares_different_prime": diff > 0}


def residue_box_correlation_obstruction() -> Dict[str, object]:
    """ABC-COR-03 (the quantified obstruction + the isolated missing estimate).

    What Part IV residue-box counting DID buy:
      * the exact JOINT main term: sum_{d,d' powerful} ris(d)^t ris(d')^t/(d d')
        * (X^2/2) = (X^2/2) G(t)^2, with G(t) finite iff t < 1 -- i.e. the correct
        main-term threshold is t < 1, STRICTLY past the diagonal t < 1/2.  The
        factor-2 gain is real: residue-box counts (a,b) JOINTLY (product of local
        densities) instead of Cauchy-Schwarz diagonalising to ris^{2t}.
    What it did NOT buy:
      * the residue-box error bound 5(X + d d') per pair, summed over the majorant,
        is >= c X^{t+2} (in fact ~ X^{t+3} from the B_Q = sum ris(d)^t d term),
        OVERWHELMING the X^2 main term for EVERY t >= 0.  So residue-box yields NO
        rigorous X^2 bound -- it does not even reprove the diagonal t < 1/2 result;
        it trades a better main term for a worse error.
      * residue-box is a NON-NEGATIVE count: it reproduces the main term exactly and
        provides ZERO cancellation below it.  The a+b=c constraint only COUPLES the
        residues by CRT (p^k|a forces b = c-a = c mod p^k: two independent
        congruences, density product, no saving); coprimality kills only the
        SAME-prime joint occupation, not the DIFFERENT-prime one that carries the
        moment.  The cancellation the problem needs is Fourier (sign-changing),
        structurally invisible to a positive lattice-point count.

    THE NEWLY-ISOLATED MISSING ESTIMATE (the Part V deliverable):
      a count  #{(a,b): a+b <= X, a == alpha, b == beta (mod q)}
        = (X^2 / 2q^2) * (#admissible classes)  +  o(X^2 / q),
      with a power/log SAVING, UNIFORM for moduli q up to q ~ X.  Residue-box gives
      only absolute error O(X + q) = O(1) RELATIVE at q ~ X (vacuous exactly at the
      large-powerful-part tail q ~ X^{1/2}..X that carries the t >= 1/2 difficulty).
      Supplying this saving is BBLT's Fourier 2nd/4th-moment exponential-sum bounds
      (Prop. 3.1) + Heath-Brown geometry-of-numbers integer-point counts (Prop. 4.1).
    """
    return {
        "claim": "ABC-COR-03",
        "residue_box_main_term_threshold": Fraction(1),   # G(t) finite iff t<1
        "diagonal_cauchy_schwarz_threshold": Fraction(1, 2),
        "main_term_beats_half": True,                     # t<1 > t<1/2
        "rigorous_bound_from_residue_box": False,         # error >> X^2 for all t>=0
        "error_growth_exponent_lower": "X^{t+2} (B_Q term ~ X^{t+3})",
        "residue_box_provides_cancellation": False,       # non-negative count
        "a_plus_b_eq_c_provides_cancellation": False,     # CRT coupling only
        "coprimality_kills_same_prime_only": True,
        "missing_estimate": ("power/log-saving integer-point count on a+b<=X in AP "
                             "of modulus q, uniform up to q ~ X (o(X^2/q) error)"),
        "missing_estimate_source": ("BBLT 2410.12234 Prop. 3.1 (Fourier 2nd/4th "
                                    "moment exp-sum) + Prop. 4.1 (Heath-Brown "
                                    "geometry-of-numbers)"),
        "abc_status": "OPEN",
        "t_half_moment_bound_status": "OPEN (main term reaches t<1; error uncontrolled)",
    }


def residue_box_error_growth_evidence(t: float = 1.0,
                                      Xs: Tuple[int, ...] = (50, 100, 200, 400)
                                      ) -> Tuple[Dict[str, float], ...]:
    """EVIDENCE (float, NOT a certificate) for ABC-COR-03: the full-majorant
    residue-box error bound 5X A_X^2 + 5 B_X^2 (summed over ALL powerful d <= X)
    divided by X^2 GROWS with X -- witnessing that the residue-box error overwhelms
    the X^2 main term, so the method gives no rigorous bound."""
    rows = []
    for X in Xs:
        A = 0.0
        B = 0.0
        for d in powerful_numbers_up_to(X):
            w = float(ris(d)) ** t
            A += w
            B += w * d
        err = 5 * X * A * A + 5 * B * B
        rows.append({"X": float(X), "t": t, "error_bound": err,
                     "error_over_X2": err / (X * X)})
    return tuple(rows)
