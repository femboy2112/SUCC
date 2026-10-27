# Claim supplement: Seinfeld inverse averaging and realized paths

**Scope:** the continuation of PR #313 at
`79344c62c39c96755b742700b3d4d22fa60d86da`. These are named local claims;
no existing claim identifier or namespace is reassigned. See the
[synthesis](../research/2026-10-26/SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md),
[contract](../research/2026-10-26/SEINFELD_REALIZATION_CONTRACT.md), and
[validation](../research/2026-10-26/SEINFELD_REALIZATION_VALIDATION.md).

| Named claim | Domain, hypotheses and quantifiers | Status and evidence | Countermodel or next falsifier |
|---|---|---|---|
| Retained fibre residual | Every finite projection and rational probability law; uniform lifting is a declared section | PAPER-PROVED classical split; native `ZeroWitness` interface and exact tests | Averages alone alias two Dirac laws on any nonconstant fibre observable |
| Linear recovery dimension | Rational-linear recovery of every row, or fixed-mass probability rows with positive marginal fibres | PAPER-PROVED rank/nullity; dimension per 16-fibre is 15 | Fixed zero-mass fibres reduce the feasible dimension; no nonlinear coding lower bound claimed |
| Four-field branch codec | Every signed rational row of length 16; channels at 1,2,4,8 in their exact cyclotomic subfields | PAPER-PROVED antipodal inverse and Galois reconstruction; independent rank and polynomial checks | Every omitted stratum has strictly positive aliases; four field elements are not four rational coordinates |
| Energy does not select a phase | Every Dirac row on the sixteen branches | EXACT universal calculation, energies $(8,4,2,1)$ | Sixteen distinct primitive phases share that energy profile |
| Authentic joint-coupling obstruction | First two native positive-time records; same source and branch marginals after swapping digits | PAPER-PROVED symbolic full-character difference; exact native source values | Swapped predecessors have even denominators and fail the original odd passport |
| Likelihood/observable innovation identity | One finite filtered law, $Q\ll P$, terminal measurable $F$, trivial initial sigma-field | CLASSICAL/PAPER proof; exact rational implementation and independent enumeration | Nontrivial differing initial laws require an initial term; positive energies omit signed correlation |
| Single inverse revelation | Every finite radix $b\ge2$, depth, integer harmonic, uniform inverse-fibre reference | PAPER-PROVED root sum; source-authenticated window wrapper and independent oracle | Whole-conductor modes are constant; reversed reveal order and literal/raw digit identification are false |
| Selected-word cost | A point law in a uniform finite radix tree | PAPER-PROVED second moment, chi-square and entropy; exact finite checks | The same cost holds for every word, so it cannot discriminate normality |
| Continuous selector barrier | Entire odd-rational circle carrier; $16\nmid h$; continuous complex approximants | PAPER-PROVED sharp uniform minimax error one and finite Lipschitz witnesses | For $16\mid h$ error is zero; no selected-orbit/weak-norm obstruction follows automatically |
| Endpoint odds invariant | Finite Markov law, fixed initial state, nonnegative terminal tilt with positive normalizer | CLASSICAL Doob identity, reused native implementation | Full-history state enlargement changes what counts as the endpoint |
| Recomputed-field path defect | Declared two-arm resistance graph, exponent-one current growth, before breakthrough | PAPER-PROVED $3/4$ equal-endpoint odds and general adjacent-swap identity | Terminal geometry does not retain the full path order in this toy; no measured lightning/wood or BBP model claimed |
| Log normalizer history | Positive state potentials on finite supported paths; normalized kernel transform | PAPER-PROVED telescoping with running normalization defect; factorial-potential instance | Dropping the running defect is valid only for a harmonic space-time potential |
| Reinforcement/inference alias | Every finite two-colour word; positive Pólya/Beta parameters | CLASSICAL all-word equality with exact finite implementation | Identical observed laws need not identify interventions or physical reinforcement |
| Posterior golden–Gamma connection | Uniform latent bias, conditionally iid letters, finite all-R prefix, declared scaling $X_m=m\Theta$ | PAPER-PROVED interpretation of the inherited beta family; exact $Z_m=-m\log(1-\Theta)$ is Exp(1), with $\epsilon_m=\mathbb E(\log Z_m-\log X_m)$ | Shared-coin dependence, changed prior or scale alter the construction; no single-latent sample-path limit or BBP path sampler is identified |
| Posterior/error comparison | Original zero-selected four-pole Green tail and Euler remainder at each integer $m\ge1$ | INHERITED PAPER theorem $T_m\sim\epsilon_m^2/16$ with all-$m$ bounds, now given a posterior log-defect interpretation | No selected Weyl bound follows; arbitrary common centering cancels from the error |
| Deterministic arithmetic factor | Full original forcing and zero seed; auxiliary outcomes preserve the selected successor almost surely | PAPER-PROVED one-transition character identity and all-time deterministic projection | Time averages can cancel; uncertain-seed ensemble cancellation is a different observable |
| Approximate-factor leakage | Unit observable, selected successor has probability at least $1-\epsilon$ | PAPER-PROVED sharp lower bound $\max(0,1-2\epsilon)$ | Antipodal contaminants attain the bound for $0\le\epsilon\le1/2$ |
| Local-loss product rejection | Biased independent signs with adjacent telescoping phases | REFUTED naive product bound; exact $1/2$ for every horizon and idempotent twisted matrix | Null bias/horizon one are equality controls; the instance flag distinguishes them |
| Twisted-kernel contraction | Declared finite irreducible stochastic kernel, supported unit edge phases | PAPER-PROVED unit-spectral-radius classification and quantified reconvergence criterion | Coboundary phases retain a unit eigenvalue; individual coefficients can still vanish |
| Arithmetic feedback identification | A specified field/path model transported to the original zero-selected observable | OPEN | Any unaccounted change of seed, source, projected successor or time law invalidates the bridge |
| Selected temporal cancellation | Every fixed nonzero integer $h$, original four-pole zero-seed history, all horizons | OPEN; no new $o(N)$ estimate or better selected-modulus order | Retaining/renaming the signed sum is not bounding it |
| Oily-macaroni cancellation invariant | Source-dependent role of $\varphi^{-1}-\gamma$ robust under prior representation controls | OPEN | Common centering leaves Fourier moduli unchanged; toy factorial potentials do not establish necessity |

## Proof and evidence map

- [Null residual and Fourier codec](../research/2026-10-26/SEINFELD_NULL_RESIDUAL_AND_FOURIER_CODEC.md)
  supplies the first five claims and the deterministic odd-selector tag.
- [Selection likelihood and revelation](../research/2026-10-26/SELECTION_LIKELIHOOD_AND_REVELATION.md)
  supplies the filtration, selector approximation, adaptive covariance and twisted-kernel proofs.
- [Realized fields](../research/2026-10-26/REALIZED_PATHS_AND_FIELD_FEEDBACK.md)
  supplies the conditioning, geometry, inference, normalization and factor proofs.
- [Posterior golden–Gamma connection](../research/2026-10-26/POSTERIOR_GOLDEN_GAMMA_CONNECTION.md)
  links the latent path model to the prior finite common source and inherited
  BBP error comparison, with extra assumptions and countermodels explicit.
- [Exact receipt](../research/2026-10-26/seinfeld_realization_validation/exact_receipt.json)
  hashes the native sources, new implementations and tests; its regeneration is
  a finite check, not a substitute for the quantified proofs.
- [Independent oracle](../research/2026-10-26/seinfeld_revelation_oracle.py)
  uses only standard-library rational and polynomial arithmetic. Its
  [receipt](../research/2026-10-26/seinfeld_revelation_oracle.json) exposes the
  actual cases and counts.

No new Lean kernel authority, independent external peer review, scholarly
priority, π-normality result or RH consequence is asserted.
