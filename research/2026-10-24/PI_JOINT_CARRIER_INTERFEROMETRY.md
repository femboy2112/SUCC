# Operation Joint Carrier: Source-aligned Pascal, Lucas, 2-adic, and odd-prime phase tomography

**Date:** 2026-10-24. **Research-only, draft #274 descendant.** Pinned parent
`research/pi-pascal-lucas-quotient-2026-10-24@d942c4707d750f788f39acb137a04e871a93e0a6`,
which inherits draft #273 `8d89711db77fea81920321d32f831eed3dec1e68`
and #272 `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`. Sibling #271
`4eafc6151e9a494f2aea8ec79ca6cf5608152c80` was *read*, not inherited.

**Claim boundary:** exact elementary paper derivations and named classical inputs,
with separate exact finite tests. No fresh Lean-kernel authority, external
refereeing, unconditional real-circle mixing estimate, or proof of pi normality.
All algorithms use rational integer arithmetic unless explicitly marked a
noncertifying numerical diagnostic. New claims JPC-01--22.

## 0. Steelman: the carrier is already actual

The user corrects a selection/observation category error. The BBP recurrence,
initial condition and positive tail identity specify one mathematical source.
Different observers do not select that source; their observations constrain
what they can certify about it. This round therefore **does not** take an
independent Haar draw at each prime and call the result the actual source.
It derives a synchronized all-prime representation *at each authentic source
time* and explicitly tests why unrelated prime marginals fail.

The desired object is the real-circle selected carry frequency, ultimately
uniform digit/block frequencies for `alpha=pi/16` under multiplication by 16.
Our previously authenticated input is

$$
U_0=0,\qquad U_n=16U_{n-1}+r(n),\qquad
r(t)={4\over8t-7}-{2\over8t-4}-{1\over8t-3}-{1\over8t-2}.
$$

Prior SUCC: #270 authentic `Z_2` source isometry and origin zero; #272 source
Pascal valuations and positive kernel; #273 exact path/history operators;
#274 Boolean-incidence / rank quotient and lost Walsh fibers. These premises
are **not** strengthened by an unrelated ensemble distribution.

## 1. The source itself splits into 2-adic integral and odd-prime fractional information

### 1.1 Exact odd-denominator normal form (JPC-01)

Combine the even-denominator terms without rounding:

$$
\boxed{r(t)={4\over8t-7}-{1\over8t-3}
-{3t-1\over(2t-1)(4t-1)}
={120t^2-89t+16\over(2t-1)(4t-1)(8t-7)(8t-3)}.}
$$

For every integer n>=1, all displayed denominators are odd. By induction,
`U_n` has odd reduced denominator, so `U_n in Z_2`. **Its p=2 fractional
primary component in Q/Z is identically zero.** This is not equivalent to
zero 2-adic source information: its *integral* residue `U_n mod 2^k` is
nontrivial and, by inherited #270, runs through every residue over a full
2^k index window.

An elementary extra proof shows the forcing `r` itself is a 2-adic isometry.
Set `D(t)=(2t-1)(4t-1)=8t^2-6t+1` and `g(t)=(3t-1)/D(t)`.
For s,t in Z_2 with s != t,

$$
{g(t)-g(s)\over t-s}=
{3D(s)-(3s-1)(8(t+s)-6)\over D(t)D(s)}
\equiv1\pmod2.
$$

The other two terms of `r` have difference quotients respectively
`-32/[(8t-7)(8s-7)]` and `+8/[(8t-3)(8s-3)]`, divisible by 2.
Consequently the quotient `(r(t)-r(s))/(t-s)` is a 2-adic unit and

$$
\boxed{v_2(r(t)-r(s))=v_2(t-s).}
$$

The Green interpolation `F(t)=sum_{j>=0}16^j r(t-j)` is consequently also
an isometry: its first difference quotient is odd; all other quotients
are divisible by 16. Identifying `F(n)` with `U_n` uses the independently
inherited #270 proof that `F(0)=0`, rather than a new assertion of that
nontrivial zero identity. The finite source permutation tests cover k<=9,
but they are not a replacement for the paper theorem.

### 1.2 Exact prime-torsion decomposition (JPC-02--05)

For any rational `x=a/b` with `(a,b)=1`, put `b=p^v b'` for a prime p
with `(p,b')=1`. Define

$$
\lambda_p(x)=
\begin{cases}
0,&v=0,\\
\displaystyle {a(b')^{-1}\bmod p^v\over p^v},&v>0,
\end{cases}
\qquad \lambda_p(x)\in\mathbb Q/\mathbb Z.
$$

The CRT proves, with **no assumption of independence**,

$$
\boxed{[x]=\sum_{p\mid b}\lambda_p(x)\text{ in }\mathbb Q/\mathbb Z.}
$$

Indeed multiplying the proposed sum by `b` gives an integer congruent to
`a mod p^v` for each prime power dividing b; CRT makes it congruent to
`a mod b`. Every sum is **finite** for the rational source. The maps
`lambda_p` are homomorphisms on `Q/Z` and the unique p-primary projections.

For the actual BBP source, every prime divisor of the denominators through
time n is at most `8n-3` (the bound comes from the *odd-denominator normal
form*, not from a guessed density). Write `a_{p,n}=lambda_p(U_n)`. Then

$$
\boxed{a_{p,n}=16a_{p,n-1}+\lambda_p(r(n))\pmod1,\qquad a_{2,n}=0,}
$$

and, for every integer h,

$$
\boxed{e(hU_n)=\prod_{\substack{p\le8n-3\\p\text{ odd}}}
 e(h a_{p,n}),\qquad e(t)=\exp(2\pi i t).}
$$

This is the exact **synchronized joint source**, not an ensemble of
independently selected trajectories. The *entire* rational real circle
phase is recovered at each n from the odd-prime primary components, while
the integral dyadic clock retains source-time information.

Integer-coefficient Pascal/Newton operators commute with every primary
projection:

$$
\lambda_p\bigl(\Delta^kU_n\bigr)=\Delta^k\lambda_p(U_n)
\pmod1.
$$

This gives an honest operator square linking signed Pascal differences to
all prime clocks; summing those clocks restores the real circle value.
The support-only Lucas operator is NOT interchangeable with the original
integer Pascal coefficients. At p=3, `C(2,1)=2` survives but differs from
support weight 1. More quantitatively, for `v_p(U_j)>=-a` and integer
coefficients `c_j congruent d_j mod p^s`, the ultrametric inequality gives

$$
v_p\left(\sum_j(c_j-d_j)U_j\right)\ge s-a.
$$

The integral-source hypothesis matters. Setting `U_j=1/p` and
`c_j=p,d_j=0` makes the difference equal 1, NOT divisible by p.

Finally, all the fractional primary components `lambda_p(x)` are unchanged
when x is replaced with x+1. But scaling by `1/b` changes its real phase by
`1/b`. Thus **even ALL Q/Z prime-primary projections do not recover an
integer lift needed by a rational base filter.** The existing #272
`b^k` carry torsor is real: the full p-adic *integral residues* at primes
dividing b, or the authentic integer source lift, must be preserved.

## 2. Four exact prime-power forcing clocks and the small-prime exceptions

### 2.1 The source-specific four-pole theorem (JPC-06--07)

Let p>=7 be prime. The four distinct congruence classes modulo p^k

$$
8n=7,\quad 8n=3,\quad 2n=1,\quad 4n=1\pmod{p^k}
$$

are the only possible p-adically nonintegral forcing classes. They are
distinct modulo p: a shared solution forces p=2,3, or 5. In any one of
the four classes, exactly one odd denominator of `r` is p-divisible and
its numerator is a p-unit; the other terms are integral at p. Hence

$$
\boxed{v_p(r(n))\le-k\iff
n\text{ belongs to one of four roots modulo }p^k.}
$$

The valuation equals minus the depth of that unique pole. Consequently,
under Haar on Z_p,

$$
\Pr(v_p(r(n))\le-k)={4\over p^k},\quad
\Pr(-v_p(r(n))=k)={4(p-1)\over p^{k+1}}\ (k\ge1),
$$

where the second probability is for the positive pole-depth random
variable and excludes the integral event. Its mean depth is `4/(p-1)`.
These are exactly distributed prime innovations, not a probabilistic
assumption about the selected pi source.

For a finite set of *distinct* primes p_i>=7 and depths k_i>=1, CRT on
`M=product p_i^k_i` gives **exactly 4^s residue classes** simultaneously
activating every prescribed pole, a fraction

$$
\boxed{\Pr_M(\text{all pole events})=
\prod_{i=1}^s{4\over p_i^{k_i}}.}
$$

This is independence of **instantaneous forcing-activation predicates**
when n is uniform modulo a complete fixed period M. It does NOT give
independence of the phase histories `a_{p,n}`, because the recurrence has
memory and all prime places see the same integer time n.

With classical Mertens prime harmonic theorem and the prime-number theorem,
the mean number of p>=7 poles of the actual forcing over 1<=n<=N obeys

$$
{1\over N}\sum_{n=1}^N\#\{p\ge7:v_p(r(n))<0\}
=4\sum_{7\le p\le8N}{1\over p}+O\left({\pi(8N)\over N}\right)
=4\log\log N+O(1).
$$

To prove the first equality, for each p count four residue classes in a
length-N index interval, each of size `N/p+O(1)`, and sum over primes.
The asymptotic uses **classical external prime-distribution results**,
not finite computation or a new prime theorem. These are innovations at
one n. The number of accumulated nonzero prime components in `U_n` can
be much larger: it remembers old innovations.

### 2.2 The exceptional small primes 3 and 5 (JPC-08)

The numerator of the exact rational forcing is

$$
N(t)=120t^2-89t+16\equiv t+1\pmod {15}.
$$

At p=3 the pole roots `7/8` and `1/2` coincide modulo 3; at p=5 the
pole roots `7/8` and `1/4` coincide modulo 5. Exactly in that shared
class the numerator has its own simple p-adic root (since `N'(t)=240t-89`
is 1 mod either prime). All roots lift uniquely to deeper p-adic digits,
but the numerator can cancel pole valuation. **Do not** apply the four
independent roots theorem to p=3 or p=5.

At the second digit their three local branches split as follows:

- p=3 modulo 9: two poles and the numerator root occupy {2,5,8}, all three children of the collision class 2 modulo 3;
- p=5 modulo 25: corresponding branches occupy {4,19,24}, three of the five children of class 4 modulo 5.

These are exact Hensel/congruence calculations and offer concrete
higher-order small-prime state variables. This is *not* a proof that base 3
alone certifies pi normality.

### 2.3 Multiplicative-order clock coupling (JPC-09)

For an odd prime p the local transport multiplier 16 is a unit. On
p^k-torsion its period is `tau_p(k)=ord_{p^k}(16)`, dividing
`(p-1)p^(k-1)`. For example,

| p | tau_p(1) | tau_p(2) |
|---:|---:|---:|
| 7 | 3 | 21 |
| 11 | 5 | 55 |
| 13 | 3 | 39 |
| 17 | 2 | 34 |
| 19 | 9 | 171 |

The p=7 and p=13 history multipliers share a period-3 clock. **Their
local pole innovations are CRT-independent on complete joint periods;
the propagated historical phases have shared clock factors.** This
identifies a specific nontrivial coupling channel for the existing
SUCC/FUCC synchronized-prime-clock research, not a vague statement that
primes interact. To infer cancellation one must evaluate source-aligned
phases, not multiply independent pole probabilities.

## 3. A formal boundary on independent all-prime completions

### 3.1 No continuous finite-adelic completion (JPC-10, PROVED PAPER)

The finite adele ring `A_f` is the restricted product of all `Q_p` with
respect to `Z_p`: every allowed point has nonintegral coordinates at
only finitely many primes. Let `Zhat=product_p Z_p` have its compact
profinite topology. The nonnegative integers are dense in Zhat by CRT.

**Theorem.** There is no continuous map

$$
R:\widehat{\mathbb Z}\longrightarrow\mathbb A_f
$$

agreeing with diagonal rational `r(n)` at every positive integer n.

*Proof.* A continuous image of the compact `Zhat` is compact in `A_f`.
Every compact subset of the restricted product has a **common finite set
of potentially nonintegral primes**: cover it by finitely many basic
restricted-product neighborhoods, each integral outside some finite set,
and take the union of those sets. Given any such set S, choose a prime
p>=7 outside S and a positive integer n solving `8n=7 mod p`.
The unique p-pole theorem yields `v_p(r(n))<0`, contradicting the
common support restriction. QED.

**Corollary:** no continuous `A_f`-valued extension of the whole original
source `n -> U_n` can exist on all of `Zhat`, since the difference
`U_n-16U_{n-1}=r(n)` would produce the forbidden continuous forcing
extension. This statement is compatible with the legitimate p=2
interpolation `F:Z_2->Z_2`; it forbids a *stronger joint global
continuity property*, not finite-adelic rational source states.

### 3.2 Haar-typical independent clocks leave A_f (JPC-11)

At each prime p>=7 sample `t_p` independently from Haar(Z_p). The pole
events `E_p={v_p(r(t_p))<0}` are independent, with `Pr(E_p)=4/p`. Euler's
classical prime harmonic divergence gives

$$
\sum_{p\ge7}\Pr(E_p)=\sum_{p\ge7}{4\over p}=\infty.
$$

By the **second Borel--Cantelli lemma**, infinitely many E_p occur
almost surely. Exact pole points where r(t_p) is undefined have measure
zero and do not affect the conclusion. Thus the coordinatewise rational
forcing evaluated on independent Haar times is **not** an element of
`A_f` almost surely. A naive independent infinite-prime observer limit
has literally changed the source domain. No continuity, Haar or
independence conjecture is being imposed on the actual diagonal index n.

This is a source-relative completion obstruction, **not** a theorem
about the independence/unprovability of pi normality.

### 3.3 Algebraic pointwise reconstruction need not be uniformly stable (JPC-12)

For odd primes q tending to infinity, take

$$
x_q={q-1\over2q}.
$$

All fixed prime-primary torsion projections eventually see zero, since
the only denominator prime is q. But `x_q mod 1 -> 1/2` in the real circle.
Thus real-phase readout from the algebraic direct sum of primary torsion
coordinates is **not continuous** for the subspace topology inherited
from the product of those discrete primary groups. Any asserted uniform
small-prime approximation needs an additional height/source restriction.

A finite-horizon repair is exact: if `x,y` have a declared common rational
denominator B, lie in `[-R,R]` in the real norm, and their cleared
numerators `Bx,By` agree modulo `M=product p^k`, then

$$
M>2BR\quad\Longrightarrow\quad x=y.
$$

Indeed `B(x-y)` is an integer multiple of M with absolute value <=2BR.
This is rational-reconstruction sufficiency, **not** a statistical saving:
for BBP, both denominator height and the real magnitude can grow sharply
with n. In particular a complete rational description already identifies
one source without proving the asymptotic frequency of its digit gates.

## 4. Joint-source synergy, its genuine control, and the overfit trap

### 4.1 Positive full-factorial synergy witness (JPC-13)

Take six equally weighted rational circle points

$$
X=\{a/2+b/3\pmod1:\ a=0,1,\ b=0,1,2\}.
$$

Let G be the actual hexadecimal zero-bin indicator `1_{0<=x<1/16}`.
Write R(S) for the best L2 error in predicting G from the **joint
p-primary observations** at primes in S. Exact enumeration gives

$$
R(\varnothing)=5/36,\quad R(\{2\})=1/9,\quad
R(\{3\})=1/12,\quad R(\{2,3\})=0.
$$

The complete 2x2 factorial contrast is

$$
\boxed{R(2)+R(3)-R(\varnothing)-R(2,3)=1/18>0.}
$$

Thus each observer individually fails to determine the real gate but
their joint observation determines it exactly. This is a rigorous
finite **existence proof for complementary-observer synergy**, not a
measurement of the pi source's frequency or of quantum interference.

### 4.2 Vanishing individual prime means do not imply a vanishing joint phase (JPC-14)

Let the finite source consist of six samples

$$
(0,0,1/3,5/6,1/6,1/6).
$$

The 2-primary character averages zero (three +1 and three -1). The
3-primary character also averages zero (two each of 1, omega, omega^2),
with `omega=e(1/3)`. But their **source-aligned product** has mean

$$
\boxed{{1-\omega^2\over3}\ne0,
\quad\left|{1-\omega^2\over3}\right|^2={1\over3}.}
$$

This is a decisive counterexample to multiplying marginal cancellation
estimates. It shows *why* the joint Fourier mode must retain synchronized
histories and their interactions.

### 4.3 The finite overfit countercontrol (JPC-15)

For a finite genuine BBP prefix, conditioning the gate indicator on
p=3 and p=5 local rational torsion can already give zero empirical
L2 residual: the pair of residues acts as an almost unique fingerprint
of the time indices. A training model with these fingerprints typically
has many *unseen* signatures on a later holdout. Zero finite empirical
projection error here is state memorization, not genuine future
prediction, let alone an all-scale theorem. The validation receipt
records this failure rather than claiming a source law from finite fits.

## 5. Exact all-prime Fourier carrier, certified error, and the open theorem

### 5.1 An exact synchronized Euler-character **product over primes** (JPC-16)

For any N>=1 and nonzero integer h, write

$$
S_N^{\mathrm{joint}}(h)=
\sum_{n=0}^{N-1}\prod_{\substack{p\le8N-3\\p\ \mathrm{odd}}}
 e(h\lambda_p(U_n)).
$$

The product is **finite at every n**, the factors equal 1 unless that
prime is active in the rational denominator, and the original source
recurrence holds separately in each p-primary group. By CRT,

$$
\boxed{S_N^{\mathrm{joint}}(h)=\sum_{n=0}^{N-1}e(hU_n).}
$$

This equality is source-faithful: we did not replace the index trajectory
with Haar, discard Pascal signs, or independently average local phases.

The inherited BBP positive real kernel has

$$
T_n=16^n\alpha-U_n
=\int_0^1{x^{8n}g(x)\over16-x^8}\,dx>0,
\quad \alpha=\pi/16,
$$

where `g(x)=(1-x)(4+4x+4x^2+2x^3+x^4)`.
As `g(x)/(16-x^8)<1-x` for `0<x<1`,

$$
\boxed{0<T_n<{1\over(8n+1)(8n+2)}.}
$$

Summing and using `sum_{n>=1} 1/n^2<2` gives the finite **uniform in N**
error budget `sum_n T_n<17/32` and thus

$$
\boxed{\left|{1\over N}\sum_{n<N}e(h16^n\alpha)
-{S_N^{\mathrm{joint}}(h)\over N}\right|
< {17\pi|h|\over16N}.}
$$

This is an explicit *all-prime source-to-pi* readout theorem. The
`O_h(1/N)` bridge is not a proof of cancellation inside the joint sum.
It is a sharper statement of exactly what would have to cancel, and how
much deterministic source-to-pi error has already been paid.

Weyl's criterion together with Wall's base-normality characterization
says **base-16 normality of pi is equivalent to**

$$
\boxed{\forall h\in\mathbb Z\setminus\{0\},\qquad
S_N^{\mathrm{joint}}(h)=o(N).}
$$

This is a correct reduction, **not** a new sufficient estimate or proof.
Controlling all digit blocks or an adequate discrepancy norm requires
source-specific uniform estimates. Nothing in the four-pole CRT law
alone gives this limit.

### 5.2 A source-selected, prime-memory interaction debt (JPC-17--18)

Let `X_{p,n}(h)=e(h\lambda_p(U_n))`. The actual sample mean over
`n<N` is `E_N`. For finite prime set `P={p_1,...,p_d}` and the
prefix products `Y_j=product_{i<=j}X_{p_i}`, define

$$
C_j=E_N[Y_{j-1}X_{p_j}]-E_N[Y_{j-1}]E_N[X_{p_j}]
\quad(j\ge2).
$$

Repeated use of the **identity**
`E_N[Y_j]=E_N[Y_{j-1}]E_N[X_{p_j}]+C_j` gives

$$
\boxed{E_N\prod_{i=1}^dX_{p_i}
=\prod_{i=1}^d E_N X_{p_i}
+\sum_{j=2}^d C_j\prod_{i=j+1}^d E_N X_{p_i}.}
$$

This is an exact, orientation-preserving mixed-correlation decomposition,
not an assumption that the `C_j` are small. The six-state counterexample
has zero prime marginals and nonzero joint product, so the interaction
terms cannot be dropped. The ordering of prime factors changes individual
`C_j` but not the total. A meaningful new bound must be invariant under
an audited choice of order or keep all orders/ablations visible.

One can now target the *actual* selected interactions on BBP prime-pole
windows. A theorem making the RHS `o(1)` uniformly as the prime window
grows would close the Weyl criterion. Such a theorem is **UNVERIFIED**.

Forcing-activation CRT independence alone does not meet it: the
multiplicative order clock `ord_{p^k}(16)`, the shared source time and
integer lift create precisely the unbounded dependency terms. Moreover
there is no generic extension from profinite Haar forcing to an admissible
finite adele, as §3 proves.

## 6. Exact finite experiments and hostile gates

The production module `observational_succ/pi_joint_prime_carrier.py`,
new tests in `tests/test_pi_joint_prime_carrier.py` and
`tests/test_pi_joint_pole_clocks.py`, and standalone script
`scripts/pi_joint_prime_carrier_probe.py` implement the synchronized
source and its failure controls.

Important controls:

1. **Independent original-pole vs odd-denominator source:** exact Fractions at 256+ times; denominator odd.
2. **Local character reassembly:** direct reduction `U_n mod 1` equals the sum of all active odd-prime primary components at each tested time.
3. **Local dynamics:** actual p-primary states satisfy the original 16-multiplier and exact four-pole innovations, including special p=3/5.
4. **Dyadic nontriviality:** local p=2 torsion zero but 2-adic integral residues permute mod `2^k` at k<=9 (inherited paper proof).
5. **Pascal interoperability:** signed finite differences commute with authentic p-primary projections; p=3 support-mask mutation fails.
6. **Two-prime full factorial:** synthetic 1/18 information synergy and an adversarial marginal-product counterexample.
7. **Prime-power poles:** complete residue enumerations, p>=7 noncancellation, first births, exceptional 3/5 Hensel lifts, shared 16-memory clock periods.
8. **True four-bit gates:** the exact positive source tail certifies the first hexadecimal digit for each source step 1..512 in the frozen check. Counts are finite statistics, not pi normality.
9. **Time-alignment mutation:** cyclically shift a prime-3 component through a fixed source prefix; its individual marginal stays exactly the same but the *joint* resulting real-digit histogram changes. This explicitly breaks the original source.
10. **Finite memorization trap:** p=3,5 local fingerprints can completely fit a finite gate sample while leaving many new holdout signatures unresolved.

No result uses the decimal expansion of pi as a construction input.
The separately labelled `mpmath.pi` gate check is an oracle against the
source/tail code, not a rigorous interval certificate; exact rational
positive-kernel inequalities supply the certificates.

## 7. Decision table and next falsifiers

| Proposition | Verdict | What is still owed |
|---|---|---|
| Joint p-primary phases reconstruct each rational U_n exactly | PROVED PAPER + VERIFIED FINITE | none within Q/Z scope |
| Pascal signed differences commute with all primary projections | PROVED PAPER | p-adic precision after changing coefficients requires integrality |
| BBP odd-prime pole events factor on exact CRT periods (p>=7) | PROVED PAPER + VERIFIED FINITE | phase/history event coupling |
| p=3,5 have honest numerator/pole collisions | PROVED PAPER + VERIFIED FINITE | full local long-memory joint frequencies |
| Independent Haar observer clocks produce valid A_f forcing | REFUTED (BC + compactness receipts) | synchronize on actual diagonal source |
| Small-prime torsion readout uniformly determines real phase | REFUTED (hidden-new-prime receipt) | source-relative height or full moving support |
| Two individually blind prime observers can jointly identify a gate | PROVED PAPER on explicit six-state control | actual selected BBP gate correlations |
| Authenticated joint prime sum has `o(N)` Fourier cancellation | **UNVERIFIED** | new arithmetic estimate, not an identity |
| Pi normality / unknowability | **OPEN / NOT ESTABLISHED** | Weyl saving or genuine logical independence theorem |

**Best next probe:** choose frozen BBP windows at prescribed scales and
an explicit exact signed Fourier mode h. For each n, record (i) the full
integer source and certified real gate, (ii) 2-adic integral residue,
(iii) *all* active odd-primary characters, (iv) 3/5 exceptional-root state,
(v) p>=7 pole-depth clock events, and (vi) the `ord_{p^k}(16)` memory
phase. Compute the exact/multiprecision joint character sum, all
single-family ablations, and the full 2x2 factorial contrast for a
predeclared pair. Require the selected joint-sum cancellation to beat a
proved adversarial bound on fresh untouched windows. The first theorem to
seek is a nontrivial uniform deficit for the **authentic mixed
source-phase correlation**; normality does not follow from the new
CRT laws without that estimate.

## 8. Attribution, sources, and scope

- Parent research #270/#272/#273/#274 supplies the exact BBP recurrence, the initial-zero source, positive real tail, dyadic isometry and Pascal quotient. Their historical claims remain untouched.
- Classical ingredients: Lucas's theorem; the Chinese remainder theorem and `Q/Z = direct sum of p-primary torsion`; standard additive characters and the rational adelic product identity; the second Borel--Cantelli lemma; divergence of the prime reciprocal series (Euler); Mertens' theorem and PNT for the optional average-pole asymptotic; Weyl's criterion and Wall's normality criterion.
- Keith Conrad, *The character group of Q* (local additive character and finite-adele sign convention): https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf . Our local character sign is chosen so the product of `e(+lambda_p(x))` equals `e(+x)`; the conventional adelic character trivial on diagonally embedded Q uses its complementary infinite sign.
- Malabika Pramanik, *Normal numbers — background*, 2024 slides, Weyl and Wall: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/0/26656/files/2024/06/Normal_Numbers_Background.pdf .
- Independent novelty and peer review of these source-specific elementary deductions are not established. A paper proof is not Lean kernel certification. Nothing here claims a proof of base-16, decimal or absolute normality of pi.
