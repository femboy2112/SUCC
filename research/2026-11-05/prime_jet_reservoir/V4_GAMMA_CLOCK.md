# Post-preregistration discovery: the four-sheet Gaussian prime clock and Gamma-weighted unitary transport

**2026-11-05, research-only.** This is a *new-to-this-branch* construction obtained AFTER the chronological prime-jet preregistration. It is not an independently blind oracle or claimed world-first construction. Sources: #499's V4 prime-Frobenius character decomposition, #515's log16 Gamma solenoid, #516's finite sphere/gauge tower, and the classical Euler-product prime log weights. The circle×finite-group model below is CHOSEN; there is no known intertwiner to SUCC's literal-zero-seeded BBP digit orbit or the entire Weil zeta quadratic form.

## 1. An exact FOUR-sheet (not merely two-sheet) prime-class fiber

Let \(G_8=(\mathbb Z/8\mathbb Z)^\times=\{1,3,5,7\}\cong C_2\times C_2\); its four real characters are \(1,\chi_{-4},\chi_8,\chi_{-8}\). This is exactly the abstract group/character set acting on SUCC #499's rational eight-tap source, although the following regular representation is a DIFFERENT representation from those 8-tap monomial operators. The ORIGINAL prime-orbit source module lies only in the \(1\oplus\chi_{-4}\) isotypic sum.

Put \(\Lambda=\log16\) and
\[
\boxed{X=(\mathbb R/\Lambda\mathbb Z)\times G_8.}
\]
For any positive ODD integer \(m\), define the compatible action
\[
\boxed{T_m(v,a)=(v+\log m\bmod\Lambda,\,[m]_8\,a).}\tag{FG1}
\]
It obeys \(T_m T_n=T_{mn}=T_nT_m\) by the logarithm and multiplication mod8. For p=2 the residue is NOT invertible and this formula is invalid: the special 2-primary clock must be treated separately. This is not a nonzero gauge curvature; it is a flat action with a finite arithmetic fiber. The minimal two-sheet model of THEOREMS.md is the quotient keeping only χ_-4.

On Haar \(L^2(X)\), set \(U_p f=f\circ T_p\) for odd p. The modes
\[
\Phi_{h,\chi}(v,a)=e^{2\pi i h v/\Lambda}\chi(a),\qquad h\in\mathbb Z,\;\chi\in\widehat G_8,
\]
form a complete orthonormal Fourier×finite-character basis, and
\[
\boxed{U_p\Phi_{h,\chi}
=\chi(p)e^{2\pi i h\log p/\Lambda}\Phi_{h,\chi}.}\tag{FG2}
\]
This is an operational common-basis transport—not an analogy between unrelated Hilbert spaces. The source-prime phase and the real Gamma logarithmic rotation appear as INDEPENDENT factors in one unitary eigencharacter.

## 2. A CHOSEN compact-clock prime-jet Hamiltonian with exact levels

For any odd prime p and k≥1, set \(w_{p,k}=\log p/p^{k/2}\). Define on \(L^2(X)\)
\[
\mathsf J_{p,k}=-w_{p,k}(U_p^k+U_p^{*k}).
\]
It is bounded self-adjoint. FG2 gives its complete point eigenvalue formula:
\[
\boxed{E_{p,k}(h,\chi)=
-2w_{p,k}\operatorname{Re}\left[
  \chi(p)^k e^{2\pi i h k\log p/\Lambda}
\right].}\tag{FG3}
\]
These are mathematical interaction energies in a DECLARED compact-clock model, not actual zeta zero ordinates or physically observed particle energies.

For every odd p, \(\log p/\Lambda\) is irrational. Therefore the eigenvalue set for any fixed character χ and k is DENSE in [-2w,2w] and
\[
\boxed{\operatorname{spec}(\mathsf J_{p,k})=[-2w_{p,k},2w_{p,k}].}\tag{FG4}
\]
Crucial spectral-type precision: all \(\Phi_{h,\chi}\) are actual eigenvectors, so the representation is pure point with **dense point eigenvalues**; an interval spectrum does NOT imply continuous spectral measure. The endpoints may be eigenvalues in some sectors (h=0) and otherwise limit points.

For the standalone 2-primary circle shift \(U_2 f(v)=f(v+\log2)\), \(U_2^4=I\), so its k=1 signed jet has exactly the THREE spectral values
\[
\boxed{\operatorname{spec}[-w_{2,1}(U_2+U_2^*)]=\{-2w_{2,1},0,2w_{2,1}\}.}\tag{FG5}
\]
At k=4, the shift is the identity and \(\mathsf J_{2,4}=-2w_{2,4}I\). The 2-primary branch is algebraically periodic; odd-prime branches have dense signed energy labels in this particular compact-clock quantization.

This is different from THEOREMS.md's L²((-L,L)) path-jet operator: finite support has a finite set of eigenVALUES determined by its cutoff, while a compact circle with irrational rotation has densely many. Different boundary conditions and different state spaces = no contradiction, and they cannot be silently equated.

## 3. The Gamma probability measure demands a unitary Jacobian

The source-faithful Γ log16 periodized density from SUCC #515 is
\[
p_\Lambda(v)=\sum_{j\in\mathbb Z}\exp(v+j\Lambda-e^{v+j\Lambda}),\quad
0\le v<\Lambda.
\]
It is strictly positive and smooth, with nonzero Fourier coefficients \(\Gamma(1-2\pi i h/\Lambda)\); it is NOT Haar. A bare composition shift \(f\mapsto f\circ T_p\) does **not** preserve \(L^2(p_\Lambda(v)\,dv\times\mathrm{uniform}(G_8))\) norm.

The CORRECT unitary Γ-weighted transport for odd p is
\[
\boxed{
(U^\Gamma_p f)(v,a)=
\sqrt{\frac{p_\Lambda(v+\log p)}{p_\Lambda(v)}}
\,f(v+\log p,\,[p]_8a).
}\tag{FG6}
\]
The density is evaluated modulo Λ. Let \(V:L^2(p_\Lambda dv)\to L^2(dv)\) be the unitary multiplication \(Vf=\sqrt{p_\Lambda}\,f\). Then
\[
\boxed{U^\Gamma_p=V^{-1}U_pV.}\tag{FG7}
\]
Thus the properly Jacobian-transported Γ-clock jet \(J^\Gamma_{p,k}=-w(U_p^{\Gamma\,k}+U_p^{\Gamma\,*k})\) has EXACTLY the same spectrum as FG3; gamma weighting alone does not create a new source-selected negative gap or eigenvalue shift. It changes how raw observations are weighted, not the unitary equivalence class. This is a rigorous **Gamma/source-map compatibility and no-go theorem**, and it pays the Jacobian demanded by #515's sideways-sphere warning.

## 4. Prime-to-2 and source-contract boundaries

- The arithmetical \(\chi_{-4}\) phase here is the SAME character as #499's genuine source eigenspace, but this is NOT proof that a p^k shift eigenmode equals #499's p-local congruence at a finite index. The latter has domain hypotheses p>8k and exceptional primes 2,3,5 in different source statements. Never use generic p=3,5 congruence out of scope.
- The V4 regular fiber includes χ_8 and χ_-8 modes not present in the original selected two-dimensional source orbit. They are control directions, not additional π periods.
- The Dirichlet L-function twisted Euler factors would use χ(p)^k but also require THEIR OWN gamma parity factors and zero side; the compact-clock jet is neither the Dirichlet completed trace formula nor Weil positivity.
- Source-mutated BBP initial seeds leave FG1–FG7 intact because those are prime-clock/fiber laws independent of the literal zero seed. Any transfer to π normality needs a new original-carry-dependent signed bound.
- The V4 fiber repairs the impossibility of representing χ_-4 as a continuous character of the real log clock alone. This is a **two-sorted geometric/arithmetic extension**; all T_m commute, so neither classical gauge curvature nor physical energy borrowing follows.

## 5. Verdict-changing next probe

Choose a precise common Hilbert space and source-preserving intertwiner \(\mathcal I\) from (i) an authenticated chronological BBP section \(\Xi_n=e(U_n)\), including integer carry and U0=0, to (ii) the four-sheet Γ–prime-clock model. Demand a NON-TAUTOLOGICAL coefficient/spectral bound that distinguishes the coherent wrong BBP seed \(s_*=-\pi/16\) and odd-torsion J-lifts from #515. Alternatively, for RH target the ACTUAL full Guinand–Weil Γ+pole+prime operator on compactly supported tests; the torus Hamiltonian alone is not Weil's operator. Without an identified source-bearing transport and quantified signed inequality, stop at an exact arithmetic-gauge model.

**Claim status:** FG1–FG7 paper-proved within stated chosen models and classical theorems; finite probes are implementation observations; independent academic novelty unverified; new RH or π-normality estimates absent.
