# All gains together: an elementary normality reduction without an entropy premise

**Date:** 2026-10-24. **Parent:** #274 at
`d942c4707d750f788f39acb137a04e871a93e0a6`.
**Authority:** paper proofs and exact finite calibration, not a formal kernel.
**Pi normality and the two actual-source estimates below remain OPEN.**
The reduction is new to this research round; scholarly originality is not claimed.

## 1. A complete classification of coherent gain-averaged laws

Write `T_q(x)=qx mod 1` on the circle, let lambda be its uniform probability,
and set

$$
A_Q\mu=\frac1Q\sum_{q=1}^Q(T_q)_*\mu.
$$

These are gains `1,2,...,Q`, not the histories `1,3,...,3^(Q-1)` of the
previous SPS dossier. For a rational point `x=a/d` in lowest terms, let
`u_d` be the uniform law on the **complete** d-torsion grid, including zero.
Then, for every circle probability,

$$
R\mu:=\lim_{Q\to\infty}A_Q\mu
=\mu(\mathbb T\setminus(\mathbb Q/\mathbb Z))\lambda
+\sum_{x\in\mathbb Q/\mathbb Z}\mu\{x\}\,u_{\mathrm{den}(x)}.
$$

The convergence is weak, equivalently in circle `W1`. To prove it, average
each continuous test function along `qx`. Rational x is periodic; irrational
x is equidistributed, as follows by the elementary geometric sum for every
nonzero Fourier character and trigonometric approximation. Integrate these
pointwise limits using bounded convergence. The countable rational series
has total mass at most one. The Haar coefficient includes irrational atoms,
not only the nonatomic part of mu.

**Fixed-law theorem.**

$$
\boxed{R\mu=\mu\quad\Longleftrightarrow\quad
\mu=c\delta_0+(1-c)\lambda,\quad0\le c\le1.}
$$

If the two measures agree, their masses at zero agree. The displayed formula
therefore gives

$$
\mu\{0\}=\mu\{0\}
+\sum_{x\in(\mathbb Q/\mathbb Z)\setminus\{0\}}
\frac{\mu\{x\}}{\mathrm{den}(x)}.
$$

All the summands are nonnegative, so there are no rational atoms away from
zero. Substituting this into `R mu` proves the assertion and also rules out
irrational atoms in a fixed law. Conversely zero and Haar are fixed by every
gain. This proof uses neither positive entropy nor a measure-rigidity
conjecture.

The same classification holds if mu is individually invariant under every
prime gain: composition gives every integer gain and hence `R mu=mu`.
Preservation of the entire averaged gain operation is the weaker-looking
input; the fixed-law class is exactly the same.

Multiplication gains indexed by primes are different observables from the
primary projections of rational circle points. The theorem does not turn
p-adic marginal agreement into gain-law preservation. Their common prime
labels do not identify these two maps.

## 2. A precise source-specific replacement for Hypothesis A

Let `mu_N=(1/N) sum_(n=1)^N delta_(y_n)` be the occupation law of the authentic
BBP source. Define `B_rho` as the closed circle ball of radius rho about zero.
The following two conditions suffice:

$$
\tag{P}
\lim_{Q\to\infty}\limsup_{N\to\infty}
W_1(A_Q\mu_N,\mu_N)=0,
$$

$$
\tag{Z}
\lim_{\rho\downarrow0}\limsup_{N\to\infty}\mu_N(B_\rho)=0.
$$

**Proof.** Take any weak accumulation law mu. For each fixed Q, `A_Q` is a
finite sum of continuous pushforwards, so continuity of W1 on the compact
circle gives

$$
W_1(A_Q\mu,\mu)\le
\limsup_N W_1(A_Q\mu_N,\mu_N).
$$

Send Q to infinity only now. Condition (P) and the first theorem imply
`mu=R mu`, hence `mu=c delta_0+(1-c)lambda`. To remove c, apply Portmanteau
to the open ball of radius rho, which is contained in `B_rho`. It gives
`mu{0} <= limsup_N mu_N(B_rho)`. Now send rho down to zero and use (Z).
Every accumulation law is Haar, so `mu_N -> lambda`. The inherited BBP tail
transport gives base-16, and therefore base-2, normality of pi. QED.

**Converse and novelty tax.** Haar convergence implies (P) at each fixed Q,
and (Z) because fixed balls have Haar-null boundaries and mass `2 rho`.
Thus the conjunction is an **equivalent criterion**, not a proved weaker
arithmetic theorem and not a proof of normality. Its components can be
attacked separately. Relative to the two-gain positive-dimension route,
the regularity premise is reduced to absence of an atom at one point;
the price is preservation under the whole gain average. Neither authentic
estimate has been established.

The order of the limits is load-bearing. An arbitrary diagonal `Q(N)` is
not supplied by this proof. The preceding tripling-history fast-schedule
counterexample concerns a different operator and must not be cited as a
counterexample to this one.

An explicit reason not to pass a weak limit through R is
`mu_j=delta_(1/j) -> delta_0`, whereas `R mu_j=u_j -> lambda` and
`R delta_0=delta_0`. Thus R is not weakly continuous. This is not a
counterexample to preservation: `W1(R mu_j,mu_j)` tends to `1/4`, not zero.

Irrationality does not give (Z). For example the nonperiodic number
`sum_(m>=1)16^(-m^2)` is irrational, but its nonzero digits have density zero.
Every fixed digit window is all zero with density one, so its occupation
law converges to `delta_0`. It satisfies (P) and fails (Z). This is a changed
source, not a claim about pi. Conversely any nonuniform nonatomic invariant
digit law satisfies (Z) and fails (P).

## 3. Every integer readout is already authentic and exact

Retain the four-pole forcing, zero initial state and literal recurrence

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
y_{n+1}\equiv16y_n+r(n+1)\pmod1.
$$

For every positive integer q,

$$
\boxed{y_{n+1}+(q-16)y_n-r(n+1)\equiv qy_n\pmod1.}
$$

The coefficients are integers, so this is a well-defined circle readout and
does not need a division-cover residue. It extends the inspected #276 signed
q=3 stencil. The source correction is exact and independent of q. Gains
compose as `T_p T_q=T_(pq)`, so prime factorizations give coherent readouts.
This proves their construction and coherence, **not preservation of their
empirical law**. The distinction survives using every gain simultaneously.

For the true orbit `z_n={16^n pi/16}`, the existing tail gives
`d_T(z_n,y_n)<B_n=1/((8n+1)(8n+2))`. Let
`bar_B_N=(1/N)sum_(n=1)^N B_n`. Pairing corresponding atoms gives

$$
W_1(\mu_N^z,\mu_N^y)\le\overline B_N,\qquad
|W_1(A_Q\mu_N^z,\mu_N^z)-W_1(A_Q\mu_N^y,\mu_N^y)|
\le\frac{Q+3}{2}\overline B_N.
$$

Indeed the Lipschitz constant of the average is at most the mean gain
`(Q+1)/2`. At fixed Q the error tends to zero. It must be retained if Q grows.

## 4. A finite certificate using all needed prime gains

For any circle probability mu write `epsilon_q=W1(T_q mu,mu)`. Then

$$
\epsilon_{ab}\le\epsilon_a+a\epsilon_b.
$$

This follows by inserting `T_a mu` and applying the a-Lipschitz bound to
`T_a(T_b mu)` versus `T_a mu`. Either factor order can be used, and every
cost is also at most the circle diameter `1/2`. Therefore certified costs
at primes generate certified costs `C_q` at all composite gains. Omitting
a prime divisor is a missing certificate, not a zero cost.

Put `e(x)=exp(2 pi i x)`, `mu_hat(h)=int e(hx)dmu`, and `0<rho<=1/2`.
For every integer h nonzero and Q>=1,

$$
\boxed{|\widehat\mu(h)|\le\mu(B_\rho)+\frac1{2Q\rho}
+2\pi\left(C_{|h|}+\frac1Q\sum_{q=1}^QC_q\right).}
$$

**Proof.** The Lipschitz constant of `e(x)` is at most `2 pi`, so
`|mu_hat(q)-mu_hat(1)|<=2 pi epsilon_q`, and similarly for positive h;
negative frequencies have the same modulus. Average over q and use

$$
\left|\frac1Q\sum_{q=1}^Qe(qx)\right|
\le\min\left(1,\frac1{2Q\|x\|_{\mathbb T}}\right).
$$

The last bound is the geometric-sum identity and
`sin(pi t)>=2t` on `[0,1/2]`. Split the integral at `B_rho`, then use the
triangle inequality. QED. This is a finite, calibrated version of the
all-prime stationary-law route. It often gives the trivial bound one on
small source samples; that outcome is preserved rather than treated as a
sign of asymptotic convergence.

The code uses exact rational circle-W1 primal/dual certificates and replaces
`2 pi` only by the safe rational upper bound `44/7`. Quarter-circle characters
give an independent exact Fourier check. A uniform grid of order 101 is a
held-out nontrivial certificate. A grid of order 7 is invariant under gains
2,3,5 but not 7, calibrating the missing-prime failure.

## 5. Rational finite-source averaging and the normalization trap

For `x=a/d` in lowest terms, and `r=Q mod d`, direct residue counting gives

$$
\mathrm{TV}(A_Q\delta_x,u_d)=\frac{r(d-r)}{dQ},\qquad
W_1(u_d,\lambda)=\frac1{4d}.
$$

The second identity follows by transporting each length-`1/d` cell around
its grid point radially; the 1-Lipschitz distance-to-grid function proves
optimality. Thus for a rational atomic probability `mu=sum m_i delta_(x_i)`,

$$
W_1(R\mu,\lambda)\le\sum_i\frac{m_i}{4d_i},\qquad
(R\mu)\{0\}=\sum_i\frac{m_i}{d_i}.
$$

Mixtures use convexity, not equality of their TV remainders. Large
denominators can make the gain-averaged ensemble close to Haar while the
selected source points cluster. Preservation (P) is precisely what an
ensemble calculation still has to pay. The implementation refuses to
materialize exponentially large grids and evaluates these scalar bounds
directly from their denominators.

## 6. Validation and explicit remaining task

The production module is `observational_succ/all_gain_observers.py`; its
tests include exact rational-period counting, composite-cost comparisons,
wrong-forcing mutations, zero and periodic laws, a missing-prime failure,
and independent quarter-circle Fourier characters. The probe records all
registered source rows and conservative decimal intervals from exact
rationals. These are finite measurements, not a rate or theorem about N
tending to infinity. No observed direction of change is used as an estimate.

The remaining source theorem is (P) and (Z), or an explicitly stated
sufficient bound implying them. Geometric coherence of the charts alone
does not supply either statement. A direct upper-only block/collision bound
is an alternative route; see `PI_TRIMMED_JOINT_ENTROPY.md`.

## 7. The real carrier cannot be a uniformly continuous decoder of time residues

There is a separate sharp restriction on an appealing all-prime completion.
Let `z_n={b^n alpha}` with irrational alpha. For every fixed Q and N,

$$
\sup_{n\ge N}d_{\mathbb T}(z_{n+Q},z_n)\ge\frac1{b+1}.
$$

Otherwise the supremum is strictly below `1/(b+1)`. Choose signed
differences `delta_n` in that interval. The number
`delta_(n+1)-b delta_n` is an integer of absolute value less than one, hence
zero. Boundedness of `delta_(n+j)=b^j delta_n` forces every delta to vanish.
Then `b^N(b^Q-1)alpha` is an integer, contradicting irrationality.
In fact the same contradiction holds if every individual distance is
strictly less than the threshold, even without a uniform strict gap.

Because the BBP y_n shadows `z_n={16^n pi/16}` with vanishing error, for every
fixed Q,N,

$$
\sup_{n\ge N}d_{\mathbb T}(y_{n+Q},y_n)\ge\frac1{17}.
$$

This is a supremum statement, not a positive-frequency estimate. It rules
out a continuous map `g:Z_hat -> circle` with `d_T(y_n,g(n))->0`:
uniform continuity on the compact profinite completion would give a period
Q for which `d_T(g(n+Q),g(n))<1/34` uniformly, and the eventual approximation
error would contradict the preceding inequality.

The input here is the **profinite time index**, not the complete exact
primary state of U_n. Full primary state data identify a rational circle
point algebraically and may have a discontinuous decoder. Pointwise limits,
measurable decoders and joint statistical estimates are not excluded. A
uniform real-continuity axiom for time clocks would be false, rather than
a missing source theorem.
