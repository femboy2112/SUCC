# Finite adelic authentication does not control future coherent epochs

**Status: PROVED LOCAL, mathematical proof below.** This is a new quantitative
obstruction to a proof method, not a new signed-cancellation estimate for the
selected zero source and not a scholarly priority claim. It strengthens the
separate second-prime shadow of #529 to one rational, same-forcing trajectory
with exact finite carry history and arbitrary finite-place authentication.

## Source and observations

Throughout,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0(s)=s,\quad U_n(s)=16U_{n-1}(s)+r(n).
\]

The authentic source has **s=0**. For rational s all histories below are exact
unwrapped rationals. Write C_n(s)=floor U_n(s), x_n(s)={U_n(s)} and
kappa_n(s)=C_n(s)-16C_(n-1)(s). Do not replace U by x in finite-place tests.
For a prime p, [y]_p denotes the canonical rational p-principal part in [0,1)
(as in #529 AT-01). For odd-denominator y, its residue modulo 2^K is well defined.
Our finite observer reads the original forcing exactly, all [U_n]_p for a
specified finite set P of odd primes, finitely many 2-adic bits, and a finite
real history to declared positive error. It can also retain the exact original
integer carry transcript through a fixed time J. It does **not** enforce
literal equality U_0=0. That omitted test is decisive.

## AR-01. Constructive finite-place shadowing with a coherent future epoch

Let 0<=J<A, L>=1, B=A+L-1, K>=0, eta in (0,1/4), and let P be any finite set
of odd primes. Define original U_B=U_B(0), and choose

\[
M=\left\lceil16^{A-B}U_B\right\rceil,\quad
c=\frac M{16^A}-\frac{U_B}{16^B},\quad 0\le c<16^{-A}.
\]

Set D=2 product_(p in P) p, and choose the explicit integer

\[
q_0=\left\lceil\frac{2^K16^B}{\eta}\right\rceil,\qquad
q=1+D\left\lceil\frac{q_0-1}{D}\right\rceil,\qquad
m=\max\left(1,\left\lceil\frac{qc}{2^K}\right\rceil\right),\qquad
s=\frac{2^Km}{q}.
\tag{AR1}
\]

Then s>0, q is odd and coprime to every p in P, and all the following hold:

1. **Every-time finite-place match.** For every n>=0,
   \([U_n(s)]_p=[U_n(0)]_p\) for every p in P, and
   \(U_n(s)\equiv U_n(0)\pmod{2^{K+4n}}\).
2. **Small real prefix error.** For every 0<=n<=J,
   \[
   0<U_n(s)-U_n(0)\le16^{J-A}+\eta16^{J-B}.
   \tag{AR2}
   \]
3. **Exact carry-memory match when its explicit margin permits.** Put
   \(d_J=\min_{0\le n\le J}(1-x_n(0))>0\). If the RHS of AR2 is less than
   d_J, then C_n(s)=C_n(0) for every n<=J, and kappa_n(s)=kappa_n(0) for
   every 1<=n<=J. This also covers original states exactly on an integer,
   because the perturbation is positive.
4. **Coherent future epoch.** For n in [A,B], let
   \(R_{n,B}=\sum_{j=n+1}^B16^{n-j}r(j)\), with R_(B,B)=0, and
   \(e_n=U_n(s)-16^{n-A}M\). Then the exact signed identity and bounds are
   \[
   e_n=-R_{n,B}+16^n(s-c),\qquad
   0\le R_{n,B}<\frac1{15(n+1)^2},\qquad
   0\le16^n(s-c)\le\eta16^{n-B}.
   \tag{AR3}
   \]
   In particular, for every integer h,
   \[
   \operatorname{Re}\frac1L\sum_{n=A}^Be^{2\pi i hU_n(s)}
   \ge1-2\pi^2h^2\frac1L\sum_{n=A}^Be_n^2
   \ge1-2\pi^2h^2\left(\frac1{225(A+1)^4}+
   \frac{\eta^2(1-256^{-L})}{L(1-1/256)}\right).
   \tag{AR4}
   \]

**Proof.** The source recurrence gives U_n(s)-U_n(0)=16^ns. Since the reduced
seed denominator divides q, the difference is p-integral for every p in P;
adding a p-integral rational does not change its p-principal part. Since q is
odd, its 2-adic valuation is at least K+4n. These statements hold at every
future time, even after further source prime births.

The ceiling construction yields 0<=s-c<=2^K/q<=eta16^-B, including c=0 because
then m=1. Thus 0<s<16^-A+eta16^-B, proving AR2. Under the stated d_J margin,
each U_n(s) stays in the same half-open real unit cell as U_n(0). Taking floors
and then differences gives assertion 3.

The finite original source identity
\(U_B=16^{B-n}U_n+\sum_{j=n+1}^B16^{B-j}r(j)\) gives AR3 exactly. No pi value,
Green-tail oracle, or real irrational seed is used. For n>=2 the source has the
positive moment formula
\[
r(n)=\int_0^1t^{8n-8}(1-t)(t^2+2)(t^2+2t+2)\,dt
<\frac{15}{(8n-7)(8n-6)}<\frac1{n^2}.
\]
The second inequality follows from
49n^2-104n+42>0 for integers n>=2. Since A>=1, every term of R_(n,B) has
index at least2. The geometric sum therefore gives its displayed strict bound.
Both R and the perturbation are nonnegative, so
\(|-R+\delta|\le\max(R,\delta)\), and
\(e_n^2\le R_{n,B}^2+\eta^2 256^{n-B}\). Average the finite geometric
series: \(L^{-1}\sum_{n=A}^B256^{n-B}=(1-256^{-L})/[L(1-1/256)]\).
Finally apply cos t>=1-t^2/2 to the real Weyl mean. QED.

A fully rational certificate replaces 2pi^2 by20 in the first AR4 inequality;
pi<22/7<sqrt(10) suffices. This is a signed lower bound, not a floating-point
phase plot. It certifies near-maximal coherence of the explicitly changed seed.

## AR-02. Uniform cancellation is impossible on these finite observer fibers

Fix any finite observed prefix J and any positive real observation tolerance
rho. Let A tend to infinity, L=A, keep any fixed eta in (0,1/4), and allow P and K to grow
arbitrarily (but finitely) with A. For all sufficiently large A, AR2 is less
than both rho and d_J. AR1 therefore supplies rational seeds s_A>0 such that:

- the four-pole forcing is unchanged at every time;
- all observed principal parts and 2-adic residues agree exactly at every time;
- the original carry history through J agrees exactly;
- the real histories through J are rho-close;
- for every fixed h, the real part of the [A,2A) Weyl mean tends to1.

Consequently there is **no** uniform o(1) upper bound on these epoch means over
the finite-authentication fiber containing the zero seed. In fact the supremum
of their modulus tends to1. P may contain *every* prime dividing *every*
original U_n for n<=2A-1; the perturbation uses a denominator coprime to all of
them. Thus matching the complete original prime principal-part transcript on a
finite epoch still leaves the new complementary conductor uncontrolled.

**Complete-support boundary.** If P contains every prime <=8B, our positive
seed is less than1, has a reduced denominator greater than1, and that denominator
is coprime to every original denominator through B. Therefore it introduces a
new conductor prime outside the full original source support. A test enforcing
*absence of all new denominator primes*, rather than matching principal parts
only on the original support, rejects this construction. Exact denominator
genealogy plus the prescribed seed support is a stronger authentication rule
than the finite-coordinate observer considered here. We do not claim to evade it.

This is a quantified refinement of #529's independent second-prime alignment
countermodel: the adversary here is one exact original-forcing recurrence, not
independently selected phases at each time. It also preserves actual finite
integer carry memory. It is a stronger obstruction to partial authentication,
not a theorem about the authentic zero-source distribution.

**Quantifier firewall.** The construction gives forall A exists s_A. It does
not give exists s forall A, nor a fixed rational nonnormal seed. No claim about
asymptotic normality of any one of these rational shifts is made. Exact U_0=0
rejects every constructed s_A immediately. The theorem does not refute any
estimate whose hypotheses genuinely require literal zero, or an exact full
unwrapped real-state readout. It does refute any derivation that discards that
condition and tries to recover it from the listed finite observations.

## AR-03. The scale at which source-selection continuity fails

Even while s_A tends to0 in the real topology and modulo arbitrarily many
finite-place bits, the future signed observable can stay near1. The physical
expansion 16^B amplifies the seed precision; our explicit q satisfies
q_0<=q<q_0+D. This is an *upper cost for this construction*, not a universal
minimal-complexity result. The source-selected all-epoch estimate cannot be
obtained by continuity from finite histories without a quantitative modulus
that survives this exponential horizon dependence.

For any finite observed J, choose A with
16^(J-A)+eta16^(J-B)<min(rho,d_J). This is an explicit stopping rule for the
adversarial construction. The observer may close the fiber by testing exact
zero; doing so identifies the source but still proves no decay of its Weyl mean.
Mathematical memory adds information; it does not change this quantifier.

## AR-04. Analytic/Gamma consequence, carefully scoped

The source character generating function for a fixed rational seed is analytic
on |z|<1 and has bounded coefficients. Any proposed finite-history-derived
boundary modulus must be checked against AR1's arbitrarily late coherent epochs.
AR1 alone does **not** analyze the full Abel mean, and we do **not** claim that
a single coherent epoch forces a nonzero Abel boundary limit. The #496 bounded Tauberian
criterion still requires a genuine boundary limit for the single selected seed.
The Gamma/Abel kernel is a time smoother and does not recover the omitted exact
source selection. The four-pole arithmetic remains in every adversarial forcing;
only its initial seed has changed.

## Unpaid original-source theorem

For every fixed nonzero integer h, prove an upper bound tending to0 for
\(A^{-1}\sum_{n=A}^{2A-1}e(hU_n(0))\), using literal zero in a way that cannot be
replaced by AR1's finite fingerprints. The later PRIME_EPOCH_THEOREM.md now proves uniform epoch coverage and a
vanishing source-prime marginal, using classical Bourgain–Konyagin and PNT/AP.
The next discriminator is an explicit zero-source bound on the remaining
complementary-conductor covariance. The new local marginal does not supply that
bound; the signed hostile controls in PE-05 make the distinction quantitative.

**pi base-16 normality: OPEN. RH: OPEN.**
