# Actual validation and remaining checks

## Executed in this response

* `cover_certificate.py`: exact SymPy 1.14.0 source differentiation, Cayley pullback,
  quartic discriminant, subresultants, cleared inverse identity, (4,4) delay curve,
  fresh rational inverse checks, and separately computed Sylvester determinants.
* `independent_polynomial_oracle.py`: pure Python stdlib reconstruction of A,D,
  substitution by coefficient convolution, full inverse polynomial identity,
  full delay-curve identity, nonzero initial denominator, and all 19 positive
  coefficients after shifting the degree-18 cleared denominator by one.
* `frame_and_monodromy_audit.py`: exact frame/clock/tangent identities, original
  first trace-residue transport, six distinct source-pole chord distances,
  characteristic-zero false sheet-gluing gcd, all 96 transposition triples with
  four-cycle product, and the trivial deck-group normalizer calculation.
* Focused unittest discovery: **60 tests run, 59 passed, 1 skipped**. The skipped
  test requires the full `observational_succ` package and is named
  `test_existing_observation_path_category`. There were no failures or errors.
* Reverse-order replay: **60 tests run, 59 passed, the same 1 skipped**. No order
  dependence observed. Tests load research modules under unique names rather than
  modifying sys.path or assuming an unqualified `independent_oracle` module.

The first source tests compare the literal four poles to the combined rational
formula for n=1..200; state checks compare sequential evolution to independent
convolution. Fourier checks compare exact modular phases, including full 15-state
basis/harmonic pairs and fresh growing conductors. All phase decisions use exact
Fractions; no float is accepted as a source/state input.

The coefficient certificate proves an identity in a polynomial ring; it is not a
large grid mistaken for a universal proof. Nonetheless this remains an inspected
paper/computer-algebra proof, not a trusted-kernel formalization.

## Controls actually exercised

Positive: original exact source; lawful path associativity and identity; correct
conductor and Fourier embeddings; entire 16-branch partition; stable quotient.
Negative/mutation: source sign, source order, seed, invalid source pole, malformed
delay pair, inverse coefficient mutation, false sheet seam, wrong Fourier sign,
undersized/even conductor, wrong dual embedding, and omitted radix branches.
Null: constant observation has no added predictive distinctions.
Boundary: pair observations are not everywhere injective in the finite projective
controls, despite the generic characteristic-zero theorem. Infinity is retained.

The coherent q=1/5 counterseed is a paper-level real-model control, not an executed
irrational value in a finite Fraction register. The report explicitly corrects that
domain mismatch instead of claiming that this seed passes the original register
contract.

## Failed attempts and repairs preserved

1. A direct repository access attempt failed with `Could not resolve host:
   github.com`. Authenticated connector reads succeeded. No full checkout existed.
2. The initial naive symbolic exploration completed the discriminant and linear
   subresultant but timed out during a large expanded rational substitution.
   `receipts/cover_exploration.txt` preserves its raw partial output and
   `receipts/aborted_naive_symbolic_exploration.py` preserves the attempted script.
   The repair was to clear denominators before expanding and to use coefficient
   polynomials. The exact parameters/source were unchanged.
3. The first frame audit failed one structural equality check: SymPy `factor`
   returned the unsimplified object `0*I`, which did not compare equal to integer
   zero. Replacing that check by rational `cancel` produced exact zero. The inverse
   and clock checks, residue, distances, and group checks were unchanged. This was
   an equality-normalization bug, not evidence against the chain-rule theorem.
4. A conceptual audit narrowed the counterseed claim: irrational coherent seeds
   belong to the real model, not the original finite odd-denominator carrier.
   The proof text and source map now retain this distinction explicitly.

## NOT executed / NOT claimed

Full SUCC test suite, actual canonical category-adapter integration, repository
provenance/foundations/ordinal scripts, new Lean formalization, external reviewer,
remote push, draft PR creation, or hosted CI for these files. Earlier repository
reports of 44/484/10k+ passing tests are not counted as runs in this response.

The connector file contents and source hashes were read, but a complete upstream
git worktree was unavailable. The downloadable additive patch is suitable for
inspection and `git apply --check` on a full checkout; no clean application to the
actual upstream worktree is asserted here.

## Verdict

Source reconstruction, lawful successor composition, and Fourier/conductor
naturality have explicit constructions with exact checks. Source-specific selected
signed cancellation is not proved. Geometry-to-heat/Feynman amplitude identification
remains unverified. No mathematical claim status in the remote repository changed.
