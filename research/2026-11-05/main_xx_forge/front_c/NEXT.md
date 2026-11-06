# Front C: the single most discriminating next inequality

**The target: a Poisson-scale pair budget for the selected orbit, resolved by lag.** Prove that for some fixed `s>0` and `C<∞`, for all large A:

```
Π_A(s) := A^{-1} · #{ n≠m ∈ [A,2A) : ||z_n - z_m|| < s/A }  ≤  C·s
```

Equivalently, for the actual orbit, since `x_{n+g}-x_n ≡ (16^g-1)x_n + S_g(n) (mod 1)`:

```
Σ_{1≤|g|<A} #{ n : ||(16^g-1)x_n + S_g(n)|| < s/A }  ≤  C·s·A   (up to the O(T_A) transfer).
```

**Why this one.**
1. By Lemma C3-2 (with δ=s/(2A), J≍log_16 A), it implies `|c_A(h)|² ≲ C/log A`. That is, it implies normality with a rate. By C3-1 and C3-2 a bounded budget at a single shrinking scale is also necessary, so this is an **equivalence-class target**: exactly as hard as normality, with no hidden extra debt. The PF7/Fekete energy and every all-scale budget are strictly stronger.
2. It sits exactly at the crossover that #501 identified, between the microscopic regime (GPB-2: true for every seed, including COH) and the mesoscopic regime (equivalent to normality). It is the first scale at which the source must matter.
3. It is lag-resolved. The source enters **only** through the radial shifts `S_g(n)=16^gT_n-T_{n+g}` (C1-1, C2-1). Small lags (`16^g ≲ A/s`) are a union of `16^g-1` shrinking targets controlled by Weyl sums at the frequencies `k(16^g-1)`, which are Weyl again. Large lags are long-range block coincidences. Every prime-Frobenius, carry or mixed label reduces to these (C1, C2), so nothing else is left to add.
4. **Every control fails or passes it for a stated reason:**
   - COH fails: `Π=A-1`.
   - PER_SHORT fails: `Π≥A/61-1`.
   - FIFTEEN fails, but only like `(A/s)^{0.023}`, which no finite receipt can show.
   - Haar-random passes with `Π→2s`.
   - PER_LONG and ROT are identical to TRUE.
   - Observed TRUE at s=1: `Π/2s` = 1.055, 0.955, 1.008, 0.968, 0.995 (A=256…4096).

**Falsification protocol.**
- A proof must use `α=π/16` beyond its Baker coordinates. Per CM-11, an argument that also applies to `Σ16^{-k!}` is void.
- It must fail for COH and for every PER_SHORT.
- It must not be phrased as a statement about seed-ensemble averages: HS-12's evaluation barrier `√A` applies.

**Honest stop.** This is not a new easier problem. It is the cleanest equivalent form of the open gate. Any claimed proof should first be tested on a nonnormal orbit of entropy dimension `κ<1`, because the discriminating signal there is only a power `δ^{κ-1}` of the scale.
