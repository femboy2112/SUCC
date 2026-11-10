# Validation record and execution limits

Validation was executed on 2026-11-10 UTC, continuing the November 9 research
round. Mathematical authority is in CAYLEY_PROOFS, BOUNDARY_PROOFS,
AFFINE_SOURCE_ACTION and SEMANTIC_AUDIT. Passing tests do not prove the
original-zero signed estimate or the missing C-monoid compiler.

## Baseline and repaired scope

At PR #576 head `afabc458323ef2e3a20ce2bae77239c4190819c5`, the selected
source-weld, lambda, omega, Scott, lag and parity-Fourier suite passed **46
tests** despite the reproduced defects. The narrower semantic set contained
27 passing tests. Provenance, observer-foundations and ordinal probes passed.

The repaired combined focused suite passes **108 tests**: 18 Cayley,
47 semantic, 33 parity-boundary/Fourier/lag/seed-separation, and 10 signed
covariance tests. These are the counts actually executed, with the complete
command and output in [FOCUSED_TEST_LOG.txt](FOCUSED_TEST_LOG.txt).

## Required native integration gates

**Final clean run: PASS — 12,946 tests in 1052.897 seconds, with zero failures
and zero errors, on Python 3.12.14.** This is the completed post-install run.
The tested Python files remained byte-identical throughout it; final result
documentation and catalog hashes were checked after recording the outcome.

The required command is

```sh
python -m unittest discover -s tests -p 'test_*.py'
```

Its clean post-install outcome is recorded in
[FULL_TEST_RESULT.json](FULL_TEST_RESULT.json), with the complete unedited
[FULL_TEST_LOG.txt](FULL_TEST_LOG.txt). The tested Python contents are bound
by [TESTED_SOURCE_HASHES.json](TESTED_SOURCE_HASHES.json); the published tree
is checked against those hashes. The result receipt distinguishes PASS from
any incomplete or failing run; a progress log alone is not a pass.

The first completed integration run exercised **12,946 tests in 1058.363s**
and reported exactly **one error**, preserved in
[FULL_TEST_PREINSTALL_LOG.txt](FULL_TEST_PREINSTALL_LOG.txt). A subprocess
could not import `observational_succ` because this fresh checkout had not
been installed as a package. Direct execution reproduced `ModuleNotFoundError`.
The standard local editable install, without dependency downloads or build
isolation, corrected the environment. The previously failing case then passed;
see [installation](EDITABLE_INSTALL_LOG.txt) and
[targeted recheck](ENVIRONMENT_RECHECK_LOG.txt). A fresh full run follows this
repair; the earlier failed run is not silently relabelled green.

An even earlier full attempt was deliberately interrupted before the additional
covariance repairs were frozen. Its partial log is retained in
[FULL_TEST_INTERRUPTED_LOG.txt](FULL_TEST_INTERRUPTED_LOG.txt) and is not a result.

The other required gates have their own successful raw receipts:

- [Provenance](PROVENANCE_LOG.txt): 72 imported items verified, including 17
  byte-identical research archives and 55 mechanical namespace migrations.
- [Observer foundations](FOUNDATIONS_LOG.txt): PASS within the probe's scope.
- [Ordinal successor](ORDINAL_LOG.txt): PASS within the probe's scope.
- [Memory catalog](CATALOG_CHECK_LOG.txt) and [typed graph](GRAPH_LOG.txt):
  reproducible build and 51 nodes/60 edges checked. The 170 inherited namespace
  warnings are retained; no new historical namespace is minted.

## Exact finite certificates

The parity probe was frozen at local commit `3f702b95` before its output was
read. The remote preservation commit `55c8d55470ba28ab8fb169079e5b5e00bf356f9b`
has the identical Git tree `e43d9da91aa20128ec73fbac983d8d5c04a36f68`.
Remote publication took place after execution; this is not a claim of a prior
server timestamp. [PROTOCOL.md](PROTOCOL.md) fixes the parameters. No parameter
was selected using the observed parity response, and no runner/source-code
correction was needed after this frozen experiment was started.

[FINITE_RECEIPT.json](FINITE_RECEIPT.json) passes every exact containment,
recurrence and hostile-control check. The completed fractional-digit parity
means are 5/257 and 23/509. The rigorous Fourier-reconstruction intervals are
approximately [-0.42901,0.46011] and [-0.45411,0.54099], respectively; these
wide intervals establish no useful asymptotic signed saving. They validate
that the numerical readout and its separate error payments are sound.

The reported boundary-recursion rows are defined on the **finite common-horizon
lower endpoints**. A later independent interval replay also separated all their
arc memberships from the completed source for these finite cases; that replay
has its own receipt and is not silently inserted into the frozen protocol.

The separately developed [affine source probe](affine_source_probe.py) has
[its own receipt](AFFINE_SOURCE_RECEIPT.json): 180 direct source/seed/completion
checks per listed family, 1,620 compositions, 20 affine-relation cases and
four false-fixed-iterate controls. It was not part of the earlier parity
preregistration. Its universal claim rests on the explicit conjugacy proof.

## Independent bearings and reproducibility

Separate assignments constructed and reviewed the proofs. These used the same
model family and shared repository provenance; they are not independent
external referees. Different failure mechanisms include named-variable and
direct-environment semantics versus de Bruijn substitution, generic ASTs
versus compressed omega paths, binomial powers versus projective squaring,
four-pole versus combined-polynomial arithmetic, and sixteen-preimage counts
versus the two-fiber recurrence.

Current replay scripts, raw outputs, versions and source hashes are in
[review_probes](review_probes/README.txt). The original semantic review found
an additional exact-carrier issue; that was repaired and its rejection is
confirmed by the current replay. The original sine/orbit review script was
not retained, so a [clearly labelled reconstruction](review_probes/README.md)
was executed on the declared grids. It passes 3,230 sine diagnostics and
2,145 exact orbit recursions. The original 1,750-case Fejer grid/stdout remain
unavailable and were not reconstructed merely to reproduce a count.
High-precision sine/Fourier comparisons are diagnostics; the rational Taylor
proof supplies certification.

## Hosted and formal scope

Local runtime: **Python 3.12.14**. This is distinct from hosted Python 3.10/3.13
execution. All 20 checks at the audited **parent** head were successful when
rechecked; [PARENT_CI_SNAPSHOT.json](PARENT_CI_SNAPSHOT.json) records their exact
head and links. They do not certify this follow-up head, and their earlier
success did not exclude the reproduced mathematical defects.

No new Lean proof was added or compiled locally. The three inherited small
Lean files were inspected for scope; their stronger interpretations are
withdrawn in ERRATA.md. Paper proofs, finite exact receipts, high-precision
diagnostics and kernel checks retain different authority. No merge or
promotion of normality, parity balance or RH follows from this record.
