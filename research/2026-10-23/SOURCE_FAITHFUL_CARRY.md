# Carry the truth: exact polyphase transport and disclosed Hilbert defects

**Date:** 2026-10-23. **Source parent:** PR #244,
`5e2ba04c8b4ab627b6b0add588609c347346a1a2`.
**Authority:** paper proofs below; exact finite Python calibration is separate.
No theorem here has Lean authority merely because a related finite statement
compiles elsewhere. No physical instrument, signed Weil positivity, or RH result
is asserted. The basic digit/Cuntz, Fourier, and defect-space constructions are
classical; the explicit one-based SUCC integration and controls are new to this
round, and academic novelty is unverified.

## 0. Hole contract and inherited baseline

**Target.** For the actual source `H=ell²({1,2,...})`, determine exactly which
state and norm sectors are lost by quotient-only and uniform-channel observation,
and construct an associative loss-accounting repair for every finite radix word.
The quantifiers are all source states, all integer radices `a>=1`, and all finite
successor horizons. Primeness is an additional authenticated arithmetic condition.
**Initial state:** proposed, with elementary candidate derivations. **Final state:**
paper proved within these domains, with the false compression identifications
refuted below. The route is materially weaker than any Weil positivity theorem:
all radix identities also hold for the counterfeit primitive radix 6.

The shortest dependency chain is source bijection → exact conjugated actions →
disclosed orthogonal defect → future reconstruction. It contains no arrow from
positive Hilbert norms to the signed completed Weil source. The smallest cheap
falsifiers are source labels 1 and 2 at radix 2, radix 6 as a false prime, and
mixed radices 2 and 3 with a nontrivial character. Fresh test regimes include
radices 5, 7 and 49, source labels through 400, all permutations of (2,3,5), and
repeated prime powers. These computations calibrate formulas; universal
quantifiers are discharged by the proofs, not finite enumeration.

Existing work is not relabelled as a discovery:

* [Reciprocal SUCC/FUCC](../2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md)
  and `observational_succ/reciprocal_succ_fucc.py` already supply the one-based
  residue clock, carry, two-radix coordinate comparison and affine relations.
* [Prime-form heat](../2026-10-14/PRIME_FORM_HEAT_MELLIN_SOURCE.md), PH-01–PH-09,
  already proves the bilateral integer digit Cuntz family, residue Fourier
  phases, Gaussian Mellin/Gamma recovery, and prime-power sieve. This round adds
  explicit unilateral domains, norm/instrument distinctions, coherent defect
  composition, energy-cocycle accounting and exact compression failures.
* `source_prime_certificates.py`, `gamma_interferometer.py`, and
  `dirichlet_cumulants.py` retain the authentic logarithmic source. The new code
  does not rewrite the imported files or the 72-entry provenance manifest.

## 1. Exact one-based polyphase decomposition

Let `e_n`, `n>=1`, be the fixed authenticated orthonormal source basis. Let
`S e_n=e_(n+1)` and, for any integer `a>=1`, `V_a e_n=e_(an)`.
For `0<=r<a`, define

`U_(a,r)e_m=e_(a(m-1)+r+1)`.

Every positive integer has exactly one expression `a(m-1)+r+1`. Therefore the
basis permutation

`W_a e_(a(m-1)+r+1)=e_m tensor e_r`

extends uniquely to a unitary `H→H tensor C^a`. Its inverse is the displayed
source address, not a rounded reconstruction. No finite cyclic multiplication
is used.

**C1 (controlled carry and all adjoints, paper proved).** With `E_(s,r)` the
residue matrix units,

`T_a := W_a S W_a* = I tensor sum_(r=0)^(a-2) E_(r+1,r)
                    + S tensor E_(0,a-1)`.

Empty sums at `a=1` give `T_1=S`. For every `h>=0`, writing
`r+h=a c+t`, `0<=t<a`, gives

`T_a^h(e_m tensor e_r)=e_(m+c) tensor e_t`.

The adjoint sends `(m,r)` to `(m,r-1)` when `r>0`, to `(m-1,a-1)` when `r=0,m>1`,
and to the **zero vector** when `(m,r)=(1,0)`. More generally, put
`n=a(m-1)+r+1`. Then `(T_a*)^h(e_m tensor e_r)=0` if `n<=h`, and otherwise it is
`W_a e_(n-h)`. Thus `T_a*T_a=I` but
`T_a T_a*=I-|e_1 tensor e_0><e_1 tensor e_0|`.

For the genuine multiplier,

`W_a V_a f = f tensor e_(a-1)`,

`V_a* W_a*(f tensor e_r) = delta_(r,a-1) f`.

In conjugated rather than rectangular form,
`W_a V_a W_a*(e_m tensor e_r)
 =e_(a(m-1)+r+1) tensor e_(a-1)`.
Its adjoint is zero on residue `r!=a-1`; on `e_j tensor e_(a-1)` it is `W_a e_j`.
For `k>=1`,

`W_a V_a^k e_n = e_(a^(k-1)n) tensor e_(a-1)`,

whereas using the full radix `a^k` gives
`W_(a^k)V_a^k e_n=e_n tensor e_(a^k-1)`.
The original adjoint is
`(V_a*)^k e_n=e_(n/a^k)` if `a^k|n`, and zero otherwise.

**Proof.** Apply each side to the declared orthonormal source basis. Division
with remainder gives the forward formulas; reversing the injective basis maps
gives exactly the stated zeros. All operators in this paragraph are bounded,
so basis equality extends by density to every vector in `H`.

In particular `V_a S=S^a V_a` and its actual adjoint
`S* V_a*=V_a*(S*)^a`. Direct divisibility also proves the further relation
`V_a* S^a=S V_a*`, whose adjoint is `(S*)^a V_a=V_a S*`.
These latter formulas need their own boundary check; they are not obtained by
dropping stars or pretending unilateral isometries are unitary.

**C2 (complete residue channels, paper proved; classical Cuntz relations).**

`U_(a,r)* U_(a,s)=delta_(r,s)I`,
`sum_(r=0)^(a-1) U_(a,r) U_(a,r)*=I`,
`V_a=U_(a,a-1)`.

Indeed the channel ranges are disjoint residue basis subsets and partition all
positive source labels. The adjoint selects precisely that subset. For `a>=2`
this is a representation of the Cuntz relations. It does not establish any
additional arithmetic C*-boundary quotient. Extra channels `r!=a-1` exist
mathematically; availability of `V_p` as an authorized operation does not grant
physical access to every `U_(p,r)`.

## 2. Mixed-radix coherence is a source permutation, not a digit swap

**C3 (all finite words, paper proved).** For an ordered word
`w=(a_1,...,a_l)`, let `A=product a_i` and let its little-endian address be

`R_w(r_1,...,r_l)=r_1+a_1 r_2+...+(a_1...a_(l-1))r_l`.

Then repeated `W` maps identify the source with
`H tensor C^(a_l) tensor ... tensor C^(a_1)` by

`n-1=A(m-1)+R_w`.

The empty word is the identity. Given words `w,v` with the same product, the
comparison sends the source integer `R_w` to its unique digits in word `v`,
leaving `m` unchanged. Denote the resulting unitary by `C_(v<-w)`. Then

`C_(w<-w)=I`, `C_(u<-v) C_(v<-w)=C_(u<-w)`.

**Proof.** Both sides in each equation preserve and reconstruct the same pair
`(m,R)` and each digit expansion is unique. This proves all triple coherence
diagrams simultaneously, including repeated primes. It does not require coprime
radices, in contrast to a CRT factorization.

Equivalently the residue Hilbert spaces `E_a=C^a` have the product-system maps
`E_a tensor E_b→E_(ab)`, `e_r tensor e_s→e_(r+a s)`. Associativity is the integer
identity `(r+a s)+ab t=r+a(s+b t)`. The source channels realize the product via

`U_(a,r) U_(b,s)=U_(ab,r+a s)`.

Reversal of radices is the permutation determined by
`r+a s=u+b t`, not `r↔s`. For `(a,b,r,s)=(2,3,1,1)`, the old digits `(1,1)`
have `R=3`, while the reversed digits are `(u,t)=(0,1)`.
The composite representations `V_a V_b=V_(ab)=V_b V_a` have the same operator,
but the causal words `(a,b)` and `(b,a)` remain different records until a
declared history quotient identifies them.

## 3. Which source information is necessary for future successor?

Let `q_a(n)=floor((n-1)/a)+1` be the quotient-only observation. A deterministic
action descends through an observation iff it is constant on every observation
fiber after the action. At `a=2`, the states 1 and 2 have the same quotient, but
their successor states 2 and 3 do not. Thus quotient-only successor is not
well-defined even in the smallest example.

**C4 (minimal future-safe repair for this probe, paper proved).** For the
declared probe `q_a` and all words `S^h`, `h>=0`, define

`n ~ n' iff q_a(n+h)=q_a(n'+h) for every h>=0`.

This equivalence is equality on the positive integers. If `n,n'` already have
different quotients, `h=0` separates them. Otherwise write residues `r<r'` in the
same block and choose `h=a-r'`. The second crosses to the next block while the
first does not. For `a>1` this costs at most `a-1` successor actions and one
final quotient reading. Retaining `(m,r)` repairs the quotient exactly.

At finite horizon `H<a-1`, the residue class `0<=r<a-H` remains one class and
the `H` remaining residues are singleton classes, giving exactly `H+1` classes
per block. At `H>=a-1` all `a` residues are distinct. Thus the minimum discrete
extra register cardinality for all future successor observations is `a`; a
fixed-length binary encoding needs `ceil(log_2 a)` bits. These are mathematical
action costs for this probe, not measured physical resource costs. Adding
genuine FUCC cannot merge classes already separated by the permitted successors.

This is a concrete instance of the repository's future-bisimulation and
operational-Yoneda logic, not a replacement for it. For other probes or action
alphabets the minimal quotient can be smaller. Probabilistic or quantum
sufficiency needs its own experiment/channel definition.

## 4. The sharp Hilbert defect and its correct repair

Put `u_a=a^(-1/2)sum_r e_r` and define the coisometry

`A_a=(I tensor <u_a|) W_a`,
`A_a* e_m=a^(-1/2)sum_r e_(a(m-1)+r+1)`.

Then `A_a A_a*=I`; its source projection is `P_a=A_a*A_a`, the orthogonal
projection onto block-constant vectors. It averages entries within each block.

**D1 (all-state defect, paper proved).**

`A_a V_a=a^(-1/2)I`,
`P_a V_a=a^(-1/2) A_a*`,
`||(I-P_a)V_a f||²=(1-1/a)||f||²`,
`||(V_a-A_a*)f||²=2(1-a^(-1/2))||f||²`.

The first formula is the terminal coordinate of `u_a`; the second follows by
applying `A_a*`. Pythagoras proves the third. Expanding the squared difference
and using `<A_a*f,V_af>=a^(-1/2)||f||²` proves the fourth. In particular
`||V_a-A_a*||=sqrt(2(1-a^(-1/2)))`. This is sharp, independent of the support
length and valid for every nonzero vector, not only a single favorable block.

For `f=M^(-1/2)sum_(j=1)^M e_j`, its uniform lift `A_a*f` is exactly the uniform
vector on `1,...,aM`. The overlap in the plan is therefore `a^(-1/2)` and the
norm-square defect never decreases as `M→infinity`. In the fixed source Hilbert
space both broadening unit vectors can converge weakly to zero. That vacuous
common weak limit does not remove their separation in norm.

**D2 (coherent versus measured repair, paper proved).** The map

`R_a f=(A_a f,(I-P_a)f): H→H direct_sum ker(A_a)`

is unitary, with inverse `(g,d)→A_a*g+d`. The source norm is exactly the sum of
visible and defect squared norms. Equivalently `W_a` retains the entire coherent
residue register and is lossless before any outcome is read.

As a measurement on source `H`, use the two Kraus operators `P_a` and `I-P_a`.
Their squares sum to `I`, so total outcome probability is conserved. For input
`V_a f` with `||f||=1`, the visible probability is `1/a` and the other probability
is `1-1/a`. After projecting the residue and identifying the visible copy with
`H`, the unnormalized output is `a^(-1/2)f`; only **conditional on the visible
outcome** is the normalized state `f`. Calling the latter an unconditional
deterministic transport silently erases the failure sector.

Crucially, preserving the classical outcome record is not preserving all quantum
coherence. At `a=2`, the distinct input states `e_1,e_2` have equal visible
components `(e_1+e_2)/2` and opposite defect components `(e_1-e_2)/2`. Their two
postmeasurement density-matrix ensembles are identical. The coherent pair
recovers either state, but the measured/dephased instrument cannot distinguish
them. A partial trace over the residue register likewise erases general
coherences. There is an important restricted exception: on the known range of
`V_a`, `W_a V_a rho V_a* W_a*=rho tensor |a-1><a-1|`. Partial trace over that
fixed residue returns `rho` exactly. It is lossless for this promised input
subspace, not for arbitrary source inputs. No arbitrary-source reversible
quantum channel is manufactured by listing the complementary probability.

## 5. A specified continuum embedding: weak amplitudes are not strong transport

This section concerns the half-line; it does not identify the separate
factorial-clock pointed limit, a bilateral source, or a finite cyclic map.
For `h>0`, let `E_h:H→L²(R_+)` send
`e_n` to `h^(-1/2)1_[(n-1)h,nh)`. Write `P_h=E_h E_h*`, the cell-average
projection, which converges strongly to identity as `h↓0` (first check compact
continuous functions, then use density and `||P_h||<=1`). Let

`D_a f(x)=a^(-1/2)f(x/a)`.

This is a unitary dilation on `L²(R_+)`, not the sparse integer isometry.

**D3 (precise convergence/no-go, paper proved).** For fixed `a>1`,

`E_h A_a* E_h* = D_a P_h → D_a` strongly,

`T_(a,h):=E_h V_a E_h* → a^(-1/2)D_a` in weak operator topology,

`||T_(a,h)f||→||f||` for every `f`,

`||T_(a,h)f-D_af||²→2(1-a^(-1/2))||f||²`.

Consequently `T_(a,h)f` has no strong limit for any nonzero `f`, since its unique
weak limit has strictly smaller norm.

**Proof.** The first equality follows by matching all `a` output cells in each
block. Define `rho_(a,h)` as the indicator of the last length-`h` cell in every
length-`ah` block. Exactly

`T_(a,h) f = sqrt(a) rho_(a,h) D_a P_h f`.

For any compact continuous test `g`, its average against `rho_(a,h)` tends to
`(1/a)∫g`; partition the support into blocks and bound each block's error by
its oscillation. The bound `0<=rho<=1` extends this weak-* limit to every
`L¹` test by density. Apply it to the product of any two `L²` functions, and
use `P_h f→f`, to obtain the weak operator limit. The norm equality
`||T_(a,h)f||=||E_h*f||=||P_h f||` is exact. Combining it with the weak limit
gives the last squared-distance limit.

More quantitatively, on complete blocks contained in a fixed compact interval,
if `g` has modulus of continuity `omega_g`, the absolute block-average error
summed over length `L` is at most `L omega_g(ah)`, with a boundary remainder at
most `2ah||g||_infinity` when the interval is not a block union. This controls
the averaging step of the proof, not a uniform operator-norm limit.

There is nevertheless a weaker probability-observation limit:

`|T_(a,h) f|² dx → |D_a f|² dx`

against every bounded continuous multiplication observable. Indeed
`|T f|²=a rho |D_a P_h f|²`; the latter squared magnitude converges in `L¹` to
`|D_a f|²`, and the weak-* averaging gives the result. The weak Hilbert-state
limit has only `1/a` of that norm-square. Squaring a weak limit is not a valid
interchange. Thus smooth position statistics can agree while coherent vector
transport still fails sharply. This identifies the exact topology in which
an apparently successful continuum replacement can conceal lost information.

## 6. Phase, origin, conductor and refinement

Fix `eta in {+1,-1}`, integer frequency `k`, and integer residue origin `o`.
Define the normalized ket

`chi_(a,k,o,eta)=a^(-1/2)sum_(r=0)^(a-1)
                 exp(eta*2pi*i*k*(r-o)/a)e_r`.

The bra coefficient of authentic multiplication is

`(I tensor <chi|)W_a V_a
 = a^(-1/2)exp(-eta*2pi*i*k*(a-1-o)/a)I`.                 (P1)

All frequencies have squared amplitude `1/a`. Changing `eta` conjugates the
phase; shifting `o` multiplies it by `exp(eta*2pi*i*k*o/a)` relative to `o=0`.
The additive character factors through the unique quotient of size
`a/gcd(a,k)`; this is the declared finite conductor. Zero frequency is uniform.
The code represents phases as rational turns modulo 1, with no floating
complex numbers used as a phase certificate.

**P2 (mixed-radix character law, paper proved).** For `R=r+a s`,

`exp(eta*2pi*i*k*R/(ab))
 = exp(eta*2pi*i*k*r/(ab)) exp(eta*2pi*i*k*s/b)`.

The first factor is the Fourier twiddle with denominator `ab`; replacing it
by an `a`-character generally breaks the source map. At `(a,b,k,r,s)=(2,3,1,1,0)`,
the true phase is `1/6` turn and the naive product of frequency-one local
characters has phase `1/2` turn, although the normalized magnitudes agree.
Under a change of radix word, the correct character is pulled back along the
source permutation `C_(v<-w)` and remains the same function of `R`.

A stronger exact warning, for `a>=2`: the tensor-product character
`exp(2pi*i*(k_a r/a+k_b s/b))`, with `0<=k_a<a,0<=k_b<b`, is an additive character
of the cyclic source `R mod ab` iff `k_b=0`. To prove necessity, increment `R`
once without carry: its phase ratio is `exp(2pi*i*k_a/a)`. At the carry from
`r=a-1` to `r=0,s→s+1` it is that same ratio times `exp(2pi*i*k_b/b)`. A cyclic
character has one constant ratio, forcing `k_b=0`. Sufficiency follows from
global frequency `K=b k_a`. This does not contradict a CRT tensor-character
factorization: mixed-radix addition has carry, and CRT uses another map.

The normalized vector invariant under every residue translation is uniquely
`u_a` up to a scalar phase: invariance forces all coordinates equal, and unit
norm fixes their magnitude. Fixing their positive phase gives `u_a` itself.
Furthermore `u_(ab)` transports to `u_b tensor u_a`. This is a genuine universal
characterization of the uniform sector, but it is prime-blind and classical.
The half-density magnitude alone is not a new arithmetic selection principle.

## 7. Source energy has an exact refinement cocycle

Let `H0 e_n=(log n)e_n` on the self-adjoint diagonal domain

`D(H0)={f: sum_n (log n)² |f_n|² < infinity}`.

Finite-support sequences form a core. For every `a>=1`, `V_a D(H0)⊆D(H0)`:
`log(an)=log n+log a` and the square is bounded by twice the two squares.
Consequently on this common domain

`[H0,V_a]=(log a)V_a`,

which has a bounded extension to all `H`. Also `V_a*D(H0)⊆D(H0)`, and
`[H0,V_a*]=-(log a)V_a*` on the common domain. No illegal trace of an unbounded
commutator is being taken.

**E1 (bounded source energy defect, paper proved).** Under `W_a`,

`W_a H0 W_a* = H0 tensor I+B_a`,

where `B_a` is the bounded diagonal operator

`B_a(m,r)=log((a(m-1)+r+1)/m)`, `0<=B_a<=log a`.

The domain on the right is `D(H0 tensor I)`. To prove it, note
`m<=a(m-1)+r+1<=am`; the logarithmic difference is uniformly bounded. Then
diagonal entries establish the operator identity with exactly equal domains.
The terminal residue gives `B_a(m,a-1)=log a`; the first vacuum residue gives
`B_a(1,0)=0`. Thus dropping the register and replacing its whole energy by a
constant shift is false even though it is correct along the terminal multiplier.

For `j=b(m-1)+s+1` and `n=a(j-1)+r+1`,

`B_(ab)(m,r+a s)=B_b(m,s)+B_a(j,r)`.                       (E2)

This is the logarithm of the exact rational multiplicative identity
`n/m=(n/j)(j/m)`. It proves refinement coherence of the energy correction
without assuming independent residue characters or primeness.

The compressed diagonal energy is

`(A_a H0 A_a*)e_m = (1/a)log[(am)!/(a(m-1))!] e_m`.       (E3)

Indeed it is the average of the `a` actual logarithmic source entries. The
formula has the same domain as `H0` because its difference from `log m` is
bounded by `log a`. It is strictly smaller than `(log m+log a)e_m` for `a>1`.
Writing factorials as Gamma values is classical finite algebra and does not
derive the real-place completed Gamma factor or its analytic continuation.

**H1 (source-indexed prime-power half-density, paper proved).** For a rational
prime `p`, `r>=1`, and `q=p^r`,

`<e_1 tensor u_q, W_q [H0,V_p]e_(p^(r-1))>
 = (log p)/sqrt(q) = Lambda(q)/sqrt(q)`.

Every displayed ket lies in `D(H0)`. The commutator gives `(log p)e_q`; `W_q`
sends `e_q` to `e_1 tensor e_(q-1)`; the uniform inner product is `q^(-1/2)`.
With character `chi_(q,k,o,eta)` the same coefficient acquires exactly the phase
in (P1), with `a=q`. These are vector coefficients, not traces or positive Weil
forms. Mixed-radix refinement preserves them only with the transported character
and energy cocycle (E2).

**H2 (minimal arithmetic gate and counterfeit, paper proved).** The positive
integer multiplicative monoid has units `{1}`; its irreducibles are exactly
rational primes. Requiring the primitive source letter to be irreducible rejects
the fake letter 6 while retaining every repeated word `(p,...,p)`. This is the
minimal *one-letter irreducibility gate* in this specified monoid, not a theorem
that no other possible authentication predicate is smaller. The source carrier
and its multiplication law must already be authenticated; a mere metadata label
does not prove a physical carrier is this monoid.

Without this gate, `[H0,V_6]=(log6)V_6` and the uniform overlap give
`log6/sqrt6`, although `Lambda(6)=0`. Radix geometry cannot repair that mismatch.
Likewise a primitive letter 4 would give `log4/sqrt4`, whereas the legitimate
repeated-prime endpoint `2²` has `log2/sqrt4`.

An independent source formulation is the formal Dirichlet logarithm of the
constant coefficient source `a(n)=1`. Unique factorization gives

`log_* a = sum_p sum_(r>=1) (1/r) delta_(p^r)`.

At each finite endpoint only finitely many products occur, so this is a formal
identity without analytic convergence assumptions. Multiplying the coefficient
at `p^r` by `log(p^r)` yields `log p`; at 6 the coefficient is zero. The mutation
`a(6)=2`, all other input coefficients initially unchanged, produces connected
coefficient 1 at 6 and is detected by the existing independent exact logarithm.
The `1/r` repeated-prime weighting is essential; calling every prime-power
endpoint a new primitive generator doubles the coefficient at 4.

**H3 (prime-side distribution only).** The coefficients define the locally
finite positive measure on positive log-time

`mu_pp=sum_(p prime,r>=1) log(p)/sqrt(p^r) delta_(r log p)`.

Local finiteness follows because `r log p<=T` implies `p^r<=exp(T)`, hence only
finitely many integer endpoints. On `Re z>1/2`, its Laplace transform is
`sum Lambda(n)n^(-z-1/2)`, absolutely convergent by `Lambda(n)<=log n` and the
integral test. The classical Euler logarithmic derivative identifies this with
`-zeta'(z+1/2)/zeta(z+1/2)` there. H1 gives a source-resolved presentation of its
individual coefficients. It does not make this positive measure the completed
signed Weil distribution: signs, Gamma, completed poles, identity contact,
conductor and admissible test space remain separate source data.

## 8. Minimal defect factorization and composition

**D4 (canonical defect universal property, paper proved; classical).** Let
`A:H→K` be a contraction of Hilbert spaces. Put
`D_A=(I-A*A)^(1/2)` and `E_A=closure ran(D_A)`. Then

`f→(Af,D_Af): H→K direct_sum E_A`

is an isometry. If another bounded `E:H→L` satisfies
`||Af||²+||Ef||²=||f||²` for all `f`, there is a unique isometry
`J:E_A→closure ran E` with `E=J D_A`, and it is onto that closed range.

**Proof.** The norm identity is the definition of `D_A`. Polarization gives
`E*E=I-A*A=D_A²`. Define `J(D_A f)=Ef`; equality of norms makes this well-defined
and isometric, and extension by density gives existence, uniqueness and the
claimed range. Thus the necessary retained Hilbert defect is unique up to
unitary equivalence on its minimal closed range. For the coisometry `A_a`,
`D_A=I-P_a`, and its full reconstruction is onto as in D2.

For contractions `A:H→K`, `B:K→L`,

`I-(BA)*(BA) = (I-A*A)+A*(I-B*B)A`,

and a coherent defect for `BA` is the ordered pair
`(D_B A f,D_A f)`. D4 compares it isometrically to the minimal defect of `BA`.
It need not fill the entire ambient `E_B direct_sum E_A`: for `A=0`, the
`D_B A` sector is unused. Claiming an onto unitary onto unused sectors would
overstate the universal property.

One can therefore use actual objects and morphisms without inventing a universal
physical category. Objects are Hilbert spaces. A representative disclosed-loss
arrow consists of a contraction `A:H→K`, a specified environment `E`, and a
bounded `D:H→E` satisfying `A*A+D*D=I`. For categorical arrows use equivalence
classes under environment-unitary equivalence:
`(A,E,D)~(A,E',U D)` whenever `U:E→E'` is unitary. Composition is

`(B,D_B) after (A,D_A) = (BA, (D_B A,D_A))`

with environment `E_B direct_sum E_A`; this descends to equivalence classes
because replacing the two environments by unitaries replaces the composite
environment by their direct-sum unitary. The identity has zero environment.
Associativity and the unit laws hold on these classes via canonical rebracketing
and the zero-space unitary: for three arrows the retained tuple is
`(D_C BA,D_B A,D_A)` in either order. Before quotienting, this is a coherent
calculus rather than a strict category of the displayed triples. Minimalization
is unique on the closed defect range by D4; unused ambient sectors are not
silently identified by the environment-unitary equivalence. Source labels
and action-intertwining equations are additional restrictions on these arrows;
the norm identity alone supplies none of them. This construction is a standard
defect-operator/isometric-dilation instrument, not a new Weil positivity engine.

For the block coisometries specifically,

`A_b A_a=A_(ab)`, `P_(ab)<=P_a`,

and the source sectors

`P_(ab)f`, `(P_a-P_(ab))f`, `(I-P_a)f`

are pairwise orthogonal and sum to `f`. This is a concrete associative accounting
of which scales discarded what. It is also a finite Haar/multiresolution
decomposition; the connection to wavelets is mathematical, not a new claim of
physical instrument availability.

## 9. Compression preserves one response, not the future semigroup

**D5 (all successor moments, paper proved).** Write `h=aq+r`, `0<=r<a`. Counting
the `a-r` uncarried and `r` carried starting residues gives

`A_a S^h A_a*=(1-r/a)S^q+(r/a)S^(q+1)`.

In particular `A_a S^a A_a*=S` but
`C_a:=A_a S A_a*=(1-1/a)I+(1/a)S`. For every `a>=2`,

`A_a S² A_a*−C_a²=−(S-I)²/a²`,

a nonzero operator, for example on `e_1`. Reusing the compressed one-step map
therefore gives binomially dispersed futures instead of the source's exact
carry returns. The hidden interaction is visible in the universal identity

`A_a S² A_a*−(A_a S A_a*)² = A_a S(I-P_a)S A_a*`.

The right side is precisely the discarded sector's return to the visible sector.
It need not be positive because the source dynamics here is a unilateral shift,
not a positive covariance form. This calculation is the concrete obstruction
that the disclosed-defect category fixes: compose the coherent full map before
forgetting, or retain the memory required for exact future response. A diagonal
or finite passive observable reconstruction alone cannot silently supply the
missing source continuation structure.

## 10. Preservation ledger, verdict and provenance

| Map | Source/action preservation | Norm and phase | Future/limit/authority boundary |
|---|---|---|---|
| `W_a` | Exact one-based bijection; actions conjugated with carry | Unitary; all residue phases retained | Mathematical access only; no physical channel authorization inferred |
| mixed-radix `C_(v<-w)` | Same `(m,R)`, coherent for every finite word | Permutation unitary; characters must be pulled back | Equal endpoint does not erase history order |
| quotient-only `q_a` | Current quotient retained, source fibers collapsed | Classical observation; no Hilbert norm claim | Fails successor descent; full residue repairs this probe |
| `A_a` | Uniform block amplitude only | Norm `1/sqrt(a)` on `V_a` range; phase-sensitive siblings exist | Successor compression is not multiplicative |
| coherent `R_a` | Exactly reconstructs source with visible+defect components | Full norm and interference retained | Keeping only measured outcomes loses relative coherence |
| two-outcome `P_a,I-P_a` instrument | Preserves outcome probabilities, not arbitrary input state | Trace preserving after summing outcomes; cross sectors dephase | Postselected normalized branch is not unconditional transport |
| `E_h V_a E_h*` | Genuine injective source multiplier before embedding | Weak limit loses amplitude norm; position densities have another limit | No strong continuum dilation limit for nonzero states |
| prime-power H1 coefficient | Authenticated primitive `p`, history length `r`, endpoint `p^r` | Correct log and half-density, with declared Fourier phase | Prime-side coefficient only; full Weil source/sign not obtained |

The strongest invalidated assumption is that a correct present-time coarse
representation also determines the next lawful source evolution. It fails both
classically at `q_2(1)=q_2(2)` and linearly at the exact nonzero D5 memory term.
Keeping the coherent residue register removes that specific obstruction. It
does not remove physical-access, signed-Weil, or source-identification gaps.

The computational companion has exact basis maps, rational projection and
defect sectors, rational phase turns, prime provenance, and certified rational
log/square-root enclosures. Its tests compare existing carry routines, direct
source addressing, independent dense projection matrices, direct support counts,
and the existing Dirichlet logarithm. Controls include wrong one-based origin,
forgotten carry, naive digit swap, counterfeit composite, false independent
Fourier factors, missing complementary norm, dephasing mistaken for reversible
repair, and semigroup-preserving compression. A passing test is not an executed
infinity. Run `python -m unittest discover -s tests -p test_source_faithful_carry.py`.

Primary external sources checked during this round:

* Joachim Cuntz, [C*-algebras associated with the ax+b-semigroup over N](https://arxiv.org/abs/math/0611541),
  2006 preprint; [publisher record](https://ems.press/books/ecr/60/1196).
  The source establishes classical operator-algebra context. The paper's extra
  quotient, crossed-product and completion theorems are not asserted for our
  raw unilateral maps. Abstract/publisher metadata were retrieved; full HTML
  retrieval failed in this pass, so no uninspected theorem is used as a premise.
* Ola Bratteli and Palle E. T. Jorgensen,
  [Isometries, shifts, Cuntz algebras and multiresolution wavelet analysis of scale N](https://arxiv.org/abs/funct-an/9612003),
  *Integral Equations and Operator Theory* 28 (1997), 382–443. The retrieved
  primary abstract explicitly connects scale-N wavelets and Cuntz representations.
  We use it for attribution, not as a black-box proof of the formulas above.
* The Bost–Connes relation of `H0=log N` to the trace `zeta(beta)` is already
  attributed in the parent source dossiers. This work uses only the explicit
  diagonal commutator proved above, not the full Bost–Connes KMS theorem.

There is no independent novelty claim for the standard Hilbert, Fourier or
Dirichlet-log ingredients. New-to-project leverage is the exact combined
source/energy/norm/phase accounting and the small hostile witnesses exposing
which compression equations fail. A next verdict-changing statement must name
the specific signed source term or low/high Schur map it controls; a positive
residue norm or generic dilation theorem alone does not change that obstruction.
