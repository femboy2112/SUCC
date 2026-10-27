# Operation First Binary Branch — two bits + actual value (authentic BBP source)

**2026-10-27. RESEARCH ONLY.** Source parent [#325](https://github.com/femboy2112/SUCC/pull/325), pinned head \`95ee2f1fab851afe1517d8ec5a0589885842426f\`. Compatible with ongoing independent [Claude #326](https://github.com/femboy2112/SUCC/pull/326) and [Codex #327](https://github.com/femboy2112/SUCC/pull/327) work; neither branch is rewritten. **π base-16 normality remains OPEN.** Status: **PAPER-PROVED exact finite number-theoretic statements**, not independent academic novelty or Lean analytic authority.

## BBP source and normal form

The original four signed rational poles are retained, with \`U_0=0\`:

$$
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}
=\frac{A(x)}{D(x)},
$$

$$
A(x)=120x^2-89x+16,\quad D(x)=(2x-1)(4x-1)(8x-7)(8x-3).
$$

For every prime \`p>=7\`, every level \`L>=1\` and \`q=p^L\`, the fractions below have denominators invertible modulo q:

$$
\boxed{A(x)=120(x-b)^2+c,\qquad b=\frac{89}{240},\quad c=-\frac{241}{480}.}
$$

Given numerator target \`a=A(x) mod q\`, the centered actual-value coordinate \`u=x-b modq\` satisfies \`u^2=v(a)\`, where

$$v(a)=(a-c)120^{-1}\pmod q.$$

At 7, \`b=6,c=1,120=1 mod7\`, so \`A(x)=(x+1)^2+1 mod7\`: the plus and minus square-root orientations meet at \`x=6\`.

## Exact two-bit state + actual value theorem (TB-1)

The discrete metadata has **two bits**, \`sheet∈{0,1}\` and \`pole∈{0,1}\`: \`sheet\` records ± the canonical Hensel unit root when that sign exists; \`pole=1\` iff the *original full-source* denominator \`D(x)\` is divisible by p. The value payload consists of \`a mod p^L\` **and a finite lifting index j**. Both bits are deterministic functions of the actual x; \`pole\` is source-authentic redundancy/check information, not an independent random input.

Classify \`v=v(a) mod p^L\`:

1. If \`v=0\`, the merged critical fiber is exactly \`u=p^ceil(L/2) j\`, with \`0<=j<p^floor(L/2)\`; there is no intrinsic root orientation and \`sheet=0\` is only a convention.
2. If \`v_p(v)=2s<L\` and its unit part \`v/p^(2s)\` is a square modulo p, choose the positive canonical root \`r\` via Hensel modulo \`p^(L-2s)\`. Every source-time solution, uniquely, has
   $$
   \boxed{u=p^s\bigl((-1)^{\text{sheet}}r+jp^{L-2s}\bigr)\pmod{p^L},\qquad 0\le j<p^s.}
   $$
   Its fiber cardinality is \`2p^s\`.
3. If \`v_p(v)<L\` is odd, or the unit part is nonsquare modulo p, the fiber is empty.

*Proof.* If \`u^2=v mod p^L\` with \`v\ne0\`, the valuation is \`2s\`, the unit equation has two Hensel roots because \`2u/p^s\` is a unit, and each lifts \`p^s\` ways from modulus \`p^(L-2s)\` to modulus \`p^(L-s)\`. If \`v=0\`, the condition is \`2v_p(u)>=L\`. Inverting \`x↦x-b\` establishes the exact reconstruction. QED.

**Sharp failure of a two-bit-only model:** at \`p=7,L=2\`, the target \`A(x)=29 mod49\` has seven distinct roots \`x=6,13,20,27,34,41,48\`. They all have \`(sheet,pole)=(0,0)\` but require seven distinct \`j\` values. **Two bits + value payload work at every depth; two bits alone fail by level 49.** No philosophical assertion that binary is canonically minimal is proved.

## Complete base-7 source state

| x mod 7 | A(x) mod 7 | sheet | pole |
|---:|---:|---:|---:|
| 0 | 2 | 0 | 1 |
| 1 | 5 | 0 | 0 |
| 2 | 3 | 0 | 1 |
| 3 | 3 | 1 | 1 |
| 4 | 5 | 1 | 1 |
| 5 | 2 | 1 | 0 |
| 6 | 1 | 0* | 0 |

\`0*\` is a sign convention at the merged branch. Numerator mirror pairs are \`(0,5),(1,4),(2,3)\`. **Every nontrivial pair contains at least one p-nonunit denominator**; the complete source \`D\` distinguishes information that A alone loses. The p-unit domain is \`{1,5,6}\`, on which the numerator is injective. Because \`A(x)=(x+1)^2+1\` is nonzero for every x mod7 (−1 nonsquare), for all integer n

$$
\boxed{v_7(r(n))=-v_7(D(n)).}
$$

Hence the pole-contact bit is precisely the indicator of **negative 7-adic valuation of the original rational BBP source**. This is not a claim that the ordinary real source is undefined at these integer times. At prime 11, regular/regular mirror pairs do occur, giving a useful hostile comparison.

## Exact SUCC successor and CRT extension (TB-2)

Let \`C_(p,L)\` denote the valid two-bit+value encoding, with exact decoder. There are exactly \`p^L\` valid source-time states. Define

$$
\boxed{\mathcal T_{p,L}=C_{p,L}\circ(x\mapsto x+1)\circ C_{p,L}^{-1}.}
$$

This is a **single-cycle finite successor machine**, and in the centered value coordinate \`u'=u+1\`. It is conjugate to the ordinary finite adding machine, **not** real-circle mixing. Combining this valid 7-power decorated inverse with the [#321](https://github.com/femboy2112/SUCC/pull/321) authentic all-time 2-adic zero boundary and [#325](https://github.com/femboy2112/SUCC/pull/325) cleared 3/5 numerator permutations gives an exact finite CRT permutation

$$n\mapsto\bigl(U_n\bmod16^k,\ A(n)\bmod3^L,\ A(n)\bmod5^J,\ C_{7,H}(n)\bigr)$$

on every time period \`16^k 3^L 5^J 7^H\`. These are typed *arithmetic* labels, not product-independent trajectories or real phases.

## First nonzero finite arithmetic Gauss response (TB-3)

For every prime \`p>=7\` and integer \`h\not\equiv0 modp\`, let \`e(x)=exp(2πix)\` and \`G_p(h)=Σ_(x modp)e(hA(x)/p)\`. Then

$$
\boxed{|G_p(h)|^2=p,\quad |G_p(h)|=\sqrt p.}
$$

Expand the square, use \`A(x)-A(y)=(x-y)(120(x+y)-89)\`, and change variables to \`(u,v)=(x-y,120(x+y)-89)\`, whose determinant 240 is invertible mod p. The double sum is \`Σ_u Σ_v e(huv/p)=p\`. For p=2,3,5, A permutes residues and every nontrivial arithmetic additive character instead sums to **zero**. Therefore 7 is the first prime where the authentic source numerator has a nontrivial *finite arithmetic* Fourier response. This is not a bound for \`Σ e(hU_n)\`.

## What remains OPEN (read #327)

The independent Codex [#327](https://github.com/femboy2112/SUCC/pull/327) demonstrates that a prescribed growing CRT energy criterion can be **strictly stronger than normality**, even for a normal carrier of finite irrationality exponent. This two-bit construction establishes a **faithful arithmetic state/branch/denominator-pole decomposition**, not a new real-phase cancellation inequality. Next probe: a source-selected signed correlation of \`e(hU_n)\` with the branch, *original-source pole bit*, and lifting index, comparing p=7 (all mirror pairs hit pole strata), p=11 (regular pairs exist), and p=241 (numerator discriminant). Exclude #320's nonnormal same-shape source and changed-initial-state controls before promoting any claim. The all-fixed-h requirement \`Σ_(n<N)e(hU_n)=o(N)\` remains unpaid.

### Authority / files

- \`scripts/bbp_two_bit_sheet_probe.py\`: pure-stdlib exact canonical Hensel unit-square root, inverse, binary states, higher-level fibers and successor, Gauss difference oracle;
- \`tests/test_bbp_two_bit_sheet_probe.py\`: independently sourced exact rational, 7² seven-way counterexample, negative/mutation/prime-power, signed-source-pole and successor controls.
- The originating longer code received 14/14 focused standalone exact tests, with raw log and SHA-256 receipt available in the separate downloadable research bundle. Any repository-native / hosted / Lean authority must be verified **on the exact commit**; never infer it from the standalone tests. Neither main nor frozen source is modified.
