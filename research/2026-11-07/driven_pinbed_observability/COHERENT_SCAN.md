# Source-authenticated coherent scanning of the B2 pin bed

**2026-11-07. Translator bearing.** Written derivations below are PROVED LOCAL
after root audit of signs, quantifiers, alias tails and source transport. No novelty priority or source-selected cancellation is
claimed. This note reads PR541 and the published PR542 note, not other new
agent notes. All source estimates preserve the original four signed BBP poles
and U0=0. The source engine and historical research files are unchanged.

## 1. The measurement object and the hole actually closed

Let mu be a circle probability, m_h(mu)=integral exp(-2*pi*i*h*x) dmu(x), and
F_mu=B2*mu be PR541's centered quadratic surface. The profile is fixed during
the measurement protocol. An M-step oscillator visits t_j=j/M and a coherent
reference retains both quadratures of exp(-2*pi*i*h*j/M). Define

    Y_(M,h)(mu) = (1/M) sum_(j=0)^(M-1) F_mu(j/M) exp(-2*pi*i*h*j/M),
    Z_(M,h)(mu) = 2*pi^2*h^2 Y_(M,h)(mu).

This is a finite spatial scan of a fixed law, or an exact computation on a
retained empirical source history. It is NOT one moving reading per changing
source state. It does not change the source seed, force the carrier, or assume
that a physical device can reset an invasive source. A pin can be moved, or the
whole recorded profile can be multiplied by the reference oscillator.

The new edge is a certified finite sampling map from PR541's exact rational
surface to signed source Fourier modes. PR542's finite binning estimate is
linear in |h|/M; this construction has a quadratic alias bound h^2/M^2, at the
cost of measuring the continuous B2 profile and retaining coherent phase.
This comparison is of different declared observation protocols.

## 2. Exact alias theorem, including its sharp worst case

**Theorem S1.** For every probability mu, integer M>=2, and integer h with
0<|h|<=M/2,

    Z_(M,h)(mu)
      = h^2 sum_(ell in Z) m_(h+ell*M)(mu)/(h+ell*M)^2.

Consequently the exact optimal universal error radius is

    a(M,h) = h^2 sum_(ell != 0) 1/(h+ell*M)^2
           = (pi*h/M)^2 csc^2(pi*h/M) - 1,

and

    |Z_(M,h)(mu) - m_h(mu)| <= a(M,h)
       <= (pi^2-4) h^2/M^2 < 6 h^2/M^2.

The first radius is sharp: equality holds for delta_0, and for any atom at a
scan-grid point a/M, all aliases have the same phase as the target mode.

*Proof.* PR541 gives Fhat_mu(q)=m_q(mu)/(2*pi^2*q^2), q!=0. This series
converges absolutely and uniformly, since |m_q|<=1. Substitute it into the
finite scan and apply exact root-of-unity orthogonality: only q=h+ell*M
survives. Here q is never zero. Removing ell=0 and bounding |m_q|<=1 gives
the error sum; delta_0 makes every term positive and attains it. The csc^2
partial fraction identity is NIST DLMF 4.22.4. Set x=|h|/M in (0,1/2]. Then

    sum_(ell != 0) 1/(ell+x)^2
      = sum_(ell>=1)[(ell-x)^(-2)+(ell+x)^(-2)]

is increasing in x, term by term. At x=1/2 it equals pi^2-4. Multiplying by
h^2/M^2 proves the second bound. Finally pi^2<10 (e.g. pi<22/7).

The simple rational bound is useful for exact receipts; the analytic sharp
radius is useful when tighter certified trigonometric evaluation is available.

**Exact finite calibration identity.** For zeta=exp(-2*pi*i*h/M) != 1 and
mu=delta_0, the rational cyclotomic sample coefficient satisfies

    M^2 (1-zeta)^2 Y_(M,h)(delta_0) + 2*zeta = 0.

Thus the sharpness calibration can be checked without floating-point roots
or using pi as a numerical input. The oracle uses an independent elementary
prime-cyclotomic quotient for this check.

## 3. The DC scan counterfeit, and an exact phase requirement

**Theorem S2.** For every circle probability mu and every M>=1,

    (1/M) sum_j F_mu(j/M) = M^(-2) F_((x->Mx)_*mu)(0).

In particular its absolute value is at most 1/(6M^2). For delta_0 it is exactly
1/(6M^2), although delta_0 is maximally locked and not Haar.

*Proof.* Bernoulli multiplication gives (1/M)sum_j B2({j/M-x})
=M^(-2)B2({-Mx}); integrate against mu. The periodic B2 is even and has
absolute value at most 1/6.

Therefore a vanishing scan average occurs uniformly for every source law.
Reporting it as source equidistribution would be vacuous. Coherent demodulation
at nonzero h retains the signed mode, while averaging away the oscillator
reference destroys that information. A simple sign mutant is delta_(1/4):
the h=1 mode is -i, while using the conjugate reference estimates +i.

For bounded per-sample additive errors |e_j|<=epsilon, the extra mode radius is
2*pi^2*h^2*epsilon. Position errors at most delta add the same expression with
epsilon replaced by delta, because periodic B2 and every F_mu are 1-Lipschitz.
Reference-phase errors need their own calibration bound; they are not folded
silently into a source estimate.

## 4. Authentic BBP transfer into the finite oscillator readout

Keep r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0 and
Un=16 U_(n-1)+r(n). Let

    T_n = sum_(j>=1) 16^(-j) r(n+j),
    x_n={U_n}, z_n={U_n+T_n}={16^n*pi/16}.

PR541 proves 0<T_n<1/[15(n+1)^2], n>=1. Let mu_A^U and mu_A^z average
n=A,...,2A-1. Since a character is 2*pi*|h|-Lipschitz,

    |m_h(mu_A^U)-m_h(mu_A^z)|
      <= (2*pi*|h|/A) sum_n T_n
      <= pi*|h|/(15 A^2).

**Theorem S3.** For all integer A>=1, M>=2 and 0<|h|<=M/2,

    |Z_(M,h)(mu_A^U)-m_h(mu_A^z)|
      <= a(M,h) + pi*|h|/(15 A^2)
      < 6h^2/M^2 + 22|h|/(105 A^2).

All B2 sample heights are exact rationals from the original BBP source. The
finite oscillator coefficient is cyclotomic, multiplied by 2*pi^2*h^2; sound
rational enclosures of pi and the reference phases give a fully finite error
certificate. The oracle evaluates trigonometric quantities by a proved Machin
interval and rational Taylor remainders, not floating tolerances.

If a measured coefficient has modulus exceeding this radius by eta>0, the
corresponding completed-pi epoch mode has modulus at least eta. Conversely
its modulus is at most the measured modulus plus this radius. These are
actual finite threshold-target certificates. Proving the measured modes tend
to zero on every sufficiently large source epoch remains an OPEN arithmetic
estimate. Changing M with A improves instrument resolution; it does not
supply source cancellation.

### Same-forcing deterministic controls

The exact coherent wrong seed s_*=-pi/16 gives

    U_n(s_*)=-T_n,

so its completed orbit is identically zero and its character average tends to
one. This follows from T_n=16 T_(n-1)-r(n), with T_0=pi/16. For every A,h,

    |m_h(mu_A^(s_*))-1| <= pi*|h|/(15 A^2),

and the same finite scan has |Z-1| bounded by the radius in S3. It is a strong
negative normality control, not an admissible replacement for U0=0.

For an entirely rational finite control, choose one fixed K before running and
s_K=-sum_(j=1)^K 16^(-j)r(j). For every n<=K,

    U_n(s_K)=-sum_(j=1)^(K-n) 16^(-j)r(n+j).

This is an exact same-forcing history, rejected at the initial-state check.
On every epoch ending before K it obeys the same upper proximity-to-zero
bound, because each finite tail is below T_n. The oracle uses the single fixed
K=154 across all of its fresh A=19,37,73 epochs; it does not select a new seed
for each individual reading.

## 5. Rectangular oscillator channels: source norm versus source energy

For 0<alpha<1 and integer k define the forward-window readout

    R_(alpha,k)mu(t)=(1/alpha) integral_(x-t mod1 in [0,alpha))
                         exp(-2*pi*i*k*(x-t)) dmu(x).

Let d be geodesic displacement in [0,1/2] and
J_alpha(d)=alpha-min(d,alpha,1-alpha), the overlap of two length-alpha arcs.
Direct integration gives the exact point-translation formula

    ||R_(alpha,k)delta_x-R_(alpha,k)delta_y||_2^2
      = 2/alpha - (2 J_alpha(d)/alpha^2)cos(2*pi*k*d)
      <= 2d/alpha^2 + 4*pi^2*k^2*d^2/alpha.

Jensen applied to the same-index coupling of two source epochs gives

    ||R_(alpha,k)mu_A^U-R_(alpha,k)mu_A^z||_2^2
      <= 1/(15 alpha^2 A^2) + 7*pi^2*k^2/(1350 alpha A^4).

The second constant uses
(1/A)sum T_n^2 <= [1/(225A)] integral_A^(2A)t^(-4)dt
=7/(5400A^4). For the k=0,1 vector, add these squared channel bounds:

    ||R_vec(mu_A^U)-R_vec(mu_A^z)||_2^2
      <= 2/(15 alpha^2 A^2)+7*pi^2/(1350 alpha A^4).

This is O(A^-1) in the vector norm, not O(A^-2). The nonsmooth aperture edges
cost a half-power relative to PR541's quadratic surface norm.

For the centered channel energy E_(alpha,k)(mu)=||R_(alpha,k)mu-R_(alpha,k)lambda||_2^2,
the real covariance kernel is J_alpha(d)cos(2*pi*k*d)/alpha^2. It has circle
Lipschitz constant at most L=alpha^(-2)+2*pi*|k|/alpha. Therefore

    |E_(alpha,k)(mu_A^U)-E_(alpha,k)(mu_A^z)|
      <= (alpha^(-2)+2*pi*|k|/alpha)/(15 A^2).

This is an O(A^-2) bound on the difference of squared norms (energies), a
different statement. For a drive bank with nonnegative budgets beta_k, these
bounds sum with the corresponding zeroth, first or second frequency moment
sum beta_k, sum beta_k|k|, sum beta_k k^2. Growing drive bandwidth must retain
those budgets; a finite-tone statement is not a free infinite oscillator bank.

In particular, for any finite bank depending on A with beta_k>=0, sum beta_k=1,
and |k|<=K_A, the squared profile error is at most

    1/(15 alpha^2 A^2)+7*pi^2*K_A^2/(1350 alpha A^4),

and the energy difference is at most
(alpha^(-2)+2*pi*K_A/alpha)/(15 A^2). Thus normalized banks with K_A=o(A^2)
retain vanishing authentic-to-completed source error. This is a proved uniform
transport window; it is not a claim that either bank energy itself tends to zero.

## 6. Exact finite cyclic readout is a continuum energy calibration

Suppose alpha=L/M and mu_v=sum_(x=0)^(M-1)v_x delta_(x/M). With the finite
profile of PR542,

    R_(L,k)v(y)=sum_(j=0)^(L-1)v_(y+j) zeta_M^(-k*j),

one has exactly

    ||R_(alpha,k)mu_v||_2^2
      = [1/(M alpha^2)] sum_y |R_(L,k)v(y)|^2.

Between successive grid breakpoints the continuous readout is the matching
finite window response times a unit phase and 1/alpha; its squared modulus
is constant. Integrating those M intervals proves the formula. To obtain the
centered energy subtract |R_(alpha,k)lambda|^2, where the k=0 value is 1 and
for k!=0 the value is [sin(pi*k*alpha)/(pi*k*alpha)]^2.

The oracle checks this independently as a rational group-ring identity:
window-intersection counts versus exact spatial arc overlap coefficients.
No evaluation of a trigonometric root is needed for that equality. Finite
cyclic uniformity is still distinct from circle Haar: the k=1 continuum
channel sees the high-frequency grid residual.

## 7. Predeclared finite probes and provenance

Before the oracle runs: prime scan moduli 2,3,5,7,11,17,29; all nonzero
positive modes up to half each modulus for the delta calibration; selected
grid translations; cyclic windows on M=3,5,7,11; fresh original BBP epochs
A=19,37,73 paired with M=11,17,29 and h=1,2,3; one fixed rational wrong seed
with K=154. Bad phase sign, missing scan normalization and missing h^2 gain
are deliberate mutants. No values in these fresh epochs were used to derive
the inequalities. All finite results are OBSERVED EXACT/ENCLOSED only after
the oracle succeeds.

Primary identities checked live: NIST DLMF 24.8.1/24.8.3 for B2 Fourier
coefficients, https://dlmf.nist.gov/24.8 ; NIST DLMF 4.22.4 for csc^2 partial
fractions, https://dlmf.nist.gov/4.22.E4 . These are classical antecedents.
The scan derivation and source transport are written above. Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239) follows by the tangent addition law and the
quadrant; alternating arctangent sums and Taylor remainder bounds certify
the oracle's rational intervals.

**Boundary:** finite coherent oscillator access and source-to-model transport
are disclosed by the stated derivations. Source-selected all-epoch signed
decay, pi base-16 normality and RH remain OPEN.

## Executed receipt (after derivation and case selection)

`independent_scan_oracle.py` completed with exit 0 and **582 checks**:
34 exact sharpness identities, 157 exact grid-phase transports, 198 exact
finite/continuum energy identities, seven locked-atom DC controls, nine fresh
original-source alias enclosures, nine completed-pi transport enclosures, nine
fixed-wrong-seed lock controls, 154 exact same-forcing transitions, initial-seed
rejection, a positive quadrature calibration and three rejected mutants.
The raw JSON is `INDEPENDENT_SCAN_RECEIPT.json`.

Oracle SHA256: d4159f4a16ad05ce281404e49455ddf570e9324b3dd25d6f7d82cfe7d5176bd4.
The independently generated U0 through U154 were also compared directly to
SUCC's integer conductor engine: **155/155 exact state values agree**. The
canonical rational source-string SHA256 in both routes is
49b2d2d8c05827389fddf521ecdfd51b1fa767938707e3fe9502e7403c0ffde9.
This separate engine comparison is not included in the 582 oracle checks.

The oracle's pi interval is produced by Machin's identity solely to calibrate
the observer's trigonometric references/gain. No pi digits enter the source
construction. It encloses pi between 3.1415926535897932384626 and
3.1415926535897932384627 at the displayed precision.
