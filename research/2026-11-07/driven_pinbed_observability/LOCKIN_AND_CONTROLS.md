# Driven pin bed: adversarial controls and constructive repairs

Research date: 2026-11-07. Independent bounded adversary assignment for the
oscillator continuation of SUCC PR541 and the finite oscillator note PR542.
These are written elementary proofs plus a separately specified finite oracle.
No source-selected cancellation, physical implementation, scholarly priority or
formal kernel verification is claimed.

## 0. Prospective finite oracle scope (written before executing the oracle)

Use the four-site circle with exact Gaussian rationals, primitive root i,
proper window lengths L=1,2,3, target characters h=1,2,3 and source states
x=0,1,2,3. Enumerate all reference centers y=0,1,2,3. Check every source word
of length N=1,2,3 against every reference word of the same length. Fresh longer
words are (0,1,1,2,3), (3,0,2,2,1), (1,3,0,3,2); enumerate all 4^5 reference
words for each. Test uniform, delta_0, (1,2,3,4)/10, and (5,3,2,7)/17 laws
against constant complex gains 3/5+4i/5 and -7/5+2i/3. Controls: erased clock,
wrong demodulation sign, erased demodulation, omitted normalization, power-only
readout and phase-cycle measurements from changed source snapshots. The exact
counts and outcomes will be appended after execution.

## 1. Declared objects and access

Write T=R/Z and e(t)=exp(2*pi*i*t). Fix 0<alpha<1. The forward window profiles
of a probability law mu are

R_k mu(y) = (1/alpha) integral_[0,alpha) e(-k*s) dmu(y+s), k=0,1.

The formula for a measure means the translated kernel integral, so for an atom
at x it is (1/alpha) 1_{[0,alpha)}({x-y}) e(-k*{x-y}). Endpoints are immaterial
to L2 profiles. The Fourier convention is m_h(mu)=integral e(-h*x) dmu(x).
Set c_alpha(r)=(1/alpha) integral_0^alpha e(r*s) ds. Fubini gives

Fourier[R_k mu](h) = c_alpha(h-k) m_h(mu).

Let a_h=(c_alpha(h),c_alpha(h-1)) and S_h=|a_h|^2. The two-channel distance is
the sum of the two L2 squared profile differences. Since laws are real,
negative source Fourier moments are conjugates; S_h need not individually be
symmetric. One can replace S_h by (S_h+S_-h)/2 without changing the distance on
real law differences. Any statement about arbitrary complex profiles must
retain the unsymmetrized weights.

Two readings of the driven complex channel mean two quadratures of the SAME
source snapshot with a common reference. The full translated profiles are
stronger access than one collector reading at one actual source time.

## 2. An unknown constant oscillator phase can self-calibrate

**Theorem A (exact constant-gain calibration).** Suppose all translated driven
readings are available and the measured profile is Y_1(y)=g R_1 mu(y), with
one fixed complex g and known total source mass one. Then

g = integral_T Y_1(y) dy / c_alpha(-1).

The denominator is nonzero for every 0<alpha<1 because
|c_alpha(-1)|=sin(pi*alpha)/(pi*alpha)>0. Thus any nonzero constant gain and
phase are recoverable, and division by g recovers the coherent channel.

Proof: integrating R_1 over y gives c_alpha(-1) times the source mass, by
Fubini. The formula follows. A zero gain is detected, but the lost channel
cannot then be reconstructed.

Finite version: for R_{L,1} of PR542, sum_y R_{L,1}v(y)=H_L(-1) sum_x v(x),
and H_L(-1) is nonzero for every proper integer window 1<=L<m.

**Noise certificate.** If Y_1=g R_1 mu+eta and ||eta||_2<=epsilon, then the
same estimator satisfies |g_hat-g|<=epsilon/|c_alpha(-1)|=:d_g. If |g|>d_g,

||Y_1/g_hat-R_1 mu||_2
 <= epsilon*(1+1/(|c_alpha(-1)|*sqrt(alpha)))/(|g|-d_g).

This follows from Cauchy-Schwarz for the mean error, the triangle inequality,
and ||R_1 mu||_2<=||1_[0,alpha)/alpha||_2=alpha^(-1/2).

**Boundary.** A constant instrument phase is different from an unknown spatial
origin or a time/position-dependent reference phase. Mean normalization does
not calibrate arbitrary g(y), nor reveal a missing coordinate origin. The
aperture endpoint alpha=1 is excluded: c_1(-1)=0. Complex quadratures must
still be available; replacing the output by its modulus erases information.

**Realizable drift control.** On G4 with L=2, let p_even=(1/2,0,1/2,0)
and p_odd=(0,1/2,0,1/2). Their static profiles both equal 1/2. Their coherent
profiles are (1/2,-i/2,1/2,-i/2) and (-i/2,1/2,-i/2,1/2).
Multiplying the first profile pointwise by g(y)=-i*(-1)^y produces the second.
Both profiles have the same mean, so the constant-gain estimator returns one.
The altered pair passes range/positivity checks because it realizes a different
probability law. Thus realization alone does not authenticate a spatially
varying instrument. The executable expected-snapshot comparison rejects this
substitution. This is a derived hostile case, not a source holdout.

## 3. Sequential coherent lock-in for an authenticated moving source

This addresses an access gap left by full-profile reconstruction: at source
time n one may have only one translated collector position, while the source
continues evolving.

Let x_1,...,x_N be any deterministic authenticated source phases, with no
assumption of uniform distribution. Choose Y_n independently and uniformly on
the circle, independently of the source. At the SAME actual source time n,
read r_{n,k}=R_k delta_{x_n}(Y_n), k=0,1, keeping the reference position Y_n.
For a fixed integer h and S_h>0 define

Z_{n,h} = e(-h*Y_n) [conj(a_{h,0}) r_{n,0}
                         +conj(a_{h,1}) r_{n,1}] / S_h.

**Theorem B (unbiased authenticated lock-in).**

E[Z_{n,h} | x_n] = e(-h*x_n),

and therefore Zbar_h=N^(-1) sum_n Z_{n,h} is an unbiased estimator of the
actual finite source Weyl mean m_{N,h}=N^(-1) sum_n e(-h*x_n).

Proof: the Fourier identity in section 1 says
E[e(-h*Y_n) r_{n,k} | x_n]=a_{h,k} e(-h*x_n). Multiply by the conjugate
coefficients, sum and divide by S_h. This conditions on the actual source;
the law being estimated is never the observer clock's distribution.

**Exact second moment for a point source.** Put a=c_alpha(h), b=c_alpha(h-1),
c=c_alpha(1), S=|a|^2+|b|^2. A change of variable s={x_n-Y_n} gives

Q_h := E|Z_{n,h}|^2
     = [ S + 2 Re(conj(a)*b*c) ] / (alpha*S^2),

independent of x_n. Consequently Q_h>=1 and

E|Zbar_h-m_{N,h}|^2=(Q_h-1)/N <= [2/(alpha*S_h)-1]/N.

The upper bound follows either from the integral formula or Cauchy-Schwarz:
|conj(a)r_0+conj(b)r_1|^2<=S(|r_0|^2+|r_1|^2), whose reference average is
2S/alpha. Cross terms from distinct n vanish because the centered errors are
independent and mean zero.

**Finite confidence bounds.** For epsilon>0,

P(|Zbar_h-m_{N,h}|>=epsilon) <= min(1,(Q_h-1)/(N*epsilon^2)).

Also |Z_{n,h}|<=B_h=sqrt(2)/(alpha*sqrt(S_h)), so separate real and imaginary
Hoeffding bounds and a union bound give

P(|Zbar_h-m_{N,h}|>=epsilon)
 <= min(1,4 exp(-N*epsilon^2/(4*B_h^2))).

These are probabilities of measurement error under the declared random
reference protocol, not probabilities that the source property is true. No
finite N proves all-epoch arithmetic cancellation. A frame bound
S_h>=c_alpha'/(1+h^2) implies O_alpha((1+h^2)/N) mean square error.

The variance conclusion also holds if x_n is measurable with respect to past
readings and Y_n is freshly independent of that past, since the centered errors
are martingale differences with the same pointwise conditional variance. The
source must be determined before its current reference choice; a drive that
changes the contemporaneous source state violates this access assumption.

**Finite exact analogue.** On G_m with unnormalized window R_{L,k}, let
a=(H_L(h),H_L(h-1)), S=|a|^2. For Y uniform on G_m,

Z_h(x;Y)=m*zeta_m^(-hY)*(conj(a_0)R_{L,0}delta_x(Y)
                            +conj(a_1)R_{L,1}delta_x(Y))/S.

Its expectation is zeta_m^(-hx). Its point-source second moment is
m/S^2 times sum_{j=0}^{L-1}|conj(a_0)+conj(a_1)zeta_m^(-j)|^2,
at most 2mL/S. It is independent of x, so the same exact variance-addition
formula holds for an arbitrary deterministic source word.

**Physical/source boundary.** Uniform reference positions and simultaneous
quadratures are explicit capabilities. A deterministic oscillator is not
automatically an independent random reference. On a finite clock, enumerating
all reference positions gives an exact mathematical mean; replaying all of them
at each source state requires frozen/reproducible snapshots. If the real source
moves while the phase cycle runs, one needs either simultaneous channels,
authenticated replay, or a separately proved drift bound.

## 4. Erasing the reference clock can manufacture apparent uniformity

**Exact finite control.** On G_4 take source x=(0,0,0,0), reference
theta=(0,1,2,3), and relative coordinates z=x-theta=(0,3,2,1). The relative
empirical law is exactly uniform, whereas the actual source is delta_0. Every
nonzero finite character has relative mean zero and source mean one.

The same relative data z arise from source x'=z and reference theta'=0. Thus
the erased-clock observation has both a uniform-source and a locked-source
realization. The scoped relative truth is valid; the original source target
does not descend through that erased-clock map.

**Positive repair.** Keep the pair (z_n,theta_n) and transport characters back:

e(-h*z_n)*e(-h*theta_n)=e(-h*x_n).

This holds pointwise, so no independence, asymptotic limit or typicality is
needed for the transport identity. Probability enters only if one uses the
sampling protocol of section 3.

A continuous version uses x_n=0 and theta_n=n*beta for irrational beta; the
rotating observer's relative phases are equidistributed while the source
remains a fixed atom. This is a counterexample to promoting observer scanning
to source normality, not a counterexample to the driven measurement theorem.

## 5. One missing quadrature is NOT a universal failure witness

Power-only observation loses phase, as PR542 shows. But losing one quadrature
does not automatically destroy injectivity when ALL translated profiles remain
available. Let R_cos=(R_1+R_-1)/2 with multiplier
b_h=(c_alpha(h-1)+c_alpha(h+1))/2.

If the static channel loses a nonzero h, then h*alpha is an integer. Such h
cannot be +/-1 for proper alpha. Writing theta=2*pi*alpha, direct simplification
gives

b_h = [h*(cos(theta)-1)-i*sin(theta)] /
      [2*pi*i*alpha*(h^2-1)].

Its numerator has nonzero real part h*(cos(theta)-1), so b_h!=0. Hence static
+ one real cosine-modulated FULL profile is already injective. Spatial
translations themselves retain phase. The two-quadrature complex protocol is
a clean sufficient construction and permits the first-order differential
inverse; it should not be advertised as the unique minimal access design.

## 6. Exact covariance and authentic BBP transport

For d in [0,1], let

A_alpha(d)=[(alpha-d)_+ +(alpha-(1-d))_+]/alpha^2,
C_alpha(d)=A_alpha(d)*(1+cos(2*pi*d)).

The first expression is the overlap autocorrelation of the normalized interval
kernel. The complex two-channel covariance is A_alpha(d)*(1+e(-d)); for real
law pairs the imaginary part cancels, leaving C_alpha.

For mu a probability, define centered energy E_alpha(mu)=sum_{k=0,1}
||R_k mu-R_k lambda||_2^2. Then

E_alpha(mu)=integral integral C_alpha(x-y) dmu(x)dmu(y)
            -[1+|c_alpha(1)|^2].

The real C_alpha is circle-Lipschitz with

L_alpha=2/alpha^2+2*pi/alpha.

Indeed A_alpha is piecewise linear, bounded by 1/alpha, and has circle
Lipschitz constant 1/alpha^2; the product bound gives the assertion.

If gamma couples mu,nu and delta_bar=integral d_T(x,y) dgamma, independent
copies of gamma and the triangle inequality imply

|E_alpha(mu)-E_alpha(nu)| <=2 L_alpha delta_bar.

Also the point-profile squared distance is

D_alpha(delta_x,delta_y)^2
 =4/alpha-2 A_alpha(d_T(x,y))*(1+cos(2*pi*d_T(x,y)))
 <=2 L_alpha d_T(x,y).

Jensen in the Hilbert space of two profiles therefore gives

D_alpha(mu,nu)^2<=2 L_alpha delta_bar.

For the authentic zero-seeded BBP epoch [A,2A), PR541's proved original-to-pi
tail gives delta_bar<=1/(30 A^2). Hence BOTH

|E_alpha(mu_A^U)-E_alpha(mu_A^pi)| <=L_alpha/(15 A^2),
D_alpha(mu_A^U,mu_A^pi)^2 <=L_alpha/(15 A^2).

The corresponding norm rate is O(A^-1). The distinction is load-bearing:
for small d<=min(alpha,1-alpha), A_alpha(d)=(alpha-d)/alpha^2 and

D_alpha(delta_0,delta_d)^2
 =4d/alpha^2 +2(alpha-d)*(1-cos(2*pi*d))/alpha^2
 =4d/alpha^2+O_alpha(d^2).

Thus the general norm has a square-root translation modulus. Importing the
smooth B2 bed's O(A^-2) norm transport into the driven rectangular bed would
require extra source structure. The O(A^-2) ENERGY transport is valid.

## 7. Access ledger and verdict

PROVED LOCAL: constant-gain self-calibration on full proper-window profiles;
unbiased sequential coherent lock-in with explicit source-independent finite
variance; erased-clock countermodel and exact registered-clock repair;
single-cosine qualification; covariance and BBP transport bounds.

UNVERIFIED until genuinely implemented: a physical instrument supplying the
declared channels, registered reference and random sampling access. A passive
mathematical observer does not authorize interventions in the authentic BBP
source. Common additive linear forcing still cancels from differences, exactly
as in PBFO-09. The new positive access comes from multiplying/probing with
spatially varying oscillatory masks and retaining the reference.

OPEN: original-source all-epoch driven energy decay and pi base-16 normality.
No finite random measurement guarantee, global profile inverse, or stable
observer quotient supplies that arithmetic estimate by itself.

## 8. Executed independent finite receipt

The independently written standard-library program
`independent_lockin_oracle.py` completed with exit code 0. Its JSON receipt is
`INDEPENDENT_LOCKIN_RECEIPT.json`. The program imports no SUCC module and uses
its own Gaussian-rational arithmetic and explicit four-site roots.

- 36 pointwise unbiasedness checks and 36 exact second-moment checks pass.
- 48 four-phase reconstructions pass; all 192 constituent mask weights are
  nonnegative.
- All 783 predeclared source words pass exact mean and variance identities,
  after enumerating 66,960 source/reference word pairs.
- 24 constant complex-gain calibration cases pass.
- Seven deliberately broken inferences/implementations are rejected with
  concrete witnesses: erased reference; reversed reference; omitted finite
  normalization; power-only estimator; erased-clock false uniformity;
  equal-power/unequal-phase full profiles; changed source during phase cycle.

Single-sample variances are exactly 3 for all L=1 cases, 11/9 for (L,h)=(2,1),
11/25 for (3,1), and 3 for the other tested pairs. In particular the purely
static-blind h=2,L=2 mode is unbiased under the coherent driven protocol and
has exact variance 3/N over N independent reference choices.

Oracle SHA256:
`70101ff53127e0f3caf3563d48f83b6deb8b1bd586c93cfb8567d480a34950e1`.

The all-parameter statements above rest on their derivations; this finite run
does not supply an infinite lift. The original BBP tail used in section 6 was
checked directly against PR541's committed theorem dossier section 9.
