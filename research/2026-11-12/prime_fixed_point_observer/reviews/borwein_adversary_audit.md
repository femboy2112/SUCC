# Adversarial audit: Borwein filters and an arithmetic ratchet

Date: 2026-11-12. Baseline: `e855200a9a447933ef93b3ee0947d14d00ef42de`.

This is a mathematical construction audit with an independently implemented
geometric calibration probe. It does not certify a new global prime-distribution
theorem. The audit distinguishes a symmetric random walk, a rectified walk, a
deterministic support counter, and a spectral filter: their notions of progress
are different.

## Verdict and load-bearing hypotheses

Two proposed constructions are valid within explicit boundaries:

1. Independent uniform increments become an almost surely unbounded ratchet
   after their negative parts are discarded **exactly when their positive
   half-widths have divergent sum**. Independence, deterministic widths, and
   rectification are load-bearing hypotheses.
2. A finite Borwein window with positive widths of total at most one, evaluated
   on the integer charge `Omega(n)-1`, is exactly the prime projection plus half
   the semiprime projection on positive integers `n >= 2`. Repeating this fixed
   filter converges in operator norm at the exact rate `2^-r`.

Neither result obtains primality from a width sequence alone. The arithmetic
charge already contains the prime distinction. A probability law described by
finite code also differs from an exact continuous sample path represented by
finitely many rational registers.

## 1. Rectification theorem: proof audit

Let `(a_j)` be a **fixed deterministic** sequence of positive real numbers. Let
the variables `U_j ~ Uniform[-a_j,a_j]` be **independent**. Define

\[
Y_j=\max(U_j,0),\qquad X_n=\sum_{j=1}^nY_j.
\]

Then

\[
\mathcal L(Y_j)=\tfrac12\delta_0+\tfrac12\operatorname{Uniform}[0,a_j],
\]

and, with the convention `sinc(0)=1`,

\[
\mathbb E e^{itY_j}
=\tfrac12+\tfrac12e^{ita_j/2}\operatorname{sinc}(ta_j/2).
\]

The exact moments are

\[
\mathbb EY_j=a_j/4,\qquad
\mathbb EY_j^2=a_j^2/6,\qquad
\operatorname{Var}(Y_j)=5a_j^2/48.
\]

### Disclosed statement

\[
X_n\longrightarrow+\infty\text{ almost surely}
\quad\Longleftrightarrow\quad
\sum_ja_j=+\infty.
\]

**Proof.** Fix `s>0`. Direct integration gives

\[
L_j(s):=\mathbb E e^{-sY_j}
=\tfrac12+\frac{1-e^{-sa_j}}{2sa_j}.
\]

On the event `Y_j >= a_j/2`, which has probability `1/4`,
`1-exp(-sY_j) >= 1-exp(-sa_j/2)`. Consequently

\[
1-L_j(s)\ge\tfrac14(1-e^{-sa_j/2})
\ge c_s\min(a_j,1),
\quad c_s=\tfrac14(1-e^{-s/2})>0.
\]

The second inequality follows from concavity on `0 <= a <= 1` and monotonicity
on `a >= 1`. If `sum a_j` diverges, so does `sum min(a_j,1)`. Independence now
gives

\[
\mathbb E e^{-sX_n}=\prod_{j\le n}L_j(s)
\le\exp\!\left(-c_s\sum_{j\le n}\min(a_j,1)\right)\longrightarrow0.
\]

Since `X_n` is nondecreasing, its limit exists as an extended nonnegative
random variable. Dominated convergence implies `E exp(-s X_infinity)=0`, with
`exp(-s infinity)=0`. Hence `X_infinity=infinity` almost surely. Conversely,
`X_n <= sum_j a_j` almost surely, so a finite width sum bounds every partial
sum. This proves both directions.

Every fixed finite threshold is therefore crossed in finitely many discrete
steps almost surely when the width sum diverges. This statement supplies no
uniform deterministic bound on a crossing time and no identification of the
step index with elapsed physical time.

### Mutation: remove independence

Take one variable `Z ~ Uniform[-1,1]` and set `U_j=a_j Z` for every `j`. Each
individual increment still has exactly the required uniform marginal. If
`sum a_j=infinity`, however,

\[
X_\infty=0\quad\text{on }\{Z\le0\},
\]

an event of probability `1/2`. Thus the marginal laws alone do not prove
unbounded progress. The factorization of Laplace transforms is the specific
proof step destroyed by this mutation.

### Useful stronger consequence for square-summable widths

If additionally `sum a_j^2 < infinity`, independence and the displayed variance
formula imply that

\[
X_n-\tfrac14\sum_{j\le n}a_j
\]

converges almost surely and in `L^2`. One justification is the martingale
convergence theorem: the centered partial sums form an `L^2`-bounded martingale.
For reciprocal odd widths the cumulative width diverges while the square sum
converges. The rectified position therefore grows with its deterministic mean,
up to a convergent random offset. The corresponding unrectified centered sum
converges instead. This identifies the actual change caused by rectification.

### Representation boundary

A finite formula specifies this transition law. Exact independent continuous
draws require a random-real or unbounded random-bit input model; a typical
complete real-valued trajectory does not fit in finitely many rational
registers. A deterministic algorithm can compute rational support sums, exact
finite-stage masses, or declared discrete approximations. These are useful
constructions with separate state semantics. They must not silently be called
exact samples of the continuum walk.

## 2. Integer-charge Borwein filter: proof audit

Let `m >= 1`, all `a_j > 0`, and `A=sum_j a_j <= 1`. Let the independent
uniform sum be `S=sum_j U_j`. Set

\[
B_{\boldsymbol a}(c)
=\mathbb P(|c+S|\le1)
=\frac2\pi\int_0^\infty
\operatorname{sinc}(x)\prod_{j=1}^m\operatorname{sinc}(a_jx)
\cos(cx)\,dx.
\]

The sinc integrand is absolutely integrable because `m >= 1` and the widths
are positive. The distribution of `S` is symmetric and atom-free, with support
`[-A,A]`. Hence, for **integer** `c`,

\[
B_{\boldsymbol a}(c)=
\begin{cases}
1,&c=0,\\
1/2,&|c|=1,\\
0,&|c|\ge2.
\end{cases}
\]

For `c=1`, the event is `-2 <= S <= 0`, exactly half the symmetric mass.
For `c=2`, the event can meet the support only at `S=-1` when `A=1`; that
single point has zero mass. Larger shifts are outside the support. These
arguments also justify the equality-boundary case `A=1`.

On `H=ell^2({2,3,...})`, let `C e_n=(Omega(n)-1)e_n`, with its usual weighted
domain, and let `P_k` project onto `Omega(n)=k`. Bounded spectral calculus gives

\[
T=B_{\boldsymbol a}(C)=P_1+\tfrac12P_2.
\]

It is a positive self-adjoint contraction on this Hilbert space. Its fixed
space is precisely the closed span of the prime basis vectors. For integers
`r >= 1`,

\[
T^r=P_1+2^{-r}P_2,\qquad
\|T^r-P_1\|=2^{-r}.
\]

The equality in the norm follows because the semiprime sector is nonempty.
The displayed formula for `T^r` excludes `r=0`, since `T^0=I` also contains
the higher-composite sectors. If the unit `n=1` is included in the carrier,
its charge is `-1` and its eigenvalue is `1/2`; it is not a fixed point of
this particular filter.

Positivity here is Hilbert-space operator positivity. Transporting the same
coefficient rule to the non-self-adjoint span of multiplication isometries
`V_m` does not by itself make it a positive or completely positive map of a
C-star algebra.

### Parameter controls and failure cases

| Change | Exact consequence |
| --- | --- |
| `m=0`, or all widths zero | The atom-free hypothesis fails. At `c=1`, a closed-window point mass gives `1`, whereas Fourier inversion of the interval gives half-weight `1/2`. |
| `A>1` | The raw central mass satisfies `B(0)<1`; primes cease to be fixed. |
| One width `a=3`, then normalize by `B(0)` | `B(0)=B(1)=B(2)=1/3`; normalization fixes charges `0,1,2`, including semiprimes and numbers with three prime factors. |
| Arbitrary real charges | The whole central plateau may contain nonzero charges. The exact fixed-space statement uses an integer spectral gap. |
| Raw `sinc(aC)` in place of the window mass | It need not be a positive operator: `a=3*pi/2` gives charge-one eigenvalue `-2/(3*pi)`. A nonnegative convolution density does not force all Fourier multipliers to be nonnegative. |

More generally, with a window radius `b>0`, the condition `A<=b` makes the
central mass one. If also `A+b<1`, every nonzero integer charge is excluded,
so the resulting operator is already the exact prime projection in one step.
This is spectral separation of the already encoded charge. It does not make
the width sequence an independent source of primality information.

## 3. Controls separating the competing ratchet claims

### Circular marginal versus lifted support

Take a circle of circumference `2`. A variable `U~Uniform[-1,1]`, reduced
modulo `2`, is uniform on the circle. Adding any independent circular
increment preserves this uniform law. In particular, for independent
`V~Uniform[-1/2,1/2]`, the circular distributions of `U` and `U+V` agree
exactly, while

\[
\mathbb P(|U|\le1)=1,\qquad
\mathbb P(|U+V|\le1)=7/8.
\]

The second probability follows from two triangular tails in the rectangle
`[-1,1] x [-1/2,1/2]`. A circular marginal can therefore be unchanged while
the line-support gate develops positive leakage. Winding or a lifted position
has to remain in the state if the observer is meant to detect that change.

### Endpoint occupancy versus survival

For independent `U_1,U_2~Uniform[-2,2]`,

\[
\mathbb P(|U_1+U_2|\le1)=7/16,
\]

but

\[
\mathbb P(|U_1|\le1,\ |U_1+U_2|\le1)=1/4.
\]

The endpoint probability is the area of one diagonal strip in a square.
Path survival intersects this strip with another strip `|U_1|<=1`. The
additional condition cannot be recovered by relabeling endpoint mass as a
first-passage or survival probability. Resetting after a crossing changes the
subsequent joint law and requires a declared fresh-increment protocol.

### Positive leakage at every stage versus infinitely many sampled clicks

At stage `k>=1`, choose two equal widths

\[
a_{k,1}=a_{k,2}=\frac{1+2^{-k}}2.
\]

Their support radius exceeds `1`. The exact two-corner area gives leakage

\[
\rho_k=\frac1{(2^k+1)^2}>0,
\qquad \rho_k\le4^{-k}.
\]

If each stage supplies at most one sampled click, `sum rho_k<infinity`.
The first Borel-Cantelli lemma implies that only finitely many clicks occur
almost surely; no independence between click events is needed for this
direction. A deterministic controller that clicks whenever it certifies
`rho_k>0` performs a different operation and can click at every stage.

### Growing support versus attenuation of a composite charge

Let `a_j=1/(2j+1)`, `j>=1`. The cumulative width diverges. Nevertheless the
growing sinc product evaluated at the composite charge `c=1` stays far from
zero. For `0<=x<=1/3`, the alternating Taylor estimate gives

\[
\operatorname{sinc}(x)\ge1-x^2/6.
\]

For finite products, `prod(1-b_j)>=1-sum b_j` when `0<=b_j<=1`. Also

\[
\frac1{(2j+1)^2}<\frac1{4j(j+1)},\qquad
\sum_{j=1}^m\frac1{4j(j+1)}=\frac{m}{4(m+1)}<\frac14.
\]

Therefore

\[
\prod_{j=1}^m\operatorname{sinc}(a_j)
\ge1-\frac16\sum_{j=1}^ma_j^2
>\frac{23}{24}.
\]

These positive partial products decrease to a limit at least `23/24`.
Appending infinitely many shrinking Borwein factors thus does not converge
to a prime projection, despite support crossing every finite threshold.
Repeating the **same fixed** filter `T` from Section 2 instead gives the
proved norm decay `2^-r`. These two iteration rules must not be interchanged.

The same odd reciprocal widths have finite square sum, so the original
centered random series converges almost surely and in `L^2`. Its pathwise
running maximum is finite almost surely. An unbounded sequence of support
radii is not a statement that a typical unrectified path travels to infinity.

## 4. Reproducible calibration and independence boundary

The script `../borwein_independent_audit.py` uses exact rational arithmetic.
Its primary two-dimensional oracle starts with a rectangle, clips it against
the required affine half-planes, and computes the resulting polygon area by
the shoelace formula. It does not use the legacy inclusion-exclusion CDF to
obtain that area. One-dimensional checks use direct interval lengths.

Positive, negative, and null geometry controls are whole, empty, half, and
quarter rectangles. The legacy Borwein CDF is then compared against this
geometric oracle across nonidentical widths, shifted windows, tiny widths,
and equality boundaries. Separate mutations remove independence, widen the
window law, discard winding, replace survival with endpoint occupancy, or
make click probabilities summable. The JSON includes exact raw control
values and check counts.

The initial inline calibration, before creating this script, checked 85
integer-charge cases through the legacy exact CDF, the broad-width mutation,
the circular line leak, the endpoint value, and 12 positive-leak stages.
Those checks shared the legacy CDF. The saved polygon implementation was
added specifically to reduce that dependency; its actual run result is
reported separately by the parent validation record. No Monte Carlo or
oscillatory numerical quadrature is used in either calibration.

The code is a finite check of the stated instances. The universal claims in
Sections 1-3 rest on their displayed derivations and hypotheses. Agreement
between agents or implementations is corroboration within those scopes,
not a replacement for the proofs.

The saved script was run on 2026-11-12 and returned `PASS`, with **382 exact
checks**. Of these, 77 compare the CDF against polygon clipping and 66 compare
it against direct interval lengths. The remaining checks cover the declared
calibration and mutation controls. The parent can reproduce the raw JSON with
`python research/2026-11-12/prime_fixed_point_observer/borwein_independent_audit.py`.

The pre-existing source family is
`research/2026-10-19/BORWEIN_DELTA_PRIME_CLOCK.md` and
`observational_succ/borwein_prime_clock.py`; its Borwein probability identity,
shallow-overflow formula, and warning about divergent support versus
convergent centered sample paths are earlier results. The charge-filter
specialization, rectification audit, and geometric countermodels above are
the scoped contribution of this audit, not a claim that the earlier Borwein
identity was newly established here.

## 5. Claim ledger and next discriminators

| Claim | Status and boundary |
| --- | --- |
| Rectified progress iff divergent width sum | Disclosed by the Laplace proof for fixed positive widths and independent uniform increments. |
| Same marginal laws suffice | Refuted by the common-uniform coupling, which stalls with probability `1/2`. |
| Integer-charge Borwein filter has exactly the prime fixed space | Disclosed on `ell^2(n>=2)` for finite positive widths with total at most one. |
| Broad-window renormalization preserves the fixed space | Refuted by the exact one-width `a=3` counterexample. |
| Circle marginal determines line leakage or winding | Refuted by the period-two uniform countermodel. |
| Endpoint Borwein mass equals path survival | Refuted by the exact values `7/16` and `1/4`. |
| Positive leak at every stage guarantees endless sampled clicks | Refuted by the summable-leak construction. |
| Divergent support radius forces charge attenuation | Refuted by the rational lower bound `23/24`. |
| Finite code for the law gives finite exact storage of all continuous sample states | Unsupported without a declared representation/oracle model. |

The next implementation discriminator is whether every API preserves these
separations: integer charge versus arbitrary phase; fixed-block repetition
versus appended widths; support/controller position versus sampled position;
and circular state versus its lift. The independent audit should be rerun
against any new production routines once they exist. This note does not
claim to have reviewed code that had not yet been written.

## 6. Production implementation review

The subsequently created `borwein_ratchet.py`, `test_borwein_ratchet.py`, and
`BORWEIN_RATCHET.md` were reviewed on 2026-11-12. This extends, rather than
retroactively changes, the construction audit above.

### Checks run and conclusions

An inline exact test compared the production APIs against the independent
polygon oracle in `borwein_independent_audit.py`. **692 checks passed**:
32 two-increment rectified CDF values, plus 165 configurations each checked
for the window value, Fourier-multiplier value, full-mass iff condition, and
zero-mass iff condition. The configurations include unequal widths, a width
of `1/100`, negative thresholds, the zero atom, shifted windows, several
window radii, and equality at support boundaries. The rectified oracle clips
each of the four sign quadrants by the relevant affine inequality for
`max(u,0)+max(v,0)`; it does not use the production mixture implementation.

Seven additional first-crossing comparisons passed: four two-dimensional
geometric examples and three three-increment examples against the existing
CDF. These include previous-radius equality, nonunit teeth, and nonuniform
widths. The 12 production unit tests then present all passed. This records
the actual finite scope of this review, not an independently re-proved test
suite or an exhaustive input search.

The anchored lift and its `d-1` offset are correct. The full support iff
statements use nonempty positive width banks and an atom-free law, exactly
the hypotheses required. The separate empty-bank probability/Fourier
interfaces preserve their distinct endpoint conventions. Operator positivity
and complete positivity are kept separate. The continuous random-state
representation is not identified with the finite rational support machine.

### Corrections requested and observed in the main note

The first reviewed draft had four documentation mismatches. Their corrected
forms were subsequently read and verified:

1. The unit has eigenvalue `1/2` under the extended filter. Fixing it requires
   `B(C)+(1/2)E_11`; adding `E_11` would instead give eigenvalue `3/2`.
2. The empty width bank is allowed by `window_mass` with closed-window
   semantics, and by `borwein_multiplier` with Fourier half endpoints; the
   text now describes this instead of saying the executable excludes it.
3. The mathematical lift also makes sense for circumference one, while the
   implementation chooses the nondegenerate domain `L>=2`. This restriction
   and the constant phase from using source address `n-1` are now explicit.
4. The proof of multiplier linear independence uses `e_1`. The note now
   explicitly returns to the original carrier `ell^2(n>=1)` for that proof.

The added maximal-inequality proof for convergence of independent centered
increments with summable variances was also checked. Its first-crossing
decomposition, summable tail-event estimate, and almost-sure Cauchy
conclusion are valid.

### Malformed public-summary receipts

The initial production constructors accepted algebraically impossible state
and certificate summaries. Two exact executed counterexamples were:

```python
ReleaseCertificate(1, 1, Q(1, 2), Q(1, 2), Q(1, 100)).deficit()
# returned Q(50), impossible for a probability

state = RatchetState(1, Q(1, 2), Q(1, 100), Q(1, 2), 0)
state = state.advance(Q(1, 2)).after
state.advance(Q(1, 2)).certificate(1).deficit()
# returned Q(25, 12), also impossible for a probability
```

The state docstring already disclaimed certification of an externally
fabricated history. The narrower defect was that these summaries are
algebraically impossible, yet the API presented their output as an exact
first-crossing leakage. A fix was requested with necessary feasibility
conditions and regression tests. For `m` positive widths with total `A` and
known attained minimum `l`, one necessarily has, when `m>=2`,

\[
l^{m-1}(A-(m-1)l)
\le\prod_j a_j
\le l\left(\frac{A-l}{m-1}\right)^{m-1}.
\]

For `m=1`, total, minimum, and product must all agree. For a release
certificate, its total is recoverable as `A=tooth+excess`. These checks
cannot establish the provenance or rational realizability of every possible
summary, but they reject the demonstrated impossible values. The repair's
verification status is recorded in the next subsection when reviewed.

### Repair verified

The subsequent implementation adds the necessary bounds in
`_validate_summary`, using exact integer cross-products, and calls this
validator from both public constructors. Singleton summaries require total,
attained minimum, and product to coincide. `deficit()` additionally rejects
a purported leakage outside the open probability interval `(0,1)`.

The repaired code and its new regression test were read. The targeted
regression test was rerun and passed. Direct replays of both original
witnesses now raise `BorweinRatchetError` during construction, with the
one-width consistency message. Four valid controls still return the exact
values `1/3`, `1/24`, `1/72`, and `1/96`; the last two attain the lower and
upper feasible products for `m=3`, `A=5/4`, and minimum `1/4`.

The cross-multiplications implement the displayed inequalities correctly,
and the bounds preserve real realizable summaries. They remain necessary
consistency conditions, not authentication of a supplied history or a
universal test for rational realizability. This limitation is stated in the
implementation. The demonstrated malformed-summary defect is **resolved**.
No unresolved blocking mathematical or implementation finding remains from
this focused audit; the source-specific prime-correlation question remains
open exactly as described in the main note.

## 7. Triadic transport extension: focused review

The later user steering about a first realized loop, a shared framework, and
the emergence of linear relations was reviewed in `TRIADIC_TRANSPORT.md` and
`triadic_probe.py`. **No blocking error was found in their stated scope.**

The minimum-length claim correctly excludes self-loops and parallel edges
and concerns a simple undirected graph. It is not presented as a theorem
that two-state dynamics are impossible or that linear algebra requires
three dimensions. The distinction between a declared scalar/coordinate
framework and additional order, measure, or inner-product structure is
correct. The cycle is a graph cycle; no conclusion about the homology of a
filled triangular face is asserted.

The twisted incidence matrix, determinant `H-1`, one-dimensional flat
kernel, and gauge covariance were checked algebraically. The note correctly
distinguishes the edge operator `B*B` from the vertex operator `BB*` and
distinguishes the smallest eigenvalue tending to zero from the first
nonzero eigenvalue at exact flatness. The probe's incidence matrix differs
from the displayed note matrix by a fixed cyclic row permutation. This
preserves its determinant and kernel and gives the corresponding row-gauge
convention. An explicit symbolic comparison of these two conventions was
run and passed.

The final note additionally states the unitary-phase identity
`A_inc=-diag(u_01,u_12,u_20) B*` and consequently
`A_inc* A_inc=BB*`. These identities were checked entry by entry and are
correct under the declared unit-modulus hypothesis. The note keeps vertex
values and edge currents distinct despite their equal coordinate dimension.

The prime-generator graph is bipartite by `Omega` parity. The displayed
square uses genuine prime edges, and a composite chord has flat transport
when it is defined by the existing composition. The adjoint remains a
partial inverse; replacing it by a global inverse is not assumed.

For `A_d=V_d* S^(d-1)`, the full Hilbert-space fixed-point statement is
valid, not merely a finite-basis observation. Its coefficient relation is
`(A_d x)_m=x_(1+d(m-1))`. A fixed vector has constant coefficients along
each infinite orbit `1+d^k(m-1)` for `m>=2`, forcing those coefficients to
vanish by square summability. Thus the fixed space is exactly `span{e_1}`
for every integer `d>=2`. The tail identity proves strong convergence to
`E_11`; the unit-vector witness `e_(1+d^r)` proves that norm convergence
fails. The all-`d` scope and `A_2 A_3=A_6` prevent a false claim that the
anchor itself singles out three or prime multipliers.

The relabeling `f=(5 7)` preserves the unit loops and, for `d=2,3`, the
full anchor fixed space and strong limit. Its adjoint index map
`m -> d f(m)-d+1` is injective, fixes one, and strictly increases every
`m>=2`; this suffices for the same tail argument. Nevertheless the source
braid gives the exact outputs `14` and `10` at input four. The direct versus
composed mixed route gives `19` and `13` at input three. The order
`(C_2 C_3)*=C_3* C_2*` is used correctly. The swap preserves `Omega`, so a
degree-only readout indeed misses this particular coupling defect.

A targeted executable replay passed: the symbolic row-convention and
determinant comparison, anchors and norm witnesses for `d=2,3,6`, four
composition inputs, and the saved counterfeit-receipt function. It returned
the exact pairs `(14,10)` and `(19,13)`. This audit did not repeat the broader
finite phase-bank or entire triadic probe campaign; those execution results
belong to the parent validation receipt. The universal conclusions above
are supported by the displayed algebra and tail proofs, not inferred from
the finite replay.
