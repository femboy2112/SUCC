# PG-09 — zero-selected prime-birth windows cannot cancel **exactly**

**2026-11-02; research-only additive source-specific theorem.** This uses the authentic original signed BBP poles, literal U_0=0, and cyclotomic fields. The original first-pole prime-birth arithmetic is inherited from SUCC; this new specialization is a narrowly scoped **strict nonzero signed-window statement**, NOT a useful asymptotic lower bound. The condition that the last endpoint is a first-time new prime is crucial.

Let p=8b−7 be any prime greater than 5 (so p≡1 mod8, b=(p+7)/8≥2). Original
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
For every i<b, every denominator in r(i) is <p; hence p does not divide the reduced denominator of U_i. At the **single first birth** at b,
\[
\boxed{U_b=\frac4p+B_b,\qquad
 B_b=16U_{b-1}-\frac2{p+3}-\frac1{p+4}-\frac1{p+5},
 \qquad p\nmid\operatorname{den}(B_b).}
\]
The last condition uses p>5, so p does not divide p+3,p+4,p+5. In particular, v_p(U_b)=−1, while v_p(U_i)≥0 for every 0≤i<b.

Fix integer h with p∤h. For ANY finite rational coefficients a_i (i≤b) satisfying a_b≠0, set
\[
Z=\sum_{i=0}^{b}a_i e(hU_i).
\]
Let M be the least common multiple of the reduced denominators of all U_i (i<b) and of B_b, after harmless multiplication by h. Then p∤M. The field K=Q(ζ_M) contains all the earlier phases and e(h B_b), while
\[
e(h U_b)=e(h B_b)\,\zeta_p^{4h}.
\]
Since p∤M, the cyclotomic compositum Q(ζ_M,ζ_p)=Q(ζ_{Mp}) has degree p−1 over K, so the primitive ζ_p^{4h} does NOT belong to K. If Z=0, division by a_b e(hB_b)∈K^\times would put ζ_p^{4h} in K, contradiction. Therefore
\[
\boxed{\sum_{i=0}^{b}a_i e(hU_i)\neq0\quad\text{for all rational }a_b\neq0,\ p\nmid h.}\tag{PG-09}
\]

In particular **every** signed adjacent-window Haar difference A−B whose last observed time is b, with coefficient ±1 on that last phase and all earlier indices below b, is STRICTLY nonzero for every h not divisible by the newborn p. Also S_b(h)≠0. Dirichlet's theorem on primes p≡1 (mod 8) supplies infinitely many such certified endpoints for each fixed nonzero h.

**Boundary:** nonzero algebraic amplitude is not a positive constant or power-saving bound. The field degree and denominators grow; this theorem alone gives no scale-useful W_j/E_j separation or D_J(h) divergence. It also doesn't establish that infinitely many such birth endpoints align with the canonical dyadic nodes used in GS-04. Cyclotomic Galois averaging can give an unrelated large mean-square while the selected embedding remains nearly coherent. The result is **seed-specific to rational initial state and the exact source passport**, excluding the coherent same-source real counterseed s=1/5−π/16 from its cyclotomic assumptions, but it is NOT a proof of π-normality.

**Verification:** exact Fraction r,U_n and p-adic reduced denominator checks at p=17,41,73,89,97,113,137,193,233,241 and no floats for the universal field argument. Attribution: elementary cyclotomic compositum and the existing SUCC first-pole prime-birth mechanism; no independent academic priority claimed.
