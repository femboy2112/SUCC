# Cursed categorical computation: coherent numerical arrows

This dossier develops the user's request for deliberately strange computation
paths, including arrows encoded by numbers that open into coherent families
and categories. It contains exact constructions, source-preserving obligations,
countermodels, executable rational probes, and an explicit statistical boundary.

## Reading map

| File | Content |
|---|---|
| [ROUND_I.md](ROUND_I.md) | Tiny categories, averaging oscillators, the bicyclic origin, source-gauge countermodels, digit randomization, and inverse-beta source recursion. |
| [ROUND_II.md](ROUND_II.md) | Numerical Karoubi completion, affine ideal categories and Möbius inversion, rational matrix corners, family functors/spans, signed groupoids, and FRACTRAN. |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Scoped proof, finite-check, refutation, and open-obligation labels. |
| [SOURCES.md](SOURCES.md) | Pinned repository context and checked primary mathematical sources. |
| [VALIDATION.md](VALIDATION.md) | Exact validation scope and publication checkpoints. |
| [round_ii_probe.py](round_ii_probe.py) | Standalone standard-library exact regression probe. |
| [round_ii_receipt.json](round_ii_receipt.json) | Saved finite execution with script hash and control outcomes. |

## The useful result

For every monoid M, its Karoubi envelope is equivalent to the category of
idempotent principal right M-sets eM and equivariant maps. Opening each such
family into its category of elements over BM gives another equivalent
presentation. The projection to BM retains the multiplication labels. This is
an actual arrow-to-number-to-family/category bridge, with maps, composition,
identities, and reconstruction supplied in Round II.

For the load-bearing positive affine clock monoid, numerical codes
2^(a-1)(2b+1) preserve the noncommuting product (a,b)(c,d)=(ac,ad+b). Its principal
ideal category is equivalent to the one-object monoid category, but ideal
inclusions must be retained to recover each particular clock operation. The
affine incidence inverse has the exact sparse form

\[
\mu_{\mathrm{Aff}}(a,b)=\mu(a)(\mathbf1_{b=0}-\mathbf1_{b=a}).
\]

These constructions help compile and audit computations. The source and
observer remain part of the mathematical object: forgetting them can identify
the authentic forcing with zero forcing while changing phase observations.

## Boundary and provenance

This is additive research based on Main XXII at
`43886e830cee5ff6d6b37719e18d809819673bd9`. Unmerged donor results are cited at
their inspected snapshots, not silently integrated as new main theorems. No
frozen source, historical seed, existing claim status, or CI workflow is changed.

The fixed source has U_0=0, U_n=16U_(n-1)+r(n), and
sum_(n>=1)16^(1-n)r(n)=pi. The alternate partial sums P_n use weights 16^(-n),
so P_infinity=pi/16. The distinction is retained throughout.

No categorical equivalence or finite run here proves pi normality, original-zero
parity balance, or RH. The next load-bearing obligation is a source-derived
signed-cancellation bound, with the evaluator and residual transported exactly.
