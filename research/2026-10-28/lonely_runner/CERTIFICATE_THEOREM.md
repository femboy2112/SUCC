# Exact source-labelled circle covers and a finite max-min theorem

Date: 2026-10-28. Base: `b763ba8ef375fbac221e29e4396989a635a6ef36`.
Status: elementary paper proofs with independent exact implementations and
adversarial finite tests. The formal mathematical cover semantics are in
`formal/LonelyRunnerCover.lean`; the kernel receipt, when available, determines
their actual kernel status. No new range-18-through-94 counterexample, optimum,
priority, or academic-novelty claim follows from this document.

## Source contract and target

There are **n moving runners**, with pairwise distinct positive integer speeds
`v_1,...,v_n` and specified shifts `s_i` in `[0,1)`. Define

\[
 d_i(t)=\|s_i+v_i t\|,\qquad
 g(t)=\min_{1\le i\le n}d_i(t),\qquad
 \gamma(v,s)=\max_{t\in\mathbb R/\mathbb Z}g(t).
\]

Here `||x||` is distance to the nearest integer. Integer speeds make every
`d_i` one-periodic; continuity gives an attained maximum. The ordinary lonely
runner conjecture has all shifts zero. Arbitrary specified shifts define the
stronger shifted question. A certificate with
`gamma <= delta < 1/(n+1)` refutes the shifted assertion for that configuration;
it says nothing against the ordinary conjecture. Every reported `n` counts
moving runners, so the threshold is `1/(n+1)`, not `1/n`.

## COV1 — finite cover soundness and completeness

**Quantifiers.** Fix the above configuration and `0 <= delta <= 1/2`. For each
runner `i` and integer winding `k`, define

\[
 I_{i,k}=\left[\frac{k-s_i-\delta}{v_i},
                   \frac{k-s_i+\delta}{v_i}\right]\cap[0,1].
\]

Discard empty intervals. The following are equivalent:

1. `gamma(v,s) <= delta`.
2. The intervals `I_{i,k}` cover `[0,1]`.
3. A finite sequence of these intervals has right frontiers
   `0 = r_0 < r_1 < ... < r_m = 1`, with the jth interval having endpoints
   `l_j,r_j` and `l_j <= r_(j-1)`.

**Proof.** For positive `v_i`, multiplication by `v_i` preserves order, so
`t in I_(i,k)` is equivalent, for `t in [0,1]`, to
`|s_i+v_i*t-k| <= delta`. Existence of such a winding is exactly
`d_i(t) <= delta`. Taking existence over runners gives (1) iff (2).
Only windings `s_i-delta <= k <= s_i+v_i+delta` can meet `[0,1]`, so the
family is finite. A sequence in (3) covers `[0,r_j]` inductively, proving
(3) implies (2), including closed endpoint equality.

For the converse, choose a covering interval meeting zero with maximum right
endpoint. It has positive right endpoint: otherwise finitely many intervals
meeting zero are singletons and all remaining intervals begin a positive
distance away, contradicting coverage. At any frontier `r<1`, some interval
has left endpoint at most `r` and right endpoint strictly greater than `r`.
Otherwise the finite intervals extending right of `r` all start a positive
distance after `r`, again leaving a gap. Choose one with maximal right
endpoint. Strictly advancing endpoints in a finite family force termination
at one. This proves (3). ∎

The certificate can therefore supply only a covering chain, rather than all
windings. A missing interval is harmless if the remaining chain still covers;
the checker must reject missing **coverage**, not arbitrary omitted data.
Zero-length clipped intervals are unnecessary. An equality of touching
endpoints is legitimate; strictness belongs to `delta < 1/(n+1)`.

**Formal scope.** `closed_chain_cover` proves closed-interval union coverage
by list induction. `source_interval_transport` proves the original real
shift/velocity/integer-winding inequality from endpoint bounds.
`closed_chain_runner_sound` quantifies over **every real** `t in [0,1]` and
returns an original runner index and integer winding. Integer time transport
extends a winding witness periodically. The proof is generic in the real
endpoint data; acceptance and decoding of an individual JSON file are outside
the Lean theorem. No formal completeness or formal breakpoint theorem is
asserted here.

## COV2 — complete finite breakpoint theorem

**Statement.** For the same configuration, define

\[
 T=\bigcup_{1\le i\le j\le n}
 \left\{\frac{k-s_i-s_j}{v_i+v_j}\pmod1:
                 k=0,\ldots,v_i+v_j-1\right\}.
\]

Then `gamma(v,s) = max_(t in T) g(t)`. The raw number of displayed
candidates, before deduplication, is

\[
 \sum_{i\le j}(v_i+v_j)=(n+1)\sum_i v_i.
\]

**Proof.** Take a maximizing circle point `t*`. If an active runner's distance
function has a corner there, its phase is an integer or half-integer. Thus
`2s_i+2v_i*t*` is an integer and `t*` belongs to the self-pair `i=j` set.
If no active runner has a corner, all active distance functions are affine
on a sufficiently small common neighborhood, with slopes `+v_i` or `-v_i`.
The finitely many inactive functions are strictly greater at `t*`, so remain
inactive on a smaller neighborhood. If every active slope were positive,
moving right slightly would increase their minimum; if every active slope
were negative, moving left slightly would increase it. Both contradict
maximality. Hence there is an active positive branch `i` and an active
negative branch `j`. Write their local fractional phases as `a,b` in `(0,1)`.
Their equal distances imply `a=1-b`, so
`s_i+s_j+(v_i+v_j)*t*` is an integer. This puts `t*` in the claimed pair set.
All such roots on the circle are listed by one complete residue system of
`v_i+v_j` consecutive integers. The count follows because each `v_i` occurs
once with each of the other `n-1` speeds and twice in its self-pair. ∎

The implemented solver also evaluates zero, which is harmless. It uses exact
modular rational arithmetic and an explicit raw-candidate budget. Exceeding
that budget means optimization was not performed; it is not a disproof or an
upper bound. The theorem gives a complete rational optimum for rational shifts,
with a rational maximizing-time witness. It does not optimize over shifts or
over velocity vectors.

## Independent checker and schema

`observational_succ/lonely_runner_verify.py` imports only Python standard
library modules and never imports the search/generator. All mathematical
rationals are canonical pairs `[numerator, denominator]`, with positive
denominator and gcd one. Mathematical integers cannot be booleans. Floats are
forbidden throughout the entire JSON payload, including metadata.

Schema `SUCC-shifted-cover-v1` requires exactly these top-level fields:

| Field | Required meaning |
|---|---|
| `schema` | Literal schema identifier |
| `n` | Length of the moving-runner velocity vector |
| `velocities` | Distinct positive integers |
| `shifts` | Canonical rational pairs in `[0,1)` |
| `delta` | Canonical rational radius in `[0,1/2]` |
| `threshold` | Exactly `[1,n+1]` |
| `velocity_gcd` | Recomputed gcd of all velocities; need not be one |
| `source` | Nonempty provenance object; text accuracy is externally audited |
| `intervals` | Objects with exactly `runner,winding,left,right` |
| `ordering` | Permutation of every supplied interval index |
| `inequalities` | Objects with exactly `left_cross,right_cross` |
| `payload_sha256` | Canonical payload binding described below |

Runner indices are zero based. Winding integers are not reduced modulo a speed.
The checker recomputes both clipped endpoints from the declared runner, shift,
velocity, radius and winding. It starts at frontier `p/q=0/1`. For the next
left endpoint `a/b`, the supplied inequality must give the exact integers
`left_cross=a*q` and `right_cross=p*b`; these must satisfy
`left_cross <= right_cross`. The next right endpoint must strictly advance the
frontier. The final frontier must be exactly one.

The digest is SHA256 of UTF-8 encoding of Python's
`json.dumps(payload, sort_keys=True, separators=(",", ":"),
ensure_ascii=True, allow_nan=False)`, where `payload` excludes only
`payload_sha256`. This binds all source and mathematical data but is not an
authentication of literature or a proof of mathematical correctness by itself.
No modular inverse or gcd-based time substitution enters cover verification.

`verify_cover(certificate)` requires the strict counterexample threshold.
`verify_cover(certificate, require_counterexample=False)` checks coverage and
explicitly labels whether the threshold is strict. The CLI is
`python scripts/verify_lonely_runner.py FILE.json`; `--coverage-only` enables
the latter mode, and `--exact-gamma` invokes the separate complete breakpoint
calculation. Standard input is accepted as `-`.

## Published baselines and literature boundary

[Blanco, Criado and Santos, arXiv:2603.24784v4](https://arxiv.org/html/2603.24784v4)
(24 October 2026), Proposition 5.11/Figure 1, supplies

\[
 v=(1,2,3,4,5),\quad s=(0,46,38,47,72)/94,\quad\gamma=15/94<1/6.
\]

The independent complete solver reproduces this exact value; its witness
`t=39/94` has active runners with zero-based indices 3 and 4. The independent
source-labelled cover also proves the matching upper bound. This is a
published result, not a new counterexample. The paper establishes shifted
counterexamples for moving-runner counts 5 through 17.

[Poliakova, arXiv:2609.23952v1](https://arxiv.org/html/2609.23952v1)
(20 September 2026) establishes them for every `n >= 95` and explicitly states
the remaining range `18 <= n <= 94`. Its local rule is handled in a separate
dossier. [Beck and Everett, arXiv:2609.06259v2](https://arxiv.org/html/2609.06259v2)
(23 September 2026) gives integer-relation reductions applicable to shifted
configurations; informal prose about failure for `k >= 5` is not a proof
closing Poliakova's explicitly stated intermediate range. The literature
search did not locate a primary-source closure of that range; this statement
is not an exhaustive priority claim.

The BCS author repository
[criado/shifted_lonely_runner_conjecture_counterexample](https://github.com/criado/shifted_lonely_runner_conjecture_counterexample)
was inspected at commit `fd0dbc5f2c7450ae8d7b784e855019507d5a8efd`, dated
24 April 2026. Its GPL-3.0 algorithms were not copied. The published
`output/consecutive.out` contains counts 2 through 13, not 17. Its SHA256 is
`d835e86ad1b559d415a801e6a06872f3a41c14464ad859414452770281dfa675`.
The arXiv v4 TeX source and that repository did not supply a retrieved explicit
17-runner seed. This is a precise data access gap, not a mathematical
impossibility or permission to fabricate missing shifts.

## Crucible, receipts, and next falsification

`tests/test_lonely_runner_verify.py` supplies 15 tests. Fifty deterministic
small random configurations compare the pair-breakpoint solver with an
independently implemented affine-cell arrangement algorithm using `Fraction`:
all half-integer phase knots partition the circle; every affine pair
intersection in each cell is evaluated. This changes both the implementation
and the finite-set derivation, though both remain same-session exact software.
Time translation, integral velocity scaling and runner permutation preserve
the computed optimum in metamorphic tests.

Hostile certificates modify windings, source endpoints, gcd, runner counts,
the off-by-one threshold, hash, ordering, exact cross-products, fraction
normalization, duplicate speeds and mathematical booleans. Unknown inverse
fields are rejected. An incomplete chain is rejected. Each semantic mutant
is rehashed to ensure that its rejection tests mathematics rather than merely
hash binding.

The float disagreement control has one speed `v=1`, shift zero, and radius
`delta=(2^59-1)/2^60`. Its true intervals `[0,delta]` and `[1-delta,1]`
leave a positive open gap, although both adjacent endpoints round to the
same binary float `0.5`. Integer cross multiplication rejects the purported
cover. This directly refutes treating floating endpoint contact as proof.

**Ledger verdicts.** COV1 and COV2 survive as elementary proved-local claims;
the known BCS configuration survives exact finite replay. The assertion that
the verifier or a finite search proves new shifted counterexamples in
18 through 94 is unsupported. Next falsification opportunities: independent
review of the maximum-point active-slope argument; exact replays with large
denominators; corrupted winding data which preserves approximate geometry;
and production certificates whose original source labels must survive an
independent all-time cover check. Kernel claims must cite the actual exported
theorem receipt, not this paper proof or the Python tests.
