# Operation WTF: Global calibration, arithmetic resonance, and the false-coherence firewall

**Date:** 2026-10-26. **Status:** classical exact finite theorems, a BBP-source-specific negative corollary, executable rational certificates, and explicit unresolved Weyl estimates. **π base-16 normality remains OPEN; RH remains OPEN.** Research parent: draft [PR #314](https://github.com/femboy2112/SUCC/pull/314) at `935c2db4c36ff56d90acd82eae30bcce15b6a053`, stacked on #313/#312/#310/#309/#306. The original BBP forcing, zero seed, frozen source data, and historical proofs are untouched.

## 0. Steelman: the author's *global* reference as referee, not applause

The author identifies arithmetic meaning by recognizing the **same variable** appearing in distinct mathematical forms. Finite coincidences may be forced by common source, may be genuinely informative, or may be created by an evaluator who selects a convincing frame after observing the values. If every coherence group rewards its own internal agreement, a model can repeatedly count the same fact as independent support: *frame coherence can become arbitrarily overweighted*. This is not merely a psychological metaphor; it is a mathematical model-selection and shared-source problem.

The strongest faithful reconstruction is to keep a reference probability law, the original arithmetic source and its constraints, the current working conditional law, the ordered selection/memory checkpoints, the full complex character spectrum, and an independent authority/status register. A proposed new alignment must (a) preserve the actual shared-variable dependence, (b) separate evidence from deterministic identities, (c) pay for adaptive frame selection and reuse of the same observation, (d) prove any alleged new algebraic constraint is not already implied, and (e) transport to a genuinely new signed estimate for the **selected original BBP orbit** before claiming progress toward π normality.

**This paper introduces no new statistical randomness into the deterministic π orbit.** Global calibration is a theorem only relative to a separately declared stochastic reference; it is not a new law about the selected orbit.

## 1. Exact two-form interference: full and primitive characters

Let `q >= 1`, and let `F,G:Z/qZ -> Z/qZ` be arbitrary explicit maps evaluated on the **same** residue `x`. Put `d(x)=F(x)-G(x)`.

The complete Fourier compatibility projector is

$$\boxed{\Pi_q(d)=\frac1q\sum_{h=0}^{q-1}\exp(2\pi ihd/q)=\mathbf1_{q\mid d}.}$$

The primitive projector is the **normalized Ramanujan sum**

$$\boxed{\mathcal R_q(d)=\frac{c_q(d)}{\varphi(q)},\qquad c_q(d)=\sum_{a\mid\gcd(q,d)}a\mu(q/a).}$$

The first is an exact agreement detector. The second is an exact signed *primitive-phase* detector and is not a substitute for the first. In particular, for `q=2^k`, `k>=2`,

$$\mathcal R_{2^k}(d)=\begin{cases}1&d\equiv0\pmod{2^k},\\-1&d\equiv2^{k-1}\pmod{2^k},\\0&\text{otherwise.}\end{cases}$$

These are classical character-orthogonality and Möbius-inversion identities. Sources: Hardy–Wright, *Introduction to the Theory of Numbers*, §16.6; [MathWorld Ramanujan's Sum](https://mathworld.wolfram.com/RamanujansSum.html); [Goel–Murty, Journal of Number Theory 271 (2025)](https://mast.queensu.ca/~murty/HigherConvolutions.pdf). No novel academic priority is claimed for them.

### A rigorous 'WTF' coincidence with a primitive-phase false negative

Set `F(x)=2x`, `G(x)=x²`, and let `X` be uniform modulo `q=2^k`, with `k>=4`. Direct arithmetic gives the complete set of matching residues

$$\boxed{\{x:x(x-2)\equiv0\pmod{2^k}\}=\{0,2,2^{k-1},2^{k-1}+2\}.}$$

Exactly four other residues have **antipodal** disagreement:

$$\boxed{\{x:x(x-2)\equiv2^{k-1}\pmod{2^k}\}
=\{2^{k-2},2^{k-2}+2,3\cdot2^{k-2},3\cdot2^{k-2}+2\}.}$$

**Proof.** Both congruences require `x` even. Write `x=2y`, so `x(x-2)=4y(y-1)`. For the zero congruence, the consecutive factors are coprime, so the even factor must be divisible by `2^{k-2}`. Thus `y≡0` or `1` modulo `2^{k-2}`; each has two representatives modulo `2^{k-1}`. For the antipodal congruence, the even factor has valuation *exactly* `k-3`, which forces `y≡2^{k-3}` or `1+2^{k-3}` modulo `2^{k-2}`, again with two representatives. The displayed sets follow. `□`

Therefore

$$\boxed{\Pr(F(X)=G(X))=\frac4q,\quad
\mathbb E\mathcal R_q(F(X)-G(X))=\frac{4-4}{q}=0.}$$

By contrast, when `X,Y` are **independent uniform** residues, `2X` is uniform on even residues and `Y²` is even with probability `1/2`; consequently `Pr(2X=Y²)=1/q`. The often-repeated *independent-copy ratio* is exactly `4` for all `k>=4`.

**Critical calibration:** That `4` is a descriptive comparison of two *different experiments*, **not** a source-calibrated e-value or a p-value for a comparison in which both forms use the same `X`. The actual shared-variable null predicts `4/q` for this event! No evidence for π equidistribution follows. Meanwhile the primitive Fourier response vanishes because agreement and antipodal opposition cancel. The complete character family cannot be truncated to primitive characters when the target is equality.

### Coherent lifts versus finite coincidences

For every `k>=4`, two of the four zero roots, `2^{k-1}` and `2^{k-1}+2`, have **no** lift to a zero root modulo `2^{k+1}`. The only roots that lift at each step as the same fixed ordinary residue are `0` and `2`; and since `Z_2` is an integral domain, the only full 2-adic solutions of `x(x-2)=0` are indeed `0` and `2`. Finite modular abundance is not an unlimited supply of coherent infinite paths.

## 2. Global reference rules: exact counterexamples to self-convincing frames

Fix a **declared before observation** null `P0(X=x)=1/q`. For every preset frame `a`, the event detector

$$E_a(X)=q\mathbf1_{X=a}$$

has `E0[E_a]=1`, so it qualifies as a finite nonnegative e-value under that specific null.

**Postselection destroys this guarantee.** If the frame is instead chosen *after seeing the same X* as `a=X`, the apparent score is `E_X(X)=q` for every outcome and `E0[E_X(X)]=q`, not `1`. Precommitting to uniform frame weights repairs this:

$$\boxed{E_{\mathrm{global}}(X)=\sum_{a=0}^{q-1}\frac1qE_a(X)=1.}$$

**Duplicating one observation** is equally dangerous. For a preset frame, the product `E_a(X)^m` reuses the same fact `m` times, and

$$\boxed{\mathbb E_0[E_a(X)^m]=q^{m-1}.}$$

For `m>=2`, this is **not** a unit-expectation e-value. The multiplication theorem for independent experiments or conditionally normalized test factors does not apply to reused copies of the same variable.

**Tautological-frame control:** `F(X)=G(X)=X` gives an independent-copy agreement ratio `q`, arbitrarily large as `q` grows, even though `F=G` is an identity and generates **no second mathematical constraint**. Thus a large ratio can be an artifact of shared-variable dependence or an exact symbolic rewrite. The global referee must ask whether the second form adds a genuinely independent source constraint, not whether its numerical coincidence score is impressive.

### Exact linear novelty firewall (Seinfeld SS-01/02)

For linear constraints on a common state vector, append the proposed new coefficient row to the existing source-equation matrix and compute the **rational rank increment**. The native `seinfeld_succ.rational_rank` is reused. On `U0,U1,U2,U3`, the three one-step recurrence rows have rank three. The three-step macro recurrence `U3-16³U0-...=0` has rank gain `0`, as it is their weighted sum; the authentic zero-seed anchor `U0=0` has rank gain `1`.

Rank gain `0` **proves linear redundancy**. Rank gain `1` proves only a new *linear* equation, **not** statistical independence, an arithmetic nonlinearity theorem, or a normality estimate. Higher polynomial, prime, and carry constraints require their own dependency tests.

## 3. Honest pathwise calibration: predictable e-martingales, not post-hoc frames

Let `(F_t)` be a declared filtration of possible stochastic paths under reference `P0`. For each step let `I_t∈{0,1}` be a compatibility event and let

$$p_t=P_0(I_t=1\mid\mathcal F_{t-1})$$

be a **source-aware conditional probability fixed before observing** `I_t`. For a predictable choice `0<=λ_t<=1/p_t` (when `p_t>0`) define

$$\boxed{L_0=1,\quad L_t=L_{t-1}(1+\lambda_t(I_t-p_t)).}$$

Both possible factors are nonnegative and `E0[L_t|F_(t-1)]=L_(t-1)`. Therefore `(L_t)` is a nonnegative test martingale, even when the conditional probabilities and stakes are history-dependent. At every bounded stopping time the expected evidence is at most one; Ville's inequality gives

$$\boxed{P_0\{\sup_{t\ge0}L_t\ge1/\alpha\}\le\alpha.}$$

The code enumerates an entire finite dependent Bernoulli reference tree using rational arithmetic, checks `E0[L_t]=1` at every checkpoint, and checks its threshold-crossing probability. This is a **global protection against optional stopping and post-hoc frame choice** under the declared null. It is not a probabilistic theorem about the unique deterministic π orbit, and it does not give a selected Fourier estimate.

Related classical references: [Ville inequality and e-processes](https://doi.org/10.1093/jrsssb/qkag066), and nonnegative supermartingale theory.

## 4. Authentic BBP false-positive theorem: algebraic coherence saturates

Now use the complete original four-pole forcing, with `U0=0`:

$$r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_{n+1}=16U_n+r(n+1).$$

For each `n>=1`, let `x_n={U_n}`, let `j_n=floor(16x_n)`, and let

$$c_{n+1}=\lfloor U_{n+1}\rfloor-16\lfloor U_n\rfloor$$

be the **literal** integer carry (it can be 16, and only its Fourier evaluation is reduced mod 16). Put `t_n={16x_n}`. Since the exact original forcing satisfies `0<r(n+1)<1` for `n>=1`,

$$\boxed{c_{n+1}=j_n+s_{n+1},\qquad s_{n+1}=\lfloor t_n+r(n+1)\rfloor\in\{0,1\}.}$$

This is an exact source identity. Consequently, the *two-form compatibility* detector and its primitive Ramanujan version agree, pointwise:

$$\boxed{\Pi_{16}(c_{n+1}-j_n)=\mathcal R_{16}(c_{n+1}-j_n)=1-s_{n+1}.}$$

The authentic carry-spill theorem of [PR #313](https://github.com/femboy2112/SUCC/pull/313) establishes an all-horizon upper bound on the exceptional count `K_N=Σ_{n<=N}s_(n+1)` with `K_N=O(N/log N)`; importantly, the proof holds **for every initial state under the same forcing**. Thus

$$\boxed{\frac1N\sum_{n=1}^N\Pi_{16}(c_{n+1}-j_n)
=\frac1N\sum_{n=1}^N\mathcal R_{16}(c_{n+1}-j_n)
=1-\frac{K_N}{N}\longrightarrow1.}$$

**New program-specific negative corollary:** A primitive Ramanujan score that approaches **perfect coherence**, even while retaining the source forcing, cannot certify the zero-initial π orbit's equidistribution. The same limit holds with `V_n=U_n+16^n/3`, a changed-seed orbit obeying the **exact same forcing** and therefore the same spill theorem. The positive compatibility score is **implied by the recurrence** and is incapable by itself of distinguishing the authentic zero boundary.

Exact finite receipts (original and changed rational seed) at `N=1,2,16,64,127` happen to report score one. They are **finite observations only**; the all-time conclusion used here is `1-K_N/N→1`, not an unsupported assertion that no spills ever occur.

### Stronger exact no-go: *perfect* coherence on a provably nonnormal same-forcing orbit

The source's positive Green tail obeys

$$T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
r(n+1)=16T_n-T_{n+1},\qquad
0<T_n<\frac{1}{64n^2}<\frac1{16}\quad(n\ge1).$$

The tail estimate follows by monotonicity of the original positive forcing and the inherited bound `r(n+1)<15/(64n²)`: `T_n <= r(n+1) sum_(j>=1)16^-j = r(n+1)/15`. Put

$$\boxed{V_0=-T_0=-\pi/16,\qquad V_n=-T_n.}$$

Then **the entire original four-pole forcing remains identical**:

$$V_{n+1}=16V_n+r(n+1).$$

But for every positive time `n`, `V_n∈(-1/16,0)`, so `floor(V_n)=-1` and `{V_n}=1-T_n`. Consequently

$$\boxed{j_n=\lfloor16\{V_n\}\rfloor=15,\qquad
c_{n+1}=\lfloor V_{n+1}\rfloor-16\lfloor V_n\rfloor=15,\qquad
s_{n+1}=0.}$$

Therefore the full and primitive source compatibility detectors are **exactly one at EVERY positive time**, not just in the limit. Yet `V_n→0` in the reals, and for every fixed integer `h≠0`,

$$\boxed{\lim_{N\to\infty}\frac1N\sum_{n=1}^N e^{2\pi ihV_n}=1.}$$

This is a **provably nonnormal same-forcing changed-seed orbit** with perfect local q16 compatibility. Unlike the arbitrary changed seed `+1/3` in the finite test table, this control is known to be maximally non-equidistributed. It fails the authentic **zero initial condition** and is thus a falsifier of claims that do not actually use that selector. The executable finite certificate returns exact rational forcing bounds, symbolic `V0=-pi/16` provenance, and all-time *paper-proved* structural digit/carry identities; it does NOT pretend to numerically evaluate the irrational seed or prove the analytic limit by finite samples.

**Verdict:** even exact, source-forcing-faithful, all-time, perfect constructive agreement of the two carry forms does not imply any selected Fourier saving. Only an additional observable constraint that genuinely distinguishes the zero-initial source from this changed-seed orbit can do that.

### What this does **not** say

It neither proves nor disproves base-16 normality of π. It does not say the actual π orbit is distributed like the changed-seed control. Its function is to reject the inference **"high same-variable compatibility → source-selected Fourier cancellation"** with an exact four-pole receipt, rather than merely a synthetic control. This is the requested protection against overconfident arithmetic frames.

## 5. Principles for SUCC's global/working/checkpoint architecture

1. **Provenance before similarity.** Every detector identifies the original source, unit, shared variable, time index, boundary, carry and admissible map. Equality under a rewrite is not independent evidence.
2. **Reference declared before selection.** Global probabilities, frame priors and null alternatives must be specified before looking at the detected match. Independent-copy comparisons are labeled descriptive unless that is the true experiment.
3. **New constraints pay a novelty tax.** Linear syzygies require a rank check; nonlinear forms need polynomial/carry/prime relation tests and controls. A rank increase does not guarantee probabilistic independence.
4. **Keep both signed and positive registers.** Full Fourier and primitive Ramanujan characters, source-class amplitudes, KL/chi-square/collision scores, and time-resolved path checkpoints cannot be replaced by a single positive "coherence" number.
5. **Global calibrates; working updates.** Back-transport working observables by actual likelihood ratios / source-compatible pullbacks. Correct for adaptive frame selection, repeated data and optional stopping where a genuine null law exists. A checkpoint martingale under a reference null is not the actual π path.
6. **Arithmetic outcome beats appealing architecture.** A real π advance must derive an **independent source-specific signed inequality** for the original zero-seeded BBP orbit, not a formal re-expression, packet marginal, positive Gram, compatibility score or finite normal-looking sample.

The 'global' object is therefore a **provenance-preserving, calibration-and-consistency authority**. It is not a second vote in favor of whatever internal frame looks convincing.

## 6. The single remaining π-normality gate

From #313, with authentic literal carry and selected arrival-bin midpoint, for every `N,M` and fixed nonzero `h`, the signed source-dependent sum

$$\widetilde C_{N,M}(h)=\frac1N\sum_{n=1}^N
\exp\left[\frac{2\pi ih}{16}\left(c_{n+1}+
\frac{\lfloor M\{U_{n+1}\}\rfloor+1/2}{M}\right)\right]$$

satisfies an **already paid** comparison

$$\left|\frac1N\sum_{n=1}^Ne^{2\pi ihU_n}-\widetilde C_{N,M}(h)\right|
\le\frac{\pi|h|}{16M}+\frac{\pi|h|}{8N}\sum_{n=1}^Nr(n+1).$$

A preset `M_N=max(2,floor(log_2 N))` makes the right side tend to zero. Showing `\widetilde C_(N,M_N)(h)→0` for **every fixed h≠0** would therefore prove π base-16 normality, via the authenticated Green-tail transfer. But **proving this signed cancellation estimate is still open**. The global referee must stop us from replacing it with the recurrence-forced `j_n≈c_(n+1)` compatibility whose score tends to one for every seed.

**Potentially fruitful next move:** find two or more genuinely **nonredundant** source forms, e.g. a Gaussian signed holonomy prediction and an integer carry/arrival prediction that are *not* generated by the same linear source identity. Construct a compatible, past-predictable finite source reference, preserve full `h`-character amplitudes and the zero seed, then prove a new **cross-time** decorrelation/cancellation bound. Audit the constraint's novelty against SS-01/02, the global null against postselection and the modulus estimate against all changed-seed/fake-forcing controls. A new quantity is useful only if its inequality is less demanding than the original Weyl estimate and is actually derived independently.

## 7. Proof, test and authority ledger

| Claim | Authority | Limitation |
|---|---|---|
| Full/primitive character projectors and Ramanujan divisor formula | CLASSICAL, algebraic proof; exact rational tests | Primitive spectrum can miss compatibility |
| Four solutions + four antipodal solutions for x(x-2) at 2^k, k>=4 | PAPER-PROVED; all residues independently enumerated k=4..8 | No theorem about π |
| Fourfold independent-copy ratio; primitive score zero | EXACT CLASSICAL finite source comparison | Ratio not calibrated evidence for same-variable null |
| Precommitted frame-mixture and duplicate-evidence inflation | PROVED elementary probability; exact finite tests | Requires specified null before observed value |
| Predictable e-process / checkpoint Ville controls | CLASSICAL, exact bounded-null-tree enumeration | Not a stochastic model of deterministic BBP selection |
| Seinfeld one-step macro redundancy / zero-seed rank gain | INHERITED SS-01/02, native rank interface | Only linear relations; doesn't prove independence |
| Authentic carry/digit normalized Ramanujan score →1 | PAPER-PROVED corollary of #313 source-spill estimate + exact q16 detector | Holds all initial seeds under forcing; **not π mixing** |
| **Perfect q16 score for all n on V_n=-T_n**; fixed-h selected Weyl mean →1 | PAPER-PROVED using original positive forcing/Green tail; exact rational finite bound tests | Explicit nonnormal changed seed, fails authentic zero selector |
| Authentic selected Weyl `S_N(h)=o(N)` for each fixed h≠0 | OPEN | This is still the actual π-normality theorem |

The code uses exact `Fraction`, integer congruences, the existing authentic source history/selected-branch interface, and the existing Seinfeld rational-rank routine. Its local isolated verification uses *inspected native interface shims*, with no claim of having run the full repository test suite or Lean. Exact receipts are source/test/script SHA-256 stamped and deliberate false-normality mutations fail on replay. The new draft research PR stacks above #314, not on `main`. Both concurrent prompts explicitly forbid main merges without maintainer authorization.
