"""Four-mode vs thirty-mode Suzuki Schur transport: exact finite rational model.

The 4-mode and 30-mode Schur reductions use DIFFERENT low/high cuts:
    F_4  = span{P_1..P_4},    high^{(4)}  = modes >= 5
    F_30 = span{P_1..P_30},   high^{(30)} = modes >= 31,   F_4 subset F_30.

Two facts, both established here by EXACT rational finite models (the real source
30-block is not needed to settle the *structural* transport questions, and an
exact model is the honest instrument for a conjectured transfer):

(1) HAYNSWORTH QUOTIENT / TRANSITIVITY.  The shorted operator (Schur complement)
    is transitive across the nested cut F_4 subset F_30:
        Short_{F_4}(G) = Short_{F_4}( Short_{F_30}(G) ).
    So S_4 = Short_{F_4}(S_30): the four-mode Schur complement is the four-mode
    Schur complement OF the thirty-mode one. A certified two-sided S_30 enclosure
    therefore transports to S_4 by an EXACT finite 26-mode (modes 5..30) shorting
    -- a genuine acceleration IFF S_30 is easier to certify than S_4.

(2) COERCIVITY DOES NOT TRANSPORT THROUGH A SIGNED MIDDLE BLOCK (no-go).  The
    30-mode high coercivity kappa_30 = 369/10000 (suzuki_moment_schur
    .source_moment30_certificate) exceeds the 4-mode kappa_4 = 1/50, but it only
    protects modes >= 31.  Going from S_30 down to S_4 shorts the SIGNED modes
    5..30, which carry no coercivity guarantee.  An exact rational countermodel
    shows a large high coercivity cannot prevent a negative four-mode Schur when
    the intermediate block is indefinite: the binding shorting is the signed
    middle, not the coercive top.  Hence the thirty-mode decomposition does not,
    by itself, decide the four-mode sign -- consistent with S_4 OPEN.

No zeta zeros. RH PROVED: NO.  These are structural finite-dimensional theorems
about the reduction, NOT statements about the sign of the authentic S_4.
"""
from __future__ import annotations

from fractions import Fraction as F

from .suzuki_moment_schur import (
    SchurSourceError, matmul, matadd, matinv, transpose, symmetric,
)

KAPPA_4 = F(1, 50)
KAPPA_30 = F(369, 10000)   # source_moment30_certificate strict_high_L2_coercivity


def _block(M, rows, cols):
    return tuple(tuple(M[i][j] for j in cols) for i in rows)


def short_to(G, keep):
    """Exact Schur complement (shorted operator) of symmetric rational G onto the
    index set `keep`, shorting out the complement block (which must be invertible):
        Short_keep(G) = G[keep,keep] - G[keep,rest] (G[rest,rest])^{-1} G[rest,keep].
    """
    n = len(G)
    if not symmetric(G):
        raise SchurSourceError("Schur complement needs a symmetric matrix")
    keep = tuple(keep)
    rest = tuple(i for i in range(n) if i not in keep)
    A = _block(G, keep, keep)
    if not rest:
        return A
    B = _block(G, keep, rest)
    D = _block(G, rest, rest)
    Dinv = matinv(D)
    corr = matmul(matmul(B, Dinv), transpose(B))
    return matadd(A, corr, F(-1))


def haynsworth_transitivity_holds(G, low, mid):
    """Check Short_low(G) == Short_low(Short_{low+mid}(G)) exactly.

    low, mid are disjoint index tuples with low+mid+high = range(n). Returns
    (direct, nested, equal). This is the exact transitivity of shorting across
    the nested cut F_low subset F_{low+mid}."""
    low, mid = tuple(low), tuple(mid)
    inner_keep = tuple(sorted(low + mid))
    G_lowmid = short_to(G, inner_keep)
    # re-index low within inner_keep
    pos = {idx: k for k, idx in enumerate(inner_keep)}
    low_in_inner = tuple(pos[i] for i in low)
    nested = short_to(G_lowmid, low_in_inner)
    direct = short_to(G, low)
    equal = (direct == nested)
    return {"direct": direct, "nested": nested, "equal": equal,
            "thirty_mode_block_S30_analogue": G_lowmid}


def coercivity_does_not_transport_example(eps=F(1, 10), b=F(1)):
    """Exact rational no-go: an arbitrarily coercive HIGH direction cannot rescue
    the four-mode Schur when the low sector couples to a NEAR-NULL intermediate
    direction of the (jointly PSD) high sector.

    4x4 model, cut low={0,1}, rest={2,3}. The rest block is PSD and invertible,
    D_rest = diag(eps, c): rest mode 2 is a near-null "signed middle" direction
    (small eps, the modes-5..30 analogue, carrying NO coercivity guarantee), rest
    mode 3 is the strongly coercive high direction (large c, the modes->=31 /
    kappa_30 analogue). Low mode 0 couples to the near-null direction with weight b.

    Short_{low}(G)[0,0] = 1 - b^2/eps, INDEPENDENT of c. For b^2 > eps the four-
    mode Schur is negative in that direction for EVERY high coercivity c, however
    large. The coercive high direction is decoupled and irrelevant: the sign is
    set by the unprotected near-null middle, not by kappa_30."""
    results = []
    for c in (F(1), F(100), F(10_000), F(10 ** 8)):
        G = (
            (F(1), F(0), b,    F(0)),   # low 0 couples to rest 2 (near-null) with weight b
            (F(0), F(1), F(0), F(0)),   # low 1 decoupled
            (b,    F(0), eps,  F(0)),   # rest 2 = near-null middle (eigenvalue eps)
            (F(0), F(0), F(0), c),      # rest 3 = coercive high (eigenvalue c)
        )
        S_low = short_to(G, (0, 1))
        a, bb, d = S_low[0][0], S_low[0][1], S_low[1][1]
        det = a * d - bb * bb
        not_psd = (det < 0) or (a + d < 0)
        results.append({"high_coercivity_c": str(c),
                        "four_mode_schur_[0,0]": str(a),
                        "det": str(det), "four_mode_schur_not_psd": not_psd,
                        "S00_equals_1_minus_bsq_over_eps": a == F(1) - b * b / eps})
    all_indefinite = all(r["four_mode_schur_not_psd"] for r in results)
    independent_of_c = len({r["four_mode_schur_[0,0]"] for r in results}) == 1
    return {"cut": "low={0,1}, rest={near-null middle(eps), coercive high(c)}",
            "eps": str(eps), "b": str(b), "sweep": results,
            "high_coercivity_cannot_rescue_four_mode_sign": all_indefinite,
            "four_mode_schur_independent_of_high_coercivity_c": independent_of_c,
            "kappa_4": str(KAPPA_4), "kappa_30": str(KAPPA_30),
            "moral": ("kappa_30 > kappa_4 but protects only modes >=31; the "
                      "modes 5..30 shorting is signed/near-null and unprotected, "
                      "so the thirty-mode coercivity does not decide the four-mode "
                      "sign -- consistent with S_4 OPEN"),
            "RH_proved": False}


def demo():
    # A symmetric signed 6x6 with invertible sub-blocks for the transitivity check.
    G = (
        (F(3),   F(0),   F(1,2), F(0),   F(1,5), F(0)  ),
        (F(0),   F(2),   F(0),   F(1,3), F(0),   F(1,7)),
        (F(1,2), F(0),   F(-1),  F(0),   F(1,4), F(0)  ),
        (F(0),   F(1,3), F(0),   F(2),   F(0),   F(1,6)),
        (F(1,5), F(0),   F(1,4), F(0),   F(5),   F(0)  ),
        (F(0),   F(1,7), F(0),   F(1,6), F(0),   F(4)  ),
    )
    trans = haynsworth_transitivity_holds(G, low=(0, 1), mid=(2, 3))
    nogo = coercivity_does_not_transport_example()
    return {"transitivity_equal": trans["equal"],
            "coercivity_transport_nogo": nogo["high_coercivity_cannot_rescue_four_mode_sign"],
            "kappa_4": str(KAPPA_4), "kappa_30": str(KAPPA_30), "RH_proved": False}


def source_30mode_middle_block_obstruction_certificate(J=16):
    """Moonshot D: Exact quantitative obstruction to nested 30->4 Schur transport
    using the 30-mode Young/L1 lower bracket L_30 = A_30 - ((11/40)^2 / kappa_30) W_{L2,30}.

    Theorem D.1:
      1. Since ||G||_{op} <= ||g||_{L^1(-1,1)} <= ||g'||_{L^1(-1,1)} < 11/40, we have
         A_30 < (11/40) W_{L2,30} in Loewner order.
      2. Consequently, on the discarded 26-mode middle subspace M_{5:30} = span{P_5..P_30}:
           L_30|_{5..30} < (11/40 - (11/40)^2 / kappa_30) W_{L2,5..30}.
         - At kappa_30 = 369/10000 (source_moment30_certificate):
             11/40 - 3025/1476 = -26191/14760 < 0.
         - At kappa_30 = 1/16 (tate_suzuki_fourier_schur):
             11/40 - 121/100 = -187/200 < 0.
         Hence L_30|_{5..30} is strictly NEGATIVE-DEFINITE on all 26 modes, violating
         the monotone nested shorting hypothesis L|_{5..30} > 0.
      3. Entrywise on the authentic source at modes m in {5, 6, 29, 30}, (A_30)_{m,m} / W_{m,m}
         decays as O(m^{-2}) (from ~0.0040 at m=5 to ~0.00075 at m=30) because G is compact,
         whereas the Young residual penalty (11/40)^2 / kappa_30 is O(1).
    """
    from .suzuki_legendre_source import authentic_full_low_entry
    from .source_weil_hierarchy import authentic_positive_gamma_tail_norm
    from .tate_suzuki_shorting import verify_original_suzuki_source

    if type(J) is not int or not 1 <= J <= 64:
        raise SchurSourceError("J must be an integer in 1..64")
    verify_original_suzuki_source()
    gprime_l1 = F(11, 40)
    penalty_moment30 = (gprime_l1 ** 2) / KAPPA_30               # 3025/1476
    penalty_fourier30 = (gprime_l1 ** 2) / F(1, 16)              # 121/100
    universal_upper_factor_moment30 = gprime_l1 - penalty_moment30   # -26191/14760
    universal_upper_factor_fourier30 = gprime_l1 - penalty_fourier30 # -187/200

    tail_J = authentic_positive_gamma_tail_norm(J)
    sampled_modes = {}
    for m in (5, 6, 29, 30):
        iv = authentic_full_low_entry(m, m, F(1, 2), J)
        w_mm = F(1, 2 * m + 1)
        a_mm_upper = iv.hi + tail_J * w_mm
        normalized_a_upper = a_mm_upper / w_mm
        l30_diag_upper = a_mm_upper - penalty_moment30 * w_mm
        sampled_modes[m] = {
            "W_mm": w_mm,
            "A_mm_upper": a_mm_upper,
            "A_mm_over_W_mm_upper": normalized_a_upper,
            "L30_mm_upper": l30_diag_upper,
            "strictly_negative": l30_diag_upper < 0,
        }
    if not (universal_upper_factor_moment30 == -F(26191, 14760) < 0
            and universal_upper_factor_fourier30 == -F(187, 200) < 0
            and all(v["strictly_negative"] for v in sampled_modes.values())):
        raise ArithmeticError("30-mode middle block obstruction invariant failed")
    return {
        "source": "AUTHENTIC_Q_ZETA_SUZUKI_30_TO_4_MIDDLE_BLOCK_OBSTRUCTION",
        "J": J,
        "kappa_30_moment": KAPPA_30,
        "kappa_30_fourier": F(1, 16),
        "young_penalty_moment30": penalty_moment30,
        "young_penalty_fourier30": penalty_fourier30,
        "universal_middle_loewner_upper_factor_moment30": universal_upper_factor_moment30,
        "universal_middle_loewner_upper_factor_fourier30": universal_upper_factor_fourier30,
        "middle_block_5_to_30_strictly_negative_definite": True,
        "monotone_nested_short_hypothesis_satisfied": False,
        "sampled_authentic_middle_diagonals": sampled_modes,
        "structural_cause": (
            "G is compact on L^2_0(-1/2,1/2) so (A_30)_{m,m}/W_{m,m} = O(m^{-2}), "
            "whereas the unprojected Young derivative cap subtracts an O(1) multiple "
            "of W_{m,m} across all middle modes 5..30."
        ),
        "RH_proved": False,
    }


__all__ = ["short_to", "haynsworth_transitivity_holds",
           "coercivity_does_not_transport_example", "demo",
           "source_30mode_middle_block_obstruction_certificate",
           "KAPPA_4", "KAPPA_30"]

