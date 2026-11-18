# Ordinal Mellin/Gamma Observer Ladder — exact execution and independent Gamma audit

**Date:** 2026-11-17. Companion to [ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md](ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md). **All π-normality and RH conclusions remain OPEN.**

## 1. Executed exact original-source regression

The local standard-library Fraction script was executed:

~~~sh
python -m unittest -v /mnt/data/test_mellin_gamma_observer_ladder.py
~~~

**9/9 tests passed, zero failures, zero errors.** The exact 5,871-byte executed file has Git blob SHA **f3be2d7ba63172f08e3c3465ab8fe8e55b73efa4**, identical to the fetched GitHub branch artifact [tests/test_mellin_gamma_observer_ladder.py](../../../tests/test_mellin_gamma_observer_ladder.py).

The tests cover the untouched literal original four signed poles and zero seed; positive source kernel Q/(16−t⁸); exact N-step Mellin/chronological shift boundary equation; exact rational finite compact-tail bound on real w; all principal positive Schur pivots of finite source-moment Hankel matrices (orders ≤4 and source prefixes N=1,2,5,10); exact residue activation of four pole channels at every new source clock; the Gamma functional-recurrence denominator; an alternate positive, strictly decreasing, zero-seed forcing whose Mellin moment tower stays positive while its completed endpoint locks; and a distinct same-mass/different-first-moment null control.

**Scope:** the all-m strict positivity and polynomial density statements are paper proofs from the positive continuous measure, not empirical extrapolations from small matrix ranks. The complex-disk tail bound and entire continuation have separate integral/holomorphic proofs, not merely real-grid checks.

## 2. Independently coded 80-decimal Gamma activation audit

A separate mpmath implementation constructed D(w)=∏_{a∈{1,4,5,6}}rgamma((w+a)/8) and E_N(w)=D(w)B_N(w)/D(0). It evaluated E_N(w0+10^−34) at pole-marker w0=−a−8j for stages N=j (unopened), N=j+1 (first activated) and N=j+2 (inherited). It compared each to the **independent explicit residue/Gamma derivative formula**.

| (a,j), w0 | N≤j predicted channel | N≥j+1 predicted inherited value |
|---|---:|---:|
| (1,0), −1 | 0 | +0.12171043049… |
| (4,0), −4 | 0 | +0.00351017647… |
| (1,1), −9 | 0 | +0.000891433817… |
| (5,1), −13 | 0 | −0.000072694908… |
| (6,2), −22 | 0 | +0.000253561887… |

Unopened channels differed from zero by at most ~3.3×10^−37; activated channels differed from the explicit gamma-residue limit by at most ~7×10^−36, consistent with the nonzero evaluation offset. These are **high-precision diagnostics**, not rigorous ball arithmetic; the stage-zero/activation/persistence theorem is established algebraically by simple pole cancellation.

## 3. Completed Gamma-shift equation checked against independent finite sums

For w=0,1/2,2 and N=1,3,10, the same separately coded 80-digit implementation evaluated

\[
\prod_{a}(w+a)\mathcal E_N(w+8)
-8^4[16\mathcal E_N(w)-D(w)r_w(1)/D(0)]
-8^4D(w)16^{-N}r_w(N+1)/D(0).
\]

All nine absolute residuals were at or below 1.8×10^−77 at 80-digit precision. The paper gives an exact source-index algebra proof, and the relative gamma shift follows from \(\Gamma(z+1)=z\Gamma(z)\).

## 4. Source-moment channel and differentiation sanity

Independent mpmath integration of K(t)(−log t)^k, at 55 digits, yielded:

| k | \(\int_0^1 K(t)(-\log t)^k\,dt\) (diagnostic) |
|---:|---:|
| 0 | 0.1963495408493620774039152115 |
| 1 | 0.2380481176058278013951488116 |
| 2 | 0.4945426474866620160223766707 |
| 3 | 1.496191596820460425125728117 |
| 4 | 5.996402591942089406378978287 |
| 5 | 29.99570019776040249509707274 |
| 6 | 179.9937722097936400312431956 |

The k=0 value matches π/16. First low-order real-source Hankel determinants are positive: det(H1)≈0.04043631546875599, det(H2)≈0.03425310046577852, det(H3)≈0.2659372957375032. These diagnostics do not replace the exact all-order positive-measure proof.

The completed function has \(\mathcal E(-1)=\Gamma(1/8)\Gamma(3/4)/(32\Gamma(3/8))\approx0.12171043049029579\). Its first derivative at 0 is approximately +0.07833412726962471, whereas the shifted zeta observer's first derivative (3/8)ξ′(−1) is approximately −0.01356112284911137. Hence **the two analytic germs do not agree directly**, despite the shared initial value \(\pi/16\).

## 5. What the observer tower cannot establish

- **The source-derived moments are not independent measurements** of π's digit distribution. They encode the original positive Mellin measure. The infinite analytic germ uniquely determines that measure within a suitable class, but this is not an empirical or arithmetic normality theorem.
- The \(\omega\)-closure of finite polynomial observers is a Hilbert-space completion, **not a terminating infinite computation**, a physically traversed ordinal, or a proof rule that settles arbitrary limit statements.
- The original-source Gamma completion is entire, but the alternate locked zero-seeded forcing from the theorem note also admits positive moment Gram matrices at every order and an entire reciprocal-Gamma completion. Hence the tower's existence and uniform analytic source convergence do not force R0.
- The proved w↦w+8 Mellin source-clock transport retains exact finite boundary terms. It **does not** automatically transport to the nonlinear modulo-one integer winding of \(U_{2B}\), nor to genuine-prime Euler factors or the nontrivial ξ-zero ordinates.
- No unrestricted uniform contraction rate of the observer approximation residual in L²(ν) has been established; the geometric 16^−N rate belongs to the analytic source truncation on fixed compact w-domains, **not** to π's dyadic-shell Weyl average.

**Unexecuted on this head:** full SUCC root unittest/provenance/observer/ordinal gate suite, pinned Lean formalization, independent blind referee review, completed hosted CI. **OPEN:** original zero-seeded R0 all-shell norm lower bound and all-mode π base-16 normality; RH also remains OPEN.

**Next falsifier:** construct a cross-plane source-authenticated map between the Γ-regularized Mellin moment/activation tower and the signed **integer winding** of the original U_(2B). Freeze its predicted density and error bound before computing new shells; require the relation to fail for the matched positive zero-seed locked source, the Kempner cold-shell source and the coherent original-forcing locked counterseed. Without a source-specific all-shell inequality, the new tower is an exact reconstruction improvement rather than a normality proof.
