# Operation Zero Boundary: uniform slips, sharp countermodels, moving frequencies

Draft research child of PR403 at
`5f350af7808532e55d74e80c948c02bb385c6e70`. All changes are additive in this
directory. The original four signed BBP poles and U_0=0 remain untouched.

**Strongest selected extension.** One threshold now works simultaneously for
all frequencies and lags satisfying `ell<=A/26` and `|h|ell<=A³/6`:
some n in `[A,8A)` has lag energy at least `eta=1-cos(pi/10)`.
Consequently one constant C, independent of N and h, satisfies

    N-|sum_(n=1)^N e(hU_n(0))|
      >= eta/(4 log8) log⁺(N/|h|^(1/3)) - C.

This extends the parent's quantifiers, but does not improve its fixed-h
logarithmic order. The proof uses the published Zeilberger–Zudilin input.

**A sharp obstruction.** Explicit changed seeds under the identical forcing
have signed deficit Θ(log N), yet their selected constants have finite
irrationality exponent; a classical Shallit/Kempner example even has bounded
partial quotients and exponent2. Finite exponent plus the Green correction
cannot force superlogarithmic saving. Positive-density lag-one dispersion
alone also has an explicit finite-exponent nonnormal countermodel.

**An actual additional signed inequality, in a different regime.** For every
real seed and `512A²/15<=|h|<=A³`,

    |sum_(n=A)^(2A) e(hU_n(s))| <= A+1-A/578.

A separate explicit bound reaches `A²/2<=|h|<=A²`. These use the authentic
source variation. The coherent seed proves that a uniform fractional saving
cannot extend below the quadratic frequency scale; the corresponding
lag-energy threshold is cubic. These are not fixed-frequency normality results.

The arithmetic front extends the conductor law to growing filters and tests
the complete CRT weight, prime-power injections and coherent dyadic aliases.
The spectral front gives a finite repunit-frequency Gram certificate, the
correct all-frequency energy threshold, an effective native three-mark
variation bound, and exact noncentral endpoint-holonomy controls.

**Still open:** authentic positive-density fixed-h dispersion, SC-06,
base16 normality of π and RH. No new fixed-h o(N) bound or positive fraction
has been proved. A new source-selected signed interaction remains necessary.

Read [claim register](CLAIMS.md), [route ledger](PROOF_ROUTE_LEDGER.md),
[Diophantine proofs](diophantine/THEOREMS.md),
[moving-frequency proofs](MOVING_FREQUENCY.md),
[CRT/arithmetic dossier](crt/CRT_DOSSIER.md),
[spectral dossier](spectral/SPECTRAL_DOSSIER.md),
[remaining obligation](CURRENT_OBSTRUCTION.md),
[validation](VALIDATION.md), and [next handoff](NEXT_HANDOFF.md).

The small Lean file proves only the finite integer no-wrap core. Paper
proofs, exact finite certificates, separate implementations, same-model
reviews, classical inputs and hosted CI have distinct authority. Raw failed
attempts and corrected runs are retained. No scholarly priority is asserted.
