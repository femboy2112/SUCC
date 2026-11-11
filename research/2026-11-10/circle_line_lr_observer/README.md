# The circle/line observer: a finite program that recovers pi

**Round IV, 2026-11-10 America/New_York / 2026-11-11 UTC.**
Built on branch `aletheia/cursed-categories-dedekind-yoneda-2026-11-10`,
baseline `964768cd1fa5116f521625abfaaad8d8fab0f222`.

**Result — PROVED PAPER, with executable finite checks.** One finite program,
using growing integer/rational registers, starts from a specified Euclidean
circle/line model and emits an infinite Stern–Brocot L/R name of the circle's
circumference/diameter ratio. Every requested finite prefix terminates. The
program also emits certified radix digits. The production source contains no
pi constant, pi-digit table, BBP oracle, floating-point threshold, or
trigonometric evaluation.

The new structure is a geometry-derived input stream of rational matrices,
an exact L/R output compiler, and a coherent circle/line action retaining its
Euclidean arclength distortion. A quantitative theorem also tells us how much
geometric input suffices to approximate the existing expanding Fourier
observer. It supplies comparison accuracy; the selected signed cancellation
problem remains open.

## Productive execution follow-up

[Round V](../aperiodic_circle_observer/README.md) proves semantic and normalized
state nonreturn, constructs finite deadlines against every proposed repeating
tail, computes whole L/R run lengths, and distinguishes normalized states by
finite rational cut probes. The existing geometric source below is retained.

## Run the observer

From this directory:

```sh
python circle_line_observer.py --steps 512 --digits 64 --output observer_trace.json
python circle_line_observer.py --source rotations --steps 512 --digits 64
python observer_probe.py --output observer_receipt.json
python circle_line_observer.py --forever
```

The final command emits one JSON certificate per arrow until the consumer
stops it. Each certificate includes the mediant, the source precision used,
and the updated rational endpoints. A finite consumer can close the pipe.
The archived demonstration is a finite execution, not a completed infinite run.

The implementation uses only the Python standard library. Its geometry is a
**fixed, compiled semantic model**: explicit equations, incidence maps, metric,
and a source justified by the supplied analysis. It is not an arbitrary-equation
parser or a general mathematical proof assistant. The proofs here are written
mathematical proofs, not a new Lean formalization.

## 1. Research contract

The previous round's L/R graph used an independently supplied BBP comparison
name. This round asks whether the circle and line can determine that name
internally, with a finite comparison procedure.

| Contract item | Exact content |
|---|---|
| Target object | Euclidean unit circle, its arclength, diameter 2, and the ordered parameter line. |
| Target output | Correct rational L/R enclosures, every finite prefix produced in finite time, unique limiting value equal to geometric pi. |
| Hypotheses | Classical Euclidean arclength/calculus, exact rational arithmetic, and the established irrationality theorem for pi. |
| Load-bearing information | The metric density, circumference/diameter normalization, source coefficients, endpoint orientation, and certified branch comparisons. |
| Accepted evidence | Written derivation plus a runnable observer, independently replayed certificates, exact countercontrols and hashes. |
| Minimal falsifiers | Erase the density, change normalization, reverse multiplication side, emit before comparison is certified, confuse radians with turns. |
| Remaining hole | An all-large-epochs bound on the actual source-selected signed contrast; a general representation theorem does not supply it. |

**Novelty boundary.** Pi computability, its irrationality, stereographic
projection, the beta integral, continued fractions and safe pi spigots are
classical. This round implements and audits their particular assembly with
the repository's observer and source conventions. It does not claim discovery
of the first pi algorithm or a new normality theorem. See [sources](#sources).

## 2. What the observer means by a circle and a line

Its internal model retains

$$
x^2+y^2=1,\qquad y=t(x+1),\qquad ds^2=dx^2+dy^2.
$$

The secant line passes through the fixed circle point \((-1,0)\).
The second intersection is

$$
P(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
\qquad \|P'(t)\|=\frac{2}{1+t^2}.
$$

For \(0\le t\le1\), this traverses a quarter circle. Four equal quarter
arcs and diameter 2 give, by definition of the geometric ratio,

$$
\pi=4\int_0^1\frac{dt}{1+t^2}.
$$

This is the source of the number. Circle incidence without the Euclidean
metric would not specify this length. Flattening the integrand to 1 changes
the answer to 4. Uniform radius scaling, including the diameter, preserves
the ratio.

There are two implemented ways to compile that integral into rational bounds.

### Primary input: a natural-number stream of integer matrices

Evenness and a rational substitution give

$$
\pi=2\int_0^1\frac{dt}{1-2t(1-t)}
=2\sum_{n\ge0}W_n,
\qquad
W_n=\frac{2^n(n!)^2}{(2n+1)!}.
$$

The geometric expansion is uniform because \(2t(1-t)\le1/2\).
Integration by parts proves its factorial coefficient, and
\(W_n/W_{n-1}=n/(2n+1)\). Define

$$
Z_k=\begin{pmatrix}k&4k+2\\0&2k+1\end{pmatrix},
\quad Z_k(x)=2+\frac{k}{2k+1}x,
\quad A_k=Z_1\cdots Z_k.
$$

The exact identity

$$
A_k(x)=2\sum_{n<k}W_n+W_kx
$$

and the strict bound \(3<\tau_k<4\) for every shifted tail prove

$$
\pi\in\operatorname{int} I_k,\quad I_k=A_k([3,4]),\qquad
|I_k|=W_k<2^{-k}\quad(k\ge1).
$$

The initial bound \(3<\pi<4\) is derived by the same tail argument; it
is not a digit supplied to the generator. Each factor is generated from the
next natural number. [LR_TRANSLATION.md](LR_TRANSLATION.md) gives the full
derivation, tail proof, and relation to Gibbons' safe streaming construction.

### Independent input: two rational rotations

The 3–4–5 triangle provides an especially small geometric certificate:

$$
P(1/2)=(3/5,4/5),\quad P(1/3)=(4/5,3/5),\qquad
P(1/2)P(1/3)=(0,1).
$$

Here the product is circle-group multiplication. These two rational points
compose to a quarter turn, giving

$$
\pi=4\left(\int_0^{1/2}\frac{dt}{1+t^2}
                  +\int_0^{1/3}\frac{dt}{1+t^2}\right).
$$

Alternating polynomial remainders supply a second exact interval source.
Its first bound is \(505/162<\pi<10/3\).
[CIRCLE_GEOMETRY.md](CIRCLE_GEOMETRY.md) proves the strict remainder signs,
nesting, and explicit width. It reaches the same L/R word through a different
coefficient implementation. Both sources share the Euclidean integral and
classical analysis; they are not logically independent definitions of pi.

## 3. The finite L/R machine and its proof

Store endpoint columns

$$
E=\begin{pmatrix}a&c\\b&d\end{pmatrix},\quad
\frac ab<\pi<\frac cd,\quad bc-ad=1,
\qquad E_0=\begin{pmatrix}3&4\\1&1\end{pmatrix}.
$$

Let \(L=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\)
and \(R=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\).
The machine repeats these finite rules:

```text
q := (a+c)/(b+d)
while the geometric interval straddles q:
    consume the next geometric source factor
if upper <= q:
    E := E L; emit L
else if lower >= q:
    E := E R; emit R
repeat
```

**Safety.** The geometric source strictly contains pi, so either displayed
comparison certifies the chosen side. Endpoint equality with the mediant is
safe because pi is strictly between the source endpoints.

**Productivity.** Each mediant is rational. Irrationality of pi gives a
positive separation from that mediant. Since the source width tends to zero,
the comparison eventually resolves. Apply this after each finite prefix.
This classical theorem is used in the proof; the program does not query an
irrationality oracle or a real-comparison oracle.

**Recovery.** Each update preserves \(bc-ad=1\), hence the output bracket
has width \(1/(bd)\). Each step increases \(bd\) by at least 1.
After \(N\) output arrows,

$$
\frac cd-\frac ab=\frac1{bd}\le\frac1{N+1}\longrightarrow0.
$$

Every bracket contains pi, so their unique common point is pi. This is a
universal proof of the recovery property, separate from the finite test run.
Finite program length is compatible with growing integers; an autonomous
machine with finitely many complete states would be eventually periodic.
Pi's transcendence excludes such a bounded-state L/R generator.

## 4. What actually ran

The saved [trace](observer_trace.json) has 512 certified arrows and 64
hexadecimal fractional digits:

```text
3.243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89
```

From the local root \([3,4]\), its runs begin

$$
L^6R^{15}LR^{292}LRLR^2LR^3LR^{14}\cdots.
$$

The full Stern–Brocot root \([0/1,1/0]\) contributes the prefix `RRRL`,
so the initial full runs are \(R^3L^7R^{15}LR^{292}\cdots\).
These conventions explain the initial 6 versus 7. Representative brackets:

| Output prefix from [3,4] | Lower endpoint | Upper endpoint |
|---|---|---|
| \(L^6\) | \(3\) | \(22/7\) |
| \(L^6R^{15}\) | \(333/106\) | \(22/7\) |
| \(L^6R^{15}L\) | \(333/106\) | \(355/113\) |
| \(L^6R^{15}LR^{292}\) | \(103993/33102\) | \(355/113\) |

The 292 run is the path's record of the especially close upper approximation
\(355/113\). It was produced by certified comparisons, not supplied as a
continued-fraction table.

The primary source used 123 factors for the 512 arrows and 254 factors after
the 64 digits. The independent rotation source used 30 and 63 refinement
stages respectively; these stages are different units of work.

[observer_probe.py](observer_probe.py) separately checks BBP interval
agreement, reconstructs source certificates from scalar formulas, compares
continued fractions, checks conic composition and the metric cocycle, and
rejects eight explicit mutations. The independent reviewer notes contain
further runs, including 4,096 arrows per source. These are differently
implemented checks by same-model agents, not blind or fully independent
proof witnesses. [VALIDATION.md](VALIDATION.md) records exact execution scope.

## 5. Which geometric structure survives the arrows?

The rational projective line and the circle conic are isomorphic by

$$
[u:v]\longmapsto[v^2-u^2:2uv:v^2+u^2].
$$

Infinity is included. Every invertible rational matrix \(M\) lifts to an
explicit rational \(3\times3\) conic matrix \(\widehat M\), with
\(\widehat{MN}=\widehat M\widehat N\). This gives an isomorphism of the
corresponding action groupoids, with objects, arrow labels and composition
retained. Scalar matrix representatives are identified projectively.

The Euclidean metric contributes additional data. For
\(M(t)=(at+b)/(ct+d)\), the arclength distortion is

$$
J_M(t)=\frac{|\det M|(1+t^2)}{(at+b)^2+(ct+d)^2},\qquad
J_{MN}(t)=J_M(N(t))J_N(t).
$$

On rational points this gives positive rational arrow values, with the
displayed composition law. On the projective point at infinity its continuous
extension is \(|\det M|/(a^2+c^2)\). Thus the cocycle is a functor from
the rational action groupoid to the one-object multiplicative group of positive
rationals. It is not faithful: retaining the underlying projective map remains
necessary. The software's `metric_jacobian` implements finite charts; the
global extension is the mathematical statement above.

This weight is relevant to the user's proposed geometric insight. The two
arcs cut by the first rational mediant \(t=1/2\) have unequal Euclidean
length. Equal branch counts do not automatically represent equal geometric
mass. Keeping the metric lets the observer detect that mistake exactly.

Input matrices and output matrices are distinct actions: \(\det Z_k=k(2k+1)\),
whereas L/R words have determinant 1. In particular \(\det Z_1=3\) prevents
identifying \(Z_1\) projectively with a rational scalar multiple of an L/R
word. The comparison compiler, not a false factorization, connects them.

For the increasing endpoint chart \(B_E=E\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\),
source consumption acts on the residual on the right; output changes act on
the left with the explicitly swapped L/R generators. Their commuting square
is proved in [LR_TRANSLATION.md](LR_TRANSLATION.md). The same note gives
correctly directed rational cut and interval probe functors, connecting this
observer to Round III's Dedekind/Yoneda reconstruction.

## 6. A concrete bridge to the existing Fourier observer

Let \(x_k\) be the rational midpoint of \(I_k\). For integers
\(A\ge1\), \(s\ge0\), and nonzero integer \(h\), the exact schedule
\(k=8A+s\) gives

$$
\left|\frac1A\sum_{n=A}^{2A-1}e(h16^{n-1}\pi)
       -\frac1A\sum_{n=A}^{2A-1}e(h16^{n-1}x_{8A+s})\right|
<\frac{|h|}{60A\,2^s},\qquad e(x)=\exp(2\pi i x).
$$

[PRECISION_TRANSFER.md](PRECISION_TRANSFER.md) proves the constant, retains
the original source's zero seed and indexing, and gives the further tail
payment for \(U_n\). This resolves how much source precision the expanding
observable needs. It does not bound the common value of the two averages.

The genuinely new proof target would be a source-specific cancellation
estimate for these moving rational approximants, or for the frontier's weaker
two-fiber contrast, with all its existing seed and complement data retained.
The same broad finite-program/LR shape also produces computable transcendental
nonnormal numbers. That control rules out inferring statistics merely from
productivity or transcendence; it leaves a more specific geometric theorem
available to be proved.

One exact unit check is essential: geometric pi **radians** is a half-turn.
The radix observer \(e(16^{n-1}\pi)\) uses its argument in **turns**.
Replacing it by \(\exp(i16^{n-1}\pi)\) gives \(-1\) once and \(1\)
forever afterward. [HOSTILE_OBSERVER.md](HOSTILE_OBSERVER.md) records this
and the other controls.

## Reading map and sources

| File | Role |
|---|---|
| [CIRCLE_GEOMETRY.md](CIRCLE_GEOMETRY.md) | Circle/line incidence, metric, rational rotation source, productive L/R proof. |
| [LR_TRANSLATION.md](LR_TRANSLATION.md) | Beta source, exact handedness, source/output coherence, conic equivalence and metric cocycle. |
| [PRECISION_TRANSFER.md](PRECISION_TRANSFER.md) | Explicit source-stage budget for the original expanding Fourier observer. |
| [HOSTILE_OBSERVER.md](HOSTILE_OBSERVER.md) | Countermodels, API defects caught and repaired, exact-version implementation audit. |
| [IMPLEMENTATION_CONFORMANCE.md](IMPLEMENTATION_CONFORMANCE.md) | Independently implemented source and certificate replay, with reproducible code. |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Domain, hypotheses, evidence and unresolved claims. |
| [VALIDATION.md](VALIDATION.md) | Local checks, repository validation scope and publishing evidence. |

### Sources

- Jeremy Gibbons, [Unbounded Spigot Algorithms for the Digits of Pi](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf), author manuscript, including correction notes through September 2024. The safe interval-tested construction is used; the later unproved shortcut is not.
- David H. Bailey, [The BBP Algorithm for Pi](https://www.davidhbailey.com/dhbpapers/bbp-alg.pdf), September 2006. Primary source for the separate verification formula.
- David H. Bailey, [An elementary, self-contained proof that pi is transcendental](https://www.davidhbailey.com/dhbpapers/dhb-pi-trans.pdf), July 2026. Explicit classical irrationality/transcendence proofs; these are mathematical dependencies, not discoveries of this round.
- [Pinned repository frontier](https://github.com/femboy2112/SUCC/blob/964768cd1fa5116f521625abfaaad8d8fab0f222/docs/PI_NORMALITY_FRONTIER.md): original source, zero seed, observer normalization, conditional two-fiber target and inherited countermodels.
- [Prior Dedekind/Yoneda round](../cursed_categorical_computation/round_iii_dedekind/DEDEKIND_YONEDA.md) and [computation graph](../cursed_categorical_computation/round_iii_dedekind/COMPUTATION_GRAPH.md): the existing categorical and source conventions being extended.

No imported source, historical seed, existing theorem status or CI workflow
was modified. The exact recovery theorem is established within its stated
classical domain; selected parity cancellation, base-16 normality and RH are
not promoted by this round.
