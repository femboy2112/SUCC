# ORIGINAL FOUR-POLE MOMENT JETS: baseline cancellation, hidden derivative and critical exponent

**2026-11-05, research only; descendant of PR #520.** Original four signed BBP poles and zero seed untouched. This is exact rational multipole/resolvent calculus, not a proof of π normality, RH, quantum physics or worldwide priority.

## SM-01: genuine primitive four-pole source = a zero-valued moment with nonzero higher jets

For the authentic original injection
\[
r_o(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\]
let weights \(w=(4,-2,-1,-1)\) and shifts \(c=(7,4,3,2)\). Define
\[
M_k(w)=\sum_{j=1}^4w_jc_j^k,\quad
F_w(z)=\sum_{j=1}^4\frac{w_j}{1-c_jz}.
\]
Then \(F_w(z)=\sum_{k≥0}M_k z^k\) in |z|<1/7, \(F_w^{(k)}(0)=k!M_k\) and
\(r_w(n)=\frac1{8n}F_w(\frac1{8n})\). The **EXACT** original source moments are
\[
\boxed{(M_0,M_1,M_2,M_3,M_4)=(0,15,151,1209,8995),}
\quad
F_w(0)=0,\ F'_w(0)=15,\ F''_w(0)=302,\ F'''_w(0)=7254.
\]
Hence the first total-pole \(1/n\) moment cancels but the FIRST source derivative is nonzero:
\[
r_o(n)=15/(64n^2)+151/(512n^3)+1209/(4096n^4)+O(n^{-5}).
\]
The zero \(M_0=0\) means only the linear functional “sum of signed pole weights” vanishes. It does NOT assert the paired pole object or the original orbit is literally the zero object; higher response is retained. This formalizes the user's proposed observer-relative baseline zero in a SOURCE-SPECIFIC way.

## SM-02: exact construction from THREE primitive unit-pair differences

Choose the fourth pole \(c=2\) as a declared reference, not a canonical unique basis. Then
\[
\boxed{
r_o(n)=4\left[\frac1{8n-7}-\frac1{8n-2}\right]
-2\left[\frac1{8n-4}-\frac1{8n-2}\right]
-\left[\frac1{8n-3}-\frac1{8n-2}\right].}
\]
Every primitive source pair \((8n-a)^{-1}-(8n-b)^{-1}=(a-b)/[(8n-a)(8n-b)]\) has an IDENTICALLY ZERO zeroth moment and a nonzero first moment. This is literal algebraic “1−1” primitive cancellation in the source family. The invariant M1=15 of the full four poles is independent of the chosen primitive reference; the pair decomposition is not. Combining pair support produces the original source but does NOT imply source-selected Haar.

## SM-03: general source cancellation depth controls the primitive carry scale

For any fixed rational weights/shifts with a common arithmetic denominator 8n, suppose \(M_0=\cdots=M_{q-1}=0\), \(M_q\ne0\). Then as n→∞,
\[
r_w(n)=\frac{M_q}{8^{q+1}n^{q+1}}+O(n^{-(q+2)}).
\]
For \(B=16^m\), \(R_{m,w}(n)=\sum_{j=1}^m16^{m-j}r_w(n+j)\), the dominated geometric moment estimate is uniform in m:
\[
R_{m,w}(n)=\frac{B-1}{15}\frac{M_q}{8^{q+1}n^{q+1}}+
O_w(B/n^{q+2}).
\]
Thus the **SOURCE-DETECTION scale** is
\[
\boxed{B\asymp n^{q+1},\qquad m\approx(q+1)\log_{16}n.}
\]
A positive correction window is guaranteed only under suitable positivity and \(0<R<1\) hypotheses; a nonvanishing forcing scale does NOT guarantee any selected orbit enters the window.

Three calibrated source hypotheses:
- ORIGINAL \(w=(4,-2,-1,-1)\): q=1, first coefficient M1=15 ⇒ \(R_m\sim B/(64n²)\), depth \(2\log_{16}n\).
- ONE-POLE MUTANT \(w=(5,-2,-1,-1)\): q=0, M0=1 ⇒ \(R_m\sim B/(120n)\), depth \(\log_{16}n\).
- DOUBLE-NULL primitive \(v=(1,-4,3,0)\): M0=M1=0, M2=12 ⇒
\[
\boxed{r_v(n)=\frac3{(2n-1)(8n-7)(8n-3)}
\sim\frac3{128n³},\quad R_{m,v}\sim\frac{B}{640n³}.}
\]
Its critical depth is \(3\log_{16}n\). These are exact source derivatives and falsifiable primitive scale predictions, NOT independent random dynamical laws.

## SM-04: source moment cancellation alone is still seed-blind

Every homogeneous initial seed for a fixed forcing \(r_w\) has the SAME \(M_k\), \(F_w\), critical exponent, source-gauge tail and ensemble carry covariance bound. In particular, the original four-pole source with coherent completed seed β=0 has \(U_n=-T_n\to0\) and is NONNORMAL despite \(M_0=0\), \(M_1=15\) and the entire same moment hierarchy. The moment sequence authenticates **which source hypothesis** was actualized; it cannot determine **which completed homogeneous source history** was selected without literal seed/carry information. The existence of the circle and Yoneda-type source observer map is not an ergodicity proof.

The next discriminating problem is therefore to couple this **source-specific cancellation order** to a proven arithmetic inequality for the exact zero-seeded history, e.g. a signed bound on fixed-radius Clausen energy Q_(1/2)(µ_A), or a quantitative selected critical moving-window deviation distinguishing the coherent/periodic same-source seeds. A result true for all source histories cannot by itself prove π normality.

**Validation:** five symbolic/exact Fraction focused tests on M0–M3, the 3-pair identity, one-pole changed exponent, double-null rational reduction, and primitive source-scale estimates all PASS. They calibrate formulas at finite n and do not certify asymptotic distribution.
