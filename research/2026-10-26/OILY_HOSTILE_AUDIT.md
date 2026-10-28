# Oily–Macaroni hostile verification: source, quantifiers, and sharp limits

**Status:** independent derivations and finite verification within the same model
family; not external peer review. Starting tree:
`a8c7c85b7a1900d422090f1757c174e7aac69f44` (draft #310).
The original four-pole source and archival provenance were not edited.
**Base-16 normality of pi remains OPEN.**

## 1. Audit contract and source reconstruction

The object is the exact recurrence

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
$$

The missing estimate remains $\sum_{n\le N}e(hU_n)=o(N)$ for every
fixed nonzero integer $h$. The audit distinguishes a larger constant in the
proved logarithmic **absolute** loss from a better asymptotic order, and both
from normality.

An independently written literal four-fraction calculation, without a pi
input, was compared at every $1\le n\le128$ against `authentic_r`,
`bbp_natural_carrier.exact_forcing`, and `integer_bbp_carrier.forcing_pair`.
All agree. Independent iteration from zero agrees with `original_state` and
the integer numerator/conductor states at these same 128 indices. Changing
the final pole coefficient from $-1$ to $-2$ is rejected at index one.
These are exact finite implementation checks, not an infinite proof.

The universal source bounds follow separately from

$$
g(t)=(1-t)(4+4t+4t^2+2t^3+t^4),\qquad
T_n=\int_0^1t^{8n}\frac{g(t)}{16-t^8}\,dt.
$$

Because the quotient multiplying $1-t$ lies strictly between zero and one,
$0<T_n<1/[(8n+1)(8n+2)]$. The identity
$16T_n-T_{n+1}=r(n+1)$ and the exact BBP sum give
$U_n+T_n=16^{n-1}\pi$. No auxiliary packet character is used in this
identity. Its summable tail supports the inherited $O_h(1)$ Weyl transfer.

## 2. The inherited Diophantine argument survives

The proof in [BBP_DIOPHANTINE_COHERENCE.md](../2026-10-25/BBP_DIOPHANTINE_COHERENCE.md)
was rederived, including the sign of every integer lift. If
$y_t=\theta+q_t=hX_t+\ell_t$ with $\ell_t\in\mathbb Z$, then

$$
q_{t+1}-16q_t-hr_{t+1}\in15\theta+\mathbb Z.
$$

When these quantities share one value $b$, let
$f=\theta-b/15$. Then
$y_{t+1}-f=16(y_t-f)+hr_{t+1}$, and the terminal identity is

$$
y_T-f=\frac{16(q_T-q_{T-1})-hr_T}{15}.
$$

This verifies the inverse-arc denominator $15|h|$, the terminal forcing
sign, and the backward radius. On the authentic block $(m,8m]$, exact
Green cancellation then gives the rational denominator $15|h|16^m$.
Using the much larger denominator of a finite BBP partial sum would miss
this cancellation; omitting the Green correction would be false.

The corrected Zeilberger–Zudilin paper proves
$\mu(\pi)\le7.103205334137\ldots<15/2$.
Consequently **one** positive rational $C\le1$ exists with
$|\pi-p/q|\ge Cq^{-15/2}$ for every integer $p$ and positive integer $q$.
For sufficiently large reduced denominators this follows from the strict
exponent gap; finitely many smaller denominators are absorbed into $C$.
Unreduced denominators only weaken the lower bound. The source proof's
single sufficiently large threshold, uniform over its polynomial frequency
band, is therefore valid. Neither the audit nor the original proof extracts
that threshold numerically.

Primary check: [Zeilberger–Zudilin, corrected v2, final section](https://arxiv.org/html/1912.06345v2),
with [published DOI](https://doi.org/10.2140/moscow.2020.9.407).
The paper's bound was checked directly, not inferred from a search snippet.

## 3. New branch-energy inverse bound: independently checked constants

The new direct-arithmetic construction replaces separate coordinate bounds
by a shared quadratic energy. For $L=D-|\sum_te(hX_t)|$, choose the
resultant angle $\theta$ and principal $q_t\in[-1/2,1/2]$. Then exactly

$$
L=\sum_t(1-\cos(2\pi q_t))\ge8\sum_tq_t^2.
$$

If two branch residuals differ, their difference is a nonzero integer
after subtracting the forcing difference. The difference of their two
linear forms has squared coefficient norm at most $546$: it is $514$
for disjoint transitions and $546$ for adjacent transitions, whose vector
is $(16,-17,1)$ up to sign. Therefore, whenever
$1-\cos(2\pi q_t)\ge c q_t^2$ and
$\rho=|h|(\max r-\min r)<1$,

$$
\text{nonconstant branch}\quad\Longrightarrow\quad
L\ge\frac{c(1-\rho)^2}{546}.
$$

The overlap case is essential: replacing $546$ by $514$ everywhere would
be an invalid strengthening. Independent integer enumeration checked
every pair of transitions for lengths two through eleven, as a calibration
of the two-case algebraic proof.

The final rational implementation was checked:

| Loss cap | Phase radius | Quadratic constant | Forcing-range cap | Exact strict margin above loss cap |
| --- | --- | --- | --- | --- |
| $1/29$ | $1/15$ | $19$ | $15/4096$ | $2329025/37950062592$ |

The phase-radius implication follows from
$q_t^2\le1/(29\cdot8)<1/15^2$. An independent rational trigonometric
check uses the elementary Taylor inequality and $157/50<\pi<22/7$:

$$
2(157/50)^2-\frac{2(22/7)^4}{3\cdot225}-19
=\frac{34853873}{81033750}>0.
$$

The production proof uses the also-valid weaker lower bound $25/8<\pi$.
Thus the branch residual is constant under the displayed hypotheses. The
authentic source supplies the forcing cap when $|h|\le m^2/64$.
Afterward the inherited exact Green identity is still required; this
finite energy lemma by itself is forcing-generic and seed-blind.

The approximation error is below $3\cdot16^{-8m}$;
the Diophantine comparison must include the corresponding factor $9$ in
$C^216^m>9(15|h|)^{15}$. Dropping this factor from a finite threshold
certificate is a mutation that must fail, even though it does not affect
the existence of a sufficiently large threshold. The final selected
inequality and exact frequency schedule were checked in
[OILY_DIRECT_ARITHMETIC.md](OILY_DIRECT_ARITHMETIC.md); this audit does not
silently promote the finite lemma to normality.

**Novelty boundary:** this shared-energy argument improves the allowable
absolute block deficit. It does not make that deficit grow with the block
length. A larger logarithmic-loss coefficient is a genuine strengthened
selected bound, but the normalized upper bound still tends to one.

## 4. Independent check of the all-order logarithmic-shadow obstruction

The cross-time worker and this auditor separately obtained the same
expansion before exchanging the formulas. The full theorem is in
[OILY_CROSS_TIME_GRAMMAR.md](OILY_CROSS_TIME_GRAMMAR.md); this section records
the independent calculation rather than creating another theorem namespace.

Write $a=8n$, $\delta=1-x$ and
$f_g(1-\delta)=C+H\delta+K\delta^2+O(\delta^3)$ for the conditional
packet observable. The authentic source weight obeys
$w(1-\delta)=1-2\delta+4\delta^2+O(\delta^3)$. With
$B_j=B(a+1,s+2+j)$, the exact beta ratios yield

$$
\frac{B_1}{B_0}=\frac{s+2}{a+s+3},\qquad
\frac{B_2}{B_0}=\frac{(s+2)(s+3)}{(a+s+3)(a+s+4)}.
$$

Expanding the **normalized tilted ratio**, rather than the unnormalized
moment, gives

$$
\frac{\mathbb E[g(J)Y^s]}{\mathbb E[Y^s]}
=C+\frac{H(s+2)}a+
\frac{K(s+2)(s+3)-H(s+2)(s+5)}{a^2}+O(a^{-3}).
$$

The first correction is affine in $s$. All mixed cumulants with one grade
observable and at least two copies of $\log Y$ therefore have vanishing
$a^{-1}$ coefficient. At second order the centered third cumulant has
coefficient $2(K-H)$, without a golden or Euler constant. For the odd-grade
projector,

$$
f_g(x)=\frac{x}{(1+u(x))(1+v(x))},\qquad
C=\frac49,\quad H=-\frac4{27},\quad K=-\frac8{81},
$$

so the independently recovered prediction is
$a^2\kappa(g,\log Y,\log Y)\to8/81$.
The source law and the observable are retained; changing packet grading
still changes the observable. Center invariance is not grading invariance.

As a separate numerical holdout, direct 70-decimal quadrature of the
untruncated density in the $y=a(1-x)$ coordinate gave:

| $a$ | $a^2\kappa(\mathbf1_{J\text{ odd}},\log Y,\log Y)$ |
| ---: | ---: |
| 32 | 0.038417315434232671758814223280671696 |
| 128 | 0.073084270434879833807759160402832943 |
| 512 | 0.091151222054563982567533113184828575 |
| 2048 | 0.096771721800717595850138285928530472 |

The limiting prediction is $8/81=0.098765432098765432\ldots$.
These are **uncertified numerical observations**, not outward enclosures
and not a proof of the asymptotic expansion. Their purpose is to attack
signs, normalization, and the proposed $a^2$ scaling by a different method.
The default Python and primary-runtime Python lacked `mpmath`; the existing
repository development virtual environment supplied it. Those initial
import failures were not mathematical failures and are not counted as tests.

The resonance-degree claim also survives an independent check. For a
nonzero finitely supported integer vector $k$ with
$\sum_nk_n16^n=0$, take its largest occupied index $m$. Then
$16|k_m|\le\sum_{n<m}|k_n|$, so $\sum_n|k_n|\ge17$.
Equality forces adjacent coefficients $(16,-1)$ up to sign and shift.
The degree refers to **reduced phase exponents**; trivial factors
$Z_n\overline Z_n=1$ must first be canceled.

The independent standard-library oracle also constructs the normalized
beta/source jet using bivariate rational polynomials in $a^{-1}$ and $s$,
through order six. It imports no production cumulant formula. Every
coefficient at inverse-power order $k$ has degree at most $k$ in $s$.
The leading mixed-cumulant coefficients for orders one through six are

$$
-\frac4{27},\quad\frac8{81},\quad-\frac{56}{81},\quad
\frac{1856}{243},\quad-\frac{56320}{729},\quad\frac{581120}{729}.
$$

They agree exactly with $m![v^m]f_g(1/(1+v))$. Replacing the outer source
weight by the positive smooth mutant $1/(1-t/3)$ changes the full beta
jet but preserves every displayed leading coefficient. This calibrates
the theorem's explicit source-blindness boundary; it does not identify
the mutant with the BBP source.

An exact two-state survival/redraw model independently checks temporal
nonuniqueness: starting masses $(1/3,2/3)$, survival weights $(1/4,3/4)$,
and observable $(0,1)$ produce the same next marginal $(1/7,6/7)$ under
independent and persistent kernels, but covariances $0$ and $1/14$.
This checks the general algebra used in the authentic source coupling
proof; it is not substituted for the authentic continuous source law.

## 5. Sound finite signed enclosures: separate audit

The principal's `oily_signed_certificate.py` was read independently. Its
Machin enclosure uses the correctly signed alternating arctangent bounds.
After phase reduction, let $p$ be its dyadic lower approximation and let
the angle be the dyadic lower approximation to twice the midpoint pi
enclosure times $p$. The resulting angular error is bounded by

$$
\frac{2\pi_{\rm upper}+1}{2^{\rm bits}}
 +|p|(\pi_{\rm upper}-\pi_{\rm lower}),
$$

exactly as implemented. The zero odd/even Taylor coefficients justify the
cosine and sine remainder exponents $2\,\mathrm{order}+2$ and
$2\,\mathrm{order}+3$, respectively. Their real derivatives are bounded
by one, and angle perturbations are controlled by the same Lipschitz
constant. Outward rational rounding, interval squaring across zero, and
subtraction of diagonal energy preserve enclosure soundness. The signed
cross-block quantity is not replaced by a positive diagonal statistic.
This confirms the stated finite analytic proof; it supplies no
asymptotic cancellation theorem.

## 6. Carry-energy certificate: boundary audit and a sharp universal ceiling

The direct worker's additional all-center certificate is valid:

$$
N-|S_N(h)|\ge\frac2{289}\mathcal E_{N,h},\qquad
\mathcal E_{N,h}=\min_\theta\sum_{n=1}^{N-2}
[q_{n+2}(\theta)-17q_{n+1}(\theta)+16q_n(\theta)]^2.
$$

Here $q_n(\theta)=hX_n-\theta-\lfloor hX_n-\theta+1/2\rfloor$.
The global chord inequality gives the factor eight, and the finite
convolution's absolute coefficient sum $34$ gives the factor $34^2=1156$.
If the resultant is zero, any center can be chosen in the proof because
the sum of the projected cosines is zero. No undefined resultant argument
is required.

**Breakpoint audit.** At a tied breakpoint $\beta$, every tied canonical
lift equals $-1/2$, so the simultaneous floor values agree with the
preceding interval's pattern. At $\beta=0$, that pattern agrees with the
last cyclic interval up to a common integer shift. The shift is killed
by $16-17+1=0$. Thus exact midpoint enumeration covers the energy at every
possible resultant center, including ties. A right-hand limit also gives
valid closed-interval lifts $+1/2$, but the canonical left pattern already
suffices. Sequentially updating tied lifts would introduce unattainable
intermediate patterns and is correctly forbidden.

The independent oracle explicitly enumerates both every rational
breakpoint **and** every intervening midpoint for all 320 histories of
length three or four on the quarter-circle grid. It agrees with the
grouped sweep on every history, including zero and tied breakpoints.
Fresh authentic-source holdouts $(N,h)=(17,-2),(37,3)$ also agree exactly.

### Sharp ceiling theorem

For **every** real phase history with $N\ge3$,

$$
\boxed{\mathcal E_{N,h}\le\frac{289}{4}(N-2).}
$$

This upper bound is attained by alternating phases $0,1/2$. Consequently
the best upper bound that the displayed certificate can ever return is
bounded below by

$$
\boxed{N-\frac2{289}\mathcal E_{N,h}\ge\frac{N+2}{2}.}
$$

This is a limitation of the **certificate's upper bound**, not a lower
bound on the actual Fourier modulus. For even-length alternating phases
the actual Fourier sum is zero while the certificate returns $(N+2)/2$.

**Elementary proof, including the covariance integral.** Average the
center uniformly over one circle. Each $q_i$ is uniform on $[-1/2,1/2)$.
For a phase displacement $d\in[0,1)$, the second centered sawtooth is
$q_j=v+d-\mathbf1_{v\ge1/2-d}$ when $q_i=v$. Hence

$$
\begin{aligned}
\int_0^1q_i(\theta)q_j(\theta)\,d\theta
&=\int_{-1/2}^{1/2}v(v+d)\,dv
  -\int_{1/2-d}^{1/2}v\,dv\\
&=\frac1{12}-\frac12d(1-d).
\end{aligned}
$$

This formula is insensitive to reversing the displacement. Put
$F(d)=d(1-d)$ and $d_{ij}=\{h(X_i-X_j)\}$. Expanding the square of
$16q_n-17q_{n+1}+q_{n+2}$, all constant $1/12$ terms cancel because the
coefficient sum is zero. The exact center average is

$$
272F(d_{n,n+1})-16F(d_{n,n+2})+17F(d_{n+1,n+2}).
$$

Since $0\le F\le1/4$, this is at most
$(272+17)/4=289/4$. Sum over the $N-2$ triples and use
minimum $\le$ average. For alternating phases,
$d_{n,n+1}=d_{n+1,n+2}=1/2$, $d_{n,n+2}=0$, and the squared linear
form is identically $289/4$ at every center. Equality follows. QED.

The independent oracle verifies this average by exact integration of the
piecewise constant cell energies, separately checks the displacement
formula on all 320 grid histories and the fresh source holdouts, and
verifies equality on a 16-state alternating control. The mean formula is
not inferred from a plot or floating-point quadrature.

**Verdict:** the certificate remains useful as a genuine carry-sensitive
finite selector witness and source-to-phase inequality. Even the strongest
possible lower bound on this energy cannot make this particular upper
bound sublinear. Normality requires another estimate, iteration with a
proved additional mechanism, or a different observable. Calling
asymptotic energy growth alone the sufficient next gate would be false.

## 7. Hostile controls and the exact scope of the obstruction

The exact-forcing control $X_0=-\pi/16$ gives $X_n=-T_n$ and hence
$N-|\sum_{n\le N}e(hX_n)|=O_h(1)$. It defeats any seed-free upgrade of
the logarithmic loss, but does **not** refute a theorem explicitly using
$U_0=0$. The necessary failure is precisely the selector identity used
after Green cancellation.

A stronger method boundary is supplied by
$\xi=\sum_{j\ge0}16^{-2^j}$. The inherited estimate
$\sum_{n\le N}\{16^n\xi\}=O(\log N)$ gives
$\sum_{n\le N}e(h16^n\xi)=N+O_h(\log N)$.
Its irrationality exponent is two, as explicitly stated for every integer
base in [Hone–Varona, section 4, equation (4.2)](https://arxiv.org/html/1810.10127v1).
With initial state $X_0=\xi-\pi/16$ it also retains the exact BBP forcing;
the summable $T_n$ changes the Fourier sum by only $O_h(1)$.
Thus forcing plus a finite irrationality exponent cannot produce a
uniform superlogarithmic loss for arbitrary selectors. This says nothing
against a new proof that genuinely exploits the **specific** zero selector.

The logarithmic shadow tests do not escape this control: changing the seed
leaves the one-time packet source law unchanged. Nor does the degree-17
resonance, since $Z_n^{16}\overline Z_{n+1}=e(-hr(n+1))$ holds for every
seed. Any proposed cross-time cancellation theorem must name the exact
step at which it distinguishes these controls.

## 8. Executed checks and remaining falsifier

The native focused invocation

```sh
PYTHONPATH=. python -m unittest tests.test_bbp_diophantine_coherence tests.test_oily_macaroni_totient -v
```

using the existing development environment completed **32 tests, all
passing**, in 4.533 seconds. Together with the 128-state independent
source reconstruction, exact rational margins, coefficient-norm check,
fresh primary-source reads and direct quadrature, this is the actual audit
evidence. Full combined-tree and hosted exact-head validation are separate
obligations owned by the principal; they are not inferred from this run.

The reusable independent instrument is
[oily_hostile_oracle.py](oily_hostile_oracle.py), with the deterministic,
source-hashed [receipt](OILY_HOSTILE_ORACLE_RECEIPT.json). It runs without
third-party packages:

```sh
python research/2026-10-26/oily_hostile_oracle.py --verify
```

Receipt generation and byte-for-byte replay both passed. Changing its
branch norm list to the false singleton `[514]` made the verifier exit
nonzero with `REJECTED: exact oracle receipt mismatch`. The oracle checks
220 transition pairs, 128 literal source states, 624 nonzero small
phase-exponent vectors, all beta jets through order six, and four explicit
mathematical mutants. Those finite checks accompany the paper arguments;
none performs an unproved finite-to-infinite lift.

The next decisive falsifier for a proposed asymptotic improvement is the
sparse-selector control above. To survive, a theorem must invoke an
authentic source/zero-selector property absent from that control and then
bound the **signed** effect, not merely count finite branch transitions or
measure a positive packet defect. The sharp unresolved question remains
whether source-conditioned moderate coherence can be bounded beyond the
constant absolute-loss regime. No such bound is claimed by this audit.
