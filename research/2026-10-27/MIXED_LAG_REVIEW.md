# Independent hostile review of the moving mixed-lag theorem

**Review result:** the proof of
[MIXED_LAG_PERIODIC_COERCIVITY.md](MIXED_LAG_PERIODIC_COERCIVITY.md)
survived the checks below. The authority is a paper proof using the classical
finite irrationality exponent of π, with independent exact finite tests.
This review does not certify a numerical arithmetic onset, a Lean proof of
the analytic theorem, relative Fourier cancellation, or normality.

## 1. The periodic template is eliminated lawfully

Choose exactly periodic real representatives $\theta_t$ for the unit
template. With centered lifts

$$y_t=hX_t+\ell_t=\theta_t+\psi+q_t,$$

the branch $k_t=\ell_{t+1}-16\ell_t$ remains an integer. For transitions
in the same residue class modulo $p$, the terms
$\theta_{t+1}-16\theta_t-15\psi$ agree exactly. Their cancellation in a
branch comparison therefore does not assume rational template phases.
The first circle bound gives $Q=\sum_tq_t^2\le1/112$; it is used only to
justify the local cosine coefficient $19$. The stronger conclusion
$Q\le1/266$ then follows from $D\ge19Q$ and $D\le1/14$, and supports
the strict branch comparison. Each residue has at least $20000$
transitions when $m\ge4096p$.

Periodic integer branches have a unique periodic rational solution to
$f_{t+1}=16f_t+k_t$, with denominator dividing $16^p-1$. The final $p$
transitions compare equal template phases and equal values of $f$.
Consequently the rational approximation to π has denominator
$|H|(16^p-1)16^m$, without an untracked template parameter. This is the
step that a scalar Fourier estimate alone does not provide.

## 2. The large completed frequency has its full cost paid

For $P(E)=\prod_i(E^{\ell_i}-1)$ and $A=P(16)$, the exact original-source
identity is

$$P(E)U_n=A16^{n-1}\pi-P(E)T_n.$$

In the positive Green integral, each lag introduces a factor
$1-t^{8\ell_i}$ in $(0,1)$. Therefore
$0<(-1)^kP(E)T_n<T_n<1/(64n^2)$ for every finite tuple, uniformly in
its order and span. This proves the full infinite error bound
$11|h|/(112M)$ on $n>M$; no infinite-order interchange is required.
The absolute value on $h$ is essential, and is present in the implementation.

The comparison is with $A16^{n-1}\pi$, not with $AU_n$. The latter leaves
$AT_n-P(E)T_n$. A finite exact test detects this discarded exponential
counterterm on the original source, with start $3$ and lags $(7,13)$.

The completed orbit has zero forcing, so the earlier source-range condition
$|H|\le m^2/64$ is inapplicable. Its frequency cost instead enters the
Diophantine comparison. Writing $b=d+\lceil\log_{16}|h|\rceil$, the stated
requirements imply

$$m-15p-15b\ge\left(\frac34-\frac{15}{4096}\right)m>m/2.$$

Thus one universal, uncomputed arithmetic onset suffices for all periods,
lag tuples and frequencies in the declared schedule. The exact source
identity, rather than a changed initial condition, identifies the completed
orbit with π. A changed seed cannot silently pass that gate.

## 3. Independent finite evidence and rejected mutations

The independent test file is
[test_mixed_lag_coercivity.py](../../tests/test_mixed_lag_coercivity.py).
It uses a collapsed rational formula for the original forcing, direct
weighted sums for $U_n$, subset expansions for filter coefficients, and
literal differences of value lists for mixed moments. These are separate
finite derivations, not additional independent evidence for the analytic
irrationality theorem.

The holdouts include order $12$ at start $1$, order $8$ at start $17$, and
lags $(7,13,29)$ at start $31$. Every positive tail interval includes an
outward remainder for the entire infinite future. Longer enclosures nest
strictly inside the shorter ones. A separate finite-plus-future calculation
checks that the transport budget pays more than the sampled terms.

The tests reject a changed rational seed with unchanged forcing, a deleted
negative source pole, the zero-forcing orbit, and an integer-lift mutation
that preserves every evaluated circle character. They also check negative
frequencies, logarithm boundaries immediately around powers of $16$,
geometric block endpoints, the joint exponent margin, replay limits, and
the distinction between a supplied onset and a certified onset.

Executed locally:

```text
python -m unittest discover -s tests -p 'test_mixed_lag_coercivity.py' -v
Ran 14 tests in 0.040s
OK
```

No full repository suite, hosted CI, or Lean analytic kernel claim is made
by this receipt.

## 4. Novelty and unresolved scope

The positive mixed Green integral and completed-orbit transport were already
proved in
[BBP_RESONANT_LAG_DESCENT.md](../2026-10-25/BBP_RESONANT_LAG_DESCENT.md).
The finite irrationality exponent and scalar $1/14$ coercivity are also
inherited. The additional conclusion is the uniform signed bound after
allowing both periodic unit templates and moving mixed lag tuples.
Academic priority outside the inspected repository lineage is unverified.

The division by $N$ still gives an upper bound tending to one. Sparse-digit
finite-type controls are not eliminated by this logarithmic-loss mechanism.
General algebraic-number digit-complexity theorems cannot be substituted for
a π-specific estimate: their algebraicity hypothesis does not apply to π.
No fresh-prime or Galois average has been used as a selected-embedding
upper bound. A growing authenticated block loss, or a stronger signed
combination of blocks, remains necessary for normality.
