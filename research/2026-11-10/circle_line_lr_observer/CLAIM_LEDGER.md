# Circle/line observer claim ledger

All universal statements below are written mathematical arguments in ordinary
classical real analysis, not new proof-assistant theorems. Finite execution
evidence is kept separate. Hypotheses, conventions and countercontrols are
part of each claim's scope.

| ID | Claim, domain and hypotheses | Status | Support and next falsification opportunity |
|---|---|---|---|
| CLO-01 | The Euclidean unit circle, secant family through (-1,0), and metric pull back arclength to `2 dt/(1+t²)`; circumference/diameter equals `4 integral_0^1 dt/(1+t²)`. | PROVED PAPER / Disclosed | `CIRCLE_GEOMETRY.md` G1; exact polynomial identities. Erasing density or diameter normalization changes the result. |
| CLO-02 | For every integer k>=0, the beta matrix source `A_k([3,4])` strictly encloses geometric pi; its width is W_k, and W_k<2^(-k) for k>=1. | PROVED PAPER / Disclosed | `LR_TRANSLATION.md` §3; uniform series, beta integral, explicit shifted-tail comparison. Stage0->1 lower endpoints coincide; no false strict-nesting claim. |
| CLO-03 | For every m>=1, the 3–4–5 rational rotations yield strict alternating-series enclosures with the stated exact width. | PROVED PAPER / Disclosed | `CIRCLE_GEOMETRY.md` G2. Branch/orientation fixed by rational substitution and a quarter-turn certificate. |
| CLO-04 | For either source, every requested finite L/R prefix terminates and all output intervals contain pi with width <=1/(N+1) after N arrows. | PROVED PAPER / Disclosed | Source contraction, imported classical irrationality, right endpoint updates, determinant invariant. Remove irrationality or the strict enclosure contract and the comparison may not terminate at a rational target. |
| CLO-05 | Every requested finite radix prefix is computable from either source by certified scaled floors. | PROVED PAPER / Disclosed | Same contraction and irrationality; `IMPLEMENTATION_CONFORMANCE.md`. Units-digit field and whole floor are distinguished for bases2/3. |
| CLO-06 | Rational projective line and circle-conic action groupoids are isomorphic via the explicit conic map and Sym² arrow lift, identifying scalar matrix representatives. | PROVED PAPER / Disclosed | `LR_TRANSLATION.md` §5. Includes infinity; not an equivalence of ordinary affine-line and Euclidean-circle isometry groups. |
| CLO-07 | Euclidean arclength distortion is the rational cocycle J_M; on rational projective points it is a functor to the one-object positive-rational multiplicative group. | PROVED PAPER / Disclosed | Explicit derivative, scalar invariance, chain rule, and continuous extension at infinity in `README.md` §5. This functor is not faithful; rotations and identities can share weight1. |
| CLO-08 | Source consumption and output changes commute in residual coordinates with the explicit L/R swap. | PROVED PAPER / Disclosed | `LR_TRANSLATION.md` equation4; `B_E=E·swap`, `bar G=swap·G·swap`, associativity. Omit the swap and the asserted map is wrong. |
| CLO-09 | For A>=1,s>=0,h nonzero, midpoint precision k=8A+s approximates the `16^(n-1)` Fourier epoch with error <abs(h)/(60 A 2^s); the original zero-seed U_n has the additional stated tail payment. | PROVED PAPER / Disclosed | `PRECISION_TRANSFER.md`, independent coefficient audit. h=0 has exactly zero error. A `16^n` clock changes the constant by16; arbitrary seeds change the target. |
| CLO-10 | Final production code passed the saved exact probe and two independently implemented reviews at its pinned SHA256. | OBSERVED / finite scope | `observer_receipt.json`, `HOSTILE_OBSERVER.md` §10, `IMPLEMENTATION_CONFORMANCE.md`. Tests support implementation conformance; they do not prove every infinite execution or statistical claim. |
| CLO-11 | An autonomous deterministic machine with finitely many complete states can emit pi's exact L/R path forever. | REFUTED | Eventual output periodicity yields a rational/quadratic value; classical transcendence excludes pi. Growing integer state is explicitly permitted in the actual program. |
| CLO-12 | Equal L/R branch weights represent equal Euclidean arc lengths. | REFUTED | First mediant1/2 gives point(3/5,4/5), off the quarter-circle angular bisector. `J_L(0)=1/2`, `J_R(1)=2/5` are exact metric controls. |
| CLO-13 | Geometric pi radians can replace pi turns in the expanding Fourier observer. | REFUTED | `exp(i16^(n-1)pi)` equals -1 at n1 and1 for every n>=2. `HOSTILE_OBSERVER.md`; exact phase mutation in probe. |
| CLO-14 | The beta source matrices are L/R words up to rational scalar. | REFUTED | det(Z_1)=3, while rational scalar multiples of L/R words have square determinant. Source/output are joined by a compiler, not identified. |
| CLO-15 | A computable transcendental input and a productive L/R program force base16 normality or hexadecimal parity balance. | REFUTED | `3+sum_(k>=1)16^(-k!)` is computable/transcendental with zero digit frequency1. `HOSTILE_OBSERVER.md` proves the asymptotic control; 1000-digit counts are only its finite illustration. |
| CLO-16 | The new source, conic equivalence, cocycle or precision theorem proves the selected two-fiber contrast tends to0. | OPEN / UNVERIFIED | No all-large-epochs signed bound has been obtained. Retain original forcing, literal zero seed, prime-power complement, winding, tail and conditional marginal hypotheses. The next discriminator must reject the coherent wrong-seed controls. |

## Proof dependencies and independence

The two geometric programs share the same Euclidean integral and classical
irrationality theorem. BBP supplies a separately implemented regression
formula, not a runtime input. The constructor, translator and adversary used
different decompositions and checks but are same-model agents; their agreement
is not three blind mathematical witnesses. The root independently replayed
finite certificates and checked the algebraic constants. Primary sources
identify classical imports and source conventions in `README.md`.

For the requested recovery problem, the missing comparison pathway is now
resolved. Source-map adequacy was improved by retaining the metric,
normalization, matrix handedness and radix observer units, and tested with
explicit mutations. These statements do not assign truth probabilities or
transfer that resolution to the separate signed cancellation problem.

## Dominance boundary

The geometry-derived observer recovers the previous BBP-based path and digit
checks while adding a source that does not consume BBP at runtime, explicit
circle/line arrow transport, and a proved precision schedule. It survives
the stated normalization and mutation controls. Its claim to dominance is
limited to this richer computational specification and verification. No
dominance over the open statistical frontier is asserted.
