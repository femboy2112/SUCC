# Source-labelled Wilson curvature, seed Fisher geometry and positive moment shadows

**Scope (2026-11-01):** Mathematically exact, original four-pole BBP forcing
`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, true selected `U_0=0`.
All real-circle characters are evaluated as `e(t)=exp(2*pi*i*t)` at **integer**
harmonics. Source mutations and initial-seed changes are strictly labelled
countermodels. These are paper derivations from classical affine/Weyl, Hausdorff
moment, orthogonal polynomial and quantum-information instruments; tests verify
finite identities, not universal analytic statements. **Pi normality and RH
remain OPEN.**

## W1. Non-Abelian affine source history produces an exact Weyl Wilson echo

Let `F_n(x)=16*x+r(n)`, with ordered unitary half-density operator
`P_n psi(y)=1/4*psi((y-r(n))/16)` from parent PR444. Matrix composition is
`(a,b)(c,d)=(ac,ad+b)`. Define the based order-comparison loop

`C_(i,j) = P_j P_i P_j^* P_i^*`,

implementing `F_j F_i F_j^{-1} F_i^{-1}`. Direct matrix multiplication gives

`C_(i,j) = T_(15*(r(i)-r(j)))` as a real translation,

where `(T_d psi)(x)=psi(x-d)`. Therefore its **second** (Weyl) loop

`C_(i,j)^* M_h C_(i,j) M_(-h) = e(15*h*(r(i)-r(j))) I`

is an exact STATE-INDEPENDENT complex phase, at any normalized `L2` data state.
It is a valid, source-labelled coherent counterfactual order comparison. No
claim is made that the unmodified deterministic BBP automatically actualizes
both orders, or that an arbitrary Riemann-sphere pole loop is this operator.

For adjacent i=n,j=n+1 set the genuine source curvature displacement

`d_n=15*(r(n)-r(n+1)) > 0`.                        (W1)

The original source admits positive Hausdorff representation
`r(n)=int_0^1 u^(n-1) dmu(u)`, with strictly positive continuous density on
(0,1), inherited from PR440. Then
`d_n=15 int u^(n-1)*(1-u) dmu(u)>0`, and `d_n` is strictly
DECREASING with n. The exact first sample is `d_1=12301/273`.

**Comparison with PR442:** its scalar meromorphic Riemann-sphere contour
records residue periods and abelianized winding numbers. W1 detects the
noncommutation of actual ordered affine operators using a new source-attested
representation. Pole-loop generators are not automatically these F_n; such a
Riemann-Hilbert identification remains unverified.

## W2. Integer circle phase closure of the entire source curvature

The source displacements telescope exactly:

`sum_(j=1)^(N-1) d_j =15*(r(1)-r(N)) =47-15*r(N)`.    (W2)

Since `r(N)->0`, the positive sum converges to `47`. Thus, for EVERY integer
`h` (not arbitrary real h), its full character transport is

`prod_(j>=1) e(h*d_j) =e(47*h)=1`.               (W3)

Finite products equal `e(-15*h*r(N))`. The real translation by 47 is NOT the
identity operator on L2(R), only its INTEGER real-circle characters are trivial.
This 47 is source-specific first-sample arithmetic, not a universal topological
integer, physical action quantum or geometric quantization theorem.

From `P(t)=(1-t)(t^2+2)(t^2+2t+2)` and the factor bound
`(t^2+2)(t^2+2t+2)<=15` on `0<=t<=1`,
`0<r(N)<15/[(8N-7)(8N-6)]`. Thus

`|e(h*sum_(j<N)d_j)-1| <=30*pi*|h|*r(N)`
`<450*pi*|h|/[(8N-7)(8N-6)]`.                (W4)

This convergence is independent of the initial BBP seed. An unchanged-forcing
coherent altered seed has exactly the SAME local Wilson holonomies while being
nonnormal.

## W3. The *weighted* same curvatures reconstruct all original BBP states

For arbitrary declared rational initial `s`, the original affine orbit is
`U_N(s)=16^N*s+sum_(j<=N)16^(N-j)r(j)`. Telescoping backward from the
last source coefficient,

`r(j)=r(N)+(1/15)*sum_(k=j)^(N-1)d_k`.

Reversing the two FINITE sums, evaluating a geometric series, gives

`U_N(s) = 16^N*s + (16^N-1)r(N)/15`
`          + (1/225)sum_(k=1)^(N-1)(16^N-16^(N-k))*d_k`. (W5)

Every coefficient is an exact rational source expression. W5 depends on the
chosen INITIAL seed, unlike the curvature d_k. For s=0 it reproduces the
original BBP states, proven by finite summation, not numerical fitting.

At the completed boundary alpha=pi/16 the BBP identity is
`alpha=sum_(j>=1)16^(-j)r(j)`. Because `r(j)->0`, monotone/Tonelli
summation-by-parts yields

`sum_(j>=1)16^(-j)*d_j = 15*r(1)-225*alpha =47-225*pi/16`.

Therefore the exact convergent source-commutator formula is

`pi = (16/225)*(47-sum_(j>=1) d_j/16^j)`.     (W6)

This is a rearrangement of the KNOWN BBP identity, not an independent proof
of pi, its irrationality or its normality. Every d_j is rational, positive,
strictly decreasing and carries genuine source path-order information.

For `pi_M=(16/225)*(47-sum_(j<=M)d_j/16^j)`, positivity gives `pi_M>pi`.
Monotonic d and a geometric sum give the **certified rational one-sided bound**

`0 < pi_M-pi < (16/3375)*d_(M+1)/16^M`.        (W7)

No external pi digits are used in this proof. Independent Machin-arctangent
rational enclosures verify W7 on finite test horizons.

**One extra algebraic inverse power.** Exact Laurent expansion of the original
four-pole rational function yields

`r(n)=15/(64 n^2)+O(n^-3)`,
`d_n=15*(r(n)-r(n+1))=225/(32 n^3)+O(n^-4)`.

As `M->infty`, monotone geometric tail comparison/dominated convergence yields

`pi_M-pi ~ (1/30)*16^(-M)*M^-3`,
`pi - sum_(j<=M)16^(1-j)r(j) ~ (1/4)*16^(-M)*M^-2`.

Their ratio is asymptotic to `2/(15M)`. This is a source-derived elementary
summation-by-parts acceleration (one extra power), NOT a new digit-normality
argument or computational speedup assertion. A separate SymPy Laurent series
checks both leading coefficients, and two rational π oracles check finite bounds.

## W4. Strong no-go: fixed local Wilson twists cannot manufacture cancellation

Let `z_n` be ANY complex sequence `|z_n|<=1`, `g` any fixed real number,
and apply local curvature twists `z_n -> z_n*e(g*d_n)`. Since
`|e(x)-1|<=2*pi*|x|`, W2 gives for ALL N

`|(1/N)sum_(n<=N)z_n e(g*d_n) - (1/N)sum_(n<=N)z_n|`
` <= 2*pi*|g|*sum_(n<=N)d_n/N < 94*pi*|g|/N`. (W8)

More generally any `L`-Lipschitz function f on `[0,d_1]` satisfying
`f(0)=1` obeys the same `47 L/N` bound when multiplying the stream
by f(d_n). This is an all-horizon *negative theorem* for fixed local
Feynman/Wilson reweighting: it cannot change the asymptotic Weyl verdict
of the ORIGINAL BBP stream or a coherent counterseed. It is a stronger
source-specific form of a generic `ell^1` perturbation argument.

**Explicit hostile seed survives the same twist.** For the identical four-pole
forcing but nonzero seed `s*=1/5-pi/16`, inherited PR437 gives
`|sum_(n<=N)e(hU_n(s*))-N*e(h/5)|<11|h|/56` for fixed integer h.
Combining this with W8 shows that the twisted mean remains within
`[11|h|/56 +94*pi*|g|]/N` of the nonzero limit `e(h/5)`.
The source-only Wilson curvature therefore cannot distinguish original
zero seed from this coherent changed seed by any claimed universal
asymptotic saving.

For a nontrivial attempt one must break the summable-curvature ceiling via
source-justified moving-scale transport (e.g. factors depending on n/16^n)
**AND** keep the actual seed and Archimedean signed phases. No cancellation
of the resulting weighted sums is inferred here.

## Q1. Exact quantum seed information geometry of the phase-echo control state

For the same immutable source define the completed real parameter `q`,
original future tail `T_n=sum_(j>=1)16^-j r(n+j)`, and finite controlled echo

`|Psi_(N,h)(q)> = (1/sqrt N)sum_(n=1)^N e(h*(16^n q-T_n)) |n>`.

At q=alpha=pi/16 this is EXACTLY the original zero-seeded echo of PR445.
For any q,q' its overlap is

`<Psi(q)|Psi(q')>=(1/N)sum_(n=1)^N e(h*16^n*(q'-q))`. (Q1)

The original source phases cancel from this overlap. Parameterizing q as
one real coordinate, the pure-state quantum Fisher information is

`F_Q(N,h)=16*pi^2*h^2*Var_(1<=n<=N)(16^n)`,     (Q2)

where

`Var = [256*(256^N-1)/(255*N)] - [16*(16^N-1)/(15*N)]^2`.

Proof: `d_q Psi = i*2*pi*h*diag(16^n)*Psi`; the standard pure-state
Fisher formula is 4 times the centered generator variance. For N=1 this
variance is zero (a single phase has no observable relative phase).

This is a precise exponentially increasing *resolution sensitivity*, but
is UNIVERSAL for the chosen radix/horizon and INDEPENDENT of the original
four-pole phase labels. It cannot by itself establish pi normality or a
source-selected entropy law. For a two-parameter family of fixed-modulus
phases `Psi(lambda)=(1/sqrt N)sum e^(i phi_n(lambda))|n>`, the quantum
metric is `Cov(d_i phi,d_j phi)` and the Berry curvature vanishes wherever
all phases are smooth and single-valued; this special commuting-diagonal
model has no source-specific local quantum curvature. A global flat Berry
holonomy on a noncontractible parameter circle may still occur, but it is
seed-blind here.

The control phase Gram `K_(mn)=e(h*(U_m-U_n))` has rank one (one pure
phase vector) for ANY source; Gram purity is not the selected return
probability `|S_N(h)/N|^2`.

## Q2. Adversarial rational completed seeds are quantum-indistinguishable
## on their own finite source-prefix horizon

For each K>=1, define a RATIONAL number using only the original source

`q_K=sum_(j=1)^K 16^(-j)r(j)`,
`alpha-q_K = 16^(-K)*T_K`,
`0<T_K<1/[(8K+1)(8K+2)]`.                      (Q3)

The last bound follows from monotonic r(j),
`T_K<=r(K+1)*sum_(j>=1)16^-j =r(K+1)/15`, and the original
`r(K+1)<15/[(8K+1)(8K+2)]` source density bound.

Run the same original four-pole forcing with changed initial seed
`s_K=q_K-alpha` (an IRRATIONAL seed), so completed q_K is rational.
For this *fixed K* altered orbit, `U_n(s_K)=16^n q_K-T_n`. For its fixed
nonzero harmonic h_K=den(q_K), `e(h_K U_n(s_K))=e(-h_K T_n)->1`, so the
completed orbit is **provably nonnormal**. This does not assert a single
seed works for all K; q_K and h_K change with K.

For any fixed nonzero INTEGER h, the selected-vs-counterfeit K-branch
pure control states satisfy by `|e(x)-1|<=2pi|x|`:

`||Psi_(K,h)(alpha)-Psi_(K,h)(q_K)||_2^2`
` <= (2pi h)^2 T_K^2 *[256*(1-256^-K)/(255*K)]`
` < [121*h^2/(12495*K^5)]`.                   (Q4)

The second strict rational bound uses `2pi<44/7` and `(8K+1)(8K+2)>64K^2`.
This controls genuine pure-state **trace distance** `D_K` as well, since
`D_K=sqrt(1-|<Psi|Phi>|^2)<=||Psi-Phi||_2`.

For m independent copies of THIS EXACT K-branch control-state pair,
`D_K^(m)=sqrt(1-(1-D_K^2)^m)<=sqrt(m)*D_K`.
With equal priors, the Helstrom optimum correct-discrimination probability
is `(1+D_K^(m))/2`. Achieving success at least 3/4 therefore NECESSARILY
requires

`m > [12495/(484*h^2)]*K^5`.                 (Q5)

This is a rigorous **restricted state-discrimination** lower bound, not a
universal quantum algorithm complexity bound. Other access models (querying
source coefficients beyond K, choosing h=h_K, receiving labels for the
seed, or preparing other states) are NOT covered. The same-source
nonnormal counterseed is a hostile finite-observer control, not evidence
that pi itself is normal or nonnormal.

## H1. Stronger finite-source indistinguishability *inside positive measures*

Retain the AUTHENTIC original positive Hausdorff source measure

`dmu(u)=(1/8)u^(-7/8)(4-2u^(3/8)-u^(1/2)-u^(5/8))du`, `0<u<1`;
`r(n)=int_0^1u^(n-1)dmu(u)`, and `alpha=int dmu(u)/(16-u)=pi/16`.

For each finite M>=1, let `P_M(u)` be the MONIC degree-M polynomial
orthogonal to `1,u,...,u^(M-1)` for inner product from THIS measure.
It has exact rational coefficients, since all source moments r(j) are
rational and the finite Gram system has strictly positive determinant.
By the elementary sign-change proof for orthogonal polynomials with
positive interval support, P_M has M simple roots in (0,1), so `P_M(16)>0`.

Define

`J_M=int P_M(u)/(16-u) dmu(u)`.

The identity `(P_M(16)-P_M(u))/(16-u)` is a polynomial of degree M−1.
Orthogonality gives

`J_M = [1/P_M(16)]*int P_M(u)^2/(16-u)dmu(u) >0`. (H1)

Let `C_M=sum_(j=0)^M|[u^j]P_M(u)|`, so `|P_M(u)|<=C_M` on [0,1].
For `0<epsilon<1/C_M`, the altered measure

`dmu_epsilon=(1+epsilon P_M(u))*dmu(u)`

remains STRICTLY POSITIVE on (0,1). Its source
`r_epsilon(n)=int u^(n-1)dmu_epsilon` satisfies

`r_epsilon(n)=r(n)` for EVERY `1<=n<=M`!              (H2)

With the SAME LITERAL zero seed, its first M realized states, path-order
generators with both indices <=M, point characters, and finite echo control
states are **exactly identical** to the original source's.

But the completed boundary value is
`alpha_epsilon=alpha+epsilon J_M`, which runs over a positive real
interval. Choose any RATIONAL `q` in `(alpha,alpha+J_M/C_M)` and set
`epsilon=(q-alpha)/J_M`. Such rationals exist by density. Then the
completed ZERO-SEEDED altered source has q rational, `r_epsilon(n)->0`
and `T_n^epsilon->0`; at the FIXED harmonic `h=den(q)` its Weyl mean tends
to 1, hence is **nonnormal**.

This yields an explicit **for every finite M** positive-source countermodel
with perfect prefix identity, not merely an approximate seed shadow.
Crucially, it CHANGES the original four-pole forcing beyond M. It cannot
refute a theorem whose hypotheses genuinely authenticate the full original
rational four-pole identity and its initial zero boundary.

**Fully rational existence receipt:** The implementation independently
computes a rational Machin enclosure `[pi_lo,pi_hi]` and positive rational
bounds

`||P_M||_mu^2/[16 P_M(16)] <= J_M <= ||P_M||_mu^2/[15 P_M(16)]`.

Set `t0=1/(2C_M)`, `eta=t0*J_lower/4`. Refine the Machin interval until
`pi_hi/16-pi_lo/16<eta`. Then the SPECIFIC RATIONAL number
`q=pi_hi/16+eta` lies strictly between alpha and alpha+t0 J_M.
Its inferred epsilon has a rational enclosure inside `(0,t0)` and the
positive measure is rigorously certified. The preregistered exact probes
construct these certificates for M=1..6. No numerical approximation of pi
acts as a proof here.

## Verdict and next decisive probe

- **Disclosed / classical mathematical proofs with original-source specialization:**
  W1–W8; Q1–Q5; H1–H2. Finite exact Fractions and independent algorithms
  check samples, not universal claims. This is not a novel Feynman physical
  theory or an independent scholarly priority assertion.
- **Refuted on its declared domain:** fixed local curvature phases or
  source-independent quantum Fisher metrics force selected pi normality;
  finite positive time moments plus zero seed authenticate the ENTIRE source;
  finite K-branch quantum echoes can reliably discriminate the chosen
  nearzero counterfeit with o(K^5) copies at fixed h.
- **OPEN:** all-horizon source-selected `S_N(h)=o(N)` for every fixed
  nonzero integer h, and any source-attested nonflat mixed phase/curvature
  estimate implying it. The original four-pole and zero seed must remain
  bound; positivity, total flux 47 and generic quantum metrics alone fail.

### Classical provenance and authority

The exact unitary affine and phase echo are inherited PR444/#445 results,
not independently invented or re-proved here. The original source and
positive Hausdorff moment are inherited from PR440. Finite orthogonal
polynomial support and second-kind Stieltjes transform are classical; see
NIST DLMF Chapter 18 (https://dlmf.nist.gov/18.30). The optimal binary
state discrimination formula is the Helstrom–Holevo theorem (IBM Quantum
Learning, https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/general-measurements/discrimination-and-tomography).
The full theory requires a new arithmetic signed saving, not simply a
new way of representing the original signed Weyl observable.
