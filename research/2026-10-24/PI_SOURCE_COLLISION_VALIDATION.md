# Source collision research — execution and validation record

**Date:** 2026-10-24. **Parent:** `de005af44cb4592d7a8be73f46fa1983f627da27`.
**Branch:** `research/pi-source-collision-entropy-2026-10-24`.

## Actual local runs

| Gate | Observed result |
|---|---|
| Parent Poisson focused baseline | 27 tests passed |
| New source collision focused suite | 13 tests passed, including exact source/carry/Machin controls |
| Full repository suite | **7,414 tests passed in 596.811 seconds**, exit 0 |
| Final namespace guard after additive SCE registration | 15 tests passed |
| Source provenance verifier | `SOURCE_PROVENANCE_VERIFIED`, 72 items, 17 byte-identical archives, 55 mechanical namespace migrations |
| Observer foundations probe | exit 0 |
| Ordinal source report probe | exit 0 |
| Main collision receipt replay | byte-for-byte `cmp` passed |
| Independent Galois oracle | 12 exact comparisons between direct all-pair and pair-grid aggregations; mutation rejected |
| Independent regret oracle | 6,240 potential inequalities, 780 energy identities, 2,150 one-step bounds; both mutations rejected |
| Python compilation and diff whitespace checks | passed |

Environment: Python **3.12.14**; mpmath **1.3.0**, NumPy **2.5.4**, SymPy
**1.14.0**, SciPy **1.18.1**. Dependencies were installed into an isolated
environment from the repository's declared ranges. The complete suite ran
with an explicit importable checkout (`PYTHONPATH`), as required by the known
subprocess-package-path contract documented in #250.

The production module and test source were unchanged during/after the full
suite. Final prose, navigation, handoffs, and the additive namespace registration
were completed while it ran; the namespace guard was separately rerun after
that edit. No claim is made that this local run occurred at a preexisting Git
commit. The committed exact receipt records the tested source file hashes.

The full and focused run logs are preserved alongside this record. Existing
upstream Python docstring escape warnings did not cause test failures. No
unrelated production change was made to suppress them.

## Mathematical review

The root researcher derived/audited the entropy and carry bridge, independently
checked the Galois/grid and prime-order arguments, and verified the primary
BBP, hot-spot, prime-progression, and computability references. Separate
constructor and adversary reviews checked the complete conditional chain.
The review repaired a strict inequality at the first source sample and added
the moving-window version of the de Bruijn strictness countermodel. An
integration reviewer caught the missing `M→∞` hypothesis in a handoff summary.

These reviews used the same model family and shared source material. They are
not independent probabilistic witnesses. The exact implementations use different
finite aggregations, and the π bin check uses the independent Machin identity;
all still depend on their stated mathematics and software execution assumptions.

**No new Lean declaration was written or checked.** Paper proofs, finite
receipts, and inherited kernel checks retain separate authority. The selected
source estimate `K_p(1)=p^{o(1)}` has not been proved or certified by any run.

## Donor heads versus this delivered branch

`PI_SOURCE_COLLISION_DONOR_SNAPSHOT.json` records the live PR/branch snapshot
and a fresh 2026-10-24 07:35:13 UTC query. All returned workflows for #250 and
the seven pre-round leaf heads #255/#259/#260/#261/#262/#263/#264 were successful,
including #264's broad validation run `40072804352`.

Those donor checks are not validation of a future combined main. The Claude
handoff requires review and full checks on the actual combined tree before
using Leah's merge/cleanup authorization.

At the time this local record is committed, this new research commit has not
yet completed hosted CI. Its draft PR description and GitHub Actions provide
the subsequent exact-head status. This temporal statement must not be read as
a green-check claim or as a request to rerun every donor workflow unnecessarily.

## Reproduce the new finite work

```sh
python -m unittest discover -s tests -p 'test_pi_source_collision.py' -v
python scripts/pi_source_collision_probe.py --output /tmp/pi-source-collision.json
cmp /tmp/pi-source-collision.json research/2026-10-24/PI_SOURCE_COLLISION_RECEIPT.json
python scripts/pi_source_collision_galois_oracle.py
python scripts/pi_source_collision_regret_oracle.py
```

The receipt includes exact selected-source windows at p=1009 and p=2017 as
fresh larger holdouts. Diagnostic resolutions and the fixed c=2/5 schedule
are labeled separately. No finite fitted exponent is claimed.

**Earned verdict:** explicit paper proof steps, a complete conditional
normality implication, exact finite calibration and a coherent integration
handoff. **π normality and its independence remain open in this work.**
