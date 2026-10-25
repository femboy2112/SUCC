# Vacuum-anchored parameter integrals and the authentic BBP moment resolvent

**Research date:** 2026-10-25. **Pinned baseline:** SUCC Coherent Main X, main@1e3a453e869992961bc2d7f3bb6f2f1ddab38854. **Branch:** research/vacuum-parameter-bbp-krylov-2026-10-25. **New-to-project synthesis of classical tools**, not a claim of independent mathematical priority. Original source contract: [π Gearbox Atlas](../../docs/PI_GEARBOX_ATLAS.md) and [π Frontier Contract](../../docs/PI_FRONTIER_CONTRACT.md). Prior EAB and CBF proofs/archives remain unchanged. **π normality and RH remain OPEN.**

## 1. Three zeroes and a declared vacuum gauge

The user's observation \(0=x-x=a\log(1)\) has three non-equivalent interpretations. An exact same-source subtraction is zero, but different cutoffs in two divergent terms can produce an arbitrary finite remainder. The positive real/principal logarithm maps multiplicative identity 1 to additive zero. For positive operators, \(\log I=0\). Neither formula alone selects a unique physical vacuum or makes a zero potential energy-minimizing. A complex logarithm requires a branch.

There is a **genuinely adelic, exact all-places** version: for every nonzero \(q\in\mathbb Q\), with standard normalized local absolute values,

\[
\boxed{\prod_{v\leq\infty}|q|_v=1,\qquad
\sum_v\log|q|_v=0.}
\]

Proof: write \(q=\pm\prod_p p^{\nu_p(q)}\). At infinity, \(|q|_\infty=\prod p^{\nu_p(q)}\); at finite place \(p\), \(|q|_p=p^{-\nu_p(q)}\); all but finitely many valuations vanish. At finite prime cutoff \(X\), the exact **unresolved-place correction** is \(-\sum_{p>X}\log |q|_p\). For \(q=12\), infinity contributes 12, the \(p=2\) place 1/4, and the \(p=3\) place 1/3: partial product through 2 is 3, full product is 1. A one-place idèle with coordinate 2 only at \(p=2\) has norm 1/2 instead: diagonal source is a substantive hypothesis. This is the classical product formula, not thermodynamic energy conservation. See Warwick Tate study notes, Proposition 2.11: https://warwick.ac.uk/fac/sci/maths/people/staff/sheth/tate/tateweek5.pdf.

## 2. Why parameterizing an integral really is operator algebra

For real \(a>-1\), the parameter trick with its vacuum anchor is

\[
F(a)=\int_0^1\frac{t^a-1}{\log t}\,dt,\quad
F'(a)=\int_0^1t^a\,dt=\frac1{1+a},\quad
F(0)=0,
\]

so

\[
\boxed{F(a)=\log(1+a).}
\]

For finite self-adjoint \(A\) with spectrum \(>-1\), functional calculus applies scalar integration in each eigenchannel:

\[
\boxed{\int_0^1\frac{t^A-I}{\log t}\,dt=\log(I+A),\qquad
\int_0^1t^A\,dt=(I+A)^{-1}.}
\]

This is exactly **matrix-element integration in a shared spectral basis**. For rank-one perturbations of positive definite \(A\),

\[
\frac{\det(A+\lambda uu^*)}{\det A}
=1+\lambda\,u^*A^{-1}u,
\]

and integrating the parameter-dependent resolvent matrix element gives

\[
\boxed{\int_0^\lambda u^*(A+tuu^*)^{-1}u\,dt
=\log(1+\lambda u^*A^{-1}u).}
\]

No arbitrary integration constant survives the declared \(\lambda=0\) vacuum reference. However, for a **noncommuting** matrix perturbation, \(D\log A[H]\) is the **double-resolvent integral** \(\int_0^\infty(A+tI)^{-1}H(A+tI)^{-1}dt\); the matrix identity \(D\log A[H]=A^{-1}H\) is false in general. The scalar trace identity \(d\log\det A=\operatorname{Tr}(A^{-1}dA)\) survives. A hostile counterexample is \(A=\operatorname{diag}(2,3)\) and off-diagonal symmetric \(H\): \(A^{-1}H\) is nonsymmetric, whereas the derivative of the symmetric matrix logarithm must be symmetric.

Classical precedents: NIST DLMF §§4.7,4.10; Kim–Cho–Lee, *The art of Schwinger and Feynman parametrizations* (2023), https://link.springer.com/article/10.1007/s40042-023-00764-3.

## 3. Exact positive vacuum factor hidden in the authentic four-pole π source

**Source passport:** SUCC Gearbox's one external clock, \(U_0=0\), \(U_{n+1}=16U_n+r(n+1)\), and \(\pi/16=\lim U_n/16^n\). Its four signed pole coefficients are retained literally:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Integrate each reciprocal using \(\int_0^1t^{k-1}dt=1/k\), to obtain the exact polynomial factorization

\[
\boxed{r(n)=\int_0^1 t^{8n-8}P(t)\,dt,\qquad
P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2).}
\]

For \(0\le t<1\), \(P(t)>0\), while \(P(1)=4-2-1-1=0\). This is the user's zero reference made operational: **the actual BBP signed forcing cancels at the continuum endpoint**. It is a boundary zero, not a physical vacuum state. Writing \(P(t)=(1-t)Q(t)\), \(Q=4+4t+4t^2+2t^3+t^4\), \(Q(1)=15\), gives by beta-integral comparison

\[
\frac{4}{(8n-7)(8n-6)}
\le r(n)\le
\frac{15}{(8n-7)(8n-6)},\qquad
\boxed{r(n)=\frac{15}{64n^2}+O(n^{-3}).}
\]

The factor \(1-t\) suppresses the \(1/n\) tail. This is an exact source law; a mutated coefficient generally destroys that cancellation.

## 4. Matrix elements, Hausdorff moments and strict Hankel positivity

Take \(\mathcal H=L^2([0,1],P(t)dt)\), the constant vector \(v(t)=1\), and the positive multiplication contraction \((Mf)(t)=t^8 f(t)\). For \(n\ge1\),

\[
\boxed{r(n)=\langle v,M^{n-1}v\rangle.}
\]

Consequently, all discrete forward differences are strictly alternating:

\[
\boxed{(-1)^k\Delta^kr(n)
=\int_0^1 t^{8n-8}(1-t^8)^kP(t)\,dt>0.}
\]

Every finite source Hankel matrix \(H_d=(r(i+j+1))_{i,j=0}^{d-1}\) is **positive definite**: for nonzero coefficient vector \(c\), its quadratic form is the integral of \(P(t)(\sum_i c_i t^{8i})^2\), strictly positive. This is a concrete Hausdorff moment system; classical moment theory says its **complete** moment tape determines its compactly supported positive measure, not that finitely many moments determine the actual arithmetic source. Continuous-parameter derivatives also insert powers of the positive generator \(-8\log t\) under the integral, proving \((-1)^k r^{(k)}(a)>0\) for real \(a>7/8\).

The source-selected generating function is the matrix-element resolvent

\[
\boxed{R(z)=\langle v,(I-zM)^{-1}v\rangle
=\int_0^1\frac{P(t)}{1-zt^8}dt
=\sum_{j=0}^\infty z^j r(j+1),\quad |z|<1.}
\]

The **original BBP equality** gives, without changing source time, signs, or initial state,

\[
\boxed{\pi=R(1/16).}
\]

For every integer \(N\ge1\), its actual source-selected circle orbit is

\[
16^{N-1}\pi=U_N+T_N,\quad
T_N=\sum_{j=1}^\infty16^{-j}r(N+j),
\]

with the exact finite correction

\[
\boxed{\frac{r(N+1)}{16}\le T_N\le\frac{r(N+1)}{15}.}
\]

This can certify finite digits when the whole rational enclosure stays inside one carry cell; it supplies no all-depth distance-to-boundary theorem or digit-frequency cancellation.

## 5. Source-authentic two-sided Krylov/Schur energy certificate

Fix \(0\le z<1\), \(A=I-zM\), so \((1-z)I\preceq A\preceq I\). Project onto the Krylov space \(K_d=\operatorname{span}\{v,Mv,\ldots,M^{d-1}v\}\). Let \(f_d\in K_d\) solve the Galerkin system

\[
G_{ij}c_j=b_i,\qquad
G_{ij}=m_{i+j}-z\,m_{i+j+1},\quad b_i=m_i,\quad
m_k=r(k+1).
\]

Positivity of the source Hankel form makes \(G\) positive definite. All entries, the linear solve, and the residual norm are exact **rational** numbers at \(z=1/16\). Put \(L_d=b^Tc\), \(e_d=v-Af_d\), \(E_d=\langle e_d,e_d\rangle\). By the Galerkin orthogonality \(\langle e_d,f_d\rangle=0\) and completing the quadratic form,

\[
\boxed{R(z)=L_d+\langle e_d,A^{-1}e_d\rangle,\qquad
L_d+E_d\le R(z)\le L_d+\frac{E_d}{1-z}.}
\]

This is a **literal exact decomposition into visible energy and a hidden but bounded correction**. The residual polynomial has degree at most \(d\), so \(E_d\) uses only \(m_0,\ldots,m_{2d}\), i.e. \(2d+1\) authentic source moments. For any \(d\), compare to the independent truncated Neumann trial \(g_d=\sum_{j=0}^{d-1}(zM)^jv\). Its residual is \(z^dM^dv\), so energy optimality proves the **all-depth** certificate

\[
\boxed{0\le R(z)-L_d\le\frac{z^{2d}m_{2d}}{1-z}.}
\]

For the π parameter this specializes to the explicit rigorous bound

\[
\boxed{0\le\pi-L_d(1/16)
\le\frac{16}{15}\,16^{-2d}r(2d+1)
\le\frac{16^{1-2d}}{(16d+1)(16d+2)}.}
\]

**Local exact proof instrument:** at dimension \(d=8\), **17 authentic rational moments** and exact Fraction Gauss elimination yield a narrow interval whose endpoints have the identical first 23 fractional hexadecimal digits:

**3.243F6A8885A308D313198A2**

The completed rational interval was compared against an **independent Machin arctangent alternating-series interval**, not π floating-point input. This is a finite π-value theorem; no frequency or normality result follows. Mathematical lineage: classical Gauss/Krylov/Lanczos Stieltjes integral inequalities, e.g. Golub–Meurant and https://doi.org/10.1016/j.cam.2021.113604.

## 6. Limit boundary: finite scalar, divergent operator

At \(z=1\), \(1-t^8=(1-t)(1+t+\cdots+t^7)\). The source zero cancels the denominator once, yielding the finite exterior observable

\[
R(1^-)=\int_0^1\frac{Q(t)}{1+t+\cdots+t^7}dt<\infty.
\]

Nevertheless the **operator inverse** is unbounded as \(z\uparrow1\), and \((I-M)^{-1}v\notin\mathcal H\): its squared norm would be \(\int P(t)/(1-t^8)^2dt=\infty\). The half-inverse vector \((I-M)^{-1/2}v\) **is** in \(\mathcal H\), with squared norm \(R(1^-)\). The two domain statements cannot be interchanged.

The exact endpoint Taylor structure \(P(t)=15(1-t)+O((1-t)^2)\), \(1-zt^8=(1-z)+8(1-t)+O((1-z)(1-t)+(1-t)^2)\) also gives

\[
\boxed{R'(z)=\frac{15}{64}\log\frac1{1-z}+O(1),\qquad z\uparrow1.}
\]

The exterior potential is finite while its **susceptibility** diverges logarithmically. This is a model of the user's graph-coarse-graining boundary idea, not a quantum vacuum or an RH theorem.

## 7. Graphs can become points while hidden determinant data survives

For an ungrounded connected graph with **one** visible port, its static Dirichlet-to-Neumann map is zero, independently of its interior. For the three-node path with weights \(a,b>0\), the grounded hidden block is

\[
D=\begin{pmatrix}a+b&-b\\-b&b\end{pmatrix},\qquad \det D=ab.
\]

Thus paths \((a,b)=(1,1)\) and \((2,3)\) have **identical one-port static response** but hidden determinants 1 and 6. Their relative log determinant is \(\log6\). A hidden Gaussian normalization can retain this constant with a separately specified measure; it is not automatically physical energy. It is precisely why discarded degrees of freedom should leave a boundary normalization and/or memory record.

## 8. Steelman, crucible, verdict

- **SURVIVES / exact classical source application:** π's genuine four-pole forcing has a positive kernel and endpoint zero; its moments are strictly completely monotone and admit a positive contraction resolvent; π is its matrix element; finite rational Krylov/Schur residuals give two-sided certified value bounds and a uniform all-depth rate; diagonal adeles obey the logarithmic product-formula vacuum.
- **REFUTED overclaim:** vacuum normalization, positive moment Grams, finite moment matching, or a finite π prefix implies π normality. A **non-authentic rank-one atomic measure** with weight \(47/15\) and point \(530/12831\) matches the first two authentic moments, yet has rational resolvent value \(1608152/511915\), whose hexadecimal expansion is eventually periodic and nonnormal. It differs already at the third moment. A complete source tape is not identified by two moments.
- **REFUTED algebraic shortcut:** \(D\log A[H]=A^{-1}H\) as a noncommutative matrix identity. Only the trace has the simple cyclic logarithmic derivative.
- **UNVERIFIED:** a certified all-depth, source-selected signed BBP phase/carry estimate (π Frontier Contract \(S_N(h)=o(N)\)); a source-derived completed signed Weil positivity factorization; source uniqueness from vacuum constants alone. RH and π normality are OPEN.

## 9. Reproducibility and decisive next probe

Files: observational_succ/vacuum_parameter_bbp.py, tests/test_vacuum_parameter_bbp.py, tests/test_vacuum_parameter_bbp_integration.py, scripts/vacuum_parameter_bbp_probe.py, and the numbered VPB claim supplement. Run the targeted tests plus the replay; then all mandatory AGENTS.md checks. **Local isolated Python 3.13.5: 24/24 exact unit tests passed**, including independently derived rational Machin holdouts. Original carrier integration tests are separate, requiring the full repository runtime/hosted CI.

**Verdict-changing next test:** couple this *positive unsigned moment measure* to the **authentic selected phase/carry state** of Coherent Main X, requiring exact source-labelled transport and a nontrivial signed bound on the highest-order four-bit Walsh interaction (Frontier Route C) or \(S_N(h)\) (Weyl). The positive resolvent provides authenticated value/regularity control, but it is not a substitute for signed long-range cancellation. No fake six, copied zero inputs, shifted BBP origins, or unproved limit exchange.


## 10. Source-specific finite Weyl-phase error transport (new second instrument)

Let \([l_d,u_d]\) be the exact rational π interval from Section 5, define the **rational midpoint** \(a_d=(l_d+u_d)/2\) and radius \(\rho_d=(u_d-l_d)/2\), and take any fixed integer \(h\ne0\). Let

\[
S_N(h,x)=\sum_{t=0}^{N-1}\exp(2\pi i h\,16^t x).
\]

Because \(|\exp(2\pi ix)-\exp(2\pi iy)|\le 2\pi|x-y|\le8|x-y|\) (classical \(\pi<4\)), the original selected π orbit and the rational proxy satisfy **for every** integer \(N\ge1,d\ge1\):

\[
\boxed{\frac{|S_N(h,\pi)-S_N(h,a_d)|}{N}
\le \frac{8|h|}{15N}(16^N-1)\rho_d.}
\]

The right-hand side is an **exact rational upper bound**, calculated by observational_succ/vacuum_phase_transport.py and tested without trigonometric floating point. By Section 5, \(\rho_d\le\frac{1}{2(1-1/16)}16^{-2d}r(2d+1)\) (a coarse but rigorous bound); hence **linear growth** of Krylov moment dimension in source-time horizon suffices to keep the normalized phase-*transport error* small. The implementation accepts finite horizons and reports its output with cancellation_proved=False.

**Important contrast:** direct transport from the older \(\gamma_2\) polynomial \(O(K^{-2})\) digit enclosures required an exponential number of additive cells to control large base-16 phase magnification. The new positive BBP resolvent has an *all-depth exponentially accurate* finite certificate. This is an **improved finite source-approximation pathway**, not a complexity theorem about rational bit lengths and **not** cancellation of \(S_N(h,a_d)\).

**Decisive countermodel:** for every fixed \(d\), \(a_d\) is rational; its hexadecimal orbit is eventually periodic, and bounding its *distance* to the true orbit does not make its signed Weyl sum small. One needs a uniform estimate for the **source-selected signed** arithmetic orbit, or a jointly controlled growing-\(d(N)\) approximation with a separately proved cancellation estimate. Thus the π Frontier Contract remains OPEN. There is no inference to RH or original signed Weil positivity.
