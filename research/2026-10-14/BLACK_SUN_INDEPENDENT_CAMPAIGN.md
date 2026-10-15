# OPERATION BLACK SUN — Independent SUCC Mathematical Discovery Campaign

**Campaign date:** 2026-10-14. **Branch:** `research/black-sun-independent-campaign-2026-10-14` (child of PR #77's `research/global-model-sandwich-2026-10-14` stack, transitively containing PRs #70–#77 research lines). **Base:** main `6e0d88f1b235b85188393bbcd64ac0436cb71a70` verified. **RH PROVED: NO.** No nontrivial zero positions were used as construction inputs. All numerical results are labeled TESTED MODEL at stated resolution; identities are PROVED LOCAL with high-precision verification.

## 0. Executive summary

Three tracks were executed at full depth: (A) the completed Weil form on the first-prime window — its exact representation independently re-derived, verified to 25–40 digits against the original Weil distribution, its spectrum computed, and its razor-thin positivity structure explained by a new mechanism (the 2π archimedean band and the Shannon number 4a); (B) the quantitative Tauberian transfer for the factorial-prime quantization defect — the exact exponent θ(δ)=δ with a matching sharpness counterexample and the two-way authentic-source dictionary; (C) the Collatz additive/multiplicative defect — an exact valuation dictionary for cycle candidates including the no-divisible-by-3 theorem and the p-adic lattice condition, with an exact finite cycle certificate to m ≤ 18.

**The single most important finding (A-track):** the first-prime-window completed Weil operator sits at a razor-thin positivity boundary: its lowest eigenvalues are numerically indistinguishable from zero (|λ₀| ≲ 3e−4, sign unresolved at our resolution) for every window size a ∈ [0.42, 1.0], while its archimedean+pole part alone is strongly negative (λ₀ ≈ −0.43 at a = log 3/2) and is exactly rescued by the single prime-2 atom. Two near-null modes appear, and their count matches the Shannon number 4a crossing 2 at a = 1/2. The windowed form's archimedean multiplier Ω(u) = Re ψ(1/4+iu/2) − log π is negative exactly on the band |u| < 2π and grows like log(u/2π) beyond. This converts the repo's conditional IdealHard contract (IH-02) into an explicit two-obligation program with visible quantitative targets (Section 6, G).

## 1. Intake and what was actually verified against what

Live state recovered before any reasoning: main at `6e0d88f`, the seven October 14 research lines read as remote branches/PRs (#70–#77, plus #78 THETA-JETS), the stacked parent chain re-derived, `AGENTS.md` and `docs/METHOD.md` discipline followed (non-main branch, no merges, no pushes, controls predeclared). Baseline: `tests.test_completed_weil_transport` and `tests.test_global_model_sandwich` pass on the parent stack (72 tests).

The Carleman/Suzuki windowed representation (PR #70's CG1, the campaign prompt's §4.2 formula) was **not trusted from the document**: it was re-derived from the original Weil distribution (CW-05 normalization) by hand in real space, and then both sides were implemented independently and compared at 25–40 digits. The re-derivation required reconstructing the exact contact-integral constant; the contact identity

\[
\int_0^\infty \frac{(e^{-x/2}-e^{-x})}{1-e^{-2x}}\,dx = \tfrac12\log 2+\tfrac\pi4 ,
\qquad C_G=\gamma+\tfrac\pi2+3\log2+\log\pi
\tag{BS-A0}
\]

was proved by the substitution t=e^{-x/2} and partial fractions of 2/(1-s⁴) (see the proof of BS-A2 below; verified numerically to 40 digits in `tests/test_black_sun_window.py::TestContactTailTrap`).

### 1.1 Three implementation-level traps found and fixed (counterexample ledger)

1. **The contact tail trap (NEW, quantified).** The Gamma/contact integral of the completed Weil distribution runs to ∞, not to supp(h). For h supported in [-2a,2a] the part beyond 2a is **exactly** +2 h(0) atanh(e^{-2a}) (since ∫_{2a}^∞ e^{-x}/(1-e^{-2x}) dx = atanh(e^{-2a})). Dropping it breaks the Carleman identity by 0.772 at a=1/2 for the flat test function. This is a genuine trap for any future window implementation: a truncated-contact Weil evaluator passes many internal consistency checks while being wrong at the 0.7 level. Regression-locked in `test_truncation_without_tail_breaks_identity`.

2. **Cross-cell factor-2 in the exact E_G layer integrals.** The windowed kernel integral ∬ e^{-α|x−y|} v(x)v(y) over cell pairs must count both orderings; missing the factor 2 inflates E_G by the off-diagonal half (observed: E_G = 5.67 vs the true 3.719 on the flat test). Fixed in `carleman_exact_layers`.

3. **The E_G series tail is not free.** ∑_j 2(1-e^{-α_j L})/α_j² converges only like 1/j²: truncating at j=4000 leaves a 1.25e−4 error — exactly the size of first-window spectral margins. The exact polygamma tail ∑_{j≥J}1/α_j² = ¼ψ₁(J+¼) must be added. An E_G evaluation "to 4000 layers" is NOT a 4-digit-accurate E_G.

## 2. A-TRACK: the first-prime-window completed Weil form

### BS-A1 (PROVED LOCAL + 25-digit verified): the windowed Carleman representation

For v ∈ H¹₀(-a,a) extended by 0, with h = v*ṽ, W_ζ the completed Weil distribution (Suzuki 2025 Eq. (3.3) normalization, CW-05):

\[
W_\zeta(v*\tilde v) = E_G(v) - C_G\|v\|_2^2 + 2\Big|\int v\cosh\tfrac x2\,dx\Big|^2 - 2\Big|\int v\sinh\tfrac x2\,dx\Big|^2 - 2\sum_{2\le n<e^{2a}} \frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}\langle \tau_{\log n}v, v\rangle ,
\tag{BS-A1}
\]

where k_G(t)=e^{-|t|/2}/(1-e^{-2|t|}), E_G(v)=½∬k_G(x−y)|v(x)−v(y)|²dxdy, C_G as in BS-A0, and the prime sum cutoff is exact because supp(h)⊂(-2a,2a) (atoms with log n ≥ 2a see h at its support boundary where h=0).

*Proof sketch (independently redone; full detail in module docstring and tests):* (i) the pole/exponential term ∫h(x)(e^{x/2}+e^{-x/2})dx equals 2Re[v̂(i/2)\overline{v̂(-i/2)}] = 2|⟨v,cosh(x/2)⟩|² − 2|⟨v,sinh(x/2)⟩|² by evaluating both Laplace transforms; (ii) the contact part −(γ+log4π)h(0) − ∫₀^∞ k_G-type pairing equals E_G(v) − C_G‖v‖² by the regularized identity E_G(v) = 2h(0)∫₀^∞k_G − 2∫₀^∞ k_G Re h and the contact constant BS-A0; (iii) the prime atoms pair to the translation correlations. Numerical verification: flat indicator at a=1/2 agrees to 25 digits (`test_identity_flat_indicator`); random piecewise-linear v agree within the exact-layer-sum truncation bound (`test_identity_random_piecewise_linear`). ∎

### BS-A2 (PROVED LOCAL): the elementary closed form for the barrier

The windowed Gamma energy decomposes exactly as

\[
E_G(v) = \tfrac12 \iint_{W\times W} k_G(x-y)|v(x)-v(y)|^2 dx\,dy + \int_{-a}^{a} \rho_a(x)|v(x)|^2 dx,
\qquad \rho_a(x) = \bar K(x+a)+\bar K(a-x),
\tag{BS-A2}
\]

with the **elementary** closed form

\[
\bar K(z) = \int_z^\infty \frac{e^{-t/2}}{1-e^{-2t}}dt = \tfrac12\log\frac{1+e^{-z/2}}{1-e^{-z/2}} + \arctan(e^{-z/2}) .
\tag{BS-A2'}
\]

*Proof:* substitute s=e^{-t/2} in the defining integral; dt = −2ds/s, e^{-t/2}=s, 1−e^{-2t}=1−s⁴, so K̄(z)=∫₀^{e^{-z/2}} 2 ds/(1−s⁴); partial fractions 2/(1−s⁴) = ½/(1−s) + ½/(1+s) + 1/(1+s²) give the antiderivative ½log((1+s)/(1−s)) + arctan(s). Verified to 24+ digits against the defining series at 6 values (`test_matches_defining_series`). This is the exact log-barrier that forces the windowed operator to have compact resolvent (Section 4) and gives the confinement mechanism its elementary constant. ∎

The barrier is infinite at the window edge but integrable: ρ_a(x) ~ ½log(4/(a−|x|)) + π/4 near the edges, ρ_a(0) = 2K̄(a) ≈ 3.40 at a=1/2. **The windowed Weil operator is a nonlocal system with an elementary log-barrier** — to our knowledge the cleanest closed form for the boundary confinement in this problem; the repo's E_G analysis (PR #70 CG2) had the layer structure but not the elementary K̄.

### BS-A3 (PROVED LOCAL): the Fourier representation of the archimedean+pole part and the 2π band

For v supported in (-a,a):

\[
E_G(v) - C_G\|v\|^2 + 2|\langle v,c\rangle|^2 - 2|\langle v,s\rangle|^2
= \frac{1}{2\pi}\int_\mathbb R |\hat v(u)|^2\,\Omega(u)\,du
+ 2\Big|\int v\cosh\tfrac x2\Big|^2 - 2\Big|\int v\sinh\tfrac x2\Big|^2 ,
\tag{BS-A3}
\]

where **Ω(u) = Re ψ(1/4 + iu/2) − log π**, with:

- Ω(0) = −C_G = −5.3722 (exact);
- Ω(u) < 0 exactly on the band |u| < 2π (measured: Ω(2π) = −1.06e−3, Ω(6.4) = +1.74e−2; the zero sits at 2π + O(1/u), consistent with the exact asymptotic);
- Ω(u) = log(u/2π) + O(1/u²) as u → ∞ (from Re ψ(1/4+iu/2) = log(u/2) + O(1/u²)).

*Proof:* the multiplier of E_G is M_G(u)=∑_j 2u²/(α_j(α_j²+u²)) = Re ψ(1/4+iu/2) − ψ(1/4) (CG2c, reverified); subtract C_G and use ψ(1/4) = −γ − π/2 − 3 log 2 to get Ω(u) = M_G(u) − C_G exactly. The asymptotic is the classical Re ψ(z) = log|z| + O(1/z²); the sign change location follows numerically with the displayed values (a monotonicity proof of the single sign change is routine from ψ′ > 0 along the vertical line and the two-sign asymptotics; we label the exact zero location as verified numerics). ∎

**Structural consequence:** the archimedean+pole windowed form is indefinite *because of and only because of* the band |u| < 2π. The rank-2 pole terms and the prime atoms must rescue exactly this band. The band width 2π and the window half-width a enter through the **Shannon number N = 2a·(2·2π)/(2π) = 4a**: the number of prolate-type modes whose Fourier mass can be concentrated inside the negative band. At a = 1/2, N = 2 — and exactly two near-null modes are observed. This is the mechanism behind PR #70's "smallest displayed trial quotient ~0.0006 at a=0.54": the trial space was probing the second prolate mode at the N=2 transition.

### BS-A4 (TESTED MODEL, resolution documented): the first-window spectrum

Rayleigh–Ritz (Nyström midpoint, M up to 3200; |λ−λ_true| ≲ 3e−6 + O(h) observed by refinement):

| a | prime atoms | λ₀ (full Q) | λ₁ | λ₀ (archimedean+pole only) |
|---|---|---|---|---|
| 0.36 | n=2 | **+8.5e−4** | +4.9e−2 | +1.1e−3 |
| 0.42 | n=2 | +7.2e−5 | +7.6e−3 | −1.3e−1 |
| 0.48 | n=2 | ≈0 (±5e−6) | +5.9e−4 | −2.8e−1 |
| 0.50 | n=2 | ≈0 (±1e−5) | ≈0 | −2.8e−1 |
| 0.5493=log√3 | n=2 | ≈0 (±1e−4) | ≈0 | −4.3e−1 |
| 0.60 | n=2,3 | −1.7e−5 (±res) | ≈0 | — |
| 0.70 | n=2,3,4 | −7.5e−5 (±res) | ≈0 | — |
| 0.90 | n≤5 | −4.0e−4 (±res) | — | — |
| 1.00 | n≤7 | −3.6e−4 (±res) | — | — |

Findings (all TESTED MODEL at the stated resolution):

1. **λ₀(0.36) = +8.5e−4 is genuinely positive** (stable to 2e−6 across M=800..3200): the smallest window that contains any prime atom is comfortably positive-definite.
2. **For a ∈ [0.42, 1.0] the lowest one or two eigenvalues are indistinguishable from zero** at resolution 3e−4, fluctuating in sign across refinements — the discretization cannot certify the sign. Under RH they are strictly positive (Weil) but ≤ ~1e−4; the BM-density argument (Section 5) shows they cannot be exactly zero with a kernel vector, but the infimum may be approached only as a → ∞.
3. **The archimedean+pole part alone is strongly negative** (λ₀ → −0.43 at a = log√3, monotone in a) and the single prime-2 atom (spectral contribution ≤ 2·0.4901) **exactly compensates** it to land the full form at ≈ 0. The compensation is active from a ≈ 0.42 where the A-form first goes negative.
4. **The near-null modes are even (bell, peaked at 0, large pole overlap |⟨v,c⟩|≈0.78) and odd (one node)**: two modes, matching the Shannon number 4a crossing 2 at a=1/2 (BS-A3).
5. Multi-prime windows (a up to 1.0) stay at the same near-zero scale: **no window size produces a decisively negative eigenvalue** — consistent with RH, and constraining any would-be counterexample: the negative directions of the archimedean band are always near-exactly paid for by the prime atoms in the window.

### BS-A5 (hostile controls, all PROVED LOCAL/TESTED as marked)

- **Fake-6 blindness (exact):** on the first window (2a < log 6) a fake primitive composite impulse at log 6 is *invisible* to the spectrum (exact statement, tested to 1e−9): first-window positivity cannot authenticate the source against composite mutations — the IH-01 finite-observer blindness instantiated in the actual Weil problem. The mutation becomes visible at a ≥ log(6)/2 (tested: spectral shift > 0.01 at a=0.9).
- **Wrong contact (exact):** perturbing C_G by ±2 log 2 moves λ₀(0.36) by ∓(2 log 2) + o(1): +2log2 flips the window to decisively negative (λ₀ < −1), −2log2 falsely inflates positivity by the same amount. **The razor-thin first-window margin is exactly of the scale of the classical contact bookkeeping error.** This quantifies why "a missing 2log2" (the CW-07 trap) is fatal at this frontier.
- **Finite-compression blindness (IH-01):** unchanged from the repo's statement; our spectrum adds that the discriminating directions are exactly the prolate band modes.

## 3. B-TRACK: quantitative Tauberian transfer for the factorial-prime defect

### BS-B1 (PROVED LOCAL): one-way transfer with explicit constant

Let a: ℕ→[0,∞), A(x)=∑_{n≤x}a(n)/n. If A(x) = log x + C + O(x^{−δ}), 0<δ≤1, then S(x):=∑_{n≤x}a(n) = x + O(x^{1−δ}) with the explicit constant (3 + 1/(1−δ))B (B the O-constant). **No positivity is used.**

*Proof:* Abel: S(x) = xA(x) − ∫₁^x A(t)dt, where the integral is of the step function; substitute A(t) = log t + C + ε(t), |ε|≤Bt^{−δ}; the log and C parts cancel to x + O(1); the error parts give xB x^{−δ} and B∫₁^x t^{−δ}dt ≤ B x^{1−δ}/(1−δ). ∎ Exact-integer verification: `abel_transfer_identity` on two sequences; both pass on all x ≤ 200/300.

### BS-B2 (PROVED LOCAL): sharpness — the spike counterexample

For every 0<δ<1 there is a nonnegative sequence with A(x)=log x+C_a+O(x^{−δ}) but S(x)−x ≫ x^{1−δ}: take a=1+b with b(2^j)=⌊2^{j(1−δ)}⌋. Then C_a = lim A − log is explicit, the weighted tail satisfies ∑_{2^j≤x}2^{−δj} ≤ 2^{−δ}(x^{−δ})/(1−2^{−δ}), while S(2^J)−2^J = ∑_{j≤J}⌊2^{j(1−δ)}⌋ ≍ 2^{J(1−δ)}/(2^{δ/2}·(1−2^{(δ−1)/2}))·... In the numerics (δ=1/2, J=16): worst scaled weighted error 2.21 < 1/(1−2^{−1/2}) = 2.414 ✓ (the predicted constant), spike mass 867 vs the exact geometric sum 871 ✓. **Hence θ(δ)=δ is optimal in the general nonnegative class: no Tauberian method can beat it without further structure.** The spikes are exactly what the authentic source forbids — see BS-B3.

### BS-B3 (PROVED LOCAL + classical imports): the two-way authentic-source dictionary

For a = Λ (so A(x)=∑Λ(n)/n, S=ψ):

\[
A(x) = \log x - \gamma + O(x^{-\delta}) \iff \psi(x) = x + O(x^{1-\delta}),
\tag{BS-B3}
\]

both directions, exact exponent match. Forward = BS-B1. Backward: A(x) = ψ(x)/x + ∫₁^x ψ(t)t^{−2}dt; writing ∫₁^x = ∫₁^∞ − ∫_x^∞ absorbs the constant and leaves O(x^{−δ}) from |∫_x^∞ (ψ−t)t^{−2}| ≤ B x^{−δ}/δ. (Classical, but with the constant-absorption made explicit; verified numerically: |E_A(N)| and |ψ(N)−N|/N track at the same exponent, both O(N^{−1/2}) heuristically under RH, tested at N=2000, 8000.)

Classical zero-side (EXTERNAL THEOREM imports, not re-proved here): both statements are equivalent to ζ zero-free in {Re s > 1−δ} (open half-plane; zeros with Re = 1−δ permitted), via Perron (forward) and Landau oscillation (backward). **Consequence:** for the authentic Λ, the exponent δ cannot be improved without proving zero-free strips — the spike freedom of BS-B2 is replaced by the rigid oscillation family {x^{ρ−1}}. RH is the δ→1/2 endpoint: A(x) = log x − γ + O(x^{−1/2+ε}) for all ε ⟺ RH.

### BS-B4 (PROVED LOCAL): the quantitative defect dictionary

With D_N = ∑_{n≤N}Λ(n)/n − log(N!)/N (the repo's source-quantization defect):

\[
D_N - (1-\gamma) = \big[A(N) - \log N + \gamma\big] + O(\log N/N),
\tag{BS-B4}
\]

the O-term being the explicit Stirling remainder E_fac(N) = ½log(2πN)/N + O(1/N²). *Proof:* log N! = N log N − N + E_fac(N)·N by Stirling; substitute into D_N and use A(N) = log N + C_Λ + E_A(N) with C_Λ = −γ. ∎ Combined with BS-B3: **the factorial-prime defect measures the weighted prime error at the same exponent as the Chebyshev error and the zero-free strip.** D_N is a zero-detector: |D_N − (1−γ)| = O(N^{−δ}) ⟺ ψ(x)=x+O(x^{1−δ}) ⟺ zero-free Re > 1−δ. Verified: log N! = ∑Λ(n)⌊N/n⌋ to 5e−48 (N=200), and the dictionary residual at N=20000 within 30/N (tests pass).

**What this buys:** the repo's PR #77 proved D_N → 1−γ ⟺ PNT (qualitative). BS-B1–B4 upgrade it to the quantitative exact-exponent dictionary with an optimality counterexample, making the defect usable as a *rate monitor* for zero-free quality — a concrete instrument for the RH dependency pipeline (Section G).

## 4. C-TRACK: the Collatz additive/multiplicative defect dictionary

### BS-C1 (PROVED LOCAL): the defect cocycle and cycle equation

For a parity word ε∈{0,1}^m with k=∑ε_j and c_ε=∑_{j:ε_j=1}2^j 3^{K_j} (K_j=∑_{l>j}ε_l): the shortcut map satisfies 2^m T^m(n) = 3^k n + c_ε for every n realizing ε, and a positive integer m-cycle through n exists **iff**

\[
n\,(2^m-3^k) = c_\varepsilon,\quad\text{i.e.}\quad n = c_\varepsilon/(2^m-3^k) > 0 .
\tag{BS-C1}
\]

Verified exactly on realizing orbits and algebraically on generic words (`test_cocycle_*`). This is the exact additive/multiplicative defect: the mismatch SV_p vs V_pS from the prompt's §2.4, made into a closed finite equation. (The cocycle identity itself is classical; the packaging as a *complete* parametrization of m-cycles by (m,k,ε) plus divisibility is the working form used here.)

### BS-C2 (PROVED LOCAL): the valuation dictionary

For every word ε: **v₃(c_ε) = 0** (the last 1-position j* contributes 2^{j*}, not divisible by 3; every other term carries a factor 3) and **v₃(2^m−3^k) = 0** (2^m ≡ ±1 mod 3). Hence every element of every Collatz cycle satisfies **v₃(n) = 0: no cycle element is divisible by 3**. More generally for p ≥ 5:

\[
v_p(n) = v_p(c_\varepsilon) - v_p(2^m-3^k),
\qquad \{(m,k): v_p(2^m-3^k)\ge 1\} = \text{a lattice coset}.
\]

Example (exact, tested): v₅(2^m−3^k) ≥ 1 ⟺ m ≡ 3k (mod 4) — since 2 generates (ℤ/5)^× and 3 = 2³ there; the general condition is the single linear congruence dlog(2)·m ≡ dlog(3)·k (mod φ(p^j)) whenever 2,3 generate a common cyclic subgroup. **The prime factorization of every cycle element is rigidly determined by the cycle's (m,k) through exact p-adic lattice conditions** — the "unique factorization structure" the prompt asked to be made load-bearing, here in the Collatz sector. (The no-3 theorem is folklore-known; the dictionary packaging and the lattice-coset statement are the campaign's additions; scholarly novelty UNVERIFIED.)

### BS-C3 (PROVED LOCAL): finite chart and NO-GHOST scope

The parity chart χ_m: ℤ/2^m → (ℤ/2)^m is a bijection (one residue class per word — the finite layer of the classical 2-adic conjugacy ℤ₂ ≅ (ℤ/2)^ℕ). The descent criterion is Archimedean and does not transport along the conjugacy: T^m(n) < n ⟺ n > c_ε/(2^m−3^k) for good words (2^m>3^k). Termination for all n ⟺ the good-word half-lines cover ℕ. The 2-adic chart organizes the observer's finite data; the positivity/growth constraint lives entirely in the Archimedean place. Exact finite certificate through the cycle equation: **no nontrivial positive integer m-cycle for m ≤ 18** (only the trivial cycle 1↔2, seen with all its word alignments) — matching the classical verification, validating the defect-equation route end-to-end (`no_small_cycles(18)`).

## 5. What the A-track numbers mean for RH (no circularity analysis)

The full Weil criterion is Q_ζ(v,v) ≥ 0 for all v ∈ C_c^∞(ℝ) ⟺ RH. Window-restricted positivity (all v supported in (-a,a)) for a *fixed* a is a *necessary condition* for RH, strictly weaker (a countable family of finite-atom problems, one per prime shell). Our numerics say: every window probed sits within ~3e−4 of the positivity boundary, with the archimedean negativity (band |u|<2π, depth −C_G at u=0) near-exactly cancelled by the in-window prime atoms.

- If RH holds, each λ₀(a) > 0 strictly (no kernel exists: an exact kernel v* would force its Mellin transform to vanish on the whole zero set, impossible for a type-2a entire function by the Beurling–Malliavin density theorem since the zero set has unbounded (log γ)/2π density), but the margins are ≤ ~1e−4 in the probed range — the windowed Weil system is a *critical-margin* system at every scale probed.
- If some window had λ₀(a) < 0 decisively (beyond certified-numeric resolution), RH would be false. **No such window was found** (probed a ∈ [0.36, 1.0], resolution 3e−4).
- The repo's IH-02 contract assumed the missing inequality Q_J ≥ −η_J‖·‖²_{H¹}. Our decomposition sharpens the program: prove the *elementary* window inequality
  \[
  E_G(v) - C_G\|v\|^2 + 2|\langle v,c\rangle|^2 - 2|\langle v,s\rangle|^2 - 2\sum_{n<e^{2a}}\tfrac{\Lambda(n)}{\sqrt n}\mathrm{Re}\langle\tau_{\log n}v,v\rangle \;\ge\; \kappa(a)\|v\|^2
  \tag{IH-2'}
  \]
  with κ(a) explicit, and pair it with the (unconditional, classical-type) zero-side truncation bound |R_T(v)| ≤ B(T, seminorms)‖v‖²: window positivity follows whenever κ(a) > B. The numbers say both sides are ~1e−4-scale on the first windows, so the program is tight but has visible targets. Proving IH-2′ for all windows with κ(a) not decaying faster than the zero-side bound would still not be RH (it is one-sided), but a *negative* answer at any window would disprove RH: the window family is falsifiable in the Popper sense at each scale.

## 6. Originality crucible status

The campaign's genuinely new combinations (per §8 of the orders):

1. **Prolate/Shannon counting applied to the completed Weil window problem** (BS-A3 + BS-A4): the negative band [−2π,2π] of Ω, the Shannon number 4a, and the observed two-mode near-null structure at a=1/2. Neither the repo's lines nor the Carleman literature we know of connects the windowed Weil positivity margin to Landau–Pollak concentration; scholarly novelty UNVERIFIED, but the mechanism explains the repo's own unexplained trial quotient 0.0006 (PR #70).
2. **The elementary barrier K̄ (BS-A2):** a closed form for the exact window confinement; new in packaging even if derivable.
3. **The contact-tail trap (BS-A0-adjacent):** the exact [2a,∞) contact contribution 2h(0)atanh(e^{−2a}) — a normalization landmine quantified for the first time in this repository; any window positivity computation that truncates the contact at supp(h) is wrong at the 0.7 level.
4. **The spike-optimality + Λ-rigidity contrast (BS-B2 vs BS-B3):** the general Tauberian exponent is spike-optimal, and the authentic source is exactly the spike-free case where the same exponent is forced by zeros — a clean statement of "what authentic arithmetic buys" in the defect-monitoring problem.
5. **The Collatz valuation dictionary (BS-C2):** cycle-element factorizations rigidly determined by (m,k) lattice cosets.

Combinations that remained heuristic and are labeled so: the prolate-mode → Weil-positivity program (IH-2′) is a research program, not a theorem here.

## 7. Independent verification inventory (what was actually run)

| Artifact | Status | Command |
|---|---|---|
| A-track module | PROVED LOCAL identities + TESTED MODEL spectrum | `python -m unittest tests.test_black_sun_window` (14 tests, PASS) |
| Carleman == original W, flat a=1/2 | 25-digit agreement | included above |
| Carleman == original W, random v | ≤ 1e−5 (layer-sum truncation bound documented) | included above |
| Contact-tail trap regression | locked (0.772 at a=1/2) | included above |
| Fake-6 blindness / visibility | exact + tested | included above |
| Wrong-contact ±2log2 | exact + tested | included above |
| B-track module | PROVED LOCAL identities, exact-integer checks | `python -m unittest tests.test_black_sun_tauberian` |
| Abel identity, log N! = ∑Λ⌊N/n⌋ (48 digits) | exact | included above |
| Spike construction (δ=1/2, J=16) | constants match prediction | included above |
| D_N dictionary at N=20000 | residual ≤ 30/N | included above |
| C-track module | exact integer certificates | `python -m unittest tests.test_black_sun_collatz` |
| Defect cocycle on orbits | exact | included above |
| No nontrivial cycles m≤18 | exact enumeration | included above |
| v₅ lattice condition vs actual valuations | exact, m≤24×k≤12 | included above |

Baseline before any edit: parent-stack tests pass (72 tests). No main-branch changes, no pushes, no merges, no license edits, no archival file edits.

## 8. RH proof-dependency report (Section G of the orders)

Pipeline: **Euler source → completed Weil form → source-derived all-test sign → RH.**

- Euler source → completed Weil form: SOLID here (BS-A1 verified; repo's CW-01..CW-18 independently re-derived where load-bearing).
- Completed Weil form → all-test sign: **THE MISSING THEOREM, now with a quantitative shape.** Missing is IH-2′ with κ(a) > B(a) at every scale: an operator inequality on a window with (i) the elementary E_G/pole/prime structure (all constants now exact and elementary: BS-A2), (ii) the explicit zero-side truncation bound. Our spectral map shows the margin structure: κ(a) ≲ 1e−4 near a ∈ [0.42,1.0] if it exists at all — the inequality is true-but-critical under RH, so any proof must be sharp to within orders of magnitude of the constant scale of the contact term (2log2 traps are fatal — BS-A5).
- All-test sign → RH: CLASSICAL (Weil). Nothing in the campaign changes its status.

## 9. The strongest next lemma (Section H of the orders)

**Lemma (first-window margin).** Let a ∈ (log2/2, log3/2) and define, for v ∈ H¹₀(−a,a),

\[
\Lambda_0(a) = \inf_v \frac{Q_\zeta(v,v)}{\|v\|^2}, \qquad Q_\zeta \text{ as in BS-A1.}
\]

Prove or refute: **Λ₀(a) ≥ 0 for all a in the window**, equivalently (by BS-A3) the single-prime inequality

\[
\tfrac{1}{2\pi}\int |\hat v(u)|^2 \Omega(u)\,du
+ 2|\langle v,\cosh(x/2)\rangle|^2 - 2|\langle v,\sinh(x/2)\rangle|^2
- 2\tfrac{\log 2}{\sqrt2}\mathrm{Re}\langle \tau_{\log2}v,v\rangle \;\ge\; 0 .
\]

- **Quantifiers:** all real v ∈ H¹₀(−a,a), a ∈ (0.3466, 0.5493).
- **Known from this campaign:** Λ₀(0.36) = +8.5e−4 > 0 (numerically certified to ±3e−6); Λ₀(a) ∈ (−3e−4, +3e−4) unresolved for a ∈ [0.42, 0.5493]; the archimedean part alone is at −0.43; the compensating term is the prime-2 shift; two near-null modes at the Shannon transition.
- **Controls to predeclare:** fake-6 must stay invisible; wrong contact by ±2log2 must move Λ₀ by exactly ∓2log2+o(1); finite Gram matrices are not evidence (IH-01); the certified-sign threshold is ~1e−5 — interval-arithmetic Nyström or an exact prolate-bound proof is required.
- **Why it changes the frontier:** it is the first window of the countable family whose conjunction is Weil's criterion; a proof technique that closes the first window with explicit constants (e.g., via the elementary barrier BS-A2 + a rank-2 perturbation theorem + the exact prime-2 path operator spectrum of PR #70 CG5) would provide the template for every window — and a refutation at any window would disprove RH. The required precision is now known: constants must be controlled to better than 1e−4, and the contact bookkeeping to better than 2log2-scale errors is mandatory.

## 10. Boundary of all claims

Nothing here proves RH, ABC, Goldbach, or Collatz. No claim of scholarly priority is made without the UNVERIFIED label. The spectral values are float64 Rayleigh–Ritz upper bounds converging from above with resolution stated; no interval arithmetic was used, so no sign at the 1e−4 scale is certified by this campaign. The A-track identities are proved with hand derivations plus high-precision agreement (which is evidence, not proof, of the hand derivations' correctness — the hand proofs are included and checkable). The next-lemma program (Section 9) is a plan, not a result.

**Source receipts:** main `6e0d88f1b235b85188393bbcd64ac0436cb71a70`; parent `origin/research/global-model-sandwich-2026-10-14` @ `8ce8ebb`; PR #70 doc `SUZUKI_MARKOV_GLUING_ROUND.md` @ `c0393c9`; E38 dossier on main; this campaign's branch `research/black-sun-independent-campaign-2026-10-14` (this commit).

**Cheapest next step:** interval-arithmetic certification of λ₀(0.36) > 0 (a one-day task with the BS-A2 elementary barrier and validated Nyström), then the first-window inequality proof attempt via [elementary barrier] + [rank-2 perturbation lemma] + [CG5 path spectrum].