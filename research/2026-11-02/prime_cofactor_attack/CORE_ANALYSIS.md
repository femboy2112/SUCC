# Selected Prime–Cofactor Non-Conspiracy Conjecture — core structural analysis

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (off `origin/main` `81045770`).
**Agent:** Ravel (main thread). **Status:** exact structural reductions + corrected finite diagnostics; no normality claim.

## 1. The exact identity that dissolves the "conspiracy" language

The conjecture factorizes the authentic phase as "prime clock × cofactor":

$$
e(hU_n)=e\left(-\frac{h\,16^{n-a_p}}p\right)\,e(hV_{p,n}),\qquad a_p\le n<b_p.
$$

This factorization is **exact** (SPP-01), but it is not a *product of independent factors*. The tower identity

$$
U_n=16^{n-a_p}U_{a_p}+\sum_{j=a_p+1}^{n}16^{n-j}r(j)=16^{n-a_p}U_{a_p}+W_{p,n}
\tag{T-1}
$$

shows that the two factors share the **same** multiplier 16, and their product collapses back to a single term:

$$
e\left(-\frac{h\,16^{n-a_p}}p\right)e(hV_{p,n})=e(hU_n)
=e\big(h\,16^{n-a_p}U_{a_p}\big)\,e(hW_{p,n}).
\tag{T-2}
$$

Consequently

$$
\boxed{R_p(h)=\sum_{n=a_p}^{b_p}e(hU_n)=S_{b_p}(h)-S_{a_p-1}(h),}
\qquad
S_N(h)=\sum_{n=1}^{N}e(hU_n).
\tag{T-3}
$$

**`R_p(h)` is exactly a suffix (a prime-window block) of the authentic Weyl sum.** The "non-conspiracy conjecture" is therefore not a new object: it is a *large-sieve-over-prime-windows* second-moment bound on the original Weyl sum `S_N(h)`. Proving it is exactly as hard as the Weyl cancellation `S_N(h)=o(N)`, because each `R_p` is literally a block of `S_N`. The factorization `e(clock)e(cofactor)` is a restatement of `e(hU_n)=e(hU_n)`.

**Status: PROVED (exact, elementary).** This sharpens SPP-08: not only is the suffix equivalent to the global sum, but the "cofactor" carries no independent content — it is the tower identity in disguise.

## 2. The cofactor is not simpler than the orbit (PROVED)

`W_{p,n}=\sum_{j=a_p+1}^n 16^{n-j}r(j)` is the *same kind* of 16-geometric sum of the forcing as `U_{a_p}` itself. There is no decoupling: the "new forcing after the prime birth" is not an independent noise source; it is more of the identical four-pole forcing, and its denominator grows with the same `exp(6n+o(n))` conductor (CG-1). Hence no source-derived bound on `e(hW_{p,n})` is available that is not already a bound on `e(hU_n)`.

**Status: PROVED (structural; reduces the cofactor to the orbit).**

## 3. Window structure and overlap (PROVED)

For `p≡5 mod 8`: birth `a_p=(p+3)/8`, window end `b_p=(p+1)/2-1`, so window length

$$
|W_p|=b_p-a_p+1=\frac{3p+1}{8}\sim\frac{3p}{8}.
$$

The clock period `ord_p(16)` is typically `(p-1)/4` but varies (down to `(p-1)/36`, e.g. `p=397`). Since `|W_p|\approx\frac38(p-1) > ord_p(16)\approx\frac14(p-1)` typically, the window covers ≈1.5 clock periods on average.

Crucially, the windows **overlap heavily**: a single time `n` lies in `\{p: 2n+1\le p\le 8n-3,\ p\equiv5\ (8)\}` windows, of cardinality `\sim n/\log n` (e.g. 177 at `n=1000`). Therefore `\sum_p|R_p|^2` is a **redundant** decomposition of the Weyl sum, not a disjoint one.

**Quantitative consequence.** Trivial bound: `\sum_p |R_p|^2\le\sum_p|W_p|^2\sim\frac{3}{64}\frac{X^3}{\log X}`. The diagonal (single-time) contribution is `\sum_p|W_p|\sim\frac{3}{8}\frac{X^2}{\log X}`. The conjecture asks for a `(\log X)^{-\eta_h}` saving over the trivial `\sum_p|W_p|^2`. This saving is exactly the off-diagonal signed cancellation `\sum_{n\ne m}e(h(U_n-U_m))` — the same signed two-time correlation the entire program targets. **The conjecture is a faithful, non-trivial reformulation of the single bottleneck.**

## 4. Corrected finite diagnostics (OBSERVED FINITE)

**Precision firewalls — a concrete false-refutation caught and corrected.**

An initial computation with `mp.dps=200` (insufficient for `16^{X/2}` at `X=8000`) produced a *false* coherence result `M/T\to 1`, which would have "refuted" the conjecture. This was a **truncation artifact**, exactly the failure the handoff forbids. With correct precision (`mp.dps\ge 0.6X`, or exact `Fraction` with `mp.dps\ge800`):

| method | X | `M/T = Σ_p|R_p|²/Σ_p|W_p|²` |
|---|---|---|
| exact Fraction, dps=800 | 200 | 0.026 |
| exact Fraction, dps=800 | 500 | 0.010 |
| digit-orbit, dps=900 | 1000 | 0.0037 |

`M/T` is **small and decreasing** — consistent with genuine signed cancellation and with the conjecture's direction. (This is *consistent with* normality; it is finite, and far too small a range to distinguish `(\log X)^{-\eta}` from any mild decay. It is **not** a proof.)

The raw Weyl sum, correctly computed (dps=5200), shows `|S_N(1)|/N` decaying `0.045\to0.010` for `N=500\to4000`, `|S_N|/\sqrt N=O(1)` — the expected equidistribution signature.

**Status: OBSERVED FINITE. Corrected. Consistent with the conjecture; no proof.**

## 5. Honest status of the conjecture

- **The conjecture is exact, well-posed, and equivalent-in-difficulty to the Weyl cancellation** (it reorganizes `S_N(h)` into prime-window blocks; it does not supply a new handle).
- **No route to prove it is currently available**: BGK-type subgroup bounds do not apply (the window is a consecutive-exponent set, not a subgroup; the cofactor twist is source-dependent, not independent noise); the conductor `exp(6n)` forbids the Stoneham-style polynomial-period mechanism (Front F, prior round); the Galois trace annihilates (SPP-03).
- **The finite data is consistent with the conjecture but proves nothing.**

The single remaining lemma, in sharpest form, is unchanged:

> **(RL)** `\sup_{1\le|h|\le 16^{m-1}} |S_N(h)| = O(N^\theta)` for some `\theta<1`, `m=\lfloor\log_{16}N/3\rfloor` — equivalently `\Sigma_{n\le N}e(h\cdot16^{n-1}\pi)=o(N)`.

π normality and RH remain OPEN.
