# Exact finite coupled observer instrument

Run from the repository root:

```sh
python research/2026-11-04/zero_frame_coupling/coupling_probe.py --verify research/2026-11-04/zero_frame_coupling/FINITE_RECEIPT.json
python -m unittest discover -s tests -p 'test_zero_frame_coupling.py' -v
```

The source pin in the receipt is #506's exact base. The receipt also binds
the executable files by SHA256; its enclosing Git commit binds the complete
instrument. No external digit input is used. The sole rational phase helper
is an audited, explicitly attributed extraction from read-only #505 at
`00b6385b6e7420b5e108e6766dcf2f7dda875f59`; this is shared implementation
provenance, not an independent sine/cosine oracle.

## Independent source paths

Path 1 iterates the original four signed Fractions and the distinct authentic
angular/radial eight-tap vectors, without ever reducing the stored states.
Path 2 collapses the original and radial sources to independently checked
integer polynomials, grows a common integer LCM and iterates its three integer
numerators. Every unwrapped state agrees exactly. Each literal carry is
separately checked against the fractional recurrence. `U=Y+Z` holds on the
line, not merely on the circle. At N=1025 the receipt records 3,075 reconciled
states and all 1,025 triples of literal carries.

Full state and phase transcripts use canonical hexadecimal numerator and
denominator encodings before SHA256 hashing. This avoids conversion limits
on large decimal integers. Raw phase observations are preserved as integer
grid pairs in deterministic `RAW_GRID.json.gz`, with an uncompressed SHA256.
The code deterministically reconstructs the exact rational inputs.

The source-jet oracle solves `z(x)-16z(x-1)=r_rad(x)` coefficient by
coefficient. It is independently compared through order six with #506's
geometric-moment/Vandermonde path. The full polynomial identities, rather
than just sampled source equality, are checked by symbolic rational algebra.

## Certified phases and maximal sums

For dyadic A, a rational positive series bounds log(2); the selector proves
`H <= A^2 log A <16H`. No floating logarithm selects the critical depth.
Every phase is reduced as a Fraction before any approximation. The character
helper uses Machin's alternating arctangent bounds, phase grid `2^-80`,
degree-47 rational Taylor polynomials and output grid `2^-60`. Its total
complex error is at most `2^-50`, including any declared tail enclosure.
The Taylor remainder is bounded by `2*4^48/48!`, with all pi/phase/output
rounding paid. Input enclosures exceeding the budget are rejected.

Reciprocal weights are exact rational numbers at most 8/3. Weighted grid
rounding adds less than `2/2^60` in complex norm; hence the common per-term
budget `3*2^-50+2/2^60` is conservative. Full-epoch and every sharp interval
mean inherit at most that error. Integer square roots enclose the largest
squared prefix chord; every consecutive interval is enumerated. A full-epoch
zero cannot masquerade as a maximal zero. The coherent real seed is computed
as `-T_n` with an explicit 24-term positive rational tail enclosure, not as
a floating subtraction of pi from exponentially large values.

The factorial design keeps raw signed complex means and all 15 nonempty
mixed differences per case. Their errors are summed by the triangle
inequality. The seed-1/5 factor is also transported back by the exact global
phase `e(-sign*H/5)`. Its apparent raw interactions disappear identically
under that declared transport. They cannot be evidence of source mixing.

## Results and boundaries

Five preregistered cases, 80 factorial cells, 20 controls and 4,272,640 prefix
chords pass. The fresh critical cases are A=256,h=7 and A=512,h=-3. Their
Lambda values, 7/16 and 3/4, are still small: these are calibration and
falsification observations, not tests of an asymptotic onset. The former's
uniform original maximum increases under lag one; the latter's decreases.
Neither direction is a universal cancellation law.

Twelve focused native tests cover independent polynomial sources, full lifts,
literal carry mutants, jet coefficients, the twisted link and wrong-frequency
failure, rational-Cayley nonperiodicity, maximal-vs-full-window failure,
complete factorial interactions and rational phase enclosure checks.
Independent mpmath evaluations are high-precision numerical diagnostics;
the enclosure authority comes from the rational error proof above.

No finite result proves normality, a source-selected rate, statistical
independence or a preferred observer. The original equal-time, unweighted
column is mask zero; all other configurations are explicitly labelled source,
seed or observer interventions.
