# Dual E-observer boundary networks: meeting, counterexamples, and correlation

**Date:** 2026-10-12. **Parent:** [Shared-carrier boundary descent, PR #28](https://github.com/femboy2112/SUCC/pull/28), head `4733d5e5534bf64f8f41d57e9da05ecc5bc42c61`. **Status:** exact classical finite theorems, new source-relative SUCC integrations, and analytically proved continuum statements with stated domains. Academic priority unverified; no model of actual Archimedean arithmetic, physical holography, or RH.

## Faithful origin and hypotheses

The maintainer proposes two circle-indexed observational networks, each with its own deepening E tower, facing complementary boundaries of the **same** underlying fundamental carrier. Initially, one might bring the networks together at an intermediate interface and verify their agreement. Alternatively, the two E systems may refine toward their opposite boundaries indefinitely, with their infinite boundary understandings eventually becoming equal, suggesting correlation of their global points/objects.

We separate six predicates that are *not logically identical*:

1. **Same source:** both report from one declared carrier state `s` in a source space `S`.
2. **Equal marginal law:** the two boundary readouts have the same distribution.
3. **Same information:** their completed observation sigma-algebras agree (or they recover the same specified source target).
4. **Source realization:** all finite observation values jointly admit a common source state, not just matching metadata.
5. **Dynamics:** the two reconstructed sides obey a common field law and match *flux* at their interface.
6. **Statistical correlation:** nontrivial covariance or information dependence, requiring a probability law and a nonconstant observable.

Only particular implications hold. Same source alone does not give 2–6. Equal marginals do not imply a coupling. For genuine empirical systems, declared source IDs do not authenticate physical source preparations.

## DB1 — A maximal common boundary factor (classical; proved locally)

Let `S` be finite, `P(s)>0`, and let `A:S->X`, `B:S->Y` be the cumulative left and right observer reports on the same source. Build the bipartite **support graph** with vertices `('L',x)` and `('R',y)` and an edge for every source state `s` connecting `A(s)` to `B(s)`. Let `C(s)` be its connected-component label.

**Theorem DB1.** There exist functions `a` and `b` such that `C=a∘A=b∘B`. Every random variable `W` simultaneously determined by both reports, `W=f∘A=g∘B`, factors through `C`: `W=h∘C`. Thus `C` is the maximal deterministic common information, in the classical Gács–Körner sense. [Original paper: Gács and Körner (1973)](https://hdl.handle.net/11573/16907).

**Proof:** Component membership is determined by either endpoint of a support edge, proving the two decoders. If `W` is determined by both reports, the `W` labels on the endpoints of each support edge agree, and so are constant along any support-graph path. Therefore they are constant on each component and factor through `C`.

If `C` is nonconstant, take `W=1_{C=c}` for a proper component with probability `p∈(0,1)`. The observers can independently compute this SAME Boolean `W`, and its exactly correlated readouts satisfy `Cov(W_E,W_E'')=Var(W)=p(1-p)>0`. Moreover, for finite alphabets, `I(A;B)>=H(C)>0` by the data-processing inequality. **This does not prove that arbitrary raw E and E'' outputs have positive scalar covariance.**

**Negative:** Set `S={0,1}²` with independent fair bits, `A(s)=s_1`, `B(s)=s_2`. The support graph is connected, so `C` is constant and `Cov(A,B)=0`, even though the carrier is one joint source. Both readouts have identical marginal distributions. Yet their *joint* information determines parity `T=s_1 XOR s_2`; neither does separately. This is exactly the common-information-vs-information-synergy boundary.

**Positive exact control:** `S={0,1}³`, `A=(k,a)`, `B=(k,b)` with independent fair bits. The support graph has two components indexed by `k`, and `Cov(1_{k=1},1_{k=1})=1/4`, though the observers retain distinct private source dimensions.

## DB2 — The two infinite refinements and a quantitative covariance theorem

Fix one source probability space `(S,ℱ,P)`, a common real target `T∈L²(P)`, and two *increasing* filtrations `(ℱ_n)` and `(𝒢_m)`. Each E tower reports its best `L²` estimate:

`X_n=E[T|ℱ_n]`, `Y_m=E[T|𝒢_m]`.

For finite source partitions, every quantity below is rational if the target and prior are rational. Define `v=Var(T)`, `e_n²=E[(T-X_n)²]`, `f_m²=E[(T-Y_m)²]`, `d_{nm}²=E[(X_n-Y_m)²]`. Orthogonality of conditional expectation to its own error implies `Var(X_n)=v-e_n²` and `Var(Y_m)=v-f_m²`. Expansion of `d²` yields the exact identity

\[
\boxed{\operatorname{Cov}(X_n,Y_m)=v-\tfrac12(e_n^2+f_m^2+d_{nm}^2).}\tag{DB2}
\]

Since `(X_n-Y_m)=(X_n-T)+(T-Y_m)` and `(a+b)²<=2(a²+b²)`, the same-source **certified lower bound** is

\[
\boxed{\operatorname{Cov}(X_n,Y_m)\ge v-\tfrac32(e_n^2+f_m^2).}\tag{DB2b}
\]

Thus if both errors tend to zero and `v>0`, the two estimates eventually have strictly positive covariance; they converge to exactly the same nonconstant target, and their covariance converges to `Var(T)`. This is not an assumption of correlation: it follows from independent evidence that **both systems reconstruct the same T in the SAME probability space**. If the same information is a weaker shared boundary target `W`, apply DB2 to `W` rather than asserting full interior recovery.

**Limit theorem (classical):** By Lévy's upward theorem / martingale convergence in `L²` for a fixed `T∈L²`,

\[
 X_n\to E[T|ℱ_\infty],\quad Y_m\to E[T|𝒢_\infty],
\quad ℱ_\infty=σ(\cup_nℱ_n).
\]

The two limits are equal **iff** the two terminal conditional expectations of `T` are equal almost surely. A sufficient condition is that `T` is measurable in *each* terminal sigma-algebra. Increasing resolution alone is not such a condition. See the classical [Lévy upward theorem](https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/chleboun/st318.pdf).

**Crucial hostile control:** A single three-state carrier with left partition `{0,1}|{2}`, right partition `{0}|{1,2}`, uniform source prior and target `(0,1,0)` gives `Cov(E[T|left],E[T|right])=-1/36`. The finite observers can be **anticorrelated**, despite their shared source. DB2's eventual positivity requires their target reconstruction errors actually to shrink.

## DB3 — Do not confuse joining two observations with alternating projections

The correct E fusion is the **information join** `ℱ_n∨𝒢_m`, not the sequential replacement
`E[E[T|ℱ_n]|𝒢_m]` (or the reverse).

With independent fair bits `A,B` and target `T=A XOR B`, both individual conditional estimates equal `1/2` while `E[T|σ(A,B)]=T` exactly. The joint knows a fact neither sees alone. With a uniform three-state space, partitions `ℱ={0,1}|{2}`, `𝒢={0}|{1,2}`, and target `(0,1,2)`,

\[
 E[E[T|𝒢]|ℱ]=(3/4,3/4,3/2),\quad
 E[E[T|ℱ]|𝒢]=(1/2,5/4,5/4).
\]

They **do not commute**. Their pointwise joint refinement is discrete and recovers `T`. This kills a naive proposal to prove the categorical square by simply composing projection-to-E operators. The actual commuting square needs source-faithful **receipt union/restriction and re-solving against the joint source**, rather than irreversible sequential coarse-graining.

## DB4 — Meeting in the middle works IF potential and flux both match

Let finite positive-conductance carrier subgraphs `L` and `R` overlap exactly on a declared interface `M`, own disjoint edges, and have disjoint external Dirichlet boundaries `B_L` and `B_R`. Assume the union is an anchored graph (each component meets the external boundary). All vertices, conductances, source ID and source version must agree on their declared semantics.

Each half is independently eliminated to its exact Dirichlet-to-Neumann (DtN) operator
`Λ_L` on `B_L∪M` and `Λ_R` on `B_R∪M`. Given external boundary values `a,b`, the unknown interface field `z` is the unique solution of

\[
\boxed{(Λ_{L,MM}+Λ_{R,MM})z=
 -(Λ_{L,ML}a+Λ_{R,MR}b).}\tag{DB4}
\]

This is a **constructive two-sided gluing theorem**: the interface matrix is positive definite under the anchored connectedness hypothesis. It is precisely the equation `flux_L(z)+flux_R(z)=0`, with potential continuity imposed by the shared `z`. Completing each half with its own harmonic solver and identifying their common interface produces the unique global harmonic extension, and

`E_global=E_left+E_right=1/2 (a,b)^T Λ_global (a,b)`.

**Proof:** Each half Dirichlet energy is a strictly convex quadratic in its interior variables for fixed boundary data. Eliminate the separate interiors, leaving a strictly convex sum of boundary quadratic forms in `z`. Its derivative yields DB4; unique minimization over `z` equals the minimization over all interior vertices, so the glued solution equals the global harmonic extension. Equivalently this is associativity of Schur complements from SC7. This result is classical domain decomposition / Kron reduction, not a novel PDE theorem. See [Schur-complement Dirichlet-to-Neumann methods](https://doi.org/10.1016/j.wavemoti.2007.07.004).

**One-edge hostile example:** `L=0`, `M=0`, `R=1`, all conductances one. Both halves can claim the same interface **value** `0`, but fluxes sum to `-1`. Their stitched function is not globally harmonic. DB4 instead solves `z=1/2` and energy `1/4`.

**Four-edge positive:** two half-paths `(0,1,2)` and `(2,3,4)`, data `u(0)=0`, `u(4)=1`. E independently obtains interface value `1/2`, full field `(0,1/4,1/2,3/4,1)` and energy `1/8`, identical to global direct solving; all values and energies are checked with exact rational arithmetic. Multi-point interfaces are also checked, not collapsed into a single scalar assumption.

## DB5 — Two ends can decorrelate on one fundamental carrier

**Deterministic energetic statement:** A unit-conductance path with `N` edges has exact end-to-end effective conductance `g_N=1/N`. The two-port boundary Schur operator equals `[[g_N,-g_N],[-g_N,g_N]]`. This cross-boundary coupling is positive at each finite `N`, yet vanishes as `N→∞`. It is an energy/response coupling coefficient; **it is not automatically a statistical covariance**.

**Genuine probabilistic statement:** Sample `X_0∈{-1,1}` uniformly and independent flip signs `ε_i∈{-1,1}` with `P(ε_i=-1)=p`. One common Markov carrier contains `X_n=X_0∏_{i=1}^n ε_i`. Both ends have the same uniform marginal, but

\[
\boxed{\operatorname{Cov}(X_0,X_N)=(1-2p)^N.}\tag{DB5}
\]

For `p=1/4` it is exactly `2^{-N}`, tending to zero. For `p=1/2` it is already zero after one step. This refutes the unconditional inference `same carrier + two limiting ends => positively correlated global point values`. Shared reports or a shared target can still be positively correlated by DB1/DB2; it is not enforced by mere topological identity.

**Continuum circle adversary:** For the harmonic cylinder `[-L,L]×S¹`, fix Fourier mode `n>0` with boundary values `a_n,b_n`. The unique harmonic solution has

\[
 u_n(t)=a_n\frac{\sinh(n(L-t))}{\sinh(2nL)}+
 b_n\frac{\sinh(n(L+t))}{\sinh(2nL)}.
\]

At the middle `u_n(0)=(a_n+b_n)/(2\cosh(nL))→0`; the two boundary DtN cross coupling is `-n csch(2nL)→0` exponentially. The zero angular mode has linear interpolation and cross coupling `-1/(2L)→0`. **Even if the two boundary traces are identical nonconstant functions**, their nonconstant harmonic influence disappears at the central meeting point as separation grows.

Stronger no-go: every **bounded** harmonic function on the entire infinite cylinder `ℝ×S¹` is constant. Its Fourier coefficients solve `c_n''-n² c_n=0`; boundedness at both ends forces `c_n=0` for `n≠0`, and `c_0(t)=at+b` bounded implies `a=0`. Thus a model where the two infinite boundary values *must agree* may do so because every interesting angular mode has been eliminated, not because it achieved full global reconstruction.

## DB6 — Two infinite limits: what must commute?

There are three different operations: advancing left observations `n→∞`, advancing right observations `m→∞`, and **joining**/checking evidence. On a fixed probability space with nested filtrations, the two-source information join is `σ(ℱ_∞∪𝒢_∞)` and directed finite joins converge to it. This is a compatible net. It does not mean the operations of sequential *conditional expectation* commute (DB3).

Without the common-source and uniform-completion hypotheses, iterated limits need not agree: `a_{n,m}=1_{m≥n}` satisfies `lim_n lim_m a_{n,m}=1` and `lim_m lim_n a_{n,m}=0`. Simply drawing two towers approaching infinity does not justify interchanging their limits or identifying their end objects.

For a rigorously nontrivial **Archimedean** version of this program one must construct, rather than stipulate, the arithmetic source-functor mapping genuine finite prime-power/Euler data and the real place to the SAME completed analytic/test-function carrier. The familiar product formula identifies the magnitude of nonzero rational numbers, not the completed Gamma factors or the Weil form. A geometric disk/cylinder illustration is not that source-functor.

## Exact implementation, adversarial controls, and research boundary

`observational_succ/dual_boundary_observers.py` adds:
- strictly positive rational finite source prior and two source-consistent refining observer report partitions;
- exact Gács–Körner support-component common knowledge and covariance witness;
- exact original-source target factorization, separate versus joint projection, and DB2 covariance/error certificates;
- two-sided DtN interface gluing from independently specified half-graphs, flux/energy replay against direct global reconstruction;
- exact two-port conductance and Markov endpoint correlation/decay.

`tests/test_dual_boundary_observers.py` includes 26 named exact controls, including 144 varied half-carrier boundary/conductance combinations. `scripts/dual_boundary_observers_probe.py` emits machine-readable rational receipts, labels that the model does not authenticate a physical source, and makes no RH or Archimedean identification.

**What it really gains:** a precise conditional route from two E-tower reconstructions of a common *nonconstant target* to objectively positive correlation of their resulting estimates, and a separate meeting-in-the-middle theorem with flux-matched gluing. **What fails:** same carrier, equal marginal distributions, matching interface values, successive projections, or existence of two infinite ends do not, separately, imply global identity or correlation.

**Next frontier:** A source-derived *joint instrument/coupling* for dynamically updated dual carrier boundaries; a proof of uniform observability/mixing along dual E refinements; quantitative spectral lower bounds preventing transmission from collapsing at infinity; cyclic/Čech boundary monodromy for nontrivial circle bundles; and only then an honest attempt to identify anything with the arithmetic Archimedean factor or completed Weil distribution. No finite tests are a proof of these global bridges.

## DB7 — The dual-circle experiment is exactly genus-zero Riemann–Roch

This is the mathematically closest *nontrivial* match to the maintainer's two opposed circles, one aimed at the origin and one at infinity. It also isolates a failure of the demand for raw equality at both boundaries: a nontrivial global field may need **a nontrivial transition law**, not identical local expressions.

Work algebraically over `Q` (or any field `K`), with the standard two affine charts of the projective line `P¹_K`:

- `U_0=Spec K[z]`, the neighborhood of finite points;
- `U_∞=Spec K[w]`, where `w=z^{-1}`;
- `U_0 ∩ U_∞=Spec K[z,z^{-1}]`, the multiplicative group (`C× ≅ R×S¹` after base-changing to `C` and taking `z=e^{t+iθ}`).

Fix integer twist `k`. Define the line bundle `O(k)` by transition

\[
\boxed{f_0(z)=z^k f_\infty(z^{-1})}\qquad(z\neq0).\tag{DB7a}
\]

The two E observer nets locally know `f_0∈K[z]` and `f_∞∈K[w]`; compatible reports must commute with this exact transition, not with the identity. Global sections form

\[
H^0(P^1,O(k))=K[z]\cap z^k K[z^{-1}]
=\operatorname{span}_K\{z^j:0\le j\le k\},
\]

with empty span for `k<0`. Thus

\[
\boxed{h^0(P^1,O(k))=\max(k+1,0).}\tag{DB7b}
\]

For sheaf cohomology, the two chart opens and overlap are **affine** and the line bundle is quasi-coherent, so this affine two-chart Čech complex computes its cohomology. A general overlap cocycle is a Laurent polynomial in `K[z,z^{-1}]`. Two local cochains may change it by `f_0-z^k f_∞`, spanning exactly all Laurent powers `j≥0` and `j≤k` respectively. The only unremovable modes are those with `k<j<0`. Therefore

\[
H^1(P^1,O(k))\cong
K[z,z^{-1}]/(K[z]+z^kK[z^{-1}]),
\]

with basis `{z^(k+1),...,z^(-1)}` if `k≤-2` and empty otherwise, so

\[
\boxed{h^1(P^1,O(k))=\max(-k-1,0).}\tag{DB7c}
\]

Subtract the two exact counts:

\[
\boxed{\chi(P^1,O(k))=h^0-h^1=k+1.}\tag{DB7d}
\]

This recovers **Riemann–Roch in genus zero** using nothing but two opposed chart observers, exact transition-arrow compatibility, and a count of obstruction modes. It is a classical algebraic argument and is NOT a scholarly-priority claim. Nevertheless it is *load-bearing* rather than an analogy: every arrow, overlap, global section and unremovable obstruction is an actual algebraic object.

**Constructive examples:** for `k=2`, `f_0(z)=1+2z+3z²` matches `f_∞(w)=3+2w+w²`. For `k=0`, only constants are globally regular in both charts, despite each separately admitting arbitrary polynomials. For `k=-2`, there are zero nonzero global sections, but an overlap cocycle `z^{-1}` is not a coboundary and represents one genuine obstruction. For `k=-3` there are two independent such obstructions, `z^{-2}` and `z^{-1}`. These are checked exactly by the new `dual_chart_riemann_roch.py` Laurent-coefficient interface with 9 additional adversarial tests.

**Physical and arithmetic firewall:** the analytic complex place `C` and its multiplicative cylinder are legitimate geometric interpretations. However the projective line, its degree `k`, and its line-bundle transition are DECLARED geometry. Nothing constructs them from actual Euler prime jets, Archimedean Gamma factors, conductor/half-density, or a source-derived completed Weil form. A fully arithmetic transfer would need a independently defined source correspondence preserving local sections, transition factors, and the global positivity/duality law on the correct completed test-function domain; one cannot replace this missing functor by the word holography.

**Immediate next research target:** Make the E-tower *generate* transition `z^k` from independently certified source geometry, then gluing gives global sections/obstructions. The next nontrivial arithmetic analogue should identify a genuine line bundle or sheaf on the relevant arithmetic space, with correct finite/Archimedean gluing—not simply a Gaussian-prime loop or a harmonic resistor analogy.
