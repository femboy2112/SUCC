# UNIT-PAIR ZERO: an exact relational lift, a quantum-information analogy, and nontrivial rational-time source cohomology

**2026-11-05, research-only.** Pinned parent draft #509 head \`16b0809b1f1426e77dad52381c3ac3fbeb187e3f\`; historical SUCC original source and zero seed unchanged. This document distinguishes (1) an exact source-labelled algebraic pairing, (2) a freely CHOSEN normalized two-qubit embedding, and (3) a genuine obstruction in rational-time cohomology. No physical entanglement, physical energy borrowing, π normality, RH, or worldwide mathematical novelty is inferred for the actual BBP source.

Conventions: \(e(x)=\exp(2\pi ix)\). Authentic original \(r_o(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)\), \(U_0=0,\ U_n=16U_{n-1}+r_o(n)\). Authentic radial taps \(w_r=(2,-2,-1,-2,-1/2,-1/2,1/4,0)\) yield \(r_r(n)=\sum_{j=1}^8w_{r,j}/(8n-8+j)\), zero-seeded radial \(Z_n\). From #499/#504: the discounted radial completed period is zero, although the finite radial source is nonzero.

## UP-01 — exact unit-pair gluing, with no invented interaction

For an additive group/module \(A\), the sequence
\[
0\longrightarrow A\xrightarrow{\Delta} A\oplus A
\xrightarrow{\delta}A\longrightarrow0,\qquad
\Delta(c)=(c,c),\quad \delta(a,b)=a-b
\tag{UP1}
\]
is exact and SPLIT: \(\ker\delta=\mathrm{im}\Delta\) and \(s(u)=(u,0)\) is a right inverse. Therefore \(\delta(1,1)=0\) does not, by itself, define a nontrivial extension, an entanglement measure, or physical energy.

The **additional** source contract defines a pair of rational trajectories
\[
a_0=b_0=1,\qquad
a_n=16a_{n-1}+\frac12r_o(n),\quad
b_n=16b_{n-1}-\frac12r_o(n).
\tag{UP2}
\]
Write \(c_n=(a_n+b_n)/2,\ d_n=a_n-b_n\). Then
\[
\boxed{c_n=16^n,\ d_n=U_n,\quad
a_n=16^n+U_n/2,\ b_n=16^n-U_n/2.}\tag{UP3}
\]
The initial zero is an initial *relation* between two matched units; the antisymmetric forcing makes the relative trajectory nonzero. The projection \(\delta\) loses the common mode, but the source-labelled lift retains it. The pair is uniquely determined only after imposing BOTH the original antisymmetric forcing and the homogeneous common-mode law. A generic lift can add arbitrary common-mode histories and cannot be inferred from \(\delta\) alone.

Let \(d^{\rm norm}_n=16^{-n}U_n=\sum_{j=1}^n16^{-j}r_o(j)\). The exact Mellin numerator \(P_o(t)=(1-t)(t^2+2)(t^2+2t+2)>0\) proves \(r_o(n)>0\) for n>=1. Direct fraction evaluation gives \(r_o(1)=47/15\). For n>=2, \(0<r_o(n)<4/(8n-7)\le4/9\). Hence
\[
\boxed{0\le d^{\rm norm}_n<
47/240+(4/9)\sum_{j=2}^{\infty}16^{-j}
=427/2160<1/5.}\tag{UP4}
\]
This bound is purely from authentic rational source data, not imported π digits. The completed BBP identity supplies \(d^{\rm norm}_n\to\pi/16\).

## UP-02 — an explicit genuine Bell-entangled TENSOR LIFT (conditional on the chosen tensorization)

Declare \(H_A=H_B=\mathbb C^2\) with local bases \(|0\rangle,|1\rangle\) and the bipartite tensor product \(H_A\otimes H_B\). This Hilbert embedding is **ADDITIONAL MODEL STRUCTURE**, NOT implied by the arithmetic identity.

Let \(|\Phi^\pm\rangle=(|00\rangle\pm|11\rangle)/\sqrt2\). Choose the unnormalized vector
\[
|\Psi_n\rangle=a_n|00\rangle-b_n|11\rangle
=\sqrt2\,16^n|\Phi^-\rangle+\frac{U_n}{\sqrt2}|\Phi^+\rangle.
\tag{UP5}
\]
Define \(\epsilon=\langle00|+\langle11|=\sqrt2\langle\Phi^+|\). Then
\[
\boxed{\epsilon|\Psi_n\rangle=U_n,\qquad
|\Psi_0\rangle=\sqrt2|\Phi^-\rangle,\quad
\epsilon|\Psi_0\rangle=0.}\tag{UP6}
\]
Here the "dark" Bell sector carries the common unit-derived history, while the "bright" Bell sector carries the source difference. The coherent dark state is NOT the zero vector. Its normalised version is a maximally entangled two-qubit state because its Schmidt rank is 2, with equal Schmidt coefficients.

The update
\[
|\Psi_n\rangle=16|\Psi_{n-1}\rangle+
\frac{r_o(n)}{\sqrt2}|\Phi^+\rangle
\tag{UP7}
\]
is **nonunitary** and describes deterministic algebraic amplitudes; it is not a physically valid closed-system Schrödinger evolution or an energy budget. Normalize only when computing quantum-information observables:
\[
|\widehat\Psi_n\rangle
=\frac{a_n|00\rangle-b_n|11\rangle}{\sqrt{a_n^2+b_n^2}}.
\]
Its reduced state on A is \(\operatorname{diag}(a_n^2,b_n^2)/(a_n^2+b_n^2)\). Because both coefficients are strictly positive by UP4, this is an entangled pure state with Schmidt rank 2 for every n. Its two-qubit negativity is
\[
\boxed{\mathcal N_n=\frac{a_nb_n}{a_n^2+b_n^2}
=\frac{4-d_n^2}{8+2d_n^2}>\frac{99}{202}
\quad(d_n=d^{\rm norm}_n,\ n\ge0).}\tag{UP8}
\]
At n=0, \(\mathcal N_0=1/2\); the literal BBP source gives the strict lower bound independent of π digits. The joint bright Bell projection probability is
\[
\boxed{p_{+,n}=|\langle\Phi^+|\widehat\Psi_n\rangle|^2
=\frac{d_n^2}{4+d_n^2}<1/101,}
\tag{UP9}
\]
zero exactly at n=0, positive thereafter, tending to \((\pi/16)^2/[4+(\pi/16)^2]\). This is a chosen encoded quantum probability, NOT the empirical distribution of π's base-16 digits or a physical detection prediction.

### The crucial entanglement falsifier

For the separable DEPHASED state
\[
\rho_{\rm mix,n}=\frac{a_n^2|00\rangle\langle00|+b_n^2|11\rangle\langle11|}
{a_n^2+b_n^2},
\]
both local reduced density matrices are IDENTICAL to those of the pure entangled state, yet
\[
\operatorname{tr}(\rho_{\rm mix,n}|\Phi^+\rangle\langle\Phi^+|)=1/2
\]
for every n. Only joint coherent observation distinguishes their cross-term.

Conversely the SEPARABLE product \(|+\rangle_A\otimes|-\rangle_B\) has \(\langle\Phi^+|+\!-\rangle=0\) too! Therefore **zero joint bright amplitude ALONE does not certify entanglement**. One must verify the independently specified tensor factors, pure-state rank/coherence, or an entanglement witness. The source/Bell embedding is a constructive example, not a necessary consequence of \(0=1-1\).

## UP-03 — the dynamical gluing class IS nontrivial over the rational source category

The split exact sequence UP1 is too weak to enforce a new interaction. Now equip the carrier with its genuine time-shift structure.

Let \(M=\mathbb Q(x)\), \(E f(x)=f(x+1)\), \(\partial_{16}=E-16\). The source is rational \(r_o(x)\), as is \(r_r(x)\). For each pole class \(a\in\mathbb Q/\mathbb Z\), define the finite sum
\[
R_a(f)=\sum_{k\in\mathbb Z}16^{-k}
              \operatorname{Res}_{x=a+k}f(x).
\tag{UP10}
\]
Only finitely many terms are nonzero for a rational function. The substitution \(j=k+1\) shows
\[
R_a(Ef)=16R_a(f),\quad R_a(\partial_{16}f)=0.
\tag{UP11}
\]
Consequently \(R_a\) descends to a linear functional on
\[
H_{\mathrm{time}}:=M/\partial_{16}M.
\]
This is a toolkit-relative rational-time cokernel, not an absolute or physical cohomology theory.

The REAL original source has only four pole residue classes, and the radial one has extra signed taps. Two independent source-labelled classes suffice:
\[
\begin{array}{c|cc}
a&R_a(r_o)&R_a(r_r)\\\hline
7/8 &1/2&1/4\\
3/4 &0&-1/4
\end{array}
\quad\Longrightarrow\quad
\boxed{\det=-1/8\ne0.}
\tag{UP12}
\]
Therefore \(\boxed{[r_o],[r_r]\text{ are linearly independent in }H_{\rm time}.}\)
Both are nontrivial: no rational function \(f(x)\) can trivialize either through \(r=\partial_{16}f\). This strengthens the source interpretation of #507 AD-4.

Crucially, the radial completed *analytic period* is ZERO:
\[
\boxed{\mathcal L(r_r)=\sum_{n=1}^\infty16^{1-n}r_r(n)=0,}
\]
because \(P_r(t)/(1-t^8/16)=2\,d\log F(t)/dt\) with \(F(0)=F(1)=1\). Yet \([r_r]\ne0\) in the *different*, rational-time cokernel. **The zero completed scalar conceals a nontrivial source-time obstruction.**

This is the strongest currently rigorous counterpart to "the field's self-cancellation preserves a relational coupling". The conclusion depends on a specified source category, a genuine time operator, and weighted pole residues. It does NOT establish a physical coupling force, tensor-product quantum entanglement, or π normality.

## UP-04 — one exact Bell "return loop" with the inherited τ threshold

Let the authenticated SUCC radial potential be
\[
G(t)=2\log\frac{2-t^2}{t^2-2t+2},\quad 0\le t\le1.
\]
From #504/#509, \(G(0)=G(1)=0\), \(G(t)>0\) internally, unique maximum \(G(\tau)=\log2\) at \(\tau=2-\sqrt2\), and \(G'(t)=K_{\rm rad}(t)\).

Independently choose a unitary LOCAL phase rotation on one factor of the Bell model:
\[
V(t)=e^{iG(t)Z_A/2}\otimes I_B,\quad
|\Omega(t)\rangle=V(t)|\Phi^-\rangle
=\cos(G(t)/2)|\Phi^-\rangle+i\sin(G(t)/2)|\Phi^+\rangle.
\tag{UP13}
\]
Every \(|\Omega(t)\rangle\) is **maximally entangled** (one ebit); both one-qubit reduced density matrices are \(I/2\) at ALL t. The actual local quantum entanglement is never generated or borrowed; it is preserved by the local unitary. The joint Bell-bright detection probability, however, is
\[
\boxed{p_{\rm bright}(t)=
|\langle\Phi^+|\Omega(t)\rangle|^2=\sin^2(G(t)/2),}
\tag{UP14}
\]
with \(p_{\rm bright}(0)=p_{\rm bright}(1)=0\), \(p_{\rm bright}(t)>0\) for \(0<t<1\), and unique peak
\[
\boxed{p_{\rm bright}(\tau)=\sin^2((\log2)/2)\approx0.1153805493.}
\tag{UP15}
\]
The signed change \(p'_{\rm bright}(t)=\frac12\sin(G(t))\,G'(t)\) reverses orientation at \(\tau\) and integrates to zero across the endpoints. This is an explicitly defined mathematical "dark → bright → dark" loop whose observation changes while local reductions and entanglement remain constant.

It is NOT derived as a physical Hamiltonian of BBP; t is an analytic source coordinate, not BBP digit time. A chosen time-dependent local Hamiltonian could realize this phase path in an engineered quantum system, but nothing here asserts such a physical implementation. A *dephased* mixture has the same local reductions but joint Bell-bright probability 1/2, so it cannot reproduce this coherent loop.

## UP-05 — sharp normality firewall

- The pair lift and normalized Bell state are reversible representations of the original source after the reference is declared. They cannot produce extra Weyl cancellation absent a NEW inequality.
- The rational source cohomology \([r_o],[r_r]\) and the analytic Bell loop depend on forcing, NOT the selected homogeneous seed. The same-four-pole coherent wrong seed \(s_*=-\pi/16\) inherits both but has a nonnormal completed orbit. It violates \(a_0=b_0=1\) if encoded as the same pair; this is **authentication**, not a proof of distribution for the authentic pair.
- A dark Bell channel could be imposed on MANY nonnormal arithmetic sequences. Fixed entanglement or joint eraser darkness is neither a source-derived mixing theorem nor an empirical quantum property of π digits.
- The nontrivial rational-time cokernel class survives because rational-potential gauge removal fails; allowing arbitrary source-specific sequences \(U_n\) would trivialize the recurrence by construction. The domain restriction is load-bearing, not cosmetic.

**Verdict:** algebraic relational-zero construction and source cohomology are exact; a coherent entangled lift and Bell loop are mathematically valid GIVEN declared Hilbert factors; physical quantum entanglement in the actual arithmetic carrier and π normality are UNVERIFIED. Next genuinely discriminating proof must control ORIGINAL zero-seeded signed chronological Fourier characters using literal carries, not just an encoded Bell witness or period zero.

References: [SUCC #507 AD-4](https://github.com/femboy2112/SUCC/pull/507); [SUCC #509 angular return](https://github.com/femboy2112/SUCC/pull/509); IBM Quantum Learning's Bell-state introduction: https://quantum.cloud.ibm.com/learning/en/courses/use-a-qc-today/quantum-mechanics-basics ; independent university quantum information lecture notes with Schmidt-rank test: https://phsites.technion.ac.il/avron/wp-content/uploads/sites/3/2023/07/Quantum_information_116031____Lecture_Notes.pdf .
