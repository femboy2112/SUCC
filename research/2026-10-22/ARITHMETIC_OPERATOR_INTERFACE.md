# Concrete arithmetic operator algebra and finite-source interface

**Scope/status:** CLASSICAL / paper proofs and PROVED LOCAL exact oracle.
This extends the finite source-indexed transfer in PR #153, not its frozen
source files. It constructs a concrete norm-closed system. It does not claim
to prove the faithfulness of its representation of the abstract Bost–Connes
Hecke completion or the classification of all its KMS states.

## 1. Baseline and provenance

`main@b116841f12b41aaf7600da39bbb40577f25b6295` contains
`affine_pontryagin_transfer.py`, originating at `6febdec`, with later changes
at `c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d` (PR #153). Its `rho_m` acts
on the rational group algebra Q[Q/Z], its `sigma_m` is character pullback,
and its source-ID/epoch check prevents combining mismatched declarations.
That is exact finite algebra, not a physical-source authentication test.
The Hilbert construction from PR #136 (`53c53e91bd1b46071d6437fed0e68c9b337892a0`)
was included through Academic Main II, despite the individual PR being closed
without a direct merge. The Git ancestry and PR discussion establish this.

Primary source read: Bost–Connes, *Hecke algebras, type III factors and phase
transitions with spontaneous symmetry breaking in number theory*, 1995,
[original IHES manuscript](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf),
§2 Propositions 7–8, §4 Propositions 18–19, §5–6. In particular Proposition
18 lists the algebraic relations below; Proposition 19 supplies a separate
completion theorem. Importing the latter is not the same as proving that a
particular representation is faithful. No novelty claim is made for these laws.

## 2. Hilbert realization, exact relations

Let H=ℓ²(N≥1), with orthonormal basis e_n. For m≥1 and r∈Q/Z set
V_m e_n=e_mn and E(r)e_n=exp(2πinr)e_n. Both operators are bounded;
V_m is an isometry, E(r) a unitary. The adjoint is
V_m*e_n=1_(m|n)e_(n/m). On all of H:

* V_m*V_m=I, V_m V_n=V_mn, E(r)E(s)=E(r+s), E(r)*=E(−r).
* E(r)V_m=V_m E(mr), and V_m* E(r)V_m=E(mr).
* For d=gcd(m,n), V_m*V_n=V_(n/d)V_(m/d)*.
* V_m E(r)V_m*=(1/m)Σ_(j=0)^(m−1) E((r+j)/m).
* P_m=V_mV_m*=(1/m)Σ_j E(j/m) is the projection onto m-divisible integers.

**Proof.** Apply each side to every e_k. For the root average the scalar is
exp(2πikr/m)(1/m)Σ_j exp(2πikj/m), which vanishes unless m|k, and otherwise
equals exp(2πi(k/m)r). For the mixed adjoints, m|nk iff m/d|k; both nonzero
outputs have index nk/m. Equal bounded operators on an orthonormal basis
agree everywhere. Composite m is valid in this semigroup; calling m=6 an
independent prime mode is a different, false source claim.

The representation of C[Q/Z] is injective: a finite sum uses one common
denominator D; if it vanishes at every positive n, evaluating n=1,…,D and
finite Fourier inversion makes every coefficient zero. It extends faithfully
on its commutative C*-completion C(Zhat), since positive integers are dense
in Zhat by the residue-cylinder definition. This does **not** by itself
establish faithfulness on the full semigroup/Hecke algebra.

## 3. A genuine concrete C*-dynamical system

Define A_ar=C*(E(r),V_m:r∈Q/Z,m≥1)⊂B(H), with its concrete operator norm.
Let H0e_n=(log n)e_n on D(H0)={x:Σ(log n)²|x_n|²<∞}.
Then α_t(X)=e^(itH0)Xe^(−itH0) preserves A_ar and
α_t(E(r))=E(r), α_t(V_m)=m^(it)V_m.

**Proof of point-norm continuity.** Each finite word in these generators and
their adjoints is an eigenoperator with frequency log(a/b). Thus its orbit
is norm-continuous and extends to an entire function. Finite linear sums of
words are norm-dense in A_ar. For any approximation Y to X, the isometric
automorphism gives ||α_t(X)−X||≤2||X−Y||+||α_t(Y)−Y||. This proves continuity
and invariance, including α_(−t). It is a C*-dynamical system, not only a
strongly continuous Hilbert-unitary group.

For β>1 let ρβ=ζ(β)^−1 exp(−βH0). Then φβ(X)=Tr(ρβX) is faithful and is
a β-KMS state on this concrete system. For an eigenword α_t(A)=e^(itω)A,
ρβ A=e^(−βω) Aρβ, and trace cyclicity yields
φβ(AB)=e^(−βω)φβ(BA)=φβ(Bα_(iβ)(A)). This extends by linearity on the dense
entire word algebra. More explicitly F_(X,Y)(z)=φβ(Xα_z(Y)) is analytic
and bounded on 0≤Im z≤β for finite sums; its boundary values satisfy
F(t)=φβ(Xα_t(Y)) and F(t+iβ)=φβ(α_t(Y)X). Approximating arbitrary X,Y
in norm, both boundaries converge uniformly, and the three-lines bound
gives uniform convergence on the whole strip. The limit supplies the KMS
strip condition. Faithfulness follows from
φβ(X*X)=Σ_n n^(−β)||Xe_n||²/ζ(β), whose positive weights force X=0 if
the expression vanishes. Neither existence nor faithfulness implies a
classification of all KMS states.

**Hostile control.** On all B(H), this dynamics is generally not point-norm
continuous. Take the isometry Te_n=e_(n²). Then
||α_t(T)−T||=sup_n|n^(it)−1|=2 for every t≠0: choose integers nearest to
exp((2k+1)π/|t|), so their logarithmic phases tend to odd multiples of π.
Thus the choice of observable algebra is load-bearing. Normal modular
theory on B(H) has a different continuity convention.

## 4. Source-preserving finite oracle

`arithmetic_operator_interface.py` imports the existing source-typed
`RationalCharacterAlgebra` and independently evaluates its finite transfer
at integer basis states. It constructs Φ_D by exact division of x^D−1 by
the proper-divisor cyclotomic factors and reduces phase polynomials modulo
Φ_D. Comparing formal phase lists would be wrong: ζ3+ζ3²=−1 despite the
different supports. The oracle checks the old root average against the
direct Hilbert action. Conductor ≤1024 is an execution budget, not a theorem
restriction. Exact phase orientation mutations and composite semigroup
controls are retained. No old imported code is edited.

## 5. Finite code obstruction and the weakest repair

Let J_K:C^(K+1)→ℓ²(N0) include prime valuations 0,…,K, and let
T_K=J_K* T J_K for the unilateral prime-mode shift T|k>=|k+1>.
For L>K, with J_(L←K) the coordinate inclusion,

    T_L J_(L←K) − J_(L←K) T_K = |K+1><K|.

This follows by checking k<K (both images k+1) and k=K (one image is zero).
The defect norm is exactly 1 at every strict refinement. There is no
operator-norm convergence to an exactly equivariant finite tower on this
interface. For the normalized geometric vector with q∈(0,1), however, its
squared defect is q^K/(1+q+…+q^K), which tends to zero. A state-dependent
approximation is available; a uniform operator assertion is refuted.

More strongly, V_p has no nonzero finite-dimensional invariant subspace.
Such a subspace would have an eigenvector over C. V_p is injective, excluding
eigenvalue zero; for λ≠0, the equation V_p x=λx first forces x_n=0 for
p∤n and then recursively for every n. This contradicts a nonzero eigenvector.
Consequently a finite exact arithmetic code can preserve a declared
compressed algebra, but cannot intertwine the full prime shift on a
nonzero finite-dimensional invariant source. The geometric code dossier
states its truncation explicitly.

## 6. Verdict and remaining debt

SURVIVES: the source-typed finite transfer has an independently checked
Hilbert interface; its concrete norm closure has a genuine dynamics and
faithful β>1 Gibbs KMS states. REFUTED: extrapolating compressed mirror
tests to an untruncated operator relation; full B(H) point-norm continuity;
uniformly equivariant finite prime-shift towers. UNVERIFIED here: faithfulness
of the abstract full BC representation, its full KMS classification, or
any correspondence from this dynamics to a gravitational bulk flow.
Next discriminator: intertwine these operators with a separately fixed
bulk dynamics, with a controlled state-dependent truncation defect, rather
than assigning the same name to two spectra.

## 7. Critical-temperature repair on the full concrete arithmetic algebra

The following extends the prime-only quasi-local limit in the foundations
dossier to this particular larger algebra. It does not extend it to arbitrary
B(H), where convergence need not hold for all bounded diagonal observables.

**Theorem OA-CRIT.** As β decreases to 1, the Gibbs states φβ converge weak-*
on A_ar to a state ψ satisfying

    ψ(V_m E(r)V_n*) = δ_(m,n) δ_(r,0) / m.

This is a 1-KMS state for α. Its restriction to C(Zhat) is Haar probability;
its restriction to C(Z_p) is p-adic Haar probability. It has no normal state
extension to B(ℓ²(N)) with these same expectations. This is a classical
Bost–Connes critical-state realization; the present argument reconstructs the
needed result directly on the specified concrete algebra without assuming
abstract representation faithfulness or invoking zeta analytic continuation.

**Proof.** The monomials M(m,r,n)=V_m E(r)V_n* span a dense *-subalgebra. In
fact the preceding relations give, for d=gcd(n,k),

    M(m,r,n) M(k,s,l)
      =M(mk/d, (k/d)r+(n/d)s, ln/d),

and the adjoint is M(n,−r,m). Their diagonal trace vanishes unless m=n, and
in that case

    φβ(M(m,r,m))=m^(−β) [Σ_(a≥1) a^(−β) exp(2πiar)]/ζ(β).

For r=0 the bracket equals 1. For nonzero r∈Q/Z, write r with denominator D.
The character has mean zero over every D-term block and its partial sums
have absolute value at most D. Summation by parts gives
|Σ_a a^(−β)exp(2πiar)|≤D for β≥1 (a bound 2D would also suffice): using
partial sums A_k, the sum is Σ_k A_k(k^(−β)−(k+1)^(−β)), with vanishing
end term. The differences are positive and sum to 1. The denominator
ζ(β) tends to infinity, so the bracket tends to zero. This proves the formula
on all monomials.

Every φβ has norm one. Approximate X∈A_ar in norm by a finite monomial sum;
the estimate |φβ(X−Y)|≤||X−Y|| makes the net Cauchy on X and defines a
unique continuous limit. Positivity and normalization pass to the limit.
For an eigenword A of frequency ω, the Gibbs KMS identity passes to the
limit because α_(iβ)(A)=e^(−βω)A converges in norm to α_i(A). The dense
entire-algebra strip argument of §3 then gives the 1-KMS condition.

On the diagonal algebra, ψ(E(r))=δ_(r,0), the Fourier characterization of
normalized Haar measure (or directly finite Fourier inversion on every
residue cylinder). In particular each cylinder mod D has mass 1/D. A
normal extension would assign nonnegative masses w_n to individual integer
basis states, summing to one. But its mass at n is at most the mass 1/D of
the cylinder n mod D for every D, hence w_n=0 for all n, a contradiction.
No analytic continuation has been used. ∎

This furnishes a positive **profinite boundary law** exactly at the failed
vacuum-vector threshold. Local arithmetic observables survive as Haar
averages while all individual integer masses escape. It supplies neither a
normal arithmetic TFD at β=1 nor a geometric bulk Hamiltonian. In particular,
the limiting state is not claimed to encode an Archimedean integer coordinate.

The independent exact oracle checks the monomial product on untruncated
basis vectors, 2,304 pairs of monomials for the critical KMS identity, and
compatibility with the pre-existing root-average/Haar API for m=1,…,8.
These finite calibrations support the implementation; the limiting argument
above, not those tests, proves OA-CRIT.
