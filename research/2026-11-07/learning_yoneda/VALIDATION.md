# Executed validation and exact authority

Pinned base: `d32342d375f44ddf62221ad6aff2f534abdc0a03`. New executable scope
is confined to `research/2026-11-07/learning_yoneda/`; the inherited package,
tests, source contracts and main-facing catalogs are unchanged.

| Check actually executed | Result | Receipt |
|---|---|---|
| Learning source lifts, categorical functor, residual memory and phase controls | 8 tests PASS | `validation/root_replay/learning.log` |
| Arithmetic finite authentication and clean prime epochs | 16 tests PASS | `validation/root_replay/arithmetic.log` |
| Spectral independent finite theorem checks | 7 tests PASS | `validation/root_replay/spectral.log` |
| Hostile exact controls | 4 tests PASS | `validation/root_replay/crucible.log` |
| Both arithmetic receipt generators, fresh output directory | PASS, byte-identical to retained receipts | `validation/root_replay/receipt_equality.log` |
| Spectral oracle | 15,495 exact checks PASS | `validation/root_replay/spectral_oracle.log` |
| Hostile oracle | 807 exact checks PASS | `validation/root_replay/crucible_oracle.log` |
| Lean4.14 finite decoder and C5 theorems | KERNEL PASS | `validation/root_replay/lean.log` |
| Required provenance verification | PASS, exit0 | `validation/verify_provenance.log` |
| Required observer-foundations probe | PASS, exit0 | `validation/observer_foundations_probe.log` |
| Required ordinal-SUCC report probe | PASS, exit0 | `validation/ordinal_succ_report_probe.log` |
| Required full native suite on unchanged pinned main package/tests | 12,147 tests PASS, exit0; 1809.685s unittest time | `validation/native_suite.log` and `validation/native_suite.json` |
| Pinned PR541,542,543 focused source replays | 31+21+32=84 tests PASS | `spectral/REPLAY_RECEIPT.json` and raw replay logs |

`validation/root_replay/replay.json` records every scoped command, exit status,
elapsed time and final Python/Lean source hash. The required probes have their
own exact command/timing receipt. These were actually executed in the isolated
worktree; they are not upstream CI claims.

The arithmetic holdouts certify 130,514 principal-part equalities, 542 2-adic
congruences, 1,084 independently generated states and 16 signed Weyl lower
bounds. The prime extension adds 1,836 clean principal-part checks, 1,224 complete
cycle points, exact interval weights and three positive signed covariance
lower certificates. These are exact rational inequalities, not floating-point
evidence of an infinite statement. See each preregistration and receipt.

The supplied theorem proofs, source replays and finite oracles have different
authority. PNT/AP and BK2003 are classical imports checked against cited author
sources. The new analytic/arithmetic paper theorems are not Lean formalized.
Lean checks only the explicitly scoped finite memory statements. Same-model
subagents with distinct implementations are not independent scholarly referees.

Environment: Python3.12.3; isolated virtualenv; mpmath1.4.1, numpy2.5.0,
sympy1.12, scipy1.18.0; Lean4.14.0. System mpmath1.2.1 was below the repository
minimum, so the required gates use the virtualenv; no global packages were
modified. Source-PR focused replays were performed separately from git archives
by the spectral agent, with their Python version recorded in its receipt.
All required local numerical gates cap BLAS/OpenMP concurrency at one.
The final paper-only PE14 corollary and scope clarifications do not change any
executed Python/Lean code. The replay's code hashes were checked against the
final worktree. The full native suite excludes this new research namespace;
its 35 focused tests are therefore reported separately.

No full suite is claimed for each read-only source PR. No hosted CI outcome is
inferred from local success. New main state is fetched before publication and
recorded separately; the pinned proof baseline is not rebased silently.

**π base-16 normality: OPEN. RH: OPEN.**
