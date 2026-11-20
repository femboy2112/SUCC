# Constructive causal Fourier atoms — exact theorems and proof boundaries

**20 November 2026.** Research-only, source-typed mathematical manuscript. Base: SUCC draft #674 (`ec4f99bbd9ec34461ba7393c15833b966284cc05`), itself stacked on #673 and #672, ultimately Main XXVI (`81be6b897ae980b801a3b9de9e22ef81e8360bfb`). This note adds no changes to the original BBP source, seed, imports, or production code. Claimed scholarly priority: **none**. R0, π base-16 normality, RH and nonclassical physical carrier claims: **OPEN**.

## 0. What the proposal is and is not

**Steelman.** A causal succession law specifies a composition algebra. Retaining source, order and basis labels creates a *bookkeeping functor* that can be analyzed in representations respecting that algebra. For additive causal clocks, scalar unitary representations are Fourier characters. For affine and noncommuting compositions the natural Fourier components undergo **dual frequency transport**, not independent scalar multiplication. Explicit 3/5-adic clock coordinates supply a complete finite Fourier eigenbasis; the original BBP source time measure supplies a separate, source-specific positive Fourier spectrum; the radix-16 phase observer lives in a third representation. The goal is a source-faithful *joining*, not identification of these distinct spectra by fiat.

**Firewall.** A causal order alone does not canonically define an additive group, Haar measure, or Fourier basis. These arise after supplying the declared action algebra, compatible quotient and readout. Conserved arithmetic product formula, Hilbert norm, actual thermodynamic energy, and a source's Weyl statistics remain distinct.

Write `e(t)=exp(2πit)`. `r(n)` below always denotes the original four-pole signed rational BBP forcing, `U_0=0`, `x=π/16`. Nonzero seed and modified forcing appear **only as explicitly labeled hostile controls**.

## CFA-01 — Additive causal composition creates Fourier characters (CLASSICAL)

For a causal action monoid whose bookkeeping is a homomorphism `b:M→(Z,+)`, a unit-modulus character is a function `χ:Z→U(1)` satisfying `χ(m+n)=χ(m)χ(n)`. Every such character is `χ_ω(n)=exp(iω n)` for `ω` modulo `2π`, since `χ(n)=χ(1)^n`. On the finite quotient `Z/qZ`, compatibility `χ(q)=1` restricts frequencies to `ω=2πa/q`.

For a real additive *source-value* journal the characters are `e(h t)`, `h∈R`. At integer `h` they descend to the circle `R/Z`. This is the precise conditional sense in which a Fourier basis emerges from **composable additive causal bookkeeping**. General directed graphs and noncommuting operations need a different representation theory; causality alone is not a theorem asserting universal ordinary Fourier coordinates.

## CFA-02 — Exact 3/5-adic odometer from radix-16 bookkeeping (CLASSICAL, explicit SUCC interface)

Let `J_n=(16^n−1)/15` for integer `n≥0` and `A(J)=16J+1`. Then `J_0=0`, `J_(n+1)=A(J_n)`, and for distinct `m,n≥0` and `p∈{3,5}`,

`v_p(J_m−J_n)=v_p(m−n)`.

**Proof.** Assuming `m>n`, `J_m−J_n=16^n(16^(m−n)−1)/15`. For odd `p=3,5` with `p|16−1` and `p∤16`, lifting the exponent gives `v_p(16^d−1)=v_p(15)+v_p(d)`. The factor `16^n` is a p-adic unit, giving the claim.

Therefore the finite map `n mod p^k→J_n mod p^k` is a bijective isometry for every `k≥1`, and `A` acts on its state residues as a **single cycle of period p^k**. The compatible finite maps extend to an isometric homeomorphism `j_p:Z_p→Z_p`; on `Z_p`, `j_p(t)=(16^t−1)/15` (p-adic exponent), with analytic inverse `t=log(1+15J)/log16`. Both `log16` and `15` have valuation one at p=3,5, so the quotient is well-defined by the power series and extends the finite clock. Hence `A∘j_p=j_p∘(t↦t+1)`. Simultaneous CRT gives a single-cycle clock modulo `15^k` and an odometer on `Z_3×Z_5` under the diagonal integer clock. No Fibonacci auxiliary transfer is assumed.

These clocks are **universal for the geometric successor**. They are not a conjugacy of the nonautonomous BBP recurrence `U_(n+1)=16U_n+r(n+1)` to a 3/5-adic odometer.

## CFA-03 — True causal clock eigenatoms versus additive state characters (CLASSICAL, explicit basis transport)

Fix `p∈{3,5}`, `k≥1`, `q=p^k`. Denote by `ℓ_q(J)∈Z/qZ` the inverse clock `J=J_n mod q ⇔ ℓ_q(J)=n mod q`. Define

`ψ_(b,q)(J)=e(bJ/q)` and `χ_(a,q)(J)=e(aℓ_q(J)/q)`.

**Different transformations:**

`ψ_(b,q)(A J)=e(b/q) ψ_(16b,q)(J)` (frequency *mixing* in the naive state chart), while

`χ_(a,q)(A J)=e(a/q) χ_(a,q)(J)` (a genuine Koopman eigenatom in causal-clock coordinates).

The `q` functions `χ_(a,q)` form an orthonormal basis of functions on `Z/qZ` under uniform measure: as `J` runs through all residues, `ℓ_q(J)` also runs through all residues. The `ψ_(b,q)` are the standard additive Fourier basis. Their change-of-basis matrix is

`C_(a,b) = (1/q) Σ_(n=0)^(q−1) e([a n − b J_n]/q)`.

It is **unitary** (the Gram of two orthonormal bases), and `χ_a(J)=Σ_b C_(a,b) ψ_b(J)`. Hence a frequency-mixing operator in one representation is *exactly diagonal* after a source-faithful, unitary bookkeeping transform. The full collection of compatible `χ` over all levels gives an orthonormal Fourier eigenbasis for `L²(Z_p,Haar)` (via density of locally constant functions and compatible characters).

No finite-dimensional transform has been asserted between these clock functions and real π phase characters. The unitary matrix is a **same-carrier, same-finite-clock** basis transport.

## CFA-04 — The 2-adic view is an attracting endpoint, not the same odometer (CLASSICAL)

`J_n+1/15=16^n/15`. Consequently `v_2(J_n+1/15)=4n`, so `J_n→−1/15` in `Z_2` as ordinary chronological `n→∞`, while the real `J_n` diverges. But `n↦J_n` does **not** continuously extend the 2-adic *clock variable* `n∈Z_2`: the integers `n_k=2^k` tend to 0 in `Z_2`, whereas `J_(n_k)→−1/15≠J_0=0` in `Z_2`.

For `Δ_n=J_n+1/15=16^n/15`, its local absolute values are

`|Δ_n|_∞=16^n/15`, `|Δ_n|_2=16^(−n)`, `|Δ_n|_3=3`, `|Δ_n|_5=5`;

all others are 1. Their product is identically one (classical rational product formula). This is **place-labeled arithmetic bookkeeping**, not a physical energy conservation or a nonclassical coupling theorem.

## CFA-05 — Original BBP source-time Fourier transform is an exact causal Mellin object (CLASSICAL BBP + explicit new-to-dossier assembly)

Retain the literal source

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_0=0`.

The original source polynomial is `Q(t)=4−2t³−t⁴−t⁵=(1−t)(4+4t+4t²+2t³+t⁴)`. Hence, for `n≥1`,

`r(n)=∫_0^1 t^(8n−8) Q(t)dt > 0`.

Define the **source-clock** coefficients `c_n=16^(−n)r(n)>0` and `F(z)=Σ_(n≥1)c_n z^n`. This series is absolutely convergent for `|z|<16` (and on its boundary by `r(n)=O(n^(−2))`); geometric summation and dominated convergence give

`F(z)=∫_0^1 Q(t) z/(16−z t^8)dt` for `|z|<16`.

For real `ω`, the chronological Fourier transform is `𝓕(ω)=F(exp(iω))`. The classical BBP evaluation supplies `𝓕(0)=F(1)=x=π/16`. **Its input variable is event time `n`; it is not the Weyl sum over the orbit `{16^n x}`.**

The source weights define a positive discrete finite measure `μ_source=Σ c_n δ_n` on the causal clock. Fourier inversion recovers each `c_n` from all modes of `𝓕`. It does **not** recover the independent homogeneous seed without the objective seed anchor.

## CFA-06 — Strict source-time constructive interference with exact BBP coefficient (PROVED elementary consequence)

Since all `c_n>0` and `Σc_n=x`, for every real `ω`,

`x²−|𝓕(ω)|² = 2Σ_(1≤j<k) c_j c_k[1−cos((k−j)ω)]`.

Using only the first two *authentic* source atoms,

`c_1=47/240`, `c_2=53/104832`, and `2 c_1 c_2=2491/12579840`.

Thus

`x²−|𝓕(ω)|² ≥ (2491/12579840)(1−cos ω)`.

This is strictly positive for `ω∉2πZ`, giving a quantified constructive-interference maximum at zero *source-time frequency*. For `M_r=Σn^r c_n`, all moments exist and `d²|𝓕(ω)|²/dω²|_(ω=0)=−2(M_0M_2−M_1²)<0`. The positive source-time variance is sufficient and the exact coefficient is source-specific; **the qualitative gap is generic for any positive source with adjacent nonzero weights**.

**Countermodel:** the same original forcing with homogeneous seed `s=−π/16` has exactly the same `𝓕`, gap, and prime-event labels while its completed *real phase* is identically zero. The gap cannot imply R0 or π normality by itself.

## CFA-07 — Covariant Fourier atoms of the exact affine causal BBP path (EXACT)

For any finite forcing word `(a_1,…,a_n)` and initial real/rational lift `s`, the forward affine source law gives

`U_n=16^n s+Σ_(j=1)^n 16^(n−j)a_j`.

The real additive character then factors *exactly*, with transported frequency:

`e(h U_n)=e(h16^n s) Π_(j=1)^n e(h16^(n−j)a_j)`.

This is not `Π_j e(h a_j)`: the semidirect affine law `L_b∘L_a(u)=256u+16a+b` transports the dual label `h↦16h` between causal steps. The swap contrast is `L_b∘L_a − L_a∘L_b =15(a−b)`, recovering the native affine source-order contrast already analyzed in #670.

For the original infinite BBP source, `x=Σ_(j≥1)16^(−j)r(j)` and original seed zero, the completed real phase has the convergent product

`e(h16^n x)=Π_(j≥1)e(h16^(n−j)r(j))`.

For `j>n`, `h16^(n−j)` is generally nonintegral; it is a character of the **real source coordinate**, not a well-defined character of an independently reduced circle source term. Preserve the integer lifts and the order. The suffix is the exact compensating BBP future tail, not a physically executed backward-time action.

For rational terminal `M≥n`, define `P_M=Σ_(j=1)^M c_j`, `T_n^[M]=Σ_(j=n+1)^M16^(n−j)r(j)`; then

`U_n+T_n^[M]=16^nP_M`, and `T_(n+1)^[M]−16T_n^[M]=−r(n+1)`.

These finite identities preserve the original source and source-derived completion (credited to #672). For a shell `[B,2B)`, select `M=2B`; using `0<T_M<r(M+1)/15<1/(64M²)`,

`|e(h16^n x)−e(h16^nP_M)| < 2π|h|/(4096B²)` for every such n, so the corresponding shell means obey the same error bound. **The error transport is proved; a nontrivial signed shell bound is not.**

## CFA-08 — Spectral contrast: real-circle Koopman has only constant L² eigenfunctions (CLASSICAL)

Let `T_b:θ↦bθ mod1`, `b=16`, and `Kf=f∘T_b` on `L²(T,Haar)`. It is an isometry and satisfies `K e(hθ)=e(16hθ)` for integer Fourier modes `h`.

If `Kf=λf` with `f≠0`, isometry forces `|λ|=1`. The Fourier coefficients of `Kf` vanish at frequencies not divisible by 16; thus the same is true for `f`. Repeatedly dividing a nonzero Fourier frequency by 16 reaches an integer not divisible by 16, so every nonconstant Fourier coefficient must vanish. Therefore the only eigenfunctions are constants (λ=1).

For any fixed nonzero Fourier frequencies `h,k`, `⟨K^n e(hθ),e(kθ)⟩=1_(16^n h=k)`, hence the correlation vanishes for all sufficiently large `n`. By trigonometric approximation this is compatible with Haar mixing of the transformation. Yet a perfectly locked point `θ=0` satisfies `T_b^nθ=0` and is **not** Haar-generic. Haar ensemble spectral properties do not imply normality of the authenticated π point.

**Comparison:** the same geometric bookkeeping supports a full *pure-point* causal-clock eigenbasis on the 3-/5-adic odometers (CFA-03), while the real circle Haar Koopman has only constant eigenfunctions. These are different completed dynamical systems; no unproved eigenbasis conjugacy is inferred between them.

## CFA-09 — Identifiability versus asymptotic statistics (EXACT obstruction)

Knowing all source-time Fourier coefficients reconstructs every `r(n)` by Fourier inversion; the independent seed must be supplied separately. With original `s=0`, the full source does uniquely determine the completed real number `x` by BBP, so the specified phase orbit is not ambiguous as a mathematical sequence. But exact **construction** of every finite stage and knowledge of an exact generating rule do not give a uniform signed estimate for its infinite chronological averages.

Controls:

1. Same `r` with `s=−x`: source-time spectrum and p-square source events unchanged; completed orbit locked. This countermodel defeats **source/seed-blind deductions**, not arguments that actually use the authenticated zero seed.
2. Shift `s=1/16`: every late real-circle phase `n≥1` aliases the zero-seeded phase, so an unwrapped source/seed journal is indispensable for *source identification* even if late orbit statistics agree.
3. Matched-first-jet mutant `Q*(t)=Q(t)+(1−t)^2` has positive forcing and a nonzero source-time Fourier gap, but source p-square residue 5 versus authentic 4; this defeats universal positivity-based source identification.
4. Constant-forcing geometric clock is a valid 3/5 odometer and can have a completely locked completed real-circle orbit. Thus p-adic clock Fourier activity cannot by itself imply real-phase anti-lock.
5. The 11-adic filter in #670 arises in a separately declared auxiliary Fibonacci representation. It is **not** replaced or authenticated as a π-phase factor map by the 3/5 geometric clock.

## CFA-10 — The remaining constructive-atom proof obligation (UNVERIFIED)

Let `z_n=e(h16^n x)` be the *authentic* original-zero completed phase. For R0, prove an independently source-derived estimate on every late integer shell, e.g. a signed Gaussian/winding/cofactor witness as in #672/#673, or a positive lower density of genuine hexadecimal domain walls as in #662. For full normality, derive `W_B(h)→0` for every integer `h≠0` (equivalently, vanishing authentic Gaussian/Borwein Haar discrepancy). All frame transports, integer carries, p-primary complements and terminal tail must be retained.

An enticing but **invalid** final step would identify the p-adic odometer eigenfrequencies or the positive source-time gap with the real-phase Weyl frequencies. The missing mathematical arrow is a **source-anchored, correctly conditioned, signed joint spectral transport with an independent all-shell saving**. No such arrow is proved here.

## Verdict

**SURVIVES:** The user's `causality → bookkeeping → compatible Fourier forms` can be implemented exactly for these declared additive and affine causal algebras, including a finite unitary clock/state Fourier basis change and an exact original BBP source-time Mellin–Fourier transform with quantified interference. The full mathematical assembly is carefully distinguished from classical antecedents; novelty beyond SUCC is not claimed.

**FAILS:** Ordinary Fourier characters/eigenmodes automatically appear in every arbitrary causal system; the naive additive state characters diagonalize the 3/5 affine successor at every resolution; a positive source-time spectral gap or pure-point clock spectrum implies π-normality. Receipts: CFA-01/03/06/08/09.

**OPEN:** A source-derived signed cross-spectrum that transfers arithmetic causal structure into uniform real-phase anti-lock, R0 and full π normality, any physical claim that arithmetic Fourier modes are thermodynamic energy, and nonclassical-carrier inference without a distinct measurement/control protocol.
