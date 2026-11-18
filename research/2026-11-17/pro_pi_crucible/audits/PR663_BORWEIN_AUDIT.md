# Pinned PR #663 Borwein audit and comparison

## Contact and scope

Read-only source inspection at commit
`16d04ab58e213e75ab47e61a170138196dbcd292`, branch
`research/bbp-borwein-kernel-discrepancy-crucible-2026-11-17`, based on
PR #657 at `7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf`.

Read:

- `research/2026-11-17/causal_clock_scrambling/BORWEIN_QUANTITATIVE_KERNEL_BRIDGE.md`
- `research/2026-11-17/causal_clock_scrambling/BORWEIN_QUANTITATIVE_VALIDATION.md`
- `observational_succ/borwein_quantitative_certificate.py`
- `tests/test_borwein_quantitative_certificate.py`
- our current `research/2026-11-17/pro_pi_crucible/BORWEIN_INVERSE.md`
- parent #657 `tests/test_borwein_bbp_sweep.py`, function `supremum_exact`.

Pinned implementation Git blob: `21168fe02d90365ff537ece2af6c302240bd772d`,
6,228 bytes. Pinned test blob:
`93f8eff792c53d6e7af11592bfc564a89f52909c`. Both match #663's receipt.
No tests were rerun in this audit; no external referee or independent model
review is claimed. No repository or remote files were changed.

## Mathematical verdict

The principal #663 mathematical statements survive this paper/code audit:

1. The L2 energy `V=integral |L*(mu-m)|^2` is exactly the weighted all-mode
   Fourier square sum. Its autocorrelation representation and rational
   piecewise quartic integration are correct.
2. Its Fourier lower floor `2205/(139876 h^2)` follows from its displayed
   reverse-triangle argument. It is conservative but valid.
3. The square-root energy transport under the known uniform source-tail
   bound is the L2 reverse triangle inequality.
4. The per-mode estimate, followed by the stated Erdős–Turán inequality,
   yields the displayed coefficient `69938/735` and the conditional
   `V^(1/6)` rate. The external Erdős–Turán citation was not independently
   primary-source audited here; the proof's algebra after that import is
   correct.
5. The full-normality equivalence needs the standard short shell-to-prefix
   decomposition when passing from W_B on [B,2B) to Weyl prefix means. This
   is an omitted explanatory lemma, not a counterexample or false result.
6. The exact word enclosure criterion safely marks boundary ambiguity.

The implementation's polynomial interpolation/integration formulas, pairwise
autocorrelation integration, duplicate-aware interval discrepancy, and
rational upper-root checks are consistent with these claims.

## Receipt / description corrections

- The theorem manuscript ends with **23/23**, while the validation says
  **24=15+9** and the new test source contains 15 methods. This is a stale
  test-count statement, not a mathematical error.
- The test named `test_direct_zero_seed_words_agree_with_independent_source_recurrence`
  calls the same U implementation used by the certificate. It is an indexing
  cross-check, not an independent original-source recurrence implementation.
- Parent #657's `supremum_exact` uses endpoint/midpoint quadratic
  interpolation. Our quarter/midpoint implementation is separately written
  within the same mathematical method, not a derivative-sweep contrast.
- The pairwise-K and swept-square formulas are two decompositions, but they
  share L, breakpoints, rational arithmetic, and quadratic interpolation.
  These shared dependencies should remain explicit.

## Overlap and surviving novelty of our BI manuscript

| Object | #663 | Our current BI |
|---|---|---|
| All-mode Fourier nonvanishing | Inherited from #657 | Inherited, with exact operator derivation |
| Explicit lower Fourier gain | 45/(289 pi^2 h^2), then rational floor | Stronger 63/(289 pi^2 h^2); upper gain and sign also proved |
| Rational finite energy | Exact L2 / autocorrelation energy | Exact supremum of the existing swept response |
| Interval discrepancy | Erdős–Turán after separate per-mode bounds | Direct exact measure inverse plus semiconcavity |
| Rate from supremum Delta | No sharp bound | D <= (34/7) sqrt(Delta), optimal exponent 1/2 |
| Measure-valued inverse | Absent | (I+P/8)nu = -(289/288) tau g'' and Neumann inverse |
| Source statistical saving | Not proved | Not proved |

The two dossiers overlap at the Fourier instrument and authentic tail
transport. The exact inverse and sharp supremum stability are not present
in the inspected #663 head. Both dossiers correctly leave the asymptotic
source estimate open.

## A further exact upgrade: L2 discrepancy exponent 1/5, with sharpness

The #663 estimate loses information by bounding each harmonic separately
before summing. A direct Cauchy–Schwarz application to the SAME energy
improves the exponent.

Let `g=L*(mu-m)` and `V=||g||_2^2`. Since g is real,

\[
V=2\sum_{h\ge1}|\widehat L(h)\widehat\mu(h)|^2.
\]

If `|Lhat(h)|>=c/h^2`, then for every H>=1,

\[
\sum_{h=1}^H\frac{|\widehat\mu(h)|}{h}
\le\frac{\sqrt V}{c}
\sqrt{\frac{H(H+1)(2H+1)}{12}}.
\tag{A1}
\]

Indeed use Cauchy–Schwarz on the factors
`|Lhat(h)muhat(h)|` and `1/(h|Lhat(h)|)`, then
`sum_(h<=H)h^2=H(H+1)(2H+1)/6`.

The same stated Erdős–Turán bound gives

\[
\boxed{D_{arc}(\mu)\le\frac3{H+1}
+\frac{3\sqrt V}{c}
\sqrt{\frac{H(H+1)(2H+1)}{12}}.}\tag{A2}
\]

Taking `H` proportional to `V^(-1/5)` gives `D=O(V^(1/5))`, improving
#663's `O(V^(1/6))`. For authentic rational shadow energy Vhat and source
tail epsilon_B, replace sqrt(V) by `sqrt(Vhat)+epsilon_B` in A2. A rational
upper square-root certificate makes the finite bound checkable. Our Fourier
bound permits `c=63/(289 pi^2)` or the rational floor `3087/139876`; #663's
weaker positive c also proves the improved exponent.

### Sharpness of 1/5 for circle probability measures

For an integer H>=1 set epsilon=1/H and define the positive probability

\[
\mu_\epsilon=m-1_{[-\epsilon/2,\epsilon/2]}dt
+\epsilon\delta_0.
\]

Every interval's signed error lies in [-epsilon,epsilon], and intervals
shrinking to 0 approach error epsilon. Thus `D_arc(mu_epsilon)=epsilon`.
For nu=mu_epsilon-m,

\[
\widehat\nu(h)=\epsilon(1-\operatorname{sinc}(\pi h\epsilon)),
\quad
|\widehat\nu(h)|\le
\min\left(2\epsilon,\frac{\pi^2h^2\epsilon^3}{6}\right).
\]

The quadratic bound uses
`1-sinc(t)=integral_0^1(1-cos(tu))du<=t^2/6`.
Our upper gain `|Lhat(h)|<=81/(289 pi^2 h^2)`, split at h=H, gives

\[
\begin{aligned}
V_\epsilon
&\le\frac{729}{167042}\epsilon^5
+\frac{17496}{83521\pi^4}\epsilon^5\\
&<\boxed{\frac{1161}{167042}\epsilon^5},
\end{aligned}\tag{A3}
\]

using `sum_(h>H)h^(-4)<1/(3H^3)` and pi>3. Consequently no uniform
`D_arc<=C V^beta` with beta>1/5 is possible: substituting this family would
require epsilon<=constant*epsilon^(5 beta) as epsilon tends to zero.

This is a sharp static observer-stability theorem. It does not yield decay
of V_B for the authentic BBP orbit. The source-specific arithmetic gap is
unchanged, and neither #663 nor this upgrade constitutes novelty-tax D/E.
