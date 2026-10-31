# Pisot interactions and the Lagrangian dual — exact theorem dossier

**Declared domain:** rank-two real and integer lattices with two fixed unimodular link operators, one specified affine source, a quadratic cell energy, and (for the continuous logarithm) a two-step coarse-graining. These are **mathematical models**, not a claimed spacetime ontology. The Pisot pair has NOT been derived from original BBP forcing. Every lemma here is independent of π's unknown digit statistics.

## PIG-01. Two arithmetic-Pisot directions (PROVED PAPER; exact rational tests)

Let

$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
B=\begin{pmatrix}2&1\\3&2\end{pmatrix}.
$$

A has characteristic polynomial t²−t−1, leading eigenvalue φ=(1+√5)/2>1 and conjugate −φ^(−1), modulus <1. B has t²−4t+1, leading eigenvalue 2+√3>1 and conjugate 2−√3 in (0,1). Therefore both leading eigenvalues are Pisot units. det(A)=−1 and det(B)=1, so both maps and their inverses preserve Z². This is an integer-lattice construction rather than a nonintegral scalar drawing.

The two positive growing directions do NOT commute:

$$
C:=AB-BA=\begin{pmatrix}2&1\\-3&-2\end{pmatrix},\qquad\det C=-1.
$$

A control using B_flat=A² commutes with A exactly. Nonzero curvature is not automatic from an expansion factor or a triangular tiling.

## PIG-02. Sixth-order holonomy and exact Eisenstein lattice (PROVED PAPER; independent exact oracle)

Take the two routes from lower left to upper right, space first (AB) and time first (BA). Since all links are invertible, the closed comparison is

$$
H=(BA)^{-1}AB=\begin{pmatrix}-11&-7\\19&12\end{pmatrix}.
$$

Its characteristic polynomial is t²−t+1. Direct multiplication yields H³=−I and H⁶=I (H not identity). Choose an integral basis

$$
P=\begin{pmatrix}1&3\\-2&-5\end{pmatrix},\qquad \det P=1.
$$

Then

$$
P^{-1}HP=
R_6:=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
$$

This matrix preserves the Eisenstein/triangular lattice form x²+xy+y². In original coordinates it preserves

$$
q_H(x,y)=19x²+23xy+7y²,\qquad \operatorname{disc}(q_H)=23²-4(19)(7)=-3.
$$

Equivalently Hᵀ G H=G, G=[[19,23/2],[23/2,7]]. This is an exact arithmetic connection-holonomy example with a sixfold triangular norm. Its gauge-invariant content is the closed-loop conjugacy class/order when the link transports and comparison convention are declared. The particular P and q are coordinate-dependent representations. The constant metric q_H is flat as a Euclidean metric: **connection holonomy is NOT Gaussian/Riemannian gravitational curvature**. The chosen B is a Pell/Pisot unit, NOT shown to be a canonical BBP prime or gamma transporter. q=6 cototient, the BBP exceptional 3, and its discriminant -3 are separate arithmetic objects until a proved common-source map relates them.

## PIG-03. Two-step real differential generator and the parity obstruction (PROVED PAPER)

For any real square matrix X, det(exp X)=exp(tr X)>0. Since det A=−1, no real 2×2 matrix logarithm of the ONE-step A exists. A real autonomous linear flow cannot realize the one-step orientation reversal without changing the state/cover or allowing a discrete reset.

But Cayley–Hamilton gives A²=A+I; its eigenvalues are φ²,φ^(−2), both positive. Define

$$
\eta=2\log\varphi,\quad
K=\frac1{\sqrt5}\begin{pmatrix}1&2\\2&-1\end{pmatrix},\quad K²=I.
$$

Then cosh η=3/2, sinh η=√5/2 and

$$
A²=\exp(\eta K).
$$

Likewise put ξ=log(2+√3) and J=(1/√3)[[0,1],[3,0]], J²=I, cosh ξ=2, sinh ξ=√3. Then B=exp(ξ J). Crucially,

$$
[K,J]=\frac2{\sqrt{15}}(AB-BA).
$$

A constant continuous GL₂(R) connection with components ηK, ξJ therefore has commutator curvature ηξ[K,J], nonzero in the SAME matrix direction as the original one-step discrete defect. **The finite holonomy of A² versus B is NOT still H:** its trace is 3, not 1. Coarse-graining preserves the bracket direction here, not the entire one-step sixfold holonomy. The one-step parity/orientation mark must not be discarded. This is a dual dynamical FORMULATION for a prescribed model, not an automatic smooth limit of a variable-step SUCC theory.

## PIG-04. Exact field-energy/plaquette-disagreement duality (PROVED PAPER)

Put a vector ψ∈R² at each vertex of an oriented square, with one corner fixed at v. Give vertical edges linear transport A and affine forcing f; give horizontal edges transport B and zero forcing. Define the **positive Euclidean** discrete energy

$$
E[\psi]=\frac12\sum_{e\in\partial\square}\Vert
\psi_{\mathrm{end}(e)}-T_e\psi_{\mathrm{start}(e)}-f_e
\Vert_2².
$$

Label the lower-left anchor v, upper-left ψ₀₁, lower-right ψ₁₀, upper-right ψ₁₁, with horizontal B and vertical A (indices are merely corner labels). The four edge residuals are x=ψ₀₁−Bv, y=ψ₁₀−Av−f, z=ψ₁₁−Aψ₀₁−f, w=ψ₁₁−Bψ₁₀.

The two endpoint predictions differ by the **affine plaquette defect**

$$
\Delta=(AB-BA)v+(I-B)f.
$$

The residuals obey A x − B y + z − w = −Δ. Minimizing (||x||²+||y||²+||z||²+||w||²)/2 subject to this single vector constraint gives, by Lagrange multipliers/least-norm linear algebra,

$$
E_{\min}=\frac12\Delta^\top W^{-1}\Delta,\qquad
W=AA^\top+BB^\top+2I
=\begin{pmatrix}9&9\\9&16\end{pmatrix}.
$$

W is strictly positive definite, det W=63. There is a unique minimizing triple of unanchored corner fields because the corresponding 8×6 edge-incidence operator has full column rank with the anchor fixed. Therefore

$$
E_{\min}=(16\Delta_1²-18\Delta_1\Delta_2+9\Delta_2²)/126.
$$

The minimum is zero iff Δ=0 for the **specified** anchor/source. A nontrivial connection holonomy can be invisible to the probe v=0 with f=0; source or sufficiently rich anchor probes are needed. For v=(1,0), f=0, Δ=(2,−3), E_min=253/126. For v=(0,0), f=(47/15,0), E_min=94987/28350. A separate exact 6×6 Gaussian-elimination oracle reconstructs E_min directly without using W^(-1). This is genuine variational energy, but **elliptic/Riemannian** rather than a physical Lorentzian action. It describes incompatibility between two prescribed transport routes, not an independently derived gravitational field equation.

The general theorem remains valid for any finite-dimensional real A,B with standard Euclidean edge norms, with W=AAᵀ+BBᵀ+2I. If link endpoints have differing coordinate gauges, their metrics and affine source vectors must be transported consistently before taking sums; the displayed Euclidean norm assumes the declared common trivialization. The vanishing/holonomy tests have proper covariant meaning; the raw energy value is not invariant under an arbitrary unaccompanied GL₂ gauge transformation.

## PIG-05. Original signed four-pole BBP forcing as a declared affine curvature source

Use the ORIGINAL source, unchanged:

$$
r_n=R(8n-7),\quad
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},
\quad U_0=0,\quad U_n=16U_{n-1}+r_n.
$$

This R(a) is exactly the logarithmic derivative of

$$
V(a)=\frac{a^4}{(a+3)^2(a+4)(a+5)},\qquad R(a)=\partial_a\log V(a),
$$

as also derived independently in adjacent PR #416. Let the declared plaquette temporal affine source be f=r_n e₁, with e₁=(1,0). Then

$$
\Delta_n=Cv+r_n(I-B)e₁=Cv-r_n(1,3)^\top.
$$

For zero field anchor v=0,

$$
E_{\min}^{\rm BBP}(n)=\frac{43}{126}R(8n-7)^2.
$$

The exact rational function and its source jet are

$$
R(a)=\frac{15a²+121a+240}{a(a+3)(a+4)(a+5)}
=\frac{15}{a²}-\frac{59}{a³}+O(a^{-4}).
$$

Against the Gamma-rank-matched fake R_fake(a)=15/a²,

$$
R(a)-R_{\rm fake}(a)
=-\frac{59a²+465a+900}{a²(a+3)(a+4)(a+5)}<0
$$

for all a>0. The corresponding source-energy difference is negative and its first asymptotic term is −12685/(21a⁵). This is a **nonzero original-source fingerprint inside a declared variational model**, but the B link and the embedding e₁ are additional choices, not derived from BBP itself; the energy sees r_n, not the selected seed or signed Weyl phases. Do not rename this a proof of π normality or intrinsically realized space.

Existing PR #404 independently supplies the exact constrained first-order action

$$
\mathcal A[U,p]=\sum_{n=0}^{N-1}p_{n+1}(U_{n+1}-16U_n-r_{n+1})
$$

and the formal bulk affine-seed Noether charge 16^n p_n, with the crucial boundary qualification that U_0=0 breaks nonzero seed shifts as allowed variations. Our lattice energy is a **separate second-layer spatial/variational model**, not an invented replacement for the established original BBP action.

## PIG-06. Non-Pisot output, Pisot quotients, and honest obstructions

1. **Explicit non-Pisot effective spectrum:** the sum of Fibonacci-Pisot A and scalar integer Pisot dilation 2I is D=A+2I=[[3,1],[1,2]], with characteristic polynomial t²−5t+5. Its two roots (5±√5)/2 are BOTH >1; the dominant root is therefore NOT Pisot. Thus coupling Pisot building blocks need not yield another Pisot system. This is a simple additive superposition, not a universal reconstruction theorem.
2. **Independent prior art, much stronger for algebraic numbers:** Dubickas (2023), Theorem 3, proves EVERY positive real algebraic α of degree d is a quotient of two Pisot numbers of degree d in Q(α). Theorem 2 proves every Salem number is a difference of two Pisot numbers with an explicit exponent construction. Attribution is ESSENTIAL. These are number identities; neither preserves a given dynamical system's transition law, source, invariant measure, or finite observation fibers.
3. **Algebraic closure firewall:** finite rational/algebraic expressions in finitely many Pisot numbers remain algebraic; they do not yield transcendental π. Infinite limits or independent analytic operations (Gamma, Mellin, source-selected boundary) may produce transcendental outputs, but need separate proof. Do NOT assert irrationality or transcendence of Euler–Mascheroni γ; those statuses are unresolved.
4. **Autonomous finite-dimensional linear no-go for authentic BBP forcing:** every scalar component of a fixed finite-dimensional homogeneous constant-coefficient linear recurrence over C is a finite exponential polynomial. If it tends to zero, its nonvanishing terms must decay exponentially (modulo possible exact cancellations). But R(8n-7)~15/(64n²)>0, so it is not such a component. The original source needs an external N clock, nonconstant coefficients, nonlinear rational observation, growing state, or another declared extension. The autonomous Pisot matrices A/B by themselves cannot generate the exact four-pole time-dependent source.
5. **Distribution firewall:** 3/2 is the quotient of two integer Pisot numbers 3 and 2, while fine distribution of powers (3/2)^n mod 1 is already a hard problem; being a Pisot quotient supplies no general equidistribution estimate. Pure Pisot powers actually approach integers in the trace-conjugate sense. No 'Pisot ⇒ mixing' implication exists.

## PIG-07. Three kinds of curvature in SUCC must retain types

- The PIG holonomy is a nonflat **GL₂(Z) lattice-transport connection** on declared square plaquettes. A coordinate change conjugates holonomy. This is not automatically physical spacetime/metric curvature.
- Research PR #402 independently constructs a **Fisher-information H³** of radius √8 and sectional curvature −1/8 for independently adjustable three-channel Gamma-Poisson observation intensities; fixing total clock yields a positive-octant S² slice of curvature +1/8. This is intrinsic statistical metric curvature, not a physical spacetime claim. Pisot transports do not automatically act by isometries of THAT source-graded metric; a typed isometry/transport theorem is missing.
- Research PR #404 proves the scalar sampled BBP phase edge connection h(U_v−U_u) is **pure gauge**, zero loop holonomy, despite possible integer lift/carry marks. Noncommuting auxiliary lattice links do not refute that scalar flatness statement; they introduce NEW independent connection data. An observer-carrier realization theorem is mandatory to identify these links with genuine arithmetic dynamics.

## A direct discriminating instrument

Test all four branches on a common basis:
1. Nonflat pair (A,B) with v=e₁ and f=0: E_min=253/126; order-six H.
2. Flat control (A,A²), f=0: exact zero energy for every v.
3. Original source f=R(a)e₁ versus rank-two fake f=(15/a²)e₁ at v=0: exact energy mismatch of O(a^(-5)).
4. Same authentic forcing with changed BBP seed s*=−π/16: identical source-only energy, but a coherent NONNORMAL phase orbit. This is the fatal control for any implied signed cancellation.

**Next true proof gate:** derive A, B and their cross-connection (or a replacement) from the **same authenticated source-to-carrier map**, retaining the zero-seed, full integer carries, p-adic/real mixed observables, and an independently calibrated signed, non-scalar long-time estimate. The triangle/Fisher geometry, variational action, and Pisot decomposition by themselves do not imply that estimate.

## Source provenance and authority

- Original paper and source contracts: docs/OPERATIONAL_TRIANGLE.md, research/2026-10-27/BBP_LOG_DIRAC_SAWTOOTH_THREAD.md (LS-1/2/5), research/2026-10-30/three_channel_spatial_h3/THREE_DIMENSION_THEOREMS.md (PR #402, read-only), research/2026-10-30/noether_radix_ward/NOETHER_RADIX_WARD.md (PR #404, read-only), research/2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md (PR #416, read-only), research/2026-10-30/universal_nz_carrier/FIBONACCI_GAMMA_OBSERVER.md (PR #417, read-only).
- External mathematics: Dubickas, DOI 10.1017/S0013091523000433; Marsden & West (2001), DOI 10.1017/S096249290100006X; McMullen, The Pisot-Vijayaraghavan Numbers (1983), https://people.math.harvard.edu/~ctm/papers/home/text/papers/minor_thesis/; Baake et al. (2026), DOI 10.1107/S2053273326003918.
- Tests: finite exact standard-library probe + independent local six-variable normal-equation solver, under the stated finite model. No Lean proof, full SUCC root suite, hosted CI, physical test, or independent scholarly review is claimed.
