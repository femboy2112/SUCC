"""Signed quadratic pushforward  K -> P K P^*  on the authentic BBP orbit.

Status: REORGANIZATION + NEGATIVE THEOREM + FIREWALL SHARPENING.  It introduces
NO new general categorical theorem and makes NO progress on  S_N(h)=sum_n e(hU_n)=o(N).
pi base-16 normality: OPEN.  RH: OPEN (separate program).  The authentic source
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U_0=0, U_{n+1}=16U_n+r(n+1) is unchanged.

This module discharges the `K -> P K P^*` naturality obligation pre-registered in
docs/CATEGORICAL_OBSERVER_ATLAS.md as a NEGATIVE result, with one genuinely new
(classical) product.  Three things are established, all exact over Q[Q/Z]:

1.  CONSERVATION / coarsening invariance (reorganization).  With cell amplitudes
    S_A = sum_{n in A} e(hU_n) = (P_f z)_A and the coarsened kernel
    (P_f K P_f^*)_{A,B} = S_A conj(S_B),  the total
        |S_N(h)|^2 = sum_A |S_A|^2  +  sum_{A != B} S_A conj(S_B)
    is INVARIANT under any partition coarsening: refinement only moves mass between
    the within-cell diagonal and the signed cross term.  No partition choice lowers a
    gate summand (the pushforward is "gate-conservative").

2.  SIGNED BASE CHANGE  <=>  CARTESIAN  (classical finite-set / Mackey base change;
    Mac Lane-Moerdijk I.9).  For a commuting Beck-Chevalley square, amplitude base
    change  g^*(q_! z) = q'_!(g'^* z)  holds for EVERY amplitude z IFF the square is
    cartesian.  NEW PRODUCT (firewall sharpening): realization/ghost-faithfulness is
    NECESSARY but NOT SUFFICIENT for signed transport -- the redundant-realizer square
    passes the ghost firewall AND Prop-base-change-for-all yet breaks signed base change
    (defect -e(1/3)).  Hence the correct signed firewall condition is `is_cartesian`,
    not `realization_firewall_breaks`.  The Prop/ghost report is amplitude-INDEPENDENT
    (signed-blind): two amplitudes on the same cartesian square give identical reports
    but energies 48 vs 0.

3.  THE OCCUPANCY-BASELINE TRAP (negative control, do not mistake for progress).  The
    rational quantity (purity.coefficient(0) - H)/H computed from the window
    compression equals (H-1)/N EXACTLY and is phase-BLIND: it is identical for the
    authentic orbit and for non-normal counterfeits (changed seed, changed forcing).
    It is NOT the section-2 Weyl gate, which is the EVALUATED complex statistic
    2 sum_{d<H}(1-d/H)|(1/N) sum_n e(dhU_n)|^2 (phase-dependent; authentic ~0.15 vs
    counterfeit ~H-1 at the receipt points).  `occupancy_baseline` is exposed only to
    certify this distinction; it carries the hard flag that it is NOT the gate.

FIREWALL (AGENTS.md rule 6): no modulus bound is promoted to cancellation; no signed
asymptotic saving is drawn from positivity / Gram-PSD / diagram commutation / CRT
occupancy independence.  Corrected positivity statement (adversarial review): positive
within-cell/ANOVA/PSD data does NOT determine |S_N(h)|^2 and cannot bound it below its
sharp trivial upper bound (sum_A |S_A|)^2; it therefore yields NO saving.  Any all-N
saving must come from a source-derived within-cell coherent-energy bound, which this
module does not supply.

All arithmetic is exact in Q[Q/Z] (PhasePoly) unless a value is explicitly marked
OBSERVED (evaluated numerically as a labeled diagnostic, never a certificate).
"""
from fractions import Fraction as Q

from . import beck_chevalley_source as bc
from . import succ_internal_matrix_walk as mw

PP = mw.PhasePoly

# --- grep-able honest status flags (firewall) -------------------------------
signed_saving_proved = False          # no signed asymptotic saving is established
pi_normality_proved = False           # S_N(h)=o(N) remains OPEN
occupancy_baseline_is_the_gate = False  # (H-1)/N is phase-blind, NOT the Weyl gate
introduces_new_theorem = False        # classical Mackey base change + reorganization

__all__ = [
    "amp_pushforward", "amp_pullback", "kernel", "quadratic_pushforward",
    "amplitude_base_change_holds", "amplitude_base_change_defect",
    "quadratic_base_change_holds", "signed_firewall_report",
    "cell_moments", "total_moment", "ones_contraction", "within_cell_energy",
    "cross_term", "conservation_holds", "rotate_cells",
    "occupancy_baseline", "weyl_gate_value", "authentic_states",
]


# =========================================================================== #
#  Linear amplitude pushforward / pullback on PhasePoly-valued data.
# =========================================================================== #
def amp_pushforward(f, z):
    """f_! z : fiber-SUM of an amplitude z: dom(f) -> PhasePoly onto cod(f)."""
    if set(z.keys()) != set(f.domain):
        raise ValueError("amplitude domain must equal f.domain")
    out = {y: PP.zero() for y in f.codomain}
    for x in f.domain:
        out[f.apply(x)] = out[f.apply(x)] + z[x]
    return out


def amp_pullback(g, w):
    """g^* w : precompose w: cod(g) -> PhasePoly with g."""
    return {o: w[g.apply(o)] for o in g.domain}


# =========================================================================== #
#  Rank-one Hermitian kernel K_{a,b}=z_a z_b^* and its pushforward P K P^*.
# =========================================================================== #
def kernel(z, index):
    """Rank-one Hermitian kernel K_{a,b} = z_a z_b^* over `index` (a tuple)."""
    return {(a, b): z[a] * z[b].star() for a in index for b in index}


def quadratic_pushforward(f, K):
    """(P K P^*)_{o,o2} = sum_{a in f^-1(o)} sum_{b in f^-1(o2)} K_{a,b}."""
    cells = {}
    for x in f.domain:
        cells.setdefault(f.apply(x), []).append(x)
    out = {}
    for o in f.codomain:
        for o2 in f.codomain:
            acc = PP.zero()
            for a in cells.get(o, []):
                for b in cells.get(o2, []):
                    acc = acc + K[(a, b)]
            out[(o, o2)] = acc
    return out


# =========================================================================== #
#  Amplitude / quadratic Beck-Chevalley base change (checkable identities).
#      g^*( q_! z ) == q'_!( g'^* z )      on O'
# =========================================================================== #
def amplitude_base_change_holds(square, z):
    left = amp_pullback(square.g, amp_pushforward(square.q, z))
    right = amp_pushforward(square.q_prime, amp_pullback(square.g_prime, z))
    return left == right


def amplitude_base_change_defect(square, z):
    left = amp_pullback(square.g, amp_pushforward(square.q, z))
    right = amp_pushforward(square.q_prime, amp_pullback(square.g_prime, z))
    return {o: (left[o] - right[o]) for o in left if left[o] != right[o]}


def quadratic_base_change_holds(square, z):
    """Kernel-level base change for K = z z^* (corollary of the amplitude one)."""
    Ks = kernel(z, square.S)
    left_push = quadratic_pushforward(square.q, Ks)
    left = {(o1, o2): left_push[(square.g.apply(o1), square.g.apply(o2))]
            for o1 in square.O_prime for o2 in square.O_prime}
    Ks_pb = {(a, b): Ks[(square.g_prime.apply(a), square.g_prime.apply(b))]
             for a in square.S_prime for b in square.S_prime}
    right = quadratic_pushforward(square.q_prime, Ks_pb)
    return left == right


def signed_firewall_report(square, z):
    """Exact readings of the three nested firewall strata.  The correct signed
    firewall is `cartesian`; ghost-faithfulness (no ghost witness) and
    Prop-base-change-for-all are NECESSARY but NOT SUFFICIENT.
    """
    ghost = any(bc.realization_firewall_breaks(square, F)
                for F in bc.all_predicates(square.S))
    return dict(
        cartesian=bc.is_cartesian(square),
        comparison_surjective=bc.comparison_is_surjective(square),
        ghost_firewall_breaks=ghost,
        prop_bc_all=bc.beck_chevalley_holds_all(square),
        amplitude_bc=amplitude_base_change_holds(square, z),
        quadratic_bc=quadratic_base_change_holds(square, z),
        amplitude_defect=amplitude_base_change_defect(square, z),
    )


# =========================================================================== #
#  Conservation / coarsening invariance on a time partition of the orbit.
# =========================================================================== #
def cell_moments(states, labelfn, h):
    """dict cell -> (count, S_A) for the partition induced by labelfn(n, u)."""
    cells = {}
    for n, u in enumerate(states, 1):
        a = labelfn(n, u)
        cnt, s = cells.get(a, (0, PP.zero()))
        cells[a] = (cnt + 1, s + PP.monomial(h * u))
    return cells


def total_moment(states, h):
    return sum((PP.monomial(h * u) for u in states), PP.zero())


def ones_contraction(cells):
    """1^* (P K P^*) 1 = |sum_A S_A|^2 = sum_{A,B} S_A conj(S_B)."""
    S = sum((s for _, s in cells.values()), PP.zero())
    return S * S.star()


def within_cell_energy(cells):
    """Diagonal of P K P^*:  sum_A |S_A|^2  (the positive ANOVA-visible object)."""
    return sum((s * s.star() for _, s in cells.values()), PP.zero())


def cross_term(cells):
    """Signed off-diagonal:  sum_{A != B} S_A conj(S_B)."""
    return ones_contraction(cells) - within_cell_energy(cells)


def conservation_holds(states, labelfn, h):
    """|S_N(h)|^2 == ones_contraction(cells): coarsening invariant (exact Q[Q/Z])."""
    cells = cell_moments(states, labelfn, h)
    S = total_moment(states, h)
    return ones_contraction(cells) == S * S.star()


def rotate_cells(cells, theta):
    """Per-cell rotation S_A -> e(h*theta_A) S_A.  theta: cell-label -> Fraction.
    Source-blind positive-Gram countermodel: within-cell energies and sizes are
    INVARIANT while |sum_A S_A|^2 changes -- so positive diagonal data cannot
    determine (and yields no saving on) the gate quantity |S_N(h)|^2.
    """
    out = {}
    for k, (cnt, s) in cells.items():
        out[k] = (cnt, PP.monomial(Q(theta[k])) * s)
    return out


# =========================================================================== #
#  The occupancy-baseline trap (negative control).  NOT the gate.
# =========================================================================== #
def occupancy_baseline(states, H, h=1):
    """(purity.coefficient(0) - H)/H  ==  (H-1)/N, EXACTLY and phase-BLIND.

    WARNING: this is NOT the section-2 Weyl gate.  It is the constant (collision /
    occupancy) term of the window-compression purity polynomial; it depends only on
    (H, N) and is identical for the authentic orbit and for non-normal counterfeits.
    Exposed solely to certify that distinction (see `occupancy_baseline_is_the_gate`).
    """
    N = len(states)

    def Ad(d):
        s = PP.zero()
        for u in states:
            s = s + mw.formal_character(d * h, u)
        return s / N

    purity = PP.zero()
    for i in range(H):
        for j in range(H):
            purity = purity + Ad(i - j) * Ad(i - j).star()
    return (purity.coefficient(0) - H) / H


def weyl_gate_value(states, H, h=1, precision=60):
    """OBSERVED (evaluated, NOT a certificate) section-2 Fejer gate statistic
        2 sum_{d=1}^{H-1} (1 - d/H) |(1/N) sum_n e(d h U_n)|^2 .
    Phase-dependent: it separates the authentic orbit from counterfeits for a
    source reason, unlike `occupancy_baseline`.
    """
    N = len(states)
    acc = 0.0
    for d in range(1, H):
        s = PP.zero()
        for u in states:
            s = s + mw.formal_character(d * h, u)
        m = complex((s / N).evaluation(precision=precision))
        acc += 2.0 * (1.0 - d / H) * (abs(m) ** 2)
    return acc


def authentic_states(N):
    """The first N states {U_n}, n=1..N, of the authentic BBP orbit."""
    return tuple(mw.original_state(n) for n in range(1, N + 1))
