# Cayley source observer: the circle on a line, with paid completion clocks

**Status:** classical transport plus paper-proved source calibration and a
sharp clock counterexample. Exact finite arithmetic tests accompany the
implementation. Original-zero signed cancellation, hexadecimal parity balance,
pi base-16 normality, and RH remain **OPEN**.

## Provenance and exact research target

This integrates Leah's line/circle and reciprocal-pi observation with the
Fourier–Yoneda pinbed and PR #576's finite Scott source weld. The proposed
meaning is precise: preserve a declared observable algebra while changing the
carrier chart, then pay explicitly for finite source precision. This does not
identify ordinary Euclidean line geometry with circle geometry.

Baseline: PR #576 at `afabc458323ef2e3a20ce2bae77239c4190819c5`, based on Main
XXII `43886e830cee5ff6d6b37719e18d809819673bd9`. The implementation imports
the unchanged `observational_succ.duck_bbp` source API. Its most recent commit
in the inspected history is `57a103b7157567fe0fee3c651c5e06794e53703c`.
The imported-foundations manifest was inspected and is unchanged.

**Hole contract.** For source horizon L, observation time n<=L, and all integer
Fourier modes |h|<=H, construct a source-preserving finite observer and state
exactly when it uniformly approximates its completed observer. Test the claim
that merely sending L,n,H to infinity suffices. This is a precision/semantic
question strictly weaker than signed cancellation: it applies equally to a
coherent wrong seed, and its conclusion does not bound the observed mean.

**Novelty boundary.** Cayley transport and Fourier completeness are classical.
The source-sensitive tail bound and its asymptotics are already in SUCC. Earlier
`floor_layercake_prime_carry/THEOREMS.md` FLP-08 and
`signal_frontier/crucible/THEOREMS.md` SC3–SC4 already establish quadratic or
higher-order source resolution thresholds. The contribution here is their
explicit integration with the Scott horizon, a necessary-and-sufficient
uniform-band clock condition, and a near-maximal exact-source counterexample
to unqualified cofinality. No worldwide priority is claimed.

## CAY-01. The complete circle observer on the compactified line

Let RP^1 be the real projective line, with homogeneous point [X:Y], and define

$$
C([X:Y])=\frac{X+iY}{X-iY}.
$$

The denominator is nonzero whenever (X,Y)!=(0,0). The formula is unchanged by
any nonzero real rescaling. It maps RP^1 bijectively and continuously onto the
unit circle, with continuous inverse. In the affine chart x=Y/X,

$$
C(x)=\frac{1+ix}{1-ix},\qquad C(\infty)=-1.
$$

Writing theta=2 arctan(x) gives `C(x)=exp(i theta)` and

$$
\frac{d\theta}{2\pi}=\frac{dx}{\pi(1+x^2)}=:d\mu(x).
$$

Thus the reciprocal 1/pi is exactly the normalization of the transported
uniform circle measure. Both line ends approach the same projective point.
This is a one-point compactification and a measure transport, not an equality
between Euclidean arc length and Euclidean line length.

Pullback by C gives a unitary map

$$
L^2(S^1,d\theta/(2\pi))\longrightarrow L^2(\mathbb R,\mu).
$$

The transported modes

$$
\Phi_h(x)=C(x)^h,\qquad h\in\mathbb Z,
$$

are a complete orthonormal basis. Orthogonality follows directly by the
displayed change of variables. Completeness follows from circle Fourier
completeness and surjectivity of the change of variables modulo a null point.
Every mode extends continuously to infinity with value `(-1)^h`.

Finite orbit readings use these explicit continuous modes. Point evaluation
is not a well-defined bounded functional on an arbitrary L^2 equivalence
class; values on null sets may change without changing that class. The
unitary statement therefore does not, on its own, authorize a Hilbert-space
point sensor. For Borel probability measures on RP^1, equality of every
continuous Fourier mode implies equality of the measures: finite
trigonometric polynomials are uniformly dense in continuous circle
functions, so their integrals determine all continuous test integrals.
This measure-level pinbed also retains a possible atom at infinity.

The classical Fourier background is available in MIT 18.102, Casey Rodriguez,
[Lecture 15](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/resources/lecture-15-orthonormal-bases-and-fourier-series/)
and
[Lecture 16](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/resources/lecture-16-fejers-theorem-and-convergence-of-fourier-series/).
The change-of-variables calculation above is supplied explicitly; no abstract
category-theoretic theorem is needed to establish it.

## CAY-02. Exact power dynamics, including tangent poles

For every integer b>=1 write

$$
P_b(X,Y)+iQ_b(X,Y)=(X+iY)^b.
$$

The homogeneous map

$$
R_b([X:Y])=[P_b(X,Y):Q_b(X,Y)]
$$

is defined everywhere: its two components cannot vanish simultaneously.
Rescaling [X:Y] rescales both outputs by the same nonzero factor. Direct
division proves

$$
C(R_b(v))=C(v)^b,\qquad
\Phi_h(R_b(v))=\Phi_{bh}(v).
$$

In the finite chart, `R_b(x)=tan(b arctan x)` wherever its denominator is
nonzero; homogeneous coordinates supply the missing values. In particular,
`R_16(infinity)=0`, and an intermediate tangent pole is not a failure of the
circle map.

For a circle translation a, set

$$
M_a([P:Q])=
[\cos(\pi a)P-\sin(\pi a)Q:
 \sin(\pi a)P+\cos(\pi a)Q].
$$

Then `C(M_a(v))=exp(2 pi i a) C(v)`. Consequently the authentic forced
recurrence admits the exact projective realization

$$
v_n=M_{r(n)}R_{16}(v_{n-1}),\qquad
C(v_n)=e(U_n),\qquad e(t)=e^{2\pi i t}.
$$

The time index and original source r(n) remain attached to the action.
Although U_n and r(n) are rational, `tan(pi U_n)` and `tan(pi r(n))` are
generally not rational. `ProjectivePoint` implements exact rational test
points and rotations only; actual source certificates remain rational lift
intervals. Replacing `tan(pi r(n))` with r(n) would change the dynamics.

## CAY-03. Hexadecimal parity becomes a homogeneous sign observable

For t in R/Z away from the sixteen cuts `t=j/16`,

$$
f(t)=(-1)^{\lfloor16t\rfloor}=\operatorname{sgn}\sin(16\pi t).
$$

Choose `v=[cos(pi t):sin(pi t)]`. Since

$$
\Phi_8(v)=\frac{(X+iY)^{16}}{(X^2+Y^2)^8},
$$

one has `f(t)=sgn Q_16(X,Y)`. The homogeneous degree is even, so the sign
does not depend on the representative of v. In the x=Y/X chart,

$$
Q_{16}(1,x)=\sum_{j=0}^{7}(-1)^j\binom{16}{2j+1}x^{2j+1}.
$$

There are fifteen finite projective zeros and the remaining cut is infinity.
The sign formula deliberately excludes all cuts, where a half-open digit
convention assigns a value but a symmetric Fourier limit gives the midpoint
zero. Sending a problematic boundary to infinity does not remove it.

This is a semialgebraic representation of the same parity observable. It
provides exact chart compatibility, not a bound on its selected orbit average.

## CAY-04. Source prefix certificates and strict naturality

Retain the original four poles and literal seed zero:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Write `P_L=sum_(j=1)^L 16^(-j) r(j)`, including P_0=0, and

$$
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
Y_n=U_n+T_n=16^{n-1}\pi.
$$

The identification with pi imports the classical BBP identity. For p=8n-7,

$$
r(n)=\frac6{p(p+3)}+\frac4{p(p+4)}+\frac5{p(p+5)}.
$$

Each summand is positive and strictly decreases with n>=1. Therefore the
existing canonical source bound is strict:

$$
0<T_n<\frac{r(n+1)}{15}.
$$

This is **reused**, not a new source theorem. Define

$$
I^*_{n,L}=
\left[16^nP_L,\ 16^nP_L+
16^{n-L}\frac{r(L+1)}{15}\right],\qquad 0\le n\le L.
$$

Its lower and upper endpoints strictly enclose Y_n. At fixed n the lower
endpoint strictly increases with L. The upper endpoint strictly decreases,
because the old upper endpoint minus the next upper endpoint equals

$$
16^{n-L}\frac{r(L+1)-r(L+2)}{240}>0.
$$

The widths tend to zero. At every finite permitted horizon,
`16 I^*_(n,L)=I^*_(n+1,L)`. The new implementation obtains these intervals
from `duck_bbp.tail_interval(0,L)` and scales them; it does not duplicate the
source formula. Relative to PR #576's looser `4/(15(L+1)^2)` tail, this
improves the integration budget using an already proved canonical bound.

## CAY-05. Coupled clocks: the exact uniform-band condition

For all n<=L and integer h,

$$
|e(hY_n)-e(h16^nP_L)|
\le \min\left(2,2\pi |h|16^{n-L}\frac{r(L+1)}{15}\right).
$$

Thus for every finite N<=L and H>=0 the rational coefficient

$$
\beta_{N,L,H}=H16^{N-L}\frac{r(L+1)}{15}
$$

pays the entire band of times `0<=n<=N` and modes `|h|<=H`. The function
`coupled_horizon` finds the least L>=N paying any declared positive rational
coefficient tolerance. This is a finite certificate, not a claim to infer an
infinite schedule's cofinality from its prefix.

There is also a sharp analytic converse. Let N_k<=L_k be nonnegative integers,
let L_k tend to infinity, and let H_k be nonnegative integers. Set

$$
\delta_k=16^{N_k-L_k}T_{L_k},\qquad
D_k=\max_{\substack{0\le n\le N_k\\|h|\le H_k}}
|e(hY_n)-e(h16^nP_{L_k})|.
$$

Then

$$
D_k\longrightarrow0
\quad\Longleftrightarrow\quad
H_k16^{N_k-L_k}/L_k^2\longrightarrow0.
$$

**Proof.** The original positive source gives `L^2 T_L -> 1/64`.
For completeness, `L^2 r(L+j)->15/64` for each fixed j, and
`0<L^2 r(L+j)<15/64` for L>=1,j>=1 by the displayed positive
decomposition. Dominated convergence in the geometrically weighted sum
proves the tail limit. Thus delta_k tends to zero and is asymptotic to
`16^(N_k-L_k)/(64L_k^2)`.

If H_k delta_k tends to zero, the elementary phase inequality bounds D_k
by `2 pi H_k delta_k`, which tends to zero. Conversely, on any subsequence
where H_k delta_k>=epsilon>0, fix `0<a<min(epsilon,1/2)` and choose
`h_k=floor(a/delta_k)`. Eventually h_k<=H_k and `h_k delta_k->a`.
The last-time phase difference tends to `2 sin(pi a)>0`. This rules out
uniform convergence. The claim follows.

More precisely, if `H_k delta_k -> c` in [0,infinity], then

$$
D_k\longrightarrow
2\sin\bigl(\pi\min(c,1/2)\bigr).
$$

When c<1/2, the h-grid has mesh delta_k and sine is increasing up to 1/2;
the largest last-time mode attains the limit, and earlier-time errors are
no larger asymptotically. When c>=1/2, choose a last-time frequency with
`h_k delta_k->1/2` and use the universal upper bound 2. The same argument
applies when c=infinity. No signed average or equidistribution premise
appears in this proof.

## CAY-06. An explicit near-maximal cofinal-clock counterexample

Take the diagonal finite horizon `L_n=n` and the integer frequency

$$
h_n=32n^2.
$$

All three clocks tend to infinity. Nevertheless,

$$
|e(h_nY_n)-e(h_nU_n)|=|e(h_nT_n)-1|\longrightarrow2.
$$

This is the largest possible complex-unit phase error. At the level of an
entire band, `H_n/n^2->a` gives the explicit response

$$
\max_{|h|\le H_n}|e(hY_n)-e(hU_n)|
\longrightarrow2\sin\bigl(\pi\min(a,32)/64\bigr).
$$

The existing effective tail inequality GQ3 in
[`quotient_signal/gamma/THEOREMS.md`](../../2026-11-08/quotient_signal/gamma/THEOREMS.md)
gives a rate:

$$
0<\frac1{64n^2}-T_n<\frac7{512n^3}.
$$

Hence `0<1/2-h_n T_n<7/(16n)`. Cosine concavity on [0,pi/2] yields

$$
|e(h_nT_n)-1|>2-\frac7{4n},\qquad n\ge1.
$$

The executable finite counterprobe does not depend on floating pi: it
encloses h_n T_n with the canonical rational `tail_interval` and applies
the rational lower bound `max(0,2-4 epsilon)`. At n=128 and depth=12 that
certificate proves the phase error exceeds 99/50.

**Verdict:** unqualified interchange of completion with growing oscillators
is REFUTED. CAY-05 gives the paid repair. Earlier SUCC critical-bandwidth
results already explain the mechanism; this is its direct Scott-clock
counterexample and calibration interface.

## CAY-07. Common-horizon epoch transport reaches subexponential bands

Pointwise last-time error and epoch-averaged error are different requirements.
For an integer A>=1, complete every time `A<=n<2A` to the **same source
horizon L=2A**. Let

$$
b_L=\frac{r(L+1)}{15},\qquad D=7H b_L.
$$

Since `2 pi<7`, for every integer Fourier cutoff H>=0,

$$
\max_{|h|\le H}\left|
\frac1A\sum_{n=A}^{2A-1}e(hY_n)
-\frac1A\sum_{n=A}^{2A-1}e(h16^nP_{2A})\right|
\le\frac1A\sum_{j=1}^{A}\min(2,D16^{-j}).
$$

Here j=2A-n. This is an exact rational upper budget. It is obtained by the
triangle inequality; no cancellation among errors is assumed.

The unclipped geometric sum also gives

$$
\text{error}\le\frac{7H b_{2A}}{15A}(1-16^{-A})
=O(H/A^3).
$$

A stronger regime follows from clipping. Let k be the least nonnegative
integer for which `D16^(-k)<=2`. Then

$$
\text{error}\le
\min\left(2,\frac{2k+2/15}{A}\right).
$$

**Proof.** If k>=1, at most the k-1 terms with j<k need the bound 2; the
remaining infinite geometric tail is at most
`2 sum_(j>=0)16^(-j)=32/15`. Their sum is `2k+2/15`.
If k=0, the sum from j=1 is at most D/15<=2/15. Truncating at A terms
can only reduce these sums, and every average error is at most 2.

It follows that for any integer cutoff sequence satisfying

$$
\log(1+H_A)=o(A),
$$

the uniform epoch-mean transport error tends to zero. This allows every
polynomial bandwidth, and subexponential bands such as `H_A=16^(floor(sqrt A))`.
The implementation computes the clipped bound by counting its saturated
prefix and summing the remaining geometric progression in exact fractions.

There is no conflict with CAY-06. The diagonal comparison at time n there
uses horizon L=n and omits the entire future tail T_n. Here all interior
states already contain their authentic future source up to L=2A; all but
O(log(1+H_A)) states have exponentially smaller residuals. Averaging permits
the terminal exceptional fraction to disappear. These are different paid
observations, not a violation of the quadratic last-time threshold.

This theorem does not show that the finite rational exponential sum is
small. It transfers that same unsigned error budget for every seed; the
original-zero signed bound remains to be proved. Its practical value is a
larger, explicitly certified finite-horizon probe family for the arithmetic
frontier.

## CAY-08. What the observer retains and what it cannot authenticate

For a seed s, write `U_n(s)=U_n+16^n s`. The complete circle observer loses
integer winding. The distinct seed s=1/16 gives

$$
U_n(1/16)-U_n(0)=16^{n-1}\in\mathbb Z,\qquad n\ge1.
$$

Every Cayley mode at every such time agrees. Source fidelity therefore
requires the original time-labelled lifted source certificate and seed,
not just the complete circle pinbed. The program retains those rational
certificates explicitly.

The coherent real wrong seed s=-pi/16 has completed orbit identically zero
and Green-tail shadow `U_n(s)=-T_n`. It retains the same forcing but
fails every nontrivial equidistribution target. This real seed is not a
rational finite-prime state; its use here is solely a countermodel to
source-forcing-only or chart-only arguments.

Cayley transport preserves each signed Weyl mode exactly. Consequently
transport alone cannot improve a Weyl cancellation estimate. It can improve
which instrument is available and how its error is certified. The next
verdict-changing arithmetic input remains an original-zero signed estimate,
with the parity boundary payments handled separately in this dossier.

## Verification scope

`python -m unittest discover -s tests -p 'test_cayley_source_observer.py' -v`
passes **18 exact tests** in the present checkout. Tests compare projective
powers with an independent binomial oracle; cover poles, infinity, negative
frequencies, declared rotations and invalid exact inputs; compare source
prefixes with the four-pole formula; verify finite naturality and nesting;
check minimal paid horizons; certify the hostile quadratic mode; and compare
the clipped epoch budget with a literal independent geometric sum.

The code tests are finite regression evidence. The universal asymptotic
claims rest on the proofs above. Full repository validation and hosted CI
are reported separately by the integration round.
