# Edge-carrier reconstruction laboratory: one-loop SUCC → Z → Q → Z[i]/Q(i), profinite Z and finite adeles

**Date:** 2026-10-15. **Branch:** research/edge-carrier-reconstruction-2026-10-15. **Parent:** research/rh-carrier-tate-functor-2026-10-15@e1cfae4fba4632e1e936d57943263e470467d27b (draft PR #120). **This is a solved-problem calibration campaign, not an RH claim.**

**Author's originating objective:** start with smaller carriers such as N, Z, Q, C and the adeles A, and construct a source-justified system of categorical edges whose formal paths and gluing provide an interface **isomorphic to a larger carrier's actual internal algebra/graph**, not just a same-sized set or a picture of one.

**Classical theorem imports:** group completion / Grothendieck group, categorical localization, ring localization, Gaussian integer presentation, Yoneda full faithfulness, CRT and profinite inverse limits, topological completion of Q(i), and the standard finite-adele localization. The executable contributions below are new SUCC integrations and proof checks, not discoveries of these classical mathematical results. **RH PROVED: NO.**

## 0. Recovery of the target: different equivalences must remain different

An admissible SUCC reconstruction contract declares:
1. Source carrier, generators (edge sorts), relations and allowed inversions/completions.
2. The *target* carrier category (monoid, group, ring, field, topological ring, metric-complete field, category with observational structure).
3. Exact comparison map and invariant, with quantified inverse / universal property; data preservation must include source law and causal cost.
4. Whether morphism completion is an **isomorphism** onto the large carrier, the original map is merely an **embedding**, or a finite evaluator describes **one point** of a much larger completed carrier.
5. Source/epoch identity, actual access, finite proof certificate versus finite-precision sample, failures, next falsification.

For categories, an equivalence functor is fully faithful and essentially surjective; for one-object monoid categories, an equivalence is an isomorphism of their endomorphism monoids. **The original B(N) and B(Z) are NOT equivalent categories. The localized B(N)[s^-1] and B(Z) ARE isomorphic.** For rings/fields, preserving merely underlying cardinality is never enough.

## 1. EC-01: one object + one generating endomorphism reconstructs Z as edges

Take the directed graph with one vertex * and one loop s:*->*. Its free category C has morphisms s^n (n>=0), with s^m∘s^n=s^(m+n). Thus End_C(*)=(N,+).

Form the localization L=C[s^-1] by freely adjoining the inverse of s. Every arrow in L is represented by a finite signed word s^{epsilon_1}...s^{epsilon_k}, epsilon_i in {+1,-1}. Adjacent inverse letters cancel; the canonical reduced form is s^z, z=sum epsilon_i in Z. Therefore

    Aut_L(*) ≅ (Z,+)    by  [s^z] ↦ z.

Proof: composition adds exponent sums; s^z∘s^-z=id; any equality follows from inverse cancellations and the exponent homomorphism into Z, which is a two-sided inverse on canonical words. Formal pairs (a,b)∈N² represent s^a(s^-1)^b; equality is exactly

    (a,b) ~ (c,d) iff a+d=b+c.

The canonical representative is (max(z,0),max(-z,0)), z=a-b. The original map n↦s^n is injective because N is cancellative.

**Universal property:** any monoid map from (N,+) to a group G sending the generator to g uniquely extends to Z by z↦g^z. In additive cyclic G=Z/m, this is z↦zg mod m. This is the *construction proof*, not a finite sample extrapolation.

Choosing a basepoint for a free transitive Z-torsor gives an honest bijection between these loop arrows and vertices of a bilateral integer line. Without a basepoint, the torsor has no canonical coordinate map. The object set of C still has one object: **the recovered integers are initially morphisms**.

**Hostile control 1 (graph shape):** if instead one builds the *ray* 0->1->2->..., then freely inverts its forward edges, the resulting graph-groupoid is thin and connected (unique reduced path between any vertices, since a ray is a tree). Aut(0) is trivial, NOT Z. The self-loop and its composition law matter; merely counting arbitrarily many SUCC states is insufficient.

**Hostile control 2 (cancellation):** if the original monoid has nonzero e with e+e=e, any homomorphism to an abelian group sends e to 0 by cancellation. Its group completion loses source distinctions. Thus 'formal inversion always gives a faithful isomorphism of the starting carrier' is REFUTED.

Code: NatLoop, IntegerLoop (raw history pairs + explicit quotient equivalence), RayPath, cyclic_target.

## 2. EC-02: Z carrier → fraction field Q by edge localization

Now equip the completed integer carrier with ring operations. Let S=Z\\{0} be the multiplicative arrows to invert. Its localization is the set of pairs (a,b), a∈Z and b∈S, with

    (a,b) ~(c,d) iff ad=bc

and operations

    a/b+c/d=(ad+bc)/bd,
    (a/b)(c/d)=ac/bd.

Because Z is an integral domain, the map a/b↦(ordinary rational a/b) is a well-defined **ring/field isomorphism** S^-1Z≅Q. The full universal property: every unital map f:Z→R taking every integer b≠0 to a unit of R uniquely factors as f~(a/b)=f(a) f(b)^-1.

**Important:** extending to finite-stage S-integers Z[S^-1] (S finite genuine primes) inverts ONLY those primes and their products. The inclusions Z[S^-1]→Z[T^-1] for S⊂T preserve +,× and the original source. Their filtered union over all finite S is Q. None of these source restrictions implies an external physical observer has evaluated infinitely many places.

**Hostile control:** localization is not generically faithful. In Z/6Z, the nonzero element 3 is annihilated by 2; inverting 2 forces 3 to zero. The ring localization exists, but the original source embedding collapses. Declaring it an isomorphism of the starting ring is false. Choosing an actual integral domain (Z) is load-bearing.

Code: RationalSpan, SLocalization. Tests compare to independent Python Fraction arithmetic and existing SUCC S-integer laws.

## 3. EC-03: Z x Z with a polynomial relation reconstructs Z[i], then Q(i)

Two completed integer path coordinates (a,b) acquire a ring law when we adjoin a generator i with i²=-1:

    (a,b) + (c,d) = (a+c,b+d),
    (a,b) * (c,d) = (ac-bd,ad+bc).

This is the quotient ring Z[X]/(X²+1) ≅ Z[i], not the coordinatewise product ring Z×Z. Conjugation (a,b)↦(a,-b) and norm a²+b² are preserved. The ring embeds into its fraction field Q(i)≅Q×Q with this **complex** multiplication, whose nonzero elements have inverse (a-bi)/(a²+b²).

**Boundary:** Q(i) is a *proper* countable dense subfield of the usual complex numbers C; without the Archimedean metric/completion it is not C. For instance sqrt(2)∉Q(i) by the parity argument for irrationality.

Code: GaussianInteger, GaussianRational. The ring operations are not inferred from generic cardinality or an arbitrary product of source sets.

## 4. EC-04: Q(i) Cauchy sequences reconstruct full C by metric completion

Equip Q(i) with the ordinary complex absolute value. The Cauchy-sequence quotient modulo sequences tending to zero is a complete field, canonically isomorphic to C:

    C ≅ Cauchy(Q(i)) / null.

The construction preserves norm/topological field operations and supplies the missing Archimedean structure. This is a classical completion theorem: it concerns **all** Cauchy sequences, most of which have no finite computable name.

**Executed test-point:** The finite source program GaussianCauchyRoot2 supplies rational Gaussian approximations to sqrt(2)+i*r, r∈Q. At decimal depth n set D=10^n and a_n=floor(sqrt(2 D²)), computed by exact integer isqrt. Then

    a_n/D < sqrt(2) < (a_n+1)/D,
    interval width = 10^-n.

For m≥n the approximations differ by strictly less than 10^-n and share the same rational imaginary coordinate, so they form a Cauchy name with an explicit modulus. Their limit is outside Q(i) but inside C.

**No-ghost claim:** one finite Cauchy-name program realizes one new point, not every complex number. The full field-isomorphism is imported by the mathematical completion theorem, NOT implied by checking forty approximants.

Code: complex_cauchy_edge.py and corresponding exact tests.

## 5. EC-05: finite modular edge diagrams reconstruct the profinite integers

For positive integers n ordered by divisibility, let X_n=Z/nZ. An edge m→n exists exactly when n|m, and is the ring homomorphism reduction modulo n. This is a genuine category/diagram of finite rings.

A **global compatible cone** is a family (x_n) such that for all n|m, x_m mod n = x_n. The ring of these cones is by definition the inverse limit

    Zhat = lim_(n|m) Z/nZ.

This is a topological ring, not merely a set of similar cardinality. Its projections are continuous, joint-injective, and induce its inverse-limit topology. Every compatible family is a UNIQUE point of this inverse limit; the proof is a universal-property argument, not an omega-stage physical observation.

The Chinese remainder theorem gives a natural topological ring isomorphism

    Zhat ≅ product_(p genuine prime) Z_p.

**Constructive categorical atoms:** for each real prime p, define an idempotent e_p in Zhat with p-component 1 and all other prime components 0. At modulus n=p^k m with gcd(m,p)=1, calculate e_p(n) by the two CRT congruences

    e_p(n) ≡ 1 (mod p^k),
    e_p(n) ≡ 0 (mod m).

Concretely, e_p(n)=m*(m^-1 mod p^k) mod n, and e_p(n)=0 if p∤n. Then

    e_p²=e_p,   e_p e_q=0 for p≠q,
    sum_(p|n) e_p(n) = 1 mod n.

**Non-isomorphism of the original source:** Z embeds diagonally into Zhat via n↦(n mod m)_m, and that map is injective, with dense image, but NOT onto. e_p cannot come from any ordinary integer a: if a=0 in Z_q for q≠p then a divisible by q^k for every k and hence a=0, contradicting a=1 in Z_p. Z has no nontrivial idempotents, while Zhat does. Thus an exact difference in ring structure proves the completion strictly larger.

**Size boundary:** there are 2^aleph0 distinct idempotents from arbitrary subsets of primes (their component flags), but only countably many finite program descriptions. The implementation provides a subclass of computably specified Zhat points with finite-work per residue query; it does NOT enumerate every global point.

**Hostile control:** for every finite observation horizon H, the different source integers 0 and L=lcm(1,...,H) have identical residues modulo all n≤H. The difference becomes visible at modulus L+1. A large finite set of compatible observations does not prove injectivity at the full source level.

Code: ProfiniteProgram, finite_prime_partition, prime_projector_is_not_integer, finite_clock_collision.

## 6. EC-06: finite adeles A_f from the profinite source, full adeles A from R

The finite adele ring of Q is the restricted product

    A_f(Q)=product'_p (Q_p, Z_p),

meaning an element x=(x_p) is p-integral at all but finitely many places. There is a classical natural algebraic ring isomorphism

    A_f(Q) ≅ Zhat [ (Z\\{0})^-1 ]
           ≅ Q tensor_Z Zhat.                                 (6.1)

Proof: Any restricted adele x has finitely many negative prime valuations. Choose a positive integer D with v_p(D)≥-v_p(x_p) at those finitely many places, so Dx belongs to product_p Z_p ≅ Zhat. Hence x=u/D. Conversely every u/D is integral outside primes dividing D. Multiplication by nonzero D is injective on Zhat because each Z_p is a characteristic-zero torsion-free domain, so the localization equivalence is exactly the equality in the restricted product. With the corresponding restricted-product/inductive-limit topology, this is an isomorphism of topological rings as well. The topology is a specified classical input; no finite CRT program establishes it by sampling.

The full rational adele ring adds the **genuine real carrier**:

    A_Q = R × A_f(Q).

A rational real chart provides a useful dense example; it is not all R. Nor is A_f a field: the genuine nonzero projectors e_p and 1-e_p have zero product. Adjoin R as an actual complete Archimedean factor, not as an imaginary 'prime at p=infinity' manufactured by a finite ring.

**Executed restricted model:** FiniteAdeleSpan represents expressions u/D with u a computably specified profinite source program. It computes all finite p-adic scaled-residue probes and conservatively refuses to conclude global equality from a single modulus. RationalArchimedeanAdeleChart carries a rational Archimedean example. The source-faithful restricted-product *theorem* establishes the full carrier A_f; code does not enumerate every adelic coordinate or certify arbitrary physical access.

**Independent controls:** Exact rational diagonal embedding Q→A_f; p-adic denominator scaling, CRT nonrational idempotents, zero divisors, non-equivalence under finite aliases and strict source epochs.

## 7. EC-07: Yoneda checks the edge-to-carrier interface itself

For any small category C, Yoneda provides a fully faithful embedding C→[C^op,Set]. If c,d are objects then

    Nat(Hom(-,c), Hom(-,d)) ≅ Hom_C(c,d).

In the one-object category B(Z/m), the representable is the regular cyclic set. A natural self-map f must commute with every translation:

    f(x+a) = f(x)+a  for all x,a ∈Z/m.

Putting x=0 gives f(a)=f(0)+a, so there are precisely m such maps, indexed by the original edge k=f(0). The implementation **independently enumerates all m^m functions** for m≤6 and recovers exactly the m natural ones; arbitrary same-cardinality functions (e.g. f(x)=2x mod5) are rejected.

This checks a second, genuinely categorical version of the objective: **the full natural transformation structure recovers exactly the internal arrow algebra**, not just its number of members. It is a small known theorem calibration and builds on the repository's existing yoneda.py and operational_yoneda_descent.py (do not claim original novelty).

## 8. Source and observer limitations: classification relative to the target

| Conversion | Target as mathematical object | Original smaller carrier identical? | Finite uniform object description? |
| --- | --- | --- | --- |
| B(N)[s^-1] → B(Z) | Isomorphism of one-object group categories | No; inverses had to be added | Yes for each arrow |
| Z[(Z\\0)^-1] → Q | Field isomorphism | No; denominators add new elements | Yes for each rational |
| Z[X]/(X²+1) → Z[i] | Ring isomorphism | No: added relation/generator | Yes for each Gaussian integer |
| Completion Q(i) → C | Complete topological field isomorphism | No | Some points computably named, not all |
| lim Z/nZ → Zhat | Profinite ring isomorphism | No: Z is proper dense subring | Some points computably named, not all |
| Zhat⊗Q → A_f | Restricted-product ring isomorphism | No: introduces nonintegral local coordinates | Some points computably named, not all |

All of these *mathematical* reconstructions are Simple relative to suitable symbolic theorem/specification targets; obtaining every global element as a terminating program is impossible for uncountable C, Zhat and A_f under ordinary countable finite programs. That does not mean the **existence of their carrier** is IdealHard or Fucked. Classifications must be relative to task, execution representation, proof assumptions, source and probe closure.

## 9. Proof and software acceptance criteria

1. Every positive identification must name the mathematical category/structure; provide an explicit comparison and its inverse or universal property.
2. Arithmetic uses exact integer/Fraction/CRT, no float-equality or numerical witness promoted to global proof.
3. An uncompleted source carrier must never be conflated with its completed target.
4. No unverified source restatement, hidden physical access, nontrivial zero positions or RH positivity premise.
5. Negative controls: thin ray vs one-loop; noncancellative collapse; non-domain localization; wrong Gaussian multiplication; missing CRT prime; finite aliasing; \hat Z nonintegral idempotent; finite adeles not field; Q(i) not C; non-natural same-sized map.
6. Test across existing S-integer / Yoneda / Tate source implementations, as feasible, under exact source identity.
7. Keep source timestamps and causal receipts distinct from mathematical source-label assertions; finite test success is not universal theorem proof.

## 10. Next larger solved-problem calibration before RH

(a) Verify additive Pontryagin duality \hat Z^ ≅ Q/Z by original-source roots of unity (finite cyclic character spectra), with strict character and topology domains. (b) Build \mathbb A_Q/\mathbb Q and independently verify its self-duality and standard Tate Poisson summation for the Gaussian × finite-indicator test. (c) Recover classical zeta completion and its functional equation from this carrier route. (d) Add a signed Weil distribution on an honest test space while refusing to assume positivity.

Each step has a known mathematical theorem to recover **before attempting a new RH sign theorem**. Required falsifications include non-natural edge maps, fake prime 6, dropped real place, wrong Haar, conductor sign and half-density shifts. The full project has prior partial machinery for (b)–(d); reuse rather than invent a second, incompatible source.

## Primary and repo references

- Grothendieck group of a commutative monoid (definition and universal property): https://ncatlab.org/nlab/show/Grothendieck+group+of+a+commutative+monoid
- Stacks Project, Algebra §10.9 localization and universal property: https://stacks.math.columbia.edu/tag/00CM
- Yoneda lemma and fully faithful embedding: https://ncatlab.org/nlab/show/Yoneda+lemma
- Profinite completion of Z and CRT: https://ncatlab.org/nlab/show/profinite+completion+of+the+integers
- Formal proof project for Zhat and finite adeles QHat := Zhat⊗_Z Q: https://imperialcollegelondon.github.io/FLT/docs/FLT/Data/QHat.html
- Existing SUCC: observational_succ/yoneda.py, operational_yoneda_descent.py, infinite_realization.py, tate_lattice_descent.py, adelic_schwartz_source.py, miniature_carrier.py; AGENTS.md and docs/METHOD.md.

**Claims:** EC-01..EC-07 are classical mathematics with exact source-typed executable finite models and separately proved scope. No original academic priority is claimed.
