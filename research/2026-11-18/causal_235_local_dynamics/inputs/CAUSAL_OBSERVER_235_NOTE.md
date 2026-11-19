# Causal observer lift for the 2–3–5 BBP/Fibonacci/pentagon program

**Date:** 2026-11-18. **Status:** research-only; exact finite algebra and a proposed source-selected test, not a pi-normality proof. **Provenance:** SUCC main `81be6b897ae980b801a3b9de9e22ef81e8360bfb` (`docs/principia_observatoris/SYNTHESIS.md`, `docs/MAIN_XXVI_OBSERVER_TRANSPORT.md`, `docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md`); SUCC PRs #322, #428, #430; user's earlier `15_angry_blind_fibonaccis_2x5x3_research.md` (18 Nov). No repository files modified.

## Steelman: the moving observer is part of the source carrier

The physical/computational arrow of time is a forward semigroup of legal source transitions. In a chosen observation frame, selected coordinates may repeat periodically without returning either the carrier to its past or the observer's retained memory to its previous state. The observer models the past and predicts the future using its current record; its model-inferred inverse is not a physical inverse. A claimed source-to-observer intertwiner must respect access order, selected origin, integer winding, memory, and declared readout.

## CO235-01 (classical exact): an observational cycle never resets its causal lift

Let a,b be the permutations `a=(12)(34)` and `b=(245)` on `{1,2,3,4,5}`. Under right-to-left permutation composition, `a^2=b^3=(ab)^5=I`, with `ab=(12345)`. These generate 60 permutations, the alternating group `A5`.

For any generator g in {a,b}, define a forward causal action on `(n,s,m)` by

`G_g(n,s,m) = (n+1, g(s), m concatenated with (g,g(s)))`.

Thus the words `a^2`, `b^3`, and `(ab)^5` act trivially on s but **not** on elapsed time or append-only memory. For `(ab)^5`, the elapsed time is 10 ticks and the transcript has 10 entries. No projection-level finite-order relation becomes a return to a prior causal state. This construction is auxiliary: it does not identify the BBP successor with the icosahedral action.

The independent commuting construction `C2 × C3 ≅ C6` gives five nonconstant regular-representation Fourier modes after removing the constant mode. Those five dimensions are not an order-5 group element. Neither a 2/3 group relation nor a 5-dimensional representation is automatically a 2-adic/3-adic source map.

## CO235-02 (exact): original BBP null differences are present-time, past-readable with k-tick delay

For original forcing

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), n>=1`, define

`r_k(n)=(-1)^k Δ^k r(n) = sum_{j=0}^k (-1)^j C(k,j) r(n+j)`.

Let `∇^k r(t)=sum_{j=0}^k (-1)^j C(k,j)r(t-j)` be the kth *backward-looking* difference, using only remembered samples. Then

`r_k(n) = (-1)^k ∇^k r(n+k)`.

Thus this signed null-jet is available from observed history at time `t=n+k`, with k units of latency, rather than by rewinding time. If the original rational law is known, a model may predict a future-indexed source term; such predictions are not observations of future events. The classical integral representation

`r_k(n)= ∫_0^1 t^{8n-8}(1-t^8)^k (4-2t^3-t^4-t^5)dt`

still holds. Its asymptotic `r_k(n) ~ 15(k+1)!/(64 n^{k+2})` is for each *fixed k* as `n→∞`; any `k=k(n)` requires uniform estimates.

## CO235-03 (exact algebra; source-specific polynomial, auxiliary operators)

Let `Q(t)=4-2t^3-t^4-t^5=(1-t)H(t)` with `H(t)=4+4t+4t^2+2t^3+t^4`. For `H_k(t)=H(t)(1-t^8)^k`, `A=[[1,1],[1,0]]`, `M=A^{-1}`, and `R` the cyclic five-coordinate permutation, let `V0={v in C^5: sum(v)=0}`. Define

`N_F(P)=det P(M)` and `N_5(P)=det(P(R)|V0)`.

Then the exact finite identities are

`N_F(H)=55`, `N_5(H)=55`, `N_F(1-t^8)=-45`, `N_5(1-t^8)=5`, hence

`N_F(H_k)=55(-45)^k`, `N_5(H_k)=55*5^k`, `N_F(H_k)/N_5(H_k)=(-9)^k` for every k>=0.

This is a comparing two *auxiliary* observer norms, not a native BBP temporal transfer. In particular `v_3((-9)^k)=2k`, `v_2((-9)^k)=0`, but the real absolute value grows as `9^k`: 3-adic convergence is not Archimedean mixing. The source mutation `H(t)→H(t)+t^4` breaks the common depth-0 norm; that is a direct falsification control.

## CO235-04 (paper-level obstruction): observable phase inverse has branches

For the exact completed BBP orbit `z_n=exp(2πi16^n pi/16)`, the forward law is `z_(n+1)=z_n^16`; retrieving z_n from z_(n+1) alone has 16 possible circle branches. In SUCC's original rational source, `U_0=0`, `U_(n+1)=16U_n+r(n+1)`, and `U_n+T_n=16^n pi/16`, the nonobservable completed tail `T_n` is a mathematical future completion and must be approximated by a lawful prediction if the observer is restricted to records through time n. Retain the actual carries, source clock and seed; purely phase-projected reverse inference is underidentified.

SUCC #322 establishes a 2-adic time/state isometry and a separately typed 3-adic cleared-numerator bijection, while its naive `Q3` backwards source Green sum diverges. SUCC #430 isolates sharp 3-adic poles and the failure of a dominated-convergence shortcut. These facts **support the need for distinct prime-place instruments**, not the conclusion that every 2/3/5 auxiliary cycle is already source-generated.

## CO235-05: observer prediction defect (Main XXVI/Principia interface)

Let `X_(n+1)=K_n X_n` (forward source), `y_n=P_n X_n` (readout), and `B_n` the observer's **internal** model of the next report. Its signed one-step defect is

`D_n=P_(n+1) K_n - B_n P_n`.

If there are two hidden carrier states sharing the same y_n but producing different y_(n+1), no such exact deterministic B_n exists on that projected state alone. Memory can refine the observation fiber; revisiting an old report value cannot reconstruct the lost causal history. This is the exact boundary in SUCC Principia's `u→v→t→t` counterexample.

## Crucible and next probe

- **Wrong-seed source control:** `s=-pi/16` preserves all source-only H_k norm identities while the completed circle orbit is identically zero. Therefore source norms, A5 cycles and the causal-lift time coordinate alone cannot certify real Weyl cancellation.
- **No 3-adic/real inference:** `(-9)^k→0` in Q3 while `|(-9)^k|→∞` in R; drawing a real contraction from the p-adic defect is refuted.
- **No time travel:** a backward algebraic inversion is an estimator/prediction that must justify the branch from retained history, not a second physical temporal arrow.
- **Probe proposal, not a theorem:** instrument forward-only original-zero BBP carries and real phases *conditioned on* true 2-adic source-state and source-legal 3-adic numerator classes. Pre-register later original-zero shells and a wrong-seed control. Require conditional **unweighted** phase escape on each selected clock class rather than merely averaging an auxiliary mean-zero character, since a balanced character can give false cancellation on a completely locked real orbit. The missing result remains a signed all-shell estimate for the authenticated zero seed.

## Executed exact controls

`test_causal_235.py` uses only Python stdlib. At authoring time, 6/6 unittest methods passed: 60-permutation closure; finite-order words versus retained clock/history; finite differences with k-step latency; 7 null depths of 2x2/4x4 exact integer determinants; source mutation failure; 2/3-adic versus real magnitude distinction. These do not constitute complete repository gates, Lean certification, an external audit or π normality.

**Claim status:** CO235-01, -02, -03: exact finite/classical mathematics as scoped and locally tested. CO235-04: classical phase inverse obstruction and sourced 2/3-adic results. CO235-05: classical factorization condition. Application of the combined observer to selected original-zero signed cancellation: **UNVERIFIED**. R0 and full base-16 π normality: **OPEN**.
