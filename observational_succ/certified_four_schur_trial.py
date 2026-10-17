"""CertifiedTrial(U, J, precision): rigorous two-sided Loewner enclosure of the
ORIGINAL four-mode Suzuki/Weil Schur complement S_4 = A_4 - R_4 at a = 1/2.

This module does NOT reconstruct zeta, Gamma, the Euler product or the completed
signed Weil distribution -- those are inherited, source-authenticated, exact
interval primitives (observational_succ.suzuki_legendre_source.authentic_full_low_entry
and observational_succ.source_weil_hierarchy). It determines, as far as the
mathematics honestly allows, the SIGN of an already-constructed source operator.

Decomposition (original Suzuki derivative carrier u in L^2_0(-1/2,1/2)):
    H = F_4 (+) H_high,   F_4 = span{P_1(2t),...,P_4(2t)},
    G = [[A_4, B^*], [B, D_4]]   (authentic completed signed Suzuki operator),
    K = (-Delta_N)^{-1} = V^* V   (inverse Neumann on mean-zero u; K^{-1}=-Delta_N),
    R_4(x) = sup_{z in H_high} ( 2 Re <Bx,z> - <D_4 z,z> ),
    S_4 = A_4 - R_4.

Inherited, independently audited source facts (reproduced, not assumed, by the
accompanying probe/tests): A_4 > 0, and D_4 >= (1/50) Q_4 K Q_4 with
kappa = 1/50 (WB4, tate_weighted_bessel_four_schur). The L^1 derivative budget
||g'||_1 < 11/40 (one_object_residual_schur) gives the zero-shift cap R_4 <=
(11/40)^2 / kappa = 121/32 on the L^2 metric.

The RESIDUAL THEOREM (independently re-derived in the dossier) gives, for ANY
finite rational parity-respecting high response U : F_4 -> H_high, with
r_U = B - D_4 U, L_U = U^*B + B^*U - U^*D_4U, and T_{r_U} the derivative Gram
of the residual high response (T_{r_U}(x) = ||(r_U x)'||^2 = <r_U x, K^{-1} r_U x>):

    A_4 - L_U - (1/kappa) T_{r_U}  <=_Loewner  S_4  <=_Loewner  A_4 - L_U.

* The UPPER bracket A_4 - L_U = <Vx, G Vx> (Vx = x - Ux) is CERTIFIED exactly:
  an interval Gram of the trial vectors under the authentic G_J, plus the proven
  PSD Gamma-tail Loewner cap (authentic_positive_gamma_tail_norm).
* The LOWER bracket is CERTIFIED with the rigorous Young/L^1 bound
  T_{r_U} <= (11/40)^2 W_L2(V) (so (1/kappa)T_{r_U} <= 121/32 W_L2(V)). This is
  U-blind -- it recovers exactly the inherited 121/32 zero-shift cap at U = 0.
  A TIGHTER lower bracket needs a certified upper bound on the derivative Gram of
  the true infinite high response (the open Section 3C modulus); the finite-mode
  derivative Gram is provided as an explicitly NON-CERTIFIED diagnostic.

No nontrivial zeta-zero location is a construction input. a = 1/2 fixed; the only
active prime atom (p=2) is VERIFIED from the authentic support law, never a
hard-coded cutoff. RH PROVED: NO. A certified positive S_4 would be a first-window
theorem, not RH. A certified negative direction would be extraordinary and is
reported with its exact rational witness for hostile independent verification.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache

from .suzuki_moment_schur import (
    SchurSourceError, positive_definite, parity_blocks, symmetric,
    inverse_neumann_entry,
)
from .suzuki_legendre_source import authentic_full_low_entry
from .source_weil_hierarchy import authentic_positive_gamma_tail_norm, authenticated_prime_wavefront
from .tate_suzuki_shorting import verify_original_suzuki_source
from .one_object_residual_schur import original_source_cancellation_certificate
from .four_schur_dual_quotient import quotient_derivative_cap

A_RADIUS = F(1, 2)
KAPPA = F(1, 50)
GPRIME_L1_UPPER = F(11, 40)           # ||g'||_1 strict upper (one_object_residual_schur)
ZERO_SHIFT_CAP = GPRIME_L1_UPPER ** 2 / KAPPA   # 121/32, the Young residual cap


class CertifiedTrialError(ValueError):
    """Invalid source/domain/normalization/provenance or ill-typed trial."""


def _q(x):
    if type(x) not in (int, F):
        raise CertifiedTrialError("exact int/Fraction required; a float is not a proof")
    return F(x)


@lru_cache(maxsize=64)
def _g_block(rank, J):
    """Cached exact interval source block G_J on Legendre modes 1..rank at a=1/2.

    Each entry is authentic_full_low_entry(i,j,1/2,J): prime-2 hinge, both poles,
    contact and the first J true positive Gamma OU modes. The omitted Gamma rungs
    are PSD, so this is a Loewner LOWER bound on the full signed source block.
    Cached because a single (rank,J) feeds an entire trial sweep.
    """
    return tuple(tuple(authentic_full_low_entry(i, j, A_RADIUS, J)
                       for j in range(1, rank + 1))
                 for i in range(1, rank + 1))


def _rational_matrix(M, rows, cols):
    if len(M) != rows or any(len(r) != cols for r in M):
        raise CertifiedTrialError(f"expected a {rows}x{cols} exact rational matrix")
    return tuple(tuple(_q(x) for x in r) for r in M)


def legendre_L2_norm2(mode):
    """<P_m(2t),P_m(2t)>_{L^2(-1/2,1/2)} = 1/(2m+1); modes are 1-indexed."""
    m = int(mode)
    if m < 1:
        raise CertifiedTrialError("Legendre mode index >= 1")
    return F(1, 2 * m + 1)


def _trial_matrix_V(U, rank):
    """V (rank x 4), columns V e_i = e_i - U e_i; rows = Legendre modes 1..rank."""
    high = rank - 4
    V = []
    for m in range(rank):               # row index 0.. -> mode m+1
        if m < 4:
            V.append(tuple(F(m == j) for j in range(4)))
        else:
            V.append(tuple(-U[m - 4][j] for j in range(4)))
    return tuple(V)


def _parity_ok(U, rank):
    """U respects reflection parity: entry (high mode h, low mode l) vanishes
    unless h and l have the same parity (h-l even)."""
    for i in range(rank - 4):
        h = i + 5                       # high modes start at 5
        for j in range(4):
            l = j + 1                   # low modes 1..4
            if (h - l) % 2 and U[i][j] != 0:
                return False
    return True


def _interval_gram_under_GJ(V, Gblk, rank):
    """Interval 4x4 Gram MG[i][j] = <v_i, G_J v_j> = sum_{a,b} V[a][i]V[b][j]G[a][b].

    Returned as (mid, rad): rational symmetric midpoint matrix and rational
    radius matrix, with  mid - rad <=entrywise <v_i,G_J v_j> <=entrywise mid + rad.
    """
    from .source_weil_hierarchy import iv
    mid = [[F(0)] * 4 for _ in range(4)]
    rad = [[F(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = iv(0)
            for a in range(rank):
                vai = V[a][i]
                if not vai:
                    continue
                for b in range(rank):
                    vbj = V[b][j]
                    if not vbj:
                        continue
                    acc += (vai * vbj) * Gblk[a][b]
            mid[i][j] = (acc.lo + acc.hi) / 2
            rad[i][j] = (acc.hi - acc.lo) / 2
    return (tuple(tuple(r) for r in mid), tuple(tuple(r) for r in rad))


def _loewner_radius(rad):
    """Certified scalar r with (interval radius matrix) <=_Loewner r I.

    For a symmetric nonnegative radius matrix the spectral radius is bounded by
    the max absolute row sum (Gershgorin / induced l-infinity norm)."""
    return max((sum(abs(x) for x in row) for row in rad), default=F(0))


def _L2_gram_of_trial(V, rank):
    """Exact rational W_L2(V)[i][j] = <v_i, v_j>_{L^2} = sum_m V[m][i]V[m][j]/(2(m+1)+1)."""
    W = [[F(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            W[i][j] = sum((V[m][i] * V[m][j] * legendre_L2_norm2(m + 1)
                           for m in range(rank)), F(0))
    return tuple(tuple(r) for r in W)


def _mat_sub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(len(A[0]))) for i in range(len(A)))


def _mat_add(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0]))) for i in range(len(A)))


def _scalar_shift(A, s):
    return tuple(tuple(A[i][j] - (s if i == j else F(0)) for j in range(len(A[0])))
                 for i in range(len(A)))


def _scale(A, c):
    return tuple(tuple(c * A[i][j] for j in range(len(A[0]))) for i in range(len(A)))


def min_eig_lower(M, depth=48):
    """Certified strict rational lower bound L on lambda_min(M): M - L I is PD.

    Exact LDL bisection. Gershgorin bounds all eigenvalues into [-B, B]."""
    if not symmetric(M):
        raise CertifiedTrialError("min eigenvalue enclosure needs a symmetric matrix")
    B = max((sum(abs(x) for x in row) for row in M), default=F(0))
    lo, hi = -B - 1, B + 1
    # M - lo I is PD (lo < lambda_min); M - hi I is not. Bisect for sup PD shift.
    for _ in range(int(depth)):
        mid = (lo + hi) / 2
        if positive_definite(_scalar_shift(M, mid)):
            lo = mid
        else:
            hi = mid
    return lo


def max_eig_upper(M, depth=48):
    """Certified strict rational upper bound on lambda_max(M): -min_eig_lower(-M)."""
    neg = tuple(tuple(-x for x in row) for row in M)
    return -min_eig_lower(neg, depth)


def _block_is_psd(M):
    """Exact PSD test (lambda_min >= 0) for a symmetric rational parity block.

    The four-mode parity blocks are 2x2, where PSD <=> det >= 0 and trace >= 0
    (both eigenvalues nonnegative). A 1x1 block is PSD <=> its entry >= 0. We use
    this (not strict LDL) for the NEGATIVE verdict so that a PSD-but-singular
    bracket (a null direction, <v,S_4 v> <= 0 but not < 0) is NOT mislabelled
    NEGATIVE_CERTIFIED: NEGATIVE requires a genuine strictly-negative direction."""
    n = len(M)
    if n == 1:
        return M[0][0] >= 0
    if n == 2:
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return det >= 0 and (M[0][0] + M[1][1]) >= 0
    raise CertifiedTrialError("PSD block test expects <=2x2 parity blocks")


def _parity_block_min_eig(M, depth=48):
    """(odd_min_lower, even_min_lower, overall_lower) using exact parity blocks."""
    pb = parity_blocks(M, 4)
    vals = {}
    overall = None
    for label in ("odd", "even"):
        block = pb[label]
        if block:
            v = min_eig_lower(block, depth)
            vals[label] = v
            overall = v if overall is None else min(overall, v)
    return vals, overall


def _finite_mode_residual_gram_diagnostic(V, Gblk, rank):
    """NON-CERTIFIED finite-mode derivative Gram of the residual high response.

    T_{r_U}(x) = ||(Q_high G Vx)'||^2 = sum_{k,l>=5} c_k c_l <P_k',P_l'>, with
    c_k = <P_k, G Vx>/<P_k,P_k> the (exact-interval) high Legendre coefficients.
    This truncates the sum at mode `rank`; the omitted tail (k>rank) is the OPEN
    Section 3C modulus and is NOT bounded here. Returned for diagnosis only:
    it indicates how much a certified tail lemma could tighten the lower bracket,
    i.e. whether the binding constraint is the conservative Young residual or the
    genuine arithmetic coupling. It is NOT a certificate and must never gate a
    sign verdict.
    """
    # Legendre derivative Gram D[k][l] = <d/dt P_k(2t), d/dt P_l(2t)>_{L^2(-1/2,1/2)}.
    # Exact rational: with x=2t, P'_k(2t)*2, integral over t in (-1/2,1/2).
    def legendre_deriv_gram(kmax):
        # Build derivative polynomials of P_m(2t) and integrate pairwise, exactly.
        from .suzuki_legendre_source import (legendre_polynomial, poly_derivative,
                                             poly_mul, poly_integral)
        polys = {m: legendre_polynomial(m, A_RADIUS) for m in range(1, kmax + 1)}
        ders = {m: poly_derivative(polys[m]) for m in range(1, kmax + 1)}
        D = {}
        for k in range(1, kmax + 1):
            for l in range(1, kmax + 1):
                D[(k, l)] = poly_integral(poly_mul(ders[k], ders[l]),
                                          -A_RADIUS, A_RADIUS)
        return D
    from .source_weil_hierarchy import iv
    D = legendre_deriv_gram(rank)
    # high Legendre coefficient of G Vx at mode k: c_k = <P_k,GVx>/<P_k,P_k>
    #   = (2k+1) * sum_a V[a][i] Gblk[k-1][a]   (exact interval)
    def high_coeff(col, k):
        acc = iv(0)
        for a in range(rank):
            if V[a][col]:
                acc += V[a][col] * Gblk[k - 1][a]
        return acc * (2 * k + 1)
    out = [[F(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc_lo = acc_hi = F(0)
            for k in range(5, rank + 1):
                ck = high_coeff(i, k)
                for l in range(5, rank + 1):
                    term = ck * high_coeff(j, l) * D[(k, l)]
                    acc_lo += term.lo
                    acc_hi += term.hi
            out[i][j] = (acc_lo + acc_hi) / 2
    return tuple(tuple(r) for r in out)


def CertifiedTrial(U, J=64, precision=F(1, 1000), rank=None, diagnostic=False):
    """Rigorous two-sided Loewner enclosure of S_4 for a finite rational trial U.

    Parameters
    ----------
    U : sequence of (rank-4) rows x 4 columns of exact int/Fraction.
        The high response F_4 -> span{P_5(2t),...,P_rank(2t)}; parity-respecting
        (entry (high h, low l) must vanish unless h-l is even). U = () or a
        zero matrix is the trivial trial and recovers the inherited 121/32 cap.
    J : int in [1,75]. Number of authentic Gamma (Archimedean) OU modes retained;
        the omitted rungs are PSD and capped by authentic_positive_gamma_tail_norm.
    precision : Fraction. Requested certified half-width target for the enclosure
        (a reporting gate; the actual certified widths are always returned).
    rank : int in [5,12] or None. Highest Legendre mode used; inferred from U if None.
    diagnostic : include the NON-CERTIFIED finite-mode residual derivative Gram.

    Returns a dict. Verdict in {POSITIVE_CERTIFIED, NEGATIVE_CERTIFIED, AMBIGUOUS,
    INVALID_SOURCE}. Every returned bound is an exact rational Loewner bound.
    """
    # ---- source / domain / normalization / provenance contract (fail closed) ----
    try:
        verify_original_suzuki_source()
        # The ONLY active autocorrelation atom at a=1/2 must be the genuine prime-2
        # power place -- verified from the authentic support law (2a=1 > log2 but
        # < log3), never a hard-coded prime cutoff.
        wavefront = authenticated_prime_wavefront(A_RADIUS)
        if wavefront != ((2, 2),):
            raise CertifiedTrialError(
                f"non-authentic prime wavefront at a=1/2: {wavefront}")
        cancel = original_source_cancellation_certificate()
        if cancel['gprime_L1_STRICT_upper'] >= GPRIME_L1_UPPER:
            raise CertifiedTrialError("inherited ||g'||_1 budget drifted above 11/40")
    except (SchurSourceError, CertifiedTrialError) as exc:
        return {"verdict": "INVALID_SOURCE", "reason": str(exc),
                "a": str(A_RADIUS), "RH_proved": False}

    if type(J) is not int or not 1 <= J <= 75:
        return {"verdict": "INVALID_SOURCE", "reason": "J out of [1,75]",
                "RH_proved": False}
    try:
        requested_precision = _q(precision)
        if requested_precision <= 0:
            raise CertifiedTrialError("precision must be strictly positive")
    except CertifiedTrialError as exc:
        return {"verdict": "INVALID_SOURCE", "reason": str(exc), "RH_proved": False}

    # normalize U and rank
    U = tuple(tuple(r) for r in U) if U else ()
    if rank is None:
        rank = 4 + len(U)
    if type(rank) is not int or not 5 <= rank <= 12:
        return {"verdict": "INVALID_SOURCE", "reason": "rank out of [5,12]",
                "RH_proved": False}
    if not U:
        U = tuple(tuple(F(0) for _ in range(4)) for _ in range(rank - 4))
    U = _rational_matrix(U, rank - 4, 4)
    if not _parity_ok(U, rank):
        return {"verdict": "INVALID_SOURCE",
                "reason": "high response U mixes reflection parities",
                "RH_proved": False}

    # ---- exact interval source block G_J on modes 1..rank ----
    from .source_weil_hierarchy import iv
    Gblk = _g_block(rank, J)
    # parity + symmetry sanity (the primitive already checks, this is defense in depth)
    for i in range(rank):
        for j in range(rank):
            if (i - j) % 2 and (Gblk[i][j].lo or Gblk[i][j].hi):
                return {"verdict": "INVALID_SOURCE",
                        "reason": "source parity violation in G block",
                        "RH_proved": False}

    V = _trial_matrix_V(U, rank)
    mid, rad = _interval_gram_under_GJ(V, Gblk, rank)
    r = _loewner_radius(rad)
    tail_J = authentic_positive_gamma_tail_norm(J)
    W_L2 = _L2_gram_of_trial(V, rank)

    # A_4 interval (for reporting): modes 1..4 block
    A4_mid = tuple(tuple((Gblk[i][j].lo + Gblk[i][j].hi) / 2 for j in range(4))
                   for i in range(4))
    A4_rad = _loewner_radius(tuple(tuple((Gblk[i][j].hi - Gblk[i][j].lo) / 2
                                         for j in range(4)) for i in range(4)))
    # rigorous: A_4 >= (A4_mid - A4_rad I), so certified min eig >= min_eig(mid) - rad
    A4_lower = _parity_block_min_eig(A4_mid)[1] - A4_rad

    # ---- CERTIFIED Loewner brackets (rational symmetric 4x4, parity-block) ----
    # <v,G v> form: mid +/- r I  (G_J interval), plus PSD tail in [0, tail_J W_L2].
    # UPPER bracket (U-dependent, rigorous for every trial U):
    #   S_4 <= A_4 - L_U = <Vx, G Vx> <= (mid + r I) + tail_J W_L2(V).
    upper_bracket = _mat_add(_scalar_shift(mid, -r), _scale(W_L2, tail_J))  # (mid + r I) + tail_J W_L2
    # LOWER bracket (U-INDEPENDENT, rigorous): uses the INHERITED WB4 zero-shift
    #   bound R_4 <= (11/40)^2/kappa * W_L2(low) = (121/32) W_L2(low), so
    #   S_4 = A_4 - R_4 >= (A_4 interval lower) - (121/32) W_L2(low).
    # The per-U residual-theorem tightening A_4 - L_U - (1/kappa) T_{r_U} would be
    # sharper, but a CERTIFIED upper bound on the true infinite residual Gram T_{r_U}
    # needs the open Section 3C decay modulus (the generalized Young bound
    # ||(Q_high G Vx)'|| <= ||(G Vx)'|| is FALSE in general -- an L^2 projection can
    # raise the derivative norm), so it is emitted ONLY as a NON-CERTIFIED diagnostic.
    W_L2_low = tuple(tuple(legendre_L2_norm2(i + 1) if i == j else F(0)
                           for j in range(4)) for i in range(4))
    A4_lower_loewner = _scalar_shift(A4_mid, A4_rad)                        # A_4 >= A4_mid - A4_rad I
    lower_bracket = _mat_sub(A4_lower_loewner, _scale(W_L2_low, ZERO_SHIFT_CAP))

    # NEW: proof-bearing U-dependent alternative. For v=x-Ux and any high w,
    #   <QGv,w>=<Gv,w>=-<(Gv)', Vw>,
    # where Vw is the primitive and K=V*V. The ORIGINAL anchored source has
    #   ||(Gv)'||_2 <= ||g'||_1 ||v||_2 < (11/40)||v||_2.
    # Combining with D >= (1/50)QKQ yields the valid variational correction
    # (121/32) ||v||_2^2 without the FALSE H1 contraction of Q.
    # M(v) >= mid-rI because omitted authentic Gamma modes are PSD.
    # This new LOWER is rigorous for every U but can be WEAKER than the old
    # U=0 floor; preserve both, never form an unjustified matrix maximum.
    source_dual_correction = quotient_derivative_cap(
        W_L2, gprime_L1=GPRIME_L1_UPPER, kappa=KAPPA
    )["residual_correction_upper"]
    source_dual_U_lower = _mat_sub(_scalar_shift(mid, r),
                                  source_dual_correction)

    # Requested precision is a measurable source-trial-energy width target,
    # not a promise of arbitrary-precision Schur sign. It now affects a
    # verifiable acceptance flag. J/rank are bounded; unmet targets stay unmet.
    w_maxrowsum = max(sum(abs(x) for x in row) for row in W_L2)
    source_trial_energy_width = 2*r + tail_J*w_maxrowsum
    requested_precision_met = source_trial_energy_width <= requested_precision
    lower_short = _scalar_shift(mid, r)   # (A_4 - L_U) lower, for the per-U diagnostic only

    # enforce exact symmetry (round-off impossible with Fractions, but assert intent)
    for M, name in ((upper_bracket, "upper"), (lower_bracket, "lower")):
        if not symmetric(M):
            return {"verdict": "INVALID_SOURCE",
                    "reason": f"{name} bracket lost symmetry", "RH_proved": False}

    up_pb = parity_blocks(upper_bracket, 4)
    lo_pb = parity_blocks(lower_bracket, 4)
    # POSITIVE gate: lower_bracket strictly PD (exact LDL) on both parity blocks.
    lower_is_pd = positive_definite(lo_pb['odd']) and positive_definite(lo_pb['even'])
    dual_pb = parity_blocks(source_dual_U_lower, 4)
    dual_lower_is_pd = (positive_definite(dual_pb['odd'])
                        and positive_definite(dual_pb['even']))
    # NEGATIVE gate: upper_bracket genuinely NOT PSD (a strictly-negative direction),
    # tested exactly on the 2x2 parity blocks -- a PSD-singular upper stays AMBIGUOUS.
    upper_is_psd = _block_is_psd(up_pb['odd']) and _block_is_psd(up_pb['even'])
    upper_has_strict_negative_direction = not upper_is_psd

    up_eig, up_min = _parity_block_min_eig(upper_bracket)
    lo_eig, lo_min = _parity_block_min_eig(lower_bracket)
    up_max = max_eig_upper(up_pb['odd']), max_eig_upper(up_pb['even'])

    # ---- verdict ----
    if lower_is_pd or dual_lower_is_pd:
        verdict = "POSITIVE_CERTIFIED"            # S_4 >= lower_bracket > 0
    elif upper_has_strict_negative_direction:
        # S_4 <= upper_bracket, which has a strictly negative direction -> S_4 not PSD
        verdict = "NEGATIVE_CERTIFIED"
    else:
        verdict = "AMBIGUOUS"

    result = {
        "verdict": verdict,
        "source": "AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3",
        "a": str(A_RADIUS), "kappa": str(KAPPA), "gamma_modes_J": J, "rank": rank,
        "requested_precision": str(requested_precision),
        "requested_precision_met_for_trial_energy": requested_precision_met,
        "source_trial_energy_width_operator_upper": str(source_trial_energy_width),
        "source_trial_energy_midpoint": tuple(tuple(str(x) for x in row) for row in mid),
        "U": tuple(tuple(str(x) for x in row) for row in U),
        "U_is_zero": all(x == 0 for row in U for x in row),
        "gamma_positive_tail_norm_upper": str(tail_J),
        "young_zero_shift_cap_1_over_kappa_times_gprimeL1sq": str(ZERO_SHIFT_CAP),
        # A_4 (inherited A_4 > 0 reproduced as an interval-midpoint lower bound)
        "A4_interval_midpoint_min_eig_lower": str(A4_lower),
        "A4_interval_radius_loewner": str(A4_rad),
        # certified Loewner brackets  lower_bracket <= S_4 <= upper_bracket
        "upper_bracket": tuple(tuple(str(x) for x in row) for row in upper_bracket),
        "lower_bracket": tuple(tuple(str(x) for x in row) for row in lower_bracket),
        "source_dual_U_lower_bracket": tuple(tuple(str(x) for x in row)
                                            for row in source_dual_U_lower),
        "source_dual_U_lower_is_pd": dual_lower_is_pd,
        "source_dual_U_certified": True,
        "source_dual_U_uses_unprojected_derivative_pairing": True,
        "source_dual_U_has_authenticated_moments": False,
        "source_dual_U_note": (
            "CERTIFIED alternate lower via primitive K-duality, full (Gv)' "
            "and ||g'||_L1<11/40; no claim that L2 projection contracts H1. "
            "Can be weaker than inherited U=0 floor. Moment subtraction is "
            "mathematically available but source-attested derivative moments "
            "have not been computed."
        ),
        "upper_bracket_min_eig_lower_by_parity": {k: str(v) for k, v in up_eig.items()},
        "upper_bracket_min_eig_lower": str(up_min),
        "upper_bracket_max_eig_upper_by_parity": [str(up_max[0]), str(up_max[1])],
        "lower_bracket_min_eig_lower_by_parity": {k: str(v) for k, v in lo_eig.items()},
        "lower_bracket_min_eig_lower": str(lo_min),
        "upper_bracket_is_psd": upper_is_psd,
        "upper_bracket_has_strict_negative_direction": upper_has_strict_negative_direction,
        "lower_bracket_is_psd": lower_is_pd,
        "interval_loewner_radius_GJ": str(r),
        "certified": True,
        "lower_bracket_mode": ("INHERITED_WB4_ZERO_SHIFT_CAP: S_4 >= A_4 - (121/32) W_L2(low), "
                               "U-independent and rigorous. Per-U residual-theorem tightening "
                               "A_4 - L_U - 50 T_{r_U} needs the open 3C modulus; diagnostic only. "
                "A separate CERTIFIED U-dependent primitive-dual alternative is "
                "returned as source_dual_U_lower_bracket, possibly weaker than this floor."),
        "first_window_only_not_RH": True,
        "nontrivial_zero_coordinates_used": False,
        "RH_proved": False,
    }
    if diagnostic:
        try:
            Tdiag = _finite_mode_residual_gram_diagnostic(V, Gblk, rank)
            diag_lower = _mat_sub(lower_short, _scale(Tdiag, F(1) / KAPPA))
            de, dmin = _parity_block_min_eig(diag_lower)
            result["diagnostic_finite_mode_residual_gram"] = \
                tuple(tuple(str(x) for x in row) for row in Tdiag)
            result["diagnostic_lower_bracket_min_eig_lower"] = str(dmin)
            result["diagnostic_note"] = (
                "NON-CERTIFIED: finite-mode residual derivative Gram truncated at "
                f"mode {rank}; omitted-mode tail is the OPEN Section 3C modulus. "
                "Shown only to locate the binding constraint, never to gate a verdict.")
            result["diagnostic_certified"] = False
        except Exception as exc:  # diagnostics must never crash a certified verdict
            result["diagnostic_error"] = f"{type(exc).__name__}: {exc}"
    return result


__all__ = ["CertifiedTrial", "CertifiedTrialError", "min_eig_lower", "max_eig_upper",
           "legendre_L2_norm2", "KAPPA", "ZERO_SHIFT_CAP", "GPRIME_L1_UPPER"]
