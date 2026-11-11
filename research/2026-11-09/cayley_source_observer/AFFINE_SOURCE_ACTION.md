# A faithful affine action on the indexed rational BBP source

**Status: PROVED PAPER; exact finite calibration.** This constructs an action
of the positive affine monoid on the infinite carrier `N0 × Q`. It fills the
source-clock part of the operator-conflation gap. It does not construct a
genuine C-monoid, identify rational-state multiplication with clock dilation,
or supply a faithful lambda compiler or a signed arithmetic estimate.

**Provenance and novelty:** the affine monoid and chronological source functor
already appear separately in the preserved
[causal-shadow dossier, sections 3–4](../scott_omega_causal_weld/session_archive/SUCC_C_MONOID_CAUSAL_SHADOWS_LOCAL.md).
The source cocycle is also ASG-01 in
[scale/adelic gluing](../../2026-11-08/scale_adelic_thermal_gluing/PROOFS.md), and
the finite seed gauge is OSF-01 in
[origin-locked spectral fingerprints](../../2026-11-08/origin_locked_spectral_fingerprint/THEOREMS.md).
The contribution here is their explicit coherent integration and its boundary
under observation. No novelty claim is made for conjugating an action.

## CS-03a. The exact source-clock representation

Keep the original four-pole forcing, and put

```math
P_0=0,\qquad P_n=\sum_{j=1}^n16^{-j}r(j),\qquad
J(n,u)=(n,16^{-n}u-P_n).
```

The map J is a bijection on `N0 × Q`, with inverse
`J^-1(n,z)=(n,16^n(z+P_n))`. The coordinate z is exactly the source seed of
the unique rational path passing through `(n,u)`; the literal zero-source
section is `z=0`. These statements use finite sums only.

For integers `a>=1,b>=0`, define `m=an+b` and

```math
\mathcal A_{a,b}(n,u)=
\left(m,16^m\bigl(16^{-n}u-P_n+P_m\bigr)\right).
```

This is `J^-1 ((n,z)↦(an+b,z)) J`. Therefore, for all admitted parameters
and all states, with the rightmost map applied first,

```math
\mathcal A_{a,b}\circ\mathcal A_{c,d}
=\mathcal A_{ac,ad+b},\qquad \mathcal A_{1,0}=\mathrm{id}.
```

Every seed fiber is preserved. The action is faithful: equality of two
carrier maps forces equality of their output clocks at n=0 and n=1, hence
equality of b and a. This remains true after restricting to any fixed seed
section. Faithfulness means injectivity of the monoid representation, not
that every action map is surjective.

Let `S_BBP(n,u)=(n+1,16u+r(n+1))`. Expanding one term of P gives

```math
\mathcal A_{1,1}=S_{\mathrm{BBP}},\qquad
\mathcal A_{a,b}(n,u)
=S_{\mathrm{BBP}}^{(a-1)n+b}(n,u).
```

The exponent is evaluated at the **input clock**; it is not a fixed power
independent of the state. In particular the declared clock dilation
`D_p=A_(p,0)` obeys, for every p>=1,

```math
D_p S_{\mathrm{BBP}}=S_{\mathrm{BBP}}^p D_p,
\qquad D_pD_q=D_{pq}.
```

For p>1, `D_p S_BBP != S_BBP D_p`, as their clocks differ by p−1.
Also `D_p != S_BBP^p`: D_p fixes every state at clock zero, whereas the fixed
iterate advances its clock to p. D_p is not `u↦pu`; it includes every
intervening forcing value. Calling it a prime-local dilation of another
carrier would require a further declared intertwiner.

## CS-03b. Source-functor naturality and finite completion

Let T be the ordered category of nonnegative times and let

```math
F(n\to m)(u)=16^{m-n}u+
\sum_{j=n+1}^{m}16^{m-j}r(j),\qquad n\le m.
```

The inherited chronological cocycle gives F as a functor to rational sets.
For `alpha(n)=an+b`, we have `n<=alpha(n)`. The components
`eta_n=F(n→alpha(n))` satisfy, for every n<=m,

```math
F(\alpha(n)\to\alpha(m))\eta_n
=F(n\to\alpha(m))=\eta_mF(n\to m).
```

Thus `eta:F⇒F∘alpha` is natural. Each fiber map is a bijective rational
affine map, so eta is a natural isomorphism of these fiber functors; this
does not make the action on the total clocked carrier surjective. The
composite components obey
`eta^alpha_(beta(n)) eta^beta_n = eta^(alpha∘beta)_n`, proving coherence
from the source cocycle rather than postulating a new higher cell.

For the source path with seed z and a **common** finite horizon L>=m>=n,

```math
u_n+T_n^{(L)}=16^n(z+P_L),\qquad
u_m+T_m^{(L)}=16^{m-n}\bigl(u_n+T_n^{(L)}\bigr).
```

This is the source-preserving finite completion square for every affine
clock arrow. Passage to the actual Green completion gives the same equation
with T_n and T_m. Its circle/Cayley observation is the exact degree
`16^(m-n)` power map. A growing oscillator frequency is multiplied by that
degree, so any joint finite approximation still owes the CAY-05/CAY-07
precision payment; naturality does not erase it.

## CS-03c. What survives the circle quotient

The quotient `(n,u)↦(n,{u})` retains a well-defined action. Replacing u by
u+k changes the output rational state by `16^((a-1)n+b) k`, an integer.
Retaining the clock also retains faithfulness of the **monoid action**.
Its individual circle maps can be many-to-one, and source seeds can alias.

Forgetting the clock is more severe: it need not even define a map on the
remaining circle observation. At input phase zero, D_2 sends `(0,0)` to
output phase zero but sends `(1,0)` to phase `r(2)=106/819`. The same input
circle point would have two different outputs. A source label/clock, or a
separately justified autonomous completed coordinate, must remain available.

## CS-03d. Generic source conjugacy is a decisive limit

This construction works for any prescribed rational forcing sequence.
If r and q have prefix sums P^r and P^q, the clock-preserving map

```math
K(n,u)=\left(n,u+16^n(P_n^q-P_n^r)\right)
```

preserves the initial seed and conjugates their entire affine actions.
It generally changes the Archimedean observer `e(u)`; it is not an
observer-preserving authentication of the source. In particular the zero
forcing with zero seed has the same abstract action laws and a constant
nonnormal orbit. Source and observation must remain named parts of the
structure. The action identities alone cannot select or prove a normal law.

## Verification and remaining compiler gate

`affine_source_probe.py` compares direct four-pole prefix arithmetic with the
unchanged canonical recurrence, checks all source-affine compositions in its
declared finite grid, and tests finite completion, source-gauge conjugacy,
clock-forgetting and false fixed-iterate controls. Its exact receipt is a
finite calibration of the paper proof, not proof by sampling.

This now supplies a faithful indexed rational source-clock action. What
remains UNVERIFIED is a genuine nontrivial C-monoid realization and an encoding
of these indexed states/operations into it with a proved preservation and
reflection theorem. Original-zero parity balance, full hexadecimal normality
and RH remain OPEN.
