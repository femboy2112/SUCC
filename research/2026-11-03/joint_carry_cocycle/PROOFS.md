# OPERATION JOINT CARRY — original Gaussian/real source cocycle, exact 2-adic debt and real odd-cofactor interface

**Date:** 2026-11-03. **Authority:** exact paper derivations plus rational finite probes, not Lean or external proof referee. **Parent:** SUCC draft #483 at SHA `8383f69f5eb92eb037dde84f686cf3c77e043c2e`, inheriting canonical Gaussian/real algebra from #481, source-isometry from on-main `PI_DYADIC_SOURCE_ISOMETRY.md`, and the selected real Weyl/collision criteria of #475/#476. `PREREGISTRATION.md` was committed first at `2dc96f2116d3a6079a680300f7037a19456ca69c`. Do not modify original four signed poles, literal `U0=0`, original `K(t)`/source contracts, production, archives, CI or main. All root files here are research/test additions.

**Not proved:** any signed all-prefix original real Weyl saving, any original odd-prime real cofactor mixing, logarithmic-mesh collision energy `E_A=o(log m_A)`, base-16 normality of pi, RH or a physical speed/GR mechanism. **No independent-source novelty claim** for standard quotient groups, CRT, Baker, Kronecker-Weyl or general carry coboundaries.

## JCC-00. Actual selected arithmetic objects and notation

The immutable original source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n),\qquad n\ge1.
\]

The unique minimal rational Frobenius source object reconstructed by SUCC #481 is `A=Q(sqrt2) × Q(i)` with source-marked projectors `e_H,e_G`; **their Mellin moments**, NOT arbitrary hand-chosen phases, are

\[
\boxed{r_H(n)=-\frac1{4n-3}-\frac1{4(2n-1)}-\frac1{4(4n-1)}-\frac1{32n}},\qquad
r_G(n)=r(n)-r_H(n).
\]

Let `U^H_0=U^G_0=0`, `U^a_n=16U^a_(n-1)+r_a(n)`. Then for ALL n, `U_n=U^H_n+U^G_n` exactly as unwrapped rationals. These n are ORIGINAL recurrence steps; do **not** conflate with the coefficient index of the distinct `K(t)` rational transfer, nor with its eight-coefficient scalar return.

For rational x let `q2(x)∈Q/Z` be the representative in `[0,1)` of its **2-primary principal fraction**: if reduced `x=a/(2^d b)` with b odd, set `q2(x)=[a b^-1]_(mod 2^d)/2^d`; if d=0 put zero. This represents the quotient `Q2/Z2` on rational inputs. It is usually NOT the ordinary real fractional part `{x}`. Write `depth2(x)=max(0,-v2(x))`. The additive quotient and its integer arithmetic are classical.

Define `o(x)={x-q2(x)}`. It has odd reduced denominator and agrees, as a real-circle phase, with the **sum of all odd-primary principal fractions**. This is the classical CRT/Tate finite-phase statement already implemented in on-main `finite_adelic_character_bridge.py` (standard sign convention here is real-positive; Tate finite character uses the opposite sign).

## JCC-01. Exact parity/harmonic principal-source cocycle — SOURCE-SPECIFIC, ALL n

For every integer n>=1, the two middle fractions in `r_H` have residues with inverse odd denominators. Modulo 4:

- If n odd, `2n−1≡1`, `4n−1≡3`, so `(2n−1)^(-1)+(4n−1)^(-1)≡1+3=0` and their sum divided by 4 is 2-integral.
- If n even, `2n−1≡3`, `4n−1≡3`, so the two inverses add to 6≡2 mod4; their *negative* quarter-sum is a half-unit modulo Z2.

The first term `−1/(4n−3)` is always 2-integral. Thus

\[
\boxed{q_2(r_H(n))=q_2\bigl(-1/(32n)+\tfrac12\mathbf1_{2\mid n}\bigr),\quad q_2(r_G(n))=-q_2(r_H(n)).}
\]

Introduce the exact rational weighted-harmonic state

\[
W_0=0,\qquad W_n=16W_{n-1}+1/n=\sum_{j=1}^n 16^{n-j}/j.
\]

After evolving the H recurrence, any *earlier* half-unit is multiplied by `16^(n-j)` and becomes 2-integral; only the current parity half-unit remains. Therefore **for every original source n>=1**:

\[
\boxed{q_2(U^H_n)=q_2\left(-W_n/32+\frac{\mathbf1_{2\mid n}}2\right),\quad q_2(U^G_n)=-q_2(U^H_n).}\tag{JCC-1}
\]

This is a closed source-specific two-channel local carry law, not a statement about real histogram or probabilistic independence. The finite weighted-harmonic generator formally has rational generating function `Σ W_n z^n = -log(1-z)/(1-16z)` on |z|<1/16, but the **2-adic local statement is finite at each original integer index** and requires no analytic continuation or zeta zeros.

## JCC-02. Sharp all-time upper bound and short causal-memory theorem

From the original source formulas (#481), for every j>=1,

\[
v_2(r_H(j))=v_2(r_G(j))=-5-v_2(j).
\]

For 1<=j<=n, `v2(j)<=floor(log2 n)`. Consequently every term `16^(n-j) r_H(j)` belongs to `2^(-B_n) Z2` for

\[
\boxed{B_n=5+\lfloor\log_2 n\rfloor.}
\]

The same holds for G and for their full states. Thus

\[
\boxed{depth_2(U_n^H)=depth_2(U_n^G)\le B_n}\tag{JCC-2}
\]

(the equality of H/G depth holds because the glued U belongs to Z2; if both are integral the depth is zero). Now put `L_n=min(n,ceil(B_n/4))`. For any lookback d>=L_n, even the worst possible source term satisfies `v2(16^d r_H(n-d))>=4d-B_n>=0`. Hence the complete 2-primary source state depends only on the LAST `L_n` source injections:

\[
\boxed{q_2(U_n^H)=q_2\left(\sum_{d=0}^{L_n-1}16^d r_H(n-d)\right).}\tag{JCC-3}
\]

Likewise for G. This is an exact logarithmic-memory representation of the local defect for ANY original source time n. It does **not** say the unwrapped real state has logarithmic memory; real carries can retain much more.

## JCC-03. Exact primitive torsion at EVERY power of two

Fix k>=1 and n=2^k. In `W_n`, the last summand is `1/n`, the preceding is `16/(n−1)`, and for d>=2 the term at j=n−d has valuation `4d-v2(n-d)=4d-v2(d)>=7`. Thus

\[
W_{2^k}\equiv1/2^k+16/(2^k-1)\equiv1/2^k+16\pmod{32\mathbb Z_2}.
\]

The current time is even, so (JCC-1) cancels the `−16/32` against the parity `+1/2`. This proves, for **ALL k>=1**, the exact source-specific identity

\[
\boxed{q_2(U^H_{2^k})=-2^{-k-5},\quad q_2(U^G_{2^k})=+2^{-k-5}.}\tag{JCC-4}
\]

The displayed negatives are quotient elements (represented by `1−2^(-k-5)` in `[0,1)`). Both have **exact additive order `2^(k+5)`** in `Q2/Z2`. Hence JCC-2 is **sharp** at every `2^k` and no bounded-torsion finite local defect register can hold the complete original two-channel source at all such times. Their principal-phase characters are a pair of inverse primitive `2^(k+5)`-th roots; their product is exactly 1, not a real Weyl cancellation estimate.

### JCC-03b. Source-specific persistent debt window after every power of two

For k>=1 and 0<=d with `5d<k`, set n=2^k+d. In the **unwrapped zero-seeded** channel state, the contribution born at j=2^k has valuation `4d−5−k`. Every earlier j<2^k has v2(j)<=k-1 and at least d+1 powers of 16, so valuation at least `4d−k`, strictly larger. Every later j=2^k+e, 1<=e<=d, has v2(j)=v2(e)<=floor(log2 d)<=d; its contribution has valuation at least `-5-d`, strictly larger than `4d−5−k` because `5d<k`. The 2-adic ultrametric equality for a **unique** minimum now gives

\[
\boxed{v_2(U^H_{2^k+d})=v_2(U^G_{2^k+d})=4d-5-k,\quad 0\le d,\ 5d<k.}\tag{JCC-5}
\]

The G equality follows from exact integrality of the glued state and negativity of the displayed H valuation. Thus each anchor generates an unbounded family of consecutive source times with explicit complementary 2-primary carry debt, decaying by EXACTLY four valuation bits per step until the certified window ends. No source random model or finite extrapolation is used.

## JCC-04. The missing all-place arrow becomes an exact ODD cofactor formula

By elementary CRT for rational principal parts, `x mod1=(q2(x)+o(x)) mod1`. For original zero-seeded channels, `q2(U_H)+q2(U_G)=0` in Q/Z. Therefore for ALL n and all integer h,

\[
\boxed{e(hU_n)=e(h\,o(U_n^H))\,e(h\,o(U_n^G)).}\tag{JCC-6}
\]

This is a **selected** real character identity retaining complete odd-prime principal fractions, including 3,5 and every generic denominator prime. It does not permit replacing either factor by a Galois average or independent random variable. Importantly the p=2 principal character cancels EXACTLY, so a bound based only on that local interference is insufficient: the entire real Fourier problem survives in the selected odd complementary phases.

The conventional global finite Tate character has opposite sign, so do not identify `e(q2(x))` with the positive Tate finite phase without stating the sign transport. The full source case is a rational diagonal of the standard adelic product formula, not an assertion that the source is statistically generic.

## JCC-05. Exact REAL binary carry vs odd-cofactor boundary identity

Use canonical representatives `a_n=o(U_n^H), b_n=o(U_n^G), delta_n=q2(U_n^G)` in `[0,1)`. Then `q2(U_H)=(-delta_n) mod1`. Define **two separately typed integer carries**

\[
\kappa_n=\lfloor\{U_n^H\}+\{U_n^G\}\rfloor\in\{0,1\},\quad
\kappa_n^{odd}=\lfloor a_n+b_n\rfloor\in\{0,1\}.
\]

Their fractional channel states are

\[
\{U_n^H\}=a_n-\delta_n+\mathbf1_{a_n<\delta_n},\qquad
\{U_n^G\}=b_n+\delta_n-\mathbf1_{b_n\ge1-\delta_n}.
\]

These are **exact** identities, with the strict/lax endpoint orientation forced by the conventional half-open `[0,1)` circle representative. Adding and taking floors proves

\[
\boxed{\kappa_n-\kappa_n^{odd}
=\mathbf1_{a_n<\delta_n}-\mathbf1_{b_n\ge1-\delta_n}.}\tag{JCC-7}
\]

In particular

\[
\boxed{|\kappa_n-\kappa_n^{odd}|
\le \mathbf1_{a_n<\delta_n}+\mathbf1_{b_n\ge1-\delta_n}.}\tag{JCC-8}
\]

This is the desired **actual selected real-carry interface** between local principal parts and real/fractional odd cofactors. It is exact but **not** a distribution theorem. At `n=2^k`, `delta_n=1/(32n)`, so the boundary conditions are exceptionally thin. They concern only a zero-density anchor family, and a thin interval does not imply a rare event for one selected orbit without a nonconcentration theorem.

## JCC-06. Original causal REAL carry discrepancy is one binary coboundary

For the canonical fractional states `x_n^a={U_n^a}`, let

\[
c_n^a=\lfloor16x_{n-1}^a+r_a(n)\rfloor,\quad
x_n^a=16x_{n-1}^a+r_a(n)-c_n^a
\]

for a=H,G. Let `y_n={U_n}`, `c_n=floor(16y_(n-1)+r(n))` be the ACTUAL source local integer carry. Since `y_n=x_n^H+x_n^G-kappa_n` and `y_(n-1)=x_(n-1)^H+x_(n-1)^G-kappa_(n-1)`, direct substitution gives

\[
\boxed{c_n-c_n^H-c_n^G=\kappa_n-16\kappa_{n-1}\in\{-16,-15,0,1\}.}\tag{JCC-9}
\]

With **literal zero seed** `kappa_0=0`, the weighted temporal sum telescopes, for ALL n>=1:

\[
\boxed{\sum_{j=1}^{n}16^{n-j}(c_j-c_j^H-c_j^G)=\kappa_n\in\{0,1\}.}\tag{JCC-10}
\]

This is a UNIFORM all-time joint-carry discrepancy inequality. The seemingly exponentially growing sum of discrepancies is exactly a single binary bit after gluing. This is a general coboundary fact specialized to the authentic canonical zero-seeded source—not a new statistical Weyl saving. Ordinary **integer lifts are essential**: replacing `U_n` with only its real fractional part changes its 2-adic value. At the first authentic source time, `U_1=47/15` has odd 2-adic residue while `{U_1}=2/15` has even residue; the integral carry `floor(U_1)=3` cannot be discarded.

## JCC-07. Exact scaled precision tax for legal gluing

Let B>=0 and suppose x,y∈2^(-B) Z2 with x+y∈Z2. To compute the result `(x+y) mod 2^k` from **separate scaled integral residues** `2^B*x` and `2^B*y`, knowledge modulo `2^(B+k)` is sufficient: add in that modulus and divide by `2^B` after integrality. It is **universally sharp**: pairs

\[
(x_0,y_0)=(-2^{-B},2^{-B}),\quad
(x_1,y_1)=(2^{k-1}-2^{-B},2^{-B})
\]

have the same separate scaled residues mod `2^(B+k-1)` but their glued integral outputs differ by `2^(k-1)` mod `2^k`. The two channel principal defects are identical even when B>0. Therefore an observer needs an **extra B precision bits** to reconstruct the glued integral result from arbitrary isolated scaled states, even with complementary 2-primary classes.

For our ACTUAL source, JCC-2 permits `B=B_n<=5+floor(log2 n)`, and the source anchors make that depth sharp. This is a worst-case separate-state reconstruction cost, NOT a theorem that complete authenticated original source data cannot exploit extra structure to do better. Moreover, reconstructing the 2-adic result remains a different problem from decoding the selected REAL phase.

## JCC-08. Decisive adversarial controls: carry agreement does NOT imply mixing

**Coherent odd-prime counterfeit:** For ANY D>=4 choose `eps=2^(-D)` and rational channel states

\[
H^*=-eps+2/5,\qquad G^*=eps+2/5.
\]

Then `q2(H*)=-eps`, `q2(G*)=+eps`, and BOTH odd cofactor phases equal `2/5`. The indicators in JCC-7 are ZERO because `eps<=1/16<2/5<1-eps`, yet the glued real phase is **identically 4/5**. Set D=k+5 at all `2^k` to reproduce the ENTIRE original anchor principal-part law. This changes the source; it refutes only the conjectural inference “exact dyadic anchor cancellation plus zero real/odd carry anomaly implies real Weyl saving.” It is not a counterexample to original source law.

**Odd-place gauge:** Changing `(H,G)` to `(H+1/5,G-1/5)` preserves the exact total and their 2-primary principal classes but can change `kappa_real`. For example `(H,G)=(-1/32,1/32+1/5)` has real carry 1, while the gauge-moved pair has carry 0. This gauge does NOT preserve the authentic canonical source channel readout; the source labels matter. It shows that the binary cross-channel carry is not an unmarked physical observable under arbitrary zero-sum sector redistribution.

**Inadequate truncated state:** The actual first original state has `U_1=47/15` but `{U_1}=2/15`; mod 4 their 2-adic residues differ. Any use of ordinary real fractional parts in place of unwrapped states for local residue reconstruction must explicitly reinstate literal carries.

**No false source independence:** The real characters `e(hU_H)e(hU_G)` are sampled at the SAME original source time n. JCC-01..10 do not prove either factor mixes, their joint sum is Haar, or the odd-prime cofiber has a large sieve saving. A family of algebraically complementary 2-adic states can carry a perfectly coherent real character.

## JCC-09. Classical source-channel irrationality, a useful but insufficient independent lamp

The completed real channel constants are inherited exactly from source integrals:

\[
\alpha_H=\sum_{n>=1}16^{-n}r_H(n)=-\log2/8,\quad
\alpha_G=\sum_{n>=1}16^{-n}r_G(n)=\pi/16+\log2/8.
\]

Baker's classical linear-forms theorem establishes that `1,log2,i*pi` are linearly independent over algebraic numbers: the two chosen logarithms `log 2` and `log(-1)=i*pi` are Q-linearly independent (one real, one imaginary), so the theorem applies. Hence `1,alpha_H,alpha_G` are Q-linearly independent. Kronecker's classical theorem then gives equidistribution of the **additive-time torus rotation** `n*(alpha_H,alpha_G)`; this is NOT the SUCC/BBP **power-16 orbit** `(16^n*alpha_H,16^n*alpha_G)`, whose selected distribution remains unverified. Even total irrationality does not imply genericity under ×16: an explicit nonnormal Liouville point `lambda=sum_{j>=1}16^(-j!)`, paired with `sqrt2*lambda`, is Q-independent with 1 but its first coordinate is nonnormal.

Classical references: A. Baker, *Linear forms in the logarithms of algebraic numbers (III)*, Mathematika 14 (1967), 220–228; and Cambridge University Press https://www.cambridge.org/core/journals/mathematika/article/abs/linear-forms-in-the-logarithms-of-algebraic-numbers-iii/C3A7D8C6F454E237D6A3FBAD8DBD006D. This is an imported theorem, NOT an original proof or a π normality route.

## JCC-10. Exact missing inequality and decision ledger

For dyadic `A=2^j`, explicit mesh `m_A=max(2,2^floor(log2 j))≈log A`, and ORIGINAL real phases `{U_n}`, parent #476 proved the conditional sufficient estimate

\[
E_{A,m_A}=(m_A/A^2)\sum_{r<m_A}\#\{A\le n<2A:\lfloor m_A\{U_n\}\rfloor=r\}^2=o(\log m_A)
\Longrightarrow \pi\text{ normal base 16}.
\]

**We did NOT prove the premise.** JCC-04 shows its **entire selected real character** lies in the combined odd-primary phases after the exact dyadic gluing. To advance beyond source-map reconstruction, one must prove a nontrivial ORIGINAL time-correlated odd-cofactor near-pair/mixed-character saving on an unbounded family, not merely JCC-05's boundary identity or JCC-06's bounded integer carry. The exact prime-clock p-free cofactor of #474 is an available but currently unbounded selected-real variable. Target its distribution, preserving all primes, zero boundary, actual time order and real integer lifts.

**Claim ledger:**

| Claim | Status / boundary |
|---|---|
| JCC-01 parity-weighted harmonic cocycle | DISCLOSED paper exact, all n, source-specific; no real mean |
| JCC-02 depth and logarithmic local memory | DISCLOSED paper exact all n |
| JCC-03/03b anchor and growing debt window | DISCLOSED paper all k/d, no real mixing |
| JCC-04 all-place odd-cofactor identity | DISCLOSED source specialization of classical CRT/Tate; no Fourier saving |
| JCC-05 actual real carry boundary indicators | DISCLOSED exact; event counts UNVERIFIED |
| JCC-06 original zero-seeded carry coboundary | DISCLOSED exact; general algebra, not mixing |
| JCC-07 additional scaled precision bits | DISCLOSED worst-case reconstruction bound; real decoding unavailable |
| JCC-08 universal false-Haar controls | REFUTED local-to-real/low-carry shortcut with rational witnesses |
| JCC-09 Baker/Kronecker arithmetic nonresonance | CLASSICAL imported + source substitution; power-16 distribution UNVERIFIED |
| JCC-10 original selected odd-prime/carry saving | **UNVERIFIED / OPEN**; π base-16 normality **OPEN** |

The exact tests and predeclared new finite receipts exercise the statements but **never extend** their quantifiers. Same-reasoner alternate oracles do not qualify as blind independent mathematical corroboration.
