# Front D — Scott causal weld: cofinal schedules and the completion discipline

**Audit correction (Cayley follow-up, 2026-11-09):** D-2 and D-3 below are corrected. Arbitrary finite prefixes cannot certify cofinality. See [semantic repair and counterexamples](../cayley_source_observer/SEMANTIC_AUDIT.md). The original statements remain in parent commit `afabc458323ef2e3a20ce2bae77239c4190819c5`.

**Status:** PROVED (cofinality + continuity transport), with the mandatory
distinction that Scott continuity does **not** manufacture equality.

## The centerpiece distinction (CW-15, restated as a theorem)

**Theorem D-1 (Scott continuity transports, does not equate).**  A Scott-continuous
map `q_*` between dcpos sends directed suprema to directed suprema:

    q_*(⊔_i x_i) = ⊔_i q_*(x_i)    (when the left sup exists).

It does **not** assert that `⊔_i q_*(x_i) = ⊔_j q_*(y_j)` for two *different* chains
`{x_i}`, `{y_j}`.  That equality requires a separate certificate.  Receipt (hostile):
take `q = id` and two distinct constant chains `x_i = 0`, `y_j = 1`; continuity is
trivially satisfied yet the two suprema are unequal.  This is exactly the CW-15
refutation made explicit.

## The weld needs the BBP identity, not just continuity

For the opposite arcs `A_n = [1 - 16^{-n}, 1]`, `B_n = [0, 16^{-n}]`, the completed
circle images coincide (`q({1}) = q({0})`) **because** `1 ≡ 0 (mod 1)`.  The Scott
continuity of `q_*` transports each limit to its own image; the *equality* of the
two images is supplied by the quotient `R → R/Z`, which is the same certificate as
the integer-deck/winding channel being quotiented out.  A winding-sensitive observer
retains `A` and `B` as distinct (deck displacement 1).

## Theorem D-2 (cofinal schedules, PROVED)

In the product-directed poset `N × N` (pointwise order), a **coordinatewise
nondecreasing** double-clock schedule `(n_k,L_k)` is cofinal iff both coordinates
are unbounded. Given two thresholds, take the later of indices reaching each;
monotonicity gives joint domination. An arbitrary subset needs the actual
quantifier `forall N,L exists k: n_k>=N and L_k>=L`.

Separate unbounded projections alone do not suffice: the alternating sequence
`s(2k)=(k,0)`, `s(2k+1)=(0,k)` never dominates `(1,1)`.

- **Canonical schedule** (seam): `(k, k)` — cofinal, witnesses the weld.
- **Hostile schedule** (diagonal): `(k, 2)` with `L_k ≡ 2` — **not** cofinal;
  the source horizon is frozen, so the completed-source limit is never approached
  and the weld's completed equivalence is not witnessed.

The repaired `scott_cofinal_schedule.py` certifies the explicitly declared affine
family `(a+bk,c+dk)`, with nonnegative integer parameters: cofinal iff `b,d>0`.
It provides an exact threshold witness. Arbitrary finite prefixes remain UNKNOWN.
For a BBP source cone, `L>=n` is an additional admissibility condition; growing
oscillator frequencies also require the paid clock coupling in CAY-05.

## Theorem D-3 (product completion, PROVED)

For dcpos `P,Q,R`, a map `f:P×Q→R` separately Scott-continuous in each variable
is jointly Scott-continuous for the product order. For directed `D⊆P×Q`, separate
supremum preservation gives `f(sup π_P D,sup π_Q D)=sup_(a,b) f(a,b)` over the
product of the projections. Each such pair is dominated by one member of D,
so this supremum equals `sup f(D)`. The converse follows by fixing a coordinate.
This proves the needed order-theoretic statement; it does not identify the Scott
topology on the product with the product of the Scott topologies.

## What this buys vs. what remains

- **Buys:** a precise, checkable criterion for which observation schedules are
  admissible witnesses of the weld, and the explicit statement that continuity
  alone cannot produce the completed equivalence.
- **Unpaid:** applying the weld to the *actual* BBP source (not the synthetic
  arcs) requires the source identity `U_n + T_n = 16^{n-1}π` as the equality
  certificate — which is the classical BBP identity, already authenticated in
  SUCC, not a new result of this front.  The completed *signed* equivalence and
  any normality consequence remain OPEN.
