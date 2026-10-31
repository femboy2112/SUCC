# Complete Gauss units still do not identify the authentic source

**Status:** locally proved identities and obstructions, with exact finite
calibration. No new Lean theorem, external referee, or scholarly-priority
claim. The original BBP coefficients and zero seed remain unchanged.
This dossier uses the positive mutant only as a typed source-identification
counterexample. It makes no normality assertion about that mutant.

## GG-01: an exact all-prime kernel of the complete weighted Gauss product

Let p be any odd prime, f=ord_8(p), q=p^f, and choose a multiplicative
character chi of exact order eight on F_q. Extend nontrivial characters
by zero at zero. Choose a nontrivial additive character psi, and put

\[
 G_d=\sum_{x\in\mathbb F_q}\chi(x)^d\psi(x),\qquad
 A_p(c)=G_1^{c_1}G_4^{c_4}G_5^{c_5}G_6^{c_6}.
\]

All seven nontrivial Gauss sums are nonzero, so integer negative powers
are legitimate. Write c=(4,-2,-1,-1), e=(1,-3,1,1). Then, for **every
integer t**, not just for a tested list of primes,

\[
 \boxed{\frac{A_p(c+te)}{A_p(c)}=\chi(2)^{2t}.}\tag{GG1}
\]

In these fields 2 is a square, so chi(2)^2 belongs to {1,-1}. Consequently

\[
 \boxed{A_p(c+te)=A_p(c)\quad\text{for every odd p and every even t}.}\tag{GG2}
\]

This is equality of the **complete algebraic Gauss products**, including
their units, signs and root-of-unity factors. It strictly strengthens the
parent's age/valuation-only nonidentifiability result.

**Proof with the quadratic multiplication identity reconstructed.** Let
phi be the quadratic character and B a character such that B, B^2 and
B phi are nontrivial. For Jacobi sums J, counting square roots gives

\[
\begin{aligned}
 J(B,\phi)
 &=\sum_y B(1-y^2)-\sum_x B(x)\\
 &=B(4)\sum_tB(t)B(1-t)=B(4)J(B,B).
\end{aligned}
\]

The substitution in the second line is y=1-2t; the discarded character
sum is zero. The elementary identity
G(B)G(C)=J(B,C)G(BC), when BC is nontrivial, follows by grouping the
double sum by x+y and changing variables. Apply it twice to obtain

\[
 G(B)G(B\phi)=B(4)^{-1}G(B^2)G(\phi).
\]

For B=chi and B=chi^2 all the stated nontriviality conditions hold.
Since phi=chi^4, multiplication yields

\[
 G_1G_5=\chi(4)^{-1}G_2G_4,\qquad
 G_2G_6=\chi(4)^{-2}G_4^2,
\]

and hence

\[
 \frac{G_1G_5G_6}{G_4^3}
 =\chi(4)^{-3}=\chi(2)^{-6}=\chi(2)^2.
\]

If f=1, p=1 mod8 and the quadratic supplementary law says 2 is a
square in F_p. If f=2, every nonzero element of F_p is a square in
F_(p^2). Thus chi(2)^4=1. Taking the t-th power proves both claims. ∎

The proof is the quadratic Davenport-Hasse multiplication formula,
reconstructed here to check its sign and applicability over F_(p^2).
It is not a new proof of the classical formula. Changing the primitive
order-eight character or replacing psi(x) by psi(ax) does not remove
the even-t blindness. In the latter case each G_d gains chi(a)^(-d),
and the mutation has sum(delta*e_delta)=0.

## GG-02: exact GK units and the combined all-horizon counterexample

Fix a primitive element g of F_q. In the complex cyclotomic realization
use chi(g)=zeta_8^(-1) and psi(x)=zeta_p^Tr(x). In the p-adic realization
choose the embedding with zeta_8 reducing to g^((q-1)/8), so
chi=bar(omega)^((q-1)/8). Let varpi_p be the Gross-Koblitz uniformizer

\[
 \varpi_p^{p-1}=-p,\qquad
 \varpi_p\equiv\zeta_p-1\pmod{(\zeta_p-1)^2}.
\]

The classical Gross-Koblitz theorem gives

\[
 G_d=-\varpi_p^{(p-1)\sum_{i=0}^{f-1}\langle p^id/8\rangle}
       \prod_{i=0}^{f-1}\Gamma_p(\langle p^id/8\rangle).
\]

Therefore A_p(c)=varpi_p^E U_p(c), with

\[
 E=(p-1)\sum_{i,d}c_d\langle p^id/8\rangle,
 \qquad U_p(c)=(-1)^{\sum c_d}\prod_{i,d}
                  \Gamma_p(\langle p^id/8\rangle)^{c_d}.
\]

For the authentic c, sum(c)=0 and the valuations E/(p-1) are
(-15/8,-5/2,-5/4,0) in classes (1,3,5,7). For e the age contribution
is zero separately for each multiplier 1,3,5,7, and sum(e)=0. Thus
GG1 implies the **exact identity in the p-adic unit group**

\[
 U_p(c+te)=\chi(2)^{2t}U_p(c).
\]

For every k>=1 choose t=2^(k+2). The parent GPR-03 proof, reproduced
algebraically below, then yields one explicit source c_t with all of:

1. a strictly positive kernel, the same Gamma rank and leading coefficient;
2. r_(c_t)(n)=r_c(n) mod2^k and U_n^(c_t)=U_n mod2^k for **every n>=1**;
3. A_p(c_t)=A_p(c), and equal complete normalized GK units, for **every
   odd prime p**;
4. a different arithmetic source, distinguished by p13's
   first-birth residue and by its second source jet.

Indeed the difference kernel is

\[
 K(u)=1-3u^3+u^4+u^5
     =(1-u)^2(u^3+3u^2+2u+1)\ge0.
\]

The forcing difference before multiplication by t has valuation -2
at 2, because its offset-four term -3/[4(2n-1)] uniquely has that
valuation. The orbit difference obeys D_n=16D_(n-1)+t k(n); induction
gives v_2(D_n)=k exactly. Yet

\[
 13(U_2^{c_t}-U_2)\equiv t\not\equiv0\pmod{13},\qquad
 Q_{c_t}''(0)=-59+14t.
\]

Its completed radix constant also differs: it is pi plus t times the
strictly positive integral `integral_0^1 K(u)/(1-u^8/16) du`. No claim
that the resulting constant is normal or nonnormal is made.

**Precisely refuted claim:** Gamma rank, these full order-eight weighted
GK products at every odd prime, and arbitrary fixed-resolution all-time
2-adic source/orbit data jointly identify the original four-pole source.
They do not. This does not refute identification from the full affine
Gamma functions as functions of time, from the four actual coefficients,
from a second jet plus the parent's other constraints, or from additional
prime-birth information. It also does not prove the mutant nonnormal.

### Executed full-unit arithmetic, beyond valuation summaries

The local Gamma computation uses
Gamma_p(n)=(-1)^n product_(1<=j<n,p∤j) j and n congruent to x mod p^3.
For odd p this computes Gamma_p(x) mod p^3 exactly: shifting an integer
argument by p^k multiplies the signed unit product by 1 mod p^k,
because the complete unit product modulo p^k is -1; continuity gives
the rational-input statement. No fitted numerical extrapolation occurs.

| p | f | E | U_p mod p^3 | independently checked power m |
|---|---:|---:|---:|---:|
| 13 | 2 | -15 | 812 | 4 |
| 19 | 2 | -45 | 2882 | 2 |
| 73 | 1 | -135 | 213387 | 8 |
| 17 | 1 | -30 | 491 | 8 |
| 29 | 2 | -35 | 17233 | 4 |
| 43 | 2 | -105 | 22550 | 2 |
| 47 | 2 | 0 | 1 | 1 |

The complete exact Gauss coefficients, field polynomials, primitive
elements, Teichmuller residues and 17 prime rows are retained in
[probe_receipt.json](probe_receipt.json). Direct algebra in
Q(zeta_8,zeta_p) verifies A_p^m/(-p)^(mE/(p-1))=U_p^m mod p^3,
where m=8 for f=1 and m=8/gcd(8,p+1) for f=2. The left side lies
in Q(zeta_8) and is evaluated in the declared unramified p-adic
embedding. This is an independent check of the **whole unit power**,
not just its valuation. The choice among m-th roots is fixed by the
classical GK normalization; the power check alone does not verify that
root choice independently. A separate Cartesian-field/univariate
cyclotomic oracle checks all 119 Gauss sums and every unit modulo p^3.

## GG-03: the Gauss product is not the complementary character

For p=1,3,5 mod8, A_p(c) has a nonzero p-adic valuation and is therefore
**not a root of unity**. Every finite BBP rational cofiber character
e(hv) is a root of unity. Consequently A_p(c)=e(hv) is impossible for
every such p, every integer h, and every rational v.

For p=7 mod8 there is an exact semiprimitive evaluation:

\[
 \boxed{A_p(c)=(-1)^{(p+1)/8}.}\tag{GG3}
\]

To prove it, chi restricts trivially to F_p^*. Let z have trace zero
in F_(p^2), so log_g(z)=(p+1)/2 mod(p+1). The trace-zero fiber has
character sum (p-1)chi(z)^d, and each nonzero trace fiber has sum
-chi(z)^d, since all such fibers are scalar translates. Summing the
additive character gives G_d=p chi(z)^d. Hence
A_p(c)=chi(z)^(sum d c_d)=chi(z)^(-15)=(-1)^((p+1)/8).
This proves the formula for all primes in that class, not just the
five direct checks. The output is a static sign, not a time-dependent
cofiber transport.

The literal finite-field Frobenius operation gives G_(pd)=G_d, by
x↦x^p and trace invariance. This differs from the BBP time transport:
the latter carries radix-dependent coefficient multipliers as well
as pole permutations. The reflected class-three source has coefficient
sum 15, so its raw weighted Gauss product has complex magnitude
q^(15/2), whereas the authentic A_p has magnitude 1. Thus the naive
identification of the time-shadow transform with mere character
Frobenius is false. A normalized new transform would need its own
definition and signed proof.

## GG-04: a field obstruction to arbitrary rational Gauss reconstruction

Let K_p=Q(zeta_(8p)). Every order-eight Gauss sum above lies in K_p,
also when the finite field is F_(p^2). Consequently field operations
(addition, subtraction, multiplication, division by a nonzero value),
Galois conjugation, and traces/norms within that field cannot leave K_p.
Unrestricted extraction of algebraic roots is **not** included here.

If a rational v has reduced denominator D with an odd prime
ell|D and ell!=p, then

\[
 e(v)\notin K_p.\tag{GG4}
\]

Otherwise K_p would contain a primitive ell-th root by taking an
appropriate power of e(v). But
[Q(zeta_(8p ell)):Q(zeta_(8p))]=ell-1>1, since ell is coprime to 8p.
This elementary cyclotomic degree contradiction proves the claim.

The first authentic p13 birth supplies a small exact witness:

\[
 U_2=\frac{12}{13}+\frac{107}{315}\pmod1.
\]

Its complementary character has order 315 and cannot belong to K_13.
The receipt retains authentic p19 conductor disappearance at n=10,...,16
and return at n=17, plus p73 cancellation at n=274 (the k=4 clock).
The complete static Gauss object has no time coordinate that can by
itself mark those disappearing and returning conductors.

### Uniform eventual consequence of the inherited sharp conductor theorem

Let d_n=den(U_n). The source is 2-integral, so d_n is odd. For every
odd prime p, the p-primary factor of d_n is at most 8n: all source
denominators are at most 8n and radix multiplication does not introduce
odd denominator factors. Write d_n=P_n D_n with P_n the full p-primary
factor. The exact CRT cofiber has denominator **exactly D_n**, not just
a divisor: its numerator reduces modulo D_n to num(U_n)*P_n^(-1), a unit.

The parent CG-01 theorem gives log(d_n)=6n+o(n). Therefore, uniformly
over p, and for each fixed nonzero integer h,

\[
 \log\operatorname{ord}(e(hv_{n,p}))=6n+o(n).
\]

Indeed deleting P_n costs at most log(8n), and multiplication by h
removes at most log|h|. Since this remaining order is odd and coprime
to p, it has a foreign prime divisor for every sufficiently large n.
Thus **for every p**, e(hv_(n,p)) is outside K_p for all sufficiently
large n; the threshold can be chosen independently of p.

More generally, delete all primary factors for a set S_n of odd primes.
If |S_n|=o(n/log n), the removed logarithmic conductor is o(n), and
the remaining character still has exp(6n+o(n)) order, coprime to
2 product_(p in S_n) p. It is outside the compositum of those Gauss
fields. Exact reconstruction by this family of fields would require
at least (6-o(1))n/log n distinct prime fields merely to include all
prime divisors of the fixed-h character's conductor. This is a necessary
field-size obstruction, **not** a sufficient reconstruction theorem or
an Archimedean separation/cancellation estimate.

## Literature and proof authority

- Gross and Koblitz, *Gauss sums and the p-adic Gamma-function*, Annals
  109 (1979), 569–581, [original publication](https://annals.math.princeton.edu/1979/109-3/p06).
  This supplies GK; no new proof or new attribution is asserted here.
- Barman and Saikia, *Sato-Tate distribution of p-adic hypergeometric
  functions*, Theorems 3.2–3.3 and the explicitly declared Gauss convention,
  [open research article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9708806/).
- Barman, Saikia and McCarthy, *Summation identities and special values of
  hypergeometric series in the p-adic setting*, J. Number Theory 153
  (2015), 63–84, Theorem 2.6 for F_(p^r),
  [author-hosted paper](https://web.iitd.ac.in/~rupam/Publication/summation-JNT%282015%29.pdf).
  The finite-extension GK convention is the one used above.
- The inherited conductor theorem is
  [CG-01](../../arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md), exact parent
  PR399 at `fe9da9b0942f046cc67b02c4fed825ef74aa675a`. Its paper authority
  and ineffective asymptotic threshold remain unchanged.

Literature accessed 2026-10-30. The new local contribution is applying
the fully normalized multiplication identities to this exact BBP mutant
family and deriving the explicit selected-cofiber field obstruction.
No exhaustive scholarly novelty audit was performed.

## GG-05: exact surviving coefficient fiber, already at one prime

The blindness above can be classified, rather than merely exhibited.
Among **integer** four-pole vectors, one complete algebraic product at
p=17 has the exact fiber

\[
 \boxed{A_{17}(b)=A_{17}(c)\iff b-c\in2\mathbb Z(1,-3,1,1).}\tag{GG5}
\]

Here equality means equality as algebraic numbers under the declared
character convention, not equality of a finite p-adic truncation. To
prove necessity, apply the four automorphisms zeta_8↦zeta_8^u,
zeta_17↦zeta_17, for u=1,3,5,7, to the asserted equality. GK valuations
give M(b-c)=0, where

\[
 M=\begin{pmatrix}
 1&4&5&6\\3&4&7&2\\5&4&1&6\\7&4&3&2
 \end{pmatrix}.
\]

The matrix has rank three and kernel Q(1,-3,1,1). Because its first
kernel coordinate is one, integer solutions are t(1,-3,1,1) with
integer t. For primitive element g=3 in F_17, 2=3^14, so
chi(2)^2=zeta_8^(-28)=-1. Equation GG1 forces t even. Its converse
is GG2. These statements are unchanged if the chosen primitive
order-eight character is replaced by an odd power of itself. ∎

It follows that the same fiber is obtained from **all** the complete
odd-prime weighted products. Intersecting this fiber with all-time
modulo-2^k equality of the source or orbit gives the exact smaller fiber

\[
 \boxed{b-c\in2^{k+2}\mathbb Z(1,-3,1,1),\qquad k\ge1.}\tag{GG6}
\]

Indeed v_2(r_b(n)-r_c(n))=v_2(U_n^b-U_n)=v_2(t)-2 for every n>=1
when t!=0. For t>=0 this fiber contains infinitely many positive,
rank-matched sources. Within it the authentic second jet -59 forces
t=0. The p13 first-birth residue separates the explicit t=2^(k+2)
controls, but a single mod13 residue does **not** separate all t in
the infinite fiber: multiples of 13 survive that additional finite
datum. This is the exact information boundary, not a claim that all
odd-prime observations are non-identifying.

An especially small **exact** repair uses the parent prime-transport
involution. Requiring J(b)=b is the linear condition b_1+4b_5=0.
On the complete-Gauss fiber its defect is `5t`, while the authentic
defect is zero. Thus

\[
 A_{17}(b)=A_{17}(c)\quad\text{and}\quad\mathcal J(b)=b
 \quad\Longrightarrow\quad b=c.
\]

This combines two distinct source constraints and identifies the four
coefficients. It still gives no selected signed inequality. A finite
residue approximation to the J condition would leave further multiples
of its modulus and is not substituted for the exact equality.

## GG-06: even arbitrarily many prime Gauss fields miss prime-power births

Every finite compositum of order-eight Gauss fields is contained in
Q(zeta_(8M)) for an odd squarefree M, regardless of how large the
finite fields F_(p^f) are. Their additive characters still have order p.
A primitive ell^a-th root for an odd prime ell and a>=2 cannot belong
to this field: adjoining it multiplies the cyclotomic degree by at
least ell^(a-1)>1. Thus the union of all these finite composita omits
every root of unity with an odd prime-square in its order.

The original zero-seed BBP source attains such orders infinitely often.
By the parent AT-03 first-birth theorem, for Q=ell^a the birth index is

\[
 b(Q)=\begin{cases}(Q+7)/8,&Q=1\pmod8,\\
                    (Q+3)/8,&Q=5\pmod8,\\
                    (Q+1)/4,&Q=3,7\pmod8,
       \end{cases}
 \qquad v_\ell(U_{b(Q)})=-a.
\]

For fixed h!=0, choose a>v_ell(h)+1. Then e(hU_(b(Q))) has ell-power
order at least ell^2, and is outside **every** such finite compositum.
The same is true of the complementary character after removing a
fixed p-primary component, by choosing ell!=p. For example, the
authentic p13 cofiber 107/315 already has a 3^2 conductor factor.

This rules out a proposed exact reconstruction by an arbitrarily large
finite collection of these Gauss fields at those authentic times.
It does not rule out prime-power additive characters, ramified
extensions, separately adjoined GK uniformizers, analytic functions,
limits, or inequalities. In particular a normalized local unit obtained
by **separately dividing by varpi_p^E** is not silently asserted to lie
in the original global cyclotomic field. GG2's unit blindness remains
valid independently of this field restriction.

## GG-07: complete Galois averaging cancels without selecting the orbit

Let e(hv) have reduced odd order D, coprime to p. The exact Galois
average fixing K_p is the normalized Ramanujan sum

\[
 \frac1{\varphi(D)}\sum_{a\in(\mathbb Z/D\mathbb Z)^\times}
       e(ahv)=\frac{\mu(D)}{\varphi(D)}.
\]

This follows by the cyclotomic degree formula and the elementary
inclusion-exclusion evaluation of the primitive-root sum. At p13,n2
the average is exactly zero because D=315 is not squarefree. The
seven-pole zero-seed coherent null source from parent AT-07 also has
examples with exactly zero cofiber Galois average, while its **selected
full** characters e(hE_n) tend to one. Multiplying the zero cofiber
average by the retained primary factor still gives zero; if necessary
fix Q(zeta_(8P)) with P the full primary denominator when averaging
the full character. The executable extra probe retains both and labels
its chord bound as a bound for the full E_n, not for the cofiber alone.

For authentic cofibers the inherited log(D)=6n+o(n) implies that the
nonzero Galois averages, when D is squarefree, have magnitude
exp(-6n+o(n)); log(phi(D))=log(D)+o(log(D)) is enough. This is a large
averaged saving and still gives no bound for the selected embedding.
The missing premise is a source-selected comparison with the Galois
average. Neither the Gamma identities nor the conductor theorem
establish that premise; the coherent null control refutes the
source-independent version.
