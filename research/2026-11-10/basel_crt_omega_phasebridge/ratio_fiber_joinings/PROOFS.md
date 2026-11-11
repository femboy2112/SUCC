# The 3/2 ratio fiber: two-to-three invariant joinings, signed controls, and original-zero π receipts

**Research continuation:** 2026-11-10, child of SUCC draft PR #588 (`896c9ff3ceec5eb062a72cf5fc9230b6f80e2467`), itself stacked on #585 → #584. **π hexadecimal normality, odd-eight original-zero Weyl decay, and RH remain OPEN.** These are additive, explicitly scoped theorems and probes; no frozen BBP source, archives, Lean, provenance, or main updates. No novelty/priority claim.

## 0. Authentic object and exact source contract

For `e(t)=exp(2πit)`, integer `h≠0`, phase parameter `α=π+16u`, and the unchanged BBP source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,
\qquad U_n=16U_{n-1}+r(n),
\]

`u=0` selects `α=π` and `Y_n(u)=16^{n-1}α`. For `A≥2` define

\[
J_A=\{\ell\ge1:A\le2\ell,3\ell<2A\}
=\{\lceil A/2\rceil,\ldots,\lfloor(2A-1)/3\rfloor\},
\quad L_A=|J_A|=A/6+O(1).
\]

Only use `T_{A,h}` when `L_A>0`:

\[
\boxed{T_{A,h}(\alpha)=\frac1{L_A}\sum_{\ell\in J_A}
 e\big(h\alpha K_\ell\big),\quad
 K_\ell=16^{2\ell-1}(16^\ell-1)
 =16^{3\ell-1}-16^{2\ell-1}.}
\tag{FIBER}
\]

It is the *mixed diagonal Fourier character* of the empirical two-time joining

\[
\nu_{A,\alpha}=\frac1{L_A}\sum_{\ell\in J_A}
\delta_{(\{16^{2\ell-1}\alpha\},\{16^{3\ell-1}\alpha\})},
\quad T_{A,h}=\int_{\mathbb T^2}e(h(y-x))\,d\nu_{A,\alpha}.
\tag{JOINING}
\]

The marginal single-orbit Weyl statistic `A^{-1}Σ_(A≤n<2A)e(h16^(n−1)α)` is a DIFFERENT observable. Any asymptotic implication between them is a separate proof obligation. The Weil explicit formula's *direct* prime-power terms do not acquire a `3/2` atom: see inherited #588. Keep the literal source, seed, winding, and all old prime powers in any further transport.

## 1. Theorem FJ-01: explicit, opposite-sign invariant 2→3 Haar joinings

**Status: DISCLOSED by the elementary construction/proof below. Domain:** integer base `b=16`, two dilation maps `T^2(x)=16²x mod1` and `T^3(y)=16³y mod1`. Fix a twist `δ∈{0,1}`. Independently sample digits `X_0,X_1,…` and `Z_0,Z_1,…`, each uniform in `{0,…,15}`. Define

\[
Y_{3r}=(X_{2r}+\delta)\bmod16,\quad
Y_{3r+1}=X_{2r+1},\quad Y_{3r+2}=Z_r
\qquad(r\ge0).
\tag{2:3-PACKET}
\]

Let `x=.X_0X_1…` and `y=.Y_0Y_1…` in base 16, and denote their joint law by `ν_δ` on the two-torus. Every `X_i` is independent and uniform. Every `Y_j` is likewise independent and uniform: the map `X_(2r)↦X_(2r)+δ` is a digit permutation, while `X_(2r+1)` and `Z_r` are distinct independent variables. Thus **both marginals are exactly Lebesgue/Haar**. Shifting `x` by 2 digits and `y` by 3 digits advances the independent block index `r` by one. Hence `ν_δ` is invariant under `(T²,T³)`.

The first TWO base-16 digits of `x` and `y` agree except that the first digit of `y` is shifted by `δ`. Splitting off those digits,

\[
y-x=\frac{[(X_0+\delta)\bmod16]-X_0}{16}+\epsilon,
\qquad |\epsilon|\le16^{-2}.
\]

For odd-eight `h=8`, the first contribution is a half-integer phase of parity `δ`, including the wrap `15→0`. Therefore

\[
\boxed{(-1)^\delta\Re \int e(8(y-x))\,d\nu_\delta(x,y)
\ge\cos(\pi/16)>0.9807.}
\tag{TWIST-CONTRAST}
\]

This is an **operational two-frame twist** with declared relative digit parity and a common basis. It is NOT a scalar Wilson-loop holonomy (vertex phase products still telescope to 1); nor is it a quantum phase, an RH result, or an inference from marginal Haar to joint Haar. In particular both joinings share identical *complete* Haar marginals, but have nearly opposite mixed Fourier coefficients. The product joining has zero nontrivial mixed coefficients; neither `ν_0` nor `ν_1` is that joining.

## 2. Theorem FJ-02: the joinings are realized by base-16 NORMAL single orbits

**Status: DISCLOSED via variance/Borel–Cantelli.** Define the *injective two-to-three successor* on positive integers `n≥2`:

\[
f(n)=\lfloor3n/2\rfloor,\qquad
f(2\ell)=3\ell,\quad f(2\ell+1)=3\ell+1.
\tag{TWO-TO-THREE}
\]

`f` is strictly increasing and `f(n)≥4n/3>n`; its forward-orbit graph is disjoint union of chains. Each integer `n≥2` has at most one predecessor, and each chain intersects `[1,N]` in at most `1+\log_{4/3}N` sites.

Independently assign a uniform hexadecimal digit to each chain root. Along every arrow `n→f(n)`, copy the digit if `n` is odd, and add `δ (mod 16)` if `n` is even. Write the resulting digit string as `d_n^(δ)` and its number as `α_δ=Σ_(n≥1)d_n^(δ)16^(−n)`.

The equalities

\[
\boxed{d_{3\ell}=d_{2\ell}+\delta\pmod{16},\qquad
 d_{3\ell+1}=d_{2\ell+1}}
\tag{CHAIN-COPY}
\]

hold for **every** `\ell`. Thus for every nonempty epoch, by the same two-digit argument,

\[
\boxed{(-1)^\delta\Re T_{A,8}(\alpha_\delta)
\ge\cos(\pi/16)>0.9807.}
\tag{NORMAL-COHERENCE}
\]

**Normality proof, not an appeal to genericity:** For any fixed word length `k`, two distinct members `n<m` of one chain have `m≥4n/3`. Once `n>3k`, the `k` consecutive digits beginning at `n` belong to *distinct* chains and are therefore independent uniform symbols, even after the deterministic modulo-16 shifts. Thus each fixed word `w` of length `k` occurs at a start `n>3k` with probability exactly `16^(−k)`.

Let `Z_n(w)` be its occurrence indicator and `C_N(w)=Σ_(n≤N)Z_n(w)`. Two indicators are independent unless their k-site blocks share a chain. Up to site `N+k`, any chain has `O(log(N+k))` members; one length-k window touches at most `k` chains, each member belongs to at most `k` window starts. The dependency degree is at most `k²(1+log_(4/3)(N+k))`. Hence

\[
\mathbb E C_N(w)=16^{-k}N+O(k),\qquad
\operatorname{Var}C_N(w)=O_k(N\log(N+2)).
\]

Chebyshev at the square checkpoints `N_j=j²` gives `Pr(|C_(N_j)/N_j−16^(−k)|>ε)≪_(k,ε)log(j)/j²`, summable. Borel–Cantelli gives convergence almost surely along the squares. Since successive squares have relative gap tending to zero and indicators are between zero and one, this extends to all `N`. Intersect the probability-one events for all finite words. **Therefore for each δ, almost every chain assignment gives a base-16 NORMAL α_δ satisfying NORMAL-COHERENCE for every A.** This is a quantified construction, not a single finite pseudorandom output being certified normal.

Moreover, the empirical pair measures `ν_(A,αδ)` converge almost surely (on cylinder sets, hence weakly) to the *explicit* `ν_δ` in FJ-01. For each fixed pair of finite digit windows and sufficiently large `\ell`, the only shared chain between the windows at `2\ell+i` and `3\ell+j` is at `j=\lfloor3i/2\rfloor`, while there are no within-window identifications. Thus its pair-word law is precisely the independent 2:3-PACKET law. Across `\ell`, the indicators have the same `O_k(log A)` dependency bound. The previous square-checkpoint argument proves joint empirical convergence, with the start-set `J_A` a contiguous interval of growing size; convergence of global prefixes transfers to intervals `[A/2,2A/3]` by subtraction and the fixed positive relative length. This establishes a **nonproduct invariant joining realized by a single normal radix-16 orbit**, with sign tunable by one digit twist.

**Crucible:** This proves that original-zero ratio-fiber cancellation, if ever established, would be stronger than base-16 normality; it cannot be deduced from normality or from the two Haar marginals. A theorem tailored to the authentic `α=π` may still succeed, but must reject these *other-seed* source controls.

## 3. Theorem FJ-03: exact NONNORMAL fiber cancellation (period-nine arithmetic)

**Status: DISCLOSED finite cyclotomic identity.** Take `α=1/9`, which has a finite, periodic radix-16 orbit since `16^3≡1 (mod 9)`. For all `\ell≥1`,

\[
K_\ell\equiv
\begin{cases}6&\ell\equiv1\pmod3,\\3&\ell\equiv2\pmod3,\\0&\ell\equiv0\pmod3.\end{cases}\pmod9.
\]

For every `h` with `3∤h`, each consecutive triplet of fiber characters is a permutation of `1,ω,ω²` for `ω=e(1/3)`, so it sums to zero. **For arbitrary consecutive `J_A`, at most two leftovers remain:**

\[
\boxed{|T_{A,h}(1/9)|\le2/L_A=O(1/A),\qquad 3\nmid h.}
\tag{PERIODIC-FALSE-POSITIVE}
\]

In particular the actual odd-eight `h=8` fiber cancels although `α=1/9` is nonnormal. For `h=24` the claim does NOT apply (3 divides 24). Hence *one fiber mode* is not a sufficient normality criterion. Combined with FJ-02, single-mode fiber cancellation and ordinary base-16 normality are **logically incomparable** among real starting phases.

## 4. Theorem FJ-04: universal irrational anti-locking, but NOT density

The integer exponent obeys

\[
K_{\ell+2}=4352K_{\ell+1}-1048576K_\ell,
\quad \lambda_1=256,\lambda_2=4096.
\tag{RECURRENCE}
\]

**Status: DISCLOSED.** Let `α` irrational and `h≠0` an integer. Then

\[
\boxed{\limsup_{\ell\to\infty}\|h\alpha K_\ell\|_{\mathbb R/\mathbb Z}
\ge\frac1{1+4352+1048576}=
\frac1{1052929}.}
\tag{ANTI-LOCK}
\]

**Proof:** If the limsup were smaller than `1/1052929`, then eventually choose the nearest integers `z_ell` so the remainders `r_ell=hαK_ell-z_ell` satisfy `|r_ell|<1/1052929`. The integer residual of RECURRENCE on the `z_ell` has absolute value strictly less than `(1+4352+1048576)/1052929=1`; hence it equals 0. The bounded `r_ell` then satisfy RECURRENCE exactly. Its characteristic roots 256 and 4096 both exceed 1, so its only bounded real solution on an infinite forward tail is identically zero. Thus `hαK_ell` is integer for every sufficiently large ell, forcing `α` rational: contradiction. ∎

**Not a cancellation estimate.** The limsup statement allows rare excursions with arbitrarily long coherent stretches. For instance choose `N_j=2^(2^j)` and `α=Σ_(j≥1)16^(−N_j)`, an irrational with isolated 1 digits. With `A_j=N_(j+1)/4` for `j≥2`, the indices `2ell,3ell∈[A_j,2A_j)` all lie far between successive 1 digits. Their fractional phases are uniformly `O(16^(−N_(j+1)/2))`, so `T_(A_j,h)(α)→1` for every fixed h. All Kℓ still have the exact prime passport of inherited #588. Thus **irrationality, recurrence, all-prime divisibility, and a universal escape constant do NOT force average cancellation.**

The exact common gauge kernel is also revealing: `gcd(K_1,K_2)=240` and all Kℓ are multiples of 240, so `T_(A,h)(α+1/240)=T_(A,h)(α)` for every A,h. For all n≥2 this shift changes `16^(n−1)α mod1` by the *same* `1/15` rotation, leaving ordinary Weyl decay unchanged. This is a legitimate common-gauge identification, not a hidden Berry phase.

## 5. Theorem FJ-05: ensemble-resolution versus selected source, exact interval identity

For any finite nonempty integer index set `J` with distinct `K_ell` and `T_J(α)=|J|^(−1)Σ_(ell∈J)e(hK_ell α)`, any closed real interval `I=[a,b]`, width `w=b−a>0`, center `c=(a+b)/2`, one has **exactly**

\[
\boxed{\frac1w\int_I|T_J(\alpha)|^2d\alpha
=\frac1{|J|}+\frac1{|J|^2}\sum_{\ell\ne m}
 e\big(h(K_\ell-K_m)c\big)\,
\operatorname{sinc}\big(\pi h(K_\ell-K_m)w\big).}
\tag{LOCAL-ENSEMBLE}
\]

Here `sinc(x)=sin x/x` with value 1 at 0; the sum of off-diagonal conjugate pairs is real. The bound `|sinc t|≤min(1,1/|t|)` quantifies when an uncertainty ensemble effectively destroys all off-diagonal information. Conversely

\[
|T_J(\alpha)-T_J(\beta)|\le2\pi|h|K_{\max}|\alpha-\beta|.
\tag{RESOLUTION}
\]

Thus a BBP prefix interval narrow enough to *select* the original zero orbit is generally too narrow for a Haar-ensemble washout argument. Averaging the parameter over a broad interval may prove a generic statement but is **not** a source-specific estimate at π. This identity is independent of RH and the Weil formula; it diagnoses the precise map/selection defect.

## 6. Theorem FJ-06: exact original-zero π certified finite h=8 observations

**Status: DISCLOSED for the stated finite epochs by rational enclosures; NO asymptotic claim.** Freeze the non-dyadic inspection epochs `A=263,521,1031`, fixed `h=8`, before executing the final independent table. Let `K=2A+12` and `Q=16^K`. From the **original four-pole BBP** source and positivity of its `(1−x)` moment density, compute

\[
L_K=\sum_{n=1}^K\left\lfloor16^{K+1-n}r(n)\right\rfloor,
\qquad\boxed{L_K\le Q\pi<L_K+K+1.}
\tag{BBP-ENCLOSURE}
\]

Indeed the total term-floor deficit is `<K` and the positive tail, scaled by `Q`, is `<16/[(8K+1)(8K+2)]<1`. This is a rigorous original-source enclosure—not an imported digit table. For each `\ell`, multiply the ENTIRE rational interval by the integer `8K_ell` **before taking floors**; reject any unresolved integer crossing. To enclose the complex phase, reduce the rigorous fractional interval to outward decimal ticks, evaluate rational Taylor sine/cosine polynomials with Lagrange bounds, and enclose the required `2π` constant independently by Machin's classical `π=16atan(1/5)−4atan(1/239)` and alternating rational bounds.

All displayed real and imaginary intervals below are integers divided by `10^12` with **outward exact rounding**. `L_A=|J_A|`.

| A | L_A | Re T_(A,8)(π) interval (×10⁻¹²) | Im interval (×10⁻¹²) | equal first digit | equal first TWO digits | equal first-digit parity |
|---:|---:|---:|---:|---:|---:|---:|
| 263 | 44 | [−31276714603,−31276714602] | [−127208057554,−127208057553] | 4 | 0 | 24 |
| 521 | 87 | [88010046868,88010046869] | [44604117458,44604117459] | 11 | 0 | 50 |
| 1031 | 172 | [54382687585,54382687586] | [−2937036627,−2937036626] | 5 | 1 | 88 |

The finite phases have magnitudes approximately 0.1310, 0.0987 and 0.0545, respectively. These observations **do not establish a decreasing sequence or a future asymptotic rate**. Unlike the engineered twist joinings, the original π source does not have uniform two-digit copying on these windows. The sample is non-blind and the independent Machin check shares the same researcher; no independent external refereeing or new Lean proof is claimed.

**Reproduce:** `python -W error -m unittest -q test_ratio_fullblast.py` in this directory; `python certified_fiber.py 263`, similarly for 521/1031; and `python -m unittest` is NOT meant to launch the parent ~13k suite for this isolated draft.

## 7. Exact status and next falsification opportunity

- **DISCLOSED (paper elementary, scoped):** invariant 2:3 joinings, normal single-orbit realization with opposite h=8 mixed sign, exact periodic false positive, recurrence anti-locking, interval energy identity, and finite original-source rational enclosures.
- **OBSERVED (local):** 13 focused stdlib unit tests; exact rational output intervals and source digit comparisons. Other repo tests/hosted CI/Lean were not executed this round.
- **REFUTED by explicit controls:** 'marginal Haar implies mixed h=8 fiber decay'; 'normality implies 3/2 fiber h=8 decay'; 'single-mode 3/2 fiber decay implies normality'; 'π irrationality + all-prime K passport forces cancellation'; and 'averaging source uncertainty is the same as selecting original zero'.
- **UNVERIFIED / OPEN:** source-selected `T_(A,8)(π)→0`, and even if proved, a transport to ordinary signed Basel/Weyl decay; π base-16 normality and RH; a completed Weil source-selected inequality that controls the mixed joining coefficient. None of these is promoted by the finite table.

**Minimal next probe:** construct a BBP-forcing, literal-zero, signed coupling functional acting on the **two-time joining** `ν_(A,π)` and prove a bound that actually rules out both `ν_0` and `ν_1` as asymptotic source-selected models, while retaining PPP-08, the coherent zero-orbit seed, exact 2/3 multiplier clocks, old prime powers, and Archimedean carry. Do not silently replace a bounded-ratio phase by a Weil prime-power atom. Even this would target the *stronger mixed statistic*, not directly π normality; the primary normality gate remains all-mode `A F_h(A;0)→0` or the corresponding fully source-selected signed Weyl estimate in #585.

**Method/provenance:** inherited #588 `RATIO_FIBER_TORUS.md` and `WEIL_PACKET_PROOFS.md`, #585 `SIGNED_BASEL_TAUBERIAN.md`, #584 `docs/PI_NORMALITY_FRONTIER.md`, original BBP import and zero seed. Classical probabilistic tools used only as elementary Chebyshev, Borel–Cantelli and countable intersection, with full derivation; generic Haar character orthogonality is not a blind witness for π. For comparison with classical almost-everywhere equidistribution see Davenport–Erdős–LeVeque (1963), *On Weyl's criterion for uniform distribution* (primary historical PDF at `https://users.renyi.hu/~p_erdos/1963-13.pdf`).
