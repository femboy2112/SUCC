# Validation and provenance boundary

Pinned repository parent: PR #475 at
20acb35a42b6ae5fb9260c041ed3a1aa47429484. The live GitHub connector confirmed
this head and draft state. Read AGENTS.md and parent #451/#453/#474/#475 proofs.
No production, formal, archive, source-contract or workflow edits are proposed.

Local git clone FAILED: github.com hostname could not resolve from the container.
This is an access boundary, not a failed mathematical test. The new files were
therefore executed in isolated staging, not represented as a complete checkout.

ACTUALLY RUN:
- 23/23 isolated new unittest tests passed. Includes six exact parent self-scale
  receipts, four-pole/odd/polynomial source agreement, integer/Fraction agreement,
  sorted transport vs independently evaluated CDF integral, adverse examples,
  finite Ward and Fejer checks, and the PSD-vs-pointwise-positivity mutation.
- Symbolic exact algebra: odd-source difference 0, rotated Cayley reciprocal
  difference 0, r2/r3 incompatibility 133558/765765, and the all-positive source
  Ward-bound polynomial numerator. These finite symbolic identities are not an
  external mathematical review of every analytic step.
- probe.py generated exact source observations through n=8191, independent
  Fraction agreement through n=256, four full-prefix mirror observations and
  three logarithmic-mesh epochs. Floating displayed values are accompanied by
  rational enclosures; count vectors/energies are exact.

Not claimed: full native >11k repository test suite, full provenance probes,
new Lean compilation, external independent referee, blind independent holdouts,
or any all-horizon original-source cancellation estimate. Existing parent CI
results do not validate these new files. Same-reasoner alternate derivations and
independent code paths are not blind reasoner independence.

Reproduce locally on a genuine checkout:
python -m unittest discover -s tests -p 'test_weyl_mirror_campaign.py' -v
python research/2026-11-02/weyl_mirror_campaign/probe.py --verify
python -m compileall -q research/2026-11-02/weyl_mirror_campaign

Mathematical status: paper proofs of the stated conditional implications and
scope-limited algebraic obstructions; selected pi source premises OPEN.
