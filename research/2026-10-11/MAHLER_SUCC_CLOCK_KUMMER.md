# SUCC finite differences are Mahler interpolation; the clocks require Kummer coherence

**Date:** 2026-10-11. **Original user question:** “Oh p-adic interpolation seems trivial. Isn't it just algebra on clocks?” This clarification follows the maintainer's integer SUCC/FUCC prime-jet periods, shared basis/differential reconstruction, p-adic residue-one Euler units and Kubota–Leopoldt weight-two interpolation.

**Verdict:** **Yes for the reconstruction mechanism.** The unit groups modulo powers of an odd prime are compatible finite multiplicative clocks, and Mahler's theorem shows that the *exact SUCC forward-difference coefficients* are a complete reconstruction basis for continuous \(p\)-adic functions. **No for the arithmetic existence theorem.** The weight-specific zeta values must satisfy nontrivial Kummer congruences before a coherent interpolation is justified. Preserving the correct Euler factor and torsion/Teichmüller branch is essential.

**Status:** classical modular arithmetic, classical Mahler theorem and Kummer congruences (IMPORTS), exact verified finite computations with negative controls. No new number-theoretic theorem, \(p\)-adic \(L\)-function or measure construction, RH proof, completed Weil positivity or Archimedean Gamma/adelic proof follows from the tests.

**Primary authorities:** NIST [DLMF §24.10(ii)](https://dlmf.nist.gov/24.10) on Kummer congruences and precise exceptional-index hypotheses; Keith Conrad, [Mahler Expansions](https://kconrad.math.uconn.edu/blurbs/gradnumthy/mahlerexpansions.pdf), Theorems 1.2 and 2.1 and §3 on exponential functions; Keith Conrad, [A q-Analogue of Mahler Expansions](https://kconrad.math.uconn.edu/articles/qmahler1.pdf), *Advances in Mathematics* 153 (2000), 185–230; [Kubota–Leopoldt Lean blueprint](https://cbirkbeck.github.io/AINTLIB-blueprints/padic/Overview-and-roadmap/Part-I-___-The-Kubota___Leopoldt-p-adic-L-function/). The mathematical statements of these theorems are **not** proved by finite tests.

## 1. Two clocks that must not be conflated

At a fixed prime \(p\), SUCC/FUCC prime jets traverse \(1,p,p^2,\ldots\), where \(v_p(p^k)=k\). These are NONUNITS mod \(p^r\) for k>0.

The independent **unit clock** is \((\mathbb Z/p^r\mathbb Z)^\times\), for an odd prime, with Euler period
\[
\boxed{T_{p,r}=\varphi(p^r)=(p-1)p^{r-1}.}
\]
Euler's theorem yields \(u^{n+T_{p,r}}\equiv u^n\bmod p^r\) for every unit u. But the maintainer's FUCC jet return gap is
\[
\boxed{\tau_{p,r-1}=p^r-p^{r-1}=(p-1)p^{r-1}=T_{p,r}.}
\]

This is an EXACT cross-description identity between additive address gaps along p-powers and the period of multiplicative unit residues at the same resolution. It is a classical equality, not a construction of the zeta functional equation or RH.

For example \(p=5,r=2\): the unit clock modulo \(25\) has period \(20\); weights \(2\) and \(22\) produce indistinguishable readings \(u^2\equiv u^{22}\bmod25\) for every unit u. We test this by enumerating the actual units and computing exact modular powers.

## 2. Mahler theorem is precisely the user's finite-difference/SUCC basis

Let \(\Delta f(n)=f(n+1)-f(n)\). Mahler's theorem says a function \(f:\mathbb Z_p\to\mathbb Q_p\) is continuous iff it has a unique, uniformly convergent Newton/Mahler expansion
\[
\boxed{f(x)=\sum_{j=0}^\infty a_j\binom xj,\quad
a_j=(\Delta^j f)(0),\quad a_j\longrightarrow0\ \text{in }\mathbb Q_p.}
\]

This is the *same* SUCC derivative basis and initial-condition reconstruction already proved locally for finite observed paths in SUCC draft PR #14, now with the genuine \(p\)-adic completion criterion. All coefficients at once determine the continuous function because the nonnegative integers are dense in \(\mathbb Z_p\). A finite prefix of the coefficients does NOT by itself determine the entire function; the tail and its \(p\)-adic bounds are necessary.

### 2a. The local Euler factor is literally a reconstructed SUCC clock

Use \(f_p(n)=(1-p)^n\). Direct finite-difference algebra gives
\[
(\Delta^j f_p)(0)=(-p)^j.
\]
Each successive coefficient gains exactly one unit of \(p\)-adic valuation. Since \(1-p\in1+p\mathbb Z_p\), Mahler's theorem permits interpolation to all \(x\in\mathbb Z_p\), particularly to \(x=-1\).

At \(-1\) the generalized binomial coefficient is \(\binom{-1}{j}=(-1)^j\). Therefore
\[
\boxed{f_p(-1)=\sum_{j\ge0}(-p)^j(-1)^j
=\sum_{j\ge0}p^j=\frac1{1-p}=E_p(-1).}
\]

For K terms:
\[
\boxed{
E_p(-1)-\sum_{j=0}^{K-1}p^j
=\frac{p^K}{1-p},\quad
v_p(\text{error})=K.}
\]
Each newly transmitted SUCC jet coefficient gives another unit of local clock precision. This **reconstructs one individual local factor**, not the infinite real Euler product or its Archimedean completed value \(\zeta(-1)=-1/12\). The failure of the global product of these locally continued factors was proved in SUCC PR #15.

## 3. Why clocks alone do not manufacture the p-adic zeta function

The special values at negative odd integers are given by classical Bernoulli numbers:
\[
\zeta(1-k)=-\frac{B_k}{k},\qquad k=2,4,\dots .
\]
At the p-adic level their correct source for interpolation is the **Euler-factor-corrected value**
\[
A_k=(1-p^{k-1})\zeta(1-k).
\]
Kummer's congruences prove that for positive even k,l, when
\[
k\equiv l\bmod(p-1)p^{r-1},
\qquad p-1\nmid k,l,
\]
these corrected rational values are p-adic integers and satisfy
\[
\boxed{A_k\equiv A_l\pmod{p^r}.}
\]

The hypothesis \(p-1\nmid k\) is not cosmetic: special exceptional weights have different divisibility and possible pole/branch issues. Analytic p-adic interpolation additionally needs the suitable Teichmüller/weight branch, compatibility at every r, and ultimately a bounded p-adic measure or equivalent function construction. A formal clock period itself never proves the required number-theoretic congruences.

### 3a. Exact negative control: p=5, precision 25

At \(p=5\), the clock period \(T_{5,2}=20\). Weights 2 and 22 occupy the same clock position.

The corrected values:
\[
A_2=(1-5)\zeta(-1)=\frac13\equiv17\pmod{25},
\]
\[
A_{22}=(1-5^{21})\zeta(-21)\equiv17\pmod{25}.
\]

**Remove the correction and clock compatibility FAILS:**
\[
\zeta(-1)=-\frac1{12}\equiv2\pmod{25},\qquad
\zeta(-21)=-\frac{B_{22}}{22}\equiv17\pmod{25}.
\]

Thus the p-th Euler correction is not arbitrary decoration. It is genuinely needed so these particular zeta-derived values occupy compatible clock readings. Tests also compare p=5 at precision 125 (weights 2 and 102, corrected residue 42), p=7 at precision 49 (weights 2 and 44, residue 25), and p=11 at precision 121 (weights 2 and 112, residue 21). The universal congruence is a **CLASSICAL imported theorem**, not an experimental inference from these examples.

### 3b. A clock/continuity failure even for an elementary source

Take \(f(n)=(-1)^n\). Its SUCC differences are \((\Delta^j f)(0)=(-2)^j\). Over \(\mathbb Z_2\), these coefficients tend to zero 2-adically, and the parity function interpolates continuously.

Over \(\mathbb Z_3\), the same coefficients are p-adic units and **do not tend to zero**. In fact \(3^r\to0\) 3-adically but \(f(3^r)=-1\) while \(f(0)=1\). So there is **no** continuous function on all \(\mathbb Z_3\) agreeing with those integer values.

To interpolate the separate exponent classes, one must respect the unit-group root-of-unity/Teichmüller clock, which is exactly the role of weight branches in KL interpolation. This falsifies the blanket assertion that modular clock algebra automatically yields one global continuous p-adic function.

## 4. What is novel here, and what isn't

**Established/classical:** unit group periods, SUCC p-jet equalities, Mahler expansion, Kummer congruences, Euler factor correction, Teichmüller branch separation and Mazur/Kubota–Leopoldt measures.

**New to this particular SUCC project:** explicit identification of its previously implemented finite Newton-difference packet with Mahler's completed function basis, the equal prime-jet and unit-clock periods, exact local Euler factor reconstruction from the geometric SUCC jet, and the negative-source clock controls tied to the zeta special-value problem. This is a REINTERPRETATION/INTEGRATION of classical results rather than a priority claim in mathematics.

**Still missing:** a source-derived SUCC/FUCC proof of Kummer congruences across all clock levels, the actual construction of the relevant p-adic measures, and any source-derived Gamma/Archimedean transport or Weil positivity object. The p-adic special-value theory also does NOT simply reproduce the complex critical-strip RH zero problem.

## 5. Falsifiers and next mathematically consequential construction

- **Clock group:** verify every admissible residue unit has exponent period dividing \((p-1)p^{r-1}\); confirm a lower-resolution period need not work at higher resolution.
- **Exact SUCC Mahler coefficient:** difference \(r\) of \(n\mapsto(1-p)^n\) equals \((-p)^r\); K-th truncation at \(-1\) has error valuation K.
- **Kummer:** corrected values at clock-equivalent weights agree modulo p^r in admissible branches; uncorrected values can fail.
- **Branch:** torsion parity source over Z3 is not continuously interpolable, despite each finite power being elementary clock algebra.
- **Provenance:** do not confuse one evaluated local Euler factor, a Kummer finite sample, a p-adic analytic interpolant, a complex completed zeta function, and a full RH-compatible operator proof.

**Next test of substance:** express a p-adic distribution on unit clocks as a projectively compatible family of finite residue-class weights \(\mu_r\), enforce pushforward coherence \(\mu_r(a)=\sum_{b\bmod p^{r+1},\ b\equiv a\bmod p^r}\mu_{r+1}(b)\), and demand a UNIFORM p-adic norm bound. Compare its moments to corrected zeta values and test false/mutated Euler sources. This builds toward a genuine Mazur measure rather than only numerical modular congruences. After verifying the \(p\)-adic side, compare a source-compatible adelic Fourier/Gamma channel; do not claim a proof of RH without completed Weil identification.

**Verdict:** p-adic interpolation is exactly *algebra on compatible clocks equipped with a convergent SUCC difference basis*, but zeta interpolation requires proving that the actual number-theoretic moment data satisfy those compatibility laws. The reconstruction is elementary; the existence and source-specificity of the zeta interpolation object are load-bearing.
