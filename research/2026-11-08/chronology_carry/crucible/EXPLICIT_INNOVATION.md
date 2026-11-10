# A bounded signed innovation with exponentially fading carry memory

**Status: PROVED PAPER, with exact finite algebra checks.** This appendix
resolves a particular observer inverse limit and bounds its memory cost.
It does not prove its original-zero time mean is zero. The finite Poisson
and retrodiction identities are [CCV1-L and CCV7](../theory/THEOREMS.md).
All original four-pole states, literal carries and the zero boundary are
retained. The following algebra is elementary; no general novelty is claimed.

## EI1. Closed finite formula, including the literal carry16

The algebra works in any integer base b>=2. Let k>=1, M=b^k, h a nonzero
integer, and let the state word w=(w_1,...,w_k) have entries in {0,...,b}.
Its literal integer code is

    K(w)=sum_(i=1)^k b^(k-i)w_i.

It may exceed M-1; no reduction of the recorded carry word is performed.
The reference transition appends a digit c uniform in {0,...,b-1}; its
operator P acts on all (b+1)^k literal words. Put

    g_k(w)=e(h(K(w)+1/2)/M),
    mu=M^-1 sum_(a=0)^(M-1)e(h(a+1/2)/M),
    psi_k=sum_(j=0)^(k-1) P^j(g_k-mu),
    eta_k(w,d)=psi_k(shift(w,d))-(P psi_k)(w), 0<=d<=b.

P^k g_k=mu, since k reference appends erase the original word, even when
it contains b. Hence (I-P)psi_k=g_k-mu. In particular mu=0 when M does
not divide h, and ||psi_k||_infinity<=k in that case.

Define

    A_(j,k)=b^-j sum_(a=0)^(b^j-1)e(h(a+1/2)/M).

Then the exact formulas are

    (P^j g_k)(w)=A_(j,k) e(h b^j K(w)/M),

    eta_k(w,d)=sum_(j=0)^(k-1) A_(j,k)e(h b^(j+1)K(w)/M)
       *[e(h b^j d/M)-b^-1 sum_(c=0)^(b-1)e(h b^j c/M)].       (EI1)

**Proof.** After j appends, the new literal code differs from b^j K+a by
an integer multiple of M. This is true also for original entries equal to b;
integer h makes that multiple invisible only to the phase. Average over all
b^j ordinary appended words. Also

    A_(j+1,k)=A_(j,k)*b^-1 sum_c e(h b^j c/M).

Insert these identities in psi_k(next)-Ppsi_k. The constant k mu cancels.
QED. No law for the source's actual next carry has been asserted.

## EI2. Uniform amplitude and memory-tail bounds

For d in {0,...,b}, convexity in d gives

    b^-1 sum_(c=0)^(b-1)|d-c| <= (b+1)/2.

Using |e(u)-e(v)|<=2 pi |u-v| and |A_(j,k)|<=1, the jth summand in EI1
has modulus at most pi |h|(b+1)b^j/M. Therefore, with

    C_(b,h)=pi |h|(b+1)/(b-1),

one has

    ||eta_k||_infinity <= C_(b,h)(1-b^-k) < C_(b,h).            (EI2a)

This improves the generic 2k bound from the finite Poisson compiler. For
ordinary next digits d<=b-1 the same argument gives the sharper constant
pi |h|, because the average absolute distance is at most (b-1)/2.

Keep only the summands j=k-R,...,k-1, for 1<=R<=k. The omitted part is at
most

    C_(b,h)(b^-R-b^-k) <= C_(b,h)b^-R.                       (EI2b)

The retained part depends only on the last R-1 literal digits of w and the
new digit d. To see this, write l=k-j. Its phase is
e(h K(w)/b^(l-1)), and adding any multiple of b^(l-1) to K changes no value.
Thus there is an explicit O(R)-term evaluation, without enumerating the
(b+1)^k table. This is a bound on information needed to evaluate a signed
statistic, not a prediction-error claim for the current full phase.

For b=16, C_(16,h)=17 pi |h|/15. Literal16 events are included exactly;
no spill-exception term is necessary in EI1--2.

## EI3. A continuous infinite-past observer with a uniform certificate

For l>=1 put

    a_l=e(h/(2b^l))*sinc(pi h/b^l), sinc(t)=sin(t)/t.

For an infinite literal past v=(...,v_-2,v_-1,v_0), each v_i in {0,...,b},
write K_(l-1)(v)=sum_(i=0)^(l-2)b^i v_(-i), with K_0=0. Define

    eta_infinity(v,d)=sum_(l=1)^infinity a_l e(h K_(l-1)(v)/b^(l-1))
       *[e(h d/b^l)-b^-1 sum_(c=0)^(b-1)e(h c/b^l)].          (EI3a)

Every term has modulus at most pi |h|(b+1)b^-l. Consequently the series
converges uniformly on the compact finite-alphabet history space and
d in {0,...,b}. It is continuous in the product topology, with

    ||eta_infinity||_infinity<=C_(b,h),
    ||eta_infinity-eta_infinity^(R)||_infinity
       <=C_(b,h)b^-R.                                      (EI3b)

Here eta_infinity^(R) is the first R terms. Histories agreeing in their
last R-1 digits have outputs differing by at most2 C_(b,h)b^-R at the same
next digit. These are uniform finite-certificate bounds, not an appeal to
pointwise convergence at a moving source time.

If M>|h|, finite geometric summation proves the **common factor** identity

    A_(k-l,k)=c_k a_l,  1<=l<=k,
    c_k=(pi h/M)/sin(pi h/M),
    eta_k(w,d)=c_k eta_infinity^(k)(v,d),                    (EI3c)

where v has w as its last k digits. The sine denominator is nonzero under
M>|h|. Thus

    |eta_k(w,d)-eta_infinity(v,d)|
       <=C_(b,h)(|c_k-1|+b^-k),                            (EI3d)

uniformly over every extension v of w. For M>=4|h|, the elementary bound
sin t>=t-t^3/6 for 0<=t<=1 and pi^2<10 give

    0<=c_k-1<=2h^2/M^2,
    |eta_k-eta_infinity|<=C_(b,h)(b^-k+2h^2 b^(-2k)).         (EI3e)

**Proof of EI3c.** The midpoint geometric sum is

    A_(k-l,k)=e(h/(2b^l))*sin(pi h/b^l)
               /[b^(k-l)sin(pi h/b^k)].

Factoring its denominator gives EI3c. The bounds follow by adding the
uniform series tail; |eta_infinity^(k)|<=C_(b,h). QED.

This is a lawful inverse-limit extension: finite alphabets provide the
compact history carrier, the formulas are cylinder-continuous, and one
summable bound works for every source history. It supplies no arithmetic
typicality theorem for the history selected by the original zero source.

### The canonical carrier is the integer lift in Z_b

The history series descends through the continuous map

    v -> C(v)=sum_(i>=0)b^i v_(-i) in Z_b.

Literal digits equal to b are permitted: their contributions propagate in
the b-adic sum, rather than being discarded coordinatewise. Every phase
e(h K_(l-1)/b^(l-1)) depends only on C(v) modulo b^(l-1). Consequently
EI3 defines a unique continuous observer

    Phi_h: Z_b x {0,...,b} -> C,

with the same uniform tail bound. Appending d transports its state by
C->bC+d. These maps commute with every quotient Z_b->Z/(b^k); no new
category structure or arbitrary phase identification is required.

For the actual source, write C_n=floor U_n. The exact literal-carry sum
telescopes to

    K_n=C_n-16^k C_(n-k),
    g_k=e(h[(C_n mod16^k)+1/2]/16^k).

Thus the real/2-adic transport used here is the **same authenticated
integer lift C_n**, in its ordinary and 16-adic roles. It is not an
identification of the rational 2-adic state U_n with its real fractional
phase, and it does not substitute an independent Haar 2-adic shadow.
Retaining C_n modulo16^k uses 4k bits and the exact update
`S_(n+1)=(16 S_n+kappa_(n+1)) mod16^k`; a literal16 carry is included
with its propagation. This is a sufficient state size, not an unconditional
memory lower bound for a singleton known zero source.

This connects to the archived [joint carry cocycle, JCC-06](../../../2026-11-03/joint_carry_cocycle/PROOFS.md),
which preserves the ordinary integer lift when relating real and 2-adic
source data. Its channel principal fractions, channel-gluing binary carry,
and the present floor residue are distinct observables. The maps above,
rather than a shared name or an independent local Haar model, establish
the common carrier used here.

## EI4. The observer transports the remaining gate; it does not pay its sign

Set b=16 and use the **actual** literal source carries. Before the initial
time, extend them by zero; the tail estimate makes this convention explicit
and asymptotically immaterial at distant epochs. Observe eta_infinity at
the transition from the past ending at n to the actual next carry kappa_(n+1).
Equivalently evaluate Phi_h(C_n,kappa_(n+1)) on that exact integer lift.
This observation is available at time n+1. It is not a current-time phase
predictor that secretly reads the future: the original frozen predictive
experiment uses carries only through n, whereas this separate signed
innovation explicitly has a one-transition observation delay.

For A>k>=1, N=A, let

    epsilon_(A,k,h)=pi |h|16^-k+2pi |h|/[15(A-k+1)^2].

The source-retrodiction identity in CCV7 gives

    |W_A(h;0)-mean_(n=A)^(2A-1)eta_k(w_n,kappa_(n+1))|
       <=4k/A+epsilon_(A,k,h),

once 16^k does not divide h. Combining this with EI3e, when 16^k>=4|h|,

    |W_A(h;0)-mean eta_infinity|
       <=4k/A+epsilon_(A,k,h)
          +C_(16,h)(16^-k+2h^2 16^(-2k)).                  (EI4)

Choosing k->infinity with k=o(A) makes this comparison vanish. For each
fixed nonzero h, decay of the original-zero eta_infinity mean is therefore
**equivalent** to the original Weyl gate. It is not a weaker conjecture.
More quantitatively, take k=ceil(log_16 A), for sufficiently large A.
Then 16^-k<=1/A, k=O(log A), and (EI4) proves the unconditional transport

    |W_A(h;0)-mean_(n=A)^(2A-1)Phi_h(C_n,kappa_(n+1))|
       =O_h(log A/A).

This rate concerns the difference of the two signed statistics. It is
not a bound on either statistic's absolute value.
The advantage is the explicit bounded signed carry observable and its
exponentially small memory truncation; its arithmetic signed mean remains
unbounded by the results here.

For every past v, the **reference** average

    b^-1 sum_(d=0)^(b-1)eta_infinity(v,d)=0

holds term by term. Applying this conditional average to the actual next
carry without a separately proved source theorem would replace the selected
path by a uniform-branch ensemble. That is exactly the archived
[CE-03 selection trap](../../../2026-11-03/circle_path_electric/PROOFS.md),
now displayed for a source-history observable rather than silently invoked.
The [earlier operator-domain audit](../../../2026-11-04/zero_frame_coupling/EXTERNAL_AUDIT.md)
also distinguishes a martingale/coboundary ensemble statement from the
literal seed. No external concentration theorem is imported here.

## EI5. An exact coherent control survives the entire inverse limit

For a constant past digit d in {0,...,b}, the actual append d leaves that
word unchanged. Hence eta_k=g_k-mu exactly. When M>|h|,

    eta_k(d,d,...,d;d)
       =e(h[d(M-1)/(b-1)+1/2]/M)
       -> e(hd/(b-1)).                                    (EI5)

In particular the constant hexadecimal carry15 history has limiting
innovation1 for every integer h. This is also an actual same-forcing hostile
history: for s_*=-pi/16 the exact completion gives U_n(s_*)=-T_n with
0<T_n<1 at late times. Its floors are all -1 and therefore its literal
carries are all15. It retains the four-pole forcing but fails the original
zero-boundary signature. No rational principal part is assigned to this
irrational seed. The observer correctly retains, rather than erases, its
coherent signed signal.

On the canonical carrier this is the fixed point C_n=-1 in Z_16, with
`16*(-1)+15=-1` and **Phi_h(-1,15)=1**. It is a counterexample to a
seed-blind zero-mean theorem for the compact observer, despite its exact
uniform-reference conditional mean zero.

Thus finite memory approximation, continuity, source-compatible phase
transport and a zero reference conditional mean all hold while the selected
wrong-seed mean equals1. The needed new theorem is specifically about the
original-zero signed innovation mean. **That theorem remains OPEN.**

## EI6. Exact frequency covariance

For every nonzero integer h, on the entire declared compact carrier,

    Phi_(16h)(C,d)=Phi_h(C,d),
    Phi_(-h)(C,d)=conjugate(Phi_h(C,d)).                    (EI6)

For the first identity, the l=1 term of Phi_(16h) vanishes because its
coefficient contains sinc(pi h)=0. Relabel l=r+1 in all remaining terms:
the coefficient, finite character and centered next-digit factor become
exactly the rth term of Phi_h. Absolute uniform convergence licenses the
reindexing. The second identity follows by conjugating each term; sinc is
real and even. The same statements hold in general base b with16 replaced
by b.

There is also an exact finite precursor: for k>=2,
`eta_(k,bh)(w,d)=eta_(k-1,h)(suffix_(k-1)(w),d)`. Indeed g_(k,bh) is the
pullback of g_(k-1,h), and the additional Poisson summand vanishes after
k-1 reference appends. The exact root-field oracle checks this identity
by embedding the smaller root field into the larger one; it separately
checks conjugation, including literal digits equal to b.

Consequently positive h not divisible by16 suffice to index the remaining
innovation means. This is frequency bookkeeping and agrees with the
source recurrence's asymptotic Weyl-frequency transport. It supplies no
decay for those remaining frequencies. The h=0 Weyl coefficient is not
covered by any of these nonzero-frequency equivalences.

**Pi base16 normality: OPEN. RH: OPEN.**
