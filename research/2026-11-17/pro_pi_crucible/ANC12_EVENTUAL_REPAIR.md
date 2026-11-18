# Eventual primitive CRT repair of the ANC-12 terminal clone

**Scope.** This appendix repairs one false assertion in ANC-12 at commit
`97c7433371feca631991a1b8227b656e92e4abcb`. It proves a theorem about rational
terminal states carrying prescribed finite local data. It does not construct
a second zero-seeded trajectory with the original BBP forcing, preserve the
full chronological history, or prove R0 or normality. This is a same-model
paper derivation and exact finite check, not external peer review.

## 1. Preserve the original failure

ANC-12 chooses `R_sharp = N mod (16^B Pi_star)` and claims that
`C_sharp + R_sharp/Q` preserves the reduced denominator Q. The smallest
counterexample in its declared range B >= 2 is B = 3 (B = 2 was also checked).
The original exact receipt is:

```json
{
  "B": 3,
  "N": "80827484660698633414",
  "Q": "24536311574775",
  "Pi_star": "19224941",
  "modulus": "78745358336",
  "R_sharp": "67379365062",
  "gcd_R_Q": "3",
  "reduced_shadow_denominator": "8178770524925",
  "same_2adic_mod_16B": true,
  "all_uncollided_principal_parts_match": true,
  "domain_wall_counts": [0, 0],
  "fits": true
}
```

Thus its reduced denominator is Q/3. The error does not destroy its finite
2-adic or selected-prime projections. It destroys the asserted preservation
of **all of Q**. The following construction adds a coprimality sieve.

## 2. A finite primitive-progression lemma

Let U = N/Q be reduced, Q a positive odd integer, and let Pi be a squarefree
divisor of Q with gcd(Pi, Q/Pi) = 1. For an integer B >= 1, set

\[
q=Q/\Pi,\quad w=\omega(q),\quad M=16^B\Pi,\quad
R_0=N\bmod M,\quad
C_0=16^B\left\lfloor\frac{\lfloor U\rfloor}{16^B}\right\rfloor.
\]

Here residues lie in [0,M), and omega(1) = 0. Suppose an integer L satisfies

\[
L>4^w,\qquad LM\le Q.                                      \tag{R1}
\]

Then there exists 0 <= t < L such that R = R_0+tM is coprime to Q. The rational

\[
V=C_0+R/Q                                                     \tag{R2}
\]

has reduced denominator exactly Q and satisfies all of:

\[
\begin{aligned}
&V-U\in16^B\mathbb Z_{(2)},\\
&V-U\in\mathbb Z_{(p)}\quad\text{for every }p\mid\Pi,\\
&\lfloor V\rfloor=C_0,\qquad D_B(V)=J_B(V)=0,\\
&\frac1B\sum_{k=1}^B\left|V/16^k\right|_{\mathbb T}^{2}
 =\frac{(R/Q)^2(1-256^{-B})}{255B}<\frac1{255B}.
\end{aligned}                                               \tag{R3}
\]

In particular, the selected principal parts are unchanged:
pV = pU modulo p Z_(p), and v_p(V) = v_p(U) = -1 for every p dividing Pi.

**Proof.** The stated hypotheses imply gcd(M,q) = 1: q is odd and has no
prime factor in Pi. Also gcd(R_0,Pi) = 1, because R_0 = N modulo Pi and N/Q
is reduced. Hence gcd(R_0+tM,Q) = 1 is equivalent to
gcd(R_0+tM,q) = 1.

Write d_0 = rad(q). For each d dividing d_0, the congruence
R_0+tM = 0 modulo d has exactly one solution class in t, since M is a unit
modulo d. Inclusion–exclusion therefore gives, with actual integer counts,

\[
\begin{aligned}
A_L&=\#\{0\le t<L:\gcd(R_0+tM,q)=1\}\\
&=\sum_{d\mid d_0}\mu(d)\#\{0\le t<L:R_0+tM\equiv0\pmod d\}\\
&\ge L\sum_{d\mid d_0}\frac{\mu(d)}d-2^w
 =L\frac{\varphi(q)}q-2^w.                                  \tag{R4}
\end{aligned}
\]

The error bound follows because each progression count differs from L/d
by less than one; there are 2^w squarefree divisors. Since
phi(q)/q = product_(p|q)(1-1/p) >= 2^(-w), condition L > 4^w makes the
right side strictly positive. This includes q = 1 with the empty product.
Choose the least admissible t.

Now 0 <= R < LM <= Q and gcd(R,Q) = 1. Thus V has fractional part R/Q,
floor C_0, and reduced denominator Q. The numerator R-N is divisible by
M. Because Q is odd and C_0 is a multiple of 16^B, V-U belongs to
16^B Z_(2). For p dividing Pi, v_p(Q) = 1 while p divides R-N, so V-U
is p-integral. This proves the principal-part statement.

For every 1 <= k <= B, C_0/16^k is an integer, while
0 <= (R/Q)/16^k < 1/16. Its distance to the nearest integer is itself.
Summing the finite geometric progression proves (R3). The last B hex
digits of C_0 are all zero. QED.

## 3. The repaired authentic-terminal theorem: an eventual quantifier

Use the original source and literal zero seed. Write
U_(2B) = N_B/Q_B in lowest terms. Let Pi_B be the product of the primes
in ANC-07's selected set at horizon n = 2B:

\[
\begin{split}
\mathcal P_n^*={}&\{4n<p\le8n-3:p\text{ prime},\ p\equiv1,5\pmod8\}\\
&\cup\{8n/3<p\le4n-1:p\text{ prime},\ p\equiv3,7\pmod8\}.
\end{split}
\]

**Theorem R-ANC12.** There exists B_0 such that for every integer B >= B_0,
the construction (R2), using U_(2B), Pi_B and

\[
L_B=4^{\omega(Q_B/\Pi_B)}+1,
\]

produces a rational V_B satisfying all conclusions (R3), with **the exact
reduced denominator Q_B**. In particular, the original denominator, finite
2-adic shell residue, and every selected prime principal part coexist with
a terminal block of B zeros and norm tending to zero.

**Proof of eventual applicability.** The combined source identity

\[
r(n)=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}
\]

shows Q_B is odd. Every selected p occurs in exactly one native pole
through horizon 2B, with nonzero coefficient modulo p; hence
v_p(U_(2B)) = -1. Therefore Pi_B is squarefree, divides Q_B, and
gcd(Pi_B,Q_B/Pi_B) = 1. These are the primitive-progression hypotheses;
they must not be dropped.

The inherited theorem CG-01 proves log den(U_n) = 6n+o(n). The fixed-modulus
prime number theorem used in ANC-07 gives log product_(p in P_n^*) p
= (8/3)n+o(n). Therefore, with q_B = Q_B/Pi_B,

\[
\begin{aligned}
\log Q_B&=12B+o(B),\\
\log\Pi_B&=(16/3)B+o(B),\\
\log q_B&=(20/3)B+o(B),\\
\log\frac{Q_B}{16^B\Pi_B}
 &=\left(\frac{20}{3}-\log16\right)B+o(B).                  \tag{R5}
\end{aligned}
\]

The last coefficient is strictly positive. The notation here is logarithmic:
q_B = exp((20/3+o(1))B). No claim q_B/exp((20/3)B) -> 1 follows.

For completeness, omega(q_B) = O(B/log B) needs no further prime-number
theorem. If w = omega(q_B), its distinct prime factors, in increasing
order, satisfy p_i >= i+1, so

\[
q_B\ge(w+1)!,\qquad
\log q_B\ge\tfrac w2\log(w/2)\quad(w\ge2).
\]

By (R5), log q_B <= 7B eventually. If w <= sqrt(B), the desired estimate
already holds. If w > sqrt(B), then for B >= 16,
log(w/2) >= (1/4)log B. Consequently w <= 56B/log B.
Thus log L_B <= omega(q_B)log4+log2 = O(B/log B) = o(B).
Combining this with (R5) gives L_B 16^B Pi_B < Q_B for all sufficiently
large B. The finite lemma applies. QED.

The argument gives no explicit B_0 and makes **no claim for every B >= 2**.
CG-01 is imported from main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`,
`research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md`.
ANC-07 and its selected prime bands are at the audited pin named above.
CG-01, rather than ANC-07's weaker lower product bound alone, is needed
for the reduced-denominator asymptotic in (R5).

## 4. One exact repaired B = 3 witness

Keep the failed original witness of section 1. Here
q = 1276275 = 3*5^2*7*11*13*17. The first coprime candidate is t = 1:

\[
R=67379365062+78745358336=146124723398,
\qquad\gcd(R,Q)=1.
\]

The repaired clone is

\[
V=3293184+\frac{146124723398}{24536311574775}
 =\frac{80802588843188556998}{24536311574775}.
\]

Its low three hex digits are 000. Both U_6 and V have 2-adic residue 1514
modulo 4096. Their selected principal parts agree exactly:

| p | pU_6 modulo p | pV modulo p |
|---|---:|---:|
| 19 | 11 | 11 |
| 23 | 11 | 11 |
| 29 | 5 | 5 |
| 37 | 21 | 21 |
| 41 | 4 | 4 |

The exact norm is

\[
\mathcal R_3(V)=
\frac{1286484195985556022150841}{27748343886818929373062103040000}
<\frac1{765}.
\]

This individual witness was checked directly from the four signed source
fractions. It does not establish a small-B universal claim. In particular,
the deliberately coarse sufficient condition L_B M <= Q fails at B = 3
(L_B = 4097); the explicit t = 1 works anyway.

**Actual command:** `timeout 10s python repaired_b3.py`, in
`prime_scratch/late_frontier`; exit 0. All exact assertions passed.
Script: `late_frontier/repaired_b3.py`.
Raw structured receipt: `late_frontier/repaired_b3_receipt.json`.

These are the original scratch execution paths. Archived copies in this
dossier are audits/repaired_b3_original.py and evidence/adelic_repaired_b3.json.
The separate root calibration audit_adelic_pinned.py rechecks the original
failure directly from the four fractions; its actual root-run receipt is
evidence/audit_adelic_pinned.json. No unperformed replay is implied.

## 5. Logical boundary

The repaired theorem shows that the listed terminal arithmetic marks do
not imply positive domain-wall density. The clone depends on B and is not
asserted to arise from one coherent original-source history. An octic
period character belongs to a forcing/history, not intrinsically to an
arbitrary rational terminal state; it is not an additional preserved
invariant established by this construction. An argument using the full
authenticated chronology may still distinguish the clone. R0, authentic
terminal coercivity, swept Borwein convergence, and full normality remain
open. The sieve repair is a quantitative no-go theorem for this specified
finite projection, not a source-specific signed saving.
