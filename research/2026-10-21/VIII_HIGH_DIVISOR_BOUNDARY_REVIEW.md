# Independent constructor review of the small-divisor tail theorem

Date: 2026-10-21. Reviewed research commit:
`9bfeb09` on the separate referee branch. Statement source:
`research/2026-10-21/VIII_COFACTOR_SMALL_DIVISOR_BOUND.md`.
The constructor first received the precise theorem from the coordinator and
reconstructed its proof before reading the implementation or full manuscript.
The manuscript was inspected afterwards. This is distinct same-model
mathematical work, not an external or human referee.

**Verdict:** the stated uniform tail estimate survives this reconstruction,
including its explicit moving cutoff and arbitrary prime-power depth.
Recommended status: **PROVED PAPER**; academic novelty **UNVERIFIED**.
It does not control the remaining all-large-divisor family.

## Reconstructed proof

Fix `0<=t<1`, `alpha=(1+t)/2`, and `sigma=1-alpha>0`.
Let `s(r^2)=r^t`, zero away from squares. Define the multiplicative function
`h(1)=1`, `h(p)=h(p^2)=0`, and `h(p^k)=p^(t(k-1))` for `k>=3`.
At exponent two, `s(p^2)=p^t>=g_t(p^2)`; at every exponent at least three,
`h(p^k)>=g_t(p^k)`. Nonnegative multiplicative convolution therefore gives
`g_t<=s*h` at every integer, including deep prime powers.

For real `Y>=1`,

\[
A_t(Y)=\sum_{n\le Y}g_t(n)
\le Y^\alpha\sum_{j\ge1}h(j)j^{-\alpha}=C_tY^\alpha,
\]

where the local tail is precisely

\[
\sum_{k\ge3}p^{t(k-1)-k\alpha}
=\frac{p^{-(3-t)/2}}{1-p^{-\sigma}}.
\]

Since `(3-t)/2=1+sigma>1` and `1-p^-sigma>=1-2^-sigma>0`, the product
converges absolutely; positivity justifies its equality with the series.
For `0<=Y<1`, define `A_t(Y)=0`; the same inequality remains valid.

Now fix `X>=2`, `Q>=X^2`, `B>=1` and put `rho=X^2/Q<=1`. For any actual
source incidence with selected `d<=B`, write `b=ev,c=fw`. The relation

\[
vw=\frac{dbc}{def}<d\rho
\]

is valid because `def>Q` and `bc<X^2`. For fixed `d,v,w,e,f`, the source
is unique: `b=ev,c=fw,a=c-b`, and then `u=a/d` if this is a positive
integer. Thus discarding divisibility, positivity, source primitivity and
congruence restrictions only enlarges a sum after a valid injection.
It does not identify all incidences over one cofactor triple.

The resulting two coefficient sums give

\[
T_{d\le B}\le C_t^2X^{2\alpha}
\sum_{d\le B}g_t(d)\sum_{vw<d\rho}(vw)^{-\alpha}.
\]

If `d rho<=1`, the inner sum is empty. Otherwise elementary summation gives

\[
\sum_{vw<d\rho}(vw)^{-\alpha}
\le\frac{(d\rho)^{1-\alpha}}{1-\alpha}
\sum_{v<d\rho}v^{-1}
\le\frac{(d\rho)^{1-\alpha}(1+\log B)}{1-\alpha}.
\]

The remaining coefficient sum is at most
`B^(1-alpha) A_t(B)<=C_t B`. Repeat for `e`. For the total divisor `f`,
use `uv=fab/(def)<f rho/4<=f rho`, retaining the actual source recovery
`c=a+b`. A union bound proves

\[
T_t(X,Q;B)\le\frac{3C_t^3}{1-\alpha}
B(1+\log B)X^{1+t}(X^2/Q)^\sigma.
\]

No coefficient or error constant here depends secretly on `X,Q,B`.
Multiple small-divisor slots merely overcount an incidence in this upper bound.

For `B_t=max(1,X^(1-t)/(1+log X))`, if `B_t=1`, then
`B_t(1+log B_t)X^(t-1)<=1`. Otherwise `B_t<=X` and the same conclusion
follows by cancelling `1+log X`. This yields the advertised `K_t X^2`
uniform tail with power `(X^2/Q)^sigma` for every fixed `t<1`.
Also, every selected divisor exceeds `Q/X^2`, so the claimed empty-tail
criterion is correct.

## Scope and complementary route

The explicit family with `d=9`, `e=m^2`, `f=(m+9)^2` is primitive for
`gcd(m,3)=1` and is genuinely high-divisor for `m>=5`; this rules out
vacuity of the growing-cutoff result. The proof never assumes squarefree
roots or bounded exponent depth. It fails to provide a uniform constant at
`t=1`, consistently with the independently established first-moment divergence.

The conic construction reviewed in this lane addresses some incidences where
all three selected moduli are large, under a separate explicit root-depth
budget. The sparse Pythagorean addendum removes that depth budget on a much
thinner unbalanced source family. These are complementary restrictions; none
of the three results covers the unrestricted balanced, deep, all-large sector.
