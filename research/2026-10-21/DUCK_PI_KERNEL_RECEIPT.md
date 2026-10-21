# Duck / π: successful pinned kernel receipt

**Successful build:** [run 39634613571](https://github.com/femboy2112/SUCC/actions/runs/39634613571),
commit `2aeaa6dba70ca6fefefe0f8eb73078a6a17eff19`, tree
`5ad9100911797d52903b95ecb12a5df09c7c1f85`.
All eleven modules compiled: **146 exported theorem types**, plus **six
declarations from two generated finite certificates**. These counts include
helper lemmas, not 146 novel discoveries. Eleven source/proposition mutations
and two generated readout mutations were rejected with positive controls.

The axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`.
No accepted declaration depends on a new proof axiom or `sorryAx`. The scan
rejects `sorry`, `admit`, `axiom`, `unsafe`, and `native_decide` in project
inputs. Failed attempts and diagnostics remain in the
[validation history](DUCK_PI_VALIDATION_HISTORY.json); successful modules
never made a failed combined run successful.

## Exact environment and evidence

* Official Lean **4.14.0** Linux archive SHA256:
  `320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`.
* Mathlib revision: `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`.
  The manifest pins all transitive dependencies; CI checks actual Git heads
  and rejects tracked modifications.
* [Complete compressed observation](DUCK_PI_KERNEL_RECORD.json): exact theorem
  expressions, type/source hashes, axiom lists, dependency revisions, command
  results, and mutation outcomes.
* Decoded observation SHA256:
  `518db0ec2e7a09491f12e316f57bc3f1f63f772d2cdefb7d6830e1b82ee94616`.

| Module | Exported declarations |
|---|---:|
| DuckPrinciple | 8 |
| DuckObserver | 17 |
| BaileyCrandall | 35 |
| BBPIntegral | 14 |
| LogisticFactor | 12 |
| Normality | 9 |
| PiSource | 7 |
| WeylBridge | 21 |
| HaarBoundary | 5 |
| HaarIntervals | 12 |
| AsymptoticTransport | 6 |

The BBP identity uses an explicit integral and dominated termwise integration.
It has no premise asserting BBP or identifying an arbitrary constant with π.
The π shadow-distance theorems quantify only their natural index. In contrast,
the final normality implication visibly requires

```lean
FourierCancellation
  (fun n => ObservationalSUCC.BaileyCrandall.liftedOrbit (n+1))
```

Its conclusion is `PiNormal16`. Replacing that hypothesis with `True` fails
by application type mismatch. This rejects unsupported proof transport; it
does not assert that π-normality is false. The cancellation premise remains
open. Base-16-to-base-2 descent is paper-proved only.

## Reproduction and trust boundary

From a committed checkout with the pinned official toolchain installed:

```sh
cd formal/duck_pi
lake exe cache get
cd ../..
python formal/duck_pi/check.py --output /tmp/succ-duck-pi-kernel
```

The script binds declared source inputs to HEAD, removes stale project oleans,
rebuilds the project, exports actual types, and inspects axiom dependencies.
It checks that sources and HEAD did not change during the build. Dependency
oleans come from mathlib's official cache; this is not a fresh source rebuild
of every mathlib dependency.

To inspect the observation without treating its JSON as authority:

```python
import base64, gzip, hashlib, json
from pathlib import Path
p = Path("research/2026-10-21/DUCK_PI_KERNEL_RECORD.json")
wrapper = json.loads(p.read_text())
raw = gzip.decompress(base64.b64decode(wrapper["payload"]))
assert hashlib.sha256(raw).hexdigest() == wrapper["decoded_sha256"]
record = json.loads(raw)
```

Generated observer certificates contain literal transition/readout/relation
tables. Lean checks every finite law using `decide`, then proves all-word
agreement by general induction. Python's verdict is not imported as proof.
Source tags/hashes identify declared data, not an external physical source.

Trust includes the official Lean binary, pinned dependencies and their cache,
GitHub execution, and reviewed build/export scripts. Arbitrary hostile code
controlling these components is outside the claim. An externally supplied
success JSON is untrusted. These exports are **not automatically admitted**
to SUCC's installed Level-C catalogue.

Local Lean startup could not read its numeric process executable path in this
cloud environment. Hosted CI supplied actual execution; no patched kernel,
permission bypass, or local Lean success is claimed.

This receipt is pinned to the build above. Later documentation commits can
carry the same checked sources; compare source hashes. Exact final PR checks
are separately attached to the actual PR head. See the
[execution report](DUCK_PI_EXECUTION_REPORT.md) and
[local validation receipt](DUCK_PI_LOCAL_VALIDATION.json).
