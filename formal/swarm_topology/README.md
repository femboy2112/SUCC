# SWARM topology kernel package

This isolated package pins Lean4.14 and mathlib commit
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. It preserves the existing
standalone core formalization and all sibling toolchain identities.

```sh
lake update
lake exe cache get Mathlib/Topology/Compactness/Compact.lean Mathlib/Topology/Constructions.lean Mathlib/Topology/Separation/Basic.lean
lake build SwarmTopology SwarmPolicyCompactness SwarmX01CompletionTransport
```

`SwarmTopology.lean` proves the genuine finite-coordinate closure criterion,
closed-image actualization criterion, inverse-thread/profile continuous inverse
maps, finite-alphabet completion compactness, and compact continuous-source
realization. All proofs concern declared mathematical source maps.
See `research/2026-10-13/SWARM_ATLAS/B09.md` for exact scopes, proof structure,
controls, executed host command, and remaining physical/effective boundaries.

`SwarmPolicyCompactness.lean` checks the open bounded-halting-set compactness
core. Continuity of policy history cylinders remains a separate paper proof.

`SwarmX01CompletionTransport.lean` checks continuous completion transport,
source naturality and actualization reflection under explicit transport gates.
Its finite-coordinate injectivity criterion remains a paper proof.
