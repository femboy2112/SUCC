# Entanglement as the relational shape of causal interference: two descriptions, one meeting

**2026-11-12 · Draft research continuation of SUCC PR #604.** This is a chosen finite operational model, not a physical Einstein–Rosen bridge, not an independent proof of ER=EPR, and not a derivation of a physical quantum state from the BBP source. The full original four-pole BBP source and literal `U_0=0` are unchanged. R0, π base-16 normality, Goldbach, completed Weil positivity and RH remain **OPEN**.

## 0. Steelman: what is being proposed

The user's sharper hypothesis is **not** “entanglement transmits information.” Entanglement is an initially prepared *non-factorizing relational shape*, while the two observers independently encounter a shared source/carrier through **lawful local interactions** along time-oriented paths. These interactions impress phase and/or information into the joint relational degrees of freedom. The observers can compare only their **present**, mutually transported model reports at a single causally admissible rendezvous. A third external view may call the relational bond a “wormhole” or shared carrier defect. The intended equivalence is between two descriptions of the **same set of boundary observables**, not an operational ability to send a message through the entanglement bond.

A genuinely traversable wormhole would be an *additional* physical claim involving a spacetime metric, causal propagators and a coupling or stress tensor. None is derived here.

### Typed diagram

```
                              mathematical carrier S
                           /                         \
     source-pinned observer A                         source-pinned observer B
       local U_A(C_A) / phase α                           local U_B(C_B) / phase -β
                 |                                                   |
     fixed entanglement resource  |Phi+> in A ⊗ B    (no remote channel)
                 |                                                   |
               A's current output    ----> M <----      B's current output
                                            |
                            joint XX and XY correlations in M
                            source authentication is separate
```

The diagram's middle line is a **tensor-network bond**, not a propagating causal arrow. All arrows carrying actual interaction/measurement outcomes are in the appropriate forward light cone. See historical `TWIN_RENDEZVOUS.md` for the independent rational Lorentz-frame model. This continuation isolates a common `U(1)` carrier connection and its source-relative interference response.

## CBR-01 — local source-to-meeting transport, exact gauge-covariant result

Work on a finite graph with vertices actualized as events `(label,t,x)` in a flat `1+1` common Minkowski chart with `c=1`. Each chosen oriented link `e:i→j` has `t_j-t_i>0`, `t_j-t_i≥|x_j-x_i|`, and a **declared** rational phase increment `a_e ∈ Q/Z`. A path is an ordered composable list of links ending at `M`. A separate source pin/calibration `c_A`, respectively `c_B`, supplies the initial anchor. These phases are *chosen observational coupling coefficients*, not a physical gauge potential extracted from arithmetic.

Let `θ_A=c_A+Σ_{e∈A} a_e` and `θ_B=c_B+Σ_{e∈B} a_e` in `Q/Z`. Define the **present rendezvous output**

`Δ_M = θ_A(M) − θ_B(M) ∈ Q/Z`.

If both observers share the same ambient gauge function `g` on all relevant vertices, use the transformation `a_(i→j) -> a_(i→j)+g(j)-g(i)` and **transport the source pins** `c_A -> c_A+g(A_start)` and `c_B -> c_B+g(B_start)`. Both present phases change by `+g(M)`; hence **the difference `Δ_M` is exactly unchanged**. This is an algebraic all-path theorem by telescoping, not a finite-sample claim. Independent gauge choices *without* a comparison isomorphism are not a common frame. Existing `twin_rendezvous.py` separately handles exact Lorentz charts; the present U(1) rule must not be mistaken for spinor parallel transport or curvature in GR.

The executable `PresentOutput` contains only `meeting`, one final model phase, source-contract label and frame identifier. The comparison routine refuses different meetings, frames and source contracts; it never directly compares distant past events. The simulator may keep paths to construct these current outputs, but the verifier has only their projected present fields. A past event carried in a memory is *present information*, not an extra spacelike measurement.

## CBR-02 — the Bell shape makes locally produced information jointly observable

Prepare `|Φ+>=(|00>+|11>)/√2`. Take two **local** diagonal phases

`U_A(α)=diag(1,e^{iα}),  U_B(-β)=diag(1,e^{-iβ})`.

At the common meeting, their joint state is

`|Ψ(Δ)>= (|00> + exp(i Δ)|11>)/√2`, with `Δ=α−β`.

For each Δ, both reduced states equal `I_2/2`. No local measurement by observer B can determine whether A changed α. But at M, the **joint observables** are

`<X_A X_B>=cos Δ`, `<X_A Y_B>=sin Δ`.

Derive the first by `X⊗X|00>=|11>`, `X⊗X|11>=|00>`; the second by `X⊗Y|00>=i|11>`, `X⊗Y|11>=-i|00>`. The two observables generally **do not commute**, so separate ensembles/settings are required for their expectations. A single Bell outcome does not deterministically reveal arbitrary Δ.

For rational turns `q=Δ/(2π)∈Q/Z`, the two expectations are represented **exactly** by elements of `Q(i)[Q/Z]`:

- `<XX> = (e(q)+e(-q))/2`;
- `<XY> = (e(q)-e(-q))/(2i)`.

The library `FormalFourier` retains the source's signed exponents; it only evaluates exactly at quarter turns (`e(k/4)=i^k`). For arbitrary rational BBP phases, a formal expression is **not** a certified complex interval or an all-N signed estimate. This is an honest carrier-to-observable representation, not evidence of equidistribution.

**Countercontrols.** A dephased classical state `1/2(|00><00|+|11><11|)` has the same local marginals but `<XX>=<XY>=0`. Changing both local phase pins by the same δ leaves Δ unchanged: identical joint readouts can arise from two *wrong but correlated* paths. The separate zero-source witness remains necessary.

## CBR-03 — the bridge (outside) and entanglement (inside) descriptions coincide on a narrow language

With `|Φ_d>=d^-1/2 Σ_j |j,j>`, direct matrix-element calculation gives the **Choi/vectorization “mirror” identity** for every complex matrix `M`:

`(M⊗I)|Φ_d> = (I⊗M^T)|Φ_d>`.

**Proof:** coefficient of `|a,b>` on the left is `M_ab/√d`. On the right it is `(M^T)_(b,a)/√d=M_ab/√d`. Thus a tensor diagram may slide a labelled operator across the internal *Bell bond* by transposition without changing the **boundary amplitude**. `choi_left_and_mirrored_right()` verifies the two actions by independent finite sums over exact Gaussian rational matrices; **625 tested matrices**, including nonunitaries.

This supplies a precise, intentionally narrow correspondence between an external “bridge/bond” diagram and an internal entangled-twins diagram. It does **not** turn the right-side transposed operator into an action physically executed at B: no state-change signal or faster-than-light communication follows. Nor does it supply a Lorentzian wormhole, gravitational dynamics, Einstein's equations, RT/ER holographic entropy or a traversable bulk.

**Witness distinguishing the shape:** replace the Bell bond by product `|00>`. For matrix `M=X`, `(X⊗I)|00>=|10>` while `(I⊗X^T)|00>=|01>`, so the slide identity fails. It really uses the *entangled* bond shape. A classical correlated mixture also lacks the required off-diagonal phase signal.

A physically traversable wormhole is a different construction: Gao–Jafferis–Wall (JHEP 2017) introduce an explicit two-boundary coupling and obtain a negative **average null energy** effect without violating causality. This is **not** the prime-power negative term in the completed zeta Weil form. In the Maldacena–Susskind proposal (2013) entangled black holes can have nontraversable ER bridges; extension to generic entangled systems is conjectural, not established by the matrix identity above.

Primary background: <https://arxiv.org/abs/1306.0533>, <https://arxiv.org/abs/1608.05687>, <https://www.ias.edu/ideas/2013/maldacena-entanglement>, <https://doi.org/10.1103/PhysRevD.98.046016>.

## CBR-04 — the original BBP carrier can supply *labels*, not the quantum interaction law

Keep frozen `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, literal zero `U_0=0`, `U_n=16U_(n−1)+r(n)` and zero-seed source witness `Z_n=16^(−n)U_n−P_n`. `original_bbp_r`, `original_bbp_state`, and `original_bbp_seed_recovery` are independent rational transcriptions for a hostile cross-check against the canonical `duck_bbp` module on full checkout. `r(1)=47/15` and `{U_1}=2/15` are exact. Setting a **chosen** local phase to `2π{U_1}` yields a formal `XX/XY` signature with rational-cyclotomic exponents; it is not an empirically measured phase and it proves no π-normality statistic.

If the selected seed is altered to `s=1/16`, the same forcing can produce later circle-phase aliases while the unwrapped source witness detects `Z_n=s`. Merely recovering an operator slide or an interference pattern is **blind to source identity** and does not discharge `R0`, signed Weyl, parity balance, Goldbach or RH.

## CBR-05 — a verdict-changing bridge test

Specify a genuine source-derived functor `F` taking each authenticated arithmetic event/path to a legal **local interaction channel**, without injecting an expected answer via a fitted phase. Declare a comparison instrument in the joint future region, and prove a commuting square between (a) the entangled local path view and (b) a geometrically specified bridge/defect view for a declared **separating family** of observables. The weakest pass is a nontrivial **source-selected** signed bound that survives wrong seed `1/16`, the coherent counterseed `s=-π/16`, constant/non-normal, fake-composite 6, independent dephased environment, and correlated path errors. An operator-slide identity or exact Bell correlator alone is insufficient.

A genuine GR comparison further requires a metric, causal cones, semiclassical stress tensor and a defensible boundary/bulk map. No such data are produced by this finite construction. Results are scoped to **algebraic boundary equivalence**, not ER=EPR itself.

## Reproduction

`PYTHONPATH=. python -m unittest discover -s tests -p 'test_causal_bridge_observers.py' -v`

In isolated Python 3.13.5 staging: 20 tests run, **19 pass / 1 skip** (the optional source-module cross-check needs the full checkout). Exhaustive gauge probes 25 combinations and exact matrix probes 5^4=625. The universal identities have the written proofs above; tests only support the implementations. See [claim ledger](CAUSAL_BRIDGE_CLAIMS.md) and [validation](CAUSAL_BRIDGE_VALIDATION.md). No original repository file overwritten.
