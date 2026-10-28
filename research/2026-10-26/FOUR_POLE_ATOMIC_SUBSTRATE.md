# Four-pole BBP from quadratic atoms, a global mirror, and a graded golden–Gamma offset

**Date:** 2026-10-26. **Base:** draft PR #306 at
7989be5753341c5e74d570e8fea51e00129d2d0a. This continues the
[logarithmic source bridge](OILY_MACARONI_SOURCE_BRIDGE.md) in response to the
author's request to find a more elementary structure beneath the eight-step BBP presentation.

**Verdict:** explicit source-preserving constructions and paper proofs below. The coefficient
compiler has two rational quadratic atoms and a minimal common scalar return of eight.
A positive binary polynomial compiler has a sharp uniform relative defect. Its specified
endpoint layer law produces a golden fixed point and an exact Euler–Mascheroni offset.
That offset depends on the retained layer decomposition. **Selected Weyl cancellation,
base-16 normality of pi, and RH remain OPEN.**

## 1. Provenance and the precise research cut

The reduced quartic, the log/arctangent primitive, the endpoint Pell hierarchy, and the
infinite Hankel rank of the integrated tail were already proved in
[PI_SOURCE_GENESIS_GREEN.md](../2026-10-24/PI_SOURCE_GENESIS_GREEN.md), G1–G6.
The signed logarithmic control and positive rational-integral control were already in
[PI_SOURCE_GENESIS_NONCOBOUNDARY.md](../2026-10-24/PI_SOURCE_GENESIS_NONCOBOUNDARY.md).
They are reused here, with their variables and scopes preserved.

The original [Bailey–Borwein–Plouffe paper](https://www.davidhbailey.com/dhbpapers/digits.pdf),
Theorem 1, already obtains the formula through a rational integral and partial fractions.
The original proof and Bailey's
[compendium](https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf) also record other
block presentations. No scholarly priority for the elementary identities or this
derived interface is asserted.

The additional work is an explicit rational state realization, a signed projective
interpretation of its clock, a global finite compiler with sharp source-relative error,
and an exact account of what the proposed golden–Gamma offset does and does not retain.
The fact that eight is composite is not itself an argument. The factorization and
return-time proof determine the answer in the declared linear model.

| Object or assertion | Status and scope |
|---|---|
| Reduced quartic and global primitive | INHERITED, classical/paper |
| Two quadratic coefficient atoms; minimal dimension four | PROVED PAPER; exact rational certificates; monomial-degree index only |
| Eight is their least common scalar clock | PROVED PAPER; relative sign survives projectivization |
| Global positive polynomial compiler and sharp relative defect | PROVED PAPER for all source times; finite exact calibration |
| Minimal endpoint PGF fixed point equals inverse-phi squared | PROVED PAPER for the specified geometric layer law |
| Oily-macaroni offset is invariant under exact source-preserving regrouping | REFUTED by explicit controls |
| Gamma–Poisson representation is the authentic source joint law | REFUTED by mixed moment 4 versus 6 |
| Any of these constructions gives selected arithmetic cancellation | OPEN; hostile controls and precision quantifiers retained |

## 2. Four poles arise from two quadratic atoms

Use the unchanged source
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad n\ge1.
\]
Set, for \(0\le x\le1\),
\[
P(x)=4-2x^3-x^4-x^5,\quad
A(x)=2-x^2,\quad B(x)=x^2-2x+2.
\]
Exact factorization gives
\[
P(x)=(1-x)(x^2+2)(x^2+2x+2),
\]
\[
16-x^8=(2-x^2)(x^2+2)(x^2-2x+2)(x^2+2x+2).
\]
Consequently the positive tail kernel is
\[
\boxed{R(x)=\frac{P(x)}{16-x^8}
=\frac{1-x}{A(x)B(x)}
=\frac{1-x}{4-4x+2x^3-x^4}.}
\]
The full degree-eight denominator includes factors canceled by the authentic output.
The surviving denominator has two irreducible quadratic factors over the rationals.

To distinguish matrices from the scalar polynomials, call the rational atom matrices
\[
C=\begin{pmatrix}0&1/2\\1&0\end{pmatrix},\qquad
D=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad M=C\oplus D,
\]
and take
\[
v=(1,0,1,0)^T,\qquad w=(0,-1/8,1/4,0).
\]
Then
\[
\boxed{R(x)=w(I-xM)^{-1}v.}
\]
Indeed, the two block resolvents give exactly
\[
R(x)=-\frac{x}{4(2-x^2)}
+\frac{2-x}{4(x^2-2x+2)}.
\]
Thus the Taylor coefficients \(c_m=[x^m]R(x)\) are
\[
c_m=wM^mv.
\]
They begin
\[
(c_0,\ldots,c_7)=
\left(\frac14,0,0,-\frac18,-\frac1{16},-\frac1{16},0,0\right)
\]
and satisfy
\[
c_m=c_{m-1}-\frac12c_{m-3}+\frac14c_{m-4}\quad(m\ge4).
\]

### Minimality within the declared model

The coefficient Hankel determinant is
\[
\det(c_{i+j})_{0\le i,j<4}=\frac1{16384}\ne0.
\]
A scalar output of a constant matrix of dimension \(d\) has all such Hankel ranks
at most \(d\). Hence four states are necessary and sufficient for an autonomous linear
realization of this coefficient sequence. Equivalently, its reduced denominator has
degree four and is coprime to \(1-x\), since the denominator equals one at \(x=1\).

This is not a lower bound for arbitrary nonlinear encodings. It does not make the
arithmetic-time sequence \(T_n\) four-dimensional. The inherited moment theorem proves
that \(T_n\) has strictly positive Hankel matrices of every size, hence infinite rank.
The integration/observation step below is essential.

The rational algebra generated by the atoms is
\[
\mathbb Q[M]\simeq\mathbb Q(\sqrt2)\times\mathbb Q(i).
\]
Over the reals the first block splits into two scalar channels; over the complex numbers
all four channels split. The complete transfer still has four distinct poles.

## 3. The signed triangle extension explains the eight-step return

The atom identities are
\[
C^2=\frac12I,\qquad D^4=-\frac14I,
\]
so
\[
\boxed{M^4=\frac14(I_2\oplus-I_2),\qquad M^8=\frac1{16}I_4.}
\]
The eigenvalue ratio between \((1+i)/2\) and \(1/\sqrt2\) is a primitive eighth root
of unity. A common scalar power must raise every eigenvalue ratio to one, so its
exponent must be divisible by eight. Eight is therefore the least common scalar return.
This remains true after a change of basis, field extension, or nonzero common scalar rescaling.

On the real projective slope \(z=a/b\), the second atom acts as
\[
z\longmapsto\frac{z-1}{z+1},
\]
with the exact marked-point cycle
\[
\boxed{0\longrightarrow-1\longrightarrow\infty
\longrightarrow1\longrightarrow0.}
\]
Its square acts as \(z\mapsto-1/z\). The first atom acts as \(z\mapsto1/(2z)\).
These are actual maps supplied by the source realization.

The four-step projective cycle forgets the sign in \(D^4=-I/4\). The other atom
has \(C^4=+I/4\). Their relative sign is visible to the output \(w\), so replacing
both by one unsigned four-step return would change the source. This gives a precise
role to the signed extension of the author's \(0/1/\infty\) picture.
On the real projective line, positive and negative infinity are the same point;
a two-ended real chart would require additional one-sided boundary data.

There is also an exact positive metric
\[
G=\operatorname{diag}(2,1,1,1),\qquad M^TGM=G/2.
\]
This contracts the coefficient state at each elementary step. The arithmetic
accumulator expands by sixteen per macrostep. A contraction of the former is not
an estimate on the Fourier coherence of the latter.

### The endpoint chart produces the inherited Pell component

Writing \(x=1+s\) replaces the state transition in the resolvent by \(M(I-M)^{-1}\).
Its blocks are
\[
C'=\begin{pmatrix}1&1\\2&1\end{pmatrix},\qquad
D'=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Thus \((C')^2=2C'+I\) and \((D')^2=-I\). In particular, for
\(h(x)=R(x)/(1-x)\),
\[
h(1+s)=\frac1{(1-2s-s^2)(1+s^2)}
=\frac1{1-2s-2s^3-s^4}.
\]
This recovers the existing Pell hierarchy from the same atoms. The golden fixed point
will enter later through a different, nonlinear generating-function operation.

## 4. Harmonic observation compiles the authentic BBP source

The source and Green tail are recovered without pi digits as input:
\[
\boxed{r(n)=16\sum_{m=0}^7\frac{c_m}{8(n-1)+m+1},}
\]
\[
\boxed{T_n=\int_0^1x^{8n}R(x)\,dx
=\sum_{m\ge0}\frac{c_m}{8n+m+1}.}
\]
The first identity is finite monomial integration. The second follows from absolute
convergence of the coefficient series on the source interval. The scalar-return relation
gives \(c_{m+8}=c_m/16\), reconstructing exactly the original base-sixteen blocks.

After \(D_0\ge1\) complete blocks, the omitted tail is exactly
\[
16^{-D_0}T_{n+D_0}.
\]
Since \(0\le R(x)\le1-x\), it is strictly bounded by
\[
\boxed{\frac{16^{-D_0}}
{(8(n+D_0)+1)(8(n+D_0)+2)}}.
\]
The finite coefficient integral is checked against the original four-pole discounted
prefix in the implementation. At \(n=0\), this certifies \(T_0=\pi/16\).

The step \(c_m\mapsto c_m/(8n+m+1)\) introduces an unbounded harmonic observation clock.
The rational coefficient generator and the integrated arithmetic-time dynamics must
therefore remain separate typed objects.

## 5. A global Möbius mirror and its weighted logarithmic defect

The inherited primitive can be written without an inserted additive pi constant:
\[
\boxed{16\int_0^xR(t)\,dt
=2\log\frac{A(x)}{B(x)}
+4\arctan\frac{x}{2-x}.}
\]
At \(x=1\), the logarithmic boundary vanishes and the angle is \(\pi/4\).
Define \(L(x)=\log[A(x)/B(x)]\); then
\[
16R=2L'+4/B,\qquad L(0)=L(1)=0.
\]

A source-derived reciprocal mirror is
\[
J(x)=\frac{2(1-x)}{2-x},\qquad
\begin{pmatrix}-2&2\\-1&2\end{pmatrix}^2=2I.
\]
It exchanges zero and one and has fixed point \(2-\sqrt2\) in the interval.
Direct substitution proves
\[
A(Jx)=\frac{2A(x)}{(2-x)^2},\quad
B(Jx)=\frac{2B(x)}{(2-x)^2},\quad L(Jx)=L(x).
\]
The measure \(dx/B(x)\) is invariant under this orientation-reversing map, and
\[
\boxed{R(x)+|J'(x)|R(Jx)=\frac1{2B(x)},}
\]
\[
R(x)-|J'(x)|R(Jx)=\frac14L'(x).
\]
In the angle coordinate \(\theta=\arctan(1-x)\), the map is
\(\theta\mapsto\pi/4-\theta\). The sum of the two reflected angular densities is
constant. Their normalized pair average is exactly uniform angle on \([0,\pi/4]\).

The antisymmetric term matters for weighted observations. For every \(f\in C^1[0,1]\),
integration by parts gives
\[
\boxed{\int_0^1 fR
=\frac14\int_0^1\frac fB-\frac18\int_0^1 f'L.}
\]
For \(m=8n>0\),
\[
T_n=\frac14\int_0^1\frac{x^m}{B(x)}\,dx
-\frac m8\int_0^1x^{m-1}L(x)\,dx.
\]
The two terms have first-order size \(1/n\); their difference has size \(1/n^2\).
The log boundary's cancellation for a constant test cannot be reused after changing
the test to \(x^{8n}\).

Equivalently the backward primitive
\[
H(x)=\frac14\arctan(1-x)-\frac18L(x)
\]
has \(H'=-R\), \(H(1)=0\), and \(H(1-y)\sim y^2/2\).
Its quadratic zero is another exact explanation of the shape-two boundary law.

## 6. Positive binary layers give finite global shapes with a sharp defect

Set
\[
u(x)=x-\frac{x^2}{2},\qquad v(x)=\frac{x^2}{2},
\qquad 0\le v(x)\le u(x)\le\frac12.
\]
The factorization is now
\[
R(x)=\frac{1-x}{4(1-u)(1-v)}.
\]
This gives a positive polynomial expansion
\[
\boxed{R=\sum_{j\ge0}p_j,\qquad
p_j(x)=\frac{1-x}{4}\sum_{k=0}^j u(x)^k v(x)^{j-k}.}
\]
Equivalently,
\[
p_j(x)=\frac{(2-x)u(x)^j-xv(x)^j}{8}.
\]
Each finite layer is rational, nonnegative on the whole interval, and retains the
endpoint zero. The exact two-variable geometric construction supplies a declared
virtual-path carrier: two successive loop stages with counts \(K_1,K_2\ge0\).
Conditioned on \(x\), their normalized weights are
\[
\Pr_x(K_1=k,K_2=\ell)=(1-u)(1-v)u^kv^\ell.
\]
The layer label is their total \(j=k+\ell\). This counts two staged loops, not all
possible interleavings of two letter types. At a finite source time, the source coordinate
itself has law proportional to \(x^{8n}R(x)\,dx\). Both the path carrier and its weights
are explicit; no random choice of the actual arithmetic orbit is thereby assumed.

Let \(R_M=\sum_{j=0}^{M-1}p_j\), and write
\[
\rho_M=\frac{M+2}{2^{M+1}}.
\]
Here \(\rho_M\) is a finite compiler error, distinct from the oily-macaroni offset.

**Theorem.** For every integer \(M\ge1\), on the entire interval,
\[
\boxed{0\le R-R_M\le\rho_M R.}
\]
The coefficient \(\rho_M\) is sharp as \(x\uparrow1\).

One direct proof starts from the exact remainder
\[
R-R_M=u^M R+\frac{x(u^M-v^M)}{8(1-v)}.
\]
After division by \(R\) away from \(x=1\), its value is
\[
u^M+\frac{x^2B(x)}4
\sum_{\ell=0}^{M-1}u^{M-1-\ell}v^\ell.
\]
Use \(u,v\le1/2\) and \(x^2B(x)\le1\). The latter follows since
\[
1-x^2B(x)=(1-x)(x^3-x^2+x+1)\ge0.
\]
This gives \(2^{-M}+M2^{-M-1}=\rho_M\), with equality in the limit at the endpoint.
Equivalently, two geometric counts with parameters at most one half are stochastically
bounded by two fair geometric counts. This second proof explains the probability
meaning of the error.

For all \(n\ge0\), define the exact rational moment
\[
T_{n,M}=\int_0^1x^{8n}R_M(x)\,dx.
\]
Positivity immediately gives the simultaneous enclosure
\[
\boxed{T_{n,M}\le T_n\le\frac{T_{n,M}}{1-\rho_M}.}
\]
Every layer moment is a finite rational expression:
\[
\int_0^1x^mp_j(x)\,dx
=\frac18\left[
\sum_{\ell=0}^j {j\choose\ell}\left(-\frac12\right)^\ell
\left(\frac2{m+j+\ell+1}-\frac1{m+j+\ell+2}\right)
-\frac{2^{-j}}{m+2j+2}
\right].
\]
For example,
\[
R_1=(1-x)/4,\quad T_{0,1}=1/8;\qquad
R_2=(1-x^2)/4,\quad T_{0,2}=1/6;\qquad T_{0,4}=4/21.
\]
These finite shapes approximate the complete BBP source with a declared error; they
are not silently identified with the exact original four-pole forcing.

## 7. The finite realization and its precision schedule

Define
\[
r_M(n)=16T_{n-1,M}-T_{n,M},\qquad
U_{n,M}=16^nT_{0,M}-T_{n,M}.
\]
The zero anchor and recurrence hold exactly. Applying the pointwise relative theorem
to the nonnegative weights \(x^{8(n-1)}(16-x^8)\) and \(16^n-x^{8n}\) gives
\[
(1-\rho_M)r(n)\le r_M(n)\le r(n),
\]
\[
0\le U_n-U_{n,M}\le\rho_M U_n.
\]
Every fixed \(M\) has rational \(T_{0,M}=p/q\), and \(T_{n,M}\to0\). Therefore
\[
e(qU_{n,M})=e(-qT_{n,M})\longrightarrow1,
\qquad e(t)=\exp(2\pi it).
\]
**Every fixed-depth realization is nonnormal.** The obstruction frequency depends on
the depth. This does not establish anything adverse about the limiting authentic
source or a depth that grows with the observation horizon.

For a common depth \(M\) over horizon \(N\), the signed transport error obeys
\[
\boxed{\left|\frac1N\sum_{n=1}^N
[e(hU_n)-e(hU_{n,M})]\right|
\le\frac{28|h|\rho_M(16^N-1)}{15N}.}
\]
Proof: use \(2\pi<7\), \(T_0<1/4\), \(U_n\le16^nT_0\), and sum the geometric series.
The bound \(T_0<1/4\) follows directly from
\(A(x)B(x)-4(1-x)=x^3(2-x)\ge0\), hence \(R(x)\le1/4\).

Thus \(\rho_M16^N/N\to0\) is sufficient for transport of normalized means.
The stronger condition \(\rho_M16^N\to0\) controls every individual phase through
the horizon. For example,
\[
M_N=4N+2\lceil\log_2(N+2)\rceil
\]
gives \(\rho_{M_N}16^N=O(1/N)\). These are sufficient schedules, not lower bounds
on every possible approximation method. They control approximation error; signed
cancellation along this growing-depth sequence remains an additional theorem.

## 8. The declared binary layers generate the golden–Gamma offset

The endpoint derivative of each layer is
\[
\boxed{w_j=-p_j'(1)=\frac{j+1}{2^{j+2}},\qquad \sum_{j\ge0}w_j=1.}
\]
It is the law of the sum of two geometric counts with parameter one half. The
finite compiler error is exactly its tail:
\[
\rho_M=\sum_{j\ge M}w_j.
\]
Its generating function is
\[
\boxed{G(z)=\sum_{j\ge0}w_jz^j=\frac1{(2-z)^2}.}
\]
The minimal fixed point of this map in \([0,1]\) is selected by the finite recursion
\[
q_0=0,\qquad q_{s+1}=G(q_s).
\]
Since
\[
q(2-q)^2-1=(q-1)(q^2-3q+1),
\]
the limit is
\[
\boxed{q_*=\frac{3-\sqrt5}{2}=\lambda^2,\qquad
1-q_*=\lambda,\quad \lambda=\varphi^{-1}.}
\]
The other fixed point in the probability interval is one. The larger algebraic root
\(\varphi^2\) belongs to the rational continuation, outside the PGF convergence disk.

This construction needs no branching-process assumption. An extinction interpretation
would require a separately declared independent-offspring model.
For finite rational certificates, iterate both endpoints of \([0,2/5]\). The interval
is invariant and
\[
0<G'(z)\le125/256<1/2.
\]
Thus the two rational iterates bracket \(q_*\), with width at most
\((2/5)(125/256)^s\).

For \(n\ge1\), the source-normalized endpoint coordinate \(Y_n=-8n\log X\), where
\(X\) has density \(x^{8n}R(x)/T_n\), tends to \(Y\) with density \(ye^{-y}\).
This is precisely the Gamma-shape-two variable from the earlier source bridge. Its
Laplace transform and log mean are
\[
L_2(s)=\frac1{(1+s)^2},\qquad \mathbb E\log Y=1-\gamma.
\]
The same source layer law satisfies the exact transform identity
\[
\boxed{G(z)=L_2(1-z).}
\]
Consequently
\[
\boxed{\mathbb E\log Y-q_*=(1-\gamma)-\lambda^2=\lambda-\gamma.}
\]
For the authentic finite source law, the earlier exact formula becomes
\[
\boxed{\mathbb E\log Y_n-q_*=(\lambda-\gamma)-\eta_n.}
\]
Using a finite rational iterate \(q_s\), this gives the quantitative bound
\[
\left|\mathbb E\log Y_n-q_s-(\lambda-\gamma)\right|
\le\frac7{16n}+\frac25\left(\frac{125}{256}\right)^s.
\]
Together with the established limits, for fixed \(k\in\mathbb Z\setminus\{0\}\),
\[
\frac{T_n}{\eta_n^2}\to\frac4{49},\qquad
\frac{\Theta_n(k)}{\eta_n}\to-1-\frac{i}{7\pi k},
\]
this gives an explicit construction connecting the specified binary layer fixed point,
the Gamma logarithmic mean, the shrinking arithmetic tail, and the auxiliary
normalized-circle coherence. The constant was not supplied to the layer recursion.

The equation here is \(L_2(1-q)=q\). It is different from the direct Gamma-2 Laplace
fixed-point equation \(L_2(q)=q\), which gives \(q(1+q)^2=1\).

## 9. Two exact tests limit the offset's invariance and probabilistic interpretation

### Source-preserving regrouping changes the fixed point

Pair adjacent layers: \(\widetilde p_j=p_{2j}+p_{2j+1}\).
The kernel is unchanged and \(\widetilde R_M=R_{2M}\), but
\[
\widetilde w_j=\frac{3j+2}{4^{j+1}},\qquad
\widetilde G(z)=\frac{8+z}{(4-z)^2}.
\]
Its only fixed point in \([0,1]\) is one; indeed
\[
\widetilde G(z)-z
=\frac{(1-z)(z^2-7z+8)}{(4-z)^2}>0\quad(0\le z<1).
\]

An even smaller perturbation changes only the first two layers:
\[
\widehat p_0=p_0/2,\qquad
\widehat p_1=p_1+p_0/2,\qquad \widehat p_j=p_j\quad(j\ge2).
\]
All layers remain positive, and every approximant of depth at least two is identical.
Nevertheless
\[
\widehat G(z)=G(z)+(z-1)/8
\]
has minimal fixed point
\[
\widehat q_*=\frac{10-6\sqrt2}{7}\ne\lambda^2.
\]
Thus the offset is selected by the **specified geometric layer law**, not by the
ungraded source kernel or even by all sufficiently deep finite approximants alone.
If it is to be part of a categorical invariant, the preserved structure must include
that law and its grading. No representation-independent cancellation role has been proved.

### A Gamma–Poisson identity does not authenticate a joint law

The identity
\[
\int_0^\infty
\frac{e^{-y}y^j}{j!}\,ye^{-y}\,dy
=\frac{j+1}{2^{j+2}}
\]
provides a valid auxiliary coupling \(J\mid Y\sim\operatorname{Poisson}(Y)\).
It explains \(G(z)=L_2(1-z)\) at the level of marginal transforms.

The natural source joint law is instead
\[
\Pr_n(J=j,X\in dx)=\frac{x^{8n}p_j(x)}{T_n}\,dx.
\]
Under \(Y_n=-8n\log X\), its joint density tends to
\[
w_j\,ye^{-y}.
\]
Indeed \(p_j(x)/(1-x)\le w_j\), \(a(1-e^{-y/a})\le y\), and \(a^2T_n\to1\)
give an integrable summable dominator. Dominated convergence proves convergence in
total variation. The limiting \(J\) and \(Y\) are independent.
Their mixed moment is \(2\cdot2=4\), whereas the Gamma–Poisson coupling gives
\(\mathbb E[JY]=\mathbb E[Y^2]=6\). The scalar offset identity survives; a conditional
branching or arithmetic-correlation mechanism cannot be imported through it.

## 10. The atoms also retain exact hostile output controls

The complete output and initial selector remain necessary.
For rational \(\varepsilon>0\), the proper kernel
\[
R_\varepsilon=R+\varepsilon\frac{(1-x)^2}{A(x)B(x)}
\]
uses the same two atoms and has all four poles, the same full coefficient clock,
positivity, and the same leading \(1/(64n^2)\) tail.
Its output row is
\[
w_\varepsilon=
(\varepsilon/4,-(1+\varepsilon)/8,1/4,-\varepsilon/4).
\]
Yet
\[
16\int_0^1R_\varepsilon
=(1-\varepsilon)\pi+4\sqrt2\,\varepsilon\log(1+\sqrt2)>\pi.
\]
This refutes selection of the pi boundary from the pole set and clock alone.
It is not a claim that this particular altered constant is nonnormal.

For a genuine nonnormal control, reuse the inherited
\[
L_0=\frac12L',\qquad W=(L_0+1)/4
=R+\frac{(1-x)^2}{4B(x)}.
\]
Then \(W>0\) on the open interval, \(W(1)=0\), \(W'(1)=-1\), and
\(\int_0^1W=1/4\). Its zero-seed orbit is nonnormal at frequency four.
It uses the same matrices with output \((0,-1/8,1/8,-1/8)\) and a declared constant
feedthrough \(1/4\). The coefficient clock holds from degree one; the feedthrough
changes the degree-zero seam. The signed proper control \(L_0\) retains the full
clock and integral zero, but loses positivity. These scopes are distinct.

The earlier two-atom and uniform-cell controls remain mandatory for the logarithmic
source-circle interface. A correct future proof must distinguish full source and
selector information, not only one of these partially preserved summaries.

## 11. Reproduction and the next dependency cut

The new production module is
[bbp_atomic_substrate.py](../../observational_succ/bbp_atomic_substrate.py), with
[nine focused tests](../../tests/test_bbp_atomic_substrate.py).
The independently written
[polynomial oracle](bbp_mirror_polynomial_independent.py) imports no production code;
its [saved output](bbp_mirror_polynomial_independent.json) records exact symbolic
identities, rational coefficients, all-n-bound calibrations, and rejected mutations.
The [substrate receipt](BBP_ATOMIC_SUBSTRATE_RECEIPT.json) adds the atomic clock,
minimality, fixed-point brackets, grouping controls, and explicit nonclaims.
Commands and actual outcomes are in [VALIDATION.md](VALIDATION.md).

The next mathematical obligation is a signed estimate that preserves the full atom
output, the harmonic observation clock, the zero selector, and the required depth
schedule. The proved auxiliary source-circle cancellation and the exact finite
compiler provide two concrete interfaces. Neither supplies that signed estimate.
The actual character still exponentiates a source expectation; the auxiliary laws
average other characters. The noncommutation identified in the first dossier remains.

An honest successful next step would be a source-specific transport identity with a
controlled residual, or a genuinely weaker signed lemma that passes the declared
countermodels. Replacing the original Weyl gate by the same gate in atom, layer,
or generating-function notation is an equivalent reformulation, not a proof.

The [combined next-round handoff](../../handoffs/FOUR_POLE_ATOMIC_NEXT_2026-10-26.md)
records these interfaces, required controls and the acceptance test for further work.
