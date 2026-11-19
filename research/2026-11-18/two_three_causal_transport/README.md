# The moving causal frame: BBP, 2-adic/3-adic transport, and the 15/16 boundary

**2026-11-18. Research branch; original source and literal zero seed retained.**

The principal result is a precise boundary-sensitive calculation. The authentic
BBP numerator factors as

```math
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),
\quad H(t)=(t^2+2)(t^2+2t+2),
```

and, with `K(t)=(2-t^2)(t^2-2t+2)`,

```math
H(t)K(t)=16-t^8.
```

For an eight-channel cyclic shift `S_8`, this gives
`H(S_8)K(S_8)=15I`. For an eight-entry causal backshift `L_8` with zero
prehistory, it gives `H(L_8)K(L_8)=16I`. The associated determinants are
`15^4` and `16^4`. This is an exact connection between the radix `16=2^4`
and `15=3*5`: closing a record changes the local arithmetic of its inverse.
The finite channel operator is not silently identified with the time evolution
of the actual BBP orbit. In the Mellin representation, one BBP time step is
eight exponent steps; the factor `t^8` respects that distinction.

The complete family is stronger. For every block count `k>=1`, the four
nonunit Smith factors of `H(S_(8k))` are all `16^k-1`; those of `H(L_(8k))`
are all `16^k`. All remaining factors are one. Equivalently,

```math
\operatorname{coker}H(S_{8k})\cong
  (\mathbb Z/(16^k-1)\mathbb Z)^4
  \cong\operatorname{Fix}(T_{16}^k)^4,
\qquad
\operatorname{coker}H(L_{8k})\cong
  (\mathbb Z/16^k\mathbb Z)^4.
```

The second identification uses the declared coefficient basis and
`a -> a/(16^k-1) mod1`. This is an exact connection to the virtual periodic
reference grid. It is not a bound on how closely the selected pi orbit can
shadow that grid.

The full signed source polynomial is retained as well. Writing `D=16^k-1`,

```math
\operatorname{coker}Q(S_{8k})
\cong\mathbb Z\oplus\mathbb Z/(D/15)\mathbb Z
\oplus(\mathbb Z/D\mathbb Z)^3.
```

Its free coordinate is the retained coefficient sum. For the causal source
filter, `I-L` is an integer-unimodular matrix, so `Q(L_(8k))` has the same
four obstruction factors `16^k` as H. Factoring Q has therefore not discarded
its difference operator or its constant channel.

This gives a mathematical version of Leah's moving-observer concern. An
observer advances through a causal record. Reconstructing missing information
requires a retained state, a valid internal model, or later observations. A
cyclic closure supplies a different boundary condition. It is a real change
in the mathematical object and can reverse which primes obstruct inversion.

## The recovered Fibonacci source bridge

The saved five-frame construction uses two-component Fibonacci states and
three quadratic observations per frame. It is not the same object as the
paired cyclic clocks above. With its exact inverse state map
`M=A^-1=[[0,1],[1,-1]]`, reducing the literal source polynomials gives

```math
H(M)=8I+M,\qquad K(M)=3M,\qquad Q(M)=7I-6M.
```

Since M is integer-unimodular, `K(M)` contracts every ternary vector by
exactly `1/3`. The literal Q and positive H are instead ternary isometries,
with determinant `55=F_10=5*11`. Their defects occur at five and eleven.
On the pentagonal zero-sum space, index doubling intertwines the source Gram
operator with this same Q evaluated at the Fibonacci quadratic algebra.
This is an exact operator connection. Its transfer to the selected BBP real
phase still requires a source-faithful coupling; a product with a locked
circle supplies the explicit negative control.

## Results and exact scope

| Result | Earned status | Boundary |
|---|---|---|
| All-size determinant of `H(S_m)` and its 2-adic isometry | PROVED | Declared cyclic channel space |
| Sharp three-/five-channel inverse losses at primes 3 and 5; extra prime 11 | PROVED | Finite linear observer, not a distribution law |
| Eight-channel cyclic inverse denominator 15 versus causal denominator 16 | PROVED | Boundary-conditioned filter; no physical time reversal |
| Causal inverse loses exactly `4n` binary precision bits at record length `8n` | PROVED | Maximum operator norm of `H(L_(8n))^-1` |
| All-block cyclic obstruction group is four copies of the radix-16 periodic grid | PROVED | Exact finite-group identification; no shadowing estimate |
| Full signed Q-filter has one free constant coordinate and explicit finite torsion | PROVED | Keeps the literal `(1-t)H` source factor |
| BBP recent-window error shrinks 2-adically but retains the omitted 3-adic boundary | PROVED | Literal source; inherited height theorem rederived |
| Collatz ternary residue is determined by the last ordered binary valuation symbols, with sharp depth | PROVED / classical affine interface | Positive odd Syracuse map and a specified finite word |
| Rational source snapshots have autonomous period greater than `4n/27` | PROVED / inherited arithmetic corollary | Unforced snapshot orbit; exact periods do not control close shadows |
| Paired cycle determinants for `(2,3)`, `(2,5)`, `(3,5)` | PROVED | Explicit CRT successor construction, distinct from the recovered quadratic Fibonacci lift |
| Paired cycle Smith forms | VERIFIED_FINITE | Exact integer calculations at sizes 6, 10, 15 |
| Fibonacci complementary filter is exactly `3A^-1`; Q/H are ternary isometries | PROVED | Declared Fibonacci module; no BBP orbit conjugacy |
| Pentagon Gram and signed Fibonacci source operator are intertwined | PROVED | Zero-sum channels; constant Gram channel 225 retained separately |
| Two-state/three-frame/five-readout quartic candidate | PROVED construction | Explicit new readout choice, not a permutation of the prior quadratic lift |
| R0, base-16 normality of pi, universal Collatz descent, completed Weil positivity/RH | OPEN | No new all-shell signed estimate |

The source's pentagonal determinant is exactly `15*F_10=825`; its
nonconstant factor is `55=5*11`. Thus the Fibonacci identity has a concrete
arithmetic interpretation, while prime 11 prevents a closed `{2,3,5}`
inventory. The paired `(2,3)` six-channel filter likewise includes prime 13.

## Read in this order

1. [Cyclic and causal source filters](CYCLIC_SOURCE_FILTERS.md): full algebra,
   inverse precision, the Fibonacci factor, and the retained closure residual.
2. [BBP causal memory](BBP_CAUSAL_MEMORY.md): exact window theorem and compact
   proof of the inherited ternary denominator law.
3. [Fibonacci source transport](FIBONACCI_SOURCE_TRANSPORT.md): the recovered
   two-state/five-frame/three-observation construction and the new exact
   complementary identity `K(A^-1)=3A^-1`.
4. [Collatz interface](COLLATZ_INTERFACE.md): legal positive-integer cylinders,
   ordered memory, product formula, and primary literature.
5. [Hole contract and next probe](HOLE_CONTRACT.md): the actual missing signed
   estimate, ranked alternatives, and refutation receipts.
6. [Source audit](SOURCE_AUDIT.md), [claim ledger](CLAIM_LEDGER.json),
   [hostile review](HOSTILE_REVIEW.md), and [validation](VALIDATION.md).

## What was recovered rather than discovered

Main XXVI is pinned at `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.
The existing October 24 joint-prime dossier already reconstructs the real
rational phase from synchronized odd-prime components. The October 31
two/three carrier already proves joint local time Haar and its failure to
imply a selected real Haar law. The November 4 ternary-height theorem already
controls the genuine accumulated state. These are explicitly reused.

The factor `16-t^8` also belongs to the inherited source/gauge module. The
new project contribution is the exact comparison of its cyclic and finite
causal realizations, the sharp local inverse cost, and the resulting
source-typed comparison with BBP and Collatz memory, and the exact
complementary-filter reduction `K(A^-1)=3A^-1`. No academic priority
claim is made.

The latest inspected donor endpoints are draft #663 at
`74b9f4806fdfebca4be66e2c5bfdbd9b5fc2273a`, #664 at
`2f0b160c52c5a2126dc8b783c8368127874ddb13`, and #665 at
`4e6e38d1578cc7a1425728964b6911c17e7ba17d`. Their source-null,
terminal-norm, prime-survival and memory-neutrality boundaries are retained;
their commits are not merged into this additive branch.

## Reproduce

```sh
PYTHONPATH=. python research/2026-11-18/two_three_causal_transport/probe.py
PYTHONPATH=. python -m unittest tests.test_bbp_two_three_causal_transport -v
PYTHONPATH=. python research/2026-11-18/two_three_causal_transport/independent_local_audit.py
```

The final command is a larger exact finite audit. Every numerical range is
a finite certificate. The paper proofs supply their own all-time quantifiers.

## Dominance and remaining boundary

For these declared filters and source windows, retaining the causal boundary
dominates bare cyclic closure: it recovers the valid cyclic calculations,
exhibits the missing record, and predicts a different, verified local inverse
cost. It also rejects the inference that excellent 2-adic reconstruction is
automatically excellent 3-adic reconstruction.

This advances the observer/transport architecture. It does not establish that
the original real phases have a positive anti-lock margin on every late shell.
That source-selected signed inequality remains the decisive next theorem.
