# Next π handoff: retain the null information, then bound its signed source pairing

Read the [synthesis](../research/2026-10-26/SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md),
[claim supplement](../docs/CLAIM_SUPPLEMENT_SEINFELD_REALIZATION.md), and
[actual validation](../research/2026-10-26/SEINFELD_REALIZATION_VALIDATION.md).
This work starts from PR #313 at
`79344c62c39c96755b742700b3d4d22fa60d86da`. Recheck live heads before continuing;
sibling #311 is inspected, not an ancestor. No main merge is authorized by this
research branch. Imported archive/source bytes remain unchanged.

## What the round actually closes

The user's inverse-averaging proposal now has an exact implementation:
joint law = declared uniform lift of coarse law + labelled fibre-null residual.
That residual is a Seinfeld zero witness against all pulled-back coarse
observables. It can pair nontrivially with a branch-sensitive observable.
Keeping it reconstructs the full law; its evaluated zero does not reconstruct
the lost information or a realized atom.

For each rational sixteen-branch row, keep the exact fields at modes $1,2,4,8$.
Their rational dimensions are $8,4,2,1$. Keep each packet attached to its source
label and its real tail phase. Neither the two separate marginals nor all
aggregate branch modes reconstruct that coupling. Every deterministic selector
has the same stratum energies, and the native authentic two-row swap exposes
the difference using the actual four-pole source values.

On a fixed finite virtual path law, selected expectation minus reference
expectation is exactly the signed likelihood/observable innovation pairing.
For a uniform inverse tree, a given nonconstant Fourier mode has exactly one
revelation level. All selected unit phase is restored there. This is now proved
and independently calibrated; do not rediscover it as gradual per-level loss.

The field idea is also concrete. The two-arm current-growth model differs from
fixed sampling and Pólya reinforcement, and it changes equal-terminal path odds.
Its log likelihood contains accumulated nonharmonic normalizers. The native
DtN machinery remains the source of the general field/history framework.

A further exact connection reconstructs the earlier golden–Gamma family from
path inference. Uniform latent bias conditioned on $m-1$ iid-given-bias failures
gives $X_m=m\Theta$ with density $(1-x/m)^{m-1}$. Its logarithmic coordinate
$Z_m=-m\log(1-\Theta)$ is exactly Exp(1) at every finite $m$; exponential
tilting and rescaling preserve its law. The inherited Euler error is exactly
$\epsilon_m=\mathbb E(\log Z_m-\log X_m)$, and the previously proved authentic
tail comparison gives $T_m\sim\epsilon_m^2/16$. See
[the posterior proof](../research/2026-10-26/POSTERIOR_GOLDEN_GAMMA_CONNECTION.md).
This does not identify the arithmetic trajectory with the Bayesian experiment.
Conditional independence, prior and normalization are explicit hypotheses;
the infinite all-failure event has probability zero, and a marginal coupling
does not assert convergence along one fixed latent-bias sample path.

## What remains exactly unchanged

The original arithmetic is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\qquad U_{n+1}=16U_n+r(n+1).
$$

The target is still

$$\sum_{n=1}^N e(hU_n)=o(N)\quad\text{for every fixed }h\in\mathbb Z\setminus\{0\}.$$

The previously proved summable Green correction transfers this to the π orbit.
No selected-modulus order improvement occurred in this round. The #311 direct
absolute-loss coefficient improvement is not a normalized saving or a new
result of this branch. The latent-path laws are declared references; they are
not stochastic laws from which the unique original zero-seed trajectory is
known to have been drawn.

## The smallest useful next source object

Reuse #313's **signed** carry/arrival approximation at the prescribed schedule
$M_N=\max(2,\lfloor\log_2N\rfloor)$. Write

$$
\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
e\!\left(\frac{h(c_{n+1}+\tau_{b_n})}{16}\right),\qquad
b_n=\lfloor M\{U_{n+1}\}\rfloor,\quad\tau_b=(b+1/2)/M.
$$

The original source already pays

$$
\left|N^{-1}\sum_{n=1}^N e(hU_n)-\widetilde C_{N,M}(h)\right|
\le\frac{\pi|h|}{16M}+\frac{\pi|h|}{8N}\sum_{n=1}^N r(n+1).
$$

Retain the full rowwise signed Fourier packets before summing over bins.
The new codec is a lossless representation of these rows, not an estimate.
The next theorem must bound their **source-correlated signed sum** at this
prescribed growing resolution. Exact fine conditioning instead returns unit
energy, as #313 already proves. Do not make a schedule depend on observed
Fourier cancellation and then call the schedule an arithmetic mechanism.

## A genuinely discriminating operator route, with its two debts exposed

For a declared finite kernel $P$ and unit phases $g$, a quantified pair of
positive-probability paths that reconverge with separated accumulated phases
gives a contraction of the twisted kernel $T_g$. This round proves the finite
criterion and its coboundary obstruction. A source-faithful application needs
both of the following, established separately:

1. An explicit map from original BBP records to the proposed kernel/phase
   observable, with a proved error $\eta_{N,h}\to0$ when comparing its output
   to $\widetilde C_{N,M_N}(h)$. Time correlations, retained null residuals,
   source labels and all coarse-graining errors must be included.
2. An independently derived arithmetic path-separation estimate. If the
   construction yields length $m_N$ and loss $a_N>0$ with
   $\|T_N^{m_N}\|_\infty\le1-a_N$, it must also prove that the number
   $L_N$ of operator steps in the transported observable satisfies
   $a_N\lfloor L_N/m_N\rfloor\to\infty$. A contraction for an unrelated
   ensemble, or at a scale with a vanishing cumulative loss, is insufficient.

The resulting bound would have the transparent shape
$|\widetilde C_{N,M_N}(h)|\le\eta_{N,h}+
(1-a_N)^{\lfloor L_N/m_N\rfloor}$, for norm-one initial/final data.
**This is a conditional proof gate, not a constructed BBP operator or a new
normality theorem. Both debts are OPEN.** If the proposed phases are an exact
coboundary, the uniform contraction route fails; selected coefficients can
still cancel, so this does not close off every spectral argument.

The cheapest first probe is to write the source/observable map before measuring
an eigenvalue. Run it on the authentic prefix and the existing same-forcing,
changed-seed controls, and account for every weight change. A source-preserving
stochastic extension at the complete arithmetic-state level has no such free
contraction: its projected next phase is deterministic. A useful coarse model
must explicitly retain and control the information discarded by its quotient.

## Boundary controls that future claims must survive

| Proposed shortcut | Executed/proved control |
|---|---|
| Average first, invert later without memory | Same coarse law, different observable; kernel residual carries the missing pairing |
| Keep four numbers or only their energies | Four field elements require fifteen rational coordinates; all Dirac energies coincide |
| Keep source and branch marginals separately | Authentic two-row swap changes the actual tail-weighted character |
| Fine conditioning creates uniform inverse randomness | Native odd selection is Dirac; all-carrier continuous minimax error is one for $16\nmid h$ |
| Selection has a small universal information cost | Uniform-tree point selection has chi-square $b^d-1$, identical for every selected word |
| Local phase losses multiply | Biased-sign coboundary has local modulus $1/2$ and total expectation $1/2$ forever |
| A changed predictive probability proves physical reinforcement | Pólya reinforcement equals static-Beta learning on every finite path |
| Any feedback is terminal conditioning | Field paths LLR/LRL have equal terminal counts but relative odds $3/4$ |
| Auxiliary mixing cancels the original next phase | Deterministic-factor theorem; leakage bound $1-2\epsilon$ before it reaches zero |
| A factorial/log potential makes Euler's constant necessary | The toy potential is declared and unauthenticated for BBP; prior reference-shift controls persist |

The triangle and mirror-language may organize the constructions, but every
arrow used in a proof must specify its domain, retained labels, pushforward or
pullback direction, and normalization. A categorical zero does not remember a
path unless the carrier retains it. Negative signed residuals are legitimate;
negative probability weights are not being introduced.

## Reproduction and review discipline

Use the commands in the validation record. The new replay regenerates source
hashes and every displayed finite value; it rejects altered status flags and
arithmetic receipts. The standalone oracle has no imports from production or
tests and explicitly checks the raw/canonical/literal inverse-digit conventions.

## Publication-time #314 connection and additional discriminator

The concurrent draft #314 at `935c2db4c36ff56d90acd82eae30bcce15b6a053`
was inspected after the initial publication of #315. Read the
[compatibility and posterior addendum](../research/2026-10-26/SEINFELD_COHERENCE_POSTERIOR_BRIDGE.md).
The sibling remains unmerged; its isolated shim tests are a different
validation scope from this branch's native suite.

Its formal rational group-algebra amplitudes correspond exactly to our mass
plus four cyclotomic packets. Add its strong-lumpability test to the proposed
source quotient: states with the same class must induce the same next-class
law, or the discarded memory must be restored. Preserving a present phase is
not sufficient to iterate the construction.

The new comparison makes the constants test stricter. Under the declared
16-color urn, avoidance of color zero and the fully specified constant word
$1^r$ both give the same scalar Beta$(1,15+r)$ posterior. They therefore share
the entire exponential/golden–Gamma/log-defect bridge. Nevertheless the
conditional latent Fourier second moments tend respectively to $1/15$ and $1$,
and those moments govern future observed averages. Any proposed authentic-source
cancellation mechanism must distinguish these joint laws despite their identical
scalar marginal. The addendum proves the formulas and its standalone oracle
checks the finite path probabilities and predictive moments without importing
either branch's production code.

Production modules and their tests were frozen for the final full suite.
Same-model collaboration and independent algebra are recorded as such; they are
not external peer review. Universal statements have paper proofs; finite
checks and inherited Lean proofs are not promoted to a new analytic theorem.
