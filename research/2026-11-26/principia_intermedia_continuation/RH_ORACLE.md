# RH as a reconstruction oracle for observer continuation

**Date:** 2026-11-26. **Purpose:** use the external Alpöge–Claude argument to
test the mathematical adequacy of Principia Intermedia. This document does
not assert a new SUCC proof of RH. Current proof-checking statements below are
reports from their named sources, not checks run in this research round.

## 1. Primary-source status and current update

### Published proof and external machine checks

[Michael Rubinstein's Waterloo index](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
reports the November 20 Alpöge–Claude announcement and successful checking of
the original Lean development. Its November 26 update reports that the compact
rewrite's 794 modules, axiom audit, kernel replay and statement-comparing
`lake comparator --paranoid` checks passed. The linked rewrite was posted
November 25. Waterloo notes that its comparator run lacked its usual sandbox;
it links Sutherland's sandboxed checks.

[Andrew Sutherland's MIT verification page](https://math.mit.edu/~drew/shortgrh/)
identifies compact/readable source `lsernau/grh-lean` at
`72fead102f663d5c7a407964a13dc0cf9d977207`. It reports sandboxed comparator
success for both editions, including two compact-edition runs, and a separately
checked derivation of Schoenfeld's explicit prime-error bound. It distinguishes
an interrupted memory-limited readable-edition attempt from the completed
checks. We inspected these reports; we did not reproduce their builds, exports,
axiom audits or kernel runs.

[Levent Alpöge's original announcement](https://alpo.ge/remark.pdf), pp. 1–2,
describes a multiplicity strategy using chained theta lifts, with arithmetic
divisibility and analytic size playing complementary roles. That announcement
is a guide to the construction, not a replacement for its full mathematical
dependencies.

### The precise boundary of the human-readable guide

[Rubinstein et al., *The Alpöge–Claude proof of the Riemann hypothesis explained
for the Riemann zeta function*, v2, November 22](https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf)
is a 265-page working guide. Its §III.11 reduces the main inequality (M) at one
scale to **H0–H11**. **H12** requires compatible data, scale-independent
constants and suitable auxiliary primes throughout intervals
\([Z,Z^{3/2}]\) with arbitrarily large \(Z\). The guide does not prove these
thirteen hypotheses outright. Theorem M and Corollary M9 expose the error
shape \(x/m+xm/k+m+k/n^2\); Corollary M11 supplies the conditional RH
deduction. Relevant preceding sections treat local divisibility (§III.5–6),
analytic size (§III.7), rank (§III.8) and denominator control (§III.9).

## 2. What the oracle asks of our own mathematics

The following is **our reconstruction analysis**, not a claim that the RH
proof uses SUCC or the absolute-value path in this round.

A faithful observer theorem should preserve a proof-bearing object while
different instruments evaluate it. The checks below are therefore stricter
than matching a diagram, a scalar zero, or a qualitative “balance” story:

1. **Common source.** Identify one object and the actual maps by which each
   observer obtains its report. Matching labels or numerically similar outputs
   do not establish this identification.
2. **Retained arithmetic structure.** If a local observer reports divisibility,
   identify its integral ring, coordinate system, valuation and exceptional
   denominators. A change of normalization must carry those data forward.
3. **Same-object analytic size.** The upper bound must concern the same
   nonzero arithmetic witness after explicit norm, period and coordinate
   transport. An upper bound on a different Gaussian model cannot close it.
4. **Independent constraints.** Repeated labels and copied null equations do
   not multiply rank or valuations. State what new independent condition each
   continuation step adds.
5. **Completion with the needed quantifiers.** Finite path existence or a
   successful example at an isolated scale does not supply uniform data on
   every point of a required late interval. The exact scale dependence is part
   of the theorem, not a bookkeeping detail after it.

PS-01 in [ARITHMETIC_PLACE_SEAM.md](ARITHMETIC_PLACE_SEAM.md) now supplies an
honest example of continuous source-coherent observers and a compulsory common
log-null seam. PS-03 recovers hidden endpoint readouts from retained oriented
germs. PS-04 proves that even all smooth jets can be null at such a seam while
the endpoint observers differ. Those results clarify the kind of observation
and regularity being used; they do not produce arithmetic multiplicity for free.

PS-05 supplies a distinct quantitative test. If a common nonzero rational
witness \(x\) has an authenticated clearing denominator \(D\), certified
prime-power divisor \(M\mid Dx\), and a proved bound \(|x|\le U\), then

\[
M\le DU.
\]

A strict opposite inequality excludes the witness. This is a genuine
arithmetic obstruction: it requires nonvanishing, integral divisibility and
real size on the same retained object. A topological zero crossing alone
does not provide any of those quantities. The determinant version in PS-05
includes all coordinate factors explicitly.

## 3. Keep the two obligation dictionaries distinct

SUCC's **M4–M10** labels predate this round and name native reconstruction
tasks. They are not the external guide's **H0–H12** numbering and are not
asserted to be a one-to-one translation of it.

The native labels below come from pinned
[Principia Genesis RH_RECONSTRUCTION.md](https://github.com/femboy2112/SUCC/blob/c5757d48a6788e1513e4276b111f7cdad075055f/research/2026-11-24/principia_math_of_math/RH_RECONSTRUCTION.md),
especially its M0–M11 table. This round leaves these native obligations open.

| Native SUCC label | Concrete reconstruction still required |
| --- | --- |
| M4 | Actual theta-kernel integral structure in authenticated CM coordinates |
| M5 | Actual period-map/lift construction with legal compositional transport |
| M6 | Nonzero common minors with accumulated source-derived divisibility |
| M7 | Real Petersson/period norm, covolume and normalization bounds on those maps |
| M8 | Enough independent images, with the actual rank/trace argument |
| M9 | Source-specific Galois, conductor and denominator losses |
| M10 | Complete quantitative main inequality with permitted parameter and scale choices |

The new source-coherent observer-path interface can organize these tasks and
reject inadmissible identifications. It does not certify their analytic or
arithmetic hypotheses. Likewise, reported verification of the external proof
is a reference result; it is not a proof that the native SUCC constructions
already implement its indispensable maps.

## 4. Symmetric-polynomial hostile control

This elementary counterfeit tests whether a proposed observer/seam argument
has silently replaced source arithmetic by functional symmetry.

Define the explicit polynomial

\[
P(s)=\bigl((s-\tfrac14)^2+1\bigr)
      \bigl((s-\tfrac34)^2+1\bigr).
\]

It satisfies the exact reflection and reality relations

\[
P(1-s)=P(s),\qquad P(\bar s)=\overline{P(s)}.
\]

Its zeros are
\(\tfrac14\pm i\) and \(\tfrac34\pm i\), all away from the symmetry
axis \(\Re s=1/2\). Yet its value on that axis is strictly positive:

\[
P(\tfrac12+it)
=\left|\left(\tfrac14+it\right)^2+1\right|^2
=\left(\tfrac{17}{16}-t^2\right)^2+\tfrac14 t^2>0
\quad(t\in\mathbb R).
\]

**Proof.** Reflection exchanges the two factors; real coefficients give
conjugation symmetry. Each quadratic factor gives its displayed roots.
On the axis the factors are conjugates, yielding the squared-modulus formula.
Both summands can vanish only if \(t=0\) and \(17/16=0\), which is impossible.
\(\square\)

Thus symmetry, conjugation pairing, and even positive values on the central
axis do not force all complex zeros onto it. A path between paired zero
locations crosses the symmetry axis, but the crossed point need not be a zero
of the polynomial. This distinguishes a zero of an observer's signed
position coordinate from a zero of the function under study.

This polynomial is an explicitly marked hostile model, not the zeta function,
an Euler-product source, or an input using actual nontrivial zeta zeros. Its
purpose is to make a symmetry-only inference fail before it reaches an RH
claim. Any successful source-specific theorem must expose the hypothesis
that this control violates.

## 5. Steelman, crucible, refined verdict

**Steelman.** Two apparently distant observers may be views of one lawful
arithmetic construction. A source-retaining continuation can expose a seam
where their relative readout is null while their oriented history retains
nontrivial information. The compulsory place seam supplies a literal theorem
of this kind on rational arithmetic.

**Crucible.** Test four different failures: magnitude-null versus equality
information; smooth flat jets versus analytic uniqueness; changed-source or
unpaid-normalization capacity; and symmetry-axis crossing versus zero location.
Each has an explicit proof or exact countermodel in this dossier. They are
different obstructions and must not be collapsed into one “coherence score.”

**Refined verdict.** Observer continuation and seam crossing are established
within their declared domains. For an RH-strength or source-specific BBP
consequence, the new work identifies the further quantitative certificate:
one authentic retained construction must supply independent arithmetic
constraints and analytic bounds that cannot coexist under the proposed
counterhypothesis. The named native M4–M10 maps and scale requirements remain
the next reconstruction targets. No status promotion is obtained from the
seam theorem alone.
