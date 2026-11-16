# Separate derivation audit of the phase and target dossier

**Date:** 2026-11-12. **Scope:** `PHASE_AND_TARGET.md` and
`phase_filters.py`, with inspection of the focused tests. This is a
separate same-model/decomposition audit, not an external mathematical
referee, a formal proof check, or independent-source corroboration.

Audited byte snapshots before the author's response to these findings:

| File | SHA-256 |
|---|---|
| `PHASE_AND_TARGET.md` | `1e2bf96017be632af7449833ef39a1235f00a2089411c8eec5ce1ec04146bf32` |
| `phase_filters.py` | `2c11e83c1601bc644f102119a0849683b2b81da83007818f67787dc3bc665241` |

## Verdict

**No mathematical blocker found in PT-01–PT-07 within their stated
finite domains.** The factor two in the ambiguity diameter, the separate
approximation/noise constants, the support-group characterization, the
Z/6 positive alias, and the Z/3 conditioning obstruction all survive
direct derivation. The distinction between phase-sensitive additive
targets and power-decay normality targets is correct and necessary.

One additional exact control sharpens the support discussion: full
rational relation rank can conceal extra finite torsion. An explicit
Z/21 example below realizes precisely that failure. A small interface
clarification about float inputs is recommended; it does not invalidate
the algebra performed on the resulting rational values.

## 1. Target completeness and the diameter constant

The row-span criterion is sound under its **universal probability-law**
quantifier. If `t` is outside the row span, choose `z in ker F` with
`t.z!=0`. The mass row forces `sum z=0`, so its nonzero positive and
negative parts normalize to probability laws with the same boundary.
For a fixed observed fiber, positivity can supply additional information;
the dossier already states that exception correctly.

For the diameter, every probability difference has l1 norm at most two,
so the upper bound is `2 dist_infinity(t,V)`. Conversely, a norming
functional of the quotient by `V` can be represented by a vector `z`
with `z annihilates V`, `||z||_1=1`, and `z.t=dist_infinity(t,V)`.
The supplied active-coordinate separation argument constructs just such
a vector: its coordinates have distinct supports and prescribed signs,
so its l1 norm is exactly the sum of the convex weights, namely one.
The mass row then makes the positive and negative masses exactly 1/2.
Thus `p=2z_+`, `q=2z_-` are probabilities and attain twice the distance.
There is no missing factor or normalization.

For the four-atom control, the filters reveal the masses of two cells
`{0,1}` and `{2,3}`. Each cell contains target values zero and one,
so every cellwise constant approximation has uniform error at least 1/2;
the constant 1/2 attains it. Point masses at atoms one and zero share
the filter data and have target difference one. Direct checking of the
implementation returned precisely those two laws.

## 2. Robust dual constants

Writing `r=t-F^T c` gives, for a probability vector `p`,

`t.p-c.y = r.p + c.(Fp-y)`.

The first term is bounded by `||r||_infinity`, not twice that norm;
there is only one probability law here. The second is bounded by
`sum_j |c_j| epsilon_j`. This verifies both PT-03 constants. A
one-sided pointwise minorant gives the stated one-sided expectation
bound by the same calculation. Large coefficients really do amplify
measurement uncertainty even when the span residual vanishes.

For the concrete signed weights `(-1,3)`, readings `(1,51/100)` and
errors `(0,1/100)`, direct checking gives center `53/100`, radius
`3/100`, and coefficient l1 norm four. The document correctly makes
source/measurement authentication an assumption rather than an output
of the algebraic verifier.

## 3. Fourier support: characters, torsion, and rank

For nonzero supported Fourier coefficients let `z_h=b_h/a_h`.
Equal powers force `|z_h|=1`. Equal bispectra at each supported triangle
force `z_h z_k=z_(h+k)`. These are exactly the characters of the
presented abelian group `U(S)`. Translation characters factor through
the natural surjection `sigma:U(S)-><S>` in Z/q.

If `ker sigma=0`, the groups agree and every compatible phase assignment
is translational, using extension of a character of a cyclic subgroup.
If the kernel has a nonzero element, characters of a finitely generated
abelian group separate it. Such a character gives compatible phases
that do not factor through sigma, hence an actual nontranslation complex
signal with the same support, powers and bispectrum. This proves the
stated iff **for arbitrary complex signals on that support**. Real and
nonnegative restrictions are additional, as the dossier acknowledges.

Full Fourier support yields the character law on all of Z/q directly;
`z_0=1`, `z_h=z_1^h`, and `z_1^q=1`. The anchoring claims are then
correct. A nonzero coefficient at frequency h leaves exactly
`gcd(h,q)` possible shift parameters; a mass anchor does not fix shift.

### New explicit extra-torsion control

Take

`q=21`, `S={0,1,2,4,8,11,16}`.

Apart from triangles involving zero, the only supported additive
triangles are

`1+1=2`, `2+2=4`, `4+4=8`, `8+8=16`, `16+16=11`, `11+11=1`

with sums understood modulo 21. Therefore `e_0=0`, every generator is
a power-of-two multiple of `e_1`, and the final relation is
`64 e_1=e_1`. Consequently

`U(S)=Z/63`, `<S>=Z/21`, and `ker sigma=Z/3`.

The relation matrix has full rational rank seven. A separate integer
Smith-normal-form calculation gave diagonal
`(1,1,1,1,1,1,63)`; the existing rank function returned seven. Thus
full rank would be a false completeness certificate here. The existing
function's warning is substantively justified, not merely cautious.

For an explicit nontranslation phase assignment, let
`z_1=exp(2 pi i/63)` and propagate by the displayed doubling cycle.
All supported triangle constraints hold, but `z_1^21!=1`, so this
assignment cannot arise from a shift on Z/21. This example concerns
complex signals; no positivity claim is made for it.

**Recommendation:** retain this example as a regression control if
the support diagnostic is later upgraded from rational rank to a full
integer/group certificate. Do not infer completeness from rank alone.

## 4. Direct audit of the Z/6 positive alias

The given formulas evaluate to the displayed integer vectors:

`f_x=14+14 cos(pi x/3)`;

`g_x=14+2 cos(pi x/3)-8 sqrt(3) sin(pi x/3)`.

Under the stated negative-exponent DFT, their supports are `{0,1,5}`.
The nonzero coefficients are

`a_0=b_0=84`, `a_1=a_5=42`,

`b_1=6+24 i sqrt(3)`, `b_5=6-24 i sqrt(3)`.

The magnitudes agree because `6^2+(24 sqrt(3))^2=42^2`.
All supported triangles either contain zero or pair frequencies one
and minus one. Hence the extra phase cancels in every bispectrum entry.
The first vector has a zero entry and the second none, excluding every
translation without any numerical phase reconstruction.

A separate implementation formed the correlation tables by summing
over all indexed pairs/triples and grouping their differences, rather
than calling the implementation's shifted-index routines. It returned
the pair table `(1764,1470,882,588,882,1470)` for both signals and
identical full third tables. This reproduces the finite alias exactly.

## 5. Direct audit of the Z/3 inverse-conditioning obstruction

For `u=(14,-7,-7)` and `v=(2,11,-13)`, direct arithmetic gives the
common pair table `(294,-147,-147)` and both third tables printed in
PT-07. The l1 distances between `u` and the three translates of `v`
are `36,54,18`. The largest entrywise third-table difference is `3078`.

The nonzero DFT coefficients at frequency one are `21` for u and
`3-12 i sqrt(3)` for v, both of magnitude 21; their conjugates occur at
frequency two. Consequently every positive epsilon gives full Fourier
support for the probability perturbations. The declared upper bound
epsilon<=1/100 ensures strict positivity, since the worst coordinate
is `1/3-13 epsilon>0`.

Expansion around the constant law eliminates the linear term by zero
mean, and the equal pair tables eliminate the quadratic difference.
Thus the observation separation is exactly cubic while the quotient
signal distance is exactly linear. Direct rational evaluation at
epsilon `1/100`, `1/257`, and `1/1009` reproduced
`3078 epsilon^3`; the last two scales were separately chosen checks,
not a basis for the universal claim.

An inverse estimate with exponent alpha>1/3 would require
`18 epsilon <= C (3078 epsilon^3)^alpha` at arbitrarily small epsilon,
which is impossible. The finite Fourier transform changes norms only
by fixed constants, so the exponent obstruction transfers to bispectrum
coordinates. This proves an **upper obstruction on possible uniform
inverse exponents**. It does not prove that an exponent exactly 1/3
is achievable for all nearby signals; avoid reading the heading's word
"sharp" as such an existence theorem.

## 6. Normality can still be proved from power decay

The final qualification is correct. For every fixed nonzero frequency,
`|W_(A,h)|^2 -> 0` implies `|W_(A,h)| -> 0`, hence `W_(A,h)->0`.
No phase reconstruction is needed for this conclusion. Full power
data can therefore be sufficient for a vanishing-magnitude target
while remaining insufficient for an additive representation coefficient.

The shell-to-prefix passage also holds with the stated all-large-A
quantifier: split a prefix into successively halved terminal shells;
each large shell contributes at most its length times a common small
Fourier bound, while the fixed initial segment and rounding endpoints
have negligible normalized contribution. Thus all fixed Fourier modes
vanish for the empirical prefixes. The usual radix-orbit criterion
then gives base-16 normality. A claim only on isolated sampled shell
sizes would not supply this passage.

For R0, `mu_A(1-cos(2 pi x))=1-Re W_(A,1)`. Its positive lower limit
is exactly a real-part saving from one. It must not be promoted to
all-mode magnitude cancellation. The coherent changed seed has completed
orbit zero, so source-blind constraints valid for that seed cannot
certify the required positive margin. These scopes are retained correctly.

## 7. Implementation observations and limits

The exact RREF/span/nullspace logic matches PT-01. The cyclotomic
implementation uses rational signals; the complex-signal theorem is a
paper result with a broader domain than this implementation. The signed
correlation conventions used by the executable tests are correct for
its real rational inputs.

**Minor recommendation:** `_rows`, `dot`, and related routines call
`Fraction(x)` directly, so they accept binary floats and interpret their
exact binary rational values. This does not spoil the ensuing exact
arithmetic, but it is weaker than a rational-input-only contract. Either
reject floats/bools explicitly or document that input conversion is
not a certificate that an intended decimal measurement was exact.

This audit did not run the repository's full suite or claim its status.
It used direct proof review, a separate exact correlation calculation,
manual Fourier coefficient derivations, a finite integer Smith calculation,
and a few explicit implementation checks. No other dossier files were
edited by the auditor.
