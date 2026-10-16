# Arithmetic Resonance: independent hostile audit

**Verdict: the checked source bounds and finite contracts survive, conditional on
their stated analytic premises. Original Suzuki four-low sign OPEN; RH NOT
PROVED.** Two implementation defects were found, notified, repaired by their
owner, and retained. Automatic contraction of the derivative of a projected
operator is refuted by an exact counterexample. The source-specific dense
range theorem survives independent paper review under its stated inherited
coercivity hypothesis; a finite numerical rank is never a range proof.

The auditor owns only `scripts/arithmetic_resonance_independent_audit.py`, this
review, and `arithmetic_resonance_receipts/audit*`. No producer file, archive,
Git index, commit, full test suite, or Lean compilation was changed or executed
by this auditor. Other workers and the principal wrote concurrently.

## Source, carrier, and authority

The initial clean branch was
`research/arithmetic-wavefront-spectral-response-2026-10-16`, at
`24d0f18a103fb2add32ee817fdfefb4ff401ed27`. Principal integration subsequently
advanced HEAD; each executable receipt records its actual HEAD and inspected
module hashes. The primary source file is
`observational_succ/source_weil_hierarchy.py`, blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, SHA256
`183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.
The audit compared its bytes with originating commit
`dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`, and checked unchanged bytes at the
end. The founding import manifest is a distinct provenance family.

The first-window carrier is complex mean-zero Lebesgue L2 on (-1/2,1/2).
Write l_n(t)=P_n(2t), P for modes 1,...,4, Q=1-P, A=PGP, b=QGP, D=QGQ,
and K=V*V with Vu(t)=integral from -1/2 to t of u. The form-coordinate metric
is W=diag(1/3,1/5,1/7,1/9). Actual source range and coercivity
D >= (20699/1000000) K_Q are inherited paper premises, not newly Lean-checked
by this audit. All inverse powers require their actual domains. No nontrivial
zero coordinates, fabricated source channel, or replacement positive source
enters the audit.

Read independently: AGENTS.md, METHOD.md, the manifest, the compactness/source
dossiers, pinned source and original commit, and subsequently all six landed
modules and their source/range/spectral/geometry/transport contracts. Primary
challenges were constructed before reading the new implementations. The
arithmetic source is shared; algorithm diversity is not independent source
provenance or a second blind reasoner.

## HA-01: derivative projection contraction is false in general

**PAPER PROOF, exact executable witness.** Let f=l_6-l_4/2 and G=f tensor f.
This is a positive, smooth, mean-zero, rank-one operator. With the actual P,
Qf=l_6. Exact polynomial integration gives

```
||f||² = 49/468,       ||f'||² = 54,
||l_6||² = 1/13,      ||l_6'||² = 84,
||partial G||HS² = 147/26,
||partial(QGQ)||HS² = 84/13 = (8/7)(147/26).
```

Thus neither smoothness, positivity, compactness, nor this specific four-low
projection licenses the disputed contraction. This is a mathematical synthetic
witness, **not a negative statement about the actual Suzuki operator**.

The valid statement is ||Q(partial G)Q||HS <= ||partial G||HS. Weighted
Legendre derivative contraction also survives: integration against
(1/4-t²) diagonalizes the derivative energy. The existing compact-compression
proof using that weighted energy is not refuted. The quotient response uses
Pi_M(partial G), with M orthogonal to degrees 0,...,3, and is safe when that
projection is applied **after** differentiation.

The geometry module keeps both projection orders explicit. Its first-prime
result is separately proved, rather than inferred from the false general
principle. I independently expanded the full two-variable kernel of
partial(R T_b R), R removing degrees 0,...,4, at the rational reference b.
Exact integration of its polynomial correction over nine rectangles and its
step-kernel cross terms over two corner triangles agrees with the producer's
adjoint/finite-rank HS calculation. This is a different calculation path.

For the true b=log 2, the transfer uses
||partial(T_b-T_b0)||HS² <= 2 L eta, ||T_b-T_b0||HS² <= L² eta²,
||partial P||op² <= sum n(n+1)(2n+1)/(2a²), and the complete resulting
4 L eta + 2 S L² eta² error. The actual source weight is enclosed, not replaced
by the reference weight. The resulting squared norm is strictly below one
fifth of the mean-zero isolated-prime derivative HS square. This result has
no trial-vector normalization assumption. It concerns **only prime 2**;
signed cross-channel cancellation blocks its automatic transfer to full G.

## HA-02: finite-source certificate laundering, repaired

**REFUTED initial API behavior; regression now rejected.** Initially,
`arithmetic_resolvent.shifted_certificate` accepted a caller-provided `upper`
after checking only candidate digest and Gamma count. A valid zero-U degree-10
record, a matching digest/J, zero V/U Grams, and H_lower=H_upper=1000 I were
accepted. At shift 1 the routine returned lower diagonals about 999.69 and
999.86 under its authentic-source status label. Those were fabricated bounds.

The owner removed the public `upper` parameter and now reconstructs the
source certificate internally. The audit's exact exploit call is rejected.
`audit-trust-boundary-failure.json` preserves the owner's execution of the
independently reported flaw and its original output. The defect remains part
of the history; a later successful run does not relabel that failure.

A subsequent runtime guard initially rejected healthy source execution by
mistaking a module-level `<genexpr>` for a named function binding. The failing
audit is retained in `audit-pre-fix.json`. The owner restricted that comparison
to named bindings. Current healthy source calls pass. This is an integrity
guard, not a sandbox or proof of mathematical source correctness.

## HA-03: genuine improved lower bound survives

**CONDITIONAL PAPER PROOF plus exact receipt replay.** From the inherited
quotient and coercivity theorem,

```
R0 <= kappa^-1 (Pi_M partial G|P)*(Pi_M partial G|P)
   <= kappa^-1 (partial G|P)*(partial G|P).
```

There is no derivative of Q hidden in this argument. The BV budget
V_J=16+8 sum_{j<J}(4j+1)^-1 is valid. Independently: the pole variation is
8 sinh(1/2)<5; the contact coefficient is <8; the two genuine prime atoms
have total mass 2 log2/sqrt2<2. These total less than 15<16. A Gamma rung
has second distributional derivative exp(-d|r|/2)-(4/d)delta_0,
d=4j+1; its variation on the window is at most 8/d. All atoms and channels
are included.

For degrees 1,...,4, |P_k(z)|<=1 on [-1,1]. Direct polynomial factorizations
verify this without a loose coefficient-sum bound: for example
1-P4=5(1-z²)(7z²+1)/8 and 1+P4=(35z^4-30z²+11)/8>0.
Convolution with the finite signed measure therefore gives each derivative
column Lipschitz constant V_J. On a full cell of width h, a point enclosure
with absolute cap m gives exactly

```
integral (m+V_J|x-mid|)^2 dx = h m² + m V_J h²/2 + V_J² h³/12.
```

Reflection reuse doubles **all three** contributions. All stored midpoint,
linear-error and quadratic-error sums were recomputed with rational arithmetic.
Twelve source point intervals, spanning center, intermediate and endpoint
cells for all four columns, were checked by an independent displacement
substitution and scalar exponential-moment integration. That route shares
the pinned contact interval but does not call the producer's point evaluator,
polynomial antiderivatives, Legendre generation or source matrix helper.
Interval agreement is a consistency check; the continuous bound follows from
the BV proof, not those twelve points alone.

Normalized sector columns carry factors 2k+1. Their squared HS norm bounds
their squared operator norm. The entire omitted Gamma derivative has
operator norm at most eta_J=2/(4J+1)+8/(4J+1)². Thus adding eta_J once to the
finite operator norm is valid; an artificial square-root-of-dimension factor
is unnecessary. Squaring and dividing by kappa gives the verified J20/grid512
caps approximately 0.45490754 (odd) and 0.84814685 (even), below the inherited
75625/20699. With the separately enclosed low A these are genuine lower
bounds for S0, still negative. A later grid refinement must have its own
receipt; these numbers identify the audited initial receipt precisely.

## HA-04: best frozen upper independently reconstructed

The full degree-20/J512 candidate has six distinct same-parity entries.
All six were recomputed from the prior auditor's shifted Rodrigues and
incomplete-gamma definitions, with independent constants and intervals,
without producer source integration helpers. Each independent interval is
contained in the recorded truncated-source interval. The frozen candidate
digest, exact V Gram, complete tau_J V Gram correction, both row radii, and
both metric-aware 2x2 PSD cap slacks were then checked independently.

The resulting upper caps survive:

| Sector | Exact upper cap for S0 | Decimal display |
|---|---|---|
| Odd | 300761/1073741824 | 0.000280105509 |
| Even | 11742983/8589934592 | 0.001367063145 |

These are upper bounds, not positivity certificates. The finite-response
direction is also falsified adversarially: D=[[2,1],[1,2]], b=(1,0), A=3/5
has one-coordinate response 1/2 and full response 2/3. Its finite short is
+1/10 while its true short is -1/15. Inverse-square-root range also does not
imply an inverse solution: D_n=n^-4 and b_n=n^-3 have D^-1/2 b=(1/n) in l2
but D^-1 b=(n) outside l2.

`audit-source-cap-replay.json` separately passes the inherited source-cap
replay (23 source pairings). That and the degree-20 reconstruction use the
**same Rodrigues audit lineage** and count as one algorithmic family.
The primitive-overlap hinge checks and displacement-moment derivative checks
are distinct representations, but all retain the same arithmetic source.

## HA-05: spectral, radius, boundary and debt checks

The spectral module was challenged in a rationally rotated basis: direct
dense Schur inversion agrees exactly with its matrix measure response.
Regularization bias and trial-completion error are distinct and correctly
oriented. Full PSD atom checks reject positive diagonals with an indefinite
cross term; coupled zero atoms are not silently pseudoinverted. Matched finite
moments and soft modes retain unbounded/uncontrolled inverse response.
The Stieltjes endpoint term, whole-matrix fractional bounds and slow-tail
controls survive within their declared finite/conditional scopes.

Independent primitive overlaps verify true source hinge intervals through
radius 1, including the prime-square coefficient log2/2. Fake composite 6,
wrong types, missing half density and unsupported source radii are refused.
Distribution pairings retain zero-extension endpoint delta and delta-prime
terms. Whole-line Fourier multipliers are not finite-window eigenvalues.

For U_a f(t)=sqrt(2a) f(2at), direct change of variables gives transported
kernel 2a g(2a(t-s)), physical forms divided by 2a, and K scaling (2a)^2.
Exact polynomial-kernel controls test all three factors at multiple radii.
The radius continuity budget uses the uniform O(J^-1) kernel tail, whereas
the full 4x4 source bracket uses the positive O(J^-2) mean-zero operator tail.
Both complete matrices and their off-diagonals are retained. No high
coercivity is transferred away from a=1/2.

The narrow tail packet passed canonical rehash attacks on status, matrices,
global conclusion, obligations, source epoch, radius, metric, signed channels
and derivative-tail substitution. Removing an inherited transitive ASSUME
obligation is rejected. Valid packets retain the original transitive source
debt and issue no semantic authority. Hash-valid false prose remains possible
by design and is explicitly tested to receive **no proof authority**.

## HA-06: actual-source range proof survives the endpoint challenge

The exact source-range controls check primitive endpoints and moments,
Gamma multiplier tail constants, and a boundary mutant that violates the
integration-by-parts identity. The landed `FRACTIONAL_SOURCE_RANGE_AUDIT.md`,
SR-01 through SR-06, was read in full. Its density result is **ACCEPTED AS
CONDITIONAL PAPER PROOF**, on the authentic Gamma identity, bounded signed
remainder and inherited D>=kappa K_Q. No formal kernel claim is made. These
are the load-bearing independent checks of the argument:

1. With T equal to convolution by the real odd g', Fubini gives T*=-T and
   R_Q*=-QT on M=E3-perp. An annihilator f is only initially in L2 and
   satisfies Tf=p in E4. One cannot assume H01 traces for f. The dossier
   states and respects this distinction.
2. The Gamma multiplier is exactly m(xi)=sum 16xi²/[d(d²+4xi²)], d=4j+1.
   The tail bound and logarithmic growth are correct, so q=m(D_R)Ef lies
   in H^(-1/4)(R) for every L2 input. This is a multiplier on a
   zero-extended primitive, not a spectral eigenvalue of compressed D.
3. Outside the interval, h(r)=exp(-r/2)/(1-exp(-2r))<=3/(2r). Indeed
   1/(1-exp(-2r))<=1+1/(2r), and r exp(-r/2)<=2/e<1. The Carleman
   Schur weight t^(-1/2) gives norm <=pi. The two disjoint exterior halves
   have combined norm <=3pi/sqrt(2)<7. Convergence on compact exterior
   sets identifies the actual distribution without a boundary condition.
4. Patch an assumed interior L2 representative with that exterior L2
   representative. The difference is supported at the endpoints and
   belongs to H^(-1/4). Every nonzero point-supported distribution is a
   finite combination of delta derivatives and fails this Sobolev condition;
   localization separates the endpoints. The difference is zero, proving
   m(D_R)Ef globally L2 and f in the logarithmic form domain X. Merely
   invoking a Friedrichs extension would not have closed this domain gap.
5. For 1/2<c<1, c²m(xi)<=m(c xi)<=m(xi), term by term. Dilation is
   uniformly bounded in the weighted Fourier norm and converges strongly by
   density. Shrinking support and mollifying preserve moments through degree
   three and supply a smooth compactly supported form core in X intersect M.
   No operator-core or H2 graph-density assertion is needed.
6. The source identity s[f]=<Gf',f'> and inherited coercivity apply first
   to that core, then extend by form continuity. For an annihilator,
   m(D_R)Ef|I=-p'-Bf is L2. The endpoint lemma applies, and
   s[f]=<-p',f>=0 because p' is in E3. Coercivity forces f=0. Thus
   ker R_Q*=0 and closure(Ran R_Q)=M. Bounded-map polynomial density gives
   arbitrarily small relative residuals over high polynomial trials.

This is an existence/density statement, not attainment, a coefficient bound,
a modulus, or convergence of the energy-Galerkin iteration. Generic relative
coercivity and compactness alone still cannot establish it: the inherited
clamped-biharmonic countermodel has different endpoint structure and remains
valid. So does the inherited example with dense range and unsuccessful
energy-Galerkin residual convergence.

SR-05's source-specific rejection of D<=C K_Q also survives. Modulated compact
smooth primitives, corrected by four fixed smooth moment functions, remain
admissible; their corrections decay rapidly. Each fixed Gamma partial
multiplier tends at high frequency to sum 4/d. The full positive Gamma form
dominates it, while the signed remainder is bounded. Choose the finite Gamma
count first and frequency second; the Rayleigh ratio becomes arbitrarily
large. There is no uncontrolled infinite-limit exchange or negative Weil
direction asserted.

SR-06's dyadic fractional premise remains unproved. Its conditional arithmetic
is correct: mass <=C*64^-j on (0,16^-j] bounds the 5/4 inverse moment on each
band by 32^(j+1)C*64^-j, summing to 64C; the part above 1 is bounded by
||b||². Density by itself supplies none of these mass inequalities.

Fractional D-power membership above one-half, a quantitative inverse-tail
modulus, a useful high-trial relative-residual bound and the original S0 sign
remain separate obligations. No numerical singular value discharges them.

## Reproduction and evidence limits

Run only the independent audit, serially:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 -B scripts/arithmetic_resonance_independent_audit.py --replay-upper \
  --output research/2026-10-16/arithmetic_resonance_receipts/audit-final.json
```

The script enforces 768 MiB address space, 180 CPU seconds and 240 wall
seconds. The first complete upper replay passed 257 checks in 19.57 seconds;
the subsequently added direct two-variable projection checks have their own
passing receipt and are included in the final replay. Final frozen counts,
hashes and timing are authoritative in the final receipt. The paper-review
record is separately identified; a file hash never certifies that proof.
No full suite, compiler, fresh formal kernel or CI is claimed.

The audit's contact is actual bytes, exact source intervals and executed
counterexamples (kappa/contact); the surviving claims are limited to those
probes and supplied derivations (phi). Shared source and Rodrigues lineage
are retained explicitly (sigma); principal suggestions and worker repairs
are not counted as independent proofs (rho). The remaining useful probe is
an authenticated quantitative source-tail or relative-residual theorem that
narrows the still sign-indefinite bracket.
