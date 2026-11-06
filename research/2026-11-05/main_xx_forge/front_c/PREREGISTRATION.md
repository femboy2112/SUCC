# Front C preregistration: mixed angular-radial correlations, prime-Frobenius orientation, and pair exclusion

**2026-11-05. Research-only.** Reference checkout is the PR #522 head plus the CI fix (`cd672158`). This front writes only into `research/2026-11-05/main_xx_forge/front_c/`. The original four signed poles, the literal `U_0=0`, main, Lean, workflows and archives are untouched. **Base-16 normality of π is OPEN, and no result here changes that status.**

This file was written before `front_c_probe.py` existed and before any main experiment ran. Development work done earlier, which is therefore NOT blind:
- reading #499, #500, #501 (`af5c7ba3`), #507, #508, #513, #522 and the critical-chirp dossiers (`c9dfcdf0`, `00b6385b`);
- one timing run of the integer-LCM exact recurrence up to n=4096 (0.18 s; denominator 35462 bits). No phase, count or Weyl value was printed.
- pen-and-paper derivations of the partial-summation duality, the carry identity, the single-scale budget lemma, the Baker log basis for the BBP periods, and the 15-symbol Borel-Cantelli bound.

## Fixed source and notation (immutable)

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)`, `x_n={U_n}`, `e(t)=exp(2πit)`, `c_A(h)=A^{-1}Σ_{n=A}^{2A-1}e(hU_n)`. The tail is `T_n=Σ_{j≥1}16^{-j}r(n+j)`, with `0<1/(64n²)-T_n<1/(64n³)` (CC-01). For seed s, `U_n(s)=16^n(s+α)-T_n` with `α=π/16`. The completed orbit is `z_n={16^n α}`.

## Instruments (fixed before running)

- **TRUE:** exact integer-LCM recurrence (unreduced numerator `N_n` with common denominator `D_n=lcm den r(1..n)`, kept mod `D_n`), and an independent `fractions.Fraction` recurrence for cross-checking at small n. Phases go to 256-bit fixed point by exact integer division. No π digits are input.
- **T_n:** backward recurrence `T_n=(T_{n+1}+r(n+1))/16` in 320-bit fixed point. It starts from `T_{N+64}:=0`, so the start error is at most `16^{-64}/(64N²)`. Each step contracts by 16 and adds at most 1 ulp of rounding. The rigorous bound on the error is `2^{-318}`.
- **z_n for TRUE:** `z_n={x_n+T_n}`. Hex digits of α come from the source as `d_{n+1}=⌊U_{n+1}⌋-16⌊U_n⌋` (the carry), corrected by the carry identity below.
- **Controls, used in every numerical check:**
  1. TRUE (`s=0`);
  2. COH (`s*=-π/16`, `α=0`, `U_n=-T_n`, from the backward tail);
  3. PER_LONG (`α'=k/(16^P-1)` with `k=⌊16^Pα⌋` taken from the TRUE source integer part, `P=2A+64`, so it matches the true completed orbit to at least 64 hex digits across the epoch; the real orbit uses the same forcing, `x'_n={z'_n-T_n}`);
  4. PER_SHORT (the same with `P=61`);
  5. ROT (seed 1/5);
  6. MUT (one-pole mutant `w_1:4→5`, i.e. `r'(n)=r(n)+1/(8n-7)`, zero seed, exact);
  7. RADIAL-ONLY NULL (the observable with the angular factor removed).
  For C3 there is also FIFTEEN: digits are the base-15 digits of `√2-1` (exact `isqrt`), written as hex digits 0..14, so the digit F never occurs. `z_n=Σ_{k≥1}b_{n+k}16^{-k}`, and the same-forcing real orbit is `x_n={z_n-T_n}`.
- **Epoch grid:** A ∈ {256, 512, 1024, 2048, 4096}. Weyl frequencies h ∈ {1, 3}. Frobenius checks use k ∈ {1, 2, 3} and all primes p with 8k<p≤211 in each class mod 8.

## C1 hypotheses and falsifiers

- **P-C1-1 (theorem; finite check is calibration).** For every radial weight `a_n` (a function of n only) and every control, `|Σ_{[A,2A)}a_n e(hU_n)| ≤ V(a)·max_{1≤L≤A}|S_L|`, where `V(a)=|a_{2A-1}|+Σ|a_{n+1}-a_n|`. Moreover `sup_{V(a)≤1}|Σa_ne_n| = max_L|S_L|` exactly. *Falsifier:* any violation beyond float error (1e-9 relative), which would mean an instrument bug.
- **P-C1-2 (theorem).** COH collapse: `|M_COH(a)-R(a)| ≤ 2π|h|A^{-1}Σ|a_n|T_n`, where R is the radial-only null `A^{-1}Σa_n`.
- **P-C1-3 (theorem).** ROT: `M_ROT(a)=e(h/5)M_TRUE(a)` to float precision.
- **P-C1-4 (theorem).** PER_LONG: `|M_PER_LONG-M_TRUE| ≤ 2π|h|16^{-60}A^{-1}Σ|a_n|`.
- **P-C1-5 (exact identity).** Carry identity `c_{n+1}=d_{n+1}+16·1[x_n≥1-T_n]-1[x_{n+1}≥1-T_{n+1}]` at every n in every epoch, for TRUE and COH (COH must give `c≡15`, `d≡0`).
- **P-C1-6 (observational).** For TRUE there are no correction events `x_n∈[1-T_n,1)` in any epoch (the Haar heuristic expects about `1/(128A)` of them). *Falsifier:* any event.
- **P-C1-7 (observational).** Liouville weight `a_n=λ(8n-7)`: `|M|≤0.25` for TRUE and also for COH, because COH inherits the radial marginal's saving. Prime weight `a_n=1[8n-7 prime]log(8n-7)`: `|M_COH-R|` is within the P-C1-2 bound (no saving), while `|M_TRUE|/|R| ≤ 0.35` for A≥256. *Falsifier:* a TRUE ratio above 0.35. That would not refute anything proved, but it would refute the observed-trend claim.
- **P-C1-8 (theorem; failure of the reduction).** Arithmetic non-BV labels are logically independent of normality in both directions (constructions in PROOFS).

## C2 hypotheses and falsifiers

- **P-C2-1 (replication of #499 PCQ-2).** `pU^w_{kp} ≡ U^{S_aw}_k (mod p)` holds at every tested eligible (p,k) for the original taps and for the mutant taps (the action is universal).
- **P-C2-2 (theorem: seed blindness).** The ROT shadow equals the TRUE shadow at every tested p≠5.
- **P-C2-3 (exact).** MUT taps have a nonzero χ₈ or χ₋₈ isotypic component.
- **P-C2-4 (lemma L-C2, outcome not known in advance).** `ker(I) ∩ E_{χ₋₄} = {0}`, where I is the [0,1] period functional on Q⁸ and `E_{χ₋₄}` is the 2-dimensional χ₋₄-isotypic subspace. *Decisive falsifier:* a nonzero rational χ₋₄ tap vector with zero period, found by exact linear algebra over Q(ζ₈) in the Baker basis `{log√2, log(1+√2), Log(√2+i), Log(√2-i), Log(2-i), Log(2+i), iπ/4}`. If this happens, L-C2 is REFUTED: χ₋₄ orientation would not even exclude a zero completion.
- **P-C2-5 (prediction).** ker(I) is stable under every S_a (Galois equivariance).
- **P-C2-6 (theorem: non-invariance).** On the line `w_t=p_ang+t·p_rad` the completed orbit is the same for all t, while the isotypic content changes.

## C3 hypotheses and falsifiers

- **P-C3-1 (theorem; calibration).** The single-scale budget inequality `|c(h)| ≤ (π/2)·sqrt((B(2δ)/(2δ)-1)_+/(2J))+2(J-1)/A` holds for every completed z-orbit control at `δ∈{A^{-1/2}, 4/A}`. Here `B(w)=A^{-2}#{(n,m): ||z_n-z_m||<w}` includes the diagonal, and `J=⌊log_16(1/(4δ|h|))⌋+1`. *Falsifier:* any violation.
- **P-C3-2 (observational).** For FIFTEEN there are 0 off-diagonal z-pairs with `||z_n-z_m|| ≤ A^{-2.5}` for every A in the grid, and `|c_A(1)| ∈ [0.03, 0.11]` for A≥512 (the predicted limit is `|ν̂_15(1)|≈1/15`).
- **P-C3-3 (observational).** For TRUE, at most 2 off-diagonal ordered pairs in z and in x at `A^{-2.5}` per epoch.
- **P-C3-4 (theorem).** For COH every ordered pair lies within `1/(64A²)`.
- **P-C3-5 (theorem; GPB-2 seed-uniformity).** COH satisfies the #501 GPB-2 occupancy bound at `w=A^{-2}(log A)^{-4}`.
- **P-C3-6 (theorem).** PER_SHORT has exact z-collisions: at least `A²/61-A` ordered off-diagonal pairs.
- **P-C3-7 (theorem).** ROT pair counts equal TRUE pair counts in x.
- **P-C3-8 (theorem).** PER_LONG z-pair counts equal TRUE z-pair counts at every scale ≥ `16^{-50}`.

## Status rules

A theorem is labeled PROVED only with a written proof in PROOFS.md. Finite checks are labeled OBSERVED-finite. They never promote an asymptotic claim. A failed preregistered observational prediction is reported as failed, never refit. Nothing here may be cited as progress on π normality unless it is an unconditional source-selected inequality, and none is expected.
