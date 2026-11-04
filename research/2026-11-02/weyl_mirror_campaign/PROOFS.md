# Weyl mirror campaign: exact symmetries, a radix-tuned mirror, and arbitrarily slow meshes

Research-only child of PR #475, exact parent `20acb35a42b6ae5fb9260c041ed3a1aa47429484`.
Original four signed poles and literal U0=0 are unchanged. The results below
are paper derivations, not Lean certificates or an unconditional pi-normality
proof. No academic priority claim. Source-selected premises remain OPEN.

## Contract

Write e(x)=exp(2*pi*i*x),

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U0=0, U_n=16 U_(n-1)+r(n),
    alpha=pi/16, X_n=16^n alpha, T_n=X_n-U_n.

Inherit the original BBP identity and positive tail from #474/#475:
`0<T_n<1/(64n^2)` for n>=1. The completed and original Weyl sums differ
by O_h(1), so their normalized fixed-h limits agree. Define
`A_N(h)=N^-1 sum_(n=1)^N e(h U_n)`.

The problem is Weyl equidistribution for pi, NOT Weil positivity for RH.
Do not change the marked initial state when transporting a source object.

## WM-01. Three distinct reciprocal operations

On the complex unit circle, 1/z=conj(z). This is the restriction of the
sphere-Mobius map z->1/z, which swaps the disk and its exterior. It is NOT
a holomorphic self-automorphism of the disk. Disk conjugation is anti-holomorphic.

On the projective REAL line, put C(t)=(1+i*t)/(1-i*t). Direct rational algebra gives

    C(1/t)=-1/C(t).

Thus the standard chart sends reciprocal to x->1/2-x in circle cycles.
The quarter-rotated chart B(t)=i*C(t) gives the exact alternative

    B(1/t)=1/B(t)=conj(B(t))  (real t),

with t=0 and infinity handled projectively. The transformed phase coordinate
is w=i*z, so an original step z->e(r)*z^16 becomes w->i*e(r)*w^16.
The coordinate rotation must transport the dynamics too.

On the ADDITIVE circle R/Z, x->1/x is not well-defined: 1/2 and 3/2 are the
same circle point, but their reciprocals 2 and 2/3 are not. Specify the chart.

Finally, conjugate terms are NOT cancelling terms:

    e(x)+e(-x)=2 cos(2*pi*x).

For example the two phases +/-1/6 have normalized Weyl sum 1/2.
Conjugation symmetry removes an imaginary component, not the real component.

## WM-02. Complete fixed Mobius centralizer and marked-source obstruction

Let P(z)=z^16 on the Riemann sphere. A Mobius map M commuting with P must
permute its critical points {0,infinity}: equivalently P=M^-1 P M, and critical
sets are preserved by conjugation. Therefore M(z)=c*z or M(z)=c/z. Substitution
proves that the COMPLETE centralizer consists of

    M(z)=zeta*z or zeta/z, with zeta^15=1.

For a fixed forced step P_n(z)=a_n*z^16, a_n=e(r(n)), the same argument applies.
Rotations commute iff c^15=1; reflections commute iff c^15=a_n^(-2).
A SINGLE reflection commuting with EVERY source step would require
`2(r(2)-r(3))` to be an integer. But exactly

    r(2)=106/819, r(3)=829/19635,
    2(r(2)-r(3))=133558/765765, strictly between 0 and 1.

Hence the common fixed Mobius centralizer of the forced system contains only
the 15 rotations. Requiring the marked phase z0=e(U0)=1 leaves ONLY identity.
This rules out a fixed source-preserving Mobius mirror, not arbitrary
approximate couplings, non-Mobius maps, or time-reindexing schemes.

In additive cycles, J_beta(x)=beta-x satisfies

    J_beta F_r = F_(-15*beta-r) J_beta,
    J_beta F_r - F_r J_beta = -15*beta-2*r (mod 1).

It intertwines DIFFERENT labelled forcings unless the displayed defect vanishes.

The completed pi orbit also is not paired into itself by a nonidentity member
of the above power-map centralizer. A reflected time equality would imply
`(16^m+16^n)*alpha = k/15 + integer`, contradicting irrationality of alpha.
The rotation case similarly gives `(16^m-16^n)*alpha` rational unless m=n
and the rotation is identity. This is exact finite pairing exclusion only.

Allowing time-dependent mirrors does not avoid marking the seed. An intertwiner
`J_n(x)=beta_n-x` obeys `beta_n=16*beta_(n-1)+2*r(n)` modulo 1. If J0 fixes
U0=0, beta0=0 and induction gives beta_n=2*U_n: J_n fixes the actual state at
EVERY time. It generates no partner. Pulling conjugation back through the
Green-tail chart gives beta_n=-2*T_n; beta0=-2*alpha, so it changes the initial
state instead. It is not a zero-seed symmetry.

Even invariance under the ENTIRE finite centralizer would not imply Haar:
the uniform measure on {k/15:0<=k<15} is x16-invariant, rotation/reflection
invariant under this group, but its h=15 Fourier coefficient equals 1.

## WM-03. Original odd-denominator arithmetic forbids exact two-term cancellation

Combine, do not discard, the two even poles:

    r(n)=4/(8n-7)-1/(8n-3)-(3n-1)/[(2n-1)(4n-1)].

All denominators on the right are odd. Thus every original U_n has an odd
reduced denominator. For integer h, h(U_n-U_m) cannot equal 1/2 modulo 1.
Consequently NO TWO original equal-weight h-characters are exactly negatives.
Likewise U_n+U_m cannot equal 1/16 modulo 1: the tuned mirror below has no
exact finite-source partners. These are universal elementary parity facts.

They do NOT prevent approximate pairing, multi-term cancellation (three odd
roots of unity already sum to zero), or asymptotic equidistribution. An
argument demanding exact two-term cancellation is simply stronger than needed.

## WM-04. A fixed RATIONAL, radix-tuned mirror is sufficient at the measure level

**Theorem.** Let T(x)=b*x mod 1, b>=2 integer, J(x)=1/b-x mod 1. For any circle
probability measure mu,

    T_*mu=mu and J_*mu=mu  =>  mu=Haar.

Proof: T J=J0 T, where J0(x)=-x. Therefore the two hypotheses imply J0_*mu=mu.
Composition J J0=R_(1/b) implies invariance under rotation by 1/b. Fourier
coefficients vanish unless b divides h. If h=b^v*g with b not dividing g,
T-invariance gives mu_hat(h)=mu_hat(g)=0. All nonconstant coefficients vanish,
so mu is Haar. No independence, irrational-axis theorem, or mixing assumption.

For b=16 the useful mirror is J(x)=1/16-x, not plain conjugation J0 and not
the unrotated reciprocal J_(1/2). This is a sufficient STATISTICAL invariance,
NOT the false assertion that J commutes with the original forced steps.

Relation to prior work: #451 AR-03 uses one fixed irrational axis; #453 uses
harmonic-dependent source-native axes to avoid small divisors. Here a single
rational axis suffices because resonant frequencies are removed using radix
frequency reduction. This is a different, elementary specialization, not a
claim that the earlier theorems were wrong or that pi has the symmetry.

## WM-05. Uniformly conditioned one-mirror criterion and exact transport observable

Define one real quadrature for every h>=1:

    B_N(h)=N^-1 sum_(n=1)^N sin(2*pi*h*U_n - pi*h/16).

The authentic Ward bound is

    |A_N(16h)-A_N(h)| < (2+165*h/56)/N.                 (5.1)

For completeness, an exact source inequality proving its budget is

    15/(64*n^2)-r(n+1)
      =(5696*n^3+7672*n^2+2910*n+225)
       /[64*n^2*(2*n+1)*(4*n+3)*(8*n+1)*(8*n+5)] > 0.

Hence sum_(n>=1)r(n+1)<15/32, using sum n^-2<2, and the two shifted endpoints
cost 2/N. Use |e(t)-1|<=2*pi*|t| and pi<22/7 for (5.1).

Put Z=A_N(h), E=A_N(16h)-Z and D_h=Z-e(h/16)*conj(Z).
Then |D_h|=2|B_N(h)| and exact subtraction gives

    (1-e(h/16))*conj(Z)=D_h-D_(16h)+E-conj(E).

For 16 not dividing h,

    |A_N(h)| <= [|B_N(h)|+|B_N(16h)|+(2+165*h/56)/N]
                 / |sin(pi*h/16)|
              <= 8[|B_N(h)|+|B_N(16h)|+(2+165*h/56)/N]. (5.2)

Indeed the nonzero residue classes give |sin(pi*h/16)|>=sin(pi/16)>=1/8.
For general h=16^v*g, 16 not dividing g, telescope (5.1):

    |A_N(h)-A_N(g)| <= [2v+(11g/56)(16^v-1)]/N.       (5.3)

Thus `B_N(h)->0 for every fixed positive h` is EQUIVALENT to original
base-16 pi normality. This is a conditioned criterion; its source premise
has NOT been proved. There are no growing-h small divisors in (5.2).

**One exact rational diagnostic.** Let mu_N be the first N original phases.
On representatives in [0,1), define

    W_N = W1_interval(mu_N, J_*mu_N)
        = N^-1 sum_i |x_(i)-y_(i)|,
    y_i=(1/16-x_i) mod 1,

where the two lists are sorted separately. This is the standard one-dimensional
monotone coupling, and equals the integral of |F_mu-F_Jmu|. It is EXACTLY rational
for these original states, computable by sorting; no trig or pi digits are inputs.
For each fixed h, Lipschitz transport gives

    |A_N(h)-e(h/16)*conj(A_N(h))| <= 2*pi*h*W_N,
    |B_N(h)| <= pi*h*W_N.

Insert in (5.2)-(5.3) to obtain the program's rational upper certificate, using
pi<22/7. In particular

    W_N -> 0 for ALL prefixes N  =>  pi normal base 16.

Conversely normality implies W_N->0, since both empirical distributions
converge to uniform on [0,1] (the reflection has only finitely many discontinuity
points in this chart, all Haar-null). So this is a scalar EQUIVALENT reformulation,
not a newly proved decay rate. The original all-N estimate remains OPEN.
Do not use only dyadic-prefix mirror statistics to claim all-prefix normality.

## WM-06. Positive Fejer energy controls EVERY partial epoch

For any A-point circle configuration and even m>=2, inherit #475's definitions

    F_m(t)=(2/m)*|sum_(j=0)^(m/2-1) e(j*t)|^2 >= 0,
    Q_(A,m)=A^-2 sum_(n,t) F_m(x_n-x_t),
    E_(A,m)=(m/A^2)*sum_(i<m) v_i^2,
    (2/pi^2) E <= Q <= c_F E, c_F=3/2+pi^2/6.

**Hereditary lemma.** For ANY subset I of the epoch,

    sum_(n,t in I) F_m(x_n-x_t) <= A^2 Q_(A,m).        (6.1)

This uses POINTWISE nonnegativity, not just positive semidefiniteness of a
Gram matrix. The rank-one kernel e(h(x-y)) is PSD but its full quadratic sum
can vanish while a subset has positive quadratic sum; that tempting mutation
fails and is tested explicitly.

Now take a true radix orbit X_n=16^n alpha, a fixed h!=0 and full epoch [A,2A).
For EVERY 0<=L<=A put s_L(h)=sum_(n=A)^(A+L-1) e(h X_n).
Let K=#{k>=0: |h|*16^k<=m/4}. If K>=1, exact index shifting gives

    |s_L(h*16^k)-s_L(h)| <= 2k.

Each of these modes has twice its Fejer weight at least 1. Equations (6.1)
and Fourier expansion therefore imply

    A^2 Q_(A,m) >= K*(|s_L(h)|-2K)_+^2,
    sup_(0<=L<=A) |s_L(h)|/A <= sqrt(Q_(A,m)/K)+2K/A.  (6.2)

No growth rate for m other than what is used below has entered. Crucially this
controls arbitrary partial epochs, resolving the all-prefix issue without the
power-scale gluing/discarded-prefix choices in parent MSA-05.

## WM-07. Arbitrarily slow-growing mesh sufficient theorem

**Theorem.** For EVERY dyadic A choose an even integer mesh m_A with

    2<=m_A<=A, m_A->infinity.

No monotonicity or power law is required. If the authentic zero-seeded source
satisfies

    E_(A,m_A) = o(log m_A)  as dyadic A->infinity,      (7.1)

then pi is normal to base 16. Premise (7.1) is OPEN.

Proof, including error and arbitrary prefixes:

1. The original Gamma tail gives, for every 2<=m<=A,

    |sqrt(Q_U-1)-sqrt(Q_X-1)|
       <= pi*m^(3/2)/(sqrt(12288)*A^2).                (7.2)

For each h, the normalized epoch Fourier sum changes by at most
pi*h/(32*A^2); apply the weighted Hilbert norm triangle inequality and
sum_(1<=h<m/2) h^2 <= m^3/24. This specializes to parent MSA-04 at m=A.
The error is O(A^-1/2) uniformly on the stated mesh range.

2. The two-sided energy comparison and (7.1)-(7.2) imply Q_X=o(log m_A).
For fixed h, K_A~log_16(m_A), K_A->infinity and K_A/A->0. Equation (6.2)
therefore gives sup_L |s_L(h)|/A ->0.

3. Decompose an arbitrary initial interval into complete dyadic epochs and
one last partial epoch. Given epsilon>0, all sufficiently large epochs have
partial-sum bound epsilon*A. Their lengths sum to <2N; the finitely many
earlier phases cost O(1). Divide by N, then let epsilon decrease to zero.
Weyl's criterion and the inherited original BBP tail prove the implication.

**Explicit slower target:** for A=2^j let m_A=max(2,2^floor(log2 j)). Then
m_A is comparable to log A. The sufficient premise becomes

    E_(A,m_A) = o(log log A).                          (7.3)

A uniform O(1) bound at these logarithmically many bins would suffice. This is
NOT the invalid weakening E=o(log A) at arbitrary slow meshes: the denominator
must also change to log m_A. The proof does not establish (7.1) or (7.3).
An existential, adaptively chosen slow schedule can merely repackage normality;
keep the EXPLICIT logarithmic schedule for a substantive source-arithmetic target.

## WM-08. What an actual cancelling permutation must certify

For a permutation tau of a finite N-sample, define

    c_h(tau)=N^-1 sum_n ||h(x_tau(n)-x_n)-1/2||_(R/Z).

Since the permutation preserves the sum, twice the Weyl sum is the sum of
paired characters. The elementary chord bound gives

    |N^-1 sum_n e(h*x_n)| <= pi*c_h(tau) <= (22/7)c_h(tau). (8.1)

This is genuine antiphase pairing, not conjugate pairing. It is valid for ANY
permutation, need not be an involution, and requires no circle automorphism.
The program uses one feasible cyclic half-rank match of the sorted h-phases,
NOT a claimed optimal assignment. For even N it is an involution. Exact parity
WM-03 forces positive finite costs for original states; costs can still tend zero.
A source-derived all-N vanishing cost for each fixed h would prove normality.
Finite small costs alone do not prove this. Multi-way source-specific cycles
are an alternative that avoid demanding exact bipartite cancellations.

## Claim ledger and provenance

WM-01/02/03: disclosed algebra and exact scope-limited obstructions.
WM-04: disclosed elementary measure-rigidity implication.
WM-05: disclosed quantitative equivalence; original mirror decay UNVERIFIED.
WM-06: disclosed positive-kernel/partial-epoch estimate.
WM-07: disclosed sufficient theorem; original energy premise UNVERIFIED.
WM-08: disclosed finite coupling certificate; all-horizon source cost UNVERIFIED.
None establishes pi normality, RH, quantum interference, or physical mechanisms.

Parent dependencies, NOT independent corroboration:
- #451, research/2026-11-01/arctan_reciprocity/PROOFS.md, AR-01..06.
- #453, research/2026-11-01/adaptive_arctan_frame/PROOFS.md.
- #474, original positive tail and source-authentic prime/cofactor decomposition.
- #475, research/2026-11-02/mesoscopic_spectral_army/PROOFS.md, MSA-01..07.

Primary/classical sources checked:
- Sabine Boegli, Complex Analysis II (2023-24), Mobius and disk automorphisms:
  https://maths.dur.ac.uk/users/sabine.boegli/CA2.html
- Jeffrey C. Lagarias, On the Normality of Arithmetical Constants (2001):
  https://arxiv.org/abs/math/0101055 . Generic perturbed/radix conjugacy is not
  a source-selected normality theorem.
- Bailey and Crandall, On the Random Character of Fundamental Constant
  Expansions (2001), DOI 10.1080/10586458.2001.10504441.
- Weyl criterion, Fejer nonnegative kernels, quantile/CDF transport, and
  uniqueness of Haar from Fourier coefficients are classical ingredients;
  their elementary use here is not an academic novelty claim.
