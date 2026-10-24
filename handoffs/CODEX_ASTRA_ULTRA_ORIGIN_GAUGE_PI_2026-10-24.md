# CODEX ASTRA ULTRA — OPERATION ORIGIN HOLONOMY → π
## Circle Gauge, Cyclotomic Coverings, BBP Source Selection and Signed Cancellation
### Maximum mathematical throughput; prove new things, do not rename the open target

**Repository:** https://github.com/femboy2112/SUCC
**Primary NEW research:** draft PR #257,
https://github.com/femboy2112/SUCC/pull/257
**Branch:** research/cyclotomic-origin-gauge-2026-10-24
**Observed source starting point:** PR #253 head
2ab8a8527b7ba3f990d75fd618a4bfd034b26b4b.
**Siblings:** PR #254 Green Rank/Coefficient Duality, which builds
independently on #252. Do not silently merge or inherit its
unreviewed paper claims. PRs #250 and #251 still have source/review
integration roles; PR #252 repairs invalid DeepSeek BBP pole claims.

Recheck actual heads, CI, provenance, AGENTS.md and imported theorem
authority before work. Work on fresh research branch(es), draft PRs,
keep histories, and DO THE MATHEMATICS. No main merge, tag, release or
publication unless separately permitted by the repository instructions.
No invented Lean authority, hidden π digit normality premises, or
positive-chord→signed-Weil inference.

## A. WHAT IS NOW EXACTLY PROVED, AND ITS CRITICAL LIMITATION

Bare circle geometry admits every origin, but a fixed expanding
covering T_b(x)=b*x mod1 is NOT rotation-equivariant without
conjugating the map. Let R_a(x)=x+a.

  R_-a T_b^d R_a(x)
      =b^d*x+(b^d-1)*a.
  H_d(a)=(b^d-1)*a mod1.

This is the **ORIGIN COVARIANCE COCYCLE**, not an actual dynamical
randomizing symmetry or a physical inertial-frame principle.
The fixed action T_b commutes with R_a precisely when
(b-1)a=0; at b=16 exactly 15 commuting origin rotations.
They have identical |A_(h,N)|, even while averaging their
COMPLEX values can give 0 for every source including x=0.

The time-cyclotomic lag factors 16^d−1 are EXACTLY the
origin covariance frequencies evaluated on the moving source
point 16^j*pi. They have prime factorization
  16^d−1=prod_(e|d) Phi_e(16).
This is our **same arithmetic object**, newly given a
source-correct geometric meaning.

Uniform average over independent origin shifts DOES
give exact shrinking differential:
  int |A_(h,N)(x+a)-A_(h,N)(y+a)|² da
    =N^-2 sum_(j<N)|e(hb^j(x-y))-1|² <=4/N.
And the exact FOURTH moment of the single shifted
orbit functional is
  int |A_(h,N)(x+a)|^4 da=(2N²−N)/N^4.
The fourth bound is summable in N and proves base-b
normality of x+a for HAAR-ALMOST EVERY a, for any x,
by Markov, Borel–Cantelli, countable modes and Weyl.
It does not show the source-selected a=0 is normal.

The adverse witness is maximally sharp: for b>=3
and d>=2, m=b^d−1, the full m-torsion group of
period-d origins tends to Haar at W1=1/(4m).
Yet the selected genuine exact-period-d orbit of
x_d=1/m converges to delta0 with W1=1/[d(b−1)],
while its fixed-h normalized Weyl amplitude tends to 1.
The full ensemble Fourier mean is EXACTLY zero at
small frequencies. Same global rules, opposite selected
trajectory. This precisely refutes "spatial origin
homogeneity alone forces selected-time genericity."

For fixed b, the number of exact-period-d points is
P_b(d)=sum_(e|d)mobius(d/e)*(b^e−1), and the
number of primitive cycles is P_b(d)/d. It is NOT
Phi_d(b); the two invariants must not be conflated.

In stereographic/projective chart s=tan(pi*x), moving
origin is Möbius:
  s -> (s+tan(pi*a))/(1-s*tan(pi*a)).
The projective chart's infinity is NOT an arithmetic
infinity. The intrinsic chord metric is
  4(s-t)^2/[(1+s²)(1+t²)].
Coordinate differences can diverge near a chart pole;
covering dynamics expands small physical separations
exponentially before wrapping.

**Mandatory reading:**
- research/2026-10-24/CIRCLE_CYCLOTOMIC_ORIGIN_GAUGE.md
- docs/CLAIM_SUPPLEMENT_CIRCLE_ORIGIN_GAUGE.md
- observational_succ/circle_origin_gauge.py
- tests/test_circle_origin_gauge.py
- research/2026-10-24/PI_SOURCE_GENESIS_REPORT.md (#253)
- research/2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md (#252)
- independent sibling research/2026-10-24/BBP_GREEN_RANK_COEFFICIENT_DUALITY.md (#254)

## B. REAL PROOF OBJECTIVE — TRANSFER AN ENSEMBLE BOUND TO π'S PINNED ORIGIN

We have genuinely small *origin-averaged* second/fourth
moments, but a selected point may be exceptional.
Prove an INDEPENDENT mathematical lemma from the
authenticated BBP/polygon/Wallis source that
constrains the selected π phase, not just a typical
rotation. In particular, derive a new all-horizon
SIGNED estimate for at least ONE actual pi mode.

For h!=0 and b=16,
  A_(h,N)(pi)=N^-1 sum_(j<N)e(h16^j*pi).
For d>=1,
  C_d(N;pi)=sum_(j<N-d)
         e(h(16^d-1)16^j*pi).

The source-equivalent BBP forced orbit y_(n+1)
is rational, y0=0, and has unique bounded
tail t_n with
  16t_n=r(n+1)+t_(n+1), t0=pi/16.
The BBP forcing is literally the MOVING-ORIGIN
connection 16t_n-t_(n+1)=r(n+1). The corrected
covariant orbit identity is
  {y_(j+1)+t_(j+1)}={16^j*pi}.

PR #253 already proves the signed lag comparison
uniform in lag. NEW PR #257 exposes the exact
monotone telescoping source boundary:
  sum_(j=0)^(N-d-1)
     [t_(j+1)-t_(j+d+1)]
   =sum_(n=1)^min(d,N-d) t_n
    -sum_(n=max(d,N-d)+1)^N t_n.
That gives a source-only RATIONAL finite-lag
error budget with π<22/7. It is transport,
not cancellation. Do not reprove it as a new
π-normality estimate.

**Best first concrete theorem:** construct the
source-justified bound
  sum_(d=1)^(R-1) (R-d) Re D_d(N)
         <= K_h*N*R,
with K_h independent of N, R≈c log_16 N,
where D_d(N) is the authentic *signed* BBP
forced lag sum (not absolute prime-word cost).
For one h this gives a genuinely sublinear
bound on that mode via van der Corput.
For all fixed nonzero h it would prove π
normal in base16. This inequality is OPEN;
never assume it or restate it as if obtained.

## C. FAN OUT INTO DISTINCT HIGH-IMPACT LANES

### Lane 1 — Gauge-anchored analytic nonconcentration
Use the exact L2/L4 Haar-origin proofs to ask if the
authenticated BBP source gives some stronger source
continuity/transversality property allowing evaluation
at a=0, with a quantified dependence on N.

Derive the exact derivative/Sobolev resource cost of
the gauge response G_(h,N,x)(a)=A_(h,N)(x+a):
  ||G||_2²=1/N,
  ||G'||_2²=(2πh/N)² Σ_(j<N)b^(2j).
Determine whether this grows too fast for generic
point-evaluation from small Lp origin norms, and prove
a rigorous impossibility for insufficient generic
regularity assumptions. Then seek the *specific BBP*
source condition that could defeat the generic loss.

Do not assume a random frame is an actual π source.
A general Sobolev estimate that remains trivial at
a=0 does not solve anything; preserve that verdict.

### Lane 2 — Cyclotomic clock and orbit tomography
Exploit the exact frame coefficient readout:
(1/m) Σ_(r<m) G_(h,N,x)(r/m)*e(-hb^k*r/m)
  =e(hb^k x)/N
when hb^j are distinct modulo m.
Build optimal finite clocks m with large
ord_m(b), exact cyclotomic/CRT proof
certificates, and matching lower bounds on sample
cost for L2 and L4 observer languages.

The m=b^d−1 torsion frame is fully source-compatible
but can hide selected nonnormal period-d trajectories.
Can source-conditioned clock sampling avoid this
alias without assuming its conclusion?

Do not confuse multiplicative factors Phi_d(b),
periodic-point counts P_b(d), and prime-power
carry representations. Check exact map laws.

### Lane 3 — Nonautonomous BBP co-moving gauge
Use four signed BBP forcing-index poles, its positive
Hausdorff Green representation, Pell endpoint
coefficients, and source-selected t0=π/16.
Develop one genuinely new source-specific theorem
on the induced complex holonomy sequence
e(h(16^d−1)16^jπ). Explore signed moments,
phase-sensitive transfer operators, twisted
Green/Perron–Frobenius forms and authenticated
nonresonance estimates. Do not use the invalid
"poles are transient circle states" claim.

### Lane 4 — Complete inverse SUCC/FUCC tree
The full b^k inverse-image measure of any point x:
  mu_(k,x)=b^-k sum_(r<b^k)δ_((x+r)/b^k)
has exact Fourier cutoff and W1 distance to Haar
1/(4b^k), while (T_b^k)_*mu_(k,x)=δ_x.
Formalize the projective fiber law, selected-path
information loss, source-labelled right inverses,
and the noncommuting k-limits. Determine if a
source-authenticated choice of inverse branch can
yield NONCIRCULAR constraints for π.

An unlabelled inverse-tree Haar proof applies to
x=0 too; it cannot establish selected π normality.

### Lane 5 — Adversarial mathematical referee
Try to kill every conjectured implication with:
fixed x=0, x=1/3, the 15 commuting hexadecimal
origins, m=7/15/17 alias clocks,
x_d=1/(16^d−1) with full period d but limiting
delta0, certified π periodic shadows, the
3-adic counterfeits #249, positive infinite-Hankel
rational source fakes, signed-pole source mutations,
and the δ_(1/8) absolute prime-path-cost failure.
Check source membership, not mere similarity.

## D. THE PRECISION/LOGICAL FIREWALL

- Circle R/Z is isomorphic as a topological space to
  one-point compactified R, not canonically as the
  line's ordinary additive group with its usual
  translations and inherited ∞ arithmetic.
- Gauge relabeling of one actual state requires
  CONJUGATING the map/observables. Sampling x+a
  under unchanged T_b means DIFFERENT sources.
- Averaging selected trajectories over a is a
  source-loss operation; without independent
  reconstruction it does not constrain π at a=0.
- Compactness bounds circle distance by 1/2,
  but a difference 1/(2b^n) expands to 1/2 in n
  steps. No horizon-uniform contraction follows.
- A generic Haar-a.e. normality theorem is
  classical and does not select π.
- Avoid assuming independent prime actions
  preserve the empirical π orbit measure.
- Finite Fourier/cyclotomic/polygon observation
  receipts must not be promoted to N→∞.
- The BBP source Green Hankel positive form is
  NOT the completed signed Weil form.
- PR #254 paper theorems are independent sibling
  work; cite and audit instead of inheriting them
  as previously installed source authority.

## E. EXECUTION AND DELIVERABLES

Operate on fresh branches/draft PR(s), exact SHA.
Read and follow AGENTS.md. Do not force main merges,
publish, tag or alter frozen archived originals.

Priority per unit time:
1. One exact lemma stated with hypotheses/quantifiers.
2. Two independent derivations or adversarial search.
3. Exact Fraction/cyclotomic/interval test and mutant.
4. Formal Lean checker only when financially useful.
5. Coherent commit with source/claim receipt.
6. Next genuine theorem, not a speculative roadmap.

Use small fan-out; serialize expensive mathlib/full-suite
builds. Validate:
  python scripts/verify_provenance.py
  python -m unittest discover -s tests -p 'test_*.py'
  python scripts/observer_foundations_probe.py
  python scripts/ordinal_succ_report_probe.py
and the actual dedicated workflows at FINAL head.
Preserve failed runs, exact source imports, Lean theorem
type/axiom audits and scholarly-novelty uncertainty.

REQUIRED final results:
- full independent audit of #257 origin/cyclotomic laws;
- any new rigorously proved source-specific π theorem
  or quantified no-go, not merely a normality criterion;
- explicit signed correlation budgets and remaining
  all-horizon hypotheses;
- source-pinned code, negative controls, formalizations
  where appropriate, committed artifacts and draft PR;
- if a proof of π base16 normality really emerges, derive
  ALL required nonzero Fourier modes with correct limits,
  then use the Lean/BBP Weyl bridge; do not silently infer
  base10 or absolute normality;
- exact explanation of what the source supplied that
  generic circle symmetry could never have supplied.

**π NORMALITY: OPEN. PROVE THE BBP-SELECTED SOURCE LAW
THAT THE CIRCLE'S HAAR ENSEMBLE DOES NOT.**


## NEW URGENT SOURCE FRONT: PR #256 (ARRIVED DURING THIS ROUND)

A separately running research branch opened
https://github.com/femboy2112/SUCC/pull/256
at last observed head 66fcb6f61b2851371bfe58ba6db74bdeacb46ef0.
It is stacked on GREENPRINT #254, not on #253/#257.
Its mathematics appears more directly relevant to actual π
cancellation than generic origin sampling. AUDIT FIRST, DO NOT
SILENTLY IMPORT IT.

For genuine source prime p=8m+1, the first p-pole
birth in the BBP rational forcing is at n=m+1,
and the next p-input does not arrive until 4m+1.
On this authenticated length-3m interval, the
p-primary state is 4*16^t/p, with order
L_p=ord_p(16) dividing m (p≡1 mod8).
The complement w_(p,t) has denominator coprime
to p, and the FULL source state is
  y_(m+1+t)=4*16^t/p+w_(p,t) mod1.

The research imports PNT in 1 mod8 and the
Bourgain–Glibichuk–Konyagin subgroup bound
to obtain power-saving p-LOCAL character
cancellation for almost all such primes.
That is real imported analytic machinery;
it does NOT bound the full π-selected phase.

The missing source-specific twisted term is
  I_p(h)=(1/(3m))*sum_(block,s)
     e(4h*16^s/p)*
     [e(h*w_(p,block*L_p+s))
      -e(h*w_(p,block*L_p))].
PR #256 records that base16 π normality is
equivalent to vanishing of I_p(h) for all
fixed h along the authenticated good-prime
family, after subtracting a local subgroup
sum which is already controlled. The
I_p convergence is OPEN.

**NEW GEOMETRIC CROSS-POLLINATION TARGET:**
The p-primary phase a_p=4/p has
H_(L_p)(a_p)=4(16^L_p-1)/p=0 mod1.
This is an EXACT periodic-origin covariance
defect of zero. Consequently, after a complete
p-clock return, the FULL state displacement
comes entirely from the complement:
  y_(t+L_p)-y_t
    =w_(p,t+L_p)-w_(p,t) mod1
within the authentic source-free window.

Formalize this source-typed **local closed
gauge / global residual connection**.
It is not a proof that its Fourier average
vanishes, since I_p measures complement
variation WITHIN each p period as well as
between periods. Attack the signed twisted
interference directly:
- derive exactly how the genuine BBP r(n)
  drives w_(p,t) inside the p-free interval;
- test whether the complement is smooth,
  low-bandwidth, or has source-certified
  cancellation on the multiplicative
  subgroup periods;
- establish a correct twisted-subgroup
  character sum estimate WITH ACTUAL WEIGHTS.
  BGK unweighted local cancellation does not
  automatically give a weighted sum bound;
- retain all cross-prime CRT interactions
  and p² Witt return/higher carrying from
  CBCW-08/09; do not apply a Q/Z
  fractional-part map before prime-primary
  decomposition.

Mandatory negative controls: nonnormal
coprime-denominator rational source clocks,
full-period exceptional x_d=1/(16^d−1),
rational BBP fake Green sources, genuine p²
valuation onset, and pointwise/ensemble
Galois mismatch.

**HIGHER PRIORITY THAN INVENTING MORE
GENERIC ORIGIN AVERAGES:** prove an actual
nonzero source-specific signed I_p bound
or a rigorous obstruction to a proposed
weighted-BGK/partial-summation mechanism.
If you cannot prove decay, produce the
sharpest authenticated unconditional bound
and isolate the one missing complementary
source estimate with falsifiers.

Recheck #256's hosted CI; when inspected
its dedicated focused checks passed but
some full-repository jobs were still running.
Its paper claims are not Lean facts.
