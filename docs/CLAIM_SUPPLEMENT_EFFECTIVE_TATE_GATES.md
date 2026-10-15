# Classical effective-field and Tate-source claim ledger (2026-10-15)

Child of draft classical PR #115 at `91d494b2d7f1821cae625ddbeb5cd4daa0fa90bf`; parent of that is main `03db44203147a7b28d445bb9f970fa71360e78c4`. Exact scope, primary-source dependencies, proofs, controls: `research/2026-10-15/TATE_SCHWARTZ_EFFECTIVE_FIELD_TRICHOTOMY.md`.

| ID | Claim | Status | Proof/hostile control |
|---|---|---|---|
| EF1 | For a known total finite deterministic source, checking the reachable orbit decides whether every future report is zero | CLASSICAL / PROVED PAPER, TESTED FINITE | Cycle proof, unreachable bad state, reachable mutation |
| EF2 | The explicit universal two-counter diagonal binary tree is decidable, prefix closed, has nodes at every depth and has no computable infinite path | CLASSICAL / PROVED PAPER using imported 2-counter universality; TESTED FINITE | Diagonal contradiction; finite depth tests and forced forbidden-bit mutation; no executed infinite path |
| EF3 | All finite prefixes of an ideal all-ones report admit eventually-zero source realizations, but the full report has no realization in that original source class | PROVED PAPER, TESTED FINITE | Each prefix uses different source; source-image closedness fails |
| EF4 | Even-coordinate probes do not determine the odd-coordinate target, and one lawful odd-coordinate probe can repair that particular ambiguity | PROVED PAPER, TESTED FINITE | Explicit observationally identical original-source pair |
| EF5 | Every finite no-pulse prefix has a later-pulse countermodel; absence of all future pulses is not proven by finite source scanning | CLASSICAL / PROVED PAPER | Adversarial arbitrary-delay pulse |
| EF6 | Deciding whether a bounded-halting probe family ever distinguishes two sources uniformly would decide halting | CLASSICAL / PROVED PAPER, TESTED FINITE | Delayed-halt plus bounded loop controls |
| EF7 | Simple/IdealHard/Fucked classify entire unqualified real/physical source world or RH as impossible/unprovable | UNVERIFIED / NOT CLAIMED | All field classes are target, source, toolkit and probe relative |
| TF1 | Every certified `V_(a,b)` is an exact finite presentation of a genuine locally constant compact-support function on Qp; Fourier maps it to `V_(b,a)` | CLASSICAL / PROVED PAPER | Exact root orthogonality and selected Haar measure |
| TF2 | Fourier² is reflection, Parseval/Plancherel hold, and support-expansion/precision-refinement squares commute under dual exchange | CLASSICAL / PROVED PAPER, TESTED FINITE | Independent rationals, Hadamard/Gauss and two-axis hostile tests |
| TF3 | The full-coset unramified Mellin/Tate equation holds meromorphically with correct `f(0)` and `f̂(0)` ports and fixed χ(p)=±1 | CLASSICAL / PROVED PAPER, TESTED FINITE | Exact shell sums, 108 varying test cases, wrong Haar rejection; negative s dual only analytic continuation |
| TF4 | Coarsening a conductor-9 source to conductor-3 data preserves all Fourier phase distinctions | REFUTED | Residue 1 vs 4, lost 9th-root phase |
| TF5 | Standard diagonal rational additive characters satisfy real × finite product =1 | CLASSICAL / PROVED PAPER, TESTED FINITE | Exact rational modular inverse phases |
| TF6 | Gaussian real local Mellin equals π^(−s/2)Γ(s/2), with exact two-step recurrence | CLASSICAL / PROVED PAPER, TESTED FINITE | Symbolic rational π powers, direct Γ relation |
| TF7 | Finite true-prime Euler product approximates ζ uniformly for Re(s)≥σ>1 with tail ≤P^(1−σ)/(σ−1); composite 6 independent factor mutates a(6) | CLASSICAL / PROVED PAPER, TESTED FINITE | Absolute Dirichlet sum, fake factor rejection |
| TF8 | Finite Tate windows prove full adelic Poisson, completed signed Weil positivity or RH | UNVERIFIED / NOT CLAIMED | Restricted-product global convergence, original-source distribution, signed all-test positivity missing |

**Provenance correction:** this child branch previously contained an Archimedean source module importing missing `classical_tate_window.py` and a nonreproducible preliminary receipt. The missing module and source-run scripts are now added; the previous preliminary receipt is superseded and not counted as prior successful verification. **No historical original archived code or main mutated.**
