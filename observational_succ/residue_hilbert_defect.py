"""Exact finite models of the retained-vs-discarded Hilbert information.

For a source block of length M, prime multiplication V_p produces a state
supported on every p-th coordinate. Compared with the normalized uniform block
over the resulting pM sites, the exact diagnostics are:

    coarse-graining overlap        <h_{pM}, V_p u_M>      = p^{-1/2}
    full-vector norm difference    ||V_p u_M - h_{pM}||^2 = 2(1 - p^{-1/2})
    uniform-residue projection     |<h_{pM}, V_p u_M>|^2  = 1/p
    complementary residue sector   1 - 1/p

HDEF-01 keeps these five diagnostics DISTINCT (they must not be equated).
HDEF-02 builds the norm-preserving residue environment: the p orthonormal
        residue-sector states, with V_p u_M equal to the *terminal* residue
        sector h^{(p-1)} (consistent with V_p = U_{p,p-1}); the uniform-channel
        amplitude is p^{-1/2}, the projection probability 1/p, complementary
        1 - 1/p, and all p instrument outcomes sum to 1.
HDEF-03 Fourier-character controls: residue-sector overlaps with a character
        state all have magnitude p^{-1/2} but phases omega^{kr}. The magnitude
        is BLIND to the residue; a single character k DETERMINES the residue
        ONLY when gcd(k,p)=1 (for prime p, any k not divisible by p). For a
        non-coprime (k,p) -- e.g. (p,k)=(4,2), overlaps (1/2,-1/2,1/2,-1/2) --
        distinct residues share a phase, so that character does NOT recover the
        residue. Correctly scoped, this is the Hilbert/Fourier shadow of
        FSO-01's "residue is necessary": recovery needs a coprime character (or
        the full character set).
HDEF-04 prime-power factor p^{-r/2}, combined with [log N, V_p]=(log p)V_p to
        reconstruct log p / p^{r/2} = Lambda(p^r)/sqrt(p^r).

CRITICAL FIREWALL: HDEF-04 is the von-Mangoldt building block of the explicit
formula, NOT the completed signed Weil distribution (no Gamma factor, no pole,
no archimedean completion, no sign). A positive overlap magnitude CANNOT
authenticate primality: a composite multiplier m gives the same-form m^{-1/2}.
No Weil/RH positivity is inferred anywhere.

Exact algebraic arithmetic via sympy for the sqrt and cyclotomic quantities;
the purely rational diagnostics use Fraction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

import sympy as sp

from observational_succ.arithmetic_interactions import von_mangoldt


class HilbertDefectError(ValueError):
    """Wrong block length, modulus, residue, or a violated normalization."""


def _modulus(p):
    if type(p) is not int or p < 2:
        raise HilbertDefectError("modulus p >= 2 required")
    return p


def _block(M):
    if type(M) is not int or M < 1:
        raise HilbertDefectError("block length M >= 1 required")
    return M


def _rational_of(expr):
    """Collapse an exact sympy expression to a Fraction (raises if irrational)."""
    r = sp.nsimplify(sp.simplify(expr))
    if not r.is_Rational:
        raise HilbertDefectError(f"expected a rational value, got {r}")
    return Q(int(r.p), int(r.q))


# ---------------------------------------------------------------------------
# exact vectors (coefficients are sympy expressions; sqrt kept symbolic)
# ---------------------------------------------------------------------------

def uniform_block(M):
    """u_M = (1/sqrt(M)) sum_{n=1..M} |n>."""
    _block(M)
    c = 1 / sp.sqrt(M)
    return {n: c for n in range(1, M + 1)}


def dilate(vec, p):
    """V_p |n> = |p n>; applied coordinate-wise to an exact vector."""
    _modulus(p)
    return {p * n: c for n, c in vec.items()}


def uniform_target(N):
    """h_N = (1/sqrt(N)) sum_{j=1..N} |j>."""
    if type(N) is not int or N < 1:
        raise HilbertDefectError("target size N >= 1 required")
    c = 1 / sp.sqrt(N)
    return {j: c for j in range(1, N + 1)}


def inner(v, w):
    """<v, w> = sum_i conj(v_i) w_i, exact (sympy)."""
    keys = set(v) & set(w)
    return sp.simplify(sp.Add(*[sp.conjugate(v[i]) * w[i] for i in keys]) if keys else sp.Integer(0))


def norm_sq(v):
    return inner(v, v)


# ---------------------------------------------------------------------------
# HDEF-01 : the five distinct diagnostics
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Diagnostics:
    coarse_overlap: object          # p^{-1/2}
    norm_diff_sq: object            # 2(1 - p^{-1/2})
    projection_prob: Q              # 1/p
    complementary: Q                # 1 - 1/p
    all_distinct: bool


def diagnostics(M, p):
    """Compute the five HDEF-01 quantities exactly from the explicit vectors."""
    _block(M)
    _modulus(p)
    u = uniform_block(M)
    Vu = dilate(u, p)
    h = uniform_target(p * M)
    overlap = inner(h, Vu)
    diff = {i: Vu.get(i, 0) - h.get(i, 0) for i in set(Vu) | set(h)}
    nds = norm_sq(diff)
    # Born relation, DERIVED from the computed overlap (not hardcoded): the
    # projection probability is |<h,Vu>|^2 and the complementary is 1 - that.
    proj = _rational_of(sp.Abs(overlap) ** 2)
    comp = 1 - proj
    # distinctness: overlap (p^{-1/2}), nds (2-2p^{-1/2}), proj (1/p) are three
    # different values for p >= 2
    distinct = len({sp.nsimplify(overlap), sp.nsimplify(nds), sp.nsimplify(sp.Rational(proj))}) == 3
    return Diagnostics(overlap, nds, proj, comp, distinct)


def closed_forms(p):
    """The claimed closed forms, as exact sympy / Fraction values."""
    _modulus(p)
    return {
        "coarse_overlap": 1 / sp.sqrt(p),
        "norm_diff_sq": 2 * (1 - 1 / sp.sqrt(p)),
        "projection_prob": Q(1, p),
        "complementary": 1 - Q(1, p),
    }


# ---------------------------------------------------------------------------
# HDEF-02 : norm-preserving residue environment
# ---------------------------------------------------------------------------

def residue_sector(M, p, r):
    """Normalized uniform over the one-based residue-r sector of {1..pM}.

    Sites j = p(n-1)+r+1, n=1..M. The terminal sector r=p-1 is exactly V_p u_M.
    """
    _block(M)
    _modulus(p)
    if type(r) is not int or not 0 <= r < p:
        raise HilbertDefectError("residue r in [0,p) required")
    c = 1 / sp.sqrt(M)
    return {p * (n - 1) + r + 1: c for n in range(1, M + 1)}


def residue_environment(M, p):
    """The p orthonormal residue-sector states {h^{(0)},...,h^{(p-1)}}."""
    return [residue_sector(M, p, r) for r in range(p)]


@dataclass(frozen=True)
class EnvironmentCertificate:
    orthonormal: bool
    vp_is_terminal_sector: bool      # V_p u_M == h^{(p-1)}
    uniform_decomposition: bool      # h = (1/sqrt p) sum_r h^{(r)}
    uniform_channel_amplitude: object  # p^{-1/2}
    outcome_probs: tuple             # p copies of 1/p
    outcomes_sum_to_one: bool


def environment_certificate(M, p):
    """Certify the norm-preserving residue decomposition and the instrument law."""
    _block(M)
    _modulus(p)
    sectors = residue_environment(M, p)
    # orthonormality
    orthonormal = all(
        sp.simplify(inner(sectors[a], sectors[b]) - (1 if a == b else 0)) == 0
        for a in range(p) for b in range(p))
    # V_p u_M == terminal sector
    Vu = dilate(uniform_block(M), p)
    vp_terminal = all(sp.simplify(Vu.get(i, 0) - sectors[p - 1].get(i, 0)) == 0
                      for i in set(Vu) | set(sectors[p - 1]))
    # h = (1/sqrt p) sum_r h^{(r)}
    h = uniform_target(p * M)
    recon = {}
    for sec in sectors:
        for i, c in sec.items():
            recon[i] = recon.get(i, 0) + c / sp.sqrt(p)
    uniform_decomp = all(sp.simplify(h.get(i, 0) - recon.get(i, 0)) == 0
                         for i in set(h) | set(recon))
    amp = inner(h, sectors[p - 1])            # uniform-channel amplitude
    # Born probabilities DERIVED from the real amplitudes |<h, h^{(r)}>|^2, not
    # hardcoded: "sum to 1" then tests the sector physics, not the constructor.
    probs = tuple(_rational_of(sp.Abs(inner(h, sectors[r])) ** 2) for r in range(p))
    return EnvironmentCertificate(
        orthonormal, vp_terminal, uniform_decomp, sp.simplify(amp),
        probs, sum(probs) == 1)


# ---------------------------------------------------------------------------
# HDEF-03 : Fourier-character controls (magnitude blind, phase informative)
# ---------------------------------------------------------------------------

def character_sector_overlap(p, k, r):
    """<h^{(r)}, g_k> for the character state g_k = (1/sqrt p) sum_r' omega^{k r'} h^{(r')}.

    Equals (1/sqrt p) omega^{k r}, omega = exp(2 pi i / p). Magnitude p^{-1/2}
    for every r; the phase omega^{k r} encodes the residue.
    """
    _modulus(p)
    if type(k) is not int or type(r) is not int:
        raise HilbertDefectError("integer character index k and residue r required")
    omega = sp.exp(2 * sp.pi * sp.I * sp.Rational((k * r) % p, p))
    return sp.simplify(omega / sp.sqrt(p))


def magnitude_blind_phase_informative(p, k):
    """Overlaps with all p sectors share magnitude p^{-1/2}; phases are DISTINCT

    iff gcd(k,p)=1 (for prime p, any k with p does-not-divide k). Only then is
    the residue recoverable from a single character's phase. For a non-coprime
    (k,p) the map r -> omega^{kr} is not injective and distinct residues share a
    phase (e.g. (p,k)=(4,2) gives phases 1,-1,1,-1). Returns
    (magnitudes_all_equal, phases_all_distinct); distinctness is decided by
    pairwise exact simplification (not set identity, which is unsafe for
    non-canonical sympy forms), so the function returns the honest False in the
    non-coprime region.
    """
    _modulus(p)
    overlaps = [character_sector_overlap(p, k, r) for r in range(p)]
    mags = [sp.simplify(sp.Abs(o)) for o in overlaps]
    phases = [sp.simplify(o / sp.Abs(o)) for o in overlaps]
    mags_equal = all(sp.simplify(m - mags[0]) == 0 for m in mags)
    phases_distinct = all(
        sp.simplify(phases[i] - phases[j]) != 0
        for i in range(p) for j in range(i + 1, p))
    return mags_equal, phases_distinct


def _complex_is_zero(expr):
    """Exact test that a sympy complex expression is zero (rectangular form)."""
    z = sp.expand_complex(expr)
    return sp.simplify(sp.re(z)) == 0 and sp.simplify(sp.im(z)) == 0


def orientation_reversal_conjugates(p, k, r):
    """k -> -k conjugates the phase (opposite character convention)."""
    _modulus(p)
    forward = character_sector_overlap(p, k, r)
    reversed_ = character_sector_overlap(p, -k, r)
    return _complex_is_zero(reversed_ - sp.conjugate(forward))


# ---------------------------------------------------------------------------
# HDEF-04 : prime-power factor and the von-Mangoldt reconstruction
# ---------------------------------------------------------------------------

def prime_power_overlap(M, p, r):
    """<h_{p^r M}, V_{p^r} u_M> = p^{-r/2} (dilate the block by q = p^r)."""
    _block(M)
    _modulus(p)
    if type(r) is not int or r < 1:
        raise HilbertDefectError("prime-power exponent r >= 1 required")
    q = p ** r
    return inner(uniform_target(q * M), dilate(uniform_block(M), q))


def log_commutator_eigenvalue(p, n):
    """[log N, V_p] |n> = (log(p n) - log n) |p n> = (log p) |p n>. Returns log p."""
    _modulus(p)
    if type(n) is not int or n < 1:
        raise HilbertDefectError("basis index n >= 1 required")
    return sp.simplify(sp.log(p * n) - sp.log(n))


def von_mangoldt_reconstruction(p, r):
    """Reconstruct the explicit-formula coefficient log p / p^{r/2}.

    Returns (overlap_route, von_mangoldt_route) which are exactly equal:
    (log p) * p^{-r/2}  ==  Lambda(p^r) / sqrt(p^r).
    """
    _modulus(p)
    if type(r) is not int or r < 1:
        raise HilbertDefectError("prime-power exponent r >= 1 required")
    overlap_route = sp.log(p) * p ** sp.Rational(-r, 2)
    vm = von_mangoldt(p ** r)                       # = log p for a prime power
    vm_route = vm / sp.sqrt(p ** r)
    return sp.simplify(overlap_route), sp.simplify(vm_route)


def magnitude_cannot_authenticate_primality(M, prime_p, composite_m):
    """A composite multiplier gives the same-form overlap m^{-1/2} as a prime.

    Returns (prime_overlap, composite_overlap); both are positive 1/sqrt(.) of
    identical form, so the magnitude alone does not distinguish prime from
    composite. The composite must be a genuine composite >= 2.
    """
    _block(M)
    _modulus(prime_p)
    if type(composite_m) is not int or composite_m < 2:
        raise HilbertDefectError("composite multiplier >= 2 required")
    po = inner(uniform_target(prime_p * M), dilate(uniform_block(M), prime_p))
    co = inner(uniform_target(composite_m * M), dilate(uniform_block(M), composite_m))
    return sp.simplify(po), sp.simplify(co)


def weil_firewall():
    """The explicit disclaimer: this is NOT the completed signed Weil distribution."""
    return {
        "is": "von-Mangoldt building block log p / p^{r/2} of the explicit formula",
        "is_not": "the completed signed Weil distribution",
        "missing": ("Gamma factor", "pole term", "archimedean completion",
                    "overall sign / signed positivity"),
        "primality": "overlap magnitude cannot authenticate primality "
                     "(a composite m gives the same-form m^{-1/2})",
        "RH_PROVED": "NO",
    }
