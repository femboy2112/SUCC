# Audit notes and productive corrections

## Stable result

The central theorem is the exact finite lower certificate and its sharp
continuous realization. The proof uses a nonnegative sixteen-cell slack
table; the sharp densities use direct integrals. Numerical optimization was
only a route to candidate coefficients. The root executable requires no LP
solver, special-function library, production import, or random draw.

## Corrections made during investigation

1. **Initial orientation missed the required gate.** The antisymmetric wedge
   using `a=(++--)` and `b=(+-+-)` is valid and detects dependence, but is
   orthogonal to `W(j,k)=w(j-k)`. Replacing `b` by `c=ab` gives the exact
   target projection. The orthogonal control remains in the executable.
2. **Nonuniqueness is not inability to force anti-lock.** Identical symmetric
   data do not determine the signed mean. However full iid unordered-pair
   data force selected mass at least1/4, and the weaker maximum law plus one
   marginal cell force at least1/16. The second pass found this positive
   implication and exact sharp controls. No claim that all radial information
   is powerless is retained.
3. **The positive source kernel was inherited.** Prior-art search located its
   factorization, five reciprocal differences, Beta product representation,
   and general floor transform in older dossiers. Their role here is a
   current-mask assembly, not a newly discovered source identity.
4. **Source coordinates have different types.** `K=[y]_4` is a dyadic rational
   residue. It is not the real quarter label `floor(4y)`. The universal
   finite-label theorem applies after this explicit transport.
5. **Clock uniformity is scoped.** The source clock is exactly uniform when
   the finite shell length is divisible by four, asymptotically otherwise.
   The finite lower certificate itself needs no uniformity assumption.
6. **All late integer shells are required.** The next target ranges over
   every sufficiently large integer `B`, not only powers of two.
7. **Aggregate test receipt selection.** The first metadata parser matched an
   earlier four-test subprocess summary in the full log. It was corrected to
   select the final aggregate summary: 13,545 tests in 1043.803 seconds, `OK`.
   The complete raw log retains both summaries; no test rerun or result change
   is implied by this receipt correction.

## Verification layers

- Three first-pass same-model lanes used separate decompositions; root then
  checked the identities and integrated a standard-library rational audit.
- A final adversarial pass separately entered all three continuous density
  tables into SymPy, checking exact cell integrals, marginal polynomials,
  diagonal CDF polynomials, and nonnegativity (the densities are multiaffine
  on their cells). Root's published audit checks the same identities using
  its own small rational polynomial integrator. Shared claims and source
  provenance are disclosed; these are not blind empirical witnesses.
- The parent source receipt is hash checked. An independent direct rational
  recurrence reproduces the first512 carry residues; finite shell counts
  beyond that reuse the inherited certified receipt.
- The full repository suite and required provenance/foundations probes are
  recorded separately in VALIDATION. Their success is software evidence and
  does not certify the asymptotic mathematical premise.

## Remaining boundary

The current work proves the implication from three coarse empirical masses
to the selected density, and supplies explicit operational probes and controls.
It does not prove those masses for the infinite original BBP trajectory.
The exact signed boundary-flux formula also shows why an auxiliary Gamma
floor law cannot be substituted for a floor applied after source integration.
