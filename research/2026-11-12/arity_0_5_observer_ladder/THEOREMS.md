# Exact derivations, hard boundaries and hostile witnesses

**Conventions:** `ω²+ω+1=0`, `ω≠1`, `ω̄=ω²`, `e(t)=exp(2πit)`; inner products conjugate-linear in the first argument. `Γ=π₁(C₃,0)≅Z`. Exact finite computations use `Q`, `Q(i)` or `Q(ω)`, never approximate complex roots.

## A03 — minimal triangular holonomy, domain: simple undirected reversible graphs

An oriented edge `i→j` carries `u_ij`, and reversal has `u_ji=u_ij^-1`. A two-edge backtrack transports by identity. A non-backtracking simple undirected cycle has at least three vertices. On `C₃`, the based holonomy `H=u_20u_12u_01` (rightmost first) may be nontrivial. Under vertex frames `g_i` the links transform `u_ij↦g_ju_ijg_i^-1`; hence `H↦g_0Hg_0^-1`. The conjugacy class is gauge invariant. There is one independent graph cycle, giving `π₁(C₃)=Z`; a character is `χ(k)=ω^k`. **CLASSICAL/PROVED LOCAL.**

**Crucible:** a directed one-vertex loop or a multigraph with parallel edges admits shorter non-backtracking cycles. The claim “3 is the first possible dynamic object” is false, as is “3 creates linear algebra.” Here 3 is the first *reversible simple-cycle* holonomy.

### A03-T — exact three-phase triad identity

For an arbitrary sequence `z_j∈Q(ω)` define `T_j(k)=z_j+ω^kz_(j+1)+ω^(2k)z_(j+2)`, `k∈{0,1,2}`. Direct expansion proves

`T_(j+1)(k)−ω^(−k)T_j(k)=ω^(2k)(z_(j+3)−z_j).`

For `N≥1`, collecting coefficients of each `z_j` yields

~~~text
Σ_(j=0)^(N−1) T_j(k)
 = (1+ω^k+ω^(2k)) Σ_(j=0)^(N−1) z_j
   −(ω^k+ω^(2k))z_0 − ω^(2k)z_1
   +(ω^k+ω^(2k))z_N + ω^(2k)z_(N+1).
~~~

At k=1,2 the interior coefficient vanishes; only boundary terms remain. For constant `z_j=1`, every nontrivial triad vanishes identically although the orbit is maximally nonnormal. Thus exact cancellation here is **structural telescoping**, not arithmetic equidistribution. Applies to original rational BBP prefix without deriving any new Weyl cancellation. **PROVED LOCAL, exact finite checks.**

## A04-B — tetrahedral face coherence, an additional 4-point feature

Assign antisymmetric rational edge 1-cochain `a_ji=−a_ij`. Let `F_ijk=a_ij+a_jk+a_ki`. On four distinct vertices `a,b,c,d`,

`F_bcd−F_acd+F_abd−F_abc=0.`

Every edge enters twice with opposite signs: `d²=0`, the boundary of a tetrahedron. The relation is invariant under `a_ij→a_ij+g_j−g_i`. The triangle can have nonzero curvature; the tetrahedron adds a genuine **four-face coherence law**. Tested against a wrong-face-sign mutation. **CLASSICAL/PROVED LOCAL**, *abelian discrete* only; not nonabelian Bianchi without transport and not gravity.

## A04-L — exact Lorentz chart from four real coordinates

For `v=(t,x,y,z)`, identify `R⁴≅Herm₂(C)` through

~~~text
X(v)=[ t+z    x−iy ]
     [ x+iy   t−z ].
~~~

`det X(v)=t²−x²−y²−z²=:η(v,v)`. For `g∈SL₂(C)`, the real-linear action `X↦gXg†` preserves the determinant (`det g=1`) and preserves the future positive semidefinite cone `X≥0` under congruence. This is the classical spinor-to-proper-orthochronous Lorentz mechanism; no independent proof of the global double-cover statement is claimed here. **CLASSICAL/PROVED LOCAL**, with exact Gaussian-rational matrix controls.

Use **the same** `Γ=Z`: the map `B(k)=diag(2^k,2^-k)` is an exact group homomorphism `Z→SL₂(Q)`. The induced Lorentz map realizes loop number k as a boost, not as a new carrier point.

For Hermitian X,Y, `Tr(X)Tr(Y)−Tr(XY)=2η(v_X,v_Y)`. By contrast, the positive Hilbert–Schmidt square is `Tr(X†X)=2(t²+x²+y²+z²)`. Under `B(1)`, `(1,0,0,0)↦(17/8,0,0,15/8)`: Minkowski square remains 1, while Hilbert–Schmidt square changes from 2 to `257/16`. `η(0,1,0,0)=−1` forbids treating it as a Hilbert norm-square. Mutant `g=diag(2,1)` has determinant 2 and breaks determinant invariance. Four arbitrary points do not determine Lorentz geometry, nor Einstein's field equations.

## A05-G — fifth observer contract; a Hilbert realization is forced *conditionally*

Fix **the same** `Γ=Z`, a real `0<ρ<1` and `χ(k)=ω^k`. Declare **observational correlation**

`φ(k)=ρ^|k|χ(k)`, so `K(m,n)=φ(n−m)=ρ^|n−m|ω^(n−m)` for integers m,n.

**All-finite-subsets positive-definite proof (paper).** On `{0,...,N−1}` first remove unit-modulus phases to obtain `R_ij=ρ^|i−j|`. Take lower triangular `B_ij=ρ^(i−j)` if `j≤i`, else 0, and `D=diag(1,1−ρ²,...,1−ρ²)`. By finite geometric summation, `R=BDBᵀ`. Its leading determinant is `(1−ρ²)^(N−1)>0`; `D` is strictly positive, so `R` positive definite. Any finite distinct integer labels are a principal subset of a translated consecutive block and remain positive definite. Twisting by phases is unitary diagonal congruence `K=C*RC`, `C_nn=χ(n)`, preserving positivity and rank. Exact rational factorization, independent exact Gaussian elimination and cyclotomic conjugation are covered by executable tests, **but the universal quantifier follows from the paper derivation, not finite examples**.

**Canonical reconstruction (classical GNS/RKHS).** Begin with formal finite sums of `δ_n` and declare `⟨δ_m,δ_n⟩=K(m,n)`. Extend sesquilinearly; quotient null vectors; Cauchy-complete. The result `H_φ` is a Hilbert space. `K(m+1,n+1)=K(m,n)` makes `Uδ_n=δ_(n+1)` isometric; the bilateral shift and inverse extend to a unitary U. `ξ=δ_0` is cyclic and `⟨ξ,U^kξ⟩=φ(k)`. As the Gram rank is N for every N, `dim H_φ=∞`. Among minimal cyclic realizations it is unique up to unitary equivalence. Nothing changed in `Γ=Z`.

**Negative and mutation controls:**
- `ρ=1` gives a single character with rank-one Gram and one-dimensional H.
- `ρ=2` gives `[[1,2],[2,1]]` with determinant −3, so it is not positive semidefinite.
- `c₀₀` with ℓ² inner product is not complete; its Cauchy sequence of partial sums of `(2^-n)_(n≥0)` has no limit there. Completion must be **required**.
- The ℓ¹ norm square fails Jordan–von Neumann's parallelogram law: defect 4 for `(1,0)` and `(0,1)`. A norm is not necessarily Hilbertian.
- A one-dimensional complex line already is Hilbert; the 4-spinor uses the adjoint on C². Thus 5 is a *rule number*, not the first arity allowing Hilbert.
- The positive Herglotz spectral measure of `φ` is a rotated Poisson kernel with strictly positive continuous density. Multiplication by the circle coordinate on its `L²` has no nonzero eigenvectors; the stage-3 character therefore does **not automatically** embed as an eigenline in the stage-5 unitary representation. Same carrier does not mean nested representation spaces.

## A05-S — phase-Gram blindness, the decisive source firewall

For **any** real orbit x_n and integer frequency h, set `z_n=e(hx_n)`. Then `K_h(m,n)=z_n \overline{z_m}=e(h(x_n−x_m))` is a rank-one positive semidefinite Gram. Its exact phase-exponent cocycle satisfies `(x_n−x_m)+(x_m−x_l)≡x_n−x_l (mod 1)`, regardless of digit statistics. Exact tests cover authentic zero-seeded four-pole rational prefixes, the rational seed alias s=1/16, and constant zero. The completed coherent counterseed `s=−π/16` of the *same source* satisfies `U_n=−T_n→0` and is nonnormal, yet retains the Gram positivity. This is a **counterexample** to “Hilbert positivity implies normality.”

The nonmodifiable source remains

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2); U_0=0; U_n=16U_(n−1)+r(n).`

Main XXV's first missing gate is **R0**:
`∃η>0 ∃B₀ ∀B≥B₀: Re W_B(1)≤1−η`, with `W_B(1)=B^-1 Σ_(n=B)^(2B−1) e({16^nπ/16})`. **OPEN.** A genuine advance requires a **new, source-authenticated signed estimate**, not the existence of a Hilbert representation or an abstract positivity result. Goldbach and RH are separate and remain OPEN.
