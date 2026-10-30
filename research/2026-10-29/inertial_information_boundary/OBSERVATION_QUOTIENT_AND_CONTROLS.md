# Boundary information, phase quotients, and hostile source controls

**Date:** 2026-10-29. **Research parent:**
`b6a3815ceb505de0b1f570eae3ff5be75cdbe99c` (draft PR #367).
**Authority:** self-contained paper proofs; finite exact checks and mutation
receipts are separate. This dossier does not assert a physical inertia law,
human reasoning mechanism, original-BBP signed cancellation, or pi normality.

The author's information claim concerns the preparation of a **full pointed
carrier**. The Fourier observer sees a quotient of that carrier. These must
remain distinct: preparing `-1` may require an extra operation in a declared
resource model even though the subsequent integer-frequency BBP phases are
identical to those prepared at zero. An observation's inability to distinguish
two preparations does not make their preparation costs equal.

## 1. Full-state seed information and the exact phase ratio

Fix an integer `b>=2`, a real forcing sequence `(r_n)_(n>=1)`, and a real
initial seed `c`. Define

$$
U_0(c)=c,\qquad U_n(c)=bU_{n-1}(c)+r_n.
\tag{OQ-1}
$$

The forcing is held **identical** when seeds are compared. The authentic BBP
specialization is `b=16`,

$$
r_n=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\tag{OQ-2}
$$

Its source and zero-seed history are the preserved native objects in
[`succ_internal_matrix_walk.py`](../../../observational_succ/succ_internal_matrix_walk.py)
and
[`lambda_source_duality.py`](../../../observational_succ/lambda_source_duality.py).
Other bases in the finite oracle are declared controls for (OQ-1); they are not
claimed to be the original BBP recurrence for pi.

Set `A_n=U_n(0)`. Finite induction gives

$$
U_n(c)=b^n c+A_n,\qquad
A_n=\sum_{k=1}^n b^{n-k}r_k.
\tag{OQ-3}
$$

Consequently full real-state observation at any known finite time is injective
in the seed:

$$
c=b^{-n}(U_n(c)-A_n).
\tag{OQ-4}
$$

This is an exact arithmetic recovery with the forcing prefix supplied. It does
not claim that a finite-precision physical measurement recovers an arbitrary
real number.

For integer frequency `h`, write `e(x)=exp(2*pi*i*x)` and
`z_n^h(c)=e(hU_n(c))`. For two seeds with `delta=c-d`,

$$
\boxed{\frac{z_n^h(c)}{z_n^h(d)}=e(hb^n\delta).}
\tag{OQ-5}
$$

The source cancels from this **comparison**, not from either individual phase
sequence. No normality conclusion follows from that cancellation.

## 2. Absolute phase observations: exact kernel and first indistinguishable time

### Theorem OQ-A — observation from a specified start time

Fix `N>=0` and integer `h!=0`. For real seeds `c,d`, the following are
equivalent:

1. `z_n^h(c)=z_n^h(d)` for every `n>=N`.
2. `z_N^h(c)=z_N^h(d)`.
3. `h b^N(c-d)` is an integer.

Thus this observer identifies exactly the cosets of

$$
\frac1{|h|b^N}\mathbb Z.
\tag{OQ-6}
$$

**Proof.** Equality of phases means their ratio in (OQ-5) is one, equivalently
`h b^n delta` is integral. Condition 1 implies condition 2; condition 2 is
condition 3. If condition 3 holds, multiplying its integer by `b^(n-N)` proves
condition 1. QED.

For `h=0`, every phase is one and every seed is indistinguishable. The
nonzero-frequency hypothesis must not be silently dropped.

If **all** integer frequencies are observed from time `N`, the kernel is
`b^(-N) Z`, because frequency one is already present. More generally, for a
nonempty finite observation set of nonzero integer coefficients
`{h_j b^(n_j)}`, its exact common kernel is `(1/g) Z`, where
`g=gcd_j |h_j b^(n_j)|`. Indeed integrality of `g delta` implies integrality
of every multiple, and the converse follows from an integer Bezout combination.

### Corollary OQ-B — eventual absolute equivalence

Define the localization

$$
\mathbb Z[1/b]=\{m/b^k:m\in\mathbb Z,\ k\in\mathbb N\}.
$$

For all-frequency observation, two seeds eventually have identical phases iff

$$
\boxed{c-d\in\mathbb Z[1/b].}
\tag{OQ-7}
$$

For one fixed nonzero frequency, the eventual kernel is
`(1/h) Z[1/b]`. These statements are immediate unions of the kernels in
Theorem OQ-A over `N`. If the start time is allowed to depend on frequency,
frequency one still supplies a single start time that works for all frequencies.

For rational `h delta=p/q` in lowest terms, with `q>0`, eventual equivalence
holds iff every prime divisor of `q` divides `b`. Its least start time is

$$
N_{\min}=\max_{\ell\mid b}
\left\lceil\frac{v_\ell(q)}{v_\ell(b)}\right\rceil,
\tag{OQ-8}
$$

where the maximum is zero when `q=1`; if `q` has an external prime factor,
there is no such time. This follows exactly from `q | b^N`. Factoring a
denominator, or iteratively dividing it by `gcd(q,b)`, gives an exact finite
test. It is not a floating-point closeness criterion.

For `b=16`, `Z[1/16]=Z[1/2]`: the eventual absolute kernel consists of the
dyadic rationals.

### The author's `0`, `-1`, and `-16` examples

For the same authentic forcing, these seeds differ by integers. Therefore

$$
z_n^h(0)=z_n^h(-1)=z_n^h(-16)
\quad\text{for every integer }h\text{ and }n\ge0.
\tag{OQ-9}
$$

Their **real carrier states** differ by `b^n` or `16b^n`; those distinctions
have been erased by the phase map. A resource theorem can assign different
costs to their preparations. A theorem based only on these phases cannot
recover that cost difference.

Likewise, the seed `1/16` becomes absolutely phase-identical to zero from
time one; `1/256` does so from time two. Neither observation says that those
seeds require the same preparation program as zero.

## 3. Relative phase observations have a larger exact kernel

Absolute phase equality and equality of all pairwise phase ratios are different
observations. Define relative agreement from time `N` by

$$
\frac{z_n^h(c)}{z_m^h(c)}
=\frac{z_n^h(d)}{z_m^h(d)}
\quad\text{for every }m,n\ge N.
\tag{OQ-10}
$$

### Theorem OQ-C — relative-phase quotient

For `h!=0`, relative agreement from time `N` holds iff

$$
\boxed{h(b-1)b^N(c-d)\in\mathbb Z.}
\tag{OQ-11}
$$

Equivalently, the ratio in (OQ-5) is the single constant
`e(h b^N delta)` for all `n>=N`. The eventual all-frequency relative-phase
kernel is

$$
\boxed{\frac1{b-1}\mathbb Z[1/b],}
\tag{OQ-12}
$$

whereas the absolute-phase kernel remains `Z[1/b]`.

**Proof.** Relative agreement is exactly constancy of
`q_n=z_n^h(c)/z_n^h(d)`. Its adjacent ratio is

$$
q_{n+1}/q_n=e(h(b-1)b^n\delta).
$$

Constancy implies that this ratio equals one at `n=N`, giving (OQ-11).
Conversely integrality at `N` implies integrality at every later index by
multiplication by `b`, so all adjacent ratios equal one. Taking the union over
`N` and including frequency one proves (OQ-12). QED.

For the authentic base `b=16`, the seed offset `1/15` gives

$$
z_n^h(c+1/15)=e(h/15)z_n^h(c)
\quad(n\ge0).
\tag{OQ-13}
$$

It changes absolute phases unless `15|h`, but retains every relative phase.
The one-torsion example is already visible in sibling research; (OQ-11) gives
the complete classification for arbitrary real offsets, bases, frequencies,
and starts.

For offsets in (OQ-12), fixed-frequency Weyl sums on the two seeds differ by
one constant rotation after a finite prefix. Hence the `o(N)` property transfers
between those two explicitly related histories. This proves neither history
has that property. It is also not an unrestricted claim about rational changes
of arbitrary normal numbers.

These are kernels for **literal phase data** or literal relative-phase data.
Spectral data of a Gram matrix can erase additional distinctions under diagonal
unitary conjugation; the present classification does not claim that such
coarser spectral observations recover the relative phases.

## 4. Quantitative observability: exponential envelopes and exact aliases

For arbitrary real seeds, (OQ-5) gives the exact chord distance

$$
|z_n^h(c)-z_n^h(d)|
=2\left|\sin(\pi h b^n\delta)\right|
=2\sin\bigl(\pi\|h b^n\delta\|_{\mathbb R/\mathbb Z}\bigr).
\tag{OQ-14}
$$

Using `|sin t|<=|t|` yields

$$
\boxed{|z_n^h(c)-z_n^h(d)|
\le\min\{2,\ 2\pi|h|b^n|\delta|\}.}
\tag{OQ-15}
$$

Thus `2*pi*|h|*b^n*|delta|<=epsilon` is a sufficient finite-horizon
closeness condition. Its failure is **not** a sufficient distinguishability
condition: exact arithmetic aliases can make the chord zero even when the
real-state separation is enormous. A fully rational conservative bound is
`min(2,8*|h|*b^n*|delta|)`, since
`pi=4 integral_0^1 (1+x^2)^(-1) dx<4`. No numerical value of pi is needed
for this weaker certified bound.

An exact small-offset discriminator is available at every integer `K>=0`.
Choose

$$
\delta=\frac1{2h b^K},\qquad h\ne0.
$$

At time `K` the phases are antipodal, so their chord distance is exactly two.
Their initial real separation tends to zero as `K` grows. If `b` is even,
they become exactly identical at every time `n>=K+1`; if `b` is odd, they
remain exactly antipodal at every time `n>=K`. Both claims follow by reducing
`h b^n delta=b^(n-K)/2` modulo one.

This shows why a generic phrase such as "a tiny seed change grows forever"
is incomplete for the Fourier observer. Real-state distance grows exactly as
`b^n|delta|`; phase distinguishability is controlled by its arithmetic residue.

## 5. Retarded and advanced seed selection have a finite-prefix discriminator

A retarded response uses `U_0=0` and (OQ-1). For any two forcing streams that
agree through index `M`, their retarded responses agree at every `0<=n<=M`.
This is immediate from the finite Green sum (OQ-3), including the empty prefix
`M=0`.

For a finite horizon `H>M`, consider instead the terminal condition `U_H=0`.
Its unique seed is

$$
c_H(r)=-\sum_{k=1}^H b^{-k}r_k.
\tag{OQ-16}
$$

If a future forcing value at `j>M` is changed by `eta!=0`, while all other
values through `H` are retained, then

$$
c_H(r')-c_H(r)=-\eta b^{-j},
$$

and the earlier advanced responses differ by

$$
U_n^{\rm adv}(r')-U_n^{\rm adv}(r)
=-\eta b^{n-j}\quad(0\le n\le M).
\tag{OQ-17}
$$

The same change leaves every earlier retarded response unchanged. This is a
finite exact test of nonanticipation; it does not depend on extrapolating an
infinite experiment.

When `sum b^(-k)|r_k|` converges, the infinite advanced seed is
`c_infinity=-sum b^(-k)r_k`, and the same single-future-pulse calculation
applies. For the authentic source this is the known `-pi/16` seed, which
produces the decaying-tail solution. Unlike `-1` or `-16`, that seed is not an
absolute or relative phase alias of zero.

The future-pulse controls compare different input streams in a **declared class
of causal systems**. They do not claim that the modified stream still obeys
the exact four-pole source passport. If the entire authentic forcing law is
hardcoded in advance, a program can calculate a future-dependent constant;
computability of that constant does not change the nonanticipatory criterion
for a uniform input-response law.

## 6. A rich virtual field does not certify the marked path's cancellation

For every forcing stream, including nonnormal controls, the circle maps

$$
T_n(x)=b x+r_n\pmod1
$$

preserve Haar measure. Indeed, for every nonzero integer `h`,

$$
\int_0^1 e(hT_n(x))\,dx
=e(hr_n)\int_0^1 e(hb x)\,dx=0.
$$

Equivalently, each point has `b` inverse branches of equal Jacobian. At depth
`d`, a uniform virtual inverse-fiber law has `b^d` branches and maximum finite
Shannon entropy `d log b`.

These observations are compatible with retaining a **separate marked seed**
zero. They do not imply that this marked point is typical for the virtual law.
Conditioning on an exactly specified deterministic history and retaining an
unconditioned full-support virtual law are different constructions. This is
the same ensemble/selection boundary already recorded in the parent research.

The source field may therefore be nonempty even when a resource model selects
zero as its unique free actualized seed. What still needs proof is a signed
property of that particular selected history.

## 7. Positive, simpler-forcing controls with an actual zero seed

These are explicitly **changed-source** controls. They refute generic
implications from zero seed, positivity, support, or forcing size; they are not
counterexamples to a theorem retaining (OQ-2) exactly.

For real `d>=0`, put

$$
R_d^*(a)=\frac{16}{(a+d)^2}-\frac1{(a+d+8)^2},\quad a>0,
$$

$$
r_{n,d}^*=R_d^*(8n-7),\qquad
U_{n,d}^*=\frac{16^n}{(d+1)^2}-\frac1{(8n+d+1)^2}.
\tag{OQ-18}
$$

Then `U_(0,d)*=0`, and direct subtraction proves
`U_(n,d)*=16 U_(n-1,d)*+r_(n,d)*`. The forcing is strictly positive and
has the authentic leading asymptotic

$$
r_{n,d}^*\sim\frac{15}{64n^2}.
$$

It also has the strictly positive full-support Laplace kernel

$$
R_d^*(a)=\int_0^\infty e^{-ax}
\,x e^{-dx}(16-e^{-8x})\,dx.
\tag{OQ-19}
$$

The exact factorization is

$$
R_d^*(a)=
\frac{15(a+d+32/5)(a+d+32/3)}{(a+d)^2(a+d+8)^2}.
$$

As in the parent atomic-carrier theorem, its positive Levy numerator can be
grouped as

$$
e^{-dx}\left[(1+e^{-8x})+(1-e^{-32x/5})
 +(e^{-8x}-e^{-32x/3})\right]>0.
$$

Thus positive infinite-divisibility and strict every-order source interactions
do not remove this control either. The parent proof's factorization argument
applies directly; no new stochastic identification of the arithmetic path is
being inferred.

### Control d=3: all integer-frequency phases become coherent

Here

$$
U_{n,3}^*=16^{n-1}-\frac1{(8n+4)^2},
$$

so `e(h U_(n,3)*) -> 1` for every integer `h`. Its Fourier Cesaro averages
therefore converge to one.

If `R` is the authentic source extension, exact polynomial algebra gives

$$
R(a)-R_3^*(a)=
\frac{15a^4+729a^3+9809a^2+50263a+87120}
 {a(a+3)^2(a+4)(a+5)(a+11)^2}>0.
\tag{OQ-20}
$$

Thus this coherent source uses strictly less positive forcing than authentic
at every source time. An unspecified injunction against "gratuitous forcing"
does not independently eliminate it.

### Control d=4: retain odd denominators too

Now

$$
r_{n,4}^*=\frac{16}{(8n-3)^2}-\frac1{(8n+5)^2},\qquad
U_{n,4}^*=\frac{16^n}{25}-\frac1{(8n+5)^2}.
$$

All states and source values have odd reduced denominators. At the fixed
nonzero frequency `h=25`,

$$
e(25U_{n,4}^*)=e\left(-\frac{25}{(8n+5)^2}\right)\longrightarrow1.
\tag{OQ-21}
$$

Moreover `R_d^*(a)` strictly decreases with `d`, since

$$
\partial_dR_d^*(a)=-\frac{32}{(a+d)^3}+
\frac2{(a+d+8)^3}<0.
$$

Hence `0<R_4^*(a)<R_3^*(a)<R(a)` for every `a>0`.

The exact pole locations, their multiplicities, and their signed coefficients
distinguish these controls from the authentic source. Retaining that passport
is necessary. Selection by an unspecified complexity or positivity principle
does not establish the remaining signed estimate for the passported source.

## 8. Scope of information statements and the surviving research edge

The explicit prefix codec and free-preparation theorem of this campaign concern
a declared protocol. They can give zero a unique free preparation and a shorter
code while retaining a nonempty neutral virtual fiber. Relabeling a valid
prefix code can instead make `-1` shorter than zero; that fact refutes a
universal code-independent ranking, not the declared relative protocol. An
empty codeword cannot coexist with another word in a prefix-free code; a
default/no-message protocol must account for its framing separately.

Likewise, a zero-cost operation that moves the actualized neutral seed is a
counterexample to the free-preparation hypothesis, not an allowed hidden
bootstrap. The independent oracle checks these explicit failure cases alongside
the arithmetic quotients.

The new constructive boundary can select and preserve `U_0=0` without erasing
the virtual carrier. The observation quotient then states exactly which of
those preparation distinctions survive into the Fourier data. It does not
imply

$$
\sum_{n\le N}e(hU_n(0))=o(N)
\quad\text{for every fixed }h\ne0.
$$

That source-selected temporal cancellation remains the next genuinely missing
arithmetic edge. Integer seed controls do not test it, because they are exact
phase aliases. The advanced seed and the explicitly changed coherent sources
test different hypotheses and must keep those types visible.

### Local claim ledger

| Claim | Status | Domain and limitation | Next falsification opportunity |
|---|---|---|---|
| Full real state recovers the seed | PROVED LOCAL (paper) | exact state and known forcing prefix | finite-precision observation needs an error model |
| OQ-A/B absolute phase quotient | PROVED LOCAL (paper) | fixed forcing, integer base and frequency, stated start | wrong source or clock shift |
| OQ-C relative-phase quotient | PROVED LOCAL (paper) | literal pairwise phases, not only spectral data | omit the factor b-1 or confuse constant rotation with equality |
| Quantitative chord bound and exact antipodal controls | PROVED LOCAL (paper) | arbitrary real seeds; bound is sufficient, not a detection equivalence | tiny exact dyadic offset with delayed aliasing |
| Retarded versus advanced finite-prefix discrimination | PROVED LOCAL (paper) | a uniform class of input streams | hidden future dependence in preparation |
| Haar virtual law plus marked seed does not ensure typicality | PROVED LOCAL (paper) limitation | virtual distribution and marked point remain distinct | source-specific realization theorem |
| Zero seed plus positive full-support source forces cancellation | REFUTED | receipts (OQ-18)--(OQ-21); source deliberately changed | exact authentic-source argument |
| Authentic signed BBP cancellation, pi normality | OPEN | no new estimate supplied by this dossier | source- and zero-boundary-dependent signed bound |
