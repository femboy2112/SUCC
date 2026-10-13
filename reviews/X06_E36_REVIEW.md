# X06 non-deriver review by E36

**Verdict: ACCEPT T1–T3 under their stated mathematical contracts; require the
state-count scope amendment below before treating the result as physical memory
or executable storage evidence.** Status: PROVED LOCAL by independent paper
derivations; TESTED MODEL for this review's finite controls. No kernel
certification, empirical resource calibration, or novelty claim.

Reviewed author commit: a80d3d6d5e8850d857a1861e6c22b9c5c6551a54.
Only its X06.md dossier was read, via git show; no author probe, receipt,
implementation or antecedent expedition conclusion was read or imported.
Dossier Git blob: d90b3ae69a592dde410fdd88fbbb6c9453fa1652.
Dossier SHA256: e5ebd2b8c34dd26276de45f301b7dfe0d46faf51f14c455d978d40160a2c4271.
This reviewer did not derive X06. The principal supplied leads to the author;
this review supplies a separate proof check and independently written controls,
not a claim of blind discovery or unrelated mathematical provenance.
Own execution parent: 06b6ba43d6d9480cf939097bee6985d2c9328ea3.

## Reconstructed contract and T1

Let actions be stationary deterministic total maps, let reports and every
immediate cost depend only on the complete state, and let the cost labels lie
in a monoid M with left cancellation. Charges concatenate in execution order;
commutativity is unnecessary. The behavioral interface B_s(w) observes endpoint
report and the zero-origin cumulative charge for every finite word, including
the empty word. It excludes final compensation, hidden clocks and replenishment.

Independent derivation: define the raw edge/report signature of a state as
its report together with all immediate action charges. Equality of B implies
equal current reports by the empty word and equal edge charges by one-letter
words. For each action a, equal B at aw supplies equal successor reports and

\[
c_a(s)+C_{U_as}(w)=c_a(s)+C_{U_at}(w).
\]

Left cancellation makes successor behaviors equal. Thus ker B is a congruence
for the action algebra preserving the raw signature. Any equivalence preserving
that signature and actions preserves every endpoint and charge by induction,
so it lies inside ker B. Quotient actions, reports and charges are well defined.
This verifies the greatest-equivalence assertion.

For pointed minimality, consider any two histories u,v reaching one state in
another stationary weighted realizer. Each source prefix total matches its
realizer prefix total. Comparing u with uw and cancelling that particular
prefix identifies the source continuation charge with the reached realizer's
continuation charge. Do the same separately for v; the two source residuals
then coincide. Endpoint reports also coincide for every continuation. Therefore
the reachable realizer states map onto the reachable source residuals. The
canonical quotient attains the bound. Reachability, the same cost monoid and
prefix fidelity are essential parts of this claim.

### Universal necessity and its exact limit

For any failure r+x=r+y with x distinct from y, use four constant-report states
s,t,u,v. Action a has successors u,v,v,v and costs r,r,x,y. A second zero-charge
action b swaps s,t and takes both u,v to s. All four states are reachable.
Before the first a, only zero-charge swaps occur. That first a charges r.
The next action either joins both paths at s without an extra charge, or
charges x versus y and joins both at v. Equality r+x=r+y and the shared
subsequent suffix establish B_s=B_t for every word, although B_u(a) differs
from B_v(a). No idempotence, commutativity or cancellation of the suffix is used.
The b transition changes control state; it does not erase accumulated charges.

The independently implemented max monoid and saturated addition
x⊕y=min(2,x+y) both instantiate r=2,x=0,y=1. Saturated addition is
nonidempotent since 1⊕1=2. Each example has three zero-origin behavioral
residuals and four raw-charge stable classes, yet a one-state pointed realizer
with a-charge 2 and b-charge 0 reproduces every saturated cumulative prefix.
Thus universal cancellation is necessary for T1's displayed interface.
It is not necessary for every individual noncancellative machine.
Recording the whole immediate-charge sequence repairs the raw-fidelity
quotient without cancellation. Merely recording an already saturated total
does not recover those charges. Semantic budget saturation and raw-charge
fidelity are different observation contracts.

## T2: unary sharpness independently derived

Under left cancellation, B_i=B_j iff the report and departing-cost tails from
i,j coincide: endpoint reports are already included, and equal adjacent
prefix totals uniquely identify the next charge after a common prefix.

Let the separate least preperiods be μ_q,μ_c and primitive eventual periods
p_q,p_c. A joint tail beginning before max(μ_q,μ_c) would make a component
eventually periodic before its least preperiod. Both components repeat from
that maximum with P=lcm(p_q,p_c). Any joint period is an eventual period of
each component, hence is divisible by each primitive period; P is minimal.
An equality of suffixes at i<j would make the joint stream periodic from i.
This excludes collisions in the initial μ=max(μ_q,μ_c) positions. In the tail,
a collision between distinct phases would contradict primitive period P.
Therefore exactly μ+P residuals occur, proving the stated count.

The independent lasso controls use distinctive finite-prefix symbols and
primitive binary cycles, without reading B16: 900 cases recover the count.
Dropping cancellation fails sharply for constant reports and repeating raw
costs (2,0,2,1) in the max monoid: the primitive raw tail has period 4, but
zero-origin cumulative behavior has three classes and is not action stable.
The formulas require least preperiods and primitive periods; arbitrary lasso
presentations can overcount.

## T3: full-word lifting, not fixed endpoints

For every fixed source s and residual target r, the two following sets of
prices are equal, not merely bounded:

\[
\{\lambda(C_s(w)):V_w(\pi s)=r\}
=\{\lambda(C_s(w)):\pi(U_ws)=r\}.
\]

This follows from the quotient action intertwiner for the entire word.
Every residual word lifts from each specified representative s, with the same
sequence of charges; no representative can be changed halfway through.
Taking infima, including inf(empty)=∞, yields

\[
d_R(\pi s,r)=\inf_{\pi t=r}d_H(s,t).
\]

An additive nonnegative valuation makes history composition add prices.
Concatenation and approximation of infima prove the directed triangle inequality;
zero-price identities give d(s,s)=0. No minimizing word need exist. This is
a possibly nonseparated asymmetric Lawvere space. A fixed physical endpoint
t gives only contraction, since the residual endpoint permits the full fibre.
Valuation need not be injective. The additive zero valuation collapses a
two-state alternating-charge source to one scalar-priced residual. T1's minimum
therefore concerns the exact M-valued interface, not a separately minimized
scalar-price interface. T3 remains valid under that nonfaithful valuation.

A separate four-state/two-residual model has an advance action costing 1
before arrival and 0 afterward, and a lane-switch action costing 4. Word lifts
preserve charges. Physical distance from lane 0 to lane 1 at the same reported
position is 4; residual distance is 0. Every target-fibre equality holds.
This independently corroborates the endpoint limitation.

## Removing other hypotheses one at a time

| Removed contract | Independent exact witness | Required boundary |
|---|---|---|
| Additivity of valuation | Two unit edges priced by λ(n)=n² give distances 1,1,4 | Triangle fails; even the source geometry is invalid |
| Nonnegativity | λ(n)=−n prices a unit edge at −1 | Outside the declared [0,∞] Lawvere base |
| Totality / visible enabledness | Unit budget 2 authorizes a and aa, but not aaa; a report-only total abstraction authorizes aaa | Partial extension must preserve the enabled-word domain |
| Priced state restoration | Fresh→spent costs 1; spent→fresh costs 3; spend-reset-spend costs 5 | Replacing the reset price by 0 changes the charge to 2 |
| Whole-path private identity | Fixed originals have paths (5,0) and (1,4), each totaling 5 | Independent maxima invent 9; independent minima invent 1 |
| Stationarity / complete state | Constant reports, departing costs 2^(−n−1) | First charges distinguish infinitely many residuals despite summable total |
| Prefix fidelity | Charges (1,1) and (0,2) have equal final total 2 | Weight redistribution fails at the first prefix |

These are scope-removal countermodels, not counterexamples to the stated
T1–T3 hypotheses. Paid, explicitly modeled reset actions remain legitimate.
A genuine budget interface needs remaining-resource state and enabledness;
a cumulative scalar alone need not describe inventory or replenish it.
Variable source identity must be retained in the report or richer interface
if the intended quotient must preserve it.

## Mandatory scope amendment and acceptance boundary

Add explicitly: “The minimum counts reachable stationary weighted control
states for supplied mathematical cost labels. It does not measure the storage
or execution cost of encoding those labels, evaluating monoid operations,
accumulating or querying totals, retaining observation history, or scheduling
inputs. Any such variable affecting future reports, costs or enabledness must
be included in the complete state.”

A one-state unit-charge machine has cumulative total n after n actions.
Its weighted residual count is one. A Moore machine required literally to
report that unbounded numeric total has infinitely many distinct states,
because the current reports n differ. The theorem has no contradiction;
the reporting and apparatus interfaces differ. Opaque infinite-precision
constants and external clocks do not acquire finite physical storage bounds
from a finite weighted control-state count.

Primary context was checked independently:
[Mohri §§1.2, 6.3–6.4](https://cs.nyu.edu/~mohri/pub/hwa.pdf)
allows initial/final weights and weight redistribution in a different
weighted-language minimization contract.
[Lawvere's author commentary](https://www.nsm.buffalo.edu/~sww/0papers/lawveres-metric-space-paper.pdf)
provides the reverse-order nonnegative additive enrichment, allowing
asymmetry and infinite distances. These references do not certify physical
resource calibration or a new scholarly theorem.

Only new review artifacts are written. The independent standard-library probe
imports neither author code nor repository modules. Command, exit 0:

    PYTHONDONTWRITEBYTECODE=1 timeout 25s python reviews/X06_E36_probe.py --receipt reviews/X06_E36_receipt.json

Observed runtime 0.481918 seconds; 2,752 tiny weighted machines, 900 unary
lassos and 508 full-word lift checks. Raw matrices and every hostile control
are retained in the receipt. Probe SHA256:
d3c03afb193d578e72bc20593f9f71bf1f3e5c03dbf8c2ba85903ae1ef4cca14.
Receipt SHA256:
55db9bd380ce29b8046a85639ee9109aad6552e849a737e0e7c19bd119c41f98.
Finite checks support the separate universal derivations; no full suite,
compiler, child agent, shared metadata, imported file or push was involved.

Next small lemma: extend the action-congruence and fixed-representative word
lifting proof to partial actions by adding enabled-word domains to B, then
test budget updates while retaining original/current private-state correlation.
κ is exact synthetic contact; φ is the reviewed proof pathway; σ is pinned
dossier provenance, not physical source calibration; ρ is controlled by the
non-deriver check and preserved countermodels. Final principal acceptance and
any shared status updates remain outside this review.
