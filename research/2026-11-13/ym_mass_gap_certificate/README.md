# SUCC × Yang–Mills: physical-time spectral mass certificate

**2026-11-13 | Research, not a mass-gap proof | stacked on SUCC draft PR #614**

**Parent:** https://github.com/femboy2112/SUCC/pull/614 (gauge-complete Wilson observers; branch head 0faa85a798de5b0b9af4d62295f405165b408eb7).
**Independent complementary research:** https://github.com/femboy2112/SUCC/pull/613 (Haar / successor / Wilson / reflection adapters).

## Truth boundary / primary sources

The original OpenAI October 2026 formal target is YangMills.JointExistence in:
https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean

It supplies a Wilson family, a selected phase/hierarchy, local operator content and a selected centeredTrace two-point function. It **does not contain a positive physical Hamiltonian mass-gap assertion**. The independent working-group acceptance guide explicitly excludes confinement, infinite-volume uniqueness and a mass gap; its positive lattice probe is not an intrinsic positive continuum reference mass:
https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/docs/checks.md

Clay's full target (unsolved): https://www.claymath.org/millennium/yang-mills-the-maths-gap/

This dossier states independent elementary spectral lemmas and calibrated finite probes. It does **not** rebuild upstream Lean, prove all-field OS reconstruction, instantiate actual SU(2)/SU(3) 4D dynamics, or prove a YM gap. Physical mass units require a declared RG normalization.

## MG1: the one-physical-time dense-bank theorem (PROVED; classical spectral theory)

Fix a reconstructed physical Hilbert space, a nonnegative self-adjoint Hamiltonian H, a normalized unique vacuum Ω spanning ker H, and a sequence (ψ_i) dense by linear span in Ω⊥. For **one physical time t★ > 0**, let T=e^{-t★H}. The finite Hermitian matrices are

\[
C_N(0)_{ij}=\langle \psi_i,\psi_j\rangle,\qquad
C_N(t★)_{ij}=\langle\psi_i,T\psi_j\rangle.
\]

If a single q with 0<q<1, **independent of N**, satisfies

\[
\boxed{\forall N\ge1:\quad 0\preceq C_N(t★)\preceq q C_N(0),}
\tag{MG1}
\]

then

\[
\boxed{\sigma(H|_{\Omega^\perp})\subseteq [-\log(q)/t★,\infty),\qquad
\Delta\ge-\log(q)/t★>0.}
\]

Conversely H|Ω⊥≥m implies (MG1) with q=exp(-m t★). This is equivalence to the target, NOT a derivation of a source estimate.

**Proof:** Any finite linear combination ψ of the bank satisfies
0≤〈ψ,Tψ〉≤q||ψ||² by the Loewner inequality. Boundedness of T and density extend the inequality to Ω⊥. This subspace reduces H; positivity of T yields ||T|Ω⊥||≤q. The spectral mapping formula for exp(-t★H) implies every positive-energy spectral value E obeys exp(-t★E)≤q, hence E≥-log(q)/t★. Conversely apply functional calculus to H≥m. No generator-domain assumption on bank vectors is needed.

If vacuum uniqueness is not proved, use (ker H)⊥ and explicitly control all zero modes. A bound for just one scalar channel (e.g. centeredTrace) does NOT certify the full Hamiltonian.

## MG2: precisely how the lattice limit would transmit the gap (CONDITIONAL PROOF)

Let a_r→0 and physical-time tick counts n_r satisfy t_r=n_r a_r→t★. Let source-selected, vacuum-centered, OS-reflection **Gram matrices from the same Wilson law and the same chosen continuum phase** satisfy, for every fixed N:

- C_{r,N}(0)→C_N(0) and C_{r,N}(t_r)→C_N(t★) entrywise;
- one fixed 0<q<1 works for all sufficiently advanced cutoffs r, with the threshold r_0 permitted to depend on N:
  0≼C_{r,N}(t_r)≼q C_{r,N}(0);
- the limiting bank is dense in the **physical OS vacuum complement**.

The finite PSD cone is closed under entrywise limits. Thus MG1 holds for every N and gives Δ≥-log(q)/t★.

**Quantifier trap:** the same selected source, Wilson coupling schedule, extraction/phase and time normalization must serve every entry of every bank. A fresh phase/subsequence per test is invalid. Positivity at each cutoff without a q<1 uniform in physical units is invalid. Continuum ultraviolet convergence alone is invalid.

A legitimate OS bank starts from positive-time, gauge-invariant, smeared Wilson/spin-network words F_i, with ψ_i=[F_i−ω(F_i)1]_OS and matrix elements 〈ψ_i,e^{-tH}ψ_j〉_OS. This avoids comparing a contact-divergent unsmeared coincident covariance to the physical Hilbert norm. SUCC #614's nonabelian simultaneous-conjugacy and noncontractible-holonomy counterexamples make mixed loop words and global topological channels load-bearing. Density/cyclicity must be established; it is not automatic from a finite list of traces.

## MG3: Haar coarse/detail spectral margin (CONDITIONAL PROOF)

Construct an **orthogonal splitting in the physical, interacting OS inner product**, not merely Haar L²:

\[
\Omega^\perp=\mathcal C\oplus\mathcal D,
\]

where C is gauge-complete coarse information and D includes **every retained fine wavelet/detail channel**. For T=e^{-t★H} put

\[
\|P_CTP_C\|\le\alpha,\quad \|P_DTP_D\|\le\beta,\quad
\|P_CTP_D\|\le\gamma.
\]

Then by self-adjointness, positivity and Cauchy–Schwarz, for f=c+d,

\[
0\le\langle f,Tf\rangle\le
\alpha\|c\|^2+2\gamma\|c\|\|d\|+\beta\|d\|^2.
\]

Consequently the **strict checkable condition**

\[
\boxed{\alpha<1,\ \beta<1,\ \gamma^2<(1-\alpha)(1-\beta)}
\tag{MG3}
\]

implies λ_max([[α,γ],[γ,β]])=:q<1 and Δ≥-log(q)/t★.
For an all-rational certificate, find positive w_C,w_D and q<1 with

\[
\alpha w_C+\gamma w_D\le q w_C,\qquad
\beta w_D+\gamma w_C\le q w_D .
\]

Weighted AM–GM bounds the quadratic form by q||f||². Example α=2/5, β=3/5, γ=1/10, weights (1,1) give q=7/10 and conditional Δ≥log(10/7)/t★.

**Hostile coherent mutation:** a positive transfer [[3/5,2/5],[2/5,3/5]] has eigenvalues 1 and 1/5. Each diagonal block contracts (3/5), yet the mixed coherent channel yields a non-vacuum zero mode. MG3 fails at equality γ²=(1−α)(1−β). Suppressing detail/coherent off-diagonals manufactures a false gap. Source-weighted orthogonalization is mandatory; the raw Haar decomposition need not be OS orthogonal.

## MG4: a verified-error matrix oracle (PAPER PROOF; no source errors claimed)

For *real-symmetric* rational or exact Q(i) *complex-Hermitian* matrix approximants \hat C_0,\hat C_t with independently **proved complex-modulus entrywise** errors ε_0,ε_t, the finite-dimensional sufficient condition

\[
\boxed{q\widehat C_0-\widehat C_t-N(q\epsilon_0+\epsilon_t)I\succeq0}
\tag{MG4}
\]

guarantees q C_0−C_t≽0. Proof: any Hermitian error E with |E_ij|≤ε obeys
|v*Ev|≤ε(Σ|v_i|)²≤Nε||v||². This gives a conservative rational margin; a claimed numerical error radius without an independent Wilson-source bound is NOT a certificate.

An exact Gram oracle checks *all* principal minors (including singular/null banks), not only leading minors. Retain Q(i) coherence rather than dropping imaginary channels. This does NOT validate that input matrices are produced by an OS-positive Wilson source.

## MG5: exact adversarial physical-time examples (ELEMENTARY PAPER DERIVATIONS + TESTS)

Let a=1/n and T_a=(1+ε_a)⁻¹[[1,ε_a],[ε_a,1]], so the vacuum has eigenvalue 1 and the excited mode has r_a=(1−ε_a)/(1+ε_a). **Physical time t★=1** is n transfer ticks.

*Gapped toy:* ε_a=1/(4n). Set x=1/(4n). Exact algebra gives
r_a≤(1+2x)⁻¹ and (1+2x)^n≥1+2nx=3/2. Hence
r_a^n≤2/3 for **all n≥2**. MG1 certifies a toy lower bound m≥log(3/2); the actual limit is m=1/2. **This is not a Yang–Mills mass.**

*Gapless toy:* ε_a=1/n². Then r_a=1−2/(n²+1), whence Bernoulli gives
1−2n/(n²+1)≤r_a^n≤1. Thus r_a^n→1 and the continuum physical mass tends to zero despite a strictly positive lattice gap for every n.

*Incomplete bank:* T_a has excitation eigenvalues 1−1/n² and 1−1/n. An observer testing only the fast latter channel passes a fixed-time q=1/2 uniformly. Including the missing slow channel destroys every uniform q<1 as n→∞. A single positive scalar correlator cannot certify the complete physical theory.

*Source/coherence controls:* exact Q(i) mixed-bank tests preserve nonzero imaginary cross terms, reject non-Hermitian inputs, and distinguish genuine Q(i) PSD from oversized coherent/matrix error bounds. Null and duplicate bank vectors are checked without unjustified Gram inverses.

These toy models are finite positive semigroups, not an OS reconstruction of 4D compact-simple-group Yang–Mills. They calibrate logical implications and failure modes.

## What SUCC must actually prove next (one explicit source-specific target)

1. Bind every channel to the **same** official Wilson plaquette measure, the registered OS reflected field hierarchy, one selected phase, and one physical time t★. Use #613's SU(2) Wilson/Haar law and #614's gauge quotient as finite starting points, not a physical-Hamiltonian identification.
2. Build complete nonabelian spin-network/Wilson mixed-word observer banks on true 4D slabs. Prove cyclic density **after OS quotient** and carry global sectors separately. Retain all Haar detail modes and coherent cross terms.
3. Derive a **source-selected, coupling/volume/cutoff-uniform** q<1 from Wilson conditional distributions or controlled multi-scale RG at a fixed physical slab size. A possible route is MG3 with independently bounded α,β,γ, source-state distortion and boundary/large-field error estimates. This is the real OPEN mathematical barrier, not a hidden consequence of the existence proof.
4. Prove the same-phase two-time Gram convergence and source/field normalization along the already constructed continuum extraction. Invoke MG2 to obtain Δ>0; quantify the lower bound and compare it with the declared renormalization scale.
5. Hostile probes: wrong coupling, global flat holonomy, omitted wavelet detail, incomplete trace marginals, gapless positive transfer, nonpositive/reflection-negative kernels, cutoff-twin families, complex off-diagonal phase mutation.

**Next falsifier:** an authentic *small* SU(2) Wilson slab with positive-time mixed spin-network words, exact or rigorously enclosed source integrals, and verified OS Gram matrices. Pass means valid source and an error-certified contraction *at that finite scale*; fail means explicit slow/coherent channel or an invalid source identity; ambiguous means tighten interval bounds. Finite pass never promotes to an all-scale theorem.

## Claim ledger / authority

| Claim | Verdict | Boundary |
|---|---|---|
| Existence theorem of October 2026 | EXTERNAL ASSESSED | No gap or unique thermodynamic limit in this theorem |
| MG1 fixed-time dense-bank equivalence | DISCLOSED classical spectral lemma | No source-derived q |
| MG2 continuum-transfer implication | DISCLOSED conditional limit lemma | Needs actual single-phase Wilson/OS convergence |
| MG3 complete coarse/detail bound | DISCLOSED conditional quadratic-form lemma | Needs physical OS-orthogonal split and true Wilson block bounds |
| MG4 exact/complex PSD and margin | DISCLOSED finite algebra | Error budgets not provided by the Wilson source |
| MG5 toy dynamics and mutations | DISCLOSED paper algebra / OBSERVED local tests | Not 4D YM |
| Actual pure YM continuum positive mass | UNVERIFIED / OPEN | Prove source-selected uniform q, bank density, physical limits |

**Validation authority:** an isolated Python 3.13.5 implementation of MG1/MG3/MG4 and toy probes passed 21 focused tests, including rational Q(i) Hermitian mutants. It is not an external verification of YM, and it does not substitute for full SUCC repository gates. The exact runnable implementation is being staged separately. No CI, upstream Lean/Comparator or full SUCC suite is claimed here.

Do not merge, tag, release or promote the mass gap until the above source-dependent obligations and AGENTS.md gates are discharged.