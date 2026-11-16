# A source-attached interference algebra and its complete declared scope

## Authority, source and meaning of completeness

Parent: #643 at 8097d9e802da1d83a615d8812e74279820f5ae7e.
All propositions below are **PROVED within their explicit mathematical
models**, by the displayed arguments or the specifically identified
inherited statements. Code checks are finite and separately recorded.
No physical phase oracle, normality estimate, R0 estimate or new quantum
realization is inferred.

Keep the literal four-pole source
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
Write \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\),
\(Y_n=U_n+T_n=16^n\pi/16\), \(e(t)=\exp(2\pi it)\), and
\[
W_B(h)=\frac1B\sum_{n=B}^{2B-1}e(hY_n),\qquad B\in\mathbb Z_{\ge1}.
\]
Use every sufficiently large integer \(B\), not only powers of two.
The same notation with a superscript U uses the exact rational states.
The inherited source bound is \(0<T_n<1/(64n^2)\) for \(n\ge1\).

There are two completeness statements. IA-01--03 classify a specified
finite algebra of labelled phase responses. The accompanying frontier
catalogue covers the named families in its pinned source inventory.
Neither statement enumerates every future mathematical experiment.
Discontinuous digit predicates, arbitrary nonlinear postprocessing,
infinite kernels and different physical carriers retain separate types.

## IA-01. Finite signed intensity compilation

Let \(z=(z_1,\ldots,z_d)\), \(|z_i|\le1\), be declared accessible channels,
and let \(H=H^*\) have Gaussian-rational entries. Rows act as
\(a z=\sum_i a_i z_i\); the convention is \(z^*Hz\).
There is an exact signed decomposition
\[
z^*Hz=\sum_{\ell=1}^{L}w_\ell |a_\ell z|^2,\qquad
L\le2d^2-d,\qquad \sum_i|a_{\ell i}|\le1.
\tag{1}
\]
The code uses the stronger rational normalization
\(\sum_i(|\Re a_{\ell i}|+|\Im a_{\ell i}|)\le1\).

**Proof.** A diagonal entry contributes \(H_{ii}|z_i|^2\).
For \(i<j\), write \(H_{ij}=a+ib\), \(w=\overline z_i z_j\).
Its contribution is \(2a\Re w-2b\Im w\), and
\[
|z_i+z_j|^2-|z_i-z_j|^2=4\Re w,\qquad
|z_i+iz_j|^2-|z_i-iz_j|^2=-4\Im w.
\]
Normalize each two-channel row by 2 and assign weights
\(+2a,-2a,+2b,-2b\), omitting zero terms. There are at most four
rows per pair and one per diagonal. This proves (1), with
\[
C:=\sum_\ell|w_\ell|
=\sum_i|H_{ii}|+
4\sum_{i<j}(|\Re H_{ij}|+|\Im H_{ij}|).
\tag{2}
\]
No positivity assumption, square root or eigendecomposition is needed.
Conversely every such signed intensity program is the Hermitian form
\(H=\sum_\ell w_\ell a_\ell^*a_\ell\).

An arbitrary complex matrix splits as
\[
K=\frac{K+K^*}{2}+i\,\frac{K-K^*}{2i}.
\]
Thus two signed programs recover the real and imaginary parts of \(z^*Kz\).
Adding a declared reference coordinate \(z_0=1\) also realizes every
Gaussian-rational linear response and its two quadratures.

**Sampling and precision.** If \(C>0\), choose row \(\ell\) with probability
\(|w_\ell|/C\), read a freshly prepared Bernoulli coin with probability
\(|a_\ell z|^2\), and report \(X=C\,\operatorname{sgn}(w_\ell)\,\mathrm{coin}\).
Then \(EX=z^*Hz\), \(|X|\le C\). Independent trials give
\[
\Pr(|\overline X-EX|\ge\epsilon)
\le2\exp[-m\epsilon^2/(2C^2)].
\tag{3}
\]
The exact implementation conservatively replaces the natural logarithm
in the sufficient budget by a binary-log ceiling. The zero program needs
no samples. A uniform intensity error \(\epsilon\) costs at most \(C\epsilon\).
Coordinate turn errors \(\delta_i\), for unit true/perturbed phases, cost
at most
\[
4\pi\sum_\ell |w_\ell|\sum_i|a_{\ell i}|\delta_i,
\tag{4}
\]
by \(|e(x)-e(y)|\le2\pi|x-y|\) and the normalized row bounds.
These are instrument costs, not arithmetic saving estimates.

## IA-02. Finite character closure and the source resonance quotient

In this section every coordinate is a unit phase, \(z_j\in\mathbb T\),
unlike the optional closed-disk domain of IA-01. For a fixed finite list
of source clocks, characters
\(\chi_a(z)=\prod_j z_j^{a_j}\), \(a\in\mathbb Z^d\), are closed under
products and conjugation. Gaussian-rational linear combinations of these
characters are exactly the finite trigonometric-polynomial algebra.
Each complex polynomial is a linear response of a finite lifted character
list, so IA-01 with an explicit reference compiles its two quadratures.
Conversely finite sums, products, conjugation and intensity operations
produce only finite polynomials of that kind.

This is completeness for the declared finite grammar. Lifting characters
requires joint access to their labelled factors. It does not make the
source clocks statistically independent, implement a physical tensor
oracle, or supply a digit predicate without its boundary decision.

For a fixed finite lag word \(P(E)=\sum_{j=0}^d a_jE^j\),
integer polynomial division gives
\[
P(E)=h+(E-16)Q(E),\qquad h=P(16).
\]
The exact, inherited echo identity is
\[
P(E)U_n=hU_n+Q(E)r(n+1),\qquad
P(E)Y_n=hY_n.
\tag{5}
\]
Here \(Q(E)r(n+1)=\sum_jq_jr(n+j+1)\), a finite rational forcing term.
Compensating that known term retains exactly the selected mode \(h\).
All integer tap words with the same \(P(16)\) differ by a multiple of
the recurrence symbol \(E-16\). Words with \(P(16)=0\) are source-only
after rational compensation and erase the seed coordinate.

The correct Haar-initial-phase benchmark for a completed lag character is
\[
\int_0^1 e\!\left(\sum_j a_j16^j x\right)dx
=\mathbf1_{\{P(16)=0\}}.
\tag{6}
\]
For example \(e(Y_{n+1}-16Y_n)\equiv1\), including for a normal orbit.
The lag coordinates are a deterministic orbit graph, not independent
Haar phases. All fixed lag-polynomial averages converge to (6) if and
only if the original orbit is normal: normality pays every fixed
nonzero \(P(16)\), and the one-term words include every fixed mode.

If lags or coefficients grow with \(B\), this argument supplies no
uniform cancellation. Substituting \(U_n\) for \(Y_n\) in a single
reduced high-frequency character costs its actual growing frequency.
Alternatively, a two-time difference transports with the smaller
two-tail cost, as already established by IAD-06. These operations must
not be interchanged.

## IA-03. Exact gauges and which target characters are identifiable

Suppose the declared reports on the full candidate torus are complex
characters with exponent rows generating \(L\le\mathbb Z^d\). Two phase
vectors have identical reports exactly when their ratio lies in
\[
L^\perp=\{g\in\mathbb T^d:\chi_a(g)=1\text{ for every }a\in L\}.
\tag{7}
\]
A target character \(\chi_b\) is determined by those reports for every
candidate phase vector if and only if \(b\in L\).

**Proof.** Membership gives a product of integer powers of the reports.
Conversely use Smith normal form: integer coordinate changes reduce
\(L\) to generators \(d_1e_1,\ldots,d_re_r\). If a coordinate of \(b\)
beyond \(r\) is nonzero, a free circle phase separates it. If
\(d_j\nmid b_j\), a \(d_j\)-th root of unity separates it. Thus
\(b\notin L\) has a nontrivial value on the kernel. This also exposes
finite-index aliases; rational linear span alone is insufficient.
This lattice closure concerns jointly retained pointwise character
values. Products of separately averaged reports do not recover the
average of their product; that requires the corresponding joint channel.

For complex pair reports \(z_i\overline z_j\) on graph edges, the kernel
has one common U(1) phase per connected component. One calibrated phase
reference in each component removes it. On a connected graph, extra
character reports with total charges \(q_1,\ldots,q_s\) leave precisely
the roots of unity of order \(\gcd(|q_1|,\ldots,|q_s|)\); if every
charge is zero the full U(1) remains. A charge-one reference fixes it.
Balanced tensor products do not remove that global gauge.

This torus theorem does not assert that all torus candidates obey BBP.
Inside the same-forcing seed family,
\(U_n(s+\Delta)-U_n(s)=16^n\Delta\). A finite collection of pair
reports \((n,m,h)\) has exact seed kernel
\[
\{\Delta:h(16^n-16^m)\Delta\in\mathbb Z\text{ for every report}\}.
\tag{8}
\]
If at least one coefficient is nonzero, this is \(g^{-1}\mathbb Z\)
where \(g\) is their positive integer gcd. For all consecutive late
clocks \(n\ge n_0\), \(h=1\), pair reports have kernel
\((15\,16^{n_0})^{-1}\mathbb Z\), while individual phase reports have
kernel \(16^{-n_0}\mathbb Z\). The factor 15 is the actual radix
fixed-point global rotation. Unwrapped zero-anchor authentication is
still needed to exclude the remaining rational late-phase aliases.

## IA-04. Reference, pair and lag clicks address different rungs

Let \(I,J\) be independent uniform draws from the same full B-shell,
with replacement, and \(z_n=e(hY_n)\).
A reference phase \(\theta\), in radians, gives the click mean
\[
p_{B,h,\theta}
=E\,\frac{|z_I-e^{i\theta}|^2}{4}
=\frac{1-\Re(e^{-i\theta}W_B(h))}{2}.
\tag{9}
\]
The independent-pair click is
\[
p^{\rm pair}_{B,h}
=E\,\frac{|z_I-z_J|^2}{4}
=\frac{1-|W_B(h)|^2}{2}.
\tag{10}
\]
These are elementary expansions, also present in donor #642.

Consequently:

- R0 is exactly an eventually positive lower bound for (9) at \(h=1\),
  \(\theta=0\).
- R1 is exactly an eventually positive lower bound for (10) at \(h=1\).
- CH and CH_k use oriented (9) at \(h=15\) and \(h=16^k-1\), respectively,
  with fixed k, by the inherited LMF/ZSC rung theorem.
- Full normality is equivalent to (9) tending to 1/2 at both quadratures,
  for every fixed nonzero h; it is also equivalent to (10) tending to 1/2
  for every such h.

Pair data cannot recover R0 orientation. Actual radix fixed points 0 and
1/3 have identical pair reports and \(|W|=1\), but the first fails R0
and the second has \(1-\Re W=3/2\). Sampling with \(I=J\) always gives
zero pair clicks; it is not an independent-pair experiment.

## IA-05. A single Gamma-sampled family contains every Fourier mode

Choose an external clock \(\tau\sim\operatorname{Gamma}(1,\text{scale }1)\),
let \(K\mid\tau\sim\operatorname{Poisson}(\tau)\), and put \(H=K+1\).
Then
\[
\Pr(H=h)=\int_0^\infty
e^{-t}\frac{e^{-t}t^{h-1}}{(h-1)!}\,dt=2^{-h},
\quad h\ge1,\qquad EH=2.
\tag{11}
\]
Independently draw \(I,J\) uniformly from the actual shell and use the
pair click at frequency H. Define
\[
\mathcal E_B=\sum_{h\ge1}2^{-h}|W_B(h)|^2.
\]
Then
\[
\boxed{E[\mathrm{click}]=\frac{1-\mathcal E_B}{2},\qquad
\mathcal E_B\to0\ \Longleftrightarrow\ \pi\text{ is base-16 normal}.}
\tag{12}
\]
**Proof.** Conditional on H, (10) applies; absolute summability permits
the average. If \(\mathcal E_B\to0\), positivity gives
\(|W_B(h)|^2\le2^h\mathcal E_B\) for every fixed h. Conversely first
truncate at fixed h<=L, apply modewise convergence, then bound the
remaining sum by \(2^{-L}\). Negative modes follow by conjugacy. The
all-integer-shell Weyl equivalence is the canonical inherited target.

This is an equivalent criterion, not a new arithmetic saving. Indeed
the *identical energy* is already present in SCE-01:
\[
P_{1/2}(t)=\frac3{5-4\cos(2\pi t)},\qquad
K(t)=\frac{P_{1/2}(t)-1}{2}
=\frac{2\cos(2\pi t)-1}{5-4\cos(2\pi t)},
\]
\[
\mathcal E_B=E_{I,J}K(Y_I-Y_J),\qquad
E_B^{\rm SCE}=1+2\mathcal E_B.
\tag{13}
\]
The current addition is the declared Gamma-sampled click readout and its
source/precision bookkeeping. Characteristic-kernel theory is a further
classical antecedent; see the primary-source audit.

The pointwise kernel lies in [-1/3,1], and its pair click in [0,2/3].
Its empirical product-law energy is nonnegative by the positive Fourier
series. The diagonal is included. No replacement of the actual source
by an independently sampled phase distribution occurs in (12).

## IA-06. Truncation, original-source transfer and consistent observation

For any cutoff L>=0, use the unnormalized partial energy
\[
\mathcal E_{B,L}=\sum_{h=1}^{L}2^{-h}|W_B(h)|^2.
\]
Then exactly
\[
0\le\mathcal E_B-\mathcal E_{B,L}\le2^{-L}.
\tag{14}
\]
Rerolling frequencies above L gives a different normalized law; it
cannot retain (12) without the normalization correction.

For the literal rational and completed sources, the finite first moment
in (11) pays the infinite frequency mixture:
\[
|W_B^U(h)-W_B(h)|\le2\pi h\,\overline T_B,\qquad
\overline T_B=B^{-1}\sum_{n=B}^{2B-1}T_n.
\]
Since both means have modulus at most one,
\[
|\mathcal E_B^U-\mathcal E_B|
\le4\pi\overline T_B\sum_{h\ge1}h2^{-h}
=8\pi\overline T_B
<\frac{\pi}{8B^2}<\frac{11}{28B^2}.
\tag{15}
\]
The click-mean debt is half this bound. This is a genuine uniform
source transfer for the whole mixture, not an unpaid exchange of a
fixed-mode limit and a growing band. It transports no digit indicator.

For a positive integer m, take independent fresh trials of the U-based
detector and let
\(\widehat{\mathcal E}_B=1-2\,\overline{\mathrm{click}}\).
Hoeffding gives
\[
\Pr(|\widehat{\mathcal E}_B-\mathcal E_B^U|\ge\epsilon)
\le2e^{-m\epsilon^2/2}.
\tag{16}
\]
For any \(\epsilon_B>0\) tending to zero and summable
\(0<\delta_B<1\), choose positive integers
\(m_B\ge2\epsilon_B^{-2}\log(2/\delta_B)\).
The union bound and first Borel--Cantelli lemma imply that almost
surely the errors are eventually at most \(\epsilon_B\). Together
with (15), on that probability-one event the observed sequence tends
to zero exactly when the true normality energy does.

This is consistency of an infinite sequence of finite experiments.
It is not a finite decision procedure for normality or a proof that
this source makes the energy vanish. The finite expected harmonic
EH=2 is not a constant-time source-computation claim.

## IA-07. What the master response controls, with its resolution price

For a fixed trigonometric polynomial
\(f(x)=a_0+\sum_{h\ne0}a_he(hx)\), put
\(\rho_h=2^{-|h|-1}\). Since
\(\sum_{h\ne0}\rho_h|W_B(h)|^2=\mathcal E_B\),
Cauchy--Schwarz gives
\[
\left|\int f\,d\nu_B-\int f\,d\lambda\right|
\le
\left(\sum_{h\ne0}\frac{|a_h|^2}{\rho_h}\right)^{1/2}
\sqrt{\mathcal E_B}.
\tag{17}
\]
Thus every fixed finite Fourier experiment has a quantitative readout
bound from this master response. The price grows rapidly with the
highest frequency. A fixed finite polynomial of lag coordinates pulls
back through (5), combining coefficients with the same P(16), and has
the same estimate against the *orbit-graph* Haar benchmark.

For a varying family \(f_B\), the right-hand product in (17) must
actually vanish; normality alone gives no prescribed rate to pay it.
Continuous observables can be approximated by finite polynomials,
which yields their qualitative weak-convergence implication. Uniform
or growing-resolution error bounds need their own approximation costs.
Discontinuous digits require boundary control. An entropy premise or
a restricted Diophantine estimate is not manufactured by (17).

## IA-08. Actual periodic radix sources defeat every finite mode band

Let \(q=3^a5^b\), \(a,b\ge1\), and \(M=q/15\). The actual radix-16
orbit of \(1/q\) has period M and consists exactly of
\[
\left\{\frac{1+15j}{q}:0\le j<M\right\}.
\tag{18}
\]
**Proof.** The elementary lifting identities give
\(\operatorname{ord}_{3^a}(16)=3^{a-1}\) and
\(\operatorname{ord}_{5^b}(16)=5^{b-1}\). Their coprime product is M.
All powers of 16 are 1 modulo 15, and there are exactly M such units
modulo q. Therefore the single orbit fills that coset.

Its complete-period Fourier mean is
\[
\widehat\mu_q(h)=e(h/q)\,\mathbf1_{\{M\mid h\}},
\quad
\mathcal E(\mu_q)=\sum_{j\ge1}2^{-jM}
=\frac1{2^M-1}=:\varepsilon_M.
\tag{19}
\]
Taking M above any prescribed finite mode band makes every tested
nonzero mean exactly zero, while the orbit remains periodic and
nonnormal. Its universal energy is positive but arbitrarily small.
Arbitrary finite shell means converge to these invariant-law means;
the exact formula (19) applies to complete-period sampling.

These controls can be attached to the original forcing by explicitly
changing the seed to \(1/q-\pi/16\); their completed orbit is (18).
They fail the zero-anchor passport and do not refute the original
zero-seed target.

A second actual-orbit control is a repeated base-16 de Bruijn word
of order k. Every word through depth k has exactly its uniform cyclic
frequency, yet some (k+1)-word is absent. There is one orbit point in
each k-digit cell. Coupling each point to uniform mass in its cell
gives \(W_1\le16^{-k}/2\), hence
\[
|\widehat\mu(h)|\le\pi|h|16^{-k},\qquad
\mathcal E(\mu)\le6\pi^2\,16^{-2k}.
\tag{20}
\]
The moment identity \(\sum h^2 2^{-h}=6\) proves the last inequality.
This supplies simultaneous finite-word and finite-frequency impostors
without confusing an arbitrary phase table with a genuine radix orbit.

## IA-09. Retaining the frequency label changes discrimination cost

Consider only the following declared statistical experiment. A rival
is either Haar or the invariant law (18). Each fresh trial chooses
H with law (11), chooses two independent samples from that rival
measure, and reports a pair-click bit. The retained report is either
(H,bit), or just bit. Full phases and sampled source-clock identities
are not part of this report model.

Write \(\varepsilon=\varepsilon_M\). Under Haar the conditional bit
is fair for every H. Under the periodic rival it is identically zero
when M divides H, and fair otherwise. The resonant-frequency probability
is exactly \(\varepsilon\). Direct summation gives
\[
\chi^2(P_{\rm periodic}\Vert P_{\rm Haar})
=\begin{cases}
\varepsilon,&(H,\mathrm{bit})\text{ retained},\\
\varepsilon^2,&\mathrm{bit}\text{ alone}.
\end{cases}
\tag{21}
\]
For m independent trials, \(\chi^2_{\rm product}=(1+\chi^2)^m-1\).
Since total variation is at most \(\sqrt{\chi^2}/2\), equal-prior
testing error at most 1/4 requires
\[
m\ge\frac{\log2}{\log(1+\varepsilon)}
\ge\frac{\log2}{\varepsilon}
\quad\text{or}\quad
m\ge\frac{\log2}{\log(1+\varepsilon^2)}
\ge\frac{\log2}{\varepsilon^2},
\tag{22}
\]
respectively. The code exposes the weaker exact rational strict lower
bounds obtained from \(\log2>2/3\).

With H retained, a resonant-frequency click is impossible under the
periodic rival and has Haar probability \(\varepsilon/2\). Its Haar
miss rate after m trials is \((1-\varepsilon/2)^m\), so fixed error
is attainable at order \(\varepsilon^{-1}\) trials. Without H, a
Bernoulli mean test attains fixed error at order \(\varepsilon^{-2}\).
Thus these two report models have different orders, approximately
\(2^M\) versus \(4^M\).

These are costs for the declared random report and two declared rivals.
Knowing M and choosing H=M, or retaining richer source data, changes
the experiment. No universal pi-computation or proof-complexity bound
is asserted.

## IA-10. Conditional, carry and high-order channels need their couplings

Let a finite source table carry a partition label b with mass \(p_b\),
and a unit complex response Z. Put \(m_b=E[Z\mid b]\) on occupied cells.
Selecting b by \(p_b\), then two conditionally independent source rows
inside that same b, gives the exact pair response
\[
E[Z_1\overline{Z_2}]=\sum_b p_b|m_b|^2.
\tag{23}
\]
Selecting two unconditional independent rows instead gives
\(|\sum_b p_bm_b|^2\). Their difference is the conditional variance
\[
\sum_b p_b|m_b|^2-\left|\sum_b p_bm_b\right|^2
=\sum_b p_b|m_b-EZ|^2\ge0.
\tag{24}
\]
The sampling gluing is part of the observable. Refining to singleton
cells makes (23) equal one even when the unconditional mean cancels.
This explains why a prescribed conditional-energy gate may be stronger
than a signed cross-bin gate; the two cannot be interchanged.

For actual carry/arrival records the coherent decoder
\[
\widetilde C_{N,M}(h)=
\sum_b p_b\,e(h\tau_b/16)\,
E[e(hc_{n+1}/16)\mid b]
\tag{25}
\]
retains the bin-relative phase \(\tau_b=(b+1/2)/M\). Its inherited
comparison to raw Weyl means is recorded in the atlas. With
\(m_b=E[e(hc_{n+1}/16)\mid b]\), Cauchy--Schwarz gives
\[
|\widetilde C_{N,M}(h)|^2\le\sum_b p_b|m_b|^2.
\]
Thus conditional-energy decay implies decoder decay; the reverse
implication fails when nonzero bin means cancel after their phase
transport. Constructing either readout alone proves no decay.
Digit branch boundaries and carry 16 are part of the input contract.

Likewise, for signs a,b with both a-fibers populated, put
\(u_\pm=E[b\mid a=\pm1]\), \(m=Ea\),
\(t=(u_++u_-)/2\), \(\beta=(u_+-u_-)/2\). Then
\[
E[ab]=\beta+mt.
\tag{26}
\]
Balanced a-marginals pay m, not the selected complement contrast beta.
For d binary signs, complete Walsh inversion uses all \(2^d\) characters.
The uniform law and the law conditioned on product +1 agree on every
proper-coordinate marginal but disagree on the full product. Its
tensor interaction must be recorded; an unobserved factorization is
not a source-derived independence theorem.

## IA-11. Signed chronological overlap is a different response type

Let \(H_-,H_+\) be the actual CDF defects of two time blocks under
the sixteen-child future-preserving projector Q. For p,q>=0, p+q=1,
linearity of CDFs and the real identity
\[
|pa+qb|=p|a|+q|b|
-2\min(p|a|,q|b|)\mathbf1_{\{ab<0\}}
\]
give
\[
D_{\rm joined}
=pD_-+qD_+
-2\int_0^1\min(p|H_-|,q|H_+|)
\mathbf1_{\{H_-H_+<0\}}\,dt.
\tag{27}
\]
The equal-block case recovers the inherited Omega overlap identity.
For odd lengths p and q are the actual relative lengths.

On a finite certified phase table, CDFs are finite step functions;
their signed overlap is computable by retaining all breakpoint
weights and signs. This is a finite classical postprocessing
experiment built from certified predicates, not a single quadratic
phase intensity. Its input certification and any asymptotic overlap
gain remain separate. Temporal Haar coefficients, seed-child flux,
source-coordinate Haar details and prime-fiber Haar contrasts must
not be identified merely because each uses a Haar basis.

## IA-12. What the atlas and compiler certify

The compiler proves that every finite response in IA-01--02's declared
phase algebra has an explicit signed measurement construction and
normalization. The lattice theorem identifies exactly which target
characters survive a declared character report. The universal mixture
is an inherited complete normality criterion with a new explicit
Gamma-sampled readout and source-transfer account.

The frontier catalogue separately registers inherited equivalents,
weaker rungs, stronger prescribed-scale gates, conditional transfers,
observer-only constructions, arithmetic auxiliaries and other programs.
Its completeness is checked against its finite pinned source inventory
and reviewed family list. Historical statements with superseded
quantifiers are flagged; the archival originals are preserved.

None of these results supplies the selected all-large-shell bound.
The new information is the response algebra, its exact gauges,
the precise connection between its benchmark and each target, and
the resource/precision debt. To advance the pi proof, one must bound
an authentic response using arithmetic beyond its representation:
for example an R0 reference click rate, the universal energy, a
selected complement contrast, a prescribed conditional interaction,
or a correctly transferred real-cell collision budget.
