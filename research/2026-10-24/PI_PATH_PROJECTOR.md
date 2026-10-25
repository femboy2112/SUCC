# Exact interference selects a source history

Date: 2026-10-24. Pinned parent: PR #272, commit
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
Working branch: `research/pi-path-selection-interference-2026-10-24`.
The proof provenance is the frozen hole contract, the inherited Pascal
synthesis and the authentic dyadic source-isometry dossier. Results comprise
elementary finite proofs and the scoped infinite-extension obstruction. Scholarly priority is not claimed. No new Lean
declaration, selected real-carry estimate, or pi-normality proof is asserted.

## 1. Source-derived finite interference projector

Fix q>=2, integer b>=2, increments a_1,...,a_N in G=Z/qZ and initial
selector s in G. For a candidate path x=(x_0,...,x_N), define

    d_0(x)=x_0-s,
    d_j(x)=x_j-b*x_(j-1)-a_j,  1<=j<=N.

Let e_q(z)=exp(2*pi*i*z/q). Set

    P_s(x)=q^(-N-1) sum_(lambda in G^(N+1))
                      e_q(sum_j lambda_j*d_j(x)).

**Theorem 1 (PROVED, finite source selection).** P_s is exactly the
indicator of the unique source history x*_0=s, x*_j=b*x*_(j-1)+a_j.
In particular sum_x P_s(x)=1. As multiplication on functions of paths,
P_s is self-adjoint and idempotent.

Proof: each independent character average is 1 when its defect is zero and
0 otherwise, by the finite geometric series. All factors are one precisely
when the initial condition and every recurrence constraint hold. The forward
recurrence constructs exactly one such path; invertibility of b is unnecessary.
The 0/1 multiplier is self-adjoint and idempotent.

This uses the authentic source to choose constraints, rather than choosing
phases from desired Fourier signs. It is a genuine interference representation
of an exact constraint projector, but its classical selection conclusion is
already implied by the deterministic recurrence and its initial value.

### Normalization and the initial boundary

Omitting d_0 leaves the transition projector

    P_free(x)=q^(-N) sum_(lambda_1,...,lambda_N)
                    e_q(sum_(j>=1) lambda_j*d_j(x)).

It selects q paths, one per initial state. Its total path mass is q, not 1.
For any real rational selector weights sigma(s) with sum sigma=1,

    mu_sigma(x)=sigma(x_0) P_free(x)

has total mass one. It is a probability law when the weights are nonnegative;
otherwise it is a normalized signed measure, not a probability. Delta sigma
selects one path. Uniform sigma averages all q source-consistent histories.

Replacing the phase by e_q(k lambda*d) with gcd(k,q)>1 selects the weaker
constraint q|kd. For example q=9,k=3 accepts defects 0,3,6. Unit k merely
permutes the dual variables and is a harmless calibration change. An incorrect
nonunit multiplier must not be accepted as the same source projector.

## 2. Observable transport and the exact selector dependence

For prescribed integer frequencies h_0,...,h_N define

    H_j=sum_(k=j)^N b^(k-j)*h_k,
    H=H_0,
    C=sum_(j=1)^N a_j*H_j.

Every source path satisfies

    sum_(j=0)^N h_j*x*_j(s)=H*s+C mod q.

Therefore, with sigmahat(k)=sum_s sigma(s)e_q(k*s),

    sum_x mu_sigma(x)e_q(sum_j h_j*x_j)
      =e_q(C)*sigmahat(H).                         (1)

This also follows by summing the path variables first in the interference
formula: their character constraints force the unique backward dual history
lambda_j=-H_j. The remaining boundary value is exactly (1). Thus apparent
exponential interference can be eliminated by finite linear character algebra;
no unproved cancellation over actual time has occurred.

For the endpoint character h_N=h and all other h_j=0,

    endpoint transform=e_q(h*A_N)*sigmahat(b^N*h),
    A_N=sum_(j=1)^N b^(N-j)*a_j.

A delta selector has endpoint character modulus one. A uniform selector has
zero endpoint transform unless q divides b^N*h; when b is invertible mod q,
every nontrivial endpoint character cancels. Both statements hold for exactly
the same transition source. The selector contains the exceptional-source debt.

This is an endpoint/finite-observable formula, not a time-average bound.
Uniquely selected constant and periodic orbits satisfy every projector theorem
above and remain valid negative controls for an inferred normality conclusion.

## 3. Coherent finite horizon marginalization

Summing the terminal coordinate of P_(s,N) gives P_(s,N-1), because every
penultimate state has exactly one allowed successor. The same is true for
mu_sigma. Arbitrary prefix marginals follow by repetition. This is finite
projectivity under horizon truncation; the companion limit dossier states the additional infinite
source-cylinder or mixing theorem and its limit hypotheses.

## 4. Two DIFFERENT carrier transports

### A. Quotient transport (profinite residue coordinates)

If q divides Q, a_j^(Q) mod q=a_j^(q), and s_Q mod q=s_q, then reduction
modulo q sends the selected Q-path to the selected q-path. For compatible
selectors, summing fine path masses over each coarse-path fiber gives the
coarse path mass. A character at coarse frequency h is the fine character
at frequency (Q/q)h. These are quotient/profinite residue assertions.

### B. Denominator inclusion (the actual rational circle)

The actual BBP finite rational phases lie in (1/D_N)Z/Z, where

    D_N=lcm(denominator(r(1)),...,denominator(r(N))).

All D_N are odd. Encode y_j as x_j=D_N*y_j mod D_N and encode forcing as
a_j=D_N*r(j) mod D_N. Then the finite cyclic recurrence with b=16 and
x_0=0 reproduces the exact authentic real-circle source prefix.

For N'>N, D_N divides D_N'. The physical circle embedding is

    Z/D_N -> Z/D_N',  x -> (D_N'/D_N)*x,

not reduction modulo D_N. It preserves phases since
e_(D_N')((D_N'/D_N)x)=e_(D_N)(x), and transports every prefix increment
and state by the same scale factor. The chosen prefixes are coherent under
this inclusion. No canonical quotient of arbitrary finer circle points onto
the coarser circle subgroup is being supplied.

Exact mutation: 1/3 is x=1 in Z/3 and x'=5 in Z/15. Reducing x' mod3 gives
2, corresponding to 2/3, which is the wrong circle point. The denominator
carriers form a direct inclusion system, not the usual inverse residue system.

Likewise, rational reduction modulo q is defined by a/b -> a*b^(-1) only
when gcd(b,q)=1. BBP r(1)=47/15 cannot be reduced that way modulo3 or5.
Those pole-domain failures must be rejected, not silently interpreted as a
circle projection. Synthetic q=3,5,7,9 carriers can still test the universal
projector; full BBP circle prefixes use their actual denominator carriers.

### Integer source lift remains separate

The circle projector constrains forcing modulo one. Adding an integer to a
forcing value leaves its circle constraints unchanged and changes the literal
carry lift. Therefore the authentic BBP receipt additionally retains original
rational forcing, unwrapped U_n, literal c_n, and cumulative C_n, checked via
U_n=y_n+C_n and C_n=16C_(n-1)+c_n. The projector alone is not said to
authenticate that integer lift. At the first source step c_1=3; replacing
r(1) by r(1)+1 keeps y_1 but changes c_1 to4. This negative control is retained.

## 5. Arithmetic payoff and boundary

Earned: source-selected finite path normalization; explicit phase-cancellation
projector; exact backward-dual observable evaluation; finite marginal and
carrier coherence; correction of a potentially serious quotient/inclusion
confusion at the authentic rational-circle source.

Unpaid: cancellation of the time average along the delta-selected BBP history,
conditional central-carry retention, same-law tripling, and the final collision
estimate. The projector can recover any function of the selected history but
does not bound it. Constraining a function and estimating its selected output
are different mathematical tasks.

Next discriminating arithmetic probe: retain the initial delta selector in
(1) and derive a new estimate on the relevant time sum or selected carry
observable from the exact four-pole coefficients. A result that first changes
delta sigma to uniform sigma has changed the source-selection problem.

## 6. Exact finite validation


Exact implementation and reproducer:

* `observational_succ/source_path_projector.py`
* `tests/test_source_path_projector.py`
* `scripts/source_path_projector_probe.py`

The final focused suite ran 25 tests and passed in the reported 0.620 seconds.
The deterministic CLI receipt also ran successfully and reported:

* 90,280 candidate paths across q=3,5,7,9 and horizons1..4, comparing exact
  direct constraints with factorized cyclotomic-character evaluations;
* 52 separately chosen candidate paths with a genuine Cartesian dual oracle,
  totaling 1,354 dual tuples actually enumerated;
* holdout q=11/base5: 14,641 candidate paths;
* 140 selected-initial-state backward-dual observable checks;
* 1,412 prefix marginal checks;
* 43 independently reconstructed authentic BBP rational states across the
  reported finite carriers;
* wrong forcing and initial selectors rejected; omitted initial selector
  changes total mass to q; q=9 with nonunit phase3 falsely accepts27 paths
  instead of1 and produces26 mismatches; wrong normalization gives mass3;
* the constant and period-3 controls remain accepted as legal selected paths;
* both declared carrier transports pass and the 1/3 inclusion/reduction
  conflation fails; BBP r(1) residue reduction at poles3,5 is rejected.

No Cartesian product of all candidate paths and all dual variables was
silently attributed to the factorized checks. The expanded modulus budget
is64; each explicitly enumerated exponential domain is capped at200,000
terms. Large authentic denominator carriers use exact modular arithmetic,
with `expanded_fourier_sum=False` in their receipts.

SHA256 at this check:

    observational_succ/source_path_projector.py
    25603db3fb8c2527f15d7be5d0d4a172c09ed66bbe937a42c060e9e387e817f6
    tests/test_source_path_projector.py
    55bb0db63612b9692c82dc8753ac2126715030c10c16faef4b65d71d53bdb484
    scripts/source_path_projector_probe.py
    d74c4aad5b780376e9c6cb9336488e52953926b23a75534bf5d373d5e60762a8
    observational_succ/bbp_source_memory.py
    dd439f0a2231399d2a0ea4cf0e40a1e399338537723c468e688b0ac7d860fb54

These are scoped finite verification receipts and elementary proofs. No
repository-wide suite, hosted CI, publication, or pi-normality claim is made
by the finite constructor results.

See [selection and limits](PI_PATH_SELECTION_LIMITS.md), [history preservation](PI_HISTORY_PRESERVATION.md), and the [integrated validation record](PI_PATH_SELECTION_VALIDATION.md).

## 7. The raw infinite amplitudes and the projected infinite path differ

Retain both a candidate path and its dual variables in the exact fixed-q
construction:

$$
a_N(x,\lambda)=q^{-(N+1)}
\exp\!\left(\frac{2\pi i}{q}\sum_{j=0}^N\lambda_jd_j(x)\right).
$$

**Proposition.** These complex atomic measures have mass one and are
consistent under terminal-pair marginalization, but have total variation
\(q^{N+1}\). Consequently they have no finite-variation complex Borel
extension to the infinite joint path/dual space.

**Proof.** The total mass is the sum of the projector over all paths, hence
one. Marginalizing \((x_N,\lambda_N)\) contributes exactly \(q\): summation
over \(x_N\) kills every nonzero \(\lambda_N\), and the zero value contributes
\(q\). This changes the normalization to \(q^{-N}\) and gives the preceding
measure. There are \(q^{2(N+1)}\) atoms, each of modulus \(q^{-(N+1)}\).
The variation is therefore \(q^{N+1}\). Apply the necessary variation bound
proved in the limit dossier. QED.

For the genuine finite BBP carrier, \(q=D_N\) varies. Do not reuse the
fixed-alphabet truncation maps without justification. Nevertheless the raw
finite variation is \(D_N^{N+1}\). These cannot all be pushforward marginals
of any one finite-variation complex measure under any proposed compatible
maps, since pushforward cannot increase variation.

After summing the dual variables first, each authentic finite prefix instead
has law \(\delta_{(y_0,\ldots,y_N)}\). Embed every prefix in the same circle
product. Ordinary coordinate truncation is then consistent, and the infinite
law is simply \(\delta_{(y_0,y_1,\ldots)}\).

This is an obstruction to one raw finite-measure interpretation of these
amplitudes. It is not an impossibility theorem about physical path integrals,
nor does it prohibit another operator or distributional limit. Such a limit
needs its own topology, normalization and convergence proof.

The post-discovery [structure receipt](PI_HISTORY_STRUCTURE_RECEIPT.json)
checks the small raw sums and marginals by actual Cartesian enumeration.
The universal argument is the proof above.

## 8. What finite space means here

A bounded circle can contain infinitely many distinguishable mathematical
states. It is not a finite set, and specifying arbitrarily precise states
need not use a bounded amount of information. An autonomous deterministic
map on a finite set eventually cycles. The authentic BBP recurrence instead
has rational states of growing denominator and an explicitly indexed source
clock. None of these mathematical constructions asserts infinite elapsed
computation in finite physical time.

The selected history is generally not shift invariant: shifting changes
its initial state and its forcing index. Selecting one history therefore
does not establish unique ergodicity. The useful remaining object is its
occupation law, and that is the law tested in the preservation dossier.
