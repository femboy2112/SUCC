# Pi normality: an exact dyadic source and the base-3 rigidity alternative

**Date:** 2026-10-24.
**Research branch:** `research/pi-dyadic-prime-base-rigidity-2026-10-24`.
**Parent:** twisted-observer draft #268, `06f6b03eed2521c6bd5c02db618cb421ac6b5a51`.
**Coherent main inspected:** `e648df3e4fca73ab6b942232b5ca4b310e9cac08`, after #267.

**Result:** the authentic unwrapped BBP source is a bijective 2-adic isometry
of its time index. Its dyadic residue collisions satisfy a proved 1/16
refinement bound. The required real-circle estimate is still open. A second
route shows precisely how base 3 could make a positive all-scale collision
exponent sufficient, using an explicit classical rigidity theorem.

**Pi normality remains OPEN.** No independence theorem, new Lean authority,
or scholarly priority is asserted. The new results have paper-proof and
exact-finite authority at the scopes stated below.

## 1. Live frontier and the question actually tested

The current repository integrates the source/circle/prime-clock program through
#267. The selected-source collision criterion from #265 is on main. Draft #268
adds the twisted-observer results and the inverse-branch refinement target;
this continuation is stacked on its exact head. The separate #266 lag/carry
branch is a cited donor, not silently merged into this branch.

The recent conversation proposed applying the circle construction to the
2-adic base, relating higher prime bases through a bounded differential, and
possibly using only base 3 or primes below 16 because 16=4^2. The strongest
faithful reading has three distinct mathematical questions:

1. Can the actual source be given an exact dyadic coordinate, with quantitative
   refinement rather than only an analogy to prime clocks?
2. Can a bounded carry transport the same inverse-branch information among
   circle and prime-coordinate descriptions?
3. Can such a transport control the selected probability law sufficiently to
   prove normality, perhaps using one additional multiplier?

The first two now have additional exact answers. The third remains a source
law problem with two precisely stated routes.

### Correction to the inherited half-bound description

In #268, the real-source inequality with retention theta=1/2 was an **open
premise**, not a proved bound. Its conditional conclusion is
K_p(1)=O(p^(3/10)); theta=1/16 would make K bounded. This round proves a
one-sixteenth statement for the authentic **unwrapped dyadic statistic**.
It does not retrospectively prove either real-circle premise.

## 2. The new source theorem

Use the authenticated rational source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n),\quad y_n=\{U_n\}.
$$

The collapsed denominator of r is odd on all 2-adic integers. The exact
difference quotient of r(x)-r(y) is a 2-adic unit. Define the convergent
backwards Green series

$$
F(t)=\sum_{j\ge0}16^j r(t-j).
$$

The j=0 term controls its difference quotient, and every later term is
divisible by 16. Thus F is a bijective 2-adic isometry. The additional identity
F(0)=0 authenticates the zero-initial source, giving

$$
F(n)=U_n,\qquad
v_2(U_s-U_t)=v_2(s-t).
$$

The proof of F(0)=0 is not a numerical extrapolation. The reversed-source
series is an analytic primitive of

$$
\frac{t(1-t)}{(1-2t^2)(1-2t+2t^2)}.
$$

The Mobius map (1-t)/(1-2t) exchanges 0 and 1 and preserves the relevant
quadratic differential on one overconvergent 2-adic analytic disc. It forces
the residual primitive to vanish; the remaining logarithms vanish at the
endpoints. The [complete proof](PI_DYADIC_SOURCE_ISOMETRY.md) specifies the
disc, convergence, integration convention and the identity log(-1)=0.
This is not an assertion that real pi has become zero in another field.

### The actual one-sixteenth bound

For any consecutive N source indices, let P_k count ordered pairs with
U_s=U_t modulo 2^k. Put M=2^k and N=qM+r with 0<=r<M. Then

$$
P_k=r(q+1)^2+(M-r)q^2
=\frac{N^2}{M}+r\left(1-\frac rM\right).
$$

The count is independent of the starting index. In particular,

$$
P_{k+1}\le\frac12P_k+\frac12N,\qquad
P_{k+4}\le\frac1{16}P_k+\frac{15}{16}N.
$$

These are exact universal source statements with the diagonal retained.
The four binary losses compose coherently in this dyadic coordinate.

Another consequence is the all-depth denominator formula for the rational
BBP truncation P_N=16^(1-N)U_N:

$$
v_2(P_N)=v_2(N)-4(N-1),\qquad
\text{base-16 preperiod}=N-1-\left\lfloor\frac{v_2(N)}4\right\rfloor.
$$

The inherited odd-depth statement is a special case. This is a useful
arithmetic corollary even if the normality bridge remains unresolved.

### Exact boundary: the carry is not optional

The real state is obtained by subtracting the cumulative integer carry:

$$
U_n=C_n+y_n,\qquad C_n=16C_{n-1}+c_n,
\qquad c_n=16y_{n-1}+r(n)-y_n.
$$

The real collision count Q_W(tau) concerns circular distances between y_s
and y_t. It is not the residue count P_k. In the prescribed regime
M approximately p^(2/5), P_k approximately N^2/M, so asserting
Q_W(1/M)<=p^o(1)P_k merely restates the inherited collision target up to
constants. That proposed comparison remains OPEN; its novelty tax is explicit.

A stronger countermodel now shows why further BBP-specific information is
necessary. A different analytic isometric forcing can preserve the exact
initial zero, contracting Green identity and positive O(n^-2) real decay,
yet make every late real pair central. Its literal carries are constantly
15, while its dyadic collision counts remain perfectly balanced. The
[binary dossier](PI_BINARY_CARRY_REFINEMENT.md) constructs it by rational
Newton interpolation. It changes the four-pole formula and therefore does
not refute the authentic source; it exposes the conditional alignment that
the real-source estimate must control.


## 3. Four conditional binary gates and finite prime observation

On an endpoint-close pair, write

$$
\delta'=16\delta+e-\kappa,
\quad \delta,\delta'\in[-1/2,1/2),\quad \kappa\in\mathbb Z.
$$

If |delta'|<=tau<=1/4 and |e|<=epsilon with epsilon+tau<1/2, then

$$
\kappa\in\{-8,\ldots,8\},\qquad
|\delta|\le1/32\quad\Longleftrightarrow\quad\kappa=0.
$$

Authentic odd denominators also give the exact dyadic readout
kappa=e-delta' modulo 16. Let S_j count endpoint-close pairs whose carry is
divisible by 2^j. Then

$$
\frac{Z_W(\tau)}{Q_{W^+}(\tau)}
=\frac{S_4}{S_0}
=\prod_{j=1}^4\frac{S_j}{S_{j-1}}.
$$

Four **conditional** half bounds with allowance Cn give
Z<=Q_successor/16+(15/8)Cn. Four marginal fair observations cannot be
multiplied. Likewise, 16=4^2 means two quarter losses give 1/16; two half
losses give only 1/4. Exact countercontrols are retained.

There is also a weaker aggregate sufficient target. If theta_j is the actual
central retention at refinement scale j, then the inherited geometric
inclusion and endpoint bound give

$$
Q_W(\tau_J)\le n^2\prod_{j<J}\theta_j+2nJ.
$$

It is enough for the cumulative excess over ideal binary losses to obey

$$
\sum_{j<J}\sum_{\ell=1}^4\log(2\rho_{j,\ell})\le o(\log p),
\qquad \rho_{j,\ell}=S_{j,\ell}/S_{j,\ell-1}.
$$

Individual unfavorable bits and scales are permitted. This is a sharpened
sufficient contract, not an established arithmetic estimate.

### What base 3 and primes below 16 really recover

Because the centered carry is bounded by 8, two ternary digits are enough
to recognize the central branch:

$$
\kappa=0\quad\Longleftrightarrow\quad\kappa=0\pmod9.
$$

Modulo 27 determines the whole signed carry. Separate residue marginals
modulo 11 and modulo 13 reconstruct the entire carry distribution, with sharp
sup-norm error constant 3. In contrast, separate modulo-3 and modulo-5
marginals can conceal a change in its zero mass, although their joint CRT
observation identifies zero. The [binary dossier](PI_BINARY_CARRY_REFINEMENT.md)
contains the reconstruction and exact sharpness/alias witnesses.

Identification does not prescribe frequency. A uniform law modulo 9 would
give 1/9 at zero, not 1/16. The correct odd-prime target is the projection
of the actual sixteen-branch law, not uniformity in unrelated residue rings.

Full phase reconstruction is different from bounded carry identification.
At authentic index 3, projecting the rational phase onto ALL prime places
below 16 omits exactly 4/17. The source dossier gives the primary-fraction
calculation and the independent oracle checks it. Thus the small-prime
carry theorem cannot be silently read as recovery of the complete real phase.


## 4. The bounded differential across inverse circle covers

At inverse-cover degree m, a circle root x and label a represent (x+a)/m.
Multiplication by q has the exact representation

$$
(x,a)\longmapsto
\bigl(\{qx\},\;qa+\lfloor qx\rfloor\pmod m\bigr).
$$

The integer carry is bounded by q-1. For q=3 it is one of 0,1,2. The same
integer works in every prime-power coordinate and obeys

$$
\lfloor qrx\rfloor
=q\lfloor rx\rfloor+\lfloor q\{rx\}\rfloor.
$$

Thus multiplication and the 16-to-4-to-2 projections commute exactly.
All inverse covers form a common profinite fibre. They do not identify
different p-adic fields; they give compatible observations of one explicitly
defined inverse-limit object. Finite inversion spends precision: an image
known modulo qm determines a preimage label modulo m. If the q-coordinate
is absent, q distinct inverse candidates remain.

This common cover has an exact adapter from the authentic source: at degree
m take root y_n and label C_n modulo m. Its represented point is U_n/m modulo
one. The forced successor sends the label to 16C_n+c_(n+1) modulo m, using
the SAME literal carry that updates the real root. Multiplication by q gives
the cover of qU_n exactly. The analytic oracle checks 728 such source-cover
transports at eight moduli. This connects the new geometry to the actual
source, while making no assertion that qU_n is another selected source time.

The source isometry gives a second, source-specific family
sigma_q=F-inverse times q times F on dyadic time. It is coherent for every
odd prime. Nevertheless sigma_3(10)=14 modulo 32 has authentic real-circle
mismatch greater than 0.49. The held-out 10-bit canonical time permutation
has mean real circular cost in [0.250518593099,0.250518593100]. Perfect
dyadic alignment is therefore not a real transport estimate.

In fact for every positive source index n and every odd integer 1<q<16,
sigma_q(n) is not a nonnegative integer: positivity of the forcing gives
U_n<qU_n<U_(n+1), whereas an ordinary source time would require equality
with some U_m. Approximate empirical-law couplings remain a separate option.

### An exact real fractional-time translator

The authentic source also has a real interpolation V(n)=U_n with
V(t)=16^t T(0)-T(t), where 0<T(t)<1/((8t+1)(8t+2)). For any integer q>1,
put a=log_16(q). Then

$$
V(t+a)-qV(t)=qT(t)-T(t+a),\qquad
0<V(t+a)-qV(t)<\frac{q}{(8t+1)(8t+2)}.
$$

This is a source-derived bounded translator, but it lands on fractionally
shifted times. If mu_a is the law of V(n+a) on the same integer index window,
then the difference between the q-invariance defect and W1(mu_a,mu) is at
most q/((8A+1)(8A+2)). The discrete sampling debt is therefore equivalent
to the existing invariance target, not a new saving. Continuous time averages
do satisfy a bound q/((8A+1)(8A+2))+a/(2L); replacing the discrete source by
that continuous average would be invalid. The base-3 dossier proves all
these statements, including the real tail bound at noninteger times.

## 5. One extra multiplier can change the required bound

Let mu_p be the empirical law of the SAME authentic source window. Its weak
limits are already times16-invariant, by the recurrence, forcing O(p^-2)
and an endpoint error O(1/N). Seek

$$
W_1((T_3)_*\mu_p,\mu_p)\longrightarrow0,
\qquad T_3(x)=3x\pmod1.
$$

Suppose also that every weak limit has a positive all-scale collision
exponent: Q_mu(r)<=C r^s for some s>0. Then every limit is Haar.

The proof uses the classical Rudolph-Johnson theorem in its nonergodic form:
if a law nu is invariant under two multiplicatively independent multipliers,
and h_nu(T16)=eta log16, then nu>=eta times Haar. The collision bound implies
h_mu(T16)>=s log16. Subtract the resulting s Haar component and normalize.
The residual inherits both invariances and the same positive collision
exponent. Repeating forces all mass to be Haar. Positive average entropy
alone would not suffice; the residual argument removes that gap.

The all-scale theta=1/2 premise from #268 would supply s=1/4. Therefore:

$$
\text{uniform half retention}
+\text{same-law tripling invariance}
\quad\Longrightarrow\quad
\text{pi normal in bases }16,4,2.
$$

Both source-specific premises are OPEN. This route avoids demanding the
full 1/16 real-circle loss, but introduces a genuinely independent symmetry
obligation. It does not assert that pi is normal in base 3: the law being
transported is the base-16 orbit law, not the separate orbit 3^n pi.

The [base-3 dossier](PI_BASE_THREE_RIGIDITY.md) proves the weak-limit step
with moving radii carefully, supplies a prefix-uniform weakening, and records
a counterexample to replacing it by a terminal-scale bound. A stationary
process alternating increasingly long uniform blocks and zero blocks has
terminal collision savings and asymptotic tripling invariance, but tends to
one-half Haar plus one-half an atom. Every-scale information matters.

## 6. Executed finite probes

The [contract](PI_DYADIC_BASE_PREREGISTRATION.md) fixes the new measurements.
The [receipt](PI_DYADIC_BASE_RECEIPT.json) retains every row, signed carry
count, conditional ratio, diagonal, lower/upper enclosure and source hash.
The decimal values below are rounded displays of exact outward rational
intervals of width at most 10^-12.

For tripling, the lower bound uses a 1-Lipschitz circle observable. The upper
bound is the cost of an explicit sorting-based source-index permutation;
it is not asserted to be optimal circle transport. Same-index matching is
shown as a control for the wrong coupling rule.

| p | N | tripling lower bound | explicit transport upper bound | same-index cost |
|---:|---:|---:|---:|---:|
| 73 | 27 | 0.011438809303 | 0.177035689865 | 0.250771010538 |
| 193 | 72 | 0.021677816245 | 0.100247088315 | 0.241197127399 |
| 353 | 132 | 0.007601302318 | 0.040372210453 | 0.245986612712 |
| 577 | 216 | 0.006823610850 | 0.024444180176 | 0.234158820515 |
| 1153 | 432 | 0.012095208236 | 0.018457114013 | 0.250100497397 |
| 1601 | 600 | 0.010387914859 | 0.014332652404 | 0.249739565288 |
| 2081 | 780 | 0.010437135136 | 0.013862510903 | 0.250033052966 |
| 4129 | 1548 | 0.001465634615 | 0.007477481901 | 0.249215268448 |

The lower-bound column is displayed rounded, not rounded downward; consult
the receipt for rigorous lower endpoints. No exponent is fitted to this table.
The windows share a deterministic source and often overlap; they are not
independent statistical samples. These finite costs do not prove decay.

Twenty diagnostic branch scales were checked. At p=1601 and tau=1/4, the
nested counts are

$$
(180493,\;90085,\;45337,\;22919,\;11793).
$$

The four conditional retentions are approximately 0.4991, 0.5033, 0.5055,
0.5146, with product approximately 0.065338. At finer diagnostic radii,
the diagonal dominates and raw retentions approach one; those unfavorable
rows are retained and their linear allowances are explicit. The diagnostic
radii are not substituted for the prescribed asymptotic schedule.

Complete dyadic forcing/source permutations were checked through 12 bits;
odd gains 3,5,7,11,13 were checked with composition and inverse transport.
The authentic p=2081 real collision replay again gives 76544 ordered pairs
at radius 1/16, while the dyadic count is exactly 38028. These are different
events on the same source. The real scaled collision is 5888/2925; the
dyadic scaled collision is 12676/12675.

## 7. Dependency cut and next research contract

| Candidate | Earned result | Remaining arithmetic obligation |
|---|---|---|
| Exact 2-adic source interpolation | Proved, including zero authentication and 1/16 refinement | Carry-sensitive comparison with the real source |
| Four conditional binary carry gates | Exact identity, controlled composition and aggregate criterion | Sublinear cumulative logarithmic excess |
| Finite ternary or 11/13 observation | Exact branch identification and stable tomography | Source frequency control; observation alone does not supply weights |
| Second-multiplier rigidity | Proved conditional route with countermodels and scope | Positive all-scale real collision exponent AND selected-law tripling transport |

The principal next moonshot is a **source-authenticated tripling transport on
the common carry space**, together with the weaker first-saving real bound.
It changes the required dimension target instead of simply renaming maximal
entropy. It remains meaningful even if the dyadic interpolation theorem were
removed: its classical rigidity conclusion is an independent route.

### Hole contract

- **Object:** the empirical law of y_(m+1),...,y_(4m), with actual initial zero
  and all literal carries, for every sufficiently large good prime p=8m+1.
- **First target:** prove a positive uniform all-scale real collision exponent,
  for example the theta=1/2 premise from #268, with constants independent of p.
- **Second target:** construct or bound a source-derived coupling of this same
  empirical law and its tripled image with mean circular cost tending to zero.
- **Weak sufficient forms:** each weak limit may have its own positive exponent;
  fixed-character tripling defects tending to zero also imply the same symmetry.
- **Closure:** the proved rigidity/coverage theorem then gives binary normality.
- **Novelty tax:** this is a conditional splitting into two arithmetic tasks;
  neither is currently discharged. It is not claimed weaker than normality
  merely because the conditions look different.
- **Cheapest falsifiers:** an authentic carry event outside the proposed domain,
  loss of source initial zero, a non-bijective alleged coupling, or a rule that
  also accepts the concentrated and alternating-block controls.
- **Finite boundary:** the present receipt calibrates only the displayed finite
  windows and quotients. No fitted rate or all-prime assertion follows.

The alternative direct route remains worthwhile: prove a bound on cumulative
binary retention excess. The weakest decisive new result would already be a
uniform real-source saving at a prefix-uniform positive density of scales.
Purely modular gains and repeated small-prime probes cannot substitute for it.

## 8. Provenance, primary sources and validation

Three same-model lanes used distinct tasks: binary carry construction,
arithmetic/p-adic proof and adversarial controls, and independent-multiplier
rigidity. A second lane audited the p-adic analytic zero proof. The root
checked the algebra, source definitions, classical hypotheses, countermodels,
code and exact receipts. This is not independent external refereeing.

The [claim supplement](../../docs/CLAIM_SUPPLEMENT_DYADIC_BASE_TRANSPORT.md)
registers DBT-01--21. The [validation record](PI_DYADIC_BASE_VALIDATION.md)
contains the executed gates, setup issues, logs, and exact scope.
Historical imported originals and previous claim rows are preserved.

Primary sources:

1. Bailey, Borwein and Plouffe, [On the Rapid Computation of Various
   Polylogarithmic Constants](https://www.davidhbailey.com/dhbpapers/digits.pdf),
   the authentic BBP identity.
2. Rudolph, [times2 and times3 invariant measures and entropy](https://doi.org/10.1017/S0143385700005629),
   including the relatively prime multiplier generalization.
3. Bourgain, Lindenstrauss, Michel and Venkatesh, [Some effective results for
   times a times b](https://www.math.ias.edu/~akshay/research/blmv.pdf),
   Theorem 1.3, the nonergodic entropy-to-Haar domination used here.
4. Becher and Slaman, [On the Normality of Numbers in Different
   Bases](https://math.berkeley.edu/~slaman/papers/bases.pdf), Theorem 5 and
   multiplicative-dependence boundaries. Normality at all prime bases alone
   does not automatically give normality at every composite base.

**Final boundary:** this round proves new-to-repository source arithmetic and
exact transport machinery, and establishes a carefully scoped alternative
conditional route. It does not prove pi normality, real tripling invariance,
or the authentic real-source half-retention bound.
