# Arithmetic covariance forge: terminal support still permits coherent shadows

All statements concern the original four-pole forcing

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_n(s)=16U_{n-1}(s)+r(n),\quad U_0(s)=s.
\]

The authenticated source is **only** s=0. Write its reduced states as
U_n(0)=a_n/d_n and D_B=lcm(d_0,...,d_B). This note proves an obstruction to
weakened source authentication. It does not upper-bound the authentic zero
source's remaining signed covariance. Every hostile seed below is positive,
rational, and depends on the tested horizon.

## CF-A1. A source-forced denominator reservoir (imported, re-audited)

For B>=17 define

\[
Q_B=\prod_{B<p\le4B}p\,
\prod_{\substack{4B<p\le8B-7\\p\equiv1\pmod4}}p.
\]

PR #532 PF01--PF04 prove Q_B divides d_B, with v_p(d_B)=1 for every p|Q_B,
and log Q_B=5B+o(B). These are properties of the original zero source.
The exact read dependency is commit
`f6560d9378b76ec4bca2e8b2bfbef591e0020fa3`, file
`research/2026-11-06/prime_frobenius_spectral/THEOREMS.md`.

To audit the scope: primes in (B,2B] have the normalized principal coefficients
7/2,33/10,47/15 for p=1 mod4, or -19/6,-65/21 for p=3 mod4.
Only p=19 with 10<=B<=16 can cancel, excluded here. Primes in (2B,4B]
have one pole, or the two-pole coefficients 16/3 and -4/3 after Frobenius
transport; these never vanish in this range. The last shell has one pole,
coefficient 4 or -1. All pole valuations are at most one because p>B>=17
and p squared exceeds 8B. Thus all asserted terminal valuations are exactly
one; the product is squarefree. PNT and PNT in class 1 mod4 give the logarithmic
mass 3B+2B+o(B). The latter analytic theorem is classical, not a finite-test
inference; see [Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).

## CF-A2. Exact terminal-denominator avoidance (new local proof)

Let q>1 be any **odd**, squarefree divisor of d_B such that v_p(d_B)=1 for every p|q.
Put t=omega(q), and assume **t<min{p:p|q}**. For K>=0 and any integer m0,
among m=m0,...,m0+t there is a choice for which

\[
\gcd\left(a_B+16^B2^Km(d_B/q),d_B\right)=1.\tag{A2}
\]

Indeed, for each p|q the coefficient 16^B 2^K(d_B/q) is invertible mod p,
so exactly one residue class is forbidden. Since t<p, that class occupies at
most one of these t+1 integers. The union of t forbidden sets cannot exhaust
them. For p|d_B with p not dividing q, the additive term is divisible by the
full p-power in d_B; a_B was already a unit. Thus no prime dividing d_B
divides the resulting numerator. This proves (A2), including when m0=0.

Consequently the seed s=2^K m/q has **den(U_B(s))=d_B exactly**. Reduction of
s itself does not affect the argument. This is stronger than den(s)|d_B;
the latter alone would not prevent cancellation of original terminal primes.

## CF-A3. A finite source-support counterfeit with signed certificates

Fix integers 0<=J<A, L>=1, B=A+L-1>=17, K>=0, rational 0<eta<1/4,
and a finite set P of observed odd primes. Take

\[
q=\prod_{p\mid Q_B,\ p\notin P}p,\quad t=\omega(q),\qquad
q>1,\quad t<\min_{p\mid q}p,\quad
(t+1)2^K16^B\le\eta q.\tag{A3}
\]

These are explicit finite hypotheses, checked before any certificate is
issued. Define the rational, pi-free terminal anchor

\[
M=\left\lceil16^{A-B}U_B(0)\right\rceil,\qquad
c=\frac{M}{16^A}-\frac{U_B(0)}{16^B},\quad 0\le c<16^{-A}.
\]

Set m0=max(1,ceil(qc/2^K)); choose the first m in [m0,m0+t] satisfying
(A2), and put s=2^K m/q. Then

\[
0<s<16^{-A}+\eta16^{-B}<1,\qquad
0\le s-c\le(t+1)2^K/q\le\eta16^{-B}.\tag{A4}
\]

The upper bound allows m0=1 when c=0. The conclusions are:

1. Original forcing and all unwrapped rational differences are exact:
   U_n(s)-U_n(0)=16^n s for every n>=0.
2. For all p in P and all n>=0 the p-principal parts agree, and
   v_2(U_n(s)-U_n(0))>=K+4n.
3. den(U_B(s))=d_B, and den(U_n(s)) divides D_B for every 0<=n<=B.
4. If 16^J s < min_{0<=n<=J}(1-{U_n(0)}), then all integer floors and
   carries through J agree. The real prefix error is at most 16^J s.
5. For every nonzero integer h the future signed Weyl average obeys

\[
\Re\frac1L\sum_{n=A}^{B}e(hU_n(s))\ge
1-2\pi^2h^2\left[
\frac1{225(A+1)^4}+\frac{\eta^2(1-256^{-L})}{L(1-1/256)}
\right].\tag{A5}
\]

Here e(x)=exp(2 pi i x). For item 2, q is odd and avoids P; multiplication
by 16^n preserves p-integrality and adds 4n to the 2-adic valuation.
For item 3, den(s)|q|d_B|D_B and the denominator of a rational sum divides
the lcm of its summands' denominators. Item 4 follows because the perturbation
is positive and remains below every next integer boundary; equal floors
give equal carry differences.

For the signed claim, put

\[
R_{n,B}=\sum_{j=n+1}^B16^{n-j}r(j),\qquad
E_n=U_n(s)-16^{n-A}M=-R_{n,B}+16^n(s-c).
\]

The authentic four-pole algebra gives 0<r(j)<j^(-2) for j>=2
(the already-audited AR2 source bound). Thus
0<=R_{n,B}<1/[15(n+1)^2] when n<B, and R_{B,B}=0. Both terms in E_n
have opposite signs. Therefore E_n^2<=R_{n,B}^2+[16^n(s-c)]^2.
Sum the second square geometrically, bound the first uniformly, and use
cos(2 pi h E_n)>=1-2 pi^2 h^2 E_n^2. This proves (A5).
The implementation additionally computes every exact rational E_n and
certifies Re W>=1-20 h^2 mean(E_n^2), since 2 pi^2<20.

## CF-A4. Linear 2-adic precision at unchanged terminal denominator

Fix P0, eta in (0,1/4), and J. Let L=A, B=2A-1. Let p_A be the largest
prime <=4A with p_A=1 mod8 and ord_(p_A)(16)^3>p_A, as in PE5--PE8.
Take P=P0 union {p_A}. Removing this one varying prime and finitely many
fixed primes from Q_B costs O(log B) in its logarithm, so log q=5B+o(B).
PNT also gives t=O(B/log B); since min p|q>B, t<min p|q eventually.

For any kappa>=0 satisfying

\[
\kappa\log2<5-\log16,\tag{A6}
\]

all integer K_A<=kappa B eventually satisfy (A3), since

\[
\log\frac{\eta q}{(t+1)2^{K_A}16^B}
\ge[5-\log16-\kappa\log2]B+o(B)\longrightarrow+\infty.
\]

The prefix condition eventually holds because J is fixed and s->0.
Thus these s_A preserve exactly the original terminal denominator, stay
within the original cumulative denominator at every earlier time, retain
all selected finite principal parts and linearly many 2-adic bits, and obey
Re W_(A,A)(h;s_A)->1 for every fixed h. Since |W|<=1, W->1 as a complex
number. The per-construction exact capacity

\[
K_{\max}=\left\lfloor\log_2\frac{\eta q}{(t+1)16^B}\right\rfloor
\]

satisfies K_max/B -> (5-log16)/log2 = 5/log2-4, approximately 3.21347.
This is a proved capacity of this construction, not a lower bound on every
possible observer or reconstruction procedure. More generally one may
remove observed primes of total logarithmic mass M_A provided
limsup(M_A/B)+kappa log2<5-log16.

**Growing memory, with explicit chronology.** The same conclusion retains
floors and carries for J=floor((A-1)/5) whenever the construction's other
finite hypotheses hold. Each literal pole denominator through J divides
H_J=lcm(1,...,8J), so D_J divides H_J. The elementary bound H_J<=4^(8J)
=16^(4J) gives

\[
\min_{n\le J}\frac{1-\{U_n(0)\}}{16^n}\ge
\frac1{16^JD_J}\ge16^{-5J}.
\]

Since s<(1+eta)16^(-A)<16^(-(A-1))<=16^(-5J), all these floors and carries
are unchanged. For completeness, lcm(1,...,N)<=4^N follows inductively:
for N=2m the quotient by lcm(1,...,m) divides binomial(2m,m)<=4^m;
for N=2m+1 the quotient by lcm(1,...,m+1) divides
binomial(2m+1,m)<=4^m. Each added prime power exceeds the smaller endpoint,
and hence contributes a carry in the respective binomial valuation.
The odd binomial inequality also follows by its successive ratio being <4.

Using the classical PNT strengthens the growing-memory range:
log D_J<=log H_J=8J+o(J), so J=floor(alpha A) is allowed for any fixed
0<=alpha<log16/(8+log16), approximately 0.25737. This is a sufficient
range, not a sharp memory threshold. The exact floor-preserving seed
cylinder is 0<=s<min_(n<=J)(1-{U_n(0)})/16^n.

## CF-A5. The selected marginal can coexist with covariance tending to one

For these seeds retain the *original* selected prime p_A. The local clock

\[
a_n=e(h[U_n(0)]_{p_A})=e(h[U_n(s_A)]_{p_A})
\]

is identical; [x]_p denotes the canonical rational p-principal part modulo
one, not the reduction of x in F_p. By the proved PE1--PE13 original-source
epoch theorem, E_A a ->0. Set
b_n=e(h(U_n(s_A)-[U_n(s_A)]_{p_A})). Then the bilinear covariance, without
complex conjugation, satisfies

\[
\mathrm{Cov}_A(a,b)=E_A(ab)-(E_Aa)(E_Ab)\longrightarrow1.\tag{A7}
\]

Indeed E_A(ab)=W_A(h;s_A)->1 and |E_A b|<=1. This refutes the shortcut
"uniform selected prime clock + terminal denominator/support authentication
+ linearly growing finite floor/carry memory + linear 2-adic precision forces small
complement covariance." The uniformity is conditional on these weaker
authentication tests, not on literal U0=0.

For finite receipts no ineffective BK constant is estimated. The classical
complete-cycle Gauss bound gives |E_(I_p) a|<=sqrt(p)/ord_p(16). With
L_p=(p-1)/4, I_p=[L_p+1,2L_p+1) and p<=4A, normalized interval gluing gives

\[
|E_Aa|\le \frac{\lceil\sqrt p\rceil}{\operatorname{ord}_p(16)}
+2\left(1-\frac{|I_p\cap[A,2A)|}{A}\right)=g_A.
\]

For p not dividing h, therefore Re Cov >= certified Re W - min(1,g_A).
Every number in this last certificate is rational and exactly checked.
The asymptotic marginal theorem uses Bourgain--Konyagin 2003 Theorem 2.1,
PNT/AP, and elementary order counting already pinned in PE's source audit;
it is not inferred from these four finite cases.

## CF-A6. The exact boundary: chronology and all principal parts

These controls do **not** retain chronological support. Because 0<s<1,
its reduced denominator is nontrivial; all its prime factors exceed B,
and they occur already at n=0. Their earliest authentic pole times are
(p+7)/8 for p=1 mod8, (p+3)/8 for p=5 mod8, and (p+1)/4 for p=3 mod4.
Thus they cannot appear in an original fixed prefix once B is sufficiently
large. Original U0=0 rejects the counterfeit immediately. Terminal-union
support is strictly weaker than chronological support.

Nor do we match every principal part on that terminal support. If the seed
denominator is supported on a finite set S and its p-principal part is zero
for *every* p in S, the seed is an integer. With |s|<1 it is zero. There is
no contradiction: our observed set P excludes the primes used for q.

The quantifiers are **for every sufficiently large A there exists s_A**.
There is no assertion of one fixed rational nonnormal seed, no replacement
of the immutable source, and no inference about normality of pi. These
constructive controls narrow which source-authentication condition a
future covariance proof must use; they do not pay its arithmetic estimate.

## Failed arithmetic estimates

On a clean p-clock interval put v_n/p=[U_n]_p with 0<=v_n<p, and let
c_n=floor(16v_n/p), y_n=U_n-v_n/p. Then
y_(n+1)=16y_n+r(n+1)+c_n. Consequently
e(hy_(n+1))=e(hy_n)^16 e(hr(n+1)). The small forcing derivative does not
make this complementary phase a slowly varying amplitude: the expansive
power and wrap carries survive. Summation by parts requires an actual
variation estimate; smooth r alone supplies none.

Folding by m=ord_p(16) produces |W|^2 <= mean_t |B_t|^2, where B_t is the
mean complementary phase along the corresponding return fiber. This is a
valid Cauchy--Schwarz identity, but it simply leaves the source-selected
return energy unpaid. The counterfeit above shows terminal support and
local-prime flatness alone cannot control that energy. Neither failed route
is promoted to a new normality reduction.
