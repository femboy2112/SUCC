# Two languages, one circle: algebra–trigonometry translation and path-observation obstructions

**Date:** 2026-10-11. **Status:** user-originated cross-language ObsSUCC research question; CLASSICAL mathematical equivalences; PROVED LOCAL finite constructions and mathematical counterexamples; UNVERIFIED universal categorical/physical theory. No RH proof or academic priority claimed.

**Dependencies:** [Knowledge-aided SUCC](../2026-10-10/KNOWLEDGE_AIDED_SUCC_LADDER.md) and [Relative SUCC](RELATIVE_DELTA_PROOF_SHAPES_AND_FROZEN_BASE.md), stacked draft SUCC PRs #6–#9. Source/architecture provenance remains pinned and imported artifacts unmodified.

## 1. Exact originating experiment and strict shared-observation conditions

The maintainer proposes two observers who use different languages: A prefers polynomials/algebra, B trigonometric identities/geometry. Both probe the **same circle**. They may need a shared observational meaning/basis or an intermediary to translate meaningfully.

**Strongest faithful reading:** compare genuinely different syntax and inference libraries, not separate realities or inherently different physical instruments. Use the *same underlying point and path observations*, with the same permitted raw empirical probes, when claiming direct cross-language equivalence. If one observer is given extra time/path observations and the other sees only an unlabeled point set, there is a probe-interface asymmetry, not a theorem that polynomial mathematics cannot represent topology.

Let C be the unit circle
\[
C=\{(x,y)\in\mathbb R^2:x^2+y^2=1\}.
\]

- A's algebraic language has polynomial coordinates x,y and relation x²+y²=1.
- B's angular language has a parameter θ mod 2π, cosine/sine and angle-addition rules.
- Their common semantic basis is a calibrated oriented Euclidean plane and the same actualized probe records. Without calibration, even "counterclockwise" and "angle 0" are not determined by the abstract point set.

The abstract translation problem is a **span of semantic interpretations**, not necessarily a direct translator:
\[
\mathcal L_A \xrightarrow{\operatorname{Interpret}_A}
\operatorname{Obs}(C)
\xleftarrow{\operatorname{Interpret}_B}\mathcal L_B.
\]

For an individual expression F in A, a translated B-expression T(F) is *semantically valid* on the declared observation domain D iff
\[
\forall d\in D,\quad
\operatorname{Eval}_A(F,d)=\operatorname{Eval}_B(T(F),d).
\]
This is an equality of interpreted reports. A **full-fidelity** observer translator must additionally preserve admissible probes, inferential rules and relevant future/path structure. Literal lexical equivalence or matching finitely many examples does not suffice.

## 2. A real algebraic bridge (CLASSICAL, exact rational software model)

For static polynomial-valued observable functions, the two languages are equivalent:
\[
\boxed{
\mathbb R[x,y]/(x^2+y^2-1)
\ \simeq\ \mathbb R[\cos\theta,\sin\theta].
}
\]

Map the residue classes of x and y to cosine and sine. The circle relation maps to cos²θ+sin²θ−1=0. Surjectivity onto the declared right-hand ring is immediate by its generator definition. For injectivity, divide any polynomial F(x,y) by the monic y²+(x²−1) to obtain
\[
F(x,y)=Q(x,y)(x^2+y^2-1)+A(x)+yB(x).
\]
If F vanishes at every circle point, then for each x in (-1,1) evaluate at y=±√(1−x²). The two equations imply A(x)=0 and B(x)=0 on an infinite interval; each is a polynomial, so each is identically zero. Hence the kernel is exactly the ideal (x²+y²−1).

**Provenance:** Darij Grinberg, *Lecture 29*, §5.2, August 2026, https://www.cip.ifi.lmu.de/~grinberg/t/23wa/lec29.pdf. The full result is classical, not an original result of ObsSUCC.

Our installed-code module uses the **rational coefficient subring**, Q[x,y]/(x²+y²−1), with canonical normal form A(x)+y B(x), and a separate exact finite Fourier/Laurent implementation of rational-coefficient trig polynomials. It checks the map in both directions, addition/multiplication, identities, and adversarial typed inputs. This is an implementation with tests, not a formal proof assistant verification of the classical general theorem.

A particularly useful shared operation is the group law. Write a point as x+iy on the complex unit circle; composition is
\[
(x,y)\odot(u,v)=(xu-yv,\ xv+yu).
\]
The angular interpretation is addition of angles. The exact rational stereographic chart
\[
t\longmapsto\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right)
\]
lets A express many rotations with rational coefficients. At t=1/2 the point is (3/5,4/5), while t=1/3 produces (4/5,3/5); the group composition is exactly (0,1), a quarter turn. Both languages agree.

## 3. Three genuine defects in an overconfident translator

### 3a. Orientation and phase are not determined by an uncalibrated circle

The mappings
\[
\theta\mapsto(\cos\theta,\sin\theta),
\qquad
\theta\mapsto(\cos\theta,-\sin\theta)
\]
both satisfy the same polynomial circle equation. Both yield valid algebra-to-trig translations, but the second reverses orientation. Their signed winding numbers differ by a minus sign.

The intended calibration must choose a distinguished zero-angle point and a positive angular orientation (or account for the O(2) gauge group of circle symmetries). An exact quarter-turn north-pole observation distinguishes two proposed handedness conventions. In the software, both orientation modes satisfy the ring identities, yet map y to opposite trig polynomials; a negative control asserts their winding signs differ.

This is **not quantum gauge theory** or a novel source of physics; it is conventional coordinate calibration. It nevertheless matters whenever A and B claim to transmit *oriented* paths, not just a circle point-set.

### 3b. A good coordinate chart can omit a genuine point

The rational stereographic parameter t∈R maps onto every circle point **except (-1,0)**. The inverse
\[
t=\frac{y}{1+x}
\]
is undefined at that one point, even though the circle is perfectly regular there. Add the projective point t=∞ or another chart to cover it.

Therefore a translator that uses only one rational chart is incomplete for reasons of its **source map/atlas**, not because the physical circle is intrinsically unknowable. Treat this as a sigma/source-map defect: the missing parameter does not entitle us to invent an observational singularity.

### 3c. Static point data do not determine a time-parametrized path

Let γ_k(t)=exp(2πikt), 0≤t≤1, for integer k. The two real coordinate observers see
\[
(x_k(t),y_k(t))=(\cos(2\pi kt),\sin(2\pi kt)).
\]
Every point lies on the polynomial circle; winding(γ_k)=k. Winding is an invariant of the **oriented loop**, not of an unordered set of points. With a lifted angle θ(t), winding is [θ(1)−θ(0)]/(2π). For C¹ paths with coordinates x,y on S¹ the exact integral is
\[
w(\gamma)=\frac1{2\pi}\int_0^1(xy'-yx')\,dt.
\]

**Constructive finite rational-time alias theorem (PROVED LOCAL):** Let t_1,…,t_m be finitely many rational sampling times and let L be the least common multiple of their reduced positive denominators. Then for every integer k,
\[
\gamma_{k+L}(t_j)=\gamma_k(t_j)\quad\text{for every j},
\qquad
w(\gamma_{k+L})=k+L\ne k=w(\gamma_k).
\]
**Proof:** L t_j is an integer, and exp(2πi L t_j)=1. The lifted-angle change for γ_k is 2πk. Thus the curves have identical measured points at all specified times but distinct winding.

At times 0,1/4,1/2,3/4,1 the examples γ_1 and γ_5 return exactly the same cardinal points. The code computes equality using exact phase fractions modulo one, without floating sine/cosine approximations. It tracks which winding number belongs to each declared source curve; it does not pretend to calculate a global winding invariant from those finite samples.

**Stronger adversarial point:** for *any finite real* sampling schedule, not just rational, one can insert a smooth full extra loop strictly between two adjacent sample times. Construct a smooth step of unwrapped angle from 0 to 2π on that sample-free time interval and exponentiate; the added factor is 1 at every sampled time, but winding increases by one. Therefore an unrestricted C∞ path family has the same finite-sample nonidentifiability, regardless of language.

**Repair under a valid restrictive prior:** If the true source belongs to the known finite family γ_k with −K≤k≤K, then a single exact sample at t=1/(2K+1) distinguishes all allowed k, because distinct integers in that range cannot differ by a nonzero multiple of 2K+1. This source-class assumption is *load-bearing*, and ideal exact phases should not be confused with physically finite precision.

**Primary conceptual reference:** Northern Michigan University, *The Fundamental Group of the Circle*, https://euclid.nmu.edu/~joshthom/ma516/lectures/lecture15.html; π₁(S¹)≅Z and path lifting are classical. The winding/coordinate line-integral formula is shown in University of Toronto MAT237 notes, https://www.math.toronto.edu/courses/mat237y1/20189/notes/Chapter5/S5.1.html.

## 4. A fresh polynomial/trig probe alias independent of winding

Even **static algebraic function identification** can fail under too few sample points. Let A's candidate polynomial observable be T_5(x)=16x^5−20x³+5x and another candidate be x. Under the trig translation,
\[
T_5(\cos\theta)=\cos(5\theta)
\quad\text{and}\quad x=\cos\theta.
\]
They agree at the four cardinal points (±1,0),(0,±1) but disagree, for example, at the rational circle point (3/5,4/5). Thus no amount of rigor in translating four sampled equalities into trig notation proves an identity on the whole circle. The program evaluates this exact countermodel with rationals. An independent degree bound/identity theorem or a genuinely separating new probe is required.

This distinguishes two mechanisms:
- The **semantic translator** between full polynomial/trig algebras is faithful.
- The **finite observational probe** that samples only certain points is nonfaithful for global function identity.

A translation failure must not be falsely attributed to the language when the actual obstruction is sparse measurement coverage.

## 5. The ObsSUCC categorical agenda

A complete cross-language observer transport should specify objects (interpreted knowledge states), morphisms (admissible observations/proofs), and a common-behavior category with at least the following squares:

1. **Value square:** translating an algebraic report and evaluating it agrees with evaluating the intended point/phase data directly.
2. **Inference square:** justified polynomial identities transport to genuine trig consequences and vice versa, not just numerical agreement on training examples.
3. **Probe-access square:** a probe A can perform corresponds to a realizable probe B can access, or the translation is explicitly partial.
4. **Path/topology square:** oriented paths and concatenations transport with their winding/homotopy information; a static point ring is insufficient by itself.
5. **Source/provenance square:** language changes do not forge measurements, alter earlier causal records, silently choose an orientation, or smuggle an unverified infinity-stage completion.

Two different architectures are possible:
- **Direct equivalence** on a restricted subdomain, e.g. the polynomial-on-circle/trig-polynomial ring.
- **Intermediary span** through a shared interpreted phenomenon, with A→C←B, which supports partial translation and makes lost invariants explicit.

The exact finite code proves only the algebraic point-report portion and samples explicit topological failure modes. It does **not** construct a general fully faithful functor or a physical observer interpreter. A full Yoneda argument still needs actual functoriality and morphism-level separation, not merely a commutative-looking picture.

## 6. Predicted probes, controls and reproducibility

| Claim | Predicted discriminator | Verdict |
| --- | --- | --- |
| Algebraic and trig-polynomial languages disagree intrinsically on the unit circle | Map x→cosθ, y→sinθ; reduce y²=1−x²; exact Laurent Fourier roundtrips | REFUTED as universal claim; classical isomorphism and exact finite tests |
| Arbitrary f(x,y)=0 on the whole circle need not vanish under trig translation | Proved kernel of substitution map is circle ideal | REFUTED; ring-isomorphism theorem |
| Equal circle point sets fix the orientation/angle convention | Map y→sinθ vs y→−sinθ | REFUTED: valid opposite calibrations |
| One finite rational stereographic chart covers every circle point | Test t=y/(1+x) at (-1,0) | REFUTED as global chart |
| Correct finite point samples uniquely determine loop winding | γ_1 vs γ_5 at quarter times; general LCM construction | REFUTED for unrestricted winding |
| No finite rational-time samples can ever distinguish k in a bounded winding family | Known |k|≤K, sample t=1/(2K+1) | REFUTED as unconditional inference |
| Four cardinal samples certify a global trig-polynomial equality | cosθ vs cos5θ; rational point (3/5,4/5) | REFUTED |
| Cross-language point translation by itself transports all future empirical and topological probes | Need path lift/time/regularity, calibrated charts and probe access | UNVERIFIED in general; explicit missing-winding countermodel |
| This circle bridge proves any RH positivity or algebraic/archimedean coupling | Source-specific completed Weil equality and independent Gamma/probe regularity absent | UNVERIFIED, not claimed |

Reproduction:
~~~sh
python -m unittest tests.test_circle_translation -v
python -m unittest discover -s tests -p 'test_*.py'
python scripts/circle_translation_probe.py
python scripts/verify_provenance.py
~~~

## 7. Ledger, next verdict-changing questions, and RH firewall

Proposed ledger:
- **O85 CLASSICAL / TESTED MODEL:** circle polynomial coordinate ring ↔ trig-polynomial ring; rational exact forward/backward translator.
- **O86 CLASSICAL / TESTED MODEL:** unit-circle rotation group law corresponds to angle addition; rational stereographic chart misses one point.
- **O87 PROVED LOCAL:** finite rational-time periodic phase samples alias infinitely many distinct integer windings; actual gamma_1 vs gamma_5 sample witness.
- **O88 CLASSICAL:** oriented smooth paths have integer winding, computed from continuous phase lifts/integrals; static circle point set does not encode it.
- **O89 REFUTED:** pointwise translator plus finitely sampled point agreement suffices for faithful winding/global-function inference.
- **O90 PROVED LOCAL:** under known bounded harmonic integer winding prior |k|≤K, a tailored exact time sample distinguishes the class.
- **O91 PROVED LOCAL:** orientation/gauge cannot be chosen from unlabeled circle membership; two valid translators reverse winding sign.
- **O92 UNVERIFIED:** fully faithful cross-language observation/proof/path/physical translator, general semantic category, RH coupling consequences.

**Next research discriminators:** 
1. Give A and B the *same raw data and probe menu*, prove translation of the oriented path differential form \(\alpha=x\,dy-y\,dx\) to \(d\theta\) with chart transitions, and preserve the integer winding under valid transport. Include the orientation-flipped negative control.
2. Upgrade the shared basis from simple point identity to **probe-labeled path category**, specify translations on both objects and morphisms and prove composition/identity laws. Check whether two local translators require an intermediary third chart and whether the overlap cocycle closes.
3. Calibrate source-map inadequacy: model a single stereographic chart missing (-1,0), then add a second chart and prove exact transition on the overlap. Distinguish source-map repair from new source observation.
4. Introduce *model-relative cost*: which translated proof is shorter in polynomial versus trig syntax, and when does a third shared basis reduce total description cost **after** including translator definitions and verification?
5. Compare purely point-functional observables with dynamic phase, path concatenation and winding, then build the first continuation-equivalence theorem **across unequal languages**.
6. Stress-test an arithmetic/analytic translation only after the circle benchmark is fully verified. RH requires Euler/Gamma/source-derived data, valid domains and no zero-reading, not circle analogy.

**Verdict:** The unit circle provides an unusually clean calibration pair: pointwise algebraic and trigonometric observer languages are classically equivalent; their current available probes, orientation, chart domains and path histories need separate preservation theorems. The finite rational-time winding alias is an exact counterexample to naive transfer of global path completion from successful local sample matching. This is a strong bounded laboratory for ObsSUCC's "same field, different language" frontier—no novel fundamental physical theorem is asserted.
