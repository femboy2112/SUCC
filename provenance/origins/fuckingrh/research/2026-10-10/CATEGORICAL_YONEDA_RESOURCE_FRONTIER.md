# Finite Yoneda, resource-bounded actualization, and the RH interface

**Date:** 2026-10-10. **Epistemic status:** implemented finite classical constructions, rigorous finite counterexamples, bounded executable probes; **RH OPEN**. No completion/positivity theorem is claimed.

**Verified starting head:** build/2026-10-09/field-relative-actualization-a1 = 927bcfac3f932a998154726fffbdbc27a835e770 (43 original tests, eight original mutation controls verified in GitHub Actions on 3.10 and 3.13). Main at first inspection: 22b6dadbd1983159e6c5d8cc32fb9aeff6925ec6 (Round 069), not merged. The earlier operational research parent is 93015589a54a8edc4ad78da0f1eb85b12b979991. The newer current main may advance independently; preserve all other branches.

## 0. What the user proposed

The primary SUCC system advances one chosen unit step within a declared field or mathematical space. Shadow means **unrealized space data**, potentially with combinatorially weighted histories. Direct observation records a context/coordinate-specific event; model integration is a distinct causal propagation. The complete lawful history is retained by a lossless idealization, while a finite observer has a restricted, resource-bounded view. Bare inversion, shadow predecessor reconstruction and complete causal/conjugate reversal are *different* operations.

The new user hypothesis: local observer and external model might become observationally indistinguishable over exactly the range of local interaction; RH could require a global certificate of an indefinitely large truth, not an impossible attempt to visit all witnesses. The mathematical moonshot is a **finite construction mechanism for categorical phenomenology**, letting Yoneda-like representations connect apparently unrelated spaces by preserving accessible relationships.

This is **not** a claim that category theory already proves RH, that finite observational equivalence implies equality of global truth, or that a zero at unimaginable height would be physically detectable.

Our engineering interpretation is to build three typed objects: finite full/restricted Yoneda on mathematical contexts, explicit and measured information-loss/coend transport between representations, and a proof-carrying resource-bounded observation relation. Then couple them to the existing finite Engine without importing inaccessible future coefficients. Only that restricted interpretation is presently established.

## 1. Theorem Y1 — sharp first distinguishability of two arithmetic targets

Let C be the divisibility poset of positive integers: Hom_C(j,n) is a singleton if j divides n and empty otherwise. Let J_B be the full observer subcategory on test objects j=1,...,B. The restricted representable for a target n is Hom_C(-,n)|_(J_B).

For distinct positive integers a,b, put

    D(a,b) = min over primes p with v_p(a)!=v_p(b)
               p^(1 + min(v_p(a),v_p(b))).

Then:

    y_(J_B)(a) is naturally isomorphic to y_(J_B)(b)
          if and only if B < D(a,b).

**Proof.** If j divides a but not b (or vice versa), some prime-power factor p^e of j satisfies e between the distinct p-adic valuations. Then j>=p^e>=p^(1+min(v_p(a),v_p(b))). Conversely the prime power achieving D divides exactly one target, so its Hom test distinguishes them. In a thin category all nonempty Hom sets are singletons, so equal existence profiles have the unique natural isomorphism. QED.

The target can be a compact formal prime-valuation word, not a fully materialized huge integer. First probes: D(6,12)=4, D(6,30)=5. For the symbolic pair L_10000 and 2 L_10000 the first distinguishing test is 2^14=16384; both look the same under **all** divisor probes at B=10000. Likewise 2^2047 versus 2^2048 first separates at 2^2048. The proof is a finite exact deduction; it is NOT a claim that a physical observer could execute that many tests or that no other observer probe could distinguish the targets earlier.

Resource limits: real integer materialization adapter <=10^6, symbolic valuations at most 2048 distinct prime generators and exponents <=2048; declared observer budgets <=2048 bits, LCM horizon <=10000, no silent truncation. Budgeted query enumeration rejects work beyond its cap. A finite certificate labels equal, distinguished, and indistinguishable WITHIN B as distinct answers; it never promotes the latter to global equivalence or RH.

## 2. Theorem Y2 — a restricted Yoneda observer can infer a spurious arrow

Take C to be the thin divisibility category on {1,2,3,6}. Globally Hom_C(2,3) is EMPTY.

For the observer subcategory J={1}:
  Hom_C(1,2) and Hom_C(1,3) are both singleton.
Therefore there is ONE natural transformation between the restricted
representables y_J(2) and y_J(3), despite there being no morphism 2->3 in C.

The full Yoneda embedding has Nat(y(2),y(3))=Hom_C(2,3)=empty. We checked the ordinary Yoneda bijection explicitly on finite path categories containing parallel arrows; the software enumerates all natural-transformation component functions and checks all naturality squares, not just Hom cardinalities.

**Consequences:** restricted observational equivalence is necessarily indexed by a declared probe category. No arbitrary map between "air-gapped" global mathematical fields can be inferred from a coincidence at one context. A meaningful bridge has to be independently constructed and functorial.

Primary math reference: Tom Leinster, Basic Category Theory, §4.3, full and faithful Yoneda, https://arxiv.org/abs/1612.09375 .

## 3. Theorem Y3 — keeping histories changes the observer category

At additive wavefront N=3 the source has integrated the multiplicative factors 2 and 3. Build the free finite category of directed multiplication paths by encountered generators, allowing shadow TARGET objects and keeping every ordered word.

There are TWO distinct 1->6 paths: (2,3),(3,2), and THREE 1->12 paths: (2,2,3),(2,3,2),(3,2,2).

Restricted extensional divisibility Yoneda at contexts {1,2,3} cannot distinguish 6 and 12. The path-category representables already can: at context 1 their Hom-sets have distinct cardinalities 2 and 3. The Dirichlet-convolution-log shadow projection assigns -1 and +1 respectively, but the underlying *sets of paths* are retained even when signed weights cancel.

The canonical functor F:Path_C -> Div_C (send any path to its unique endpoint arrow) preserves identity and composition but is NOT faithful. In particular two distinct arrows 1->6 have one image. This is an exact categorification of the user's "history coherent, observed scalar lossy" requirement. It is also a warning: Yoneda applied **after** F cannot recover path distinctions which F deliberately erased.

These are free category/unique factorization calculations, not a new RH theorem. Calling a path "structurally online" does not claim the integer endpoint or its source coefficient has been directly encountered.

## 4. Theorem Y4 — finite genuinely checked categorical bridge and coend

The multiplicative order a|b is equivalent by unique factorization to coordinatewise inequalities in the prime-valuation vectors v_p(a)<=v_p(b). The functor a -> (v_p(a)) between the finite divisibility poset and its finite image inside formal logarithmic prime coordinates is full and faithful. Morphism grades compose by addition of v_p(b)-v_p(a), a formal version of sum_p k_p log p. A corrupted prime grade fails the exact source contract.

**This is only a formal log-coordinate category.** It is not the actual real place, a Gamma factor, a p-adic-to-R field equivalence, or an arithmetic Hodge polarization.

Given any checked functor F:C->D, build its source-derived companion profunctor B(c,d)=Hom_D(Fc,d). We verify source contravariance, target covariance and interchange; and construct the finite co-Yoneda quotient

    integral^c Hom_C(a,c) x B(c,d)  ~= B(a,d)

by identifying witness pairs (k∘f,h) with (f,h∘F(k)).
For the two-prime path category and its forgetful transport, the explicit computation has FIVE raw composable witness pairs but ONE quotient class, mapping to exactly the ONE thin target arrow 1->6. That is a measurable four-distinction loss; it is not a new primitive scalar event at 6.

A declared bridge with bad arrow composition fails the functor test; one with invalid source/target actions fails the naturality audit; dropping coend relations fails the quotient test. A legitimate functor automatically has a coherent companion. Hence success at these tests is **construction-stage mathematics**, not evidence that Weil positivity is true.

## 5. Theorem Y5 — causal internal/external model agreement is observational, not ontological

The new local_global adapter takes a finite local Engine and a more complete global Engine, but extracts only integrated events with n<=B from either journal. It STOPS before reading the next global source coefficient. From these prefixes it recomputes the source-connected and unrealized shadow indices. No future-data mutation is passed into the local comparison.

At B=3, genuine zeta and a global source mutated only at n=6 agree on all declared coefficient observations and on their 6/12 shadow histories. At B=6 the first mismatch is n=6, while the ordered-factor shadow of 6 itself can remain identical. One may have different internal *predictions* despite identical observations; the API explicitly refuses to claim model identity. Context labels can be measured strictly or dropped by declared choice.

The effective inference is:
  same reachable observations under the declared protocol
      -> same *finite observation signature*, not
         same theory, same inaccessible truths or RH.

A source provider with a fake coefficient at 6 is disallowed by the actual multiplicative Euler-source gate. Global physical impossibility and logical independence are NOT derived. The local/global comparator is an instrument for measuring probe-relative agreement, not a refutation of proof by finite symbolic deduction.

## 6. Hostile controls and correction ledger

- Early CI FAILED because the thin morphism record accidentally exposed the ratio b/a. This leaked the very global target label the local observer supposedly lacked. FIXED: a thin hom reports only singleton existence, never target ratio. Path morphisms still return their declared words.
- The new local/global lane initially expected DomainError instead of the correct BudgetExceeded for an invalid shadow target. This was a **test harness expectation error**; corrected.
- Deliberately broken path-forgetting, source-audit erasure, too-weak separation boundary, loss of factor knowledge, future-source leakage, missing coend-identifications and the original eight event/history failures are checked by isolated mutation subprocesses. These errors are not hidden or elevated into mathematics.
- Genuine ζ and primitive χ modulo 5 retain Euler connected-source consistency; positive character mixtures or the Davenport–Heilbronn coefficients can violate scalar multiplicativity. The categorical objects themselves remain valid for fake arithmetic, so the source gate is **independent and indispensable**.
- Wrong p=2 logarithmic clock and nonunit unramified α_2 are separately rejected by the earlier exact clock/character auditors. The new formal valuation functor alone is incapable of detecting a fake scalar prime impulse unless source grading is added.
- A finite negative Suzuki/Weil witness would be mathematically finite, but can be practically inaccessible; absence of a witness below a resource bound proves no RH theorem. No zeros or scattering phases are construction inputs.

Provenance: previous actualization build branch head 927bcfac3f932a998154726fffbdbc27a835e770, previous research observations 93015589a54a8edc4ad78da0f1eb85b12b979991, main Round 069 22b6dadbd1983159e6c5d8cc32fb9aeff6925ec6. No fresh independent AI agents; six isolated Python subprocess test lanes are an execution fan-out, not independent mathematical evidence.

## 7. Fourth gate and falsifiable next experiment

The exact RH-facing target is the full Weil form, including true Λ(p^k), half-density p^(-k/2), physical log p, character/conductor phases, **negative Gamma and pole terms**, and the required sign for every supported test. Suzuki's 2023 theorem states RH iff his completed Ψ(t)>=0 for all real t (https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785, Theorem 1.7).

A finite category must be enriched to represent *arithmetic source coefficients and analytic form topology*, not merely invertible labels. The missing theorem would require a source-derived profunctor or functor from the actualization/history-and-probe category into a specified Archimedean Schwartz/Mellin/Weil-form **core**, subject to:

1. Natural in both observation/transport directions; preserve the contextual history and avoid silently forcing state purity or scalar multiplicativity.
2. Primitive source coefficients exactly match the connected Euler logarithm: fake n=6, |α_2|!=1, shifted log2, forbidden log(3/2) and genuine Davenport–Heilbronn negative control must not pass unnoticed.
3. An exact identity, on a declared form domain and with controlled horizons, with the **completed** Q_L=P_L-K_L, not only the positive primewise Gram or formal-valuation degree.
4. An **independent**, non-circular Hodge-index/coercivity/energy inequality for that matching form, or an explicit obstruction that rules out this bridge.

**First decisive probe:** a 2–3–infinity typed Hecke/Schwartz bridge whose coend tracks the two distinct 1->6 histories but whose connected scalar trace at log6 remains zero. Check its action on an actual smooth compactly supported test function and its Gamma/pole normalization. If it produces a positive generic norm while passing fake sources, it is RH-inert; if it creates a scalar 6 or ratio impulse, refute it. If exact trace and source fidelity survive, only then investigate an independent sign.

## Claim ledger

| ID | Claim | Status |
| --- | --- | --- |
| CY-1 | sharp resource-bounded divisibility separation | DEMONSTRATED |
| CY-2 | restricted Yoneda spurious morphisms | DEMONSTRATED (classical) |
| CY-3 | paths enable earlier shadow discrimination; forgetful functor nonfaithful | DEMONSTRATED |
| CY-4 | formal-log valuation equivalence and checked companion/coend | DEMONSTRATED (classical) |
| CY-5 | causal prefix equivalence, mutation detection at event 6 | DEMONSTRATED in finite engine |
| CY-6 | continuous analytic/Psi-Weil form-core transport | UNVERIFIED / not built |
| CY-7 | full completed Weil sign and RH | OPEN |

New code files: actualization/yoneda.py, resource_probe.py, phenomenology.py, local_global.py; CLI commands yoneda-demo, local-global-demo, probe-budget; tests/actualization/test_category.py, test_resource_probe.py, test_local_global.py; documentation actualization/YONEDA_GUIDE.md. Existing CI script and isolated mutation harness extended. Read the GitHub workflow artifacts for exact environment-specific counts/output; no claim is made that the historical full repository test suite has run.


## 8. Theorem Y6 — a real circle-character bridge with reversed arrows

This is separate from the formal-log valuation category in Y4. Take the
additive finite state clock G_m=Z/mZ and its character group Hom(G_m,R/Z).
A character j is given exactly by k |-> (jk/m) mod Z, and its value at the
cyclic generator 1 is the m-torsion angle j/m of the REAL circle R/Z.

For m|n, define

    pi_(n,m): G_n -> G_m,       k |-> k mod m,
    iota_(m,n): G_m^ -> G_n^,   j |-> (n/m)j mod n.

Both are group homomorphisms and honest one-object group-category functors.
Their directions reverse (surjective state reduction versus injective dual
character transport). The evaluation square commutes:

    <pi_(n,m)(k),j>_m = <k,iota_(m,n)(j)>_n in R/Z.

**Proof:** The two rational phases differ by an integer because
(j*(k mod m))/m - (n/m*j*k)/n = -j*floor(k/m).
No complex exponential or floating approximation is needed. For m|n|r,
state projections and dual inclusions both satisfy the appropriate tower
composition laws. This is a completely explicit finite–continuous
(Pontryagin) coupling, though ONLY to circle torsion.

At the real case m=2,n=6, old dual characters {0,3} embed in the n-clock,
while indices {1,5} have exact order 6 and {2,4} order 3. New dual modes
4 = L_3 - L_2. The rank is exactly the early conductor innovation, not
an invented extra Euler primitive at integer 6.

Hostile correction: mapping the dual character j to the numerically same
index j (rather than (n/m)j) FAILS the evaluation square even at k=j=1.
A code mutation replacing the inclusion multiplier is required to be
caught by the test suite. A finite cycle can map into R/Z while the
full continuous real analytic structure, Gaussian/Gamma local factor and
non-torsion states remain OUTSIDE this model.

In the directed limit, the familiar duality (Z-hat)^vee = Q/Z accounts
for all finite-order circle characters. This is classical harmonic
analysis, not an independent RH proof. See Jordan Bell,
https://jordanbell.info/LaTeX/mathematics/Qdual/Qdual.pdf .

**New next gate:** Can we lift the exact finite torsion duality, alongside
Hecke source coefficients and shadow path data, to the actual
Archimedean Schwartz/Mellin test core in a way that preserves the complete
Weil distribution and logarithmic form norm? In particular, a false
scalar impulse at n=6 must remain excluded even though an exact-conductor-6
character is perfectly legitimate. An exact lift must keep these distinct.
The remaining independent Hodge/Weil SIGN is unchanged and unproved.

**Y6 status:** DEMONSTRATED classical finite duality; zero-free,
rational-exact regressions/mutation tests. The proposed Schwartz/Gamma
and Weil-polarization lift is UNVERIFIED.
