# The operational triangle — SUCC's formal apparatus (2026-10-29)

**Status:** formal interface / research apparatus, installed by Operation Main XV. This is a
**typed mathematical framework**, not a claimed universal physical law and not a proof of π
normality or the Riemann Hypothesis. The finite Bernoulli source model below is a *declared
observer*, not a stochastic sampler of π's digit orbit. **π base-16/base-3 normality and RH
remain OPEN.**

SUCC remains freestanding: a theory of how a finite embodied observer constructs mathematical
knowledge from causal interactions. RH is a downstream application, not the definition. The
operational triangle gives that observational story an exact, composable shape.

## 1. The three vertices and the maps between them

```text
          finite-path / source update   K
                       /         \
                      /           \
                     v             v
      superposed endpoint field --------> observation / selection
      (mass + retained posterior)   O     (linear, nonlinear, carry)
```

1. **Finite-path / source update `K`.** A finite history, a source-dependent transition kernel,
   and a posterior-field update on the latent source. For the authentic BBP carrier the latent is
   `X ~ mu_a(dx) = e^{-ax}Q(x)dx / R(a)` with `Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}` and
   `R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)`; the orbit `U_n` keeps the original four signed poles and
   `U_0=0`.
2. **Superposed endpoint.** All finite histories reaching a coarse point, carried **with their
   path weights and the retained source posterior** — the measure-valued object
   `M_(a,m,j)`, not a bare integer grade. A point is `(j, q_(a,m)(j), nu_(a,m,j))`.
3. **Observation / selection `O`.** Explicit typed maps producing harmonic, Gamma, logarithmic,
   geometric, signed-character, and literal-carry observables.

### Composition and commutation discipline (load-bearing)

Every edge must carry a **declared map**. The framework's content is precisely *which routes
commute and which carry a defect*:

- **Commute:** path superposition and **linear** observers `A(j,x)` — enumerating word histories
  equals pushing forward to `(j,x)` and then observing (TG-01).
- **Strict information defect (do not drop):**
  - **Nonlinear** observers: `A(E X) != E A(X)` in general; strict Jensen for `log`.
  - **Posterior resetting:** replacing `nu_(a,m,j)` by the prior `mu_a` destroys predictive
    sufficiency; the covariance `R(a+16)/R(a) - [R(a+8)/R(a)]^2 > 0` is strictly positive.
  - **Premature primitive / parity projection:** merging grades `J=0,2` into one parity bit joins
    strictly different posterior source fields — irrecoverable source-information loss (TG-03).
  - **Integer-branch quotients and literal carry** `kappa_n`: exponentiation/parity reduction
    before the carry is attached is not justified; carries are extra integer-lift marks.

The source-update diamond is *flat under order-swapping of a fixed-grade word yet the letters are
statistically dependent*: **memory is not curvature.** Flatness of the update diamond does not
make all SUCC path geometry flat, and noncommuting observer/projection operations need explicit
defects.

### The one exact joint transform

For `m>=0`, `a>0`, `0<=z<=1`, `t>=0`,
`F_(a,m)(z,t) = E_mu_a[e^{-t a X}(z+(1-z)e^{-8X})^m]`
has two exactly equal finite representations (source-shift polynomial in `R`, and superposed
path/posterior sum), conserves `F_(a,m)(1,t)=R(a(1+t))/R(a)` at every depth, and specializes to
the earlier harmonic observer. See `research/2026-10-29/operational_triangle_frontier/THEOREMS.md`
(TG-03) and PR #386.

## 2. Sufficiency theorem and its stated boundary

For the declared retained-`X`, conditional-i.i.d. sensor, the endpoint grade `J=#ones` is an
**exact sufficient statistic for the latent-source question**: `X ⟂ W | J` and `I(X;W)=I(X;J)`
at every finite depth (TG-02). This is a specialization of the classical sufficiency / chain
rule, and it is **not universal**: a committed order-sensitive latent A/B countermodel (two
grade-1 paths with posteriors `P(A)=3/4` vs `1/4`) breaks sufficiency outside the exchangeable
model. Do **not** generalize the sufficiency theorem to arbitrary SUCC spaces.

## 3. The author's original triangle as a specialization — preserved, not replaced

The author's **Harmonic Numbers / Golden Ratio / Euler–Mascheroni triangle** and its
**Oily–Macaroni** vertex `Omega_OM = phi^{-1} - gamma = lambda - gamma` keep their names,
authorship, and roles. The naming provenance is recorded verbatim in
`research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md` (merged PR #365, the
FlammableMaths/FappableMaths callback and the macaroni/oily-cheese dish metaphor) and is
**not** altered here.

**Emergence map.** If a positive source kernel has `Q(x) ~ c x^{r-1}` near zero and the observer
depth satisfies `8m/a -> theta > 0`, then jointly `Y=aX => Gamma(r,1)`, `J|Y => Poisson(theta Y)`,
and
`F_(a,m)(z,t) -> F_(r,theta)(z,t) = [1+t+theta(1-z)]^{-r}` (TG-04, classical Laplace/Gamma/Poisson
under stated regularity). The **original four-pole source has `r=2, theta=1`** (because
`Q(x)=15x-(59/2)x^2+O(x^3)`), hence `F_infty(z,t)=(2+t-z)^{-2}`. Then:

- the latent slice `F_infty(1,t)=(1+t)^{-2}` identifies `Y ~ Gamma(2,1)`, whose **log observable**
  gives `E log Y = psi(2) = 1 - gamma`;
- the endpoint PGF `G(z)=F_infty(z,0)=(2-z)^{-2}`, **if separately iterated as an offspring PGF**,
  has a nontrivial attracting fixed point iff the mean `r theta > 1`; at `(2,1)` it is the golden
  root `q = phi^{-2} = (3-sqrt5)/2`, with `1-q = phi^{-1} = lambda` (from
  `(q-1)(q^2-3q+1)=0`);
- the **Laplace readout** at rate `lambda` gives `E e^{-lambda Y} = (1+lambda)^{-2} = lambda^2`;
- therefore `[Gamma log] - [fixed-point Laplace] = (1-gamma) - lambda^2 = lambda - gamma =
  Omega_OM` (using `lambda^2 + lambda - 1 = 0`).

So the Oily–Macaroni constant **emerges** from the rank-two source boundary and a properly scaled
superposed-endpoint / fixed-point observer, rather than being imposed as three algebraically
independent vertices. The branching/extinction reading is a **declared auxiliary iteration**, not
a claim that the π digit orbit is a physical offspring process.

**Keep two rank families distinct (TG-09).**
- fixed-golden probe (prior #369): `D_lambda(r) = psi(r) - lambda^r`;
- self-consistent (new): `D_self(r,theta) = psi(r) - q_(r,theta)`, where `q_(r,theta)` is the
  least fixed point of `G_(r,theta)`.

**The golden locus (TG-11, Operation Main XVI, PROVED).** The two families coincide exactly along a
one-dimensional curve, not only at the single point:
```
q_(r,theta) = lambda^r   <=>   theta = theta*(r) := lambda/(1 - lambda^r),   r > 0,
```
and the process is supercritical there (`r*theta>1`), so `lambda^r` is genuinely the least fixed
point. Calibration: `(r,theta,q) = (1, phi, lambda), (2, 1, lambda^2), (3, phi/2, lambda^3)`. The
clock `theta*(r)` is strictly decreasing from `+infinity` (`r->0+`) to `lambda` (`r->infinity`), and
the Laplace probe is **rate-locked** at the single golden rate `theta*(r)(1-q)=lambda` along the
whole locus. Hence `D_self(r, theta*(r)) = psi(r) - lambda^r = D_lambda(r)` for every `r>0`: the
golden locus is precisely the coincidence set `{D_self = D_lambda}`. **Restricted uniqueness:** on
the authentic clock slice `theta=1`, coincidence holds **iff** `r=2`. So the original BBP point
`(2,1)` is the *unique* intersection of its authentic clock `{theta=1}` with the golden locus — it
stays distinguished on its own source/clock slice, but it is **not** the only `(r,theta)` at which
the historical golden mark `lambda^r` equals the self-consistent root. (This corrects the earlier
"agree only at `(2,1)`".) Off the locus the two families differ. Proof and checks:
`research/2026-10-29/triangle_genesis_repair/GOLDEN_LOCUS_THEOREM.md`, `golden_locus.py`,
`tests/test_triangle_genesis_repair.py`.

The old triangle remains a **signature of a particular rank-two boundary**, not an axiom for
arbitrary spaces. The golden *fixed point* is realized by a one-parameter family of (rank, clock)
pairs on the locus, but the authentic *source-induced* boundary still forces rank `2`; the observer
clock `theta` tuned to recover a golden root must stay distinguished from that source rank. SUCC
continues to search for the triangle in Gamma / negative-binomial / supercritical branching /
order-statistic / arithmetic-finite-part spaces by the recipe in
`research/2026-10-29/operational_triangle_frontier/ORIGINAL_TRIANGLE_PROVENANCE.md`, recording exact
emergence conditions rather than forcing the golden parameter by hand.

## 4. Source discrimination and the firewall

- **Joint two-variable 59-jet (TG-05, PROVED LOCAL, independently re-derived).** At the native
  diagonal `a_n=8n-7, m=n`, with `d=2+t-z`,
  `F_n(z,t) = d^{-2} + J_BBP(z,t)/n + O_T(n^{-2})`,
  `J_BBP = [59 t^2 + 92 t z - 33 t - 511 z^2 + 813 z - 302]/[120 d^4]`,
  and against the Gamma-matched fake `Q_fake(x)=15x`,
  `J_BBP - J_fake = 59(1+t-z)/[120 d^3]` — a genuine source-visible readout, zero at `(z,t)=(1,0)`
  by mass conservation. This is **source discrimination of a joint observable**, not a selected
  signed cancellation and not a unique identification of all positive-source mutants
  (`Q_epsilon = Q + epsilon(1-e^{-x})^3` matches the first jet).
- **Seed-resolved Fourier tomography (TG-06/07/08).** The finite seed displacement
  `s -> s + u/16^n` yields distinct integer frequencies `h·16^j`, so every weighted **selected**
  phase `q_j e(h U_(n+j)(s))` is exactly recoverable — a **representation/observability** result,
  **not** a Weyl estimate. Averaging over the seed displacement vanishes for **every** seed,
  including the coherent same-forcing nonnormal counterseed `s* = -pi/16`. Recovering phases is
  information preservation, not normality.

**What must never be promoted (firewall).** Normality-equivalent observables, source-only
positivity, entropy formulas, Gaussian/Gamma phase rotations, and invertible signed filters are
**not** proofs of π normality. Equal endpoint marginals (the two-geometric Oily packet of #368,
the Pascal source of #370, the Gamma–Poisson sensor here) do **not** establish identical latent
couplings — do not transport proof or source ownership across those declarations. Positive
classical superposition is not a quantum amplitude.

## 5. Post-main frontier (Triangle Genesis)

**Weyl normalization convention (Operation Main XVI, P0).** Write the **unnormalized** Weyl sum
`T_N(h) = sum_{n<=N} e(h U_n(0))` (`|T_N| <= N`) and the **normalized** average
`Sbar_N(h) = T_N(h)/N` (`|Sbar_N| <= 1`). The Weyl/normality gate is
`T_N(h) = o(N)  <=>  Sbar_N(h) = o(1)` for every integer `h != 0`; it is **OPEN**. The vacuous
`Sbar_N(h) = o(N)` (true for every orbit, since `|Sbar_N| <= 1`) is **never** the gate — see
`research/2026-10-29/triangle_genesis_repair/WEYL_NORMALIZATION_CONVENTION.md`. The repo's
historical `S_N(h)` denotes the unnormalized `T_N(h)`, for which `S_N(h) = o(N)` is the correct gate.

The primary remaining target is a genuinely new, source-specific, zero-seed-sensitive **signed
intertime estimate** improving the trivial `|Sbar_N(h)| <= 1` on a declared sub-band, `h != 0`,
using all four authentic signed
poles and `U_0=0`, full radix-16 carries and four-bit Walsh sectors, the `q=3` orientation and
`q=6` primitive/cototient grades, the retained source posterior and joint Gamma/grade observables,
and the moving-grade / shrinking-target resolution of Kepler III (#384). It must **fail** on the
coherent same-forcing seed `s*=-pi/16`, Gamma-matched fakes, higher-jet-matched mutants, wrong
poles, prematurely averaged sources, phase aliases, nonnormal digit controls (Kempner, de Bruijn),
and independent holdouts — and must not reduce to invertible filtering, scalar `O(log N / N)`
reweighting, source-only phasors, or a restatement of the Weyl criterion. These are **open proof
obligations**, not theorems. See
`research/2026-10-29/operational_triangle_frontier/THEOREMS.md` (TG-07) and the Main XV handoff.

## 6. Status summary

| Object | Status |
|---|---|
| Finite measure-valued Pascal gluing, dual `F_(a,m)` routes (TG-01/03) | PROVED LOCAL (paper + exact Fraction tests) |
| Sufficiency `I(X;W)=I(X;J)` in the declared sensor (TG-02) | CLASSICAL, specialized; **non-universal** (order-sensitive countermodel) |
| Gamma–Poisson emergence class `F_(r,theta)` (TG-04) | CLASSICAL under stated regularity |
| Galton–Watson fixed point, `q=phi^{-2}` at `(2,1)`, `Omega_OM=lambda-gamma` (TG-05/09) | CLASSICAL analysis + **declared** observers; original-triangle SPECIALIZATION |
| Golden locus `q_(r,theta)=lambda^r <=> theta=lambda/(1-lambda^r)`; restricted uniqueness `theta=1 => r=2` (TG-11) | PROVED (classical GW/Gamma); supersedes "agree only at `(2,1)`"; exact + independent checks |
| Seed-alias dichotomy (7 classes) + corrected control slate (TG-12); literal-carry obstruction, no `|T_N|` saving (TG-13) | PROVED (exact ℚ + mpmath); negative result, selected cancellation OPEN |
| Two-variable 59-jet and fake difference (TG-05/TG-06) | PROVED LOCAL, independently re-derived |
| Seed-resolved tomography + universal seed-smearing zero (TG-06/07/08) | PROVED LOCAL (finite Fourier); representation, not Weyl |
| "Operational triangle certifies π normality / RH" (TG-10) | **REFUTED as an implication**; π normality and RH **OPEN** |
| Prime-ladder R4/R5 transcendence→entropy bridge (#334) | **REFUTED as a general bridge / UNVERIFIED for π** (Kempner firewall, #337) |

## References and provenance

- Frontier dossiers: `research/2026-10-29/operational_triangle_frontier/` — `README.md`,
  `THEOREMS.md`, `CLAIMS.md`, `ORIGINAL_TRIANGLE_PROVENANCE.md`, `VALIDATION.md`,
  `operational_triangle.py`, `independent_oracle.py`, `test_operational_triangle.py`.
- Main XVI repair & advance: `research/2026-10-29/triangle_genesis_repair/` —
  `WEYL_NORMALIZATION_CONVENTION.md` (P0), `GOLDEN_LOCUS_THEOREM.md` (P1, TG-11),
  `SEED_ALIAS_CLASSIFICATION.md` (P2/P3, TG-12/13), `golden_locus.py`, `seed_alias.py`,
  `independent_oracle_xvi.py`; regression `tests/test_triangle_genesis_repair.py`.
- Parent exact finite triangle: PR #386 (`research/2026-10-29/finite_field_superposition_triangle/`).
- Author naming provenance: `research/2026-10-28/AUTHOR_ANALOGY_PROVENANCE_LEDGER.md` (PR #365).
- Corrective firewall: `research/2026-10-27-furstenberg-kempner/KEMPNER_FURSTENBERG_FIREWALL.md`
  (PR #337); corrected reduction doc `research/2026-10-27-ravel-prime-ladder/PRIME_LADDER_REDUCTION_THEOREM.md`.
- Primary source: Bailey, Borwein, Plouffe, *On the rapid computation of various polylogarithmic
  constants*, Math. Comp. 66 (1997), 903–913. Digamma/Gamma: NIST DLMF §5.5.

Integration receipt and branch inclusion matrix:
`research/2026-10-29/main_xv_integration/MAIN_XV_INTEGRATION_RECEIPT.md`.
