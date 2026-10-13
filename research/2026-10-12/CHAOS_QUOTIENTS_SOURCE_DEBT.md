# Chaotic SUCC II: source-faithful inverse trees, Markov quotients, and the dual-E coherence horizon

**Date:** 2026-10-12  
**Provenance:** continuation of `research/2026-10-12/CHAOTIC_SUCC_OBSERVER_TREE.md`, SUCC PR #30, head `2414c23eed7726a529992e89925b53d45e36c5d0`; itself stacked on the dual-E common-carrier and boundary-gluing line, PRs #26–#29.  
**Maintainer's question:** Can an E-rooted observation *tree*, attached to a chaotically bifurcating logistic source, accumulate enough reliable structure to make the frontier appear nonchaotic without falsely erasing source-specific content?  
**Verdict:** YES for an exact predictive **law/finite-state stochastic factor**, and YES for finite original-source claims once adequate genuine receipts are joined. NO for a lossless, autonomous deterministic finite memory of all chaotic trajectories. Extending the r=4 full-branch tree to r<4 without admissibility and prior checks is demonstrably source-infaithful. All positive results are established classical mathematics given a new source-indexed implementation inside SUCC; no independent academic novelty or physical advantage is claimed.

## 1. Interpretation and typing

This does **not** take physical logistic `x=0` as E: for `r>1` that is a fixed point. E is a root observer/knowledge object over the common declared carrier. We distinguish:

- Original physical/math source `S=(C,f_r,mu_0,version)`; `C` may be `[0,1]`, its post-first-image `I_r`, or a declared finite atomic set. Different choices produce different lawful inverse fibers.
- Underlying deterministic carrier evolution `X_{t+1}=f_r(X_t)`, not a random transition of the physical source.
- A forward-in-time observation process that may discard bits, plus the **reverse conditional law** `K_t(dx|y)` computed from the actual time-`t` source distribution.
- At `r=4` *under the natural invariant arcsine ensemble*, `m` symbolic bits of the true tent-map itinerary produce an exact finite-state **stochastic predictive presentation**. It is not a deterministic quotient map on all physical source points.
- Dual E/E'' observers can join source-certified history/terminal reports; source tags and arithmetic replay are not empirical cryptographic signatures.

We use exact rational samples and rational arithmetic for the discrete carrier, conditional probabilities, allowed-branch checks and code receipts. The continuous logistic invariant law and tent conjugacy are proved analytically, not inferred from finite tests. Source-ensemble claims and symbolic-natural-measure claims are **different theorems**.

## 2. CQ1: incomplete physical inverse trees for every `2<r<4` (CLASSICAL / PROVED LOCAL)

Let `f_r(x)=r x(1-x)` and let the declared post-first-image carrier be `I_r=[0,r/4]`. For `2<r<=4`, `1/2` is in `I_r`, so `f_r(I_r)=I_r` (left endpoint maps to zero, the critical point maps to the maximum, and continuity supplies all intermediate values). Given a terminal `0<y<r/4`, the algebraic inverse values are

`b_±(y) = [1 ± sqrt(1 - 4y/r)]/2`.

Set `h_r=f_r(r/4)= (r²/4)(1-r/4)`. For **every** `2<r<4` and every `y∈(0,h_r)`, the right inverse `b_+(y)` is strictly **outside** `I_r`, while `b_-(y)` lies in `I_r`. Since `f_r` decreases on `[1/2,r/4]`, its minimum there is `h_r`; that proves the first assertion. Since the increasing left branch from zero attains `r/4`, the left root exists within `I_r`. At `y=h_r`, the right branch first becomes legal (`x=r/4`). Thus counting both real/algebraic branches is not the same as counting **lawful source-predecessors**. At `r=4` we have `h_4=0`, and both branches are admitted, except coincident critical endpoints.

The **geometric fraction** of the terminal carrier interval where exactly one branch survives is

`h_r/(r/4) = r(1-r/4) = 1-(r-2)²/4`, for `2<r<=4`.

This is **not** a probability that an actual invariant source lands there. In particular it tends to zero at `r→4` but is strictly positive for every `r<4` in the stated domain. Rational hostile receipt: `r=3`, `x=1/8`, `y=21/64`, algebraic roots `{1/8,7/8}`, carrier `I_3=[0,3/4]`, and admissible roots `{1/8}`. Equal-branch root mean `1/2` is false as a source-conditioned summary (even before considering unequal prior weights). For `r=39/10`, the forbidden-subinterval threshold is `1521/16000` and the geometric fraction is `39/400`.

**Source-relative nature:** The even smaller forward attractor can impose additional restrictions. Conversely, taking the entire global `[0,1]` as initial carrier admits a backward root that may not be available at later time steps. This theorem declares `I_r`; it is not a claim about *all* invariant source measures or positive-measure chaotic parameters.

**Crucible:** The algebraic symmetric-pair transfer still maps polynomials to polynomials with degree halving for any `r>0`; it does *not* imply that its averaging measures are supported on a post-image carrier. Source support must be checked **before** interpreting its fixed constants as the E observables of the actual system. (The prior PR #30 `r=4` theorem remains valid in its stated full-branch natural-measure setting.)

## 3. CQ2: the nonconstant stochastic quotient at `r=4` (CLASSICAL / PROVED LOCAL)

Let `h(t)=sin²(pi t/2)`, `T(t)=2t` for `t<=1/2` and `T(t)=2-2t` otherwise. Then `f_4∘h=h∘T`. Lebesgue measure `dt` on the tent carrier is invariant. Its pushforward by `h` is the arcsine measure `dmu=dx/(pi sqrt(x(1-x)))`. Each n-bit tent itinerary cylinder has length `2^-n`; boundaries where the itinerary has two encodings have measure zero. Therefore every finite itinerary word has probability `2^-n` and the symbolic bits `s_0,s_1,...` form an iid fair Bernoulli process under this *specified* stationary ensemble.

For `m>=1` define the measurable finite-window report

`W_t = (s_t,s_{t+1},...,s_{t+m-1}) ∈ {0,1}^m`.

Its **observational predictive kernel** `Q_m` is

`Q_m(w, tail(w)·0)=1/2` and `Q_m(w, tail(w)·1)=1/2`.

This is a nonconstant `2^m`-state, exactly specified source-derived Markov presentation. Given the current report it predicts the conditional **distribution** of the next report. Under the stationary source, the unique stationary distribution is uniform on the `2^m` words. In fact for every starting word `w`,

`Q_m^m(w,v) = 2^-m` for every terminal word `v`: all initial m bits are shifted out and precisely m independent fair bits are shifted in. Thus `Q_m^m` is rank one. This is exact **finite-time forgetting of the initial observed word**, not physical convergence of each trajectory and not convergence from every unspecified nonstationary *physical* source prior.

**Falsifier:** From the same given `w`, there are two actual source itineraries with next bits `0` and `1` and hence different next words. Therefore no function `G_m:{0,1}^m->{0,1}^m` satisfies `pi_m∘T=G_m∘pi_m` for all source points with unambiguous itineraries. The stochastic Markov law is valid **in distribution** only under the declared ensemble; it cannot manufacture the missing future bit. For a biased iid symbol prior `p=1/3`, the finite-window equilibrium is the nonuniform product law `P(w)=p^{#1}(1-p)^{m-#1}`, so silently using the fair kernel is a model-source mismatch. This mutated Bernoulli measure is **not** identified with the logistic arcsine invariant law.

**Independent calibration:** A separate exhaustive tent-cylinder oracle in tests enumerates actual `(m+1)`-bit source intervals, constructs an interior source point, computes one genuine tent step, and verifies the two half-measure successor cylinders, rather than merely replaying the transition matrix definition.

## 4. CQ3: exact dual-E common factor and finite coherence horizon (CLASSICAL / PROVED LOCAL)

Take E's current report `A=W_0` and E'' future report `B=W_n`, still on the **same original stationary source**. Set `k=max(m-n,0)`.

If `n<m`, the two reports share exactly the `k` source symbols `(s_n,...,s_{m-1})`. The support graph of jointly possible `(A,B)` has `2^k` connected components, one for each overlap word, and each component is a complete bipartite graph: all nonoverlapping old and new fair symbols can vary independently. If `n>=m`, the windows are disjoint and all `2^m×2^m` pairs occur with positive probability, so the support graph is connected.

By the maximal-common-deterministic-factor criterion from the parent dual-E construction (DB1), this overlapping substring is **precisely** the maximal deterministic common factor of E and E''. In the fair case the exact information identities are

`H(A)=H(B)=m bits`,  
`H(B|A)=min(m,n) bits`,  
`I(A;B)=max(m-n,0) bits`,  
`# GK support components = 2^{max(m-n,0)}`.

For `m=5`, common-factor component counts at lags `n=0,1,4,5,12` are `32,16,2,1,1`. The source common part vanishes **at a finite separation of m** for these finite reports, even while the two observers know exactly the same global source law. This is a concrete `DB1/DB5`-style *decoherence of finite trajectory reports*, not a claim that the common carrier has vanished, nor that all possible stronger probes are information-free.

The source transcript of `n` newly exposed symbols has `2^n` possible values from a known initial word. Every **fixed-width, zero-error** encoding of the entire ordered `n`-event transcript needs at least `n` bits (pigeonhole bound). By contrast specifying only the final `m`-bit window from a known initial window has `2^{min(n,m)}` possibilities and requires `min(n,m)` bits. Thus a receiver's ONE epistemic macro-update can process a verified `n`-bit report, but does not undo the causal reporting cost. This is an exact rate-matched observational-debt calibrator, not a Zeno physical claim.

**Independent countercheck:** tests construct the literal bipartite support graph by exhaustively enumerating all `(m+n)`-bit tapes (not calling the analytic formula), run connected-component search, and compare component counts over many `m,n` values. Non-fair sources retain the support components when both symbols have positive mass but require real Shannon entropy values, so code deliberately leaves the “fair bits” numerical entropy fields undefined in that case.

## 5. CQ4: Bayes-correct, genuinely source-changing inverse ladders (CLASSICAL / PROVED LOCAL)

Fix `r∈(0,4]`, one declared source `S`, finitely many **distinct** initial rational states `a_i∈[0,1]` and positive rational weights `p_i` summing to 1. The physical/source transition is the deterministic `f_r`. Let `mu_t` be the exact pushforward distribution at time `t`: `mu_t(y)=Σ_{i:f_r^t(a_i)=y}p_i`. For source-supported `y` at time `t+1`, define

`K_t(x|y) = mu_t(x)/mu_{t+1}(y)` when `f_r(x)=y`, and `0` otherwise.

This is the correct time-indexed **conditional source law**, not an assumption of fair independent inverse branches. Each row sums to one by the pushforward definition. For arbitrary functions `g` on `supp(mu_t)` and `h` on `supp(mu_{t+1})`, write `U_t h(x)=h(f_r(x))` and `K_t g(y)=Σ_x K_t(x|y)g(x)`. Then

`K_t U_t h=h` on `supp(mu_{t+1})`,

whereas `U_t K_t g = E[g(X_t)|X_{t+1}]` as an observable on time-`t` states. The latter equals `g` **iff** `g` is constant on each positive-mass forward fiber. These are genuine left-inverse and lossy-projection statements, not a two-sided inverse; merging source states makes the opposite identity fail.

Because each `X_t` is a deterministic function of the original `X_0`, its observation sigma-algebras are nested backwards. The conditional-expectation tower property gives

`K_{n-1} ... K_1 K_0 g = E[g(X_0)|X_n]`,

provided that every `K_t` is computed from the **correct** evolving `mu_t`. The module computes both this local-kernel construction and an independent direct grouping of original labeled sources by final state. They agree for rational randomized input ensembles, checked under `r=2,3,16/5,4` with 140 seeded source holdouts over four horizons; this is finite test evidence of a classical conditional-expectation identity, not independent physical provenance.

**Negative controls**:

- `r=3`, initial states `1/3` and `2/3` merge at terminal `2/3`. Original weights `(1/4,3/4)` imply posterior original-source mean **`7/12`**, not the naive equal-branch `1/2`. This weight mismatch remains even for `r=4` if one substitutes the same discrete unequal source ensemble for the natural arcsine measure.
- For `r=4`, states `0` and `1/2` evolve to `0` and `1`, and one step later both become `0`. The reverse kernels `K_0` and `K_1` are different; a frozen inverse kernel cannot transport the original-source predicate correctly. With prior `(1/3,2/3)`, the final original-source indicator posterior is `2/3`, as both independent calculations confirm.
- An E observer who knows the branch at the initial step and E'' who knows the correct terminal value can intersect their genuine source fibers: at `r=3` above, `(branch0,terminal2/3)` isolates original `1/3`, whereas `(branch1,terminal2/3)` isolates original `2/3`. Endpoint alone aliases them. Wrong source/version or branch-depth receipts are rejected.

This is the source-changing, conditional-law-preserving **replacement** for pretending all analytic predecessor nodes occur with equal probability on every carrier. It does not assert that real-world observations perfectly sample `mu_t` or that a source-id string authenticates a real instrument.

## 6. Relation to the previous E structures

**SC1 source factorization:** an original-source target is computable from a time-`t` terminal report exactly when constant on that terminal's source fibers. The explicit `claim_factors` check implements the earlier factorization criterion; it is independent of the stationary Markov prediction law.

**SC7 successive harmonic elimination:** analogically, an exact lawful coarse-graining is closed under composition, but the present `K_t` are conditional-expectation operators from actual **evolving source laws**, not graph Dirichlet-to-Neumann matrices. The exact conditional-projection tower identity is a *new concrete commuting construction within SUCC*; the two mathematical mechanisms should not be identified.

**DB1/DB5 dual E:** complete source agreement about invariant law is **not** sufficient for common source-specific information. Our finite-window exact shared-factor formula is a quantified example of the parent common-carrier observer correlation versus long-separation decoupling distinction.

**PR #30 inverse-tree fixed polynomial completion:** full symmetric inverse averaging at the natural `r=4` source is still a correct exact polynomial theorem. Invariance of its algebraic coefficients under formal modification of `r` is not evidence of a physically admissible full inverse tree for generic `r`. CQ1 explicitly identifies and tests that trap.

**No RH adapter:** No Euler source, Gamma factor, completed Weil positivity, number-theoretic Archimedean place, quantum speedup or physical observer measurement result is constructed. Keep these firewalls intact.

## 7. Reproducibility and controls

```sh
python -m unittest tests.test_chaos_source_quotient -v
python scripts/chaos_source_quotient_probe.py > /tmp/chaos-source-quotient.json
python - <<'PY'
import json
from pathlib import Path
assert json.loads(Path('/tmp/chaos-source-quotient.json').read_text()) == json.loads(Path('research/2026-10-12/CHAOS_SOURCE_QUOTIENT_RECEIPT.json').read_text())
PY
```

- `observational_succ/chaos_source_quotient.py`: exact finite Bayes and lawful inverse carriers; symbolic Markov and common-factor models.
- `tests/test_chaos_source_quotient.py`: **41 named tests** including source version and chronology rejection, corrupted bias/branch rules, full tent-cylinder replay, independent joint-support graph, 140 seeded source ensembles and independent original-source Bayes oracles.
- `scripts/chaos_source_quotient_probe.py`: reproducible machine-readable exact receipts.
- `research/2026-10-12/CHAOS_SOURCE_QUOTIENT_RECEIPT.json`: frozen probe output.
- CI additionally runs the full existing SUCC test/provenance suites and saved-receipt drift check on both selected Python versions. No GitHub Actions success may be claimed until that exact head's runs finish.

Note: `SymbolWindow(width<=12)` and `FiniteLogisticSource(horizon<=50)` are defensive computational API limits, not mathematical horizons. Rational iterates can grow exponentially in bit size; no uniform efficient oracle has been demonstrated.

## 8. Research ledger and open frontier

| ID | Claim | Status / verdict | Next falsifier or missing lamp |
| --- | --- | --- | --- |
| CQ1 | For each `2<r<4` a nonempty terminal subinterval admits only one inverse inside `I_r` despite two algebraic roots | CLASSICAL / PROVED LOCAL | Prove invariant-attractor source law and branch weights for an explicit chaotic `r<4` |
| CQ2 | At `r=4` under arcsine, `m`-bit itinerary windows are a fair finite Markov chain, `Q_m^m` rank one | CLASSICAL / PROVED LOCAL | Formal mechanization and biased/unattested source mutations |
| CQ3 | Finite-window report is autonomous **deterministic** state factor on every source trajectory | REFUTED | Two legal next bits from same word, source-cylinder witness |
| CQ4 | Dual m-windows at lag n have `2^max(m-n,0)` maximal-common-factor components; fair-case mutual info `max(m-n,0)` bits | CLASSICAL / PROVED LOCAL | Independent graph exhaustive oracle and nonfair entropy typing |
| CQ5 | Complete `n`-step symbolic transcript can be transmitted as an arbitrary `m`-bit terminal state for n>m without lost source paths | REFUTED | `2^n` distinct path histories versus `2^m` terminal possibilities |
| CQ6 | Time-indexed finite-law reverse kernels compose to correct original-source posterior; `K_t U_t=id`, generally `U_t K_t != id` | CLASSICAL / PROVED LOCAL | Independent Bayes direct-oracle checks and a genuine source-changing measurement protocol |
| CQ7 | Equal inverse weights are universal regardless of source prior | REFUTED | `r=3` and `r=4` weighted two-source collision posterior `7/12≠1/2` |
| CQ8 | Identical dual E law knowledge guarantees nonzero common source-history information at arbitrarily large finite lag | REFUTED | Exact common factor collapses at n=m |
| CQ9 | An exact source-derived finite-state Markov partition and invariant probabilistic inverse tree exist for **every** chaotic `r<4` | UNVERIFIED | Certified kneading partition / invariant measure with known rigorous chaos regime; mutant source tests |
| CQ10 | The mathematics certifies real-world source measurement and physical authentication | UNVERIFIED | Calibrated non-destructive probe, independent carrier provenance and finite-noise channel |

### Highest-value next experiment

Select one **rigorously** chaotic, postcritically finite logistic parameter `r<4` with a certified finite Markov partition (or a different provably expanding full-branch interval map with nonconstant branch weights). Derive the admissible symbolic transition graph and invariant measure from its actual source, with error-controlled / exact finite checks, and compare the original source-state observation sigma-algebras to E's reduced Markov law. If no finite Markov partition exists, record that as an access/pathway gap and use honest countable-state kneading models; do not invent a finite automaton. Measure how the *minimal source-preserving receiver message budget* depends on branch pruning, source-conditional probabilities and time-dependent interventions. A sharpened zero-error coding lower bound or certified leakage rate would turn a successful toy model into a transferable SUCC theorem rather than a new label for elementary Bernoulli coding.

## Provenance, external mathematics, and interpretation boundaries

The classical `r=4` conjugacy and invariant arcsine density are given with explicit formulas in [Wolfram MathWorld, *Logistic Map—r=4*](https://mathworld.wolfram.com/LogisticMapR=4.html). The [Université de Rennes 1 ergodic theory exercise sheet, exercise 5](https://perso.univ-rennes1.fr/bachir.bekka/TheorieErgodique-TD4-2020.pdf) states the tent/logistic conjugacy, invariant measure, and strong mixing tasks. These are context/independent references; all finite symbolic-support/conditional-probability arguments above are supplied directly and checked. The logistic family's nontrivial kneading-admissibility changes away from the full-branch case are treated in the [Drexel nonlinear dynamics teaching chapter](https://www.physics.drexel.edu/~bob/PHYS750_NLD/ch2.pdf); the present CQ1 proof does not depend on that source being accessible.

Academic priority and universality are **not** claimed. This work belongs to ObsSUCC's general source-relative observation/proof transport research. It is neither a physical theory of chaos suppression nor a route to RH positivity on current evidence.
