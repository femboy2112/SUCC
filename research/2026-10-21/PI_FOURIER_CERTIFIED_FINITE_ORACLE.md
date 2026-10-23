# Certified finite Fourier means from the polygon source

Date: 2026-10-21. Status: **PROVED PAPER / EXACT FINITE CERTIFICATE / NOT FORMALIZED**.
This is a narrow implementation of issue #217's proposed holdout instrument.
The construction uses classical Taylor remainder bounds, polygon exhaustion,
and the circle-map Lipschitz inequality. Its value is a new-to-project exact
source-to-observable certificate, not an originality claim or a π-normality
argument. It is separate from the Main VIII integration repair commit
`72d78d8a5cdd595caf144fa1b5e773519511ce0c`.

## 1. The finite theorem

For integers `b≥2`, `h≠0`, and `1≤N≤4096`, define

\[
 A_{b,h,N}(x)=\frac1N\sum_{j=0}^{N-1}\exp(2\pi i h b^j x).
\]

The function `pi_orbit_fourier_enclosure` returns exact rational rectangles
containing the real and imaginary parts of `A_{b,h,N}(π)`, and an exact rational
interval containing its squared modulus. It internally builds an outward
Archimedean polygon bracket; no caller-supplied assertion that an arbitrary
interval contains π is accepted. An exact rational source has a separate entry
point and pays no source uncertainty. Both entry points still pay the error in
π's role as the angle conversion constant.

Resource parameters are `0≤polygon_steps≤100`, `1≤precision_bits≤4096`, and
`1≤taylor_order≤128`. Every discrete parameter must be an actual Python integer,
not a bool, float or Fraction. Rational source inputs must be exact integers or
Fractions. If polygon refinement cannot maintain a positive chord enclosure,
the function fails closed. A coarse valid bracket may instead yield a trivial
interval; no accuracy target is promised independently of these parameters.

A reproducible exact instance is

\[
 \boxed{\frac1{25}<
 \left|\frac1{32}\sum_{j=0}^{31}\exp(2\pi i\,2^j\pi)\right|^2
 <\frac1{20}.}
\]

Parameters: base 2, frequency 1, horizon 32, 36 polygon doublings, 256 bits,
Taylor order 20. The source transport budget is less than `1/10^12`. This is
a theorem about one finite sum. Neither positive finite bias nor a small
finite mean determines its limiting behavior.

## 2. Derivation, with both appearances of π accounted for

Let `[L,U]` be the returned rational polygon enclosure, `p=(L+U)/2`, and
`ε=(U−L)/2`. Its **actual rounded width** is used throughout. First replace the
orbit source π by the exact rational number p. For the true Fourier character,
`|exp(2πiu)−exp(2πiv)|≤2π d_circle(u,v)<8d_circle(u,v)`. Thus

\[
 |A_{b,h,N}(\pi)-A_{b,h,N}(p)|
 \le 8|h|\epsilon\frac{b^N-1}{N(b-1)}=:E_{\rm source}.
\]

This also bounds each coordinate error. It is a paid finite-horizon estimate,
not a bound uniform in N at fixed precision.

For each rational phase, reduce `h b^j p` modulo one to
`q_j∈[-1/2,1/2]`. The desired angle is `2πq_j`; evaluate at the rational angle
`t_j=2p q_j` instead. Since sin and cos are 1-Lipschitz on the real line, the
additional coordinate error is at most `2|q_j|ε`. This separate triangle step
is valid even though the same π generated both errors; no independence of
uncertainties is assumed. The reduction is performed in **turns**, before
multiplication by the approximate radian constant, so a falsely approximate
period is not used.

For an integer `r≥1`, form the exact rational Taylor polynomials

\[
 C_r(t)=\sum_{k=0}^r\frac{(-1)^k t^{2k}}{(2k)!},\qquad
 S_r(t)=\sum_{k=0}^r\frac{(-1)^k t^{2k+1}}{(2k+1)!}.
\]

Regard `C_r` as the degree-`2r+1` Taylor polynomial with a zero last coefficient,
and `S_r` as degree `2r+2` with a zero last coefficient. Taylor's theorem and the
unit bound on every real derivative of sin/cos give

\[
 |\cos t-C_r(t)|\le\frac{|t|^{2r+2}}{(2r+2)!},\qquad
 |\sin t-S_r(t)|\le\frac{|t|^{2r+3}}{(2r+3)!}.
\]

No alternating-term monotonicity or floating arithmetic is needed. Average the
polynomials and their individual error budgets; enlarge each coordinate by
`E_source`. Intersecting with `[-1,1]` is valid because an average of unit-circle
points has both coordinates there. For any rectangle `[a,b]×[c,d]`, the sum of
the minimum coordinate squares is a lower bound for the squared modulus, and
the sum of the maximum squares is an upper bound. Intersect the latter with 1
by the triangle inequality. This proves every returned interval.

The use of positive finite source bounds here is geometry, not Weil source
positivity. These modules are not registered as formal or external proof
authority. The trust boundary is the paper derivation plus the executable exact
checker on reviewed sources, not an arbitrary object labeled a certificate.

## 3. A genuinely different finite evaluation holdout

The independent tests do not call the Fourier Taylor implementation to obtain
the comparison values. Their two separate constructions are:

1. An alternating-series Machin identity encloses π and therefore its finite
   orbit source phases. It is a holdout source, never an input to the production
   polygon algorithm.
2. Starting from the exact fourth root `i`, repeated half-angle square roots
   enclose `exp(2πi/2^20)`. Exact interval complex multiplication and binary
   exponentiation evaluate a dyadically quantized phase. The loss from replacing
   any phase by its left `2^-20` grid point is at most `8·2^-20`. Every square root
   and arithmetic operation is outward rounded on a declared 160-bit grid.

This gives a second rigorous rectangle for the true π Fourier mean, including
its separately paid Machin source error. The sharper Taylor rectangle lies
inside the independent wider rectangle for `(b,h,N)=(2,1,8),(2,1,32),(2,-3,16),
(3,2,12)`. The methods share the elementary Lipschitz transport theorem and
circle source semantics. They use different transcendental-evaluation
mechanisms; this is not independent academic refereeing or formal verification.

## 4. Calibrated countercontrols

The exact same instrument is run on nonnormal rational sources:

- `x=0`: the mean is exactly 1 at every horizon, with squared modulus exactly 1.
- `x=1/3`, base 2, even N: the mean is `−1/2`, squared modulus `1/4`.
- `x=1/4`, base 2, `N≥2`: the mean is `(N−3+i)/N`.
- `x=1/7`, base 2, N=3: the mean is `(-1+i sqrt(7))/6`, squared modulus `2/9`.

The last identity is an independent algebraic control: the quadratic-residue
root sum plus its conjugate is −1, its product with its conjugate is 2, and its
imaginary part is positive. No decimal sine value is needed to check the test.
The rational controls reject any proposed inference that a fine source
bracket alone creates Fourier cancellation.

An underresolved π calculation with two doublings, sixteen bits and horizon
32 correctly returns the trivial squared-modulus range `[0,1]`. An insufficient
error budget cannot silently manufacture a precise answer. Negative frequencies,
integer phase shifts, nonexact numerical inputs and invalid resource parameters
are also tested.

## 5. Evidence, limitations and next decisive probe

Files:

- `observational_succ/pi_fourier_certificate.py`: exact instrument;
- `tests/test_pi_fourier_certificate.py`: six tests, including four independent
  true-π evaluations and rational algebraic controls;
- `scripts/pi_fourier_certificate_probe.py`: small fixed receipt;
- [PI_FOURIER_FINITE_RECEIPT.json](PI_FOURIER_FINITE_RECEIPT.json): source hashes,
  explicit parameters, outward rational endpoints and separate error budgets.

Reproduce:

```sh
python -m unittest tests.test_pi_fourier_certificate -v
python scripts/pi_fourier_certificate_probe.py --output /tmp/pi-fourier.json
```

All six tests passed on Python 3.12.14. The receipt's output endpoints are rounded
outward to a declared denominator `10^18`; paid error budgets are rounded upward
to `10^30`. The computations internally remain exact. No full-repository suite,
Lean theorem, infinite Fourier cancellation or normality assertion is included.

The missing theorem is still: for each fixed nonzero h and fixed base b, prove
`A_{b,h,N}(π)→0` from π-specific structure. The oracle can refute proposed finite
inequalities, diagnose unpaid phase budgets, and independently check finite
consequences of a future source theorem. It supplies no decay mechanism. A
useful next probe is a **predeclared** finite consequence of a proposed
π-specific recurrence estimate, tested against these exact certificates and
the rational controls; merely increasing N is not a verdict-changing theorem.
