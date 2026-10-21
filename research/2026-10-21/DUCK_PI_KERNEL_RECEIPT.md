# Duck / π kernel receipt

This is an observation of actual pinned builds, not a self-authenticating JSON
proof. Final combined validation is in progress; the successful observations
below are scoped to their exact commits.

The project uses official Lean 4.14.0 and mathlib revision
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. The official Linux toolchain archive
SHA256 is `320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`.
The manifest pins all transitive dependencies. CI checks their actual Git heads
and rejects tracked modifications before compilation.

## Observed checkpoint

[Run 39613723244](https://github.com/femboy2112/SUCC/actions/runs/39613723244),
commit `6fbe9d29355aaccca5ebf2753d34eee2e2ece627`, compiled and exported
97 declarations from DuckPrinciple, DuckObserver, BaileyCrandall, BBPIntegral,
LogisticFactor, Normality and PiSource. It also compiled two generated finite
certificates with three declarations each. The BBP identity has no premise
asserting that identity; its proof uses an integral and dominated convergence.
The π transport declarations quantify only their natural index.

The axiom union of those exports is exactly `propext`, `Classical.choice`, and
`Quot.sound`. Nine applicable mutations failed while their positive originals
compiled. The two generated readout mutations also failed. The whole run was
**FAILED** because WeylBridge did not elaborate; its blocked Haar mutation was
not counted as a successful control. Later source edits require a new build.

## Reproduction and trust boundary

With the pinned official toolchain installed, run from the repository root:

```sh
cd formal/duck_pi
lake exe cache get
cd ../..
python formal/duck_pi/check.py --output /tmp/succ-duck-pi-kernel
```

The script removes stale project oleans, rebuilds declared modules, exports
actual theorem types, computes type/source hashes, and inspects dependencies.
It rejects forbidden proof escapes in project sources and rejects exported
axioms outside the declared standard set. Paired false-proposition mutations
must fail for semantic reasons, with a compiling positive control.

Generated observer certificates contain literal transition/readout/relation
tables. Lean checks every finite relation law using `decide`, then proves the
all-word statement by the general induction theorem. Python's prior verdict is
not imported as a proof. The JSON/hash comments bind declared model data for
comparison but do not authenticate an external physical source.

Trust includes the official Lean binary, pinned dependencies, GitHub execution
and the reviewed build/export scripts. An attacker controlling those components
or arbitrary code inside the same interpreter is outside this claim. An
externally supplied success JSON is not trusted. These research exports are
**not automatically admitted** to SUCC's installed Level-C catalogue.

Local Lean startup could not read its numeric process executable path in this
cloud environment. Hosted CI supplied actual execution; no patched kernel or
permission bypass was used, and no local Lean success is claimed.
