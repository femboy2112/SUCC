# Coupled Wilson construction: hole contract and probe protocol

Date: 2026-11-13. Parent: PR #613 at
`a8da424c84869d737462fdec0a64d7921a92eb50`, itself unmerged into main.
PR #614 at `0faa85a798de5b0b9af4d62295f405165b408eb7` is a read-only
comparison source, not an integrated dependency.

## Object and missing bridge

The finite object is a declared graph with SU(2) link variables, ordered
plaquette words, product normalized Haar measure and Wilson weight
`exp(sum beta_p Re(holonomy_p))`. Constant action terms cancel only in
normalized expectations. Preserve the shared links, word order, gauge action,
source weight and (when declared) reflection and positive-half algebra.

Parent #613 already supplies a one-plaquette rational construction, graph/matrix
semantics, weighted Haar transport and conditional reflection transfer. Its
explicit next hole is a multi-plaquette construction retaining shared edges.
The new goal is a terminating rational bounded-observable certificate at each
fixed finite lattice, with a reflection-compatible approximation theorem.
No uniform lattice-size, ultraviolet, infrared or mass-gap bound is assumed.

## Competing routes and predetermined verdicts

1. **Global polynomial amplitude.** An even Taylor polynomial of half the
   total action is positive, and its square gives a positive gauge-invariant
   state with a factorial error. Hypothesis that this automatically preserves
   reflection positivity is already **REFUTED in exploration**: on two
   reflected SU(2) scalar holonomies, degree-four orthogonal tests produce a
   negative reflected Gram determinant. Preserve that witness; do not count
   its rediscovery as a held-out validation.
2. **Factorwise truncation.** Even Taylor polynomials of individual Wilson
   plaquette weights have nonnegative SU(2) character coefficients for beta
   nonnegative. Prediction: under an explicit reflection split, their product
   is reflection positive and converges with a proved normalized error.
   Failure of a character coefficient or exact reflected Gram test under the
   hypotheses refutes the implementation/proof. A graph lacking that split
   gives no RP verdict; ordinary positive covariance is insufficient.
3. **Gauge-relative trace observer.** Singles and pairs reconstruct the vector
   Gram data of holonomies but can lose orientation. Ordered triples recover
   signed volume and hence simultaneous conjugacy. The Q8 triples enumeration
   (512 inputs) and the `(i,j,k)/(i,j,-k)` twin are exploratory calibration,
   not fresh validation. The all-SU(2) conclusion requires its paper proof.

## Fresh checks declared before their implementation

- Exact product-S3 moments: compare coordinate moments with the existing
  one-plaquette Catalan recurrence at degrees 0 through 20 and 24, 30, 38.
  Odd coordinates must vanish; the polynomial sphere relation must integrate
  to zero also after multiplication by selected monomials.
- Shared-link control on a two-loop bouquet: for x=Re(a), y=Re(b),
  z=Re(ab), product Haar gives E[xyz]=1/16, whereas independent loop
  surrogates give zero. Treat bouquet loops as a finite calibration source,
  not a four-dimensional lattice by assertion.
- Ordered multiplication: rational unit quaternions must distinguish an
  actual commutator from a commutative collapse; inverses must cancel exactly.
- Factorwise character expansion: exact coefficient reconstruction at even
  degrees 0,2,4,6,10 and rational beta 0,1/3,1,5/2. Coefficients must be
  nonnegative. Negative-beta/odd-degree controls are outside the theorem and
  must not receive its certificate.
- Reflected positive kernel matrices at rational SU(2) inputs, including
  repeated/singular inputs; verify exact PSD or reflected-square decomposition.
  Moving top-degree witnesses must continue to reject the global-polynomial
  route at further degrees, without refuting its fixed-test convergence.
- Trace-bank fresh controls: stereographic rational quaternions from integer
  triples (1,2,3), (2,-1,1), (0,3,-2), and conjugators from (1,1,2),
  (-2,1,0). Compare all retained traces and several ordered longer words;
  include rank-zero, rank-one and rank-two tuples. Exact conjugation must
  preserve the bank; an orientation reversal in rank three must change an
  ordered triple. Conditioning claims require a separate analytic proof.
- Formal reproduction: run upstream integrity checks at the pinned release;
  compile the dependency-light transport module with the pinned Lean version;
  accept a valid transported proposition and reject a changed value. This
  tests a transport instrument, not the Yang–Mills endpoint. Preserve failures.

Finite passes validate implementations and falsify shortcuts. They do not
establish universal positivity, gauge completeness or continuum existence;
those assertions inherit their explicitly stated proofs and hypotheses.
Same-family agent derivations are cross-checks, not independent reasoners.

## Acceptance and next falsification

Deliver exact code, complete finite proofs, source pins, hostile receipts and
claim ledger on a dedicated draft branch. Run focused tests and repository
required checks on the actual final commit. Report any pre-existing failure
and any full proof replay not performed. Never replace a continuum source by
an independent product of plaquette marginals.

The next harder probe is a growing reflection-compatible lattice family with
fixed physical observables: account for coupling, volume and observable-norm
growth in the error and reflection budgets. Failure of uniformity would leave
the finite theorem intact while preventing its use as a continuum shortcut.
