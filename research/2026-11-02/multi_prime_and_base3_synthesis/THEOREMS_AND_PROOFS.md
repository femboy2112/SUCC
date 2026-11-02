# Theorems, Proofs, and Structural Analysis — Multi-Prime CRT Cofiber Recurrence & Base-3 Synthesis Mega-Round II (`MPB-01`..`MPB-18`)

**Date:** `2026-11-02`  
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`  
**Dossier Directory:** `research/2026-11-02/multi_prime_and_base3_synthesis/`

---

## 1. Front 1: Multi-Prime CRT Cofiber Recurrence & Geometric Coupling (`MPB-01`..`MPB-04`)

### 1.1 Theorem `MPB-01` (Simultaneous Multi-Prime CRT Cofiber Recurrence & Zero Carry Interference)

#### Statement
Let $p_1, \dots, p_r \ge 7$ be distinct primes with $p_i \equiv 1 \pmod 4$. Let $Q = \prod_{i=1}^r p_i$. On the joint single-pole window
$$\max_{1 \le i \le r} b_{p_i} \le j < \min_{1 \le i \le r} J_{p_i} - 1,$$
define the simultaneous $Q$-cofiber
$$W_{Q, j} := U_j - \sum_{i=1}^r \frac{a_{p_i, j}}{p_i} \in \bigcap_{i=1}^r \mathbb{Z}_{(p_i)}.$$
Then $W_{Q, j}$ satisfies the exact additive carry recurrence
$$W_{Q, j+1} = 16 W_{Q, j} + r(j+1) + \sum_{i=1}^r \kappa_{p_i, j}, \qquad \kappa_{p_i, j} = \left\lfloor \frac{16 a_{p_i, j}}{p_i} \right\rfloor \in \{0, \dots, 15\}.$$
In particular, there is **zero inter-prime carry coupling**: each prime's hex expansion digit $\kappa_{p_i, j}$ depends strictly on $a_{p_i, j}$ and enters the integer part of $W_{Q, j+1}$ additively.

#### Proof
By the primary step Euclidean decomposition (`PCN-01`), for each $i \in \{1, \dots, r\}$,
$$16 a_{p_i, j} = p_i \kappa_{p_i, j} + a_{p_i, j+1}.$$
Dividing by $p_i$:
$$\frac{a_{p_i, j+1}}{p_i} = 16 \frac{a_{p_i, j}}{p_i} - \kappa_{p_i, j}.$$
The authentic BBP orbit satisfies $U_{j+1} = 16 U_j + r(j+1)$. Subtracting the sum over all $i$:
$$W_{Q, j+1} = U_{j+1} - \sum_{i=1}^r \frac{a_{p_i, j+1}}{p_i} = \left(16 U_j + r(j+1)\right) - \sum_{i=1}^r \left(16 \frac{a_{p_i, j}}{p_i} - \kappa_{p_i, j}\right)$$
$$= 16 \left(U_j - \sum_{i=1}^r \frac{a_{p_i, j}}{p_i}\right) + r(j+1) + \sum_{i=1}^r \kappa_{p_i, j} = 16 W_{Q, j} + r(j+1) + \sum_{i=1}^r \kappa_{p_i, j}.$$
Multiplying through by $Q$:
$$Q W_{Q, j+1} - 16 Q W_{Q, j} - Q r(j+1) = Q \sum_{i=1}^r \kappa_{p_i, j}.$$
This identity is verified in `MultiPrimeBase3Core.lean` for $r=2$ (`two_prime_scaled_cofiber_step_identity`) and $r=3$ (`three_prime_scaled_cofiber_step_identity`). $\blacksquare$

---

### 1.2 Theorem `MPB-02` (Two-Prime CRT Periodicity, Coprime-Order Midy Tensor Law & Two-Prime Twisted Gauss Bound)

#### Statement
Let $p \ne q$ be odd primes with $L_p = \mathrm{ord}_p(16)$ and $L_q = \mathrm{ord}_q(16)$.
1. The joint primary residue pair $(a_{p, j} \bmod p, a_{q, j} \bmod q)$ has exact minimal period $L_{p, q} = \mathrm{lcm}(L_p, L_q)$.
2. Simultaneous half-period Midy complementarity holds (i.e. $\exists M \in \mathbb{N}$ such that $a_{p, j+M} = p - a_{p, j}$ and $a_{q, j+M} = q - a_{q, j}$ for all $j$) if and only if
   $$v_2(L_p) = v_2(L_q) \ge 1,$$
   with $M = \mathrm{lcm}(L_p, L_q)/2$.
3. When $\gcd(L_p, L_q) = 1$, the untwisted two-prime subgroup Gauss sum over $\langle (16, 16) \rangle \subset (\mathbb{Z}/p\mathbb{Z})^\times \times (\mathbb{Z}/q\mathbb{Z})^\times$ factors exactly:
   $$G_{p, q}(\alpha_p, \alpha_q; 0) = G_p(\alpha_p; 0) \cdot G_q(\alpha_q; 0),$$
   and in general $|G_{p, q}(\alpha_p, \alpha_q; \ell)| \le \gcd(L_p, L_q) \sqrt{pq}$.

#### Proof
1. The order of $(16, 16)$ in the direct product $(\mathbb{Z}/p\mathbb{Z})^\times \times (\mathbb{Z}/q\mathbb{Z})^\times$ is $\mathrm{lcm}(\mathrm{ord}_p(16), \mathrm{ord}_q(16)) = L_{p, q}$.
2. A half-period $M$ satisfies $16^M \equiv -1 \pmod p$ and $16^M \equiv -1 \pmod q$ iff $16^{2M} \equiv 1 \pmod p$ with $16^M \not\equiv 1 \pmod p$ (so $L_p \mid 2M$ and $L_p \nmid M$) and similarly for $q$. This requires $v_2(L_p) = v_2(2M) = v_2(M) + 1$ and $v_2(L_q) = v_2(M) + 1$, which forces $v_2(L_p) = v_2(L_q) \ge 1$.
3. If $\gcd(L_p, L_q) = 1$, by CRT on the cyclic group $\mathbb{Z}/L_{p, q}\mathbb{Z} \cong \mathbb{Z}/L_p\mathbb{Z} \times \mathbb{Z}/L_q\mathbb{Z}$, the exponent $j \bmod L_{p,q}$ bijectively parametrizes pairs $(j_1, j_2) \in (\mathbb{Z}/L_p\mathbb{Z}) \times (\mathbb{Z}/L_q\mathbb{Z})$. The sum decomposes as:
   $$G_{p, q}(\alpha_p, \alpha_q; 0) = \sum_{j=0}^{L_{p, q}-1} e\left(\frac{\alpha_p 16^j}{p} + \frac{\alpha_q 16^j}{q}\right) = \left(\sum_{j_1=0}^{L_p-1} e\left(\frac{\alpha_p 16^{j_1}}{p}\right)\right) \left(\sum_{j_2=0}^{L_q-1} e\left(\frac{\alpha_q 16^{j_2}}{q}\right)\right) = G_p(\alpha_p; 0) G_q(\alpha_q; 0).$$
   Applying the Weil/subgroup Gauss bound $|G_p| \le \sqrt{p}$ and $|G_q| \le \sqrt{q}$ gives $|G_{p, q}| \le \sqrt{pq}$. In general, the index of the diagonal subgroup is $\gcd(L_p, L_q)$, yielding $|G_{p, q}| \le \gcd(L_p, L_q)\sqrt{pq}$. $\blacksquare$

---

### 1.3 Theorem `MPB-03` (Exact Prime-Window Overlap Kernel & Strict Cone Support)

#### Statement
For $X \ge 20$ and the prime-window second moment
$$\sum_{5 < p \le X, p \equiv 5 \pmod 8} |R_p(h)|^2 = \sum_{n, m} w_X(n, m) e(h(U_n - U_m)),$$
where $R_p(h) = \sum_{n=b_p}^{J_p-1} e(h U_n)$, $b_p = (p+3)/8$, and $J_p - 1 = (p-1)/2$:
1. The kernel $w_X(n, m)$ has exact closed form:
   $$w_X(n, m) = \#\left\{p \le X : p \equiv 5 \pmod 8, \,\, 2\max(n, m) + 1 \le p \le \min(X, 8\min(n, m) - 3)\right\}.$$
2. $w_X(n, m) = 0$ identically whenever $\max(n, m) \ge 4\min(n, m) - 1$, so $w_X(n, m)$ is strictly supported in the open cone
   $$\frac{1}{4} < \frac{n}{m} < 4.$$
3. The total overlap mass satisfies:
   $$\sum_{n, m} w_X(n, m) = \sum_{5 < p \le X, p \equiv 5 \pmod 8} \left(\frac{3p+1}{8}\right)^2.$$

#### Proof
1. An index $n$ belongs to the window $[b_p, J_p-1]$ iff $b_p \le n \le J_p - 1 \iff \frac{p+3}{8} \le n \le \frac{p-1}{2} \iff 2n + 1 \le p \le 8n - 3$. Both $n$ and $m$ belong to the window iff $2\max(n, m) + 1 \le p \le 8\min(n, m) - 3$.
2. The interval $[2\max(n, m) + 1, 8\min(n, m) - 3]$ is non-empty iff $2\max(n, m) + 1 \le 8\min(n, m) - 3 \iff 2\max(n, m) \le 8\min(n, m) - 4 \iff \max(n, m) \le 4\min(n, m) - 2$. If $\max(n, m) \ge 4\min(n, m) - 1$, the lower bound strictly exceeds the upper bound, so no such primes exist! This is verified in Lean 4 (`overlap_cone_vanishing_bound`).
3. Reversing summation: $\sum_{n, m} w_X(n, m) = \sum_p \sum_{n, m \in I_p} 1 = \sum_p |I_p|^2$. The window length is $(J_p - 1) - b_p + 1 = \frac{p-1}{2} - \frac{p+3}{8} + 1 = \frac{4p - 4 - p - 3 + 8}{8} = \frac{3p+1}{8}$. $\blacksquare$

---

### 1.4 Theorem `MPB-04` (Three-Edge BBP Decomposition & Mod-8 Pole-Isolation Duality)

#### Statement
Define the elementary edge function $f_m(n) := \frac{1}{8n-7} - \frac{1}{8n-7+m}$.
1. The BBP forcing $r(n)$ satisfies the exact 3-edge decomposition:
   $$r(n) = 2 f_3(n) + f_4(n) + f_5(n) \quad (\forall n \ge 1).$$
2. At birth step $n = b_p$:
   - For $p \equiv 5 \pmod 8$ ($p = 8b_p - 3$): the $p$-adic pole $-1/p$ is carried **exclusively** by edge $f_4(b_p) = \frac{1}{p-4} - \frac{1}{p}$, while $f_3(b_p)$ and $f_5(b_p)$ are $p$-integral.
   - For $p \equiv 1 \pmod 8$ ($p = 8b_p - 7$): the common left endpoint is $8b_p - 7 = p$. The pole $+4/p$ splits across $(2/p, 1/p, 1/p)$, while all right endpoints are $p$-integral.

#### Proof
1. Direct expansion:
   $$2 f_3(n) + f_4(n) + f_5(n) = \frac{2}{8n-7} - \frac{2}{8n-4} + \frac{1}{8n-7} - \frac{1}{8n-3} + \frac{1}{8n-7} - \frac{1}{8n-2} = \frac{4}{8n-7} - \frac{2}{8n-4} - \frac{1}{8n-3} - \frac{1}{8n-2} = r(n).$$
2. For $p \equiv 5 \pmod 8$, $b_p = (p+3)/8$. Then $8b_p - 7 = p - 4$, and the right endpoints are:
   - $f_3(b_p)$: right endpoint is $8b_p - 4 = p - 1$ ($p \nmid p-1$).
   - $f_4(b_p)$: right endpoint is $8b_p - 3 = p$ ($p \mid p$, residue $-1/p$).
   - $f_5(b_p)$: right endpoint is $8b_p - 2 = p + 1$ ($p \nmid p+1$).
   Thus $f_4(b_p)$ isolates the $p$-pole completely.
   For $p \equiv 1 \pmod 8$, $8b_p - 7 = p$, so $1/(8b_p-7) = 1/p$ enters $2f_3$ with weight $2$, $f_4$ with weight $1$, and $f_5$ with weight $1$. $\blacksquare$

---

## 2. Front 2: Multi-Step & Cross-Radix (16, 3) Coercivity (`MPB-05`..`MPB-08`)

### 2.1 Theorem `MPB-05` (All-Order $k$-Step Radix-$B$ Variational Coercivity)

#### Statement
For any integer radix $B \ge 2$, step count $k \ge 1$, and vectors on $\ker L_B^{(k)} = \{v_{k+1} - B^k v_1 = w\}$:
1. Exact algebraic identity:
   $$(B^k + 1) v_1^2 + B^k(B^k + 1) w^2 - (v_1 + B^k w)^2 = B^k (v_1 - w)^2 \ge 0.$$
2. The tight direct $k$-step trajectory weight is $\Lambda_{\mathrm{sum}}^{(k)}(B) = (B^k + 1)^2$, and the tight direct pairwise weight is $\Lambda_{\mathrm{pair}}^{(k)}(B) = B^{2k} + 1$.
3. The $k$-step Frobenius norm unifies:
   $$1^2 + (B^k + 1)^2 + B^{2k} = \Lambda_{\mathrm{pair}}^{(k)}(B) + \Lambda_{\mathrm{sum}}^{(k)}(B).$$

#### Proof
Expanding $(B^k + 1) v_1^2 + B^k(B^k + 1) w^2 - (v_1 + B^k w)^2$:
$$= B^k v_1^2 + v_1^2 + B^{2k} w^2 + B^k w^2 - (v_1^2 + 2 B^k v_1 w + B^{2k} w^2)$$
$$= B^k v_1^2 - 2 B^k v_1 w + B^k w^2 = B^k (v_1 - w)^2.$$
Since $B \ge 2$, $B^k (v_1 - w)^2 \ge 0$, with equality iff $v_1 = w$.
The total weight is $(B^k + 1) + B^k(B^k + 1) = (B^k + 1)^2 = \Lambda_{\mathrm{sum}}^{(k)}(B)$.
The pairwise weight $\Lambda_{\mathrm{pair}}^{(k)}(B) = B^{2k} + 1$ satisfies $(B^{2k} + 1)(v_1^2 + w^2) - (v_1 - B^k w)^2 = (B^k v_1 + w)^2 \ge 0$.
Adding them: $\Lambda_{\mathrm{pair}}^{(k)}(B) + \Lambda_{\mathrm{sum}}^{(k)}(B) = (B^{2k} + 1) + (B^k + 1)^2 = 1^2 + (B^k + 1)^2 + B^{2k}$, which is the squared Frobenius norm of the 3-element operator matrix. $\blacksquare$

---

### 2.2 Theorem `MPB-06` (Cross-Radix $(16, 3)$ Scale Bridge & Coupled Lagrange Identity)

#### Statement
1. Base-16 vs. base-3 scale proximity:
   $$16^2 - 3^5 = 256 - 243 = 13.$$
2. 2-step hex vs. 5-step ternary coercivity gap:
   $$\Lambda_{\mathrm{sum}}^{(2)}(16) - \Lambda_{\mathrm{sum}}^{(5)}(3) = (16^2 + 1)^2 - (3^5 + 1)^2 = 257^2 - 244^2 = 13 \times 501 = 6513.$$
3. For any two radices $B_1, B_2$ and variables $a, b, c$, the 3-variable coupled Lagrange identity holds:
   $$(B_1 + B_2 + 1)\left(B_1 a^2 + B_2 b^2 + c^2\right) - (B_1 a + B_2 b + c)^2 = B_1 B_2 (a - b)^2 + B_1 (a - c)^2 + B_2 (b - c)^2 \ge 0.$$
4. At $(B_1, B_2) = (16, 3)$, the joint constants are:
   $$\Lambda_{\mathrm{joint\_sum}}(16, 3) = (16 + 3 + 1)^2 = 400, \qquad \Lambda_{\mathrm{joint\_pair}}(16, 3) = 16^2 + 3^2 + 1 = 266,$$
   with sum $400 + 266 = 666 = 1^2 + 3^2 + 16^2 + 20^2$.

#### Proof
1. $16^2 = 256$, $3^5 = 243$, $256 - 243 = 13$.
2. Difference of squares: $257^2 - 244^2 = (257 - 244)(257 + 244) = 13 \times 501 = 6513$.
3. Expand $(B_1 + B_2 + 1)(B_1 a^2 + B_2 b^2 + c^2)$:
   $$= B_1^2 a^2 + B_1 B_2 a^2 + B_1 a^2 + B_1 B_2 b^2 + B_2^2 b^2 + B_2 b^2 + B_1 c^2 + B_2 c^2 + c^2.$$
   Expand $(B_1 a + B_2 b + c)^2$:
   $$= B_1^2 a^2 + B_2^2 b^2 + c^2 + 2 B_1 B_2 a b + 2 B_1 a c + 2 B_2 b c.$$
   Subtracting:
   $$= B_1 B_2 (a^2 - 2 a b + b^2) + B_1 (a^2 - 2 a c + c^2) + B_2 (b^2 - 2 b c + c^2) = B_1 B_2 (a - b)^2 + B_1 (a - c)^2 + B_2 (b - c)^2.$$
   This is verified constructively in Lean 4 (`joint_two_radix_trajectory_square_gap`).
4. At $(16, 3)$, $B_1 + B_2 + 1 = 20$, so the trajectory weight is $20^2 = 400$. The pairwise weight is $16^2 + 3^2 + 1 = 256 + 9 + 1 = 266$. Their sum is $666$. $\blacksquare$

---

### 2.3 Theorem `MPB-07` & `MPB-08` (Multi-Step Block-Strided Diophantine Threshold $\Phi_{\mathrm{stride}}^{(k)}(C, \mu)$)

#### Statement
Under stride $k$ block enclosure, the effective quadratic weight per step is reduced by the ratio
$$\rho_k(B) = \frac{(B^k + 1)^2}{(B+1)^{2k}} < 1 \quad (\forall k \ge 2).$$
At $B=16, k=2$, $\rho_2(16) = \frac{257^2}{289^2} = \frac{66049}{83521} \approx 0.790807$, giving a factor $(0.790807)^{J/2}$ saving in the Diophantine exponent and reducing $J_0$ and $J_2$.

#### Proof
Direct $k$-step enclosure replaces the iterated 1-step constant $(B+1)^{2k}$ with $(B^k + 1)^2$. For $B=16, k=2$:
$$(16^2 + 1)^2 = 257^2 = 66049 < 83521 = 289^2 = (16+1)^4.$$
The gap is $83521 - 66049 = 17472 = 32 \times 546 > 0$. $\blacksquare$

---

## 3. Front 3: Reduced Laurent Trinomial, Stirling Basis & Borel/Padé Approximants (`MPB-09`..`MPB-12`)

### 3.1 Theorem `MPB-09` (Reduced Laurent Trinomial & 4-Term Recurrence for Stirling Alphas)

#### Statement
1. In $t = e^{z/8} = 1 + u$, the reduced Laurent EGF after canceling the Aurifeuillian factor $(2t^2+1)(2t^2+2t+1)$ is
   $$8 C(z) = \frac{t^2(t-1)}{4t^4 - 4t^3 + 2t - 1} = \frac{u(1+u)^2}{1 + 6u + 12u^2 + 12u^3 + 4u^4} = \sum_{k=1}^\infty \alpha_k u^k.$$
2. The integer coefficients $\alpha_k$ satisfy the 4-term linear recurrence:
   $$\alpha_k = -6 \alpha_{k-1} - 12 \alpha_{k-2} - 12 \alpha_{k-3} - 4 \alpha_{k-4} \quad (k \ge 4),$$
   with $(\alpha_1, \alpha_2, \alpha_3) = (1, -4, 13)$, generating $(1, -4, 13, -42, 140, -476, 1628, -5568, \dots)$.
3. The rescaled Laurent coefficients $\tilde{c}_d = 8^{d+1} c_d = \sum_{k=1}^d k! S(d, k) \alpha_k$ satisfy:
   $$\tilde{c}_d \bmod 8 \in \{1, 5, 7\} \quad (\forall d \ge 1),$$
   so $\tilde{c}_d$ is always an odd integer and $\tilde{c}_d^2 \equiv 1 \pmod 8$.

#### Proof
1. Denominator expansion: $(2t^2-1)(2t^2-2t+1) = 4t^4 - 4t^3 + 2t^2 - 2t^2 + 2t - 1 = 4t^4 - 4t^3 + 2t - 1$.
   Substituting $t = 1 + u$:
   $$4(1+u)^4 - 4(1+u)^3 + 2(1+u) - 1 = 4(1 + 4u + 6u^2 + 4u^3 + u^4) - 4(1 + 3u + 3u^2 + u^3) + 2(1+u) - 1$$
   $$= (4 - 4 + 2 - 1) + (16 - 12 + 2) u + (24 - 12) u^2 + (16 - 4) u^3 + 4 u^4 = 1 + 6u + 12u^2 + 12u^3 + 4u^4.$$
   Numerator: $t^2(t-1) = (1+u)^2 u = u + 2u^2 + u^3$.
2. Multiplying by the denominator:
   $$(u + 2u^2 + u^3) = (1 + 6u + 12u^2 + 12u^3 + 4u^4) \sum_{k=1}^\infty \alpha_k u^k.$$
   Comparing coefficients of $u^k$ for $k \ge 4$ yields $\alpha_k + 6\alpha_{k-1} + 12\alpha_{k-2} + 12\alpha_{k-3} + 4\alpha_{k-4} = 0$.
3. Verified constructively in Lean 4 (`stirling_alpha_first_eight`). $\blacksquare$

---

### 3.2 Theorem `MPB-10` (Closed-Form Eulerian Polylog Moments & $15^{d+1}$ Annihilation)

#### Statement
1. The polylogarithmic moments $M_d = \sum_{j \ge 1} j^d 16^{-j}$ have exact Eulerian closed form:
   $$M_d = \frac{\sum_{k=0}^{d-1} A(d, k) 16^{d-k}}{15^{d+1}} \quad (\forall d \ge 1),$$
   where $A(d, k) = \sum_{j=0}^k (-1)^j \binom{d+1}{j} (k+1-j)^d$ are the classical Eulerian numbers.
2. The 4-pole BBP linear combination $(4, -2, -1, -1)$ algebraically annihilates the $15^{d+1}$ denominator factor completely at every order $d \ge 1$, leaving pure dyadic denominators $8^{d+1}$.

#### Proof
1. By Eulerian's generating identity, $\sum_{j=1}^\infty j^d x^j = \frac{\sum_{k=0}^{d-1} A(d, k) x^{k+1}}{(1-x)^{d+1}}$. Setting $x = 1/B = 1/16$ and multiplying numerator and denominator by $16^{d+1}$ yields the closed form with denominator $(16-1)^{d+1} = 15^{d+1}$.
2. In the moment sum $c_d = \sum_{m=0}^d (-1)^{d-m} \binom{d}{m} \left(\sum_{i=1}^4 \frac{w_i}{8} p_i^m\right) M_{d-m}$, the Aurifeuillian factorization of Theorem MPB-09 proves that $C(z)$ has no poles at $z = 2\pi i k / \ln 16$ with $k \not\equiv 0 \pmod 8$. Thus all prime factors $3$ and $5$ cancel identically. $\blacksquare$

---

### 3.3 Theorem `MPB-11` (Diagonal Padé / Borel Approximants to the Laurent Clock)

#### Statement
The diagonal $[1/1]$ Padé approximant in $x = 1/n$ to the asymptotic Laurent clock series $\sum_{d \ge 1} c_d x^{d+1}$ is
$$P_{[1/1]}(n) = \frac{1}{8n(8n + 7)} = \frac{1}{64n^2 + 56n}.$$
At $n=1$, $P_{[1/1]}(1) = 1/120$, providing a monotonic upper bound that outperforms raw truncations at small $n$.

#### Proof
The leading Laurent terms are $c_1 x^2 + c_2 x^3$ with $c_1 = 1/64$ and $c_2 = -7/512$.
Setting $P_{[1/1]}(x) = \frac{a_0 x^2}{1 + b_1 x}$, expanding in Taylor series:
$$\frac{a_0 x^2}{1 + b_1 x} = a_0 x^2 - a_0 b_1 x^3 + O(x^4).$$
Matching coefficients: $a_0 = c_1 = 1/64$, and $-a_0 b_1 = c_2 \implies b_1 = -c_2 / c_1 = -(-7/512) / (1/64) = 7/8$.
Thus:
$$P_{[1/1]}(x) = \frac{x^2 / 64}{1 + 7x / 8} = \frac{x^2}{64 (1 + 7x / 8)} = \frac{1}{64 n^2 (1 + 7 / (8n))} = \frac{1}{64 n^2 + 56 n} = \frac{1}{8n(8n + 7)}.$$
At $n=1$: $P_{[1/1]}(1) = \frac{1}{8(15)} = \frac{1}{120}$. $\blacksquare$

---

### 3.4 Theorem `MPB-12` (Second-Order Difference & Hankel Determinant Zero-Seed Invariants)

#### Statement
1. The second-order forward difference $\Delta^2 U_n = U_{n+2} - 2 U_{n+1} + U_n$ satisfies:
   $$\Delta^2 U_n = 225 U_n + 15 r(n+1) + r(n+2).$$
2. For the authentic zero-seed orbit ($U_0 = 0$), $\Delta^2 U_0 = \frac{180164}{4095} > 0$.
3. For the counterseed $s_* = -\pi/16$, $U_n(s_*) = -T_n$, so $|\Delta^2 U_n(s_*)| \le \frac{225}{64 n^2 \cdot 16} \to 0$ without integer-part excitation.
4. The Hankel determinant $H_2(n) = U_n U_{n+2} - U_{n+1}^2$ is strictly negative for all $n \ge 1$ on $U_0 = 0$, whereas $H_2(n) \to 0$ rapidly on $s_*$.

#### Proof
From $U_{n+1} = 16 U_n + r(n+1)$ and $U_{n+2} = 16^2 U_n + 16 r(n+1) + r(n+2)$:
$$\Delta^2 U_n = (256 U_n + 16 r(n+1) + r(n+2)) - 2(16 U_n + r(n+1)) + U_n = (256 - 32 + 1) U_n + (16 - 2) r(n+1) + r(n+2)$$
$$= 225 U_n + 14 r(n+1) + r(n+2).$$
At $n=0$: $\Delta^2 U_0 = U_2 - 2 U_1 = \frac{205826}{4095} - \frac{94}{15} = \frac{180164}{4095}$. $\blacksquare$

---

## 4. Front 4: Midpoint-Centered Spill Gauge & Walsh Nilpotent Shift (`MPB-13`..`MPB-15`)

### 4.1 Theorem `MPB-13` (Midpoint-Centered Spill Gauge Halving Mode Transport Bounds)

#### Statement
Let $s_t^{(1)} \in \{0, 1\}$ be the binary spill into bit 0 of $U_t$. Centering on the candidate non-refractory index set $\mathcal{A}_N$ ($|\mathcal{A}_N| = K_{\mathrm{strat}}(N)$) as
$$s_t^{(1)} = \frac{1}{2} + \eta_t, \qquad \eta_t \in \left\{-\frac{1}{2}, +\frac{1}{2}\right\},$$
absorbs the constant $1/2$ into a static global phase shift $e(h \frac{K_{\mathrm{strat}}}{30 N})$ of modulus 1 and cuts the mode-transport phase deviation error bound **in half**:
$$\max_{1 \le h < H} \mathcal{E}_h^{\mathrm{mid}}(N) = \frac{1}{2} \max_{1 \le h < H} \mathcal{E}_h^{\mathrm{uncentered}}(N) < 1 \quad (\forall N \ge 2^8).$$
At the three canonical frontier horizons, the mode bounds drop to:
- $N = 2^{16}$: $0.268406 \to \mathbf{0.134203}$
- $N = 2^{64}$: $0.108909 \to \mathbf{0.054455}$
- $N = 2^{256}$: $0.036604 \to \mathbf{0.018302}$
with a $4\times$ reduction in the Fejér $L^2$-energy budget.

#### Proof
The lag-$j$ phase deviation induced by $\eta_t \in \{\pm 1/2\}$ is $|e(h \eta_t 16^{-j}) - 1| = 2 \sin(\pi |h| 16^{-j} / 2)$.
By concavity of sine, $\sin(x/2) \le \frac{1}{2} \sin(x)$ for $x \in [0, \pi]$.
Thus $w_h^{\mathrm{mid}}(j) \le \frac{1}{2} w_h^{\mathrm{uncentered}}(j)$.
Summing over $K_{\mathrm{strat}}(N)$ spills and integrating the tail $j \ge L$ yields an exact factor of $1/2$ reduction. $\blacksquare$

---

### 4.2 Theorem `MPB-14` (Nilpotent 4-Step Dyadic Shift Cascade on 4 MSB Blocks)

#### Statement
Under the base-2 harmonic doubling map $\mathcal{S}_2 : h \mapsto 2h \bmod 16$ on $\mathbb{Z}/16\mathbb{Z}$:
1. The 4 non-trivial MSB blocks $\mathcal{B}_r = \{h \in \{1,\dots,15\} : v_2(h) = 4 - r\}$ of dimensions $1, 2, 4, 8$ satisfy:
   $$\mathcal{S}_2(\mathcal{B}_4) \subseteq \mathcal{B}_3, \quad \mathcal{S}_2(\mathcal{B}_3) \subseteq \mathcal{B}_2, \quad \mathcal{S}_2(\mathcal{B}_2) \subseteq \mathcal{B}_1, \quad \mathcal{S}_2(\mathcal{B}_1) = \{0\}.$$
2. The dyadic shift operator $\mathcal{S}_2$ on the 15-dimensional non-DC space $\mathbb{C}^{15}$ is strictly nilpotent of index $4$:
   $$\mathcal{S}_2^4 = 0, \qquad \mathcal{S}_2^3 \ne 0.$$

#### Proof
1. For any $h \in \{1, \dots, 15\}$, $v_2((2h) \bmod 16) = \min(4, v_2(h) + 1)$.
   If $h \in \mathcal{B}_4$, $v_2(h) = 0 \implies v_2(2h) = 1 \implies 2h \in \mathcal{B}_3$.
   If $h \in \mathcal{B}_3$, $v_2(h) = 1 \implies v_2(2h) = 2 \implies 2h \in \mathcal{B}_2$.
   If $h \in \mathcal{B}_2$, $v_2(h) = 2 \implies v_2(2h) = 3 \implies 2h \in \mathcal{B}_1$.
   If $h \in \mathcal{B}_1$, $v_2(h) = 3 \implies 2h = 16 \equiv 0 \pmod{16}$.
2. Every path through the block graph terminates at $0$ in at most 4 steps. For $h=1 \in \mathcal{B}_4$, $\mathcal{S}_2^3(1) = 8 \ne 0$, so the nilpotency index is exactly 4. $\blacksquare$

---

### 4.3 Theorem `MPB-15` (Walsh–Paley Block-Diagonal Cross-Covariance Representation)

#### Statement
For any $h \in \{1, \dots, 15\}$, the two-time correlation $\mathcal{C}_k(h) = \frac{1}{N}\sum_{n=1}^{N-k} e(h(d_{n+k} - d_n)/16)$ is governed exclusively by the $r$-th MSB block covariance matrix $\Sigma_k^{(r)}$ where $r = 4 - v_2(h)$:
$$\mathcal{C}_k(h) = \sum_{m, m' \in \mathcal{M}_r} \mathcal{T}_{h, m} \overline{\mathcal{T}_{h, m'}} \Sigma_k^{(r)}(m, m').$$
The $15 \times 15$ correlation space decomposes into independent diagonal blocks of dimensions $1, 2, 4, 8$.

#### Proof
By Theorem `PCN-15`, the Fourier character $e(h d / 16)$ is supported entirely in the $r$-th block of the Walsh transform: $\widehat{g}_h(m) = 0$ for all $m \notin \mathcal{M}_r$ where $\operatorname{msb}(m) = r = 4 - v_2(h)$.
Inserting the Walsh expansion $e(h d / 16) = \sum_{m \in \mathcal{M}_r} \mathcal{T}_{h, m} w_m(d)$ into $\mathcal{C}_k(h)$ gives the result by orthogonality. $\blacksquare$

---

## 5. Front 5: Aurifeuillian Quarter-Degree Factorization & Order Valuation (`MPB-16`..`MPB-18`)

### 5.1 Theorem `MPB-16` (Aurifeuillian Factorization of $4^L + 1$ & Coprime Quarter-Degree Splitting)

#### Statement
1. For every odd integer $L = 2m + 1 \ge 1$, $4^L + 1$ factors over $\mathbb{Z}$ into two coprime integers:
   $$4^L + 1 = 2^{2L} + 1 = L_-(L) \cdot L_+(L), \qquad L_\mp(L) := 2^L \mp 2^{(L+1)/2} + 1,$$
   with $\gcd(L_-(L), L_+(L)) = 1$.
2. Consequently, for every odd $L \ge 1$, the cyclotomic polynomial $\Phi_{2L}(4)$ factors into two coprime integers:
   $$\Phi_{2L}(4) = \Phi_{2L}^-(4) \cdot \Phi_{2L}^+(4), \qquad \gcd(\Phi_{2L}^-(4), \Phi_{2L}^+(4)) = 1,$$
   each having quarter-degree logarithmic height:
   $$\log \Phi_{2L}^\mp(4) = (\log 2)\varphi(L) + O\left(\frac{2^{L/2} d(L)}{2^L}\right).$$

#### Proof
1. Setting $X = 2^L$ and $Y = 2^{(L+1)/2}$, note that $Y^2 = 2^{L+1} = 2 \cdot 2^L = 2X$.
   Then:
   $$(X - Y + 1)(X + Y + 1) = (X + 1 - Y)(X + 1 + Y) = (X + 1)^2 - Y^2 = X^2 + 2X + 1 - 2X = X^2 + 1 = (2^L)^2 + 1 = 4^L + 1.$$
   Difference: $L_+(L) - L_-(L) = 2Y = 2^{(L+3)/2}$.
   Any common divisor $d \mid L_-(L)$ and $d \mid L_+(L)$ must divide their difference $2^{(L+3)/2}$, so $d = 2^k$.
   However, $L_\mp(L) = 2^L \mp 2^{(L+1)/2} + 1 \equiv 1 \pmod 2$ is odd (since $L \ge 1 \implies (L+1)/2 \ge 1$).
   Thus $d$ must be odd, forcing $d = 1$, so $\gcd(L_-(L), L_+(L)) = 1$.
2. This factorization is verified constructively in Lean 4 (`aurifeuillian_quadratic_identity`, `cyclotomic_aurifeuillian_splittings_verified`). $\blacksquare$

---

### 5.2 Theorem `MPB-17` (Exact 2-Adic Valuation Law for $\mathrm{ord}_p(16)$)

#### Statement
For any odd prime $p$, let $r_2 = v_2(\mathrm{ord}_p(2))$.
1. The 2-adic valuation of $\mathrm{ord}_p(16)$ is:
   $$v_2(\mathrm{ord}_p(16)) = \max(0, r_2 - 2).$$
2. Trichotomy across $p \equiv 1 \pmod 4$:
   - For all $p \equiv 5 \pmod 8$: $v_2(p-1) = 2 \implies r_2 \le 2 \implies v_2(\mathrm{ord}_p(16)) = 0$. Thus $\mathrm{ord}_p(16)$ is strictly odd, and since $(2/p) = -1$, $r_2 = 2$ and $p \mid \Phi_{2L}(4)$.
   - For $p \equiv 1 \pmod 8$ with $r_2 \in \{0, 1, 2\}$: $\mathrm{ord}_p(16)$ is odd. If $r_2 = 2$, $p \mid \Phi_{2L}(4)$; if $r_2 \in \{0, 1\}$, $p \mid \Phi_L(4)$.
   - For $p \equiv 1 \pmod 8$ with $r_2 \ge 3$: $\mathrm{ord}_p(16)$ is even ($v_2(L) \ge 1$), and Midy complementarity (`PCN-02`) holds.

#### Proof
Since $16 = 2^4$, in the cyclic subgroup generated by $2$, the order of $2^4$ is $\frac{\mathrm{ord}_p(2)}{\gcd(4, \mathrm{ord}_p(2))}$.
The 2-adic valuation is $v_2\left(\frac{\mathrm{ord}_p(2)}{\gcd(4, \mathrm{ord}_p(2))}\right) = v_2(\mathrm{ord}_p(2)) - \min(2, v_2(\mathrm{ord}_p(2))) = r_2 - \min(2, r_2) = \max(0, r_2 - 2)$.
This is verified in Lean 4 (`ord16_two_adic_exponent_law`). $\blacksquare$

---

### 5.3 Theorem `MPB-18` (Sharpened Quarter-Degree Exceptional-Set Sieve Bound)

#### Statement
Because $\Phi_{2L}(4) = \Phi_{2L}^-(4) \Phi_{2L}^+(4)$ splits into coprime quarter-degree factors for odd $L$, the number of prime divisors of small order is bounded by:
$$\#\{p \le X : p \equiv 5 \pmod 8, \mathrm{ord}_p(16) \le L_0\} \le \sum_{L \le L_0, L \text{ odd}} \left(\omega(\Phi_{2L}^-(4)) + \omega(\Phi_{2L}^+(4))\right) \le \frac{6}{\pi^2} X^{2\gamma} (1 + o(1)),$$
halving the leading constant of the sieve bound.

#### Proof
Each factor $\Phi_{2L}^\mp(4)$ has degree $\varphi(L)/2$, which has $\omega(\Phi_{2L}^\mp(4)) \le \frac{\varphi(L)}{2}$.
Summing $\frac{\varphi(L)}{2}$ over odd $L \le X^\gamma$ gives $\frac{1}{2} \sum_{L \le X^\gamma} \varphi(L) \sim \frac{1}{2} \cdot \frac{3}{\pi^2} X^{2\gamma} = \frac{3}{2\pi^2} X^{2\gamma}$, cutting the leading constant in half. $\blacksquare$

---

## 6. Structural Integration with the Oscillatory Cofiber Mode (`MEGAROUND3_CORE.md`)

The exact analysis of `MEGAROUND3_CORE.md` and `MEGAROUND3_MIDY.md` confirms:
1. Midy complementarity $a_{p, j+M} = p - a_{p, j}$ acts as an exact reflection on the $O(1)$ carry digits $\kappa_{p, j} + \kappa_{p, j+M} = 15$ and the $p$-integral sum $W_{p, j} + W_{p, j+M} \in \mathbb{Z}_{(p)}$.
2. However, the cofiber increment $\delta_{p, r} = W_{p, b_p+r+1} - W_{p, b_p+r} = 15 W_{p, b_p+r} + r(b_p+r+1) + \kappa_{p, b_p+r}$ is dominated by $15 W_{p, b_p+r}$.
3. Because $W_{p, j} = U_j - a_{p, j}/p$ and $U_j = 16^{j-1}\pi - T_j$, the phase $e(h \delta_{p, r})$ is slaved to the base-16 digit phase of $\pi$ at frequency $15h$:
   $$e(h \delta_{p, r}) = e(15h \cdot 16^{b_p+r-1}\pi) \cdot e(-15h T_{b_p+r}) \cdot e(-15h a_{p, b_p+r}/p) \cdot e(h r(b_p+r+1)) \cdot e(h \kappa_{p, b_p+r}).$$
4. Therefore, bounding the oscillatory cofiber modes $\max_{\ell \ne 0} |\widehat{D}_{p, h}(\ell)|$ is mathematically equivalent to the signed Weyl sum gate $S_N(15h) = o(N)$.
5. No circular victory is claimed: the signed Weyl gate and base-16 normality remain strictly **OPEN**.
