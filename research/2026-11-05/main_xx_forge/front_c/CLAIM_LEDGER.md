# Front C claim ledger

The status labels used are PROVED, PROVED-CONDITIONAL, REFUTED-with-receipt, OPEN and OBSERVED-finite. Imported classical theorems are named. No result here bears on π normality except by reduction to the open Weyl gate.

| ID | Statement | Status | Receipt | Next falsifier |
|---|---|---|---|---|
| FC-G | Gauge `U^w_n(s)=16^n(s+I(w)/16)-T^w_n`, for every w, s, n | PROVED | telescoping; `lcm==Fraction` for n≤300 | a source with non-absolutely-convergent tail (none among 8-tap sources) |
| FC-C1-1 | Label classification; carry identity `c_{n+1}=d_{n+1}+16·1[x_n≥1-T_n]-1[x_{n+1}≥1-T_{n+1}]` | PROVED | 0 violations at all n, A=256…4096; 0 TRUE events | an event `z_n<T_n` in a fresh epoch would not falsify the identity, but would end P-C1-6 |
| FC-C1-CB1 | front_b CB-1 interval form of branch bits | Checked; proof is front_b's | 39680 agreements, 0 disagreements, including critical depths with 31–1023 bits equal to 1 per epoch | (m,k) with `S_d(n)` near 1 |
| FC-C1-2 | `|Σa_ne_n|≤V(a)max_L|S_L|`; `sup_{V≤1}=max_L|S_L|` exactly; reverse transfer for nonvanishing a | PROVED | `bv_holds` for every control, weight, h and A; the step weight attains equality | none (finite algebra) |
| FC-C1-2c | Critical-chirp BV cost `V=1+(3π/128)Λ(1+O(1/A))` | PROVED | V=1.0732 (Λ=1), 1.2208 (Λ=3), 1.2944 (Λ=4) | — |
| FC-C1-3 | COH collapse `|M_COH-R|≤2π|h|ΣaT/A`; ROT `=e(h/5)M_TRUE`; PER_LONG equality | PROVED | all pass | — |
| FC-C1-4 | Carry-coupled mixed sums are cylinder-function Weyl sums of `z_n` with a nonzero Haar mean (`16/(2πih)` for g=id) | PROVED | TRUE `|M|`∈[2.27,2.83] against 2.546 (h=1); COH = 15 | — |
| FC-C1-5 | Prime-label mixed savings are logically independent of normality (both directions) | PROVED (classical PNT-in-AP and upper sieve imported) | CM-8, CM-9 | — |
| FC-C1-V | "A mixed angular-radial correlation yields a normality-relevant saving beyond the marginals" | **REFUTED-with-receipt** | FC-C1-2 (exact duality), FC-C1-4, FC-C1-5, CM-12 | a weight family that is neither BV, cylinder, nor seed-independent arithmetic (none identified) |
| FC-C1-O | Observed decoupling `|M(label)|≈|c_A(h)|·R` | OBSERVED-finite | PER_SHORT 0.24–0.30 vs 0.26 (h=3); TRUE prime ratio 0.012–0.177 | a fresh epoch with ratio > 0.35 (P-C1-7 passed here) |
| FC-C2-1 | Y, Z, U share the completion data (`α=π/16`, resp. 0); every real observable is `G(n,z_n)`; `w_t=p_ang+t p_rad` has one orbit | PROVED | line diffs ≤ 3.7e-5 within bounds ≤ 1.1e-3 | — |
| FC-C2-2 | Shadow domain is `s∈Q`; p-integral seeds are invisible; Wall invariance means normality is constant on the domain | PROVED (Wall's theorem; self-contained proof given) | 1/5: 122/122 identical; 1/13 at p=13: 7 vs 4 | — |
| FC-C2-3 | `ker I=Q·(8,-8,-4,-8,-2,-2,1,0)=Q·p_rad`; isotypic periods `E_1→⟨log2,log3,log5⟩`, `E_{χ₋₄}→⟨π,arctan(1/2)⟩`, `E_{χ₈}→√2log(1+√2)`, `E_{χ₋₈}→√2arctan(1/√2)`; dichotomy `α_w∈{0}∪transcendental` | PROVED (Baker 1966 imported) | exact RREF; log identities to 5e-61; `I(p)=π`, `I(p♯)=2π`, `I(p_rad)=0` | — |
| FC-C2-4 | Reflection gauge: the sign law flips, normality-relevant quantities are invariant | PROVED | residues negate at every tested (p,k) | — |
| FC-C2-L | L-C2: a nonzero χ₋₄ component implies `α_w` transcendental | PROVED | preregistered P-C2-4 passed | — |
| FC-C2-V | "Prime-Frobenius χ₋₄ orientation is a nonreducible handle that orients the Weyl/chronological sign" (#500 reading) | **REFUTED-with-receipt** as a normality lever | FC-C2-1..4, CM-1, CM-2, CM-10, CM-11 | an inequality that uses the Baker coordinates of α and fails for some nonnormal transcendental α |
| FC-C3-1 | ×16-invariant ν with `Φ_ν(2δ_j)≤2Cδ_j` ⇒ `Σ|ν̂|²≤C`, L² density, Haar; normality ⟺ mesoscopic budget with any constant | PROVED | — | — |
| FC-C3-2 | Single-scale lemma `|c(h)|≤(π/2)√((B/2δ-1)_+/2J)+2(J-1)/A`; normality ⟺ budget at one shrinking scale | PROVED | holds for 7 orbits × 2 scales × 2 h × 5 A | — |
| FC-C3-3a | Coherent seed satisfies #501 GPB-2 (occupancy ≤ `1+1024wA³`) | PROVED | 58…211 | — |
| FC-C3-3b | ν₁₅-a.e. α is nonnormal with strict zero-pair exclusion at `A^{-β}` for β>2/κ (z), and for β∈(2/κ,3) (same-forcing x) | PROVED | Borel–Cantelli with an offset-uniform cylinder bound | — |
| FC-C3-3c | Explicit √2 base-15 orbit matches TRUE's microscopic counts, with mesoscopic excess 1.10–1.20 | OBSERVED-finite | table in PROOFS C3-3 | larger A, where the δ^{-0.023} growth should continue |
| FC-C3-V | "Microscopic (pair/Fekete) exclusion implies normality" | **REFUTED-with-receipt** (and consistent with #513's own claim) | CM-1, CM-7 | — |
| FC-P | Preregistered observational band P-C3-2 (`|c_A(1)|∈[0.03,0.11]` for FIFTEEN, A≥512) | **FAILED** at A=1024 (0.11095); not refit | receipt flags | — |
| FC-OPEN | Zero-seed fixed-h Weyl decay; zero-seed mesoscopic budget; π base-16 normality; RH | OPEN | — | NEXT.md |
