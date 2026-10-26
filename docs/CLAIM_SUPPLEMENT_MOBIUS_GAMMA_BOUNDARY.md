# Mobius/Gamma boundary claim supplement

Date: 2026-10-25. Family **MGB**, local to this research branch. Parent PR #297
at `eca4462ee4d62642b15c4af672136aa5bcacd00b`. Shared theorem registry
integration is deferred to a coherent merge. **Pi normality and RH: OPEN.**

Main authority: [proof report](../research/2026-10-25/MOBIUS_GAMMA_BOUNDARY_REPORT.md).
Validation: [actual runs](../research/2026-10-25/MOBIUS_GAMMA_VALIDATION.md).
Classical sources and inherited lemmas are identified in the linked dossiers;
no independent scholarly priority or new Lean authority is claimed.

| ID | Domain, statement, and hypotheses | Status / evidence | Boundary and next probe |
|---|---|---|---|
| MGB-01 | Real c: H_N-log(e^c N)->gamma-c; shifting the Euler field leaves its successor defect invariant and changes its infinite boundary to -c | PROVED PAPER; finite shift identity, inherited certified gamma intervals | c=gamma uses gamma in the reference; it does not derive gamma or change its standard value |
| MGB-02 | Gamma_c(z)=exp(c(z-1))Gamma(z): psi_c(1)=c-gamma, successor multiplier exp(c); BBP Gamma primitive scales by exp(-15c/8) | PROVED PAPER; direct derivative/product identities | Cannot retain all canonical normalization conditions while changing only the finite part |
| MGB-03 | a>0: Q(a)=Gamma((a+1)/2)/Gamma(a/2), Q(a+1)=a/[2Q(a)]; two-step multiplier (a+1)/a | PROVED PAPER, classical Gamma recurrence; independent finite/numerical checks | Reciprocal successor is not identity holonomy and not identified with BBP orbit phases |
| MGB-04 | Same positive Euler defect delta(n): ordinary sum gamma, alternating sum log(4/pi); real-positive generalization and reflection | PROVED PAPER, classical digamma/Wallis inputs; rational outward intervals | A source sum identity does not establish statistics of e(hU_n) |
| MGB-05 | J>=0: exact dyadic decomposition gamma=sum_(j<J)2^j A(2^j)+positive remainder <zeta(2)/2^(J+1) | PROVED PAPER; parity telescope and all-index source bound; finite certificates | Classical Gamma expressions; no academic novelty claim or normality transfer |
| MGB-06 | Original four signed BBP poles: Gamma product successor derivative equals8r, ordinary tail is -(log G)'/8 | PROVED PAPER; exact rational identities and independent product construction | Ordinary tail and discounted Green tail are distinct |
| MGB-07 | Canonical Gamma primitive: logG(0)=(15/8)gamma+positive zeta-series; inherited B'(0)=logG(0)-(15/8)log8 | PROVED PAPER; two certified rational enclosures; missing-compensator and scale mutations rejected | Balanced derivative cancels gamma; primitive coefficient depends on declared normalization |
| MGB-08 | N>=1, real fixed lambda,beta: finite seam selector (beta-U_N)/(16^N-lambda), with all/none singular cases; authentic iff beta=U_N | PROVED PAPER; exact convolution and seam controls | A finite seam is not a cyclic extension of nonperiodic forcing |
| MGB-09 | Sign seam has fixed-index limit -T_n and terminal profile alpha16^(-j) | PROVED PAPER; exact tail-enclosed errors | Convergence is nonuniform at the moving endpoint |
| MGB-10 | Fixed nonzero h, N=4m sign seam: m*(1-|mean e(hX)|)->(1/3)sum_j[1-cos(2pi h alpha16^-j)]>0 | PROVED PAPER with explicit finite error S-4; certified character-box holdouts | This control has m^-1 loss, unlike inherited carefully tuned m^-4 family |
| MGB-11 | Projective J(y)=1/y reverses F(y)=16y but F fails to descend under y~1/y; Fourier reflection gives conjugation, not additive negation | PROVED PAPER; exact rational quotient witness | Does not exclude other correctly defined geometric constructions |
| MGB-12 | Every time-preserving source-commuting map family H_n fixing initial0 fixes U_n pointwise, without a linearity assumption; affine families additionally classified | PROVED PAPER; induction; affine coefficient classification and exact conjugacy checks | Nonlinearity alone does not escape; next nontrivial operator must mix times or leave pointwise equivariance |
| MGB-13 | q=1/16 seam products give q-Pochhammer and q-Gamma ratio; rational infinite-product/series bounds | PROVED PAPER, classical q-products; exact finite tests | Products across horizons are declared aggregation; source-erasure control survives |
| MGB-14 | q->1: gamma_q->gamma, reference multiplier ell shifts limit by log ell; sign-twisted derivative tends -log2; modular product finite part -log2/2 | PROVED PAPER, classical q-Gamma/modular inputs and convexity argument | q->1 changes multiplier; not an asymptotic of fixed base16 |
| MGB-15 | Gamma recurrence/reflection/positivity alone admit periodic gauges shifting psi(1); source-only identities admit periodic BBP selected seeds | PROVED PAPER, inherited gauges with strengthened reflection/jet accounting | Exact forcing plus U0 already fixes the orbit; no theorem establishing its equidistribution is supplied |
| MGB-16 | p=8m+1 prime, N=4m: simple sign seam imports p-primary mass before birth and changes first-window numerator4*16^t to2*16^t | PROVED PAPER using inherited first-birth theorem; four exact prime holdouts | Unlike the PRK p-free tuned controls, this seam changes the selected prime clock |
| MGB-OPEN | A source-authenticated time-mixing or other richer transform proves signed cancellation for actual U0=0 | OPEN | Retain full numerator and prove a genuine bound; renamed Weyl sums do not count |

Analytic proofs and finite computations have separate authority. Agents share
a model family and repository provenance; their agreement is not independent
external refereeing. Exact source recurrence, independent product expansions,
rational interval bounds and hostile mutations provide different failure
modes. No diagnostic score is a truth probability.
