# DY-11 — exact prime survival, not just dyadic exposure

**Status: DISCLOSED (classical theorem + elementary corollaries); finite tests OBSERVED.** This advances the weaker necessary prime-exposure statement in the sibling README to a complete denominator classification. Nothing here is a theorem about BBP's actual digit orbit.

## 1. Full denominator theorem

For every even integer m>=2, write \(B_m\) for the Bernoulli number with the standard generating convention, and \(\zeta(1-m)=-B_m/m\). Two separate classical results are required:

1. The von Staudt–Clausen theorem: \(\operatorname{den}(B_m)=\prod_{p-1\mid m}p\), squarefree.
2. Von Staudt's **second** theorem: a prime p divides the reduced denominator of \(B_m/m\) if and only if p divides the reduced denominator of \(B_m\). The second theorem is necessary because naively dividing by m might introduce new prime denominators when p divides m but p-1 does not divide m.

If p-1 divides m, the first theorem gives \(v_p(B_m)=-1\), hence \(v_p(B_m/m)=-1-v_p(m)\). If p-1 does not divide m, the second theorem gives \(v_p(B_m/m)\ge0\).

Therefore the COMPLETE reduced denominator, including prime-power multiplicities, is

\[
\boxed{\operatorname{den}(\zeta(1-m))
=\prod_{\substack{p\ \mathrm{prime}\\p-1\mid m}}p^{1+v_p(m)}
\quad\text{for even }m\ge2.}\tag{DY-11}
\]

For m=2 this is 2²*3=12; for m=4 it is 2³*3*5=120; for m=6 it is 2²*3²*7=252; for m=8 it is 2⁴*3*5=240; for m=10 it is 2²*3*11=132; for m=12 it is 2³*3²*5*7*13=32760; for m=16 it is 2⁵*3*5*17=8160.

Thus p appears among reduced negative-odd-zeta denominator primes at **exactly** the even levels m divisible by p-1; its exponent at such a level is fixed by 1+v_p(m). The first occurrence is m=p-1, equivalently zeta(2-p).

This theorem is old mathematics. Its value to SUCC is the **complete and falsifiable prime-survival interface** between the finite Stirling numerator and the analytic continuation.

## 2. Exact Stirling numerator p-adic cancellation law

The independent finite Stirling–Pascal identity from README is

\[
\eta(1-m)=\frac{C_{m-1}}{2^m},
\qquad
\zeta(1-m)=-\frac{C_{m-1}}{2^m(2^m-1)}.
\]

For any **odd** prime p and even m>=2, 2 is a p-adic unit, so the following identity is unconditional:

\[
v_p(C_{m-1})=v_p(2^m-1)+v_p(\zeta(1-m)).
\]

Insert DY-11. We obtain a precise cancellation theorem for the integer constructed by finite Stirling partitions:

\[
\boxed{
v_p(C_{m-1})=
\begin{cases}
v_p(2^m-1)-1-v_p(m),&p-1\mid m,\\
\ge v_p(2^m-1),&p-1\nmid m.
\end{cases}}\tag{DY-12}
\]

In the second case, the dyadically exposed prime is completely cancelled from the continued zeta denominator. In the first case, it survives with the *exact* Bernoulli/von Staudt multiplicity. The first line is compatible with integrality of C because Fermat's theorem plus lifting the exponent yields \(v_p(2^m-1)\ge1+v_p(m)\) for odd p when p-1 divides m.

**Counterexamples to exposure = survival:** at m=8, p=17 has ord_17(2)=8, so 17 divides 2^8-1, but p-1=16 does not divide 8: the finite Stirling numerator C_7=-272=-16*17 cancels that 17. At m=10, 31 divides 2^10-1, but p-1=30 does not divide 10: the numerator C_9=7936=256*31 cancels it. Conversely the first 17 denominator occurrence is m=16, not m=8.

**Interpretation:** parity/dyadic continuation provides an **exposure clock** (multiplicative order of 2 mod p). Bernoulli/von Staudt arithmetic applies a stronger, independent **survival rule** (p-1 divides the index). Their exact intersection produces the negative-odd-zeta denominator spectrum. This is the precise replacement for a conjectural consecutive-prime-production story.

## 3. Proof provenance and an unexpected historical echo

A primary mathematical exposition is J. Milnor and J. Stasheff, *Characteristic Classes*, Appendix B, pp. 289–290, Theorems B.3 and B.4, including a proof of the second theorem:

https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/milnor-stasheff2.pdf

The B.4 argument uses a primitive root modulo p to rule out denominator primes when p-1 does not divide the index. This is not derivable from von Staudt–Clausen's *squarefree denominator of B_m alone* without the extra integrality step. Compare NIST DLMF §24.10.

That same Appendix B relates Bernoulli denominators to homotopy-theoretic stable J-homomorphisms, offering an honest arithmetic/topological research interface. It does **not** identify SUCC's BBP circle holonomy with this topological J-homomorphism; that would require additional construction and proof.

## 4. Fresh exact rational probe and scope

Run:

~~~sh
python research/2026-10-30/dyadic_zeta_prime_exposure/denominator_survival_probe.py
~~~

Observed local run: **3/3 unittest methods PASS**, using exact Fractions, independently computing the Bernoulli triangle and Stirling numerator through every even m=2..100, prime factorizations through 101, exact surviving/exposed valuations, and first appearance at each odd prime through 101. All 50 even indices matched DY-11. This finite test does not prove the unbounded classical theorem, and it is not a blind independent referee.

**Next source-aware probe:** transport the fully resolved DY-12 prime cancellation data into a *declared* original four-pole BBP first-jet and literal zero-seed observer, then compare the same-source coherent counterseed and #421's entire-remainder shadow. Matching negative zeta denominator spectra on both is evidence of observer insufficiency, not of pi normality.
