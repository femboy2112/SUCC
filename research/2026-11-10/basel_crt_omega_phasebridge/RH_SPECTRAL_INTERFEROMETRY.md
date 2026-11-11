# RH => pi normal? A source-locked Mellin boundary test and two no-go controls

**SUCC research note, 2026-11-10.** Companion to draft PR #585's `SIGNED_BASEL_TAUBERIAN.md`, stacked on Main XXIII #584. This is an **exploratory conditional reduction and adversarial test**, not a proof that RH implies base-16 normality of pi. RH and normality remain OPEN. No original BBP source, literal zero seed, provenance contracts, archives, or historical results are altered.

## 1. Three distinct pieces of data

The Basel value `zeta(2)=pi^2/6` fixes the real scalar `pi=sqrt(6 zeta(2))` (positive root). The Riemann hypothesis concerns the zero locations of the analytically continued *ordinary* `zeta(z)`. Hexadecimal normality concerns the distribution of the *radix orbit* `16^n pi (mod 1)`. An identity involving all three does **not** imply that the second controls the third.

Fix an integer Fourier mode `h != 0`, a real BBP seed `u`, and the authenticated completed phase `Y_n(u)=16^n(u+pi/16)` (`n>=1`). Put

```math
a_n(h;u)=\exp(2\pi i hY_n(u)),\quad
\mathcal D_h(z;u)=\sum_{n\ge1}\frac{a_n(h;u)}{n^z},\quad\Re z>1.
```

The zero-seed identity is

```math
\mathcal D_h(z;0)=\sum_{n\ge1}\frac{\exp(2\pi i h16^{n-1}\sqrt{6\zeta(2)})}{n^z}.
```

The series is absolutely convergent on `Re z>1`. It generally has **no Euler product**: `n -> a_n` is not a multiplicative arithmetic function. Therefore ordinary RH estimates are not automatically estimates for `D_h`. At `h=0`, `D_0=zeta`; for the coherent wrong seed `u_*=-pi/16`, `D_h(z;u_*)=zeta(z)` for **every** nonzero `h`, while every digit of the completed orbit is zero. This is a precise source-blind no-go control: RH, even if true, cannot be applied identically to all seeds to infer digit balance.

The preceding companion proves, for **each** nonzero integer `h` and the literal zero seed, `A F_h(A;0)->0` if and only if the corresponding Weyl epoch means vanish; all modes yield base-16 normality. This is a repackaging of Weyl/Abel, not a proof that the limit vanishes.

## 2. A genuine sufficient Dirichlet boundary gate (classical Kronecker lemma)

**Theorem (sufficient, not necessary).** If the ordinary series `D_h(1;0)=sum a_n(h;0)/n` converges for every fixed nonzero integer `h`, then pi is normal to base 16.

**Proof.** Write `u_n=a_n/n`, `U_N=sum_(n<=N)u_n` and suppose `U_N->U`. Discrete summation by parts gives

```math
\frac1N\sum_{n=1}^Na_n
=U_N-\frac1N\sum_{n=1}^{N-1}U_n\longrightarrow U-U=0.
```

This is Kronecker's lemma for complex sequences. Weyl's criterion then gives normality. **Warning:** convergence of `D_h(1;0)` is stronger than the required `A F_h(A;0)->0`; it is not necessary. For example, the bounded *abstract* coefficients `a_n=1/log(n+1)` have `N^{-1}sum_(n<=N)a_n->0`, while `sum a_n/n` diverges. Neither abstract control is the authentic pi phase.

**A second sufficient analytic gate.** Suppose for each relevant `h`, `D_h(z;0)` admits a holomorphic continuation to `Re z>1-delta_h` for some `delta_h>0`, with at most polynomial vertical growth on closed substrips. Then `N^{-1}sum_(n<=N)a_n(h;0)->0`. Indeed for any `f in C_c^infty(0,infty)`, Mellin inversion and a contour shift from `Re z>1` to `Re z=1-delta_h/2` give `sum a_n f(n/N)=O_f(N^(1-delta_h/2))`. Choose `0<=f<=1`, `f=1` on `[epsilon,1]`, `supp f subset [epsilon/2,1+epsilon]`. Boundedness `|a_n|<=1` pays at most `O(epsilon N)` to compare with the sharp prefix. First send `N->infty`, then `epsilon->0`. This is a **conditional sufficient theorem**, not a known continuation or estimate for the pi-selected twisted series; standard zeta RH supplies neither premise.

## 3. Exact radix-16 transport of Dirichlet singularities

For any real seed, `a_(n+1)(h;u)=a_n(16h;u)`. Consequently, initially for `Re z>1`,

```math
\boxed{\mathcal D_{16h}(z;u)-\mathcal D_h(z;u)
=-a_1(h;u)+\sum_{n=2}^{\infty}a_n(h;u)
\big((n-1)^{-z}-n^{-z}\big).}
```

The difference series converges **locally uniformly for `Re z>0`**, since the bracket is `O_z(n^{-Re z-1})`. Therefore the difference has a holomorphic extension to `Re z>0` without any RH assumption. Whenever the individual `D_h` profiles have meromorphic continuations, all modes in the same chain `h,16h,16^2h,...` have identical singular principal parts on `Re z>=1`. This reduces an analytic gate to frequency representatives **not divisible by 16**, without claiming cancellation for those representatives.

## 4. Crucible: a regular real point conceals vertical boundary obstructions

The abstract bounded sequence `b_n=(-1)^{floor(log_2 n)}` is constant on each dyadic shell `[2^k,2^(k+1))`. Thus, for `A=2^k`, `A^{-1}sum_(n=A)^(2A-1)b_n=(-1)^k`: no cancellation.

Define the step function `b(x)=(-1)^{floor(log_2 x)}` for real `x>=1`. Its **exact** Mellin transform is, for `Re z>1`,

```math
M(z)=\int_1^\infty b(x)x^{-z}dx
=\frac{2^{1-z}-1}{(1-z)(1+2^{1-z})}.
```

The apparent singularity at `z=1` is removable and `M(1)=log(2)/2` by analytic continuation. But the denominator vanishes at every

```math
z_m=1+\frac{(2m+1)\pi i}{\log2},\qquad m\in\mathbb Z,
```

and the numerator does not; these are genuine nonreal poles **on `Re z=1`**. The discrete Dirichlet series `sum_(n>=1)b_n n^{-z}` differs from `M(z)` by `sum_(n>=1)b_n[n^{-z}-int_n^(n+1)x^{-z}dx]`, a locally uniformly convergent holomorphic series on `Re z>0`. It therefore inherits these nonreal boundary poles although it is regular at the real point `z=1`.

**Verdict:** a recipe that checks only a real residue at `z=1`, or uses only the scalar Basel value, cannot certify the signed Weyl means. A meaningful analytic proof must control sufficient vertical boundary information. This counterexample does **not** refute any *specific* source-locked pi theorem, and it does not imply RH is independent of pi normality.

## 5. The actual RH-to-pi seam

The ordinary RH is equivalent (with an explicitly admissible test-function class and **completed** prime-power plus Gamma/pole source) to the nonnegativity of Weil's completed quadratic form. To prove the extraordinary implication `RH => pi base-16 normality`, one needs an additional *source-selected theorem* transporting the selected BBP phase into a bound that follows from this completed positivity. Neither `zeta(2)=pi^2/6` nor nonnegative Gibbs/Weil quadratic forms produce such transport by themselves.

One **falsifiable conditional architecture** is: construct admissible test functions `g_(A,h)` from the original four BBP poles, literal `U0=0`, full real carries and CRT complement, and prove, with `c_h>0` and `epsilon_A->0`,

```math
\mathcal W_\zeta(g_{A,h}*\widetilde{g}_{A,h})
\le \epsilon_A-c_h|A F_h(A;0)|^2.
```

Then RH would yield `A F_h(A;0)->0`. **No such construction or inequality has been obtained.** The burden is particularly severe: the same formula must fail or change with the coherent zero-orbit seed and the p-integral PPP-08 control; otherwise it would contradict those exact countermodels. Specifying this gate does not promote it from UNVERIFIED to a plausible theorem.

A separate published precedent for *zeta-to-digit criteria*, **not** for RH implying normality of pi, is Kanado–Saito (2025), *A criterion for the simple normality of fractional powers of two via the Riemann zeta function*, Canadian Journal of Mathematics, DOI 10.4153/S0008414X25101077. It relates binary simple normality of selected fractional powers of two to zeta values on vertical arithmetic progressions. Its scope is distinct from the authentic BBP source.

## Claim ledger and next discriminator

- **DISCLOSED (elementary classical proof):** Dirichlet harmonic convergence suffices; frequency-shift difference is holomorphic on `Re z>0`; Mellin dyadic-block counterexample has nonreal `Re z=1` poles; holomorphic-strip-with-growth gate suffices.
- **OBSERVED finite:** companion `test_rh_spectral_gate.py` uses only standard-library arithmetic to verify eight algebraic/finite controls. Same-researcher verification is not independent refereeing.
- **UNVERIFIED:** source-selected vertical boundary control for `D_h`, a valid Weil-form transport with a negative residual, and any implication from ordinary RH to the needed estimates.
- **OPEN:** original-zero `A F_h(A)->0`, pi base-16 normality, RH.

**Next verdict-changing probe:** derive an explicit prime-power and completed-Gamma pairing for `D_h(z;0)` which can distinguish original zero from PPP-08. First test it on `a_n=1`, rational periodic radix orbits, and dyadic log blocks. Refuse any source-blind or real-s=1-only inference, any missing Archimedean source, or any alleged test of actual asymptotic normality from a finite sample.

**Provenance:** SUCC #584/#585 and `docs/PI_NORMALITY_FRONTIER.md`; classical Weyl, Abel, Kronecker, Mellin inversion and Weil positivity; Bombieri, *The Riemann Hypothesis* (Clay Mathematics Institute, https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf); Kanado–Saito DOI above. This paper-note does not claim scholarly priority or computational certification of an infinite theorem.