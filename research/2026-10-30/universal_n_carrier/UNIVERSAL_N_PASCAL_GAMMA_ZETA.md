# Operation Universal \(\mathbb N\)-Carrier — Pascal, Gamma, Pisot, zeta(-1), prime-place truth and BBP

**Research date:** 2026-10-30. **DRAFT RESEARCH ONLY**; stacked continuation of PR #414 at exact SHA e4773979802cf0ef3a8d46444acb6bc5966788a9, itself stacked on #412/#409/#406/#404/#402/#397 from merged Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5. Adjacent, read-only parallel work: #408 and #413 on Fibonacci/triangle extrusion, #400–#401 prime/Gamma holonomy, #403–#405 signed phase slips, #415 cylinder arithmetic. No original signed four-pole source, U0=0, archival contract, workflows, production, main, or adjacent PR files modified. π base-16 normality and RH remain OPEN.

## 0. Author's original thesis; steelman, not a retrofitted coincidence

The author identifies one mathematical thread constructed through the successor operation on \(\mathbb N\): Pascal counts finite possible paths; Gamma becomes Pascal-like when a continuum-scale latent is observed finitely; Fibonacci/golden and more general Pisot numbers arise from suitable finite recursive composition rules; the finite path reaching \(\zeta(-1)\) and harmonic divergence carries information across the prime arithmetic and archimedean continuation. Build the **carrier independently of BBP**, embed the observer in it, then require a typed source-faithful embedding of the authentic four-pole model. Mathematical source model \(\neq\) physical carrier \(\neq\) observed selected digit history. Claim status must remain separated at each map.

Main new contribution of this round: a single finite \(\mathbb N\)-Dirichlet spine and the **original four-pole logarithmic potential** yield a rigorous finite-to-archimedean/prime transport diamond with exact prime-2 slope and a positive first-jet-matched hostile mutant.

## UN-01. THE finite \(\mathbb N\) Dirichlet spine is not a slogan (EXACT)

For \(N\ge1\), \(s\in\mathbb C\), define the finite entire function
\[
Z_N(s)=\sum_{n=1}^N n^{-s},\qquad Z_{N+1}(s)-Z_N(s)=(N+1)^{-s}.
\]
Its exact finite specializations, all from ONE successor-threaded carrier, are
\[
Z_N(-1)=N(N+1)/2=\binom{N+1}{2},\quad Z_N(0)=N,\quad Z_N(1)=H_N,
\quad -Z_N'(0)=\log(N!)=\log\Gamma(N+1).
\]
For every finite \(N\), prime-factorization/Legendre gives
\[
\boxed{\log\Gamma(N+1)=\sum_{p\le N}\sum_{j\ge1}\lfloor N/p^j\rfloor\log p.}
\]
The derivative at \(s=0\) is performed on the **finite** sum, not by differentiating the divergent infinite Dirichlet series at zero. \(H_N-\log N\to\gamma\), whereas \(Z_N(-1)\to+\infty\). \(\zeta(-1)\) is a separately justified analytic continuation/regularized value. Do NOT commute finite-to-infinite limits with evaluations outside their convergence domain.

### All arithmetic places of ONE Pascal cell (EXACT CLASSICAL)

For \(0\le k\le n\), the archimedean reading and prime-place readings of a single **integer**
\[
B_{n,k}=\binom nk=\frac{\Gamma(n+1)}{\Gamma(k+1)\Gamma(n-k+1)}
\]
satisfy
\[
\boxed{\log B_{n,k}=\sum_p v_p(B_{n,k})\log p,\qquad
\log|B_{n,k}|_\infty+\sum_p\log|B_{n,k}|_p=0.}
\]
Kummer's theorem identifies \(v_p(B_{n,k})\) with the number of carries in base \(p\) when adding \(k+(n-k)=n\); Legendre gives
\[
v_p(B_{n,k})=\sum_{j\ge1}\left(\lfloor n/p^j\rfloor-\lfloor k/p^j\rfloor-\lfloor(n-k)/p^j\rfloor\right).
\]
**Genuine bridge:** finite Pascal counts, Gamma's real size and p-adic carries are EXACT observations of the SAME finite integer. They do not automatically identify with the DIFFERENT literal radix-16 BBP carry \(\kappa_n\) or its real-circle selected phase. Any such map would require a separate proof. Finite exact checks cover all \(n\le31\) and all \(k\), \(p\le29\) with an all-primes identity for \(n<30\).

Primary/official literature: DLMF §5.5 Gamma recurrence https://dlmf.nist.gov/5.5; Kummer/Legendre in Integers 21 (2021) https://community.middlebury.edu/~jschmitt/papers/CaroGirardSchmitt21.pdf; MIT p-adic/product formula notes https://math.mit.edu/classes/18.095/2015IAP/lecture1/padic.pdf.

## UN-02. The UNIVERSAL (source-independent) measure-valued Pascal triangle and extrusion (EXACT)

Let \(\mu\) be an arbitrary finite positive measure on \(t\in[0,1]\) (the declared failure probability). For \(n,m\ge0\), \(0\le j\le m\), define the **per-word measure**
\[
\widetilde{\mathcal M}_{n,m,j}(dt)=t^{n+m-j}(1-t)^j\,\mu(dt)
\]
and its counted grade measure \(\mathcal G_{n,m,j}=\binom mj\widetilde{\mathcal M}_{n,m,j}\).
Then for EVERY such source measure and every admissible index,
\[
\boxed{\widetilde{\mathcal M}_{n+1,m,j}
=\widetilde{\mathcal M}_{n,m+1,j}}
\]
and
\[
\boxed{\mathcal G_{n,m+1,j}
=t\mathcal G_{n,m,j}+(1-t)\mathcal G_{n,m,j-1}}
\]
(with missing grade terms zero). Measure equality is pointwise after multiplying density by the displayed \(t\) functions. The generating function is
\[
\sum_{j=0}^m z^j\mathcal G_{n,m,j}
=t^n[t+(1-t)z]^m\,\mu.
\]
At \(z=1\), the sum is \(t^n\mu\). At fixed \(j\), the **counting quotient** divides out \(\binom mj\) before comparing the \(n+1\) and \(m+1\) routes. The counted grade measures themselves are NOT equal across the two routes unless the binomial factors coincide. Chronology must remain in an external path record when actually observed.

**Authentic BBP embedding:** take \(t=e^{-8x}\), \(\mu(dx)=e^{-x}Q(x)dx\), source \(Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}\). Replace abstract n by \(n-1\): the word measure becomes
\[
e^{-[8n-7+8(m-j)]x}Q(x)(1-e^{-8x})^jdx,
\]
exactly the archived source-native Pascal posterior. This is a **type-correct commuting square** from the general \(\mathbb N\) carrier to BBP's positive latent observation model. It does NOT supply a law for the selected signed digit sequence \(U_n(0)\). A history-conditioned nonexchangeable binary observer has the same unweighted Pascal counts but is not sufficient under the grade-only quotient; an explicit finite rational counterexample is tested.

## UN-03. Zooming Gamma through finite counts gives Pascal exactly (CLASSICAL + AUTHENTIC LIMIT)

Suppose the source's density is \(Q(x)\sim c x^{r-1}\) as \(x\downarrow0\), \(r,c>0\), and ordinary integrable-dominating hypotheses hold. With \(\mu_a(dx)\propto e^{-ax}Q(x)dx\) and \(Y=aX\), then \(Y\Rightarrow\Gamma(r,1)\). Let the observer perform \(m(a)\) Bernoulli trials with success \(p(x)=1-e^{-hx}\) and \(hm(a)/a\to\theta>0\). Conditional on \(Y\), the count converges to \(\mathrm{Pois}(\theta Y)\), and after mixing
\[
\boxed{\Pr(J=j)=\frac{\Gamma(r+j)}{\Gamma(r)j!}
\frac{\theta^j}{(1+\theta)^{r+j}}.}
\]
For integer \(r\), the Gamma quotient is the literal stars-and-bars/Pascal coefficient \(\binom{r+j-1}{j}\). For noninteger \(r\), it remains a positive **analytic continuation coefficient**, not a cardinality of finite paths. Source/local-scale rank is NOT a claim that every integer carrier has one unique continuum limit.

For authentic BBP, \(Q(x)=15x-\frac{59}{2}x^2+\frac{243}{6}x^3+\cdots\); therefore \(r=2\), and at native \(\theta=1\), \(\Pr(J=j)=(j+1)/2^{j+2}\), PGF \(G(z)=(2-z)^{-2}\). Independent direct positive-source integral and Gamma–Poisson numerical controls passed.

## UN-04. The GOLDEN/PISOT finite path branch and its exact scope

Fibonacci tiling along Pascal diagonals gives, for all \(n\ge0\),
\[
\boxed{\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}k=F_{n+1},\quad
\sum_{n\ge0}F_{n+1}z^n=(1-z-z^2)^{-1}.}
\]
The transfer/recurrence characteristic polynomial \(x^2-x-1\) has roots \(\varphi\) and \(-\varphi^{-1}\), with the latter contracting; its trace
\(\varphi^n+(-\varphi^{-1})^n=L_n\in\mathbb Z\) is a concrete Pisot near-integer mechanism. Higher multinacci recurrences built from compositions with parts \(1,\ldots,m\) yield other Pisot characteristic roots (classical family, not a result peculiar to SUCC).

**Hostile non-Pisot finite counting recursion:** one singleton or THREE distinguishable double-length tiles gives \(a_n=a_{n-1}+3a_{n-2}\) and polynomial \(x^2-x-3\). Its dominant eigenvalue \((1+\sqrt{13})/2>1\), but its conjugate \((1-\sqrt{13})/2<-1\) has modulus >1. Finite recursive counting does NOT force Pisot behavior; specific path composition is load-bearing.

The Gamma rank/clock family \(G_{r,\theta}(z)=[1+\theta(1-z)]^{-r}\) has a distinguished golden-mark locus, with \(\lambda=\varphi^{-1}\):
\[
\boxed{q=\lambda^r\text{ is fixed}\iff\theta=\frac{\lambda}{1-\lambda^r}.}
\]
On the native clock slice \(\theta=1\), the locus intersects ONLY at \(r=2\), giving \(q=\lambda^2\). Harmonic/Gamma readout \(\psi(r)=H_{r-1}-\gamma\) for integer \(r\), together with \(\mathbb E e^{-\lambda Y}=(1+\lambda)^{-r}=\lambda^r\), produces the graded SUCC Oily contrast \(H_{r-1}-\gamma-\lambda^r\); at \(r=2\), \(\lambda-\gamma\). Thus this is an exact coherent triangle **once** the rank/clock and observable are declared. The golden root is not magically attached to every Pascal row or every positive source.

Overlapping Fibonacci developments in PRs #408/#413 are prior SUCC provenance; this dossier does not claim novelty or silently incorporate their branch ancestors.

## UN-05. Analytic zeta(-1) is an ARCHIMEDEAN TRANSPORT, not infinite addition

For finite \(N\), \(Z_N(-1)=N(N+1)/2\) diverges as \(N\to\infty\). A declared heat regulator gives
\[
\sum_{n\ge1}n e^{-\epsilon n}
=\frac{e^{-\epsilon}}{(1-e^{-\epsilon})^2}
=\epsilon^{-2}-\frac1{12}+\frac{\epsilon^2}{240}+O(\epsilon^4).
\]
The constant is \(-1/12=\zeta(-1)\) for this canonical regulator/analytic continuation, but NOT the ordinary sum of integers. Scheme comparison: multiplying the kernel by \(1+c\epsilon^2\) changes the finite constant to \(c-1/12\). Finite parts require an explicit normalization. At \(s=1\), sharp harmonic cutoff gives \(H_N-\log N\to\gamma\), whereas exponential harmonic smoothing \(\sum_{n\ge1}e^{-\epsilon n}/n+\log\epsilon\to0\). Do not identify regulator-dependent constants.

DLMF Riemann functional equation and Euler product (the latter ONLY for \(\Re s>1\)) give
\[
\boxed{\zeta(-1)=-\frac{\zeta(2)}{2\pi^2}
=-\frac1{2\pi^2}\prod_p(1-p^{-2})^{-1}.}
\]
The \(\Gamma/\pi\) factor is the **archimedean completion** carrying the convergent prime product at \(s=2\) to the continued value at \(s=-1\). The product \(\prod_p(1-p)^{-1}\) or naive \(s=-1\) Euler product does NOT converge and is NOT used. In completed form \(\pi^{1/2}\Gamma(-1/2)\zeta(-1)=\pi^{-1}\Gamma(1)\zeta(2)=\pi/6\).

Primary sources: DLMF §§25.2,25.4,25.5,25.6 https://dlmf.nist.gov/25.2 https://dlmf.nist.gov/25.4 https://dlmf.nist.gov/25.5 https://dlmf.nist.gov/25.6; Bernoulli generating function https://dlmf.nist.gov/24.2; gamma Stirling https://dlmf.nist.gov/5.11.

## UN-06. NEW-to-SUCC original four-pole ARITHMETIC/GAMMA potential bridge (EXACT)

The authenticated forcing is
\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\]
Observe the completely exact fact:
\[
\boxed{R(a)=\partial_a\log\mathcal V(a),\qquad
\mathcal V(a)=\frac{a^4}{(a+3)^2(a+4)(a+5)}.}
\]
The four signed original poles are **the logarithmic derivative of one rational carrier potential**. Every factor \(\mathcal V(8n-7)\) is a strictly positive rational. Let
\[
\mathcal P_N(u)=\prod_{n=1}^N\mathcal V(8n-7+u),\quad u>-1.
\]
Its exact continuous-shift derivative is
\[
\boxed{\partial_u\log\mathcal P_N(u)=\sum_{n=1}^N R(8n-7+u).}
\]
This gives the N-source path a natural continuous variation with a pinned observable, without changing the actual source.

Let \(c=(4,-2,-1,-1)\), shifts \(d=(0,3,4,5)\) and \(q_i(u)=(1+d_i+u)/8\). Their sum \(\sum c_i=0\) and weighted shift sum \(\sum c_i q_i(u)=-15/8\). Gamma recurrence yields the **exact finite identity**
\[
\boxed{
\mathcal P_N(u)=\prod_{i=0}^{3}
\left[\frac{\Gamma(N+q_i(u))}{\Gamma(q_i(u))}\right]^{c_i}.
}
\]
In particular the original \(\mathcal P_N=\mathcal P_N(0)\) has
\[
\boxed{\mathcal P_N=C_{\rm BBP}N^{-15/8}(1+O(N^{-1})),\qquad
C_{\rm BBP}=\frac{\Gamma(1/2)^2\Gamma(5/8)\Gamma(3/4)}{\Gamma(1/8)^4}>0.}
\]
The exponent \(15/8\) comes from the original SOURCE first jet \(Q'(0)=15\) divided by the native age step 8. Independently, \(Q''(0)=-59\), \(Q'''(0)=243\); equivalently the rational-potential Laurent series begins
\(\log\mathcal V(a)=-15/a+59/(2a^2)-81/a^3+\cdots\).
The first exact gamma-quotient constant is approximately \(0.00171415831468372017104\).

Define \(C(u)=\prod_i\Gamma(q_i(u))^{-c_i}\). Since the \(N\)-power exponent is independent of \(u\), differentiation of the limit gives
\[
\boxed{
\frac{d}{du}\log C(u)\Big|_{u=0}
=-\frac18\sum_i c_i\psi(q_i(0))
=\sum_{n\ge1}R(8n-7)=S_R.
}
\]
Numerically \(S_R\approx3.38604761959719172\). DLMF's Lerch/Hurwitz identity \(\zeta'(0,q)=\log\Gamma(q)-\tfrac12\log(2\pi)\) gives the further exact archimedean representation
\[
\boxed{\log C_{\rm BBP}=-\sum_i c_i\,\zeta'(0,q_i).}
\]
Because \(\sum_i c_i=0\), the \(\frac12\log(2\pi)\) terms cancel. This is a **source-authenticated finite→Gamma→Hurwitz zeta construction**, not a zeta-regularized statement about the selected π digit law. The original SUCC Green memory constant is \((S_R-\pi)/15\approx0.01629699773382656556\); its BBP origin remains an independent arithmetic identity.

Primary sources: DLMF gamma recurrence/multiplication §5.5 https://dlmf.nist.gov/5.5; Stirling gamma ratios §5.11 https://dlmf.nist.gov/5.11; Hurwitz \(\zeta'(0,q)\) §25.11.18 https://dlmf.nist.gov/25.11.

## UN-07. EXACT all-prime signature of the very same BBP gamma quotient, and a nontrivial mutant firewall

Since \(\mathcal P_N\in\mathbb Q_{>0}\), for every finite \(N\)
\[
\boxed{\log\mathcal P_N=\sum_p v_p(\mathcal P_N)\log p,\qquad
|\mathcal P_N|_\infty\prod_p|\mathcal P_N|_p=1.}
\]
At \(a_n=8n-7\), the integer factors have valuations
\[
v_2(a_n)=0,\quad v_2(a_n+3)=2,\quad v_2(a_n+4)=0,\quad v_2(a_n+5)=1.
\]
Thus, EXACTLY for ALL \(N\ge1\),
\[
\boxed{v_2(\mathcal P_N)=-5N.}
\]
The other odd prime places must collectively compensate this linear nonarchimedean slope while the archimedean size decays polynomially:
\[
\boxed{\sum_{p\ \mathrm{odd}}v_p(\mathcal P_N)\log p
=5N\log2-\frac{15}8\log N+\log C_{\rm BBP}+O(N^{-1}).}
\]
This statement is an exact finite product formula plus a classical archimedean asymptotic. It does NOT require a nonconvergent infinite p-adic product or moving all prime limits inside one sum.

**Hostile first-jet-matched, positive mutant:** the source-coefficient perturbation \(c'=c+(1,-3,1,1)=(5,-5,0,0)\) gives
\[
Q_{\rm mut}(x)=5(1-e^{-3x})>0,\quad
R_{\rm mut}(a)=\frac5a-\frac5{a+3},\quad
\mathcal V_{\rm mut}(a)=\left(\frac{a}{a+3}\right)^5.
\]
It matches \(Q'_{\rm mut}(0)=Q'_{\rm BBP}(0)=15\) and the same Gamma-rank 2 and native \(\theta=1\) GOLDEN/OILY limiting law. Its \(Q''_{\rm mut}(0)=-45\ne-59\). Its real normalized Gamma potential has the SAME exponent \(-15/8\), but
\[
\boxed{v_2(\mathcal P_N^{\rm mut})=-10N\ne-5N.}
\]
**Verdict:** the universal Pascal/Gamma/golden carrier does NOT determine the original four-pole prime-place realization. The original source-specific threading enters through the poles, their prime valuations and their higher jets. The mutant also shares universal counting and does not prove or refute π's selected digit distribution.

The 2,3,5 exceptional prime set from the authentic rational map's resultant/discriminant is a DIFFERENT statement from all primes dividing the rational products \(\mathcal P_N\); there is no assertion that only 2,3,5 divide \(\mathcal P_N\).

## UN-08. Observer embedded in the universal carrier; proof transfer firewall

**Physical/semantic architecture:** Construct the universal \(\mathbb N\) path category and its count-normalized measure-valued triangle first. Embed a finite observer as a constrained path/fiber with explicit readout and external history ledger. Specialize to BBP through an exact typed source map \((t,\mu)=(e^{-8x},e^{-x}Q(x)dx)\), then attach the independent selected real-circle signed recurrence \(U_{n+1}=16U_n+R(8n+1),U_0=0\). The positive triangle alone is NOT the selected sign. A statement about generic Pascal–Gamma probability observables does not automatically transfer to \(\pi\)'s digit orbit.

**Truth/provenance gates** (must remain separate):
(1) universal path/combinatorial identity;
(2) positive source representation and source authentication;
(3) signed original selected orbit and literal integer carry;
(4) a source- and zero-seed-specific all-horizon estimate;
(5) target theorem (normality or Weil/RH).
Commutative positive diagrams through (1)–(2) do not supply (3)–(4). A finite observer cannot inertially contain all realized carrier degrees; storing a finite program plus externally certified observation history is allowed.

**Nearest verdict-changing probe:** find a source-to-selected theorem involving the authentic 2-adic slope \(-5N\), odd-prime compensation, and real-circle integer carry/CRT distribution that fails for the rank-2 mutant slope \(-10N\) and the same-forcing coherent counterseed \(-\pi/16\). Merely inserting \(\mathcal P_N\), \(\Gamma\), or all-prime factorization into a positive posterior gives a source-only invariant, not selected Weyl saving. Compare Stoneham 3/5 normal controls, 2 nonnormal, dense nonnormal irrational controls, q6/four-bit Walsh, and exact BBP phases. No new asymptotic digit-cancellation bound was found.

## UN-09. NEW: The *authentic zero-seeded signed recurrence* is the log derivative of a finite RATIONAL \(\mathbb N\)-carrier (EXACT)

The unweighted source product \(\mathcal P_N\) is naturally linked to Gamma/archimedean scale. The actual BBP time law is a **different, but canonically source/base-locked multiplicative observation** of the same \(\mathcal V(a)\). For \(u>-1\) set
\[
\boxed{\mathscr B_0(u)=1,\qquad
\mathscr B_{N+1}(u)=\mathscr B_N(u)^{16}\,\mathcal V(8(N+1)-7+u).}
\]
Thus
\[
\mathscr B_N(u)=\prod_{n=1}^N\mathcal V(8n-7+u)^{16^{N-n}}
\]
is a finite positive rational at \(u=0\), composed by the successor operation on \(\mathbb N\). Define the **selected infinitesimal response**
\[
\boxed{U_N=\left.\partial_u\log\mathscr B_N(u)\right|_{u=0}.}
\]
Differentiating, and using the exact four-pole identity \(R=\partial_a\log\mathcal V\), proves
\[
U_0=0,\qquad U_{N+1}=16U_N+R(8(N+1)-7).
\]
This is EXACTLY the original, *unwrapped*, signed zero-seeded BBP recurrence, including its original source rather than a Gamma surrogate or a fitted positive random digit law. The literal integer carries remain extractable from \(U_N\), and the selected circle state remains \(\{U_N\}\). The finite history is not averaged or randomized.

The normalized derivative gives the exact finite BBP partial sum:
\[
\boxed{
16^{-N}\partial_u\log\mathscr B_N(u)|_{u=0}
=\sum_{n=1}^N16^{-n}R(8n-7)
\underset{N\to\infty}{\longrightarrow}\frac\pi{16}.}
\]
The limit equality is the **known BBP identity rewritten in carrier-response form**, NOT an independent proof of π normality or an independently obtained π formula.

### Its finite gamma-factor decomposition by discrete Abel summation (EXACT)

Let \(\mathcal P_j(u)=\prod_{n=1}^j\mathcal V(8n-7+u)\), \(\mathcal P_0=1\). Repeatedly using the ordinary finite Abel summation identity yields
\[
\boxed{
\mathscr B_N(u)=\mathcal P_N(u)\prod_{j=1}^{N-1}
\mathcal P_j(u)^{15\,16^{N-j-1}}.
}
\]
Every \(\mathcal P_j(u)\) has the Gamma quotient from UN-06. This is an EXACT **composition route from finite Gamma-factor products to the authentic, realized BBP time extrusion**. It is not the same as assuming π digits are sampled from a Gamma–Poisson observer.

At the prime-2 place,
\[
\boxed{
v_2(\mathscr B_N(0))
=-5\sum_{n=1}^N16^{N-n}
=-\frac{16^N-1}{3}.
}
\]
For the positive first-jet-matched source mutant \(Q_{\rm mut}=5(1-e^{-3x})\), the identical construction has
\[
v_2(\mathscr B_N^{\rm mut}(0))=-\frac{2(16^N-1)}{3}.
\]
These exact all-N identities detect genuine source-specific prime-place distinctions even though both sources have the same rank-two Gamma/Pascal/golden limit.

### No-discard / model adequacy counterexample: pointwise carrier values do NOT fix the seed

The initial *function* \(\mathscr B_0(u)\equiv1\) carries a marked first-jet boundary. To see why that matters, for any sufficiently small real/rational seed \(s\) take an alternative initial deformation \(g_s(u)=1+su\), positive on a neighborhood of \(u=0\), and define
\[
\mathscr B_N^{(s)}(u)=g_s(u)^{16^N}\mathscr B_N(u).
\]
It obeys the SAME multiplicative update, has \(\mathscr B_N^{(s)}(0)=\mathscr B_N(0)\) for EVERY N and hence the SAME finite rational prime valuations at \(u=0\), but
\[
\boxed{
\partial_u\log\mathscr B_N^{(s)}(u)|_{u=0}
=U_N(0)+16^Ns=U_N(s).
}
\]
Thus the initial zero **derivative/preparation**, not just the finite pointwise potential, selects the authentic BBP realization. This is an exact counterexample to inferential shortcuts that recover the original seed from source potential values, prime valuations, or positive Gamma/Pascal snapshots alone. The coherent changed-seed \(-\pi/16\) is captured by \(s=-\pi/16\) on a suitable small u-neighborhood.

**Archimedean versus p-adic differentiation firewall:** \(\partial_u\log\mathscr B_N(u)\) is an ordinary real analytic derivative. The prime-valuations identity for rational \(\mathscr B_N(0)\) is discrete; **do not differentiate \(v_p\)** with respect to real u as though it were smooth. Cross-place prime-to-selected transport still needs an independently defined common finite-difference/adelic instrument. This is where π normality remains dark.

**Validation:** exact rational 4-stage multiplicative recurrence, \(\log\)-derivative from original R, Abel product decomposition, valuation slope \(-(16^N-1)/3\), mutant slope and all-seed affine first-jet countermodel checked locally, with 17/17 expanded symbolic/finite tests PASS; no infinite signed density inference.

## UN-10. Extension from \(\mathbb N\) to \(\mathbb Z\) is NOT a free quotient (EXACT signed controls)

For integer index symmetry, the **even** bilateral finite carrier (zero excluded) is
\[
\sum_{n=-N,\ n\ne0}^{N}|n|^{-s}=2Z_N(s),
\]
whereas the signed/odd bilateral counterpart cancels to zero for every finite N:
\[
\sum_{n=-N}^{N}n=0.
\]
Thus symmetrizing \(\mathbb N\) to \(\mathbb Z\) before selecting parity/orientation would erase the positive triangular sum \(Z_N(-1)=N(N+1)/2\). Also \(0^{-s}\) is not defined for general \(s\), so the integer origin needs a declared boundary/exclusion.

The Gamma-defined generalized binomial is \(\binom{-1}j=(-1)^j\): a valid algebraic continuation to negative index, but no longer a nonnegative finite path **count**. Building the signed \(\mathbb Z\) carrier therefore requires oriented edges, explicit sign/branch data and a stated positive-versus-signed observation law. This is particularly important before identifying the BBP signed four-pole arithmetic with its positive latent Gamma/Pascal observer. An unqualified \(\mathbb Z\)-extension is NOT a preservation of the original finite counting category.

## Claim status and validation

- **DISCLOSED/EXACT:** finite Dirichlet successor specializations; Pascal/prime/Kummer product; universal word-level measure-valued triangle, count normalization and diagonal; log-derivative source potential, finite Gamma quotient, 2-adic \(-5N\), positive mutant \(-10N\); finite classical zeta functional equation evaluation.
- **CLASSICAL conditional limit:** Gamma–Poisson → negative-binomial/Pascal; golden fixed-point locus; Stirling/Hurwitz archimedean bridge; Euler product/functional equation; Pisot properties of selected recurrences.
- **REFUTED as universal implications:** all recursive finite counts Pisot; all positive sources rank2 or uniquely golden; \(\sum n=\zeta(-1)\) as ordinary sums; termwise Euler product at \(-1\); universal source-only Gamma/Pascal implies \(\pi\) normal; all arithmetic carries identical across places.
- **UNVERIFIED:** universal physical spacetime interpretation, a canonical all-places completed object selecting π's actual zero seed and normality, RH, a genuinely new signed selected Weyl/occupation estimate.
- **Executed local:** 17/17 exact/symbolic first-probe tests; 6/6 general measure-valued triangle exact Fraction tests; independent 85-digit direct original-Laplace/Gamma-product/finite-prime/Gamma–Poisson, source-mutant and functional-equation oracle PASS after correcting numerical Hurwitz derivative precision (see validation). Full SUCC root provenance/unit suite, Lean, hosted exact-head CI and external referee NOT RUN.

This is mathematical stitching with explicit type contracts, not an assertion of physics, a brand-new classical theorem or completion of the RH/π-normality program.
