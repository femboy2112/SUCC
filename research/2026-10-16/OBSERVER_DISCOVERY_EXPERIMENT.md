# Bounded observer/envelope discovery and joint probes

**Status:** classical conditional paper identities, exact finite matrix/table
checks, and five refuted weakenings. New-to-SUCC implementation, not a claim of
new classical mathematics. This lane does not load the genuine Suzuki kernel,
prove its Schur sign, invoke Lean, run hosted CI, or prove RH.

Implementation: `observational_succ/observer_discovery.py`; entry point:
`scripts/observer_discovery_probe.py`; focused suite:
`tests/test_observer_discovery.py`. All matrices are complete declared models in
an orthonormal Euclidean coordinate basis, rather than sampled compressions of
an unidentified infinite operator. Rational coefficients extend to real forms
for the following paper proofs. The implementation also works on rational
vectors: every accepted minimizer has rational coefficients.

## Inputs, inheritance and legal grammar

Read-only baseline: branch `research/observers-schur-complement-2026-10-16`,
initial HEAD `5d6d717312eebee648d3cfb092875eb4120bb4b3`, child of Proof Teeth.
This lane writes only the three files above, this dossier and `discovery*`
receipts. Other lanes own the general observer theorem, authentic Schur
analysis, compactness and formal bridge. No code from those lanes is imported.
The principal owns Git, integration and full-suite validation.

The exact source/model is `(source_id, epoch, ordered_axes, full_matrix)`.
`RationalForm.digest` binds all of these, not just a favorable source name.
Dimensions are 1..4; entries are `int` or `Fraction`, never bool/float/string.
Coordinate observations retain a nonempty ordered subset of the actual axes.
Their digest must match the entire input form. This is an orthogonal coordinate
projection in the specified metric. A basis with a different Gram matrix needs
a proved metric transport outside this grammar.

The executable composition is

```
RationalForm --observe coordinates--> FiniteSchurEnvelope
             --observe fewer output coordinates--> FiniteSchurEnvelope
```

Every edge checks shapes, coordinates, source digest, symmetry, high-block PSD
and all cross-column range equations. A nested route emits a dependency graph
with full input/output digests. Looking up an eliminated coordinate, composing
against the original form's hash instead of the intermediate form, or replacing
the source matrix while retaining its name is refused. Matching hashes still
establish byte/model identity, not identity with an external arithmetic source.

Inherited code is reused narrowly: `recursive_operator_gluing.matrix/psd` for
exact rational input and principal-minor PSD checks, and
`minimal_observation.FiniteObservation/compile_factorization/replay_factorization`
for complete finite coimages. `proof_gluing` was inspected for its source/debt
discipline; its general instrument grammar is not duplicated. The new range
solver uses exact row reduction, including singular matrices, rather than an
inverse or a positive floating-point eigenvalue.

| Inherited file | SHA256 at lane start |
|---|---|
| `minimal_observation.py` | `0c429dd4087d9be774e26dd0c5b975b20707aaba122d0b436a6353310950ef80` |
| `recursive_operator_gluing.py` | `0dda6bdf871dfdefffe48649c785ab9d18addab6cea5553ac1d4472a3094fd94` |
| `proof_gluing.py` | `8c191ee1c20f3790c5a7eb83ee3340a2f2fb6b7a00dcf392a928e02a006d34ab` |
| `covariant_proof_descent.py` | `4245d8c0f64e3968221c15ab62b91c009230de23569d21b63e3f5c0943336ed8` |
| `provenance/IMPORT_MANIFEST.json` | `2eec9a3a730afdca338f92fbaf195e65130cec21efc68062206163f9f6a0d57f` |

The replay hashes every imported local Python dependency and checks unchanged
inherited bytes against the previous `proof_teeth_receipts/final-py313.json`
snapshot. It also records its own code/tests, this proof and import manifest.
That historical snapshot is a source pin, not a substitute for current tests.
No imported archive is changed. The inherited transitive-premise and OPEN
authority failures remain in their original audit and regression suite.

## OD-01

**Finite quadratic envelope: PAPER_PROVED, classical.** Let a real symmetric
finite matrix, in retained/hidden coordinate order, be

`G = [[A,C^T],[C,D]]`.

Assume `D >= 0` and that there is a matrix `X` with `D X = C`. For all real
vectors `x,y`, expansion gives the polynomial identity

`Q_G(x,y) = x^T (A-X^T D X) x + (y+Xx)^T D (y+Xx)`.

Symmetry of `D` and `DX=C` identify both cross terms. The last term is
nonnegative and vanishes at `y=-Xx`. Thus the envelope is the finite quadratic
form `S=A-X^T D X`, with an attained minimum. No inverse is required. A second
solution differs by columns in `ker D`, so `X^T D X` and the short are unchanged.
For rational data with solvable range equations, row reduction supplies a
rational `X`; the same minimum is attained over rational vectors.

Conversely, if every low fiber has a finite lower bound, the `x=0` fiber shows
`D>=0`: a negative quadratic high direction scales to minus infinity. For a
symmetric finite matrix, `Ran D=(ker D)^perp`. If some column combination `Cx`
is outside this range, choose `z in ker D` with `z^T Cx != 0`. Along `y=t z`,
the energy is `x^T A x+2t z^T Cx`, unbounded below. Thus `Ran C subset Ran D`
is also necessary. Rational inconsistent range equations admit a rational
nullspace witness. This finite theorem does not equate `Ran D` and
`Ran D^(1/2)` for infinite compact operators.

Runtime verifies `DX=C`, PSD via all principal minors, and
`S=A-X^T D X`. Independent replay checks these equations without calling the
producer's row-reduction solver. The paper supplies the all-vector implication;
an `EXACT_FINITE_CHECK` receipt does not become a Lean theorem. A range failure
refuses the finite-matrix rule, rather than assigning minus infinity to every
fiber. For `G=[[0,1],[1,0]]`, the `x=0` envelope is 0 but every `x!=0` envelope
is minus infinity.

## OD-02

**Compatible nested finite envelopes: PAPER_PROVED, classical.** Split source
coordinates into `x,y,z`. First eliminate `z`, retaining `x,y`, under OD-01's
PSD and full cross-column range assumptions. In the resulting matrix on `x,y`,
assume OD-01 again for elimination of `y`. Then eliminating `z` and `y` in
sequence gives exactly the same quadratic form as eliminating `(y,z)` together.

Proof: at fixed `x,y`, OD-01 attains the first minimum at a linear function
`z=z_*(x,y)`. OD-01 at the second stage attains its minimum at `y=y_*(x)`.
Consequently the staged value bounds every `Q(x,y,z)` below and is attained at
`(y_*(x),z_*(x,y_*(x)))`. It is the direct infimum. It is finite for all `x`, so
the necessity half of OD-01 shows the direct eliminated block is PSD and has
the required cross-column range inclusion. Thus the direct rule applies too.
Equality of all quadratic values implies equality of symmetric matrices by
polarization (or evaluation at basis vectors and their sums).

All intermediate matrices remain tied to the original model through checked
edges. A high block may be singular. The executable singular example is

```
G = [-1  1  1]       eliminate z, then y:  S = [-2]
    [ 1  1  1]       eliminate (y,z):      S = [-2]
    [ 1  1  1]
```

Its second-stage hidden block is zero with zero cross column. This is a
legitimate range-compatible singular case, not an illicit zero inverse.
Twenty-seven additional exact models use arbitrary `a,b,c in {0,1,-1}` in
`[[a,b,c],[b,2,1],[c,1,2]]`. These finite runs are checks of implementations;
they do not establish the universal theorem by sampling.

## OD-03

**Extended-real nesting without positivity: PAPER_PROVED, elementary.** Fix
one real-valued function `q` on a nonempty product fiber. Then

`inf_(y,z) q(x,y,z) = inf_y inf_z q(x,y,z)`

as extended-real values, with no assumption of positivity, finiteness or
attainment. Indeed a real number `b` is a common lower bound of all the values
on the left exactly when it bounds every value in every `z` fiber, exactly
when it bounds every inner infimum on the right. This identifies the greatest
lower bounds, including minus infinity; there is no subtraction of infinities.

More generally, for a source `S`, observation `O:S->A`, coarsening `r:A->B`
and real target `q:S->R`, the nonempty coarse fiber is the union of the fine
fibers with `a in O(S)` and `r(a)=b`. Therefore

`m_(r O)(b) = inf_{a in O(S), r(a)=b} m_O(a)`.

Use the reachable coimage; including unreachable artifacts requires the
explicit convention `inf empty=+infinity`. This is the precise quotient rule.
It does **not** say `m_O(a)=m_(r O)(r(a))` pointwise: the right side takes a new
infimum across fine observations. Such equality holds for every reachable `a`
iff `m_O` is constant on each reachable coarse fiber. That is an additional
factorization condition, not a consequence of nested observations.

This rule is represented as a conditional paper theorem. The executable
matrix grammar does not encode arbitrary extended-real functions or return a
finite short when OD-01's hypotheses fail. The obligation is retained in the
rule record and increases its application-debt rank.

## OD-04

**Joint finite probe minima: PAPER_PROVED plus exact finite checks.** Fix the
entire finite source `S`, target `h`, and menu `O_0,...,O_(k-1)`. For a subset
`J`, the joint observation is the ordered tuple `(O_j(s))_(j in J)`. The
inherited coimage criterion says it is sufficient iff equal joint observations
always imply equal target values. The decoder is defined only on reachable
joint artifacts. The new wrapper exhausts every subset, including the empty
one, compiles its decoder or collision, and independently replays each result.
Bounds are `|S|<=64`, `k<=8`: at most 256 subsets. No input source is sampled.

The smallest successful subset cardinality is therefore a genuine minimum
within the declared fixed menu. Inclusion-minimal and minimum-cardinality
subsets are reported separately. For each inclusion-minimal `J` and `j in J`,
the failed subset `J\{j}` supplies `s,t` with different targets but identical
remaining observations. Since `J` succeeds, probe `j` must distinguish this
pair. These are indispensable-probe witnesses, not a count of failed trials.
If the entire joint menu fails, its collision survives every deterministic
postprocessing of that joint readout. A nonconstant target with an empty menu
fails; a constant target needs zero probes. The procedure makes no general
claim about adaptive worst-case probe complexity or probes outside the menu.

**Authentic finite arithmetic calibration.** On the entire residue source
`Z/4`, use inherited `character_four` values `(0,1,0,-1)`. Let `b0(r)=r mod 2`
and `b1(r)=floor(r/2)` for standard representatives `0<=r<4`. Each is a lawful
finite set observation; `b1` is not asserted to be a group homomorphism.
Together they recover `r=b0+2b1` and hence chi4. Each alone is insufficient:

* Without `b0`, residues 0 and 1 have equal `b1=0` but values 0 and 1.
* Without `b1`, residues 1 and 3 have equal `b0=1` but values 1 and -1.

Thus the minimum is exactly two probes in this two-probe menu. Periodic
extension to integers follows by first taking the residue modulo 4, not by
sampling a long interval. If the menu adds the target itself as a probe, the
minimum is one: this is a source/toolkit-relative statement, not an absolute
two-experiment law. A separate XOR control contains both a size-two
inclusion-minimal subset and a size-one global minimum, rejecting the false
identification of irredundancy with minimum cardinality.

## Predeclared false candidates and smallest bounded witnesses

The generator lists five deliberately false weakenings before search. It
enumerates symmetric `2x2` forms `(a,b;b,d)` with each of `a,b,d` drawn from
the ordered alphabet `(0,1,-1,2,-2)`, in product lexicographic order, up to 125
matrices. A result is the **first matrix in this stated order**, not the
smallest rational matrix under all possible encodings. Witness vectors are
constructed algebraically after the matrix is found, not claimed globally
minimal. Reducing the budget to just before each first witness produces
UNRESOLVED; zero budget never proves a candidate. At this minimal nontrivial
split there is one retained and one hidden coordinate.

| False candidate | First matrix | Exact obstruction |
|---|---|---|
| `Q=0` on hidden kernel implies exact energy factorization | `(0,1;1,0)` | `(1,0)` and `(1,1)` have the same observation and energies 0,2 |
| `A>0,D>0` imply positive short | `(1,2;2,1)` | `(1,-2)` has energy -3; short is -3 |
| Compression equals the envelope | `(0,1;1,1)` | at x=1, compression 0, attained envelope -1 |
| Coarsening preserves each fine envelope value | `(0,0;0,1)` | identity observation at `(0,1)` has envelope 1; coarse x=0 envelope 0 |
| Singular PSD high block alone gives finite envelope | `(0,1;1,0)` | x=1,y=-t gives -2t, while the x=0 fiber still has infimum 0 |

The returned ray in the last row has an exactly negative linear coefficient
and zero quadratic coefficient. Unboundedness is proved by that formula, not
by testing large negative numbers. The finite search returns
`EXACT_FINITE_CHECK / REFUTED` with full coefficients and rational witnesses.
No lower bound is misreported as a genuine negative source eigenvalue: all
five witnesses belong to explicitly synthetic declared rational models.

## Proof authority, adversarial checks and reproduction

Every conditional rule has immutable required hypotheses. Its record says
`recorded_authority=PAPER_PROVED`, `runtime_issued_universal_proof=false`,
`Lean_kernel_replayed=false`, `external_source_identified=false`. The prose
proof supplies its mathematical authority. Search survival cannot alter that
record or discharge a hypothesis. Application ranking uses the number of
explicit outstanding application obligations, followed by stable rule ID;
it measures proof debt, not mathematical novelty or anticipated success.

The full finite certificate replay rejects mutated response entries, result
coefficients, authority labels, source epochs and basis coordinates. A
different valid solution in `ker D` is accepted, testing the mathematical
criterion rather than equality with the producer's preferred solver output.
The independent algebra check constructs 45 PSD outer-product high blocks and
cross columns from `D w`, then reconstructs **every coefficient** of the
completed-square polynomial. It does not call the range solver or PSD helper.
Joint-menu checks independently enumerate every binary decoder on 64
three-state/two-probe cases. Countermodel tests evaluate scalar polynomials
directly, rather than calling the envelope routine. These are method/code-path
differences within one reasoning session, not independent human peer review.

Run serially from the repository root, with native thread pools bounded:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /tmp/succ-proof-teeth-py310/bin/python -m unittest discover -s tests -p test_observer_discovery.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /tmp/succ-proof-teeth-py310/bin/python scripts/observer_discovery_probe.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /tmp/succ-proof-teeth-py313/bin/python -m unittest discover -s tests -p test_observer_discovery.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /tmp/succ-proof-teeth-py313/bin/python scripts/observer_discovery_probe.py
```

Pinned outputs and actual command/exit-code receipts live in
`observer_schur_receipts/discovery*`. The initial focused run passed 18 tests;
the final receipts determine the current counts and hashes. No full suite is
claimed by this lane. Next extension: represent an actual source-defined
finite observation with a separately verified semantic bridge; an arbitrary
finite matrix, a digest or a successful conditional rule cannot supply it.
Infinite Schur response/range certification remains the analytic lane's debt.
