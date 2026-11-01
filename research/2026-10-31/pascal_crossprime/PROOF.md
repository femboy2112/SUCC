# Pascal transport, explicit 2-adic↔3-adic dynamical conjugacy, and Pisot field boundaries

**2026-10-31. Research only.** Stacked child of SUCC draft PR #427 at exact parent 8558a95b2a28a20c63e5df7f2995755e84c4e642; Main XVII base e8598cfa. Historical sources and original zero-seeded signed four-pole BBP untouched. **RH, π base-16 normality, selected ×3 invariance, unrestricted Furstenberg measure rigidity remain OPEN.** This package explicitly distinguishes exact finite algebra, topological conjugacy, measure transport, field representation, and the selected real phase.

## 1. CP-01: the Pascal operator is an EXACT 2→3 scale translation (CLASSICAL / PROVED LOCAL)

For any commutative ring and any sequence a=(a_n), define
\[
(Ba)_n=\sum_{k=0}^n{n\choose k}a_k,\qquad
(B^{-1}b)_n=\sum_{k=0}^n(-1)^{n-k}{n\choose k}b_k.
\]
Binomial inversion proves B^{-1}B=BB^{-1}=I at every finite n. For the exponential eigen-sequence a_n=λ^n,
\[
\boxed{B(\lambda^\bullet)_n=(\lambda+1)^n}.
\]
In particular \(3^n=\sum_k {n\choose k}2^k\), while \(2^n=\sum_k(-1)^{n-k}{n\choose k}3^k\). The same formula acts on algebraic linear-recursion traces: \(B(\operatorname{Tr}\beta^n)=\operatorname{Tr}(\beta+1)^n\).

**Boundary:** B is an invertible triangular change of SEQUENCE coordinates, not an isomorphism of Z₂ and Z₃ as topological rings, not a Haar-preserving orbit conjugacy, and not an arithmetic source-selected estimate for π. This generalizes the already integrated PIS-01 matrix-shift construction, which is credited rather than claimed new.

## 2. CP-02: the Pascal translation has DIFFERENT local convergence domains (PROVED LOCAL)

The infinite binomial series \((1+2)^x=\sum_{k\ge0}{x\choose k}2^k\) converges for every \(x\in Z₂\), since \({x\choose k}\in Z₂\). It is a continuous interpolation of n↦3^n. For signed integer n, modulo 2^a terms k≥a vanish. The exact finite evaluator uses only k<a. LTE gives for j≥1
\[
v_2(3^{2^j}-1)=j+2.
\]
Similarly \((1+15)^x=\sum_{k\ge0}{x\choose k}15^k\) defines a continuous interpolation n↦16^n on Z₃, since \(v_3(15)=1\), with
\[
v_3(16^{3^j}-1)=j+1.
\]
**Critical asymmetry:** n↦2^n has NO continuous extension from the ordinary nonnegative integers (densely embedded) to Z₃. The integers 3^j→0 in Z₃, but \(2^{3^j}\equiv2\bmod3\) for every j, whereas \(2^0\equiv1\bmod3\). Thus the coordinate change is not analytically symmetric across the two primes. The input base and output metric cannot be silently exchanged.

## 3. CP-03: a CONSTRUCTIVE homeomorphic conjugacy of ×2+1 with ×3 (PROVED LOCAL)

Put \(F(x)=2x+1\) on \(Z₂\), \(G(y)=3y\) on \(Z₃\). Write \(u=x+1\), so \(u(F(x))=2u(x)\). We explicitly construct a homeomorphism \(g:Z₂^\times\to Z₃^\times\) of unit Cantor spaces.

A 2-adic unit has binary digits \((1,b_1,b_2,\dots)\). Map \(b_1\) to the first ternary digit \(y_0=1+b_1\in\{1,2\}\). Parse the remaining infinite binary digits using the complete prefix code
\[
00\mapsto0,\quad 01\mapsto1,\quad1\mapsto2.
\]
Every infinite bit stream has a unique concatenation of these codewords (maximum length 2), and every ternary digit stream has a unique inverse concatenation. The coding and its inverse are continuous in the product topologies, hence g is a homeomorphism.

Every nonzero \(u\in Z₂\) has a unique representation \(u=2^n v\), \(n=v_2(u)\ge0,v\in Z₂^\times\). Define
\[
h(0)=0,\quad h(2^nv)=3^n g(v),\qquad H(x)=h(x+1).
\]
This is a bijection of the full compact adic spaces. Continuity on each clopen valuation shell follows from g. Continuity at the unique accumulation point 0 follows since n→∞ gives 3^n g(v)→0 uniformly. The inverse is analogous. Finally
\[
\boxed{H(2x+1)=h(2(x+1))=3h(x+1)=3H(x).}
\]
This is an exact topological dynamical conjugacy, **not** a claim the ring fields are isomorphic. The source affine map F is not the BBP map \(U_{n+1}=16U_n+r(n+1)\). Applying H to the authentic BBP trajectory would require a separately derived source morphism; no such identification is asserted.

Finite restriction: g sends positive odd integers to positive nonmultiples of 3 (the tails are eventually zero). Thus H restricts to a bijection \(N_0\to N_{>0}\), with H(-1)=0, obeying H(2n+1)=3H(n). The exact implementation has both directions.

## 4. CP-04: finite-to-global modulus / no GROUP conjugacy (PROVED LOCAL)

Let \(H\) be the explicit code of §3. From \(x\equiv y\bmod2^{2b}\), the common valuation shells and at most two input bits per output ternary digit imply
\[
\boxed{H(x)\equiv H(y)\pmod{3^b}.}
\]
Conversely if \(H(x)\equiv H(y)\bmod3^b\), the inverse code outputs at least one binary bit per ternary digit, giving \(x\equiv y\bmod2^b\). These uniform moduli certify continuity without a fictitious finite-level bijection \(Z/2^a=Z/3^b\).

**Group-theoretic no-go:** every continuous additive group homomorphism \(Z₂\to Z₃\) is zero. Its composition with each finite quotient \(Z₃\to Z/3^b\) is a finite image of a pro-2 group inside a 3-group, hence trivial. All levels vanish. Likewise in the reverse direction. Therefore H cannot be an additive/ring isomorphism, and no nontrivial native ring/group quotient from one p-adic integer carrier to the other exists. Both are nevertheless homeomorphic Cantor spaces.

## 5. CP-05/06: the reparameterization has a compulsory HAAR defect (PROVED LOCAL)

Let m₂,m₃ be normalized additive Haar probabilities. Under x∼m₂, x+1 is Haar and
\(m₂(v₂(x+1)\ge n)=2^{-n}\). Because H maps the n-th F-image \(F^n(Z₂)\) bijectively to \(G^n(Z₃)=3^nZ₃\),
\[
\boxed{(H_*m₂)(3^nZ₃)=2^{-n}\ne3^{-n}=m₃(3^nZ₃),\qquad n\ge1.}
\]
This rules out **every Haar-preserving topological conjugacy** between these two contraction systems, regardless of how its unit shells are parameterized.

The explicit variable-length code is more informative. Conditional on the 2-adic unit shell, the input tail bits are fair independent bits. The first ternary output digit is uniformly 1 or 2, but **each subsequent output ternary digit is independent with distribution**
\[
q=(q_0,q_1,q_2)=(1/4,1/4,1/2).
\]
Indeed input codewords 00,01,1 have probabilities 1/4,1/4,1/2, and fair bits regenerate after each bounded stopping time. At depth k the output unit law has exact cylinder weights
\[
\Pr(y_0=j,y_1=d_1,\dots,y_{k-1}=d_{k-1})=
\tfrac12\prod_{i=1}^{k-1}q_{d_i},\quad j=1,2.
\]
Exhaustive exact rational finite-prefix checks confirm the formula at k≤6.

The per-tail-symbol Shannon entropy and divergence relative to native ternary Haar are
\[
\boxed{H(q)=\tfrac32\log2,\qquad
D_{\mathrm{KL}}(q\,\|\,u_3)=\log3-\tfrac32\log2>0}
\]
(the strict sign follows from \(3^2>2^3\)). A ternary output symbol consumes a mean of \(1/2\cdot1+1/4\cdot2+1/4\cdot2=3/2\) input bits, so **entropy per consumed input bit remains \(\log2\)**. This is a change of clock/units rather than destruction of source information.

By the strong law for i.i.d. ternary digits, q-almost every output has asymptotic digit-2 frequency 1/2; Haar₃-almost every output has frequency 1/3. The explicit transported measure is therefore singular to Haar₃ on unit shells. This is a quantifiable example of a faithful *topological* source map with a NON-HAAR image law. It is not a physical black-hole result, a quantum measurement, or a model of actual π digits.

## 5b. CP-06B: Pascal occupancy is a SUFFICIENT statistic for the induced Haar defect

For the explicit prefix code, among the next m ternary output symbols let A be the number of occurrences of symbol 2, which is encoded by a **single** binary bit; the others (0 or 1) each consume **two** bits. The induced q law gives each ternary word w with A(w)=a probability \(2^{-(2m-a)}\); native Haar₃ gives \(3^{-m}\).

There are exactly \({m\choose a}2^{m-a}\) such words. Therefore
\[
\boxed{\Pr_{\mathrm{transport}}(A=a)={m\choose a}2^{-m},\qquad
\Pr_{\mathrm{Haar}_3}(A=a)={m\choose a}
(1/3)^a(2/3)^{m-a}.}\tag{CP-06B}
\]
These are **two different binomial/Pascal rows**: probability parameter 1/2 versus 1/3. Conditional on A=a, both measures are UNIFORM among precisely those \({m\choose a}2^{m-a}\) words. Hence A is a sufficient statistic for discriminating the two finite-prefix probability laws. The data-processing inequality becomes an exact equality:
\[
D_{\mathrm{KL}}(q^{\otimes m}\Vert u_3^{\otimes m})
=D_{\mathrm{KL}}(\operatorname{Bin}(m,1/2)\Vert
\operatorname{Bin}(m,1/3))
=m\big(\log3-\tfrac32\log2\big).
\]
The right-hand KL is between the *distributions of the count A*, not between the two Bernoulli symbols at a fixed position. The common per-word likelihood ratio depends only on A, so the equality follows directly. Also the average source bits consumed are \(\mathbb E(2m-A)=3m/2\).

**Significance:** the Pascal triangle is an **operational and complete information discriminator** for this particular cross-adic code, not merely a visual analogy or arbitrary connection of numbers. But g is still a *chosen* homeomorphism, not a BBP-source-derived function. Nothing licenses applying CP-06B's probabilities to the π-selected orbit until a compatible, authenticated source diagram and its measure pushforward are proved.

Exact Fraction regression: for each 0≤m≤6, enumerate all \(3^m\) ternary words; the word probabilities, Pascal count histograms and their conditional ratios agree without floating-point approximation.

## 6. CP-07/08: Pisot generation and the sharp limit of algebraic decompositions

SUCC previously proved/registered PIS-10: every **real number field** K has a Pisot-unit generator β with K=Q(β). This is classical (Salem, and algorithmic work by Vávra–Veneziano 2018, DOI 10.1016/j.jsc.2017.11.005). Thus for any *real algebraic number* α, choosing K=Q(α), one can express α as a rational polynomial in a Pisot β. This is a finite field-coordinate expression, stronger than existence of an arbitrary infinite Pisot-based series. It does **not** preserve positive path grammar, original BBP prime-place labels, or selected real orbits without extra maps.

For a Pisot β and α∈Q(β)∩[0,1), Klaus Schmidt's 1980 theorem proves α has an **eventually periodic greedy β-expansion** (DOI 10.1112/blms/12.4.269). More general algebraic α can be shifted/scaled before expansion; complex algebraic values require real/imaginary components or complex Pisot generalizations. This proves a strong version of the author's algebraic representation conjecture when inverse Pisot powers and finite digit alphabets are allowed; it does **not** prove every sequence of finite arithmetic operations admits a positive, uniform, source-faithful Pisot functor.

**Pisot phase rigidity points toward coherence, not generic randomness:** for a Pisot algebraic integer β>1 with other conjugates β_j in |β_j|<1,
\[
\operatorname{Tr}_{Q(\beta)/Q}(\beta^n)\in Z,\qquad
\left|\beta^n-\operatorname{Tr}(\beta^n)\right|
\le\sum_{j>1}|\beta_j|^n\to0.
\]
Thus β^n mod1 approaches 0, giving a **nonnormal and non-equidistributed phase** by itself. Example β=1+√2 has conjugate 1−√2, so the deviation is exactly (√2−1)^n.

**Pascal need not preserve Pisot:** β=2+√2 is Pisot because its other conjugate 2−√2 is in (0,1), but β+1=3+√2 is **not**, because the other conjugate 3−√2 exceeds 1. The Pascal transform maps traces Tr(β^n) to Tr((β+1)^n) exactly, so it can destroy Pisot contraction. Exact quadratic-integer arithmetic in tests detects this with no floating tolerance. The earlier SUCC PIS-11..13 firewalls remain in force.

Since π is transcendental, it belongs to no fixed finite-degree algebraic field Q(β). A representation of π through Pisot coordinates must involve an **unbounded series, infinite tower, or transcendental source operation**. Existence of such a representation is easy; proving its selected phase entropy is not.

## 7. CP-09 — RH/Archimedean interface remains a separate arithmetic hypothesis

The completed Riemann zeta contains the genuine Archimedean Gamma factor \(\pi^{-s/2}\Gamma(s/2)\), and \(\zeta(2)=\pi^2/6=\prod_p(1-p^{-2})^{-1}\) is exact. But RH constrains zeros of ζ, not by itself the signed additive lacunary sum \(N^{-1}\sum_{n<N}e(h16^n\pi)\). There is no known proof RH implies π normality, nor a theorem proving that such an implication cannot exist. The continuous and measurable selected-source/Haar defects in parent #427 prevent bare local quotient/topological transfer from supplying the missing phase estimate.

The literal quotient line→circle is \(\mathbb R\to\mathbb R/\mathbb Z\); they are NOT homeomorphic or algebraically identical. The quotient forgets the integer winding/carry. Any reconstruction using SUCC's Pascal triangles, adelic solenoids or arithmetic prime spectra must preserve the source-selected real phase, its integer carries, and all limits in the correct topology.

## 7b. CP-10: authentic BBP source realizes the cross-prime Pascal law EXACTLY (PROVED LOCAL from inherited DSI)

This theorem connects the constructed topological parameterization to **the original zero-selected signed four-pole BBP recurrence**, rather than sampling an unrelated model.

Main XVII's inherited DSI-4 proves that \(n\mapsto U_n\bmod2^a\) is an exact permutation of the residues in every complete block of \(2^a\) consecutive times, since the original 2-adic source interpolation \(F_2\) is an isometry and satisfies \(F_2(0)=U_0=0\).

By CP-04, the ternary prefix \(H(x)\bmod3^b\) is determined by \(x\bmod2^{2b}\). Set \(M=2^{2b}\). Thus for **every starting time A**, every ternary residue c, and the exact original BBP source,
\[
\boxed{
\#\{A\le n<A+M:\ H(U_n)\equiv c\bmod3^b\}
=\#\{0\le x<M:\ H(x)\equiv c\bmod3^b\}.
}\tag{CP-10a}
\]
Here U_n is interpreted in Z₂ using its odd reduced rational denominator; H is the explicitly declared nonadditive homeomorphism of §3. The left side is a genuine source-dependent statement, the right side a finite and exact rational/integer counting problem.

At b=1 (M=4), the distribution is explicitly
\[
\boxed{\Pr(H(U_n)\bmod3=0,1,2)=(1/2,1/4,1/4).}\tag{CP-10b}
\]
This is **not** the 3-adic Haar law \((1/3,1/3,1/3)\). It is a precise source-authenticated example that *perfect* local 2-adic arithmetic equidistribution can become a nonuniform 3-adic probability law under a lawful but non-Haar coordinate change.

**Joint authenticated clock:** the true 3-adic time clock \(16^n\bmod3^b\) has period \(L=3^{b-1}\). By the parent #427 CRT theorem, \((U_n\bmod M,16^n\bmod3^b)\) visits every product state exactly once per \(ML\) consecutive time indices. Applying H to its first coordinate gives the exact factorization
\[
\#\{A\le n<A+ML:\ (H(U_n)\bmod3^b,16^n\bmod3^b)=(c,z)\}
=\#\{0\le x<M:H(x)\equiv c\bmod3^b\}
\]
for every \(z\in1+3\mathbb Z/3^b\mathbb Z\). This is a finite **joint product law** with a biased H-pushforward factor; it does not equate the transported source with the native 3-adic BBP value or with the Archimedean π phase.

**Source/Pascal triangle calibration:** Within an \(M'=2^{2m}\) time block, condition on \(U_n+1\) being a 2-adic unit. Exactly half the times satisfy this, and their first \(2m-1\) freely varying binary unit bits are Haar-uniform by the DSI permutation. Applying g gives precisely the conditional unit prefix word law from CP-06; consequently the short-codeword count has the exact Pascal distribution
\[
\boxed{\Pr_{\mathrm{BBP},\,\mathrm{unit}}(A=k)={m-1\choose k}2^{-(m-1)}}
\]
for the \(m-1\) ternary tail symbols. This is SOURCE-AUTHENTICATED 2-adic local probability. It does **not** assert that \(U_n\) is 3-adically integral (it need not be), or that π's real-circle orbit is normal.

Finite exact tests cross-check b=1..6 complete source periods, b=1..4 full joint clock periods, and m=1..6 conditioned Pascal paths. Every all-horizon assertion is justified by inherited DSI plus the declared exact modulus, not by extrapolating these tests.

## 8. Source-aware verdict and next falsification

- **DISCLOSED/CLASSICAL:** CP-01 binomial transform; CP-02 local interpolation/nonextension; CP-03 explicit Cantor dynamical conjugacy; CP-04 no pro-p group iso and quantitative modulus; CP-05/06 Haar obstruction and exact q-sensor defect; CP-07/08 established Pisot algebraic generator and Schmidt eventual-periodic expansion, plus explicit Pisot-shift failure.
- **OBSERVED FINITE:** integer-forward/backward identities, exact finite prefix probabilities, 2/3-adic modulus checks, quadratic Pisot controls. Exact Python tests do not certify whole field-theoretic literature.
- **REFUTED as inference:** dynamic topological conjugacy ⇒ invariant Haar; Pascal sequence equivalence ⇒ isomorphism of adic rings; Pisot algebraic decomposability ⇒ π normality; prime/Gamma zeta source alone ⇒ selected Archimedean phase cancellation.
- **OPEN:** a four-pole, U_0=0 selected mixed real/2-adic/3-adic phase theorem, the source-selected ×3 triangle-defect decay in parent #427, positive entropy/nonconcentration in every relevant ergodic component, RH, π normality.

**Decisive next experiment:** Transport the *actual original BBP triangle sensor* through a declared common real/2-adic/3-adic chart, pre-register both raw and Haar-parameterized views, and measure a signed ×3 mixed real/cofiber correlation. Any genuine saving must distinguish the original seed from the coherent counterseed and from the explicit biased-prefix homeomorphism, not merely reproduce a Pascal equality or a topological conjugacy.

**Independent primary references:** Schmidt, *On Periodic Expansions of Pisot Numbers and Salem Numbers* (1980), https://doi.org/10.1112/blms/12.4.269 ; Vávra & Veneziano, *Pisot unit generators in number fields* (2018), https://doi.org/10.1016/j.jsc.2017.11.005 ; Rudolph, *×2 and ×3 invariant measures and entropy* (1990), https://doi.org/10.1017/S0143385700005629 ; existing SUCC PIS-01/PIS-10/11/12/13 and prior #427 and Main XVII; Clay RH problem, https://www.claymath.org/millennium/Riemann-Hypothesis/.
