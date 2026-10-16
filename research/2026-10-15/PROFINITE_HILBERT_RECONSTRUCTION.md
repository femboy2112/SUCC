# Operation Proof Teeth, Swarm A: normalized-Haar Hilbert reconstruction

Date: 2026-10-15. Stable theorem IDs: **PH-01–PH-08**.
Capsule status: **PAPER_PROVED** (classical mathematics with explicit proofs below),
not Lean/formal verification. Executable status is separately **TESTED MODEL**.
Base: `0f86ba2478a72bf90cf33a4ee192cb2265d992dd`.
Branch: `research/succ-yean-proof-teeth-ultra-2026-10-15`.
Scope: Swarm A's additive Hilbert module, tests, probe, this paper and dedicated
receipts. No archival changes, global ledger edits, commits or pushes by Swarm A.

## 1. Question, assumptions and provenance

The strongest faithful mathematical claim is that the normalized finite cyclic
observation spaces assemble by isometric **pullback**, and their Hilbert completion
recovers all of complex `L²(Zhat, μ)`. Its Fourier coordinates are counting-measure
`ell²(Q/Z)`. Neither the algebraic direct limit alone nor any fixed finite stage is
the completion. No inference about physical realization, infinite elapsed computation,
completed Weil signs, or RH follows.

Fix one declared source identity and epoch `s=(source_id, epoch)` throughout each
diagram. Set `G=Zhat=lim_(n|N) Z/NZ` with its inverse-limit topology. All moduli are
positive integers, including 1; the directed order is **divisibility**, not numerical
size. Write `π_(N,n)(x)=x mod n`, `π_n:G→Z/nZ`, and `K_n=ker π_n`.
We use ordinary complex Hilbert spaces, countably additive **regular Borel Haar
probability** `μ`, and its measure completion if necessary. `L²` identifies functions
equal almost everywhere. Inner products are **linear in the first variable**.
The finite space `H_n=C^(Z/nZ)` has

\[
 \langle f,g\rangle_n={1\over n}\sum_{x\bmod n}f(x)\overline{g(x)}.
\]

The universal property requires a complete Hilbert target and a **uniformly bounded**
compatible family of linear operators, not merely individually bounded operators.
Strong convergence requires the full divisibility net or a divisibility-cofinal
refinement chain (e.g. `n_j=j!`). A single prime-power chain is not cofinal for `Zhat`.

This work reuses, without changing, these current-repository kernels:

| Existing source | Role and last touching commit at the base |
|---|---|
| `classical_haar_clock.py` | Prime-clock Haar calibration and affine source law; `0f80b987b9524edd16467437cc8b9f5b5feb21e6` |
| `dynamic_fourier_tower.py` | Canonical cyclotomic embeddings and raw fiber sums; `c17538418aed8bfe84876f0014acbbf421ede513` |
| `pontryagin_source_duality.py` | Source-typed rational-circle characters and dual arrow; `dacafa82b2f220ad74aeaea90a9474fa0509a475` |
| `finite_quotient_retract.py` | Pullback/average kernels extended coefficientwise; `058e9d8e8225d687b24fe2bf51a736b8332507a3` |

The shared exact arithmetic is `finite_fourier_carrier.CyclotomicElement`. These
routes share provenance and are not independent mathematical witnesses. The existing
[prime Haar dossier](CLASSICAL_HAAR_TOWER_AND_NONUNIT_BRIDGE.md) and
[source-duality dossier](PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md) supply the local
context. The import manifest identifies frozen origin commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; none of the four requested kernels is an
imported archival path. The provenance verifier checks the archives separately.

Classical attribution: compact abelian Fourier completeness is stated in
[Terence Tao, 254A Notes 3, Exercise 22](https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/).
The specialized profinite arguments below establish the claimed reconstruction
directly; they do not assume Fourier completeness as a premise of its own proof.
Standard foundational inputs are compactness of a countable product of finite
spaces, measure extension/regularity on compact metric spaces, density of simple
functions in `L²`, and completion of inner-product spaces.

## PH-01 — normalized finite Hilbert tower and adjoints

**Statement (PAPER_PROVED).** For every `n|N`, put `k=N/n` and define

\[
 (U_{N,n}f)(x)=f(x\bmod n),\qquad
 (A_{N,n}g)(a)={1\over k}\sum_{j=0}^{k-1}g(a+jn).
\]

Then `U_(N,n)` is isometric, `A_(N,n)=U_(N,n)*`, `AU=I`, and `UA` is the
orthogonal projection onto the cylinder subspace. Identities hold when `N=n`.
For `n|N|L`, `U_(L,N)U_(N,n)=U_(L,n)` and
`A_(N,n)A_(L,N)=A_(L,n)`.

**Proof.** Each residue modulo `n` has exactly `k` lifts, so

\[
 \|U_{N,n}f\|_N^2={k\over N}\sum_a|f(a)|^2=\|f\|_n^2.
\]

Grouping the mixed inner product by those same fibers gives
`<Uf,g>_N=<f,Ag>_n`. Averaging a constant fiber gives `AU=I`.
Thus `(UA)*=UA` and `(UA)²=UA`; its range is exactly the range of `U`.
Reduction maps compose, proving the pullback identity. Taking adjoints gives
the averaging identity (also obtained by enumerating each lift exactly once).
These calculations apply to arbitrary complex values, not only rational samples. ∎

**Falsifying control.** Under counting measure, raw pullback has norm `sqrt(k)`,
and its adjoint sums fibers without division. For `n=2,N=4,f=(1,0)`, the counting
squared norms are 1 and 2, while the Haar squared norms are both `1/2`.
Replacing `A` by a raw sum also changes `AU` from `I` to `kI`.

## PH-02 — regular Haar probability and completion of the cylinder direct limit

**Statement (PAPER_PROVED).** There is a regular Borel Haar probability `μ` on `G`
with `μ(π_n^(-1){a})=1/n`. The algebraic isometric direct limit
`D=colim_(n|N)(H_n,U_(N,n))` embeds as precisely the locally constant cylinders
in `L²(G,μ)`, is dense there, and has Hilbert completion canonically unitarily
isomorphic to `L²(G,μ)`.

**Proof of the measure and density hypotheses.** The compatibility conditions
define a closed subset of the countable product of finite discrete compact spaces;
thus `G` is compact metrizable Hausdorff. Each `π_n` is onto, since diagonal integers
represent every residue. Kernels `K_n` and their cosets form a countable clopen base.
Finite intersections reduce to a common multiple.

Every clopen subset is a finite union of basic cylinders by compactness, hence
`π_n^(-1)(B)` for some subset `B⊆Z/nZ`. Assign it mass `|B|/n`. Passing to a common
multiple shows that the value is independent of representation and finitely
additive. This is a premeasure on the clopen algebra: if a countable disjoint
union of clopen sets is clopen, its compact union has a finite subcover, so all
but finitely many nonempty disjoint terms disappear. The premeasure is therefore
countably additive whenever the union belongs to the algebra. The finite-measure
extension theorem gives a unique Borel probability, because the algebra generates
the Borel sigma algebra. A finite Borel measure on this compact metric space is
regular. Translation preserves the cylinder masses, so uniqueness of extension
implies translation invariance. This constructs the asserted normalized Haar
probability and proves that each finite quotient has uniform pushforward measure.

For density, let `E` be the class of Borel sets approximable in symmetric-difference
measure by clopen sets. It contains the clopen algebra and is closed under complements
and finite unions. It is closed under countable unions: a countable union is
approximated in measure by a sufficiently long finite union (continuity from below
and total mass 1), and then each of its finitely many terms is approximated by a
clopen set. Thus `E` is a sigma algebra containing the cylinder algebra, so it
contains every Borel set. Completed-measurable sets differ from Borel sets by null
sets and have the same approximation property. Since
`||1_B-1_C||²=μ(B△C)`, clopen simple functions are dense among measurable simple
functions in `L²`. Simple functions are dense in `L²` by truncation and value
approximation. Every finite clopen simple function factors through one common
finite modulus. Cylinder functions are therefore dense.

**Proof of the direct-limit identification.** Represent an element of `D` by `(n,f)`.
Declare `(n,f)~(m,g)` exactly when their pullbacks agree at a common multiple.
Coherence and injectivity from PH-01 make this an equivalence relation. Addition
and inner products are computed at a common multiple; isometry makes them
independent of the chosen multiple. The resulting inner product is positive
definite. Define `j_n(f)=f∘π_n`. Haar cylinder masses give
`||j_n f||=||f||_n`, and `j_N U_(N,n)=j_n`. Equality in `L²` is faithful on finite
cylinders: a nonzero value on one residue occupies positive measure `1/n`.
Consequently `D` embeds isometrically. Its image is the cylinder union, dense by
the preceding paragraph. A locally constant function on compact `G` has finite
range by a finite constant-neighborhood subcover; its level sets are clopen, so
it too is a cylinder. Extension to the completion is an isometry with dense
closed image, hence a unitary onto `L²(G,μ)`. ∎

**Boundary and next falsifier.** None of compactness, regularity, or cylinder density
is inferred from successful finite probes. Changing the sigma algebra, measure,
or directed index family requires checking this proof again. In particular,
`p^r` alone reconstructs `L²(Z_p)`; its image in `L²(Zhat)` is generally proper.

## PH-03 — Fourier completion is counting ell²(Q/Z)

**Statement (PAPER_PROVED).** Put `D_n=(1/n)Z/Z⊂Q/Z` and

\[
 \chi_{a/n}(x)=e^{2\pi i a\pi_n(x)/n},\qquad
 (\mathcal F_n f)(a/n)={1\over n}\sum_{x\bmod n}f(x)e^{-2\pi i ax/n}.
\]

The `χ_r`, for `r∈Q/Z`, form an orthonormal basis of `L²(G,μ)`. Fourier analysis
extends to a unitary `F:L²(G,μ)→ell²(Q/Z,counting)` with
`Ff(r)=<f,χ_r>`. For `n|N`, let `J_(N,n)` extend spectral coordinates by zero
from `D_n` to `D_N`. Both squares commute:

\[
 \mathcal F_N U_{N,n}=J_{N,n}\mathcal F_n,
 \qquad
 \mathcal F_n A_{N,n}=J_{N,n}^{*}\mathcal F_N. \tag{PH-03a}
\]

In integer labels the injection is `a↦(N/n)a`; it does not retain label `a`.

**Proof.** Transport to a common denominator proves the character formula
well-defined. At a finite level the geometric sum of an `n`th root of unity is
`n` for the trivial root and zero otherwise. Thus the `n` characters form an
orthonormal basis for the `n`-dimensional normalized-Haar space. Inversion and
Parseval follow by expanding in this basis:

\[
 f(x)=\sum_{a=0}^{n-1}(\mathcal F_n f)(a/n)e^{2\pi i ax/n},\qquad
 {1\over n}\sum_x|f(x)|^2=\sum_a|\mathcal F_n f(a/n)|^2.
\]

Pulling back `χ_(a/n)` along reduction gives `χ_((ka)/N)` with `k=N/n`.
This proves the first square on a basis and hence on all vectors; unitarity and
adjoints prove the second. On `G`, the inner product of any two characters is
computed at a common finite denominator, giving orthonormality. Every cylinder
is a finite linear combination of these characters; PH-02 makes their span dense.

For completeness of the dual identification itself, each continuous character
`χ:G→S¹` factors through some finite quotient. Choose an open arc about 1 containing
no nontrivial subgroup of `S¹`, for example `Re(z)>0`. By continuity, `χ^(-1)` of
that arc contains some `K_n`. Its image is a subgroup contained in the arc, hence
trivial. Therefore `χ` factors through `G/K_n=Z/nZ` and equals `χ_(a/n)` for some
`a`. Different rational classes are separated already by evaluation at the
diagonal integer 1. The compact-open topology on the dual is discrete: demanding
that the image of the whole compact `G` lie in that arc isolates the trivial
character. This identifies the continuous dual with discrete `Q/Z`.

The isometric Fourier map on `D` identifies it with the finitely supported
sequences on `Q/Z`: finitely many rational frequencies lie in one `D_n` by taking
the least common multiple of denominators. For any square-summable sequence `c`,
finite partial sums `Σ_r c_r χ_r` are Cauchy by finite Parseval; completeness gives
an `L²` limit. Its coefficient at each `r` is `c_r`, since the coefficient
functional is bounded by the `L²` norm. Thus the extension is onto, and both
Parseval and inversion in `L²` follow. This proves the full Fourier theorem here
without using a finite test as an infinite completeness argument. ∎

**Sign control.** The existing `exact_dft` is the unnormalized **positive** sum.
The implementation uses `F_n f[a]=exact_dft(f)[-a mod n]/n`. Analysis of the
positive character `χ_(1/3)` has its sole coefficient at `1/3`; retaining the
positive analysis exponent puts it incorrectly at `2/3`.

## PH-04 — universal property for uniformly bounded cones

**Statement (PAPER_PROVED).** For every complex Hilbert space `K` and family of
linear operators `T_n:H_n→K` satisfying

\[
 T_NU_{N,n}=T_n\quad(n\mid N),\qquad
 C:=\sup_n\|T_n\|<\infty,
\]

there is a unique bounded linear `T:L²(G,μ)→K` with `Tj_n=T_n` for every `n`,
and `||T||=sup_n||T_n||`. If every `T_n` is isometric then `T` is isometric;
it is unitary onto `K` exactly when the union of the images `T_n(H_n)` is dense.
In particular, this is a colimit in the category of Hilbert spaces and contractions.

**Proof.** On `D` set `T[(n,f)]=T_n f`. Compatibility at a common multiple
proves well-definedness and linearity. The uniform bound gives
`||T[(n,f)]||≤C||[(n,f)]||`. If `d_j→h` in the completion, `Td_j` is Cauchy
and converges in the complete target `K`; define `Th` by that limit. The bound
shows independence of the approximating sequence and continuity. Density forces
uniqueness. Restricting `T` to each isometric `j_n` gives `||T||≥||T_n||`;
the extension bound gives the converse. If all component maps preserve norms,
the same is true first on `D` and then by continuity on its completion. An
isometry has closed range; it is onto exactly when that range is dense. ∎

**Necessary hypothesis / negative control.** The evaluation maps
`T_n(f)=f(0)` are compatible and individually bounded, with `||T_n||=sqrt(n)`.
They have no bounded extension to `L²(G,μ)`: the cylinder `1_(K_n)` has image
1 under evaluation but norm `1/sqrt(n)`. In fact point evaluation is not
intrinsically defined on arbitrary almost-everywhere equivalence classes. Thus
an unrestricted compatible cone in the category of all bounded maps need not
factor through this completion. Uniform boundedness is load-bearing.

## PH-05 — strong convergence and the exact character norm obstruction

**Statement (PAPER_PROVED).** Let `P_n=j_n j_n*` be conditional expectation onto
the finite sigma algebra generated by `π_n`. In Fourier coordinates,

\[
 P_n\chi_r=\begin{cases}\chi_r,& nr=0\text{ in }Q/Z,\\0,&nr\ne0.\end{cases}
 \quad P_nP_m=P_{\gcd(n,m)}. \tag{PH-05a}
\]

The divisibility net `P_n` converges strongly to the identity; the same is true
on any increasing divisibility-cofinal chain. Nevertheless, for **every** finite
`n≥1`, `||I-P_n||=1`. There is no convergence in operator norm.

**Proof.** Averaging a character over fibers kills it unless it is constant
on `K_n`, equivalently unless its conductor divides `n`; this also follows
from PH-03a. The frequency sets intersect as `D_n∩D_m=D_gcd(n,m)`, proving
the product formula. Given `f∈L²` and `ε>0`, choose a cylinder `h∈j_d H_d`
with `||f-h||<ε`. For every multiple `n` of `d`, `P_n h=h`. Since `I-P_n`
is an orthogonal projection,

\[
 \|(I-P_n)f\|=\|(I-P_n)(f-h)\|\le\|f-h\|<\epsilon.
\]

This proves strong convergence with its exact quantifiers. Equivalently,
`||(I-P_n)f||²=Σ_(r∉D_n)|Ff(r)|²` tends to zero along the directed net.
For the norm lower bound choose the explicit unit character

\[
 h_n=\chi_{1/(2n)}. \tag{PH-05b}
\]

Its conductor `2n` does not divide `n`, so `P_n h_n=0` and
`||(I-P_n)h_n||=1`. The projection upper bound is 1, giving equality.
The witness is allowed to vary with `n`; this is precisely why it does not
contradict convergence for each **fixed** `f`. ∎

**Noncofinal control.** For the numerically increasing tower `2,4,8,...`, the
fixed unit character `χ_(1/3)` is killed at every stage, so strong convergence
to the identity on all of `L²(Zhat)` fails. Merely letting the modulus grow
numerically is insufficient. A finite prefix cannot certify an arbitrary
source's remaining Fourier tail; the exact norm obstruction persists beyond
every finite observation stage.

## PH-06 — finite conditional expectation versus translations and multipliers

**Statement (PAPER_PROVED).** Fix `N=nk`, an integer translation `t`, positive
integer `m`, and integer offset `b`. On either finite level let
`T_t f(x)=f(x+t)` and `M_(m,b)f(x)=f(mx+b)` (Koopman pullbacks).
Pullbacks always intertwine these compatible source maps:

\[
 U_{N,n}T_t^{(n)}=T_t^{(N)}U_{N,n},\qquad
 U_{N,n}M_{m,b}^{(n)}=M_{m,b}^{(N)}U_{N,n}. \tag{PH-06a}
\]

Translation also intertwines averaging. For multiplication the exact criterion is

\[
 A_{N,n}M_{m,b}^{(N)}=M_{m,b}^{(n)}A_{N,n}
 \quad\Longleftrightarrow\quad \gcd(m,k)=1. \tag{PH-06b}
\]

This is a condition on the **fiber multiplicity** `k`, not on `N` alone.

**Proof.** Reduction commutes with each affine source map, proving PH-06a.
Translation takes each reduction fiber bijectively onto the corresponding
translated fiber, preserving its uniform distribution. For multiplication,
the left average at residue `a` samples

\[
 ma+b+mn j\pmod N,\qquad 0\le j<k,
\]

while the right average uniformly samples all lifts of `ma+b mod n`. On the
fiber index modulo `k`, this is multiplication by `m` followed by a translation
(the carry of `ma+b`). It is a permutation iff `gcd(m,k)=1`, proving sufficiency.
For necessity put `d=gcd(m,k)>1` and take the fine-level function
`f=1_{x=b mod N}`. At `a=0`, the left average is `d/k`, because
`mj=0 mod k` has exactly `d` solutions. The right average is `1/k`.
They differ, so the operator identity fails. The proof includes `n=1`
and the trivial quotient `k=1`. ∎

**Exact negative and positive controls.** For `N=4,n=2,m=2,b=1`, the authentic
unit-origin source action is `x↦2x+1`; with `f=1_{x=1}` one obtains

\[
 A M f=(1,0),\qquad M A f=(1/2,1/2).
\]

For `N=6,n=2,m=2,b=1`, the same nonunit multiplier **does** commute with
averaging because `gcd(2,3)=1`, despite `gcd(2,6)>1`. Thus the stronger claim
“every nonunit fails on every finite quotient” is refuted.
In a prime-power adjacent tower `N=p^(r+1),n=p^r`, the criterion reduces to
`p∤m`; in particular genuine prime multiplication `m=p` fails.

## PH-07 — global nonunit multiplication: boundedness and noncommutation

**Statement (PAPER_PROVED).** For every positive integer `m` and `b∈G`, the
source map `a_(m,b)(x)=mx+b` is injective and has image `b+mG`, of Haar mass
`1/m`. Its Koopman operator on almost-everywhere classes is well-defined and
bounded, with

\[
 \|M_{m,b} f\|_2^2=m\int_{b+mG}|f(y)|^2\,d\mu(y),
 \qquad \|M_{m,b}\|=\sqrt m. \tag{PH-07a}
\]

For every `t∈G`, translations `T_t` are unitary and commute with every `P_n`.
For `m>1`, no finite `P_n` commutes with `M_(m,b)` on the whole `L²(G)`.
An exact unit-character witness is `χ_(1/(mn))`. The global commutators
converge strongly to zero along cofinal refinement, but not in operator norm.

**Proof of injection and image.** If `mx=0`, inspect the coordinate modulo
`mn`. The congruence `m x_(mn)=0 mod mn` implies `x_n=0 mod n` for every `n`,
so `x=0`. Clearly `mG⊆K_m`. For the reverse inclusion let `y∈K_m`. Its
coordinate `y_(mn)` is divisible by `m`; define
`x_n=(y_(mn)/m) mod n`. Division is well-defined modulo `n`, and these
coordinates are compatible under reduction. They define `x∈G` with `mx=y`.
Thus `mG=K_m`, which has index `m` and mass `1/m`. The injection from compact
`G` onto `K_m` is a homeomorphism.

**Proof of the L² formula.** The pushforward of Haar probability under this
group isomorphism is Haar probability on `K_m`. It equals the restriction
`m μ|_(K_m)`: that restriction has total mass 1 and is invariant under `K_m`.
Translation by `b` yields pushforward `m 1_(b+K_m) μ`, proving PH-07a first
for nonnegative simple functions and then by monotone integration. In particular
null sets pull back to null sets, so composition is well-defined on `L²`
classes. The formula gives the norm upper bound, attained by a nonzero
function supported on `b+K_m`, proving exactness.

For clarity the adjoint is

\[
 (M_{m,b}^*g)(y)=m\,1_{b+mG}(y)\,g((y-b)/m).
\]

Hence `MM*=mI` and `M*M=m 1_(b+mG)` as multiplication by a function.
The operator `m^(-1/2)M` is a coisometry; for `m>1`, `M` itself is not an
isometry. At a finite level the source multiplication may have a nonzero
kernel and the operator norm squared is only `gcd(m,N)`. These finite facts
do not contradict the injective global source map or its global norm.
Indeed, putting `d=gcd(m,N)`, each attained residue has exactly `d` preimages
and the image has `N/d` residues; normalized finite summation gives the same
energy formula with `d` in place of `m` and proves that finite norm statement.

**Proof of commutation and failure.** Translation preserves Haar measure and
acts by `T_t χ_r=χ_r(t)χ_r`, so it is unitary and commutes with the diagonal
frequency cutoff `P_n`. Multiplication acts by

\[
 M_{m,b}\chi_r=\chi_r(b)\chi_{mr}.
\]

For `r=1/(mn)` with `m>1`, `nr=1/m≠0` in `Q/Z`, whereas `nmr=1=0`
in `Q/Z`. Therefore

\[
 M_{m,b}P_n\chi_r=0,\qquad
 P_nM_{m,b}\chi_r=\chi_r(b)\chi_{1/n},
\]

and the latter has norm 1. Thus `||[P_n,M_(m,b)]||≥1` at every finite stage.
For each fixed `f`, however,

\[
 \|(P_nM-MP_n)f\|
 \le \|(P_n-I)Mf\|+\|M\|\,\|(I-P_n)f\|\longrightarrow0
\]

by boundedness of `M` and PH-05. This is another strong-versus-norm distinction.
When `m=1`, the operator is a translation and commutes. ∎

**Boundary.** This theorem concerns nonzero positive integer multiplication;
the finite evaluator admits integer offsets, while the proof permits any
`b∈G`. Zero multiplication collapses to point evaluation and has no bounded
`L²` extension. The normalized Haar measure is real-valued probability, not
a bounded `Q_p`-valued Haar measure.

## PH-08 — source-indexed commuting diagrams and convention transport

**Statement (PAPER_PROVED).** Fix `s` and `n|N`. The source square commutes:

\[
\begin{array}{ccc}
 X_N^s&\xrightarrow{x\mapsto mx+b}&X_N^s\\
 \downarrow\pi_{N,n}&&\downarrow\pi_{N,n}\\
 X_n^s&\xrightarrow{x\mapsto mx+b}&X_n^s.
\end{array}
\]

Applying observable pullback reverses arrows and gives PH-06a. The Hilbert
and spectral squares are explicitly

\[
\begin{array}{ccc}
 H_n^s&\xrightarrow{U_{N,n}}&H_N^s\\
 \downarrow\mathcal F_n&&\downarrow\mathcal F_N\\
 \ell^2(D_n)^s&\xrightarrow{J_{N,n}}&\ell^2(D_N)^s,
\end{array}
\qquad
\begin{array}{ccc}
 H_N^s&\xrightarrow{A_{N,n}}&H_n^s\\
 \downarrow\mathcal F_N&&\downarrow\mathcal F_n\\
 \ell^2(D_N)^s&\xrightarrow{J_{N,n}^*}&\ell^2(D_n)^s.
\end{array}
\]

The maps into the completed spaces obey `j_N U_(N,n)=j_n` and
`F j_n=i_n F_n`, with `i_n` extension by zero into `ell²(Q/Z)`.
All diagrams retain the same source ID and epoch. These labels enforce
declared mathematical provenance; they do not authenticate physical sourcing.

**Proof and conventions.** Commutativity of the first square is the congruence
`(mx+b) mod n = m(x mod n)+b mod n`. The remaining squares are PH-03a and
the construction of the extensions in PH-02–PH-04. The exact changes of
normalization are:

| Quantity | Counting convention | Normalized Haar convention |
|---|---|---|
| Norm at level `n` | `Σ|f|²` | `(1/n)Σ|f|²` |
| Cylinder pullback `U` | norm `sqrt(k)` | norm 1 |
| Adjoint of that same `U` | raw fiber sum `S` | average `A=S/k` |
| Fine-level orthogonal projection | `US/k` | `UA`, the same pointwise map |
| Fourier analysis used here | repository `D_n^+f[a]=Σ f(x)e^(+2πiax/n)` | `F_n f[a]=D_n^+f[-a]/n` |
| Spectral target of `F_n` | counting on characters | counting on characters, not probability |

The usual unitary counting DFT is `D_n^-/sqrt(n)`; using it on a Haar input
without changing the identification multiplies squared output energy by `n`.
The identification from Haar-coordinate functions to counting-coordinate vectors
is `f↦f/sqrt(n)`, and it transports cylinder pullback to `U/sqrt(k)`.
The present implementation avoids square-root coefficients by keeping Haar
coordinates and exact `1/n` Fourier coefficients throughout.

On the existing integer-source chart `x=z-1`, source multiplication is
`x↦mx+(m-1)` and successor is `x↦x+t`. On the reflected chart `x=1-z`,
the offsets are `1-m` and `-t`. `source_multiply` and `source_successor`
call the existing chart functions. Choosing additive ring origin `x=z` instead
permits `mx` but is a different declared coordinate convention. Koopman order
is contravariant: in either consistent chart `T_t M_m=M_m T_(mt)`.

Taking an adjoint of an intertwining equation gives an equation for the
**adjoint** multiplier. It does not license `A M_N=M_n A` for the original
nonunit multiplier. PH-06 and PH-07 provide the explicit failure receipts. ∎

## 2. Implementation, crucible and claim ledger

`observational_succ/profinite_hilbert.py` represents finite cylinders by exact
cyclotomic samples with canonical complex root embeddings. Carrier and coefficient
field are kept separate: the average of the constant `ζ_3` from carrier 6 to
carrier 2 still has value `ζ_3`, even though it is not in `Q(ζ_2)`.
The arithmetic implementation bounds both carrier and required common root
order by 100. It rejects larger least common multiples; the mathematical
theorems do not have this bound. Arbitrary complex amplitudes and arbitrary
`L²` elements occur in the proof, not as finitely encoded runtime objects.

`HaarCylinder.refine/condition` extend the existing rational retraction kernels
coefficientwise. `fourier` calls the existing exact DFT with the declared index
reversal and normalization; `character` uses the existing source-typed characters.
Prime-clock formulas are checked against `classical_haar_clock` and raw sums
against `dynamic_fourier_tower`. No alternative polynomial/cyclotomic kernel was
created. `equivalent` compares representations after lawful common refinement;
dataclass representation equality alone is not equality in the direct limit.

The 16 focused tests include coordinate-basis matrix checks of
PH-06 over several composite and prime-power quotients; these are exact finite
instances. They also preserve the wrong sign, wrong dual label, missing Haar
normalization, dropped affine offset, unbounded cone, noncofinal tower, and
nonunit-commutation boundaries. The unbounded-cone counterexample is a paper
family in PH-04 with finite specimen tests; no runtime enumeration pretends to
prove its unbounded limit.

| IDs/claim | Status | Evidence and scope | Adversarial receipt / next falsification |
|---|---|---|---|
| PH-01–PH-04, PH-08 | PAPER_PROVED / classical | Full proofs above; finite arithmetic regression is separate | Change normalization, dual label, source epoch or bounded-cone hypothesis |
| PH-05 | PAPER_PROVED | Density and projection argument with quantified net | Unit character `χ_(1/(2n))`; fixed `χ_(1/3)` for the noncofinal 2-tower |
| PH-06 | PAPER_PROVED | Complete fiber permutation argument, iff criterion | `4→2,m=2,b=1` fails; `6→2,m=2,b=1` commutes |
| PH-07 | PAPER_PROVED | Source injection/image, Haar scaling, character proof | `χ_(1/(mn))` at every finite `n`, for every `m>1` |
| Exact implementation specimens | TESTED MODEL | Bounded rational/cyclotomic tests and replayable receipt | Hostile input, basis matrices, conjugation and coefficient-field descent |
| Uniform operator-norm reconstruction | REFUTED | PH-05b gives exact norm 1 error | Witness varies with each finite horizon |
| Individually bounded cone suffices | REFUTED | PH-04 evaluation family has norms `sqrt(n)` | Uniform boundedness is necessary |
| Physical source authentication / RH consequence | UNVERIFIED / not asserted | No such construction or conclusion here | Requires separate physical evidence / arithmetic analytic theorem |

Aletheia accounting: **κ/contact** is direct code inspection and exact execution;
**φ** is finite test survival distinct from the universal paper derivations;
**σ** is declared source/epoch plus file hashes and the archived provenance check,
not authentication of a physical source; **ρ** is shared author, shared cyclotomic
oracle and shared repo lineage. No nested agents or blind independent theorem
checker were used. The live gap was an omitted global derivation and convention
transport, resolved at paper-proof level; machine-checked proof remains outside
this capsule. Repeated finite agreement is not promoted to universal proof.

The `aletheia-interferometry` provenance review uses a dependency audit, not an
invented numerical coherence score. Its rival explanations were correct Haar
transport, a missing normalization shared across implementations, a Fourier sign
or label error, and correct abstract content attached to the wrong source/chart.
The discriminator set explicitly retains controls for all four. The two tested
source charts are related by `x↦-x`; changing between them transports the affine
offset and translation sign together. No semantic phases are assigned to evidence.

| Family removed in the logical dependency audit | What remains and what is lost |
|---|---|
| Cyclotomic execution family (new Fourier code, existing DFT and character roots) | Paper derivations and rational fiber calculations remain; runtime Fourier validation is lost |
| Rational counting/prime-clock comparison family | Paper derivations and cyclotomic checks remain; cross-kernel finite normalization calibration is lost |
| Paper derivations and their stated measure-theoretic hypotheses | Only bounded finite observations remain; no global PAPER_PROVED status is justified by tests |
| Source ID/epoch and affine-chart provenance | Abstract arithmetic identities may still hold; attribution to the requested source diagram is no longer justified |

This is an explicit **logical** leave-family-out audit, not a claim that runtime
modules were disabled. All implementations and the paper share one reasoner in
this run. No statistical holdout, measured factorial/Möbius score, phasor evidence
score, or physical quantum inference is asserted. The strongest additional check
would be an independent formal proof of PH-02–PH-04 with the same normalization
and cone hypotheses; more samples alone cannot replace it.

## 3. Reproduction and receipts

Run from the isolated SUCC worktree:

```sh
python -m unittest tests.test_classical_haar_clock tests.test_dynamic_fourier_tower tests.test_pontryagin_source_duality tests.test_finite_quotient_retract
python -m unittest tests.test_profinite_hilbert -v
/tmp/succ-proof-teeth-py310/bin/python -m unittest tests.test_profinite_hilbert -v
/tmp/succ-proof-teeth-py313/bin/python -m unittest tests.test_profinite_hilbert -v
python scripts/profinite_hilbert_probe.py --verify
python scripts/verify_provenance.py
```

`PROFINITE_HILBERT_RECEIPT.json` contains exact rational witnesses, normalization
flags and SHA-256 hashes of the four reused kernels, supporting arithmetic/chart
sources, instructions, this dossier, new code, tests and probe. Regeneration is
explicit: `python scripts/profinite_hilbert_probe.py > research/2026-10-15/PROFINITE_HILBERT_RECEIPT.json`.
`--verify` recomputes both content and source hashes and fails on drift.
`PROFINITE_HILBERT_VALIDATION.json` records actually executed commands, versions,
exit codes and output hashes; the companion output file preserves their text.
Final full-suite/CI coordination belongs to the principal; Swarm A performs
focused validation only after that instruction. No claim of CI passage is made.

**Verdict:** the normalized-Haar cylinder lane survives as the explicitly proved
classical Hilbert reconstruction, with source-indexed Fourier diagrams and a
uniformly bounded-cone universal property. Uniform finite-horizon reconstruction
and unconditional nonunit-adjoint commutation fail with exact receipts. These
boundaries are part of the result. **RH PROVED: NO.**
