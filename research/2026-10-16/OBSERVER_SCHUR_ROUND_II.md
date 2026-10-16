# The Observer's Schur Complement — Round II

**Original Suzuki four-low sign OPEN. RH PROVED: NO.** This round connects
observation factorization to the actual signed Schur envelope, proves a genuine
source-specific obstruction to an entire trial family, and supplies fresh formal
proofs and exact-instance applications. The scope is the first-prime radius
`a=1/2`; there is no all-radius result or replacement of the signed source.

## Lineage and preservation

SUCC child branch: `research/observers-schur-complement-2026-10-16`, based on
`5d6d717312eebee648d3cfb092875eb4120bb4b3` (draft PR134). YEAN child:
`research/succ-observer-schur-kernel-2026-10-16`, based on
`bf49477d9758e17070e9603526ead3e3e11122a1` (draft PR135), now at
`4bda4fc92f722464d17a3911ccc12f7f28193e6b`, [draft PR136](https://github.com/femboy2112/YEAN/pull/136).
Initial live heads, worktrees, clean states and parent checks are in the
[initial audit](observer_schur_receipts/initial-live-audit.json). All changes are
in isolated child worktrees. Main, original research worktrees and archives were
not merged, reset, overwritten or released. Six workers owned disjoint files;
only the principal integrated Git. Completed workers were closed.

The arithmetic source remains Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, from commit
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`, SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.
The PR85 source lineage and the founding 72-entry import lineage remain distinct.
Real Gamma, both pole channels, true prime-2 half-density and contact are retained.

## Proved mathematics and exact implementations

The [observer theorem dossier](OBSERVER_SCHUR_THEOREMS.md), with stable IDs
OS-01–08, proves the following with full domains and countermodels:

- For a Hermitian form and linear observation, quadratic energy factors exactly
  iff the observation kernel lies in the radical. Isotropy on the kernel alone
  fails because of hidden cross terms.
- For bounded signed blocks with D≥0 and D nonzero, low-only nonnegative-sign
  factorization is equivalent to positivity of the whole form. If D=0 instead,
  it is equivalent to zero cross coupling; low A can be negative.
- A fiber envelope is finite precisely when its cross column belongs to the
  actual range of sqrt(D). Its reduced square gives A−C*C; it is attained iff
  that column belongs to ran(D). Closure range and injectivity alone do not suffice.
- With A≥αI, α>0, the short is positive iff C A^(-1/2) is a contraction.
  Source-compatible reflection splits the four-low problem into two 2×2 sectors.
- Actual residual range and D≥κK give the two-sided trial bracket. A negative
  upper value constructs an original-source negative direction; a negative
  sufficient lower value cannot do so.
- Algebraic coimage factorization and bounded completion factorization are
  distinct. The latter requires a uniform domination bound in the observation norm.

The general shorting and range mathematics is classical; see
[Douglas's factorization theorem](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)
and [Anderson–Trapp](https://epubs.siam.org/doi/10.1137/0128007).
The signed low block is handled by the explicit variational proof, not by assuming
that the whole original G is positive. The new integration is the source-typed
observer interface. Academic originality is not asserted.

A direct corollary clarifies minimum access to a **known** finite low envelope.
If m(x)=x*S0x on an n-dimensional low carrier and L is a linear observation,
then m factors through L iff ker(L)⊆ker(S0), by OS-01. Therefore the minimum
dimension of a linear observation image is rank(S0): rank-nullity gives the
lower bound, and the quotient by ker(S0) attains it. This is a paper corollary,
not an additional kernel declaration or a computed rank of the actual S0.
If the whole G is PSD, its nonnegative-sign report needs no observation at all:
the report is the constant true value. Four moments are thus not automatically
minimal for every target, even though they index the current Schur envelope.

The [compactness dossier](COMPACT_SOURCE_GALERKIN.md), CG-01–09, proves compact
compression convergence and specializes it to source-defined Legendre projections:

    ||G − P_N G P_N|| < 11 / [40(N+1)].

The stronger bound uses the exact signed derivative enclosure divided by
sqrt((N+1)(N+2)); a Hilbert–Schmidt estimate and whole-Gamma derivative-Gram
remainder are also supplied. Exact high Galerkin response energies converge
monotonically to R0, hence their shorts converge from above to S0, under the
actual square-root range hypothesis. This gives no unproved residual convergence
rate and no bounded inverse of compact D.

High polynomials are dense in the graph norm of the bounded source residual
map R_Q:u↦Π_M(Gu)'. The target can be approximated in that residual norm iff
its columns annihilate ker(R_Q*). This is a separate source obligation. Two
countermodels prove that neither ordinary energy convergence nor compactness
plus relative coercivity discharges it.

The strongest general obstruction is the clamped-biharmonic model: true
S0=1/12>0, while **every** admissible L2 trial has sufficient lower value
at most −4/5 at the declared valid κ=1. This is an independently audited
synthetic model, explicitly not the Suzuki source or a claim for all κ.

## Actual arithmetic progress and current bound

The [source dossier](OBSERVER_SCHUR_SOURCE.md) and
[final source receipt](source-schur-final.json) preserve the exact fractions.
For low input P2, every response U(P2) in complex span(P6,P8) fails the
K-relative sufficient certificate, with uniform exact upper consequences:

| Comparison κ | Uniform upper on the sufficient lower value |
|---|---:|
| 20699/1000000, inherited valid bound | less than −1/1000 |
| 1/10, hypothetical | less than −18/100000 |
| 1/5, hypothetical | less than −3/100000 |

Monotonicity excludes every 0<κ≤1/5 for this response family. The proof uses
all coefficients, full source intervals, the whole omitted Gamma tail, and a
negative-definite rational matrix majorant. An independent auditor reconstructed
source pairings through a separate polynomial representation and confirmed it.
This strengthens the previous eight fixed failures; it is neither a negative
original-source direction nor an obstruction to all polynomial degrees.

A genuine high Rayleigh test bounds all admissible κ strictly below
0.818124. It does not prove κ≤1/5, so improving κ alone is not completely ruled out.
A newly frozen rational response gives an authentic continuum upper form H+:

    A − (75625/20699) I ≤ S0 ≤ H+.

The lower bound is inherited and remains coarse. H+ and exact generalized
parity caps are in the source receipt; its positive upper bounds do not settle
S0's sign. No improved rigorous derivative-Gram lower certificate closed.
The rigorous operator upper caps are 1939731/4294967296 in the odd sector
and 3654297/2147483648 in the even sector (approximately 0.000451629 and
0.001701665). These bound the entire sector operators above, not below.

A different 17-column threshold-aware spline family was fitted, frozen as rational
coefficients and evaluated on a separate quadrature grid. Relative optimization
improved its own numerical lower estimates but did not close the sign or beat
the prior polynomial experiment globally. These are TESTED_MODEL results only.
All finite Gamma, spatial integration and relative residual errors remain separate.

## Formal proofs and semantic authority

YEAN PR136 kernel-checked **28 new rational theorems**, freshly compiled 22 local
modules, replayed the inherited 62 theorems and passed 63 Rust tests. Exact types,
source/artifact hashes and axiom budgets are in its formal report and manifest.
Lean is 4.29.1; audits use trust zero. The new theorem budget is exactly
`propext`, `Quot.sound`, `Classical.choice`; no custom axiom or admitted proof.
Eight false Lean applications were rejected with normal diagnostics.

The [application contract](FORMAL_SOURCE_APPLICATION_CONTRACT.md) and
[final bridge replay](observer_schur_receipts/bridge-kernel-final/replay.json)
add seven actually checked generated declarations: the fixed affine word
S1,V2,S3,V3 normalizes to 6x+15 with prime admission and all-input semantics;
the complete 4-to-2 quotient pullback/average/projector tables match their actual
Lean definitions, with retraction for every rational input function. Two wrong
coefficient/normalization mutants were rejected. Five local imports were freshly
compiled for this replay, not counted as five additional distinct project modules.

This verifies the serialized mathematical instances. It is not verified extraction,
a universal proof of Python semantics, or external source authentication. Those
obligations remain in every packet. The separate ten-capsule bundle retains open
range debt transitively and leaves S0 as UNVERIFIED / OPEN_TARGET. Its structural
checker grants no semantic theorem authority.

Hosted YEAN CI at the exact new commit executed **zero steps**, blocked by account
billing: [fresh receipt](observer_schur_receipts/yean-hosted-ci.json). Local proof
receipts are not hosted CI. Repository text validation passed; the inherited
Markdown-math gate still fails two unchanged prior notes. Raw diagnostic receipt
whitespace is intentionally preserved.

## Small executable discovery and minimum observations

The [typed experiment](OBSERVER_DISCOVERY_EXPERIMENT.md) composes only compatible
finite rational sources and nested observations. It verifies range-solved Schur
identities, searches a declared finite alphabet for witnesses to five false
conjectures, and retains missing assumptions rather than inventing proof status.
No general theorem-discovery engine or mathematical novelty is claimed.

The minimum-observation compiler now handles a complete finite joint-probe menu:
exhausting its powerset proves minimum cardinality, while ablation pairs establish
irredundancy. The two bits of a residue modulo4 jointly recover canonical chi4;
either bit alone fails. The inherited conductor, polynomial descent and paired
prime-power mutation theorems are preserved rather than re-proved. Synthetic
coefficient mutations remain distinct from alternative legitimate zeta sources.

## Audits, validation and next handoff

The [hostile audit](../../reviews/2026-10-16_OBSERVER_SCHUR_HOSTILE_AUDIT.md)
records independently reconstructed rational source integrals, singular/range and
norm countermodels, forged-packet controls, and the corrected complex conjugation
error. Initial failed Lean generation, coarse interval failure, numerical calibration
failure, and a detected concurrent-file drift are retained. A failed gate remains
failed even when a later corrected replay passes.

The principal also preserved an executable regeneration of the source-cap audit,
using the prior auditor's Rodrigues definitions and no producer source/matrix
helpers. It recomputed all required source pair intervals and passed 25 checks:
[script](replay/source_cap_audit.py), [receipt](observer_schur_receipts/source-cap-regeneration.json).
Run `python -B research/2026-10-16/replay/source_cap_audit.py` from the root.
This makes fresh interval computation reproducible in addition to checking the
stored audit endpoints; it is not another independent arithmetic source.

Final validation receipts and publication pointers are recorded below.
The [claim supplement](../../docs/CLAIM_SUPPLEMENT_OBSERVER_SCHUR.md) and updated
[dependency graph](../../docs/SUCC_RESEARCH_DEPENDENCY_DAG.md) distinguish paper
proof, kernel proof, exact enclosure, tested model and unresolved source obligation.

The next consequential missing lemma is quantitative control of the **actual**
source target columns in the quotient-derivative response range. Determine their
pairing with ker(R_Q*), or construct a source-matched trial with a rigorous full
continuum residual Gram. Propagate the whole-Gamma derivative tail and spatial
errors through the matrix Loewner bound. Compact operator convergence, accurate
low moments and finite positive upper shorts cannot replace this lemma.

Additional formal debt is the general finite block range-solved Schur identity,
then bounded analytic operators and their domains. The infinite Hilbert carrier
reconstruction remains a classical paper proof with finite exact interfaces;
no arbitrary global point has become finitely programmable. The original
all-radius Weil sign and RH remain unresolved.

## Coherent code checkpoints

| SUCC commit | Review scope |
|---|---|
| `5ebf0c033a2d04650b7c7bca28693f30ce3470ea` | Typed nested envelopes and joint observation minima |
| `a50d939f7ad7b21b88b2b75085d1b39b9eb93365` | Observer energy/sign/envelope proofs and exact finite implementation |
| `de0d41dd8a7d9b6a887120a1d191084a055f0edb` | Source compactness rate and relative response counterexamples |
| `6da4854f7458b0135a27254cb1dc8c49e43f1e29` | Seven generated Lean instance proofs and authority boundary |
| `cdc80c4a584e6ca96ddcc817a89a7c8547af68f6` | Conditional capsule debt and reproduction driver |
| `990e5493a3698f1124eb52e09d5febf80a5e6c5f` | Source-family obstruction, frozen response upper bound and experiments |

The validation receipts identify their starting Git head and hash every module,
test and probe before and after execution. Subsequent documentation/receipt
commits preserve those exact tested code bytes. Final hosted results must be
read at the draft PR's exact head, separately from historical parent checks.

## Final local validation

[Machine-readable summary](observer_schur_receipts/final-validation-summary.json):
all 16 commands passed on each interpreter, with unchanged before/after code
hashes and no full-suite skips.

| Interpreter | Full suite | Focused suite | Full-suite elapsed |
|---|---:|---:|---:|
| Python3.10.20 | 4,523 passed | 103 passed | 657.401s |
| Python3.13.13 | 4,523 passed | 103 passed | 426.057s |

The command receipts include source provenance, observer foundations, ordinal
report, observer Schur, compact Galerkin, typed discovery, inherited capsules
and new conditional capsules. Provenance verified all 72 imported entries:
17 byte-identical archives and 55 documented mechanical namespace migrations.
This byte gate does not certify their mathematical truth. The independent
hostile audit passed 4,109 checks on each interpreter, with a separate 25-check
source-cap addendum and 16 formal-receipt integrity checks.

Reproduce from the checkout root (choose either supported interpreter):

```sh
python3 scripts/check_observer_schur_round.py --python python3 --output /tmp/observer-schur-replay
python3 -B research/2026-10-16/replay/source_cap_audit.py
python3 scripts/formal_instance_bridge_probe.py --output /tmp/observer-schur-formal --yean /path/to/pinned/YEAN --formal-manifest /path/to/fresh/YEAN/manifest.json
```

First generate the fresh formal manifest in the pinned YEAN child using
`python3 tools/check_observer_schur.py --dependencies /path/to/pinned/packages --rust`.
The formal bridge performs actual kernel replay only with both formal arguments;
omitting them generates models with `kernel_verification_performed=false`.

The [preservation audit](observer_schur_receipts/preservation-audit.json) records
clean original/parent worktrees. YEAN's original development branch advanced
concurrently and was preserved. This round used isolated branches throughout.
The final SUCC exact-head hosted receipt belongs to the draft PR after push;
no historical parent CI is counted as this round's hosted validation.
