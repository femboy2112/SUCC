# Round V hostile bearing: periods, residuals, and escape certificates

**Status:** direct proofs below are mathematical arguments under their stated
hypotheses. Finite control receipts are separately labelled Observed. The
implementation audit is pending the assembled code. This is a same-model
adversarial decomposition, not an independent external proof certificate.

**Baseline:** SUCC `aletheia/cursed-categories-dedekind-yoneda-2026-11-10`,
`4e311d03e3ac9c3dbcbdc32477cd113f2ac0743b`; the inherited Round IV
`circle_line_observer.py` and `LR_TRANSLATION.md`. No checkout or remote file
was changed by this bearing.

## 1. The three nonrepetition statements are different

Fix a strict rational interval name `I_k` for a real `x` in `(3,4)`. Let

\[
 E_n=\begin{pmatrix}a_n&c_n\\b_n&d_n\end{pmatrix},\quad
 J_n=[a_n/b_n,c_n/d_n],\quad b_nc_n-a_nd_n=1.
\]

The endpoint updates are **right multiplication** by

\[
 L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 R=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

These notions must not be conflated:

| Statement | Sufficient hypothesis | What it does not establish |
| --- | --- | --- |
| The semantic interval pair `(I_k,J_n)` never returns | Every completed source/output update strictly decreases a positive interval potential | Aperiodicity of the output letters |
| Distinct normalized residual states never agree | The target is not algebraic of degree at most two | A new proof that pi is transcendental |
| The LR output is not eventually periodic | Irrational productivity plus the target's nonquadraticity | Normality, cancellation, random-looking behavior, or a useful uniform runtime bound |

### Counter-free potential

For the beta-matrix source, put

\[
 W_k=|I_k|=\prod_{j=1}^k\frac{j}{2j+1},\qquad
 \Phi(k,n)=\frac{W_k}{b_nd_n}=|I_k|\,|J_n|.
\]

A completed source update multiplies `Phi` by `j/(2j+1)<1/2`; an L output
multiplies it by `d/(b+d)<1`; an R output by `b/(b+d)<1`. Thus the interval
pair cannot repeat even if its explicit counters are erased. This is a strict
descent in positive rationals, which permits infinite descent. It does not
prove termination, nor does it describe each individual Python instruction.

The useful negative control is exact and decisive. Set

\[
 \alpha=\frac{9-\sqrt5}{2},\qquad f(X)=X^2-9X+19.
\]

On `[3,4]`, `f` is strictly decreasing, with `f(3)=1`, `f(4)=-1`. Rational
bisection using only the sign of `f` yields strict shrinking enclosures of
alpha. Their width, and the semantic interval potential, decrease forever.
Nevertheless the LR output is

\[
 (LR)^\infty.
\]

The initial normalized residual is
`z=(sqrt(5)-1)/2`; it satisfies `z^2+z-1=0`. L sends it to `z/(1-z)=z+1`,
and R sends it back to `z`. Hence nonreturn of intervals and return of
normalized residuals can coexist. Any inference from interval descent alone
to output aperiodicity is **Refuted** by this control.

## 2. Residual normalization: the swap is load-bearing

With `S=[[0,1],[1,0]]`, the increasing residual chart is

\[
 B_E=ES=\begin{pmatrix}c&a\\d&b\end{pmatrix},\qquad
 B_E(z)=\frac{a+cz}{b+dz},\qquad
 z=B_E^{-1}(x)=\frac{bx-a}{c-dx}>0.
\]

Although endpoint updates use L and R, their forward residual transitions are

\[
 z\mapsto\frac{z}{1-z}\quad(L,z<1),\qquad
 z\mapsto z-1\quad(R,z>1).
\]

For an output word `w` with right product `W`, the reconstruction map on the
residual is `SWS`, not `W`. For `m>n`, `B_m=B_n(SWS)` and consequently
`z_n=(SWS)(z_m)`.

If `z_n=z_m`, it is a fixed point of a nonempty positive word. A nonempty
word in L,R is not a scalar identity: a pure word has a positive off-diagonal
entry, and a mixed word has both off-diagonal entries positive. If its matrix
is `[[u,v],[s,t]]`, the fixed-point equation is the nonzero polynomial

\[
 s z^2+(t-u)z-v=0.
\]

Therefore z, and its rational Möbius image x, have algebraic degree at most
two. Contraposition proves pairwise residual nonreturn for nonquadratic x.
For pi, this imports its classical transcendence/nonquadraticity; it does not
derive that theorem from observer shape.

A rational separator between two distinct residuals is computable. Refine a
common source interval until it lies strictly inside both Farey brackets,
map its endpoints by the two increasing residual charts, and continue until
the resulting rational intervals are disjoint. The midpoint of their gap is
a separating rational probe. Totality uses the theorem of nonreturn. This
does not provide a general equality decision procedure for arbitrary
computable reals.

## 3. Candidate periods and fixed-point polynomials

Let `N>=0`, `p>=1`. Generate exactly through the first candidate block
`w[N:N+p]`, save that block, and compute its right product W. With the prefix
endpoint matrix E at N, define

\[
 F=EWE^{-1}=
 \begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
 P_F(X)=CX^2+(D-A)X-B.
\]

This global conjugation is correct with E's endpoint convention. With the
increasing residual chart, the equivalent expression is
`B_E(SWS)B_E^{-1}`. Forgetting S changes the claimed target.

Examples at the root interval `[3,4]`:

| Word | Global matrix F | Fixed-point polynomial, up to nonzero scalar | Selected limit |
| --- | --- | --- | --- |
| LR | `[[-3,19],[-1,6]]` | `X^2-9X+19` | `(9-sqrt(5))/2` |
| L | `[[4,-9],[1,-2]]` | `(X-3)^2` | 3 |
| R | `[[-3,16],[-1,5]]` | `(X-4)^2` | 4 |

An infinite mixed-word repetition selects the unique limit in the nested
Farey cylinders. For mixed W, all four entries are at least one and
`trace(W)>=3`. The discriminant `trace(W)^2-4` lies strictly between
consecutive relevant integer squares and is not a square. The selected
point is genuinely quadratic. Pure words are parabolic and select a
rational endpoint; use the primitive linear endpoint polynomial `bX-a` for
all-L or `dX-c` for all-R when a sharper certificate is wanted. The squared
fixed-point polynomial is valid but loses a factor of the small gap.

Nonprimitive periods such as `(LR)^r` must be accepted as candidate inputs;
their matrix fixed points agree with those of LR. Integer scalar matrix
representatives must not change the selected projective map. Normalize the
polynomial's gcd/sign if the interface requires a canonical certificate.

### Strict enclosure and a sound polynomial range

Refine the source until a sound rational interval for `P(I_k)` excludes zero.
For nonquadratic x, `P(x)!=0`, so convergence guarantees termination. Store
the source stage, endpoints, polynomial, and signed value interval. A
verifier must reconstruct the source stage from its finite geometric rules;
merely trusting supplied endpoints leaves the certificate unanchored.

**Mandatory mutation:** for

\[
 Q(X)=16X^2-112X+195,
\]

`Q(3)=Q(4)=3` while `Q(7/2)=-1`. Same-sign endpoint evaluations do not prove
the entire quadratic range has that sign. A correct exact range includes
the vertex when it lies inside the interval, or uses a sound interval
arithmetic enclosure. An interval-arithmetic enclosure may be wider than
the true range; that is safe and convergence eventually resolves the sign.

## 4. Predictive finite deadlines

Suppose the certificate supplies `|P(x)|>=epsilon>0`. For
`P(X)=uX^2+vX+w` and roots in `[3,4]`,

\[
 M=8|u|+|v|\ge\sup_{3\le t\le4}|P'(t)|.
\]

The mean value theorem gives

\[
 |x-\alpha_W|\ge\delta:=\epsilon/M>0.
\]

For a linear endpoint polynomial, use its exact constant derivative. The
nonzero polynomial constructed from a nonidentity candidate has a root in
the bracket, so this use never needs a zero derivative bound.

If the actual output follows r complete copies of W, both x and the
candidate periodic point lie in the cylinder `J_N W^r`. Thus any r for
which that cylinder has width **strictly less** than delta is an escape
deadline. Derive and save this deadline before inspecting the remaining
output, to distinguish prediction from fitting.

### Mixed blocks

Write the denominator row as `[b,d]`. After one mixed block,

\[
 [b',d']=[b,d]W,\qquad b',d'\ge b+d,
\]

so

\[
 \frac{|J_{n+p}|}{|J_n|}=\frac{bd}{b'd'}\le\frac14,
 \qquad |J_{N+rp}|\le\frac1{bd\,4^r}.
\]

This is a cylinder-width contraction. It is not an assertion that the
associated real map has derivative at most 1/4 at every point. Select r by
exact integer/rational arithmetic until `1/(bd*4^r)<delta`; floating
logarithm rounding must not control a rigorous strict deadline.

### Pure blocks

For W=`L^p` and W=`R^p`, respectively,

\[
 |J_{N+rp}|=\frac1{b(d+rp\,b)},\qquad
 |J_{N+rp}|=\frac1{d(b+rp\,d)}.
\]

Both tend to zero, yielding a finite deadline with exact arithmetic. The
mixed-block bound 1/4 is false for a pure block and must not be used there.

### Indexing is part of the theorem

All following positions are zero based. If the first divergence from the
infinite repetition of the saved first block occurs at j, then `j>=N+p`.
The actual p-shift mismatch is

\[
 w[j-p]\ne w[j],\qquad F(N,p)=j-p.
\]

If r complete blocks cannot survive, then

\[
 j\le N+rp-1,\qquad F(N,p)\le N+(r-1)p-1.
\]

Do not substitute `N+rp` for a zero-based witness index. An arbitrary later
deviation from the candidate pattern need not disagree with its own
p-predecessor: both may already have deviated in the same way. The first
divergence guarantees the witness, or the implementation may directly
search for `w[n]!=w[n+p]`.

A rational source target is a necessary negative boundary case. For
`x=10/3`, the first output is L and the next mediant equals x exactly. A
strict enclosing interval name alone cannot resolve that equality with
the irrational observer's comparison guard. Productivity claims therefore
require irrationality; a rational-aware observer needs an equality witness
and terminal symbol. Pure-letter infinite candidates are limiting cylinder
paths, not productive strict-enclosure observations of the rational endpoint.

## 5. Whole-run acceleration

Before evaluating normalized bounds, refine until

\[
 a/b<\ell<u<c/d.
\]

This prevents the current rational source endpoints from landing at the
residual chart's zero or pole. Source containment in the closed Farey
bracket is insufficient. In particular, the original stage-zero upper
bound 4 is a pole at the root, and later source bounds can touch current
bracket endpoints even when every emitted arrow is valid.

Let `z=(bx-a)/(c-dx)`. For R, z is greater than one and the maximal run has
length `floor(z)`. Its interval is obtained in increasing endpoint order.
For L, z is below one and the maximal run has length `floor(1/z)`. Since
the reciprocal residual decreases with x, its interval is

\[
 \left[\frac{c-du}{bu-a},\frac{c-d\ell}{b\ell-a}\right].
\]

Refine until both rational bounds certify the same integer floor, accounting
correctly for strictness if a rational bound is exactly integral. The actual
irrational residual is never integral. A conservative floor-equality rule
may refine longer and is still total.

After an R run of length r, `z-r` is in `(0,1)`; after an L run,
`1/(1/z-r)>1`. Thus the next branch flips. An accelerated stream consisting
of **branch labels only** is consequently periodic `L,R,L,R,...`.
Aperiodicity is a claim about the `(branch,length)` stream, or its integer
length sequence, with lengths retained.

The pi control starts `(L,6),(R,15),(L,1),(R,292),...`. The first L length
is the first fractional continued-fraction coefficient minus one. Do not
apply that offset without checking the initial branch for a generic target
in `(3,4)`; targets above 7/2 start with R.

## 6. Classical uniform bounds already exist

Waldschmidt's **Corollary 3.2**, *Transcendence measures for exponentials and
logarithms*, J. Austral. Math. Soc. 25 (1978), pp445–465, gives, for nonzero
integer P of degree at most `D>=2` and height at most H with `log(H)>=D`,

\[
 \log|P(\pi)|>
 -2^{40}D(\log H+D\log D)(1+\log D).
\]

The original author-hosted PDF was visually checked at Fig.1 (p446) and
Corollary3.2 (p452):
<https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/JAustralMS25-1978-445-465.pdf>.
The same pi bound is tabulated in Table1 of Gallego-Hernández and Mansutti,
*On the Existential Theory of the Reals Enriched with Integer Powers of a
Computable Number*, STACS2025:
<https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.37/LIPIcs.STACS.2025.37.html>.

For the present degree-at-most-two polynomials, choose
`H=max(16,height(P))` and `D=2`. Since `log H>=4 log 2`,
`log H+2 log 2<=1.5 log H` and `1+log 2<2`. Hence the conservative corollary

\[
 |P(\pi)|>H^{-2^{43}}
\]

follows. Also `M<=9H`, so every selected root in `[3,4]` satisfies

\[
 |\pi-\alpha_W|>\frac1{9H^{2^{43}+1}}.
\]

This supplies a completely a priori, astronomical integer-height escape
bound when inserted into the previous cylinder formulas. Its existence is
classical. The source-adaptive certificate can be vastly sharper and does
not need to compute such enormous integers. Do not claim that a uniform
bound is unknown merely because the current implementation uses refinement.

The remaining useful question is quantitative and explicit: can the
special prefix/period polynomials arising from this observer admit much
sharper, practically useful separation and escape estimates, with proofs
that exploit their geometry or arithmetic? Such a result would strengthen
the current interface. Merely renaming the same interval search, or stating
nonquadraticity in another category, would not pay that quantitative debt.
Any normality or signed statistical theorem remains a separate frontier.

## 7. Executed finite controls

**Observed:** a separate stdlib-only exact-arithmetic script was run by this
bearing. It used tuple matrices and rational bisection, independently of the
new implementation. It checked the following finite cases:

| Control | Exact result |
| --- | --- |
| Root conjugation for LR, L, R | Primitive fixed polynomials `(1,-9,19)`, `(1,-6,9)`, `(1,-8,16)` |
| Quadratic alpha observer | 200 outputs were exactly `(LR)^100` |
| Interval potential on that periodic control | All 479 completed events decreased it strictly: 279 source refinements and 200 outputs |
| Residual return in `Q(sqrt(5))` | Applying L then R returned exactly to `(-1+sqrt(5))/2` |
| All mixed words of lengths 2 through 8, denominator rows `(1,1)`, `(106,113)`, `(17,23)` | All 1,482 width-contraction checks passed |
| Pure L/R, periods 1,2,17; repetition counts 1,2,31; the same three denominator rows | All 54 exact-width formulas passed |
| Vertex omission mutation | Endpoint values `3,3` concealed interior value `-1`; endpoint-only test refuted |

These runs calibrate sign, orientation and boundary conventions. The
universal proofs above do not follow from their finite count. The raw output
of the executed command was:

```text
global_polynomial LR (1, -9, 19)
global_polynomial L (1, -6, 9)
global_polynomial R (1, -8, 16)
quadratic_control {'arrows': 200, 'source_refinements': 279,
 'strict_potential_decreases': 479, 'period': 2}
contraction_controls {'mixed': 1482, 'pure': 54}
endpoint_only_polynomial_mutation {'left': 3, 'right': 3, 'vertex': -1,
 'false_positive_if_vertex_ignored': True}
normalized_residual_control {'exact_return_after': 'LR', 'field': 'Q(sqrt(5))'}
```

## 8. Required implementation audit before promotion

- Reconstruct source intervals and prefix matrices from the claimed source
  stage and prefix, rather than trusting certificate-supplied geometry.
- Reject zero/negative p, negative N, invalid letters, singular/scalar-identity
  candidate matrices, and forged or noncanonical polynomial data where the
  interface promises canonical values.
- Recompute a sound polynomial interval and the strict distance/deadline
  inequality; mutations to polynomial, gap, deadline or witness must fail.
- Distinguish first candidate-pattern divergence from the p-shift witness.
- Check the quadratic control remains unresolved for its genuine period;
  a finite diagnostic may time out without claiming a refutation.
- Keep both rational endpoints inside normalized chart domains, reverse the
  L reciprocal interval endpoints, and retain run lengths.
- Do not let Python's integer-to-decimal digit cap silently destroy the
  unbounded-run API. Existing `rational_text` has a bounded-chunk fallback;
  any new path that serializes raw growing integer fields needs equivalent
  treatment or an explicit CLI configuration.
- Preserve source separation certificates before reading future output for
  the prediction holdout; confirm the resulting witness with the independent
  rational-rotation source or another independently decomposed recurrence.

No implementation outcome is claimed by this checklist. It records the
remaining checks to apply when the Round V code is assembled.

## 9. First assembled-code audit

**Observed:** the staged `aperiodic_observer.py` with SHA-256
`adfb443efb1ebd0591a58e985b2e5767581be3df3ac916f735e3e78f7b8e630f`
was loaded with only its import path redirected in memory to the frozen
Round IV source. No source file was changed by the audit. A separate replay
used tuple matrices, a scalar beta recurrence, direct alternating sums for
the rotation source, and its own chart/polynomial arithmetic.

The replay verified the saved period, run and pinbed artifacts, plus live
period certificates for twelve requested `(N,p)` pairs under each of the
two sources. It independently checked source intervals, certified prefixes,
matrix conjugation, primitive polynomial, exact polynomial range including
the vertex, derivative and gap, minimal escape-block count, strict escape
inequality, deadline/witness indices, the classical budget's numeric and
symbolic fields, and the first actual p-shift mismatch.

| Executed audit | Result |
| --- | --- |
| Saved `(N,p)=(22,1)` period artifact | escape blocks294; first mismatch index314 |
| Live certificates with `extra=2` | 12 beta and12 rotation certificates passed |
| Saved maximal-run trace | 12 blocks, 338 expanded arrows, every floor and closed update passed |
| Saved residual pinbed | 6 states, 5 rational thresholds, all reconstructed intervals and signatures passed |

The live requested pairs were `(0,1)`, `(0,2)`, `(0,7)`, `(1,7)`, `(5,2)`,
`(6,15)`, `(21,2)`, `(22,1)`, `(97,3)`, `(310,7)`, `(314,4)`, `(500,13)`.
Their first mismatch indices were, respectively,
`6,6,7,8,7,21,23,314,314,319,318,588` for both sources. The different
source-derived escape counts are expected: certificates depend on the
available enclosure, while the represented output word is the same.

No production defect was found at that revision. This audit did not yet
test the separately assembled verifier's rejection of malicious mutations;
that remains a distinct gate. The generated certificate verifier must
reconstruct the full claimed data, including uniform-budget and deadline
metadata, if its success status is intended to cover all those claims.

## 10. Targeted checker mutation audit and repairs

The initial independent checker revision
`5246a2aed330ddce4ad7b4a163e7e40843c03de1a05f6233eb469dabba35a8b5`
accepted three targeted changes. None changed the authenticated mathematical
period mismatch, but each corrupted a claim printed in the accepted record:

| Mutation | Why accepting it was misleading | Repaired validation |
| --- | --- | --- |
| For `(N,p)=(0,1)`, replace witness source stage10 by genuine stage9 and replace its interval consistently | The source interval still certified the witness, but the claimed execution clock rewound after preparing at stage10 | Witness source stage is at least the plan source stage |
| Replace the classical-import label by a claim of a proof without classical dependencies | Numeric estimates still matched the imported formula, but the provenance claim was false | Exact named classical provenance is required |
| Replace fixed nonadaptive threshold scope by a claim of global adaptive optimality | The threshold family still separated the states, but the optimality claim exceeded its theorem | Exact declared probe-class scope is required |

Root repaired all three and added named regression mutations. This bearing
then reran **only these three former acceptances** on checker revision
`5cb1db3f39a124d2ed703656282c8614e66b3554c57579515f1e2f8f48b157fc`,
with producer revision
`07126c2f5ea63f7b40ea58a4d735f374abe19a4dc15952a9b2b0488d6e9fde72`.
All three were rejected, respectively with:

```text
witness source clock cannot rewind
classical theorem provenance
threshold optimality scope
```

The producer revision also rejects nonintegral matrix images instead of
silently truncating them in `Bracket.apply`. Its ordinary generated outputs
are unchanged. The source-stage and no-future-read execution descriptions
remain grounded in the producer code and recorded execution ordering;
matching a static metadata field alone would not prove execution history.

One additional code-review boundary was reported without an extra runtime
probe: natural-number fields should be explicitly required to be integers
when checking untrusted JSON. Inequalities alone do not establish that
domain, and a matrix-power helper using `%` and `//` can otherwise process
fractional inputs. This is a schema/domain-validation observation, not a
claim that a malformed certificate was executed or accepted in that test.

Root subsequently added explicit integer-domain checks for the quantified
counts, stages, matrix exponents, chart/polynomial entries and threshold
signatures. The final root probe also rejects a fractional escape-block count.
Its complete thirteen-mutation suite passed at checker SHA256
`032ff19a0b8192c752a976660096d1d396f39925930604396783d2d0f746acec`.
The earlier auditor rerun above remains attributed to its actual revision;
this final domain-validation result is root's separately recorded run in
`audit_receipt.json`. An unclosed subprocess stderr handle in an early smoke
check was also closed; the final run under `python -W error` is warning-free.
