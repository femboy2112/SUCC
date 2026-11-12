# A Borwein ratchet on the arithmetic cylinder

**Date:** 2026-11-12. **Parent publication:**
`e855200a9a447933ef93b3ee0947d14d00ef42de`.
**Verdict:** SURVIVES as an exact construction with a declared directional
controller. The integral identities, release theorem, lifted traversal,
rectification theorem and degree-filter identities below are **PROVED LOCAL**.
This means the displayed derivations in their stated domains, not academic
priority, external refereeing, a formal proof kernel, physical realization,
or an arithmetic speedup. Goldbach, RH and the source-specific correlation
estimate remain OPEN.

## 0. What the proposed mechanism does

We interpret an arithmetic ratchet faithfully as a common carrier with
symmetric wiggles, a tooth that can be certified to release, and a remembered
orientation that advances the arithmetic observer. Three pieces have distinct
jobs:

| Piece | Exact object | Role |
|---|---|---|
| Clock | Growing uniform-convolution support, encoded by Borwein integrals | Certifies each next release |
| Pawl and lift | A nondecreasing integer count, retained with the angular residue | Supplies direction and remembers completed turns |
| Arithmetic readout | A fixed Borwein window applied to the degree charge `Omega(n)-1` | Preserves primes and suppresses composite degrees |

The clock and the readout use **different width banks**. Letting the clock's
support grow without bound destroys the readout's prime-preserving plateau.
The common integer carrier and the authentic SUCC/dilation maps couple these
pieces; an unlabelled distribution of widths does not replace that coupling.

### Prior work, not rediscovery

The October 19 dossier [BORWEIN_DELTA_PRIME_CLOCK.md](../../2026-10-19/BORWEIN_DELTA_PRIME_CLOCK.md)
already proves normalized Borwein mass, inclusion-exclusion, the first shallow
leakage formula, the classical denominator 15 break and an odd-prime-width
break at 29. Its exact implementation is
`observational_succ/borwein_prime_clock.py`, originating at
`932a2f2d4b8dd24690bcabf642ea0f14b841bedc`.

[FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md](../../2026-10-19/FACTORIAL_BORWEIN_HOLOGRAPHIC_CLOCK.md)
already proves stable cardinal interpolation, genuine prime-power transport,
and a prime-detecting variance increment. The implementation originates at
`938319e10db142310afa3bb257457e58eb3691dc`. The later transport calculus
originates at `2ede8b26ad8c5e707d7e6a10f8089609afb8b655`.

This extension joins those interfaces to the current cylinder, adds an
all-tooth release certificate and an explicit observer, and separates three
different limiting behaviors that a geometric analogy can conceal. The
original modules and archival sources are used without modification.

## 1. A Borwein integral is an exact window gate

Write `sinc(t)=sin(t)/t`, with `sinc(0)=1`. Let `m>=1`, `b>0`, and
`a_1,...,a_m>0`. Let independent `U_j` be uniform on `[-a_j,a_j]`, and put
`S_m=sum U_j`, `A_m=sum a_j`. For real shift `c`, define

\[
M_{b,m}(c)=\frac{2b}{\pi}\int_0^\infty
 \operatorname{sinc}(bt)\cos(ct)
 \prod_{j=1}^{m}\operatorname{sinc}(a_jt)\,dt.
\]

**Theorem BRT-01 (window identity and boundaries).**

\[
\boxed{M_{b,m}(c)=\Pr\{|S_m+c|\le b\}.}
\]

In particular,

\[
\begin{aligned}
M_{b,m}(c)=1&\iff |c|+A_m\le b,\\
M_{b,m}(c)=0&\iff |c|\ge A_m+b.
\end{aligned}
\]

It lies strictly between zero and one in the remaining cases. Equality at a
support endpoint contributes no probability mass: `m>=1` is load-bearing.

**Proof.** The characteristic function of `S_m` is the product of the sinc
factors. The Fourier transform of the window `[-b,b]` is `2b sinc(bt)`.
Fourier inversion, or convolution of that window with the uniform densities,
gives the displayed integral. The integral is absolutely convergent for
`m>=1`. The density of `S_m` is positive throughout `(-A_m,A_m)`, zero
outside its closure, and has no atoms. The two boundary statements follow by
interval containment and overlap. This is the classical Borwein mechanism
with a declared normalization and shift; see sources [1] and [2].

For an **empty** width bank, the integral is only conditionally convergent
and gives half-weight at `|c|=b`. A closed-window probability for the
deterministic point `S_0=0` instead gives weight one there. The executable
interfaces keep these conventions separate: `window_mass` returns the
closed-window probability, while `borwein_multiplier` uses the Fourier
half-value at an empty-bank endpoint.

For rational widths, shift and window, the value is rational. We reuse the
existing exact CDF through the scaling

\[
M_{b,m}(c)=M_{1,m}(c/b; a_1/b,\ldots,a_m/b).
\]

The inherited general CDF has a declared exponential-work budget of at most
11 widths. The next theorem bypasses that general subset sum at a first
release; it is not limited to 11 factors.

## 2. All teeth release, with a certificate for each one

Let `a_j` now be an infinite positive rational sequence, with unbounded
partial sums. For tooth `k>=1`, set

\[
\tau_k=\min\{m\ge1:A_m>k\},\qquad
\ell_m=\#\{k\in\mathbb N_{>0}:k<A_m\}
       =\max(0,\lceil A_m\rceil-1).
\]

**Theorem BRT-02 (productive support ratchet).** Every `tau_k` is finite,
`ell_m` never decreases, and `ell_m` tends to infinity. Tooth `k` releases
exactly when its centered Borwein gate first leaves the plateau:

\[
m\ge\tau_k\quad\Longleftrightarrow\quad A_m>k
\quad\Longleftrightarrow\quad M_{k,m}(0)<1.
\]

This equivalence follows from BRT-01 and positivity of the widths. In
particular, `A_m=k` **does not** release tooth `k`. Replacing the strict count
by `floor(A_m)` is an actual boundary bug, not an innocent rounding choice.

If the widths are nonincreasing, every first release has a particularly
simple exact amplitude certificate. Put `r=tau_k` and `delta=A_r-k`.
Minimality gives

\[
0<\delta\le a_r=\min_{j\le r}a_j.
\]

**Theorem BRT-03 (first release is always a shallow cap).**

\[
\boxed{1-M_{k,r}(0)=
 \frac{\delta^r}{2^{r-1}r!\prod_{j=1}^r a_j}>0.}
\]

**Proof.** In the product box `prod[-a_j,a_j]`, the condition `S_r>k`
cuts a corner. Write `y_j=a_j-U_j`. The cut is `sum y_j<delta`, `y_j>=0`.
Since `delta<=a_r<=2a_j`, no upper face clips this simplex. Its volume is
`delta^r/r!`. Divide by the box volume `2^r prod a_j` and double for the
opposite corner. Boundary faces have measure zero. The older first-leakage
formula applies at **every** first tooth crossing for this reason.

More generally, for a shifted shallow gate, let
`delta_+=A_m+c-b`, `delta_-=A_m-c-b`. If each positive part is at most
`2 min a_j`, then

\[
1-M_{b,m}(c)=
\frac{(\delta_+)_+^m+(\delta_-)_+^m}
 {2^m m!\prod a_j}.
\]

The separate derivation audit checks the signs and equality faces.

### The classical odd-width clock

Take `a_j=1/(2j+1)`, starting with `1/3`. Its sum diverges, while its sum of
squares converges. Exact rational comparison gives:

| Tooth `k` | First stage `tau_k` | Last denominator | Normalized first leakage, illustrative decimal |
|---|---:|---:|---:|
| 1 | 7 | 15 | approximately `1.4706281350e-11` |
| 2 | 56 | 113 | approximately `1.4848708092e-138` |
| 3 | 418 | 837 | approximately `2.8772167025e-1320` |

The stage certificates are exact. The displayed decimals are evaluations of
an exact rational formula and are not used for any decision. The first loss
recovers the prior known value

\[
\frac{6879714958723010531}
 {467807924720320453655260875000}.
\]

Every tooth has an elementary effective deadline:

\[
\boxed{\tau_k\le 8^k-1\quad(k\ge1).}
\]

To see this, divide `j=1,...,8^k-1` into the `3k` dyadic blocks
`r<=j<=2r-1`, `r=1,2,4,...,2^(3k-1)`. Cauchy--Schwarz gives

\[
\sum_{j=r}^{2r-1}\frac1{2j+1}
\ge\frac{r^2}{\sum_{j=r}^{2r-1}(2j+1)}=\frac13.
\]

At least one block has `r>1`, so the total is strictly greater than `k`.
This is a termination bound, not a practical speedup. More precisely,
`A_m=H_(2m+1)-(1/2)H_m-1`, so the standard harmonic-number estimate gives

\[
\tau_k\sim\frac{e^{2-\gamma}}4 e^{2k}\quad(k\longrightarrow\infty).
\]

Thus this particular gear schedule spends exponentially many width inputs
per arithmetic-label scale. Constant rational widths can make the support
clock advance linearly; the odd schedule is chosen to expose the classical
Borwein phenomenon, not to optimize enumeration.

## 3. The observer has finite rules and a retained lift

The exact controller needs rational arithmetic and a growing integer state.
Its essential transition is:

```text
stage := 0; support := 0; tooth := 1; source := 1
repeat:
    stage := stage + 1
    support := support + 1/(2*stage + 1)
    while support > tooth:
        certify the first-crossing cap
        source := source + 1
        emit the source label and its arithmetic readout
        tooth := tooth + 1
```

**Theorem BRT-04 (lifted productive traversal).** This finite program visits
each positive integer source label, and therefore reaches every prime label,
at a finite stage. For this width schedule a stage releases at most one
tooth. The source label is `n_m=1+ell_m`. The proof is BRT-02, together with
`a_j<=1/3`, so the nondecreasing integer counter cannot skip a value.

The program has a finite description, **not** a uniform bound on the bits of
its rational registers or its runtime. Each finite output demand terminates;
an infinite completed execution is not asserted. Compiling its rational and
integer operations into the earlier lambda observer is possible by ordinary
effective encodings, but this extension does not claim a new measured beta
trace for that compilation. The executed implementation is Python with exact
`Fraction` arithmetic.

For a cylinder of circumference `L>=1` integer teeth, retain

\[
c=n-1=Lh+r,\qquad 0\le r<L.
\]

The geometric display can be `(exp(2 pi i r/L), h+r/L)`; `(h,r)` is the exact
arithmetic address. The implementation restricts to the nondegenerate case
`L>=2`. The prior character `exp(2 pi i n/L)` differs from this display angle
by the declared constant phase `exp(2 pi i/L)`. SUCC and multiplication by
`d>=1` act as

\[
\begin{aligned}
S(h,r)&=\left(h+\left\lfloor\frac{r+1}{L}\right\rfloor,
                         (r+1)\bmod L\right),\\
V_d(h,r)&=\left(dh+\left\lfloor\frac{dr+d-1}{L}\right\rfloor,
                         (dr+d-1)\bmod L\right).
\end{aligned}
\]

The `d-1` term records our choice of source origin `n=1+c`. Dropping it
transports the wrong multiplication. These maps obey the authentic pointed
braid `V_d S=S^d V_d`. Forgetting `h` identifies different source integers
and destroys the global observer.

Categorically, let the time category be the ordered set of stages, and let
the successor path category have objects positive integers and arrows
`S^(v-u):u->v` for `v>=u`. The assignment

\[
m\mapsto n_m,\qquad (u\le v)\mapsto S^{\ell_v-\ell_u}
\]

is a functor: identities have exponent zero, and composition adds the
exponents. Waiting maps to an identity. This path action uses the additive
carrier already declared in `PRIME_WAVES.md`; SUCC is not falsely declared
an arrow of the pure divisibility category. A prime filter is a readout on
this carrier, not a demand that the moving carrier erase every composite
intermediate.

## 4. A genuine stochastic pawl can rectify the same wiggles

The support clock is a deterministic controller of a **distribution's
possible range**. It is not the typical trajectory `S_m`. To obtain literal
one-way stochastic motion, declare a pawl:

\[
Y_j=\max(U_j,0),\qquad X_m=\sum_{j=1}^mY_j.
\]

Then

\[
\mathcal L(Y_j)=\tfrac12\delta_0+
                  \tfrac12\operatorname{Unif}[0,a_j],
\qquad
\mathbb E e^{itY_j}=
\tfrac12+\tfrac12e^{ita_j/2}\operatorname{sinc}(ta_j/2).
\]

Here the phase is operationally defined by the translation of a uniform box;
it is not an inferred physical or quantum phase. Multiplying these factors
expresses the finite law as a mixture of shifted uniform convolutions, hence
of Borwein window calculations. The all-zero component has mass `2^-m` and
must be kept as an atom. The executable CDF retains it.

**Theorem BRT-05 (rectified progress).** For independent uniforms with any
deterministic positive finite widths,

\[
\boxed{X_m\longrightarrow\infty\ \text{almost surely}
       \quad\Longleftrightarrow\quad \sum_j a_j=\infty.}
\]

**Proof.** If the sum is finite, `0<=X_m<=sum a_j` pathwise. Conversely fix
`s>0`. Independence gives a product for the Laplace transform, and

\[
\mathbb E e^{-sY_j}=\frac12+\frac{1-e^{-sa_j}}{2sa_j},
\qquad
1-\mathbb E e^{-sY_j}\ge
\frac14(1-e^{-sa_j/2})\ge c_s\min(a_j,1),
\]

where `c_s=(1-e^(-s/2))/4>0`. The first bound restricts to `Y_j>=a_j/2`,
an event of probability `1/4`; the second uses concavity on `[0,1]` and
monotonicity above one. Divergence of `sum a_j` implies divergence of
`sum min(a_j,1)`. Therefore
`E exp(-s X_m)<=exp(-c_s sum min(a_j,1))` tends to zero. Monotonicity of
`X_m` and dominated convergence show `E exp(-s X_infinity)=0`, hence
`X_infinity=infinity` almost surely.

The moments are `E Y_j=a_j/4` and `Var(Y_j)=5a_j^2/48`. In particular the
odd-width clock has a diverging rectified mean, while the sum of its centered
variances is finite. Independent-series convergence gives

\[
X_m-\tfrac14 A_m\longrightarrow Z\quad\text{almost surely and in }L^2.
\]

An unrectified odd-width walk instead converges almost surely and in `L^2`.
That is a real difference caused by the one-way map.

For completeness, if independent centered increments `Z_j` have summable
variances, their partial sums are Cauchy in `L^2`. The first-crossing
decomposition gives the maximal inequality
`Pr(max_(n<=k<=M)|sum_(j=n)^k Z_j|>=t)<=sum_(j=n)^M Var(Z_j)/t^2`:
on each first-crossing event the remaining increment has conditional mean
zero, so the final second moment dominates `t^2` times the crossing
probability. Choose `n_r` with tail variance at most `2^(-3r)`, and put
`t=2^(-r)`. Taking `M` to infinity bounds the bad-tail probability by
`2^(-r)`. Its summability makes the tails Cauchy almost surely. Apply this
argument to `U_j`, and separately to `Y_j-a_j/4`. This supplies both
convergence statements without extrapolating a finite random trajectory.

Independence is essential. If all `U_j=a_j Z` share one
`Z~Unif[-1,1]`, the same marginals and divergent support budget coexist with
`X_m=0` for all `m` on an event of probability one half. Almost-sure progress
is also not progress of every path. A finite rule for a continuous random
transition uses an unbounded randomness/real-input model; it is not the
exact finite-rational machine of section 3. A discrete approximation changes
the Fourier kernel and must be declared as such.

## 5. A second Borwein bank fixes precisely the prime sector

Freeze a nonempty finite width bank `boldsymbol a` with
`A=sum a_j<=1`, for example `(1/3,1/5)`. Define

\[
B_{\boldsymbol a}(c)=M_{1,m}(c).
\]

**Theorem BRT-06 (exact degree filter).** At integer charges,

\[
\boxed{B_{\boldsymbol a}(c)=
 \begin{cases}1,&c=0,\\[2pt]1/2,&|c|=1,\\[2pt]0,&|c|\ge2.\end{cases}}
\]

Indeed, the continuous symmetric law of `S_m` is supported in `[-1,1]`.
The centered window contains all its mass. A shift by one contains exactly
one half, and a shift of magnitude at least two overlaps only an empty set
or an atom-free endpoint.

On `H=ell^2({2,3,...})`, let `Omega(n)` count prime factors with
multiplicity, `C e_n=(Omega(n)-1)e_n`, and let `P_j` project onto
`Omega(n)=j`. Functional calculus defines the bounded positive contraction

\[
\boxed{T=B_{\boldsymbol a}(C)=P_1+\tfrac12P_2.}
\]

Thus, for integer `r>=1`,

\[
\boxed{T^r=P_1+2^{-r}P_2,\qquad
       \|T^r-P_1\|=2^{-r},\qquad \operatorname{Fix}(T)=\operatorname{ran}P_1.}
\]

Semiprimes include prime squares. If the unit `n=1` is included, it has
charge `-1` and eigenvalue `1/2`, so it is suppressed. On that extended
carrier, fixing the unit too requires the explicit modification
`B(C)+(1/2)E_11`; it is not automatic.

This also realizes the requested fixed-point commutator on the previously
specified finite multiplier algebra. Here use the original carrier
`ell^2({1,2,...})`, including `e_1`. Let `V_d e_n=e_(dn)` and
`delta(X)=[N_Omega,X]`. Then `delta(V_d)=Omega(d)V_d`. Define on finite
linear combinations of these multipliers

\[
\mathcal T(V_d)=B_{\boldsymbol a}(\Omega(d)-1)V_d.
\]

Linear independence of `V_d` follows by applying a combination to `e_1`.
Consequently

\[
\boxed{\mathcal T(X)=X\iff \delta(X)=X
       \iff X\in\operatorname{span}_{\rm finite}\{V_p:p\text{ prime}\}.}
\]

The bounded positive-operator assertion concerns `T` on `H`. No positivity
or complete positivity is asserted for this coefficient map on a non-star
algebra, and the fixed-space statement is not extended to arbitrary
operators or adjoints. This is a new integral realization in this dossier,
not a new way to learn `Omega` without arithmetic source access. The charge
already encodes which labels are prime.

### Why the clock bank cannot also be the fixed readout bank

If its total width becomes greater than one, `B(0)<1`: primes stop being
fixed. Dividing by `B(0)` does not generally repair prime-only selection.
For one uniform of half-width three,

\[
B(0)=B(1)=B(2)=1/3.
\]

The normalized filter therefore fixes prime, semiprime and three-factor
charges alike. The plateau hypothesis is load-bearing.

The older factorial cardinal bank has the complementary property: its
extra half-width sum stays below `11/24` uniformly. It supplies a stable
embedding/readout and cannot cross every fixed integer support threshold.
Use that bank for its proved role; use a nonsummable clock for releases.

## 6. Growing support is not growing suppression or path survival

The following receipts distinguish plausible but different interpretations.

| Tempting inference | Counterexample or boundary |
|---|---|
| Unbounded finite-prefix support makes the unbiased walk wind forever | Odd reciprocal widths have divergent sum and square-summable variances; the centered random series converges almost surely |
| Infinitely many sinc factors eliminate every composite charge | At charge one, all odd-width partial sinc products are greater than `23/24` |
| A positive leak at every stage guarantees infinitely many sampled clicks | Two widths `(1+2^-k)/2` at stage `k` give leak `1/(2^k+1)^2`; the sum of event probabilities is finite |
| The endpoint Borwein gate is the probability of never leaving the window | For two independent uniforms `[-2,2]`, endpoint mass in `[-1,1]` is `7/16`, but survival at both steps is `1/4` |
| A circle retains support releases | On circumference two, `Unif[-1,1]` and that variable plus `Unif[-1/2,1/2]` both wrap to uniform, although the latter has line-window leak `1/8` |
| Any shifted score decreases as a width is added | With `b=1,c=9/4`, widths `(1)` give mass zero; adding `1/2` gives `1/64` |
| Width information authenticates a prime source | Permuting arithmetic labels leaves an unlabelled width distribution unchanged; the pointed SUCC/dilation braid is separate source information |

**Theorem BRT-07 (a rational non-suppression certificate).** For every
`m>=1`,

\[
\prod_{j=1}^m\operatorname{sinc}\!\left(\frac1{2j+1}\right)>\frac{23}{24}.
\]

Use `sinc(x)>=1-x^2/6` for `0<=x<=1`, and the finite inequality
`prod(1-b_j)>=1-sum b_j` for `0<=b_j<=1`. Since

\[
\sum_{j=1}^m\frac1{(2j+1)^2}
 <\frac14\sum_{j=1}^m\frac1{j(j+1)}<\frac14,
\]

the bound follows. The positive decreasing product has a limit at least
`23/24`. On the composite label `4`, the charge is one. Thus the raw
shrinking-width product is decisively different from the repeated fixed
window filter `T^r`, whose nonprime norm decays as `2^-r`.

For the summable-leak control, the first Borel--Cantelli conclusion can be
proved directly: the probability of any click after stage `K` is at most
`sum_(k>=K) 1/(2^k+1)^2`, which tends to zero. No independence of those click
events is required. Strictly positive leakage alone gives no recurrence.

## 7. What is gained, and what must still be paid for

The construction makes three resources explicit.

First, direction resides in a monotone controller or a declared rectifying
map. Symmetric convolution alone supplies neither. Second, a phase on a
circle loses winding; the cylinder's lift retains it. Third, symbolic access
to a support sum differs from detecting a tiny loss in an amplitude.

For the last distinction, suppose a measurement reports the normalized mass
with worst-case absolute error `epsilon`. The possible report intervals for
mass `1` and mass `1-lambda` overlap whenever `2 epsilon>=lambda`.
Consequently a guaranteed discrimination requires `epsilon<lambda/2` in
this observation model. The first three releases illustrate how quickly
this demand grows. The rational comparison `A_m>k` certifies release without
measuring that loss, but it requires exact source widths and growing integer
arithmetic. Neither route is resource-free. This is an elementary
observation-interface bound, not a universal lower bound for all algorithms.

The source observer visits composites between prime reports. Its readout
does not commute with SUCC: for example, `[T,S]e_3=-e_4/2` and
`[T,S]e_4=e_5/2`. A projection after every physical step is a different
dynamic; the earlier `P K_p P=0` control remains relevant.

The natural next research probe is therefore a **coupled source estimate**:
retain this explicit clock and prime readout, retain the authentic pointed
braid, and ask whether a predeclared interval or two-register observable
gets a new quantitative bound. It must distinguish the modulo 30 counterfeit
and positive-full-period/empty-interval controls in `PRIME_WAVES.md`.
The Borwein ratchet alone does not do so. Each next tooth is independent of
whether a chosen even sum contains a pair of prime source labels.

## 8. Claim ledger and reproducibility

| ID | Domain and conclusion | Truth state | Falsification / boundary |
|---|---|---|---|
| BRT-01 | Nonempty finite positive width bank: shifted window identity and exact plateau/zero boundaries | CLASSICAL ingredients; PROVED LOCAL normalization | Empty-bank endpoint convention excluded |
| BRT-02 | Positive rational widths with divergent sum: every strict integer tooth releases at finite time | PROVED LOCAL | Summable dyadic widths release no tooth at radius one |
| BRT-03 | Nonincreasing widths: every first release has an exact shallow-simplex certificate | PROVED LOCAL | Nonmonotone widths can leave the shallow regime |
| BRT-04 | Odd reciprocal clock plus retained lift visits every positive integer and every prime in finite prefix time | PROVED LOCAL; finite executable calibration | Finite description is not bounded memory, completed infinity, or a speedup |
| BRT-05 | Independent rectified uniform increments diverge almost surely iff their positive widths have divergent sum | PROVED LOCAL | Shared-noise countermodel stalls with probability one half |
| BRT-06 | Nonempty fixed bank with total width at most one gives `T=P_1+P_2/2`; prime fixed space and norm error `2^-r` | PROVED LOCAL | Width-three normalization fixes extra composite charges; source degree is supplied |
| BRT-07 | Odd-width sinc product at charge one stays above `23/24` | PROVED LOCAL rational bound | Infinite support does not imply spectral projection |
| BRT-08 | Declared interval-error observation needs `epsilon<lambda/2` to separate plateau from loss `lambda` | PROVED LOCAL within this measurement model | Exact symbolic source access is another interface |
| BRT-09 | A source-derived gain for universal prime-pair remainders | OPEN | Must defeat the existing source-transport and interval controls |

`borwein_ratchet.py` is the exact arithmetic implementation, with declared
width-count budgets on its general CDF queries;
`test_borwein_ratchet.py` checks its domains and independent finite controls.
`borwein_probe.py` records exact releases and calibration receipts.
`borwein_independent_audit.py` uses separate finite geometry where stated.
`BORWEIN_DERIVATION_AUDIT.md` and `reviews/borwein_adversary_audit.md` retain
the proof and countermodel audits. The audits share model provenance and
are not external peer review. See `VALIDATION.md` for actual runs, including
any retained failures. No run is inferred from this proof text.

The explanatory figure is reproducible from `plot_borwein_ratchet.py`.
Its curve samples and leakage logarithms are illustration, while the
release decisions and integer-charge values are exact rational certificates.

The subsequent [TRIADIC_TRANSPORT.md](TRIADIC_TRANSPORT.md) develops the
user's third-relation proposal. It distinguishes the first simple cycle
from the onset of dynamics or linear algebra, gives an exact twisted
incidence determinant, and compares a mixed arithmetic unit anchor with
counterfeit sources. Its source loops add a consistency observation to this
ratchet; they do not replace its explicit directional update.

## Primary sources

1. David Borwein and Jonathan M. Borwein, **Some Remarkable Properties of
   Sinc and Related Integrals**, *The Ramanujan Journal* 5 (2001), 73--89.
   [Original paper](https://gwern.net/doc/math/humor/2001-borwein.pdf).
   Theorem 1 and the convolution development support the classical plateau,
   boundary and integral framework. The author PDF is read, not redistributed.
2. Satya N. Majumdar and Emmanuel Trizac, **When random walkers help solving
   intriguing integrals**, *Physical Review Letters* 123, 020201 (2019).
   [Author manuscript](https://arxiv.org/abs/1906.04545),
   [PDF](https://arxiv.org/pdf/1906.04545).
   Equations (4)--(6) make the independent uniform-walk characteristic
   function and sinc integral explicit. Their random-walk explanation is
   an antecedent, not evidence for a source-specific prime theorem.

All claims specific to the present controller, lift and arithmetic charge
are supported by the derivations above. We make no literature-completeness
or priority claim for these elementary constructions.
