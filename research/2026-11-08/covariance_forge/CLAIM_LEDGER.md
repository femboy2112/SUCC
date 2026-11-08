# Claim ledger for the covariance forge

Domains and proofs are linked; statuses do not inherit upward from tests.

| Claim | Status and precise scope | Receipt / next falsifier |
|---|---|---|
| CFS1: all cyclic temporal bins of the selected prime clock decay | PROVED PAPER, original local factor, imported BK | [Proof](spectral/THEOREMS.md); full-order shift is excluded |
| CFS2: all real temporal tones on every actual epoch decay | PROVED PAPER; exact eps_A retained | Dirichlet interpolation, cyclic repetitions, PE interval gluing |
| CFS7/CF-R1: polynomial chirps with 2^d=o(logp) decay uniformly | PROVED PAPER, local factor only | [Growing-degree proof](GROWING_CHIRPS.md); degree near log2logp with bounded subtraction not licensed |
| CFS3–5: history/sparse/chirp approximation implies signed bound | PROVED CONDITIONAL; fitting rates unpaid | Leakage plus residual certificate; arbitrary rank-one resonance is hostile |
| CFS6: maximal-covariance shadows evade cheap sparse models | PROVED PAPER; sharp norm lower bound | Exact finite sharp witnesses; no original-source sparsity conclusion |
| CF-A2–5: exact terminal-denominator counterseeds | PROVED PAPER with pinned #532/PNT inputs | [Proof](arithmetic/THEOREMS.md); four independent exact holdouts |
| C1–3: rational height isolation, carry fiber and precision loss | PROVED LOCAL at stated source/access domains | [Proof](crucible/THEOREMS.md); exact zero/source-height hypotheses matter |
| C4: zero marginals plus simple finite source need not decorrelate | REFUTED shortcut by fixed changed-forcing model | Covariance lower48001/48841 at p13,q17; source mutation explicitly rejected |
| Finite R4 covariance threshold | CERTIFIED FINITE only,32 listed cases | All pass; next unseen epoch could refute, no asymptotic promotion |
| Best sqrt(m)-sparse error<=1/2 on every tested original clock | REFUTED FINITE | Six exact failures, four finite passes; all ten AR controls fail |
| Cheap carry-history certificate<=1/2 | REFUTED FINITE in all12 cases | Causal features fixed before measurement; certificate expression distinguished from true W |
| Cancellation implies a cheap chirp predictor | REFUTED in the general unit-factor class | [Exact changed-complement control](PREDICTOR_BOUNDARY.md) has W=0 but predictor budget at least1 |
| Original-zero complement approximation or covariance decay | OPEN | Need an all-epoch signed source estimate for each fixed nonzero h |
| Pi base-16 normality / RH | OPEN / OPEN | No complete proof chain supplied |

No new asymptotic theorem is Lean-certified. Independent implementations and
same-model proof reviews support scrutiny; they do not replace paper proofs
or external scholarly review. Classical imports and the immutable source
remain explicit in the provenance record.
