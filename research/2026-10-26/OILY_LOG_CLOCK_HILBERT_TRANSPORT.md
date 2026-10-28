# Operation Oily Macaroni II — certified source-to-selected-Weyl log-clock Hilbert transport

**2026-10-26, staged on Oily Macaroni draft PR #307.** Same source baseline Main XI `6dd80730c3575d91f746546a25da5aedbd2e2737`. This theorem strengthens the companion `OILY_MACARONI_SOURCE_MELLIN_HILBERT.md`: the exact positive Hilbert overlap is now tied to the **unweighted authentic Weyl sum** by a source-derived, frequency-uniform, quantitatively vanishing transport error. **π base-16 normality remains OPEN**: no weighted signed sum is proved small.

## 1. Construction and source type

Let `a_n=8n-7`, `Q(x)=4-2e^-3x-e^-4x-e^-5x>0`, and `R(a)=int_0^infty e^-a x Q(x)dx` so that `R(a_n)=r(n)` is precisely the original signed four-pole forcing. Define unit vectors on the **one common** Hilbert carrier `L²((0,infty),dx)`:

$$
 f_a(x)=\frac{e^{-a x/2}\sqrt{Q(x)}}{\sqrt{R(a)}}
 \quad\Rightarrow\quad
 \|f_a\|_2=1.
$$

Their exact overlap (positive, symmetric, PSD kernel) is

$$
H(a,b)=\langle f_a,f_b\rangle
=\frac{R((a+b)/2)}{\sqrt{R(a)R(b)}}.
$$

Its **square** is an exact rational number whenever `a,b` are the original integer clock values. This is the same source for both viewpoints: BBP's Laplace endpoint weights and the selected arithmetic phases `z_n=e^{2 pi i h U_n}`. It is not an external random phase ensemble.

## 2. Finite source Fisher geometry and certified logarithmic overlap bound

Let `mu_a(dx)=f_a(x)^2 dx`, a source-conditioned exponential family. Its derivative in Hilbert space obeys the exact identity

$$
\partial_a f_a(x)=-\frac12 (x-\mathbb E_{\mu_a}X)f_a(x),
\qquad
\|\partial_a f_a\|_2^2=\frac14\operatorname{Var}_{\mu_a}(X).
$$

This is a classical Fisher–Rao/Hellinger relationship in a concrete BBP source. Now exploit the **specific authenticated four-pole Q**:

- `Q(0)=0`, `0<Q'(x)=6e^-3x+4e^-4x+5e^-5x<=15`; hence `Q(x)<=15x` for every `x>=0`.
- The Taylor remainder is nonnegative: `Q(x)>=15x-(59/2)x²`, so
  `R(a)>=15/a²-59/a³`.
- Therefore for `a>=16`, `R(a)>= (181/16)/a²`, and

$$
\mathbb E_{\mu_a}(X^2)
 =\frac{\int x^2e^{-a x}Q(x)dx}{R(a)}
 \le\frac{90/a^4}{(181/16)/a^2}
 =\frac{1440}{181 a^2}<\frac8{a^2}.
$$

Consequently `||partial_a f_a||_2<=sqrt(2)/a`. By integrating the Hilbert-valued derivative and using `||f_a-f_b||²=2(1-H(a,b))` we prove for all `a,b>=16`:

$$
\boxed{0\le1-H(a,b)\le [\log(b/a)]^2},
$$

with the square understood as nonnegative regardless of orientation. This is a **uniform all-parameter theorem**, not fitted to finite experiments.

For clock times `m>=3`, `n in [m,m+L-1]`, `a_n/a_m=1+8(n-m)/a_m`. Using `log(1+x)<=x`,

$$
\boxed{1-H(a_n,a_m)\le \left(\frac{8(L-1)}{8m-7}\right)^2.} \tag{LOC-1}
$$

The right side is an *exact rational certificate*.

### Consecutive SUCC steps have the same vanishing error scale as the Green tail

Watson's elementary endpoint expansion `R(a)=15 a^-2-59 a^-3+O(a^-4)` implies

$$
H(a,a+8)=1-\frac{16}{a^2}+O(a^{-3}).
$$

Since the authenticated future Green tail is `T_n~1/a_n²` (from the first dossier), we have the second exact positive-shrinking relation

$$
\boxed{\lim_{n\to\infty}\frac{1-H(a_n,a_{n+1})}{T_n}=16.} \tag{LOC-2}
$$

This is **not** Euler gamma alone generating cancellation: it is a source-specific Hilbert overlap and a positive future-boundary error, both quadratic on the logarithmic time clock.

## 3. A real signed Fourier transport theorem (local blocks)

Let `z_n` be **any** complex sequence with `|z_n|=1`. For the authentic π program select `z_n=exp(2 pi i h U_n)`, keeping the unchanged unwrapped `U_n`.

On `B=[m,m+L-1]`, select the natural Hilbert reference `f_(a_m)`. Then

$$
\bigg|\frac1L\sum_{n\in B} z_n
 -\bigg\langle\frac1L\sum_{n\in B} z_n f_{a_n},f_{a_m}\bigg\rangle\bigg|
=\bigg|\frac1L\sum_{n\in B}z_n[1-H(a_n,a_m)]\bigg|
\le\left(\frac{8(L-1)}{8m-7}\right)^2. \tag{LOC-3}
$$

The equality relies on the *actual signed phases* and genuine source vectors; the bound holds independently of their values. This is a valid native source-to-observer arrow, **not** a positivity-derived saving: it compares one signed quantity to another without establishing either is small.

## 4. An all-N source-authenticated Weyl-to-Hilbert reduction with explicit rate

For `N>=27` let `k=floor(N^(1/3))`, `M=k²`. Discard the first `M-1` phases, charging their exact trivial cost `(M-1)/N`, and partition `M..N` into consecutive blocks of at most `k` times. For each block B, let m(B) be its first time and define

$$
\widetilde A_N(h)=\frac1N\sum_B\sum_{n\in B}
 e(hU_n) H(a_n,a_{m(B)}).
$$

Then **for every nonzero integer h, simultaneously**, and indeed for every unit-modulus sequence,

$$
\boxed{\left|\frac1N\sum_{n=1}^N e(hU_n)-\widetilde A_N(h)\right|
\le\frac{M-1}{N}+\left(\frac{8(k-1)}{8M-7}\right)^2
=O(N^{-1/3}).} \tag{LOC-4}
$$

Both terms on the RHS are **exact rational numbers computed solely from the time horizon** and the source's fixed affine clock. The asymptotic proof uses only `k~N^(1/3)`; it does not assume the wished-for cancellation.

At `N=512`, the rigorous all-frequency source-transport error upper bound is exactly `17672207/130572800 ≈ 0.13534`; it is not yet a useful cancellation upper bound because no control on `tilde A_N` is proved. Tests evaluate finite authentic selected complex sums at h=1,2,3 and verify their discrepancy is below LOC-4, while preserving a separate exact certificate for the bound.

**If** a valid source-specific estimate `tilde A_N(h)=o(1)` is proved for every fixed h, LOC-4 **does** give the authentic Weyl criterion and base-16 π normality through the previously proved Green transfer. This is a conditional theorem, not its hypothesis.

## 5. Explicit frontier and no-go controls

- Source Laplace–Mellin one-time virtual characters `Phi_n(t)` converge to a **nonzero** limiting Gamma(2) characteristic. Averaging those one-time characters does not prove cancellation.
- The Hilbert windows are designed to approximate the actual signed sum with small error, but the signed window contributions may align perfectly; then `tilde A_N(h)` remains order one. LOC-4 is **also valid for fake coherent phases**. This is why the proof's missing part is exactly the arithmetic signed bound on `tilde A_N`.
- A constant `O_mac=lambda-gamma` does not appear as an intrinsic relative phase; the shared Euler first jet cancels under two-time comparison. The golden selection is a possible consistent cross-carrier chart, not forced by the BBP recurrence, and neither its value nor the positive fidelity inequality supplies Fourier decay.
- The new log-clock kernel `H(a,b)` has a macroscopically positive limiting overlap with itself over all times: the phase-free normalized double sum tends to `4 log2-2>0`. Positive fidelity does not become negative signed interference on demand.
- The mutant `Q+epsilon exp(-6x)(1-exp(-x))^3` shares the first two endpoint jets and first-order complex Oily-Macaroni coefficient; this prevents false source authentication by first jets.

**Next explicit goal:** bound the actual **signed** Hilbert window sum `tilde A_N(h)` by proving source-specific cross-block cancellation, or demonstrate that its weighting is too close to identity to add useful estimates. Compare intact BBP and matched fake controls in identical log-clock windows.

## 6. Validation and integration status

- Source module: `observational_succ/oily_macaroni_transfer.py` (`local_hilbert_block_budget`, `multiscale_hilbert_transport_budget`).
- Exact/falsification tests: `tests/test_oily_macaroni_transfer.py`, including source-law identity and numerical complex integral holdouts.
- Isolated local tests: **23/23** passed on a declared minimal shim; full combined-repository CI is separate and should be checked on the latest pushed branch SHA.
- No frozen source archive changes; no new Lean authority or academic priority asserted; π normality, RH and their logical independence remain OPEN.
