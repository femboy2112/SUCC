# A stable target-relative boundary instrument

**PROVED LOCAL (paper):** one signed Fourier target admits factorially convergent
reconstruction from a single digit-character line coupled to centered future
moments. The coefficient norm stays bounded independently of moment order and
sample size. The order of the required number of power-moment channels is sharp
within this declared prefix bank. **No source-selected moment estimate, R0 or
normality is proved here.** This is a quantitative instrument, not new evidence
that its actual arithmetic response is small. Worldwide novelty is unverified.

The classical ingredients are Taylor's integral remainder, finite differences,
Hahn–Banach and the Riesz representation theorem. The SUCC predecessors are
RHY-10's signed digit/future Fourier lines, ZLHC-07's Pascal–Fourier observer,
and PR #605's target-ambiguity duality. The contribution is their target-specific
compression with an explicit stable inverse and matching channel-order lower
bound. It does not replace source acquisition by an oracle.

## TM-01. Compact target-ambiguity duality

Let X be a compact Hausdorff space, V a closed **real** linear subspace of C(X,R)
containing 1, and v a real continuous target. Then

\[
\sup_{\substack{p,q\in\mathcal P(X)\\
\int f\,dp=\int f\,dq\ (f\in V)}}
\left|\int v\,d(p-q)\right|
=2\inf_{f\in V}\|v-f\|_\infty. \tag{1}
\]

The upper bound follows because p-q annihilates V and has total variation at
most 2. For the reverse, Hahn–Banach gives a norm-one real functional on C(X)
annihilating V and evaluating v at its distance from V. Riesz represents it by
a real signed measure nu. Since 1 belongs to V, nu has total mass zero; its
Jordan parts each have mass 1/2. Thus p=2nu+ and q=2nu- attain the bound when the
distance is positive. The zero-distance case is immediate.

For a proposed finite response combination f=sum lambda_i f_i, errors bounded
by epsilon_i cost at most

\[
\|v-f\|_\infty+\sum_i|\lambda_i|\epsilon_i. \tag{2}
\]

For complex filters use their real and imaginary parts in (1), or use (2)
directly with complex error discs and the triangle inequality. Do not apply a
complex signed-measure dual as if it automatically produced two probabilities.

The admissible set matters. An exact forcing law plus exact literal U0=0
defines one trajectory by induction. There cannot be two different fully
authenticated trajectories with different R0 behavior. Ambiguity witnesses
below concern a specified **relaxed observation class**, not two solutions of
that singleton initial-value problem.

## TM-02. A single coupled line reconstructs one Weyl coefficient

Fix integer b>=2, nonzero integer h, and any probability law p on the compact
digit-cut carrier X={0,...,b-1} times [0,1]. Set

\[
z=(a+y)/b,\quad u=2y-1,\quad t=\pi h/b,
\quad M_j=\int e(ha/b)u^j\,dp(a,y).
\]

This carrier retains endpoint labels; its target e(hz) has compatible endpoint
values. Actual radix data use y in [0,1). The extra endpoint is useful for
compactness, and is not a newly realizable arithmetic measurement.

For every integer q>=1 define

\[
R_q=e(h/(2b))\sum_{j=0}^{q-1}\frac{(it)^j}{j!}M_j.
\]

Then, for **every** p and q,

\[
\boxed{\left|\int e(hz)\,dp-R_q\right|
\le\frac{|t|^q}{q!},\qquad
\sum_{j<q}\frac{|t|^j}{j!}\le e^{|t|}.} \tag{3}
\]

Proof: e(hz)=e(ha/b)e(h/(2b))exp(itu). Taylor's integral remainder on the real
segment from 0 to tu has modulus at most |tu|^q/q!, because every derivative
of exp(iv) has modulus one on the real line. Integrate, using |u|<=1. The
coefficient bound is the exponential series. Neither independence of a and y,
nor stationarity, nor any limiting distribution is used.

If the measured M_j have complex errors at most epsilon_j, add
sum_(j<q) |t|^j epsilon_j/j!. A common error epsilon costs at most
e^|t| epsilon, uniformly in q. For R0, b=16 and h=1, this norm is less than
61/50 and q=6 gives a truncation radius below 10^-7. This includes the complex
phase of every response. Magnitudes alone do not implement (3).

For an arbitrary fixed h one may block L actual digits, take b=16^L and
a=floor(bz), y={bz}. Choosing b>=16|h| gives the same norm <61/50. Acquiring
that longer leading block still has a cost. No change of the source is made.

### Why this differs from full Haar reconstruction

RHY-10 recovers the entire first-digit/future-word defect. ZLHC-07 bounds all
Lipschitz observables using all 15 digit modes and Bernstein polynomials.
Equation (3) instead requests one digit mode, q centered mixed moments, and
one specified smooth target. Its inverse need not reconstruct an exponentially
large conditional word table. It retains the **joining** of digit and future:
M_j is not the product of its two marginal means.

The first q monomials are finite linear combinations of degree-(q-1) Bernstein
polynomials, so these channels are available from the existing Pascal–Fourier
interface as well as by direct paired measurement. That change of basis can
amplify errors; the bound in (3) applies to the stated moment-error model, not
to arbitrary inaccurate Bernstein inputs without a further payment.

## TM-03. Finite banks leave an explicit residual, and the channel order is sharp

Fix 0<r<1 and q>=1, take a=0 and u_k=-r+2rk/q, k=0,...,q. Put mass
binom(q,k)/2^(q-1) on the even k for p+, and on the odd k for p-.
Both are probability laws, supported strictly inside one digit cylinder.
Finite differences annihilate every polynomial of degree less than q, so
their first q measured M_j are exactly equal. Nevertheless

\[
\int e(hz)\,d(p_+-p_-)
=2(-i)^q e(h/(2b))\sin(tr/q)^q. \tag{4}
\]

To verify (4), factor e(h/(2b))exp(-itr) from the binomial sum and use
(1-exp(2itr/q))^q=(-2i)^q exp(itr)sin(tr/q)^q.
When 0<|t|r/q<pi this difference is nonzero. The formula preserves sign and
phase; no floating evaluation is needed to establish nonvanishing.

Consequently the worst-case error of any procedure using this q-moment prefix
is at least |sin(tr/q)|^q; one common output cannot be closer than half the
separation to both targets. For fixed nonzero t and fixed 0<r<1, the lower
bound is exp(-q log q+O(q)); (3) gives an upper bound of the same logarithmic
order. Thus, as epsilon decreases to zero, the minimal prefix length needed
for a uniform epsilon-accurate target reconstruction satisfies

\[
q_{\min}(\epsilon)
=(1+o(1))\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}. \tag{5}
\]

This is an information statement about this exact moment-prefix family.
It is not a lower bound for every possible filter, not a runtime estimate,
and not a claim about bit compression of an exact real response. The witness
laws need not be stationary radix laws and are not alternative zero-seeded
BBP solutions. Their purpose is to certify the instrument's finite ambiguity.

## TM-04. A source-realized finite certificate with paid acquisition

For the authentic source take z_n={U_n+T_n}, n in [B,2B), and
(a_n,y_n)=(floor(16z_n),{16z_n}). The existing `certified_phase_grid` uses only
the four-pole source and zero seed to prove

\[
z_n\in[k_n/Q,(k_n+1)/Q),\qquad Q=16^d.
\]

It uses a common horizon H, sums the floors of 16^(H-j)r(j), and encloses the
result by [lo,lo+H+1]; the final unit includes T_H<1. Each queried cell must
be identical for both endpoints. This code is reused, not reimplemented.
At its midpoint zhat_n=(k_n+1/2)/Q, the mixed moments are exact sums of
rational powers times cyclotomic characters. They can be stored in Q(zeta_16).

Use (3) at these midpoints, then transport the **combined target** back:

\[
\left|W_B(h)-R_q(\widehat p_B)\right|
\le \frac{(\pi|h|/16)^q}{q!}+\frac{\pi|h|}{Q}. \tag{6}
\]

This bound is uniform in B and does not silently transfer individual moments
through a branch seam. Circular closeness controls the smooth combined target;
individual digit characters require their own chart certificate. Exact Machin
bounds for pi, integer rounding and Taylor angle intervals pay the remaining
evaluation error in the implementation. A forged grid is rejected by source
re-acquisition, rather than trusted because its label says BBP.

If q=q(B) tends to infinity and Q=Q(B) tends to infinity, the right side of
(6) tends to zero uniformly in B. This **justifies** that joint-resolution
limit for this target. It does not justify any arbitrary interchange for full
conditional Haar tables or noisy seed ensembles.

## TM-05. The arithmetic premise is now explicit, and still open

For h=1, a sufficient finite-channel R0 theorem would be: there exist q>=1,
eta>0 and B0 such that for every B>=B0 the authentic exact moments satisfy

\[
\operatorname{Re}\left[e(1/32)
\sum_{j<q}\frac{(\pi i/16)^j}{j!}M_j(B)\right]
\le1-\eta-\frac{(\pi/16)^q}{q!}. \tag{7}
\]

Then (3) proves R0 with saving eta. Conversely, any R0 saving admits some
fixed q with a slightly weaker inequality (7), by taking the remainder below
a quarter of the saving. Existence of unspecified q, eta is therefore a
**reformulation of R0**. The instrument is new quantitative access; (7) is not
an independently established arithmetic estimate.

The coherent completed orbit z=0 gives M_j=(-1)^j and target 1. Fixed point
1/15 gives a nonzero constant R0 margin but is nonnormal. Equal digit and
future marginals can conceal opposite signed target corrections: the two
laws on phases {1/64,35/64} and {3/64,33/64} have the same marginals but
opposite nonzero real Weyl means. Product replacement predicts zero and is
wrong. The tests retain these controls and deliberate error omissions.

**Next falsifier:** a source-dependent estimate on these actual coupled
moments that survives the coherent seed after the exact zero anchor is used.
More precise finite evaluation alone cannot discharge (7).

## Executed finite receipts and proof review

The root protocol was committed locally as
`17e58672bbd3954a8e72ec9de9ca90c1c2b5de0d` before these observations.
That identifier records local preregistration, not an earlier remote publication.
The three calibration shells and all three preregistered held-out shells ran.
For q=6, h=1 and grid depth 6, the outward rational certificates give:

| Shell start B | Lower bound for A_B | Upper bound for A_B |
|---:|---:|---:|
| 17 | 0.979650117655 | 0.979650651338 |
| 65 | 1.070159120212 | 1.070159653896 |
| 129 | 1.025254920464 | 1.025255454147 |
| 32771 | 0.999900226798 | 0.999900760482 |
| 65537 | 1.002818477407 | 1.002819011091 |
| 131101 | 0.998764021362 | 0.998764555046 |

The receipt also retains q=1,2,4, the exact moment field coordinates,
unrounded rational interval endpoints and every error budget. The deterministic
compressed source certificates retain the integer enclosure and every grid point;
their hashes are in `target_moment_results.json`. These are finite observations,
with shared source provenance. No extrapolation or probability of normality is
attached to them. The largest source horizon is 262223 hexadecimal places.

The target suite passed **15 tests**, including the exact binomial matching
witnesses, a real periodic radix orbit with all sixteen first digits balanced,
independent rational character evaluation, the small exact recurrence plus tail,
and mutations of phase orientation, coupling and error budgets. All four bearing
suites together passed **60 tests** in the preliminary combined run. Final
repository validation is recorded separately.

One first attempt at the bulk run was interrupted by an executor reset after
the calibration shells. Its incomplete receipt was not called complete. After
restoring the explicit repository import path, the entire six-shell run finished.
A large independent Machin digit computation was **not** run; the small-angle
Machin interval used to certify trigonometric evaluation is a different task.

A separate same-model agent reviewed TM-01 through TM-05, the sign in (4),
the asymptotic inversion in (5), and the implementation's interval rotations.
No defect was found. This is not external review. `MomentPacket` is a low-level
value object: arbitrary construction is not proof that its entries are moments
of a probability law or the authentic source. Source claims require the
`certified_shell` / `verify_packet_source` acquisition path.
