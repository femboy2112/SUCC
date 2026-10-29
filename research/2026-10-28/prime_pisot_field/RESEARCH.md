# Prime charges, Pisot virtual support, and zeta-field equilibria

**Date:** 2026-10-28. **Parent:** SUCC PR #349 at `ad19e3794f1d8da4a81418d38a4fc731b7d355c7` (Main XIII ancestor `b763ba8ef375fbac221e29e4396989a635a6ef36`). **Authority:** elementary paper proofs and exact finite probes, with separately labeled numerical observations. Academic priority and external review are UNVERIFIED. No RH, pi-normality, or physical-field claim. Local PPF identifiers below are not historical registry IDs.

## 0. Steelman and source contract

The author's proposal is that SUCC can generate a virtual supporting field through Pisot-type hidden modes; prime-specific charges distinguish elementary states from composites; and the zeta zeros may have an equilibrium interpretation in that field. We preserve all three parts, but distinguish an arithmetic state, a transfer eigenmode, a zero of a scalar response, and a stationary point of a potential. They are different mathematical types until an explicit map connects them.

We use the actual inherited divisor fibers and marked states from OLZF-04, and the actual PCR-02 leakage form, not a substitute random field. Their sources and immutable blob pins are in SOURCES.md. We then construct a prime-indexed quadratic Pisot realization, prove a zero-divisor-preserving analytic transport, and test which stronger conclusions fail. No nontrivial zeta zero location is a construction input. All constructions retain the original integer label unless a change of arithmetic energy is explicitly declared.

Three distinct fidelities must not be conflated:

1. **Source fidelity:** original integer labels, coefficients, selected seed, and observables are preserved.
2. **Zero-divisor fidelity:** the same zeros with the same multiplicities occur in a stated domain.
3. **Positive support:** a probability, Hilbert norm, or nonnegative quadratic form exists.

Zero-divisor fidelity and positive support do not establish source fidelity. Source fidelity alone supplies no new positivity theorem for a different spectral pairing. The constructions below give explicit separations.

## 1. PPF-01: the prime charge algebra (elementary paper proof)

On the finite-support core of `ell^2(N_{>=1})`, put

$$S|n\rangle=|n+1\rangle,\quad V_p|n\rangle=|pn\rangle,\quad N_p|n\rangle=v_p(n)|n\rangle.$$

Unique factorization gives, for every pair of genuine primes p,q,

$$[N_q,V_p]=\delta_{pq}V_p,\qquad N=\sum_pN_p,\qquad N|n\rangle=\Omega(n)|n\rangle.$$

The sum is finite on each basis vector. The elementary sector is exactly `N=1`, so `Pi_prime=1_{N=1}`; the one-prime label p is the basis ray `|p>`. This is an exact occupation-charge interpretation, not a physical electric charge or a proof that nature chooses this observable. With `H|n>=log(n)|n>`,

$$\operatorname{Tr}(\Pi_{\rm prime}e^{-sH})=\sum_p p^{-s},\qquad \Re s>1.$$

**Proof:** `v_q(pn)=v_q(n)+delta_pq`; `Omega(n)=1` iff n is prime. Absolute convergence is dominated by the ordinary zeta series. The independent phase action `U_theta|n>=exp(i sum_p theta_p v_p(n))|n>` satisfies `U_theta V_p=e^{i theta_p}V_pU_theta`. Prime labels can therefore be retained by the full charge torus, rather than one scalar energy.

Charge is not conserved by additive SUCC:

$$[N_p,S]|n\rangle=[v_p(n+1)-v_p(n)]|n+1\rangle.$$

At `n=p^k-1` the coefficient is k; at `n=p^k` it is -k. It is unbounded in both signs, while the affine relation `V_p S=S^p V_p` still holds. Any claimed interaction dynamics must respect both facts.

## 2. PPF-02: what the existing virtual equilibrium actually selects

The inherited source fiber and uniform marked vector are

$$\mathcal H_n=\operatorname{span}\{|a,b\rangle:ab=n\},\quad
\omega_n=d(n)^{-1/2}\sum_{ab=n}|a,b\rangle.$$

For `n=product p^j`, splitting each exponent between a and b gives a canonical prime-labeled tensor decomposition

$$\mathcal H_n\cong\bigotimes_{p^j\Vert n}\mathbb C^{j+1},\qquad
\omega_n=\bigotimes_{p^j\Vert n}\omega_{j+1}.$$

The authentic PCR-02 leakage matrix on `C^m` is

$$\langle v,L_m v\rangle=\frac1{m(m+1)}\sum_{l=1}^{m-1}l(m-l)|v_l-v_{l-1}|^2.$$

Every coefficient is strictly positive for `1<=l<m`; hence `L_m>=0` and its kernel is the uniform ray. Define `L_n` to be the tensor sum of these prime-local matrices, with `L_1=0`.

**Theorem:** For every integer `n>=1`, `L_n>=0` and `ker L_n=span{omega_n}`. In the orthogonal direct sum, the kernel is the complete marked source subspace `J ell^2(N)`, where `J|n>=omega_n`.

**Proof:** the energy is a sum of nonnegative edge differences on the connected Cartesian product of finite paths. Vanishing forces every coordinate to be equal. Alternatively, the kernel of a sum of commuting positive tensor operators is the tensor product of their kernels. The direct-sum assertion follows blockwise; no finite uniform spectral gap is assumed.

Thus composites are fully supported equilibria too: `n=4,6,12,...` all have their own zero-energy marked state. Moreover `sum_n c_n omega_n` has zero energy for every square-summable coefficient sequence, including arbitrary phases. Source support does not select the phase sequence needed for a zeta or BBP conclusion.

Adding `(Omega(n)-1)^2 I` to each block makes the kernel prime-only, exactly. But it adds an independent grade-selection term. It does not derive primality from PCR leakage. Positive prime-dependent weights on the summands do not change this obstruction.

**Finite-observer obstruction:** for a finite menu P of prime-local registers, pick q outside P. The states `omega_n` and `omega_{nq}` have the same reduced state on P. Thus no observable supported only on those registers distinguishes a prime n in P from the composite nq. The simpler inherited overlap already shows `F_2(2)=F_2(6)=2/3`.

**Character-null obstruction:** the inherited characteristic function factorizes as

$$\chi_n(t)=\prod_{p^j\Vert n}\frac{\sin((j+1)t\log p)}{(j+1)\sin(t\log p)}.$$

At removable singularities use the finite sum definition. If `chi_p(t)=0`, then `chi_pq(t)=0` for every different prime q. A local null is inherited by composites, not exclusively owned by p. At `t log p=pi/2`, `chi_{p^2}=-1/3`, so prime repetitions and products of distinct primes must also be distinguished.

## 3. PPF-03: connected extraction, not invented composite repulsion

For `Re s>1`, absolute convergence licenses

$$\log\zeta(s)=\sum_{p,k\ge1}\frac{p^{-ks}}k.$$

Only prime powers occur in this connected expansion. Möbius inversion removes repetitions:

$$P(s)=\sum_p p^{-s}=\sum_{k\ge1}\frac{\mu(k)}k\log\zeta(ks).$$

Indeed the coefficient of `p^{-js}` on the right is `(1/j) sum_{k|j}mu(k)`, equal to one for j=1 and zero otherwise. These are classical Euler-product identities [S1], not new definitions of primality.

Two source controls are decisive. Adding an independent generator 4 yields `Z_fake= zeta(s)/(1-4^{-s})`: the coefficient at 4 becomes 2, its logarithmic coefficient becomes 3/2, and primitive extraction wrongly treats 4 as an extra generator. Penalizing composites by `a_q(n)=q^{Omega(n)(Omega(n)-1)/2}` also changes the source. Its coefficient at 6 is q and the coefficient at 6 in its Dirichlet logarithm is `q-1`; for q=1/2 this is -1/2, not zero.

The complete 2x2 experiment combines fake-4 present/absent and q=1/2 penalty present/absent. At the coefficient of `12^{-s}` in the Dirichlet logarithm, its mixed contrast is -3/8. All four cells, not a partial comparison, are present in the test suite. This interaction is a diagnostic of the declared deformation, not a physical prime force.

**Zero matching is weaker than source matching:** the fake-4 multiplier is holomorphic and nonzero throughout `Re s>0`. It preserves the genuine nontrivial zeros despite the wrong coefficients. Similarly removing finitely many authentic Euler factors preserves the nontrivial zero divisor. Individual zeros cannot be assigned exclusively to one independent prime factor on this evidence.

## 4. PPF-04: a constructive Pisot virtual register

For every integer `m>=1`, define

$$\beta_m=\frac{m+\sqrt{m^2+4}}2,\quad \beta'_m=-\beta_m^{-1},\quad
A_m=\begin{pmatrix}m&1\\1&0\end{pmatrix}.$$

The polynomial `x^2-mx-1` is irreducible over Q (its discriminant is not an integer square), and `beta_m>1`, `|beta'_m|<1`; hence beta_m is a quadratic Pisot unit. The integer recurrence

$$L_0=2,\ L_1=m,\ L_k=mL_{k-1}+L_{k-2}$$

gives `beta_m^k+(-beta_m^{-1})^k=L_k`. The contracting branch supplies exact virtual correction to an integer trace. This works for composite m as well as primes: Pisot contraction alone does not test primality.

Normalize `T_m=A_m/beta_m` and set `c_m=beta_m^{-2}`, `D_m=diag(beta_m,1)`. Then

$$D_m^{-1}T_mD_m=\begin{pmatrix}1-c_m&c_m\\1&0\end{pmatrix}=M_m.$$

This is a positive row-stochastic two-register realization. Its stationary row distribution is `(1/(1+c_m), c_m/(1+c_m))`. For a column state `(u,v)`, the update is `u'=(1-c)u+cv`, `v'=u`, so the mismatch obeys `u'-v'=-c(u-v)`. Thus virtual support has an explicit causal memory law, not merely a spectral analogy. Its modes are the supported constant mode 1 and the contracting alternating mode -c.

On the same realization,

$$\det(I-zT_m)=(1-z)(1+c_mz),\quad
\operatorname{tr}(T_m^k)=1+(-c_m)^k.$$

The rank-one invariant projection `P_+=(T_m+c_m I)/(1+c_m)` instead satisfies `tr(P_+ T_m^k)=1`. Ordinary and marked traces are different observables.

## 5. PPF-05: Pisot clocks retain the entire critical-strip zero divisor

This is a constructive connection to the actual zeta zeros, with a precise limitation.

For each genuine prime p choose the preceding `beta_p`. Keep the original arithmetic occupation labels and put

$$B(n)=\prod_p\beta_p^{v_p(n)},\quad H_\beta|n\rangle=\log B(n)|n\rangle.$$

Different labels with equal B(n) remain distinct states. Since `beta_p>p`, `B(n)>=n`; for `sigma=Re s>1`,

$$Z_\beta(s)=\operatorname{Tr}(e^{-sH_\beta})
=\sum_{n\ge1}B(n)^{-s}=\prod_p(1-\beta_p^{-s})^{-1}.$$

This uses unique factorization of the original label n, NOT independence of the real logarithms `log beta_p`.

**Theorem:** There is a holomorphic, nowhere-zero function C on `Re s>0` such that

$$Z_\beta(s)=\zeta(s)C(s).$$

This identity continues Z_beta meromorphically from `Re s>1` to `Re s>0`. Its zeros there coincide with the zeta zeros with exactly the same multiplicities; its pole at 1 also remains simple.

**Proof.** Write `delta_p=log(beta_p/p)`. The quadratic equation gives `beta_p=p+1/beta_p`, hence

$$0<\delta_p=\log(1+1/(p\beta_p))<p^{-2}.$$

For `sigma>0`, define

$$h(s)=\sum_{p,k\ge1}\frac{\beta_p^{-ks}-p^{-ks}}k.$$

Using `exp(-ks delta)-1=-ks integral_0^delta exp(-ksu)du` and `Re s>0`,

$$\left|\frac{\beta_p^{-ks}-p^{-ks}}k\right|
\le |s|\delta_p p^{-k\sigma}.$$

Thus the double series converges locally uniformly in `Re s>0`, dominated on compact sets by a constant times `sum_p p^{-2-sigma}`. Its exponential `C=exp(h)` is holomorphic and nowhere zero. In `Re s>1`, convergent logarithms of the Euler factors give `Z_beta/zeta=exp(h)` directly. The claimed continuation and equal zero multiplicities follow. No zero location or RH assumption entered the proof. QED.

For integer cutoff P>=1, the same proof gives the explicit mathematical tail

$$|h(s)-h_P(s)|\le
\frac{|s|}{1-2^{-\sigma}}\frac{P^{-1-\sigma}}{1+\sigma}.$$

For `sigma>=1/2`, `|s|<=R`, a rational upper bound is `(8R/3)/floor(sqrt(P))^3`. At P=10000 and R=18 it is exactly `3/62500`. This bounds omitted analytic terms, not floating-point roundoff. Finite numerical evaluations in the receipt remain OBSERVED.

### PPF-06: a non-Pisot control proves the scope is not Pisot-specific

Replace beta_p by `q_p=p+1/p`, a nonintegral rational and therefore not an algebraic integer/Pisot number. It has the same bound `0<log(q_p/p)<p^{-2}`. The entire proof applies, so its generalized trace has the same critical-strip zero divisor too. The property sufficient for this theorem is summably small logarithmic clock displacement, not Pisot contraction.

By contrast `q_p=p^c` gives `Z_q(s)=zeta(cs)`, moving the zero locations when c differs from 1. That displacement does not satisfy the small-clock hypothesis. This is a discriminating control, not a contradiction.

The conclusion is **zero-divisor transport**, not unchanged arithmetic source, positive spectral realization of all zeros, or a proof that their real parts equal 1/2. The energies have explicitly changed. The positive self-adjoint operator H_beta has eigenvalues log B(n), NOT the nontrivial zeta zeros; its positivity is not a Hilbert-Polya realization of those zeros. The usual gamma/pole completion becomes `C(s)xi(s)` on this domain; it is not automatically symmetric. On `0<Re s<1` it satisfies only the derived twisted equation

$$C(s)\xi(s)=\frac{C(s)}{C(1-s)}\,C(1-s)\xi(1-s).$$

The multiplier has modulus one on the critical line by real conjugation, but this fact alone places no zeros there.

## 6. PPF-07: an exact collision makes prime labels indispensable

Let `phi=(1+sqrt(5))/2`. Direct algebra gives

$$\beta_{11}=\phi^5=(11+5\sqrt5)/2,\qquad
\beta_{29}=\phi^7=(29+13\sqrt5)/2.$$

Consequently

$$\boxed{\beta_{11}^{\,7}=\beta_{29}^{\,5}=\phi^{35}},\qquad
11^7=19487171\ne20511149=29^5.$$

These are different original prime-power histories with exactly the same Pisot clock energy. The scalar clock cannot reconstruct its arithmetic source. Collapsing these states into one would change the trace multiplicity and invalidate the source-indexed Euler expansion. Retaining the full charge vector resolves the ambiguity.

This also prevents importing generalized-prime theorems that assume rational independence of all prime logarithms. [S2] makes that assumption in its definition; it does not directly license this labeled, degenerate system. The proof in section 5 does not need that assumption.

## 7. PPF-08: virtual-mode decoration and finite trace rigidity

There is another exact bridge using the ORIGINAL prime periods `log p` with the new two-register support. For `Re s>1`, form

$$D_\beta(s)=\prod_p\det(I-p^{-s}T_p)^{-1}
=\zeta(s)E(s),\qquad
E(s)=\prod_p(1+c_p p^{-s})^{-1}.$$

Because `0<c_p<p^{-2}`, the logarithm of E converges absolutely and locally uniformly for `Re s>-1`: on every compact subset, `|c_pp^{-s}|<=p^{-2-sigma}<1` and the sum is bounded by a constant times `sum_p p^{-2-sigma}`. Therefore E is holomorphic and nowhere zero on that half-plane. This decoration also leaves all nontrivial zeros unchanged.

Nevertheless its local coefficient at `p^j` is `sum_{k=0}^j(-c_p)^k`, positive but not the original 1 for j>=1. In particular the prime coefficient is `1-c_p`. Positive support and unchanged zeros have not authenticated the source.

**Finite trace rigidity:** for a finite matrix T, if `tr T^k=1` for every k>=1, the formal identity

$$\det(I-zT)=\exp\left(-\sum_{k\ge1}\frac{z^k}{k}\operatorname{tr}T^k\right)=1-z$$

implies that the only nonzero eigenvalue, with algebraic multiplicity, is a single 1. Additional zero/nilpotent modes are not excluded. Hence a nonzero stable Pisot mode cannot be visible in an ordinary finite determinant while preserving every original one-prime repeated-orbit coefficient. The marked projection P_+ restores those coefficients, but makes this stable mode invisible to that readout.

This is scoped to ordinary finite traces. It does NOT exclude a meaningful supertrace, cohomological cancellation, interacting infinite realization, or a source-derived marked trace. Constructing one with the required global duality and positivity is a distinct unsolved task here.

## 8. PPF-09: zeros, field charges, and equilibria are not interchangeable

Let f be holomorphic near a zero rho of multiplicity m. Factor `f(s)=(s-rho)^m g(s)` with `g(rho)!=0`. Then

$$f'/f=m/(s-\rho)+g'/g.$$

Thus rho is a pole/charge of the logarithmic response, not a regular zero-force point. In real coordinates, distributionally `Delta log|f|=2pi sum m delta_rho` locally. This follows from the corresponding logarithm identity for `s-rho` and harmonicity of `log|g|`.

If instead one declares the potential `U=|f|^2`, every simple zero is a strict local minimum with Hessian `2|f'(rho)|^2 I`. That equilibrium property is true at off-line zeros just as at critical-line zeros; it cannot select the line.

**Exact polynomial control:** set `w=s-1/2`,

$$f(s)=((w-1/4)^2+4)((w+1/4)^2+4).$$

It has real coefficients, `f(s)=f(1-s)`, and an off-line zero `rho=3/4+2i`. At rho, `f'=-8+i`, the Hessian of `|f|^2` is `130 I`, and the residue of `f'/f` is 1. These were reconstructed symbolically, not fitted to zeta zeros.

### PPF-10: even positive virtual support plus both symmetries is insufficient

The stronger entire control

$$G(s)=2+\cosh(4(s-1/2))$$

is order one, real under conjugation, and symmetric under `s -> 1-s`. On the critical line,

$$G(1/2+it)=2+\cos(4t)$$

is the Fourier transform of the positive measure `2 delta_0+(delta_4+delta_-4)/2`. It therefore has positive-semidefinite finite Gram matrices on that line (not strictly positive definite for arbitrary matrix size). Yet its zeros are

$$s=\frac12\pm\frac{\operatorname{arcosh}2}{4}+\frac{(2k+1)\pi i}{4},\qquad k\in\mathbb Z.$$

They are off the critical line and inside the critical strip because `0<arcosh(2)<2`. At the positive-sign k=0 root, `G'=-4sqrt(3)` and the Hessian of `|G|^2` is `96 I`. Positive support, symmetry, and stable minima all survive this hostile model. It lacks the authentic Euler coefficients and archimedean completion, so it is a counterexample to their proposed substitutes, NOT to RH.

Similarly `diag(2,1/2)` preserves the indefinite pairing `[[0,1],[1,0]]` but no positive-definite invariant Hermitian form: invariance forces both diagonal entries of such a form to zero. Balanced reciprocal modes do not imply normalized unitarity.

## 9. Classical zero dynamics: a closer, but conditional, comparison

The de Bruijn-Newman heat deformation supplies an established interacting-zero framework [S3]. Under its real/simple-zero and convergence conditions the zero motion has the form `x_j'=2 sum_{k!=j}1/(x_j-x_k)`, with the required interpretation of the infinite sum. These are generally moving interacting zeros, not stationary points each attached to a single prime. Rodgers and Tao prove nonnegativity of the de Bruijn-Newman constant; that does not prove RH. Their local-equilibrium argument is part of a contradiction under an additional negative-constant assumption, not a claim that the actual zeros are exactly equally spaced.

A finite calibration is `f_t(w)=w^2-1-2t`, satisfying `partial_t f=-partial_w^2 f`. Its positive zero `sqrt(1+2t)` has nonzero speed `1/sqrt(1+2t)`, exactly equal to the two-zero interaction law. This calibrates the dynamics without supplying zeta zero coordinates.

## 10. Verdict and next construction gate

**SURVIVES:** prime-graded virtual support has an explicit positive Pisot register, and a genuine all-prime analytic construction carries precisely the actual zeta zero divisor. The charge labels are essential, as the exact 11/29 collision demonstrates. The zero divisor emerges collectively, not from one independent prime-local root.

**FAILS in the tested scope:** PCR support alone selects primes; local character nulls exclude all composites; generic composite repulsion preserves zeta; positive support and reflection symmetry force RH; or zero preservation identifies a source. Each has an explicit countermodel above.

**UNVERIFIED:** a source-derived global interaction/pairing on these virtual states, compatible with original prime powers, additive SUCC, and completed Gamma/pole data, that forces a full realization of the zeta zeros to be unitary after half-density normalization. The current trace identities do not provide it.

The next verdict-changing task is to construct that global pairing from the source, or prove a scoped obstruction. It must distinguish the authentic source from fake-4, the rational non-Pisot deformation, arbitrary phases in the PCR kernel, and the positive-cosh counterfeit. It may use a marked or graded trace, but must state why that trace is forced rather than inserted. A potential built from known zeros, an RH-assuming spectral metric, or a finite numerical fit does not pass.

All finite computation is subordinate to the displayed analytic/algebraic proofs. No independence of separate agents is asserted: this run used one reasoner, distinct implementations, source families, algebraic derivations, holdouts, and actual mutations. The discovered shared-oracle blind spot and its repair are retained in VALIDATION.md and the raw receipts.
