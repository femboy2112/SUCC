# Operation PROOF TEETH — YEAN ↔ SUCC

Research audit and implementation handoff, 2026-10-15. **RH PROVED: NO.**
Parent SUCC main 02fc9f46ad3b914d49df7a658e304d06ed8a6200 (Academic Main
consolidation, PR #132). Actual active YEAN parent
dev/yean-r5-ouroboros-memes-2026-10-13 at
c9e2c030c091694c1425c43589767e1260fcd48a (61 commits
ahead of YEAN main c671226732f38bd4ae86d281fd0206217dfd43b1).
Both branches are research-only; nothing on main or in original RH
archive changes.

Companion YEAN dossier:
[operator roadmap](https://github.com/femboy2112/yean/blob/research/succ-carrier-operators-to-yean-2026-10-15/research/succ_yean_operators_2026-10-15/YEAN_IMPORT_HANDOFF.md),
[affine proof](https://github.com/femboy2112/yean/blob/research/succ-carrier-operators-to-yean-2026-10-15/research/succ_yean_operators_2026-10-15/AFFINE_TWO_POINT_GENERATOR.md),
[quotient/Fourier proof](https://github.com/femboy2112/yean/blob/research/succ-carrier-operators-to-yean-2026-10-15/research/succ_yean_operators_2026-10-15/FINITE_RETRACT_AND_DUALITY.md).

## Audit: SUCC's actual theorem/proof frontier

Main has reconstructibility N→Z→Q, CRT/profinite limits,
finite adeles, Pontryagin duality, Fourier/Poisson and Tate
Mellin using **classical theorems with exact source-chart
implementations**. It also has scoped analytic completed-zeta
Weil coercivity on high moment-null sectors and small intervals.
The important difference is between a theorem established on
its exact domain, an exact finite-program observation, and an
unverified arrow to a universal signed Weil norm.

As documented in docs/RESEARCH_FRONTIER_2026-10-15.md
and docs/SUCC_RESEARCH_DEPENDENCY_DAG.md, the original
completed Weil sign remains OPEN on prime-active/all-radius
test functions. The low Schur block S0=A-R0, full
low/high coupling, source-derived positive kernel
identification and uniformity are **not** provided by
positive finite Gram experiments. No RH conclusion follows.

The SUCC pinned signed ζ/Suzuki source listed in the
frontier is Git blob
0cc8510b71d178fc79e8d410a86d8b6014cf9178:
true von Mangoldt prime-power jets, half-density 1/2,
one Gamma_R, proper poles and conductor/parity.
No nontrivial zero ordinate is a legitimate construction
input. Wrong half-density, fake composite impulse,
incorrect Gamma/pole, root-number/parity and sign
mutations must remain active negative controls.

## Import YEAN's strongest already-verified instruments

### Y1 — The coimage factorization theorem (a proof-access gate)

At the LIVE YEAN dev head, Yean/MemeSufficientArtifact.lean,
claim YEAN-C-0201, proves for any observation Q:S→A and
desired report h:S→B that a decoder
v:Coim(Q)→B with v([s])=h(s) exists **iff**
\[
\forall s,t,\quad Q(s)=Q(t)\Longrightarrow h(s)=h(t).
\]
This is not a counting guess. It is the quotient universal
property, with uniqueness of the decoder on the coimage;
the constructive quotient proof does not silently use
Classical.choice to extend to unreachable artifact values.

**SUCC application:** source observation maps in
observational_succ/covariant_proof_descent.py and
carrier_lawful_profile.py already compute fiber
collisions. Instantiate the mathematically proved
YEAN factorization with genuinely declared source maps.
A claimed theorem that only consults the observation
is invalid if two indistinguishable sources have
different truth values for the desired claim.

Negative calibration: S={0,1}, Q constant, h=id.
No decoder exists. A decoder that secretly reads s
or an imported original-source label is a provenance
violation, even if every local arithmetic check passes.
Positive calibration: h constant on Q-fibers, construct
the quotient decoder and show uniqueness. Do not treat
an abstract Q/h theorem as proof that the real Q
matches the original physical source.

### Y2 — Finite generating bases, with *minimality proof*

YEAN Yean/GeneratingBasis.lean proves a finite
coordinate/unit/multiplication basis sufficient for
**all** free-monoid-substitution naturality obligations
using induction; it has per-generator ablation
counterexamples. This is exactly the discipline
SUCC needs to turn a class of infinite paths into
a finite proof obligation — but **only after the
source category and presentation are precisely given**.

New SUCC instance: source words in successor
T_t(x)=x+t and prime multiplication V_p(x)=px
normalize to exact affine maps F_{a,b}(x)=ax+b
under composition
\[
(a,b)\circ(c,d)=(ac,ad+b).
\]
For every finite word an inductive proof computes (a,b).
On R_n=Z/nZ, n>=2, equality of two such maps at inputs
**0 and 1** is equivalent to equality on ALL R_n,
because b=F(0) and a=F(1)-F(0).
Both inputs are essential in this class:
id vs V_2 agrees at 0 but differs at 1;
id vs T_(n-1)∘V_2 agrees at 1 but differs at 0.
The theorem is paper-PROVED in the companion YEAN note.
It is NOT kernel-checked yet.

The two-probe equality statement is about a
specified family of affine maps, NOT arbitrary
functions and NOT a universal two-observation
physical epistemology. Furthermore id vs T_n
agrees on R_n but differs on N. The source/
quotient distinction must be retained even
when all residues in a finite stage are checked.

Source: observational_succ/finite_affine_presentation.py
and tests/test_finite_affine_presentation.py added here.
The implementation structurally normalizes each legal
typed action and guards against composite V_6
as a fake prime generator. Its finite probes
are an exact-instance diagnostic, not a proof by
enumeration of all maps or all word lengths.
Core relation: V_p∘T_1=T_p∘V_p,
so SUCC and FUCC do not generally commute.

### Y3 — Finite structural route equality and matrices

The active YEAN branch already has
Yean/MemeRouteDecide.lean (routeEqB_iff_ext)
and **Yean/MemeRouteLeafSort.lean**
(YEAN-C-0208, every label-preserving permutation
of an arbitrary mixed-label sum tree is
structurally realizable). The second theorem
is already CLOSED in the active branch,
despite older intermediate research notes
listing it as unfinished.

YEAN's Yean/MemeHomMatrix.lean and
MemeHomMatrixCoherence.lean prove the natural
n-ary map decomposition
\[
\mathrm{Hom}(\coprod_i C_i,\prod_j D_j)
\cong\prod_{i,j}\mathrm{Hom}(C_i,D_j),
\]
with row/column read-off coherence and
transport under leaf reindexing. SUCC already
has a finite Set Beck–Chevalley interface
in covariant_proof_descent.py. Import the
actual commutative squares, not just a
matrix metaphor: label every source arrow,
object/domain, transport law, and mutation
that would break naturality.

These YEAN statements concern structural
isos and functions. They do not automatically
provide a linear operator product,
spectral calculus, source authenticity,
or positivity. A non-invertible V_p
on R_p cannot inhabit an invertible
MemeRoute groupoid.

### Y4 — Split idempotents and source-faithful Fourier operations

YEAN Core/SplitCodec.lean proves
split-idempotent logic. Its
MemeProjectorRigidity.lean proves
that an invertible route cannot be a
nontrivial idempotent. A genuine
nontrivial projector is nevertheless
possible in the category of **total
non-invertible** linear maps; no
partiality is required.

This branch adds FiniteQuotientRetract:
with m=kn and q:Z/m→Z/n, let
U:Q^(Z/n)→Q^(Z/m) be pullback,
P:Q^(Z/m)→Q^(Z/n) sum over fibers,
A=P/k, E=UA. Counting-metric adjunction
U*=P gives AU=id, E²=E, E*=E, and
\[
\|g\|^2=\|Eg\|^2+\|g-Eg\|^2.
\]
The companion YEAN dossier contains a
full finite proof. The executable
checks source-tagged exact rational
instances and preserves wrong 1/k
as a hostile mutation.

SUCC's PLUS-phase finite Fourier convention
requires the dual character injection
a mod n → (m/n)a mod m. For f on
Z/n and b mod m,
\[
\widehat{Uf}_m(b)=
\begin{cases}
k\,\mathrm{emb}(\widehat f_n(a)),& b=ka,\\
0,&k\nmid b.
\end{cases}
\]
Here emb is the actual cyclotomic
inclusion, not equality of coefficients
in different root fields. SUCC's
pre-existing dynamic_fourier_tower.py
has the **opposite** pushforward square
\(\widehat{Pg}_n(a)=\widehat g_m(ka)\).
The two together make E a frequency mask.
The standard finite Tate character
has the opposite sign from SUCC's positive
characters: χ_r(z)=ψ_f(-rz), not ψ_f(rz).

A rational finite orthogonal projector
**is not** a positive factorization of
the completed signed Weil form. It is a
calibrated algebraic object, not the
missing RH-hard arrow.

### Y5 — Proof-certificate separation and axiom budget

YEAN has a standalone Rust T0 verifier
plus independent Lean reference checker,
canonical content-addressed proof objects,
checked Lean metatheory and explicit
axiom scanners. The pinned toolchain
is Lean 4.29.1 / Rust 1.85.1.
SUCC should import the *discipline*:
untrusted producer, narrow trusted
statement/proof verifier, separate
source/morphism authentication, and
checked axiom budget. A Python claim
boolean is never a replacement for
an independently verified theorem.

YEAN Ouroboros R5 has demonstrated
source-free reproduction only on
specified small profiles; the deep
decoder and full multi-module source
bootstrap remain open; R6 endogenous
self-hosted generational fixed point
and R7 release audit are not proved.
No artifact self-reproduction observation
magically validates analytic theorems.

## New executable SUCC artifacts (exact, scoped)

1. observational_succ/finite_affine_presentation.py
2. tests/test_finite_affine_presentation.py
3. observational_succ/finite_quotient_retract.py
4. tests/test_finite_quotient_retract.py

The first pair normalizes finite prime-gated
SUCC/FUCC words and reports source N vs
Z/n equalities. The second adds quotient
retraction, projector, Fourier pullback
and source/epoch typed instance receipts.
The existing SUCC Fourier implementation
is **reused**, not replaced.

Validation status: **OBSERVED in an isolated
local Python harness** — five finite
retraction test groups and four affine
test groups passed. The Fourier dependency
in the isolated harness was independently
implemented using SymPy exact cyclotomic
arithmetic. Therefore the tests support
the new algebra but **do not exercise
the actual checked-in SUCC finite Fourier
dependency stack** end-to-end. The new
branch has NOT had official CI or the
entire SUCC unittest gate run by this
session. SUCC's parent main *reports*
4338 tests passed and Academic Main PR
CI 69/69; those are not current branch
validation. There is no new Lean theorem
in this checkpoint.

## A proof-bearing SUCC claim capsule

For each proposed result, make the next
local session produce a typed record with:

1. **Statement** — exact source carrier,
   test space, function domain, quantifiers,
   target proposition and assumptions;
   distinguish all words vs a finite
   word-length cap and all tests vs
   a fixed Gram basis.
2. **Source morphism** — actual original
   source Git blob, source-ID/epoch,
   operations, phase and normalization;
   a validated name is not source proof.
3. **Proof terms** — derived lemmas,
   imported classical theorems, kernel/
   checker version, #print axioms and
   an exact dependency graph. No
   unexplained propext, Quot.sound,
   Classical.choice or analytic axiom.
4. **Quantitative certificates** — exact
   rational arithmetic, certified outward
   intervals and uniform error tails
   as applicable; measured floats
   are never universal proof.
5. **Hostile controls** — mutated source,
   fake prime, wrong sign, wrong Gamma,
   wrong pole, missing dual factor,
   source aliases and known negative
   signed matrices.
6. **Reproducibility** — SHA, command,
   stdout/exit, independent implementation
   or true mathematical derivation,
   known failures and fresh holdouts.
7. **Promotion gate** — statuses
   CLASSICAL / PAPER PROVED /
   LEAN PROVED / TESTED MODEL /
   UNVERIFIED / REFUTED are separate.
   No status promotion from a
   simulator's self-reported flag.

A locally checked theorem may still be
irrelevant to the target: a Lean proof of
"if the original Weil form is PSD then
it is PSD" has not manufactured a
source-derived positive morphism.
The theorem type and source bridge
are the actual acceptance criteria.

## Predicted discriminating failures

**Affine:** checking only 0 misses
id vs V2; checking only 1 misses
id vs T_(n-1)∘V2; equality mod n
is not equality on N.

**Operator direction:** missing 1/k
makes PU=kI instead of AU=I
and destroys idempotence; mapping
frequency a→a instead of a→ka
breaks the Fourier/quotient square;
the wrong Tate sign breaks translated
cosets. Vp at a composite modulus
can be noninjective and must not be
treated as an automorphism.

**Source:** Q constant with
h nonconstant admits no
artifact-only decoder. Any source
ID/epoch laundering or access to
hidden original source is a failure.

**Quadratic positivity:** the signed
matrix
\[
M=\begin{pmatrix}1&-2\\-2&1\end{pmatrix}
\]
has positive diagonal tests
Q(e1)=Q(e2)=1 but
Q(e1+e2)=-2. This decisively
refutes the inference "positive
on each generator ⇒ PSD on
their span." The global signed
Weil sign is vastly stronger
than generatorwise positivity.

**Limits:** finite positive Gram,
finite profinite characters,
short support or high moment-null
positivity cannot certify
global topological, analytic,
or all-window Weyl/Weil positivity
without separate hypotheses
and their proof.

## Directed local execution — acceptance criteria

**P0, SUCC reproducibility:** obtain
this exact branch, verify HEAD,
then run in a complete SUCC checkout:

    python -m unittest tests.test_finite_affine_presentation tests.test_finite_quotient_retract
    python scripts/verify_provenance.py
    python -m unittest discover -s tests -p 'test_*.py'

Record interpreter, commit, test count,
traceback and exit status. Test the
real SUCC Fourier dependency and
all hostile mutants. Full parent
suite is not automatically validated
by the isolated local harness.

**P0, YEAN formal finite lemmas:** from
its companion research branch, use
pinned Lean to prove every finite
word has its declared affine form;
0/1 equality iff entire R_n
agreement; U/P/A/E split,
self-adjointness, energy;
Fourier contravariant lift and
normalization. Prove all theorem
types with genuine source terms
and record #print axioms.
Do NOT modify the Mathlib-free
Ouroboros germline or import
analytic assumptions into T0.

**P0, abstract factorization meets
real source:** instantiate
MemeSufficientArtifact.factor_iff
on SUCC original-source reports,
including a collision failure and
an equal-fiber successful decoder.
Audit actual channel Q separately.
Failure to authenticate Q must
remain UNVERIFIED, not be
silently replaced by a guessed
observation model.

**P1, generic finite theorem capsules:**
port only minimal source-typed IR,
normal form proof constructors,
independent certificate replay,
source-map diagram checker and
axiom budget. Use YEAN's
Meme route and hom matrix proofs
where the operations are genuinely
isos or functions. Do not smuggle
non-invertible Vp through a groupoid.

**P1, dynamic proof policies:** import
SUCC adaptive_proof_policy.py
into a separate YEAN reasoning
lane with proven finite AND/OR
rank semantics. Actions can
change carriers and probe menus;
the result is conditional
on actual declared source state,
not a statement about infinite
observers.

**P2, RH application only after
finite proof infrastructure:** work
backwards from the original
complete signed Weil form on a
declared full test-function space,
source gamma/poles/half-density,
correct completed convolution
and uniform tails. Show a source-
faithful positive map and test
its failure under source
mutations. Do not assume the
unknown low Schur sign or call
source-free positivity "proved".

Scope ledger for this checkpoint:
- **PROVED ON PAPER:** elementary
  finite affine and finite quotient
  theorems in paired YEAN notes.
- **OBSERVED:** bounded exact instance
  tests under isolated local harness.
- **UNVERIFIED:** newly written actual
  Lean proof kernels; production
  SUCC all-tests; source→Weil
  positive Hilbert identification.
- **OPEN:** RH, global original Weil
  sign for arbitrary source-authentic
  test functions.

The proof system must have teeth
because it refuses false universality,
not because it blesses a compelling
analogy. Review this against AGENTS.md
and docs/METHOD.md before integration;
no default rewrite, release,
archive edit, or merge is authorized.
