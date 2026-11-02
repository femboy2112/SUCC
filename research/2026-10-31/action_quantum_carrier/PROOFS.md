# Carrier-relative action quantum and covariant unit-SUCC frames

**Research-only paper derivations, 2026-10-31.** Source: SUCC Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`, stacked draft PR #440 exact head `7833a238012bb8e70ff363a3bcf6d60354ecb795`. Do not modify original BBP source, literal `U_0=0`, or historical theorem contracts. Physical Planck's constant, real quantum mechanics, a relativistic energy law, π normality and RH are **not derived**. Classical inputs include finite Heisenberg/Weyl representation, finite Fourier uncertainty and symplectic covariance. New-to-SUCC specialization: explicit radix-16 *original BBP source/carry* coupling to these frame maps and a strong real/cofiber no-factor counterexample.

## AQC-01: Finite carrier action quantum is a Weyl *pairing*, not a universal scalar

Let A be a finite abelian group, `H_A=C[A]` with orthonormal basis `|x>`. For `a in A`, define `S_a|x>=|x+a>`. For a character `chi in A^`, define `C_chi|x>=chi(x)|x>`. For every `x`,

`C_chi S_a |x> = chi(x+a)|x+a> = chi(a) S_a C_chi|x>`.

Thus **exactly** `C_chi S_a = chi(a) S_a C_chi`. The carrier-relative phase datum is the bicharacter `omega_A(a,chi)=chi(a)`; choice of a primitive vector/character is additional frame data. For A=`Z/QZ` with `Q=16^r`, primitive `a=k=1` gives `omega=exp(2pi i/Q)`. Set `theta_r=2pi/16^r` as a **dimensionless effective phase mesh**. `theta_(r+1)=theta_r/16` under the stated refinement. No physical hbar, minimum length or quantum speedup is inferred. For a noncyclic A there may be NO primitive character of order |A| (see AQC-08).

A literal finite-dimensional `[X,P]=i hbar I` with nonzero hbar is impossible: `Tr [X,P]=0` while `Tr(i hbar I)=i hbar dim H`. The exponentiated Weyl identity is the correct finite statement. For the real circle R/Z, an **integer** SUCC `x->x+1` acts trivially on all integer characters `e(hx)`; the local finite clock phase does not automatically transfer to the real circle.

## AQC-02: Full 16-branch refinement, exact carry and Weyl covariance

Let `Q_r=16^r`, `H_r=C[Z/Q_rZ]`, and for digit `a=0,...,15` define the isometric map `J_(r,a):H_r->H_(r+1)` by

`J_(r,a)|x> = |16x+a>`, with `0<=x<Q_r`.

The supports are disjoint and cover the whole fine basis, giving `J_a^*J_b=delta_(a,b) I`, `sum_a J_a J_a^*=I` (domains/codomains are explicitly level-dependent). With `S_r|x>=|x+1 mod Q_r>`:

- `S_(r+1) J_(r,a) = J_(r,a+1)` for a<15;
- `S_(r+1) J_(r,15) = J_(r,0) S_r` (the exact carry seam);
- `S_(r+1)^16 J_(r,a) = J_(r,a) S_r` for every a.

Let `C_(r,k)|x>=exp(2pi ikx/Q_r)|x>`. Then

`C_(r+1,k)J_(r,a) = exp(2pi ika/Q_(r+1)) J_(r,a)C_(r,k)`.

The `16`-step fine translation has Weyl phase `exp(2pi ik*16/Q_(r+1))=exp(2pi ik/Q_r)`, matching one coarse translation. **Without** scale adjustment, the new primitive fine phase is 16 times smaller and the native fine clock is not the same observer. These are complete basis-wise proofs, no numerical approximation.

The same-level endomorphism `x->16x mod Q_r` has kernel of size 16 for every r>=1, so it is NOT an automorphism and cannot implement the full unit frame by conjugation. The full *level-changing and branch-complete* maps repair that loss. The finite direct-sum branch identities resemble a finite-level Cuntz decomposition; they are not asserted to be an `O_16` representation on one fixed Hilbert space.

## AQC-03: Original 4-pole BBP forcing has an exact 2-adic source/carry factorization

Keep the literal authentic signed expression, for integer n>=1:

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`.

The exact common rational form is

`r(n)=(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]`.

Every factor of the reduced (or unreduced combined) denominator is odd. Consequently every r(n), and every `U_n` obtained by `U_0=0`, `U_(n+1)=16U_n+r(n+1)`, lies in `Z_(2)` (rationals with odd denominator), hence has a well-defined residue modulo `Q_r=16^r` for every r.

Let `R_(n+1,r+1) = r(n+1) mod Q_(r+1)` (exact modular inversion of the odd denominator). Divide it into uniquely determined source digit/carry:

`a_(n+1,r) = R mod16 in {0,...,15}`,
`c_(n+1,r) = (R-a)/16 in {0,...,Q_r-1}`.

For `x_(n,r)=U_n mod Q_r`, the **actual original-source** recurrence is exactly

`U_(n+1) mod Q_(r+1) = 16(x_(n,r)+c_(n+1,r)) + a_(n+1,r) (mod Q_(r+1))`
`                           = J_(r,a)( S_r^c |x_(n,r)> )` (basis-address notation).

The local character therefore obeys the exact *source-attested* multiplier

`chi_(r+1,k)(U_(n+1)) = exp(2pi i k a/Q_(r+1)) chi_(r,k)(U_n+c)`.

Equivalently `chi_(r+1,k)(U_(n+1)) = chi_(r,k)(U_n) chi_(r+1,k)(r(n+1))` where the characters on Z_(2) mean exact reduction at the stated level. The source phase cocycle is seed-blind while the state initial condition remains `U_0=0`; this is **not** real-circle Weyl cancellation. As a receipt, `r(1)=47/15 mod256=225=16*14+1`, so its first fine source digit is 1, source carry 14. A separate exact rational implementation reconstructs many n/r independently.

## AQC-04: No finite 2-adic clock report can carry the real-circle character

For ANY r>=1, take `x=0`, `y=16^r/3` in the same honest `Z_(2)` source domain. Because `16^r` is a multiple of the local modulus and 3 is odd, `x` and `y` give identical reports modulo `Q_r`. Yet `16^r ≡1 (mod3)` means

`exp(2pi i x)=1`, `exp(2pi i y)=exp(2pi i/3)`, and their complex difference has modulus `sqrt(3)`.

Consequently **no** function of the local residue `Z/Q_rZ` can approximate the real character on *all* `Z_(2)` with uniform error less than `sqrt(3)/2` (triangle inequality). More strongly, the sequence `16^r/3 ->0` in the 16-adic/2-adic topology but its real-circle characters stay `exp(2pi i/3)`; **there is no continuous map** from the 2-adic completion agreeing with `x->exp(2pi ix)` on this rational source domain. This is a genuine proof of a SOURCE-MAP obstruction, not a claim that one cannot transfer the **complete exact rational source and Archimedean data** by a separately authenticated map.

The local unit Weyl phase can be nontrivial while real-circle *integer* successor has phase one. A mixed Archimedean/cofiber observable is unavoidable for π; local clock equidistribution is insufficient.

## AQC-05: Exact finite Fourier uncertainty, the operational minimum unit

For a nonzero function f on a finite abelian group A, normalize its Fourier transform by `1/sqrt(|A|)`. If `s=|supp f|` and `t=|supp fhat|`, Cauchy and Parseval give

`|fhat(chi)| <= sqrt(s/|A|) ||f||_2`, and
`||f||_2²=||fhat||_2² <= t*s/|A| * ||f||_2²`.

Hence **`s*t >= |A|`**. This is the classical finite uncertainty principle, a mathematically meaningful resolution/information floor *within A*. It does NOT imply a universal physical minimum length; enlarging/refining A alters the bound. Sharp examples: in Z16, `H={0,4,8,12}` has s=t=4; in (Z2)^2, a 2-element subgroup also gives s=t=2. Exact character zeros are certified symbolically with cyclotomic `Phi_(2^k)=X^(2^(k-1))+1`, not float root-of-unity equality.

## AQC-06: Position-momentum frame covariance is symplectic, not SR's mass shell

On the *real* phase plane with canonical one-form `lambda=p dx`, define translation `T_d(x,p)=(x+d,p)` and dilation `D_m(x,p)=(mx,p/m)`, m>0. Then `D_m T_d=T_(md)D_m` (on states), and

`D_m^* (p dx)=(p/m)*d(mx)=p dx`, therefore `D_m^*(dx wedge dp)=dx wedge dp`.

The matrix `diag(m,1/m)` has determinant one and preserves the standard symplectic form; `diag(m,1)` does not when m!=1. The function-level pullbacks reverse arrow order; SUCC's inherited Hausdorff moment identity `A B_m=B_m A^m` has precisely the pullback convention. This gives the correct reciprocal **momentum** scaling to accompany multiplicative SUCC, without deriving a physical Lorentz transformation.

The standard special-relativistic dispersion `E²=p² c² + m_0² c⁴` is an EXTRA metric/dynamics law. It is not the source of `V_m S=S^m V_m`; the latter is affine covariance. We can *choose* a discrete kinetic operator on H_r, `K_r=(2I-S_r-S_r^(-1))/delta_r²` where `delta_r=1/Q_r`; it is selfadjoint positive with eigenvalues `4 sin²(pi k/Q_r)/delta_r²`. At the fine level take the **coarse physical stride 16**, `K_(r+1)^[16]=(2I-S_(r+1)^16-S_(r+1)^(-16))/delta_r²`. Then

`K_(r+1)^[16] J_(r,a)=J_(r,a) K_r` for every a.

Every polynomial/spectral function of K has corresponding exact intertwinement on the branch subspace, so a *chosen* dispersion `H_r² = m_0² I + c² K_r` is frame-compatible under this rescaling. The naive native fine unit kinetic `(2-S_f-S_f^-1)/delta_(r+1)²` does NOT intertwine J. This is a finite *kinematic* energy analogue, not physical GR/SR or proof of a source-selected signed estimate.

## AQC-07: A Pisot carrier of four states without a primitive fourth-root phase

Let `L=Z[sqrt2]`, `beta=2+sqrt2`. Multiplication by beta has integral matrix `M=[[2,2],[1,2]]` in basis (1,sqrt2), determinant 2 and eigenvalues `2±sqrt2` with conjugate in (0,1); hence beta is a quadratic Pisot integer. Its digit quotient `L/beta L` has exactly 2 cosets, distinguished by the parity of the integer coefficient, with digits `{0,1}` and unique division algorithm `a+b sqrt2=beta w+d`.

**Stronger:** `beta²=2(3+2sqrt2)`, and `3+2sqrt2` is a unit of norm `3²-2*2²=1`. Thus `beta² L = 2 L`. The second-level quotient is therefore

`L / beta² L = L/2L ≅ (Z/2Z)^2`, order FOUR but exponent TWO.

All its character values are ±1. No character has order four; there is no primitive e^(2pi i/4) Weyl phase for that carrier even though it contains four states. This decisively kills the attempted universal scalar definition `theta=2pi/|A|` for arbitrary finite fields/carriers. The correct object is the *whole bicharacter pairing* A×A^->U(1) and exact source-relevant colors. It is a separate Pisot *model*, not a claimed exact BBP embedding.

## AQC-08: A NEW original-BBP symplectic action-cocycle realization

**Source-authenticated exact theorem.** For any *exact* original four-pole r(n) define one real canonical affine step on `(x,p)` by

`F_(n+1):(x,p) -> (16x+r(n+1), p/16)`.

Its Jacobian is `diag(16,1/16)` and `F^*(p dx) = (p/16)d(16x+r(n+1))=p dx` because r depends on the *time index n*, not the position x. It is therefore a canonical/symplectic transformation for each fixed n. Equivalently it has an exact type-2 generating function `G_(n+1)(x,p')=(16x+r(n+1))p'`: differentiating gives `p=16p'` and `x'=16x+r(n+1)`. This is Hamiltonian canonical-transform algebra, NOT the SR dispersion law or dynamical energy conservation.

Set the **actual BBP** initial frame `(x_0,p_0)=(0,1)` and let `A_n=x_n p_n`. Then induction yields `p_n=16^(-n)`, `x_n=U_n` and for every n>=0

`A_(n+1)-A_n = (16x_n+r(n+1))p_n/16 - x_n p_n = r(n+1)/16^(n+1)`.

Hence, with no approximation,

`A_n = sum_(j=1)^n r(j)/16^j = 16^(-n) U_n`, and
`lim_(n->infty) A_n = sum_(j>=1) r(j)/16^j = pi/16`.

The final equality is the **original BBP series identity**, imported and preserved. Since original `r(j)>0`, this cumulative dimensionless pairing is strictly increasing and bounded by pi/16. The position–momentum pairing encodes exactly the original finite-to-analytic BBP source accumulation. Its **source cocycle** is `p_(n+1) r(n+1)`: in one formula, the multiplicative expansion on x, reciprocal dilation on p and additive forcing are coherent. The same actual states are reconstructible from PR #440's unit-SUCC Pascal atoms:

`A_n = 16^(-n) sum_(k=0)^(n-1) (-1)^k C_(n,k) a_k`.

For an altered real initial x_0=s and p_0=1, the pairing becomes `A_n=s+sum_(j<=n) 16^(-j) r(j)`, selecting a *different* completed boundary. The coherent `q=1/5` counterseed corresponds to `s=1/5-pi/16`, and has the same **step cocycle** but different initial action. Thus this source-action construction faithfully accounts for seed dependence, while its positive increments alone **do not imply the signed Fourier cancellation** required for pi normality. `A_n` is a mathematical canonical coordinate pairing, not a measured physical action or a derived Planck constant.

## AQC-09: Verdict and π frontier

**Disclosed/classical within stated models:** Weyl/Heisenberg pairing, finite-dimension no-CCR trace, 16-branch exact isometries/carry, exact all-level BBP rational source inclusion and phase cocycle, no continuous 2-adic-to-real circle character, finite support uncertainty, symplectic frame covariance, kinetic intertwining, original BBP canonical action cocycle, Pisot noncyclic clock counterexample.

**Tested locally:** 31 distinct exact standard-library tests with independent source rational/Euclid, clock/branch, shifted kinetic and Pisot decomposition oracles. Software tests reproduce instances; analytic/combinatorial paper arguments supply universal quantifiers. **Not Lean-certified, not externally refereed.**

**OPEN:** a transport retaining both local character/carry and the *actual* real-circle phase sufficient to establish `S_N(h)=o(N)` for every fixed integer h!=0 on the original BBP zero-seeded orbit. All local source cocycles are compatible with nonnormal altered seeds; a phase/uncertainty/energy theorem without an original-source signed saving cannot establish π normality. Do not import the physical hbar or SR mass shell as axioms to assert it.

### External mathematical provenance (classical ingredients, not priority claims)

- Rutgers G. Moore group-theory lectures, finite clock and shift/Heisenberg pair: https://www.physics.rutgers.edu/~gmoore/618Spring2021/GTLect1-AbstractGroupTheory-2021.pdf
- Finite canonical commutation obstruction, Waterloo thesis: https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/c881d8b9-b97a-4666-b23c-5c0055cccdfd/content
- Dutkay, Haussermann, Jorgensen, *Atomic representations of Cuntz algebras*, JMAA 2015 (finite branches are analogous, not asserted to give an O16 action): https://www.sciencedirect.com/science/article/pii/S0022247X14006441
- SUCC `observational_succ/proto_succ_variable_unit.py`, `prime_clock_yoneda.py`, `operational_yoneda_descent.py`, PR #440 U7N and Main XVIII source-lag frontier. This work does not create a parallel category or overwrite that spine.
