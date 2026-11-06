# Front C countermodels

Each entry gives the object, what it defeats, the receipt, and its status. "Receipt" refers to `FINITE_RECEIPT.json` or to the proof in PROOFS.md.

| ID | Object | Defeats | Receipt / proof | Status |
|---|---|---|---|---|
| CM-1 | Coherent seed `s*=-π/16` (`α=0`, `U_n=-T_n`, `x_n=1-T_n`) | (a) "a mixed test rejects COH" whenever its radial marginal saves (C1-3); (b) "GPB-2 microscopic dispersion ⇒ normality" (C3-3a); (c) "a χ₋₄ source ⇒ normal orbit" without the seed pin (C2-5) | Mixed Liouville `|M|≤0.07`; all carries are 15; GPB-2 occupancy 58…211, with ratio to `A/log A` 1.26→0.43; every pair lies within `1/(64A²)`; the shadow is undefined (irrational state) | PROVED + OBSERVED |
| CM-2 | PER_LONG: `α'=k/(16^P-1)`, `P=2A+64`, k from the source's own carries | Any finite-epoch claim that distinguishes TRUE from a periodic, nonnormal completion. L-C2 has zero finite-epoch content | Mixed sums, Weyl sums and all pair counts are identical to TRUE (64-hex-digit agreement) | PROVED |
| CM-3 | PER_SHORT: P=61 | Fails microscopic exclusion (exact z-collisions ≥ A²/61) and every budget. Shows the decoupling `|M(label)|≈|c_A(h)|·R` | 828…270948 collisions; prime-label ratio 0.09–0.19 (h=1) and 0.24–0.30 (h=3), against `|c|`=0.15 and 0.26 | PROVED + OBSERVED |
| CM-4 | Rotation seed 1/5 | Shadow-based seed authentication. The seed is invisible at every eligible prime and the statistics are only rotated | 122/122 identical shadows; `M_ROT=e(h/5)M_TRUE`; identical pair counts | PROVED |
| CM-5 | One-pole mutant `w_1:4→5` | The idea that the PCQ-2 action is special to π: it is universal | PCQ-2 holds at 122/122. Its χ₋₄ component `(9/4,2,9/8,0,-9/16,-1/2,-9/32,0)≠0`, so `α_mut` is transcendental, normality unknown, statistics Haar-like | PROVED + OBSERVED |
| CM-6 | Radial-only null (`Z=-T^rad`, and `R(a)=A^{-1}Σa_n`) | "Having a Frobenius shadow indicates mixing": Z satisfies `pZ_{kp}≡Z_k`, has α=0, and converges to 0 | `ker I=Q·p_rad`; COH mixed equals R within `2π|h|ΣaT/A` | PROVED |
| CM-7 | FIFTEEN: Bernoulli(uniform on 0..14) generic point; explicit deterministic representative from the base-15 digits of √2-1 | "Microscopic exclusion ⇒ normality" for ×16 orbits (the half-grid of #513 is not an orbit) | a.s. zero pairs at `A^{-β}` for β>2/κ=2.0477 (proof). Explicit: 0 pairs at `A^{-2.5}` and `A^{-3}` for A=256…4096, the same as TRUE; mesoscopic excess 1.10–1.20; digit F absent | PROVED (a.e.) + OBSERVED (explicit) |
| CM-8 | Normal α with the digit after each n∈{8n-7 prime} set to 0 | "Normality ⇒ prime-label mixed saving" | C1-5(a): density-zero edit; `Re M ≥ cos(π/8)R` | PROVED |
| CM-9 | Nonnormal α: Kronecker windows of length `⌈log_16 log n⌉` after prime times, zeros elsewhere | "Prime-label mixed saving ⇒ normality" | C1-5(b) (Brun/Selberg upper sieve imported) | PROVED |
| CM-10 | Reflection `w↦-w` | "The χ₋₄ sign law orients a normality-relevant sign" | All residues negate; all `|c_A|`, pair counts and normality are invariant | PROVED |
| CM-11 | Liouville `Σ16^{-k!}` | Any route from L-C2 (transcendence of `α_w`) to normality | Transcendental and nonnormal | PROVED (classical) |
| CM-12 | `α=1/17` with phase-locked radial weight `(-e(2/17))^{n mod 2}` | "A saving neither marginal has" being evidence of anything | Mixed sum is 0 exactly while `|R|≍1` and `|c(1)|=cos(2π/17)`; but the V-ball supremum equals `M_A` (C1-2 ii) | PROVED |
| CM-13 | #513 half-circle grid (inherited) | Hard-core spacing ⇒ Haar for arbitrary point sets | #513 PF-03; superseded for orbits by CM-7 | inherited |

**What was attacked hardest and survived:** Lemma L-C2 (`ker I ∩ E_{χ₋₄}=0`). It was preregistered with a decisive falsifier: a rational χ₋₄ vector of period zero. Exact Q(ζ₈) linear algebra found `ker I` to be one-dimensional and purely trivial-character. It survives as a transcendence statement. It dies as a normality lever (CM-1, CM-2, CM-10, CM-11).
