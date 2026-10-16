# Observer–Schur Round II claim supplement

Parent SUCC `5d6d717312eebee648d3cfb092875eb4120bb4b3`; parent YEAN
`bf49477d9758e17070e9603526ead3e3e11122a1`. Statements below retain their
domains and assumptions. Classical results, new-to-project integrations,
formalizations and exact model checks are distinguished. Academic novelty is
not established. **Original four-low sign OPEN; RH PROVED: NO.**

| ID | Statement, domain and premises | Authority and evidence |
|---|---|---|
| OS-01 | Hermitian quadratic energy on a real/complex vector space factors through linear O iff ker O lies in the radical | PAPER_PROVED; [observer theorem](../research/2026-10-16/OBSERVER_SCHUR_THEOREMS.md); rational formal counterpart in YEAN |
| OS-02 | For bounded self-adjoint blocks with D≥0: D≠0 gives low-only sign factorization iff G≥0; D=0 gives it iff cross B=0 | PAPER_PROVED; same dossier; D=0 with negative A is a necessary edge case |
| OS-03 | Fiber envelope is finite iff B*x belongs to the actual range of sqrt(D); reduced square gives x*(A−R0)x | PAPER_PROVED, classical Douglas/variational argument; closure range alone is insufficient |
| OS-04 | A finite envelope is attained iff B*x belongs to ran(D) | PAPER_PROVED; explicit compact nonattainment and divergent-response sequences |
| OS-05 | A≥αI, α>0, plus range gives S0≥0 iff norm(D^-1/2 B* A^-1/2)≤1; compatible source reflection splits sectors | PAPER_PROVED; uniform A positivity retained; no inverse of compact D on arbitrary vectors |
| OS-06 | Under D≥κK and actual residual square-root range: A−L_U−C_U/κ≤S0≤A−L_U | PAPER_PROVED; negative upper gives a source direction, negative lower does not |
| OS-07 | Linear coimage factorization iff kernel inclusion; bounded completion decoder iff one uniform domination bound | PAPER_PROVED; inherited diagonal decoder counterexample retained |
| OS-08 | Genuine four-low source admits a finite envelope and two parity contraction problems under the five explicitly listed source premises | PAPER_PROVED conditional application; sign remains OPEN |
| CG-COMPACT | Compact T and strongly convergent orthogonal P_N imply norm(T−P_NTP_N)→0 | PAPER_PROVED, classical; [compact dossier](../research/2026-10-16/COMPACT_SOURCE_GALERKIN.md); T=I refutes bounded-only extension |
| CG-SOURCE | Source-defined Legendre projections approximate genuine G with norm error below 11/[40(N+1)] | PAPER_PROVED with replayed signed derivative enclosure; mean-zero first-prime interval only; exact compression required |
| CG-ZERO-SHIFT | Norm convergence of compact signed block operators need not preserve zero-shift responses | REFUTED shortcut; explicit changing-cross source, fixed compact D=K |
| CG-GALERKIN-RESIDUAL | Ordinary coordinate Galerkin response energy convergence need not imply K-relative residual convergence | PAPER_PROVED counterexample; fixed compact 2×2-block direct sum with D≥K and compact relative map |
| CG-RANGE-GAP | A compact relative response map and relative coercivity do not guarantee target membership in its range closure | PAPER_PROVED clamped-biharmonic model; synthetic, not identified with Suzuki |
| CG-ALL-TRIAL | In the clamped model with A=1/6 and valid κ=1, true S0=1/12 but every L2 trial has sufficient lower value ≤−4/5 | PAPER_PROVED, independently audited; this does not identify a Suzuki obstruction or exclude every stronger κ |
| CG-POLYNOMIAL | High Legendre polynomials are graph-norm dense for the bounded source residual map | PAPER_PROVED; target range closure and convergence of a particular solver remain separate obligations |
| OD-01–03 | Range-compatible finite Schur envelopes associate; extended-real fiber infima associate under genuine coarsening | PAPER_PROVED classical identities; [discovery dossier](../research/2026-10-16/OBSERVER_DISCOVERY_EXPERIMENT.md); pointwise preservation under coarsening is refuted |
| OD-04 | Exhausting a complete finite probe menu's powerset certifies minimum cardinality; indispensable pairs certify irredundancy | PAPER_PROVED + EXACT_FINITE_CHECK; chi4 two-bit menu example; no adaptive optimality claim |
| OD-FALSE | Five predeclared false observer/envelope implications have exact bounded-search witnesses | REFUTED; first witness only in the declared finite ordering, no global witness-minimality claim |
| OSS-ANSATZ | Every parity-preserving P2 response in span(P6,P8) fails the sufficient K-relative criterion at the certified κ and the tested hypothetical constants through 1/5 | PAPER_PROVED with rational whole-source interval majorant; [source dossier](../research/2026-10-16/OBSERVER_SCHUR_SOURCE.md); not a negative direction of G or S0 |
| OSS-SPLINE | Threshold-aware projected step responses provide a different source-matched numerical trial family | TESTED_MODEL only; frozen coefficients and held-out quadrature do not certify continuum residual error |
| OSS-UPPER | A frozen rational response supplies a whole-source upper Schur matrix and two generalized parity eigenvalue caps | EXACT_SOURCE_INTERVAL plus variational paper theorem; positive upper caps do not certify positivity |
| FI-TRANSLATION | Fixed affine/retract packets replay their exact parameter and complete finite-table mapping, preserving all source obligations | EXACT_FINITE_CHECK; [application contract](../research/2026-10-16/FORMAL_SOURCE_APPLICATION_CONTRACT.md); generation alone is not kernel verification |
| FI-KERNEL | Seven generated declarations for one natural word and the complete 4-to-2 quotient instance pass fresh kernel replay, with two false applications rejected | LEAN_KERNEL_PROVED for those exact statements; [receipt](../research/2026-10-16/observer_schur_receipts/bridge-kernel-final/replay.json); universal Python correctness and source identification remain obligations |
| YK-OBSERVER | 28 rational observer/Schur theorems, including radical/coimage, scalar envelope, PSD, contraction and sign distinctions | LEAN_KERNEL_PROVED in [YEAN PR136](https://github.com/femboy2112/YEAN/pull/136); exact types and three-axiom budgets recorded; no infinite analytic theorem |
| OS-SCHUR-OPEN | Authentic unmodified S0≥0 at a=1/2 | UNVERIFIED / OPEN_TARGET; no positivity promotion from any finite or conditional entry above |

The final formal declaration list, axiom budgets, exact source bounds, corrected
audit findings, execution receipts and current GitHub pointers are indexed by the
[round report](../research/2026-10-16/OBSERVER_SCHUR_ROUND_II.md). The ledger does
not substitute its labels for those proof and replay artifacts.
