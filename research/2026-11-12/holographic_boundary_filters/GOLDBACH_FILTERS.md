# Goldbach boundary filters: certify the target without reconstructing the whole interior

**2026-11-12.** Paper proofs and exact finite controls; no external mathematical
referee or formal proof checker. Binary Goldbach remains **OPEN**. The polynomial
and separation principles are classical finite linear algebra/optimization;
the contribution is their explicit, source-audited interface to this SUCC
grade carrier, with a useful coarse certificate and falsifiable limitations.

## 1. Live source and novelty boundary

This work starts from Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.
The fuller, unmerged donor snapshots were inspected, not merged or edited:

- [PR 600, `dbc7fed1`, grade cylinder](https://github.com/femboy2112/SUCC/blob/dbc7fed19189016f6ab27550f3e84940b632b09b/research/2026-11-12/prime_fixedpoint_cylinder/THEOREMS.md):
  the zero-grade projector, the exact angular average, finite-angle aliasing,
  and the pure-gradient twist obstruction already exist.
- [PR 600, signed sieve](https://github.com/femboy2112/SUCC/blob/dbc7fed19189016f6ab27550f3e84940b632b09b/research/2026-11-12/signed_sieve_coupling/THEOREMS.md):
  polarization gives a genuine lower operator, while its source-selected
  pointwise positivity remains open.
- [CRT–Haar legacy certificate](https://github.com/femboy2112/SUCC/blob/dbc7fed19189016f6ab27550f3e84940b632b09b/research/2026-11-12/prime_interferometer_legacy/RESEARCH_NOTE.md):
  sharp elementary cellwise intersection bounds and refinement monotonicity
  are prior work, not new claims here.
- [PR 600, wave limits](https://github.com/femboy2112/SUCC/blob/dbc7fed19189016f6ab27550f3e84940b632b09b/research/2026-11-12/wave_resonance/THEOREMS.md)
  and [support-edge counterexample](https://github.com/femboy2112/SUCC/blob/dbc7fed19189016f6ab27550f3e84940b632b09b/research/2026-11-12/wave_resonance/BOUNDARY_NO_GO.md)
  already separate positive coarse average from every-target positivity.
- [PR 601, prime waves](https://github.com/femboy2112/SUCC/blob/774191e7679cd63c56bdb105541ce21c8ee27448/research/2026-11-12/prime_fixed_point_observer/PRIME_WAVES.md)
  already uses a phase-loss/homometric control. Section 6 below gives a
  different, factorized exact witness for the same necessary distinction.

The existing `observational_succ/no_ghost.py` contains a rational Farkas
feasibility/certificate implementation for another finite observation model.
Its general separation principle is not claimed anew. The new question is
whether a *small set of authenticated arithmetic boundary responses* already
excludes every zero-ground-sector completion. This can be weaker than full
reconstruction and admits a complete finite answer for a declared relaxation.

## 2. Hole contract

| Item | Precise statement |
|---|---|
| Object | A finite nonnegative grade histogram `c=(c_0,...,c_L)` and declared linear boundary filters |
| Target | Certify `c_0>0` from the observed filter responses, without reading `c_0` or reconstructing every `c_j` |
| Arithmetic specialization | `c_j=#{d:0<=d<=n-2, Omega(n+d)+Omega(n-d)-2=j}`; then `c_0=G(n)` is the unordered Goldbach count |
| Finite theorem | The response excludes every nonnegative real completion with `c_0=0` iff a signed combination of the filters is a positive certificate of the form below |
| Status | **PROVED LOCAL**, using classical finite-dimensional separation; exact finite implementation controls **VERIFIED FINITE** |
| Proof leverage | Certifies the desired property from a target-adapted dual filter; need not identify the full histogram |
| Novelty tax | An application/certificate interface, not a new separation theorem or an asymptotic number-theory estimate |
| Cheapest falsifier | A no-ground histogram sharing the measured responses; or a combined filter positive at a forbidden grade |
| Arithmetic gap | Uniform, independently derived moment/filter estimates and a controlled error budget that keep a positive margin for every sufficiently large midpoint |
| Boundary | Completeness concerns nonnegative **real** histograms on the declared finite support, not integer histograms, genuine-prime realizability, or unbounded horizons |

## 3. GBF-01 — target-specific dual boundary certificate

**PROVED LOCAL.** Let `c_j>=0`, `0<=j<=L`. Choose real filters `f_i(j)`,
`0<=i<=m`, with `f_0(j)=1`, and let

\[
y_i=\sum_{j=0}^{L}f_i(j)c_j.
\]

Suppose coefficients `lambda_i` form the combined filter

\[
q(j)=\sum_i\lambda_i f_i(j),\qquad
q(0)=1,\qquad q(j)\le0\quad(1\le j\le L).
\]

Then the boundary alone certifies

\[
\boxed{c_0\ \ge\ \sum_i\lambda_i y_i.}
\]

**Proof.** Interchange two finite sums. The right side equals
`sum_j q(j)c_j`, which is at most `c_0` by nonnegativity and the declared
signs. If the margin is positive and the true counts are integers, `c_0>=1`.
The coefficients may be signed even though the unknown histogram is nonnegative.

**Exact finite completeness.** Assume at least one nonnegative histogram
on `0,...,L` realizes the observations. A positive certificate exists exactly
when there is no nonnegative real histogram supported on `1,...,L` with
those same observations.

To prove this, let `v_j=(f_i(j))_i`. A zero-ground completion exists iff
`y` belongs to the finitely generated cone `cone(v_1,...,v_L)`. If it does
not, finite-dimensional Farkas separation supplies `lambda` satisfying
`lambda.v_j<=0` for `j>=1` and `lambda.y>0`. Evaluating against any feasible
full histogram shows that `lambda.v_0>0`; otherwise every contribution is
nonpositive. Divide `lambda` by `lambda.v_0` to obtain the normalized filter
above. Conversely, a positive certificate is incompatible with any zero-ground
completion by the first inequality. For rational tables and data a rational
separating certificate can be chosen; its signs and margin can then be checked
with exact arithmetic.

This is the standard alternative for nonnegative linear equations, used in
a specific observable model. Primary reference: Boyd and Vandenberghe,
[*Convex Optimization*, authors' slides, sections 5.34–5.35](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
PDF pages 188–189. The theorem concerns finite polyhedral cones; no analogous
closedness or exact-duality claim is made for an infinite moment problem.

If a real zero-ground completion survives but no integer/source-realizable
one does, this relaxation can remain inconclusive. It does not manufacture
a genuine prime counterfeit from an arbitrary feasible histogram.

### GBF-02 — certified response uncertainty

**PROVED LOCAL.** If the true response satisfies `lo_i<=y_i<=hi_i`, the
same sign checks certify

\[
c_0\ge\sum_{\lambda_i\ge0}\lambda_i\,lo_i
       +\sum_{\lambda_i<0}\lambda_i\,hi_i.
\]

Each term is its minimum over the declared interval; summing proves the
formula. This is a sound sufficient bound, not an optimality assertion for
correlated response errors. With symmetric error radii `eps_i`, the paid
error is `sum_i |lambda_i| eps_i`. Small individual errors do not suffice
if the chosen filter has large coefficients.

## 4. GBF-03 — an authentic three-moment Goldbach certificate

For an integer midpoint `n>=2`, put

\[
h_n(d)=\Omega(n+d)+\Omega(n-d)-2,\qquad 0\le d\le n-2.
\]

Both endpoints are at least two. Thus `h_n(d)>=0`, and it vanishes exactly
when both endpoints are prime. Also `2^{Omega(k)}<=k`, so

\[
0\le h_n(d)\le L_n:=\lfloor\log_2(n^2)\rfloor-2.
\]

This ceiling is obtained before evaluating any grades. For `L=L_n>=1`,
the quadratic polynomial

\[
q_L(h)=\frac{(h-1)(h-L)}L
      =1-\frac{L+1}{L}h+\frac1Lh^2
\]

satisfies `q_L(0)=1` and `q_L(j)<=0` at every integer `1<=j<=L`.
Therefore, with `m_k=sum_d h_n(d)^k`,

\[
\boxed{G(n)\ge m_0-\frac{L+1}{L}m_1+\frac1L m_2.}
\]

For `L=0` every grade is zero and `G(n)=m_0`. This is a universal finite
inequality with an elementary proof; it need not be a positive lower bound.

At `n=10`, exact integer factorization gives `L=4` and

\[
(m_0,m_1,m_2)=(9,16,46),\qquad
9-\frac54(16)+\frac14(46)=\frac12>0.
\]

The response of the three boundary filters `1,h,h^2` certifies `G(10)>=1`.
An independently implemented trial-primality count gives `G(10)=2`, namely
the unordered pairs `(3,17)` and `(7,13)`. The certificate never reads the
zero-grade count as an input.

This is a **coarser certificate than full histogram reconstruction**. The
true histogram is `(2,2,3,0,2)`. After measuring only `1,h`, the zero-ground
histogram `(0,2,7,0,0)` remains possible: both responses are `(9,16)`.
The second moment distinguishes them, and the signed quadratic excludes
*every* nonnegative zero-ground histogram on `1,...,4`, not just this one.

Computing these moments by factoring every endpoint is not claimed faster
than finding a Goldbach pair. The analytic research question is whether such
responses can be bounded independently and cheaply while retaining a strict
margin. No all-midpoint moment estimate is obtained here.

**Support-authentication mutation.** If a dishonest packet declares `L=3`
while keeping the actual moments `(9,16,46)`, the formally admissible filter
`q_3` returns the false bound `G(10)>=3`. The actual grade four lies outside
that counterfeit packet. An algebraic verifier cannot infer omitted source
support. `prime_grade_data` computes the a priori correct support ceiling;
the mutation is retained as a regression test and an explicit trust boundary.

## 5. GBF-04 — any fixed moment depth can hide the zero sector

**PROVED LOCAL, source-blind obstruction.** For every integer `d>=0`, set
`r=d+1` and define two integer histograms on `0,...,r` by

\[
c_j^+=\begin{cases}\binom rj&j\text{ even},\\0&j\text{ odd},\end{cases}
\qquad
c_j^-=\begin{cases}0&j\text{ even},\\\binom rj&j\text{ odd}.\end{cases}
\]

They have the same moments of every order `0<=k<=d`, but
`c_0^+=1` and `c_0^-=0`.

**Proof.** Their moment difference is
`sum_{j=0}^r (-1)^j binom(r,j) j^k`, the `r`th finite difference of a
polynomial of degree less than `r`, hence zero. For the next moment its
absolute value is `r!`, so the control is nondegenerate. At `d=2` the two
histograms are `(1,0,3,0)` and `(0,3,0,1)`, with identical data `(4,6,12)`.

Thus more precision in the same finite list of moments cannot resolve this
particular ambiguity. A new filter is needed. The obstruction applies to
arbitrary nonnegative finite grade models; these histograms have not been
realized by genuine integer midpoint grades. It refutes a source-blind
reconstruction implication and does not refute a theorem exploiting additional
full-prime arithmetic.

For a *known* finite ceiling `L`, all moments through `L` do recover the
histogram. In particular `prod_{j=1}^L(1-h/j)` is exactly one at grade zero
and zero elsewhere. Its boundary evaluation equals `G(n)`. This finite
interpolation is a reconstruction identity, not new asymptotic leverage.

## 6. GBF-05 — magnitude data can lose the target at every frequency

**PROVED LOCAL countercontrol.** Put `X={0,1,4}`, `Y={0,10,25}`, and

\[
A=X+Y=\{0,1,4,10,11,14,25,26,29\},
\quad
B=X+(25-Y)=\{0,1,4,15,16,19,25,26,29\}.
\]

All sums defining each set are distinct. For source polynomials,
`P_A(z)=P_X(z)P_Y(z)` and `P_B(z)=P_X(z)z^{25}P_Y(z^{-1})`.
On `|z|=1`, their squared magnitudes agree. Equivalently, their exact
ordered difference histograms agree at every lag. They also have the same
cardinality and the same anchored endpoints zero and 29.

Nevertheless the ordered coefficient of sum ten is two for `A` and zero
for `B`. Full power spectra reconstruct autocorrelation, whereas an additive
sum coefficient uses the *phase-sensitive square* `P(z)^2`, not `|P(z)|^2`.
No additional precision or frequency samples of those power data fix this
ambiguity. These sets are explicit nonprime controls, not claims about the
actual prime source. The broader phase-loss mechanism is classical and was
already present in donor PR 601; this factorized control is independently
checkable with integer counts.

## 7. GBF-06 — a circular answer must pay the wrap aliases

For a finite integer source `S` and ordinary ordered coefficients
`r(t)=#{a,b in S:a+b=t}`, a modulus-`M` Fourier reconstruction returns

\[
r_M(t)=\sum_{k\in\mathbb Z}r(t+kM).
\]

**Proof.** The finite character average is one exactly when
`a+b=t (mod M)`; group those pairs by their ordinary sum. If
`S subset {0,...,X}`, taking `M>2X` makes this agree with `r(t)` for every
`0<=t<=2X`. A smaller modulus requires an explicit no-alias argument.

For the genuine complete prime source through eight, `S={2,3,5,7}`,
ordinary `r(8)=2`. Modulus four returns five, adding `(2,2)` at sum four
and `(5,7),(7,5)` at sum twelve. Modulus fifteen recovers all coefficients
of this source, whose maximum endpoint is seven. Congruence-class admissibility
is a different observation contract from ordinary Goldbach existence.

## 8. Order, execution, and remaining obligation

Every scalar grade filter `f(H)` commutes with every other `g(H)`. Ordering
or repeatedly twisting this same commuting family creates no new boundary
data. To reveal additional positional coupling, a candidate must declare
another arithmetic operation and its noncommuting action; the existing
additive/multiplicative donor work supplies examples. Noncommutation alone
still does not prove a positive zero-grade mass.

The exact verifier checks filter signs, normalization, rational arithmetic,
and interval-error payment. Its source attribution string is metadata;
arbitrary external packets require separately authenticated responses and
support. The local arithmetic builder uses explicit trial factorization of
every finite endpoint, and a separate trial-primality route checks counts.

Executed locally:

```sh
python -W error -m unittest -v test_goldbach_filters.py
python goldbach_filters.py
```

The focused suite passed **14 tests**, including exact finite interpolation
against direct primality for every `2<=n<=128`, all `0/1/2` histograms through
grade four for the quadratic inequality, binomial controls through moment
degree twelve, deliberately invalid filter signs, interval error, support
forgery, and power/circle aliases. The midpoint-ten discovery was exploratory;
it is not described as a preregistered holdout. These tests verify the finite
implementations and mutations, not the infinite Goldbach claim.

**Next verdict-changing probe.** Specify a filter family and its support
bound before examining the target count. Derive its response bounds from
genuine multiplicative/additive source information, optimize a rational
dual certificate, then test the signed margin on new arithmetic windows
and on surviving moment/phase/support mutants. If the analytic error exceeds
the margin or a valid zero-ground completion remains, report that exact gap.
No conversion from finite certificate success to an all-large-`n` theorem
is supplied by the boundary formalism itself.
