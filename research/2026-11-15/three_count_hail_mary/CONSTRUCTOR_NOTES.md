# Constructor: exact-source budget, finite-state obstruction, and sharp floor flux

**Parent:** `bf27f7ec8e757482613808bff693ba520ac13b3b` (#650).
**Scope:** the original four rational poles; no change to their coefficients.
**Verdict:** the zero-seeded positive three-count budget is **OPEN**. This pass
proves a stronger obstruction to a seed-uniform potential argument, and an
asymptotically sharp, signed floor-flux construction. Neither result proves
the authentic budget or pi normality.

The first pass used the inherited notes and source recurrence without reading
the other agents' new reports. Root subsequently communicated the translator's
mask-specific tail-removal observation. Section 4 independently sharpens its
rate and tests its sign; the upper tail-removal theorem is not claimed here
as an independent discovery.

## 1. What the three counts actually ask for

Write

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n),\quad C_n=\lfloor U_n\rfloor.
\]

The inherited clock gives \(K_n=J_n-C_n\pmod4\), \(J_n=n\pmod4\).
Consequently the lower-certificate summand has the following exact form:

\[
\begin{aligned}
\ell_n
&=1_{\{J_n=K_n=0\}}+1_{\{K_n=1\}}-1_{\{J_n<2,K_n<2\}}\\
&=1_{\{n\equiv2\ (4),\ C_n\equiv1\ (4)\}}
 +1_{\{n\equiv3\ (4),\ C_n\equiv2\ (4)\}}
 -1_{\{n\equiv1\ (4),\ C_n\equiv1\ (4)\}}.
\tag{C1}
\end{aligned}
\]

Thus \(L_B=B^{-1}\sum_{B\le n<2B}\ell_n\) is a signed, clock-conditioned
carry count. It is not a nonnegative energy. For a fixed carry residue, the
four simultaneous clock/cofactor gauge shifts obey

\[
\sum_{q=0}^3g(J+q,K+q)=1_{\{J-K\equiv2\ (4)\}},
\quad
g(j,k)=1_{k=1}+1_{j=k=0}-1_{j<2,k<2}.
\tag{C2}
\]

Therefore a choice among these four gauges can extract one quarter of an
already established residue-2 frequency. It does not establish that frequency.
This identifies precisely why a gauge average alone does not close the gate.

## 2. A source-exact obstruction to uniform bounded potentials

### 2.1 Finite-horizon, deep-dyadic shadows

For a changed real seed \(s\), keep the same forcing at every time:

\[
U_n(s)=U_n(0)+16^ns=16^n(\alpha+s)-T_n,
\quad \alpha=\pi/16,
\quad T_n=\sum_{j\ge1}16^{-j}r(n+j).
\tag{C3}
\]

**PROVED.** Given any finite horizon \(N\) and prescribed precision \(M\),
there is an odd-denominator rational seed \(s\in2^M\mathbb Z_{(2)}\) such
that the carry residues through that horizon are

\[
C_n(s)\equiv
\begin{cases}1,&n\equiv1\pmod4,\\3,&n\not\equiv1\pmod4.
\end{cases}
\tag{C4}
\]

Here \(\mathbb Z_{(2)}\) denotes rationals with odd reduced denominator.
These trajectories use the exact four poles, retain odd-denominator rational
states, and satisfy

\[
U_n(s)-U_n(0)\in2^{M+4n}\mathbb Z_{(2)}.
\tag{C5}
\]

In particular the authentic mod-four clock is unchanged for every positive
index when \(M\ge0\).

**Proof.** Let

\[
\beta=0.\overline{1333}_{16}=983/13107.
\]

The four fractional parts of \(16^n\beta\) are rotations of this word,
all at least \(\beta\), and all below \(1/4\). The inherited bound
\(0<T_n<1/(64n^2)\le1/64\), together with \(\beta>1/64\), implies
that \(\lfloor16^n\beta-T_n\rfloor\) has precisely the carry residues
(C4). There is an open interval of completed endpoints about \(\beta\)
on which all these finitely many floors agree. The set
\(\alpha+2^M\mathbb Z_{(2)}\) is dense in \(\mathbb R\): for any odd
\(q\), its points \(\alpha+2^Ma/q\) have spacing \(2^M/q\), which tends
to zero along odd \(q\). Choose a point in that interval. Equation (C5)
then follows from (C3). This is a constructive finite approximation, not an
infinite-time claim about a fixed rational seed. \(\square\)

On any shell in that horizon,

\[
L_B(s)=-\frac1B\#\{B\le n<2B:n\equiv1\pmod4\}
       =-\frac14+O(B^{-1}).
\tag{C6}
\]

This refutes a positive block drift that is uniform over all carrier states
with the exact source and any fixed amount of authentic dyadic information.
It also refutes a proposed telescoping estimate

\[
\sum_{n=B}^{2B-1}\ell_n
\ge\delta B+V_B(U_B)-V_{2B}(U_{2B}),
\qquad |V_n(x)|\le M_0,
\tag{C7}
\]

if (C7) is asserted for all those states with fixed \(\delta>0,M_0<\infty\).
Take \(B\) arbitrarily large and use (C6). A potential valid only on the
actual zero-seeded orbit is not refuted; proving its bound would have to use
that source selection explicitly. Unbounded or height-sensitive corrections
are also not excluded by this argument.

### 2.2 The authentic denominator grid still permits bad late blocks

Let \(D_B=\operatorname{lcm}(1,3,\ldots,8B-1)\); the letter \(D\) avoids
confusing this modulus with the statistic \(L_B\). The authentic state
\(U_B(0)\) belongs to \(D_B^{-1}\mathbb Z\).

Fix a desired residue word \(d_n\in\{1,3\}\), \(B\le n<2B\), and a
precision \(M\). If

\[
\frac{2^M}{D_B}<16^{-(B-1)},
\tag{C8}
\]

then an alternate state \(V_B\in D_B^{-1}\mathbb Z\) exists with
\(V_B-U_B(0)\in2^M\mathbb Z_{(2)}\), such that the exact future recurrence
has \(\lfloor V_n\rfloor\equiv d_n\pmod4\) for the whole shell. Every
future reduced denominator divides the authentic \(D_n\).

**Proof.** Choose integers \(q_B=d_B\) and
\(q_n=16q_{n-1}+d_n\). Because \(0<r(n)<1\) for \(n\ge2\), the
backward inverse of each interval \((q_n,q_n+1)\) lies within
\((q_{n-1},q_{n-1}+1)\): its fractional part is
\((d_n+u-r(n))/16\in(0,1)\) for \(0<u<1\). Pulling back the final
unit interval therefore gives an initial open interval of length
\(16^{-(B-1)}\) satisfying the whole word. The points of
\(D_B^{-1}\mathbb Z\) congruent to \(U_B(0)\) modulo \(2^M\) have
real spacing \(2^M/D_B\); (C8) puts one in that interval. The denominator
claim follows by induction using the actual four-pole denominators.
\(\square\)

This is a conditional, exact lattice lemma. No estimate of the growth of
\(D_B\), prime distribution, or equidistribution is needed for it. It shows
that a local proof cannot replace the zero-seeded ancestry by only the
current denominator divisor and sufficiently many dyadic congruences.

### 2.3 Executed exact receipt

An independent Python `Fraction` calculation, using the displayed four-pole
formula directly, instantiated (C8) at \(B=8,M=48\). It produced

\[
D_8=18472920064106597929865025,
\]

\[
s=-\frac{117004818048662636658688}{595900647229245094511775},
\quad v_2(s)=16,
\]

\[
U_8(s)=\frac{6311125010945226836920984}
                   {2052546673789621992207225}.
\]

The denominator of this state divides \(D_8\),
\(v_2(U_8(s)-U_8(0))\ge48\), and the entire recurrence through index 15
has odd denominators and clock \([U_n(s)]_4=n\pmod4\). Its audited shell is:

| n | carry mod 4 | cofactor K | summand ell |
|---:|---:|---:|---:|
| 8 | 3 | 1 | 0 |
| 9 | 1 | 0 | -1 |
| 10 | 3 | 3 | 0 |
| 11 | 3 | 0 | 0 |
| 12 | 3 | 1 | 0 |
| 13 | 1 | 0 | -1 |
| 14 | 3 | 3 | 0 |
| 15 | 3 | 0 | 0 |

Thus this source-exact, clock-exact, late-height-matched control has
\(L_8=-1/4\). Its seed is explicitly **not zero**. This is a receipt against
the proposed uniform proof architecture, not a counterexample to the
authentic theorem.

## 3. The signed floor boundary flux

For any real completed endpoint \(\beta\), define

\[
P_n=\lfloor16^n\beta\rfloor,\quad
C_n^{\beta}=\lfloor16^n\beta-T_n\rfloor,
\quad b_n=1_{\{\{16^n\beta\}<T_n\}}.
\]

Since \(0<T_n<1\), \(C_n^{\beta}=P_n-b_n\). Put

\[
f_j(c)=1_{\{j=2,c\equiv1\}}
       +1_{\{j=3,c\equiv2\}}
       -1_{\{j=1,c\equiv1\}},
\]

where residues are modulo four. At a borrow, the exact difference is

\[
\begin{aligned}
f_j(P_n-1)-f_j(P_n)
={}&(1_{j=1}-1_{j=2})(1_{P_n\equiv1}-1_{P_n\equiv2})\\
 &+1_{j=3}(1_{P_n\equiv3}-1_{P_n\equiv2}).
\tag{C9}
\end{aligned}
\]

The right side has both signs. Positivity or complete monotonicity of
\(T_n\) does not select either sign. Its only potentially helpful effect
is to make nonzero-mask borrow sites rare; raw borrow sites can be numerous.
Section 4 proves that this rarity estimate is already sharp in order and
leading asymptotic constant when the endpoint is unrestricted.

## 4. Sharpness of the logarithmic mask-tail error

### 4.1 A lower bound using the literal four poles

For \(n\ge1\), direct subtraction gives

\[
r(n)-\frac{15}{64n^2}
=\frac{9664n^3-9656n^2+3090n-315}
 {64n^2(2n-1)(4n-1)(8n-7)(8n-3)}>0.
\]

Indeed, at \(n=m+1\), the numerator becomes
\(9664m^3+19336m^2+12770m+2783\). Hence

\[
\frac{15}{1024(n+1)^2}<T_n<\frac1{64n^2}.
\tag{C10}
\]

Both inequalities retain the original finite source law. The lower one uses
only the first term \(16^{-1}r(n+1)\) of the positive tail.

### 4.2 One fixed endpoint realizes negative flux of the sharp size

For an integer \(n\ge1\), let \(q(n)\) be the smallest positive multiple
of four such that

\[
16^{q(n)}-1>\frac{1024}{15}(n+1)^2.
\tag{C11}
\]

Choose \(n_1=2\) and recursively \(n_{k+1}=n_k+q(n_k)\). All markers
are \(2\pmod4\), their gaps are nondecreasing, and

\[
q(n)=2\log_{16}n+O(1).
\tag{C12}
\]

Define the single endpoint

\[
\beta_- =\sum_{k\ge1}16^{-n_k}.
\tag{C13}
\]

Its hexadecimal digits are 1 at the markers and 0 elsewhere. It is
irrational, because its nonzero digits are infinite and its zero runs are
unbounded; such a digit sequence is not eventually periodic.

At a marker, monotonicity of the future gaps yields

\[
\{16^{n_k}\beta_-\}
=\sum_{j\ge1}16^{-(n_{k+j}-n_k)}
\le\sum_{j\ge1}16^{-j q(n_k)}
=\frac1{16^{q(n_k)}-1}
<\frac{15}{1024(n_k+1)^2}<T_{n_k}.
\tag{C14}
\]

Every marker therefore borrows from completed digit 1 to source-floor carry
0. At every other index the completed digit is 0, and its carry is 0 or 3.
Consequently the selected carry gate and the lower statistic of this changed
seed vanish **at every positive index**:

\[
1_{\{C_n^{\beta_-}\bmod4\in\{1,2\}\}}=0,
\qquad f_{n\bmod4}(C_n^{\beta_-})=0.
\tag{C15}
\]

The completed-digit statistic is exactly the marker indicator. If
\(m_B=\#\{k:B\le n_k<2B\}\), its signed floor correction is therefore

\[
\frac1B\sum_{B\le n<2B}
 \bigl(f_{n\bmod4}(C_n^{\beta_-})-f_{n\bmod4}(P_n)\bigr)
=-\frac{m_B}{B}.
\tag{C16}
\]

Monotonicity of \(q\) gives, for all sufficiently large \(B\),

\[
\frac{B}{q(2B)}-1\le m_B\le\frac{B}{q(B)}+1.
\]

Together with (C12), this proves

\[
\boxed{\quad
\frac{m_B}{B}=\frac1{2\log_{16}B}
             +O\!\left(\frac1{(\log B)^2}\right).
\quad}
\tag{C17}
\]

Thus a universal mask-tail upper error of size
\(1/(\lfloor\log_{16}(64B^2)\rfloor+1)+O(B^{-1})\) has the correct
leading asymptotic constant. No universal \(o(1/\log B)\) estimate is
available even with the exact four-pole tail.

Starting instead at \(n_1=1\), with the same gap rule, puts every marker
at clock class 1. The completed statistic is then minus the marker count;
the source-floor statistic still vanishes. This gives positive flux of the
same asymptotic size. The sign cannot be recovered from the tail's positive
Gamma/Beta representation alone.

### 4.3 Exact scope of this control

The two endpoints use the original forcing and real seeds
\(s_\pm=\beta_\pm-\alpha\). They are not the authentic zero seed, and
their real states are not asserted to have odd rational denominators.
Indeed \(0<\beta_\pm\le1/15<\pi/16\), so both seeds are nonzero; the
irrationality of each endpoint does not settle the rationality of its seed.
On any fixed finite interval, the open floor conditions can be shadowed by
odd-denominator rational seeds in \(2^M\mathbb Z_{(2)}\) as in Section 2,
while preserving any fixed dyadic precision. All inequalities at the marker
boundaries are strict. Even if a non-marker value lands exactly on an integer,
all finitely many completed and source-floor values remain unchanged on a
sufficiently short common right neighborhood of the endpoint. That supplies
the required open interval. No infinite rational-seed analogue is claimed.

## 5. What failed, what survived, and the remaining source premise

**Failed implication, with receipts:** positive four-pole forcing, exact
dyadic clock, odd denominators, the authentic late denominator grid, and a
bounded local/telescoping correction do not by themselves force a positive
three-count budget. Section 2 supplies exact source-matched finite controls.
The missing information is the zero-seeded ancestry, not another positive
norm. A state-uniform argument cannot silently supply it.

**Surviving theorem:** the fixed positive four-pole tail admits both signs
of floor flux at the largest universal asymptotic scale. The logarithmic
mask-tail removal is therefore quantitatively sharp across completed
endpoints. This is a proved boundary of a proposed proof architecture, not
a boundary on a source-selected proof for pi.

**Smallest unpaid source statement after these reductions:** establish for
the actual \(U_0=0\) orbit a fixed positive margin in the signed count (C1),
on every sufficiently late integer shell. One possible split is to bound
the difference between the two clock-conditioned residue-1 counts below
by \(-\varepsilon B\), while proving more than \(\varepsilon B\)
residue-2 events at clock class 3. Neither half is proved by this pass.

Removing the tail at its now calibrated rate transfers this question to
the completed digits of \(\pi/16\); it does not supply their distribution.
The finite rational source remains load-bearing through that selected
endpoint. The complete all-frequency normality objective requires further
estimates beyond this one positive signed count.

## 6. Validation record and truth states

- **PROVED:** (C1)-(C2), finite-horizon shadow lemma, denominator-grid lemma,
  signed flux identity, lower tail bound, fixed-endpoint sharpness theorem.
- **OBSERVED, exact arithmetic:** the explicitly printed \(B=8,M=48\)
  rational-seed control; every listed residue and congruence was computed
  with Python `Fraction`, using no approximation of pi.
- **OBSERVED, additional exact checks:** all 16 cells of (C1), (C2), and
  (C9); marker-tail inequalities for every generated marker below 100000;
  and both counting bounds for \(B=16,64,256,1024,4096,16384,32768\).
  The one-off script completed 17391 assertions. These checks calibrate
  the formulas; the all-index claims use the proofs above.
- **CROSS-REVIEW:** after the first pass, read Theorem A-FS in
  `ADVERSARY_NOTES.md`. Its rational prefix construction, constants,
  dyadic typing, and stated height bound passed inspection. This is a
  same-model mathematical cross-check, not an independent empirical witness.
- **OPEN:** eventual positive budget for the authentic zero seed; any
  positive lower density obtained from it; the full pi-normality target.
- **Not run by this child:** the repository's full test suite or fresh
  authentic-source holdouts. Root owns those checks. No production module,
  frozen source file, or GitHub state was modified by this contribution.

## 7. Focused second pass: the exceptional set contains optimal-type endpoints

**2026-11-16.** Root asked whether the proposed Hausdorff-dimension analysis
of the exceptional set can combine with existing source arithmetic to close
the gate. Independently of any dimension claim, define

\[
\mathcal E=\left\{\beta:\liminf_{B\to\infty}\frac1B
 \sum_{B\le n<2B}1_{\{\lfloor16^n\beta-T_n\rfloor\bmod4\in\{1,2\}\}}=0\right\}.
\]

There is an explicit inherited element of this set with the best possible
ordinary irrationality exponent **and** zero restricted radix exponent.
Let \(t_0=0,t_{2k}=t_k,t_{2k+1}=1-t_k\) and set

\[
\beta_{\rm TM}=3\sum_{k\ge1}t_k16^{-k}.
\tag{C18}
\]

Every three consecutive Thue--Morse symbols contain a complementary pair.
Its completed hexadecimal digits belong to \(\{0,3\}\), and therefore

\[
3/4096\le\{16^n\beta_{\rm TM}\}\le1/5\qquad(n\ge0).
\tag{C19}
\]

For \(n\ge5\), \(T_n<1/(64n^2)<3/4096\), so no floor borrow occurs.
The exact original forcing then has no selected carries from time 5 onward.
Thus \(\beta_{\rm TM}\in\mathcal E\), with the stronger conclusion that
its selected shell density is identically zero for every \(B\ge5\).
This is the already proved control WP20--WP23 in
`../carry_quadrature_assault/WINDING_PACKETS.md`; it is not newly discovered
here.

Bugeaud's theorem gives irrationality exponent two for
\(\sum_{k\ge0}t_k b^{-k}\) for every integer \(b\ge2\). Rational scaling
therefore gives \(\mu(\beta_{\rm TM})=2\). The primary publisher record
was freshly reopened in this pass:
[Bugeaud, *On the rational approximation to the Thue--Morse--Mahler numbers*,
Ann. Inst. Fourier 61 (2011), 2065--2076, doi:10.5802/aif.2666](https://www.numdam.org/item/AIF_2011__61_5_2065_0/).
This is an imported theorem, not a finite experiment.

Moreover (C19) proves directly, with the repository's notation,

\[
v_{16}(\beta_{\rm TM})
=\limsup_n\frac{-\log\|16^n\beta_{\rm TM}\|}{n\log16}=0.
\tag{C20}
\]

**A sharpened application to the new exceptional set.** For any length-\(N\)
hexadecimal prefix \(A\in\{0,\ldots,16^N-1\}\), let

\[
\beta_A=(A+\beta_{\rm TM})/16^N.
\tag{C21}
\]

After the prefix its digits are again only 0 and 3. Equations (C19) and
the original tail bound give no selected raw carries for
\(n\ge\max(N+1,5)\). Rational affine changes preserve the ordinary
irrationality exponent, and the eventual shifted orbit gives the same
restricted exponent. Hence

\[
\boxed{\quad
\mathcal E\cap\{\beta:\mu(\beta)=2,\ v_{16}(\beta)=0\}
\text{ is dense in }[0,1].\quad}
\tag{C22}
\]

This matches any finite authentic digit prefix. It does not assert
\(\beta_A\ne\pi/16\) for every \(A\): such an equality question must not
be settled by assumption. To obtain an explicitly nonzero alternate seed,
one can use the two tails \(\beta_{\rm TM}/16\) and
\((3+\beta_{\rm TM})/16\) in the same prefix cylinder. Both have the
stated properties, are distinct, and a sufficiently narrow certified BBP
interval for \(\pi/16\) excludes at least one. The base control itself
is unequal to \(\pi/16\), since
\(\beta_{\rm TM}\ge51/256>47/240+1/1024>\pi/16\).
No rationality claim about the changed seeds is used.

**Inspection of the existing source arithmetic.** The relevant repository
results do not currently remove this obstruction:

- `../../2026-11-12/frontier_rungs/RESTRICTED_EXPONENT.md`, RDT-04(a),
  proves that the original BBP prefixes fail the restricted-transference
  test: their odd denominators grow exponentially while the completed
  remainder \(T_n\) decays only quadratically. Clearing those denominators
  spends the useful smallness. This is a scoped obstruction to the prefix
  forms, not a theorem against all possible approximants.
- RDT-06(a) proves a 2-adic shadow bound on the rational part of a Gaussian
  one-pole integral family. RDT-06(b) observes, in seven tested families,
  the valuation imbalance on the wrong coefficient for the desired pi
  estimate. The absence of a successful family is observational; no
  all-family impossibility is proved.
- Even a future improvement all the way to \(\mu(\pi)=2\) or
  \(v_{16}(\pi)=0\) would not, by those numerical properties alone,
  exclude \(\pi/16\) from \(\mathcal E\), as (C22) demonstrates.

**Second-pass verdict:** the dimension calculation can quantify the size of
the exceptional class, but neither finite irrationality type, its optimal
value two, the strongest nonnegative restricted exponent, nor finitely many
correct digits selects the authentic endpoint outside it. An exclusion must
use additional arithmetic of that endpoint or its exact zero-seeded
ancestry. This pass found no proved source-specific exclusion. The actual
four-pole-plus-zero-seed assertion remains untouched by these controls.
