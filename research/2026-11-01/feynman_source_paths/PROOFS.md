# OPERATION FEYNMAN — rigorous original-source BBP phase-space paths

**2026-11-01 · research-only paper derivations.** This is a source-specific mathematical model, not a demonstration that arithmetic itself is quantum. The real physical value of Planck's constant, real laboratory dynamics, infinity-dimensional physical path measures, π base-16 normality and RH are **NOT proved**. Historical original four-pole source, selected `U_0=0`, production, formal contracts and workflows are untouched. Parent is SUCC PR #443, pinned at `00ba302898a8c81d3dbea0f4dd29f541a0f3d158`.

## 0. Source contract, finite action and quantization choice

The immutable arithmetic source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\tag{F0}
\]

All `r(n)` and `U_n` are *exact rationals*. The first two source terms are `r(1)=47/15`, `r(2)=106/819`, and the actual source-order commutator is `15(r(1)-r(2))=12301/273`. The selected completed boundary is `alpha=sum_{n>=1}16^-n r(n)=π/16`. The altered completed point `q=1/5` is a coherent **NONSELECTED** orbit of the same forcing.

Parent PR #443 already proved that the per-step classical Hamiltonian

\[
 H_n(x,p)=\lambda p(x+c_n),\qquad \lambda=\log16,\quad c_n=r(n)/15,
\]

has time-one map `F_n:(x,p)->(16x+r(n),p/16)`. Introduce `\hbar_*>0` as an arbitrary **chosen action/Fourier scale**; it is not identified with the physical Planck constant. The symmetric/Weyl quantization on `S(R)` is

\[
 \widehat H_n=-i\hbar_*\lambda\big((x+c_n)\partial_x+\tfrac12\big).
\tag{F1}
\]

The essential `1/2` is the half-density divergence correction. A formal operator `-i ħ λ (x+c)∂_x` without it is not unitary on Lebesgue `L²`. The source value `r(n)` is real (indeed rational) and depends on discrete **time index**, not position, so the declared affine flow is exact.

## F-01 — source-specific strongly continuous unitary group (CLASSICAL + original source)

For every `t in R` and fixed n define

\[
 (W_n(t)\psi)(y)=16^{-t/2}\psi\!\left(16^{-t}(y+c_n)-c_n\right).
\tag{F2}
\]

A variable substitution shows exactly `||W_n(t)ψ||_2=||ψ||_2`. Also `W_n(t)W_n(s)=W_n(t+s)`, and `t->W_n(t)ψ` is strongly continuous on `L²`, initially on compactly supported smooth functions and then by density. Differentiation on `C_c^∞` gives `dW_n(t)/dt|_0 = -i\widehat H_n/\hbar_*`. Stone's theorem associates a selfadjoint generator with this explicit unitary group; the displayed differential expression identifies its action on the indicated test core, without an unsupported claim about every other unbounded-operator domain.

At `t=1`, `W_n=W_n(1)` satisfies

\[
 (W_n\psi)(y)=\frac14\psi((y-r(n))/16).
\tag{F3}
\]

The ordered product (not a commuting surrogate) is

\[
 (W_N\cdots W_1\psi)(y)=16^{-N/2}\psi((y-U_N)/16^N),
\tag{F4}
\]

because the affine source matrices multiply to `(16^N,U_N)` with the genuine exact zero-seeded recurrence. This is a unitary representation of the source-ordered affine composition, not a stochastic path selection.

Let `Xψ(y)=yψ(y)`, `P=-i ħ_*∂_y`. Their conjugation obeys, on Schwartz functions,

\[
 W_n^{-1}XW_n=16X+r(n),\qquad W_n^{-1}PW_n=P/16.
\tag{F5}
\]

Thus the quantization is symplectically compatible with parent PR #441 and reproduces original BBP phase-space updates exactly. It does not assert a physical realization of `W_n`.

## F-02 — finite Feynman integral, rigorously a tempered distribution

At one time step, the Schwartz kernel of `W_n` is

\[
 K_n(y,x)=4\,\delta(y-16x-r(n)).
\]

Indeed `int 4 delta(y-16x-b)ψ(x)dx=(1/4)ψ((y-b)/16)`. Compose these kernels by integrating over `x_1,...,x_(N-1)`. The result is

\[
 K_N(y,x)=16^{N/2}\delta(y-16^Nx-U_N).
\tag{F6}
\]

Use the distributional Fourier identity `delta(z)=(2π ħ_*)^-1 int_R exp(i p z/ħ_*) dp`. On Schwartz test functions the **time-sliced phase-space oscillatory integral** becomes

\[
\boxed{K_N(x_N,x_0)=\frac{16^{N/2}}{(2\pi\hbar_*)^N}
\int_{\mathbb R^{2N-1}}\exp\!\left[\frac i{\hbar_*}\sum_{j=1}^Np_j\big(x_j-16x_{j-1}-r(j)\big)\right]
\,d^{N-1}x\,d^Np.}\tag{F7}
\]

`x_0,x_N` are fixed external endpoints; the oscillatory integral is **NOT** absolutely convergent and is defined as a tempered distribution by its Fourier action (or compatible Gaussian cutoff and distributional limit). Integrating all `p_j` yields exactly the constraints `x_j=16 x_(j-1)+r(j)`. The unique internal position trajectory is the original SUCC arithmetic history, and (F6) follows. No σ-additive real-time path-space probability measure or quantum branch choice is asserted. The time-slice operator is already exact, so subdividing a source unit into `k` pieces with (F2) yields identical `W_n(1)` for every integer `k` and the strong limit is trivial in this solvable class.

## F-03 — honest nondegenerate Fresnel paths via a declared quadratic regulator

For **ε>0** add quadratic momentum kinetic action:

\[
 \mathcal S_{N,\varepsilon}
 =\sum_{j=1}^N[p_j(x_j-16x_{j-1}-r(j))-\varepsilon p_j^2/2].
\tag{F8}
\]

This is a **different, expressly declared** discrete quantum dynamics. Define the free unitary `G_ε=exp(iε ħ_*/2 ∂_y²)` (Fourier multiplier `exp(-iε ħ_* k²/2)`) and regulated step `W_{n,ε}=G_ε W_n`. Each step is exactly unitary. At one step the kernel is

\[
 4 (2\pi i\varepsilon\hbar_*)^{-1/2}
 \exp\!\left(i\frac{(y-16x-r(n))^2}{2\varepsilon\hbar_*}\right),
\tag{F9}
\]

with the standard continuous square-root phase for ε>0. It is an **oscillatory Fresnel distribution**, not a function integrable in absolute value over all `x,y`. Formula (F9) follows by performing the one-dimensional Gaussian-Fresnel `p` integration with a vanishing damping cutoff. It is not an approximation guessed from a physical heat equation.

Now use the exact conjugation `W_n G_t=G_(256 t) W_n` (because position dilation is 16 and momentum is scaled reciprocally). Induction gives

\[
 W_{N,\varepsilon}\cdots W_{1,\varepsilon}
 =G_{\varepsilon C_N}W_N\cdots W_1,
\qquad C_N=\sum_{j=0}^{N-1}16^{2j}=\frac{16^{2N}-1}{255}.
\tag{F10}
\]

Thus the **full original-source N-time-slice Fresnel path integral** is exactly

\[
\boxed{K_{N,\varepsilon}(y,x)=
\frac{16^{N/2}}{\sqrt{2\pi i\varepsilon\hbar_*C_N}}
\exp\!\left[\frac{i(y-16^Nx-U_N)^2}{2\varepsilon\hbar_*C_N}\right].}\tag{F11}
\]

This is a genuine nondegenerate multi-path quadratic model at every finite N. In `S'` as ε→0+, `K_(N,ε)->K_N`. In Hilbert space, `G_t` is strongly continuous at zero, so `W_(N,ε)...W_(1,ε)->W_N...W_1` strongly for every **fixed N**.

**Exact stationary equations.** Varying each `p_j` gives `x_j=16x_(j-1)+r(j)+εp_j`. Varying internal `x_j` yields `p_j=16p_(j+1)`. Let `D=x_N-16^Nx_0-U_N`. The unique solution for ε>0 and fixed endpoints is

\[
 p_j=16^{N-j}\frac{D}{\varepsilon C_N},\qquad
 \mathcal S_{N,\varepsilon}(\mathrm{stationary})=\frac{D^2}{2\varepsilon C_N}.
\tag{F12}
\]

This is precisely the phase of (F11). Therefore the selected classical trajectory is the stationary/zero-regulator limit **for this declared quadratic model**. In general, the stationary point does not prove a unique quantum *actualization*: all intermediate histories are integrated coherently before readout.

A **separate positive/Wick-type partner** replaces each Fresnel factor with a normalized real heat kernel of variance ε ħ_*. It gives a bona fide Gaussian Markov path law `x_j=16x_(j-1)+r(j)+η_j`, with `η_j ~ N(0, ε ħ_*)` independent. Its endpoint is Gaussian with mean `16^N x_0+U_N` and variance `ε ħ_* C_N`. This is an honest positive stochastic model, NOT the real-time unitary amplitude; the quantum half-density `16^(N/2)` is different from Markov density normalization.

## F-04 — new-to-SUCC UNIFORM Fourier-band regulator bound

For any `ψ in L²(R)` with Fourier support `|k|<=K`, equation (F4) gives `supp Fourier(W_N...W_1ψ) subset [-K/16^N,K/16^N]`. The Fourier multiplier of (F10) is `exp(-i ε ħ_* C_N k²/2)`. Using `|exp(it)-1|<=|t|` and Plancherel,

\[
\begin{aligned}
\|(W_{N,\varepsilon}\cdots W_{1,\varepsilon}-W_N\cdots W_1)\psi\|_2
&\le\frac{\varepsilon\hbar_*C_NK^2}{2\cdot16^{2N}}\|\psi\|_2\\
&=\frac{\varepsilon\hbar_*K^2}{510}(1-16^{-2N})\|\psi\|_2\\
&<\frac{\varepsilon\hbar_*K^2}{510}\|\psi\|_2.
\end{aligned}\tag{F13}
\]

The effective Fresnel variance grows exponentially but the Fourier bandwidth of expanded packets contracts at the reciprocal rate. The bound is **uniform in every positive integer N**, any chosen positive scale ħ_*, and the ORIGINAL source (`r(j)` only produces a unit-modulus translation factor in Fourier space). This is a rigorous wavepacket-band theorem, NOT a pointwise kernel estimate or a proof of BBP source-selected normality.

## F-05 — the point-seed/Feynman smoothing trap (NEGATIVE theorem)

Let initial `ψ_{σ,p0}` be a normalized Gaussian with probability density `|ψ|²=N(0,σ²)` and optional plane-wave momentum `p0`. From (F4), the final probability density is `N(U_N,16^(2N)σ²)`. Hence every nonzero integral h has the exact real-circle character expectation

\[
\boxed{\langle W_N\psi,e^{2\pi i hX}W_N\psi\rangle
=e^{2\pi i hU_N}\exp(-2\pi^2 h^2 16^{2N}\sigma^2).}\tag{F14}
\]

For a Gaussian initially centered at a real seed `s` rather than zero, replace the phase in (F14) by `e^{2π i h(U_N+16^N s)}` while leaving the attenuation unchanged. For **any fixed σ>0**, it tends to zero even for the same-original-forcing changed seed `s=1/5−π/16` with completed `q=1/5`, whose point-seed orbit is provably NONNORMAL: `U_n(q)=16^n/5-T_n`, `16^n=1 mod5`, and the positive source Green tail `T_n=O(n^-2)`. Thus any 'π normality proof' that replaces its fixed point by a fixed-width L² quantum wavepacket and uses vanishing Fourier expectations is **REFUTED**.

To recover the deterministic phase along a growing horizon `N` with σ depending on N, one needs at least `16^N σ_N->0`; then `exp(-2π²h²(16^Nσ_N)²)->1` and (F14) transports each fixed h without a false positive. If `16^Nσ_N` approaches a nonzero constant, the phase suffers a nontrivial permanent attenuation. These are **exact resolution/limit-order statements**, not extra π source cancellation.

### F-05B — the imaginary-time/point-seed regulator has a different precision bill

For the **separate positive Gaussian/Wick partner** in F-03, start from the literal deterministic point `x0=0` and add independent Gaussian source-perturbing noise of variance `epsilon*hbar_*` at every arithmetic step. Then the endpoint distribution has mean the ORIGINAL `U_N` but variance `epsilon*hbar_* C_N`. Its exact character is

\[
\boxed{\mathbb E e^{2\pi i h X_N}
=e^{2\pi i h U_N}\exp[-2\pi^2h^2\varepsilon\hbar_*C_N].}\tag{F14B}
\]

If `epsilon>0` is fixed then this expectation vanishes for every `h!=0`, even on the same-source NONNORMAL counterseed. To preserve the point-phase along horizons N using epsilon_N, a sufficient (and for fixed h!=0 necessary for attenuation→1) condition is `epsilon_N * hbar_* * C_N ->0`, equivalently `epsilon_N*16^(2N)->0` when hbar_* is fixed. **This differs fundamentally from F-04**: F-04 has a uniform operator norm bound for initial *bandlimited L²* states at fixed epsilon, whereas F14B must resolve a *Dirac point seed* and pays exponential horizon precision. The imaginary-time partner has real positive normalized probabilities; no generic positivity-to-real-time signed cancellation arrow is asserted.

## F-06 — original-BBP noncommutative path interferometer (SOURCE-LABELLED MODEL)

There are two physically DECLARED but mathematically exact routes applying the **first two** BBP affine generators in different orders: `W_2 W_1` and `W_1 W_2`. Both have spatial dilation `16²`; their translations differ by

\[
\Delta=15(r(1)-r(2))=12301/273\ne0.
\tag{F15}
\]

Prepare a normalized Gaussian source packet `ψ(x)=constant*exp(-x²/(4σ²)+i p0 x/ħ_*)`. Denote the two possible final states by `φ_21=W_2W_1ψ` and `φ_12=W_1W_2ψ`. Their widths are both `16²σ`, and their final momentum is `p0/16²`. Direct Gaussian integration gives the exact *complex source-order visibility*

\[
\boxed{\langle\phi_{12},\phi_{21}\rangle
=\exp\left(-\frac{\Delta²}{8\cdot16^4\sigma²}\right)
 \exp\left(-i\frac{p_0\Delta}{16²\hbar_*}\right).}\tag{F16}
\]

The two routes can be put in a **declared controlled-order interferometer**:

`(|0>⊗φ_21+|1>⊗φ_12)/sqrt(2)`.

Measurement of control Pauli X/Y accesses the real/imaginary overlap and hence the authentic two-step ordering defect. This is genuine coherent *interference between two deliberately allowed quantum routes*, with SUCC-authenticated affine source labels. It is NOT an assertion that the original time-ordered arithmetic recurrence physically superposes these alternative temporal orderings. The selected source normality remains open.

An independent 60-digit mpmath Gaussian quadrature compared (F16) to explicit integration at σ=1/8, p0=3, ħ_*=2 and found absolute error `8.1e-62` (numeric diagnostic, not the proof; full formula follows by completing the square).

## F-07 — source/probe/authority map and frontier

These constructions re-use the **existing SUCC** `operational_yoneda_descent.ObservationPathCategory`, actual BBP affine source and `yoneda.FiniteFunctor` notion of source-faithful transport, as *external typed research components*, not a second category module. The real quantum Hilbert-space model is a NEW declaration: no physical apparatus or alternate-unitary generator is claimed source-deduced. The coefficients `r(n)` are the only source labels; operator ordering is inherited. The `ħ_*` value, free kinetic regulator ε, initial wavepacket, controlled two-order qubit, and stochastic/imaginary-time law are separate user/model inputs.

A finite oscillatory path integral is now rigorous **as a tempered distribution**, and an exact strongly continuous unitary time-sliced evolution is derived. However, extending the model to arbitrary interactions, an infinite-time quantum path **measure** or a unique physical path actualization requires further mathematical or empirical evidence. Existing rigorous real-time path-integral theory often uses oscillatory linear functionals and time-slicing, not σ-additive probability weights; do not transpose positive Feynman–Kac statements without verification.

The **selected π proof gate** is unchanged: for every fixed integer `h!=0`, prove `sum_{n<=N} e^{2π i h U_n}=o(N)` using authentic `U0=0`, complete four-pole forcing and real circle phase. The wavepacket expectation (F14), any source-blind path probability, and any action-transport identity alone do **not** pay the signed saving. A verdict-changing source-specific quantum-path result would be a NEW controlled estimate on ordered source phase/current or Fejér lag that fails on the coherent altered-seed and Gaussian-smoothing controls.

### Classical and primary mathematical references

- Daisuke Fujiwara, *Rigorous Time Slicing Approach to Feynman Path Integrals*, Springer (2017), DOI `10.1007/978-4-431-56553-6`: well-defined time-slicing and oscillatory integrals, with explicit regularity hypotheses. Our affine/Gaussian case is solved directly; we do not claim Fujiwara's theorem for an unverified potential class.
- Albeverio and Mazzucchi, *Infinite dimensional oscillatory integrals as projective systems of functionals*, J. Math. Soc. Japan 67 (2015), DOI `10.2969/jmsj/06741295`: why generalized oscillatory functionals are mathematically appropriate.
- Albeverio and Mazzucchi, *Feynman path integrals for polynomially growing potentials*, J. Funct. Anal. 221 (2005), DOI `10.1016/j.jfa.2004.07.014`: rigorous complex oscillatory integrations (a more difficult class than this exact affine model).
- Cordero et al., *Wigner Analysis of Operators. Part II: Schrödinger Equations*, Comm. Math. Phys. (2024), DOI `10.1007/s00220-024-04992-x`: metaplectic rescaling unitary operators.
- Parent SUCC #443 exact Hamiltonian/path-history band, #442 Riemann-sphere source residues, #441 finite Weyl clocks, #440 Pascal–Gamma source; and Main XVIII's selected signed-lag frontier. Those are inherited dependencies, not blind mathematical witnesses.

**Verdict:** All F-01–F-06 are classical/operator identities specialized to a genuinely authenticated arithmetic source, supported by explicit derivations and independent finite checks. The all-horizon selected signed phase theorem remains OPEN. No statement about real physical quantum dynamics is inferred.
