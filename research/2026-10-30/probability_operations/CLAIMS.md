# SUCC probability-operation claim ledger

Date 2026-10-30; stacked draft child of PR #409, source original unchanged, selected U_0=0 unchanged. Normality of π and RH remain OPEN.

| ID | Claim & quantifiers | Status | Hostile control / boundary |
|---|---|---|---|
| PO-01 | If U,U1,U2 independent Uniform(0,1), sqrt(U) and max(U1,U2) have the same t² CDF | CLASSICAL / exact | Beta(c,1) with c≠1 also passes; δ0 passes, so law not uniquely characterizing Haar |
| PO-02 | Even on a normal orbit, consecutive full radix tails (x_n,x_(n+1)) are graph-Haar, not independent; at t=1/3 event max<=t has limit 1/8 vs t²=1/9 | DISCLOSED exact measure calculation | Falsifies naive independent-tail test; disjoint fixed-block sampling or independent time-index sampling needed |
| PO-03 | Uniform fair-branch operator P μ=1/16 Σ_d (y→(d+y)/16)_*μ is 1/16-contraction in W1 and has unique fixed point Lebesgue | CLASSICAL IFS specialized to 16 | Actual deterministic inverse identity without independent fair digit is tautological |
| PO-04 | For α arbitrary and pure radix x_n, ε_N=W1(μ_N,P μ_N^+) satisfies (16/17)ε_N−1/(17N)≤W1(μ_N,λ)≤(16/15)ε_N+1/(15N); hence ε_N→0 iff α base16 normal | DISCLOSED exact quantified criterion | Normality-equivalent; finite ε never falsifies asymptotic normality; coherent α0 has ε=15/32 |
| PO-05 | If normal base16, two disjoint nonoverlapping k-digit blocks in each aligned 2k-word are asymptotically independent grid uniforms at each fixed k; sqrt-max CDF difference ≤3/16^k | CLASSICAL Wall base-power normality, exact CDF discretization | Requires first N→∞ then k→∞; no rates for moving k(N) |
| PO-06 | For independent uniforms, G_r=−ln∏U_i~Gamma(r,1), E(logG_r−e^(−λG_r))=H_(r−1)−γ−λ^r; r=s+2 reproduces full SUCC Oily tile D_s | CLASSICAL exact identity | Generic to ALL normal sequences; unbounded empirical expectation needs additional tail/limit control |
| PO-07 | Atomless idempotent law μ*μ=μ on circle is Haar | DISCLOSED elementary Fourier proof | δ0 and uniform finite subgroups are idempotent and non-Haar if atomlessness dropped |
| PO-08 | Exact four-pole BBP rational intervals certify enough π/16 digits to compute finite truncated ε and quantitative W1 upper bound | OBSERVED exact finite scope | N=32,128,256 finite only, near-boundary and tail errors separately bounded; no all-N saving |
| PO-09 | Source-specific ε_N→0 or limsup ε_N>0 for the original selected π/16 state is proven | UNVERIFIED | Require independent original four-pole/carry/CRT arithmetic bound, full same-source and normal controls; π normality remains OPEN |

Proof debt: identify an arithmetic route that genuinely controls branch–tail factorization for the *selected* zero-seed orbit, not a source-only posterior, Haar seed average, or retrofitted stochastic rule. Transport full raw/adjusted/conditional views; do not assume actual digit randomness.
