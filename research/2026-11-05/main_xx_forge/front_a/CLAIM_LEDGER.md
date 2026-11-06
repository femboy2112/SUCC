# Front A claim ledger

**Domain:** the authentic four-pole forcing, any real seed unless stated otherwise. **π base-16 normality: OPEN.**

## Proved results and reformulations

| ID | Claim (quantifiers) | Status | Support | Provenance | Next falsifier |
|---|---|---|---|---|---|
| FA-1 | ∀ forcing, seed, `r∈(0,1)`, `A>=2`: `P_{A,2A,r}=-Q_r(μ_A)+B_r/(2A)+θ·LIP_r/(30A)`, `\|θ\|<=1` | PROVED | RC3/RC4 rederived; calibration `\|E+Q-log2/A\|<=1.1e-17`, `\|θ\|<=0.033` | #520 front_delta RC3/RC4 | Any receipt with `\|θ\|>1` |
| FA-2 | `liminf P_{A,2A,r}>=0` ⟺ `Q_r(μ_A)→0` ⟺ fixed-h Weyl ⟺ (at `s=0`) π normal; `limsup P<=0` universally | EQUIVALENT-REFORMULATION (proved both ways) | PROOFS §A1 | #520 RC-03, R-02, SGO-09, Wall | Logical gap in epoch→prefix (needs all `A`) |
| FA-2s | Source-specific content of FA-2 is only the gauge `U_n+T_n=16^{n-1}π` with `T_n→0` | PROVED | §A1 audit | #521 CT7 | — |
| FA-3 | ×b-invariant `ν` with `ν>=Leb` on an open arc ⇒ `ν=Haar`; equivalently, deficiency appears in every arc | PROVED | Lebesgue decomposition plus Birkhoff | Classical ingredients; new to SUCC | Counterexample invariant measure |
| FA-3′ | `liminf_A μ_A(I)>=\|I\|` ∀`I⊂(0,ε)` ⇒ equidistribution (seed-uniform) | EQUIVALENT-REFORMULATION | FA-3 + R-04 | #520 R-04 | — |
| FA-4 | `p_0=1/16` and stochastically smaller digits ⇒ every 16-shell has nonnegative discrepancy | PROVED | Coupling; exact grid check | this front | — |
| FA-5 | Seed-uniform compactness: ∀η ∃δ,M,A_0 ∀s ∀A>=A_0: `𝒥^(1)<=δ ∧ V_{A,M}<=δ ⇒ Q_{1/2}(μ_A)<=η` (only `k=1`, `c<=c_*`) | PROVED (qualitative; no rate) | Contradiction + compactness; front B Lemmas 2.2–2.4 rechecked; FA-3 | builds on front B CB-2′ | A seed family violating it would contradict FA-3 or Lemma 2.2 |
| FA-6 | Coherent seed: `log2-2π^2Δ_A^2<=Q_{1/2}(μ_A)<=log2`, so `Q→log2` | PROVED + OBSERVED-finite | Enclosures at 5 `A` | — | — |
| FA-7 | Periodic: closed form `Q(ν_α)>0`; `\|Q(μ_A)-Q(ν_α)\|<=4(p-1)log2/A+4πT_A` | PROVED + OBSERVED-finite | 20/20 inside the band | — | — |
| FA-8 | Seed `1/5`: `c_A(h;1/5)=e(h/5)c_A(h;0)` | PROVED + exact check | `n<=2112` | #520 R-07 | — |
| FA-11 | Bernoulli: `J_∞` formula; only Haar has `J_∞≡0`; zero set of `J_∞(·,1)` has empty interior; single-lattice calibration exists | PROVED (paper) | §A3 FA-11 | — | — |

## Observed finite values (not evidence about the limit)

| ID | Claim | Status | Support | Next falsifier |
|---|---|---|---|---|
| FA-9 | True seed `A·Q_{1/2}(μ_A)∈{0.285,0.460,0.900,0.385,1.277}`; mutant in the same band | OBSERVED-finite | Interval enclosures | `A·Q>6` at a fresh `A` |
| FA-10 | CB-1 has 0 mismatches; max `sqrt(A)\|J\|=0.489`; coherent `J` exact | PROVED identity + OBSERVED-finite | Exact Fractions | `sqrt(A)\|J\|>4` at a fresh `A` |

## Refuted favourite-lemma variants

| ID | Claim | Status | Receipt |
|---|---|---|---|
| FL | ∃C ∀ seeds: `limsup[Q_{1/2}(μ_A)-C𝒥_A]<=0` | **REFUTED-with-receipt** | Front B CB-3 (rederived and audited) |
| FL-q | ∀ seeds: `𝒥_A→0 ⇒ Q_{1/2}(μ_A)→0` | **REFUTED-with-receipt** | Same as FL |
| FL-1 | Frequency existence + `liminf J>=0` ⇒ Haar | **REFUTED-with-receipt** | FA-4 / CM-A2 |

## Open items

| ID | Claim | Status | Note |
|---|---|---|---|
| FL-quant | Linear rate `Q<=C·sup\|J_∞\|` for invariant `ν` | OPEN | No countermodel and no proof |
| FL-0 | FL for the zero seed | OPEN | Unprovable by forcing-uniform arguments (CB-3) |
| LIMINF | `liminf_A Q_{1/2}(μ_A)=0` for π | OPEN | Would give every hex word infinitely often in π |
| GATE | `Q_{1/2}(μ_A)→0` for π, i.e. π base-16 normal | OPEN | unchanged |

## Audit of the orchestrator's CB items

| Item | Verdict |
|---|---|
| CB-1 | Correct |
| CB-2 | Correct but over-hypothesized (`k=1` and `c<=c_*` suffice) |
| CB-3 | Correct (constant 2.21 loose; true bound ≤2.134) |
| CB-4 | Correct factorization |
