# Integration and exact source provenance — SUCC signed lag forge

**2026-10-31, DRAFT research only.** No merge into main, no edit to archival source, formal kernel, workflows, user data or published mathematical claims.

## Pinned ancestor and sibling heads

- Main XVII: e8598cfa5d32fd1de8e94a3e458a366a0850d59e.
- PR #431 carrier-relative path measure: cf23b8cfc39f56935c432ed764adf0a33efb0d7e (parent of both #432 and #433).
- PR #433 BBP selected-seed superposition: 5721c048b54430b3d2195d63ba4d1a9ec0794f99, **direct parent** of this branch; its historical positive-path and seed controls are inherited unchanged.
- PR #432 original BBP edge/seed tomography: d3907a7937b10dbf51f3926e0dd3460d5ff12353, independently based on #431, **sibling explicitly imported** into this combined research branch. No independent proof-family claim from copying.
- PR #430 3-adic BBP source-pole sharpening: ba8bc0d3636af19c93f5983094456e44ecac457c, read-only research context, NOT merged or made an undeclared runtime dependency.
- Main XVII source definition and U0=0 stay byte-for-byte unchanged.

## Verbatim sibling PR #432 import — 11 original Git blobs

These paths are imported into the new research branch by setting the existing original blob identities in the Git tree, **without reauthoring or modifying** the files. The import was atomic, commit 766b7e14cea50899d8e5358fbfd2dc4ed9694e4c.

| Source-relative imported path | Exact original Git blob SHA |
|---|---|
| research/2026-10-31/edge_seed_tomography/CLAIMS.md | bf497dd06d339122eba5b120afa3112882b47c40 |
| research/2026-10-31/edge_seed_tomography/NEXT.md | d829758991b645495716328be71e97014f99105e |
| research/2026-10-31/edge_seed_tomography/PROOFS.md | 03139eb39f749a3414d951fb3f0c246d1f7786da |
| research/2026-10-31/edge_seed_tomography/README.md | 612e1e77865e96e6da8f03859f40523c2415b710 |
| research/2026-10-31/edge_seed_tomography/SOURCE_MAP.md | be72ed51acc5050e9ea1571dea1b018281f84bb6 |
| research/2026-10-31/edge_seed_tomography/VALIDATION.md | f3f68ade4ebdbf2de2f42365b453ebe825dc4414 |
| research/2026-10-31/edge_seed_tomography/edge_seed_tomography.py | 364ed2223d9bc865f1bb411d1faa2d44bdb39959 |
| research/2026-10-31/edge_seed_tomography/finite_receipt.json | 620fbd9e2eaeaa91e384ab284ebd542ae447abd4 |
| research/2026-10-31/edge_seed_tomography/independent_oracle.py | 9aab65be541b71c392a152984d96802ae31a4a3c |
| research/2026-10-31/edge_seed_tomography/probe.py | 0995df743b59e0445aed39fadafa3b5407252c00 |
| tests/test_edge_seed_tomography.py | d2fbbbd137f67e2a7039ef7af0b7643f52ba0bac |

**No conflict was silently reconciled:** #432 and #433 touch disjoint additive research/test paths. The combined branch exposes them together for the first time. CI on that exact combined head—not separate sibling CI alone—is the integration gate.

## Exact newly authored and local-tested blobs

The new signed lag research module and tests were authored in isolated local runtime, run together on Python 3 and verified byte-for-byte by comparing their SHA-1 Git blob hashes to the results from the GitHub connector before the atomic source commit bdda83caabe5a647bef405f01e47d3180a3cd1eb.

| New authored path | Exact SHA |
|---|---|
| research/2026-10-31/selected_lag_tomography/selected_lag.py | 59d0351484865ab919317ae1a34f6e9ec1b12da3 |
| research/2026-10-31/selected_lag_tomography/independent_oracle.py | d4c5a4a815fe3d8beb29b075972e2de03eb63fdf |
| research/2026-10-31/selected_lag_tomography/run_receipt.py | f294eb5ae0c6b77fe300623591755c27e0037304 |
| tests/test_selected_lag_tomography.py | 75df7fdae1a790bce4e23a39620da3dd9c2f4551 |

The 28 focused exact source/Gaussian/Taylor/CRT/hostile tests passed locally; full on-branch parent/sibling tests, Lean and original 10k+ suite remain subject to hosted exact-head results. Independent mathematical proof of the all-horizon selected signed saving remains OPEN.

**Branch discipline:** This work is an additive child PR against #433, not a claim its siblings have been merged into main. Maintain draft. Any later integration to main must review both original sibling and child provenance/contract status, test all imported code together and explicitly authorize merge.