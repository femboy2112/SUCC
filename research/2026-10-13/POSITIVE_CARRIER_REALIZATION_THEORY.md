# Positive Carrier Realization: the exact boundary between linear prediction and lawful carriers

**Status.** Conditional finite-source theorem architecture over exact rationals.  Kernel-checked
cores: `formal/EODCS_PositiveCarrier.lean` (Lean 4.14.0 root pin, no mathlib, no `sorry`,
compiled locally and gated lexically exactly as `eodcs-lean.yml` does).  Every finite certificate
in this dossier is reproduced byte-for-byte by `scripts/positive_carrier_probe.py` into
`research/2026-10-13/POSITIVE_CARRIER_RECEIPT.json` and re-executed by
`tests/test_eodcs_positive_carrier.py` (37 exact tests) and `tests/test_eodcs_positive_carrier_receipt.py`.
Snapshot: branch `research/positive-carrier-realization-2026-10-13` forked from PR #53 head
`9e7589e5` (carrier-indexed unification), whose base is PR #50 `759c30c7`.  Nothing here touches
`main`, PR #49's rolling worktrees, or any `research/swm-*` child branch.

Labels follow `docs/CLAIM_LEDGER.md`: CLASSICAL, EXTERNAL THEOREM, PROVED LOCAL (paper proof,
finite exact tests), LEAN-KERNEL VERIFIED, TESTED MODEL, CONJECTURE, REFUTED, UNVERIFIED.
Claims are ledgered as PCR-01 … PCR-24 in `docs/CLAIM_SUPPLEMENT_POSITIVE_CARRIER.md`.

**One-paragraph answer to the central question.**  A finite-dimensional source-indexed predictive
behavior admits a finite positive carrier realization iff its minimal linear realization carries
a polyhedral cone sandwiched between the closed reachable cone and the nonnegative-prediction
cone and invariant under every event operator (Heller's criterion, made exact for controlled,
source-indexed, bottom-completed behaviors, with the normalization derived rather than assumed).
This is strictly more than linear dimension.  Three independent obstruction mechanisms are
certified with finite witnesses: *support* (nonnegative rank / fooling sets; the lazy path walk
PW₁ has linear dimension 3 and needs 4 states, PWₙ needs 4ⁿ against 3ⁿ), *spectrum* (Frobenius
imprimitivity: a peripheral eigenvalue ρζ with ζ of order k forces ≥ k states, and an
irrational angle forces no finite carrier at all; the cyclotomic clocks C_k have linear
dimension 1+φ(k) and positive dimension exactly k; the rational clock with cos θ = 3/5 has
dimension 3 and no finite carrier), and *availability* (a quotient that preserves every
legal-word probability can still promote an illegal action; the bottom completion ⊥ turns
availability into a zero-probability observable and makes positivity sufficient for lawful
policy transport).  Positivity of the *legal-word* behavior alone is **not** sufficient for
lawful realization; positivity of the **bottom-completed** behavior is, and it transports every
public-history adaptive policy, its closed-loop joint law, and every source posterior.

---

## 0. Essential distinctions honored throughout

* A source label σ is a mathematical index of a declared preparation π_σ; nothing authenticates it.
* p_σ(w) is the unnormalized joint probability of the actual receipt history w; posteriors are ratios.
* Equal outcome marginals never imply equal joint outcome/post-state laws (CAR-08 in PR #53).
* A signed linear predictor (an OOM/PSR/multiplicity automaton) need not be a stochastic generator.
* A finite list of tests bounds the Hankel rank from below only; the upper bound comes from a
  realization (Prop. 3.1), never from a finite table.
* With source labels in Hankel *rows*, the latent index of a factorization is the carrier state
  c; only when source-propositions are placed in *columns* does the joint index (σ, c) appear
  (Remark 8.8), and then |Σ|·|C| is the honest bound.
* The one-stage matrix P is a calibration test.  The rank of the full sequential Hankel matrix is
  computed separately (Theorem 7.1) and happens to agree for PW₁ by a proof, not by assumption.

## 1. Setting

**D1 (positive carrier).**  Finite carrier C, finite action alphabet A, outcome alphabets Z_a,
event matrices M_{a,z} ∈ Q_{≥0}^{C×C} with the column convention
M_{a,z}[c'][c] = P(outcome z, next c' | current c, action a), enabled sets E_a ⊆ C, and declared
preparations π_σ ∈ Δ(C) for σ in a finite source set Σ.  Mass law: for every a and every
c ∈ E_a, Σ_z 1ᵀ M_{a,z} e_c = 1; for c ∉ E_a every column is zero.  An action with E_a = C is
*total*.  (Implementation: `PositiveCarrier`; PR #53's `CarrierInstrument` rows are exactly
these joint kernels and adapt by index.)

**D2 (bottom completion).**  Add to each action the refusal outcome ⊥ with
M_{a,⊥} = diag(1 − 1_{E_a}) (keep the state, emit mass 1 on disabled states).  Every action
becomes total; the mass law holds on all of C.  ⊥ is a representation change, not a sensor: by
D4 it has probability zero exactly on legal triples.

**D3 (words and probabilities).**  For a word w = (a₁,z₁)…(aₙ,zₙ) put M_w = M_{aₙ,zₙ} ⋯ M_{a₁,z₁}
(first event acts first, rightmost) and p_σ(w) = 1ᵀ M_w π_σ.  The source-indexed Hankel matrix
is H_{(σ,u),v} = p_σ(uv) (rows: source and recorded prefix; columns: future test), with
H = O·R, R_{c,(σ,u)} = (M_u π_σ)_c ≥ 0, O_{v,c} = (1ᵀ M_v)_c ≥ 0.

**D4 (legality).**  Action a is *uniformly available* after (σ,u) iff supp(M_u π_σ) ⊆ E_a; a word
is *legal* at σ iff each action is uniformly available when applied.  Equivalently, for legal u
with p_σ(u) > 0: a available ⟺ p_σ(u a ⊥) = 0.  Executing an unavailable action is illegal, not
an observation (PR #53 CAR-07: the action menu is not a hidden-state sensor).

**D5 (behavior).**  The *complete behavior* is p = (p_σ)_σ on all bottom-completed words; the
*legal behavior* is its restriction to legal words; the *legality pattern* is the function
(σ,u,a) ↦ [a available after (σ,u)] on legal u with p_σ(u) > 0.

**D6 (linear realization).**  (V, T_{a,z}, v_σ, τ) with p_σ(w) = τ(T_w v_σ).  It is *reachable* if
V = span{T_u v_σ}, *observable* if ⋂_v ker(τ∘T_v) = 0, *minimal* if both; dim of a minimal one is
the **linear predictive dimension** r(p).  Implementation: `minimal_realization` (exact
forward closure then observability quotient).

**D7 (positive carrier dimension).**  d⁺(p) = min |C'| over positive carriers (D1, all actions
total) with the same complete behavior; d⁺ = ∞ if none exists.  **Lawful positive dimension**
d⁺_law = min |C'| over carriers with enabled sets realizing the legal behavior *and* the
legality pattern.  **Bottom-completed positive dimension** d⁺_⊥ = d⁺ of the bottom-completed
behavior.  Always r ≤ d⁺ (H factors through C') and d⁺_law ≤ d⁺_⊥ (Prop. 8.1).

**D8 (cones in V).**  For a minimal realization put R̄ = closure of cone{T_u v_σ} (the *reachable
cone*) and P = {x : τ(T_w x) ≥ 0 ∀w} (the *nonnegative-prediction cone*).  Both are closed,
convex, T-invariant, and R̄ ⊆ P.

## 2. Calibration (mandatory)

**Proposition 2.1 (CLASSICAL / LEAN-KERNEL VERIFIED core).**  P = ½[[1,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,1]]
is row-stochastic; rank P = 3 with the explicit dependence r₁ − r₂ − r₃ + r₄ = 0; and rank₊ P = 4.

*Certificate.*  Upper bound: the four rows of P are themselves a nonnegative 4-term factorization.
Lower bound: the cells (1,1),(2,3),(3,2),(4,4) are positive and pairwise *fooling*
(P(i_k,j_l)·P(i_l,j_k) = 0 for k ≠ l), so in any factorization P = Σ_{t<m} u_t v_tᵀ with u_t,v_t ≥ 0
each fooling cell is covered by a term with both factors positive, and two fooling cells cannot
share a term (the shared term would make both cross cells positive).  Hence m ≥ 4.  Clearing
denominators turns any rational factorization into an integer one of a positive multiple of P
with the same support, so the integer statement
`calibration_fooling_bound : … → 4 ≤ m` in `formal/EODCS_PositiveCarrier.lean` is the
kernel-checked core.  (Mutation control: changing one fooling column makes `decide` refute the
fooling property — recorded in the receipt scope.)

Interpretation: a one-stage source→report experiment with the four Dirac preparations admits a
3-dimensional signed compression but cannot factor through any 3-state source-blind
preparation-and-readout mediator.  This is classical (Cohen–Rothblum-type example); it is not the discovery.

## 3. Minimal linear realization facts

**Proposition 3.1 (CLASSICAL, exact implementation).**  Let p be the complete behavior of a
positive carrier (bottom-completed).  (i) The minimal realization exists, is unique up to
similarity, and r(p) = rank H (infinite Hankel).  (ii) On a minimal realization, mass conservation
holds on all of V: τ∘Σ_z T_{a,z} = τ for every action a.  (iii) `minimal_realization` computes
it exactly: the reachable closure stabilizes after ≤ |C| extensions, the observability closure
likewise, and the quotient has dimension rank(O·R).

*Proof.*  (i) Standard multiplicity-automaton theory (Carlyle–Paz; Fliess; Thon–Jaeger): V_min =
span of the prediction functions f_{σ,u} = p_σ(u·), T_{a,z} = left shift by (a,z), τ = evaluation
at ε.  (ii) For reachable x = T_u v_σ: τ(Σ_z T_{a,z} x) = Σ_z p_σ(uaz) = p_σ(u) = τ(x) by the mass
law of the bottom-completed carrier; reachable vectors span V.  (iii) Both closures are exact
basis extensions in Q^C; the profile map v ↦ (f(v))_{f ∈ O} has kernel = reachable ∩ unobservable. ∎

**Lemma 3.2 (mass positivity, PROVED LOCAL).**  On a minimal realization of a valid behavior:
(a) every nonzero reachable vector has τ > 0; (b) R̄ ∩ ker τ = {0} and P ∩ ker τ = {0};
(c) consequently R̄ and P are pointed and every nonzero element of P has τ > 0.

*Proof.*  (a) If τ(T_u v_σ) = p_σ(u) = 0 then every continuation has p_σ(uv) ≤ p_σ(u) = 0 (the
terms of Σ_z p_σ(uaz) = p_σ(u) are nonnegative), so T_u v_σ is unobservable, hence 0.
(b) Let x ∈ P with τ(x) = 0.  Since P is T-invariant, τ(T_{a,z} x) ≥ 0 for all (a,z), and by 3.1(ii)
Σ_z τ(T_{a,z} x) = τ(x) = 0; hence each τ(T_{a,z}x) = 0, and by induction τ(T_w x) = 0 for all w,
so x = 0 by observability.  R̄ ⊆ P gives the other half.  (c) A line in P would contain x and −x
with τ(x) ≥ 0 and τ(−x) ≥ 0, so x ∈ ker τ ∩ P = 0. ∎

## 4. The cone theorem, made exact

Throughout, (V, T, v_σ, τ) is a linear realization of the complete behavior p — minimal unless said
otherwise — and g₁,…,g_m ∈ V, K = cone(g₁,…,g_m).

**Hypotheses.**
(N) normalization: τ(g_i) = 1 for all i;
(P) preparations: v_σ ∈ K for all σ;
(I) invariance: T_{a,z} K ⊆ K for all (a,z);
(M) mass conservation on generators: τ(Σ_z T_{a,z} g_i) = 1 for all a, i.

**Theorem 4.1 (cone ⇒ carrier; CLASSICAL direction, exact constructive form; PROVED LOCAL + TESTED).**
Under (N),(P),(I),(M) choose, for each (a,z) and i, nonnegative coefficients with
T_{a,z} g_i = Σ_j B_{a,z}[j][i] g_j (they exist by (I); any choice works), and λ_σ ≥ 0 with
v_σ = Σ_i λ_σ[i] g_i.  Then (B_{a,z}, λ_σ) is a positive carrier on m states with the same complete
behavior, and
  1ᵀ Σ_z B_{a,z} = 1ᵀ   (column-stochastic)   and   Σ_i λ_σ[i] = 1.

*Proof.*  Let G: Q^m → V, G e_i = g_i.  Then T_{a,z} G = G B_{a,z}, hence T_w G = G B_w by induction
(same multiplication order).  τ(T_w v_σ) = τ(T_w G λ_σ) = τ(G B_w λ_σ) = Σ_j (B_w λ_σ)_j τ(g_j) =
1ᵀ B_w λ_σ by (N).  Normalization: Σ_z Σ_j B_{a,z}[j][i] = Σ_z τ(T_{a,z} g_i) = τ(Σ_z T_{a,z} g_i) = 1
by (N),(M) — this is exactly the stochastic requirement, and (M) is *derived* from (N) on a
minimal realization by Prop. 3.1(ii); Σ_i λ_σ[i] = τ(v_σ) = 1 by (N).  Nonnegativity is by choice. ∎

Three consequences of (N) that the brief asked to be settled:
* *Pointedness is automatic:* Σλ_i g_i with λ ≥ 0 has τ = Σλ_i, so K ∩ ker τ = {0}; a line would
  lie in ker τ.  No separate pointedness hypothesis is needed.
* *Convexity of the source representation is automatic:* v_σ ∈ K and τ(v_σ) = 1 force Σλ = 1.
* *Nonzero generators are automatic:* τ(g_i) = 1.
* *Mass positivity is a hypothesis only off the reachable span:* on a non-minimal V, (M) can fail
  for generators outside span{T_u v_σ}; the stochastic normalization of B then fails exactly
  there.  For V = V_min, or for V = the span of the prediction functions of an actual carrier,
  (M) holds (τ(Σ_z T_{a,z} g_c) = column sum of a stochastic matrix).

**Theorem 4.2 (carrier ⇒ cone; CLASSICAL, PROVED LOCAL).**  Let (C', M', π') be an m-state positive
carrier of p.  Let Φ: Q^{C'} → F (functions on words), Φ(e_c)(v) = 1ᵀ M'_v e_c.  Then
(i) W := im Φ is an observable realization of p of dimension ≤ m with T = shift, τ = ev_ε, and
V_min ⊆ W as a T-invariant subspace;
(ii) K_W = cone(Φ e_c) satisfies (N),(P),(I),(M) in W;
(iii) K := K_W ∩ V_min is a polyhedral T-invariant cone in V_min with R̄ ⊆ K ⊆ P, satisfying (N)
after normalization, (P), (I), (M) — but possibly with **more than m** extreme rays.

*Proof.*  Φ M'_{a,z} = T_{a,z} Φ is the identity (Φ M'_{a,z} e_c)(v) = 1ᵀ M'_v M'_{a,z} e_c = (Φ e_c)(az v).
v_σ = Φ π'_σ is in K_W, and T_u v_σ = Φ(M'_u π'_σ) ∈ K_W, so K_W ⊇ reachable, hence K_W ⊇ R̄ after
intersecting with V_min (closedness of polyhedral cones).  K_W ⊆ P: for g ∈ K_W, T_w g ∈ K_W ⊆ {τ ≥ 0}.
Intersection of a polyhedral cone with a subspace is polyhedral (Minkowski–Weyl).  Generator count:
a d-dimensional section of an m-generator simplicial cone can have Θ(m^{⌊(d−1)/2⌋}) rays
(upper bound theorem), so no bound ≤ m is available. ∎

**Theorem 4.3 (exact criterion — Heller's theorem in the controlled, source-indexed, bottom-completed
setting; CLASSICAL core, PROVED LOCAL specialization).**  For a valid finite-dimensional behavior p:
  d⁺(p) < ∞  ⟺  there is a polyhedral cone K ⊆ V_min with R̄ ⊆ K ⊆ P and T_{a,z} K ⊆ K for all (a,z).
Moreover d⁺(p) = min over observable extensions W ⊇ V_min (as in 4.2(i)) of the minimum number of
generators of a cone in W satisfying (N),(P),(I),(M); and the *restricted* quantity
d⁺_res(p) := min #generators of such K inside V_min satisfies d⁺ ≤ d⁺_res, with d⁺ < ∞ ⟺ d⁺_res < ∞.

*Proof.*  ⇒ is 4.2(iii).  ⇐: K polyhedral has finitely many extreme rays; by Lemma 3.2(c) each has
τ > 0, so normalize them to generators; (P) since R̄ ⊇ {v_σ}; (I) given; (M) by Prop. 3.1(ii).
Apply 4.1.  The equality for d⁺ is 4.1 + 4.2(i),(ii) (the carrier obtained from a cone in W with m
generators has m states, and any m-state carrier yields such a W).  d⁺ ≤ d⁺_res because V_min is
itself an admissible W. ∎

**Proposition 4.4 (restricted vs unrestricted; EXTERNAL THEOREM + PROVED LOCAL transfer; gap not
exhibited here).**  The one-shot embedding of a nonnegative matrix H (Lemma 7.4 below) has
d⁺ = rank₊(H) + 1 and d⁺_res = rank₊*(Hᵀ) + 1, where rank₊* is the restricted nonnegative rank of
Gillis–Glineur (factor column space = column space of the matrix; here the readout rows must lie
in the row space of H, i.e. the restriction is on Hᵀ).  Since rank₊*(M) > rank₊(M) occurs
(Gillis–Glineur 2012; take H = Mᵀ), d⁺_res > d⁺ occurs for behaviors.  The oracle's cone search is restricted
(it searches V_min), hence it is complete only for d⁺_res; this is why it can only answer
UNRESOLVED, never "impossible".

**Proposition 4.5 (rational vs real; EXTERNAL THEOREM + PROVED LOCAL transfer).**
(a) If the data and the generators are rational, the carrier of 4.1 is rational: the coefficients
are solutions of rational LPs (`cone_coordinates`, exact phase-I simplex with Bland's rule).
(b) There is a rational behavior with d⁺_ℝ = 6 and d⁺_ℚ = 7: take the Chistikov–Kiefer–Marušič–
Shirmohammadi–Worrell 6×11 rational matrix with rank₊ 5 over ℝ and 6 over ℚ (SIAM J. Appl.
Algebra Geom. 2017), scale rows to be stochastic (positive diagonal scaling preserves rank₊ over
either field), and apply Lemma 7.4.  Hence *existence of a positive carrier over ℝ does not give one
over ℚ of the same size*; exact-arithmetic realizability is a strictly stronger demand.
(c) Decidability: for fixed m, "∃ m-state real positive carrier" is a finite polynomial system in
the unknowns (B_{a,z} ≥ 0, λ_σ ≥ 0, G) — namely T_{a,z} G = G B_{a,z}, G λ_σ = v_σ, τ G = 1ᵀ — in the
existential theory of the reals (PSPACE).  Searching m = r, r+1, … is a semi-algorithm for d⁺ < ∞;
whether finiteness of d⁺ is decidable is not claimed (open in the HMM-realization literature), and
decidability over ℚ is open even for one-shot matrices (CKMSW).

**Proposition 4.6 (termination and soundness of the implemented verifier; PROVED LOCAL).**
`verify_cone` terminates (finitely many exact LPs; Bland's rule prevents cycling) and is sound:
`valid = True` only if (N),(P),(I),(M) hold exactly, and then `carrier_from_cone` is a carrier with the
same complete behavior (Theorem 4.1), which `equivalence_certificate` re-checks independently by
an exact difference-realization closure (two realizations of dimensions n, m agree iff the
reachable space of the direct sum with mass (τ₁, −τ₂) is unobservable; the closure terminates in
≤ n + m steps).  `reachable_cone_refinement` only adds reachable rays, so every generator it uses lies
in R̄; it terminates with LAWFUL_REALIZATION only after an exact invariance proof, and otherwise with
UNRESOLVED (budget), never with an impossibility verdict.

## 5. Low dimension collapses

**Theorem 5.1 (PROVED LOCAL; cf. Schönhuth 2009, Cor. 5.2 for uncontrolled Mealy HMMs).**  Over ℝ,
r(p) ≤ 2 ⇒ d⁺(p) = r(p).  Over ℚ this is not claimed (see 5.2).

*Proof.*  r = 1: v_σ spans; T_{a,z} v_σ = p_σ(az) v_σ with p ≥ 0 summing to 1 — a 1-state carrier.
r = 2: R̄ is a closed convex cone in ℝ², pointed with R̄ ∩ ker τ = 0 (Lemma 3.2), hence a sector with
two extreme rays (or a ray, contradicting r = 2); it is T-invariant and contains every v_σ; normalize
the two rays (τ > 0 on R̄∖0) and apply Theorem 4.3 (K = R̄ ⊆ P). ∎

**Remark 5.2 (where ℚ may already fail).**  The extreme rays of R̄ are limits of reachable rays and
may be Perron directions of some T_w with irrational slope (quadratic irrationalities already occur
for 2×2 rational matrices).  If moreover R̄ = P, then K = R̄ is forced and no rational 2-state carrier
exists although a real one does.  Whether R̄ = P can occur with irrational rays at r = 2 is UNVERIFIED;
it is the smallest candidate for a ℚ/ℝ gap below the CKMSW rank-4 threshold.

## 6. The peripheral-spectrum obstruction (quantitative)

**Theorem 6.1 (PROVED LOCAL; classical ingredients: Frobenius 1912, Fox–Rubin 1968 for stationary
processes, Anderson–Deistler–Farina–Benvenuti 1996 for SISO positive systems).**  Let p have an
m-state positive carrier and let (V_min, T, v_σ, τ) be minimal.  Then for **every** event word w and
every eigenvalue λ of T_w with |λ| = ρ(T_w):  λ = ρ(T_w)·ζ with ζ a root of unity of order ≤ m.
In particular, if some peripheral ratio λ/ρ is not a root of unity, then d⁺(p) = ∞, and if it is a
primitive k-th root of unity then d⁺(p) ≥ k.

*Proof.*  Let S ⊆ C' be the set of positively reachable states, S = ⋃_{σ,u} supp(M'_u π'_σ).  S is
closed under all events (mass flows only along positive entries), so N := M'_w|_{S×S} is a nonnegative
matrix and p is realized by the restriction to S.  Let Φ be as in 4.2 with domain Q^S; then
ker Φ is N-invariant and Φ N = T_w Φ on W = im Φ ⊇ V_min, so
  χ_{T_w|V_min} | χ_{T_w|W} | χ_N,   hence   spec(T_w) ⊆ spec(N) (with multiplicity) and ρ(T_w) ≤ ρ(N).
Conversely, Perron–Frobenius gives x ≥ 0, x ≠ 0, N x = ρ(N) x.  Choose a finite family F of pairs
(σ,u') with u := Σ_F M'_{u'} π'_σ > 0 on S (possible since each state of S is reached by some pair);
then u ≥ δx for some δ > 0 and
  δ ρ(N)ⁿ 1ᵀx ≤ 1ᵀ Nⁿ u = Σ_F p_σ(u' wⁿ) = Σ_F τ(T_wⁿ T_{u'} v_σ) ≤ C·n^{r}·ρ(T_w)ⁿ,
so ρ(N) ≤ ρ(T_w).  Thus ρ(N) = ρ(T_w) =: ρ.  If ρ = 0 there is nothing to prove.  Otherwise every
peripheral eigenvalue λ of T_w is a peripheral eigenvalue of the nonnegative matrix N.  Put N in
Frobenius normal (block-triangular) form; λ is an eigenvalue of an irreducible diagonal block B with
ρ(B) = ρ, and by Frobenius' theorem the peripheral spectrum of B is ρ·μ_h, h the index of
imprimitivity of B.  Hence λ/ρ is an h-th root of unity, and B, being h-cyclic, has at least h
states (one per cyclic class).  So ord(λ/ρ) ≤ h ≤ |S| ≤ m. ∎

**Corollary 6.2 (finite certificate).**  `peripheral_spectrum_certificate` computes χ_{T_w} exactly
(Faddeev–LeVerrier over ℚ), splits off all rational roots (rational root theorem), and decides the
cofactor when it is (a) a quadratic x² − bx + c with b² < 4c — then ρ² = c and λ/ρ is a root of
unity iff b²/c ∈ {0,1,2,3} (the ratio w = λ/λ̄ = λ²/c satisfies c w² + (2c − b²) w + c = 0, so it is a root
of unity of degree ≤ 2 iff that polynomial is Φ₂², Φ₃, Φ₄ or Φ₆; the respective orders of λ/ρ are
4, 6 or 3, 8, 12) — or (b) a scaled cyclotomic ρ^d Φ_k(x/ρ) with rational ρ (orders recognized by
exact comparison with Φ_k computed from Φ_k = (x^k − 1)/∏_{d|k,d<k} Φ_d).  Peripherality is decided by
exact comparison of moduli squared; real irrational quadratic cofactors are bounded exactly when
ρ² is a rational square.  Anything else returns UNRESOLVED.  No floating point is used.

The number-theoretic input for the rational clock is kernel-checked:
`gaussian_rotation_never_real : ∀ n, (gpow (n+1)).2 ≠ 0` via the invariant (a,b) ≡ (3,4) (mod 5) for
(3+4i)^n = a + bi, n ≥ 1 (equivalently Niven's theorem: cos θ = 3/5 ∉ {0, ±½, ±1} ⇒ θ/π ∉ ℚ).

## 7. Separation theorems with finite certificates

Three families, three mechanisms.  All data rational; all certificates in the receipt.

### 7.1 Support obstruction: the lazy path walk PWₙ (two non-commuting actions)

**Definition.**  PW₁: carrier C = {1,2,3,4}; action **a** ("step and report the position"):
M_{a,z}[c'][c] = P[c][z]·[c' = z] (lazy reflecting walk on the path 1–2–3–4, position observed);
action **b** ("silent pair swap"): the permutation (1 2)(3 4), single outcome.  Sources: the uniform
preparation u and, for n = 1, the four Dirac preparations.  PWₙ := PW₁^{⊗n} (n independent copies,
both actions act on every coordinate, the outcome of a is the position tuple).
P·S ≠ S·P: the interventions do not commute (receipt `PW1`).

**Theorem 7.1 (PROVED LOCAL; n = 1 lower bound LEAN-KERNEL VERIFIED core).**
r(PWₙ) = 3ⁿ and d⁺(PWₙ) = 4ⁿ.  In particular PW₁ has linear dimension 3, no 3-state positive
carrier realizes its complete behavior, and the 4-state carrier does.  The lower bound holds
already for the single uniform source.

*Proof.*  (r ≤ 3ⁿ.)  Let f_c be the prediction function of state c and ε = (1,−1,−1,1).  Claim
Σ_c ε_c f_c ≡ 0 for n = 1: f_c(ε) = 1 gives Σε = 0; f_c(az·v) = P[c][z] f_z(v) and εP = 0; f_c(b·v) =
f_{S(c)}(v) and ε∘S = −ε, so Σ_c ε_c f_{S(c)} = −Σ_c ε_c f_c = 0 by induction on |v|.  Hence
dim span{f_c} ≤ 3.  For PWₙ the prediction functions are tensor products f_{c₁}⊗⋯⊗f_{cₙ}
(independent coordinates, both actions act coordinatewise), so span ≤ (span for n = 1)^{⊗n},
dimension ≤ 3ⁿ.  (r ≥ 3ⁿ.)  With the uniform source, after one a-step every position tuple z has
probability 4^{−n}·p > 0 and the current law is δ_z, so every f_c is reachable; the one-step block
of the Hankel matrix restricted to these rows and the columns (a,z') is diag(p_u(az))·P^{⊗n}, of rank
3ⁿ.  Hence V_min = span{f_c} has dimension exactly 3ⁿ.  (d⁺ ≥ 4ⁿ.)  Any m-state carrier factors that
block nonnegatively through m (D3); a positive diagonal row scaling preserves the support, and the
product F^n of the fooling set F = {(1,1),(2,3),(3,2),(4,4)} is a fooling set of P^{⊗n} of size 4ⁿ
(fooling sets are multiplicative under Kronecker product: positivity of a product cell is
coordinatewise, and a shared term would make a cross cell positive in every coordinate); so m ≥ 4ⁿ.
(d⁺ ≤ 4ⁿ.)  The product carrier.  Exact checks: n = 1 (block rank 3, fooling 4, oracle verdicts
FINITE_OBSTRUCTION at 3 and LAWFUL_REALIZATION at 4 with an equivalence certificate), n = 2 (block
rank 9, product fooling set of size 16 verified). ∎

Minimality in r: by Theorem 5.1 no behavior with r ≤ 2 has a gap, so (r, d⁺) = (3, 4) is the smallest
possible gap pair, and PW₁ attains it with two non-commuting interventions, all states reachable
from one full-support preparation, and a lower bound that does not depend on multiple sources.

### 7.2 Spectral obstruction, irrational: the rational probability clock

**Definition.**  V = ℚ³ with coordinates (m, x, y); τ = (1, ¼, 0);
T_tick = ½·diag(1, Rot), Rot = [[3/5, −4/5],[4/5, 3/5]];  v_* = (4/5)(1, 1, 0);  v₀ = (1, 0, 0);
T_reset = v_*·(τ − τT_tick) (rank one: emit the leftover mass and restart at v_*);
action **clock** has outcomes {tick, reset}; action **b** ("hard reset", silent) has T_b = v_* τ.
Sources s₀ ↦ v₀, s_* ↦ v_*.  T_tick T_b ≠ T_b T_tick.

**Theorem 7.2 (PROVED LOCAL; LEAN-KERNEL VERIFIED number-theoretic core).**  The clock is a valid
behavior (every word probability ≥ 0, mass conserved), its linear dimension is 3, and it has **no
finite positive carrier**: d⁺ = ∞.

*Proof.*  Validity: τ(v_*) = 1 and τT_tick + τT_reset = τT_tick + τ(v_*)(τ − τT_tick) = τ, so the clock
action is mass-conserving; b is mass-conserving since τ(T_b x) = τ(x)τ(v_*).  Let
S = {λ T_tickⁿ v : λ ≥ 0, n ≥ 0, v ∈ {v₀, v_*}}.  Put q_v(n) = τ(T_tickⁿ v): q_{v₀}(n) = 2^{−n} and
q_{v_*}(n) = (4/5) 2^{−n}(1 + ¼ cos nθ) with cos nθ = Re((3+4i)/5)ⁿ ∈ ℚ, so 0 < q_v(n+1) ≤ q_v(n)
(indeed ¾ ≥ ½·5/4).  Then T_tick S ⊆ S, T_reset(λT^n v) = λ(q_v(n) − q_v(n+1)) v_* ∈ S and
T_b(λT^n v) = λ q_v(n) v_* ∈ S, so every T_w v_σ ∈ S and p_σ(w) = τ(T_w v_σ) ≥ 0.  Minimality: v₀,
v_* = 2T_reset v₀ and T_tick v_* are independent, so reachable; τ, τT_tick, τT_tick² are independent,
so observable (exact check in the receipt).  χ_{T_tick} = (x − ½)(x² − (3/5)x + ¼): all three
eigenvalues have modulus ½, and the complex pair is ½e^{±iθ} with cos θ = 3/5.  By the kernel-checked
invariant, (3+4i)ⁿ ∉ ℝ for n ≥ 1, so e^{iθ} is not a root of unity.  Theorem 6.1 with w = tick gives
d⁺ = ∞.  (The word tick·b has peripheral spectrum {½} ∪ {0}: the reset kills the rotation, so the
certificate is word-sensitive, as it must be.) ∎

Exhaustive exact check: 19,682 words of length ≤ 8 from both sources, none negative.

### 7.3 Spectral obstruction, finite: the cyclotomic clocks C_k (unbounded exact gaps)

**Definition.**  For k ≥ 3 let Φ_k be the k-th cyclotomic polynomial, φ = φ(k), C the companion
matrix of Φ_k (rational, order exactly k, irreducible characteristic polynomial).  V = ℚ ⊕ ℚ^φ,
T_tick = ½(1 ⊕ C), τ = (1, ε, 0, …, 0) with ε > 0 chosen so that |ε (Cⁿ e₁)₁| ≤ ¼ for all n (finite
orbit), v_* ∝ (1, e₁), v₀ = (1, 0), T_reset = v_*(τ − τT_tick), T_b = v_* τ, sources s₀, s_*.

**Theorem 7.3 (PROVED LOCAL; exact finite checks for k ∈ {3,4,5,6,8,10,12,30}).**
C_k is a valid behavior with  r(C_k) = 1 + φ(k)  and  d⁺(C_k) = k  exactly.

*Proof.*  Validity exactly as in 7.2 (the orbit {Cⁿ e₁} is finite and ε bounds its visibility by ¼).
Minimality: v₀ and v_* are reachable; {Cⁿ e₁} spans ℚ^φ because Φ_k is irreducible, so C has no proper
invariant rational subspace and every nonzero vector is cyclic; likewise {e₁ᵀ Cⁿ} spans the dual,
so τT_tickⁿ separate.  Hence r = 1 + φ.  Lower bound: χ_{T_tick} = (x − ½)·2^{−φ}Φ_k(2x), whose roots are
½ and ½ζ for every primitive k-th root of unity ζ, all of modulus ½; Theorem 6.1 with the peripheral
eigenvalue ½ζ_k (order k) gives d⁺ ≥ k.  Upper bound: let g_j be the τ-normalization of T_tick^j v_*,
j = 0,…,k−1, and K = cone(g_j).  T_tick g_j ∝ g_{j+1 mod k} (T_tick^k = 2^{−k}·id); T_reset g_j =
(1 − τT_tick g_j) v_* with nonnegative coefficient; T_b g_j = v_* = g₀; and v₀ ∈ K because
Σ_{j<k} (1, C^j e₁) = (k, 0) as Σ_{j<k} C^j = 0 (C − I is invertible and (C − I)ΣC^j = C^k − I = 0).
Hence (N),(P),(I),(M) hold and Theorem 4.1 gives a k-state carrier (verified by exact LP and an
exact equivalence certificate for each listed k; k − 1 orbit generators fail for k = 4, 6). ∎

Numerics of the gap: (r, d⁺) = (3,4), (3,6), (5,8), (5,10), (5,12), (9,30) for k = 4, 6, 8, 10, 12, 30;
for k a prime, r = d⁺ = k (no gap, e.g. k = 5); along primorials k = 2·3·5·7⋯, r/d⁺ = (1+φ(k))/k → 0.
**Support-blindness.**  For C₆ the Hankel block (rows tick^i from s_*, columns tick^j·reset) is
strictly positive, so every fooling-set / rectangle-covering / Boolean-rank bound equals 1 while the
truth is 6: the spectral mechanism is invisible to support arguments, and conversely PWₙ's gap is
invisible to spectral arguments (all its event operators have rational spectra).  An oracle needs both.

### 7.4 The one-shot embedding (transfer lemma)

**Lemma 7.4 (PROVED LOCAL).**  Let H ∈ ℚ_{≥0}^{Σ×Z} be row-stochastic.  The *one-shot behavior* of H has
one action a with outcomes Z, preparations π_σ, p_σ(az) = H[σ][z], and after one step every further
action yields ⊥ deterministically (bottom-completed: p_σ(az·v) = H[σ][z] for every v made of ⊥'s,
p_σ(a⊥) = 0).  Then, over any field 𝔽 ⊇ ℚ,  d⁺_𝔽 = rank₊^𝔽(H) + 1  and  d⁺_{res,𝔽} = rank₊*^𝔽(Hᵀ) + 1
(restricted on the readout side: the rows of the right factor lie in the row space of H).

*Proof.*  Upper bound: from H = WV (Σ×m, m×Z, nonnegative) put s_j = Σ_z V[j][z] > 0 (zero rows can be
dropped), states {1..m} ∪ {d}, π_σ[j] = W[σ][j] s_j (sums to Σ_z H[σ][z] = 1), M_{a,z}[d][j] = V[j][z]/s_j,
M_{a,⊥}[d][d] = 1: an (m+1)-state carrier.  Lower bound: in any carrier, p_σ(a⊥) = 0 forces π_σ to be
supported on *live* states L (those with zero ⊥-mass under a); H = Λ_L B_L with Λ_L[σ][c] = π_σ[c] and
B_L[c][z] = 1ᵀM_{a,z}e_c, so |L| ≥ rank₊(H); and the post-step law M_{a,z}π_σ ≠ 0 must be supported on
states producing ⊥ with probability 1 forever, which are not live, so |C'| ≥ |L| + 1.  Restricted
version: a cone generator g in V_min = span{v_σ} ⊕ ℚf_d that is live has g(a⊥) = 0, hence lies in
span{v_σ}; as a function of the outcome z it lies in the row space of H.  So H = Λ_L B_L with the rows
of B_L in rowspace(H), i.e. Hᵀ = B_Lᵀ Λ_Lᵀ with col(B_Lᵀ) ⊆ col(Hᵀ): the restricted factorization of Hᵀ. ∎

## 8. Causal, source-faithful layer: availability, policies, destructive observation, resources

**Proposition 8.1 (legality is a function of the bottom-completed behavior; PROVED LOCAL).**
For legal u with p_σ(u) > 0: a is available after (σ,u) iff p_σ(ua⊥) = 0.  Consequently
(i) any positive carrier of the bottom-completed behavior of K has the same legality pattern as K;
(ii) d⁺_law ≤ d⁺_⊥; (iii) the legality pattern of any lawful carrier is determined by its own bottom
completion, so two lawful carriers that agree on legal words and on the *zero pattern* of ⊥-events
are lawfully equivalent even if their ⊥-masses differ.

*Proof.*  p_σ(ua⊥) = 1ᵀ M_{a,⊥} M_u π_σ = mass of M_u π_σ outside E_a, zero iff supp ⊆ E_a.  (i) is
induction on |u|; (ii) a carrier of the completion is lawful by (i); (iii) by definition of the pattern. ∎

**Theorem 8.2 (adaptive policy transport; LEAN-KERNEL VERIFIED skeleton `closed_loop_law_transport`,
PROVED LOCAL body).**  Let K, K' be lawful carriers over the same sources with equal legal behavior and
equal legality pattern.  Let ψ be any public-history policy (ψ(a | h) depending on the recorded history
h only, possibly randomized, possibly stopping).  Then ψ is legal for K iff legal for K', and for every
source σ the closed-loop joint law of actual (action, receipt) histories agrees:
  P^ψ_σ(h) = ∏_{i} ψ(a_i | h_{<i}) · p_σ(h),
and every source posterior Pr(σ | h) ∝ prior(σ) p_σ(h) agrees.  In particular original-target
certification status (CERTIFIED / AMBIGUOUS / INCONSISTENT, as in PR #53 `decide_original`) is
transported.

*Proof.*  Legality of ψ is a statement about the legality pattern.  By the chain rule
P(z_i | h_{<i}, a_i) = p_σ(h_{≤i})/p_σ(h_{<i}) (bottom-completed mass law), and the telescoping product
gives the formula; both factors are equal for K and K'.  The Lean statement records that the
closed-loop law is literally a function of the behavior on legal histories. ∎

**Proposition 8.3 (minimal failed availability square; REFUTED claim "positivity of the legal
behavior suffices"; PROVED LOCAL).**  FINE: C = {0,1}, action a total (outcome o, keep state),
action b enabled on {0} only (outcome ok, keep state); sources pure = δ₀, mixed = (½,½).
COARSE: one state, a and b total.  Then: every legal-word probability agrees (all equal 1);
r(legal behavior) = 1 and COARSE is a 1-state positive carrier of it; yet after the empty history at
the mixed source FINE's menu is {a} and COARSE's is {a,b} — COARSE promotes an unavailable action into
a legal one, and the policy "execute b" is legal in COARSE and illegal in FINE.  Minimality: one
state cannot carry two distinct menus for two sources (the menu is a function of the support);
one action cannot be both available and unavailable; one source cannot witness a difference.  The
bottom-completed FINE behavior has r = 2 (p_mixed(b⊥) = ½, p_pure(b⊥) = 0) and d⁺_law = d⁺_⊥ = 2.

**Lemma 8.4 (menu-count obstruction; PROVED LOCAL).**  The menu after a legal history depends only on
the support of the current law, so a lawful carrier with m states exhibits at most 2^m − 1 distinct
menus; hence d⁺_law ≥ log₂(#distinct menus + 1).  (For 8.3: two menus ⇒ m ≥ 2.)

**Proposition 8.5 (weakest source-preserving repair; PROVED LOCAL).**  Given a carrier K and a
quotient q that fails the availability square, the coarsest lawful refinement is the partition by
(q-label, enabledness profile, pushed joint law) — PR #53's CAR-4 one-step q* with the enabledness
component — iterated to its stationary fixed point (CAR-12).  In realization terms (no quotient
assumed), the weakest repair is: realize the bottom completion.  It is weakest in the sense that any
lawful realization of K realizes a bottom-completion-like behavior (Prop. 8.1(iii)) with the same zero
pattern, and the completed behavior is the *canonical* choice of ⊥-masses; d⁺_law ≤ d⁺_⊥, and whether
the inequality can be strict (a cheaper lawful carrier with different ⊥-masses) is UNVERIFIED.

**Remark 8.6 (destructive observation).**  If an action collapses the current law (e.g. an erase),
source knowledge survives in the scalar p_σ(h), i.e. in J_h, not in the post-state.  Theorem 8.2 shows
that any realization of the complete behavior preserves exactly this: the posterior is a ratio of
behavior values and is transported even when the carrier state after h is source-independent.
PR #53 CAR-13 is the quotient instance.

**Proposition 8.7 (resources are a graded product; PROVED LOCAL).**  Let cost: A → ℕ and a budget
B.  The budgeted process is K × {0,…,B} with the counter decremented deterministically and
E_a^{(b)} = E_a × {b ≥ cost(a)}.  Its bottom-completed linear dimension is ≤ r_⊥(K)·(B+1) and its
positive dimension ≤ d⁺_⊥(K)·(B+1); its carrier space is ℕ-graded, V = ⊕_b V_b with T_a: V_b → V_{b−cost(a)},
and an invariant cone of the product is ⊕_b K_b with each K_b a face.  Costs attach to actions, not
to states, and never change which words are legal in K alone; they only restrict availability through
the counter.  (Nothing deeper is claimed; this records that the brief's "faces / graded carrier
spaces" are the right objects and that they do not interact with positivity.)

**Remark 8.8 (source tags).**  A *source-blind* carrier has one M per action and one π_σ per source.
If the behavior must also answer source-propositions as *tests* (columns "original = σ₀"), the
latent index is (σ, c) and realizations are products Σ × C'; bounds on |C'| must then be read as
bounds on |Σ|·|C'|.  All dimensions in §7 are source-blind.

## 9. Main theorem (corrected form) and what is false as originally posed

**Theorem 9.1 (Source-Indexed Causal Carrier Realization; PROVED LOCAL from §§3–8).**
Let K be a finite lawful carrier (D1) with complete behavior p and legal behavior p_leg.
(A) [positive realization]  A finite positive carrier realizes the bottom-completed behavior p iff the
minimal realization of p admits a polyhedral cone K with R̄ ⊆ K ⊆ P invariant under all event
operators (Theorem 4.3); the number of states equals the number of generators of such a cone in an
observable extension (restricted: in V_min), and the explicit stochastic matrices are the
coefficient matrices B_{a,z} (Theorem 4.1).
(B) [lawfulness]  Any such realization has the legality pattern of K (Prop. 8.1), transports every
legal public-history adaptive policy with identical closed-loop joint laws and source posteriors
(Theorem 8.2), and never promotes an unavailable action.
(C) [obstruction witnesses]  Each of the following certifies that no carrier of a proposed size m
exists: a fooling set of size > m in any finite block of H (including ⊥-columns); a peripheral
eigenvalue of some T_w whose ratio to ρ(T_w) is a root of unity of order > m (or not a root of
unity: then no finite carrier); more than 2^m − 1 distinct legal menus; a failed availability
square for a proposed quotient.
(D) [falsity of the naive boxed equivalence]  "positive carrier of the legal-word behavior ⇒ lawful
realization" is REFUTED by Prop. 8.3; "linear dimension = positive dimension" is REFUTED by PW₁
(3 vs 4), by C_k (1+φ(k) vs k) and by the rational clock (3 vs ∞); "finite experiment table ⇒
Hankel rank" is not used anywhere; "real realizability ⇒ rational realizability" is REFUTED by
Prop. 4.5(b).

## 10. The carrier realization oracle

`carrier_realization_oracle(system, proposed_dimension, hankel_rows, hankel_cols, obstruction_words,
cone_depth, cone_budget)` returns one of:

* **LAWFUL_REALIZATION** — an explicit positive carrier (B_{a,z}, λ_σ) from a verified cone
  (Theorem 4.1), plus an exact equivalence certificate (Prop. 4.6) between the input and the carrier
  on *all* bottom-completed words (Tzeng-type closure, no horizon assumption).  With the input's
  enabled sets, the legality pattern is transported by Prop. 8.1.
* **FINITE_OBSTRUCTION** — a rigorous lower bound exceeding the proposed dimension: fooling set on a
  declared Hankel block (support), or a peripheral-spectrum witness (order k > m, or d⁺ = ∞).
* **MORE_EXPERIMENTS_REQUIRED** — produced by `distinguishing_experiment(c₁, c₂)`: two candidate
  models consistent with the same finite data are separated by an explicit (source, word) with
  both probabilities, flagged with whether that word is legal in the first model.  The oracle never
  asserts that the preparation σ is physically available; it is a declared mathematical datum.  In
  the availability square the only distinguishing word (b·ok from the mixed source) is *illegal* in
  FINE: the two models are legally indistinguishable by probabilities and differ only in the menu law.
* **UNRESOLVED** — cone-search budget or decidable-cofactor horizon exhausted.  Never emitted as
  "impossible".

**Proposition 10.1 (soundness; PROVED LOCAL).**  Every LAWFUL_REALIZATION verdict is accompanied by a
carrier whose complete behavior equals the input's (exact certificate); every FINITE_OBSTRUCTION
verdict is accompanied by a witness satisfying the hypotheses of Prop. 2.1's argument or Theorem 6.1,
each of which is a theorem about *all* carriers of the behavior; UNRESOLVED carries no claim.

**Counterexample-guided refinement.**  `reachable_cone_refinement` starts from normalized reachable
rays up to a depth, adds every image T g that escapes the current cone (an exact LP failure is the
counterexample), prunes nonnegatively redundant generators, and re-verifies.  Every added generator is
reachable, so the search explores R̄ only; it finds a carrier iff finitely many reachable rays generate
an invariant cone (true for PW₁ in one round and for C_k's orbit cones), and it correctly stalls on
the rational clock.  **Which repairs are representation changes and which need new instrumentation:**
enlarging the cone (more generators, same V_min), passing to an observable extension W, and
bottom-completing availability are representation changes — no new sensor, no new action.  Making an
illegal distinguishing word legal (e.g. enabling b on the mixed support), or adding a reset, changes
the instrument set and is *not* something the oracle may do; it reports the word and stops.

**Connection to existing machinery.**  EODCS/Nerode: `minimal_stationary_repair` (PR #53) is the
*partition* (strong-lumpability) closure; the cone theorem is its *linear-positive* generalization
(a lumpable partition is the special case of an invariant cone generated by block indicator vectors);
CAR-3's "necessary for all Dirac preparations" is the statement that the Dirac generators must lie in
the cone.  E40/CT10 `carrier_hankel_bounds`: the scalar LTI Hankel minor bound is the one-action,
one-outcome, one-source case of D3; `hankel_block` + `rank` generalize it to words and sources, and
`fooling_set_lower_bound` adds the positive bound the scalar module lacks.  Genetic representation
synthesis: candidate generators can be bred, but acceptance is only by exact LP (`verify_cone`).

## 11. Formal status

| Statement | Where | Status |
|---|---|---|
| rank₊(P) ≥ 4 via the fooling set, over nonnegative integer factorizations of the support pattern | `EODCS_PositiveCarrier.lean: calibration_fooling_bound` | LEAN-KERNEL VERIFIED (Lean 4.14.0, no mathlib, no `sorry`/`axiom`; mutation controls fail) |
| (3+4i)ⁿ has imaginary part ≡ 4 (mod 5), n ≥ 1; the rotation (3+4i)/5 has infinite order | `gpow_mod5`, `gaussian_rotation_never_real`, `rotation_power_not_identity` | LEAN-KERNEL VERIFIED |
| closed-loop policy laws and posterior numerators are functions of the legal behavior | `closed_loop_law_transport`, `posterior_data_transport` | LEAN-KERNEL VERIFIED (skeleton; the chain-rule body is paper, Theorem 8.2) |
| rational ⇒ integer factorization transfer; fooling sets multiplicative under ⊗ | §2, §7.1 | PROVED LOCAL |
| Theorems 4.1–4.3, 5.1, 6.1, 7.1–7.3, 8.1–8.5, Lemma 7.4 | this dossier + receipt | PROVED LOCAL / TESTED (finite exact checks) |
| Theorem 4.1 in Lean | — | LEAN-READY PLAN (below) |

**Lean-ready plan for Theorem 4.1 (not claimed verified).**  In the mathlib lane
(`formal/swarm_topology`, Lean 4.14 + pinned mathlib): state over `Matrix (Fin n) (Fin n) ℚ` with
`Fin m → Fin n → ℚ` generators `G`, hypotheses `hB : ∀ a z, T a z * G = G * B a z`, `hBnn : ∀ a z i j, 0 ≤ B a z i j`,
`hN : ∀ i, τ ⬝ᵥ G i = 1`, `hM : ∀ a i, τ ⬝ᵥ (∑ z, T a z) *ᵥ G i = 1`; prove `word_intertwine : T_w * G = G * B_w`
by `List.foldr` induction (this is the same shape as `all_finite_carrier_reports_transport`),
`behavior_eq : τ ⬝ᵥ (T_w *ᵥ G λ) = ∑ j, (B_w *ᵥ λ) j` from `hN`, and `column_stochastic` from `hN`,`hM`.
No part needs reals; a separate `Fin m`-pigeonhole-free statement is not needed since m is explicit.
Estimated size: ~120 lines; the only nontrivial lemma is the finite sum manipulation.

## 12. Prior-art crucible and novelty verdict

**Classical foundations (not claimed).**
* Linear/OOM/PSR/multiplicity-automaton minimal realization and Hankel rank: Carlyle–Paz 1971, Fliess 1974,
  Jaeger 2000, Singh–James–Rudary 2004 (PSR, arXiv:1207.4167), Thon–Jaeger 2015 (JMLR 16): Prop. 3.1.
* Invariant polyhedral cone criterion: Heller 1965 (Ann. Math. Stat. 36) for functions of finite Markov
  chains; restated with string functions as Theorem 5.1 of Schönhuth, "Equations for hidden Markov
  models" (arXiv:0901.3749), whose Corollary 5.2 is the uncontrolled form of Theorem 5.1 here; Ohta–Maeda–
  Kodama 1984 / Benvenuti–Farina 2004 (Kybernetika 39) Theorem 1 for SISO positive linear systems
  (cone K with FK ⊆ K, K ⊆ observability cone, g ∈ K; "number of edges = positive dimension").
  Vidyasagar 2011 (Math. Control Signals Systems) surveys quasi-realization vs realization;
  Huang–Ge–Kakade–Dahleh 2014 (arXiv:1411.3698) and Ohta 2020 (arXiv:2008.11487) treat minimal HMM
  realization via tensor decomposition under genericity assumptions — orthogonal to the cone
  criterion, which is exact and assumption-free but not an algorithm.
* Nonnegative rank vs rank and fooling sets: Cohen–Rothblum 1993; Yannakakis 1991; Dietzfelbinger et al.
  1996; Gillis–Glineur 2012 (restricted rank, nested polytopes); Fiorini–Rothvoß–Tiwary 2012
  (extension complexity).  Multiplicativity of fooling sets under Kronecker products is folklore.
* Irrational rotations have no finite HMM: Fox–Rubin 1968; Dharmadhikari 1963; Jaeger's probability
  clock (2000; addendum at rug.nl with rational starting vector but irrational angle φ = 1).
  Peripheral-spectrum obstruction for positive linear systems: Anderson–Deistler–Farina–Benvenuti 1996;
  Benvenuti–Farina 2004 Example 1 (angles π/2^q; gap exponential in q) is the SISO ancestor of C_{2^{q+1}}.
* Rationality: Chistikov–Kiefer–Marušič–Shirmohammadi–Worrell, "Nonnegative matrix factorization requires
  irrationality" (SIAM J. Appl. Algebra Geom. 2017; ICALP 2016 restricted version): rank₊ over ℝ is 5,
  over ℚ is 6 for a 6×11 rational matrix; computability over ℚ open.
* Taghavian–Sjölund 2025 (arXiv:2502.21102): LP for minimal positive *Markov-form* realizations of SISO
  transfer functions; it records that dominant poles at irrational angles exclude positive realizations
  and gives N = ∏ m_k constructions for rational angles — the SISO cousin of Theorem 7.3's upper bound.

**Newly proved SUCC specializations (PROVED LOCAL unless marked).**
1. The exact controlled, source-indexed, bottom-completed cone theorem with the normalization (M)
   *derived* and pointedness/convexity automatic (Thms 4.1–4.3), with the restricted/unrestricted
   distinction made explicit at the process level (Prop. 4.4, Lemma 7.4).
2. Theorem 6.1 in quantitative word-indexed form for controlled behaviors with the sub-quotient and
   mass-growth argument written out, and its exact finite certificate (Cor. 6.2) without floating point.
3. The cyclotomic clock family: r = 1 + φ(k), d⁺ = k exactly, Hankel strictly positive (support-blind gap).
4. PWₙ with a silent non-commuting intervention: r = 3ⁿ, d⁺ = 4ⁿ, single-source lower bound.
5. The rational clock with the mod-5 certificate (Lean) — a fully rational instance of the Fox–Rubin /
   Jaeger phenomenon.
6. Availability theory: bottom completion, Prop. 8.1, Theorem 8.2, the minimal failed square 8.3, the
   menu-count bound 8.4, the repair statement 8.5; Theorem 9.1(B),(D).
7. Lemma 7.4 (one-shot embedding: d⁺ = rank₊ + 1), transferring CKMSW's ℚ/ℝ gap and Gillis–Glineur's
   restricted gap to behaviors.
8. Three kernel-checked cores (§11).

**Potential scholarly contributions (modest, to be checked against the PSR/POMDP literature before
any claim).**  (a) Realization theory *with partial action availability*: the legality pattern as part of
the behavior, the ⊥-completion, and the "menu is not a sensor" transport theorem.  I am not aware of
a treatment of action menus in OOM/PSR realization; POMDP literature assumes total actions.
(b) The exact value d⁺(C_k) = k for the stochastic (sub-stochastic, reset-equipped) clocks with the
matching orbit carrier; the SISO analogue is known in spirit (Benvenuti–Farina Example 1), so this is a
transfer, not a discovery.  (c) The observation that support and spectral certificates are mutually
blind (PWₙ vs C_k) is a useful organizing fact for oracles; probably folklore.

**Unresolved (UNVERIFIED / CONJECTURE).**  d⁺ vs d⁺_res strictness for a *recurrent* process (one-shot
transfer only); the ℚ/ℝ question at r = 2 (Remark 5.2); d⁺_law < d⁺_⊥ possibility (Prop. 8.5); for
r = 3, which values of d⁺ occur beyond {3,4,6,∞} with rational data (Benvenuti–Farina Example 5 suggests
every N ≥ 4 with real poles); decidability of d⁺ < ∞.

## 13. Integration map (reusable interfaces, no monolith)

* PR #53 `carrier_indexed.py`: `CarrierInstrument.rows` (joint atoms (z, next, p)) ↔ `PositiveCarrier.events`
  (a ↦ z ↦ M_{a,z} with M[next][current] = p); `enabled` ↔ `enabled`; `Carrier.preparation` rows ↔
  `preparations`; `ActualHistory.mass` J_h ↔ `PositiveCarrier.law(σ, w)`; `audit_descent` (lumpability)
  is the partition special case of `verify_cone` with indicator generators; `repair_one_step`/
  `minimal_stationary_repair` ↔ Prop. 8.5; `decide_original` ↔ `source_posterior` + Theorem 8.2.
  A thin adapter (`CarrierInstrument` → event matrices) is one function and is left to the integration
  PR to avoid touching PR #53 files here.
* EODCS (`EODCS_CarrierIndexed.lean`): `all_finite_carrier_reports_transport` is the deterministic
  intertwining; Theorem 4.1's `T_w G = G B_w` has the same induction shape (Lean plan, §11).
* F48 (`swarm_lawful_history.py`): `quotient_source` checks availability/outcome/update descent; the
  bottom completion makes availability a behavior coordinate so that F48's deterministic quotient theorem
  is the deterministic special case of Prop. 8.1 + Theorem 8.2.
* E40/CT10 (`carrier_hankel_bounds.py`): `hankel_dimension_receipt` → `hankel_block`/`rank` (word- and
  source-indexed) and `fooling_set_lower_bound` (positive); the receipt convention
  (`global_upper_bound_proved: False` for finite tables) is kept: upper bounds come only from realizations.
* C17 (`swarm_probability.py`): `StochasticInstrument` rows (label, after, p) map to event matrices as
  for PR #53; `find_garbling` (Blackwell) is an LP of the same exact kind as `cone_coordinates`.
* A06 (`Swarm_Repair.lean` coreflection): cone enlargement is the positive analogue of the stable-
  refinement interior operator; not formalized here.
* CI: `eodcs-tests.yml` reproduces `POSITIVE_CARRIER_RECEIPT.json` byte-for-byte; `eodcs-lean.yml` compiles
  `formal/EODCS_PositiveCarrier.lean` under the existing lexical gate.  The 4.19 EOS lane is untouched.

## 14. The most consequential remaining obstruction, and the next lemma

The oracle's blind spot is the region "finite d⁺ but R̄ not finitely generated by reachable rays":
a polyhedral invariant K strictly between R̄ and P may exist while every finite set of reachable rays
fails invariance.  There the oracle says UNRESOLVED, and no present certificate can say "finite" or
"infinite".  The sharpest finite case is r = 3, where (Gillis–Glineur) the restricted problem is a
planar nested-polygon problem and polynomial-time *statically*; what is missing is the *dynamic*
version: a polygon T with R̄-slice ⊆ T ⊆ P-slice such that the projective maps induced by every T_{a,z}
send T into T.

**Next experiment (concrete, exact, one afternoon).**  For r = 3 and a dominant real eigenvalue of every
T_{a,z} (so that P's slice is a compact polygon computable as the intersection of finitely many
half-planes τT_w ≥ 0 up to a provable depth — the depth bound is the first lemma to prove), enumerate
candidate invariant polygons with vertices on ∂P (an invariant minimal polygon can be pushed to the
boundary) and decide invariance by exact LP.  Run it on a non-symmetric rank-3 cousin of C₄ obtained by
replacing Rot₉₀ with a rational matrix of infinite order and eigenvalues of modulus < ½ (contractive
rotation): Theorem 6.1 is silent there, R̄ is non-polyhedral, and the question "finite or not" is exactly
the one the present oracle cannot answer.  A finite answer would give the first (3, k) example with
k ≥ 5 and rational data; an infinite answer would need a new obstruction beyond spectrum and support —
which is the theorem worth having next.
