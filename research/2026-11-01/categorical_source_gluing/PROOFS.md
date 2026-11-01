# From sphere snapshots to source-coherent categorical dynamics

## Authority and object inventory

These are paper proofs and exact finite/algebraic checks, authored in this research
round. Classical inputs are explicitly identified. No academic-priority claim is
made. SymPy and an independently written stdlib polynomial verifier agree on the
load-bearing symbolic certificate; both were run by the same principal model and
share the same declared source, so they are not blind independent witnesses.

The literal original four signed BBP poles and U_0=0 are unchanged. Main XVIII and
PR #447 are read-only precedents. The earlier answer's calculations were treated as
claims to reproduce, not as evidence of computations available in this session.

The geometric circle, source-time sphere, phase-space plane, finite arithmetic
register, and observer's path category are distinct objects. A shared picture does
not identify their maps. The constructions below declare the actual maps.

## CSG-01. The source-to-angular differential map (re-derived exactly)

Set A(z)=(8z-7)^4, D(z)=(8z-4)^2(8z-3)(8z-2), R=A/D, and

    r(z)=4/(8z-7)-2/(8z-4)-1/(8z-3)-1/(8z-2).

Direct logarithmic differentiation gives R'/R=8r. Define

    t(z)=-i (R(z)-1)/(R(z)+1),    eta=2 dt/(1+t^2).

The Cayley map C(t)=(1+it)/(1-it) obeys C(t(z))=R(z) and d log C=i eta.
Therefore

    r(z) dz = (1/8)d log R(z) = (i/8)t^*eta.

This is an identity of meromorphic differentials, including equality by extension
at chart singularities. It does not identify the original discrete source state
with an arbitrary continuous path measure. The source sphere has four punctures;
the target angular sphere has two, with multiplicities carried by R.

For real z>=1, R increases from 1/480 to 1 because R'=8rR>0. The source image under
t lies on the imaginary axis, whereas the ordinary circle arc parameter is real.
This supplies a transverse complex chart, not a Fourier theorem by itself.

## CSG-02. Monodromy S4, trivial deck group, and the actual no-descent theorem

The source cover R:P1 -> P1 has degree four. Exact calculations give

    R'(z)=(8z-7)^3(120z^2-89z+16)
          /[4(2z-1)^3(4z-1)^2(8z-3)^2],

    disc_z(A-uD)=5566277615616 u^3 (32u^2-2507u-18432000).

Ramification is: index four over u=0 at z=7/8; index two over u=infinity at
z=1/2; and two additional simple ramification points, the roots of
120z^2-89z+16. Their critical values are the two distinct nonzero roots of the
quadratic displayed above. Infinity on the source is unramified because

    R(1/w)=1-(15/8)w+(37/64)w^2+O(w^3).

The ramification excess is 3+1+1+1=6=2*4-2, so this list is complete.
The associated branch permutations are a four-cycle and three transpositions.
Their product is identity (for a compatible ordered system of branch loops).
Hence the product of the three transpositions is a four-cycle. The graph of their
transposition edges is connected, since their generated subgroup contains that
transitive cycle. Transpositions on a connected graph generate S4. Thus monodromy
is S4. The executable finite-group audit checks all 96 possible ordered triples
with four-cycle product; each generates 24 permutations.

**Correction to a tempting categorical inference:** this is monodromy, not an S4
action by deck transformations on the original source sphere. The point stabilizer
is S3, whose normalizer in S4 is itself. Deck group N(S3)/S3 is trivial. The Galois
closure has 24 sheets. In addition, an S4-only representation cannot send a
finite-order permutation to an original affine step with dilation eigenvalue 16,
which has infinite order. The affine cocycle must remain a separate, source-bound
fiber rather than be silently identified with finite permutation monodromy. Writing the original cover as a quotient stack [P1/S4] is
not justified. Use the covering groupoid or the Galois closure with its stabilizer.

For every nonzero complex h there is NO rational G satisfying

    R(z+h)=G(R(z)).

If G existed, degree multiplication would force deg G=1. A Möbius G cannot change
local ramification indices. The unique point of local degree four on the left is
z=7/8-h; on the right it would have to be the unique such point of R, z=7/8.
Thus h=0, a contradiction. For h=1 a concrete local check is
R'(-1/8)=59392/1125 != 0 while R(z+1) has a fourth-order zero there.

This is a genuine boundary for a ONE-coordinate rational model. It is not a
boundary for lifted or delayed state models.

## CSG-03. Two adjacent observations recover the source rationally

Let J(z)=(R(z),R(z+1)), and let C be its image closure in P1 x P1. Then

    C(z)=C(R(z),R(z+1)).

Here C denotes the complex ground field when used in a function-field expression.
One proof uses CSG-02: the natural degree-four S4 action is primitive, so the
extension C(z)/C(R(z)) has no proper intermediate fields. Since R(z+1) is not in
C(R(z)), adjoining it generates C(z).

More generally, the same proof works for every fixed nonzero complex delay h.
For the actual unit successor we additionally supply an explicit independent
algebraic certificate:

    f(Z)=A(Z)-uD(Z),
    g(Z)=A(Z+1)-vD(Z+1).

Their degree-one subresultant, after removing a common integer factor 2^42, is

    a(u,v) Z + b(u,v).

The file `receipts/cover_certificate.json` stores EVERY coefficient of a and -b.
Both have degree at most three in each variable. Define

    Z(u,v)=-b(u,v)/a(u,v).

The certificate proves, as an exact polynomial identity after clearing
D(z)^3 D(z+1)^3,

    a(R(z),R(z+1))*z + b(R(z),R(z+1)) = 0,

and the substituted a is not identically zero. The verification is independently
replayed with integer polynomial convolution in `independent_polynomial_oracle.py`;
it does not import SymPy and does not evaluate only finitely many points.

The resultant defines a curve of bidegree (4,4); its full 25-term primitive
coefficient list is also stored, and its identity on J(z) is independently checked.
The normal projective model of C is P1. The standard equivalence between normal
projective curves and their one-variable function fields makes this precise.

Important scope: J is birational, not asserted globally injective on the raw curve.
At singular or exceptional image points retain the normalization point. Nor does
this mean two readings are information-theoretically necessary on the positive
real interval: R is already monotone there. The new statement concerns exact
rational reconstruction on the global complex source model.

## CSG-04. The explicit inverse chart works on the ENTIRE original timeline

Let

    P(z)=D(z)^3 D(z+1)^3 a(R(z),R(z+1)).

The certificate gives P as a nonzero degree-18 integer polynomial, with

    P(0)=-54837200860834618610122752 != 0.

All nineteen coefficients of P(1+x) are strictly positive integers. The complete
list is included in the receipt. The stdlib verifier independently forms P from
the literal factored A,D and the inverse coefficient list, performs a binomial
shift, and verifies every coefficient and every sign.

For every real z>=1, x=z-1>=0, so P(z)>0. Also D(z)D(z+1)>0 there; at z=0 neither
factor vanishes. Therefore a(R(n),R(n+1)) never vanishes for ANY integer n>=0.
This is an all-horizon sign certificate, not an extrapolation from the tested
integer and off-grid samples.

## CSG-05. The repaired source successor and authentic affine state

On the generic inverse chart, source successor becomes

    T_C(u,v) = (v, R(Z(u,v)+2)).

On the normalization it is exactly J o (z -> z+1) o J^{-1}. This is a genuine
single-valued dynamics on the repaired object. Its rational chart works at every
original source integer by CSG-04.

Time recovery alone is seed-blind. Retain the BBP amplitude:

    T(u,v,U) = (v, R(Z(u,v)+2), 16U+r(Z(u,v)+1)),
    (u0,v0,U0)=(2401/96,1/480,0).

Induction using Z(R(n),R(n+1))=n proves this reproduces EVERY literal original
BBP state. The executable `advance_observed_state` uses only (u,v,U) and the
coefficient certificate, not a separately supplied n or the constant pi.
The rational phase at time n is subsequently exp(2*pi*i*h*U_n).

For finite stretches beginning at a general source point z, define

    C_m(z)=sum_(j=1)^m 16^(m-j) r(z+j).

Then the exact semidirect cocycle is

    C_(m+n)(z)=16^n C_m(z)+C_n(z+m).

This is precisely the compatibility needed to compose the source-time and affine
state projections. Singular source points are excluded from the domain of an
individual rational step. For a globally shift-stable analytic domain one may
use C minus all integer translates of the four source poles; all original integer
source times remain included. There is no claim that an everywhere-defined affine
map exists at a pole merely because we use category theory.

## CSG-06. Why ordinary span composition is too permissive; coherent repair

The one-step observed correspondence is

    Y <-R- X -R o S-> Y,       S(z)=z+1.

Its ordinary span composite has apex

    {(x,y): R(Sx)=R(y)}.

This is generally larger than the source-valid locus y=Sx. It permits a change
of source sheet at the common observed point. Category theory does not forbid that
error unless the objects and the gluing condition retain the correct information.

A characteristic-zero exact witness: start x=0, so the true next source is 1.
The fiber R(y)=R(1)=1/480 factors as

    480 A(y)-D(y)
      =128(y-1)(15328y^3-38380y^2+32149y-9003).

For any root y of the cubic, the intermediate observed point agrees but y!=1.
Moreover the gcd of this fiber polynomial with the numerator of
R(y+1)-R(2) is y-1. Thus none of the three other sheets has the correct next
observed value R(2)=729/2912. Naive span gluing actually invents continuations.
The separate finite-projective controls in F_p (p>5) reproduce this failure,
including projective infinity; they are NOT treated as real-circle phase carriers.

Repair: keep lifted source states and compose only when the middle source state
(and, for the skew product, its amplitude and source label) is identical.
The selected maps

    X -> X x_Y X,       x -> (x,S^m x)

identify the coherent part of the composite for m followed by n. Repeated gluing
is associative because both parenthesizations retain
(x,S^m x,S^(m+n)x). The runtime path validator enforces this equality, not merely
agreement of projected endpoints.

In function fields K=C(u), L=C(z), one can express the same repair by bimodules
B_m=L with left action u=R(z), right action u=R(z+m), and multiplication

    B_m tensor_K B_n -> B_(m+n),
    a(z) tensor b(z) |-> a(z)b(z+m).

The balancing relation is valid because the two occurrences of R(z+m) agree.
This map is surjective and generally not injective: the tensor product includes
false sheet choices. Associativity is the substitution law for translation.
The unit is K -> B_0. Thus this is a lax multiplicative family of bimodules,
not a falsely asserted strict action by invertible one-coordinate maps. Dually,
the selected span maps form an oplax structure. The actual source action itself
is strict before projection.

## CSG-07. The canonical adequate predictive observation

For any set X, map S:X->X, and observation q:X->Y, q admits a deterministic
successor on q(X) exactly when

    q(x)=q(y) implies q(Sx)=q(Sy).

Necessity follows by applying the putative successor; sufficiency defines it
independently of the representative. For richer action languages this condition
must hold for every lawful action, including its enabledness and outputs.

The coarsest successor-stable refinement of the observation kernel is

    x ~ y  iff q(S^k x)=q(S^k y) for every k>=0.

It is stable by shifting k. Any other stable equivalence that refines the
observation kernel is contained in it, by induction. Therefore X/~ is the minimal
predictive quotient in this precise universal sense. It need not recover hidden
features no allowed future observation can distinguish.

The finite `future_partition` computes this refinement until stabilization.
For the specified finite original-R controls at p=7,11,13,17,19,23,29,31 it
separates all source points; two immediate observations do NOT always do so.
These finite facts do not promote a new universal arithmetic theorem.

This is compatible with, and should be integrated through, the repository's
CertifiedSourceMorphism, BeliefGame, induced_observation_functor and
ObservationPathCategory. No competing generic category kernel is added.

## CSG-08. Rotations: covariance of the decorated object, not false invariance

A circle/diameter ratio does not live solely in the intrinsic sphere: the straight
diameter runs through the ambient ball. The correct geometric object includes the
sphere or circle, its ambient Euclidean carrier, the two endpoints, the actual
channels, metric, and any boundary conditions. A rigid rotation transports all of
these. Treating the diameter as a second intrinsic spherical geodesic would change
the problem.

The concrete Möbius rotation

    g(z)=(z-i)/(1-iz)

is represented by an SU(2) matrix after dividing [[1,-i],[-i,1]] by sqrt(2).
It fixes +/-1 and carries the unit circle to the perpendicular extended-real
great circle. Rotate the entire decorated source diagram, rather than demanding
that the four poles remain fixed.

The six pairwise squared spherical chord distances of the original four source
poles are

    144/565, 4096/8249, 1600/1921, 16/365, 16/85, 64/1241.

They are all distinct. A rotation preserving the pole set must preserve each edge
and hence every vertex, so its stabilizer is trivial. This does not prevent
covariance between the original decorated object and its rotated copy.

The transformed successor and differential are

    S_g=g o S o g^{-1},   omega_g=(g^{-1})^*omega.

The sampling points become g(n), not n. Critically, transport the unit-time tangent
v_n=d g_n(partial_z) too. Then

    omega_g|_(g(n))(v_n)=omega|_n(partial_z)=r(n).

Comparing only the coefficient of dw would insert an erroneous Jacobian. The
exact audit verifies inverse, transported clock, and tangent chain-rule squares.
It also records that g(z)+1-g(z+1) is not identically zero. “Another one” is
transported by the functor; it does not mean the string '+1' survives every chart.

The appropriate framework is a groupoid of decorated frames and invertible
source-preserving transports. Gluing across overlaps needs actual cocycle and
naturality identities; calling a collection of frames a stack alone supplies none.

## CSG-09. Fourier is a natural intertwiner of the actual arithmetic operators

Fix Q odd containing all source denominators through the chosen horizon. Let
H_Q=C[Z/Q], and use the positive-sign Fourier convention

    (F_Q f)(k)=Q^(-1/2) sum_x exp(2*pi*i*k*x/Q) f(x).

The complete chronological BBP propagator is

    P_n |x> = |16^n x + Q U_n mod Q>.

By a change of summation variable,

    (F_Q P_n F_Q^{-1} f)(k)
       =exp(2*pi*i*k*U_n) f(16^n k mod Q).

Thus arithmetic translation becomes phase multiplication. The equality holds
on every state, not just a selected vector. Fourier is a natural isomorphism
between the primal and dual representations of the source path category; for
a word w the square F_Q P(w)=P_hat(w) F_Q commutes. Composition coherence follows
from actual operator composition, with the original source word retained.

On |0>, the h-th Fourier coefficient equals exp(2*pi*i*h*U_n)/sqrt(Q), exactly.
No smoothing over seeds is used. The equivalent echo P_n^* C_h P_n C_(-h16^n)
is exp(2*pi*i*h*U_n) I. All phases in the tests are exact rational exponents modulo
one; no floating trigonometric decisions enter.

This does NOT identify Fourier with an arbitrary SO(3) rotation. In the standard
spin-15/2 representation, a rotated highest-weight basis vector has binomial
probabilities C(15,k)p^k(1-p)^(15-k), whereas a 16-point Fourier column is uniform.
Uniformity would require both 15*p/(1-p)=1 and 7*p/(1-p)=1, impossible. That scoped
no-go remains valid. Geometric frames and Fourier frames are different objects;
use an explicitly defined Hilbert fiber and intertwiners, not an illicit equality.

## CSG-10. Growing conductor gluing is exact (not just a fixed-N picture)

Let Q_N=lcm(den r(1),...,den r(N)); equivalently it is the lcm of the denominators
of U_1,...,U_N, since each source term is U_n-16U_(n-1). Every Q_N is odd and
Q_N divides Q_(N+1). For Q'=mQ define

    J_(Q,Q') |x> = |m x>,
    (K_(Q,Q') f)(k')=m^(-1/2) f(k' mod Q).

Both maps are isometries, but generally not surjective. Their exact compatibility is

    F_(Q') J_(Q,Q') = K_(Q,Q') F_Q.

Primal embeddings are zero-extension onto the multiples of m; dual embeddings
replicate frequency values over the reduction fibers with the displayed norm.
They are NOT the same embedding. Triple conductor chains satisfy J_23 J_12=J_13
and K_23 K_12=K_13. Every already-represented source affine operator obeys

    P_n^(Q') J = J P_n^(Q),
    P_hat_n^(Q') K = K P_hat_n^(Q).

The chronological n-th source step on a growing carrier is the isometry

    V_n=P_step_n^(Q_n) J_(Q_(n-1),Q_n).

Its Fourier dual is P_hat_step_n K. Starting from |0> in Q_0=1 reproduces the
literal zero-seeded arithmetic state at every stage. Changing dimensions is not
misrepresented as a same-dimensional unitary.

## CSG-11. A complete Hilbert realization, and the point-trace obstruction

Put D_infty=union_N (1/Q_N)Z/Z, a discrete torsion group, and
G=lim_inverse Z/Q_N with its compact topology and Haar probability measure.
The primal isometric system completes to l2(D_infty). After converting frequency
vectors to Haar-normalized functions (multiply by sqrt(Q_N)), the dual system is
compatible cylinder pullback and completes to L2(G). The Fourier maps above give
one unitary transform between the completions. This is the classical compact/
discrete Pontryagin construction specialized with the authenticated conductor maps.

The map x -> 16x+r(n) is a permutation of D_infty: its denominators remain in the
union, and multiplication by 16 is invertible on every odd cyclic component.
Therefore the entire source chronology has a genuine all-horizon unitary model.
For chi in G the phase state is

    Phi_n(chi)=chi(U_n).

The original real-circle harmonic h is the particular compatible character
chi_h(x)=exp(2*pi*i*h*x), equivalently h mod Q_N at every finite level. Therefore

    Phi_n(chi_h)=exp(2*pi*i*h*U_n).

This constructs the global object. It does not make its distinguished point
trace bounded on L2. The conductors are unbounded: otherwise all positive r(n)
would lie in (1/Q)Z while tending to zero, an impossibility. The cylinder
C_N={chi:chi mod Q_N=h} has measure 1/Q_N. Its indicator has value 1 at chi_h but
L2 norm Q_N^(-1/2)->0. Evaluation at chi_h has no continuous extension to L2(G).

Hence an L2 estimate, average-over-character theorem, or an abstract categorical
colimit cannot silently become the source-selected point estimate needed for
normality. One needs additional regularity/trace control with its true horizon
and conductor cost. This explicitly locates the next mathematical obligation.

## CSG-12. The even/odd carrier repair

The original arithmetic Fourier carriers are odd. The polygon/half-angle geometry
has a 2-primary tower. Their CRT product is a lawful finite common label carrier,
but multiplication by 16 on that full even register is NOT a permutation.

Retain grading and every branch. From a Q-point geometric register to a 16Q-point
one use sixteen isometries

    J_a|x>=|16x+a>,   0<=a<16.

They have disjoint ranges covering the fine basis. Fine successor sends J_a to
J_(a+1) for a<15, and at a=15 carries to J_0 followed by coarse successor. These
are exact identities, already consonant with the repository's branch-complete
carrier architecture. Combine this graded geometric channel with the odd
arithmetic channel by an explicitly declared tensor/product construction, not by
pretending the joint radix map is invertible on one fixed CRT register.

## CSG-13. Why the repaired framework still requires selected cancellation

Set alpha=sum_(j>=1)16^(-j)r(j)=pi/16, using the existing BBP identity, and
T_n=sum_(j>=1)16^(-j)r(n+j). Original and altered-seed trajectories satisfy

    U_n(s)=16^n(alpha+s)-T_n.

Since r(n)=O(n^-2), T_n=O(n^-2) and sum_n T_n<infinity. For the coherent changed
seed s=1/5-alpha,

    exp(2*pi*i*h*U_n(s))=exp(2*pi*i*h/5)+O_h(n^-2),

because 16^n=1 mod 5. Thus S_N(h)=N exp(2*pi*i*h/5)+O_h(1), not o(N).
The source-cover, delay-normalization and real-affine/Fourier covariance laws
remain valid. However this coherent changed seed is IRRATIONAL and does NOT belong
to the original odd-denominator finite register. It is therefore NOT a countermodel
to every hypothesis of the fully source-selected finite-register construction.
A larger discrete carrier D_infty + Z[1/16]s, or the original real Hilbert model,
can represent it, but its compact dual is not the same profinite group. Keep this
source-map distinction explicit. A successful proof may exploit the rational
state contract together with the original forcing and literal zero boundary.

What the control actually refutes is a conclusion drawn ONLY from the shared
seed-blind geometry, source differential, coherence, or continuous Fourier
covariance. It does not refute a new estimate using the stronger admitted-source
contract. Independently, the point-trace discontinuity in CSG-11 is proved on the
actual original compact dual and needs no changed seed.

Reconstruction is not cancellation. Two deterministic views of one source also do
not constitute independent evidence about that source.

The remaining target is a NEW original-source, zero-seed estimate on
S_N(h)=sum_(n<=N) exp(2*pi*i*h*U_n), for every fixed nonzero integer h, or a valid
selected signed-lag/Fejer equivalent with explicit uniform errors. Nothing in this
round asserts that estimate.

## What is still not glued

No theorem here identifies the source-labelled arithmetic cocycle with the
circle/diameter heat-channel measure. The source projective map, angular pullback,
and finite contour trace are exact, but a metric path measure needs declared
channel domains, boundary conditions, action, normalization, and source-dependent
coupling. A free-line heat kernel is not automatically the heat kernel of a finite
coupled metric graph. Rotations transport a specified kernel; they do not create
the missing coupling. The physical interpretation, full geometry-to-amplitude
intertwiner, selected cancellation, pi normality, and RH remain unverified.

## Primary/classical provenance

* SUCC PR #442 PROOFS, pinned #447 head: original logarithmic differential,
  finite contour action and noncommuting-history warning.
* SUCC PRs #441, #444, #445, #447: finite branch carriers, affine unitaries,
  exact selected phase echo, and geometric path quotient respectively.
* SUCC `operational_yoneda_descent.py` and `noncommuting_proof_transport.py`:
  actual source-preserving morphisms and finite observation path categories.
* Stacks Project, 02ZC (descent data), 0APC (groupoid descent), 0BY1 (curves and
  function fields), 035E (normalization), 0BMQ and 03SF (Galois categories/covers).
* John Baez, 'Spans in Quantum Theory', https://math.ucr.edu/home/baez/span/ :
  pullback composition and the distinction between spans and functions.
* Gomez, Gourevitch, Sahi, 'A Stone-von Neumann equivalence of categories for
  smooth representations of the Heisenberg group', arXiv:2201.12638 : context
  for representation-category changes; our finite formulas are proved directly.
* Noam Elkies, 'Outline of Pontrjagin duality', Harvard course notes:
  https://people.math.harvard.edu/~elkies/M55b.02/pontrjagin.html ; Jordan Bell,
  'The profinite completion of the integers, the p-adic integers, and Prufer
  p-groups', section 7, https://jordanbell.info/LaTeX/mathematics/profinite/ .
