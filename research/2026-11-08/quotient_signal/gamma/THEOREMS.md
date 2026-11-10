# The authentic completion residual has a Gamma-normalized phase

**Status: paper-proved source calibration; original signed covariance and
pi base-16 normality remain OPEN.** No worldwide novelty claim. This
extends the inspected source first-moment identities to the *Green-tail
weighted phase product*, with an effective sharp harmonic remainder.

The faithful test of the conjecture is to specify both the residual and
its subtraction convention. Here the residual is the discrepancy between
the original finite rational state and its completed source orbit. It is
not silently identified with the residual after learning a prime phase.

## GQ1. The balanced source and its classical finite parts

Keep exactly

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U_0(s)=s, U_n(s)=16 U_(n-1)(s)+r(n),
    X_n(s)=16^n(s+pi/16), T_n=X_n(s)-U_n(s).

The authenticated BBP identity gives

    T_n=sum_(j>=1)16^(-j) r(n+j),  T_0=pi/16,
    16 T_(n-1)-T_n=r(n).

For n>=1 let `H_N=sum_(n<=N)1/n`, and write

    R=sum_(n>=1)r(n)
      =pi/4 +5 sqrt(2) pi/16 +5 log(2)/8
        +5 sqrt(2) log(1+sqrt(2))/8,

    B=sum_(n>=1)[n r(n)-15/(64n)]
      =(27+31sqrt(2))pi/128 +39log(2)/32
        +31sqrt(2)log(1+sqrt(2))/64.

These two identities are **inherited**, not this round's discovery:
TS5 and TS10 in read-only PR#530 at
`9b53501e37f6bb9ab5bd6f63cadf4cbfc1607749`, and the earlier original-source
Dirichlet finite part in WCG10. They also follow directly from
`sum_(n=1)^N 1/(n-1+alpha)=psi(N+alpha)-psi(alpha)` with
`alpha=(1/8,1/2,5/8,3/4)` and Gauss's rational digamma formula.
The `-gamma` terms cancel in R because the four coefficients sum to zero.
In B they cancel against the explicitly subtracted harmonic counterterm.
With logarithmic subtraction the source first moment instead has finite
part `15 gamma/64+B`. Classical identities:
[DLMF recurrence](https://dlmf.nist.gov/5.5.E2),
[rational digamma values](https://dlmf.nist.gov/5.4.E19),
[digamma series](https://dlmf.nist.gov/5.7.E6).

## GQ2. A sharp effective weighted Green-tail finite part

Define, for every integer N>=1,

    C_N=sum_(n=1)^N [n T_n-1/(64n)],
    C=B/15 -16R/225 +pi/225
     =pi*(7/9600-7sqrt(2)/1152) +53log(2)/1440
        -7sqrt(2)log(1+sqrt(2))/576.

Then C_N strictly decreases to C and

    0<C_N-C<7/(512N),
    lim_(N->infinity) N(C_N-C)=7/512.                    (GQ2)

The limit constant is approximately `-0.01434210851239401967408`;
this display is not the proof. The coefficient 7/512 in the upper bound
is asymptotically sharp.

**Proof of the uniform bound.** Put

    Q(x)=(x^2+2)(x^2+2x+2)=x^4+2x^3+4x^2+4x+4,
    f(x)=Q(x)/(16-x^8).

Expansion of the original four poles and geometric summation give

    T_n=integral_0^1 x^(8n)(1-x) f(x) dx.

All terms are nonnegative, so the interchange is legitimate. On [0,1],
`Q(1)=15`, `0<=Q'(x)<=22`, and `0<=1-x^8<=8(1-x)`. Hence

    0<=1-f(x)=[15-Q(x)+1-x^8]/(16-x^8)<=2(1-x),

with strict positivity except at x=1. For m=8n this implies

    (m-1)/[(m+1)(m+2)(m+3)] <= T_n
        <1/[(m+1)(m+2)] <1/m^2.

The lower bound can be negative when m<1, but here m>=8. Subtracting
it from 1/m^2 and multiplying denominators shows

    0<1/(64n^2)-T_n<7/(512n^3).                         (GQ3)

Indeed the numerator of the difference from that lower bound is
`7m^2+11m+6`, and
`m(7m^2+11m+6)<7(m+1)(m+2)(m+3)`. Therefore C_N decreases and its
positive omitted correction is less than
`(7/512)sum_(n>N)n^-2<7/(512N)`.

**Identification of the constant.** Let
`R_N=sum_(n<=N)r(n)`, `A_N=sum_(n<=N)n r(n)`,
`S_N=sum_(n<=N)T_n`, `Q_N=sum_(n<=N)n T_n`.
The tail recurrence gives the two exact endpoint identities

    R_N=pi+15 S_N-16T_N,
    A_N=pi+15 Q_N+16 S_N-16(N+1)T_N.                   (GQ4)

Since `S_N ->(R-pi)/15`, `N T_N->0`, and
`A_N-(15/64)H_N->B`, subtraction of `(1/64)H_N` in the second
identity gives C as displayed. This keeps the original boundary term pi;
it is not a replacement of the zero source by an arbitrary integration
constant.

**Sharpness.** The rational f is smooth near1, with f(1)=1 and f'(1)=2.
Thus `f(x)=1-2(1-x)+O((1-x)^2)` uniformly on [0,1]. Integrating the
remainder gives `O(m^-4)`, and the two beta integrals above give

    T_n=1/(64n^2)-7/(512n^3)+O(n^-4).

Consequently `C_N-C=(7/512)sum_(n>N)n^-2+O(N^-2)`, proving the limit.

## GQ3. Euler–Mascheroni survives a declared logarithmic subtraction

For all N>=1 set

    G_N=64[sum_(n<=N)n T_n-C]-log N.

Then

    0<G_N-gamma<11/(8N),   G_N -> gamma.                (GQ5)

**Proof.** `G_N=H_N-log N+64(C_N-C)`. The elementary harmonic bound
`0<H_N-log N-gamma<1/(2N)` follows by writing its difference from
the limit as
`sum_(k>=N)[log(1+1/k)-1/(k+1)]`. Convexity of1/x bounds each term
strictly by `(1/k-1/(k+1))/2`; telescope. Add GQ2.

Thus a precisely defined small residual **does** carry gamma:

    lim [sum_(n<=N)n T_n-(log N)/64]=C+gamma/64.         (GQ6)

The harmonic convention gives C instead. For the scale `log(lambda N)`
the finite part is `C+(gamma-log lambda)/64`, for any fixed lambda>0.
These are explicit changes of normalization, not contradictory constants.
Dyadic differences `sum_(N<n<=2N)nT_n-(log2)/64` tend to zero: the
origin-anchored constant disappears when two cumulative cutoffs are
subtracted. A claim about a single epoch covariance therefore needs its
own transport to this cumulative observable.

## GQ4. A genuine Gamma-normalized residual phase product

For each fixed integer h and every real seed s define, in the declared
common phase reference,

    q_n(h;s)=e(h U_n(s)) e(-h X_n(s))=e(-hT_n),
    P_N(h)=exp(2pi i h log N/64) product_(n=1)^N q_n(h;s)^n,
    e(t)=exp(2pi i t).

Integer powers avoid any logarithm branch convention. Exactly

    P_N(h)=e(-h[sum_(n<=N)nT_n-(log N)/64]),

so

    P_N(h) -> e(-h[C+gamma/64]),
    |P_N(h)-e(-h[C+gamma/64])|<11 pi |h|/(256N)         (GQ7)

for h!=0 (equality to1 is exact when h=0). Multiplying by the known
source counterphase e(hC) leaves the limit `e(-h gamma/64)`. This is an
exact mathematical realization of a Gamma-characterized residual after
quotienting a coherent completed phase. No random seed, statistical fit,
or numerical identification of a constant is used in the proof.

**What this quotient retains.** The source-completed reference is
`X_n(s)=16^n(s+pi/16)`, and q_n is independent of s. In particular the
same q_n and the same gamma limit hold for the coherent bad seed
`s*=-pi/16`, where `U_n(s*)=-T_n` and
`mean_(A<=n<2A)e(hU_n(s*)) ->1`. The calibrated tail is present while
that seed has no Weyl cancellation. This is not a counterexample to an
unproved zero-seed theorem; it identifies exactly which source information
the quotient removes.

If instead one freezes the original zero reference X_n(0), the *unwrapped*
defect is `X_n(0)-U_n(s)=T_n-16^n s`. Its weighted sum differs by

    -s sum_(n=1)^N n16^n
      =-s[16+(15N-1)16^(N+1)]/225.

Thus the unwrapped renormalization has a finite limit iff s=0. This is
a boundary-authentication fact. Its phase-only version can have integer
aliases and is not asserted to identify every seed. Neither version
estimates the zero-source prime/complement covariance.

## GQ5. Exact connection still required to the learning quotient

For the actual local/complement split, `a_n=e(h[U_n]_p)` and
`b_n=e(h(U_n-[U_n]_p))`, the product is `e(hU_n)`. It is not q_n,
because q_n divides by the completed full phase X_n. GQ7 establishes a
calibration of the analytic source completion, while the learning
quotient retains a source-selected **signed** term. No identity presently
equates that term to P_N, G_N or a derivative of either.

The productive next hypothesis is an explicit source-preserving transport
from a signed conditional covariance or lag aggregate to this Gamma
calibration plus a uniformly vanishing error. Such a theorem must retain
the literal zero boundary, original four poles, a common phase reference,
and all-A quantifiers; it must reject the coherent seed without assuming
the desired original cancellation. This note neither proves that bridge
nor rules it out.

## Provenance and authority

- Original source/Green identity: existing selected-orbit dossier and
  `observational_succ/selected_orbit.py`, pinned parent above.
- Inherited R and B: read-only PR#530 TS5/TS10 at
  `9b53501e37f6bb9ab5bd6f63cadf4cbfc1607749`; also WCG10,
  `research/2026-10-28/OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md`.
- Existing neighboring results inspected: original Gamma primitive
  `observational_succ/bbp_gamma_boundary.py`; AE05/AE07/AE08 in
  `research/2026-11-04/analytic_exile/PROOFS.md`; transverse s=2 Mellin
  boundary in `research/2026-11-04/europa_weyl/beta/GAMMA_BOUNDARY.md`;
  original/alternative frame slip in Frobenius prime saturation. Those
  are not republished as this round's results.
- New-to-this dossier: GQ2 effective weighted Green-tail finite part,
  its GQ3 calibrated estimator and GQ4 renormalized phase product.
  These are elementary consequences of the authentic source, not claims
  of new classical special-function theory or new normality decay.
- Exact rational finite oracles validate algebra and declared bounds;
  no Lean/kernel claim and no external scholarly referee review.
