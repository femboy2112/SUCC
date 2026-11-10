# π Fourier via exact additive-adelic gluing; full-conductor no-go; critical source holonomy

**Research checkpoint, 2026-11-08. Base-16 normality of π OPEN, selected signed Weyl decay OPEN, RH OPEN.** This branch is a strictly additive child of #556 at `f999bdd8ebd90c80e06a1484e128d1dda31d2fb6`, with #544, #554 and #555 inspected read-only. No frozen source, zero seed, provenance, formal, main, or historical research has been edited. `PROVED LOCAL` denotes a complete paper derivation and scope-appropriate finite tests, **not** Lean verification or independent scholarly referee review.

## Objects, notation, and source contract

Write `e(t)=exp(2πit)`. The **authentic** original four-pole forcing is

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`;
`U_0=0`, `U_(n+1)=16 U_n+r(n+1)`, `U_n=a_n/d_n` in lowest terms (`d_n>0`).

All states and all proofs referring to their denominators use the **unwrapped** rational state. Main XXI's authenticated `duck_bbp.forcing` is imported, not reconstructed in the research code. The completed source identity and tail are

`U_n+T_n=16^(n−1) π`, with `0<T_n≤1/[15(n+1)²]`, for n≥1.

For a rational x=a/d in lowest terms, with d positive, and a prime p with `p^v || d`, define the canonical p-adic **additive** fractional part

`[x]_p = (a * (d/p^v)^(-1) mod p^v)/p^v ∈ [0,1)∩Q`, if v≥1, else zero.

This is the fractional part of x as an element of Q_p, modulo Z_p. It is not `x mod 1` in R and is **not** a multiplicative valuation. Local additive characters with the conventional negative sign are `ψ_p(x)=e(−[x]_p)`; at the real place `ψ_∞(x)=e(x)`.

## AAG-01. Full additive product formula and complete finite-place phase reconstruction (CLASSICAL + ORIGINAL-SOURCE COROLLARY)

For every x∈Q and integer h,

`e(h x) = product_(p|den(x)) e(h [x]_p)` **exactly**.          (AAG1)

Equivalently, `ψ_∞(h x) product_p ψ_p(h x)=1`, where all but finitely many p factors equal one. This is the classical additive product formula for Q, **distinct** from #556's multiplicative formula `|x|_∞ product_p |x|_p=1`.

**Elementary proof.** Let `d=product p^v`, and set `m_p=d/p^v`, `t_p≡a m_p^(-1) mod p^v` in `0..p^v−1`. Then `S=sum_(p|d) t_p m_p` has `S≡a mod p^v` for each p: all other terms contain p^v. CRT gives `S≡a mod d`. Thus `sum t_p/p^v −a/d=(S−a)/d∈Z`. Apply `e(h·)`. Negative rationals and integers are included, with the reduced denominator convention.

**Source corollary.** Original r(j) denominators have only odd prime factors ≤8j−3, so by induction the reduced denominator d_n of U_n is **odd**, and every p|d_n obeys `p≤8n−3`. Therefore, for every n≥1,

`e(h U_n)=product_(p|d_n, p odd) e(h[U_n]_p)` **exactly**. (AAG2)

The full selected real character needs **no independent real/complement input at finite n** once all actual p-primary rational data are retained. This is a phase identity, not an independence assumption, an infinite distribution law, or a proof of normality. Finite p-adic **valuations alone** cannot reconstruct the characters: the residue/unit information `t_p` is essential.

## AAG-02. Every source step commutes with all-place additive character transport (PROVED LOCAL)

The map `x -> [x]_p mod Z`, from Q to Q/Z, is additive, since `x−[x]_p∈Z_p` and Z_p is an additive subgroup. Therefore for all n≥0, all primes p,

`[U_(n+1)]_p ≡16[U_n]_p+[r(n+1)]_p (mod 1)`. (AAG3)

Equivalently, for `z_(p,n)(h)=e(h[U_n]_p)` and `j_(p,n)(h)=e(h[r(n)]_p)`, 

`z_(p,n+1)(h)=z_(p,n)(h)^16 j_(p,n+1)(h)`.

Multiplying over all primes gives the authentic real recurrence because AAG1 applies to r(n+1): `e(hU_(n+1))=e(16hU_n)e(hr(n+1))`. Thus every observation origin/finite-time composition agrees with the original source dynamics; the diagram commutes at the **full character** level. Each n uses a finite product; **uniform convergence in n over an infinite changing prime support is not asserted**.

**π-place paid boundary.** By the inherited Green completion and `|e(x)-e(y)|≤2π|x−y|`,

`|e(h16^(n−1)π)−product_p e(h[U_n]_p)|≤2π|h|/[15(n+1)²]`.

For the actual dyadic epoch average, since `sum_(n=A)^(2A−1)(n+1)^−2 ≤1/(2A)`,

`|W_A^π(h)−(1/A)sum_(n=A)^(2A−1) product_p z_(p,n)(h)| ≤ π|h|/(15A²)`. (AAG4)

This is a genuinely phase-preserving, source-authenticated **finite-place pin of the analytic π orbit up to paid O_h(A^-2) error**. The *decay of its average* remains OPEN, since exact source reconstruction does not imply cancellation.

## AAG-03. The balanced-prime real complement is exactly the other-prime product (PROVED LOCAL)

Fix a prime `p≡1 (mod8)` in #554's **first simple-pole shell**, with every relevant source pole below p², and use its zero-initial p-primary history `C_p(n)=p U_n mod p∈{0,...,p−1}`. For these times, `p U_n∈Z_p`, so `[U_n]_p=C_p(n)/p` **exactly** as a rational in [0,1). Thus #554's exact factorization

`a_(p,n)(h)=e(h C_p(n)/p)`, `b_(p,n)(h)=e(h(U_n−C_p(n)/p))`

obeys

`b_(p,n)(h)=product_(q|d_n, q≠p) e(h[U_n]_q)`. (AAG5)

This is a **stronger source-map** than an abstract analytic complement: every complementary phase is itself exactly the full product of the other finite prime characters. There is no extra unknown real coordinate in finite rational U_n; the obstacle is their **signed chronological joint correlation**.

Write `J_(p,n)=(p r(n) mod p)` in the p-integral residue ring, with J=0 away from actual p-pole events, and `C_p(n+1)≡16C_p(n)+J_(p,n+1) mod p`. Then exactly

`b_(p,n+1)(h) = b_(p,n)(h)^16 e(h [r(n+1)−J_(p,n+1)/p])`. (AAG6)

The square brackets here are grouping of a **real rational argument**, not the p-adic fractional-part symbol. This identity retains the genuine four source births at times `k+1,4k+1,5k+1,6k+1` when `p=8k+1`, every fractional/integer carry and exact source forcing. Between those four events J=0, so the real complement is an almost-homogeneous ×16 trajectory with a small forcing r(n). It is **not** a stationary random phase. No source-selected decay follows. A rational p-integral seed perturbation preserves C_p and changes b, so the identity itself cannot choose the zero seed.

## AAG-04. Exact full-conductor Haar and full-band Parseval no-go (PROVED LOCAL)

For epoch `[A,2A)`, let `Q_A=lcm(d_A,...,d_(2A−1))` and set `t_n=Q_A{U_n}∈Z/Q_A`. Let `s_A` be the number of distinct t_n (≤A), and let `μ_A` be their empirical measure. When Q_A≥A, each occupied residue has mass ≥1/A≥1/Q_A, hence

`TV(μ_A,Haar_(Q_A))=1−s_A/Q_A≥1−A/Q_A`. (AAG7)

This says the full uncompressed finite-CRT empirical measure cannot approach Haar in total variation if Q_A/A→∞. In SUCC this last growth is assured by the already inherited original denominator theorem #532 (PF7): `log d_n≥(5−o(1))n` (with the usual meaning of liminf), and `Q_A≥d_(2A−1)`.

Define `W_(A,Q)(j)=(1/A)sum_(n=A)^(2A−1)e(j t_n/Q)`. Finite-group Parseval gives the **exact** identity

`sum_(j=1)^(Q−1)|W_(A,Q)(j)|² = (Q/A²)sum_(t modQ) count(t)²−1≥Q/A−1`. (AAG8)

**Proof.** Expand the squares, use `sum_(j=0)^(Q−1)e(j(x−y)/Q)=Q·1_(x=y)`, subtract j=0 term 1. The diagonal contribution is A, so the stated lower bound follows. Thus **simultaneous full-conductor Fourier whitening is impossible at scale A**, even if every fixed ordinary integer h eventually cancels.

Counterexample (REFUTED FULL-HAAR SHORTCUT): in Q=4000, the four addresses `0,1000,2000,3000` give `W(1)=0` exactly, while `TV=999/1000` and `sum_(j≠0)|W(j)|²=999`. Single-frequency cancellation, full Haar, and full-spectrum energy are distinct targets. At realistic Q_A, the gap is exponentially severe. A coarse observation with at most O(A) effective cells is not ruled out by this simple cardinality argument; it still needs a genuine source bound.

## AAG-05. Critical scale source-defect holonomy: explicit non-Haar log-periodic structure (PROVED LOCAL)

Import **ASG-02 from #556**, already paper-proved for the original four poles: with `F_(n,k)=U_(n+k)−16^k U_n`, `c_k=(16^k−1)/64`, `β_k=−7/8+2k/(16^k−1)`, for all n,k≥1,

`|F_(n,k)/c_k − 1/n²−β_k/n³| ≤ (298/25)/n⁴`, `|β_k|≤7/8`.

Define `Θ_(A,k)=sum_(n=A)^(2A−1) F_(n,k)` and the **scalar source-defect character** `H_(A,k)(h)=e(h Θ_(A,k))`, which also equals the product over observations of the *transported* ratios `e(h(U_(n+k)−16^k U_n))`.

**All integer A,k≥1, no growth restriction:**

`|Θ_(A,k)−(16^k−1)/(128A)| ≤ 7(16^k−1)/(32 A²)`. (AAG9)

**Proof.** For f(x)=x^-2, summing right-end integral discrepancies gives

`0≤sum_(n=A)^(2A−1)n^-2−∫_A^(2A)x^-2dx≤sum_(n=A)^(2A−1)(n^-2−(n+1)^-2)≤3/(4A²)`.

The integral is `1/(2A)`; also `sum n^-3≤1/A²`, `sum n^-4≤1/A³≤1/A²`. Substitute ASG-02 and bound the normalized residual by `3/4+7/8+298/25=13.545<14`; multiply `14c_k/A²=7(16^k−1)/(32A²)`.

For `A≥2` set `k_A=max(1,ceil(log_16 A))`. Then `1≤16^(k_A)/A<16` (except the first interval, where the same weaker bound holds), so

`Θ_(A,k_A) = (16^(k_A)−1)/(128A)+O(A^-1)`;
`(16^(k_A)−1)/(128A)∈[1/128−1/(128A),1/8]`.

More explicitly for every `A≥M≥32`,

`|Θ_(A,k_A)−17/256| ≤15/256+449/(128M) <1/4` turns. (AAG10)

Therefore the *rotated real part* of every h=1 source holonomy is bounded below by

`Re(e(−17/256) H_(A,k_A)(1)) ≥ cos[2π(15/256+449/(128M))] >0`.

**Every nonnegative normalized weighted average across arbitrarily many observation scales A≥M satisfies the same positive lower bound**. As M→∞ this bound approaches `cos(15π/128)>0`. This refutes the proposal that merely averaging compatible *source-defect scalar* holonomies over all large scales will produce Haar cancellation. The object is seed-independent and its modulus is exactly one; it is **not** W_A(h).

For any fixed integer t, along `A=16^m`, `k=m+t≥1`, the exact limit is

`H_(16^m,m+t)(h) → e(h16^t/128)` for each fixed integer h. (AAG11)

This is a **source-selected critical-scale phase**, not a contraction, entropy production, physical heat dynamics, or a π-normality estimate.

## AAG-06. The critical scalar holonomy is NOT a same-π cohomological invariant (PROVED LOCAL)

Use draft #555's rational null/coboundary `g_n=n/[257(2n+1)^3]`, `g_0=0`, and the *different source* `r'(n)=r(n)+g_n−16g_(n−1)` with `U'_n=U_n+g_n`. This source has the same completed constant as original and the same normality question; **it is NOT the frozen original four-pole source**. Its affine defect is

`F'_(n,k)−F_(n,k)=g_(n+k)−16^k g_n` exactly.

Summing over the epoch yields

`| (Θ'_(A,k)−Θ_(A,k)) +16^k/(4112A) |
 ≤ 9·16^k/(8224A²) + 1/(2056A)`. (AAG12)

**Proof.** `g_n=[2056n²]^-1(1+1/(2n))^-3` and `|g_n−1/(2056n²)|≤3/(4112n³)`. The same right-end integral comparison gives `|sum_(A<=n<2A)g_n−1/(4112A)|≤9/(8224A²)`. Also `0≤sum g_(n+k)≤1/(2056A)`. Substituting proves the bound.

Therefore on `A=16^m`, `k=m+t`:

`H'_(A,k)(h)/H_(A,k)(h) → e(−h16^t/4112)`. (AAG13)

For t=0,h=1 the limiting phase is genuinely not one, despite unchanged completed π constant and asymptotically identical fixed-h Weyl means (because g_n→0). This **refutes source-holonomy as an intrinsic normality invariant** under even a vanishing source coboundary, unless the exact four-pole source class is retained. It also shows why all-scale compatibility is a property of a chosen *presentation*, not by itself a forcing law for π's digit statistics.

## AAG-07. Original-zero signed gate is still OPEN (precise unresolved equation)

By AAG1–AAG4, for every integer A≥1 and fixed h≠0,

`W_A(h)=(1/A)sum_(n=A)^(2A−1) product_(p|d_n) e(h[U_n]_p)` **exactly**.

Selecting #554's genuinely balanced p≈(12/5)A and splitting AAG5 gives

`W_A(h)=(1/A)sum_(n=A)^(2A−1) a_(p,n)(h) product_(q≠p) e(h[U_n]_q)`.

#554 controls one local p-marginal under classical inputs, including incomplete Gauss completion, but **not** the signed joint correlation with the other-prime product. Its forcing-corrected van der Corput condition `limsup R^bal_(A,h)(H_A)≤0` remains OPEN. Our new exact additive arithmetic removes no cross term. ASG magnitude pressure and AAG scalar holonomy cannot prove it. The coherent counterseed, no-oracle rational dyadic shadows, CB-3 seeds, and GA-09 grid must still falsify any candidate that is not genuinely zero-selective.

**Strongest new interpretation:** finite places can fully pin every finite rational π-orbit phase, and the analytic completion has a paid O_h(A^-2) error; the unsolved theorem is *chronological signed multi-prime nonconspiracy*, not an unknown finite rational source map. This is a pathway improvement, not proof of normality.

## Sources, provenance, and claim authority

- Main: `observational_succ.duck_bbp`, `integer_bbp_carrier`, `selected_orbit`, `docs/PI_NORMALITY_FRONTIER.md`, and Main XXI claim/handoff contracts; frozen and read-only.
- Parent #556 `research/2026-11-08/scale_adelic_thermal_gluing/PROOFS.md` (ASG-01–07, especially uniform ASG-02), parent exact test/oracle.
- Sibling #554 `three_channel_prime_tomography/BALANCED_EPOCH.md`, including the p∤h qualification and corrected dyadic counterseed averaging; sibling #544 signed carry/Poisson observer. Sibling #555 `origin_locked_spectral_fingerprint/THEOREMS.md` for the vanishing rational coboundary and same-π status. These are **READ-ONLY**, not silently merged.
- Classical additive adelic product formula and Schwartz–Bruhat characters: Tate's thesis / Warwick Tate notes `https://warwick.ac.uk/fac/sci/maths/people/staff/sheth/tatesthesis_notes.pdf`. Classical finite CRT and character orthogonality underlie AAG1/AAG8. No academic priority claimed for them.
- Validation: root-discoverable tests in `tests/test_adelic_additive_gluing.py`; preregistered fresh signed clocks in `PREREGISTRATION.md` and `FINITE_DIAGNOSTICS.json` are finite high-precision numerical **diagnostics**, not asymptotic proofs. Full inherited SUCC 12k+ suite and Lean for new results have not been run locally.
