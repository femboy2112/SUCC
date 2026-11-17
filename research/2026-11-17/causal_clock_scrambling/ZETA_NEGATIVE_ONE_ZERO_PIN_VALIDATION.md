# ξ(−1) / BBP Null-Jet Zero-Pinning Defect — execution and falsification receipt

**Date:** 2026-11-17. Companion to [ZETA_NEGATIVE_ONE_ZERO_PIN_DEFECT.md](ZETA_NEGATIVE_ONE_ZERO_PIN_DEFECT.md). All identities are scoped classical analytic mathematics. The RH-equivalent pinning-defect condition is **not shown to vanish**, and neither RH, R0 nor π base-16 normality is claimed proved.

## Executed exact-rational focused tests

Locally executed:

~~~sh
python -m unittest discover -s /mnt/data -p 'test_zeta_minus_one_zero_pin_defect.py' -v
~~~

**Result: 8 tests PASS, zero failures, zero errors.** The committed script [tests/test_zeta_minus_one_zero_pin_defect.py](../../../tests/test_zeta_minus_one_zero_pin_defect.py) has Git blob SHA-1 identical to the *final reexecuted local bytes*:

~~~text
9e0efbeb085ddd9eb4ae89ef9d533bda5902c26f
~~~

Tests include original zero-seeded finite BBP partial sums; first six formal jets computed **independently** from the recurrence \((P_N+s)G_N(s)=s\); \(\zeta(-1)=-1/12\) and \(\xi(-1)=\pi/6\) normalization; finite genuine-prime Euler/Hurwitz complementary registers; exact on-line versus off-line square-factor contrasts using Fraction at multiple **synthetic** zero coordinates; the β↦1−β mirrored pair; the positive quadratic response coefficient; a low-height mutant where the factor inequality reverses; and a finite example proving that all observed zeros on a line do NOT establish the infinite claim.

**Scope:** all off-critical-line coordinates in tests are synthetic mathematical controls. They are NOT identified with actual Riemann zeros.

## Separate symbolic algebra audit

An independently executed SymPy derivation established as **exact symbolic identities**:

\[
\xi(-1)=\frac12(-1)(-2)\sqrt\pi\,\Gamma(-1/2)\zeta(-1)=\pi/6,
\]

and, writing \(t=\gamma^2+1/4\), \(d=(\beta-1/2)^2\),

\[
|1+2/[\rho(1-\rho)]|^2=
1+\frac{4(t+1-d)}{t^2+(2\gamma^2-1/2)d+d^2}.
\]

It then independently factored the pinned-square minus actual-square response:

\[
\left(1+\frac2t\right)^2-
\left|1+\frac2{\rho(1-\rho)}\right|^2
=
\frac{4d\,[3t^2+t-1+(t+1)d]}
{t^2[t^2+(2t-1)d+d^2]}.
\]

The local expansion in the squared horizontal displacement has coefficient

\[
\frac{2(3t^2+t-1)}{t^2(t+2)^2}.
\]

All symbolic residuals simplified to zero. Exact sample \( \beta=1/4,\gamma=14 \) has squared-gain gap \(23705552/1215918531925>0\); the corresponding exact quadratic-log coefficient is \(59257568/387512475025>0\). These computations independently check the algebraic source of the positivity; the universal proof is the paper factorization plus established zero-height facts.

## First 40 actual critical-line zeros — numerical sanity check, NOT a product proof

An independent mpmath implementation at 38 decimal working digits used its built-in zetazero(n) to evaluate the first 40 known critical-line zero ordinates and accumulate the *finite* pinned product. Results:

| Number of positive zeros | Finite pinned product | \(\pi/3\) minus that finite product |
|---:|---:|---:|
| 1 | 1.0099979776674464 | 0.0371995735291515 |
| 2 | 1.0145662836529958 | 0.0326312675436018 |
| 5 | 1.0218875080756462 | 0.0253100431209516 |
| 10 | 1.0273662069032110 | 0.0198313442933867 |
| 20 | 1.0323580332392750 | 0.0148395179573227 |
| 40 | 1.0365465169155360 | 0.0106510342810619 |

Only 40 **known** line zeros were sampled; the tail is not computed or certified by this table. The **infinite** paired Hadamard identity and its absolute convergence follow from classical theorems, not from these finite values.

## Adversarial controls and claim boundaries

- The **actual zero-product identity** gives \(\pi=3\prod_{\Im\rho>0}(1+2/[\rho(1-\rho)])\) **without assuming RH**. Hence the BBP jet equality \((16/\pi)\xi(-1)=8/3\) holds even under a hypothetical RH-false zero distribution. It cannot select the critical line.
- The **pinned** product \(\Pi_{\rm pin}=3\prod_{\Im\rho>0}(1+2/[\gamma_\rho^2+1/4])\) uses the full *actual upper-zero ordinate multiset* and has \(\Pi_{\rm pin}\ge\pi\), equality iff RH. This is an exact **equivalent restatement of RH**, not a proof that the equality occurs. Its irrationality is not asserted without RH.
- The factorwise inequality requires \(\gamma>1/2\), supplied for actual zeros by established certified first-zero results. A synthetic small-height control reverses the inequality, so this is not a generic all-complex-root result.
- At large heights, the logarithmic off-line gain starts at order \(6(\beta-1/2)^2/\gamma^4\), a **resolution decay**, not an independent observation of off-line zeros.
- The Euler product \(\prod_p(1-p)\) **does not converge** to \(\zeta(-1)\). The finite E_Q R_Q product uses a separate correctly analytically continued Hurwitz/coprime complement and its genuine-prime source passport.
- The BBP null-seed first jet and ξ(-1) identify a **single scalar**, not the full γ-list or the real parts β. Even all higher derivatives of \(G_\infty(s)=s/(s+\pi/16)\) contain only powers of the same π endpoint. No source-derived all-shell π-digit inequality follows.
- The locked changed-source, matched positive non-telescoping locked source, changed-seed dyadic aliases and sparse badly approximable κ16 remain valid hostile controls.

**Unexecuted on this head:** full SUCC root unittest/provenance/observer/ordinal gates; Lean kernel proof of the new formula; certified interval computation of the entire zero set; independent mathematical refereeing; final GitHub CI completion.

**Verdict-changing probe:** construct a source-passported BBP observable family that transports actual four-pole chronological carries and signed terminal winding into *nontrivial variation* of ξ or its zero-location defect. A single normalization at −1, or a projected product defined using all unknown zeros, does not close either universal problem.
