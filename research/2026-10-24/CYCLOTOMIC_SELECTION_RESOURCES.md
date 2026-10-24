# Selected-source observations: sharp norm costs, exact clocks, and delayed inverse information

**Authority:** PROVED LOCAL, PAPER, with separately identified exact finite
checks. These are elementary Fourier, metric and arithmetic results newly
assembled for this research program; academic priority is unverified.
No theorem here establishes a vanishing Fourier mode of pi.

**Source boundary:** this work starts at PR #257,
`5435497dc77a313d1ebbc56ac96c11e593db2619`, above PR #253 and the corrected
BBP source #252. It does not import an assumption or theorem from sibling
PR #254/#256. The BBP identification used below is the inherited exact
identity `16 T_0 = pi`, with forced initial condition `y_0 = 0`.

Throughout, `e(t)=exp(2 pi i t)`, the circle is `T=R/Z`, Haar measure has
total mass one, and `d_T(x,y)=min_(n in Z)|x-y-n|`. Let integer `b>=2`,
integer `h!=0`, and integer `N>=1` be fixed when a finite identity is used.

## 1. Independent audit of the inherited origin geometry

The source contract, code and tests in
`CIRCLE_CYCLOTOMIC_ORIGIN_GAUGE.md`, `circle_origin_gauge.py` and its test
module were inspected directly. The following checks found no analytic
error in the stated domains.

* `R_-a T_b R_a(x)=b x+(b-1)a` and
  `H_(d+e)(a)=H_d(a)+b^d H_e(a)` follow by expanding actual maps. A change
  of initial source under an unchanged map is a different operation.
* The projective chord formula follows from
  `e(x)=(1+i tan(pi*x))/(1-i tan(pi*x))`. Substitution of
  `(s+tau)/(1-s*tau)` preserves that chord wherever both finite charts
  are defined. Excluded poles are chart boundaries.
* Fixed-point counts partition by minimal period, so Mobius inversion
  counts primitive dynamical points; cyclotomic polynomial values do not.
* For `x_d=1/(b^d-1)`, its minimal period is `d`. The exact circle
  Wasserstein-to-zero formula requires `b>=3`, as stated: then every
  representative `b^j/(b^d-1)` lies below one half. The formula is not
  transferred to base two.
* The fourth moment is `(2N^2-N)/N^4`. For base two, equal-exponent
  pairs yield one binary bit after carrying, while unequal-exponent
  pairs yield two. These cases cannot alias each other as integers.
* A regular `m`-gon has circle Wasserstein distance `1/(4m)` from Haar.
  Nearest-cell transport proves the upper bound and the distance-to-grid
  1-Lipschitz function proves the lower bound. This includes `m=1`.
* The moving BBP origin residual and finite lag boundary follow by exact
  telescoping, with the endpoint indices used in the code.

One implementation authority caveat is essential. The helper
`certified_cyclotomic_pi_shadow(lo,hi,...)` checks interval ordering,
containment in `(3,4)`, and unique rounding. Those guards do not themselves
prove `lo <= pi <= hi`. Membership is a caller-supplied source premise.
The inherited actual-pi test correctly supplies independently derived
polygon bounds. An arbitrary interval inside `(3,4)` is not an authentic
pi source merely because it passes those guards.

## 2. Exactly what the ensemble can and cannot lift to a selected point

Define

    G_x(a) = (1/N) sum_(j=0)^(N-1) e(h b^j (x+a)),
    V_N = span_C { a -> e(h b^j a) : 0<=j<N }.

### SOR-01. Sharp selected-point norm

For every `a_0 in T`, evaluation `f -> f(a_0)` on `V_N`, equipped with
Haar `L2`, has operator norm **exactly `sqrt(N)`**.

Write `f(a)=sum_j c_j e(h b^j a)`. Fourier orthogonality gives
`||f||_2^2=sum_j|c_j|^2`. Cauchy--Schwarz therefore gives
`|f(a_0)|<=sqrt(N)||f||_2`. Equality holds for
`c_j=e(-h b^j a_0)`, proving sharpness.

In particular, for every selected `x`,

    ||G_x||_2 = N^(-1/2),
    ||G_x||_4 = (2N^2-N)^(1/4)/N,
    ||G_x||_infinity = 1.

The last equality is attained at `a=-x`. Thus the exact peak-to-fourth-
moment ratio in this actual orbit-response family is

    N/(2N^2-N)^(1/4),

which also grows like `sqrt(N)`. The sharp `L2` evaluation factor uses
up the entire `N^(-1/2)` gain of the averaged second moment. Any uniform
`L4` evaluation bound for this family must similarly have at least the
displayed factor. This is a lower bound; it is not a claim that the same
factor is the exact `L4` operator norm on all of `V_N`.

### SOR-02. Every translation-invariant ensemble descriptor is source-blind

The exact identity `G_x(a)=G_0(a+x)` implies that every translation-
invariant functional of this response is independent of `x`. This covers
the complete Haar distribution of values, every Haar `Lp` norm, and every
Haar norm of every derivative that is defined. In particular,

    ||G'_x||_2^2 = (2 pi h/N)^2 (b^(2N)-1)/(b^2-1).

All derivatives exist, because these are finite trigonometric sums.
No interchange of an infinite sum and differentiation occurs.

**Restricted no-go, with its quantifiers:** a bound on `|G_x(0)|` that
uses only these source-independent descriptors and is asserted uniformly
for all `x in T` cannot tend to zero. The admissible source `x=0` has
`G_0(0)=1` for every `N`. Adding the exact derivative norm to the second
and fourth moments does not repair this inference, because its value is
also independent of `x`.

This does not prove an impossibility theorem about the complete BBP
source. The exact four-pole source and authenticated boundary value
exclude `x=0`; they are information outside these descriptors. A genuine
BBP proof must actually use that information in a point-sensitive way.
Merely computing the same ensemble descriptors for the authenticated
source still discards the relevant information.

### SOR-03. Quantified near-peak and precision bounds

Set `S_N=(b^N-1)/(b-1)` and
`D_N=2 pi |h| S_N/N`. The elementary chord bound gives, for real `a`,

    |G_0(a)-1| <= D_N |a|.

Thus the exceptional source is uniformly near its maximal value on
`|a|<=eta/D_N`, for every `eta>0`. The scale is a constant times
`N b^(-N)` for fixed `eta,b,h`. This exponentially narrow neighborhood
is fully compatible with small global second and fourth moments.

There is also a two-sided local conditioning statement. If
`0<=|a|<=1/(4 |h| b^(N-1))`, use
`sin(theta)>=2 theta/pi` on `[0,pi/2]`, taking the sign of `h a`:

    (4 |h| S_N/N)|a| <= |G_0(a)-1| <= D_N |a|.

Every summand's imaginary part has the same sign in this range. This
proves that the derivative-scale sensitivity is real, rather than an
artifact of an upper estimate. It is a local statement; it does not claim
that fixed-error approximation of a normalized average always requires
full last-digit accuracy.

For comparison, averaging over the interval `[-delta,delta]`, with
`0<delta<=1/2`, proves the legitimate pointwise inequality

    |G_x(0)| <= ((2N^2-N)/(2 delta N^4))^(1/4) + D_N delta/2.

The first term is Holder's inequality; the second is the mean Lipschitz
error `D_N average|a|`. The growing `D_N` prevents this generic procedure
from extracting a vanishing uniform bound. SOR-02 already proves this
failure without relying on the numerical optimization of the estimate.

## 3. Complete finite tomography clocks, including nonunits

Let `m>=2` be an integer and set `q=m/gcd(m,|h|)`. Factor it by genuine
prime powers as `q=q_s q_c`, where every prime of `q_s` divides `b`, and
`gcd(q_c,b)=1`. Put

    tau = max_(p|b) ceil(v_p(q)/v_p(b)),
    L = ord_(q_c)(b), with ord_1(b)=1.

An empty maximum is zero. The valuations in this display are valuations
of integers, and prime powers from `q_s` and `q_c` are relatively prime.

### SOR-04. Exact onset, period, and nonalias criterion

The sequence `h b^j mod m`, for `j>=0`, has exact preperiod `tau` and
exact eventual period `L`. Its first `N` entries are distinct if and only if

    N <= tau+L.

Proof: cancel `gcd(m,h)`. For `0<=i<j`, a collision is equivalent to
`q | b^i (b^(j-i)-1)`. For `p|b`, the second factor is a unit modulo `p`,
so the `p` condition is exactly `i v_p(b)>=v_p(q)`. Together these are
`i>=tau`. For the coprime component, the condition is exactly
`L | (j-i)`. Hence the earliest repeated index is `tau+L`, repeating
index `tau`, and no earlier collision occurs. This also proves minimality
of the preperiod and eventual period, including `q=1`.

CRT makes the eventual clock explicit:

    L = lcm_(p^a || q_c) ord_(p^a)(b).

Thus neither treating a composite modulus as a prime nor replacing its
prime powers by their square-free radical is lawful. The earlier
coprime-order condition is recovered when `tau=0`; it was sufficient,
not necessary.

### SOR-05. Linear-size hexadecimal tomography clocks

For `b=16`, one has for every integer `u>=1`

    v_3(16^u-1)=1+v_3(u),
    ord_(3^a)(16)=3^(a-1)  (a>=1).

Proof without an imported order assumption: start with `16=1+3*5`.
If `A=1+3^r v`, `r>=1`, `3` does not divide `v`, expansion of `A^3-1`
shows valuation `r+1`. Repeated cubing handles powers of three. For an
exponent relatively prime to three, the geometric quotient is that
exponent modulo three, hence a unit. This proves the valuation identity
and the order formula.

Let `v=v_3(|h|)` and `c` be the least nonnegative integer with `3^c>=N`.
Then the actual grid

    m = 3^(v+1+c)

has `N` distinct frequencies and therefore gives exact reconstruction and
the exact source-independent second moment on that grid. Its sample count
satisfies

    3^(v+1) N <= m < 3^(v+2) N.

For `N>=2`, it is the smallest power-of-three modulus that achieves the
required nonaliasing. For `N=1` the displayed choice remains sufficient;
minimality is not asserted. For fixed `h`, this is a deterministic linear
sample-count upper bound, in contrast with the exponentially large
trivial clock `m>b^(N-1)|h|`. It says nothing about the cost of obtaining
each source response `G_x(r/m)`: these are not free observations, and
their evaluation already involves the selected orbit.

### SOR-06. Second-moment clock closure does not provide fourth moments

For `b=16`, `N>=2`, a power-of-three grid, and `v=v_3(|h|)`, every unordered pair sum
`h(b^j+b^k)` is congruent to `2h` modulo `3^(v+1)`. Distinct pair labels
therefore require

    m >= 3^(v+1) N(N+1)/2.

Here `N>=2` is necessary unless one separately assumes
`m>=3^(v+1)`: if the modulus is smaller, there is only one available
residue class, which already prevents the required three or more pair
labels when `N>=2`. For `N=1,h=9,m=3`, the sole pair label is distinct
but the displayed lower bound would be false. No such `N=1` claim is made.

Even this counting condition does not ensure distinctness. At
`b=16,h=1,N=3,m=27`, the source frequencies `1,16,256` are distinct
modulo 27 and `ord_27(16)=9`. But

    1+1 == 16+256 (mod 27),
    (16+256)-(1+1)=270.

Expanding the finite fourth moment, with the full selected-source phases
retained, gives exactly

    (1/27) sum_(r<27) |G_x(r/27)|^4
      = [15+4 cos(2 pi*270*x)]/81.

At `x=0` this is `19/81`, whereas the Haar fourth moment is `15/81`.
The capacity condition holds (`27>=18`), yet aliasing remains. For pi,
the displayed cosine is an actual selected-source term; setting it to
zero would assume an unproved and in fact inappropriate orthogonality.
This example separates exact phase reconstruction, second-moment design,
and fourth-moment design with one genuine prime-power clock.

## 4. What finite noisy tomography actually costs

Suppose `m` is nonaliased for the `N` frequencies. For any `f in V_N`,
discrete Fourier orthogonality gives

    c_k = (1/m) sum_(r<m) f(r/m) e(-h b^k r/m).

The coefficient map is an isometry from `V_N` with Haar `L2` to its
sampled vector with normalized discrete `l2`. Writing
`K_N(r)=sum_(j<N)e(-h b^j r/m)`, evaluation at zero is

    f(0) = (1/m) sum_(r<m) f(r/m) K_N(r).

The kernel has exact normalized discrete `l2` norm `sqrt(N)`.
Consequently sampled RMS error at most `epsilon` causes evaluation error
at most `sqrt(N)*epsilon` for this reconstruction, and the factor is
attained by a noise vector proportional to `conjugate(K_N)`.
Equivalently, the least-`l2` exact linear evaluation weights have this
norm: the orthogonal projection of any admissible weight vector onto the
sampled copy of `V_N` is the same representer, while an orthogonal
component only increases its norm.

This is **not** a universal lower bound for bounded pointwise noise.
The grid contains `a=0`; directly reading that sample has amplification
one in the uniform-noise norm. But such a readout is already a measurement
of the desired selected sum. It does not infer its smallness from the
small spatial mean square. Likewise a sparse known Fourier spectrum can
be reconstructed from a linear number of exact probes despite its large
maximum frequency. An exponential bandwidth must not be misreported as
an unconditional exponential sample-count lower bound.

## 5. Source-labelled inverse trees: information is hidden, not destroyed

For `k>=0`, write `M=b^k` and

    mu_(k,x) = (1/M) sum_(r=0)^(M-1) delta_((x+r)/M),

where `x in [0,1)` represents its circle point.

### SOR-07. Exact inverse-fibre conditioning

For every pair of circle points `x,y`,

    W1(mu_(k,x),mu_(k,y)) = d_T(x,y)/b^k.

Let `delta=d_T(x,y)`. Pair each point in the first lattice with its
nearest point in the second; a cyclic relabeling gives a bijection and
every distance is `delta/M`. This gives the upper bound. Conversely,
distance to the support of `mu_(k,x)` is 1-Lipschitz, is zero on that
support, and is identically `delta/M` on the other support. Integrating
this function gives the matching lower bound by the elementary transport
inequality `|integral f dmu-integral f dnu|<=W1(mu,nu)`.

The `k`-step pushforward recovers `delta_x` and `delta_y`, whose distance
is `delta`. Thus the Lipschitz amplification factor `b^k` of the forward
covering is sharp even on this highly structured class of inverse fibres.
If a Lipschitz test `f` is required to separate the two fibre averages by
an amount `eta>0`, its Lipschitz constant must satisfy

    Lip(f) >= eta*b^k/d_T(x,y).

This is an exact resource bound for that observer class, not a prohibition
on other measurements or an abstract information-loss claim.

### SOR-08. Exact Fourier invisibility and the first future observation

For integer `q`, finite character orthogonality gives

    integral e(q z) dmu_(k,x)(z)
      = 0                  if M does not divide q,
      = e((q/M)x)          if M divides q.

Hence an observer containing all nonzero characters `|q|<=H`, for integer
`H>=1`, sees exactly the same zero vector for **every** source whenever
`b^k>H`. This is exact equality of observations, not a small-error claim.
But the character `q=M` recovers `e(x)` exactly. Even the unlabelled full
measure retains the source; weak or fixed-bandwidth observation hides it.

After `j` forward pushes, `0<=j<=k`, the measure is `mu_(k-j,x)`.
Let `s` be the largest nonnegative integer with `b^s<=H`. The first time
a character in the cutoff can be source-sensitive is exactly

    j_0 = max(0,k-s).

Before `j_0`, all those characters vanish. At `j_0`, the character
`q=b^(k-j_0)<=H` has expectation `e(x)` and distinguishes every distinct
pair of circle roots. Consequently this finite-observer equivalence is
not future-sufficient for the expanding dynamics. Declaring it a quotient
that preserves every future observation would contradict this witness.

### SOR-09. Labelled history reconstruction and its boundary

For a labelled branch `(z,r)` with `0<=r<M` and `z=(x+r)/M`,

    x=M z-r.

Successive inverse branch choices `a_k in {0,...,b-1}` obey

    z_(k+1)=(z_k+a_k)/b,
    r_(k+1)=r_k+a_k b^k,
    r_(k+1) == r_k (mod b^k).

Thus finite inverse histories are exactly compatible base-b branch
prefixes together with the root. Uniform branch choices supply an
independent uniform prefix distribution; choosing or averaging branches
does not impose a law on the root's forward orbit.

Carrying a branch label authenticates the reconstruction route. It does
not remove the conditioning: an error `epsilon` in the real branch
coordinate gives root error at most `M epsilon`, and locally that factor
is attained. If the root is instead stored explicitly in the state, it
has already been supplied as information. The high-frequency readout
`e(Mz)=e(x)` also shows that exact labels are not necessary when an exact
branch coordinate and unrestricted frequencies are available.

For the actual BBP-selected root `x={16 T_0}={pi}`, these statements
recover the authenticated pi phase. For the unforced fixed source `x=0`
they recover zero, with identical Haar-limit and cutoff properties.
They therefore provide an exact source-recovery invariant and a sharp
future-observer obstruction, but no selected-source cancellation theorem.

## 6. Applying the actual BBP correction hierarchy to the observer

Use the inherited definitions in `PI_SOURCE_GENESIS_GREEN.md`:

    q_n^(K)=y_n+A_K(n),
    z_n=y_n+T_n=16^(n-1)*pi (mod1),
    z_n=q_n^(K)+(-1)^K E_K(n) (mod1),
    0<E_K(n)<a_K B(8n+1,K+2),
    E_K(n)=integral_0^1 u^n dnu_K(u).

Here `K>=0`, `n>=1`, `nu_K` is the strictly positive Hausdorff measure
proved there, and `a_K` is the exact Pell-product coefficient. Nothing
from sibling PR #254 is needed for these inherited facts.

### SOR-10. Source-specific corrected-response error, and exact moment blindness

For integers `M>=0`, `N>=1`, let

    P(a)=(1/N) sum_(j<N) e(h 16^(M+j)*(pi+a)),
    Q_K(a)=(1/N) sum_(j<N)
             e(h [q_(M+j+1)^(K)+16^(M+j)*a]).

Orthogonality at the actual distinct frequencies proves the exact identity

    ||P-Q_K||_2^2
       =N^-2 sum_(j<N) |e(h E_K(M+j+1))-1|^2.

The sign `(-1)^K` disappears only inside this squared chord; the actual
complex response retains it. Since `E_K` decreases, the inherited
nonnegative-tail estimate gives

    sum_(n>=M+1) E_K(n)^2
       <= E_K(M+1) sum_(n>=M+1) E_K(n)
       < (a_K^2/8) B(8M+9,K+2) B(8M+2,K+1).

Therefore

    ||P-Q_K||_2^2
       < (2 pi h a_K/N)^2
            B(8M+9,K+2) B(8M+2,K+1)/8.

This is an all-horizon source-specific bound, with RMS error
`O_(h,K)(N^-1 (M+1)^(-K-3/2))` for each fixed `K`. It is not inferred
from finite tests. The proof uses the genuine signed remainder measure
and its rational beta mass bound.

Yet `P` and `Q_K` have **exactly the same** Haar second moment, fourth
moment, and every derivative `L2` norm: all their Fourier coefficients
have modulus `1/N`, and the fourth moment has only matched pairs.
These summaries cannot even detect the known, explicitly bounded
authentic rational-tail approximation error. Their agreement must not be
reported as an independent source-identification test.

### SOR-11. The first phase-sensitive origin moment, with a BBP sign law

More generally, for integer base `b>=2`, sums of `k` powers of `b` have
unique unordered exponent multisets whenever `1<=k<=b`. For `k<b`, this
is uniqueness of base-b digits with all coefficients less than `b`. For
`k=b`, a carry can only occur when all `b` summands have the same
exponent; its canonical representation is one power, which cannot equal
a no-carry representation containing `b` summands. Two such single-carry
representations agree only when their exponents agree.

Consequently, for any unit-modulus coefficient vector `c_j`, the response
`N^-1 sum_(j<N)c_j e(h b^j a)` has source-blind Haar moments through
order `2b`. Its exact `2k`th moment in this range is

    N^(-2k) sum_(alpha_0+...+alpha_(N-1)=k)
                   [k!/(alpha_0!...alpha_(N-1)!)]^2.

For base sixteen, **all even moments through order 32** have this
blindness. The first possible nontrivial equal-cardinality relation is
at `k=b+1`:

    b*b^j+b^(j+d+1)=b^(j+1)+b*b^(j+d),  d>=1.

This is an additive carry relation, not cancellation of an incomplete
temporal Fourier sum.

The phrase "first phase-sensitive moment" concerns arbitrary unit
coefficient vectors and the rational corrected responses. The actual
covering responses `G_x` are translations of one another, so **all** their
Haar moments, of every order, are independent of the selected `x`.
No higher moment of that translated family can select pi over a fixed
orbit merely by its value.

For the actual corrected BBP phases, define its signed three/four-time
carry defect, with `n>=1,d>=1`, by

    Delta_(K,d)(n)
      =16 q_n^(K)+q_(n+d+1)^(K)-q_(n+1)^(K)-16 q_(n+d)^(K) (mod1).

The true selected phases `z_n` have zero defect. Subtracting their signed
remainders gives the exact source-specific law

    Delta_(K,d)(n) == -(-1)^K F_(K,d)(n) (mod1),
    F_(K,d)(n)=integral_0^1 u^n (16-u)(1-u^d) dnu_K(u) > 0.

In particular the actual complex carry character is
`e(h Delta_(K,d)(n))=e(-h (-1)^K F_(K,d)(n))`; its orientation has not
been replaced by an absolute path cost.

Thus `F_(K,d)` is itself a strict Hausdorff moment sequence. It is not
an arbitrary choice of correction sign. In the original t variable,
the bounds `16-t^8<=16`, `1-t^(8d)<=8d(1-t)`, and the inherited
Taylor remainder give, for all these parameters,

    0<F_(K,d)(n)<128 d a_K B(8n+1,K+3),
    F_(K,d)(n)<16 a_K B(8n+1,K+2).

These moment identities and bounds also hold at n=0, by the same finite
measure representation. The orbit-indexed observer below uses n>=1.

For `K=0` the same quantity is exactly rational:

    F_(0,d)(n)=r(n+1)-r(n+d+1)>0.

In fact **every finite-order defect is exactly rational**. An independent
formula, suitable for an exact oracle and requiring no pi digits, is

    F_(K,d)(n)=(-1)^K [r(n+1)-r(n+d+1)
        -16A_K(n)-A_K(n+d+1)+A_K(n+1)+16A_K(n+d)].

The positive Hausdorff representation proves the sign of this alternating
rational expression for all parameters; a finite sign sweep alone would
not prove it.

The equality follows independently by subtracting the two actual
recurrences `16T_n-T_(n+1)=r(n+1)`. For fixed `K,d` the first bound is
`O_(K,d)(n^(-K-3))`. No convergence in `K` at fixed `n` is asserted.

There is also a sharp fixed-order endpoint limit:

    F_(K,d)(n)/B(8n+1,K+3) -> 120 d a_K  as n->infinity.

Indeed the ratio of the t-integrand's non-power factor to
`(1-t)^(K+2)` tends to `a_K*15*8d`, is bounded by `128d a_K`, and
the normalized beta weight concentrates at `t=1`. The same elementary
concentration proof used for the inherited signed Taylor remainder
therefore applies. For `K=0` this gives
`F_(0,d)(n) ~ (15d/32)n^-3`, independently consistent with the difference
of the leading forcing terms `15/(64n^2)`.

There is a fully explicit observer for this signed defect. For any three
phases `theta_0,theta_1,theta_2`, write

    V(a)=[e(h[theta_0+a])+e(h[theta_1+16a])
                          +e(h[theta_2+256a])]/3.

Let

    D=sum_(alpha+beta+gamma=17) [17!/(alpha! beta! gamma!)]^2.

Then exact finite Fourier expansion yields

    integral |V(a)|^34 da
      =[D+34 cos(2 pi h [16theta_0+theta_2-17theta_1])]/3^34.

To verify that these are all terms, two triples of nonnegative counts
with total 17 and equal weighted sum at `1,16,256` have differences
`(16t,-17t,t)`. The count bounds force `t=0,1,-1`. The only nontrivial
pair is `(16,0,1)` versus `(0,17,0)`, whose multinomial multiplicities
are 17 and 1. This gives exactly the displayed cosine coefficient 34.

For the authentic covering phases `theta_i=z_(n+i)`, that cosine is one.
For the raw BBP forced phases `theta_i=y_(n+i)`, `h=1`, it equals
`cos(2 pi [r(n+2)-r(n+1)])<1` for every `n>=1`: positivity and monotonicity
give `0<r(n+1)-r(n+2)<r(2)<1`. Thus this 34th-moment observer **strictly
distinguishes** the authentic forced triple from its corrected absolute
covering triple, although all moments through order 32 are identical.
For every fixed `K,h`, the same distinction holds for sufficiently large
`n`, using `0<|h|F_(K,1)(n)<1` and the proved beta bound.
Its exact moment deficit is
`34[1-cos(2 pi h F_(K,1)(n))]/3^34`, asymptotic to
`68 pi^2 h^2 F_(K,1)(n)^2/3^34`. Thus its decay is explicitly of order
`n^(-2K-6)` for fixed `K,h`, with a nonzero source-derived constant.

This is a new source-specific sign and finite-observer result. It
authenticates the moving-origin correction. The complex carry character
retains its signed phase; the displayed 34th moment observes its real
part and does not itself distinguish conjugate phases. It does not make the selected covering orbit
generic: every unforced covering orbit, including a fixed orbit, has zero
carry defect. The remaining normality gap is not hidden in this observer.

## 7. Claim boundaries and the next discriminating use

The arithmetic clock theorem supplies an efficient exact observation
design; it does not produce source samples. The norm theorem proves the
cost of one particular ensemble-to-point inference and the impossibility
of a uniform vanishing bound from translation-invariant descriptors. The
inverse-tree theorem shows why convergence to Haar can coexist with exact
recovery of any selected source after a growing number of pushes.

These negative controls do not satisfy the complete BBP source contract.
They refute only statements whose hypotheses forget the selected root or
ignore all nontranslation-invariant source data. The exact four-pole
forcing, Green measure, Pell hierarchy and authenticated initial state
remain available; this work does not declare them globally insufficient.

A source-specific improvement must constrain the actual ordered Fourier
coefficients or the complementary BBP phases. Such a constraint could
reduce the relevant source class below the extremizers above. No such
constraint yielding a vanishing pi mode is assumed, proved, or hidden in
the word "lawful" here. The signed interference investigation is recorded
separately in `CYCLOTOMIC_SELECTED_INTERFERENCE.md`.

All displayed claims have elementary proofs above. The new exact oracle
records finite arithmetic examples separately; passing those examples is
not the authority for the all-parameter proofs. No new Lean authority is
claimed in this document unless explicitly linked by the formal report.
