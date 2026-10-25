# Twisted observer agreement and the selected pi source

**Date:** 2026-10-24. **Base:** `main@e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Branch:** `research/pi-twisted-observer-agreement-2026-10-24`.
**Authority:** elementary paper proofs, exact finite arithmetic, and outward
phase intervals. No new Lean declarations; scholarly priority unverified.
**Pi normality remains OPEN. No independence theorem is established.**

## 1. Result of this round

The author's twisted-cable proposal survives as an exact observation mechanism:
recorded relative wire orientation recovers every signed temporal correlation,
even when the initial wire identity is unknown. This removes a representation
ambiguity. It does not supply the arithmetic estimate on those correlations.

The round also proves a positive repair to a genuine observation defect. On the
actual BBP source's odd-denominator carrier, a doubled differential is exactly
injective but not uniformly stable. Authentic source states at p=41 and p=73
show near agreement hiding an almost half-turn. Two coprime differential gains
repair that defect, with the sharp squared-norm constant 4/3 for gains 2 and 3.

An independent construction isolates the remaining mathematical information:
two invariant joint laws can have identical individual-observer histories and
identical differential histories, while the source sum is uniform in one and
constant in the other. Their disagreement lies exactly on the nonzero (h,h)
Fourier diagonal. This is the same diagonal sampled by the selected BBP source.

These are proved observation and obstruction results. No new all-prime saving
for the actual selected BBP sum or collision count has been proved. The new
signed temporal-energy instrument states that missing estimate without losing
the sign, the initial selector, the source carry, or the time endpoints.

A final source-specific local lemma gives an exact inverse-branch recursion
for collisions. A fixed branch-loss estimate on a positive proportion of
scales would yield a first polynomial saving; that estimate remains open.

## 2. Latest repository state and what its progress buys

The inspected live main is the PR #267 integration, rather than the older
Academic Main VIII head cited in historical dossiers. It incorporates #250
through #265, including the final #256 p-squared contribution. The two distinct
#260/#261 implementations and their MP claim identities are now preserved as
separate gauge/birth families. See the
[integration receipt](../../docs/COHERENT_MAIN_INTEGRATION_RECEIPT_2026-10-24.md).

The newer [PR #266](https://github.com/femboy2112/SUCC/pull/266), pinned at
`e821a90d615aa5f78a61ad08c9d7a44709ad6189`, remains a separately inspected donor.
Its [lag/carry dossier](https://github.com/femboy2112/SUCC/blob/e821a90d615aa5f78a61ad08c9d7a44709ad6189/research/2026-10-24/PI_LAG_CARRY_RIGIDITY.md)
is not silently merged here. A fresh exact Fraction computation in this round
reproduces its p=2081 pair count. The million-prime result is cited as that
branch's certified finite receipt, not claimed as a rerun in this round.

| Established component | Its actual leverage | Remaining limitation |
|---|---|---|
| Correct original four-pole source and positive Green tail (#252--254) | Authenticates which orbit is pi; controls approximation and carry transport | Positive memory and small forcing do not prove cancellation |
| Exact first-prime windows, later prime-power births, Witt carries (#256, #261) | Separates a local clock from the complete complementary source without deleting terms | Many arithmetic clocks do not become independent random inputs |
| Cyclotomic projections and periodic-twist estimates (#255, #258--259) | Proves cancellation against a specified class of low-complexity weights | The actual complementary source is not in that class by assumption |
| Full-source relative-Galois moments and collisions (#261, #265) | Includes the entire real complement; proves almost all conjugates are well behaved | The selected embedding is a=1, not a randomly chosen conjugate |
| Collision-to-entropy and dense-window-to-prefix bridge (#265) | A precise selected-source counting estimate would imply binary normality | That selected estimate is unproved |
| Carry-retaining lag dynamics and finite authentication no-go (#266) | Proves close-run restrictions and locates where initial/carry information is lost | A bound on lengths of close runs is not a bound on the total return count |

Two corrections matter. The four-pole-lane closure verdict was withdrawn by
#252 because it mistyped the forcing-index poles as orbit-state poles.
Positive Poisson regret is asymptotically equivalent to normality, as corrected
by #265; restating that condition is not a new proof step. Both corrections are
already reflected in current main and are preserved here.

### Exact unresolved contracts

Write e(x)=exp(2*pi*i*x). For every fixed nonzero integer h, the selected
Fourier route needs

$$
\frac1N\sum_{n<N} e(h16^n\pi)\longrightarrow0.
$$

The existing sufficient collision contract fixes c=2/5 in advance. For good
primes p=8m+1 with L=ord_p(16)>sqrt(p)/log(p), put N=3m and
M=16^floor((2/5)log_16(p)). It asks for

$$
\frac{M}{N^2}\#\{(s,t)<N:
\|y_{m+1+s}-y_{m+1+t}\|_{\mathbb T}\le1/M\}=p^{o(1)}.
$$

This means every positive epsilon eventually works on all good primes, or on
an independently proved sufficiently dense subfamily. A single favorable prime,
a fixed positive exponent, and a Galois average do not discharge it. This
prescribed-scale condition is stronger than rate-free normality in general;
its novelty tax is explicitly paid by the existing de Bruijn-repeat control.

The present round targets the observation-to-signed-correlation edge. The
positive results are unconditional elementary theorems about that edge. The
source-specific decay estimate remains a pathway gap, not a demonstrated
logical boundary or proof of unknowability.

## 3. Source and notation: state, observation and character

The source is exactly

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
y_0=0,\qquad y_n=\{16y_{n-1}+r(n)\}.
$$

On the first p-window,

$$
y_{m+1+t}=u_t+w_t\pmod1,\qquad
u_t=\frac{4\,16^t}{p}\pmod1,\qquad 0\le t<3m.
$$

Here u and w are additive circle states. To avoid the older ambiguity where
u sometimes meant its exponential, this report uses

$$
U_t=e(hu_t),\qquad V_t=e(hw_t),\qquad F_t=U_tV_t=e(hy_{m+1+t}).
$$

The p-primary projection rho_p on Q/Z satisfies

$$
\rho_p(y_{m+1+t})=\rho_p(u_t+w_t)=u_t,\qquad \rho_p(w_t)=0.
$$

Thus the user's equality is valid **as an equality of p-observations**. The
residual can be information absent from one observer rather than external noise
added to the physical source. The full circle character still depends on it.

### Target-character descent criterion

Let P:G->H be a group quotient and chi:G->unit circle a character. Then chi
can be recovered from P alone exactly when chi is trivial on ker(P).
Necessity follows by applying the factorization to a kernel element;
sufficiency follows because chi is constant on every quotient fiber.

For P=rho_p, every nonzero archimedean character e(hx) fails this test: choose
a prime q not dividing ph and use x=1/q in ker(rho_p). Then e(h/q) is not 1.
The statement is not that quotient agreement is false. It is that this specific
target observable does not descend through that quotient.

If w is literally zero in the full carrier, the source character equals the
prime-clock character, and a bound on the latter transfers. If instead w is
zero only after observation, the descent test is the missing requirement.
One may also choose a new coordinate u'=u+w and write w'=0, but then u' is
the complete source; the old estimate for u=4*16^t/p does not automatically
become an estimate for u'. Coherent coordinate changes preserve the target
when its observable is transported along with the state.

### A source restriction that must be retained

Regrouping, without omitting a term, gives

$$
r(n)=\frac4{8n-7}-\frac1{8n-3}
-\frac{3n-1}{(2n-1)(4n-1)}.
$$

All displayed denominators are odd. Therefore authentic y_n and every w_t
belong to the odd rational torsion group G_odd. A literal half-turn is outside
that source class. This matters in the next theorem.

## 4. What agreement forces about unshared correlations

Let Q be the real symmetric time-residue averaging projection used in PSC-03,
with normalized empirical mean E. For arbitrary complex arrays a,b,

$$
\mathbb E[ab]=\mathbb E[(Qa)(Qb)]
+\mathbb E[(a-Qa)(b-Qb)].
$$

The two mixed terms vanish because the residual has zero average in every
fiber. There is no conjugation in this formula: the source target is the
bilinear product U V. Its residual is the previously isolated signed J term.

Knowing the shared projections does not determine this residual's sign.
For a=(1,-1) and b=a,-a,ia, all shared averages are zero and both residual
energies equal one, while E[ab] is respectively 1,-1,i. All three arrays can
be read from one two-point carrier. Source consistency is compatible with
each signed answer. An independence or orthogonality premise would add real
information; it cannot be inferred from the common source alone.

There is also an exact orientation-independent difference formula. If each
Q-fiber has K points and there are d fibers, then

$$
J=\frac1{dK^2}\sum_r\sum_{i<j\text{ in fiber }r}
(a_i-a_j)(b_i-b_j).
$$

To prove it, expand the pair products in one fiber; the result is
K*sum(a_i b_i)-(sum a_i)(sum b_i). Swapping i and j changes both signs,
so the product is invariant. This is a precise realization of agreement living
in transported differences. It retains the missing signed quantity rather than
forcing it to vanish.

## 5. Unknown initial wire identity is removable

Model the recorded complex signal by d_t=s_t z_t with s_t in {+1,-1}.
The recorded local twist is a_t=s_(t+1)s_t. Its path transport is

$$
P_{s,t}=\prod_{j=s}^{t-1}a_j=s_ts_s.
$$

Direct multiplication gives

$$
P_{s,t}\,d_t\overline{d_s}=z_t\overline{z_s}.
$$

Taking q_0=1 and q_t=product_(j<t)a_j recovers q_t d_t=s_0 z_t. The
remaining global sign does not change a lag product or the squared magnitude
of the sum. Every signed real and imaginary lag correlation is recovered.

On a graph rather than a path, a coherent choice of wire labels exists exactly
when the product of edge twists around every cycle is +1. Necessity telescopes;
for sufficiency choose a root and integrate along paths. A negative cycle
product indicates inconsistent label transport, not arithmetic cancellation.

The negative control is essential. A constant z_t=1 with alternating labels
s_t=(-1)^t has raw mean zero on an even sample. Its transported correlations
are maximal and its actual mean is one. Randomizing labels without transporting
the observable can manufacture precisely the desired-looking answer.

There are two different sign actions here. Changing the sign of a measured
complex differential multiplies it by -1. Swapping two **additive circle**
states changes delta to -delta, so e(delta) becomes its complex conjugate,
not its negative. The two actions must not be substituted for each other.

## 6. Exact agreement can be unstable: a sharp repair

Consider balanced phase readouts

$$
A=e(u+w),\qquad B=e(u-w).
$$

Then AB=e(2u), A*conjugate(B)=e(2w), and

$$
A+B=2e(u)\cos(2\pi w),\qquad
A-B=2i e(u)\sin(2\pi w).
$$

These are paired readouts of a declared source split. They are not asserted
to be two BBP trajectories with the same forcing; reversing the complement
also reverses its forcing contribution.

### Exact identification versus uniform stability

On the full circle, A=B means w is 0 or 1/2. On G_odd, exact A=B forces w=0,
because odd torsion has no nonzero element killed by 2. This is a legitimate
source-specific strengthening of the observation inference.

For every w on the circle,

$$
\mathrm{dist}(w,\{0,1/2\})=\frac12\|2w\|_{\mathbb T}.
$$

For odd q and w in (1/q)Z/Z, the sharp one-branch bound is

$$
\|w\|_{\mathbb T}\le\frac{q-1}{2}\|2w\|_{\mathbb T}.
$$

Proof: write ||w||=k/q with 0<=k<q/2. The doubled distance is
min(2k,q-2k)/q. The ratio is either 1/2 or k/(q-2k), maximized at
k=(q-1)/2. Equality is attained there. Consequently w=(q-1)/(2q)
has doubled distance 1/q tending to zero and original distance tending to
1/2. Doubling on G_odd is an algebraic automorphism with discontinuous inverse
for the inherited circle topology.

### Authentic source witnesses

Independent original-four-pole and odd-form reconstructions agree exactly:

| p | t in prime window | source index n | certified residual distance | certified doubled distance |
|---:|---:|---:|---|---|
| 41 | 13 | 19 | ||w|| > 12/25 | ||2w|| < 1/40 |
| 73 | 15 | 25 | ||w|| > 12/25 | ||2w|| < 1/40 |

Using 4||x||<=|1-e(x)|<=(44/7)||x||, these imply

$$
|A-B|<11/70,\qquad |A-e(u)|>48/25.
$$

The readouts can nearly agree while their common output is almost opposite to
the local-clock output. These are finite authentic examples; no claim is made
about their density or asymptotic recurrence.

### Coprime gains: exact classification

For a finite integer gain family S with at least one nonzero gain, let
d=gcd{|k|:k in S}. The readout w -> (e(kw))_(k in S) is:

* injective on the full circle exactly when d=1;
* injective on G_odd exactly when d is a power of two, including 1;
* uniformly coercive in the circle metric, even restricted to G_odd, exactly
  when d=1.

The common kernel is d-torsion, proving the two injectivity claims. If d=1,
choose Bezout coefficients with sum a_k k=1. Telescoping unit phases and
Cauchy--Schwarz give

$$
|e(w)-1|^2\le\left(\sum_k a_k^2\right)
\sum_k|e(kw)-1|^2.
$$

If d>1, the nonzero point 1/d lies in the common kernel. Odd rational phases
approaching it disprove every uniform constant even when the point itself is
not in G_odd. This is a complete distinction between exact and stable access.

### Sharp gains 2 and 3

For every unit complex v,

$$
|v-1|^2\le\frac43\bigl(|v^2-1|^2+|v^3-1|^2\bigr).
$$

For v!=1, put c=Re(v). Dividing by |v-1|^2 gives

$$
2+2c+(1+2c)^2=4(c+3/4)^2+3/4\ge3/4.
$$

The inequality is trivial at v=1. Equality is attained by
v=(-3+i sqrt(7))/4, so 4/3 is optimal; density proves optimality on odd torsion
as well. A gain-3 discrepancy can compare e(u+2w) with e(u-w); both gains
remove the common u. Direct gain 1 would already solve identification, so the
two-gain construction is useful when that direct readout is unavailable.
No physical access to these probes is assumed.

For a source window, D_k^2=E|V_t^k-1|^2 yields the valid finite consequence

$$
|\mathbb E[U_tV_t]|
\le |\mathbb E[U_t]|+
\sqrt{\frac43(D_2^2+D_3^2)}.
$$

This is a sufficient error budget. D_2^2+D_3^2 tending to zero is **unproved**
for BBP and is stronger than the signed cancellation actually needed. It must
not become the next arbitrary assumption: a dispersed complementary signal
can cancel perfectly while these absolute mismatch energies stay large.

That limitation was tested on fresh source windows, specified after the
coercivity proof and before measuring them. The
[certified holdout](PI_TWISTED_COPRIME_GAIN_RECEIPT.json) gives at h=1:

| p | D2 squared + D3 squared, approximate | (4/3) times that sum, approximate |
|---:|---:|---:|
| 193 | 3.910981944 | 5.214642592 |
| 353 | 4.211093993 | 5.614791991 |
| 577 | 3.770479569 | 5.027306093 |

Each last-column **lower endpoint is above one**. The square-root error term
alone is therefore larger than the trivial bound on a unit-phase mean. This
specific absolute-smallness route is quantitatively vacuous on every fresh
finite window tested. The positive observation theorem remains valid. Its
useful role is to preserve the residual for a signed estimate, rather than
pretend that better measurement makes the residual small.

With gain 2 alone, let sigma_t be the sign of Re(V_t). Then
|V_t-sigma_t|^2<=|V_t-conjugate(V_t)|^2/2. Near agreement therefore reduces
the unresolved residual to a binary branch-sign process; it does not bound
that process's correlation with U. This is the exact information the first
differential can conceal.

## 7. The same source does not produce a persistent antiphase copy

For any two trajectories with identical forcing,

$$
x'_{t+1}-x_{t+1}=b(x'_t-x_t)\pmod1.
$$

Writing q_t=e(h(x'_t-x_t)) gives q_(t+1)=q_t^b. If b is even, q_t=-1
becomes q_(t+1)=+1. An initially opposite copy cannot remain opposite.

There is a sharp quantitative obstruction:

$$
\max\{\mathrm{dist}(h\delta_t,1/2),
\mathrm{dist}(h\delta_{t+1},1/2)\}
\ge\frac1{2(b+1)}.
$$

If the first distance is A, evenness gives dist(bh delta_t,0)<=bA, so the
second is at least 1/2-bA. Minimizing max(A,1/2-bA) proves the bound. At b=16
the exact two-cycle 9/17 <-> 8/17 attains 1/34. Odd bases preserve a half-turn,
providing a decisive parity control rather than a generic rejection of pairing.

If the forcings differ by eta, the bound becomes
(1/2-||h eta||)/(b+1). Exact persistent antiphase in an even base needs a
half-turn forcing difference at character frequency h at every step:
h eta = 1/2 mod 1. A change of coordinates may supply
such a formula, but transporting the observable preserves its original value.

Fixed translations commuting with the entire BBP source satisfy 15a=0;
there is no nontrivial involution in this 15-element rotation group. A fixed
reflection a-x would require 15a+2r(n)=0 modulo one for every n, impossible
because r(n) strictly decreases to zero. A covariant moving reflection has
a_(n+1)=16a_n+2r(n+1). If a_0=0 it has a_n=2y_n and fixes the selected
point, so it creates no distinct cancelling partner.

This excludes one precise mechanism: synchronous same-forcing antiphase
copies. It does not exclude time-index pairings, other source operators,
weighted cancellation, or a successful proof of normality.

## 8. A sharp joining obstruction: even random-looking differences can miss the sum

Let m be Haar probability on the circle. Compare

$$
\mu_{\rm ind}=m\times m,\qquad
\mu_{\rm anti}=\mathrm{Law}(X,-X),\quad X\sim m.
$$

Both are invariant under T_16 x T_16. Under both laws, u, w and u-w are
Haar distributed, and each separately observed full T_16 trajectory has the
same law. Nevertheless u+w is Haar for the first and exactly zero for the
second. Explicitly,

$$
\int e(au+bw)\,d\mu_{\rm anti}
=\begin{cases}1,&a=b,\\0,&a\ne b.\end{cases}
$$

The product law vanishes at every nonzero (a,b). Thus every off-diagonal
character agrees between the two models; their disagreement is exactly the
nonzero (h,h) diagonal used by e(h(u+w)). Even complete **separate** marginal
and differential trajectory laws do not determine that diagonal. Jointly
observing u and w would determine it, and is a stronger observation contract.

In fact this extends to **every** proposed sum law, not just these two examples.
Given any probability law nu for Y, take independent U uniform on the circle
and set W=Y-U. Then U, W and U-W=2U-Y are each uniform, while U+W=Y has the
arbitrary prescribed law nu. Its full character table is

$$
\widehat\nu(b):=\int e(by)\,d\nu(y),\qquad
\int e(aU+bW)\,d\mu_\nu
=\begin{cases}\widehat\nu(b),&a=b,\\0,&a\ne b.\end{cases}
$$

If nu is T_16-invariant, so is this joint law: apply T_16 to the independent
pair (U,Y) and then the same map (U,Y)->(U,Y-U). Thus even after source-limit
invariance is imposed, the separate observer data permit **every invariant
sum law**. This proves a complete nonidentification statement for that probe
family. It does not hold if one also observes the joint U/W or U/(U-W) law.
The finite odd-clock version is identical because multiplication by 2 is a
permutation; q=31 with sum law one-quarter mass at zero plus three-quarters
uniform on the five-point orbit of 1 is an additional exact control.

Every mu_nu is also invariant under swapping the two wires and under every
balanced redistribution (U,W)->(U+a,W-a). Conditional on Y, either operation
just replaces the uniform U by another uniform coordinate. Such balanced
redistributions are dynamically coherent when a_t=16^t a_0. Therefore even
stability under this entire coherently randomized observer family leaves the
sum law arbitrary. Stability of the declared gauge family and randomness of
the preserved carrier observable are different mathematical properties.

The exact q=31 rational-grid oracle, with q=17 holdout, realizes this separation
on finite odd carriers. It compares entire history distributions, not just
one-time histograms. These controls are unforced; they are not counterfeit
claims to the authentic BBP y0=0 contract.

### Why the source limit itself does not remove the obstruction

The actual joint empirical measure on a p-window is approximately invariant.
For a bounded Lipschitz F and T(u,w)=(16u,16w), telescoping the interior steps
gives

$$
\left|\int(F\circ T-F)\,d\mu_p\right|
\le\frac{2\|F\|_\infty}{N}
+\mathrm{Lip}(F)\max_{\rm interior}r(n+1).
$$

The final transition is charged as a boundary, avoiding the next p-birth.
The forcing is O(p^-2); every weak limit is T-invariant. Existing local-clock
cancellation gives a Haar first marginal along good primes. Even adding Haar
second and differential marginals would still permit mu_anti. Therefore
invariance and locally uniform clocks cannot themselves exclude the resonant
selected diagonal. The p-free denominator condition is not a closed
archimedean nonalignment condition: those rational phases are dense.

### Exact same-forcing differential no-go, with source scope preserved

For two copies x,z with the same forcing, d_n=z_n-x_n=16^n d_0. A common
homogeneous displacement 16^n c cancels from the complete differential record
and preserves the forcing. The independent rational control uses initial pairs
(0,1/15) and (1/7,1/7+1/15); their differential is exactly 1/15, while their
common signals differ nonconstantly by 16^n/7. All states have odd denominators.
It changes initial zero and makes no claim about asymptotic normality.

An infinite statistical control uses the actual Green tail T_n:
x_n={16^n X-T_n}, z_n={-16^n X-T_n}. Both obey the authentic forcing.
For Haar-almost every X, each wire and their difference are normal, while
x_n+z_n=-2T_n tends to zero. These generally irrational initial states do not
preserve the selected rational source. The example proves exactly why source
forcing alone is weaker than forcing plus authenticated initial state.

The [common-shift probe](../../scripts/twisted_observer_common_shift_probe.py)
also strengthens the finite two-wire control at p=2081: a common initial
perturbation preserves the infinite differential 1/15 and both early carry
prefixes, while changing all 780^2 window pairs into close pairs. Its dyadic
and odd-3-primary versions state separately which primary information changes.
This extends the inherited authentication no-go to the cable record; it is
not an actual-source counterexample or a new asymptotic result.

## 9. The useful differential compares different times of the actual source

The synchronized two-copy no-go does not apply to y_(t+d)-y_t. That lag sees
different forcing indices and obeys

$$
\delta_{t+1,d}=16\delta_{t,d}+r(t+d+1)-r(t+1)\pmod1.
$$

Its exponential is a temporal correlation of the actual source, with its
initial zero retained. In the true pi shadow it is the character at frequency
h(16^d-1), evaluated along the original orbit. Wire transport can recover this
quantity without knowing a global initial orientation.

For any unit complex array z_t, 0<=t<N, extend it by zero. For 1<=H<=N define

$$
E_{N,H}=\frac1{NH^2}\sum_{j=-H+1}^{N-1}
\left|\sum_{k=0}^{H-1}z_{j+k}\right|^2.
$$

Writing C_d=sum_(t<N-d) z_(t+d) conjugate(z_t), direct expansion gives

$$
E_{N,H}=\frac1H+
\frac2{NH^2}\sum_{d=1}^{H-1}(H-d)\Re C_d.
$$

Every sample appears in exactly H blocks. Cauchy--Schwarz on the N+H-1
block sums proves the finite signed van der Corput bound

$$
\left|\frac1N\sum_{t<N}z_t\right|^2
\le\frac{N+H-1}{N}E_{N,H}.
$$

This is classical correlation mathematics with all constants and boundaries
shown. The real signed terms must remain signed. Replacing them with absolute
values discards a possible cancellation mechanism; the alternating-signal
control makes the loss explicit.

### Source transport does not grow exponentially with lag

On the prime window, the inherited exact identity is
{16^(n-1)pi}={y_n+T_n}, with
0<T_n<B_n=1/((8n+1)(8n+2)). Hence each phase changes by at most
(44/7)|h| B_n. For a block of length at most H, its energy changes by at most
2H times the sum of its phase errors. Each sample appears in H blocks, yielding
the uniform all-H budget

$$
|E_{N,H}(\text{pi})-E_{N,H}(y)|
\le\frac{88|h|}{7N}\sum_{n=m+1}^{4m}B_n.
$$

This is O_h(p^-2), with no exponential lag factor. The independent Machin
shadow test verifies the finite instrument separately from the rational source.

### Exact criterion and its novelty boundary

Pi normality in base 16 is equivalent to requiring the following condition
for every fixed h!=0, on the good-prime family with the proved relative-scale
coverage:

$$
\lim_{H\to\infty}\limsup_{p\to\infty}E_{p,H}(h)=0.
$$

The inner limit fixes H. If pi is normal, each fixed nonzero lag character
h(16^d-1) cancels on these windows; the source budget gives E_(p,H)->1/H.
Conversely, the finite inequality makes the selected window means vanish,
and the inherited dense-window-to-prefix theorem gives normality.

This is an **equivalence**, not a new unconditional selected-source bound.
It is useful because the actual twisted temporal measurements can compute the
entire positive energy while preserving all signed information. A proof must
still show that these measured energies become small in the stated order.

## 10. Prespecified finite source measurements

The [preregistration](PI_TWISTED_OBSERVER_PREREGISTRATION.md) fixed every prime,
frequency and smoothing length before the measurements. Exact rational source
states and independent Machin/Taylor outward boxes produced the
[complete receipt](PI_TWISTED_SOURCE_ENERGY_RECEIPT.json). No supplied pi digits,
floating sign decisions, fitted exponent, or discarded unfavorable row enters.

For compactness the following entries display interval midpoints rounded to
nine decimals; exact outward intervals of width 10^-10 are in the receipt.

| p | h | N | squared source mean | E at H=2 | H=4 | H=8 | H=16 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 41 | 1 | 15 | 0.027717281 | 0.569333555 | 0.346619913 | 0.182963379 | outside domain |
| 41 | 3 | 15 | 0.067506179 | 0.406922972 | 0.188163863 | 0.095360473 | outside domain |
| 97 | 1 | 36 | 0.059775073 | 0.501781446 | 0.240114199 | 0.125970551 | 0.082490749 |
| 97 | 3 | 36 | 0.056065374 | 0.541574034 | 0.289604075 | 0.124485552 | 0.072429685 |
| 257 | 1 | 96 | 0.000762182 | 0.465521857 | 0.217368363 | 0.118379728 | 0.055967257 |
| 257 | 3 | 96 | 0.004317461 | 0.558006083 | 0.273281194 | 0.126327914 | 0.064369884 |
| 1009 | 1 | 378 | 0.002145141 | 0.492796722 | 0.245983268 | 0.116003794 | 0.065357139 |
| 1009 | 3 | 378 | 0.001799884 | 0.510853855 | 0.268459302 | 0.147233231 | 0.074065174 |

The independent-mean benchmark is 1/H; at H=16 that is 0.0625. The table is a
finite calibration near that scale, with visible variation. It proves no
uniform rate or limit. A constant source has the exact energy
1-(H^2-1)/(3NH), close to one, and the instrument rejects cancellation induced
only by alternating wire labels.

The independent p=2081 replay gives 76544 ordered close pairs and scaled
collision 5888/2925, exactly matching the pinned #266 result. Its 1048601
measurement, about 2.00073516 at M=256, remains a cited donor result. Neither
number can pay an all-good-prime estimate.

## 11. Research choices after the probes

| Candidate | Verdict | Reason |
|---|---|---|
| Average over unknown wire identity | Rejected as a cancellation mechanism | Coherent transport restores the original signal; additive swaps conjugate rather than negate its character |
| Small single-gain disagreement controls the source | Repaired as an observation theorem | Actual odd-source exact injectivity survives, uniform stability fails; coprime gains provide a sharp repair |
| Infer global randomness from local clocks and differential randomness | Refuted for the stated observation class | Product and anti-diagonal joinings agree on those observations but disagree on the target diagonal |
| Build a synchronous same-forcing antipodal copy | Refuted in even radix | Sharp 1/34 two-step obstruction for radix 16 |
| Bound actual cross-time signed energy or nonresonant collision visits | Principal surviving arithmetic front | Retains the source selector and target correlations; requires a new source-specific estimate |

The observation frame improves in a scoped sense: it recovers the older signed
quantities, distinguishes a genuine carrier defect from a label defect, exhibits
an authentic instability, and provides a stable coprime-probe repair. It does
not dominate the existing arithmetic estimates or prove the selected-source
bound. The first consequential arithmetic advance remains a nontrivial uniform
saving on authentic cross-clock correlations or nonresonant near-collision
visits, with y0=0 and later carries doing explicit work.

### 11.1 An exact inverse-branch step toward a first arithmetic saving

The following local lemma and conditional implication make the collision
direction more specific. They do not prove the new arithmetic premise.
They were developed after the prespecified measurements and checked against
the pinned donor's
[arithmetic track](https://github.com/femboy2112/SUCC/blob/e821a90d615aa5f78a61ad08c9d7a44709ad6189/research/2026-10-24/PI_LAG_ARITHMETIC_TRACK.md).

Let A=m+1, B=4m, N=3m, n=N-1, and use the overlapping windows
W={A,...,B-1} and W+={A+1,...,B}, each of length n. Let Q_W(tau) count
all ordered pairs in W whose source phases have circular distance at most
tau, including the diagonal. Define

$$
\epsilon_p=r(A+1)-r(B),\qquad
0<\epsilon_p<\frac{15}{(p+8)(p+9)}.
$$

The latter is an authentic source bound. Indeed

$$
r(k)=\int_0^1 t^{8k-8}(1-t)(4+4t+4t^2+2t^3+t^4)\,dt
<\frac{15}{(8k-7)(8k-6)}.
$$

The positive integral also makes r strictly decreasing. For each ordered
pair s,t in W, choose the centered difference delta_(s,t) in [-1/2,1/2).
The exact next difference satisfies

$$
\delta_{s+1,t+1}=16\delta_{s,t}+r(t+1)-r(s+1)-\kappa_{s,t},
\qquad \kappa_{s,t}\in\mathbb Z.
$$

For epsilon_p<tau<=1/4 define the zero inverse-branch count

$$
Z_W(\tau)=\#\{(s,t)\in W^2:
|\delta_{s,t}|\le1/32,\quad |\delta_{s+1,t+1}|\le\tau\}.
$$

Then, unconditionally on the authentic source,

$$
Q_W((\tau-\epsilon_p)/16)\le Z_W(\tau),\qquad
|Q_{W+}(\tau)-Q_W(\tau)|\le2n.
$$

The first inclusion follows from the forcing difference bound; its small
current distance is automatically inside 1/32. Within Z_W, the integer
kappa has absolute value at most 1/2+epsilon_p+tau<1, so it is zero.
This is the centered carry; the two literal source carries need not agree.
The endpoint estimate follows because the windows replace only one sample
(the sharper 2(n-1) also holds).

**Open intermediate premise.** Seek fixed 1/16<theta<1 and C>=0 such that,
for every sufficiently large good prime and all prescribed refinement scales,

$$
Z_W(\tau_j)\le\theta Q_{W+}(\tau_j)+Cn,
\qquad \tau_0=1/4,\quad \tau_{j+1}=(\tau_j-\epsilon_p)/16.
$$

This says the zero branch cannot repeatedly retain essentially all nearby
pairs. It does not demand equal occupancy of all sixteen inverse branches.
The linear allowance includes the diagonal. The actual initial state y0=0,
not only the forcing formula, is part of this unproved premise.

**Proved conditional consequence.** The two proved bounds give

$$
Q_W(\tau_{j+1})\le\theta Q_W(\tau_j)+(C+2\theta)n,
$$

and therefore

$$
Q_W(\tau_J)\le\theta^J n^2+
\frac{C+2\theta}{1-\theta}n.
$$

Here M=16^d is the largest power of 16 with M<=p^(2/5), and J=d-1 for
sufficiently large p. The exact terminal radius is

$$
\tau_J=\frac4M-\frac{\epsilon_p}{15}\left(1-\frac{16}{M}\right)
\ge\frac1M.
$$

The source bound on epsilon_p makes every used radius admissible. Restoring
the omitted last sample costs at most 2N-1 pairs. Since M is comparable to
p^(2/5), the full selected window would consequently satisfy

$$
Q(1/M)=O(N^2p^{-\eta}+N),\qquad
\eta=-\frac25\log_{16}\theta>0.
$$

This is a first positive exponent saving. For theta=1/2 it gives eta=1/10
and only K_p(1)=O(p^(3/10)), which does not meet the subpower target.
The conditional theorem also applies at theta=1/16, where it would give
K_p(1)=O(1) and reach the inherited sufficient normality contract. A fixed
theta<1/16 is impossible: the same consequence would give K_p(1)->0,
whereas partitioning into M cells gives Q(1/M)>=N^2/M and hence K_p(1)>=1.

There is a weaker first-step version. If the open inequality holds on at
least alpha*J of the prescribed scales, with fixed 0<alpha<=1, the others obey
Q_W(tau_(j+1))<=Q_W(tau_j)+2n without any extra premise. Multiplying the
stepwise factors gives

$$
Q_W(\tau_J)\le\theta^{\alpha J}n^2+(C+2)Jn.
$$

The resulting first saving has eta=-(2/5)*alpha*log_16(theta)>0 and additive
O(N log p). Thus a positive proportion of scales would already be useful.

**Why this is a limited target and where it can fail.** An invariant base-16
Cantor law with independent fair digits in {0,1} is nonnormal. For two
independent draws, their successor tails are independent of their leading
digits. Equal leading digits give current distance at most 1/240; unequal
digits give distance at least 7/120. Hence its population zero-branch law
is exactly Z(tau)=(1/2)Q_successor(tau), despite nonnormality. This is a
population analogue, not a certificate of the finite all-good-prime-window
hypothesis for a deterministic orbit. No implication from rate-free
normality to this quantitative premise is asserted.

The changed-initial-state tracking controls can instead put essentially
every pair in the zero branch at every such scale. They defeat any attempt
to derive the open premise from the forcing law and partial prime-clock
authentication alone. The selected zero and its later carry history must do
new arithmetic work. The [adaptive exact oracle](PI_TWISTED_BRANCH_RECURSION_RECEIPT.json)
checks the proved inclusion, carry gate and endpoint count on finite authentic
windows; it does not fit theta or test the asymptotic premise. Enlarging the
branch to 1/16 is a deliberately rejected carry mutation.

A source-derived time-index transport or bilinear incidence argument could
also address the actual (h,h) diagonal directly. Its rule must be specified
from source arithmetic before observing the desired Fourier signs. It must
reject the common-shift and anti-diagonal controls for a reason contained in
its hypotheses. The inverse-branch step above supplies one concrete local
place to try this, while preserving the unproved premise.

## 12. Provenance, validation and references

The three exploratory agents share model and repository provenance; their
agreement is not independent external refereeing. Distinct exact formulations
were used: literal versus regrouped four-pole forcing, independent finite
probability tables, direct Gaussian products versus transported products,
block-energy versus signed-lag expansion, and Machin shadow versus rational
BBP states. The root audited the derivations and reran the retained instruments.

See [claim supplement](../../docs/CLAIM_SUPPLEMENT_TWISTED_OBSERVER.md) and
[validation record](PI_TWISTED_OBSERVER_VALIDATION.md) for earned status,
commands, exact receipts and the final tested revision boundary. Imported
archival originals, provenance hashes and historical claim records are unchanged.

Primary mathematical and engineering sources consulted:

1. Bailey, Borwein and Plouffe, [On the Rapid Computation of Various
   Polylogarithmic Constants](https://www.davidhbailey.com/dhbpapers/digits.pdf):
   original source identity, not a normality theorem.
2. Bailey and Crandall, [Random Generators and Normal
   Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal.pdf): established
   normality results in specified classes and the source-dynamics program;
   no conjectural rational-forcing assertion is imported as proved.
3. Bailey and Misiurewicz, [A Strong Hot Spot
   Theorem](https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf): orbit
   frequency criteria; no ensemble-to-selected shortcut.
4. Tao, [The van der Corput trick, and equidistribution on
   nilmanifolds](https://terrytao.wordpress.com/2008/06/14/the-van-der-corputs-trick-and-equidistribution-on-nilmanifolds/):
   only the elementary classical correlation inequality is used and reproved
   above, not the general nilmanifold extension discussed in its correction.
5. Analog Devices, [Understanding Common-Mode
   Signals](https://www.analog.com/en/resources/technical-articles/understanding-commonmode-signals.html):
   physical motivation for a balanced differential readout. Its engineering
   cancellation mechanism is not treated as a theorem about BBP phases.

**Final mathematical boundary:** exact and stable observer agreement are now
distinguished and implemented. The authentic source's signed correlation
decay, pi normality in any requested base, and pi-specific independence remain
unproved by this round.
