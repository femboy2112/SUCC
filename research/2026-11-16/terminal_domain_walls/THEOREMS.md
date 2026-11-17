# Operation TERMINAL WALLS — the Virtual Zero-Field Norm, Two-Boundary Symbolics, and an Exact BBP Source Crucible

**Date:** 2026-11-16  
**Primary target:** Main XXVI's weakest open hexadecimal π rung R0.  
**Author's originating imperative:** *One original source. One finite rational endpoint for each shell. A family of backward computational probes. A precise distance from the zero-phase reference. Prove that the norm cannot collapse to zero on arbitrarily late shells, and R0 follows.*  
**Scope:** new-to-SUCC synthesis of elementary radix/conditional-observation mathematics and an explicit all-prefix counterfeit. Classical ingredients are not claimed as academic novelty. **R0, π-normality, the all-B density and RH remain OPEN.**

This is an independently reviewable companion to [draft PR #657](https://github.com/femboy2112/SUCC/pull/657), based on immutable Main XXVI main commit 81be6b897ae980b801a3b9de9e22ef81e8360bfb. No imported sources, literal zero seed, historical files, provenance, or production paths are changed.

## 1. The authenticated BBP object and terminal norm

Retain the **exact** four signed poles and zero seed:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
By the imported classical BBP identity, \(x=\pi/16\), \(P_m=\sum_{j=1}^m16^{-j}r(j)\), \(U_m=16^m P_m\), \(16^m x=U_m+T_m\), and \(0<T_m<r(m+1)/15\). For each integer B≥1 set \(m=2B\) and
\[
\boxed{\mathcal R_B
=\frac1B\sum_{k=1}^{B}\left\|\frac{U_{2B}}{16^k}\right\|_{\mathbb T}^2,}
\qquad
\|a\|_{\mathbb T}=\min_{j\in\mathbb Z}|a-j|.
\tag{TW1}
\]

The parent [virtual-field form metric manuscript](https://github.com/femboy2112/SUCC/blob/research/defect-window-tomography-2026-11-16/research/2026-11-16/defect_window_tomography/VIRTUAL_FIELD_FORM_METRIC.md) proves the existing exact source-rational bridge
\[
8\mathcal R_B-\rho_B
\le 1-\Re W_B(1)\le2\pi^2\mathcal R_B+\rho_B,\quad
\rho_B=\frac{8r(2B+1)}{225B}=O(B^{-3}),
\tag{TW2}
\]
with \(W_B(1)=B^{-1}\sum_{n=B}^{2B-1}e(16^nx)\), \(e(t)=\exp(2\pi it)\). Thus
\[
\boxed{R0\Longleftrightarrow\liminf_{B\to\infty}\mathcal R_B>0.}
\tag{TW3}
\]
This equivalence is **established under the inherited four-pole source identity and tail**. The actual positive liminf remains UNVERIFIED.

## 2. Backward symbolic dynamics: two sides of the zero-phase carrier

Write the rational terminal state as \(U_m=C_m+u_m\), \(C_m=\lfloor U_m\rfloor\in\mathbb Z\), \(0\le u_m<1\). Its k-th least significant hexadecimal digit is
\[
d_k(C_m)=\Big\lfloor\frac{C_m}{16^{k-1}}\Big\rfloor\bmod16,\quad 1\le k\le B,
\]
with residues in {0,...,15}; this remains well-defined for negative C via integer modulo.

Define the backward fractional carrier \(y_0=u_m\) and \(y_k=\{U_m/16^k\}\). Then for *every* integer C and real u in [0,1),
\[
\boxed{y_k=\frac{d_k+y_{k-1}}{16},\qquad
\mathcal R_B=\frac1B\sum_{k=1}^B\min(y_k,1-y_k)^2.}
\tag{TW4}
\]
This is a **contracting inverse-branch path**: 0 iterated attracts y to 0, F=15 iterated attracts y to 1. The points 0 and 1 are the *same* unit phase \(e(0)=e(1)=1\), but are opposite **oriented** faces of the chosen fractional chart. The analogy to a two-sided "virtual zero" is mathematically typed by this quotient; it is not an assertion about quantum vacuum or two physical temperatures.

Let
\[
D_B=\#\{1\le k\le B:d_k\in\{1,\ldots,14\}\},
\]
\[
J_B=\#\{2\le k\le B:(d_{k-1},d_k)\in\{(0,15),(15,0)\}\}.
\tag{TW5}
\]
D counts non-extreme digits; J counts **direct zero/F domain walls**, not every unequal pair of symbols. Both are exact integers determined by the one rational endpoint.

### TW-01 — coercive digit-wall inequality (PROVED PAPER)

For *every* rational or real terminal U=C+u and every B≥1,
\[
\boxed{
\frac{D_B/256+225J_B/65536}{B}
\le\mathcal R_B
\le\frac{D_B/4+(D_B+J_B+1)/255}{B}.
}
\tag{TW6}
\]

**Lower proof:** If \(d_k\in\{1,\ldots,14\}\), then \(y_k\in[1/16,15/16)\), so \(\min(y_k,1-y_k)\ge1/16\). If consecutive extreme digits switch from 0 to F, \(y_{k-1}\in[0,1/16)\) and \(1-y_k=(1-y_{k-1})/16>15/256\); for F to 0, \(y_{k-1}\in[15/16,1)\) and \(y_k=y_{k-1}/16\ge15/256\). Each wall corresponds to a distinct *extreme* index k, disjoint from bad-digit indices. Sum squared contributions.

**Upper proof:** Every non-extreme digit costs at most \(1/4\). Partition all remaining extreme digits into maximal constant runs of all 0 or all F. There are at most \(D_B+J_B+1\) runs. At the j-th position of any such run the distance to the selected endpoint 0 or 1 is at most \(16^{-j}\). The sum of squared distances per run is at most \(\sum_{j\ge1}16^{-2j}=1/255\). Sum runs and non-extreme contributions. \(\square\)

In particular if \(E_B:=D_B+J_B\),
\[
\frac{225}{65536}\frac{E_B}{B}
\le\mathcal R_B
\le\frac{1/4+1/255}{B}E_B+\frac1{255B}.
\tag{TW7}
\]

### TW-02 — *exact* symbolic R0 criterion, not an asymptotic proof

Combining TW3 and TW7 yields for the **literal zero-seeded, original four-pole source**:
\[
\boxed{
R0\Longleftrightarrow
\liminf_{B\to\infty}\frac{D_B+J_B}{B}>0.
}
\tag{TW8}
\]
No implication about positive \(\liminf\) is deduced from formal contraction. This is a new-to-project equivalent arithmetic target: the late terminal digits cannot be dominated by arbitrarily long nearly monochromatic 0/F islands **with sublinear total excitations/domain walls**.

If \(\mathcal R_B\to0\) along a subsequence, TW7 gives \(E_B=o(B)\). The \(B-D_B\) extreme digits lie in at most \(E_B+1\) constant extreme runs; hence one run has length at least
\[
\boxed{L_B\ge\frac{B-D_B}{E_B+1}\longrightarrow\infty.}
\tag{TW9}
\]
This is a necessary long-shadow witness; its length may still be o(B) and cannot be excluded by mere irrationality. The converse "one long run means R0 fails" is **false**, because other digits may carry a positive density of energy.

### TW-03 — source carry correction changes at most three events (PROVED PAPER)

The actual completed terminal integer \(H_m=\lfloor16^m x\rfloor\) differs from \(C_m\) by at most 1, since \(0<T_m<1\):
\[
H_m=C_m+\varepsilon_m,\qquad\varepsilon_m\in\{0,1\}.
\tag{TW10}
\]
Adding 1 to a base-16 integer changes its trailing run of F digits into 0 and increments the first following non-F digit. Within any last-B suffix it changes at most **one** non-extreme digit status and at most **two** zero/F wall events:
\[
\boxed{|\Delta D_B|\le1,\quad|\Delta J_B|\le2,\quad
|E_B(H_{2B})-E_B(C_{2B})|\le3.}
\tag{TW11}
\]
Thus TW8 is equivalently stated using the **actual** B hexadecimal digits of x at positions B+1,...,2B, up to a uniform O(1/B) correction. The observation is not an assertion of ordinary digit normality. The sign/position of the carried boundary must be retained for exact finite certificates.

## 3. Collapse = sublinear symbolic source complexity, conditionally

Fix B and an event budget K. Let \(N(B,K)\) count all length-B hexadecimal words with \(D+J\le K\). Choose d nonextreme positions (14 symbols each), at most d+1 groups of extreme digits (at most 2 choices of first digit in each group), and w zero/F switches on at most B edges. The elementary overcount gives
\[
\boxed{
N(B,K)\le2\!\!\sum_{\substack{d,w\ge0\\d+w\le K}}
\binom Bd\binom Bw\,28^d.
}
\tag{TW12}
\]
If \(K_B=o(B)\), the standard entropy bound on binomial coefficients implies
\[
\boxed{\log N(B,K_B)=o(B).}\tag{TW13}
\]
This is a **count of possible symbolic forms** under a declared event budget, not Shannon entropy of a deterministic π orbit, thermodynamic entropy, or a bound on π's Kolmogorov complexity (π's computability already supplies short programs for its prefixes).

**TW-04 (PROVED PAPER):** a hypothetical subsequence \(\mathcal R_{B_j}\to0\) forces the actual terminal symbolic suffixes into a subexponential-size 0/F-domain-wall language. Source arithmetic would have to exclude that low-complexity *form family* on every sufficiently late shell. This recovers the user's "computational fixed-point shadow" idea with a falsifiable mathematical cost.

## 4. Nested prime/cofactor and radix residual tomography

Write the *actual* reduced rational terminal \(U_m=N_m/Q_m\), \(Q_m>0\), \(\gcd(N_m,Q_m)=1\). At radial depth k define
\[
a_{m,k}=N_m\bmod(16^kQ_m),\qquad 0\le a_{m,k}<16^kQ_m.
\tag{TW14}
\]
These satisfy the **compatible inverse system**
\[
a_{m,k+1}\equiv a_{m,k}\pmod{16^kQ_m},
\qquad
\left\|\frac{U_m}{16^k}\right\|_{\mathbb T}
=\frac{\min(a_{m,k},16^kQ_m-a_{m,k})}{16^kQ_m}.
\tag{TW15}
\]
Therefore \(\mathcal R_B\) can also be calculated from a single source-labelled modular residue tower with **zero floating-point operations**. This is a concrete interferometry interface among radix-16, denominator/cofactor and the signed integer representative. It does not assume an independent prime clock, uniform CRT residues, or Haar digit statistics.

### TW-05 — fresh prime in the original source, but no positive density from one prime (PROVED PAPER)

If \(m\ge2\) and \(p=8m-7\) is prime, then \(U_m\) has p-adic valuation \(-1\) and its reduced denominator \(Q_m\) is divisible by p. Indeed every earlier source denominator is less than p; the other three denominators at time m are \(p+3,p+4,p+5<2p\), so none is divisible by p. Only the genuine \(4/p\) term creates the pole and 4 is invertible modulo p. This is an **original four-pole** rational source fact.

But it does **not** force a positive low-digit event count: for any finite odd Q and any residue a modulo Q, the CRT gives an integer \(C=16^Bt\) with \(C\equiv a\pmod Q\). Its terminal \(V=C+1/Q\) has reduced denominator Q, numerator congruent to 1 modulo Q, and \(D_B(V)=J_B(V)=0\) while
\[
\mathcal R_B(V)=\frac{1-16^{-2B}}{255BQ^2}.
\tag{TW16}
\]
An all-F terminal suffix is equally compatible. Thus **finite odd cofactor congruences without source height, orientation and full history cannot imply R0**. This is a source-map inadequacy countermodel, not a falsification of the actual four-pole chronology.

### TW-06 — endpoint phase/cofactor clone that erases the winding (EXACT)

For the genuine \(U_{2B}=C+u=N/Q\), construct the **unauthenticated** terminal phase-fiber clone
\[
C^\star=16^B\left\lfloor\frac{C}{16^B}\right\rfloor,
\qquad V=C^\star+u.
\tag{TW17}
\]
Then
\[
\begin{aligned}
e(V)&=e(U_{2B}),\\
\operatorname{den}(V)&=Q,\qquad
\operatorname{num}(V)\equiv N\pmod Q,\\
0&\le U_{2B}-V<16^B,\qquad D_B(V)=J_B(V)=0,\\
\boxed{\mathcal R_B(V)}
&=\boxed{\frac{u^2(1-16^{-2B})}{255B}.}
\end{aligned}
\tag{TW18}
\]
This clone preserves the **exact terminal circle phase, fractional state, reduced denominator and every prime-divisor residue of the numerator** while changing integer winding and the backward family of probes. It is a one-stage clone, not the legal zero-seeded BBP historical source. This is a decisive receipt against any theorem deriving \(\mathcal R_B>0\) from a terminal scalar, local cofactor, or denominator alone.

At every tested authentic shell B=16,32,64,128,256, the original norm is >0.075 while the clone norm is <1/(255B). The exact comparisons are executed, not novel asymptotic evidence.

## 5. Hostile crucible: identical finite forcing + positive decreasing Gamma-asymptotic tail yet locked endpoint

The following is the strongest new negative control. It preserves *arbitrarily many exact* source forcing terms and **also** the literal zero seed, positivity, strict monotonicity and the authentic leading Gamma/BBP n^-2 forcing coefficient.

Fix any integer M≥1. Let \(P_M=\sum_{j=1}^M16^{-j}r(j)\in\mathbb Q\). Define
\[
b_n=\frac1{64(n+1)^2},\qquad
f_0(n)=16b_{n-1}-b_n=\frac1{4n^2}-\frac1{64(n+1)^2}.
\tag{TW19}
\]
The exact rational gap \(\Delta_M:=r(M)-f_0(M+1)\) is *positive* for every integer M≥1, since its denominator is positive and its numerator equals
\[
24000M^5+87240M^4+47714M^3-56719M^2+1180M+2773>0.
\tag{TW20}
\]
Proof of sign: \(87240M^4-56719M^2=M^2(87240M^2-56719)>0\), and every other displayed term is positive.

Choose \(0<D<\min\{b_M/2,(8/255)\Delta_M\}\) and a *radix-rational* \(q=a/16^K\) such that
\[
q=P_M+16^{-M}(b_M+D).
\tag{TW21}
\]
Such a q exists: choose K sufficiently large so the radix grid meets the nonempty interval \(P_M+16^{-M}(b_M,b_M+\min\{b_M/2,(8/255)\Delta_M\})\). Define \(g_n=b_n+D16^{-(n-M)}\) for n≥M and
\[
\widetilde r(n)=
\begin{cases}
r(n),&1\le n\le M,\\
16g_{n-1}-g_n,&n>M.
\end{cases}
\qquad\widetilde U_0=0,\quad
\widetilde U_n=16\widetilde U_{n-1}+\widetilde r(n).
\tag{TW22}
\]

### TW-07 — finite-prefix/Gamma counterfeit theorem (PROVED PAPER, original-source mutant)

This constructed **rational** forcing has all of the following properties:

1. It agrees **exactly** with the original four-pole r(n) for every 1≤n≤M, and retains the literal zero seed.
2. It is strictly positive and strictly decreasing for all n≥1. The authentic prefix monotonicity follows from its positive Mellin integral; for n>M, \(f_0(n)\) and the positive exponential correction \((255/16)D16^{-(n-1-M)}\) are separately strictly decreasing. At the seam, \(\widetilde r(M+1)=f_0(M+1)+(255/16)D<r(M)-\Delta_M/2<r(M)\).
3. It has **the same leading Gamma-shaped source asymptotic** as the authentic BBP:
\[
\widetilde r(n)=\frac{15}{64n^2}+O(n^{-3}),
\qquad
g_n=\frac1{64n^2}+O(n^{-3}).
\tag{TW23}
\]
The authentic r(n) also has leading \(15/(64n^2)\); their n^-3 coefficients generally differ. No claim is made of matching all source jets or the original poles.
4. Exact telescoping gives
\[
\sum_{n\ge1}16^{-n}\widetilde r(n)=P_M+16^{-M}g_M=q,
\qquad
\widetilde U_n=16^nq-g_n\quad(n\ge M).
\tag{TW24}
\]
Because q has denominator dividing 16^K, the **completed** radix-16 orbit is identically phase 1 for every n≥K. For B≥max{M,K}, \(0<g_{2B}<1\), the last B integer digits of \(\widetilde U_{2B}\) are all F, and
\[
\boxed{\widetilde{\mathcal R}_B
=\frac{g_{2B}^2(1-16^{-2B})}{255B}
=O(B^{-5})\longrightarrow0.}
\tag{TW25}
\]

**Consequent no-go:** any claimed R0 theorem using only finitely many literal authentic forcing values, zero seed, positive monotonic rational forcing and the leading Γ(2)/n² scale is false. The exact **infinite four-pole law and its global signed arithmetic** must contribute. This does NOT show π fails R0. It is an adversarial source mutation, not an alternate π formula.

The full explicit algorithm for selecting q and D is committed as a focused exact Fraction test. The first attempted finite calibration made a wrong finite-n error threshold, which was repaired before publication; the final signed asymptotic identities were checked exactly.

## 6. The remaining R0 arithmetic theorem (OPEN) and decisive probes

Combining TW8 with the source passport, the desired event budget is
\[
\boxed{
\exists\eta>0,\ B_0:\ \forall B\ge B_0:
\quad D_B(C_{2B})+J_B(C_{2B})\ge\eta B.
}
\tag{TW26 — OPEN}
\]

An arithmetic proof must act on the **actual** zero-seeded four-pole rational \(U_{2B}\) and its full odd-denominator, integer-winding and signed cofactor history. The rank-one finite-prime register in TW-05 and the exact Gamma-asymptotic forcing profile in TW-07 are **not** sufficient.

Suggested non-circular next probe: select an original-source cofactor/carry **signed conditional response** that predicts event density TW26 but is not simply a renamed average of its target. Predeclare a lower estimate on that response with an explicit rational error; use source-compatible CRT and Fourier orientations. Then run leave-one-cofactor-family-out ablations and compare the genuine source against the locked counterfeits TW-06/TW-07. A theorem must *eliminate* the counterfeits using a feature the authentic source has and the mutants lack. Merely accumulating new finite shells does not discharge the all-B quantifier.

A distinguished *source-general impossibility* is now certified: neither finite cofactor residues nor finite forcing prefixes nor the first Γ asymptotic coefficient can be that discriminating feature alone.

## 7. Claim ledger (read-only inherited frontier + new exact scope)

| Claim | Status | Exact scope / decisive boundary |
|---|---|---|
| TW-01 | **CLASSICAL / PROVED PAPER** | Universal terminal digit-wall coercivity TW6; test against all length-3 hexadecimal words |
| TW-02 | **EXACT EQUIVALENCE / INHERITED R0 OPEN** | Original-source TW8; does NOT provide positive liminf |
| TW-03 | **PROVED PAPER** | One source-tail carry changes D by ≤1, J by ≤2; source and completed digits differ by ≤3 events |
| TW-04 | **CLASSICAL / PROVED PAPER** | Low-energy forms occupy a subexponential *word family*; not entropy of deterministic π |
| TW-05 | **SOURCE-SPECIFIC FINITE PRIME FACT / CRT NO-GO** | Fresh p=8m−7 and independent congruence impostor; source-incomplete |
| TW-06 | **EXACT HOSTILE CLONE** | Equal terminal phase/cofactor with radically different integer-winding backward energy |
| TW-07 | **PROVED PAPER / COUNTERMODEL** | Any finite authentic forcing prefix + zero seed + positive decreasing asymptotically Gamma-matched source can complete to locked rational |
| TW-26 | **OPEN / UNVERIFIED** | Original exact four-pole terminal defect density uniformly positive on every sufficiently late B |
| R0 / π normality / RH | **OPEN** | R0 is weaker than all-mode base-16 normality; no promotion |

**Reproducibility:** the exact stdlib [test_terminal_wall_crucible.py](../../../tests/test_terminal_wall_crucible.py), [VALIDATION](VALIDATION.md), [SOURCE_MAP](SOURCE_MAP.md) and [NEXT](NEXT.md) separate executed arithmetic, paper proofs and all outstanding source-selection debt. The first two levels are shared mathematical definitions and are not independent witnesses.

**User's virtual-zero interpretation:** The terminal norm has two oriented zero-phase basins (all 0, all F) and paid transitions/in-between digits. This is a *precisely defined finite dynamical quotient with a computable defect norm*, not a literal quantum vacuum, thermodynamic absolute zero, or proof that π's digits are random.
