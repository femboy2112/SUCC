# Complementary review of categorical arrows

Reviewed `../category/CATEGORICAL_ARROWS.md`, with exact SHA256 retained in
`receipts/category-review.json`. This is a complementary **same-model**
review with fresh implementations, not independent external refereeing.

No substantive mathematical issue found in CA-01 through CA-04:

- The three-bit perturbation preserves the full (X,J_m) law for every m,
  pointwise in X. Its history-conditioned third-step law changes. The native
  conditional-iid assumption distinguishes it, so the construction correctly
  refutes marginal-to-history identification, not the original sensor itself.
- The row/column support graph has kernel dimension m(d−1); the proposed
  adjacent-square cycles are independent and have exactly that cardinality.
  One-step d=1 uniqueness is compatible with hidden non-Markov history.
- The complete two-time {1,H,λ^j} probe family is genuinely insufficient at
  m=d=4. Independent symbolic Q(sqrt5) elimination found rank7 and nullity5,
  then verified all nine mixed products vanish on a nonzero direction.
  Euler–Mascheroni offsets are marginal terms and correctly cancel.
- The Cauchy two-time inversion proof and row-norm amplification bound are
  valid. Identifiability is not uniform conditioning or selected cancellation.

Minor clarification applied after the hashed review: the harmonic cycle defect
has the sign of ε; the displayed strict positive inequality now explicitly
assumes ε>0. The author reports this as the only dossier change since the
review read. It does not change the formula, rank argument, or experiment.

`category_review.py` imports no category implementation. Its fresh checks:
27 direct word-to-grade marginal comparisons at p=1/7,3/8,7/11;
10 independent incidence/cycle ranks; rank7/nullity5 for the triangle design;
9 exact symbolic product checks; and3 Cauchy reconstructions with rational
nonconsecutive marks. All passed. Raw output, Python/SymPy versions, command,
UTC start, duration, exit status and hashes are retained.
