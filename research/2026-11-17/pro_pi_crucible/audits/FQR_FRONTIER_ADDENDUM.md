# Closing FQR frontier audit: valid arithmetic refinements and their limits

**Pin:** `9ff8544c799b5e4c8eb1db33127438bc3f221045`.
**Paper:** `research/2026-11-17/causal_clock_scrambling/FERMAT_QUADRATIC_RECIPROCITY_SELF_DUALITY_AND_RAMIFIED_CARRY.md`.
Paper Git blob: `460495d29d184148ff46ac2ef20b613b0ccd6734`.
Module blob: `beddee1e63137466e6ebd6f46d2b509816556331`.
Test blob: `bf9799c912bcdc6f1954286c8f017dcc5589e18d`.

The paper and the parent-to-commit module/test diff were inspected read-only.
This is same-model paper triangulation, not an external referee report or
confirmation of the author's model identity. The history agent separately
audits the analytic and counterfeit claims.

**Verdict:** credit the valid lane-LCM improvement of EPS and the smaller
carry fiber obtained from a larger actual-survivor inventory. Neither
excludes a low-wall authentic word or proves a signed shell saving.
There are correctable errors in the printed valuation, normalization,
and unqualified top-block equality. The older ANC-12 failure remains.

## 1. FQR-01 through FQR-04

The pairwise denominator GCD identities are correct. Their conclusion
must be v_p(U_N) >= -1, or equivalently that the reduced denominator has
p-exponent at most one. The printed conclusion v_p(U_N) in {-1,0} is
false: U_1 = 47/15 and p = 47 meet the stated hypotheses and have
v_47(U_1) = +1. This does not invalidate the modular principal-part formula.

FQR-02's four local coefficients agree term by term with EPS after the
simple exact rational normalization

\[
F_{N,p}=16\,\mathcal C_{p\bmod8}(p,N).                      \tag{A1}
\]

The modular normalization is consistent because
16^(j_0) = 16 modulo p for j_0 = (p+1)/2. The rational equality (A1) also
follows directly by comparing each of the four coefficient formulas.
Thus the universal collapse is the existing EPS/CG coefficient in a
different normalization. FQR-03 correctly identifies its full packets
with the first BBP partial sum or the negative second BBP partial sum.
The identification with the second published formula is useful, but
does not force nonzero reduction modulo a varying prime or real-circle
cancellation. First-period exceptional-prime classification was already
handled by main's PF-01; extending a fixed table of packets is finite
arithmetic information.

## 2. FQR-05: valid stronger cutoff after correcting the printed F

The paper prints
F = 8*2^(4j_0-4N)*C. This is not EPS's F and makes its displayed
denominator assertion false. At p = 13, N = 8, j_0 = 7, one has
C = 7/32 and K = floor((8N-2)/p) = 4. Its printed F is 7/64, while
the stated denominator bound is 2^floor(K/2)*D_odd(4,1) = 4.
The correct F from (A1) is 7/2, which satisfies the bound.

After that correction, the lane idea is valid. Set

\[
S(K,r)=\{k\le K:k\equiv r\pmod4\}
\cup\{k\le K/2:k\text{ odd}\},\qquad r=p\bmod4,
\]
\[
H(K,r)=2^{\lfloor K/2\rfloor}\operatorname{lcm}S(K,r).
\]

For the two 8j lanes, the odd multiplier k satisfies k = p modulo 4.
The 4j and 2j lanes have k <= K/2. EPS's powers-of-two bound is unchanged.
Therefore den(F) divides H. EPS also proves the uniform sign and size
bound 0 < |F| < 64/15 at every actual nonempty chronological prefix.
Writing F = a/d reduced gives

\[
0<a^2<(4096/225)H(K,r)^2<19H(K,r)^2.
\]

Hence a valid improved finite certificate is

\[
\boxed{p>7,\ p^2>8N,\ p\text{ born},\quad
p^2\ge19H(K,r)^2\ \Longrightarrow\ v_p(U_N)=-1.}            \tag{A2}
\]

For clarity, the lane-LCM asymptotic uses the classical fixed-modulus
prime number theorem. Its first-power prime support is exactly the primes
p <= K with p = r modulo 4, together with the other odd class up to K/2.
Thus their logarithmic weight is (1/2+1/4)K+o(K). Additional prime powers
cost O(sqrt(K) log K) = o(K). It follows that

\[
\log H(K,r)=\left(\tfrac12\log2+\tfrac34+o(1)\right)K.
\]

This proves eventual survival for every born

\[
p\ge A N/\log N,\qquad A>4\log2+6,
\]

using K <= 8N/p and log p = log N+o(log N) at the cutoff. Bounded K
is covered directly by the finite coefficient bound. This is a legitimate
quantitative refinement of EPS's sufficient constant 20 log2. Credit the
new paper for the lane restriction, with the normalization repaired.
The value is sharp for the stated LCM asymptotic; no proof that it is the
optimal possible prime-survival threshold is supplied. The argument is
not self-contained without its classical prime-distribution input, and
it does not improve the known conductor exponent 6 or establish R0.

## 3. FQR-06: a valid smaller fiber, with stronger supplied data

Let X = 16B and let Pi be the product of **all actually surviving** primes
above sqrt(X), each occurring once in Q = den(U_(2B)); the harmless
small-prime threshold max(6,floor(sqrt(X))) matters only for small B.
Put q = Q/Pi. Then all prime factors of q lie below sqrt(X) eventually.
Since Q divides the native odd LCM, an elementary bound avoids even PNT:

\[
\begin{aligned}
\log q
&\le\sum_{a\ge1}\vartheta\big(\min(\sqrt X,X^{1/a})\big)\\
&\le\log4\left(2\sqrt X+
X^{1/3}\lfloor\log_2X\rfloor\right)
=O(\sqrt X).
\end{aligned}                                               \tag{A3}
\]

Here theta(y) <= y log4 follows from the elementary LCM bound. Thus
q = exp(O(sqrt(B))) is valid. It does **not** assert that all born primes
above sqrt(X) survive: the inventory is selected using actual nonzero
principal parts (or the already computed reduced denominator).

Let R_0 = N mod Pi, A_U = U_(2B) mod16^B, and set
Z = q A_U - R_0/Pi modulo 16^B. The master congruence is

\[
qC+t\equiv Z\pmod{16^B},\qquad 0\le t<q.
\]

This is precisely M-02 multiplied by q. The full reduced-denominator-Q
signature has exactly phi(q) admissible words eventually, since q<16^B
and the progression in t is injective. This improves the cardinality
bound from exp(O(B/log B)) to exp(O(sqrt B)) **when the larger inventory
is supplied**. EPS instead guarantees survival from the native inventory
above an explicit cutoff without presupposing the entire survivor set.

The reduction is useful finite arithmetic. It does not show that the
authentic word avoids the low-domain-wall subset. In particular, neither
the exact scalar Z nor any positive wall density of it is bounded here.
The scaled word qC is not the target C; multiplication by the changing
odd integer q has no supplied domain-wall coercivity theorem.

## 4. FQR-07: the top-block equation needs modular wrap

Write K = 16^B, H = 16^L, X_0 = (qC) mod K, with t<q<=H. Then
Z = (X_0+t) mod K gives the correct identity

\[
\left\lfloor Z/H\right\rfloor
\equiv\left\lfloor X_0/H\right\rfloor+\epsilon
\pmod{K/H},\qquad
\epsilon=\left\lfloor\frac{(X_0\bmod H)+t}{H}\right\rfloor\in\{0,1\}.
                                                               \tag{A4}
\]

Ordinary equality, as printed, needs an additional no-wrap assertion.
For an exact demonstration that the arithmetic inference alone does not
supply it, take B=2, q=15, Pi=7 and U=1793/105=17+8/105. Then
R_0=1, t=1, X_0=255, Z=0, H=16: top(Z)=0 while top(X_0)=15.
This is a comparison rational, **not an authentic-source counterexample**.
A bounded authentic probe B=1,...,32 found no wrap witness. Therefore
the audited status is an unproved all-B no-wrap assertion, not a proved
failure on the original source.

The cyclic version still has the stated domain-wall stability under a
single increment: the full wrap changes all F digits to all 0 digits,
both of energy zero. This repair preserves the auxiliary scaled-word
comparison, not a coercive estimate on C.

## 5. Persistence, scope, and actual receipts

The commit appends to the prior module and tests; the original
`construct_adelic_crt_shadow` remains unchanged. Its B=3 reduced-denominator
counterexample remains valid. The earlier ANC all-B fitting assertion is
not repaired by these new results. The history audit separately records
the continuing analytic errors and the incorrect claims to refute prior
countermodels merely by adding hypotheses they never satisfied.

No upstream 25-test suite or broad gate was replayed. The sole new run was

`timeout 10s python minimal_arithmetic_probe.py`

in `prime_scratch/fqr_frontier`; exit 0. It records the exact FQR-01 and
printed-normalization witnesses and the bounded authentic wrap check.
Every corrected modular identity in that finite check passed.

Artifacts:

- `fqr_frontier/extraction_receipt.json`: pinned blobs and SHA256 hashes;
- `fqr_frontier/minimal_arithmetic_probe.py`: actual small probe;
- `fqr_frontier/minimal_arithmetic_receipt.json`: raw exact results.

**Claim boundary:** corrected A2 and A3 are proved quantitative arithmetic;
the current branch supplies no new exclusion of the authentic asymptotic
low-wall failure mode. No D/E promotion follows. Terminal coercivity,
original-source R0, swept convergence, and full base-16 normality remain
open.
