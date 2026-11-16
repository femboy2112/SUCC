# A reproducible SU(2) Wilson ingredient and the reflection/gap boundary

**Status:** elementary paper proofs plus finite exact rational witnesses.
**Scope:** a single compact-group plaquette, its normalized observable state,
and scalar reflection kernels. This is a reconstruction of reusable ingredients,
not a reproduction of the four-dimensional Yang–Mills continuum proof. No
novelty claim is made for Haar moments, positive-state limits or spectral theory.

Code: [`ym_reflection_bridge.py`](../../../observational_succ/ym_reflection_bridge.py).
Checks: [`test_ym_reflection_bridge.py`](../../../tests/test_ym_reflection_bridge.py).
Run from the repository root:

```sh
python -m unittest discover -s tests -p 'test_ym_reflection_bridge.py' -v
```

## 1. Bind the finite calculation to the actual Wilson source

The public construction uses plaquette holonomies and the action

\[
 S(U)=\sum_p\left(1-\frac{\operatorname{Re}\operatorname{Tr}U_p}{d}\right),
 \qquad d\mu_\beta=Z_\beta^{-1}e^{-\beta S(U)}\prod_e dU_e.
\]

This is the literal normalization in [`PublicWilson.lean`, `wilsonEnergy` and
`wilsonLaw`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean).
For one square plaquette with four independent Haar SU(2) links, its holonomy
is Haar SU(2): condition on three links and apply left/right invariance to the
fourth. Equivalently, fixing the three edges of a spanning tree leaves the
plaquette holonomy as the one free group variable. This does **not** assert
independence of plaquettes sharing links on a four-dimensional lattice.

Write a unit quaternion as \(U=xI+i\mathbf y\cdot\boldsymbol\sigma\), where
\(x^2+|\mathbf y|^2=1\). Normalized Haar measure is uniform measure on
\(S^3\); the scalar coordinate \(x=\operatorname{Tr}U/2\) has density

\[
 d\nu(x)=\frac2\pi\sqrt{1-x^2}\,dx,\qquad -1\le x\le1.
\]

The one-plaquette action is \(1-x\). Its constant factor \(e^{-\beta}\)
cancels from every normalized expectation, so the scalar state is

\[
 L_\beta(f)=\frac{\int_{-1}^1 f(x)e^{\beta x}\,d\nu(x)}
                  {\int_{-1}^1e^{\beta x}\,d\nu(x)}.
\]

This dictionary is exact for the declared one-plaquette restriction.

## 2. Exact moment certificate, by two routes

**WS-01 — CLASSICAL, re-derived.** For every integer \(k\ge0\),

\[
 \mu_{2k}:=\int x^{2k}\,d\nu
   =\frac{1}{4^k(k+1)}\binom{2k}{k},\qquad \mu_{2k+1}=0.
\]

Odd moments vanish by symmetry. Substitution \(u=x^2\) gives
\(\mu_{2k}=\frac2\pi B(k+\tfrac12,\tfrac32)\), yielding the stated
Catalan expression. There is a second elementary derivation that does not use
the Catalan formula. The endpoint terms vanish in

\[
 0=\int_{-1}^1\frac d{dx}\big[x^{n+1}(1-x^2)^{3/2}\big]\,dx,
\]

so \((n+1)(\mu_n-\mu_{n+2})=3\mu_{n+2}\), and hence

\[
 \mu_{n+2}=\frac{n+1}{n+4}\mu_n,
 \qquad\mu_0=1,\quad\mu_1=0.
\]

`haar_moment` implements Catalan arithmetic; `haar_moment_recurrence`
implements this integration-by-parts recurrence. Agreement is tested at
degrees 0–80 and fresh degrees 97, 100, 126, 181 and 200. The all-degree
statement is justified by the derivation, not by this finite list.

## 3. A positive exact approximation to the Wilson state

Let \(K\ge0\), \(\beta\in\mathbb Q\), and

\[
 P_{2K}(y)=\sum_{j=0}^{2K}\frac{y^j}{j!},\qquad
 L_{\beta,K}(f)=\frac{\int f(x)P_{2K}(\beta x)\,d\nu(x)}
                         {Z_{\beta,K}},\quad
 Z_{\beta,K}=\int P_{2K}(\beta x)\,d\nu(x).
\]

**WS-02 — PROVED LOCAL.** \(P_{2K}(y)>0\) for every real \(y\), and
\(L_{\beta,K}\) is a normalized positive state. For real rational
polynomials, all its values are exact rational numbers.

*Proof.* For \(y\ge0\), the constant term is 1 and all terms are nonnegative.
For \(y<0\), Taylor's theorem gives
\(e^y=P_{2K}(y)+e^\xi y^{2K+1}/(2K+1)!\) for a real \(\xi\) between
\(y\) and 0. The remainder is negative; thus \(P_{2K}(y)>e^y>0\).
Consequently \(Z_{\beta,K}>0\), \(L_{\beta,K}(1)=1\), and
\(L_{\beta,K}(\overline f f)\ge0\). Exact polynomial evaluation follows
from WS-01. The implementation evaluates real rational polynomials; the
paper positivity statement also covers complex polynomials. ∎

**WS-03 — PROVED LOCAL, explicit error bound.** For every bounded measurable
complex function \(f\) with \(|f|\le M\), set \(b=|\beta|\). Then

\[
 |L_\beta(f)-L_{\beta,K}(f)|
 \le 2M e^{2b}\frac{b^{2K+1}}{(2K+1)!}
 \le 2M\,3^{2\lceil b\rceil}\frac{b^{2K+1}}{(2K+1)!}.
\]

*Proof.* The uniform Taylor error on \([-b,b]\) is at most
\(\delta=e^b b^{2K+1}/(2K+1)!\). Denote the exact numerator and
partition by \(N,Z\), and their polynomial versions by \(N_K,Z_K\).
Then \(|N-N_K|\le M\delta\), \(|Z-Z_K|\le\delta\),
\(|N_K|\le MZ_K\) by WS-02, and \(Z\ge e^{-b}\). Therefore

\[
 \left|\frac N Z-\frac{N_K}{Z_K}\right|
 \le\frac{M\delta}{Z}
       +\frac{|N_K|}{Z_K}\frac{|Z-Z_K|}{Z}
 \le 2M e^b\delta.
\]

Finally \(e^b\le3^{\lceil b\rceil}\), including \(b=0\). For a
rational polynomial \(f=\sum c_jx^j\), a valid rational bound is
\(M=\sum|c_j|\). At fixed \(\beta,M\), the factorial tail tends to
zero. This is a proved limit of normalized states for this finite source.
It is not a lattice-spacing or infinite-volume limit. ∎

The exact check builds moment Gram matrices
\(G_{ij}=L_{\beta,K}(f_if_j)\) and checks positive semidefiniteness
by rational Schur complements. Singular matrices, zero observables and
duplicate observables are included. Positive matrix checks alone do not prove
WS-02; its pointwise positive-weight argument does.

### A mutation that must fail

**WS-04 — REFUTED shortcut, exact receipt.** Arbitrary Taylor truncation
does not preserve a positive observable state. The odd truncation at
\(\beta=3\) gives \(w(x)=1+3x\), whose partition is still 1. For
\(f(x)=1-x\),

\[
 \int f(x)^2w(x)\,d\nu(x)
 =1-5\mu_2=-\frac14.
\]

Its Gram matrix in the basis \((1,x)\) is
\(\begin{pmatrix}1&3/4\\3/4&1/4\end{pmatrix}\), with determinant
\(-5/16\). The positivity checker rejects it. Thus normalization and
formal resemblance to a Boltzmann weight do not pass this instrument.

## 4. Ordinary covariance and reflection positivity are different requirements

For a scalar translation-invariant kernel \(C\), ordinary covariance tests
\(C(t_i-t_j)\); time-reflection positivity tests \(C(t_i+t_j)\) for
\(t_i\ge0\). The latter corresponds to the reflected observable and
positive-time observable being paired on the **same** correlation hierarchy.

This distinction is used explicitly by the committee's
[`ReflectionPositivity.lean`](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/checks/ReflectionPositivity.lean):
compact reflected entries are identified with the chosen source state,
then support-preserving approximations extend positivity to the required
Schwartz/Borchers test functions. Our scalar checks do not reproduce that
mixed-arity support and continuity argument.

**WS-05 — REFUTED implication, exact receipt.** Let
\(C(t)=\cos(\pi t/2)\). For arbitrary complex coefficients,

\[
 \sum_{ij}\bar c_ic_j C(t_i-t_j)
 =\frac12\left|\sum_j c_je^{i\pi t_j/2}\right|^2
  +\frac12\left|\sum_j c_je^{-i\pi t_j/2}\right|^2\ge0.
\]

Nevertheless the reflected one-observable test at \(t_1=1\) equals
\(C(2)=-1\). Integer times give an exact rational counterexample with
no trigonometric approximation. Thus an SUCC Gram-positivity certificate
does not automatically supply Yang–Mills reflection positivity.

## 5. Reflection positivity and unique vacuum do not force a mass gap

**WS-06 — PROVED LOCAL countermodel.** The kernel

\[
 C(t)=\frac1{1+t}=\int_0^1x^t\,dx
      =\int_0^\infty e^{-tE}e^{-E}\,dE,\qquad t\ge0,
\]

is reflection positive because

\[
 \sum_{ij}\bar c_ic_j C(t_i+t_j)
 =\int_0^1\left|\sum_j c_jx^{t_j}\right|^2dx\ge0.
\]

It is a legitimate scalar quantum-mechanical spectral model with
\(\mathcal H=\mathbb C\Omega\oplus L^2((0,1),dx)\),
\(H=0\oplus M_{-\log x}\), and \(f=0\oplus1\).
The vacuum \(\Omega\) is the unique zero-energy vector up to scalar:
\(-\log x>0\) almost everywhere. The excited spectrum nevertheless
extends arbitrarily close to zero, so no positive mass gap exists. The
correlation is \(\langle f,e^{-tH}f\rangle=C(t)\). This is a scalar
spectral countermodel, not a four-dimensional Yang–Mills theory.

There is an exact finite gapped approximation. For \(N\ge1\), set

\[
 C_N(n)=\frac1N\sum_{j=1}^N\left(\frac j{N+1}\right)^n,
 \qquad n\in\mathbb N_0.
\]

Every reflected matrix is a finite sum of positive rank-one matrices.
Adjoin one vacuum to the \(N\) excited states. Their energies are
\(-\log(j/(N+1))\), so each finite model has a unique vacuum and gap
\(-\log(N/(N+1))>0\). For every fixed integer \(n\ge0\),

\[
 \left|C_N(n)-\frac1{n+1}\right|\le\frac1N.
\]

For \(n=0\), equality of the correlations is exact. For \(n>0\), use
left and right Riemann sums for the increasing function \(x^n\), with
mesh \(1/(N+1)\). The left sum is \(N C_N(n)/(N+1)\), and the
right-minus-left difference is \(1/(N+1)\). If
\(I=1/(n+1)\), this implies
\((I-1)/N\le C_N(n)-I\le I/N\), proving the bound. Thus the
gapless limit retains the positivity and unique vacuum that the finite
approximants had; their nonuniform gaps are exactly what disappears.

### Physical units also matter

**WS-07 — PROVED LOCAL countermodel.** For rational lattice spacing
\(a>0\), take the transfer eigenvalue \(q_a=(1+a^2)^{-1}\).
Each lattice has a positive transfer gap, but its physical decay rate is

\[
 m_a=-\frac{\log q_a}{a}
     =\frac{\log(1+a^2)}a,
 \qquad\frac a{1+a^2}\le m_a\le a.
\]

The inequalities follow by integrating
\(1/(1+a^2)\le1/(1+s)\le1\) over \(0\le s\le a^2\).
Hence \(m_a\to0\), not a positive limit. At fixed physical time \(t\),

\[
 0\le1-q_a^{\lfloor t/a\rfloor}
 \le\lfloor t/a\rfloor(1-q_a)\le ta.
\]

The middle bound follows from the finite geometric sum. This gives exact
rational witnesses for gap collapse without numerically evaluating a logarithm.

## 6. The additional estimate that really would prove a gap

For a positive finite spectral measure \(\sigma\) on \([0,\infty)\),
write \(C(t)=\int e^{-tE}\,d\sigma(E)\). If a fixed \(m>0\) and
finite \(M\) obey \(C(t)\le Me^{-mt}\) for every \(t\ge0\), then
\(\sigma([0,m))=0\). Indeed, for each \(r<m\),

\[
 e^{-rt}\sigma([0,r])\le C(t)\le Me^{-mt},
\]

and letting \(t\to\infty\) forces \(\sigma([0,r])=0\).
Conversely support in \([m,\infty)\) gives the bound with
\(M=\sigma([0,\infty))\). For a theory-wide gap, this must control
a family whose linear span is dense in the vacuum-orthogonal subspace with
the **same** \(m\); the finite prefactor may depend on the vector. The
low-energy spectral projection then vanishes on a dense subspace and hence
everywhere by boundedness. A single observable could miss a slower sector. For
continuum passage, the lattice estimate needs uniform physical units and
control of the observed limits. These are substantive extra hypotheses.

## 7. Verdict and next discriminating probes

The reusable result is a **source-matched positive Wilson approximation with
a rigorous factorial error budget**. It can check SUCC's observable-state
interfaces and distinguish an actual compact-group density from a merely
positive-looking formal expression. The independent moment recurrence and
negative-square mutation calibrate that finite instrument.

The reflection and spectral controls expose two separate missing bridges:
ordinary Gram positivity to the exact reflected form, and positivity/existence
to a uniform spectral estimate. They do not refute any source-specific estimate
that could supply those bridges. No inference about BBP normality, RH,
Goldbach or the Yang–Mills mass gap is made by these finite checks.

The next constructive enlargement would be an exact compact-group or finite-group
multi-plaquette reflection calculation with shared edges and declared reflection
boundary, retaining the original Wilson weight. Independent one-plaquette
averages cannot stand in for that dependence. A continuum reproduction must
add the original construction's renormalization bounds and limit topology;
the small calculation here does not hide those obligations.
