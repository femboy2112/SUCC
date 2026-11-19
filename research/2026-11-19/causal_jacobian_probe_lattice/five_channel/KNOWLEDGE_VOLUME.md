# Knowledge volume: compatible fibers, retained history, and paid resolution

**Status:** exact finite-dimensional and local-field algebra within the stated
observer model. These statements concern distinguishability, not truth
probabilities or the temporal distribution of pi digits.

## 1. The observer's internal equivalence class is an actual fiber

For a linear exact observation `P` and record `m`, compatible states form
`K_m={x:Px=m}`. Differences lie in `ker P`. A linear map `G` descends to the quotient
when `G ker P subset ker P`; keeping this particular record unchanged requires
`PG=P`. In a nonlinear model the condition must concern entire fibers. The
differential kernel describes local invisible directions only.

This separates two legitimate meanings of the owner's rotation:

- Re-express already acquired knowledge by an invertible change of readout
  coordinates, transporting its metric and precision contract as well.
- Query another direction or earlier sample that is actually available from
  the retained history. This can refine the compatible-state fiber.

Neither operation rewrites an earlier source event. A new physical source tick
is recorded separately. In particular, at time233 the full implemented journal
can recover the previously unselected innovation at147. An observer that retained
only four innovation scalars needs extra access or a new future sample instead.

## 2. The prime-resolution lattice and its exact volume

Consider the normalized innovation chart `A=A_p` of CONSTRUCTION.md and
coefficients in `Z_p^4`. At absolute precision `a>=1`, a consistent report
`y mod p^a` has compatible-state fiber

\[
K_{y,a}=c_0+\{v\in\mathbb Z_p^4:Av\in p^a\mathbb Z_p^4\}.
\]

Let the Smith exponents of `A` over `Z_p` be
`0<=s_1<=s_2<=s_3<=s_4`. Unimodular changes of basis reduce the four conditions
to `p^(s_j) v_j in p^a Z_p`. Therefore the compatible lattice has normalized
Haar volume

\[
\boxed{\operatorname{vol}_p(K_{y,a})
 =p^{-I_p(a)},\qquad I_p(a)=\sum_{j=1}^4\max(a-s_j,0).}
\]

Equivalently, modulo `p^a` it contains `p^(sum_j min(a,s_j))` coefficient
vectors out of `p^(4a)`. The number `I_p(a)` counts resolved base-p digits of
the declared four-parameter space. Calling it Shannon information would require
a specified prior; no such statistical interpretation is assumed here.

**Proof:** each coordinate condition admits exactly the ideal
`p^max(a-s_j,0) Z_p`. Haar volume multiplies across these declared coordinate
factors; the unimodular transformations preserve Haar volume. This is a
coordinate theorem, not independence of the actual source's prime reports.

For the original Fibonacci clocks the independent all-minors audit gives:

| p | Smith exponents of normalized innovation chart | I_p(a) |
|---|---|---|
| 2 | (0,2,6,15) | a+(a-2)_+ +(a-6)_+ +(a-15)_+ |
| 3 | (0,0,0,1) | 3a+(a-1)_+ |
| 5 | (0,0,0,0) | 4a |
| 7 | (0,0,0,0) | 4a |
| 11 | (0,0,0,1) | 3a+(a-1)_+ |

Here `(t)_+=max(t,0)`. At one-digit binary resolution only one of four
directions is visible; additional directions become visible only as precision
crosses2,6,15. At11, the forward or retrospective rank repair restores four
directions already at the first digit. At7, polar normalization is essential
even though the resulting chart has no inverse precision loss.

The valuations of successive determinantal divisors independently establish the
Smith exponents. For2 these are `(0,0,2,8,23)` including the order-zero divisor;
their successive differences are `(0,2,6,15)`. They agree with the exact inverse
loss15. The audit receipt records every prime and the repaired tuple.

The later common repair supplies an even cleaner reference. For four consecutive
clocks beginning at `n=2 mod3`, `n!=0 mod5`, the **integer** row-cleared matrix
has Smith form `(1,4,64,2048)`. Hence every odd prime has `I_p(a)=4a`, while
the binary count is

\[
I_2(a)=a+(a-2)_++(a-6)_++(a-11)_+.
\]

This common chart completes within9future source ticks. It is an exact
arithmetic-resolution improvement, with its row scaling and fifth-channel
precision cost still charged. It does not turn coefficient-space volume into
the empirical time distribution of the source phase.

The [all-clock closure theorem](BINARY_CLOSURE.md) proves that this common
integer row lattice already contains every row-cleared integer-clock source
innovation. Thus at uniform fixed congruence precision, no number of additional
innovation clocks shrinks its compatible coefficient fiber further. This is
stronger than merely testing many later clocks. It follows from cubic Newton
interpolation and the exact lattice determinant. The source-only eleven-digit
binary loss is unavoidable in this full innovation family for arbitrary unknown
coefficients; it is not a lower bound for the full observer after adding a known
seed, its terminal-state readout, a stronger prior, or other observations.

**Precision units matter.** This volume uses normalized rows `p^e_i C_i` at
precision `a`. The required accuracy of a raw pole observation must be
transported through its factor `p^e_i`. These are not free extra digits.
The fifth seed channel has a separate, sometimes much larger, inverse budget.

## 3. Retaining an atlas gives genuine knowledge monotonicity

If two retained readouts impose lattices `L_1,L_2` of compatible differences,
the combined history imposes `L_1 intersect L_2`. Thus adding a sound observation
cannot enlarge the compatible set. This is the precise monotonicity statement.

A newly chosen four-row sub-chart can have worse conditioning at another prime.
For example, the ordinary11repair changes the binary innovation debt from15
to16 and the ternary debt from1to2. That does not erase knowledge if the old
reports remain available. It means the new sub-chart alone is a worse decoder
for those places. The observer therefore retains an atlas of prime-specific
bases on one causal journal rather than declaring one best matrix for every
place. These views share provenance and are not independent evidence.

## 4. Real Jacobian volume and the two-dimensional Fibonacci surface

In fixed real parameter and readout units, `|det C|` measures the four-dimensional
volume response to coefficient perturbations. This is why separated Fibonacci
clocks improve `n^-16` to `n^-10`; other separated proportional schedules do too.
It is a sensitivity/latency result. Rescaling the readouts rescales this volume,
and a large determinant need not bound the worst singular direction.

For the distinct polynomial Fibonacci readout

\[
w(a,b)=(a^4,a^3b,a^2b^2,ab^3,b^4),\qquad B=A^2,
\]

the genuine state Jacobian is the five-by-two matrix `Dw`, and the exact
connection to `T=Sym^4(B)` is the chain rule

\[
Dw(Bv)B=T\,Dw(v).
\]

Over the reals its rank is two at every nonzero `v`, and zero at the origin.
For `a!=0`, the first two rows have minor `4a^6`; for `b!=0`, the last two
rows have minor `4b^6`. The map also identifies `v` and `-v`. Thus five
linearly independent polynomial functions can observe a two-dimensional state
surface without supplying five independent state directions. The mod2
derivative has additional degeneracies; real differential rank must not be
silently transported to that characteristic.

This is compatible with the older function-space knowledge volume
`span(1,u,...,u^m)`: its dimension counts available functions in an explicitly
specified source measure, not the intrinsic dimension of each individual state.
Neither a growing function space nor a nonsingular coefficient Jacobian forces
the selected chronological phase law to be Haar. That final assertion requires
the signed source estimate in FRAME_AGREEMENT.md.
