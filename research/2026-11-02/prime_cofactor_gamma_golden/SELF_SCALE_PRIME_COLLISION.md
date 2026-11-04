# PGC-10 — ONE self-resolution collision observable per prime-clean dyadic epoch

**2026-11-02 · Research-only paper theorem, CONDITIONAL on original-source upper bound.** This sharpens the quantifier of PGC-09's remaining real-cofactor inequality. No source poles, seeds or previous proof contracts are changed.

## I. A single fully finite ORIGINAL source histogram

For a dyadic integer A=2^j≥2, take the exact ORIGINAL four-pole, literal-zero-seeded rational BBP orbit
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_n=16U_{n-1}+r(n)\in\mathbb Q.
\]
Let
\[
v_i(A)=\#\{A\le n<2A:\lfloor A\{U_n\}\rfloor=i\},
\quad i=0,\dots,A-1,\qquad
\boxed{\mathscr C_A=\frac1A\sum_{i=0}^{A-1}v_i(A)^2.}
\tag{SELF-01}
\]

This is a SINGLE exact nonnegative rational/integer collision observable at matching time/space scales: A source times, A bins, one value per dyadic A. The diagonal enforces \(\mathscr C_A\ge1\). It can be evaluated with exact integer remainders of U_n; no π digits, trigonometric floating-point, probability prior or modified seed enter.

For every sufficiently large dyadic A, PGC-09 proves (using classical unconditional PNT in p≡1 mod8) that there exists p=8k+1 prime such that the ENTIRE source epoch [A,2A) is in an exact p-clean interval [k+1,4k] with original p-free cofactor. The prime p changes by epoch; the actual U_n and \(\mathscr C_A\) do not.

## II. Universal fine→coarse histogram transfer

**Lemma SELF-02.** For ANY finite configuration of A points on the circle, let \(v_i\) be counts in A equal half-open bins and \(u_j\) counts in M equal half-open bins, where 2≤M≤A. Then

\[
\boxed{\sum_{j=0}^{M-1}u_j^2
\le\bigl(\lceil A/M\rceil+1\bigr)\sum_{i=0}^{A-1}v_i^2
\le(A/M+2)\sum_{i=0}^{A-1}v_i^2.}
\tag{SELF-02}
\]

Proof with no independence assumption. Intersect fine bin i with coarse bin j, and write \(v_{i,j}\ge0\) for the number of original points in that intersection; \(\sum_j v_{i,j}=v_i\), \(\sum_i v_{i,j}=u_j\). Any coarse M-bin meets at most \(\lceil A/M\rceil+1\) fine A-bins, including its endpoints. Cauchy gives \(u_j^2\le(\lceil A/M\rceil+1)\sum_i v_{i,j}^2\). Sum over j, then \(\sum_jv_{i,j}^2\le(\sum_jv_{i,j})^2=v_i^2\). Done. The circle is modeled by matching [0,1) half-open partitions, so neither wraparound nor boundary points are discarded.

In particular if for the ORIGINAL chosen source \(\mathscr C_A\le C\), then for EVERY coarse M≤A,

\[
\boxed{\sum_{j<M}u_j(A,M)^2
\le C(A^2/M+2A)\le2C(A^2/M+A).}
\tag{SELF-03}
\]

Thus PGC-09's still-OPEN all-M source hypothesis is implied by a SINGLE all-epoch self-scale bound, with constant 2C. A hypothetical all-M hypothesis obviously implies its M=A case, so the two hypothesis types are **equivalent up to a universal constant** in their stated all-dyadic-epoch quantified form. This is a genuine quantifier reduction, NOT new arithmetic cancellation.

## III. Closed conditional normality route: exact one-number-per-epoch theorem

**THEOREM SELF-04 (proved implication; premise OPEN):**

\[
\boxed{
\left[\exists C<\infty,\ A_*:\ 
\forall A=2^j\ge A_*,\quad
\mathscr C_A\le C\right]
\ \Longrightarrow\
\pi\text{ is normal in base }16.
}
\tag{OPEN-SELF-SCALE-GATE}
\]

Proof: SELF-03 yields PGC-09 local bound with constant \(2C\) on every dyadic epoch and all meshes M≤A. PGC-09's EXACT source Gamma one-bin transport and ℓ² Minkowski gluing then imply \(\limsup_{L\to\infty}\mathscr B_L\le36(2C)=72C\) for the square checkpoint \(N=L²,M=L+1\), where \(\mathscr B_L=\frac{M}{N²}\sum_jc_j²\) and the c_j are exact rational-completion histogram counts. PGC-05's universal Fejér bound gives \(\mathscr Q_L\le(3+\pi²/12)\mathscr B_L=O(1)\), and parent #471 GF-07 establishes base-16 π normality by the radix Ward ladder and Weyl's criterion. No conjectural prime count or false p-to-real transfer occurs at these steps. QED **as a conditional theorem**.

## IV. One numerical diagnostic per epoch (not evidence of a bound)

Exact integer original U histograms, no numerical circle phases:

| dyadic A | exact Σ v_i² | \(\mathscr C_A\) |
|--:|--:|--:|
| 8 | 14 | 7/4 |
| 16 | 34 | 17/8 |
| 32 | 52 | 13/8 |
| 64 | 110 | 55/32 |
| 128 | 220 | 55/32 |
| 256 | 504 | 63/32 |

These are merely FINITE tests, not asymptotic evidence. A source-changed or same-source real counterseed can invalidate uniform collision control; the *literal rational zero state* is essential. The prime clocks can have small order, so showing only a large new prime denominator does not establish SELF-04's premise.

## V. Next decisive lamp

Instead of proving infinitely many \((A,M)\) histogram bounds or covering all ordered pairs with one prime, prove or refute just ONE bound for the original selected sequence:

\[
\sup_{j\ge j_0}
\frac1{2^j}\sum_{a=0}^{2^j-1}
\#\left\{
2^j\le n<2^{j+1}:
\left\lfloor2^j\{U_n\}\right\rfloor=a
\right\}^2<\infty.
\]

At each A, select the prime p≡1 mod8 whose source-clean window contains [A,2A), keep all four signed poles and the real p-free phase together, and derive an O(A) true near-cell pair count. A Galois-averaged O(A) statement is **not** an adequate substitute for the selected real embedding. Independent holdouts should vary p-clock order, cofactor height, n/parity, Fibonacci/gamma shell, and wrong seeds. Gamma/Euler–Mascheroni η-defect scales certify finite/global seam error but contribute no statistical independence.

**Ledger:** SELF-02/03 = disclosed elementary universal combinatorics; SELF-04 = proved conditional theorem; self-scale selected source bound = UNVERIFIED / OPEN; π normality and RH = OPEN. Attribution: classical Cauchy–Schwarz and refinement collisions (cf. SUCC #407); new to the branch is the exact one-number-per-dyadic-epoch pipeline through #471 and PGC-09, not a novelty claim for general histogram normality criteria.
