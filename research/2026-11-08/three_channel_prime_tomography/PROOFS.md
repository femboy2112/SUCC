# Three-channel prime-clock tomography: a four-stage arithmetic source with a stratified Fourier limit

**2026-11-08; research-only, additively stacked on draft #552.** The imported four-pole BBP source, literal zero seed, provenance and historical theorem names are unchanged. **Base-16 normality of π remains OPEN.** `PAPER-PROVED` here means an explicitly checkable mathematical argument, NOT Lean certification, external peer review, or a proof of a signed zero-seed estimate.

## 0. Actual sources, scopes and the old result we do not claim as new

For integer n≥1, put a_n=8n−7 and

\[
 r(n)=\frac4{a_n}-\frac2{a_n+3}-\frac1{a_n+4}-\frac1{a_n+5},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Write the **exact** positive three-channel decomposition

\[
 f_3(n)=2\left(\frac1{a_n}-\frac1{a_n+3}\right),\quad
 f_4(n)=\frac1{a_n}-\frac1{a_n+4},\quad
 f_5(n)=\frac1{a_n}-\frac1{a_n+5},\quad r=f_3+f_4+f_5.
\]

Define the genuine zero-seeded **partial-source histories** `V_{d,0}=0`, `V_{d,n}=16 V_{d,n−1}+f_d(n)` for d=3,4,5. Their sum equals U_n exactly at every finite n, and no alternative digit source has been substituted. The instantaneous three-channel **positive Laplace Gram** of #552 is a different object from the **prime-character phase Gram** constructed here.

**Inherited, not claimed as a novel theorem:** #497's Prime–Frobenius PF-01–04 already derives every original four-pole p-event and its scalar rational normalizers (including 4,7/2,33/10,47/15 at p≡1 mod8) and the full-shell self-shadow. #499 independently gives the all-eight-tap Klein-four source action. The contributions below are the three-channel *lift*, explicit Fourier stratification, quantitative 3×3 phase-frame limit, and a fully typed bridge to the unsolved signed complement.

## TCP-01. Channel-resolved exact prime-Frobenius shell (PAPER-PROVED; exact oracle)

Fix a **genuine prime** p=8k+1>5, and an integer r with 0≤r<k. Consider the complete shell

\[
 b_r=k+1+rp,\qquad J_{p,r}=\{b_r,b_r+1,\ldots,b_r+p-1\}.
\]

For all n≤b_r+p−1, every source denominator is strictly less than p²: indeed the largest is `8n−2 ≤ (8r+9)p−3 ≤ p²−3`. Thus p times each partial state V_{d,n} is p-integral. Let

\[
 C_{d,p}(n):=pV_{d,n}\pmod p\ \in\mathbb F_p,\qquad
 \mathbf C_p(n)=(C_{3,p},C_{4,p},C_{5,p}).
\]

The sole new p-divisible denominators within shell r occur at the four actual time stamps

\[
 b_r,\quad b_r+3k,\quad b_r+4k,\quad b_r+5k.
\]

They are respectively `(a_j)=(8r+1)p`, `(a_j+3)=(8r+4)p`, `(a_j+4)=(8r+5)p`, `(a_j+5)=(8r+6)p`. Their vector injections into **p times the three histories** are

\[
 \frac{(2,1,1)}{8r+1},\quad
 \frac{(-2,0,0)}{8r+4},\quad
 \frac{(0,-1,0)}{8r+5},\quad
 \frac{(0,0,-1)}{8r+6}.
\]

All fractions are ordinary rationals with p-unit denominators in the given range. Define exact rational stage vectors

\[
 \mathbf v_{r,s}=16\mathbf V_r+\sum_{j=1}^s\frac{\mathbf b_j}{8r+q_j},\quad
 (q_j)=(1,4,5,6),\quad
 (\mathbf b_j)=((2,1,1),(-2,0,0),(0,-1,0),(0,0,-1)).
\]

Let t=n−b_r; stage index s(t) equals 1 on 0≤t<3k, 2 on 3k≤t<4k, 3 on 4k≤t<5k, and 4 on 5k≤t≤8k. Then the exact **original-state** congruence is

\[
 \boxed{\mathbf C_p(b_r+t)=16^t\mathbf v_{r,s(t)}\pmod p.}\tag{TCP1}
\]

**Proof.** A source fraction contributes to pV modulo p only when its denominator has one p factor; then it injects its integer tap weight divided by the remaining factor. Event arithmetic follows by solving `8j−7+d=mp` and using p≡1 mod8. Between events, multiply by 16. Euler's criterion gives `16^k=2^((p−1)/2)=1 mod p`. Fermat gives `16^p=16 mod p`; consequently the entire contribution from earlier completed shells at the beginning of shell r is `16 V_r` in the rational shadow. For each new event the `16^(-t_event)` factor is 1 because every offset is a multiple of k. This proves TCP1 by induction on r and within each shell. At stage four,

\[
 \boxed{\mathbf v_{r,4}=16\mathbf V_r+\mathbf f(r+1)=\mathbf V_{r+1}} \tag{TCP2}
\]

as an equality in Q³, not merely modulo p. This explicitly lifts inherited #497 PF-03. **Do not** assert an unwrapped real equality `pV_n=16^t V_{r+1}`: it is a finite-field residue statement.

At r=0 the successive vectors are exactly

\[
 \boxed{(2,1,1),\ (3/2,1,1),\ (3/2,4/5,1),\ (3/2,4/5,5/6).}\tag{TCP3}
\]

Their sums are 4,7/2,33/10,47/15, reproducing the known scalar normalizers. Each complete shell contains exactly 3k+k+k+(3k+1)=p consecutive times.

## TCP-02. Genuine rank growth (PAPER-PROVED)

The first injection spans one line in the three-channel space. The first, second and third event injection vectors span all three dimensions: their row determinant is

\[
 \det\begin{pmatrix}
 2&1&1\\ -2/(8r+4)&0&0\\ 0&-1/(8r+5)&0
 \end{pmatrix}
 =\frac{2}{(8r+4)(8r+5)}\ne0.\tag{TCP4}
\]

Thus the chronological *source-response* rank progresses 1→2→3 after the first three events. The fourth event closes the original source pulse. This is a three-dimensional **deterministic source-labelled representation**, not three independent random prime channels or proof of nine independent information bits.

## TCP-03. Exact four-stage Fourier law and the resonance-plane lattice (PAPER-PROVED)

For `e_p(c)=exp(2πi c/p)`, let m=ord_p(16), which divides k because 16^k=1 modp. Put

\[
 \mathcal S_p(c)=\frac1m\sum_{u=0}^{m-1}e_p(c16^u),\quad
 \delta_p=\max_{c\ne0}|\mathcal S_p(c)|,\quad \mathcal S_p(0)=1.
\]

For any integer mode `t=(t_3,t_4,t_5)` and integer h, define the **entire original shell** signed mode

\[
 \widehat\nu_{p,r,h}(\mathbf t)=\frac1p\sum_{n\in J_{p,r}}e_p\!\left(h\mathbf t\cdot\mathbf C_p(n)\right).
\]

Writing `c_s=h t·v_{r,s} mod p`, the exact identity is

\[
 \boxed{
 \widehat\nu_{p,r,h}(\mathbf t)=\frac{k}{p}\Bigl[3\mathcal S_p(c_1)+\mathcal S_p(c_2)+\mathcal S_p(c_3)+3\mathcal S_p(c_4)\Bigr]+\frac1p e_p(c_4).}
 \tag{TCP5}
\]

Proof: each of the first three stages consists of 3k,k,k successive times, and the last consists of 3k full times plus its endpoint. All starts are integer multiples of k, and `m|k`, so every complete stage is an integer number of identical multiplicative subgroup cycles; the extra endpoint has `16^(8k)=1 modp`. This is an exact histogram equality before evaluating any trigonometric function. It has been checked against an independent four-pole term-by-term modular recurrence, not just an implementation of the same stage formula.

Define the finite **resonant mass**

\[
 \rho_{p,r,h}(\mathbf t)=\frac{k}{p}\bigl(3\mathbf1_{c_1=0}+\mathbf1_{c_2=0}+\mathbf1_{c_3=0}+3\mathbf1_{c_4=0}\bigr).
\]

Then uniformly over *all* integer modes, even p-dependent ones,

\[
 \boxed{|\widehat\nu_{p,r,h}(\mathbf t)-\rho_{p,r,h}(\mathbf t)|\le\delta_p+1/p.}\tag{TCP6}
\]

The `1/p` term is the genuine incomplete endpoint; dropping it is wrong. This is a quantitative structural reduction, not an imported saving: `δ_p→0` needs an independent subgroup exponential-sum theorem (the BK/CP imports and strong-prime selectors in #544 are suitable under their exact stated order hypotheses).

For the **first** shell r=0 and fixed nonzero h, every fixed rational nonzero `t·v_{0,s}` is p-nonzero for all sufficiently large p; hence, along any p≡1 mod8 sequence with δ_p→0,

\[
 \boxed{\widehat\nu_{p,0,h}(\mathbf t)\to
 \frac38\mathbf1_{2t_3+t_4+t_5=0}
 +\frac18\mathbf1_{3t_3+2t_4+2t_5=0}
 +\frac18\mathbf1_{15t_3+8t_4+10t_5=0}
 +\frac38\mathbf1_{45t_3+24t_4+25t_5=0}.}\tag{TCP7}
\]

**Full law, not just a scalar limit.** The phase triple `(e_p(C3),e_p(C4),e_p(C5))` converges weakly in T³ to the mixture of Haar probabilities on the four one-dimensional subtori generated by the primitive directions `(2,1,1),(3,2,2),(15,8,10),(45,24,25)`, in weights `(3,1,1,3)/8`. This follows by checking *every fixed integer Fourier character* via TCP7 and applying density of trigonometric polynomials in continuous functions on compact T³. The limiting three-channel law is emphatically **not** Haar on T³. Its nontrivial transverse resonances are exact source information, not an independence statement.

## TCP-04. A nondegenerate prime-phase 3×3 Gram (PAPER-PROVED conditionally on δ_p→0)

Let `z_d(n)=e_p(h C_{d,p}(n))` for d=3,4,5 and h nonzero modp. Form the positive Hermitian 3×3 **chronological character Gram**

\[
 M_{de}(p)=\frac1p\sum_{n\in J_{p,0}}z_d(n)\overline{z_e(n)}.
\]

Apply TCP5 with `t=e_d−e_e`. The first two stages have **identical** channel-4 and channel-5 local phases; the last two resolve them. All other off-diagonal pair modes are nonresonant at all four stages for every p≡1 mod8, p>5. Consequently, putting `c_p=4k/p=(p−1)/(2p)`,

\[
 \boxed{\left|M_{34}\right|,\left|M_{35}\right|,\left|M_{45}-c_p\right|\le\delta_p+1/p,\quad M_{dd}=1.}\tag{TCP8}
\]

Therefore `M(p)` approaches

\[
 \boxed{M_\infty=\begin{pmatrix}1&0&0\\0&1&1/2\\0&1/2&1\end{pmatrix},\quad
 \operatorname{spec}(M_\infty)=\{3/2,1,1/2\}.}\tag{TCP9}
\]

For a **finite**, unconditional comparison (with measured δ_p left as a parameter), the difference from `M_0(p)` having off-diagonal entry `c_p` only in its (4,5) pair has Frobenius norm ≤sqrt(6)(δ_p+1/p); Hermitian eigenvalue perturbation yields

\[
 \boxed{\lambda_{\min}(M(p))\ge \frac{p+1}{2p}-\sqrt6\,(\delta_p+1/p).}\tag{TCP10}
\]

This bound can be negative for small p and is then simply noninformative. Under δ_p→0 it certifies a **uniform asymptotic lower frame bound 1/2**. This contrasts sharply with the positive common-L² three-channel Gram of #552 whose unnormalized determinant decays as 115200/a^15. Different carriers/observables mean no direct contradiction and no free transfer between them.

## TCP-05. A typed conditional complementary-phase budget (PROVED REDUCTION, arithmetic premise OPEN)

For n in the first p-shell, define the **genuine original rational state** `U_n=sum_d V_{d,n}` and its p-principal circle part

\[
 a_n=e_p\Bigl(h\sum_d C_{d,p}(n)\Bigr),\quad
 b_n=e\left(h\left[U_n-\frac{(\sum_d C_{d,p}(n)\bmod p)}p\right]\right).
\]

Then `a_n b_n=e(h U_n)` **exactly**. For any finite trigonometric candidate `B_n=Σ_{t in T}c_t e_p(h t·C_p(n))`, define the observable signed model error `η=(1/p)Σ_{n∈J}|b_n−B_n|`. Applying TCP6 to `a_n B_n` gives the fully quantitative **source-shell** criterion

\[
 \boxed{\left|\frac1p\sum_{n\in J_{p,0}}e(hU_n)\right|
 \le\eta+\sum_{\mathbf t\in T}|c_{\mathbf t}|\left[\rho_{p,0,h}(\mathbf1+\mathbf t)+\delta_p+\frac1p\right].}\tag{TCP11}
\]

For fixed Fourier modes in T, the four nonzero-mass **dangerous complement planes** are

\[
 \begin{array}{rcl}
 2t_3+t_4+t_5&=&-4,\\
 3t_3+2t_4+2t_5&=&-7,\\
 15t_3+8t_4+10t_5&=&-33,\\
 45t_3+24t_4+25t_5&=&-94.
 \end{array}\tag{TCP12}
\]

The coherent antagonist is `t=(-1,-1,-1)`: it sits on **all four planes**, with exact `a_n B_n=1`. Thus even a positive, uniformly conditioned three-channel *prime-phase* Gram does not prevent the complementary phase from reintroducing full real coherence. Another danger: any purported model with coefficients depending on p needs **finite mod-p** `ρ` rather than the limiting rational planes, since exceptional modular resonances may appear. **No small-η or small-resonant-mass model for the authentic zero-seed complementary phases has been proved**. TCP11 is a nontrivial explicit resonance *classification* and a conditional route; it does not establish selected signed decay nor imply base-16 π normality from its existing hypotheses. A vanishing estimate on only these prime shells is also insufficient to cover all integer epochs without a new gluing theorem.

## TCP-06. Hostile controls and source-map separation

1. **Rational changed seed.** Replacing U0 by a rational `s` with p∤den(s) changes the REAL phases by e(h16^n s) but does NOT change `p U_n modp`: `p16^n s=0 modp`. A prime-phase-only observer is seed-blind on this class. The coherent irrational counterseed `s*=-π/16` cannot itself be called a p-integral rational state, but taking the complement `b_n=conjugate(a_n)` as a *virtual* control makes full mean 1. Neither case refutes original-π normality; both refute phase-blind inferences.
2. **Source-matched Gamma mutant.** Let `Q_ε(x)=Q(x)+ε exp(-6x)(1-exp(-x))^3`, ε rational nonzero (and positive for a positive density). `Q_ε(0)=Q(0)`, `Q_ε'(0)=Q'(0)`, `Q_ε''(0)=Q''(0)`. Its new Laplace forcing adds `ε[1/(a+6)-3/(a+7)+3/(a+8)-1/(a+9)]`. At time n=k and p=8k+1, the original source has not yet acquired ANY p-pole, but the mutant injects `+3ε/p` through its `(a+8)=p` denominator. Thus the source can be distinguished **before the original first birth** despite matching the leading Gamma jets. The stage taxonomy is authentically four-pole, not forced by shape-two Gamma alone.
3. **No scalar-Gamma rescue.** The `1/9` Poisson antipodal bound survives a two-pole source, while the four-stage resonance normals, rank growth and transverse p-phase Gram do not survive unaltered. The former is universal boundary geometry; the latter is actual source chronology.
4. **No false real-bound promotion.** The old #552 source Gram, new finite p-character Gram, #544 local prime/chirp cancellation and the selected real Weyl covariance have different types. The conclusion that the first three are calculable does NOT pay the last one. Do not erase signed cross-terms or make any seed-blind proof claim.
5. **No claim for p² poles.** At the next shell r=k the first event denominator is p²; `p V mod p` need not exist. Extrapolating TCP1–12 beyond r<k is INVALID.

## TCP-07. Status, provenance and decisive next lamp

- TCP-01/02/03 and finite inequalities TCP-06/08/10/11: **PAPER-PROVED** elementary exact arithmetic, with stated p and shell boundaries.
- Weak limit and asymptotic spectrum TCP-07/09: **PROVED CONDITIONAL** on `δ_p→0` along the declared prime sequence. This is an explicit subgroup cancellation premise, supplied on suitable prime subsequences by classical Bourgain–Konyagin/Cochrane–Pinner estimates as audited in #544, subject to their order selectors; not an unconditional all-prime bound.
- Direct source oracle, complete exact Fourier residue-count histograms, fractional stage vectors, small-p numerical Gram tests and hostile controls: **OBSERVED FINITE** with executable tests. Numerical complex characters are not interval certificates.
- Original-zero complemented Fourier approximation with `η→0` and no dangerous resonances: **OPEN/UNVERIFIED**. The original zero-seed signed covariance, π normality and RH: **OPEN**.

The most discriminating next proof would control the original **real complement** against the four resonance planes, from the literal zero seed and full carries, for every relevant growing prime clock, with a genuine Fourier-support and approximation-error theorem. This would then need a verified all-integer-epoch gluing argument to give base-16 normality. Existing #544 resonant-polynomial and signed-lag theorems are sibling controls, not implicit proofs of this new assumption.
