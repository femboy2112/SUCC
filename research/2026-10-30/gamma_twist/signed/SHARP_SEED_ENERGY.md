# The exact cofiber and the sharp source-only lag-energy floor

**Status:** local paper proofs, exact rational finite certificates, and a
separately implemented numerical oracle. These are not Lean proofs or blind
external review. The zero-seed signed estimate SC-06 and π normality remain
open. No scholarly priority is asserted.

## 1. Definitions and inherited authority

Keep the authentic coefficients `(4,-2,-1,-1)`, offsets `(1,4,5,6)`, and

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_n(s)=16U_{n-1}(s)+r(n),\quad U_0(s)=s.
\]

The authentic trajectory has `s=0`. Define the inherited positive Green tail

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
U_n(s)=16^{n-1}(\pi+16s)-T_n,
\quad 0<T_n<(8n+1)^{-2}.
\]

The exact total tail budget already occurs in the October 27
[Selected Boundary dossier](../../../2026-10-27/PI_SELECTED_BOUNDARY_CRT_FRONTIER.md),
as does nonlinear Lipschitz cylinder transport (SB-1). The new PR400 Gamma
derivation is another source representation of that inherited budget. We do
not re-label its existence as a new result.

For fixed nonzero integer h put

\[
E_n(s;h)=1-\cos\big(2\pi h(U_{n+1}(s)-U_n(s))\big),\qquad
D_n=T_n-T_{n+1}>0.
\]

Strict positivity and monotonicity of the tails follow from the positive
Laplace kernel `4-2 exp(-3x)-exp(-4x)-exp(-5x)`. In particular,

\[
D_{n+1}-16D_n=r(n+2)-r(n+1).                    \tag{1}
\]

## 2. SG-01: the complete prime-complementary recurrence

For a prime p, let `P_p` be the canonical p-primary projection on `Q/Z` and
`Q_p=1-P_p` its complementary projection. If a reduced rational is `A/(p^a d)`
with `(p,d)=1`, then

\[
P_p\left(\frac A{p^a d}\right)
=\frac{A d^{-1}\bmod p^a}{p^a}\pmod1.
\]

Both maps are additive homomorphisms and commute with integer multiplication.
Consequently the actual zero-seed cofiber `v_n=Q_p(U_n(0))` satisfies

\[
\boxed{v_n=16v_{n-1}+r(n)-P_p(r(n))\pmod1,\quad v_0=0,}
\]

and therefore

\[
v_n=\sum_{m=1}^n16^{n-m}\big(r(m)-P_p(r(m))\big)\pmod1. \tag{2}
\]

On a p-pole-free interval after a first birth b,

\[
v_{b+j}=16^jv_b+\sum_{t=1}^j16^{j-t}r(b+t)\pmod1.       \tag{3}
\]

This is an exact expression for the actual weight `w_j=e(hv_(b+j))`, with the
full earlier source history retained in `v_b`. The source increments are
small in the real metric but the homogeneous multiplier is still 16. There
is no slowly varying-weight conclusion. At pole collisions equation (2),
rather than the pole-free simplification (3), is mandatory.

**Execution:** 301 times at each of p=2,3,5,7,13,19,73, reconstructed by
projecting the forcing first, agree exactly with projections of the full
orbit. The p19 disappearance at n=10,...,16, return at n=17, and p73 zero at
n=274 survive. This is a representation theorem, not a signed saving.

## 3. SG-02: an unconditional source-forcing energy floor

For every real seed s, all integers `A>=1`, `L>=2`, and every integer h,

\[
\boxed{\sum_{n=A}^{A+L-1}E_n(s;h)\ \ge\
\frac1{289}\sum_{n=A}^{A+L-2}
\left[1-\cos\big(2\pi h(r(n+2)-r(n+1))\big)\right].}       \tag{4}
\]

**Proof.** Set `z_n=e(h(U_(n+1)-U_n))`. Exact recurrence gives
`z_(n+1)=z_n^16 e(h(r(n+2)-r(n+1)))`. Since
`|z^16-1|<=16|z-1|` for a unit complex z,

\[
|e(h(r(n+2)-r(n+1)))-1|
\le |z_{n+1}-1|+16|z_n-1|.
\]

Apply the Euclidean triangle inequality to the two truncated vectors on
the right. Each truncated norm is at most the full norm on A,...,A+L-1,
so the source vector norm is at most 17 times that full norm. Squaring and
using `|e(t)-1|^2=2(1-cos(2*pi*t))` proves (4). ∎

This bound uses the authentic forcing but **not** the authentic zero seed.
It is a positive coercivity floor; it is much too small for SC-06. The next
theorem shows its scale cannot be repaired to a constant using only the
forcing and allowing arbitrary seeds.

## 4. SG-03: finite nonlinear minimization by one quadratic projection

Fix A,L,h as above with h nonzero. Write `d_j=h D_(A+j)`,
`a_j=16^(j-L+1)`, `0<=j<L`, and

\[
M=\sum_{j=0}^{L-1}\left[1-\cos(2\pi d_j)\right],\qquad
Q=\sum_jd_j^2-\frac{(\sum_ja_jd_j)^2}{\sum_ja_j^2}.
\]

Suppose the following explicit small-branch conditions hold:

\[
\frac{17^2 M}{8}<\frac14,\qquad
\max_{A\le n<A+L-1}|h(r(n+2)-r(n+1))|<\frac12.            \tag{5}
\]

Then, for the **infimum over all real seeds**,

\[
\boxed{2\pi^2\left(1-\frac{\pi^2M}{24}\right)Q
\ \le\ \inf_{s\in\mathbb R}\sum_{n=A}^{A+L-1}E_n(s;h)
\ \le\ 2\pi^2Q.}                                         \tag{6}
\]

The right side can be sharpened by evaluating the actual trigonometric sum
at `tau=-(sum a_j d_j)/(sum a_j^2)`.

**Proof.** The initial lag phase runs over the entire circle as s runs over
the reals: its seed coefficient is the nonzero real number `15h16^A`.
All later lag phases depend continuously on this circle coordinate, so a
minimum exists on a compact circle. The coherent same-forcing seed
`s_*=-pi/16` has lag phases d_j; hence the minimum is at most M.

At any minimizing seed choose centered lifts `u_j in [-1/2,1/2]` of its lag
phases. The elementary chord bound `1-cos(2*pi*u)>=8u^2` gives
`u_j^2<=M/8` for every j. The exact recurrence says

\[
u_{j+1}-16u_j-h(r(A+j+2)-r(A+j+1))\in\mathbb Z.
\]

Condition (5) makes the absolute value of this integer strictly less than
one. It is therefore zero for **every** adjacent pair at **every** minimizer.
Equation (1) then forces `u_j=d_j+a_j tau` for some real tau.

The minimum of `sum_j(d_j+a_j tau)^2` over all real tau is exactly Q, by
completing the square. For centered minimizing lifts, Taylor's inequality
gives

\[
1-\cos(2\pi u_j)
\ge 2\pi^2u_j^2\left(1-\frac{\pi^2u_j^2}{3}\right)
\ge 2\pi^2u_j^2\left(1-\frac{\pi^2M}{24}\right).
\]

This proves the lower bound. Conversely, every real tau specifies a valid
initial lag phase and hence some real seed. Use the quadratic minimizing
tau and `1-cos(2*pi*u)<=2*pi^2u^2` to prove the upper bound. No assertion
that the authentic seed minimizes this functional is made. ∎

**Executable certificate.** `minimum_energy_certificate` uses exact rational
Green-tail intervals, the inherited outward Machin/Taylor instrument, and
interval bounds for the displayed Q. It verifies (5), then encloses the
nonlinear infimum. The independent oracle reconstructs the source by a
common-denominator recurrence and uses a separate 100-digit trigonometric
derivative bisection. Numerical agreement is a cross-check of the rigorous
enclosures, not their proof authority.

## 5. SG-04: sharp asymptotic floor, including all prime-birth window scales

For fixed h nonzero and C>0, let `A -> infinity`, `L=L(A) -> infinity`,
`L<=C A`. Then

\[
\boxed{\inf_s\frac1L\sum_{n=A}^{A+L-1}E_n(s;h)
\sim\frac{2\pi^2h^2}{L}\sum_{n=A}^{A+L-1}D_n^2
\sim\frac{\pi^2h^2}{512L}\sum_{n=A}^{A+L-1}n^{-6}.}       \tag{7}
\]

The single fixed coherent seed `s_*=-pi/16` attains this asymptotic value;
this is not merely an adversary whose seed changes with A.

**Proof.** Direct expansion of the authentic rational forcing gives

\[
r(n)=\frac{15}{64n^2}+O(n^{-3}),\qquad
r(n)-r(n+1)=\frac{15}{32n^3}+O(n^{-4}).
\]

Summing the positive future resolvent and its difference, with geometric
weights whose total is 1/15, gives

\[
T_n=\frac1{64n^2}+O(n^{-3}),\qquad
D_n=\frac1{32n^3}+O(n^{-4}).                            \tag{8}
\]

One can justify each uniform remainder by splitting j<=n and j>n in the
geometric sum; alternatively Taylor's rational remainder is bounded by a
constant times `(n+j)^-4`, and `sum j16^-j` is finite. Thus `M=O_h(LA^-6)`
is `O_(h,C)(A^-5)`, and (5) holds for all sufficiently large A.

Since `sum a_j<=16/15`, `sum a_j^2>=1`, and `D_n` is decreasing, the amount
subtracted by the quadratic projection is at most
`(16/15)^2 h^2 D_A^2`. Meanwhile
`sum d_j^2>=L h^2 D_(A+L-1)^2`; by (8) and L<=CA its ratio to the previous
bound tends to infinity with L. Hence `Q~sum d_j^2`. Equation (6) proves
the first asymptotic in (7), and (8) proves the second. Applying Taylor
directly to the coherent seed proves asymptotic attainment. ∎

In particular, if L=o(A),

\[
\inf_s\frac1L\sum E_n(s;h)\sim\frac{\pi^2h^2}{512A^6}.
\]

If L/A tends to a positive theta,

\[
\inf_s\frac1L\sum E_n(s;h)
\sim\frac{\pi^2h^2}{2560\theta}
\big[1-(1+\theta)^{-5}\big]A^{-6}.
\]

On SC-06 windows, A=b_p is asymptotic to p/8 and the number of lag-energy
terms is `L=ord_p(16)-1`; since `ord_p(16)<= (p-1)/4`, L<=CA for an absolute
C. Eligibility forces `ord_p(16)>=sqrt(p)`, hence L tends to infinity.
The best energy lower bound valid
for **every seed with the authentic forcing** is therefore of order p^-6,
while SC-06 requires a positive constant for the selected zero seed.
This quantifies the missing selection step. It does not supply that step.

For L=o(A), the elementary source floor (4) is asymptotic to 225/289 times
the sharp infimum, because `r(n+2)-r(n+1)~-15D_n`. Thus even that elementary
derivative estimate is already on the correct source-only scale.

## 6. SG-05: a sharper window form of inherited Gamma transfer

For every seed s and consecutive lag-one window A,...,A+L-1,

\[
\left|\sum_{n=A}^{A+L-1}E_n(s;h)
-\sum_{n=A}^{A+L-1}\left[1-
\cos(2\pi(15h)16^{n-1}(\pi+16s))\right]\right|
\le 2\pi|h|\sum_{n=A}^{A+L-1}D_n
=2\pi|h|(T_A-T_{A+L}).                                 \tag{9}
\]

This follows directly from the chord inequality and telescoping. It is a
monotonicity sharpening of earlier SB-1, not a new signed saving. Its
normalized error is less than `2*pi*|h|/[L(8A+1)^2]`.
It locates SC-06 precisely at the *actual* pure-radix frequency 15h on the
same moving window. The Gamma correction is too small to manufacture or
destroy a constant energy gap at large p; the selected arithmetic phase is
where the unresolved estimate lives.

## 7. Two analytic attacks and the exact approximate-grid rotation

**Weighted Gauss completion.** Formula (2) was used in the actual full
Fourier factorization, never replaced by independent cofiber marks. All 18
declared `sqrt(p)*Wiener(w)` bounds were at least L. The reconstruction
residuals were numerical cross-checks, while the Fourier identity is exact
algebra. This route still needs a source-selected signed bound between the
completed terms; taking all absolute values has paid away the needed gain.

**Source derivative / annihilator.** Equations (4)--(7) solve the best
all-seed version asymptotically. Higher source regularity alone cannot turn
the p^-6 floor into the required selected constant. This is an exact
obstruction, not a failure of numerical precision. The zero boundary is a
necessary extra input to any successful estimate by this route.

**Approximate conductor grids.** For finitely many rational phases x_j and
an integer q, sort the residues `{q x_j}` around the circle and let G be
their largest circular gap. Then

\[
\min_\theta\max_j\operatorname{dist}
(x_j,\theta+q^{-1}\mathbb Z)=\frac{1-G}{2q}.              \tag{10}
\]

Indeed multiplying by q reduces to the smallest circle arc containing all
residues; its length is one minus the largest complementary gap. Its
midpoint realizes the radius, and no shorter arc can contain all points.
This exact criterion tested all `1<=q<=L` on the full authentic p701,709,733
first-birth windows at error `1/p^2`. All q were excluded in these three
finite cases. The independent oracle computes the shortest arc by all
cuts, and the tests compare a pair-center minimax implementation on four
authentic phases. There is no all-horizon or unrestricted approximate-grid
impossibility theorem here.

Stoneham c3/c5 exact stage grids recover q/c occupied cells with multiplicity
c(c-1). Conductor2 has a `ceil(j/4)` transient and then a single zero cell
of multiplicity `2^j-ceil(j/4)`; a failed immediate-collapse assertion is
retained in [FAILED_CONTROLS.md](FAILED_CONTROLS.md).

## 8. What the actual zero seed did, and what remains unproved

All 36 fresh declared prime/frequency cases are eligible and certify
SC-06's trial `E>=1/4`; their minimum lower endpoint exceeds 0.9456199934.
The 6 p13/p73 calibration rows are retained separately. These are exact
finite observations, not evidence of a universal theorem by extrapolation.

The hostile controls distinguish the question: a coherent same-forcing
seed and the seven-pole zero-seed null source have tiny energy; rational
constant twists and exact circle aliases preserve the expected readouts.
The positive finite-p2-resolution mutant, wrong/same-ratio sources,
Gamma-rank/higher-jet fakes, periodic de Bruijn, and biased Bernoulli can
also have large energy. Thus passing one lag threshold neither identifies
the authentic source nor proves normality.

The remaining source-selected obligation is to exclude sustained alignment
of `e_p(h delta a_j)` with `e(h delta v_j)` by using both equation (2) and
`v_0=0`. The selected zero-seed initial condition must force an energy
strictly above the sharp source-only floor on a non-negligible fraction of
the window. No theorem doing that uniformly has been established here.

Classical calibration sources: [Bailey--Crandall 2001](https://doi.org/10.1080/10586458.2001.10504441),
[Bailey--Crandall 2002](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf).
Their Hypothesis A is not assumed. The published finite irrationality bound
of [Zeilberger--Zudilin](https://arxiv.org/abs/1912.06345) is not used as a
substitute for a selected moving-window estimate. No current-best
irrationality claim or unverified 2026 preprint is adopted in these proofs.
