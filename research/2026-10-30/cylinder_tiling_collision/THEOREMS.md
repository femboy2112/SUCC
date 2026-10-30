# SUCC Arithmetic Cylinder Tiling — proofs, tests, and exact obstruction

**Research status:** classical symbolic-dynamical, entropy and Fourier facts specialized to the authentic BBP selected recurrence, plus a source-faithful Green-tail transfer for *two-time collision kernels*. The finite arithmetic observations are exact and bounded. No theorem below proves π normality, SC-06, or RH. **No novelty claim for the classical cylinder/entropy theory.**

Parent research: PR #405 head `6cf5050ff2cfd92e7a0c8876da5233be6ff117f5` rooted in the preserved four-pole Main XVI. Related: PR #392's shared-latent two-triangle *positive* law is mathematically distinct from the *actual selected two-time* collision statistic here. PR #405's bounded-slip cylinders are source-determined **lag-coordinate** inverse images; the present cylinders are **base-16 digit-word** inverse images. They share an expanding-map grammar but must not be identified.

## CTC-01 — authentic source-conjugate cylinder tiling (EXACT)

Let `e(t)=exp(2*pi*i*t)`, and keep the unmodified authentic recurrence

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2),
U_0=0,    U_(n+1)=16 U_n + r(n+1),
T_n=sum_(j>=1) 16^(-j) r(n+j),
U_n + T_n = 16^(n-1)*pi (n>=1).
```

Positive source regrouping gives `r(n)>0`, strictly decreasing, and
`0<T_n<(8n+1)^(-2)`. The exact tail recurrence is `T_(n+1)=16 T_n-r(n+1)`.

Define time-dependent circle maps

```
F_(n+1)(x)={16x+r(n+1)},    C_n(x)={x+T_n},    D(x)={16x}.
```

Then **the exact commuting square** holds:

```
C_(n+1) o F_(n+1) = D o C_n.
```

At refinement depth m, define the standard half-open base16 cylinder
`I_w=[k/16^m,(k+1)/16^m)` for digit word `w` with integer value k, and the transported source-relative cylinder `C_(n,w)=C_n^(-1)(I_w)`.

The actual selected state `x_n={U_n}` belongs to exactly one such cylinder at every n,m. Its word labels are exactly the m hexadecimal digits beginning at the n-th fractional digit of π. Admissible transitions shift the word left and append one digit. Consequently the time/cylinder incidence space is the ordinary full 16-ary symbolic shift, expressed in source-relative coordinates. **Geometry alone does not exclude any digit history**, since the same recurrence with real seed s completes to `{16^(n-1)(pi+16s)}`. The zero seed selects a particular path; another arithmetic theorem is necessary to prove its genericity.

All words at a fixed finite time can be certified with rational arithmetic only. Set `T_n^[R]=sum_(j=1)^R 16^(-j)r(n+j)`. Monotonicity gives

```
T_n^[R] < T_n < T_n^[R] + 16^(-R) r(n+R+1)/15.
```

If the two endpoints `16^m(U_n+T_n^[R])` and `16^m(U_n+T_n^[R]+remainder_bound)` have the same integer floor, their common residue mod 16^m certifies the word exactly. If not, increase R and preserve ambiguity. No decimal approximation of π is required.

## CTC-02 — exact double-path collision energy and its refinement law

Let `d` be the *single deterministic* hexadecimal digit stream selected by s=0. Write `sigma` for the one-sided left shift. For m>=0 and word `w` of length m,

```
c_(m,N)(w) = #{0<=n<N: the m-prefix of sigma^n d equals w},
p_(m,N)(w) = c_(m,N)(w)/N,
Q_(m,N)=16^m sum_(|w|=m) p_(m,N)(w)^2.
```

Thus `Q_(m,N)=16^m/N^2` times the number of ordered pairs `(i,j)` of time positions whose length-m digit blocks agree; `Q_(0,N)=1` and Cauchy gives `Q_(m,N)>=1`.

For every m,N **exactly**,

```
Q_(m+1,N)-Q_(m,N)
 = 16^(m+1) sum_(|v|=m)sum_(a=0)^15
          (p_(m+1,N)(va) - p_(m,N)(v)/16)^2 >= 0.       (CTC-2)
```

Proof: `p(v)=sum_a p(va)` and complete the square for each parent v. This is a nonnegative, context-resolved defect of equal-child balancing. It uses visits of ONE selected trajectory; the pair count does not assert independence of its two times.

**Sixteen Walsh components.** Let `chi_b(a)=(-1)^popcount(a & b)` for masks b=0,...,15, and set

```
J_(v,b,N) = sum_(a=0)^15 chi_b(a) p_(m+1,N)(va).
```

Finite Walsh orthogonality and Parseval give the exactly equivalent signed-channel identity

```
Q_(m+1,N)-Q_(m,N)
 = 16^m sum_(|v|=m)sum_(b=1)^15 |J_(v,b,N)|^2.       (CTC-3)
```

All 15 nontrivial four-bit characters are retained, with the exact context v. These are actual digit currents, **not** the q=6 primitive weights nor the auxiliary Gamma/Pascal sensor's endpoint probabilities. The selected source/carry/prime data may decorate each current, but no source-derived bound has been established.

## CTC-03 — collision-entropy normality criterion (CLASSICAL principle, locally proved)

For every infinite hexadecimal digit stream d, define `Q_(m,N)` above. Then

```
d is base-16 normal
  iff limsup_(m->infty) (1/m) limsup_(N->infty) log Q_(m,N) = 0.    (CTC-4)
```

Both `limsup` orders are essential. No uniformity in a moving m(N) is assumed.

Proof. If d is normal, each fixed-length word has frequency 16^-m, hence `lim_N Q_(m,N)=1` for fixed m.

Conversely, let `nu_N=(1/N)sum_(n=0)^(N-1)delta_(sigma^n d)` on the compact one-sided symbolic space. Along any subsequence take a weak limit nu. Every cylinder is clopen, so its masses and Q_m converge along this subsequence. The finite-boundary identity `sigma_*nu_N-nu_N=(delta_(sigma^N d)-delta_d)/N` shows nu is shift-invariant.

Let `H_m(nu)` be the Shannon entropy of the m-cylinder distribution, and `H2_m=-log sum_(|w|=m) nu([w])^2` its order-two Renyi block entropy. Classical Jensen gives `H_m>=H2_m=m log16-log Q_m(nu)`. By the assumed uniform limsup bound, `liminf_(m->infty)H_m/m>=log16`. Stationarity yields subadditivity of H_m, so `h(nu)=lim H_m/m=inf H_m/m`, and necessarily h=log16. For every fixed k, `H_k/k>=h=log16`, while `H_k<=k log16`; hence equality. The unique maximal k-word entropy distribution is uniform, so `nu([w])=16^-k` for every k,w. Every subsequential limit is the uniform Bernoulli measure, hence the full digit stream is normal. QED.

**Quantitative finite-block corollary.** If the RHS of (CTC-4) is at most epsilon≥0 (not necessarily zero), every subsequential invariant limit nu satisfies `H_k(nu)>=k(log16-epsilon)` for every fixed k. Its k-block KL divergence to uniform is at most `k epsilon`; Pinsker then gives total variation at most `sqrt(k epsilon/2)` (natural logarithms). The theorem provides a **conditional certificate**, NOT a source proof of its premise.

**Source-directed research target:** derive from the exact four-pole zero-seeded arithmetic a bound `limsup_N Q_(m+1,N)-Q_(m,N) <= poly(m)` for every m, or any other **subexponential** bound on Q_m. Since Q_m is a sum of nonnegative squared full-Walsh, history-conditioned currents, this would prove π normality by CTC-4. Stating that bound without proving it is only a reformulation of the open problem.

## CTC-04 — normality calibration and hostile controls

For a base-16 *Haar-distributed starting real number* beta, the digits are i.i.d. uniform. For each distinct pair of starting indices i!=j, even with overlap, the probability their m-blocks match is exactly 16^-m. For overlap lag l<m, equality enforces period l on a string of length m+l; it has l free digits, among 16^(m+l) equiprobable strings, hence probability 16^-m. Nonoverlap is ordinary independence. Therefore

```
E_Haar Q_(m,N) = 1+(16^m-1)/N.                        (CTC-5)
```

This is an **ensemble** benchmark, not a theorem about the authentic one-point zero seed. It exposes the unavoidable diagonal collision floor `Q_(m,N)>=16^m/N`.

A cyclic de Bruijn hexadecimal word of order two has 256 distinct length-two words, hence its periodic infinite continuation satisfies exactly:

```
Q_m = 1 (m=1,2);    Q_m=16^(m-2) (m>=2).
```

It passes the first two scales perfectly while being periodic and nonnormal. All-zero digits give Q_m=16^m. The biased iid model with `Pr(0)=1/2, Pr(a)=1/30` for a!=0 has `Q_m=(64/15)^m`, and is nonnormal. The coherent same-forcing seed `s*=-pi/16` has completed beta=0, so Q_m=16^m for every m. The auxiliary positive SUCC source geometry is unchanged under that seed change. These controls refute a source-only positive-triangle implication to the desired collision bound.

## CTC-05 — a genuine four-pole source-to-two-time *smoothed* transport bound

Let `q=16^m`, `ell=1/q`, `||t||=distance(t,Z)`, and define the periodic nonnegative tent kernel

```
K_ell(t)=ell^(-1) (1-||t||/ell)_+.
```

Its integral on the circle is 1, its Lipschitz constant is `ell^-2=q^2`, and its Fourier coefficient at integer h is `sinc(pi h ell)^2`, interpreted as 1 at h=0. The last fact is the Fourier transform of a triangle, or the square of the transform of a uniform box. This is a *literal* triangle-on-triangle construction: superposing two interval cells then averaging the translation of their lattice gives K_ell.

For an orbit `a_1,...,a_N` define the double-time collision energy

```
Kcal_(ell,N)(a) = (1/N^2)sum_(i,j<=N) K_ell(a_i-a_j)
                 = sum_(h in Z)|mu_hat_N(h)|^2 sinc(pi h ell)^2.
```

It is also `q` times the translation-average of the squared m-cylinder masses. In particular it is >=1, and `Kcal>=q/N` by the diagonal.

Use **authentic** selected rational states `x_n={U_n(0)}` and completed pure-radix states `y_n={U_n(0)+T_n}`. The source tail is positive and summable. Write `B=sum_n T_n=(sum_n r(n)-pi)/15 <1/32` (the exact Gamma/digamma B has already been derived and credited in prior SUCC research). Since K is q²-Lipschitz,

```
|Kcal_(ell,N)(y)-Kcal_(ell,N)(x)|
 <= (q^2/N^2)sum_(i,j) |T_i-T_j|
 <= (2q^2/N)sum_(i<=N)T_i
 <= 2B q^2/N < q^2/(16N).                            (CTC-6)
```

This is a source-authenticated ALL-N bound on an actual *two-time* quantity, valid without assumptions on digit distribution. At each fixed m the error tends to 0. It also vanishes for moving levels m(N) satisfying `16^(2m(N))/N->0`. The stronger Kepler III moving resolution `16^m ~ n²` is far outside this source-transfer regime.

**Firewalls:** (i) CTC-6 compares two exact representations of the *same* selected orbit and does not upper-bound Kcal for either. (ii) The hard cylinder indicators have discontinuous boundaries; transferring them requires a source-derived boundary-visitation bound. Their smoothed overlap has a clean Lipschitz budget but still lacks a bounded collision estimate. (iii) Averaging the cylinder lattice's *origin* over its translations is an analysis instrument, not randomizing π's initial boundary.

## CTC-06 — exact source certificate, finite calibration only

The standalone Fraction probe certifies the first eight hexadecimal digits of π as `243F6A88`, using original four-pole U_n plus a bounded rational positive future tail (no π decimal digits). For the first N=256 digit-start positions, exact cylinder visits give:

| m | q=16^m | selected Q_(m,256) | distinct visited words | Haar expected Q_(m,256) | de Bruijn order-two Q_m |
|---:|---:|---:|---:|---:|---:|
| 1 | 16 | 2117/2048 | 16 | 1+15/256 | 1 |
| 2 | 256 | 31/16 | 164 | 1+255/256 | 1 |
| 3 | 4096 | 17 | 248 | 1+4095/256 | 16 |

These are **finite exact** original-source certificates, not evidence establishing asymptotic normality. At m=3 the diagonal floor is 16, so Q=17 is not itself remarkable. The exact Walsh defect identity was independently tested on both the de Bruijn and source-selected finite streams. No unbounded arithmetic estimate has been run or claimed.

## CTC-07 — graph-current conservation, not the missing mixing law

At depth m, construct the directed de Bruijn graph whose vertices are length-(m-1) words and whose edges are length-m words. The realized digit stream defines an edge path. At any vertex v,

```
out_N(v)-in_N(v) = 1_(initial prefix=v)-1_(prefix at time N=v).
```

This is exact conservation with a boundary defect of at most 1 and follows from counting successive starts. Balanced flows also occur on periodic directed cycles, so the identity is not a normality theorem.

The exact source update, prior/posterior triangle, prime-primary snapshot, literal carry, base16 digit and selected cylinder MUST remain different typed layers. The missing proof is a **source-selected, all-horizon upper bound on collision concentration or on the full conditional Walsh defect**, not another lossless bookkeeping square.

## Classification and next discrimination

- CTC-01/02/05/07: **PROVED LOCAL** elementary exact algebra/Fourier/finite combinatorics in stated domains.
- CTC-03: **CLASSICAL entropy/unique-maximal-measure principle**, self-contained proof above; a new SUCC arithmetic estimate has **NOT** been derived from it.
- CTC-04: **CLASSICAL** Haar/de Bruijn/product calibrations with exact finite controls.
- CTC-06: **OBSERVED FINITE exact rational source certificates**, 16 focused unit tests passed.
- Claim that these theorems establish π normality: **UNVERIFIED / OPEN**. No source-derived subexponential Q_m bound or selected fixed-frequency Weyl o(N) has been supplied.

**Next verdict-changing instrument:** prove a source-authenticated estimate on signed context-conditioned Walsh currents at every depth, strong enough to force `Q_m=e^{o(m)}` in empirical limits, and test on the coherent counterseed, source mutants, normal Stoneham c=3/5, nonnormal Stoneham c=2 and periodic de Bruijn. Consider cylinder boundaries and moving-depth sampling before claiming any quantitative transport. One can also attack a weighted lag/prime-CRT two-time kernel directly, but it must retain complementary real phase and zero seed.
