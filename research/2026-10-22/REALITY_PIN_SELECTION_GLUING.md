# Reality Pin: quantitative selection, constructive RC learning, and lawful gluing

Date: 2026-10-22. Parent source: PR #243 at
`d2f760ab9d9a11719e950caeb2d54bfa5114f495`; prior boundary theorem: PR #242
at `146ddf514f05928158b38f0d8216b45df13dc92b`.

**Status:** paper proofs using classical compactness, monotonicity, and Schur
elimination; exact finite tests; synthetic experiment only. No new mathematical
originality, actual instrument reading, or Lean certification is asserted here.
The source family, source identity, instrument calibration, and availability of
probes are separate assumptions. The code cannot authenticate these assumptions.

## 1. Hole contract and the new edge

The inherited construction gives interval selection and a qualitative compact
inverse theorem. The missing edge addressed here is **an operational resolution
budget**: which finite probes and precision suffice, what convergence can be
constructed, and how errors behave under actual interface composition?

We prove a countable-probe compact selection theorem with an inverse modulus,
give an effective RC instance with a stated resolution bound, and prove a block
perturbation estimate for Schur gluing. We also identify the extra assumptions
needed to turn the compact theorem into an algorithm. This is a strengthening
of the research interface, not a new general solution of inverse problems.

Cheapest falsifiers: nonseparating probes, a noncompact family, fixed nonzero
errors, wrong source labels, an omitted dark sector, or an interior eigenvalue
approaching zero. All remain explicit failure conditions below.

## 2. Finite model family: the sharp box-separation condition

Let a predeclared finite family have model identities i, gauge classes [i],
computed values a_ij, and componentwise theoretical error bounds t_ij >= 0.
For an actual model i*, assume a true observable vector z satisfies
|z_j-a_i*j| <= t_i*j. The reading y satisfies |y_j-z_j| <= e_j.
The surviving fiber is

    V(y) = {i : |a_ij-y_j| <= t_ij+e_j for every measured j}.

**RP-S1 (finite identification).** The true model survives. If, for every pair
in different gauge classes, some measured coordinate j satisfies

    |a_ij-a_lj| > t_ij+t_lj+2e_j,

then V(y) lies in exactly one gauge class.

**Proof.** The true model survives by the triangle inequality. If both i and l
survived, the triangle inequality through y_j would give the reverse non-strict
inequality at every coordinate, a contradiction. The strict condition is sharp
for independent closed coordinate-error boxes: at equality the two expanded
intervals can meet. More generally two product boxes intersect iff every pair
of corresponding coordinate intervals intersects. Thus the pairwise condition
is also necessary for the expanded boxes of each cross-class pair to be
disjoint. It is not necessary for uniqueness at one particular observed y. QED.

Gauge equivalence must be independently specified. Declaring every model to be
one gauge class makes the conclusion vacuous. Likewise deleting inconvenient
models can manufacture uniqueness: the direct and series RC models below have
the same DC response. Restricting the family to the direct model yields a
singleton without having distinguished the real source.

`PinPlan.digest()` commits the exact prediction values, uncertainty budgets,
source ID and probe IDs. It catches mutation of a recorded plan. A digest does
**not** prove when the plan was made, that a physical apparatus exists, or that
the data are independent. A real experiment needs an independently dated plan
and retained raw observations. Synthetic runs are labelled as such.

## 3. Compact family: finite resolution from countably many probes

Let X = M/~ be a compact metric space with distance d. This is an assumption
about a legitimate physical gauge quotient, not a consequence of writing '~'.
Let f_j:X -> [-1,1], j >= 1, be continuous, gauge invariant, and jointly
separating. Define

    D(x,x') = sum(j>=1) 2^-j |f_j(x)-f_j(x')|/2.

Uniform convergence makes D continuous on X x X; joint separation makes it a
metric. Define the canonical inverse modulus

    omega(t) = max{d(x,x') : D(x,x') <= t}.

**RP-S2 (finite-prefix stability).** The maximum exists, omega is monotone, and
omega(t) -> 0 as t -> 0. If the first m observations have total error <= eps,
and both the true source and a survivor satisfy the observation bands, then

    d(x,x*) <= omega(eps + 2^-m).

Consequently every desired resolution rho > 0 admits finitely many probes and
a positive precision budget that force all survivors within rho of the truth.

**Proof.** The admissible pair set defining omega is nonempty (it contains the
diagonal) and compact, so the maximum exists. If omega(t_n) failed to approach
zero for t_n -> 0, compactness would give a convergent subsequence of maximizing
pairs with d bounded below but D = 0 at the limit, contradicting separation.
For j <= m two survivors differ by at most 2 eps in f_j; their contribution to
D is <= eps sum(j<=m)2^-j <= eps. The unobserved tail is <= 2^-m.
The bound follows from the definition of omega. QED.

An equivalent finite-resolution proof uses the compact set
{(x,x'):d(x,x')>=rho}: for every such pair some probe differs, a finite subcover
supplies a finite probe set with a positive separation margin. This is why a
countably infinite separating language can supply finite **approximate**
identification without supplying finite exact identification.

**RP-S3 (learning limit).** Suppose at stage n the first n probes are available
with certified total errors eps_n -> 0, and the true source is fixed and
contained in the family. Any choice x_n from the stage-n survivor set converges
to x*. Intersecting all previous bands produces nested nonempty compact version
spaces with the same singleton intersection. The cost at stage n is n probe
evaluations at precision eps_n, in addition to the cost of computing model
predictions and finding a survivor.

**Important constructive boundary.** Bare compactness does not compute omega,
the required n, a survivor, or a physical error-reduction schedule. To get an
effective algorithm one needs effective compactness, evaluable probes with
error bounds, an effective inverse modulus or certified parameter subdivision,
and actual source/instrument access at the required precision. Threshold
equality also prevents naive finite-precision membership decisions. The next
section gives a complete computable special case using outer interval covers.

**Counterexamples.**

1. For X = {0,1}^N and coordinate probes, every finite probe list leaves
   continuum-many compatible infinite sequences, even though the full language
   separates and X is compact. Finite exact stopping is not implied.
2. For X = {0,e_1,e_2,...} in the norm metric of l2 and coordinate probes,
   f_j(e_n) -> f_j(0) for every fixed j but ||e_n||=1. The family is not compact
   in that metric. Coordinate convergence is not source-norm convergence.
3. In the source of eventually-zero binary sequences, every finite prefix of
   the all-one sequence is source-realizable, but the completed all-one record
   has no original-source representative. Closure/source realization is an
   independent obligation, as already established in SUCC's VOYAGER work.
4. Locally admissible records with alternating first bit are not compatible
   records and have no limit. A collection of local models is not a projective
   family merely because each member exists.
5. Nonvanishing measurement or theory error may leave a positive-diameter
   limiting fiber. More repetitions do not remove an unbounded systematic bias.

## 4. A constructive continuous RC family with a quantitative rate

Consider a one-port path: boundary -- g -- internal capacitor C=1 -- g --
ground, with both conductances equal and unknown g in [1,2]. At real Laplace
parameter s >= 0 the normalized admittance is

    f_s(g) = g(g+s)/(2g+s).

Its derivative is

    f_s'(g) = (2g^2+2gs+s^2)/(2g+s)^2,
    1/2 <= f_s'(g) <= 1.

The lower bound follows after subtracting half the denominator numerator:
the remainder is s^2/2 >= 0. The upper bound follows by direct subtraction.
Thus this declared one-parameter family is globally identifiable from one exact
reading and obeys |g-g'| <= 2|f_s(g)-f_s(g')|. This does not identify arbitrary
RC networks; equality of the two resistances and known C are source assumptions.

**RP-S4 (constructive observer).** Subdivide [1,2] into dyadic intervals of width
h=2^-r. Retain [a,b] iff [f_s(a),f_s(b)] meets [y-eps,y+eps]. This finite outer
cover contains every feasible conductance, including the true one under a valid
error budget. Its total span is at most 4eps+2h.

**Proof.** Monotonicity gives the exact image of every interval. The exact
feasible set is an interval whose image length is at most 2eps; the derivative
bound gives length at most 4eps. Every retained subdivision cell intersects
this feasible interval. The outer cover extends it by at most one cell on each
side. QED.

At stage r take eps_r=2^-r and h_r=2^-r. The surviving span is <= 6*2^-r and
converges to one g. Each stage uses one source reading at the specified accuracy
and at most 2^(r+1) exact rational endpoint evaluations, with at most 2^r stored
intervals in this simple implementation. No infinite physical completion is
claimed. A more efficient branch-and-bound algorithm is optional; this one is
already constructive and calibrated by exact tests.

## 5. Predeclared modest RC experiment with tolerances and a held-out response

Use reference units R*=1 kilohm and C*=1 microfarad, so G*=1 millisiemens and
time unit R*C*=1 millisecond. All code values are dimensionless. Two candidate
**topology families** are fixed before the synthetic readings:

* Direct: boundary-to-ground conductance in [0.495,0.505].
* Series-capacitor: two conductances and midpoint shunt capacitance each in
  [0.99,1.01]. The grounded endpoint and capacitor reference are specified.

For component values a,b,c > 0,

    Y(s) = a(b+sc)/(a+b+sc).

It is coordinatewise increasing: its derivatives in a,b,c are respectively
(b+sc)^2/(a+b+sc)^2, a^2/(a+b+sc)^2, and s a^2/(a+b+sc)^2. Hence evaluating
the two opposite corners gives an exact uncertainty interval over the whole
continuous component box; testing only corners is justified by this proof.

The frozen probe list is DC, s=1 (calibration/selection), and s=3 (held out).
The direct interval is [99/200,101/200] for all probes. The series intervals
are, respectively, [99/200,101/200], [33/50,101/150], and [99/125,101/125].
Per-probe calibrated observation error is declared <= 1/500. The dynamic
intervals are separated far beyond the error margin; DC cannot separate them.

The script freezes the entire plan and its SHA256 before generating data from
the off-center component triple (201/200,199/200,501/500). Exact readings are

    Y(0) = 39999/80000,
    Y(1) = 401397/600400,
    Y(3) = 804201/1001200.

DC leaves both topology families. Calibration selects series-capacitor. The
previously fixed held-out probe independently tests its predicted interval and
also rejects direct. No component is fitted from the calibration datum. This
selects a topology family with a continuous tolerance fiber, **not** one exact
component realization. For exact parameter recovery use an appropriate
separating family, such as the constrained one-parameter family above or the
full inherited path response with its source hypotheses.

The executable plan types this result as `identification_scope=topology_family`
and returns `unique_gauge_within_family=false`. Component-tolerance variation is
not silently declared to be a physical gauge symmetry. For genuine
`model_gauge` plans the supplied grouping must be justified independently.

### What a real measurement would require

Real s > 0 is a Laplace parameter, not an AC drive frequency. One defensible
implementation applies a known voltage step V0 to the boundary from a zero
initial capacitor state, measures the resulting current, and computes

    Y(s) = (s/V0) integral(0,infinity) exp(-st) i(t) dt.

The RC source equation gives i(t)/V0 = ab/(a+b) +
a^2/(a+b) exp(-(a+b)t/c). This derives the response above without treating real
s as an oscillator frequency. A finite record must include tail, quadrature,
current, voltage and time-base uncertainty in its calibrated budget. For a
normalized bound |i(t)/V0| <= M and a record ending at T, the omitted tail is
<= M exp(-sT). Here M <= 101/100. At sT >= 12 it is < (101/100)/4096, since
e > 2. Thus a **proposed**, unverified budget is: tail <= 1/4000, quadrature
<= 1/4000, time-base/step calibration <= 1/2000, current/voltage calibration
<= 1/1000, totaling 1/500. Each bound needs a real calibration certificate;
the script supplies none. DC requires its own settling/drift certification.

The s=3 reading must use a reserved independent acquisition or an explicitly
modelled covariance if taken from the same time trace. Sharing one calibrated
sensor can share systematic error; no claim of statistical independence follows
from using two mathematical transform parameters. The deterministic bounded-
error theorem does not require independence, but independent validation does.

## 6. Boundary-only gluing with actual maps

For a real symmetric finite energy matrix L, ordered boundary B, and interior
I, write

    L = [[C, B0^t], [B0, A]],  A > 0.

For imposed u the unique stationary/minimizing interior is
v = -A^-1 B0 u. Substitution gives boundary energy (1/2)u^t Lambda u and flux
j = Lambda u, where Lambda=C-B0^t A^-1 B0. For passive source networks L is
positive semidefinite; the algebraic identity only needs A invertible.

**RP-C1 (trace-map gluing).** Let component interiors be disjoint with no
cross-interior interaction. Fix actual linear trace maps T_i from a shared
boundary potential space to each component's boundary: u_i=T_i u. The total
energy is the sum, and

    Lambda_total = sum_i T_i^t Lambda_i T_i.

**Proof.** The full interior block is block diagonal, so each interior
minimizes independently. Substitute the component harmonic extensions into
the summed energy. Differentiation with respect to u gives the displayed
flux. This also proves the power identity
u^t j_total=sum_i u_i^t j_i. QED.

Ordinary interface identification uses 0/1 trace matrices. Signed or scaled
maps describe independently specified coordinate orientation/transformers;
they cannot be silently added after observing disagreement. A naive sum is
valid only when all T_i are the same identity in the same coordinates. A source
coupling between supposedly private interiors adds off-diagonal blocks and
invalidates the independent-sum assumption.

**RP-C2 (elimination order).** Partition private variables into I1 and I2.
If the full private block is positive definite, eliminating I1 then I2,
eliminating I2 then I1, and eliminating both at once give exactly the same
boundary response and the same full harmonic extension.

**Proof.** Completing the square first in I1 replaces the energy by its unique
minimum over I1. The residual private block on I2 is positive definite (evaluate
the positive original form on its minimizing lift). Minimizing the residual is
therefore equivalent to the unique simultaneous minimum. The induced boundary
quadratic forms and linear harmonic extensions agree. This proves the Schur
quotient identity with existence and uniqueness supplied, not assumed. QED.

**RP-C3 (source-coordinate naturality).** For invertible private U and any
boundary trace T, transform coordinates by P=diag(T,U). Then

    Schur(P^t L P) = T^t Schur(L) T.

**Proof.** The transformed blocks are T^t C T, U^t B0 T and U^t A U.
Use (U^t A U)^-1 = U^-1 A^-1 U^-t and cancel adjacent factors. QED.

This is a genuine map-level naturality law. It does not say arbitrary physical
refinements preserve the response. New hidden source inputs f change the flux
by a B0^t A^-1 f term (with sign fixed by the forcing convention). Omitting f
would hide an intervention. Nor does one-frequency black-box equality preserve
all time histories. For passive RC systems with zero initial state, equality
of their full rational transfer matrices preserves boundary input/output
convolution histories on the common causal domain; rational equality at one
frequency does not. Internal state histories and their provenance are still
forgotten by black-boxing.

## 7. Quantitative stability of the gluing operation

**RP-C4 (Schur perturbation bound).** Assume A >= aI with a>0, ||B0||<=b.
For perturbed blocks A',B0',C', assume

    ||A'-A||<=da<a, ||B0'-B0||<=db, ||C'-C||<=dc.

Then A' is positive definite and

    ||Lambda'-Lambda|| <= dc + (2b db+db^2)/(a-da)
                               + b^2 da/[a(a-da)].

All norms are Euclidean operator norms; the implementation evaluates this
formula from supplied certified bounds and does not infer the certificates.

**Proof.** The quadratic lower bound gives A'>=(a-da)I. The resolvent identity
gives ||A'^{-1}-A^{-1}|| <= da/[a(a-da)]. First compare B0'^t A'^{-1} B0'
with B0^t A'^{-1} B0 by expanding B0'=B0+E; the two cross terms and quadratic
term total at most (2b db+db^2)/(a-da). Then replace A'^{-1} by A^{-1} in the
remaining term, paying b^2 da/[a(a-da)]. Add dc. QED.

After gluing, certified component response errors delta_i contribute at most
sum_i ||T_i||^2 delta_i. Eliminating an additional interface requires another
positive gap bound. The estimate deliberately deteriorates as a-da -> 0;
there is no unconditioned stable gluing/inverse theorem near a singular
interior. Forward stability does not imply inverse identifiability.

## 8. What category is actually available?

The class of finite DtN matrices alone is insufficient for a category with
ideal-wire identities: an ideal wire imposes equality of terminal potentials
and opposite outward currents, a linear relation that is not the graph of a
finite unconstrained DtN matrix on its two terminals.

Use the classical circuit category with named input/output terminals, tagged
private vertices, and source element labels. Composition identifies matching
terminals and imposes zero net external injection at the glued vertices.
Retain the externally visible linear relation

    R_L = { (u_in,j_in; u_out,-j_out) :
            there exist private potentials solving the source equations }.

The minus sign on the output current makes relational composition match flux
conservation. The identity is the ideal-wire relation. Eliminating private
variables is existential quantification; relational composition is associative
because nested finite existential quantifiers commute. When the internal block
is invertible, this relation is represented by the Schur matrix above.
Disjoint union supplies the monoidal product. This is a concrete restriction
of classical black-box circuit semantics, not an independently new category.

A SUCC-compatible enrichment appends a versioned source event to an immutable
source journal and changes L by the declared component update. The black-box
map acts at each journal state; RP-C1--C3 specify when transport commutes. It
does not invert the journal: different component histories, decompositions,
and hidden states can yield the same response. Even the positive matrix L can
be obtained as one component L or two parallel components L/2 and L/2. Gluing
is therefore not faithful on source decomposition.

## 9. Evidence and provenance

New files: `observational_succ/reality_pin_selection.py`,
`tests/test_reality_pin_selection.py`, `scripts/reality_pin_rc_experiment.py`.
The exact finite suite tests strict and boundary-touching error margins,
continuous component-box corners and fresh interiors, source/plan mutation,
gauge copies, empty fibers, misleading restricted families, held-out rejection,
constructive refinement, fixed-error noncollapse, full-graph RC cross-oracles,
two elimination orders, interior congruence, independently assembled gluing,
orientation mutation, singular elimination, and quantitative Schur error.

The source is additive; inherited implementation and immutable import archives
are not altered. The manifest identifies the original foundational import as
FuckingRH `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; this new work does not
promote its optional RH applications. Positive network energy does not provide
signed completed Weil positivity, RH, or physical gravitational geometry.

Primary literature checked 2026-10-22:

* J. C. Baez and B. Fong, *A Compositional Framework for Passive Linear
  Networks*, Theory and Applications of Categories 33 (2018), 1158--1222,
  [arXiv:1504.05625v6](https://arxiv.org/abs/1504.05625v6). This is the classical
  source for circuit categories and black-box linear-relation semantics.
* C. I. Cârstea, *Hölder Stability from Exact Uniqueness for Finite-Dimensional
  Analytic Inverse Problems*, [arXiv:2605.06354](https://arxiv.org/abs/2605.06354).
  Its abstract states a stronger qualitative finite-measurement result under
  analytic finite-dimensional assumptions and explicitly notes the lack of an
  effective measurement list/exponent/constant. No theorem from this preprint is
  imported into our proof: RP-S2 is proved directly above, with weaker
  hypotheses and weaker non-effective conclusions; RP-S4 gives its own concrete
  effective instance.

**Next decisive missing theorem:** obtain an effective, source-authenticated
inverse modulus for a nontrivial multi-parameter admissible geometric family,
with the necessary probes physically available and a fresh held-out experiment.
The present work proves the selection mechanism and a modest quantitative
instance; it does not establish coverage of actual spacetime by that family.
