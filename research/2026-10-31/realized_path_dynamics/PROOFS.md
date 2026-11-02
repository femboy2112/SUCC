# Exact realized-path theory and authenticated BBP Hamiltonian band

**Authority:** classical finite path probability/Doob transforms, Gibbs variational algebra and symplectic affine dynamics, with paper-proved specializations to the literal original BBP four-pole source. Finite exact tests independently corroborate implementations; no Lean kernel or external refereeing; no novel physical quantum, GR, entropy-production or π-normality theorem.

## 0. Declared types and SOURCE firewall

The unchanged BBP rational forcing and zero-seeded trajectory are

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

For every integer horizon N this uniquely determines all real/rational states `U_0,...,U_N` and the ordered matrices `F_N...F_1`. It carries NO nontrivial conditional path law or entropy merely by being deterministic.

A separate **virtual finite path carrier** consists of a rooted time-indexed directed automaton (finite reachable histories), exact rational transition priors `p_t(e|history)>0` summing to one, nonnegative integer edge costs `c_t(e)`, a declared terminal goal `G`, and a discount `lambda in (0,1)`. The automaton's histories may share a coarse visible endpoint while differing in future transitions. The weighted Gibbs law is inferred from this DECLARED reference; it is not an intrinsic extra physical law of the real BBP orbit.

Keep distinct: (i) the realized discrete history, (ii) positive probabilities and costs, (iii) canonical symplectic momentum on real phase space, (iv) complex signed characters `exp(2πihU_n)`, (v) a candidate stochastic/quantum path integral. Only explicit maps can relate these objects.

## RP-01 — Actualization is normalized conditioning, with a precise information bill (CLASSICAL)

Let `R` be any finite probability law on paths and `eta` a realized prefix with `R([eta])>0`. The virtual field after observing eta is exactly

\[
R_\eta(\gamma)=\frac{R(\gamma)\mathbf 1_{\{\gamma\supset\eta\}}}{R([\eta])}.
\]

If a second decision `e` occurs, the *incremental realized surprisal* is

\[
I(e|\eta)=-\log R(e|\eta)\ge0,
\quad I(\eta e)=I(\eta)+I(e|\eta).
\]

The relative entropy (information gained from the event itself) satisfies the exact KL identity

\[
D(R_\eta\Vert R)=\log\frac1{R([\eta])}.
\]

Proof: wherever `R_eta` is positive, `R_eta/R=1/R([eta])`, a constant, so expectation of its log is this log. This is information-theoretic, NOT a proof of physical heat/energy production or quantum wavefunction collapse. Conditional Shannon entropy of remaining futures is NOT monotone in each realized outcome. Counterexample: root A/B fair; A has 8 equally likely completions and B one. Prior total-path entropy is `1+(1/2)log_2(8)=5/2` bits, while after realizing A the remaining future entropy is 3 bits, an INCREASE. The actual prefix surprisal is still exactly 1 bit.

A physical intervention may also alter the transition law; that is a NEW declared controlled dynamics, not merely Bayesian conditioning. The recorded outcome alone does not entail backaction on an unchanged external arithmetic source.

## RP-02 — Entropy-regularized geodesic and source-dependent future potential (CLASSICAL)

For finite admissible paths ending in G, reference path law R, additive declared cost `C(gamma)=Σ_e c(e)`, inverse temperature beta>0 and lambda=`exp(-beta)`, define

\[
Z=\sum_{\gamma:\,\mathrm{end}(\gamma)\in G}R(\gamma)e^{-\beta C(\gamma)},\qquad
Q_*(\gamma)=\frac{R(\gamma)e^{-\beta C(\gamma)}\mathbf1_G}{Z}.
\]

For ANY probability Q supported on admissible target paths and absolutely continuous w.r.t. R,

\[
\boxed{\mathbb E_Q C+\beta^{-1}D(Q\Vert R)
=-\beta^{-1}\log Z+\beta^{-1}D(Q\Vert Q_*)}.\tag{V}
\]

This follows by substituting `log(Q/Q*)=log(Q/R)+beta C+log Z`, so the unique minimizer is Q*. It is the KL/entropy-regularized version of a path geodesic; the cost and reference prior are declared inputs and must not be inferred from an attractive analogy.

For a (possibly history-augmented) state s at time t, define desirability by the backward recursion `H_T(s)=1_{s in G}`, and

\[
H_t(s)=\sum_{e:s\to s'}p_t(e|s)e^{-\beta c_t(e)}H_{t+1}(s').
\]

Then the normalized *Doob-selected* transition (on H_t(s)>0) is

\[
\boxed{P^*_t(e|s)=p_t(e|s)e^{-\beta c_t(e)}\frac{H_{t+1}(s')}{H_t(s)}}.\tag{D}
\]

Its row sums equal one by the recursion. If `V_t(s)=-(1/beta)log H_t(s)`, then

\[
V_t(s)=-\beta^{-1}\log\sum_ep_t(e|s)e^{-\beta[c_t(e)+V_{t+1}(s')]},
\]

and the `edge potential difference` `V_{t+1}(s')-V_t(s)` appears explicitly in the negative log of P*. It is a **discrete forward directional costate**, not automatically the symplectic momentum `p` of the real BBP orbit. A genuine momentum covector requires a chosen differential/discrete phase-space geometry.

As beta→infinity on a FINITE path set with positive reference mass, Q* concentrates on paths minimizing C among the feasible paths (Laplace principle). If several paths tie, Q* retains their prior-normalized weights: *no unique geodesic is forced*. For beta finite the law is stochastic. A realized path still requires an action sampling/decision rule; a Boltzmann law is not proof of ontological choice.

## RP-03 — Exact history/endpoint inadequacy and posterior shift (LOCAL MODEL)

The declared two-step automaton has root choice A or B with prior 1/2 each and both report visible x=1. After A: T with prior 3/4, X with 1/4; after B: T with 1/4, X with 1/4, Y with 1/2. Only T is the goal. The edge B→T has cost 2; all others cost 0. Let lambda=1/2 (beta=log2).

The exact backward H is `H_1(A)=3/4`, `H_1(B)=(1/4)(1/4)=1/16`, `H_0=(1/2)(3/4)+(1/2)(1/16)=13/32`. Hence

\[
P^*(A|root)=12/13,\qquad P^*(B|root)=1/13.
\]

After realized A or B, all its remaining posterior mass is concentrated on T and the alternative histories have been discarded. Under the PRIOR, A's next-support is `{T,X}` whereas B's is `{T,X,Y}`. Thus the coarse observer `q(A)=q(B)=1` fails to determine even the **support** of future observations; the future probability of T also differs (3/4 vs 1/4). No Markov factorization through this observer quotient is possible. The same visible state is NOT the same fully specified path. The realized first choice A carries information `log_2(13/12)` bits under Q*, B carries `log_2 13` bits. **RP-03B, a telescoping path-entropy/action identity:** for a goal-reaching path gamma, the ordered product of the Doob transitions equals Q*(gamma), since each intermediate H cancels. Taking logarithms at lambda=1/2 gives `-log_2 Q*(gamma) = -log_2 R(gamma) + C(gamma) + log_2 Z`: prior information plus declared path cost plus the single horizon normalization term. Every edge carries `-log_2 P*(e|s)= -log_2 p(e|s)+c(e)+V_(t+1)(s')-V_t(s)`, and the last potential differences telescope. This is the exact lawful version of forward-time path information; the cost and its units must be DECLARED, not inferred from BBP.

For general lambda in (0,1], the exact A posterior is `3/(3+lambda²)`; as lambda→0 it approaches 1. An independent enumeration of all five paths reproduces the Doob recursion. This is **finite classical test-model mathematics**, not the genuine BBP source selection.

## RP-04 — Noncommutative operator path sums need *ordered* histories (CLASSICAL)

Let M_e be a source-labelled linear operator for edge e. Its history transport is

\[
M_\gamma=M_{e_T}\cdots M_{e_1},
\qquad \mathcal Z_M=\sum_\gamma R(\gamma)e^{-\beta C(\gamma)}M_\gamma.
\]

For INDEPENDENT time-step choices the finite operator sum factorizes exactly as

\[
\mathcal Z_M=\left(\sum_{e_T}p_T(e_T)e^{-\beta c_T(e_T)}M_{e_T}\right)\cdots
\left(\sum_{e_1}p_1(e_1)e^{-\beta c_1(e_1)}M_{e_1}\right).
\]

This is distributivity of noncommuting matrix multiplication; the ORDER must be retained. With HISTORY-DEPENDENT transition laws, naïvely substituting unconditional time marginals into those factors can fail: a two-step exact original-source affine-matrix control in the code gives different rational matrices. A larger transfer operator on FULL history states repairs the factorization. A matrix-valued operator sum is not itself a positive scalar partition function; no `log` or probability measure is assigned to an arbitrary matrix without further structure.

## RP-05 — The authentic original BBP generator is a right-zero band (PROVED LOCAL)

For each literal original four-pole r(n), let

\[
G_n=\begin{pmatrix}1&r(n)/15\\0&0\end{pmatrix},\qquad
F_n=I+15G_n=\begin{pmatrix}16&r(n)\\0&1\end{pmatrix}.
\]

Direct matrix multiplication gives the **right-zero idempotent band law** `G_i G_j=G_j`; in particular `G_i²=G_i`. Since the r(n) vary, G_i and G_j do NOT generally commute. Their normalized commutator has top-right `(r(j)-r(i))/15`.

Expand the genuinely ordered source evolution `F_N...F_1=∏_{n=N}^1(I+15G_n)`. In each nonempty subset of selected factors, the product of G's equals `G_min_index` by the right-zero law. There are `binom(N-j,k-1)` ways to select k−1 later factors with earliest j, and their geometric binomial sum is `16^(N-j)`. Consequently

\[
\boxed{F_NF_{N-1}\cdots F_1=I+15\sum_{j=1}^N16^{N-j}G_j}.\tag{B}
\]

The upper-left entry is `1+15 Σ_{j=1}^N16^(N-j)=16^N`. Its upper-right entry is `Σ_{j=1}^N16^(N-j)r(j)=U_N`, using U0=0. This is an EXACT algebraic sum over optional generator factors, with combinatorial path-history multiplicities. It is not a physical quantum path ensemble and not a probabilistic observer field. An independent direct `2^N`-subset enumerator and a separate original BBP recurrence verified B for all finite tested horizons.

For the actual first two original affine steps, `r(1)=47/15`, `r(2)=106/819`, and

\[
(F_2F_1-F_1F_2)_{12}=15(r(1)-r(2))=12301/273\ne0.
\]

A scalar contour residue from PR #442 abelianizes the history and does not recover this commutator without a separately defined ordered/representation-valued transport. For any attempted Riemann-sphere monodromy, the map from pole loops to the time-indexed F_n must be source-authenticated; pole residues alone do not determine it.

## RP-06 — Exact unit-time Hamiltonian flow for the selected original BBP (PROVED LOCAL)

On the real symplectic phase plane, during step n (parameter s∈[0,1]) declare the time-dependent-by-index Hamiltonian

\[
\boxed{\mathscr H_n(x,p)=(\log16)\,p\left(x+\frac{r(n)}{15}\right).}\tag{H}
\]

Hamilton's equations `dx/ds=partial_p H`, `dp/ds=−partial_x H` give

\[
x(s)=16^s x(0)+\frac{16^s-1}{15}r(n),\qquad p(s)=16^{-s}p(0).
\]

At s=1 these are EXACTLY `x_new=16x_old+r(n)` and `p_new=p_old/16`, so the evolution is the original source-authenticated canonical affine step. Its matrix generator is `(log16)G_n`, and the idempotent identity gives the exact exponential

`exp((log16)s G_n)=I+(16^s−1)G_n`.

The pairing `A=xp` obeys

\[
\frac{dA}{ds}=(\log16)\frac{r(n)}{15}p(s),\quad
A(1)-A(0)=p(0)\frac{r(n)}{16}.
\]

With original zero-seed `(x_0,p_0)=(0,1)`, `p_(n-1)=16^{-(n-1)}` and hence `A_n−A_(n-1)=r(n)/16^n`; `A_N=U_N/16^N→π/16` by the known BBP identity. At quarter times, `16^{k/4}=2^k` makes this full flow EXACTLY rational and independently testable.

This is a *chosen mathematical interpolation* that is an actual time-one flow of each original step. It is not an SR/GR energy-momentum law, does not prove least action or entropy production, and does not identify the Hamiltonian covector p with the Doob costate V. The time-indexed source r(n) makes H vary between unit intervals; no global H-conservation theorem is asserted.

## RP-07 — Two precise path-selection/phase no-go results

**(a) Same original step, different intermediate history.** The exact maps `V_16;T_{r}` and `T_{r/16};V_16` (composition in execution order) both implement `x→16x+r`. Their intermediate rational states differ but the final real character `e(hx_new)` is identical. Both carry the same original canonical action increment when viewed from the same actual source state. Therefore a variational law depending solely on the authentic step endpoint or source action cannot select a unique microhistory: a model-specific extra path cost is required. In the simple two-route equal-cost positive model, even beta→∞ leaves probabilities 1/2,1/2.

**(b) Positive path energies cannot select real signed cancellation.** For two equally weighted admissible paths with the SAME endpoints, priors, costs and entropy, choose phase labels `(1,1)` or `(1,−1)`. Their signed amplitude averages are respectively 1 and 0. Thus any purported BBP cancellation theorem that uses only positive path probabilities, KL, metric energy, moment positivity or geodesic cost while discarding source-authenticated character phases is REFUTED by a two-path counterexample. Arbitrarily choosing path phases by fiat is not a proof of selected π normality.

## RP-08 — Deterministic original source and selected-seed firewall

For the complete authentic r(n), literal U0=0 and fixed finite horizon, the supported true arithmetic history consists of EXACTLY one path. A reference measure concentrated on that history is a Dirac mass; any absolutely continuous controlled measure is the same Dirac mass. Its path-entropy is zero. A meaningful virtual stochastic field requires added declared alternative histories, uncertainty or interventions and must not silently be identified with the source's actual deterministic future.

For any altered real initial seed s, the SAME forcing still gives `U_n(s)=U_n(0)+16^n s`; all source increments `r(n)/16^n` and generator band identities depending only on r are unchanged. SUCC PR #437 explicitly gives coherent, nonnormal same-forcing altered seed `s=1/5−π/16`. Therefore source-increment-only entropic or canonical action claims cannot force the zero-seeded normality result; the **selected real-circle seed/readout** and genuine signed phase estimate are essential.

## RP-11 — A source-specific no-go for scalar action Gibbs reweighting (PROVED LOCAL)

Let `alpha=pi/16` and `A_n=Σ_(j<=n)16^(−j)r(j)=U_n/16^n`. The ORIGINAL source is strictly positive; PR #442/#434 established `r(j)<15/[64(j−1)^2]` for all `j>=2`. All sums below consist of nonnegative terms and can be rearranged by Tonelli:

\[
\sum_{n\ge1}(\alpha-A_n)=\sum_{j\ge2}(j-1)16^{-j}r(j)
<\frac{15}{64}\sum_{j\ge2}16^{-j}=\boxed{\frac1{1024}}.
\tag{T1}
\]

(The middle estimate uses `(j−1)r(j)<15/[64(j−1)]<=15/64`.) This is an **all-horizon, source-authenticated, rational upper bound** on the accumulated *missing* canonical action; no numerical π input is required.

More generally, let any function f on `[0,alpha]` be real L-Lipschitz and satisfy `f(x)>=c>0`. Put `w_n=f(A_n)`, `w_inf=f(alpha)`. Then `Σ|w_n−w_inf|<L/1024`; and for **every** complex stream with `|z_n|<=1`, letting `D_N=Σ(w_n−w_inf)` (possibly signed), the normalized difference is bounded via the direct numerator identity:

\[
\left|\frac{\sum_{n<=N}w_nz_n}{\sum_{n<=N}w_n}
-\frac1N\sum_{n<=N}z_n\right|
\le\frac{2\sum_{n<=N}|w_n-w_\infty|}{Nc}
<\frac{L}{512cN}\quad(L>0).
\tag{T2}
\]

**Derivation:** write `w_n=w_inf+delta_n`, `R=Σdelta_n z_n`, `D=Σdelta_n`, `S=Σz_n`. The exact difference is `[N R−D S]/[N(Nw_inf+D)]`. Its numerator has absolute value at most `2N Σ|delta_n|`, and the denominator is at least `N^2c`. That is the bound. If L=0, weights are constant and the means are **identical**, so use `<=` rather than a strict bound of zero.

For the *canonical-action Gibbs* choice `w_n=e^(−beta A_n)`, any fixed beta>0 has Lipschitz L<=beta because `A_n>=0`, and c=`e^(−beta alpha)`; using `alpha<1/5` gives

\[
\boxed{\left|\frac{\sum_{n<=N}e^{-\beta A_n}z_n}{\sum_{n<=N}e^{-\beta A_n}}
-\frac1N\sum_{n<=N}z_n\right|
<\frac{\beta e^{\beta/5}}{512N}}\qquad(\beta>0).
\tag{T3}
\]

At `beta=0` both means coincide identically. The proof is uniform in *every* phase stream, hence applies to authentic `z_n=e(hU_n)` and to the coherent same-forcing altered seed. It does not prove either normality; it proves the scalar-action-only Gibbs reweight preserves the normality test. A genuinely new selection law must depend on history/continuation/phase with an independently justified source mapping, not merely on a positive smooth function of the convergent total scalar action.

The code implements exact rational finite analogues `w_n=1/(1+A_n)` and rational finite partial sums of T1, independently checked by two original-source implementations. T2/T3 are paper-proved inequalities; the tests do not attempt floating-point certification of the all-horizon bound.

## Verdict and truth debt

- **CLASSICAL / paper-proved:** finite conditional path normalization and event information; KL Gibbs principle; Doob/soft Bellman and zero-temperature limit; finite operator-valued path expansion; time-one canonical Hamiltonian algebra.
- **PROVED LOCAL (paper + exact implementation):** source-specific right-zero band `G_iG_j=G_j`, original 2-step commutator, subset expansion of BBP matrix evolution, rational quarter-time Hamiltonian source action, and the exact five-path observer countermodel.
- **REFUTED oversells:** increased future Shannon entropy at every actualized path; geodesic uniquely selected from endpoints alone; scalar endpoint quotient preserving arbitrary path costs; entropy-only implication of signed π Weyl cancellation; random intrinsic branch of unchanged zero-seeded BBP.
- **PROVED LOCAL / SOURCE FIREWALL:** any positive Lipschitz action-only Gibbs time tilt is asymptotically equivalent to uniform Weyl averaging with explicit O_beta(1/N) bound.
- **OPEN:** source-attested nonflat real-circle phase transport from a **justified** realized-history/energy law sufficient for all-horizon `S_N(h)=o(N)` at each fixed nonzero h. Source-labelled puncture transport from the four-punctured sphere to these affine time generators is not established by the scalar residue differential.

## Provenance for classical instruments

- Doob `h`-transform and finite Markov bridges: https://mathworld.wolfram.com/Doobh-Transform.html ; Doob, *Conditional Brownian Motion*, Bull. Soc. Math. France 85 (1957).
- Entropy-regularized path costs / linearly-solvable control: Dvijotham/Todorov chapter https://homes.cs.washington.edu/~todorov/papers/DvijothamChapter12.pdf .
- Maximum caliber on trajectory distributions: Ghosh et al., *The Maximum Caliber Variational Principle for Nonequilibria*, https://pmc.ncbi.nlm.nih.gov/articles/PMC9827727/ .
- Authenticated parent arithmetic: SUCC PR #442 Riemann-sphere source and path-order obstruction; #441 BBP symplectic action; #440 Pascal–Gamma unit-SUCC; Main XVIII selected signed lag. These are SOURCE DEPENDENCIES, not independent proofs of the new results.
