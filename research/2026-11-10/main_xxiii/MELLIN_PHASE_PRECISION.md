# Exact phase precision from positive Mellin data

Let $`\mu`$ be a positive finite measure on $`[0,1]`$ with moments
$`m_j=\int t^j\,d\mu(t)`$ and mass $`M=m_0`$. For the authentic source,
push $`P(x)\,dx`$ forward by $`t=x^8`$, where
$`P(x)=4-2x^3-x^4-x^5`$. Its moments are the authentic zero-based
forcing values $`R(j)`$ and its completion is

```math
\Pi(\mu)=\int\frac{d\mu(t)}{1-t/16}=\pi.
```

The positive aliases agree on finitely many moments and can change
$`\Pi`$. The following rational interval bounds the amount they can change it.

## A rational polynomial certificate

Let $`T_d`$ be the Chebyshev polynomial defined by
$`T_0(y)=1`$, $`T_1(y)=y`$, and $`T_{d+1}(y)=2yT_d(y)-T_{d-1}(y)`$.
Given moments through degree $`N\ge0`$, set $`d=N+1`$ and

```math
D_d=T_d(31),\qquad
p_N(t)=\frac{1-T_d(2t-1)/D_d}{1-t/16}.
```

The numerator vanishes at $`t=16`$, so $`p_N`$ is a rational
polynomial of degree at most $`N`$. Its integral $`C_N=\int p_N\,d\mu`$
therefore uses only the given moments. The identity
$`T_d(\cos\theta)=\cos(d\theta)`$ gives $`|T_d(2t-1)|\le1`$ on
$`[0,1]`$. Since $`1-t/16\ge15/16`$ there, the exact residual yields

```math
\big|\Pi(\mu)-C_N\big|\le\frac{16M}{15D_d}.
```

This is an exact rational interval whenever the supplied moments are rational.
The recurrence $`D_0=1`$, $`D_1=31`$, $`D_{d+1}=62D_d-D_{d-1}`$
computes its denominator. Two positive measures matching the moments
$`m_0,\dots,m_N`$ have the same center and a completion difference of at
most $`32M/(15D_d)`$. Positivity matters because it supplies a bound on
total variation from the zeroth moment.

## Transfer to all positions in an epoch

Write $`\rho=31-\sqrt{960}`$. The recurrence gives
$`D_d=(\rho^{-d}+\rho^d)/2`$. For $`e(z)=\exp(2\pi i z)`$, the mean
value bound gives, uniformly for integer $`n\in[A,2A)`$ and fixed $`h`$,

```math
\left|e\big(h16^{n-1}\Pi(\mu)\big)-e\big(h16^{n-1}C_N\big)\right|
\le 2\pi|h|\,16^{2A-2}\frac{16M}{15D_{N+1}}.
```

Thus for any fixed $`\eta>0`$, taking
$`N\ge (2\log 16/\log(1/\rho)+\eta)A`$ gives uniform exponentially
small phase error. The coefficient of $`A`$ before $`\eta`$ is
approximately $`1.343675`$. This counts sampled moments. It makes no
runtime claim about computing the rational center or about the signed mean.

The center tracks the source completion. For an independently prescribed
seed $`s`$, the actual phase uses $`16^{n-1}\Pi(\mu)+16^n s`$, and
the seed term must be retained. With the authentic source and
$`s=-\pi/16`$, every completed phase is $`1`$ after exponentiation. The
precision estimate transports this hostile control just as accurately as the
zero-seed orbit.

**Status.** The finite-moment completion interval and epoch phase transport
are proved. The sign cancellation for the literal zero seed remains open.
