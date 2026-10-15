# OPERATION ORDINAL II — Probabilistic epochs, infinite expected path lengths and the TRUE Tate source chart

**Date:** 2026-10-15. **Source branch:** research/ordinal-ranked-succ-goodstein-2026-10-15, stacked on ATOM II PR #118 head 8ce326b28ed0b4a86d4f51c9a6923c507c06a947; Phoenix II main unchanged. **RH PROVED: NO.** Theorems are classical well-founded induction, elementary probability and p-adic Schwartz–Bruhat/Fourier geometry. Synthesis/application is new-to-this-research-branch, scholarly novelty unverified.

## I. A theorem that actually unifies ordinal SUCC progress and ranking supermartingales

A sequence of SUCC observations may include arbitrarily many stochastic RETRIES that do not change its ordinal rank. Requiring strict ordinal descent at every physical tick is too strong for almost-sure termination.

Let S be a countable (or suitably measurable) source state space with an absorbing terminal subset T. Fix a rank \(\rho:S\to\alpha\) into a well-order \(\alpha<\varepsilon_0\) (or any genuine well-order), and assume every state of rank zero is terminal. The next transition is source-measurable and may stay at the same rank or move to a STRICTLY smaller rank; no transition ever increases \(\rho\).

**Source progress hypothesis:** At every nonterminal state and after any permitted history at unchanged rank, the conditional probability that the *next* step strictly decreases \(\rho\) is at least a fixed rational p>0. This is a conditional source law; it does NOT follow from observing finitely many successes.

For each epoch begun at rank β>0, conditioning successively on no rank decrease gives
\[
\boxed{\Pr(\text{no strict descent during first }n\text{ retries}\mid \mathcal F_{\mathrm{epoch}})
\le(1-p)^n.}
\tag{OE-1}
\]
The bound tends to zero, so a strictly smaller rank is reached eventually almost surely.

**Ordinal–martingale termination theorem (CLASSICAL/PROVED conditional on declared source law):**
\[
\boxed{
\text{uniform conditional hazard}
+
\text{no rank increases}
+
\text{strict ordinal decrease on progress}
\ \Longrightarrow\
\Pr(\tau_{\mathrm{terminal}}<\infty)=1.
}
\tag{OE-2}
\]
**Proof:** Transfinite induction on β. Rank zero is terminal. Suppose all source states with ranks <β terminate almost surely. By OE-1 the first progress epoch at β ends in finite time almost surely. Conditioned on its terminal state of rank γ<β, the transfinite inductive hypothesis applies, so the entire run terminates a.s. The set of failed-progress epochs is a countable null union under the declared laws. This is a mathematical theorem about source-conditioned processes, NOT a pathwise sure-termination assertion: an infinite sequence of unchanged-rank retries may exist as an admissible graph path with probability zero.

A slightly broader sufficient law is a history-valid conditional hazard sequence \(p_n\), for which \(\sum_n p_n=\infty\), since \(\prod_n(1-p_n)=0\) under the usual product bound. The code implements the simpler fixed-p source theorem with exact rational finite-time tails.

**Sharp negative control:** Merely saying each finite attempt has positive chance of progress is insufficient. Choose independent hazards \(p_n=2^{-(n+2)}\). Then \(\sum_n p_n=1/2\). Bernoulli's product inequality gives
\[
\Pr(\text{no progress forever})
=\prod_{n\ge0}(1-p_n)
\ge1-\sum_n p_n=\tfrac12>0.
\tag{OE-3}
\]
Thus a beautifully descending rank ONCE PROGRESS OCCURS cannot prove almost-sure termination if the source can stutter forever with positive probability. Exact Fraction code computes every declared finite survival product and independently verifies the analytic uniform lower bound.

This is a meaningful **source/observer/martingale/ordinal composition law**, but it is a classical transfinite termination argument, not a new theorem about the Riemann zeros.

## II. Sure ordinal termination need not provide finite expected runtime

Here is a load-bearing result for the user's idea of ridiculously long normal paths. Start at rank \(\omega\) and choose a NATURAL number n>=0 with declared source probability
\[
\Pr(N=n)=\frac1{(n+1)(n+2)}.
\]
The distribution sums to 1 because it telescopes. The first transition is \(\omega\to n\), a STRICT ordinal rank decrease. Every subsequent step counts down n→n−1→...→0. Thus **every possible sample path** is FINITE, with exact length \(\tau=n+1\). No stochastic exceptional infinite path exists in this source graph.

But
\[
\boxed{\Pr(\tau>h)=\frac1{h+1},
\qquad \mathbb E\tau=\sum_{h\ge0}\frac1{h+1}=\infty.}
\tag{OE-4}
\]
This is genuine infinite branching at the initial ordinal state. There is no uniform finite natural bound on path length, and even its source expectation diverges, despite strict descent on EVERY edge. The code independently checks finite mass, exact tail and harmonic partial sums with rational arithmetic. It never attempts to simulate an infinite expectation.

**Verdict:** “proof that all source paths terminate” and “finite computational expectation / bounded normal path length” are separate tasks. Infinite expected work is not evidence that a global mathematical witness fails to exist, nor that RH is hard in precisely the same way.

## III. Exact \(2^{256}\)-milestone stochastic SUCC normalizer (PROVED synthetic)

Take the hierarchical finite protocol already certified in OR-03 with base R=2^128 and initial digits (1,0,0). The deterministic source milestone count is exactly N=R²=2^256, ranked by ω² before its first transition.

At each nonterminal milestone, use a declared independent geometric(p) retry law. The natural remaining-milestone potential V is a NONNEGATIVE ranking supermartingale:
\[
\mathbb E[V_{t+1}\mid V_t>0]=V_t-p.
\]
Consequently the total expected number of RETRY steps is exactly
\[
\boxed{\mathbb E \tau=\frac{N}{p}}
\]
for any rational p∈(0,1]; at p=1/2 it is \(2^{257}\). Termination is a.s., yet for p<1 there are exceptional graph paths of endless stuttering. No \(2^{256}\)-step trace was executed and none was smuggled into an exact observable.

This example has an additional natural-number countdown potential V, so the ordinal rank is not strictly NECESSARY for its termination. Its mathematical value is that the higher-level ordinal method generalizes to source protocols whose lower obligations can grow arbitrarily with no similarly simple natural-time potential.

## IV. SOURCE-TYPED Tate application: actual two-axis p-adic normalization

The most useful arithmetic use of the technique is not Goodstein itself, but SUCC's already valid Tate-local finite-chart system.

For a genuine p-adic Schwartz–Bruhat source function in a chart
\[
X_{p;r,s}=p^{-r}\mathbb Z_p/p^s\mathbb Z_p
\]
suppose an observer is instructed to produce a fixed, LAWFUL finer chart \(X_{p;R,S}\), with R>=r and S>=s. The existing Tate source has two actual refinement transformations:
- SUPPORT growth r→r+1, inserting old cells in the larger support by source-preserving zero extension;
- PRECISION growth s→s+1, replicating old values into narrower congruence cells.

Define the fixed-target rank
\[
\boxed{\rho(r,s\mid R,S)=\omega(R-r)+(S-s).}
\tag{OE-TATE}
\]
Every legal support refinement decreases the HIGH \(\omega\)-term; every precision refinement decreases the finite term. Both are strictly descending source transitions. Thus all such fixed-target normalization schedules terminate in at most (R−r)+(S−s) transitions; the SOURCE law also provides the natural bound in this simple instance. Each intermediate source chart is an actual finite Tate mathematical object, not an artificial positivity matrix.

The terminal source value-table is independent of the order of refinements: SUPPORT then PRECISION equals PRECISION then SUPPORT, by the existing exact two-axis Tate diagram. The same is true of the terminal Fourier coefficients with the genuine p^-s additive Haar normalizations and original cyclotomic phase. The dedicated module tate_ordinal_chart_normalizer.py executes both orders, checks strict ordinal rank descent, preserves the exact original source table and verifies the actual local Fourier square.

**Cofinal tower no-go (CRUCIAL):** after a fixed target (R,S) has been completed, extending the target to (R+1,S) creates a NEW obligation of rank \(\omega\) even though the old proof finished at rank 0. This is NOT one globally decreasing ordinal computation completing *all* Q_p Schwartz functions in finite time. The source space itself is an unbounded filtered union; completion on each requested chart is finite, while its full universal theorem comes from a separate algebraic/analytic exhaustion proof.

Therefore **ordinals certify local observer normalization without laundering an infinite cofinal Tate construction into one finite experiment**. This is exactly the source/target/toolkit distinction developed in ATOM II.

## V. Connection to Weil/Suzuki—what is still required

The original completed Weil form \(W_\zeta\) is signed and RH positivity is all-test/global. A recursive source-correct Schur proof might generate enormous subordinate source/Gamma/prime-window tasks; an ordinal \(\omega^2 H+\omega M+L\) could prove termination if every corresponding source transformation STRICTLY decreases it.

However ordinal or stochastic termination alone cannot alter the inertia of a true signed operator under invertible congruence. In the exact rational control \(G=\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}\), rank-descending completion of squares leaves the negative pivot \(-3\). The actual original Suzuki low 30 Schur sign is likewise still unverified in PRs #107/#109/#116. **No ordinal measure has been derived from the AUTHENTIC prime/Gamma/contact operator that forces a positive terminal sign.**

The next proof-bearing target is **not** a larger finite trace: construct a well-founded SOURCE-SPECIFIC reduction on the actual signed low/high Schur residual (and its infinite analytic error terms), prove every source step maintains equivalence of the completed Weil form, then independently show its terminal canonically reduced source is positive. If probabilistic searches are introduced, they additionally require a source-authenticated uniform/divergent-hazard theorem; model-generated martingales cannot imply zeta arithmetic positivity.

## Status and literature

- OE-1/OE-2 source-hazard + ordinal milestone almost-sure termination: CLASSICAL/PROVED conditional theorem.
- OE-3 positive-but-summable hazard fails almost-sure termination: PROVED exact countermodel.
- OE-4 \(\omega\)-ranked sure finite paths with infinite expected length: CLASSICAL/PROVED exact probability source law.
- OE-5 \(2^{256}\)-milestone geometric normalizer and exact expected \(2^{257}\): PROVED synthetic source.
- OE-TATE actual p-adic fixed-chart ordinal rank/commuting Fourier diagram: CLASSICAL/PROVED source-typed, bounded exact original-chart computations.
- All-target Tate-global construction in one finite descending normalizer: REFUTED as inference; changing targets restarts rank.
- Original source signed Weil/Schur global positive normalization and RH: **UNVERIFIED. RH PROVED: NO.**

References:
- Ordinal source all-path Goodstein: Kirby–Paris 1982 DOI https://doi.org/10.1112/blms/14.4.285; Rathjen https://arxiv.org/abs/1405.4484 .
- Ranking supermartingale termination (different from source-evidence LR martingales): Agrawal–Chatterjee–Novotny https://arxiv.org/abs/1709.04037 ; Chatterjee et al. https://arxiv.org/abs/2108.02188 .
- Existing project source: tate_observer_completion.py with actual PadicBruhatChart, exact Fourier/Plancherel/support/precision squares; ordinal_succ_report.py with source-real formal ω colimits; heuristic_evidence_martingales.py with *evidence*, not *termination*, martingales.
