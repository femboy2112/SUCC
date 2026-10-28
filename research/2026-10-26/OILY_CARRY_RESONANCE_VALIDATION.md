# Oily carry/resonance validation record

This record is finalized after the combined-tree gates. Historical archives and
the original four-pole forcing are unchanged. Worktree parent:
`a8c7c85b7a1900d422090f1757c174e7aac69f44`.

**Final local result:** full discovery passed **8,844 tests in 1,146.182 seconds**,
exit 0, with no failures, errors or skips. All 1,697 snapshotted Python source
paths and hashes remained unchanged. Provenance, observer and ordinal probes
also passed on the final tree. Pinned local Lean results below retain their
explicit runtime qualification; hosted CI is a separate observation.

## Environment and baseline

Python is the existing virtual environment at
`/workspace/scratch/d39f55bad1de/succ-venv/bin/python` (3.12.14), with
mpmath 1.3.0 and SymPy 1.14.0. Native invocations set `PYTHONPATH` to the
current worktree root. Without that setting, the environment's old editable
installation resolves to the prior worktree; one early receipt invocation
failed for that ordinary environment reason. It was rerun correctly.

The parent #310 tests passed 16/16 before development. Provenance verified all
72 entries; observer and ordinal probes passed; the six historical-registry
tests passed, including the formerly missing pinned blob.

## Focused implementation checks and exact evidence

| Check | Result / boundary |
|---|---|
| New integer-branch coercivity tests | 12 passed; exact finite claims and adversaries |
| New carry-conditioned totient tests | 14 passed; source decoder/cyclotomic/coupling controls |
| New signed interval instrument tests | 8 passed; sound-enclosure calibration and mutants |
| Parent totient receipt | replay passed |
| Parent Oily source receipt | replay passed |
| Parent quadratic-substrate receipt | replay passed |
| New selected signed receipt | write and independent replay passed |
| Independent hostile oracle | replay passed; corrupted norm fixture rejected |
| New branch-energy oracle | 16 exact certificates, direct-cell and tied-boundary controls; independent hostile replay |

The parent receipt scripts have different command interfaces: the totient
script uses a flag, whereas Oily/substrate require the receipt path after
`--verify`. An early invocation without that path was rejected by argparse;
the documented reruns passed. No failing mathematical receipt was overwritten.

The signed receipt is
[OILY_SIGNED_CERTIFICATE_RECEIPT.json](OILY_SIGNED_CERTIFICATE_RECEIPT.json).
The independent audit uses
[oily_hostile_oracle.py](oily_hostile_oracle.py) and
[OILY_HOSTILE_ORACLE_RECEIPT.json](OILY_HOSTILE_ORACLE_RECEIPT.json).
It checks 128 source states via three adapters, 220 transition-pair norms,
six exact beta/cumulant orders, and false source/constant controls. Finite
checks corroborate implementations; the universal mathematical statements
have their separate paper proofs.

During final review, `lru_cache`'s default numeric-key equality could bypass
the public exact-input type rejection after an equal Fraction was cached.
Both new caches were hardened with `typed=True`, and the existing invalid-input
test gained explicit float/bool alias controls. The eight focused tests and
the regenerated source-hashed signed receipt passed. Mathematical enclosures
were unchanged. The first unfinished full run is preserved as interrupted;
full discovery was restarted on the final hardened tree rather than reporting
the earlier imported code as final-tree validation.

The staged whitespace check finds only the interrupted raw log's final
`unittest` progress-space; that byte is preserved with the original log rather
than edited. The same check excluding that one raw log passes for all submitted
source, documentation, workflows and remaining receipts.

## Mandatory full and formal gates

See [formal/native gate record](OILY_FORMAL_VALIDATION.md) and its linked raw
receipts for commands, pinned revisions, source hashes, theorem expressions,
axioms, mutants, environment failures and the final full-discovery outcome.
Only nine branch-coercivity declarations are new. Supporting source/carry,
selected-phase, spectral-purity and π-source-genesis declarations are replayed
existing mathematics, not new results of this round.

The local Lean runtime uses a documented executable-path compatibility shim;
its compiler/kernel files are the hash-verified official pinned release.
Local qualified results and clean hosted results remain separately labeled.
The new narrow pull-request workflow checks the nine new declarations on
an ordinary GitHub runner and uploads its actual exports and mutation logs.

## Source/authority boundaries

No full analytic cancellation theorem is Lean-formalized. The cited
irrationality input, complex inverse lemma, asymptotic block count and
cumulant limits are paper arguments. No selected `o(N)` bound is claimed.
Finite receipts are not evidence that a specified asymptotic onset has been
reached. No external mathematical peer review is claimed.

Exact final commit, draft PR URL and hosted status are reported in the PR
and final delivery, after publication. A queued/running hosted workflow is
not recorded here as a passing check.
