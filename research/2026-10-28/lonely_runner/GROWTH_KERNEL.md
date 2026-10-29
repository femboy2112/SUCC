# Actual-source interval geometry and upper-half cubic growth in Lean

This addition formalizes a complete upper-half growth theorem from real-time
coverage. It does not formalize the unrestricted Gamma theorem, its imported
one-entry classification, the sharp periodic occupancy estimate, or the new
unrestricted quadratic paper bound. The existing four formal modules are
unchanged. The new source is `formal/LonelyRunnerGrowth.lean`.

## Exact theorem and definitions

Define

\[
\operatorname{Bad}(v,\delta,t)\iff
\exists k\in\mathbb Z:\ |vt-k|\le\delta,
\]

and, for a finite integer source V,

\[
\operatorname{Covers}(V,\delta)\iff
\forall t\in[0,1]\ \exists v\in V:
\operatorname{Bad}(v,\delta,t).
\]

The definitions in Lean quantify over real time and integer windings. They
are not finite-sample predicates. Define the retained source by filtering the
integer interval `[1,n-1]` to remove exactly r and s.

**KG-01, `upper_half_cubic_growth`.** For all integers n,r,s,w1,w2 with

\[
n\ge5,\quad 1\le r<s\le n-1,\quad n-1<2r,\quad n\le w_1<w_2,
\]

if the actual source
`([n-1] minus {r,s}) union {w1,w2}` covers at radius `1/n`, then

\[
\boxed{w_2<3n^3.}
\]

The same source assumptions separately yield

\[
w_2\le2(n-1)w_1,
\qquad
w_1<\frac{3r(n-1)}{n-r}.
\]

These are unconditional implications from the stated original-source cover.
No gap, endpoint certificate, occupancy bound, measure law, Lonely Runner
conjecture, or classification is hidden in their hypotheses. The earlier
full upper-half one-insertion-hole theorem is imported as a proved Lean
declaration, not as an assumption or a new axiom.

This geometric first-speed bound differs from the sharper density expression
in the earlier paper proof. Formalization of this result must not be reported
as kernel verification of that different expression.

## KG-02: construct a labelled gap from a real source point

Let V be any nonempty finite set of positive integer speeds, all at most M
except possibly one declared speed w, with `1<=M<=w`. Suppose a real
`t0 in [0,1]` is strictly farther than `1/n` from every integer for every
speed in V, where `n>=3`. For each v set `k_v=floor(v*t0)` and form

\[
L_v=\frac{nk_v+1}{nv},\qquad
R_v=\frac{n(k_v+1)-1}{nv}.
\]

The actual strict separation and the floor inequalities imply
`L_v<t0<R_v`. Finiteness gives a source label u maximizing L and a source
label v minimizing R. Put `a=L_u`, `b=R_v`. The formal result proves

\[
0\le a<t_0<b\le1,
\quad b-a\ge\frac1{nwM},
\]

and every real point of `(a,b)` is good for every declared source speed.
It also exports the actual endpoint labels and integer windings. A supplied
unlabelled interval or numerical margin is not substituted for this
construction.

The spacing proof explicitly distinguishes equal endpoint speeds. For
different u,v, cancel the common factor n first; the positive numerator is
an integer over denominator `nuv`, with `uv<=wM`. For equal endpoint speeds
the denominator is `nu`, and `u<=wM`. Using `nu^2` in this second case would
lose the claimed bound. This branch is formalized rather than dismissed by
an implicit distinctness assumption.

The general theorem `inserted_speed_bound_from_hole` deliberately retains
the hypothesis that such a real uncovered point exists. It proves the
second-speed bound from that hypothesis and actual coverage. The final
upper-half result supplies that point from `upper_half_one_insertion_hole`.
An unrestricted source theorem would still need its unrestricted point
existence proof; the formal result does not assert that missing implication.

## KG-03: actual one-band and two-band interval bounds

For `v>0`, `delta<1/2`, and `a<b`, suppose every real point of `(a,b)` belongs
to `Bad(v,delta)`. Then a single integer winding k satisfies

\[
k-\delta\le va,\qquad vb\le k+\delta,
\]

so `b-a<=2*delta/v`. The proof picks a band covering the interval midpoint.
If the interval crosses either edge of that band, an explicitly constructed
point lies in the open good region before the adjacent band. This contradicts
actual coverage. No continuity or connectedness premise is assumed from the
user, and closed endpoint equality is preserved.

For two positive speeds, suppose

\[
\frac{2\delta}{v_2}<\frac{1-2\delta}{v_1},
\]

and their bad sets cover `(a,b)`. If no first-speed band meets the interval,
the one-band result applies to the second speed. Otherwise select one
first-speed band meeting it. The interval cannot extend more than
`2*delta/v2` beyond either edge: such an extension would create a
first-speed-good subinterval longer than a second-speed bad band. Reflection
handles the left edge. Therefore

\[
b-a\le\frac{2\delta}{v_1}+\frac{4\delta}{v_2}.
\]

At `delta=1/n`, `n>=5`, and `w2>w1>0`, the gap condition holds, and strict
ordering of the speeds gives

\[
b-a<\frac6{nw_1}.
\]

This is an actual geometric cover theorem. It is not a measure-theoretic
occupancy assertion with an unproved conversion to covers.

## KG-04: close the source growth argument

The retained upper-half source is good throughout the real interval centered
at `1/r` with radius

\[
\rho=\frac{n-r}{nr(n-1)}.
\]

The proof transports the already verified integer separation at `1/r` by
the triangle inequality and the speed bound `i<=n-1`. It proves that this
interval lies inside `[0,1]`. Actual full-source coverage therefore forces
the two inserted speeds to cover its whole interior. The two-band result
gives `2*rho<6/(n*w1)`, hence the displayed first-speed bound.

Since `r<=n-2`, that bound implies
`2*w1<3*(n-2)*(n-1)`. Combining it with the actual-source second-speed
bound gives

\[
w_2<3(n-2)(n-1)^2<3n^3.
\]

All source construction, integer-to-real casts, endpoint labels, strict
inequalities, case splits, and final polynomial inequalities are checked in
the new Lean source. The construction does not require primitive speed gcd
or replace the original zero shifts by adjustable phases.

## Authority controls and limitations

The new serial audit `scripts/check_lonely_runner_growth_lean.py` verifies
the pinned dependency revisions and tracked-source cleanliness, builds
Deletion, TwoEntry, and Growth in a separate temporary directory, and exports
the complete kernel type and axiom list of each of the 18 new declarations.
It rejects zero, missing, duplicate, unexpected, or nonstandard-axiom exports
and checks source hashes again after compilation. The allowed foundational
axioms are exactly `propext`, `Classical.choice`, and `Quot.sound`.

Three paired controls compile the exact valid statement and reject a changed
conclusion: halve the single-band width, double the integer-spacing lower
bound, or replace the cubic upper bound by zero. The first two have immediate
exact semantic countermodels: a whole radius-1/3 bad band at speed 1, and
consecutive numerators 1 and 2 over denominator 3. The last is contradicted
by the known upper-half cover at n=74, removed speeds 70 and 72, inserted
speeds 140 and 144, already replayed in Gamma. Compiler rejection alone is
a statement-transport check; these countermodels explain why the changes
are mathematically invalid.

Six focused Python tests verify export rejection and exact control arithmetic,
including retention of the explicit general-hole hypothesis and its absence
from the unconditional upper-half cubic theorem. They do not substitute for
Lean compilation. Local kernel evidence is not hosted-CI evidence. Correlated
same-model reviews are not external independent witnesses.

The completed guarded local replay is saved in
`receipts/kernel-growth/kernel-observation.json` with its compiler logs. It
reports `KERNEL_CHECKED`, all 18 exact theorem exports, all three paired
controls passing, and unchanged proof/audit source hashes. Only the three
permitted standard axioms occur. The six focused Python tests also passed;
compilation of the new Python files and the whitespace check passed.

The result is an additional formal proof of a restricted consequence; the
located prior upper-half classification is stronger mathematically. Neither
that known classification nor the unrestricted cubic or quadratic paper
theorem is promoted to kernel status here. Academic novelty is not claimed.

## Replay and falsification

```sh
python -m unittest tests.test_lonely_runner_growth_authority -v
python scripts/check_lonely_runner_growth_lean.py \
  --output /tmp/succ-growth-replay \
  --dependency-project /home/leah/SUCC/formal/mathlib_bridge
```

The dependency-project path denotes the existing pinned cache and is read-only;
another clean cache at the same locked revisions is equally admissible. The
output path is arbitrary and contains all observations. No old archive is
rewritten by this replay.

Next falsification: inspect the exact exported type of
`upper_half_cubic_growth`, compare its source set and all integer quantifiers
against KG-01, challenge the same-speed endpoint branch, and replay the
negative controls in a fresh pinned environment. Extending kernel authority
to all deletion pairs requires the unrestricted hole lemma; extending it to
the new quadratic bound additionally requires its unit-lifting and source
phase arguments.
