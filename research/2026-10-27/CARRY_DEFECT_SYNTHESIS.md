# Beyond one Fourier sum: periodic observers and moving mixed lags

**Research continuation of PR #317, UTC 2026-10-27.**
The original four-pole source, $U_0=0$, and complete lifted histories remain
unchanged. **π normality is OPEN.** This round improves the scope of the
signed theorem, rather than optimizing its $1/14$ coefficient again.

## The strongest new source theorem

Let $P(E)=\prod_i(E^{\ell_i}-1)$ for any nonempty tuple of positive integer
lags, and put $d=\sum_i\ell_i$. For every fixed $h\ne0$ and $0<\delta<1$,
uniformly over all periods $p$ and all lag tuples with $p+d\le N^\delta$,

$$
\boxed{
\sum_{a=0}^{p-1}
\left|\sum_{\substack{1\le n\le N\\n\equiv a\pmod p}}
e(hP(E)U_n)\right|
\le N-\frac{1-\delta}{14}\log_8N+O_h(1).
}
$$

The proof gives an all $N$ schedule and exact rational transport error with
one universal but uncomputed arithmetic onset. The sum of residue moduli
is the supremum over every period $p$ unit template, including a template
selected after seeing the observations. Each eligible geometric block may
even use its own optimizing template. Mixed-difference order may grow with
$N$, and the resulting completed frequency can be exponential in $N^\delta$.

This is a stronger source-authentic signed theorem than the previous bound
on a single ordinary Weyl sum. It does not improve the logarithmic order:
the normalized upper bound still tends to one. See the full
[joint theorem and proof](MIXED_LAG_PERIODIC_COERCIVITY.md).

## Why the extension works

**Periodic integer rigidity.** Very small template-weighted phase loss gives
one quiet transition in every residue class. Within each class the arbitrary
template phases cancel exactly, forcing an integer branch pattern of period
$p$. Its unique rational periodic solution has denominator $16^p-1$.
The last $p$ transitions remove the template from the endpoint correction.
The exact zero-selected Green identity then produces a rational approximation
to π that the published irrationality measure excludes. This gives the
[simultaneous periodic theorem](PERIODIC_TEMPLATE_COERCIVITY.md).

**Order-independent tail control.** Each mixed lag multiplies the positive
Green integrand by $1-t^{8\ell_i}\in[0,1]$. Thus its entire signed tail
has magnitude at most $T_n$, however large the order or span. Comparing
with the completed orbit at frequency $hP(16)$ costs at most
$11|h|/(112M)$ over the entire future $n>M$. The frequency's large size is
paid separately in the Diophantine denominator. Comparing instead with
$P(16)U_n$ would introduce an exponentially large error; an exact source
holdout detects that shortcut.

The positive mixed integral and scalar coercivity are inherited facts.
The new result combines them with periodic integer rigidity and a uniform
completed-frequency schedule. Their agreement is not counted as multiple
independent constraints. Academic priority outside the inspected repository
is not asserted.

## A finite arithmetic instrument, with its exact limit

For any rational source history, enumerate the finitely many cuts at which
centered phase lifts change. The actual integer branch word is constant
between cuts. An exact nonmodal-count minimum gives

$$D\ge\frac4{289}(1-R)^2K_{\min}\qquad(0\le R<1).$$

Here $R$ is the frequency-scaled forcing range and $K_{\min}$ is computed
from all cut branch words; no complex resultant has to be guessed.
A stronger unequal-pair bound and the complete signed inverse Green kernel
retain cross terms and the homogeneous boundary direction $16^i$.

The full kernel minimization is exactly circular quadratic variance.
Circle averaging proves it cannot certify more than $2L/3$ loss on $L$
observations, even when the true Fourier sum vanishes. That is a proved
instrument limitation, not a claim that the authentic source has such a
limit. The [instrument dossier](CARRY_DEFECT_ENERGY.md) states this boundary
and the still-unproved arithmetic growth condition on the selected counts.

## Controls, authority and next obligation

The same-forcing control $V_n=-T_n$ has bounded loss for every fixed mixed
lag tuple and constant observer. It fails the original zero selector at
the precise Diophantine identification step. Periodic rational controls,
integer-lift-preserving circle mutations, a missing negative pole, and a
discarded homogeneous boundary are tested separately. Finite irrationality
type alone still permits sparse-digit nonnormal controls, so no normality
claim is inferred from these logarithmic estimates.

The analytic theorems are **PAPER-PROVED with CLASSICAL input**. Exact
integer/Fraction tests and full-source outward tail intervals are finite
authority. Four small finite algebraic/count declarations have a separate
Lean receipt; the analytic theorem is not kernel-checked.

The next source-specific statement must force growing loss inside these
blocks or control their signed combination. A finite carry count or an
optimized positive quadratic representation does not discharge that step.
The stronger moving-lag theorem is now available as a proved input, with
all parameter dependence paid.

See [the scoped ledger](../../docs/CLAIM_SUPPLEMENT_CARRY_DEFECT.md),
[independent hostile review](MIXED_LAG_REVIEW.md), and
[validation receipt](CARRY_DEFECT_VALIDATION.md).
