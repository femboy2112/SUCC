# Source map and provenance

**Repository baseline:** Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`
(`origin/main` at branch creation, 2026-11-11). Additive dossier; no frozen source, provenance
manifest, Lean file or existing dossier is modified.

## Frozen source

- Forcing: `observational_succ.selected_orbit.original_forcing` → `duck_bbp.forcing` (reused, never
  redefined; `iad_core.r`). Literal seed `U_0 = 0`. Carries: `C_n = ⌊U_n⌋`, `κ_n = C_n - 16C_(n-1)`
  as in `observational_succ/integer_bbp_carrier.py` and the frontier contract.
- Completed identity `U_n + T_n = 16^(n-1)π`: classical BBP (Bailey–Borwein–Plouffe 1997), imported
  as in `docs/PI_NORMALITY_FRONTIER.md` §1.

## Internal results reused (by reference, not re-proved unless stated)

| Result | Location | Use here |
|---|---|---|
| Handoff lag interface `R_(B,L,h)` and (1.2) | `docs/MAIN_XXIV_HANDOFF.md` §4 | re-derived in IAD-01 |
| SP-01 fixed-lag reduction, NON-IMPROVEMENT | `research/2026-10-30/arithmetic_barrier/SPECTRAL_AND_SELECTION.md` | extended by IAD-02 |
| LL-01/LL-02 two-index sheet, near-pair energy | `research/2026-11-10/gaussian_circle_long_lag/LONG_LAG.md` | IAD-03a equivalence; SWT-05 instance B |
| CG-01 `log den(U_n) = 6n + o(n)` | `research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md` | height in IAD-07/08/09 |
| PPP-08 odd-denominator coherent counterseed | `research/2026-11-09/pi_parity_pressure/PROOFS.md` | generalized by IAD-07 |
| AT-07 seven-pole null source | `research/2026-10-30/arithmetic_barrier/arithmetic/ARITHMETIC_THEOREMS.md` | "necessary, not sufficient" control |
| RIO-09/10/11 carry-language constraints | `research/2026-10-29/inertial_origin_q6/INERTIAL_ORIGIN_Q6_CARRY.md` | SWT-03 context; IAD-08 calibration |
| RS-04 odometer entropy obstruction | `research/2026-11-06/adelic_return_bridge/THEOREMS.md` | SWT-06 |
| D-2 cofinal schedules | `research/2026-11-09/scott_omega_causal_weld/SCOTT_COFINAL_SCHEDULE.md` | SWT-05 domain reading |
| Integer-carry cocycle `d_n = κ_(n+1)+ε_(n+1)-16ε_n` | issue #580 / PR #579 dossier | re-derived in SWT-03 |

## External literature

Checked on 2026-11-11 by a delegated web search (same-model helper; this is a citation check, not
refereeing). "Seen" = the cited statement was read in the source or in a faithful transcription.

| Fact | Citation | Check |
|---|---|---|
| `μ(π) ≤ 7.103205334137…` | D. Zeilberger, W. Zudilin, *Moscow J. Combin. Number Theory* 9 (2020) 407–419; arXiv:1912.06345 | confirmed; best **refereed** bound found |
| `μ(π) < 7.101862832357` | Y. Bai, arXiv:2609.11276 (2026) | **unrefereed claim**; not imported |
| `μ(π) = 2` | preprint with Lean formalization in the `openai/math` repository (2026) | **unrefereed claim**; the helper scanned the sources but did **not** build or kernel-check them; not imported |
| Exponents `v_b`, `v'_b`; `v_b = v_(b^t)`; `μ - 1 ≥ v'_b ≥ v_b` | M. Amou, Y. Bugeaud, "Exponents of Diophantine approximation and expansions in integer bases" (author PDF read; journal details UNVERIFIED) | seen |
| No improved `v_2(π)`/`v_16(π)` or run-length bound for π | — | none found (absence by search; medium-high confidence) |
| Complexity of expansions under small `μ` | B. Adamczewski, *Math. Ann.* 346 (2010) 107–116; Y. Bugeaud, D. H. Kim, *Ann. Sc. Norm. Super. Pisa* (5) XVII (2017) 931–947 | seen; inapplicable to π at `μ ≤ 7.10` |
| Kusmin–Landau with constant `cot(πθ/2)` | E. Landau, *Nachr. Ges. Wiss. Göttingen* (1928) 21–24; R. Kuzmin (1927); exposition J. Arias de Reyna, arXiv:2002.05982 | seen via the exposition; IAD-04 contains its own proof |
| van der Corput `k`-th derivative test | S. W. Graham, G. Kolesnik, *Van der Corput's Method of Exponential Sums*, LMS LN 126 (1991), Thms 2.2, 2.8 | **book not seen**; import used only in the non-load-bearing extension of IAD-04 |
| Normal numbers are Π⁰₃-complete | H. Ki, T. Linton, *Fund. Math.* 144 (1994) 163–179 | confirmed |
| Normality under rational affine maps | D. D. Wall, PhD thesis, UC Berkeley (1949) | attributed; thesis not seen |
| Finite-automaton selection | V. N. Agafonov, *Dokl. Akad. Nauk SSSR* 179 (1968) 255–256 | confirmed citation |
| Finite-state dimension and normality | C. P. Schnorr, H. Stimm, *Acta Inform.* 1 (1972) 345–359; J. Dai, J. Lathrop, J. Lutz, E. Mayordomo, *Theoret. Comput. Sci.* 310 (2004) 1–33 | confirmed citations |
| Finite-state dimension and real arithmetic | D. Doty, J. Lutz, S. Nandakumar, *Inform. and Comput.* 205 (2007) 1640–1651 | confirmed citation |
| Prime number theorem in arithmetic progressions (fixed modulus 8) | classical; as cited in CG-01 | import in IAD-09e only |

The orientation citations in SWT-06 (Wall, Agafonov, Schnorr–Stimm, Dai et al., Doty et al.) are
not used in any proof. Korobov's incomplete-sum bound was checked but is not used in this dossier.

## Authorship and independence

All derivations are by one model family in one session, with a same-model adversarial audit
(recorded in [VALIDATION](VALIDATION.md)). That is neither external peer review nor kernel
verification. The maintainer's Scott-transport thesis is quoted verbatim in SCOTT_TRANSPORT.md and
kept separate from the mathematical statements that test it.
