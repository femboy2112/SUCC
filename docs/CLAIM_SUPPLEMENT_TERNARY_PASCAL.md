# Weighted ternary Pascal and prime charts: claim supplement

**Namespace:** TPG. **Date:** 2026-10-24.
**Parent:** draft #272 at `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
**Authority:** paper proofs, named classical inputs, exact finite checks.
No new Lean authority or academic-priority claim. **Pi normality remains OPEN.**

The [synthesis](../research/2026-10-24/PI_TERNARY_SYNTHESIS.md),
[constructor proof](../research/2026-10-24/PI_TERNARY_CONSTRUCTOR.md),
[denominator and reset proof](../research/2026-10-24/PI_TERNARY_TRANSLATOR.md),
[coherent chart proof](../research/2026-10-24/PI_TERNARY_CHART_COHERENCE.md),
and [adversarial proof](../research/2026-10-24/PI_TERNARY_ADVERSARY.md)
state the domains, hypotheses, quantifiers, derivations, controls and next
falsification opportunities. This table indexes those scoped statements.

| ID | Statement | Earned status and boundary |
|---|---|---|
| TPG-01 | Weighted Pascal rows sum binom(k,j)2^j to3^k, and phase addition gives T_(3^k)x=sum binom(k,j)T_(2^j)x | CLASSICAL identity. Deterministic orbit coordinates do not become independent samples |
| TPG-02 | (E-4)/4 constructs a rational base3 source with alternating positive kernel error asymptotic Gamma(1/8)(4/k)^(1/8)/32 | PROVED PAPER for the fixed authentic source, all orders; no source-law invariance |
| TPG-03 | Common denominator4 is minimal for a fixed polynomial base3 shadow; it forces even errors Omega(k^-1/8). Denominator5 is the least permitting exponential decay and rate1/5 is optimal at that denominator | PROVED PAPER over all fixed polynomial degrees; does not cover varying-degree, matrix or modulo-one methods |
| TPG-04 | The unnormalized quarter-filter source retains the full nu profile and is a dyadic isometry, while normalized values have valuation v2(k)-2k | PROVED PAPER; a dyadic denominator is not a disappearing real carry |
| TPG-05 | P81=(E^2-E+3)/3 is a Pascal transform of the difference-table diagonal, with positive vanishing kernel and an explicit rational enclosure | PROVED PAPER; P81(t) lies in[11/12,1], with the sharp integer exponent8 comparison used in the translator bound |
| TPG-06 | Denominator3 is the global minimum among fixed filters for any3^m; at denominator3 endpoint conditions require4 dividing m, with m4 attained uniquely at degree2 | PROVED PAPER. Necessity for multiples of4 is not a sufficiency assertion for every such exponent |
| TPG-07 | The normalized base81 source has Newton coefficients3^-j Delta^j U_j, full uniform nu profile and a bijective analytic dyadic isometry | PROVED PAPER, all dyadic arguments and difference orders; source profile only |
| TPG-08 | A dyadically integral polynomial P with P(1)=1 and odd P'(1) preserves the source's nu profile | PROVED PAPER. Real kernel bounds and multiplier identification are additional hypotheses |
| TPG-09 | Base81 forcing is positive and completely monotone; its Newton coefficients are positive diagonal beta moments with a12^-j bound | PROVED PAPER. Rational values do not make it the original four-pole rational function |
| TPG-10 | A fixed original shift n>=2 and zero reset retain source isometry while the tail is asymptotic9/(64k^2) and forcing45/(4k^2) | PROVED PAPER, fixed n. New forcing's first-difference valuation2 differs from the original0 |
| TPG-11 | The reset constant T_n=16^(n-1)pi-U_n has the same fixed-base normality status as pi; base81 andbase3 normality are equivalent | CLASSICAL rational-affine and power-of-base preservation. No equality of arbitrary empirical laws or independent-base transfer |
| TPG-12 | For everyq>=2, oddd withq<=16^d and a=(q-1)/(16^d-1), (1-a+aE^d)^kU0 shadowsq^k alpha with positive error asymptotic1/(64a^2d^2k^2) | PROVED PAPER, fixedq,d; coefficient norm1 and positive completely monotone derived forcing |
| TPG-13 | The positive prime chart has Newton valuation nu(j)+j delta, exact distance scale2^-delta, and derivative of valuation delta=v2(q-1) everywhere | PROVED PAPER onZ2; normalized higher profile is nu(j)+(j-1)delta, not unchanged nu |
| TPG-14 | Prime charts below16 have distortion at most4; base11 has a two-state modulo3 local transform with O(n^-2) source error | PROVED PAPER. No uniform unnormalized distortion bound over all primes or statistical superiority is claimed |
| TPG-15 | Normalized prime charts have analytic inverse isometries, so chart transitions compose exactly with unit derivative | PROVED PAPER coherent coordinate transport. All domains remainZ2; not field maps between different completions |
| TPG-16 | Clock-respecting16-to4-to2 chart maps compose exactly, with dyadic scales1/2,1/2,1/4; real blocked source values agree toO(n^-2) | PROVED PAPER. Image embeddings and asymptotic real agreement are not finite polynomial identities |
| TPG-17 | Canonical affine filters are not multiplicative in the base; a scalar polynomial fourth root of the authentic shift on all translated states is impossible | PROVED PAPER with explicitP3^2 versusP9 counterexample and full-support moment proof. Other operator classes are not excluded |
| TPG-18 | Positive Pascal weights average unwrapped values without amplifying compatible absolute errors; fixed phase multiplication preserves entropy rate | PROVED PAPER/classical entropy inequalities. Averaging observables is a different operation and supplies no law preservation |
| TPG-19 | Naive unsigned/deblocked Pascal ternary constructions can have exponentially growing absolute errors | PROVED PAPER asymptotics and exact finite controls. No claim about distribution of the growing remainder modulo1 |
| TPG-20 | A biased binary Bernoulli law has positive all-scale collision dimension and exact doubling invariance but a tripling one-bit defect3/26 at bias1/4 | PROVED PAPER non-atomic counterexample; explicitly a changed law, not the authentic BBP source |
| TPG-21 | Finite tripling lookahead fails exactly on two alternating suffixes; their Haar mass is2^(1-L); oddq has(q-1)2^m ambiguous cells when2^L>=q | PROVED PAPER with finite-state carry explanation. Haar counts do not give BBP frequencies |
| TPG-22 | The finite-block tripling discrepancy bounds W1 by2^-m plus half its TV defect plus an explicit collision-controlled boundary budget | PROVED PAPER operational reduction; the authentic block discrepancy remains unbounded |
| TPG-23 | The four binary phase average inherits a positive collision exponent; its tripling invariance suffices to force the original T16-invariant law Haar | PROVED CONDITIONAL reduction with all cross terms and nonergodic residual paid. The weaker symmetry is open for BBP |
| TPG-24 | The local base81 transform uses three source states and a modulo3 carry; T81 symmetry is strictly weaker than T3 symmetry but eligible for the same collision-rigidity route | PROVED PAPER local identity and conditional implication. Neither source symmetry is proved |
| TPG-25 | The base81 quadratic is the norm(t-omega)/3 with omega^2-omega+3=0 and16-omega=conjugate(omega)^5 | PROVED exact algebra; no rotational or statistical inference |
| TPG-26 | A degree6 integer base31 filter simultaneously preserves the nu profile and has a vanishing moment remainder | PROVED PAPER secondary construction. Degree1 base31 was inherited; no real frequency improvement |
| TPG-27 | Exact independent source/kernel, denominator, dyadic, carry and coherence checks calibrate the instruments | VERIFIED_FINITE only to executed ranges and hashes in validation. Shared-model audits are not external refereeing |
| TPG-28 | Authentic positive all-scale real collision control, same-law symmetry under3/11/81, four-phase symmetry, and pi normality | OPEN. Source constructions and proved local differentials do not discharge these statistical requirements |

## Reproduction and provenance

Read [the frozen contract and split disclosure](../research/2026-10-24/PI_TERNARY_HOLE_CONTRACT.md)
and [validation record](../research/2026-10-24/PI_TERNARY_VALIDATION.md).
The primary exact instrument is
[pi_ternary_pascal_probe.py](../scripts/pi_ternary_pascal_probe.py), with a
separate late [convex-chart probe](../scripts/pi_ternary_convex_probe.py).
Independent carry and polynomial-filter calibration scripts are also preserved.
Historical claim rows, imported originals and prior source implementations
remain unchanged.
