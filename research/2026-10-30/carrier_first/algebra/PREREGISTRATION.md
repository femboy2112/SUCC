# Algebra-front claims and discriminators, before implementation

Parent: PR417 at `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
Read-only sibling PR421 at `e14916aa2b4dfc2cce948facc729fb02ce1efafa`
already supplies scalar Pascal residue transport and a dual-number carrier.
Those are inputs, not new results of this front.

| Candidate | Expected pass | Expected failure / ambiguous |
|---|---|---|
| A1 Typed labeled paths form an extension category; split/concatenate gives Pascal and Vandermonde bijections | Exhaustive short words, three blocks and identity paths | Reused labels or mismatched middle objects rejected; endpoint grade alone cannot recover word history |
| A2 Signed completion is a quotient of positive rank pairs; grade-two polarization recovers multiplication | Positive/negative ranks and different representatives | Negative binomial coefficients are not literal counts; uncolored total rank cannot recover colored cross-grade |
| A3 Coefficientwise umbral map on a noncommutative rational algebra intertwines derivative/difference | Arbitrary exact 2x2 matrix coefficients, signed evaluation ranks | Ordinary product is not transported unchanged; expected lower-grade overlap defect |
| A4 Source-decorated grade descent iff every Pascal diamond kills every reachable state | Commuting edges; noncommuting edges flat on an invariant reachable line | Two shears fail; ambient nonflatness alone is ambiguous if reachable states miss the defect |
| A5 Swap defects telescope with full prefix/suffix transport | Nonconstant edges and exact matrix words | Bare commutator without transport generally gives wrong total defect |
| A6 Authentic BBP chronological ordering uniquely maximizes its unwrapped finite lift among source permutations | Four-pole source, strict positive source differences | Seed change leaves the theorem intact; it supplies no selected circle-dispersion certificate |

Paper proofs establish unbounded algebraic statements. Exhaustive finite tests,
a separately written word/SymPy oracle and a standalone Lean4.14 proof will
check implementation and a declared finite algebraic subset. Same-model agents
are not independent referees. Fresh exact cases will use labels, matrix entries,
signed ranks and source horizons excluded from discovery examples.
