# Preregistered finite probes (development-only, no blind referee)

Declared **before running probe.py** and separate from the exploratory
17+1 exact unit tests. All calculations must retain the **original** four
signed Mellin terms, literal `U_0=0`, and the exact parent PR #481 algebra.

Positive reference tests:
- Original index/finite-precision pairs `(n,k)`:
  `(257,9), (1023,28), (4097,53), (4097,97)`.
  Full zero-seeded recursion and exact `ceil(k/4)`-term source suffix must agree.
- Canonical 2-adic frame/step pairs `(t,k)`:
  `(-133,11), (255,32), (1027,65), (65537,53)`.
  Verify `F(t+1)=16 F(t)+r(t+1)` modulo `2^k`, and bit-lift inverse.
- Independent source channel gluing for `n=257,509,1021` at k=9,53:
  each channel must be nonintegral; only their glued sum has a legal residue.
- Covector/primal eight-step return and gamma=257/32, beta=255/257.

Negative/mutation controls:
- Acting with T on both primal and dual (instead of inverse transpose)
  must FAIL preservation of the canonical split quadratic form.
- Same original four-pole forcing, modified rational initial seed 1/5:
  the difference vanishes at finite 2-adic precision after enough steps,
  while its REAL circle phase offset remains 1/5 forever.
- p-adically tiny rational 2^k/(2^(k+1)+1) remains real-circle distance >=1/3.
- The inherited same-eight-return, changed-observer polynomial mutation of
  PR #481 retains the same representation boost without authenticating π.

Pass/FAIL: exact identities, exceptions, and replayable finite hashes only.
No extrapolation to source-selected Weyl decay, real mixing, physical gravity,
or all-horizon normality. This preregistration is same-reasoner development;
all test independence must remain qualified. Local full repository access may
be unavailable; report explicitly.
