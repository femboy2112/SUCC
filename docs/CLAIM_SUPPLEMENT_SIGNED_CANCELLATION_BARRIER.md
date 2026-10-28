# Signed-cancellation barrier claim ledger

Research-only child of #324. Parent source commit:
`fca58d3e0289e57596dd8ca74bace325a450df31`.
`PROVED` below means a paper proof in the stated domain, not Lean verification
or external peer review. `VERIFIED_FINITE` does not imply an infinite limit.
No old claim status is promoted.

| ID | Statement and domain | Status | Proof / next falsifier |
|---|---|---|---|
| SCB-01 | For every real carrier, original-tail visits to the 15 nonzero hexadecimal cuts obey the explicit SC-1 packing bound and O(N/log N) | PROVED | [Single-wrap proof](../research/2026-10-27/PI_SINGLE_WRAP_SEAM.md), endpoint and shifted-window controls |
| SCB-02 | Every digit statistic has exact wrap-jump decomposition SC-2/3; wrap-neutral nonlinear lag observers transport under budget o(log N) | PROVED | Same dossier; omitted-wrap mutation fails at carrier 0 |
| SCB-03 | Sparse finite-type carrier has N-Theta(log²N) original-tail zero-seam visits; elementary uniform rational separation exceeds 1/(32q³) | PROVED | Same dossier; changed selector explicitly retained |
| SCB-04 | Nested residue conditioning increases weighted signed energy by exact squared innovations; E differs from that norm by at most M/N | PROVED | [CRT energy](../research/2026-10-27/PI_CRT_ENERGY_REFINEMENT_OBSTRUCTION.md), alternating-sign counterexample |
| SCB-05 | Authentic E and completed-pi E differ by at most 4*pi*abs(h)*B*(1+M/N)/N | PROVED | Same dossier E2; full summed tail retained |
| SCB-06 | Fixed-M or existential sufficiently slow growing energy gates for all fixed nonzero modes are equivalent to normality | PROVED | E3; explicit order of quantifiers |
| SCB-07 | Every prescribed M tending to infinity with M=o(N) admits a normal carrier with limsup E=1 at every fixed h | PROVED | E4/E5; all-prefix normality, partial stages and endpoint error paid. Constructed carriers are Liouville |
| SCB-08 | Same-forcing finite-type sparse selector has all mixed-lag means tending uniformly to 1 for sublinear span and abs(h)=o(N²) | PROVED | [Moving-lag proof](../research/2026-10-27/PI_MOVING_LAG_SPARSE_OBSTRUCTION.md); tracks order, coefficient norm, span and tail |
| SCB-09 | Any finite nonzero Fourier band can vanish under a full-support strongly mixing singular radix law; higher mode has real part >49/900; a common full-measure set of generic carriers has irrationality exponent <=8/3 | PROVED | [Mixing proof](../research/2026-10-27/PI_MIXING_FINITE_SPECTRUM_OBSTRUCTION.md); explicit rational transition matrix and Frostman bound |
| SCB-10 | Exact rational source, phase enclosures, finite energies, finite cuts, refinement controls and mutation checks | VERIFIED_FINITE | [Receipt](../research/2026-10-27/PI_SIGNED_CANCELLATION_RECEIPT.json), [validation](../research/2026-10-27/PI_SIGNED_CANCELLATION_VALIDATION.md) |
| SCB-11 | Arithmetic refinement alone decreases energy; all discontinuous statistics escape transport; finite irrationality type alone forces o(N) zero-seam visits; old mixed losses force o(N); finite bands plus mixing select Haar | REFUTED with stated generic scopes | SCB-01–09 and SCB-14–15 supply distinct exact countermodels; no single countermodel is claimed to satisfy all hypotheses of the genuine source |
| SCB-12 | Selected pi zero-seam count o(N) | OPEN | A weaker next boundary theorem; would not establish digit uniformity |
| SCB-13 | Improved selected pi signed-Weyl order, prescribed authentic CRT energy decay, pi normality or RH | OPEN | No such conclusion established; inherited selected logarithmic saving unchanged |
| SCB-14 | Every prescribed M tending to infinity with M=o(N) admits one normal carrier with eventual separation 2^(-10)q^(-6), 4<=mu<=16/3, and liminf endpoint energy >=1/4 | PROVED | E6/E6a; marker, all-prefix normality and both rational determinant branches; exact finite marker controls |
| SCB-15 | Every prescribed M tending to infinity with M=o(N) admits one normal carrier with irrationality exponent <=4 and liminf energy >=1/4 along N=2^j for every fixed h | PROVED | [E7 proof](../research/2026-10-27/PI_NORMAL_FINITE_TYPE_ENERGY_OBSTRUCTION.md); exact conditional second moment, all-prefix counts and marker determinant bounds; no uniform Cq^(-4) asserted |

The new paper proofs use elementary radix geometry, conditional expectation,
explicit symbolic constructions and classical ergodic facts. The stronger
imported Kempner irrationality exponent two is not needed: an internal
exponent-three bound suffices for the sparse obstruction. The Gaussian atoms,
conductor clock, Pascal/Lucas geometry and Gamma normalization are retained as
upstream constraints, but no new theorem coupling all of them to selected
signed real cancellation is claimed.

The new frontier is summarized in the
[research synthesis](../research/2026-10-27/PI_SIGNED_CANCELLATION_SYNTHESIS.md).
