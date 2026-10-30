# Stoneham transfer, adjacent BBP conductors, and typed arithmetic gluing

**Research only, 2026-10-30.** Parent PR #398, exact source head
`1a1524de28b155139d8fe84ea90fc2f117fbb9f3`, Main XVI ancestor
`e18ba565ca540adb7edf3292f5593929e76d91c5`. All additions are in this directory.
Original signed poles, zero seed, archives, and historical contracts are unchanged.
**Pi normality and RH remain OPEN.** These are elementary paper proofs plus finite
exact checks, not Lean proofs or externally refereed scholarly-priority claims.

The positive result is a constraint on the exact original rational trajectory:
the smallest equally spaced translated circle grid containing two successive BBP
states has exponentially many sites. It decisively excludes one natural Stoneham
transfer architecture. It does not give signed real-circle cancellation.

## 1. Source and exact translated-grid barrier (TR-01, TR-02)

Write

\[
r(n)=\sum_{d\in\{1,4,5,6\}}\frac{c_d}{8(n-1)+d},\quad
(c_1,c_4,c_5,c_6)=(4,-2,-1,-1),\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

For an integer n>=3 define two **disjoint** finite prime sets

\[
\mathcal P_n^+=\{p>5:p\text{ prime},\ p\equiv1\pmod4,
                 \ 2n+2<p\le8n-7\},
\]
\[
\mathcal P_n^-=\{p>5:p\text{ prime},\ p\equiv3\pmod4,
                 \ 8n+8<3p,\ p\le4n-1\},\qquad
G_n=\prod_{p\in\mathcal P_n^+\cup\mathcal P_n^-}p.
\]

**TR-01, exact theorem.** Every prime in those sets satisfies

\[
v_p(U_n)=v_p(U_{n+1}-U_n)=-1.
\tag{1}
\]

Consequently `G_n` divides both reduced denominators. This is a statement at
**every** n>=3, with a product allowed to be empty; it does not assert an effective
small-n exponential constant.

**Proof for the plus set.** If p is 1 mod8, the first p-divisible denominator is p
at offset 1 and index b=(p+7)/8, coefficient 4. If p is 5 mod8, it is p at offset
5 and b=(p+3)/8, coefficient -1. In either class the next multiple with an allowed
offset is 4p, at index (p+1)/2. Our upper bound ensures b<=n, while p>2n+2 puts
that second event strictly after n+1. Also p^2>8(n+1)-2, so there is no squared
pole. Unrolling the recurrence therefore gives

\[
pU_n\equiv c\,16^{n-b}\ne0\pmod p,\qquad c=4\text{ or }-1.
\]

All terms except this one have p-integral denominators. No p-pole is present in
r(n+1), and `U_(n+1)-U_n=15U_n+r(n+1)`. Since p>5, multiplying by 15 cannot
cancel the unique p-primary component. This proves (1).

**Proof for the minus set.** For p=3 or7 mod8 the first allowed multiple is 2p,
always at offset 6, coefficient -1, and index b=(p+1)/4. The next is 3p at
offset 1 (class3), index (3p+7)/8, or offset 5 (class7), index (3p+3)/8.
The upper bound puts b<=n; `3p>8n+8` puts either second event after n+1.
Again p^2>8(n+1)-2. Thus

\[
pU_n\equiv-\tfrac12 16^{n-b}\ne0\pmod p,
\qquad p(U_{n+1}-U_n)\equiv-\tfrac{15}{2}16^{n-b}\ne0\pmod p.
\]

This completes the proof. The code independently scans the actual four
denominator channels to check that exactly one p-pole occurs through n+1, and
compares direct rational differences with these modular residues.

**TR-02, translated-grid theorem.** For any real t and positive integer q, if
both `{U_n}` and `{U_(n+1)}` belong to `t+(1/q)Z/Z`, then

\[
\operatorname{den}(U_{n+1}-U_n)\mid q,\qquad q\ge G_n.
\tag{2}
\]

Indeed subtracting the two grid coordinates implies `q(U_(n+1)-U_n)` is an
integer; reduction of that rational proves the divisibility. Conversely, taking
`t={U_n}` and q equal to the reduced denominator attains a two-point grid. Thus
the denominator is the **exact smallest** grid size, not merely a loose bound.

The classical fixed-modulus prime number theorem in arithmetic progressions
gives `theta(x;4,a)=x/2+o(x)`, a=1,3. Applying it to the explicitly displayed
intervals yields

\[
\log G_n=3n+\tfrac23n+o(n)=\tfrac{11}{3}n+o(n),
\quad \liminf_{n\to\infty}\frac{\log q_{\min}(n)}n\ge\frac{11}{3}.
\tag{3}
\]

This invokes a published theorem, not RH or a distribution conjecture. A primary
modern reference proving more than the asymptotic needed here is Bennett,
Martin, O'Bryant and Rechnitzer, *Explicit bounds for primes in arithmetic
progressions*, Illinois J. Math. 62 (2018),
[arXiv:1802.00085](https://arxiv.org/abs/1802.00085). No effective threshold from
that paper is implemented in this finite probe.

**Controls and scope.** The wrong-ratio vector `(5,-2,-1,-1)` also has these
nonzero first poles and passes (1); this is not a uniqueness certificate for pi.
The fixed-ratio mutant `(4,0,-1,0)` retains the plus family but deletes the
minus-family pole entirely and fails that part. Rational p-integral seed changes
add `15*16^n*s` to the difference and preserve (1). This is correct: rational
translations preserve integer-base normality. The known `p=73,k=4,N=274`
stroboscopic disappearance is retained; 73 is outside the prime intervals of
(1) at n=274. The coherent irrational seed `s=-pi/16` leaves the rational domain;
it cannot be reduced modulo p by the rational projection used here.

## 2. A complete exclusion of the natural exact-grid certificate (TR-03)

The inherited PR #395 certificate partitions all sufficiently late times into
finite consecutive blocks B_j, puts a surrogate z_n on a translated grid of
q_j sites within block j, and bounds its per-site multiplicity by M_j>=1.
It asks, for every cutoff N, that the budgets over **all blocks touched before N**
satisfy

\[
\sum_{j:B_j\cap[0,N)\ne\varnothing}M_jq_j=O(N),\qquad
\sum_{j:B_j\cap[0,N)\ne\varnothing}M_j(1+q_j\epsilon_j)=o(N).
\tag{4}
\]

**TR-03, stronger finite-horizon form.** Let C be any fixed finite positive
constant. At each N, permit a separately chosen partition of the first N source
times into consecutive blocks and arbitrary translated grids containing the
natural exact states `z_n={U_n}`. If `sum_j M_j q_j<=CN`, then necessarily

\[
\sum_j M_j(1+q_j\epsilon_j)\ge N-O_C(\log N),\qquad \epsilon_j\ge0.
\tag{7}
\]

Thus no certificate satisfying (4) exists, even with N-dependent partitions.

**Proof.** By (3), choose n_0 such that `G_n>=exp(3n)` for n>=n_0; this is an
existence assertion with no explicit numerical n_0 claimed. Put
`L=max(n_0,ceil(log(CN)/3)+1)`. If a block contains consecutive times n,n+1
with n>=L, then its grid costs `M_j q_j>=G_n>=exp(3n)>CN`, contradicting the
assumed total budget. Hence every edge between times L and N is a block cut.
There are at least `N-L` distinct blocks meeting this tail, and each contributes
at least1 to the left side of (7). Since L=O_C(log N), (7) follows. For a single
fixed all-horizon partition this also shows that only finitely many blocks can
have length greater than1. QED.

This is a proved obstruction to a precise **certificate architecture**, not a
proof that BBP is nonnormal, or that moving/multiple conductors cannot help.
Rounding to approximate grids, allowing different surrogates, using signed
weights, or proving direct cofiber correlations remain possible. Their visits
and errors must be bounded independently; no such estimate is assumed here.
The exponential grid size alone says nothing about actual interval occupancy.

**A finite approximate-grid attack, not an asymptotic theorem.** For four
consecutive exact states starting at n=97,127,211,257,383, the probe searches all
q in1..n and **every real translation**. For fixed q, the minimum radius is
`(1-max cyclic gap of {qU_m})/(2q)`; this follows by choosing the shortest arc
containing all scaled phases. A separate integer-LCM oracle reconstructs each
state and computes the same arc by rotating each of its four endpoints tozero.
With epsilon=(8n+1)^(-2), the floor of the exact minimum/epsilon is respectively
1110,932,1671,1110,1008. Thus each minimum exceeds2epsilon. Since each actual
pi phase is within epsilon of the rational state, **none of these five actual
four-state pi windows** can lie within epsilon of a translated q-grid with
q<=n. The exact radii are in `approximate_grid_receipt.json`; no floating
minimization is used. This is finite calibration only: larger q, larger errors,
other windows, and asymptotic approximate-grid certificates remain open.

## 3. Stoneham normal controls reproduced (TR-04, classical recovery)

For c=3 or5 use `alpha_(16,c)=sum_(j>=1)1/(c^j*16^(c^j))`, and the rational
pulse orbit `z_n={16 z_(n-1)+1_(n=c^j)/c^j}`, z_0=0. On the stage
`c^j<=n<c^(j+1)`, put q=c^j. The birth numerator is 1 modc. LTE gives
`v_c(16^m-1)=1+v_c(m)`, so `ord_(c^j)(16)=c^(j-1)`. The residue group
`1 modc` has exactly that size; each residue therefore appears precisely
`M=c(c-1)` times in the complete stage.

The true circle orbit differs by a positive tail bounded by
`epsilon=1/[16(c-1)c^j]`. An arc of length ell, enlarged by that tail, meets at
most `c^(j-1)*ell+3` grid sites. Sum complete and partial stages and include the
first c times to recover for every N>c

\[
A_N(I)\le cN|I|+3c(c-1)\lfloor\log_c(N-1)\rfloor+c.
\tag{5}
\]

Every empirical weak limit is times-16 invariant and has density bounded by c
against Haar. Its Fourier coefficients satisfy `nu_hat(h)=nu_hat(16^kh)`;
Riemann--Lebesgue forces all nonzero coefficients to vanish. Hence the orbit
is normal. This is a rederivation of an established result, not a new pi theorem.
The published class normality is Bailey--Crandall,
[*Random Generators and Normal Numbers*](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf),
Experimental Mathematics 11 (2002), 527--546. The occupancy-to-normality mechanism
is also the classical weak hot-spot criterion, recalled as Theorem 1.1 in
Bailey--Misiurewicz,
[*A Strong Hot Spot Theorem*](https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf).

The exact full-stage character sum is

\[
\sum_{n=c^j}^{c^{j+1}-1}e(hz_n)
 =(c-1)c^j e(h/c^j)\,\mathbf1_{c^{j-1}\mid h}.
\]

The probe verifies zero sums by polynomial reduction modulo the prime-power
cyclotomic polynomial, without complex floating arithmetic. Independent pulse
recurrence and modular finite sums agree. The full-stage true sum for frequencies
outside the divisibility exception has magnitude at most `pi*|h|/8`, by paying
the positive tail. Partial stages need (5); complete-stage cancellation alone
does not prove all-horizon normality.

For c=2 every pulse is exactly one nonzero hex digit:
`1/(2^j*16^(2^j))=A_j/16^(J_j)`, where
`J_j=2^j+ceil(j/4)` and `A_j=2^(4ceil(j/4)-j)` lies in {1,2,4,8}.
The positions strictly increase, no carries overlap, and only O(log N) digits
among the first N are nonzero. This control is nonnormal, by proof.

The BBP Green-tail precision leg survives, `0<T_n<(8n+1)^(-2)`, but the exact
grid leg cannot survive in the natural surrogate architecture by TR-03. Even
before that asymptotic obstruction, the copied c=3 stage-2 bin law fails:
BBP n=9..26 counts are exactly `(9,7,2)`, while Stoneham residues have `(6,6,6)`.
The exceptional BBP primes 2,3,5 do not supply Stoneham's pulse recurrence/LTE law.

## 4. Exact arithmetic gluing and its lost observations (TR-05)

For `x=A/(p^a D)` in lowest terms, `(p,D)=1`, define the canonical rational
p-primary projection

\[
P_p(x)=\frac{A D^{-1}\bmod p^a}{p^a}\pmod1.
\]

It is the primary direct-sum projection of Q/Z and hence an additive map,
commuting with multiplication by16. It supplies a valid edge of the full
rational-source update triangle:

\[
P_p(x_n)=16P_p(x_{n-1})+P_p(r(n))\pmod1,
\quad x_n=16x_{n-1}+r(n)-\kappa_n,
\]

where x_n={U_n} and the **literal integer** carry kappa_n is retained in the
upstairs state. Carries need not always be in 0..15; the four-bit Walsh label is
kappa_n mod16, together with its separately retained integer quotient. The
prime-stroboscopic map is an additional exact endpoint congruence on this edge.

This projection loses all 16 possible next radix digits even on the finite set
`x=d/16`, d=0..15: for odd p each P_p(x)=0, while floor(16x)=d. Every nontrivial
four-bit Walsh mask takes both signs on that same fiber. Carry residues mod3 or6
cannot recover the full Walsh mark either: d=0 and d=6 have equal mod3/mod6
labels but opposite mask-2 values. The q=3 orientation, q=6 primitive/cototient
grades, and full 16-state characters remain distinct coordinates; no quotient
is silently declared sufficient.

**No continuous real-circle extension.** Let `q_j=1+jp`,
`x_j=1/(p q_j)`. Then x_j tends to zero in the real circle, but
`P_p(x_j)=1/p` for every j. Thus P_p is discontinuous at zero in the inherited
circle topology, and no continuous map on the real circle can agree with it on
all rationals. This is not a claim about every possible discontinuous algebraic
extension or every selected source; it forbids a continuity-based transport of
the small Green error through this projection. Full CRT reconstruction with its
complement remains exact; a p-only lift to the actual irrational pi phase is
not supplied.

## 5. Retained-posterior obstruction to a literal frame reset (TR-06)

The authentic auxiliary positive source is
`mu_a(dx)=exp(-a x)Q(x)dx/R(a)`,
`Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x)>0`, `a_n=8n-7`.
Retaining the same latent X, forward native time k to N>k is exactly the bounded
failure likelihood `exp(-8(N-k)X)`, normalized by `r(N)/r(k)`.
The reverse density is

\[
\frac{d\mu_{a_k}}{d\mu_{a_N}}(x)
 =\frac{R(a_N)}{R(a_k)}e^{8(N-k)x}.
\tag{6}
\]

It is unbounded on x>0, a set having positive mu_(a_N) density everywhere.
Any nonzero bounded likelihood L produces a normalized posterior with bounded
density `L/E[L]`. Hence **no bounded likelihood on the same retained latent X**
turns mu_(a_N) into mu_(a_k). In particular the arithmetic N_p(k) to k strobe
does not itself furnish a probabilistic backward frame reset of this posterior.
Unbounded weighting or a different latent-variable transformation is a different
declared instrument and is not excluded. Finite rational checks evaluate (6) at
`x=j log2/8`, where its value is an exact rational times `2^(j(N-k))`.

This is compatible with the exact Pascal word-mass diamond and its continuous
Beta extension in the sibling Lorentz--Gamma work. Those identities concern
source posteriors. Appending deterministic marks `(U_n,P_p(U_n),cofiber,kappa_n)`
to every history makes a lossless marked representation, but a source-only
expectation of the common mark is simply that mark times the positive mass.
It supplies no bound on signed time correlations. The coherent same-forcing
seed `s=-pi/16` has exactly the same positive posterior and `U_n(s)=-T_n`, so its
phases tend to1. Any source-only posterior proof of cancellation fails this
explicit changed-seed control; it is not a counterexample to the zero seed.

The author's **Harmonic Numbers / Golden Ratio / Euler--Mascheroni triangle**,
and **Oily--Macaroni** `phi^(-1)-gamma`, retain Leah/femboy2112's naming and
motivation in `research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md`.
The native Gamma(2) boundary, fixed-golden readout `psi(r)-lambda^r`, and corrected
golden locus `theta=lambda/(1-lambda^r)` remain valid declared-observer results.
No harmonic, Euler, golden, Fibonacci, Beta, or Lorentz constant has been
inserted into (1)--(5) without an arithmetic role.

## 6. Spectral and dynamical routes audited

The original Bailey--Crandall
[*Hypothesis A*](https://www.davidhbailey.com/dhbpapers/baicran.pdf) assumes the
zero-initialized rational-polynomial forced orbit has either a finite attractor
or equidistribution. Applying the pi instance as a premise would assume the
missing distribution result. Here the exact congruences and conductor obstruction
do not establish that dichotomy. No proof from the hypothesis is relabeled
unconditional.

Expanding-map invariance is automatic for empirical weak limits. It does not
imply that the selected limit has an L1 density: the coherent zero phase and
periodic de Bruijn paths are elementary countermodels. The Gamma/Pascal
multiplier in PR #391 has operator norm1 despite pointwise damping; the source
clock Fourier and Lorentz transforms of #390--394 are different observables
from selected real-phase sums. The human T-action of #396 retains a digit and
residual and is bijective as an augmented state, but bijectivity supplies no
occupancy bound. #397's normal-stream conclusions assume normality and cannot
be read backwards as a source proof.

The corrected `research/2026-10-27-furstenberg-kempner/` firewall is retained:
the Kempner number `sum 2^(-2^j)` has empirical base16 orbit limit delta0.
For each fixed leading binary window length L, only O(L log N) of N shifts
by 4n meet a nonzero bit; all other phases lie within 2^(-L) of0. Consequently
times2/times3 invariance of the limiting measure does not force Haar. Even its
published transcendence and irrationality exponent2 cannot repair that inference.
Positive entropy of every relevant invariant component, or a new selected
anti-concentration theorem, remains absent. Finite sparse-window checks here
certify only their explicitly tested counts.

Control closure: Q has exact derivative vector `(0,15,-59,243)` through order3.
The Gamma fake15x matches orders0,1; adding `(1-exp(-x))^3` changes that vector
by `(0,0,0,6)`, so the positive cubic mutant matches through order2. The biased
independent digit law with mass1/2 at0 and1/30 at each other symbol has every
nontrivial Walsh expectation exactly7/15, yet every finite-word reset preserves
its law. Uniform digit expectations are0. The probe also reconstructs a finite
hexadecimal Champernowne prefix by two encodings. Its classical normality is a
published construction theorem, not a conclusion from this finite prefix;
the biased product law is a probability ensemble, not the selected BBP path.

**Next concrete obligation.** On first-pole windows where
`P_p(U_(b_p+j))=c_p16^j/p`, prove a nontrivial bound for the *actual product*
`sum_j e_p(hc_p16^j) e(h[U_(b_p+j)-P_p(U_(b_p+j))])`, with original source
and zero seed. Grid denominators and positive posterior maps cannot replace
the second factor. This directory attacks the exact-grid and bounded-likelihood
alternatives and proves their specific obstructions; the campaign's signed-CRT
directory attacks that remaining product directly.
