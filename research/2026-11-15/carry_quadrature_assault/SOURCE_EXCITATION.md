# Uniform source excitation and the selected carry orientation

**Date:** 2026-11-15. **Source baseline:**
`895c0ae63af7b09548c608a1b0b6f298cea0e6d1`.

**Result.** The authentic four-pole recurrence supplies a finite,
logarithmic-lag interference response whose squared magnitude has a positive
uniform lower bound. A finite reference then recovers the actual fourth-root
carry phase with a uniformly bounded denominator. Separately, the inherited
dyadic isometry supplies an exact next-bit phase flip at every finite clock
return, including returns from the zero seed. The source-specific low-bit
formula fixes the absolute clock orientation of the carry phase.

**Status.** The uniform echo estimate is a proved quantitative construction in
this note; the calibrated readout is an exact instrument reduction; the
dyadic-loop statement is a corollary of the inherited source isometry. These
statements do not establish a signed carry-density estimate. The carry gate
defined below, the original real-phase anti-locking objective, and pi
normality remain **OPEN**. No claim of academic priority is made.

## 1. Authentic source, characters, and the remaining gate

For integers $n\geq1$, let

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{N(n)}{D(n)},
\]

where

\[
N(n)=120n^2-89n+16,\qquad
D(n)=(2n-1)(4n-1)(8n-7)(8n-3).
\]

Use the original zero-seeded recurrence and its literal real carries:

\[
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
C_n=\lfloor U_n\rfloor,\qquad y_n=U_n-C_n,
\]

\[
c_n=C_n-16C_{n-1}=\lfloor16y_{n-1}+r(n)\rfloor.
\tag{1}
\]

Every $U_n,y_n,r(n)$ is a rational with odd reduced denominator. Write

\[
e(t)=\exp(2\pi i t),\qquad
[v]_{2^\ell}=a b^{-1}\pmod{2^\ell}
\quad\text{for }v=a/b,\ b\text{ odd},
\]

with the residue in $\{0,\ldots,2^\ell-1\}$, and define

\[
\chi_{2^\ell}(v)=e\!\left(\frac{[v]_{2^\ell}}{2^\ell}\right),
\qquad \ell\geq1.
\tag{2}
\]

These characters extend to $\mathbb Z_2$. In particular,

\[
\chi_4(C)=i^C\quad(C\in\mathbb Z),
\]

but $\chi_4(v)$ and $e(v/4)$ are different observations for a general
odd-denominator rational $v$. Every transport below declares which one is
used.

The selected quadrature is

\[
w(C)=\Re((1+i)i^C)
=\begin{cases}
1,&C\equiv0,3\pmod4,\\
-1,&C\equiv1,2\pmod4.
\end{cases}
\tag{3}
\]

For every integer $B\geq1$, define

\[
d_B=\frac1B\#\{n\in\mathbb Z:B\leq n<2B, C_n\bmod4\in\{1,2\}\}.
\]

The open carry gate is

\[
\boxed{\liminf_{B\to\infty}d_B>0.}
\tag{G}
\]

Equivalently, there exist $\delta>0,B_0$ such that $d_B\geq\delta$
for every integer $B\geq B_0$; equivalently,

\[
\limsup_{B\to\infty}\frac1B\sum_{n=B}^{2B-1}w(C_n)<1,
\]

because the displayed average is exactly $1-2d_B$.

## 2. Quantitative forcing and tail bounds

**SE-01 — PROVED.** For every integer $n\geq1$,

\[
r(n)>\frac{15}{64n^2}>0.
\tag{4}
\]

For every integer $n\geq2$,

\[
r(n)<\frac{15}{64(n-1)^2}.
\tag{5}
\]

**Proof.** All factors of $D(n)$ are positive for $n\geq1$. The numerator
of (4), after multiplication by $64n^2D(n)$, is

\[
64n^2N(n)-15D(n)
=9664n^3-9656n^2+3090n-315
\]

\[
=9664n^2(n-1)+8n^2+3090n-315>0.
\]

For (5), put $n=t+1$, where $t\geq1$. Direct expansion gives

\[
15D(t+1)-64t^2N(t+1)
=5696t^3+7672t^2+2910t+225>0.
\]

Division by the positive denominators proves both bounds. $\square$

Define the real tail

\[
T_n=\sum_{j\geq1}16^{-j}r(n+j),\qquad n\geq0.
\]

The classical BBP identity gives $U_n+T_n=16^n\pi/16$. Only the displayed
positive convergent tail, its recurrence, and the rational forcing are
needed for the estimates that follow.

**SE-02 — PROVED.** For every integer $n\geq1$,

\[
\frac{15}{1024(n+1)^2}<T_n<\frac1{64n^2}.
\tag{6}
\]

**Proof.** Retain the first term and apply (4) for the lower bound. For the
upper bound, (5) gives, term by term,

\[
16^{-j}r(n+j)<16^{-j}\frac{15}{64(n+j-1)^2}
\leq16^{-j}\frac{15}{64n^2}.
\]

Sum the geometric series $\sum_{j\geq1}16^{-j}=1/15$. $\square$

## 3. A uniformly visible finite source echo

For every integer $n\geq4$, choose

\[
m(n)=\lceil\log_4 n\rceil,\qquad q_n=16^{m(n)},\qquad s_n=n+m(n).
\tag{7}
\]

Equivalently, $m(n)$ is the smallest integer $m$ with $16^m\geq n^2$.
Thus $n^2\leq q_n<16n^2$. Define the finite rational echo

\[
R_n=U_{s_n}-q_nU_n
=\sum_{j=1}^{m(n)}16^{m(n)-j}r(n+j).
\tag{8}
\]

Iterating the recurrence proves the finite identity. Splitting the tail also
gives

\[
R_n=q_nT_n-T_{s_n}.
\tag{9}
\]

**SE-03 — PROVED; new uniform quantitative bound in this note.** For every
integer $n\geq4$,

\[
\boxed{\frac1{128}<R_n<\frac14.}
\tag{10}
\]

**Proof.** By (6), $q_n\geq n^2$, and $s_n\geq n$,

\[
R_n>
\frac{15n^2}{1024(n+1)^2}-\frac1{64n^2}.
\]

Both summands on the right increase with $n\geq1$. At $n=4$, their sum
is $43/5120>1/128$. For the upper bound, $T_{s_n}>0$, so

\[
R_n<q_nT_n<\frac{q_n}{64n^2}<\frac14.
\]

This proves the strict bounds at every declared index. $\square$

For $\theta\in\{1,1/4\}$, define a two-time response

\[
\Delta_{n,\theta}
=e(\theta U_{s_n})-e(\theta q_nU_n)
=e(\theta q_nU_n)\bigl(e(\theta R_n)-1\bigr).
\tag{11}
\]

**SE-04 — PROVED.** For every $n\geq4$ and either declared $\theta$,

\[
|\Delta_{n,\theta}|^2
=4\sin^2(\pi\theta R_n)
>4\sin^2\!\left(\frac{\pi\theta}{128}\right)>0.
\tag{12}
\]

Consequently, every integer $B\geq4$ satisfies the extensive response bound

\[
\boxed{
\sum_{n=B}^{2B-1}|\Delta_{n,\theta}|^2
>4B\sin^2\!\left(\frac{\pi\theta}{128}\right).
}
\tag{13}
\]

**Proof.** Equation (11) removes a unit-modulus factor. On the interval

\[
0<\frac{\pi\theta}{128}<\pi\theta R_n<\frac{\pi\theta}{4}\leq\frac\pi4,
\]

sine is strictly increasing. Apply (10) and sum. $\square$

The lag is $O(\log n)$, and the amplified harmonic is $q_n\asymp n^2$.
The inherited $n^{-2}$ forcing scale therefore has a finite, uniformly
visible response after this amplification. This is a bound on the sum of
squared individual responses; it is not a lower bound on the squared
magnitude of their signed sum.

### Why the amplification scale is quadratic

For any integer lag \(m\ge1\), at any \(n\ge1\), put \(q=16^m\) and
\(R_{n,m}=\sum_{j=1}^m16^{m-j}r(n+j)\). The same forcing bounds give

\[
\boxed{\frac{q-1}{64(n+m)^2}<R_{n,m}<\frac{q-1}{64n^2}.}
\]

For the lower bound use \(r(n+j)>15/[64(n+m)^2]\) throughout
the finite sum; for the upper bound use \(r(n+j)<15/(64n^2)\).
The geometric coefficient sum is \((q-1)/15\). In particular, if
\(q/n^2\to0\), the unwrapped echo and its phase response tend to zero.
If \(m=o(n)\), the two envelopes also show
\(R_{n,m}\sim(q-1)/(64n^2)\). Thus quadratic amplification is the
threshold scale for a response of fixed size in this instrument. The
specific choice in (7) additionally keeps the response in a phase interval
that avoids an integer turn. This makes explicit the inherited source-scale
mechanism; it adds no signed-density theorem.

## 4. A finite reference recovers the actual carry orientation

Define the source reference

\[
J_{n,\theta}=1-e(-\theta R_n).
\tag{14}
\]

It depends on the finite sum (8). It requires no infinite-tail evaluation.
The same bound gives

\[
|J_{n,1}|>2\sin(\pi/128),\qquad
|J_{n,1/4}|>2\sin(\pi/512).
\tag{15}
\]

**SE-05 — PROVED; exact instrument reduction.** For every integer $n\geq4$
and $\theta\in\{1,1/4\}$,

\[
\boxed{
\frac{\Delta_{n,\theta}\overline{J_{n,\theta}}}
{|J_{n,\theta}|^2}
=e(\theta U_{s_n}).
}
\tag{16}
\]

In particular,

\[
\boxed{
\frac{\Delta_{n,1/4}\overline{J_{n,1/4}}}
{|J_{n,1/4}|^2}\ e(-y_{s_n}/4)=i^{C_{s_n}}.
}
\tag{17}
\]

**Proof.** Equation (8) implies

\[
\Delta_{n,\theta}
=e(\theta U_{s_n})\bigl(1-e(-\theta R_n)\bigr)
=e(\theta U_{s_n})J_{n,\theta}.
\]

Divide using the strictly positive bounds (15). At $\theta=1/4$, multiply
by $e(-y_{s_n}/4)$ and use $U_{s_n}-y_{s_n}=C_{s_n}\in\mathbb Z$.
$\square$

For fixed exact $J_{n,\theta}$, a perturbation of $\Delta_{n,\theta}$
of size at most $\varepsilon$ changes the readout by at most

\[
\frac{\varepsilon}{2\sin(\pi\theta/128)}.
\]

Thus the reference division has a condition bound independent of $n$.
This does not grant cheap access to the original phase or the real fractional
correction: both remain part of the declared observation. In particular,
(17) is an exact carry-sensitive response, not a computation of its mean.
No uniform distance of the original states from an integer carry boundary
is proved here. The bounded reference gain therefore does not supply a
uniform noise tolerance for deciding the floor branch itself; (17) uses the
correct fractional representative as an input.

### Sampling the delayed indices preserves the gate

**SE-06 — PROVED.** For every function $f:\mathbb Z_{\geq0}\to\mathbb C$
with $|f(n)|\leq1$, and every integer $B\geq4$,

\[
\left|
\frac1B\sum_{n=B}^{2B-1}f(s_n)
-\frac1B\sum_{n=B}^{2B-1}f(n)
\right|
\leq\frac{2m(2B)}B.
\tag{18}
\]

**Proof.** Since $m(n)$ is nondecreasing, $s_n=n+m(n)$ is strictly
increasing. The sampled set has exactly $B$ distinct points, all in

\[
[B,\,2B+m(2B))\cap\mathbb Z.
\]

At most $m(2B)$ lie outside $[B,2B)$. Its symmetric difference with
$[B,2B)\cap\mathbb Z$ therefore has at most $2m(2B)$ elements.
Cancel the common terms and use $|f|\leq1$. $\square$

The right side tends to zero. Apply (18) either to $w(C_n)$ or to the
indicator in (G). Consequently the gate for the delayed carry phase recovered
by (17) is exactly equivalent to the original gate, with the same limiting
upper or lower averages.

## 5. Exact next-bit excitation on dyadic clock returns

**Inherited source theorem, with its origin scope retained.** The report
[PI_DYADIC_SOURCE_ISOMETRY.md](../../2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md),
DSI-2--DSI-4, proves that

\[
F(t)=\sum_{j\geq0}16^j r(t-j),\qquad t\in\mathbb Z_2,
\]

is a bijective isometry, that its analytic source-selected value is

\[
F(0)=0,
\]

and that $F(n)=U_n$ for **every integer $n\geq0$**. The latter follows
from the same recurrence and the authenticated initial value. Thus the
inherited assertion is

\[
v_2(U_a-U_b)=v_2(a-b)
\qquad(a,b\geq0, a\ne b),
\tag{19}
\]

including comparisons with index zero. The zero identity is an inherited
analytic theorem, not inferred here from finitely many congruences.

**SE-07 — PROVED; inherited-isometry corollary.** For all integers $n,k\geq0$,
put $t=n+2^k$. Then

\[
U_t\equiv U_n\pmod{2^k},\qquad
U_t-U_n\equiv2^k\pmod{2^{k+1}},
\tag{20}
\]

and therefore

\[
\boxed{
\frac{\chi_{2^{k+1}}(U_t)}{\chi_{2^{k+1}}(U_n)}=-1,
\qquad
|\chi_{2^{k+1}}(U_t)-\chi_{2^{k+1}}(U_n)|^2=4.
}
\tag{21}
\]

**Proof.** Equation (19) gives valuation exactly $k$. Modulo $2^{k+1}$,
every element of valuation $k$ has residue $2^k$. Apply the character.
$\square$

For $k\geq1$, this is a closed return in the observer retaining $k$ bits,
with an exact phase reversal in the next-bit character. The $k=0$ case
has a trivial coarse quotient and a parity reversal. The response value
$4$ in (21) is exactly quantized for this specified mathematical observable.

### Carry transport retains the fractional cofactor

At the same pair of indices, $U_t-U_n=(C_t-C_n)+(y_t-y_n)$. Hence

\[
\boxed{
\chi_{2^{k+1}}(C_t-C_n)
=-\chi_{2^{k+1}}(-(y_t-y_n)).
}
\tag{22}
\]

This is the exact transport from raw source holonomy to carry holonomy.
The fractional cofactor is the term that can absorb or preserve the sign.
For $k=1$, the raw fourth-root source character reverses after two steps;
the carry fourth-root character also includes the displayed cofactor.

## 6. The actual four poles fix the absolute fourth-root clock

**SE-08 — PROVED; source-selected low-bit identity.** For every integer $n\geq0$,

\[
[U_n]_{16}=\bigl(2(n\bmod2)-n\bigr)\bmod16,
\qquad
\boxed{[U_n]_4=n\bmod4.}
\tag{23}
\]

**Proof.** For $n\geq1$, the recurrence gives $[U_n]_{16}=[r(n)]_{16}$.
Modulo 16, the numerator and odd denominator of $r(n)$ are

\[
N(n)\equiv8n^2+7n,\qquad D(n)\equiv8n^2+2n+5.
\]

If $n=2t$, subtracting $(-2t)D(2t)$ from $N(2t)$ leaves
$8t(t+3)\pmod{16}$. If $n=2t+1$, subtracting
$(1-2t)D(2t+1)$ from $N(2t+1)$ leaves
$8t(t+5)\pmod{16}$. Both products are divisible by 16 since the paired
factors have opposite parity. Invert the odd denominator to prove the first
identity. Reducing it modulo 4 gives $n\bmod4$. At $n=0$, both identities
hold directly from $U_0=0$. $\square$

This agrees with the inherited implementation
[first_spatial_digit](../../../observational_succ/bbp_spatial_haar_lift.py).
Its formula was checked independently here against the exact rational
recurrence, rather than used as an assumption in the proof.

Define the fractional cofactor $z_n=\chi_4(-y_n)$. Equation (23) gives

\[
\boxed{
i^{C_n}=\chi_4(U_n)\chi_4(-y_n)=i^n z_n,
\qquad
w(C_n)=\Re\bigl((1+i)i^n z_n\bigr).
}
\tag{24}
\]

Thus the exact remaining object is a signed correlation between the known
four-periodic source clock and the actual fractional cofactor. The orientation
$i^n$ comes from the four-pole formula and the zero-seeded source, beyond a
bare assertion that some dyadic isometry exists.

The one-step cofactor law can be checked without any distribution assumption.
For $z_{n,\ell}=\chi_{2^\ell}(-y_n)$, (1) gives

\[
z_{n,\ell}=z_{n-1,\ell}^{16}\,
\chi_{2^\ell}(-r(n))\,e(c_n/2^\ell),\qquad n\geq1.
\tag{25}
\]

At modulus 4 this simplifies to

\[
z_n=\chi_4(-r(n)+c_n)=i^{c_n-n}.
\tag{26}
\]

The old cofactor disappears because its sixteenth power is 1; the unknown
literal carry $c_n=\lfloor16y_{n-1}+r(n)\rfloor$ remains. Substituting (26)
into (24) returns $i^{C_n}=i^{c_n}$, since $C_n=16C_{n-1}+c_n$.
This particular recurrence therefore re-encodes the carry. It does not yet
provide an independent restriction on its signed distribution.

## 7. Seed scope, control, and the remaining signed estimate

For a real seed $a$, let $U_0(a)=a$ and use the same forcing. Then

\[
U_n(a)=U_n(0)+16^n a.
\]

The finite echo cancels this term exactly:

\[
U_{s_n}(a)-q_nU_n(a)=R_n.
\tag{27}
\]

Thus (10), the pulse magnitudes, and the reference bounds hold for every
real seed. The oriented readout (16) still returns the phase of the chosen
seed; it has not discarded that orientation.

**Exact control.** Take $a_*=-\pi/16$. The classical completion identity
gives

\[
U_n(a_*)=-T_n.
\]

For $n\geq1$, (6) implies $-1<U_n(a_*)<0$, hence

\[
C_n(a_*)=-1,\qquad w(C_n(a_*))=1.
\tag{28}
\]

This trajectory has the same uniformly positive echo energies and no hits
in the gate. Its seed is a different real irrational value; it is **not**
claimed to retain the authentic rational diagonal source, the interpolation
$F(n)=U_n(0)$, or the zero-seed dyadic passport. It is an exact control
against inferring the selected signed estimate from the seed-blind energy
alone, not a counterexample to (G) for the authentic source.

The surviving positive construction is concrete: a finite source echo has
extensive uniformly nonzero squared response; a bounded reference recovers
the actual carry phase; every coarse dyadic return excites the next
character exactly; and the four poles fix the clock orientation in (24).
The next proof must bound the mean of that source-selected signed response,
for example by proving that some $\eta>0,B_0$ satisfy

\[
\boxed{
\Re\!\left[
\frac{1+i}{B}\sum_{n=B}^{2B-1}i^n\chi_4(-y_n)
\right]\leq1-\eta
\quad\text{for every integer }B\geq B_0.
}
\tag{29}
\]

Equation (29) is precisely the open gate with $\delta=\eta/2$, not a newly
proved saving. Any proposed use of the excitation should state the additional
source-selected inequality that forces this signed response away from 1.

## 8. Provenance and finite validation scope

- The four-pole source and completion are the classical
  [Bailey--Borwein--Plouffe formula](https://www.davidhbailey.com/dhbpapers/digits.pdf),
  retained in the repository's original `duck_bbp.forcing` source.
- Echo seed cancellation and polynomial filters annihilating the homogeneous
  factor 16 are inherited from
  [BBP_ECHO_DELAY_TRANSPORT.md](../../2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md)
  and [pi_carrier_collision/THEOREMS.md](../pi_carrier_collision/THEOREMS.md),
  PC-01. The forcing's $n^{-2}$ scale and resulting quadratic amplification
  scale are also inherited; SE-03 supplies the particular uniform interval
  and SE-04--SE-06 its conditioned readout and sampling consequences.
- The all-index dyadic interpolation, including $n=0$, is inherited from
  [PI_DYADIC_SOURCE_ISOMETRY.md](../../2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md),
  DSI-2--DSI-4. SE-07 is its explicit loop-character corollary.
- The low spatial nibble formula is already implemented in
  [bbp_spatial_haar_lift.py](../../../observational_succ/bbp_spatial_haar_lift.py).
  SE-08 supplies a direct modular verification and makes the exact selected
  clock--cofactor target explicit.

Exact rational checks in this worktree compared the source recurrence,
`first_spatial_digit`, and `particular_mod` for $0\leq n\leq256$, checked
the modulus-4 source and carry-cofactor identities on the same indices, and
checked the loop residue at $0\leq n\leq16, 0\leq k\leq8$, including
returns from index zero. These comprised 924 exact assertions and passed.
Separate checks verified both polynomial identities in SE-01, the echo
interval at 257 indices (every $4\leq n\leq256$ and $n=512,1024,4096,65536$),
and the sampling-set bound for every $4\leq B\leq256$. All passed. The six
local document links were also checked. These finite controls check
implementation and origin conventions; the
universal claims above rest on the displayed proofs and the expressly
inherited isometry theorem. They provide no finite-to-infinite certificate
for the open gate.

**Next falsification opportunity.** A candidate signed inequality should be
tested against its own declared source and seed scope, then proved with the
fractional cofactor retained. The real counterseed (28) detects accidental
loss of seed orientation; replacing $\chi_4(-y_n)$ by 1 detects accidental
loss of the carry transport. Passing those controls would still require an
all-shell proof of (29).
