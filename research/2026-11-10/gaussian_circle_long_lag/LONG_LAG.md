# The actual π near-return target, the two-clock geometry, and a source-selected obstruction

**Frozen source:** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`. The completed tail is `T_n=Σ_(j≥1)16^{-j}r(n+j)`, with `Y_n=U_n+T_n=16^{n-1}π`. All source arithmetic below uses the true four poles and a declared seed.

## LL-01: the positive near-return gate (PROVED CONDITIONAL / classical route)

Put `x_n={Y_n}`, `u_n={U_n}`, `d_T` circular distance, and for integer `q≥2`

```math
J_{A,q}^{x}=\frac{q}{A^2}\sum_{n,m=A}^{2A-1}
\left(1-q\,d_\mathbb T(x_n,x_m)\right)_+.
```

The normalized box window `g_q(t)=q·1_[0,1/q)(t)` satisfies the **exact** overlap formula `||μ_A*g_q||²_(L²)=J_(A,q)^x≥1`. If there is `q_A→∞`, with `q_A=o(A)` and `sup_A J_(A,q_A)^x<∞`, weak L² compactness gives an absolutely continuous limit of every subsequence of empirical orbit measures. Exact endpoint stationarity gives invariance under `T(x)=16x mod1`. The Fourier identity `fhat(h)=fhat(16^j h)` and the Riemann–Lebesgue lemma force every absolutely continuous invariant density to be Haar. Hence the original selected point `π/16` is base-16 normal. This is a sufficient theorem **whose source-specific hypothesis is OPEN**.

The existing weaker SUCC criterion `J_(A,q_A)=o(log q_A)` with `q_A→∞` and `log q_A=o(A)` also suffices: finite Fourier coercivity on the ray `h,16h,...,16^(L-1)h`, with `L≈log_16 q_A`, gives

```math
|c_A(h)|\le(\pi/2)\sqrt{(J_{A,q_A}-1)/L}+2L/A.
```

A bounded-energy growth schedule exists for a general normal base-16 orbit by a sufficiently slow diagonal choice, so existence of **some** such schedule is not a stronger arithmetic property than normality. The practical research target must specify a source-derived, controlled schedule (we use `q_A=floor(log2 A)` in the finite probes). Its estimate remains unproved.

## LL-02: the true two-index source sheet (PROVED exact)

Let `D_(n,k)=U_(n+k)-U_n`. Then

```math
D_{n+1,k}=16D_{n,k}+r(n+k+1)-r(n+1).
```

After the genuine Green completion, `E_(n,k)=D_(n,k)+T_(n+k)-T_n`, the forcing disappears **exactly**:

```math
E_{n+1,k}=16E_{n,k},\qquad
E_{n,k}=(16^k-1)16^n\pi/16.
```

Therefore

```math
J_{A,q}^{x}=\frac qA+
\frac{2q}{A^2}\sum_{k=1}^{A-1}\sum_{n=A}^{2A-k-1}
\left(1-q\left\|(16^k-1)16^{n-1}\pi\right\|\right)_+.
```

Every lag `k≤K` contributes at most `2qK/A`, since it has at most A ordered pairs and each kernel weight is ≤1. For `q_A≈log A` and `K≈log A`, that is `o(1)` even with no source estimate. The main unsolved **collision budget is long-lag**: most pairs are separated by more than logarithmic SUCC time. A bound on only the critical local scale `16^k≈A²` cannot directly pay the entire near-pair budget.

**Exact rational source transfer:** triangular kernel Lipschitz continuity and `0<T_n≤4/[15(n+1)²]` give

```math
|J_{A,q}^x-J_{A,q}^u|\le\frac{8q^2}{15(A+1)^2}.
```

Thus the actual no-π-oracle source target is `J_(A,q_A)^u=O(1)` at some predetermined growing `q_A=o(A)`, or the weaker `o(log q_A)`. These are **OPEN** for the literal zero seed.

## LL-03: a genuinely source-selective wrong-seed energy theorem (PROVED)

Choose **the same four-pole forcing** and the rational epoch-dependent seed `s_A=-P_L`, with `P_L=Σ_(j=1)^L16^{-j}r(j)` and `L≥2A`, then

```math
U_n(s_A)=-T_n^{(L)}<0,\quad
T_n^{(L)}=\sum_{j=n+1}^L16^{n-j}r(j)
\in\bigl(0,\frac4{15(A+1)^2}\bigr)
\quad(A\le n<2A).
```

All raw fractional points lie inside one circular arc of length at most `4/[15(A+1)²]`. If `q·4/[15(A+1)²]<1`, every ordered near-pair satisfies

```math
\boxed{q\left(1-\frac{4q}{15(A+1)^2}\right)
\le J_{A,q}^{u(s_A)}\le q.}
```

For `q_A=floor(log2 A)`, the shadow energy diverges as `q_A`, while the desired original-zero bound would remain O(1). Thus the proposed pinbed gate is **genuinely seed-discriminating**. This rational shadow need not retain the strong p-integrality properties of PPP-08, which remains a distinct required control.

## LL-04: three π-completion clocks and the finite/infinite mismatch (PROVED, classical inputs)

**Gauss disk clock.** For integer R let `N(R)=#(Z²∩{a²+b²≤R²})`; unit-square tiling gives

```math
|N(R)/R^2-\pi|\le\pi\left(\frac{\sqrt2}{R}+\frac1{2R^2}\right).
```

Rotation by `i` partitions every nonzero lattice point into a four-element orbit, so `N(R)≡1 (mod4)`. At radius `R=16^M`, `π_R=N(R)/R²` is a rational with **exact reduced denominator `16^(2M)`**, so its base-16 orbit is eventually zero (nonnormal) even though `π_R→π`.

For an epoch `[A,2A)`, `|{16^(n-1)π}-{16^(n-1)π_R}|_T≤16^(2A-2)|π-π_R|` for every n. Therefore the pair energy transport satisfies

```math
|J_{A,q}^{\pi}-J_{A,q}^{\pi_R}|\le
2q^2 16^{2A-2}\pi\left(\frac{\sqrt2}{R}+\frac1{2R^2}\right).
```

A sufficient **Gauss scalar-precision** radius for vanishing error at growing epoch is `R_A≫q_A²16^(2A)`; for `R_A=16^M`, `M_A≥2A+3log_16 q_A+ω(1)` is ample. The geometric angular sampler with `M_R≈A` instead needs `R≈√A` for bounded pointwise sampling multiplicity. These are **different clocks**. Their coexistence does not supply the missing map from BBP time to Gaussian angles.

**Viète polygon clock.** For regular inscribed and circumscribed N-gons in the unit circle,

```math
N\sin(\pi/N)<\pi<N\tan(\pi/N),\qquad N=4\cdot2^m,
```

and the interval width obeys

```math
0<N(\tan(\pi/N)-\sin(\pi/N))
\le\frac{\pi^3}{\sqrt2 N^2}.
```

The initial `N=4` inscribed ratio is `2sqrt(2)`, **not sqrt(2)**; the individual chord is sqrt(2). Half-angle recursion gives the classical Viète nested-radical product `2/π=∏_(j≥1) cos(π/2^(j+1))`. The exact rational interval probe constructs these without numerical π, and its output intersects both Gaussian disk and source BBP rational enclosures at every tested stage.

**BBP clock.** Finite `P_L` from the authentic original four poles gives `0<π-16P_L<64/[15(L+1)²16^L]`. This is exponentially faster in L than the polygon's `O(4^-m)` in its half-angle depth m. The three paths share an exact Archimedean limit, but **only BBP** has the source-attested causal relation to the selected hexadecimal orbit. Their scalar completions do not make their statistical limits interchangeable.

## LL-05: the missing map, in one quantified statement

The candidate next theorem is **GC-06 in THEOREMS.md**: derive a map from each real BBP time index to a Gaussian integer whose angular phase tracks the true completed orbit within `c/q_A`, and whose sampling multiplicities are comparable with `A/M_R`. With `R_A≈√A` and `q_A≈log A`, that would pull back GC-01's exact one-sided angular occupancy to the original source and prove normality. Neither natural projection from the source integrand nor a map created by sorting already-computed π phases qualifies as an independently established source mechanism.

A weaker alternative is an all-epoch count directly from the two-index source sheet:

```math
\#\{(n,m)\in[A,2A)^2: d_T(u_n,u_m)<1/q_A\}
\le C A^2/q_A.
```

This is still **OPEN**. The Gaussian lattice bound is a proved *model of the desired mechanism*, not a proof for π.