# Reproduction and scope

Run from repository root:

```sh
python research/2026-11-08/covariance_forge/arithmetic/test_terminal_support.py -v
python research/2026-11-08/covariance_forge/arithmetic/run_receipts.py
python research/2026-11-08/covariance_forge/arithmetic/update_hashes.py
```

To replay without overwriting the retained receipt, pass
`--output /absolute/path/to/fresh-receipt.json` to run_receipts.py. Its parent
directory must already exist. Fresh-output replay was byte-identical to the
retained RECEIPTS.json after this option was added.

The first command passed **9 tests**. TEST_LOG.txt captures the local run.
The second passed all **4 prospective controls**, covering 1,008 independently
recomputed exact source states, 708 prime-residue avoidance checks, 4,032
selected principal-part equalities and 1,008 increasing-precision 2-adic
equalities. REPLAY_LOG.txt is the concise output; RECEIPTS.json retains exact
hexadecimal rational seeds, original/shadow history hashes, precision costs,
source chronology failures, and downward-rounded rational signed bounds.

| A | p_A | K | exact construction Kmax | certified Re Cov, h=1 (rounded down) |
|---:|---:|---:|---:|---:|
| 37 | 137 | 73 | 180 | 0.023847376029 |
| 73 | 281 | 145 | 422 | 0.377299412865 |
| 137 | 521 | 273 | 807 | 0.456372824251 |
| 257 | 1009 | 513 | 1554 | 0.675992835525 |

All four exact terminal denominators agree with the authentic source. All
earlier mutant denominators divide its cumulative original D_B. None of the
seeds equals zero; each introduces an original future prime at time zero.
The smallest genuine source birth among their seed primes is respectively
12, 19, 35, 66. These are explicitly rejected by chronological authentication.

The signed certificates use cos(t)>=1-t^2/2 and 2*pi^2<20, plus a complete-cycle
Gauss upper bound and exact interval-overlap weights. No floating pi or complex
evaluation certifies a sign. These finite cases cannot certify the asymptotic
PNT/AP or Bourgain--Konyagin imports, and they do not prove zero-source decay.

This directory is an isolated research artifact on root's pinned worktree.
Only its nine local tests and the described finite replay were run by this
bearing. Repository-wide validation, publication, CI and any formalization
belong to the root integration report; none is claimed here.
