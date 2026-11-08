# Learning Yoneda, source-prime epochs and the remaining signed covariance

**π base-16 normality: OPEN. RH: OPEN.** This additive research dossier is
based on main `d32342d375f44ddf62221ad6aff2f534abdc0a03`. All changes live in
this directory. The original source, global claim ledger and main integration
files are untouched. Exact source heads and stack relationships are in
[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json).

## Strongest new mathematical result

[PE1–PE9](arithmetic/PRIME_EPOCH_THEOREM.md) prove an **unconditional all-epoch
local-prime character cancellation theorem** for the original rational BBP
orbit. Let p_A be the largest prime p≤4A with p≡1 mod8 and ord_p(16)^3>p.
For all sufficiently large A this is defined, p_A/(4A)→1, and

\[
\max_{1\le h<p_A}\left|\frac1A\sum_{n=A}^{2A-1}
 e\bigl(h[U_n(0)]_{p_A}\bigr)\right|
 \le p_A^{-\gamma}+\varepsilon_A\longrightarrow0,
\]

where γ>0 is a classical subgroup exponent, [·]_p is the canonical rational
p-principal part, and ε_A is an explicit interval-weight distance tending to
zero. The source-prime selector uses no real Fourier observations.

The key source fact is that p≡1 mod8 is born at (p+7)/8 and next appears at
(p+1)/2. Writing L=(p−1)/4, the entire interval [L+1,2L+1) consists of complete
clean prime cycles. An elementary product argument bounds the number of
small-order primes by O(x^(2/3)); fixed-modulus PNT/AP supplies p_A~4A;
Bourgain–Konyagin supplies cancellation on those cycles. These two classical
theorems are declared imports, with primary references in the proof.

This pays the local marginal and epoch coverage obligations in #529. It is
not a bound on e(hU_n) itself. The local marginal survives every fixed rational
seed eventually, so it does not distinguish the literal zero boundary alone.
Worldwide novelty is not asserted; the claimed advance is relative to the
actual pinned SUCC proofs inspected here.

## One proof spine, with the unpaid arrow explicit

The immutable source is
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
Unwrapped rationals, circle phases and integer carries are retained. The
established Green identity is U_n(s)+T_n=16^n(s+π/16).

For the same p_A define
\[
a_n=e(h[U_n(0)]_{p_A}),\qquad
b_n=e(h(U_n(0)-[U_n(0)]_{p_A})).
\]
The product a_n b_n is exactly the original real character. With averages on
[A,2A), set Cov_A(a,b)=E_A(ab)−E_Aa E_Ab, **without conjugation**. PE11 proves
\[
W_A(h;0)=\operatorname{Cov}_A(a,b)+o(1).
\]
Thus the next missing theorem is precisely Cov_A(a,b)→0 for every fixed
nonzero h. It remains an equivalent gate, not a newly weaker premise.

| Arrow and objects | Establishing result | Falsifier if hypotheses are weakened | Status and contribution |
|---|---|---|---|
| Literal source → exact history and rational principal parts | Shared `selected_orbit` forcing; `learning.exact_history`; PE1–PE2 | Pole mutation or hidden new seed denominator | Exact algebra, source authenticated mathematically |
| Histories → lawful transcript paths and retained target information | LY1–LY3 using main `BeliefGame`, `ObservationPathCategory`, `FiniteFunctor` | Same current projection with distinct earlier pins; C5 conditional-memory conflict | Finite realization and memory theory; no mixing bound |
| Source chronology → complete prime cycles covering asymptotically every epoch | PE1–PE8, elementary order count, PNT/AP | Unclean interval crosses next pole; sparse isolated cycles | New source-specific coverage theorem |
| Complete cycles → signed local marginal decay | PE9, imported BK subgroup theorem | Gauss-only bound at p=641 exceeds1; p divides h gives trivial character | Unconditional local cancellation; observation prime varies with A |
| Local marginal plus complement → original signed Weyl statistic | PE10–PE11, exact factorization | AR seeds preserve local phases while producing positive large covariance | Exact reduction, no estimate on covariance |
| Original zero-source covariance →0 | PE12-OPEN | Finite authentication can accept horizon-dependent coherent seeds | **OPEN; all remaining normality difficulty on this route** |
| Fixed-h dyadic Weyl decay → base-16 normality of π | Classical Weyl criterion, dyadic decomposition, original Green tail | Finite cutoffs, seed ensembles or changing h do not satisfy the quantifiers | Established conditional implication |

For the last arrow, dyadic epoch decay implies prefix Cesàro decay by splitting
a prefix into successively halved intervals: the finitely many small intervals
have vanishing total relative size, and every large interval has the stated
bound. The vanishing Green tail transfers characters to 16^nπ/16. Normality
then follows from the standard orbit form of Weyl's criterion. The required
quantifiers are ∀ fixed h≠0, ∀ε>0, ∃A0, ∀A≥A0. They have not been proved.

## Other proved results and instrument audit

- **Finite arithmetic authentication obstruction (AR1–AR4):** for any finite
  odd-prime menu, 2-adic precision, earlier carry transcript and chosen future
  epoch, an explicit positive rational wrong seed preserves those observations
  while making the future signed mean arbitrarily close to1. The construction
  uses only the original finite source recurrence. New denominator support
  and the nonzero initial state expose it to complete source authentication.
  Combining it with PE9 proves PE14: the selected local mean tends to zero
  while the complementary complex covariance tends to1. It is an
  epoch-dependent family, not a fixed rational nonnormality theorem.
- **Continuum sensor cost (SP3):** for all initial probability laws, exact
  complex Fourier sensors |h|≤H at times0,…,N have future two-tone minimax
  error Θ(sqrt(min(16^k/H,1))) at N+k, uniformly in finite N. Explicit positive
  aliases attain the lower scale. The upper estimator is an arbitrary L2
  response, not necessarily a realizable law. This is an instrument theorem;
  it is not a statement about uncertainty in the already specified singleton
  U0=0.
- **Adaptive finite-noise obstruction (C2):** every finite deterministic causal
  Lipschitz probe policy with positive error tolerances has a periodic completed
  wrong seed that reproduces its truthful zero-source transcript under allowed
  errors. A certified π interval gives an actual seven-probe example, period21.
- **Operator reconciliation:** #541–#543's distributional pin inverse,
  first-order two-tone inverse and syzygies survive the independent audit.
  The sharp real-law half-aperture ×16 constant is 341/√205, attained by the
  frequency32→2 cosine perturbation. It concerns the stated coherent L2
  operator norm, not total variation or magnitude-only inversion. Historical
  partition refinement contributes a nonnegative conditional variance and
  does not determine the sign of cross-cell interference.

The learning theory is complete at its stated domains: LY1 history-relative
realization; LY2 offline, transcript and streaming memory distinguished;
LY3 finite toolkit saturation; LY4 threshold policy4 versus15 probes;
LY5 open-path seed charge and transported Fourier naturality; LY6 compact
inverse limits with continuity and source-domain counterexamples. These are
classical/inherited statements and source-family specializations. A Boolean
late-address target needs4M working bits after M hex digits despite its final
one-bit answer. Exact finite source families are separated from the continuum.
No claim of physical nonlocality is made.

## Hostile controls and remaining hypotheses

The retained controls include s*=−π/16, periodic completed seeds, CB-3
nonstationarity, 2-adic Haar/real-nonnormal shadows, phase-blind homometric
aliases, independently rotated gauges, mutated pole coefficients, closed
seed-blind holonomies, finite sensor bandwidth and Haar-seed ensemble versus
selected zero. CB-3's infinite construction is inherited; only the stated
finite ingredient is rerun. Seed1/5 is never used as a known nonnormal seed.

The most promising unproved target is a **complement covariance estimate using
the exact original denominator support and literal zero boundary**. AR and
PE13 show why preserving arbitrarily extensive finite prime and carry data
cannot replace that condition. LS, H2*, selected golden/two-tone energy decay
and critical Fejér control all remain open.

Ranked by actual unpaid debt: (1) PE pays local coverage and cancellation;
(2) AR/PE13 rule out a concrete proposed transfer mechanism; (3) SP3 and C2
quantify instrument limits; (4) LY supplies coherent semantics and source
contracts. The signed-lag/Gamma and positive-energy routes generated no new
full-phase saving; their failed steps are retained, not advertised as advances.

The next single useful experiment is an interval-certified measurement of
Cov_A(a,b) for the deterministic p_A selector on fresh, preregistered dyadic
epochs, paired with AR controls having the identical p_A character. Report
the full complex covariance and complement conductor, not just local energy.
This can falsify a proposed quantitative rate; finite success still would not
prove an asymptotic bound. The decisive theorem would bound that covariance
uniformly using the support that the AR construction necessarily violates.

## Reproduction, proof authority and integration

Run from the repository root, with Python3.12 and repository requirements:

```sh
python research/2026-11-07/learning_yoneda/validate.py --output /tmp/learning-yoneda-replay --full
```

Without `--full` this runs the scoped tests, independent finite oracles and
Lean check. The full flag additionally runs all four mandated AGENTS.md gates.
Separate subprocesses prevent different `independent_oracle` modules from
contaminating one another. BLAS/OpenMP concurrency is capped at one.

See [VALIDATION.md](VALIDATION.md) for actual execution status and exact scope,
the raw logs in `validation/`, and the source/hash manifests. A fresh isolated
virtualenv was used because system mpmath1.2.1 is below the declared minimum;
global packages were not changed. Existing PRs541,542,543 were separately
replayed from their pinned git archives, 84 focused tests total.

Lean4.14 kernel-checks the finite decoder/fiber criterion and C5 memory result
in `crucible/ConditionalMemory.lean`. It does **not** certify PNT/AP, BK, the
analytic spectral theorem, the arithmetic asymptotic theorem or π normality.
Exact rational oracles certify their finite instances only. The three research
agents used distinct methods/implementations but share a model and source
provenance; this is not independent scholarly refereeing.

For integration, retain the pinned baseline, read-only sibling/stacked sources,
and this namespace. Any newer main head is recorded separately; no silent
rebase or shared catalog modification is part of this delivery. Draft publication
is for review by the maintainer performing main integration.
