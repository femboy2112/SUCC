# Hostile audit of the institute nucleus

Date: 2026-10-18. Starting branch: `research/institute-nucleus-2026-10-18`;
starting commit: `610efacf02556e1c5922bc5d4e87d0087f19b446`.
This review found and reproduced a kernel-authority transport bypass, which
was repaired. The new mathematical statements survive the derivations and
bounded controls below. No independent external peer review, academic novelty,
complete inherited source proof, physical authentication, hosted CI result,
or RH proof is certified here.

The reviewer is a separate agent stream using the **same model lineage and
shared repository**. It read the papers before challenging them. This is a
hostile second derivation with implementation diversity, not a blind or
independent-model bearing. The Aletheia method and provenance-tomography
discipline were used; no phase, probability, or quantum inference is involved.

## 1. Concrete faults and their disposition

### H-AUDIT-1: paper comparison silently feeds kernel authority

**Refuted behavior, repaired.** Initially, create kernel-typed claims A and B,
let B depend on A, and change B's topology signature. Supply an explicit
comparison edge with `authority="PAPER_PROVED"`. The registry returned
`CONTRACTS_AND_BYTES_VALID`. Checking only the authority of dependency nodes
missed the authority of the intervening comparison map.

The production repair requires kernel authority on every comparison feeding
a kernel-typed target. A claimed kernel comparison must additionally name
nonempty declarations present in the target's checked declaration list and
use its hashed Lean source as evidence. The hostile regressions reject:

- a paper comparison between kernel-typed endpoints;
- a bare kernel-authority string without declaration names;
- an unknown declaration outside the checked target manifest.

The positive control deliberately uses a synthetic `True` theorem and
synthetic receipt. Passing it proves only that the declared structural
contract is accepted. It does **not** prove that this theorem establishes a
continuity map, that the compiler was actually run, or that the natural
language statement matches the Lean type. This trust boundary remains
explicit and unavoidable for this metadata checker. Fresh fixed-toolchain
execution and semantic theorem-to-claim review are separate gates.

### H-AUDIT-2: positive local margin was named a global minimum

**Naming error, repaired.** For
`F(y)=13y/16-log(1+y^2)`, the global minimum on `[0,infinity)` is zero at
`y=0`. The positive certificate encloses the other, positive local minimum.
The receipt key was changed from `strict_global_minimum_margin` to
`positive_local_minimum_margin`. The all-y inequality was valid before this
repair; the old key overstated what the scalar certified. The exact margin
also exceeds `1/100`, as the paper claims.

### H-AUDIT-3: the recorded lower matrices are negative definite

**Documentation error, repaired.** Both new two-by-two lower matrices
have negative diagonal entries and strictly positive determinant. Thus they
are negative definite, not indefinite. Exact rational comparisons establish
the signs; decimal determinant summaries are approximately
`0.00026858614304086617` for odd derivative parity and
`0.000057910185361761984` for even derivative parity. Either “negative
definite lower certificate” or “not positive semidefinite” is accurate.

This correction makes no negative statement about the true source Schur
form. An operator can be positive while possessing a negative definite lower
bound. The strict improvement in the lower bound is real; sign certification
still fails.

### H-AUDIT-4: an Option failure carries no failed-prefix transcript

**Scope wording clarified.** `run_naturality` proves exact equality of
the `Option (List L x State)` results. A fully accepted run preserves its
whole label list. If a later action fails, both results are `none`; the data
type discards the previously successful labels and failure position. The
commuting one-step law also implies equal prefix behavior, but the displayed
`run` value itself does not return a failed-prefix receipt. This is a wording
qualification, not a false Lean theorem.

### H-AUDIT-5: parameterized replay exceeded the pinned source domain

**Input-domain mismatch, repaired.** During finalization the replay became
parameterized in J and Taylor degree M. Its first wrapper accepted J through
64, while the immutable PR177 `source_residual_schur_trial` accepts only
`1<=J<=24`. The new hostile regression failed at J25 and J64 before the
repair; its subprocess trap established that invalid requests reached
archive execution. The wrapper now enforces the actual J24 ceiling before
execution and bounds M by 256. The theorem for general Gamma coefficients
has no J24 restriction; this ceiling belongs to the archived experiment.

At J1 the selected H2 budget can remain unchanged, so the parameterized
helper correctly permits nonnegative gains. The legacy receipt key
`positive_Loewner_gain_scalar` is retained for compatibility; the new
`strict_gain` field distinguishes strict improvement from equality. The
original J8 receipt has a strictly positive gain in both parity blocks.

## 2. Atomic/Haar results: independent derivation verdicts

| Claim | Verdict | Decisive check and boundary |
| --- | --- | --- |
| AH1, all-prime bounded adjoint-preserving disjointness | PROVED LOCAL, PAPER survives | The image of every atomic vacuum lies in the common Haar adjoint kernel; the all-prime unit set is Haar-null. Forward shifts then kill the whole atomic basis. Both adjoint and forward hypotheses matter. |
| AH2, incompatible strong limits | PROVED LOCAL, PAPER survives | Atomic diagonal indicators converge to the singleton vacuum; Haar indicators converge a.e. to zero. Finite nonzero projection norms remain one, so operator-norm convergence is false. |
| AH3, arbitrary prime-subset threshold and classification | PROVED LOCAL, PAPER survives | Reciprocal-prime summability is equivalent to positive unit-set measure. The shells exhaust Haar measure exactly in that regime; both wandering multiplicities are countably infinite. |
| AH4, countable Wold warning | PROVED LOCAL, PAPER survives | Each fixed-prime isometry is pure because the nested range supports have mass `p^-r`, yet the all-prime joint wandering space is zero. This does not contradict finite-tuple theorems or establish novelty. |
| AH5, unit-supported distribution classification | PROVED LOCAL, PAPER survives | Transpose kernels impose support in the compact unit set; finite clopen separation of distinct `n Zhat^times` proves algebraic injectivity. The transpose is not a Hilbert adjoint on the distribution space. |
| AH6, weighted extension and unweighted obstruction | PROVED LOCAL, PAPER survives | Total variation is exactly the weighted `ell^1` norm. The constant test has truncated functional norm squared `H_N`, ruling out a continuous unweighted `ell^2` extension. |
| AH7, nonclosability | PROVED LOCAL, PAPER survives | Harmonic-weighted atomic vectors tend to zero in `ell^2`, while their distributional images tend to additive Haar. This is a graph counterexample, stronger than mere unboundedness. |

For AH3, the countable shell argument needs genuine summability, not only
positivity of each finite product. If `S` has finite reciprocal-prime sum,
`alpha_S sum_(k in M_S) 1/k=1`, with the Euler sum justified by monotone
limits. Unique selected-prime valuation vectors make the shells disjoint.
The complement of S is infinite; its unselected Haar coordinates ensure
that `L^2(E_S)` is infinite dimensional and separable. Every intertwiner
restricts to a bounded map between the common wandering spaces and its
values on all shells are then forced. This proves the asserted complete
classification, including `S=empty`. For divergent sums, apply the adjoint
kernel argument to **every** selected-prime-free atomic basis element,
not just `e_1`. That additional quantifier is present in the paper.

For AH5, support is a distributional statement, not an absolute-continuity
statement. A test supported outside the units has compact support covered
by finitely many prime-divisibility clopens. Refining those to a disjoint
clopen partition makes the implication from all transpose kernels rigorous.
For a finite linear relation among the `n`-pushforwards, clopen valuation
tests isolate each compact support. Scaling is injective, and every locally
constant test on its clopen image extends to the ambient profinite space.
These facts prove injectivity even for distributions that are not measures.

For AH7, independently checking the root's proposed witness gives the exact
Abel-summation identity. If
`C_r(k)=#{1<=n<=k:n=r mod m}-k/m`, then `|C_r(k)|<=1` and

```
sum_(n<=N,n=r mod m) 1/n - H_N/m
 = C_r(N)/N + sum_(k<N) C_r(k)(1/k-1/(k+1)).
```

The discrepancy has absolute value at most one. Hence the normalized
harmonic measure converges to mass `1/m` on every residue cylinder, and
therefore to additive Haar against every locally constant test. Meanwhile
the input norm squared is `1/H_N`. The graph closure contains `(0,Haar)`
and `(0,0)`, so it is not an operator graph. All statements here use the
specified weak dual topology; changing the input or target topology requires
a new argument.

## 3. Causal quotient, gluing, and public policy

The Lean quotient theorem correctly assumes a surjective quotient map,
partial deterministic actions, and full fiber congruence including the
retained labels. Necessity follows from the commuting square. Choosing one
representative per quotient point gives sufficiency. Induction on an action
word gives naturality, and unpacking a successful `some` value proves lifting
from **every chosen initial representative**, without resampling an
incompatible private state midway. This is stronger than merely requiring
each projected edge to have some source lift.

Current observations are an extra factorization checked by Python; the new
Lean Q1 type does not contain them. The paper identifies this boundary.
Immutable source tags are an extra edge invariant; the final eighth Lean
theorem, `path_preserves_source`, propagates that invariant along an actual
path. It does not derive the invariant from public report equality.

The relation-level gluing theorem is valid for arbitrary carriers and
branching on **finite** label words. Unfolding existential image propagation
maintains one compatible intermediate source state. The exclusion theorem
is the constructive backward dual of path existence. Its exclusion cuts
need satisfy only the closure implications and empty terminal cut; they
need not be the maximal sets of impossible states. The Python verifier
checks sufficient raw conditions directly and handles empty initial support
and empty transcripts correctly.

The public-policy equivalence survives under its stated model: the policy
may stop on branches outside the nominated transcript, and the initial
support lies in one observation fiber. Universal availability must be
checked **before** conditioning on the next outcome. The code does this.
It is neither a fixed-horizon strategy theorem nor a physical execution
claim. The refinement algorithm has the standard monotone finite-partition
argument and produces the coarsest lawful refinement of the initial report
partition. A mathematically finer partition need not be available as an
instrument to the observer.

The added hostile test rotates beyond the original two-state/one-action
controls: 96 seeded four-state/two-action machines, 576 state pairs,
including partiality, two public observations, two outcomes, and exact costs
`0,1/3,2`. Literal table replay enumerates all words of length at most four,
independently of production refinement and pair-graph BFS. The tested
partitions agree with these experimental traces, and every BFS witness has
the minimum length found by enumeration. This is a finite control, not the
proof of arbitrary-state minimization.

**Verdicts:** quotient/lifting, finite relation gluing, source preservation,
and exclusion survive paper review and match the final kernel statements.
Public-safe transcript equivalence and refinement correctness survive paper
review and finite controls; neither was promoted to new kernel authority.

## 4. Gamma envelope, domains, and actual source replay

The second derivative of
`f(s)=16 xi^2/[s(s^2+4xi^2)]` is the positive rational expression printed in
the paper. Width-four midpoint cells yield the shifted logarithmic upper;
width-four trapezoids yield the stated lower with half the first rung.
The factor `1/4` is essential. Letting frequency tend to zero in the lower
bound and comparing the `d^-3` term shows that every fixed shift below two
eventually fails as `J` grows. The optimality claim is exactly within that
one-parameter family, not among all possible envelopes.

The Fourier multiplier of the declared rung `4/d I - E_(d/2)` is exactly
`16 xi^2/[d(d^2+4xi^2)]`. This independently matches the source spacing and
normalization. Plancherel converts the pointwise linear/quadratic frequency
bounds to H1/H2 action bounds. The H2 route requires zero derivative trace
as well as zero value trace, because zero extension otherwise introduces
singular boundary terms. Restriction back to the interval is a contraction.
No bounded full-L2 tail estimate or change from K-relative to L2-relative
coercivity has been shown.

At J=1 the new midpoint H2 coefficient is worse; taking the minimum with the
old valid coefficient preserves the correct exception. The all-y logarithm
bound survives the independent critical-point calculation; its exact local
margin is about `0.0144255829 > 1/100`. Finite prefix checks supplement this
proof and do not replace its universal quantifier.

The source module's Git blob was recomputed as
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`. The reviewer then independently
exported PR177 commit `f309d9104ba480c1999c962af1df7c50f19e1bfe` to a temporary
directory and executed its `source_residual_schur_trial(J=8,M=80,P=18,fit=True)`.
The process used Python 3.12.3, the isolated mpmath 1.3.0 environment, a
1 GiB address-space limit, and a 60 CPU-second limit; it completed in about
eight wall seconds. Each fitted polynomial's value and derivative traces
were checked at both endpoints.

The new error and Schur update were recomputed directly, without calling
the new coefficient helper:

```
t_new = min((13/496) sqrt_up(||h'||^2),
            (2/961) sqrt_up(||h''||^2))
gain = 5/kappa * sum_i ((finite_i+t_old_i)^2-(finite_i+t_new_i)^2)
new_lower = archived_lower + gain*I.
```

For both parity blocks, exact rational equality holds with every old/new
matrix entry and gain in `INSTITUTE_GAMMA_SCHUR_REPLAY.json`. Observed output:

```
odd_derivative: exact archived source replay and independent Schur update match
even_derivative: exact archived source replay and independent Schur update match
inherited coercivity not re-proved; no positivity conclusion
```

This gives a second calculation of the **update**, while reusing the same
archived source-action implementation. It does not count as a new source
family or independent proof of the archived coercivity constants. The signed
prime/contact/pole source, all-radius conclusion, external Suzuki paper,
and academic priority have not been fully re-audited by this reviewer.

**Verdicts:** IN-GAMMA-01 and IN-GAMMA-02 survive as paper proofs on their
stated domains. IN-GAMMA-03 is an exactly reproduced strict improvement of
the same source-conditional lower bound. Genuine Schur positivity remains
undecided.

## 5. Executed checks, provenance, and remaining lamps

Actual focused commands, each with exit code zero:

```sh
python -m unittest discover -s tests -p test_institute_hostile.py -v
python -m unittest discover -s tests -p test_institute_audit.py -v
python -m unittest discover -s tests -p test_institute_schur.py -v
python scripts/institute_audit.py
```

Results after the final follow-up: **10 hostile tests, 10 registry tests,
7 Gamma tests passed**. The
hostile tests include the 576 trace pairs and 138 exact harmonic
residue-discrepancy controls (`N=1,2,11,37,128,512`, moduli `2,3,7,11`).
The real archived-source replay described above also exited zero. No heavy
suite or Lean compilation was duplicated by this reviewer.

The final central Lean receipt was inspected: its source hash matches the
current file, it lists eight declarations, reports successful compilation
and a failed false-proof control, and separates the permitted axioms.
This reviewer did not independently execute that compiler. The pinned
Lean source hash at inspection was
`7d88fe4123e07d0b5776f229d82c4b1ab593435bbe62fa1106d50fadf53016fc`.

Other inspected implementation SHA256 identities after the transport and
margin-name repairs:

| File | SHA256 |
| --- | --- |
| `observational_succ/institute_causal.py` | `79d6a9e345adc7578237bf37766042e5b7810f783a319f35141348ebe20fb01a` |
| `observational_succ/institute_audit.py` | `d2be86d9ab4c977b2230a2456ebb002ee078cd183612682578d7bb19476f367a` |
| `scripts/institute_schur_probe.py` | `ea04689cde1d74f4e389c6aa951021bac381fbebd72bfea3e033664a6099dc22` |
| `tests/test_institute_hostile.py` | `ca9422ac8aa9226a2badc730ec94668e5be91fa5fdbeb7be8c7531ae9bac28c8` |

### Actual thirteen-claim graph

The actual `institute/theorem_registry.json` was audited, not only synthetic
fixtures. The inspected snapshot has SHA256
`6aa5e6e7086a9c63e7958677347bae2922ec10ea955f2f7ec773c4a791015eb0`.
It passed with 13 canonical claims and two explicit comparison edges.
Later receipt/paper changes require refreshed hashes and another integrity
run; this fingerprint identifies the snapshot reviewed here.

`INS-01` and `INS-02` name the actual eight checked causal declarations.
`INS-03` retains paper authority for finite refinement. `INS-04` records
classical Haar scaling; `INS-05` through `INS-08` retain paper authority for
the atomic/Haar and distributional interfaces. `INS-09`/`INS-10` retain paper
authority for the Gamma envelope and action-domain estimates. None of those
analytic statements is relabeled as kernel-proved.

Crucially, `INS-11` is **UNVERIFIED**: the complete pinned source adapter and
inherited all-high K-relative coercivity have not received a complete
independent audit. `INS-12` declares `ASSUME:INS-11`, lists `INS-11` in
`proof_debt`, and the actual audit output retains it in `open_dependencies`.
Its paper result is therefore an explicitly conditional implication.
`INS-13` keeps the first-window and all-radius signed positivity targets
unverified. The output grants no semantic authority, proves no theorem,
authenticates no physical source, and reports `RH_proved=false`.

The two comparison edges preserve the relevant changes of domain:
`INS-04 -> INS-07` uses the opposite-test-adjoint transpose into Dprime,
without asserting a bounded Hilbert map; `INS-10 -> INS-12` inserts a
proved Gamma action estimate into the original K-relative source error
ledger, retaining its source-conditional geometry.

Six mutations of this **actual registry**, performed only on in-memory
copies, were all rejected:

| Mutation | Observed rejection |
| --- | --- |
| Delete `ASSUME:INS-11` from INS-12 | Unproved premises cannot disappear from a theorem type |
| Delete INS-12 proof debt | Unverified dependency missing from proof debt |
| Delete distributional comparison | Source/carrier/topology change without a proved comparison map |
| Delete Schur comparison | Source/carrier/topology change without a proved comparison map |
| Relabel universal INS-09 as an exact finite instance | An instance cannot carry universal quantifier scope |
| Mutate an INS-10 source blob | Git source identity mismatch |

A concurrent helper edit also caused the unrefreshed real registry to reject
`Evidence changed: scripts/institute_schur_probe.py`; after intentional
refresh, the baseline and six mutation controls passed. This is a successful
stale-byte guard, not a failure of the mathematical statement. The checker
cannot discover a completely omitted semantic dependency from natural
language; explicit declarations still require paper/type review.

At the initial audit, the deeper J24/M192 replay planned by the principal
was inside the repaired source domain but had not been reviewed here.
Section 6 records the subsequent exact reconstruction of its sealed data.
The independent full source replay above remains specifically J8; the
follow-up does not claim a second J24 source execution.

The evidence coordinates remain separate:

- **Contact:** current source bytes, actual finite executions, and a fresh
  archived-source run; no physical sensor or real performed event.
- **Truth pathway:** paper derivations, stated kernel theorems, finite
  controls, and receipt validation each retain their own authority.
- **Source adequacy:** Git/hash identity is checked; the source's physical
  authenticity and full mathematical interpretation are not thereby proved.
- **Commitment coupling:** shared authorship/model/source creates common-mode
  risk despite separate algorithms and reviewer roles.

Next decisive work is external mathematical review and exact prior-art
comparison for the two analytic interfaces, formalization of their
measure/operator arguments, a source-complete proof of inherited high
coercivity, and a genuine completed-Weil comparison with all source channels.
For causal generalization, preserve the distinction between nondeterministic
trace equivalence and branching congruence. Additional finite success alone
does not discharge any of those debts.

## 6. Final follow-up: universal parameter obstruction on sealed J24 data

**Verdict: valid scoped algebraic no-go, not source negativity.** The final
`scripts/institute_eta_probe.py` and paper's IN-GAMMA-04 were reviewed against
an independent derivation. Let T be symmetric, M positive semidefinite,
kappa positive, and delta_i nonnegative. In a fixed real direction c put
`t=c'Tc`, `m=c'Mc`, `e=sum_i |c_i|delta_i`. The direct triangle-budget
certificate is `t-(sqrt(m)+e)^2/kappa`. Its strict negativity is equivalent
to `H<0`, or `H>=0` and `H^2<4me^2`, where `H=kappa*t-m-e^2`.
Checking the sign before squaring is necessary.

For two columns write `a=|c1|delta1`, `b=|c2|delta2`. Every positive diagonal
Young allocation theta has directional error penalty

```
g_theta = (1+theta)a^2+(1+1/theta)b^2
        = (a+b)^2+(sqrt(theta)a-b/sqrt(theta))^2 >= e^2.
```

The isotropic penalty `||c||^2 sum delta_i^2` also dominates e^2. For any
positive normalized weights, Cauchy-Schwarz similarly gives
`sum_i (|c_i|delta_i)^2/w_i >= e^2`. For every eta>0 and any such g,

```
(1+eta)m+(1+1/eta)g >= (sqrt(m)+sqrt(g))^2 >= (sqrt(m)+e)^2.
```

Thus strict negativity of the triangle envelope blocks a PSD certificate
from **all** those parameters on the same T,M,kappa,delta. In degenerate
cases the best envelope can be an unattained supremum: a zero triangle
envelope does not guarantee an admissible finite eta with a nonnegative
lower. The criterion is an iff for strict negativity of that envelope,
not an iff for existence of a finite successful matrix parameter.

The fresh hostile controls check both sign branches before squaring, the
strict equality boundary, zero m/e cases, mixed-sign c with cancellation
retained in M, and a positive control where changing eta repairs a bad
fixed-eta certificate. They do not extrapolate the finite grid to a theorem;
the displayed inequalities supply the universal quantifiers.

For the actual J24/M192/P18 result, the independent calculator used the
sealed source decomposition with SHA256
`0a24144e8a22178296ad314e846ea13ab41a67efc291a42b6764f73d61e0d7aa`.
It reconstructed the signed energy lower T, residual Gram M, selected entire
Gamma tail matrix, and interval-radius deductions from the raw packet.
It reconstructed the fitted polynomials using the factorial formula for
Legendre polynomials rather than the production recurrence, anchored their
primitives at -1/2, evaluated derivative norms by direct monomial product
integration, and checked the exact outward square-root brackets. The source
clamped-polynomial coefficients remain the same declared input family.
All endpoint traces, combined column-error budgets, T/M entries, and exact
directional witnesses agree with the ETA receipt. No J24 source evaluation
was rerun during this reconstruction.

Both blocks have the exact witness `c=(1,0)`, and both satisfy the stronger
inequality `kappa*t-m<0`. Decimal displays of the exact rational gaps are:

| Block | kappa*t-m | H=kappa*t-m-e^2 |
| --- | ---: | ---: |
| odd derivative | -0.00006395255884716468 | -0.00006871603180253912 |
| even derivative | -0.00022976185382767651 | -0.0002376408291084794 |

Consequently, for **every eta>0 and every positive semidefinite D**,
`c'[T-((1+eta)M+D)/kappa]c <= t-m/kappa < 0`. This stronger conclusion
depends only on the recorded rational matrices and positive kappa; it does
not depend on the truth of inherited source coercivity. Interpreting such
matrices as bounds on the genuine source still does require those source
hypotheses. Even setting the error penalties to zero cannot rescue this
fixed matrix family. Changing the retained energy, nominal residual, trial,
or inverse comparison is outside this no-go and remains a legitimate next
probe. In particular, changing J may change T/M and is not ruled out.

The actual source decomposition and exact witness review support the new
`INS-14` universal finite-matrix statement. They do not discharge `INS-11`,
promote the source interpretation of `INS-12`, or resolve `INS-13`.
The updated fourteen-claim registry's final hash audit belongs to the
principal's final validation; the thirteen-claim fingerprint above is
preserved as the earlier actually inspected snapshot.

After this follow-up, `python -m unittest discover -s tests -p
test_institute_hostile.py -v` passed **10 tests** in about 0.2 seconds,
including the complete independent exact decomposition calculator.
The reviewed ETA script SHA256 is
`c497566d05a8085b57745139ce790dca124318c69ad3ca175f6ab1ad0898a8ee`;
the reviewed final ETA receipt SHA256 is
`f2ca68a76b0fd54d5dd233a4064188c228588f3ba2f87aa89ecd15560272a011`.
The grid has 240 points per parity, but neither its failures nor the 130
tested directions establish the all-parameter claim: the exact single
direction and algebra above do.
