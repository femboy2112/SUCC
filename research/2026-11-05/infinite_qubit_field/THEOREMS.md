# OPERATION INFINITE QUBIT FIELD — compatible many-body gluing for the authentic BBP source

**Draft paper mathematics, 2026-11-05.** Pinned additive parent #511 at \`378a77eefa084225f30a209c27a2b4bc54897e72\`. Source inherited from authentic original four-pole BBP and its angular/radial source-prime decomposition. All original source data, literal U0=0, source manifests, historical Lean/proof contracts, CI/production/main unchanged. No physical quantum dynamics, automatic truth of all propositions, global novelty or π normality claimed.

Notation: \(e(t)=\exp(2\pi i t)\); \(X,Y,Z\) are Pauli matrices; \(CZ=\operatorname{diag}(1,1,1,-1)\); \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). Here **q-bit means a declared two-level Hilbert factor**, not an a priori actual quantum substrate of mathematical truth.

## IQ-00: the global state is the inverse limit of compatible finite observations

For the unital inclusions \(\iota_N:\mathcal A_N\hookrightarrow\mathcal A_{N+1}\) with \(\iota_N(O)=O\otimes I\), let \(\mathrm{State}(\mathcal A_N)\) denote all positive normalized linear functionals on the finite matrix algebra, or equivalently finite density matrices. Restriction is dual to inclusion. Then there is a natural bijection
\[
\boxed{
\mathrm{State}\left(\overline{\varinjlim_N\mathcal A_N}^{\|\cdot\|}\right)
\ \cong\ 
\varprojlim_N\mathrm{State}(\mathcal A_N).
} \tag{IQ0}
\]
**Proof:** any infinite state restricts to a normalized positive compatible family. Conversely suppose \(\omega_{N+1}(O\otimes I)=\omega_N(O)\) for all O. Define a functional on the algebraic union by \(\omega([O]_N)=\omega_N(O)\); compatibility makes it well-defined. It is positive, normalized, and \(|\omega(O)|\le\|O\|\), so it extends uniquely by continuity to the norm completion. These constructions are inverse. In density-matrix language, the condition is \(\rho_N=\operatorname{Tr}_{N+1}\rho_{N+1}\).

This is the exact categorical content of "all finite forms coherent inside one global state." **The state spaces are convex; the set of PURE states is not generally preserved by restriction.** An entangled pure global state naturally has mixed finite marginals. This does not yield a canonical single global Hilbert-space wavefunction or joint definite values for noncommuting propositions. The physical tensor factorization is an explicit model choice.

## IQ-01: finite global coherence does NOT automatically glue to infinity (sharp GHZ obstruction)

For \(N\ge2\), choose \(\theta\in\mathbb R\) and define the *finite pure* GHZ vector
\[
|G_N(\theta)\rangle=\big(|0\rangle^{\otimes N}
 -e^{i\theta}|1\rangle^{\otimes N}\big)/\sqrt2,\quad
\rho_N^G=|G_N\rangle\langle G_N|.
\]
Every finite GHZ_N is entangled across any nontrivial bipartition: its Schmidt coefficients are \(1/\sqrt2,1/\sqrt2\). But the compatibility obligation for an infinite state with EXACT finite marginals \(\rho_N\) is
\[
\boxed{\operatorname{Tr}_{N+1}\rho_{N+1}=\rho_N.} \tag{IQ1}
\]
Directly tracing the last qubit gives
\[
\operatorname{Tr}_{N+1}\rho_{N+1}^G
=\tfrac12(|0^N\rangle\langle0^N|+|1^N\rangle\langle1^N|)
\ne\rho_N^G
\]
because the GHZ_N off-diagonal \(|0^N\rangle\langle1^N|\) is nonzero. Thus the sequence of **pure** finite GHZ states is NOT projectively consistent under ordinary physical partial trace.

Moreover, for any fixed \(m<N\), the reduced GHZ_N state on the first m sites is
\[
\rho_{m|N}^G=\tfrac12(|0^m\rangle\langle0^m|+|1^m\rangle\langle1^m|),
\]
independent of \(\theta\). Every fixed local observable has the same \(N\to\infty\) expectation as the **separable mixture of the two infinite product states** \(|0^\infty\rangle\) and \(|1^\infty\rangle\). Since the local observables are norm dense in the quasilocal algebra, the limiting algebraic state loses the phase on the ENTIRE quasilocal algebra. This is a precise *local-access* obstruction to interpreting "infinite GHZ wavefunction" as a retained operational global coherence. It is NOT a no-go for all genuinely entangled infinite spin systems or for non-quasilocal global observables in different representations.

## IQ-01b: a PURE Bell pair cannot remain unchanged while joining genuine larger entanglement

**Sharp compatibility/monogamy lemma.** Let \(\rho_{ABC}\ge0\) be any normalized state on finite-dimensional tensor factors A,B,C. If its AB restriction is PURE, \(\rho_{AB}=|\psi\rangle\langle\psi|\), then necessarily
\[
\boxed{\rho_{ABC}=|\psi\rangle\langle\psi|_{AB}\otimes\sigma_C.} \tag{IQ1b}
\]
**Proof:** Let \(P=|\psi\rangle\langle\psi|\) on AB. Since \(\operatorname{Tr}_{AB}[(I-P)\rho_{AB}]=0\) and \(\rho_{ABC}\) is positive, \((I-P)\otimes I_C\) has zero expectation; positivity forces \(\rho_{ABC}\) to have support only on the rank-one AB subspace \(P\otimes H_C\). Thus the state factors as claimed. The same argument extends to arbitrary remaining finite or quasilocal environment using restrictions.

In particular, the **exact pure parent Bell pair** of SUCC #511 cannot be an unchanged two-site reduced density matrix of a connected graph state genuinely involving new sites. One MUST either (a) allow the original two-site marginal to become mixed, (b) retain the Bell pair as a decoupled factor, or (c) change the meaning of inclusion/observation and declare that new map explicitly. For example, finite \(|C_2\rangle\) is a pure Bell-equivalent state with two-site purity 1, whereas the actual first-two-site restriction of the semi-infinite cluster is mixed, with purity 1/2, already witnessed by \(\operatorname{Tr}_3|C_3\rangle\langle C_3|\). This is not a failure of global coherence: it is precisely how *multipartite* entanglement redistributes local information.

This no-go directly constrains the user's idea that all finite entangled forms should remain simultaneously realized. **The correct invariant is compatibility of the finite marginal states and their jointly supported observables, not preservation of every standalone pure finite-state wavefunction.**

## IQ-02: coherent infinite reconstruction via a quasilocal cluster automorphism

For every finite \(N\ge2\), define the N-qubit path graph state
\[
|C_N\rangle=\prod_{j=0}^{N-2}CZ_{j,j+1}|+\rangle^{\otimes N}.
\]
The local observable algebra is \(\mathcal A_N=\bigotimes_{j=0}^{N-1}M_2(\mathbb C)\), embedded through \(A\mapsto A\otimes I\). The infinite quasilocal algebra is
\[
\mathcal A_\infty=\overline{\bigcup_N \mathcal A_N}^{\|\cdot\|}.
\]

**Constructive theorem.** For any strictly local observable O supported in a finite set \(S\subset\mathbb N_0\), conjugation by \(U_N=\prod_{j=0}^{N-2}CZ_{j,j+1}\) is independent of N once N contains every site in S and its adjacent neighbors. This is because all CZ gates commute and those acting outside the one-neighbor buffer cancel against O. Define the local *-automorphism
\(\alpha(O)=U_N^\dagger O U_N\) at sufficiently large N; it preserves products, * and norms and has inverse itself since CZ gates square to I. Thus it extends uniquely to a bounded *-automorphism of \(\mathcal A_\infty\). Let \(\omega_+(O)=\langle+|^{\otimes \infty}O|+\rangle^{\otimes\infty}\) on local observables and extend by norm. Then
\[
\boxed{\omega_C(O)=\omega_+(\alpha(O))}
\]
is a well-defined normalized positive state on the entire quasilocal algebra. The product state \(\omega_+\) is pure, and automorphisms preserve purity; hence \(\omega_C\) is a pure infinite-system algebraic state.

**Compatibility.** For each fixed first-m subsystem, let \(\rho_m^\infty\) be its density matrix induced by \(\omega_C\). For EVERY \(N\ge m+1\), \(\operatorname{Tr}_{[m,N)}|C_N\rangle\langle C_N|=\rho_m^\infty\). The ONE right-neighbor buffer is necessary: pure \(|C_m\rangle\langle C_m|\) need not equal the mixed \(\rho_m^\infty\). Consequently, \(\operatorname{Tr}_{m}\rho_{m+1}^\infty=\rho_m^\infty\), and all finite true local restrictions belong to ONE global state. This fulfills the precise meaning of "simultaneously coherent local forms" without asserting a canonical single Hilbert wavefunction for arithmetic.

**Multipartite entanglement.** For every finite N and any contiguous cut \([0,j]|[j+1,N-1]\), the graph-state preparation factors into unitaries within each side and exactly ONE CZ crossing the cut. Acting on the two cut-boundary input \(|+\rangle\) factors, this CZ creates the state \((|0\rangle|+\rangle+|1\rangle|-\rangle)/\sqrt2\) with Schmidt coefficients \(1/\sqrt2\) each. All other gates are local relative to that cut. Thus the pure graph state has **exactly one ebit** across every contiguous cut. This is genuine connected multipartite entanglement, though entanglement entropy obeys an area law rather than growing without bound with N.

The stabilizer equations for the infinite right-sided chain are
\[
K_0=X_0Z_1,\qquad K_j=Z_{j-1}X_jZ_{j+1}\ (j\ge1),\qquad
\omega_C(K_j)=1.
\]

## IQ-03: arbitrary group-size complex phase glue, all within ONE state

For arbitrary real source-labelled angles \(\theta_j\) at *even* sites \(2j\), define a rotated state \(\omega_{\boldsymbol\theta}\) by the local unitary \(R_z(\theta_j)=\exp(-i\theta_j Z_{2j}/2)\) on each even site. On a finite observable only finitely many rotations matter, so this sitewise action is a well-defined *-automorphism EVEN if infinitely many angles are nonzero, with no requirement that an infinite tensor product of Hilbert-space unitaries converge. It preserves purity and consistency.

Define for every integer \(m\ge1\) the complex **finite-support** group witness
\[
\boxed{B_m=\left[\prod_{j=0}^{m-1}(X_{2j}+iY_{2j})\right]Z_{2m-1}.} \tag{IQ2}
\]
This acts on m+1 distinct sites, including an endpoint Z.

Let \(K_{2j}\) be the original graph stabilizers at even positions. Their product is
\[
\prod_{j=0}^{m-1}K_{2j}
=\left(\prod_{j=0}^{m-1}X_{2j}\right)Z_{2m-1}.
\]
All intermediate odd-site Z factors occur twice and cancel. More directly, conjugating each \((X+iY)_{2j}\) through the CZ network inserts the adjacent odd-site Z factors, all cancelling except the endpoint factor, leaving \(\prod(X+iY)_{2j}\) on product \(|+\rangle\). Because \(\langle+|X+iY|+\rangle=1\), the original graph expectation of B_m is exactly 1.

Under the source-labelled local rotations,
\(R_z(\theta)^\dagger(X+iY)R_z(\theta)=e^{i\theta}(X+iY)\).
Therefore
\[
\boxed{\omega_{\boldsymbol\theta}(B_m)
=\exp\left(i\sum_{j=0}^{m-1}\theta_j\right)
=\prod_{j=0}^{m-1}e^{i\theta_j}.} \tag{IQ3}
\]
This is EXACT for EVERY finite m, in the SAME compatible infinite-system state. It is an operationally precise many-body gluing of simultaneous local source phases. It is not stochastic independence or a claim that arbitrary logical propositions are jointly true.

**Readout budget.** The canonical raising-string witness obeys \(\|B_m\|=2^m\). Hence its unit-norm version \(B_m/2^m\) has phase expectation \(2^{-m}e^{i\sum_{j<m}\theta_j}\). The scalar signal of this particular bounded-norm readout therefore decays exponentially with group size. Do NOT generalize this to a proof that all possible sophisticated collective measurements must have the same cost, or claim that \(B_m\) itself converges in operator norm as \(m\to\infty\). Infinite-state existence is not equal to an infinitely supported phase observable of finite cost.

Every one-qubit reduced state of the connected cluster is maximally mixed, and remains so under the source local rotations. Hence all one-site measurements are phase-blind even though the finite multi-site witness recovers the phase. This supplies exactly the kind of load-bearing *relational* information inaccessible to marginal scalar observations.

## IQ-04: the AUTHENTIC BBP angular/radial phases as first two channels

Let the genuine zero-seeded rational original, angular and radial states be
\[
U_0=Y_0=Z_0=0,\quad U_n=16U_{n-1}+r_o(n),\quad
Y_n=16Y_{n-1}+r_a(n),\quad Z_n=16Z_{n-1}+r_r(n),\quad U_n=Y_n+Z_n.
\]
For every integer h≠0 and source time n, set the two even-site local angles
\[
\theta_{0,n}=2\pi hY_n,\qquad
\theta_{1,n}=2\pi hZ_n,\qquad
\theta_{j,n}=0\ (j\ge2).
\]
All phases are constructed from the exact original rational source, not from supplied digits of π. IQ3 gives
\[
\boxed{\omega_{n,h}(B_1)=e(hY_n),\quad
\omega_{n,h}(B_m)=e(hU_n)\quad (m\ge2).} \tag{IQ4}
\]
The same state holds the angular observation, its radial extension, and every further finite group witness simultaneously. At m=2, \(B_2=(X_0+iY_0)(X_2+iY_2)Z_3\) is a THREE-site joint observable; m=3 and m=4 give four- and five-site observables. The graph entanglement across cuts remains exactly one ebit because these source-rotations are local unitaries.

The witness obeys the exact time-labelled original-source law
\[
\boxed{\omega_{n+1,h}(B_2)
=\omega_{n,h}(B_2)^{16}\,e(h r_o(n+1)),\quad
\omega_{0,h}(B_2)=1.} \tag{IQ5}
\]
This is a source-exact *encoding of the BBP recurrence*. A time-dependent product of local Z rotations maps each encoded state to the next, but their angles were selected FROM the original arithmetic solution. That chosen unitary encoding is not a derivation of the source law from quantum physics.

A finite array of additional source angles \(\theta_{j,n}\) may refine any source decomposition whose sum is the correct original phase, but new algebraic phase slots are not automatically independent arithmetic information. Conversely source-dependent constraints must be preserved before treating their product as an original-source correlation.

## IQ-04b: the gluing of source channels COMMUTES with their actual dynamics

The many-body phase product is not merely a simultaneous snapshot; it is a morphism of the **declared source-labelled nonautonomous phase recurrences**.

For any fixed finite group of source channels \(j=0,\ldots,m-1\) with exact forcing \(r_j(n)\), literal initial phase \(\theta_{j,0}=0\), and recurrences \(q_{j,n+1}=16q_{j,n}+r_j(n+1)\), define \(w_{j,n}=e(hq_{j,n})\). The local phase dynamics are \(w_{j,n+1}=w_{j,n}^{16}e(hr_j(n+1))\). The graph-state grouped character is \(W_{m,n}=\omega_{n,h}(B_m)=\prod_{j<m}w_{j,n}\). Then
\[
\boxed{
W_{m,n+1}=W_{m,n}^{16}\,
e\!\left(h\sum_{j<m}r_j(n+1)\right),\qquad
W_{m,0}=1.} \tag{IQ6}
\]

**Proof:** The multiplication map \(\mu_m:(S^1)^m\to S^1\), \(\mu_m(z_0,\ldots,z_{m-1})=\prod_j z_j\), is a continuous group homomorphism. It commutes with the power map \(z\mapsto z^{16}\). Multiplying the individual exact source-rotated phase recurrences gives IQ6 term by term. In SUCC's actual two-sector partition \(r_o=r_a+r_r\), this becomes IQ5 and retains the original four-pole source without changing initial seed.

There is a coherent commuting source/gluing diagram at **EVERY finite group size**, and these observations coexist in the same compatible infinite cluster state. What does NOT follow is time distribution of \(W_{m,n}\). The homomorphism law holds identically for coherent wrong-seed extensions too (with the correctly transported initial values). This is an exact dynamic composition law, not a contraction estimate, a measured energy force, or a normality theorem.

## IQ-05: the sharp normality and logical-consistency firewalls

For any source time n, the global state \(\omega_{n,h}\) is a pure, compatible, genuinely multipartite-entangled algebraic state. Yet
\[
\boxed{\frac1A\sum_{n\in I}\omega_{n,H_A(h)}(B_2)
=\frac1A\sum_{n\in I}e(H_A(h)U_n)}
\]
is EXACTLY the same unknown original high-depth Weyl statistic. Its smallness is NOT obtained by preparing an infinite entangled state.

**Wrong-seed test.** The same forcing with changed seed \(s_*=-\pi/16\) has \(U_n(s_*)=-T_n\to0\), with \(T_n=\sum_{k\ge1}16^{-k}r_o(n+k)\). Applying the identical cluster encoding at angles \(2\pi hU_n(s_*)\) produces a perfectly compatible pure infinite graph state at every time, with one ebit across every contiguous cut and a complex witness \(\omega_{n,h}(B_2)\to1\) for each fixed h. Thus graph-state compatibility and many-body entanglement do NOT imply base-16 normality. The literal zero-seed arithmetic/carry and source-specific signed estimate remain load-bearing.

A completely separable single equatorial qubit state can likewise realize any individual complex phase witness \(\langle X+iY\rangle=e^{i\theta}\); the graph's entanglement is useful for a *source-labelled group of distributed observables*, not logically necessary to encode one scalar phase.

**Simultaneous state ≠ simultaneous sharp truth of noncommuting measurements.** A global state assigns consistent joint expectations where observables commute and valid probabilities to each measurement context; it does not give simultaneous dispersion-free values to all noncommuting projections. An infinite chain should be treated as a compatible state on the quasilocal observable algebra, not an automatically meaningful 'wavefunction of all mathematical truth'.

## Next mathematics that can change the π verdict

The graph construction is a rigorously compatible **supporting carrier** for all finite original-source angular/radial phase observations. The actual missing theorem is still a source-authenticated signed bound (or a direct fixed-h Weyl theorem) for the selected original U0=0, distinguishing the coherent same-forcing wrong seed. A genuinely new direction would derive an additional interaction or local stabilizer/carry constraint that is not freely programmable from U_n and that quantitatively restricts the time variation of \(\omega_{n,h}(B_2)\). Require fresh independent source oracles and falsification against wrong seeds and the #505 ternary mutant.

### Scholarly sources (classical facts, not original π-normality theorems)

- Infinite quasilocal spin C*-algebras and normalized positive states: https://link.springer.com/article/10.1007/s00220-026-05571-y and https://link.springer.com/article/10.1007/s00023-026-01768-y .
- Graph/cluster states and stabilizers: https://pmc.ncbi.nlm.nih.gov/articles/PMC9021024/ and https://www.cpsjournals.cn/en/article/doi/10.1088/0256-307X/43/7/070601 .
- Parent #511 source-paired Bell encoding and rational-time cohomology: https://github.com/femboy2112/SUCC/pull/511 .

**Claim scope:** IQ1-IQ5 paper-derived exact algebra and quasilocal state construction; finite controls are diagnostic, not proof of an infinite theorem. New globally novel scholarship, physical entanglement of π digits, algorithmic quantum speedup, source-selected Weyl decay, base-16 normality of π and RH remain UNVERIFIED/OPEN.
