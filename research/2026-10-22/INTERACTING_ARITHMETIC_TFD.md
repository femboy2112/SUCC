# Interacting arithmetic quantum mechanics: spectral stability and actual entanglement

**Baseline:** SUCC `b116841f12b41aaf7600da39bbb40577f25b6295`.
**Branch:** `research/prime-bridge-2026-10-22`.
**Status:** complete paper proofs below; exact rational finite controls and
separately labelled floating diagnostics. No Lean certification is claimed
for the infinite-dimensional theorems. Scholarly priority is unverified.

## 0. Hole contract and provenance

**Question.** Does a bounded additive SUCC interaction preserve the arithmetic
Gibbs threshold while creating correlations between the otherwise independent
prime factors? The weakest sufficient positive result is a spectral comparison,
an actual entangling unitary, and a Gibbs nonproduct witness in a fixed declared
factorization. Neither entropy growth nor nonproductness supplies a bulk metric.

**Hypotheses.** The carrier is the complex Hilbert space
`H = l2(N_{>=1})`, with its usual counting-measure orthonormal basis. The
operators and tensor factorization are specified below. Parameters `g,t` are
real and Gibbs statements require real `beta>1`. Source labels mean these
mathematical objects, not authenticated physical preparations.

**Dependency closed.** Authentic arithmetic successor → bounded interaction →
stable thermal domain and operational internal-prime entanglement. The next
edge, correlation data → separately constructed and reconstructible geometry,
remains open and is not inserted by terminology.

`observational_succ/unit_prime_succ.py`, originating at commit
`53c53e91bd1b46071d6437fed0e68c9b337892a0`, already supplies the affine braid,
logarithmic Hamiltonian and convergence scope. `quantum_records.py` supplies
exact real-qubit instruments; `entropy_transport.py` concerns classical laws.
The new modules extend these interfaces without changing archival imports.
`provenance/IMPORT_MANIFEST.json` was inspected: its 72 originating imports
come from FuckingRH `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; the new files
are not edits to those preserved originals.

**Classical dependencies and novelty boundary.** Self-adjoint bounded
perturbations, the compact spectral theorem and min–max are standard spectral
theory. Their hypotheses were checked against Gerald Teschl's author-hosted
*Mathematical Methods in Quantum Mechanics*, online 2009 edition, §§4.3,6.1–6.2,
Theorems 4.10,6.4,6.6: [actual full text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The present proofs specialize these tools to the specified arithmetic Jacobi
operator. Linear entropy as an entanglement diagnostic for pure bipartite
states is classical; see Zanardi–Zalka–Faoro, Eqs. (1)–(2),
[actual paper](https://arxiv.org/pdf/quant-ph/0005031).
The explicit minor/time-window estimates below are derived here; no claim
of first discovery is made.

## 1. The self-adjoint arithmetic interaction

Let `S e_n=e_(n+1)`; then `S*e_1=0`, `S*e_n=e_(n-1)` for `n>=2`.
Thus `S*S=I` but `SS*=I-|1><1|`. It is an isometry, not a unitary.
Define

\[
 H_0e_n=(\log n)e_n,\qquad
 D(H_0)=\{x:\sum_{n\ge1}(\log n)^2|x_n|^2<\infty\},
 \qquad A=S+S^*,\qquad H_g=H_0+gA.
\]

**Theorem B1 (CLASSICAL / PROVED PAPER specialization).** For every real `g`,
`H_g` is self-adjoint on exactly `D(H0)`, bounded below by `-2|g|`, and has
compact resolvent. Its eigenvalues, with multiplicity and in nondecreasing
order, satisfy

\[
 \log n-2|g|\le\lambda_n(H_g)\le\log n+2|g|\quad(n\ge1).
\tag{B1}
\]

**Proof.** The real diagonal operator `H0` is self-adjoint on the displayed
maximal square-summability domain: testing its adjoint on each basis vector
forces the same diagonal action and domain. The bounded operator `A` is
self-adjoint and has norm exactly 2. The upper bound is the triangle
inequality; for `x_N=N^(-1/2)sum_(n=1)^N e_n`,
`<x_N,A x_N>=2(N-1)/N`, proving the lower norm bound.
For a densely defined operator `T` and bounded `B`, the adjoint definition
gives `D((T+B)*)=D(T*)` and `(T+B)*=T*+B*`. Applying this with `T=H0`,
`B=gA` proves self-adjointness without a relative-bound ambiguity.

For `R>2|g|`, set `R0=(H0-iR)^(-1)`. Its diagonal entries tend to zero, so
its finite-rank diagonal truncations converge in norm: it is compact.
Since `||gA R0||<=2|g|/R<1`,

\[
 (H_g-iR)^{-1}=R_0(I+gAR_0)^{-1}
\]

exists and is compact. The quadratic bound
`<x,H0 x>-2|g| ||x||² <= <x,Hg x> <= <x,H0 x>+2|g| ||x||²`
holds on the common domain, and `H0>=0`. Compact resolvent and a lower
bound give a discrete eigenbasis with eigenvalues tending to infinity.

For completeness, the relevant min–max formula is
`lambda_n(T)=inf_(dim L=n,L subset D(T)) sup_(x in L,||x||=1)<x,Tx>`.
Its lower inequality follows because any `n`-dimensional `L` contains a
nonzero vector orthogonal to the first `n-1` eigenvectors; its upper
inequality uses the span of the first `n` eigenvectors. Substituting the
quadratic comparison into this formula and using `lambda_n(H0)=log n`
proves (B1). This argument does **not** exponentiate an operator-order
inequality. ∎

**Corollary B2 (CLASSICAL / PROVED PAPER specialization).** The positive
operator `exp(-beta Hg)` is trace class exactly when `beta>1`, and then

\[
 e^{-2\beta|g|}\zeta(\beta)\le
 Z_g(\beta)=\sum_{n\ge1}e^{-\beta\lambda_n(H_g)}
 \le e^{2\beta|g|}\zeta(\beta).
\tag{B2}
\]

**Proof.** For `beta>0`, exponentiate the *scalar eigenvalue inequalities*
in (B1), sum the nonnegative terms, and apply the elementary p-series
criterion. For `0<beta<=1` the lower comparison diverges, so the positive
trace is infinite. At `beta=0`, the identity has infinite trace. For
`beta<0`, the exponential is unbounded as the eigenvalues tend to infinity;
it cannot be a trace-class density. No analytic continuation supplies a
positive normalized Gibbs state at the forbidden temperatures. ∎

**Further exact consequences.** Finite-support sequences form a graph core
for `H0` by weighted-tail convergence, and hence for `Hg` by boundedness
of `gA`. The unitary `J e_n=(-1)^n e_n` obeys `JHgJ=H_(-g)`, so the spectra
and partition functions are even in `g`. For `g!=0` each eigenspace is
one-dimensional: the recurrence at `n=1` determines `x2` from `x1`, and
each subsequent equation determines `x_(n+1)`; if `x1=0`, all entries vanish.
These statements are ordinary Jacobi-operator facts in this specialization.

## 2. Interacting thermofield double and its exact type

Write `bar(H)` for the conjugate Hilbert space. For an orthonormal eigenbasis
`u_j` of `Hg`, define

\[
 |\Omega_{\beta,g}\rangle
 =Z_g(\beta)^{-1/2}\sum_j e^{-\beta\lambda_j/2}
 |u_j\rangle\otimes|\bar u_j\rangle
 \in\mathcal H\otimes\overline{\mathcal H},\qquad \beta>1.
\tag{B3}
\]

This converges in Hilbert norm by B2, is normalized, and has reduced left
density `rho_g=exp(-beta Hg)/Zg` and conjugate right density `bar(rho_g)`.
These follow by orthonormality and finite-sum partial traces followed by
trace-norm convergence of the positive tails. Each eigenweight is positive,
so both reductions are faithful. In the Hilbert–Schmidt vectorization
identification, B3 is `vec(sqrt(rho_g))`. Consequently it is independent
of eigenvector phases and of orthonormal changes inside a degenerate
eigenspace; omitting the right conjugation would lose this invariance.

The eigenvalue comparison gives
`sum |lambda_j| exp(-beta lambda_j)<infinity` for `beta>1`, since a constant
multiple of `(1+log j)j^(-beta)` dominates the tail. Differentiation of
`Zg` on any compact interval inside `(1,infinity)` is therefore justified,
and

\[
 S(\rho_g)=\log Z_g-\beta\partial_\beta\log Z_g<\infty.
\tag{B4}
\]

This is **left/right** thermofield entanglement. It is a different partition
from the prime factorization *within* either side. `Hg` is the explicitly
chosen deformation here; it is not asserted to be the original
Bost–Connes time evolution.

## 3. Exact successor entanglement and the subsystem countercontrol

For a fixed genuine prime `p`, unique factorization gives a unitary

\[
 F_p:\mathcal H\longrightarrow
 \ell^2(\mathbb N_0)\otimes\ell^2(\{m\ge1:p\nmid m\}),
 \qquad e_n\mapsto e_{v_p(n)}\otimes e_{n/p^{v_p(n)}}.
\]

`Vp` acts as the unilateral shift on the first factor and identity on the
second. If `q!=p` is prime, `Vq` acts only on the second factor. These are
local isometries. For `p=2`, however,

\[
 \psi_0=(e_1+e_2)/\sqrt2
 =((e_0+e_1)/\sqrt2)\otimes e_1,
 \quad S\psi_0=(e_2+e_3)/\sqrt2
 =(e_1\otimes e_1+e_0\otimes e_3)/\sqrt2.
\tag{B5}
\]

The first reduced density has purity 1; the latter is
`diag(1/2,1/2)` and has entropy `log 2` and purity `1/2`.
In the ordered basis `(0,1),(0,3),(1,1),(1,3)`, the partial transpose of
the latter density is

\[
 \frac12\begin{pmatrix}0&0&0&1\\0&1&0&0\\0&0&1&0\\1&0&0&0\end{pmatrix},
\]

with spectrum `(-1/2,1/2,1/2,1/2)`. The eigenvectors are respectively
`(1,0,0,-1)`, `(1,0,0,1)`, `(0,1,0,0)`, `(0,0,1,0)`.
These are exact rational density and eigenpair checks, independent of an
eigensolver. Removing the off-diagonal coherence instead gives the separable
mixture of the two product basis states; its partial transpose is itself
and its purity is `1/2`. Identical marginal entropy does not certify
mixed-state entanglement.

**CRT countercontrol (PROVED LOCAL).** On the distinct finite carrier
`l2(Z/6)`, CRT gives `e_x -> e_(x mod 2) tensor e_(x mod 3)`.
The same ray on labels 1 and 2 now has two orthogonal coordinates on
each factor and is entangled. Cyclic successor `T e_x=e_(x+1 mod6)`
is `T2 tensor T3`, a local product unitary. Multiplication by 2 is a
coordinatewise map but is not an isometry: it identifies residues 0 and 3.
Prime-valuation locality and CRT locality are different questions on
different carriers. Even on CRT, `exp(it(T+T*))` need not be a local
product merely because `T` is one; its generator is a sum of products.

## 4. A quantitative entangling unitary theorem

The preceding use of `S` is a legitimate isometry witness, not unitary
physical time evolution. Here is a genuine unitary replacement.

For a normalized pure vector with arithmetic amplitudes `a_n`, the two-by-two
coefficient minor in rows `v2=0,1` and columns `odd=1,3` is

\[
 D=a_1a_6-a_2a_3.
\]

Any product vector has every such minor zero. More quantitatively, for
coefficient matrix `C`, Cauchy–Binet (first on finite rectangles, then
by Hilbert–Schmidt convergence) gives

\[
 1-\operatorname{tr}((CC^*)^2)
 =2\sum_{i<j,k<l}|C_{ik}C_{jl}-C_{il}C_{jk}|^2\ge2|D|^2.
\tag{B6}
\]

All sums here converge: `C` is Hilbert–Schmidt with norm 1, the finite
truncations converge in that norm, and their reduced matrices converge
in trace norm. Thus the finite identity passes to the countable factors.

**Theorem B3 (PROVED PAPER, explicit quantitative local theorem).** For
`psi(t)=exp(itA)psi0`, where `psi0` is from B5, and every real `t`,

\[
 |D(t)|\ge |t|/2-16t^2,
 \qquad
 1-\operatorname{tr}(\rho_{v_2}(t)^2)
 \ge2\max\{0,|t|/2-16t^2\}^2.
\tag{B7}
\]

In particular this is an entangled state for every `0<|t|<1/32`.

**Proof.** Since `A` is bounded self-adjoint, its exponential is a unitary
norm-convergent power series. Directly `D(0)=0` and `D'(0)=-i/2`:
`a3'(0)=i/sqrt2`, `a6'(0)=0`, and `a2(0)=1/sqrt2`.
Every amplitude has bounds `|a_n|<=1`, `|a_n'|<=2`, `|a_n''|<=4`.
Twice differentiating the two products in `D` gives `|D''|<=32`.
Taylor's integral remainder gives `|D(t)+it/2|<=16t²` for either sign
of `t`; reverse triangle inequality and B6 prove the claim. ∎

**Theorem B4 (PROVED PAPER, interacting counterpart).** For
`psi_g(t)=exp(itHg)psi0`, put `a=|g|` and `C(a)=13a²+12a+3`. Then

\[
 |D_g(t)|\ge a|t|/2-C(a)t^2,
 \qquad
 1-\operatorname{tr}(\rho_{v_2,g}(t)^2)
 \ge2\max\{0,a|t|/2-C(a)t^2\}^2.
\tag{B8}
\]

For `g!=0` this proves entanglement for
`0<|t|<a/(2C(a))`. At `g=0` the state stays a product at all times.

**Proof.** The finite vector `psi0` is in `D(Hg²)`; thus the first two
strong time derivatives exist with norms
`M1=||Hg psi0||`, `M2=||Hg² psi0||`, invariant under time evolution.
The same product differentiation gives `|Dg''|<=4M2+4M1²` and
`Dg'(0)=-ig/2`. Writing `l2=log2,l3=log3` gives the exact coefficient lists

\[
 \sqrt2H_g\psi_0=(g,\ g+l_2,\ g),
\]
\[
 \sqrt2H_g^2\psi_0=
 (g(g+l_2),\ 2g^2+gl_2+l_2^2,\ g^2+g(l_2+l_3),\ g^2).
\]

The elementary bounds `0<log2<1`, `0<log3<2` imply
`M1²<=(3a²+2a+1)/2` and `M2<=5a²+5a+1` (use the coefficient l1
bound for the second norm). Therefore the Taylor remainder is at most
`(2M2+2M1²)t²<=C(a)t²`. B6 proves B8. At `g=0`,
`H0=(log2)Nv2 tensor I+I tensor log(Modd)`, so the evolution is a
product of local unitaries, explicitly preserving the initial product. ∎

These are conservative bounds, not claims of optimal entanglement rates.
For example `g=1,t=1/128` gives exact minor lower bound `9/4096` and
linear-entropy lower bound `81/8388608`. For `A` alone at `t=1/64`,
the corresponding bounds are `1/256` and `1/32768`.

## 5. Genuine Gibbs correlations for every nonzero coupling

**Theorem B5 (PROVED PAPER).** For every real `g!=0` and `beta>1`, the
Gibbs density `rho_g` is **not** a tensor product under `F2`. This proves
internal correlation. It does not prove that this mixed state is entangled.

**Proof.** Suppose `rho_g=rho_2 tensor rho_odd` with normalized density
operators. Faithfulness of `rho_g` implies that both factors are faithful.
Their eigenvalues are in `(0,1]`, so `K2=-log rho2` and `Ko=-log rhoodd`
are nonnegative self-adjoint operators. Spectral calculus on the product
eigenbasis gives

\[
 -\log\rho_g=K_2\otimes I+I\otimes K_o
 =\beta H_g+(\log Z_g)I.
\]

There is no hidden cancellation of domains: for spectral variables
`x,y>=0`, `x²,y²<=(x+y)²`. Hence the domain of the displayed sum is
contained in each summand's domain. Every arithmetic basis vector belongs
to `D(Hg)=D(-logrho_g)`, so in particular the required tensor basis
vectors lie in both local domains.

The matrix element between `e2=e1 tensor e1` and `e3=e0 tensor e3`
vanishes for both local summands, because their unchanged factors are
orthogonal. The same matrix element of `beta Hg+(logZg)I` is `beta g`,
which is nonzero. Contradiction. ∎

This is a sharper correlation statement than a floating finite marginal
defect. It supplies no conclusion about separability of `rho_g`; the
unitary pure-state entanglement theorem is the separate B4.

## 6. Truncation, numerical oracles, and counterfeit correlations

Let `PN` project onto labels `1,...,N`, and `Hg,N=PN Hg PN` on that
finite-dimensional space. Its eigenvalues obey the same B1 bounds for
`1<=j<=N`. The min–max principle also gives
`lambda_j(Hg,N)>=lambda_j(Hg)`, decreasing with `N`. The finite-support
graph core proves convergence for each fixed `j`: approximate a basis
of the first `j` eigenspace in graph norm by finite supports and apply
min–max to their spans. It follows that, for `beta>1`,
`Tr exp(-beta Hg,N)` increases to `Zg(beta)`; use pointwise eigenvalue
convergence, positivity and finite partial sums. A floating eigensolver
output is still not a certified lower enclosure without a rounding bound.

For `A` alone, if `psi` is normalized and supported on `1,...,M` and
`N>=M`, define `d=N-M+1`. The full and compressed powers on `psi` agree
through order `d-1` by nearest-neighbor path support. Extending `AN` as
zero on the orthogonal complement, the exponential-series comparison gives

\[
 \|e^{itA}\psi-e^{itA_N}\psi\|
 \le2\sum_{k\ge d}\frac{(2|t|)^k}{k!}
 \le\frac{2e^{2|t|}(2|t|)^d}{d!}.
\tag{B9}
\]

This is a genuine analytic truncation bound, not an observed stability
plateau. The factor 2 bounds the difference of two powers separately.
No identical bound is asserted for `Hg`, which is unbounded.

**Prefix-cutoff obstruction (PROVED LOCAL).** A finite integer-prefix Gibbs
state at `g=0` already has internal classical prime correlations for every
`N>=3`. Its positive diagonal support is not a Cartesian rectangle under
`F2`: let `m` be the largest odd number at most `N`. The marginals have
positive weights at `v2=1` (label 2) and odd part `m` (label `m`), but
the product label `2m>N` has zero weight. Thus it cannot be a product.
An infinite free state is a product; conditioning it on a nonrectangular
cutoff has created this artifact. A prime-exponent rectangle, such as
labels `{1,2,3,6}`, is the correct exact product control.

The numerical oracle returns an explicit flag for this issue. It forms
`rho` by diagonalization and independently by `scipy.linalg.expm`, uses
the conjugated eigenbasis TFD, and verifies its reduction. Its finite
product defect is never promoted to a proof of an infinite correlation
or mixed-state entanglement.

## 7. Calibration, receipts, and remaining obligations

The two owned modules and their matching test modules provide:

| Probe | Positive control | Negative/null/mutation control |
|---|---|---|
| Prime factors | `n=p^k*m`, `Vp:(k,m)->(k+1,m)` | Composite 6 and malformed basis inputs rejected |
| Pure entanglement | Exact B5 reduced densities and four PT eigenpairs | Dephased mixture, wrong PT eigenvalue, product prime rectangle |
| Factorization | Same initial ray is prime-product and CRT-entangled | CRT cyclic successor is local; finite nonunit dilation loses injectivity |
| Unitary theorem | Exact half-line walk series has `D'(0)=-i/2` | `g=0`, zero time, wrong coefficient sign, finite boundary leakage |
| Thermal oracle | Actual eigenbasis/conjugate TFD and independent matrix exponential | `beta<=1` is finite only at a cutoff; nonrectangular free cutoff is correlated |
| Input/calibration | Fractions and finite valid parameters | Float in exact controls, bools, zero ray, colliding coordinate maps rejected |

Locally executed command:

```sh
python -m unittest tests.test_arithmetic_entanglement tests.test_interacting_arithmetic_hamiltonian -v
```

**Observed result:** 17 tests passed, including 27 finite thermal parameter
combinations `N in {6,12,24}`, `g in {-1,0,0.4}`,
`beta in {0.5,1,2}`. The tests retain numerical tolerance and status labels;
they do not certify infinite statements. Exact prime factor checks cover
`p in {2,3,5,7}`, `1<=n<=80`; cutoff leakage controls use `N in {2,4,7}`;
Taylor coefficients through order 8 are compared with an independent
finite-matrix power implementation whose boundary is out of reach at that
order. The repository-wide receipt records the integrated validation SHA.

**Refuted inferences with receipts:** unilateral `S` is unitary (its
range omits `e1`); correlations require interaction (the free prefix
counterexample); marginal entropy alone certifies mixed-state entanglement
(dephased B5); entanglement is independent of factorization (CRT example).

**Open obligations / next verdict-changing probes.** Determine the
separability or entanglement of the infinite thermal `rho_g` under `F2`,
with actual trace-norm bounds transferring any finite witness. Find
optimal rates or propagation estimates in a declared prime-interaction
metric. Prove an intertwiner to a separately supplied code or geometric
bulk if such an interface exists. B1–B9 provide no Einstein equations,
wormhole, adelic gluing, Weil positivity or RH statement. The thermal
threshold stability is a classical bounded-perturbation consequence;
the connected geometric interpretation still owes its own theorem.
