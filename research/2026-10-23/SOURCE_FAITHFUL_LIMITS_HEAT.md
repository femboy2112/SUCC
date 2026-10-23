# Clock blow-ups, heat limits, and an exact discarded-carry defect

**Date:** 2026-10-23. **Parent:** `5e2ba04c8b4ab627b6b0add588609c347346a1a2`.
**Authority:** paper derivations and exact finite regression witnesses; no Lean
certification of the analytic statements and no physical measurement. Classical
results are reconstructed in source-labelled form. Independent academic novelty
is **UNVERIFIED**.

## Hole contract and inherited boundary

The target is to compare the *same finite integer-labelled cycles* under two
different limiting constructions, and determine whether deleting their residue
register commutes with heat evolution. The starting claim that a geometric
blow-up might recover real heat survives below. The stronger claim that uniform
residue projection intertwines the corresponding heat generators is refuted by
an explicit factor and a nonzero hidden coupling.

The hypotheses are `N_k -> infinity`, positive edge scales `epsilon_k`, and the
nearest-neighbor successor on `Z/N_k Z`. The weakest line-limit conditions are
`epsilon_k -> 0` and `L_k=N_k epsilon_k -> infinity`. This statement neither
assumes nor concludes signed Weil positivity. The cheapest falsifiers are a
wrapped pair in a metric ball, the parity character, and a single block-constant
basis state. The finite/computational boundary is exact rational clocks and
enclosed finite heat probabilities; the infinite lift is the proof below.

The inherited source files actually consulted are
`WITT_CARRY_OBSERVER_LIMIT.md` (LCW-10 factorial completion),
`REALITY_PIN_QUANTUM_GLOBAL.md` (RPQ-05 no continuous real SUCC decoding),
`witt_carry_learning.py`, and `completed_weil_transport.py` (already existing
Gaussian/Mellin completion with explicit source caveats). No archived source is
modified. The arithmetic Hilbert source is one-based `ell^2(N_{>=1})`; **this
heat construction instead uses finite cycles and their bilateral local limit**.
It is not an undeclared intertwiner from the one-based source.

## LH-01: explicit pointed geometric limit

Let `C_N=Z/NZ`, with vertex metric

`d_N(i,j)=min(|i-j|,N-|i-j|)`

using residues in `0,...,N-1`. Its scaled circumference is `L=N epsilon`.
For `L>4R`, every point in the closed radius-`R` ball about zero has a unique
signed representative `n` with `|n|<=floor(R/epsilon)`. The map

`iota(n)=epsilon n`

is an **exact isometry on that whole ball**, including pairwise distances:
`|n-m| epsilon<=2R<L/2`, so the shorter arc cannot wrap. Its image has Hausdorff
distance less than `epsilon` from `[-R,R]`, in their common ambient real line.
This proves pointed Gromov--Hausdorff convergence to `(R,|.|,0)` whenever
`epsilon_k->0` and `L_k->infinity`, with the displayed local-radius bound.

For `N_k=k!`, `epsilon_k=1/sqrt(k!)`, both conditions hold. For any specified
radius `R` and error `eta>0`, a sufficient exact threshold is

`k! > max(16 R^2, eta^(-2))`.

The roots in this paper statement are exact real numbers; the finite code uses
rational scales so it does not pretend a floating square root is a certificate.

**Hostile control.** `N=12, epsilon=1, R=4` satisfies `L>2R` but the pair `-4,4`
has real separation `8` and cycle distance `4`. Merely preventing individual
coordinates from wrapping is weaker than preserving all distances in a ball.

## LH-02: complete list of subsequential scale limits

Assume `N_k->infinity` and use *vertex metrics*, not metric graphs with filled
edges. The following limits hold:

| Scale behavior | Pointed limit |
|---|---|
| `epsilon_k->0`, `L_k->infinity` | real line |
| `epsilon_k->0`, `L_k->ell in (0,infinity)` | circle of circumference `ell` |
| `L_k->0` | point, even in unpointed GH topology |
| `epsilon_k->a in (0,infinity)` | lattice `a Z` with its usual distance |
| `epsilon_k->infinity` | point in pointed topology |

For the circle case, place the vertices on the circle of circumference `L_k`;
their mesh distance is at most `epsilon_k/2`. Rescaling that circle to
circumference `ell` has distortion at most `|L_k-ell|/2`. For collapse use
`diam(C_k)<=L_k/2`. For the lattice case each fixed finite set of signed labels
eventually has exactly the unwrapped distances, converging to those of `a Z`;
the number of labels in a fixed ball is uniformly finite. For the sparse case,
every fixed radius ball eventually consists only of the basepoint. Diverging
diameter does not prevent that *pointed* collapse.

These exhaust subsequential limits. Extract a subsequence with epsilon tending
in `[0,infinity]`; when its limit is zero, extract another with L tending in
`[0,infinity]`. The preceding cases cover every possibility. In fact the family
is pointed precompact: for fixed `R,eta>0` a cycle ball can be covered by a
number of radius-eta balls bounded by `4+4R/eta`, independently of mesh and
circumference. This follows by walking along the at-most-two arcs from zero,
placing a center every eta of arc, or at each vertex if epsilon>eta. Thus
oscillating scales can fail to converge, but **no nonprecompact scale regime
exists for this family of vertex cycles**. For example alternating
epsilon=`1/N` and `1/sqrt(N)` has circle and line subsequential limits.

The scale `1/sqrt(k!)` is one convenient choice. No successor or ring law in
these hypotheses selects it or supplies a physical length unit.

## LH-03: actions and exact finite horizon

For real `t`, choose `r_k(t)` nearest to `t/epsilon_k`, with any fixed tie rule.
Then `|epsilon_k r_k(t)-t|<=epsilon_k/2`. On an unwrapped ball,
`S_k^(r_k(t))` therefore converges uniformly to `T_t(x)=x+t`.
The point map `M_p[n]=[pn]` converges locally to `M_p(x)=px`: its error in
unwrapped coordinates is zero, provided `pR<L_k/2`.

More generally take a fixed finite word in translations and positive integer
multiplications. Starting with radius bound `R_0` and error `E_0=0`, update

* translation by t: `R_j=R_(j-1)+|t|`,
  `E_j=E_(j-1)+|epsilon r_k(t)-t|`;
* multiplication by p: `R_j=p R_(j-1)`, `E_j=p E_(j-1)`.

If `2(R_j+E_j)<L_k` at every stage (including stage zero), no intermediate
coordinate wraps and the declared error holds by induction. These are the
finite-horizon certificates implemented in `action_horizon`. Each fixed word
eventually meets them in the line regime. For all real x,t,

`M_p T_t(x)=p(x+t)=T_(pt) M_p(x)`.

The exact finite law is `M_p S^r=S^(pr)M_p`. Independently rounding `pt` need
not give exactly `p r_k(t)`; the limiting law must not be substituted as an
exact rounded finite identity.

On counting Hilbert spaces, the linear map `F_p e_n=e_(pn mod N)` has
`d=gcd(p,N)` equal-size fibers. Hence it has rank `N/d`, kernel dimension
`N-N/d`, and norm `sqrt(d)`. Its Gram matrix consists of all-one fiber blocks
and has nonzero eigenvalue d. When p divides N, `e_0-e_(N/p)` is a nonzero
kernel vector. Multiplying by `d^-1/2` gives a partial isometry, not the
injective arithmetic FUCC. Local injectivity of point maps does not repair
this global Hilbert distinction or the half-density defect proved in the
companion carry manuscript.

## LH-04: incompatible completions, with the common source retained

The authentic reductions `Z/(k+1)! -> Z/k!` give the profinite inverse limit
`Zhat`. This uses equality of fixed residue observations, not scaled shortest
path distances. The compactness proof of RPQ-05 remains valid: a continuous
`f:Zhat->R` with `f(x+1)=f(x)+1` would be bounded, yet
`f(n)=f(0)+n`. Alternatively `k!->0` profinitely while its ordinary real
values diverge.

The geometric charts are not compatible maps of that inverse system.
Their unit displacement is epsilon_k, which tends to zero. In particular,
every *fixed* integer label has geometric coordinate tending to zero, and a
fixed nonzero real translation uses a k-dependent power of successor. Neither
the limit space nor its action is a continuous unit-preserving decoder of
Zhat. This is exactly why LH-01 does not contradict RPQ-05.

There are honest common-source spans `Z -> Zhat` and `Z -> R`, and, after
declaring rational inversion, `Q -> Q_p` and `Q -> R`. They require their
separate topologies. There is no unital ring map from Q to a finite `Z/NZ`:
the invertible rational N would have to map to zero. Reduction of rationals
modulo N requires explicitly restricting denominators to units. The geometric
choice epsilon=`1/sqrt(k!)` is often irrational, so it is not silently a
diagonal rational-source coordinate either. Rational choices with the same
line-limit conditions are available, but remain choices.

## LH-05: local heat density with an explicit uniform error

Assume N is even, epsilon>0, and set `L=N epsilon`. On counting `ell^2(C_N)`
let

`A_(N,epsilon)=epsilon^(-2)(2I-S-S*)`.

Let `P_(N,epsilon)(t,n)` be its heat transition probability from zero to n.
The density relative to physical Lebesgue length is
`h_(N,epsilon)(t,n)=P_(N,epsilon)(t,n)/epsilon`, not P itself. Diagonalizing
the finite cyclic shift gives, with `xi_j=2 pi j/L`,

`h(t,n)=(1/L) sum_(j=-N/2)^(N/2-1) exp(-t lambda_epsilon(xi_j)) exp(i n epsilon xi_j)`,

`lambda_epsilon(xi)=4 epsilon^(-2) sin^2(epsilon xi/2)`.

This is the standard discrete-circle Fourier formula (Dowker, below), with
time and counting-density normalization made explicit. Let

`g_t(x)=(4 pi t)^(-1/2) exp(-x^2/(4t))`, `c=4/pi^2`.

For every t>0 and integer n, putting `x=n epsilon`,

`|h(t,n)-g_t(x)| <= epsilon^2/[32 sqrt(pi) c^(5/2) t^(3/2)]`

`                     + epsilon exp(-pi^2 t/epsilon^2)/(2 pi^2 t)`

`                     + [2/c+|x| sqrt(pi/(ct))]/L`.                 (1)

**Proof.** On the Nyquist interval `|xi|<=pi/epsilon`, elementary sine bounds
give

`c xi^2 <= lambda_epsilon(xi) <= xi^2`,
`0 <= xi^2-lambda_epsilon(xi) <= epsilon^2 xi^4/12`,
`|lambda'_epsilon(xi)|<=2|xi|`.

The lower bound uses concavity of sine on `[0,pi/2]`; the quartic error follows
from `cos u <= 1-u^2/2+u^4/24`, obtained from Taylor's formula or two integrations
of `1-cos u<=u^2/2`. For
`F(xi)=exp(-t lambda_epsilon(xi)) exp(i x xi)`, left-endpoint Riemann error
with mesh `2pi/L`, divided by `2pi`, is bounded by

`(1/L) integral |F'| <= [2/c+|x|sqrt(pi/(ct))]/L`.

Here `integral 2t|xi| exp(-ct xi^2)=2/c` over the real line.
The mean-value inequality for the exponential bounds the dispersion error by

`(t epsilon^2/(24pi)) integral_R xi^4 exp(-ct xi^2) dxi`

which is the first term of (1), since the integral is
`3 sqrt(pi)/(4(ct)^(5/2))`. The omitted Gaussian Fourier tail is at most the
second term, using
`integral_B^infinity exp(-t u^2)du <= exp(-tB^2)/(2tB)` with `B=pi/epsilon`.
The Fourier inversion of the Gaussian completes the proof. No limiting
interchange or fitted asymptotic estimate was used.

For an entirely rational, conservative certificate, if t>=a^2 with rational
a>0 and |x|<=R, the right side of (1) is at most

`epsilon^2/a^3 + epsilon/[18 a^2(1+9a^2/epsilon^2)] + (8+4R/a)/L`.   (2)

Use `3<pi<4`, `c>=1/4`, and `exp(-u)<=1/(1+u)`. The implementation returns
the three separate terms. Thus local heat densities converge uniformly for
`t>=tau>0` and bounded x whenever epsilon->0 and L->infinity. For the proposed
factorial scale, the dispersion error is `O((k!)^-1)` and the displayed
quadrature bound is `O((k!)^-1/2)` at fixed t and radius. These are bounds, not
claims of optimal rates.

## LH-06: embedded strong semigroups and resolvents

Assume explicitly that every N_k is even, as in LH-05 (factorial clocks satisfy
this from k=2). Represent each finite source in `L^2(R,dx)` by the isometry B_k that sends e_n
to `epsilon_k^(-1/2)` times the indicator of
`[n epsilon_k,(n+1)epsilon_k)`, for signed representatives
`-N_k/2 <= n < N_k/2`. Its range is a step-function space supported on
`[-L_k/2,L_k/2)`. Then for each t>=0 and every f in L^2(R),

`B_k exp(-t A_k) B_k* f -> exp(t d^2/dx^2) f` strongly,              (3)

and for every alpha>0,

`B_k (alpha+A_k)^(-1) B_k* f -> (alpha-d^2/dx^2)^(-1) f` strongly.   (4)

The real operator is the nonnegative Laplacian `-d^2/dx^2` with domain
`H^2(R)`. Equation (4) is **generalized embedded strong-resolvent convergence**,
not an assertion that the varying finite-dimensional operators share one
unchanged Hilbert space/domain.

**Proof.** For compactly supported f,g, both supports eventually lie inside
the embedding interval. The kernel of the left side of (3) equals the density
in LH-05 at the associated cell-address difference. The physical difference
`x-y` differs from that address by at most epsilon. The derivative of g_t is
bounded in absolute value by `1/t`, so (1), with radius increased by epsilon,
gives uniform kernel convergence on those supports. It follows that all such
matrix coefficients converge. Both finite and infinite semigroups are
contractions; density extends this to weak convergence for all f,g.

Write `T_k(t)=B_k exp(-tA_k) B_k*`. Since B_k is an isometry,

`||T_k(t)f||^2=<f,T_k(2t)f>`.

Weak convergence at time 2t gives convergence of these norms to
`<f,H_(2t)f>=||H_t f||^2`. Weak convergence plus norm convergence in Hilbert
space gives (3) strongly. At t=0 the operators are expanding step projections,
which converge strongly to identity by approximation of continuous compactly
supported functions. Finally integrate (3) against `exp(-alpha t)dt`;
contraction bounds give Bochner dominated convergence and (4). QED.

This proof supplies the requested operator limit without importing an
unverified Mosco or norm-resolvent theorem. Operator-norm convergence is not
claimed. A finite-rank operator cannot converge in norm to the noncompact
real heat semigroup at t>0: translate a fixed nonzero localized input beyond
the embedding interval to witness a nonvanishing norm error.

## LH-07: heat, Fourier and the real Gamma factor

Use Fourier transform `F_+ f(xi)=integral_R f(x) exp(2pi i x xi) dx` and its
inverse with a minus sign. Then `F_+ g_t(xi)=exp(-4pi^2 t xi^2)`. At the
**specified** time `t_*=1/(4pi)`, `g_(t_*)(x)=exp(-pi x^2)` is self-dual.
This time is fixed by the chosen Fourier convention and coordinate scale; it
does not derive a physical unit from the abstract successor source.

For `Re(s)>0`, absolute convergence at zero and infinity permits the ordinary
change of variables `u=pi x^2`, giving

`integral_(R*) exp(-pi x^2) |x|^s dx/|x|`
` = 2 integral_0^infinity exp(-pi x^2) x^(s-1) dx`
` = pi^(-s/2) Gamma(s/2) = Gamma_R(s)`.

For arbitrary t>0 the same Mellin transform of g_t is instead
`(4pi t)^((s-1)/2) Gamma_R(s)`. That explicit free scale factor is a control
against announcing normalization from an arbitrarily selected heat time.
This is a recovery of classical Tate mathematics, already present in another
form in `completed_weil_transport.py`, not a new derivation of the completed
Weil sign or a physical constant.

## LH-08: rational characters survive, but their heat scales do not

Choose the global rational-source character convention

`psi_infinity(x)=exp(2pi i x)`,
`psi_p(x)=exp(-2pi i {x}_p)`.

For rational x, `x-sum_p {x}_p` is an integer, so the product of local
characters is one. A finite exact proof writes `x=a/b` in lowest terms; for
each prime-power factor `p^v||b`, take the residue
`r_p = a (b/p^v)^(-1) mod p^v`. Then `{x}_p=r_p/p^v`. CRT says
`a-sum_p r_p(b/p^v)` is divisible by b. The supplied test implements this
independently on signed rational sources and rejects the wrong finite sign
(already at x=1/6).

With Haar measure `vol(Z_p)=1` and this conductor-Z_p character, `1_(Z_p)` is
self-Fourier: its integral against a character is one for y in Z_p and zero
otherwise, the latter by translation by an element that changes the character.
With multiplicative Haar measure giving units volume one, the local Mellin
integral of `1_(Z_p)` is `sum_(r>=0) p^(-rs)=(1-p^-s)^(-1)` for `Re(s)>0`.
The usual rational absolute-value product formula follows independently from
prime factorization of numerator and denominator. These compatible
conventions support Tate's classical global construction. The geometric
blow-up alone does not force their character sign, Haar scale or global use.

There is also a sharp obstruction to a stronger proposed commuting diagram.
Fix a nontrivial rational source character `theta in Q/Z`. At every factorial
level with denominator(theta) dividing k!, the *same* profinite character is
`chi_theta(n)=exp(2pi i theta n)`. It is a heat eigenvector with eigenvalue

`4 epsilon_k^(-2) sin^2(pi theta) -> infinity`.

Thus every fixed positive heat time kills its normalized eigenmode amplitude
in the blow-up regime. A fixed finite real frequency, in contrast, uses source
frequencies tending to zero and usually increasing conductor. The conductor-2
parity vector gives the exact eigenvalue `4/epsilon_k^2`. Hence a diagram that
simultaneously preserves **fixed profinite character labels** and **finite
Archimedean heat frequency** cannot commute on every nontrivial character.
This is a source-frequency defect, not failure of either Fourier theory.

## LH-09: exact uniform-register compression gives the wrong generator

Now use the bilateral Hilbert source `ell^2(Z)` and bounded nearest-neighbor
Laplacian `A_epsilon=epsilon^-2(2I-T-T*)`. For any integer a>=2, define the
uniform-residue embedding

`J_a e_m = a^-1/2 sum_(r=0)^(a-1) e_(am+r)`.

It is an isometry. Its adjoint averages blocks with factor `a^-1/2`. Direct
block-edge calculation gives

`J_a* A_epsilon J_a = (1/(a epsilon^2))(2I-T-T*)`
`                       = a A_(a epsilon)`.                       (5)

**Proof.** The constant value inside each block cancels at all interior
nearest-neighbor differences. Exactly one fine edge crosses each coarse
boundary. The two endpoint contributions, after averaging, give diagonal
`2/a` and adjacent entries `-1/a` before restoring epsilon^-2. QED.

Let `Q_a=I-J_a J_a*`. On the normalized coarse basis vector e_0,

`||Q_a A_epsilon J_a e_0||^2 = epsilon^-4 (4a-6)/a^2 > 0`.         (6)

Indeed `A_1 J_a e_0` has four nonzero endpoint entries of magnitude
`1/sqrt(a)`, giving squared norm `4/a`; its visible projection has squared
norm `6/a^2`. Pythagoras proves (6). At a=2 the hidden norm squared is 1/2.
Finite cyclic calculations with at least three coarse blocks give the same
entries and supply exact regression witnesses; no floating sqrt is required.

For fixed epsilon the bounded-operator Taylor expansion gives

`J_a* exp(-t A_epsilon) J_a - exp(-t J_a* A_epsilon J_a)`
` = (t^2/2) J_a* A_epsilon Q_a A_epsilon J_a + O(t^3)`              (7)

in operator norm as t->0. The coefficient is nonzero by (6). The remainder
constant depends on epsilon; (7) is not used as a uniform continuum estimate.
Equation (7) is an explicit falsifier of the supposed exact heat intertwiner.

There is a stronger **noncommuting continuum limit**. Fix a>=2 and take even
coarse sizes M_k->infinity, epsilon_k->0, with `a M_k epsilon_k->infinity`.
Use aligned left-edge cell embeddings so
`B_(epsilon_k) J_a = B_(a epsilon_k)` exactly. Full fine heat, compressed only
after evolution, has the strong real limit

`B_(a epsilon) J_a* exp(-t A_(aM,epsilon)) J_a B_(a epsilon)* -> H_t`.

To see this, the left side is `P_coarse T_fine(t) P_coarse`; the coarse step
projections tend strongly to identity and LH-06 gives `T_fine(t)->H_t`.
But compressing the generator first gives, by (5) and LH-06,

`B_(a epsilon) exp(-t J_a* A_(aM,epsilon) J_a) B_(a epsilon)* -> H_(a t)`.

These limits differ for every a>1 and t>0 on, for example, a Gaussian input:
their Fourier multipliers are `exp(-4pi^2 t xi^2)` and
`exp(-4pi^2 a t xi^2)`. **Removing the carry environment before exponentiating
changes the limiting diffusivity by exactly a.** Keeping the complete
polyphase register removes this particular defect by unitary conjugation;
simply retaining its uniform component does not.

The source of the discrepancy is identified rather than attributed to mystery:
the uniform block subspace is not invariant under the fine generator. If
`u(t)=J_a* exp(-tA)J_a f` and the hidden initial component is zero, write
`A_v=J_a*AJ_a`, `B=J_a*AQ_a`, `D=Q_a A Q_a` on their declared subspaces.
Solving the hidden equation exactly gives

`u'(t)=-A_v u(t)+integral_0^t B exp(-(t-s)D) B* u(s) ds`.

This is the elementary projection-memory equation, with bounded A at each
fixed epsilon. Deleting the integral gives the incorrect generator evolution.
Its Laplace counterpart is the exact Schur correction
`alpha+A_v-B(alpha+D)^(-1)B*`, alpha>0. These are familiar projection and
Schur mechanisms, not a positivity bridge to the signed arithmetic source.

## Scholarly provenance and status

* J. S. Dowker, *Heat-kernels on the discrete circle and interval*,
  [arXiv:1207.2096v2](https://arxiv.org/pdf/1207.2096), sections 2--3,
  equations (5)--(10), supplies the classical integer Bessel kernel and circle
  image/Fourier formulas. It also treats character twists. Our local error
  bound and embedded convergence proof are written out above and do not rely
  on its numerical evaluation.
* Bjorn Poonen, [*Tate's thesis*, MIT 18.786 notes](https://math.mit.edu/~poonen/786/notes.pdf),
  section 1 and the local zeta-integral sections, provides the Fourier/Gaussian
  and local-factor conventions. The Gaussian Mellin identity here is directly
  proved by substitution. This exposition is attributed to Tate's classical
  work, with Poonen's authored notes used to check normalization.
* J.-F. Burnol, [*On Fourier and Zeta(s)*](https://arxiv.org/pdf/math/0112254),
  section 2, emphasizes normalized additive character/Haar data in the local
  Fourier identities. It is background for the source-normalization boundary,
  not an invoked proof of any new signed Weil claim.
* Existing repository papers already prove factorial profinite completion,
  the continuous-SUCC obstruction, and a source-indexed Gaussian/Mellin bridge.
  Those results are not renamed as new discoveries. The explicit heat
  error/embedding proof, fixed-conductor obstruction, and block compression
  witnesses are **new-to-project derivations and implementation**; no priority
  claim against classical coarse-graining/projection theory is made.

## Source-preservation ledger

| Map or limit | Preserved | Discarded, changed, or unavailable |
|---|---|---|
| `Z->C_k`, authentic reductions | finite residue ring, integer SUCC/multiplier maps | full integer label, injective Hilbert FUCC |
| inverse limit `C_k->Zhat` | all compatible finite congruence information | real metric and physical scale are not supplied |
| pointed blow-up charts | finite local distances and declared rescaled point actions | fixed integer unit becomes infinitesimal; reductions are not intertwined |
| cell embedding B_k | Hilbert norm and heat density normalization | finite range omits remote positions; no norm convergence on all L2 inputs |
| full polyphase register | every source state and fine heat action | physical access is not established |
| uniform projection J_a* | visible block coefficient | hidden coupling (6), memory term, and exact future heat action |
| Gaussian/Mellin | classical real Fourier/Mellin identity in `Re(s)>0` | absolute length unit; completed poles/contact and signed Weil comparison |
| fixed-conductor character refinement | authentic rational finite character | finite real heat frequency in blow-up; eigenenergy diverges |

## Validation, refutations and next theorem

`observational_succ/source_faithful_limits.py` contains only exact integer or
Fraction inputs for certification. Heat probabilities use Poisson
uniformization with a geometric tail bound, exponential intervals use a
positive Taylor tail with range reduction, and Gaussian intervals use Machin
pi brackets and integer-square-root enclosures. Independently derived four-cycle
closed forms, explicit block vectors, parity eigenvectors, probability mass,
and wrong-sign/wrong-scale mutations calibrate those routines. Finite checks
do not certify the universal analytic claims above.

The refuted identifications have exact receipts: `L>2R` is insufficient for
pair distances; epsilon=`1/N` yields a circle; cyclic multiplication has a
kernel; transition mass is not Lebesgue density; fixed conductor is not fixed
real frequency; uniform-residue generator compression is not heat transport.

The Weil obstruction is unchanged by this lane. No equality between these
positive heat forms and the original signed completed Weil distribution has
been established. The initial next target, a **uniform resolvent bound for
the exact hidden-register Schur correction** on a low physical-frequency band,
was subsequently closed in the same research round; see
[the resolvent-memory supplement](SOURCE_FAITHFUL_RESOLVENT_MEMORY.md). It
recovers the missing diffusivity `(a-1) xi^2` quantitatively for every fixed
radix a. The next boundary is a growing radix/environment dimension, where
those fixed-radix constants are no longer uniform.
