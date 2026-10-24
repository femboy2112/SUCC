# Cyclotomic origin to pi: selected-source execution report

**PI NORMALITY PROVED: NO.** This is a completed theorem-and-counterexample
research increment, not a claim that the selected-source cancellation gap
has closed. Academic novelty is unverified.

## Source boundary and live starting audit

The isolated branch `research/cyclotomic-selected-source-2026-10-24` starts
at PR #257, `5435497dc77a313d1ebbc56ac96c11e593db2619`, above #253.
The sibling #256 was read at `66fcb6f61b2851371bfe58ba6db74bdeacb46ef0`,
above #254. Git independently returned their common ancestor as
`364962ac0c0e8fb4d06c37468a5d50336d68a9ee`, the repaired source in #252.
Neither sibling was merged into the other. No #254 assumption is imported
to fill a missing proof: the Green and Pell inputs used here are already
on the #253/#257 lineage, and the needed #256 prime split is rederived.

The [starting receipt](CYCLOTOMIC_SELECTED_START_STATE.json) preserves live
heads and CI. At initial retrieval the focused #256/#257 jobs passed and
their full validation jobs were still running. Historical successful runs
are not final-head validation for this work. The original worktree, main,
the import manifest and archival source files are preserved.

Mandatory origin-gauge files and the complete sibling prime-window source
were audited. The origin identities, projective chord, B2 fourth moment,
periodic-point counts, selected long-period counterexamples, inverse-tree
Wasserstein law and BBP boundary transport are correct in their stated
domains. A source API caveat is explicit: an interval merely lying in
(3,4) does not authenticate pi; the actual tests supply polygon/Machin/BBP
source proofs. The new routines likewise distinguish a supplied error
budget from proof that a selected initial state satisfies that budget.

During this run #256 advanced to `0683f8f166b9106ab8405a2d6538415b5ac84ba3`
with a filtered p² lift. Its original prime-window files are byte-unchanged.
The new three-test suite passed against the actual shared source, and the
filtered recurrence was independently rederived. The paper addendum keeps
its authority separate. A claimed wrong-endpoint-gap mutation was absent
from that test file; our new exact witness supplies it (p=17: correct 175,
mutant 124). The source theorem itself was not refuted.

The readout boundary matters: dyadic changes preserve odd-primary circle
torsion and the specified filtered source, but not arbitrary raw unwrapped
carry readouts. With shift 1/16, at time 1 both circle states are 2/15 while
the unwrapped lifts reduce to 138 and 139 modulo 17². Any fixed finite list of
odd p-adic congruences can also be preserved by paying additional dyadic
precision; literal integer carry histories are not claimed preserved.

The sibling's original 12 tests were executed directly from its pinned
Git objects against the actual, byte-identical shared BBP implementation,
without the earlier minimal stub. They passed. See the
[source audit receipt](cyclotomic_selected_receipts/sibling_256_audit.json).

## The strongest positive interference theorem

Let p=8m+1 be prime, L=ord_p(16), Delta=3m and B=Delta/L. The authentic
four-pole forcing first introduces the p-primary phase 4/p at m+1, and
introduces no further p-source until 4m+1. Quadratic reciprocity gives L|m.
For h not divisible by p, retain the actual split

    y_(m+1+t)=4*16^t/p+w_t (mod1),
    u_s=e(4h16^s/p),
    z_s=B^-1 sum_b [e(hw_(bL+s))-e(hw_(bL))].

For the subgroup H=<16>, write epsilon for the largest normalized
nontrivial additive character sum over H. Exact autocorrelation proves

    sup_k |Uhat(k)|^2 <= 1/L+(1-1/L)*epsilon = delta_p^2.

This controls **every multiplicative clock character**, using only the
unweighted subgroup estimate. No arbitrary complementary weight is passed
to BGK. For good primes L>p^(1/3), the external theorem supplies
epsilon<=C p^(-nu), so delta_p tends to zero uniformly in the clock
character. Its actual prime-field, subgroup-size and nonzero-frequency
hypotheses were checked against [Kowalski's proof, Theorem 1.1](https://arxiv.org/html/2401.04756v2#Thmtheorem1.1).

Fourier completion then controls every **incomplete local interval**:

    |sum_(s<J) e(a*16^(r+s)/p)| <= J*epsilon+delta_p*L*log L,

for every J>=0, every starting r, and every nonzero a modulo p. Consequently
the original noncyclic p-local lag factors are o(Delta) uniformly over all
growing lags d<Delta with L not dividing d. Resonant multiples of L remain
exactly coherent. This is new control of incomplete local signed sums;
complete-period averages have not been substituted for them. The correct
Abel consequence still contains the actual complementary variation, which
is not bounded by the small forcing alone.

Finite Fourier pairing then proves for the **actual mixed term**

    |I_p(h)| <= epsilon*|zhat(0)|
                 +delta_p*sum_(k!=0)|zhat(k)|.

This is a quantitative inequality with a genuine unpaid factor: the
actual complementary Fourier coefficient mass. The generic bound
2sqrt(L) does not close the estimate. Taking absolute values here is a
sufficient diagnostic and can still discard useful signed alignment;
the exact complex pairing is retained in the derivation and oracles.

The exact BBP Green change of coordinates gives a further source-specific
statement. Replacing each complementary block by its free expanding orbit
with the **exact** tail included in its initial phase changes its Fourier
mass by at most

    2*pi*|h|*(sqrt(L)+1)/((8m+9)(8m+10)) = O_h(m^-3/2),

and its signed interference by O_h(m^-2). Thus small forcing creates a
small spectral perturbation, but does not prove regularity of the free
phase chosen by the source. Replacing that exact initial tail by a cheap
rational approximation would reintroduce exponential error amplification.

All derivations, constants and domains are in
[the interference paper](CYCLOTOMIC_SELECTED_INTERFERENCE.md).

## A stronger same-forcing control, with the correct quantifiers

For K=4m+q, choose a certified nearest dyadic delta_K=c/16^K to -T0.
The shifted orbit uses the **same full forcing at every time** and satisfies

    y_n(delta_K)+T_n = 16^n(delta_K+T0) (mod1),
    |delta_K+T0| <= 1/(2*16^K).

Every odd-prime-power component is unchanged for every n. Nevertheless the
whole window m+1 through 4m has normalized Fourier sum approaching 1, for
each fixed h and q. Its mixed interference also approaches1 on good
primes. The explicit all-m error is displayed in CSI-04 and certified with
exact rational Taylor boxes in the finite oracle.

For every fixed delta_K, however, the changed and original circle states
are **exactly equal after K steps**. The control therefore has exactly the
same eventual normality verdict as pi. This refutes only a uniform
finite-window estimate that ignores the dyadic depth of the selected
initial state. It is not a fixed nonnormal source or a refutation of the
full BBP contract with y0=0.

More precisely, for rational initial states under the same forcing,
complete equality of all odd-primary data is equivalent to finite future
circle-state coalescence. A finite collection of odd clocks is a weaker observation.
The exact second and fourth moments over a deep dyadic initial-state fibre
also tend to zero, even though it contains these nearly coherent members.
This reproduces the selection gap **inside the same-forcing, same-odd-clock,
eventually-coalescing class**, with all branch and initial-state labels kept.

## Observer costs and a new signed BBP carry hierarchy

The [observer paper](CYCLOTOMIC_SELECTION_RESOURCES.md) proves sharp,
restricted resource statements rather than a global impossibility claim:

* Point evaluation on the N-frequency lacunary space has exact L2 norm
  sqrt(N), consuming the entire gain of its averaged second moment.
  Translation-invariant response descriptors cannot give a uniform
  pointwise vanishing bound; x=0 is the explicit admitted counterexample.
* Exact prime-power transient/order classification gives deterministic
  base16 tomography with fewer than 9*3^v3(h)*N samples. These samples are
  not supplied for free. Modulus 27 provides an exact counterexample to
  extending second-moment clock closure to fourth moments.
* Inverse fibres satisfy W1(mu_k,x,mu_k,y)=d(x,y)/16^k. A cutoff-H Fourier
  observer first sees the root after max(0,k-floor(log_16 H)) forward
  steps. The low-frequency quotient is therefore not future-sufficient.
* Pell-corrected BBP responses have explicit all-horizon L2 comparison
  budgets while their individual second/fourth moments and derivative-L2
  norms remain identical to the authentic response.

A new source-specific signed phase is controlled exactly. For the
corrected rational phase q_n=y_n+A_K(n), its first equal-cardinality
hexadecimal carry has the lift

    16q_n+q_(n+d+1)-q_(n+1)-16q_(n+d) = -(-1)^K F_(K,d)(n) (mod1),
    F_(K,d)(n)=integral u^n(16-u)(1-u^d) dnu_K(u)>0.

Each F is an exactly rational, strictly positive Hausdorff moment sequence.
It obeys two global beta ceilings and the sharp fixed-order limit

    F_(K,d)(n)/B(8n+1,K+3) ->120*d*a_K.

Even origin moments through order 32 cannot distinguish arbitrary unit
coefficient phases. The first possible detecting moment is 34. A three-term
observer has exact moment

    [399769750195965+34*cos(2*pi*h*(16theta0+theta2-17theta1))]/3^34.

For raw BBP forced triples and h=1 this strictly differs from the
authenticated covering triples at every n>=1. It detects the actual
source correction; it does not select pi as generic. All moments of the
true translated covering family remain independent of its selected root.

## Proof authority, hostile review and reproducibility

The generic finite twisted-clock identity and squared bound, centered
signed Abel identity/bound, dyadic state erasure, and coarser actual-tail
window estimates are among **13 freshly checked Lean declarations**.
Actual theorem expressions and axiom lists were exported; only propext,
Classical.choice and Quot.sound occur. Four paired false-statement controls
were rejected while their positives compiled. BGK, the prime application,
spectral perturbation, resource theorems and all-order carry analysis retain
their separately stated paper/external authority.

An initial Abel positive-control wrapper failed because its numeric casts
did not match the theorem expression. That failed gate is preserved; the
wrapper was repaired, then a second fresh rebuild and all controls passed.
No source theorem was weakened. See [the exact formal scope](CYCLOTOMIC_SELECTED_LEAN.md).

The deterministic [finite receipt](CYCLOTOMIC_SELECTED_FINITE.json) retains
full rational source states and complements, original complex I intervals,
all tested twist intervals, rational spectral budgets, the changed source
label/depth, exact coalescence, complete clock profiles, rational carry
signs/differences, and the first phase-sensitive moment polynomial.
It includes an independent group-algebra fibre oracle that imports only
the common BBP forcing and proves finite equalities as signed rational
phase-coefficient maps. No input digits or floating values are proof inputs.

Finite tests cover disclosed examples, not a normality holdout. Independent
agents share a model family and source dossier; their different derivations,
exact implementations and Lean checks are cross-checks, not external
academic refereeing. Source membership, observed execution, survival under
the probes, and commitment to the goal remain distinct.

Local required validation is recorded in
[validation.json](cyclotomic_selected_receipts/validation.json): **7,454
tests passed in 847.966 seconds** (856.006 seconds process wall time),
including all 15 new tests. The 15 origin-gauge tests and 15 new tests also
passed separately. All 72 import-provenance entries and both required
observer/ordinal probes passed. Sibling audits add 12 original-window and
3 filtered-Witt tests, outside that full-suite count. Final-head
hosted CI and test-merge/tree identity are recorded in the delivery receipt
and PR body after observation. No hosted result is inferred from local tests.

```sh
python -m unittest discover -s tests -p 'test_cyclotomic_selected_source.py' -v
python -m unittest discover -s tests -p 'test_circle_origin_gauge.py' -v
python scripts/cyclotomic_selected_oracle.py --output /tmp/cyclotomic-selected.json
cmp /tmp/cyclotomic-selected.json research/2026-10-24/CYCLOTOMIC_SELECTED_FINITE.json
python scripts/cyclotomic_fiber_moment_oracle.py
python scripts/check_cyclotomic_selected_lean.py --output /tmp/cyclotomic-selected-lean
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

## Direct answers and the remaining smallest useful arithmetic step

**What new signed phases are controlled?** Every temporal multiplicative
twist and incomplete interval of the authentic local p-clock, including
all nonresonant growing local lags; the exact quantitative spectral
budget for its full mixed interference; the small BBP Green perturbation;
and a positive rational hierarchy of source-corrected carry phases. No
authentic full mixed term has been proved to vanish asymptotically.

**Which authentic inputs matter?** The exact four-pole source fixes the
first prime birth and complementary recurrence. The exact Green kernel
and Pell hierarchy give the spectral and carry error budgets. T0=pi/16
and y0=0 identify the actual pi-selected source. The local subgroup theorem
alone does not require that last identification and therefore cannot
silently supply its missing consequence.

**Which fake sources are rejected?** Composite or wrong-residue clocks,
p-denominator changed initials wrongly labelled p-integral, mismatched
carry signs, insufficient dyadic selectors and aliased sample clocks are
rejected by explicit contracts. The same-forcing dyadic controls pass
their stated weaker contracts and are excluded from the authentic source
by their changed initial state. Periodic and inverse-tree controls are
used only in the source-independent hypothesis classes they actually fit.

**Where is genuinely new information still required?** In the signed
coupling of Uhat and the complementary BBP spectrum at initial state zero.
The absolute Fourier-mass bound is sufficient and may be unnecessarily
strong; its failure would not refute cancellation. It is not a replacement
definition of lawful dynamics.

A next decisive theorem for h=1 would bound that actual signed pairing by
o(1) along the authenticated good primes, with all source and conductor
conditions retained. Alternatively, the earlier growing-lag aggregate
`sum_(d<R)(R-d) Re D_d(N) <= K_h N R`, for R tending to infinity and
R=o(N), would control one actual pi mode through the proved transport and
van der Corput. Both remain open; they are proof obligations, not this
round's claimed results. All required fixed nonzero modes must be closed
before hexadecimal normality is declared proved.
