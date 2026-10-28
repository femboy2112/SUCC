# SUCC π: Gaussian Prime Ramification and the First Quadratic Source-Pair Branch

**2026-10-27 · Independent research-only child of [#324](https://github.com/femboy2112/SUCC/pull/324), pinned head fca58d3e0289e57596dd8ca74bace325a450df31.** This is an additive proof dossier for the concurrent Claude/Codex lanes, not a main merge, not a new π-normality theorem. All original signed source poles, initial zero, frozen archives, and inherited claims remain unchanged. The separate longer independent local dossier passed **12/12 standalone exact tests** (not a claim that GitHub's full native suite or these uploaded files ran); the small included probe exercises the key integer identities. **π normality and RH remain OPEN.**

## 1. Exactly which primes are exceptional in the original source?

The original forcing, not a fitted model, is

$$
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}
=\frac{A(x)}{D(x)},
$$

$$
A(x)=120x^2-89x+16,\qquad
D(x)=(2x-1)(4x-1)(8x-7)(8x-3).
$$

For a denominator pole factor \(ax+b\), the exact resultant is

$$
\mathrm{Res}(A,ax+b)=a^2A(-b/a)=120b^2+89ab+16a^2.
$$

In displayed pole order, these resultants are \(6,20,1920,-32\). Thus

$$
\boxed{\mathrm{Res}(A,D)=-2^{15}3^25^2.}
$$

The six pairwise denominator-factor resultants are \(2,-6,2,-20,-4,32\), giving

$$
\boxed{\mathrm{Disc}(D)=2^{24}3^25^2.}
$$

For the integral projective model

$$
[F(X,Y):G(X,Y)]=
[Y^2(120X^2-89XY+16Y^2):
(2X-Y)(4X-Y)(8X-7Y)(8X-3Y)],
$$

the homogeneous resultant is \(512^2\mathrm{Res}(A,D)=-2^{33}3^25^2\). Therefore **this rational map in its displayed normalized coordinates has good reduction at every prime \(p>5\)**, while \(2,3,5\) are precisely its bad-reduction primes. A statement about *minimal* bad reduction over all coordinate conjugacies is not proved. Local \(2\)-adic integrality of \(r(z)\) on its affine chart is compatible with global projective bad reduction at \(2\).

This is the source-specific, exact reason to investigate the complete small-prime set \(2,3,5\), with \(7\) as the first *clean* comparison.

## 2. The Gaussian prime and SUCC's genuine eight-step return

Let \(\lambda=1+i\) in \(\mathbb Z[i]\). Exactly,

$$
2=-i\lambda^2,\quad \lambda^4=-4,\quad \boxed{\lambda^8=16}.
$$

The two-atom BBP construction in [#308](https://github.com/femboy2112/SUCC/pull/308) has a rotating transfer matrix \(G=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}\), multiplication by \(g=(1+i)/2=i/\lambda\), so \(G^4=-I/4\), \(G^8=I/16\). This is an exact ramified-prime account of its intermediate sign and eighth return, *not* a new selected π phase cancellation.

The three classical Gaussian prime behaviors occur among the first three rational primes:

| p | In \(\mathbb Z[i]\) | Finite structural interface |
|---|---|---|
| 2 | ramifies: \((2)=(1+i)^2\) up to unit | mod-2 nonzero nilpotent \(\epsilon=1+i,\ \epsilon^2=0\) |
| 3 | inert | \(\mathbb F_9\), one conjugate Frobenius pair |
| 5 | splits as \((2+i)(2-i)\) | \(\mathbb F_5\times\mathbb F_5\) |
| 7 | inert, a distinct holdout | \(\mathbb F_{49}\), first clean BBP reduction |

For rational inputs \(n\), the two split mod-5 Gaussian images are diagonal \((n,n)\); extra Gaussian channels do *not* mean new independent source observations without an authenticated complex lift. The Gaussian filtration \((\lambda^{8k})=(16^k)\) has \(2^{8k}\) full Gaussian residues, while the rational time-sector has \(2^{4k}\) residues.

## 3. Authentic Gaussian analytic source lift (PAPER PROOF; upstream zero imported)

Let \(R=\mathbb Z_2[i]\), \(\lambda=1+i\). Because each factor of \(D(z)\) has even slope and odd constant, \(D(z)\) is a \(\lambda\)-adic unit for every \(z\in R\); \(r(z)\) is therefore defined on this full integral Gaussian ring. Extend the actual source by

$$
\Psi(z)=\sum_{s\ge0}16^s r(z-s)=\sum_{s\ge0}\lambda^{8s}r(z-s),\qquad z\in R.
$$

The sum converges uniformly. For unequal \(z,w\), \((A(z)-A(w))/(z-w)=120(z+w)-89\) is a unit, whereas \((D(z)-D(w))/(z-w)\) is divisible by 2. The quotient difference \((r(z)-r(w))/(z-w)\) is thus a \(\lambda\)-unit. As \(\Psi-r\) is 16 times a 1-Lipschitz map,

$$
\boxed{v_\lambda(\Psi(z)-\Psi(w))=v_\lambda(z-w).}
$$

Every finite ring \(R/(\lambda^m)\) is permuted. Exact successor:

$$
\Psi(z+1)=16\Psi(z)+r(z+1).
$$

Inheriting the **nontrivial** source-specific \(\Phi(0)=0\) theorem from [#321](https://github.com/femboy2112/SUCC/pull/321) gives \(\Psi(0)=0\) and \(\Psi(n)=U_n\) for natural \(n\), embedded in \(R\). However natural \(n\mapsto n+1\) fills only the rational-time sector, **not the imaginary Gaussian fibers**. The enlarged source-compatible virtual space is not a real-circle mixing proof. Exact local Gaussian-modulus and rational-state comparisons were among the independently exercised focused tests.

## 4. The first nontrivial quadratic source-pair ramification is at 7

There are two exact identities:

$$
\boxed{A(x)-A(y)=(x-y)[120(x+y)-89]},
$$

$$
\boxed{(240x-89)^2=480A(x)+241}.
$$

Since \(120\) is divisible by 2,3,5 and 89 is coprime to them, **A is an isometric bijection modulo every \(2^a,3^b,5^c\)**. This extends [#322](https://github.com/femboy2112/SUCC/pull/322)'s exact CRT clock to

$$
n\mapsto (U_n\bmod16^k,\ A(n)\bmod3^L,\ A(n)\bmod5^J),
$$

a bijection on every full time block of \(16^k3^L5^J\), conditional on the inherited authentic #321 zero boundary. The 3,5 coordinates are cleared source numerators, **not p-adic U states**.

For every prime \(p\ge7\), the numerator has a second equal-value sheet

$$
\boxed{\iota_p(x)=89/120-x\bmod p},
$$

intersecting the diagonal only at \(x=89/240\bmod p\). Crucially, at prime powers \(p^L\), the constraint \(p^L\mid A(x)-A(y)\) has **mixed valuation strata**, not just two disjoint congruence sheets.

Because the affine map \((x,y)\mapsto(u,v)=(x-y,120(x+y)-89)\) has determinant \(240\), a unit at all \(p\ge7\), it is a bijection modulo \(p^L\). Count \(uv\equiv0\pmod{p^L}\): \(u=0\) supplies \(p^L\) solutions; each of the \(L\) valuation strata \(v_p(u)=a<L\) supplies \((p-1)p^{L-1}\). Thus the **exact all-level pair count** is

$$
\boxed{\#\{(x,y)\bmod p^L:A(x)\equiv A(y)\}
=p^L+L(p-1)p^{L-1},\qquad p\ge7.}
$$

At p=2,3,5 the count is only \(p^L\). The first new off-diagonal source pair sheet genuinely appears at p=7 (2p−1=13 pairs mod 7). Exact finite examples: p=7,L=2 yields 133; p=7,L=3 yields 1225; p=11,L=2 yields 341.

At 7 there is a further source-specific Gaussian **norm** identity:

$$
\boxed{A(x)\equiv(x+1)^2+1
=N_{\mathbb F_{49}/\mathbb F_7}((x+1)+i)\pmod7.}
$$

As −1 is nonsquare modulo 7, \(A\) has no zero there. The four source denominator poles are distinct \(4,2,0,3\) modulo 7, and the full signed \(D\) **breaks** the numerator mirror: \(\iota_7(0)=5\), \(D(0)\equiv0\) but \(D(5)\equiv2\). This asymmetry is a candidate **actual source selector**, rather than mere CRT reindexing.

The quadratic numerator discriminant is \(241\): at p=241 the two *numerator roots* meet. Since \(241=15^2+4^2\), it splits in \(\mathbb Z[i]\). It is not a source rational-map bad-reduction prime; numerator-root ramification and map reduction are different notions.

## 5. Exact ramified-pair Fourier energy and the real proof obligation

For the actual authentic \(z_n(h)=e^{2\pi ihU_n}\), define at \(q=p^L\)

$$
\mathcal C_{N,q}(h)=\frac q{N^2}\sum_{a\bmod q}
\left|\sum_{\substack{0\le n<N\\A(n)\equiv a\bmod q}}z_n(h)\right|^2.
$$

By Cauchy–Schwarz, \(\lvert\sum_{n<N}z_n(h)\rvert^2/N^2\le\mathcal C_{N,q}(h)\). A genuine source-specific proof \(\mathcal C_{N,q(N)}(h)\to0\) for every fixed \(h\ne0\), with a well-defined \(q(N)=o(N)\), would establish π base-16 normality. **No such estimate is proved.** It may be stronger than Weyl, so the newly identified off-diagonal structure must do work.

At a single prime p≥7, write \(Z_r=\sum_{n<N,n\equiv r\bmod p}z_n\), \(c=89/120\bmod p\), \(b=c/2\bmod p\). There is an EXACT signed decomposition:

$$
\boxed{\sum_{a\bmod p}\left|\sum_{r:A(r)=a}Z_r\right|^2
=\sum_r|Z_r|^2+\sum_rZ_r\overline{Z_{c-r}}-|Z_b|^2.}
$$

The middle term is a **source-labelled signed mirror correlation**. The complete expression is nonnegative, and coherent phases \(z_n=1\) retain order \(N^2\) energy. No independence, Gaussian random sampling, or automatic negative correlation has been assumed. For p-adic depth L>1, use the *valuation law* above, not an invalid mod-p two-sheet shortcut.

**Codex frontier:** can the authentic four-pole \(D\), Gaussian sign holonomy, original zero seed and source boundary yield a growing signed saving in that reflected off-diagonal term, absent in the #320 nonnormal fake, the future-selected changed seed \(-T_n\), and PR #324's q-grid counterfeit? Start p=7; use p=11 and the separate 241 branch as holdouts. **Claude audit:** independently rederive resultants, good-reduction qualifications, Gaussian local lift and native test/origin provenance. Do not merge without independent review. **π normality: OPEN.**

Classical background: [Gaussian primes](https://people.math.osu.edu/leibman.1/algebra/rings.pdf); [Silverman's arithmetic dynamics/good reduction notes](https://swc-math.github.io/aws/2010/2010SilvermanNotes.pdf).
