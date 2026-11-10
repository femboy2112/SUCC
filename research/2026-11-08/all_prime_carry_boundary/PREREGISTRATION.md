# Frozen protocol: ALL prime residues at the real carry boundary

**Date**: 2026-11-08. **Parent**: SUCC #560 at `f33705847afa9a4ff4fe6fdeb30f24754494345c`. Exact four-pole BBP forcing, U0=0, integer lifts, and all imported files frozen. π normality and real signed Weyl decay OPEN.

**Correction to earlier front:** A pole birth or a single p-primary injection is not the total carry. Keep every prime power of the common conductor Q=lcm(den(U_(n-1)), den(r(n))), including inherited p-primary unit residues with *zero source injection* and all local winding integers.

**Predicted exact finite identities (no analytic inference):**
1. Local additive characters `theta_(p,n)=[U_n]_p in Q/Z` and source fractions `rho_(p,n)=[r(n)]_p` satisfy `theta_(p,n)={16theta_(p,n-1)+rho_(p,n)}`. Winding `j_p=floor(16theta_(p,n-1)+rho_(p,n))`, with absent-prime fractions zero.
2. Let `S_n=sum_p theta_(p,n)`, `q_n=floor(S_n)`, `R_n=sum_p rho_(p,n)`, `J_n=sum_p j_p`, and `m_n=r(n)-R_n in Z`. Prove literal carry `kappa_n=floor(U_n)-16floor(U_(n-1)) = m_n+J_n+q_n-16q_(n-1)`, with all-prime contribution retained and with source r(1)>1 handled.
3. Common-conductor CRT preimage (min[0,Q)) of the inherited real phase has exact boundary gate `floor(16m/Q+r(n))`. Build complete carry fiber threshold histogram, not merely carry==1 or newly born p.
4. For any partial prime subset product M|Q, the complementary L=Q/M residues in each fixed M-fiber produce interior k=1..15 carry counts within O(1) of L/16 (uniform reference only). If L≥17, every interior carry occurs for every such fiber. Prove directly by interval/progression counting and record limitations for endpoint carries 0,16.
5. Counterfactual reference controls: n=2 authentic r(2), exact previous U1=47/15; keep its p=3 local fraction while varying inherited p=5 local fraction, with 5∤den(r(2)); determine whether the actual carry changes. Do not call alternative phases authentic U0=0 or use this to deduce π normality.

**New holdout**: certify complete source transitions n=17..32 (not pre-seen in this round), with all denominator primes and their p^v exponents, exact literal carries from independent unwrapped Fraction and integer conductor engines, global q winds, zero-input primes, and source-only prime births separately. Test arithmetic mutations: omit inherited-but-nonforcing primes; replace p^v by p; reduce literal carry modulo 16; drop the q winding; reverse additive-character signs.

**Passing means:** exact identities and independence-checked controls hold, or explicitly recorded failure with reproduction. Any finite histogram, DFT or wrong-seed reference is a diagnostic/negative control only. Prove no unearned unconditional bound on zero-selected `W_A(h)` or signed #544/#554 lag. No main merge/tag/release.
