# SUCC × Ω × Scott: source-indexed causal weld at an infinite observational boundary

**Local mathematical research note. No GitHub changes.** Prepared from the conversation's SUCC/C-monoid/omega program; independent classical sources are distinguished from the proposed architecture. **Verdict: one explicit nontrivial weld theorem proved; generic omega–SUCC compiler unconstructed.**

## 0. Corrected reconstruction

The SUCC carrier supplies source-indexed data and lawful successor steps. Lambda-calculus and omega reductions supply computational path syntax. A C-monoid, if faithfully realized, internalizes composition/pairing/application/abstraction and gives typed observational components by idempotent splitting. Scott domain semantics permits partial outputs ordered by information; directed suprema encode completed computations without finite termination. A quotient/observation map specifies what information is preserved by an *equivalence*. The claimed welding theorem is about equality **in that observation domain** (and preservation of specified causal data), not about homeomorphism of the line and circle.

The raw generalized terms Ω_k = ω_k ω_k (ω_k=λx.x^k, k left-associated occurrences) expand under leftmost beta reduction by k−2 additional ω_k occurrences. For k≥3 they have infinite strongly convergent reductions in an appropriate infinitary lambda calculus; ordinary finite β-normal forms do not exist. In conventional Scott D∞ semantics all such head-unsolvable terms denote bottom, and that observational equivalence is too coarse for preserving path histories. Alessandro Berarducci's *Infinite lambda-calculus and non-sensible models* constructs finer infinitary β⊥ normal-form semantics and explicitly treats Ω3. The trace-sensitive omega-indexed semantic compiler remains **PROPOSED**, not established by these classical theorems.

## 1. Exact dcpo theorem: two distinct nonterminating paths, one circle result

Let T=R/Z, q:[0,1]→T the quotient map, and let K(X) be the set of nonempty compact subsets of a compact Hausdorff space X. Equip K(X) with the reverse-inclusion information order:

    K ⊑ L  iff  K ⊇ L.

A directed family of nonempty compact subsets has a nonempty intersection (compactness plus the filtered-intersection property), hence K(X) is a dcpo with

    ⨆_i K_i = ⋂_i K_i.

The observation/quotient map

    q_*: K([0,1]) → K(T),  K ↦ q(K)

is Scott-continuous. It is monotone, and for any directed filtered family K_i,

    q(⋂_i K_i) = ⋂_i q(K_i).

The nontrivial inclusion (right to left) follows as follows: for y belonging to every q(K_i), each nonempty compact set K_i∩q^{-1}({y}) belongs to a filtered family. By compactness its intersection is nonempty, producing a common preimage. This proves preservation of directed suprema. No arbitrary unlicensed interchange of q and intersection is assumed.

For each n≥1 let e_n=16^{-n}, and define rational interval information states

    A_n=[1-e_n,1]  (prefix FFF...F in base 16)
    B_n=[0,e_n]    (prefix 000...0 in base 16).

Each chain is increasing in the reverse-inclusion information order. At *every* finite n,m, A_n and B_m are disjoint real intervals, and their circle images q(A_n),q(B_m) are unequal compact arcs on opposite sides of the seam. Their exact Hausdorff distance for the standard circular geodesic metric is

    d_H(q(A_n),q(B_m)) = max(e_n,e_m) > 0.

But the limits are

    ⨆ A_n = {1},   ⨆ B_m = {0}.

Thus Scott continuity gives

    q_*(⨆ A_n) = q_*({1}) = {[0]} = q_*({0}) = q_*(⨆ B_m).

The *joint* computation is indexed by the directed product N×N and satisfies

    ⨆_(n,m) (q(A_n), q(B_m)) = ({[0]}, {[0]}).

The joint limit lands on the equality diagonal of K(T)×K(T), while every finite pair lies outside it. No finite simultaneous termination or equality is necessary. Both chains retain their distinct data histories; only their explicitly declared circle observation is equal.

A simpler rational point version uses a_n = 1−16^{-n}, b_n=0: they are unequal modulo one for all n, but their circle distance is exactly 16^{-n} and q(lim a_n)=q(lim b_n).

**This is a proved example of the precise phenomenon proposed in the conversation.** Its construction involves rational arithmetic, SUCC steps, a quotient observation, and Scott-continuous passage to the limit. The particular omega/C-monoid implementation is still a separate task.

## 2. Explicit preservation of the surviving causal defect

The two limiting lifts differ as real numbers by the integer 1. Under q they agree; as lifted paths they are distinct. Retain a separate deck/winding channel, e.g. winding difference w=1. Therefore

- phase-only observation: A_∞ ∼ B_∞ (proved);
- phase + chosen lift/winding observation: A_∞ not equivalent to B_∞ (proved).

This is not a failure of the weld. It demonstrates **relative equivalence based on precisely the information selected to survive**. Quotient observation is not an equivalence of the full line and circle as spaces. It is a lossful but exact map with a classified integer kernel.

## 3. Abstract causal weld theorem (in a declared observation domain)

Let D,E be dcpos, W:D→E Scott-continuous, and a_n,b_m increasing chains in D. Suppose their directed suprema exist. Then

    W(⨆ a_n) = ⨆ W(a_n),  W(⨆ b_m) = ⨆ W(b_m).

If the two observed directed suprema agree, the computations have equal completed observations, even if W(a_n)≠W(b_m) for every finite pair (n,m). Importantly, Scott continuity does NOT itself make the two suprema equal. Equality is a mathematical obligation, constructively supplied in §1 by the line/circle quotient. For an algebraic E, equality is also equivalent to agreement on all finite compact observations; this offers a more computationally checkable certificate.

**Categorical formulation.** A finite causal graph G generates a path category P(G). An instrumented interpretation into partial-information objects can be extended to directed completion/ideal completion, and a Scott-continuous observation functor can identify completed path values. To claim a full functorial or higher-categorical equivalence, separately verify identities, β-soundness, source labels, operation naturality, and composition of the proposed equality witnesses. Some quotient observations may erase these; the retained information must be declared rather than assumed.

## 4. Two productive semantic layers, not an invalid ordinary beta-normalization claim

- **Operational omega layer:** generalized Ω_k (k≥3) has continuing beta reductions. Instrumented finite reduction prefixes encode computation stages. Use coinductive/infinitary normal forms or guarded fixed-point streams if full infinite program objects are required. Do not claim all Ω_k have ordinary finite beta-normal forms; they do not.
- **Partial-information layer:** representations of the finite outputs form a directed chain in an interval/compact-set domain. Scott-continuous observations map these to common completed meanings.

Conventional D∞ sends unsolvable raw generalized omega terms to ⊥. Equality of all raw Ω_k at bottom, by itself, does **not** certify a nontrivial weld. Berarducci-style finer infinitary semantics retains distinctions among some unsolvables, and can be paired with a separate coarser observational quotient that forgets only the distinctions intentionally declared irrelevant.

## 5. Source-faithful SUCC next step

Replace the toy digit streams by two source-labelled computational paths built from SUCC's exact four-pole BBP recurrence and its Green-tail lift. Require a **source-attested naturality square** relating computation prefix, exact rational evaluation, quotient to circle, and Scott-continuous completion. Track the carry/winding cocycle as a separate typed channel. Check beta-reduction/trace sensitivity in the Ω_k encoding, including hostile wrong-seed and non-Haar periodic controls.

A concrete mathematical goal is to prove that the chosen path category's observational completion *preserves a given family of Fourier and source/carry probes*. This would give a genuine nontrivial finite-to-analytic interpretation theorem, not just the coarse bottom equality of divergent lambda terms. No statement about π normality follows without a source-dependent estimate; that is a subsequent, separate target.

## 6. Proof/claim ledger

| Claim | Status | Reason |
|---|---|---|
| Scott-continuous quotient map K([0,1])→K(S¹) | DISCLOSED | Direct compactness proof (§1) |
| Two finite-disjoint chains with equal observed suprema | DISCLOSED | Exact dyadic/hexadecimal intervals (§1) |
| Explicit shrinking finite Hausdorff defect | DISCLOSED | Opposite arcs, max(16^-n,16^-m) (§1) |
| Surviving integer winding distinguishes lifts | DISCLOSED | q(1)=q(0), 1−0=1 (§2) |
| Omega-indexed faithful C-monoid compiler for SUCC | UNVERIFIED | Need implementation and soundness proof |
| Full higher-coherence/naturality for source BBP | UNVERIFIED | Need source-attested construction |
| π source-selected cancellation or normality | OPEN | Not implied by topological glue |

## Sources

- Keye Martin, *Domain Theory and Measurement*, University/Oxford-hosted lecture notes: https://www.cs.ox.ac.uk/people/bob.coecke/domains.pdf (Scott continuity, interval domains).
- Jean Goubault-Larrecq, *First-countable spaces and their Smyth powerdomain*: https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=3930 (nonempty compact sets, reverse inclusion, directed filtered intersections).
- Alessandro Berarducci, *Infinite λ-calculus and non-sensible models*: https://people.dm.unipi.it/berardu/Art/1996Nonsensible/non-sensible.pdf (different infinitary semantics, explicit Ω3 expansion, not all unsolvables identified).
- Stanford Encyclopedia of Philosophy, *The Lambda Calculus*: https://plato.stanford.edu/entries/lambda-calculus/ (standard Scott denotational interpretation and its constraints).

## Local validation

Run `python /mnt/data/succ_scott_omega_weld_probe.py`; all exact rational finite-stage checks pass. The limit theorem is proved using nested compact sets, independently of these finite tests. No repository mutation.