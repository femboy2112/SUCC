# Euler--Mascheroni as a source interface: SUCC, refinement, pi, and RH

**Research round:** October 24, 2026. **Main baseline:**
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Verdict:** coherent finite constructions, proved cutoff and transport
theorems, explicit countermodels, and reproducible finite certificates.
**Pi normality and RH remain open.** No scholarly-priority claim and no new
Lean-kernel authority are asserted.

The user's formula is correct for the stated order of limits:

$$
\gamma=\lim_{r\downarrow1}\sum_{k\ge1}(k^{-r}-r^{-k})
       =\lim_{r\downarrow1}\left(\zeta(r)-\frac1{r-1}\right).
$$

Its useful extension is the full regularized, shifted, and geometrically
weighted source family. This round makes those extensions concrete and
identifies which operations preserve the original arithmetic data.

## Read the results by mathematical question

| Question | Complete proof / artifact | Earned result |
|---|---|---|
| How does gamma arise from finite successors, and how do refinements compose? | [Successor and refinement](EULER_MASCHERONI_SUCCESSOR_REFINEMENT.md) | Exact finite boundary repair; uniform remainder; shifted Hurwitz successor and affine integer refinement; positive kernel and finite-jet controls |
| Does this family actually contain the unchanged BBP source? | [BBP regulator](EULER_MASCHERONI_BBP_REGULATOR.md) | Exact finite Lerch embedding; uniform positive-exponent tail; explicit noncommuting endpoint with cofinal limits |
| What would its character-weighted version need to prove about pi? | [Character Tauberian bridge](EULER_MASCHERONI_CHARACTER_TAUBERIAN.md) | Exact two-time-dilation criterion; source transport; one-scale and local-germ counterexamples; four rigorous actual-source windows |
| How does the Stieltjes hierarchy reach RH without losing completion? | [Completed Li bridge](EULER_MASCHERONI_COMPLETED_LI.md) | Classical completed coefficient map; three rational sign certificates; uniform all-degree cutoff bound; explicit finite-jet source counterfeit |
| What is asserted, and at what scope? | [EMS claim supplement](../../docs/CLAIM_SUPPLEMENT_EULER_MASCHERONI.md) | Separate paper, classical, finite, refuted, and open entries |
| Can the finite work be replayed? | [Probe](../../scripts/euler_mascheroni_probe.py), [receipt](euler_mascheroni_validation/probe_receipt.json), [validation](EULER_MASCHERONI_VALIDATION.md) | Exact rational/integer checks with a local source-file manifest |

The four new implementation modules depend only on current main. The recent
sibling drafts were inspected at pinned heads, not merged or silently made
runtime dependencies. The [start-state record](EULER_MASCHERONI_START_STATE.json)
contains every reviewed head and the observed CI snapshot; the
[hole contract](EULER_MASCHERONI_HOLE_CONTRACT.md) records the initial tests of
the proposed interpretation.

## 1. Reconstructed recent frontier

The initial review covered all 18 recent open PR descriptions, #266 and
#268--#284, with selected proof/source files opened. A final live check found
the newly available gamma-specific #285, whose dossier, implementation and
claim supplement were then read at its exact head. The final scope is
19 recent open drafts. This is a review of the recent research frontier,
not a claim to have re-proved every theorem in every sibling.

| Recent work | What it contributes | Consequence for this gamma round |
|---|---|---|
| [#266](https://github.com/femboy2112/SUCC/pull/266), [#268](https://github.com/femboy2112/SUCC/pull/268) | Lag/carry controls, selected collisions, signed twisted transport, and first-saving targets | A source-specific signed estimate is still required; a positive or invariant model is insufficient |
| [#269](https://github.com/femboy2112/SUCC/pull/269), [#270](https://github.com/femboy2112/SUCC/pull/270) | Four dyadic gates and conditional base-three rigidity | A dyadic residue refinement is not a proof of real-orbit frequency; this round's 2/3 theorem concerns time windows, not circle invariance |
| [#271](https://github.com/femboy2112/SUCC/pull/271), [#272](https://github.com/femboy2112/SUCC/pull/272) | Pascal/Walsh jets, prime filters, carry information | Four-way information cannot be replaced by lower marginals; retaining gamma alone similarly discards the shifted/character data |
| [#273](https://github.com/femboy2112/SUCC/pull/273), [#274](https://github.com/femboy2112/SUCC/pull/274) | Path selection and Pascal/Lucas quotient obstructions | Every coordinate change must retain the selected initial state and source indices |
| [#275](https://github.com/femboy2112/SUCC/pull/275), [#276](https://github.com/femboy2112/SUCC/pull/276) | Weighted ternary charts and a source-coherence Tauberian bridge | Exact finite refinements are useful; the asymptotic selection premise remains separate |
| [#277](https://github.com/femboy2112/SUCC/pull/277) | Joint four-pole CRT and noncommuting all-prime limits | Motivates explicit cofinal clocks; the new BBP exponent/cutoff theorem provides another source-labelled limit-order diagnostic |
| [#278](https://github.com/femboy2112/SUCC/pull/278) | Trimmed joint entropy Hypothesis A | Remains an alternative sufficient source-selection route; it is not proved by this round |
| [#279](https://github.com/femboy2112/SUCC/pull/279) | Exact twisted-pair differential and source-anchor decoding | An exact decoder retains information but supplies no cancellation theorem by itself |
| [#280](https://github.com/femboy2112/SUCC/pull/280) | Rational-base 11/10 carries and signed decimal transport | No promotion from the base-16 source criterion to decimal or absolute normality |
| [#281](https://github.com/femboy2112/SUCC/pull/281), [#282](https://github.com/femboy2112/SUCC/pull/282) | Natural/integer internal BBP carriers and exact recurrence readouts | Confirms the correct comparison is the original zero-initial recurrence, even in another carrier |
| [#283](https://github.com/femboy2112/SUCC/pull/283), [#284](https://github.com/femboy2112/SUCC/pull/284) | Sharp growing-lag errors and harmonic mirror/Fejer weights | The improved error budget still leaves selected signed interference open; harmonic lag weights and our harmonic time windows are different constructions |
| [#285](https://github.com/femboy2112/SUCC/pull/285), head `f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad` | Generalized Euler boundary, centered cell tails, genuine-prime cofinality, theta completion and exact Basel/hex prefixes | Prior/sibling source for overlapping regularization; its centered remainder yields the sharper completed-Li cutoff corollary below. [Full reconciliation](EULER_MASCHERONI_PR285_RECONCILIATION.md). |

Main's prescribed-scale collision target remains
$K_p(1)=p^{o(1)}$ at $c=2/5$ (SCE-07), unverified. The sibling trimmed-entropy
route relaxes the sufficient hypothesis but does not prove it. The newest
harmonic mirror branch retains a source error of the form

$$
\frac{88|h|}{1575}\frac{16^K}{N H_K K^3},
$$

allowing a larger logarithmic lag cutoff while leaving the signed aggregate
uncontrolled. None of these earlier open claims changes status here.

The immediately preceding gamma chat already identified
$G(s)=\zeta(s)-1/(s-1)$ and warned that a finite Euler product cannot have the
pole subtracted before its source cutoff is taken. Those are prior context,
not discoveries attributed to this round. Its raw $s=0$ successor limit is
$1$, whereas the continued $G(0)=1/2$. At the initial review no exact
repository artifact for that chat was available. The later #285 supplies
that concrete research context, now pinned and reconciled separately.

The older Gamma-function path, Tate remainder and completion modules remain
distinct from Euler's constant. Baseline tests of `gamma_succ_path`,
`mobius_tate_gamma_remainder` and `tate_idelic_zeta` passed before integration.
The new work joins those completion requirements to the Euler--Mascheroni
finite part without conflating $\gamma$ and $\Gamma$.

## 2. The first substantive result: repair the two clocks exactly

Define the literal equal-cutoff sum and a continuum-compensated successor sum:

$$
T_N(r)=\sum_{k=1}^N(k^{-r}-r^{-k}),\qquad
B_N(r)=\sum_{k=1}^Nk^{-r}-\int_1^Nx^{-r}\,dx.
$$

For $r>1$,

$$
B_N(r)=T_N(r)+\frac{N^{1-r}-r^{-N}}{r-1}.
$$

The correction has removable value $N-\log N$ at $r=1$. The compensated
construction obeys, for every real $r\ge1$,

$$
0<B_N(r)-G(r)<N^{-r}\le N^{-1}.
$$

The raw construction has no such uniform convergence: at $r=1+1/m$ and
$N=m^m$, it tends to $\gamma-1$. More generally, a critical cofinal clock
$\varepsilon\log N-\log(1/\varepsilon)\to c$ yields
$T_N(1+\varepsilon)\to\gamma-e^{-c}$.

This is a concrete SUCC operation: each finite stage has an exact boundary
defect, and the defect is retained under passage to the limit. It also
explains why a regularized scalar identity cannot be applied to arbitrary
weighted observations. The normalized power-law and geometric clocks have
total variation tending to one; equality of their total leading masses
does not identify their sampling of a selected sequence.

## 3. The actual FUCC/refinement structure

Use $G(s,a)=\zeta(s,a)-1/(s-1)$ and

$$
B_N(s,a)=\sum_{n=0}^{N-1}(n+a)^{-s}-\int_1^Nx^{-s}\,dx.
$$

At finite horizons the successor law keeps its endpoint:

$$
B_N(s,a+1)-B_N(s,a)=(N+a)^{-s}-a^{-s}.
$$

Integer refinement is also exact:

$$
\frac1p\sum_{j=0}^{p-1}B_N\!\left(s,\frac{a+j}{p}\right)
=p^{s-1}B_{pN}(s,a)+\frac{p^{s-1}-1}{s-1}.
$$

Thus the induced affine maps
$\mathcal A_p(x)=p^{s-1}x+(p^{s-1}-1)/(s-1)$ obey
$\mathcal A_p\mathcal A_q=\mathcal A_{pq}$. The removable anomaly is
$\log p$ at $s=1$. Prime and composite refinements share this source law;
prime-specific arithmetic must be added through genuine source data.

The same family has a positive transform

$$
\frac{G(s)}s=\int_0^\infty(1-\{e^y\})e^{-sy}\,dy,
\qquad \Re s>0.
$$

This yields unconditional positive Gram kernels and moments
$m_j=j!\sum_{k=0}^j\gamma_k/k!$. The full positive moment hierarchy determines
its measure. Every fixed finite hierarchy admits explicit positive
Legendre-polynomial perturbations with the same observed moments and a
different next moment. These controls change the source, and no positive
kernel here has been identified with the signed completed Weil form.

## 4. A genuine BBP connection, with an exact limit-order theorem

The shifted Lerch family at $z=1/16$ and $s=1$ is exactly the original BBP
series. This is proved by a finite source-index identity, not by a fit to
known pi digits. Its unregulated exponent family has

$$
\frac{15}{8}(8N+6)^{-s}
<\sum_{n>N}r_s(n)
<\frac{15}{8}(8N-7)^{-s},\qquad s>0.
$$

The entire Hurwitz continuation gives $B(0)=15/8$, while $r_0(n)=0$ at every
finite index. Consequently

$$
s\log N\to c,\quad s\downarrow0,\ N\to\infty
\quad\Longrightarrow\quad
\sum_{n\le N}r_s(n)\to\frac{15}{8}(1-e^{-c}).
$$

At $s=1/m,N=2^m$ the limit is $15/16$. This is proved for all such cofinal
sequences by the tail squeeze. It does not imply any digit-frequency result,
because $s\ne1$ changes the original forcing.

Reflection also gives $G(1,1/4)-G(1,3/4)=\pi$. In this difference the common
gamma term cancels. Therefore neither this identity nor the BBP embedding
says that knowing the scalar gamma determines the required digit statistics.

## 5. The pi route: two harmonic time windows

For a bounded complex sequence $a_n$, set

$$
W_p(N)=\sum_{N<n\le pN}\frac{a_n}{n}.
$$

The complete proof in the character note establishes

$$
\boxed{\frac1N\sum_{n\le N}a_n\to0
\quad\Longleftrightarrow\quad
W_2(N)\to0\ \hbox{and}\ W_3(N)\to0.}
$$

The forward implication is partial summation. The reverse implication uses
the exact dilation cocycle, density of $2^{\mathbb Z}3^{\mathbb Z}$, a
logarithmic continuity bound, and dominated convergence. No invariance of
circle measures is assumed. An explicit dyadic log-periodic sequence passes
the doubling condition and has nonzero ordinary mean; tripling detects it.

For the actual $a_n=e(hU_n)$, $e(x)=\exp(2\pi i x)$, source transport costs
at most

$$
\frac{33|h|}{896N^2}\quad(p=2),\qquad
\frac{11|h|}{252N^2}\quad(p=3).
$$

The corresponding all-horizon limits for every fixed nonzero integer $h$
are therefore equivalent to base-16 pi normality. That is a proved
reformulation with an explicit authentic-source error, not a cancellation
proof. It concerns base-16, hence base-2 normality; decimal and absolute
normality require additional arguments.

The actual four rational interval observations are:

| $N$ | $p$ | Enclosure for $|W_p(N)|$, $h=1$ |
|---:|---:|---:|
| 32 | 2 | $[0.035688976370,0.035688976371]$ |
| 32 | 3 | $[0.090656713295,0.090656713296]$ |
| 128 | 2 | $[0.065276411366,0.065276411367]$ |
| 128 | 3 | $[0.061958856714,0.061958856715]$ |

These exact outward enclosures refute monotone decay of the doubling-window
magnitude at the two tested scales. They neither refute nor prove the limit.

An analytic alternative retains
$D_h(s)=\sum_{n\ge1}e(hU_n)n^{-s}$. The source-to-pi difference continues
holomorphically to $\Re s>-1$. A sufficiently regular boundary on the entire
line $\Re s=1$ would imply cancellation by classical Tauberian theory. A
regular germ at $s=1$ alone does not: the bounded sequence $a_n=n^{it}$ has
$D(s)=\zeta(s-it)$, regular at one for $t\ne0$, but a nonvanishing mean.
The off-axis boundary pole is the missing information.

## 6. The RH route: completed coordinates and a quantified cutoff

The full Stieltjes jet

$$
G(1+z)=\sum_{m\ge0}\frac{(-1)^m\gamma_m}{m!}z^m
$$

enters the actual completed function through

$$
\xi(1+z)=\frac12(1+z)\pi^{-(1+z)/2}
\Gamma\!\left(\frac{1+z}{2}\right)[1+zG(1+z)].
$$

The new evaluator constructs Stieltjes intervals from finite integer
successors and monotone tails, then applies the classical formal-log and
Li transforms while retaining the Gamma, pole, and pi terms. At cutoff 512
it certifies positivity of $\lambda_1,\lambda_2,\lambda_3$. This is a
calibration of a reusable source instrument, not a new positivity frontier.

There is also a paper theorem uniform in the coefficient degree. Let
$\lambda_n^{(N)}$ replace only $G$ by $B_N$ in the displayed product, with
the actual Gamma and pi completion fixed. Then for all integers $n,N\ge1$,

$$
\boxed{|\lambda_n^{(N)}-\lambda_n|
\le\frac{20}{7}\,n\,5^{n-1}N^{-3/4}.}
$$

The proof bounds both $1+zG(1+z)$ and $1+zB_N(1+z)$ inside the same disk
$|w-1|\le5/12$ for $|z|\le1/4$, controls their logarithms on the connecting
segment, and applies Cauchy's coefficient estimate. It supplies an explicit
sufficient cutoff for any requested degree and tolerance. It does not prove
that exponential cutoff growth is necessary, and it does not resolve a
uniform sign as $n\to\infty$.

The centered-sawtooth observation in #285 permits a better approximation.
Put $B_N^*(s)=B_N(s)-(1/2)N^{-s}$ and retain the same completion. One
Euler--Maclaurin integration by parts, with the explicit bounded primitive
$P_2(x)=(\{x\}^2-\{x\})/2$, improves the all-degree bound to

$$
\boxed{|\lambda_n^{(N,*)}-\lambda_n|
\le\frac{135}{392}\,n\,5^{n-1}N^{-7/4}.}
$$

Thus a sufficient cutoff for error $\eta$ is
$N\ge\lceil(135n5^{n-1}/(392\eta))^{4/7}\rceil$.
This is a paper-only corollary; the frozen finite evaluator is not silently
claimed to implement it. The classical endpoint correction also extends
local uniform convergence to $\Re s>-1$, repairing the value at $s=0$.
It does not include the next boundary $s=-1$.

There is an exact completion crosswalk to the earlier work. If $B_{\rm EAB}$
is #285's balanced two-pole remainder, then
$2\xi(s)=1+s(s-1)B_{\rm EAB}(s)$ and $B_{\rm EAB}(1)=\lambda_1$.
Its positive theta integral already establishes that first sign. Our
rational prefix is an executable calibration of the same classical value.

The strengthened finite-information control is

$$
\widetilde\xi_m(s)=\xi(s)-\xi(3/4)
\left(\frac{s(s-1)}{(3/4)(-1/4)}\right)^m,\qquad m\ge2.
$$

It preserves the completed reflection symmetry, entire order at most one,
and the first $m-1$ Li coefficients, yet has zeros at $1/4$ and $3/4$.
Its corresponding zeta deformation retains the pole residue, trivial zeros,
and positive-real-axis normalization. The added term decays faster than
every exponential $A^{-\sigma}$, so first-coefficient uniqueness proves it
cannot be an ordinary absolutely convergent Dirichlet series. It is
therefore a changed-source analytic control, not an RH counterexample.
The arithmetic source law supplies information not present in any fixed
finite gamma/Li jet.

## 7. A second RH connection: the same sawtooth reaches Nyman's space

With $0<\theta\le1$, define the centered fractional-part source

$$
\rho_\theta(t)=\{\theta/t\}-\theta\{1/t\},\qquad 0<t<1.
$$

The gamma kernel is itself a Mellin transform on this interval:

$$
\frac{G(s)}s=\int_0^1[1-\{1/t\}]t^{s-1}\,dt.
$$

For $\Re s>0$,

$$
\int_0^1\rho_\theta(t)t^{s-1}\,dt
=(\theta-\theta^s)\frac{\zeta(s)}s
=(\theta-\theta^s)\left[\frac{G(s)}s+\frac1{s(s-1)}\right].
$$

To derive it first for $\Re s>1$, use
$\lfloor\theta/t\rfloor=\sum_{n\ge1}1_{t\le\theta/n}$ and integrate each
indicator. The centered bounded function gives analytic continuation of
the integral to $\Re s>0$. Its value at one is $-\theta\log\theta$; its
derivative there is

$$
-\theta\log\theta(\gamma-1)-\frac\theta2(\log\theta)^2.
$$

This identifies gamma with a concrete jet of the same dilation defect used
in the classical Nyman--Beurling criterion. The constant function one lying
in the closed span of all these $\rho_\theta$ in $L^2(0,1)$ is equivalent to
RH. That closure is not proved here. The Mellin identity and precise domain
are recorded in [Balazard--Saias, ESI 623](https://www.esi.ac.at/preprints/esi623.pdf).
For the later reciprocal-integer strengthening, use
[Baez-Duarte](https://arxiv.org/abs/math/0202141), not the historical open
question in the 1998 text. The existing `bidirectional_cut` and
`zero_centered_residue` modules already mark the closure boundary.

## 8. Reconcile the earlier finite-prime gamma observation

For an integer prime cutoff $X\ge2$ and $\varepsilon>0$, let
$P_X(1+\varepsilon)=\prod_{p\le X}(1-p^{-1-\varepsilon})^{-1}$.
Its positive series contains every integer $n\le X$, so

$$
0\le\zeta(1+\varepsilon)-P_X(1+\varepsilon)
\le\sum_{n>X}n^{-1-\varepsilon}
\le\frac{X^{-\varepsilon}}{\varepsilon}.
$$

Consequently $\varepsilon\log X-\log(1/\varepsilon)\to+\infty$ is a
sufficient cofinal condition for $P_X(1+\varepsilon)-1/\varepsilon\to\gamma$.
At fixed $X$, subtracting the pole instead tends to negative infinity.
This rederives and quantifies the preceding chat's warning. The condition
is sufficient; it is not asserted to be necessary or optimal.

## 9. What to attack next, and how to tell whether it is real progress

**First pi target, smaller than the full normality statement.** Retain
$U_0=0$ and the four exact poles. For $h=1,p=2$, prove an explicit
$|W_2(N)|\le C(\log N)^{-\delta}$ with $\delta>0$ and an explicit onset.
Even this single-mode, single-scale saving would be a new selected-source
estimate. It would not by itself prove normality; the countermodel explains
why the second scale and all integer modes are still needed. An estimate
averaged over changed initials, a prime ensemble, or an altered forcing
does not meet this target.

**Use the newest lag work only with its signed term retained.** Reweight its
finite correlation identity for the $1/n$ time window, preserving the
actual initial phase and full error budget. Before claiming an asymptotic
lift, bound the selected signed aggregate. Improving the tail budget alone
does not pay for that cancellation.

**First RH target, smaller than all-degree positivity.** Improve the explicit
cutoff-to-logarithm transfer so the certified error tracks the actual signed
Stieltjes combination across growing degree. Compare the new source-built
coefficient map against the older theta-built map with completion fixed.
A meaningful new result is a proved uniform signed remainder estimate with
an explicit cutoff schedule, not a longer list of positive decimal values.
Only a subsequent bound strong enough to establish the actual all-degree
sign would discharge Li's criterion.

**Dominance boundary.** This round dominates raw equal-index regularization
as a finite gamma construction because it supplies a uniform error and a
concrete failing raw cofinal clock. It supplies a source-faithful alternate
coordinate for pi and RH, and a new uniform finite Li approximation bound.
It does not dominate the selected-collision or harmonic-lag research by
proving their missing estimate. Gamma is a productive organizing object;
the claim that its scalar value alone settles either target is unsupported.

## Provenance and review limits

Primary analytic identities are attributed in the four proof notes. The
stronger finite cutoff theorem, BBP regulator squeeze, and two-dilation
proof were checked with multiple internal derivations and hostile controls.
All agents share model provenance; this is not independent external
refereeing. Finite exact arithmetic, classical references, and paper proofs
are separately labelled. No nontrivial zeta-zero locations were used as
construction inputs. The actual-source implementation and tests stayed
fixed during the full repository run. Validation details, numerical failure
history, and reproducible commands are in the
[validation record](EULER_MASCHERONI_VALIDATION.md).
