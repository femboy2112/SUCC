# Infinite realization of finite observations: Ind-Yoneda, analytic reconstruction, and the RH sign

**2026-10-10. RH REMAINS OPEN.** Continuation of the Gamma/actualization branch (frozen parent 971bb5fbea3c756c01d6d077c2b03a8ec5f76989). A user-corrected thesis is the input: **not merely a coherent totality of finite observations, but a coherent totality of an INFINITE REALIZATION of finite observations, taken as a limit.** No finite stage is required to contain the limiting object.

**Core files:** actualization/infinite_realization.py, tests/actualization/test_infinite_realization.py. Both are source-zero-free; mpmath is used in the tests as an independent numerical calibration, not as an axiom or RH oracle.

**Sources for standard external theorems:**
- The Stacks Project, Yoneda lemma, https://stacks.math.columbia.edu/tag/001L
- Stacks Project, presheaf limits/colimits are pointwise, https://stacks.math.columbia.edu/tag/00VB
- Ind-objects are filtered colimits of representables, https://ncatlab.org/nlab/show/ind-object
- NIST DLMF §25.2, zeta's Dirichlet series on Re(s)>1 and unique meromorphic continuation, https://dlmf.nist.gov/25.2
- Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*, https://arxiv.org/abs/math/0008177
- Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), https://doi.org/10.1112/jlms.12785

## 0. The object, stated without metaphor

A never-ending path is NOT a final finite arrival at infinity. We require:
(1) an actual directed system of finite stages, (2) declared transport maps,
(3) an observation functor into a specified target category, and (4) a
completed object in which the diagram's limit/colimit exists.

The order and target matter. Different functors can extract different completions
from the same integer stages. There is no topology-free passage from finite
divisibility or finite adic clocks to the real/Archimedean place.

**Our strongest mathematically valid reading**: a global object can be
determined by infinitely many compatible finite probes even when no finite
model represents that object. This is already a theorem for a concrete
arithmetic ind-object below. It does NOT assert that the resulting object
is Gamma, the zeros, or a positive Weil form.

## 1. Disclosed arithmetic theorem: a global ind-object with no finite representative

Let C be the thin category of positive integers under divisibility, with
Hom_C(j,m) a singleton iff j|m, empty otherwise. Define

\[
L_N=\operatorname{lcm}(1,\ldots,N),\qquad
L_N\longrightarrow L_{N+1}
\]

using the unique divisibility arrow, so the finite representatives form a
directed diagram. Under the **contravariant Yoneda embedding**,

\[
h_{L_N}(j)=\operatorname{Hom}_{C}(j,L_N),
\qquad
F_\infty=\operatorname*{colim}_N h_{L_N}.
\]

The presheaf colimit is computed pointwise. For each **fixed finite** j,
we have j|L_N as soon as N>=j. Consequently, F_infty(j) is a singleton for
every j: F_infty is the terminal presheaf on C.

**Nonrepresentability:** suppose F_infty=h_m for some finite integer m.
Take the valid finite query j=m+1. Then Hom_C(j,m)=empty while
F_infty(j) is a singleton. Contradiction.

Hence the ind-object F_infty is constructed entirely from a filtered
infinite realization of finite objects, yet is not any finite stage or any
object of C. In the enlarged supernatural-number divisibility category, its
representative is U=product over all p of p^infinity. No ordinary integer is U.

The test engine uses symbolic factorization, not an impossibly large lcm
materialization: stage(N) produces the exact valuations v_p(L_N);
activation_stage(j)=max_(p^k || j) p^k; first_missed_prime_power(N)
returns the earliest larger prime power. Finite hypothesis checking never
pretends to execute infinitely many queries.

**A distinction to preserve:** for FIXED ambient objects X,Y and an
exhaustion of the entire probe category by full subcategories C_N, one
may indeed recover

\[
\operatorname{Hom}_{C}(X,Y)\cong
\varprojlim_N \operatorname{Nat}
 (h_X|_{C_N},h_Y|_{C_N}).
\]

That inverse limit enforces compatibility of restricted natural
transformations. But when the **target object itself changes with N**
as L_N, the needed construction is the *filtered colimit of representables*,
not this fixed-object inverse limit. Mixing the two obscures the precise
mechanism identified by the user.

**Warning:** this C only reads divisibility. It cannot distinguish a true
Euler source from an otherwise identical coefficient sequence with a fake
event at 6. Consequently this ind-object is **RH-INERT** until the
observation category is enriched with source weights, Hecke phases, and
the completed analytic form.

## 2. π and e: separately certified effective Cauchy reconstruction

These are genuine, explicit examples where no finite truncation must equal
the ultimate real, yet a finite algorithm gives a certified rational interval
containing it with a width provably tending to zero.

**e** is defined by exp(1)=sum_(k>=0) 1/k!. Let S_N be the sum to N. Then

\[
S_N<e<S_N+\frac{N+2}{(N+1)(N+1)!}.
\]

Proof: after the (N+1)-st summand, the ratio of successive positive terms
is at most 1/(N+2), so compare to a geometric series. The interval shrinks
factorially. No floating-point judgment is needed to prove the inclusion.

**π** is obtained through the Machin identity

\[
\pi=16\arctan(1/5)-4\arctan(1/239).
\]

Its identity has a short exact check: tan(4 arctan(1/5))=120/119;
subtraction of arctan(1/239) yields tangent 1 in the first quadrant.
For 0<x<1, the alternating arctangent series gives rational upper and
lower bounds from the first omitted term. Combining intervals with the
correct signs gives exact rational enclosures for π that shrink
geometrically. The code's intervals are exact Fractions; its high-precision
independent π/e readings are only calibration.

**Important:** each computation is finite; the mathematical theorem that
the nested intervals have a unique common real belongs to the completion
of Q. The limit exists in a declared target (R), not as a last rational.
The code computes certified finite enclosures, not an infinite observer.

## 3. The same arithmetic field already determines ALL zeta zeros uniquely

This is a critical correction to an overly strong "RH is intrinsic, hence
the finite field cannot see it" claim.

On Re(s)>1,

\[
\zeta(s)=\sum_{n=1}^{\infty}n^{-s}.
\]

If sigma=Re(s)>1, the finite-prefix tail has the effective estimate

\[
\left|\zeta(s)-\sum_{n\le N}n^{-s}\right|
\le\sum_{n>N}n^{-\sigma}
\le\frac{N^{1-\sigma}}{\sigma-1}.
\]

For sigma>=1+delta this is at most N^-delta/delta, uniformly.
The module supplies *exact rational* enclosures for positive integer s>=2.

As a meromorphic function, the analytic continuation of this Euler-region
germ is **unique by the identity theorem**, given existence and a connected
continuation domain. Standard theory supplies that existence for zeta.
The completed xi is likewise determined by the known Gamma/pole factors;
its zeros, including their actual locations, are mathematically determined
by the infinite arithmetic data.

Thus the zeros are **not intrinsically absent from the information**.
What is missing is a source-derived argument about their *global
distribution* (all nontrivial zeros on Re(s)=1/2).

Finite computations and contour/argument-principle methods can investigate
bounded spectral regions; this is not a mathematical proof of a uniform
statement over all heights. Lagarias's arithmetic equivalent likewise makes
clear that the RH truth-value has a universal finite-index formulation; if
RH were false its violation could be witnessed at some finite index. The
nonexistence of an accessible global *positive certificate* is a current
research obstruction, not proven information-theoretic invisibility.

## 4. Stronger local-to-global actualization fact for Suzuki Psi

For the exact Gamma-plus-pole term A_infty(t) and genuine Euler-source
connected coefficients b(n)=log_*(a)(n), define

\[
\Psi_N(t)=A_\infty(t)-
\sum_{2\le n\le N}
\frac{b(n)\log n}{\sqrt n}(|t|-\log n)_+.
\]

Fix any real t. Once \(N\ge e^{|t|}\), all new ramps are identically zero
at that t; therefore

\[
\boxed{
\forall t\ \exists N_t\ \forall N\ge N_t:
\Psi_N(t)=\Psi(t).
}
\]

This is **eventual EXACT EQUALITY**, not just approximate convergence,
for the true full arithmetic source. Tests compare integer-labelled events
against later complete prefixes without using zeros. It is the cleanest
mathematical realization of "the wavefront's finite accumulated history
agrees with the global completed reading on every fixed finite past."

Still, the quantifiers in RH/Suzuki are different:

\[
\mathrm{RH}\iff \forall t\in\mathbb R:\ \Psi(t)\ge0.
\]

No single finite N_t covers all t. This is a genuine **quantifier gap**:
pointwise eventual reconstructability of the function does not produce a
uniform sign theorem. Conversely a finite mathematical proof of a uniform
sign theorem COULD exist; nothing here proves an impossibility of proof.

**Hostile delayed-source control:** for any chosen finite N, select a mixed
composite m>N and perturb a(m) from 1 to 1+C, leaving all earlier source
coefficients unchanged. Its connected log coefficient at m acquires C.
The earlier observations and pointwise responses are exactly identical up
to the arrival time. For t=log(m+1), the difference is

\[
\Delta\Psi(t)=-C\,\frac{\log m}{\sqrt m}
\log\!\left(\frac{m+1}{m}\right).
\]

Choosing C sufficiently large can make the **artificial,
zeta-Gamma-normalized diagnostic** negative. This proves bounded source
prefixes cannot discriminate all possible unrestricted future extensions.
It does NOT contradict the actual zeta Euler product; the mutated system
is deliberately a non-Euler source, not a completed genuine L-function.
Tests use multiple hostile horizons and exact formulas, with high-precision
numerical checks as diagnostics.

## 5. Decisive correction to the finite-stage positivity objection

Here is a genuinely sharp, **independent, elementary form-limit theorem**
that exactly captures why requiring each finite stage to be PSD was the
wrong kind of gate.

Let H=ell²(N), e_N its basis vectors, P_N the orthogonal rank-one
projection onto e_N, and

\[
A_N=I-2P_N,\quad Q_N(x)=\langle x,A_Nx\rangle
=\|x\|^2-2|x_N|^2.
\]

Every finite N has the explicit negative direction e_N:

\[
Q_N(e_N)=-1.
\]

But for any FIXED finitely supported vector x there is a bound
N_x>max supp(x) such that

\[
\forall N\ge N_x:\quad Q_N(x)=\|x\|^2.
\]

In fact P_N tends strongly to 0 on the whole H, so A_N tends strongly
to I and the **limit is positive**, although not a single A_N is PSD.
The convergence is NOT in operator norm: ||A_N-I||=2 for every N.

Formally these two statements coexist:

\[
\forall N\ \exists x_N:\ Q_N(x_N)<0,
\qquad
\forall x\ \exists N_x\ \forall N\ge N_x:\ Q_N(x)\ge0.
\]

This is the missing quantifier distinction in the earlier individual
impulse no-go. A local sign obstruction need not survive a correctly
constructed infinite realization.

**Adversarial control:** replace the escaping negative direction e_N by
the fixed e_1:

\[
R_N=I-2P_1.
\]

The same statement "every finite stage indefinite" remains true, but
now the negative direction never escapes and the limit stays indefinite.
Thus finite-stage indefiniteness by itself cannot distinguish positive
from nonpositive limits. To select the RH-bearing situation, one needs a
proven source-dependent transport/escape/renormalization law, not merely
the vocabulary of infinity or category theory.

**Scope:** a bounded H toy on the finite-support core. This does not
represent the unbounded Weil functional. Transfer would need closability,
common domains, Gamma counterterms, form-norm control, and an exact
source-to-Weil identity. These are NOT provided by the example.

## 6. Proof-gate inventory and next discriminating instrument

The mathematics now separates five phenomena:

1. **Presence:** arithmetic source events actually integrated (SUCC).
2. **Distinguishability:** chosen probe category detects a structural difference (restricted Yoneda).
3. **Realization:** filtered source diagram defines a legitimate global ind-object, possibly nonrepresentable at any finite stage.
4. **Analytic transport:** source information maps, with quantitative convergence, into the completed Gamma/Mellin/Weil form domain.
5. **Independent sign:** the completed form is globally positive by a non-circular arithmetic theorem.

(1)–(3) have executable bounded models; (4) is implemented only as the
scalar, eventually exact Suzuki wavefront and safe Euler-domain enclosures,
not as a full operator-valued form-domain transport; (5) remains UNVERIFIED.

**Next verdict-changing probe:** construct a *source-sensitive enriched
Yoneda/Ind bridge* carrying coefficient values, prime powers and phases,
not merely divisor existence, into a specified domain of the completed Weil
quadratic form. Prove naturality and coherence under finite-window embeddings;
construct the archimedean renormalized limit *before* assigning positivity;
check convergence on an exact dense test core and extend through a rigorous
form closure. Then compare the true Euler data against composite and
half-density mutations, and against a matched Hecke/Davenport–Heilbronn
pair with the correct, separately computed Gamma factors.

**Pass**: a new independently proved positivity or eventual-positivity
theorem for the actual source, combined with an exact form-domain Weil
identification. **Fail**: a generic positive Gram insensitive to source,
a nonrepresentable ind-object alone, a fake-arithmetic-insensitive
limit, an unproved swapping of limit and sign, or an assumption
equivalent to RH. **Ambiguous**: finite pointwise agreement without
a uniform functional/sign theorem.

## 7. Claim ledger

| Claim | Verdict | What supports it |
|---|---|---|
| F_infty is terminal, ind-representable, not finite-integer-representable | **DISCLOSED** (classical presheaf/Yoneda proof) | §1; exact finite controls |
| pi and e have effectively shrinking rational intervals | **DISCLOSED** (series and tail proofs) | §2; Fraction module |
| Euler-region zeta is effectively reconstructed and continuation is unique | **DISCLOSED** (classical, domain-limited) | §3; DLMF |
| Each fixed Suzuki time stabilizes exactly after enough prime events | **DISCLOSED** (finite ramp support) | §4; Gamma tests |
| A_N indefinite at all N but tends strongly to I>0 | **DISCLOSED** (rank-one proof) | §5; exact rational probes |
| Future arbitrary source can evade any chosen finite prefix | **DISCLOSED** (source-prefix construction) | §4; mutation tests |
| These facts solve RH or supply the missing Weil-positive pairing | **UNVERIFIED** | no fourth-gate object |
| "RH zeros are intrinsically hidden forever from finite data" | **NOT ESTABLISHED / REJECT STRONG FORM** | uniqueness of continuation and finite counterexample possibilities |

The independent mpmath checks and CI success, when present, are **OBSERVED**
software tests. They do not independently establish the external theorems
or the RH global sign. No input zeros or fitted ordinates enter the code.
