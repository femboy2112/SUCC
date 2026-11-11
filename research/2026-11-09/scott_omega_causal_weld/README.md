# SUCC × Scott × Ω — Causal Weld / Computational Descent

**Historical initial-round scope:** additive-file statements and validation counts
below describe the original causal-weld submission, not the complete current
branch. Later DeepSeek additions are audited and repaired in the
[Cayley follow-up](../cayley_source_observer/README.md); its
[validation record](../cayley_source_observer/VALIDATION.md) owns current execution
status. No inherited count is promoted to a fresh run.

**Research branch; additive to verified Main XXII `43886e830cee5ff6d6b37719e18d809819673bd9`.** No main merge, release, alteration of frozen source/provenance/Lean. **π normality, original-zero hexadecimal parity balance, and RH remain OPEN.**

## Research thesis

- **SUCC** supplies source-indexed data, realized events, arithmetic transitions and marked seed.
- **Generalized Ω/λ calculus** supplies operational *syntax* for inexhaustible, indexed reductions. Raw Ωₖ is not normally terminating; its leftmost expansion adds exactly `k−2` copies per step. That numerical growth does **not** supply `k−2` independent dimensions without an explicitly sound compiler.
- **C-monoid** supplies internal pairing/application/abstraction. A literal nontrivial one-object CCC is impossible; the **Karoubi envelope of a genuine C-monoid** is CCC (Scott/Lambek). Our affine/finite prototypes do not themselves form C-monoids.
- **Causal categorical paths and higher cells** record source-attested maps, commuting squares/cubes, rewriting witnesses and provenance; diagrams alone do not create nontrivial higher morphisms.
- **Scott domains** order partial information. Scott-continuous observation preserves directed completion, and separately checked equality of completed images licenses **relative observational equivalence even without finite-stage equality**.
- **Pinbeds / sheet and volume gluing** arise from currying, products and fiber products under explicit compatibility. Geometric circle gluing is quotienting `R/Z` with integral winding retained separately. Global dimension is not inferred from the increment count in Ωₖ.

The claim is not that Scott semantics proves arbitrary two computations equal, or that completion solves the original signed cancellation. It is that we can **construct** the graph, evaluator, source-preserving observer and a certificate of equality in a declared observational completion. A nontrivial exact instance is derived here; the all-source faithful higher compiler is open.

## New exact source-weld theorem (this round)

For the genuine original four signed BBP poles, `U_0=0`, let `P_L=Σ_{j=1}^L 16^{-j}r(j)` and `T_n^(L)=Σ_{j=n+1}^L16^{n-j}r(j)` for `0≤n≤L`. Then **at every finite `L`**:

`U_n + T_n^(L) = 16^n P_L`, and `[16^nP_L,16^n(P_L+B_L)]` with `B_L=4/(15(L+1)^2·16^L)` are nested nonempty rational compact intervals converging to the true completed real orbit `16^(n−1)π`. The whole finite `n→n+1` square commutes **exactly**, not merely approximately; the quotient to `R/Z` and directed-limit observation commute by Scott continuity. This gives a certified finite-to-analytic weld carrying the **original** rational source, with a paid Fourier phase approximation bound. It does not establish cancellation of the finite rational phases. Full proof, including strict nesting and its polynomial certificate, in [THEOREMS](THEOREMS.md).

## What is in this branch

| Artifact | Responsibility |
|---|---|
| [SESSION_INDEX.md](SESSION_INDEX.md) | Chronological reconstruction of all user-originated ideas and their receipts |
| [THEOREMS.md](THEOREMS.md) | New exact BBP/Scott weld, C-monoid and Ω firewalls, nontrivial limits and counterexamples |
| [CONNECTION_ATLAS.md](CONNECTION_ATLAS.md) | Connect existing Main XXII mathematics by actual interfaces, not by buzzwords |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Proof/observed/open/refuted classification and next discriminators |
| [SOURCE_MAP.md](SOURCE_MAP.md) | Frozen source, repo lineage, classical provenance and signature boundaries |
| [NEXT.md](NEXT.md) | Typed modules, proof contracts, hostile tests, acceptance gates |
| [VALIDATION.md](VALIDATION.md) | Actual test scope; full native repo/Lean not falsely claimed |
| [DEEPSEEK_THEOREM_CAMPAIGN.md](DEEPSEEK_THEOREM_CAMPAIGN.md) | Exhaustive, surgical DeepSeek handoff |
| `session_archive/` | Byte-for-byte eight earlier local dossiers/probes from this conversation, **historical scope**; re-read audit before promoting claims |
| `observational_succ/scott_omega_source_weld.py` | New exact rational/interval interpreter, source-weld and omega trace |
| `tests/test_scott_omega_source_weld.py` | Ten additional direct exact tests incl. nesting, chronology, origin alias, circle seam, Fourier error |

## How to validate the new exact interpreter

~~~bash
python -m unittest discover -s tests -p "test_scott_omega_source_weld.py" -v
python research/2026-11-09/scott_omega_causal_weld/session_archive/succ_cmonoid_local_probe.py
python research/2026-11-09/scott_omega_causal_weld/session_archive/succ_omega_dimension_probe.py
python research/2026-11-09/scott_omega_causal_weld/session_archive/succ_omega_gluing_probe.py
python research/2026-11-09/scott_omega_causal_weld/session_archive/succ_scott_omega_weld_probe.py
~~~

Run the repo-wide four AGENTS gates **after** checking out a full repository and installing dependencies. Never equate their absence with success.
