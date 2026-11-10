# The reconstruction error is paid; the signed carry mean remains open

This round constructs an explicit, source-authenticated integer-clock observer
and proves a quantitative transport of the remaining normality gate. It also
executes the previously proposed frozen carry-model experiment on a later
source clock and rejects its L1-approximation premise for entire model classes.
**No original-zero signed decay or pi-normality proof is claimed.**

Starting research head: `19d98078b60e47092c9b9d050a70b6b7eabb7cd2`.
Fetched main: `43a607818907120d4cdab73d240f5b4d7700b63f`.
Original proof baseline: `d32342d375f44ddf62221ad6aff2f534abdc0a03`.
Everything in this round is under this directory. The four signed poles,
literal U0=0, original integer carries and unwrapped states are unchanged.
The [latest sibling-branch audit](LATEST_REPO_REVIEW.md) is read-only and
includes two precise proof qualifications communicated on PR554.

## Strongest new proof step: a bounded carry statistic with a paid error

Write C_n=floor(U_n) and kappa_n=C_n-16C_(n-1). The exact state

\[
S_n=C_n\bmod16^k,\qquad
S_{n+1}=(16S_n+\kappa_{n+1})\bmod16^k
\]

uses 4k bits. A literal carry16 propagates normally; it is not discarded by
reducing each carry separately. This state defines the **ancestral** phase
reading g_k(S)=e(h(S+1/2)/16^k). It reconstructs the phase k steps earlier,
up to an explicit quantization and four-pole forcing error. It is a different
task from predicting the present phase with past carries.

The uniform-append reference operator P has P^k g_k=0 when 16^k does not divide
h. Its finite Poisson potential is psi_k=sum_(j<k)P^j g_k. Define the actual
transition innovation D as the epoch mean of
`psi_k(S_(n+1))-(P psi_k)(S_n)`. The reference operator is an algebraic tool,
not an asserted random law of the actual carries. [CCV7](theory/THEOREMS.md)
proves, on every original-zero epoch [A,2A),

\[
|W_A(h;0)-D_{k,A}(h)|\le
{4k\over A}+\pi|h|16^{-k}+{\pi|h|\over32(A-k)^2},\qquad A>k.
\]

For fixed h and k=ceil(log_16 A), this is O_h(log A/A). The reconstruction
residual and boundary costs are now proved to vanish for this concrete
source-derived model. **The retained signed innovation has not been bounded.**

[EI1--6](crucible/EXPLICIT_INNOVATION.md) further constructs an explicit
continuous observer

\[
\Phi_h:\mathbb Z_{16}\times\{0,\ldots,16\}\longrightarrow\mathbb C,
\quad \|\Phi_h\|_\infty\le {17\pi|h|\over15},
\]

whose truncation after R terms has uniform error at most
`(17*pi*|h|/15)*16^-R`. Consequently

\[
W_A(h;0)-{1\over A}\sum_{n=A}^{2A-1}
\Phi_h(C_n,\kappa_{n+1})=O_h(\log A/A).
\]

The common carrier is the exact integer lift C_n, in its real and 16-adic
roles. This is not an identification of real and 2-adic rational U_n states.
The observation arrives at time n+1, after the transition it measures.
Uniform tail bounds justify the inverse limit without exchanging uncontrolled
limits. Exact identities Phi_(16h)=Phi_h and Phi_(-h)=conjugate(Phi_h) remove
redundant frequency bookkeeping.

This is a concrete, bounded arithmetic target with explicit memory/error
costs. Its selected-source mean decay is **equivalent to Weyl decay**, not a
strictly weaker theorem. No proof debt is claimed paid by renaming that mean.

## The preregistered experiment actually fails

[Protocol](PROTOCOL.md) was pushed at `8c43eaf1`; code and tables were frozen
and pushed at `5e1e3fad` before opening the later source clock. Training used
the union of old intervals1103--2204 and2189--4376, deduplicating their16
overlapping times. The held-out clean interval is55003--110004, with
p=220009, m=27501 and q=2, entirely beyond the earlier endpoint44000.

The shared tables use only kappa_n or (kappa_(n-1),kappa_n), never a future
carry or later phase value. All predictions are exact frozen Gaussian dyadics.
The source replay retains all110004 carries, unwrapped/carry hashes, every
principal-part check and separate modular endpoint checks.

| h | Trained one-carry rho, rounded down | Trained two-carry rho, rounded down | Lower bound for **every** one-carry table | Lower bound for **every** two-carry table |
|---:|---:|---:|---:|---:|
|1|0.637743|0.664902|0.619878|0.571309|
|3|0.638673|0.668024|0.616537|0.573692|

The last two columns are the stronger, subsequently derived [CCM4](model/THEOREMS.md)
dual certificates, valid even for tables chosen after seeing this holdout.
The class is one shared unit-disk-valued table applied to both replicas, with
the specified carry feature; arbitrary extra time/replica labels are not allowed.
These are approximation-cost lower bounds, not lower bounds on W. The actual
clean-clock Weyl moduli are below0.003372 and0.007613 respectively.

The original rho+resonance+signed-orbit cost is fully charged in the
[model receipt](model/HOLDOUT_SUMMARY.json). Canonical compression of the
prediction reads its carry-occupancy mean, not the held-out W; it still cannot
beat the direct predictor certificate. The zero predictor also fails the
registered L1 threshold. Increasing fit freedom inside these two classes does
not repair the failure.

## Signed residuals succeed finitely, but learning did not improve the baseline

The [signed extension](SIGNED_PROTOCOL.md), also pushed before holdout access,
uses all padded windows and all cross terms. At H=512, its certified clean-clock
Weyl upper bounds, rounded upward, are:

| h | Zero model | Frozen one-carry model | Frozen two-carry model |
|---:|---:|---:|---:|
|1|0.042654|0.072833|0.063378|
|3|0.044011|0.072701|0.081385|

Every registered aperture H=32,128,512 passes the finite1/4 threshold, but
both trained models are worse than zero at every tested h/aperture. The
coherent inverse control stays at one. These measurements do not prove an
all-epoch rate. See [complete signed results](SIGNED_HOLDOUT.json).

The later **exploratory**, unfitted ancestor-reading model k=3 gives direct
signed-residual certificates below0.004286 and0.009980 on this same clock.
This is not a second fresh holdout: the retained carry means are already close
to W by the proved retrodiction identity. The small finite certificate verifies
the instrument; it supplies no independent decay theorem. All endpoints and
analytic errors are in [the exploratory receipt](RETRO_EXPLORATORY.json).

## Why the approximation target needed repair

[FR1--3](FOLDED_FINITE_RANGE.md) proves an explicit finite inequality for a
two-replica law and an M-point output alphabet. Conditional on both normality
and infinitely many selected q2 clocks, it gives the uniform floor

\[
\liminf\inf_{|D|\le M}\operatorname{mean}\operatorname{dist}(aB,D)
\ge {1\over8192M^2}>0.
\]

Thus a fixed finite output alphabet can be incompatible with demanding a
vanishing folded L1 error even under the desired normality conclusion.
Both hypotheses remain conditional. Raw current-phase prediction has a
separate risk-one obstruction under normality (CCV5); a same-forcing unknown-
seed ensemble has its own HCP3 floor. Those results must not be conflated.

The strongest hostile control survives the new compact observer exactly:
for s*=-pi/16, late C_n=-1 and kappa_(n+1)=15, and **Phi_h(-1,15)=1**.
Uniform reference-branch mean zero, continuity, memory convergence and exact
forcing transport therefore do not imply selected-path cancellation.
The [failed stationarity attempt](theory/ATTEMPT_AND_VERDICT.md) retains
explicit periodic cycles and rational finite-horizon controls as receipts.

## The one proof frontier

| Arrow | Establishing result | Status and surviving hostile control |
|---|---|---|
| Original four poles and U0=0 -> unwrapped U, integer C and literal carries | Exact recurrence, source stream and modular checks | PROVED; source/seed mutants fail authentication |
| Authenticated carry history -> finite ancestor observer | CCV1-L/Q and CCV7 | PROVED, explicit error and4k-bit state; current-phase prediction is a different target |
| Finite observer -> bounded Phi_h with uniform memory tail | EI1--4 | PROVED PAPER; coherent fixed point has Phi=1 |
| Original-zero history -> mean Phi_h tends0 for every fixed h!=0 and every large integer epoch | No source-specific signed bound supplied | **OPEN**; reference averaging is not a proof |
| That bound -> full Weyl decay | EI4, with O_h(log A/A) comparison | PROVED implication; the same comparison makes it an equivalence |
| Weyl decay -> base16 normality | Inherited original Green tail, all-epoch-to-prefix and Weyl theorem | PROVED implication; finite frequencies/subsequences are insufficient |

The prime-covariance route remains equivalent: its local marginal tends to
zero on the authenticated clocks, leaving the same unpaid real signed mean.
The balanced three-channel sibling supplies additional local observations,
not a bound for this mean. No arrow has been promoted by a numerical test.

## Evidence and next decisive task

See [validation](VALIDATION.md), [provenance](PROVENANCE.json),
[claims/failures](CLAIM_LEDGER.md), [connections](CONNECTIONS.md) and the
[artifact manifest](ARTIFACT_MANIFEST.json). Exact tests, interval certificates,
paper proofs, Lean checks and hosted CI have separate scopes. Three agent
fronts and root share a model family; this is not external refereeing.

The next theorem that changes the verdict is an original-zero upper bound
on the average of the explicit Phi_h, with its finite-memory tail charged.
A more focused exploratory probe can combine its labelled carry-transition
terms with the balanced prime-birth stages. Such a probe must keep signed
cross terms and defeat the p-invisible near-coherent controls; a full-rank
local Gram or a zero reference conditional mean is insufficient.

**Pi base16 normality: OPEN. RH: OPEN.**
