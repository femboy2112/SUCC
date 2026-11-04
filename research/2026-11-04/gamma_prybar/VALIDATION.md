# Validation and reproduction

Runtime: CPython 3.12.14, Git 2.52.0, mpmath 1.3.0, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. All new files are additive and scoped to this directory. All thresholds that use PNT or unspecified analytic constants are proved symbolically. Observations at small epochs have a different meaning from the growing q_A schedule.

## Research payload

Run from repository root:

```sh
python research/2026-11-04/gamma_prybar/replay.py
```

19/19 core JSON receipts matched. The replay runs isolated processes and compares parsed JSON. It includes direct four rational fractions, the collapsed source polynomial and a separate LCM/integer/carry reconstruction, modular versus gcd clocks, explicit rational tail enclosures, interval character evaluations, and actual positive and negative controls. Output is in [replay.txt](validation/replay.txt). The optional, slower denominator-only extension replays with `python cofactor_probe.py 1536 2048` in front1; both individual epoch evaluations were also run. Raw receipts and probe specifications are next to each implementation. Retain initial failed sufficient certificates and exploratory extensions separately.

| Probe | Exact scope |
|---|---|
| Principal reset and packing | 533 state denominators and prefix LCMs; 139 first-pole checks. A=91,211,367 at w=A^-3, including independent brute-force ordered-pair counting at 91. |
| Original/alias fiber and angular discriminator | Four silent-prime holdouts, two exhaustive small fiber means, mixed-denominator checks at 157,293,503, and denominator-only capacity successes and failures. |
| Checkpoint and cross-time heights | 1,281 direct divisibility checks, geometric clock counts, all 684,437 unordered pairs in three controls, direct reduced-difference cross-checks and lag rectangles. The bounded exceptional-lag theorem rests on the paper proof. |
| Valve and sparse reset | Three fixed-mesh epochs. Both lookahead and causal variants through time 602, including 43 resets, 499 born-prime windows and a nonunit mutant. |
| Signed Fourier | Six preregistered epoch/character pairs, 5,924 unwrapped affine identities and 2,872 checks of the exact increments. The signed means are interval diagnostics. |
| Radial | Direct and compressed rational sources, 303 lift comparisons, finite exceptions; 116,934 modular-vs-rational loss checks and 18,306 one-pair divisibility guards. Extra two-band guard checks reuse development data. |
| Hostile and ternary | 16 source-family subset comparisons; lookahead and causal controls, finite normal-looking continuation, constant/periodic controls, omitted-prime constructions. Exact ternary table checked against Fraction through 333 and modular chronology through 180,001. |

## Source baseline and donor replay

The initial exact main commit and all donor SHAs are in [SOURCE_MAP.md](SOURCE_MAP.md). On the main source checkout these commands were actually run:

```sh
python -m unittest discover -s tests -p 'test_integer_bbp_carrier.py'
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The focused baseline passed 15 tests. Provenance verified all 72 entries and both other probes exited zero; raw JSON is under validation/. The full native discovery was launched once on the pinned main checkout while this separate research dossier was being developed. The main source, tests and workflows are byte-identical on the draft branch. The final local native result and any hosted results are reported separately on the integration PR with their SHA and run identity. The research-only core replay is separate from native discovery.

Detached donor worktrees were exact Git checkouts. For each row, the command was `python -m unittest` on modules selected under tests/ by the indicated filename prefix(es).

| PR | Prefix | Passed |
|---|---|---:|
| #491 | test_renorm_transport | 13 |
| #492 | test_alias_valve, test_source_native, test_sharp_shear | 25 |
| #495 | test_source_sound | 21 |
| #496 | test_analytic_exile | 21 |
| #497 | test_frobenius_prime | 18 |
| #498 | test_gamma_pigeonhole | 17 |

The 115 donor tests have six raw logs under validation/. PR #499 added three Markdown files to #497; 26 additional tests passed in the isolated ZIP extraction. The archive SHA and test log are in SOURCE_MAP.md. Hosted runs on donor SHAs do not certify the integration SHA, and local runs confer no hosted status. No new Lean authority.

Main's #485/#487/#488/#489 descendant tests were also exercised by their five named modules (odd_gamma_front, odd_gamma_symbolic, oily_shear, circle_path_electric, selected_current_front): 72 passed, [log](validation/main_ancestry.txt). At the newly appeared #500 SHA the restored primal tests and Europa research entrypoint passed, [log](validation/pr500.txt). The local archive and restored native runs are separately identified and share their underlying 26 tests.

The native discovery run initially had the repository on the current interpreter's working-directory path but lacked the editable package needed by child script processes. The meta_choice_descent subprocess therefore raised ModuleNotFoundError. After installing the local checkout in editable mode with the already-installed test dependencies, the exact failed test passed. The discovery process continued; its raw final exit and explicit reruns are tracked on the PR instead of restarting the full matrix on each documentation change.
