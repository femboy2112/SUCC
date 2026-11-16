# Carry-quadrature controls and source passports

**Status:** proved reductions and counterexamples within their stated domains.
The original four-pole, zero-seeded density claim remains open. None of the
controls below satisfies all of its premises. Their purpose is to identify
which premises a proposed proof actually uses.

## 1. The authentic target and its one-way implication

Keep the source and its seed explicit:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\]

\[
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
U_n+T_n=16^n\pi/16.
\]

Write \(C_n=\lfloor U_n\rfloor\), \(y_n=\{U_n\}\), and
\(c_n=C_n-16C_{n-1}\). The exact carry equation is

\[
c_n=16y_{n-1}+r(n)-y_n,\qquad C_n\equiv c_n\pmod4.
\]

For \(w(a)=\Re((1+i)i^a)\), its values on residues \(0,1,2,3\) are
\((1,-1,-1,1)\). Thus

\[
A_n:=1_{\{C_n\bmod4\in\{1,2\}\}}=\frac{1-w(C_n)}2.
\]

Once \(0<r(n)<1\), a hit forces
\(c_n\in\{1,2,5,6,9,10,13,14\}\), and therefore

\[
\frac{1-r(n)}{16}\le y_{n-1}<\frac{15}{16}.
\]

Consequently, if

\[
\delta=\liminf_{B\to\infty}\frac1B\sum_{n=B}^{2B-1}A_n>0,
\]

then the completed real orbit satisfies

\[
\liminf_{B\to\infty}\frac1B\sum_{n=B}^{2B-1}
\bigl[1-\cos(2\pi16^n\pi/16)\bigr]
\ge\delta\,[1-\cos(\pi/8)]>0.
\]

The fixed time shift changes only two bounded summands; \(T_n\to0\)
transfers the phase. This is a sufficient condition for the anchored
anti-locking target. It is not a necessary condition: the fixed-point
control in section 2 has positive angular response and no hits.

### True hexadecimal digit versus raw carry

Let \(\alpha=\pi/16\), \(K_n=\lfloor16^n\alpha\rfloor\),
\(d_n=K_n-16K_{n-1}\), and \(s_n=\{16^n\alpha\}\). Once
\(T_n<1\), define the tail borrow \(\beta_n=1_{\{s_n<T_n\}}\).
Then exactly

\[
C_n=K_n-\beta_n,\qquad
C_n\bmod4=(d_n-\beta_n)\bmod4.
\]

Equality \(s_n=T_n\) causes no borrow, as the strict inequality specifies.
In particular, every true digit in \(\{2,6,10,14\}\) forces a hit,
irrespective of the borrow; a true digit congruent to zero modulo four
never forces one. Digits congruent to one or three depend on the borrow.
Positive lower shell density of digits \(\{2,6,10,14\}\) would suffice,
but is another unproved source-selected density assertion.

## 2. A closed loop can carry a quantum without a useful rate

For the unforced circle map \(x\mapsto\{16x\}\), let

\[
x_L=\frac1{16^L-1},\qquad L\ge1.
\]

Its repeating digit word is \(0^{L-1}1\). After \(L\) steps it closes,
with integer winding \((16^L-1)x_L=1\), and the sum of its ordinary
one-step digits is one. Exactly one two-bit hit occurs per period.
Thus nonzero quantized charge per closed loop allows the hit rate
\(1/L\), with no lower bound independent of return time.

There is a second obstruction: the charge can lie in the wrong residue.
The fixed point \(x=1/5\) satisfies

\[
16x=3+x.
\]

Its carry is always three, so its two-bit hit rate is zero and
\(w(3)=1\), while its angular response is the positive constant
\(1-\cos(2\pi/5)\). A nonzero loop quantum need not excite the selected
quadrature at all.

The latter example can preserve the **exact original real forcing** by
choosing a different real seed:

\[
V_n=16^n/5-T_n,\qquad V_0=1/5-\pi/16.
\]

Since \(T_n\le4/[15(8n+1)]<1/5\) for \(n\ge1\),

\[
\lfloor V_n\rfloor=(16^n-1)/5\equiv3\pmod4\quad(n\ge1).
\]

This is an exact-forcing control, not an authentic zero-seed trajectory.
Its forward states are generally irrational real numbers, so the original
rational diagonal embedding into the real and 2-adic carriers is not
preserved. The source-only backward 2-adic zero identity remains true
because the source is unchanged; the new real trajectory is not that
zero-pinned 2-adic solution.

## 3. Exact forcing, exponent-two endpoint, and no late hits

Use the base-16 Kempner endpoint

\[
\xi=\sum_{j\ge0}16^{-2^j},\qquad
V_n=16^n\xi-T_n.
\]

The real recurrence remains exactly
\(V_n=16V_{n-1}+r(n)\), but the seed is now
\(V_0=\xi-\pi/16\). The number \(\xi\) is transcendental and has
irrationality exponent two: see Hone and Varona,
[*Continued fractions and irrationality exponents for modified Engel and
Pierce series*, section 4, equation (4.2)](https://kar.kent.ac.uk/70203/11/Hone-Varona2018_Article_ContinuedFractionsAndIrrationa.pdf).
That cited theorem is not needed for the following exact carry calculation;
it shows the calculation survives ordinary finite-type restrictions.

The true digit \(d_n\) is one exactly when \(n\) is a power of two,
and otherwise zero. At every non-power of two, the borrowed carry has
residue zero or three, so there is no hit. At a power-of-two index
\(n=2^j\ge4\), the completed fractional tail satisfies

\[
s_n=\sum_{k>j}16^{n-2^k}
\le\sum_{\ell\ge1}16^{-\ell n}
<2\,16^{-n}.
\]

The authentic source has the elementary lower bound

\[
r(k)>\frac{47}{512k^2}\qquad(k\ge1).
\]

Indeed, its numerator minus \(47k^2\) is
\((k-1)(73k-16)\ge0\), and its positive denominator is less than
\(512k^4\). Consequently,

\[
T_n>\frac{47}{8192(n+1)^2}>2\,16^{-n}\qquad(n\ge4).
\]

The last inequality holds at \(n=4\), and
\(16^{-n}(n+1)^2\) decreases thereafter. Thus the borrow is one at
every power-of-two digit index \(n\ge4\), removing the visible one
from the raw carry. We have proved

\[
\boxed{\quad\lfloor V_n\rfloor\bmod4\in\{0,3\},\quad
w(\lfloor V_n\rfloor)=1\quad\text{for every }n\ge3.\quad}
\]

The effective threshold is three, not an unspecified asymptotic onset.
This control preserves the exact four-pole forcing and a strong ordinary
irrationality restriction. It changes the seed and therefore does not
equal the globally zero-pinned diagonal trajectory. No claim that
\(\xi-\pi/16\) is irrational is needed or made: the difference of two
specified transcendental numbers need not be known to be irrational.
It is not a counterexample to the original source plus zero-seed assertion.

## 4. The older rational counterfeit fails the global zero passport

The earlier [PC9 control](../../2026-10-27/POINTED_CIRCLE_SOLENOID_TWO_ADIC_CLOCK.md)
uses

\[
\tau_n=\frac{n+1}{(2n+1)(4n+1)(8n+1)},\qquad
r_n^*=16\tau_{n-1}-\tau_n,\qquad
U_n^*=16^n-\tau_n.
\]

Here \(\tau_0=1\), so \(U_0^*=0\). The source is positive, has odd
denominators, and \(n^2r_n^*\to15/64\), matching the authentic leading
decay. For every \(n\ge1\),

\[
\lfloor U_n^*\rfloor=16^n-1\equiv3\pmod4.
\]

Its finite-quotient Haar property after the appropriate initial transient
does not establish the global zero pin. In the 2-adic carrier the backward
source sum telescopes to

\[
F^*(t)=\sum_{j\ge0}16^j r^*(t-j)=-\tau(t),\qquad F^*(0)=-1.
\]

Thus the forward zero-seeded orbit and the analytic backward source
solution disagree at zero. PC9 cannot refute a theorem that uses the
authentic global identity \(F(0)=0\). It also changes the forcing.

## 5. A stronger analytic control preserves the global zero pin

**Proved control theorem.** There are positive rational odd-denominator
sources \(\widetilde r(n)\) whose source-selected trajectory has all of
the following properties:

- \(\widetilde U_0=0\), and every forward value is rational with odd
  denominator;
- \(\widetilde U_n=F(n)\) for a 2-adic analytic isometry
  \(F:\mathbb Z_2\to\mathbb Z_2\), with \(F(0)=0\);
- \(\widetilde r(t)=F(t)-16F(t-1)\) is itself a 2-adic analytic
  isometry;
- the backward source sum equals \(F\), including its exact zero pin;
- \(n^2\widetilde r(n)\to15/64\) in the real place;
- the completed real endpoint is either \(a=1\) or \(a=1/5\), as chosen;
- the two-bit hit count is zero for every \(n\ge1\).

These are **not the original four-pole source**. The forward source values
are rational, but the source is not asserted to be a finite rational
function of the index. This distinction is essential.

### Construction by simultaneous real approximation and 2-adic divisibility

Define

\[
\mathbb Z_{(2)}=\{p/q:p\in\mathbb Z,\ q\text{ odd}\}\subset\mathbb Q.
\]

For every integer \(m\ge0\), the set \(2^m\mathbb Z_{(2)}\) is dense
in the real line: choose an arbitrarily large positive odd denominator
\(q\), then round on the real grid \(2^m\mathbb Z/q\). The translated
set \(1+4\mathbb Z_{(2)}\) is also dense.

Fix \(a\in\{1,1/5\}\). For \(n\ge1\), set

\[
f_n=16^n a-\tau_n,\qquad
\delta_n=\frac{\tau_n}{100(n+1)}.
\]

Choose rational Mahler coefficients successively. Put \(b_0=0\), choose
\(b_1\in1+4\mathbb Z_{(2)}\) with
\(|b_1-f_1|<\delta_1\), and for \(n\ge2\) choose
\(b_n\in2^{2n}\mathbb Z_{(2)}\) so that

\[
\left|\sum_{k=0}^{n}b_k\binom nk-f_n\right|<\delta_n.
\]

The previously chosen summands are fixed rational numbers, so real
density proves each choice exists. This is a constructive rounding
procedure, not an appeal to random coefficients. Define

\[
F(t)=\sum_{k\ge0}b_k\binom tk\qquad(t\in\mathbb Z_2).
\]

At a nonnegative integer \(n\), the sum truncates exactly at \(k=n\).
Hence \(F(n)\in\mathbb Z_{(2)}\), \(F(0)=0\), and

\[
F(n)=16^n a-\tau_n+\varepsilon_n,\qquad
|\varepsilon_n|<\delta_n\quad(n\ge1).
\]

The formula involving \(\tau_n\) and \(\varepsilon_n\) is deliberately
restricted to \(n\ge1\). For \(a=1/5\), it is not a formula for
\(F(0)\): the exact initial value is zero by construction.

### Analyticity and the exact isometry

The polynomials \(\binom tk\) take \(\mathbb Z_2\) into
\(\mathbb Z_2\), and \(v_2(b_k)\ge2k\) for \(k\ge2\), so the
series converges uniformly. More strongly, every coefficient of
\(b_k t(t-1)\cdots(t-k+1)/k!\) has valuation at least

\[
2k-v_2(k!)\ge k+1\longrightarrow\infty.
\]

The power-series coefficients therefore tend to zero 2-adically, giving
an analytic function on the unit disc.

For \(s,t\in\mathbb Z_2\), the difference of the integer-coefficient
numerator polynomials is divisible by \(t-s\). Thus, for \(k\ge2\),

\[
v_2\left(b_k\left[\binom tk-\binom sk\right]\right)
\ge v_2(t-s)+2k-v_2(k!)
\ge v_2(t-s)+3.
\]

All terms beyond \(b_1t\) are strictly more contractive than the unit
linear term. Consequently

\[
v_2(F(t)-F(s))=v_2(t-s).
\]

In particular \(F\) induces a permutation of each finite quotient
\(\mathbb Z/2^k\mathbb Z\), hence preserves its uniform measure.
The source difference is also an isometry: in

\[
\widetilde r(t)-\widetilde r(s)
=[F(t)-F(s)]-16[F(t-1)-F(s-1)],
\]

the second bracket has valuation exactly four higher than the first.
The backward identity has no missing seed term:

\[
\sum_{j=0}^{J}16^j\widetilde r(t-j)
=F(t)-16^{J+1}F(t-J-1)\longrightarrow F(t)
\quad\text{in }\mathbb Q_2.
\]

Thus its value at zero is exactly zero.

### Real positivity, correct leading decay, and locked carry

The positive sequence \(\tau_n\) decreases. For \(n\ge2\),

\[
\widetilde r(n)=16\tau_{n-1}-\tau_n
+\varepsilon_n-16\varepsilon_{n-1}>0,
\]

because \(\delta_j\le\tau_j/100\) makes its lower bound at least
\(15.84\tau_{n-1}-1.01\tau_n>0\). At \(n=1\) the correct expression
is \(\widetilde r(1)=F(1)>0\), since the initial value is zero.
Also \(\varepsilon_n=O(n^{-3})\), giving
\(n^2\widetilde r(n)\to15/64\).

The completed real endpoint is

\[
\lim_{n\to\infty}16^{-n}F(n)=a,
\]

and its positive tail is \(\widetilde T_n=\tau_n-\varepsilon_n\)
for \(n\ge1\). For \(a=1\), this tail is between zero and one, so

\[
\lfloor F(n)\rfloor=16^n-1\equiv3\pmod4.
\]

For \(a=1/5\), the tail is less than \(1/5\), while the fractional
part of \(16^n/5\) is \(1/5\). Therefore

\[
\lfloor F(n)\rfloor=(16^n-1)/5\equiv3\pmod4.
\]

The first endpoint has zero completed angular response; the second has
the fixed positive response \(1-\cos(2\pi/5)\). Both have exact zero
seed, rational diagonal forward states, global analytic zero passport,
and no two-bit hits.

The escape from this counterfamily is the **literal finite four-pole
formula**, including its specified coefficients and odd-denominator
heights. The construction above uses freely chosen rational denominators;
it cannot be substituted for that source in a proof.

### Any fixed number of authentic source bits can also be retained

**Proved strengthening, conditional only on the inherited analytic source
theorem.** For every integer \(L\ge0\) and each
\(a\in\{1,1/5\}\), there exists a changed source
\(\widetilde r_{L,a}\) with all the properties above such that

\[
\widetilde F_{L,a}(t)\equiv F_{\rm src}(t)\pmod{2^L},\qquad
\widetilde r_{L,a}(t)\equiv r(t)\pmod{2^L}
\quad\text{for every }t\in\mathbb Z_2.
\]

Here \(F_{\rm src}\) is the authentic analytic isometry with
\(F_{\rm src}(0)=0\) and exact rational forward values
\(F_{\rm src}(n)=U_n\). Its analyticity, isometry, and origin identity
are inherited from
[PI_DYADIC_SOURCE_ISOMETRY.md](../../2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md),
DSI-2--DSI-4, rather than inferred from numerical comparisons.

**Proof.** Construct a correction

\[
G(t)=\sum_{k\ge1}g_k\binom tk,
\qquad g_k\in2^{2k+L}\mathbb Z_{(2)}.
\]

At the \(n\)-th step choose \(g_n\) so that

\[
\left|F_{\rm src}(n)+\sum_{k=1}^{n}g_k\binom nk-f_n\right|
<\delta_n.
\]

All previously fixed terms and \(F_{\rm src}(n)\) are rational.
Density of \(2^{2n+L}\mathbb Z_{(2)}\) in the real line makes the
choice possible with an odd-denominator rational coefficient. Put
\(\widetilde F_{L,a}=F_{\rm src}+G\) and
\(\widetilde r_{L,a}(t)=\widetilde F_{L,a}(t)
-16\widetilde F_{L,a}(t-1)\).

The previous factorial bounds prove \(G\) analytic, and now give

\[
v_2(G(t)-G(s))\ge v_2(t-s)+L+2.
\]

It is therefore strictly more contractive than the authentic isometry,
so their sum is still an isometry. Since \(G(0)=0\), the global zero
pin is exact. In fact \(G(t)\in2^{L+2}\mathbb Z_2\) uniformly; this
proves both displayed congruences, including the source congruence after
translation and multiplication by 16. At each nonnegative integer the
correction sum is finite, so every forward value remains an exact
odd-denominator rational. The real approximation inequalities are the
same as before, hence prove source positivity, the prescribed leading
decay, endpoint, and carry floors. The backward source sum again
telescopes exactly to \(\widetilde F_{L,a}\). This proves the claim.

Choosing \(L\ge4\) retains the authentic absolute low-nibble formula,
not merely the modulus-four clock or an unspecified Haar isometry.
More generally it retains every observation made solely from any fixed
finite number of source bits, at every clock index, while still defeating
the carry gate.

The quantifiers are essential:

\[
\boxed{\forall L\ \exists\text{ a changed source }\widetilde r_{L,a}.}
\]

There is no assertion of a single changed source agreeing at every
precision. A single rational forward source agreeing with the authentic
one modulo \(2^L\) for all \(L\) would agree exactly at every index.
The refinement proves a finite-precision dependency limitation, not a
counterexample with the full original four-pole premises.

## 6. What each control preserves

| Control | Exact four-pole forcing | Real zero seed | Rational diagonal forward states | Forward trajectory is the globally zero-pinned 2-adic analytic isometry |
|---|---|---|---|---|
| Same-forcing endpoint \(1/5\) | Yes | No | No | No |
| Same-forcing Kempner endpoint | Yes | No | Not established or assumed | No |
| PC9 rational counterfeit | No | Yes | Yes | No: backward value at zero is \(-1\) |
| Section 5 Mahler controls | No | Yes | Yes | Yes |
| Authentic target | Yes | Yes | Yes | Yes |

For the first two rows the **source-only** backward identity is unchanged;
the altered real trajectory does not match it. Local finite-quotient Haar
and a global zero-pinned diagonal orbit are distinct requirements.

## 7. Verdict and the remaining selective mechanism

**Refuted within the broad proposed class:** nonzero closed-loop winding,
nonzero angular energy, ordinary irrationality type, local dyadic Haar,
or even global analytic dyadic isometry plus zero pin force a positive
rate in the selected fourth-root quadrature. The controls above give
explicit receipts for the corresponding broadened implications.

**Still open:** the density claim for the original four poles, their exact
integer chronology, the rational real/2-adic diagonal embedding, and the
zero seed together. None of these controls refutes that full assertion.

A viable quantization argument must identify both a quantum that excites
this quadrature and a source-selected lower bound on its rate. Here the
quantum is already exact, \(1-w(C_n)\in\{0,2\}\); proving that the
nonzero quantum occurs on a positive lower proportion of every late
shell is the unpaid step. A source-specific arithmetic restriction on
the forbidden carry words, using the literal four-pole denominator and
its coupling to the full real winding, could pay it. Generic energy or
isometry statements cannot.

### An exact filter audit for the next attack

Let \(P(E)=\sum_{j=0}^{m}a_jE^j\) be a finite constant-coefficient
time filter, where \(EU_n=U_{n+1}\). A real seed change \(s\) gives
\(U_n(s)=U_n(0)+16^ns\), and hence exactly

\[
P(E)U_n(s)-P(E)U_n(0)=16^nP(16)s.
\]

Every such source echo with \(P(16)=0\) is seed-blind. The corresponding
circle character is also seed-blind. This remains true when the echo is
evaluated using every coefficient and pole of the literal source.
For variable-coefficient filters the same criterion is
\(\sum_j a_{n,j}16^j=0\) at each index.

In particular, writing the original rational forcing as
\(r(n)=P_2(n)/D_4(n)\), the exact identity

\[
D_4(n)[U_n-16U_{n-1}]=P_2(n)
\]

and any subsequent finite differences of it eliminate the seed. They
can certify source excitation but cannot alone choose the selected
carry orientation. This is a structural property, not a claim that all
temporally coupled probes fail.

An admissible next argument must expose where it retains the zero-seed
selection: for example, a filter with \(P(16)\ne0\) and the specified
boundary value, or a floor/branch operation taken before source
elimination. It must also use a finite-pole or denominator-height
restriction that excludes section 5. Passing these tests does not
prove the density estimate; failing them identifies a precise lost
premise and supplies the controls above for calibration.

### Finite calibration scope

An exact `fractions.Fraction` audit checked the authentic carry implication
through index 512 (261 hits), charge-one periodic loops for lengths 1
through 16, and PC9 through index 128. A separate exact Mahler construction
checked both endpoints through index 48, including positive source,
coefficient divisibilities, carry floors, and all 1176 distinct index pairs
for the isometry identity at each endpoint. These finite checks calibrate
the formulas; the universal control statements rest on the proofs above.
No normality or authentic positive-density claim is inferred from them.
