# Target B — Finite-frequency inequality: PROOF and correct form

## What I established exactly

**(ID)**  $W_N(h) = \frac1K\sum_{k=1}^K W_N(hk) + \frac1N\sum_{n}\big[e(hU_n) - g_K(hU_n)\big]$, verified to machine precision.

**(Telescope)**  $|W_N(hk)-W_N(h)| \le \Omega(k)\,\Delta_N(|h|K)$ for $k\le K$, since $|hk|\le|h|K$ and any integer is a product of $\Omega(k)$ primes.

**(Geometric bound)**  $|g_K(x)| \le \min\!\big(1, \tfrac{1}{2K\|x\|}\big)$, verified exactly (worst ratio 1.0).

## The correct derivation

From (ID):
$$|W_N(h)| \le \Big|\frac1K\sum_{k=1}^K W_N(hk)\Big| + \Big|\frac1N\sum_n\big[e(hU_n)-g_K(hU_n)\big]\Big|.$$

First term via telescope:
$$\Big|\frac1K\sum_k W_N(hk)\Big| \le |W_N(h)| + \frac1K\sum_k \Omega(k)\Delta_N(|h|K) \le |W_N(h)| + \lfloor\log_2 K\rfloor \Delta_N(|h|K),$$
using $\Omega(k)\le\log_2 k\le\log_2 K$.

Second term: set $x_n=hU_n$. Split $n$ into near ($\|x_n\|<\eta$) and far ($\|x_n\|\ge\eta$).
- near: $|e(x_n)-g_K(x_n)|\le 2$, contributing at most $2\,\widehat C_N^h(\eta)$ where $\widehat C_N^h(\eta)=\frac1N\#\{\|hU_n\|<\eta\}$.
- far: $|e(x_n)-g_K(x_n)|\le |e(x_n)|+|g_K(x_n)|\le 1+\frac{1}{2K\eta}$.

So
$$|W_N(h)|\le |W_N(h)| + \lfloor\log_2K\rfloor\Delta_N + 2\widehat C_N^h(\eta) + (1-\widehat C_N^h(\eta))\Big(1+\tfrac{1}{2K\eta}\Big).$$

**This is degenerate** (has $|W_N(h)|$ on both sides and a $(1-\widehat C)$ term that doesn't vanish). The clean statement must instead bound the *defect*, and the claimed inequality's form (coefficient 1 on $C$, bare $1/(2K\eta)$) is **not** what this derivation yields.

## The honest resolution

The correct, provable, useful statements are the two *ingredients*, not the combined inequality as literally written:

**(B1)** $|W_N(h)|\le\widehat C_N^h(\eta)+1+\frac1{2K\eta}+\lfloor\log_2K\rfloor\Delta_N(|h|K)$ — but the "$+1$" and $\widehat C^h$ (near-zero of $hU_n$, not $U_n$) make it weak.

**(B2)** The *defect* form, which is the load-bearing one:
$$\Big|W_N(h)-\frac1K\sum_{k=1}^K W_N(hk)\Big|\le \frac1N\sum_n\Big|e(hU_n)-g_K(hU_n)\Big|.$$

## Verdict on Target B

The inequality **as literally stated in the prompt** has:
1. A subtle **type mismatch**: $C_N(\eta)$ is defined on $\|U_n\|<\eta$, but the geometric kernel is evaluated at $x_n=hU_n$, so the correct near-zero term is $\widehat C^h_N(\eta)$ (fraction with $\|hU_n\|<\eta$).
2. The constant structure ($C_N(\eta)+\frac1{2K\eta}$ with coefficient 1 on each, no $+1$ and no $(1-C)$ correction) **does not close** under the natural derivation — the natural derivation produces a $(1-\widehat C)$-weighted far term and an extra $+1$.

**However**, 8000 structured + random adversarial cases produced **zero violations**, so the literal inequality may still be true via a sharper argument than the crude $|e|+|g_K|$ split (specifically, exploiting cancellation in $e(x)-g_K(x)$ that the crude bound discards).

**Status:** Target B is **UNVERIFIED as stated** — its constants/types do not follow from the natural derivation, and I have not yet found the sharpening that would prove (or a witness that would refute) it. It is numerically consistent but NOT a theorem I can sign yet. This is exactly the kind of "attractive but not-yet-proved" statement the discipline forbids me to promote.

## What is PROVED and USEFUL (the real content)

The **defect identity (B2)** is exact and proved, and it isolates precisely where a signed source-cancellation theorem must act: the real phase $e(hU_n)$ is *exactly* its $K$-averaged multiplier average plus a defect that the geometric kernel bounds by $1/(2K\|hU_n\|)$ off the zero set. This decomposes the Weyl requirement into:
(a) near-zero concentration $\widehat C^h_N(\eta)\to0$, and
(b) prime-frequency defect $\Delta_N(H)\to0$ along suitable schedules.
