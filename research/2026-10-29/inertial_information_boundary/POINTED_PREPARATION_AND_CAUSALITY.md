# Pointed inertial preparation, exact coding and causal boundary selection

**Date:** 2026-10-29. **Parent:** research PR #367 at
`b6a3815ceb505de0b1f570eae3ff5be75cdbe99c`.
**Branch:** `research/inertial-information-boundary-2026-10-29`.
**Authority:** elementary paper proofs and separately scoped exact tests.
No physical carrier law, cognitive model, Lean proof, scholarly priority,
pi-normality proof or RH proof is claimed.

The author's claim is explicitly **relative**: a neutral boundary needs no
additional preparation relative to an inertial carrier, while selecting a
nonneutral boundary requires an intervention. The results below preserve that
claim. They distinguish preparation cost, the bit length of a framed message,
and the information in a probability law. Their units and hypotheses differ.

## 1. The pointed preparation theorem

Let `Omega` be a state space with an actualized observable `q:Omega->A` and
a distinguished neutral value `0 in A`. Let `F=q^(-1)({0})` be its nonempty
neutral fiber. A preparation is a finite word of declared state maps, each
with nonnegative cost; word cost is the sum. Assume:

1. The unprepared initial state lies in `F`.
2. Every zero-cost instruction maps all of `F` into `F`.
3. Every positive-cost instruction costs at least a fixed `delta>0`.

The third condition holds for a finite grammar with at least one paid
instruction. It needs a separate assumption for an infinite instruction family.

### Theorem PPC-01: zero is the unique zero-cost actualized boundary

Every zero-cost preparation ends in `F`. Every reachable nonneutral value
has preparation cost at least `delta`. Neutral zero is reachable at cost
zero by the empty preparation.

**Proof.** Nonnegative summands total zero only if every instruction has cost
zero. Induction then keeps the state in `F`. A word ending outside `F` must
contain a paid instruction, so its total cost is at least `delta`. The empty
word leaves the initial state in `F`. QED.

This concerns the actualized value, not the cardinality of its microstate
fiber. It also does not say every preparation ending at zero is free: paid
interventions can cancel.

**Failed assumptions.** A free instruction leaving `F` from a freely reachable state in `F` makes
a nonneutral boundary free. Preservation of all of `F` is sufficient, not
necessary when some microstates are unreachable. An infinite family of nonneutral preparations with positive
costs tending to zero has zero infimum cost despite charging for each word.
The uniform gap prevents this second ambiguity. These are explicit model
choices, not consequences of the word "inertial" alone.

### An exact arithmetic preparation grammar

For integer radix `b>=2`, take actual states in `Z` and instructions

$$
R:u\mapsto bu,\qquad N:u\mapsto-u,\qquad
+:u\mapsto u+1,\qquad -:u\mapsto u-1.
$$

Declare `R,N` free and `+,-` to cost one intervention each. Every free word
fixes zero; every integer is reachable by unit instructions. PPC-01 applies.
Within this arithmetic structure the neutral point is also characterized
intrinsically: `bu=u` with `b>=2` forces `u=0`. Thus zero is the unique common
fixed point of the declared free radix and sign operations. A change of
coordinates transports these operations and their fixed point together.
For `b=16`, the words `-` and `-R` prepare `-1` and `-16`, both with exact
minimum intervention cost one. Their binary descriptions need not have
equal lengths. The word `+-` returns to zero with cost two.

The implementation admits finite affine grammars `u->m*u+d` with exact
rational coefficients and costs. A free instruction is accepted only when
`d=0`, the exact condition for fixing zero. A free translation by `-1` or
the mutant free radix map `u->16u+1` is rejected at construction.

## 2. A complete framed integer code and its exact limitation

The positive-integer ingredient is the classical Elias gamma construction;
see P. Elias, *Universal codeword sets and representations of the integers*,
IEEE Transactions on Information Theory 21(2), 194--203 (1975),
[publisher record](https://ieeexplore.ieee.org/abstract/document/1055349),
[DOI](https://doi.org/10.1109/TIT.1975.1055349).
The signed framing below is declared here. Every property used is proved.

For `m>=1`, set `k=floor(log_2 m)` and let `bin(m)` be its `k+1`-bit
binary representation. Define `gamma(m)=0^k bin(m)`. Now put

$$
\operatorname{code}(0)=0,\qquad
\operatorname{code}(n)=1\,\operatorname{signbit}(n)\,\gamma(|n|)
\quad(n\ne0),
$$

where the sign bit is zero for positive and one for negative.

| Integer | Codeword | Bit length |
|---:|---|---:|
| 0 | `0` | 1 |
| 1 | `101` | 3 |
| -1 | `111` | 3 |
| -16 | `11000010000` | 11 |

### Theorem PPC-02: decoding, prefix property and Kraft equality

This code is injective and prefix-free. Its lengths are

$$
\ell(0)=1,\qquad
\ell(n)=2\lfloor\log_2|n|\rfloor+3\quad(n\ne0).
$$

Its full Kraft sum is one, and at every complete magnitude shell,

$$
\sum_{|n|\le2^{K+1}-1}2^{-\ell(n)}=1-2^{-(K+2)}\quad(K\ge0).
$$

**Proof.** The first bit distinguishes zero from nonzero. For nonzero
symbols read the sign, count payload zeros until its first one, and then
read exactly that many additional bits. The first one and those additional
bits determine the magnitude. Its own leading-zero count fixes a complete
payload's length, so no complete payload is a proper prefix of another.
This gives exact unique decoding. A decoder for one complete codeword must
reject extra trailing bits, not silently ignore them.

At magnitude level `k`, there are `2^k` positive and `2^k` negative symbols,
all with length `2k+3`. Their Kraft contribution is `2^(-k-2)`. Adding
the zero contribution `1/2` and summing the geometric series proves both
the full equality and the displayed partial sum. QED.

For arbitrary maximum magnitude `M`, the exact partial sum is

$$
\frac12+\sum_{k:2^k\le M}
\frac{\min(M,2^{k+1}-1)-2^k+1}{2^{2k+2}}.
$$

This rational number is returned by `integer_kraft_partial`.

### Empty preparation is not an empty multiclass codeword

The empty instruction word requires no intervention. A self-delimiting
code with more than one possible message cannot contain the empty bit
string: it prefixes every other codeword. The displayed code therefore
uses the one-bit word `0` for zero.

A default/no-message protocol can exist if the parties share a frame or
observation interval indicating when a message would have arrived. That
convention belongs to the protocol. It does not violate the prefix result.

### Exact countercoding control

Swap the labels zero and minus one while retaining the set of codewords.
The new code remains injective and prefix-free, but minus one has length one
and zero length three. Thus fixed-numeral rankings are not invariant under
all coding conventions. This does not refute PPC-01: that theorem fixes the
preparation reference and allowed free operations before comparing costs.

Neither these framed lengths nor intervention counts are Shannon entropy,
relative entropy or machine-independent Kolmogorov complexity. A separate
information-law statement needs a specified law or reference machine.

## 3. Causal neutrality selects the retarded response

Fix integer `b>=2`. For every real forcing sequence `r=(r_1,r_2,...)`,
let a response assignment satisfy

$$
U_n(r)=bU_{n-1}(r)+r_n\quad(n\ge1).
\tag{3.1}
$$

Require **prefix causality**, including time zero: inputs agreeing through
time `n` have equal responses through time `n`. A compatible family of
finite-prefix maps is equivalent. Also require **unprepared neutrality**,
`U_n(0)=0`. A separately supplied initial preparation is an additional
input, not silently part of the unprepared response law.

### Theorem PPC-03: unique causal neutral response

The unique assignment satisfying these conditions is

$$
U_0(r)=0,\qquad U_n(r)=\sum_{k=1}^n b^{n-k}r_k.
\tag{3.2}
$$

**Proof.** Every input shares the empty prefix with zero input, so causality
gives `U_0(r)=U_0(0)=0`. Induction yields (3.2). Conversely, those finite
sums are causal, satisfy the recurrence and vanish on zero input. QED.

No linearity axiom is needed: linearity follows from the result. This is a
selection theorem across counterfactual inputs, without invoking normality,
pi, entropy or a claimed physical law.

If a preparation `c` is supplied, the general solution is

$$
U_n(c)=b^nc+\sum_{k=1}^n b^{n-k}r_k.
\tag{3.3}
$$

Writing `Y_n=b^(-n)U_n` gives

$$
Y_n=c+\sum_{k=1}^n b^{-k}r_k,
\qquad Y_n-Y_{n-1}=b^{-n}r_n.
\tag{3.4}
$$

Inertia alone permits every constant `Y=c` under zero forcing. A cost
depending only on `Y` increments cannot distinguish these constants.
Neutrality supplies the missing preparation boundary; it does not follow
from the recurrence alone.

**Naturality alternative.** Causality makes `U_0(r)=c` input-independent.
If the response rule is also sign-equivariant, `U(-r)=-U(r)`, then `c=-c`
and hence `c=0`. This is symmetry of a universal response rule across
different sources, not a forced symmetry of the authentic BBP forcing or
its positive virtual field. Without causality, sign equivariance alone
permits anticipatory nonzero seeds.

## 4. Future minimization selects an anticipatory boundary

For a finite forcing prefix of length `N`, the unique seed making `U_N=0`
is also the unique minimizer of `U_N(c)^2`:

$$
c_N^{\rm adv}=-\sum_{k=1}^N b^{-k}r_k.
\tag{4.1}
$$

For `r_1=1`, it is `-1/b`, not zero. Minimizing `U_0(c)^2+U_1(c)^2`
instead gives `-b/(1+b^2)`. Minimal initial preparation and minimal future
trajectory size are distinct optimization problems.

Changing only `r_(N+1)` by `epsilon` changes the advanced seed for the
extended prefix by `-b^(-(N+1))*epsilon`: the response at time zero changes
before the altered source arrives. Retarded earlier responses do not
change. This is an exact finite causality discriminator.

For the authentic BBP forcing, the infinite version converges to `-pi/16`
and gives the inherited coherent changed-seed response `V_n=-T_n`.
Unprepared causal neutrality excludes that anticipatory boundary. Excluding
it does not prove cancellation of the retarded response; section 8 gives a
zero-seeded coherent-source control.

## 5. Pointedness and coordinate changes

A neutral state is a marked point, not a numeral invariant under arbitrary
coordinate labels. The static translation `X_n=U_n-a` gives

$$
X_n=bX_{n-1}+r_n+(b-1)a.
\tag{5.1}
$$

It changes the forcing. The moving inertial origin `X_n=U_n-b^n a`
instead preserves the forcing:

$$
X_n=bX_{n-1}+r_n,\qquad X_0=U_0-a.
\tag{5.2}
$$

The marked unprepared state must be transported along with the coordinates.
Declaring `X_0=0` while discarding its transformed marked point selects a
different preparation; it is not a coordinate-only proof that every seed
is neutral. Equations (5.1)--(5.2) follow by direct substitution and identify
the reference data needed by the author's relative claim. An unpointed
affine torsor does not choose an origin by itself.

## 6. Rich virtual support in the neutral actualized fiber

Take `Omega=R x V`, `q(u,v)=u`, and any probability `nu` on `V`, including
a full-support law. Then

$$
\delta_0(du)\,\nu(dv)
$$

has exactly neutral actualization and a nonempty virtual field. The same
holds for any law supported on `q^(-1)(0)`. Free transformations may
rearrange that fiber while preserving the actualized coordinate; PPC-01
does not require every internal coordinate to vanish.

On a finite neutral fiber, maximum entropy with no additional constraints
selects its uniform law. This is compatible with actualized zero; it is
not a uniform law over nonzero actual seeds. On an unrestricted unbounded
space, an entropy maximizer need not exist.

If a virtual law is literally the marginal law of `U_0`, exact `U_0=0`
forces that marginal to be `delta_0`. A symmetric mixture of nonzero seeds
has zero expectation, not zero realization. Rich hidden support and a sharp
actualized boundary must therefore retain distinct types.

If the full dynamics obeys the exact factor law

$$
q(T_r\omega)=bq(\omega)+r,
$$

then every hidden history starting in the neutral fiber has the same
retarded arithmetic history. Hidden randomness cannot change that factor.
This is the inherited deterministic-factor obstruction in pointed form;
it does not rule out cancellation across different arithmetic source times.

## 7. Conserved charge and exactly what phases erase

### Theorem PPC-04: finite-time charge reconstruction

Given an exact source prefix and one exact state at time `n`, the initial
homogeneous charge is

$$
c=b^{-n}U_n-\sum_{k=1}^n b^{-k}r_k.
\tag{7.1}
$$

**Proof.** Divide (3.3) by `b^n` and subtract the finite source sum. QED.

This uses no future data. It shows that the exact state and source prefix
preserve the charge; a phase-only observation may erase it.

Same-forcing histories with seed difference `delta` satisfy

$$
U_n(c+\delta)-U_n(c)=b^n\delta,
$$

so at integer frequency `h!=0` their character ratio is

$$
\exp(2\pi i h b^n\delta).
\tag{7.2}
$$

### Theorem PPC-05: exact eventual phase equivalence

For rational `delta`, let `q` be the reduced denominator of `h*delta`.
The characters agree at time `n` exactly when `q | b^n`; agreement then
persists at all later times. Thus equality for every `n>=N` is equivalent
to `q | b^N`.

An eventual equality time exists exactly when every prime dividing `q`
divides `b`. Its least value is

$$
N_* =\max_{p\mid q}\left\lceil\frac{v_p(q)}{v_p(b)}\right\rceil,
\tag{7.3}
$$

with empty maximum zero if `q=1`.

**Proof.** The exponential in (7.2) is one exactly when its argument is an
integer. Reduce `h*delta` to coprime numerator and denominator and apply
this criterion. Prime valuations give (7.3). Further multiplication by
integer powers of `b` preserves divisibility. QED.

The algorithm repeatedly divides the denominator by its gcd with `b`.
Each iteration removes one step's available prime valuations. If the gcd
becomes one first, an outside prime proves impossibility. This exact
terminating test is not a finite-time empirical guess.

Integer seed offsets are invisible at every integer frequency and every
time, including zero. For `b=16`, offset `1/16` is invisible from time one
and `1/256` from time two. Offset `1/3` is never invisible at frequency one
in base 16; it is invisible from time one in base 3 and from time zero at
frequency three in either base.

Thus neutral preparation may select zero over `-1` while their original
integer-frequency phase histories are already identical. A phase probe
cannot distinguish them. The inherited irrational changed seed `-pi/16`
is a different kind of boundary change, not an integer or finite radix-
denominator offset.

## 8. A neutral, richly supported coherent source family

For real `d>=0`, define the different positive source

$$
R_d(a)=\frac{16}{(a+d)^2}-\frac1{(a+d+8)^2},\qquad a>0,
$$

and `r_n^(d)=R_d(8n-7)`. It has the exact positive Laplace representation

$$
R_d(a)=\int_0^\infty e^{-ax}
xe^{-dx}(16-e^{-8x})\,dx.
\tag{8.1}
$$

The kernel is strictly positive for every `x>0`; its normalized exponential
tilts have full positive support. This is a labelled countercontrol, not
the authentic signed four-pole source.

### Theorem PPC-06: positive zero-seeded coherent response

For every `n>=0`, put

$$
U_n^{(d)}=\frac{16^n}{(d+1)^2}-\frac1{(8n+d+1)^2}.
\tag{8.2}
$$

Then `U_0^(d)=0`, `U_n^(d)=16U_(n-1)^(d)+r_n^(d)`, the forcing is
positive, and `r_n^(d)~15/(64n^2)`. For nonnegative rational `d`, choose
`h` equal to the positive reduced denominator of `(d+1)^(-2)`. Then

$$
\exp(2\pi i hU_n^{(d)})
=\exp\left(-\frac{2\pi i h}{(8n+d+1)^2}\right)\longrightarrow1,
\tag{8.3}
$$

and its normalized character mean tends to one.

**Proof.** At `n=0` the two terms in (8.2) coincide. Subtracting
`16U_(n-1)^(d)` cancels the expanding term and yields
`16/(8n+d-7)^2-1/(8n+d+1)^2`, exactly the declared source.
Positivity follows from (8.1), and the leading asymptotic follows by
dividing denominators by `n^2`. The chosen integer `h` makes the expanding
first term in `hU_n^(d)` an integer. The remaining exponent tends to zero,
giving (8.3); the elementary Cesaro implication gives its mean limit. QED.

### This control has the parent's full convolution structure

Exact factorization gives

$$
R_d(a)=\frac{15(a+d+32/5)(a+d+32/3)}{(a+d)^2(a+d+8)^2}.
\tag{8.4}
$$

Apply the paired pole-zero criterion in
[the parent atomic dossier, section 11](../recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md)
with unpaired shifts `(d,d+8)` and pairs `(d,d+32/5)`,
`(d+8,d+32/3)`. Every zero shift exceeds its paired pole shift. This source
therefore also has arbitrary convolution subdivision, compatible source
tilting and strict connected logarithmic interactions of every finite order.

It satisfies neutral causal preparation and a richly supported positive
carrier with the parent's subdivision properties, but fails generic signed
cancellation. It does not refute a theorem essentially using the authentic
BBP coefficients and zero boundary together. It shows why source-specific
signed arithmetic remains necessary after neutral preparation is selected.

## 9. Instrument and proof boundaries

The module
[`inertial_information_boundary.py`](../../../observational_succ/inertial_information_boundary.py)
uses standard-library exact integers and `Fraction` values. It exposes the
codec, partial Kraft mass, validated affine preparations, finite recurrence
and charge reconstruction, advanced boundary, exact phase residues and
eventual equivalence, native source histories and the labelled coherent
family. Existing native source files remain unchanged.

The focused
[`tests`](../../../tests/test_inertial_information_boundary.py)
compare source values against a separate native implementation, reconstruct
responses by finite Green sums, compare phase ratios from separate histories,
and reject coding and free-displacement mutants. Finite tests corroborate
these instruments; they do not prove infinite statements by sampling.

| Statement | Status and boundary |
|---|---|
| PPC-01, unique zero-cost actualized boundary | PROVED LOCAL (paper) with a pointed free-operation class and positive cost gap |
| PPC-02, signed prefix code and Kraft mass | PROVED LOCAL (paper) for the declared framing |
| Zero is shortest under every recoding | REFUTED by the zero/minus-one label swap |
| Empty codeword with several prefix-coded outcomes | REFUTED by the prefix definition |
| PPC-03, causal neutrality selects zero | PROVED LOCAL (paper) for a universal compatible response law |
| Inertia alone selects zero | REFUTED by arbitrary constant scaled responses |
| Future trajectory minimization selects zero | REFUTED by the one-step advanced seed |
| PPC-04, finite charge reconstruction | PROVED LOCAL (paper) from exact state and complete source prefix |
| PPC-05, phase equivalence and first time | PROVED LOCAL (paper); the observer can erase seed information |
| PPC-06, rich positive zero-seeded coherent family | PROVED LOCAL (paper); generic-selection-to-cancellation countermodel |
| Authentic zero-seeded BBP signed cancellation | OPEN |

The next arithmetic theorem must use both the original source and selected
boundary to bound the remaining signed time average. It must respect the
exact observer kernel: integer and eventual radix-denominator seed changes
can be phase-tail identical while their preparation records remain distinct.
