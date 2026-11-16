# OPERATION π-SLOT — unfold the π operand, preserve the entire source

**Research-only, 2026-11-15, additive continuation of SUCC draft #649.** Original signed four-pole forcing, `U_0=0`, full rational lift, odd denominators, and historical source remain unchanged. No claim of π-normality, R0, physical energy or quantum/Higgs coupling. All mathematical advances are graded in `THEOREMS.md` and `CLAIM_LEDGER.json`.

## The single replacement that matters

The prior [randomized BBP coin in #649](https://github.com/femboy2112/SUCC/pull/649) satisfies `P(C=1|τ=t)=Q(t)/(16-t⁸)` and `E C=π/16`. **Retain τ and C together across all source times**. Then

`Y_n=C τ^(8n)`; `T_n=E Y_n`; `U_n=E[C(16^n-τ^(8n))]`; `E Y_nY_m=T_(n+m)`.

These are exact for every n,m. The source carries a single positive contraction `Lf=τ⁸ f` and a telescoping identity `Σ_(j≤N)16^-j(16-L)L^(j-1)=I-16^-N L^N`. This is the original signed-four-pole BBP series realized as one source-dependent **operator path**, not just as a numerical constant.

**Crucial nonlinearity:** `E[e(h16^n C)]=1` while `e(h16^n E C)` is the nontrivial real π orbit. Never average inside circle character/digit floor. The Poisson-generated complex product `e(hU_n)∏(1+i2πh C_j τ_j^(8n)/λ)` has the correct *expectation* and exact source variance. Shared marks across times provide signed Hankel correlations and increasingly cheap difference-probe variance.

Four-time signed source real lift: for any source times n,n+q,n+2,n+q+2, replace `255(16^q-1)16^n π/16` by the rational `Δ_qΔ_2 U_n` plus the **strictly positive** integral `D=E[Cτ^(8n)(1-τ^(8q))(1-τ^16)]`. This correction has `O(n^-3)` bound uniform in q, and `O(q n^-4)` when q is fixed. It is a real gain in **phase-transport precision**, not a signed Weyl cancellation theorem.

**Adversarial correction:** #648's integral polynomial coboundary mutation `g(n)=2n²` changes the arithmetic source/chiral holonomy **but not π/16 itself**. Its original target-change prose is incorrect. See PS-07. Thus 2-adic source holonomy is not by itself a gauge-invariant property of the completed real circle.

## What to read / run

- `PI_SLOT_ATLAS.md` — the audited π-bearing equation interfaces and safe substitutions.
- `THEOREMS.md` — PS-01 through PS-08 with domain, derivations, exact variance, source-gauge countermodel.
- `pi_slot_probe.py` — standalone standard-library authentic source, finite rational tail brackets, operator/Poisson sources, and phase sampler.
- `test_pi_slot_probe.py` — focused exact tests and hostile nonlinearity/mutation controls.
- `independent_audit.py` — separately coded SymPy/MPMath oracle and finite numerical receipts; optional dependencies.
- `FINITE_REPORT.json`, `TEST_OUTPUT.txt`, `ORACLE_OUTPUT.txt`, `VALIDATION.md` — executed outputs with exact limitations.
- `NEXT.md` — the missing *noncircular* signed arithmetic inequality and falsifiers.

Run `python -m unittest discover -s research/2026-11-15/bbp_pi_slot_lifting -p 'test_*.py'` after checking out the draft branch, or `python independent_audit.py` within this directory. The native SUCC root gates are NOT claimed for this additive isolated research commit.

**All frequencies:** `all_mode_oily_pair_sample` additionally samples a harmonic from #644's complete Oily law, uses intensity `λ_h=λ₀h²` and **two independent coherent whole-shell replicas**. Its signed real cross-product expectation equals the entire positive normality energy, with finite expected Poisson row count `64λ₀/3` and uniform-in-h second moment. The target decay remains open. Proof: PS-09.
