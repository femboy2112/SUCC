# Constructor: fixed-carrier echoes and source-frequency resolution

Date: 2026-11-15. Parent `85a14bb68aeae31d3a2796350529fda9a5c39072`.
Branch `research/pi-carrier-collision-2026-11-15`.

## Verdict, dependency cut and provenance

**PROVED within the stated model:** matched integer echoes retain a fixed
target frequency while scanning the authentic forcing. The forcing nodes on
a length-B shell have minimum spacing asymptotic to `15/(256 B^3)`. Gamma--
Poisson and bounded triangular frequency laws therefore give stable population
frames with frequency spread of order B^3. A variance bound proves a matching
order obstruction for a uniformly stable unrestricted coefficient-vector
inverse. A large frequency offset alone cannot repair this obstruction.

**PROVED diagnostic:** in a well-resolved frame the total raw response energy
is approximately `1/B` for every unit-modulus carrier, including the locked
carrier. It is therefore not evidence of the original signed cancellation.
An oriented residual from the locked response instead reconstructs the
real-escape statistic up to explicit stable constants. Its all-scale positive
lower bound is equivalent to the already open R0 rung; no weaker arithmetic
premise has been discharged.

**OPEN:** a uniform positive source-selected R0 escape density; all-mode Weyl
decay; pi normality. No new arithmetic saving is claimed. No physical meaning
of the frequency or variance parameter as energy has been established.

Source reconstruction preceded new construction. Read:

- `docs/PI_NORMALITY_FRONTIER.md`, especially the authenticated origin, exact
  Green completion and Main XXV rung ladder; `docs/PI_FRONTIER_CONTRACT.md`.
- `research/2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md` and
  `observational_succ/bbp_echo_delay_transport.py`: arbitrary integer filter
  division, seed erasure, moving coefficient budgets and completed-orbit
  transport already exist. These identities are not a new result of this round.
- `research/2026-10-25/SUCC_INTERNAL_MATRIX_WALK.md`, IMW-04/05: the forcing
  B^2 scale and adjacent-difference B^3 scale already exist.
- `research/2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md`, IAD-03
  through IAD-06, and its `OBSTRUCTIONS.md`: untwisted forcing cancellation
  and the precise failure of the innovation/history split to pay the selected
  signed estimate. A source-independent chirp cannot establish normality.
- `observational_succ/bbp_resonant_lags.py`, `mixed_lag_coercivity.py`,
  `bbp_binwindow_conjugacy.py`, `duck_bbp.py`, and the existing volume algebra.
- `research/2026-10-27/GLOBAL_BRANCH_COERCIVITY.md`, GB-12, for the later
  bounded review of root's PC-09 detection corollary.

The increment is the quantitative source-frequency frame, recovery/precision
accounting, lower variance obstruction and oriented escape calibration.
The finite triangular frame was derived independently by this constructor;
the Gamma--Poisson choice was supplied by root and its constants were checked
here. Both use classical characteristic functions, frame algebra and row-sum
bounds. No independent academic-priority claim is made. No other current-round
agent's scratch work was read.

## CF-01. Exact carrier-retaining and erasing filters

Keep the original four-pole forcing and literal zero seed:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Let `E` be the forward shift. For every finite integer polynomial `P`, divide

\[
P(X)=P(16)+(X-16)Q(X),\qquad Q\in\mathbb Z[X].
\]

Since `(E-16)U_n=r(n+1)`, this gives the inherited exact identity

\[
P(E)U_n=P(16)U_n+Q(E)r(n+1).                            \tag{1}
\]

It holds at every finite clock and for every real seed in the same recurrence.
Changing the seed by `s` changes the output by `P(16)16^n s`. Thus `P(16)=0`
is exactly seed independence of the unwrapped filter for all seeds; a nonzero
symbol retains a homogeneous carrier coefficient. This does not make the
complex character injective in the seed: integer and rational phase aliases
remain. The original seed is authenticated independently by the source path.

In particular, the two integer taps

\[
(a_0,a_1)=(h-16K,K)
\]

give

\[
a_0U_n+a_1U_{n+1}=hU_n+K r(n+1).                       \tag{2}
\]

Here `h` stays fixed as the integer probe parameter `K` grows. Choosing
`(-16K,K)` instead erases the target, not just a nuisance term. The code
permits `h=0` solely as an explicit erasure control and labels it accordingly.

For any nonnegative finite taps with total absolute coefficient mass `V_B`
on the shell `B<=n<2B`, the inherited tail bound `T_n<1/(64n^2)` gives

\[
\sup_{B\le n<2B}
|e(P(E)U_n)-e(P(16)(U_n+T_n))|
\le\frac{\pi V_B}{32B^2}.                              \tag{3}
\]

Here “nonnegative taps” refers to lag indices, not coefficient signs; integer
coefficients may have either sign. Formula (3) follows by expanding the full
tail `sum a_j T_(n+j)` and using `|e(x)-e(y)|<=2pi|x-y|`. The bound is uniform
in the nonnegative lags. Thus filters with `P(16)=h` and `V_B=o(B^2)` are
asymptotically the same fixed target on shells. This is a shell specialization
of inherited Green/filter transport, not a signed source estimate.

## CF-02. What K of order B^2 actually does

Write `t_n=r(n+1)`. The inherited IMW bound is

\[
0<\frac{15}{64}-n^2t_n<\frac7{5n}\qquad(n\ge1).
\]

If `K_B/B^2 -> tau` is bounded, then uniformly for `B<=n<2B`,

\[
K_Bt_n-\frac{15\tau}{64(n/B)^2}\longrightarrow0.        \tag{4}
\]

Indeed the absolute error is at most
`7|K_B|/(5B^3)+(15/64)|K_B/B^2-tau|`. Thus this scale creates a known smooth
source chirp. It does not make the original target phase random.

For `q_n=e(K_Bt_n)`, monotonicity of `t_n` implies

\[
\operatorname{Var}_{[B,2B)}q
\le2\pi|K_B|(t_B-t_{2B-1})
\le\frac{30\pi |K_B|}{(8B+1)(8B+2)}.                   \tag{5}
\]

Let `z_n` be any bounded sequence and compare its partial sums from B with
those of `q_n z_n`. Abel summation, and then the same argument for `conj(q_n)`,
give

\[
\max_m\left|\sum_{n=B}^m q_nz_n\right|
\le(1+\operatorname{Var}q)\max_m\left|\sum_{n=B}^m z_n\right|,
\]

and the reverse inequality with the same factor. Thus at bounded `K_B/B^2`,
uniform partial-sum cancellation is equivalent before and after modulation.
This statement concerns all shell partial sums; cancellation of one weighted
whole-shell average alone is not asserted equivalent. At larger intensity the
variation factor grows and must be paid. This is the existing signed debt,
not an independent route around it.

## CF-03. Sharp source-node spacing from the four poles

The exact polynomial identity gives

\[
t_n=\int_0^1x^{8n}(1-x)A(x)\,dx,
\qquad A(x)=x^4+2x^3+4x^2+4x+4.
\]

For `0<=x<=1`, each monomial of degree at most four is at least `x^4`, so
`15x^4<=A(x)<=15`. Also

\[
8x^7\le1+x+\cdots+x^7\le8.
\]

Subtract consecutive moments and bound their positive integrands:

\[
120\!\int_0^1x^{8n+11}(1-x)^2dx
\le t_n-t_{n+1}
\le120\!\int_0^1x^{8n}(1-x)^2dx.
\]

Using the elementary beta integral yields, for every integer `n>=0`,

\[
\frac{240}{(8n+12)(8n+13)(8n+14)}
\le t_n-t_{n+1}
\le\frac{240}{(8n+1)(8n+2)(8n+3)}.                     \tag{6}
\]

The difference is positive and strictly decreases with n, since multiplying
the positive difference integrand by `x^8` strictly reduces its integral.
For `B>=2`, the closest nodes on `B,...,2B-1` are the last adjacent pair:

\[
\delta_B=t_{2B-2}-t_{2B-1},\qquad
d_B:=\frac{240}{(16B-4)(16B-3)(16B-2)}\le\delta_B.
\tag{7}
\]

For any two shell indices,

\[
|t_n-t_m|\ge d_B|n-m|.                                 \tag{8}
\]

Also

\[
0<t_{2B-1}<t_B\le\frac{15}{(8B+1)(8B+2)}\le\frac16<\frac12.
\]

Thus every pairwise difference has absolute value below one half and equals
its circle distance. No wrapping assumption is omitted. Squeezing (6), and
the analogous moment bounds
`15/[(8n+5)(8n+6)]<=t_n<=15/[(8n+1)(8n+2)]`, proves

\[
t_n\sim\frac{15}{64n^2},\qquad
\delta_B\sim\frac{15}{256B^3}.                          \tag{9}
\]

The rational certificate computes the exact last gap from the inherited source
adapter and returns both polynomial bounds. It does not scan a shell to guess
its minimum. A deleted-pole control violates the authentic cubic upper bound;
the cancellation of all four source channels matters.

## CF-04. Population frames and two admissible integer clock laws

Let `c in C^B`, and define

\[
F_c(K)=\frac1B\sum_{n=B}^{2B-1}c_n e(Kt_n),\qquad
v_K=(e(-Kt_n))_n,\qquad G=E[v_Kv_K^*].                 \tag{10}
\]

Then `F_c=v_K^*c/B` and
`G_nm=E[e(K(t_m-t_n))]`. Complex conjugation is fixed throughout; the outputs
must retain their orientation, not just their magnitudes. Diagonal entries
are one. The following row estimates are uniform over all coefficient vectors.

### A. Gamma--Poisson shape two

Choose an auxiliary positive clock `T~Gamma(shape=2,scale=Lambda)`, and,
conditional on T, an integer `K~Poisson(T)`. For `Lambda>0`, direct integration
gives

\[
P(K=k)=\frac{(k+1)\Lambda^k}{(1+\Lambda)^{k+2}},\qquad
m(u):=E[e(Ku)]=[1+\Lambda(1-e(u))]^{-2}.                \tag{11}
\]

Equivalently K is the sum of two independent geometric counts on the
nonnegative integers. Its mean is `2Lambda` and variance
`2Lambda(1+Lambda)`. With `q=Lambda/(1+Lambda)`, the exact tail is

\[
P(K>L)=q^{L+1}[(L+2)-(L+1)q].                          \tag{12}
\]

These are external probe laws, not an identification of the original Oily
source law with a new latent Gamma coupling. Scale zero is represented only
as the separate degenerate point-mass control, not an ordinary Gamma density.

For `|u|<=1/2`,

\[
|m(u)|=\frac1{1+4\Lambda(1+\Lambda)\sin^2(\pi u)}
\le\frac1{1+16\Lambda(1+\Lambda)u^2}.                  \tag{13}
\]

Use (8), sum at most two terms at each integer separation, and use
`sum_(j>=1)j^-2<2`. Every off-diagonal row sum is strictly less than

\[
\eta_\Gamma=\frac1{4\Lambda(1+\Lambda)d_B^2}.           \tag{14}
\]

Hence the Hermitian row-sum bound gives

\[
(1-\eta_\Gamma)I\preceq G\preceq(1+\eta_\Gamma)I.
\]

Taking `Lambda=ceil(1/d_B)` certifies `eta_Gamma<=1/4`, with mean frequency
of order B^3. Infinite support is paid through (12); silently truncating the
law changes the Gram. A deterministic integer offset multiplies the
character by a unit phase and only diagonally unitarily conjugates G.

### B. A fully bounded triangular law

Choose independent uniform integers U,V in `0,...,M-1` and set
`K=offset+1+U+V`, with integer `offset>=0`. The support is the strictly
positive finite band `offset+1,...,offset+2M-1`, with exact probabilities

\[
P(K=k)=\frac{\max(0,M-|k-offset-M|)}{M^2}.              \tag{15}
\]

Its mean is `offset+M`, and its variance is `(M^2-1)/6`. The character is

\[
E[e(Ku)]=e((offset+M)u)
 \left(\frac{\sin(\pi Mu)}{M\sin(\pi u)}\right)^2.      \tag{16}
\]

At removable singularities use the finite-sum formula. For distinct source
nodes, (8) and `|sin pi u|>=2|u|` bound each off-diagonal magnitude by
`1/[4M^2d_B^2|n-m|^2]`. Thus every row sum is strictly less than

\[
\eta_F=\frac1{M^2d_B^2}.                               \tag{17}
\]

Taking `M=ceil(2/d_B)` gives `eta_F<=1/4` and a deterministic maximum
frequency of order B^3 when the offset is zero. This is an independent
bounded positive clock law; it is not a truncation of the Gamma law.

For either law with `eta<1`, the analysis-frame condition number is at most
`sqrt((1+eta)/(1-eta))`, at most `sqrt(5/3)` for the recommended scales.
The Gram's condition number is the square of this. The implementation exposes
the squared analysis condition number explicitly to avoid confusing them.

## CF-05. A matching order obstruction uses frequency variance

Let any probability law on K have finite variance V. Its mean need not be
small, and its support need not be bounded. Put `m(u)=E[e(Ku)]`. The two
closest columns give a principal Gram block with eigenvalues `1+|m(delta_B)|`
and `1-|m(delta_B)|`. Since centering changes only a unit phase,

\[
\begin{aligned}
1-|m(\delta_B)|
&\le1-\Re E[e((K-EK)\delta_B)]\\
&\le2\pi^2\delta_B^2 V,
\end{aligned}
\]

by `1-cos x<=x^2/2`. Testing a vector supported on these two columns proves

\[
\lambda_{\min}(G)\le2\pi^2\delta_B^2 V.                \tag{18}
\]

The code uses `pi<22/7` to return the rational upper bound
`min(1,(968/49)delta_B^2 V)`; `lambda_min<=1` follows from the unit diagonal.
By (9), `V=o(B^6)` forces the minimum eigenvalue to zero. Consequently a
uniform lower frame bound requires frequency standard deviation of order at
least B^3. Gamma scale `o(B^3)` and triangular width `o(B^3)` fail that test.

Translating a law by any integer, including a diverging offset, sends G to
`D^*GD` for a diagonal unitary D. It changes neither the spectrum nor V.
Thus arbitrarily large central intensity with small spread does not resolve
the adjacent source columns. Tests preserve that orientation change while
checking identical singular values.

**Boundary:** this is a uniform linear inverse bound for unrestricted complex
coefficient vectors. It is not a computational lower bound for the already
specified pi source, a lower bound for every estimator of the single mean,
or a claim about the nonlinear one-parameter family of all same-forcing seeds.
The known original source has additional structure not used by this frame
bound. No unsupported impossibility claim is attached to that structure.

## CF-06. Recovery, source precision and universal energy

For `eta<1`, exact orientation-retaining recovery is

\[
c=B G^{-1}E[v_KF_c(K)].                                \tag{19}
\]

This follows by substituting (10): the expectation is `Gc/B`. For a finite
design with positive empirical Gram, replace expectations by sample averages.
The representation itself supplies no cheaper instrument for computing the
coherent aggregate than accessing the underlying phases.

Let the actual population analysis operator send c to `v_K^*c`, in `L^2`
of the clock law. Its Gram is G. If normalized aggregate reports F have
additive error e with weighted squared mean `epsilon^2=E|e|^2`, canonical
least-squares reconstruction has

\[
\|\widehat c-c\|_2\le\frac{B\epsilon}{\sqrt{1-\eta}},
\qquad
\left|\frac1B\sum_n(\widehat c_n-c_n)\right|
\le\sqrt{\frac B{1-\eta}}\,\epsilon.                  \tag{20}
\]

The first bound uses the inverse singular-value bound; the second uses that
the averaging functional has norm `1/sqrt(B)`. Finite-design formulas are
identical with weighted mean-square error replaced by the sample mean and
the lower Gram eigenvalue substituted. These are deterministic error bounds;
they are not shot-noise promises for an unprovided physical instrument.

For a source-node error at most epsilon_t, each individual modulation has
complex error at most `2pi|K|epsilon_t`. If the two original states instead
have separate error bounds epsilon_n and epsilon_(n+1), the exact tap bound is

\[
2\pi\bigl(|h-16K|\epsilon_n+|K|\epsilon_{n+1}\bigr).    \tag{21}
\]

No probabilistic independence of these errors is needed. A large offset
therefore costs source precision even though it does not improve conditioning.
The implementation returns the rational coefficients of pi in these bounds.
Exact rational evaluation followed by reduction modulo one avoids avoidable
floating-point subtraction loss; it does not authenticate an empirical source
law or remove actual sensor error.

### Why total detector energy can look excellent on a locked orbit

For every complex vector,

\[
\frac{1-\eta}{B^2}\|c\|_2^2
\le E|F_c(K)|^2\le\frac{1+\eta}{B^2}\|c\|_2^2.          \tag{22}
\]

In particular, when each `|c_n|=1`,

\[
\frac{1-\eta}{B}\le E|F_c(K)|^2\le\frac{1+\eta}{B}.     \tag{23}
\]

This holds for the authentic `c_n=e(hU_n)`, every changed seed with the same
forcing, and the locked coefficient vector `c=1`. In the last case the target
mean is exactly one. The small response energy is supplied by the resolving
probe law, not by target cancellation. Moreover `c` and `-c` have identical
raw output magnitudes at every K, so magnitudes alone cannot recover the
oriented real-escape statistic.

The actual coherent same-forcing seed is `s=-pi/16`, giving `U_n(s)=-T_n`.
Its unit phase vector also obeys (23), whereas

\[
A_B^{\rm counter}:=\frac1B\sum_n(1-\Re e(-hT_n))
\le\frac{\pi^2h^2}{2048B^4},                           \tag{24}
\]

using `T_n<1/(64n^2)`. This changed seed is a source-blindness diagnostic;
it is not a counterexample to the literal zero seed. The finite test retains
all four poles and uses the exact rational finite-future seed `-T_(0,L)`;
its state equals `-T_(n,L)` and approximates the coherent boundary with a paid
geometric remainder. It is explicitly labelled as a different seed.

## CF-07. An oriented collision residual is a calibrated R0 detector

Let `F_1(K)` be the known response for the locked vector, and retain the
complex difference

\[
D_B:=E|F_c(K)-F_1(K)|^2.
\]

For unit-modulus c, the desired real escape is

\[
A_B=\frac1B\sum_n(1-\Re c_n)=\frac{\|c-\mathbf1\|_2^2}{2B}.
\]

Apply the frame inequality to `c-1`, not separately to the two energies:

\[
\frac{2(1-\eta)}B A_B\le D_B\le\frac{2(1+\eta)}B A_B.
\]

Equivalently,

\[
\boxed{\frac{B D_B}{2(1+\eta)}\le A_B
\le\frac{B D_B}{2(1-\eta)}.}                           \tag{25}
\]

The missing mixed term is essential:
`D_B=E|F_c|^2+E|F_1|^2-2Re E[F_c conj(F_1)]`.
The difference of the two raw energies is not D_B and need not be positive.
The global phase inversion control preserves every raw energy while changing
escape. For the coherent counterseed (24), the upper side of the residual
comparison gives `D_B=O_h(B^-5)` despite raw energy of order `1/B`.

For any uniformly stable design family `eta_B<=eta_0<1`, the existence of
constants `epsilon>0,B0` with `D_B>=epsilon/B` for all `B>=B0` is equivalent,
up to the explicit constants in (25), to the R0 lower escape bound for h=1.
It does not become a weaker arithmetic edge merely because it is measured
by an external randomized instrument. A source-derived lower bound of this
size remains the next required lamp.

## Implementation and finite controls

Assigned files only:

- `observational_succ/bbp_collision_frame.py`.
- `tests/test_bbp_collision_frame.py`.
- This note.

The implementation imports `source_verified` and `authentic_state`; the
original source and zero initialization are not copied into a new mutable
engine. Tests reconstruct the four literal poles independently. Source-shell
certificates use constant-size rational calculations, with shell B capped at
100000. Actual unwrapped echo replay is capped at clock 512. Exact probability
indices and tail cutoffs are capped at 4096. Large triangular supports are
represented symbolically; calculating a probability does not enumerate them.
Input integer/rational bit sizes are not asserted uniformly bounded.

Probability, source and certificate inputs reject floats and booleans.
Unstable certificates expose their nonpositive lower bound and refuse inverse
gain properties. The finite proof checks include source holdouts, deletion of
a source channel, exact seed-erasure mutations, independent geometric and
uniform-pair clock constructions, closed versus truncated Gamma characters,
explicit finite complex Gram energies, original and coherent-boundary carriers,
oriented residuals, global phase inversion, central-frequency shifts, and the
small-variance obstruction. Numerical complex calculations are finite checks,
not substitutes for the bounds proved above.

No full suite, branch change, commit or publication was initiated by this
constructor. Root owns random finite-frame concentration and integration.

## Bounded review of root synthesis

Initial review of PC-01--06 confirmed the source spacing, Gamma and triangular
constants, the `v_K=e(-Kt)` convention, whitening in the matrix-Chernoff
argument, the lower variance obstruction and the recovery dimension factors.
Necessary clarifications sent to root: explicitly assume `eta<1` before
population inversion; explicitly normalize the sample data vector as
`y_j=(F(K_j)+e_j)/sqrt(s)`; state `0<delta<1` for confidence budgets. The
averaging functional has norm `1/sqrt(B)`. The oriented residual comparison
(25) is to be integrated as the calibrated R0 equivalence, not as a new saving.

The PC-09 detection calculation agrees with the actual inherited GB-12:
block loss greater than `1/14` over `7m` times gives phase-coin acceptance
greater than `1/(196m)`. The same-forcing coherent seed has acceptance at most
`pi^2 h^2/[4096(m+1)^4]`. Therefore order `m log m` fresh trials give the stated
fixed-h separation, conditional on the inherited unextracted onset. This
corollary improves neither the arithmetic block loss nor its onset.

### Closing receipt — 2026-11-15

**Bounded PASS: PC-01 through PC-06 and PC-09.** The reviewed bytes of
`THEOREMS.md` have SHA256
`03938f2d19125d214ad2e517982365d4f73f33fe8a264a6ef3278741d3021e1b`.
This receipt does not extend the proof review to PC-07, PC-08 or PC-10.

All necessary corrections from this constructor's review are resolved in
that snapshot. PC-06 explicitly assumes `0<=eta<1` before inversion,
normalizes the observations as `y_j=[F(K_j)+e_j]/sqrt(s)`, and includes
both recovery dimension factors. The oriented detector retains the complex
cross term, and its equivalence to R0 now explicitly requires a family
with a uniform margin `eta_B<=eta_*<1`. Confidence statements include
`0<delta<1`. The finite-row concentration bound is conditional on the
stated independent sampling and authentic source nodes; it is a frame
statement, not a signed arithmetic estimate. PC-09 preserves the inherited
GB-12 onset qualification, fixed-h asymptotic scope, original zero seed,
and status of the changed-seed family as a diagnostic control.

The constructor's final focused execution was
`python -m unittest tests.test_bbp_collision_frame -v`:
**21 tests passed in 0.141 seconds**. This is the already completed run;
no tests were rerun for this closing receipt. The production and test
files are frozen at:

| File | SHA256 |
| --- | --- |
| `observational_succ/bbp_collision_frame.py` | `6df7e69e0d5d121c526af8f767a01ca3415ec56d54ae2a5f35b0dfd028cb8eaf` |
| `tests/test_bbp_collision_frame.py` | `d0f15bb435b35cc724e4ba4271f6fa16aab262105108f6a0e2e73d108cb443ad` |

Only this owned note was amended during closure. Root owns the integrated
suite, independently implemented numerical diagnostics, and publication.
The formal source spacing, coherent reconstruction and calibrated detector
are established within their stated domains; an authentic all-scale R0
lower bound and normality remain open.
