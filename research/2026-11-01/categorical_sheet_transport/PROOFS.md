# Categorical source completion: from snapshots to a faithful successor object

**2026-11-01. Research-only paper proofs and exact certificates.**
Parent: SUCC PR #447, `6fedcbe445f856878ecb1b1d9a0a84ad97a77e2e`.
Original source, literal U0=0, production, historical contracts and main are unchanged.
No new Lean theorem, external priority, physical quantum law, pi normality or RH is claimed.

## 0. Object and acceptance criteria

The author's proposal is to interpret SUCC as “another one” in each mathematical
realization and use category theory to reconstruct objects from otherwise lossy
snapshots. The strongest valid reading is not that all mathematics has literally
been two-dimensional: it is that the current observation maps may forget data
needed to transport a successor. A real categorical repair must supply objects,
morphisms, composition, source/seed markings, compatible charts and phase-aware
observables. It must not turn a forbidden quotient map into a theorem by renaming it.

We prove: (1) a general minimal dynamical observation completion; (2) a source-specific
two-frame rational reconstruction and a globally faithful THREE-frame sphere
embedding; (3) marked rotation covariance; (4) exact Fourier naturality and conductor
refinement; (5) limits on what these representation theorems imply analytically.

## CST-01. “Another one” as a pointed dynamical object

In Set, let an object be (X,x0,T), with T:X->X and x0 in X. A morphism
f:(X,x0,T)->(Y,y0,S) satisfies f(x0)=y0 and f T=S f. Then (N,0,n->n+1)
is initial: the unique morphism is n->T^n x0. Proof is ordinary recursion and
induction. Equivalently, an unpointed dynamical object is a representation of
the free one-generator monoid N, regarded as a one-object category.

This is an exact version of the author's intuition: the *abstract operation*
is represented in different carriers. It does not furnish a canonical successor
on every unstructured mathematical object. Source, action and initial point
remain declared data. In general categories the corresponding natural-number
object must exist; we make no universal existence assertion.

Nonautonomous original BBP becomes autonomous after retaining its clock:

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    T(n,x)=(n+1,16x+r(n+1)),  (n0,x0)=(0,0).

This is total on N x R. Its complex extension is meromorphic/partially defined
at the forcing poles, not an everywhere holomorphic map. The source clock's
sphere successor z->z+1 is, separately, an everywhere holomorphic automorphism.

## CST-02. Minimal completion of a snapshot, with a universal property

Let p:X->Y be an observation and T:X->X a deterministic successor. A map
S:p(X)->p(X) satisfying S p=p T exists exactly when

    p(x)=p(y) => p(Tx)=p(Ty).

Necessity follows by applying S. Sufficiency defines S(p(x))=p(Tx), with the
condition proving independence of the representative.

Define the behavior map

    H(x)=(p(x),p(Tx),p(T^2x),...),
    x ~ y iff p(T^n x)=p(T^n y) for every n>=0.

Then shift acts on H(X), and H T=shift H. Its kernel is the largest T-stable
equivalence relation contained in ker p. In particular, if q:X->Z is any
surjective observation refinement with p=a q and q T=S q, there is a unique
map b:Z->H(X) with b q=H, b S=shift b. Set b(q(x))=H(x); equality of q-values
implies equality of every future p-value by induction. This proves the
universal property. It is the standard behavior/final-coalgebra construction
for the coalgebra x->(p(x),T(x)), specialized to this use.

On a finite carrier, start with labels p(x), and refine by
(label(x),label(Tx)) until stable. The executable complete_observer implements
exactly this construction. Its rounds identify the first finite future that
separates rivals. Termination on finite X does not imply effective finite
termination on an arbitrary infinite carrier.

**Span warning.** The coarse k-step span is Y <-[p]- X -[p T^k]-> Y.
Composing two such spans uses X x_Y X and admits all pairs satisfying
p(T^k x)=p(x'), not merely the physically compatible x'=T^k x.
The faithful history embeds diagonally into that pullback; generally it is a
proper subset. Thus “replace maps by spans” alone can invent branch changes.
For the exact four-cycle T=(0 1 2 3), p=(0,0,1,1), true two-step coarse
transitions are only 0->1 and 1->0; composing coarse one-step relations also
allows 0->0 and 1->1. Retain lift compatibility or use the completed state.

## CST-03. Independently verified original four-sheeted source cover

Write

    A(z)=(8z-7)^4,
    D(z)=(8z-4)^2(8z-3)(8z-2),
    R(z)=A(z)/D(z).

The exact original source satisfies r(z) dz=(1/8)dlog R(z). This is checked
by an integer-polynomial identity, independently of the symbolic derivation.
The Cayley coordinate t=-i(R-1)/(R+1), with eta=2dt/(1+t^2), obeys
r(z)dz=(i/8)t^*eta. These are transports of DIFFERENTIALS, not a claim that
time successor already descends to the two-puncture angular sphere.

The quartic discriminant is

    Disc_z(A(z)-uD(z))
      =5566277615616 u^3 (32u^2-2507u-18432000).

The cover has degree 4, one index-4 ramification point over u=0, and three
simple branch transpositions: one over infinity (the double pole z=1/2),
and two distinct finite nonzero branch values. Riemann-Hurwitz accounts for
all ramification, 3+1+1+1=6. The three transpositions multiply, up to loop
convention, to a 4-cycle. Their edge graph is therefore connected; transpositions
along a connected graph generate S4. Hence the complex geometric monodromy is S4.
This is not an arithmetic source-state evolution group.

**Original non-descent is real and tightly scoped.** If R(z+1)=G(R(z)) for
rational G, degree multiplicativity forces deg G=1. R(z+1) has a fourth-order
zero at z=-1/8, but R is unramified there:

    R'(-1/8)=59392/1125 != 0.

A Mobius postcomposition cannot create that zero multiplicity. Thus no such G
exists. More generally no nonzero translation z->z+c descends rationally:
R has only one point of local degree 4, z=7/8, and its translated preimage
would be z=7/8-c. A degree-one postcomposition preserves local degrees.

This is NOT a failure of successor on the source sphere. Nor is it a failure
on the selected positive real trajectory: R>0 and R'=8rR>0 on [1,infinity),
so the real-analytic map R o S o R^{-1} already exists on that real interval.
The obstruction is a *single globally rational quotient-state law*.

## CST-04. TWO consecutive snapshots recover the source rationally

Let H2(z)=(R(z),R(z+1)). Compute the degree-one subresultant in z of

    A(z)-uD(z),  A(z+1)-vD(z+1).

With explicit integer bidegree-(3,3) polynomials a,b in sheet_transport.py,
that subresultant is

    2^42 [8 a(u,v) z+b(u,v)].

The stdlib checker verifies the universal identity

    8 z P_a(z)+P_b(z)=0,
    P_a=D(z)^3 D(z+1)^3 a(R(z),R(z+1)),
    P_b=D(z)^3 D(z+1)^3 b(R(z),R(z+1)),

by multiplying integer coefficient lists and obtaining the zero polynomial.
It independently verifies the bidegree-(4,4) implicit curve F(u,v)=0. No
sampled numerical equality is used to infer the rational-function identities.
Thus, on the chart a!=0,

    Psi(u,v)=-b(u,v)/(8a(u,v)),  Psi(H2(z))=z,
    S2(u,v)=(v,R(Psi(u,v)+2)).

Consequently S2 H2=H2 S exactly. A polynomial representative for P_a has
degree 18. After dividing by its positive integer coefficient gcd and
substituting z=1+t, ALL 19 coefficients are strictly positive. Therefore
this inverse chart works for EVERY real z>=1, not merely tested integers.
The literal initial clock z=0 is verified separately and is also in this chart.
Rational inverse coefficients and positivity receipts are executable and retained.

The field consequence is C(R(z),R(z+1))=C(z). A concise independent proof
works for every nonzero observation spacing c: C(z)/C(R) has degree 4 and
no proper intermediate field. If it had an intermediate quadratic extension,
there would be a nontrivial Mobius involution preserving R. Such an involution
must fix the unique zero 7/8 and the unique double pole 1/2, and exchange
3/8 and 1/4. In t=(z-7/8)/(z-1/2), it would be t->-t, but those two simple
poles have t-values 4 and 5/2, not negatives. Contradiction. Since R(z+c) is
not in C(R) by the local-degree proof, adjoining it gives all of C(z).

H2 is birational onto its image; this does not assert one inverse affine chart
works at every complex source point. Normalization of its image recovers P1.
The following stronger result removes even that global chart/identification issue.

## CST-05. THREE snapshots give a global embedding of the entire source sphere

Define

    H3:P1 -> (P1)^3,
    H3(z)=(R(z),R(z+1),R(z+2)),   H3(infinity)=(1,1,1).

This map is a holomorphic (indeed algebraic) embedding. Here is an explicit
finite proof, including all complex points and all projective infinity values.

For distinct finite x,y, equality R(x)=R(y) is equivalent to
A(x)D(y)-A(y)D(x)=0. After dividing by x-y and a nonzero integer, this is
f(s,p)=0 with s=x+y, p=xy, where

    f(s,p)=245760p^3-475136p^2s+215552p^2
            +318464ps^2-308544ps+75628p
            -73760s^3+114100s^2-60319s+10976.

For the next two snapshots the equations are

    f0=f(s,p),
    f1=f(s+2,p+s+1),
    f2=f(s+4,p+2s+4).

GLOBAL_DELAY_CERTIFICATE.json contains three integer polynomials h0,h1,h2
of total degree <=4, and an explicitly nonzero 87-digit integer C, such that

    h0 f0+h1 f1+h2 f2=C.

The independent stdlib checker expands this identity in Z[s,p]. Therefore
these three collision equations have NO common complex solution. This proves
separation of every pair of distinct finite points, including pairs mapping
to infinity in one of the sphere coordinates.

For separation from the source point infinity, the same file supplies an
integer Bezout identity for A(z)-D(z) and A(z+1)-D(z+1). They cannot vanish
together. No finite z can therefore have H3(z)=(1,1,1).

Finally, all finite critical points of R are zeros of

    c(z)=(8z-7)(2z-1)(120z^2-89z+16).

The double-pole critical point is included; simple poles are not critical in
the target infinity chart. A third integer Bezout identity proves c(z) and
c(z+1) have no common zero. Hence even the first two coordinates have no
simultaneous vanishing derivative. At source infinity, with w=1/z,
R(1/w)=1-(15/8)w+O(w^2), also unramified.

H3 is thus injective and immersive. Its compact source makes it a homeomorphism
onto its image; the holomorphic local inverse gives a holomorphic embedding.
Let C3=H3(P1). The global successor on the full reconstructed object is

    S3=H3 o (z->z+1) o H3^{-1}: C3 -> C3.

It is an everywhere defined automorphism of this smooth rational curve.
This proves a genuine global repair, not a plan to add unknown sheet labels.
C3 is still a one-complex-dimensional curve: three observation coordinates do
not mean three independent hidden spatial dimensions.

**Executable projective decoder.** On P1(Q), reconstruct_triple uses exact
polynomial gcds of A(z+j)-u_j D(z+j), replacing that polynomial by D(z+j)
when u_j=infinity. The three-frame injectivity and immersion ensure a unique
simple finite common root; (1,1,1) represents infinity. It rejects off-curve
triples rather than choosing a branch. Tests include original source poles,
negative clocks, zero, rational holdouts and infinity.

**Whole BBP object, not only its clock.** Over the selected integer-clock
image add the arithmetic fiber x:

    ((u,v,w),x) -> (S3(u,v,w),16x+r(H3^{-1}(u,v,w)+1)).

Start at (H3(0),0). This is conjugate to the exact pointed original skew product.
At complex clocks it has the original forcing's meromorphic domain restrictions;
we do NOT pretend the pole singularities have disappeared. Clock recovery is
not a closed rational formula for U_n, and does not erase the need for its state.

## CST-06. Rotation is a morphism between marked objects, not necessarily a symmetry

Use objects (M, labeled divisor D, omega, S, x0, sampling marks). For an
invertible coordinate map g, transport ALL of these:

    D_g=g(D), omega_g=(g^{-1})^*omega,
    S_g=g S g^{-1}, x0_g=g(x0).

Then S_g g=g S, and g^*omega_g=omega. Between frames a,b the transition is
b a^{-1}; triple-overlap composition (c b^{-1})(b a^{-1})=c a^{-1} is exact.
This is an action groupoid of marked presentations. Requiring g to fix the
original source poles asks for an automorphism of ONE marked object, a much
stronger condition, which generic pole configurations lack. Covariance does
not require such an automorphism.

For g(z)=(z-1)/(z+1), an SU(2) sphere quarter-turn after normalization,
S_g(w)=(w+1)/(3-w), not w+1. Source pole positions and sampled integer marks
move as well. The circle metric must be transported if using more general
Mobius maps that are not round isometries. Pole loops and temporal source
steps remain different arrow types unless an additional transport identifies them.

## CST-07. Fourier transformation is a natural change of representation

For a finite horizon choose Q=lcm(den U0,...,den UN), necessarily odd. Then
Qr(j) is integral for j<=N, and multiplication by 16 is invertible modulo Q.
On H_Q=C[Z/Q], use F_+(k,x)=exp(2pi i kx/Q)/sqrt(Q).

An exact monomial operator is

    O(a,t,b,c)|x> = e((b x+c)/Q)|a x+t>,  gcd(a,Q)=1.

Composition and inverse are explicitly implemented. Conjugation by F_+ gives

    F_+ O(a,t,b,c) F_+^{-1}
      = O(a^{-1}, -a^{-1}b, a^{-1}t, c-a^{-1}bt),

with all register coordinates mod Q. Proof: expand the Fourier kernel;
summing over x gives zero unless input k=b+a output l, and the surviving
phase is c+t l. This derives the formula without numerical root approximations.
It preserves composition. F_+^2 is parity and F_+^4=I; signs are declared,
not inferred from a geometric picture.

Original source steps are P_j=O(16,Qr(j),0,0). Their ordered product has
translation QU_n. In function coordinates the exact dual law is

    (F_+ P_n F_+^{-1} f)(k)=e(k U_n) f(16^n k).

Hence the projective-circle source phases, ordered affine propagation and
Fourier carrier agree under an explicit source-authenticated transport.
For every source path arrow p, write Pos(p) for its exact ordered operator
and Freq(p)=F_+ Pos(p) F_+^{-1}. The family F_+ is a natural isomorphism:

    F_+ Pos(p)=Freq(p) F_+.

path_adapter.py uses the EXISTING ObservationPathCategory and its verified
arrow words; it does not create a second category implementation.

**Central phase is load-bearing.** For T_a|x>=|x+a> and M_b|x>=e(bx/Q)|x>,
M_b T_a M_b^{-1} T_a^{-1}=e(ab/Q) I. Discarding scalar phases identifies
this loop with the identity, but a coherent reference distinguishes them.
Our operators retain c; projective equivalence alone is not sufficient.
The original phase echo is exactly

    P_n^{-1} M_h P_n M_{-h16^n}=e(hU_n)I.

The natural transformations make this identity basis-independent. They do
not estimate its sum over time.

**Sphere/Fourier obstruction is not denied.** A single rotation in the usual
spin-15/2 representation sends a highest-weight vector to binomial weights
C(15,k)p^k(1-p)^(15-k); F_16 sends a coordinate basis vector to uniform weights.
Equal adjacent probabilities would demand both 15p/(1-p)=1 and 7p/(1-p)=1.
Thus no such single rotation implements F_16 in that representation. The
repair is a Hilbert-state representation fiber and its Fourier intertwiner,
NOT a false identification of all Fourier operators with spatial sphere rotations.

## CST-08. Conductor growth glues exactly, but point traces are not bounded in the limit

For Q'=mQ, position refinement is I|x>=|mx>. Its Fourier-dual isometry is

    (J f)(k)=m^{-1/2} f(k mod Q).

Direct kernel computation gives F_{Q'} I=J F_Q. These embeddings compose
coherently through any divisibility tower. Original source operators obey
P_j^{Q'} I=I P_j^Q. Between growing horizons the evolution is an isometric
embedding followed by a unitary, not a unitary between unequal dimensions.

Finite register operators alone do not determine their unique future extensions:
16 and 1 induce the same dilation modulo 15, but not modulo 105. The canonical
source family is reconstructed from the retained exact label a=16 and r(j), not
inferred from a reduced finite matrix. Monomial.embed provides a compatible
extension when its dilation remains a unit; source_operator(j,Q') is the
source-authenticated extension. These agree on the embedded old carrier but
need not agree on every new state. This distinction is explicitly tested.

The arithmetic phase evaluator is

    ell_{h,Q}(f)=sqrt(Q) f(h mod Q).

It is compatible: ell_{h,Q'} J=ell_{h,Q}. However ||ell_{h,Q}||=sqrt(Q).
The conductors are unbounded: otherwise every positive r(n)->0 would belong
to one fixed lattice (1/Q)Z, impossible. Thus the compatible point evaluation
is UNBOUNDED on the Hilbert inductive limit. An L2 colimit does not justify
passing a pointwise arithmetic observable through a limit.

An exact rational witness in normalized Haar coordinates is phi_Q=Q*1_{k=h}:
||phi_Q||_2^2=Q while |phi_Q(h)|^2=Q^2. The evaluation/norm ratio diverges.
This is a concrete functional-analytic boundary, not an objection to gluing.
The finite signed observable remains exactly available at every horizon.

## CST-09. Non-Abelian cover monodromy is not the arithmetic path category

S4 is finite. Each original affine source step x->16x+r(j) has infinite order
(the dilation factor of its m-th iterate is 16^m). Consequently no group
homomorphism from S4 can identify a finite-order sheet permutation with that
step. This kills the tempting shortcut “S4 automatically is BBP path order.”

The repair is to retain the full source-labelled chronological/path category,
not merely its finite sheet-permutation quotient. A full punctured-sphere
fundamental group also retains loops in the kernel of monodromy, but an
identification of those loops with source-time operations would still require
its own declared and verified representation. This round does NOT invent it.
The implemented adapter transports the already authenticated chronological arrows;
its upstream-category integration tests are explicitly not run locally.

## CST-10. Coherence is not cancellation; the precise remaining analytic problem

Conjugating every operator and transporting every observer preserves every
scalar readout exactly. Naturality therefore holds for coherent as well as
cancelling phase streams. Along a time chain any invertible propagator can
be trivialized by a co-moving frame; its arithmetic then moves into the
transformed observable. Flatness on that chain is not a normality theorem.

For the same original forcing, put alpha=sum 16^-j r(j)=pi/16 and
T_n=sum_{j>=1}16^-j r(n+j). A changed initial state s=1/5-alpha gives

    U_n(s)=16^n/5-T_n,
    e(h U_n(s)) -> e(h/5),    h integer,

because 16^n=1 mod 5 and T_n->0. It has the same source cover, the same
three-frame reconstruction, marked rotation covariance and Fourier naturality.
The pointed authentic object s=0 is distinct, but a seed-blind categorical
coherence theorem cannot distinguish their asymptotic character means.

To advance normality we still need a new bound for the exact pointed scalar

    S_N(h)=sum_{n=1}^N e(hU_n(0)),   S_N(h)=o(N) for every fixed h!=0,

or the inherited critical Fejer signed-lag criterion. The new framework
eliminates representation and source-clock ambiguity; it does not declare
that the analytic estimate is automatic. A useful next probe must exploit
something about the selected section *beyond* basis covariance, positivity,
finite monodromy or Hilbert energy, while paying the unbounded point-trace norm.

## Provenance / classical sources

The initial-object/free-action and natural-transformation language is classical:
Emily Riehl, Category Theory in Context, https://math.jhu.edu/~eriehl/context/ .
Behavioral completion: J.J.M.M. Rutten, Universal coalgebra: a theory of systems,
CWI report (1996), https://ir.cwi.nl/pub/4802 .
Categories of elements/fibred sets: Stacks Project, tag 0042,
https://stacks.math.columbia.edu/tag/0042 . For the covariant Set-valued action
used here, take the dual opfibration convention; do not silently reverse arrows.
Normalization/function fields: Stacks Project, tags 0BXQ and 0BXX,
https://stacks.math.columbia.edu/tag/0BXQ and https://stacks.math.columbia.edu/tag/0BXX .
Spans and composition: Baez, Hoffnung, Walker, Groupoidification,
https://math.ucr.edu/home/baez/groupoidification/ .
Finite Heisenberg/Weil context: Cruickshank, Gutierrez Frez, Szechtman (2019),
https://arxiv.org/abs/1906.03468 . Our composite-conductor formulas are derived
explicitly above and are not imported as a finite-field-only theorem.

Original source/phase identities and carrier constraints are inherited from
SUCC #438–#447 and the existing operational_yoneda_descent core. Source-specific
delay inverse and global three-frame certificates are derived in THIS round.
No claim of independent external reviewer or academic priority is made.
