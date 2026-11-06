# Quantized arithmetic atoms? Sphere-covering charge, chosen Hamiltonians, and the spectral limit

**2026-11-05 — additive research extension to SUCC's gauge-coded sphere-tower preregistration, descendant of draft #515 at SHA \`2ea21654bfe1f1ec1e4310ef5f71a653200f3e84\`.** All original four signed BBP poles and literal zero seed remain untouched. Existing #499/#510/#513/#515 work is inherited context. This is classical complex geometry, geometric quantization, spectral theory and an arithmetic specialization. **No physical energy spectrum of π, π normality, RH or world-first novelty is claimed.**

## A. Exact authenticated sphere tower

Let \(e(x)=\exp(2\pi i x)\). SUCC's source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\qquad U_n=16U_{n-1}+r(n).
\]

On \(\mathbb{CP}^1\) in homogeneous coordinates define \(P_n([Z:W])=[e(r(n))Z^{16}:W^{16}]\). The composition is the **exact algebraic identity**

\[
F_n=P_n\circ\cdots\circ P_1,\quad
F_n([Z:W])=[\Xi_n Z^{d_n}:W^{d_n}],\qquad
d_n=16^n,\quad\Xi_n=e(U_n).
\]

Every \(P_n\) is a degree-16 holomorphic branched cover; the composition has degree \(d_n\) with ramification at zero and infinity. The map degree does **not** count new physical particles, and its inverse fibers are alternative roots, not measured quantum-superposition amplitudes. The chronological forward BBP orbit is NOT equivalent to sampling Haar on those inverse fibers.

## B. A genuine integer flux at each finite depth

Take the positive hyperplane line bundle \(\mathcal O(1)\to\mathbb{CP}^1\). Its pullback under \(F_n\) is \(\mathcal L_n=F_n^*\mathcal O(1)\cong\mathcal O(d_n)\), with

\[
\boxed{\int_{\mathbb{CP}^1}c_1(\mathcal L_n)=d_n=16^n.}
\]

This follows from the degree of a holomorphic self-map of a sphere; it is **topological quantization**, independent of any Hamiltonian. Riemann–Roch for genus zero (equivalently, homogeneous polynomial sections of degree \(d_n\)) gives

\[
\boxed{\mathcal H_n:=H^0(\mathbb{CP}^1,\mathcal O(d_n)),\quad
\dim_\mathbb C\mathcal H_n=d_n+1.}
\]

With the **chosen standard** round-sphere/Hermitian SU(2)-equivariant quantization, this Hilbert space is the irreducible spin \(j_n=d_n/2\) representation. It has \(d_n+1\) magnetic labels \(m=-j_n,-j_n+1,\dots,j_n\). This is a mathematical quantization model built *on* SUCC's coverings; the BBP recurrence alone does not prescribe a Hilbert inner product or a Hamiltonian.

## C. A declared monopole Hamiltonian gives literal discrete levels

Choose a round sphere of radius \(R>0\), a mass \(M>0\), \(\hbar>0\), and the **constant-curvature** magnetic monopole connection of Chern charge \(d_n\) on \(\mathcal O(d_n)\). Its spinless covariant kinetic Hamiltonian has the familiar monopole-harmonic spectrum

\[
\boxed{E_{n,k}=\frac{\hbar^2}{2MR^2}
 \left[(d_n/2+k)(d_n/2+k+1)-(d_n/2)^2\right]
 =\frac{\hbar^2}{2MR^2}\left[\frac{d_n}{2}(2k+1)+k(k+1)\right]}
\]

for \(k=0,1,2,\ldots\), and degeneracy \(d_n+2k+1\). In the convention \(E_{\rm scale}=\hbar^2/(2MR^2)\), the ground energy is \(d_n/2\) and first gap \(d_n+2\), in units of \(E_{\rm scale}\). At depth \(n=1\): \(d_1=16\), lowest degeneracy \(17\), energies \(8,26,46,\ldots\) (**note:** the third level is \(d/2\cdot5+6=46\)); at depth \(n=2\): \(d_2=256\), lowest degeneracy \(257\), ground energy \(128\).

**Non-negotiable distinction:** this standard uniform-monopole connection is a **chosen representative** of the same topological Chern class. The connection directly *pulled back* by \(F_n\) is generally NOT constant curvature for \(d_n>1\), so these simple monopole harmonic eigenvalues must not be asserted for the raw nonuniform pulled-back connection. Nor do \(R,M,\hbar\) come from SUCC arithmetic.

A still simpler alternative is the ordinary scalar round-sphere Laplacian: \(E_\ell=\hbar^2\ell(\ell+1)/(2MR^2)\), degeneracy \(2\ell+1\); it has no dependence at all on the degree \(d_n\). **Geometric topology does not select a unique energy operator.**

## D. A sharp source-blindness theorem for the most natural curvature

Normalize the Fubini–Study form by

\[
\omega_{\rm FS}=\frac{i}{2\pi}\frac{dz\wedge d\bar z}{(1+|z|^2)^2},
\qquad \int_{\mathbb{CP}^1}\omega_{\rm FS}=1.
\]

For \(\Xi\in S^1\), \(d\in\mathbb N\), and \(F(z)=\Xi z^d\),

\[
\boxed{F^*\omega_{\rm FS}
=\frac{i}{2\pi}\frac{d^2|z|^{2d-2}}{(1+|z|^{2d})^2}dz\wedge d\bar z.}
\]

**The right-hand side contains NO \(\Xi\).** Its integral is exactly \(d\), via the elementary substitution \(x=r^{2d}\) in polar coordinates:

\[
\int_{\mathbb{CP}^1}F^*\omega_{\rm FS}
=2d^2\int_0^\infty \frac{r^{2d-1}}{(1+r^{2d})^2}\,dr
=d.
\]

Therefore original zero seed, the coherent same-forcing wrong seed \(s_*=-\pi/16\), a rational shift seed, and even a mutated phase forcing produce *identical* degree-\(d_n\) topological charges and pulled-back curvature densities. This is an **exact no-go** for deriving BBP-selected equidistribution from flux, Fubini–Study curvature or source-blind monopole eigenvalues alone. Pullback curvature is nonuniform for \(d>1\) (it vanishes at branch points in a local coordinate); no silent substitution of uniform-monopole eigenvalues is permitted.

## E. Where source specificity ACTUALLY resides: coherent section transport

Using homogeneous coordinates, pull back a section \(Z^jW^{k-j}\) of \(\mathcal O(k)\) along \(F_n\):

\[
\boxed{F_n^*(Z^jW^{k-j})
=\Xi_n^j Z^{d_nj}W^{d_n(k-j)}.}
\]

The source disappears from the Chern number but survives as a **relative coefficient \(\Xi_n^j=e(jU_n)\)**, provided an endpoint/trivialization convention is retained. In a free gauge it is removable along a linear chain; with anchored endpoints it is observable as a source-dependent transport phase. The normalized chronological sum of the \(j=1\) phases is *exactly* the still-open SUCC fixed-frequency Weyl observable. This is a source-preserving location for the "gauge code," **not** a new signed bound.

For an initial state \(s\), \(U_n(s)=U_n(0)+16^ns\); all Chern/curvature levels agree while source-anchored phase transport differs by \(e(j16^ns)\). A true SUCC energy claim would require a declared self-adjoint, source- and anchor-dependent Hamiltonian and a discriminating inequality between these cases.

## F. Infinite Russian-doll limit: quantized labels without an energy gap

On the UNIT CIRCLE boundary (not all of \(\mathbb{CP}^1\)), define the **standard** 16-adic solenoid

\[
\Sigma_{16}=\varprojlim(S^1,z\mapsto z^{16}).
\]

Its Pontryagin dual is exactly the direct limit \(\mathbb Z\xrightarrow{\times16}\mathbb Z\xrightarrow{\times16}\cdots\), isomorphic to \(\mathbb Z[1/16]\). The character at level \(n\), frequency \(m\in\mathbb Z\), is identified across levels with frequency \(q=m/16^n\), because \((m,n)\sim(16m,n+1)\).

One **possible**, explicitly CHOSEN longitudinal spectral operator on Haar \(L^2(\Sigma_{16})\) is diagonal on its Fourier characters, with eigenvalues

\[
H\chi_q=\kappa q^2\chi_q,\qquad q\in\mathbb Z[1/16],\ \kappa>0.
\]

This is a legitimate self-adjoint diagonal operator (with its maximal weighted-domain closure), and its eigenlabels are countable. But \(\mathbb Z[1/16]\) is dense in \(\mathbb R\): \(q_n=16^{-n}\to0\), so positive eigenvalues \(\kappa16^{-2n}\to0\); indeed their closure fills \([0,\infty)\). **There is no strictly positive spectral gap in this model.** A tower with quantized finite levels need not preserve finite separation in its infinite virtual limit. This operator and its scale \(\kappa\) are NOT canonically imposed by the SUCC recurrence; fixed-radius finite-sphere monopole Hamiltonians have a different scale behavior.

With the source-twisted finite map, character pullback is
\(P_n^*(z^m)=e(mr(n))z^{16m}\).
The source enters as a phase, while the degree/frequency refinement remains \(m\mapsto16m\). On a chain the phase twist admits a gauge; there is no intrinsic source-selected gap or nontrivial two-direction curvature without an independently specified transverse source action.

## G. Gamma connection as a TRUE spectral transform

For the standard UNIT round-sphere scalar Laplacian (not the BBP source operator), its nonzero eigenvalues are \(\lambda_\ell=\ell(\ell+1)\), multiplicity \(2\ell+1\), \(\ell\ge1\). Define \(\Theta(t)-1=\sum_{\ell\ge1}(2\ell+1)e^{-t\lambda_\ell}\). For \(\Re s>1\), absolute convergence and Euler's Gamma integral give

\[
\boxed{\Gamma(s)\zeta_{\Delta}(s)
=\int_0^\infty t^{s-1}[\Theta(t)-1]dt,\quad
\zeta_\Delta(s)=\sum_{\ell\ge1}\frac{2\ell+1}{[\ell(\ell+1)]^s}.}
\]

This is a **rigorous Gamma ↔ quantized sphere spectrum** (Mellin/heat-kernel) interface. It does not identify \(\zeta_\Delta\) with the Riemann zeta function, nor establish a spectral model of RH or π normality.

## H. Controls, validation scope, decision boundary

- Exact symbolic proof: projective composition and pullback degree; homogeneous section basis; Fubini–Study pullback and its integral; source-phase-only coefficient; solenoid dual; nonzero-gap absence.
- Independent finite probes: original four-pole forcing vs collapsed rational formula; unwrapped literal \(U_0=0\) state and odd denominators; bounded finite-tail gauge identity without π digits; stage energies/degeneracies; sphere curvature at separate phase sources; odd-torsion inverse-branch discontinuity.
- Executed 45-digit independent mpmath integrals for pulled-back flux at \(d=1,16,256\) each recovered \(d\); finite heat-trace Mellin check at \(s=2.25\) recovered the Gamma-weighted eigenvalue sum. These are diagnostics, **not** proof of general identities.
- Hostile controls: coherent wrong seed, source tap mutation, SU(2) sideways-conjugate axis and scalar Laplacian. All disallow a jump from integer flux to source-selected normality.

**Claim ledger:** integer Chern degree, holomorphic-section count, source-blind curvature and source-bearing section phase = **DISCLOSED** algebraic/classical within declared models; monopole energy levels = **DISCLOSED conditional on the chosen standard kinetic Hamiltonian and uniform connection**; solenoid gaplessness = **DISCLOSED for the chosen longitudinal operator**; exact arithmetic physical energy levels, independent source curvature, new π signed rate, base-16 π normality and RH = **UNVERIFIED/OPEN**.

**Primary/context references:** Toronto geometric quantization lecture notes (CP1 O(k) sections), https://www.math.toronto.edu/~jeffrey/mat1312/lec14.gq.pdf ; Nature Communications Physics, https://www.nature.com/articles/s42005-025-02208-9 (spherical monopole Hamiltonian); prior SUCC #499, #510, #513, #515. None is a proof of source-selected BBP normality.
