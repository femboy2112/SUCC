# SUCC Structural-Coupling Discovery — a finite source-relative experiment engine

**Checkpoint:** 2026-10-13 (New York).  **Research branch:** `research/structural-coupling-discovery-2026-10-13`, forked from `main@6e0d88f1b235b85188393bbcd64ac0436cb71a70`.  **Scope:** exact finite cyclic-by-cyclic group extensions and deterministic simulated interventions.  **Status:** classical group extension theorems with explicit derivations, executable exhaustive controls and conditional observer results. No independent scholarly priority, physical source authentication, unbounded syntax invention, global mathematical truth mechanism, RH theorem or Weil positivity is claimed.

## 0. Faithful object: "A is B and C, coupled like D"

The question is not whether two languages become equivalent once they are already known to describe the same structure. The problem is to **generate and distinguish candidate *couplings*** of structures that are individually familiar but whose joint object is not determined by their separate descriptions. SUCC's existing `relational_model_genetics`, `genetic_obstruction_holonomy`, `contextual_heuristics` and `causal_nerode_succ` already provide finite relational joins, shape priors, observational refinement and failure-driven language birth. This contribution adds a concrete, independently classifiable structural-coupling family with a constructive source-relative discrimination plan.

The source family is **stipulated and complete only within this grammar**: kernel `B=C_k`, quotient `C=C_q`, action `rho` of `C_q` on `C_k`, and a twisted 2-cocycle `f`. It is not a search through all finite groups or all mathematical structures. A shared finite label `(b,x)` is a **declared mathematical frame**, not an independently calibrated actuator or physical sensor. An observer's source knowledge consists of admitted extension hypotheses, permitted named actions, readouts, actual/synthetic receipts and a declared source/basis/epoch; the verifier can inspect full mathematical tables, but the operational policy can branch only on public reports.

The realization equation is

\[
 (b,x)\star_{g,f}(c,y)
   =\bigl(b+g^x c+f(x,y)\bmod k,\ x+y\bmod q\bigr),
 \qquad g^q=1\pmod k,
\]

where `g` is a unit modulo `k`.  `f(0,y)=f(x,0)=0` and

\[
 f(x,y)+f(x+y,z)\equiv g^x f(y,z)+f(x,y+z)\pmod k
 \tag{SCD-01}
\]

with cyclic indices. The equation is precisely associativity. Each accepted table yields a group: `(0,0)` is an identity; each element `(b,x)` has a left inverse from the `(-x)` fiber since `g^x` is a unit, and finite associative monoids with every element invertible are groups. The exact verifier also checks all identities/inverses/associativity independently, not merely the defining cocycle equation.

This is a **two-parameter coupling**: `g` describes the quotient's action on the kernel; `f` describes the twist of combining lifts. The two can change independently. This is classical extension theory, not novel group theory.

## 1. Theorem SCD-1 — normal form, gauge, and classification (CLASSICAL / DERIVED)

For fixed `k,q,g` with `g` invertible and `g^q=1 mod k`, normalized cocycles produce all group extensions in this fixed action/presentation class, up to changes of section of the quotient. For any normalized 1-cochain `t:C_q->C_k` with `t(0)=0`, define

\[
 f^t(x,y)=f(x,y)+t(x)+g^x t(y)-t(x+y).
\]

Then

\[
 \Phi_t:(C_k\times C_q,\star_f)\to(C_k\times C_q,\star_{f^t}),
 \qquad \Phi_t(b,x)=(b-t(x),x)
 \tag{SCD-02}
\]

is an exact group isomorphism fixing the kernel injection and quotient projection. *Proof:* substitute `Phi_t` into the products. The difference of the kernel coordinates cancels term by term by the displayed formula; `Phi_t` has inverse `(b,x)->(b+t(x),x)`. A finite independent test checks the equality for every element pair and every cochain in the 2×2, 3×2 and 3×3 families.

**Independent classification route (cyclic group cohomology):** let `u=(0,1)` be the chosen quotient lift and `a=(1,0)` generate the kernel. The lift obeys `u a u^-1=a^g`. Its `q`-th power lies in the kernel: `u^q=a^w`. Since `u` commutes with `u^q`, `(g-1)w=0 mod k`. Changing the lift to `a^s u` changes its winding by the norm

\[
 N_gs=(1+g+\cdots+g^{q-1})s\pmod k.
\]

Conversely the resulting presentation `a^k=1`, `u a u^-1=a^g`, `u^q=a^w` constructs the corresponding extension (the consistency condition is `(g-1)w=0 mod k`). Thus framed *extension-equivalence* classes for each action `g` correspond to

\[
 \boxed{H^2(C_q,C_k)_g\cong\ker(g-1)/\mathrm{im}(N_g).}
 \tag{SCD-03}
\]

This is a **classical** computation of cyclic group cohomology. Our exact `theoretical_extension_count` implements its cardinality independently of brute cocycle enumeration and checks the class identifier `cohomology_signature` derived from the `q`-fold lift. The equation does *not* classify all groups up to unrestricted isomorphism: the equivalence must respect the named kernel and quotient maps.

### Reproduced classes

| Kernel/quotient | Valid raw cocycles | Distinct framed extension classes | Abstract group classes | Identification |
|---|---:|---:|---:|---|
| `C2 by C2` | 2 | 2 | 2 | `C2×C2`, `C4` |
| `C3 by C2` | 4 | 2 | 2 | `C6`, `S3` (nontrivial action) |
| `C3 by C3` | 9 | 3 | 2 | `C3×C3`, two framed `C9` extensions |
| `C4 by C2` | 6 | 4 | 4 | `C4×C2`, `C8`, `D8`, `Q8` |

The cyclic-by-cyclic constructor is not hardcoded to any row above; the enumerator checks all normalized cocycles under all valid quotient actions in a finite bounded grammar, quotients them by cochain transformations, and computes complete finite isomorphism oracles for order ≤9. The action/winding invariants for `C4 by C2` are respectively `(g,w)=(1,0),(1,1),(3,0),(3,2)`. The last two are `D8` (order-two reflection lift) and `Q8` (reflection-like lift squares to the unique order-two kernel element). The `C8` lift has order eight; the `C4×C2` lift has order two. Independent element-order histograms distinguish all four, in addition to the exact full-group isomorphism check.

**Precision note:** a *gauge class* is a mathematical equivalence under a transported section; it is not automatically one empirical hypothesis if the physical actuator/readout labels are held fixed. This is audited separately in §3.

## 2. Theorem SCD-2 — public-history discrimination (CLASSICAL FINITE GAME)

A deterministic observer starts at the declared source preparation `(0,0)`. Each named action `a=(b,x)` performs right multiplication by that element under the unknown admitted candidate multiplication table. A legal action is available to all candidates by the declared common interface; **this is a hypothesis about the mathematical apparatus, not empirical authentication**. A report is the next state's quotient coordinate, kernel coordinate or complete labelled state, selected explicitly by the observer contract. Each actual/synthetic receipt contains source, basis, epoch, action and readout.

The state of the planning problem is the complete *set of live `(candidate,current_state)` pairs*. A policy may choose an action from the allowed menu using only the public history. It succeeds for target labels `T(i)` when **every** terminal live candidate has the same target. The finite-horizon recurrence is

\[
 W_0(B)\iff T\text{ is constant on }B;
\qquad
 W_{h+1}(B)\iff W_0(B)\lor
  \exists a\;\forall o\in\mathrm{Out}_a(B): W_h(B_{a,o}).
 \tag{SCD-04}
\]

Each `B_(a,o)` is computed from all candidate transitions with the indicated PUBLIC outcome. By induction on `h`, the recurrence is necessary and sufficient for existence of a deterministic successful adaptive policy of depth at most `h`. Iterative deepening therefore yields the shortest *worst-case action count* among available policies for the finite declared family. A failure at search depth `h` means `UNRESOLVED_WITHIN_HORIZON`, **not** unbounded impossibility. For the two-candidate examples, an independent enumerator checks all constant action words of each shorter length; for multiple candidates, all policy branches are independently replayed against their actual stipulated tables.

For the `C2 by C2` family, quotient lift `u=(0,1)` has `u²=(0,0)` or `(1,0)`; two `u` actions with a kernel readout identify the two groups. For `C3 by C2`, use quotient-generator then kernel-generator actions; the observed kernel coordinate becomes `g=1` or `g=2`, detecting action twisting. For `C3 by C3`, three quotient-generator actions expose the framed extension's winding class, while the two nonzero classes are nonetheless abstractly isomorphic. For `C4 by C2`, the algorithm finds a three-action conditional experiment distinguishing all four candidates; the exact receipt records each synthetic branch.

### Theorem SCD-3 — unbounded quotient-observation darkness (CLASSICAL / PROVED)

The quotient projection `p(b,x)=x` is a homomorphism **for every admitted `(g,f)`**. A fixed labelled action `(b,y)` always updates the quotient by `x -> x+y (mod q)`, independent of candidate. At the shared starting state, induction on a deterministic or adaptive public-history policy therefore gives the SAME quotient outcome history under every candidate. Thus no finite adaptive policy using only quotient reports and these named multiplication actions can distinguish candidates carrying different target labels. This is an all-horizon statement, not an extrapolation of the bounded planner's failure.

A newly licensed kernel-sensitive readout changes the admissible observational closure; merely adding a mathematical *name* for one does not. A source-dependent kernel reading could itself be unavailable or physically destructive; the present laboratory only represents the deterministic available case.

## 3. Theorem SCD-4 — model equivalence requires transported instruments

Take a `C3 by C2` trivial-action extension with zero cocycle. Change section by `t(0)=0,t(1)=1`. The target cocycle is gauge-equivalent and the group-isomorphism `Phi_t` is exact. Under the SAME untransported action label `u=(0,1)` and kernel sensor, the two-step readout is `0` under one multiplication table and `2` under the other. Therefore naive "gauge-equivalent mathematical models imply equal same-named empirical action predictions" is **false**.

Transport the entire operational diagram instead:

- source state `s` maps to `Phi_t(s)`;
- action `a` maps to `Phi_t(a)`;
- target report `r'` satisfies `r'(Phi_t(s))=r(s)`.

Then for any finite action word, the observable traces agree by inductive application of the group homomorphism equation; the code checks every fixed word through length four and the homomorphism on the full finite carrier. It does not authenticate the source-side physical map `Phi_t`. A calibrated physical lift could *break* the nominal gauge freedom, in which case the observer must admit the different framed action/interface hypotheses instead of quotienting them away. This is a concrete source-map (`sigma`) versus within-model theorem (`phi`) separation.

**Limitation of the current policy implementation:** candidates are canonically reduced to one representative per uncalibrated cochain gauge orbit, then compared under a declared common canonical action-label convention. That convention is **not derived from the source**. Before using this on a laboratory system, model the actor, sensor and basis jointly as candidate-specific calibrated interfaces, or restore all physically distinct candidate presentations. The unconditional structural-class and theoretical cohomology results do not depend on this modeling convention; operational policy conclusions DO.

## 4. Heuristic shape-weighting is not proof

Weights on the finite candidate set are exact rational **conditional model weights**, not truth probabilities for group axioms. A deterministic source receipt eliminates models predicting a different outcome and renormalizes surviving weights. Source/basis/epoch mismatch, unavailable actuation, zero evidence and floating-point priors are rejected. In the `C2 by C2` example a uniform `1/2,1/2` prior remains unchanged after the first source-compatible report and becomes `(0,1)` after the distinguishing second report **if** the synthetic `C4` model supplied that readout.

The engine also ranks admissible *next actions* by target-conditioned quadratic/Gini information gain:

\[
 \operatorname{Gain}(a)=G(T\mid h)-\sum_o P(o\mid h,a)G(T\mid h,a,o),
 \qquad G=1-\sum_zP(T=z)^2,
\]

with an optional declared exact action cost. On the four `C4 by C2` hypotheses after one quotient-step report, the next quotient step yields gain `1/2`; the next kernel-generator step yields gain `1/4`. If the quotient step is assigned cost four instead of one, the gain/cost ranking reverses. This is an **operational heuristic under supplied priors and costs**, not a theorem that the greedy action minimizes ultimate proof cost. The separate AND/OR planner computes its own certified bounded worst-case objective.

## 5. Connection to global SUCC and existing artifacts

- **GENIE / TLICA:** §3 distinguishes correct mathematical transport from independently established map between mathematical names and actual apparatus. High internal identification does not imply correct source map.
- **Operational Yoneda and NO-GHOST:** SCD-04 is a bounded exact public-policy game over source candidates. There is no synthetic hidden-source oracle in policy branching. Asymmetric source-changing/stochastic actions would require original/current pair, joint receipt/next-state law and public-policy realization constraints; the present single-state group action is a strict subcase.
- **Genetic model fusion:** SCD-01 generalizes "combine relations" to a generator of lawfully associative operation tables. Cochain/gauge orbits prevent counting formal recodings as structurally independent mathematical extensions when the entire frame transports correctly.
- **Matryoshka:** the system derives *mathematical observation programs*, not physically constructible sensors. A genuine miniature requires the parent carrier's compiler, safe actions, budgets and externally justified access interface.
- **Global/RH:** this is **not** a source-derived prime/Gamma/Weil identification. The transferable contribution is a method for generating coupling obstructions, distinguishing framed/global isomorphism types and designing source-relative discriminators. A future arithmetic coupling must be built from authenticated prime-power and Archimedean laws, with a correct analytic limit and sign theorem.

## 6. Exact falsification controls and reproduction

Source `AGENTS.md` contract applies. New files are additive, not modifications of frozen imported results:

- `observational_succ/structural_coupling.py` — normalized cocycle generator, theoretical norm quotient, exact group-isomorphism oracle, gauge transport, finite AND/OR policy search, causal receipts, exact Bayesian update and heuristic Gini ranking.
- `tests/test_structural_coupling.py` — independent raw multiplication associativity and inverses, exhaustive small cochains, theoretical H² classification counts, explicit full transport squares, brute short-word oracles, all-branch replay and malformed/mutated source/cost controls.
- `scripts/structural_coupling_probe.py` — deterministic source-stipulated JSON experiment and negative controls.
- `research/2026-10-13/STRUCTURAL_COUPLING_RECEIPT.json` — exact reproducible output, **not** laboratory data or proof of group-cohomology novelty.
- `docs/CLAIM_SUPPLEMENT_STRUCTURAL_COUPLING.md` — scoped mathematical claim ledger.

**Commands:**

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_structural_coupling.py' -v
PYTHONPATH=. python scripts/structural_coupling_probe.py > /tmp/coupling_recomputed.json
python -m json.tool research/2026-10-13/STRUCTURAL_COUPLING_RECEIPT.json >/dev/null
# Inspect / compare the recomputed JSON with the frozen source receipt.
```

Baseline `main@6e0d88f` reported 2,132 integrated tests in its prior review. This research's isolated tests are a **different test execution**; do not claim that 2,132+N tests, whole-union CI or Lean have passed without running them on the exact new branch head. No Lean proof file is added here; SCD-01 through SCD-04 are scoped paper derivations supported by exact finite tests. Classical cyclic extension cohomology is established prior art; exact same-model tests are not independent peer review.

## 7. Next verdict-changing probes (priority order)

1. **Restore source-map uncertainty:** attach per-hypothesis actuator and readout calibrations, and determine when raw cocycle gauge reduction is observationally sound. The hostile untransported `C3 by C2` example must survive as a negative control.
2. **Open-ended relational types:** synthesize noncyclic kernels, multiple quotient generators, genuine crossed modules/2-group actions or network pushouts. Test whether a proposed coupling law lies OUTSIDE the grammar, rather than silently assigning zero posterior to an omitted source.
3. **Stochastic/destructive instruments:** integrate with canonical `source_indexed_carrier` and NO-GHOST public information sets, original/current source, normalized joint `(receipt,next)` distributions, event budgets and no-reset rules. A constant current group state is not yet a physical measurement process.
4. **Analytical/global transport:** attempt a source-specific family of finite algebraic couplings with a mathematically certified continuum or profinite limit; distinguish an ideal completion from one original-source realizer. Hostile examples should include nonclosed source classes and missing compactness.
5. **Formalization and blind holdouts:** Lean-check the twisted-cocycle group constructor and `q`-quotient homomorphism. Verify the group extension classification by an independent source, and pre-register new `(k,q,g)` counts beyond those used to write the generator. No untested claim of academic priority.

**Verdict:** *PROVED LOCAL / CLASSICAL* for the finite algebra and policy theorems; *OBSERVED* for exact generated witnesses and synthetic tests; *UNVERIFIED* for empirical apparatus calibration, general mathematical-language genesis and source-correct global analytic transport. This system finds actual **mathematical couplings** and the probes separating their presentations under declared semantics; it does not yet discover arbitrary categories or physical instruments.
