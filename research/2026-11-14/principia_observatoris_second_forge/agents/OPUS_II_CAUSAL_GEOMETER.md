# OPUS II — The Causal Geometer: quotient geometry for weighted causal structure

**Operation Principia Observatoris — Second Forge, Question C.** Delegated report, 2026-11-14.
**Status of this document:** research report for principal-investigator integration. It changes no
ledger entry and promotes nothing. Each theorem below carries its own label.
**Starting point (attributed, not rediscovered):** PAP-01 … PAP-05 in
[CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md](../../../../docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md),
`formal/PrincipiaAncestral.lean`, `observational_succ/ancestral_observer.py`,
`observational_succ/future_safe_quotient.py`. Founding input: the causal-relevance research note
(2026-11-13), used only for its cancellation countermodel and its "closeness = relevance" framing.
**Independence:** no material from any parallel campaign was consulted.
**Lab:** [`observational_succ/observatoris_quantale_quotient.py`](../../../../observational_succ/observatoris_quantale_quotient.py),
tests [`tests/test_observatoris_quantale_quotient.py`](../../../../tests/test_observatoris_quantale_quotient.py)
(45 tests, ≈45 s, stdlib and exact arithmetic only).

```sh
python -m unittest tests.test_observatoris_quantale_quotient -v
```

**Honesty statement.** Almost everything here is classical mathematics in different clothes:
- quantale-enriched relations and Lawvere metric spaces (Lawvere 1973; Hofmann–Seal–Tholen, *Monoidal Topology*, 2014; Stubbe's quantaloid-enriched categories);
- shortest-path potentials and LP duality;
- may/must abstraction (Larsen–Thomsen 1988; Dams–Gerth–Grumberg 1997);
- lumpability (Kemeny–Snell 1960);
- bisimulation (Park 1981; Milner) and open maps (Joyal–Nielsen–Winskel 1996);
- mates and Beck–Chevalley (Kelly–Street 1974);
- structural controllability and faithfulness (Lin 1974; Spirtes–Glymour–Scheines; Meek 1995).

No scholarly novelty is claimed. "New to the project" means only that SUCC did not previously state it. Finite tests are validation, not proof. The proofs below are paper proofs and are not Lean-checked.

---

## 0. Standing definitions and the axioms used

**Quantale.** V is a complete lattice (≤, ⋁, ⋀, ⊥, ⊤) with an associative multiplication ⊗ and a unit k. ⊗ need **not** be commutative. Each proof step names the axioms it uses:

| tag | axiom |
|---|---|
| (A) | associativity of ⊗ |
| (U) | k ⊗ a = a = a ⊗ k |
| (QL) | a ⊗ ⋁ᵢ bᵢ = ⋁ᵢ (a ⊗ bᵢ), including the empty join: a ⊗ ⊥ = ⊥ |
| (QR) | (⋁ᵢ aᵢ) ⊗ b = ⋁ᵢ (aᵢ ⊗ b), including ⊥ ⊗ b = ⊥ |
| (M) | monotonicity of ⊗ in each argument (a consequence of binary QL/QR) |

**Correction to the brief.** Every quantale is residuated, so "if V is residuated" is automatic. The left residual is a\c = ⋁{b : a⊗b ≤ c} and the right residual is c/b = ⋁{a : a⊗b ≤ c}. Then a⊗b ≤ c ⇔ b ≤ a\c ⇔ a ≤ c/b. This needs only completeness together with QL and QR; the lab checks it exhaustively on its finite instances.

**Relations.** A V-relation is R: X×X → V, with composition (R;S)(x,z) = ⋁_y R(x,y)⊗S(y,z). R⁰ = I, where I(x,x) = k and every other entry is ⊥. Rⁿ⁺¹ = Rⁿ;R and R* = ⋁ₙ Rⁿ.

By (A, QL, QR), Rⁿ(x,z) is the join over all length-n paths of the **path-ordered** product R(x₀,x₁)⊗R(x₁,x₂)⊗…. All products below are in path order.

**Observation.** q: X → Y. Y may be larger than q(X), and fibres may be empty. The fibre of a is q⁻¹(a), and Γ_q(x,a) is k if q(x) = a and ⊥ otherwise. Define:
- q_!φ(b) = ⋁_{q(u)=b} φ(u) (existential image);
- q^*ψ = ψ∘q;
- q_*φ(b) = ⋀_{q(u)=b} φ(u).

**Three quotients.**
- Q∃(a,b) = ⋁_{q(u)=a, q(v)=b} R(u,v) (may), also written Q.
- Q∀(a,b) = ⋀_{q(u)=a} ⋁_{q(v)=b} R(u,v) (forward must, ∀∃).
- Q←(a,b) = ⋀_{q(v)=b} ⋁_{q(u)=a} R(u,v) (backward must).

For any relation S, Q∀(S) and Q∃(S) denote the same constructions applied to S.

**Closed predicates.** φ: X → V is **R-closed** when φ(u)⊗R(u,v) ≤ φ(v), and Cl(R) is the set of such φ. Define:
- Cl_R φ(v) = ⋁_u φ(u)⊗R*(u,v);
- Int_R φ(u) = ⋀_v φ(v)/R*(u,v).

**Profiles.** ρ_x = R*(x,·) and ρ̂_x = q_!ρ_x, so ρ̂_x(b) = ⋁_{q(z)=b} R*(x,z) is the true source value from x to report b. Define:
- S(a,b) = ⋁_{q(x)=a} ρ̂_x(b) = (Γ_q^op;R*;Γ_q)(a,b) = Q∃(R*)(a,b) (may-profile);
- M(a,b) = ⋀_{q(x)=a} ρ̂_x(b) = Q∀(R*)(a,b) (must-profile).

**Exactness.** q is **exact at x** when Q*(q(x),b) = ρ̂_x(b) for all b, and **all-start exact** when it is exact at every x. For Boolean V this is PAP-03's condition (3).

**Lemma 0 (closure algebra).** PROVED; CLASSICAL.
1. R*;R ≤ R*, R*;R* = R*, and I ≤ R*. These use QR and QL.
2. R* is the least S with I ≤ S and S;R ≤ S. This is Kleene's fixed point, which the lab iterates.
3. If φ ∈ Cl(R), then φ(x)⊗R*(x,z) ≤ φ(z).

*Proof of (3).* Induction on n. By QL and A,

φ(x)⊗Rⁿ⁺¹(x,z) = ⋁_y (φ(x)⊗Rⁿ(x,y))⊗R(y,z) ≤ ⋁_y φ(y)⊗R(y,z) ≤ φ(z),

using the induction hypothesis with M, then closedness. Take ⋁ₙ with QL. ∎

**Lemma L (q^* preserves and reflects closedness).** For every ψ: Y → V, ψ ∈ Cl(Q∃) ⇔ q^*ψ ∈ Cl(R). PROVED.

*Proof.*
- ⇒: ψ(q(s))⊗R(s,t) ≤ ψ(q(s))⊗Q(q(s),q(t)) ≤ ψ(q(t)). This uses M.
- ⇐, nonempty fibre a: ψ(a)⊗Q(a,b) = ⋁_{q(s)=a, q(t)=b} ψ(q(s))⊗R(s,t) ≤ ψ(b). This uses QL.
- ⇐, empty fibre a: Q(a,·) = ⊥ and ψ(a)⊗⊥ = ⊥ by QL. ∎

---

## CG-1. Weighted hereditary characterisation (weighted PAP-01)

**Domain.** Any unital quantale V and any set X; no finiteness assumed.

**Statement.** For all x, z:
- (a) R*(x,z) = ⋀{φ(z) : φ ∈ Cl(R), k ≤ φ(x)}, and the meet is attained at φ = ρ_x.
- (a′) R*(x,z) = ⋀_{φ∈Cl(R)} φ(x)\φ(z), using the **left** residual.
- (a″) The *opposite-side* condition R(u,v)⊗φ(u) ≤ φ(v) characterises instead the closure in V^rev (a⊗′b = b⊗a), i.e. the **reversed** path products. The backward form is R*(x,z) = ⋀{ψ(x) : R(u,v)⊗ψ(v) ≤ ψ(u) ∀u,v, k ≤ ψ(z)}.

**Proof.**
- (a), "≤": if k ≤ φ(x), then R*(x,z) = k⊗R*(x,z) ≤ φ(x)⊗R*(x,z) ≤ φ(z), by U, M and Lemma 0.3.
- (a), "≥": ρ_x is closed, since R*(x,u)⊗R(u,v) ≤ R*(x,v) by Lemma 0.1 (uses QR), and k ≤ R*(x,x).
- (a′): Lemma 0.3 gives R*(x,z) ≤ φ(x)\φ(z). For φ = ρ_x, since \ is antitone in its first argument and k\c = c, we get R*(x,x)\R*(x,z) ≤ k\R*(x,z) = R*(x,z).
- (a″): apply (a) to the quantale V^rev, which is again a quantale. The backward form is (a) for R^op over V^rev. ∎

The backward form is proved by symmetry only; it is not separately tested.

**Instances.**
- **Boolean.** Exactly PAP-01.
- **Lawvere tropical** ([0,∞], order reversed, ⊗ = +, k = 0). k ≤ φ(x) means φ(x) = 0, closed means φ(v) ≤ φ(u) + w(u,v), and ⋀_V is numeric sup. So d(x,z) = max{π(z) : π(x) = 0, π feasible}: shortest-path LP duality with feasible potentials (CLASSICAL; e.g. Schrijver, *Combinatorial Optimization*, shortest-path chapters).
- **Viterbi** ([0,1], max, ×, k = 1). Best-path relevance is the least value of φ(z) over multiplicatively sub-invariant φ with φ(x) = 1.
- **Bottleneck** (max, min on a chain). Widest-path value.
- **P(M).** Path languages (free monoid), path lengths mod k (ℤ/k), and a noncommutative left-zero monoid.

**Status.**
- CLASSICAL in substance: R* is the meet of representables, an enriched-Yoneda-type fact for V-categories. PROVED here in this generality.
- OBSERVED IN EXACT FINITE MODELS:
  - all 9,082 relations in the exhaustive families (Boolean n ≤ 3; tropical-budget-2, max-min chain-3, P(ℤ/3) and P(left-zero) with n ≤ 2): Kleene closure = distributivity-free path oracle = hereditary meet = residuated meet, for every (x,z);
  - 60 + 60 random exact-rational tropical and Viterbi models.

**Countermodels (receipts, all tested).**
1. **Wrong side (noncommutative).** P(left-zero {e,a,b}) with ab = a and ba = b, path 0 –{a}→ 1 –{b}→ 2. R*(0,2) = {a}. The opposite-side meet gives {b} (the reversed trace), and the right residual gives ∅.
2. **Distributivity removed.** M3 with ⊗ = ∧ is associative, unital and monotone, but not a quantale. Take edges 0→1 (1), 0→2 (a), 1→2 (b), 2→3 (c). The path sum R*(0,3) = (a∧c) ∨ (b∧c) = 0. The hereditary meet is (a∨b)∧c = c. Kleene iteration also gives c, and ρ₀ is not closed. So CG-1 requires QL/QR, not merely monotonicity.

**Buys.** A potential/invariant (V-valued hereditary predicate) certifies a quantitative bound on every source path.
**Does NOT establish.** Attainment of R* by a single path in infinite non-integral V, or any probabilistic or physical meaning.
**Interoperability.** Input: a V-relation and a selected start. Output: R*(x,·) as the least closed predicate above the unit at x.
**Next falsification.** Lean-formalise (a)/(a′) for a `CompleteLattice` with a monoid and two-sided ⊔-distributivity; attack infinite X with non-integral V (e.g. P(ℤ)).

## CG-2. Projection soundness (weighted PAP-02)

**Statement.** For all x, z: R*(x,z) ≤ Q*(q(x),q(z)). Hence ρ̂_x(b) ≤ Q*(q(x),b) for all b.

**Proof.** Each edge satisfies R(u,v) ≤ Q(q(u),q(v)), and k ≤ Q⁰(q(x),q(x)). Path products are then bounded using M. ∎

Only M is used, so CG-2 survives in M3 if R* is read as the path sum.

**Status.** PROVED; CLASSICAL (a V-functor). Tested on all models listed in CG-3.

**Reading.**
- Tropical: d_Q(q(x),b) ≤ d_src(x, fibre b) numerically. The quotient never over-estimates source distance; it can only invent shortcuts and endpoints. The brief's phrasing is **confirmed**.
- Viterbi: quotient relevance is ≥ source relevance.

**Does NOT establish** any converse; see CG-3.
**Interoperability.** Input: (R, q). Output: one-sided bound source ≤ quotient.

## CG-3. All-start exactness: seven equivalent conditions (weighted PAP-03)

**Domain.** Any unital quantale (noncommutative allowed), any X and Y (non-surjective q allowed).

**Statement.** The following are equivalent.
1. **All-start exactness.** For all x, b: Q*(q(x),b) = ρ̂_x(b).
2. **Fibre-constant profiles.** q(x) = q(x′) ⇒ ρ̂_x = ρ̂_{x′}. Equivalently, R* is lumpable: R*;Γ_q = Γ_q;N for some N, and then N = Q* on image rows.
3. **Images preserve closedness.** q_! maps Cl(R) into Cl(Q).
4. **Saturation preserves closedness.** q^*q_! maps Cl(R) into Cl(R).
5. **One-step may ≤ closure must.** Q∃(R)(a,b) ≤ Q∀(R*)(a,b) for every a ∈ q(X) and every b. This is new to the project: every one-step quotient edge is realised by the source closure from **every** representative.
6. **May = must for the closure.** Q∃(R*) = Q∀(R*) on image rows, i.e. S = M.
7. **Left Beck–Chevalley.** The left Beck–Chevalley mate of CG-8 is invertible.

**Proof.**
- (1)⇒(2): immediate.
- (2)⇒(4): let φ ∈ Cl(R) and s, t ∈ X. By QR, (q^*q_!φ)(s)⊗R(s,t) = ⋁_{q(u)=q(s)} φ(u)⊗R(s,t). For each such u:
  - R(s,t) ≤ ρ̂_s(q(t)) = ρ̂_u(q(t)), by Lemma 0.1 and then (2);
  - so φ(u)⊗R(s,t) ≤ ⋁_{q(v)=q(t)} φ(u)⊗R*(u,v), by M and QL;
  - and this is ≤ ⋁_{q(v)=q(t)} φ(v) = q^*q_!φ(t), by Lemma 0.3.
- (4)⇔(3): Lemma L.
- (3)⇒(1): ρ_x ∈ Cl(R) (CG-1), so ρ̂_x ∈ Cl(Q) and k ≤ ρ̂_x(q(x)). CG-1(a) applied to Q gives Q*(q(x),·) ≤ ρ̂_x, and CG-2 gives ≥.
- (2)⇔(6): a nonempty family has ⋀ = ⋁ iff all its members are equal. Off-image rows are excluded.
- (6)⇒(5): Q(a,b) = ⋁_{u∈a, v∈b} R(u,v) ≤ S(a,b) = M(a,b).
- (5)⇒(1): show Qⁿ(q(x),b) ≤ ρ̂_x(b) for all x by induction on n. The case n = 0 holds by reflexivity. For the step,

  Qⁿ⁺¹(q(x),c) = ⋁_b Qⁿ(q(x),b)⊗Q(b,c)
  ≤ ⋁_{z} R*(x,z)⊗Q(q(z),c) (induction hypothesis and QR)
  ≤ ⋁_{z} R*(x,z)⊗⋁_{q(w)=c} R*(z,w) (by (5), since q(z) ∈ q(X))
  ≤ ρ̂_x(c) (QL and Lemma 0.1).

  Take ⋁ₙ; CG-2 gives the reverse inequality. Off-image b contribute ⊥ by QL.
- (7): see CG-8. ∎

**Status.** PROVED. Conditions (1)–(4) are the direct weighted lift of PAP-03 (CLASSICAL ELEMENTARY in substance), and Boolean V recovers PAP-03 verbatim. Conditions (5) and (6) are new to the project.

OBSERVED IN EXACT FINITE MODELS — all seven conditions agree on:
- **all 2,594 Boolean relation/partition models with ≤ 3 states**, which reproduces the existing count, cross-checked state by state against `audit_ancestral_observer` (endpoint exactness and ghost report sets);
- all 18,113 two-state models over the budget-2 tropical, saturating-2 tropical, chain-3, P(ℤ/2), P(ℤ/3) and noncommutative P(left-zero) quantales;
- 1,600 random three-state models over four quantales.

**Noncommutativity.** Nothing breaks, provided the path-order and left-residual conventions of CG-1 are used.
**Mutation.** In M3 the model R = ((c,1,c),(0,1,0),(a,c,0)) with q = (0,1,0) satisfies (1) and (2) but violates (3) and (4). The equivalence needs distributivity.
**Interpretation.** Condition (5) is a "weak zig-zag" or open-map-up-to-closure property: a visible quotient step is matched by a source *closure* move from every representative, in the way weak bisimulation matches visible steps with τ*-paths. This is an analogy (Joyal–Nielsen–Winskel), not a claimed theorem about open maps.
**Buys.** A single finite check, (5) or (6), decides all-start exactness for weighted relations.
**Does NOT establish.** Step, length or trace preservation (CG-5, CG-6), probabilities, or anything about a selected start beyond CG-4.
**Interoperability.** Input: finite (V, R, q). Output: a Boolean exactness verdict plus, on failure, the representative pair whose profiles differ.
**Next falsification.** Exhaust three-state models over a five-element noncommutative quantale (needs a faster engine), and infinite X.

## CG-4. Selected-start criterion (weighted PAP-03(5))

**Statement.** For a fixed x, exact at x ⇔ ρ̂_x ∈ Cl(Q) ⇔ q^*ρ̂_x ∈ Cl(R). The last condition says that the V-saturation of x's reachable profile is closed, generalising Closed_R(Sat_q(Reach x)).

**Proof.** ⇒: Q*(q(x),·) is closed. ⇐: the (3)⇒(1) argument applied to the single start x. The second equivalence is Lemma L. ∎

**Status.** PROVED. OBSERVED on all models in CG-3, for every start.
**Does NOT establish.** Exactness at other starts; see the PAP-04 three-state ghost, which the lab reproduces.

## CG-5. Change of base: strict, oplax, lax

Let h: V → W preserve **arbitrary joins** (in the finite case: binary joins and ⊥).
- h is **strict** if h(a⊗b) = h(a)⊗h(b) and h(k) = k.
- h is **oplax** if h(a⊗b) ≤ h(a)⊗h(b) and h(k) ≤ k.
- h is **lax** if h(a)⊗h(b) ≤ h(a⊗b) and k ≤ h(k).

**Statement.**
1. **Strict.** h∘R* = (h∘R)* and h∘Q_R = Q_{h∘R}. Hence exactness at x over V implies exactness at x over W, every W-ghost at x is a V-ghost at x, and all-start exactness transports.
2. **Oplax transports all-start exactness.**
3. **Oplax transports selected-start exactness hereditarily.** If q is V-exact at every state support-reachable from x, then hR is W-exact at x.
4. **Oplax does NOT transport bare selected-start exactness.** REFUTED by receipt.
5. **Lax does NOT transport all-start exactness,** even with strict unit and strict joins. REFUTED by receipt.
6. **Converses fail.** There is a strict chain of strict base changes, language → cost → Boolean, with strictness witnesses at each link.
7. **Not transported.** Q∀ does not transport, because joins-only maps do not preserve meets.

**Proofs.**
- (1): h preserves ⋁ and finite products and unit, hence path sums. Apply h to the equation in CG-3(1).
- (2): via CG-3(5). From V-exactness, Q(a,c) ≤ ⋁_{q(w)=c} R*(z,w) for every z ∈ a. Applying monotone h:
  h Q(a,c) ≤ ⋁_w h(R*(z,w)) ≤ ⋁_w (hR)*(z,w).
  The second step holds because h(⋁_paths ∏ rᵢ) = ⋁ h(∏ rᵢ) ≤ ⋁ ∏ h(rᵢ) (oplax, iterated; h(k) ≤ k for the empty path). Since h Q = Q_{hR}, condition (5) holds over W.
- (3): run the (5)⇒(1) induction over W, restricted to the z with (hR)*(x,z) ≠ ⊥. Such z are support-reachable because h(⊥) = ⊥, and exactness at z gives the needed one-step bound. ∎

**Receipts (tested).**
- (4) Budget tropical {0..3,∞}, h(a) = ⌊a/2⌋, which is oplax and not strict. States: A = {0}, B = {1,2}, C = {3}; edges 0→1 (1), 0→3 (2), 2→3 (1). Exact at 0 over V, with profile (0,1,2) = Q*. Over W the profile from 0 is (0,0,1) but Q* = (0,0,0): a ghost shortcut, because state 1 is not exact.
- (5a) h: Bool → P(ℤ/2), h(1) = {0,1}, which is lax with lax unit. X = {0,1}, a self-loop at 1, q constant. Boolean is exact, but over W Q*(A,A) = {0,1} while ρ̂₀ = {0}.
- (5b) h(A) = [0 ∈ A]: P(ℤ/2) → Bool, which is lax with **strict unit and strict joins**. Edges 1→2 ({1}), 2→0 ({0}), 2→2 ({1}); q = (0,1,1). Exact over P(ℤ/2). Over Bool the edge 2→0 survives but 1→2 dies, so start 1 has a ghost.
- (6) The PAP-04 chain under strict homs P(Σ^{≤2}+#) → saturating tropical(3) → Bool (all three strict, checked exhaustively on the finite carriers):
  - Boolean-exact but not cost-exact: the chain 0→1→2 with q = (0,0,1) and unit costs has source cost 2 and quotient cost 1.
  - Cost-exact but not language-exact: edges 0 –x→ 2 and 1 –y→ 2 with q = (0,0,1). The quotient language is {x,y}; from 0 it is {x}.
- **Budget-truncated tropical → Bool** (a ↦ a < ∞) is only **oplax** (2⊗1 = ∞), not strict. By (2) it still transports all-start exactness; the lab exhausts this.

**Corrections to the brief.**
- "Whether LAX homomorphisms suffice in one direction": they do not (receipts 5a, 5b). The correct one-directional notion is **OPLAX**, and it suffices only for all-start (or hereditary selected) exactness.
- "The PAP-04 hierarchy is exactly a chain of base changes": the endpoint < cost < language levels are realised as strict base changes with explicit strictness witnesses. Identifying SUCC's `future_safe_quotient` trace contract with language exactness is **NOT ESTABLISHED**: that contract also tracks per-edge costs, source tags, task outputs and rejection behaviour. CG-6(ii) supplies the precise link for letter-valued relations.

**Status.** (1)–(3) PROVED. (4) and (5) REFUTED by tested receipts. OBSERVED: three oplax maps with 625×2 two-state models plus 400×5 random three-state models each, with zero transport failures.
**Interoperability.** Input: an exactness certificate over V and a map h of known type. Output: an exactness verdict over W, without recomputation when h is strict or oplax.

## CG-6. Instances, minimality, and the graded theorem

1. **Minimal ghost size.** Integral V means k = ⊤ (Boolean, tropical, Viterbi, bottleneck).
   - For **integral V, three states are minimal** for a ghost. With two states, q is injective (trivially exact) or constant. If constant, Q*(A,A) ≤ ⊤ = k ≤ R*(x,x). PROVED; OBSERVED on all two-state integral models.
   - For **non-integral V, two states suffice.** P(ℤ/2), edge 0 –{1}→ 1, q constant: Q*(A,A) = {0,1}, while from 1 the profile is {0}. The quotient invents odd-length loops. One state never suffices, since q is then injective.
   - This **corrects** an over-reading of PAP-04's minimality, which is a Boolean statement.
2. **Graded theorem.** PROVED; new to the project; classical in content.
   - **Hypotheses.** V = P(M), deg: M → (ℕ,+) a monoid homomorphism, and R valued in P(deg⁻¹(1)), e.g. letter-labelled edges.
   - **Statement.** All-start exactness ⇔ one-step lumpability (q_!R(x,·) is constant on fibres).
   - **For letter-valued R.** This says ker q is a **bisimulation equivalence** of the labelled transition system (CLASSICAL notion).
   - **Proof.** Rⁿ ⊆ P(deg⁻¹(n)), so the degree-1 component of Q* is Q and that of ρ̂_x is q_!R(x,·). Exactness forces these to be equal. Conversely, lumpability implies CG-3(5).
   - The truncated monoid Σ^{≤L} + # used in the lab is fine because # never has degree 1.
   - **Consequence.** The trace (language) level of the hierarchy is as strong as bisimulation for all starts, while each single start only demands trace-type agreement. The time-graded quantale P(ℕ) behaves the same way.
   - OBSERVED: 150 random letter-valued relations × 3 report maps, exact ⇔ lumpable.
3. **(max, ×) on [0,∞].** This is a non-integral quantale; cycles of weight > 1 force R* = ∞. The lab implements [0,1] only.

## CG-7. May/must sandwich and the refined chain

**Statement.** PROVED. For every x with a = q(x) and every b:

Q∀*(a,b) ≤ M(a,b) ≤ ρ̂_x(b) ≤ S(a,b) ≤ Q∃*(a,b).

Every link can be strict, including **both outer links at one (x,b)**.

**Hypotheses actually used.** QL, QR and M only.
- **No distributivity of ⊗ over meets** is needed.
- **Empty fibres and non-surjective q are harmless.** Q∀ has a ⊤-row at an empty fibre, so Q∀ ≤ Q∃ holds only on image rows. Both Q∀(a,b) and Q∃(a,b) are ⊥ when a ∈ q(X) and b has an empty fibre, so paths starting on the image never leave it.

**Proof.**
- **Key lemma: q_! maps Cl(R) into Cl(Q∀).** For a nonempty fibre:
  q_!φ(a)⊗Q∀(a,b) = ⋁_{u∈a} φ(u)⊗Q∀(a,b) (QR)
  ≤ ⋁_u φ(u)⊗⋁_{v∈b} R(u,v) (Q∀(a,b) is below each u's inner join; M)
  ≤ ⋁_v φ(v) (QL and closedness).
  For an empty fibre, ⊥⊗· = ⊥.
- **Lower bound.** Apply CG-1(a) to the relation Q∀ with the closed ψ = ρ̂_x, which satisfies k ≤ ψ(a).
- **Refinement Q∀* ≤ M.** M is reflexive and transitive on the image. For transitivity, pick x ∈ a: M(a,b)⊗M(b,c) ≤ ⋁_{z∈b} R*(x,z)⊗ρ̂_z(c) ≤ ρ̂_x(c). Also Q∀ ≤ M on image rows, so Q∀ⁿ ≤ M by induction along image-only paths.
- **Remaining links.** M ≤ ρ̂_x ≤ S is meet ≤ member ≤ join; S ≤ Q∃* is CG-2. ∎

**Global hierarchy.** PROVED, with each implication strict and receipts tested:

lumpable (Q∀(R) = Q∃(R) on image) ⇒ Q∀* = Q∃* on image ⇒ **exact** (Q∃(R) ≤ Q∀(R*)) ⇒ unpointed (Q∃* = Q∃(R*) on image).

| implication fails to reverse | receipt |
|---|---|
| Q∀* = Q∃* does not imply lumpable | 0→1, q constant |
| exact does not imply Q∀* = Q∃* | the PAP-04 chain 0→1→2, q = (0,0,1) |
| unpointed does not imply exact | the PAP-04 ghost: 1→2, q = (0,0,1) |
| (unpointed itself fails) | 0→1, 2→3, q = (0,1,1,2) |

In the Boolean census of 2,594 models all of these strict separations occur:
- 462 models: may* = must*, not lumpable;
- 384 models: exact, not may* = must*;
- 384 models: unpointed, not exact;
- 240 models each: forward-exact but not backward-exact, and backward-exact but not forward-exact.

**Answers to the brief.**
- *Does Q∀* = Q∃* characterise exactness?* **No — REFUTED.** It is strictly stronger; the receipt is the PAP-04 chain.
- *The exact characterisation:* CG-3(5)/(6), "the one-step may-quotient is bounded by the must-quotient of the closure", equivalently "may = must for R*".
- *Is the source value a fixed point between the two?* **Not in terms of the quotients — REFUTED.** Two models share q, Q∃, Q∀, Q∃* and Q∀* exactly but have different source profiles from start 0:
  - edges {1→2, 1→0} with q = (0,0,1): from 0 the profile is {A};
  - edges {0→1, 1→2} with the same q: from 0 the profile is {A,B}.

  The best intrinsic description is M = Q∀(R*) = Γ_q \ (R*;Γ_q), the relational residual. It is the **largest** relation N on Y with N(q(x),b) ≤ ρ̂_x(b) for every x, i.e. the optimal representative-uniform lower bound. Exactness is precisely M = Q∃* on image rows. The exact values themselves are recovered by the canonical refinement in CG-10.

**Tropical reading.** d_∀(a,b) ≥ d_src(x, fibre b) ≥ d_∃(a,b) numerically. The may-quotient invents shortcuts; the must-quotient never does. Receipt for both links strict: fibre A = {0,1,2} with 0→3 (2), 1→3 (1), and 2 idle gives (∞, 2, 1).

**Interoperability.** Input: (R, q, x). Output: a certified interval [Q∀*, Q∃*] containing the true value, computable from the quotients alone.

## CG-8. Adjunctions and the two Beck–Chevalley conditions

**Statement.** PROVED.
1. Cl(R) is a **complete sublattice** of V^X, closed under **all** joins (QR) and **all** meets (M). Cl_R ⊣ incl ⊣ Int_R, with the formulas of §0.
   - Int: if ψ is closed and ψ ≤ φ, then ψ(u)⊗R*(u,v) ≤ φ(v), hence ψ ≤ Int φ. Int φ is closed because R(u,w)⊗R*(w,v) ≤ R*(u,v).
2. q_! ⊣ q^* ⊣ q_* on V^X and V^Y (CLASSICAL hyperdoctrine structure).
3. q^* restricts to Cl(Q) → Cl(R) (Lemma L), with **left adjoint L = Cl_Q∘q_!** and **right adjoint Int_Q∘q_***. For ψ ∈ Cl(Q):
   - Cl_Q q_!φ ≤ ψ ⇔ q_!φ ≤ ψ ⇔ φ ≤ q^*ψ;
   - q^*ψ ≤ φ ⇔ ψ ≤ q_*φ ⇔ ψ ≤ Int_Q q_*φ.
4. **Counit.** L q^*ψ = ψ·1_{q(X)}: it equals ψ on the image and ⊥ off it. So the counit is an isomorphism exactly at ψ supported on q(X), and everywhere iff q is surjective.
5. **Unit.** φ ≤ q^*q_!φ ≤ q^*Lφ. The first inequality is **fibre blur**: equality iff φ is constant on fibres; it is not a ghost. The second is the **ghost**: equality iff q_!φ ∈ Cl(Q). Since Lρ_x = Q*(q(x),·) (shown in CG-9), the unit at ρ_x lists exactly the invented futures from x.
6. **Left Beck–Chevalley.** The square of right adjoints incl∘q^*| = q^*∘incl commutes, so the left adjoints satisfy L∘Cl_R = Cl_Q∘q_! **always**. The mate q_!∘incl ⇒ incl∘L has component q_!φ ≤ Cl_Q q_!φ. It is invertible ⇔ CG-3(3) ⇔ **forward all-start exactness**. Mate calculus is CLASSICAL (Kelly–Street); the instance is new to the project.
7. **Right Beck–Chevalley.** The mate incl∘Int_Q q_* ⇒ q_*∘incl is invertible
   ⇔ q_* maps Cl(R) into Cl(Q)
   ⇔ Q∃(R) ≤ Q←(R*)
   ⇔ **backward exactness**: for all a and z, Q*(a,q(z)) = ⋁_{q(x)=a} R*(x,z).
   This is CG-3(1) for (R^op, V^rev): the **time reverse** of forward exactness.
   - *Proof.* Testing on φ = Cl_R(k·1_a) gives necessity. Sufficiency: q_*φ(a)⊗Q(a,b) ≤ q_*φ(a)⊗⋁_{u∈a} R*(u,v) ≤ φ(v) for each v ∈ b. The relation B = Q←(R*) is reflexive and transitive, so Q* ≤ B, and B ≤ ⋁_x R*(x,z) yields backward exactness. ∎
8. **Pairings, which correct the brief.** q_! always maps Cl(R) → Cl(Q∀) (CG-7). q_* always maps Cl(R) → Cl(Q←), **not** Cl(Q∀).
   - The receipt (REFUTED: "q_* pairs with the forward must-quotient"): edge 0→2, q = (0,1,1), φ = (1,0,1). Then q_*φ = (1,0) is not Q∀-closed but is Q←-closed.
   - **Backward sandwich.** Q←*(a,b) ≤ ⋀_{z∈b} ⋁_{x∈a} R*(x,z) ≤ Q∃*(a,b).

**Status.** PROVED; OBSERVED: the adjunction laws, reflection, counit formula, and both Beck–Chevalley equivalences hold exhaustively on Boolean n ≤ 3 and on noncommutative P(left-zero) with n ≤ 2.

**Time-reversal receipts.**
- Ghost 1→2 with q = (0,0,1): forward ✗, backward ✓.
- Reversed edge 2→1: forward ✓, backward ✗.
- The census contains both kinds.

**Does NOT establish.** Any duality beyond these adjunctions. In particular, Cl(R) and Cl(Q) are not shown equivalent.
**Interoperability.** Input: (R, q). Output: two mate tests, forward (left) and backward (right), each a finite check.

## CG-9. Ghost defect functional

**Statement.** PROVED. For φ ∈ Cl(R), let D_φ(b) = Lφ(b) \ q_!φ(b). Let G = ⋀_{x,b} Q*(q(x),b) \ ρ̂_x(b).
1. k ≤ D_φ(b) for all b ⇔ q_!φ ∈ Cl(Q), because q_!φ ≤ Lφ.
2. Exact ⇔ every D_φ is ≥ k ⇔ every D_{ρ_x} is ≥ k ⇔ **k ≤ G**.
3. Lρ_x = Q*(q(x),·). The bound "≥" uses k ≤ ρ̂_x(q(x)); the bound "≤" uses ρ̂_x ≤ Q*(q(x),·) and closedness of Q*(q(x),·). Hence D_{ρ_x}(b) = Q*(q(x),b) \ ρ̂_x(b). ∎

**What the defect returns at ρ_x.**
- Boolean: D = 0 exactly at the invented endpoints, which matches `audit_ancestral_observer` on all 2,594 models.
- Tropical: D = d_src − d_Q, truncated at 0, with ∞ − finite = ∞ for an invented endpoint. **This is exactly the shortcut amount.** G is the worst shortcut, and G = 0 iff exact.
- Viterbi: the relevance ratio.
- Boolean-algebra P(M): the residual is a quotient language; the invented traces are Lφ(b) ∖ q_!φ(b).

**Receipts.**
- Chain with unit costs: D(B) = 1 (2 vs 1).
- Edges 0→2 (3) and 1→2 (1), with q = (0,0,1): G = 2.
- k ≤ G ⇔ exact, exhaustively on Boolean n ≤ 3, tropical-budget-2 n ≤ 2 and P(left-zero) n ≤ 2.

**Status.** PROVED; OBSERVED.

## CG-10. Canonical coarsest exact refinement

**Statement.** PROVED for arbitrary X.
1. Exact partitions of X are closed under **arbitrary joins** in the partition lattice. The discrete partition is exact. So for every q there is a **unique coarsest exact refinement** q̂ of ker q.
2. For finite X, q̂ is the fixpoint of profile-splitting refinement: P₀ = ker q, P_{i+1} = P_i ∧ ker(x ↦ q_{P_i!}ρ_x).
3. **Value formula.** ρ̂_x(b) = ⋁_{blocks c ⊆ q⁻¹(b)} Q̂*(q̂(x),c). The true source values are computed by the canonical exact quotient.
4. **Base-change monotonicity.** If h is strict or oplax, V-exact implies W-exact, so q̂_V refines q̂_W.

**Proof.**
- (1): if π₁ is finer than π, then π-profiles are joins of π₁-profiles over the π₁-blocks inside each π-block. So π₁-equivalent states have equal π-profiles. The join π₁ ∨ π₂ is generated by finite chains of π₁- and π₂-steps, hence is exact.
- (2): every exact π ≤ ker q stays below every P_i, by the same coarsening argument. The fixpoint is exact.
- (3): partition the fibre q⁻¹(b) into q̂-blocks and apply CG-3(1) to q̂. ∎

**REFUTED / limits (receipts).**
- **Meets fail.** Edges {0→0, 0→3, 1→0, 1→2, 2→3, 3→0} with π₁ = {012|3} and π₂ = {01|23}: both exact, but the meet {01|2|3} is not. OBSERVED: no meet failure exists on ≤ 3 states (exhaustive), so 4 states is minimal for this.
- **Selected-start exact partitions are not join-closed, and there is no canonical coarsest one.** Edges {2→0, 2→1, 3→0}, start 0: {03|1|2} and {0|1|23} are both exact at 0, but their join {023|1} invents report {1}.

**Correction to the brief.** The worry that "exact partitions may not be closed under joins" is **refuted** for all-start exactness. It is **correct** for meets and for the selected-start variant.

**Status.** PROVED; OBSERVED exhaustively on all Boolean relations with n ≤ 3 (join closure; q̂ equals the brute-force maximum), on 60 random tropical models with n = 4, and the value formula on 120 random models over three quantales.
**Interoperability.** Input: (R, q). Output: the canonical exact report map q̂ ≤ q, and source values computed through it.

## CG-11. Weighted ghost certificate (weighted PAP-05)

**Format.** A certificate is (x, a quotient path q(x) = a₀ → … → a_n = b, φ). It is accepted iff:
- φ ∈ Cl(R), checked over the full finite edge table;
- k ≤ φ(x);
- w = ⊗ᵢ Q(aᵢ,aᵢ₊₁) satisfies w ≰ q_!φ(b).

**Soundness.** ρ̂_x(b) ≤ q_!φ(b) by CG-1(a), and w ≤ Q*(q(x),b). Hence Q*(q(x),b) ≰ ρ̂_x(b): the quotient over-claims from x, and quantitatively, every source path from x into fibre b has weight ≤ q_!φ(b).

**Completeness.** Holds in **any** V, with no attainment assumption. If Q*(q(x),b) ≰ ρ̂_x(b), then some single path has weight ≰ ρ̂_x(b), since otherwise their join would be below it. Take φ = ρ_x.

In tropical terms: a feasible potential with φ(x) = 0 and φ > w on fibre b proves that every source route costs more than the quotient's route.

**Status.** PROVED. Tested: an accepted tropical certificate; rejection of a non-separating bound, a non-closed invariant, a missing root, a wrong-start path and an empty path; and completeness on all Boolean n = 3 ghosts.
**Does NOT establish.** Validity against a truncated edge table. As in PAP-05, a partial table certifies nothing.

## CG-12. Whole-distance preservation

**Statement.** PROVED.
1. R*(x,z) = Q*(q(x),q(z)) for all x, z ⇔ ker q ⊆ ≅, where x ≅ x′ iff k ≤ R*(x,x′) and k ≤ R*(x′,x). In words, q only merges V-isomorphic states (mutually reachable at unit cost; zero distance both ways in the tropical case). This is CLASSICAL: it is the skeleton (T₀ reflection) of a V-category.
2. It implies all-start exactness, and it is **incomparable** with lumpability.
3. **Unpointed exactness** (Q* = q_!R* on the image) holds ⇔ q_!R* is transitive on q(X). It is strictly weaker than exactness; see the PAP-04 ghost.

**Proof of (1).**
- ⇐: R*(x,z) depends only on ≅-classes, by transitivity of R* and k ≤ R* across the class. So D(a,c) = R*(x,z) is well defined on the image, reflexive and transitive, and satisfies D ≥ Q. Hence Q* ≤ D, and CG-2 gives ≥.
- ⇒: if q(x) = q(x′), then R*(x,x′) = Q*(a,a) ≥ k. ∎

**Receipts for (2).**
- Fully faithful but not lumpable: 0 ⇄ 1 and 0→2, with q = (0,0,1).
- Lumpable but not fully faithful: two idle states merged.

**Status.** PROVED; OBSERVED on every model in the CG-3 battery.

## CG-13. Where idempotence ends: signed weights

Here A is a real matrix with A[y][x] the weight of x → y, as in the founding note's D = C A^{t−s−1} B. This is not a quantale.

**Statements.**
1. supp(ab) = supp a ∧ supp b, and supp(a+b) ≤ supp a ∨ supp b, with equality when a, b ≥ 0.
   - supp is a semiring homomorphism (ℝ≥0, +, ×) → Bool, and only join-lax on ℝ. ℝ≥0 is a semiring, not a complete quantale.
2. supp((A^τ)_{yx}) ≤ W_τ(x,y), where W_τ(x,y) means some length-τ walk exists in the support graph. Equality holds for A ≥ 0, and **more generally for sign-balanced A**: εDAD ≥ 0 with D = diag(±1). This is a **correction/extension** of the brief's "A ≥ 0".
   - *Proof.* Every x→y walk of length τ then has weight sign ε^τ d_x d_y. A sum of nonzero terms of one sign is nonzero.
   - This is CLASSICAL balance (Harary 1953). Cancellation therefore requires walk signs that are not balanced between the two endpoints.
3. **Minimal cancellation receipt.** A = [[1,0],[1,−1]] gives (A²)₁₀ = 1 − 1 = 0, though a walk exists.
   - Two states and τ = 2 are minimal: one state never cancels, and τ = 1 never cancels.
   - The founding note's z₁ = x, z₂ = x, y = z₁ − z₂ is the same phenomenon.
4. **Signed quotients both invent and delete,** which contrasts with CG-2, where deletion is impossible. Use the fibre-mean quotient Ā, which equals Kemeny–Snell's Â when the matrix is lumpable.
   - Receipt: edges x→z (1), x′→z (−1), x′→w (1), with q(x) = q(x′) = A, q(z) = B, q(w) = C. From x at τ = 1:
     - B: source 1, quotient 0 (deleted);
     - C: source 0, quotient ½ (invented).
   - A 3-state example at τ = 2 was found by exhaustive search over weights in {−1,0,1} and τ ≤ 2. The same search found none on 2 states, and none on 3 states at τ = 1. These are OBSERVED, scoped to those weights.
5. **Lumpability** (Kemeny–Snell, CLASSICAL): VᵀA = ÂVᵀ, i.e. Σ_{q(z)=b} A[z][x] depends only on q(x). It gives the aggregated response Σ_{q(z)=b}(A^τ)[z][x] = (Â^τ)[b][q(x)] for all τ. It is the signed analogue of one-step lumpability, which by CG-6(ii) is time-graded exactness.
6. **Exact relation to CG-3.** PROVED; new to the project; probably known in the lumpability literature. CG-3(2) is precisely **lumpability of the closure R***.
   - For idempotent V this is strictly weaker than lumpability of R (the PAP-04 chain).
   - For signed linear dynamics, with I − A invertible and q surjective: **(I−A)⁻¹ is lumpable ⇔ A is lumpable**, and then the lumped resolvent is (I−Â)⁻¹.
   - *Proof.* Vᵀ has rank m. VᵀN = N̂Vᵀ forces N̂ to be invertible, and then Vᵀ(I−A) = N̂⁻¹Vᵀ. The converse is symmetric.
   - So the gap between closure-exactness and one-step lumpability exists *because* R ↦ R* is not injective (R* = (R*)*), whereas A ↦ (I−A)⁻¹ is.
   - OBSERVED: all 69,280 (matrix, partition) pairs with entries in {−1,0,1}, n = 3, and invertible I − A.
7. **Generic faithfulness.** CLASSICAL in spirit: Lin 1974; Spirtes–Glymour–Scheines; Meek 1995 (unfaithful parameters have measure zero).
   - (A^τ)_{yx} is a polynomial in one indeterminate per support edge, with **nonnegative integer** coefficients counting walks per monomial. It is nonzero iff a length-τ walk exists.
   - Exact cancellation therefore lies on the zero set of a nonzero polynomial: a proper algebraic, Lebesgue-null subset of (ℝ∖0)^E. Tested: coefficients, evaluation against A^τ, and one-signed weights never cancel.

**Status.** (1)–(7) PROVED, with receipts tested.
**Does NOT establish.**
- A canonical signed "closure" geometry: a shortest-path metric on |weights| is still blind to cancellation, as CG-2 cannot be signed.
- Any statistical identifiability.
- Any physics.

**Interoperability.** Input: a signed matrix and q. Outputs:
- a support upper bound;
- lumpability, which guarantees exact aggregated responses at every horizon;
- otherwise, explicit invented and deleted reports.

---

## Summary table

| ID | Statement (short) | Status | Main receipt / evidence |
|---|---|---|---|
| CG-1 | R* = meet of closed predicates (left residual form; side convention forced) | PROVED; CLASSICAL in substance | 9,082 exhaustive relations; wrong-side, wrong-residual and M3 mutations |
| CG-2 | R* ≤ q^*Q* (only shortcuts are invented) | PROVED; CLASSICAL | every model |
| CG-3 | seven equivalent forms of all-start exactness, including Q∃(R) ≤ Q∀(R*) | PROVED | 2,594 Boolean + 18,113 two-state + 1,600 random; M3 breaks it |
| CG-4 | selected start: ρ̂_x ∈ Cl(Q) | PROVED | every start of every model |
| CG-5 | strict ⇒ transport; oplax ⇒ all-start transport; lax ✗; oplax-selected ✗ | PROVED + REFUTED parts | receipts 4, 5a, 5b; hierarchy witnesses |
| CG-6 | integral: 3 states minimal; non-integral: 2; graded ⇒ exact ⇔ lumpable (bisimulation) | PROVED | P(ℤ/2) two-state ghost; language sample |
| CG-7 | Q∀* ≤ M ≤ ρ̂ ≤ S ≤ Q∃*; may* = must* strictly stronger than exact | PROVED + REFUTED part | (∞,2,1); non-determination pair |
| CG-8 | L ⊣ q^* ⊣ Int∘q_*; left BC ⇔ forward, right BC ⇔ backward exactness | PROVED + REFUTED part (q_* vs Q∀) | exhaustive Boolean n ≤ 3, P(left-zero) n ≤ 2 |
| CG-9 | ghost defect; at ρ_x it equals the shortcut / invented endpoints | PROVED | tropical 1, 2; Boolean census |
| CG-10 | unique coarsest exact refinement; meets and selected-start fail | PROVED + REFUTED parts | 4-state receipts |
| CG-11 | weighted ghost certificate, sound and complete | PROVED | accept / five rejections / completeness |
| CG-12 | whole distance ⇔ ker q ⊆ ≅; unpointed ⇔ q_!R* transitive | PROVED; CLASSICAL | incomparability receipts |
| CG-13 | signed: lax supp, balance, invent+delete, resolvent lumpability ⇔ lumpability | PROVED | 2-state cancellation; 69,280 resolvent checks |

## Holdouts and test provenance

These values were **predicted by hand before running the code**, then pinned:
- the sandwich (∞, 2, 1);
- the chain defect (2, 1, 1);
- global defects 1 and 2;
- the language witness ({x,y} vs {x});
- the 4-state signed invent/delete values (1/0 and 0/½);
- the M3 values (0 vs c);
- the left-zero side receipt ({a} vs {b}).

These receipts were **found by search** and then minimised or checked by hand:
- lax receipts 5a and 5b;
- the oplax selected receipt;
- the partition meet and selected-join receipts;
- the M3 TFAE receipt;
- the 3-state signed τ = 2 example.

Mutation tests use M3 (not a quantale), opposite-side closedness, the wrong residual, and lax and oplax maps. The regression count 2,594 is reproduced independently and cross-checked against the existing audit.

## Open / unproved but promising

1. **Lean formalisation** of CG-1, CG-3 (including (5)), CG-7 and CG-10. Only the Boolean case exists, in `PrincipiaAncestral.lean`. CONJECTURED to need only `CompleteLattice` plus a ⊔-distributive monoid.
2. **Exact transport class.** Which join-preserving maps transport exactness beyond oplax ones? Lax fails; is oplax optimal among "law-defined" classes? UNVERIFIED.
3. **Selected-start canon.** The maximal selected-exact refinements are not unique. Describe them, e.g. as maximal elements of a convex family, and decide whether the hereditary exact region of CG-5(3) is canonical. CONJECTURED: the coarsest partition exact on Reach(x) exists.
4. **Open-map form.** Is CG-3(5) exactly "q is an open map for the closure path category" in the sense of Joyal–Nielsen–Winskel? This is a plausible re-statement and is UNVERIFIED.
5. **Probabilistic (non-idempotent) semirings.** Does an analogue of CG-13(6) hold for weak lumpability and for absorbing-chain fundamental matrices? UNVERIFIED.
6. **Complexity.** Polynomial bounds for computing q̂ over finite V of height h. Not analysed.
7. **Scale.** Exhaustive three-state checks over the eight-element quantales (8⁹ relations) need a faster engine. The current evidence there is a random sample.

## What this round does NOT establish

- No claim that physical causal coupling is a quantale.
- No positive Weil form, RH, π or physics statement.
- No promotion of any existing ledger item.
- The "relevance geometry" here is the V-category structure of declared finite tables. Its empirical calibration, from intervention identification and unit scales in the founding note, is untouched.

---

## Erratum added by the principal investigator after adversarial review (2026-11-14)

The text above is the workstream's report as delivered. The second hostile referee
([OPUS_IV_REFEREE_ROUND2.md](OPUS_IV_REFEREE_ROUND2.md), findings `S-n`, independent receipts in
`tests/test_observatoris_referee_round2.py`) found the following; the body is left unchanged so
the corrections stay visible. Every theorem it could test survived, including over a
noncommutative, non-integral value structure the workstream had not used.

- **CG-13(4) (S-9, REFUTED observation).** The statement that an exhaustive search found no
  three-state example at `τ = 1` in which the signed quotient both invents and deletes is false.
  Receipt: `x→x (1)`, `x′→x′ (−1)`, `x′→z (1)`, `q = (A,A,B)`: from `x` the source gives `(1, 0)`
  and the fibre-mean quotient gives `(0, ½)`. Three states at `τ = 1` is therefore the minimum;
  the four-state receipt in the text is valid but not minimal. The "three-state `τ = 2` example"
  mentioned in the text is never exhibited: UNVERIFIED.
- **CG-7 (S-3, REQUIRES REPAIR).** "Both outer links strict at one `(x,b)`" is true but the cited
  receipt has chain `(∞, ∞, 2, 1, 1)`, in which both outer links are equalities; it cannot happen
  over truth values. A valid receipt over the saturating tropical structure with all four links
  strict has chain `(∞, 3, 2, 1, 0)` (in the referee's tests).
- **CG-6(2) (S-7, REQUIRES REPAIR).** The grading `deg : M → ℕ` cannot exist on the truncated
  monoid used in the lab (the overflow element forces `deg(x) = 0`). With values in `ℕ ∪ {∞}` the
  theorem survives.
- **Census numbers (S-18).** The counts 462/384/384/240/240 quoted for CG-7 were not pinned by
  any test of the workstream; the referee reproduced them with independent code and pinned them.
- **Attribution (S-19).** CG-10 is the classical coarsest-lumpable-refinement / partition
  refinement fact (attributed by the referee, from memory, to Buchholz, Paige–Tarjan and
  Derisavi–Hermanns–Sanders); the global sign `ε = −1` in CG-13(2) is antibalance (Harary).
