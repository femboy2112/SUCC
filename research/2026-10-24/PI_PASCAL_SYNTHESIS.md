# Pascal geometry, the authentic BBP source, and the normality frontier

**Date:** 2026-10-24. **Branch:** `research/pi-pascal-mahler-source-2026-10-24`.
**Parent:** draft #270, `3acd547ff122368d5694efdab029b3156a292d8a`.
**Main inspected:** `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Authority:** paper proofs, named classical inputs, and exact finite checks.
**Pi normality, real half retention, and same-law tripling remain OPEN.**

## 1. Outcome and the precise role of Pascal

Pascal's triangle gives substantial exact arithmetic for the authentic BBP
source. Its signed rows expose the entire dyadic difference profile, a sharp
polynomial approximation theorem, positive beta kernels, and coherent source
filters for every integer base. The fixed four poles also impose finite
recurrences and fresh-prime constraints on translated Pascal rows.

None of these statements yet bounds the frequency of the real central carry.
The principal advance is a set of exact source theorems together with stronger
counterexamples specifying which extra information a successful proof must use.
The broad implication from Pascal valuations and positive real kernels to real
mixing is refuted. The narrower fixed-BBP carry problem remains open.

The user's observation about powers of two is literally the row-sum identity

$$
\sum_{j=0}^k\binom kj=2^k.
$$

Individual entries also encode prime carries by Kummer's theorem, and their
prime residues obey Lucas's theorem. Those classical facts describe counts and
divisibility. They do not assign independent probabilities to four successive
carry decisions of one selected trajectory. In this round we apply the signed
row to the actual source before drawing any probabilistic conclusion.

The main proof dossiers are:

- [Full dyadic profile and sharp Mahler degree](PI_PASCAL_MAHLER_SOURCE.md).
- [Positive real kernels, all-base filters and carry costs](PI_PASCAL_REAL_KERNEL.md).
- [Full-profile positive-moment countermodels](PI_PASCAL_ADVERSARIAL_BOUNDARY.md).
- [Minimal recurrences and the integer base-31 filter](PI_PASCAL_HOLONOMIC_FRONTIER.md).
- [Fresh-prime restrictions and source denominator heights](PI_PASCAL_PRIME_HEIGHT.md).

The [PJT claim supplement](../../docs/CLAIM_SUPPLEMENT_PASCAL_SOURCE.md),
[frozen hole contract](PI_PASCAL_HOLE_CONTRACT.md),
[exact receipt](PI_PASCAL_RECEIPT.json), and
[validation record](PI_PASCAL_VALIDATION.md) separate the earned authorities.

## 2. Live frontier and historical reconstruction

The relevant prior conversation and repository threads already distinguished
Pascal/Gamma valuations, circle-chord Haar moments, ordered versus unordered
paths, and the need to sample the actual source. In particular, Pascal heat
intuition previously needed independent steps; scalar binomial counts did not
prove them. This round does not revive that inference.

The current inherited chain is main, draft #268 at
`06f6b03eed2521c6bd5c02db618cb421ac6b5a51`, then draft #270 at the parent above.
The separate draft #269 at `b445b0d9c604f45548a45b5db4f31428f73b35a2`
was inspected as a donor, not merged or treated as inherited authority.
Its finite base-conversion and signed Ramanujan-shell identities do not give
the missing real retention frequency.

A late live-frontier check also read sibling [draft #271](https://github.com/femboy2112/SUCC/pull/271)
at `4eafc6151e9a494f2aea8ec79ca6cf5608152c80`. It remains unmerged here.
Its complete four-bit Walsh contrast and source-corrected Fourier jet
complement this branch. The analytic remainder was audited, and the bounded
phase-removal corollary below records the additional deduction precisely.

The actual source, with its original normalization, is

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n),\quad y_n=\{U_n\}.
$$

The inherited dyadic interpolation is

$$
F(t)=\sum_{j\ge0}16^j r(t-j),\qquad F(0)=0,\quad F(n)=U_n.
$$

It is a bijective isometry of the dyadic integers. The resulting exact
one-half and one-sixteenth refinements concern unwrapped dyadic residue
collisions. An unconditional real-circle half-retention estimate has not been
proved. This distinction is essential when reading “we have a half bound.”

There are still two closure paths:

1. Control the cumulative excess of the four conditional carry-bit losses,
   strongly enough to close the inherited prescribed-scale collision bound.
2. Obtain any positive all-scale real collision exponent and invariance under
   multiplication by 3 of the **same** selected source laws. The inherited
   classical rigidity argument would then yield binary normality.

The second route does not require separately proving base-3 normality, nor
normality in every prime base below 16. It does require its two real-source
hypotheses. A new ternary formula for pi supplies neither by itself.

## 3. Exact Pascal arithmetic of the fixed source

Write $\Delta f(t)=f(t+1)-f(t)$ and let $s_2(k)$ count the ones in the
binary expansion of $k$. For all $k\ge1$ and all $t\in\mathbb Z_2$,

$$
\boxed{v_2(\Delta^k r(t))=v_2(\Delta^kF(t))
=k-1+v_2(k!)=2k-s_2(k)-1.}
$$

The proof is source-specific and elementary. The reciprocal identity

$$
\Delta^k\frac1{at+b}
=\frac{(-a)^k k!}{\prod_{j=0}^k(a(t+j)+b)}
$$

is applied to

$$
r(t)=\frac4{8t-7}-\frac1{8t-3}
-\frac1{2(2t-1)}-\frac1{2(4t-1)}.
$$

For dyadic integral $t$, every denominator factor is odd. The slope-2
term has uniquely smallest valuation. Its competitors exceed it by
$k$, $2k+1$, and $2k+3$. Therefore cancellation cannot raise its valuation.
The Green series transfers this exact profile to $F$; its first term is
the unique minimum. In fact, writing $\nu(k)=2k-s_2(k)-1$,

$$
v_2(\Delta^kF(t)-\Delta^kr(t))=\nu(k)+4.
$$

Let $A_k=\Delta^kU_0$. Its rational coefficients obey

$$
A_0=0,\qquad A_{k+1}=15A_k+\Delta^kr(1).
$$

They are the Mahler coefficients of $F$. The finite Newton identity on
nonnegative integers, uniform coefficient decay, and density of those integers
in $\mathbb Z_2$ prove the global expansion. This use of the classical Mahler
coordinate system should not be mistaken for a novel general expansion theorem.

There is also a sharp result about information at finite dyadic precision.
For either $f=r$ or $f=F$, with its Mahler truncation $P_D$,

$$
\|f-P_D\|_\infty=2^{-\nu(D+1)}
=\inf_{\deg P\le D}\|f-P\|_\infty.
$$

The infimum includes every polynomial over $\mathbb Q_2$. Applying
$\Delta^{D+1}$ at zero gives the lower bound, since that operator has
sup-norm at most one and kills all degree-$D$ polynomials. The truncation
attains the bound. Hence the minimal degree modulo $2^B$ is

$$
D_B=\max\{k\ge1:2k-s_2(k)-1<B\}=B/2+O(\log B).
$$

| Precision $B$ | 8 | 16 | 32 | 64 | 128 | 256 |
|---|---:|---:|---:|---:|---:|---:|
| Exact minimal degree $D_B$ | 5 | 9 | 17 | 33 | 65 | 129 |

This is a sharp representation theorem, not a speed claim over the inherited
backwards evaluator. Exact coefficient and binomial sizes must be paid for.

### A concrete failure of automatic transfer to the circle

For $n\ge1$ and $0\le D\le n$,

$$
\frac{|P_D(n)|}{U_n}
\le\frac{16(D+1)(17n)^D}{15\,16^n}.
$$

At $n=128$, the degree-9 polynomial gives the source exactly modulo $2^{16}$,
yet its real relative magnitude is below $2^{-400}$. The exact receipt gives
its circle distance from $U_{128}$ in
$(0.07848964664540803521660,0.07848964664540803521661)$, which exceeds $1/16$.
The inequality is a paper theorem; the particular phase gap is VERIFIED_FINITE.

Odd primes have a different geometry. Their valuations count the prime powers
among the reciprocal denominator factors. Multiple four-pole minima can cancel:
at $(t,k,p)=(0,1,3)$ the weighted pole valuations are $(0,-1,0,-1)$,
but $\Delta r(0)=83/35$ has valuation zero. The dyadic unique-minimum
argument cannot be copied unchanged to every prime.

## 4. What the positive real kernel supplies

Set $\alpha=\pi/16$ and

$$
g(x)=4-2x^3-x^4-x^5
=(1-x)(4+4x+4x^2+2x^3+x^4).
$$

The authentic real error is the positive moment

$$
T_n=16^n\alpha-U_n
=\int_0^1\frac{x^{8n}g(x)}{16-x^8}\,dx.
$$

The signed forcing and tail differences are

$$
D_{n,k}=\int_0^1x^{8n}g(x)(1-x^8)^k\,dx,
\qquad
R_{n,k}=\int_0^1\frac{x^{8n}g(x)(1-x^8)^k}{16-x^8}\,dx.
$$

Both are positive. Expanding $g$ gives an exact rational beta formula for
$D_{n,k}$, and

$$
\frac{15}{64}\mathrm B(n+1/8,k+2)<D_{n,k}
<\frac12\mathrm B(n+1/8,k+2),\qquad
\frac{D_{n,k}}{16}<R_{n,k}<\frac{D_{n,k}}{15}.
$$

The geometric expansion of $(16-x^8)^{-1}$ gives an arbitrarily tight
positive rational enclosure, with an explicit one-sided remainder.
Consequently

$$
\boxed{A_k=15^k\alpha-(-1)^kR_{0,k}},\qquad
R_{0,k}\sim\frac{\Gamma(1/8)}{32k^{1/8}}.
$$

Signed Pascal rows thus supply an actual base-15 source with vanishing
absolute error. Unsigned rows instead give base 17 with an absolute remainder
asymptotic to $2^k/(16k^2)$, which grows. A small relative error is insufficient
for passing to fractional parts. Nor does a large absolute error alone prove
a large circle error; both distinctions are retained in the report.

## 5. Coherent prime-base filters and their exact carry cost

For $q\ge2$, $d\ge1$, define

$$
X_k^{q,d}=\left(\frac q{15^d}\right)^k A_{dk}.
$$

Then

$$
X_k^{q,d}=q^k\alpha
-(-1)^{dk}\left(\frac q{15^d}\right)^kR_{0,dk}.
$$

The error tends to zero whenever $q\le15^d$. In particular
$A_k/5^k$ shadows $3^k\pi/16$, and $A_k/3^k$ shadows $5^k\pi/16$.
Every prime below 16 uses $d=1$.

The operators $P_{q,d}(E)=q(E-1)^d/15^d$ compose exactly:
$P_{q,d}P_{r,e}=P_{qr,d+e}$. Choosing an additive prime-factor degree
$D(q)$, as defined in the kernel report, gives

$$
X_k^{16,4}=X_{2k}^{4,2}=X_{4k}^{2,1}.
$$

This satisfies the requested coherence across powers of a base. It is a
coherence theorem about source constructions, not an invariance theorem for
their empirical laws.

If $q/15^d=a/b$ in lowest terms and $A_{dk}=C_k+x_k$, with
$C_k\in\mathbb Z$ and $0\le x_k<1$, then

$$
\{X_k^{q,d}\}
=\left\{\frac{a^k(x_k+(C_k\bmod b^k))}{b^k}\right\}.
$$

For a universal readout across unrestricted integer lifts, the $b^k$
classes give distinct answers. This does not claim all classes occur along
the actual source or rule out a structural way to compute them. It does
show why merely retaining the input fractional part is insufficient.
At $k=1$, dividing $A_1=47/15$ by 5 gives phase $47/75$; dividing only
its fractional part gives $2/75$.

Direct scaling was already available:
$Y_k^{q,d}=(q/16^d)^kU_{dk}$. Its real error is asymptotically smaller
at matched $d$. Thus the new feature is the signed difference arithmetic
and the changed division cover, not the existence of arbitrary base shadows.

| Target base, $d=1$ | Pascal carry modulus | Direct carry modulus |
|---|---:|---:|
| 2 | $15^k$ | $8^k$ |
| 3 | $5^k$ | $16^k$ |
| 5 | $3^k$ | $16^k$ |
| 7, 11, 13 | $15^k$ | $16^k$ |

For this family the auxiliary denominator primes are 3 and 5. Their required
depth grows; a finite prime list is not a uniformly bounded information budget.
Moreover, the BBP source itself accumulates other odd denominator primes.

### A useful additional prime: 31

For a fixed nonconstant integer polynomial $P$, a vanishing absolute kernel
error requires $|P(t)|\le1$ on $[0,1]$. Hence $P(0),P(1)\in\{-1,0,1\}$.
If $P(16)=q$, necessarily

$$
q\bmod16\in\{0,1,15\},\qquad q\bmod15\in\{0,1,14\}.
$$

The smallest prime admitted by this mechanism is 31, realized by $P(t)=2t-1$.
Thus $(2E-1)^kU_0$ shadows $31^k\alpha$ with an explicit vanishing
error and no extra division-cover label. Its coefficient norm is $3^k$.
This is limited to the stated integer-polynomial mechanism; it is not a
universal restriction on prime-base transfer.

At a translated start, two exact local identities are especially transparent:

$$
\frac{U_{n+1}-U_n}{5}=3U_n+\frac{r(n+1)}5,
\qquad
2U_{n+1}-U_n=31U_n+2r(n+1).
$$

Their output laws approach $(T_3)_*\mu$ and $(T_{31})_*\mu$ with explicit
$O(A^{-2})$ errors on windows starting at $A$. Proving that an output law
also approaches $\mu$ is still the missing symmetry. The identities do not
make it follow. One tripling test uses a fixed five-cover coordinate per
sample; iterating the filter is the operation that spends $5^k$ precision.

## 6. What is special about the four poles beyond the generic profile

The four beta components give an explicit minimal recurrence. With
$\mathcal B=k(E^{-1}-1)$ and
$\mathcal P(z)=(8z-1)(2z-1)(8z-5)(4z-3)$,

$$
\mathcal P(\mathcal B)D=0.
$$

Its order over $\mathbb Q(k)$ is exactly four. The distinct fractional
asymptotic exponents prevent a lower-order annihilator. With
$\mathcal C=-k(E^{-1}+1)$,

$$
\mathcal P(\mathcal C)(E-15)A=0
$$

has exact minimal order five. It gives an integer relation among six
consecutive phases and their carries, with coefficients of degree at most
four. Every fixed rational base filter also has minimal recurrence order
five. This finite rank is real information, but a separate positive rational
clustering source can have the same rank and exponent classes. The exact
coefficients and initial data, not the rank alone, distinguish BBP.

There is also a local obstruction to exact phase locking. For a prime
$p\equiv1\pmod8$, put $b_p=(p+7)/8$, $c_p=4$; for
$p\equiv5\pmod8$, put $b_p=(p+3)/8$, $c_p=-1$.
For $b_p\le n\le(p-1)/2$,

$$
U_n=\frac{c_p16^{n-b_p}}p+\text{a $p$-integral rational}.
$$

Consequently, if $P\in\mathbb Z[E]$, its entire translated support lies
in that interval, and $p\nmid P(16)$, then
$v_p(P(E)U_n)=-1$. For Pascal differences $P=(E-1)^k$, this applies
when $p\nmid15$. The corresponding phase cannot be exactly integral.
The real separation furnished by the common denominator is only of order
$1/\operatorname{lcm}(\text{odd integers}\le8(n+k)-3)$.

Writing $D_n$ for the reduced odd denominator of $U_n$, the two prime classes
give an explicit product dividing $D_n$, while
$D_n\mid\operatorname{lcm}(\text{odd integers}\le8n-3)$.
The classical prime number theorem in the fixed residue classes modulo 8
therefore gives

$$
(3+o(1))n\le\log D_n\le(8+o(1))n.
$$

Thus a generic polynomial-height shortcut is unavailable: these source
denominators are exponentially large. The fixed formula may still provide
stronger cancellation or counting information; height alone does not.

The source row beginning at zero requires particular care. Its binomial
coefficients can cancel a prime introduced partway through that row.
For $p=89$, $b_p=12$, and $k=35$, the relevant local residue cancels and
$v_{89}(A_{35})=0$. The translated all-after-birth lemma cannot be applied
to this origin row. The exact adverse example remains in the receipt.

## 7. Countermodels that a new estimate must survive

There exists an entire positive density $w$ with $3/2<w<5/2$ on $[0,1]$
and rational moments

$$
\eta_n=\int_0^1x^n(1-x)w(x)\,dx,\qquad \eta_0=1,
\qquad H(n)=16^n-\eta_n.
$$

Its dyadic interpolation and its forcing have the same full valuation profile
as the authentic source. For any fixed precision $L$, it can match every
normalized authentic Pascal difference to that precision, uniformly in
dyadic input and difference order. Yet its real phases cluster completely,
its literal carries are 15, and its forcing is positive, completely monotone,
and of quadratic real decay.

The construction uses rational orthogonal polynomials for the weight $1-x$.
At each order, a small rational perturbation changes the next moment without
changing earlier moments. Rational dyadic congruence classes are dense in the
real line, allowing both the desired dyadic coefficient and an arbitrarily
small real perturbation. Disk bounds ensure convergence to an entire density.
This changes the exact four-pole BBP forcing. It is not a counterexample to pi
normality, nor a construction with the original rational function of time.

The executable polynomial-density control certifies a finite number of jets.
Its positive real moment sequence exists at every time, but its dyadic jet
certificate stops at the declared depth. A retained depth-2 example fails
the desired third normalized valuation: it has valuation $-1$ instead of 2.
The separate infinite construction is essential to the all-order theorem.

Normalized Pascal averaging has a different exact obstruction. The operator
$2^{-m}\sum_j\binom mj f\circ T^j$ preserves every $T$-invariant law.
On a finite window of length $N$ its average differs from that of $f$ by at
most $m\|f\|_\infty/N$, with sharp endpoint examples. It cannot turn a
stationary non-Haar law into Haar by reweighting its translates.

## 8. The surviving proof targets, with a stop rule

### Paper followup: even the real constant can be prescribed

A final strengthening is proved in
[the prescribed-constant addendum](PI_PASCAL_PRESCRIBED_CONSTANT.md).
For every positive real $C$ and fixed dyadic precision $L$, the orthogonal
moment construction can start from density $2C$, keeping total tail mass $C$.
At every stage choose the next Newton coefficient in the same rational
dyadic coset as before. The density corrections may now be real rather than
rational. The resulting density is entire and lies between $3C/2$ and $5C/2$.

The zero-initial source still has **rational values at every integer**, a
compatible analytic dyadic interpolation with the full authentic profile and
fixed-precision agreement, and positive completely monotone real-analytic
forcing of quadratic decay. Its real source states are

$$
H(n)=C16^n-\eta_n,\qquad \eta_n=O_C(n^{-2}).
$$

When $C$ is irrational, the tail moments $\eta_n$ need not be rational;
the values of $H$ and its forcing are rational by the Newton construction.
No common power series converging in both completions is asserted.

The same construction can also satisfy arbitrary fixed precision at **any
fixed finite set of primes**. In particular, at every nonnegative integer
time it can agree with the authentic rational source modulo $p^L$ for each
$p\in\{2,3,5,7,11,13\}$, while retaining the full dyadic profile. The
origin Newton coefficients can match their relative precision at those
primes as well. Denominators coprime to the finite prime set keep the
required rational cosets dense in the real line. No analytic interpolation
on every odd $\mathbb Z_p$ is asserted. This is a finite-place congruence
counterexample; it does not refute the separate conditional theorem using
real tripling invariance of the selected law.

Choose $C=\sum_{j\ge2}16^{-j!}$. Elementary rational approximations prove
this constant transcendental. Its nonzero base-16 digits have density zero,
so its empirical circle law is a point mass at zero, and the source tail
preserves that law. On windows comparable to $[u,4u]$, all but
$O_C((\log u)^2)$ source indices and their required successors cluster
within $O_C(u^{-2})$ of the same circle point. Central retention consequently
tends to one at the prescribed polynomial radii. Thus even transcendence
does not rescue the generic profile-plus-positive-kernel inference.

Positive absolute precision at every prime simultaneously would instead
force equality of the corresponding rational values; the finite-prime
construction does not make that assertion. Exact source identification
alone still does not provide its statistical estimate.

This construction still changes the exact BBP four-pole function. It does
not supply the authentic common-denominator restrictions or a finite
rational forcing formula. The addition is a paper theorem, with no new
finite test count or formal-kernel authority.

### Closure targets

The newly available [sibling carry-jet proof](https://github.com/femboy2112/SUCC/blob/4eafc6151e9a494f2aea8ec79ca6cf5608152c80/research/2026-10-24/PASCAL_CARRY_INTERFEROMETRY.md)
makes the full four-bit interaction explicit. With $b_j$ the four bits of
$\kappa\bmod16$ and $\sigma_j=(-1)^{b_j}$,

$$
16\mathbf1_{\kappa\equiv0\ (16)}=\prod_{j=0}^3(1+\sigma_j).
$$

The interaction groups have Pascal multiplicities $(1,4,6,4,1)$. Uniform
even-parity words have every one-, two-, and three-bit marginal uniform,
while the zero word has probability $1/8$. Thus the fourth interaction
cannot be discarded on the strength of all lower-order tests. This is an
observation-class counterexample, not an authentic BBP trajectory.

### A bounded forcing-phase removal (PROVED LOCAL)

Keep the authentic source and the exact selected mask. For $p=8m+1\ge17$,
let $W=\{m+1,\ldots,4m-1\}$, $D=3m-1$, and let
$E_\tau=\{(s,t)\in W^2:|\delta^+_{s,t}|\le\tau\}$ for
$\epsilon_p<\tau\le1/4$. Here $\delta^+$ is the centered successor
difference, $Q_0=|E_\tau|$, and
$\eta_{s,t}=r(t+1)-r(s+1)$ obeys
$|\eta|\le\epsilon_p<15/[(p+8)(p+9)]$. Let $Z$ count its zero centered
carry branch, and $H=\{-7,\ldots,-1,1,\ldots,8\}$.

The integer carry identity and cyclic character orthogonality give

$$
16Z-Q_0=\sum_{h\in H}\sum_{E_\tau}
e(h(y_t-y_s))e(h(\eta-\delta^+)/16),\qquad e(x)=e^{2\pi ix}.
$$

Remove only $\eta$ from the exponential phase, defining

$$
S_0=\sum_{h\in H}\sum_{E_\tau}
e(h(y_t-y_s))e(-h\delta^+/16).
$$

Since $\sum_{h\in H}|h|=64$ and
$|e(x)-e(y)|\le2\pi|x-y|$,

$$
\boxed{|16Z-Q_0-S_0|\le8\pi Q_0\epsilon_p<1485/28.}
$$

The last constant follows from $Q_0\le D^2<9p^2/64$ and $\pi<22/7$.
No source distribution estimate is used. The same exact mask $E_\tau$
and the actual successor values remain throughout.

Let $\widetilde{\mathcal J}_2$ replace $e(-h\delta^+/16)$ in $S_0$
by its degree-two Taylor polynomial. The real-argument integral remainder
gives

$$
|16Z-Q_0-\widetilde{\mathcal J}_2|
\le8\pi Q_0\epsilon_p+
\frac{15Q_0}{6}\big((22/7)\tau\big)^3.
$$

At the inherited terminal radius $\tau\asymp p^{-2/5}$, this is
$O(1)+O(p^{4/5})=o(D)$. At every prescribed scale, choosing Taylor degree
$\lceil\log p\rceil$ gives $O(1)+o(1)$, still $o(D)$; it does not give
$o(1)$ after the forcing-phase removal. The first term is uniformly bounded.

The hard selected sum remains. For a trigonometric cutoff $K$, its leading
conditional term at an outer frequency $h$ is exactly

$$
\sum_\ell\widehat K(\ell)
\left|\sum_{n\in W}
e\big((h+16\ell)y_n+\ell r(n+1)\big)\right|^2.
$$

Thus fifteen fixed outer frequencies do not imply a fixed bandwidth: the
near-return cutoff retains further frequencies. Removing forcing from the
discontinuous mask would require a new boundary-count bound. The clustering
controls have small Taylor errors and interaction sums of quadratic size.
The corollary pays a deterministic phase budget, not a cancellation budget.

### The statistical estimate still required

The frozen principal question was whether Pascal differences plus the fixed
real kernel control conditional alignment of the real carry. This round
proves exact components and refutes several generic shortcuts. It does not
answer that principal question positively.

The direct closure target remains, on the inherited windows and scales,

$$
\prod_{j<J}\theta_j\le16^{-J}p^{o(1)},
\qquad
\left[\log\!\left(16^J\prod_{j<J}\theta_j\right)\right]_+
=o(\log p).
$$

Here $[x]_+=\max(x,0)$, and $\theta_j$ is the actual central carry retention conditioned on
successor closeness. Writing $\theta_j=\prod_{\ell=1}^4\rho_{j,\ell}$
does not make the four conditional factors independent. Four half losses
would work; two half losses give only $1/4$. The factorization $16=4^2$
corresponds to two quarter losses, not two half losses.

The strongest surviving experimental contract is to test the **fixed**
four-pole formula and its exact six-phase relation against the conditional
carry fibers on selected prime windows, retaining the correlated prime
residues and all endpoint/diagonal costs. A successful new lemma must give
a frequency or transport estimate that fails for the explicit clustering
controls. Re-deriving the source recurrence, its finite rank, a base shadow,
or an equivalent Fourier/transport target does not count as that estimate.

The height results delimit a second possible route: a genuinely different
Padé or simultaneous-place construction would need to improve numerator
cancellation enough to overcome exponential authentic denominators. The
existing minimal-degree dyadic truncation does not do this; its real norm
and phase control have been explicitly measured. This is a potential next
arithmetic tool, not an established sufficient theorem disguised as progress.

Base 3 remains sufficient for the **conditional** rigidity route. The new
base-31 integer filter is a clean alternative observable if it makes a
source-law symmetry estimate easier. No result here proves such symmetry
for either prime. The option to use all primes remains available, but the
current identities do not demand a sweep through every prime below 16.

### Two additional checks on arithmetic shortcuts

The inherited source windows correspond to true-orbit indices
$j=u,\ldots,4u-1$ for $p=8u+1$. Suppose, for a fixed nonzero integer $h$,
that $\|h16^j\pi\|<\varepsilon=1/18$ throughout such a window. Write
$e_j=h16^j\pi-a_j$ for its nearest-integer errors. The integer
$e_{j+1}-16e_j$ has modulus below $17\varepsilon<1$, so it is zero.
Consequently

$$
\left|\pi-\frac{a_u}{h16^u}\right|
<\frac{\varepsilon}{|h|}\,16^{-(4u-1)}.
$$

An irrationality lower bound $|\pi-a/q|\ge c q^{-\mu}$ gives an
asymptotic contradiction by this exponent comparison if $\mu<4$.
The inherited weaker input $\mu<8$ does not establish that. Taking
$h=16^d-1$ tests concentration near a fixed period-$d$ rational cycle.
This calculation does not claim such windows exist; it shows why the
available irrationality estimate alone fails to exclude them. Irrationality
does rule out approaching the same finite periodic orbit at every sufficiently
late time. That weaker global exclusion is not a frequency bound.

The exact simple-pole class also excludes a rational source constant by a
classical theorem. For $r(n)=\sum_{j=1}^{a-1}c_j/(an-j)$ with rational $c_j$,
$b\ge2$, $z=b^{-1/a}$, and $\zeta=e^{2\pi i/a}$, a root-of-unity filter gives

$$
\sum_{n\ge1}b^{-n}r(n)
=-\frac1a\sum_{j=1}^{a-1}\sum_{\ell=0}^{a-1}
c_jz^j\zeta^{\ell j}\operatorname{Log}(1-\zeta^\ell z).
$$

The logarithms are the determinations defined by their convergent power
series. Baker's theorem makes a nonzero such algebraic linear combination
transcendental. Strictly positive forcing ensures nonzero value; BBP has
$a=8$, $b=16$. This excludes the rational constant used by our positive-moment
countermodel within this particular pole-location class. General rational
poles can add algebraic boundary terms, so the assertion is not silently
extended to them. This is classical transcendence information, with no new
conditional carry loss.

## 9. Literature and priority boundary

- Kummer/Lucas carry arithmetic and binomial prime-power congruences:
  Andrew Granville, [Arithmetic properties of binomial coefficients](https://dms.umontreal.ca/~andrew/Binomial/intro.html).
- Mahler expansion is classical; see Keith Conrad's
  [Mahler Expansions](https://kconrad.math.uconn.edu/blurbs/gradnumthy/mahlerexpansions.pdf).
  The original 1958 article's [bibliographic record](https://doi.org/10.1515/crll.1958.199.23)
  was located; its full paywalled text was not used as if read.
- Jeffrey Lagarias, [On the Normality of Arithmetical Constants](https://arxiv.org/abs/math/0101055),
  explains why a general perturbation/source identity is insufficient and
  treats the rational-function and G-function structure. This is the closest
  classical methodological comparison, not a claimed new solution of Hypothesis A.
- David Bailey and Richard Crandall,
  [Random Generators and Normal Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf),
  is relevant background for dynamical source descriptions.
- The denominator asymptotics import the classical prime number theorem and
  its fixed-modulus version; see Terence Tao's
  [254A Notes 2, Exercise 55](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
- Baker's [Linear forms in the logarithms of algebraic numbers III](https://doi.org/10.1112/S0025579300003843)
  excludes nonzero algebraic logarithmic combinations from being algebraic.
  For the appropriate simple-pole source class this excludes rational source
  constants, but this classical transcendence information is not a digit-frequency bound.

The source-specific formulas and countermodels above have paper derivations
and exact calibration. No academic priority or formal-kernel certification is
asserted. The three research lanes use the same model; their cross-audits and
distinct exact implementations are not independent external refereeing.
