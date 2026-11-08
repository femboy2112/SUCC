# Operation PRIME–FROBENIUS SOURCE SIEVE × RH-SHAPED SPECTRAL GATE

**2026-11-06. Original four-pole BBP, literal U0=0, strictly additive child of PR #531.** The exact pole/local-residue theorems are new **LOCAL DERIVATIONS** with finite independent arithmetic checks, not claimed globally novel. Their n→∞ consequences invoke the classical **unconditional** prime number theorem (PNT) and PNT in arithmetic progressions mod4. π normality, source-selected real signed Weyl cancellation and RH remain **OPEN**.

## Setup — unwrapped source, odd denominator and typed prime principal part

\[
r(j)=\frac{120j^2-89j+16}{(2j-1)(4j-1)(8j-7)(8j-3)}
=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2},
\quad U_0=0,\quad U_n=\sum_{j=1}^{n}16^{n-j}r(j).
\]

Write \(U_n=a_n/d_n\) in lowest terms; \(d_n\) is odd. The real fractional phase \(x_n=\{U_n\}\) has the same reduced denominator \(d_n\). For an odd prime p and a rational z with p-adic valuation at least -1, the notation \([p z]_p\) denotes its reduction in \(\mathbb F_p\). It is **not** a real Fourier phase. If \([p z]_p\ne0\), then v_p(z)=-1.

For n≥8 and p>n, \(p^2>8n\); every BBP pole has magnitude at most 8n. A pole divisible by p is therefore a simple contribution with denominator \(k p\) for an odd integer k∈{1,3,5,7}, and all k are invertible modulo p. Since p>7, no exceptional small-prime denominator occurs in the coefficient.

## PF-01: full (n,2n] Frobenius source residue — PROVED LOCAL

Fix n≥8, prime n<p≤2n, and \(j_0=(p+1)/2\), the original \(2j-1=p\) pole time. Factor the p-local principal part as

\[
\boxed{[pU_n]_p=16^{n-j_0} F_{p,n}\pmod p.}\tag{PF1}
\]

The coefficient \(F_{p,n}\) is one of **five explicit rational numbers** (all denominators coprime to p):

1. For p≡1 mod4, put
\[
j_5=
\begin{cases}
(5p+3)/8,&p\equiv1\pmod8,\\
(5p+7)/8,&p\equiv5\pmod8,
\end{cases}
\quad j_3=(3p+1)/4.
\]
Then
\[
\boxed{F_{p,n}=\frac72-\frac15{\bf1}_{j_5\le n}-\frac16{\bf1}_{j_3\le n}
\in\{7/2,33/10,47/15\}.}\tag{PF2}
\]
The j3 pole cannot enter before j5 because \(j_3-j_5=(p+2-b)/8>0\) for b∈{3,7} and p>7.

2. For p≡3 mod4, put
\[
j_7=
\begin{cases}
(7p+3)/8,&p\equiv3\pmod8,\\
(7p+7)/8,&p\equiv7\pmod8.
\end{cases}
\]
Then
\[
\boxed{F_{p,n}=-\frac{19}{6}+\frac1{14}{\bf1}_{j_7\le n}
\in\{-19/6,-65/21\}.}\tag{PF3}
\]

**Proof, explicit Euler/Frobenius transport.** Each original signed pole is a rational summand \(c/(a j-b)\) with a∈{2,4,8}; if \(a j-b=k p\), its p principal part is \(c/k\) multiplied by 16^(n-j). The only possible odd pole multiples for p>n are k≤7. Let χ₂(p)=(2/p) be the quadratic Legendre character; Euler's criterion gives \(2^{(p-1)/2}\equiv χ₂(p)\pmod p\).

Normalizing each contribution by \(16^{n-j_0}\), elementary exponent subtraction gives:
- pole \(8j-7=kp\): \(16^{j_0-j}=\chi_2(p)2^{(1-k)/2}\);
- pole \(8j-3=kp\): \(16^{j_0-j}=\chi_2(p)2^{(5-k)/2}\);
- pole \(4j-1=kp\): \(16^{j_0-j}=2^{3-k}\);
- pole \(2j-1=p\) at j0: coefficient −1/2.

Negative exponents are modular inverses of 2, well defined for p odd. These identities also use \(2^{p-1}=1\pmod p\).

For p≡1 mod8: k=1 in 8j−7 contributes +4, k=5 in 8j−3 contributes −1/5, k=3 in 4j−1 contributes −1/6. For p≡5 mod8 the same constants come from 8j−3(k=1) and 8j−7(k=5). Together with −1/2 this gives PF2.

For p≡3 mod8: k=1 in 4j−1 contributes −2, k=3 in 8j−7 contributes −2/3, k=7 in 8j−3 contributes +1/14. For p≡7 mod8 the same constants come from 8j−3(k=3) and 8j−7(k=7). Together with −1/2 this gives PF3. These are actual modular interference coefficients. They have NO automatic interpretation as real signs of e(h U_n).

For primes p≡1 mod4, none of 7/2,33/10,47/15 vanishes modulo p: their positive numerator prime factors {7,3,11,47} are all ≡3 mod4. For p≡3 mod4, −65/21 never vanishes since its numerator factors {5,13} are ≡1 mod4. The **only** possible zero is −19/6 at p=19; the j7 pole enters at n=(7·19+3)/8=17. Thus for n≥8 and p in (n,2n]:

\[
\boxed{v_p(U_n)=-1\quad\text{except exactly }p=19,\ 10\le n\le16.}\tag{PF4}
\]

At that exceptional finite interval, \([19U_n]_{19}=0\), so \(v_{19}(U_n)\ge0\); it does not divide the reduced denominator. The exception is retained as a true pole-interference failure, **not** erased by a test adjustment.

## PF-02: (2n,4n] source residues and collision-corrected bit character — PROVED LOCAL

Let n≥8 and p prime in (2n,4n]. If p≡1 mod4, only one pole denominator in the original history is divisible by p:
- p≡1 mod8: 8j−7=p, j=(p+7)/8, coefficient 4;
- p≡5 mod8: 8j−3=p, j=(p+3)/8, coefficient −1.

Thus \([pU_n]_p=c16^{n-j}\ne0\) modulo p.

If p≡3 mod4, the first pole is 4j−1=p at \(j_a=(p+1)/4\) with coefficient −1/2. A second pole may occur at 3p:
- p≡3 mod8: 8j−7=3p at \(j_b=(3p+7)/8\), coefficient +4/3;
- p≡7 mod8: 8j−3=3p at \(j_b=(3p+3)/8\), coefficient −1/3.

If j_b>n the single pole is nonzero. If j_b≤n, Euler's criterion gives \(16^{j_b-j_a}\equiv-8\) for p≡3 mod8 and \(16^{j_b-j_a}\equiv2\) for p≡7 mod8. Factoring 16^(n−j_b), the combined coefficients are respectively

\[
-\tfrac12(-8)+\tfrac43=\tfrac{16}3\not\equiv0\pmod p,
\qquad
-\tfrac12(2)-\tfrac13=-\tfrac43\not\equiv0\pmod p.
\]

Thus every p∈(2n,4n] has exactly v_p(U_n)=−1. The p=23, n=10 case is a recorded **failed single-pole prediction**: a 3p pole contributes and cannot be omitted. The corrected two-pole formula passes exact tests. This is a genuine *prime-Frobenius interference* calculation, not an RH/normality assertion.

## PF-03: (4n,8n−7] conductor-four prime shell — PROVED LOCAL

For prime 4n<p≤8n−7 with p≡1 mod4:
- p≡1 mod8 appears uniquely at 8j−7=p;
- p≡5 mod8 appears uniquely at 8j−3=p.

All other pole denominators are smaller than p or incompatible with p modulo4, and 3p>8n. Hence the principal coefficient is 4 or −1, respectively, and v_p(U_n)=−1.

## PF-04: exponential ORIGINAL denominator growth, with both limits controlled — PROVED LOCAL using classical PNT/AP

For every n≥17, define the source-forced prime product

\[
\boxed{\displaystyle
\mathscr Q_n=
\prod_{\substack{n<p\le4n\\p\ {\rm prime}}}p
\prod_{\substack{4n<p\le8n-7\\p\equiv1\pmod4}}p.
}\tag{PF5}
\]

PF1–PF3 prove \(\mathscr Q_n\mid d_n\) and each selected prime occurs with p-adic valuation **exactly −1** in U_n. By the ordinary prime number theorem \(\vartheta(x)\sim x\), and the classical prime number theorem for residue class 1 mod4 \(\vartheta(x;4,1)\sim x/2\),

\[
\log\mathscr Q_n=
[\vartheta(4n)-\vartheta(n)]
+[\vartheta(8n-7;4,1)-\vartheta(4n;4,1)]
=5n+o(n).
\]

Thus

\[
\boxed{\displaystyle \liminf_{n\to\infty}\frac{\log d_n}{n}\ge5.}\tag{PF6}
\]

This is UNCONDITIONAL (no RH/GRH): the PNT/AP inputs are established classical theorems. Finite checks are not substitutes for those analytic theorems.

**Matching linear-depth upper class.** Let \(f_1(j)=2j-1,f_2(j)=4j-1,f_3(j)=8j-7,f_4(j)=8j-3\). Differences of suitable integral multiples of distinct factors are in {±1,±3,±4,±5}. Consequently no prime p>5 divides two distinct f_i(j) at the same j. Since each 0<f_i(j)≤8n for j≤n, for p>5 we have v_p(D(j))≤floor(log_p(8n)). The exceptional odd primes 3 and 5 each contribute at most 4floor(log_p(8n)), increasing a common lcm by at most a polynomial factor. Because every r(j) denominator divides D(j), and U_n is an integer-weighted sum,

\[
d_n\mid {\rm lcm}_{j\le n}D(j)
\mid {\rm lcm}(1,\dots,8n)\cdot
3^{3\lfloor\log_3(8n)\rfloor}5^{3\lfloor\log_5(8n)\rfloor}.
\]

Since \(\log{\rm lcm}(1,\dots,x)=\psi(x)\sim x\), conclude

\[
\boxed{\displaystyle
5\le\liminf\frac{\log d_n}{n}
\le\limsup\frac{\log d_n}{n}\le8.}\tag{PF7}
\]

Thus \(\log d_n=\Theta(n)\) for the genuine zero-seeded rational BBP states. This proves, rather than numerically extrapolates, the source-specific **linear exact-readout depth** missing in PR #528.

## PF-05: precise cross-place resolution barrier — PROVED LOCAL for THIS reconstruction method

PR #528 reconstructs the fractional rational numerator 0≤a_n<d_n from V(n)−C_n modulo 2^K and *known* d_n provided 2^K≥d_n. For this explicit bounded-residue method the minimum valid K_n satisfies

\[
K_n=\lceil\log_2 d_n\rceil,\quad
\boxed{\liminf_{n\to\infty}K_n/n\ge5/\log2=7.2134\ldots.}\tag{PF8}
\]

A complete 2-adic Haar census from N observations only resolves at most 2^k≤N, i.e. k≤log₂N. At time n comparable to N, the exact rational numerator readout requires **linear** bits. This incompatibility is unconditional *for the PR #528 single-modulus numerator reconstruction*, not an information-theoretic impossibility theorem for all source-aware algorithms.

The prime-denominator sieve also survives addition of any fixed **rational seed** s with denominator coprime to sufficiently large selected primes: the extra 16^n s is p-integral. Thus PF6 is source-specific but **NOT literal-zero-seed selective**. This is a crucial limitation: the missing real phase inequality must use the original zero commitment beyond these prime divisors.

## PF-06: a genuinely uniform Galois virtual orbit, and its failed transport — PROVED LOCAL

Because \(U_n=a_n/d_n\) is a reduced rational and d_n is odd, \(\zeta_n=e(U_n)\) is a **primitive d_n-th root of unity**. Let

\[
\nu_n^{\rm Gal}=\frac1{\varphi(d_n)}
\sum_{\substack{u\bmod d_n\\(u,d_n)=1}}\delta_{\{uU_n\}}
\]

be the uniform Galois orbit over the cyclotomic conjugates. For each fixed nonzero integer h, Ramanujan's exact sum identity gives

\[
\int e(hx)\,d\nu_n^{\rm Gal}(x)
=\frac{c_{d_n}(h)}{\varphi(d_n)},\quad
c_d(h)=\sum_{q\mid\gcd(d,h)}q\,\mu(d/q).
\]

Hence \(|c_d(h)|\le\sigma_1(|h|)\) independently of d. For odd d, multiplicativity and \(\varphi(p^a)\ge\sqrt{p^a}\) for odd p imply \(\varphi(d)\ge\sqrt d\). PF6 therefore gives for any \(\epsilon>0\) and all large n

\[
\boxed{\left|\int e(hx)\,d\nu_n^{\rm Gal}(x)\right|
\le\sigma_1(|h|)\exp[-(5/2-\epsilon)n].}\tag{PF9}
\]

Consequently **the entire original-source Galois virtual ensemble converges to Haar** on the real circle, with exponentially decaying fixed-mode Fourier errors.

**Selection gap, explicitly REFUTED inference.** A completely different nonnormal rational sequence \(y_n=1/\mathscr Q_n\) has the same exponentially large forced prime *denominator mass*, and its Galois orbits are Haar in the limit, but the selected phases \(\{y_n\}\to0\), not Haar. It is not the authentic four-pole recurrence. Thus **high cyclotomic order plus virtual-field Haar does not imply selected real-time Haar**. The actual original source/zero selector still needs a signed transport law. PF9 is not a base-16 normality result.

## PF-07: RH-shaped operator analogy, typed and adversarial

Weil's criterion characterizes RH through a **nontrivial signed prime/Gamma quadratic form** required to be nonnegative for every admissible test function. SUCC's dyadic Fourier return/Poisson energies are already positive for EVERY orbit by Gram-square algebra. This positivity cannot select π or distinguish nonnormal measures; the needed step is **decay/coercivity** for the authenticated zero-seeded state.

One cannot replace this by an abstract claim of spectral mixing. Construct a Bernoulli digit measure with p0=1/2 and each p_a=1/30 for 1≤a≤15. This is a ×16-invariant **mixing** measure (iid base-16 digits), but it is not Haar: its first digit is zero with probability 1/2 instead of 1/16. It is singular to Haar by the almost-sure limiting zero-digit frequency. Thus exclusion of nontrivial Koopman eigenvalues / weak mixing **does NOT** imply normality. The measure's Fourier amplitudes must be pinned to Haar, not just its eigenvalue locations.

The new PF1–PF6 use quadratic character (2/p) at conductor 8 and prime density at modulus 4. Their analytic inputs concern known zero-free behavior at the Re(s)=1 boundary for Dirichlet L-functions, **not RH critical-line positivity**. Neither RH nor GRH is assumed or proved here, and RH would not by itself supply the missing π signed source-carry transport.

## PF-08: honest conditional "no residual coarse phase energy" gate — PROVED CONDITIONAL, premise OPEN

For N=2^m and fixed h≠0, let \(F_n=e(hU_n)\). Define dyadic clock-conditional energies E_(k,m) from PR #531, with \(E_{0,m}=|W_{2^m}(h)|^2\), \(E_{m,m}=1\), and \(D_{k,m}=E_{k+1,m}-E_{k,m}\ge0\). If E_(k+1,m)>0, put \(g_{k,m}=D_{k,m}/E_{k+1,m}\in[0,1]\). Then

\[
\boxed{|W_{2^m}(h)|^2=\prod_{k=0}^{m-1}(1-g_{k,m}).}\tag{PF10}
\]

If some denominator energy vanishes, E0=0 and the corresponding case is trivial. If for some constants η,c>0 at least cm levels have g_(k,m)≥η, then

\[
|W_{2^m}(h)|^2\le(1-\eta)^{cm}.
\]

This is a genuine sufficient **reverse-Poincaré/coarse-energy-exclusion criterion** for dyadic horizons. To obtain **all-prefix** normality one additionally needs the mesoscopic gluing of PR #531 or equivalent off-dyadic control. We have not proved the hypothesis for the selected BBP orbit; its numerical appearance at finite scales is NOT evidence of a source-specific infinite theorem. The exact real source ratio \(\Xi_{2^k,h}(n)=e(h[(16^{2^k}-1)U_n+S_{2^k}(n)])\) is the operative complex phase basis; the Legendre symbol (2/p) used in PF1–PF3 is **not** that phase.

## Provenance, claims and next falsification

- Original four poles and U0=0: SUCC PRs #527–#531.
- Classical PNT/AP modulus 4: [PNT/AP formal blueprint](https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html), [Penn State analytic number theory](https://personal.science.psu.edu/rcv4/568s20/568chapter11.pdf).
- Classical Ramanujan sums: [Montgomery–Vaughan, Multiplicative Number Theory](https://www.ndl.ethernet.edu.et/bitstream/123456789/23715/1/Hugh%20L.%20Montgomery.pdf), §4.1.
- Weil positivity: [Conrey, The Riemann Hypothesis](https://aimath.org/~kaur/publications/90.pdf), §16.
- Related dynamical caveat: Lagarias (2001), DOI 10.1080/10586458.2001.10504456.

All all-n prime principal-part formulas are proved algebraically here; the n→∞ exponent relies on well-established PNT/AP as an external theorem, not finite testing. Fresh exact rational holdouts and failure receipts are preserved separately. **OPEN:** for the authentic four-pole and literal zero state, a real signed \(\mathcal P_{2A}\le\rho\mathcal P_A+o(1)\) or equivalent all-horizon Weyl saving. No globally novel priority is claimed without independent external review.
