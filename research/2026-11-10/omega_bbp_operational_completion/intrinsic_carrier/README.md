# Source-first Ω–Haar carrier extension: arithmetic Hamiltonians and finite-Mellin inverse aliases

**Research date:** 10 November 2026. **Intended parent:** draft #582, head `762c99952fc28c46754cb2d30a3adf0a52816721`; it rests on #579 and #576, not on main. **Scope:** additive research artifacts, no frozen source or prior dossiers rewritten. **Authority:** paper-level theorems with exact finite tests, *not* a proof of π normality, RH, quantum advantage, physical MERA, or source-to-lambda compiler.

## Executive result

We advance the user's **forward injection / noninjective reverse / orientation** proposal in two genuinely distinct directions:

1. **Intrinsic carrier:** On `ℓ²(N_{≥1})`, the additive successor `S|n⟩=|n+1⟩` and multiplicative dilation `V_p|n⟩=|pn⟩` generate a **Toeplitz–Cuntz-type inverse-branch packet with a finite rank boundary defect**. Its genuine Haar low-pass (`B_p`) and prime-divisibility (`Q_p`) projections give an explicit *source-free* Hermitian arithmetic Hamiltonian `H_p=i[B_p,Q_p]`. For `p=2,3`, the chronological `[B_2,B_3]` reproduces the BBP six-block Ω₄/Ω₅ oscillator in each bulk block **plus an independently characterized five-site boundary oscillator**. A Bost–Connes-like diagonal `H_0|n⟩=(log n)|n⟩` gives `Tr(e^{-β H_0})=ζ(β)` for β>1 and an exact thermal identity for `H_p²`. It does not give RH.
2. **Finite inverse/observation:** For **every** `N≥0`, explicitly construct a *different, strictly positive*, `(1−x)`-factored rational-source kernel with exactly the same first `N+1` sampled Mellin moments as the genuine four-pole BBP kernel, but with a **strictly larger completed value**, bounded between two explicit rational numbers. This is an exact information-loss witness for any finite-moment reverse fold, even within positive kernels preserving the endpoint cancellation. It does **not** keep the four-pole contract; source-authentication remains essential.

The constructions complement the parent [inverse-beta BBP root](../INVERSE_BETA_BBP_ROOT.md), [Ω₄/Ω₅ Haar source oscillator](../OMEGA_HAAR_WAVELET.md), and [finite quantum dagger bridge](../quantum_bridge/README.md). See [PROOFS](PROOFS.md) and [claim ledger](CLAIM_LEDGER.md).

## 1. Intrinsic carrier, not source decoration

Let `H=ℓ²(N_{≥1})` on basis `|n⟩`. For any integer `p≥2`, `S|n⟩=|n+1⟩`, `V_p|n⟩=|pn⟩` satisfy the SUCC/FUCC affine relation `V_p S=S^p V_p`. The `p` child maps `T_{p,a}=S^a V_p`, `0≤a<p`, are isometries with orthogonal ranges and

\[
T_{p,a}^{*}T_{p,b}=\delta_{ab}I,\qquad
\sum_{a=0}^{p-1}T_{p,a}T_{p,a}^{*}=I-E_{<p},\qquad
E_{<p}=\sum_{1\le n<p}|n\rangle\langle n|.
\]

This is **not** the unital Cuntz relation on positive integers: the `p−1` boundary basis vectors are missing. The exact inverse observer is the unitary partition into the finite boundary register and the `(m,a)` registers with `n=pm+a`; no detail is discarded before low-pass postselection. On `ℓ²(N_0)` the range partition is unital, but the zeta Hamiltonian `log n` is undefined at zero. This is a measurable choice of arithmetic carrier/boundary.

Define `W_p=(1/√p)Σ_{a=0}^{p-1}T_{p,a}`, `B_p=W_p W_p*` and `Q_p=V_p V_p*`. Both are orthogonal projections, yet they do not commute. The **intrinsic arithmetic Hamiltonian** is

\[
\boxed{H_p=i[B_p,Q_p]
=\frac{i}{p}\sum_{m\ge1}\sum_{a=1}^{p-1}
\left(|pm+a\rangle\langle pm|-|pm\rangle\langle pm+a|\right).}
\]

On each block `pm,...,pm+p−1`, its spectrum is `±√(p−1)/p` with `p−2` zeros; it vanishes on `1,...,p−1`. For `p=2`, `H_2²=(I−|1⟩⟨1|)/4`. `H_p` is a bounded **self-adjoint** operator; `e^{−itH_p}` is unitary. These are exact operator identities, not a correspondence to a physical laboratory Hamiltonian.

**Hostile controls:** Composite `p` obeys the same formulas; diagonal prime-divisibility projectors `Q_p,Q_q` commute and yield a *zero* commutator. Thus this construction alone does not extract primes or zeta zeros. Antiunitary complex conjugation maps `H_p↦−H_p`; its nonzero spectrum is symmetric and cannot be a positive Weil form.

## 2. Ω₄/Ω₅ reappear in the arithmetic carrier, including a boundary payment

The source-first Ω₄/Ω₅ computational diamond `(F²)³=(F³)²=F⁶` is independent of these projections; its observed disagreement comes specifically from *overlapping chronological* pair/triple averages. Let `B_2,B_3` be the intrinsic block projections just defined. Their commutator, on `ℓ²(N_{≥1})`, splits as

\[
\boxed{i[B_2,B_3]\cong H_\partial\oplus\bigoplus_{m\ge1} H_6.}
\]

Here the boundary occupies `|1⟩,...,|5⟩`, with `σ(H_∂)={0,0,0,±√5/6}`. Each subsequent block `|6m⟩,...,|6m+5⟩` has `σ(H_6)={0,0,0,0,±√2/3}`. **The exact √2/3 spectrum already proved in the six-entry BBP wavelet is the bulk spectrum of an operator on the full arithmetic carrier.** The finite √5/6 mode is the boundary choice's additional information, not a BBP source signal. Real time reversal / complex conjugation flips the Hamiltonian, preserving spectral magnitudes.

## 3. Actual zeta bridge, and why it is not RH

Let `H_0|n⟩=(log n)|n⟩`, with its standard self-adjoint diagonal domain. Then `e^{itH_0}V_p e^{−itH_0}=p^{it}V_p`, and for real `β>1`, `Z(β)=Tr(e^{−βH_0})=ζ(β)` (the known Bost–Connes energy representation; see [Marcolli's QSM notes](https://www.its.caltech.edu/~matilde/NotesBCsystemQSM.pdf)). For every integer `p≥2`,

\[
\boxed{\mathrm{Tr}(e^{−\beta H_0}H_p^2)
=\frac{\zeta(\beta)\big[1+(p-2)p^{−\beta}\big]-\sum_{a=1}^{p-1}a^{−\beta}}{p^2}.}
\]

The Gibbs-normalized expectation is this divided by `ζ(β)`. In particular,

\[
\boxed{\langle H_2^2\rangle_\beta=\tfrac14(1-\zeta(\beta)^{−1}),\qquad\langle H_p\rangle_\beta=0.}
\]

**Crucial negative control:** The `p=2` identity merely measures the Gibbs probability away from the basis vector `|1⟩`. It carries ζ as the partition-function normalizer; it has no new zero-free region or Weil positivity content. The trace exists as a positive Gibbs trace for `β>1`, not on the critical line. A weighted prime-indexed field `Σ_{p prime}(log p)p^{−σ}H_p` converges absolutely in operator norm when `Re σ>1/2`, by the bound `||H_p||≤p^{−1/2}`. This is a **sufficient operator norm convergence domain**, not an RH theorem or analytic continuation to its boundary. On finitely supported vectors the sum is locally finite for all coefficients because `H_p|n⟩=0` when `p>n`. Closure/self-adjointness outside norm convergence remains open.

The authentic prime–Archimedean dynamical interaction is already observable on each directed edge:

\[
e^{itH_0}|pm+a\rangle\langle pm|e^{−itH_0}
=\left(\frac{pm+a}{pm}\right)^{it}|pm+a\rangle\langle pm|.
\]

This is a concrete carrier-level bridge to SUCC's prior prime-jet/log-energy work, but **not** a substitute for the signed Weil explicit formula, its completed Γ factor, admissible test-function space, source/oracle provenance or the RH-equivalent positivity obstruction.

## 4. Exact finite-Mellin inverse defect, even for positive kernels

The source-derived BBP polynomial is

\[
P(x)=4-2x^3-x^4-x^5=(1-x)M(x),\quad
M(x)=(x^2+2)(x^2+2x+2)\ge4\quad(0\le x\le1).
\]

Writing `t=x⁸`, use the positive moment measure `dν=(1−x)dx`, with `ν_k=1/[(8k+1)(8k+2)]`. For every `N≥0`, form the **unique monic** polynomial `q_N(t)` of degree `N+1` orthogonal to `1,t,...,t^N` in this positive measure. The Gram matrix is positive definite, all coefficients are rational, and all its roots lie in `(0,1)`.

Let `ε=(Σ_j |[t^j]q_N|)^{-1}>0`, and mutate only the *adversarial control source*:

\[
P_\epsilon(x)=(1-x)\big[M(x)+\epsilon q_N(x^8)\big].
\]

Because `|εq_N(t)|≤1` on `[0,1]`, `P_ε>0` for `0≤x<1`, and `P_ε(1)=0`. It is different from the original four-pole source but preserves its endpoint root and positivity. For **every** `0≤n≤N`,

\[
\boxed{\int_0^1 x^{8n}P_\epsilon(x)dx
=\int_0^1 x^{8n}P(x)dx.}
\]

However the completed BBP-type sums differ *strictly*:

\[
\begin{aligned}
\Delta\Pi&=\int_0^1\frac{P_\epsilon(x)-P(x)}{1-x^8/16}\,dx\\
&=\frac{16\epsilon}{q_N(16)}\int_0^1\frac{(1-x)q_N(x^8)^2}{16-x^8}\,dx>0.
\end{aligned}
\]

Thus with the **exact rational** squared norm `D_N=∫(1−x)q_N(x⁸)² dx`,

\[
\boxed{0<\frac{\epsilon D_N}{q_N(16)}<\Delta\Pi<\frac{16\epsilon D_N}{15q_N(16)}.}
\]

For `N=0`, `q_0(t)=t−1/45`; the completed difference lies in `(0.0001849684664,0.0001972996976)` (bounds, not a π interval). The finite first moment is identical exactly. The arbitrary-N proof uses orthogonality and the Cauchy-transform identity; no numerical extrapolation.

**Interpretation:** the forward **all-index** Mellin observer is injective (previous branch), but every finite slice has an exact nontrivial nullspace *even within positive endpoint-factored sources*. A finite quantum circuit loaded only from those observed moments cannot tell the two sources apart. The authentic frozen **four-pole identity**, rather than positivity/moment agreement alone, selects the true π source.

## 5. Sixteen-branch Ω–Haar and the selected orbit

For the radix-16 phase map `T(θ)=16θ (mod 1)`, every inverse has a branch digit `d∈{0,...,15}`. The four-qubit inverse-label register and its Haar/Fourier packets are **unitary with all branch information retained**. Forgetting `d` is a non-injective average or partial trace. An exactly reversible lift is a *separate* natural extension carrying the full past digit string; it is not the non-invertible circle map itself. The parity sign character `(-1)^d` is a genuine character of cyclic group `Z/16Z`: for odd `p`, `(-1)^d` is **not** a character of `Z/pZ`, so the Möbius sign cannot naively be carried over to all prime channels.

Do **not** identify the integer-carrier residue `n mod 16` with the hexadecimal **digit of π**. The latter depends on the selected phase `Y_n=16^n(π/16)`, exact floor/winding and the original zero seed. A sound source-to-digit reversible oracle must retain `n`, rational `P_L`, the seed, integer carry, four-pole forcing, inverse branch and scratch/precision budget; no such full circuit/compiler is certified here. A source-blind observer has the same input on the coherent wrong-seed control `s=−π/16`, whose completed orbit is zero and digit parity is 1. Therefore **no source-only Hamiltonian statistic can by itself force selected digit balance**.

The earlier [quantum phase-tail bound](../quantum_bridge/README.md) is retained: for `n≥0,L≥1`,

\[
0<16^n(P_\infty-P_L)<\frac{16^{n-L}}{(8L+1)(8L+2)},\qquad P_\infty=\pi/16.
\]

This pays smooth Fourier precision only; discontinuous parity additionally requires a boundary-strip count. The remaining genuine arithmetic gate is source-selected decay of the **signed** epoch mean `c_A(8(2j+1))`, for every fixed integer `j`, not another source-only positive norm. That condition would give fair parity words but not full hexadecimal normality.

## 6. Reproducible artifacts and integration

- [PROOFS.md](PROOFS.md): quantified proofs, spectral and thermal identities, exact alias/Cauchy-transform inequality, falsifiers.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): separate claims and evidence grades; π/RH remain OPEN.
- [intrinsic_carrier.py](intrinsic_carrier.py), [finite_alias.py](finite_alias.py): rational reference implementations.
- [test_intrinsic_carrier.py](test_intrinsic_carrier.py), [test_finite_alias.py](test_finite_alias.py): **22 fast focused tests passed** with `python -W error -m unittest discover ...` (local Python 3.13.5). Optional test dependencies: `mpmath`, `sympy`.
- [independent_carrier_audit.py](independent_carrier_audit.py): independent SymPy/MPMath matrix and positive alias check; same researcher, not blind external referee.
- [VALIDATION.md](VALIDATION.md): exact execution and source-hash receipts; **long repo-native suite/hosted CI not rerun**.
- [NEXT.md](NEXT.md): proof-producing next discriminators and no-go controls.
- [SOL_6_1_ULTRA_MAIN_INTEGRATION_PROMPT.md](SOL_6_1_ULTRA_MAIN_INTEGRATION_PROMPT.md): full Work-mode handoff to consolidate the stacked PRs onto current main under explicit tests/CI gates, never claiming a proof that is still open.

**Primary scholarly context:** Fijany & Williams, [Quantum Wavelet Transforms](https://arxiv.org/abs/quant-ph/9809004); Selinger–Valiron, [Quantum Lambda Calculus](https://doi.org/10.1017/S0960129506005238); Marcolli, [Bost–Connes QSM notes](https://www.its.caltech.edu/~matilde/NotesBCsystemQSM.pdf). This paper does not claim priority for Haar, Cuntz, Bost–Connes, or quantum-circuit concepts. The source-specific finite-alias proposition and intrinsic coupling have explicit proofs, but external priority review remains unpaid.
