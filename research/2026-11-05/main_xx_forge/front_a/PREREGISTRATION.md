# Front A preregistration: the Clausen gate and the carry gate

**Written 2026-11-05. No experiment in `front_a_probe.py` had been run when this file was written.** Paper work came first. It was an independent rederivation of the carry identity and of the stationarity rigidity; front B's CB-1..CB-4 file appeared afterwards and was checked line by line against that rederivation. π base-16 normality is OPEN. Nothing below can promote it.

Source (immutable): `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)`, `x_n={U_n}`. Also `c_A(h)=A^-1 sum_{n=A}^{2A-1} e(hU_n)`, `μ_A` is the epoch measure, and `Q_r(μ)=sum_{h>=1}(r^h/h)|μ^(h)|^2`.

## A1 — audit of #520's finite-cut inequality

**H-A1 (to prove both ways).** Write `P_A=P_{A,2A,1/2}`. Then `liminf_A P_A>=0` ⟺ `Q_{1/2}(μ_A)→0` ⟺ `c_A(h)→0` for every `h≠0` ⟺ π is base-16 normal. The predicted exact finite form is
`P_A = -Q_{1/2}(μ_A) + log2/A + θ_A·4π/(30A)`, with `|θ_A|<=1`.
This would make `limsup_A P_A<=0` hold universally, so the "one-sided" open inequality is really a two-sided limit.

**Falsifiers.**
- A logical gap in RC3/RC4 or in the epoch-to-prefix step.
- A numerical violation of `|P_A+Q_{1/2}(μ_A)-log2/A|<=4π/(30A)` at any preregistered `A`. This is an instrument check of a proved identity, not evidence about π.

**Prediction for the split.** The source-specific inputs are only the Green-tail gauge `U_n+T_n=16^(n-1)π` with `T_n→0`. Every other step is generic for any forcing.

## A2 — favourite candidate lemma, stated BEFORE any hostile test

**FL (Clausen–carry transfer, forcing-uniform).** There is an absolute `C<∞` such that, for **every** real seed `s` under the authentic forcing,
`limsup_A [ Q_{1/2}(μ_A(s)) - C·𝒥_A(s) ] <= 0`.
Here `𝒥_A(s)=sup{|J_{A',m,k}(s)| : A<=A'<=4A, (A',m,k) admissible}` and `J_{A,m,k}=A^-1 sum_n (b_{n,m,k}-δ_{n,m,k})` (#522 HS-08).

- **FL-q (qualitative).** `𝒥_A(s)→0` implies `Q_{1/2}(μ_A(s))→0`.
- **FL-0.** The same statement for the literal zero seed only.

**Hypotheses.** The forcing is authentic. An admissible triple means `m,k>=1` and `16^(m+k)T_n<=1` on the epoch.

**Mechanism.**
1. The carry bit is an exact interval indicator of the orbit on Green-tail shells near 0 (CB-1).
2. Every weak limit of `μ_A` is ×16-invariant (#520 R-04).
3. A ×16-invariant measure that agrees with Lebesgue near 0 is Haar (rigidity lemma, to be proved).

**Why FL would count as an advance.** FL is weaker in proof debt than fixed-h Weyl: it is a transfer inequality, not a cancellation estimate. If true, it would move the entire normality gate onto source-threshold carries.

**Hostile falsifiers, declared in advance.**
- **F1** kills FL and FL-q as forcing-uniform statements. It would be a same-forcing seed with `𝒥_A→0` and `limsup Q_{1/2}(μ_A)>0`. Candidate: a phase-locked independent-digit seed whose digit law at time `N` is calibrated to the source lattice `{16^j/(64N^2)}`. It is built on paper only. The numerical "Bernoulli lattice-calibrated" build belongs to another agent and will **not** be done here.
- **F2** kills the one-sided variant FL-1: `liminf inf J>=0` plus stationarity implies Haar. It would be an invariant non-Haar measure with nonnegative carry limits on every shell. Candidate: an i.i.d. digit law with `p_0=1/16` and stochastically smaller digits.
- **F3** kills the linear rate even under stationarity. It would be invariant measures with `Q_{1/2}/sup_c|J_∞|→∞`. If none is found, this stays OPEN and is not claimed.
- **F4 (finite).** No finite computation at the zero seed can refute an `o(1)` statement. `A·Q_{1/2}(μ_A)` and `sqrt(A)·sup|J|` are recorded as OBSERVED-finite only.

**Corrected formulation, to be proved if FL dies (CC).** For every `η>0` there are `δ>0`, an integer `M` and `A_0` such that, for every seed `s` and every `A>=A_0`, `𝒥^(1)_A(s)<=δ` together with `V_{A,M}(s)<=δ` implies `Q_{1/2}(μ_A(s))<=η`.
- `𝒥^(1)` uses only `k=1` and lattice values `c<=c_*`, for one fixed `c_*>0`.
- `V_{A,M}` is the largest kernel distance between the `7M` mesh sub-windows of `[A,8A)` and `μ_A`.

## A3 — exact controls: predictions with numbers

The preregistered epochs are `A ∈ {64,173,347,691,1024}`. The truncation is `H=50`, with rigorous tail `sum_{h>50}2^-h/h <= 2^-50/51`. The trigonometric factors use outward interval arithmetic (`mpmath.iv`, 80 bits) evaluated on exact Fraction phases `{h x_n}`.

1. **Coherent seed `s*=-π/16`.** Prediction: `log2-8π^2Δ_A^2 <= Q_{1/2}(μ_A) <= log2`, where `Δ_A=T_A-T_{2A-1}<1/(64A^2)`. The limit is `log2`.
2. **Periodic completions `α=k/(16^p-1)`.** Cases: `α=1/15`, and the nearest such `α` to `π/16` for `p=2,3,4`. Prediction: `|Q_{1/2}(μ_A)-Q_{1/2}(ν_α)| <= 4(p-1)log2/A+4πT_A`, where `Q_{1/2}(ν_α)=p^-2 sum_{i,j}-log|1-½e(α_i-α_j)|>0` is the closed form.
3. **Rational seed `1/5`.** Prediction: exact identities `x_n(1/5)={x_n(0)+1/5}`, `{h x_n(1/5)}={h x_n(0)+h/5}`, and therefore identical `|c_A(h)|` and identical `Q`. Any mismatch falsifies the claim.
4. **True seed.** Under the Haar–iid model, `A·Q_{1/2}` has mean `log2`. Anomaly falsifier: `A·Q_{1/2}(μ_A)>6` at any preregistered `A`; the model probability is below `1e-4`. A pass is OBSERVED-finite and proves nothing.
5. **Carry probes (true seed).** Epochs `A ∈ {173,347,691,1024}`, `k ∈ {1,2}`, every admissible `m`.
   - CB-1 must hold with **zero** mismatches against the HS-01 definition.
   - Anomaly falsifier: `sqrt(A)·sup|J|>4`.
   - For the coherent seed, `J=-A^-1 sum δ` exactly.
6. **One-pole mutant** (`3/(8n-7)` in place of `4/(8n-7)`). Prediction: the same band as the true seed. The instrument is not source-selective.
7. **Instrument calibration.** The pair-sum energy `E_{A,1/2}(0)` and `-Q_{1/2}(μ_A)+log2/A` must agree to `1e-9`, and `|P_A-E_{A,1/2}(0)|<=4π/(30A)`.
8. **Bernoulli product measures (paper).** Derive the carry limit functional `J_∞(c,k)` from `μ^(h)=prod_i φ_p(h16^-i)`. Predictions:
   - Haar is the only i.i.d. law with `J_∞≡0`.
   - Calibration on one lattice `c_*16^Z` is possible.
   - Calibration on a full log-period is impossible.
