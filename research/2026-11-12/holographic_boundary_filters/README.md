# Holographic boundary filters: reconstruct, certify, and increase resolution

**Research round, 2026-11-12.** Based on Main XXV
`db9fb4b84672050efa79b13377f1e73364598a14`; donor work is pinned separately
in [SOURCE_MAP.md](SOURCE_MAP.md). This is an additive research dossier,
with paper proofs, exact arithmetic implementations, hostile controls and
separate derivation audits. No worldwide novelty or formal-proof authority
is claimed. **Goldbach, R0, pi normality and RH remain OPEN.**

## What the boundary approach actually earned

The strongest result of this round is a **stable, monotone reconstruction
of the zero-grade mass from damped boundary responses**, on an unbounded
integer spectrum. It gives a concrete answer to “choose the right filters”:
cancel low unwanted grades, retain the desired grade with unit gain, and
bound every remaining grade with a known sign. Its response coefficients
have total absolute value less than nine at every order.

Two complementary results make the wider proposal precise. An ordered
Gram-response certificate determines whether a reconstructed finite space
is closed under every permitted filter. A target-specific duality theorem
decides whether the observations determine the property of interest at all,
and measures the worst ambiguity when they do not.

The last stage turns the instrument against its own arithmetic application:
[FIXED_RESOLUTION.md](FIXED_RESOLUTION.md) derives a source-specific
obstruction to keeping the damped filter order fixed as the midpoint grows.
It also recovers positive aggregate response when the order grows at a
sufficient rate of order `sqrt(log log X)`. This distinguishes a useful
reconstruction instrument and its averaged calibration from an adequate
all-target arithmetic estimate.

## 1. A usable version of the holographic intuition

An object is observed through a declared family of interventions and
responses. Its “boundary” is that interface. The interior is reconstructible
up to the equivalence relation left by the interface; a particular property
is provable from the responses when it is constant on the corresponding
observation fibers. This is an exact identifiability statement, not a claim
of an efficient decision procedure for every property.

The important move is to work backward from a desired distinction. Which
two candidate interiors currently look the same? Which joint or ordered
response separates them? Does the new distinction survive measurement
error? This realizes the user's probe-based intuition without assuming
that any finite collection of shadows is automatically complete.

The present-output meeting rule is retained: responses are compared in one
declared frame and normalization. Past states enter only with an explicit
transport. In the operator model, phase, adjoints and chronological order
are part of that declaration. The scalar grade filters commute; their gain
comes from signed cancellation, rather than physical order.

## 2. Stable grade filters and the two monotone bounds

Let `c_h>=0` for integer `h>=0`, with total mass `M<infinity`, and suppose
the boundary supplies `F(s)=sum_h c_h s^h`. For even `d>=2`, `0<t<=1/2`, set

\[
Q_{d,t}(z)=\frac{z\prod_{j=1}^{d-1}(z-t^j)}
 {\prod_{j=1}^{d-1}(1-t^j)}=\sum_{r=1}^d a_rz^r,
\qquad B_{d,t}=\sum_{r=1}^d a_rF(t^r).
\]

The pointwise filter has value one at grade zero, zero at grades
`1,...,d-1`, and lies in `[-epsilon_d,0]` at every higher integer grade,
where `epsilon_d=t^[d(d+1)/2]`. Consequently

\[
\boxed{c_0-\epsilon_d(M-c_0)\le B_{d,t}\le c_0,
\qquad \sum_{r=1}^d|a_r|<527/63<9.}
\]

The odd versions give upper bounds, with a full monotone refinement law:

\[
B_{2,t}\le B_{4,t}\le\cdots\uparrow c_0,
\qquad B_{1,t}\ge B_{3,t}\ge\cdots\downarrow c_0.
\]

Thus two current observers can meet with a lower and an upper bound for
the same target, and tighten their bracket as filter order grows. This
statement is about information refinement, not entanglement or physical
time. If each supplied response has absolute error at most `eta`, the
signed center has error less than `9 eta`. An explicit feasible interval
and an integer-count recovery rule pay that uncertainty.

For exact responses and integral `c_0`, `epsilon_d M<1` gives
`c_0=ceil(B_d)`. The response-channel count can be of order
`sqrt(log M)`. Acquisition cost, rational bit lengths and normalization
precision are separate: this is not a runtime or information-compression
claim. With normalized responses `F/M`, detecting one count still requires
absolute accuracy of order `1/M`.

**Proof and domain:** [DAMPED_FILTERS.md](DAMPED_FILTERS.md).
The coefficients are classical geometric Lagrange extrapolation / finite
q-product coefficients. The result here is the explicit signed envelope,
conditioning, refinement and source-scoped application. Continuous grades,
signed masses and an unproved response oracle are outside its guarantees.

### Finite Goldbach application

At midpoint `n`, grade an offset `0<=a<=n-2` by
`Omega(n+a)+Omega(n-a)-2`. Zero grade counts unordered prime pairs summing
to `2n`. The boundary responses retain the shared midpoint:

\[
F_n(s)=\sum_{a=0}^{n-2}s^{\Omega(n+a)+\Omega(n-a)-2}.
\]

Every frozen combination of `n=10,257,509,1021,2053,4099` and
`d=2,4,6`, at `t=1/2`, was evaluated exactly. These responses were acquired
by finite factorization, not by an unproved analytic shortcut.

| Midpoint | Degree-two response | Degree-four response | Degree-six response | Actual count |
|---:|---:|---:|---:|---:|
| 10 | 1.515625 | 1.998047 | 2.000000 | 2 |
| 257 | 1.352051 | 13.907479 | 13.999980 | 14 |
| 509 | -5.231679 | 19.817233 | 19.999948 | 20 |
| 1021 | -19.361301 | 29.620452 | 29.999886 | 30 |
| 2053 | -45.905215 | 52.236436 | 52.999753 | 53 |
| 4099 | -109.071371 | 82.449051 | 83.999483 | 84 |

The table displays the unclipped lower response, rounded only for display
to six decimal places; integer recovery uses exact rationals. Four lower responses fail
by being negative, fourteen are positive, and eleven determine the exact
count. Every degree-six certificate determines its count. At `n=4099`,
the theorem predicts this because `4098/2^21<1`, before looking at the count.
[Exact responses and certificates](DAMPED_RESULTS.json) and
[independent SPF/Lagrange replay](DAMPED_AUDIT.md) are preserved.

The preceding quadratic moment filter was substantially weaker:
only nine midpoints through 257 had positive bounds. Its failure led to
the damped construction. Its proof, fixed-moment counterfeit families and
source-cap mutation remain in [GOLDBACH_FILTERS.md](GOLDBACH_FILTERS.md)
and [GOLDBACH_AUDIT.md](GOLDBACH_AUDIT.md).

## 3. A finite certificate for all ordered responses

For independent observed word states forming `V`, let
`G=V*V`, `H_i=V*A_iV`, and `Q_i=V*A_i*A_iV`, with `G>0`. Define

\[
R_i=Q_i-H_i^*G^{-1}H_i,
\qquad M_i=G^{-1}H_i.
\]

The identity `R_i=[(I-P)A_iV]*[(I-P)A_iV]`, where `P` projects onto
`range(V)`, proves that every `R_i` is positive semidefinite and vanishes
exactly when that filter leaves the observed space invariant. If every
residual vanishes, the matrices `M_i` reconstruct every ordered word and
cross-response in the cyclic sector accessible from the boundary state.
No unobserved direct summand can be reconstructed by this interface.

For approximate closure, the normalized residual
`G^(-1/2) R_i G^(-1/2)` controls leakage. Under a separately established
global contraction premise, word error is at most the sum of the per-step
leakages times the boundary-state norm. Small raw residuals alone fail
when the Gram matrix is poorly conditioned. These exact-input results do
not include an unproved measurement-perturbation bound.

The Pauli control `(X,Y)` versus `(X,-Y)` has the same individual spectra,
all single-filter moments and every word-return intensity. Nevertheless
the signed return of `XY` is `i` versus `-i`. Coherent cross-responses,
with a declared phase reference, reveal the difference. This is a precise
instance where the order and twist of probes matter.
[Full proof and controls](ORDERED_REALIZATION.md).

## 4. Certify the target without reconstructing the whole object

On a finite probability carrier, let the rows of `F` be the available
filters, including the constant-one row, and let `v` be the target.
Then `v` is universally determined by the observations iff `v` lies in
`rowspan(F)`. Moreover,

\[
\sup_{p,q\ \mathrm{probabilities},\ Fp=Fq}|v\cdot(p-q)|
=2\,\operatorname{dist}_{\infty}(v,\operatorname{rowspan}F).
\]

This measures exactly how much target ambiguity the current filters leave.
For any proposed dual coefficients `lambda`, the error payment is
`||v-F^T lambda||_infinity + sum_i |lambda_i| epsilon_i`.
The implementation returns a reconstruction or an explicit indistinguishable
pair; it does not purport to solve every minimax optimization problem.

The phase tests expose concrete inadequacies of tempting filter families:

- Equal power spectra can hide different additive representation counts.
- Equal power spectra **and all third correlations** can still hide
  nontranslation differences when Fourier support leaves unconstrained phases.
- Full rational rank of the support relations can hide finite torsion:
  the `Z/21` example has presented group `Z/63`, leaving a `Z/3` ambiguity.
- Even with full support, near the uniform law a signal difference of order
  `epsilon` can produce only a triple-response difference of order
  `epsilon^3`. This rules out uniform inverse Hölder exponents above `1/3`
  in that regime; it does not establish a general inverse at exponent `1/3`.

Power decay to zero would still suffice for the corresponding Weyl target.
Phase loss is target-relative, not a universal objection to power methods.
[Proofs and exact controls](PHASE_AND_TARGET.md),
[separate audit](PHASE_AUDIT.md).

## 5. The original BBP source also gets an exact boundary instrument

The four-pole forcing and literal `U_0=0` are retained. For the authentic
shell Fourier response `W_B(1)`, cell filters give a rigorous lower bound
for `1-Re W_B(1)`, paying the future tail explicitly. Fixed-point interval
rounding is propagated through every multiplication by 16.

Six shells and three resolutions per shell produced eighteen exact
certificates, with no unresolved cells. At resolution 64, the four new
session-fixed shells `137,271,547,1091` give lower bounds approximately
`0.666926,0.671860,0.658958,0.607061`. A separate rational four-pole recurrence
reproduced every vector. These are finite shell inequalities; their positivity
does not prove the all-late-shell R0 condition.
[Proof](PI_FILTERS.md), [full census](PI_RESULTS.json),
[independent replay and precision mutants](PI_AUDIT.md).

## 6. What remains decisive

For Goldbach, the missing result is a source-derived estimate of the
**coupled** boundary responses, with resolution allowed to grow and with
enough signed margin for every sufficiently large midpoint. For pi, it is
a uniform positive R0 margin across every sufficiently late shell. An
equivalent restatement, a product of separately averaged marginals, or
exact finite counting does not discharge those quantifiers.

This round earns general filter theorems, an arithmetic limitation of fixed
resolution, and finite authenticated applications. It does not promote
the conjectures. [NEXT.md](NEXT.md) specifies the next discriminating cuts
and exit products; [CLAIM_LEDGER.md](CLAIM_LEDGER.md) records the scopes.

## Reproduce and review

From the repository root:

```sh
python research/2026-11-12/holographic_boundary_filters/run_checks.py
python -m unittest discover -s tests -p 'test_holographic_boundary_filters.py'
```

The first command runs the focused tests, verifies both frozen arithmetic
receipts, reconstructs the finite control reports and checks the saved
verification receipt. Use `--write` only to deliberately regenerate that
receipt after reviewing a change. The ordinary repository test discovery
includes the same focused tests through the second command's loader.
The full required baseline and the final checks are recorded in
[VALIDATION.md](VALIDATION.md). All scripts use the Python standard library.

Read in order: this overview, the damped-filter theorem, the fixed-resolution
obstruction, then whichever of the operator/phase/BBP applications is relevant.
The audits are methodologically distinct same-model checks, not independent
external referees or a proof-assistant kernel.
