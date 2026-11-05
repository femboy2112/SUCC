# Front A/H: exact-tail derivative control and the discrete coherent barrier

**Status:** paper proofs, with exact finite instrument checks. These results are
about the original BBP forcing. The signed chirp theorem is explicitly for the
changed fixed seed `s*=-pi/16`. There is no new selected zero-seed cancellation,
Lean proof, external referee, or scholarly priority claim. The derivation is an
independent same-model pass over the inherited arguments, not an independent
source family.

Let `e(t)=exp(2 pi i t)` and

\[
r(x)=4/(8x-7)-2/(8x-4)-1/(8x-3)-1/(8x-2),
\quad T(x)=\sum_{j\ge1}16^{-j}r(x+j),\quad x>0.
\]

All derivatives below concern this smooth tail, not an invented smooth
interpolation of the selected circle orbit. Put
`B(t)=4+4t+4t²+2t³+t⁴`, `F(t)=B(t)/(16-t⁸)`.
The original Mellin identity is

\[
T(x)=\int_0^1 t^{8x}(1-t)F(t)\,dt.
\]

## AH-01: a sharp-coefficient all-derivative sandwich

For every real `x>0` and every integer `k>=0`,

\[
0<\frac{(k+1)!}{64x^{k+2}}-(-1)^kT^{(k)}(x)
 <\frac{7(k+2)!}{1024x^{k+3}}. \tag{1}
\]

The coefficient on the right is asymptotically sharp for each fixed `k`:

\[
\lim_{x\to\infty}x^{k+3}
 \left(\frac{(k+1)!}{64x^{k+2}}-(-1)^kT^{(k)}(x)\right)
 =\frac{7(k+2)!}{1024}. \tag{2}
\]

In particular `0<1/(64x²)-T(x)<7/(512x³)`, sharpening CC-01's
`1/(64x³)` error coefficient without changing its source or seed scope.

**Proof.** The elementary bounds `0<F<=1`, `F(1)=1`, `0<=F'<=2`
follow directly from `B<=15`, `B'<=22`, and `16-t⁸>=15`. Set `u=-8 log t`.
Then

\[
T(x)=\int_0^\infty e^{-xu}W(u)\,du,\qquad
W(u)=\tfrac18 e^{-u/8}(1-e^{-u/8})F(e^{-u/8}).
\]

Write `v=u/8`, `t=e^-v`. For `u>0`,

\[
\begin{aligned}
0<v-t(1-t)F(t)
&=[v-(1-t)]+(1-t)[1-tF(t)]\\
&<\tfrac12v^2+3v^2=\tfrac72v^2.
\end{aligned}
\]

Here `0<v-(1-e^-v)<v²/2`, and
`1-tF(t)=(1-t)+t(1-F(t))<=3(1-t)<3v`.
Consequently

\[
0<u/64-W(u)<7u^2/1024. \tag{3}
\]

Differentiation under the integral is justified on each compact subinterval of
`x>0` by the integrable majorant `u^(k+1)e^(-x0 u)/64`. Multiply (3) by
`u^k e^-xu` and integrate to obtain (1), with strictness on positive measure.
Finally `F'(1)=2` gives
`W(u)=u/64-7u²/1024+O(u³)` as `u->0`. After substituting `u=v/x`,
(3) supplies a dominated-convergence majorant `7v^(k+2)e^-v/1024`.
This proves (2) and explicitly pays the limit interchange.

**Independent algebraic check.** For integer `n>=1`, the derivative of the
four signed poles agrees identically with the positive beta-difference formula

\[
(-1)^k r^{(k)}(n)=8^k k!\sum_{j=0}^4 b_j
 \left[(8n-7+j)^{-k-1}-(8n-6+j)^{-k-1}\right],
\quad(b_0,\ldots,b_4)=(4,4,4,2,1).
\]

The latter proves positivity and decrease in `n` term by term. The exact
instrument computes the original four-pole expression and this second
expression separately, then bounds the infinite `16^-j` remainder. Both share
BBP provenance; they are independent implementations, not independent sources.

## AH-02: uniform discrete coherent asymptotic on a larger frequency range

There is an absolute constant `C` such that, for all sufficiently large integer
`A` and every positive integer `H` with `1<=Lambda=H/A²<=A`,

\[
\left|M_A^{(s_*)}(H)-\frac{256}{\pi\Lambda}\right|
 \le C\left(\Lambda^{-2}+A^{-1}\right),\qquad s_*=-\pi/16. \tag{4}
\]

Thus for **every** sequence of integer epochs and frequencies satisfying
`Lambda->infinity` and `Lambda/A->0`,

\[
\Lambda M_A^{(s_*)}(H)\longrightarrow256/\pi. \tag{5}
\]

This extends CC-02's sufficient regime `Lambda²/A->0` to `Lambda/A->0`.
The constants in (4) are uniform in `A,H` and in both subinterval endpoints.
No pointwise replacement of `T(n)` by `1/(64n²)` is used inside the phase.

**Discrete proof.** Set `f(x)=-H T(x)`, `z_n=e(f(n))`,
`delta(x)=f(x+1)-f(x)>0` and

\[
q(x)=\frac1{e(\delta(x))-1}
     =-\frac12-\frac i2\cot(\pi\delta(x)).
\]

On `A-1<=x<=2A`, (1), for `k=1,2,3`, implies

\[
 c\Lambda/A\le\delta(x)\le C_0\Lambda/A\le1/8,
\quad |\delta'(x)|\le C_1\Lambda/A^2,
\quad |\delta''(x)|\le C_2\Lambda/A^3. \tag{6}
\]

These constants are absolute. For example the lower bound follows from
`-T'(t)>=1/(64t³)` for `t>=4`, and the upper bounds follow from
`-T'(t)<=1/(32t³)`, `T''(t)<=3/(32t⁴)`,
`-T'''(t)<=3/(8t⁵)`. Taking `A>=8` makes the displayed `1/8` bound
immediate. The elementary cotangent formulas and (6) give, uniformly,

\[
 |q|\ll A/\Lambda,\qquad |q'|\ll1/\Lambda,
 \qquad |q''|\ll1/(A\Lambda). \tag{7}
\]

For clarity, the derivative estimates use
`|q'|<=C|delta'|/delta²` and
`|q''|<=C(|delta''|/delta²+|delta'|²/delta³)` on `0<delta<=1/8`.
They do not hide frequency-dependent constants.

For any integers `A<=a<b<=2A`, exact telescoping gives

\[
\sum_{n=a}^{b-1}z_n
 =q(b-1)z_b-q(a)z_a+
   \sum_{n=a+1}^{b-1}[q(n-1)-q(n)]z_n. \tag{8}
\]

Put `w(x)=q(x-1)-q(x)` and `p(x)=w(x)q(x)`. By (7),
`|w|<<1/Lambda`, `|w'|<<1/(A Lambda)`,
`|p|<<A/Lambda²`, `|p'|<<1/Lambda²`.
Apply the identical telescoping identity to the last sum in (8), with
coefficient `w(n)`. Its endpoints and total variation are at most
`2 sup|p|+integral|p'|<<A/Lambda²`. This also covers empty or singleton
remainders. Thus

\[
\sum_{n=a}^{b-1}z_n=q(b-1)z_b-q(a)z_a+O(A/\Lambda^2). \tag{9}
\]

Equation (1) with `k=1` also gives
`delta(x)=H/(32x³)+O(H/x⁴)`. Since
`q(x)=1/(2 pi i delta(x))+O(1)`, uniformly on (6), (9) becomes

\[
\frac1A\sum_{n=a}^{b-1}z_n
 =\frac{16}{\pi i\Lambda}
   \left[(b/A)^3z_b-(a/A)^3z_a\right]
 +O(\Lambda^{-2}+A^{-1}). \tag{10}
\]

Replacing `(b-1)³` by `b³` costs `O(1/(A Lambda))`, already absorbed.
The upper bound in (4) follows because the bracket has modulus at most 16.

For the lower bound set `b=2A`. For all sufficiently large absolute `Lambda`,
there is a unique real `a0` in `[A,2A)` with
`f(b)-f(a0)=1/2`. Indeed (6) bounds the total phase increase below by
`c Lambda`; it also gives `b-a0=O(A/Lambda)`. Choose an integer `a` within
one unit of `a0`, inside `[A,b)`. The upper derivative bound in (6) ensures
such an endpoint and yields

`z_a=-z_b+O(Lambda/A)`, `(a/A)³=8+O(1/Lambda)`.

Substitute in (10). The modulus is at least
`256/(pi Lambda)-O(Lambda^-2+A^-1)`. For `1<=Lambda<=Lambda0`,
increasing the same absolute constant handles (4) by `0<=M<=1`.
This proves the uniform statement and then (5).

**Second view of the constant.** Under the continuous change of variable
`v=H T(x)`, the inverse phase density at the right endpoint is
`1/(H(-T'(2A)))~256 A³/H`. An opposite-phase endpoint pair contributes
`2/(2 pi)` times this density. Dividing by `A` gives
`256/(pi Lambda)`. The discrete proof above independently pays the lattice
error and proves maximality; this second calculation is a check on the factor,
not a substitute for the uniform proof.

## AH-03: audit of inherited CC-01--04 and F4

CC-01 is valid: the Mellin positivity and `F'<=2` imply its stated tail
sandwich. AH-01 strengthens its coefficient and derivatives.

CC-02's two continuous integrations by parts give a uniform endpoint remainder
`O(mu^-2)` on `[1,2]`. The half-turn endpoint
`a=2(1+2/mu)^(-1/2)` satisfies `mu/a²-mu/4=1/2` exactly.
Consequently its `4/(pi mu)` and `256/(pi Lambda)` constants are correct.
Its phase-replacement and mesh errors are `O(Lambda/A)`; after multiplying
by `Lambda`, its stated `Lambda²/A->0` regime is sufficient. AH-02 improves
this proof by keeping the exact phase throughout.

CC-03 follows for each fixed nonzero integer `h`: for sufficiently large `A`,
`log A/16<Lambda_A<=log A`, so either coherent asymptotic applies. Negative
`h` only conjugates the sums. CC-04's tail increment follows directly from
`1-t⁸<=8(1-t)` and `F<=1`:

`0<T_n-T_(n+1)<=16/[(8n+1)(8n+2)(8n+3)]<1/(32n³)`.

Its phase-span and midpoint-rotation lower bound are valid, including `m=1`.
No one of these statements controls the authentic zero seed.

For parent F4, write exactly
`U_m=16^j U_(m-j)+S_j(m)`,
`S_j(m)=sum_(ell=0)^(j-1)16^ell r(m-ell)`.
Discard at most `j` indices below `A+j`. The remaining shifted indices remain
inside the same original epoch. The positive moment makes `S_j` decreasing,
so the multiplier `e(h S_j(m))` has variation bounded by
`2 pi |h| S_j(A+j)<<H/A²`. Discrete partial summation gives

`M_A(h)<=j/A+(1+C H/A²)M_A(H)`.

If `j>=A`, the discarded contribution already exceeds the trivial bound;
otherwise the displayed proof applies. In the intended fixed-h range
`H<=A³`, one has `j=O(log A)` anyway. Thus the stated retrieval cost and
its maximal-subinterval scope survive this audit.

Finally suppose the critical gate is actually proved for all fixed nonzero
`h` along all sufficiently large dyadic epochs. Then F4 gives `M_(2^k)(h)->0`.
For `2^L<=N<2^(L+1)`, subdivide `[1,N]` into complete dyadic epochs and
one last partial epoch. After a fixed early prefix, every block sum is at most
`epsilon 2^k`. Their geometric sum is at most `2 epsilon N`.
Divide by `N`, let `N->infinity`, then `epsilon->0`. This is the full-prefix
Weyl gate. The completion error
`|e(h U_n)-e(h 16^n pi/16)|<=2 pi |h| T_n=O_h(n^-2)`
is summable, hence has vanishing normalized prefix effect. The resulting
all-character Weyl criterion gives base-16 normality. Every step is
conditional on the still-open selected critical gate.

## AH-04: why the selected derivative and fixed-lag attempts stop

The exact selected sequence is `U_n(0)=16^n pi/16-T_n`; the coherent sequence
is only `-T_n`. Removing the term `16^n pi/16` is a seed change, not a
legitimate phase simplification. Smooth interpolation gives an enormous
positive derivative, but a first-derivative exponential-sum bound requires
control of the increments **away from integers**. Monotonicity of an
unwrapped derivative alone does not provide that control: `f(n)=n` already
has derivative one and maximal, not cancelling, characters.

For fixed integer lag `d`, the exact difference is

\[
U_{n+d}-U_n=(16^d-1)U_n+
 \sum_{j=1}^d16^{d-j}r(n+j).
\]

Thus a van der Corput reduction exposes a selected coefficient at
`H(16^d-1)` with a known multiplier; it does not remove the original
unknown phase. At critical `H~A² log A`, that multiplier has non-negligible
variation. Bounding its modulus and discarding its phase simply recreates a
retrieval loss. The first missing estimate is a signed selected correlation,
not a tail derivative bound. AH-02 demonstrates that every argument using
only those seed-independent tail derivatives meets a nonzero `256/pi`
barrier. It refutes a seed-uniform little-o claim, not a zero-seed theorem.

**Remaining statuses:** authentic fixed-h Weyl OPEN; critical selected ratchet
OPEN; original coarse collision energy OPEN; pi base-16 normality OPEN; RH
OPEN and separate.
