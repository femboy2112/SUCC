# Source-authenticated holographic triangle — exact reconstruction, Gamma drive, and two-scale obstruction

**2026-11-06; SUCC research only.** Strictly additive child of PR #529 at `2016e3bd96b3aefc3902380bce8e0ca0bac9d547`. `PROVED LOCAL` means a full displayed mathematical argument within the scope stated, not Lean or independent priority. The user's **golden–harmonic–Euler–Mascheroni co-dual** is preserved as the motivation, with its unproved source-identification separated from the exact BBP coupling. **π base-16 normality remains OPEN.**

## 0. Exact source and where the objects live

Original zero-seeded four signed poles:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\tag{HT0}
\]

For every n the **combined** denominator is odd. The rational unwrapped state U_n therefore has odd denominator. Write in the ordinary real ordering

\[
U_n=C_n+x_n,\qquad C_n=\lfloor U_n\rfloor\in\mathbb Z,\quad x_n=\{U_n\}\in\mathbb Q\cap[0,1).
\tag{HT1}
\]

All three rationals can be embedded in \(\mathbb Z_2\), with congruence modulo \(2^K\) defined by the inverse of any odd denominator; this is NOT a reduction homomorphism from \(\mathbb R/\mathbb Z\). Parent PR #527 proves the entire-clock 2-adic interpolation V and the exact selected equality \(V(n)=U_n\in\mathbb Z_2\). Parent #528 supplies the carry and finite-numerator reconstruction. We reconstruct those mathematical objects here rather than identifying Euler's constant or the real golden ratio with 2-adic numbers.

## HT-01. Pairwise projection has a one-bit obstruction on unrestricted triples — PROVED LOCAL

Fix K>=1 and R_K=Z/2^K Z. For (A,B,X) in R_K³ define the *pairwise edge hologram*

\[
E_K(A,B,X)=(P,Q,R)=(A+B,\ A+X,\ B+X).
\tag{HT2}
\]

Its integral matrix \(\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix}\) has determinant \(-2\). For unrestricted input triples:

\[
\boxed{\ker E_K=\{(0,0,0),\;2^{K-1}(1,1,1)\},\quad
\mathrm{im}\,E_K=\{(P,Q,R):P+Q+R\equiv0\pmod2\}.}\tag{HT3}
\]

Proof. In the kernel, B=X=−A and 2A=0; the only solutions in R_K are A=0,2^(K-1). Every output has P+Q+R=2(A+B+X), hence even total. Exactly half the target triples have even total. The kernel has order 2, so image size (2^K)^3/2; equality follows. Over Z₂ itself, the kernel vanishes, but the cokernel is Z/2. Over Q, E is invertible. **This algebraic parity obstruction does not by itself identify a physical BBP carry defect.**

## HT-02. Authentic source/carry seam removes the binary ambiguity — PROVED LOCAL

Restrict the center to the physically admissible plane

\[
\mathsf S_K=\{(A,B,X)\in R_K^3:A=B+X\}.
\]

The boundary data land in

\[
\mathsf T_K=\{(P,Q,R)\in R_K^3:P+Q=3R\}.
\]

On these subgroups the pairwise map is a **bijective R_K-linear map**:

\[
\boxed{E_K|_{\mathsf S_K}:\mathsf S_K\simeq\mathsf T_K,\qquad
(A,B,X)=(R,\ P-R,\ Q-R).}\tag{HT4}
\]

Proof. If A=B+X, then R=B+X=A, P=2B+X, Q=B+2X, so P+Q=3R. Conversely any edge triple satisfying P+Q=3R is the E-image of the proposed inverse triple, since (P−R)+(Q−R)=R. Thus the inverse is exact and *requires no division by 2*, for ALL K including K=1. Modulo 2, (P,Q,R)=(X,B,A): the restricted “hologram” simply permutes the two component bits plus their sum.

**Correction to the earlier intuition:** the unrestricted mod-2 null direction is real, but the physical BBP source/carry seam kills it. It is incorrect to claim a surviving holographic one-bit defect on the exact admissible center. The nontrivial missing information is now the *transport of source-labelled real phases*, not a static failure to reconstruct the center.

The map is naturally a labelled-state-graph isomorphism when source and carry labels are included in transitions (HT-03). It is not evidence that spacetime gravitational holography or a physical mind is involved.

## HT-03. Genuine commuting BBP dynamics and exact defect contraction — PROVED LOCAL

Put \(\kappa_{n+1}=\lfloor16x_n+r(n+1)\rfloor\). Then

\[
C_{n+1}=16C_n+\kappa_{n+1},\quad
x_{n+1}=16x_n+r(n+1)-\kappa_{n+1},\quad
U_{n+1}=16U_n+r(n+1).
\tag{HT5}
\]

The edge coordinates obey the **closed source-and-carry-labelled transport law**

\[
\boxed{
P_{n+1}=16P_n+r(n+1)+\kappa_{n+1},\qquad
Q_{n+1}=16Q_n+2r(n+1)-\kappa_{n+1},\qquad
R_{n+1}=16R_n+r(n+1)
}\tag{HT6}
\]

in each R_K. Under any consistently used labels, the compatibility defect \(D=P+Q-3R\) evolves by

\[
\boxed{D_{n+1}=16D_n.}\tag{HT7}
\]

Consequently |D_(n+1)|_2<=2^-4 |D_n|_2 for the corresponding Z₂ lift, and its finite K reduction becomes zero after at most ceil(K/4) steps. With inconsistent edge injections epsilon_P,epsilon_Q,epsilon_R, the exact relation instead is \(D_{n+1}=16D_n+\epsilon_P+\epsilon_Q-3\epsilon_R\). This supplies a calibrated *diagram/coherence error* detector, not a source-uniqueness criterion.

**Adversarial refuter:** the constant non-Haar world U_n=0 under zero forcing has D_n=0 at every step. The rational shadow source \(r_H(n)=H(n)-16H(n-1)\), \(H(n)=n/(2n-1)^4\), also satisfies all these categorical identities and has real x_n→0, not Haar. A consistent mutant source with all labels changed together also preserves D=0. Therefore HT7 **cannot** imply π normality, even when coupled with 2-adic isometry in the shadow example. The genuine source must be authenticated separately.

## HT-04. Gamma/digamma source drive, not an unexplained chart label — PROVED LOCAL / CLASSICAL

Let (w_1,...,w_4)=(4,-2,-1,-1) and (a_1,...,a_4)=(7,4,3,2). Define the finite original-source harmonic potential

\[
H_n=\sum_{j=1}^{n}r(j)
=\frac18\sum_{i=1}^4w_i\left[\psi(n+1-a_i/8)-\psi(1-a_i/8)\right].
\tag{HT8}
\]

The second equality follows termwise from the classical digamma recurrence \(\psi(z+1)-\psi(z)=1/z\) (NIST DLMF 5.5.2). It can also be expressed as a **logarithmic derivative of a normalized Gamma product**:

\[
G_n(t)=\prod_{i=1}^4
\left[\frac{\Gamma(n+1-a_i/8+t)\Gamma(1-a_i/8)}
{\Gamma(1-a_i/8+t)\Gamma(n+1-a_i/8)}\right]^{w_i},\qquad
H_n=\tfrac18\left.\frac{d}{dt}\log G_n(t)\right|_{t=0}.
\tag{HT9}
\]

Thus \(r(n+1)=H_{n+1}-H_n\) exactly. *Substitute this difference into HT6:* the Gamma-derived harmonic edge **supplies the actual source input to the holographic transport**, with no invocation of Gamma as a free-standing metaphor.

A discrete Abel transform gives a useful exact source-to-real realization identity:

\[
\boxed{U_n=H_n+15\sum_{j=1}^{n-1}16^{n-j-1}H_j.}\tag{HT10}
\]

Proof: write U_n=sum_(j=1)^n 16^(n-j)(H_j−H_(j-1)), H0=0, and telescope. At each *finite* horizon the corresponding telescoped identity is

\[
\sum_{j=1}^{n}16^{-j}r(j)
=\frac{15}{16}\sum_{j=1}^{n}16^{-j}H_j+16^{-(n+1)}H_n.
\tag{HT10a}
\]

Normalizing by 16^n and letting n→∞ using the genuine convergent original source gives a second exact Gamma/harmonic representation of the BBP constant:

\[
\boxed{\frac\pi{16}=\frac{15}{16}\sum_{j=1}^{\infty}16^{-j}H_j.}\tag{HT11}
\]

Here HT11 is a re-summation of the original BBP formula, **not** evidence of hexadecimal normality. The analytic common Euler–Mascheroni constant cancels in this source because sum_i w_i=0; parent #529 derives the exact unweighted source sum

\[
H_\infty=\frac{(4+5\sqrt2)\pi}{16}+\frac58\log2
+\frac{5\sqrt2}{8}\log(1+\sqrt2).
\tag{HT12}
\]

This native **silver Pisot unit** \(1+\sqrt2\) is a source-backed analytic/Gamma coordinate. A 4→5 source mutant changes sum_i w_i from0 to1 and reintroduces a (1/8)log n divergence; it is not equivalent to HT12.

## HT-05. Native silver vs externally supplied golden — PROVED LOCAL field obstruction

The original pointed minimal rational source atom algebra identified in SUCC PR #481 uses

\[
m(s)=s^4-s^3+\frac s2-\frac14
=\left(s^2-\frac12\right)\left(s^2-s+\frac12\right).
\tag{HT13}
\]

Its rational algebra is \(\mathscr A=\mathbb Q[s]/(m)\simeq\mathbb Q(\sqrt2)\times\mathbb Q(i)\), by the coprime CRT. The silver unit \(\delta=1+\sqrt2\) belongs to the first factor. The golden unit \(\varphi=(1+\sqrt5)/2\) is NOT an element of this unextended rational algebra, in the sense that no element of \(\mathscr A\) satisfies \(t^2-t-1=0\): such an element would project to a root in EACH factor, forcing \(\sqrt5\in\mathbb Q(\sqrt2)\) and \(\sqrt5\in\mathbb Q(i)\), both impossible. Hence the golden chart requires a **declared scalar extension** (e.g. tensoring with Q(sqrt5)) or a different explicit nonlinear observation. It is not an intrinsic new source unit.

Even allowing that extension, no NONZERO Q-linear intertwiner can send multiplication by golden phi to multiplication by16: if \(L(\varphi v)=16L(v)\), then \(\varphi^2=\varphi+1\) forces \((16^2-16-1)L(v)=239L(v)=0\), so L=0. The corresponding silver relation \(\delta^2=2\delta+1\) yields \((256-32-1)L(v)=223L(v)=0\). Thus the co-dual Pisot chart must be nonlinear, action-dependent, time-dependent or differently transported to encode the authentic BBP recurrence. This is a *typed design constraint*, not a ban on exploring the user's golden triangle.

## HT-06. NEW: every original sample horizon forces two distinct arithmetic readout scales — PROVED LOCAL using Bertrand

Let d_n be the odd reduced denominator of x_n (equivalently U_n). **For every integer N>=6**,

\[
\boxed{\max_{0\le n<N}d_n>N.}\tag{HT14}
\]

Proof. Bertrand–Chebyshev's theorem supplies a prime p with N<p<2N. Since N>=6, p>5. The exact original four-pole prime-birth theorem (parent PR #529 AT-02) gives the first p-pole index

\[
n_p=\begin{cases}(p+7)/8,&p\equiv1(8),\\(p+3)/8,&p\equiv5(8),\\(p+1)/4,&p\equiv3,7(8).\end{cases}
\tag{HT15}
\]

For p<2N each expression is <N when N>=6; hence 0<n_p<N. Before n_p every original r(j), and hence U_(n_p−1), is p-integral. At n_p precisely one of the original four simple pole terms contributes c_p/p with c_p nonzero modulo p; all other original terms are p-integral. Therefore v_p(U_(n_p))=−1 and p divides d_(n_p), so d_(n_p)>=p>N. QED.

**Corollary, sharply scoped.** A complete 2-adic Haar *census* on one sample of N successive observations modulo 2^K requires 2^K<=N. The generic, unambiguous **denominator-bounded** reconstruction of ALL real numerators through the same residue requires 2^K>=max_(n<N)d_n (parent #528's RS4 algorithm). By HT14 these two inequalities cannot BOTH hold for ANY N>=6 on the authentic original source:

\[
\boxed{2^K\le N<\max_{n<N}d_n\le2^K\quad\text{is impossible}.}\tag{HT16}
\]

This proves the need for separate *low-depth census* k and *high-depth readout* K **within this exact residue-census/denominator-bounded reconstruction protocol at every finite horizon**. It does NOT forbid adaptive observers, alternative source-aware decoders, or proofs using a weaker property than numerator reconstruction. Previous PR #528 documented only finite denominator-growth measurements and a conditional bound; HT14 supplies the missing universal original-source quantifier.

## HT-06c. STRONGER original-source Gaussian prime strip and linear readout depth — PROVED LOCAL + CLASSICAL PNT-AP

At a **single arbitrary time n>=2**, look at all odd primes in the strip

\[
\mathcal P_n=\{p\text{ prime}:4n<p\le8n-7\}.
\]

The original four signed BBP poles enforce an **exact Gaussian split/inert distinction**:

\[
\boxed{\text{For every }p\in\mathcal P_n:\quad
v_p(U_n)=\begin{cases}-1,&p\equiv1\pmod4,\\\ge0,&p\equiv3\pmod4.\end{cases}}\tag{HT18}
\]

Proof, with **no probabilistic or asymptotic assumption**: for all 1<=j<=n we have 2j−1<p and 4j−1<p, while 8j−7 and 8j−3 are strictly below 2p. So p divides *some* original source denominator iff it is **exactly equal** to `8j−7=p` (requiring p=1 mod8) or `8j−3=p` (requiring p=5 mod8); those are precisely p=1 mod4. Because p<=8n−7, the corresponding j=(p+7)/8 or j=(p+3)/8 lies in 1..n. Its occurrence is unique among all four pole factors and all source times 1..n, and the signed coefficient there is 4 or −1, a p-unit for p>4n>=8. The rational convolution `U_n=sum_(j=1)^n 16^(n-j)r(j)` therefore contains **one** term of valuation −1 and all others have valuation >=0. Its p-adic valuation is exactly −1, since 16 is a p-unit. For p=3 mod4 in the strip no denominator factor is divisible by p, so U_n is p-integral. QED.

Put

\[
D_n^{\mathrm{split}}=\prod_{\substack{4n<p\le8n-7\\p\equiv1\ (\mathrm{mod}\,4)}}p.
\]

Every such p occurs to *exactly* the first power in the reduced denominator d_n, yielding

\[
\boxed{D_n^{\mathrm{split}}\mid d_n.}\tag{HT19}
\]

The primes congruent to 1 modulo4 are exactly the rational primes that **split** in the Gaussian field Q(i); those congruent to 3 modulo4 are inert. The original source's native atom algebra (PR #481) has a Q(i) component. This is an **exact source-level Gaussian-splitting signature**, not yet a proof of a canonical Frobenius transport arrow from that factor to π's real Weyl phases.

**Linear lower bound using classical PNT in arithmetic progressions.** Let \(\vartheta(x;4,1)=\sum_{p\le x,\ p\equiv1(4)}\log p\). The classical PNT-AP gives \(\vartheta(x;4,1)=x/2+o(x)\). Therefore

\[
\log d_n\ \ge\ \vartheta(8n-7;4,1)-\vartheta(4n;4,1)
=2n+o(n),
\]

where the last remainder is an asymptotic equality for the explicit **lower-bound expression**, not an assertion that log d_n itself equals 2n. Equivalently,

\[
\boxed{\liminf_{n\to\infty}\frac{\log d_n}{n}\ge2,\qquad
\liminf_{n\to\infty}\frac{\log_2 d_n}{n}\ge\frac2{\log2}\approx2.88539.}\tag{HT20}
\]

This is an **unconditional, original-source, all-sufficiently-large-time linear lower bound on denominator precision**, using only (a) the exact original pole genealogy proved above and (b) the classical prime number theorem in progressions. No RH or unknown zero information is assumed.

**Two-resolution consequence (sharpening HT16):** the worst-case denominator-certified readout modulus requires \(K_n\ge\lceil\log_2 d_n\rceil\ge(2/\log2-o(1))n\) at EACH sufficiently large original time n. Meanwhile a complete census of all 2^k states from N observations can have only k<=floor(log2 N). Thus the exact modular reconstruction protocol demands LINEAR high-precision readout against LOGARITHMIC low-precision census. This quantifies the obstruction first identified in SUCC #528 without claiming all possible source-aware decoders obey the same cost.

Classical references: Gaussian prime splitting in Q(i) (Fermat two squares), e.g. Dartmouth number theory notes `https://math.dartmouth.edu/~carlp/kalai3.pdf`; weighted PNT in arithmetic progressions, e.g. Kontorovich's formalized blueprint `https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html`. Parent SUCC PR #529 supplies source first-pole machinery, though the stronger one-time-window proof above is self-contained.

## HT-07. The source-faithful real signed character is still the decisive gate — OPEN

At high readout depth 2^K>=d_n, edge decoding gives X_n=Q_n−R_n modulo 2^K and the exact real numerator

\[
a_n=[d_n(Q_n-R_n)]_{2^K}\quad(0\le a_n<d_n),\quad
\boxed{e(hU_n)=e\left(h\frac{[d_n(Q_n-R_n)]_{2^K}}{d_n}\right).}\tag{HT17}
\]

This is a **complete boundary-to-bulk reconstruction of every finite selected real phase**. Yet the source-specific phase average \(W_N(h)=N^{-1}\sum_{n<N}e(hU_n)\) has no new small bound: the encoding is faithful, not mixing. PR #528's return-fiber energy RS10–RS12 and PR #529's newborn-prime covariance AT6 are still open signed-cancellation gates. The new two-scale theorem shows *why* replacing those by single-depth p-adic Haar is structurally insufficient.

A defensible next theorem must exploit the source-specific Gamma-driven carry increments and the odd-prime genealogy to control the *conditional real phases* across low-depth Haar fibers, not just prove the atlas commutes. A proposed defect energy that vanishes for the wrong source/zero orbit cannot substitute for such a bound.

## Literature, provenance and limitations

- NIST DLMF §5.5.2: digamma recurrence `psi(z+1)=psi(z)+1/z`: https://dlmf.nist.gov/5.5.E2
- Classical Bertrand–Chebyshev (a proof by Erdős): https://math.stanford.edu/~ksound/Math152A10/Bertrand.pdf
- Original Bailey–Borwein–Plouffe (1997), DOI `10.1090/S0025-5718-97-00856-9`.
- Source-local atom algebra in SUCC #481 (read-only source), gamma/silver in #529, exact 2-adic source in #527, and carry reconstruction in #528. Repo AGENTS.md / docs/METHOD.md govern claim labels.
- Claimed here: exact R_K pairwise reconstruction, dynamic intertwiner with source/carry labels, an exact Gamma/harmonic source functor, and a **universal original-source denominator > N theorem**. Not claimed: a real normality theorem, physical holography, Gamma positivity, an embedding phi or Euler gamma into Q₂, a proof that an abstract defect contracts real Fourier bias, or independent external peer review.
