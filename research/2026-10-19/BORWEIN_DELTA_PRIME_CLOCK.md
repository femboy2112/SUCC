# Borwein integral × prime-clock delta gates × SUCC/Brownian transport

**Date:** 2026-10-19. **Base:** Green–Tao synchronized prime-clock branch PR #186, commit 7e8984e0cb5d138760719018e5ac6ec2ab511b26. **Authority:** classical Fourier/probability/CRT theorems with explicit elementary derivations, *exact* rational finite oracles, and one new-to-project cross-domain typed assembly. **Academic priority UNVERIFIED. ABC OPEN. RH OPEN. Original signed Suzuki S4 OPEN.**

## 0. Steelman and boundary conditions

Original intuition (corrected): Borwein integrals rather than Brownian integrals, arranged as a chain of prime-clock evolution, Dirac-delta contacts, one-SUCC jumps, subsequent delta contacts, and later clock evolution, all with an emergent factorial cost. Brownian is a *second, scaling-limit* branch of the same stochastic-operator grammar.

There are three distinct types of mathematical structure. We do not erase their distinction:
1. Continuous Borwein sinc products are Fourier transforms of independent **uniform real increments**. These do **not** read the residues of an integer.
2. Prime-clock phase selectors are exact **finite-group character projectors**, anchored at an explicit genuine prime modulus and SUCC orientation.
3. Markov/Dyson/Poisson/Brownian evolution supplies optional **time-dependent transport**; it is a model chosen by us, not the distribution of prime numbers.

Conflating (1) with (2), or treating (3) as a source-derived proof of arithmetic randomness, is REFUTED as an inference.

## 1. The exact Borwein simplex factorial (BDW-01; CLASSICAL / PAPER PROVED)

Let a_1,...,a_m>0 and let U_j be independent uniform random variables on [-a_j,a_j]. Write sinc(x)=sin(x)/x, sinc(0)=1, and S_m=sum U_j. Fourier inversion applied to the first sinc factor gives

\[
 \boxed{\frac2\pi\int_0^\infty \mathrm{sinc}(x)
   \prod_{j=1}^{m}\mathrm{sinc}(a_jx)\,dx
   =\Pr(|S_m|\le1).}
\]

For m>=1 the sinc product decays sufficiently fast to justify Fourier inversion (ordinary boundary values have probability zero). Set A=sum a_j, delta=A-1.

- When A<=1, no possible sequence of steps escapes [-1,1], so the integral equals pi/2 **exactly**.
- When 0<delta<=2 min_j a_j, the only exceptional paths live in one corner simplex of the m-dimensional jump cube. Put Y_j=a_j-U_j∈[0,2a_j]. Then S_m>1 iff sum Y_j<delta; the simplex volume is delta^m/m!, and cube density is 1/prod(2a_j). Both tails give

\[
 \boxed{
 1-\frac{2I_m}{\pi}=
 \frac{\delta^m}{2^{m-1}m!\prod_{j=1}^{m}a_j}.}
\]

This factor 1/m! is geometric, NOT a fitted normalization or a statement about primes. When delta exceeds 2 min a_j, a single simplex is invalid: **include–exclude overlapping translated simplices**. The exact general formula is

\[
 \Pr(S_m\le x)
 =\frac{1}{m!\prod_j(2a_j)}
 \sum_{T\subseteq\{1,\ldots,m\}}(-1)^{|T|}
 \left(x+A-2\sum_{j\in T}a_j\right)_+^m.
\]

The code implements the full exact Fraction sum and the independently derived first-boundary closed form. An unrelated triangle-law and moderate-scale numerical quadrature were calibrated separately; small 10^(-12) leaks must NEVER be measured by naive oscillatory quadrature.

Classical Borwein data: for a_j=1/(2j+1), j=1,...,6, A<1, and I=pi/2. Add a_7=1/15: delta=982/45045 and

\[
 \boxed{1-2I_7/\pi=
 6879714958723010531/467807924720320453655260875000}
 \quad(\approx1.4706281350\times10^{-11}).
\]

## 2. Prime-only Borwein window: a new finite arithmetic example, not a prime theorem (BDW-02)

Declare the analytic widths a_q=1/q for genuine odd primes q. These widths are a **choice of model**, not a consequence of modular clock readouts.

For odd primes q up through 23, Q=(3,5,7,11,13,17,19,23), the sum A_Q≈0.998956013251 is below 1, so the Borwein integral is EXACTLY pi/2. Adding q=29 gives

\[
 Q'=(3,5,7,11,13,17,19,23,29),\qquad
 A_{Q'}=3343015913/3234846615\approx1.033438771872.
\]

The first overflow remains within one full corner simplex because delta=A-1≈0.03344<2/29. Its exact rational leak is delta^9/(2^8 9! prod_{q∈Q'}(1/q))≈1.82013483066771×10^(-12); the integral itself is approximately pi/2-2.85906110628429×10^(-12). These are exact closed-form finite values, using a declared sequence of **true prime labels**.

**Counterexample to an attractive but false conclusion:** this crossing does not mean that q=29 is the first prime disrupting global synchronization for any specific integer. The unshifted product has NO integer n input; it only knows the selected widths. To read a prime clock we need a separate source-derived projector.

## 3. Prime-clock delta projectors (BDW-03)

For a genuine prime q and any integer n, the exact indicator that the q-clock reads r is

\[
 \boxed{
 P_{q,r}(n)=1_{n\equiv r\bmod q}
 =\frac1q\sum_{k=0}^{q-1}
 e^{2\pi i k(n-r)/q}.}
\]

This is a discrete Kronecker delta, an exact finite root-of-unity identity; it is **not** a Dirac distribution on R and no floating-point equality is required. The code uses exact integer exponents to verify cyclotomic cancellation.

There are three useful gates:
- phase 1: q|(n−1);
- phase −1: q|(n+1), or n mod q=q−1;
- coprime/nonzero: q∤n.

For a verified prime n>q, the nonzero gate is **automatically true**; it therefore carries no discriminatory power in that domain. The −1 gate is one step before phase 0, whereas phase 1 is one step after phase 0. It is NOT generally the nearest residue to phase 1 (q−1 is two steps behind residue 1 when q>3). For q=2, +1 and −1 gates coincide.

A soft **chosen diagnostic**, not source truth, uses phase-distance D_Q(n)=sum_q min((n−1) mod q, q−((n−1) mod q))/q and the shifted Borwein mass

\[
 {\cal B}_Q(n;\lambda)
 =\Pr\left(\left|\lambda D_Q(n)+\sum_{q\in Q}U_q\right|\le1\right),
 \qquad U_q\sim U[-1/q,1/q].
\]

At lambda=0 the score is entirely residue-blind. Even when lambda=1 it may have a BORWEIN PLATEAU: with Q=(3,5), n=31 and n=11 have distinct actual q=3 phase-1 statuses but both scores equal 1. Their hard gates disagree. Thus this soft operator should never be substituted for source authentication, a clock-proof oracle, or the genuine Weil distribution.

## 4. Delta-gated discrete SUCC walk (BDW-04)

Work on the explicitly finite wheel G=Z/WZ, W=prod_{q∈Q}q. Let the deterministic SUCC permutation shift be (Sf)(n)=f(n−1). Let K_h be the Markov convolution with independent **discrete uniform** increments in {-h,...,h}, and let P_{q,r} multiply by the exact q-clock indicator.

A word of stochastic segments, one-unit SUCC steps, and delta contacts is the legitimate sub-Markov operator

\[
 \boxed{
 T=P_m S^{s_m}K_{h_m}\cdots
   P_2 S^{s_2}K_{h_2}
   P_1 S^{s_1}K_{h_1}.}
\]

For a starting delta state, the total mass of Tδ_start is exactly the probability that *every declared readout* succeeded. The Python engine calculates this with rational Fractions. A completely independent test enumerates all possible increment words and checks equality.

The Fourier multiplier of K_h on frequency θ is the **normalized Dirichlet kernel**

\[
 \widehat K_h(\theta)=
 \frac{\sin((2h+1)\theta/2)}
 {(2h+1)\sin(\theta/2)},
\]

with continuous value 1 at θ=0. It is **not identically** sinc(aθ). In a separately declared mesh-scaling limit, a sequence of discrete uniforms can converge to continuous box increments whose Fourier factors are the Borwein sinc factors. Exact CRT projectors remain finite-group objects through the limit only after specifying the maps and preventing aliasing. This is the mathematical typed repair of the imagined Borwein→delta→SUCC→delta chain.

## 5. Brownian is the optional Gaussian scaling, not the original Borwein process (BDW-05)

For an independent centered uniform increment U[-a,a], variance is a²/3 and fourth cumulant is −2a⁴/15. Therefore, for S_m=sum U_j,

\[
 \operatorname{Var}(S_m)=\frac13\sum_j a_j^2,\quad
 \boxed{\kappa_4(S_m)=-\frac2{15}\sum_j a_j^4<0.}
\]

A **nondegenerate finite** uniform sum is not exactly Gaussian. Its Fourier transform satisfies

\[
 \prod_j\sinc(a_jk)
 =\exp\left(-\frac{k^2}{6}\sum_j a_j^2
           +O(k^4\sum_j a_j^4)\right)
\]

in a stated small-frequency range. Under a Lindeberg/small-maximum-step scaling, the limit is Gaussian heat/Brownian, with time parameter T=sum a_j²/3. This scaling is a classical central-limit theorem; no inference is licensed for arbitrary widths.

For *unscaled prime widths* 1/q, the series sum_{q prime}1/q diverges but sum_q1/q² converges. Thus the maximal possible displacement of finite prefixes grows without bound while the independent centered random sum converges in L² and almost surely. It is **not a Gaussian law**: the fourth cumulant remains strictly negative, with finite sum of q^(-4) corrections. This juxtaposes worst-case support with typical stochastic size, not deterministic ABC cancellation.

Alternatively, on a finite prime wheel, continuous-time symmetric random SUCC jumps have the exact Poissonized semigroup

\[
 \boxed{H_t=e^{-t}\sum_{m\ge0}\frac{t^m}{m!}
        \left(\frac{S+S^{-1}}2\right)^m.}
\]

Here the **other** 1/m! arises from a Poisson jump count / time ordering, not a Borwein simplex. The code computes exact finite return coefficients; for a 5-clock wheel, the fifth-jump return c_5=1/16 occurs from winding around the finite circle, but on a 7-wheel c_5=0. This is a genuine finite-boundary diagnostic reminiscent of the finite-propagation account of Borwein's plateau.

## 6. A proof frontier, not another representation theorem (BDW-06)

**Survivors:** Exact Fourier convolution, factorial simplex suppression, genuine modular root projectors, sub-Markov SUCC words, and separately declared Brownian/Poisson limits are mathematically consistent and source-typed.

**Failed inference:** Merely replacing q by a sinc width 1/q and multiplying sinc factors cannot detect whether a prime p lies at phase 1, −1, or nonzero on q. A p-dependent clock delta is indispensable. Moreover, prime moduli and a Brownian limit do not imply prime randomness or ABC/Weil positivity. An apparent 1/m! smallness in a stochastic model is not a deterministic upper bound on all exceptional additive triples.

**Verdict-changing probe:** Fix a genuine finite Q, place an actual source-indexed (a,b,c) p-adic cancellation delta (q^k|a+b), and compare (i) exact integer-box primitive triple counts, (ii) the finite CRT null model, and (iii) a Borwein-smoothed source model, with held-out growing Q and k. Predetermine the discrepancy and reject fake-composite clocks, false additive equality, and matched artificial non-Euler sources. Only a **uniform arithmetic bound** controlling the residual could approach ABC. Any attempted RH application additionally needs the authentic Gamma/pole and signed Suzuki/Weil form, not a substitute positive probability kernel.

## Reproduction

```sh
python -m unittest discover -s tests -p 'test_borwein_prime_clock.py' -v
python -m compileall -q observational_succ/borwein_prime_clock.py tests/test_borwein_prime_clock.py
```

Full SUCC CI and source provenance checks are independent gates; no all-tests pass may be claimed without an actual hosted receipt.

**Primary external mathematical sources:**
- David Borwein and Jonathan M. Borwein, [*Some Remarkable Properties of Sinc and Related Integrals*](https://www.carmamaths.org/resources/db90/pdfs/db90-119.00.pdf), *The Ramanujan Journal* 5 (2001), 73–89. Original Borwein result.
- Robert Baillie, David Borwein and Jonathan Borwein, [*Surprising Sinc Sums and Integrals*](https://carmamaths.org/resources/jon/sinc-sums.pdf), 2007, exact Fourier/Sinc context.
- Satya N. Majumdar and Emmanuel Trizac, [*When random walkers help solving intriguing integrals*](https://arxiv.org/abs/1906.04545), *Physical Review Letters* 123 (2019), random-walk and boundary-causality interpretation.
- Standard finite Fourier orthogonality, Poisson semigroups, Gaussian fourth cumulants, and central limit theorems; original claims are individually derived above. Literature novelty remains UNVERIFIED.
