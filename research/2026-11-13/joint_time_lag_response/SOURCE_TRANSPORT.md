# Source-preserving transport of the signed time–lag response

**Status: PROVED LOCAL, paper proof with exact finite checks.** The source is
unchanged, with literal `U_0=0`. This is a quantified stability theorem for an
available observable, not a signed statistical saving for that source. No R0
or normality conclusion is asserted. The argument is also valid for every
changed seed; that broader validity is a transport feature and prevents using
this result alone to select the desired statistics.

## 1. Contract and archival inputs

For the authentic four-pole source, put

\[
U_{n+1}=16U_n+r(n+1),\quad
T_n=\sum_{j\ge1}16^{-j}r(n+j),\quad Y_n=U_n+T_n=16^nx,
\qquad x=\pi/16.
\]

The inherited exact moment representation is

\[
T(t)=\int_0^1 z^{8t}G(z)\,dz,
\quad G(z)=\frac{1-z}{(2-z^2)(z^2-2z+2)},\qquad t>0.
\tag{ST-1}
\]

This is IAD-03 and the source contract of
`research/2026-11-11/innovation_arithmetic_decoupling/THEOREMS.md`.
IAD-06(a) already transports the two-time rational difference to the completed
difference with a lag-uniform `O(|h|/B^2)` error. We reuse that exact transport.
The contribution here is a smaller, explicitly summed **joint time–lag**
error budget, retaining the actual Fejer weights and shell endpoints.
No new Mellin kernel or new source is introduced. The adjacent source-tail
`O(n^-3)` estimate is also inherited: SB-01 in
`research/2026-10-30/selected_boundary_slip/THEOREMS.md`, and the sharper
CC-04 in `research/2026-11-04/critical_chirp/PROOFS.md`. In particular, the
order `n^-3` is not a discovery of this round.

For an integer shell `B>=1`, integer `1<=H<=B`, and integer frequency `h`,
let `z_n^V=e(hV_n)` on `B<=n<2B`, zero off that shell, for `V=U,Y`. Define

\[
c^V_{B,h}(\ell)=\frac1B
\sum_{n=B}^{2B-1-\ell}e\bigl(h(V_{n+\ell}-V_n)\bigr),
\]

\[
F^V_{B,H,h}=\frac1H+
\frac2H\sum_{\ell=1}^{H-1}
\left(1-\frac\ell H\right)\operatorname{Re}c^V_{B,h}(\ell).
\tag{ST-2}
\]

The real signed sum in ST-2, not the sum of absolute correlations, is the
object being transported. Its nonnegativity and window-energy meaning are
inherited Fejer identities (IAD-01); this file does not recount them as new.

## 2. Derivative and exact lag budget

For `0<=z<=1`, both `2-z^2` and `z^2-2z+2` are at least one. Thus
`0<=G(z)<=1-z`, with strict inequality inside `(0,1)`. Differentiation under
the integral is justified on compact positive `t` intervals by integrability
of `z^(8t)|log z|`. It gives

\[
0<-T'(t)
<8\int_0^1z^{8t}(-\log z)(1-z)\,dz
=\frac{8(16t+3)}{(8t+1)^2(8t+2)^2}
<\frac1{32t^3}.
\tag{ST-3}
\]

For the final inequality, multiplying the positive denominators reduces it
exactly to

\[
(8t+1)^2(8t+2)^2-256t^3(16t+3)
=2304t^3+832t^2+96t+4>0.
\]

Consequently, for all integers `n>=1, ell>=1`,

\[
0<T_n-T_{n+\ell}
<\frac1{64}\left(\frac1{n^2}-\frac1{(n+\ell)^2}\right)
<\frac{\ell}{32n^3}.
\tag{ST-4}
\]

The exact source completion gives

\[
e\bigl(h(U_{n+\ell}-U_n)\bigr)
=e\bigl(h(Y_{n+\ell}-Y_n)\bigr)
e\bigl(h(T_n-T_{n+\ell})\bigr).
\]

Using `|e(t)-1|<=2 pi |t|` and ST-4,

\[
\left|e\bigl(h(U_{n+\ell}-U_n)\bigr)
-e\bigl(h(Y_{n+\ell}-Y_n)\bigr)\right|
<\frac{\pi|h|}{32}
\left(\frac1{n^2}-\frac1{(n+\ell)^2}\right)
<\frac{\pi|h|\ell}{16n^3}
\tag{ST-5}
\]

when `h!=0`; at `h=0` both differences are exactly zero.
The coarse pointwise `O(|h|/n^2)` budget is thereby sharpened by the relative
lag `ell/n` when `ell=o(n)`.

## 3. The signed Fejer response has a telescoping boundary budget

Define the nonnegative rational number

\[
Q_{B,H}=\frac1{16HB}
\sum_{\ell=1}^{H-1}\left(1-\frac\ell H\right)
\left[
\sum_{n=B}^{B+\ell-1}\frac1{n^2}
-\sum_{n=2B-\ell}^{2B-1}\frac1{n^2}
\right].
\tag{ST-6}
\]

**Theorem ST-7.** For every integer `B>=1`, `1<=H<=B` and integer `h`,

\[
\boxed{
|F^U_{B,H,h}-F^Y_{B,H,h}|
\le\pi|h|Q_{B,H}
\le\frac{\pi|h|(H^2-1)}{128HB^3}
<\frac{11|h|(H^2-1)}{448HB^3}
}
\tag{ST-7}
\]

where the last strict inequality is replaced by equality when `h=0` or
`H=1` (all budgets and differences then vanish). The last displayed rational
budget uses the classical elementary bound `pi<22/7`.

*Proof.* Insert ST-5 in the signed sum ST-2 and apply the triangle inequality
only to the **transport error**. No absolute-value estimate is substituted
for the signed target response. The coefficient becomes

\[
\frac{\pi|h|}{16HB}
\sum_{\ell=1}^{H-1}\left(1-\frac\ell H\right)
\sum_{n=B}^{2B-1-\ell}
\left(\frac1{n^2}-\frac1{(n+\ell)^2}\right).
\]

The inner sum telescopes to the bracket in ST-6, including when the two
endpoint sets overlap. Pair its terms as

\[
\sum_{j=0}^{\ell-1}
\left[(B+j)^{-2}-(2B-\ell+j)^{-2}\right].
\]

Every summand is positive and at most `3/(4B^2)`, because its first term is
at most `1/B^2` and its second is at least `1/(4B^2)`. Finally,

\[
\sum_{\ell=1}^{H-1}\ell(1-\ell/H)=(H^2-1)/6.
\]

Combining these identities proves the first two inequalities. Substituting
`pi<22/7` proves the rational certificate. The empty `H=1` sum and `h=0`
case hold directly. ∎

**Resolution consequence.** Along any schedules `1<=H(B)<=B` and integer
`h(B)` for which `|h(B)|H(B)/B^3 -> 0`, the rational and completed signed
responses differ by `o(1)`. For a logarithmic lag window this permits
`|h(B)|=o(B^3/log B)`. This is a source-preserving transport range; no
cancellation at those frequencies is inferred. For fixed `h` and `H=o(B)`,
it improves the inherited `O(|h|/B^2)` response transport by `H/B`.

**Hostile seed.** For `s=-x`, the completed response is the coherent padded
response, not a small one. ST-7 still transports it accurately from the
rational orbit `U_n(s)=-T_n`. Thus neither the shrinking correction nor its
uniformity supplies the missing arithmetic saving. The exact zero-seed
identity must enter a further estimate.

## 4. An archived obstruction that must remain in the proof graph

The tempting claim that a growing, short-lag filter will itself reduce the
rational carrier's denominator complexity was already settled by CT-01 in
`research/2026-10-30/zero_boundary_dispersion/crt/CRT_DOSSIER.md`.
For integer polynomials `P_n(z)=sum_(j=0)^(d_n) b_(n,j)z^j`, with

\[
d_n=o(n),\qquad
\log\max(1,\sum_j|b_{n,j}|)=o(n),\qquad P_n(16)\ne0,
\]

that inherited source theorem proves

\[
\log\operatorname{den}(P_n(E)U_n)=6n+o(n).
\tag{ST-8, inherited CT-01}
\]

In particular every sublinear moving lag keeps this exponential conductor.
The short-interval LCM lemma and exact denominator inequalities proving
ST-8 are already in CT-01; no novelty is claimed here. The original
sharp conductor `log den(U_n)=6n+o(n)` is CG-01 in
`research/2026-10-30/arithmetic_barrier/SHARP_CONDUCTOR_GROWTH.md` and imports
the prime number theorem in fixed arithmetic progressions.

If `P_n(16)=0`, the completed filtered phase is zero for **every** seed.
Any successful filter construction must therefore do more than replace the
phase by one finite linear recurrence annihilator. The conductor theorem
excludes this particular proposed simplification; it does not exclude
signed combinations of filter outputs, approximate filters, nonlinear
observables, or a new real inequality on their joint response.

## 5. Exact remaining inequality and finite verification

One sufficient all-mode target is a chosen schedule `H(B)->infinity`,
`H(B)<=B`, for which the original zero-seeded response satisfies

\[
\forall h\in\mathbb Z\setminus\{0\},\qquad F^U_{B,H(B),h}\longrightarrow0.
\tag{OPEN-ST}
\]

ST-7 pays its completion error, and the padded van der Corput inequality
then gives `W_B(h)->0`. But IAD-02 already establishes the relevant
all-mode Fejer schedule equivalence. OPEN-ST is an **open cancellation
interface, not a newly simpler theorem**. The result of this file is the
smaller source-derived error on that interface.

Before selecting any numerical theory, the finite checks were fixed as:

1. Exact rational evaluation of ST-6 and its ST-7 bound for every
   `1<=B<=100`, `1<=H<=B` (5,050 cases).
2. Exact rational tail intervals, using the first 20 authentic source terms
   plus remainder at most `16^(-20)r(n+21)/15`, for
   `n in {1,2,7,31,127,509}` and `ell in {1,2,7,31}` (24 cases).
   Verify the lower interval difference is positive and its upper endpoint
   lies below the ST-4 integrated bound.

Both checks were executed and passed. They check implementation and
constants; ST-3 through ST-7 derive their universal quantifiers from the
paper proof. No floating-point phase sample was used as a certificate.

The next falsifier is an exact failure of the rational endpoint budget or
one rigorous tail interval violating ST-4. The next arithmetic input is an
actual zero-seed-dependent upper bound on the signed response in OPEN-ST
(or a fixed saving sufficient for a weaker stated gate), not a smaller
transport residual.
