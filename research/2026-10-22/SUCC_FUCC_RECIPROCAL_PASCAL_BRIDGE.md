# SUCC ↔ FUCC: reciprocal prime clocks, zeta detailed balance and the infinite Pascal lift

**2026-10-22 · research branch:** `research/reciprocal-succ-fucc-pascal-2026-10-22`, stacked on `research/prime-bridge-coherent-tower-2026-10-22@328f1c0bd8d564acb9da50e96d1101850ebb9cdd` (draft PRs #235 and #234). **Scope:** established operator and stochastic identities, explicitly derived universal paper theorems, exact finite independent probes, and new-to-SUCC synthesis. **No** actual backwards physical causation, no Einstein–Rosen wormhole, no original Weil positivity, no RH proof, and **no claimed academic novelty**.

## The mathematical claim, properly typed

“SUCC looks backward while progressing forward” and “FUCC looks forward while progressing backward” must be **two representations of the same source system**. Distinguish four operations: source state pushforward; pullback of future observables; partial inverse/adjoint of a source injection; and Bayesian cotransition under a specified probability measure. They are not automatically identical, and changing basis may be unbounded.

The construction has three jointly compatible layers: a precise mixed adjoint square, a fully reversible p-residue carry register, and a common Gibbs reversible transition system. The infinite prime-Pascal multiset hierarchy then reconstructs the same arithmetic thermal amplitudes as the thermofield double, without collapsing prime powers to squarefree support.

## Theorem RSFP-01: the reciprocal affine square

On `H=ell²(N_{\ge1})` define `S e_n=e_(n+1)` and `V_p e_n=e_(pn)` for each genuine rational prime `p`. The familiar forward braid `V_p S=S^p V_p` has a distinct **forward/backward** counterpart:

\[
\boxed{V_p^\dagger S^p=S V_p^\dagger.}
\]

**Proof.** For every `n>=1`, either `p|n`, in which case both sides return `e_(n/p+1)`, or `p∤n`, in which case both sides return zero. In particular, `V_p^\dagger` is not a globally defined inverse: `V_p V_p^\dagger` projects onto `p`-divisible integers. QED.

For a shift `S^r` with `p∤r`, this shortcut fails: choose `n` with `p∤n` but `p|(n+r)`. The left side `V_p^\dagger S^r e_n` is nonzero, while `S^t V_p^\dagger e_n=0` for every `t`. **The correct repair is to retain the residue-clock phase.**

## Theorem RSFP-02: full reversible residue clocks and their coherence

Use the basis relabeling

\[
U_p:e_n\mapsto e_m\otimes e_r,\qquad
n=p(m-1)+r+1,\quad 0\le r<p.
\]

This is a Hilbert-space unitary onto `H\otimes C^p`. Forward SUCC becomes a **local carry rule in this enlarged frame**:

\[
U_p S U_p^{-1}e_{m,r}=
\begin{cases}
e_{m,r+1}&r<p-1,\\
e_{m+1,0}&r=p-1.
\end{cases}
\]

The `p`-step cover becomes `U_p S^p U_p^{-1}=S\otimes I_p`, and `U_p V_p e_m=e_m\otimes e_{p-1}`. Correspondingly `V_p^\dagger=(I\otimes\langle p-1|)U_p`. The reciprocal square follows from these identities without treating division as invertible on nonmultiples.

For two scale clocks `p,q`, reading the p clock then the q clock gives `n-1=pq(m-1)+ps+r`, whereas the reverse read order gives `n-1=pq(m-1)+qt+u`. Their change-of-frame is the **actual carry permutation** `ps+r=qt+u`, *not* naive digit transposition. By uniqueness of Euclidean division, arbitrary rebracketing and permutations of finitely many mixed-radix clocks give the same decoded original source integer. The executable probes check all six readings of primes `2,3,5` and 2560 two-clock cases.

## Theorem RSFP-03: SUCC and FUCC uniquely share a zeta Gibbs source

Let `β>1` be real and define `π_β(n)=n^{-β}/ζ(β)`. Attach source-labelled continuous-time transition channels:

| Source edge | Ascending transition rate | Descending transition rate |
|---|---|---|
| Additive SUCC `n↔n+1` | `(n/(n+1))^β` | `1` |
| Prime FUCC `n↔pn` | `p^{-β}` | `1` |

When the same endpoint pair occurs in different source channels, keep parallel labels and **add** their rates in the Markov generator, rather than pretending the channels are the same causal record.

Every edge satisfies

\[
\boxed{\pi_\beta(n)q(n,m)=\pi_\beta(m)q(m,n).}
\]

**Proof and rigidity.** For the additive edge, the left side is `n^{-β}(n/(n+1))^β/ζ(β)=(n+1)^{-β}/ζ(β)`, equal to its reverse flux. For prime multiplication, `π_β(n)p^{-β}=π_β(pn)`. Conversely, if any strictly positive probability distribution satisfies these fixed additive-edge rates, then `π(n+1)/π(n)=(n/(n+1))^β`. Telescoping yields `π(n)=π(1)n^{-β}`; normalization forces `π(1)=ζ(β)^{-1}` and is possible iff `β>1`. Prime-edge balance separately implies `π(pn)=p^{-β}π(n)`, and unique factorization also forces the same distribution. Thus **the two orientations must agree on one source law, given their declared rates**.

This matches the standard zeta Gibbs equilibrium of arithmetic quantum statistical mechanics at the probability level. It is not an assertion that reversible stochastic evolution is an Einstein–Rosen bridge.

### Full countable-state dynamics, not just finite toy matrices

On test observables with the requisite domain, the generator is

\[
\begin{aligned}
L_\beta f(n)={}&
\left(\frac n{n+1}\right)^\beta[f(n+1)-f(n)]\\
&+\mathbf1_{n>1}[f(n-1)-f(n)]\\
&+\sum_{p}p^{-\beta}[f(pn)-f(n)]\\
&+\sum_{p\mid n}[f(n/p)-f(n)].
\end{aligned}
\]

At each finite `n`, the sum of upward rates is at most `1+\sum_p p^{-\beta}<\infty`; there are finitely many downward source channels. To rule out finite-time explosion, dominate all upward events by a constant-rate Poisson clock. Almost surely finitely many upward jumps happen before any fixed time, and their target integers are finite; between and after them, every downward jump strictly decreases the integer. Hence only finitely many downward events can occur. Edge-wise detailed balance makes `π_β` invariant and reversible.

The stationary mean total jump rate equals

\[
2\left(1-\frac1{\zeta(\beta)}+\sum_p p^{-\beta}\right)<\infty.
\]

The associated source-labelled, nonnegative Dirichlet form for bounded `f` is

\[
\mathcal E_\beta(f)=
\sum_{n\ge1}\pi_\beta(n+1)|f(n+1)-f(n)|^2
+\sum_p\sum_{n\ge1}\pi_\beta(pn)|f(pn)-f(n)|^2.
\]

This genuinely connects **both** SUCC and FUCC within one reversible countable-state Markov system. It is not the signed completed Weil form. Finite reflecting charts inherit the conditional Gibbs source `π_β(\cdot\mid n\le N)` and satisfy exact stationarity and symmetry over all channel rates.

### Arithmetic coherence of rates

The affine square `V_pS=S^pV_p` also has **path-weight equality**:

\[
\underbrace{\left(\frac n{n+1}\right)^\beta p^{-\beta}}_{S\ {\rm then}\ V_p}
=
\underbrace{p^{-\beta}
\prod_{j=0}^{p-1}
\left(\frac{pn+j}{pn+j+1}\right)^\beta}_{V_p\ {\rm then}\ S^p}
=
\left(\frac n{p(n+1)}\right)^\beta.
\]

This is a pure gradient cocycle for the potential `Φ(n)=β\log n`; its absence of square holonomy is real, but is **not** a source-authentication proof: a fake composite generator can preserve algebraic relations yet must not be admitted as a *primitive prime jet*.

## Theorem RSFP-04: the same weighted reversal is the arithmetic EPR mirror

Let `\Omega_\beta=\zeta(\beta)^{-1/2}\sum_{n\ge1}n^{-\beta/2}|n,n\rangle` and let `U_{a,b}|n\rangle=|an+b\rangle` for `a≥1,b≥0`. Define the state-conditioned mirror on the explicitly specified monoid generators by

\[
M_\beta(U_{a,b})|an+b\rangle
=
\left(\frac{an+b}{n}\right)^{\beta/2}|n\rangle,
\]

and zero off the source image. This operator is bounded for each `a,b`, with norm bounded by `(a+b)^{\beta/2}`. Direct source-basis calculation proves

\[
M_\beta(U_fU_g)=M_\beta(U_g)M_\beta(U_f),
\qquad
(U_f\otimes I)\Omega_\beta
=(I\otimes M_\beta(U_f))\Omega_\beta.
\]

The **opposite order of operator composition** is the algebraic reversal; it is not a backwards physical effect. The mirror amplitude is the reciprocal of the forward square-root Gibbs edge rate, as required by the common Schmidt coefficients. The diagonal inverse implicit in the formal similarity is unbounded, so the statement is restricted to explicitly verified bounded source operators.

## Theorem RSFP-05: prime-Pascal divided powers produce the same thermal spectrum

The bottom rung must be a countably infinite family of genuine primitive units, but an ordinary Boolean subset of primes does not remember prime powers. Replace it by the **finite-support prime occupation multiset** `α=(v_p(n))_p`, ranked by `|α|=\sum_pα_p=\Omega(n)` (number of prime factors with multiplicity).

For each prime `p`, define the source-weighted creation on the finite-occupation core by

\[
C_p|\alpha\rangle=(\alpha_p+1)p^{-\beta/2}|\alpha+e_p\rangle.
\]

The factor `α_p+1` records the current form/number of existing instances of that unit. Distinct `C_p,C_q` commute on their common core. Let `R=\sum_pC_p`, interpreted first at finite prime support/rank.

\[
\boxed{
\frac{R^k}{k!}|\varnothing\rangle
=\sum_{|\alpha|=k}\prod_p p^{-\beta\alpha_p/2}|\alpha\rangle.
}
\]

**Proof:** for each terminal multiset `α`, there are `k!/\prod_pα_p!` distinguishable ordered source histories. Along each such history, the factors `α_p+1` accumulate to `\prod_pα_p!`. The scalar factor per path depends only on the endpoint and equals `\prod_pα_p!\,p^{-\beta\alpha_p/2}`. Dividing by `k!` cancels exactly. No ambiguity about repeated primes survives.

For countably many primes and real `β>1`, each rank vector exists in Hilbert norm and its squared norm is the degree-`k` complete homogeneous symmetric sum `h_k(p^{-\beta})=\sum_{\Omega(n)=k}n^{-\beta}`. Orthogonality across ranks yields

\[
\sum_{k\ge0}\left\|\frac{R^k}{k!}|\varnothing\rangle\right\|^2
=\sum_{n\ge1}n^{-\beta}=\zeta(\beta)<\infty.
\]

This establishes a **vacuum-defined** exponential series; it does not claim an everywhere bounded `e^R`. Its normalized result is `\zeta(\beta)^{-1/2}\sum_n n^{-\beta/2}|\alpha(n)\rangle`. Applying the diagonal basis-label isometry `|\alpha(n)\rangle\mapsto|n,n\rangle` produces the arithmetic EPR thermofield double. The map is *not* a universal unknown-state quantum cloning machine.

With a declared interacting scalar source form `Φ(α)`, the edge weights

\[
w_p(\alpha)=(\alpha_p+1)\exp[-(\Phi(\alpha+e_p)-\Phi(\alpha))/2]
\]

still commute around elementary diamonds by telescoping, but convergence, source realization and physical interpretation are separate obligations. Flatness is not a proof of entropy geometry.

## Theorem RSFP-06: cotransition/projectivity counterexample

For **one endpoint-conditioned equally weighted ensemble of ordered histories** ending at occupation `α` of rank `k`, Pascal backward removal gives

\[
Q(\alpha,\alpha-e_p)=\alpha_p/k.
\]

However, this kernel need not make the **separately normalized** zeta Gibbs distributions conditional on each rank projectively compatible.

For just primes 2 and 3 put `u=2^{-\beta},v=3^{-\beta}`. Direct rank-one Gibbs mass at occupation `(1,0)` is `u/(u+v)`; rank-two Gibbs mass, transported by the Pascal backward kernel, becomes

\[
\frac{u^2+uv/2}{u^2+uv+v^2}.
\]

Their difference is `uv(u-v)/[2(u+v)(u^2+uv+v^2)]`, nonzero for distinct primes. At `β=2` the exact answers are `9/13` versus `99/133`. **Therefore the rank-conditioning, path prior and backward kernel must be transported together.** A source-specific continuous-time detailed-balance model (`RSFP-03`) is one valid way to have consistent forwards and backwards descriptions; it is not identical to conditioning each graded Gibbs rung and applying `α_p/k`.

A second hostile control: choosing a death rate proportional to `α_p` with constant prime birth rates produces Poisson/factorial occupation laws, rather than the geometric Euler factors `(1-p^{-\beta})^{-1}`. The genuine zeta reversible graph has reverse death rate `1` for every occupied distinct prime species.

## Theorem RSFP-09: exact rank-one obstruction when the future boundary is forgotten

This is a sharper result than the blanket strong-versus-norm claim. The **full** mixed adjoint relation \(V_p^\dagger S^p=SV_p^\dagger\) is exact, and the **finite forward–forward** affine relation survives every complete initial segment, but the corresponding **finite mixed forward/backward** square fails by precisely one source-boundary channel.

Let \(P_N\) project onto the first \(N\) integers, and \(S_N=P_NSP_N,\ V_{p,N}=P_NV_pP_N\), acting on the range of \(P_N\). Put \(q=\lfloor N/p\rfloor\). Then, for \(N\ge p\),

\[
\boxed{
B_{p,N}:=V_{p,N}^{\dagger}S_N^p-S_NV_{p,N}^{\dagger}
=-|q+1\rangle\langle pq|
=-P_NV_p^\dagger(I-P_N)S^pP_N.}
\]

When \(N<p\), the left side is zero.

**Proof.** For any basis vector \(|n\rangle\) with \(p\nmid n\), both finite routes vanish. For \(n=pm\le N\) with \(pm+p\le N\), both give \(|m+1\rangle\). The **only** divisible input with \(pm+p>N\) is \(n=p\lfloor N/p\rfloor=pq\), the last visible multiple: \(S_N^p|pq\rangle=0\), whereas \(S_NV_{p,N}^\dagger|pq\rangle=|q+1\rangle\) (and \(q+1\le N\)). This proves the rank-one formula. For the last identity, expand \(P_NV_p^\dagger S^pP_N=P_NS V_p^\dagger P_N\) using the full reciprocal relation; the only missing term in the finite route is the excursion into \(I-P_N\), which later returns to range \(P_N\) under \(V_p^\dagger\). QED.

Consequently, \( \|B_{p,N}\|=1 \) for all \(N\ge p\), but \(B_{p,N}\to0\) **strongly** as \(N\to\infty\), because the input bra \(\langle p\lfloor N/p\rfloor|\) escapes to infinity and every fixed \(\ell^2\) state has vanishing amplitude there. This is not uniform operator-norm convergence.



### Graded Pascal-rung corollary: rank grows exactly with the backward horizon

The rank-one case is the first cell in an exact hierarchy. Fix a positive integer \(t\). Since the full relation iterates as \(V_p^\dagger S^{pt}=S^t V_p^\dagger\), its complete-prefix finite compression has the explicit graded defect

\[
\boxed{
V_{p,N}^\dagger S_N^{pt}-S_N^tV_{p,N}^\dagger
=-\sum_{j=\max(1,q-t+1)}^{\min(q,N-t)}
|j+t\rangle\langle pj|,
\qquad q=\lfloor N/p\rfloor.}
\]

**Proof:** a source basis state \(|pj\rangle\), \(j\le q\), survives the reverse-first route precisely when \(j+t\le N\), and the forward-first route precisely when \(p(j+t)\le N\), i.e. \(j+t\le q\). Their difference consists exactly of the indices \(q<j+t\le N\); all nonmultiples vanish on both sides. The displayed summands have mutually orthogonal source and destination vectors. For fixed \(p,t\) and sufficiently large \(N\), the boundary defect has **exact rank \(t\)** and operator norm one, while converging strongly to zero as \(N\to\infty\).

This gives a precise **rung-by-rung hierarchy of backward-returnable source channels**: a \(p\cdot t\)-step forward excursion can discard \(t\) distinct FUCC-recoverable amplitudes, not an uncontrolled cloud of information. The \(t=1\) formula is the rank-one case above. The arithmetic paths are the true original states; Pascal-like rank multiplicity is a bookkeeping analogy, not a derivation of a geometric metric.

An independent finite source oracle checks **1,820 graded cutoff configurations and 60,060 basis inputs**, plus the existing 400 rank-one configurations and 16,200 rank-one basis inputs. Universal validity follows from the basis proof, not the finite census.

**Source significance:** a finite forward observer discards a step beyond the present horizon; a subsequent backward FUCC quotient could have returned that same amplitude inside the observed carrier, but the necessary intermediate record was lost. A source-preserving completion must keep the boundary-excursion witness. This is a mathematical *future-boundary dependence*, not literal reversal of physical causality. Exact finite independent tests exhaust **16,200 basis inputs** over 400 \(N,p\) configurations and independently verify the rank-one support; the universal formula follows from the basis proof.

## Theorem RSFP-07: previous locality no-go survives its stated boundary

The Prime Bridge II no-go says no single uniformly finite-depth local operator on the **particular three-ray code** realizes all of arithmetic successor. It does **not** forbid a one-step local carry automaton applied repeatedly, a larger precomputed source register, or an explicitly available future-conditioned backward message. The residue clocks exhibit a reversible finite-state *rule* for each scale, but global arithmetic successor still carries information through arbitrarily many ranks. Local rule depth, actual total causal time, entanglement preparation, postselection, and access to boundary conditions require separate resource accounting.

Thus the user’s insight repairs a pathway gap without claiming an impossible fixed-depth implementation. It supplies a concrete lamp: determine whether an intrinsic Pascal/source-graded cotransition can be transported into the existing infinite two-ray geometric code with independently derived locality and norm bounds.

## Verification and provenance

Executable module `observational_succ/reciprocal_succ_fucc.py`; hostile exact suite `tests/test_reciprocal_succ_fucc.py`; replay `scripts/reciprocal_succ_fucc_probe.py`; frozen source-blob receipt; claim supplement `docs/CLAIM_SUPPLEMENT_RECIPROCAL_PASCAL.md`. Twenty exact independent tests cover full residue-clock phases, mixed-radix triple coherence, finite reversible Markov matrices, source-weighted diamonds, EPR mirror anti-homomorphism, repeated-prime divided powers, counterfeit composite primes, incompatible Gibbs rank cotransitions and malformed inputs. No Lean kernel admission or scholarly originality asserted.

**Next verdict-changing probe:** build a common source-indexed intertwiner connecting (a) the Gibbs reversible generator and its adjoint, (b) the projectively compatible graded Pascal path law, and (c) the two-ray quantum code/analytic Hardy–Dirichlet representation. Require a single preserved backward kernel and a transportable geometric locality budget. A sharp impossibility or noncanonicity theorem is also a valid result.

### Attribution
The zeta partition function and arithmetic quantum system are classical Bost–Connes (1995); detailed balance and reversible Markov chains are classical; Pascal cotransition and divided-power combinatorics are classical. Existing SUCC `pascal_rotated_transport.py`, `succ_discrete_integration.py`, and Prime Bridge II (#235) provide the repository-specific interfaces. This dossier's mathematical synthesis is **new to SUCC; academic novelty unverified**.
