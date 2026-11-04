# Operation Oily–Macaroni: original source, analytic completion, Archimedean numerator and finite/global boundary

**2026-11-03. RESEARCH ONLY.** Exact arithmetic and paper proofs, not an external referee, Lean theorem, or solution to π base-16 normality. Pinned parent SUCC draft PR #485 at `cdb01d73839f08cb10b46f51d42afecf44469ee2`. Separate preregistration committed at `48777b17383d8c42c6f3adb9853923b2017bed23` **before** the specified held-out source phase tests. Inherited source and entire original four signed BBP terms, literal U0=0, main, provenance, CI and formal artifacts are immutable.

The author's finite/global hypothesis is examined at two different types: **signed linear BBP analytic completion** and **nonlinear chronological Fourier cancellation**. The first genuinely has finite nonzero null-channel prefixes with an exact zero infinite completion. This does NOT prove the second. Finite complex roots of unity can cancel exactly even at finite length; an absolute claim that finite cancellation is impossible is false.

## Source and original audited identities

For positive integer n retain

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U0=0, U_n=16 U_(n-1)+r(n).

Let `alpha=pi/16`, `X_n=16^n alpha`, `T_n=X_n-U_n>0` (unwrapped). The complete genuine original-source Green tail, including its continuous positive s extension, is inherited from SUCC's original two-quadratic-atom and Gamma dossiers:

    T(s)=int_0^1 x^(8s) (1-x)/D(x) dx,
    D(x)=(2-x^2)((x-1)^2+1),  s>0.

The original BBP numerator P(x)=4-2x^3-x^4-x^5 satisfies the EXACT polynomial identity `P/(16-x^8)=(1-x)/D`. These formulas are equivalent to the unchanged four Mellin terms; no different forcing or pi digits are construction inputs. Define

    B(s)=int_0^1 x^(8s)(1-x)dx=1/[(8s+1)(8s+2)].

For actual epochs use the corrected split prime and inert prime passports of PR #485, with common clean window `I_A=[A,ceil(4A/3))` and disjoint prime product P_A. All p-primary statements below use these ORIGINAL windows, never the refuted inert [k,2k) window.

## OMC-01. Strict positivity, complete monotonicity and one-sided original Gamma lag shear (PROVED)

For all s>0 and d>0 let `sigma_d(s)=T(s)-T(s+d)`. The exact positive kernel is

    sigma_d(s)=int_0^1 x^(8s)(1-x)(1-x^(8d))/D(x) dx > 0.

Differentiate under the integral: for any integer j>=0,

    (-1)^j d^j/ds^j sigma_d(s)
      =int_0^1 (-8log x)^j x^(8s)(1-x)(1-x^(8d))/D(x)dx >0.

Thus BOTH T and each positive-lag shear are strictly completely monotone on s>0, no probabilistic digits or finite extrapolation. Since D(x)>=1,

    0<sigma_d(s)<B(s)-B(s+d).

The algebraic derivative `-B'(s)=8(16s+3)/[(8s+1)^2(8s+2)^2]` obeys `0<-B'(s)<1/(32s^3)` for every s>0. The inequality follows by clearing positive denominators: their difference numerator is `2304s^3+832s^2+96s+4>0`. Integrate from s to s+d to get

    0<sigma_d(s)<B(s)-B(s+d)<d/(32s^3).       (OMC-1)

This cap is asymptotically sharp in the declared regime **fixed d>0, s->infinity**:

    lim_(s->infinity) 32s^3 sigma_d(s)/d = 1.  (OMC-2)

Proof: in the positive Beta integral the normalized weight concentrates at x=1. Since 1/D(1)=1 and `(1-x^(8d))/(1-x)->8d` at x=1, the ratio to the explicit Beta second-moment integral tends to 1 by dominated convergence; that moment is `2/[(8s+1)(8s+2)(8s+3)]`. This is a source-specific sharp lag-shear scale, NOT signed time-character cancellation.

## OMC-02. Oily–macaroni kernel geometry as an exact phase shear (INHERITED + EXACT CONSEQUENCE)

Let `D_gamma(s)=psi(s+1)-log s`. SUCC #474 proved the full original-source positive kernel gap

    W(s)=D_gamma(s)^2/16-T(s)>0,

strictly completely monotone for every real s>0. Hence for all s,d>0,

    sigma_d(s)
      =[D_gamma(s)^2-D_gamma(s+d)^2]/16-[W(s)-W(s+d)]

with BOTH square and W bracket strictly positive, and

    0<sigma_d(s)<[D_gamma(s)^2-D_gamma(s+d)^2]/16.  (OMC-3)

This is the sound use of the Euler–Mascheroni/Gamma “oily” geometry: an exact positive *one-sided finite-to-infinite phase shear*. It is not a phase mixing law. The source-selected real Weyl correlation remains UNVERIFIED.

## OMC-03. Full-window signed lag transfer is an endpoint coboundary (PROVED, sharp source tail)

For ALL positive n,d,

    U_(n+d)-U_n=(16^d-1)16^(n-1)pi+[T_n-T_(n+d)].

The positive bracket is sigma_d(n). For integers B>A+d,

    sum_(n=A)^(B-d-1) sigma_d(n)
      =sum_(j=0)^(d-1)T_(A+j)-sum_(j=0)^(d-1)T_(B-d+j)
      <=sum_(j=0)^(d-1) B(A+j) <=d B(A).   (OMC-4)

The identity is an exact chronological **coboundary**; no cancellation of the positive individual σ terms is claimed. Put `e(x)=exp(2πix)` and fixed nonzero integer h. The universal chord inequality gives on EVERY such window

    |sum_(n=A)^(B-d-1) e(h(U_(n+d)-U_n))
       -sum_(n=A)^(B-d-1) e(h(X_(n+d)-X_n))|
        <=2π|h| d B(A) <(44/7)|h|d B(A). (OMC-5)

In particular if |h|<=m_A≈log A and 1<=d<=A/3, the difference of these **unnormalized** selected lag sums is O(log A/A), uniformly in d. This transfers source to exact π orbit with a shrinking error; it does NOT prove either lag sum small. Gamma determines the correction, not the selected sign.

## OMC-04. Rigorous finite-source-to-analytic-π horizon (PROVED)

Let the rational ORIGINAL prefix

    alpha_M=sum_(j=1)^M 16^(-j)r(j)=U_M/16^M.

Then EXACTLY, for every integer n>=0,

    16^n alpha=16^n alpha_M+16^(n-M) T_M.   (OMC-6)

A positive rational **two-sided** Green enclosure follows from the integral D(x). On 0<=x<=1, `D(x)-1=(1-x)(x^3-x^2-x+3)`, where the cubic decreases from 3 to 2, so `D>=1` and `0<=1-1/D(x)<=3(1-x)`. For s>=1,

    L(s)=B(s)*(1-6/(8s+3)) < T(s) < B(s).  (OMC-7)

Fix mesh m>=2 and assume m B(M)<1. Define q_lower as the LARGEST nonnegative integer q for which `m 16^q B(M)<1`. Then for every 0<=j<=q_lower, the exact rational prefix orbit `16^(M+j)alpha_M` shadows the completed true orbit within **strict real-circle distance 1/m**. The actual last extra step satisfying `m 16^q T_M<1` is either q_lower or q_lower+1, because `L(M)/B(M)>1/16` for M>=1. This is a sharp **within one step** source-only horizon certificate; it does not require π digits.

For m comparable to log M,

    q_lower=2 log_16 M-log_16 m+O(1).

BEWARE: real-circle distance <1/m does NOT guarantee the two points lie in the same half-open m-bin. The code certifies a common bin only if the entire outward-rational analytic interval avoids every cell boundary. The finite rational alpha_M is eventually periodic in base 16 and hence nonnormal, despite shadowing the true π orbit for a growing window. No finite stage is a universal limiting normality certificate.

## OMC-05. The canonical BBP null channel is finite-nonzero/global-zero (INHERITED FORMULA, VERIFIED NEW FINITE BOUND)

The original October 26 minimal Gaussian/real filter has the exact radial tap vector

    (2,-2,-1,-2,-1/2,-1/2,1/4,0)

and angular/radial decomposition

    P_rad(x)/(1-x^8/16)=2 d/dx log F(x),
    F(x)=(2-x^2)/((x-1)^2+1), F(0)=F(1)=1,
    F(x)>1 for 0<x<1.

For every finite N>=1 let R_N be the first N radial BBP shells (rational, with exact coefficient denominator 16^j(8j+k+1)). From the full zero integral and integration by parts,

    R_N=2 int_0^1 [d/dx(x^(8N)/16^N)] log F(x) dx >0.

Since `0<log F(x)<2(1-x)` on (0,1),

    0<R_N<4/[16^N(8N+1)],    R_N~1/(2N16^N). (OMC-8)

Nevertheless its COMPLETE integral `2[log F(1)-log F(0)]=0`. First N=1,2,3 exact residuals are 2/105, 67/90090, 1443053/42833831040. This is a genuinely source-authentic example of **no exact zero at any finite cutoff, exact zero after analytic completion**. It is not a proof of π digit normality. The blanket claim “finite complex sums never cancel” is false: three cube roots of unity add to zero at a finite stage.

## OMC-06. The original selected radical survives in every reduced denominator (PAPER PROOF, source-specific)

For `I_A=[A,ceil(4A/3))` let P_A be the product of both corrected, simultaneously clean split/inert prime families from SUCC #485. For 1<=d<|I_A| define

    R_(A,d)=P_A/gcd(P_A,16^d-1).

For any `n,n+d∈I_A` and integer `0<|h|<=A`, each p|R_(A,d) has p∤h, and the ORIGINAL p-local residue of `h(U_(n+d)-U_n)` is a nonzero p-unit times `(16^d-1)/p`; its valuation is exactly -1. Therefore

    R_(A,d) divides den(h(U_(n+d)-U_n)).    (OMC-9)

This is a genuine SOURCE-SELECTED arithmetic noncancellation. Use classical fixed-modulus PNT-AP in SUCC #485 and `log gcd(P_A,16^d-1)<=d log16` to obtain uniformly for d across the full 4/3 window

    log R_(A,d) >= [11/9-(log16)/3+o(1)] A,

and the bracket is ~0.298026...>0. It is a denominator/conductor bound, NOT a lower **Archimedean** real-circle gap. The original reduced fraction can have a large denominator and a centered numerator equal to 1.

## OMC-07. Strong quantitative CRT counterexample with EVERY original selected p clock (PROVED COUNTERMODEL)

Let B=ceil(4A/3), and let D_A=lcm of the reduced odd denominators of the ORIGINAL forcing r(j), 1<=j<B. The actual original U_n has denominator dividing D_A for every n<B. Each selected clean p occurs to exponent exactly 1 in D_A. Independently, for EACH ordinary prime 7<=q<2A, the original source at j=(q+1)/2 is

    r(j)=4/(4q-3)-1/(2q)-1/(4q+1)-1/(4q+2),

so `v_q(r(j))=-1` and q|D_A. These OLD primes are disjoint from the selected new primes (all >2A). Put

    S_A=product_(prime q in [7,2A)) q.

Then `P_A S_A | D_A`. The ordinary PNT gives `log S_A=2A+o(A)` with no RH assumption. For every REAL selected original source state n∈I_A set

    a_n = centered integer representative of (D_A U_n mod P_A),
    -P_A/2 < a_n <=P_A/2,
    U_fake(n) = 1/5+a_n/D_A.

Since the source's p-primary denominator exponent is one, for EVERY selected p and every n∈I_A,

    p U_fake(n) ≡ p U_n (mod p)

as p-INTEGRAL rationals. Consequently for every adjacent pair in I_A the fake also matches the original `p*(U_(n+1)-16U_n-r(n+1))≡0 mod p` at EVERY selected prime. ALL selected prime-clock labels, exact source p-residue values and local recurrences survive. But

    |U_fake(n)-1/5| <= P_A/(2D_A) <=1/(2S_A)
       =exp[-(2+o(1))A].                   (OMC-10)

Therefore for every power-of-two mesh m_A≈log A, all the fake phases eventually occupy **one** real mesh bin; its normalized collision energy is m_A, rather than the desired `o(log m_A)`.

**Type / source firewall:** U_fake is a DIFFERENT rational finite-window trajectory, NOT the original full Q-valued recurrence nor the same zero boundary. It refutes any inference from selected p-local passport data **alone** to real-circle nonconcentration. It does NOT refute a future proof using complete original global U0=0, all old-prime cofactor/carries, or analytic completion.

The fraction of residue integers modulo P_A that are p-units at every selected prime is

    phi(P_A)/P_A = prod_(p selected)(1-1/p)=1-O(1/log A),

since all selected primes are Θ(A) and there are O(A/log A) of them (PNT-AP). Thus **nonzero unit conditions exclude asymptotically almost no candidate numerators**, despite the product P_A being exponentially large. We need the actual residue values AND the cross-prime real lift/carry, not just the fact that every prime survives.

A second independent control, already in the tested code, changes ONLY the rational INITIAL SEED while retaining the entire original four-pole forcing. For each finite window A, choose a rational seed s_A with denominator coprime to P_A approximating 1/5-alpha. The original forced recurrence then shadows the coherent fixed point 1/5 throughout the finite window, with all p-clock passports unchanged. These seeds vary with A; the zero-seed marked source is not thereby refuted.

## OMC-08. A **signed** Gamma boundary-flux equation at the real near-pair gate (PROVED)

Take mesh m>=4, rho=1/m, original lag delta_U={U_(n+d)-U_n}∈[0,1), and original positive shear sigma=sigma_d(n). When `0<sigma<rho`, completed lag delta_X is delta_U−sigma mod 1. Direct comparison of the two half-open near-circle arcs gives the exact integer equation

    1_{||delta_X||<=rho}-1_{||delta_U||<=rho}
      =1_{delta_U in (rho,rho+sigma]}
       -1_{delta_U in [1-rho,1-rho+sigma)}.   (OMC-11)

This is an **ORIENTED** gain/loss, not an unsigned boundary-count estimate. Summing over unordered pairs, the change in ordered near-pair counts is twice the signed total; diagonal pairs never change. The original selected differences are rationals with ODD reduced denominators. Since m is even, they never lie EXACTLY at ±rho (noncontact). In fact

    m*(U_t-U_n)-1 is a unit in Z2,
    v2((U_t-U_n)-1/m)=-v2(m),             (OMC-12)

which highlights that real proximity to a binary mesh boundary cannot be inferred from 2-adic proximity: the source is always maximally far from this equation in the scaled 2-adic metric.

The analytic shears obey `0<sigma_d(n)<d/(32 n^3)`, so the gain/loss arcs are extremely narrow. **But their actual selected membership counts are UNPROVED**, and even a small signed boundary correction would not prove the original nearpair count small. The exact source/π finite pair classifier in the code uses outward-rational sigma intervals, NO π digits, and returns `near/far/ambiguous` rather than inventing decisive results.

## OMC-09. The still-unpaid Archimedean centered-numerator bound (OPEN)

Let m_A≈log A, I_A=[A,ceil(4A/3)), L=|I_A|, and common original odd source denominator D_A as above. For genuine original pairs write

    a_(n,d)=D_A*(U_(n+d)-U_n)∈Z,
    a_center=unique centered residue a_(n,d) (mod D_A).

The real nearpair event is **exactly**

    |a_center| <= D_A/m_A.

The selected p-local data determine `a_(n,d) mod P_A`, hence a full CRT class but **do not** determine which huge integer lift in that class was realized by the actual four-pole zero-seeded source. The fake U(n) in OMC-07 shows an exponentially near-zero alternative. A new genuine theorem must control the actual all-place coupling / signed lag, with the original old-prime cofactor, integer carries and U0=0, enough to prove

    P_(A,m_A)=o(A² log(m_A)/m_A)

on every clean window (or on the 3 windows in SUCC GL-09). Then inherited SUCC #476 + three-window gluing imply pi base-16 normality. This premise remains OPEN. An appeal to average Galois Ramanujan factors, ordinary PNT-AP, Gamma positivity, large denominators, or finite nonzero residuals is insufficient.

## Status, sources and independent checks

OMC-01/03/04/06/07/08: paper proofs in stated domains; finite tests and independent SymPy polynomial identities only corroborate. OMC-02/05: source-inherited positive Gamma and Gaussian null-channel formulas with a newly explicit sharp lag/finite-residual bound. OMC-09: UNVERIFIED selected real nearpair saving. No new Lean kernel, external referee, RH, quantum, physical c, or pi normality claimed.

Source dependencies (shared provenance, not independent): SUCC #474 (positive Gamma sheet); #475/#476 (mesoscopic/hyperbolic Fejér conditional normality); #481 (quadratic atoms); #484 (joint carry); #485 (corrected split/inert prime windows, original prime clocks and 3-window gluing), October 26 `BBP_TWO_QUADRATIC_ATOMS.md`, main `bbp_two_adic.py`.

External classical antecedents: Bailey–Crandall (2001), *On the Random Character of Fundamental Constant Expansions*, https://doi.org/10.1080/10586458.2001.10504441; Lagarias (2001), *On the Normality of Arithmetical Constants*, https://arxiv.org/abs/math/0101055; classical prime number theorem/PNT-AP and elementary CRT. The derivations do not require RH or locations of zeta zeros.
