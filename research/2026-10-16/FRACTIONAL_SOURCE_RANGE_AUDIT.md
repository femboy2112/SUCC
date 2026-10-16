# Actual-source adjoint, logarithmic domain, and fractional range audit

Operation Arithmetic Resonance, source-range lane, 2026-10-16.
Base `24d0f18a103fb2add32ee817fdfefb4ff401ed27`.
**Original four-low sign OPEN. RH NOT PROVED.**

**Review status:** the density result below is a **PRINCIPAL / INDEPENDENTLY
AUDITED CONDITIONAL PAPER PROOF**, conditional on the inherited whole-high
inequality. The principal reported acceptance after reading SR-01–06, including
the Carleman and endpoint-distribution argument. This records the reported
analytic audit; the worker's numerical tests do not constitute that audit.
No formal kernel proof is claimed.
The maximal-domain step is proved explicitly in SR-03. It is not inferred from
the existence of a Friedrichs extension or from form-core density alone.
Fractional membership beyond the inherited square-root range remains OPEN.

## Authority and source

Only the assigned new module, test, probe, this dossier and `source_range*`
receipts are owned. No archive, shared index, existing module, commit, or push
was changed by this lane. Concurrent workers' files are not this lane's evidence.
Required reading included `AGENTS.md`, `docs/METHOD.md`, the import manifest,
Round II principal, source, theorem, compactness and hostile-audit dossiers,
and the actual source/Legendre/derivative/shorting modules. Their hashes are
recorded by the probe.

The live source and its originating commit were checked:

- `observational_succ/source_weil_hierarchy.py` Git blob
  `0cc8510b71d178fc79e8d410a86d8b6014cf9178`;
- source commit `dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc`;
- SHA256 `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.

This PR85 lineage is distinct from the founding 72-entry import manifest.
The real Gamma, contact, both poles and actual prime-2 half-density are retained.
No nontrivial zeta-zero coordinates enter any construction. Fourier test
frequencies below are ordinary freely chosen frequencies, not zero data.

Primary sources consulted: [Suzuki, §§2.2–2.5 and 8](https://arxiv.org/html/2606.09096v3)
for the genuine kernel and its distributional interpretation;
[Chen–Weth, Theorem 3.1](https://arxiv.org/html/1710.03416) for comparison with
logarithmic form-core density; and
[Douglas, Theorem 1](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)
for the inherited square-root range framework. The new domain argument is
given below, not imported from a theorem with an unspecified domain. No claim
of academic novelty is made.

## Fixed domains and conventions

Let $I=(-a,a)$, $a=1/2$, and use complex inner products linear in the first
argument. Set $E_j=\mathcal P_j$, the polynomials of degree at most $j$,
as subspaces of $L^2(I)$. Write

\[
H=1^\perp,\quad PH=\operatorname{span}(P_1(2t),\ldots,P_4(2t)),
\quad QH=E_4^\perp,\quad M=E_3^\perp.
\]

Here $Q$, when acting on all of $L^2(I)$, means $1-\Pi_{E_4}$;
it restricts to the existing high projection on $H$. Let $E$ also denote
zero extension $L^2(I)\to L^2(\mathbb R)$, always without a subscript.

$G$ is the genuine mean-zero compression of convolution by $g$.
$Vu(t)=\int_{-a}^t u(s)\,ds$, $K_Q=(V|_{QH})^*(V|_{QH})$, and
$D=QGQ|_{QH}$. The only positivity hypothesis used for SR-04 is the inherited

\[
\langle Du,u\rangle\ge\kappa\|Vu\|_2^2\quad(u\in QH),
\qquad\kappa=20699/10^6>0. \tag{H}
\]

Its source-specific weighted-Bessel proof is in
`tate_weighted_bessel_four_schur.py` and its existing dossier. This lane
does **not** independently re-prove (H). It does not assume $G\ge0$.

Put $Tf(x)=\int_I g'(x-y)f(y)\,dy$. The inherited $g'\in L^1(-1,1)$
and $L^2(-1,1)$ make $T:L^2(I)\to L^2(I)$ bounded and Hilbert–Schmidt.
Define $R_Q=\Pi_M T|_{QH}$, $R_P=\Pi_M T|_{PH}$. These are everywhere
defined bounded operators, with no endpoint trace condition on their inputs.

## SR-01 — actual adjoint, conjugation, parity and endpoint terms

**PAPER DERIVED, actual source.** Since $g'$ is real and odd, Fubini gives

\[
(T^*f)(y)=\int_I\overline{g'(x-y)}f(x)\,dx=-Tf(y),
\qquad R_Q^*f=-QTf\quad(f\in M). \tag{1}
\]

Thus the **actual annihilator equation**, including its domain, is

\[
f\in L^2(I),\quad \int_I t^j f(t)\,dt=0\ (j=0,1,2,3),
\qquad Tf=p\in\mathcal P_4. \tag{2}
\]

There is no conjugation on $f$ inside (1); it appears in the inner product.
For a general complex kernel one must retain the conjugate on the kernel.
The tests include a complex weighted-adjoint mutant, in addition to real
symmetric matrices. For an annihilator, the four target pairings are

\[
\langle R_Px,f\rangle=\langle x,-PTf\rangle.
\]

Before proving injectivity below, merely knowing $Tf\in\mathcal P_4$
does not make these pairings zero. It would require $PTf=0$.

Reflection $Jf(t)=f(-t)$ anticommutes with $T$ and commutes with both
projections. Hence $R_Q$ and $R_Q^*$ reverse parity. Even annihilators
would have $Tf\in\operatorname{span}(t,t^3)$; odd ones would have
$Tf\in\operatorname{span}(1,t^2,t^4)$. Complex conjugation commutes
with all these real-source maps.

For $f\in H^1(I)$, direct integration by parts, with the **uncompressed**
convolution $G_{\rm raw}$, gives

\[
Tf=G_{\rm raw}f'+g(x+a)f(-a)-g(x-a)f(a). \tag{3}
\]

If additionally $f\in M\cap H^1_0(I)$, integration by parts in the moments
gives $f'\in QH$, and (3) implies $QTf=Df'$. Therefore (H) proves that
an annihilator in this strong domain is zero. **One may not assume that an
arbitrary annihilator lies in this domain.** Even $P_4(2t)\in M$ has
traces (1,1). The exact affine-exponential Gamma control detects the missing
boundary terms for this polynomial. It is a boundary countercontrol, not an
actual annihilator.

## SR-02 — the genuine Gamma multiplier and signed bounded remainder

Write $d_j=4j+1$, $\tau=\log2$, $w=\log2/\sqrt2$, and
$C=C_\infty=\gamma+\pi/2+3\log2+\log\pi$. The pinned source gives, for
$0<r\le1$,

\[
g'(r)=-4\sinh(r/2)+C/2+w\mathbf1_{r>\tau}
 -\operatorname{atanh}(e^{-r/2})-\arctan(e^{-r/2}).
\]

Each genuine Gamma rung is
$g_j(r)=-4(1-e^{-d_j|r|/2})/d_j^2$. Distributionally on the full line,

\[
-g_j''=\frac4{d_j}\delta_0-e^{-d_j|r|/2}.
\]

With unitary Fourier transform (so Plancherel has no extra constant), its
convolution multiplier is

\[
m_j(\xi)=\frac4{d_j}-\frac{d_j}{\xi^2+d_j^2/4}
=\frac{4\xi^2}{d_j(\xi^2+d_j^2/4)}\ge0,
\qquad m=\sum_{j\ge0}m_j. \tag{4}
\]

The entire first-derivative Gamma series converges in $L^1(\mathbb R)$,
since its rung $L^1$ norm is $8/d_j^2$. Differentiating in distributions
therefore identifies the full Gamma distribution with $m(D_{\mathbb R})$,
where $D_{\mathbb R}$ in this notation is Fourier functional calculus,
not the high operator $D=QGQ$.

For rational $\xi$, partial sums plus

\[
0\le m(\xi)-\sum_{j<J}m_j(\xi)
\le\frac{16\xi^2}{(4J+1)^3}+\frac{2\xi^2}{(4J+1)^2} \tag{5}
\]

are exact rational whole-tower enclosures. This is a primitive multiplier
bound, **not** an eigenvalue bound for compressed $D$.

Splitting the series at $j\asymp1+|\xi|$ proves
$m(\xi)\le C_1+C_2\log(2+|\xi|)$: the initial sum is bounded by a
harmonic sum and the tail by (5). The matching logarithmic lower growth
follows by keeping rungs $d_j\le2|\xi|$, each at least $2/d_j$.
In particular $m(D_{\mathbb R})E:L^2(I)\to H^{-\epsilon}(\mathbb R)$
is bounded for every $\epsilon>0$. No positive Sobolev regularity is
being inferred from this logarithmic multiplier.

On $I$ the remaining exact signed operator is bounded:

\[
(Bf)(x)=-Cf(x)+2\int_I\cosh((x-y)/2)f(y)\,dy
 -w\{Ef(x-\tau)+Ef(x+\tau)\}. \tag{6}
\]

All channels in (6) are essential. In particular, the pole contribution
is the signed rank-two form
$2(|\langle f,\cosh(t/2)\rangle|^2-|\langle f,\sinh(t/2)\rangle|^2)$,
not a manufactured positive term. A sufficient bound is
$\|B\|\le C+2\cosh(1/2)+2w<10$.

Consequently the distributional identity, valid for every $f\in L^2(I)$, is

\[
-\partial_x(Tf)=\left.m(D_{\mathbb R})Ef\right|_I+Bf. \tag{7}
\]

Only the Gamma operator is extended globally in (7); the exponentially
growing pole formula is not asserted to be a bounded whole-line convolution.

For $f\in H^1_0(I)$, integration by parts and (4) yield

\[
\langle Gf',f'\rangle=s[f]
:=\int_{\mathbb R}m(\xi)|\widehat{Ef}(\xi)|^2d\xi+\langle Bf,f\rangle.
\tag{8}
\]

The closed semibounded form has domain

\[
X=\{f\in L^2(I):\sqrt m\,\widehat{Ef}\in L^2(\mathbb R)\},
\quad\|f\|_X^2=\int(1+m)|\widehat{Ef}|^2.
\tag{9}
\]

This closed form has a Friedrichs-associated self-adjoint operator. That
existence alone does **not** identify its maximal distributional domain.

## SR-03 — explicit endpoint/domain lemma, not an extension assumption

**PAPER PROOF, genuine Gamma kernel on this interval.** If $f\in L^2(I)$
and $(m(D_{\mathbb R})Ef)|_I\in L^2(I)$ as distributions, then

\[
m(D_{\mathbb R})Ef\in L^2(\mathbb R),\qquad
Ef\in\operatorname{Dom}(m(D_{\mathbb R})),\qquad f\in X. \tag{10}
\]

Here the global multiplier domain is the explicit set
$\{v\in L^2(\mathbb R):m\widehat v\in L^2(\mathbb R)\}$.
The proof does not appeal to essential self-adjointness of a minimal
moment-restricted interval operator.

**Exterior estimate.** Away from the closed interval, the delta terms vanish
and the off-diagonal kernel is

\[
h(r)=\sum_{j\ge0}e^{-d_jr/2}
=\frac{e^{-r/2}}{1-e^{-2r}},\qquad r>0,
\quad h(r)\le\frac3{2r}. \tag{11}
\]

Indeed $1/(1-e^{-2r})\le1+1/(2r)$, from $e^{2r}-1\ge2r$,
and $r e^{-r/2}\le2/e<1$. Multiplying gives (11).
The Carleman operator $Cv(s)=\int_0^\infty v(t)/(s+t)\,dt$ has
$L^2(0,\infty)$ norm at most $\pi$: the Schur weight $p(t)=t^{-1/2}$
satisfies $\int_0^\infty p(t)/(s+t)\,dt=\pi p(s)$, and the same
identity applies in the other variable. The identity follows by
$t=su^2$ and $\int_0^\infty2/(1+u^2)\,du=\pi$.

For the right exterior write $x=a+s$, $y=a-t$, extending (f(a-t))
by zero for (t>1). Formula (11) gives an exterior norm at most
$3\pi\|f\|_2/2$. Reflection gives the identical left-exterior bound.
The two outputs have disjoint supports, hence

\[
\left\|\int_Ih(|x-y|)f(y)\,dy\right\|_{L^2(I^c)}
\le\frac{3\pi}{\sqrt2}\|f\|_2<7\|f\|_2. \tag{12}
\]

The actual exterior distribution equals the negative of this integral:
on compact sets separated from the interval, the rung kernels converge
uniformly and can be integrated against $f\in L^1(I)$. Thus (12)
constructs an $L^2$ representative on the **entire open exterior**,
including its approach to the endpoints.

**No hidden endpoint distribution.** Let $q=m(D_{\mathbb R})Ef$.
By SR-02, $q\in H^{-1/4}(\mathbb R)$. Patch its assumed interior
$L^2$ representative with the exterior representative just constructed,
obtaining $q_0\in L^2(\mathbb R)\subset H^{-1/4}(\mathbb R)$.
The distribution $q-q_0$ is supported at $\{-a,a\}$. A distribution
supported at finitely many points is a finite sum of derivatives of deltas.
No nonzero such distribution belongs to $H^{-1/4}(\mathbb R)$.
For a single point, its Fourier transform is an exponential times a nonzero
polynomial, whose square is not integrable with weight
$(1+\xi^2)^{-1/4}$; smooth localization isolates either point and is
bounded on this Sobolev space. Hence $q=q_0$ globally.

Taking Fourier transforms gives $m\widehat{Ef}\in L^2$. Together with
$Ef\in L^2$, Cauchy–Schwarz gives the finite form integral in (9).
This proves (10). The absence of endpoint deltas is a **proved step**;
it is not assumed by imposing zero traces on $f$.

**Quantitative form of the lemma.** The same proof yields

\[
\|m(D_{\mathbb R})Ef\|_2^2
\le\|\left.m(D_{\mathbb R})Ef\right|_I\|_2^2+49\|f\|_2^2.
\tag{13}
\]

This is an implementable source-specific domain bound, not a bound on a
compact inverse or on the numerical integration error.

## SR-04 — coercivity extension and disappearance of the annihilator

**CONDITIONAL PAPER PROOF**, depending on source (4), (6) and inherited (H).

First $C_c^\infty(I)\cap M$ is dense in $X\cap M$ for the form norm.
Here is the exact core argument. Shrink a zero-extended $f\in X\cap M$
by $f_c(t)=f(t/c)$, $0<c<1$, giving support strictly inside $I$.
Dilation is strongly continuous in the weighted Fourier norm (9).
For completeness, the rational summands in (4) give

\[
\min(1,c^2)m(\xi)\le m(c\xi)\le\max(1,c^2)m(\xi).
\]

This makes dilation uniformly bounded for $1/2<c<1$; approximation
in weighted $L^2$ by smooth Fourier data proves strong continuity.
Mollify after shrinking, with support small enough to stay inside $I$.
Fourier multiplication by the mollifier converges in (9) by dominated
convergence. Dilation preserves the first four vanishing moments; convolution
also preserves them by the binomial moment formula. This supplies the
claimed compactly supported smooth approximants without a boundary assumption
on $f$. It is form density, **not** an unproved assertion of operator-core
density in an $H^2$ or graph norm.

For each such smooth $f$, let $u=f'$. Integration by parts gives
$u\in QH$, $Vu=f$. Equations (8) and (H) imply

\[
s[f]\ge\kappa\|f\|_2^2.
\]

Continuity in the form norm extends this inequality to every $f\in X\cap M$.

Now let $f\in\ker R_Q^*\subset M$. By (2), $Tf=p\in\mathcal P_4$.
Equation (7) gives the actual interior identity

\[
\left.m(D_{\mathbb R})Ef\right|_I=-p'-Bf\in L^2(I).
\]

SR-03 supplies $f\in X$ and indeed the global multiplier operator domain.
Therefore the form integral can be paired in $L^2$, and

\[
s[f]=\langle\left.m(D_{\mathbb R})Ef\right|_I+Bf,f\rangle
=\langle-p',f\rangle=0,
\]

because $p'\in\mathcal P_3$ and $f\in M$. Coercivity forces $f=0$.
Thus, under the explicit inherited hypothesis,

\[
\boxed{\ker R_Q^*=0,\qquad\overline{\operatorname{Ran}R_Q}=M.} \tag{14}
\]

In particular all four genuine $R_P$ columns annihilate the adjoint kernel,
and the infimum of their relative residual norm over high $L^2$ responses
is zero. Round II's bounded-map polynomial graph density then gives the same
infimum over high polynomial responses. No assertion that this infimum is
attained, no convergence rate, and no claim about a particular energy-Galerkin
sequence follows. The numerical experiment below is not evidence for a
universal theorem; the domain argument above is its proposed proof.

**Why CG-08 is not contradicted.** The clamped-biharmonic construction has
an actual finite-dimensional cokernel caused by its boundary conditions.
It has no source identity (4), no off-diagonal Gamma kernel (11), and no
logarithmic $H^{-\epsilon}$ control excluding endpoint distributions.
Coercivity plus compactness alone still cannot prove (14). CG-07 remains
a valid counterexample to convergence of an energy-Galerkin sequence even
when the residual range is dense.

## SR-05 — actual-source obstruction to a bounded upper relative form

**PAPER PROOF, source-specific; does not require (H).** There is no finite
$C_0$ such that $D\le C_0K_Q$ on (QH).

Choose nonzero $\psi\in C_c^\infty(I)$. Choose four fixed compactly
supported smooth functions $\eta_j$ whose moment matrix is the identity
through degree three. They exist by multiplying $1,t,t^2,t^3$ by one
nonnegative interior bump and inverting its positive definite moment Gram.
Put

\[
f_\omega=e^{i\omega t}\psi(t)
-\sum_{j=0}^3\left(\int_I t^j e^{i\omega t}\psi(t)dt\right)\eta_j(t).
\]

Then $f_\omega\in C_c^\infty(I)\cap M$, its corrections decay faster
than every power of $|\omega|^{-1}$, and
$\|f_\omega\|_2\to\|\psi\|_2>0$. Set $u_\omega=f_\omega'\in QH$,
so $Vu_\omega=f_\omega$.

For **fixed** $J$, the bounded finite multiplier
$m_J=\sum_{j<J}m_j$ tends to $c_J=\sum_{j<J}4/d_j$ as frequency
tends to either infinity. Plancherel, modulation and dominated convergence
give

\[
\frac{\langle m_J(D_{\mathbb R})Ef_\omega,Ef_\omega\rangle}
 {\|f_\omega\|_2^2}\longrightarrow c_J.
\]

The full Gamma form dominates every finite partial form. Equation (6)
therefore gives

\[
\liminf_{|\omega|\to\infty}
 \frac{\langle Du_\omega,u_\omega\rangle}
 {\langle K_Qu_\omega,u_\omega\rangle}
\ge c_J-\|B\|\quad\hbox{for every }J.
\]

Since $c_J\to\infty$, the ratio tends to infinity. The order of limits
is explicit: choose finite $J$ to exceed the desired bound, then increase
$|\omega|$. There is no exchange of a frequency limit with an uncontrolled
infinite sum. This refutes the bounded-$S$ upper-comparison repair suggested
conditionally in CG-04/05 **for the genuine source**. It neither refutes
fractional range nor gives a negative source direction.

## SR-06 — fractional range: what was tried and the exact remaining lemma

**OPEN beyond exponent $1/2$.** The inherited range argument gives
$b=QGP\in\operatorname{Ran}D^{1/2}$ columnwise. For $\alpha>1/2$, neither
the bounded map $G:L^2\to H^1$, (14), nor the source's logarithmic order
licenses $b\in\operatorname{Ran}D^\alpha$.

The tempting interpolation route fails at a specific algebraic gate:
$D\ge\kappa K_Q$ permits the square-root Douglas inclusion, but raising
that inequality to power $2\alpha>1$ is not an operator-monotone operation.
Moreover SR-05 proves the convenient upper comparison $D\le CK_Q$ is
unavailable for this source. These failed routes are retained, not repaired
by an unsupported Sobolev-to-$D$-spectral identification.

The primitive source picture does give a concrete next problem. Let $S$
be the operator associated with $s$, and $S_M$ the positive operator
associated with $s|_{X\cap M}$. The latter is boundedly
invertible by (H). For a low input $p$, put $z=Vp\in H^1_0(I)$.
Equation (7) and integration by parts give
$\Pi_M S z=-R_Pp$. The variational primitive response is the unique

\[
f_*=S_M^{-1}\Pi_M S z\in\operatorname{Dom}S_M.
\]

Indeed $R_Qu=-S_MVu$ on its appropriate smooth domain. If one proved
$f_*\in H^1_0(I)\cap M$, then $u=f_*'\in QH$ would attain the
response and $b\in\operatorname{Ran}D$. That regularity is not proved:
the logarithmic domain itself contains functions with nonzero traces and
does not imply $H^1_0$. A fractional version requires a theorem relating
the regularity of $f_*$ to the spectral powers of $D=V^*S_MV$, with
the compression and endpoints included. Merely quoting a full-line symbol
with multiplier size $|\xi|^{-2}\log(2+|\xi|)$ does not supply that theorem.

An equivalent exact spectral test is available. For one actual target column
$b$, let $\mu_b$ be its spectral measure for positive injective $D$.
Then

\[
b\in\operatorname{Ran}D^\alpha
\iff \int_{(0,\|D\|]}\lambda^{-2\alpha}\,d\mu_b(\lambda)<\infty.
\tag{15}
\]

For $0<\alpha<1$, Tonelli and $t=\lambda s$ also give

\[
\int_0^\infty t^{-2\alpha}\|t(D+t)^{-1}b\|^2\frac{dt}{t}
=\Gamma(2-2\alpha)\Gamma(2\alpha)
 \int\lambda^{-2\alpha}\,d\mu_b(\lambda). \tag{16}
\]

Thus an implementable sufficient lemma for exponent $5/8$ is the
**actual infinite-source** bound

\[
\mu_b((0,16^{-j}])\le C_b64^{-j}\qquad(j=0,1,\ldots).
\tag{F}
\]

On the $j$-th geometric band, $\lambda^{-5/4}\le32^{j+1}$.
Summing gives the explicit consequence
$\|D^{-5/8}b\|^2\le\|b\|^2+64C_b$.
This is a conditional bound, not an established source estimate. No finite
positive matrix or a fitted slope in the experiment discharges (F).

## Executed controls and numerical discriminator

The first exact/default probe passed **14 focused tests** in under one second.
Exact controls check the primitive moment map, all boundary terms in the
finite-rung identity as rational coefficients of $1,e^{-d/2}$, whole-tower
multiplier tails, and rejected input types. Numerical controls independently
compare the complete derivative with existing rational source boxes, check
the geometric Gamma kernel, and catch complex-conjugation/parity mutants.
Passing numerical tolerances is explicitly separate from interval proof.

`source_range-numerical-initial.json` records a serial source computation
with rank 24, 24 fit nodes and 48 holdout nodes **per panel**. Inner quadrature
splits at the diagonal and actual prime thresholds; outer panels split at
their shifted endpoints. The full Gamma derivative is used, with no finite
Gamma truncation, diagonal regularization, positive-part projection, or
eigenvalue clipping. Low/high modes are orthonormal Legendre coordinates.

Each high least-squares response is frozen on the fit grid and evaluated
without refitting on the holdout grid. The four holdout residual norms are:

| Highest mode | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---:|---:|---:|---:|
| 8 | 0.0128091 | 0.0188667 | 0.0138395 | 0.0256036 |
| 12 | 0.0084233 | 0.0140028 | 0.0087460 | 0.0186138 |
| 16 | 0.0069224 | 0.0124178 | 0.0071555 | 0.0162910 |
| 24 | 0.0058170 | 0.0095669 | 0.0060125 | 0.0126904 |

**EXPERIMENT ONLY.** Holdout $T$-skew defect is $4.80\,10^{-7}$;
fit-grid defect is $1.27\,10^{-5}$. The rank-24 residual-Gram change between
fit and holdout is $1.62\,10^{-6}$, appreciable compared with the residuals.
The continuum Gram has no rigorous quadrature error enclosure here.
Finite singular values decrease but are not a continuum nullspace test.

Finite $D$-spectral moments at exponent 1 grow, for example column 4
from about 0.263 at rank 8 to 1.869 at rank 24. At exponent $5/8$ the
same column changes from about 0.003382 to 0.005440. These are different
finite compressions, not certified bounds for the infinite functional
calculus; neither divergence nor convergence has been proved.

The computed right-endpoint $R_P$ fluxes are approximately
$(-0.0603845,-0.116875,-0.0963181,-0.162500)$, with parity-consistent left
fluxes. They identify boundary cancellation as a real numerical issue,
not a licensed nonattainment theorem. No larger numerical sweep is required
to review the decisive domain argument above.

## Claim ledger and reproduction

| ID | Claim | Status and boundary |
|---|---|---|
| SR-01 | Actual adjoint integral equation, conjugation, parity, boundary formula | PAPER DERIVED; exact finite controls do not prove the infinite identity |
| SR-02 | Actual Gamma multiplier and signed remainder | PAPER DERIVED; exact rational whole-tower multiplier bounds executed |
| SR-03 | Interior distributional $L^2$ implies global Gamma multiplier domain | PRINCIPAL / INDEPENDENTLY AUDITED PAPER PROOF; Carleman bound plus explicit endpoint-distribution exclusion |
| SR-04 | $\ker R_Q^*=0$, dense actual residual range | PRINCIPAL / INDEPENDENTLY AUDITED CONDITIONAL PAPER PROOF on inherited (H) and actual-source identities; not generic coercivity |
| SR-05 | No finite $C$ with $D\le CK_Q$ | SOURCE-SPECIFIC PAPER PROOF; not a fractional-range obstruction |
| SR-06 | $b\in\operatorname{Ran}D^\alpha$, some $\alpha>1/2$ | OPEN; exact remaining spectral lemma (F) and formula (16) |
| SR-NUM | Frozen responses on a fresh quadrature grid | EXPERIMENT ONLY; raw spectra, coefficients and errors retained |
| SR-SIGN | Original $S_0\ge0$ and RH | OPEN / NOT PROVED |

Provenance grouping: the source formula, exact rung calculation, and numerical
derivative all share one arithmetic lineage. They are different representations,
not independent arithmetic sources. This worker and the principal independently
reached the logarithmic-upper-obstruction route before exchanging it. The
principal subsequently reported acceptance of the domain proof after analytic
review; the reported independent audit is distinct from this worker's tests.
The inherited hostile audit remains separate evidence. No numerical coherence is promoted
to a probability or proof. Contact/source identity, survived claims, source-map
adequacy and commitment pressure remain separate audit items.

The standalone probe has no file writes without `--output`. It disables
bytecode and numerical thread fan-out. Reproduction:

```sh
python -B scripts/arithmetic_source_range_probe.py --output research/2026-10-16/arithmetic_resonance_receipts/source_range-default.json
python -B scripts/arithmetic_source_range_probe.py --numerical --rank 24 --fit-nodes 24 --holdout-nodes 48 --output research/2026-10-16/arithmetic_resonance_receipts/source_range-numerical.json
python -B -m unittest discover -s tests -p test_arithmetic_source_range.py -v
```

Initial receipts are retained. Both Python 3.10.20 and Python 3.13.13 passed
all 14 focused tests and the default probe, with no skips. The 72-entry
provenance replay also passed. The final source_range-py310.json,
source_range-py313.json and source_range-freeze.json receipts record the
final file hashes and source stability. The numerical receipt pins the same
module, test and script bytes; subsequent dossier editing changes no executable.
The principal owns full-suite execution, integration and any promotion after
independent analytic review.
