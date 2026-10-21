# Duck → Lean → π: research execution report

Date: 21 October 2026. Draft PR [#232](https://github.com/femboy2112/SUCC/pull/232).
Starting main: `b116841f12b41aaf7600da39bbb40577f25b6295`.
Starting PR head: `9894d39250021bbbc2615c33dee0d286ddf0950f`.
The existing draft is extended without rewriting its history. Main is unchanged.
The successful mathematical build is `2aeaa6dba70ca6fefefe0f8eb73078a6a17eff19`;
subsequent documentation preserves its exact checked source hashes. The actual
PR head and its final combined checks are recorded on the linked draft.

## Mathematical gains

* Observable quotients now have exact universal descent statements, and finite
  relation tables generate Lean certificates proving agreement for every word.
  The separate finite search has a sharp paper bound on distinguishing depth.
* The actual BBP identity and its π source transport have compiled in Lean,
  including an analytic integral proof of the source identity. The rational
  forcing and geometric tail are independently checked against exact formulas.
* Canonical overlapping block frequencies use half-open cylinders. The genuine
  circle-to-logistic map is continuous, onto the unit interval, and noninjective.
* A sharper tail gives Fourier-sum difference at most |h|/5, Wasserstein distance
  at most 1/(40N), and arc-discrepancy difference at most (33/32)N^(-2/3).
  These are paper transport theorems, not estimates for either orbit separately.
* The actual forcing has no rational shift correction, yet every weighted
  neighborhood contains positive rational-shadow counterfeits with the same
  leading term. A declared rational degree bound restores a decisive finite
  discriminator: one of 2d+5 exact probes must fail.
* RH gives a precisely scoped genuine-prime approximation/Fourier-difference
  theorem. ABC gives a normalized integer-residual/radical inequality. Neither
  supplies the missing π-specific cancellation.

The next verdict-changing theorem remains a source-specific sublinear bound
for the Fourier sums of the actual π digit orbit. No normality theorem is
claimed. The failure of a candidate mechanism is not a refutation of normality.

## Evidence and navigation

The [kernel receipt](DUCK_PI_KERNEL_RECEIPT.md) records the successful whole
project: 146 theorem exports, six generated declarations, and 13 rejected
mutations. The [validation history](DUCK_PI_VALIDATION_HISTORY.json) preserves
seven failed attempts before that successful run, including exact heads and
diagnostics. The [local receipt](DUCK_PI_LOCAL_VALIDATION.json) records a
6,610-test full-suite pass before the ten added dependency tests, followed by
a 63-test focused pass that includes all ten. Production Python sources did
not change between those checks. Final Python 3.10/3.13 and installed-kernel
checks are read from the actual PR head, not inferred from these earlier runs.
The [claim supplement](../../docs/CLAIM_SUPPLEMENT_DUCK_PRINCIPLE.md) preserves
the original identifiers; the [dependency ledger](../../docs/DUCK_PI_DEPENDENCIES.json)
separates proved implications from their open instantiated conclusions.

| Family | Detailed proof / audit |
|---|---|
| Observable quotients and finite probes | [Observer certification](DUCK_OBSERVER_CERTIFICATION.md) |
| Rational forcing and analytic tails | [BBP formal transport](DUCK_BBP_FORMAL_TRANSPORT.md) |
| Actual π source identity | [Integral proof](DUCK_BBP_SOURCE_IDENTITY.md) |
| Normality vocabulary and logistic factor | [Normality dossier](DUCK_NORMALITY_AND_LOGISTIC.md) |
| Quantitative transport and source counterfeits | [Analytic investigation](DUCK_ANALYTIC_MOONSHOT.md) |
| RH / ABC conditional source transport | [Conditional dossier](DUCK_RH_ABC_GAMMA_CONTINGENCY.md) |
| Independent hostile review | [Referee report](DUCK_INDEPENDENT_REFEREE.md) |
| Target and falsifier contract | [Execution contract](DUCK_EXECUTION_HOLE_CONTRACT.md) |

The agents used the same model family. Separate derivations, independent
algorithms, symbolic checks and actual kernel checking are identified by
mechanism; internal agreement is not an external academic referee report.
Most structural and analytic tools are classical. The explicit constructions
are new to this project; academic novelty is unverified.

## Strongest checked source-specific statement

Let `y_0=0`, `y_(n+1)=16y_n+r(n+1)` be the actual BBP lifted recurrence,
and let `T_n=sum_(k>=1)16^(-k)r(n+k)`. For every integer n>=0, Lean proves

\[
\frac{15}{1024(n+2)^2}
<d_{\mathbb R/\mathbb Z}([y_{n+1}],[16^n\pi])
=T_{n+1}\le\frac1{(8n+9)^2}.
\]

The actual BBP identity is proved from calculus, rather than supplied as a
new axiom. The distance is on the circle; real fractional representatives
need not be close across their cut. This theorem proves source-faithful
shadowing, not cancellation or digit statistics.

The full conditional theorem is also kernel-checked:

```lean
baileyCrandall_fourier_implies_pi_normal16
  (hu : FourierCancellation
    (fun n => ObservationalSUCC.BaileyCrandall.liftedOrbit (n+1))) : PiNormal16
```

Actual characters and Fourier density give continuous-test Haar convergence.
Compact uniform continuity and Cesaro convergence transport it across the
vanishing circle error. Portmanteau and the null three-point arc frontier give
half-open interval frequencies; the exact floor identity gives all canonical
overlapping digit-block frequencies. None of those arrows assumes π-normality.
The displayed `hu` is still an unproved, source-specific global hypothesis.

## Earned negative theorem and discriminating probe

For every integer K>=1, the positive rational forcing

\[
\widetilde r_K(n)=\frac{16^K r(n)-r(n+K)}{16^K-1}
\]

has the same leading term `15/(64n^2)` as BBP and satisfies

\[
\sup_{n\ge1}n^2|\widetilde r_K(n)-r(n)|
\le\frac{47}{15(16^K-1)}\longrightarrow0.
\]

Nevertheless each resulting orbit approaches a finite rational orbit and is
not equidistributed. The complete paper proof constructs its rational shift
correction explicitly. Thus decay, matching leading asymptotics and arbitrary
weighted closeness cannot alone certify the desired distribution. This does
not decide whether the actual π orbit is normal.

The actual BBP forcing has no rational shift correction, by four nonzero
weighted pole invariants. Under the additional declared degree bound d and
nonsingularity assumptions, a proposed correction must fail one of `2d+5`
exact probes. Independent polynomial-root and symbolic checks support that
paper theorem. It is an effective model discriminator, not a normality proof.

## Completed validation and remaining boundaries

The source verifier confirms all 72 items, including 17 byte-identical
archives and 55 established namespace migrations. Academic Main VII/VIII
ancestry, namespace and authority gates pass locally. Required observer and
ordinal probes pass. The navigation audit found no missing target among 269
local Markdown links before the final receipt links were added. The final
48-node dependency ledger passes its diagnostic and is now checked by CI.
The ledger validates declared structure only; it does not confer authority.

The final internal referee retrieved the hosted build directly and compared
its decoded observation, source hashes, actual types and axiom dependencies.
Generated finite certificates are rechecked by Lean, independently of the
Python search verdict. The exact arithmetic also has independent positive
fraction, polynomial, Machin-source and symbolic controls. These mechanisms
are distinct; the agents themselves are from the same model family.

* **Established here:** the exact Duck quotient/certificate laws; genuine
  logistic factor; actual BBP identity and quantitative shadowing; the complete
  conditional source-to-normality bridge; the stated paper transport and
  counterexample theorems.
* **Formal debt:** base-16-to-base-2 descent, quantitative Fourier/discrepancy
  constants and the rational-pole/degree counterexample package remain paper
  proofs rather than newly kernel-checked declarations.
* **Open pathway:** a source-specific sublinear Fourier-sum bound for the
  actual forced orbit or π digit orbit. No tested prefix or irrationality
  measure has supplied it. Weyl transport moves a proved bound; it does not
  create the missing cancellation.
* **Conditional boundary:** RH supplies the explicitly scoped prime-source
  approximation estimate, with exponential cutoff cost for this digit route.
  ABC constrains an actual integer residual; joint approximation/radical
  control is still missing. Neither assumption yielded normality here.
* **Unresolved:** π-normality in bases 16, 2, 10, and absolute normality; RH,
  integer abc, and binary Goldbach. No claim about any is promoted.
* **Priority:** the general machinery is classical; refinements and explicit
  constructions are new to this project. Academic novelty and publishability
  require outside literature/referee scrutiny. No publication is authorized.

The next verdict-changing arithmetic result is genuine cancellation for the
actual source, with all index/frequency quantifiers and constants stated. The
new counterfeit theorem is a demonstrated boundary on weaker substitutes.
The source-identity and conditional-transport gaps have been closed in Lean;
that specific global arithmetic gap has not.
