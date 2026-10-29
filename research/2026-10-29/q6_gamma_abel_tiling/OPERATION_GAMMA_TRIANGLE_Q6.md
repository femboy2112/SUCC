# Operation Gamma Triangle × q=6 Totient/Cototient × Original BBP Signed Carry

**Date:** 2026-10-29. **Authority:** source-derived paper proof and independent exact-rational / high-precision probes; **no Lean kernel claim, no hosted CI, no academic-priority claim.**

**Parent SUCC draft:** #374 at `cf27c6f35d98fc88451e81ad5d586bdfaead24ef` (includes #372, #370, #369, #367); #371 read as an independent sibling. **Merged main** when inspected was `ac7303b2e0e2ec16e3b1d88d186324e1fae65ea5`. Neither original signed forcing, U0=0, historical theorem statements, nor main is modified. **Base-16 normality of pi and RH remain OPEN.**

## 1. The exact source and types

The unchanged four-pole forcing, actual arithmetic state and literal carry are

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
 U_0(s)=s,\quad U_n(s)=16U_{n-1}(s)+r(n),
\]

\[
 x_n(s)=\{U_n(s)\},\qquad
 \kappa_n(s)=\lfloor16x_{n-1}(s)+r(n)\rfloor,
 \quad z_n(h;s)=e^{2\pi i hU_n(s)}.
\]

Here h is a fixed nonzero integer and the genuine selector is s=0. The literal integer carry is retained, not silently replaced by its mod-16 class; for the authentic seed and coherent counterseed it belongs to 0,...,16; for arbitrary initial seeds at n=1 the forcing r(1)>3 can permit larger carries, while at every n>=2 all seeds have carry in 0,...,16. The exact four-pole Green tail satisfies

\[
 T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\qquad
 U_n(0)=16^{n-1}\pi-T_n\quad(n\ge1),\qquad
 0<T_n\le\frac1{15(n+1)^2}\quad(n\ge1).
\]

The displayed source identity and tail estimate are inherited from the positive original-BBP source dossiers; they are not observations from a digit experiment. In particular T_n tends to zero.

A **declared** Pascal sensor on the authentic positive source produces finite exact rational grade probabilities

\[
 q_n(j)=\frac{\binom nj}{r(n)}\sum_{k=0}^{j}(-1)^k\binom jk r(2n-j+k),
 \quad 0\le j\le n;
\]

set q_n(j)=0 outside 0..n. They are nonnegative and sum to one. The inherited proof in draft #370 gives, for n>=3,

\[
 \operatorname{TV}(q_n,w)\le\frac{22}{n},\qquad
 w_j=\frac{j+1}{2^{j+2}},\quad j\ge0.
\]

The Pascal sensor is a mathematical observation of the original source, **not an empirical random mechanism for pi digits**. The finite rank-j+2 Gamma differential used below is a **fixed limiting-rank reference observable** evaluated at each finite grade, not an assertion that finite-n conditional laws are exactly Gamma. The signed marks are taken from the deterministic unchanged recurrence.

## 2. The complete q=6 factorial sheet, before losing the carry

Define `chi(j)=1_[gcd(j,6)=1]`. Primitive grade is chi(j); primitive **Gamma rank** is chi(j+2), because the authentic Pascal–Poisson limit has

\[
 Z\mid J=j\sim\operatorname{Gamma}(j+2,1).
\]

The exact Oily endpoint four-cell masses are

| chi(j) | chi(j+2) | Source-weighted mass |
|---:|---:|---:|
| 0 | 0 | 5/9 |
| 0 | 1 | 172/1323 |
| 1 | 0 | 352/1323 |
| 1 | 1 | 64/1323 |

All four are positive. The **grade-to-rank selector commutator** (not physical Yang–Mills curvature) is

\[
 d_j=\chi(j+2)-\chi(j)
 =\begin{cases}-1,&j\equiv1\pmod6,\\+1,&j\equiv3\pmod6,\\0,&\text{otherwise}.
 \end{cases}
\]

Equivalently, on grade basis vectors e_j with P6 e_j=chi(j)e_j and S²e_j=e_(j+2),

\[
 [P_6,S^2]e_j=d_j e_{j+2}.
\]

This is nonzero for q=6 but identically zero for q=2 because j and j+2 have the same parity. Hence q=6 is the first useful composite selector for this *two-step* seam test. The commutator is a defect of the marked selection, not evidence that the geometric plane has Gaussian curvature.

The complete **unprojected** finite original-source probability tensor is

\[
 M_{n;a,b,c,\theta}=\sum_{j=0}^{n}q_n(j)
 1_{\chi(j)=a}\,1_{\chi(j+2)=b}
 1_{\kappa_{n+j}(0)=c}
 1_{\{U_{n+j}(0)\}=\theta}.
\]

All its nonzero coefficients are exact rational numbers and all phase labels theta are exact rational residues for the original seed. Marginalizing the marks recovers the four finite q_n cell masses. There is no hidden use of real pi in these *finite* exact rational certificates.

## 3. Gamma is the rank differential; Euler gamma is a shared origin

Put lambda=(sqrt(5)-1)/2 and D(r)=psi(r)-lambda^r for r>0. At integer r,

\[
 D(r)=H_{r-1}-\gamma-\lambda^r,
 \qquad D(2)=\lambda-\gamma=\Omega_{OM}.
\]

The two-step grade-to-rank differential is EXACTLY

\[
 A_j:=D(j+4)-D(j+2)
 =\frac1{j+2}+\frac1{j+3}+\lambda^{j+3}>0.
\]

This uses the Gamma/digamma recurrence psi(r+1)=psi(r)+1/r and the golden identity 1-lambda²=lambda. Gamma's logarithmic derivative is load-bearing in **deriving** the harmonic increment. The additive Euler--Mascheroni constant gamma *cancels* across every normalized rank difference: inserting gamma as an extra edge weight would double-count the reference. A_j decreases strictly with j, and

\[
 A_3=11/30+\lambda^6,\qquad A_7=19/90+\lambda^{10},\qquad A_j\le A_7\quad(j\ge7).
\]

## 4. Gamma half-rank, 45-degree Abel twist and flat Beta gluing

Draft #367 constructs the original positive four-pole convolution semigroup mu_(a,t) with Laplace transform

\[
 \mathcal L_{a,t}(s)=[R(a+s)/R(a)]^t,\qquad
 R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad a>0,t\ge0.
\]

Since R(a)~15/a², for every fixed t>0 the scaled aX_(a,t) tends to Gamma(2t,1). Splitting the authentic t=1 positive field into FOUR equal independent convolution parts t=1/4 gives four limiting Gamma(1/2,1) variables whose sum is Gamma(2,1). Their proportions conditional on the sum are Dirichlet(1/2,1/2,1/2,1/2). This splitting is SOURCE-PERMITTED; choosing exactly four subdivisions is a **marked convention**, motivated by the 4 bits of radix 16, not uniquely forced by the original source.

For any r>0 and epsilon>0,

\[
 \int_0^\infty x^{r-1}e^{-(\epsilon-i)x}dx
 =\Gamma(r)(\epsilon-i)^{-r},
 \quad\lim_{\epsilon\downarrow0}=e^{i\pi r/2}\Gamma(r).
\]

The limit is Abel-regularized when the undamped integral is not an ordinary convergent integral. For r=1/2, the phase is exactly pi/4 (45 degrees), and the classical Fresnel integral gives

\[
 \int_0^\infty e^{ix^2}dx=\frac12\Gamma(1/2)e^{i\pi/4}=\frac{\sqrt\pi}{2}e^{i\pi/4}.
\]

For the Gamma rank j+2 split into four equal parts, **each part** carries the declared Abel-boundary phase

\[
 \vartheta_j=e^{i\pi(j+2)/8},\qquad \vartheta_{j+2}=e^{i\pi/4}\vartheta_j.
\]

So the rank-shift +2 rotates the marked complex boundary by exactly **45 degrees**. At q=6's two commutator residues, j=1 has phase 3pi/8 (67.5 deg) and j=3 has 5pi/8 (112.5 deg). This is a rigorous phase identity within the chosen Gamma/Abel representation, **not** a physical rotation in spacetime or proof that BBP carries implement it.

The amplitude needed to glue Gamma pieces is Beta:

\[
 B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)},\quad
 B(a,b)B(a+b,c)=B(b,c)B(a,b+c).
\]

The second identity is exact 2-2 diagonal-flip coherence. For four half-rank pieces the Gamma-normalization ratio is `Gamma(1/2)^4/Gamma(2)=pi²`. Beta/Gamma by itself has **flat** associative gluing: neither a nontrivial surface holonomy nor any pi digit statistics follows from this identity. Standard background: NIST DLMF https://dlmf.nist.gov/5.12 and https://dlmf.nist.gov/5.5.

## 5. Full signed q=6 × carry × rank × phase seam tensor

For every n>=5, nonzero integer h, seed s, and literal carry c in {0,...,16}, define

\[
 \boxed{\mathcal A_{n,h,c}(s)=\sum_{j=0}^{n}q_n(j)
 \underbrace{[\chi(j+2)-\chi(j)]}_{\text{totient/cototient commutator}}
 \underbrace{A_j}_{\text{Gamma/harmonic/golden edge}}
 \underbrace{e^{i\pi(j+2)/8}}_{\text{declared Abel quarter-split twist}}
 1_{\kappa_{n+j}(s)=c}
 [z_{n+j}(h;s)-z_{n+1}(h;s)].}
\]

The full unprojected tensor M from §2 retains **all four** q=6 factorial cells even though the *oriented seam differential* only sees the off-diagonal cells (01) and (10). The terminal phase is **absolute**, not only a gauge-invariant difference, and literal carries are not averaged away before the certificate is formed. The difference from the anchor z_(n+1) deliberately removes the leading j=1 contribution, allowing j=3 to dominate the complete later-grade tail.

The complex twist is optional for the next norm inequality; it has unit magnitude. This explicitly tests its epistemic role: Gamma gives a real decreasing rank differential and a mathematically justified phase reference, but the 45-degree factor alone is **not load-bearing** for the nondecay theorem, much less for pi normality.

### THEOREM GTQ6-1: nonzero authentic limsup versus coherent counterseed

For every fixed nonzero integer h, the genuine s=0 original four-pole BBP orbit satisfies

\[
 \boxed{\limsup_{n\to\infty}\sum_{c=0}^{16}|\mathcal A_{n,h,c}(0)|
 \ge\frac{86984497}{13280710590}>0.}
\]

For the **same forcing** with s*=-pi/16 (mod 1),

\[
 \boxed{\sum_{c=0}^{16}|\mathcal A_{n,h,c}(s_*)|
 \le 2\pi|h|T_{n+1}\le\frac{2\pi|h|}{15(n+2)^2}\to0.}
\]

**PROOF with a genuinely all-n tail bound:**

1. Summing the carry bins recovers a single signed expression \(L_n=\sum_c\mathcal A_{n,h,c}\), and the triangle inequality gives \(\sum_c|\mathcal A_c|\ge|L_n|\). The inherited source TV certificate \(TV(q_n,w)\le22/n\) shows that \(L_n\) differs from its limiting Oily-filter version by at most 88/n: the summand has magnitude at most 2 (|d|<=1,A_j<1 whenever d!=0, and the complex phases are unit modulus). Thus the finite n correction vanishes.

2. The only nonzero d_j have j≡1 with d=-1 and j≡3 with d=+1 (mod6). The j=1 term is **exactly zero** because it uses anchor z_(n+1). The first remaining term is \(w_3 A_3 e^{5\pi i/8}(z_{n+3}-z_{n+1})\) with \(w_3=1/8\). Every other nonzero term has j>=7. The exact residual source mass is

\[
 W_1=\sum_{j\equiv1\ (6)}w_j=352/1323,\quad
 W_3=\sum_{j\equiv3\ (6)}w_j=172/1323,\]
\[
 \rho=(W_1-w_1)+(W_3-w_3)=223/10584.
\]

Since A_j decreases, the entire later signed tail has modulus at most \(2\rho A_7\), regardless of arbitrary phase alignments. This is a complete source-weighted hostile bound, not an independence assumption.

3. From the genuine BBP Green identity, for all n>=1,

\[
 U_{n+3}(0)-U_{n+1}(0)
 =255\cdot16^n\pi+(T_{n+1}-T_{n+3}).
\]

The tail correction tends to zero. **Elementary lacunary lemma:** for every irrational real beta and every integer b>=2,

\[
 \limsup_{n\to\infty}\|b^n\beta\|_{\mathbb R/\mathbb Z}\ge\frac1{b+1}.
\]

To prove it, suppose the limsup is <1/(b+1), and choose delta between them. Every sufficiently late circle iterate lies either in a low arc [0,delta] or a high arc [1-delta,1). Since b*delta<1-delta, a low iterate cannot jump to the high arc, and a high iterate cannot jump to low while staying within these two arcs. Each surviving arc distance from its endpoint multiplies by b at every step; the only indefinitely surviving endpoint orbit is exactly zero, forcing beta rational. Contradiction. No normality or distribution assumption is present.

Take b=16 and beta=255h*pi, irrational because pi is irrational. Therefore

\[
 \limsup_n |z_{n+3}(h;0)-z_{n+1}(h;0)|\ge2\sin(\pi/17).
\]

4. Using w3=1/8, A3>=11/30, A7<=19/90+(2/3)^10 (lambda<2/3), and concavity of sin on [0,pi/6], which yields sin(pi/17)>=3/17, obtain

\[
 \limsup_n|L_n(0)|\ge\frac14 A_3\sin(\pi/17)-2\rho A_7
 \ge\frac3{68}\frac{11}{30}
 -\frac{446}{10584}\left(\frac{19}{90}+\left(\frac23\right)^{10}\right)
 =\boxed{\frac{86984497}{13280710590}}>0.
\]

5. For s*=-pi/16, original series gives U_n(s*)=-T_n, all literal carries are **15** for n>=1, and |z_(n+j)-z_(n+1)|<=2pi|h|(T_(n+1)-T_(n+j)) for the only allowed nonzero j>=1. Summing the positive total source weight ≤1 and A_j≤1 gives the displayed O_h(n^-2) bound. QED.

**TRUTH BOUNDARY:** The lower bound proves a quantitative *limsup* noncoherence and a carry-resolved norm difference on the original selected source. It proves NEITHER a positive lower density of visits NOR \(\sum_{n\le N}z_n=o(N)\). A sparse exceptional sequence could satisfy the limsup constraint while still having normalized Fourier means near 1. It also does not distinguish the zero seed from every other irrational seed: the irrationality lemma is generic. Thus this is source-faithful progress on a weaker observable, not the missing normality rigidity theorem.

## 6. A genuine triangular lattice and its domain obstruction

The vertices \((n,j)\in\mathbb Z_{\ge1}\times\mathbb Z_{\ge0}\) embed into a Euclidean equilateral triangular lattice by

\[
 (n,j)\mapsto (n+j/2,\sqrt3\,j/2).
\]

For each unit grid cell, take the two triangles with vertices

\[
 [(n,j),(n+1,j),(n,j+1)],\qquad
 [(n+1,j),(n+1,j+1),(n,j+1)].
\]

Every interior edge is shared consistently by the two adjacent triangles, with no overlapping interiors or gaps; moving to adjacent cells propagates the same source integer clock and grade labels. Each vertex retains the source-forcing clock n, grade j, rank r=j+2, q6 primitive/cototient bits, and actual BBP carry/phase at index n+j. The two-step grade transport j->j+2 runs along two consecutive lattice edges. The q6 seam commutator is 6-periodic in j. The Beta identity above is a valid 2-2 flip law for any THREE positive rank parameters and gives a local coherence rule for regrouping Gamma subdivisions.

**Does this tile the whole Euclidean plane as the exact same SUCC source law?** Not canonically: actual time requires n>=1 and original Gamma ranks require r=j+2>0; carrying r=j+2 to all j in Z hits the poles of Gamma at nonpositive integers. An extension to a full Euclidean plane can be made by mirroring the quadrant or restarting ranks across a seam, but its reflection/renormalization is an **additional choice**, not inherited from BBP. So the rigorous statement is a coherent SUCC-labelled triangular quadrant/half-sheet, plus a geometrically possible but source-unproven full-plane extension.

A second natural tiling of a *hyperbolic* plane is the Farey tessellation: neighbors a/b,c/d have |ad-bc|=1, and mediants generate triangles under PSL(2,Z). This gives genuine arithmetic geometry but **no derived map** from Farey triangles to the authentic original four-pole zero-seeded carry. Sources: https://mathrepo.mis.mpg.de/farey/index.html and the earlier SUCC Farey–Gauss dossier.

## 7. Research tasks that might actually move pi-normality

- [ ] Seek a **density**, variance, or signed conditional carry estimate on the full q6 4-cell × literal-carry × complex-phase tensor, rather than limsup. The proven limsup cannot be promoted to a Weyl saving.
- [ ] Retain the exact original source first jet Q''(0)=-59 and finite Pascal weight corrections: the all-horizon limsup currently uses only their shared leading Gamma(2) packet tail and pi irrationality, not a uniquely four-pole cancellation property.
- [ ] Compare the sibling #371 exact marked Doob martingale with the q6 filtered seam, without conflating observation randomness and deterministic digit statistics.
- [ ] Test whether a nontrivial source-derived Galois/archimedean phase transport could turn the Gamma Abel 45-degree factor into a **nonflat** arithmetic holonomy. Beta gluing and rank shift phase alone remain flat and gauge-like.
- [ ] Formalize the elementary lacunary noncoherence lemma, exact q6 residue weights, and Gamma/Beta flip in Lean, keeping the selected normality target explicitly OPEN.

**Reproduction:** `python gamma_totient_tiling_probe.py -v` and `python independent_oracle.py`. The 14 standard-library tests and independent high-precision finite holdouts were performed locally; all remote exact-head, full inherited gates, Lean and CI checks remain pending.
