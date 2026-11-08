# Complete source-prime epochs: unconditional local character decay and the remaining covariance

**Status: PROVED LOCAL using two declared classical imports.** Original four
BBP poles and literal U0=0 throughout. This result pays the prime-clock coverage
and local marginal cancellation obligations left open in #529 AT-03. It does
not pay the complementary-conductor covariance. No scholarly priority or Lean
certificate is claimed.

Write e(t)=exp(2pi i t), m_p=ord_p(16) for odd primes p, and [y]_p for the canonical rational
p-principal part, retaining the original unwrapped rational U_n. Let

\[
\mathcal G=\{p\text{ prime}:p\equiv1\pmod8,\ m_p^3>p\}.
\]

For every sufficiently large integer A define p_A to be the **largest** member
of G not exceeding4A, and put L_A=(p_A-1)/4. This selector is deterministic and
arithmetic; no pi digit or observed real Fourier amplitude enters its definition.

## PE-01. A complete clean epoch inside each split prime's lifetime

For every prime p=1 mod8, put L=(p-1)/4. Then

\[
n_p=(p+7)/8=(L+2)/2,\qquad n'_p=(p+1)/2=2L+1
\tag{PE1}
\]

are the first and second positive times at which p divides a source denominator.
For all n_p<=n<n'_p,

\[
[U_n]_p=\frac{[4\,16^{n-n_p}]_p^{\mathrm{int}}}{p},
\tag{PE2}
\]

where the bracket on the numerator denotes its least integer residue modulo p.
The integer interval

\[
I_p=\{L+1,L+2,\ldots,2L\}
\tag{PE3}
\]

lies wholly in this clean lifetime, has length L, and consists of exactly L/m_p
complete local cycles. In particular for p not dividing h,

\[
\frac1L\sum_{n\in I_p}e(h[U_n]_p)
=\frac1{m_p}\sum_{x\in\langle16\rangle} e(\xi x/p),
\quad \xi=4h16^{L+1-n_p}\not\equiv0\pmod p.
\tag{PE4}
\]

**Proof.** In the odd-denominator decomposition the four factors are
2n-1,4n-1,8n-7,8n-3, with pole coefficients -1/2,-1/2,4,-1 respectively.
For p=1 mod8 the earliest positive multiples yielding a source pole are:

| factor | first possible multiple | time |
|---|---:|---:|
| 8n-7 | p | (p+7)/8 |
| 2n-1 | p | (p+1)/2 |
| 8n-3 | 5p | (5p+3)/8 |
| 4n-1 | 3p | (3p+1)/4 |

The next multiple for 8n-7 is9p, later than (p+1)/2. Thus the first pole is
unique with residue4/p; the next is exactly the 2n-1 pole. Since U0=0,
all prior history is p-integral. Between the two births the recurrence multiplies
the principal numerator by16, proving PE2. Because L is even and L>=4,
L+1>=n_p and 2L=n'_p-1. Fermat gives16^L=2^(p-1)=1 modp, hence m_p dividesL.
The epoch therefore covers a whole number of subgroup cycles, proving PE4. QED.

The classical Gauss estimate immediately gives |PE4|<=sqrt(p)/m_p. That alone
need not tend to0 when m_p is only larger than p^(1/3); the stronger import
below is essential, and the p=641 control exposes the distinction.

## PE-02. Elementary abundance of good orders; full epoch coverage

For x>=2 let M=floor(x^(1/3)). If p<=x and m_p<=p^(1/3), then p divides

\[
V_M=\prod_{j=1}^M(16^j-1).
\]

Since log_2 V_M<4 sum_(j=1)^M j=2M(M+1), the number of its distinct prime
factors is less than2M(M+1). Consequently

\[
\#\{p\le x:p\text{ odd prime},\ m_p^3\le p\}\le2\lfloor x^{1/3}\rfloor
(\lfloor x^{1/3}\rfloor+1)=O(x^{2/3}).
\tag{PE5}
\]

This is elementary counting, not an assumption about multiplicative orders.
The classical prime number theorem in the fixed progression1 mod8 says

\[
\#\{p\le x:p\equiv1\pmod8\}\sim\frac{x}{4\log x}.
\tag{PNT8}
\]

For every **fixed** epsilon in (0,1), the number of such primes in
[(1-epsilon)x,x] is asymptotic to epsilon x/(4 logx). Subtracting PE5 leaves
positive, indeed unbounded, good-prime counts in that interval for every
sufficiently large x. Hence p_A is eventually defined and

\[
\boxed{p_A/(4A)\longrightarrow1,\qquad L_A/A\longrightarrow1.}
\tag{PE6}
\]

No unproved statement about primes in an arbitrarily specified shrinking
interval is used: fixed-epsilon intervals imply the displayed ratio limit.
No Artin conjecture, GRH, Erdős–Murty order theorem, or selected source-frequency
hypothesis is imported.

## PE-03. Unconditional local Fourier cancellation on every actual dyadic epoch

**Classical finite-field input.** Bourgain–Konyagin (2003), Theorem2.1, printed
page78, provides an exponent gamma_delta>0 for every delta>0 such that every
multiplicative subgroup H of F_p^* of size at least p^delta satisfies

\[
\max_{\xi\ne0}\left|\frac1{|H|}\sum_{x\in H}e(\xi x/p)\right|
\le p^{-\gamma_\delta}.
\tag{BK}
\]

Their exponent has the stated form exp(-C1/delta^C2) for absolute positive
constants; no numerical value is claimed here. This is an imported classical
sum-product theorem, not something certified by our finite tests.
[Primary paper](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf).

Apply BK with delta=1/3 to p_A, since m_(p_A)^3>p_A. Put gamma=gamma_(1/3)>0.
By PE4 the local mean on I_(p_A) has modulus at most p_A^-gamma for **every**
integer h not divisible by p_A.

For any bounded sequence |f_n|<=1, averages on finite integer intervals J,I
of sizes A,L differ by at most the exact total-variation weight distance

\[
\left|\frac1A\sum_{n\in J}f_n-\frac1L\sum_{n\in I}f_n\right|
\le\sum_n\left|\frac{1_J(n)}A-\frac{1_I(n)}L\right|
=2\left(1-\frac{|I\cap J|}{\max(A,L)}\right).
\tag{PE7}
\]

Indeed both weight sequences sum to1 and their overlap mass is
|I intersection J|/max(A,L). For J_A=[A,2A) and I=I_(p_A), set

\[
\varepsilon_A=2\left(1-\frac{|I_{p_A}\cap J_A|}{A}\right).
\]

Here p_A<=4A and p_A=4L_A+1 imply L_A<=A-1. Direct endpoint counting gives

\[
|I_{p_A}\cap J_A|=\max(0,2L_A+1-A),\qquad
0\le\varepsilon_A\le\frac{4(A-L_A)}A\longrightarrow0.
\tag{PE8}
\]

Therefore the **actual original-source marginal** obeys the unconditional bound

\[
\boxed{
\max_{1\le h<p_A}\left|\frac1A\sum_{n=A}^{2A-1}e(h[U_n(0)]_{p_A})\right|
\le p_A^{-\gamma}+\varepsilon_A\longrightarrow0.
}
\tag{PE9}
\]

This is an all-epoch source-prime character theorem with uniform nontrivial
p-local frequencies, not a Galois ensemble average. The observation prime changes
with A; the character is only one factor of the authentic real phase. Its
unconditional limit is a genuine mathematical component, not pi normality.

## PE-04. The only remaining obligation on this route is selected complement covariance

For fixed nonzero integer h and sufficiently large A (so p_A does not divide h),
use actual J_A and define

\[
a_n=e(h[U_n]_{p_A}),\qquad
b_n=e(h(U_n-[U_n]_{p_A})),\qquad
\operatorname{Cov}_A(a,b)=E_A(ab)-(E_Aa)(E_Ab).
\tag{PE10}
\]

This is the bilinear signed covariance with **no conjugation**; the definition
is stated to avoid confusing it with a Hermitian covariance. Canonical rational
principal parts give a_n b_n=e(hU_n) exactly. Thus

\[
\boxed{
|W_A(h;0)-\operatorname{Cov}_A(a,b)|
=|(E_Aa)(E_Ab)|\le p_A^{-\gamma}+\varepsilon_A\to0.
}
\tag{PE11}
\]

It follows that the original Weyl gate is equivalent to

\[
\forall h\in\mathbb Z\setminus\{0\},\quad
\operatorname{Cov}_A(a,b)\longrightarrow0.
\tag{PE12-OPEN}
\]

**What changed relative to #529 AT6:** that criterion left a useful-order prime
cycle, covering every source epoch, and complementary-conductor covariance as
separate obligations. PE1–PE9 prove the order/cycle/marginal/coverage components
unconditionally using the original pole chronology and the declared classical
imports. PE12 is still an equivalent reformulation of the remaining source
cancellation, not a weaker premise proved true, and it carries the entire
remaining normality difficulty. No estimate on that covariance has been proved.

The local marginal also survives any fixed rational seed at every sufficiently
large selected p, because those primes eventually avoid its seed denominator.
It is therefore source-specific but not itself selective for literal zero.

## PE-05. Signed hostile controls: preserve local cancellation, restore near-total coherence

For each aligned p in137,281,521, use AR1 with A=L+1, lengthL, J=3, K=9,
eta=2^-20 and P=(3,5,7,p). These rational seeds preserve the p-principal part at
every time and give exact rational lower certificates C_h for Re W on I_p.
Since the finite Gauss bound gives |E a|<=sqrt(p)/m_p and |E b|<=1,

\[
\boxed{\operatorname{Re}\operatorname{Cov}_{I_p}(a,b)
\ge C_h-\frac{\lceil\sqrt p\rceil}{m_p}.}
\tag{PE13}
\]

This is a rational signed covariance lower bound, without evaluating a complex
exponential numerically. All three positive lower certificates are retained in
PRIME_EPOCH_RECEIPTS.json. They refute transferring local prime cancellation
to full real cancellation without the selected complementary-phase condition.
They change the seed and introduce a new conductor, so exact source selection
rejects them. They do not refute PE12 for literal zero.

## Dependencies and status

- Original poles, U0=0, unwrapped recurrence: pinned main and #529's canonical
  principal parts; PE1 is rederived above, with independently enumerated pole
  times and exact cycles in the finite oracle.
- PNT in arithmetic progressions at fixed modulus8 is a classical unconditional
  theorem; its use is exactly PNT8, with no claimed explicit error term. See the
  [Kedlaya, Notes on Analytic Number Theory, Theorem4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).
- Bourgain–Konyagin, *Estimates for the number of sums and products and for
  exponential sums over subgroups in fields of prime order*, C. R. Acad. Sci.
  Paris337 (2003),75–80, Theorem2.1, DOI10.1016/S1631-073X(03)00281-4.
- The primary BK PDF was independently rendered by root and its printed
  Theorem2.1 checked visually. Downloaded PDF SHA-256:
  `2d87a571d068007f2d6ed2657beb4e37d4dab56e858b2128852a70077dfa7fb6`.
  Only this hash/citation is retained; the paper is not redistributed.
- New paper derivations relative to the inspected SUCC research: PE1–PE11; finite arithmetic checks are not formal
  certification of PNT/AP or BK. The new source instance has not been externally
  refereed, and worldwide novelty is not asserted.
- **OPEN:** PE12, pi base-16 normality, RH. No independent selected signed upper
  saving is claimed from the new local marginal theorem.
