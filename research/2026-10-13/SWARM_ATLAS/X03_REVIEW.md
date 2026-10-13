# X03 adversarial review receipt

Author/owner: independent second-generation assignment `cross03_gluing_cegis`.
This is its adversarial self-review, not an additional independently staffed
reviewer. The assignment independently reconstructed the A03 × F42/F44 bridge
from source at `71eaf11e48ca3ccb349858bba64abf36b59ee6f5`.

| Claim attacked | Attack | Result and boundary |
|---|---|---|
| Constraint cores persist under constructor expansion | Add a free hidden bit; add a deterministic parity graph | Inherited unsatisfiability persists; onto projection preserves all 8 constraint subproblems and the minimal core. |
| Minimal cores persist for arbitrary original maps | Restrict contradictory 0/1 carrier to original 0 | False: two-constraint core becomes singleton. Surjectivity is essential. |
| Finite grammar exhaustion proves original inconsistency | Grammar includes only 0 while original source includes 0 and 1; require 1 | Returns `UNSAT_GRAMMAR`, retaining original witness 1 in the independent source oracle. |
| A learned counterexample can be dropped after the next mutation | One-bit mutually contradictory obligations | Last-only learner alternates eight checked proposals; monotone learner terminates in two failures. |
| Pairwise support compatibility is enough | Equality/equality/inequality bit triangle | All overlaps agree; the three constraints form a minimal obstruction. |
| More probes fix inconsistency | Preserve old triangle relations with parity coordinate | Refuted; the original obstruction pulls back unchanged. |
| A relaxed relation is a conservative solution | Replace triangle inequality by full relation | Witnesses 000/111 violate the old relation; explicit contract change. |
| Semantic global sections license execution | Two-bit original 11; first read erases the second bit | Static section exists, sequential two-1 report does not. |
| Finite enumeration implementation may silently use the same oracle | Adaptive retained-constraint solver versus separate dictionary join | All 4,096 relation families agree, all returned unsatisfiable cores independently checked for deletion-minimality. |
| Successful synthesis may invent originals | Grammar row outside the declared source, missing coordinate, bad domain | Each rejected with a typed error. |

The proof of termination uses strict growth of the learned index set and strict
shrinkage of viable grammar candidates. Random proposal policies, unavailable
empirical sensors, source-dependent changes to the verifier, and infinite
grammars are not covered. The executable grammar is a finite **denotation**
table, not a verified parser/compiler for an arbitrary constructor language.

No code from the earlier gluing, discovery, or history implementation is
imported. Sources are explicitly complete mathematical tables. A passing
test does not authenticate their empirical interpretation.

Validation: 11 targeted tests passed, including the complete 4,096-family gate.
The reproducible probe records exact family counts and file SHA-256 values in
`X03_RECEIPT.json`. No Lean-kernel check or full repository run is claimed for
this assignment. A coordinator can rerun the probe and inspect the proof.
