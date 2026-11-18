# Source-Shadow Interferometry: exact finite certificates and numerical independent audit

**Date:** 2026-11-16. Companion to [SOURCE_SHADOW_INTERFEROMETRY.md](SOURCE_SHADOW_INTERFEROMETRY.md). **Domain:** original source \(\{U_n\}_{1\le n\le512}\) with four literal BBP poles, zero seed and exact rational tail upper bounds. These are finite, not prospective all-large-shell proofs.

## 1. Executed source-rational certificate

A local Python standard-library Fraction implementation was executed with:

~~~sh
python -m unittest -v /mnt/data/test_shadow_interferometry.py
~~~

**Result:** 13 tests, 13 PASS, 0 errors, 0 failures. The exact 9,781-byte locally executed script was uploaded as [tests/test_shadow_interferometry.py](../../../tests/test_shadow_interferometry.py). Independent local calculation of its Git blob SHA-1 and GitHub connector's file SHA match **exactly**:

~~~text
bcbd25f3865c3e6bfb3526d3f9e5a2385bd85de9
~~~

The test source uses no third-party libraries, no floating-point π, no exponential evaluation, and no independent prime/coin clocks. It constructs \(U_n\) from the authenticated recurrence, \(\beta_n=r(n+1)/15\), literal integer \(C_n=\lfloor U_n\rfloor\), and exactly computes rational pair and anchor lower bounds. A separate expression \(16^n\sum_{j=1}^n16^{-j}r(j)\) cross-checks seven sample source states against the chronological recurrence. That check is an independent implementation path with **shared source coefficients**, not independent evidence for BBP evaluation of π.

The source-rational \(\mathcal Q_{B,\Pi}\) output (reported as approximate decimals solely to keep the table readable; each comparison to \(3/5\) was **exact Fraction arithmetic**):

| \(B\) | carry4 \(\mathcal Q\) | clock4 \(\mathcal Q\) | joint carry4×clock4 \(\mathcal Q\) |
|---:|---:|---:|---:|
| 32 | 0.6528733780393821 | 0.60693… | 0.44269… |
| 64 | 0.6380465660555075 | 0.63190… | 0.53490… |
| 128 | 0.6595855043699800 | 0.64348… | 0.58102… |
| 256 | 0.6532520322667094 | 0.65020… | 0.62533… |

For every listed \(B\), the exact carry4 and clock4 rational certificates **strictly exceed \(3/5\)**. This proves finite-only \(V_{B,\mathrm{carry}}>3/5\) and \(\Re W_B(\pi/16)<\sqrt{2/5}\), conditional only on inherited exact BBP identity and tail lemma. The same statement **is not asserted for every \(B\)**.

The independently executed weighted pair-count audit at separation threshold \(a_{n,m}\ge1/4\), where \(N_{B,c}\) counts unordered pairs within carry cell \(c\):

| \(B\) | \(\sum_cN_{B,c}/(|c|B)\) (approx) | unordered pair count |
|---:|---:|---:|
| 32 | 0.25208 | 75 |
| 64 | 0.23688 | 257 |
| 128 | 0.24661 | 1056 |
| 256 | 0.24712 | 4069 |

The count is *finite arithmetic output*, not a fitted probabilistic independence law; the values do not imply an eventual positive weighted pair density.

## 2. Independent representation: 750-digit completed π phases

A separate script, using mpmath with **750 decimal digits**, evaluated the *completed orbit* \(z_n=e^{2\pi i16^n\pi/16}\) directly and computed the actual carry-cell conditional variance from its complex cell means. It did not import or call the lower-bound estimator to calculate the phase statistic; it used the same source-produced carry-cell partition and compared after the fact. Results:

| \(B\) | High-precision true \(V_{B,\mathrm{carry}}\) | Exact rational lower \(\mathcal Q\), decimal view | Actual minus lower (diagnostic) | \(\Re W_B\) |
|---:|---:|---:|---:|---:|
| 32 | 0.9724117207292273686 | 0.6528733780393821 | 0.31953834269 | 0.06202717746258600113 |
| 64 | 0.9551522537903212590 | 0.6380465660555075 | 0.31710568774 | -0.05546332165829332075 |
| 128 | 0.9804490095734942602 | 0.6595855043699800 | 0.32086350520 | -0.0220058404212315568 |
| 256 | 0.9828119108097610439 | 0.6532520322667094 | 0.32955987854 | -0.06920619354649055256 |

These values are **numerical diagnostics, not certified intervals**. The rigorous certificate is the entirely rational comparison in §1, combined with the paper inequality \(V\ge\mathcal Q\). The high-precision route is a different representation of the same imported classical π endpoint, not an external blind witness. Source sample lengths end at index 511; these are previously explored clock regimes and **not a new held-out prediction** beyond the Main XXVI training horizon 131072.

## 3. Hostile and mutation controls

The 13 executable focused tests include:

- zero-seeded chronological recurrence and a direct BBP-prefix cross-check;
- exact circular-distance symmetries; mutation enlarging a tail budget to erase a pair certificate;
- four finite carry-only and clock-only strict \(>3/5\) comparisons;
- joint carry×clock and singleton refinement observations;
- exact unit-circle anchored/global-variance decomposition over Gaussian-rational points;
- exact Gamma-defect scalar transport of the paired energy;
- independent anchor \(>1/2\) finite shells;
- a fixed nonunit phase \(x=1/15\) with R0 but zero within-fiber variance;
- a completely locked \(x=1\) with no anchored or hidden phase disagreement;
- the failure of a universal lower bound for observers allowed to retain all time indices or arbitrary fine phase precision.

The sparse irrational control \(x_\star=3/16+\sum_j16^{-4^j}\) is proved in [the preceding AGIC dossier](ADAPTIVE_GAMMA_ICE_CLIMB.md); it carries hidden source distinctions arbitrarily far but has subsequential R0 defect \(\to0\). It defeats the infinite-horizon inference independently of any finite test.

## 4. Claim scope and next discriminating proof

- **Disclosed as paper algebra:** exact anchored/conditional variance, Gamma scalar energy transport, rational tail/chord lower envelope, pair-mass sufficient criterion.
- **Observed finite exact:** explicit BBP rational lower thresholds at four selected shells, plus additional finite anchor checks.
- **Observed numerical:** separate high-precision π-phase audit for those finite shells; no interval certification claimed.
- **UNVERIFIED:** an all-integer-shell positive lower bound for *any source-declared* nontrivial observer schedule, including the literal carry4 observer.
- **OPEN:** R0, full Weyl cancellation for all nonzero modes, π normality, completed Weil positivity and RH.

**Next verdict-changing probe:** first define an explicit arithmetic reason why original zero seed and its odd-denominator/cofactor chronology force a **weighted positive fraction of source-separated pairs** (IFS16), rather than just finite observed pair counts. Test the conjectured constants against changed-seed, rational finite-shadow and coboundary controls; require a genuinely new all-shell proof. If a proposed bound survives, its normalization immediately gives the quantitative R0 margin by IFS17. No assertion of physical causal entropy or quantum effect follows from this finite computation.
