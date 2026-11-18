# Moving circle origin and rational BBP pair energy — validation receipt

**Date:** 2026-11-17. Companion to [CIRCLE_ZERO_FRAME_TRANSPORT.md](CIRCLE_ZERO_FRAME_TRANSPORT.md). This is an exact classical gauge/observer construction and a finite source-rational π-shell certificate, **not an all-shell R0 or π-normality theorem**.

## Executed local focused tests

The original 7,280-byte Python standard-library source was executed locally:

~~~sh
python -m unittest -v /mnt/data/test_circle_origin_gauge.py
~~~

**10/10 tests PASSED; 0 failures/errors.** Its exact tested bytes were uploaded under the non-conflicting filename [tests/test_bbp_circle_pin_pair_energy.py](../../../tests/test_bbp_circle_pin_pair_energy.py), after discovery that an existing SUCC session owned [tests/test_circle_origin_gauge.py](../../../tests/test_circle_origin_gauge.py). The local Git blob SHA-1 matches the fetched branch copy exactly:

~~~text
d6b23bb1cccb32b16aae6a6539eee470478382a5
~~~

Tests cover exact finite fixed-circle origins (15), arbitrary moving-clock origin connection, source-chart cocycle and three-part path composition, oracle-dependent perfect tracking with zero apparent connection, transported original zero-seed origin, Gaussian-rational phase variance under reference rotations, the nonunit fixed-point objection to upgrading R0 to a stronger origin-free theorem, six exact original-zero BBP rational pair-energy certificates, their invariance under common reference shifts, and independently computed conjugacy of the six-tap auxiliary lag filter with a transported zero kernel.

An early local test deliberately used a forbidden reference \(1/3\), which is *actually* among the 15 legal fixed origins: \(1/3=5/15\). That test was corrected to \(1/7\), and all tests were rerun before committing. A previous tautological conjugacy test was replaced by an independent one-step implementation of \(G^{-1}SG\); both changes are preserved in the committed version. **No invalid first run is counted as a passing result.**

## Original-source exact rational certificates

The 4-pole recurrence \(U_0=0,\ U_n=16U_{n-1}+r(n)\) was evaluated using exact Fraction arithmetic to compute
\[
\mathcal C_B=B^{-2}\sum_{1\le k<l\le B}
\|U_{2B}/16^k-U_{2B}/16^l\|_{\mathbb T}^{\,2},
\qquad
\rho_B=8r(2B+1)/(225B).
\]

The elementary geometric-tail and pair-chord inequalities imply
\[
8\mathcal C_B-\rho_B\le1-|W_B(\pi/16)|
\le4\pi^2\mathcal C_B+\rho_B.
\]
The following lower comparisons are exact rational inequalities; decimals are for readability:

| B | \(\mathcal C_B\) | Exact-rational lower bound \(8\mathcal C_B-\rho_B\) |
|---:|---:|---:|
| 4 | 0.03569540244463036 | 0.2855334575221658 |
| 8 | 0.03889454710511759 | 0.31115248904882153 |
| 16 | 0.03608117299376219 | 0.28864888687648715 |
| 32 | 0.04180327048581740 | 0.33442610103758850 |
| 64 | 0.04169064021997943 | 0.33352511385836436 |
| 128 | 0.04174617626938677 | 0.33396940916455410 |

All six source-rational lower bounds were checked **strictly >1/5** in full Fraction comparisons. This is a new basis-invariant finite *representation*, not a new asymptotic source inequality, and the clocks are in-sample.

## Independent completed-phase numerical audit

A separate mpmath program with **370 decimal working digits** evaluated \(z_n=e(16^n\pi/16)\) and the actual \(1-|W_B|\), without using the rational pair estimator to construct the circle phases. It confirmed the lower inequality in every listed shell:

| B | Numerically observed \(1-|W_B|\) |
|---:|---:|
| 4 | 0.59752473676329 |
| 8 | 0.70006470688088 |
| 16 | 0.64770894499748 |
| 32 | 0.93761718871622 |
| 64 | 0.93707470521309 |
| 128 | 0.93456030465674 |

These are floating numerical cross-checks, **not interval-certified proofs**. The full finite certificates derive from exact source Fraction arithmetic and elementary published trigonometric inequalities.

## Hostile limits and all-shell status

- **The trivial character of the auxiliary source-lag filter is not the arbitrary marked origin of the chronological physical circle**; \(Q(S)\)'s null kernel survives a simultaneous unitary gauge conjugacy.
- An observer may pin itself to an unknown actual phase every clock and see only zeros; this is an oracle-dependent chart and hides the carrier information in the chosen reference.
- There are exactly **15 constant circle origins** that preserve the unmodified radix-16 update. Other origins are lawful only when their affine source connection is retained.
- The anchored \(1-\Re W_B\) depends on reference pinning; the pair variance \(1-|W_B|^2\) does not under a common rotation. At \(x=1/15\), R0 holds although all pair variance is zero: the **origin-independent** positive gap is a strictly stronger, unproved goal.
- The finite rational \(\mathcal C_B\) continues to factor through the one scalar \(U_{2B}\); it cannot by itself reconstruct source histories erased by the terminal rank-one map.
- **Unrun:** full repository root tests and AGENTS gates, Lean, independent scholarly review, hosted CI completion on the new PR head.
- **OPEN:** a positive source-selected lower bound for \(\mathcal C_B\) on **every sufficiently late shell**, the weaker original R0 and all-mode base-16 π normality.

**Next proof discriminator:** keep both channels—the origin-free shell dispersion \(1-|W_B|\) and the original source-anchored alignment \(|W_B|-\Re W_B\). Build a source-authenticated carry/cofactor comparison able to force a positive contribution from one channel on every late shell without choosing an oracle-dependent moving origin.
