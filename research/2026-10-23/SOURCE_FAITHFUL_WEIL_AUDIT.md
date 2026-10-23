# Carry to the signed source: a sharp half-density transport and its boundary

**Date:** 2026-10-23. **Baseline:** PR #244 at
`5e2ba04c8b4ab627b6b0add588609c347346a1a2`.
**Status:** paper proofs with exact finite/interval controls; no Lean claim for
these analytic statements. **Original four-mode Schur sign: OPEN. RH: OPEN.**

The strongest result of this lane is an actual source map together with its
obstruction. Authentic integer multiplication cannot be transported by a
nonzero bounded Hilbert map to unweighted translations at logarithmic
addresses. The critical half-density repairs boundedness, with an explicitly
weakened covariance law. It reconstructs the genuine prime distribution after
smoothing, while the cost of removing that smoothing diverges. This separates
three operations that were easy to conflate: preserving arithmetic addresses,
preserving Hilbert norms, and constructing the signed completed Weil form.

## 1. Contract, recovered source, and unchanged obstruction

The proposed strong statement is the existence of a nonzero bounded map

\[
J:\ell^2(\mathbb N_{\ge1})\longrightarrow L^2(\mathbb R,dx),\qquad
JV_p=\tau_{\log p}J,\qquad (\tau_t f)(x)=f(x-t),
\tag{W1}
\]

for every genuine prime multiplier. Its status before the proof below was
UNVERIFIED. It is much weaker than identifying the completed Weil form, yet it
would close a concrete source-action interface. The cheapest falsifier is a
normalized group of integer addresses whose logarithms become almost equal.
The claim fails. A weighted version survives, without assuming any zeta-zero
statement, any physical instrument, or any positivity of the Weil form.

The actual inputs inspected were `AGENTS.md`, `docs/FOUNDATIONS.md`,
`docs/METHOD.md`, `provenance/IMPORT_MANIFEST.json`, and the source and proofs
behind these ancestors:

| Ancestor | Actual inspected mathematical object | Authority retained |
|---|---|---|
| #175 | `EQUIVARIANT_REDUNDANCY_WEIL.md`; source-relative form descent, contact ambiguity, prime homotopy defects | Classical/local paper results; not a positive Weil identification |
| #177 | `ORIGINAL_CONTINUUM_RESIDUAL_SCHUR.md`, `original_continuum_residual.py`, `suzuki_legendre_source.py` | Original continuum action, true residual and paid Gamma tails |
| #181 | `DIRECTIONAL_ORIGINAL_INVERSE.md`, `ORIGINAL_SOURCE_FORM_CLOSURE.md`, `directional_source_inverse.py` | Directional inverse bounds with the original high-space gap as an explicit premise |
| Earlier source | `source_weil_hierarchy.py`, `tate_suzuki_shorting.py`, `tate_weil_distribution.py`, `TATE_TO_WEIL_DISTRIBUTION.md` | Frozen source formulas and source-defined signed distribution |

The original source module is unchanged:

- Git blob: `0cc8510b71d178fc79e8d410a86d8b6014cf9178`.
- SHA256: `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`.
- Foundational import: `femboy2112/FuckingRH` at
  `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; 72-entry manifest. The later
  frozen Suzuki module is a distinct source pin, not one of those original
  72 imported bytes.

The code checks the actual bytes before importing source constants. A hash
authenticates those bytes; the analytic identification with Suzuki is supported
by the displayed formula and existing source derivations, not by the hash alone.

For \(g\in C_c^\infty(\mathbb R;\mathbb C)\), retain the original source

\[
W(g)=P(g)+A(g)-E(g),\quad
P(g)=\int 2\cosh(u/2)g(u)\,du,
\]
\[
E(g)=\sum_{p,r\ge1}\frac{\log p}{p^{r/2}}
       [g(r\log p)+g(-r\log p)],
\]
\[
A(g)=-(\gamma+\log(4\pi))g(0)
 -\int_0^\infty\frac{e^{-x/2}}{1-e^{-2x}}
 [g(x)+g(-x)-2e^{-x/2}g(0)]\,dx.
\tag{W2}
\]

The prime sum is locally finite. The cancellation in the Archimedean integral
defines its identity contact. The completion is exactly
\(\pi^{-s/2}\Gamma(s/2)\zeta(s)\): one real Gamma, conductor 1, even parity,
root number +1, and poles at both 0 and 1. The global Fourier convention is
\(\widehat f(y)=\int f(x)e^{2\pi ixy}dx\), paired with the opposite finite-place
character; the log-test angular transform is
\(H_g(s)=\int g(u)e^{(s-1/2)u}du\), with inversion factor \(1/(2\pi)\).
Neither the additive residue character nor its magnitude can replace these
conventions without a transport theorem.

The source is **signed**. This does not assert that its complete quadratic
form is known to be indefinite: its nonnegativity on all admissible
autocorrelations is precisely the unresolved positivity question.

## 2. W-01: no bounded unweighted arithmetic-to-log-translation intertwiner

**Theorem.** Let \(p,q>1\) be multiplicatively independent integers. If a
bounded linear \(J:\ell^2(\mathbb N_{\ge1})\to L^2(\mathbb R)\) satisfies
\(JV_p=\tau_{\log p}J\) and \(JV_q=\tau_{\log q}J\), then \(J=0\).
In particular, the theorem holds for the genuine prime pair 2,3. No adjoint
intertwining, successor intertwining, or zeta hypothesis is required.

**Proof.** Fix any \(m\ge1\) and put \(\phi=Je_m\). Suppose \(\phi\ne0\).
Strong continuity of translations gives \(\delta>0\) such that
\(\|\tau_h\phi-\phi\|_2\le\|\phi\|_2/2\) whenever \(|h|\le\delta\).
The \((L+1)^2\) distinct source labels
\(mp^a q^b\), \(0\le a,b\le L\), have logarithmic offsets in
\([0,L(\log p+\log q)]\). Partition this interval into at most
\(1+\lceil L(\log p+\log q)/\delta\rceil\) subintervals of length at most
\(\delta\). One bin contains \(M_L\) labels, with \(M_L\to\infty\).
For its offsets \(t_i\), choose one \(t_0\). Intertwining gives
\(Je_{mp^a q^b}=\tau_{a\log p+b\log q}\phi\). Hence the triangle inequality
gives

\[
\left\|\sum_{i=1}^{M_L}\tau_{t_i}\phi\right\|_2
\ge M_L\|\phi\|_2-
\sum_i\|\tau_{t_i}\phi-\tau_{t_0}\phi\|_2
\ge\tfrac12M_L\|\phi\|_2.
\]

The source sum divided by \(\sqrt{M_L}\) has norm one, so
\(\|J\|\ge\tfrac12\sqrt{M_L}\|\phi\|_2\), a contradiction. Thus
\(Je_m=0\) for every basis label; boundedness implies \(J=0\). QED.

**Common-flow corollary.** The same proof works for any Hilbert target carrying
a strongly continuous one-parameter unitary group `U_t`: if bounded J satisfies
`J V_p=U_(log p) J` and `J V_q=U_(log q) J` for two multiplicatively independent
integers, then J=0. Replace every translation above by U; only its group law,
unitarity and strong continuity were used. In particular the normalized real
dilations `U_t f(x)=exp(-t/2) f(exp(-t)x)` on `L²(R_+)` cannot be a nonzero
bounded unweighted simultaneous transport of V2 and V3. This corollary does
not prohibit a target with genuinely separate prime actions that fail to be
one common continuous unitary flow. The weighted covariance in W-02 evades
precisely this unweighted hypothesis.

**One-generator positive control.** For just \(V_2\), map \(e_{2^a}\) to
\(\tau_{a\log2}\phi\), where \(\phi=\sqrt2\,1_{[0,1/2]}\), and map every
other basis vector to zero. The translated supports are disjoint since
\(\log2>1/2\). This is a nonzero norm-one partial isometry intertwining
\(V_2\). Therefore a purported proof that one multiplier already forces zero
would be false. The two-dimensional arithmetic orbit is load-bearing.

**Concrete all-prime calibration.** If \(Je_n=\tau_{\log n}1_{[0,1]}\), then
all pairs \(n,m\in[N,2N]\) have overlap at least \(1-\log2>3/10\).
The unit source block has squared image norm at least \(3(N+1)/10\).
The executable interval oracle verifies this independently on
\(N=1,4,16,31\); the universal divergence is the preceding proof.

This theorem forbids exactly (W1). It does **not** forbid rigged Hilbert spaces,
distributions, unbounded maps on a dense core, a changed covariance law,
different source measures, or richer target carriers with additional registers.
An abstract unitary between separable Hilbert spaces exists but need not
intertwine the authenticated source actions.

## 3. W-02: half-density is the sharp boundedness threshold in this family

Let \(0\ne\phi\in L^2(\mathbb R)\) be supported in an interval of finite
length \(L>0\). On finitely supported source sequences define

\[
J_{\alpha,\phi}a=\sum_{n\ge1}a_n n^{-\alpha}\tau_{\log n}\phi,
\qquad\alpha\in\mathbb R.
\tag{W3}
\]

**Theorem.** This map extends boundedly from counting-measure \(\ell^2\) to
\(L^2(dx)\) if and only if \(\alpha\ge1/2\). At the endpoint,

\[
\|J_{1/2,\phi}\|^2\le (1+L)\|\phi\|_2^2,
\qquad
J_{\alpha,\phi}V_p=p^{-\alpha}\tau_{\log p}J_{\alpha,\phi}.
\tag{W4}
\]

For the second identity, equality initially holds on finite support; for
\(\alpha\ge1/2\) it extends everywhere by boundedness.

**Proof of boundedness.** Write the support interval as \([a,b]\). At each
x, nonzero terms have \(e^{x-b}\le n\le e^{x-a}\). If the integer range is
\(m\le n\le M\), then \(M/m\le e^L\), and

\[
\sum_{n=m}^M\frac1n\le\frac1m+\int_m^M\frac{dt}{t}\le1+L.
\]

Weighted Cauchy–Schwarz therefore bounds

\[
|J_{1/2,\phi}a(x)|^2\le(1+L)
\sum_n |a_n|^2|\phi(x-\log n)|^2.
\]

Integration gives (W4). For larger \(\alpha\), precompose with the diagonal
contraction \(e_n\mapsto n^{-(\alpha-1/2)}e_n\).

**Proof of necessity.** By translation continuity, choose \(\delta>0\) with
\(\Re\langle\tau_t\phi,\tau_u\phi\rangle\ge\|\phi\|^2/2\) for
\(|t-u|\le\delta\). The labels
\(N\le n\le\lfloor e^\delta N\rfloor\) number \(M\asymp N\) and have
pairwise log gaps at most \(\delta\). On the unit source block,

\[
\|J_{\alpha,\phi}a\|^2
\ge\frac{\|\phi\|^2}{2M}\left(\sum_n n^{-\alpha}\right)^2
\ge c_{\alpha,\delta,\phi}N^{1-2\alpha}.
\]

The positive constant is independent of N: throughout the block,
\(n^{-\alpha}\ge\min(1,e^{-\alpha\delta})N^{-\alpha}\).
For \(\alpha<1/2\) this diverges. Finally, the covariance formula follows
on \(e_n\) from \((pn)^{-\alpha}=p^{-\alpha}n^{-\alpha}\). QED.

**What is and is not selected.** Half-density is the *least damping exponent*
that makes this declared family bounded. Every larger exponent is also
bounded; boundedness alone does not uniquely select the endpoint, a physical
scale, or the Weil completion. The choice of counting measure, log addresses,
fixed finite-resolution seed, and target Lebesgue measure is explicit.

The repair is lossy in norm:
\(\|J_{1/2,\phi}e_n\|=n^{-1/2}\|\phi\|\to0\).
It has no uniform lower bound, and cannot be a unitary or have a bounded
inverse on its image. Finite translated nonzero \(L^2\) seeds are linearly
independent: Fourier transformation reduces a finite dependence to an
exponential polynomial vanishing on a positive-measure set where
\(\widehat\phi\ne0\); analyticity forces every coefficient to vanish.
Thus finite algebraic distinguishability can coexist with arbitrarily poor
Hilbert conditioning. No claim of injectivity on all infinite sequences is
needed here.

## 4. W-03: an actual commutator-to-prime-distribution map

Let \(H_0e_n=(\log n)e_n\) with
\(\operatorname{Dom}H_0=\{a:\sum_n(\log n)^2|a_n|^2<\infty\}\).
Multiplication by a fixed positive integer preserves this domain, since
\(\log(pn)=\log n+\log p\). On it,
\([H_0,V_p]=(\log p)V_p\), with bounded commutator extension. Hence for
every genuine prime p and integer r≥1,

\[
J_{1/2,\phi}[H_0,V_p]e_{p^{r-1}}
=\frac{\log p}{\sqrt{p^r}}\tau_{r\log p}\phi.
\tag{W5}
\]

This is an independent realization of the carry register's half-density
coefficient with a genuine log-address action. It has the weakened covariance
(W4), not the forbidden isometric covariance (W1). It also distinguishes the
primitive logarithm \(\log p\) from \(r\log p\).

The negative-address map requires an explicit orientation transport. Put
\((Rf)(x)=f(-x)\) and
\(J^-_{\alpha,\phi}=R J_{\alpha,R\phi}\). Then
\(J^-_{\alpha,\phi}e_n=n^{-\alpha}\tau_{-\log n}\phi\) and
\(J^-_{\alpha,\phi}V_p=p^{-\alpha}\tau_{-\log p}J^-_{\alpha,\phi}\).
It has the same bound as its positive-address partner. Thus no evenness of
the seed is required and no unlabelled phase/orientation change is hidden.

For a chosen \(\phi\in C_c^\infty\), summing the two oriented versions of
(W5) gives exactly

\[
\phi*E=\sum_{p,r\ge1}\frac{\log p}{p^{r/2}}
 [\tau_{r\log p}\phi+\tau_{-r\log p}\phi].
\tag{W6}
\]

The sum is locally finite. A composite channel \(V_6\) satisfies the same
commutator calculation but would insert a false primitive log(6) atom.
Primeness/primitive-history provenance remains an independent input, verified
by the authentic source tape. Repeated-prime input 4 must retain log(2).
`regularized_prime_tape` retains n,p,r, input \(p^{r-1}\), the log center and
outward original-source weight. An independent factorization oracle checks
all n≤125, including withheld prime powers 49 and 125 and fake composite 6.

**Distributional completion and its exact price.** Choose a smooth compact
seed with integral one and support width L. Put
\(\phi_\epsilon(x)=\epsilon^{-1}\phi(x/\epsilon)\). Then
\(\phi_\epsilon*E\to E\) in \(\mathcal D'(\mathbb R)\). Indeed, on any
fixed test support only finitely many atoms can contribute for small epsilon,
and approximate-identity convergence applies to each. Moreover

\[
\frac{\|\phi\|^2}{\epsilon}
\le\|J_{1/2,\phi_\epsilon}\|^2
\le\frac{(1+\epsilon L)\|\phi\|^2}{\epsilon}.
\tag{W7}
\]

The lower bound is the source vector e1; the upper is (W4). Thus
\(\epsilon\|J_{1/2,\phi_\epsilon}\|^2\to\|\phi\|^2\): resolution removal
has a sharp divergent Hilbert cost. The box-seed interval tests calibrate this
at widths 1,1/4,1/16,1/64. A smooth seed is used in the distribution theorem;
the box oracle does not purport to be a smooth Weil-test certificate.

There is also a raw distribution map
\(e_n\mapsto\delta_{\log n}\), with exact unweighted prime covariance on
the algebraic source. It is not an \(L^2\)-valued bounded map. The two routes
make the topology change visible rather than identifying incompatible norms.

**Boundary.** (W6) reconstructs E, not W. Gamma, poles and contact in (W2) are
separate authenticated analytic data. Adding their already-known formulas
recovers the already-known signed distribution; it supplies no positive norm
representation and no new Schur margin. Formula (W6) is a real but limited
source bridge, not an RH-equivalent assertion disguised as a theorem.

## 5. W-04: exact inverse defects and why residue norm cannot pay the Schur debt

Work in the actual first-window primitive completion
\(E=(\operatorname{span}\{1,x,x^2,x^3\})^\perp\subset L^2(-1/2,1/2)\).
The source high operator D is the restriction of the closed completed form;
the inherited theorem gives \(D\ge\kappa I\) under its source/core
hypotheses, with derivative-parity values 63/500 and 153/500. This is **not**
an ordinary derivative-\(L^2\) gap. With actual low source map B and energy A,
the original coefficient-space Schur form is \(S_4=A-B^*D^{-1}B\).
The primitive low span need not equal \(E^\perp\).

If a unitary U really transports this high space and its domain, then
\(D'=UDU^*\), \(B'=UB\), and

\[
B'^*D'^{-1}B'=B^*D^{-1}B.
\tag{W8}
\]

This follows directly from the resolvent functional calculus; a change of
coordinates alone creates no inverse saving. It does not prohibit a better
inequality discovered in those coordinates. Before applying a discrete
polyphase W to the continuum high space, one must construct the source and
domain map; a shared separable Hilbert dimension is insufficient.

There is also a precise cost when a genuine high-space decomposition exists.
For a **bounded** positive block operator

\[
D=\begin{pmatrix}E_0&F\\F^*&G\end{pmatrix}\ge\kappa I,
\quad B=\binom b c,\quad R=G-F^*E_0^{-1}F,
\]

block completion of the square gives

\[
B^*D^{-1}B=b^*E_0^{-1}b+
(c-F^*E_0^{-1}b)^*R^{-1}(c-F^*E_0^{-1}b).
\tag{W9}
\]

Here E0 and R are positive invertible. The discarded term is PSD. Replacing
the full inverse correction by the first term alone therefore gives a
**lower** correction, hence an **upper** Schur form; it cannot certify a lower
Schur bound. The discarded term vanishes exactly when
\(c=F^*E_0^{-1}b\). Even c=0 does not suffice if F couples the sectors.
For an unbounded original D this algebra requires a justified form/domain
version of the block decomposition; it is not silently applied as a bounded
matrix formula to the original operator.

**Exact phase control.** Let

\[
D=\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad A=1,
\quad B_+=\binom11,\quad B_-=\binom1{-1}.
\]

Both couplings have the same visible and hidden norms, and D is identical.
Yet \(B_+^*D^{-1}B_+=2/3\), \(B_-^*D^{-1}B_-=2\), so the Schur values
are respectively 1/3 and −1. This refutes *phase-blind norm data imply a
Schur sign*. It is a synthetic exact countermodel, not a negative witness
for the authentic Weil source. Conjugating D and B together by
diag(1,−1) leaves the correction unchanged, as required by (W8); changing
only one factor is the rejected fake phase transport.

The #181 directional inequality can improve the original inverse only from
actual source responses \(Z=(D-\kappa I)W\) and actual cross terms \(Z^*B\).
Uniform residue amplitudes, the scalar norm deficit 1−1/p, and (W6) do not
currently determine these responses in the original high completion.
No quantitative #181 or #177 bound is improved in this lane; the inverse
alternatives in #181/#182 must still never be summed as independent savings.

## 6. W-05: calibrated signed-source falsifiers

Let \(f(x)=(1-x^2)^3\) on [−1,1], zero outside, and
\(h=f*\widetilde f\). This is a legitimate compact C² test and extends to
the smooth test core by approximation. With b=log2, the certified inequalities
3/10<b<7/10 give, by integrating x in [0,3/10],

\[
h(b)\ge\frac3{10}\left(\frac{51}{100}\right)^6>0.
\]

Consequently the isolated genuine prime pair satisfies
\(-E_2(h)=-2(\log2)/\sqrt2\,h(b)<0\). It cannot equal a positive Hilbert
norm square. This refutes only a **termwise** positive-prime identification.
The other completion terms may compensate; no conclusion about the sign of
the complete W(h) follows. Smooth mollifications preserve strict positivity
of h(b), so the counterexample also reaches the compact smooth core.

The executable source mutations retain the original source function and
calculate explicit mutant-minus-original changes in its g_J chart at r=2:

| Mutant | Source change | Detection |
|---|---|---|
| Fake independent 6 | Add log(6)/sqrt(6) hinge | Strict positive interval |
| Omitted repeated prime power 4 | Remove log(2)/2 hinge | Strict negative interval |
| Matched non-Euler amplitude | Double the p=2 hinge | Strict positive interval |
| Wrong half-density at 2 | Replace 1/sqrt2 by 1/2 | Strict negative interval |
| Shifted real Gamma | Replace first rung d=1 by d=3 | Strict nonzero interval |
| Wrong poles | Flip the entire two-pole contribution | Strict nonzero interval |
| Contact change | Raise original C by 1 | Exact change r/2 |

At r=1/2 every prime mutation above is inactive: the code returns exact zero.
This is a meaningful support null control, preventing false claims that an
unexercised probe authenticates a source. Separate source contracts reject
wrong conductor, parity, root number, extra Gamma, missing poles, and bad
primitive provenance. The phase-sensitive inverse control exercises a
different failure mechanism from these source-value mutations.

## 7. Preservation ledger and scholarly scope

| Map or operation | Preserves | Loses or changes | Authority / topology |
|---|---|---|---|
| Exact carry W_p | Discrete source basis, norm, transported actions and histories if labels retained | No information when all sectors retained | Unitary on source Hilbert space; not a physical access claim |
| Forbidden unweighted J | Desired Vp/log-translation covariance | Boundedness impossible already for V2,V3 | W-01 paper theorem |
| J_(1/2),phi | Genuine addresses and weighted covariance; finite linear independence | Norms, uniform inverse stability; seed/resolution supplied | Bounded Hilbert map at fixed resolution, W-02 |
| Smoothed commutator sum | Prime-power log(p), half-density, signed atom locations | Does not supply Gamma/poles/contact | Locally finite smooth distribution, W-03 |
| epsilon→0 | Authentic prime distribution on every compact test | Uniform Hilbert operator bound diverges sharply | Distributional convergence, not strong bounded-operator convergence |
| Unitary high transport | Exact inverse correction and S4 | No automatic improved numerical bound | Requires real source/domain map, W-04 |
| Discard high/residue sector | Selected visible data | Positive inverse defect and phase-sensitive coupling | (W9), with domain assumptions explicit |

Cuntz residue relations and polyphase/wavelet correspondences are classical.
Bratteli–Jorgensen's primary paper explicitly connects multiresolution filters
and Cuntz representations; our source labels do not create a new Cuntz algebra.
The arithmetic logarithmic Hamiltonian and multiplier dynamics have established
Bost–Connes provenance. Connes–Marcolli display the log(n) spectrum and
distinguish Hilbert completions from rapidly decreasing/nuclear test spaces;
their adelic construction is richer than the target in (W1), so W-01 does not
refute it. Tate/Weil/Burnol already supply the completed explicit formula.

The log-address threshold and two-multiplier obstruction above are elementary
paper derivations newly used here to constrain SUCC's proposed transport.
Related weighted sampling and local Dirichlet-series embedding theory is
extensive; **academic priority is unverified**. These results should be
described as new-to-project preservation and failure theorems, not announced
as a new foundation of analytic number theory. The computation adds source
fingerprints, sign-aware mutations and a separate exact inverse oracle.

Primary references checked during this round:

1. O. Bratteli and P. E. T. Jorgensen, *Isometries, shifts, Cuntz algebras and
   multiresolution wavelet analysis of scale N* (1997),
   https://arxiv.org/abs/funct-an/9612003 .
2. J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase
   transitions with spontaneous symmetry breaking in number theory* (1995),
   https://doi.org/10.1007/BF01589495 . The original scan was located in the
   IHES archive and on Connes's author site; the web reader rejected its size.
   The author-written account used for the displayed log-spectrum comparison
   is Connes–Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*,
   Chapters 2–4, especially pp. 358 and 578–579:
   https://alainconnes.org/wp-content/uploads/bookwebfinal-2.pdf .
3. J.-F. Burnol, *On Fourier and Zeta(s)*, §2 and the local/global Tate
   discussion, https://arxiv.org/html/math/0112254v6 .
4. A. Connes, *Trace formula in noncommutative geometry and the zeros of the
   Riemann zeta function* (1999), https://arxiv.org/abs/math/9811068 .
5. M. Suzuki, *Weil's quadratic form via the screw function*, v3,
   2026-09-23, §1–2 and Eq. (1.3):
   https://arxiv.org/html/2606.09096v3 .
6. J.-F. Olsen, *Local properties of Hilbert spaces of Dirichlet series*,
   https://arxiv.org/abs/1011.3370 . This is neighboring prior art, not a
   claim that its theorems are identical to W-01/W-02.

## 8. Validation, remaining gap, and next discriminating theorem

`python -m unittest discover -s tests -p 'test_source_faithful_weil.py' -v`
passes **24 tests**. All arithmetic is rational or outward original-source
interval arithmetic. The initial exact-equality expectation for a perfect
square was corrected: the inherited sqrt oracle returns a valid nondegenerate
enclosure, so the calibration must test enclosure rather than equality.
This was a test expectation error, not a tightened or silently modified
source interval. Analytic theorems above remain paper proofs.

The hidden assumption decisively invalidated is that a correct arithmetic
address map can automatically be implemented as a bounded, norm-faithful
Hilbert transport to the continuous log carrier. Crowd density makes the
unweighted version impossible; critical damping repairs boundedness but
discloses norm loss, and exact resolution restores a divergent cost.

The actual remaining source gap is a comparison with the *completed* primitive
high inverse, not the ability to display the correct prime coefficient. A
verdict-changing precise next target is: construct a source-derived family
\(W_\epsilon:\mathbb C^k\to\operatorname{Dom}(D)\) in the original high
space, from the regularized arithmetic map, and prove a **strict source-
certified lower bound** on the directional correction

\[
\kappa^{-1}B^*Z_\epsilon
\bigl(\kappa W_\epsilon^*(D-\kappa I)W_\epsilon+
Z_\epsilon^*Z_\epsilon\bigr)^{-1}
Z_\epsilon^*B,\qquad Z_\epsilon=(D-\kappa I)W_\epsilon,
\]

with \(W_\epsilon^*(D-\kappa I)W_\epsilon>0\), large enough to improve the
existing #181 lower on at least one declared
original low direction after all source/domain/tail errors are charged.
The cheapest legitimate falsifier is one actual source low residual whose
certified overlap with every proposed Z column is zero or whose paid errors
exceed the improvement. The map from log atoms to this primitive high space,
its endpoint/moment constraints, and all completion terms must be proved
first; no finite positive Gram can replace those premises. This target is
strictly smaller than S4 positivity, and S4 positivity on one window is
strictly smaller than the all-support Weil criterion.
