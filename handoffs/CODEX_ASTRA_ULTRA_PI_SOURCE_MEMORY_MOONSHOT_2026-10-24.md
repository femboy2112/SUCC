# ASTRA ULTRA / CODEX — OPERATION π SOURCE MEMORY → SIGNED TIME-CORRELATION

**Mode:** EXECUTE genuine mathematical research, adversarial proof verification,
formalization and commits; NOT speculative roadmaps, NOT π-normality claims
without a complete all-horizon proof. Maximize mathematical gain per unit
compute and wall time.

**Repo:** https://github.com/femboy2112/SUCC
**New repaired source branch:** research/bbp-source-fidelity-hausdorff-moment-2026-10-24
**Parent:** DeepSeek research PR #251 at de257fad8966bbe02ecdd19c2c0e9f68cee77e15
**Grandparent:** Academic Main IX candidate PR #250 at
f986507851e34636f60bee657dcdf0771a934380
**Historical main:** Academic Main VIII b116841f12b41aaf7600da39bbb40577f25b6295.
Recheck all current heads, CI, and branch status. The user requested
this repair and source-specific work; do not merge/publish without complying
with repo's actual review and validation requirements. Keep archival histories.

## The essential repaired mathematics — START HERE

Four forcing-index poles:
  (a_i,rho_i)=(7/8,1/2),(1/2,-1/4),(3/8,-1/8),(1/4,-1/8).
  r(n)=sum_i rho_i/(n-a_i).
  m0=sum rho_i=0, m1=sum rho_i*a_i=15/64.
Their first signed moment produces the actual n^-2 coefficient.
Their artificial T16-pushforward is ZERO because 16a_i=0 mod1
and the total mass is zero, but their source Stieltjes readout
r(n) is NONZERO. That pushforward was NOT an authenticated source
dynamics map. The old "all poles transient, lane closed" conclusion
is mathematically wrong.

An exact positive kernel exists:
  g(t)=4-2t^3-t^4-t^5
      =2(1-t^3)+(1-t^4)+(1-t^5)>0 for 0<=t<1.
  r(n)=int_0^1 t^(8(n-1))*g(t)dt, n>=1.
  T_n=sum_(k>=1)16^-k r(n+k)
     =int_0^1 t^(8n)*g(t)/(16-t^8) dt.
Let u=t^8 and dmu(u)=g(u^(1/8))/[8u^(7/8)(16-u)]du.
Then T_n=int u^n dmu, with mu having a strictly positive
density on (0,1). Thus for ALL n,k>=0:
  (-1)^k Delta^k T_n=int u^n(1-u)^k dmu>0.
The Hankel Gram [T_(i+j)]_(0<=i,j<=m) is strictly PD
for every finite m. T_n cannot be a finite-dimensional,
time-HOMOGENEOUS linear realization. Its generating function
  sum_(n>=0) T_n z^n=int (1-zu)^-1 dmu, |z|<1
is not rational. The elementary BBP integral independently
identifies T_0=pi/16.

The backward recurrence:
  16 T_n=r(n+1)+T_(n+1)
has a unique BOUNDED solution. The source-authenticated
forward recurrence is y0=0, y_(n+1)={16y_n+r(n+1)}.
It follows exactly that
  {y_(n+1)+T_(n+1)}={16^n*pi}.
Changing y0 to 1/3 while retaining r changes the
selected circle phase to 1/3+T0 and gives y1=7/15,
NOT the unforced fixed point 1/3. The original
DeepSeek "same forcing α=1/3" countermodel was outside
the complete source fiber.

Four readouts r(1)..r(4), with pole positions authenticated,
uniquely recover the signed residue vector; the exact Cauchy
matrix determinant is 8388608/1224171073125 !=0.

The positive rational counterfeit T_n^*=1/[(n+1)(n+2)]
has all-size strictly positive Hausdorff/Hankel structure;
r^*(n)=16/[n(n+1)]-1/[(n+1)(n+2)] is positive O(n^-2);
but T0^*=1/2 and its selected circle orbit is nonnormal.
So a positive infinite-memory Green carrier is NOT sufficient
for normality, absent the precise BBP source data.

The older "geometric 16^-n is non-coboundary" example is
WRONG outside rational-function restrictions:
  16^-n=16 q(n-1)-q(n), q(n)=16^-n/255.
A stronger genuine RATIONAL source-control family is
  R_K(n)=K!/[n(n+1)...(n+K)],
  R_K(n)=sum_(j=0)^K(-1)^j binom(K,j)/(n+j).
Its rational pole residue-class invariant is
  (1-16)^K !=0
but its forcing decays O(n^(-K-1)) for arbitrary K.
A nonzero rational-coboundary obstruction does NOT
fix an algebraic tail decay exponent.

The claimed universal bound on absolute prime-word
min-plus costs in PR #251 is FALSE. For the source
delta_(1/8) with c_n=cos(n*pi/4), d15=d255=2sqrt(2),
and with R=3,
  (2/9)*(2*d15+d255)=4sqrt(2)/3 > 4/3,
contradicting the claimed right-hand side.
Endpoint phases may agree while absolute path costs
are large. Preserve signed lag correlations.

**Read the complete repair dossier:**
research/2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md
and executable code:
observational_succ/bbp_source_memory.py
tests/test_bbp_source_memory.py
research/2026-10-23/CYC03_LANE_CLOSED.md (corrected)
research/2026-10-23/CYC03_LANE_CLOSED_HISTORICAL.md (unaltered former claim)

The proof-mechanism tool now separates a self-reported
negative margin from finite-checker-authenticated source
membership; bisection reports a dyadic bracket, not the
unknown threshold itself. Even code-checked membership
is not a Lean theorem certificate.

## PRIORITY A — Independent REFEREE AND PROOF FORGE

Rederive every coefficient, integral, density, signs, domains,
convergence interchange, uniqueness, and Hankel rank. Test
a full range of n,k and wrong-source mutations using two
independent oracles. Do not trust prose or local CI receipts
unconditionally; inspect hosted exact-head logs.

Attempt Lean proofs for finite exact:
  pole moments m0,m1;
  four source readouts and Cauchy nonzero determinant;
  positive g(t) factorization on [0,1);
  algebraic recurrence and source-state mismatch;
  high-order rational control and nonzero weighted invariant;
  exact delta_(1/8) min-plus refutation (Qsqrt2).
For full analytic Hankel / moment claims, paper proof
is acceptable only with explicit rigorous measure/convergence
premises; do not fabricate a Lean axiom or label as checked.

Report mathematical provenance against classical Hausdorff
moment, Stieltjes/Pick, Cauchy interpolation, BBP and
Bailey–Crandall–Lagarias research. Scholarly novelty UNVERIFIED.

## PRIORITY B — ONE GENUINELY NEW π-SPECIFIC THEOREM

The target is to derive from the PRECISE G(t) source a
source-authenticated estimate that does not hold for generic
positive Green/Hausdorff sources. Start with one modest
unconditional analytic theorem about the actual BBP-selected
digit orbit. Seek all-horizon signed-frequency or lag constraints,
not another sufficient condition equivalent to normality.

Let e(t)=exp(2*pi*i*t), h!=0, and
  A_(h,N)(pi)=N^-1 sum_(j=0)^(N-1) e(h16^j pi)
  C_d(N;pi)=sum_(j=0)^(N-1-d)
           e(h(16^d-1)16^j*pi).
Weyl says base-16 normality iff A_(h,N)->0 for
every fixed h!=0. RH by itself doesn't imply this.
DO NOT assume a generic mixing theorem for the
π-selected initial phase.

Suggested executable parallel attack lanes:
- B1. Green / Fourier: construct the actual two-sided
  SUCC/FUCC source-to-phase functor with T_n as positive
  contraction moments and x_j={16^(j+1)T0}. Determine
  whether source-specific analyticity, pole geometry,
  or orthogonal-polynomial structure yields ANY verified
  sign-sensitive bound for one h or cyclotomic lag family.
- B2. Cauchy / rational approximation: source-certified
  Gauss quadrature, Padé or rational approximants to
  T0 with FULL error and observation-horizon budgets.
  Attack a genuinely incomplete exponential sum rather
  than assume complete-period mixing; preserve phases
  and conductor.
- B3. Cyclotomic signed correlation: exploit
  16^d-1=prod_(e|d)Phi_e(16) and the exact
  van der Corput lag identity. Keep signed correlations
  to the end. Compare with the lossy min-plus
  source cost and exhibit sources where the latter
  overestimates dramatically.
- B4. Exact BBP/nonautonomous dynamics: derive a
  new operator transfer, effective recurrence, or
  arithmetic obstruction from the ACTUAL forcing
  r(n) (not only rational pole count or decay).
  Verify the source initial value and backward tail
  throughout. If it produces only a reformulation,
  label as such and pivot quickly.
- B5. Independent skeptical lane: construct irrational
  nonnormal positive-moment and rational period
  counterfeits; identify if any candidate lemma
  wrongly classifies them or silently chooses Haar.

Prioritize a new unconditional π theorem even if
much weaker than normality. One source-specific
infinite-horizon inequality is more important than
100 finite digits or ten equivalent criteria.

## PRIORITY C — Improve SUCC's rigorous source semantics

Develop genuinely typed distinction among:
  pole-index coordinates,
  the positive measure/harmonic Green carrier,
  forward circle state,
  actual causal history,
  the observable family,
  source/authentication authority,
  generic source-family theorems,
  individual selected trajectory.
Define what a morphism must preserve, which limit
topology it uses, and how its time memory is retained.
Formally distinguish category-theoretic faithfulness
(injectivity on Hom sets), observational
target-sufficiency, source consistency, and
instrument failure detectability.

The signed pole measure disappearing under T16
is a TYPE-ERROR EXAMPLE, not evidence the
original forcing disappears. Use adversarial
commuting-square tests that fail the wrong map
and pass the genuine Green transform.

## PRIORITY D — PERFORMANCE / VALIDATION

Work on independent research branches and draft PRs;
preserve all original PR ancestry, archived failed attempts,
and historical SHA-backed sources. Do not silently merge
#251's older false claims into Academic Main IX.
The #250 integration candidate separately passed
29 hosted workflows / 7374 full Python tests on 3.10
and 3.13 at last inspection; verify current state.
If #250 has already reached main, rebase the
research stack with full source/replay verification.

Fan out independent derivations/tests/formal work, but
serialize full suite and Lean/mathlib builds on the
resource-constrained computer. Run focused exact tests
before broad hosted CI. Reject use of float π or a
low-precision mpf created outside the working context
for 16^N*pi fractional orbits. Numerical data must
carry certified errors to support a finite claim.

Ensure:
  python scripts/verify_provenance.py
  python -m unittest discover -s tests -p 'test_*.py'
  python scripts/observer_foundations_probe.py
  python scripts/ordinal_succ_report_probe.py
and all dedicated formal/source workflows passing,
on the FINAL combined SHA. Investigate old
PYTHONPATH/import subprocess artifacts separately
from true mathematical failures.

## REQUIRED DELIVERABLES (DONE, NOT ROADMAP)

1. Independent proof audit with exact source SHA and all
   corrections; preserve original invalid claims as
   superseded history rather than erasing evidence.
2. Mathematical manuscript deriving the strongest
   new actual theorem or a source-typed rigorous
   no-go with a minimal counterexample.
3. Executable independent exact or certified-interval
   model and hostile negative controls.
4. Lean kernel-check material where feasible;
   name precisely which claims remain paper-proved.
5. Committed modular implementation + draft PR,
   hosted CI and provenance receipts.
6. A claim ledger mapping
   CLASSICAL / PROVED PAPER / LEAN CHECKED /
   EXACT FINITE TESTED / REFUTED / UNVERIFIED.
7. An explicit final status of π normality in
   base 16, base 2, base 10, and absolutely.
8. The NEXT source-specific lemma with
   its exact falsifier and why it is NOT
   just Weyl's criterion in new notation.

**Do not let a negative result about an inappropriate
quotient or absolute-value majorant close the
authentic BBP route. Preserve exactly what the
source causes, and attack the SIGNED temporal
phenomenon it still cannot explain.**

**GO FOR THE RIGOROUS π MOONSHOT.**
