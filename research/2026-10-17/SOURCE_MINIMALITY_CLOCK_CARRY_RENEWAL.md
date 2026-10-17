# Operation SOURCE MINIMALITY — finite-observer cofinality, lawful carry, renewal and analytic camouflage

**Date:** 2026-10-17. **Research status:** CLASSICAL structural imports with independent paper derivations; new-to-SUCC source classifications, finite executable countermodels and noncircularity audit. **Stacked parent:** `research/prime-jet-genesis-affine-rigidity-2026-10-17@1bcebd265ee78ae6faef5995467df6c1d85b42cf` (PR #157). **RH proved: NO.** No original Tate, Gamma, signed Weil, Suzuki, source passports or provenance imports changed; no zero ordinate is read.

## Abstract and strongest defensible result

Bare prime jets / free FUCC words do not force the positive integers. PRIME GENESIS #157 proved a conditional rank-braid rigidity theorem and reconstructed the ordinary primes from the **entire** universal procyclic quotient system. Here we isolate precisely the source debt:

> Within the category of *rooted cyclic finite observers*, with genuine predecessor-free successor actions, unique root-preserving equivariant quotient maps, and closure under finite quotient and rooted simultaneous-product observations, the inverse-limit carrier is `Zhat` **if and only if** each prime-power period is observed/cofinally represented. Equivalently, both full simple-prime exposure and unbounded prime-specific refinement depth hold. This is a necessary-and-sufficient relative characterization, NOT a proof that an actual observer produces all clocks.

The missing prime-power refinement admits a finite-state constructive **carry-coupled skew product**. But its causal accessibility is an additional, testable constructor law. A logically different sufficient condition is an **exact shift-renewal equation** for the counting measure on the independently normalized positive-real additive carrier. Neither is implied by prime jets, any finite amount of observation, a first unit calibration, an ordinary prime-number theorem, density-one counting, or even the critical-strip zero divisor of zeta.

The last conclusion has an explicit rational countermodel: replace prime generator `3` by `9/2` and `5` by `35/11`; retain every other rational prime. This is a collision-free Beurling generalized integer system with first cell `1->2`, `N_B(X)~X`, `pi_B(X)=pi(X)+O(1)` and a generalized zeta function `zeta_B(s)=zeta(s)F(s)` where `F` is holomorphic **and nowhere zero** throughout `Re(s)>0` with `F(1)=1`. Its rank braid nevertheless fails on a finite rational witness. **Zeros alone are not a source-authentication mechanism.**

## 0. Recovered source contract; dependencies and originality

Existing SUCC: `research/2026-10-17/PRIME_JET_GENESIS_AFFINE_RIGIDITY.md` (PJG-01–13), `PROFINITE_INDEX_SOURCE_GENESIS.md` (PIG-01–07), `observational_succ/prime_jet_genesis.py`, `profinite_index_genesis.py`, the carrier atlas and Yoneda/no-ghost foundations. We deliberately *do not* assume that finite C_m already implements an infinite free p-jet chain; the parent PIG paper correctly warned against this. The new `authenticate_prime_word` check makes that warning executable.

A source record must carry: (i) finite rooted transition graph, (ii) observed exact period, (iii) root-preserving equivariant bonding map, (iv) which predecessor/independent-product/carry edges were physically or programmatically justified, (v) domain, arithmetic precision, epoch, source cost and identity, (vi) whether the conclusion is finite, cofinal, a typed construction schema, or an inaccessible mathematical limit. No label alone is a proof of source access. All numerical tests below use exact integer/Fraction computations; transcendental analytic theorems are paper proofs.

**Classical prior art:** procyclic/supernatural-number classification (e.g. Ribes–Zalesskii *Profinite Groups*, classification of procyclic groups; a standard accessible reference is the Springer survey on procyclic groups and supernatural orders), Beurling generalized arithmetic, Euler products/convolution exponentials (Diamond–Zhang *Beurling Generalized Numbers*, Chapters 2–3). The simple generalized-prime perturbation, odd/even carry construction, renewal equation and finite shadow are presented as elementary derivations/controls, with academic priority **UNVERIFIED**. No claim of new RH theorem.

## 1. SM-01: exact observation category and supernatural classification

Take the free rooted unary successor action. Its reversible connected finite quotients are rooted cycles `C_m` of period `m>=1`, with distinguished root `0` and `S(k)=k+1 mod m`. For rooted successor-equivariant maps `C_m->C_n`, equivariance and root conservation force `f(k)=k mod n`; this map is well-defined **iff** `n|m`, and is then unique. An unrooted equivariant map has `n` phase shifts, which cannot be silently used as independent aligned source histories.

Let `D` be a **nonempty** collection of available periods closed under (Q) division and (P) lcm. The lcm operation comes from the successor orbit of the paired-root observer, **not** automatically from the full Cartesian product: the orbit of `(0,0)` in `C_m × C_n` under simultaneous successor has period `lcm(m,n)` and occupies exactly `lcm(m,n)` of the `mn` ordered pairs. For `m=4,n=6`, this is 12 states inside a 24-state product, partitioned into two orbits.

Set for each ordinary metatheoretic prime `p`:

`e_p = sup { v_p(m): m in D } in N_0 union {infinity}`.

**CLASSICAL / paper proved:** `D={m>=1 : v_p(m)<=e_p for all p}`. The forward inclusion follows by definition. For reverse inclusion, for the finitely many `p|m`, the supremum condition supplies a period divisible by `p^{v_p(m)}`; taking a divisor produces that prime power inside `D`; taking finite lcm produces `m`. Thus `D` is completely classified by the supernatural number `N_D=product_p p^{e_p}`.

By CRT, coherent sequences of residues split prime-by-prime, yielding the canonical isomorphism of topological pointed procyclic groups

`L_D = lim_{m in D} C_m  ≅  product_p C_{p^{e_p}}`,

where `C_{p^0}={0}`, finite exponent means `Z/p^{e_p}Z`, and infinite exponent means `Z_p`. The diagonal successor root is the element `(1)_p`, dense by finite CRT. In particular:

`L_D ≅ Zhat (as rooted procyclic groups)  <=>  e_p=infinity for EVERY p`.

Equivalently, the local source must produce *each prime power* somewhere in the directed diagram. This equivalence is under the explicitly declared cyclic-observer category, not for arbitrary source graphs or noncommutative observers.

## 2. SM-02: minimal independent obligations (relative, not absolute)

Within that category, the universal condition splits into:

- **Simple-exposure (E):** every prime-index simple quotient occurs: for every metatheoretic prime p, `C_p` exists as an authenticated finite-source object.
- **Power-lift (L):** for each exposed p and each k>=1, a compatible rooted quotient extension `C_{p^{k+1}} -> C_{p^k}` is available when `C_{p^k}` is available; the source maps and actual higher-depth period must be verified.
- **Finite gluing (G):** periods can be divided and root-product/lcm combined with the exact unique bonding maps.

`(E)+(L)+(G)` suffice for all `C_m`: construct every `C_{p^k}` and combine distinct p-power clocks by coprime CRT/lcm. Conversely, a universal diagram requires (E) and arbitrarily deep (L), while (G) is the ambient finite-observer closure convention.

Independence countermodels:

- Only `2^k` periods: arbitrary depth and indefinitely many fresh refinements, but fails (E) for odd primes.
- All squarefree periods: every simple prime quotient, and directed quotient/lcm closure, but fails (L) for every `p^2`. Limit is `product_p C_p`, *not* `Zhat`.
- Periods from primes in a fixed finite set with all powers: unbounded depth for every **observed** p, but not (E) globally.
- Every period allowed except 2-power exponent above a fixed `e>=1`: infinite procyclic group possessing **every** simple-prime quotient but missing `C_{2^{e+1}}`.

There is no absolute 'weakest law' without first declaring a source-language, allowed primitive operations and ordering of axiom packages. The above is a **necessary/sufficient characterization within a fixed clock-observer category**, not a unique minimal foundation for all conceivable SUCC models.

## 3. SM-03: finite observational saturation is not universal access

For a **finite** adaptive transcript querying rooted clock periods `m_1,...,m_r`, set `M=lcm(m_i)`. The finite source `C_M` contains every observed quotient and reproduces the exact rooted bonding maps *between the queried clocks*. It does not contain the next `2^{v_2(M)+1}` clock. Therefore no finite positive transcript (including adaptive branching that actually makes finitely many queries) proves universal availability. A finite quotient agreeing on finitely many queries is a countermodel for that transcript's inferred universality, not necessarily for any globally assumed source axiom.

A sharper version remains **infinite** and possesses **all simple prime quotients**. Put `e=max(1,v_2(M))` and let `D_e` permit all periods whose 2-adic exponent is at most `e`, with no cap on any odd-prime exponent. Its inverse limit is `C_{2^e} × product_{p odd} Z_p`. Every finite query in the transcript is matched, every `C_p` simple quotient exists, yet `C_{2^{e+1}}` does not. The exact distinguisher and the claim's scope are recorded in the deterministic receipt.

This is a probe-gap theorem, not evidence that actual observers cannot eventually construct a mathematical presentation of all finite clocks. An **algorithmic constructor with a proved universal schema** is mathematically stronger evidence than any finite list of completed clock experiments; it still does not perform infinitely many real-world executions in finite time.

## 4. SM-04: source-lift by carry — an actual finite automaton

Let `C_m x C_p` be the state set of a low `m`-clock and high `p`-clock, with root `(0,0)` and **coupled** transition

`T_c(x,y)=((x+1) mod m, (y + c*1_{x=m-1}) mod p)`.

For `c` an exact integer, after each complete low lap the high coordinate advances by `c mod p`. If an orbit returns to its root after `t` steps, `t` must be a multiple `m*l`, and high return is equivalent to `l*c=0 mod p`. Minimal `l=p/gcd(c,p)`. Thus the root orbit period is **exactly**

`period(T_c)=m*p/gcd(c,p)`.

The full `mp`-state machine has `gcd(c,p)` disjoint successor cycles; it is a **connected rooted C_{mp}** iff `gcd(c,p)=1`. Projection `(x,y)->x` is a lawful root-preserving successor-equivariant quotient onto `C_m`.

When `p|m`, uncoupled diagonal `(x+1 mod m,y+1 mod p)` has only `m` states in its rooted orbit. The carry gate with `c=1` raises it to `mp`, establishing a **true prime-power lift**, not the fake `C_p × C_p -> C_{p^2}` slogan. If `c=p`, the lift fails and the high states become disconnected, despite every local component still appearing to be a correct counter. Exact controls: `C4` with `C2`: uncoupled period 4; genuine carry period 8; corrupt carry amount 2 period 4.

**Generative corollary (conditional, paper proved):** If every primitive simple `C_p` can be constructed, its carry update and high-counter memory are source-authorized at every depth, and coprime rooted products are lawful, then all finite periods are constructible. This yields the universal procyclic inverse diagram, whose mathematical completion is `Zhat`. The carry operation supplies (L) constructively; it does **not** generate missing prime species. Finite smoke tests do not verify physical/semantic access to unlimited storage, memory or energy. Exact resource budgets must grow with m,p and depth.

### SM-04B — A finite, proof-producing clock compiler (new source program)

`observational_succ/clock_compiler.py` accepts an explicitly declared passport of *observed primitive simple clock indices*, plus independent capability flags `allow_carry` and `allow_crt`, source ID/epoch and an explicit finite state budget. Given a requested finite prime-power factor word `((p_1,e_1),...,(p_r,e_r))`, it builds each p-adic odometer as an e-digit base-p register with **actual cascaded carries**, then forms the simultaneous product across coprime powers. The resulting transition system has `n=prod p_i^{e_i}` states in **one rooted cycle**. This is not a label-only “expected period”: the generated machine verifies each of the n distinct states against an independent direct modular-time oracle, and returns to the origin exactly at time n.

**Source discipline:** A finite `C_30` may certify primitive seeds 2,3,5 without certifying an already-existing `C_{360}` quotient. Given newly authorized carry and CRT construction actions, however, a *new machine* `C_{360}` can be built. The compiler's receipt explicitly reports `all_power_clocks_already_observed_in_parent_source=false`, and refuses missing seed 7, unauthorized carry, unauthorized CRT, oversized memory budgets or duplicate/fake composite seeds. It does NOT upgrade declared source IDs into a physically authenticated observation; it is a finite program theorem with an auditable transition history.

For `n=2^3*3^2*5=360`, the exact completed orbit has 360 states. The register for 2 carries 180 times to its second digit and 90 times to its third; the register for 3 carries 120 times to its second. In general, over n steps the p-register carry into digit j (1<=j<e) occurs exactly n/p^j times, giving a precise causal-budget/cost observable beyond the mere final arithmetic size.

This compiler proves *finite constructive adequacy conditional on the allowed-source program constructors*. It does not, from one 360-state run, prove a physically executed all-n system or source-independent universal procyclic completion. A uniform program schema plus ordinary induction justifies each finite target in metatheory, with finite time/state resources increasing as the target grows.

## 5. SM-05: virtual FUCC words are not automatically real source clocks

This is a concrete boundary inherited from PIG #157. At finite stage `C_30`, the simple subgroup indices are {2,3,5}; freely generating words from the extracted primes yields a formal value 4=2^2. But the finite source `C_30` has **no** subgroup of index 4, since 4 does not divide 30. So formal FUCC `V_2^2` is computationally nameable but **not authenticated as an observed clock subgroup**. Similarly a squarefree infinite diagram has all primitive species but none of their square refinements. The new `authenticate_prime_word` reports `formal_free_word_exists` separately from `source_authenticated` and Haar mass. The latter is defined only if that exact finite quotient is supported.

This distinction is analogous to the project's existing source-map (sigma) vs pathway (phi) discipline: a syntactically constructible hypothesis is not automatically an accessible source observation.

## 6. SM-06: independent route — the exact Archimedean shift-renewal law

Let `ν` be a locally finite (nonnegative) Borel measure on the **independently supplied** additive real half-line `[1,infinity)`. Let `tau(x)=x+1`, with pushforward `tau_*ν`. Suppose the full source law is the **single global distribution identity**

`ν = δ_1 + tau_*ν`.

**Theorem (elementary / paper proved):** The unique locally finite measure satisfying it is `ν=sum_{n>=1}δ_n`.

**Proof.** Iterating `r` times yields `ν=sum_{j=0}^{r-1}δ_{1+j}+(tau^r)_*ν`. For any compact interval `[1,R]` and any `r>R`, the translated remainder has no mass in that interval because its support is `[1+r,infinity)`. Restrict the identity to the interval and let r grow. Hence `ν` coincides with the counting comb on every compact interval and thus globally. QED. The result remains valid for signed locally finite measures supported in `[1,infinity)` provided the stated distribution identity is well defined; no positivity was required in the telescoping proof.

Now assume `ν` is the pushforward of the free-FUCC prime-jet exponential under the declared real evaluation `q_j=e^{lambda_j}>1`, with **no** word collisions and unit atom mass. The renewal law then forces its support to be the ordinary positive integer lattice. As the source is multiplicatively free and maps bijectively onto the entire lattice, its primitive species map exactly to ordinary prime integers; rank multiplication and `V_pS=S^pV_p` become conclusions. This avoids assuming UDC or the full procyclic clock system, **but imports an independent exact additive-real translation law over every interval**. A finite measurement of the first cell and any ordinary mean-stationarity assumption are far weaker.

Why 'one equation' does not mean 'weakest': this equation already encodes the global additive successor as a *source operation*. It is an alternative sufficient package, not a consequence of prime jets or a demonstration of a physical observer generating unbounded translation covariance.

## 7. SM-07: explicit density-one, unit-calibrated, isozero Beurling counterfeit

Define `a=9/2`, `b=35/11`, and the generalized integer set

`B={m*a^j*b^k : m>=1, gcd(m,15)=1, j,k in N_0}`.

Equivalently, begin with all genuine rational-prime generators **except** 3 and 5, replace generator 3 with `a` and generator 5 with `b`, and take free finite products. Every generator exceeds 1; the generalized primes tend to infinity. The first two generalized integers are 1 and 2, so **the sole real first-unit cell** `[1,2]` has additive mass one.

### Exact free-factor uniqueness

For any word `m a^j b^k`, the 3-adic valuation is `2j` and the 5-adic valuation is `k`: `m` is coprime to 15, `v_3(a)=2`, `v_5(b)=1`, and cross valuations at 3 and 5 vanish. Equal positive rational word values force equal `j,k`; after cancelling, equal `m`. Hence the source has **no collisions**, and the counting measure is atomically unit-mass everywhere.

### Exact leading density equals one — infinite paper proof

Let `A(y)=#{1<=m<=y:gcd(m,15)=1}`. Elementary inclusion-exclusion gives `A(y)=(8/15)y+O(1)` and `0<=A(y)<=y` for all `y>=0` (take A=0 for y<1). The generalized count is

`N_B(X)=sum_{j,k>=0} A(X/(a^j b^k))`.

For each fixed `(j,k)`, `A(X/(a^j b^k))/X -> (8/15)a^{-j}b^{-k}`. The summands are dominated by `a^{-j}b^{-k}`, which is summable. Dominated convergence over the countable index set yields

`lim_{X->infty}N_B(X)/X = (8/15)/(1-a^{-1})/(1-b^{-1})`.

But `1-a^{-1}=7/9`, `1-b^{-1}=24/35` and `(7/9)(24/35)=8/15`, so

**`N_B(X) ~ X` with exact leading coefficient 1.**

This is a paper proof, **not** inferred from the finite list of observed ratios (which fluctuate).

### Prime number theorem and zeros still do not authenticate the source

Let `pi_B` count the declared generalized-prime generators by size, not generalized composites. Only 3 and 5 were deleted, and only `b` and `a` were inserted, so

`pi_B(X)-pi(X) = 1_{b<=X}+1_{a<=X}-1_{3<=X}-1_{5<=X}`.

The difference is bounded in absolute value by 1 for every X (ordered crossings 3 < b < a < 5). In particular the classical prime-number theorem transfers to `pi_B(X) ~ X/log X` without any new prime theorem.

On `Re(s)>1`, absolute convergence and multiplicative unique words give the Euler identity

`ζ_B(s)=ζ(s) F(s)`, with

`F(s)= ((1-3^{-s})(1-5^{-s}))/((1-(9/2)^{-s})(1-(35/11)^{-s}))`.

Every factor `1-q^{-s}` is holomorphic and **nonzero** for `Re(s)>0` (because `|q^{-s}|=q^{-Re(s)}<1`). Thus `F` is holomorphic and nowhere zero on that entire half-plane, with the exact rational value `F(1)=1` established above. It follows **without reading or specifying any zeta-zero locations** that `ζ_B` inherits the same nontrivial-zero divisor (including multiplicities) throughout `0<Re(s)<1`, and its pole at 1 has the same residue as ζ. This does not imply the generalized ζ has the standard functional equation, real Gamma factor, full Tate source, original signed Weil form, or RH positivity. It emphatically does not!

### The finite discriminators that kill the counterfeit

`ν_B` fails exact shift-renewal at `x=3` because 2 exists while 3 is absent: the residual `ν_B({3})-ν_B({2})=-1`. It has a novel atom at `35/11`, giving a `+1` renewal defect there. Its rank braid for multiplying by 2 fails at the finite source rectangle `x=4 -> Sx=9/2`, with `rank(2*Sx)-rank(2*x)-rank(2) = 9-8-2 = -1` within the tested horizon. These are **exact rational witnesses**.

**Consequence:** first-unit Archimedean calibration + density-one counting + ordinary-prime PNT + unaltered entire critical-strip zero divisor are **still not sufficient source laws**. Authentic local Euler normalization and the completed analytic test passports must not be replaced by those aggregated observables.

## 8. Dependency graph and proof authority

```
A. PROFINITE / CLOCK ROUTE (relative to finite unary source)
  rooted reversible finite clocks
    + quotient/pointed-product gluing                 CLASSICAL / PROVED PAPER
    + exposure of ALL simple prime periods            SOURCE SCHEMA OPEN
    + authenticated carry-powers at ALL depths        CONDITIONAL SOURCE SCHEMA
       -> supernatural exponents e_p=∞ all p           CLASSICAL / PROVED PAPER
       -> G = Zhat, full cyclic quotient system        CLASSICAL
       -> subgroup index/Haar/CRT prime clocks        PR #157 CLASSICAL
       -> exact jet comb / order / affine braid        PR #157 CONDITIONAL RECONSTRUCTION

B. ARCHIMEDEAN / RENEWAL ROUTE
  collision-free free FUCC source                     DECLARED SOURCE
    + independent additive-real positive half-line   REAL-PLACE IMPORT
    + full equation ν=δ_1+(τ_1)_*ν                    SOURCE SCHEMA OPEN
       -> ν=∑δ_n                                     PAPER PROVED
       -> integer evaluation and prime labels          PAPER PROVED
       -> global braid and unit cells                  PAPER PROVED

NOT IMPLIED BY:
 finite probes; coprime product alone; simple prime labels alone;
 unbounded some-prime depth; flat Euler jets; first unit cell;
 N(X)~X and π(X)~X/log X; zeta's critical-strip zero divisor.

RH AND ORIGINAL COMPLETED SIGNED WEIL POSITIVITY: OPEN.
```

## 9. Implementation, validation and finite evidence limits

New additive source modules: `observational_succ/source_minimality.py`, `observational_succ/carry_clock_lift.py`, `observational_succ/clock_compiler.py`, `observational_succ/renewal_rigidity.py`. Each uses exact integer/Fraction arithmetic and no numerical ζ, Gamma, nontrivial zero or complex analytic approximation. Test suite `tests/test_source_minimality.py` covers rooted map laws, CRT orbit sizes, 2-adic and squarefree countermodels, infinite same-finite-shadow procyclic sources, source-authenticated word costs, finite carry machines, density-one analytic normalization and genuine renewal/affine falsification. The independent deterministic probe and pinned JSON receipt use fixed systematic finite tests and explicitly **do not** promote them to universal analytic proofs.

To replay from a real SUCC checkout:

```
python -m unittest discover -s tests -p 'test_source_minimality.py' -v
python scripts/source_minimality_probe.py --verify
python -m unittest discover -s tests -p 'test_prime_jet_genesis.py' -v
python -m unittest discover -s tests -p 'test_profinite_index_genesis.py' -v
```

The previous PR #157 CI/claim ledger are inherited by the stacked PR. Main and historical source files remain untouched. Full repo CI must be checked by exact head; a draft PR is not merge authorization.

## 10. Specific next verdict-changing work

1. **Source constructor reality (sigma + phi separately):** Define an actual SUCC `E` protocol witnessing `C_p` primitive exposure with source ID, seed generator, finite state storage, root/phase, and legal causal dynamics. Require its `p` to come from verified *simple-quotient index*, not a string or a numerical guess.
2. **Carry lifting cost and preservation:** Construct a lawful modular high counter with a single carry at each low wrap, and independent repeat/mutation tests showing the new length is exactly `mp`, not a disguised constant shortcut. Track memory, event count, and available finite path.
3. **Completeness schema:** Prove a universally quantified program-constructor correctness theorem for every finite `p,k` and show it composes via CRT. Separate its algorithmic proof from an impossible claim of all infinite clocks already run.
4. **Independent real-place conservation:** Seek a causal source condition that actually proves the exact translation-renewal distribution, and refute first-moment/mean-density surrogates with the rational Beurling mutant.
5. **Cross-route source check:** If two routes claim the same atoms, compare their source passports and primitive generators without counting the same standard arithmetic theorem as independent evidence. Apply fake-6, q3=3/2, q3=9/2, paired rational mutant, squarefree, 2-adic-only and bad-carry controls.
6. **Weil firewall:** Authentic finite Euler/Gamma/poles and any claimed derived positive form require a further real source transport. Neither cofinality nor renewal demonstrates original Suzuki's signed low/high Schur sign, nor implies RH.

## Claim ledger

| ID | Scope | Status |
|---|---|---|
| SM-01 | Rooted quotient uniqueness; supernatural classification; `Zhat` iff every p-power cofinal | CLASSICAL / PAPER PROVED |
| SM-02 | Simple exposure + power-lift under closure equivalent to universality | PAPER PROVED, conditional finite-observer category |
| SM-03 | Finite transcript shadowed by proper finite **and infinite all-simple** procyclic source | PAPER PROVED / finite EXACT TESTED |
| SM-04 | Skew-product period `mp/gcd(c,p)` and root-preserving projection | PAPER PROVED / finite EXACT TESTED |
| SM-04B | Authenticated primitive seeds + allowed carry/CRT compile a verified full finite rooted period; exact carry budgets | PAPER PROVED / finite EXACT TESTED, conditional source constructors |
| SM-05 | Free finite-stage FUCC word is actual clock subgroup | REFUTED (C30 virtual 4) |
| SM-06 | Exact shift-renewal forces integer counting comb | PAPER PROVED, assumes global additive-real source law |
| SM-07 | Collision-free `9/2,35/11` Beurling source has unit first cell, density1, PNT, same critical-strip zero divisor but fails braid | PAPER PROVED from classical ζ continuation/PNT + EXACT FINITE TESTED |
| SM-08 | Ordinary density/PNT/first cell/zero positions suffice to identify original arithmetic source | REFUTED by SM-07 |
| SM-09 | Some finitely many observations certify all finite cyclic quotient types | REFUTED (SM-03, finite positive-observation scope) |
| SM-10 | Actual E physically builds all simple clocks plus source-authenticated unlimited carry lifts | UNVERIFIED; requested next source instrument |
| SM-11 | Finite clock/Beurling positivity implies signed Weil positivity or RH | REFUTED AS AN INFERENCE; RH OPEN |

