# many-worlds-swarm parallel-assembly receipts (source-qualified)

The canonical assembly in `main` is the atlas (#49). The `many-worlds-swarm` (#50)
sibling is a parallel assembly of the same 48+12 swarm whose consolidated
`observational_succ/swarm_*.py` library is kept (a load-bearing dependency of the
carrier/no-ghost code). Its reproducibility gate `scripts/verify_swarm_receipts.py`
replays the `scripts/swarm_*_probe.py` probes against the frozen receipts THEY produce.

Those receipts live here, source-qualified, so they do not collide with the atlas's
canonical `research/2026-10-13/SWARM_ATLAS/*_RECEIPT.json` (verified by the atlas's own
per-mission tests). Same filename, different assembly — kept apart, not resolved away.
See docs/MANY_WORLDS_SWARM_AUDIT_2026-10-13.md.
