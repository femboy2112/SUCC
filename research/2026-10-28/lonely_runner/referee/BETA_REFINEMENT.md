# Endpoint-critical Beta probe and a necessary-condition countermodel

A separate endpoint-dual probe first tested nonnegative weights on all 384
endpoint cells against 1,598 distinct rescuer patterns, with odd velocities
through 383 and the complete resonance alpha menu for the same affected
family. The floating linear program was infeasible after 1.159 seconds;
no rational dual certificate was obtained. This supplies neither an exact
nonexistence theorem nor a positive rule. Its source is
`scripts/lonely_runner_endpoint_dual.py`, and its raw JSON and log are
`receipts/endpoint-dual-190.json` and `receipts/endpoint-dual-190.log`.

The bounded search fixes the two affected odd-part chains
`{2^a,3*2^a}` below 190, giving affected family
`{2,4,6,8,12,16,24,32,48,64,96,128}`. Odd additions may have any velocity
1,3,...,31. Smaller affected supports embed by retaining other family members
as zero-phase S runners. The target gain is at least one.

Every rescuer gets the complete rational resonance alpha menu. For each
alpha, the beta menu contains zero and every value `+-1+-v/q` at which a
resonant tangent interval reaches an endpoint. Actual velocity and phase
labels are preserved, including equal endpoint patterns from different
velocities or different beta values. There are 16,317 candidates and 384
endpoint requirements. Each velocity selects at most one candidate; the
total rescuer count is at most |Q|-1.

The exact literal published L=192 rule is retained in the menu, after harmless
zero-phase padding, and passes the full exact locality checker. This is the
positive calibration. A SAT endpoint candidate would then receive a full
tangent-interval check; each genuine gap would add a clause requiring its
coverage. The implementation permits at most twenty such candidates within
a total solver/refinement budget of 120 seconds. A surviving rule would also
be instantiated and checked by the separate integer-only circle-cover verifier.

**Executed outcome:** the first solver call returned `unknown`, reason
`timeout`, after 120.030 seconds. No model was returned, so no refinement
iteration or positive certificate was produced. This is not UNSAT and is not
an exclusion of the finite menu, much less arbitrary continuous beta values.
The run used one CPU/worker and a 1 GiB virtual-memory cap. Raw metadata and
output are in `receipts/endpoint-refinement/`. The source code is
`scripts/lonely_runner_endpoint_refine.py`.
Peak RSS was 120,588 KiB. Both endpoint-control tests passed.

This differs from the previous continuous-beta timeout: endpoint-critical
candidate patterns and Boolean cardinality constraints are used, with exact
interior-gap refinement specified. The bounded outcome still leaves the
mathematical existence question open; no additional solver attempt was made.

## Endpoint coverage is not full locality

A small exact source control illustrates why the full check is mandatory.
Take R={2}, S empty, and the following four odd additions:

|v|alpha|beta|
|---|---|---|
|1|0|3/2|
|3|0|-5/2|
|5|1/2|7/2|
|7|1/2|-9/2|

For q=2,k=0, the first two runners cover z=-1 and z=1 respectively; their
tangent intervals meet [-1,1] only at those single endpoints. For k=1,
the last two runners do the same. Thus every responsible endpoint cell is
covered. At q=2,k=0,z=0 no rescuer covers. The exact gap constructor supplies
an actual finite source failure at N=12, delta=1/13, b=1, t=0: q=2 is
responsible and all four rescuer distances exceed delta.

The gain of this control is -3. It refutes sufficiency of endpoint tests,
not a positive-gain existence or nonexistence statement. Closed endpoints
are intentional and valid. The tests in `test_lonely_runner_endpoint_refine.py`
verify the published positive calibration and this negative source control.

Priority of basic endpoint-cover counterexamples is not claimed. The next
productive step would need a new arithmetic or combinatorial pruning theorem,
or an explicitly larger search budget; the recorded timeout supplies neither.
