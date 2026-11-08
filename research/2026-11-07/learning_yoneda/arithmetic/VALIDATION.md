# Validation and authority

Executed from the isolated pinned-main worktree:

```
python -m unittest discover -s research/2026-11-07/learning_yoneda/arithmetic -p 'test_*.py' -v
python research/2026-11-07/learning_yoneda/arithmetic/run_receipts.py
python research/2026-11-07/learning_yoneda/arithmetic/run_prime_epoch_receipts.py
```

Results: **16/16 local tests pass** (`TEST_LOG.txt`), receipt/oracle command exits0
(`ORACLE_LOG.txt`). Four prospective rows collectively verify:

- 130,514 equalities of canonical principal parts at all odd primes <=8B;
- 542 exact 2-adic congruences at precision K+4n;
- 1,084 independently generated unwrapped rational states, using common-denominator
  integers and the combined source polynomial;
- 60 original floor values and 56 integer carry increments retained exactly;
- sixteen rigorous signed Weyl lower bounds, h=1,2,3,5 across four future epochs.

The weakest h=5 lower bound is greater than `999999610297/10^12`; the largest
holdout gives greater than `999999999900/10^12`. These are rational certificates
from cos t>=1-t^2/2 and 2pi^2<20, not rounded complex sums. Each corresponding
seed fails literal zero and complete original denominator-support authentication.

The prospective rows use A=17,37,73,137 and L=19,41,79,139; these deliberately
vary the time and window lengths. The asymptotic theorem separately specifies
L=A. A regression checks the fixed-eta geometric bound. Primary unwrapped states use main's shared `original_forcing` and agree with
its `SelectedOrbit` circle projection through n=156. The literal four-fraction
source is checked independently against both shared and combined formulas.
Malformed primes (including p=1), duplicate entries, floats and bool inputs
are rejected explicitly before any certificate is generated. No cached binary was used and no pi digits were input.

`ARTIFACT_HASHES.json` hashes the core theorem, preregistration, two independent
implementations, replay script, tests, exact receipt JSON, and the two unchanged
shared-source modules (paths relative to this directory). `SOURCE_READ_AUDIT`
records hashes of inherited read-only files. The mathematical proof is paper
algebra; finite certificates check implementations. No local Lean or external
referee certificate is claimed. Repository-wide gates and publication are owned
by the root integration task; this file does not claim them.

The later prime-epoch extension passes four additional tests and its separate
receipt replay. It verifies 1,836 exact clean principal parts, 1,224 complete-cycle
epoch points, five explicit total-variation calculations, and three positive
signed covariance certificates (greater than0.294117646089,0.514285714228,
and0.646153846148). The imported BK/PNT asymptotics are not inferred from these
finite checks. See PRIME_EPOCH_THEOREM.md and PRIME_EPOCH_ORACLE_LOG.txt.

The prime-epoch theorem does prove an unconditional all-epoch *local-prime
marginal* upper saving. No upper cancellation estimate for the full original
real character, LS, H2*, or Fejer decay was proved here. **pi base-16 normality OPEN; RH OPEN.**
