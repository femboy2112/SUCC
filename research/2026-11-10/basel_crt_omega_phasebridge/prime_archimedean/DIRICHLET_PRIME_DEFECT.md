# Möbius–prime-jet transport and a **certified original-π 2×3 defect**

**Objects.** Let `e(x)=exp(2πix)`, integer mode `h≠0`, and seed `u∈R`. Keep SUCC's literal four-pole source and original-zero completion:

```math
R(j)=\frac4{8j+1}-\frac2{8j+4}-\frac1{8j+5}-\frac1{8j+6},
\quad P_\infty=\sum_{j\ge0}16^{-j-1}R(j)=\pi/16,
\quad Y_n(u)=16^n(u+P_\infty),
\quad a_n(h;u)=e(hY_n(u)).
```

Every claim below is for this fixed source, except algebraic identities explicitly quantified over an arbitrary bounded arithmetic sequence `a`. All Dirichlet series are initially used only for `Re z>1`. Do not confuse the complex variable `z` with a BBP seed.

## D1. Exact Dirichlet–Möbius deconvolution (classical algebra, source-selected coefficients)

For **any** bounded complex arithmetic sequence `a(n)` define `b=μ*a`, the Dirichlet convolution with the Möbius function. Then

```math
\boxed{\mathcal D_a(z)=\sum_{n\ge1}\frac{a(n)}{n^z}
=\zeta(z)\mathcal B_a(z),\qquad
\mathcal B_a(z)=\sum_{n\ge1}\frac{b(n)}{n^z},\quad
b(n)=\sum_{d\mid n}\mu(d)a(n/d).}
```

Both series converge absolutely for `Re z>1`: `|b(n)|≤τ(n)` and `Στ(n)n^(-σ)=ζ(σ)^2`. In particular,

```math
b(1)=a(1),\quad b(2)=a(2)-a(1),\quad b(3)=a(3)-a(1),
\quad\boxed{b(6)=a(6)-a(3)-a(2)+a(1).}
```

**This is not SUCC's Dirichlet logarithm `log_* a`**. Even when `a(1)=1`, the connected logarithmic coefficient at 6 is `a(6)-a(2)a(3)`, generally different from `b(6)` above. The former tests multiplicativity; the latter is an exact **mixed 2×3 finite difference** of the dilation graph. For the coherent wrong seed `u=−π/16`, all `a(n)=1`, so `b=δ_1` and `D_a=ζ`.

## D2. Exact prime-jet derivative and analytic transport

Let `Λ(n)=log p` on prime powers `n=p^k` and 0 otherwise. For an arbitrary bounded sequence `a`, define the arithmetic source defect

```math
\mathcal E_a(n)=\log n\,a(n)-(\Lambda*a)(n)
=\sum_{p^k\mid n}(\log p)\,[a(n)-a(n/p^k)].
```

This uses `log n=Σ_(d|n)Λ(d)`, with **every old prime power** included. It is an exact integer-coefficient identity, not an assumption of independence. At the first mixed node,

```math
\mathcal E_a(6)=\log2\,[a(6)-a(3)]
+\log3\,[a(6)-a(2)].
```

For `Re z>1` let `E_a(z)=Σ_n E_a(n)n^(−z)`. Product and differential rules for absolutely convergent Dirichlet series give

```math
\mathcal E_a(z)=-\mathcal D_a'(z)+\frac{\zeta'(z)}{\zeta(z)}\mathcal D_a(z)
=-\zeta(z)\left(\frac{\mathcal D_a(z)}{\zeta(z)}\right)'.
```

Equivalently `E_a(n)=Σ_(d|n)(log d)b(d)`, and

```math
\boxed{\left(\frac{\mathcal D_a}{\zeta}\right)'(z)
=-\frac{\mathcal E_a(z)}{\zeta(z)},\qquad
\frac{\mathcal D_a(z)}{\zeta(z)}
=a(1)+\int_0^\infty\frac{\mathcal E_a(z+t)}{\zeta(z+t)}dt,\quad \Re z>1.}
\tag{PRIME-JET-TRANSPORT}
```

The real-translation integral is absolutely convergent because `E/ζ=−B'` and the coefficients at `n≥2` decay like `n^(−Re z−t)log n`; integrate termwise. **No RH is needed** here: the denominator is nonzero in `Re z>1` by Euler's product. Analytic continuation across `Re z=1` of the genuinely BBP-selected `E_a/ζ` is **UNVERIFIED**. RH zero-free information alone does not bound the composite phase coefficients `b(n)` nor yield the missing continuation.

## D3. **A finite genuine-BBP theorem**, with rational proof and no π-digit oracle

**Theorem (h=1, u=0).** Set `a_n=e(16^(n−1)π)` for integer `n≥1`. Then the four source-derived oriented prime edges

```math
\Re(a_2\overline{a_1})>0,\qquad
\Re(a_6\overline{a_3})<0,
\qquad\Re(a_3\overline{a_1})>0,\qquad
\Re(a_6\overline{a_2})<0.
```

Moreover the Möbius–Dirichlet composite coefficient at 6 satisfies the **quantitative strict inequality**

```math
\boxed{\Im[(\mu*a)(6)]
=\Im[a_6-a_3-a_2+a_1]<1-\sqrt3<0.}
\tag{AUTHENTIC-6-DEFECT}
```

**Proof from the immutable four poles.** The source has the exact positive moment form

```math
R(j)=\int_0^1 x^{8j}(1-x)(x^2+2)(x^2+2x+2)\,dx.
```

For `0≤x<1`, the final product is between 0 and 15. Therefore

```math
0<P_\infty-P_L<\frac{16^{-L}}{(8L+1)(8L+2)}.
```

Fix `L=12`. The **rational number** `P_12=Σ_(j=0)^11 R(j)/16^(j+1)` gives the strict rational interval

```math
P_{12}<\pi/16<P_{12}+\eta_{12},\qquad
\eta_{12}=1/[16^{12}\cdot97\cdot98].
```

For any integer `n`, propagate this interval through multiplication by `16^n`; for differences use `(16^n−16^m)P_∞`. At each of the following observations the lower and upper rational bounds have the **same integer floor**, so reduction mod 1 is justified rather than silently assuming a carry:

| Certified fractional quantity | Strict rational subinterval |
|---|---|
| `{Y_1}` | `(1/8,1/6)` |
| `{Y_2}`, `{Y_3}` | `(1/6,1/3)` |
| `{Y_6}` | `(1/2,1)` |
| `{Y_2−Y_1}` | `(1/10,1/8)` |
| `{Y_6−Y_3}` | `(2/5,5/12)` |
| `{Y_3−Y_1}` | `(1/10,1/9)` |
| `{Y_6−Y_2}` | `(3/8,2/5)` |

All seven containments are verified **exactly using `Fraction` comparisons**, not by printing rounded decimals. Cosine is positive on `(0,1/4)` of a cycle and negative on `(1/4,1/2)`; this proves the four edge signs. Further, for each of `x={Y_2},{Y_3}∈(1/6,1/3)`, `sin(2πx)>√3/2`; for `{Y_6}∈(1/2,1)`, its sine is negative; and any sine is at most 1. Consequently

```math
\Im(a_6-a_3-a_2+a_1)<0-\sqrt3/2-\sqrt3/2+1=1-\sqrt3.
```

This proves AUTHENTIC-6-DEFECT without any cosine numerical evaluation, arbitrary-precision π value, or RH oracle. QED.

**Adversarial controls.** For the coherent wrong seed `u_*=−π/16`, all `a_n=1`, each edge cosine is +1 and `b(6)=0`. A finite common-horizon rational seed `u_L=−P_L` also gives zero completed *finite-horizon* phase, but is not the same mathematical seed and must not be treated as globally coherent. For any vertex phases (including authentic π), scalar Wilson products around the diamond equal 1, by telescoping. The source-selected mixed defect is **not** a holonomy and does not prove an asymptotic sign estimate.

## D4. What would bridge RH to original-zero normality?

The exact product `D_h=ζ B_h` does **not** mean that control of zeros of ζ controls `B_h`: the latter contains all nonmultiplicative, source-selected `μ*a_h` coefficients. Similarly, `PRIME-JET-TRANSPORT` is exact only in `Re z>1` and cannot be analytically continued by naming RH.

A real source-to-Weil transport theorem would have to control *the complete prime-power defect and the Γ/pole test-function contribution* in a common analytic setting that yields a source-specific `A F_h(A;0)→0` (at least odd-eight modes for parity). It must reject the coherent wrong seed (where `B_h≡1`) and PPP-08's rational p-integral same-source shadow. The newly **proven finite nonzero b_h(6)** is a discriminating source bit, not an all-epoch estimate.

**Claim classes:** algebraic identities **DISCLOSED within Re z>1**; BBP-based finite sign **DISCLOSED by exact rational interval plus elementary trigonometry**; finite executable controls **OBSERVED**; completed source-to-Weil continuation and zero-seed signed saving **UNVERIFIED / OPEN**. Novelty priority not asserted.
