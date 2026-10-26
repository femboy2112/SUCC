# Mobius/Gamma boundary audit: what a twist preserves, and what it cannot select

Date: 2026-10-25. Parent `eca4462ee4d62642b15c4af672136aa5bcacd00b`
(PR #297). The newer sibling PR #298 at
`dc6b87d3b8790f507d2447cc1a24f0ab0d15104f` was read without merging it.
This note supplies paper proofs and inherited counterexample provenance.
No numerical experiment is promoted to an infinite theorem. Academic novelty
is unverified; the classical identities are explicitly attributed.

## 1. Faithful proposal and the domains that must survive the translation

The useful interpretation of the proposed twist is a boundary identification
with an explicit transport law. The initial zero, the zero of the bounded
future solution, and a renormalized zero are different boundary data until
their transition maps have been specified. Three distinct constructions are
available:

1. A Mobius strip reverses a real transverse fiber at its seam. Its centered
   sign flip preserves fiber zero; it does not exchange zero and infinity.
2. A fractional-linear Mobius transformation such as `J(y)=1/y` exchanges
   projective zero and infinity. This is a coordinate transformation, not
   automatically a quotient of a dynamical system.
3. A sign-twisted successor sum weights its successive terms by `(-1)^n`.
   Its Gamma/digamma identities concern those source sums. Additional work
   is required to identify them with the phases `e(h U_n)` of the BBP orbit.

The companion notes construct precise versions of all three. This audit
tests claims that their compatibility already supplies digit cancellation.

## 2. Finite reversed endpoints do not produce a global cyclic source

Let `r(n)>0` be the authentic four-pole source and
`X_n=16 X_(n-1)+r(n)`. Suppose, for an integer `N>=1`, a global extension
satisfied `X_(n+N)=-X_n` for every `n>=0`. Then for every `n>=1`,

$$
r(n+N)=X_{n+N}-16X_{n+N-1}
=-X_n+16X_{n-1}=-r(n).
$$

This contradicts strict positivity. Thus a **global antiperiodic extension
with unchanged source** is REFUTED. The finite condition `X_N=-X_0` remains
consistent for its separately selected initial value. It does not assert
the extension above, and this argument does not refute that finite problem.

The ordinary periodic condition has a similar source-compatibility issue:
a global extension `X_(n+N)=X_n` requires `r(n+N)=r(n)`, whereas the authentic
source is strictly decreasing. A valid geometric construction can retain
the nonperiodic source as additional data, but may not discard this condition.

## 3. Seed-preserving equivariance fixes a deterministic trajectory

**PROVED PAPER, elementary general theorem.** Let `F_n:S_n->S_(n+1)` be
any deterministic maps, and let `u_(n+1)=F_n(u_n)` be their trajectory
from a specified `u_0`. Suppose arbitrary self-maps `H_n:S_n->S_n` satisfy

$$
H_{n+1}\circ F_n=F_n\circ H_n,\qquad H_0(u_0)=u_0.
\tag{A-0}
$$

Then `H_n(u_n)=u_n` for every `n>=0`. No linearity, continuity, injectivity
or invertibility hypothesis is needed. **Proof:** the assertion holds at
zero by hypothesis; if it holds at n, then
`H_(n+1)(u_(n+1))=H_(n+1)(F_n(u_n))=F_n(H_n(u_n))=F_n(u_n)=u_(n+1)`.
Induction proves the claim. QED.

Thus replacing an affine twist by a nonlinear one does not escape the
pointwise-fix conclusion while time-preserving equivariance and the
selected seed are retained.

### Complete classification for the unwrapped BBP flow

Put `F_n(x)=16x+r(n+1)` on the **unwrapped real line**, `U_0=0`, and
`U_(n+1)=F_n(U_n)`. The map from initial states to time n is the bijection

$$
P_n(x)=U_n+16^n x,\qquad P_n^{-1}(x)=\frac{x-U_n}{16^n}.
$$

Every family of arbitrary real self-maps commuting with this time-dependent
source is exactly of the form

$$
\boxed{H_n=P_n\circ H_0\circ P_n^{-1}.}
\tag{A-0b}
$$

**Proof:** iterated equivariance gives `H_n P_n=P_n H_0`, which implies
A-0b since P_n is bijective. Conversely `F_n=P_(n+1) P_n^(-1)` proves
equivariance for the displayed family. QED. This full classification uses
the invertibility of the unwrapped flow; it is not asserted for the
16-to-1 circle map. The general pointwise-fix theorem A-0 still applies
to deterministic circle trajectories.

### Affine corollary and the literal sign flip

For each `n>=0` let `H_n(x)=a_n x+b_n` be a real affine map. The identity

$$
H_{n+1}(F_n(x))=F_n(H_n(x))\qquad\text{for every real }x
\tag{A-1}
$$

holds at every time if and only if there are constants `a,b_0` such that

$$
a_n=a,\qquad b_n=(1-a)U_n+16^n b_0.
\tag{A-2}
$$

**Proof.** Compare coefficients of `x` in A-1 to get
`16a_(n+1)=16a_n`. The constant terms give
`b_(n+1)=16b_n+(1-a)r(n+1)`. Iterating this inhomogeneous recurrence
gives A-2. Conversely substitution establishes A-1. QED.

If the maps preserve the selected initial zero, `H_0(0)=0`, then `b_0=0`
and consequently

$$
\boxed{H_n(U_n)=U_n\quad\text{for every }n.}
\tag{A-3}
$$

In particular the nontrivial affine involution is `H_n(x)=2U_n-x`;
it reverses the fiber but fixes the authentic trajectory pointwise. The
general theorem does not forbid time-mixing operators, time reversal with
additional source data, transforms that are not state self-maps satisfying
A-0, or new estimates. It says precisely that **any** source-commuting,
time-preserving state map fixing the selected origin cannot pair
**distinct** authentic observations. Nonlinearity by itself is no escape.

The tempting reflection around the midpoint of the authentic solution and
the bounded solution does exchange them. Its initial reflection sends
`0` to `-pi/16`, so it fails the same initialization condition explicitly.

## 4. Reversal is not descent, and conjugation is not cancellation

With the authentic Green tail, `y_n=X_n+T_n` obeys `F(y)=16y`.
The projective inversion `J(y)=1/y` satisfies

$$
JFJ=F^{-1}.
$$

Thus it is a legitimate reversing symmetry. But `F` does not descend to
the naive quotient `y~1/y`: for instance `2~1/2`, while `F(2)=32` and
`F(1/2)=8` are not equivalent under this relation. The latter equivalence
class is `{8,1/8}`, neither of which equals `32`. This is an exact rational
counterexample to quotient descent, not a claim that all projective or
dihedral constructions fail.

On the real circle, `e(x)=exp(2 pi i x)` satisfies

$$
e(hx)+e(-hx)=2\cos(2\pi h x).
$$

A reversed orientation pairs complex conjugates, which need not cancel.
Even a half-circle translation cancels only odd frequencies: it multiplies
the h-th character by `(-1)^h`. Normality requires the relevant signed
average to vanish for **every** fixed nonzero integer frequency.

## 5. The entire exact BBP source and its Gamma identities still need a seed

The inherited [MP-01 gauge theorem](../2026-10-24/BBP_MINIMAL_PATH_GAUGE_AND_MISSING_PRIME.md)
is the strongest direct adversary to a source-only Gamma shortcut. For
every real `beta`,

$$
X_n^{(\beta)}=16^n\beta-T_n
$$

obeys the original four-pole forcing at every time. Its initial value is
`beta-alpha`, with `alpha=T_0=pi/16`. Choose any period-L seed
`beta=k/(16^L-1)` and set `h=16^L-1`. Then `h16^n beta` is an integer,
so

$$
e(hX_n^{(\beta)})=e(-hT_n)\longrightarrow1,
\qquad
\frac1N\sum_{n=1}^N e(hX_n^{(\beta)})\longrightarrow1.
\tag{A-4}
$$

All source-only Gamma primitives, balanced digamma identities, exact source
pole data and source-tail asymptotic coefficients are unchanged. The failed
gate is precisely the authentic initial value: this trajectory has
`X_0=beta-pi/16`, not zero. A source-only theorem therefore cannot prove
normality uniformly over these seeds. This does not refute normality of the
authentic `U_0=0` solution.

The rational controls in PR #297 are a different quantifier regime: a
different rational initial value is chosen for each finite prime window,
and the resulting modulus deficit has order `m^-4`. They must not be
described as a single rational nonnormal initial state across all windows.

The [newer sibling PR #298](https://github.com/femboy2112/SUCC/pull/298)
adds a different obstruction: for every prescribed finite prefix and finite
endpoint-jet order, one changed positive rational source matches them,
retains all strict Hausdorff signs and odd denominators, yet has a rational
selected seed and is nonnormal. Its exact global four-pole law fails. This
reinforces the need for the full source and initialization jointly; it
does not weaken the exact same-forcing statement A-4.

## 6. Gamma recurrence plus reflection does not fix Euler's constant

The periodic-gauge construction and its failure of log convexity are
**inherited**, not new: see FGF-6 of
[the factorial Gamma dossier](../2026-10-16/FACTORIAL_GAMMA_FUCC_SUCC.md).
We record its reflection and finite-jet consequences for this proposal.

For a nonzero real parameter `epsilon`, define

$$
F_\epsilon(z)=\Gamma(z)\exp(\epsilon\sin(2\pi z)).
\tag{A-5}
$$

The extra factor is entire, nowhere zero, 1-periodic, positive on the
positive real axis, and equal to one at every integer. Consequently this
family preserves all of the following:

- the exact recurrence `F(z+1)=zF(z)` and normalization `F(1)=1`;
- every positive-integer factorial value;
- all Gamma pole positions and residues, and the absence of zeros;
- the reflection identity `F(z)F(1-z)=pi/sin(pi z)`;
- the modulus of Gamma on every vertical line through an integer, away
  from poles.

Reflection follows because `sin(2 pi(1-z))=-sin(2 pi z)`. On `z=n+it`,
the sine is `i sinh(2 pi t)`, so the added exponential has modulus one.
Nevertheless,

$$
\frac{F_\epsilon'(1)}{F_\epsilon(1)}=-\gamma+2\pi\epsilon.
\tag{A-6}
$$

Thus these recurrence, reflection and positivity conditions do not select
the canonical Euler-constant jet. This does **not** change the value of
Euler's constant: the function has been changed from the standard Gamma
function, and that change is explicitly visible in the logarithmic derivative.

The decisive failed canonical hypothesis is log convexity. For real `x>0`,

$$
(\log F_\epsilon)''(x)=\psi'(x)-4\pi^2\epsilon\sin(2\pi x).
$$

The trigamma series gives
`0<psi'(x)<=1/x^2+1/x`, hence it tends to zero. At the arbitrarily large
points where the sine has the sign of epsilon and absolute value one,
the displayed second derivative is eventually negative.
Bohr--Mollerup therefore excludes this family when **global log convexity**
is imposed along with recurrence, positivity and normalization.

### Arbitrarily many integer jets can also survive a false Gamma choice

For any odd integer `q>=1`, replace the exponent in A-5 by
`epsilon sin(2 pi z)^q`. Recurrence, reflection, integer values, poles,
residues, real positivity and the same integer-vertical-line moduli still
hold. At each positive integer `n`,

$$
F_{\epsilon,q}(z)-\Gamma(z)=O((z-n)^q).
$$

Therefore for every specified finite derivative order `K`, choosing an odd
`q>K` makes **all** positive-integer jets through order K agree exactly.
The functions remain different. They still fail global log convexity:
the nonconstant smooth periodic function `epsilon sin(2 pi x)^q` has a
second derivative negative at some point, repeated arbitrarily far out,
while `psi'(x)` tends to zero. This is a finite-order, not an all-orders,
jet claim.

These elementary extensions sharpen the relevance of inherited FGF-6.
They are not a new characterization theorem for Gamma and make no
scholarly priority claim.

## 7. Where Euler gamma genuinely appears, and where balance erases it

The source's four ray coefficients are `(4,-2,-1,-1)`, whose sum is zero.
Consequently the common `-gamma` term cancels from their balanced digamma
combination. This is already proved in section 5 of
[the Euler--Mascheroni BBP regulator dossier](../2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md).
The primitive Gamma product may retain a normalization constant involving
gamma; its balanced derivative or successor quotient can erase that scalar.
These are different observables, not contradictory evaluations.

Likewise, a declared reference shift `H_N-log N-c` tends to `gamma-c`.
Choosing `c=gamma` makes that coordinate zero and stores the conversion
constant in the reference. A positive multiplicative rescaling of a finite
nonzero number cannot do this; the operation is a subtraction of origins.
Both the old and new conventions must be transported through any claimed
source identity.

## 8. Surviving bridge and falsification requirements

The general equivariance theorem makes the next dependency cut explicit:
a source-authenticated twist that pairs distinct orbit observations must
mix times or leave the class of time-preserving state maps satisfying A-0.
Simply using a nonlinear state map does not suffice. A useful observable
or operator must retain both the exact forcing and the selected initial
state; source-only Gamma spectra or seam denominators do not meet that
condition. This is a limitation of the proposed pairing mechanism, not a
claim that such equivariances can never help establish another theorem.

A candidate should be tested against these separate controls:

| Candidate claim | Decisive control or remaining obligation |
|---|---|
| A finite sign seam makes the source cyclic | Global extension forces a negative future source |
| Reciprocal coordinate equivalence supports forward dynamics | `2~1/2` but `32` is not equivalent to `8` |
| A time-preserving source-commuting state map fixing the seed pairs distinct authentic phases | General induction A-0 forces pointwise fixation, including nonlinear maps |
| Gamma recurrence/reflection select the canonical Euler jet | A-5 preserves them and changes the jet |
| Any finite collection of Gamma integer jets repairs uniqueness | Odd-power gauge preserves any prescribed finite order |
| Full source-only Gamma information implies BBP cancellation | Periodic-seed same-forcing family A-4 |
| Endpoint jets and positive moments imply selected cancellation | Existing PR #298 simultaneous matched-source controls |
| Canonical Gamma selection itself proves source-orbit genericity | No implication supplied; the signed orbit estimate remains OPEN |

PR #298 leaves a particularly explicit sufficient target: a signed
conductor-flat Fejer innovation estimate after removing conductor births.
The current round does not prove that estimate or merge its implementation.
Alternatively, a new Gamma identity could yield a genuine bound on
authentic cross-time character correlations. Writing those correlations
in Gamma notation without estimating them is a reformulation, not a proof
step. The missing inequality is a pathway gap, not an independence result
or evidence that new axioms are required.

## Primary classical references checked

- [NIST DLMF 5.5.1--5.5.4](https://dlmf.nist.gov/5.5): Gamma/digamma
  recurrence and reflection, with the stated pole exclusions.
- [NIST DLMF 5.5(iv)](https://dlmf.nist.gov/5.5.iv): the positive-real
  Bohr--Mollerup characterization, including normalization and log convexity.
- [NIST DLMF 5.7.4](https://dlmf.nist.gov/5.7.E4): `psi(1)=-gamma`.
- [NIST DLMF 5.15.1](https://dlmf.nist.gov/5.15.E1): trigamma series used
  for its vanishing large-x bound.
- [NIST DLMF 5.2](https://dlmf.nist.gov/5.2): Gamma poles/residues,
  logarithmic derivative, and the standard Euler-constant definition.

The web checks establish the classical premises. The general equivariance
theorem, invertible-flow and affine classifications, reflection-gauge
consequences and source counterexample deductions above have explicit
algebraic proofs. Same-model agent agreement is not an additional independent
theorem authority.
