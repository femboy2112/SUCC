# Minimum-cost global obstruction repair for F₂ parity transport

**Date:** 2026-10-19
**Status:** exact finite classical-optimization theorem + replayable certificates. This is **not** a claim of a new complexity-theory result, a physical experiment on an observer, or any progress on RH.
**Research parent:** `origin/main` at `455600a2e013895c36238a3a97e0f470fd7ba197`; non-main research branch `research/amv-moonshot-b-maxcut-repair-2026-10-19`.
**Extends:** round #188, `observational_succ/meta_choice_descent.py` and `research/2026-10-19/SUCC_META_GENERATIVE_CHOICE_DESCENT.md` §10 ("compute **minimum repair costs** to make an obstructed local system globally representable while preserving the original carrier laws").
**Named claim family:** **PR (Parity Repair).** The exact cost of lawfully repairing an F₂ descent obstruction equals a weighted Max-2-LIN optimum, and in the all-flip unit-weight case equals `|E| − MaxCut(G)`.

## 0. Object, probe, gap

#188 settled the **decision** question: does a finite F₂ parity-transport system admit a global section? The obstruction is a nonzero class `[t] ∈ H¹(G; F₂)`, witnessed by an odd closed walk. This round settles the **optimization** question one layer down: when `[t] ≠ 0`, what is the *minimum lawful cost* to make the system globally representable, and what classical object is that cost? The gap #188 left open is the quantitative one — an obstruction is either present or absent there; here it is *priced*.

## 1. Definitions, hypotheses, quantifiers

**Domain.** A finite undirected (multi)graph `G = (V, E)`, viewed as in #188 as a 1-dimensional CW complex. Parallel edges and self-loops are permitted. Let `n = |V|`, `m = |E|`.

**Data.** For each edge `e = (u, v)`:
- a **target** `t_e ∈ F₂` (the declared source transport parity — identical to `ParityEdge.parity` in #188);
- a **repair cost / weight** `w_e ≥ 0`, an exact `int` or `Fraction` (never a float).

**Variable.** A vertex assignment `x : V → F₂`.

**Cost functional.**
$$ C(x) \;=\; \sum_{e=(u,v)\in E} w_e \cdot \mathbf 1[\,x_u \oplus x_v \neq t_e\,], \qquad C_* \;=\; \min_{x:V\to\mathbb F_2} C(x). $$

**Quantifiers.** `C_*` is a minimum over the finite set `F₂^V` (`2^n` assignments). It is gauge-invariant under flipping all vertices of any connected component, so the gauge-fixed enumeration over `2^{n-1}` assignments (`x_{v₀}=0`) is complete. Every statement below is `∀ (G, t, w)` within this finite grammar unless a family (forest / bipartite) is named.

## 2. Exact relation to weighted parity (Max-2-LIN over F₂)

Each edge is a two-variable F₂ linear equation `x_u ⊕ x_v = t_e`; `C(x)` is the total weight of *violated* equations. With `W = Σ_e w_e` the total weight and
$$ \mathrm{MaxSAT} \;=\; \max_x \sum_{e} w_e\,\mathbf 1[\,x_u\oplus x_v = t_e\,] $$
the weighted Max-2-LIN(2) optimum:

**Proposition PR-1 (exact complementarity).** `C_* = W − MaxSAT`.
*Proof.* For every `x`, satisfied-weight + violated-weight `= W`; minimize the second iff maximize the first. ∎ **Status: CLASSICAL / PROVED ELEMENTARY.**

## 3. ALL-FLIP unit weight: `C_* = |E| − MaxCut(G)`

**Theorem PR-2.** If every `t_e = 1` (ALL-FLIP) and every `w_e = 1` (UNIT-WEIGHT), then
$$ \boxed{\,C_* \;=\; |E| \;-\; \mathrm{MaxCut}(G)\,}. $$
*Proof.* With `t_e = 1`, a unit edge `e = (u,v)` is satisfied iff `x_u ⊕ x_v = 1` iff `x_u ≠ x_v` iff `e` is cut by the partition `(x^{-1}(0), x^{-1}(1))`. Hence `MaxSAT = max_x #\{\text{cut edges}\} = \mathrm{MaxCut}(G)`, and PR-1 gives `C_* = |E| − MaxCut(G)`. ∎ **Status: CLASSICAL / PROVED ELEMENTARY.**

Boundary tie to #188: `C_* = 0` iff `MaxCut = |E|` iff `G` is bipartite iff the all-flip transport has an F₂ section iff `[t]=0 ∈ H¹`. The odd triangle gives `|E|=3`, `MaxCut=2`, `C_*=1` (one edge must stay frustrated — the #188 odd-loop obstruction, now priced at 1). Verified for the triangle and for **all 31 connected graphs on ≤5 vertices** (`verify_maxcut_identity`; §6).

## 4. Signed-graph frustration and the Ising ground state (exact)

**Signed graph.** Put `σ_e = (−1)^{t_e} ∈ {+1,−1}`. An assignment `x` satisfies edge `e` exactly when it respects `σ_e` in Harary's sense (a `+` edge wants equal endpoints, a `−` edge wants unequal). Therefore the unit-weight `C_*` is the **frustration index** (line index of balance) `L(G,σ)`, and the weighted `C_*` is the weighted frustration index. The signed graph is **balanced** (`L = 0`) iff a global F₂ section exists iff `[t]=0 ∈ H¹(G;F₂)`. The ALL-FLIP all-negative signed graph recovers Theorem PR-2: `L(G,-) = |E| − MaxCut`.

**Ising mapping.** Put spins `s_v = (−1)^{x_v} ∈ {+1,−1}` and couplings `J_e = w_e σ_e` (ferromagnetic when `t_e=0`, antiferromagnetic when `t_e=1`). For the Hamiltonian `H(s) = −Σ_e J_e s_u s_v`:

**Proposition PR-3.** For every `x` with spins `s`, `H(s) = 2C(x) − W`; hence the ground-state energy `E_min = 2C_* − W`.
*Proof.* `J_e s_u s_v = w_e(−1)^{t_e}(−1)^{x_u⊕x_v} = +w_e` on a satisfied edge, `−w_e` on a violated edge, so `Σ_e J_e s_u s_v = W − 2C(x)` and `H = −(W − 2C) = 2C − W`. ∎ **Status: CLASSICAL / PROVED ELEMENTARY.** Checked pointwise over all assignments (including `Fraction` couplings) and against an independent exhaustive Ising ground-state search in `tests/test_parity_repair_cost.py`.

## 5. Computational status — the CRITICAL nuance

Computing `C_*` for general `(G, t, w)` is **NP-hard**: it contains weighted Max-2-LIN over F₂, and by Theorem PR-2 it contains unweighted MaxCut, which is NP-hard (Karp 1972; the Max-2-LIN / frustration-index hardness is in Garey–Johnson–Stockmeyer 1976 and Barahona 1982 for Ising ground states).

**NP-hardness is NOT noncomputability.** `C_*` is a finite minimum over `2^n` assignments; a finite program (the exhaustive solver here) *always* returns the exact value. In the `FieldClass(Source, Target, Tools)` taxonomy of `docs/OBSERVER_PROOF_ACCESS.md`:

- `C_*` is a **SimpleField**: a verified finite program supplies the exact interface in finite time.
- `C_*` is **NOT** an **IdealHardField**. An IdealHardField requires a *proof that no computable selector exists* (e.g. the Kleene-tree calibration at `field_limit_trichotomy.py:124`). A merely slow — even super-polynomial — but finitely terminating computation never qualifies. "No polynomial algorithm is known (and, under P≠NP, none exists)" is a statement about *resource cost*, not about *computability*. Conflating the two would be a category error of exactly the kind AGENTS.md §5 forbids (finitary proof vs ω-rule; finite observation vs universal proof).

This is the load-bearing SUCC distinction this round contributes: **the inferential path from local construction to global representability has a well-defined finite cost `C_*`, whose hardness is a complexity fact, not an inaccessibility or impossibility fact.**

## 6. Cheap exact families vs. general hardness

| Family | Cheap exact? | Why | Here |
|---|---|---|---|
| Forest / tree | **Yes**, `C_* = 0` for any `t` | acyclic ⇒ no closed walk ⇒ section always exists (#188 spanning-forest propagation) | implemented: `forest_repair_cost` |
| Bipartite | **Yes** for ALL-FLIP: `MaxCut = |E|`, so `C_* = 0` | bipartition cuts every edge | implemented: `bipartite_max_cut` |
| Planar | **Yes** (weighted MaxCut / frustration) | T-join / Chinese-postman matching in the dual: Hadlock 1975; Orlova–Dorfman 1972; Barahona 1982 | **stated, not implemented** |
| General | **No** (NP-hard) | Max-2-LIN / MaxCut hardness (§5) | exhaustive `2^{n-1}` solver only |

Caveat recorded in code and tests: bipartite does **not** make *general*-`t` frustration cheap — an even cycle with an odd number of flips (e.g. C₄ with three flips) is frustrated. The cheap bipartite result is specifically about MaxCut / the all-flip case.

## 7. Replayable optimality certificates

`connected_graph_certificates(5)` enumerates one canonical representative (lexicographically least edge set over all `n!` relabelings) of every connected graph up to isomorphism on `1..5` vertices — **31 graphs** (per-`n`: 1, 1, 2, 6, 21), an independently known sequence (OEIS A001349). For each it stores, for ALL-FLIP UNIT-WEIGHT, the exact `|E|`, `MaxCut`, `C_*` (= frustration index), a lex-least optimal assignment, and the forest/bipartite flags, asserting `C_* = |E| − MaxCut` on every one. The frozen artifact is `research/2026-10-19/PARITY_REPAIR_CERTIFICATES.json`; `test_certificate_replay_bit_for_bit` regenerates it and asserts **byte-for-byte** equality, and the probe `scripts/parity_repair_cost_probe.py --write-certificates` reproduces it. All values are integers; no float, no randomness, hence deterministic.

## 8. Repair / probe / interface / illegal-source-law taxonomy

A SUCC observer facing `[t] ≠ 0` has four distinguishable moves. Only two are lawful; the firewall is that a *source law is never silently rewritten*.

| Move | Source laws `t_e` | Cost | Makes globally representable? | Lawful? | Code |
|---|---|---|---|---|---|
| **Observational probe** | unchanged | 0 | **No** — reveals the odd-loop witness / `[t]` class; a positive `C_*` is unchanged by looking | **Yes** (pure observation) | `probe_reveal_obstruction` |
| **Lawful model repair** | unchanged | `C_*` (the irreducible frustration index) | the residual is accepted and minimized | **Yes** | `lawful_model_repair` |
| **Interface / cover change** | unchanged on the original target | may expose a new accessible representation but must transport the *original* target (cf. #188 §4.1: a double cover trivializes lifted holonomy yet does **not** descend a section on the original triangle) | only if the original source can lawfully use the new interface | **Conditional** | (stated; #188 cover modules are the baseline) |
| **Illegal source-law alteration** | **flipped** (`t_e → 1−t_e`) | apparent 0 | by *cheating* | **NO** | `illegal_source_law_alteration` (flags `lawful_succ_repair=False`) |

The negative control (`test_probe_vs_repair_vs_illegal_source_law`): on the odd triangle, the probe pays 0 and reveals but does not fix (`C_*` stays 1); lawful repair pays `C_*=1` with targets intact; the illegal flip of one edge target reaches apparent cost 0 but has `source_targets_altered=True`, `lawful_succ_repair=False`, and its altered target vector differs from the original — the "cheap" cost is a lie, because under the *true* source law the cost is still 1. This is the pricing analogue of #188's MC-4 ("formal sheafification does not supply an original-source realizer") and the FuckedField/toolkit "new-tag probe repairs" calibration.

## 9. Negative controls: heuristics are strictly suboptimal (proved by exact min)

- **Single-flip local optimum (C₄, all-flip unit).** The "two-block" 2-coloring `x=(0,0,1,1)` has cost 2; **every** single-vertex flip stays at cost 2 (a strict local optimum), yet the global `C_* = 0` (the alternating coloring cuts all four edges). Certified by `single_flip_local_certificate`: all `n` neighbor costs recomputed exactly, and `C_*` by exhaustive min. **Status: REFUTED** (the claim "single-flip local search solves parity repair"), receipt: C₄ cost-2 strict local optimum vs exact 0.
- **Sequential greedy (K₄ minus an edge, all-flip unit).** Deterministic order-based greedy returns cost 2; the exact minimum is 1 (`|E|=5`, `MaxCut=4`). **Status: REFUTED** (the claim "sequential greedy is exact"), receipt: greedy 2 > exact 1.

These are not merely "heuristics can be bad" folklore; they are exact, replayable receipts that the only trustworthy value here is the exhaustive `C_*` (or a proven poly special case), consistent with AGENTS.md §8 (a finite numerical/heuristic output is not a certificate).

## 10. Steelman → crucible → verdict

| ID | Strong claim | Receipt / obstruction | Verdict |
|---|---|---|---|
| PR-1 | `C_*` equals total weight minus weighted Max-2-LIN optimum | satisfied+violated = `W` | **CLASSICAL / PROVED ELEMENTARY** |
| PR-2 | ALL-FLIP unit-weight `C_* = |E| − MaxCut(G)` | cut ⇔ satisfied unit flip; checked on all 31 graphs ≤5 vertices | **CLASSICAL / PROVED ELEMENTARY; finite tests green** |
| PR-3 | Ising `E_min = 2C_* − W`, couplings `J_e = w_eσ_e` | per-edge `J s s = ±w`; pointwise + exhaustive cross-check | **CLASSICAL / PROVED ELEMENTARY** |
| PR-BAL | balanced ⇔ `C_*=0` ⇔ #188 section exists ⇔ `[t]=0∈H¹` | cross-checked against `solve_parity_descent` | **CLASSICAL; verified against #188** |
| PR-HARD | general `C_*` is NP-hard but **computable (SimpleField), not IdealHard** | Karp/Barahona hardness; finite `2^n` min | **CLASSICAL hardness; NP-hardness ≠ noncomputability asserted and labeled** |
| PR-TREE | forests give `C_*=0`; bipartite ALL-FLIP gives `C_*=0`, both poly | spanning-forest propagation; `MaxCut=|E|` | **PROVED ELEMENTARY; poly special cases implemented** |
| PR-GREEDY | sequential greedy / single-flip local search solve parity repair | K₄−e greedy 2>1; C₄ strict local optimum 2>0 | **REFUTED (two exact receipts)** |
| PR-ILLEGAL | flipping a source target is a lawful zero-cost repair | altered target vector ≠ original; `lawful_succ_repair=False` | **REFUTED; not a lawful SUCC repair** |
| PR-RH | this pricing says anything about Weil positivity / RH | no signed source→Weil morphism, no Schur sign | **NOT ESTABLISHED; RH OPEN** |

No proof-status promotion from a finite test, an analogy, or a cross-model check is authorized.

## 11. Provenance

- **New files:** `observational_succ/parity_repair_cost.py`, `tests/test_parity_repair_cost.py`, `scripts/parity_repair_cost_probe.py`, `research/2026-10-19/PARITY_REPAIR_CERTIFICATES.json`, this document.
- **Imported, unmodified:** `observational_succ/meta_choice_descent.py` (#188) — `FiniteTransportGraph`, `ParityEdge`, `LoopObstruction`, `solve_parity_descent`, `verify_loop` are reused for the forest/bipartite detectors and the obstruction probe. No archival/frozen file is touched; YEAN is not touched.
- **Classical references (not claimed new here):** R. Karp, *Reducibility among combinatorial problems* (1972, MaxCut NP-hard); F. Barahona, *On the computational complexity of Ising spin glass models*, J. Phys. A **15** (1982) 3241 (planar poly, general NP-hard); F. Harary, *On the notion of balance of a signed graph*, Michigan Math. J. **2** (1953); F. Hadlock, *Finding a maximum cut of a planar graph in polynomial time*, SIAM J. Comput. **4** (1975); Garey–Johnson–Stockmeyer (1976). OEIS A001349 (connected graphs: 1,1,2,6,21 on 1..5 vertices).
- **Attribution boundary:** the SUCC framing (lawful source-preserving repair, the probe/repair/illegal taxonomy, the NP-hard≠IdealHard firewall) is the author's program; Max-2-LIN, MaxCut, frustration index, and the Ising dictionary are classical. The exact finite implementation and certificates are new to this repository round, not a novelty claim.

## 12. Open obligation (next falsification opportunity)

1. **Planar poly, implemented.** Implement the dual T-join / blossom-matching solver for planar weighted frustration and certify it against the exhaustive solver on a documented planar family; the next falsifier is a planar instance where the matching solver and brute force disagree.
2. **Approximation boundary.** State and test the Goemans–Williamson 0.878 SDP bound as an *upper-bound certificate on `MaxSAT`* (hence a lower bound on `C_*`) — but only with a rigorous rational/interval SDP, never a float (AGENTS.md §8); a float SDP value is explicitly not a certificate.
3. **Interface-repair theorem.** Formalize the "cover change transports the original target" condition so that an interface move is provably lawful iff the original source can realize the new chart (the #188 §4.1 double-cover caveat), with a two-source observationally-identical counterexample as the falsifier.
4. **Firewall:** nothing here touches RH / Weil / Schur positivity; `RH_proved=False` is asserted at every return site. **RH remains OPEN.**
