# Operation SUCC: Mathematical Many-Worlds Swarm

Integration baseline: VOYAGER `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. EOS sibling: `b2774ca485db4b5b4f7ce92e535220352fb3af2f`; shared ancestor `1cb30a3d92420f1197fc1615a68fb4309c0e036d`. Main: `52d2c02b85b246aec67160260ac06bb1da33645e`. Verified live on 2026-10-13 with git fetch, GitHub branch API, PR list/checks. Existing stack CI passed; this is baseline evidence, not new-swarm CI.

[Live registry](registry.json) records 48 distinct first-generation assignments. QUEUED is not completed research. First-generation investigators write separate worktrees from that immutable baseline; second-generation investigators use a named reviewed integration snapshot; the principal reviews and integrates semantic commits. Three native investigators plus one principal, tiny exact probes, one compiler maximum. Observed machine at launch: 7GiB RAM, about 2.1GiB available, 31GiB swap with 5.2GiB used.

No archive/default changes, no wholesale EOS merge, no main mutation. Lean4.14 remains the integration pin; EOS4.19 is isolated. Supplementary IDs SWM-* do not alter historical O*/EOS-* numbering.

Every dossier supplies exact question, classical context, typed objects, quantified theorem, proof, hostile witness, verdict, obstruction, lawful cross-domain map and command/commit receipts. Kernel, paper, exact finite and numerical evidence remain distinct. The [rolling atlas](SUCC_MATHEMATICAL_ATLAS.md), [claim supplement](CLAIM_SUPPLEMENT.md), [branch map](BRANCH_MAP.json) and [checkpoint](CHECKPOINT.md) link reviewed survivors and preserved failures. They explicitly distinguish assignment completion from mathematical acceptance.


Local repository validation passed all 1,602 tests and required provenance/observer/ordinal probes. Cold GitHub topology run38365807103 and full repository run38365807118 passed at integration3e538c6; exact receipts are retained. These results do not certify unfinished expeditions.

To reproduce the pinned topology gate, keep dependencies outside this checkout:

```sh
python scripts/swm_topology_bootstrap.py --lean /path/to/lean4.14/bin/lean --mathlib-dir /external/mathlib-4.14 --receipt /tmp/swm-bootstrap.json
python research/2026-10-13/SWARM_ATLAS/experiments/B09_topology_gate.py --lean /path/to/lean4.14/bin/lean --mathlib-dir /external/mathlib-4.14 --receipt /tmp/swm-kernel.json
```

The bootstrap checks exact compiler/dependency commits, refuses wrong existing checkouts, and downloads only declared topology imports. Compiler runs are serial with1,280MiB resident-process-tree limit,4GiB address-space limit,768MiB minimum system headroom and explicit timeouts. Kernel output rejects nonstandard axiom dependencies. Original resource-limit failures remain in receipts.
