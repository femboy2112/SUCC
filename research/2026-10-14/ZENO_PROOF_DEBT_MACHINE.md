# Operation ZENO DEBT — A source-indexed calculus of finite proof, effective remainder, and global obligations

**Date:** 2026-10-14. **Research parent:** `femboy2112/SUCC`, draft ZENO-SUCC PR #94, commit `cd9091572d11d85e0007e9b87e2004b6d3d85f63`; parent is already stacked above WILD ADELIC #88, authentic Arithmetic Meta-Weil #86, and Recursive Meta-SUCC #80. **Research branch:** `research/zeno-proof-debt-synthesis-2026-10-14`. No existing research texts, main, provenance, releases, or the separate RH repository are edited. **RH PROVED: NO.** Mathematics below is primarily classical, with new-to-SUCC proof-typed synthesis, exact algorithms, adversarial controls and sharp source normalization; **academic originality UNVERIFIED**. No physical event at ordinal ω and no external actual source authentication.

## 0. Steelman the proposal, differentiate the four debts

The maintainers' hypothesis is that a finite embedded reasoner can construct a whole globally quantified model without observing its infinitely many particulars. Its Zeno version is **not** “infinitely many events were performed”: it is a finite *proof* that a source-indexed successor law has a mathematically licensed endpoint and that the relevant property survives passage to that endpoint.

An observer can have four logically independent debts:

1. **Analytic debt:** a declared mathematical residual or norm difference `||Q-Q_J|| <= epsilon_J` on one specified common test domain.
2. **Epistemic debt:** remaining variation of the original target across *still-compatible original sources*, `diam T(P_n)`. It can shrink through lawful actual history, but never by making up an impossible outcome or losing an original source label.
3. **Semantic debt:** a mathematical *change of target* or source interpretation. A shrinking current-model error does not certify an older or future target without a separately quantified transport law.
4. **Resource debt:** time, computation, memory and irreversible/mandatory costs of performing a history. A summable duration neither supplies a proof certificate nor makes a nonsummable energy expenditure disappear.

These debts can interact only through **proved conversion inequalities**. For example: compactness+continuity converts finite chart agreement into approximate original-target agreement; a valid Gamma multiplier bound converts truncation depth into a Sobolev form error; a validated Schur complement converts an infinite-complement coercivity certificate plus finite blocks into all-test positivity.

The previous Zeno PR #94 established geometric SUCC, the four classical motion paradoxes, Thomson's lamp, and the source-correct Gamma-rung tail. The current project explicitly moves on to quantified proof debt, original-source target widths, adaptive search barriers, weak-sign computability and two-axis operator budgets. A parallel sibling BLACK SUN IV PR #93 already discusses a Zeno completion audit, Gamma schedules and Baez–Duarte/Nyman distances; **do not merge its separate formulas or claims implicitly**. This branch strengthens the missing general proof-debt / source-width / computability layer independently.

## 1. PDM-01 — exact successor bookkeeping (elementary / PROVED LOCAL)

Fix a mathematical source stamp `(source_id,epoch,basis,domain)`, a fixed original target `T`, and initial outstanding obligation weight `D_0>=0`. A *modeled*, correctly stamped stage `n` carries nonnegative born weight `b_n`, discharged weight `d_n`, elapsed time `t_n` and resource cost `c_n`, subject to `d_n <= D_n+b_n`. The exact source-typed successor is

\[
\boxed{D_{n+1}=D_n+b_n-d_n,\qquad
\tau_{n+1}=\tau_n+t_n,\qquad E_{n+1}=E_n+c_n.}\tag{PDM-1}
\]

Finite summation proves `D_n=D_0+Σ_{j<n}(b_j-d_j)`, `τ_n=Σt_j`, `E_n=Σc_j`. No equation among these three accumulated quantities is licensed without an additional source law. **Negative control:** `t_n=2^{-(n+1)}`, `c_n=1`, `b_n=d_n=0`: mathematical time tends to `1`, while energy diverges and initial proof debt never changes. Even in this toy, no *physical* infinite sequence has been executed. Missing source/epoch/target provenance or overdraft discharge is rejected.

## 2. PDM-02 — amortized Zeno with born obligations (elementary quantitative theorem / PROVED LOCAL)

Let `D_n>=0` satisfy a *universally proved* successor inequality for every `n>=0`:

\[
D_{n+1}\le qD_n+C r^n,\quad D_0\le D,\quad 0\le q,r<1,\quad C,D\ge0.\tag{PDM-2}
\]

Then iteration gives the exact bound

\[
D_n\le D q^n+C\sum_{j=0}^{n-1}q^{n-1-j}r^j .\tag{PDM-3}
\]

Put `M=max(q,r)` and `rho=(1+M)/2`, so `M<rho<1`. Define

\[
\boxed{K=D+\frac{C\rho}{(\rho-M)^2}.}\tag{PDM-4}
\]

**Uniform effective Zeno theorem:**

\[
\boxed{\forall n\ge0,\quad D_n\le K\rho^n.}\tag{PDM-5}
\]

**Proof.** Inductively expand the recurrence for (PDM-3). For `n>=1`, its convolution is at most `nM^{n-1}`. With `b=M/rho<1`, `n b^{n-1}<=Σ_{k>=1}k b^{k-1}=(1-b)^{-2}`. Consequently `CnM^{n-1}<=C rho^{n-1}(1-M/rho)^{-2} = C rho^n rho/(rho-M)^2`; also `Dq^n<=D rho^n`. At `n=0`, `D_0<=D<=K`. This proof includes `q=0` and `r=0` by the finite-sum convention, without manipulating an undefined `0^{-1}`. QED.

For any positive rational `epsilon`, a finite rational multiplication loop finds `N` with `K rho^N<=epsilon`, and then certifies the bound for **every later stage**. The engine stores the universal law as an *external mathematical premise*. Merely replaying its first hundred instances does not prove it for all stages. A finite resource-budget exhaustion is not a theorem that no such `N` exists.

**Controls:** if instead `D_{n+1}=qD_n+C` with `C>0`, then `D_n->C/(1-q)>0`, so persistent new independent obligations defeat Zeno closure. But even summability of `b_n` is unnecessarily strong for convergence: if `b_n->0` and `D_{n+1}<=qD_n+b_n` with `q<1`, splitting the convolution into a fixed early prefix and a late small tail proves `D_n->0`. For example `b_n=1/(n+1)` is not summable but debt still vanishes. **Outstanding debt, total information acquired, and total physical resource need not share a limit.**

## 3. PDM-03 — source-indexed epistemic width (finite theorem / PROVED LOCAL; compact analogue classical)

For a fixed complete *mathematical* set of possible originals `S`, retained lawful history `h_n` specifies nonempty nested compatible-source sets `P_{n+1}⊆P_n`. For fixed scalar original target `T:S->R`, define

\[
L_n=\inf_{s\in P_n}T(s),\quad U_n=\sup_{s\in P_n}T(s),\quad W_n=U_n-L_n.\tag{PDM-6}
\]

Any authentic source surviving history has target in `[L_n,U_n]`; widths are nonincreasing. For a *finite* complete source, the exact rational engine returns the extrema and two original states witnessing the width. Action reports must be supplied on **every declared original state**, with correct source stamp. Empty/forged outcomes and admissions of new incompatible originals are rejected. The finite chart tables are mathematical premises, **not** instruments physically performed simply because a user typed them.

**Compact source theorem.** Suppose `S` is compact Hausdorff, `T:S->R` is continuous, and each `P_n` is a nonempty closed nested subset. Then the intersection `P_∞=∩P_n` is nonempty, and

\[
\boxed{\lim_{n\to\infty} W_n=\operatorname{diam}T(P_\infty).}\tag{PDM-7}
\]

**Proof.** Compactness and the finite-intersection property give a nonempty intersection. Let `d=lim_n W_n` (it exists by bounded monotonicity). Each image `T(P_n)` is compact, so `W_n` is attained and `K_n={(s,t)∈P_n×P_n:|T(s)-T(t)|>=d}` is nonempty compact. These `K_n` are nested; compactness of `S×S` yields an element `(s,t)∈∩K_n`. Then `s,t∈P_∞` and `|T(s)-T(t)|>=d`. Conversely `diam T(P_∞)<=W_n` for each `n`, hence `<=d`. Equality follows. **This proof uses a nested-compact intersection rather than sequential compactness, so it works for arbitrary compact Hausdorff `S`.** QED.

**Interpretation:** exact global target identification on a compact surviving source fiber is equivalent to *Zeno convergence of target-width debt*, even if no finite stage identifies the exact real value. This is an existence theorem; absent a source modulus, it does not produce a computable stage bound.

**Hostile failures:** noncompact nested `[n,∞)` can have no realizer; discontinuous target `T(0)=0`, `T(1/n)=1` on compact `S={0}∪{1/n}` retains width `1` along `P_n={0}∪{1/k:k>=n}` despite the singleton intersection `{0}`. Source-changing experimental backaction must be tracked through original-state histories before using the nesting hypothesis; this is exactly SUCC's NO-GHOST/F48 source type constraint.

## 4. PDM-04 — compact finite-accuracy extraction (classical compactness, PROVED as an explicit SUCC bridge)

This strengthens GMS-02 of PR #77 from finite-valued target extraction to **real-valued finite-accuracy extraction**.

Let `S` be compact Hausdorff; let `T:S->R` be continuous; let `q_i:S->O_i` be a family of continuous finite-discrete mathematical charts. Assume that whenever `T(s) != T(t)`, at least one `q_i` separates `s,t`. Then:

\[
\boxed{\forall\varepsilon>0\quad\exists I_\varepsilon\subset I
\text{ finite},\quad
q_{I_\varepsilon}(s)=q_{I_\varepsilon}(t)
\Rightarrow |T(s)-T(t)|<\varepsilon.}\tag{PDM-8}
\]

**Proof.** The target-disagreeing-at-scale set `K_e={(s,t):|T(s)-T(t)|>=e}` is a closed subset of compact `S²`, hence compact. For every `(s,t)∈K_e`, target separation assures some `q_i(s)!=q_i(t)`. Since `O_i` is finite discrete and `q_i` continuous, the pair-separation set `U_i={(s,t):q_i(s)!=q_i(t)}` is open. These `U_i` cover `K_e`, so compactness extracts a finite subcover. Agreement on those charts is incompatible with membership in `K_e`, giving strict `<e` as claimed. QED.

A finite original-source implementation enumerates exact chart families, chooses a **minimum-cardinality** one for a rational epsilon, and returns the largest unresolved width and original-source collision witness when the declared charts are inadequate. Its output deliberately sets `physical_joint_executability_verified=false` and `source_law_authenticated_externally=false`.

**Real Zeno example:** `S={0,1}^N` with product topology and `T(s)=Σ_(k>=1) 2^{-k}s_k` is continuous. Observing its first `n` coordinates determines `T` within width `2^{-n}` but, for any finite `n`, cannot determine the exact value for all source tapes. This is a source-defined, effective infinite-to-finite accuracy schedule. **Noncontinuous negative control:** `T(s)=1` iff infinitely many coordinates equal `1` cannot be determined to error `<1/2` from any finite coordinate family. **Read-only causal blindness:** if two original sources have the same report under **every available read-only probe** yet their targets differ by `d>0`, any deterministic adaptive protocol using only these probes has identical transcripts on both sources; at least one of its outputs errs by `d/2` or more. Randomized source-independent policies have the same identical-transcript obstruction for guaranteed zero error. This conclusion does not cover destructive instruments, independently created new probes, or a stronger external source law.

## 5. PDM-05 — moving target has an independent semantic tail (classical / PROVED LOCAL)

For a fixed original source class `S`, let `T_n:S->R` change with mathematical epoch. Suppose a separately established original-source drift law holds:

\[
\sup_{s\in S}|T_{n+1}(s)-T_n(s)|\le\beta_n,
\qquad \sum_{n=0}^\infty\beta_n<\infty.\tag{PDM-9}
\]

Then `T_n` converges uniformly to `T_∞` with `|T_∞(s)-T_n(s)|<=B_n=Σ_{k>=n}β_k`. If `P_n` is a nested original-source fiber, then for every `s∈P_∞`:

\[
L_n-B_n\le T_\infty(s)\le U_n+B_n,
\qquad\boxed{\operatorname{diam} T_\infty(P_\infty)\le W_n+2B_n.}\tag{PDM-10}
\]

**Proof.** Uniform Cauchy follows from the summable supremum differences; R-completeness yields `T∞`. The triangle inequality gives the enclosure and diameter. QED. The code checks every finite declared target law on all original states and refuses to invent any **future** `B_n` from finite observations. A trusted future universal envelope is an explicit additional premise. Geometric `β_n<=Cr^n` has certified `B_n<=Cr^n/(1-r)`.

**Counterexample:** on a singleton source, `T_n=n mod 2` has source-width zero at every stage yet no target limit. Also `T_n=Σ_(j<=n)1/j` changes by a vanishing amount but diverges; `β_n->0` without summability is insufficient. This distinguishes a changing original theorem from a fixed theorem whose proof budget shrinks.

## 6. PDM-06 — Dini's uniformity gate and noncompact all-test obstruction (CLASSICAL)

Let `S` be compact and `d_n:S->[0,∞)` continuous, with `d_{n+1}(s)<=d_n(s)` and `d_n(s)->0` for every `s`. By Dini's theorem,

\[
\boxed{\sup_{s\in S}d_n(s)\to0.}\tag{PDM-11}
\]

**Proof:** for `eps>0` the open sets `{s:d_n(s)<eps}` increase and cover `S`; a finite subcover plus monotonicity gives a common stage. QED. Without compactness, `S=(0,1]` and `d_n(s)=(1-s)^n` tend to zero separately but have supremum `1` for every `n`. Without continuity, even compact source doesn't suffice. An infinite-dimensional Hilbert unit sphere is not norm compact, and arbitrary signed Weil form tests do not inherit Dini from finite model samples. Dini is a mathematical existence theorem, not automatically an *effective* modulus.

## 7. PDM-07 — effective Zeno convergence does NOT decide a weak sign (CLASSICAL COMPUTABILITY NO-GO)

Even when rational approximants have a **known geometric error modulus**, there is no universal terminating procedure that decides `x>=0` for every computable real `x` described in this way.

**Proof by a uniform source construction.** Given a Turing machine `M` and fixed input, define the real `x_M=0` if `M` never halts; if it first halts at stage `t>=0`, let `x_M=-2^{-(t+2)}`. The stage-`N` approximation simulates `M` for exactly `N` steps, returning that negative dyadic if a halt is seen and `0` otherwise. The approximation is rational and total computable for each `N`. If the halt is not yet seen, any future first halting time satisfies `t>N`, hence `|x_M-a_N|<=2^{-(N+2)}`. If it is seen, the approximation is exact. Thus a *uniform known* error modulus is supplied independent of when/if `M` halts. But `x_M>=0` iff `M` does **not** halt. A general decision algorithm for the weak sign would decide the nonhalting set, contradicting the undecidability of halting. QED.

**Operator consequence (PDM-07B, sharpened no-go).** On `H=ℓ²(N)` let `P_1=|e_1><e_1|` and `A_M=x_MP_1`, with finite-rank approximation `A_(M,N)=a_NP_1`. This is an effectively presented **compact, bounded, self-adjoint rank-one operator**, and the operator-norm approximation satisfies `||A_M-A_(M,N)||<=2^{-(N+2)}` with the SAME universal known modulus. Yet `A_M>=0` iff `M` does not halt. Therefore there is **no universal positivity decision algorithm for generic source-computable self-adjoint compact operators**, even when exact rank-one finite matrices and a geometric norm-convergence schedule are supplied. A negative direction is semidecidable when it has a strict witnessed margin; an operator approaching a semidefinite boundary cannot be classified universally by finite approximation alone. This is precisely a **generic** IdealHard/FuckedSpace control, not a theorem that the authentic zeta Weil form is unprovable.

The finite test code receives a synthetic **known** halt index; it is NOT a universal halting oracle. Its purpose is to show exact indistinguishability across every prescribed finite horizon. Strict positivity and strict negativity **are semidecidable** from effective enclosures: if the true value has a strict sign, eventually a valid interval lies entirely on that side. Exact zero need not receive any finite sign verdict. This is a generic toolkit-level no-go; it says **nothing** about undecidability or truth of RH, whose arithmetic source is far more specialized.

**Prior-art context:** computable analysis of Weihrauch (2000), Brattka–Gherardi–Pauly (2017), and the standard undecidable comparison/equality reduction; Specker's noncomputable convergence modulus is a *different* obstruction already recorded in PR #94. Zeno can fail effectively at either (i) finding a modulus or (ii) deciding a boundary-sign even with that modulus.

## 8. PDM-08 — the original signed Weil Gamma tail, now with SHARP uniform constant (CLASSICAL SOURCE COUPLING / PROVED LOCAL)

**Imported authentic source normalization:** for fixed `a>0` and `v∈C_c^∞(-a,a)`, set `u=iv'`, `d_j=4j+1`. From the original Suzuki/Gamma decomposition (PR #71/#76/#85, with true Euler prime powers, half density, exactly one Gamma, pole channels and scalar contact retained), truncating **only the positive Gamma bath** gives

\[
Q_\zeta(v,v)-Q_{\zeta,J}(v,v)=
\frac1{2\pi}\int_{\mathbb R}
\sum_{j\ge J}\frac4{d_j(\xi^2+d_j^2/4)}\,|\widehat{iv'}(\xi)|^2\,d\xi.\tag{PDM-12}
\]

Every term on the right is nonnegative. Since each resolvent multiplier is maximized at `xi=0`, its **exact best multiplier bound** is

\[
\boxed{E_J^*=\sum_{j=J}^\infty\frac{16}{(4j+1)^3}}
\quad\text{and}\quad
\boxed{0\le Q_\zeta-Q_{\zeta,J}\le E_J^*\|v'\|_2^2.}\tag{PDM-13}
\]

This constant is the sharp **support-uniform** bound, where all compact support lengths `a` are allowed. Indeed choose fixed smooth nonzero `phi` and rescale `v_L(x)=sqrt(L)phi(x/L)`; the derivative L² norm is unchanged and its normalized Fourier energy concentrates around `xi=0`. By bounded continuity of the Gamma multiplier, the Rayleigh ratio converges to its value `E_J^*` at zero. **At a fixed compact support radius** the optimal constant can be lower, and no sharper claim is made.

Exact rational integral comparisons give, for `k=J+M` and any `M>=0`,

\[
S_{J,M}+\frac2{(4k+1)^2}
< E_J^* <
S_{J,M}+\frac2{(4k+1)^2}+\frac{16}{(4k+1)^3},
\quad S_{J,M}=\sum_{j=J}^{J+M-1}\frac{16}{(4j+1)^3}.\tag{PDM-14}
\]

These bounds converge effectively as `M->∞`, and at `M=0` recover the PR #94 valid `2/(4J+1)^2+16/(4J+1)^3` upper budget. The false earlier proposal `1/(8J²)` fails already for `J=1` since its first omitted term `16/125>1/8`. This is *not* a novel spectral theorem; it is the corrected, source-true optimal constant and a reusable exact rational certificate of the existing Gamma tail.

**Asymmetric sign consequence:** if a valid full-source enclosure for **one** test gives `Q_J(v,v)>=0`, then `Q(v,v)>=0`. If instead a verified upper bound plus `E_J^*||v'||²` is negative, the full original Weil value at that test is negative. A signed test's *numerical* lower bound alone never proves that every admissible test is nonnegative. One negative genuine full-Weil witness would refute RH; no such witness is reported here.

## 9. PDM-09 — two-axis certified Schur reduction (CLASSICAL SUFFICIENT THEOREM)

Work in the **specified Hilbert/form norm**, not an arbitrary L² basis, and split `H=F⊕K` orthogonally with `dim F=m<∞`. Let `Q` be a bounded Hermitian form (for instance the bounded Riesz form induced by the original Weil form in an audited `H0¹` topology). Let `Q_J` be another bounded Hermitian form with uniform operator-form error `||Q-Q_J||<=epsilon` and exact block certificates:

- `Q_J(f,f)=<f,Mf>` for a symmetric/Hermitian finite matrix `M`;
- `Q_J(w,w)>=kappa||w||²` on the entire infinite complement `K`;
- `|Q_J(f,w)|<=L||f|| ||w||` for all `f∈F,w∈K`.

Assume `0<=epsilon<kappa`. Then for every `f+w`, by orthogonality and the uniform form error,

\[
Q(f+w)\ge <f,(M-\epsilon I)f>-2L\|f\|\|w\|+(\kappa-\epsilon)\|w\|^2.
\]

Completing the square proves the sufficient condition

\[
\boxed{M-\left[\epsilon+\frac{L^2}{\kappa-\epsilon}\right]I\succeq0\quad\Longrightarrow\quad Q\succeq0.}\tag{PDM-15}
\]

The executable exact rational engine uses the **more conservative** `(L+epsilon)^2/(kappa-epsilon)` instead of `L^2/(kappa-epsilon)`; this is still sufficient, and avoids weakening an external cross-block error allowance. It checks finite symmetric PSD using rational congruence pivots, correctly handling singular PSD and returning an explicit negative original-coordinate Rayleigh vector if a matrix is indefinite. Independently written exhaustive principal-minor oracles agree on 300 random `1×1`–`4×4` matrices.

**Crucial unsatisfied source contracts:** neither `M`, `L`, nor the all-test complement `kappa` have been computed from actual source-certified Weil inputs in this PR. The existing PR #86 *claims* a 30-moment complement bound; it requires independent proof audit and a genuine basis/coupling construction before insertion. The engine always returns `claimed_authentic_weil_coefficients_verified=false`. A positive toy Schur matrix is **not** an RH proof, nor yet a first-prime-window proof.

## 10. Dependence graph, proof debt still owed, and next discriminator

```
 AUTHENTIC INTEGER EULER + ONE GAMMA + POLES + CONTACT + HALF-DENSITY
        | (existing true signed Weil source identity; no zero lookup)
        v
 SIGNED WEIL FORM Q and finite-Gamma approximants Q_J
        | (PDM-08: sharp rational source-positive error; PROVED LOCAL)
        v
        certified analytic depth J ----\
                                      +--> two-axis Schur certificate PDM-09
        certified test-complement --->|            |
        source coupling B and M ------/            |
                                          [missing authenticated M,B,kappa]
                                                    |
                                                    v
                                  ALL-TEST Q >= 0 on one interval
                                                    |
                                  all compact intervals (still missing)
                                                    v
                                               Weil <=> RH
```

**Genuinely next mathematical experiment:** start at `a=1/2`. Audit the PR #86 infinite-dimensional 30-moment coercivity claim in the actual `H0¹` form norm; build *source-verified* moment-dual basis functions, matrix entries and cross operator estimates. Predeclare the expected outward error for Gamma mode truncation and finite spatial quadrature; prove a finite-dimensional Schur bound with a rigorous infinite complement bound. If it cannot close, retain the exact failed numerical/source inequality as a research obstruction, not a positive theorem. Above all, check that changing the form topology doesn't destroy the supposed coercive complement.

## 11. What should change in SUCC architecture

Promote source-typed proof debts into the generic mathematical engine instead of pretending they are numbers attached to arbitrary facts. A theorem application should expose at least (a) original source/epoch/basis/domain, (b) stable original target vs changing target, (c) successor law and whether it is a checked universal premise, (d) outstanding epistemic/analytic/semantic/resource components, (e) mathematical completion/carrier topology, (f) the specific bridge (compactness, effective modulus, closed target, Schur), (g) a full-domain versus finite-sample proof-status flag, and (h) a negative witness or the remaining unresolved obligation. Proof discovery should minimize the *right* debt rather than attempting to make every metric numerically small.

## Reproducibility

Python standard library, `Fraction` only, no source access outside the checked-out repository and no `zeta`/zero lookup. New files: `observational_succ/zeno_proof_debt.py`, `tests/test_zeno_proof_debt.py`, `tests/test_zeno_epsilon_probes.py`, `scripts/zeno_proof_debt_probe.py`, deterministic source receipt, scoped claim ledger, and a dedicated Python 3.10/3.13 CI workflow. Run the focused suites and byte-identical frozen receipt, then full SUCC CI and source provenance. Tests check **finite exact instances only**, paper arguments carry the universal theorems. Full suite and Lean cannot be presumed passed until verified at the exact remote head.

### Scholarly sources

- SUCC PR #94: `research/2026-10-14/ZENO_SUCC_GLOBAL_CERTIFICATES.md` (direct parent); PR #93: the independent Black Sun IV Zeno audit; SWM B09, F45; Global Model Sandwich PR #77; Recursive Meta-SUCC PR #80; genuine Weil PR #71, #76, #85, #86.
- Dini theorem: classical compactness argument; UCL analysis notes https://www.homepages.ucl.ac.uk/~ucahad0/3103_handout_5.pdf
- Computable analysis: Klaus Weihrauch, *Computable Analysis* (2000), Springer https://doi.org/10.1007/978-3-642-56999-9 ; Brattka–Gherardi–Pauly, *Weihrauch Complexity in Computable Analysis*, arXiv:1707.03202; Stanford Encyclopedia of Philosophy, *Computability and Complexity* https://plato.stanford.edu/entries/computability/ .
- Suzuki Weil screw theory: https://arxiv.org/abs/2606.09096 (author/source normalization as documented in PR #71/#76); these results do not supply the missing signed all-test inequality.
