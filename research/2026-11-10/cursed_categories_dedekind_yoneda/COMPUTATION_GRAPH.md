# Rational computation graphs of irrational cuts: Stern–Brocot, affine arrows, and authenticated BBP

**Status:** Exact classical algebra and paper proof; tested rational finite certificates for `sqrt(2)` and `pi/16`. This is a *representation* paper, not an ergodic theorem.

## CG-01. Two generator paths: Stern–Brocot certificates

For positive irrational `x`, begin with rational extended Farey bounds `0/1 < x < 1/0 = +infinity`, determinant `bc-ad=1` for lower `a/b`, upper `c/d`. Let the mediant be `m=(a+c)/(b+d)`. The exact cut oracle decides `x<m` versus `x>m`; equality never occurs because `x` is irrational. Write `L` in the first case (replace the upper bound by `m`), `R` in the second (replace the lower by `m`). Both replacements preserve `bc-ad=1` by direct expansion, and for finite endpoints the width is **exactly** `1/(bd)`. All data at any finite stage are rational numbers and two-by-two unimodular integer matrices.

The alphabet `{L,R}` is the generating set of a one-object free monoid category. Its action on Farey-neighbor states produces a path category. Every irrational positive x selects a unique infinite L/R word with infinitely many changes of direction. Conversely such a word has nested interval brackets shrinking to a unique positive irrational: whenever both directions recur, both denominators become arbitrarily large, and determinant one forces width ->0; a rational limit would have a finite mediant decision and then an eventually constant ray. Thus the poset of admissible rays ordered lexicographically (`L<R` at first differing bit) is **order-isomorphic** to the positive irrational order category. This is an actual alternative *equivalent computational-form category*, not an identification of the two-arrow monoid itself with the irrational poset.

Rational endpoints are the critical hostile case: a rational may terminate at a mediant or admit an eventually constant infinite boundary ray. Do not present *every* infinite binary word as a unique irrational. Nor assume the binary word is efficiently computable from a cut with a fixed uniform complexity bound: comparisons can require unbounded precision near rational mediants.

**Fresh exact finite receipt:** `pi/16` first 32 decisions = `LLLLLRRRRRRRRRRLRRRLLLLLLLLRRRRR`; final rational bounds `1818/9259 < pi/16 < 355/1808`, with determinant one and width `1/16740272`. For `sqrt(2)`, first 32 decisions = `RLLRRLLRRLLRRLLRRLLRRLLRRLLRRLLR`, with bounds `941664/665857 < sqrt(2) < 665857/470832`, width `1/313506783024`. The computation uses original-source rational intervals for π and integer-square-root dyadic intervals for sqrt(2); no floating point. These finite examples do **not** validate the infinite correspondence, which has the separate proof above.

## CG-02. Continued fractions and unimodular speedups

Consecutive Farey endpoints are integer vectors `(a,b),(c,d)` with determinant one. Each L/R mediant update adds one column to the other, i.e. multiplication by a nonnegative integer shear matrix of determinant one (orientation depends on the column convention). Runs `L^k` or `R^k` become a single shear with parameter k: **the continued-fraction partial quotients accelerate a ridiculously long path of elementary categorical arrows**. The compression is exact because matrix powers compute the same rational endpoints.

For a convergent `p_k/q_k` of an irrational x, classical continued-fraction theory gives `|x-p_k/q_k|<1/(q_k q_(k+1))`. If measuring phase `e(h16^n x)`, the trivial Lipschitz bound gives

`|e(h16^n x)-e(h16^n p_k/q_k)| <= 2*pi*|h|16^n/(q_k q_(k+1))`.

This can reduce the cost of *certified finite phase calculations* when a proven rational enclosure is available. It does not control signed averages; a large frequency can still require enormous denominators. Acceleration is a computational shortcut, not statistical contraction.

## CG-03. Original BBP source -> rigorous Dedekind intervals

Keep the immutable original forcing, for integer n>=1:

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`.

The source-selected completed cut is `x=pi/16=sum_(j>=1)16^(-j)r(j)` with **literal BBP zero seed**. Put `P_L=sum_(j=1)^L16^(-j)r(j)`. The source has Hausdorff-moment representation

`r(n)=int_0^1 t^(8n-8) (1-t)(t^2+2)(t^2+2t+2) dt`.

The integrand is positive on `(0,1)`, so r(n)>0 and r(n+1)<r(n) strictly. Therefore

`P_L < x < P_L + r(L+1)/(15*16^L)`.

The upper bound sums the geometric tail using `r(j)<=r(L+1)` for `j>=L+1`. Its width tends to zero; strict positivity proves the lower inequality. Upper bounds also decrease: for `H_L=P_L+16^(-L)r(L+1)/15`, use `r(L+2)<r(L+1)` to show `H_(L+1)<H_L`. This gives a **nested, source-derived, rational interval name** of the Dedekind cut.

One may query `q<x` using `q<=P_L`, or `q>x` using `q>=H_L`. For each rational q and irrational x the search halts at some finite L. It returns `UNKNOWN` if a finite budget expires. For fixed k, if `floor(16^k P_L)=floor(16^k H_L)`, that integer is the rigorously certified first-k-digit hexadecimal winding `k_k=floor(16^k x)`. The standalone module certifies the first 16 digits of `pi/16` as `3243F6A8885A308D` without a decimal π oracle. No asymptotic estimate is inferred.

## CG-04. A source-locked Yoneda square for the real phase

Let `theta_n={16^n x}` with integer winding `k_n=floor(16^n x)`. The true affine numerical arrow is `g_n=(16^n,-k_n)`. It transports the full Dedekind probe via

`F_(theta_n)(q)=F_x((q+k_n)/16^n)`.

At the authenticated original zero source, the exact rational recurrence gives

`U_0=0`, `U_n=16U_(n-1)+r(n)`, `U_n=16^n P_n`.

The *unwrapped* completed phase is `16^n x=U_n+T_n` with `T_n=sum_(j>=1)16^(-j)r(n+j)`. Thus the interval cut, rational recurrence, and winding agree after the positive future tail. The prime-power/integer-CRT observer must be **separately** transported: this real-cut proof does not discard old prime powers, identify an arbitrary winding, or prove a prime-local identity.

The source gauge is essential. Translating x by `1/16` changes the first digit but yields the same later fractional orbit for all n>=1: `{16^n(x+1/16)}={16^n x}`. Translating by the irrational `-x` makes the completed orbit zero; this is outside the rational affine action and **outside the category of irrational objects**. A proof that uses only later rational cut probes or only irrational objects cannot reject that coherent wrong seed.

## CG-05. Lambda semantics and the 2:3 discriminating bridge

A typed lambda compiler could present the finite source-bound production as a typed state transition `(L,P_L,H_L)->(L+1,P_(L+1),H_(L+1))`; a path certificate preserves source identity, rational arithmetic, and decreasing interval. It would map to the rational interval refinement category and then via evaluation to the cut presheaf. A faithful *reflection* theorem must prohibit forged interval boundaries, swapped sources, missing seeds, and false digit certifications. The standalone Python code does not supply that complete lambda-compiler theorem: **UNVERIFIED**.

The newest SUCC 2:3 joining instrument measures joint signed phases, not just pointwise precision. The cut tool can rigorously calculate each specified finite phase and its winding, but cannot infer the signed mean tends to zero. To seek load-bearing arithmetic, feed certified finite source intervals and complete 2:3 chronological pairing labels into #591/#593 signed-observer machinery, preregister independent comparison controls, and prove a new source-selected inequality that rejects normal-but-dependent, nonnormal-but-mixed-zero, and coherent wrong-seed countermodels.
