# Integration of the two Principia research programs

[Unified manuscript](../../../docs/principia_observatoris/SYNTHESIS.md) · [Theorem register](UNIFIED_THEOREMS.md) · [Validation](FORMAL_AND_TEST_RECEIPTS.md)

## The two inputs and their origin

The reconstruction found all three preparation commits live. Main and both predecessor draft branches were read from GitHub. The integration starts with the following source graph.

~~~mermaid
flowchart TD
  M["Main XXV db9fb4b8"] --> F["Founding note #618 ab310575"]
  F --> A["Astra #619 f9efa624"]
  M --> B["Second Forge #620 5b7470c6"]
  A --> J["Two-parent integration df5bd184"]
  B --> J
  J --> T["Tenacious D synthesis"]
~~~

From the common base the Astra line changed 55 paths including the founding note. The Fable line changed 31. Their path intersection is empty. Inspection of the second parent's commit range identified the Second Forge development and its two preserved correction rounds. The GitHub integration object and the locally constructed merge have the same ordered parents and the same tree `20a2bd81d422e45b679e26347f29a926e287cc8f`. Every path changed on either side was compared by its Git blob identity at integration. The packages' research history remains inspectable from either parent. [Ancestry and all 86 source blobs](receipts/ancestry.json)

| Research layer | Original source and retained role |
|---|---|
| Founding questions | [All nine sections of #618](../../2026-11-13/causal_relevance_proximity/RESEARCH_NOTE.md) supply the conjectures and original examples shared by both teams. |
| Astra theory | [Six books](../../../docs/principia_observatoris/README.md), [original claim register](../../../docs/principia_observatoris/REFERENCE.md), [audits and exact laboratory](../../2026-11-13/principia_observatoris/README.md). |
| Second Forge theory | [Complete package](../principia_observatoris_second_forge/README.md), [theorem forge](../principia_observatoris_second_forge/THEOREM_FORGE.md), [handoff and interoperability contract](../principia_observatoris_second_forge/TENACIOUS_D_HANDOFF.md), [two rounds of hostile review](../principia_observatoris_second_forge/agents/OPUS_IV_REFEREE_ROUND2.md). |
| Existing SUCC foundation | [Ancestral relations](../../../docs/CLAIM_SUPPLEMENT_PRINCIPIA_ANCESTRAL.md), [carrier-relative targets](../../../docs/CARRIER_RELATIVE_TARGETS.md), [architecture](../../../docs/ARCHITECTURE.md), [claim ledger](../../../docs/CLAIM_LEDGER.md), [original import manifest](../../../provenance/IMPORT_MANIFEST.json). |
| New common interface | [Axiom/type map](AXIOM_AND_TYPE_MAP.md), [bilateral verdicts](CROSS_EXAMINATION.md), [adversarial cases](COUNTERMODEL_EXCHANGE.md), [primary-source lineage](PRIMARY_LITERATURE.md). |

## How to use the combined mathematics

1. Specify a source set, the actual observation map, branch outcomes, action availability, costs and which outcomes a performed record admits. Public refusal needs a specified post-refusal law. Retain original and current state jointly if interventions are destructive.
2. Name the target and the semantics of the comparison. Endpoint reachability, a successful decorated word, a joint stochastic law, a signed amplitude, a coarse readout and a safe terminal command live in different spaces.
3. Use the rooted descent test when every representative must execute the same action. Use the stated value algebra if only a particular path valuation matters. For real or stochastic weights transport actual operations on signed values or probability masses. Reachability alone does not determine their magnitudes.
4. Ask which policies one carrier can execute. Give the uncertainty class, sensor calibration and action costs. With a deadline add the actuation map and arrival times. The exact precision and polyhedral results supply checkable positive and negative certificates in their respective classes.
5. If the conclusion concerns a future law or a limit, discharge the model-class, continuity and convergence hypotheses. A rational finite simulator can establish implications from these inputs. Physical source selection and interpretation need evidence of their own.

The only new native Python API solves a declared scalar recovery problem using existing Astra rational matrix operations. Its entry points are `central_radius` and `best_interval_schedule`. The theorem-specific experiments remain standalone and the separate Lean bridge imports the two original formal modules. [Code](../../../observational_succ/tenacious_acquisition.py) · [Tests](../../../tests/test_tenacious_acquisition.py)

## Research contract and verdict

**Initial question.** Does path exactness imply knowledge of the next target? Positive case: exactness for every rooted one-letter experiment with complete public labels. Negative control: a chain of length two that reaches the same reports from two representatives at different times. Other adversaries include cashing a hypothetical reset twice, forgetting an outcome on one branch, resolving the initial source from the current state alone, and identifying a projected signed response with graph support.

**What closed.** There is a sharp finite test language for deterministic action descent and a formal bridge to filtered Boolean endpoint exactness. For a prescribed target, timely action can require fewer distinctions than full identification. The new manuscripts give deterministic adaptive acquisition and constrained control certificates, a stochastic counterpart, and exact source-specific precision estimates. These are mathematical proof steps within the declared model classes. The original papers, same-model subreviews, exact enumeration, formal kernels and external research have separately attributed authority.

**Next boundary.** Certificate size for finite-precision action and observation is now a sharper research question than existence in a finite model. The full policy tree can be exponential. For π the weakest open rung still requires a signed estimate for the actual zero seed. [Next theorem and a falsifying experiment](NEXT_FOUNDATIONAL_THEOREM.md)

The concurrent downstream [RH/abc observer draft #621](https://github.com/femboy2112/SUCC/pull/621), inspected at `6255b84b538994975910cc738761620d3b69f9ff`, lies outside the two-parent research ancestry.
