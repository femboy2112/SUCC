# Leah-Gamma observer bridge: preregistration and exact contract

Date: 2026-11-13. Baseline: `db9fb4b84672050efa79b13377f1e73364598a14`.
This file is written before the new observer probes are executed.

## Frozen source and word convention

The source remains
`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`,
`U_n=16 U_(n-1)+r(n)`. Completed `Y_n=U_n+T_n=16^n pi/16`.
No arbitrary seed average, zero data, or physical quantum claim is used.

An affine source letter is `F_j(u)=16u+r(j)`; its mathematical inverse
is `(u-r(j))/16`. A word is listed in chronological application order.
These letters are declared mathematical operations; arbitrary reorderings
are controlled experiments, not claims that actual source history was
executed in that order or that time travel is available.

## Frozen proof targets

1. Every ordered word is exactly `16^k u+c_W`, with rational offset.
   Source phase compensation is mandatory before comparing different words.
2. Matching scale cancels the seed and measures only the source offset.
   Nonmatching forward scales, at a matched integer character, retain
   frequency `h(16^k-16^l)` of the original state.
3. All such relative frequencies are divisible by 15; their full common
   kernel on the circle is the 15-torsion subgroup. Any higher-arity
   expression with integer charges summing to zero retains this kernel.
4. The chronological two-letter order defect is
   `15[r(n+a)-r(n+b)]`; its fixed-shift scaled limit is
   `(225/32)(b-a)n^-3` before multiplying by `n^3`.
5. The exact source differences `D_m(n)=sum_j(-1)^j binom(m,j)r(n+j)`
   are positive and satisfy two explicit beta-integral bounds, implying
   `n^(m+2) D_m(n) -> 15 Gamma(m+2)/64` for fixed `m`.
6. A uniform positive compensated relative-phase energy implies R0
   with an explicit frequency-squared loss and a paid BBP tail error.
   Such positivity is not assumed proved for the original zero-seed path.

## Frozen adversarial controls

The executable probe will use exact integers and `Fraction`, with no
floating trigonometric sign claims. Expected pass/fail/ambiguous outcomes:

- PASS: word composition agrees with independently iterated recurrence;
  reversing both order and inverses gives identity; a wrong inverse order
  gives the computed source-dependent translation.
- PASS: rational seed changes alter absolute states; equal-slope word
  differences remain unchanged, while unequal slopes retain the predicted
  seed coefficient. A source-only defect is not an absolute anchor.
- PASS: compensated matched-character comparisons are unchanged by adding
  `j/15`, for all 15 distinct classes in a fixed exact test grid. A grade-one
  absolute character separates those classes. This is a symbolic phase
  equality test modulo one, not a simulated physical measurement.
- PASS: the exact signed finite difference computed directly from four
  poles agrees with a separately expanded moment-polynomial integral.
  The two all-n rational bounds hold on a preregistered bounded grid
  `n in {1,2,5,17,64}`, `m in {0,1,2,3,4,5}`.
- FAIL by design: sorted words and order-erased offsets; same-seed metadata
  substituted for a checked present-time seed residual; an uncalibrated
  source phase treated as relative arithmetic phase; improper multiplier
  16 or source sign; illegal negative source indices and boolean inputs.
- AMBIGUOUS by design: every finite successful source/word calibration
  leaves the all-shell selected-path lower estimate open.

No test or scan is claimed at this preregistration stage. Final derivations,
actual run scope and limitations will be appended below without deleting
these frozen predictions.

---

## OB-01. The exact ordered affine carrier

Write `e(t)=exp(2 pi i t)`. For a word `W` in the letters `F_j` and
`F_j^(-1)`, applied in its listed order, let `k(W)` be its number of forward
letters minus its number of inverse letters. Then

\[
 W(u)=16^{k(W)}u+c_W,\qquad c_W\in\mathbb Q.                 \tag{1}
\]

**Proof.** Start with `(k,c)=(0,0)`. Appending a forward letter changes this
to `(k+1,16c+r(j))`; appending an inverse changes it to
`(k-1,(c-r(j))/16)`. Induction proves (1). In particular order is retained
in the offset, although the net scale alone is commutative. This is an
elementary affine-group calculation, not an assertion of academic novelty.

For two words, the difference is exactly

\[
 W(u)-V(u)=(16^{k(W)}-16^{k(V)})u+c_W-c_V.                 \tag{2}
\]

Equal net scales therefore measure only a known source offset. Unequal
scales can retain the selected state. Before interpreting a phase difference
as an arithmetic observation, remove `e(h(c_W-c_V))`; otherwise a source
offset can be mistaken for arithmetic disagreement. For nonnegative net
scales and a common integer character `h`, the compensated output is

\[
 e\{h[W(u)-V(u)-(c_W-c_V)]\}=e(qu),\quad
 q=h(16^{k(W)}-16^{k(V)}).                                \tag{3}
\]

There are three different comparisons here. Raw unequal-scale outputs
contain both (2) terms. Source-compensated, common-character outputs retain
the frequency in (3). A comparison whose characters are themselves chosen
to match the total scale cancels the state again. Changing those character
weights is a change of instrument, not merely a new verbal description of
the same two observers.

### Present-time backward transport with its branch record

Let the **same forcing** run from an explicitly declared seed `s`:

\[
 U_n(s)=16^ns+U_n(0),\quad
 T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad x=T_0=\pi/16,
 \quad \xi=s+x.
\]

Then `U_n(s)+T_n=16^n xi`. A word starting at clock `N`, with net exponent
`k` and final absolute clock `m=N+k >= 0`, has the exact completed and
compensated output

\[
 W(U_N(s))+16^kT_N-c_W=16^{N+k}\xi.                       \tag{4}
\]

This is an identity of unwrapped real values before passing to characters.
For a genuinely chronological backward step, the appropriate old source
index must also be retained. Arbitrary reordered words are declared
mathematical controls; (4) does not assert they are an executed history.
At negative `k`, `e(16^k u)` is **not** a well-defined function of `u mod 1`
alone. Its lift or inverse branch is extra data. Formula (4) uses that data
and rejects a negative final absolute clock. It never identifies an
unobserved infinite future boundary with a present-time measurement.

## OB-02. Full neutral relative-bank theorem

Define the completed neutral bank of an initial parameter `xi mod 1` to
contain **every finite** response

\[
 R_{\mathbf m,\mathbf a}(\xi)
   =e\!\left(\xi\sum_{j=1}^d a_j16^{m_j}\right),
 \qquad m_j\in\mathbb Z_{\ge0},\quad a_j\in\mathbb Z,
 \quad\sum_{j=1}^d a_j=0.                                \tag{5}
\]

The clock labels, charges, source offsets and completion in (4) are part
of this definition. The bank includes common-character two-observer
comparisons, three-channel products and all higher-arity neutral products.
Its arbitrary functions and finite compositions cannot distinguish points
that (5) does not distinguish.

**Theorem.** Two initial parameters have the same entire bank if and only if

\[
             15(\xi-\eta)\in\mathbb Z.                  \tag{6}
\]

Thus the bank reconstructs exactly `15 xi mod 1`, not `xi mod 1`.

**Proof.** Every frequency in (5) is divisible by 15, because
`16^m = 1 mod 15` and the charges sum to zero. Thus (6) suffices. Conversely
the bank contains clocks `(0,1)` and charges `(-1,1)`, whose frequency is
15. Equality of that response gives (6). This proves both the sufficiency
and necessity, with no finite-to-infinite extrapolation. ∎

**Precision of the word "full".** If only clocks `m>=m_0` are available,
and both `m_0,m_0+1` occur, the quotient in the *initial* parameter is instead
`15*16^m_0 xi mod 1`. Relative to the present state `16^m_0 xi mod 1`, it is
again fifteenfold. Returning to clock zero with authenticated branch data
removes the radix-prefix ambiguity but still leaves the 15-torsion in (6).
For another declared clock subset, the common kernel is governed by the
greatest common divisor of its actual integer frequencies. A weak or finite
sub-bank can lose more information than (6).

**Higher arity.** No finite or unbounded arity of the neutral family removes
this kernel: the same congruence holds term by term. This does not say that
all higher-arity instruments fail. Nonneutral charges, an absolute phase
reference, or a different source/clock coupling are genuinely different
observables. In particular `e(xi)` resolves all 15 members of each fiber.
It is extra reference access. No common eigenvector or quantum mechanism is
used anywhere in the proof.

### A sharp target-ambiguity control, with the tail kept

For `j=0,...,14`, keep the original forcing but set the **wrong** seed

\[
 s_j=j/15-x,\qquad
 U_n(s_j)=16^n(j/15)-T_n,
 \qquad Y_n(s_j)=U_n(s_j)+T_n=16^n(j/15).                 \tag{7}
\]

All 15 neutral banks are identical, since the completed orbit has constant
phase `j/15` and every total charge is zero. Yet

\[
 \frac1B\sum_{n=B}^{2B-1}[1-\cos(2\pi Y_n(s_j))]
       =1-\cos(2\pi j/15).                              \tag{8}
\]

For `j=0` it is zero, so R0 fails. For each `j=1,...,14` it is strictly
positive, so R0 holds. The comparison is an exact **same-forcing,
wrong-seed** pair, not a Goldbach counterexample, a π counterexample or a
pair consistent with all source authentication. Every seed in (7) differs
from zero. The full original source contract, including literal `U_0=0`,
has a singleton trajectory; no distinct pair can satisfy that complete
contract. Even after zero-seed authentication identifies that trajectory,
its R0 estimate still requires proof.

The executable control represents `x=pi/16` symbolically. At clock `n`, its
state has coefficients `(-16^n, U_n(0)+16^n j/15)` and its tail has
`(16^n,-U_n(0))`. Only their sum cancels `x`. The report exposes both pairs;
the tail has not been silently deleted. On raw source phases the discrepancy
from (8) tends to zero by the quantitative bound in OB-04.

## OB-03. The positive ordered curvature and its Gamma endpoint

For fixed source indices `a,b`, applying `F_a,F_b` and applying `F_b,F_a`
give the same slope 256 and offset difference

\[
 (F_b\circ F_a)(u)-(F_a\circ F_b)(u)=15[r(a)-r(b)].       \tag{9}
\]

The chronological word `F_a,F_b,F_a^(-1),F_b^(-1)` has the exact action

\[
 u\longmapsto u+\frac{15}{256}[r(a)-r(b)].               \tag{10}
\]

Reversing the order of the inverse letters instead gives the identity.
Both facts follow by direct substitution in (1). Thus order is detectable
without pretending that a loop measures the absolute seed.

There is a useful all-order source theorem. For `m>=0` let

\[
 D_m(n)=\sum_{j=0}^m(-1)^j\binom mjr(n+j),\qquad n\ge1.
\]

Put

\[
 g(z)=4-2z^3-z^4-z^5=(1-z)K(z),\quad
 K(z)=(z^2+2)(z^2+2z+2).
\]

Termwise integration of four monomials and the finite binomial identity give

\[
 D_m(n)=\int_0^1z^{8n-8}(1-z)K(z)(1-z^8)^m\,dz>0.       \tag{11}
\]

On `[0,1]`, expansion of `K=4+4z+4z^2+2z^3+z^4` gives
`15z^4<=K<=15`; also
`8z^7(1-z)<=1-z^8<=8(1-z)`. Apply these pointwise inequalities to (11).
Repeated integration by parts gives
`int_0^1 z^(a-1)(1-z)^(m+1) dz=(m+1)!/[a(a+1)...(a+m+1)]`
for `a>0`. Therefore, for **every** `n>=1,m>=0`,

\[
 \boxed{
 \frac{15\,8^m(m+1)!}{\prod_{j=0}^{m+1}(8n-3+7m+j)}
 \le D_m(n)\le
 \frac{15\,8^m(m+1)!}{\prod_{j=0}^{m+1}(8n-7+j)}.}         \tag{12}
\]

These are exact rational bounds, not an asymptotic fit. For each **fixed**
`m`, multiply by `n^(m+2)` and squeeze:

\[
 \boxed{\lim_{n\to\infty}n^{m+2}D_m(n)
                =\frac{15\Gamma(m+2)}{64}.}             \tag{13}
\]

Here `Gamma(m+2)=(m+1)!` is Euler's Gamma function, not Euler–Mascheroni's
constant. No uniform growing-`m` asymptotic is asserted. In particular, for
fixed integer shifts `a,b` with the indices eventually positive,

\[
 n^3\,15[r(n+a)-r(n+b)]\longrightarrow
                   \frac{225}{32}(b-a).                 \tag{14}
\]

For `a<b`, telescope the difference into the `b-a` adjacent first
differences and use (13); reverse the sign for `a>b`.

**A realizable ordered-word hierarchy.** The chronological edge
`F_j,F_(j+1)^(-1)` translates by `D_1(j)/16`. For `m>=1`, compose these
translation edges with integer signed multiplicities
`(-1)^j binom(m-1,j)`, `0<=j<m`; a negative multiplicity uses the actual
inverse word. The result translates by `D_m(n)/16`. The displayed
construction contains exactly `2^m` affine letters. It does not provide a
free arbitrarily high-order measurement. The Gamma hierarchy is a
source-conditioned, signed difference invariant with a concrete cost.

**Why this is not a π estimate.** Equations (9)–(14) hold unchanged for
every seed, including all the incompatible R0 behaviors in (7). A shrinking
raw defect can have a nonzero normalized limit while giving no uniform
positive arithmetic phase energy. The new connection to the old positive
BBP moment carrier is useful for calibrating the ordered instrument; a
source-only positivity theorem cannot supply the missing selected-path
positivity theorem.

## OB-04. The first conditional arrow to R0, quantitatively paid

For the authentic zero seed define

\[
 E_B(q)=\frac1B\sum_{n=B}^{2B-1}
               [1-\cos(2\pi qY_n)],\quad Y_n=16^n\pi/16,
 \quad R0:\ \liminf_{B\to\infty}E_B(1)>0.
\]

For every integer `q!=0` and every real `y`,

\[
 1-\cos(2\pi qy)\le q^2[1-\cos(2\pi y)].               \tag{15}
\]

For `q>0`, write `z^q-1=(z-1)(1+...+z^(q-1))`, `|z|=1`, take absolute
values and square; `|z-1|^2=2(1-Re z)`. Negative `q` follows by conjugation.
Thus `E_B(1)>=E_B(q)/q^2`.

If words of fixed nonnegative net exponents produce the compensated raw
phase `e(qU_n)` in (3), put

\[
 \widehat E_B(q)=B^{-1}\sum_{B\le n<2B}[1-\Re e(qU_n)].
\]

The genuine source tail has `0<T_n<=47/[225(n+1)^2]`. The derivative bound
of cosine and `2 pi<44/7` give the explicit transfer

\[
 |\widehat E_B(q)-E_B(q)|
 \le \frac{44|q|}{7B}\sum_{n=B}^{2B-1}T_n
 \le \frac{2068|q|}{1575(B+1)^2}.                        \tag{16}
\]

Combining (15) and (16),

\[
 \boxed{E_B(1)\ge
 \frac{\widehat E_B(q)-2068|q|/[1575(B+1)^2]}{q^2}.}       \tag{17}
\]

This is the first conditional π arrow for the two-observer construction:

> For the original four poles and literal zero seed, a proved constant
> `delta>0`, a fixed nonzero accessible integer `q`, and a `B_0` such that
> `widehat E_B(q)>=delta` for **every** `B>=B_0` imply R0.

The source-curvature theorem does not prove this premise. A finite packet
of positive shell values does not prove it either. For the nearest two
scales `q=15`, this is the already known stronger mode-15/(CH) route; the
new result identifies exactly why it can miss the distinction needed by
R0. The converse is false by (7). Allowing `q` to grow with the shell needs
a fresh argument: (16) pays a growing frequency error and (17) loses
`q^2`; a fixed positive observed margin with `q(B)->infinity` does not give
a fixed R0 margin.

No signed Basel tail is introduced as a renamed target here. A Basel
transport would need a separately controlled source quantity strong enough
to prove its required decay. This note supplies an exact observation
quotient and a stronger conditional route; it does not supply that analytic
control.

## Overlap, novelty boundary and source contracts

1. **APH-01**, `research/2026-11-07/pinbed_yoneda_oscillators/ANCHORED_PATHS_VS_HOLONOMY.md`
   on pinned main, proves that source-corrected temporal loops whose total
   scale is matched are seed blind. **APH-02** proves finite-precision
   periodic-seed impersonation, while explicitly retaining a separate
   literal zero selector. OB-01 respects both. OB-02 generalizes from the
   flat matched-scale loop subfamily to the full neutral relative bank,
   which has real arithmetic content but exactly 15 residual phase classes.
2. **PR #602**, `frontier_rungs/LIMIT_FACES.md`, already separates R0 from
   R1 and (CH), and already uses the fixed points `j/15`. We do not claim to
   discover those points. OB-02 proves that they are exactly the ambiguity
   fiber of the declared all-arity observer bank, and (7) supplies the
   explicit same-forcing source realizations with their tails.
3. **PR #605**, head `8fa0fe392f8c59f168a5d59a1f9c998c9e0de814`,
   `holographic_boundary_filters/PHASE_AND_TARGET.md`, proves finite
   torsion/target-ambiguity statements and distinguishes observable
   reconstruction from target descent. This is the same research lineage,
   not independent evidence. OB-02 supplies a complete character-family
   kernel for this actual affine source action, rather than a generic
   finite readout example.
4. `GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md` already gives the positive BBP
   density, its cyclic vector, moment comparison and finite-moment
   counterfeits. OB-03 uses that exact density; its explicit all-order
   beta bounds, normalization and ordered-loop realization are the local
   extension. This is elementary finite-difference/Beta calculus; academic
   priority has not been checked.
5. **PR #601/#604** separate current-frame Hilbert transport, source
   authentication and arithmetic estimates. Their same-model proof notes
   are provenance leads, not independent validation of this theorem. The
   exact source pin remains `16^(-n)U_n - sum_(j<=n)16^(-j)r(j)=s`.

## Executed scope and ledger

Executed on 2026-11-13:

```sh
cd research/2026-11-13/leah_gamma_twist
python -m unittest -v test_observer_probe
```

**Observed:** 14 tests, zero failures/errors. The compiled-word control
checks every word of length at most four over three declared letters and
three rational seeds. The independent sequential interpreter does not call
the compiler. The moment control checks the frozen 30 `(n,m)` cells using
direct four-pole finite differences versus independently expanded
polynomial integration. `observer_results.json` records those exact
fractions and bounds, all 15 symbolic wrong-seed states and retained tails,
the charged patterns, loop translation and source/test SHA256 hashes.
The finite arithmetic checks are alternative implementations with shared
source and same-model provenance, not blind external witnesses.

| Claim | Status | Remaining boundary |
|---|---|---|
| OB-01 ordered source action and present-time completion | Disclosed by exact algebra | Physical access to arbitrary words is not asserted |
| OB-02 full neutral-bank quotient, all-arity torsion and target ambiguity | Disclosed by exact proof | Extra absolute-reference probes are outside this bank |
| OB-03 positive differences, beta bounds, fixed-order Gamma limits | Disclosed by integral proof | Uniform growing-order limits not supplied; seed blind |
| OB-04 relative energy implies R0 with paid loss | Disclosed conditional implication | Uniform zero-seed relative energy remains open |
| 14 local tests / 30 grid cells / 15 torsion records | Observed exact finite scope | No finite-to-infinite statistical inference |
| Authentic π R0, higher rungs, normality | UNVERIFIED here; existing open frontier | Need an actual source-selected all-shell inequality |

No native repository suite, Lean kernel, external referee, commit or
publication was run by this subagent.

---

## OB-05. A prime-cofactor regression candidate with a paid tail

**Added after the initial protocol, 2026-11-13.** This addendum is a new
paper derivation requested during the final cross-audit. No new code,
numerical scan, independent external witness or finite holdout is claimed
for it. The two uniform arithmetic premises below are **OPEN**. The exact
factorization, conditional inequality, finite strictness and error-transfer
lemmas are proved here.

### 1. The actual prime birth and its pulse-free interval

Let `B>=2` be an integer. Suppose a genuine prime `p=1 mod 8` has integer
birth time

\[
 a=(p+7)/8,\qquad B\le a\le 5B/4.
\]

Equivalently `8B-7<=p<=10B-7`. Define the integer interval

\[
 I=\{a,a+1,\ldots,2B-1\},\qquad L=2B-a\ge 3B/4.         \tag{18}
\]

The choice of a prime in this range is explicit hypothesis data. This
lemma does not obtain a phase estimate from mere prime existence, nor
average over possible prime choices.

The first denominator divisible by `p` in the original source is
`8a-7=p`, with atom `4/p`. To locate the next pulse, write a possible
denominator as `kp`. Since `p=1 mod 8`, the four poles require respectively
`k=1,4,5,6 mod 8`. After the first `k=1` pulse, the earliest possibilities
have source times

\[
 4a-3,\quad 5a-4,\quad 6a-5,\quad 9a-7.
\]

The first is `n=(p+1)/2=4a-3`, where `8n-4=4p`. The interval (18) ends
strictly before it: `2B-1<4a-3` for `a>=B`, `B>=2`. Hence there is no
second `p`-pulse on `I`.

For the original literal zero seed define the **accumulated cofactor**

\[
 q_n=4\,16^{n-a}/p,\qquad R_n=U_n(0)-q_n,\qquad n\in I.
\]

Every `R_n` is rational with reduced denominator coprime to `p`. All source
denominators before `a` are smaller than `p`; at `a` subtract the displayed
atom; afterwards every remaining source term up to `n` is `p`-free.
Multiplication by 16 preserves that property. This proves the assertion
by induction. In particular the `p`-part of `U_n(0)` cannot cancel: after
putting `q_n+R_n` over `p` times a `p`-coprime denominator, its numerator is
nonzero modulo `p`.

The word "cofactor" does **not** mean a frozen old prefix. `R_n` contains
all later `p`-free forcing up to `n`, including the births of other primes.
The completed character is exactly

\[
 e(Y_n)=A_nB_n,\qquad
 A_n=e(q_n),\qquad B_n=e(R_n+T_n).                        \tag{19}
\]

The raw factor `B_n^0=e(R_n)` has the finite `p`-free rational passport.
`B_n` includes the genuine tail and should not be assigned that same
finite-conductor passport. The source index, sign, ordering and zero seed
are retained throughout (19).

### 2. A strict covariance fraction yields a shell margin

Let `E_I` mean the uniform average over `I`. Set

\[
 \alpha=E_IA,\quad\beta=E_IB,\quad
 C=E_I[(A-\alpha)(B-\beta)],\quad
 v_A=1-|\alpha|^2,\quad v_B=1-|\beta|^2.
\]

This is a **non-Hermitian** covariance: the product inside `C` has no
conjugation. It is precisely the covariance in
`E_I(AB)=alpha beta+C`.

Suppose, for constants `0<epsilon<=1` and `0<delta<=1`,

\[
 |\alpha|\le1-\epsilon,\qquad
 |C|\le(1-\delta)\sqrt{v_Av_B}.                          \tag{20}
\]

Then

\[
 \boxed{|E_I(AB)|\le
 K:=\sqrt{1-(2\delta-\delta^2)(2\epsilon-\epsilon^2)}<1.} \tag{21}
\]

**Proof.** Write `u=|alpha|`, `v=|beta|`, `rho=1-delta`. Triangle
inequality followed by the real two-dimensional Cauchy–Schwarz inequality
gives

\[
 |E_I(AB)|\le uv+\rho\sqrt{(1-u^2)(1-v^2)}
 \le\sqrt{u^2+\rho^2(1-u^2)}
 \le K.
\]

The last expression increases with `u` for `0<=rho<=1`, so substitute
`u<=1-epsilon`. If `v_B=0`, then `C=0`; the same argument remains valid.
This is not an independence assumption: the covariance in (20) may be
nonzero and large, provided it stays a uniform fraction below its maximal
possible size.

The scalar bound is sharp over unrestricted laws of unit-modulus complex
pairs. For `K>0`, take balanced signs `X,Z` with `E(XZ)=rho`, set
`u=1-epsilon`, `v=u/K`, and use
`A=u+i sqrt(1-u^2)X`, `B=v-i sqrt(1-v^2)Z`. The four sign-pair probabilities
are `(1+rho XZ)/4`, and the bound is attained. The case `K=0` is immediate
with zero mean and zero covariance. This is a calibration law, **not** an
arithmetic realization of (19).

On the rest of `[B,2B)` a unit character has magnitude at most one. Thus

\[
 \boxed{|W_B(1)|\le1-\frac LB(1-K)
                   \le1-\frac34(1-K).}                 \tag{22}
\]

Its real part obeys the same bound. If for **every sufficiently large B**
there is an admitted prime with the same positive constants in (20), the
result is a uniform **first-mode modulus saving R1**, hence the weaker R0
with margin at least `3(1-K)/4`. It is stronger than the requested minimum
target. No uniform instance of either premise in (20) has been established
for the actual source by this addendum.

### 3. The corresponding regression residual

Since (20) makes `v_A>0`, define

\[
 \mathcal R(B)=
 \inf_{\lambda\in\mathbb C}
 E_I|B-\beta-\lambda\overline{(A-\alpha)}|^2
 =v_B-\frac{|C|^2}{v_A}.                                \tag{23}
\]

Expanding the square gives
`v_B-2 Re(conjugate(lambda) C)+|lambda|^2 v_A`; its minimizer is
`lambda=C/v_A`. The predictor is `conjugate(A)`, not `A`. Equivalently,
`R(B)` is the squared distance of `B` from the complex span of
`{1,conjugate(A)}` in the finite `L^2(I)` space.

With `eta=2delta-delta^2 in (0,1]`, the covariance premise is exactly

\[
                    \mathcal R(B)\ge\eta v_B.            \tag{24}
\]

This is a concrete source-conditioned defect against the conjugate prime
factor. It allows general coupled behavior and does not replace the joining
by the product of its marginals. The fact that it has a name and a finite
formula does not establish a uniform lower bound.

An absolute bound `R(B)>=r>0` would itself imply
`|E_I(AB)|<=sqrt(1-r)`: orthogonally project `B` onto
`span{1,conjugate A}` and pair it with the unit vector `conjugate A`.
This alternative remains an unproved source estimate and need not follow
from the relative condition if `v_B` tends to zero.

### 4. Strictness on each fixed authentic interval is elementary

For `p>17` and `L>=3`, the first three `A_n` are distinct. Otherwise the
order of 16 modulo `p` would be at most two, forcing `p` to divide
`16^2-1=255`; among primes `1 mod 8` this leaves only 17. Thus `v_A>0`.

Also `v_B>0` on the authentic path. If `B` were constant, equality at two
consecutive clocks would imply

\[
 15\,16^n x-(q_{n+1}-q_n)\in\mathbb Z,
 \qquad x=\pi/16,
\]

contradicting irrationality of `x`, since the second term is rational.

Suppose `R(B)=0`. A finite sum of nonnegative squares can vanish only
pointwise, so

\[
                   B_n=c_0+c_1\overline{A_n}
 \quad\hbox{for every }n\in I.
\]

As `|A_n|=|B_n|=1`, expansion of the second modulus makes
`Re(c_0 conjugate(c_1) A_n)` constant. If `c_0 conjugate(c_1)` were nonzero,
this would put three distinct unit-circle points on one line, which is
impossible. Hence `c_0=0` or `c_1=0`. The second case makes `B` constant,
already excluded. The first gives `AB=c_1` constant, so two consecutive
clocks imply `15*16^n x` is an integer, again impossible. Consequently

\[
 v_A>0,\quad v_B>0,\quad\mathcal R(B)>0,
 \quad |C|<\sqrt{v_Av_B}                                \tag{25}
\]

on each such fixed authentic interval.

This only supplies interval-dependent positive `epsilon_(B,p)` and
`delta_(B,p)`. Irrationality excludes equality; it supplies no uniform
positive distance from equality. Equation (25) is not a proof of (20)
with fixed constants, and finite strictness is not an R1 or R0 advance.

A related raw statement uses the rational passport alone. If `B^0` is
nonconstant and its regression residual vanishes, the same circle argument
forces `B^0=c conjugate A`. Ratios at two different `A` values would then
be both nontrivial `p`-th roots of unity and roots with order coprime to
`p`, a contradiction. The constant-`B^0` case has zero variance and must
be treated separately. Again this gives no uniform gap: for a fixed
finite interval, arbitrary rational numbers with a common denominator
coprime to `p` can approximate `-q_n` as closely as desired. Their phases
approach `conjugate A` and their normalized regression defect approaches
zero. These are relaxed cofactor controls; they do **not** obey the full
original forcing and zero-seed contract.

### 5. Pay the exact tail when testing the raw rational cofactor

The following simpler source bound supplies a transparent rational error
budget. Put `(d,v)=(3,2),(4,1),(5,1)`. Direct regrouping gives

\[
 r(n+1)=\sum_{d,v}\frac{vd}{(8n+1)(8n+1+d)}
          <\frac{15}{(8n+1)^2}.
\]

These positive summands decrease with `n`. Therefore for every `n>=1`,

\[
 T_n=\sum_{j\ge1}16^{-j}r(n+j)
 \le\frac{r(n+1)}{15}
 <\frac1{(8n+1)^2}<\frac1{64n^2}.                       \tag{26}
\]

Since `B_n=B_n^0 e(T_n)`, the chord bound and `pi<22/7` give on `I`

\[
 \|B-B^0\|_{L^2(I)}
 \le 2\pi\max_{n\in I}T_n
 <\frac{\pi}{32a^2}
 <\kappa_a:=\frac{11}{112a^2}.                          \tag{27}
\]

Use the same fixed `A` for both regressions. Distance from any fixed closed
subspace is 1-Lipschitz, so

\[
 |\sqrt{\mathcal R(B)}-\sqrt{\mathcal R(B^0)}|\le\kappa_a.
\]

Both squared distances are at most one. Projection onto constants gives
the identical argument for the variance. Thus

\[
 \boxed{|\mathcal R(B)-\mathcal R(B^0)|\le2\kappa_a,
        \qquad |v_B-v_{B^0}|\le2\kappa_a.}               \tag{28}
\]

In particular the exact raw-source inequality

\[
 \boxed{\mathcal R(B^0)-\eta v_{B^0}
                         \ge2(1+\eta)\kappa_a}           \tag{29}
\]

is sufficient for (24). No ill-conditioned division by a small variance is
used in this error transfer. The raw phases are computed from the actual
zero-seeded rational `U_n` and the declared prime atom. Their mathematical
availability is not a zero-cost response oracle; finite evaluation and any
additional numerical error must still be paid. This addendum does not run
that evaluation or prove (29) uniformly.

### 6. The coherent control is a real wrong-seed control

Keep the same forcing, but take `s=-x`. Then

\[
 U_n(s)=-T_n,\quad R_n(s)=-T_n-q_n,\quad
 B_n(s)=e(R_n(s)+T_n)=\overline{A_n}.
\]

The genuine tail is included before it cancels. Hence
`beta=conjugate(alpha)`, `C=v_A`, `v_B=v_A` and `R=0`. This kills the
strict covariance premise, as it should. But `R_n(s)` is irrational:
the initial seed has changed by `-pi/16`. It is a **real-phase,
wrong-seed** control, not a member of the original rational cofactor
passport or the literal zero-seed trajectory.

More generally `s=j/15-x` gives
`B=e(j/15) conjugate A` and still has maximal normalized covariance and
zero regression residual. For `j!=0` it satisfies R0 yet fails the proposed
strict covariance premise. This confirms that the candidate is stronger
than R0, in agreement with its R1 conclusion.

There are no two distinct trajectories compatible with the full original
forcing **and** literal `U_0=0`. The wrong-seed controls diagnose which
assumptions carry the argument; they do not refute a future source-specific
proof. The outstanding task is now explicit: establish a uniform prime-line
saving and a uniform source-conditioned residual inequality, with the
actual cofactor joining retained and (27)–(29) paid. Both uniform estimates
remain open in this addendum.
