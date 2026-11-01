# Operation MOONSHOT: exact source phase echoes, quantum resolution and signed holdouts

**2026-11-01. Research-only; paper proofs, not Lean or externally refereed.** Parent PR444
is pinned at `661553f182c425b06b5339ed02d7739a0ae72380`; Main XVIII was
`4eb411e3730a9e7b95480369a438b89d9a433a4b`. Original source and U0=0 are unchanged.
The results below are classical operator/Fourier tools specialized and assembled for
SUCC. They make no academic-priority claim. **No proof of pi normality or RH is obtained.**

## M00. Source, notation and boundaries

Throughout, b=16, e(t)=exp(2 pi i t),

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U0=0, U_n=b U_(n-1)+r(n),
    A_n=b^(-n)U_n, alpha=sum_(j>=1)b^(-j)r(j)=pi/16,
    T_n=sum_(j>=1)b^(-j)r(n+j)=b^n(alpha-A_n).

The alpha identity is the original BBP theorem, not a new derivation. Positive
regrouping gives r(n+1)<15/(64 n^2), n>=1. Therefore

    0<T_n<1/(64 n^2),   sum_(n>=1) T_n<1/32.                 (M0)

The latter uses sum n^-2<2. Every finite r(n), U_n is exact rational. The chosen
quantization scale hbar_*>0 is mathematical model data, not physical Planck's constant.
On L2(R), T_s psi(x)=psi(x-s), D_a psi(x)=a^(-1/2)psi(x/a), and
M_h psi(x)=e(hx)psi(x), for a>0 and real s,h. The original ordered propagator is

    P_n=W_n ... W_1=T_(U_n) D_(b^n)=D_(b^n) T_(A_n).        (M1)

This is inherited from PR444; multiplication is rightmost-first. An altered seed s
means P_n T_s, NOT an undeclared replacement of the original state.

## Round 1 / M01. Exact arithmetic scattering, with the correct topology

**Theorem.** The co-expanding-frame evolution D_(b^-n) P_n=T_(A_n) converges
strongly on L2(R) to T_alpha. For psi in H1(R),

    ||(T_(A_n)-T_alpha)psi||_2
      <= |A_n-alpha| ||psi'||_2
      < ||psi'||_2/(64 n^2 b^n).                            (M2)

Proof: write translations as integrals of psi' for H1 and use Minkowski; extend
strong convergence by density and unitarity. Equation M0 gives the explicit rate.
For every n, A_n<alpha, however,

    ||T_(A_n)-T_alpha||_(L2->L2)=2.                         (M3)

Indeed its Fourier multiplier difference has essential supremum 2 whenever the
translation difference is nonzero. Strong convergence must NOT be promoted to
operator-norm convergence. The scattering operator retains the complete source
constant alpha, so no source arithmetic has disappeared.

**Provenance.** The perturbed-orbit/pure-radix relation is inherited and is classical
in Lagarias (2001). The H1 specialization and exact norm warning are elementary
Fourier consequences, not an independent witness for normality.

## Round 1 / M02. A closed, source-authenticated loop isolates the point phase

From direct substitution in M1, for every real h,

    P_n^* M_h P_n = e(hU_n) M_(h b^n).                     (M4)

Consequently the SAME-HILBERT-SPACE ordered operator loop

    E_(n,h) = P_n^* M_h P_n M_(-h b^n) = e(hU_n) I          (M5)

is exact. No Dirac initial vector, random seed, wavepacket width or approximation
appears. On every normalized L2 state its expectation is the actual selected
arithmetic phase. Its global phase is observable only RELATIVE to a declared
coherent reference, e.g. a controlled E and a Hadamard/Pauli readout. This is an
exact mathematical quantum model, not a claim of available hardware or speedup.

**Seed binding.** Replace P_n by P_n T_s in M5. The phase is then
 e(h(U_n+b^n s)), so the same-forcing coherent seed is not erased. The unshifted
reference fixes the actual zero boundary. At s=1/5-alpha, the completed orbit is
b^n/5-T_n and the mean tends to e(h/5), never zero for integer h.

**Order binding.** If one replaces the counterfrequency -h b^n by -h, a residual
modulation M_(h(b^n-1)) remains: the proposed loop is no longer scalar. Changing the
order of original source steps changes U_n; the first two-step displacement is
12301/273. Equal endpoint affine maps do still have equal M5: this is not a faithful
representation of every free path microhistory.

**Common-endpoint path interferometer (constructive consequence).** Introduce a
DECLARED N-dimensional control clock, v=N^(-1/2)sum_(n=1)^N |n>, and the unitary
V=sum |n><n| tensor E_(n,h). Each branch returns the data register to EXACTLY its
original state and contributes ONLY the authentic source phase. Thus

    V(v tensor psi)=N^(-1/2)sum e(hU_n)|n> tensor psi,
    Prob(control returns to v)=|S_N(h)/N|^2.                (M5B)

This remains true for every normalized mixed data state, since the scalar loop
leaves it unchanged. It is a bona fide coherent path sum with common data
endpoints and source-determined phases, not a probabilistic averaging over
alternative arithmetic seeds. The coherent altered seed q=1/5 has return
probability at least max(0,1-11|h|/(56N))^2 (strict when N>11|h|/56);
it cannot masquerade as normal.
The inverse gates are operations in a declared reversible unitary model, NOT a
claim that actualized physical history or thermodynamic entropy can be undone.
No ready-made physical device, finite-cost realization or speedup is assumed.
The corresponding two-loop E_(n+k,h) E_(n,h)^* extracts the TRUE signed lag
phase e(h(U_(n+k)-U_n)), allowing the same construction to interrogate M16.

**Cost.** The countermodulation frequency grows as |h| b^n. Formula M5 repairs
Gaussian false positives but has NOT proved cancellation across n and is NOT an
algorithmic shortcut for normality. The coherent average of E_(n,h) is exactly
(S_N(h)/N) I; bounding that scalar is still the arithmetic problem.

The implementation triangulates this identity by (i) exact affine/Weyl group law,
(ii) direct tracing of function arguments through the primitive word, and
(iii) an exact finite conductor model below. These are different algorithms with
shared source mathematics, not blind external reviewers.

## Round 2 / M03. A finite phase-faithful register exists, but it is NOT a 2-adic clock

The combined original rational source is

    r(n)=(120 n^2-89 n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)].

Its denominator is odd. Set Q_N=lcm(den r(1),...,den r(N)); it is odd and every
Q_N U_j, j<=N, is an integer. On C[Z/Q_N Z], the map

    |x> -> |16 x+Q_N r(j) mod Q_N>

is unitary because gcd(16,Q_N)=1. Its ordered product is |x> -> |b^N x+B_N>,
where B_N=Q_N U_N mod Q_N. The character clock C_h|x>=e(hx/Q_N)|x> obeys

    P_N^* C_h P_N C_(-h b^N)=e(h B_N/Q_N) I=e(hU_N) I.     (M6)

This is a finite exact implementation of M5 with a normalizable |0>. In contrast,
reducing an odd-denominator rational modulo 16^r alone does NOT recover its real
circle character. The two carrier types and their embeddings cannot be conflated.

There is no uniformly adequate fixed conductor for all times. If Q_N were bounded,
its nondecreasing divisibility chain would eventually be constant Q; then the
positive source r(n)->0 would always be an integer multiple of 1/Q, impossible.
The growing denominator/register cost is real. No array of size Q_N is allocated
by our code; it verifies exact address and character identities.

## Round 2 / M04. Strong cancellation for every fixed L2 probe can coexist with full coherence

Define the raw, UNCORRECTED averaged Heisenberg readout

    B_(N,h)=(1/N) sum_(n=1)^N P_n^* M_h P_n.

For integer h!=0 this is multiplication by
 f_(N,h)(x)=(1/N)sum e(h(U_n+b^n x)). Orthogonality of the distinct integer
frequencies h b^n gives, on every interval [j,j+1],

    integral |f_(N,h)(x)|^2 dx=1/N.                       (M7)

As |f|<=1, bounded compactly supported functions are a dense test class showing
B_(N,h)->0 STRONGLY on L2(R). This holds for any real source coefficients U_n,
including nonnormal completed points. It uses neither probabilistic selection of
pi nor quantum ergodicity of a specified arithmetic state.

Nevertheless at x=-alpha, M0 gives

    |f_(N,h)(-alpha)| > 1-pi|h|/(16N).

Since f is continuous this is a lower bound for its essential supremum, and

    1-pi|h|/(16N) < ||B_(N,h)|| <=1,  hence ||B_(N,h)||->1. (M8)

Strong convergence of a family of quantum readouts is therefore compatible with
a coherent exceptional arithmetic seed. Taking a horizon-dependent state is a
DIFFERENT quantifier from fixing psi and taking N->infinity. M5's loop, which
removes the large position modulation, is not the raw readout of M7.

## Round 3 / M05. General H1 resolution budget: polynomial energy can give universal false positives

For normalized psi in H1(R), let D=||psi'||_2 and rho=|psi|^2. Then rho in W^(1,1),
||rho'||_1<=2D. Integration by parts at nonzero frequency gives

    |integral rho(x)e(h b^n x) dx|
        <= min(1,D/(pi |h| b^n)).                         (M9)

Thus for ANY phase stream z_n (in particular the actual BBP phases),

    |(1/N) sum z_n integral rho(x)e(h b^n x) dx|
        <= (1/N)sum min(1,D/(pi |h|b^n))
        <= min(1,(t+1/15)/N),                            (M10)

where t=max(0,ceil(log_16(D/(pi|h|)))) for D>0. To see the last estimate, bound
n<=t by one and sum the geometric tail from t+1. If t>N, the minimum with one
keeps the bound valid. A normalized nonzero L2 state cannot have D=0, but the
zero limit is harmless in the code.

For varying psi_N, log(1+D_N)=o(N) therefore forces the raw averaged quantum
reading to zero for EVERY arithmetic source. In particular polynomial derivative
norm, and hence polynomial kinetic-energy expectation hbar_*^2 D_N^2, cannot
distinguish the selected pi orbit from the coherent counterseed by this raw
readout. A nonvanishing raw mean delta along a subsequence requires
log_16 D_N >= delta N-O_h(1) there. This is a necessary resolution cost for THIS
measurement, not a universal computational lower bound for all pi algorithms.

The phase-echo M5 can avoid this state-squeezing cost but pays exponentially large
control frequency instead. Its operation list and observables must be included
in resource accounting.

## Round 3 / M06. Repair the Gaussian measure: normalize by the resolved horizon

Let psi_m be a normalized zero-centered Gaussian with position variance b^(-2m).
For 0<=m<=N integers, the raw sum of separate expectation values (not assumed
nondisturbing sequential measurements on one system) is exactly

    G_(N,m,h)=sum_(n=1)^N e(hU_n) exp[-2pi^2 h^2 b^(2(n-m))].

For ANY complex stream |z_n|<=1 in place of e(hU_n),

    |G_(N,m,h)-sum_(n=1)^m z_n| < B_h,                    (M11)
    B_h=1+968 h^2/(49*255)+1/(4590 h^2), h integer !=0.

Proof: the one boundary term n=m costs at most one. For n<m use
1-exp(-u)<=u and sum b^(-2j), j>=1, giving 2pi^2 h^2/255. For n>m use
exp(-u)<=1/u and the same geometric series, giving 1/(2pi^2 h^2*255).
The rational bound uses 3<pi<22/7. For m=0 or m=N one part is absent, so the
same bound holds without change. No sign or phase-independence assumption occurs.

**Resolved-horizon criterion.** If m_N->infinity, m_N<=N, and the attained
integer depths have vanishing relative gaps (in particular m_N=floor(theta N),
0<theta<=1, or m_N=floor(log_16 N)), then

    for all fixed h!=0: G_(N,m_N,h)/m_N ->0
    iff the original point is normal in base16.           (M12)

M11 proves equivalence along the attained depths; bounded terms fill relative
gaps by |S_{m+d}-S_m|<=d. This is a valid repaired criterion, NOT an estimate on
its selected value. For m_N=floor(theta N), the value normalized by N tends,
on the coherent seed q=1/5, to theta e(h/5). If m_N=o(N), normalization by N
instead tends to zero for every phase stream, a universal false positive.
At m=N, even sigma_N=b^-N (without b^N sigma_N->0) recovers the averaged point
Weyl statistic with O_h(1/N) error. Recovering EACH LAST phase, which PR444
studied, is stronger and correctly has a stricter localization requirement.
Polynomial localization sigma_N~1/N can be used with m_N~log_16 N, but then one
has only resolved a logarithmic prefix: this is NOT accelerated normality proof.

## Round 4 / M07. The Feynman regulator interacts nontrivially with the echo

Use the EXACT parent regulator: P_(n,epsilon)=G_t P_n,
G_t=exp(i t hbar_*/2 partial_x^2), t=epsilon C_n,
C_n=(b^(2n)-1)/255. Let kappa be ANGULAR frequency (kappa=2pi h),
a=b^n, and use M^ang_kappa=exp(i kappa X). A separate Fourier calculation gives

    E^epsilon=P_(n,epsilon)^* M^ang_kappa P_(n,epsilon)
                    M^ang_(-a kappa)
      =exp(i kappa U_n-i hbar_* t kappa^2/2)
                    T_(-hbar_* t kappa/a).               (M13)

Proof: the Fourier action of P_(n,epsilon) is
sqrt(a)exp(-i xi U_n-i hbar_*t xi^2/2) psi_hat(a xi).
Conjugating the Fourier shift xi->xi-kappa and the final countershift leaves
exp(i kappa U_n+i hbar_*t(kappa xi/a-kappa^2/2)). This is precisely M13.
Our independent oracle composes argument shifts and quadratic Fourier phases,
not the position-space algebra used in M5.

On an initial band |xi|<=K, M13 implies

    ||(E^epsilon-e^(i kappa U_n)I)psi||
    <= min(2,hbar_* epsilon C_n*(kappa^2/2+|kappa|K/a))||psi||. (M14)

One CANNOT re-use PR444's uniform epsilon hbar_* K^2/510 propagation bound
without paying the exponentially increasing countermodulation frequency. That
bound assumes the input's original fixed band. After M_-a kappa the band is shifted
by a kappa. For fixed uncorrected echo parameters the safe vanishing-error scale
is epsilon_N b^(2N)->0. This is a sufficient estimate, not a claim that no special
resonant epsilon_N sequence can do better.

**Exact constructive repair:** multiply M13 by the calibrated operator

    exp(+i hbar_*t kappa^2/2) T_(+hbar_*t kappa/a).

The result is e^(i kappa U_n) I exactly, for every finite horizon and epsilon>=0.
It explicitly pays the regulator chirp and displacement rather than treating
positive smoothing as arithmetic cancellation. Exact calibration is model data;
experimental finite precision is not automatically certified by the identity.

## Round 5 / M08. Certified signed-lag tests, and why the signs matter

The inherited original source lag identity is

    U_(n+k)-U_n=(b^k-1)U_n+F_(n,k),
    0<F_(n,k)<(b^k-1)/(64 n^2).

For C_k=sum_(n<=N-k)e(h(U_(n+k)-U_n)),
D_k=sum_(n<=N-k)e(h(b^k-1)U_n), the first-derivative phase bound and monotonic
integral comparison give

    |C_k-D_k| <= sum_(n>=1) min(2,pi |h|(b^k-1)/(32n^2))
                < sqrt(11 |h|(b^k-1)/14).                 (M15)

This is the Main XVIII clipped transport, credited, not new. We measure the
SIGNED weighted real parts

    Lactual=(2/(KN)) sum_(1<=k<K)(1-k/K) Re C_k,
    Lreduced=(2/(KN)) sum_(1<=k<K)(1-k/K) Re D_k.

Finite sliding-window Cauchy-Schwarz supplies

    |S_N/N|^2 <= (1+(K-1)/N)(1/K+Lactual)
              <= (1+(K-1)/N)(1/K+Lreduced+E),             (M16)

E being the same weighted sum of upper bounds M15. All h and windows in
PREREGISTRATION.md were fixed BEFORE the measurements. N=48,96 are calibration;
N=384,768,1537,3072 and h=1,3,5,7,11 are holdouts; K=floor(log_4 N).

**Certificate method.** Literal rational recurrence modulo one is compared with
an independently implemented modular-exponentiation-per-summand oracle at the
full fresh horizons. Each phase is reduced exactly, enclosed on a dyadic grid,
then the angle is enclosed using independent Machin arctangent bounds for pi.
Fixed-point integer Taylor recurrences round BOTH endpoints outward. Their
Lagrange remainders use |angle|<22/7. The phase-grid error and angle error are paid
by the global derivative bounds |sin'|,|cos'|<=1. All decisions use Fractions and
integers; JSON decimal displays are descriptive only. The certificate API checks
the source and declared seed modulo one before attaching original-source transport
bounds. This authenticates the circle-observation history, not an unwrapped lift;
the actual runs start from the literal rational zero. Arbitrary comparison streams
must disable source verification and receive no original-source error budget. Sign, square-modulus and
VdC inequalities use the exact rational interval endpoints.

Both signs occur in the source-selected lag statistic. In particular positive
values on the fresh grid refute the OVERSTRONG claim that every finite selected
lag score is nonpositive. They do not refute a limsup<=0 conjecture. None of these
finite observations establishes an all-horizon signed o(N) estimate.

## Round 6. What survived, what failed, and next discriminating work

SURVIVES: exact phase-loop extraction M5/M6, explicitly corrected regulator M13,
resolved-horizon normalization M11/M12, exact source scattering, and the certified
finite source measurements. These are genuinely source-faithful maps and bounds.
FAILS WITH RECEIPTS: fixed-probe cancellation=>selected normality (M7/M8);
polynomial-energy raw probe=>point resolution (M10); normalization by all N while
only o(N) terms are resolved; reuse of a fixed-band error through an exponentially
modulated echo; endpoint/clock-only phase replacement; universal finite lag negativity.
OPEN: proving (1/N)sum e(hU_n)->0, for every fixed integer h!=0, on literal U0=0.
No theorem here is such a new signed saving. The new loop makes the selected
observable accessible without smoothing, but estimating its chronological sum
still requires an arithmetic mechanism not supplied by generic unitarity.

A useful next experiment is to feed the SAME exact loop phases into the full
prime-primary/real-cofactor signed conditional correlations and original signed
lag machinery. Any claimed contraction must fail on q=1/5 for a SOURCE/SEED
reason and must not be a statement about arbitrary fixed L2 vectors instead.
Do not infer physical quantumness, a laboratory resource advantage, or RH.

## Primary provenance

1. Bailey, Borwein, Plouffe, *On the Rapid Computation of Various Polylogarithmic
   Constants*, NASA report NAS-96-016 / Mathematics of Computation 66 (1997):
   https://ntrs.nasa.gov/citations/19970009337 . Original BBP identity only.
2. Lagarias, *On the Normality of Arithmetical Constants* (2001),
   https://arxiv.org/abs/math/0101055 . Perturbed orbit/pure-radix relation and
   source-class limitation; does not prove the selected normality assertion.
3. Combescure and Robert, *Quadratic Quantum Hamiltonians Revisited* (2005/2006),
   https://arxiv.org/abs/math-ph/0509027 . Exact quadratic/metaplectic covariance
   and echo context. All affine echo formulas above are derived explicitly.
4. NIST DLMF 4.24, https://dlmf.nist.gov/4.24 . Arctangent power series/addition
   formulas; Machin branch is checked by tangent algebra and its quadrant.
5. SUCC Main XVIII and PR444: source transport, original unitary propagator,
   Gaussian formulas and signed-lag reductions are INHERITED, not independent
   confirmations. All new statements explicitly separate mathematical proof,
   executable finite check, and currently unproved selected asymptotics.
