# Information-repair + online-control: an exact 3-way Pareto frontier

**Date:** 2026-10-18. **Module:** `observational_succ/repair_control_pareto.py`.
**Test:** `tests/test_repair_control_pareto.py` (11 cases, exact `Fraction`).
**Status:** VERIFIED-EXACT-MODEL for the finite construction; the lossless +
free + realizable corner is CLASSICAL. **No RH content** — finite, exact, no
zero ordinates, one real Archimedean role is irrelevant here. Every objective
record returned by the instrument carries `"RH_proved": False`.

## 1. Object and probe

A finite observer repairs its knowledge of a finite jointly-distributed source
`X = (X_1, ..., X_k)` (exact rational prior) by running probes. The instrument
holds three resources **separate**, per the SUCC physical-carrier / semantic
discipline:

| Axis | Symbol | Meaning | Direction |
|---|---|---|---|
| retained semantic information | `R` | what the controller learns about `X` | maximize |
| lawful acquisition cost | `C` | declared nonnegative rational cost per probe | minimize |
| physical carrier fidelity | `F` | how much of the forwarded datum survives | maximize |

A probe carries an exact rational observation channel `W` (a stochastic matrix
over `Fraction`). A **deterministic** (0/1) channel is a perfect or coarsening
probe; a **non-0/1** channel is IMPERFECT / noisy. A **destructive** probe
consumes its target datum, removing it from the forwarded carrier.

## 2. The measures (exactly rational, and why)

We use the **Gini impurity** `G(p) = 1 - sum_i p_i^2`, i.e. the order-2
(collision / quadratic Rényi / Tsallis-2) information. It is chosen *precisely*
so every certificate stays in `Fraction`: Shannon entropy needs a transcendental
`log`, which cannot be an exact rational certificate, whereas `G` is a finite
sum of squares of rationals. `G` is the classical CART "Gini index"; the
mutual-information surrogate is the classical CART "Gini gain".

- **Retained information** is the Gini mutual information
  `R(S) = G(P_X) - E_Y[ G(P_{X|Y}) ]`, which the instrument computes by the
  algebraically identical and division-light form
  `R(S) = sum_{x,y} P(x,y)^2 / P(y) - sum_x P(x)^2`.
  `R >= 0` by concavity of `G` and `E_Y[P_{X|Y}] = P_X` (Jensen) — this is the
  order-2 data-processing inequality. It is CLASSICAL. The test checks it on
  every schedule and reproduces `R` from explicit Bayes posteriors in an
  independent oracle.
- **Cost** `C(S) = sum_{p in S} cost(p)`, one declared charge per scheduled probe.
- **Carrier fidelity** `F(S) = sum_{d not destroyed} G(P_{X_d})`: each surviving
  datum forwards losslessly (full marginal Gini); a destroyed datum contributes 0.

`R` and `F` are deliberately distinct functionals: `R` is *semantic* (what the
controller estimates), `F` is *physical carrier* (what is forwarded downstream).
A destructive probe can raise `R` while zeroing `F` for its datum. We never
identify the two, and neither is a completed Weil form.

## 3. Future causal realizability

Each datum `X_d` has an integer arrival time. A policy is a set of
`ScheduledProbe(pid, schedule_time, conditions_on)`. `audit_realizability`
requires (1) `schedule_time >= arrival(target)` and (2) every conditioned
observation was produced by a probe scheduled *strictly earlier*. Static
schedules (`static_policy`) place each probe at its datum's arrival with no
conditioning and are always realizable; adaptive conditioning on the *past* is
accepted (test `test_lawful_adaptive_conditioning_accepted`).

## 4. The exact frontier (worked instance)

Binary correlated pair, `P(0,0)=P(1,1)=2/5`, `P(0,1)=P(1,0)=1/10`; both
marginals fair (`G=1/2`, so `F_max = 1`); `G(P_X) = 33/50`. Arrivals
`X_1 @ 1`, `X_2 @ 2`. Catalog: `N1`/`N2` perfect non-destructive on `X_1`/`X_2`
at cost `3/10`; `D1` perfect **destructive** on `X_1` at the cheaper cost
`1/10`; `P` an imperfect probe on `X_1` (`3/4`-reliable) at cost `1/10`. The
exact non-dominated vertices over all 16 subsets:

| `R` | `C` | `F` | schedule | reading |
|---|---|---|---|---|
| `0` | `0` | `1` | `()` | no probe — carrier intact, nothing learned |
| `17/200` | `1/10` | `1` | `P` | cheap imperfect info, carrier intact |
| `17/50` | `1/10` | `1/2` | `D1` | cheap full info, **carrier consumed** |
| `17/50` | `3/10` | `1` | `N2` (= `N1`) | full info, carrier intact, dearer |
| `1803/4550` | `2/5` | `1` | `N2,P` | both-datum partial, intact |
| `33/50` | `2/5` | `1/2` | `D1,N2` | full joint info, `X_1` consumed |
| `33/50` | `3/5` | `1` | `N1,N2` | full joint info, intact, dearest |

The destructive `D1` and non-destructive `N1` share `R=17/50` but neither
dominates (D1 wins cost, N1 wins fidelity) — both are boundary points. This is
the genuine SUCC 3-way trade: destruction buys cheap semantic information at
the price of carrier fidelity.

## 5. Recovering the classical corner

`classical_corner()` returns the **lossless + free + realizable** vertex
`(R, C, F) = (33/50, 0, 1)`: full information (`R = G(P_X)`, every posterior a
point mass), zero cost, carrier intact. This is the clairvoyant
rate-distortion / zero-cost feedback ideal and is labeled CLASSICAL. It is the
limiting vertex of a hypothetical *free, perfect, non-destructive* catalog, and
when attainable it dominates every other vertex (test
`test_classical_corner_is_limiting_and_dominant`).

The SUCC content is exactly the gap: in the actual **costly / destructive**
finite catalog the corner is **unreachable** — the instrument verifies that no
zero-cost schedule attains `R = 33/50` — so the realizable frontier of Section 4
is a nontrivial 3-way trade rather than a single dominant point.

**Classical vs SUCC separation.** Classical, imported wholesale: nonnegativity
and data-processing of Gini information; the lossless-free-realizable corner as
the rate-distortion/feedback-capacity optimum; Pareto non-dominance. SUCC
extension: the simultaneous, exactly-rational accounting of a *destructive*
acquisition against a *physical carrier* axis distinct from the semantic axis,
under a *future-causal* scheduling constraint, with the classical corner
recovered only as an unattainable limit of the costly catalog.

## 6. Falsifier (and its rejection)

A claimed Pareto improvement that only "wins" by prescience: decide the cheap
destructive probe `D1` at `t=1` *conditioned on* an observation `N2` of `X_2`
that only exists at `t=2`. `audit_realizability` returns
`realizable=False, violation=("acausal", "D1", "N2", 1, 2)` and
`reject_acausal_improvement` raises `RepairControlError`, so the acausal repair
never enters the frontier (test `test_falsifier_acausal_improvement_rejected`).
A probe scheduled before its datum arrives is likewise rejected (`"premature"`).

## 7. Boundaries / what is NOT claimed

- Gini (order-2) information is a lawful rational surrogate, **not** Shannon
  mutual information; the frontier shape is order-2 specific. The classical
  theorems invoked (data-processing, rate-distortion) hold for this surrogate.
- `F` models lossless pass-through for surviving carriers and total loss for
  consumed ones; a graded physical degradation is out of scope.
- The Pareto enumeration is over *static* realizable schedules; adaptive
  policies are handled only by the realizability audit, not optimized here.
- Nothing here bears on RH, zeta zeros, or any Weil positivity. Exact finite
  linear algebra over `Fraction`; a passing test is a check, not a proof of
  anything beyond the stated finite model.
