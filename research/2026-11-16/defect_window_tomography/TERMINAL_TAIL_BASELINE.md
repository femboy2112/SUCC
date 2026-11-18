# The terminal norm's coherent tail baseline and the threshold for arithmetic gain

Independent constructor bearing for SUCC PR #657, 2026-11-16.
Repository baseline: `1f04b869182ad68deb764637034d72b19352ca48`.
The parent audit checked the stated metric and conditional arithmetic proofs.
The lower-bound premise for the original zero seed remains OPEN.

## Objects and provenance

Keep the literal original forcing

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\]

and its authentic tail `T_m=sum_{j>=1}16^{-j}r(m+j)`.
For a completed endpoint beta, put `s=beta-pi/16`, so
`U_m(s)=16^m beta-T_m`. Only `s=0` is the canonical source.
Define

\[
R_B(s)=\frac1B\sum_{k=1}^B\|U_{2B}(s)/16^k\|_{\mathbb T}^2,
\quad E_B(\beta)=\frac1B\sum_{k=1}^B\|16^{2B-k}\beta\|_{\mathbb T}^2,
\]

\[
h_B^2=\frac{T_{2B}^2(1-16^{-2B})}{255B}.
\]

The old VFM source-shadow comparison controls phase differences. The following
is its torus-residual, two-sided calibration; it does not assert new arithmetic
cancellation. Existing RI-02 already gives the balanced-carry/R0 equivalence,
so that equivalence should not be republished as a new result of this round.

## CTB-01: exact two-sided norm calibration

For every real beta and every integer B>=1,

\[
\boxed{|\sqrt{R_B(s)}-\sqrt{E_B(\beta)}|\le h_B.}
\]

Consequently

\[
\boxed{E_B(\beta)\ge[\sqrt{R_B(s)}-h_B]_+^2,\qquad
E_B(\beta)\le(\sqrt{R_B(s)}+h_B)^2.}
\]

**Proof.** The distance-to-integers function is 1-Lipschitz, hence each pair
of corresponding nonnegative residuals differs by at most `T_{2B}/16^k`.
Apply the reverse triangle inequality in the normalized finite Euclidean norm,
then use `sum_{k=1}^B 16^{-2k}=(1-16^{-2B})/255`.
This proof tolerates every wrapping and nearest-integer tie.

An exact-rational upper instrument is obtained by replacing `T_{2B}` by
`beta_{2B}=r(2B+1)/15`. Both `R_B(0)` and this bound are rational, although
the displayed square-root comparison need not itself be rational.

## CTB-02: the coherent raw norm is quintic, not zero

For the coherent same-forcing control `s=-pi/16`, the completed endpoint is
beta=0, but the raw terminal state in this control is `U_m(s)=-T_m`.
Since `0<T_m<1/(64m^2)<1/2` for m>=1, no wrap occurs and

\[
\boxed{R_B(-\pi/16)=h_B^2.}
\]

The control states are generally irrational, and its seed is not zero. It is
a control of an inference from forcing/tail machinery; it is not a rival
authentic rational prefix.

The original forcing has

\[
r(n)=\frac{15}{64n^2}+O(n^{-3}),\qquad
T_m=\frac1{64m^2}+O(m^{-3}).
\]

For the second identity, insert the first into the tail and use
`(m+j)^{-2}=m^{-2}+O(j m^{-3})`, uniformly for m,j>=1, together with
the convergent sums of `16^{-j}` and `j16^{-j}`. Therefore

\[
\boxed{R_B(-\pi/16)\sim L B^{-5},\qquad
L=\frac1{255\cdot256^2}=\frac1{16711680}.}
\]

Thus the assertion that *any* polynomial raw-norm floor is meaningful
anti-locking is refuted by an exact infinite coherent control. An energy
of this scale can come entirely from the still-uncompleted source tail.

## CTB-03: which weaker lower bound would buy a restricted exponent

Let

\[
v_{16}(\beta)=\limsup_{m\to\infty}
\frac{-\log\|16^m\beta\|_{\mathbb T}}{m\log16},
\]

with value infinity when the distance vanishes infinitely often.
Each of the following hypotheses is sufficient to prove `v16(beta)<=1`:

1. There are c>0, alpha<5 and B0 such that `R_B(s)>=c B^{-alpha}`
   for every B>=B0.
2. `liminf_{B->infinity} B^5 R_B(s)>L`.
3. The pointwise inequality `R_B(s)>=L B^{-5}` holds for every sufficiently
   large B. This is sharper than item 2 and must not be weakened to
   `liminf B^5 R_B(s)>=L`.

**Proof of the norm step.** In case 1, `h_B^2/R_B(s)->0`, so CTB-01
gives `E_B(beta)>=c B^{-alpha}/4` eventually. In case 2 choose
`L<c<liminf B^5 R_B(s)` and use `B^(5/2)h_B->sqrt(L)`; CTB-01 gives
`E_B(beta)>=c' B^{-5}` eventually for some c'>0.

For item 3, use the inherited exact source bound
`T_{2B}<1/((16B+1)(16B+2))`. With `D_B=(16B+1)(16B+2)`,

\[
\sqrt{R_B(s)}-h_B>
\frac1{\sqrt{255B}}\left(\frac1{256B^2}-\frac1{D_B}\right).
\]

Since `D_B<=306B^2` and `D_B-256B^2=48B+2>=48B` for B>=1,

\[
\boxed{E_B(\beta)>\frac1{255\cdot1632^2\,B^7}
=\frac1{679173120\,B^7}}
\]

at every B where item 3's hypothesis holds. No rounding of the critical
constant is used.

**Proof of the exponent step.** If `v16(beta)>1`, choose epsilon>0 and
infinitely many m with `||16^m beta||<16^{-(1+epsilon)m}`. For
`n=m,...,2m-1`, multiplication of a nearest integer to `16^m beta`
gives

\[
\|16^n\beta\|\le16^{n-m}\|16^m\beta\|.
\]

Hence

\[
E_m(\beta)\le
\frac{16^{2m}-1}{255m}\|16^m\beta\|^2
<\frac{16^{-2\epsilon m}}{255m},
\]

which contradicts any eventual positive polynomial lower bound for E.

**Boundary.** None of the hypotheses is proved for beta=pi/16. A bound at the
quintic rate with constant below L holds for the coherent control, yet
`v16(0)=infinity`. The same is true of any weaker rate `B^{-alpha}` with
alpha>5. Moreover the coherent control has `liminf B^5R_B=L`, so a
liminf inequality with equality permitted is false as a proposed sufficient
condition. The inherited subleading rational tail bound is what makes the
pointwise inequality in item 3 valid. This is a
calibration threshold for this family of raw-norm lower-bound routes, not a proof that every
above-baseline sequence satisfies R0. Positive polynomial E still tends
to zero; R0 requires a positive constant lower bound.

### A strict-separation control: the critical intermediate is weaker than R0

Let `beta_sq=sum_{j>=1}16^{-j^2}`. Its hexadecimal digits are 0 or 1,
with unbounded gaps between the ones, so it is irrational. For every n,
`0< {16^n beta_sq} <=1/15<1/2`. If B>=9, some square lies in
`[B+1,2B]`; immediately before its marker the circle distance is at
least 1/16. Thus `E_B(beta_sq)>=1/(256B)`.

For the upper bound, let M_B count square positions in `[B+1,2B]`.
Summing the contribution of each marker backwards gives

\[
\sum_{n=B}^{2B-1}\{16^n\beta_{\rm sq}\}
\le M_B/15+1/225.
\]

The second term bounds all markers beyond 2B by allowing a marker at
every remaining position. Because each fractional part is at most 1/15,

\[
E_B(\beta_{\rm sq})\le M_B/(225B)+1/(3375B)=O(B^{-1/2}).
\]

Therefore this endpoint fails R0. On the other hand CTB-01 and
`h_B<1/(32 sqrt(B))` give `R_B(beta_sq-pi/16)>=1/(1024B)` for B>=9.
In particular the critical quintic inequality holds on every such shell.
This is a same-forcing, changed-seed control. It proves the intermediate
condition is strictly weaker than R0; it is not evidence that canonical
pi satisfies the condition.

## Source attempt and exact obstruction

The original `U_n` have odd reduced denominators. Their known 2-adic clock,
the presence of fresh denominator primes, and the positivity of the tail
do not by themselves give a floor above CTB-02: existing RI-03 and GP-5
controls already retain relevant subsets of those properties while
locking the real phase. The original BBP partial-sum argument also fails
the RDT-04 denominator/error threshold. No new numerator-versus-sparse-word
exclusion has been derived in this bearing.

The worthwhile open intermediate statement is therefore an **excess over
the actual coherent tail baseline**, with the zero-selected numerator
retained. It must be established arithmetically; CTB-01 transports such
an excess but does not create it.

## Claim state and novelty tax

- CTB-01: elementary proved comparison, inherited source ingredients.
- CTB-02: exact source-attached calibration and infinite hostile control.
- CTB-03: proved conditional restricted-exponent consequence, with sharp
  scale distinction; its premise for canonical pi remains OPEN.
- No new all-shell lower bound for original pi, no new irrationality
  exponent, and no R0/normality claim.

This is a useful calibration theorem, not a genuine statistical proof step.
It prevents a weaker polynomial raw-energy result from being mistaken for
progress when it is fully explained by uncompleted tail energy.
