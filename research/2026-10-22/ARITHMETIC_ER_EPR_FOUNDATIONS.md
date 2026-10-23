# Arithmetic thermofield foundations: proved type-I interface

Date: 2026-10-22. Baseline: `b116841f12b41aaf7600da39bbb40577f25b6295`.
Status: **CLASSICAL / PAPER PROVED**, with separate **PROVED LOCAL / EXACT FINITE**
controls in `arithmetic_tfd.py`. No Lean certification is claimed for analysis.
No novelty priority, gravitational solution, source-authentication measurement,
or Weil/RH positivity is claimed.

## Hole contract and inherited boundary

**Statement:** genuine integer prime multiplication determines a normalisable
bipartite Gibbs purification and an explicit modular system, while its prime
mirror equations reconstruct all amplitudes. Quantifiers: every real beta>1;
fixed number basis and fixed authenticated prime-indexed operators. Weakest
useful form: coefficient recurrence plus a summable Euler product. This closes
arithmetic source → quantum state → modular observable arrows; it does not close
modular system → gravitational geometry. Cheapest falsifiers: reverse the mirror
coefficient, change a_6, or discard cutoff leakage. Reference completion and
observed probe closure are load-bearing, not inferred from tests.

`unit_prime_succ.py` already supplies source-gated affine arithmetic, vacuum
Hilbert convergence and logarithmic commutators (PR #136, head
`53c53e91bd1b46071d6437fed0e68c9b337892a0`; PR closed without merging as a PR,
subsequent baseline contains its module). `affine_pontryagin_transfer.py` supplies
exact Q[Q/Z] root averages (PR #153, `c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d`).
`quantum_records.py` is a real two-state instrument model; `entropy_transport.py`
is classical source-relative information. Neither is a general entanglement
entropy oracle. This additive work leaves those implementations and frozen
provenance originals unchanged. Its prime validation reuses `unit_prime_succ`.

## A1. Domains, bounded operators and source relations

Let H=ell²(N_{>=1}) with basis e_n. Define S e_n=e_(n+1), V_m e_n=e_(mn)
for integer m>=1, and H0 e_n=(log n)e_n on

    D(H0)={x: sum_n (log n)^2 |x_n|² < infinity}.

The maximal real diagonal operator is self-adjoint: solving (H0±i)x=y gives
x_n=y_n/(log n±i), in D(H0), and the coordinate adjoint has the same domain.
Its resolvent is compact, since the diagonal entries tend to zero and their
finite-rank truncations converge in operator norm. S and V_m are norm-one
isometries, with S*e_1=0, S*e_n=e_(n-1) for n>1, and
V_m*e_n=1_(m divides n)e_(n/m). Thus S*S=V_m*V_m=I,
SS*=I-|1><1| and V_m V_m*=P_m, the multiples-of-m projection.

On basis vectors and hence all H, V_m S=S^m V_m and V_m V_k=V_(mk).
In general V_m S is not S V_m (n=1,m=2 gives e_4 versus e_3).
S,S*,V_m,V_m* preserve D(H0), by |log(n+1)-log n|<=log2 and
log(mn)=log m+log n. Consequently on D(H0)

    [H0,V_m]=(log m)V_m,
    [H0,S]e_n=log(1+1/n)e_(n+1).

The commutators extend boundedly; the second is compact, the first is
noncompact for m>1. Prime multiplication remains distinguished from an arbitrary
composite generator by unique factorisation, not merely these semigroup laws.

## A2. Normalisation, Schmidt data and faithfulness

For real beta, exp(-beta H0) is positive with diagonal n^-beta (unbounded if
beta<0). Its extended trace is sum n^-beta, finite exactly when beta>1 by the
integral test. For beta>1 define Z=zeta(beta), w_n=n^-beta/Z and

    Omega_beta = sum_n sqrt(w_n) e_n ⊗ e_n.

Orthogonality gives norm²=sum w_n=1 and norm convergence. Before normalisation,
the series lies in H⊗H exactly when beta>1. Analytic continuation at beta<=1
cannot supply a norm or a positive trace-class density for these coefficients.
All coefficients are positive, so this is a Schmidt decomposition. Taking finite
partial traces and then the trace-norm limit gives both reduced densities
rho_beta=Z^-1 exp(-beta H0). Every w_n>0, so kernel(rho_beta)=0: it is faithful,
although rho_beta^-1 is unbounded and no uniform lower spectral bound exists.
Indeed Tr(rho X*X)=0 implies X e_n=0 for each n, hence X=0.

Omega is cyclic and separating for B(H)⊗I. For cyclicity, each basis vector
|i,j> equals (|i><j|/sqrt(w_j) ⊗ I)Omega. For separatingness, XOmega=0
implies X e_n=0. This is a type-I standard representation/GNS realisation of
the faithful normal Gibbs state; it is not a type-III local QFT algebra.

## A3. Entropy, spectra, Rényi and fidelity

For every beta>1 the series sum (log n)n^-beta converges, uniformly on compact
beta intervals inside (1,infinity). Differentiating the series is justified and

    S(rho_beta)=log zeta(beta) - beta zeta'(beta)/zeta(beta).

The entanglement spectrum is {-log w_n=beta log n+log Z}. For alpha>0,
alpha!=1 and alpha beta>1,

    S_alpha(rho_beta)=[log zeta(alpha beta)-alpha log zeta(beta)]/(1-alpha).

If alpha beta<=1 the Rényi entropy is +infinity (this case has alpha<1).
S_infinity=log Z and the rank entropy S_0 is infinite. The pure bipartite
mutual information is I(L:R)=2S(rho_beta), finite for beta>1.

For beta,gamma>1 the pure-state fidelity (the squared-overlap convention) is

    F(Omega_beta,Omega_gamma)
      =zeta((beta+gamma)/2)^2/[zeta(beta)zeta(gamma)].

This is also the fidelity of the commuting reduced densities. All formulas
follow by their absolutely convergent defining sums, not analytic continuation.

Applying V_p to the left is a deterministic isometric channel. It preserves
Schmidt values and L:R entropy, leaves rho_R fixed, and changes rho_L to
V_p rho V_p*, which is no longer faithful on all H. Its overlap with the
unshifted Omega is zero: matching the right index forces matching n, whereas
pn=n is impossible. States (V_p⊗I)Omega and (V_q⊗I)Omega are orthogonal for
p!=q. Entropy equality therefore does not imply source-state identity.
Applying V_p* on the right is a trace-decreasing filter with success probability
p^-beta; its normalised selected vector equals (V_p⊗I)Omega. Filtering is not
a deterministic inverse channel.

A classical mixture sum w_n |n,n><n,n| has exactly the same reduced densities
but is separable. The pure Omega is entangled: on span{|m,n>,|n,m>}, m!=n,
its partial transpose has eigenvalues ±sqrt(w_m w_n), including a negative
one. This two-dimensional compression witnesses entanglement even when the
full infinite-dimensional partial transpose is not trace class (in particular,
its trace norm is finite only for beta>2). Local marginals alone do not
certify the coherence or its arithmetic phase.

## A4. Prime tensor product with its reference completion

Let H_p=ell²(N_0), reference vector |0>_p. The **incomplete tensor product**
H_vac=⊗_(p,|0>) H_p is the completion of finite-excitation elementary tensors.
The map U e_n=⊗_p |v_p(n)> is unitary: unique prime factorisation identifies
its orthonormal bases bijectively. U V_p U*=T_p⊗I, where T_p is the unilateral
shift of valuation k. On finite-excitation vectors UH0U*=sum_p(log p)N_p;
the maximal diagonal closures agree. S is not local in this factorisation.

For q_p=p^-beta define the normalised paired-prime vector

    omega_(p,beta)=sqrt(1-q_p) sum_(k>=0) q_p^(k/2)|k,k>.

Its finite-prime products, with |0,0> elsewhere, are Cauchy in the paired
vacuum completion iff product_p(1-q_p)>0, equivalently sum_p q_p<infinity
(for beta>0). For beta>1 this holds by comparison with sum_n n^-beta.
Their mutual overlap over F⊂G is product_(p in G\F)sqrt(1-q_p); the Cauchy
criterion proves the assertion. In the limit, the coefficient of |n,n> is
product_p sqrt(1-q_p) n^-beta/2. Monotone expansion of finite Euler products
and unique factorisation give product_p(1-q_p)^-1=zeta(beta). Therefore

    (U⊗U)Omega_beta = ⊗_p omega_(p,beta)

in this explicitly declared completion. The right side is not an arbitrary
unrestricted infinite tensor product.

The single-prime density is geometric, (1-q_p)sum_k q_p^k|k><k|. Its entropy
is -log(1-q_p)-q_p log(q_p)/(1-q_p). Summing these nonnegative terms gives
A3's entropy, by Tonelli and the convergent logarithmic Euler derivative.
Distinct prime pairs have zero mutual information; so do distinct prime
subsystems within one side. Entanglement between each p,L and p,R supplies
no inter-prime connectivity.

## A5. Explicit modular operator and topology

Identify the right space with the number-basis conjugate of H. On the algebraic
span of |i,j>, the closable Tomita map T0(X⊗I)Omega=(X*⊗I)Omega is

    T0 |i,j> = sqrt(w_i/w_j)|j,i>  (antilinearly).

Its closure is the antilinear weighted swap on its maximal square-summability
domain; finite-support vectors are a graph core by coordinate truncation.
Its polar decomposition T=J Delta^(1/2) is explicit:

    J(sum z_ij |i,j>)=sum conjugate(z_ij)|j,i>,
    Delta |i,j>=(w_i/w_j)|i,j>=(j/i)^beta |i,j>.

Delta is generally unbounded, with maximal domain
sum_(i,j)(w_i/w_j)^2 |z_ij|²<infinity. Direct calculation gives
J(B(H)⊗I)J=I⊗B(conjugate H) and

    Delta^(it)(X⊗I)Delta^(-it)
        =(rho^(it) X rho^(-it))⊗I,
    sigma_t(X)=exp(-it beta H0)X exp(it beta H0)=alpha_(-beta t)(X),
    alpha_t(X)=exp(it H0)X exp(-it H0).

These formulas are obtained here by weighted-coordinate closure, not by
assuming an unspecified modular-geometric theorem. On arbitrary B(H), alpha
is a W*-dynamics, not a point-norm continuous C*-dynamics. Counterexample:
T e_n=e_(n²) satisfies ||alpha_t(T)-T||=2 for every t!=0, since n may be chosen
arbitrarily close in relative error to exp((2k+1)pi/|t|). On the norm-continuous
subalgebra, including C*(E(r),V_m), it is point-norm continuous, as each
E(r) is fixed and each V_m gains the scalar m^(it).

## A6. Gibbs KMS identity, with its domain

With alpha_t as above, the normal Gibbs state satisfies the W*-KMS_beta strip
condition. A direct proof uses

    F_X,Y(z)=Z^-1 Tr(exp(-(beta+iz)H0) X exp(iz H0) Y),
             0<Im z<beta.

For z=t+is both heat exponents have positive real parts beta-s and s. Schatten
Hölder, with indices beta/(beta-s) and beta/s, bounds |F|<=||X||||Y|| uniformly.
Spectral truncation proves holomorphy, with convergence uniform on compact
interior strips; the trace-class tail and strong continuity prove the boundary
limits. At the lower boundary cyclicity gives F(t)=phi(X alpha_t(Y)); at the
upper, F(t+i beta)=phi(alpha_t(Y)X). Equivalently, finite matrix units give
phi(e_ij alpha_(i beta)(e_ji))=phi(e_ji e_ij). On them this is
exp(-beta(log j-log i))w_i=w_j. Finite-support matrix operators (finite linear combinations of number-basis
matrix units) are entire analytic; restrictions
to any invariant point-norm continuous C*-subalgebra give usual C*-KMS states.

For clarity, the normal state is unique among normal W*-KMS_beta states on
B(H): invariance kills off-diagonal matrix elements because log n is simple;
KMS matrix-unit equations force d_j=(j/i)^-beta d_i. Normalisation then
forces d_i=w_i, possible only at beta>1. This does not deny singular states or
KMS states in other representations/algebras at beta<=1.

## A7. Critical boundary: a positive limit in a different category

As beta decreases to 1, zeta(beta) diverges and each w_n tends to zero.
Omega_beta tends weakly to zero in H⊗H: all basis coefficients tend to zero,
and approximation by finite-support vectors proves weak convergence.
The normal states satisfy Tr(rho_beta K)→0 for every compact K, first for
finite-rank K and then by norm approximation. They cannot converge in trace
norm to a density matrix, since any normal limit would vanish on every rank-one
projection but must have trace one. On K(H)+CI the limit is the singular state
K+cI↦c. No nonzero normal vacuum Gibbs state appears at beta=1.

There is nevertheless an explicit **quasi-local prime-algebra** limit.
For each finite prime set F take its geometric product state at q_p=1/p.
These density matrices are normalised and compatible under partial trace.
Their product expectations define a positive norm-one functional on the union
of finite spatial tensor products, hence extend uniquely by continuity to its
norm closure. On each finite F the beta>1 restrictions converge in trace norm
(by dominated geometric summation), so the global states converge weak-* on
this quasi-local algebra. The same construction works for the paired-prime
pure local vectors omega_(p,1). It is not a vector in the original paired
vacuum completion: product_p(1-1/p)=0, since otherwise the finite Euler sums
would bound the divergent harmonic series. This gives a precise category
change at the threshold, not an analytic-continuation density matrix.

The preceding argument constructs compatibility and positivity itself. It
does **not** independently prove the von Neumann factor type or extend the
limit to an arbitrary larger observable algebra. Those are separate results.
For the specific concrete algebra C*(E(r),V_m), a separately proved extension
is [operator interface, section 7](ARITHMETIC_OPERATOR_INTERFACE.md#7-critical-temperature-repair-on-the-full-concrete-arithmetic-algebra): the critical limit is a 1-KMS state whose diagonal restriction is profinite Haar measure.

## A8. No signaling

For any trace-preserving local channel with Kraus operators K_a on L and any
bounded B on R,

    sum_a Tr[(K_a⊗I)rho(K_a*⊗I)(I⊗B)]
       =Tr[rho(sum_a K_a*K_a ⊗ B)]=Tr[rho(I⊗B)].

The finite Kraus proof is exact; countable Kraus families extend by normal
monotone convergence when sum K_a*K_a=I strongly. V_p alone is an isometry,
so it is such a channel. V_p* alone is not: its effect is P_p. Complete it by
I-P_p, and the outcome-forgotten channel preserves the other marginal. A
selected outcome requires a classical success flag. A mirror equality between
vectors supplies no communication channel.

## Provenance, novelty and validation boundary

Primary sources actually opened and inspected on 2026-10-22:

* J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase
  transitions with spontaneous symmetry breaking in number theory* (1995),
  [original 49-page IHES preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf),
  §2, Lemma 6 and Propositions 7–8, PDF pp7–11. These establish the arithmetic
  Fock/Toeplitz setting and prime product KMS states, including a nonnormal
  critical state. The prime gas and zeta partition function are classical.
* E. Witten, *Notes On Some Entanglement Properties Of Quantum Field Theory*,
  [arXiv:1803.04993v6](https://arxiv.org/pdf/1803.04993), §4.1, equations
  (4.24)–(4.31), and §4.2. This primary exposition confirms the type-I modular
  conventions. Our countable diagonal domain proof is given above; no QFT
  localization claim is imported.

* M. A. Rieffel and A. van Daele, *A bounded operator approach to
  Tomita–Takesaki theory*, Pacific Journal of Mathematics 69(1), 187–221 (1977),
  [original publisher PDF](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf),
  §§1–3 and §4 Theorems 4.2 and 4.10 inspected. Its cyclic/separating and
  faithful-normal hypotheses match A2; A5 independently computes the
  specialised modular operators instead of importing the full general theorem.

Historical TFD source contact: Takahashi–Umezawa's publisher reprint,
[doi:10.1142/S0217979296000817](https://www.worldscientific.com/doi/pdf/10.1142/S0217979296000817),
was located but its full text returned HTTP403 in this session. It is not
represented as read or used as an unchecked proof dependency; A2–A4 give
the needed purification and prime-factor proofs directly.

No source excerpt is copied. All displayed derivations are supplied here.
Next falsification targets: an explicit independently defined bulk intertwiner;
a nontrivial source-faithful embedding beyond an arbitrary isometry; refinement
compatibility of that embedding. Present results stop before those arrows.
