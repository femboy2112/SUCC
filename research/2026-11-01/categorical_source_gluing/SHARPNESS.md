# CSG-16: three observations are genuinely necessary for a global successor

**2026-11-01. Exact research theorem.** Independent of numerical root fitting. Parent
[PR #449](https://github.com/femboy2112/SUCC/pull/449) proves the global
three-frame sphere embedding. This addendum supplies the complementary sharp
lower bound: the two-frame observation curve has a *real* self-collision whose
next observations differ. Its source is still the unchanged original four-pole
BBP rational function; no replacement forcing or seed is used.

Let

\[
R(z)=\frac{(8z-7)^4}{(8z-4)^2(8z-3)(8z-2)},\qquad
H_k(z)=(R(z),R(z+1),\dots,R(z+k-1)).
\]

## Theorem (CSG-16, exact)

There exist **distinct real** finite source coordinates \(x,y\), neither
at a cover pole and with their first two translates also avoiding cover poles,
such that

\[
H_2(x)=H_2(y),\qquad R(x+2)\ne R(y+2).
\]

Consequently **no single-valued successor map of any kind** on the full
raw two-observation image can satisfy \(S_2H_2=H_2(z+1)\). This is stronger
than merely failing to find a rational successor formula. Parent PR #449's
exact global H3 embedding shows that **three consecutive observations are
minimal for a globally faithful successor on the whole complex source sphere**.
This statement concerns the global source domain, not the selected
nonnegative-integer orbit: there the existing H2 inverse chart works all horizon.

## Proof: symmetric collision variables

For \(x\ne y\), put \(s=x+y\), \(p=xy\). The exact difference quotient of
\(A(x)D(y)-A(y)D(x)\), divided by \(x-y\) and a nonzero integer, is
\[
\begin{aligned}
f(s,p)={}&245760p^3+(-475136s+215552)p^2\\
 &+(318464s^2-308544s+75628)p\\
 &-73760s^3+114100s^2-60319s+10976.
\end{aligned}
\]
Thus \(R(x)=R(y)\) is equivalent to \(f(s,p)=0\) wherever the
cover values are finite. The second-observation collision is
\(f(s+2,p+s+1)=0\).

An **independently expanded 6×6 Sylvester determinant**, evaluated over
\(\mathbb Z[s]\), gives their resultant \(2111062325329920\,Q(s)\), where

\[
\begin{aligned}
Q(s)={}&138011809795276800s^9-356902560308264960s^8\\
&+435631352005140480s^7-326110189092528128s^6\\
&+163752693520971264s^5-56851206836033792s^4\\
&+13583685706776288s^3-2147182431023808s^2\\
&+203276412515538s-8758669850307.
\end{aligned}
\]

Let
\[
\begin{aligned}
a(s)={}&22293381120s^4-25663197184s^3+11554414080s^2\\
&-2390662784s+189988416,\\
b(s)={}&-3230484480s^5+8935808256s^4-7641171904s^3\\
&+3067138968s^2-606244406s+47673279.
\end{aligned}
\]

The independently expanded exact polynomial divisions show
\[
Q(s)\mid a(s)^3f(s,-b(s)/a(s)),\qquad
Q(s)\mid a(s)^3f(s+2,-b(s)/a(s)+s+1).
\]
Therefore any zero \(s_*\) of Q with \(a(s_*)\ne0\) supplies an
actual pair-collision with \(p_*=-b(s_*)/a(s_*)\).

The integer/rational evaluations give
\[
Q(301451/10^6)<0<Q(301452/10^6).
\]
Thus a real \(s_*\) exists in that open interval. Outward rational interval
Horner calculations on the **entire** interval give strict positivity of
\(a\), \(b\), \(8b-a\), and \(a-4b\). Hence
\[
-\frac14<p_*=-\frac{b(s_*)}{a(s_*)}< -\frac18.
\]
The two roots of \(X^2-s_*X+p_*\) are distinct and real, one positive and
one negative. Direct inequalities put the positive root in \((1/2,7/8)\)
and negative root in \((-1/2,-1/7)\). Their next translates lie in
\((3/2,15/8)\) and \((1/2,6/7)\), respectively. None hits one of the
three cover poles \(1/2,3/8,1/4\). Thus the two equalities of projective
observations are genuine, not cross-multiplication artifacts at an
indeterminate point.

## Third frame separates the collision

Set \(f_2(s,p)=f(s+4,p+2s+4)\), and let
\(V_2(s)=a(s)^3 f_2(s,-b(s)/a(s))\). The same independent polynomial
implementation reduces Q and \(V_2\) modulo **101**, with their leading
coefficients still nonzero. Their finite-field polynomial gcd has degree
**zero**. By the primitive-factor/leading-degree argument, Q and \(V_2\)
are coprime over \(\mathbb Q[s]\). In particular
\(V_2(s_*)\ne0\), so \(R(x+2)\ne R(y+2)\).

## Categorical interpretation and scope

The two-frame quotient is a faithful **generic** source coordinate and a
valid all-horizon integer-trajectory chart (original CSG-03/04). But the
full raw two-frame image is a singular observational quotient: it identifies
states with **different next observations**. Its normalization restores the
source P1, while adding the third observed coordinate is an explicit
embedding into an ordinary product of spheres with globally unambiguous
successor (parent CST-05). This supplies a sharp distinction between
birational recovery and a genuine global observational automorphism.

**New information:** exact real collision plus third-frame separation; a
proof of minimality for consecutive windows on the entire source sphere.
**Not implied:** selected π-digit cancellation, finite-time observation
resolution without error, physical quantum paths, RH, or a new
same-source-theory of all nonconsecutive observation sets.

Reproduce with no optional dependencies:

```sh
python research/2026-11-01/categorical_source_gluing/two_frame_sharpness.py
python -m unittest discover -s tests -p 'test_categorical_source_gluing_sharpness.py' -v
```
