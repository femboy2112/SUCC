# Cloud E: finite Schur transport and complete rational witnesses

Parent: `main@0e56e0ae26f3d52a2ea34c0a4288478139fcb634`. Independent lane; no
changes to Claude's `quantitative_rigidity.py` or `proof_contracts.py`.

## Hole contract and status

For every finite symmetric matrix with rational entries, produce an independently
checkable alternative: a rational negative vector, or a positive weighted rational
Gram decomposition. No numerical eigenvectors, denominator cutoff, or supplied
verification function may decide the answer. This closes the finite exact witness
edge; it does not identify any matrix with a signed Weil form.

**CLASSICAL / PROVED LOCAL:** finite Schur theorem, terminating elimination
alternative, and rational witness existence. These are recovered classical linear
algebra, not claims of mathematical novelty. **TESTED FINITE:** executable generator
and independent checker; exhaustive and seeded principal-minor comparisons below.
**UNVERIFIED pending hosted kernel run:** the Lean wrapper and extraction lemmas.
The local Lean runtime cannot read `/proc/<pid>/exe`; it exits before elaboration
with `error: failed to locate application`. No modified toolchain or access-control
workaround was used. The branch-owned GitHub Actions workflow is the next check.

The next falsifiers are a negative result from an independently recomputed Gram
identity, a disagreement with the all-principal-minors criterion, or failure of the
pinned Lean kernel/mutation job. RH, integer abc and binary Goldbach remain OPEN.

## E1. Finite Schur transport

Let `m,n` be nonnegative integers; `A` is an `m` by `m` real matrix, `B` an `m` by
`n` real matrix, and `D` an `n` by `n` positive definite real matrix. Then

\[
 M=\begin{pmatrix}A&B\\B^T&D\end{pmatrix}\succeq0
 \quad\Longleftrightarrow\quad S=A-BD^{-1}B^T\succeq0.
\]

Here PSD includes symmetry. Thus an extra symmetry assumption on `A` is not
necessary for the equivalence: each side enforces it. For all real `x,y`,

\[
 (x,y)^TM(x,y)=x^TSx+(y+D^{-1}B^Tx)^TD(y+D^{-1}B^Tx).
\]

Expansion verifies the identity using symmetry and invertibility of `D`. If
`S` is PSD both terms are nonnegative. Conversely choose
`y=-D^{-1}B^Tx`; nonnegativity of `M` gives nonnegativity of `S`. Symmetry
transports because `BD^{-1}B^T` is symmetric. This is a complete finite-dimensional
argument; no topological or source assumption enters it.

The Lean theorem `finite_schur_psd_iff` invokes the pinned mathlib theorem
`Matrix.PosSemidef.fromBlocks₂₂`; the inverse instance is obtained from
`hD.isUnit.invertible`, so it is not an unproved invertibility premise.

**Counterexample if positive definiteness is dropped:** `A=1,B=0,D=-1` has positive
Schur complement and indefinite full matrix. If `D=0,B=1`, replacing the inverse
by zero gives `S=A`, but `[[A,1],[1,0]]` is indefinite for every real `A`.
Singular PSD blocks require a range condition; this lane does not silently add a
Moore–Penrose extension.

## E2. Complete constructive rational alternative

For every `n>=0` and every symmetric `M` in `Q^(n by n)`, finite rational arithmetic
constructs exactly one kind of certificate:

1. `v in Q^n` with `v^T M v < 0`; or
2. `r<=n`, positive rational numbers `p_1,...,p_r`, and rational row vectors
   `l_1,...,l_r` with `M=sum p_k l_k^T l_k`.

These alternatives are mutually exclusive, since a positive weighted sum of real
squares is nonnegative. The second alternative allows `r=0` for the zero matrix.

**Proof and construction by induction on dimension.** The empty matrix has the
empty Gram decomposition. If `M_ii<0`, return `v=e_i`. If `M_ii=0` and
`b=M_ij!=0`, put `c=M_jj`, `v_j=1`, `v_i=-(c+1)/(2b)`, and all other entries zero.
Then `v^T M v=2b v_i+c=-1`. If neither case occurs, every diagonal is nonnegative,
and each zero diagonal has an entirely zero row. If all diagonals vanish, the
matrix is zero. Otherwise choose a positive diagonal `p=M_ii`, and reorder this
coordinate first only for the notation:

\[
 M=\begin{pmatrix}p&b^T\\b&C\end{pmatrix},\qquad S=C-bb^T/p.
\]

The dimension of `S` is one smaller. If induction returns a negative vector `w`,
return `v=(-b^Tw/p,w)`. Square completion gives `v^TMv=w^TSw<0`. If induction
returns `S=sum q_k r_k^T r_k`, then

\[
 M=p(1,b^T/p)^T(1,b^T/p)+\sum_k q_k(0,r_k)^T(0,r_k).
\]

All divisions have a verified nonzero rational denominator. Each recursion
strictly reduces dimension. This proves termination, correctness, and the
alternative for every input, including singular matrices.

**Corollary (genuine rational negative-witness theorem).** If a rational symmetric
matrix is not PSD as a form on `R^n`, it has a rational negative vector. Indeed,
the algorithm cannot return a Gram decomposition, since that decomposition is a
sum of nonnegative real squares on every real vector. Therefore it returns the
first alternative. This proves the rational/real bridge without numerical
approximation or a density argument. The corollary and the Python refinement are
paper-proved here; they are **not** claimed fully formalized in Lean.

## E3. Formal scope and axiom boundary

`formal/cloud_schur/CloudSchur.lean` contains:

- the full finite real Schur equivalence above;
- a negative real direction from non-PSD of a Hermitian real matrix;
- exact rational scalar square completion;
- exact lifting of a negative rational scalar Schur direction;
- the exact `q(v)=-1` zero-diagonal coupling identity.

The imported mathlib source is pinned to
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, Lean `v4.14.0`. All transitive git
dependencies are frozen in `lake-manifest.json`. The Lean archive SHA-256 used by
the hosted workflow is
`320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`.
Each exported theorem has `#print axioms`. The job must pass and the actual output
must be inspected before reporting the observed axiom set. There are no local
axiom declarations, `sorry`, or `native_decide` in the proof file.

Two fresh typecheck-failure controls mutate the actual source: weaken `D.PosDef`
to `D.PosSemidef`, and change the zero-pivot negative value from `-1` to `+1`.
Both must be rejected by elaboration. Rejection is a calibration check, not a
proof of all soundness properties of the toolchain.

## E4. Independent executable certification and holdouts

`observational_succ/cloud_schur_certificates.py` uses only `Fraction` and integers.
The generator performs dimension-reducing elimination. The checker does not
repeat elimination: it recomputes the single negative quadratic value, or every
entry of the weighted Gram identity. A caller cannot pass a function such as
`lambda: True` or a `verified=True` record. Malformed shapes, nonsymmetry,
floating-point entries, booleans, nonpositive Gram weights, altered matrices, and
forged witnesses are rejected.

This is **finite executable evidence**, not a Lean-kernel authority API. It
provides no source-authentication certificate and accepts no theorem metadata.

The independent testing method is the all-principal-minors PSD criterion, with
determinants evaluated by Leibniz permutation sums, not elimination. The test
domain is all 125 symmetric 2 by 2 matrices with upper entries in `{-2,...,2}`,
all 729 symmetric 3 by 3 matrices with upper entries in `{-1,0,1}`, and 120 seeded
rational 4 by 4 / 5 by 5 matrices (seed `20261020`). Finite agreement is not used
as the proof of E2. Both implementations were prepared in the same model session;
their algorithmic difference is not independent human or model provenance.

Hostile exact families include, with `d=10^100`,

\[
 \begin{pmatrix}d^2&d\\d&1-d^{-2}\end{pmatrix},
 \qquad v=(-d^{-1},1),\quad q(v)=-d^{-2};
\]

and `[[0,10^-100],[10^-100,10^100]]`, where the zero-pivot construction gives
`q(v)=-1`. These defeat any justification based on fixed denominator or precision
search. A zero diagonal arising only after Schur elimination is also tested.

## Reproduction and prior art

From repository root:

```sh
python -m unittest discover -s tests -p test_cloud_schur_certificates.py -v
cd formal/cloud_schur
lake exe cache get Mathlib/LinearAlgebra/Matrix/SchurComplement.lean Mathlib/Tactic/FieldSimp.lean Mathlib/Tactic/Ring.lean
lake build
lake env lean CloudSchur.lean
python3 check_mutations.py
```

The coordinator runs repository-wide validation once. No common index, source
archive, or existing implementation is edited by this lane.

Primary checked source: [mathlib's pinned SchurComplement.lean](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/LinearAlgebra/Matrix/SchurComplement.lean),
especially `schur_complement_eq₂₂` and `PosSemidef.fromBlocks₂₂`; and the pinned
[PosDef.lean](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/LinearAlgebra/Matrix/PosDef.lean)
for `PosDef.isUnit`. The elimination argument is classical symmetric Gaussian
elimination/square completion, reconstructed here from first principles.
The project's contribution is a separately checkable exact alternative and
adversarial benchmark. No academic novelty claim is made.

**Next decisive proof obligation:** formalize the complete dimension-reducing
rational elimination, then prove the exact Python-to-kernel data interpretation
or replace its checker with generated kernel certificates. Infinite positivity
still requires a valid form core and signed source identity; E1/E2 do not supply
either.
