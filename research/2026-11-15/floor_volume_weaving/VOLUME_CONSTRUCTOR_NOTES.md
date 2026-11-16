# Constructor audit: positive source volumes, ordered clocks, and the floor gate

**Status:** exact classical identities and source-typed assembly, independently
derived in this agent lane. No new signed-density estimate or normality theorem.
Parent `fec5cdda24ca36328e123b0b367a0628491e1eb8`. This lane did not read the
other agents' new notes. Parent supplied the candidate Beta decomposition and,
later, the candidate two-exponential realization. Same-model review is not an
independent source family.

## 1. Provenance first: what the repository already contains

The positive factorization below is inherited. It appears in
`research/2026-10-24/BBP_SOURCE_MEMORY_REPAIR.md`,
`research/2026-10-24/PI_PASCAL_REAL_KERNEL.md` and
`research/2026-10-24/PI_SOURCE_GENESIS_GREEN.md`, among many later dossiers.
The explicit five reciprocal differences with coefficients `(4,4,4,2,1)`
appear in `research/2026-11-04/critical_chirp_source/front_ah/PROOFS.md`, AH-01.
The generic independent-Beta product representation of ordered uniforms is
already proved in `research/2026-10-16/FACTORIAL_GAMMA_FUCC_SUCC.md`, FGF-7B.
The original source's accepted second-largest-uniform construction and Gamma(2)
endpoint are in `research/2026-10-29/oily_triangle_sheet/README.md`.
Floor layer-cake, signed carry thresholds, and the authentic four-pole
floor-Laplace transform are in
`research/2026-11-09/floor_layercake_prime_carry/THEOREMS.md`, FLP-01--06.

The present contribution is a direct assembly around the **specific period-four
carry mask**: its `sech` response, Mellin/Dirichlet-beta scale integral, exact
two-successor exponential realization for each of the five original branches,
and an explicit dyadic typing check on those branches. Targeted repository
searches did not find this particular combined presentation. No scholarly
priority is asserted.

## 2. The authentic four poles are five positive Beta volumes

For integer `n>=1`, put `a=8n-7` and `(q_0,...,q_4)=(4,4,4,2,1)`. Then

\[
r(n)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\int_0^1u^{a-1}P(u)\,du,
\]

\[
P(u)=4-2u^3-u^4-u^5
=(1-u)(4+4u+4u^2+2u^3+u^4).
\]

Termwise integration, using positive `a+j`, gives

\[
\boxed{r(n)=\sum_{j=0}^4q_j\mathrm B(a+j,2)
=\sum_{j=0}^4\frac{q_j}{(a+j)(a+j+1)}
=\sum_{j=0}^4q_j\frac{\Gamma(a+j)}{\Gamma(a+j+2)}.}
\tag{V1}
\]

Proof can be checked without a Gamma evaluation: replace every reciprocal
product by `1/(a+j)-1/(a+j+1)` and telescope the five weighted differences.
The resulting coefficients are exactly `4,0,0,-2,-1,-1`.
Euler's Beta integral and Gamma recurrence give the special-function notation:
[DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1),
[DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1).

The Gamma denominator advances by **two in its argument**, because the second
Beta parameter is two. The arithmetic step `n -> n+1` advances `a` by **eight**.
These are different operations. Formula (V1) explains the source's order-two
decay: the five coefficients sum to 15, so `n^2 r(n)->15/64`.

### Ordered-volume realization

For a positive integer `k`, take `k+1` independent uniform variables
`Z_1,...,Z_(k-1),X,Y` on `(0,1)`. Then

\[
\Pr(Z_1,\ldots,Z_{k-1}\le X\le Y)
=\int_0^1x^{k-1}(1-x)\,dx=\frac1{k(k+1)}.
\tag{V2}
\]

The event names **which** label is second largest and which is largest. Its
normalized `X` density is `k(k+1)x^(k-1)(1-x)`, namely Beta(k,2). Equivalently,
the unlabelled second-largest order statistic among `k+1` uniforms has that
density. Choosing `j` with probability `q_j/15`, independently of the uniforms,
makes `r(n)/15` exactly the probability of the corresponding event (V2), with
`k=a+j`. This is an auxiliary probability representation of the scalar forcing.

### Two ordered waiting times give the same branch

For every real `k>0`, let `E_k` and `E_(k+1)` be independent exponentials of
rates `k` and `k+1`. Convolution gives

\[
f_{E_k+E_{k+1}}(x)
=k(k+1)(e^{-kx}-e^{-(k+1)x}),\qquad x>0.
\]

Changing variables `u=e^(-x)` gives exactly the Beta(k,2) density. Thus, for
independent uniforms `V_1,V_2`,

\[
\boxed{U\sim\mathrm{Beta}(k,2)
\quad\Longleftrightarrow\quad
-\log U\overset d=E_k+E_{k+1}
\quad\Longleftrightarrow\quad
U\overset d=V_1^{1/k}V_2^{1/(k+1)}.}
\tag{V3}
\]

Each equivalence is an equality of laws; a pathwise realization is obtained
only by explicitly defining the variables using the displayed construction.
The full normalized original `u`-source is realized by first choosing branch

\[
\Pr(J=j)=\frac{q_j}{(a+j)(a+j+1)r(n)},
\]

then applying (V3) with `k=a+J`. This preserves the entire one-time source
density `u^(a-1)P(u)/r(n)`. It does not specify a joint stochastic law across
different arithmetic times `n`, nor identify such a law with the BBP orbit.

For every `m>=0`, an independent rational check is

\[
\mathbb E[(V_1^{1/k}V_2^{1/(k+1)})^m]
=\frac{k}{k+m}\frac{k+1}{k+1+m}
=\frac{k(k+1)}{(k+m)(k+m+1)}.
\]

The scaled sum `k(E_k+E_(k+1))` tends in law to Gamma(2,1). The same result
follows from the rescaled Beta gap. This limit is inherited endpoint geometry,
not a statement about literal carry frequencies.

The user's square-root/maximum identity has a complementary clock meaning.
If `U_1,U_2` are independent uniforms and `E_i=-log U_i`, then
`-log max(U_1,U_2)=min(E_1,E_2)` has exponential rate two. Likewise
`-log sqrt(U)=(-log U)/2` has rate two. A maximum is therefore a **parallel
race** in the logarithmic clock: rates add. Formula (V3) uses **serial waits**:
waiting times add. Their shared two-component construction does not make the
two operations interchangeable.

### Dyadic typing: positive branches need coherent reassembly

In the five summands of (V1), the `j=3` and `j=4` summands both have 2-adic
valuation `-1` for every `n>=1`; individually they are not in `Z_2`. Their sum is

\[
\frac2{(8n-4)(8n-3)}+\frac1{(8n-3)(8n-2)}
=\frac{3n-1}{(2n-1)(4n-1)(8n-3)}\in\mathbb Z_2.
\tag{V4}
\]

The first two summands combine to `8/((8n-7)(8n-5))`. Therefore an entirely
odd-denominator positive regrouping is

\[
r(n)=\frac8{(8n-7)(8n-5)}
+\frac1{(8n-5)(2n-1)}
+\frac{3n-1}{(2n-1)(4n-1)(8n-3)}.
\tag{V5}
\]

This is an exact assembly constraint. A positive real decomposition need not
remain in the authentic dyadic carrier branch by branch. It does not create a
new lower bound on selected real carries.

## 3. The full original trajectory has the same positive integral source

For `n>=0`, finite geometric summation gives

\[
\boxed{U_n=\int_0^1P(u)\frac{16^n-u^{8n}}{16-u^8}\,du.}
\tag{V6}
\]

For `n=0` this is exactly zero. For `n>=1` expand the kernel as
`sum_(k=1)^n 16^(n-k)u^(8k-8)` and use the original recurrence. Define

\[
\alpha=\int_0^1\frac{P(u)}{16-u^8}\,du,\qquad
T_n=\int_0^1\frac{u^{8n}P(u)}{16-u^8}\,du.
\]

Then `U_n+T_n=16^n alpha` exactly, and the original BBP identity gives
`alpha=pi/16`; see [Bailey--Borwein--Plouffe, Theorem 1](https://www.davidhbailey.com/dhbpapers/digits.pdf).
Every denominator here is at least 15, so the compact integrals are ordinary
finite integrals; the positive geometric tail uses Tonelli.

The carry gate is applied **after** (V6) is integrated. If `Z` is an auxiliary
variable representing its integrand under a probability measure, then
`A(E Z)` is not generally `E A(Z)`. For example, let `Z=0` or `4`, each with
probability one half. The period-four selected gate below gives
`A(E Z)=A(2)=1`, while `E A(Z)=0`. This exact counterexample defeats an
unjustified interchange without changing any universal integral identity.

## 4. Floor is a counting integral; its period-four gate has a sech transform

For `x>=0`, the boundary convention is

\[
\lfloor x\rfloor=\sum_{k\ge1}\mathbf1_{x\ge k}
=\int_{(0,x]}\sum_{k\ge1}\delta_k(dt).
\tag{V7}
\]

The right side is an integral against an atomic counting measure. For a
nonnegative random variable, Tonelli also gives
`E floor(X)=sum_(k>=1) P(X>=k)`, with both sides allowed to be infinite.

Define, on `x>=0`,

\[
A(x)=\mathbf1_{\lfloor x\rfloor\bmod4\in\{1,2\}}
=\sum_{j\ge0}\mathbf1_{[4j+1,4j+3)}(x),\qquad g(x)=1-2A(x).
\]

This is exactly the current selected carry gate: `A(U_n)=A_n` and
`g(U_n)=w(C_n)`. For every real `t>0`, integrating each interval gives

\[
\boxed{\int_0^\infty e^{-tx}A(x)\,dx
=\frac{e^{-t}(1-e^{-2t})}{t(1-e^{-4t})}
=\frac1{2t\cosh t}.}
\tag{V8}
\]

Consequently

\[
\int_0^\infty e^{-tx}g(x)\,dx=\frac{1-\operatorname{sech}t}{t},\qquad
\int_0^\infty e^{-tx}(-1)^{\lfloor x/2\rfloor}\,dx
=\frac{\tanh t}{t}.
\tag{V9}
\]

The phase shift between the two square waves matters. Point values at integer
boundaries do not change these Lebesgue integrals but do matter when reading
the deterministic orbit. No Fourier midpoint convention is being substituted.

For an exponential probe `X_t` of rate `t`, (V8) says

\[
p(t):=\Pr(A(X_t)=1)=\frac1{2\cosh t}.
\tag{V10}
\]

For an Erlang/Gamma probe of positive integer shape `m` and rate `t`, the
corresponding exact probability is

\[
\frac{t^m}{(m-1)!}(-\partial_t)^{m-1}
\left(\frac1{2t\cosh t}\right).
\tag{V11}
\]

Differentiation is legitimate by the exponentially integrable polynomial
majorant on each compact rate interval. These formulas declare the probe law;
they are not observations of the zero-seeded BBP trajectory.

## 5. Mellin scale integration recovers Gamma times Dirichlet beta

For complex `s` with `Re(s)>0`, all the following integrals converge absolutely:

\[
\int_0^\infty A(x)x^{-s-1}\,dx
=\frac1s\sum_{j\ge0}\left((4j+1)^{-s}-(4j+3)^{-s}\right)
=\frac{\beta(s)}s.
\]

The paired sum converges absolutely on this half-plane, as follows by
integrating `s x^(-s-1)` over each interval. For `Re(s)>1` it is the ordinary
Dirichlet series `L(s,chi_4)`; the paired formula continues it to `Re(s)>0`.
Here `chi_4` is zero on even integers and `+1,-1` on `1,3 mod4`, respectively.

Insert (V10), interchange by absolute convergence, and use Euler's Gamma
integral to obtain

\[
\boxed{\int_0^\infty t^{s-1}p(t)\,dt
=\Gamma(s+1)\int_0^\infty A(x)x^{-s-1}\,dx
=\Gamma(s)\beta(s),\quad\Re s>0.}
\tag{V12}
\]

At `s=1`, the classical arctangent integral or the substitution `z=e^(-t)`
gives

\[
\boxed{\int_0^\infty p(t)\,dt
=\int_0^\infty\frac{A(x)}{x^2}\,dx
=\int_0^1\frac{dz}{1+z^2}=\frac\pi4.}
\tag{V13}
\]

This is a scale integral of the **same mask**, not a proof about how frequently
the BBP orbit visits that mask. If extending the connection to negative
arguments, Dirichlet beta has odd character parity; its trivial zeros occur at
negative odd integers. The zeta negative-even pattern must not be transplanted.
Primary references: [DLMF 25.15](https://dlmf.nist.gov/25.15),
[DLMF 5.2.1](https://dlmf.nist.gov/5.2.E1). Formula (V12) itself is derived here.

## 6. Attach the exact gate transform to all four original poles

For real `a>0`, define

\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\quad
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},
\]

\[
\mu_a(dx)=R(a)^{-1}e^{-ax}Q(x)\,dx.
\]

This positive probability measure is exactly the logarithmic image of the
normalized positive source in Section 2. For `L>0`, apply (V8) to each of the
four exponential terms:

\[
\boxed{\Pr_{\mu_a}(A(LX)=1)
=\frac1{2R(a)}\sum_{(d,w)=(0,4),(3,-2),(4,-1),(5,-1)}
\frac{w}{(a+d)\cosh((a+d)/L)}.}
\tag{V14}
\]

This specializes the inherited FLP-11 transform to the actual period-four
gate. With `f(k)=1/[k cosh(k/L)]`, it is equivalently
`[2R(a)]^(-1) sum_j q_j[f(a+j)-f(a+j+1)]`. Each difference is positive,
since `f` is strictly decreasing on positive arguments.

At native scale `L=a -> infinity`, the source variable `aX` converges to
Gamma(2,1). Its limit law has no mass at the gate's integer boundaries, so the
bounded gate probability converges. Equation (V11), with `m=2,t=1`, yields

\[
\boxed{\Pr_{\mu_a}(A(aX)=1)\longrightarrow
\frac{\operatorname{sech}(1)}2(1+\tanh1)
=\frac{2e^{-1}}{(1+e^{-2})^2}>\frac12.}
\tag{V15}
\]

For an elementary strict bound, `2<e<3`, so `q=e^(-1)` lies in `(1/3,1/2)`;
`2q/(1+q^2)^2` increases on that interval and is larger than `27/50`.
Thus this source-attached Gamma gate law is **not** the Haar reference `1/2`.
Neither value supplies the actual deterministic carry frequency. It does
provide an exact diagnostic target for any proposed joint-source transport.

## 7. Audit receipt and remaining obligation

A standalone in-session `Fraction` audit, with no production imports or
special-function calls, checked:

- 517 original four-pole versus five-Beta rational identities (`n=1..512` and
  holdouts `1001,4093,10007,12345,1000003`);
- 517 positive odd-denominator regroupings and 517 half-dyadic cancellations;
- 1,536 Beta/product moments (`k=1..64`, integer moment orders `0..23`);
- 561 rational-q versions of the geometric gate transform;
- 1,078 coefficient and phase mutation rejections.

These are finite calibration checks of the displayed proofs. They do not
replace the proofs, and no full repository suite was run by this agent.

**Verdict.** The proposed volume connection survives as an exact construction.
The strongest source-attached addition is (V14), with its explicit current-gate
response and Gamma endpoint (V15), plus the branchwise dyadic constraint (V4).
The density target remains

\[
\exists\delta>0,B_0\ \forall B\ge B_0:
\quad\frac1B\sum_{B\le n<2B} A(U_n)\ge\delta.
\]

None of (V1)--(V15) establishes this inequality. A verdict-changing next step
must preserve the authentic zero seed, four poles, and **joint ordered
correlation** while transporting an observable to `A(U_n)`. A norm law or
auxiliary Gamma floor probability alone does not perform that transport; the
explicit floor-of-mean counterexample above locates the unpaid step.
