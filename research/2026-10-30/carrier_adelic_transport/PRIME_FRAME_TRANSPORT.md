# Rational frames, prime valuation changes, and the selected BBP first jet

## Scope and lineage

Exact parent inspected: SUCC PR #417, `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
The multiplicative source carrier is inherited from PR #416 and independently
audited by #417. The Q/Z primary decomposition and exact joint CRT phase
factorization are classical and already present in main (`NCB-07`, `PCG-09`)
and drafts #398/#399. The dyadic source isometry and exact `F(0)=0` are already
proved in main's `PI_DYADIC_SOURCE_ISOMETRY.md`; no rediscovery is claimed.

This bearing contributes a concrete **prime-value changes -> real derivative**
operator with rigorous source-specific accuracy, a precise local carry seam,
and an observation-kernel classification. These repair interfaces; they do
not bound a selected Weyl sum. Every theorem below is elementary paper-level
mathematics, supported by exact rational probes, not a Lean certificate or
independent external referee. No scholarly-priority claim.

## Hole contract

**Question.** Can observations at prime places of the same multiplicative
carrier recover its selected real first jet, with explicit finite accuracy?

**Domain.** Natural time n>=1, rational source shift u near zero, original
four-pole rational potential V, initial function B0(u)=1. Rational alternative
initial jets are declared controls. Irrational initial jets are a different
real carrier and are not silently assigned rational p-components.

**Proposed sufficient statement.** All-prime valuation differences between
two rational source frames recover a logarithmic secant, whose error from
the selected first jet has explicit source-derived upper and lower bounds.

**Falsifiers.** Wrong sign of secant error, failure of factorization at a
rational frame, neglected initial-function contribution, omission of a CRT
inverse or integer carry seam, or a purported exact finite-frame derivative
without a regularity/degree restriction.

**Novelty tax.** The local additive character product is inherited. The
new-to-this-round mixed operator changes what is observed: valuations at a
varying rational frame, rather than fixed point valuations; its precision
bound shows exactly how the real derivative is recovered. Its limitation
is quantitative and independently testable. It does not supply the missing
signed time-occupation estimate.

## 1. Algebraic carrier and exact additive observations

Write D=Q[epsilon]/(epsilon^2). Every unit is uniquely

    j=a(1+q epsilon),  a in Q*, q in Q.

Multiplication is `(a,q)(c,r)=(ac,q+r)`, integer powering is
`(a,q)^m=(a^m,mq)`, and the logarithmic first-jet map L(j)=q is a group
homomorphism. The value projection j->a has the entire additive q-coordinate
as its kernel. This is the precise fixed-value blindness, not a failure of
ordinary prime factorization of a known rational number.

For

    R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
    V(a)=a^4/[(a+3)^2(a+4)(a+5)],  a_j=8j-7,
    B_n(u)=product_(j=1)^n V(a_j+u)^(16^(n-j)),

the first jet is `j(B_n)=B_n(0)(1+U_n epsilon)`, with
`U_0=0`, `U_n=16U_(n-1)+R(a_n)`. Changing B0 to `1+s u`, s rational,
changes U_n by 16^n s and leaves B_n(0) unchanged.

For a reduced rational q=m/d and a prime p^a||d, define

    c_p(q) = (m*(d/p^a)^(-1) mod p^a)/p^a in [0,1).

Set c_p(q)=0 if p does not divide d. This is the canonical p-adic
principal part. The difference `q-sum_p c_p(q)` lies in every Z_p and
is rational, hence is an integer. Thus, with e(t)=exp(2*pi*i*t),

    e(hq) = product_p e(h*c_p(q))  for every h in Z.

The product is finite. In the usual adelic convention
`psi_infty(x)=e(-x)`, `psi_p(x)=e(c_p(x))`, their product is 1 on the
diagonal rational carrier. Reversing both signs is equally valid; mixing
them is not. These are declared classical character phases.

This is `Q/Z ~= direct_sum_p Q_p/Z_p`, with kernel exactly Z.
It faithfully recovers the circle class of the rational first jet, but
does not recover its integer lift without the lift or an initial condition.

### Authentic p=2 separation

The original source simplifies exactly to

    r(n)=4/(8n-7)-1/(8n-3)-(3n-1)/[(2n-1)(4n-1)].

Its denominator is odd at every integer n. Therefore U_n(0) has odd
denominator and `c_2(U_n)=0` for every n, even though
`v_2(B_n(0))=-(16^n-1)/3` is highly nontrivial. The multiplicative value
valuation and the additive first-jet phase are different observations.
The full 2-adic integral residue of U_n is informative (as main already
proves), but its additive principal character alone is trivial.

## 2. The exact local-to-global carry seam

This statement applies to any rational forcing r_n, integer radix b>=2,
rational seed, and q_n=bq_(n-1)+r_n. Define finite sums

    S_n=sum_p c_p(q_n),  C_n=floor(S_n),
    R_n=sum_p c_p(r_n),  I_n=r_n-R_n in Z,
    ell_(p,n)=floor(b*c_p(q_(n-1))+c_p(r_n)).

Since principal parts add modulo integers,

    c_p(q_n)=b*c_p(q_(n-1))+c_p(r_n)-ell_(p,n).

The circle state is `x_n={q_n}=S_n-C_n`. Substitution, with no limit,
gives the literal source carry

    kappa_n=floor(b*x_(n-1)+r_n)
           =sum_p ell_(p,n)+I_n+C_n-b*C_(n-1).       (CS)

The integer lift then obeys
`floor(q_n)=b floor(q_(n-1))+kappa_n`. All sums are finite at each time.

The carry is **not** merely the sum of local carries: the global seam
`C_n-b C_(n-1)` and source integer remainder I_n are essential. This gives
an explicit commuting interface from the multiplicative first-jet object,
through all prime principal parts, to the literal arithmetic carry. It
does not identify a forced carry with a pure radix digit after discarding
the Green-tail seam. Pure digits need the separately retained real tail.

At the authentic first step, `r(1)=47/15`, its two principal parts are
`c_3=1/3`, `c_5=4/5`, their sum is `17/15`, the source integer remainder
is 2, and the global seam is 1. Every local carry from the zero seed is
zero, while the literal carry is **3=0+2+1**. This is an explicit mutation
receipt for omitting the global seam or the source integer remainder.

## 3. Exact kernel of a finite-prime observer

Fix a finite prime set S. The kernel of

    q mod Z -> (q mod Z_p)_(p in S)

is exactly the rational classes with denominator supported outside S.
For a prime p outside S and p not dividing b, changing the same-forcing
seed by s=a/p^k changes q_n by b^n a/p^k, which is integral at every
retained prime for every time. Thus the entire S-observation history is
unchanged.

At any chosen time n, a modulo p^k yields every translate of the p^k
uniform mesh because multiplication by b^n is invertible modulo p^k.
For any cylinder depth K, choose p^k>b^K: every one of the b^K radix
cylinders contains some such same-observation seed alias. This is an
exact failure of finite-prime observation sufficiency for a circle phase
or a prescribed finite cylinder. The seed has changed; it is not a
counterexample to the authenticated zero initial jet.

The same statement includes finitely many retained integral p-adic digits.
For prescribed nonnegative precisions K_p at p in S, put
`L=product_(p in S) p^(K_p)` and use seed `s=L*a/q^k`, where the omitted
prime q divides neither b nor L. Then `b^n*s` lies in every
`p^(K_p) Z_p` for all n, while varying a still gives the full q^k phase
mesh. Thus the stronger observation in `Q_p/p^(K_p)Z_p` has the same
all-time alias obstruction. SOURCE_AUTHENTICATION section 4 states this
version separately.

Important provenance/strength limits:

* Draft #399 SC-05 and main #259/#266 lineage already have stronger
  finite-coherence dyadic aliases preserving all odd-primary components
  and carry-prefix constraints. The result here gives a generic kernel
  classification attached to the new jet carrier; it supersedes none of
  that work.
* Rational translations preserve integer-base normality. These finite
  aliases are **not** claimed to have different asymptotic normality.
* The coherent seed `-pi/16` lives in a real first-jet carrier, not the
  rational diagonal Q. It cannot be silently given the same rational
  p-adic first jets. Fixed value valuations still miss it, as #417 proves.

## 4. A genuinely mixed prime-value to Archimedean-jet operator

For integers n,M>=1, let delta=1/M and define

    A_(n,M) = M log[B_n(delta)/B_n(0)].

Both carrier values are positive rational, so unique prime factorization
gives the exact common-basis equality

    A_(n,M) = M sum_p [v_p(B_n(delta))-v_p(B_n(0))] log p.       (PF)

The sum is finite. This is an ordinary real logarithm of a positive
rational ratio. It does **not** differentiate a discrete p-adic valuation
in a real variable. It observes valuation changes at two rational frames
and then applies a declared real linear combination.

The source provides an efficient factorized representation of those
valuation changes, without forming the enormous powered product:

    V(a+1/M)/V(a)
      = (Ma+1)^4 (a+3)^2(a+4)(a+5)
        / [a^4 (M(a+3)+1)^2 (M(a+4)+1)(M(a+5)+1)].

Add these finite prime vectors with weights 16^(n-j). No complexity
claim about factoring the displayed integers is made.

### Theorem PF1: explicit two-sided forward-frame accuracy

For every n,M>=1,

    (38447/44100)*16^(n-1)/(2M)
      <= U_n-A_(n,M)
      <= (6853/1800)*(16^n-1)/(30M).                     (PF1)

In particular A_(n,M)<U_n and A_(n,M)->U_n at each fixed n as M->infinity.

**Proof.** R is completely monotone on a>0, since

    R(a)=integral_0^infinity e^(-a t)
          [4-2e^(-3t)-e^(-4t)-e^(-5t)] dt,

and the bracket is positive for t>0. Therefore `-R'(a)>0` decreases
with a. The fundamental theorem of calculus gives

    U_n-A_(n,M)
      = M sum_(j=1)^n 16^(n-j)
          integral_0^(1/M) integral_0^t [-R'(a_j+s)] ds dt.

For the upper bound every integrand is at most `-R'(1)=6853/1800`;
the geometric weights sum to `(16^n-1)/15`, and the double integral
times M is 1/(2M). For the lower bound keep only j=1 and use
`a_1+s<=2`, hence `-R'(a_1+s)>=-R'(2)=38447/44100`. QED.

**Exact phase consequence.** For every integer h,

    |e(hU_n)-e(hA_(n,M))|
      <= 2*pi*|h|*(6853/1800)*(16^n-1)/(30M).           (PF2)

This transports one selected character through actual prime-frame data.
It is a representation-error bound, not cancellation in a sum over n.
At all times n<=N, choosing `M_n=L 16^n` makes each absolute state error
at most `(6853/1800)/(30L)`; choosing a larger growing L_n makes it vanish.

**Precision scope.** Within this *forward-secant instrument*, fixed absolute
accuracy requires M=Omega(16^n), and M=O(16^n) suffices. This means a source
shift of order 16^(-n), requiring O(n) bits of spacing precision. It is
neither exponential bit complexity nor an impossibility of computing U_n,
which is already an exact rational recurrence. It is not an instrument-
independent lower bound, as the centered comparison below demonstrates.

### Theorem PF2: exact sharp-order constant

Put

    C_n=sum_(j=1)^n 16^(-j)[-R'(8j-7)],
    C_*=sum_(j>=1)16^(-j)[-R'(8j-7)] >0.

Taylor's theorem, using R''>=0 and decreasing, yields

    0 <= C_n/2 - (M/16^n)(U_n-A_(n,M))
       <= R''(1)/(90M),  R''(1)=427261/54000.

Also

    0<C_*-C_n <= [-R'(8n+1)]/(15*16^n).

Hence as n and M both tend to infinity, at arbitrary relative rates,

    (M/16^n)(U_n-A_(n,M)) -> C_*/2.

An exact 24-term rational enclosure gives

    0.2380481176058278013951488115997030192023992 < C_*
      < 0.2380481176058278013951488115997030226094133.

The displayed decimal rounding is outward; the finite rational sum and
its rational tail are the authority. Thus the leading error coefficient
is about 0.1190240588029139006975744057998515. No input digits of pi enter.

### Centered-frame control: forward precision is not universal

For M>=2, set

    A^c_(n,M)=(M/2) log[B_n(1/M)/B_n(-1/M)].

Both frames remain positive rational. Convexity of R and a symmetric
integral remainder give

    R''(3/2)*16^(n-1)/(6M^2)
      <= A^c_(n,M)-U_n
      <= R''(1/2)*(16^n-1)/(90M^2).                    (PF3)

Proof: average the Taylor identity for R(a+t) over -1/M<=t<=1/M.
The odd linear term integrates to zero; the quadratic remainder lies
between R''(a+1/M)t^2/2 and R''(a-1/M)t^2/2. Sum as above.

This instrument needs M=Theta(4^n) for fixed absolute accuracy. Higher
order finite differences can further change the spacing exponent. Such
improvements are classical numerical analysis and provide no statistical
mixing. The forward bound must never be advertised as an absolute barrier.

### A single finite-frame sequence with summable phase error

One need not leave the n versus M limit order unspecified. Choose the
explicit integer frame precision `M_n=16^n n^2` and define

    A_n=M_n sum_p [v_p(B_n(1/M_n))-v_p(B_n(0))] log p.

Every sum uses a finite rational carrier at finite time. PF1 gives

    0<U_n-A_n<6853/(54000 n^2).

Thus for each fixed integer h and every N>=1,

    |sum_(n=1)^N e(h U_n)-sum_(n=1)^N e(h A_n)|
      <= 6853*pi^3*|h|/162000.                         (PF4)

Proof: sum PF2 over n and use `sum n^-2=pi^2/6`. Consequently the two
normalized Weyl sums differ by O_h(1/N). This is an operational common-basis
transport of the genuine zero-seeded selected path to finite prime-value
differences, with a declared moving resolution and paid error. It is also
an equivalent cancellation criterion, **not a new bound on either sum**.
The exact rational recurrence is generally cheaper than this measurement
procedure; no computational advantage is claimed.

## 5. What rational frames do and do not authenticate

For the declared linear seed `g_s(u)=1+s u`, s rational and chosen frames
inside the positive domain, changing seed adds

    M 16^n log(1+s/M)

to A_(n,M). This converges to 16^n s as M grows and is observed through
the prime factors of the positive rational `1+s/M`. Thus varying-frame
prime observations repair the fixed-value blindness **within this
declared seed family**.

They do not identify arbitrary analytic germs from finitely many values.
For example

    g_s(u)=1+s u(1-Mu)

has g_s(0)=g_s(1/M)=1 and g_s'(0)=s. The two sampled prime-value vectors
are identical to the zero-seed model, but the first jet differs. This
does not contradict PF1 because PF1 uses the specified B0 identically1;
the added germ has additional derivative/curvature terms. With any
finite frame set, a polynomial vanishing at those frames gives the same
obstruction. Source passport and initial-function/regularity data must
remain attached to the observer.

## 6. Validation and the exact unproved edge

`adelic_jet_probe.py` checks jet group laws, original four poles including
negative-integer clock holdouts, 560 rational primary decompositions,
CRT-inverse mutation, 200 source-relative carry identities, seam omission,
all-horizon retained-prime seed aliases on finite holdouts, all 256
two-hex-digit cylinders inside one retained-prime fiber, prime-frame
factorization, rational log-interval bounds, linear-seed frame detection,
nonlinear-germ alias, and centered-frame improvement.

The logarithm enclosure uses t=(x-1)/(x+1), x>=1:

    L_J=2 sum_(k=0)^(J-1) t^(2k+1)/(2k+1),
    L_J <= log x <= L_J+2 t^(2J+1)/[(2J+1)(1-t^2)].

Every quantity in this enclosure is rational. All error comparisons are
made between Fractions, without binary floating point.

The missing theorem remains a bound on the **joint signed time product**
of the selected principal characters, or the actual selected carry/
cylinder occupation. PF2 permits an exact finite-source prime-frame
readout to replace a selected phase with controlled error; it does not
show the resulting prime-log phases cancel. Positivity, all-place
factorization, and resolving the zero first jet are not a statistical law.

## Primary/background source audit

Keith Conrad, *The character group of Q*, pp.3-4, equation (2.1), defines
the same p-principal parts and proves `q-sum_p {q}_p in Z`; later sections
explain the adelic sign convention:
https://math.stanford.edu/~conrad/154Page/handouts/characterQ.pdf
(retrieved in this bearing; web reference `turn1view0`).

The primal decomposition is already imported in SUCC's earlier native
carrier and joint-prime dossiers. PF1-PF3 and CS have self-contained proofs
above; their ingredients are elementary factorization, calculus and CRT.
