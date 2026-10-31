# Operation SUMMATION SNAPSHOT ARROWS — admissible quotients, finite triangles, heat-kernel observers and exact noncommutation

**Research-only stacked continuation, 2026-10-30.** Parent: SUCC dyadic-zeta prime-exposure draft PR #422, exact head e8a4978207871a47466cdbb6f15cc86fae784164; ultimate merged Main XVI parent e18ba565ca540adb7edf3292f5593929e76d91c5. Related read-only drafts: #417 universal N/Z carrier; #420 finite Basel cycle; #421 source-shadow obstruction. This is a **new-to-SUCC synthesis of predominantly classical mathematics**, not scholarly priority, RH, or proof of π-normality. Original signed four-pole BBP forcing and U0=0 are unchanged.

## 0. Object, question and discipline

The intuition is that an infinite sum retains a supported set of factorable algebraic forms, so formal linear combinations and quotients can be used to deduce categorical arrows connecting different observational snapshots. Make that precise without equating different summation methods, reordering divergent series illegally, or inferring a later snapshot from insufficient earlier data.

**Typed presentation.** A generator is a quadruple (formula, index/parameter domain, summation/continuation protocol, source/seed label). Build a Q-vector space on these symbols and quotient ONLY by certified, protocol-compatible identities. Examples of authorized relations: finite distributivity, finite reindexing, Fubini/Tonelli for absolutely convergent sums, identity-theorem transport of a meromorphic family agreeing on a nonempty open set, and an explicitly declared finite-part subtraction on its domain. A scalar may be pulled through a linear sum only where the scalar is independent of the summation index and the operation is defined; arbitrary multiplication needs a separately defined product and a check of its compatibility.

This is a **presented module** (or a presented algebra if products are proven), not the whole quotient of real constants modulo unknown relations. It is not known, for example, that e, gamma and pi are Q-linearly independent, so do not silently add independence as an axiom or equate arbitrary regularized representatives.

## 1. SA-01 — exact categorical arrow / quotient criterion (PROVED, classical)

Let P be a vector space of admissible presentations, and q_A:P->V_A, q_B:P->V_B be linear observational maps. There is a unique linear arrow F:im(q_A)->im(q_B) with q_B=F o q_A **if and only if** ker(q_A) is a subset of ker(q_B).

Proof: if F exists, q_A(x)=0 entails q_B(x)=F(0)=0. Conversely define F(q_A(x))=q_B(x). If q_A(x)=q_A(y), x-y belongs to ker(q_A), hence q_B(x-y)=0 and F is well-defined; the unique map is linear and surjective onto im(q_B).

For **nonlinear** q_A,q_B the corresponding condition is fiber constancy: q_A(x)=q_A(y) implies q_B(x)=q_B(y), where F is a set map and need not be linear.

Exact finite countercontrol: for x=(1,0), y=(0,1) in Q², q_A(a,b)=a+b has q_A(x)=q_A(y)=1, whereas q_B(a,b)=a+b/4 gives 1 versus 1/4. Thus q_B does **not** factor through q_A. This is the same mathematical requirement as the q o F = Fhat o q fiber-adequacy contract already documented in SUCC #417, applied to **two different observers**.

## 2. SA-02 — a universal positive heat-kernel carrier realizing e, gamma, zeta and Basel

For every real t>0, set

\[
K(t)=\sum_{n\ge1}e^{-nt}=\frac{e^{-t}}{1-e^{-t}}=\frac1{e^t-1}.
\]

This sum is absolutely convergent at each t>0, with positive terms. Different *typed* observers of this one complete kernel give:

**Finite evaluation, a nonlinear map:**
\[
\boxed{e=1+K(1)^{-1}.}
\]

**Convergent Mellin transform:** for Re(s)>1, Fubini/Tonelli and the gamma integral yield
\[
\boxed{\mathcal M K(s)=\int_0^\infty t^{s-1}K(t)dt
=\Gamma(s)\sum_{n\ge1}n^{-s}=\Gamma(s)\zeta(s).}
\]
In particular
\[
\boxed{\int_0^\infty tK(t)dt=\zeta(2)=\pi^2/6.}
\]

**Renormalized gamma observation with its subtraction explicitly declared:**
\[
\boxed{\mathcal R(K)=
\int_0^\infty \left(K(t)-\frac{e^{-t}}{t}\right)dt=\gamma.}
\]
At t=0 the integrand has finite limit 1/2; at infinity it decays. For epsilon>0,
\[
\int_\epsilon^\infty K(t)dt=-\log(1-e^{-\epsilon}),\quad
\int_\epsilon^\infty\frac{e^{-t}}{t}dt=E_1(\epsilon)
=-\gamma-\log\epsilon+o(1).
\]
The difference tends to gamma. The subtraction is part of the observation, and an arbitrary change in subtraction changes the assigned finite part.

**Negative zeta by a *completed* Laurent germ:** for 0<|t|<2pi (and no other singularities in that disk),
\[
K(t)=t^{-1}-\frac12+\frac{t}{12}
-\frac{t^3}{720}+\frac{t^5}{30240}-\cdots.
\]
For every nonnegative integer m,
\[
\boxed{\zeta(-m)=(-1)^m m!\,[t^m]K(t).}
\]
For m>=1 this follows from K(t)=t^{-1}\sum_{j>=0}B_j t^j/j!, ζ(-m)=-B_(m+1)/(m+1), vanishing B_(odd>=3), and the parity of m; for m=0 use the separate identity ζ(0)=-1/2=B1. The convention B1=-1/2 is essential. At m=1 the coefficient is +1/12 and ζ(-1)=-1/12; at m=3 the coefficient is -1/720 and ζ(-3)=1/120.

**No unearned arrows:** e is a rational function of the specific point evaluation K(1); gamma and Basel require the entire kernel and different integrals. On a general family of positive kernels, a single point value cannot recover these integrals.

Primary-source exact identities: DLMF 25.5.1, 24.2.1, 25.6.3, 5.9.18; see links at end.

## 3. SA-03 — an exact noncommuting finite-to-complete diagram

Define the literal positive finite snapshots \(K_N(t)=\sum_{n=1}^N e^{-nt}\). For every t>0, K_N(t) increases to K(t). Yet the finite Taylor coefficient at t=0 is
\[
[t]K_N(t)=-\sum_{n=1}^N n=-\frac{N(N+1)}2 \longrightarrow-\infty.
\]
The **complete** Laurent coefficient is instead
\[
[t]K(t)=+\frac1{12}.
\]
The two operations "first extract t coefficient at the finite stage, then send N to infinity" and "first complete K_N for t>0, then take its analytic Laurent germ" DO NOT COMMUTE. The reason is failure of uniform convergence near t=0, not a contradiction or equality of divergent ordinary sums.

This is a rigorous finite-to-analytic boundary discontinuity in exactly the sense SUCC wants to track. A commuting diagram must explicitly include a lawful renormalization/continuation arrow; the untreated finite cutoff does not supply one.

## 4. SA-04 — the actual finite square decomposes into two triangles and a diagonal

For any N and any sequences a_n,b_n in a commutative ring:
\[
\boxed{\left(\sum_{n=1}^N a_n\right)
\left(\sum_{m=1}^N b_m\right)
=\sum_{n>m}^{N} a_n b_m
+\sum_{m>n}^{N} a_n b_m+\sum_{n=1}^N a_nb_n.}
\]
The index square {1,..,N}² is partitioned into **upper triangle, lower triangle, and diagonal**. This is finite combinatorics, requiring no infinite sum or regularization. In a domain of absolute convergence it passes to N=infinity. Consequently,
\[
\boxed{\zeta(2)^2=2\zeta(2,2)+\zeta(4)}
\]
where ζ(2,2)=sum_(n>m>=1) n^-2 m^-2. This is the convergent multiple-zeta **stuffle** product, not an allowed naive identity for zeta(-1)² by separately assigning values to divergent sums.

For the inclusive partial-sum operator P(a)_N=sum_(n=0)^N a_n, the exact pointwise identity is
\[
\boxed{P(a)P(b)=P(aP(b))+P(P(a)b)-P(ab),}
\]
a weight -1 **Rota–Baxter identity**. Different strict/inclusive conventions have different signs/weights. This is a concrete algebraic categorical arrow from finite products to finite triangles, and a natural interface to SUCC's finite Pascal/extruded triangle carrier. It does **not** uniquely produce the BBP orbit.

## 5. SA-05 — additive vs multiplicative convolution: same symbols, different carriers

For ordinary generating functions A(x)=sum_(n>=0)a_n x^n and B(x), multiplication means **additive** convolution:
\[
A(x)B(x)=\sum_{k>=0}\left(\sum_{i+j=k}a_i b_j\right)x^k.
\]
For Dirichlet functions D_a(s)=sum_(n>=1)a_n n^-s, multiplication on their common absolute-convergence domain means **multiplicative** convolution:
\[
\boxed{D_a(s)D_b(s)=\sum_{k>=1}
\left(\sum_{d\mid k}a_d b_{k/d}\right)k^{-s}.}
\]
Thus ζ(s)^2=sum_(k>=1)d(k)k^-s, whereas ζ(2s)=sum n^-2s is a different operation (exponent dilation, not product). Two factorization schemes are separately typed by the underlying monoid (N,+) versus (N_positive,×); a symbol "square" alone is insufficient to determine the arrow.

The coefficient Borel transform \(\mathcal B(\sum a_n x^n)=\sum a_n x^n/n!\) is a linear map that takes the geometric formal series 1/(1-x) to e^x. But it **does not preserve ordinary products**:
\[
\boxed{\mathcal B((1-x)^{-2})=(1+x)e^x
\ne e^{2x}=(\mathcal B(1/(1-x)))^2.}
\]
So e genuinely has a transform arrow from the geometric presentation, but it does not follow from the isolated regularized numeric value -1 of (1-x)^-1 at x=2. A multiplication-preserving map requires a **transported** target product.

## 6. SA-06 — gamma and Oily–Macaroni are typed second observations

For |z|<1 the complete analytic Gamma germ has
\[
\boxed{\log\Gamma(1+z)=-\gamma z+
\sum_{n=2}^\infty(-1)^n\frac{\zeta(n)}n z^n.}
\]
Its linear and higher Taylor coefficients recover gamma and the positive integer zeta values, respectively. This overlaps with the K-based gamma and Mellin observers, providing exact coherence checks rather than numerical coincidences. DLMF 5.7 supports the Gamma expansion.

For \(\lambda=\varphi^{-1}=(\sqrt5-1)/2\), the independent algebraic relation \(\lambda^2+\lambda-1=0\) gives the SUCC Oily–Macaroni mark
\[
\boxed{\Omega_{\rm OM}=\lambda-\gamma
=(1-\gamma)-\lambda^2.}
\]
With the explicitly declared Y~Gamma(shape=2,rate=1) observer:
\[
\mathbb E\log Y=\psi(2)=1-\gamma,\qquad
\mathbb E e^{-\lambda Y}=(1+\lambda)^{-2}=\lambda^2,
\]
hence
\[
\boxed{\Omega_{\rm OM}=
\mathbb E\log Y-\mathbb E e^{-\lambda Y}.}
\]
This is inherited in substance from SUCC #420. The golden parameter is an *independent algebraic mark*: no theorem here says universal K determines phi uniquely or that Ω proves BBP cancellation.

## 7. SA-07 — all-asymptotic-data positive shadow (PROVED, hostile control)

Work in the class of smooth positive functions on (0,infinity), admitting a full small-t algebraic asymptotic expansion with a t^-1 pole, exponential decay at infinity, and finite Basel and renormalized-gamma observations. Let
\[
\boxed{h(t)=(t-1)^2e^{-t-1/t},\quad
\widetilde K(t)=K(t)+h(t).}
\]

Then h(t)>=0, h(1)=0, and h is nonzero except at t=1. For every real M and every nonnegative derivative order j,
\[
h^{(j)}(t)=O_M(t^M)\qquad(t\to0^+).
\]
Indeed differentiating introduces only polynomial powers of 1/t, which are dominated by e^-1/t. Thus **K and Ktilde have the identical all-order formal asymptotic Laurent series** and K(1)=Ktilde(1). Nevertheless,
\[
\boxed{\int_0^\infty t\widetilde K(t)dt
=\zeta(2)+\int_0^\infty t h(t)dt>\zeta(2),}
\]
and
\[
\boxed{\mathcal R(\widetilde K)=\gamma+
\int_0^\infty h(t)dt>\gamma.}
\]

This proves that neither the full *formal asymptotic* snapshot nor its augmentation by a fixed rational-point observation reconstructs global integrals on that broad smooth class. The changed K is **not** the original counting spectrum \(\sum_{n>=1}e^{-nt}\); this is explicitly a changed-source hostile control, not an alternative value of ζ(2).

**Analytic restoration criterion.** In contrast, if both functions are meromorphic on one connected domain reaching the evaluation path, and the complete **convergent Laurent germs** agree on a punctured neighborhood of zero, the identity theorem forces them to coincide throughout the domain; the evaluations and convergent Mellin observations agree. The flat h has an essential singularity at t=0, so it is outside this meromorphic-at-zero class. A full convergent germ is stronger data than a merely asymptotic jet.

This exactly mirrors #421's warning that all polar/asymptotic data can miss an entire remainder in a broader source class.

## 8. Source/seed firewall, status and next discriminating probe

**DISCLOSED (classical proofs adapted to this declared category):** the arrow iff fiber theorem, common-kernel observer formulas with stated domains, finite coefficient/completion noncommutation, exact triangle/stuffle/Rota–Baxter identities, separate additive/multiplicative convolution, Borel nonmultiplicativity, and flat positive observer shadow.

**OBSERVED finite calibrations:** 10/10 exact stdlib-only unittest methods and independent mpmath quadrature with 50 digits. See VALIDATION.md. No publication priority is asserted, no full native SUCC suite/CI/Lean/blind external review is claimed.

**Open source-sensitive question:** Does there exist a faithful typed map from SUCC's actual four-pole \(R(8n-7)\), literal \(U_0=0\) update and source-selected phase \(e^{2\pi ihU_n}\), through these summation presentations, to a new discriminating bound? It must distinguish the same-forcing coherent counterseed and the #421 all-order changed-source shadow. An identity of generic Gamma/zeta objects is not enough. A meaningful next proof must create and bound a new **source-sensitive** finite triangular correlation, not just rewrite the Weyl criterion.

### Primary/classical provenance
- NIST DLMF 25.5.1: https://dlmf.nist.gov/25.5.E1
- NIST DLMF 24.2.1: https://dlmf.nist.gov/24.2.E1
- NIST DLMF 25.6.3: https://dlmf.nist.gov/25.6.E3
- NIST DLMF 5.9.18: https://dlmf.nist.gov/5.9.E18
- NIST DLMF 5.7: https://dlmf.nist.gov/5.7
- Guo and Keigher, *On differential Rota–Baxter algebras*, J. Pure Appl. Algebra 212 (2008), 522–540: https://doi.org/10.1016/j.jpaa.2007.06.008
- Relevant SUCC drafts: #417, #420, #421, and parent #422.
