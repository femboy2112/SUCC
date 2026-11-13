# Coupled Wilson graphs: preserve the reflection before changing resolution

This continuation builds on **unmerged PR #613**, pinned at
`a8da424c84869d737462fdec0a64d7921a92eb50`. It also audits unmerged #614 at
`0faa85a798de5b0b9af4d62295f405165b408eb7`. Neither is silently treated as
part of main, whose verified head was `db9fb4b84672050efa79b13377f1e73364598a14`.

The external announcement is substantive: the November 10 assessment judges
the October 28 OpenAI submission to construct a four-dimensional Wightman
theory from Wilson lattice gauge theory. The assessment explicitly leaves
mass gap and infinite-volume uniqueness unproved. See
[the primary-source audit](UPSTREAM_SCOPE.md) for the narrower domain of each
formal adapter and the source-witness quantifiers. Our work here does not
reproduce or replace that continuum proof.

## What this continuation adds

The previous branch gives a one-plaquette construction and exact graph/matrix
and Haar interfaces. This branch retains **multiple plaquettes sharing the
same ordered link variables** and gives an explicit finite approximation
whose reflection behavior can be proved, rather than inferred from positive
probability weights.

1. [Exact coupled construction](CONSTRUCTION.md): for any fixed finite SU(2)
   graph with closed plaquette words, nonnegative rational couplings and a
   rational polynomial observable, a terminating rational calculation gives
   its Wilson expectation to any positive rational tolerance. The procedure
   uses actual compact SU(2) Haar moments, not a finite subgroup surrogate.
2. [Reflection and order](REFLECTION_ORDER.md): a global polynomial truncation
   can destroy reflection positivity at every finite order despite positive
   weights and convergence. Factorwise character-positive truncations repair
   this under a declared reflection split. With independent halves and fixed
   or absent boundary variables, the reflected kernel has a finite feature
   representation and therefore a finite-dimensional OS quotient.
3. [Gauge-relative observer](TRACE_OBSERVER.md): ordered single, pair and
   triple SU(2) traces determine a connected finite graph's gauge orbit after a tree
   gauge choice. Pairs alone can miss orientation. A nondegenerate anchor
   triple gives a quantitative inverse bound, with the conditioning loss
   retained. Completeness is classical invariant theory, not a new priority
   claim.
4. [Bounded formal replay](FORMAL_REPLAY.md): fresh upstream integrity checks,
   an actual Lean proof-transport replay and hostile mutation, and a small
   rational reflection countercertificate. These are explicitly bounded;
   the full Yang–Mills endpoint and Comparator pipeline were not rebuilt.

## The approximation that respects the source

Write `x_p(U)=Re(holonomy_p(U))`, so `|x_p|<=1`, and let

\[
w(U)=e^{\sum_p\beta_p x_p(U)},\qquad
w_{\mathbf K}(U)=\prod_p P_{K_p}(\beta_p x_p(U)),
\quad P_K(t)=\sum_{j=0}^K t^j/j!,
\]

where every `K_p` is even and every `beta_p>=0`. Both weights are strictly
positive. They use exactly the same graph and shared links. For any bounded
observable `|f|<=M`, with `S=sum beta_p`,

\[
\left|\frac{\int fw}{\int w}-\frac{\int fw_{\mathbf K}}{\int w_{\mathbf K}}\right|
\le 2M\,3^{\lceil2S\rceil}
\sum_p\frac{\beta_p^{K_p+1}}{(K_p+1)!}.
\]

For polynomial quaternion observables all integrals on the approximation side
are rational. Factorial decay proves termination at fixed graph and couplings.
The displayed dependence on `S`, the number of plaquettes and `M` is part of
the result: it is not an unproved uniform continuum estimate.

## The exact failure that chose the better construction

Take two reflected independent SU(2) holonomies with scalar traces `x,y`.
The Wilson weight `exp(x+y)` factorizes and is reflection positive. The
strictly positive global approximation

\[
Q(x+y)=\left(1+\frac{x+y}{2}+\frac{(x+y)^2}{8}\right)^2
\]

has partition `645/512`. On tests `1,U_4(x)`, its normalized reflected Gram
matrix is

\[
\begin{pmatrix}1&1/1290\\1/1290&0\end{pmatrix}.
\]

Thus `1-1290 U_4(x)` has reflected squared norm **-1**. Every ingredient is
exact rational arithmetic. The general top-degree orthogonal-polynomial
argument explains why the defect persists at higher polynomial orders.
The offending test moves with resolution, so this does not refute convergence
on each fixed bounded test. The repair keeps the plaquette factorization and
its nonnegative character coefficients before performing the approximation.

## How this answers the SUCC/QM question

| Existing SUCC structure | Exact connection | Remaining condition |
|---|---|---|
| Successor paths on the half-line | `J=(S+S*)/2` represents the normalized SU(2) trace by Chebyshev character fusion (#613) | This trace observable is not the Yang–Mills Hamiltonian |
| Computational graphs | Finite path sums represent matrix composition, tensor product and adjoints over the declared coefficient field (#613) | The Hilbert metric, null quotient and source state must accompany the graph |
| Haar coarse/detail transforms | Full transforms preserve the source metric and all transported observables (#613) | Keeping only the coarse component is a different operation |
| Coupled Wilson polynomials | Ordered quaternion paths and exact compact Haar integration evaluate shared-link polynomial moments | No independent-plaquette substitution |
| Reflection-positive finite features | Reflected sums of squares give an actual positive Hilbert quotient | Time evolution and a physical Hamiltonian require further compatible maps |
| Three-channel observers | Triple traces recover orientation invisible to pairs | Inverse stability worsens near a degenerate anchor |
| Source-conditioned comparison | The upstream combined endpoint uses one Wilson family and shared witnesses | A representation match does not supply missing renormalization bounds |

These are literal mathematical interfaces within their stated domains. The
finite graph perspective earns a quantum Hilbert-space construction where the
reflection proof applies. It does not become four-dimensional QFT merely
because its notation resembles a path integral. Group Haar measure and a Haar
wavelet basis have different roles; the source law determines the metric in
which a wavelet change of coordinates is unitary.

No theorem about the BBP zero-seeded orbit, pi normality, RH or a Yang–Mills
mass gap is imported through this dictionary. A further application must bind
its own source, observables and limiting estimates. In particular, the
finite trace bank is complete for a configuration modulo gauge, not an oracle
for the statistics of an entire continuum probability law.

## Next decisive strike

Take a specified reflection-compatible lattice family and renormalized
positive-time observables from the same Wilson construction. Choose the
factor degrees as functions of the lattice spacing and volume. Prove that
the displayed expectation error tends to zero while controlling the observable
norms and reflection support, then identify those limits with the chosen
upstream hierarchy. A pass supplies a certified finite computational graph
approximation to that hierarchy. Failure of a uniform bound leaves this finite
theorem intact and exposes the exact extra renormalization estimate needed.

For a gap, an additional uniform physical-time exponential decay bound is
still necessary on a dense vacuum-orthogonal family. The existence result and
the finite Hilbert quotients do not provide it.

See [protocol](PROBE_PROTOCOL.md), [claim ledger](CLAIM_LEDGER.md), and
[validation](VALIDATION.md). Same-family agent cross-checks are not external
independent verification. No worldwide novelty is claimed for classical
representation theory, Haar moments or reflection-positive character kernels.
