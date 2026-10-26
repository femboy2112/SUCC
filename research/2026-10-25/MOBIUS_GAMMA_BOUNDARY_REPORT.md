# Boundary twists, Gamma, and the zero of a renormalized Euler constant

Date: 2026-10-25 (America/New_York). Parent: PR #297,
`eca4462ee4d62642b15c4af672136aa5bcacd00b`.
Branch: `research/mobius-gamma-boundary-2026-10-25`.

**Result:** the proposed twist has several exact Gamma interpretations. The
same Euler-defect source has ordinary sum gamma and alternating sum
log(4/pi). A logarithmic reference change can set its finite part to zero,
while preserving the conversion constant in the reference. The authentic
BBP forcing has a Gamma primitive, and finite reversed endpoint conditions
have an exact boundary layer. These results do **not** establish signed
BBP cancellation, pi normality, RH, or independence of those problems.

The classical special-function identities are attributed below and in the
companion notes. New means new to this inspected branch, unless explicitly
stated otherwise. Academic priority has not been established.

## 1. What the user's proposal asks us to preserve

The motivating chain was: the order-m^-4 coherence defect tends to zero but
retains a rescaled coefficient; initial zero and zero at infinity select
different solutions; perhaps a Mobius twist connects the two; perhaps Gamma
and Euler--Mascheroni encode that connection. The subsequent observation was
that gamma is a finite difference of two divergences and becomes zero in a
different declared reference.

The strongest faithful mathematical reading is a **boundary comparison with
explicit transition data**. It is not ordinary arithmetic on an undefined
infinity minus infinity. It is not an assertion that a topology alone
forces uniform digit frequencies.

### Hole contract and live frontier

| Field | Exact scope |
|---|---|
| Object | Original r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0, U_n=16U_(n-1)+r(n) |
| Observable | Signed means of e(h U_n), e(x)=exp(2 pi i x), fixed nonzero integer h |
| Established | U_n+T_n=16^n alpha, alpha=pi/16; summable positive T_n; inherited sharp forcing-only m^-4 deficit and tuned controls |
| Open edge | Source-selected signed cancellation, retaining zero initialization and exact cross-time numerators |
| Proposed instrument | Source-preserving twisted boundary response or Gamma-normalized identity involving those actual signed phases |
| Cheapest falsifier | Same forcing with periodic selected seed, zero-forcing seam determinant control, or a source-fixing twist acting trivially on U_n |
| Success | A proved estimate or structural identity that excludes those controls for a stated source/initialization reason |
| Finite boundary | Exact finite certificates prove their domains only; source-tail bounds justify the separately proved limits |
| Novelty tax | Gamma/Lerch coordinates and phase conjugacy are classical reformulations until a new bound is proved |

Live read: PR #297 remained at the parent above and all five returned hosted
workflow runs were successful. Main remained
`1e3a453e869992961bc2d7f3bb6f2f1ddab38854`. New sibling PR #298,
`dc6b87d3b8790f507d2447cc1a24f0ab0d15104f`, was read without merging it:
it removes conductor-birth innovation at a prescribed width and leaves the
conductor-flat selected signed estimate open. Its stronger finite-prefix,
jet and positivity controls are respected here. This branch is stacked on
#297, not a merger of the two research campaigns.

The initial 58-test parent baseline passed. Full validation and reproducible
receipt commands are recorded separately in [validation](MOBIUS_GAMMA_VALIDATION.md).

## 2. Gamma can be zero in a shifted reference: what exactly changes

Let H_N=sum_(n=1)^N 1/n. For a real declared logarithmic offset c, define

$$
g_N(c)=H_N-\log N-c=H_N-\log(e^cN).
$$

Every finite N satisfies g_N(d)-g_N(c)=c-d. Therefore

$$
g(c):=\lim_{N\to\infty}g_N(c)=\gamma-c,
\qquad g(0)=\gamma,\quad g(\gamma)=0.
\tag{N-1}
$$

This is the precise sense in which the user's two zeros are related. The
change is a shift of the logarithmic reference, equivalently a rescaling of
its cutoff by e^c. An ordinary nonzero multiplicative unit conversion of
the already finite number gamma would not send it to zero. Selecting c=gamma
uses gamma in the new reference; it does not independently calculate gamma.

An invariant under this reference change is the **local source defect**

$$
\delta(x)=\frac1x-\log\frac{x+1}{x},\qquad x>0.
\tag{N-2}
$$

Indeed constants cancel from logarithmic increments. The inherited Euler
field E(x)=sum_(k>=0)delta(x+k)=log x-psi(x) obeys
E(x)-E(x+1)=delta(x), E(1)=gamma and E(x)->0 at infinity. Its shifted
version E_c=E-c has the same difference law, E_c(1)=gamma-c, but now
E_c(infinity)=-c. One cannot set both endpoints to zero while keeping
their nonzero difference. **The boundary difference survives the choice
of origin.** See the [inherited Gamma carrier](GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md).

There is also an exact Gamma normalization implementing the shift:

$$
\Gamma_c(z)=e^{c(z-1)}\Gamma(z),\qquad
\psi_c(z)=\psi(z)+c,
$$
$$
\Gamma_c(1)=1,\quad\psi_c(1)=c-\gamma,\quad
\Gamma_c(z+1)=e^c z\Gamma_c(z).
\tag{N-3}
$$

At c=gamma the logarithmic derivative at one vanishes. The successor
normalization has changed by e^gamma. Keeping the standard Gamma recurrence,
normalization and log convexity fixes the standard Gamma function instead;
the precise uniqueness conditions cannot be omitted. These classical inputs
are [DLMF 5.4.12](https://dlmf.nist.gov/5.4.E12) and
[DLMF 5.5](https://dlmf.nist.gov/5.5).

For the BBP Gamma product in section 4, the same change only multiplies the
whole primitive by e^(-15c/8); its rational successor ratio and its balanced
logarithmic derivative stay unchanged. Gamma's appearance in a primitive
must therefore be accompanied by a declared normalization.

## 3. A literal reciprocal Gamma successor, and one source with two sums

For a>0 define

$$
Q(a)=\frac{\Gamma((a+1)/2)}{\Gamma(a/2)}.
$$

The standard Gamma recurrence proves

$$
\boxed{Q(a+1)=\frac{a}{2Q(a)},\qquad
Q(a+2)=\frac{a+1}{a}Q(a).}
\tag{T-1}
$$

One step reciprocates; two steps retain the factor (a+1)/a. A double
twist is not the identity on this weighted source. Its logarithmic derivative
is the alternating harmonic resolvent

$$
F(a)=\frac12\left[\psi((a+1)/2)-\psi(a/2)\right]
=\sum_{n\ge0}\frac{(-1)^n}{n+a},\qquad
F(a)+F(a+1)=\frac1a.
$$

Now apply the sign twist to the **same** absolutely summable source delta:

$$
\boxed{\sum_{n\ge1}\delta(n)=\gamma,\qquad
\sum_{n\ge1}(-1)^{n-1}\delta(n)=\log\frac4\pi.}
\tag{T-2}
$$

The untwisted sum telescopes to H_N-log(N+1). For the twisted sum,
sum (-1)^(n-1)/n=log2 and the alternating logarithm product is pi/2
by Gamma's product/Wallis identity, giving log2-log(pi/2).
The companion [twisted digamma dossier](TWISTED_DIGAMMA_BOUNDARY.md)
proves the general positive-real identity, the Gamma reflection formulas,
and certified finite errors.

There is a complete dyadic hierarchy. Put

$$
A(d)=\sum_{n\ge1}(-1)^{n-1}\delta(dn)
=\frac{\log2}{d}
-\log\frac{\sqrt\pi\,\Gamma(1+1/(2d))}{\Gamma(1/2+1/(2d))}.
$$

For every integer J>=0,

$$
\gamma=\sum_{j=0}^{J-1}2^j A(2^j)
+2^J\sum_{n\ge1}\delta(2^J n),\qquad
0<\text{remainder}<\frac{\zeta(2)}{2^{J+1}}.
\tag{T-3}
$$

Proof: with S(d)=sum delta(dn), the exact parity partition gives
A(d)=S(d)-2S(2d); telescope. The remainder follows from
0<delta(x)<1/(2x^2). Hence gamma is a convergent sum of these dyadic twisted
Gamma expressions, whose first term is log(4/pi). This is a source-preserving
identity and a finite approximation scheme. It is not a digit-normality theorem.

## 4. The actual BBP forcing has a Gamma primitive

Set a=(1/8,1/2,5/8,3/4), w=(4,-2,-1,-1), and

$$
G(x)=\prod_i\Gamma(x+a_i)^{w_i},\qquad x\ge0.
$$

Its exact rational successor quotient is

$$
\frac{G(x+1)}{G(x)}
=\frac{(x+1/8)^4}{(x+1/2)^2(x+5/8)(x+3/4)},
\qquad\frac18\frac{d}{dx}\log\frac{G(x+1)}{G(x)}=r(x+1).
\tag{B-1}
$$

Since sum w_i=0, the constant -gamma cancels from the corresponding
balanced digamma combination. At the primitive level, the canonical Gamma
expansion instead gives

$$
\log G(0)=\frac{15}{8}\gamma+
\sum_{k\ge2}\frac{\zeta(k)}{k}
\left[4(7/8)^k-2(1/2)^k-(3/8)^k-(1/4)^k\right].
\tag{B-2}
$$

All bracketed moments are positive. The inherited exponent-regularized
source B(s)=8^(-s)sum w_i zeta(s,a_i) has B(0)=15/8 and

$$
B'(0)=\log G(0)-\frac{15}{8}\log8.
\tag{B-3}
$$

The [Gamma primitive dossier](BBP_GAMMA_BOUNDARY.md) gives proofs, separate
normalization hypotheses, independent interval constructions, and the exact
distinction between the ordinary tail of r and the base-16 discounted tail T.
Replacing Gamma by Gamma_c multiplies G by e^(-15c/8), because sum w_i a_i
=-15/8. Thus c=gamma removes the explicit gamma term in B-2 from this
renormalized primitive, while B-1 is invariant. B-3 refers to the canonical
Hurwitz normalization, so it must carry the compensating constant if G is
replaced by G_c. One cannot silently change only one side of the identity.

## 5. What a finite Mobius-type seam really selects

For the original forcing and an arbitrary initial value c,

$$
X_n=U_n+16^nc=16^n(c+\alpha)-T_n,\qquad\alpha=\pi/16.
$$

Imposing X_N=lambda X0+beta gives

$$
c=\frac{\beta-U_N}{16^N-\lambda},\qquad\lambda\ne16^N.
\tag{S-1}
$$

The singular case is either inconsistent or underdetermined, according as
beta differs from or equals U_N. The authentic c=0 satisfies the seam
exactly when beta=U_N. The simple sign seam lambda=-1,beta=0 instead gives

$$
c_N=-\alpha+\frac{\alpha+T_N}{16^N+1},\qquad
X_n^{(N)}=-T_n+\frac{16^n(\alpha+T_N)}{16^N+1}.
\tag{S-2}
$$

For fixed n this tends to -T_n. For fixed j>=0, however,
X_(N-j)^(N)->alpha 16^(-j). The boundary layer survives near the moving
endpoint. This is a finite endpoint condition, **not** a proved Mobius-strip
quotient of the nonperiodic dynamics. A global antiperiodic extension would
force r(n+N)=-r(n), contradicting the strictly positive authentic source.

For p=8m+1 prime and N=4m, it also changes the first-birth prime clock:
16^N+1=2 modulo p, and the new primary numerator is 2*16^t rather
than the authentic 4*16^t. Its initial value already contains p-primary
mass. The companion proof derives this for every eligible prime; four
exact holdouts check the implementation. The earlier PRK tuned controls
deliberately preserved that clock, so the two controls must not be conflated.

The projective reciprocal chart y=X+T, J(y)=1/y obeys JFJ=F^(-1) for
F(y)=16y. Reversal is exact, but F does not descend to the naive equivalence
y~1/y. These facts and the generating-function pole are proved in the
[boundary dossier](BBP_TWISTED_BOUNDARY.md). The Mobius strip sign flip and
the projective Mobius inversion are different constructions.

### A new scale distinction: this seam has m^-1 loss, not m^-4

Take N=4m, D=3m, n=m+1,...,4m, and fixed integer h!=0. Define

$$
C_h=\sum_{j\ge0}\left[1-\cos(2\pi h\alpha16^{-j})\right].
$$

Then for the sign-seam states S-2,

$$
\boxed{m\left(1-\left|\frac1{3m}\sum_{n=m+1}^{4m}e(hX_n^{(4m)})\right|\right)
\longrightarrow\frac{C_h}{3}>0.}
\tag{S-3}
$$

**Proof.** Put B_N=(alpha+T_N)/(1+16^(-N)). At n=N-j,
X_n=-T_n+B_N16^(-j). The sum of T_n over this window is less than
1/(64m). Moreover B_N->alpha, and the geometric series sum16^(-j)
converges. The Lipschitz inequality |e(u)-e(v)|<=2pi|u-v| therefore proves

$$
\sum_{n=m+1}^{4m}(e(hX_n)-1)
\longrightarrow Z_h:=\sum_{j\ge0}(e(h\alpha16^{-j})-1).
$$

The mean is 1+(Z_h+o(1))/(3m). Expanding its modulus around1 gives
S-3 because -Re Z_h=C_h. The series is absolutely convergent; each C_h
summand is nonnegative, and eventually 0<|h alpha16^(-j)|<1, so at least
one is strictly positive. This proves the strict coefficient without a
decimal approximation of alpha. QED.

For a fully finite budget, let A be a rational upper bound on alpha,
b_N=1/[(8N+1)(8N+2)], and

$$
\epsilon_m=\frac{44|h|}{7}
\left[\frac1{64m}+\frac{16}{15}
\left(b_{4m}+A16^{-4m}+A16^{-3m}\right)\right],
\quad M_m=\frac{44|h|}{7}\frac{16A}{15}+\epsilon_m.
$$

The preceding complex-sum error is at most epsilon_m. If 2M_m<=3m,
Re(mean)>=1/2 and |z|-Re(z)=(Im z)^2/(|z|+Re z) yields

$$
\left|m(1-|\text{mean}|)-C_h/3\right|
\le\epsilon_m/3+M_m^2/(9m).
\tag{S-4}
$$

The new [exact module](../../observational_succ/bbp_twist_boundary_layer.py)
certifies C_h and this bound using rational source-tail and character
enclosures. The inherited PRK changed-initial controls tune away this
terminal layer more accurately and genuinely have order m^-4 loss. These
are different control families; pointwise convergence to the same bounded
solution does not identify their moving-window asymptotics.

More generally fixed lambda,beta give the same S-3 with alpha replaced by
b=beta-lambda alpha, provided b!=0. If b=0, the residual terminal correction
is of size m^-2 and the inherited bulk profile yields the m^-4 coefficient
3pi^2h^2/131072. With rational fixed lambda,beta, b=0 forces lambda=beta=0,
by irrationality of alpha. This statement uses fixed seam parameters;
N-dependent tuned controls require their own error estimates.

## 6. q-Gamma is present in the seam denominator

With q=1/16 the normalized S-1 denominator is 1-lambda q^N. Its finite
product over horizons in the sign case is

$$
\prod_{N=1}^M(1+q^N)=\frac{(q^2;q^2)_M}{(q;q)_M}.
$$

For P_q(a)=product_(n>=0)(1+q^(n+a)), a>0, the q-Gamma definition gives

$$
\frac{P_q(a)}{P_q(1)}
=(1+q)^{1-a}\frac{\Gamma_q(a)}{\Gamma_{q^2}(a)}.
\tag{Q-1}
$$

The [q-Gamma dossier](QGAMMA_SEAM_DETERMINANT.md) supplies finite rational
product bounds, the neighboring q-Euler constant converging to gamma, and
the classical modular small/large-parameter identity. The sign-twisted
limiting derivative is -log2; the gamma terms cancel. A q->1 limit changes
the recurrence multiplier; the authentic q is fixed at1/16.

These products are an explicitly chosen aggregation of seam coefficients,
not an established determinant of a single infinite source operator. They
are unchanged by setting r=0, and that zero-source orbit can be constant.
Their source-specific numerator beta-U_N must be retained.

## 7. What survives the hostile audit, and the next cut

The [hostile audit](MOBIUS_GAMMA_HOSTILE_AUDIT.md) classifies every affine
source symmetry. Its source-fixing conclusion is more general: for **any**
maps H_n satisfying H_(n+1)F_n=F_n H_n and H_0(U_0)=U_0, induction gives
H_n(U_n)=U_n. No linearity, continuity or invertibility of H_n is needed.
For the invertible BBP real flow P_n(x)=U_n+16^n x, all such families are
H_n=P_n H_0 P_n^(-1). Thus merely making the same time-preserving,
source-commuting twist nonlinear cannot pair distinct authentic observations.
This is an elementary consequence of deterministic equivariance, not a new
general rigidity theorem. Reflection of a circle phase supplies a complex
conjugate, not generally its negative.

Three candidate reframes were tested:

| Candidate | Earned result | Remaining boundary |
|---|---|---|
| Twisted boundary problem | Exact selector and new terminal-layer asymptotic | Replaces U0=0 unless seam is authenticated |
| Gamma/alternating Euler source | Reciprocal Gamma law, gamma/log(4/pi) identity, dyadic certificates | Source statistics are not orbit statistics |
| q-Gamma seam denominator | Exact products, classical modular duality and finite parts | Erases forcing entirely |

The chosen useful change of object is the **joint source-and-boundary
response**, retaining numerator and denominator, plus its bulk and endpoint
observables. It explains why identical pointwise limits can have different
coherence scales, and why a normalization constant can disappear from one
readout while remaining in its conversion map. It dominates the informal
gluing picture for these questions, not for proving normality.

The next genuine cancellation instrument must mix times or otherwise leave
the class of source-fixing pointwise equivariant maps, while keeping exact
U0=0. A sufficient new theorem could bound authentic off-diagonal Fourier
correlations in that enlarged class; no such bound is established here.
Merely restating a Weyl sum, Gamma quotient, or seam numerator does not pay
the novelty tax. No claim of a logical impossibility or need for new axioms
is made.

The earlier analogy with zeta(-1) is retained only in its precise form:
sum n exp(-epsilon n)=epsilon^(-2)-1/12+O(epsilon^2), and a declared finite
part is -1/12. Likewise m^4 times the PRK control deficit has a nonzero
limit. Neither operation converts an undefined infinity into an ordinary
number, nor transfers the control asymptotic to the authentic trajectory.
