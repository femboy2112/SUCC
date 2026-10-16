# Collective Gamma clocks: rational aliases and actual certified evaluation

**Scope/status.** Classical source analysis, complete paper proofs below, and
stdlib exact finite tests. No proof-assistant certification. The source is the
normative real-place factor `Gamma_R(s)=pi^(-s/2) Gamma(s/2)` on `Re(s)>0`.
No prime-source derivation or signed-Weil identification is made.

**Ownership.** Only `observational_succ/collective_gamma.py`, its matching test
and probe, this dossier, and receipts `collective_observer_receipts/gamma*`.
Worktree base `940f089d10926ecbdf24ee9e3483c993042b9275`, branch
`research/collective-observer-2026-10-16`. Principal owns commits and integration.

## 1. Actual source and dependency pins

Read via `git show`, not imported or modified:

| Source | Exact snapshot | Used result / boundary |
|---|---|---|
| PR141 | `849b241801578542997972eb46f3c8d309b36d0c` | DGC-2/3: log-Gaussian source and Poisson replicas; its mpmath readouts are explicitly uncertified |
| Concurrent gamma-band branch | `6623fd11b710a40dc5f9cd2375ba74d759be0245` | BGD-1: complete shifted lanes; BGD-3/4: contour and finite-tail bounds already solved; BGD-5: derivative-error theorem outside this implementation |

The concurrent branch initially had PR141's head, then advanced during work.
The exact later commit was obtained with
`git fetch --no-write-fetch-head origin acabe016aab55e921c0525da33e47937b73f3363`
and inspected with `git show`; no branch/index/working source was changed.
The final inspected snapshot is `6623fd11b710a40dc5f9cd2375ba74d759be0245`,
obtained in the same way. Relative to acabe01 its module and dossier changes
only restore terminal newlines; the source receipt also records byte hashes.

SHA256 of PR141 `observational_succ/gamma_dirac_continuum.py`:
`05f8bb74ee202c4c8b8a53b05ddd03a92ba4121e2ccceba0b2474155232d14f5`.
SHA256 of later `observational_succ/gamma_band_dealias.py`:
`ff01af58064f05a96aabee5bf31cdc4a56ec15d2beb9f1c79b308d709d074b37`.
The old files are not runtime dependencies. Existing rational interval modules
were inspected; this narrow implementation uses only stdlib and no imported
archive code. `provenance/README.md` and `IMPORT_MANIFEST.json` were inspected.

**Delta from solved work:** the rational *tuple* period/no-decoder theorem and
the end-to-end enclosure of actual finite **complex values**, including pi,
sin/cos, exp, and rounding. Interleaving and analytic band estimates are credited
dependencies, not new discoveries. Multiple clocks share the same source;
reindexing them does not create independent evidence.

## 2. Source and Poisson identity (DGC-2/3, supporting proof)

For `h>0`, `s=sigma+it`, `sigma>0`, put

\[
 f_s(u)=e^{su/2-\pi e^u},\qquad
 R_h(s)=h\sum_{n\in\mathbb Z}f_s(nh).
\]

Both tails converge absolutely, locally uniformly in this half-plane: the left
is bounded by a geometric series and the right decays faster than exponentially.
Substitution `x=pi exp(u)` in the integral gives exactly `Gamma_R(s)`.
Every real derivative of `f_s` is a polynomial in `e^u` times `f_s`; hence it
is Schwartz on the real u-line. With transform
`hat f(omega)=integral f(u) exp(-i omega u) du`, the same substitution gives
`hat f_s(omega)=Gamma_R(s-2i omega)`. Classical Poisson summation applies:

\[
R_h(s)=\sum_{k\in\mathbb Z}\Gamma_{\mathbb R}(s-4\pi i k/h).\tag{1}
\]

Section 4 supplies an absolute summable bound on the replicas. This is an
identity of the infinite mathematical source, not a finite-event observation.

## 3. Finite rational multi-clock theorem (PROVED PAPER)

Fix a nonempty finite family of positive rational spacings `h_1,...,h_m` and
write `h_j=a_j/D` with positive integers `a_j,D`. Define
`g=gcd(a_1,...,a_m)/D`, independently of the chosen common denominator.
Let `Phi(s)=(R_{h_1}(s),...,R_{h_m}(s))`.

**Theorem G1.** For each fixed `sigma>0`, the full additive group of imaginary
translation periods of `Phi(sigma+it)` is `(4 pi/g) Z`. Its least positive
period is `P=4 pi/g`; duplicates do not change it.

**Proof.** On this line, each clock is an absolutely uniformly convergent
Fourier series in t with frequencies `n h/2` and strictly positive coefficients
`h exp(sigma n h/2-pi exp(nh))`. A translation tau is a period only if its
nonzero n=1 Fourier coefficient is unchanged, so `exp(i tau h/2)=1`.
Conversely that equality makes every summand invariant. Thus a joint period
has `tau h_j/(4 pi)` integer for every j. Set `x=tau g/(4 pi)` and
`b_j=h_j/g`, relatively prime as a family. The condition is `x b_j` integer
for every j. Bezout integers with `sum c_j b_j=1` imply x is an integer;
the converse is immediate. This also proves minimality. QED.

**Theorem G2.** No deterministic decoder `D` whose *only input* is `Phi(s)`
can equal `Gamma_R(s)` throughout the positive half-plane. Even with arbitrary
nonlinear/discontinuous D, on each line sigma>0 its absolute uniform error is
at least `Gamma_R(sigma)/2`. Its supremum error over the whole positive
half-plane is infinite.

**Proof.** Put `A=Gamma_R(sigma)>0` and `c=D(Phi(sigma))`. At every
`s_n=sigma+i nP`, G1 gives the same decoder value c. The contour estimate in
Section 4 proves `Gamma_R(s_n)->0` as `n->infinity`. Therefore the line's
supremum error is at least `max(|c-A|,|c|)>=A/2`, by the triangle inequality.
This uses no regularity of D. For an entirely elementary rational divergence
bound, the source on u<=0 gives

\[
 A\ge e^{-\pi}\int_{-\infty}^0e^{\sigma u/2}du
 =2e^{-\pi}/\sigma >2/(81\sigma).
\]

Here `pi<4` and `e<3`; the latter follows by summing `1/n!<=1/2^(n-1)`
for n>=1 with strict inequality somewhere. Hence the uniform-error floor is
strictly above `1/(81 sigma)`, unbounded as positive rational sigma tends to
zero. Equivalently the familiar Gamma recurrence and continuity at 1 yield
`Gamma_R(sigma)~2/sigma`, but that asymptotic is unnecessary. QED.

At sigma=1 the exact floor is at least 1/2 (`Gamma_R(1)=1`, Gaussian integral).
If D could additionally inspect exact s, height, a period index, or a target
oracle, it would be a different observation contract; G2 does not cover it.
The fixed mesh and period metadata may be built into D.

**Hostile cases.** Meshes `(1/2,1/3)` have individual periods `8pi,12pi` and
joint period `24pi`, not either individual period. Repeating mesh 1/2 any
finite number of times leaves period `8pi`. If two positive spacings have
irrational ratio, the single-clock argument rules out a nonzero common
translation period. This alone does **not** establish injectivity: the map
`t -> (cos(t),cos(sqrt(2)t))` has no nonzero common period but identifies t and
-t. This is a counterexample to the logical inference, not a claim of a
specific collision of the incommensurate Gamma tuple. Its injectivity is open
here. Having no universal period does not settle all pairwise collisions.

## 4. Uniform finite-strip bound (BGD-3/4 specialization; PROVED PAPER)

Fix rational `0<a<=b`, `T>=0` and the strip `a<=sigma<=b`, `|t|<=T`.
Set `M=ceil(b/2)-1` and `C=2/a+M!` (M>=0). Rotate the log-integral contour
by `u -> u+i sign(v)` (one radian). On the closing vertical edges the left
decays like `exp(sigma u/2)` and the right like
`exp(-pi cos(1) exp(u))`, with all intermediate angles having positive cosine.
Thus the edges vanish. On the shifted line,

\[
 |\Gamma_{\mathbb R}(\sigma+iv)|
 \le e^{-|v|/2}(\pi\cos1)^{-\sigma/2}\Gamma(\sigma/2)
 \le C e^{-|v|/2}.\tag{2}
\]

For completeness `cos(1)>=1-1/2=1/2` and `pi>3`, so the power prefactor is
at most 1. Splitting Euler's integral at x=1 bounds its first piece by 2/a;
on x>=1, `x^(sigma/2-1)<=x^M`, and the remaining integral is at most M!.
The numerical constant C is exact rational. Unlike a numerical application of
Stirling, this proof has no hidden asymptotic threshold or fitted constant.

Let `q=exp(-2pi/h)`. Using `|t-4pi k/h|>=4pi|k|/h-T` in (1),(2) gives

\[
 E_{alias}=\frac{2C e^{T/2}q}{1-q},\qquad
 \sup_{strip}|R_h-\Gamma_{\mathbb R}|\le E_{alias}.\tag{3}
\]

This remains valid even when the band crosses an alias; it then becomes large.
It is an absolute bound, not a relative error guarantee at tiny target values.
The sibling's pi/3 shift yields a somewhat sharper exponent. We use the
one-radian version as a simple independent derivation supporting this evaluator.

For `L<=0<=R`, define the actual finite source
`F=h sum_(n=L)^R f_s(nh)`, `v=(R+1)h`, `A=a/2`, `B=b/2`. The omitted tails
satisfy

\[
 E_{left}=\frac{h e^{A(L-1)h}}{1-e^{-Ah}},\quad
 r=e^{Bh-\pi e^v(e^h-1)},\quad
 E_{right}=\frac{h e^{Bv-\pi e^v}}{1-r}\quad(r<1).\tag{4}
\]

**Proof.** At omitted negative u, modulus <=exp(Au). Sum its geometric
progression, starting at `(L-1)h`. For positive u>=v, modulus
<=exp(Bu-pi exp(u)); the ratio of successive majorants is
`exp(Bh-pi exp(u)(exp(h)-1))<=r`. Sum this geometric majorant when r<1.
Together (3),(4) imply `sup_strip |F-Gamma_R| <= E_alias+E_left+E_right`.
The code rejects a right cutoff if the *upper interval endpoint* of r is >=1.

**Constructivity.** For a fixed strip and rational epsilon>0, decreasing h
through `2^-j` makes (3) tend to zero. At fixed h, decreasing L makes the left
tail tend to zero; increasing R eventually gives r<1 and a right tail tending
to zero. Each is a computable real with the rational enclosures of Section 6,
so search terminates using strict positive margins, without a Gamma oracle.
For the resulting finite event set, increase arithmetic grid precision until
its rectangle widths meet the remaining budget. This proves finite certified
approximability on any such strip. The implemented finite resource guards may
reject very demanding requests; they are not mathematical impossibility claims.
The mathematical scheme allows arbitrarily fine grids; this executable caps
digits at 16..100, sigma_max at 64, retained events at 20000, the last retained
positive u at 20, positive exp arguments at 10000, and lane count at 64.

## 5. Cooperative dealiasing contract (credits BGD-1)

For m>=1 and r=0,...,m-1 define a genuinely shifted source lane
`A_r(s)=h sum_n f_s(h(n+r/m))`. Absolute convergence permits reindexing:

\[
 D_m(A_0,...,A_{m-1}):=\frac1m\sum_r A_r(s)=R_{h/m}(s).\tag{5}
\]

The decoder is a fixed arithmetic mean with **no s input**. The map
`(n,r)->mn+r` is a bijection onto Z, so the effective weight is h/m.
Equivalently shifted Poisson gives alias coefficient
`m^-1 sum_r exp(2pi i kr/m)=1` if m divides k, zero otherwise; this follows
by summing a finite geometric progression. Thus the surviving aliases are at
`4pi m k/h`, and (3) applies with h/m. Finite evaluation partitions exactly the
fine indices L,...,R by their residues modulo m, including negative indices.
The module checks all m lanes occur exactly once before certifying the average.

This spends additional source samples. It does not reconstruct the missing
lanes from duplicated unshifted values, nor establish independence of observers.
At any fixed m the output still has a common period and G2 remains applicable.
No finite construction becomes a globally exact Gamma factorization.

## 6. Paying transcendental and rounding debt (PROVED arithmetic design)

`Interval(lo,hi,d)` represents rational `[lo/10^d,hi/10^d]` with integer
endpoints. Exact integer addition and negation preserve endpoints. Product
and quotient endpoints are minima/maxima of four exact rational corner values,
then floored/ceiled to this grid; division across zero is rejected. All inputs
are integers/Fractions, with bools, floats and strings rejected.

1. **pi.** Use `pi=16 atan(1/5)-4 atan(1/239)`. For `0<x<1`, integrate the
   finite geometric identity for `1/(1+x^2)` to get the alternating arctan
   series whose remainder has the next term's sign and smaller magnitude.
   Machin's identity follows from tangent addition: if alpha=atan(1/5),
   `tan(2alpha)=5/12`, `tan(4alpha)=120/119`, and
   `tan(4alpha-atan(1/239))=1`. This last angle lies in `(0,pi/2)`, so equals
   pi/4. Rational interval subtraction and outward grid conversion pay all
   cancellation. Terms are retained until the next is below `10^(-d-8)`.
2. **exp.** Rational grid endpoints are converted exactly by Decimal tuple
   construction in a fresh context with precision d+12. Python documents
   `Decimal.exp` as correctly rounded in ROUND_HALF_EVEN, regardless of the
   ordinary directed rounding setting. We bracket its result by `next_minus`
   and `next_plus`, convert those finite decimals to exact Fractions, and then
   round outward to the grid. Monotonicity encloses the whole input interval.
   For x<-3d use `[0,10^-d]`: `e^3>10` proves this bound and avoids underflow.
   Each endpoint is treated separately. Ambient precision/rounding is irrelevant.
3. **sin/cos.** Choose an integer k using rational midpoints and reduce the
   entire phase interval by `2k[pi]`. The true phase is represented modulo
   2pi for this k, irrespective of how k was chosen. If the residual interval
   is not inside [-4,4], return [-1,1]. Otherwise use interval Taylor recurrences
   through sin degree 2N+1 and cos degree 2N. All real derivatives have modulus
   <=1, so Lagrange remainders are bounded together by
   `4^(2N+1)/(2N+1)!` for N>=2. Choose this below `10^(-d-4)`, add it outward,
   and intersect with [-1,1]. Argument-reduction uncertainty is retained.
4. **samples.** Enclose amplitude `exp(sigma u/2-[pi] exp(u))` and phase
   `t u/2` separately, multiply the amplitude by the sin/cos enclosures, then
   multiply by the exact mesh and add. Every finite complex sum lies in the
   resulting rectangle. Evaluate (3),(4) outward and take their rational upper
   endpoints. Expanding *both* coordinates by their sum encloses Gamma_R(s).
   The advertised coordinate radius from the finite rectangle's rational
   midpoint is `analytic_total+max(real_width,imag_width)/2`.

This is an actual enclosure, not an error bound attached to unchecked floating
samples. Its trusted numerical component is the documented stdlib Decimal.exp
contract; a separate exact Fraction Taylor/geometric oracle calibrates it at
seven rational arguments in tests. Those finite comparisons are not a proof
of CPython/libmpdec. Kernel verification and universal compiler/runtime assurance
remain outside scope. pi/trig proofs and rounded integer arithmetic are explicit.

## 7. Hostile controls, verdicts and receipts

| Claim / rival | Verdict and evidence | Boundary / next falsifier |
|---|---|---|
| Rational clocks globally determine Gamma | REFUTED, G1/G2; `(1/2,1/3)` has period 24pi; half-plane error infinite | Decoder has only tuple values; an s input changes the contract |
| Complete shifted lanes suppress first aliases | PROVED PAPER (BGD-1); actual certified rectangles near rational t=1256637/50000 | Additional source samples required; fixed m still aliases |
| Duplicate/omitted lane is equally good | REFUTED by near-alias rectangle; duplicate lane reads >99/100, authentic two-lane target coordinates have magnitude <1/1000 | Coverage validation is essential; bare arithmetic mean cannot authenticate inputs |
| Finite-strip actual evaluation is certified | PROVED PAPER plus finite rational certificates, Section 6 and gamma-probe.json | Absolute error; Re(s)>0; not derivative/log-derivative certification |
| Drop density, negative history, pi, or half slope | REFUTED by exact inequalities in tests | These are changed sources and cannot inherit the authentic bound |
| No common period implies injectivity | REFUTED as logical inference by even incommensurate cosine pair | No Gamma-tuple collision or injectivity theorem asserted |

Near the first coarse alias `8pi`, use rational t=1256637/50000 and strip
`sigma=1, |t|<=26`. Coarse mesh 1/2 with indices -160..12 yields real value
>99/100. Two complete shifted lanes give mesh 1/4 with -320..24; both target
coordinates have absolute enclosures <1/1000. The coarse alias bound becomes
large, correctly declining a false accuracy claim. Duplicate lane zero stays
>99/100. No float approximation to pi is used as an exact alias input.

On `[1,4] x [-4,4]`, mesh 1/8 and indices -512..32 (545 source events) give
actual evaluated coordinate radii <10^-12 at four deterministic points,
including `(sigma,t)=(3/2,5/3)` and `(4,-4)`. The analytic part is uniform
over the entire strip; rounding widths are certified for each evaluated point.
These four checks are not four independent source families.

Reproduce from the worktree root:

```
python -m unittest discover -s tests -p test_collective_gamma.py -v
python scripts/collective_gamma_probe.py --verify --output research/2026-10-16/collective_observer_receipts/gamma-probe.json
```

The probe always enforces its controls. Receipts retain source pins, exact
rational intervals, component errors, file hashes, and a byte-identical replay
check. `gamma-validation.json` records targeted test results and durations;
repository-wide integration validation belongs to the principal's shared pass.
No Git commit/push is performed by this worker.

**Aletheia boundary.** kappa/contact: authenticated mathematical kernel plus
executed finite sums; phi: supplied exact probes and paper theorems;
sigma/source: pi normalization, half exponent, event weight and index coverage
are load-bearing; rho: no observer-identity or source-independence inference.
The discriminating intervention is adding the missing phase lane, not duplicating
one source report. Remaining debts: proof-assistant formalization, independent
implementation audit, relative-error regimes, and incommensurate Gamma-tuple
injectivity. The next useful probe is an independent certified quadrature of
the same complex integral on a disjoint strip, with its own remainder proof.

**Primary references:** [DLMF Euler integral](https://dlmf.nist.gov/5.2#E1),
[DLMF Poisson summation](https://dlmf.nist.gov/1.8#E14),
[DLMF Gamma integral representations](https://dlmf.nist.gov/5.9),
[DLMF asymptotics](https://dlmf.nist.gov/5.11) (principal's additional reference;
not needed for our explicit contour constant), and
[Python Decimal.exp](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp).
