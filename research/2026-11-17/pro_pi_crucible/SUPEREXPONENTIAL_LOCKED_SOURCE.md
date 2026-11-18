# A superexponentially matched, radix-locked source with the same four finite clock poles

## Status and exact purpose

**PROVED PAPER / REFUTATION OF A BROADER SOURCE-CLASS INFERENCE.** This is
an explicit changed-source countermodel. It does not prove or refute R0 or
normality for the original four-pole rational function with the literal zero
seed. It is a strict strengthening of two existing SUCC countermodels, with
no claim of external academic priority.

The inherited CAT-12/13 construction in
`research/2026-10-30/carrier_adelic_transport/ALL_ORDER_SHADOW.md` retains every
asymptotic source coefficient and an arbitrary finite authentic prefix, but
its rational completed endpoint can have a nonzero periodic phase and thus
need not fail the particular R0 test. The inherited TW-07 construction at
PR #662 has a radix-rational locked endpoint, positive decreasing forcing,
and an arbitrary exact authentic prefix, but matches only the leading
asymptotic coefficient. The theorem below simultaneously strengthens these
properties and retains all four finite clock poles by an explicitly
nonrational entire correction.

**Predeclared candidate and falsifier.** Attempt to force R0 from the literal
zero seed, any finite authentic history, positive decreasing rational-valued
forcing, all original asymptotic coefficients, and the four finite
meromorphic clock poles with their signed principal parts. A source satisfying
all these properties with a radix-rational endpoint falsifies that proposed
inference. Exact membership in the original rational-function class is
deliberately not among these broader hypotheses; if it is required, the
countermodel is rejected and says nothing against the original target.

## 1. Original source and elementary bounds

Retain the original source as reference:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write

\[
P_M=\sum_{j=1}^M16^{-j}r(j),\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad x=P_M+16^{-M}T_M=\pi/16.
\]

Define the exact rational positive gaps and tolerances

\[
d_n=r(n)-r(n+1)\quad(n\ge1),\qquad
\epsilon_n=\frac{16^{-(n+1)^2}d_{n+1}}{1024}\quad(n\ge0).
\tag{H1}
\]

The elementary source integral

\[
r(n)=\int_0^1t^{8n-8}Q(t)\,dt,\quad
Q(t)=4-2t^3-t^4-t^5
=(1-t)(4+4t+4t^2+2t^3+t^4)
\]

proves `r(n)>r(n+1)>0` and `d_n>d_(n+1)>0` for every n. Also

\[
\frac{r(n+1)}{16}<T_n<\frac{r(n+1)}{15},\qquad
0<\epsilon_n<\frac{r(n+1)}{1024}<\frac{T_n}{64}.
\tag{H2}
\]

The source-tail upper bound follows by strict decrease; the lower bound is
the first term of the positive sum. All finite source data below are rational.

## 2. A finite algorithm chooses the exactly locked endpoint

Fix any integer M>=0. Choose integers L>=M and K>=M such that

\[
16^{M-L}\frac{r(L+1)}{15}<\frac{\epsilon_M}{4},
\qquad 16^{M-K}<\frac{\epsilon_M}{4}.
\tag{H3}
\]

These can be found by increasing integers and exact rational comparisons;
both searches terminate by geometric decay. Put

\[
q=16^{-K}\lceil16^KP_L\rceil\in\mathbb Z[1/16],
\qquad g_M=16^M(q-P_M).
\tag{H4}
\]

Since `P_L<x<P_L+16^(-L)r(L+1)/15`, while
`P_L<=q<P_L+16^(-K)` (the weak inequality at the lower endpoint is harmless),

\[
|g_M-T_M|=16^M|q-x|<\epsilon_M/4<\epsilon_M.
\tag{H5}
\]

In particular `g_M>0`. No equality decision about pi, no pi digit oracle,
and no irrational coefficient is used: q is calculated from finitely many
literal four-pole fractions and a rational ceiling.

For each n>M choose any integer L_n>=1 satisfying

\[
16^{-L_n}\frac{r(n+L_n+1)}{15}<\epsilon_n,
\qquad
g_n=\sum_{j=1}^{L_n}16^{-j}r(n+j)\in\mathbb Q.
\tag{H6}
\]

Again this is a terminating exact rational search. The authentic tail identity
gives

\[
0<T_n-g_n=16^{-L_n}T_{n+L_n}<\epsilon_n.\tag{H7}
\]

Thus every g_n is computable from a finite authentic prefix, is positive,
and tends to zero.

## 3. Quantified source theorem

Define the altered forcing and its literal-zero recurrence by

\[
\widetilde r(n)=
\begin{cases}
r(n),&1\le n\le M,\\
16g_{n-1}-g_n,&n>M,
\end{cases}
\quad
\widetilde U_0=0,\quad
\widetilde U_n=16\widetilde U_{n-1}+\widetilde r(n).
\tag{H8}
\]

### Theorem H-01: exact prefix, all-order matching, and monotonicity

For every integer M>=0, the construction gives a rational-valued sequence
with exact equality through M and, for every integer n>=1,

\[
\boxed{|\widetilde r(n)-r(n)|
<\frac{17}{1024}\,16^{-n^2}d_n.}\tag{H9}
\]

Moreover, for every n>=1,

\[
\boxed{\widetilde r(n)>\frac{1007}{1024}r(n)>0,\qquad
\widetilde r(n)-\widetilde r(n+1)>\frac{495}{512}d_n>0.}\tag{H10}
\]

**Proof.** Let e_n=g_n-T_n for n>=M and
`delta_n=r_tilde(n)-r(n)`. For n<=M, delta_n=0. For n>M, use the authentic
identity `r(n)=16T_(n-1)-T_n` to obtain

\[
\delta_n=16e_{n-1}-e_n,
\quad |\delta_n|<16\epsilon_{n-1}+\epsilon_n
<\frac{17}{1024}16^{-n^2}d_n,
\]

because d_(n+1)<d_n. Since d_n<r(n), the positivity estimate follows. For
all n, including the seam n=M,

\[
\widetilde r(n)-\widetilde r(n+1)
\ge d_n-|\delta_n|-|\delta_{n+1}|
>\left(1-\frac{34}{1024}\right)d_n=\frac{495}{512}d_n.
\]

There is no exceptional seam or unproved eventual monotonicity. QED.

Consequently, for every real A>0,

\[
n^A(\widetilde r(n)-r(n))\longrightarrow0.
\]

Since the original rational r(n) has a full inverse-power asymptotic
expansion at infinity, every coefficient of this expansion is retained.
This is stronger than matching any prescribed finite number of coefficients.
It is not equality of the forcing laws.

### Theorem H-02: exact eventual phase lock and the terminal norm

For every integer n>=M,

\[
\boxed{\widetilde U_n=16^nq-g_n,\qquad
\sum_{j\ge1}16^{-j}\widetilde r(j)=q.}\tag{H11}
\]

**Proof.** At n=M the equality is H4 and
`U_tilde_M=16^MP_M`. H8 then proves it by induction. Divide by 16^n and
let n tend to infinity; g_n tends to zero. Equivalently, the positive
completed tail of the new forcing is exactly g_n, since finite telescoping
and the boundedness of g give

\[
\sum_{j\ge1}16^{-j}\widetilde r(n+j)=g_n\quad(n\ge M).
\]

Because q has denominator dividing 16^K, its completed orbit has phase 1
for every n>=K. This refutes R0 for the altered source, not just some
higher Fourier-mode normality criterion.

For every B>=max(1,M,K), one has 0<g_(2B)<1 and
`16^(2B)q` is divisible by 16^B. Hence

\[
\lfloor\widetilde U_{2B}\rfloor=16^{2B}q-1,
\qquad \widetilde D_B=\widetilde J_B=0.
\tag{H12}
\]

Every last-B hexadecimal digit is F. The exact raw terminal norm is

\[
\boxed{\widetilde{\mathcal R}_B
=\frac{g_{2B}^2(1-16^{-2B})}{255B}
\sim\frac1{16711680B^5}.}\tag{H13}
\]

For the equality, divide H11 by 16^k for 1<=k<=B: the integer part from q
is integral and the torus distance equals g_(2B)/16^k. Sum the geometric
squares. For the asymptotic, the original rational source has
`r(n)~15/(64n^2)`. Dominated convergence in its geometric tail gives
`T_n~1/(64n^2)`; H7 is superexponentially smaller, so g_n has the same
asymptotic. At n=2B the coefficient is 1/256, and 255*256^2=16711680.

## 4. The exact same finite clock poles still do not suffice

Extend the rational perturbation sequence by delta_n=0 for n<=M, and set

\[
F(z)=\sum_{n=M+1}^{\infty}\delta_n
e^{-(z-n)^2}\operatorname{sinc}(\pi(z-n)),
\qquad \operatorname{sinc}(w)=\begin{cases}\sin w/w,&w\ne0,\\1,&w=0.
\end{cases}
\tag{H14}
\]

### Theorem H-03: entire interpolation with exact signed clock poles

F is a real entire function with F(k)=delta_k for all positive integers k.
The meromorphic function

\[
\widetilde r_{\mathrm{mer}}(z)=r(z)+F(z)
\]

therefore produces the H8 sequence at every clock n, and has **exactly the
same four finite poles and signed principal parts as r**:

| Pole | Residue |
|---|---|
| 7/8 | 1/2 |
| 1/2 | -1/4 |
| 3/8 | -1/8 |
| 1/4 | -1/8 |

For every fixed derivative order j>=0 there are constants C_j,c_j>0 such
that

\[
|F^{(j)}(t)|\le C_j e^{-c_jt^2}\qquad(t\ge0).
\tag{H15}
\]

Thus the entire real-axis asymptotic expansion, including each differentiated
expansion, agrees with the original source.

**Proof of entire interpolation.** H9 gives `|delta_n|<=C exp(-a n^2)` with
a=log16 and, for example, C=17d_1/1024. On a compact complex set with
|Re z|,|Im z|<=R, the integral formula

\[
\operatorname{sinc}(\pi w)=\frac12\int_{-1}^1e^{i\pi s w}\,ds
\]

bounds its modulus by exp(pi R), while
`|exp(-(z-n)^2)|<=exp(R^2-(n-R)^2)` for n>=R. Thus the series converges
locally uniformly, giving an entire function. At an integer k, every term
except possibly n=k has an exact sinc zero; the remaining Gaussian and
sinc factors equal 1. The coefficients are real. Addition of an entire
function cannot remove or alter a nonzero finite principal part.

**Proof of the real-axis bound.** For j=0, use |sinc(pi u)|<=1 for real u
and complete the square:

\[
a n^2+(t-n)^2
=(a+1)\left(n-\frac{t}{a+1}\right)^2+
\frac{a}{a+1}t^2.
\]

The translated Gaussian lattice sum is uniformly bounded, so
`|F(t)|<=C' exp(-a t^2/(a+1))`. Each j-th derivative of the Gaussian-sinc
factor is bounded by `C_j'(1+|t-n|^j)exp(-(t-n)^2)`; the sinc derivatives
are bounded by pi^j using the same integral formula. Absorb the polynomial
into exp(-(t-n)^2/2) and complete the square again. This proves H15 and
also justifies differentiation on compact sets. QED.

**The necessary boundary is explicit.** F is not a polynomial or a rational
function: if it were rational, being entire it would be polynomial, and H15
would force F=0. That would give the original endpoint x=q, contradicting
the classical irrationality of pi. Thus the new meromorphic source is
strictly outside the fixed rational four-pole class. Its behavior at complex
infinity differs, and its regular Laurent coefficients need not agree.
Neither equality of the full analytic germ nor a common fixed positive
Mellin measure is claimed. Complete monotonicity beyond the proved first
discrete difference is not claimed. This matters: exact rationality/global
growth can authenticate a source more strongly than finite pole data and
real-axis asymptotics.

For example, if two meromorphic functions have the same finite principal
parts and their difference has polynomial growth on the whole complex
plane, their difference is a polynomial by Cauchy's estimate. If it also
tends to zero along the positive real axis, it is zero. This elementary
rigidity condition rejects H14. It authenticates the source; it does not
supply signed cancellation for its orbit.

## 5. A decisive missing-property witness: high-order complete monotonicity

The enlarged source does not preserve every authentic positive-moment
constraint. This is testable, rather than an unspecified caveat.

### Theorem H-04: one exact high-order alternating difference is negative

Use the concrete M=0 construction returned by `FlatLock(0)` in the probe
(the selection algorithm starts L=K=0 and increments until H3 holds; each
L_n starts at max(1,(n+1)^2) and increments until H6 holds). It has
q=3217/16384, K=4. Let k=100,000,000. Then

\[
\boxed{\sum_{j=0}^{k}(-1)^j\binom{k}{j}\widetilde r(3+j)
<-10^{-15}.}\tag{H16}
\]

This is an exact analytic-rational bound, not a sum of one hundred million
rounded terms.

**Proof.** For the authentic contribution, use 0<Q(t)<=4, t^16<=t^15 on
[0,1], and the exact beta integral:

\[
0<\sum_{j=0}^k(-1)^j\binom kjr(3+j)
=\int_0^1t^{16}Q(t)(1-t^8)^kdt
\le\frac1{2(k+1)(k+2)}.
\]

Retain delta_3 and delta_4 exactly. For j>=2 put
`a_j=binom(k,j)(17/1024)d_(3+j)16^(-(3+j)^2)`. By H9,
these majorize the absolute values of the remaining perturbation terms.
Their successive ratio obeys

\[
\frac{a_{j+1}}{a_j}
<\frac{k}{j+1}16^{-(7+2j)}
\le\frac{k}{3\cdot16^{11}}<\frac12.
\]

Therefore the entire remaining tail is at most 2a_2, and the left side of
H16 is bounded above by the exact rational

\[
\frac1{2(k+1)(k+2)}+\delta_3+k|\delta_4|
+k(k-1)\frac{17}{1024}d_5\,16^{-25}.
\tag{H17}
\]

Substituting the finite rational g values from H6 makes H17 equal to

```
-58315204340264152768911846887031704052869692500996947547993661606613894565390674029487941341457
/
47843291154128651828722862472083243692494133473544183042981480643306090750039374476648075176000013358596096000
```

This is strictly less than -1/10^15 by integer cross multiplication. Its
decimal value about -1.21887944858e-15 is only a display. QED.

If a sequence has a fixed positive Hausdorff representation
`a(n)=integral_[0,1] v^(n-1) dmu(v)`, every alternating difference equals
`integral v^(n-1)(1-v)^k dmu(v)>=0`. Thus H16 rigorously excludes that
representation for this counterfeit. Positive monotonic forcing and exact
meromorphic poles do not retain the entire positive moment cone. The
authentic source does retain it, but the separate locked source in PR #657's
Mellin/Gamma tower shows that positivity of a moment tower alone also does
not prove R0. No contradictory combination of these two different
countermodels is asserted.

## 6. Calibration and limits

`flat_lock_probe.py` uses exact Fractions and the literal four pole terms.
Its seven focused test methods cover:

- exact authentic prefixes M=0,1,3,7 and source-tail selection without pi;
- rational radix endpoint and the exact g_M seam;
- H9/H10 for tested n through 20, including the prefix seam;
- forward original-zero recurrence and telescoping identities through 22;
- exact all-F terminal suffixes and geometric terminal norms on finite
  locked shells from the M=0 construction;
- mutation controls: multiplier 15 in place of 16 fails the source error
  bound, and a coarse endpoint perturbation violates the allowed error;
- the exact H17 upper bound proving the high-order complete-monotonicity
  violation, without enumerating 100,000,001 source terms.

Executed command (scratch analysis only):

```
timeout 60s python flat_lock_probe.py
```

Initial result: **6/6 PASS**, 0.224 seconds reported by unittest. The H-04
test was then added and all **7/7 PASS** in the final focused replay. The exact log is
`evidence/flat_lock_initial.txt` (final replay: `evidence/focused_final.json`). Examples: M=0 gives q=3217/16384, K=4;
M=1 gives q=13493037705/68719476736, K=9. These finite runs check the
implementation; H-01–03 are justified by the displayed all-index proofs.
No root repository tests, Lean, hosted CI, or external referee review is
claimed by this subtask.

## 7. Source map and novelty boundary

Inspected main base:
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

Inspected newest frontier:

- PR #657, `7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf`:
  `BBP_POLE_SHIFT_CRUCIBLE.md`, `PROOF_DIRECTION_ORACLE.md`,
  `ENDPOINT_COERCIVITY_REPORT.md`, `ENDPOINT_COERCIVITY_HOLE_CONTRACT.md`.
- PR #662, `fc723029eddd7d3f32dff12218cd9c6bfa916f84`:
  `research/2026-11-16/terminal_domain_walls/THEOREMS.md`.
- PR #661, `ea7eecd38e83b2b60887cfacd5ce2a8cf854f7ea`:
  `research/2026-11-16/prime_compensation_energy/source_sections/THEOREMS.md`.
- Main CAT predecessors:
  `research/2026-10-30/carrier_adelic_transport/ALL_ORDER_SHADOW.md` and
  `SOURCE_AUTHENTICATION.md`.

The new content relative to those inspected sources is the **simultaneous**
radix lock, every-order superexponential matching, uniform positive and
decreasing bounds across every seam, and preservation of the exact four
finite clock poles by a proved entire interpolation. The all-order
counterfeit idea itself was recovered from CAT rather than claimed anew.

The authentic original-source terminal coercivity, R0, swept-origin Borwein
convergence and full normality all remain OPEN. This is a stronger combined
no-go theorem, not novelty-tax category D or E. It eliminates a proposed
relaxation of the source passport, not an asymptotic failure mode for the
actual original source.

**Smallest surviving arithmetic obligation:** use the exact global
rational-function forcing, its literal zero seed and signed integer
winding to bound the source-selected endpoint away from the low-wall
language. Preserving every finite pole and every real asymptotic coefficient
is insufficient in the enlarged meromorphic source class; proving source
identity is also insufficient by itself to establish the missing density.

## 8. Closing-frontier addendum: the discrete backward seed (H-05)

The new FQR-10 at 9ff8544c799b5e4c8eb1db33127438bc3f221045 asserts that this
counterfeit's backward seed is -q. For the explicit meromorphic extension
constructed in H-03, that assertion is false. Its interpolant is

\[
F(z)=\sum_{n>M}\delta_n e^{-(z-n)^2}\operatorname{sinc}(\pi(z-n)).
\]

For every integer k<=0, each k-n is a nonzero integer, so every sinc factor
is zero. The established locally uniform convergence gives F(k)=0. Hence

\[
\widetilde r_{\rm mer}(-m)=r(-m)\quad(m\ge0),\qquad
\sum_{m\ge0}16^m\widetilde r_{\rm mer}(-m)
=\sum_{m\ge0}16^m r(-m)=0\quad\text{in }\mathbb Q_2.
\]

The last identity uses the authentic null-seed theorem with the repaired
logarithmic sign; see audits/ADELIC_HISTORY_AUDIT.md. Thus the forward
radix-rational lock and the zero discrete backward seed coexist for this
extension. This gives no analytic continuation on Z_2 and no integrality
claim for the positive-index perturbations. The complex meromorphic clock,
its rational integer samples, and a Q_2 analytic clock are distinct objects.
A real bound on delta_n also does not determine its 2-adic valuation.

This is a paper deduction from H-03, not a newly executed numerical test.
The latest-head claim and its exact scope are retained in
audits/ADELIC_9ff8544c_DELTA_ADDENDUM.md. The stronger hypothesis of a common
authenticated 2-adic analytic clock is not disproved by this counterfeit.
