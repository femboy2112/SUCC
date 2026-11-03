# OPERATION INERTIAL GYROSCOPE — common-carrier Spin(3) frame consensus and original π Weyl purity

**2026-11-03 · RESEARCH ONLY.** Exact parent [draft PR #480](https://github.com/femboy2112/SUCC/pull/480) SHA \`a5ea2c51446feb1e48099f18730fc60fa2f45d8e\`, itself stacked on #478/#477/#475/#474/#473/#471/#468 and Main XIX. Read-only old Main source files: \`observational_succ/hopf_source_exact.py\`, \`observational_succ/covariant_observer_frames.py\`, \`observational_succ/rank_two_chiral_towers.py\` and the October Pisot/Hopf arithmetic relativity dossier. The E-tower source protocol comes from #26/#27/#28/#61. Sibling #479 and older Cycloframe work are provenance, not independent success witnesses. **No π base-16 normality or RH theorem is claimed.**

## GY-01. The spinning top is an exact source-selected positive density matrix

The original zero-seeded signed four-pole BBP source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Put \(\chi_{n,h}=e^{2\pi ihU_n}\), \(c_N(h)=N^{-1}\sum_{n=0}^{N-1}\chi_{n,h}\) for integer \(h\ne0\). A normalized spinor \(\psi_{n,h}=(1,\chi_{n,h})/\sqrt2\) yields

\[
\boxed{\rho_{N,h}=\frac1N\sum_n\psi_{n,h}\psi_{n,h}^\dagger
=\frac12\begin{pmatrix}1&\overline{c_N(h)}\\c_N(h)&1\end{pmatrix}.}\tag{GY-01}
\]

This is PSD, trace 1, eigenvalues \(\frac12(1\pm|c_N(h)|)\), and exact *frame-independent spin purity*

\[
\boxed{\mathsf P_{N,h}=2\operatorname{tr}(\rho_{N,h}^2)-1
=|c_N(h)|^2
=\frac1{N^2}\sum_{n,m}\cos2\pi h(U_n-U_m).}\tag{GY-02}
\]

For any single common \(V\in SU(2)\), the source-representation change \(\rho\mapsto V\rho V^\dagger\) leaves trace, eigenvalues and purity unchanged. In particular the top is **maximally mixed** for that h iff \(c_N(h)=0\), not merely when a chosen x-axis report happens to vanish.

The classical Weyl criterion combined with the inherited original source Gamma/Green summable tail gives the exact **equivalence**

\[
\boxed{\pi\text{ base-16 normal}\Longleftrightarrow
\forall h\ne0:\ \rho_{N,h}\longrightarrow I/2
\Longleftrightarrow \forall h\ne0:\mathsf P_{N,h}\longrightarrow0.}\tag{GY-03}
\]

This is a robust observable reformulation and no proof of the unverified limiting property. A single h, a finite frequency window, or a fixed finite family of gyroscopes is never sufficient for complete normality.

## GY-02. Every legitimate E observer can synchronize noncommuting frames without Euler-angle gimbal lock

Reuse the **already-main** exact Hamilton quaternion \(\mathbb H_\mathbb Q\) class \`H\` and unit quaternions \(\mathrm{Sp}(1)=SU(2)\), with action \(v\mapsto qv\bar q\) on pure vectors \(v=x i+y j+z k\). This action is in \(SO(3)\), preserves exact rational dot products and has no Euler-angle coordinate singularity. Rotors \((3+4i)/5\) and \((5+12j)/13\) are exactly unit and do not commute.

For E-observer frames \(q_a\) on ONE source carrier define directed transport

\[
\boxed{L_{a\to b}=q_b q_a^{-1},\qquad
L_{b\to c}L_{a\to b}=L_{a\to c}.}\tag{GY-04}
\]

If local camera n reports \(v_n^{(n)}=q_n v_nq_n^{-1}\), the recovered vector at common E frame 0 is

\[
\boxed{\widetilde v_n=L_{n\to0}v_n^{(n)}L_{n\to0}^{-1}
=q_0v_nq_0^{-1}.}\tag{GY-05}
\]

Its mean squared norm is exactly \(|c_N(h)|^2\), regardless of **time-dependent** camera rotations, provided every link is genuine. Averaging local \(v_n^{(n)}\) without transporting them can turn a physically constant sequence into a false zero mean; it is an illicit frame mixture.

**Nonabelian E-relay gluing:** For a finite connected undirected network with source-labelled edges \(L_{ab}\in SU(2)\), a source-consistent global rotor assignment exists iff every closed loop's ordered product is identity. Proof: select a root and a spanning tree; transport its unit rotor along each tree path. Every additional edge agrees precisely when the fundamental cycle product is 1. This is classical torsor/Čech descent, previously studied in SUCC #27, now instantiated as an executable exact quaternion gyro protocol. No measured physical torque or cryptographic source attestation is inferred.

**Critical center:** \(q\) and \(-q\) act identically on ordinary Bloch vectors but are distinct spin lifts. A loop of product \(-1\) is closed in \(SO(3)\) and NOT in the specified \(\mathrm{Spin}(3)\) source register. Reject it if source spinor parity is committed; do not silently clip it to +1. The root-test mutation demonstrates both decisions and a genuinely noncentral forged link.

## GY-03. The authenticated BBP carry is the missing Spin double-cover datum

For every exact rational original U and integer h define a spinor rotation

\[
Q_h(U)=\exp(\pi khU)\in \mathrm{Spin}(2)\subset SU(2),\qquad
\operatorname{Ad}_{Q_h(U)}(i)
=\cos(2\pi hU)i+\sin(2\pi hU)j.
\]

Changing an unwrapped source lift \(U\to U+m\), integer m, changes the spinor by \((-1)^{hm}\) while leaving its Bloch vector unchanged:

\[
\boxed{Q_h(U+m)=(-1)^{hm}Q_h(U).}\tag{GY-06}
\]

Thus reducing \(U\) modulo one **before** retaining integer carry can erase the central spinor sign. A finite formal exact source register \(\mathrm{Spin2Mark}(hU\bmod2)\in\mathbb Q/2\mathbb Z\) preserves it; numerical sine/cosine evaluations are never treated as exact rational certificates.

The original source rotor recurrence is also exact in this abelian subgroup:

\[
\boxed{Q_h(U_{n+1})=Q_h(U_n)^{16}\,Q_h(r(n+1)).}\tag{GY-07}
\]

**Important no-go:** all selected \(Q_h(U_n)\) lie in the **same maximal torus** and commute pairwise. The genuine SOURCE phase is abelian even though the OBSERVERS may use noncommuting quaternion frames. A representation change cannot manufacture a non-Abelian source torque or a signed real mixing inequality. Source rank-two E² \(\mathbb Q(i)^2\) remains a commutative coordinatewise algebra; its additive \(\mathbb Q\)-linear embedding in quaternions from the historical Hopf module is NOT a ring isomorphism.

A globally continuous, unique spinor lift from an arbitrary direction on \(S^2\) is obstructed by the nontrivial Hopf fibration \(S^1\to S^3\to S^2\). The observer protocol uses local source-marked frames and authenticated transitions, **not** an imaginary global section. Reference: classical Hopf bundle topology, already SUCC main's Hopf source dossier.

## GY-04. SOURCE-SPECIFIC Γ correction transports the spinning-top purity with O_h(N⁻¹) cost

The original positive four-pole Green/Gamma tail satisfies \(U_n=16^n\alpha-T_n,\ \alpha=\pi/16\), with \(T_0=\alpha<11/56\) and for all n≥1, \(0<T_n<1/(64n^2)\). Classical \(\sum_{n\ge1}n^{-2}<2\) gives \(\sum_{n\ge0}T_n<11/56+1/32=51/224\).

Let \(c_N^U(h)\) be the original source mean and \(c_N^X(h)\) the completed radix mean. By \(|e(x)-e(y)|\le2\pi|x-y|\) and elementary π<22/7,

\[
\boxed{|c_N^U(h)-c_N^X(h)|<
\frac{561|h|}{392N}.}\tag{GY-08}
\]

Since \(|c_N^U|,|c_N^X|\le1\), the exact spin-purity identity yields

\[
\boxed{\left|\operatorname{tr}((\rho_{N,h}^U)^2)
-\operatorname{tr}((\rho_{N,h}^X)^2)\right|<
\frac{561|h|}{392N}.}\tag{GY-09}
\]

This explicit SOURCE-SELECTED carrier/frame-invariant O_h(1/N) transport is inherited in essence from SUCC #468 Gamma seam and #480 stationary Gamma section, now instantiated for the spinning top. It is **not** a proof that either purity decays.

## GY-05. The unbroken connection to the SUCC mesoscopic π-normality proof gate

For even M≥2 and a finite original source phase list, define

\[
\boxed{\mathfrak G_{N,M}=
\sum_{1\le h<M/2}\left(1-\frac{2h}{M}\right)
\bigl(2\operatorname{tr}(\rho_{N,h}^2)-1\bigr)
=\frac{\mathcal Q_{N,M}-1}{2}.}\tag{GY-10}
\]

Here \(\mathcal Q_{N,M}\) is exactly the original positive Fejér pair energy of #475/#476, with bandwidth H=M/2−1. Every summand is nonnegative and \(\mathfrak G\) is invariant under common or correctly transported local \(SU(2)\) E frames. No new PSD gain or signed estimate has been proved by this reexpression.

**Conditional theorem (inherited #476 WM-07, retyped):** Let A run through all sufficiently large dyadic integers. If there exists an EXPLICIT even mesh schedule \(M_A\) with \(2\le M_A\le A,\ M_A\to\infty\) such that the AUTHENTIC ZERO-SEEDED original phase window [A,2A) satisfies

\[
\boxed{\mathfrak G_{A,M_A}=o(\log M_A),}\tag{OPEN-GYRO-GATE}
\]

then π is normal to base 16. Proof: \(Q=1+2\mathfrak G=o(\log M_A)\), the old hereditary pointwise Fejér/Ward ladder plus genuine Gamma source transport controls every partial epoch and hence every prefix. This is precisely the OLD conditional normality route, expressed as consensus-invariant SU2 purity.

SUCC #478's genuine original h-specific opposite phase-sector imbalance \(\mathcal A_{N,M}(h)\) also yields a purely RATIONAL finite upper bound

\[
\boxed{\mathsf P_{N,h}\le
\left(\mathcal A_{N,M}(h)+\frac{22|h|}{7M}\right)^2.}\tag{GY-11}
\]

This uses original exact rational bin counts and π<22/7. SUCC #475's two-sided Fejér-versus-collision bound gives the rational (often weak) \(\mathcal Q_{N,M}<(\frac32+\frac{(22/7)^2}{6})\,\frac M{N^2}\sum_j c_j^2\). These are actual finite source-observer **certificates**, but no all-epoch sublogarithmic estimate for original U₀=0 is established.

## GY-06. Two independent false-Haar adversaries and a no-gimbal verdict

1. **Moving-camera fake Haar:** Fix a genuine coherent vector i at all times. Let the local E frames alternate unit quaternions 1 and k. Their untransported Bloch measurements alternate i,−i and falsely average to zero. Transport through the actual source-aligned quaternion groupoid produces the constant i and coherence 1. This is a rigorous rational gauge counterexample, not an assumption about π.
2. **Quaternion frame twirl fake Haar:** For any pure quaternion vector v,
   \(\frac14\sum_{q\in\{1,i,j,k\}}qv q^{-1}=0\). A source-blind average over E-frame choices produces a maximally mixed spin observable for **every source**, including a fully coherent periodic one. Thus “all observers agree after averaging orientations” is false evidence for Haar.
3. **Same-original-forcing changed seed:** Preserve all four original poles and Γ source, but take the real seed \(s=1/5-\alpha\). The completed orbit is \(16^n/5=1/5\) on the circle and \(U_n(s)\to1/5\). Its gyro \(\mathsf P_{N,h}\to1\) for every fixed integer h, while the Γ section, E² taps and source potential stay intact. A source-only/group-only purity estimate cannot distinguish it.
4. **Gamma vs rotor:** The old historical E² gain \(g=(1+i)/2\), equal to the Gamma(shape1,rate1) Fourier multiplier at ω=1, has squared norm \(1/2\), NOT 1. It is a **contraction + 45° rotation**, not an admissible orientation rotor. Calling it a unit quaternion would spuriously change purity. Separate its phase/orientation from its field amplitude; do not fit a decay mechanism by normalizing the wrong type.
5. **Full inertial physics firewall:** This exact gyro constructs spatial \(\mathrm{Spin}(3)/SO(3)\) *observer orientation* covariance. It is NOT a proof of arbitrary Lorentz-frame covariance or a physical inertial gyroscope in spacetime; the existing \`covariant_observer_frames.py\` treats 2+1 Lorentz transformations separately and requires a metric/source event map. The mathematical Weyl criterion is coordinate-independent under the declared common-carrier transports.

## GY-07. Predeclared source-specific tests, what they demonstrate, and next lamp

Before executing new selected source horizons, \`PREREGISTRATION.md\` froze N=96,192,384, h=1,2,16, three rational noncommuting observer frames and a fixed error threshold \(5\times10^{-12}\) for numeric invariance checks. For each N, exact integer/rational phase-difference SHA256 receipts and original sector collision rationals were archived; displayed coherent spin purities are float diagnostics, NOT rigorous asymptotic certificates. All 9 selected coherence cross-frame cases passed and every exact Fejér majorant controlled its respective finite diagnostic. The coherent same-forcing finite rational wrong seed had last-192 coherence squared >0.999. Full raw receipt in \`HOLDOUTS.json\`, replayable by \`probe.py --verify\`.

The local staged suite reports 32/32 tests PASS, including inherited old E² original source cross-check, exact quaternion/rational SO3 orthogonality, four-E graph gluing, source sign/parity and coerced-fake-Haar controls. Historical SUCC main native Hopf module was read through connected GitHub; isolated local staging used a source-matched minimal quaternion H arithmetic adapter only for tests, so this is **not** a claim that all existing main Hopf tests ran in the full native repo. New files must run against the real native module in hosted exact-head CI before promotion. No full local >11k SUCC suite, independent external peer review or new Lean proof is claimed.

**Final ledger:**

- **PAPER PROVED / classical relative to source:** GY-01/02/03 exact spin purity and frame equivalence; GY-04/07 E-relay nonabelian loop gluing; GY-06 SU2 central parity/carry; GY-08/09 original Γ purity transport; GY-10/11 positive Fejér/sector certificate transport; quaternion twirl and time-varying-camera countermodels.
- **FINITE OBSERVED:** local 32 focused tests and three preregistered original source horizons, numeric spin values with exact rational input and separate exact rational collision bounds.
- **REFUTED:** frame twirling, mere q-dependent observation rotations, unit-normalization of Γ gain, and a global independent quaternion source ring are ways to prove π normality.
- **UNVERIFIED:** the actual marked original zero-seed \(\mathfrak G_{A,M_A}=o(\log M_A)\), or any other source-specific signed all-prefix Weyl saving. Base-16 normality of π and RH remain OPEN.

**Next decisive probe:** Derive a genuinely new source-attested inequality restricting \(\operatorname{tr}(\rho_{A,h}^2)\) across many h or growing dyadic epochs from the ORIGINAL E² chiral pair with full prime-clock/cofactor and exact integer carries. It must distinguish literal \(U_0=0\) from the coherent same-four-pole counterseed. An invariant trace identity or another valid frame alone does NOT pay this truth debt.
