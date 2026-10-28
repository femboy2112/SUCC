# AR-7. The all-rank thread is an EXACT product of odd-prime local characters

**October 27, 2026. Addendum to SUCC #332.** This theorem is the classical CRT/global additive-character product formula, now source-typed for original zero-seeded BBP rational states. It is not π normality, prime-phase independence, or a claim of new scholarly priority.

## AR-7a. Exact arithmetic factorization (PROVED)

Let u=A/B be a reduced rational with B>0 **odd**. For each prime power p^k exactly dividing B, put b_p=B/p^k and let

$$
c_p=[A b_p^{-1}]_{p^k}\in\{0,\ldots,p^k-1\}.
$$

Then the complete **real phase** is exactly the product of local odd-prime phases:

$$
\boxed{\frac AB\equiv\sum_{p^k\parallel B}\frac{c_p}{p^k}\pmod1,\qquad
e(A/B)=\prod_{p^k\parallel B}e(c_p/p^k).}
$$

**Proof:** Multiply the putative phase sum by B. The resulting integer C=Σ b_p c_p has C≡b_p c_p≡A modulo p^k, because every other summand contains p^k. CRT gives C≡A modulo B, so C/B−A/B is integral. Replacing A by hA proves this for **every integer Fourier frequency h**, including negative h. For B=1 the empty product is 1.

Equivalently, with the standard signed local additive character ψ_p(x)=e(−{x}_p), the global rational additive product formula is

$$
\boxed{e_\infty(hu)\prod_{p<\infty}\psi_p(hu)=1.}
$$

**Original BBP source application:** the canceled rational four-pole forcing has odd denominator for every positive integer n; with U_0=0 and U_{n+1}=16U_n+r(n+1), every U_n belongs to Q∩Z₂. Therefore for the authentic rational states,

$$
\boxed{e(hU_n)=\prod_{p\mid \operatorname{den}(U_n)}
e\left(
\frac{[h\,\operatorname{num}(U_n)
(\operatorname{den}(U_n)/p^{k_p})^{-1}]_{p^{k_p}}}{p^{k_p}}
\right).}
$$

The **unscaled** 2-adic additive character is trivial, since U_n∈Z₂. This does not contradict the nontrivial **scaled** p=2 characters ψ₂(U_n/16^k) in the inherited 2-adic clock. The missing real phase is in odd-denominator local characters, precisely the complement exposed by #328/#330.

## AR-7b. The universal adelic seam (CLASSICAL group identity)

On the all-prime solenoid X_all=A_Q/ΔQ, the real lift of a rational number is exactly equivalent to an everywhere-adic representative:

$$
\boxed{j_{\mathbb R}(u)=[(u,0,0,\ldots)]
=[(0,-u,-u,\ldots)]\quad(u\in\mathbb Q).}
$$

Indeed their difference is the diagonal rational adele Δu, which vanishes in the quotient. The all-adic tuple is a valid adele because u∈Z_p for all but finitely many p. Consequently **every actual rational BBP state can be represented with zero real coordinate and a coherent all-prime adic memory**, while the circle alone forgets that memory. This is not an isomorphism between R/Z and sqrt(Z₂).

Caution: at a finite S-solenoid, subtracting a diagonal u directly is legal only when u∈Z[S^{-1}]. For general odd-denominator U_n, use the canonical universal-to-S factor map; truncating the adic tuple naively can miss the excluded-prime correction.

## AR-7c. Finite-rank packets and the noncancellation firewall

For a finite prime subset S, define ω_{p,n}(h) as the exact local phase above. Then

$$
\boxed{e(hU_n)=
\underbrace{\prod_{p\in S}\omega_{p,n}(h)}_{\text{observed}}
\underbrace{\prod_{p\notin S}\omega_{p,n}(h)}_{\text{residual}}.}
$$

A prime-filtered observer must retain the second, generally nontrivial, factor. Choosing S so large it contains every prime in den(U_n) simply reconstructs e(hU_n): this is faithful *representation*, not signed cancellation. The factors are deterministic and correlated through U_n's numerator/denominator and their shared source-time history.

This is consistent with #328's modular character cancellation coexisting with stubborn real phases. The rational nonnormal #320 mutant also admits this product representation, so even perfect local character reconstruction does not establish normality. Source-specific zero-boundary and signed cross-prime cancellation remain load-bearing.

## Executed finite verification

New Python exact sources, tests and a standalone probe are in the same draft branch:
- observational_succ/pi_odd_prime_character.py
- tests/test_pi_odd_prime_character.py
- scripts/pi_odd_prime_character_probe.py

**Six of six focused tests PASS**, including exact CRT products for the first 14 authentic rational U_n across h=−5,−1,0,1,2,7 (84 checked cases), explicit negative and positive rational controls, partial-S residual, p2 typing and factoring-budget mutation. An independent probe repeats all 84 exact source-character/filtered checks.

The number of **distinct odd denominator primes** goes from 2 at n=1 to 20 at n=14 in the observed prefix; no universal or asymptotic growth assertion is made. These finite tests are not the theorem; CRT supplies its universal proof. Full SUCC native suite, provenance and hosted CI remain separate gates.

**Next verdict-changing probe:** derive a nontrivial *signed* estimate for the real average of the authentic low-prime packet S={3,5,7} multiplied by its complementary packet, and falsify it against #320's rational nonnormal source mutant before proposing any normality status upgrade.
