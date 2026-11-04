# Operation Causal Lorentz Gluing — source clock, split state/dual geometry, and a typed c / γ

**2026-11-03 · RESEARCH-ONLY · exact rational paper theorems, not physical general relativity.**

**Repository parent:** SUCC draft #481 at exact SHA `7237c2ae8b7b98557f39e47e8988b033404b587a`. The existing on-main `observational_succ/galilean_lorentz_succ.py`, `covariant_observer_frames.py`, `bbp_two_adic.py`, and the October 24 `PI_DYADIC_SOURCE_ISOMETRY.md` are prior mathematical sources; this work does NOT claim originality for the ordinary Lorentz formula, `V⊕V*` split metric, or 2-adic isometry. PR #482's parallel source-gyroscope construction is **READ-ONLY** context, NOT imported. All original signed BBP poles, literal U0=0, proof archives, formal/Lean contracts, main, workflows and production remain unchanged.

## The actual object and two incompatible clock indices

The **original** BBP source is exactly

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad n\ge1.
\]

There are two time variables that must never be identified without a proved transport:

- `n` = time index of the full nonautonomous rational BBP recurrence.
- `j` = coefficient index of the **different** four-dimensional linear realization `K(t)=Σ c_j t^j` from #481; its successor is multiplication by `u` and its **eight** coefficient steps equal `1/16`.

The shared scalar factor 16 licenses comparing *clock calibration*, but does NOT provide a bijection between these clocks, real-circle phase, p-adic time, or physical spacetime. The complete object is not a physical metric theory.

## CLG-01. Original-source sharp four-bit precision cone (DISCLOSED, elementary)

Every `r(n)` is a rational 2-adic integer. From the literal zero boundary,

\[
U_n=\sum_{j=0}^{n-1}16^j r(n-j).
\]

Fix an integer precision k≥1 and set `L(k)=ceil(k/4)`. If `j≥L(k)`, then `16^j r(n-j)≡0 mod 2^k`, so

\[
\boxed{U_n\equiv\sum_{0\le j<\min(n,L(k))}16^j r(n-j)\pmod{2^k}.}
\]

This is a sharp finite source-dependency cone. If one source injection at n−j is changed by a **2-integral unit** δ, its effect at time n is `16^j δ`, nonzero mod 2^k if and only if `4j<k`. At age L(k)−1 an integral unit pulse is detectable; at age L(k) it is not. The same budget applies to the inherited backward analytic source `F(t)=Σ_{j≥0}16^j r(t-j)` for any t∈Z2.

Define `c_precision=4` **binary valuation levels per original source step**. This is a filtration/attenuation slope, NOT a velocity of matter, an electromagnetic speed, or an independently specified spatial metric. It is a sharp **causal sensitivity budget under declared integral perturbations** of this recurrence. A matched nonintegral channel perturbation is not admissible before gluing.

## CLG-02. Zero-seeded source gluing makes the finite cone legal (DISCLOSED, on inherited #481)

The canonical spectral projectors of #481 split the authentic Mellin forcing into `r_H(n),r_G(n)` and its literal zero-seeded states. For every n≥1,

\[
\boxed{v_2(r_H(n))=v_2(r_G(n))=-5-v_2(n)<0,\quad r_H(n)+r_G(n)=r(n)\in\mathbb Z_2.}
\]

Separate mod2^k reduction of either channel is undefined. Only their GLUED sum has a legal integral residue, and the source cone in CLG-01 applies **after** that gluing. This is an exact compatibility statement of the source's two distinct quadratic channels, not a Lorentz covariance principle. The pole cancellation and source integrality are inherited from #481, while the precision-cone application is explicit here.

## CLG-03. Exact source-index versus source-state observer conjugacy (CLASSICAL, inherited DSI + new typed assembly)

Define the convergent analytic 2-adic source function

\[
F(t)=\sum_{j\ge0}16^j r(t-j),\qquad t\in\mathbb Z_2.
\]

The earlier SUCC DSI-1..4 proves `F(0)=0`, `F(n)=U_n` for every n≥0, and the isometry

\[
v_2(F(t)-F(s))=v_2(t-s)\quad(t,s\in\mathbb Z_2).
\]

The proof uses the fact that `[(r(x)-r(y))/(x-y)]` is a 2-adic unit: the numerator polynomial divided difference `120(x+y)−89` is odd, the denominator D is odd, and the divided difference of D is even. The j=0 term in F is therefore a unit multiple of t−s; every later j is divisible by 16. The finite inverse-limit construction establishes surjectivity. The source identity includes the nontrivial analytic **zero boundary** `F(0)=0`, not merely a fitted coefficient.

Let `S(t)=t+1` on Z2 and define the source-state successor by conjugation:

\[
\boxed{\Sigma=F\circ S\circ F^{-1},\qquad
\Sigma(y)=16y+r(F^{-1}(y)+1).}
\]

The diagram `F∘S=Σ∘F` is an exact **source-attested observer-frame agreement**. Since S and F are isometries, Σ is an isometry. The apparently contracting component `16y` must be combined with the state-dependent forcing, whose difference quotient is a 2-adic unit, to get the net isometry. No physical inertial frames are involved.

At every fixed precision 2^k, F induces a permutation and Σ a full single cycle of length 2^k (conjugate to addition of 1). Thus the source orbit visits all 2^k local states once per complete block, and its profinite empirical measures converge to Haar. This is **local 2-adic Haar**, not uniform real-circle digit frequencies; it inherits source isometry rather than proving a new equidistribution theorem. Finite bit-lift implementations check the exact diagram. The valuation budget CLG-01 and isometry CLG-03 are NOT contradictory: the preprogrammed source injections themselves encode the time state and restore the lost precision.

## CLG-04. Canonical split quadratic carrier from source state and dual (CLASSICAL, source-instantiated)

The already proved canonical minimal algebra is

\[
\mathcal A=\mathbb Q[u]/(u^4-u^3+u/2-1/4)
\cong\mathbb Q(\sqrt2)\times\mathbb Q(i).
\]

Put `V=A` as a four-dimensional Q-vector space and `T=M_u:V→V` as multiplication by u (invertible because the polynomial constant term is nonzero). In the **different** doubled carrier `W=V⊕V*` define

\[
B((v,f),(w,g))=f(w)+g(v),\quad Q(v,f)=f(v).
\]

B is a nondegenerate split symmetric form of signature `(4,4)` after real scalar extension; its matrix is `J=[[0,I4],[I4,0]]`. For ANY invertible T, its canonical cotangent / contragredient lift

\[
\boxed{\widehat T(v,f)=(Tv,(T^{-1})^*f)}
\]

satisfies `B(T^x,T^y)=B(x,y)` because `((T^{-1})*f)(Tw)=f(w)`. In particular `\widehat T^T J\widehat T=J`. This is the standard natural inclusion `GL(V)→O(V⊕V*)`, not a physical gravitational theorem, and does not imply source-selected mixing. The original algebra and T make the construction *source-attested*; the existence of a split form is universal.

The original four-step half-clock still distinguishes the sectors:

\[
T^4 e_H=\frac14e_H,\qquad T^4 e_G=-\frac14e_G.
\]

After EIGHT generating-function coefficient steps,

\[
\boxed{T^8=\frac1{16}I_V,\qquad
\widehat T^8=\operatorname{diag}(I_V/16,16I_{V^*}).}
\]

The covector is transported by inverse transpose; transporting the same matrix on both sides generally violates the split metric (an exact hostile mutation test). The opposite half-clock sign is invisible after the eighth return but is not retroactively erased from the original transfer.

Classical reference: MIT OCW, *Topics in Geometry: Dirac Geometry*, Lecture 4, §4.1, `https://ocw.mit.edu/courses/18-969-topics-in-geometry-dirac-geometry-fall-2006/be64b58d0e22a39cca5c715138703351_lecture4.pdf`. We use an unscaled version of its standard split pairing.

## CLG-05. Source-marked two-dimensional Lorentz boost and EXACT gamma (DISCLOSED representation identity)

The source's distinguished input is `b=1∈A` and distinguished output is the Frobenius readout `ell`, with `ell(1)=4`. Hence the normalized dual `f=ell/4` obeys `f(b)=1`. This gives a specified null two-plane inside W spanned by `(b,0)` and `(0,f)`, preserved by \hat T^8.

Write an arbitrary point there as `(a b,d f)`; its quadratic value is `ad`. After one *eight-tap return*, `(a,d)→(a/16,16d)`. Choose **dimensionless** light-cone coordinates

\[
\tau=(a+d)/2,\qquad x=(d-a)/2,\qquad ad=\tau^2-x^2.
\]

The natural eighth-return action on these coordinates becomes

\[
\boxed{\begin{pmatrix}\tau'\\x'\end{pmatrix}
=\begin{pmatrix}\gamma&\gamma\beta\\\gamma\beta&\gamma\end{pmatrix}
\begin{pmatrix}\tau\\x\end{pmatrix},\quad
\gamma=\frac{16+16^{-1}}2=\frac{257}{32},\quad
\gamma\beta=\frac{16-16^{-1}}2=\frac{255}{32},\quad
\beta=\frac{255}{257}.}
\]

Thus `gamma^2−(gamma beta)^2=1`, `gamma=(1−beta^2)^(-1/2)`, and the half-rapidity parameter is `(16−1)/(16+1)=15/17`. This matches SUCC's **pre-existing** exact 1+1 rational boost parameterization in `galilean_lorentz_succ.py`. The corresponding exact Pythagorean identity is `255²+32²=257²`.

**Interpretation boundary, load-bearing:** This `gamma` is canonically computed from the eight-tap reciprocal scalar return **once we choose the cotangent lift and the indicated null coordinates**. No physical v, c, clock synchronization, inertial equivalence, gravitational curvature, energy dynamics, or Lorentz signature of actual spacetime was derived from π. It is a valid representation-level Lorentz matrix on one marked **auxiliary plane**, not the real/imaginary Gaussian channels serving as two spacetime null rays. Source one-step n and transfer one-step j are distinct clocks.

We have TWO different c-like concepts:

1. `c_precision=4` bits per original recurrence time n (sharp arithmetic filtration slope).
2. `c_L=1` in dimensionless null coordinates τ,x; one MAY set spatial units `x_phys=c_precision*x` to obtain `c_L=4` as a **declared calibration**, with v/c=255/257. This identification is a choice of units, NOT forced by a spacetime measurement or a canonical inter-clock isomorphism. Rescaling spatial units changes numerical c while retaining every source/dual theorem. It would be incorrect to advertise v=1020/257 bits/tick as measured causal propagation.

The classical light-cone boost correspondence is documented in University of Virginia's *SR Formalism*, `https://galileoandeinstein.phys.virginia.edu/Elec_Mag/2022_Lectures/EM_62_SR_Formalism.html`. The hyperbolic formula is prior textbook mathematics; the exact 16 substitution is our stated source specialization.

## CLG-06. Frame composition, source labels and a curvature/holonomy firewall (DISCLOSED)

For integer transfer indices a,b let `L_(a→b)=\hat T^(b−a)`. All such **source-attested** frame arrows preserve B and satisfy

\[
L_{b\to c}L_{a\to b}=L_{a\to c},\quad
L_{c\to a}L_{b\to c}L_{a\to b}=I.
\]

Thus the canonical transfer-frame groupoid is FLAT (trivial loop holonomy) by construction. Multiplying one edge by central `−I` preserves the split metric but violates source-labelled loop agreement: metric invariance alone cannot certify the observer comparison. This is an exact analogue of SUCC's existing quaternion/SU2 source-marked holonomy firewall in sibling draft #482, not an import or an independent proof of GR curvature.

A full geometric GR model would need locally varying metrics, causal curve geometry, connection/curvature and a physical law matching measurements. None is claimed here. The source is a fixed rational arithmetic law.

## CLG-07. No-go: finite 2-adic causal agreement is not selected real-circle phase agreement (REFUTED naive transport)

A universal local-to-real inverse is FALSE. For any k≥1, the 2-integral rational

\[
\delta_k=\frac{2^k}{2^{k+1}+1}
\]

satisfies `v2(delta_k)=k` but `1/3 ≤ delta_k < 1/2` as an ordinary real circle displacement. Thus arbitrarily close 2-adic rationals can be far apart in the real circle. This is an explicit source-map obstruction, not a counterexample to a future theorem with additional original-source structure.

More sharply, keep **THE SAME ORIGINAL FOUR-POLE FORCING** but change initial seed from `0` to the distinct rational `1/5`. Then

\[
\Delta U_n=16^n/5\equiv0\pmod{2^k}\quad\text{when }4n\ge k,
\qquad \{\Delta U_n\}_{\mathbb R}=1/5\quad\text{for EVERY }n.
\]

So the 2-adic finite-precision frame cannot distinguish these same-forcing trajectories at sufficiently late times, even though their real-circle phase difference remains a fixed fifth-turn. **This changes the marked seed**; it is an adversarial control against seed-blind transport, NOT a counterexample to the original zero-seed normality conjecture. In particular a constant rational rotation of the real phase is NOT itself evidence of nonnormality; the example refutes preservation of the phase, not equidistribution.

Also #481's positive source-mutant polynomial retains the same minimal 8-step multiplier, and therefore the same cotangent boost γ, while changing the completed real constant. Thus the boost itself is insufficient to authenticate the original source. Local source gluing and dual covariance do not force real signed Weyl cancellation.

## CLG-08. The next theorem-producing probe (UNVERIFIED)

The signed selected original Weyl sum remains

\[
S_N(h)=\sum_{n=1}^Ne(hU_n),\qquad h\ne0.
\]

PRs #475/#476 proved the **conditional** sufficient bound on source-local dyadic collision energy: for an explicit logarithmic mesh m_A≍log A, show

\[
E_{A,m_A}=\frac{m_A}{A^2}\sum_{j<m_A}v_j(A,m_A)^2
=o(\log m_A),\quad A=2^q\to\infty.
\]

That premise is STILL OPEN. The new construction supplies exact finite precision, a source-boundary isometry, and a canonical invariant pairing; NONE of these alone is a positive all-horizon real collision count estimate. Any proposed bridge must retain BOTH channel terms, literal real integer carries, time alignment, original zero seed, real embedding and all prime cofactors. A new theorem must exclude the fake changed seed or a source-mutant at its stated scope and prove a quantitative real Fourier/carry saving, not merely identify two equal quadratic forms.

**Status ledger:**
- CLG-01: disclosed exact source-cone implication, filtration slope 4 and sharpness for integral perturbations.
- CLG-02: source-specific gluing inherited #481; no novel local-integral theorem claimed.
- CLG-03: inherited DSI source-isometry and F(0)=0; new explicit state-frame conjugacy and full finite-cycle consequences, classical conditional on inherited theorem.
- CLG-04: classical `GL(V)→O(V⊕V*)` with source-attested T, proved exact.
- CLG-05: exact derived source-return γ, β in an **auxiliary mathematical Lorentz plane**, NOT physical velocity.
- CLG-06: exact flat transport groupoid plus refuting sign-twist mutation, no spacetime curvature.
- CLG-07: refuted general local-to-selected-real phase transport via exact rational counterexamples.
- CLG-08: original source-selected real near-collision saving, signed Weyl and π base-16 normality remain **UNVERIFIED / OPEN**.

Every assertion holds within its declared type. No claim of RH, zeta-zero mechanism, physical relativity, quantum speedup, new Lean kernel compilation or independent mathematical peer review.
