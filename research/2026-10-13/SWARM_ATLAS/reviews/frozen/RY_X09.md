# SWM-X09 — Uniform analytic source control makes approximate reports actualizable

## 1. Original question and dependency cut

Does the source-actualization theorem survive when observations are analytic
values rather than finite-alphabet symbols, and what must be added to the
finite Gamma and p-adic observations in E35/E37? The bridge is a **declared
compact analytic source class with continuous evaluation**, not an inference
of global regularity from finitely many values. Parent is integrated checkpoint
`7913e10`; donor dossiers are B09, B10, E35, E37, E38. No imported archival
source is edited. This independent second-generation mission also audits the
Gamma boundary and finite p-adic claims.

## 2. Existing context and truth states

Compact-image closedness and elementary power-series estimates are classical.
B09 kernel-checks a discrete-output version; it cannot be applied literally
with complex evaluation values given their usual topology. X09 supplies a
paper proof with the correct nondiscrete topology and approximate observation
quantifiers. The result is new coverage in this checkpoint, **not a priority
claim or a kernel-checked analytic theorem**.

NIST DLMF [5.5](https://dlmf.nist.gov/5.5) and
[5.8](https://dlmf.nist.gov/5.8), independently retrieved 2026-10-13, confirm
Gamma's recurrence, Bohr–Mollerup hypotheses, and Euler limit formula. Those
facts remain classical inputs. The proof below needs neither Montel's theorem
nor analytic continuation, nor any zero locations.

## 3. Actual objects, topology, and maps

Fix a finite real M>=0. Let D={z in C:|z|<1} and

`K_M = product_{n>=0} {a in C : |a|<=M}`.

Equip K_M with product topology. Define
`H(a)(z)=sum_{n>=0} a_n z^n`. Its image A_M consists of holomorphic functions
with this coefficient bound and has the compact-open topology (uniform
convergence on compact subsets of D). Let R be any **closed** subset of K_M.
A global coefficient law or equality between fixed evaluations can be imposed
by a closed condition; its truth is a source premise, not a finite test result.

Choose a countable family of evaluation points z_j in D. The source report is
`Phi:R -> C^N`, `Phi(a)_j=H(a)(z_j)`, with the usual product topology on C^N.
For finite F, `E_F(a)=(H(a)(z_j))_{j in F}`. For F subset G,
`restriction_{G,F} E_G = E_F` literally, and all these maps are continuous.
Reports share **one coefficient source**. The invariant is the common bound
and the common closed source law R through all finite restrictions and limits.

## 4. Quantified candidate theorem

**Analytic actualization.** For every M>=0, every closed R subset K_M, every
sequence (z_j) in D, and every target (y_j) in C^N, the following are equivalent:

1. For every finite F subset N and every rational epsilon>0 there exists
   `a in R` such that `|H(a)(z_j)-y_j|<=epsilon` for every j in F.
2. There exists one `a in R` such that `H(a)(z_j)=y_j` for every j.

In particular exact finite compatibility suffices. Approximate compatibility
is strictly the right general closure criterion for nondiscrete observations.
The theorem asserts existence, not uniqueness, computable preparation, finite
certification of its hypotheses, or correctness of an arithmetic source law.

**Quantitative companion.** If a prefix a_0,...,a_(L-1) is supplied and all
coefficients obey |a_n|<=M, then for |z|<=r<1,

`|H(a)(z)-sum_{n<L} a_n z^n| <= M r^L/(1-r)`.

For real 0<=x,y<1 the sharp bound is

`|H(a)(x)-H(a)(y)| <= M |x/(1-x)-y/(1-y)|`.

Both estimates retain the same source coefficient constraint, and neither
asserts that arbitrary separately consistent intervals admit one common tail.

## 5. Complete proof

The geometric majorant bounds the series uniformly on each closed disk of
radius r<1, with precisely the displayed tail. The differentiated series has
majorant `sum_{n>=1} n M r^(n-1)=M/(1-r)^2`; thus H(a) is holomorphic. The
same tail estimate proves product-to-compact-open continuity of H: given a
compact set choose r<1 containing it, truncate at L so that two tails total
less than half the requested error, and make the finitely many coefficient
differences sufficiently small to handle the polynomial head.

K_M is compact. For completeness, the elementary countable-product argument
is diagonal extraction: every sequence has a subsequence converging in its
zeroth coordinate, a further subsequence converging in the first, and so on,
by compactness of closed disks. The diagonal subsequence converges in every
coordinate to an element of K_M. The product is metrizable by
`sum_{n>=0} 2^(-n-1) min(1,|a_n-b_n|)`, so this sequential compactness is
compactness. Closed R is compact as well. H is injective: if two coefficient
sequences differ, let k be their first differing coordinate. For positive
real t tending to zero,
`(H(a)(t)-H(b)(t))/t^k -> a_k-b_k`, by the geometric tail bound; the limit is
nonzero, so their functions differ. The compact-open function space is
Hausdorff (point evaluation separates distinct functions). Therefore H is a
homeomorphism from K_M to A_M, since a continuous bijection from compact to
Hausdorff has continuous inverse. This verifies the actual function-space
interpretation rather than naming an abstract compact parameter set alone.

For the main implication choose a^(k) in R matching j<=k within 1/(k+1).
Compactness gives a convergent subsequence with limit a in R. Fix j. Along all
sufficiently late terms j was constrained. Evaluation continuity and the
vanishing error give H(a)(z_j)=y_j. The reverse implication uses this same
source for every finite request. Equivalently, continuous Phi has compact,
hence closed, image in the Hausdorff product C^N. A target lies in its closure
exactly when the finite approximate condition holds. No infinite computation
has been substituted for this mathematical existence argument.

For the pairwise bound assume x>=y>=0. The constant coefficients cancel, and
`|sum_{n>=1} a_n(x^n-y^n)| <= M sum_{n>=1}(x^n-y^n)`.
Summing the geometric series gives the formula. Coefficients a_n=M for every
n>=1 attain it. This sharper inequality supplies a finite necessary test for
the global source contract; passing that necessary test does not certify it.

## 6. Crucible: three distinct failure receipts

**Drop the common uniform bound.** Set x_j=1/(j+2) and y_j=(-1)^j. Every finite
set of these rational data has a rational Lagrange polynomial interpolant.
No continuous function on D realizes the full sequence: x_j tends to 0 while
the values have subsequential limits +1 and -1. Hence allowing arbitrary
holomorphic source functions does not make finite interpolation actualizable.
The obstruction is quantitatively visible. A polynomial fitting the first n
points, n>=2, must have maximum coefficient magnitude at least `2n(n-1)`:
apply the sharp bound to its last two samples at 1/n and 1/(n+1), whose value
difference is 2. Thus the finite witnesses cannot have one common M. Exact
Lagrange probes for n=2,...,12 verify interpolation and the necessary bound;
the proof covers every n.

**Keep a bound but omit closedness.** Let P_1 consist of finite-support
coefficient sequences in K_1, namely polynomials with all coefficients bounded
by 1. The partial sums `1+z+...+z^(L-1)` approximate `1/(1-z)` uniformly on
compact subsets, so its sampled profile is approximately compatible with
P_1 at every finite request and every tolerance. Yet no polynomial agrees
with `1/(1-z)` at all distinct x_j=1/(j+2): the polynomial
`(1-z)p(z)-1` would have infinitely many roots, hence be identically zero,
contradicting its value -1 at z=1. The source class P_1 is not closed; replacing
it by its coefficient closure K_1 repairs exactly this failure. This negative
control concerns approximate compatibility; no exact bounded-polynomial
interpolation claim is smuggled into it.

**Replace joint witnesses with separate witnesses.** In K_1, report f(0)=1
is individually realized by f=1, and f(1/2)=-1 by f=-1. The individual empty
prefix intervals contain both requested values. There is no common source:
the observed difference is 2, exceeding the sharp bound 1. Hence intersecting
marginal enclosures or accepting each coordinate separately is insufficient.

## 7. Independent donor audit and verdict

E37's finite ratio survives direct factorial/product computation at 16 fresh
cutoff/integer pairs: `G_N(z+1)/G_N(z)=Nz/(N+z+1)`, with strictly positive
defect `z(z+1)/(N+z+1)`. The independent positive periodic multiplier
`P(z)=1+sin(2pi z)/2` is 1 at integers, has period 1, stays positive on the
positive real axis, and equals 3/2 at z=1/4. Thus Gamma(z)P(z) provides another
recurrence-and-integer-data ambiguity witness. Quarter phases are checked
exactly; their finite check is not the proof of periodicity. Bohr–Mollerup's
global log-convexity supplies a separate uniqueness premise.

E35's polynomial rival is independently evaluated by the product formula for
`binom(x,N+1)`. It vanishes at all observed integers and is 1 next. The spike
argument is sound because p^r tends to 0 in Z_p while its reported values
remain 1 and its value at 0 is 0. Finite evaluations neither decide continuity
nor identify a continuous extension. No p-adic compactness is inferred from
that finite record.

Verdict: **PROVED LOCAL (paper proof; classical compactness method)** for the
analytic source theorem and quantitative condition; **REFUTED** for unrestricted
finite interpolation implying global realization; **TESTED MODEL** for the
finite rational instruments. E35/E37 audited claims survive. One E37 wording
correction is requested in X09_REVIEW.md. E38's source-phase firewall persists:
existence of a holomorphic realizer supplies no phase authentication, Euler
law, Gamma uniqueness, completed-Weil identity, or RH conclusion.

## 8. Remaining obstruction and next falsification opportunity

An application must actually establish a uniform coefficient envelope and a
closed source class before invoking this theorem. A smaller pole-free local
disk may be appropriate for a Gamma expression, but no such bound for an
arbitrary candidate is manufactured here. Closedness proves existence only;
uniqueness requires injectivity of the selected evaluation map on R. The next
falsifier is to inspect a proposed source family whose fitted polynomial
coefficients grow without one common bound, or a global source law that is
not preserved under coefficient limits. Either kills this particular route.
A numerical fit with a small recurrence defect does not establish either
premise.

## 9. Cross-domain connection beyond the donor union

B09's discrete cylinder proof becomes an approximate complex-valued report
problem. The uniform geometric tail gives the explicit continuity modulus
needed to transport coefficient compactness to a genuine holomorphic function
space. The alternating interpolation witness then identifies exactly why the
Archimedean and p-adic finite-prefix ambiguities are not solved merely by
completing report coordinates. Adding the common source bound plus closed
source laws is a new sufficient **condition**, not a hidden claim that these
laws follow from the original arithmetic inputs. This is a typed, quantified
bridge from source topology to analytic observation completion.

## 10. Deliverables and reproduction

- `observational_succ/swarm_cross09.py`: exact interpolation, coefficient-tail
  enclosure, sharp pairwise bound, independent Gamma and Mahler controls.
- `tests/test_swarm_cross09.py`: 8 passing tests; independent finite tail-cube
  checks, exact-fit countermodels, source-coupling and domain mutations.
- `scripts/swarm_cross09_probe.py`: deterministic receipt generator.
- `X09_RECEIPT.json` and `X09_REVIEW.md`: frozen exact results and audit scope.

Executed successfully in the isolated X09 worktree:

```sh
python -m unittest discover -s tests -p 'test_swarm_cross09.py' -v
python scripts/swarm_cross09_probe.py --output research/2026-10-13/SWARM_ATLAS/X09_RECEIPT.json
```

The root integrator owns full-suite/provenance validation. X09 changes no
shared registry, archival theorem, existing formal module, or source default.
