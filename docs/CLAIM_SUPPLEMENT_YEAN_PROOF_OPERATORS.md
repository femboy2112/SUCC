# Claim Supplement — YEAN × SUCC finite proof operators

**Research branch only; 2026-10-15.**
Base SUCC 02fc9f46ad3b914d49df7a658e304d06ed8a6200,
YEAN active-source c9e2c030c091694c1425c43589767e1260fcd48a.
This supplement is additive: no existing O#### or historical RH
source claim is renamed, dropped or status-promoted.
See [full handoff](../handoffs/YEAN_PROOF_KERNEL_OPERATOR_BRIDGE_2026-10-15.md).
**RH PROVED: NO.**

Status vocabulary distinguishes paper proof, executable
instance and Lean kernel proof; the last is NOT claimed here.

## YX-01 — finite affine-word normalization

**Statement:** For every finite word in integer successor T_t
(t>=0) and genuine prime dilation V_p, applied chronologically,
there are unique a>=1,b>=0 with F_w(x)=ax+b for every x in N.
The recursive fold produces them, with composition
(a,b) after (c,d) = (ac,ad+b).

**Domain:** mathematical finite words with unbounded length,
all x in N; runtime implementation bounds action length,
integer magnitude and prime argument.

**Status:** CLASSICAL, PROVED ON PAPER in YEAN
AFFINE_TWO_POINT_GENERATOR.md; TESTED MODEL exact finite
instances in SUCC; Lean kernel proof UNVERIFIED.

**Evidence:** observational_succ/finite_affine_presentation.py;
tests/test_finite_affine_presentation.py; paired YEAN note.

**Adversarial controls:** the false commutativity
S V_p=V_p S without p successor shifts, composite V_6
masquerading as prime, reversed action order, bool
as integer, and mismatched carrier.

**Next discriminator:** actual pinned Lean theorem
for every finite word and independent direct-action
differential testing on the full SUCC checkout.

## YX-02 — affine two-point decision and its boundary

**Statement:** For any n>=2 and any two integer affine
words w,v, equality as functions on Z/nZ is equivalent
to equality at residue inputs 0 and 1. Neither probe
alone suffices: id vs V_2 and id vs T_(n-1)∘V_2.
Equality on Z/nZ is weaker than equality on N:
id vs T_n.

**Status:** CLASSICAL, PROVED ON PAPER for the
restricted affine function class. Lean mechanization
UNVERIFIED. Bounded runtime TESTED MODEL.

**Scope:** the conclusion is NOT for arbitrary
functions/unknown sources; n need not be prime.
The two basis observations must actually be
available to the declared observer before it
can operationally use the decision procedure.

**Proof:** evaluate at 0 to recover b mod n;
subtract at 1 to recover a mod n; then
evaluate arbitrary x. Reversibility
or physical oracle completeness is not assumed.

**Mutation:** check only input zero, check only
input one, or upgrade mod-n equality to original
source equality. All have explicit counterexamples.

**Next discriminator:** verify exact theorem
statement and typed finite source endomorphism
semantics in Lean, including both one-probe ablations.

## YX-03 — quotient retraction and orthogonal projector

**Statement:** For m=kn, n>=2,k>=2, over
rational functions on finite cyclic carriers,
pullback U and fiber sum P satisfy U*=P
for counting inner products and PU=kI.
Let A=P/k. Then AU=I, E=UA is a
nontrivial self-adjoint idempotent;
||g||²=||Eg||²+||g-Eg||².
For towers n|m|ell, U,P,A compose
in their typed directions.

**Status:** CLASSICAL, PROVED ON PAPER in
FINITE_RETRACT_AND_DUALITY.md; exact finite
instance tests OBSERVED in isolated harness;
Lean mechanization UNVERIFIED.

**Hostile controls:** omit the factor 1/k,
identify P and U despite opposite types,
or put nontrivial E in an invertible
groupoid, violating the only-idempotent-
is-identity theorem.

**Next discriminator:** use the actual
SUCC exact rational implementation in
a full checkout; prove U/P/A/E in Lean,
inspect axiom budget and source projection.

## YX-04 — Fourier dual injection and source phase

**Statement:** The quotient Z/m→Z/n for m=kn
induces the dual character lift a mod n→ka mod m.
With PLUS unnormalized DFT and a declared
cyclotomic field embedding,
hat(U f)_m(b) vanishes off b in k(Z/n)
and equals k times embedded hat(f)_n(a)
at b=ka. Opposite P restriction already
exists in dynamic_fourier_tower.py.

**Status:** CLASSICAL, PROVED ON PAPER;
exact specimens in isolated local harness
OBSERVED via independent SymPy cyclotomic
backend. Actual GitHub checked-in SUCC
dependency integration UNVERIFIED;
global adelic Poisson not inferred.

**Mutations:** keep character label a
unchanged when lifting, invert the
positive Fourier phase, lose k factor,
or conflate chi_r=psi_f(-rz) with
chi_r=psi_f(rz).

**Next discriminator:** run the actual
finite_fourier_carrier/CyclotomicElement
path in repo-wide Python tests, plus
proof from root-of-unity orthogonality
in a named formal setting.

## YX-05 — original-source proof factorization

**Statement:** For observation Q:S→A
and target h:S→B, a decoder on
Coim(Q) recovers h iff h is constant
on every Q-fiber. This is YEAN's
MemeSufficientArtifact.factor_iff
in the live dev branch.

**Status:** EXISTING YEAN LEAN-PROVED
abstract quotient theorem (as reported
by verified source and exact declaration
review), but a SUCC original-source
instance and source-map authentication
remain UNVERIFIED.

**Adversarial control:** S=Bool,
Q constant, h=id has no artifact-only
decoder; a simulated decoder consulting
hidden original source is a false proof.

**Next discriminator:** define an
actual source-typed Q from existing
SUCC carrier model, prove commuting
square from the real event semantics,
import the Lean theorem and require
a reproducing non-factorization
witness when Q fibers collide.

## YX-06 — positivity non-consequence

**REFUTED inference:** Positive
quadratic form on each basis vector
implies positivity on their span.
Matrix M=[[1,-2],[-2,1]] has
Q(e1)=Q(e2)=1 while Q(e1+e2)=-2.
Thus YEAN finite generating-basis
sufficiency for **naturality** cannot
be substituted as a sign theorem.

**STATUS:** REFUTED universally
by an explicit rank-two counterexample.

**RH firewall:** the completed
original source's low Schur
sign, source-derived universal
positive Weil Gram and
all-radius all-test positivity
remain OPEN. No current claim
capsule has closed them.
Any assertion that the new
positive E=UA is that Weil
positive source is UNVERIFIED
and must be source-identified
before consideration.

## Exact status and reproducibility

New code and tests were created on the
paired non-main SUCC branch; the paper
proofs live on the non-main YEAN
branch, not silently on its main.

The research session validated five
finite quotient and four affine
focused test groups in an **isolated**
local harness; for finite Fourier
the harness used an independent
SymPy exact cyclotomic oracle.
Official branch CI, entire SUCC
unittest suite, real SUCC cyclotomic
implementation integration, and
Lean theorem compilation on these
new lemmas are NOT claimed run.

Before a status change:
1. reproduce current Git checkout and
   run narrow and broad tests;
2. inspect theorem universality and
   declared fields for vacuity;
3. run actual kernel #print axioms;
4. retain mutant and negative
   counterexample outputs;
5. revalidate correct source
   provenance and exact mapping;
6. run fresh holdouts and
   independent routes.

An experimental operator,
even exact and self-adjoint, is
not a substitute for the missing
source-to-signed-Weil identification.
