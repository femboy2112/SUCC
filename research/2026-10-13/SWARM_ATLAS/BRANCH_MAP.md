# Frozen research DAG and integration provenance

The initial reconstruction inspected the live repository rather than assuming
main contained the research. These exact heads were observed at swarm intake.
The stack is preserved; this work creates a draft above VOYAGER. PR45 is a
parallel sibling, audited file by file, never merged wholesale.

| Ref | Exact intake SHA | Parent research line |
|---|---|---|
| main | 52d2c02b85b246aec67160260ac06bb1da33645e | default branch |
| PR40 | a085d754e037498a20cbb4d2330e3ce02d2f60c2 | main |
| PR41 | a5462ea4ef655bba7dd67fbc16ec048acfb994d1 | PR40 |
| PR42 | 45597a5750971130e3399ed69c03e107bdc28c70 | PR41 |
| PR43 | 1cb30a3d92420f1197fc1615a68fb4309c0e036d | PR42 |
| PR44 | 091b9e6ecb0f4bb1a162db2e97ef0f8d9a00f6ed | PR43 |
| PR46 | 00bc0d44cb011b1d333aa0fa8549d6b402662317 | PR44 |
| PR47 | b17c357e2aa6aee17ae87115b8620a51a262e1fc | PR46 |
| PR48 | 5eb09e7cba36ec01b8f9d6834b78b5766fd93935 | PR47; integration base |
| PR45 | b2774ca485db4b5b4f7ce92e535220352fb3af2f | PR43; sibling |
| PR50 initial durable checkpoint | 3e0efe08a314fd50e308d96d6de6b806e79e3568 | PR48 |

[Draft PR50](https://github.com/femboy2112/SUCC/pull/50) tracks
`research/many-worlds-swarm-2026-10-13` against
`research/voyager-observational-profinite-completion-2026-10-13`.
Its final head is reported by the PR itself; this file does not contain a
self-referential final-commit hash. `REGISTRY.json` records exact investigator
commits and integration state. Local cherry-pick hashes and GitHub connector
checkpoint hashes may differ; the published final tree is checked against the
local integration tree. Original investigator hashes identify the audited
local snapshots, not an assertion that those branch refs were separately pushed.

Lean identities remain separated: VOYAGER and this swarm use 4.14.0; PR45
uses 4.19. The new topology package pins mathlib
4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84. No archival source, default branch,
release, tag, or historical runtime default was changed.
