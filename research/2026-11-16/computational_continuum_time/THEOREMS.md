# Computational continuum time: source-labelled paths, integer-deck holonomy and Gamma's smoothing no-go

**Scope / status (2026-11-16).** Research-only, additive successor of SUCC Main XXVI and draft #658. Classical topology, exact BBP source algebra, a new-to-SUCC pointed-lift path construction, elementary metric/holonomy identities, and a calibrated Gamma loss-of-history counterexample. These are paper derivations with separate executable finite controls, **not** a proof of π-normality, R0, signed all-shell carry density, a physical continuum, or an intrinsic metric determined by a bare computational graph. No novelty/priority claim in classical topology or Gamma analysis.

## 0. Original source, typed objects, and dependency contract

Keep without modification

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\ U_{n+1}=16U_n+r(n+1),\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]

Set \(x=\sum_{j\ge1}16^{-j}r(j)\). The classical BBP identity identifies \(x=\pi/16\). For all integers \(n\ge0\):
\[
16^n x=U_n+T_n,\qquad U_n\in\mathbb Q,\quad T_n>0.
\]

**Types:** (i) a source-authenticated real lift \(x\in\mathbb R\), (ii) its observed circle point \(z_n=16^nx\bmod1\), (iii) an inverse-history solenoid state, (iv) an explicitly declared fractional-time path, (v) a path metric based on lawful observations, and (vi) Gamma averaging of that path. Circle observations, 2-adic source addresses, and the larger continuation space are **not identical data types**. An additional interpolation/measurement rule is additional structure, not deduced from the integer orbit.

## CCT-01 — No continuous global fractional-time circle flow with time-one radix-16 expansion (CLASSICAL, PROVED)

Let \(T:S^1\to S^1\) be \(T(z)=z^{16}\) (additive coordinate \(z\mapsto16z\bmod1\)). There is **no** family \(\Phi_s:S^1\to S^1\), continuous jointly in \((s,z)\in[0,1]\times S^1\), with \(\Phi_0=\operatorname{id}\), \(\Phi_1=T\). The family would be a homotopy; the circle degree is homotopy-invariant, but degrees at its two ends are 1 and 16. In particular there is no continuous circle flow realizing this time-one map. Neither analyticity nor choosing Gamma coefficients repairs the degree obstruction.

There *are* isolated intermediate endomorphisms. At \(s=j/4\), \(16^s=2^j\in\mathbb N\), so multiplication by \(16^s\) descends from \(\mathbb R\) to \(S^1\). These four binary substeps do not produce a jointly continuous interval of circle maps.

## CCT-02 — The original pointed lift supplies a coherent fractional-time path, not a global circle action (EXACT)

For each selected real lift \(x\) define
\[
\boxed{\gamma_x(t)=\exp(2\pi i16^t x),\quad t\ge0.}
\]

This solves \(\dot X=(\log16)X\) on the *real lift* \(X(t)=16^t x\), followed by circle observation. At integer times, \(\gamma_x(n)=\exp(2\pi i(U_n+T_n))\) for the authentic BBP zero seed. The curve is continuous and real analytic as a function of real t, and it depends on x's real lift. It does **not** define \(S^1\to S^1\) at noninteger t because a deck shift \(x\mapsto x+k\), \(k\in\mathbb Z\), changes its value by \(\exp(2\pi ik16^t)\), which need not equal 1. This is a *pointed trajectory* in an extended carrier, not an intrinsic interpolation of the original circle endomorphism.

For integer seed shift k, the same literal forcing gives \(U_n(k)=U_n(0)+k16^n\), while T is unchanged. Hence all integer-time circle observations agree, while the source's initial value changes from 0 to k. Source authentication supplies a lawful distinction that is invisible in the completed circle observations.

## CCT-03 — Hidden signed winding for identical integer-time observations (EXACT TOPOLOGY)

For every integer k, all n>=0, the **relative** curve on one computational tick is
\[
\frac{\gamma_{x+k}(n+s)}{\gamma_x(n+s)}=\exp(2\pi ik16^{n+s}),\quad 0\le s\le1.
\]

At both ends it is 1. Its lift to the real argument has total increase \(k(16^{n+1}-16^n)\); therefore the closed relative loop has exactly
\[
\boxed{\operatorname{wind}_{[n,n+1]}(\gamma_{x+k}/\gamma_x)=15k16^n.}
\]

This signed winding is invariant under homotopies of the **declared relative paths** fixing the endpoints. It is *not* an invariant of the original unlabelled circle dynamics, because an alternate continuous interpolation could insert an arbitrary extra integer loop while preserving all integer samples. The ODE or another source-calibrated path law must select the interpolation. The same relative trajectories agree at all quarter-ticks \(t=j/4\) because \(16^{j/4}=2^j\in\mathbb Z\): even a finer discrete radix-two clock cannot, by itself, recover the between-tick winding.

## CCT-04 — An explicit faithful metric on source-labelled real lifts (EXACT)

Define, for real x,y,
\[
\boxed{d_{\rm path}(x,y)^2=\int_0^1|\gamma_x(s)-\gamma_y(s)|^2\,ds
=2-\frac2{\log16}\int_1^{16}\frac{\cos(2\pi(x-y)u)}{u}\,du.}
\]

This is a translation-invariant **metric** on \(\mathbb R\), because it is the L² distance of two continuous circle-valued functions; zero distance implies \(\exp(2\pi i(x-y)16^s)=1\) on an interval, forcing x=y. Triangle inequality is Minkowski. The metric is bounded, not Euclidean, and does not descend to \(\mathbb R/\mathbb Z\): integer-deck lifts have zero circle distance at all integer times but positive path distance.

For every nonzero integer k, integration by parts at integer endpoints gives the rigorous, explicit envelope
\[
\boxed{\left|d_{\rm path}(x,x+k)^2-2\right|
\le\frac{15}{16\pi|k|\log16}.}
\]

Indeed the sine boundary term vanishes at u=1,16, and \(|\int_1^{16}\cos(2\pi ku)du/u|\le(2\pi|k|)^{-1}\int_1^{16}u^{-2}du=15/(32\pi|k|)\). Thus any nonzero integer deck shift is separated from the original lift by a uniform positive gap. The proof is analytic; Simpson numerical checks in `test_continuum_probe.py` are calibration only. This metric is **chosen** by the specific real-dilation path law and unit-time observation weight.

## CCT-05 — Source-labelled solenoid natural extension and a lawful suspension flow (CLASSICAL / EXACT)

Let \(\mathbb T=\mathbb R/\mathbb Z\), \(T(z)=16z\bmod1\). Form the compact inverse limit
\[
\mathscr S_{16}=\{(z_0,z_{-1},z_{-2},\ldots)\in\mathbb T^{\mathbb N_0}: T(z_{-j-1})=z_{-j}\}.
\]

Its *natural extension* \(\widehat T(z_0,z_{-1},\ldots)=(Tz_0,z_0,z_{-1},\ldots)\) is a homeomorphism with inverse the left shift. The real source lift x defines one compatible backward-history point
\[
\boxed{\widehat x=(x\bmod1,\ x/16\bmod1,\ x/16^2\bmod1,\ldots).}
\]

The source's zero-seed x is the declared selector. A different lift x+k has **the same future circle samples** but a distinct backward history whenever k≠0: at level j the two states coincide exactly when \(16^j\mid k\). In particular finite prefix depth does not distinguish shifts divisible by 16^j, whereas sufficiently deep history always does. This is the computational inside-out refinement in a bona fide topological inverse system, not a claim that observing the original circle reveals its missing prehistory.

Construct the mapping torus
\[
\boxed{\mathscr M=(\mathscr S_{16}\times\mathbb R)/[(p,t+1)\sim(\widehat T p,t)].}
\]

The continuous flow \(\varphi_s[p,t]=[p,t+s]\) has return map \(\widehat T\) on the cross-section. Its integer-time projected orbit is exactly \(T^nz_0\). Thus a continuous **state-preserving** computational-time realization exists after enlarging the carrier to remember compatible backward paths. It is not a continuous fractional circle endomorphism. The arbitrary unit-time roof/choice of topology is part of the model. The real-dilation curve of CCT-02 and this suspension are two *distinct* lawful extensions with the same integer observations; identifying their fractional-time outputs requires a further transport map.

## CCT-06 — Gamma acts on trajectories; pathwise information must precede compression (CLASSICAL / EXACT)

For \(\alpha>0\), let \(S_\alpha\sim\mathrm{Gamma}(\alpha,1)\). For bounded continuous \(f:[0,\infty)\to\mathbb C\), define
\[
(\mathcal G_\alpha f)(t)=\mathbb E[f(t+S_\alpha)]
=\frac1{\Gamma(\alpha)}\int_0^\infty s^{\alpha-1}e^{-s}f(t+s)ds.
\]

Gamma convolution proves \(\mathcal G_\alpha\mathcal G_\beta=\mathcal G_{\alpha+\beta}\); \(\mathcal G_0=I\), with pointwise \(\mathcal G_\alpha f(t)\to f(t)\) as \(\alpha\downarrow0\). Do not claim strong continuity on all of \(C_b\) in the uniform norm; the phase path of CCT-02 is not uniformly continuous on the unbounded time half-line.

Define the *pre-average* observation distance
\[
\boxed{d_\alpha(x,y)^2=\mathbb E|\gamma_x(S_\alpha)-\gamma_y(S_\alpha)|^2.}
\]

At every fixed \(\alpha>0\) this is a metric on \(\mathbb R\), by positivity of the Gamma density on all s>0 and continuity/uniqueness of the original paths. By contrast \(d_0(x,y)=|e^{2\pi ix}-e^{2\pi iy}|\) is only a pseudometric on real lifts, identifying integer shifts. For fixed integer k≠0, \(d_\alpha(x,x+k)>0\) for every α>0 but tends to 0 as α↓0. These metrics describe an explicitly **added fractional-time observer**, not an instrument automatically present in the original BBP sequence.

For complex \(Z_s=\gamma_x(s)-\gamma_y(s)\), the exact variance identity is
\[
\boxed{\mathbb E|Z_S|^2=|\mathbb EZ_S|^2+\mathbb E|Z_S-\mathbb EZ_S|^2.}
\]

Gamma-compressing first retains only the first summand; comparing coherent paths **before** compression retains the strictly nonnegative hidden-path variance. The latter is not automatically a signed real-circle Weyl estimate. It depends on the availability of the continuum observable and the source path law.

## CCT-07 — Gamma smoothing can falsely erase a perfectly locked integer orbit (PROVED COUNTEREXAMPLE)

Take \(x=1\). At every integer n>=0, \(\gamma_1(n)=e^{2\pi i16^n}=1\): the discrete orbit is perfectly coherent and nonnormal.

Nevertheless, for every fixed positive Gamma shape \(\alpha\) and every real lift x≠0,
\[
\boxed{\lim_{t\to\infty}(\mathcal G_\alpha\gamma_x)(t)=0.}
\]

Proof: put \(c=\log16\), \(A=2\pi x16^t\), \(u=16^s\). Then
\[
(\mathcal G_\alpha\gamma_x)(t)
=\int_1^\infty e^{iAu}\,
\underbrace{\frac{(\log u/c)^{\alpha-1}u^{-1-1/c}}{c\Gamma(\alpha)}}_{h_\alpha(u)\in L^1([1,\infty))}\,du.
\]

The amplitude \(h_\alpha\) integrates to one. The Riemann–Lebesgue lemma sends its Fourier transform to zero as \(|A|\to\infty\). This proof does not presume \(x\) normal, irrational or source-authenticated. For \(\alpha=1\), integration by parts gives a rigorous quantitative bound
\[
\boxed{|(\mathcal G_1\gamma_x)(t)|\le\frac{1}{\pi|x|\log16\,16^t}.}
\]

Indeed \(h_1(u)=u^{-1-1/c}/c\) and \(h_1(1)+\int_1^\infty|h_1'(u)|du=2/c\). This is a **decisive refutation** of the inference that continuous Gamma-time attenuation on the chosen interpolated orbit yields any positive-density hexadecimal digit theorem.

The order-of-limits defect is exact for x≠0:
\[
\boxed{
\lim_{\alpha\downarrow0}\lim_{t\to\infty}|\mathcal G_\alpha\gamma_x(t)|=0,
\qquad
\lim_{t\to\infty}\lim_{\alpha\downarrow0}|\mathcal G_\alpha\gamma_x(t)|=1.}
\]

The pointwise \(\alpha\downarrow0\) limit equals the unit phase \(\gamma_x(t)\), not a uniform-in-time limit. The obstruction is methodological; it is not π-normality progress by itself.

## CCT-08 — No canonical continuum from discrete arrows alone (PROVED COUNTERMODEL)

Knowing two endpoints and their composable discrete arrow is insufficient to determine internal winding. A closed relative path on one unit interval can be multiplied by \(e^{2\pi iqs}\), \(q\in\mathbb Z\), leaving both endpoints unchanged but changing winding by q. The original integer successor recurrence does not specify the fractional-time winding. A unique continuation requires an authenticated differential equation/connection, a selected inverse-history lift, admissible probes, or an equivalent source condition.

For any common continuous, source-labelled state space X and declared readouts \(O_e\), the family
\[
\boxed{d_{\mathcal E}(\gamma,\eta)^2=\sum_{e\ge1}2^{-e}\int_0^1\delta_e(O_e\gamma(s),O_e\eta(s))^2ds}
\]

is a pseudometric on continuous paths when the bounded \(\delta_e\) are metrics, and a metric on the quotient by identical declared readout paths. When the readout family separates all actual path states and their coordinate responses are continuous, zero distance entails path equality. This extends the maintained SUCC Principia CG-08 behavioral pseudometric from point probes to *time-resolved path probes*. A quotient remains essential when lawful instruments fail to distinguish histories. Holonomy \(\int_\gamma A\) is an independent signed observation requiring an operationally declared connection A and correct gauge transport; positive path energy does not determine that holonomy.

## CCT-09 — A source-selected, falsifiable next arithmetic gate (OPEN)

The natural extension/suspension is a legitimate *pathway* for continuous time, but it includes no new source-derived signed inequality. The source-specific R0 target remains \(\exists\eta>0,B_0\ \forall B\ge B_0:1-\Re W_B(1)\ge\eta\). Main XXVI's stronger selected carry target is \(d_B\ge\delta\) on every large integer shell. A legitimate next experiment must:

1. Define a **common typed state** retaining original \(U_0=0\), four signed poles, rational winding, future Green completion, odd cofactor/CRT passport, and selected inverse-history branch. Do not identify real suspension arcs with paths inside \(\mathbb Z_2\); that space has no nonconstant continuous real interval paths.
2. Supply a **lawful, explicit observation** at interior computational time (or prove the desired statement uses only original discrete observations). The new path metric alone cannot increase source contact. If a Gamma kernel is introduced, measure or transport the retained complex phase before taking a positive norm; retain the source gauge and zero seed.
3. Specify a mixed time/refinement square and calculate its **signed connection defect** on the actual source. Distinguish the two proposed continuum constructions CCT-02 and CCT-05 rather than implicitly identifying them. Require a countermodel that destroys the proposed nonzero defect while preserving its declared premises.
4. Predict a fixed-frequency shell margin from that defect. Prove a coercive estimate using original zero ancestry, with explicit seed-height boundary cost if the theorem admits changed rational seeds. The historical A-FS rational finite shadows from Main XXVI refute a seed-blind uniformly bounded potential; the coherent real counterseed defeats source-only Gamma averages. The integer coboundary g(n)=2n² changes the source presentation but preserves the completed circle, so a completed-orbit result must transport under that gauge.
5. Freeze probe hypotheses and parameters before any fresh source holdout beyond index 131072. The current positive Gamma/suspension constructions and a finite test do not certify an all-shell signed saving.

**Ledger:** CCT-01..08 are scoped classical/paper-exact; CCT-07 is a decisive counterexample to smoothing→normality. CCT-09 is UNVERIFIED and retains the weakest open premise. Independent mathematical review and Lean certification are not claimed by these paper proofs or local tests.
