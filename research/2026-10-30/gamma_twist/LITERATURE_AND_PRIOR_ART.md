# Literature and repository prior-art audit

Checked 2026-10-30. This is a targeted applicability audit, not an exhaustive
priority search. New results have local paper authority and shared-model
review only. External theorems, inherited proofs, finite tests and open
selected-phase obligations remain separate.

- **BBP source:** Bailey, Borwein and Plouffe,
  [On the Rapid Computation of Various Polylogarithmic Constants](https://www.davidhbailey.com/dhbpapers/digits.pdf).
  The four signed coefficients and original zero seed are retained.
- **Complete Gauss normalization:** Gross and Koblitz,
  [Gauss sums and the p-adic Gamma-function](https://annals.math.princeton.edu/1979/109-3/p06).
  The finite-extension formula, uniformizer choice, additive character and
  Teichmuller embedding are explicit in the Gauss dossier. Direct cyclotomic
  checks of unit powers do not independently choose the remaining root.
- **Quadratic multiplication:** Evans and Greene,
  [Evaluations of hypergeometric functions over finite fields](https://www.d.umn.edu/~jgreene/papers/Evaluations_Hiroshima.pdf),
  equation1.5. The needed Davenport–Hasse identity is also rederived from
  Jacobi sums in this campaign, so its signs are checkable without reliance
  on a name or a valuation-only formula.
- **Gauss equidistribution scope:** Rojas-Leon,
  [Equidistribution and independence of Gauss sums](https://arxiv.org/abs/2207.12439).
  Variation over multiplicative characters is a declared family. The actual
  BBP chronological cofiber has not been identified with that family. Our
  exact mutant relation is a classical multiplication relation, not evidence
  contradicting the published theorem.
- **Gamma/Beta/Barnes:** [DLMF5.5](https://dlmf.nist.gov/5.5),
  [5.12](https://dlmf.nist.gov/5.12), [5.17](https://dlmf.nist.gov/5.17).
  Recurrence, multiplication, positive integrals and Barnes primitives are
  recovered identities; none is promoted to a selected cancellation bound.
- **Normality calibration:** Bailey and Crandall,
  [Random Generators and Normal Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf),
  and Lagarias, [On the Normality of Arithmetical Constants](https://arxiv.org/abs/math/0101055).
  Stoneham normality is classical. Hypothesis A remains an unproved input
  for this campaign. Rational translations are not required to fail normality.
- **Integral Frobenius models:** Mellit–Vlasenko
  [constant-term congruences](https://arxiv.org/abs/1306.5811) and
  Rowland–Yassawi [rational diagonals](https://arxiv.org/abs/1310.8635).
  DF-01/02 prove why the direct original rational coefficient sequence
  lacks those particular integral/diagonal models. Different auxiliary
  sequences and time-dependent denominator clearing remain possible.

## Recovered results must not be counted again

The exact total Green budget `(R-pi)/15`, its numerical value and nonlinear
Lipschitz transfer are already in
`research/2026-10-27/PI_SELECTED_BOUNDARY_CRT_FRONTIER.md`, originating commit
`1f9305e6b78c4921c3f001bc9a77b079f1362756`. Thus PR400 GPR-04's characterization
of the constant as new is corrected here **additively**: it is recovered.
No historical dossier is rewritten.

The exact two-adic backward zero and orbit isometry are already in
`research/2026-10-27/BBP_BINWINDOW_ZERO_BOUNDARY.md`, originating commit
`eeb2a48ea1b43967ea385009a3f8ec280b2efa69`. Four exact source samples already
identify four fixed-pole weights in `bbp_source_memory.py`. The new TI
result is the entire fixed-precision congruence lattice, its sharp bit loss,
and the derivative/unit-factor blindness, not the old exact reconstruction.

PR370 already gives the finite golden fixed point and first correction.
GEO-02 derives its second coefficient and cubic/quartic mutant hierarchy.
The original Harmonic/Golden/Euler–Mascheroni triangle and Oily–Macaroni
retain Leah / femboy2112 authorship and their original provenance ledger.

## Recent irrationality claims are not imported as proof inputs

The current search found Bai's September2026
[preprint claiming an improved upper bound](https://arxiv.org/abs/2609.11276)
and an OpenAI September2026
[preprint claiming irrationality exponent two](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex).
The latter introductory source was read at Git blob
`fe28ac589090c44a8877aa326b60e753c863fa24`; its proof is in separately included
sections and was not independently certified here. These are recorded as
unverified external claims for this campaign, not current-best facts or
inputs to any new theorem. No irrationality exponent, even two by itself,
would supply the missing constant mean energy on the declared prime windows.
