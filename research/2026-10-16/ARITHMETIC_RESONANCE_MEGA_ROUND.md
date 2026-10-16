# Arithmetic Resonance: source response, exact wavefronts and retained soft-mode debt

**Original first-prime Schur sign OPEN. RH PROVED: NO.**
This round improves both sides of the authentic zero-shift Schur enclosure and
proves a conditional source-specific dense-response theorem. It does not prove
fractional spectral rigidity or a computable vanishing inverse-spectral tail.
No nontrivial zero coordinates were used to construct these source certificates.

## Source, lineage and authority

The isolated SUCC branch is
`research/arithmetic-wavefront-spectral-response-2026-10-16`, a child of
`24d0f18a103fb2add32ee817fdfefb4ff401ed27` ([parent draft #135](https://github.com/femboy2112/SUCC/pull/135)).
The reviewable publication is [draft #137](https://github.com/femboy2112/SUCC/pull/137).
The actual source blob remains `0cc8510b71d178fc79e8d410a86d8b6014cf9178`,
SHA256 `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`,
origin commit `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`.
Academic main was `02fc9f46ad3b914d49df7a658e304d06ed8a6200` at the live audit.
Original worktrees, research archives and main were not modified.

The formal child is `research/arithmetic-response-kernel-2026-10-16` in YEAN,
from `4bda4fc92f722464d17a3911ccc12f7f28193e6b`
([parent draft #136](https://github.com/femboy2112/YEAN/pull/136)).
Its exact final commit and fresh proof receipts are recorded in the integration
receipt. Historical formal results remain historical; local replay is not hosted CI.
YEAN is published at `2c44b033e400801ceceaf5758bc0671b4226e1e6`,
[draft #137](https://github.com/femboy2112/YEAN/pull/137).

The founding 72-entry provenance manifest and this later Suzuki source lineage
are distinct. The real Gamma completion, contact, both pole channels and the
actual log2/sqrt2 hinge were retained. The genuine kernel is compared with
[Suzuki's formula (1.3)](https://arxiv.org/html/2606.09096v3); no positive auxiliary
Gram is substituted. Source identification is a paper-level comparison,
separate from byte integrity and finite execution.

## Solved geometry and a corrected premise

For an isolated hinge `c(|r|-b)_+`, a>0, b>=0, delta=(2a-b)_+,

    ||H||_HS² = c² delta⁴/6,
    ||partial_x H||_HS² = c² delta².

The proof uses the overlap measure 2(2a-r)dr on the square and weak derivatives.
Exact mixed-hinge formulas, symbolic integration, and an independent two-variable
kernel integration check the implementation. Whole-line h'' gives the two delta
atoms and 2c cos(b omega); hard windowing adds explicit endpoint delta and
delta-prime terms. Those cosines are not finite-window eigenvalues.

The prompt's generic derivative-after-projection contraction is false. A rank-one
Legendre operator gives squared ratio 8/7. Projection contracts HS norms only in
the appropriate order; differentiating an output projection is a different map.
For the actual isolated prime 2 component at a=1/2, a separate source calculation
proves a squared ratio below 1/5. This does not transfer to the complete signed
source or its response. Details and exact witnesses are in
[the hinge dossier](PRIME_WAVEFRONT_HILBERT_SCHMIDT.md).

## The spectral object and the arithmetic range result

For finite-dimensional low L and positive high D, define mu(E)=B 1_E(D) B*.
Under the actual square-root range condition,

    R0 = integral lambda^-1 dmu(lambda),
    Rweak(tau) = integral_(0,tau] lambda^-1 dmu(lambda).

The finite low dimension gives norm convergence of this tail to zero, without
a rate. Conditional mass and fractional-range theorems are proved in
[SPECTRAL_RESPONSE_MEASURE.md](SPECTRAL_RESPONSE_MEASURE.md). In particular,
`mu((0,t]) <= C t^(1+alpha) I` implies the tail bound
`C(1+1/alpha) tau^alpha I`; `B*=D^(1/2+eta)V` with bounded V and
0<eta<=1/2 implies the requested tau^(2eta) and epsilon^(2eta) bounds, with
sharper constants retained. These are classical functional-calculus consequences,
not evidence that their arithmetic premises hold.

A fixed compact diagonal control d_j=4^-j, b_j=2^-j/j is in the square-root
range and in no stronger fractional range. Its inverse tail is at least 1/n at
tau=4^-n. Further, any finite number of nonnegative moments can be held exactly
fixed in a positive atomic family whose inverse moment is unbounded. These
countermodels rule out general shortcuts based on compactness or finite moments.

The authentic source yields a stronger qualitative statement. Let
I=(-1/2,1/2), M=polynomials-through-degree3 perpendicular, Q=polynomials-through-
degree4 perpendicular, T the g' convolution and R_Q=Pi_M T|Q. Then

    R_Q* = -QT|M.

The genuine Gamma multiplier has logarithmic growth. Its exterior kernel is
bounded by 3/(2r), giving a Carleman L2 estimate. If its interior distribution is
L2, patching interior and exterior representatives leaves only endpoint-supported
distributions; H^(-1/4) membership excludes them. This proves the needed maximal
multiplier-domain assertion without assuming endpoint traces or an operator core.
A moment-preserving smooth form core and the inherited `D>=kappa K_Q`,
kappa=20699/10^6, then give

    ker R_Q* = {0},   closure Ran R_Q = M.

This is an independently audited **conditional paper proof**, not Lean analysis.
It implies that all four relative residual targets can be approximated by high
polynomials. It gives neither an attained response nor a rate nor convergence of
a chosen energy-Galerkin sequence. The clamped-biharmonic and graph-norm
counterexamples retain their original force.

A principal corollary makes the distinction sharper. Since g' is L2 on this
finite difference interval, T and hence R_Q are Hilbert-Schmidt and compact.
R_Q cannot be onto the infinite-dimensional M: the open mapping theorem would
put a fixed M-ball in the image of a bounded high ball, whereas compactness would
make its closure compact, impossible in infinite dimension. Thus the dense range
above is nonclosed. Some residual targets are unattainable, and there is no
bounded right inverse on all M. This classical compactness argument does not
decide attainment of any of the four particular low-source target columns.

The late [independent residual-method review](../../reviews/2026-10-16_OPTIMAL_RESIDUAL_COROLLARY_AUDIT.md)
closes a further qualitative implication. Let U_N minimize each actual continuum
residual over span(P5,...,PN). Coercivity makes R_Q injective, so these finite
minimizers exist uniquely. Projection onto the nested image spaces gives

    C_N = R_P* (I-Pi_(R_Q X_N)) R_P decreasing to0 in low operator norm,
    ||H_(U_N)-S0||, ||H_(U_N)-kappa^-1 C_N-S0|| <= kappa^-1 ||C_N|| ->0.

These are source-specific, conditional paper consequences of the proved density
and inherited Schur bracket. They establish convergence for the residual objective,
not for ordinary energy Galerkin. The upper matrices themselves need not be
monotone; the response norms may diverge. Thus a fixed conservative kappa does
not obstruct eventual exact-trial certification of a strictly positive short,
or detection of a strictly negative direction. Singular nonnegative shorts have
no guaranteed finite stopping certificate. No degree/rate is supplied.

The audit also constructs an injective diagonal residual model for which the
approximating operator converges in norm and its unique finite minimizers have
vanishing *approximate* residuals, while their true residuals diverge. An effective
implementation must control source error multiplied by the trial norm. Exact
continuum optimization, finite sampled fitting and a certified algorithm remain
distinct. The conditional rational-trial semidecision route in that review is
not represented as an implemented solver or a resource guarantee.

An additional actual-source theorem rules out every finite upper comparison
`D<=C K_Q`. Compactly supported, moment-corrected modulations make the Gamma
primitive energy arbitrarily large relative to L2 primitive norm. This refutes
a proposed bounded-comparison route, not the fractional-range hypothesis.
The exact proofs, domains, numerical diagnostics and open interpolation lemma
are in [FRACTIONAL_SOURCE_RANGE_AUDIT.md](FRACTIONAL_SOURCE_RANGE_AUDIT.md).

## Authentic first-window bracket, before and after

All bounds use the original a=1/2 source and low form metric
W=diag(1/3,1/5,1/7,1/9). Odd indices are1,3; even are2,4.
The displayed upper numbers are normalized operator caps, not raw form eigenvalues.

| Quantity | Inherited certified bound | This round |
|---|---:|---:|
| Odd S0 upper cap | <0.000452 | 300761/1073741824, about 0.000280106 |
| Even S0 upper cap | <0.001702 | 11742983/8589934592, about 0.001367064 |
| Odd R0 cap used in lower bound | 75625/20699, about 3.65356 | c_odd, about 0.454908, <455/1000 |
| Even R0 cap used in lower bound | 75625/20699, about 3.65356 | c_even, about 0.848147, <849/1000 |

The exact response caps are

    c_odd  = 405333569368851711757618861801 / 891024077979000000000000000000,
    c_even = 107959895025855318145227769087 / 127289153997000000000000000000.

With A^- the rigorous finite-Gamma lower matrix, the complete rational bracket is

    A^- - diag(c_odd/3,c_even/5,c_odd/7,c_even/9) <= S0 <= H+.

The [deterministic packet](arithmetic_resonance_receipts/resolvent-final-py313-packet.json)
contains all matrix entries, parity blocks, coordinate metrics and error budgets.
The upper uses a frozen degree 20 rational trial with whole Gamma completion.
The lower integrates exact derivative-column point enclosures over 512 cells,
uses a total-variation Lipschitz bound between points, and includes the entire
omitted derivative Gamma ladder in operator norm. An independent auditor checked
source pairings, the continuum cell argument, normalization and outward caps.

A final exact principal-minor check of those matrices gives the outward scalar
operator enclosures

    -249986756855/549755813888 I <= S0_odd <= 300761/1073741824 I,
    -932513462611/1099511627776 I <= S0_even <= 11742983/8589934592 I.

Thus coarser decimal enclosures are [-0.454724,0.000280106] and
[-0.848117,0.001367064]. These are intervals for normalized operator spectra,
not estimates of an observed eigenvalue. The
[normalization receipt](arithmetic_resonance_receipts/normalized-schur-bracket.json)
pins the input packet and supplies rational diagonal/determinant witnesses.
Replay requires, in each sector, the two diagonal entries and determinant of
`exactlower - lower_cap*W` to be nonnegative, and the same check for
`upper_cap*W - exactupper`. Forty steps of rational bisection produce the
recorded lower caps; floating eigenvalue computations are unnecessary.

Both lower matrices remain insufficient to settle the sign. Positive upper caps
are not positivity evidence. The degree 12/16 whole-family obstruction attempts
were inconclusive at their fixed budget and are preserved as such. Positive-shift
certificates at epsilon 1/100 and 1/1000 include spatial and Gamma errors, but lack
a quantitative zero-shift gap. See
[AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md](AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md).

## Beyond prime 2 and the source-access boundary

The explicit unitary rescaling to a common interval transports kernel, low
Legendre projections, metric and K. Finite Gamma approximants plus a uniform
kernel tail prove norm continuity as radius changes. Exact completed low matrices
at 1/2, 9/16, 11/16, 7/10 include prime 2, then prime 3, then prime-square 4 with weight
log2/sqrt4. No high-coercivity or zero-shift-continuity theorem is transferred to
the larger windows. Fake 6 is rejected even if outside the current support.

[CROSS_PRIME_WAVEFRONT_CONTINUATION.md](CROSS_PRIME_WAVEFRONT_CONTINUATION.md)
also implements the rational product formula and its finite-menu obstruction.
Finite prime support of each rational does not give a uniform finite observer
menu, an Archimedean spectral rate, or a limit Q_p->R.

## Formal authority, failures and validation

The paired finite Lean module and source application contract are separate from
all infinite/source proofs above. The final integration receipt records its exact
commit, named theorem types, axiom budgets, runtime outcomes and hosted CI status.
The fresh replay checked 31 theorems and 12 definitions in one module, using Lean
4.29.1 at trust zero. All 43 declarations report exactly `propext`,
`Classical.choice`, `Quot.sound`. The main declarations prove a finite rational
solved-system resolvent difference and antitonicity, diagonal range compatibility,
finite spectral sums, and cubic/quartic hinge primitive identities. The latter
prove formal coefficient differentiation, not a real integral theorem. Twelve
false Lean controls were rejected; 63 Rust tests, formatting, Clippy and T0 examples
passed under Rust 1.85.1. The inherited two Markdown-math failures remain failures.
The older 62+28 theorems were hash-checked, not freshly replayed. Both hosted YEAN
jobs at the published head were blocked by billing before executing any step.
See [formal integration](arithmetic_resonance_receipts/formal-integration.json)
and [exact-head CI evidence](arithmetic_resonance_receipts/yean-exact-head-ci.json).
The early SUCC snapshot in YEAN is retained with any later byte differences
explicitly listed; it is not an implemented source-to-Lean extraction bridge.
The SUCC [tail contract](SPECTRAL_TAIL_CERTIFICATE_CONTRACT.md) preserves source
identification, fractional-mass and regularization-gap debts transitively. Its
structural/hash verifier issues no semantic theorem authority.

The [hostile audit](../../reviews/2026-10-16_ARITHMETIC_RESONANCE_HOSTILE_AUDIT.md)
records 259 executable checks, independent paper routes and retained failures.
It found an actual API flaw: a caller-supplied, self-consistent upper packet could
launder a forged response bound. The optional input was removed; the source bound
is regenerated. A runtime integrity guard initially rejected a healthy generator
binding and was repaired. Both failures and regression tests remain visible.
Wrong source channels, clocks, half-densities, metrics, parity, hidden debt,
projection order, moment extrapolation and compact-inverse shortcuts have controls.

Validation is performed on frozen Python source bytes using
`scripts/check_arithmetic_resonance_round.py`, independently under Python 3.10 and
3.13, including full unittest discovery, focused suites, provenance, observer,
ordinal and five new probes. Detailed final results and head mapping are recorded
in the execution receipt; a receipt's starting commit is not misrepresented as a
later commit. Hosted CI must be inspected at the publication head.

Final local results: **4,631 full-suite tests and 141 focused replays passed on
each of Python 3.10.20 and 3.13.13**, with no skips. This adds108 tests to the
parent's4,523; the focused counts overlap the full suite. Both runs passed all
five new probes and the72-entry provenance, observer and ordinal gates. Their
Python source snapshots are identical and stable throughout both runs. Full-suite
wall times, exact commands, dependency versions, logs and hashes are in the
[execution summary](arithmetic_resonance_receipts/execution-summary.json).
The original imported SyntaxWarning is retained; no unrelated historical source
was rewritten to remove it. The final PR records the separately inspected hosted
CI results at its exact head, avoiding a self-referential receipt/commit cycle.
The first hosted certificate workflow failed because checkout omitted history:
the exact source-origin and branch-ancestry probes correctly rejected a shallow
clone. An isolated shallow clone reproduced both failures; fetching full history
made both probes pass without changing their gates or mathematical code. The
workflow now requests full history and uploads receipts even after failures.
The [reproduction](arithmetic_resonance_receipts/ci-history-reproduction/manifest.json)
and original failed hosted transcript are retained. This failure is not relabeled
as an earlier pass.

## Most consequential next lemma

Dense response is now a source theorem, conditional on the inherited coercivity;
quantitative response remains the bottleneck. Prove a computable rate for
approximating the four targets in the actual relative residual norm, or prove an
actual spectral-mass/fractional-domain estimate. A full-line symbol analogy,
finite positive moments, or a low-block numerical fit does not close that lemma.
The [successor handoff](ARITHMETIC_RESONANCE_NEXT_ROUND.md) separates the two routes
and the conditions for extending beyond the first-prime window.
