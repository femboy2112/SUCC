# SWM-X06 — Reusable reversible memory has a fiber law, not an additive debt law

## 1. Original question

Join A08's resource geometry, B16's autonomous source-state bounds, C24's
reversible-memory theorem, and F45's service/debt threshold. What exactly can
be charged when a deterministic observation destroys current-state information?
Does stage-by-stage erasure force additive storage, and can that storage be
substituted into the proposed debt recurrence?

## 2. Context, provenance, and priority

This independent second-generation assignment starts at
`71eaf11e48ca3ccb349858bba64abf36b59ee6f5`. The four dossiers and their relevant
implementations were read without modification. C24's pigeonhole principle,
finite-map composition, and A08's path-concatenation argument are the only
mathematical ingredients. The theorem below is proved directly; classical
priority is not investigated and academic novelty is **UNVERIFIED**. C24's
thermodynamic model is deliberately not imported into this cardinal theorem.

## 3. Common ambient objects, actual maps, and invariant

Let X,Y,Z be nonempty finite sets, f:X→Y and g:Y→Z total deterministic maps.
A memory lift of e:X→E is an injective map x↦(e(x),m(x)) into E×M. Define

    ρ(e) = max over u in e(X) of |e⁻¹(u)|,
    b(e) = ceil(log₂ ρ(e)).

The original carrier X stays fixed. Memory denotes the extra finite label M,
not the current carrier, retained observation records, an external controller,
a language recognizer, expected entropy, runtime, or heat.

For reports r:X→O and s:Y→P that are actually retained, the two endpoint maps are

    J₁(x) = (f(x), r(x)),
    J₂(x) = (g(f(x)), r(x), s(f(x))).

The second endpoint is a deterministic function of the first: it keeps the
old record and appends the new report. A longer lawful fixed program gives
maps e_n:X→E_n with e_(n+1)=h_n e_n. E_n includes every retained record; stage
control is specified separately. The invariant is each endpoint's partition
of the SAME original set, together with its exact fiber cardinalities.

## 4. Candidate theorem and exact scope

**PROVED LOCAL (paper, classical ingredients).**

1. The smallest memory alphabet for an injective lift of e has size ρ(e).
   Thus K memory labels suffice iff every endpoint fiber has at most K originals.
2. For composable f,g,

       ρ(f) ≤ ρ(gf) ≤ ρ(f)ρ(g),
       b(gf) ≤ b(f)+b(g).

   If f is surjective, also ρ(g)≤ρ(gf). The upper bounds are sharp; both
   product and bit-sum can be strict even when both maps are surjective.
3. With retained reports, define c(y,o)=|{x:f(x)=y and r(x)=o}|. Then

       ρ(J₂) = max_(z,o,p) Σ_(y:g(y)=z, s(y)=p) c(y,o),
       ρ(J₁) ≤ ρ(J₂) ≤ ρ(J₁)ρ((g,s)).

   Retaining the extra reports cannot increase the rank relative to gf alone.
4. For every finite deterministic chain e₀,...,e_N on the same X, the minimum
   capacity of ONE reusable memory alphabet that makes each stage injectively
   encoded is exactly ρ(e_N). There are encodings with a common fixed memory
   label m(x), and each stage induces a bijection **between its two reachable
   encoded images**, each of size |X|. The required capacity does not generally
   equal the product of separately reserved local memory alphabets.
5. Always |X|≤|e(X)|ρ(e). With C permitted reachable endpoint labels, the best
   possible rank over arbitrary maps is ceil(|X|/C) when 1≤C≤|X|; balanced
   fibers attain it. A specified map can need more than that average bound.

These are existence statements for injective encodings. They do not assert a
permutation of full product registers of unequal cardinalities. A global
reversible circuit requires explicit matched registers, initialization,
ancillas, allowed gates, and controller; its physical implementation is not
supplied here. Record storage and stage control are not included for free in M.

The existence of m:X→M presupposes original access during initialization, or
an initially injective preparation. If the observer begins only with an
already noninjective e₀:X→E₀, every available initialization m=k e₀ has the
same erased fibers as e₀: the pair (e₀,m) is injective iff e₀ is. A buffer
cannot recover an original distinction already erased before the encoding
contract begins. The arbitrary-e₀ theorem asserts existence of labeled
encodings, not that an observer seeing only E₀ can construct them.

## 5. Complete derivation and composition coherence

For (1), two originals with the same endpoint must receive different memory
labels. This forces at least the largest fiber size. Number the members of
each fiber from zero, reusing the same labels across different fibers; the
result is injective and uses exactly ρ(e) labels.

For (2), the fiber (gf)⁻¹(z) is the disjoint union of f⁻¹(y) over g(y)=z.
There are at most ρ(g) such y and each contributes at most ρ(f) originals.
Every f-fiber is contained in a composite fiber, proving the lower bound.
If f is onto, each y in a largest g-fiber contributes at least one original,
proving the additional lower bound. Taking logarithms and rounding up gives
b(gf)≤b(f)+b(g), since ρ(f)≤2^b(f) and ρ(g)≤2^b(g). Uniform fiber sizes
attain the product bound, including repeated two-to-one resets on independent
coordinates. Associativity is literal composition of finite functions, and
identities have rank one and bit cost zero.

For (3), fix the complete retained endpoint (z,o,p). Its originals partition
according to y=f(x), giving exactly the displayed weighted sum. Each summand
is at most ρ(J₁), and at most ρ((g,s)) intermediate y occur. Every J₁-fiber
lies in a J₂-fiber because the later endpoint is a function of the earlier
one. Conversely, a J₂-fiber lies in the corresponding gf-fiber after reports
are forgotten, proving the other comparison. Ignoring zero-weight unreachable
y is essential: they are not original uncertainty.

For (4), e_n(x)=e_n(x') implies e_N(x)=e_N(x') by deterministic composition.
Color each final fiber injectively with labels 0,...,ρ(e_N)−1 and use that
same coloring m at all stages. If (e_n(x),m(x))=(e_n(x'),m(x')), the originals
are in the same final fiber and have the same color, so x=x'. Thus every
stage encoding is injective. The correspondence indexed by x from one image
to the next is a well-defined bijection; it is not claimed to be onto either
full ambient product. The endpoint lower bound proves optimality.

If e₀ is the identity and the auxiliary register starts blank, the first
encoded transition can produce the chosen m(x); later stages retain it.
This is an injective partial map on its reachable domain, not a claim about
unspecified physical gates. The construction may depend on the complete
known finite program. Uniform online implementations with unknown future
programs are a separate problem.

For (5), sum the endpoint fiber sizes. Each is at most ρ(e), so their total
|X| is at most |e(X)|ρ(e). Distribute originals among C labels with sizes
floor(|X|/C) or ceil(|X|/C) for attainment. Fibers (3,1) show that four
originals and two endpoints can require three labels even though the coarse
average lower bound is only two.

## 6. Crucible, minimal countermodels, and independent receipts

The new probe enumerates **430 complete finite maps** with original sizes
one through five and declared target sizes one through three. Its independent
oracle exhausts all assignments of candidate memory labels, in increasing
capacity; it does not count fibers to obtain the answer. Every minimum agrees
with C24's implementation and every returned lift is injective.

For **38,084 composable map pairs** with original/intermediate sizes one
through four and final size one through three, the probe checks the product
bound, integer-bit bound, common-buffer injectivity, and reachable-image stage
bijections. Among the 1,840 pairs surjective at both stages, 266 have a strict
product bound and 116 have a strict bit-sum bound.

| False additive claim | Complete countermodel and result |
|---|---|
| Local optimal alphabet sizes must multiply | f=(0,0,1), g=(0,0): ranks 2,2,3. Three labels suffice, not four. |
| Local optimal bit requirements must add | f=(0,0,0,1), g=(0,0): bit requirements 2,1,2. Two final bits suffice, not three. |
| Two one-bit stage buffers must remain separate | f=(0,0,1,2), g=(0,1,1): ranks 2,2,2. The same binary label separates both stages. |
| Composite rank always dominates the full next-map rank | f=(0) into three states, g=(0,0,0): composite rank 1, next-map rank 3; f is not onto. |
| Reporting and discarding a reset bit are the same resource contract | Reset two originals with retained original-bit report has residual rank 1; discarding that record requires rank 2. |

The first two countermodels have the smallest possible number of originals
among surjective composable maps. For at most two originals, a noninjective
surjection is a reset to one point; its other composable surjection is
injective, so the product is exact. For three originals, the only chain with
two noninjective surjections is 3→2→1, with ranks 2,2,3 and bits 1,1,2, so
there is no strict bit-sum inequality. The exhaustive bounded check agrees.

A separate enumeration covers **20,340 binary-report two-stage models**,
independently recounting each final fiber by summing its intermediate weights.
A reset followed by a purported spontaneous reappearance of the erased bit
is rejected: its later endpoint is not a function of the former endpoint.
Eight regression tests retain these positive and adversarial controls, including
the impossibility of recovering an already erased preparation from its current
state alone.

## 7. Verdict and audit of the imported claims

C24's finite sharp memory theorem **SURVIVES** independent proof and exhaustive
assignment tests. It concerns injective lifts; it does not by itself supply a
global permutation/circuit of arbitrary physical product registers.

F45's recurrence theorem also **SURVIVES**: an independent closed form agrees
on 3,328 exact rational values across 256 positive parameter tuples. The audit
has 194 explicit finite crossing certificates and 62 noncompletion coefficient
certificates. The boundary D₀=2,a=1,b=1,r=1/2 remains positive at every finite
stage by its exact formula 2^(1−n). `debt_stages` algebraically continues after
a crossing; those later values are not further executed debt-service stages.

**REFUTED:** local reversible bit costs must add, source-generator size equals
reversible buffer debt, and these invariants alone impose F45's recurrence.
The replacement is the exact fiber law above. No thermodynamic conclusion,
physical cost estimate, general proof-search bound, or Lean-kernel status is
claimed for this bridge.

## 8. Remaining obstruction and next falsification opportunity

A feedback policy can choose actions using history, but a fixed deterministic
policy still induces deterministic maps on (current, history, controller).
The theorem applies after those state variables are declared. It does not
optimize restricted-gate reversible circuits, memory-access time, unknown-future
online algorithms, external-record deletion, stochastic realizations, or
reservoir heat. The next useful falsification probe is a finite gate set with
limited access to old records: compare reachable injective lifts with the
unrestricted fiber bound and produce a strict implementation overhead.

## 9. Cross-domain consequence and dominance boundary

The cost c(f)=log₂ρ(f) is subadditive under composable maps and zero on the
identity. It is not additive. In any specified category of permitted finite
maps, d(X,Y)=inf{c(f):f:X→Y permitted}, with infinity for no arrow, satisfies
the directed triangle inequality: compose near-optimal arrows and apply the
product bound. This is A08's resource-geometry bridge. Charge explicit edge
costs additively along a path only if they describe genuinely separately
consumed resources; the optimal reusable buffer is a different functional.
No symmetric metric or raw pairwise distinguishability triangle follows.

B16's source-state count is independent of this residual buffer rank. A
stationary source emitting 0^(L−1)1 needs at least L states, even for ONE
prepared original trajectory; that one original needs one buffer label at
all times. Conversely, resetting N possible originals while reporting only
zeros needs N buffer labels, while its constant output word has a one-state
stationary generator. These controls were checked for N,L from one through
eight. Time-dependent one-state reporting shifts the word into an external
clock/controller and does not evade B16's stationarity premise.

Finally, one reset followed by identities has cumulative ranks 1,2,2,2,...,
so unobserved original information does not gradually disappear as service
passes. To apply F45, one must define the debt variable from an actual resource
and prove its growth/service recurrence for every permitted strategy. None of
the surviving cardinal or source-memory theorems supplies that missing premise.

## 10. Deliverables and actual validation

- `scripts/swarm_x06_probe.py`: independent auditors, exact weighted-fiber and
  common-buffer constructions, and source-memory/debt separation controls.
- `tests/test_swarm_x06_memory.py`: eight hypothesis-sensitive regression tests.
- `X06_RECEIPT.json`: exact deterministic probe output.
- `X06_REVIEW.md`: independent adjudication and scope limitations.

Executed successfully:

```sh
python scripts/swarm_x06_probe.py > research/2026-10-13/SWARM_ATLAS/X06_RECEIPT.json
python -m unittest discover -s tests -p 'test_swarm_x06_memory.py' -v
```

The full integrated repository gate is the root agent's responsibility. No
historical file, archived theorem, shared index, or cohort implementation was
changed. This assignment is a paper theorem plus exact bounded audits, with
no formal kernel proof or unbounded computation claimed.
