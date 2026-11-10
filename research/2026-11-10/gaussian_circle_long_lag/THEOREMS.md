# Theorems: Gaussian angular pinbeds, primitive directions and viable source transport

All geometric proofs below are classical elementary arguments organized for the SUCC long-lag program. The finite BBP source is never silently substituted by a new source.

## GC-01: all-scale angular sector occupancy and bounded triangular energy (PROVED)

For real `R≥4` (for the program we use integer R) let

`Λ_R={z=a+ib∈Z[i]: 0<|z|≤R}`, `M_R=#Λ_R`,
`θ_z=arg(z)/(2π)∈T=R/Z`, and `ν_R=M_R^{-1} Σ_(z∈Λ_R) δ_(θ_z)`.

The standard unit-square tiling with square radius `c=√2/2<1` gives

```math
\pi(R-1)^2-1\le M_R\le\pi(R+1)^2-1.
```

**Angular theorem.** For any integer `2≤q≤R` and any half-open circular arc `I` of normalized length `1/q`,

```math
\boxed{\nu_R(I)\le\frac{6+4/\pi}{q}<\frac8q.}\tag{GC1}
```

*Proof.* The (closed) disk sector `W` of radius R and angular width `2π/q≤π` is convex, area `πR²/q`, perimeter `(2+2π/q)R≤(2+π)R`. Every integer center in W has a unit square wholly contained in the radius-1 parallel body `W+B_1`, and these unit squares have disjoint interiors. Steiner's formula for the convex sector gives

```math
\#(\Lambda_R\cap W)\le |W+B_1|
=\frac{\pi R^2}{q}+(2+2\pi/q)R+\pi
\le\frac{(3\pi+2)R^2}{q},
```

where `q≤R` pays both lower-order terms. On the other hand, `M_R≥π(R-1)^2-1≥(π/2)R²` for `R≥4`. Divide. Open/half-open arc counting is bounded by closed sectors, so endpoints cause no difficulty. □

For integer `2≤q≤R`, define

```math
J_{R,q}^{\mathrm{Gauss}}=
\frac{q}{M_R^2}\sum_{z,w\in\Lambda_R}
\bigl(1-q\,d_\mathbb{T}(\theta_z,\theta_w)\bigr)_+.
```

**Corollary.** `1≤J_{R,q}^{Gauss}≤16` uniformly over all R≥4 and all `2≤q≤R`.

*Proof.* For each z, the angular ball `d_T(θ_z,θ_w)<1/q` is an arc of total length `2/q`, coverable by two arcs of length `1/q`. GC1 bounds at most `16M_R/q` neighbors. Each triangular weight is at most one; summing over z and multiplying by `q/M_R²` gives 16. The general normalized overlap/kernel identity gives the lower bound 1. □

This is **the full Gaussian angle sample**. Nothing above proves the analogous bound for the selected BBP orbit.

## GC-02: exactly surviving angular characters and an effective fixed-mode estimate (PROVED)

For `h∈Z\{0}`, write `C_R(h)=M_R^{-1}Σ_{z∈Λ_R}(z/|z|)^h`. Rotation by `i` permutes Λ_R and multiplies every term by `i^h`, so `C_R(h)=0` exactly if `h≢0 (mod4)`.

For all `R≥4`, an elementary proof using the same unit squares gives

```math
\boxed{ |C_R(h)|\le
\frac{6\pi|h|(R+1)+4\pi R+18}{\pi(R-1)^2-1}
=O\bigl((|h|+1)/R\bigr).}\tag{GC2}
```

*Proof.* Define `F_h(z)=(z/|z|)^h` for z≠0 and `F_h(0)=0`. The integral of F_h over the disk D_R is zero for nonzero h by polar integration. Let U_R be the union of unit squares centered at the lattice points of the disk. The symmetric difference `U_R Δ D_R` lies inside the annulus `R-1≤|z|≤R+1`, of area `4πR`. For center `p` with `|p|≥2`, the gradient estimate `|∇F_h(z)|≤|h|/|z|` yields `|F_h(p)-F_h(x)|≤2|h|/|p|` for x in its square. Moreover `1/|p|≤(3/2)∫_{Q_p}|z|^{-1} dz` because `|p|≥2` and `|z|≤|p|+1`. Integrating over disjoint squares inside `D_{R+1}` yields `Σ_{|p|≥2}|p|^{-1}≤3π(R+1)`. At most nine remaining center squares contribute at most 2 each. Summing the three errors and dividing by `M_R≥π(R-1)²-1` proves GC2. □

**Parity firewall:** hexadecimal parity's real Fourier support is `h≡8 (mod16)`. Every such h is divisible by four. Therefore **the exact quarter-turn symmetry alone kills none of the parity-supported frequencies**. Actual angular cancellation needs more than the lattice's discrete C4 symmetry; the geometric sector theorem supplies it for complete disk sampling, not for the original π chronology.

For even h divisible by four, `Re((a+ib)^h)/(a²+b²)^(h/2)` is an exact rational number; the finite script checks these coefficients with `Fraction` arithmetic, not floating trigonometry.

## GC-03: primitive Gaussian directions via Möbius inversion (CLASSICAL, derivation given)

Let `Λ_R^prim={a+ib∈Λ_R:gcd(|a|,|b|)=1}` and let `μ(d)` be the Möbius function. For a disk sector W_R(I), primitive points are exactly

```math
M_R^{prim}(I)=\sum_{1\le d\le R}\mu(d)\,M_{R/d}^{all}(I),
```

where `M_{R/d}^{all}(I)` counts nonzero lattice points in the scaled sector. The square-tiling proof gives `M_t^{all}(I)=(π t²)|I|+O(t+1)` uniformly for arcs of normalized length `|I|≤1/2` (and the remaining arcs by finite partition). Hence

```math
M_R^{prim}(I)=\frac{\pi R^2}{\zeta(2)}|I|+O(R\log R),
\qquad M_R^{prim}=\frac{\pi R^2}{\zeta(2)}+O(R\log R).
```

The `O` constants are uniform in the location/width of the arc. It follows that

```math
\nu_R^{prim}(I)=|I|+O\left(\frac{\log R}{R}\right).
```

For `q_R→∞` with `q_R log R/R=O(1)`, primitive angular occupancy is `O(1/q_R)` and primitive angular triangular energy is `O(1)`. This proves a **genuinely coprime arithmetic angular sample**, but it is still not the source-selected π sample.

The independent direct-gcd and Möbius formulas were checked on Gaussian disks R=4,8,16,24,32,48 and the sector `0≤arg z≤π/4`. These are finite controls, not substitutes for the proof above.

## GC-06: conditional source-to-Gaussian pinbed pullback (PROVED CONDITIONAL)

Let `A≥1`, `q≥2`, `R≥q`, and `x_n∈T` for `n∈[A,2A)`. Suppose there is a map `φ_A:n↦z_n∈Λ_R` with constants c≥0 and B>0 independent of A, satisfying:

1. **Phase alignment:** `d_T(x_n, θ_(z_n))≤c/q` for every n.
2. **Controlled multiplicity:** `#φ_A^{-1}(z)≤B A/M_R` for every z∈Λ_R (so a nonempty map forces `M_R≤B A`).

Set `r_c=ceil(2+4c)`. Then

```math
\boxed{J_{A,q}(x)\le 8B\,r_c.}\tag{GC6}
```

*Proof.* If `d_T(x_n,x_m)<1/q`, the triangle inequality gives `d_T(θ_(z_n),θ_(z_m))<(1+2c)/q`. That circular arc has total normalized length `2(1+2c)/q`, and can be covered by at most `r_c` arcs of length `1/q`. By GC1 each arc contains fewer than `8M_R/q` lattice points, and the multiplicity hypothesis turns this into at most `8B A/q` source indices per arc. Thus at most `8B r_c A/q` indices m can contribute to the triangular energy of each n. Summing with weight ≤1 proves GC6. □

**If** `x_n={U_n+T_n}` are the actual original-zero π orbit, `q_A→∞`, and a family of such maps exists with uniform c,B and `q_A≤R_A`, then the established SUCC bounded-pinbed criterion forces base-16 normality. A source-derived proof of such maps is **UNVERIFIED**. A map reverse-engineered by sorting observed π phases would not independently establish the hypothesis.

**One-radius obstruction (precise scope).** A bounded multiplicity constant B and A indexed points imply `M_R≤BA`, hence `R=O(√A)`. The *same* Gaussian circle radius would need to be exponentially larger to approximate the π phase accurately over `[A,2A)` using only the disk-count error. These two demands cannot be met simultaneously by the naive single-radius construction; they can be represented as separate clocks, but then an independent source-to-angle transport map is still required. This is an obstruction to that **specific** proof architecture, not to normality or to every possible geometric approach.


## GC-08: χ₋₄, Gaussian factorization and the exact lattice-count ledger (CLASSICAL)

The two-squares representation function obeys Jacobi's divisor identity

```math
r_2(m)=\#\{(a,b)\in\mathbb Z^2:a^2+b^2=m\}
=4\sum_{d\mid m}\chi_{-4}(d).
```

Here `χ₋₄(d)=0` for even d, +1 for `d≡1 (mod4)`, and −1 for `d≡3 (mod4)`. Consequently, at every positive integer radius R,

```math
\boxed{N(R)=1+4\sum_{d=1}^{R^2}\chi_{-4}(d)
\left\lfloor\frac{R^2}{d}\right\rfloor.}\tag{GC8}
```

This is an exact **finite grid-to-arithmetic** bridge, and the Dirichlet-series generating function is `4 ζ(s)L(s,χ₋₄)` for `Re s>1`. The value `L(1,χ₋₄)=π/4` is the classical Leibniz series. These identities require Gaussian factorization/arithmetic input; the area limit alone does not automatically derive the Leibniz series. This χ₋₄ arithmetic does not supply signed cancellation of the original BBP orbit.

The pure integer divisor-sum oracle and independent disk lattice count agree for eight radii `R=1,2,3,4,8,16,24,32`.