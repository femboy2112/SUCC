# Duck Principle: pinned Lean proof-authority receipt

**Date:** 2026-10-21. **Branch:** research/duck-principle-pi-proof-first-2026-10-21. **Main base:** b116841f12b41aaf7600da39bbb40577f25b6295.

## Exact artifact

- Formal source: [formal/DuckPrinciple.lean](../../formal/DuckPrinciple.lean), blob SHA-1 **4d72da20f41b0ff06305b6f19acd7fa864b87924**, source commit **bbb4c383cb44f4bdfd6c51142ad70880eefc5773**; unchanged by later CI/report edits.
- First fully successful pinned compile + audited four key declarations: [GitHub Actions run 39605851189](https://github.com/femboy2112/SUCC/actions/runs/39605851189), job 119241714545.
- Expanded **all-eight-declaration axiom audit**: [GitHub Actions run 39606041265](https://github.com/femboy2112/SUCC/actions/runs/39606041265), job 119242359686, **conclusion success**. CI checked out the PR synthetic merge commit for the branch against main. Only the CI audit file changed between the source success and expanded audit.
- Installed toolchain output: Lean 4.14.0, x86_64-unknown-linux-gnu, commit 410fab728470, Release. Repository lean-toolchain: leanprover/lean4:v4.14.0.
- Commands in workflow: compile formal/DuckPrinciple.lean; copy the file, append eight #print axioms directives, then compile the combined input. The placeholder scan on uncommented code rejected sorry/admit/axiom/unsafe/native_decide and passed.

## Kernel statements and axiom boundaries

The source contains exactly the following **eight theorem declarations** in namespace ObservationalSUCC.Duck. The whole file compiled, and every theorem received an axiom-report inspection in run 39606041265.

| Lean theorem name | Exact limited meaning | Observed #print axioms |
| --- | --- | --- |
| factor_all_words | Declared action factor commutes with every finite action-word execution | no axioms |
| factor_preserves_observations | Commuting word theorem remains true after an arbitrary declared readout | no axioms |
| factors_compose | Composition of same-action-alphabet factors is a factor | no axioms |
| faithful_probe_certifies_factor | Injective report plus all one-step observed commuting squares implies actual factor | no axioms |
| bounded_separating_probes_certify_factor | Declared target word probes of length ≤budget separating all target states + agreement imply factor | no axioms |
| failed_factor_yields_separating_experiment | If all finite target action-word probes separate states and a factor fails, some action/source/word has differing observations | propext, Classical.choice, Quot.sound |
| erased_systems_mimic_every_word | For Bool flip-vs-idle and erased Unit readout, any finite word produces the same readout | no axioms |
| erased_resemblance_does_not_certify_identity | Candidate identity map is *not* a factor for Bool flip→idle | no axioms |

All these claims are **LEAN_KERNEL_PROVED for exactly their theorem signatures**. The classical existence statement makes no efficiency or computability guarantee. The results do not infer the existence of a factor from resemblance, and do not verify the specific source maps of any physical system. They do not formalize the logistic-map example, π, Gamma, Euler prime data, BBP, RH or ABC.

## Negative controls and independence

- The erased Bool example is a **kernel-proved counterexample** to the invalid inference that identical reported behavior under a coarse probe forces the candidate identity factor law. This proves a limitation of *that candidate factor*, not that no common trivial quotient exists.
- Source-file placeholder screening passed; actual Lean kernel compilation and dependency inspection passed.
- A separate negative **mutation-rejection run was not carried out** in this receipt; it remains an acceptance task for the broader proof infrastructure, not a claim about the current eight proofs.
- Same-repository GitHub CI is an authentic kernel run, but not an independent human referee or a proof that the formalized proposition matches every philosophical interpretation.

## Subsequent dependencies

1. Define and kernel-prove the logistic semiconjugacy over Mathlib Real.pi/circle quotient; preserve noninjectivity and distinction from conjugacy.
2. Formalize BBP rational r(m), its O(m^-2) bound and the O(n^-2) orbit transport of the genuine base-16 π sequence. The current bound is paper-proved in [the dossier](DUCK_PRINCIPLE_AND_PI_PROOF_FRONTIER.md) but not Lean-certified.
3. Seek π-specific global Fourier cancellation; normality remains **OPEN**, and RH/ABC assumptions must never replace the missing theorem by fiat.
4. Obtain hostile mutations, independent theorem type audit, and combined repository validation before main merge.
