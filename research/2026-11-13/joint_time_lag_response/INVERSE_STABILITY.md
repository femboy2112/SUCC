# Quantitative reconstruction from complete adjacent-lag records

**Status: PROVED LOCAL, elementary paper proof.** A fixed-precision,
clock-resolved lag record recovers a finite signed Fourier mean with an
explicit error of order `1/N`, after resolving a fifteenfold phase ambiguity.
This is a stable inverse theorem, not an arithmetic cancellation estimate.
It applies to the authentic BBP source, but also to wrong seeds. It proves
neither R0 nor normality for pi.

## 1. Source, instruments and provenance

Write `T=R/Z`, `||t||_T=min_(j in Z)|t-j|`, and
`e(t)=exp(2 pi i t)`. The circle metric is measured in **turns**, not radians
or chord length. Let `X_n=16^n x` and `Y_n=16^n y`, for real `x,y`.
Their unit-frequency adjacent-lag outputs are

\[
 L_n(x)=e(X_{n+1}-X_n)=e(15\,16^n x).
 \tag{IS-1}
\]

The observed data retain each absolute clock. Averages of `L_n`, their
magnitudes, an unlabeled multiset, or a sparse subsequence are different
instruments and do not satisfy the hypothesis below automatically.

For the original four-pole forcing, keep every source term and write

\[
 U_n(s)=16^ns+U_n(0),\qquad
 U_n(s)+T_n=16^n(s+\pi/16).
 \tag{IS-2}
\]

The complete neutral-character bank and its exact fifteenfold kernel are
already proved in **OB-02** of unmerged draft
[PR #610](https://github.com/femboy2112/SUCC/pull/610), at head
`00897c94289fc94a491429d4054d548afe20b7c2`,
[OBSERVER_BRIDGE.md](https://github.com/femboy2112/SUCC/blob/00897c94289fc94a491429d4054d548afe20b7c2/research/2026-11-13/leah_gamma_twist/OBSERVER_BRIDGE.md).
That exact file and its OB-02 proof were read for this note. The donor was
open, draft and unmerged when inspected. It is an archival input, not a
theorem silently integrated into main.

The quantitative extension here is a finite-horizon modulus for the signed
target, the sharp admissible lag-error threshold, and a control showing
that averaged accuracy cannot replace clock-resolved accuracy. The proof is an
elementary positive-expansivity/phase-unwrapping argument for multiplication
by 16. We make no worldwide priority claim for that classical mechanism,
and do not count the inherited fifteenfold kernel as a new result.

## 2. Uniform lag accuracy forces exponentially accurate initial data

**Theorem IS-3.** For every integer `B>=0`, integer `N>=1`, real `x,y`,
and real `0<=epsilon<1/17`, suppose

\[
 \left\|15\,16^{B+n}(x-y)\right\|_{\mathbb T}
 \le\epsilon\qquad(0\le n<N).
 \tag{IS-3a}
\]

Set `delta=16^B(x-y)`. There is a unique `k` modulo 15 such that

\[
 \boxed{
 \left\|16^n\delta-\frac{k}{15}\right\|_{\mathbb T}
 \le\frac{\epsilon}{15\,16^{N-1-n}}
 \qquad(0\le n<N).
 }
 \tag{IS-3b}
\]

For every integer target frequency `h`, define

\[
 W_{B,N}^{(h)}(x)=\frac1N\sum_{n=0}^{N-1}e(h16^{B+n}x).
\]

Then

\[
 \boxed{
 \left|W_{B,N}^{(h)}(x)
       -e(hk/15)W_{B,N}^{(h)}(y)\right|
 \le\frac{32\pi|h|\epsilon}{225N}(1-16^{-N}).
 }
 \tag{IS-3c}
\]

**Proof.** Let `u_n` be the unique representative of `15*16^n*delta`
in `[-epsilon,epsilon]`. It exists by IS-3a and is unique because
`epsilon<1/2`. Since `16u_n-u_(n+1)` is an integer and

\[
 |16u_n-u_{n+1}|\le17\epsilon<1,
\]

that integer is zero for every `0<=n<N-1`. Thus
`u_n=16^n u_0` and `|u_0|<=epsilon*16^(-(N-1))`.
Choose an integer `j` such that `15delta=j+u_0`, and let `k=j mod15`.
As `16^n=1 mod15`,

\[
 16^n\delta\equiv k/15+u_n/15\pmod1.
 \tag{IS-3d}
\]

This proves IS-3b. The fifteen possible residues `k/15` have minimum
separation `1/15`; the error radius in IS-3b is smaller than `1/255`, so
no second `k` is possible. In particular,

\[
 |e(h16^{B+n}x)-e(hk/15)e(h16^{B+n}y)|
 \le 2\pi |h|\,|u_n|/15.
\]

Sum, divide by `N`, and use

\[
 \sum_{n=0}^{N-1}16^{-(N-1-n)}
 =\frac{16}{15}(1-16^{-N}).
\]

The result is IS-3c. The proof also covers `N=1`; no transition is then
used. For `h=0` both sides of the target difference are identically zero.
There is no exchange of limits. The inequality holds for each stated
`B,N,x,y,epsilon,h`. End of proof.

The surprising conditioning is specific to **exact radix dynamics**.
For a general path, adjacent phase errors can accumulate with time.
Here exact expansion plus the no-wrapping threshold forces errors at early
clocks to be exponentially smaller than those at the final clock. Summing
the allowed errors costs a geometric series, not `N` times the largest
error. Altering the radix law or adding unbudgeted process noise invalidates
this deduction.

## 3. One coarse absolute anchor resolves the target's global phase

**Corollary IS-4.** Under IS-3a, the additional present-time anchor

\[
 \|16^B(x-y)\|_{\mathbb T}\le1/30
 \tag{IS-4a}
\]

forces `k=0`. Consequently IS-3c directly bounds
`|W_(B,N)^(h)(x)-W_(B,N)^(h)(y)|`.

**Proof.** At `n=0`, IS-3b and the triangle inequality give

\[
 \|k/15\|_{\mathbb T}
 \le1/30+\epsilon/(15\,16^{N-1})<1/15.
\]

Every nonzero residue `k mod15` has circle distance at least `1/15`
from zero. Hence `k=0`. More generally an anchor error `beta` suffices
whenever

\[
 \beta+\epsilon/(15\,16^{N-1})<1/15.
 \tag{IS-4b}
\]

For the R0 target set `h=1` and `N=B>=1`. The real shell defects
`A_B(x)=1-Re W_(B,B)^(1)(x)` then obey

\[
 |A_B(x)-A_B(y)|
 \le\frac{32\pi\epsilon}{225B}(1-16^{-B}).
 \tag{IS-4c}
\]

This transfers a separately proved signed margin from an admitted reference
orbit to the source. It does not produce that margin. Without the anchor,
the finite rotation `e(hk/15)` can change R0 even when all relative
observations agree exactly, as OB-02 already demonstrates.

### A finite noisy-record version with explicit acquisition costs

Suppose two exact candidate radix orbits each fit one record of the `N`
adjacent-lag phases within `tau` turns **at every recorded clock**. Suppose
they also each fit one common absolute phase record at clock `B` within
`a` turns. If

\[
 0\le\tau<1/34,\qquad 0\le a\le1/60,
\]

the circle triangle inequality gives IS-3a with `epsilon=2tau` and
IS-4a. Thus the diameter of their possible signed means is at most

\[
 \boxed{
 \frac{64\pi|h|\tau}{225N}(1-16^{-N}).
 }
 \tag{IS-4d}
\]

All record errors include computation, enclosure, phase conversion and
instrument error; this theorem does not acquire the record for free.
The record may be inconsistent with every exact orbit. A separate
feasibility certificate is required before reporting a nonempty inverse
set. Even a nonempty inverse set of vanishing target diameter need not
have a small mean: exact observation of a coherent orbit reconstructs a
coherent mean.

The finite theorem allows arbitrary integer `h`, with its displayed factor
`|h|`. A vanishing reconstruction error with a changing frequency schedule
requires `|h|*epsilon/N -> 0`; no uniform unrestricted frequency-band
assertion is made.

## 4. The threshold 1/17 is sharp, even with a coarse anchor

**Counterexample IS-5.** Set `B=0`, `y=0` and `x=delta=1/255`.
Since `256delta=delta mod1`, the orbit of `delta` alternates between
`delta` and `16delta`. Moreover

\[
 15\,16^n\delta\equiv(-1)^n/17\pmod1.
\]

Every adjacent-lag error is therefore exactly `1/17` turns. The anchor
`||delta||_T<1/30` holds, but the lift at the first transition has
`16u_0-u_1=1`, so the no-wrapping proof fails exactly at its threshold.

For every even `N`,

\[
 W_{0,N}^{(1)}(\delta)
 =\frac{e(1/255)+e(16/255)}2
 =e(1/30)\cos(\pi/17).
 \tag{IS-5a}
\]

This mean stays uniformly away from **every** fifteenth root of unity.
Indeed its argument is halfway between the roots `1` and `e(1/15)`.
Put `r=cos(pi/17)>0` and `alpha=pi/15`. Every root has principal angular
distance at least `alpha` from the mean's ray. Therefore

\[
 \begin{split}
 |e(1/30)r-e(k/15)|^2
 &\ge1+r^2-2r\cos\alpha\\
 &=(r-\cos\alpha)^2+\sin^2\alpha
 \ge\sin^2(\pi/15)>0.
 \end{split}
 \tag{IS-5b}
\]

Thus an `O(1/N)` estimate of the form IS-3c is impossible at
`epsilon=1/17`, even with IS-4a. The same example excludes every weaker
threshold `epsilon>=1/17`. This is a rational period-two control, not a
claim about pi and not an alternative literal-zero BBP trajectory.

## 5. One missed clock can permanently hide a different mean

**Counterexample IS-6.** Set `B=0`, `x=0`, and `y=1/240`.
The coarse initial anchor holds because `1/240<1/30`. At the first clock
the adjacent-lag discrepancy is `15y=1/16`, exceeding `1/17`; at every
subsequent clock it is zero:

\[
 \|15\,16^n y\|_{\mathbb T}=
 \begin{cases}1/16,&n=0,\\0,&n\ge1.\end{cases}
 \tag{IS-6a}
\]

For every finite `p>0`, its normalized error tends to zero:

\[
 \left(\frac1N\sum_{n=0}^{N-1}
          \|15\,16^n y\|_{\mathbb T}^{p}\right)^{1/p}
 =\frac1{16N^{1/p}}\longrightarrow0.
 \tag{IS-6b}
\]

Only one clock in the entire infinite record is bad. Nevertheless,
`16^n y=1/15 mod1` for all `n>=1`, and

\[
 W_{0,N}^{(1)}(0)=1,\qquad
 W_{0,N}^{(1)}(y)
 =\frac{e(1/240)+(N-1)e(1/15)}N
 \longrightarrow e(1/15)\ne1.
 \tag{IS-6c}
\]

For every fixed positive lag `ell`, the entire relative phase row after
the first clock is also identical: both outputs equal one for `n>=1`.
Thus any finite family of lag rows has the same limiting empirical
response in the two systems. The later shell R0 defects differ: one is
zero, the other is `1-cos(2 pi/15)>0`.

This refutes replacing IS-3a by a vanishing averaged error, or by accuracy
outside a zero-density set of bad clocks, while retaining only a coarse
anchor at the initial clock. It does **not** refute a new coarse anchor at
each later shell start: at every `B>=1`, the two present states are
separated by `1/15`, so IS-4a then fails. The exact literal-zero source pin
likewise rejects the wrong-seed control. This exception is the mechanism:
one unobserved branch jump can move the orbit into a different permanent
fifteenth-root phase class.

## 6. Exact transfer to same-forcing raw BBP observations

For any fixed real seeds `s,t`, the exact source relation IS-2 gives

\[
 U_n(s)-U_n(t)=16^n(s-t),
\]

and hence

\[
 [U_{n+1}(s)-U_n(s)]-[U_{n+1}(t)-U_n(t)]
 =15\,16^n(s-t).
 \tag{IS-7}
\]

The forcing cancels in this **comparison of two same-forcing paths**.
Adding the common `T_n` cancels in their state differences and in their
relative adjacent-lag differences as well. Therefore IS-3 through IS-4
apply, with the same constants, to the means of either

\[
 e(hU_n(s))\quad\hbox{or}\quad e(h[U_n(s)+T_n]),
\]

compared with the corresponding mean for seed `t`. For raw means this
follows directly from the termwise argument after IS-3d; no homogeneous
radix recurrence for an individual raw path is falsely assumed. The
reference and source must use the **same forcing** and the same completion.
Mutated source terms do not cancel by IS-7.

There is no tail charge for this same-forcing two-seed comparison.
Comparing raw and completed responses **within one fixed seed** is a
different operation and does incur a tail budget; see
[SOURCE_TRANSPORT.md](SOURCE_TRANSPORT.md). These two kinds of transport
must not be conflated.

The hostile circle controls above are same-forcing realizable by taking
`s=x-pi/16` and `t=y-pi/16` in IS-2. They preserve the four poles but
change the distinguished seed. The complete original contract
`U_0=0` plus the entire forcing already specifies one trajectory, so
there are no two distinct trajectories satisfying that full contract.
Approximate observation stability is a different question from exact
source authentication, and neither is signed cancellation.

## 7. Finite horizons and the all-horizons boundary

IS-3 is uniform in the explicitly quantified finite data: for each `B,N`
it permits a different pair `x,y` and a different residue `k`. It does
not identify one fixed seed from one finite observation packet.

If **one fixed pair** `x,y`, one fixed `B` and one fixed
`epsilon<1/17` satisfy IS-3a for every `N`, then

\[
 \|15\,16^B(x-y)\|_{\mathbb T}
 \le\epsilon16^{-(N-1)}\quad\hbox{for every }N,
\]

so `15*16^B(x-y)` is an integer exactly. The pair differs at the present
clock by one of the fifteen phase classes. With IS-4a the present states
are equal modulo one, and every future phase is equal. At `B>0` the
original seeds may still differ by an integer multiple of `16^(-B)`;
those past-prefix aliases are not resolved by future circle observations.
At `B=0`, an integer seed difference is likewise invisible to every
circle character and must be excluded by the unwrapped source pin if
literal seed identity is the goal.

Consequently a fixed, exactly normal reference cannot approximate every
growing clock-resolved record under these hypotheses without having the
same future circle orbit after anchoring. A varying reference family
could still be useful computationally, but needs an independently proved
signed estimate for that family. Merely naming such a family does not
move the pi cancellation problem.

## 8. Scope, claim ledger and falsifying probes

| Claim | Hypotheses retained | Status | Boundary |
|---|---|---|---|
| Exact fifteenfold neutral-bank kernel | Full declared neutral bank | Inherited, OB-02 | Extra absolute reference needed for R0 |
| IS-3 signed target inverse modulus | Exact radix difference, every clock, epsilon<1/17 | Disclosed by proof | Does not make the recovered target small |
| IS-4 anchor and noisy-record modulus | Present anchor, all measurement errors paid | Disclosed by proof | Feasibility and acquisition are separate |
| IS-5 sharp threshold | Rational period-two control | Disclosed by exact counterexample | Wrong seed, not a pi counterexample |
| IS-6 failure of averaged accuracy | One bad initial clock, coarse initial anchor | Disclosed by exact counterexample | A new later anchor separates the pair |
| IS-7 same-forcing applicability | Identical source and completion | Disclosed by exact subtraction | Not valid for free source mutants |
| Uniform signed saving on the authentic orbit | Literal U_0=0 and all sufficiently late shells | OPEN | No new arithmetic lower bound supplied |

**Next decisive probe.** Use the authenticated exact-rational BBP source
to acquire each adjacent-lag phase in a declared finite shell with rigorous
angular error below `1/34`, and a present anchor with error at most `1/60`.
Construct a nonempty feasible exact-orbit set and compare its target
enclosure against direct certified Fourier evaluation. The predicted
diameter bound is IS-4d. Controls must include the exact fifteenth-root
aliases, IS-5 at the threshold, and IS-6 with its single exception.
An enclosure violating IS-4d while satisfying every hypothesis falsifies
the implementation or proof. A smaller enclosure validates finite target
access only. A small mean observed on finitely many shells remains
ambiguous for R0; the verdict-changing analytic obligation is a proved
uniform signed margin, not a successful reconstruction.

This file supplies a complete checkable derivation. Computational checks
and repository validation are recorded separately by the research-round
receipt; no unexecuted run, external referee, Lean proof or independent
research-group verification is claimed here.
