# Front D — Scott causal weld: cofinal schedules and the completion discipline

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

In the product-directed poset `N × N` (pointwise order), a double-clock schedule
`(n_k, L_k)` is **cofinal** iff both `n_k → ∞` and `L_k → ∞`.  Equivalently, a
schedule can approximate the joint completed observation of the two independent
clocks exactly when neither coordinate is eventually bounded.

- **Canonical schedule** (seam): `(k, k)` — cofinal, witnesses the weld.
- **Hostile schedule** (diagonal): `(k, 2)` with `L_k ≡ 2` — **not** cofinal;
  the source horizon is frozen, so the completed-source limit is never approached
  and the weld's completed equivalence is not witnessed.

Verified in `observational_succ/scott_cofinal_schedule.py`; the characterisation is
the standard fact that a subset of a product of directed sets is cofinal iff each
projection is cofinal.

## Theorem D-3 (product completion, PROVED)

For two directed sets `D_1, D_2` of finite source information, the product `D_1 × D_2`
is directed, and a map `f : D_1 × D_2 → X` is Scott-continuous iff it is continuous
in each argument separately (for the standard product topology of the Scott
topologies).  The independent clocks therefore admit a well-defined joint completion,
and the cofinal schedules of D-2 are exactly those approaching it.

## What this buys vs. what remains

- **Buys:** a precise, checkable criterion for which observation schedules are
  admissible witnesses of the weld, and the explicit statement that continuity
  alone cannot produce the completed equivalence.
- **Unpaid:** applying the weld to the *actual* BBP source (not the synthetic
  arcs) requires the source identity `U_n + T_n = 16^{n-1}π` as the equality
  certificate — which is the classical BBP identity, already authenticated in
  SUCC, not a new result of this front.  The completed *signed* equivalence and
  any normality consequence remain OPEN.
