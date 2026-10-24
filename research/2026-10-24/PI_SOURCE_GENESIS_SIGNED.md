# Signed BBP correlations: uniform lag transport, exact conductors, and an arithmetic baseline

Date: 2026-10-24. Base source: PR #252 at
`364962ac0c0e8fb4d06c37468a5d50336d68a9ee`.

**Status:** paper derivations, independently checked finite rational identities,
and explicitly imported classical arithmetic. No academic-priority claim.
The infinite analytic assertions in this note are not certified merely by
the Python checks. Any Lean authority is confined to the declarations and
exact build receipt reported separately. **Pi normality proved: NO.**

The original single-frequency bounded-error transport was already established
in [DUCK_BBP_FORMAL_TRANSPORT.md](../2026-10-21/DUCK_BBP_FORMAL_TRANSPORT.md)
and sharpened in `observational_succ/duck_bbp_fourier.py`. The additions here
are the lag-uniform two-time transport, horizon-matched full-conductor
approximation, an exact dyadic preperiod obstruction for odd truncation
depths, and a logarithmic deficit for the actual pi exponential sums using
an external irrationality-measure theorem. The last result is deliberately
not attributed to the BBP poles.

## SG-S1. Definitions and authenticated source

Write `e(t)=exp(2*pi*i*t)`. For integers `n>=1`, use exactly

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).

Let `T_n=sum_(k>=1)16^(-k)r(n+k)`, for `n>=0`, and let the circle-valued
forced orbit satisfy `y_0=0`, `y_(n+1)={16y_n+r(n+1)}`. The authenticated
BBP source gives

    T_0=pi/16,
    16T_n=r(n+1)+T_(n+1),
    {y_(j+1)+T_(j+1)}={16^j*pi}.

The repaired positive integral proves that `T_n` is strictly decreasing,
positive, and summable for `n>=1`. Its source-derived beta upper bound is

    0<T_n<B_n=1/[(8n+1)(8n+2)].

These claims are independently re-audited in the companion Green report.
The integral identification of pi is classical BBP, with its exact source
formalized previously in `formal/duck_pi/BBPIntegral.lean` and
`formal/duck_pi/PiSource.lean`. The statements below use the actual pi, not
an unspecified real constant named pi.

## SG-S2. Uniform-in-lag signed transport

Fix an integer `h`, a starting index `J>=0`, a lag `d>=1`, and a length
`L>=0`. Define the two **complex signed** sums

    C_(J,L,d)=sum_(j=J)^(J+L-1) e(h*(16^d-1)*16^j*pi),
    D_(J,L,d)=sum_(j=J)^(J+L-1) e(h*(y_(j+d+1)-y_(j+1))).

The convention for an empty sum is zero. For `J=0`, `L=N-d`, the first
sum is exactly the user's `C_d(N;pi)`. Set

    delta_(j,d)=T_(j+1)-T_(j+d+1)>0.

The source identity gives the termwise equality

    e(h*(16^d-1)*16^j*pi)
      =e(h*(y_(j+d+1)-y_(j+1))) * e(-h*delta_(j,d)).       (S2.1)

The modulus-one representatives cause no error because h is an integer.
The negative sign on the last factor is part of the identity. In particular,
we have not replaced a complex correlation by an absolute prime-path sum.

The elementary character bound `|e(hx)-e(hy)|<=2*pi*|h|*|x-y|`, followed
by an exact finite cancellation, proves

    |C_(J,L,d)-D_(J,L,d)|
      <=2*pi*|h| * sum_(j=J)^(J+L-1) delta_(j,d)
      =2*pi*|h| * [sum_(n=J+1)^(J+d)T_n
                   -sum_(n=J+L+1)^(J+L+d)T_n]
      <=2*pi*|h| * sum_(n=J+1)^(J+d)T_n.                (S2.2)

The finite-sum identity is valid even when the intervals overlap; expand
both sides as differences of partial sums. When `L=0`, the bracket is zero.
Since the moments are positive, we may further bound the last expression
by `2*pi*|h|*M_J`, where `M_J=sum_(n>=J+1)T_n`.

For `n>=1`, the following rational telescoping majorant is valid:

    B_n < 4/[(16n-5)(16n+11)]
        =(1/4)*[1/(16n-5)-1/(16n+11)].

Indeed the two positive denominator products differ by exactly 63 when
`B_n` is written as `4/[(16n+2)(16n+4)]`. Consequently

    M_J < 1/[4(16J+11)],
    |C_(J,L,d)-D_(J,L,d)| < pi*|h|/[2(16J+11)]          (S2.3)

for `h!=0`, uniformly in both `d` and `L`. This gives an `O_h(1/J)`
moving-window transport error with **no factor `16^d`**.

A better global constant is available from four exact source-tail bounds.
For `n=1,...,4`, put

    U_n=sum_(k=1)^4 16^(-k)r(n+k)+r(n+5)/(15*16^4).

Positivity and decrease of r prove `T_n<U_n`. Exact rational arithmetic gives

    sum_(n=1)^4 U_n+1/300
      =125384865675219366581009/7614798572538913454899200
      <1/60,

    1/60-[sum_(n=1)^4 U_n+1/300]
      =1528443867095857667311/7614798572538913454899200>0.

The `1/300` bounds `sum_(n>=5)T_n` by the same telescoping majorant.
Therefore every `N>d>=1` and nonzero h satisfy

    |C_d(N;pi)-D_d(N)| < pi*|h|/30 < 2*|h|/15.        (S2.4)

The last bound is wholly rational after the elementary inequality `pi<4`.
It is an all-horizon analytic theorem; the displayed rational comparison
certifies only its finite constant, with the infinite tail controlled by
the proved telescoping inequality.

The difference itself converges as `L->infinity` for each fixed `J,d,h`:
its defining summands are absolutely summable by (S2.2). The remainder after
length L is at most

    2*pi*|h| * sum_(n=J+L+1)^(J+L+d)T_n
      <=2*pi*|h|*min(d*B_(J+L+1), 1/[4(16(J+L)+11)]).

This is convergence of the **difference of the two sums**. Neither separate
correlation sum has been shown to converge or to be `o(N)`.

For clarity about what was gained: a one-time substitution in
`e(h*(16^d-1)*y_(j+1))` has the large correction
`h*(16^d-1)*T_(j+1)`. The lawful two-time comparison (S2.1) instead has
`h*(T_(j+d+1)-T_(j+1))`. These are distinct rational observables. One cannot
claim the smaller error while retaining the wrong one-time surrogate.

### Source requirements and hostile controls

The transfer theorem needs the authenticated real source identity and a
positive decreasing summable tail. Those structural premises suffice for
the theorem with their own tail constant; BBP supplies the explicit beta
bound and small certified number. These premises do not force cancellation:
the positive-Hankel rational counterfeit
`T_n^*=1/[(n+1)(n+2)]`, `r^*(n)=16T_(n-1)^*-T_n^*`, has selected phase
`16T_0^*=8`, hence all true characters equal one. Its lag transport remains
valid. This is a member of the broad transport class but not the exact BBP
source class.

There is also a genuine observation blindness within the fixed BBP forcing.
Changing `y_0` by `k/15` changes every selected circle phase by the same
`k/15`, since `16=1 mod 15`. Every signed lag correlation is unchanged:
`15` divides `16^d-1`. In particular the `y_0=1/3` control is different as
a selected orbit but indistinguishable through these lag correlations.
Its first forced value is still `7/15`, not the unforced fixed point.
Thus lag observations alone do not authenticate the initial state. This
finite translation preserves Haar genericity if it exists, so it is not a
counterexample to a normality implication.

## SG-S3. One rational source approximant for the whole horizon

For `M>=1`, define the rational BBP truncation

    P_M=sum_(n=1)^M 16^(1-n)*r(n).

The exact positive remainder is

    pi-P_M=16^(1-M)*T_M.                              (S3.1)

For any `N>=1`, any nonzero integer h, and any `1<=d<N`, the geometric
series gives

    |sum_(j<N)e(h16^j*pi)-sum_(j<N)e(h16^j*P_M)|
      <=(2*pi*|h|/15)*16^(1-M)*(16^N-1)*T_M,

    |C_d(N;pi)-sum_(j<N-d)e(h*(16^d-1)*16^j*P_M)|
      <=(2*pi*|h|/15)*16^(1-M)
          *(16^d-1)*(16^(N-d)-1)*T_M
      <(32*pi*|h|/15)*16^(N-M)*B_M.                  (S3.2)

The factor 16 in `16^(1-M)` is essential. For `M=N+K`, `K>=0`, a rational
upper bound for either error is

    128*|h| / [15*16^K*(8M+1)*(8M+2)].                (S3.3)

For fixed h, `K=0` already gives an absolute `O_h(N^-2)` error, simultaneously
for every allowed lag. This uses a horizon-dependent rational approximant,
not a fixed rational substitute followed to infinite time. Choosing M odd
with `N<=M<=N+1` preserves this error order and enables the exact arithmetic
statement below.

Write `P_M=A_M/q_M` in lowest terms, `q_M>0`. The exact character conductor
of its lag summand at time j is

    q_(M,j,d,h)=q_M/gcd(q_M, |h|*(16^d-1)*16^j).       (S3.4)

For every prime p its exponent is exactly

    max(0, v_p(q_M)-v_p(|h|)-v_p(16^d-1)-j*v_p(16)).  (S3.5)

This retains all prime powers. Since
`16^d-1=product_(e|d)Phi_e(16)`, its valuation is the **sum** of the
valuations of these cyclotomic factors. Distinct cyclotomic values may share
primes; treating them as pairwise coprime loses information.

For a complete local phase representation, factor the reduced conductor as
`q=product p^a`; put `Q_p=q/p^a` and take `u_p Q_p=1 mod p^a`. Then

    e(A/q)=product_(p^a||q) e(A*u_p/p^a).

The inverses are necessary. Factorization into unit-modulus local characters
does not make those phases independent over the short time window. No
complete-period estimate has been substituted for that window here.

## SG-S4. Exact dyadic preperiod of odd BBP truncations

The collapsed authentic forcing is

    r(n)=(120n^2-89n+16)
          /[(2n-1)(4n-1)(8n-7)(8n-3)].                (S4.1)

Its denominator is odd for every integer `n>=1`; reduction cannot introduce
an even denominator. For odd n its numerator is odd as well. If M is odd,

    16^(M-1)*P_M=sum_(n=1)^M16^(M-n)*r(n)
                =16*R+r(M),

where R has odd denominator. The right side has odd numerator and odd
denominator in lowest terms: after bringing to an odd common denominator,
the first numerator is even and the second is odd. Hence

    v_2(q_M)=4(M-1)                       (M odd).     (S4.2)

For a reduced rational `a/q` with `q=2^v*q_odd`, the orbit under multiplication
by 16 has exact preperiod `ceil(v/4)`. Before that time, a return after any
positive period l would require `q | a*16^j*(16^l-1)`; when `v>0`, a and
`16^l-1` are odd, so this requires `4j>=v`. The condition is automatic
when `v=0`. At `j=ceil(v/4)`, the remaining
denominator is odd, so multiplication by 16 is invertible and periodic.
Applying this elementary fact to (S4.2) proves

    the exact preperiod of P_M is M-1, for every odd M. (S4.3)

Thus when an odd `M>=N` certifies pi's required N-window via (S3.3), at most
one of the samples `j=0,...,N-1` has reached the periodic odd-conductor orbit.
A theorem averaging a full period of that eventual orbit does not estimate
this initial window. For lag characters the odd factor `16^d-1` cannot
remove any dyadic conductor. A fixed h removes only `v_2(h)` dyadic powers.

This is a precise no-go for an **unjustified complete-period substitution**,
not for rational approximation or incomplete exponential-sum methods.
The numerator A_M, its odd denominator, and correlations among the local
phases remain potential useful source information.

## SG-S5. An unconditional logarithmic deficit for the actual pi orbit

This section imports a different, classical arithmetic source. The published
Zeilberger--Zudilin theorem implies `mu(pi)<8`; see
[the primary 2020 paper](https://arxiv.org/abs/1912.06345v2) and its
[author-hosted manuscript](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/pimeas.pdf).
Only that coarse inequality is used, not a claim about the currently best
record. The theorem in that paper is external mathematical authority, not a
new local Lean proof.

It follows that there exists `c_pi>0` such that, for all integers p and all
integers `q>=1`,

    |pi-p/q| >= c_pi*q^(-8).                          (S5.1)

Indeed the irrationality-exponent theorem handles sufficiently large
denominators; the finitely many remaining denominators have positive nearest
rational distances because pi is irrational. Decrease `c_pi` if necessary
so that `c_pi<=1`. An explicit numerical value for it is not extracted here.

The following elementary argument applies to any irrational real alpha
with (S5.1), with alpha replacing pi. We state its pi specialization.
Fix a nonzero integer m and put

    epsilon=1/18,
    K_m=max(1, ceil(1+log_16(epsilon/c_pi)+7*log_16|m|)),
    B_m=8*(K_m+1)/7.

Call j an escape if `||m*16^j*pi||>=epsilon`, where `||.||` is distance to
the nearest integer. If a consecutive block beginning at s has no escapes,
choose nearest-integer errors `u_j` with `|u_j|<epsilon`. The number
`u_(j+1)-16*u_j` is an integer and has modulus less than
`17*epsilon=17/18<1`. It must vanish. Thus throughout a length-L such block,

    |u_s| < epsilon*16^(-(L-1)).

But (S5.1), used at denominator `|m|*16^s`, gives

    |u_s| >= c_pi*|m|^(-7)*16^(-7s).

Comparison shows `L<=7s+K_m`. Therefore there is an escape in every interval
`[s,8s+K_m]`. Enumerate the escapes increasingly as `g_0,g_1,...`. They exist
indefinitely and obey

    g_0<=K_m,
    g_(i+1)<=8*g_i+8+K_m,
    g_i < B_m*8^i.

Consequently the number of escapes among `j=0,...,N-2` is at least

    max(0, log_8((N-1)/B_m)),                    N>=2. (S5.2)

For the integer count, use all i with `B_m*8^i<=N-1`; the strict upper bound
on `g_i` then places it at most `N-2`. A negative logarithm yields only the
trivial zero lower bound.

Now write `a_j=e(h16^j*pi)` and `S_N=sum_(j<N)a_j`, with `h!=0`. Choose a
unit complex z with `Re(conj(z)*S_N)=|S_N|` (any z if `S_N=0`). Then

    sum_(j<N-1)|a_(j+1)-a_j|^2
       <=4*sum_(j<N)|a_j-z|^2
       =8*(N-|S_N|).                                (S5.3)

On an escape for `m=15h`,

    |a_(j+1)-a_j|=|e(15h16^j*pi)-1|
       =2*sin(pi*||15h16^j*pi||) >=4/18.

Here `sin(pi*t)>=2t` for `0<=t<=1/2`, by concavity. Combining (S5.2) and
(S5.3) proves the all-N bound

    |S_N| <= N-(1/162)*max(0,log_8((N-1)/B_(15h))),  N>=2. (S5.4)

In particular, for every fixed nonzero h,

    |S_N| <= N-log(N)/(162*log(8))+O_h(1).             (S5.5)

The signed lag sum is the same type of sum at frequency
`h*(16^d-1)` and length `N-d`, so for `N-d>=2`,

    |C_d(N;pi)| <= N-d
      -(1/162)*max(0,log_8((N-d-1)/B_(15h(16^d-1)))). (S5.6)

These are actual pi-orbit estimates, with an unbounded improvement over
the triangle bound. They are not consequences of general circle dynamics:
the fixed orbit zero violates them. Their load-bearing arithmetic input is
the external finite irrationality exponent, **not the BBP kernel**. The
constant in (S5.4) is existential until `c_pi` is made explicit.

The scale is far too weak for Weyl cancellation. After division by N, the
right side of (S5.5) still tends to one. Nor does it exclude empirical
concentration at a fixed point. The next counterexample shows why that
limitation is essential rather than a cosmetic caveat.

## SG-S6. Finite irrationality measure still permits near-maximal sums

Define the explicit non-BBP source

    alpha=sum_(k>=0)16^(-2^k).

Its hexadecimal expansion has digit one exactly at positions `1,2,4,8,...`,
and zero elsewhere. It is irrational because this digit string is not
eventually periodic: gaps between ones are unbounded and ones occur forever.
This is a fully specified digit source, not a source-faithful counterfeit
of pi or the BBP forcing.

Let `P_k/Q_k` be its truncation through position `2^k`, with
`Q_k=16^(2^k)`. The numerator is odd, so this fraction is reduced. The tail
satisfies

    0<alpha-P_k/Q_k<2/Q_k^2.

For any sufficiently large q choose the least k with `Q_k>=4q`. Then
`Q_k=Q_(k-1)^2<16q^2`. No `p/q` equals `P_k/Q_k`, because equality would
force `q>=Q_k>=4q`. Hence

    |alpha-p/q|
       >=1/(q*Q_k)-2/Q_k^2
       >=1/(2q*Q_k)>1/(32q^3).                       (S6.1)

The finitely many small q can be absorbed into a positive constant. Thus
`mu(alpha)<=3`, proved here without importing a sharp theorem about this
number.

Nevertheless the fractional orbit coordinate is exactly

    {16^j*alpha}=sum_(2^k>j)16^(j-2^k).

For `N>=1`, nonnegative geometric summation gives

    sum_(j<N){16^j*alpha}
       <=(floor(log_2 N)+1)/15+1/225.                 (S6.2)

Each digit position at most N contributes at most `1/15`; for later
positions the sum is at most `1/225`, by domination by all integer
positions `N+1,N+2,...`. Therefore, for each fixed integer h,

    |sum_(j<N)e(h16^j*alpha)-N|=O_h(log N),
    A_(h,N)(alpha)->1,
    N-|sum_(j<N)e(h16^j*alpha)|=O_h(log N).             (S6.3)

So even a much stronger finite irrationality exponent than the one used
for pi is compatible with nonnormality and logarithmic-order deficit.
The logarithmic baseline cannot be promoted to cancellation from those
arithmetic premises alone. This is a rigorous limitation of that premise
class, not a no-go for the particular BBP source.

## SG-S7. Ledger, provenance, and the next decisive theorem

| Claim | Status and source | What is actually controlled | Remaining gap |
|---|---|---|---|
| Single-frequency O(1) transport | Prior project paper result; classical perturbation method | Difference of pi and forced sums | No cancellation of either |
| Uniform-lag two-time transfer (S2.2)--(S2.4) | New-to-project paper derivation from authenticated BBP tail | Complex correlation transport error, all horizons and lags | Forced correlation size |
| Simultaneous rational approximation (S3.2) | New-to-project paper derivation, exact BBP remainder | Absolute approximation error O_h(N^-2) at horizon-matched depth | Incomplete sum at full rational conductor |
| Odd-depth exact dyadic preperiod (S4.3) | Elementary all-M arithmetic derivation | Exact location of the eventual periodic regime | No estimate for the preperiod sum |
| Pi logarithmic deficit (S5.4)--(S5.6) | New-to-project consequence of imported classical irrationality measure | Actual sum modulus below trivial bound by an unbounded logarithm | Far weaker than o(N); no BBP-specific cancellation |
| Finite-measure sparse source (S6.1)--(S6.3) | Paper counterexample with complete source contract | Refutes finite irrationality exponent implying cancellation | Does not share exact BBP source |
| Pi base-16 normality | Unproved | None of these results establishes it | All required fixed-mode o(N) estimates |

The independently assigned agents share the same model family and inherited
source dossier. They are independent derivation tracks, not independent
external witnesses. The source-specific beta bounds, BBP source identity,
and exact rational forcing are common mathematical dependencies. The
irrationality-measure theorem is a distinct external source family. No
counting of source echoes as independent corroboration is intended.

In Aletheia terms: direct contact `kappa` comes from the source formulas,
exact algebra, and authenticated pi identity; toolkit-relative survival
`phi` is limited to these statements and their stated probes; `sigma`
distinguishes BBP, external irrationality theory, and hostile non-BBP
sources; commitment risk `rho` is controlled by explicitly retaining
normality as open. The actual Fourier signs supply the operational common
basis in (S2.1); no invented phase or quantum interpretation appears.

The smallest genuinely verdict-changing source theorem is an independently
proved sublinear bound for a fixed authentic BBP forced Fourier mode, or
for an appropriately weighted family of its signed lag correlations that
implies that bound. The transport cost is now bounded uniformly in lag,
and horizon-matched rational truncation costs only O_h(N^-2). Thus neither
source approximation error nor loss of cyclotomic signs needs to be the
obstruction. What is still missing is an estimate for the **incomplete,
source-selected rational phase sum itself**, using more than positivity,
finite irrationality measure, or an eventual complete-period distribution.
