# Adversary: source information, randomized phase, and detection dose

## Starting state and authority

Parent is #641, commit `85a14bb68aeae31d3a2796350529fda9a5c39072`, on
`research/pi-carrier-collision-2026-11-15`. Read the new hole contract,
the live Main XXV pi frontier, the older source contract, and #641's
Gamma/Haar code and interpretation. These distinguish source-selected
temporal cancellation from changing an observer's law or basis.

Source artifacts inspected before this implementation:

| Artifact | Git blob at the parent |
|---|---|
| `observational_succ/duck_bbp.py` | `34cb7b64f6975e05586ec220a4655961a8e7b636` |
| `observational_succ/bbp_echo_delay_transport.py` | `6632813341f47239fd64d618a7e41b641b1f0e17` |
| `research/2026-11-01/moonshot_phase_echo/PROOFS.md` | `b5681551a2e1bf0a8a7cbde6fdef87b0f0389a41` |
| `observational_succ/haar_gamma_bridge.py` | `5a8fcfddae659fd4cc5aa566efb600058b82430e` |
| `docs/PI_NORMALITY_FRONTIER.md` | `bb50ef8d5e1404bccd6c40e4dade975c79020fa7` |

The fixed source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_n(s)=16U_{n-1}(s)+r(n),\quad U_0(s)=s.
\]

Write \(\xi=\pi/16\) and \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\).
The inherited exact identity is
\(U_n(s)+T_n=16^n(\xi+s)\). The target retains **s=0**.
Every changed-seed control below is labelled; it is not a counterexample
to a theorem restricted to the authentic zero seed.

The existing finite-delay module already implements integer-tap symbols,
division by `X-16`, and authentic source/Green transport. The moonshot
dossier already distinguishes a source-faithful phase echo from raw
probe smoothing, with the latter's resolution cost. Those are reused
mathematical boundaries, not claimed as discoveries of this round.

## Preregistered finite controls

Freeze these cases before writing `phase_detection.py`:

- Integer Gamma shapes `1,2,5,12`, rates `1/3,1,5/2`, angular frequencies
  `-3/2,0,1,7`. Exact rational real and imaginary responses will be checked
  against an independent binomial-power oracle, conjugation, and shape
  addition. Angular frequency is in radians per clock unit; it is not
  silently identified with an integer Fourier frequency measured in turns.
- Finite phase circles of sizes `2,3,5,8,11`, with locked, uniform, and
  nonuniform rational source laws. Uniform forgotten clocks must erase
  their distinction, and retained clocks must recover it exactly.
- Unit-noise ensembles with support `{1,i}` and `{i,-i}`, chosen to match
  the first moments of Gamma shapes one and two at rate/frequency one.
  Enumerate their complete product sample spaces at lengths `1,3,5` to
  test the exact mean-square-error identity. These ensembles are moment
  controls, not simulated Gamma distributions.
- Bernoulli detection rates `0,1/17,1/2,1`, with trial counts
  `0,1,2,7,19`. Enumerate a separate small Bernoulli product space and
  test a repeated-single-record mutation against fresh repetitions.
- Propensity controls include uniform selection, the two-point policy
  `(99/100,1/100)`, and a one-success-in-eight population selected with
  success propensity `9/10`. Corrected expectations must recover the
  uniform population statistic while the naive selected mean changes.
- Authentic-source counterseed shells `B=1,2,5,11`, using inherited exact
  tail enclosures at depths `1,3,7`. A new rational cosine inequality
  supplies finite escape bounds; no decimal cosine or asymptotic formula
  may be called a finite certificate.

Positive, negative, zero, sign, and support controls include zero intensity,
erased clock, reversed angular sign, source-dependent clock coupling,
zero propensity, unnormalized probability laws, wrong `escape/2`
normalization, unsupported zero-length averages, and illegal float inputs.

## Review boundary

At this stage the production proposal is bounded exact arithmetic for
Gamma response and recovery cost, finite rotation laws, propensity
correction, fresh-trial detection probabilities, and original-forcing
counterseed enclosures. Universal asymptotics belong to the proofs below.
No full repository suite, physical measurement, or all-scale zero-seeded
escape claim is authorized by those finite controls.

## PD-01. Retaining a randomization clock preserves the source; forgetting it can erase everything

Let \(S\) take values in the finite circle \(\mathbb Z/q\mathbb Z\)
with law \(\mu\), and let an independent clock \(C\) have law \(\nu\).
Report \(Y=S+C\). The complete report has law

\[
J(y,c)=\mu(y-c)\nu(c),\qquad
\Pr(Y=y)=\sum_c\mu(y-c)\nu(c).
\tag{PD1}
\]

**DISCLOSED.** Retaining the clock gives exact recovery
\(S=Y-C\), and at the law level
\(\mu(s)=\sum_cJ(s+c,c)\). For any two source laws the complete
reports preserve total variation exactly:

\[
\frac12\sum_{y,c}|J_\mu(y,c)-J_{\mu'}(y,c)|
=\frac12\sum_s|\mu(s)-\mu'(s)|.
\]

The equality follows by changing variables \(s=y-c\) in each column
and using \(\sum_c\nu(c)=1\). The retained report preserves source
information; it has not generated a source distinction that was absent.

For the uniform clock, however, the forgotten output is uniform for
**every** source law, including the perfectly locked source \(S=0\).
Consequently its finite-circle nontrivial Fourier modes vanish exactly.
This is an exact false-positive control for inferring source cancellation
from detector cancellation. It is not a counterexample to normality of
the actual zero-seeded BBP source. On a finite circle, modes divisible by
\(q\) are the trivial character; they are not claimed to vanish.

Clock dependence matters. If a uniform source uses \(C=-S\), then the
forgotten output is locked at zero despite uniform source and clock
marginals. The independent convolution formula cannot be used from those
marginals alone. Retained decoding still works: it uses the full joint
law, not an independence assumption.

## PD-02. Gamma rotation has an exact inverse cost, and increasing intensity can destroy statistical identifiability

Let \(T\sim\mathrm{Gamma}(\alpha,\lambda)\), shape \(\alpha>0\),
rate \(\lambda>0\). Let \(\omega\) be angular frequency, and define
\(\eta=\exp(i\omega T)\). The Gamma integral gives

\[
m_\alpha(\omega)=\mathbb E\eta
=\left(\frac{\lambda}{\lambda-i\omega}\right)^\alpha,
\quad
|m_\alpha(\omega)|
=\left(1+\frac{\omega^2}{\lambda^2}\right)^{-\alpha/2}.
\tag{PD2}
\]

Use the principal power; \(\lambda-i\omega\) lies in the right
half-plane. This is the classical Laplace–Gamma formula with a complex
argument, [NIST DLMF 5.9.1](https://dlmf.nist.gov/5.9.E1). For integer
shape, it also follows by multiplying the exponential-clock response
\(\lambda/(\lambda-i\omega)\). The production interface restricts
shape to an integer and rate/frequency to rationals, making both parts
of the multiplier exact Fractions. A frequency in turns would require
the explicit conversion \(\omega=2\pi f\); the interface never
silently drops that factor.

For any fixed unit phase \(z\), reporting \(Y=z\eta\) gives
\(\mathbb EY=m_\alpha(\omega)z\). In particular, \(z=1\) produces
arbitrarily small forgotten-clock mean as \(|\omega|\to\infty\).
More strongly, each fixed nonzero integer Fourier coefficient of the
wrapped rotation is \(m_\alpha(h\omega)\to0\). Trigonometric
polynomial approximation then proves weak convergence to uniform circle
measure. This uniformity is manufactured by the clock, even on a locked
source.

For finite intensity the multiplier is nonzero. Exact mean recovery is
possible, but an additive error \(\delta\) in the measured mean is
amplified in absolute value by the exact factor

\[
\kappa=|m_\alpha(\omega)|^{-1}
=\left(1+\omega^2/\lambda^2\right)^{\alpha/2}.
\tag{PD3}
\]

This is the exact condition number of that scalar inverse. It is not a
claim that every numerical error has that size. On the Fourier band
\(|h|\le H\), the corresponding circle-convolution inverse has
\(L^2\) norm \((1+H^2\omega^2/\lambda^2)^{\alpha/2}\). All modes
are nonzero, so the convolution is injective on finite measures, but
for \(\omega\ne0\) its inverse is unbounded on unrestricted \(L^2\).
Injectivity therefore does not imply stable recovery at every resolution.

### Exact sampling cost for the recovered mean

Fix deterministic phases \(|z_n|=1\), and use mutually independent
Gamma clocks with the stated common parameters. Put

\[
Z_N=\frac1N\sum_{n=1}^Nz_n,\qquad
\widehat Z_N=\frac1{Nm_\alpha(\omega)}\sum_{n=1}^Nz_n\eta_n.
\]

Then

\[
\mathbb E\widehat Z_N=Z_N,\qquad
\boxed{\mathbb E|\widehat Z_N-Z_N|^2
=\frac{(1+\omega^2/\lambda^2)^\alpha-1}{N}.}
\tag{PD4}
\]

**Proof.** Each centered rotation has squared absolute expectation
\(1-|m|^2\). Cross terms vanish by independence, while
\(|z_n|=1\). Divide the sum of the \(N\) variances by
\(N^2|m|^2\). QED.

For varying detector intensity, this estimator converges in mean square
exactly when the numerator in (PD4) is \(o(N)\). A probability error
bound follows directly from
\(\Pr\{|\widehat Z_N-Z_N|\ge\varepsilon\}\le
(\kappa^2-1)/(N\varepsilon^2)\).
These are statements about the displayed estimator, not universal
computational lower bounds for arithmetic. Reusing a single clock gives
correlated errors and does not buy the factor \(1/N\). The tests
explicitly reject that mutation.

If the clock is retained, instead demodulate each observation:
\(Y_n\exp(-i\omega T_n)=z_n\) exactly. A clock reconstruction with
\(|\widehat T_n-T_n|\le\epsilon_n\) gives

\[
|Y_n e^{-i\omega\widehat T_n}-z_n|
\le\min(2,|\omega|\epsilon_n).
\tag{PD5}
\]

The resource changes from inverse noise amplification to clock precision.
The statement assumes that the phase observation and its clock are
available; it does not supply a physical measurement device.

### A statistical lower bound applying to every forgotten-clock test on a declared rival class

There is an elementary stronger control, derived after the initial finite
grid was frozen. Give the source angle the two densities
\(1\pm\epsilon\cos(h\theta)\) relative to normalized circle measure,
with \(h\ne0\) and \(0<\epsilon\le1/2\). Their total-variation
distance is \(2\epsilon/\pi\). After Gamma rotation, the densities
are \(1\pm\epsilon r\cos(h\theta-\varphi)\), where
\(r=|m_\alpha(h\omega)|\) and \(\varphi\) is its declared phase.
Their total-variation distance is exactly \(2\epsilon r/\pi\).

For the two output laws \(P_+,P_-\),

\[
\chi^2(P_+\Vert P_-)
=\int\frac{4\epsilon^2r^2\cos^2(h\theta-\varphi)}
{1-\epsilon r\cos(h\theta-\varphi)}\,d\theta/(2\pi)
\le4\epsilon^2r^2.
\]

The bound uses \(1-\epsilon r\cos\ge1/2\) and mean cosine square
\(1/2\). For \(N\) independent observations, direct product
integration gives \(1+\chi^2(P_+^{\otimes N}\Vert P_-^{\otimes N})
=(1+\chi^2(P_+\Vert P_-))^N\). Cauchy–Schwarz gives
\(\operatorname{TV}\le\sqrt{\chi^2}/2\). Equal-prior testing error
at most \(1/4\) requires total variation at least \(1/2\), hence

\[
\boxed{N\ge\frac{\log2}{4\epsilon^2r^2}.}
\tag{PD6}
\]

This lower bound applies to any test using those independent
forgotten-clock observations. It establishes an actual statistical
instability on the specified rival class, not just a poor choice of
linear estimator. It is neither a lower bound for every BBP algorithm
nor an assertion that the actual arithmetic orbit is one of these
random source laws.

## PD-03. A favorable sampling policy changes what is sampled; propensity correction exposes the debt

Fix a finite population \(f_1,\ldots,f_N\), and target its uniform
mean \(\bar f=N^{-1}\sum_i f_i\). Sample index \(I\) with known
positive propensities \(q_i\). The selected mean is
\(\sum_iq_if_i\), while the corrected observation is
\(X=f_I/(Nq_I)\). Direct finite summation gives

\[
\mathbb EX=\bar f,\qquad
\mathbb E|X|^2=\frac1{N^2}\sum_i\frac{|f_i|^2}{q_i},\qquad
\mathbb E|X-\bar f|^2=\mathbb E|X|^2-|\bar f|^2.
\tag{PD7}
\]

For unit phases the second moment is
\(N^{-2}\sum_i1/q_i\). If \(q_i\ge\varepsilon/N\), it is at
most \(1/\varepsilon\). If any propensity is zero, general recovery
is impossible: populations differing only at that unobserved index have
identical report laws and different target means.

The identity also holds conditionally for a predictable adaptive policy
\(q_{t,i}\) given the retained past, provided those are the true
conditional selection probabilities. The corrected error is then a
martingale difference. A propensity reconstructed only after seeing the
selected outcome, or a selection law with an omitted hidden dependence,
does not inherit this calibration.

**Exact controls.** The population \((1,0)\) sampled with propensities
\((99/100,1/100)\) reports a naive success rate \(99/100\), while
its corrected and target means are both \(1/2\). One success among
eight indices can be reported with probability \(9/10\), although
its uniform population density is \(1/8\). Conversely, placing the
important value in the rare second position gives corrected variance
\(99/4\). High selected success and low recovery variance for one
fitted population do not certify the unobserved parts of another.

## PD-04. Detection amplification is exact, but its required arithmetic event rate cannot be omitted

For any specified phase stream, put

\[
d_n=1-\cos(2\pi U_n),\qquad
A_B=\frac1B\sum_{n=B}^{2B-1}d_n\in[0,2].
\]

Choose a fresh uniform index \(I\in\{B,\ldots,2B-1\}\), and an
independent uniform threshold \(V\in[0,1]\). The source-coupled
detector succeeds iff \(V\le d_I/2\). Its event rate is exactly
\(p_B=A_B/2\). For \(m\) independent repetitions,

\[
\boxed{\Pr\{\text{at least one success}\}
=1-(1-A_B/2)^m.}
\tag{PD8}
\]

For \(m\ge1\) and \(0<\delta<1\), confidence at least
\(1-\delta\) is therefore equivalent to

\[
\boxed{A_B\ge2(1-\delta^{1/m}).}
\tag{PD9}
\]

If the same bounded trial budget works on all sufficiently large shells,
this is a uniform positive escape estimate. It is a reformulation of
that arithmetic obligation, not its proof. If the trial budget grows,
the necessary bound shrinks like \(2\log(1/\delta)/m\); high
detection probability can then coexist with vanishing shell escape.

For any fixed shell with \(A_B>0\), repeated independent trials
eventually succeed with probability one. Countably many such searches
can each terminate almost surely, while their costs grow without a
uniform bound. A witness somewhere in each shell is much weaker than a
positive lower density. Copying one previously observed Bernoulli event
does not repeat the trial: four copies of a rate-\(1/3\) event still
have success probability \(1/3\), whereas four fresh trials have
probability \(65/81\).

Independence can be weakened for a lower guarantee: if each new trial's
conditional success probability, given every previous failure, is at
least \(p_*\), then failure after \(m\) trials is at most
\((1-p_*)^m\). The required conditional lower bound is the premise;
calling a repeated or adaptive probe “fresh” does not establish it.

## PD-05. The original-forcing counterseed has quartic detection-dose growth

Set the **changed seed** \(s=-\xi\), keeping all four authentic
forcing channels. Then \(U_n(s)=-T_n\) exactly. The positive
regrouping

\[
r(n+1)=\frac6{(8n+1)(8n+4)}
+\frac4{(8n+1)(8n+5)}
+\frac5{(8n+1)(8n+6)}
<\frac{15}{64n^2}
\]

proves \(0<T_n<1/(64n^2)\), for \(n\ge1\). For each fixed
\(j\ge1\), \(n^2r(n+j)\to15/64\), and the displayed bound
dominates the geometric tail sum. Hence

\[
n^2T_n\longrightarrow\frac1{64},\qquad
1-\cos(2\pi T_n)\sim\frac{\pi^2}{2048n^4}.
\]

The positive coefficient limit is uniform on tails of the sequence, so
the shell Riemann sum gives

\[
\boxed{A_B\sim\frac{7\pi^2}{49152}B^{-4},\qquad
p_B\sim\frac{7\pi^2}{98304}B^{-4}.}
\tag{PD10}
\]

Indeed \(\int_1^2t^{-4}dt=7/24\). Every finite shell has strictly
positive detection rate, although \(A_B\to0\). For fixed
\(0<\delta<1\), the least number of fresh trials reaching confidence
\(1-\delta\) is

\[
\left\lceil\frac{\log\delta}{\log(1-p_B)}\right\rceil
\sim\boxed{\frac{98304}{7\pi^2}\log(1/\delta)B^4}.
\tag{PD11}
\]

This follows from \(-\log(1-p)\sim p\). Its expected waiting time
is \(1/p_B\), with the same quartic scale and no logarithmic
confidence factor. Thus unlimited detection dose can manufacture
near-certain successful reports on a source with no uniform escape.
The failure is a seed-selected arithmetic rate, not an error in the
Bernoulli amplification law.

### A genuine finite rational enclosure, separate from the asymptotic

The code does not initialize a rounded approximation to \(-\pi/16\),
which would incur exponential source-seed error. It uses the exact
symbolic identity \(U_n(-\xi)=-T_n\), and calls the inherited
original-source `duck_bbp.tail_interval`. Suppose that returns
\(0<\ell_n\le T_n\le u_n\), with
\((44/7)u_n\le1\), as verified exactly in the implemented domain.
For \(|t|\le1\),

\[
\frac{t^2}{3}\le\frac{t^2}{2}-\frac{t^4}{24}
\le1-\cos t\le\frac{t^2}{2}.
\]

Using the classical rational bounds \(3<\pi<22/7\) gives

\[
12\ell_n^2\le1-\cos(2\pi T_n)
\le\frac{968}{49}u_n^2.
\tag{PD12}
\]

Averaging (PD12) supplies exact rational shell bounds and monotonicity
of (PD8) transports them to detection-probability bounds. These are
finite certificates backed by analytic inequalities. They are not
decimal observations or finite evidence for the all-scale asymptotic.
The source adapter is independently checked in the tests against the
literal four-pole formula.

## PD-06. Coherent echoes must be typed by the seed coordinate they retain

For integer taps \(P(X)=\sum_{j=0}^da_jX^j\), integer synthetic
division gives \(P(X)=P(16)+(X-16)Q(X)\), with \(Q\in\mathbb Z[X]\).
The original recurrence therefore gives

\[
P(E)U_n(s)=P(16)U_n(s)+Q(E)r(n+1).
\tag{PD13}
\]

This identity and its bounded implementation are **inherited** from
`bbp_echo_delay_transport.py`. If \(P(16)=0\), the echo is identical
for every seed. For fixed taps its source-only value tends to zero, so
its phase tends to one even when the selected carrier statistics differ.
The elementary echo \(U_{n+1}-16U_n=r(n+1)\) is the sharp control.
It authenticates forcing without authenticating the selected initial
state. Increasing the number of taps does not change the exact algebraic
criterion for erasing that seed coordinate.

If \(m=P(16)\ne0\), removing the known forcing phase leaves
\(z^m\), where \(z=e(hU_n)\). On the whole candidate circle this
recovers \(z\) exactly only for \(m=\pm1\); otherwise it has
\(|m|\) aliases. Multiple demodulated taps with symbols
\(m_1,\ldots,m_k\) recover \(z\) on that candidate circle iff
\(\gcd(m_1,\ldots,m_k)=1\). Bézout coefficients give an explicit
reconstruction \(z=\prod_j(z^{m_j})^{b_j}\), with phase-error budget
\(\sum_j|b_j|\epsilon_j\) for unit-modulus readout errors
\(\epsilon_j\). If the gcd is \(d>1\), multiplication by a
\(d\)-th root of unity is an exact indistinguishable rival. This is
a finite-observable recovery criterion, not a new normality obstruction
for the special radix orbit.

The source-faithful phase echo M02 in the inherited moonshot dossier is
a different construction: its declared coherent reference returns
\(e(hU_n(s))I\), preserving seed dependence. It is therefore not
refuted by the annihilating-tap control. That dossier already records
its exponentially increasing countermodulation frequency. Neither echo
identity proves cancellation of the original phases across time.

For an uncertain seed, \(U_n(s+\Delta)-U_n(s)=16^n\Delta\).
Consequently \(\Delta=1/(2h16^N)\) reverses the \(N\)-th phase,
while the discrepancy at time \(N-k\) is at most \(\pi16^{-k}\).
This is an exact conditioning cost for retaining that seed coordinate,
not a changed-seed refutation of a zero-seed theorem.

## Actual validation and verdict

Executed:

```sh
python -m unittest tests.test_phase_detection
```

**Actual result: 29 tests PASS, exit code zero.** The run includes the
48-case Gaussian-rational response grid, independent finite-product
variance enumeration, five finite-circle sizes, exact propensity
mutations, Bernoulli event-tree enumeration, and twelve original-source
counterseed shell/depth cases. No Monte Carlo or floating-point phase
calculation is used for these verdicts. The code's bounds on shapes,
finite circles, trial powers, shell length, and tail depth are explicit;
the bit cost still depends on the input rational sizes.

| Inference or construction | Verdict |
|---|---|
| Forgotten randomized output is uniform, therefore the original source is uniform | **REFUTED**, locked-source exact finite control and Gamma limit |
| Recorded clock permits exact phase demodulation | **DISCLOSED**, (PD1), (PD5), declared report access |
| Finite-intensity Gamma inversion is automatically stable at every resolution | **REFUTED**, (PD3), (PD4), and all-tests rival-class bound (PD6) |
| Favorable adaptive selection raises the unmodified population event rate | **REFUTED**, exact propensity controls |
| Fresh repetitions amplify a known nonzero event rate | **DISCLOSED**, (PD8)–(PD9) |
| Pointwise positive shell rates imply uniform positive shell escape | **REFUTED**, original-forcing changed-seed control (PD10) |
| Counterseed detection dose grows quartically at fixed confidence | **DISCLOSED**, (PD10)–(PD11), paper proof |
| Recurrence-annihilating taps recover the selected seed | **REFUTED**, inherited identity (PD13) |
| These detector laws prove original-zero shell escape or pi normality | **OPEN**, the required uniform source-specific signed rate is not supplied |

The surviving next obligation is quantitative and source-specific: show
that the authenticated zero-seeded detector law retains a signed response
with a controlled inverse cost, and prove its required event rate on
every sufficiently large shell. A source-frequency tomography theorem
may supply a different positive interface; the detector derivations
above were completed before this adversary read the root's synthesis
of that construction. A probability-one statement
about repeated randomized reports does not by itself change the truth
value or prove the density of a fixed arithmetic property.

## Final bounded review receipt for PC-01–PC-10

**PASS within the stated mathematical domains.** The root synthesis
`THEOREMS.md` was read in full and checked against the detector proofs,
actual module domains, and the inherited GB-12 statement. The initial
reviewed SHA-256 was
`246be441264b34e3c4cf4e86a85f260cd1ac71a2289cf85912c0ebf2ceb550cb`.
The final reviewed SHA-256 is
`03938f2d19125d214ad2e517982365d4f73f33fe8a264a6ef3278741d3021e1b`.

The final text closes the reported guards: the inverse-confidence
formula requires integer `M>=1`; the sampling confidence parameter
satisfies `0<delta<1`; Gamma random clocks are denoted `tau` rather than
reusing the original source's Green-tail symbol `T_n`; and PC-06's
all-scale equivalent target explicitly uses a uniform
`eta<=eta_*<1`.

Specific mathematical checks:

- PC-01 retains `h` after the matched two-tap substitution; its source
  and seed scope agrees with the inherited synthetic-division identity.
- PC-02's polynomial factors give the displayed difference bounds with
  numerator 240 and the adjacent spacing constant `15/(256 B^3)`.
  The block nodes lie in an interval of length less than one half, so
  their circle distances are their ordinary differences.
- PC-03's Gamma–Poisson characteristic modulus, negative-binomial tail,
  and triangular-law modulus give the stated off-diagonal row bounds.
  The Gamma scale and the angular-clock rate in PC-07 are different
  declared parameters, not interchangeable conventions.
- PC-04's whitening gives independent positive matrices bounded by
  `B/(1-eta)`. The quoted Chernoff bound has the correct exponent and
  dimension factor. The rational logarithm overestimate is conservative.
  Summing `1/[B(B+1)]` yields the stated eventual detector-faithfulness
  probability, without requiring independence between different shells.
- PC-05's two-column test proves the lower eigenvalue bound from the
  actual frequency variance. It correctly restricts the cubic-width
  necessity to unrestricted full-vector linear reconstruction.
- PC-06 retains the factors `B/sqrt(l)` and `sqrt(B/l)` in its error
  bounds. The new reference-difference comparison follows from
  `D_B=(c-1)^*G(c-1)/B^2` and `||c-1||^2=2B A_B`. It requires the
  interference cross term; separate energies cannot substitute for it.
- PC-07 agrees with the independent Gamma inverse/MSE derivation and
  the statistical rival-class bound above. Its source densities use
  normalized circle Haar measure and nonzero integer harmonics.
- PC-08's counterseed coefficient is `7*pi^2/98304` for the acceptance
  probability, with the factor of two between escape and acceptance
  retained. Its symbolic source evaluation and finite enclosure are
  compatible with the exact code.
- PC-09 was checked against
  `research/2026-10-27/GLOBAL_BRANCH_COERCIVITY.md`, specifically its
  GB-12 hypothesis and conclusion. A total modulus loss greater than
  `1/14` on `7m` points gives acceptance probability greater than
  `1/(196m)`. The counterseed upper bound has denominator
  `4096*(m+1)^4`; multiplying by the specified dose gives the stated
  fixed-mode `O(log(m)/m^3)` false-hit control. This is a corollary of
  inherited zero-seed arithmetic with an unextracted onset, not a new
  uniform-density estimate or a computed finite threshold.

No remaining substantive defect was identified. The positive finite
frame construction preserves information under its declared readout
model; its conditioning event and universal small detector energy do
not authenticate pi cancellation. The reference-difference criterion is
a calibrated equivalent target until its source-specific lower bound is
proved. PC-09 does distinguish the authentic orbit from the named
counterseed asymptotically, but does not distinguish it from every
nonnormal source or establish the open normality/rung claim.

Production files were frozen after the actual 29-test focused PASS:

| File | SHA-256 |
|---|---|
| `observational_succ/phase_detection.py` | `dad8d4e12261984f323c44958ff5645fee5bb0a46b90d4d1a6d3123d3a556fba` |
| `tests/test_phase_detection.py` | `50523da417dadf41a684be395a1d8e9f66d36e21c9777ef9b60ce0a2233603b8` |

No additional test run is claimed for this prose review. It is not a
formal proof-assistant certificate, a new physical measurement, or an
independent empirical source family. The source-specific irrationality
input and GB-12 retain their inherited paper/classical authority.
