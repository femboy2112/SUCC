# Four poles, three channels, nine matrix entries: source geometry vs Poisson circle response

2026-11-08 research draft. Starting from Main XXI `43a607818907120d4cdab73d240f5b4d7700b63f`. Original four-pole forcing, zero seed and all imported source contracts remain unchanged. **π base-16 normality OPEN.**

The balanced authentic source decomposes exactly into three positive difference channels (3,4,5) with weights (2,1,1). Their source Hilbert Gram is a genuine full-rank 3×3 matrix, with exact rational entries and leading determinant 115200/a^15. The source's second endpoint jet is -59, distinct from the universal rank-two Gamma limit. The observed 1/9 bound is instead the antipodal minimum of one-third the Poisson kernel at radius 1/2, and occurs for a two-pole matched-Gamma source too. A categorical three-channel covariance has rank two, not three. These facts separate actual source multiplicity from observer response geometry.

**Implementation:** `observational_succ/three_channel_source.py`. **Tests:** `tests/test_three_channel_source.py` (8 focused local checks). **Proofs:** `PROOFS.md`. **Truth states:** `CLAIM_LEDGER.md`. **Next source-selected signed target:** `NEXT.md`.
