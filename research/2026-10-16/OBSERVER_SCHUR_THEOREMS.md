# The observer's Schur complement: energy, sign, and conditional envelope

Round II, observer lane, 2026-10-16. Base inspected:
`5d6d717312eebee648d3cfb092875eb4120bb4b3`, branch
`research/observers-schur-complement-2026-10-16`.
**Original Suzuki four-low sign: OPEN. RH PROVED: NO.**

The mathematical statements OS-01–OS-07 below are **PAPER_PROVED**, with their
exact hypotheses; OS-08 is their **PAPER_PROVED conditional application** to
the inherited source hypotheses. The separate implementation supplies
**EXACT_FINITE_CHECK** instances on declared rational matrices. This lane
does not execute Lean, claim an arithmetic sign, or import a numerical matrix
as the original source. No academic originality claim is made: these are
classical algebra/functional analysis and a new-to-SUCC observation interface.

## Source, authority, and attribution

The assigned lane owns only `observational_succ/observer_schur.py`, its test
and probe, this document, and `observer-schur*` receipts. No Git mutations,
archival rewrites, full-suite execution, or worker creation are performed.
`AGENTS.md`, `docs/METHOD.md`, the prior claim supplement, the Proof Teeth
overview, Hilbert/minimum-observation/gluing/capsule dossiers, prior audits,
import manifest and final receipts were inspected. Load-bearing code read:
`recursive_operator_gluing.py`, `source_field_inverse_limits.py`,
`four_low_schur_proof_teeth.py`, and `source_weil_hierarchy.py`.
The existing exact matrix kernel is reused; finite nullspace elimination and
congruence witnesses are added, without adding a competing arithmetic source.

The historical import manifest identifies FuckingRH commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. This is distinct from the later
Suzuki adapter blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178` at SUCC
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`. The new probe hashes inspected
files but does not re-prove their claims or authenticate the original source
from a string. The principal owns the full provenance replay and source-lane
certification. Previous failures/corrections remain in the inherited archives.

Classical attribution: [R. G. Douglas, *On majorization, factorization, and
range inclusion of operators on Hilbert space*, Theorem 1 (1966)](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)
equates bounded factorization, actual range inclusion, and an operator
majorization inequality. We give the needed variational argument explicitly.
[Anderson and Trapp, *Shorted Operators II* (1975)](https://epubs.siam.org/doi/10.1137/0128007) defines shorting for a **positive
whole operator**. Our whole operator is allowed to be signed. Its conditional
low envelope is derived below; positivity of the whole operator is a
conclusion equivalent to positivity of that envelope, not an imported premise.
The Douglas original paper and Anderson–Trapp publisher abstract were browsed
in this lane. No full-text theorem inaccessible behind the latter page is
silently used. The prior source dossier supplies the arithmetic provenance.

Throughout, real or complex Hilbert inner products are linear in the first
argument. Write `B_G(u,v)=<Gu,v>` and `Q_G(u)=<Gu,u>`. Rational finite models
use transpose, symmetric matrices and the Euclidean bilinear metric; the
identities extend to real coordinates. All operators in OS-02–OS-06 are
bounded and everywhere defined unless an inverse domain is explicitly given.

## OS-01 — the exact energy radical criterion

Let V be a vector space over R or C, B a Hermitian sesquilinear form (symmetric
bilinear over R), and O:V→W linear. No topology is needed for this statement.
Put Q(u)=B(u,u), and `rad(B)={z: B(z,u)=0 for every u}`. The following are
equivalent:

1. Q is constant on every fiber of O.
2. There is a unique function q on ran(O) with Q=q∘O.
3. ker(O)⊆rad(B).

The decoder q is itself the diagonal of the induced Hermitian form on ran(O).
This does not yet assert continuity for the subspace norm on ran(O).

**Proof.** (1)↔(2) is the coimage theorem: define q(Ou)=Q(u), with exactly
fiber constancy as the well-definedness condition. If z∈ker(O), constancy at
0,z gives Q(z)=0. Constancy at u,u+z and expansion give Re B(u,z)=0.
Over C repeat with iu to get Im B(u,z)=0. Thus z is radical. Conversely, if
all such z are radical, Q(u+z)=Q(u)+2Re B(u,z)+Q(z)=Q(u). The induced form
`b(Ou,Ov)=B(u,v)` is well-defined by radical annihilation of both entries.
For bounded self-adjoint G on H, rad(B_G)=ker(G), since <Gz,u>=0 for all u
forces Gz=0. For an orthogonal splitting H=L⊕M and observation P onto L,
exact energy factorization is therefore equivalent to **B=0 and D=0** in
`G=[[A,B],[B*,D]]`. ∎

**Mandatory mutant.** Let G=[[0,1],[1,0]], O(x,y)=x. Every hidden vector
(0,y) has zero quadratic energy, but Q(1,0)=0 and Q(1,1)=2. The kernel is
isotropic, not radical. For complex forms, omitting the iu polarization test
would likewise discard imaginary cross information. Positivity of the whole
form would make isotropic vectors radical, but it is absent here.

**Exact implementation.** Rational elimination computes a full basis of
ker(O), then tests Gz=0 for every basis vector. If Gz≠0 and Q(z)≠0, 0,z
are a witness pair. Otherwise choose i with (Gz)_i≠0; e_i,e_i+z have the same
observation and unequal energies. `decode_energy` solves Ou=y only after
the radical gate succeeds and rejects unreachable y. This is an exact
finite-dimensional algebraic certificate, not a grid of sampled vectors.

## OS-02 — complete low-only sign classification when D≥0

Let H=L⊕M and G=[[A,B],[B*,D]]=G*, with D≥0. Define
`s(x,h)=1_{Q_G(x+h)≥0}`. The zero threshold is included in the positive report.

- If D≠0, s factors through P **iff G≥0**. The decoder in that case is
  the constant 1.
- If D=0, s factors through P **iff B=0**. In that case its decoder is
  `1_{<Ax,x>≥0}`; A need not be positive.

Neither statement needs injectivity or a Schur range assumption.

**Proof for D≠0.** Positivity and nonzeroness give z∈M with <Dz,z>>0
(otherwise polarization makes D zero). In each fixed low fiber, the polynomial
`Q_G(x+tz)=<Ax,x>+2t Re<z,B*x>+t²<Dz,z>` has positive leading
coefficient. Hence each fiber contains a strictly positive-energy point.
If sign is constant on fibers, every point has nonnegative energy, so G≥0.
The converse is immediate. In particular, a negative direction anywhere
forces a negative and a positive direction in the same observed fiber.

**Proof for D=0.** If B=0 the formula depends only on x. If B≠0 choose x
with b=B*x≠0 and h=tb, t∈R. The energy is `<Ax,x>+2t||b||²`, which takes
both signs. Thus sign cannot factor. ∎

Here B maps M→L and B* maps L→M; the cross term is `2Re<h,B*x>`.

For a fixed fiber with D≠0, let m(x) be its extended-real infimum. That fiber
is all nonnegative iff m(x)≥0; if m(x)<0, including −∞, it has both strict
signs. When D=0 and B*x=0, the fiber is constant and can instead be all
negative. This edge case invalidates the unrestricted assertion that every
negative fiber also contains a positive point.

**Exact controls.** G=I₂ has sign factorization but not exact energy
factorization. G=diag(1,−1,0) with two observed coordinates has D=B=0 and
sign factorization although G is indefinite. G=[[1,2],[2,1]] has A,D>0,
S=−3, and opposite signs in a single fiber. The cross-term mutant gives
energies −1 and +1 at (1,−1/2),(1,1/2).

## OS-03 — finite envelope iff actual square-root range

Fix bounded D≥0 on M, b∈M, and a∈R. Set

    F(h)=a+2Re<h,b>+||D^(1/2)h||².

Then inf F is finite **iff b∈ran(D^(1/2))**. If this holds, let c be the
unique solution D^(1/2)c=b lying in M₀=(ker D)⊥. Then

    F(h)=a−||c||² + ||D^(1/2)h+c||²,
    inf_(h∈M) F(h)=a−||c||².                         (OS3)

If the range condition fails, inf F=−∞. Membership in the closure of the
range is not sufficient. No injectivity is required for the reduced solution.

**Proof of necessity, including the nonclosed-range case.** Suppose
`F(h)−a≥−C` for all h, where C≥0 since h=0 is allowed. If D^(1/2)h=0,
vary real multiples and complex phases of h to conclude <h,b>=0.
Otherwise minimize the scalar quadratic on t h after choosing its phase:
`|<h,b>|²≤C||D^(1/2)h||²`. Thus the rule
`ell(D^(1/2)h)=<h,b>` is a well-defined bounded linear functional on
ran(D^(1/2)). It uniquely extends to its closure M₀. The Hilbert Riesz
theorem supplies c∈M₀ with `ell(y)=<y,c>`. Consequently
`<h,b>=<D^(1/2)h,c>=<h,D^(1/2)c>` for every h, hence b=D^(1/2)c.
If the condition fails, the function is not bounded below, which is precisely
the assertion inf F=−∞.

**Sufficiency and exact infimum.** Substitute b=D^(1/2)c and expand the
square to obtain OS3. The closure of the range of a bounded self-adjoint
operator T is (ker T)⊥: the orthogonal complement of its range is ker T*.
Hence D^(1/2)M is dense in M₀ and approximates −c. The last square has
infimum zero. This argument does not assert that it equals zero at a vector. ∎

For the block form, put b=B*x and a=<Ax,x>. All low fibers have finite
envelopes iff `ran(B*)⊆ran(D^(1/2))`. The reduced map C:x↦c is linear and
bounded. Finite-dimensional L makes boundedness automatic; more generally
the closed graph theorem applies: x_n→x,Cx_n→c gives D^(1/2)c=B*x,
c∈M₀, hence c=Cx. This is also the Douglas reduced factorization.
Thus the source-defined bounded response R₀=C*C and signed short S₀=A−R₀
satisfy, for **all** x,h,

    Q_G(x+h)=<S₀x,x>+||D^(1/2)h+Cx||²,
    m(x)=inf_h Q_G(x+h)=<S₀x,x>.                    (OS4)

For injective D, C is denoted D^(-1/2)B*. The unbounded D^(-1/2) is only
applied to its established domain ran(D^(1/2)). It is not a bounded inverse
on M. The range gate and OS4 prove G≥0 iff S₀≥0. Without that gate,
positivity of an arbitrarily chosen finite pseudoinverse expression is not
a substitute. The map u↦m(Pu) always factors through P **by definition**
(possibly extended-real); the theorem gives its source-dependent quadratic
decoder, not a source-free algorithm for computing C.

## OS-04 — attainment, nonattainment, and singular countermodels

Under OS3's range condition, the infimum is attained iff **b∈ran(D)**.
The minimizing h solve Dh=−b; any two differ by ker D. For injective D
the minimizer, if present, is unique.

**Proof.** Attainment of OS3 means D^(1/2)h=−c, which implies Dh=−b.
Conversely, if Dh=−b then D^(1/2)(D^(1/2)h+c)=0. The expression in
parentheses lies in M₀, so it is zero. This proves the criterion and the
kernel ambiguity. In finite dimensions ran(D)=ran(D^(1/2)); therefore a
finite envelope is attained even when D is singular. ∎

**Compact nonattainment with rational constants.** Take M=ell²(N_{≥1}),
`D e_n=4^(-n)e_n`, `b_n=4^(-n)`, `A=1/3` on L=R, and `B*x=x b`. Then
`c_n=2^(-n)`, `||c||²=sum 4^(-n)=1/3`, so S₀=0 and G≥0. For x=1,
the would-be minimizer has every h_n=−1 and is not in ell². The finite
vectors h^(N)=−sum_(n≤N)e_n give

    Q_G(1+h^(N))=1/(3·4^N)>0, tending to zero.

Thus a perfectly well-defined envelope can fail to have a high-state
minimizer. D is strictly positive on nonzero vectors, compact, and has no
uniform positive L² gap. Changing A to 0 gives S₀=−1/3 and the same
nonattainment, with genuinely negative energies at finite N.

**Injective but infinite envelope.** Keep D, take `b_n=2^(-n)` and A=0.
b∈ell² and ker D=0, but the formal reduced c is the constant-one sequence,
outside ell². Set h_n=−2^n for n≤N and zero otherwise. Each h is in ell²
and has energy −N. Hence the envelope is −∞. The finite kernel test is
vacuous in this infinite injective model and cannot replace actual range.

**Finite singular control.** D=diag(1,0), B*=(0,1)^T, A=1 gives energy
`x²+h₁²+2x h₂`; every x≠0 fiber has infimum −∞. A matrix pseudoinverse
blindly gives B D† B*=0 and the apparently positive number 1, omitting
exactly the violated range obligation. Conversely D=diag(2,0), B*=(2,0)^T,
A=3 has S=1, minimizing h₁=−x and arbitrary h₂.

## OS-05 — contraction and the two parity problems

Assume OS3 for every x, and A is uniformly positive: A≥αI_L for α>0.
For finite-dimensional L this is exactly positive definiteness. Define
T=C A^(-1/2). It is bounded because C and A^(-1/2) are bounded. Then

    S₀=A^(1/2)(I−T*T)A^(1/2),
    S₀≥0  iff  T*T≤I  iff  ||T||≤1.                (OS5)

**Proof.** Substitute C*C=R₀ and multiply the factors. The invertible
congruence preserves the sign of every quadratic form. Finally
`<T*Tx,x>=||Tx||²`, which makes T*T≤I equivalent to the norm bound.
For infinite-dimensional A, pointwise strict positivity alone does not
supply bounded A^(-1/2); the uniform α hypothesis must remain. ∎

Let J=J*=J^(-1), JP=PJ and JG=GJ. The restricted involutions give
`J_L A=A J_L`, `J_L B=B J_M`, `J_M D=D J_M`. Functional calculus makes
D^(1/2) commute with J_M. Its reduced solution is unique in M₀, so
`C J_L=J_M C`. Consequently R₀,S₀ commute with J_L. A^(-1/2) commutes
with J_L and T intertwines the parity spaces as well. Thus
`||T||=max(||T_+||,||T_-||)`. This proves parity at zero directly from
the range theorem, independently of exchanging a singular inverse limit.

For four low Legendre modes with signs (−,+,−,+), the sectors are indices
(1,3) and (2,4). In each sector a Hermitian matrix [[a,z],[conj(z),d]]
is PSD iff `a≥0`, `d≥0`, `ad−|z|²≥0`. If a>0, complete
`a|x+(z/a)y|²+(d−|z|²/a)|y|²` using the consistent matrix
convention; if a=0 the determinant condition forces z=0. Necessity follows
from coordinate vectors and the same completion. Positive determinant alone
does not suffice: diag(−1,−1) is a counterexample. The finite code tests
full G's parity before selecting sectors; it does not zero forbidden entries.

**Retained initial defect and correction.** The first draft printed
`conj(z)/a` instead of `z/a` inside this complex square. That expression is
false for the declared matrix convention: take a=d=1, z=i, x=i, y=1.
The actual quadratic form is 4, the incorrectly conjugated square is 0,
and the corrected square is 4. The draft was corrected before freezing;
the independent auditor also identified this exact defect. A regression
uses pairs of rational coordinates for these Gaussian numbers, with no
floating arithmetic. Production `psd_two_by_two` accepts only real rational
entries; its finite checks never purported to verify the complex theorem.

No square root matrix need be computed to test OS5: directly certify the
generalized Loewner inequality R₀≤A. A source-enclosed response R_low≤R₀≤R_up
gives `A−R_up≤S₀≤A−R_low`. In each 2×2 sector this supports independent
lower and upper PSD/eigenvalue tests. For a real symmetric matrix M,
`min(M₁₁,M₂₂)−|M₁₂|≤lambda_min(M)` and
`lambda_max(M)≤max(M₁₁,M₂₂)+|M₁₂|`, by bounding the cross quadratic term.
Rational interval endpoints give rigorous coarse bounds with no floating
eigenvalue computation. Loewner order gives
`lambda_min(L)≤lambda_min(S₀)≤lambda_min(U)` for L≤S₀≤U.

In unnormalized Legendre coordinates, W=diag(1/3,1/5,1/7,1/9) is the
metric; PSD of the form matrix is invariant under its positive congruence.
Euclidean eigenvalues of that raw form matrix are **not** the operator's
normalized eigenvalues. This finite lane's declared metric is Euclidean;
the source lane must provide the W conversion before transporting eigenvalues.

## OS-06 — trial responses bound the envelope, not its sign oracle

Under OS3, let U:L→M be bounded, define r=B*−DU and
`L_U=BU+U*B*−U*DU`. Then

    R₀−L_U=(C−D^(1/2)U)*(C−D^(1/2)U)≥0.           (OS6)

For an additional bounded positive K on M, assume D≥κK, κ>0, and
**r=K^(1/2)E** for a bounded E:L→(ker K)⊥. Set C_U=E*E. Then

    A−L_U−κ^(-1)C_U ≤ S₀ ≤ A−L_U.                 (OS7)

**Proof.** Expand the Gram in OS6 using D^(1/2)C=B*. Douglas factorization
from κK≤D yields K^(1/2)=D^(1/2)F with ||F||≤κ^(-1/2).
The reduced solution to D^(1/2)z=r x is the orthogonal projection of FEx
onto M₀, hence has norm at most κ^(-1/2)||Ex||. Its reduced solution is
also `(C−D^(1/2)U)x`. Apply the bound to OS6 and subtract from A. This
requires the actual range factorization of **every** residual column, not
only r∈closure ran(K^(1/2)). ∎

There is a useful exact negative-witness identity:
`<x,(A−L_U)x>=Q_G(x−Ux)`. Thus a certified negative upper quadratic
value directly supplies a negative direction of the original source form.
A negative lower value does not. For A=2,B=D=K=1,U=0,κ=1/10, the bracket
is **−8≤S=1≤2**. Its negative lower endpoint is compatible with a positive
whole form. The exact response U=1 closes both endpoints at S=1 even with
that conservative κ. This separates trial quality from inherited coercivity.

The finite implementation requires K>0 and uses the genuine finite inverse
to compute C_U=r^T K^(-1)r, checking D−κK≥0 first. It is explicitly a
finite counterpart; it does not apply a bounded inverse to the source's
compact K. The source quotient derivative formula supplies E in that setting.

## OS-07 — algebraic and bounded observation factorization

Let X,Y,Z be real or complex vector spaces and O:X→Y, h:X→Z linear.
The following are equivalent: h is constant on O-fibers; ker O⊆ker h;
there is a unique linear d:ran O→Z with h=dO. Indeed if the kernel inclusion
holds define d(Ox)=hx, which is well-defined and linear; all converses
follow by applying the factorization to kernel vectors. An arbitrary
set-theoretic decoder, if it exists, therefore induces the same linear map
on the reachable image. Extension beyond the image is a separate operation.

Now give X,Y norms and assume Z is Banach. The induced d is bounded iff
there exists C<∞ such that

    ||hx|| ≤ C ||Ox|| for every x.                 (OS8)

This same condition is necessary and sufficient for a unique bounded linear
extension to closure(ran O), with the same least norm. Proof: OS8 first
forces the kernel inclusion, then is exactly the norm inequality for d.
For each y in the closure take y_n∈ran O converging to y; d(y_n) is Cauchy,
converges in Z, and has a limit independent of the approximating sequence.
Linearity, the norm bound and uniqueness pass to that limit. The converse
is immediate. If Y is Hilbert, composing with its orthogonal projection
onto closure(ran O) gives a bounded decoder on all Y. Such whole-Y
extensions are generally nonunique. No such extension principle is asserted
for arbitrary Banach Y and a noncomplemented closed range.

For Hilbert X,Y,Z and bounded O,h, OS8 is equivalently the operator inequality
`h*h≤C²O*O`; this follows by evaluating both quadratic forms on every x.
In finite-dimensional rational models every algebraic decoder is bounded,
but bounds across growing dimensions need not be uniform.

**Sharp failure.** On ell² let Oe_n=e_n/n and h=I. O is bounded and
injective, so the coimage decoder exists algebraically. Yet for y_n=e_n/n,
||y_n||→0 while ||d(y_n)||=1. The decoder is not continuous and cannot
extend boundedly to closure(ran O)=ell². At dimension N its optimal bound
is exactly N: the inequality follows termwise and e_N attains it. Passing
every finite bound does not establish a single global bound.

There is a quadratic analogue, useful when OS-01 is coupled to completion:
a bounded Hermitian form q on closure(ran O), pulled back to Q_G, exists iff
`|Q_G(u)|≤C||Ou||²` uniformly for some C. Sufficiency follows by the
same polarization and scaling as OS-01: Q vanishes on the kernel; for
u+tz the inequality forces cross terms to vanish when Oz=0. The induced
Hermitian form b satisfies `|b(y,y)|≤C||y||²`. Real/complex polarization
gives a bounded sesquilinear form (for example a constant 2C suffices), so
it extends by continuity to the completion. The represented self-adjoint
operator has norm sup_(||y||=1)|b(y,y)|≤C, retaining the sharp diagonal
bound. Necessity is its norm inequality. This is a theorem about a uniform
bound, not a source-free continuity promotion from an algebraic quotient.

## OS-08 — source-preserving conditional Suzuki application

Retain the actual source and domain from the inherited
[four-low dossier](../2026-10-15/FOUR_LOW_SCHUR_CROSSPOLLINATION.md):
`H=L²_0((-1/2,1/2);C)`, G the mean-zero compression of the **complete
signed** convolution kernel g, P the orthogonal projection onto Legendre
degrees 1..4, Q=I−P. The Gamma factor, both pole channels, genuine prime-2
half-density impulse and contact term are unchanged. This lane does not
recompute their interval constants. Its application retains these premises:

1. The source identification and bounded self-adjoint G on this H.
2. `D=QGQ≥κ K_Q`, κ=20699/1000000, with K_Q the compression of V*V,
   `Vu(t)=integral_(-1/2)^t u(s) ds`; K_Q is positive injective.
3. The source weak derivative is integrable, so G:H→H¹ on the interval.
4. For F∈H¹, the inherited quotient-residual theorem gives
   `QF∈ran(K_Q^(1/2))` and
   `||K_Q^(-1/2)QF||²=||Pi_M F'||²`, where M is the L² orthogonal
   complement of polynomials of degree≤3.
5. A=PGP is positive definite and source reflection commutes with G,P.

These are source theorem hypotheses, not facts inferred from exact finite
models. Premises 2–4 applied to F=Gx and Douglas imply
`ran(B*)⊆ran(D^(1/2))`. The four-dimensional reduced map C is bounded.
D is strictly positive on each nonzero hidden vector; no L² spectral gap
is asserted. The following conclusions are therefore conditional theorems:

| Target from the four low moments | Exact conclusion | Remaining access/sign debt |
|---|---|---|
| Actual energy Q_G(u) | Does **not** factor through P, since D≠0 | Hidden energy remains even at x=0 |
| Boolean nonnegative sign | Factors iff G≥0 iff S₀≥0 iff ||T||≤1 | Equivalent reformulation; original sign OPEN |
| Worst-case envelope m(x) | Finite quadratic `<S₀x,x>` | Source R₀ must be known/certified to evaluate it |
| Certified lower report | Any genuine OS7 lower form depends only on x and bounds every hidden completion | All continuum residual/source enclosures must be certified |
| Negative original direction | A negative upper value gives explicit x−Ux; a negative S₀ value implies existence of a negative completion | A negative lower bound or positive upper bound alone decides neither |

Reflection gives exactly two 2×2 contraction/Loewner tests, not their signs.
If S₀ is not PSD, choose x with <S₀x,x><0. OS3 supplies a sequence of hidden
completions with energies tending to that negative number, so some are
negative; OS-02 supplies positive completions of that same x. Thus low-only
sign determination is impossible in that conditional regime. This is **not
evidence that the regime occurs**.

One lawful approximate completion is `h_lambda=−(D+lambda I)^(-1)B*x`,
lambda>0. The spectral multiplier `D/(D+lambda)` converges strongly to I
on M₀, hence `D^(1/2)h_lambda+Cx→0`. This proves eventual negative energy
when the envelope is negative, without claiming an effective lambda, a
bounded zero-shift inverse, or a quantitative source error. Constructing
a certified admissible test still needs the inherited source-domain/core
bridge or a directly admissible trial. The mathematical envelope does not
constitute physical enumeration of the high carrier.

## Executable contract, adversarial evidence, and replay

`RationalSourceSpace` fixes the existing source passport (identity, observer,
epoch), ordered basis and Euclidean rational metric. Matrices/vectors reject
floats and bool aliases, dimension is capped at eight, and complete exact
arithmetic depends on rational input bit lengths. Source strings and hashes
bind model data only; even a source named `PINNED_ORIGINAL_SUZUKI` cannot
discharge a source-identification debt. There is no caller flag for Lean or
infinite sign authority. RREF and exact matrix arithmetic require no BLAS.

The API includes radical factorization with a witness or reachable decoder,
sign classification with strict opposite-sign witnesses, per-fiber and
all-fiber envelopes, full parity checks, a square-root-free contraction
test, trial brackets, and finite linear domination gates. These are narrow
exact certificates, not a universal theorem prover. The independent finite
comparison uses congruence elimination against all principal minors on all
729 symmetric 3×3 matrices with entries in {−1,0,1}; these are two algorithms
sharing rational arithmetic and one mathematical source specification, not
blind independent reasoners or separate arithmetic provenance.

Focused checks also cover 140 scalar low/high triples, direct original
polynomial expansion on 81 four-coordinate inputs, singular range failure,
nonunique finite minimizers, positive original/negative sufficient lower,
wrong source epoch/basis, false source tokens, joint versus single probes,
and finite decoder norm growth. The analytic nonattainment example is
proved by its explicit infinite sequences; finite geometric sums merely
calibrate that formula. The formal agent/principal receives OS-01–OS-05's
typed theorem statements; this lane claims no formal compilation result.

Reproduce from the repository root, serially, with `OPENBLAS_NUM_THREADS=1`,
`OMP_NUM_THREADS=1`, `PYTHONDONTWRITEBYTECODE=1`:

```sh
/tmp/succ-proof-teeth-py310/bin/python -B -m unittest discover -s tests -p 'test_observer_schur.py' -v
/tmp/succ-proof-teeth-py313/bin/python -B -m unittest discover -s tests -p 'test_observer_schur.py' -v
/tmp/succ-proof-teeth-py310/bin/python -B scripts/observer_schur_probe.py
/tmp/succ-proof-teeth-py313/bin/python -B scripts/observer_schur_probe.py
```

Actual command output, exit codes, interpreter versions, assigned-file
before/after hashes, and source dependency hashes are recorded in
`observer-schur-validation.json` and `observer-schur-py310/py313` receipts
beside this document. No full-suite or hosted-CI result is claimed by this lane.
κ/contact is the read source and executed exact instances; φ/survival is
restricted to stated theorems and finite models; σ/source identification is
retained separately; ρ/commitment to the desired sign has no evidential weight.

| ID | Status | Domain and conclusion | Falsification boundary |
|---|---|---|---|
| OS-01 | PAPER_PROVED | Hermitian energy factors iff observation kernel is radical | Isotropy alone fails; continuity separate |
| OS-02 | PAPER_PROVED | Full sign classification for bounded G with D≥0, including D=0 | Without D≥0 the classification changes |
| OS-03 | PAPER_PROVED | Finite envelope iff actual square-root range; reduced Schur formula | Closure range and kernel orthogonality alone fail |
| OS-04 | PAPER_PROVED | Attainment iff actual D range; explicit compact nonattainment | Finite minima do not imply infinite attainment |
| OS-05 | PAPER_PROVED | A≥αI contraction equivalence and full-source parity | Positive whole G is not assumed; sectors still need sign proofs |
| OS-06 | PAPER_PROVED | Trial bracket under residual range plus relative coercivity | Negative lower is not negative source |
| OS-07 | PAPER_PROVED | Algebraic versus bounded factorization, closure extension | Uniform domination cannot be inferred from finite prefixes |
| OS-08 | PAPER_PROVED conditional | Apply OS-01–07 to the pinned source under five inherited premises | Original four-low sign and effective response computation remain OPEN |
| Finite receipts | EXACT_FINITE_CHECK | Complete rational matrix identities and witnesses in bounded dimensions | No Lean/physical/source/universal analytic promotion |

The most consequential remaining analytic lemma is a **source-certified
uniform bound on the actual continuum residual columns in their K-relative
norm**, sharp enough to decide the two parity Schur matrices. None of the
observer factorizations supplies that bound. Better numerical eigenvalues
alone cannot discharge it.
