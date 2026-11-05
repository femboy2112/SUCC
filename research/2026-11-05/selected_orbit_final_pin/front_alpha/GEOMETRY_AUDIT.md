# Rotated independent EPSILON/ZETA audit

Read-only sources inspected by the separate carry-arithmetic worker:

- `gamma_sphere_solenoid/ARITHMETIC_DECK_RIGIDITY.md` and
  `gauge_sphere_tower/QUANTIZED_ARITHMETIC_ATOMS.md` via `git show` at the pinned
  #517 head `a2905c9e1770fea519193839433bdca4bd29336f`; these contain #515/#516's
  inherited proofs. No sibling code or theorem was merged.
- #508 `zero_frame_bispectrum_audit/PROOFS.md`, whose source commit is
  `ce74006a7e742fb26a9d32fdd6060479d7c61119`, and its #507 prerequisite
  `zero_frame_coupling/front_cf/PROOFS.md` in the pinned #518 ancestry.

This review rederives the claims below. It is not a blind external scholarly
review, kernel proof, new source-selected theorem, or new experiment campaign.

## Z1: odd-torsion branch proof survives; its exact domain matters

The Cayley map `t=-i(z-1)/(z+1)` sends `z=e(x)` to `tan(pi x)` with the
stated positive orientation. Substitution in `q=(t-1-i)/(t-1+i)` gives

```
B(z)=((1+2i)z+1)/(z+1-2i),   S(z)=-B(z)^2.
```

The proposed involution `J=B^(-1) (-B)` consequently satisfies `S J=S`.
Clearing `w=J(z)` yields

```
(2-i)zw - 3i(z+w) - (2+i)=0.
```

At a prime above 1+i, reduction gives `(z+1)(w+1)=0` in a field of
characteristic 2. Prime-to-2 torsion injectivity can be checked directly:
if an odd-order root z of order q reduced to 1 but z was not 1, then
`1+z+...+z^(q-1)=0` would reduce to `q=1` in characteristic 2, impossible.
Thus z or w is 1. But `J(1)=(-3+4i)/5` is in Q(i) and not Z[i], so it is
not an algebraic integer and cannot be a root of unity. The claimed
injectivity of S on *all odd-order roots of unity* follows.

The collapsed four-pole denominator is odd, so original U_n has odd reduced
denominator. This is a real arithmetic restriction. The coherent seed
`-alpha` and periodic-completion seeds `beta-alpha` generally have irrational
finite states and lie **outside this exact domain**. It would therefore be
wrong to say the odd-torsion observation is itself seed-blind. Its limitation
is different: exact algebraic membership and injectivity do not give a
quantitative distribution bound. Odd-denominator rational seeds such as 1/5
still belong to the admissible set, and it is dense in the whole circle.

## Z2: phase/Jacobian transport and inverse instability are correct

For the Blaschke zero `z0=(-1+2i)/5`, `|z0|=1/sqrt(5)`. Its angular derivative
is the positive Poisson kernel `(1-|z0|^2)/|z-z0|^2`, with range
`[phi^(-2),phi^2]`. This is the Jacobian of **B**. The angular derivative of
**S=-B^2** is twice that value, and S has two inverse branches. Dropping
that factor or averaging without its branches would be invalid transport.

Mean-value applied to S^h gives the transported input-Haar moments
`S(0)^h`, where `S(0)=(3-4i)/25`. Thus input Haar transports to the stated
Poisson measure, not uniform sphere-circle measure. Moreover `S_*Haar`
equals `S_*(J_*Haar)`, whereas `J_*Haar` is non-Haar because its first
moment is `J(0)=(-1+2i)/3`. Approximating the two input arrays by odd roots
preserves their weak limits and asymptotically equal S-observation limits.
This does not contradict Z1: there is no exact equality of the two individual
odd-root observations. It proves the stated D obstruction to stable inversion
on the dense arithmetic set. Those arrays do not obey the original time
recurrence; this is an inverse-observation obstruction, not a counterexample
to original-source normality.

## Z3: curvature erases phase; anchored sections retain the Weyl observable

For `F(z)=Xi z^d`, `|Xi|=1`, direct differentiation gives
`|F'(z)|^2=d^2|z|^(2d-2)` and `|F(z)|^2=|z|^(2d)`. Hence

```
F*omega_FS = (i/(2pi)) d^2 |z|^(2d-2)/(1+|z|^(2d))^2 dz wedge dbar(z).
```

Its integral is d, from substitution `u=r^(2d)` in
`2d^2 integral_0^infinity r^(2d-1)/(1+r^(2d))^2 dr`. Both the curvature
and charge are exactly independent of Xi. Original, coherent and mutated
phase histories therefore have identical values. The distinction between
the raw nonconstant pullback connection and a *chosen* constant-curvature
monopole connection is necessary and correctly stated in #516.

Pulling back the homogeneous section `Z^j W^(k-j)` gives exactly
`Xi^j Z^(dj)W^(d(k-j))`. With fixed endpoint/trivialization conventions,
its relative coefficient is `e(jU_n)`. This is a source-faithful B
representation. No averaging bound follows; removing the anchor also removes
the asserted interpretation of that coefficient as an observed phase.

## E1: bispectrum sign and source-derived error survive independent check

For `c_j=(-1)^(j-1) binom(m,j)`, their sum is 1 and

```
sum_(j=1)^m c_j Z_(n+j) = Z_n + (-1)^(m+1) Delta^m Z_n.
```

Thus the angular coefficient is 1, not 0. At m=2,
`Q_2=e(HU_n)e(-H Delta^2 Z_n)`; the minus sign is essential. A pairwise
Gram cancels the angular phase, while this cubic observable retains it.

The #507 radial derivative prerequisite also checks. Its seven taps have
coefficient sum 15 and absolute offset sum 167. In
`z(x)=(1/4) sum_(k>=1)16^-k d(x+k)`, the leading pole gives
`z(x)~1/(32x)`. The differentiated remainder constant is

```
C_m=(m+1)! [1/30 + (167/3840)(16/9)^(m+2)].
```

The 1/30 term is `(15/32) sum k16^-k`; the other term is the pole-offset
error times `(1/4)sum16^-k`. For m=2 the constant is `18413/6561` and
`32 C_2<128`, giving `0<z''(x)<=1/(8x^3)` on x>=128. Integrating twice
on a unit square gives `0<Delta^2 Z_n<=1/(8n^3)`. The chord estimate then
bounds every normalized sharp-interval bispectrum/Weyl difference by
`pi |H|/(4A^3)`. At `|H|=A^2 Lambda` and `Lambda~log A`, multiplying
by Lambda gives `pi Lambda^2/(4A)->0`.

For the same-forcing coherent control one must keep this genuine radial
Z unchanged and put the homogeneous seed shift `16^n s` into Y, as #507
explicitly does. An arbitrary allocation of the seed shift into Z would
invalidate the derivative bound. With the stated allocation the transport
error is unchanged and the original coherent obstruction transfers. At
critical growing H, "coherent" does not mean that the full-epoch mean
necessarily tends to 1; the failure is of the specified critical ratchet.
No new trilinear saving or signed source bound has been proved.

## Ledger verdict and precise open interface

| Claim | Review outcome | Scope |
|---|---|---|
| Odd-torsion deck injectivity | Inherited paper proof independently rederived | Exact finite arithmetic identification; B, not an occupancy inequality |
| Odd-root weak inverse instability | Inherited countermodel rederived | D obstruction to distribution recovery from this observation alone |
| Source-blind pullback curvature | Inherited exact identity rederived | D for curvature-only selection; coherent seed has identical values |
| Anchored section phase | Inherited identity rederived | B; exactly the unpaid selected Fourier character |
| Bispectrum defect at critical depth | Inherited bound independently rederived from signed radial taps | B transport with explicit sharp-window error; no signed saving |
| New selected-embedding conditioning or nonlinear coercivity | OPEN / none obtained | No new class A result and no new class C reduction |

The surviving next interface is a quantitative bound on the chronological
nonzero-charge coefficients `e(jU_n)` or on the bispectrum mean itself,
retaining original selected carry/numerator data. Exact branch injectivity,
curvature, or the small radial error cannot supply that bound. No interface
to the completed zeta Weil form is established by these calculations.
