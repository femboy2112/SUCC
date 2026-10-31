# Original four-pole BBP source as a zeta-shifted Dirichlet boundary at s=-1

**Status: exact source-specific paper derivation and independently calibrated finite sums.** The only external analytic input is classical zeta's pole at 1 and Gamma/digamma finite sums. This is an additional instrument in the freestanding N/Z arithmetic carrier, NOT an equality between ζ(-1) and an ordinary divergent sum; NOR does it prove π normality, RH or a selected signed real-circle bound.

## 1. A source-specific Dirichlet family of the integer carrier

For the original immutable four-pole BBP forcing,

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n),
\]

write `δ=(1,4,5,6)`, `c=(4,-2,-1,-1)`, `q_δ=δ/8` and `w_δ=c_δ(8-δ)/64`, i.e.

\[
 \boxed{w=(7/16,-1/8,-3/64,-1/32),\quad \sum_δ w_δ=15/64=:A.} \tag{BR1}
\]

The exact cancellation `Σc_δ=0` gives the partial-fraction identity

\[
 \boxed{n r(n)=\sum_{δ}\frac{w_δ}{n-1+q_δ}.}\tag{BR2}
\]

Therefore every finite cumulative source-path sum obeys

\[
 \boxed{\sum_{n=1}^N n r(n)=\sum_δ w_δ[\psi(N+q_δ)-\psi(q_δ)].}\tag{BR3}
\]

This is **not** an assumed observer distribution: it is a literal exact identity of the original signed source at every natural-number time, with no changed seed or pole. As N grows, `ψ(N+q)=log N+O_q(1/N)`, hence

\[
 \boxed{\sum_{n=1}^N n r(n)= A\log N+F_{\rm BBP}+O(N^{-1}),\quad F_{\rm BBP}=-\sum_δ w_δ\psi(q_δ).} \tag{BR4}
\]

Numerical calibration: `F_BBP=3.32249791110640475659473238782379790945...`.

## 2. Explicit positive harmonic remainder and effective finite certificate

The authentic source has the nonnegative Laplace decomposition

`r(n)=6/[a(a+3)]+4/[a(a+4)]+5/[a(a+5)]`, `a=8n-7`.

The published/inherited elementary source bounds are

`15/(8n-2)^2 < r(n) < 15/(8n-7)^2`, with harmless endpoint strictness.

Define the **actual rational source defect**

\[
 g(n)=r(n)-\frac{A}{n^2},\qquad A=15/64.
\]

Because `8n-2<8n` and `r(n)≥15/(8n-2)^2`, the defect is strictly positive for every n. For n≥2, use `8n-7≥(9/2)n` and

\[
 \frac1{(8n-7)^2}-\frac1{(8n)^2}
 =\frac{112n-49}{64n^2(8n-7)^2}
 \le\frac7{81n^3}.
\]

Hence

\[
 \boxed{0<g(n)\le\frac{35}{27n^3}\quad(n\ge2),\qquad g(1)=2783/960>0.} \tag{BR5}
\]

This yields an absolutely convergent, **positive source-specific finite-part correction**

\[
 G(-1)=\sum_{n\ge1}n g(n)
 =F_{\rm BBP}-A\gamma
 =3.18721298964510799239008111671073483967\ldots,
\]

with the explicit all-N positive truncation certificate

\[
 \boxed{0<G(-1)-\sum_{n=1}^N n g(n)\le\frac{35}{27N},\quad N\ge2.} \tag{BR6}
\]

Since `0<H_N-log N-γ<1/(2N)`, the finite harmonic source realization also obeys

\[
 \boxed{\left|\sum_{n=1}^N nr(n)-A\log N-F_{\rm BBP}\right|
 \le\frac{A/2+35/27}{N},\quad N\ge2.}\tag{BR7}
\]

This is a genuinely source-derived *effective* finite-to-analytic compatibility law; the constants are conservative and can be sharpened.

## 3. Why the singularity is at the same analytic coordinate −1

For `Re(s)>-1`, define the convergent original-source Dirichlet series

\[
 \mathcal D_R(s)=\sum_{n\ge1}\frac{r(n)}{n^s}.
\]

The exact decomposition BR5 implies

\[
 \boxed{\mathcal D_R(s)=\frac{15}{64}\zeta(s+2)
 +\sum_{n\ge1}\frac{g(n)}{n^s}.} \tag{BR8}
\]

The remainder series converges locally uniformly for `Re(s)>-2`; classical ζ(s+2) has a simple pole at s=-1, with Laurent expansion `1/(s+1)+γ+O(s+1)`. Thus

\[
 \boxed{\operatorname{Res}_{s=-1}\mathcal D_R(s)=15/64,\qquad
 \operatorname{FP}_{s=-1}\mathcal D_R(s)=F_{\rm BBP}.} \tag{BR9}
\]

This is a **source-twisted Dirichlet series**, *not* ζ(s) itself. Its pole at -1 comes from the original first source jet `Q'(0)=15` combined with the native clock step 8. The finite part retains the complete original four-pole shifts. In a distinct universal zeta channel, ζ(-1) is a regular analytic value reached via functional equation; they are separate target objects on the same declared integer carrier.

## 4. A controlled source mutant separates the finite part from the leading residue

Replace the original four signed poles by the explicitly **changed** positive rank-two source

\[
 r_{\rm mut}(n)=\frac5{8n-7}-\frac5{8n-4}.
\]

The mutant also has leading `r_mut(n)~15/(64n²)` and the same source rank-two Gamma/Pascal/golden limit (under the declared observer), hence its source Dirichlet series has exactly the same residue at `s=-1`. But its finite-part weights are

\[
 w_{\rm mut}=(35/64,-20/64,0,0),
\quad F_{\rm mut}=-\frac{35}{64}\psi(1/8)+\frac{20}{64}\psi(1/2),
\]

which is not equal to the authentic `F_BBP`. This proves that the new finite part retains source-specific information that leading Gamma rank and first asymptotic slope do not.

**Counterseed firewall:** If the same forcing is used but seed changes to `s*=−π/16`, then BR1–BR9 remain identical. So the finite part detects source mutations but **not** the distinguished selected π boundary. To prove digit normality one still needs a separate source-and-zero-seed-sensitive signed/carry/CRT/occupation estimate, not another scalar Gamma identity.

## 5. Next instrument

Consider the bivariate source/observer family `D_R(s,u)=Σ_(n≥1)n^(-s) ∂_u log V(8n-7+u)`, where `V(a)=a^4/[(a+3)^2(a+4)(a+5)]` comes from sibling PR416. BR8–BR9 locate its s=-1 singularity and first source-specific finite part. Determine whether transporting **both** the universal Hasse/Pascal analytic-order tangent and the BBP source-shift u-tangent yields a nontrivial *mixed* observable with a fixed operational common basis. Compare source mutant and coherent seed; no phase or nontrivial holonomy is licensed without an actual transport law.

Status: PROVED LOCAL algebra/analytic continuation, exact finite tests and independent numerical oracle. No new analytic zero-free region, Weil positivity, RH or π normality theorem. No academic novelty claim for underlying Dirichlet/Gamma methods.
