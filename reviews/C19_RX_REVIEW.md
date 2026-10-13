# C19 independent crucible review

**Verdict: SURVIVES / PROVED LOCAL for the stated finite-initial-dimensional,
fixed-word theorem.** The countable-mixture repair also survives with its
membership hypothesis. No repair to the principal finite-dimensional statement
is required. Fresh terminal measurements, compact pure classes in infinite
dimension, source-dependent branches, and positive infinite-event probability
are distinct claims; the stronger claims fail with the receipts below.

## 1. Review question and provenance

Review date: 2026-10-13. Reviewed source: only
`research/2026-10-13/SWARM_ATLAS/C19.md` at
`e6c792b26f2497ba8cb7a266cc518ec79d59fd56` in
`/home/leah/succ_lab/swm-c19`. Its SHA-256 is
`3863e853e952a785188619dbd3c8b0203d15fc3ffb8a3619d195208605d01f76`.
The review starts from clean parent
`e0ae020047b9555cf9075e01463a56ccc3e2890e` on
`research/swm-rx-c19-2026-10-13`, in its own worktree.

I read the permitted claim dossier, which contains the author's written proof;
this is a fresh adversarial review, **not a blind reading of the statement
alone**. I reconstructed the argument and wrote the exact probe independently.
The author's probe and receipt were neither read nor imported. No other
first-generation dossier, native module, shared ledger, or imported original
was inspected or changed. AGENTS.md, METHOD.md, and PROTOCOL.md supplied the
working rules. The native replay and archival provenance assertions in C19 are
therefore outside this review's independently checked scope.

## 2. Existing mathematical context

Positive operators, bounded maps on trace-class operators, instruments, and
finite-dimensional kernel chains are classical mathematical objects. The local
proof below does not establish academic novelty.

Primary framework check: Ozawa, [*Quantum Measurement, Information, and
Completely Positive Maps*](https://arxiv.org/pdf/quant-ph/0107090), sections 4
and 8, supplies the trace/dual instrument description and the realization theorem
for CP instruments. His [*Operations, Disturbance, and Simultaneous
Measurability*](https://arxiv.org/pdf/quant-ph/0005054), section I, distinguishes
single-measurement probabilities from successive-measurement statistics that
also depend on disturbance. These references were opened during this review;
they support the standard measurement framework, not the new support proof or
any implementation/hardware claim.

## 3. Faithful objects, hypotheses, and quantifiers

Let `H0` have finite dimension `d >= 1`, and let `C` be one fixed, nonempty,
arbitrary set of density operators on `H0`. Neither convexity, compactness,
closedness, nor computability of `C` is assumed.

There is **one** infinite action/outcome word. On that word, every candidate
initial source encounters the same bounded linear positive trace-nonincreasing
maps `Phi_n : T(H_(n-1)) -> T(H_n)`; CP is additionally assumed for the quantum
instrument interpretation. Every retained degree of freedom that is needed to
determine later branch laws must be in the mapped state, or have a fixed
source-independent preparation that induces a well-defined map from `H0`.
Output dimensions may vary or be infinite.

Write `T_n = Phi_n ... Phi_1`, `E_n = T_n^*(I)`,
`p_n(rho) = tr(T_n(rho)) = tr(rho E_n)`, and
`C_n = {rho in C : p_n(rho) > 0}`. At index zero, `T_0 = id` and `E_0 = I`.

The claim is exactly

\[
  (\forall n<\infty\;\exists\rho_n\in C:\ p_n(\rho_n)>0)
  \Longrightarrow
  (\exists\rho\in C\;\forall n<\infty:\ p_n(\rho)>0).
\]

This asks for one original source compatible with all **finite** prefixes. It
does not assert that this source is uniquely identified, that an infinite
record was actualized, or that the infinite word has positive probability.

## 4. Independent proof and assumption audit

For a positive trace-class operator `X`, `tr(X) = 0` implies `X = 0`.
Consequently, for every vector `v` in the initial space,

\[
 \langle v,E_n v\rangle=0
 \iff T_n(|v\rangle\langle v|)=0
 \Longrightarrow T_{n+1}(|v\rangle\langle v|)=0.
\]

The equivalence uses positivity of `T_n`; the implication uses linearity of the
next map. Since `E_n >= 0`, its zero quadratic form is exactly its kernel.
Therefore `K_n = ker(E_n)` is an increasing sequence of subspaces of the **same
initial finite-dimensional space**. Every proper inclusion increases dimension,
so only finitely many proper inclusions occur. Their indices have a last member.
There is some finite `N` after which `K_n = K_N`.

Independently of any factorization of `rho`, its finite spectral decomposition
gives

\[
 \rho=\sum_j\lambda_j|u_j\rangle\langle u_j|,\quad\lambda_j>0,
 \qquad
 p_n(\rho)=0\iff u_j\in K_n\ \hbox{for every }j.
\]

Choose the premise's witness at `N` (or at `max(N,1)` if prefixes were indexed
from one). Its support is not contained in `K_N`. For earlier indices the
kernels are smaller; for later indices they are equal. The **same member of
the original C** therefore has positive likelihood at every finite index.
This is a proof for arbitrary `C`, not a numerical search or a compactness
argument.

For the stated TNI maps, positivity of the dual yields separately

\[
 0\le E_{n+1}=T_n^*(\Phi_{n+1}^*(I))\le T_n^*(I)=E_n\le I.
\]

Under the premise, the kernels never fill `H0`, so at most `d-1` proper
inclusions occur. **Their count does not bound the index of their last
occurrence.** A constant-rank plateau is not a finality certificate.

| Hypothesis or mutation | Audit result |
|---|---|
| CP weakened to positivity | The support proof still holds. Transpose is positive and trace preserving; its extension to an entangled pair fails positivity, so this weakening loses the standard instrument interpretation. |
| TNI removed, positivity retained | Kernel nesting and the existential support conclusion still hold by the proof above. Decreasing effects and probability bounds can fail: `K = 3I` gives `E_1 = 9I`. TNI is load-bearing for the stated monotonic/probability package, not the existential core alone. |
| Positivity removed | The zero-trace-output step and support lemma fail; the exact mutation below refutes the existential conclusion. Such a mutation is not a quantum instrument. |
| Output dimension changed | Harmless: all effects and kernels are pulled back to the same finite `H0`. The exact control uses `2 -> 3 -> 1 -> 4`. |
| Each source has finite rank, but no uniform finite initial support | Insufficient. The infinite-dimensional counterexample below consists entirely of pure sources. |
| One branch word replaced by fresh terminal measurements | Fails. Prefix effects need not be nested; section 5 gives a finite-qubit counterexample. |
| Branch selected using the unknown original candidate | Fails as a common linear-map model, even if every candidate's selected map is individually CP. |
| Original class changed with the horizon | Different quantifiers. An identity branch with alternating disjoint singleton classes has no member in all classes. This does not refute the fixed-C theorem. |
| Retained memory omitted | The reduced-state likelihood may cease to be a function at all. Unknown source-correlated memory belongs in the original state domain. |
| Normalized poststate used as a prefix weight | Invalid. Its trace is one whenever defined; the raw branch weight must be retained. Zero-probability branches have no conditional poststate. |

The nonpositive mutation is the fixed bounded linear map

\[
 F(X)=\operatorname{diag}(X_{11},X_{00}-X_{11}).
\]

For positive `X`, `tr(F(X)) = X_00` lies between zero and `tr(X)`, but `F` is
not positive. For `C = {P0,P1}`, successive trace rows start
`(1,0), (0,1), (1,-1), (-1,2), (2,-3), ...`. For every index at least one
candidate has a positive trace, but `P1` fails at the first and `P0` at the
second. For `n >= 2` the row is
`((-1)^(n-1) F_(n-2), (-1)^n F_(n-1))`, with the usual Fibonacci integers;
this proves the premise for all indices. Negative later traces make the
physical interpretation explicitly invalid. The probe preserves exact finite
rows; the all-index assertion is this analytic recurrence.

## 5. Decisive fixed-word versus fresh-terminal control

Take `H0 = C^2`, `C = {P0,P1}`, and, in each independently prepared experiment,
apply identity actions followed by a **fresh** terminal projector. Alternate
terminal effects `P0,P1,P0,P1,...`. Each horizon has a positive-likelihood
source. Neither candidate has positive likelihood at every horizon.

These are different action/outcome words. They are not finite prefixes of one
fixed word: the earlier terminal measurement is absent from the longer
experiment. The effects are incomparable and their kernels alternate.

If the projectors are instead composed as a single physical word, its second
branch product is `P1 P0 = 0`. The second prefix has likelihood zero for **all**
original sources, so C19's premise fails. The exact probe checks both sides:

```
fresh terminal rows:       (1,0), (0,1), (1,0), (0,1)
one fixed word, prefix 2:  (0,0)
```

**REFUTED:** using independently chosen terminal measurements as if their
effects were the prefixes required by C19. **SURVIVES:** C19 with its actual
fixed-word hypothesis.

Late drop receipt: use identity branches for 37 steps on a qubit, then the
projector onto `(3/5,4/5)`, then identities. The effect ranks are two through
index 37 and one from index 38. There is one proper inclusion, arbitrarily
postponable. This refutes a dimension-only stabilization deadline and the
claim that a long plateau rules out a future drop.

## 6. Infinite-dimensional countermodel and repairs

Let `H = l2(N_0)` and `P_n` project onto the closed span of `e_k` for `k >= n`.
The fixed branches `X -> P_n X P_n` are CP and TNI, and can be completed by the
complementary projection. Their products have effect `E_n = P_n`.

For an independently parameterized compact pure class, set `m_k = 2^k`,

\[
 a_k=\frac{m_k^2-1}{m_k^2+1},\qquad
 b_k=\frac{2m_k}{m_k^2+1},\qquad
 \psi_k=a_ke_0+b_ke_k,\quad k\ge1.
\]

Let `rho_k = |psi_k><psi_k|`, `rho_0 = |e_0><e_0|`, and
`C = {rho_0} union {rho_k : k >= 1}`. Since `a_k^2+b_k^2=1`, these are pure
density operators. On the two-dimensional span of `e0,ek`, the difference
`rho_k-rho_0` has trace zero and determinant `-b_k^2`; its eigenvalues are
`+b_k,-b_k`. Thus `||rho_k-rho_0||_1 = 2b_k -> 0`, proving trace-norm
compactness of the convergent sequence together with its limit.

For `n >= 1`,

\[
 p_n(\rho_k)=\begin{cases}b_k^2&k\ge n,\\0&k<n,\end{cases}
 \qquad p_n(\rho_0)=0.
\]

Prefix `n` has witness `rho_n`, but each `rho_k` fails at `k+1`, and `rho0`
fails immediately. **REFUTED:** extension to arbitrary initial dimension,
even with a trace-norm compact pure class. Nonempty nested **open** support
sets do not have the closed-set finite-intersection guarantee supplied by
compactness.

**SURVIVES / PROVED LOCAL — countable-mixture repair.** Suppose the original
class `C` contains countable convex mixtures of its members. Choose one
witness `rho_n` at each prefix and put `rho = sum_(n>=1) 2^-n rho_n`.
The series converges in trace norm to a positive trace-one operator. For each
fixed `k`, boundedness of `E_k` makes its trace functional continuous, so

\[
 p_k(\rho)=\sum_{n\ge1}2^{-n}p_k(\rho_n)
 \ge 2^{-k}p_k(\rho_k)>0.
\]

The membership hypothesis makes this **one source in the original class**.
This proof does not even require nested effects, only countably many positive
bounded likelihood functionals. Trace-norm closed convex classes satisfy the
membership hypothesis: the finite mixtures obtained by putting the unused
tail weight on `rho_1` lie in `C`, and converge in trace norm to `rho`.

**REFUTED — convexity alone.** The finite convex hull of the basis pure states
`|e_k><e_k|`, `k >= 1`, is convex, supplies a witness at each prefix, and every
member is killed beyond its finite largest occupied index. Its trace-norm
closure contains the diagonal countable mixture with weights `2^-k`, whose
tail probabilities are `2^(1-n) > 0`. Passing to that closure repairs the
claim **by enlarging C**; it does not prove the statement for the original
pure class or original finite convex hull.

Another valid repair restricts every member of `C` to one common
finite-dimensional subspace of the initial Hilbert space and compresses
`E_n` to it. The finite-dimensional proof applies to the compressed effects.
"Finite common support" must mean this uniform bound, not finite rank of each
candidate separately. Eventual kernel stabilization itself also suffices in
any dimension by the zero-likelihood support lemma.

## 7. Original source, records, memory, and actualization

A source-dependent mutation can use full-rank qubit candidates
`rho_k = diag(1/(k+2),1-1/(k+2))`, `k >= 1`. For candidate `k`, choose identity
branches until step `k`, then the zero branch. Each selected branch is CP and
TNI, but every candidate eventually dies and each finite horizon has a later
candidate. This cannot be a common branch law: any nonzero positive effect
has strictly positive trace against **every** full-rank qubit state. Killing
one such state while preserving another is impossible for a common effect.
The external candidate label is doing the selection.

Similarly, retain a countable memory label `k` while every reduced qubit is
`P0`, and project that memory onto its tail at step `n`. Labels zero and one
give first-prefix likelihoods zero and one for the **same reduced state**.
There is no map from the reduced source alone that produces both laws. On the
proper joint original domain, the initial dimension is infinite and the tail
counterexample applies. Finite memory restores a finite joint dimension.
An initially fixed, source-independent memory state, including an
infinite-dimensional one, can instead induce a well-defined map from finite
`H0`; merely adding output memory does not invalidate C19.

The CP reset `R(X) = tr(X) P0` takes both `P0` and `P1` to the same poststate,
with probability one. Their original Z labels still differ. Thus positive
support, or knowing the later poststate, does not identify the original
source or its target. For a declared target `g:C->Y`, a deterministic
zero-error report from a finite history `h` can exist exactly when `g` is
constant on `C_h`: two positive-likelihood sources with different targets
force any one report to be wrong under one of them; the common value supplies
the set-theoretic converse. No computability or physical realizability follows.

For the completed two-outcome instrument whose two operations are each
`X -> X/2`, the fixed all-first-outcome word has `p_n(rho)=2^-n` for every
density operator. All finite prefixes have the **same** compatible source.
Under the consistent Bernoulli product law, continuity from above gives
probability zero for the infinite event. `E_n -> 0` although every finite
kernel is `{0}`: the kernel of the limiting effect need not equal the
stabilized finite kernels. No positive lower bound, infinite record, elapsed
infinite computation, or actual occurrence follows from C19.

Normalizing a positive branch in this example produces the unchanged state
with trace one. Its trace cannot replace `2^-n`. For the impossible branch
`P0 P1 P0 = 0`, the conditional normalization denominator is zero; an arbitrary
replacement state would manufacture unsupported continuation.

The framework is declared mathematical quantum measurement theory. The proof
does not validate real apparatuses, actual human reasoning, unknown-source
preparations, or a connection to RH/Weil positivity. Existence of a witness
for arbitrarily declared `C` is compatibility within that model, not source
correctness or empirical actualization.

## 8. Exact probe receipt

Independent command, from the review worktree:

```
python reviews/C19_RX_probe.py
```

Executed once, with exit code **0**, on Python **3.12.3**. The probe uses only
standard-library rational arithmetic and small real matrices. It checks 13
witness families, including the two terminal-word configurations, the late
drop, changing output dimensions, the CP/positivity/TNI separations,
normalization, and exact compact-tail coordinates. The subprocess calls read
the allowed source dossier and the local Git parent. No author's executable
or receipt is a dependency.

Probe SHA-256:
`13e6609faad72a2ab3991fd1a184fd47a41aedd2e8cfe7f8ccb74c43c1c075ab`.
The machine-readable output is `C19_RX_RECEIPT.json` beside this review,
SHA-256 `aaedfee019557f6ac973c07d7d173cc577e5d7b2b85fe03e4695a6de157c24fa`.
The infinite-family limits, kernel theorem, and mixture theorem are proved
above; the finite panels in the receipt are **not** substitutes for those
proofs. No full suite, compiler, hardware run, or native replay was run. The
repository-wide required validation remains principal work.

## 9. Labeled verdict and claim limits

| Reviewed subclaim | Verdict and status | Receipt and boundary |
|---|---|---|
| Fixed-word, finite initial dimension, arbitrary original C | SURVIVES / PROVED LOCAL | Independent kernel proof in section 4; common positive maps and one fixed C. |
| Decreasing prefix effects under positive TNI maps | SURVIVES / PROVED LOCAL | Dual order calculation; fails without TNI. |
| Countable-mixture closure in arbitrary dimension | SURVIVES / PROVED LOCAL | Trace-norm convergence and positive summand lower bound; mixture must belong to original C. |
| Convexity alone in infinite dimension | REFUTED | Finite convex hull of basis states under tail projections. |
| Compact pure class replaces finite initial dimension | REFUTED | Rational compact family in section 6. |
| Fresh terminal experiments are prefixes of one word | REFUTED | `(1,0)/(0,1)` fresh likelihoods versus zero second composed prefix. |
| Dimension bounds stabilization time or a plateau proves final rank | REFUTED | Arbitrarily delayed first rank drop. |
| Finite positive support implies positive infinite-event probability | REFUTED | Completed halving instrument and probability-zero all-first-outcome event. |
| Later poststate identifies arbitrary original target | REFUTED | Reset with distinct original Z targets. |
| Exact finite probe outputs | TESTED MODEL | Exit-zero rational probe and retained receipt; no universal status from finite search. |
| Native smoke, archival source correctness, or apparatus implementation | Not independently reviewed | Only the permitted C19 dossier and framework references were consulted. |

The support theorem needs no change. Optional sharpening: its existential
core requires positivity and a common linear branch chain, whereas TNI is
needed for decreasing effects and genuine probability bounds. That sharpening
does not license non-CP maps as ordinary apparatuses.

## 10. Next falsification opportunity and epistemic boundary

Mechanize the trace-zero/support lemma and the finite kernel-chain argument;
then audit a real retained-memory history by explicitly specifying the joint
state, branch operations, and original source class. In particular, verify that
the records being compared are actual prefixes and that an initially fixed
memory preparation induces a common map. No finite rank plateau can certify
the last future drop, so an implementation must not infer stabilization from
an observation window alone.

κ: exact executable mathematical-model contact, no apparatus contact. φ: the
displayed proof plus hostile exact witnesses. σ: one author dossier and two
primary framework papers; citations do not independently prove the local
theorem, and source-class correctness is untested. ρ: fresh reviewer distinct
from the derivation role, but the written source proof was available. No phase,
truth probability, physical quantum cognition, or quantum speedup is assigned.
Final mathematical acceptance and integration remain with the principal.
