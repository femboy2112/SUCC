# Operation Prime Stroboscope — the authentic BBP source has a modular frame reset

**DRAFT research-only, 2026-10-30.** Parent `main@e18ba565ca540adb7edf3292f5593929e76d91c5` (Main XVI). Independent contemporaneous draft contexts: #390–#396; #395 is the Stoneham frame-reset positive/negative control. No `main`, original BBP source, historical theorem namespace, `U_0=0`, provenance archive, workflow or production code modified. **Base-16 normality of π and RH remain OPEN.** This is a new-to-current-SUCC derivation of classical modular and p-adic arithmetic; scholarly priority is not asserted.

## The mathematical advance

For the **authentic four-pole** rational forcing

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_0=0`, `U_n=16 U_(n−1)+r(n)`,

an odd prime `p ≡ 1 (mod 4)` and `k≥1` with `p>8k−2`, set

`N_p(k)=((4k−1)p+1)/4`.

**THEOREM (PS-01):** `p U_(N_p(k)) ≡ U_k (mod p)` in the localization of rationals with denominators not divisible by `p`. The result is an exact, **source-specific prime stroboscope**, not a Weyl or real-circle equidistribution bound.

**COEFFICIENT DUALITY (PS-02):** with general pole coefficients `(A,B,C,D)` at offsets `(1,4,5,6)`, the remote shadow is the original coefficient vector when `p≡1 (mod 8)`, but when `p≡5 (mod 8)` it is `(-4C,B,-A/4,D)`. This pole-exchange map is an involution. Its fixed subspace requires `A=-4C`, satisfied by BBP's `A=4,C=-1`. Coefficients `B,D` remain free: this does NOT uniquely characterize π.

**PRIME CLOCK BIRTHS (PS-03):** first appearance of the new prime is at `(p+7)/8` for `p≡1 (mod 8)` and `(p+3)/8` for `p≡5 (mod 8)`. First later collision has `p U_((p+1)/2) ≡ 7/2` for both classes; after four pole encounters, `p U_((3p+1)/4) ≡ 47/15 = U_1`. In fact an entire base-16 multiplicative period in the p-fiber occurs before the first collision. No p-primary period claim is promoted to a real-circle mixing claim.

**REAL-PHASE FIREWALL (PS-04):** the congruence identifies the p-primary CRT phase of the remote rational selected state, *not its complementary CRT phase*. Complete p-fiber cancellation, even when provable, cannot force the complete real-circle Weyl sum to vanish without a cofactor correlation bound. Seeds integral at `p` are invisible to the p-primary invariant; an explicit numerator-zero example `p=73,k=4` shows that p-conductor can disappear.

**FINITE SELECTED ORBIT CERTIFICATE (PS-05):** the classical positive BBP tail bound `0<T_n<(8n+1)^{-2}` and exact rational `U_n` certify every one of the first **256** pure hexadecimal digit positions without floating-point input. Exact hexadecimal bin counts for `n=1..256` are `[17,18,18,15,14,12,16,18,19,24,13,13,14,16,13,16]`. These are finite facts, not an asymptotic normality proof.

## Exact execution

```sh
cd research/2026-10-30/prime_stroboscope
python -m unittest discover -s . -p 'test_*.py' -v
python independent_oracle.py
python selected_occupancy.py
python -m compileall -q prime_stroboscope.py selected_occupancy.py independent_oracle.py test_prime_stroboscope.py
```

The local run tested 15/15 unittest methods; the independently implemented oracle checked 138 coefficient-modular equivalences across 46 authentic prime/clock cases, 5 exact CRT decompositions, and a 410-dps independent π readout of 256 finite hexadecimal bins. All are finite receipts; the universal identities have separate paper proofs. No full SUCC root tests, hosted exact-head CI, or Lean kernel proofs have been run by this research branch. See [RESEARCH.md](RESEARCH.md), [CLAIMS.md](CLAIMS.md), [VALIDATION.md](VALIDATION.md), [NEXT.md](NEXT.md) and [CODEX_ASTRA_ULTRA_HANDOFF.md](CODEX_ASTRA_ULTRA_HANDOFF.md).
