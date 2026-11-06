# Front C: proofs

**2026-11-05. Research-only.** Reference checkout: PR #522 head plus the CI fix `cd672158`. This front is additive to its own directory. The original four signed poles, the literal `U_0=0`, main, Lean and workflows are untouched. Classical theorems are imported and named; nothing here is a claim of worldwide priority. **π base-16 normality, original fixed-h Weyl decay, and RH remain OPEN.**

Numbers quoted as "receipt" come from `FINITE_RECEIPT.json`, written by `front_c_probe.py` (deterministic: the same sha256 on rerun). Those numbers are OBSERVED-finite only.

## 0. Notation and the one structural fact used everywhere

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)`, `x_n={U_n}`, `e(t)=exp(2πit)`. For a rational tap vector `w∈Q^8` write `r_w(n)=Σ_j w_j/(8(n-1)+j)`, `T^w_n=Σ_{j≥1}16^{-j}r_w(n+j)`, and `I(w)=Σ_j w_j Σ_{k≥0}16^{-k}/(8k+j)=∫_0^1 P_w(t)/(1-t^8/16)dt`.

**Gauge (PROVED; elementary).** For every w, every real seed s and every n≥0,
`U^w_n(s)=16^n(s+I(w)/16)-T^w_n`.
*Proof.* `16^n Σ_{j≥1}16^{-j}r_w(j) - Σ_{j≥1}16^{-j}r_w(n+j) = Σ_{j=1}^n16^{n-j}r_w(j)`. Then add `16^n s`. ∎

Hence `x_n={z_n-T_n}` with `z_n={16^nα}`, `α=s+I(w)/16`; for the original source `I(p)=π`. A real-circle observable of the selected orbit is any Borel `F(n,x_n)`. It equals `G(n,z_n)` with `G(n,z)=F(n,{z-T_n})`. The source enters only through `α` and the smooth, seed-independent `T_n`, where `0<1/(64n²)-T_n<1/(64n³)` (CC-01).

---

## C1. Mixed angular-radial correlation

### C1-1. Label classification (PROVED)

**Definitions.** A label is a sequence attached to the selected orbit.
- *Radial:* a function of n and the source alone (independent of seed and orbit).
- *Orbit:* a function `G(n,z_n)` (equivalently `F(n,x_n)`).
- *Rational-arithmetic:* a function of the rational state `U_n(s)`, defined only when `s∈Q`; see C2.

**Theorem C1-1.**
(a) The following are **radial**:
- `r(n)`, `T_n`, `T^ang_n`, `T^rad_n=-Z_n`, `Δ^mZ_n` (#508), `S_j(n)=Σ_{i≤j}16^{j-i}r(n+i)=16^jT_n-T_{n+j}`, and `den r(n)`;
- every mod-8 character of the four denominator factors `2n-1, 4n-1, 8n-7, 8n-3`;
- prime-level labels: `λ(8n-7)`, `μ`, primality of `8n-j`, `χ₋₄(P⁺(8n-7))`, odd cofactors.

(b) Mod-8 characters of the four denominator factors are **periodic in n with period dividing 4**. For example `χ₋₄(2n-1)=(-1)^{n-1}`, `χ₋₄(8n-7)=χ₋₄(8n-3)=1`, `χ₈(8n-3)=-1`, and `χ₈(4n-1)` depends on n mod 2.

(c) The following are **orbit labels**: `x_n`, the carries `c_{n+1}=⌊16x_n+r(n+1)⌋`, the hex digits `d_{n+1}=⌊16z_n⌋`, and the branch bits `b_{n,m,k}`. The exact carry identity is
`c_{n+1} = d_{n+1} + 16·1[x_n ≥ 1-T_n] - 1[x_{n+1} ≥ 1-T_{n+1}]`.
The correction events `{x_n≥1-T_n}` are exactly `{z_n<T_n}`, a shrinking target of width below `1/(64n²)`.

*Proof of (c).* `⌊U_{n+1}⌋=16⌊U_n⌋+c_{n+1}` and `⌊U_{n+1}+T_{n+1}⌋=16⌊U_n+T_n⌋+d_{n+1}`, since `U_n+T_n=16^nα`. Subtract, and use `⌊U+T⌋-⌊U⌋=1[x+T≥1]` for `0<T<1`. ∎

For the branch bits, the orchestrator's front_b **CB-1** gives `b_{n,m,k}=1[S_m(n+k)≤x_{n+d}<S_d(n)]` (d=m+k, `S_d(n)<1`). That is an orbit indicator with radial endpoints. *Receipt:* CB-1 agrees with the defining branch rule `b=1[θ+δ≥1]` at all 5×(256+…+4096)=39680 tested (n,m,k) for the TRUE orbit, with 0 disagreements. The pairs tested are `(m,k)∈{(1,1),(2,1),(1,2)}` (all b=0) and the two critical pairs `(d_A-1,1)`, `(d_A-2,2)`, where `d_A` is the largest admissible depth. In the critical pairs, 31 to 1023 of the bits per epoch equal 1, so both branches are exercised. The carry identity holds at every n of every epoch. There were 0 correction events for TRUE, and the event margins are at least 2^238 ulps. COH has `c≡15`, `d≡0`.

### C1-2. Partial summation and exact duality (PROVED)

**Setting.** Fix an epoch `[A,2A)`, any complex unimodular `e_n` (for example `e(hU_n)` for any seed), `S_L=Σ_{n=A}^{A+L-1}e_n`, and `V(a)=|a_{2A-1}|+Σ_{n=A}^{2A-2}|a_{n+1}-a_n|`.

**Theorem C1-2.**
(i) For every complex weight a,
`|Σ_{n∈[A,2A)} a_n e_n| ≤ V(a)·max_{1≤L≤A}|S_L|`.
(ii) Exact duality: `sup{|Σa_ne_n| : V(a)≤1} = max_L|S_L|`.
(iii) Reverse transfer: if `a_n≠0` on the epoch, `max_L|S_L| ≤ (sup|1/a|+Σ|Δ(1/a)|)·max_L|Σ_{n=A}^{A+L-1}a_ne_n|`.

*Proof.*
(i) Abel summation with `S_0=0`: `Σa_ne_n = a_{2A-1}S_A - Σ_{L=1}^{A-1}S_L(a_{A+L}-a_{A+L-1})`.
(ii) Extend `a_{2A}:=0`. Then `a=Σ_{L=1}^{A}(a_{A+L-1}-a_{A+L})·1_{[A,A+L)}` with total coefficient mass `V(a)`. So the V-unit ball is the absolutely convex hull of the step weights `1_{[A,A+L)}`, each of which has `V=1` and gives `|S_L|`.
(iii) Apply (i) on each initial window to `b=1/a` and the sequence `a_ne_n`. ∎

**What it implies.**
- For every radial weight with bounded variation, the mixed angular-radial mean is at most `V(a)` times the windowed Weyl maximal function `M_A=max_L|S_L|/A`.
- Over the whole family `V≤1` it is **equal** to `M_A`.
- A nonvanishing radial weight with bounded `V(1/a)` gives an equivalent statement.

So no radial BV weight produces a saving beyond the windowed Weyl sums. This covers:
- `T_n`, `r(n)` and `Z_n` weights;
- the #508 bispectrum `Q_m=e(hU_n)e(±hΔ^mZ_n)`;
- the critical chirp `e(h16^jU_n)=e(hU_{n+j})e(-hS_j(n))`. That identity is exact; receipt error at most `6.6e-16`.

For the chirp, the weight `a_n=e(-hS_j(n))` has
`V ≤ 1+2π|h|(S_j(A)-S_j(2A-1)) = 1+(3π/128)Λ(1+O(1/A))`, with `Λ=|h|16^j/A²`.
*Proof:* `r` is decreasing (the #501 integral representation), so `S_j` is decreasing. Combine `S_j=16^jT_n-T_{n+j}` with CC-01.
*Receipt:* `V=1.0732` (Λ=1), `1.2208` (Λ=3), `1.2944` (Λ=4), against `1+0.0736Λ`. The F4/critical-chirp transfer constant is therefore exactly this BV cost.

### C1-3. Controls (PROVED)

For any weights a, and the same forcing:
- **COH collapse:** `|M_COH(a)-R(a)| ≤ 2π|h|A^{-1}Σ|a_n|T_n`, where `R(a)=A^{-1}Σa_n` is the radial-only null. *Proof:* `U_n(s*)=-T_n`, and `|e(-hT)-1|≤2π|h|T`.
- **ROT** (seed 1/5): `M_ROT=e(h/5)M_TRUE`. *Proof:* `16^n/5≡1/5 (mod 1)`.
- **PER_LONG** (`P=2A+64`): `|M_PER_LONG-M_TRUE| ≤ 4π|h|16^{-65}A^{-1}Σ|a_n|`. *Proof:* `|16^nα'-16^nα| ≤ 2·16^{n-P}`.

*Receipt:* all three hold for all 7 weights, both h and all 5 epochs.

Consequence for COH: the coherent seed passes a mixed test **iff** the radial marginal passes it. A mixed observable can only reject COH through a radial marginal that has no saving.

### C1-4. Carry-coupled observables (PROVED)

**Theorem C1-4.** For any bounded g of the m-digit lookahead, write `G_h(z)=g(⌊16z⌋,…,⌊16^mz⌋ mod 16)e(hz)`, a step function times a character. Then
`|Σ_n g(c_{n+1},…)e(hU_n) - Σ_n G_h(z_n)e(-hT_n)| ≤ 2(m+1)·max|g|·N_E(A)`,
where `N_E(A)=#{n∈[A,2A+m]: z_n<T_n}`.

Hence carry-coupled mixed sums are windowed integrals of Riemann-integrable cylinder functions against the epoch measure of z. The weight `e(-hT_n)` has `V≤1+2π|h|T_A`, so C1-2 applies. Under normality, `N_E(A)=o(A)` (since `μ_A([0,ε))→ε` for every ε), and the mean tends to `∫G_h≠0` in general. For g = identity and `16∤h`, `∫⌊16z⌋e(hz)dz=16/(2πih)`.

So the "saving" is relative to a nonzero Haar mean. Carry observables are cylinder frequencies, which are equivalent to normality as a family, and they add nothing beyond it.

*Receipt (h=1):* TRUE `|M|∈[2.27,2.83]`, against `8/π=2.546`. COH gives 15 exactly.

### C1-5. Where the BV reduction genuinely fails: arithmetic labels (PROVED)

Let `S={n: 8n-7 prime}` and `a_n=1_S(n)log(8n-7)`. Then `R(a)→2` by PNT in progressions. `V(a)` is of order `A` (the receipt gives 848…14040), so C1-2 is useless.

**Proposition C1-5.** Prime-label mixed savings are logically independent of normality.

(a) **Normal does not imply a saving.** Let `α_0` be any base-16 normal number. Set the digit at position `n+1` to 0 for every `n∈S`, and call the result α. S has density 0, so every block frequency is unchanged and α is normal. But `z_n∈[0,1/16)` for `n∈S`, so `Re A^{-1}Σa_ne(z_n) ≥ cos(π/8)R(a) → 2cos(π/8)`, and there is no saving.

(b) **A saving does not imply normality.** Let θ be the golden ratio and `L_n=⌈log_16 log n⌉`. For the j-th element `n_j∈S`, write the first `L_{n_j}` hex digits of `{jθ}` at positions `n_j+1…n_j+L_{n_j}`, skipping n whose window would collide with the next prime window. All other digits are 0.
- The windows have total density 0, so the digit 0 has frequency 1 and α is not normal.
- Colliding n (a pair `8n-7` and `8n-7+8g`, both prime, `g≤L_n`) number at most `≪Σ_{g≤L}A(log log g)/log²A=o(A/log A)` by the classical Brun/Selberg upper sieve. Their weight is `o(R)`.
- For the remaining `n∈S`, `|z_n-{jθ}| ≤ 2·16^{-L_n}→0`. Kronecker blocks have discrepancy `O(log N/N)` uniformly in their start (θ has bounded partial quotients). So `A^{-1}Σa_ne(hz_n)→0` for every fixed `h≠0`.

(c) **Coherent seed.** For `a_n=λ(8n-7)`, `R(a)→0` (Liouville in progressions), so COH passes the mixed test by C1-3. Receipt: COH `|M|≤0.07`.

(d) **"A saving neither marginal has" exists only for tuned weights.** Take `α=1/17` (`16≡-1 mod 17`), so `z_n` alternates between `1/17` and `16/17`, and `|c(1)|=cos(2π/17)`. The radial weight `a_n=(-e(2/17))^{n mod 2}` has `|R|≍1`, yet the mixed sum is exactly 0. Such a weight is phase-locked to a periodic orbit. By C1-2(ii), the supremum over every radial V-ball is still `M_A`.

*Observed decoupling (receipt):*
- In every control, `|M(prime)|≈|c_A(h)|·R` up to fluctuation. PER_SHORT: ratio 0.09–0.19 (h=1) and 0.24–0.30 (h=3), against `|c|=0.15` and `0.26`.
- TRUE ratio ∈ [0.012, 0.177], so preregistered P-C1-7 passed.

**Verdict C1.** No mixed angular-radial correlation yields a normality-relevant saving beyond the marginals.
- BV radial weights: exact duality with the windowed Weyl maximal function.
- Carry/branch labels: interval and cylinder observables of `z_n` with radial endpoints.
- Non-BV arithmetic labels: logically independent of normality in both directions.

The claim "mixed coupling supplies a saving neither marginal has, bearing on normality" is **REFUTED-with-receipt**: C1-2(ii) plus C1-5(a–d).

---

## C2. Prime-Frobenius / χ₋₄ orientation

### C2-0. The exact statement under test (quoted from #499/#500)

- PCQ-1: `(S_aw)_l=χ₂(a)^{8-l}2^{(j_a(l)-l)/2}w_{j_a(l)}`, with `S_aS_b=S_ab`.
- PCQ-2: `pU^w_{kp}≡U^{S_aw}_k (mod p)` for `p>8k`, `p≡a (8)`, zero seed.
- PCQ-4/5: `S_5p=p`, `S_3p=-p♯/2`, `p=p_ang+p_rad`, with `p_ang` χ₋₄-isotypic and `p_rad` trivial.
- PCQ-6: `pY_{kp}≡χ₋₄(p)Y_k`, `pZ_{kp}≡Z_k`.
- PCQ-17: `sgn C^ang_a(8k+l)=χ₋₄(a)χ₂(a)^l`.

#500 adds: "the radial and angular characters differ at inert primes; a genuine signed distinction a successful estimate could use."

*Receipt:* the group law holds; isotypic dimensions are `(1,χ₋₄,χ₈,χ₋₈)=(4,2,1,1)`; PCQ-2 holds at all 122 eligible (p,k) with `k≤3`, `p≤211`, for both the original and the mutant taps (the action is universal).

### C2-1. Completion reduction (PROVED)

By the gauge, `Y_n=16^nα-T^ang_n` and `Z_n=-T^rad_n`, with the **same** `α=π/16` as U (because `I(p_ang)=I(p)=π` and `I(p_rad)=0`). Every real-circle observable of U, Y or Z is `G(n,z_n)`. The angular quotient changes only the deterministic tail.

The whole line `w_t=p_ang+t·p_rad` (t∈Q) has one completed orbit. Its trivial-character content `t·p_rad` varies, while its fixed-h Weyl means differ by at most `2π|h||t-1|/(32A+16)`. *Receipt, A=1024:* differences ≤ 3.7e-5, against bounds ≤ 1.1e-3.

### C2-2. Domain and seed-blindness of the shadow (PROVED)

(a) `U_n(s)∈Q` for all n iff `s∈Q`. So the shadow exists exactly on the fiber `α_w+Q`, and is undefined at the coherent seed and at every irrational seed.

(b) For `s∈Q` with `v_p(s)≥0`: `pU_{kp}(s) ≡ pU_{kp}(0) (mod p)`, since `p·16^{kp}s∈pZ_(p)`. A rational seed is visible only at primes dividing its denominator. *Receipt:* seed 1/5 is identical at all 122 eligible (p,k); seed 1/13 at p=13 gives 7 versus 4.

(c) Wall invariance: `α` is normal iff `α+s` is normal, for `s∈Q`. *Proof:* `16^ns mod 1` is eventually periodic with some period P. Normality in base 16 gives normality in base `16^P` of every `16^iα`. So each residue class `{16^{Pm+i}α}` is equidistributed, and a constant shift per class preserves that. The converse is the same argument.

So **on its entire domain the shadow sees no change in normality**.

### C2-3. Character–period dictionary and the Baker dichotomy (PROVED; Baker's theorem imported)

**Exact decomposition.** `L_j=∫_0^1t^{j-1}/(1-t^8/16)dt = -(1/8)Σ_{k=0}^7 t_k^jΛ_k`, with `t_k=√2ζ^k`, `ζ=e(1/8)` and `Λ_k=Log(1-ζ^{-k}/√2)`. Each `Λ_k` is an integer combination of the Baker basis
`ℓ = (log√2, log(1+√2), Log(√2+i), Log(√2-i), Log(2-i), Log(2+i), iπ/4)`.
For example `Λ_3=Log((3+i)/2)=ℓ_5-ℓ_1+ℓ_7`, using `3+i=(1+i)(2-i)`. Numerical check: maximal error 5e-61.

**Lemma (independence).**
- `√2`, `1+√2`, `√2±i` and `2±i` are multiplicatively independent modulo torsion in `Q(ζ₈)`. They have nonzero valuations at five distinct primes: `𝔭₂` (with `√2∼𝔭₂²`), two distinct primes above 3 (`(√2+i)(√2-i)=3`, and 3 is unramified), two distinct primes above 5, and `1+√2` is a unit of infinite order.
- Hence the seven logs are Q-linearly independent.
- By **Baker's theorem** (A. Baker 1966) they are Q̄-linearly independent, and any nonzero Q̄-linear form in them is transcendental.

**Theorem C2-3.** Let `I(w)=Σ_ic_i(w)ℓ_i`, with exact `c_i(w)∈Q(ζ₈)` computed by `baker_coeffs`.
(i) `ker I = Q·(8,-8,-4,-8,-2,-2,1,0) = Q·p_rad`. It is one-dimensional, it is the classical BBP zero relation, and it is S_a-stable. This was computed by exact rational RREF of the 28×8 system.
(ii) Isotypic periods lie in disjoint Baker blocks:
  - `I(E_1)=Q⟨log2, log3, log5⟩` (rank 3 on a 4-dimensional space; kernel `Q p_rad`);
  - `I(E_{χ₋₄})=Q⟨π, arctan(1/2)⟩`, injective. The basis maps as `(1/4,0,1/8,0,-1/16,0,-1/32,0)↦π/8-arctan(1/2)/4` and `(0,1/2,0,0,0,-1/8,0,0)↦arctan(1/2)/2`;
  - `I(E_{χ₈})=Q·√2log(1+√2)`;
  - `I(E_{χ₋₈})=Q·√2arctan(1/√2)`.
(iii) These seven reals are Q-linearly independent. So `w mod Q·p_rad` is determined by `I(w)`. In particular, **the χ₋₄ component of w is a function of `α_w` alone**: its (π, arctan(1/2)) coordinates. For the original source they are (1, 0); the original BBP χ₋₄ vector is the unique one that kills the Gaussian-prime-5 angle `arctan(1/2)=arg(2+i)`.
(iv) **Dichotomy.** `α_w=0` iff `w∈Q·p_rad`; otherwise `α_w` is transcendental.

*Proof.*
(i)–(ii) are exact finite linear algebra over Q(ζ₈) once the Λ-expansions are fixed. Each principal-Log identity holds up to `2πi·m`. A numeric error below 1e-60 forces m=0.
(iii) The seven reals are invertible Q̄-combinations of the ℓ's: `log2=2ℓ_1`, `log3=ℓ_3+ℓ_4`, `log5=ℓ_5+ℓ_6`, `π=-4iℓ_7`, `arctan(1/2)=(ℓ_6-ℓ_5)/(2i)`, `√2log(1+√2)=√2ℓ_2`, `√2arctan(1/√2)=√2(ℓ_3-ℓ_4)/(2i)`. Apply Baker.
(iv) follows from (i) and Baker. ∎

**Interpretation.** The χ₋₄ character is the Galois parity of the period: Gaussian arguments (χ₋₄) versus log-norms (trivial). It is arithmetic data about the single real number `α`, not dynamical data about digit statistics.

### C2-4. Reflection gauge: the sign law carries no normality information (PROVED)

Map `w↦-w`. Then `U^{-w}_n=-U^w_n`, `α↦-α`, `z_n↦1-z_n`, and `c_A(h)↦conj c_A(h)`. Pair distances, Fekete energy and normality are invariant (digits map `d↦15-d`). The isotypic type is preserved, since `S_a` is linear. But every p-adic residue negates (`u_p↦-u_p`), so every PCQ-17 pulse sign flips.

So the sign law is a Z/2 orientation label, and every normality-relevant quantity is reflection-invariant. A sign law cannot bound any of them. *Receipt:* residues negate at every tested (p, k≤2); the test file checks `x^{-w}_n=1-x^w_n`.

### C2-5. The strongest non-reducible handle, and its falsification

**Lemma L-C2 (PROVED).** For every `w∈Q^8` with nonzero χ₋₄-isotypic component, the zero-seeded completion `α_w` is transcendental. In particular its orbit is neither eventually periodic nor convergent to 0. The same holds for a nonzero χ₈ or χ₋₈ component, or a trivial component outside `Q p_rad`.
*Proof:* C2-3 (i) and (iv), with `ker I∩E_{χ₋₄}=0`. Preregistered P-C2-4 passed. ∎

**Falsification attempts (all controls):**
- *Coherent seed α=0.* It lies outside the hypothesis (`U_0≠0`), and the shadow is undefined there (C2-2a). The same χ₋₄ source with seed `-α_w` has `x_n=1-T_n`, a nonnormal orbit. So "χ₋₄ source ⇒ normal orbit" is REFUTED without the seed pin, and the seed pin is invisible to every shadow.
- *Periodic completion `α'=k/(16^P-1)`.* This is rational, so it is not the period of any 8-tap source with any nonzero isotypic content (dichotomy). That is consistent with L-C2. But PER_LONG agrees with TRUE to 64 hex digits on every epoch (identical receipts), so L-C2 has **zero finite-epoch content**.
- *Rational seed 1/5.* `α+1/5` is transcendental, all statistics are rotated, and the shadow is identical. Nothing is distinguished.
- *One-pole mutant (w₁:4→5).* Its χ₋₄ component is `(9/4,2,9/8,0,-9/16,-1/2,-9/32,0)≠0`, so `α_mut=(π+L_1)/16` is transcendental. Its normality is unknown, and its finite statistics look like TRUE's.
- *Radial-only null Z.* Trivial character, α=0, orbit converging to 0. It satisfies every PCQ-2/PCQ-6 relation. Having a Frobenius shadow is therefore not evidence of mixing.
- *Liouville `α_L=Σ_{k≥1}16^{-k!}`.* Transcendental (Liouville 1844) and nonnormal (digit 0 has frequency 1). L-C2's conclusion is shared by a nonnormal number, so **no argument from L-C2 can yield normality**.

**Verdict C2.**
- **De-sources (PROVED):** the prime-Frobenius quotient factors through `w ↦ (α_w, T^w)`. On the orbit side it is a function of `(n, z_n)`. The χ₋₄ orientation is a Baker coordinate of α and is reflection-gauged.
- It carries no information about the selected orbit that is not a function of `(n, z_n)` and of α itself, and it cannot orient the chronological or Weyl sign.
- #500's suggestion that the χ₋₄/trivial distinction is "a genuine signed distinction a successful estimate could use" is **REFUTED-with-receipt** as a normality lever: C2-2c, C2-4 and the Liouville countermodel. It is true only as the statement `α_w≠0` (L-C2).

---

## C3. Pair/Fekete exclusion versus global equidistribution

Let `μ_A=A^{-1}Σ_{n∈[A,2A)}δ_{z_n}` and `B_A(w)=A^{-2}#{(n,m): ||z_n-z_m||<w}`, diagonal included. For any probability measure ν, let `Φ_ν(δ)=(ν⊗ν){||x-y||<δ}=∫ν(B(x,δ))dν(x)`.

### C3-1. Mesoscopic budget: L² density, then Haar (PROVED)

**Theorem C3-1.** Let ν be ×16-invariant with `Φ_ν(2δ_j)≤2Cδ_j` along some `δ_j↓0`. Then `Σ_k|ν̂(k)|²≤C`, ν has an L² density, and ν is Haar.

*Proof.* Let `φ_δ=(2δ)^{-1}1_{[-δ,δ]}` and `ψ=φ_δ*φ_δ≤(2δ)^{-1}1_{||t||<2δ}`. Then
`Σ_k|ν̂(k)|²(sin2πkδ/2πkδ)² = ∫∫ψ(x-y)dνdν ≤ Φ_ν(2δ)/(2δ) ≤ C`.
Fatou along `δ_j→0` gives `Σ|ν̂(k)|²≤C`, hence an L² density.
Invariance gives `ν̂(16k)=ν̂(k)`, so `|ν̂(k)|=|ν̂(16^jk)|→0` for k≠0, and ν is Haar. ∎

**Corollary (genuine equivalence).** Fix any C<∞. Then α is normal iff, for a sequence `δ_j↓0`, `limsup_A B_A(2δ_j)≤2Cδ_j`.
- (⇐) The weak limits of `μ_A` are ×16-invariant, because `μ̂_A(16k)-μ̂_A(k)=O(1/A)`. By the portmanteau theorem on the open set `{||x-y||<δ}`, `Φ_ν≤liminf B_A`. Apply C3-1.
- (⇒) `B_A(δ)→2δ` for every fixed δ.

The budget constant is irrelevant; only **boundedness at mesoscopic scales** matters. Strictly stronger, non-equivalent conditions:
- the uniform-in-A budget down to microscopic scales;
- #513's PF7/PF13 (the Fekete energy `E_A≥-o(1)`, which #513 itself proves sufficient but not necessary: planted sparse near-repeats keep normality).

### C3-2. Single-scale quantitative lemma (PROVED)

**Lemma C3-2.** For every epoch, every `h≠0`, every `0<δ≤1/(4|h|)`, with `J=⌊log_16(1/(4δ|h|))⌋+1`:
`|c_A^z(h)| ≤ (π/2)·sqrt((B_A(2δ)/(2δ)-1)_+/(2J)) + 2(J-1)/A`.

*Proof.* As in C3-1 with `μ_A`, `Σ_{k≠0}|c(k)|²ψ̂(k) ≤ B(2δ)/(2δ)-1`, and `ψ̂(k)≥4/π²` for `|k|≤1/(4δ)`. The 2J frequencies `±16^jh` (`j<J`) are distinct and nonzero. The exact shift `c(16k)=c(k)+(e(kz_{2A})-e(kz_A))/A` gives `|c(±16^jh)|≥|c(h)|-2j/A`. ∎

**Consequence (finite equivalence).** α is normal iff there exist `C` and `δ_A→0` with `B_A(2δ_A)≤2Cδ_A` for all large A.
- (⇐) The diagonal forces `δ_A≥1/(2CA)`, so `J_A→∞` and `J_A/A→0`; apply the lemma.
- (⇒) Take `δ_A=max(D_A,A^{-1/2})`, where `D_A` is the epoch discrepancy; then `B_A(2δ)≤4δ+D_A`.

A **single** shrinking mesoscopic scale suffices, at the rate `|c_A(h)|² ≲ C/log(1/δ_A)`. The x-orbit transfers with errors `2π|h|T_A` and `T_A`.

*Receipt:* the inequality holds for all 7 z-orbits, both scales `δ∈{A^{-1/2}, 4/A}`, both h and all epochs. At these A the bounds (0.68–1.2 for Haar-like orbits) are numerically uninformative. That is expected from the `1/log` rate and is not evidence. This is the invariant-orbit analogue of "Poissonian pair correlation implies uniform distribution" (Aistleitner–Lachmann–Pausinger 2018; Grepstad–Larcher 2017). Here invariance lets mere **boundedness at one scale** suffice. No priority is claimed.

### C3-3. Microscopic exclusion does not imply normality (PROVED + receipt)

**What #513 and #501 actually claim.**
- #513 PF-03/PF-06 states that hard-core exclusion is **not** enough (non-orbit half-circle grid), and that #501's microscopic theorem cannot supply PF7.
- #501 GPB-2 proves, for **every real seed** under the original forcing: at `A^{-B}≤w≤A^{-2}log^{-4}A`, the maximal occupancy is `≪A/log A`, `N_A(w)≪A²/log²A`, and `N_A(w)=o(A²)` for `w=o(A^{-2})`.

Neither asserts that microscopic exclusion implies normality. The attack below therefore confirms them and moves the countermodel into the dynamical (×16-orbit) class.

(a) **The coherent seed satisfies GPB-2 (PROVED).** From CC-01, `T_n-T_{n+1} > (n²-n-1)/(64n³(n+1)²) ≥ 1/(128n³)` for n≥5. The points `1-T_n` are monotone, so any arc of width w holds at most `1+1024wA³` epoch points. At `w=A^{-2}log^{-4}A` this is `1+1024A/log⁴A=o(A/log A)`.
*Receipt:* maximal occupancy 58, 77, 105, 147, 211 (A=256…4096), with ratio to `A/log A` 1.26 → 0.43. The orbit is maximally nonnormal (`c_A(h)=1-O(h/A²)`). So **GPB-2-type microscopic dispersion does not imply normality**: receipt COH.

(b) **Strict microscopic exclusion, nonnormal ×16 orbit (PROVED).** Let `ν₁₅` be the Bernoulli measure with digits uniform on `{0,…,14}` in base 16, and `κ=log15/log16=0.976723`.

For `ν₁₅`-a.e. α:
- α is not normal (the digit F never occurs), and `c_A(1)→ν̂₁₅(1)=-0.06484+0.01378i`, with `|·|=0.0663`, by Birkhoff (ν₁₅ is ×16-ergodic).
- For every `β>2/κ=2.04766`, for all large A, there are **no** `n≠m∈[A,2A)` with `||z_n-z_m||≤A^{-β}`.
- The same holds for the same-forcing actual orbit `x_n={z_n-T_n}` (seed `α-π/16`) for `β∈(2/κ,3)`.

*Proof.* Let `L=⌊log_16(1/(4w))⌋`.
- If `|n-m|≥L`: condition on everything except `d_{m+1..m+L}`, which is independent of `z_n`. The arc of length 2w around `z_n-t` meets at most 3 L-cylinders, so `P(||z_m-z_n+t||≤w)≤3·15^{-L}`, **uniformly in the offset t**.
- If `1≤|n-m|=g<L`: an L-digit agreement (or ±1, which is carry-free because F is forbidden) forces a g-periodic word of length `g+L`. So `P≤45·15^{-L}`. For x-pairs the offset `|T_n-T_m|≤L/(32A³)≤w` when β<3, which reduces to the z-case at 2w.
- Since `15^{-L}≤(64w)^κ`, `E#{pairs in [2^j,2^{j+2}) within 2^{-jβ}} ≪ 4^j·2^{-jβκ}`. This is summable iff `βκ>2`. Borel–Cantelli finishes, since each `[A,2A)` lies in some `[2^j,2^{j+2})`. ∎

**Exponent bookkeeping.**
- Expected ordered pairs at `w=A^{-β}`: Haar `≍A^{2-β}` (threshold β=2); ν₁₅ `≍A^{2-βκ}` (threshold `2/κ=2.0477`).
- At `A^{-2-ε}`: Haar is excluded for every ε>0, ν₁₅ for `ε>2/κ-2=0.0477`. The general Bernoulli `ν_p` has threshold `2/κ₂(p)`, where `κ₂=-log_16Σp_i²` (Rényi-2 dimension). Since `κ₂→1` as p→uniform, **for every fixed β>2 there is a nonnormal ×16 orbit with strict exclusion at `A^{-β}`**.
- Nonnormality shows up only at mesoscopic scales: `Φ_{ν₁₅}(δ)≍δ^κ`, so the budget ratio grows like `δ^{κ-1}=δ^{-0.0233}` (C3-1 correctly rejects it, but logarithmically slowly).

**Finite exact receipt** (ordered off-diagonal z-pairs; the seven scales are recorded in the receipt):

| A | TRUE `A^{-2.5}` / `A^{-3}` | FIFTEEN `A^{-2.5}` / `A^{-3}` | TRUE `A^{-1}`÷2A | FIFTEEN `A^{-1}`÷2A | COH x at `1/(64A²)` | PER_SHORT z exact collisions |
|---:|---|---|---:|---:|---:|---:|
| 256 | 0 / 0 | 0 / 0 | 1.055 | 1.203 | 65280 = A(A-1) | 828 |
| 512 | 0 / 0 | 0 / 0 | 0.955 | 1.096 | 261632 | 3800 |
| 1024 | 0 / 0 | 0 / 0 | 1.008 | 1.117 | 1047552 | 16176 |
| 2048 | 0 / 0 | 0 / 0 | 0.968 | 1.137 | 4192256 | 66726 |
| 4096 | 0 / 0 | 0 / 0 | 0.995 | 1.160 | 16773120 | 270948 |

- PER_LONG and ROT are identical to TRUE at every scale (theorem).
- MUT is Haar-like (`A^{-1}` ratios 0.81–1.03).
- FIFTEEN (base-15 digits of √2-1, explicit and deterministic, digit F count 0 in every window) has the same microscopic exclusion as TRUE. It has a mesoscopic excess of 1.10–1.20 (predicted to grow like `δ^{-0.023}`) and `|c_A(1)|` = 0.140, 0.040, 0.111, 0.060, 0.059, against TRUE's 0.074, 0.042, 0.049, 0.019, 0.017.
- At A=512 the h=1 Weyl magnitudes of FIFTEEN and TRUE overlap (0.040 vs 0.042). Finite Weyl data do not separate a dimension-0.977 orbit from TRUE until A≳2000.

**Failed preregistered prediction (reported, not refit).** P-C3-2's band `|c_A(1)|∈[0.03,0.11]` for A≥512 failed at A=1024 (0.11095). The band was narrower than the `A^{-1/2}` fluctuation around 0.066. This affects no theorem: FIFTEEN's nonnormality is proved by the absent digit, not by c(1).

**Verdict C3.**
(i) The mesoscopic budget is **equivalent** to normality (C3-1 and C3-2, PROVED). A single shrinking scale with any bounded constant suffices.
(ii) Microscopic exclusion does **not** imply normality (PROVED):
  - GPB-2-type dispersion is satisfied by COH;
  - strict zero-pair exclusion at any `A^{-β}`, β>2, is satisfied by nonnormal Bernoulli ×16 orbits;
  - an explicit deterministic 15-symbol orbit matches TRUE's microscopic counts (OBSERVED).

#513's own claim (small-scale-only bounds fail) **survives** and is strengthened to the orbit class.
