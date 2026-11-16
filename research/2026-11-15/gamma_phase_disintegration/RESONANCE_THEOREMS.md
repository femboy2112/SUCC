# GP-R — Authentic Green residual: detuned and avoided resonances

## Status and provenance

The source audit read `AGENTS.md`, `docs/METHOD.md`, draft #651 at
`94c7252ac7db3c8b14229544087119bd9cc01933`, and the inherited dossiers.
The exact positive Gamma rate mixture, the first two moments below, the
fixed-frequency modulus theorem, and the undetuned lattice first-order
limit are **inherited**, explicitly in
`research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md`, sections 6–8, and
`observational_succ/bbp_log_mixture.py`. The positive rate-mixture
mechanism is also reused in #639 CN-06/CN-07. Do not count rediscovery as
new progress.

The new local consequence developed here is a quantified **avoided
resonance** theorem. An asymptotically zero auxiliary Fourier coefficient
cannot be canceled to the next order by any bounded real frequency
detuning. The surviving imaginary coefficient is a source readout
residual. It is not an arithmetic Weyl or carry estimate.

## 1. Exact inherited probability law

Let `J>=1` have mass `15*16^(-J)` and let `U` have density
`[2*1_[0,3]+1_[0,4]+1_[0,5]]/15`, independently. Set

$$ B=8J-7+U. $$

Equivalently `B=K+V`, where `V` is uniform on `[0,1]`, independent of the
integer `K`, and

$$
\Pr(K=8j-7+i)=16^{-j}c_i,\qquad
(c_0,c_1,c_2,c_3,c_4)=(4,4,4,2,1).
$$

All moments are finite, and independent exact geometric/polynomial
calculation gives

$$
m_1=\frac72,\quad m_2=\frac{55}3,\quad
m_3=\frac{595}4,\quad m_4=\frac{8551}5.
$$

For `a=8n`, `n>=1`, put

$$
D_a=\mathbb E(1+B/a)^{-2}=a^2T_n,
\qquad d\nu_a=D_a^{-1}(1+B/a)^{-2}d\mu,
$$
$$
\Psi_a(t)=\mathbb E_{\nu_a}e^{-it\log(1+B/a)}.
$$

The inherited normalized tail Gamma law has logarithmic characteristic
function `Gamma(2+it)*Psi_a(t)` (up to the declared common centering
phase). `Psi_a` here is the inherited `Psi_n`; subscript `a` makes the
scaling explicit.

## 2. Complete real zero set of the limiting moving-frequency spectrum

For every real `c`, dominated convergence gives

$$\Psi_a(ac)\longrightarrow F(c):=\mathbb E e^{-icB}.$$

For `c!=0`, putting `z=e^{-ic}` gives the exact expression

$$
F(c)=\frac{1-e^{-ic}}{ic}\,
\frac{z(z^2+2)(z^2+2z+2)}{16-z^8}.
\tag{S1}
$$

The factorization is `4+4z+4z^2+2z^3+z^4=(z^2+2)(z^2+2z+2)`.
The four polynomial roots have modulus `sqrt(2)>1`; the denominator
cannot vanish on `|z|=1`. Consequently the real zeros of `F` are
**exactly** `c=2*pi*k`, nonzero integer `k`. These zeros are simple:

$$F'(2\pi k)=\frac1{2\pi k}.$$

This is a full classification of the limiting auxiliary spectrum's real
zeros, not a classification of finite-`n` zeros or BBP orbit phases.
For comparison, the inherited moving-frequency bound extends directly to
all real `c`:

$$
|\Psi_a(ac)-F(c)|\le
\frac{14+55|c|/6}{a}\left(1+\frac7{2a}\right)^2.
\tag{S2}
$$

For general `c`, the extra 7 in (S2) pays for normalization of a nonzero `F(c)`; at a lattice zero it drops out, recovering the inherited coefficient 7. The initial version mistakenly omitted this normalization term and was corrected after root audit. This extension follows from the inherited proof with that additional cost;
(S1)'s exact zero classification and the next-order detuning consequence
are the useful new pieces.

## 3. Quantified avoided resonance theorem

Fix a nonzero integer `k`, set `c=2*pi*k`, and fix a finite real `D>=0`.
For every integer `n>=1`, `a=8n`, and every real `d` with `|d|<=D`, define

$$L(c,d)=\frac d c-\frac72-\frac i c,$$

$$
C(c,D)=
\left(3+\frac{5D}2+\frac{D^2}2\right)m_2
+|c|\left(\frac43+\frac D2\right)m_3
+\frac{c^2}8m_4.
$$

Then

$$
\boxed{
\left|a\Psi_a(ac+d)-L(c,d)\right|
\le \frac{(1+m_1/a)^2}{a}
\left[C(c,D)+2m_1|L(c,d)|\right].}
\tag{S3}
$$

In particular the asymptotic expansion

$$
\boxed{
\Psi_a(ac+d)
=\frac1a\left(\frac d c-\frac72-\frac i c\right)
+O_{k,D}(a^{-2})}
\tag{S4}
$$

is uniform over the entire declared detuning interval. The real term can
be canceled by the choice `d=(7/2)c`; the imaginary term cannot. Thus

$$
\inf_{d\in\mathbb R}|L(c,d)|=\frac1{|c|},
\qquad
L(c,(7/2)c)=-\frac i c.
\tag{S5}
$$

The infimum in (S5) is a statement about the first-order coefficient.
It does not authorize optimizing `d` outside any fixed interval while
using the uniform estimate (S3).

### Explicit eventual lower bound

Let

$$
E(c,D)=\frac{529}{256}
\left[C(c,D)+7\left(\frac72+\frac{D+1}{|c|}\right)\right].
$$

Since `a>=8`, `(1+m_1/a)^2<=(23/16)^2=529/256`, and
`|L(c,d)|<=7/2+(D+1)/|c|`. Therefore

$$
\left|a\Psi_a(ac+d)-L(c,d)\right|\le E(c,D)/a.
$$

For every `n>=max(1,ceil(|c|E(c,D)/4))` and every `|d|<=D`,

$$
\boxed{|\Psi_a(ac+d)|\ge\frac1{2|c|a}>0.}
\tag{S6}
$$

The cutoff is intentionally conservative and computable. No small-index
zero-free claim is made. Equation (S6) proves that every such finite
frequency neighborhood is eventually free of exact zeros, although its
limiting rescaled coefficient vanishes.

### Proof of the uniform remainder

Put `x=B/a`, `w=(1+x)^(-2)`, and

$$
y=c[B-a\log(1+B/a)]-d\log(1+B/a),\qquad
 y_0=(cB^2/2-dB)/a.
$$

Elementary integral remainders, valid for every `B>=0`, give

$$
|w-1+2B/a|\le3B^2/a^2,\qquad |w-1|\le2B/a,
$$
$$
|y-y_0|\le\frac{|c|B^3/3+D B^2/2}{a^2},\qquad
|y|\le\frac{|c|B^2/2+D B}{a}.
$$

The inequality `|exp(iy)-1-iy|<=y^2/2` now yields

$$
\left|w e^{iy}-1-\frac{-2B+i(cB^2/2-dB)}a\right|
\le\frac1{a^2}\left[
\left(3+\frac{5D}2+\frac{D^2}2\right)B^2
+|c|\left(\frac43+\frac D2\right)B^3
+\frac{c^2}8B^4\right].
$$

Multiply by `exp(-icB)`, whose modulus is one, and take expectations.
At the integer resonance, `exp(-icK)=1` and the uniform-cell integrals are

$$
\mathbb E e^{-icB}=0,\quad
\mathbb E[B e^{-icB}]=\frac i c,\quad
\mathbb E[B^2e^{-icB}]=\frac{7i}c+\frac2{c^2}.
$$

For the last identity use `E K=3` and
`integral_0^1 v^2 exp(-icv)dv=i/c+2/c^2`. Thus the unnormalized numerator
is `L(c,d)/a+R` with `|R|<=C(c,D)/a^2`. Finally

$$
D_a\ge(1+m_1/a)^{-2},\qquad |1-D_a|\le2m_1/a
$$

by Jensen and `1-(1+x)^(-2)<=2x`. Divide the numerator by `D_a`:
`|aPsi-L| <= [a|R|+|L||1-D_a|]/D_a`. This is (S3). Every remainder is
integrable because the fourth source moment is finite.

## 4. Discriminating controls and conditioning interpretation

The leading coefficient also identifies a limit of source specificity. The
same calculation for any `B=K+V`, with independent integer K, uniform V and
finite fourth moment, replaces `7/2` by `E B`. Thus another unit-cell law with
the same mean reproduces this first-order response. The exact original law
fixes the full spectrum and explicit remainder constants, but this one
coefficient is not a unique authentication of pi. The inherited rational
unit-cell control in the October 26 bridge must still be rejected by the full
four-pole source contract.

1. **Remove the source tilt.** Replacing `nu_a` by `mu` preserves the
leading limiting spectrum `F`, but the same derivation yields
`a Psi_untitled(ac+d) -> d/c-7/2+i/c`. The imaginary coefficient flips
sign. This is a concrete mutation discriminator for the load-bearing
weight `(1+B/a)^(-2)`.
2. **Remove log curvature.** Replacing `a log(1+B/a)` by `B` before the
first-order expansion loses the `i c B^2/2` term and gives a different
coefficient. It cannot validate (S4).
3. **Mean phase substitution.** `exp(-it E_n log(1+B/a))` always has
modulus one, while (S4) tends to zero. This directly separates the two
orders of nonlinear operation without any claim about π normality.
4. **Seed control.** All quantities above are functions of the forcing
and tail, not of the recurrence seed. The coherent changed seed `-pi/16`
leaves the entire spectral theorem intact while the completed real
circle orbit becomes identically zero. Therefore no all-seed arithmetic
Weyl inference follows.

At the optimized detuning `d=(7/2)c`, the inverse multiplier of the
**residual factor** grows asymptotically like `|c|a`; at the unshifted
frequency it grows like `a/sqrt((7/2)^2+1/c^2)`. The full normalized
Gamma multiplier also includes `Gamma(2+it)`, whose classical exponential
high-frequency attenuation remains in force. Algebraic residual
reconstruction is not a bounded, frequency-uniform inverse.

## 5. Actual finite audit and its boundary

`audit_resonance.py` imports no SUCC production modules. It independently
computes the geometric law's moments, compares positive interval and
literal four-pole terms, checks the unit-cell polynomial factorization,
and evaluates the exact interval antiderivative with mpmath at 70 digits
and geometric depth 48.

Executed receipt: **36 exact checks and 75 numerical diagnostic checks
passed**. The diagnostic grid is `k=1,2,5`, detunings
`d=(7/2)c+offset` for `offset=-1,0,1`, and
`n=4,16,64,256,1024,16384,262144`. Each checks the proved remainder;
the last index is also compared to the limiting coefficient with
absolute tolerance 0.001. The tilt mutation is calibrated separately.
The omitted base mass is exactly `16^-48`. The reported floating-point
values are not interval certificates. Neither the finite grid nor the
threshold0.001 establishes the universal theorem; the explicit proof
above does.

The initial exploratory diagnostic incorrectly demanded monotone
convergence at every small n and failed: at k=1, optimized d, error rose
from about 0.46057 at n=4 to 0.46997 at n=16 before decreasing. No such
monotonicity is part of (S3). The final audit tests the actual remainder
instead. This failure should be retained as a scope warning if the
script's validation history is reported.

At n=262144, k=1, optimized detuning, the scaled true response was
`0.00000435049-0.15921759346i`, against the limit `-0.15915494309i`.
Removing the tilt instead gave `0.00000148952+0.15909176066i`, verifying
the predicted imaginary-sign reversal. This corroborates the algebraic
sign convention with a separately implemented finite calculation.
