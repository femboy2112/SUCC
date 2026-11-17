# Moving-Frame Interferometry — validation and source boundaries

**Date:** 2026-11-16. **Scope:** finite exact rational and separately computed high-precision checks of [MF-01–08](MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md), without a universal statistical theorem.

## Exact local unittest

Executed in the assistant's working container:

~~~sh
python -m unittest -v /mnt/data/test_moving_frame_horizon.py
~~~

**Outcome:** 11 tests run; **11 PASS, zero failures, zero errors**. Source is a 6,390-byte stdlib-only Python module subsequently committed to [tests/test_moving_frame_horizon.py](../../../tests/test_moving_frame_horizon.py). Its independently computed local Git blob SHA-1 and the GitHub connector file SHA are identical:

~~~text
22eff24716f7dc8f3bc18d49f92883f8ea65b053
~~~

Exact tests use literal four signed BBP poles, \(U_0=0\), exact Fraction recurrence, and \(\beta_n=r(n+1)/15\). The module checks the original rational prefix by an independently summed expression, the source-commuting co-moving chart for five rational states and five arbitrary circle phases, literal source-frame displacements, positive finite tail allowances, rational speed lower bounds, and finite shell R0 implications. Other tests calibrate a rational nonunit fixed point, fully locked source, coherent wrong-seed **tail interval control** (not a synthetic assertion that the tested tail is the actual irrational wrong seed), and digit-horizon counting with and without sufficient precision.

The entropy test enumerates uniform base-16 digit words under a **Haar/full-shift prior** and checks \(H=4u\) bits. It is **not an entropy measurement of π digits** or physical heat.

## Exactly certified speed energy

Put \(a_n=[\|15U_n\|_{\mathbb T}-r(n+1)]_+\) and
\(\mathcal Q_B=(16/B)\sum_{n=B}^{2B-1}a_n^2\). Every displayed value below is a decimal view of a strictly exact rational Fraction computation.

| B | \(\mathcal Q_B\) source-rational lower certificate | \(\mathcal Q_B/8-1/B\), certified lower for \(1-\Re W_B\) |
|---:|---:|---:|
| 16 | 1.115511010778805585 | 0.0769388763473507 |
| 32 | 1.419544018700511624 | 0.14619300233756397 |
| 64 | 1.457849048509467970 | 0.1666061310636835 |
| 128 | 1.335706813143392397 | 0.15915085164292406 |
| 256 | 1.332030683976076938 | 0.16259758549700962 |

The exact tests certify \(\mathcal Q_B>6/5\) and \(\mathcal Q_B/8-1/B>1/10\) for each \(B\in\{32,64,128,256\}\); the comparisons do not depend on decimal precision. No claim covers all future B.

## Separate high-precision completed-phase replay

A different implementation using mpmath with **760 decimal digits** evaluated \(Y_n=16^n\pi/16\), computed the true real-circle squared-speed
\(\mathcal S_B=B^{-1}\sum|e(Y_{n+1})-e(Y_n)|^2\), and independently compared it to the Fraction source lower bound.

| B | True \(\mathcal S_B\), numerical diagnostic | \(1-\Re W_B\), numerical diagnostic |
|---:|---:|---:|
| 16 | 1.614671860763343471 | 0.900994447666808142 |
| 32 | 2.106262584163424450 | 0.937972822537413999 |
| 64 | 2.172219976569028863 | 1.055463321658293321 |
| 128 | 2.017034078051673771 | 1.022005840421231557 |
| 256 | 2.043328714478134068 | 1.069206193546490553 |

Every true speed exceeds the rational lower bound in this finite replay. These evaluations are **not interval certificates** and use the same imported π endpoint. The universal lower-certificate inequality is justified by the separate elementary circular-distance proof in MF-05, not by this computation.

## Refuted implications and unrun work

- **Refuted without an appeal to finite training:** an irrational objective orbit moves at every integer tick, but the sparse irrational countermodel in [Adaptive Gamma Ice-Climb](ADAPTIVE_GAMMA_ICE_CLIMB.md) has subsequential speed mean tending to zero. Thus no general "always moves ⇒ uniform energy" theorem.
- A finite prefix observer over the unrestricted radix-16 full shift has increasing missing information, but an observer with \(m\ge n+k\) initial digits can determine the next \(k\) digits at horizon \(n\). Under a point-mass authenticated BBP source, Haar conditional entropy does not apply.
- Source-corrected co-moving residual \(T_n\) tends to zero without ever vanishing at finite \(n\). This is an **analytic** unattainability analogy, not Nernst's thermodynamic third law.
- **Not run:** full SUCC root AGENTS.md gates, Main XXIV/XXV/XXVI integration suites, Lean kernel formalization, new independent physical source observation, hosted CI final-head completion, and a theorem establishing the positive all-late-shell rational speed mean MF-08.
- **OPEN:** R0, base-16 π normality, and all-mode signed Weyl cancellation.

**Next verdict-changing probe:** propose a source-derived, zero-seed-sensitive inequality forcing \((1/B)\sum_{n=B}^{2B-1} a_n^2\ge\delta>0\) on **every** sufficiently late integer shell. Use signed/odd-denominator carry and the original four-pole forcing; test hostile same-forcing counterseeds and source-coboundary controls before claiming any all-shell saving.
