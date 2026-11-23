# Source-typed prime/Euler/BBP transfer: theorem statements and proofs

**Conventions.** `e(t)=exp(2πit)`, `Λ` is the genuine von Mangoldt function, and `χ=χ₄` is the real primitive character mod 4: `χ(2n)=0`, `χ(4n+1)=1`, `χ(4n+3)=−1`. All source labels and phases are retained. `X` is a prime-power cutoff **distinct** from the BBP clock `n` and the Weyl-shell length `B`.

## I1. An exact prime-spectral representation of the authentic π endpoint — classical + new-to-SUCC integration

Take the **unaltered** original BBP source

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Define `P_n=Σ_{j=1}^n 16^(−j)r(j)` and `T_n=Σ_{j>=1}16^(−j)r(n+j)`. Classical BBP gives

\[U_n+T_n=16^n x,\qquad x=\sum_{j\ge1}16^{-j}r(j)=\pi/16.\]

Independently, the character Dirichlet series (Leibniz–arctangent) gives

\[L(1,\chi)=\sum_{j\ge0}\frac{(-1)^j}{2j+1}=\frac\pi4,\quad x=\tfrac14L(1,\chi).\]

For each integer `X≥2`, define the **finite, exact rational** prime-power Euler log

\[
 S_\chi(X)=\sum_{p^k\le X}\frac{\chi(p)^k}{k p^k}
 =\sum_{2\le n\le X}\frac{\chi(n)\Lambda(n)}{n\log n},\qquad
 x_X=\frac14\exp(S_\chi(X)).
\]

The second equality follows termwise: if `n=p^k`, then `Λ(n)=log p` and `log n=k log p`; all other terms vanish. For `Re s>1`, the Euler product gives `log L(s,χ)=Σ_{n≥2}χ(n)Λ(n)/(n^s log n)`. The convergence and identification at `s=1` are justified in I3 below using GRH, so `x_X→x` under that assumption. No independent/principal fake-prime clocks are introduced.

## I2. Exact FUCC matrix coefficient (finite, unconditional)

On the finite-support subspace of `ℓ²(N_{>0})`, define `D|n⟩=(log n)|n⟩` and `V_m|n⟩=|mn⟩`. For every integer `X≥2`, the finite operator

\[L_{X,\chi}=\sum_{p^k\le X}\frac{\chi(p)^k}{k}V_{p^k}\]

satisfies

\[[D,L_{X,\chi}]=\sum_{n\le X}\chi(n)\Lambda(n)V_n.\]

This is the `χ₄`-twisted form of #687's FUCC Euler-log commutator. Let the finite row be `⟨b_X|=Σ_{2≤m≤X} (m log m)^(−1)⟨m|`. Then **exactly**

\[\boxed{\ \langle b_X|[D,L_{X,\chi}]|1\rangle=S_\chi(X).\ }\]

The matrix coefficient is real, finite and source-labelled. Note that `D` and `b_X` contain real logarithms; the final scalar is rational because the logarithms cancel **at genuine prime powers**. The identity does not import any theta-kernel integrality, p-adic divisor lower bound, nonzero determinant, or Archimedean slope bound from Alpöge's proof; those would be different statements.

## I3. The genuine Dirichlet-GRH gravity assist (conditional on GRH for χ₄)

Assume `GRH(χ₄)`: every nontrivial zero of `L(s,χ₄)` has real part `1/2`. Classical explicit-formula estimates yield, with absolute/character-dependent `C₀`, for all `t≥3`,

\[A_\chi(t):=\sum_{n\le t}\chi(n)\Lambda(n),\quad |A_\chi(t)|\le C_0\sqrt t\log^2(4t).\]

Partial summation with `f(t)=1/(t log t)` gives the convergent tail:

\[
\log L(1,\chi)-S_\chi(X)
=-A_\chi(X)f(X)-\int_X^\infty A_\chi(t)f'(t)\,dt
=O(X^{-1/2}\log X).
\]

(Here `f'(t)=−(log t+1)/(t²(log t)²)`, and `A(t)f(t)→0` under GRH. The series limit agrees with `log L(1,χ)` by approaching `s=1` from `s>1`.) Since `L(1,χ)=π/4>0`, exponentiation has a bounded Lipschitz multiplier in the tail regime. Thus

\[\boxed{\left|x_X-\frac\pi{16}\right|\le C_1 X^{-1/2}\log X\quad(X\ge X_0).}\]

This is a quantitative **endpoint representation** from actual primes. It is neither a probability law for their `χ`-signs nor a digit normality result. The basic analytic consequence `Aχ=O(√t log²t)` is classical under the stated GRH; SUCC does not independently prove it.

## I4. Uniform late-shell transfer from a finite prime-power observer (conditional on I3)

For integer `B≥1`, integer `h≠0`, and real `y`, let

\[W_B(h;y)=\frac1B\sum_{n=B}^{2B-1}e(h16^n y).\]

The elementary mean-value bound `|e(u)-e(v)|≤2π|u-v|` and I3 give

\[
|W_B(h;x)-W_B(h;x_X)|
\le 2\pi |h|16^{2B-1}C_1 X^{-1/2}\log X
\]

for all sufficiently large `X`. Set the **predeclared** enormous prime cutoff `X_B=16^(4B)B^6`. Then `log X_B=O(B)` and hence

\[\boxed{W_B(h;\pi/16)=W_B(h;x_{X_B})+O_h(B^{-2}).}\]

The complete original BBP orbit has the separate unconditional tail transport `U_n+T_n=16^n x`, with `T_n=O(n^(-2))`. Therefore **both authentic observations recover the same selected real-phase shell within the stated errors**. Their agreement is not evidence of independence: both are functions of the *same* `x`.

As a precise obstruction, suppose I3 and I4 hold but no additional signed estimate does. The displayed error identity is compatible with `W_B(1;x)→1` along a subsequence. Therefore the GRH *endpoint bound alone* cannot be promoted into an anti-locking estimate by taking absolute values, squaring, changing Fourier bases, or replacing the finite sum with a random prime model. To prove R0 via this interface one must derive a genuinely source-specific positive lower bound for `1−Re W_B(1;x_{X_B})` on **every sufficiently late shell**; for normality, all nonzero characters must cancel. Those remain open.

## I5. Prime-clock sparsity and the propagation requirement (classical)

The original prime pole `p=8n−7` is prime for `O(B/log B)` values of `n∈[B,2B)` by the prime number theorem for residue `1 mod 8`; in fact the count is asymptotic to `2B/log B`. Thus its direct proportion in the Weyl mean tends to zero. Any use of those prime slots for an `Ω(B)` shell bound **must** prove an effect of prime events on the *complementary source-clock dynamics*, such as their lasting signed influence on the cofactor/carry/CRT phases. Prime-sign equidistribution at prime slots is not such a theorem.

## I6. Independent π-exponent-two input: what it can and cannot buy

OpenAI's September 2026 manuscript and Lean files claim the exact irrationality exponent `μ(π)=2`. The proof uses high-dimensional interpolation jets, nonzero determinants, and competing arithmetic/analytic bounds, superficially akin to the multiplicity-versus-size architecture of Alpöge–Claude, but **it does not derive from RH**. SUCC #686's generalized Kempner number `β=Σ_{j≥0}16^(−2^j)` has imported known `μ(β)=2` while its late-shell anti-locking statistic tends to zero. So neither GRH's prime marginal saving nor `μ=2` gives normality. Imported `μ(π)=2` does improve SUCC #686's periodic-shadow inequality conditionally: a length-`L` periodic mimic of period `p` after `n` digits obeys `L≤(1+ε)n+(2+ε)p+1` eventually. That bound is not an R0 inequality.

## I7. Exact rank-one prime-to-phase Jacobian (new obstruction, unconditional finite algebra)

At any fixed finite cutoff `X`, label each genuine prime power `a=(p,k)` with
`p^k≤X`. Introduce independent real *probe parameters* `θ_a` by replacing
`Sχ(X)` with `S_X(θ)=Σ_a θ_a c_a` where `c_a=χ(p)^k/(k p^k)` and
`x_X(θ)=exp(S_X(θ))/4`. These parameters define a **hypothetical perturbation
family**, not independently random actual primes. For all times `n` and modes
`h`, set `z_(n,h)(θ)=e(h16^n x_X(θ))`. The chain rule gives

\[
\frac{\partial z_{n,h}}{\partial\theta_a}
=\underbrace{2\pi i h16^n x_X(\theta)z_{n,h}(\theta)}_{v_{n,h}}
\underbrace{\frac{\chi(p)^k}{k p^k}}_{c_a}.
\]

Therefore the entire finite-time/finite-mode Jacobian is the outer product
`J=v cᵀ`, hence `rank_C J≤1` (rank one if an odd prime-power column and a
nonzero mode are included). **All its 2×2 minors vanish identically.**

This is not a claim that the arithmetic prime process intrinsically has rank
one; it proves that **once its contributions have been compressed into the
single endpoint `x_X`, no observer reading only that endpoint's radix orbit
can reconstruct independent prime-perturbation directions from first-order
phase measurements.** Recovering prime dynamical effects needs an additional
observable (the original BBP integer carry/cofactor journal, or a source-native
arithmetic lattice), not another change of endpoint Fourier basis. The
identity holds for any fixed `X`, without RH, and on locked and nonnormal
perturbation endpoints too. It is an instrument/no-go theorem, not R0.

## What could falsify or advance this bridge?

- **Finite arithmetic mutations:** replace `χ₄` by the principal sign, insert composite `6` into Λ, drop the `1/k`, replace `U₀=0` with a rational or cancelling seed; the normalized source coefficient fails in the predicted places.
- **Asymptotic logic mutation:** remove Dirichlet-GRH and pretend the `X^-1/2` saving follows; invalid. Even granting GRH, replace the signed shell lower bound by a bound on endpoint error; this does not distinguish the generalized Kempner R0 countermodel.
- **Verdict-changing new theorem:** build an integral source-conditioned theta/FUCC lattice, with a nonzero rank certificate, a local divisibility gain and a *same-object* global size bound, **from which one can prove a non-tautological signed estimate for the χ₄ prime-product phase shell**. Its controls must include the real BBP zero-seed, carry aliases, and Kempner/periodic locking. Without this new arithmetic-to-temporal inequality, do not claim a π normality proof.
