# Gaussian-moat / entropy branch — swarm audit (2026-10-12)

**Status of this document:** an auditable record of a multi-bearing adversarial
audit and open-problem scouting pass over the (unmerged) research branch
`research/gaussian-moat-certificate-duality-2026-10-12`. It establishes no new
mathematics beyond the ledger entries it cites; the canonical per-claim status is
[docs/CLAIM_LEDGER.md](CLAIM_LEDGER.md). This audit and its corrections were consolidated into `main` on 2026-10-12 together
with the moat/entropy and source-relative-coverage work; the audit's result claims
were renumbered **O262–O268** to compose with the coverage claims O251–O261.

## 1. What was run

After the 2026-10-11 research-stack consolidation
([docs/INTEGRATION_AUDIT_2026-10-11.md](INTEGRATION_AUDIT_2026-10-11.md)), nine
independent read-only / scratch-only bearings were run against the new moat/entropy
branch and against the open question "what would promote this work from a clean
certificate exercise toward verified, novel mathematics." Each bearing was caged
(no repo mutation, no `main`, truth-status labels, receipts, kills reported as
kills) and every load-bearing numeric claim was re-verified by the orchestrator.

| Bearing | Target | Outcome |
| --- | --- | --- |
| external-anchor audit | O236 (OpenAI moat theorem) | real artifact, **unrefereed**; relabelled EXTERNAL CLAIM |
| novelty + proof audit | O237 dichotomy | valid proof; **classical** voltage-graph theorem |
| entropy adversary | T1–T5 (O245–O249) | standard info theory, honestly labelled, nothing broke |
| 104-bound recompute | O242 | **independently reproduced** (36,864 / 71 / 104) |
| existence moonshot | O250 | **KILL** (route circular); produced Theorem R + the DR family |
| open-problem scout | new targets | all metaphor/solved except the Eisenstein port |
| 2D-Jacobsthal | g(z) sequence | computed; produced **Theorem A** + a growth conjecture |
| Eisenstein port ledger | O236 portability | ports clerically; already a corollary of Kitamura 2026-10-10 |
| coverage-organ spec | a "proving" tool | **vaporware**, with a precise Σ₁/Π₂ reason |

## 2. Verified shards (re-checked by the orchestrator)

- **O242, the 104-vertex bound.** An independent clean-room BFS reproduced
  36,864 surviving residues, maximum sieve component 71, and maximum enlarged
  component 104 — agreeing with the branch probe, the branch's own direct-lattice
  audit, and the 19 periodic tests. Modest but exact; rests on the classical norm
  classification (O240) and survives even if the O236 anchor is wrong.
- **O264, Theorem A (Gaussian 2-halving): `K*(P∪{2}) = 2·K*(P)` for odd `P`.** A
  genuine new small theorem. The odd points are the coset `1+(1+i)Z[i]`, every edge
  is `s=(1+i)t`, and the similarity `w↦(1+i)w` makes `A(P∪{2})` at bound `K`
  isomorphic to `A(P)` at bound `⌊K/2⌋`. Orchestrator-verified numerically
  (`A({5,13})@1` and `A({2,5,13})@2` both have max component 580) and by hand.
- **O262, Theorem R.** An exact, sieve-free and torus-free reformulation of the
  component bound (residue-surjectivity of large connected sets under split
  characters), which isolates the entire open content as **Lemma L(K)**.
- **O263, the divisor-ruler family.** A genuinely new infinite family of step
  alphabets with an explicit certificate constructor and proved modulus — but
  degenerate (a 2D CRT ruler); it does not illuminate the fixed-small-K moat.
- **O266, the 2D-Jacobsthal data.** `g(z)` computed exactly for `z ≤ 17` in both
  the Gaussian and Eisenstein lattices (sequences absent from OEIS), with a
  CONJECTURED `g(z) ≍ log z` growth law (Vardi-consistent; honest counter-evidence
  recorded).

## 3. Kills (honest, with receipts)

- **O250 moonshot — REFUTED as a route.** Building an integrating potential for
  arbitrary alphabets is *circular* with O237/P1 (the potential exists iff the thing
  to be proved holds). P1–P3 give no induction on the step bound. The holonomy does
  **not** factor over primes (counterexample: `K*({5})=K*({13})=K*({17})=1` but
  `K*({5,13})=2` while `K*({5,17})=1`), so no per-prime closed form exists.
- **Entropy track (T1–T5).** All standard information theory (total correlation,
  the MI chain rule, data-processing-with-equality, Csiszár–Körner / Alhejji–Smith
  continuity). Nothing broke under an independent engine; the mod-5 `2H(U)`
  counterexample is real. The only new-to-project content is one proof-plumbing
  simplification. Zero novelty inflation — the labels are accurate.
- **Scouting.** Crystal-net dimensionality and periodic-graph homology are already
  solved (Systre/CrystalNets.jl; Onus–Robins). Lonely Runner and covering systems
  are **metaphor, not functor** (no component/cocycle question survives).
- **The coverage-lower-bound "organ" — vaporware.** See §4.

## 4. Capstone: the Σ₁/Π₂ reach characterization (O267)

Three bearings converged on one precise statement of what this program can and
cannot do. SUCC's validated voltage-graph tool is a **decision procedure**: it
settles every *fixed* instance by running it, so it decides **Σ₁** instance-facts
("this `(P,K)` confines", witnessed by a potential or a nonzero-holonomy word). The
open problem is the **Π₂** universal closure ("for all `D` a confining sieve
exists"). **No finite certificate witnesses a Π₂ statement** — that requires a total
computable `K↦X(K)` plus a proof of its correctness, i.e. a proof assistant with a
domain library (which is exactly what OpenAI's Lean development is). The gap between
the Σ₁ tool and the Π₂ theorem is precisely the externally supplied
arithmetic/analytic coverage content. This is the framework's honest epistemic
boundary, and it is the sharpest result of the operation: SUCC is a
**verifier / certificate / porting layer**, not a theorem-prover.

## 5. External anchor and corrections applied

- **O236 relabelled** EXTERNAL THEOREM → **EXTERNAL CLAIM (unrefereed)**. The OpenAI
  manuscript is real (eight source hashes match; the Lean endpoint `fullMain` is a
  faithful statement with no `sorry`/`axiom`), but it is unrefereed, AI-generated,
  and its Lean kernel check has not been independently rerun. erdosproblems.com
  lists zero proof claims; Wikipedia still lists the moat problem as unsolved.
- **Kitamura's 2026-10-10 generalization** corroborates *portability* (it covers
  every irreducible binary form; `F=X²−XY+Y², r=1` is Eisenstein) but **shares the
  same AI provenance** — common-mode, not independent confirmation of correctness.
- **O237 attributed** to the classical voltage-graph component theorem
  (Cohen–Megiddo 1990; Bass 1993 Thm 3.6; Dicks–Dunwoody Cor 1.9.3; Gross–Tucker).
  SUCC's contribution there is the certificate interface, not the theorem.
- The dossier's own framing was found **already careful** (it explicitly disclaims
  Yoneda, observer models, and "abstract holonomy" implications); no prose edit was
  needed. The hollow abelian-cocycle↔O200 tie-in existed only in orchestrator
  discussion, not in the research note.
- **Firewall re-confirmed:** no PROVED LOCAL / CLASSICAL claim depends on O236; only
  O243's totality clause does, and it is labelled conditional everywhere.

## 6. What SUCC currently is (honest status)

- **Proves / computes (exact):** the certificate dichotomy (classical), the 104
  bound (O242), Theorem A (O264), Theorem R (O262), the divisor-ruler family (O263),
  and the `g(z)` data (O266).
- **Models / assembles:** the entropy transport layer (standard info theory, one
  genuine proof simplification).
- **Conjectural:** `g(z) ≍ log z` (O266); the small-prime inert-irrelevance and
  pair/triple rules.
- **Out of reach, by O267:** the all-`D` moat theorem (Π₂) and anything equivalent
  to it (`g(z)→∞`). SUCC imports it; it does not and cannot re-prove it with
  certificates alone.
- **The honest contribution is the framing/recipe:** an observational
  certificate-and-audit layer that emits independently checkable finite witnesses
  for, and ports, a landmark result — valuable precisely because that landmark is an
  unrefereed, non-explicit, machine-generated proof.

## 7. Next experiments (ranked)

1. **Proof-mine an explicit `D↦P(D)`** from OpenAI's "sufficiently large" constants,
   calibrated against the `g(z)` data (O266). This is the only route to an explicit
   bound; feasibility unknown.
2. **DCO-3: exact Shannon-cone (Farkas) certificates** for the T1/T3/T5 chain-rule
   skeleton (prior art ITIP/PSITIP), upgrading the entropy module's float
   diagnostics to machine-checkable exact certificates and discharging AGENTS.md
   rule 8 for that layer. Cheap, buildable, honest hygiene.
3. **Explicit Eisenstein certificates** via a norm-form-agnostic sieve adapter
   (use the ramified prime 3, density 1/3); SUCC does the certificate-and-audit half
   only — the theorem half is Kitamura's / OpenAI's and is non-explicit.
4. **Extend the `g(z)` sequence** past the `Q ≈ 3·10⁴` exhaustive wall (the search is
   the bottleneck, not the mathematics) and settle the growth constant.

## 8. Provenance and boundary

- All results are computational (Python/C, local Python 3.12). No Lean was rebuilt.
- OpenAI and Kitamura are both unrefereed AI-generated work with shared provenance;
  treat cross-references between them as common-mode.
- The engine behind O266 was cross-checked against the branch's `analyze_periodic` /
  `verify_confinement` / `verify_translation` on 546 cases (0 mismatches) with 135
  independently replayed escape witnesses; large-`Q` confinement rests on that
  single engine.
- `provenance/` and the archived originals were not touched. This audit is additive and
  was folded into `main` via the 2026-10-12 consolidation merge (`--no-ff`), after full validation.
