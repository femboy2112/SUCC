# Internal hostile audit — Adelic solenoid and Poisson reconstruction

**Date:** 2026-10-15. **Review status:** internal source/proof audit, NOT independent peer review.
**Manuscript:** research/2026-10-15/ADELIC_SOLENOID_POISSON_RECONSTRUCTION.md
**Research branch:** research/pontryagin-finite-adelic-duality-2026-10-15 (stacked draft PR #129).
**RH PROVED: NO.**

## Independent proof map and theorem status

| Mathematical assertion | Actual proof obligation | What finite programs do NOT prove |
| --- | --- | --- |
| A/Q ~= (R x Zhat)/Z, compact covolume 1 | Af=Q+Zhat, Q intersect Zhat=Z; open subgroup quotient; fundamental [0,1) x Zhat | All R, Zhat points or empirical access |
| (A/Q)^dual ~= Q_discrete | R^dual=R, Zhat^dual=Q/Z, diagonal Z annihilator lambda+r in Z; compact dual discreteness | Surjectivity on all continuous characters from finitely sampled ones |
| Q^perp=Q under normalized adelic Fourier | Local Qp nondegeneracy, restricted-product duality, solenoid character classification | Finite phase matching as proof of a global annihilator |
| S(Af) exact span of rational coset indicators | Compact support, local constancy, subgroup base D Zhat, Af=Q+D Zhat | A Gaussian-only or one-prime-only basis |
| Fourier coset and full Poisson | Haar subgroup orthogonality + ordinary real Schwartz Poisson + finite tensor linearity | Infinite equality from numerical agreement |
| Outward rational Gaussian control | Proof-backed pi and exponential enclosures, tail bounds from exp(x)>=x^2/2 and pi>3 | RH, analytic continuation, or all-test positivity |

## Alternative formula derivation (external theorem, independent route)

For each true basic test f=phi(x_infty) times indicator_(u+D Zhat)(x_f), with u,D rational, D>0, real phi Schwartz:

1. Rational intersection Q intersect D Zhat is D Z, hence primal sum over x=u+Dn exactly.
2. Haar volume of D Zhat equals 1/D by the full rational product formula.
3. Its finite Fourier transform equals (1/D) psi_f(u y) indicator_(D^-1 Zhat)(y).
4. Dual diagonal rational frequencies are exactly y=m/D, m integer. Real Fourier sign is plus and finite sign minus, yielding exp(-2*pi*i*u*m/D).
5. Real Poisson on u+D Z with the positive real Fourier convention gives the equality of source and dual lattice sums for ALL phi in S(R).
6. Finite rational coset spanning extends the result linearly to ALL S(A)=S(R) tensor_alg S(Af).

This avoids relying on finite Gaussian numerical agreement. The competing classical approach proves the same formula through Fourier inversion on compact A/Q (Poonen Theorem 5.7); its different assumptions give a genuine route for hostile triangulation.

## Required negative controls

- Flip only the finite Fourier sign: diagonal Q is no longer annihilated in general.
- Delete finite Haar 1/D: a rigorous outward rational Gaussian test at D=2, heat=1 has provably disjoint primal and mutant dual ranges.
- Replace dual annihilator D^-1 Zhat with D Zhat: wrong support and incorrect topology.
- Drop newly added p-adic source coordinates: phase naturality fails at the already identified rational principal-part source.
- Claim Gaussian theta alone proves Poisson for all Schwartz-Bruhat: REFUTED without the rational coset spanning lemma.
- Promote finite congruence agreement to all-global-carrier identity: CRT projectors and 0 vs lcm(1,...,H) provide exact aliases.
- Equate positive auxiliary Hilbert covariance with the signed Weil functional: source identity is missing, and RH positivity cannot be presumed.
- Confuse a genuine cyclic modulus 6 with a fake standalone Euler place p=6.
- Confuse a declared source token with authenticated physical instrument access.
- Silently use the complete real carrier from rational Cauchy charts alone.

## Validation evidence

Focused GitHub push run at the proof/test checkpoint 8dc7e714dc53: https://github.com/femboy2112/SUCC/actions/runs/38816772603 .
Python 3.10 and Python 3.13 both passed 52 focused exact tests in seven suites: cyclic duality 11, finite-adèle quotient 11, earlier Tate S-chart 3, finite cyclic Poisson 5, global solenoid 9, rational Schwartz cosets 10, outward Gaussian interval 3. Source provenance verified in both CI jobs. A subsequent review-document commit does not change mathematical source code; CI must still be checked at the final branch head.

Historical failures are retained: cyclic period test referenced an undefined variable; identity gauge added a redundant zero program node; an attempted Gaussian half-shift used an exp input outside the certified analytic interval. The test or representation was corrected, NEVER the mathematical theorem weakened.

The mandatory full-repository CI suite is distinct from this focused validation and must be checked separately. No peer reviewer has approved the paper.

## Next research and review priorities

1. Independently scrutinize topological claims: uniform compact-open subgroup for finite adelic Schwartz functions, quotient topology, Haar normalization and all-valued Schwartz domain.
2. Recover Tate's complete idelic Mellin zeta integrals, Gamma factor, residue poles and functional equation from these same source-justified generators, then compare with the existing SUCC all-places zeta modules.
3. Challenge against primitive odd Dirichlet character chi4: conductor, parity, local epsilon/root number, genuine Euler labels, signed theta.
4. Construct and attempt to falsify a typed functor from Tate Schwartz/ideles to the ENTIRE completed signed Weil distribution with uniform analytic errors. No nontrivial zero positions as inputs, no fake-composite or matched non-Euler control excluded.
5. Independently prove Weil positivity or sharpen an obstruction. Finite Gaussian/Poisson positivity does NOT imply RH.
6. Consider Lean formalization of one bounded theorem first (finite cyclic character naturality or CRT quotient), not an unverified claimed complete formalization of A or RH.

## Attribution

The base number theory is CLASSICAL: John Tate (1950); Bjorn Poonen, Tate's Thesis, MIT §5.5 Theorem 5.7, https://math.mit.edu/~poonen/786/notes.pdf ; Jordan Bell, Pontryagin duals and adeles, https://jordanbell.info/LaTeX/mathematics/Qdual/ . The contribution here is SUCC's typed proof/observation reconstruction and adversarial implementation, not new academic priority in Poisson summation.

**RH PROVED: NO.**
