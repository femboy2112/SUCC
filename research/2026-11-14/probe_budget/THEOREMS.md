# Principia Observatoris — The Lawful Probe Budget Forge

**Research date:** 2026-11-14. **Status:** draft, not merged. **Stack:** PR #626 (`9728718f3d04eda8c7aef83de23be549ec52eca8`). **Scope:** finite declared source tables, deterministic readout-before-update probes, positive rational costs, one actual prepared source in a finite uncertainty fiber, and finite source actions. Theorems below are elementary/classical unless explicitly designated a new-to-SUCC synthesis. Scholarly priority, source-map adequacy, physical realizability, and quantum generalization are NOT established. Original BBP source and zero seed are untouched.

## 0. Contracts, three different budgets, and the 'oracle' firewall

The source is a finite set `X={0,...,n-1}` with a presently known report `q:X→Y` and a supplied family of **source dynamics** `T_g:X→X`. A registered probe `p_i` comprises a total source-relative readout `r_i:X→O_i`, a **source update** `U_i:X→X` (identity if nondisturbing), a positive rational cost `c_i`, and an available/unavailable menu flag. The readout is taken **before** its update; records are stored in observer memory. A model's `available=True` means only *declared lawful inside this source table*, not physically attested. A label called `source_ID` or a `readout(x)=x` map gains no evidentiary authority unless independently authenticated as an actual instrument. Unregistered or unavailable probes are excluded from every optimizer.

Target `P:X→V` describes the **original** state unless stated otherwise. Distinguish three mathematical quantities:

- `C_fixed(P)`: minimum total cost of one fixed set of compatible, nondisturbing probe readouts sufficient to know `P`, given `q`.
- `C_active(P)`: minimum **worst-case total** cost of a terminating adaptive single-copy policy, permitting declared probe updates and no undeclared reset, which determines `P` for every possible original source.
- `C_lift^point, C_lift^stoch`: minimum cost of a fixed set of nondisturbing probe channels whose **refined current-state report** has a well-defined descended source `T`-action and admits respectively an exact equivariant point or normalized stochastic section.

All costs may be `+∞` if the declared menu is insufficient. **Do not compare these quantities as though the corresponding output contracts were the same.** A point section is only a coherent representative convention, not identification of the actual source. A stochastic section is not an empirical posterior. An apparently lawful probe which alters the carrier cannot be repackaged as a persistent static readout without paying for its destructive update.

## PB-01 — Exact minimum fixed identification = weighted pair cover (CLASSICAL/PROVED)

For each original pair `(x,x')` with `q(x)=q(x')` but `P(x)≠P(x')`, define its distinguishing menu `D(x,x')={i: r_i(x)≠r_i(x')}` over admitted **passive** probes.

**Theorem.** A fixed subset `S` identifies the original target for every admissible source iff `S∩D(x,x')≠∅` for every such pair. Hence

`C_fixed(P) = min_{S} Σ_{i∈S}c_i` subject to those pair-cover constraints.

**Proof.** If a target-disagreeing pair shares the old report and every selected new readout, it reaches the same terminal evidence with different target values; no decoder is possible. If every conflicting pair is separated, every nonempty joint evidence fiber is `P`-constant. Source-relative target descent produces a unique decoder on the realized evidence image. The identity source updates permit executing every selected probe sequentially on one copy with unchanged source value. Finite enumeration returns the exact cost. QED.

**Complexity receipt.** Minimum fixed probe budget contains weighted SET COVER: given universe `U` and covering subsets `S_i`, make for each element `u` two states `(u,0),(u,1)`, give them the same initial report `q(u,b)=u` and opposite target `P(u,b)=b`, and set readout `r_i(u,b)=b` if `u∈S_i`, otherwise `0`. Only the pair within each `u` must be distinguished, and probe `i` does so iff `u∈S_i`. The optimum equals weighted set cover. Thus the unrestricted optimization is NP-hard (by the classical set-cover result), despite the elementary iff. We claim no polynomial-time universal algorithm. [Karp 1972](https://doi.org/10.1007/978-1-4684-2001-2_9), [minimum test set background](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf).

**Hostile case:** pairwise separation by *counterfactual destructive* probes is not enough; PB-02 uses actual updates. An unadmitted `r_i(x)=x` is not an admissible reduction of the optimum.

## PB-02 — Exact adaptive single-copy minimax budget (CLASSICAL/PROVED)

The sufficient belief state is a **set of pairs** `B⊆X_original×X_current`. Initially for each known current report `y`, `B_y={(x,x):q(x)=y}`; when historical uncertainty is already present, a separately authenticated initial belief may instead contain `(a,c),(b,c)` with different past origins and identical present state `c`.

For an allowed probe `i`, partition `B` by its *current* output `r_i(current)`; in outcome `o`, replace each pair `(original,current)` by `(original,U_i(current))`. Let the resulting nonempty beliefs be `B_{i,o}`. A terminal belief is one where all original coordinates have the same target value.

**Theorem.** With positive costs and a finite source/menu, the minimum sure-win worst-case cost `V(B)` is characterized by

`V(B)=0` if the original target is constant on `B`, and otherwise

`V(B)=min_i[c_i + max_{o possible} V(B_{i,o})]`, interpreting unavailable/infeasible continuations as `+∞` and taking the **least finite winning-policy solution**, not an arbitrary algebraic fixed point. If no finite winning policy exists, `V(B)=+∞`.

**Proof.** Every successful policy has an allowed first probe and must subsequently succeed on **every** actual outcome branch; its worst-case cost is the displayed expression for that first probe plus the worst descendant. Conversely, selecting an action attaining a finite recurrence value and recursively doing so constructs a policy. A proper winning policy can be pruned of repeated identical beliefs on one branch: its later subtree already works from the earlier identical belief, and all costs are positive. Thus it suffices to search policy depth at most the finite number of reachable beliefs. The monotone backward algorithm starts with target-constant leaves at 0 and assigns a state a finite value only after all outcomes of an action have finite values; after at most that many rounds it reaches the optimal finite policy and leaves exactly the unwinnable beliefs. QED.

**Independent certificate:** For a reported finite `V(B)`, an explicit chosen action at each intermediate belief attains the recurrence. For every action, a Bellman inequality certifies no cheaper alternative. For a reported `+∞`, the nonterminal **losing region** is closed under adversarial response: after every available probe at least one possible outcome remains in that region. The source code independently replays all terminal-policy branches and checks both certificates; mutation tests reject forged optimal values and forged impossibilities.

**Strict adaptivity witness:** `X={A0,A1,B0,B1}`, initial report constant, three unit-cost nondisturbing probes `group`, `A_detail`, and `B_detail`. Every fixed identifying set needs all three (`C_fixed=3`), but one can probe `group` then the appropriate detail, giving `C_active=2`. These are **worst-case**, not Bayes-expected, budgets. The original Hyafil–Rivest 1976 paper treats an *expected-cost* binary decision-tree problem, so its particular hardness theorem is not silently used as a proof of our worst-case Bellman formula; see [publisher DOI](https://doi.org/10.1016/0020-0190(76)90095-8).

**Destructive control:** `X={A,B,C}`, readouts `r_a=1_A`, `r_b=1_B`, and both updates send all states to `A`. Although the two hypothetical readouts separate all three initial states, no single-copy policy identifies `P=1_C` from a uniform initial belief; the losing-trap certificate finds the irreparable pair. Replacing them with actual nondisturbing versions (a *different*, stronger toolkit) gives cost 2.

## PB-03 — Observation refinement must first descend the source action (PROVED)

For an admitted passive subset `S`, define the refined **joint** report

`q_S(x)=(q(x),(r_i(x))_{i∈S})` on its realized image.

**Theorem.** For each source generator `T_g`, an observed action `\bar T_{g,S}` satisfying `q_S∘T_g = \bar T_{g,S}∘q_S` exists iff

`q_S(x)=q_S(x') ⇒ q_S(T_g x)=q_S(T_g x')` for all `x,x'`.

**Proof.** Necessity is applying the proposed observed action to two equal reports. For sufficiency define `\bar T_{g,S}(q_S(x))=q_S(T_g x)`; the condition makes this independent of representative and uniquely defined on the actual image. QED. This is the deterministic specialization of SUCC's existing source/descent contract, not a new universal discovery.

If the condition fails, return the pair `x,x'` and generator as a *noncongruence witness*. The verdict is **there is no well-defined observed T-action here**, NOT “there is a T-action but no stochastic section.” The two obstructions are categorically different.

## PB-04 — Exact minimum equivariant lift budget (PROVED finite algorithm)

Define `Adm` as the explicitly listed available nondisturbing probes, with individual costs. For `kind∈{point,stochastic}`,

`C_lift^kind = min{ Σ_{i∈S}c_i : S⊆Adm, q_S is action-congruent, and q_S admits a kind-compatible section }`.

A deterministic section is a tuple of source choices `s_y∈q_S^{-1}(y)` satisfying `T_g s_y=s_{\bar T_g(y)}`. A stochastic section is a nonnegative rational kernel `K_y` with support in the source fiber, row sums 1, and `T_{g*}K_y=K_{\bar T_g(y)}`. For finite rational tables, stochastic feasibility is a bounded rational linear program. Its nonempty compact feasible polytope has a rational vertex; a complete positive-support vertex enumeration is an exact feasibility algorithm. Infeasibility is distinguishable from exhausting a declared size cap: the latter **raises an error**, not “no lift.”

Enumerate candidate subsets by cost, reject noncongruent partitions with witnesses, then test exact point (finite enumeration) or stochastic (rational LP) sections. The first success is globally minimum-cost. If every subset is checked without success, no admitted fixed passive refinement achieves that goal. A point section induces a Dirac-valued stochastic section, so necessarily

`C_lift^stochastic ≤ C_lift^point`, with possible strict inequality or both infinite.

**Warning:** unlike PB-01, admissible *refinement does not preserve lift existence monotonically.* A selected extra probe may impose a new incompatible dynamical constraint. Hence the fixed target-cover formula cannot optimize the lifting problem.

## PB-05 — Exact two-stage upgrade: no lift → stochastic-only (cost 2) → point (cost 5) (PROVED MODEL)

Let `X=(a1,a2,b1,b2,c,d)`, encoded `(0,1,2,3,4,5)`, with source update

`T=(2,3,4,5,5,4)`; equivalently `a1→b1→c↔d←b2←a2`.

Base observer report `q=(u,u,w,w,w,w)` merges the entire intermediate/cycle field. The available nondisturbing probes are

- `m=(0,0,1,1,0,0)`, cost 2: distinguishes middle pair `{b1,b2}` from final cycle `{c,d}`.
- `v=(0,1,0,1,0,1)`, cost 3: distinguishes the two partners within all three pairs.

**Base NO-LIFT proof:** Any source distribution `K_u` is supported on `{a1,a2}`. Its image under `T` lies in `{b1,b2}`, forcing `K_w` to be supported there. But report `w` is absorbing, so `T_*K_w=K_w`. Under repeated `T`, the intermediate states leave `{b1,b2}` and enter the recurrent cycle `{c,d}`, so no invariant probability can be supported on `{b1,b2}`. Contradiction; no stochastic or point section.

**With `m`:** The report refines into three fibers `{a1,a2}`, `{b1,b2}`, `{c,d}` with chain `u→v→w→w`. Assign uniform `(1/2,1/2)` on each source pair. This is T-equivariant. There is **no deterministic section**, since the terminal `w` must select a fixed point of the swap `c↔d` and none exists. Thus `C_lift^stochastic = 2` because the empty selection is impossible, while `m` succeeds; `v` alone does not define a descended report T-action.

**With both probes:** Joint reports are injective and the observed T-action is conjugate to the actual source action, so the inverse report map is a deterministic equivariant section; cost `2+3=5`. Neither empty selection nor `m` works deterministically, and `v` alone is noncongruent. Thus `C_lift^point=5`. All four subsets were audited in exact rational arithmetic.

This is an upgrade of the *mathematical representation*, not a claim that the stochastic lift accurately samples an already selected actual source without a prior. In particular, the uniform choice on a two-cycle is not automatically the real-world posterior about which initial branch occurred.

## PB-06 — Refutation: more passive information can abolish a previously valid lift (PROVED)

Let `X={a,b,c}` with `T(a)=b,T(b)=c,T(c)=c`. Initially let `q` be the constant report. The equivariant point section `s(*)=c` exists, as does the Dirac stochastic section `K_*=δ_c`.

Now add a **genuinely nondisturbing** readout `r(a)=1,r(b)=r(c)=0`. The refined report is a valid deterministic T-quotient `u→w→w`. But an equivariant kernel is impossible: `K_u=δ_a` forces `K_w=δ_b`, while stationarity at `w` requires `K_w=δ_c`. Thus additional information can strictly destroy an exact **backward dynamical section**. An otherwise legal readout `r(b)=1,r(a)=r(c)=0` causes the refined report action not to descend at all, by PB-03, a third distinct outcome.

**No contradiction:** All previously available observation information is retained. The ability to infer the original *target* from accumulated nondisturbing probe records is monotone. What fails monotonicity is the **existence of one globally T-consistent representative/probability assignment over every newly created report class**.

## PB-07 — A point section does not certify actual source identification (PROVED COUNTEREXAMPLE)

For a constant current report on three states with the **identity** source action, `s(*)=x0` is a completely valid equivariant point section at zero probe cost. If no admitted probe distinguishes states `x1,x2`, the actual source ID is *not* identified, and `C_fixed(ID)=C_active(ID)=∞` under that menu. Thus point lifting may be free precisely when actual source identification is impossible.

Conversely a target `P` already determined by q may have `C_fixed(P)=0` even if the q quotient has no stochastic right inverse (PB-05). Do not collapse target knowledge, representative choice, and actual source history into one scalar resource statistic.

## PB-08 — Source history after merging has an infinite present-only probe budget (PROVED)

Let histories `γ_a=(a→c)` and `γ_b=(b→c)` produce the **same current source state** `c` with different original labels. Even a perfectly source-state-injective identity probe `p(current)=current` cannot distinguish their *past* origins, because every lawful probe depending only on current state sees the same input and every common update keeps subsequent reports equal. The exact single-copy original/current belief is `{(a,c),(b,c)}`; with target `P(a)≠P(b)`, the coinductive losing-region certificate proves `C_active(P)=∞` for a present-state-only menu. An archived source tag or independently authenticated history-sensitive signal would be a different instrument and must be priced as such.

## PB-09 — Optimality evidence and hostile controls (OBSERVED finite / CLASSICAL proof)

The code supports exact finite-action quotient reconstruction and a finite-belief AND/OR solver. The tests deliberately attack the following tempting shortcuts:

1. **Invented ID probe:** unavailable readouts are ignored; an available `r(x)=x` is valid only as a *declared model probe*, not as a physical identification.
2. **Destructive masquerade:** a source-updating probe is rejected from passive joint-refinement optimization, but allowed in the actual single-copy policy game with its declared update.
3. **Counterfactual ≠ executable:** a pairwise separating readout bank cannot overcome destructive state erasure unless some allowed policy actually succeeds.
4. **Present ≠ history:** state identity probing fails on merged historical origins.
5. **Congruence ≠ lifting:** a refined observed T-action may descend while no compatible probability lift exists.
6. **Probability ≠ possibility:** a feasible K is a dynamically coherent stochastic section, never a posterior without an independently supplied source prior/likelihood.
7. **Source ambiguity:** the tool's `available=True` bit records modeling permission, not physical authentication.
8. **False optimality/impossibility:** certificate mutations change values or fake winning/losing states; the verifier rejects them.
9. **Wrong source family:** source and report actions are table data; all-N and external physical transfer require an actual source map.

**Independent oracle:** a separately implemented, budget-decreasing enumerator checked 320 randomized finite models for fixed probe cost, 250 exactly bounded adaptive valuations with budget ≤6, and 70 certified losing models against all budgets 0..6. The exact stochastic LP solver independently recovered the existing PR #626 three-state one-generator census of 279 source/report tables, 24 without an equivariant stochastic section. These are computational checks, not universal proof substitutes. Exact commands/logs in `VALIDATION.md`.

## PB-10 — Where the next claim actually changes (OPEN)

A new theorem would characterize the **minimum lawful resource cost of genuine posterior calibration** for source Markov kernels and stochastic observation outcomes. The present code handles deterministic readouts/updates, and a backward T-compatible probability assignment *without* claiming to represent the actual selected source. The next discriminator should preserve original-source labels and all outcome probabilities, then compare minimum budgets for (i) point identification, (ii) target identification, (iii) stochastic future prediction, and (iv) statistically calibrated posterior inference.

More ambitious extensions require explicit time-dependent action menus, partial action/refusal contracts, calibrated observation noise, continuous/carrier limits, single-copy quantum instrument restrictions, and actual SUCC arithmetic source authentication. Neither invoking a hypothetical identity observer nor writing a `source_ID` probe creates those resources.

### Provenance and literature firewall

- SUCC [#625](https://github.com/femboy2112/SUCC/pull/625): OC-1..OC-6, source identity, nondisturbing observation and history.
- SUCC [#626](https://github.com/femboy2112/SUCC/pull/626): EC-01..EC-10, equivariant point/probability sections, LP/Farkas, minimal single-T no-go, Markov lift obstruction, analytic-limit defect.
- SUCC [#47](https://github.com/femboy2112/SUCC/pull/47): exact set-valued successor descent and the proof that support does not determine likelihood.
- SUCC `docs/CARRIER_RELATIVE_TARGETS.md`: target factorization, the observer algebra and destructive single-copy witness.
- [Karp 1972, Reducibility Among Combinatorial Problems](https://doi.org/10.1007/978-1-4684-2001-2_9): classical set-cover hardness.
- [Hyafil and Rivest 1976, Constructing Optimal Binary Decision Trees Is NP-Complete](https://doi.org/10.1016/0020-0190(76)90095-8): **expected** cost decision-tree hardness; not a proof of our worst-case statement.

**Claim ledger summary:** PB-01..04 and 06..08 = PROVED PAPER / CLASSICAL under exact finite contracts; PB-05 = exact finite theorem with independent exhaustive calculation; PB-09 = OBSERVED exact test evidence; PB-10 = UNVERIFIED next theorem. Source-map adequacy remains UNVERIFIED for all models. No normality, RH, physical inflation, quantum universal knowledge or source-free Einstein result is inferred.
