# Final hostile audit: mesoscopic CRT rigidity and eventual ANC-12 repair

**Authority:** same-model paper audit plus one separately recomputed exact
B=3 witness. This is not an external independent witness, a formal proof,
or a replay of a broad test suite. No repository file was changed.

## Inputs and pins

- `prime_scratch/MESOSCOPIC_CRT_RIGIDITY.md`, SHA-256
  `dc6189907f03af7ee89b7aa473d634e0331eb99100621380d8f13721cc439718`.
- `prime_scratch/ANC12_EVENTUAL_REPAIR.md`, SHA-256
  `d0db9002a86e14553ec78fcba9544edb549d93e2594273f2ecae2b13047e7459`.
- Imported CG-01 reread at main
  `81be6b897ae980b801a3b9de9e22ef81e8360bfb`,
  `research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md`.
- ANC-07 bands and ANC-12 claim reread at
  `97c7433371feca631991a1b8227b656e92e4abcb`,
  `research/2026-11-17/causal_clock_scrambling/ADELIC_BBP_NULL_SEED_AND_NORMALITY_CRUCIBLE.md`.

## Verdict

No fatal algebraic, sign, counting, cutoff, or asymptotic-transfer error was
found in either appendix as scoped. Their conclusions concern finite
rational terminal signatures. They do not establish authentic domain-wall
coercivity or signed phase cancellation. All four original-source targets
remain OPEN.

## Finite classification

For reduced N/Q, require Q>0 odd, Pi a positive squarefree divisor of Q,
and gcd(Pi,Q/Pi)=1. These hypotheses ensure v_p(Q)=1 for p dividing Pi
and make both q=Q/Pi and Pi invertible modulo K=16^B.

Equality of the principal parts is exactly R=N modulo Pi. The q possible
fractional numerators are uniquely R=R_0+t Pi, 0<=t<q. Because Pi is a unit
modulo q, these traverse every class modulo q once. Exactly phi(q) are
coprime to Q, including the standard phi(1)=1 convention.

The word formula

`W_t = [A_U - Q^(-1) R_0 - q^(-1)t]_K`

and its converse are exact. If q<=K, equality of two words implies
t=s modulo K and therefore t=s as ordinary integers; the admissible word
count is exactly phi(q). Negative integer parts cause no problem because
the word is defined by reduction of the floor modulo K.

**Scope clarification:** the single-residue zero-word test (M7) must retain
q<=K, which is already furnished by the eventual application immediately
before it. It is false if quoted for unrestricted q>K. For example,
B=1, Q=q=17, Pi=1, U=16/17 has a zero word. Its t_0=0 fails coprimality,
but the admissible t=16 produces that word. For arbitrary q the correct
test is existence of t in [0,q) congruent to t_0 modulo K and coprime as
specified. Adding “in this q<K regime” before (M7) makes its scope explicit.

## Source cutoff and residual cofactor

The original signed terms give Q_n dividing 2 Lambda_n, and the combined
source identity makes Q_n odd; hence Q_n divides Lambda_n. Under (M1),
every born p>Y satisfies all EPS-01 hypotheses, occurs to first power in
Lambda_n, and survives to first power in Q_n. Thus q_n(Y) is integral,
coprime to Pi_n(Y), and contains only primes <=Y.

The first prime powers cost at most Y log 4. Additional powers are confined
to p<=sqrt(8n) and cost at most sqrt(8n) log(8n), as claimed. For fixed
A>20 log 2, the coefficient of log n in the displayed threshold comparison
is positive. Y_n=A n/log n eventually exceeds both 7 and sqrt(8n), and
sqrt(n) log n=o(n/log n). Consequently log q_n(Y_n)=O(n/log n), and at
n=2B one has q<16^B eventually. No PNT is needed for these steps.

The mesoscopic inventory eventually contains all ANC-07 selected bands
because Y_n<8n/3 eventually. If the word “strictly” is retained, one may
justify the extra prime by elementary Bertrand: eventually a prime between
Y_n and 2Y_n lies below 2n-1, hence is born via 2j-1 and lies below the
ANC-07 bands. Alternatively say simply that the inventory contains those
bands; the classification does not require strict containment.

## Primitive sieve and eventual repair

The finite inclusion-exclusion estimate

`A_L >= L phi(q)/q - 2^omega(q)`

is valid: every squarefree-divisor congruence has one progression class,
and its count differs from L/d by less than one. The coarse bound
phi(q)/q>=2^(-omega(q)) makes L>4^omega(q) sufficient. LM<=Q puts every
candidate R_0+tM strictly below Q. Coprimality then preserves the entire
reduced denominator, while C_0 divisible by 16^B gives the claimed 2-adic
agreement and all-zero terminal word. The norm is exactly

`(R/Q)^2 (1-256^(-B))/(255B)`.

The ANC-07 band endpoints and residue classes are correctly copied.
The first band has logarithmic prime weight 2n+o(n), and the second has
(2/3)n+o(n), by the imported fixed-modulus PNT. CG-01 supplies the essential
matching denominator asymptotic 6n+o(n). At n=2B these give
log q_B=(20/3)B+o(B), and the available progression length has logarithm
((20/3)-log16)B+o(B), with positive coefficient.

The elementary q_B>=(w+1)! argument, its split at w=sqrt(B), and the bound
w<=56B/log B in the large branch are correct. Therefore
log(4^w+1)=o(B), so the sufficient finite-sieve condition holds for every
sufficiently large B. The result is eventual with an unspecified B_0;
neither appendix upgrades it to every B>=2.

## Separate exact B=3 recomputation

A fresh Python `Fraction` calculation directly iterated all four signed
source terms through n=6 and recomputed the proposed clone. It returned:

- N=80827484660698633414, Q=24536311574775;
- Pi=19224941, q=1276275, original R_0=67379365062;
- gcd(R_0,Q)=3, C_0=3293184;
- repaired R=146124723398, gcd(R,Q)=1;
- V=80802588843188556998/24536311574775;
- norm=1286484195985556022150841/27748343886818929373062103040000;
- authentic and repaired 2-adic residue 1514 modulo 4096;
- matching principal parts 11,11,5,21,4 for primes 19,23,29,37,41.

These match the appendix exactly. No other finite cases or broad tests
were executed in this final review.

## Remaining gap

The expanded source signature restricts its possible terminal words to a
subexponential explicit modular progression. It does not prove that the
authentic word avoids low-domain-wall subsets of that progression. The
small-inventory sieve repair supplies comparison rationals, not another
trajectory with the same authenticated infinite forcing and zero seed.
Neither statement supplies the remaining all-late-shell arithmetic saving.
