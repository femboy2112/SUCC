# Oscillator-driven Yoneda–Fourier pin-bed: carrier-relative truth

**Research note — 2026-11-07 — source parent main@d32342d375f44ddf62221ad6aff2f534abdc0a03 — DRAFT.**

**Scope:** exact finite cyclic arithmetic / classical harmonic analysis / observer quotient. No physical experiment, independent referee, formal Lean verification or priority claim. Frozen four-pole BBP source and literal zero seed are unchanged. **π base-16 normality OPEN; selected signed Weyl cancellation OPEN; RH OPEN.**

## 1. The observer and its truth contract

The observer cannot necessarily represent the inaccessible carrier directly. It builds a responsive surface of metal-like pins. A selected family of lawful tests determines a *profile*; coherent oscillators can actively modulate the probes. For an authenticated carrier C and a candidate M, define

\[
M\equiv_{\mathcal P}C \iff (\forall p\in\mathcal P)\ p(M)=p(C).
\]

**Observation-equivalence is itself a valid, exactly scoped truth output.** It is not universal identity; adequate source provenance, permission to perform the probes, and a sufficiently complete model class remain independent obligations.

**PBFO-01 (CLASSICAL, PROVED LOCAL):** If a specified observation map is \(\Phi:S\to O\), a target \(q:S\to T\) descends to an observable truth \(\bar q:\Phi(S)\to T\) with \(q=\bar q\circ\Phi\) **iff** q is constant on every fiber of Phi. Proof: factorization implies fiber constancy; conversely define \(\bar q(\Phi(s))=q(s)\), which is well-defined and unique on the observed image exactly under this condition. Report separately **INDISTINGUISHABLE_RELATIVE_TO_DECLARED_PINS** and **TARGET_DETERMINED_ON_DECLARED_FIBER**; failure to determine q is not a refutation of q.

## 2. The finite pin surface and Fibonacci ladder

Let \(G_m=\mathbb Z/m\mathbb Z\), \(V=\mathbb Q^{G_m}\), and let \(v\) be a signed vector, or a probability when all coordinates are nonnegative and sum to 1. For \(1\le L\le m\), the translated window profile is

\[
P_Lv(y)=\sum_{j=0}^{L-1} v(y+j),\quad y\in G_m.
\]

**PBFO-02 (PROVED):** With all translated locations, \(\dim\ker P_L=\gcd(m,L)-1\). Proof: if \(P_Lv=0\), subtract consecutive outputs to get \(v(y+L)=v(y)\); the input is constant on each of \(d=\gcd(m,L)\) residue cycles. Every length-L window contains L/d points from each cycle, leaving exactly one equation on the d cycle values. Consequently \(P_L\) is invertible over Q iff gcd(m,L)=1. A constructive inverse walks the +L cycle using \(P_Lv(y+1)-P_Lv(y)=v(y+L)-v(y)\) and fixes the additive constant by \(\sum P_Lv=L\sum v\).

**PBFO-03 (PROVED):** For probability v and gcd(m,L)=1, if \(\epsilon=\max_y |P_Lv(y)-L/m|\), then \(\max_j|v(j)-1/m|\le2(m-1)\epsilon\). Adjacent values along the +L cycle differ by at most 2ε, and the mean is 1/m. **The bound deteriorates with m**: finite identifiability does not prove stable asymptotic reconstruction.

For \((m_k,L_k)=(F_{k+1},F_k)\), k≥2 (grids 2,3,5,8,13,...), consecutive Fibonacci numbers are coprime and \(L_k/m_k\to\varphi^{-1}\). This is a *chosen golden probe aperture*, not an intrinsic golden BBP source intertwiner or a consequence of π-normality.

## 3. Drive the sheet with oscillators

For \(\zeta_m=e^{2\pi i/m}\) and coherent mode k, actively modulate the local pin weights:

\[
R_{L,k}v(y)=\sum_{j=0}^{L-1}v(y+j)\zeta_m^{-kj}.
\]

This complex measurement requires **two quadratures and a calibrated phase reference**. With \(\widehat v(q)=\sum_yv(y)\zeta_m^{-qy}\), one obtains

\[
\widehat{R_{L,k}v}(q)=\widehat v(q)H_L(q-k),
\qquad H_L(r)=\sum_{j=0}^{L-1}\zeta_m^{rj}.
\]

The multiplier vanishes exactly if \(r\not\equiv0\pmod m\) and \(m\mid rL\).

**PBFO-04 (PROVED — two-tone repair):** If m≥2 and **1≤L<m**, observing **all translated locations** with oscillator menu **k=0,1** reconstructs *every* complex m-site signal. A Fourier frequency q lost by both channels would require \(m\mid qL\) and \(m\mid(q-1)L\), so \(m\mid L\), a contradiction. One additional coherent tone removes every blind Fourier mode of a proper rectangular moving window. A *single fixed pin* without translated access is not covered.

**PBFO-05 (PROVED):** At L=m, a static full-footprint pin reads only total mass, but the *same fixed collector* driven through k=0,...,m−1 reads the complete DFT \(\widehat v(k)\), and inversion recovers v. This is classical phase-coherent Fourier tomography, not arithmetic cancellation.

**PBFO-06 (REFUTED phase-free shortcut):** On the eight-site carrier, probabilities uniform on distinct supports A={0,1,2,5} and B={0,1,3,4} have identical full cyclic autocorrelation \((4,2,1,2,2,2,1,2)/16\), hence equal **Fourier power spectra at all modes**, but distinct complex Fourier responses. Their supports are not related by any translation or reflection. Intensity alone is an insufficient probe; coherent phase is load-bearing.

## 4. Drive closure, naturality, and a stronger truth certificate

Let the lawful dynamics be affine maps \(T_a:G_m\to G_m\); they need not be invertible (e.g. ×16 mod m). On state vectors, push forward mass; on readout functions pull back. The exact naturality law is

\[
\langle f,(T_a)_*v\rangle=\langle f\circ T_a,v\rangle.
\]

A pulled-back rectangular oscillating window may become a *nonrectangular* mask: **actual availability and source-realization cannot be inferred merely from algebraic commutation.**

**PBFO-07 (PROVED — stable dynamical quotient):** Let E₀ be the Q-row space of the declared oscillator/pin outcomes (expand algebraic outputs into a Q-basis) and set \(E_{t+1}=E_t+\sum_a T_a^*E_t\). Because \(\dim V=m\), the row space stabilizes after at most \(m-\dim E_0\) strict rank increases, and equality of two consecutive spans certifies closure. With \(E_\infty\) the closure, define \(v\sim w\) iff every row in \(E_\infty\) annihilates \(v-w\). Then \(v\sim w\Rightarrow (T_a)_*v\sim(T_a)_*w\) for all lawful actions, and hence for all finite action words. The observer has a true **dynamically stable observational equivalence relation**, even when it lacks full reconstruction.

Hostile witness: m=6,L=3 has nonidentical probabilities with *identical* static complete surfaces, but their surfaces differ after the abstract ×16 mod6 pushforward. Static equality is not a dynamic congruence. Separately, one fixed L=3 pin using tones 0 and 1 becomes full-rank if an **independently permitted** +1 carrier translation moves all positions through the collector. A synthetic cyclic +1 action is not claimed to be an intervention on the authentic BBP recurrence.

**PBFO-08 (PROVED — all-probability linear truth criterion):** For a linear claim \(q(v)=\ell\cdot v\), q is constant on *every* fiber of the closed response map on the **whole probability simplex** iff

\[
\ell\in E_\infty+\mathrm{span}_{\mathbb Q}\{(1,\ldots,1)\}.
\]

Sufficiency uses annihilation of input differences and preservation of total mass. Necessity: outside this row span, choose a rational zero-mass d annihilated by all readings but not ℓ; small rational perturbations of the interior uniform probability u±εd remain valid probabilities, give the same complete readings, and yield different q. This certifies an actual **carrier-relative truth output for the declared whole finite simplex**. At a special boundary fiber a claim might still be determined even when this universal test fails.

**PBFO-09 (PROVED additive-drive no-go):** For two candidates under the **same** known linear dynamics \(v_{t+1}=Tv_t+Bu_t\) with the same additive oscillatory waveform uₜ, their difference obeys \(\delta_{t+1}=T\delta_t\). The output difference \(C_tT^t\delta_0\) does **not** depend on the common known input. A bigger additive drive alone cannot open a fixed initial-state blind space; changes to the probe C, lawful nonlinear/state-coupled dynamics, or complementary phase-coherent tests must supply the information.

## 5. Where Yoneda genuinely enters

For a locally small category C, the restricted Yoneda nerve \(Y_{\mathcal P}(X)=\operatorname{Hom}_C(-,X)|_{\mathcal P}\) is fully faithful when the context subcategory is **dense** ([Kerodon §8.4.1](https://kerodon.net/tag/03V8)). Our finite pin map is an **observation representation**, not by itself an authenticated Yoneda embedding. Define actual category objects/arrows, test identities/composition/naturality and physical/source realizations; reuse SUCC's existing operational_yoneda_descent and yoneda.FiniteFunctor spine.

Illustration: in finite-dimensional Q-vector spaces, the full probe subcategory on Q and Q² is dense. Natural transformations on representable restrictions are forced to commute with scalars by the endomorphisms of Q and with addition by the diagonal Q→Q² and the coordinate maps. Thus these are exactly the linear maps. **Probe relationships constrain truth, not merely the numerical readings.**

## 6. Infinite measure profile and the frozen BBP proof gate

**PBFO-10 (PROVED, classical):** For a Borel probability μ on the circle let \(B_k(\mu)\) be its masses on the m_k equal half-open bins and \(\Psi_k(\mu)=P_{L_k} B_k(\mu)\). The map \(\mu\mapsto(\Psi_k(\mu))_{k\ge2}\) is injective: finite coprime inverses recover all bin masses; as the Fibonacci meshes shrink, uniform approximation of every continuous function by bin-step samples implies equal integrals against μ and ν; hence μ=ν. **Finite** initial ladders still alias different measures (e.g. masses at 1/5 and 21/100).

The source contract remains

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad x_n=\{U_n\}.
\]

Set \(\mu_A=A^{-1}\sum_{n=A}^{2A-1}\delta_{x_n}\). Using the maintained BBP Green-tail/Weyl bridge in [the π frontier](../../../docs/PI_NORMALITY_FRONTIER.md):

\[
\boxed{\pi\text{ base-16 normal}\iff
\forall k\ge2:\ 
\max_y|\Psi_k(\mu_A)(y)-L_k/m_k|\to0 \ (A\to\infty).}
\]

This is an **EQUIVALENT-REFORMULATION — convergence OPEN**, not an asymptotic estimate. Each fixed-k bin has the Haar-boundary continuity needed for the forward implication; conversely arbitrarily fine fixed-k bin uniformity forces weak Haar convergence.

**PBFO-11 (PROVED, deterministic binning):** Let \(b_{A,m}(j)\) be the exact empirical bin probabilities and \(W_{A,m}(h)=\sum_jb_{A,m}(j)e^{2\pi i h j/m}\). For any integer h, every A,m≥1,

\[
\left|A^{-1}\sum_{n=A}^{2A-1}e^{2\pi ihU_n}-W_{A,m}(h)\right|\le 2\pi |h|/m,
\]

because each phase differs from its lower bin endpoint by less than 1/m. A **source-selected** all-epoch decay theorem \(W_{A,m(A)}(h)\to0\) with \(m(A)\to\infty\) at fixed nonzero h would imply normality. The required signed estimate is **OPEN**. Do not rotate the observer origin independently and mistake an artificial scan for real source uniformity.

## 7. Validation and next discriminating test

Isolated local Python 3.13 implementation with exact Fraction / cyclotomic arithmetic: **26 focused tests PASS**; separate independent exact rational rank checks, coprime inverse, Fibonacci aliases, non-dihedral phase-blind countermodels, noninvertible ×16 naturality, rational RREF action closure, linear target descent, additive drive cancellation, and exact finite four-pole zero-seed source states. This **does not** mean tests ran on this GitHub commit or in hosted CI, and is not an independent proof referee. Expanded reproducible source/test/dossiers are held in the downloadable local research bundle; the present GitHub note is the deliberately limited, stand-alone committed checkpoint.

**NEXT:** Bind the new readout to source-authenticated selected-orbit history, phase calibration, actual accessible actuator maps, carries and odd-prime denominators. Pre-register a source-specific signed bound and attack it with the same-forcing coherent wrong seed, periodic completions, phase-blind mutants and independently rotating observer frames. Demand an inequality uniform on every sufficiently large epoch, not fitted finite trends or Fourier identity. No main merge, tag, release, full categorical equivalence, physical realization, π proof or RH proof authorized.

**Related work:** [categorical observer atlas](../../../docs/CATEGORICAL_OBSERVER_ATLAS.md); [maintained π normality frontier](../../../docs/PI_NORMALITY_FRONTIER.md); [Kerodon density](https://kerodon.net/tag/03V8); [functional observability](https://pmc.ncbi.nlm.nih.gov/articles/PMC8740740/).
