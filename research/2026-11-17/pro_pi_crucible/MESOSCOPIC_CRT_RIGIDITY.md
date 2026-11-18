# Mesoscopic prime inventory, 2-adic signature, and terminal-word rigidity

**Status:** exact finite algebra plus an eventual consequence of EPS-01.
This is auxiliary source arithmetic, not a proof of terminal coercivity,
R0, or normality. It does not exclude the authentic word from any
low-domain-wall language. Finite calibration is recorded separately below.

## 1. Authenticated inventory and a small remaining cofactor

Keep the original four-pole source and literal seed U_0 = 0. Write
U_n = N_n/Q_n in lowest terms, Q_n > 0, and define the native odd LCM

\[
\Lambda_n=\operatorname{lcm}\{2j-1,4j-1,8j-7,8j-3:1\le j\le n\}.
\]

The four summands show Q_n divides 2*Lambda_n; the combined source
identity shows Q_n is odd, hence Q_n divides Lambda_n.
A prime is born by n precisely when it divides Lambda_n. For a real Y
satisfying

\[
Y\ge\max(7,\sqrt{8n}),\qquad
Y^2\ge19\,32^{8n/Y},                                      \tag{M1}
\]

put

\[
\Pi_n(Y)=\prod_{\substack{p>Y\text{ prime}\\p\mid\Lambda_n}}p,
\qquad q_n(Y)=Q_n/\Pi_n(Y).
\]

**Lemma M-01.** The quotient q_n(Y) is a positive odd integer,
gcd(Pi_n(Y),q_n(Y)) = 1, and

\[
\log q_n(Y)\le Y\log4+\sqrt{8n}\log(8n).                   \tag{M2}
\]

**Proof.** EPS-01 says a born p > 7 with p^2 > 8n and
p^2 >= 19*32^K, K = floor((8n-2)/p), has v_p(U_n) = -1.
For p > Y, all these hypotheses follow from (M1), since
K <= 8n/Y. Also p^2 > 8n, so p occurs to first power in Lambda_n.
Every born prime above Y therefore occurs exactly once in Q_n and Pi_n(Y).
No prime above Y remains in q_n(Y).

Since Q_n divides Lambda_n, the contribution of the first power of primes
p <= Y to log q_n(Y) is bounded by
log lcm(1,...,floor(Y)) <= Y log4. The elementary LCM bound is proved in
the EPS manuscript. Any additional powers can occur only at
p <= sqrt(8n); each such prime contributes at most log(8n), and there
are at most sqrt(8n) of them. This gives (M2), without a prime number
theorem. The statements about parity and coprimality follow as well. QED.

For any fixed A > 20 log2, take Y_n = A n/log n. For all sufficiently
large n, (M1) holds: the logarithmic comparison is

\[
2\log Y_n-\log19-\frac{8n}{Y_n}\log32
=\left(2-\frac{40\log2}{A}\right)\log n
 -2\log\log n+2\log A-\log19\longrightarrow+\infty.
\]

Consequently,

\[
\log q_n(Y_n)=O(n/\log n).                                 \tag{M3}
\]

## 2. Finite signature and the complete set of terminal words

The following is an all-rational finite statement. Fix B >= 1 and a
reduced rational U = N/Q with Q odd. Let Pi be a squarefree divisor
of Q such that q = Q/Pi is coprime to Pi. Set K = 16^B. Define

\[
A_U=[NQ^{-1}]_K\in\{0,\ldots,K-1\},\qquad
R_0=[N]_{\Pi}\in\{0,\ldots,\Pi-1\}.
\]

For Pi = 1, use R_0 = 0. All inverses modulo K exist because Q and q
are odd. The **finite signature** consists of:

- the reduced denominator Q;
- the 2-adic residue A_U modulo K;
- for each p dividing Pi, the principal part [pU]_p. Here pU is p-integral,
  since v_p(Q) = 1, and [pU]_p means its rational reduction modulo p.

For a rational V, its terminal word is the integer
[floor(V)]_K, encoding its last B hexadecimal digits.

**Theorem M-02.** Every V with exactly this signature has a unique
fractional numerator

\[
\{V\}=\frac{R_0+t\Pi}{Q},\qquad 0\le t<q,
\qquad \gcd(R_0+t\Pi,q)=1.                                \tag{M4}
\]

Its terminal word is

\[
W_t=\left[A_U-Q^{-1}R_0-q^{-1}t\right]_K.                  \tag{M5}
\]

Conversely, every t satisfying (M4) gives such a rational V by taking
any integer C congruent to W_t modulo K and setting V = C+(R_0+tPi)/Q.
Thus these formulas characterize the entire set, not merely a necessary
condition.

There are exactly q raw values of t before the coprimality restriction
and exactly phi(q) admissible values. If q <= K, all q raw words W_t
are distinct, so the number of admissible terminal words is exactly phi(q)
and at most q.

**Proof.** Write V = C+R/Q in reduced-denominator-Q form, with C an integer,
0 <= R < Q and gcd(R,Q) = 1. For p dividing Pi, equality of principal
parts means p(V-U) belongs to p Z_(p), equivalently V-U is p-integral.
Since v_p(Q) = 1, this is equivalent to R = N modulo p. Combining the
distinct primes gives R = N modulo Pi, hence uniquely R = R_0+tPi with
0 <= t < q. Because gcd(R_0,Pi) = 1, reduced denominator Q is equivalent
to gcd(R_0+tPi,q) = 1.

The 2-adic congruence V = U modulo K Z_(2) now gives

\[
C\equiv A_U-Q^{-1}(R_0+t\Pi)
 \equiv A_U-Q^{-1}R_0-q^{-1}t\pmod K,
\]

which is (M5). Reversing these computations proves sufficiency.
Because Pi is a unit modulo q, the q integers R_0+tPi run through every
residue modulo q exactly once. Exactly phi(q) are units. Finally,
W_t = W_s implies t = s modulo K, because q is a unit modulo K.
When 0 <= t,s < q <= K, this implies t = s as integers. QED.

## 3. Source-specific eventual consequence and the precise limitation

**Theorem M-03.** Apply M-02 to U = U_(2B) with Pi = Pi_(2B)(Y_(2B)), where A > 20 log2
was fixed in section 1. By (M3),

\[
q=\exp(O(B/\log B))<16^B
\quad\text{for every sufficiently large }B.                \tag{M6}
\]

Therefore the authentic denominator, its 2-adic shell residue, and
**every born prime principal part above the effective threshold** permit
exactly phi(q) terminal words, contained in the q-term progression (M5).
Their number is at most exp(O(B/log B)). This couples the large-prime
arithmetic inventory to possible integer winding words. Its inventory contains ANC-12's uncollided bands eventually, together
with any other born primes above Y; the proof requires no assertion of
strict containment.

In this q <= K regime, the zero word is possible exactly when the unique residue

\[
t_0=\left[qA_U-\Pi^{-1}R_0\right]_K                       \tag{M7}
\]

satisfies t_0 < q and gcd(R_0+t_0 Pi,q) = 1. This is a necessary and
sufficient finite test, not an assertion that the test fails for the
authentic source. The authentic terminal word always belongs to the set.
No estimate here determines whether that word has many nonextreme digits
or 0/F transitions.

The eventual repaired ANC-12 construction relied on
Q/(16^B Pi) = q/16^B growing exponentially for its **small** selected
inventory. For the mesoscopic inventory here, q/16^B tends to zero.
Its multiple-candidate sieve inside one fractional unit interval is
therefore unavailable: the simultaneous numerator modulus 16^B Pi is
larger than Q eventually. This does not prove that no zero-word clone
exists; (M7) gives the remaining exact possibility. It only disproves
any reading of ANC-12 as granting arbitrary terminal-word freedom while
preserving an arbitrarily extensive authenticated prime inventory.

**Dependencies.** EPS-01 and its elementary LCM lemma are in
`EFFECTIVE_PRIME_SURVIVAL.md`. The source is unchanged throughout M-01
and M-03. The terminal shadows of M-02 are comparison rationals, with no
claim of an original-source chronological realization. This appendix
uses no imported asymptotic prime theorem.

## 4. Exact finite calibration and its boundary

The standalone crt_signature_probe.py checks the complete classification
on four predeclared cases. Three small denominators are also enumerated
directly over every fractional numerator and integer residue, without
using the progression to select the candidates. They cover q=1, q<K,
and q>K. In the last case, 16 admissible parameters give only 15 words,
confirming why the injectivity hypothesis cannot be dropped.

For the literal U_6, selecting every denominator prime above 7 gives
Q=24536311574775, Pi=46735831571, q=525. There are exactly 240 admissible
words, including the zero word at t=215. This is a finite M-02 check;
Y=7 at n=6 is not asserted to satisfy the EPS cutoff. No universal
low-wall exclusion can be inferred from this finite example.

The executed receipt and raw output are evidence/crt_signature_probe.json
and evidence/crt_signature_probe.stdout.json. These checks calibrate the
finite algebra. The paper proof, not enumeration, supplies the quantifiers.

## 5. Closing-frontier refinement: the actual simple-prime inventory

The newly inspected FQR-06/07 at commit
9ff8544c799b5e4c8eb1db33127438bc3f221045 observes a stronger cofactor-size
bound when the supplied inventory includes every ACTUALLY SURVIVING prime
above the square-root cutoff. Credit for that inventory choice and its
ramified-carry formula belongs to that source. Applying M-02 makes its
primitive-word count exact. The following proof also avoids a prime-number
theorem for the cofactor size.

**Corollary M-04.** For B>=3 set X=16B, U_(2B)=N/Q, and

\[
\Pi^{\rm simple}=\prod_{\substack{p>\sqrt X\\p\mid Q}}p,
\qquad q^{\rm ram}=Q/\Pi^{\rm simple}.
\]

Then Pi is squarefree, gcd(Pi,q)=1, and

\[
\log q^{\rm ram}\le\log4\left(2\sqrt X+
X^{1/3}\lfloor\log_2 X\rfloor\right)=O(\sqrt B).
\]

Consequently, preserving Q, its residue modulo 16^B, and the principal
parts for all these actually surviving primes allows exactly phi(q^ram)
terminal words for all sufficiently large B, and at most exp(O(sqrt B)).
They are precisely the M-02 progression with this choice of Pi and q.
The zero-word criterion remains conditional, with q<=16^B required.

**Proof.** Q divides the native LCM, whose individual factors are <=X.
No p>sqrt X can occur to a second power. All prime factors of q are <=sqrt X,
and v_p(q)<=floor(log X/log p). Write theta(t)=sum_(p<=t)log p. The elementary
LCM bound gives theta(t)<=t log4. Summing the prime powers therefore yields

\[
\begin{aligned}
\log q
&\le\sum_{a=1}^{\lfloor\log_2 X\rfloor}
\vartheta\big(\min\{\sqrt X,X^{1/a}\}\big)\\
&\le\log4\left(2\sqrt X+
X^{1/3}\lfloor\log_2 X\rfloor\right).
\end{aligned}
\]

The second term is o(sqrt X). Thus q<16^B eventually, and M-02 proves
the exact count and classification. QED.

This is not a theorem that every born prime above sqrt X survives. Actual
cancellation information is part of the enlarged inventory. EPS instead
certifies survival from birth data above its n/log n cutoff. These are
different input contracts. Neither count excludes low-wall words, controls
the authentic parameter t, or transfers wall energy through multiplication
by q. The valid FQR congruence q C+t=Z modulo 16^B is the same classification
after multiplication by q; it is not a signed cancellation estimate.
