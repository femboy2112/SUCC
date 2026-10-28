# Oily carry research: validation and finite formal authority

This record concerns the research tree descended from PR #310,
`a8c7c85b7a1900d422090f1757c174e7aac69f44`. The exact source remains
the imported four-pole BBP recurrence with zero initial state. Formal checks
below certify only their displayed finite statements, not base-16 normality.

## Newly checked finite proof core

[`formal/OilyBranchCoercivity.lean`](../../formal/OilyBranchCoercivity.lean)
contains nine declarations used by the direct arithmetic dossier:

- coefficient squared norms 546 and 514;
- adjacent and separated quadratic bounds, obtained from explicit sums of
  squares;
- phase square below `1/225` from `8*q^2 <= loss <= 1/29`;
- the exact rational Taylor and branch-separation margins;
- coercivity consequences from explicitly assumed gap and energy estimates.

The exact positive coercivity margin is

$$\frac{19}{546}\left(\frac{4081}{4096}\right)^2-\frac1{29}
=\frac{2329025}{37950062592}>0.$$

The [checker](../../scripts/check_oily_branch_coercivity_lean.py) verifies the
repository Lean and mathlib pins, clean tracked dependency trees, every declared
theorem's exact exported type and axioms, and source hashes before/after the run.
It rejects added proof-authority tokens. Four deliberate mutations must fail for
mathematical reasons: squared norms reduced to 545 and 513, a dropped small-loss
premise, and a false rational equality. **Final local result: nine exports and
all four rejected mutants, `KERNEL_CHECKED`.**

The transcendental chord estimate, branch extraction from the authentic BBP
orbit, irrationality-measure input, block counting, and all infinite-limit
claims remain paper-level obligations. The Lean file does not certify them.

## Local runtime and reproducibility boundary

Python uses the recovered declared-dependency environment, Python 3.12.14,
mpmath 1.3.0 and SymPy 1.14.0, with `PYTHONPATH` set to the repository root.
The bare runtime Python lacked mpmath; its failed targeted test/ordinal outputs
are preserved as environmental failures, not rewritten as passes.

Lean is the unmodified official 4.14.0 release, compiler commit `410fab728470`.
The downloaded release archive has SHA256
`320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`.
Mathlib is pinned to `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`; every
transitive source revision is checked against the repository manifest.

As documented by earlier source-carry validation, this host does not resolve
Lean's numerical current-process executable alias. The local run used the
existing narrowly scoped executable-path compatibility shim, translating only
that current-process query to `/proc/self/exe`. The compiler, kernel and
dependency sources were not edited. The complete shim source and hashes appear
in the runtime note. Local receipts are therefore explicitly **shim-qualified**;
they are distinct from a clean hosted run.

The new [targeted workflow](../../.github/workflows/oily-branch-coercivity.yml)
runs only on changes to the new formal source, its checker, or the workflow
(plus manual dispatch). It verifies the official archive hash, uses the pinned
dependency manifest, and uploads clean-host theorem/axiom/mutation receipts.
No hosted result is asserted until that workflow finishes at the submitted head.

## Replayed supporting formal gates

| Gate | Local result | Actual scope |
|---|---:|---|
| [SourceFaithfulCarry](oily_carry_validation/source-faithful-carry-lean.json) | 22 exports, 5 rejected mutants | Finite source coordinates and future-safe carry reconstruction |
| [SelectedPhase](oily_carry_validation/selected-phase-lean/kernel-observation.json) | 8 exports, 3 passing positive/negative pairs | Backward finite telescope and conditional block-deficit algebra |
| [SpectralPurity](oily_carry_validation/spectral-purity-lean-final/kernel-observation.json) | 10 exports, 2 passing positive/negative pairs | Finite signed kernel identities and explicitly conditional energy estimates |
| [PiSourceGenesis](oily_carry_validation/pi-source-genesis-lean/kernel-observation.json) | 41 exports, 4 passing positive/negative pairs | Original finite source/jet algebra; supporting BaileyCrandall, BBPIntegral and PiSource modules compile |

The [new final coercivity receipt](oily_carry_validation/oily-branch-lean-final/kernel-observation.json)
adds nine exports and four rejected mutants. In total these runs export 90
declarations across five separately scoped lanes and reject 18 mathematical
false controls. These counts do not enlarge any theorem's stated scope. The
[runtime note](oily_carry_validation/lean-runtime-note.json) records the common
local compatibility qualification.

The first SpectralPurity attempt found a missing pinned `Positivity.olean`
cache file. Downloading that exact pinned cache resolved it; no source or
expectation changed. Archive extraction also required `--no-same-owner` for
this container's user mapping. These were configuration corrections.

## Native validation status

Baseline provenance verifies 72 entries: 17 byte-identical archives and 55
mechanical namespace migrations, with source commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a` unchanged. Observer foundations and
ordinal report probes exit zero. The inherited Oily totient module passes all
16 native tests. The historical theorem-registry module passes all six tests,
including the previously missing immutable-blob check.

The first combined discovery was deliberately interrupted (exit 130) after
5,278 passing markers. Principal review found that untyped `lru_cache` could
reuse an exact-rational cached value for an equal floating-point input before
the input guard ran. The two cache decorators now use `typed=True`, and four
regression assertions were added to the existing invalid-input test. The
interruption was a validation reset after a real API edge was fixed, not a
mathematical failure and not a completed passing suite. The
[interruption record](oily_carry_validation/full-unittest-interruption.json)
preserves the exact two changed file hashes; the original
[partial log](oily_carry_validation/full-unittest-interrupted-before-cache-hardening.log)
is retained. A separate [cache-alias replay](oily_carry_validation/cache_type_independent_control.py)
re-wraps the original functions with deliberately untyped caches and reproduces
both invalid aliases, while the final typed caches reject them. Its
[raw result](oily_carry_validation/cache-type-independent-control.log) matches
an independent one-shot execution byte for byte.

A fresh full combined discovery was started after the production/test tree was
frozen again. **Final result: 8,844 tests passed in 1,146.182 seconds, exit 0,
with no failures, errors or skips.** All 34 newly added tests passed in this
same final run. Its [before-run snapshot](oily_carry_validation/python-final-source-snapshot.json)
hashes 1,697 Python source files; the exact file set and every hash were
unchanged at completion. The [final summary](oily_carry_validation/full-unittest-final-summary.json)
records the exit status, count, duration, stability comparison and log hash.
The complete [raw log](oily_carry_validation/full-unittest-final.log) has SHA256
`715e51dc024544a9d4a86452cc4c5d43ab2db5710a0a649bfccbfaeeef751017`.

The provenance, observer-foundations and ordinal probes were also replayed
after the cache fix: all exit zero and their outputs are byte-identical to the
successful baselines. Those outputs are retained as
[`provenance-post-cache.log`](oily_carry_validation/provenance-post-cache.log),
[`observer-post-cache.log`](oily_carry_validation/observer-post-cache.log) and
[`ordinal-post-cache.log`](oily_carry_validation/ordinal-post-cache.log).
All mathlib-lane receipt source hashes still match the final working tree.
The source-genesis formal replay has completed as tabulated. Hosted CI remains
a separate exact-head gate and is not asserted by these local receipts.

The principal also mutated the signed finite receipt to assert
`infinite_cancellation_proved=True`. Verification rejected it with exit 1 and
`RECEIPT_MISMATCH`; the [small control record](oily_carry_validation/signed-receipt-mutation-control.json)
is preserved. This is a receipt-authentication control, not a mathematical
disproof of any infinite conjecture.

**Authority boundary:** all numerical experiments remain finite. A fresh local
formal receipt is a reproducible observation of the pinned kernel, not an
automatic update to the historical proof-authority catalogue. No declaration
here proves the analytic cancellation theorem or normality.
