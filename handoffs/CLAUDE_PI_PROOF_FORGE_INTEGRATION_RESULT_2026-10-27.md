# CLAUDE — π Proof-Forge Integration & Hostile Audit RESULT (2026-10-27)

Independent integration + firewall audit of **PR #324** (`research/pi-selected-boundary-crt-finite-spectral-2026-10-27`, head `fca58d3e`) and its inherited chain #317/#319–#323. Child audit branch: `research/pi-proof-forge-integration-audit-2026-10-27`. **No merge, no source rewrite, no claim promotion, no Lean authority over the infinitary target.** π base-16 normality and RH remain **OPEN**.

## Verified ancestry (linear, 16 commits, zero merges)

```
main 6dd80730
 → #306 7989be57 → #309 8e9d8a4d → #310 a8c7c85b → #312 0c306a88
 → #313 79344c62 → #314 68976633 → #316 239df54f
   → #317 848bad22  → #319 6a187a61 → #320 5ea12570 → #321 eeb2a48e
     → #322 73a12463 → #323 ae5dad40 → #324 1f9305e6 + fca58d3e (★ head)
```

- **#317 (`848bad22`) is a load-bearing ancestor** of #324 (it carries the strengthened signed loss + source-curvature). The seed prompt's chain `#319→#323` omits it; it is audited here.
- **#318 (`8a9e8acc`) is a SIBLING off #316, NOT in the #324 chain** (the WTF integration-audit branch). Not conflated.
- CI on #324: the single `Python 3.10 mathematical and epistemic checks` "fail" `gh pr checks` shows is a **`cancelled`** duplicate run (`40539611511`); the *same commit* ran that job to `success` in run `40539622085`, 3.13 passed everywhere, and `lean`/`exact`/`finite_source`/`contracts` all pass. Certified green by native reproduction below, not by trusting either CI run.

## Firewall — INTACT (coordinator-verified by hand)

- **Frozen source untouched across #316→#324**: `git diff 239df54f HEAD` on `succ_internal_matrix_walk.py`, `integer_bbp_carrier.py`, `bbp_source_memory.py`, `provenance/IMPORT_MANIFEST.json` is empty. Live `succ_internal_matrix_walk.py` sha256 `989976921d…` matches the committed `source_ancestry_audit.json`; `IMPORT_MANIFEST.json` matches `main` byte-for-byte.
- **No π-digit oracle / zero-position as construction input** in the 25 chain modules. The only π references are root-of-unity *character evaluations* (`cmath.exp(2j*pi*i/16)`, `mp.e**(2j*pi*h/q)`), never a digit of π fed into state/digit/carry. `U_0=0` and the four signed poles are unmodified.
- **No normality / o(N) overclaim**: `status_flags()` reports `pi_base16_normality_proved=False`, `nontrivial_selected_weyl_bound_proved=False`, `source_selector_specific_saving_proved=False`. Dossier source-of-truth states the inherited saving as `|S_N(h)| ≤ N − (log_8 N)/14 + O_h(1)` (logarithmic, **not** o(N)) and lists `S_N(h)=o(N)` as OPEN.

## Numeric spine — independently confirmed to 80 digits (instrument calibrated on true π, |π_recon−π|=8e-81)

- **Master identity** `U_n = 16^{n−1}π − T_n`: residual `0.0` at 80 dps (n=1,2,3,8,12); derived by hand from `U_n=Σ_{m≤n}16^{n−m}r(m)` + BBP tail `Σ_{m>n}16^{n−m}r(m)=T_n`.
- **`R` closed form** `π/4+5√2π/16+5log2/8+5√2 log(1+√2)/8 = 3.38604761959719…`; series agrees to `5.861e-5` = exactly the `Σ_{n>4000}0.234/n²` 1/n² truncation tail.
- **`B=(R−π)/15=0.0162969977338265…`** ✓ (derived by hand: `B=(1/15)[(R−r₁)−(π−r₁)]`); **`16B=0.26075196374122…`** ✓.
- **`T_n` bounds** `0<T_n<1/16` and sharper `T_n<1/(15(n+1)²)` hold.

## Native execution (this exact head `fca58d3e`, Python 3.12.3, PYTHONPATH=/home/leah/SUCC)

- **Full suite** `python -m unittest discover -s tests -p 'test_*.py'`: **Ran 9059 tests in 1030s — OK, 0 failures / 0 errors, exit 0** (pre-audit tree). This closes the authoring round's admitted **isolated test-only shim** gap (#322 §6: a native import was shimmed in the focused suite only). Combined with the new audit file: **9070 tests**, all green.
- **New independent regression** `tests/test_pi_proof_forge_integration_audit.py`: **11/11 OK**. Non-vacuous, π-free, exact-rational / exact-cyclotomic re-derivations of the load-bearing finite claims (master identity, T_n endpoints + sharp bound, SB-2 α=0 mismatch-every-n, SB-2 Tonelli per-step measure = 16·T_n, SB-3 Plancherel for arbitrary N and random complex z, SB-3 coherent z→E=1, SB-4 16^t permutation mod q and exact cyclotomic indicator limit for q∈{17,19,21,23}, SB-4 independent holdout q=19 separation, firewall flags). Placed in a SEPARATE file so the source-hashed receipts stay byte-exact.
- **Native Lean kernel re-check** — reproduced independently against prebuilt mathlib (pin `4bbdccd9`, Lean v4.14.0), both against `SUCC-rf/formal/mathlib_bridge` and the now-populated local `formal/mathlib_bridge` (5692 oleans unpacked from the local `~/.cache/mathlib` olean cache):
  - `SelectedBranch`: **10 theorems + 4 paired controls**, `KERNEL_CHECKED`
  - `GlobalSigned`: **13 theorems + 7 paired controls**, `KERNEL_CHECKED`
  - `CarryDefect`: **4 theorems + 4 paired controls**, `KERNEL_CHECKED`
  - Every positive theorem compiles (exit 0); every mutant **fails to compile** (exit 1) — false claims are rejected by the kernel. Axioms = `{propext, Classical.choice, Quot.sound}`; no `sorry`/`axiom`/`native_decide`. **Finite facts only — no infinitary normality inherits kernel authority.**

## Adversarial re-derivation + verify (workflow `wf_5e7acc03-423`, 9 blind bearings + d'Alembert break on each; 18 agents, 0 errors)

| Bearing | Rederive | Adversary | Note |
|---|---|---|---|
| SB-1 cylinder transfer | SOUND_WITH_CAVEAT | SURVIVES | inequality never violated; tight-in-limit; firewall intact. Cosmetic: a prose Lipschitz constant for a coordinate shared across terms is understated (4π not 2π) — no numeric break (repo test uses the character case with correct 2π\|h\|). |
| SB-2 digit seam + 16B | CONFIRMED_SOUND | SURVIVES | generic-in-seed, α=0 mismatches every n. Flagged two weaknesses in **my own** regression — both fixed (below). |
| SB-3 CRT Plancherel | SOUND_WITH_CAVEAT | SURVIVES | exact for arbitrary N & complex z; `E_{N,M}(h)→0` UNPROVED (strictly stronger than normality); `a_n` is the 2-adic `U_n mod 16^k`, not the real residue `{U_n}` — a CRT identity is not a real-circle estimate. |
| SB-4 q-grid counterfeit | CONFIRMED_SOUND | SURVIVES | q=17 mode→0.94; **q=21 (composite) also works → coprimality, not primality, is the live condition**; near-miss h=15 decays monotonically. |
| #321 BW-1/BW-2 2-adic | CONFIRMED_SOUND | SURVIVES | `C_past=0` proved two independent ways (`v₂(C_k)`→163 by k=40); Q₂(i) log valuations match. |
| #322 3-adic Hensel + CRT | SOUND_WITH_CAVEAT | SURVIVES | exact-Fraction `binary_code(n,4k)==U_n mod 16^k` for all n=0..199 (no real/2-adic conflation); A bijects Z/3^L. Inherits the 2-adic isometry from #321 (finite-verified, not re-proved here). |
| #323 moving-lag + R,B | CONFIRMED_SOUND | SURVIVES | `R_digamma−R_closed=0.0` @80dps. A dps=60 "break" (ratio 9.95) was a **float artifact** (carrier 16^62), not real. |
| #317/#319 signed loss | CONFIRMED_SOUND | SURVIVES | per-block saving fixed 1/14 → `(log_8 N)/14`, **structurally logarithmic, never o(N)**; bound/N→1. `O_h(1)` onset rests on an uncertified Diophantine constant (already OPEN). |
| INTEG firewall + dedup | SOUND_WITH_CAVEAT | **OVERCLAIM_CONFIRMED** | see below — a census-completeness slip in my own bearing; **firewall itself INTACT**. |

**8 of 9 claims survive the adversary clean.** The one hit is narrow and against my own audit bearing, not the chain's math: my INTEG bearing claimed "the only normality flag set True in the tree is the negative control at `bbp_binwindow_conjugacy_probe.py:97`." That census was **incomplete** (its grep was scoped to `observational_succ/`+`scripts/`). Authoritative tree-wide census (excluding `.lake/` and transient `.claude/worktrees/` agent copies): **five** `.py` sites set a normality/RH flag True —
`tests/test_directional_source_inverse.py:101`, `tests/test_fucc_braid_resonance_capsules.py:132/136`, `scripts/bbp_binwindow_conjugacy_probe.py:97`, `research/2026-10-27/global_signed_validation/audit_receipt.py:19`, `research/2026-10-27/carry_defect_validation/audit_receipt.py:19`. **I read all five: every one is a negative-control mutation** — the flag is set True in a `deepcopy`/mutant specifically to confirm the receipt verifier *rejects* a false-normality receipt (`raise SystemExit('FAILED: false normality mutation escaped')`). So the correction adds *more* firewall evidence, not less: no genuine normality/o(N) assertion exists anywhere in the tree.

### Corrections applied by this audit (additive; frozen source & receipts untouched)
1. **De-vacuumed my own test.** `tests/test_pi_proof_forge_integration_audit.py::test_mismatch_measure_is_16Tn_per_step` was a tautology (re-asserted `16·Σ = Σ·16`); rewritten to evaluate `D(x)=floor(16{x})` at inside/outside breakpoints of all 16 windows and confirm the mismatch-set measure `=16·T_n` (would fail for `8·T_n`/`32·T_n`).
2. **Relabeled** `test_master_identity_finite_self_consistency` to state it is finite telescoping self-consistency (`prefix=16·T_0` is a rational π-truncation), NOT a proof of the π limit — the mpmath/true-π check is the independent one.
3. **Recommendations to the authoring round / Codex** (not applied — frozen-dossier surface, coordinate-don't-race): correct SB-1's shared-coordinate Lipschitz accounting (4π); re-scope or enumerate the INTEG census; make the SB-4 finite probe test the full band `1..q-1` with an h-aware bar.

## Proof-status ledger (audited)

| Claim | Status | Boundary |
|---|---|---|
| Master identity `U_n=16^{n−1}π−T_n`, `B=(R−π)/15` | PROVED (coordinator, 80-digit + hand) | exact |
| SB-1 nonlinear cylinder transfer `|Σw[f(X)−f(Y)]|≤B·ΣL` | PAPER-PROVED | discontinuous digit indicators EXCLUDED; graph-Haar ≠ product-Haar |
| SB-2 digit seam + `E#{mismatch}=16B` | PAPER-PROVED | generic-in-seed, NOT fixed α=π (α=0 mismatches every n) |
| SB-3 finite CRT Plancherel | PAPER-PROVED, conditional on #321/#322 CRT bijection | `E_{N,M}(h)→0` UNPROVED; z≡1 ⇒ E=1 |
| SB-4 q-grid finite-frequency counterfeit | PAPER-PROVED | refutes finite-band→normality; NOT the BBP source |
| #321 BW-1/BW-2 2-adic zero boundary `C_past=0`, `Φ(n)=U_n` | PAPER-PROVED in Q₂ | 2-adic ≠ real circle; no Weyl transport |
| #322 CRT-1 joint 2×3 clock | PAPER-PROVED | finite clock identity, NOT real equidistribution |
| #317/#319 signed loss `|S_N(h)|≤N−(log_8 N)/14+O(1)` | PAPER-PROVED | logarithmic saving; forcing-defect method ceilinged at `(19/8)√|h|+2` |
| π base-16 normality / `S_N(h)=o(N)` | **OPEN** | the actual gate; Codex moonshot |

## Smallest remaining arithmetic obligation

Prove, for every fixed `h≠0`, a **source-specific signed bound on the CRT-binned sums** `B_{a,b;N}(h)=Σ_{n≤N, [U_n]_{16^k}=a, [A(n)]_{3^L}=b} e(hU_n)` forcing `E_{N,M}(h)=(M/N²)Σ_t|Σ_{n≡t}e(hU_n)|² → 0` along some admissible `M=16^k3^L=o(N)` — equivalently, upgrade #319's logarithmic loss from `N−(log_8 N)/14` to `o(N)`. Finite marginals, symbolic reindexing, 2-adic orthogonality, generic-seed digit counts, and any finite-frequency band are proven insufficient (SB-4 counterfeit + #320 mutant + changed-seed `V_n=−T_n`).

## Reproduction

```sh
PYTHONPATH=/home/leah/SUCC python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=/home/leah/SUCC python -m unittest tests.test_pi_proof_forge_integration_audit
PYTHONPATH=/home/leah/SUCC python scripts/verify_provenance.py
python scripts/check_selected_branch_lean.py --output <dir>   # default local bridge, now populated
```

## Strengthening round (post-audit, adversary-verified)

New dossier [`PI_FRONTIER_AUDIT_STRENGTHENING_2026-10-27.md`](../research/2026-10-27/PI_FRONTIER_AUDIT_STRENGTHENING_2026-10-27.md)
+ regression `tests/test_pi_frontier_strengthening_audit.py` (**10/10 OK**, non-vacuous, π-free/exact
where possible). Four obligations sharpened; a d'Alembert adversary pass ran against the draft and
**killed one of my own headline claims** before commit — folded in.

1. **2-adic isometry (#3) upgraded finite-verified → PROVED on all ℤ₂.** `r(x)=A(x)/D(x)` is a 2-adic
   isometry because `A(x)≡x`, `D(x)≡1 (mod 2)` force the quotient `Q(a,b)≡1 (mod 2)` (verified
   symbolically to be the *constant* 1 in 𝔽₂[a,b]); `Φ` inherits it by ultrametric tail-domination.
   Proves `r` itself, not only `Φ`. Stays 2-adic — no Weyl content.
2. **#319 Diophantine input reclassified — and a self-overclaim corrected.** The real barrier is the
   **collision exponent 8** (`q=15|h|16^m`, `|h|≤m²/64` polynomial ⇒ `q^{−8+o(1)}` approximation), not
   the dossier's convenient `15/2`. EITHER Salikhov-2008 (7.6063) or ZZ-2020 (7.1032) clears `μ(π)<8`
   and licenses the `−(log₈N)/14` order; ZZ only lowers the onset. My draft had claimed the result
   "requires the 2020 bound / Salikhov insufficient" — **the adversary refuted this** with the structure
   theorem (onset exists ⇔ `s<8`, verified in log-space: `m₂=44` Salikhov, `9` ZZ, none at `s=8`). Only
   the effective constant `C`/onset is unextracted (CONDITIONAL, not open).
3. **SB-1 Lipschitz (#4) made precise.** `2π|h|` per slot; shared-coordinate budget `2π·Σ|hᵢ|` (sharp
   `2π·|Σhᵢ|`; `+h,+h→4π|h|`, `+h,−h→0`). Cosmetic, no numeric break.
4. **Gate (#1) reduction, honest.** `|S_N(h)−W_N(h)|≤2π|h|B` for all N ⇒ per-`h` gate = π Weyl sum;
   over all `h≠0` = base-16 normality (carrier normality-neutral). Via ISO-1, the SB-3 energy
   `E_{N,M}(h)` is the L²-energy of `e(hUₙ)` across APs mod `M=16^k3^L`; smallest obligation = its decay
   along admissible `M=o(N)`. **π normality / RH OPEN.**

**Process note:** the one overclaim (#2 "requires 2020") was caught by running the adversary gate on the
draft *before* committing — the same discipline that caught the vacuous test last round. Firewall
untouched; additive files only (no frozen source / Codex dossier / receipt edited).

```sh
PYTHONPATH=/home/leah/SUCC python -m unittest tests.test_pi_frontier_strengthening_audit -v
```
