# Source-selected logarithmic packets in the **completed** Weil formula

**Scope/authority:** Classical Guinand–Weil explicit formula (Bombieri, §5) specialized to a finite BBP-labelled packet. This is a paper derivation and calibrated finite arithmetic probe, *not a proof of RH or π normality*. Treat the global exact zero sum and the conditional RH-positive expression as separate claims. All indices here start at `n=1`, with SUCC's **original zero-seed** `Y_n=16^(n−1)π` and `a_h(n)=exp(2πihY_n)`.

## W1. Packet, admissible test class, exact Mellin transform

Choose a nonzero **real, even** `φ∈C_c^∞((-ε,ε))`, with `ε>0`, and finite nonempty `I⊂N_{≥1}`. Let `b_h(n)=a_h(n)/n`, and set

```math
g_{I,h}(u)=\sum_{n\in I} b_h(n)\phi(u-\log n),
\quad\widetilde g_{I,h}(u)=\overline{g_{I,h}(-u)},
\quad K_{I,h}=g_{I,h}*\widetilde g_{I,h},
\quad f_{I,h}(x)=x^{-1/2}K_{I,h}(\log x).
```

`f` is smooth and compactly supported on `(0,∞)`, so it is an admissible Weil test function. Write `κ=φ*φ̃`, `κ(0)=||φ||²>0`, `supp κ⊂[-2ε,2ε]`. Its log kernel is exactly

```math
K(t)=\sum_{n,m\in I} b_h(n)\overline{b_h(m)}\,\kappa(t-\log(n/m)).
```

With Mellin transform `f̃(s)=∫_0^∞ f(x)x^s dx/x`, 

```math
\widetilde f(1/2+i\gamma)
=|\widehat\phi(\gamma)|^2
\left|\sum_{n\in I}a_h(n)n^{-1+i\gamma}\right|^2,
\qquad \widehat\phi(\gamma)=\int\phi(u)e^{i\gamma u}\,du.
```

The equality is *only an identity of functions* on the critical line; interpreting each zeta-zero contribution as nonnegative requires RH. `D_(I,h)(1−iγ)=Σ_(n∈I) a_h(n)n^(−1+iγ)` is a **finite** Dirichlet polynomial, not the analytically continued infinite `D_h`. No zero ordinate is a construction input.

## W2. Correct complete Guinand–Weil balance, no missing Γ term

Adopt Bombieri's normalization, with `f^♯(x)=x^(−1)f(1/x)` and `Λ(p^k)=log p`, zero otherwise. The explicit formula for the admissible `f=f_(I,h)` is

```math
\boxed{\widetilde f(0)-\sum_\rho\widetilde f(\rho)+\widetilde f(1)
=\underbrace{\sum_{q\ge2}\Lambda(q)[f(q)+f^\sharp(q)]}_{P(f)}
+\underbrace{(\log(4\pi)+\gamma_E)f(1)
+\int_1^\infty\frac{f(x)+f^\sharp(x)-2f(1)/x}{x-x^{-1}}\,dx}_{W_{\infty}(f)}.}
```

The nontrivial-zero sum has its *standard symmetric limit*. This is **the completed** formula: it includes the polar `f̃(0)+f̃(1)`, every prime power, and the Archimedean Γ/pole expression `W_∞`. No RH assumption is used to state the equality. Under RH, with zeros `ρ=1/2+iγ` counted with multiplicity,

```math
\boxed{\sum_{\gamma}|\widehat\phi(\gamma)|^2
\left|D_{I,h}(1-i\gamma)\right|^2
=\widetilde f(0)+\widetilde f(1)-P(f)-W_\infty(f)\ge0.}
```

The ≥0 is Weil positivity conditional on RH. It says nothing directly about the unsampled frequency `γ=0`, about `D_h(s)`'s singularities on `Re s=1`, or about `A F_h(A)→0`.

## W3. An exact arithmetic prime-power *edge* formula

The prime-power term has no ambiguity:

```math
P(f)=\sum_{q=p^k}\frac{\log p}{\sqrt q}
[K(\log q)+K(-\log q)].
```

For each **finite** `I`, choose `ε` so small that for every prime power `q` within the compact ratio-support range, `|log(n/m)−log q|>2ε` whenever `n≠qm`. (Such an epsilon exists because the possible ratios and relevant prime powers are finite.) Then

```math
\boxed{P(f)=2\|\phi\|_2^2
\sum_{q=p^k}\frac{\log p}{\sqrt q}
\operatorname{Re}\sum_{\substack{m,qm\in I}}
\frac{a_h(qm)\overline{a_h(m)}}{q m^2}.}
\tag{W-EDGE}
```

This is an **exact source-selected** signed prime-power graph observable. Its edges are multiplicative `m→p^k m`; its phase data originate from the additive-index radix orbit. The phase on a directed edge is, without quotienting out integer winding,

```math
\frac{a_h(pm)}{a_h(m)}
=\exp\{2\pi i h\,[16^{(p-1)m}-1]Y_m\}.
```

It makes source/seed dependence explicit. Taking `a_h≡1` (coherent wrong seed) makes all such edges real-positive, but does *not* change zeta or its putative RH truth.

## W4. Exact support no-go and its repair by 2/3/6 expansion

Set `I=[A,2A)∩Z`, `A≥2`. Then `n/m<2` and `m/n<2` for all `n,m∈I`. If

```math
2\epsilon<\log\frac{2A}{2A-1},
```

then `supp K⊂(-log 2,log 2)`, because the maximal positive `log(n/m)` is `log((2A−1)/A)`. Consequently `K(±log q)=0` for every prime power `q≥2`, **hence `P(f)=0` identically for every phase/seed**. This is a *finite-support geometric theorem*, not a claim that completed RH supplies no information through the zero/Γ side.

In general, a full SUCC/FUCC `2×3` multiplicative diamond has nodes `{m,2m,3m,6m}`. Any index interval supporting all four must have multiplicative span at least `6`. For this four-node packet, if `ε=1/100` (or any sufficiently small ε), the exact primitive edges are:

```text
    m  ----(×2)----> 2m
    |                 |
   (×3)             (×3)
    |                 |
    v                 v
   3m  ----(×2)----> 6m
```

**There is no direct `m→6m` von Mangoldt edge**, since `Λ(6)=0`. Formula (W-EDGE) becomes

```math
\frac{P(f)}{2\|\phi\|_2^2}
=\frac{\log2}{\sqrt2}\Re[b_{2m}\bar b_m+b_{6m}\bar b_{3m}]
+\frac{\log3}{\sqrt3}\Re[b_{3m}\bar b_m+b_{6m}\bar b_{2m}].
\tag{2-3-DIAMOND}
```

For the coherent wrong seed, the two bracketed sums are `5/(9m²)` and `5/(12m²)` respectively; a phase flip on the `2m,6m` fiber reverses the first bracket but leaves the second positive. These tests show why the relative phase and the complete CRT complement cannot be erased.

**Pure-gauge control:** set `u_n=a_h(n)` (unit modulus) and edge transports `U_(v,u)=u_v conj(u_u)`. The Wilson product around `m→2m→6m→3m→m` is exactly `1`, for *all* seeds, because the vertex phases telescope. Any claimed **nontrivial closed-loop Berry/Weil phase** from these scalar edge labels alone is therefore **REFUTED**. Oriented edge projections can still distinguish seeds; extra noncommuting transport would have to be supplied and justified.

## W5. Signed Basel as *vacuum overlap*, not Weil positivity

For the same `I`, also define `g_(I,0)(u)=Σ_(n∈I)n^(−1)φ(u−log n)`. Choose epsilon small enough that translated bumps at distinct `n∈I` have disjoint supports. With inner product linear in the first argument,

```math
\boxed{\langle g_{I,h},g_{I,0}\rangle
=\|\phi\|_2^2\sum_{n\in I}\frac{a_h(n)}{n^2}.}
\tag{BASEL-VACUUM-OVERLAP}
```

Both vectors have the **same** L² norm squared `||φ||² Σ_(n∈I)n^(−2)`; no cancellation follows from Cauchy–Schwarz. Under the coherent wrong seed they are equal, so the signed overlap reaches its maximal value. The Weil form in W2 is not the same as the ordinary L² overlap, and Weil positivity alone does not give an asymptotically vanishing off-diagonal overlap.

The existing Basel–Tauberian theorem in #585 makes the required asymptotic explicit: `A F_h(A;0)→0` for all nonzero h would prove base-16 normality. W1–W5 **construct a genuine completed-source pairing** but furnish no estimate implying this limit.

## W6. Precise next theorem

For original-zero `a_h`, and moving windows that contain `×2` and `×3` cross-octave edges, prove a **non-circular, uniform in A** inequality transporting completed prime-power plus Γ/pole information to `|⟨g_(I,h),g_(I,0)⟩|=o(1/A)`, with correct tail/carry controls and without assuming the desired conclusion in the test function. Countermodel must include the coherent seed `s=−π/16`, all-zero/periodic radix streams, and the PPP-08 p-integral shadow. If only one dyadic octave is sampled, the direct prime term is zero and an independent Archimedean/zero-side mechanism is required.

### Provenance/reference

Bombieri, *The Riemann Hypothesis* (Clay Mathematics Institute), §5, explicit formula (PDF p. 8), https://www.math.ucdavis.edu/~tracy/courses/math205A/riemann.pdf ; Bombieri (2000), *Remarks on Weil's quadratic functional*, §2, https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0 . Exact SUCC source: Main XXIII candidate PR #584 and the original four-pole `R(j)`; signed Basel criterion: PR #585.
