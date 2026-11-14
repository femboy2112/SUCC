# Geometry and defect workstream: proof and provenance receipt

**Date:** 2026-11-13 (America/New_York).
**Files owned:** docs/principia_observatoris/02_causality_geometry.md and this receipt.
**Scope:** finite-dimensional source-relative observation; no physical experiment,
formal-kernel run, or academic novelty claim.
**Status:** paper derivations complete; root-owned executable and repository
validation have separate receipts.

## Source reconstruction

Read AGENTS.md, docs/METHOD.md, all nine sections of the PR #618 note,
docs/CLAIM_SUPPLEMENT_BOUNDARY_PORT_GEOMETRY.md,
docs/CLAIM_SUPPLEMENT_OBSERVATION_PINNED_GEOMETRY.md, and targeted source
passages in the boundary-port implementation, complete BPGS dossier,
carrier-relative targets, and Principia ancestral supplement. The action descent
criterion is already BPGS-09. It is reused as a theorem interface, not claimed
as a discovery. The OPIG counterexample already prevents metric uniqueness from
topology; this book keeps that boundary.

## Hole contract and result

**Proposed statement.** Given finite-dimensional source actions and a present
linear readout, construct the smallest linear refinement admitting exact
prediction under every finite action word, and quantify the unavoidable error
when no refinement is available.

**Hypotheses.** Known finite-dimensional linear source laws, a field for the
algebraic theorem; a calibrated Hilbert norm and symmetric ball/fiber prior for
the quantitative optimal-recovery result. Obtaining the refined coordinates
through lawful interventions is a separate access problem.

**Weakest useful form.** Kernel invariance characterizes exact closure.
Hidden-fiber target radius quantifies error without reconstructing the carrier.

**Dependency edges closed.** Present observation to closure obstruction to
minimal predictive refinement; indistinguishable hidden perturbations to exact
worst-case target error.

**Novelty tax.** Classical quotient linear algebra, observable-subspace
construction and optimal recovery supply the mathematical ingredients. The
new-to-this-manuscript gain is their explicit joint interface, exact certificates,
and retained policy/source-adequacy gap. These do not disguise a π-normality
estimate or claim an entirely new branch of mathematics already exists.

**Cheapest falsifiers.** A two-dimensional nilpotent shift, the signed four-node
diamond, and a scalar two-step cancellation. They kill stronger statements
without expensive computation.

**Finite boundary.** Exact finite rational examples check implementations.
The universal finite-dimensional statements have paper proofs. No theorem
identifies an unknown real-world source from a fitted matrix.

## Theorems, obligations, and implementation cases

| ID | Exact content | Antecedent/status | Discriminating case |
|---|---|---|---|
| CG-01 | Finite chain-rule response transport | Classical; proved by induction | \(a^2\) at zero and \(|a|\) at zero refute derivative sufficiency/existence |
| CG-02 | \(PA=BP\) iff \(PA|_{\ker P}=0\) | BPGS-09 linear specialization | \(P=[1,0]\), \(A=[[0,1],[0,0]]\): hidden \(\pm e_2\) yield next outputs \(\pm1\) |
| CG-03 | Over all predictors, exact unit-ball error \(=\|F\Pi_{\ker P}\|\) | Classical optimal recovery; full proof | Same shift gives error 1; diagonal source gives zero next-readout error |
| CG-04 | Row closure stabilizes by \(n-\operatorname{rank}P\), gives unique minimal row-space refinement | Classical observable-subspace extension to an action family | Superdiagonal shift attains bound for every \(1\le r\le n\) |
| CG-05 | Typed telescoping identity and norm bound for defects | Classical algebra; full proof | Scalar \(A_1=A_2=1,\ B_1=B_2=-1\): both local defects 2, final defect 0 |
| CG-06 | Defect conjugacy and transported-norm invariance | Classical linear algebra | Rescale hidden/input coordinates; rank and vanishing stay invariant, naive Euclidean sizes do not |
| CG-07 | Vertical derivative test gives descent on connected smooth/convex fibers | Classical calculus consequence | \(q(x)=x^2,\ F(x)=e^x\) on \(\mathbb R\setminus0\): tangent test vacuous, disconnected fibers disagree |
| CG-08 | Declared response bank induces a behavior pseudometric; countable weighted version induces its initial topology | Classical metric construction | Empty bank has zero distance everywhere; more instruments refine zero classes |
| CG-09 | Earliest response equals graph distance for nonnegative linear propagation | Classical walk expansion | Signed diamond has two paths and zero net response, violating a proposed latency triangle inequality |
| CG-10 | A prescribed actual record \(H_tx_0\) identifies current predictive coordinates \(QM_tx_0\) iff \(\ker H_t\subseteq\ker(QM_t)\) | Target descent specialization; paper proof and conservative noise bound | Swap reveals initial hidden coordinate; erasure identifies current state while losing initial history |
| CG-11 | For a fixed initial linear target on the entire Hilbert ball, deterministic adaptive worst-case acquisition error equals the best feasible fixed-schedule radius | Classical adaptive optimal-recovery consequence; full zero-run proof and finite rational decision certificate | Symmetric seven-state nonconvex prior has adaptive error 0 and best fixed error \(1/4\) |

Additional exact non-coordinate row example for CG-03:

\[
P=[1,1],\quad A=\operatorname{diag}(1,2),\quad
P^\dagger=\tfrac12(1,1)^T,\quad B_*=\tfrac32,
\quad PA-B_*P=(-\tfrac12,\tfrac12).
\]

The squared optimum is \(1/2\). A rational arithmetic test can check that
residual row and its squared Euclidean norm without approximating a square root.

For the sharp CG-04 example \(n=4,r=1\), the successive ranks are \(1,2,3,4\).
For a two-action holdout, take \(P=e_1^T\), let \(A_a\) have only entry
\((1,2)=1\), and \(A_b\) only entry \((2,3)=1\). The observed row span gains
\(e_2^T\) and then \(e_3^T\). Testing either generator alone misses the
two-action hidden pathway. This uses standard one-based matrix indices.

CG-10 acquisition controls: use \(P=[1,0]\), source action alphabet consisting
of swap \(S=[[0,1],[1,0]]\) and erasure \(D=\operatorname{diag}(1,0)\), so
\(Q=I_2\). After swap, \(H_1=I_2\), current target \(F_1=S\) is identified.
After erasure, \(H_1=[[1,0],[1,0]]\) and \(F_1=D\): current target identified,
initial target \(I_2\) not identified. The target radius formula is exact without
noise; the added \(\epsilon\|F_tH_t^\dagger\|\) term is only an upper bound
under bounded record noise.

CG-11 predeclared adversary: replace the entire ball by
\(\{0,\pm u,\pm v,\pm w\}\), where
\(u=(0,1/2,0),v=(1/2,0,0),w=(1/2,0,1/2)\), append a zero readout buffer,
and allow unit-cost coordinate-to-buffer queries. At budget two, adaptive
first-coordinate then branch-selected query identifies all seven states;
every fixed pair leaves an ambiguity, and best fixed error is exactly \(1/4\).
This deliberately fails the full-ball hypothesis while preserving linear
actions, symmetry, the norm bound, fixed initial target and exact readout.

## Primary-source audit

- [Boyd–Lall, Observability and state estimation](https://ee263.stanford.edu/lectures/observ.pdf), retrieved PDF, slides 4–7: observability matrix, null-space ambiguity, and finite closure via Cayley–Hamilton. It is an antecedent for the one-action specialization, not a cited proof of every switched-action assertion here.
- [Boyd–Lall, Autonomous linear dynamical systems](https://ee263.stanford.edu/lectures/lds.pdf), retrieved PDF, slides 16–20: conditional linearization and examples of different dynamics with the same first-order linearization.
- [Foucart–Liao, Radius of Information for Two Intersected Centered Hyperellipsoids](https://foucart.github.io/publi/OR_L1Noise_v2.pdf), retrieved PDF, §1 and Lemma 2: general optimal-recovery formulation and the classical symmetric-pair lower bound. Only the elementary ball case is used and independently proved.
- [Lawvere 1973, official reprint metadata](https://www.tac.mta.ca/tac/reprints/articles/1/tr1abs.html), metadata returned by search: directed metric/enriched category antecedent. Direct PDF and later page fetches returned 502 errors; no uninspected detailed theorem is assumed.
- [Novak, Some Results on the Complexity of Numerical Integration](https://users.fmi.uni-jena.de/~novak/novak2.pdf), Theorem 0; [Krieg–Kritzer, Homogeneous algorithms and solvable problems on cones](https://www.ricam.oeaw.ac.at/files/reports/23/rep23-30.pdf), Introduction: both retrieved as PDFs. They establish the classical antecedent and warn against silently extending factor-one nonadaptive optimality to arbitrary vector-valued/convex-class problems.
- [Bakhvalov 1971, journal metadata](https://www.mathnet.ru/eng/zvmmf6826), original attribution checked; full Russian text not used as a proof dependency.

Proofs were derived before the optimal-recovery literature lookup. The lookup
explicitly confirms a classical antecedent, so the radius statement is not
promoted to novel mathematics.

## Hostile review and corrections

A separate same-model workstream audited CG-02–CG-09 and the nonlinear-predictor
minimax strengthening, reporting no mathematical counterexample under the
stated assumptions. This is role-separated review, not external peer review or
independent-model evidence. It caught damaged inline LaTeX escaping in the first
file write. The escaping was repaired, with matched delimiters and restored
commands/norms; the mathematical claims were unchanged. The sharp closure
example was expanded from rank one to every positive initial rank.

A second review required explicit linearity types, nonnegative fiber radius,
an empty-bank convention, and the distinction between factorization into the
observed ambient space and an effective selfmap of the observed domain. These
were made explicit before publication.

The CG-10 noisy-record formula was additionally repaired to specify the ambient
Moore–Penrose inverse, extended by zero off the exact-record image. Otherwise
an arbitrary additive noise vector could put the inverse outside its declared
domain. CG-11's finite rational witness scaling is explicitly Euclidean.

CG-11 received a further same-model hostile proof audit and survived under its
stated assumptions. The geometry workstream replayed the independently written
adaptive_linear_probe.py successfully: 13 fixed schedules on seven rational
prior states give minimum squared error \(1/16\), while the adaptive policy
identifies all seven targets exactly. Its nonlinear-action, state-dependent-cost
and randomized-expected-squared-loss controls also passed. The output records
their scopes separately; none is treated as a universal numerical proof.

Potential overclaim removed: \(d-r\) counts extra predictive coordinates. It
does not by itself count memory cells that a one-copy observer can fill.

## Next lamp

CG-10 resolves exact acquisition for one prescribed schedule. CG-11 resolves
deterministic adaptive acquisition for a fixed initial linear target on the
entire Hilbert ball by reduction to fixed schedules, with finite rational
certificates under positive costs. The unresolved constructive edge outside
those hypotheses is synthesis of an executable, disturbance-aware policy
for obtaining enough of the minimal predictive refinement. Formal all-word
separation can coexist with no successful one-carrier policy. A theorem
characterizing accessible sufficient subspaces under a typed instrument family
would most change this layer.
