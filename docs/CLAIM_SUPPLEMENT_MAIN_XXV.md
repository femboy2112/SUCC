# Main XXV — integration claims and governing corrections

**Authority:** written derivations, classical imports, exact finite certificates, kernel checks
and literature citations are separate and are labelled separately. This supplement adds no
normality, Goldbach or RH theorem. Contributed dossiers stay as their authors committed them;
where an independent audit found a defect in a contributed file that the integration did not
rewrite, **this document governs the interpretation.**

"PROVED PAPER" below means: a paper proof in the named dossier by one model, read once by a
separate read-only instance of the same model family with its own code. It is not external
review. "KERNEL" means Lean 4.14.0 with the pinned mathlib and the three standard axioms.

## 1. Integrated claims

| Scope | Definitions, hypotheses and quantifiers | Verdict and receipt | Next falsifier |
|---|---|---|---|
| Fejér / lag schedule (IAD-01, 02) | every bounded unimodular sequence; windows `1 ≤ L ≤ B` | PROVED PAPER: `√γ_L ≤ √γ_J + J/L`; the schedule cannot be the obstruction | a sequence violating the chain |
| Innovation calculus (IAD-03, 04) | four-pole forcing, lags `(2+δ)log_16 B ≤ ℓ ≤ (3−δ)log_16 B`; progression corollary for `1 ≤ q ≤ B−ℓ` | PROVED PAPER after two repairs (the corollary was false without occupied cells) | a shell violating (4.1) |
| History factor, gate (IAD-05, 06) | every seed | PROVED PAPER identity; sufficient gate PROVED CONDITIONAL with OPEN premise | — |
| Adelic no-go (IAD-07) | every odd prime `q`, horizon `K = 2B + t`, lags `1 ≤ d ≤ B−1` | PROVED PAPER after two repairs: identical data at all finite places `p ≠ q`, coherent completed orbit on the shell | a transfer argument that distinguishes the hijack seed |
| Saving–exponent law (ZSC-01; IAD-08) | every real `ξ`, one mode `h`, saving `η` on all shells `B ≥ B_0` | PROVED PAPER: `‖16^m ξ‖ ≥ c·16^(−((2−η)/(2+η))m)`; near-sharp | a point with a uniform saving and exponent above the bound |
| Digit-change rung (ZSC-02, 03) | every real `ξ`; zero seed for the carry form | PROVED PAPER two-sided inequalities; locality and renewal lemmas **KERNEL** | a shell violating an inequality |
| Run bounds (ZSC-04) | `π/16`, all `n ≥ 2` | PROVED PAPER from Mahler's `q^(−42)` (IMPORT, read at source): runs `≤ 41n` | — |
| Source moduli (ZSC-06) | sources `(g, s)`, proper form `deg g ≤ 7` | PROVED PAPER; null relation **KERNEL**; uniqueness of the null line uses Baker's theorem (IMPORT, **secondary sources only**) | a proper zero-seeded source off `Q·A_0` with rational completion |
| Limit faces (LMF-01…03) | every real `ξ` | PROVED PAPER; two strictness witnesses use classical imports | a witness on the wrong side |
| Thresholds (LMF-04, 05) | every probability measure on `[0,1]`; shells and prefixes of every orbit | PROVED PAPER: `1/4`, `1/60`, `1/(4(16^k−1))`; prefix `15/256`, `1/256` | a measure below a bound |
| Restricted transference (RDT-01…04) | every base `b`, multiplier `g`, linear form | PROVED PAPER | one violating instance |
| `log 2` at powers of two (RDT-05) | tilted family `(2,4,3)` | PROVED PAPER with the prime number theorem as import: `v_2(log 2) ≤ 2.3814`; recomputed independently to `n = 40`. **No novelty claimed**; `m_0` not explicit | `‖2^m log 2‖ < 2^(−2.39m)` for arbitrarily large `m` |
| `log(16/15)` (RDT-07) | Rivoal 2007 Theorem 1 (IMPORT, read at source); local extension to `g·16^m` | `v_16 ≤ 0.8813` COMPUTED FROM IMPORT (no interval enclosure); a digit change in every large shell PROVED PAPER given the import | a late shell of `log(16/15)` without a change |
| π at restricted denominators (RDT-06, 08) | seven Gaussian one-pole families, `n ∈ {12, 18}` | **OBSERVED**: no gain; shadow lemma and minimal-modulus lemma PROVED PAPER; `v_2(1/π) ≤ 3.11` CONDITIONAL | a convergent family with a π-side imbalance |
| Prime fixed-point observers (#601 at `836d0380`) | divisibility category; lazy lambda program; twisted cylinder | PROVED PAPER within the declared models (PFO-01…13, CYL-01…10), re-derived by the integration audit; several items are classical (§3) | see the dossier's ledger |
| Prime fixed-point cylinder, Scott-relative defect, carrier (#600 at `8bf797d7`) | reduced divisor coproduct; factorisation trees; CRT–Haar certificates | PROVED PAPER within the declared algebraic model, re-derived with explicit matrices by the integration audit; corrections in §3 | see the dossiers' ledgers |
| Statistical frontier | literal zero seed, every fixed nonzero mode, all large shells | R0, R1, (CH), signed cancellation, parity, π normality: **OPEN**. Goldbach, completed-Weil positivity, RH: **OPEN** | a source-derived all-shell estimate, not a table |

## 2. Corrections to earlier statements of the same programme

These supersede the corresponding sentences wherever they still appear in older files.

1. **"(CH) is the weakest statistical statement of the signed family" is false.** A fixed saving at
   mode 1 is strictly weaker; the bottom rung is R0 (`limsup Re W_B(1) < 1`). (CH) remains the
   first *hexadecimal density* rung and keeps everything proved for it.
2. **"L2 and L3 are open for algebraic numbers as well" is false for L2.** A digit change in every
   large shell holds for algebraic irrationals by Ridout's theorem (ineffectively).
3. **The recollection "`‖2^k log 2‖ ≥ 2^(−0.79k)` (Rhin 1987)" was false**; the constant belongs to
   `‖(3/2)^k‖`. No use was ever made of it.
4. **Provisional thresholds of the 2026-11-12 preregistration:** `4/225` for `W_1` is false (the
   proved value is `1/60`; shell measures also approach the lift `1` of the fixed point `0`); the
   prefix value `1/120` is not the extremum (`1/240` is).
5. **IAD-04 progression corollary and IAD-07** were each false or incomplete as first written and
   were repaired twice; the statements in THEOREMS.md as merged are the governing ones, and the
   stale copy in OBSTRUCTIONS O-2 has been replaced.
6. **Unrefereed 2026 claims** (`μ(π) = 2`; `μ(log α) = 2`; `μ(π) ≤ 7.1019`) are CLAIMED /
   UNVERIFIED, are not imported, and by ZSC-01 could not yield a saving even if correct.

## 3. Governing corrections to contributed dossiers (not rewritten)

Found by read-only integration audits of the pinned snapshots. None affects a proof.

### `research/2026-11-12/prime_fixedpoint_cylinder`, `carrier_first_goldbach`, `prime_interferometer_legacy`, `scott_relative_defect` (#600 at `8bf797d7`)

1. **Explicit Chen threshold.** `prime_fixedpoint_cylinder/THEOREMS.md` and `README.md` quote
   "`2n > exp(36)`". The explicit versions in the literature are double-exponential:
   `exp(exp(32.7))` (Bordignon–Johnston–Starichkova, arXiv:2207.09452), improving Yamada's
   `exp(exp(36))`; the cited 2022 item is a thesis abstract. Only "sufficiently large" is used by
   the dossier. A single-exponential threshold would, with the known numerical verification, make
   the corollary unconditional for all `n`; nothing supports that.
2. **`carrier_first_goldbach/README.md`**: "Goldbach ⇔ `G ≥ I` ⇔ `ker G ∩ H_even = 0`" must be read on
   `H_(even, ≥4)`, the closed span of `|N⟩` with `N` even and `N ≥ 4` (`R(2) = 0`).
3. **Labels without code behind them.** `MIXED_COUPLING.md` "Finite check (OBSERVED)" for the defect
   operator `D`: no code constructs `D`; read as "paper derivation; the committed test checks `R(N)`
   only". `SHANNON_CARRIER.md` "exhaustively enumerated (OBSERVED)": the enumeration script is not
   committed; read as "closed-form values".
4. **Ledger gaps.** `carrier_first_goldbach/CLAIMS.md` has no rows for CARR-09 and for the defect
   identity; they are PROVED PAPER (re-derived by the audit). That directory and the legacy note do
   not state that RH and π normality are OPEN; they are.
5. **`prime_interferometer_legacy/RESEARCH_NOTE.md`** (an archival original, deliberately not
   edited): "not committed to SUCC" is now stale; the audit script checks lower bounds and counts,
   not upper certificates (the upper bounds were recomputed and are correct); "subadditivity of
   min" should read "superadditivity"; the singular series is CLASSICAL (Hardy–Littlewood), not
   PROVED LOCAL.
6. **Convention.** `|1⟩` is called "primitive" in the sense of the dossier's reduced coproduct; in
   standard Hopf-algebra usage it is group-like.
7. **Tests that cannot fail** and therefore are not evidence: the flat-plaquette test (a telescoping
   sum), the Hilbert–Schmidt test (re-implements the formula under test; the identity itself was
   confirmed with explicit matrices), five hard-coded fields of `carrier_first_goldbach/RECEIPT.json`.
   Two documented regeneration commands add a trailing newline that the committed
   `SCOTT_RESULTS.json` and `RECEIPT.json` lack.

### `research/2026-11-12/prime_fixed_point_observer` (#601 at `836d0380`)

1. **Classical antecedents** of items labelled PROVED LOCAL: the Fréchet–Hoeffding bounds (PFO-11),
   composite runs `n!+2, …, n!+n` (CYL-04), the parity law `R(2n) ≡ 1_P(n) (mod 2)` (PFO-09).
2. **Lambda observer (PFO-04).** The implemented evaluator is call-by-name without sharing, so
   stream heads are unevaluated successor chains; termination is unaffected, contraction counts
   grow superlinearly (1 986 / 14 929 / 44 018 / 114 586 delta steps for 10 / 20 / 30 / 40 primes).
3. **Wording.** "The finite Goldbach resolvent trace" is a fixed-sum pair-count resolvent trace, an
   exact recoding of `R(N)`, not a Goldbach estimate. "A certified equivalence between
   computational paths" (CYLINDER.md) is an operator identity (coprime multipliers commute), not a
   certificate-checker result.
4. **Protocol order.** The repository history does not evidence that the protocol preceded the
   code: protocol, code and receipts were committed together.
5. **Tautological assertions** (harmless, not evidence): listed in the integration audit record;
   several fields of `CYLINDER_REPORT.json` are constants written by the script.

Both pull requests received further commits after the pinned snapshots. Those commits are not
integrated, were not audited, and remain in their open pull requests.

## 4. What Main XXV does not claim

No estimate for the zero-seeded source at any mode; no evidence for R0, R1 or (CH) from finite
shells; no restricted exponent for π below the unrestricted record; no novelty for any statement;
no external review; no kernel authority beyond the listed exact lemmas; no proof or partial proof
of Goldbach, π normality or RH.
