# Cambrian B: transfer, entropy, advancing targets, and noisy chaos

**Assignments actually executed:** 07, 08, 09, 10, 11, 12, by one cluster worker in one isolated worktree. These are six investigations, not six independent agents. **Base:** `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. Initial worktree clean; scoped additions only. Initial hypotheses and competitive rivals were frozen in `CAMBRIAN_B_HYPOTHESES.json` before new computations or sharing conclusions. Read AGENTS, foundations, method, relevant architecture/roadmap/ledger entries, the import manifest, and existing chaotic-tree/source-quotient/Misiurewicz dossiers. No imported source or archival original changed.

## Verdict and hole contract

The strongest result here is a **proved paper theorem about advancing observation targets**: in the specified logistic/arcsine transfer setting, asymptotic completion of every continuous fixed-base target requires observer depth to exceed target advance by an unbounded amount. Merely increasing both clocks at the same rate does not suffice. Continuous nonpolynomial eigenfunctions make this obstruction exact, with no simulation or finite-to-infinite inference.

The contract is: for the logistic source `f(x)=4x(1-x)`, invariant arcsine measure `mu`, Koopman `Ug=g composed with f`, and invariant conditional transfer `L`, characterize `L^n(t) U^m(t) g - mu(g)` in sup norm, for every continuous `g` and all integer-valued clocks `n,m>=0`. Current truth state: **PROVED LOCAL / paper**, with exact finite algebraic controls. The weakest useful statement is the clock normal form plus one nonpolynomial counterexample. It closes the existing fixed-target-to-moving-target edge without hiding an RH or universal cognition theorem. This is classical operator algebra applied to SUCC's declared observation clocks; scholarly novelty is **UNVERIFIED**. The cheapest falsifier is a sparse Chebyshev mode compared with the independent power-polynomial recurrence. Next lamp for formal authority: a Lean functional-analysis library and proofs of arcsine orthogonality/completeness and the operator extension.

Status vocabulary: DISCLOSED below means explicit paper proof inside the stated mathematical boundary, corresponding to PROVED LOCAL; it does **not** mean Lean-kernel verification. Machine output alone is TESTED MODEL/OBSERVED. No results assert physical sensor attestation, suppression of individual chaotic trajectories, an RH interface, or an actual finite-time supertask.

## 07 — Transfer beyond polynomials

### B07.1: exact Hilbert-space structure

Let `psi_k(x)=T_k(1-2x)`, `k>=0`, where `T_k` is the Chebyshev polynomial. Substitution `x=sin²(pi theta/2)` gives `psi_k=cos(k pi theta)` and transports `mu` to Lebesgue measure on `[0,1]`. Consequently the modes are an orthogonal complete basis of `L²(mu)`, with norm squared 1 for `k=0` and 1/2 otherwise. Completeness follows from density of the cosine basis, or from polynomial density in continuous functions followed by continuous-function density in L² of this finite Borel measure.

The actual logistic map satisfies `1-2f(x)=T_2(1-2x)`. Therefore

`U psi_k=psi_(2k)`,

`L psi_(2k)=psi_k`, and `L psi_(2k+1)=0`.

The last identities follow independently by averaging the two logistic inverse roots (their angle coordinates are `theta/2` and `1-theta/2`); their cosines cancel for odd k. Invariance of the arcsine law makes U an L² isometry, L its adjoint, and `LU=I`. Equal inverse weights are valid for this source law, rather than for arbitrary logistic priors.

Every positive integer is uniquely `q*2^j` with q odd. On each orthogonal chain `{sqrt(2)*psi_(q*2^j):j>=0}`, U is the unilateral forward shift and L the unilateral backward shift. Thus mean-zero L² is the Hilbert direct sum of these chains. L's spectrum on that space is the **closed unit disk**: its norm is at most 1; for each complex `|lambda|<1`, the vector with coefficients `lambda^j` on one chain is an L-eigenvector with eigenvalue lambda; closedness fills the boundary. U has the conjugate spectrum and has no eigenvectors on the mean-zero subspace, by comparing successive coordinates in a forward shift. On the full space the constants add the eigenvalue 1. This is a function-space-specific statement, not a contradiction to spectra/resonances on smoother or rigged spaces.

### B07.2: convergence is targetwise and regularity-sensitive

For every fixed continuous g, `L^n g -> mu(g)` uniformly. Proof: choose a polynomial p with `||g-p||infinity<epsilon`. Transfer is a positive sup-norm contraction, invariant integration is continuous, and the existing degree-halving theorem makes `L^n p=mu(p)` at sufficiently large n. The residual for g is at most `2 epsilon`. The same density/contraction argument establishes convergence in Lp for every fixed `1<=p<infinity` target. No uniform speed over the unit ball follows.

Indeed the mean-zero L² operator norm `||L^n||=1` for every n: apply it to `sqrt(2)*psi_(q*2^n)`. The exact probe includes odd q=5 and depths 38 and 70, retaining norm without expanding an astronomical polynomial.

For a much sharper continuous counterexample, fix any `0<lambda<1` and define

`g_lambda(x)=sum_(j>=0) lambda^j psi_(2^j)(x)`.

The Weierstrass bound `|psi_k|<=1` proves uniform convergence and continuity. Termwise transfer is valid by bounded linear continuity, so `L g_lambda=lambda g_lambda` and `mu(g_lambda)=0`. Evaluating at x=0, where every mode equals 1, proves

`||g_lambda||infinity=1/(1-lambda)` and

`||L^n g_lambda||infinity=lambda^n/(1-lambda)>0` for every finite n.

Hence finite polynomial completion does **not** extend even to all continuous targets. Eigenvalues arbitrarily close to 1 also rule out one exponential rate valid for the entire continuous unit ball. More generally, replace geometric coefficients by nonnegative summable `a_j`; then `||L^n sum a_j psi_(2^j)||infinity=sum_(j>=n) a_j`. Summable tails can decay arbitrarily slowly, making an explicit regularity/target contract indispensable.

Nor does strong convergence extend to all L-infinity targets. In the fair Bernoulli itinerary model, let A be the union, over `j>=1`, of events that all `j+3` bits beginning at position `j²` are zero. Its measure is at most `sum 2^(-j-3)=1/8`. For every n choose j with `j²>=n`: that event depends entirely on the time-n tail and has positive probability. On it, `L^n 1_A=1`. Thus `||L^n 1_A-mu(A)||infinity>=7/8` for every n, although the Lp conclusions remain valid. This is a paper counterexample, not a generated infinite tape.

**Controls:** zero/constant targets; odd-mode annihilation; even-mode survival; sparse versus dense recurrence; high-index holdouts; floats and negative clocks rejected. All finite tests compare declared scopes. **Priority:** standard Chebyshev/shift theory; new-to-repository continuation. **Remaining hole:** certified quantitative rates for a specified regularity class with costs attached to representing/certifying its norm.

## 08 — Natural acim versus Parry symbolic law

Retain the inherited exact alpha root of `r³-2r²-4r-8`, carrier `J=[a,q]`, `a=1/alpha`, `q=alpha/4`, critical point c=1/2, and fixed postcritical point `z=1-a`. Markov cells are A=[a,c], B=[c,z], C=[z,q].

### B08.1: lawful continuous Perron–Frobenius representation

For a Lebesgue density rho supported on J, change variables separately on each monotone branch. At almost every interior y,

`(P rho)(y)=sum_[x in J, f(x)=y] rho(x)/|alpha(1-2x)|`.

Its integral equals the integral of rho, it is positive, and it pushes the source probability law forward. The inverse roots are `b_±(y)=(1±sqrt(1-4y/alpha))/2`. On `(a,z)` there is exactly one J-preimage, `b_+(y)` in C; on `(z,q)` both roots are admissible, lying in A and B. Thus

`P rho(y)=rho(b_+(y))/(alpha sqrt(1-4y/alpha))` on `(a,z)`,

and the numerator on `(z,q)` is `rho(b_-(y))+rho(b_+(y))` with the same denominator.

If rho is an invariant probability density, then its correct stationary inverse conditional operator is

`L_mu g(y)=P(rho*g)(y)/rho(y)` wherever `rho(y)>0`.

This supplies a valid representation; it does not solve its fixed-point equation. Its branch weights explicitly depend on the unknown invariant density. Uniform averaging of algebraic roots is not a source-law identification.

### B08.2: an exact finite-partition obstruction

There is **no invariant probability density constant on each of A,B,C**. If the C-value is zero, PF gives zero on A and B, and then invariance gives zero everywhere. If it is positive, the PF image on each open left cell is a positive constant divided by `alpha sqrt(1-4y/alpha)`, a strictly increasing nonconstant function. It cannot equal a cell constant almost everywhere.

Exact algebra independently checks two C points `17/20` and `9/10`, their two images in A, and unequal Jacobians `7alpha/10` and `4alpha/5`. These witness values calibrate the general monotonicity proof; point values alone would not refute an almost-everywhere density statement. **REFUTED:** the naive cellwise-uniform acim construction from the Parry matrix. **Not refuted by this argument:** a nonconstant invariant density whose aggregate A/B masses happen to equal 1/4 each.

### B08.3: conditional periodic-multiplier discriminator

The actual logistic two-cycle has

`x_±=(alpha+1±sqrt((alpha-3)(alpha+1)))/(2alpha)`

and multiplier `M=-alpha²+2alpha+4`. Algebraically multiply the two derivatives, eliminating the radical, to obtain this formula. The certified alpha bracket proves `|M|>2`; the cycle is away from the finite postcritical set. The inherited Markov source has `h_top(f)=log(sqrt(2))`, so a maximum-entropy periodic-multiplier requirement would demand `|M|=2`.

[Misiurewicz 1981](https://www.numdam.org/item/PMIHES_1981__53__17_0.pdf), Theorem 8.1, printed pp.45–46, provides that requirement for periodic points outside its exceptional set, under conditions (i)–(vi) and its acim component assumptions. This would separate the natural acim from Parry if every applicability assumption is established. The paper also gives PF and acim existence/ergodic results under specified hypotheses, rather than deriving density from adjacency.

**Status is CONDITIONAL, not an unconditional Parry/acim inequality.** Unpaid obligations: full matching of interval partition/exceptional set; all-periodic-point derivative condition including possible neutral cycles; natural acim existence and component support; lifting the symbolic Parry law to the actual carrier. A negative-Schwarzian no-attractor argument is suggested by [Singer 1978](https://epubs.siam.org/doi/abs/10.1137/0135020), but citation proximity does not discharge those obligations. No numerical acim or rigorous interval iteration was constructed. The natural C-to-A branch probability remains explicitly null in the receipt.

**Rival/control:** adjacency already determines natural density versus PF requires Jacobians/density. Null C-density, constant-cell candidate, unequal Jacobians, periodic multiplier, and r=4 explicit arcsine law distinguish the claims. **Next lamp:** complete theorem-applicability audit, then an induced expanding-map or weighted-density interval scheme with certified tail and postcritical singularities; ordinary unbounded orbit histograms are insufficient.

## 09 — Additional source-certified kneading controls

[Milnor and Thurston, *On iterated maps of the interval*](https://public.websites.umich.edu/~kochsc/MilnorThurston.pdf), develops kneading invariants and their relationship to interval-map symbolic/topological structure. The limited construction here does not implement the full theory or classify arbitrary chaotic parameter windows.

Three additional source controls are derived from their original critical orbits:

| Source parameter | Critical itinerary | Declared invariant source | Consequence |
|---|---|---|---|
| r=2 | C,C | atom at 1/2 | one-state phase, zero entropy |
| r=1+sqrt(5) | C,R,C | uniform two-cycle | superstable two-phase source, zero entropy |
| unique r in (383/100,96/25) with f_r³(1/2)=1/2 | C,R,L,C | uniform three-cycle | superstable three-phase source, zero entropy |
| r=4 | C,R,L,L,... | explicit arcsine law | full Bernoulli source, one bit/step |

For the second source, `f²(c)-c=0` at `r=1+sqrt5` follows by exact arithmetic in Q[sqrt5]; the first iterate differs from c. The two-cycle multiplier is zero because one point is critical.

For the third source, exact polynomial recurrence constructs `p(r)=f_r³(c)-c`. Endpoint signs and a rational Taylor enclosure of p' certify a unique root in the stated bracket. A separate direct rational iteration at both endpoints and at 3835/1000 checks the polynomial. The same bracket certifies first iterate >c and second iterate <c; since 3 is prime and the first iterate differs from c, the return has prime period 3. The multiplier is zero. All claims are about this exact cycle source, not all trajectories, full ambient entropy, or an entire attracting parameter window.

Finally a time-dependent rational source at r=3 with initial states `(2/5,3/5)` and prior `(1/3,2/3)` merges at the same next state. Its original-state posterior mean is `8/15`, whereas fair inverse-root averaging gives `1/2`. This is a finite source-prior mutant, not a natural invariant source. The inherited direct source-index oracle and inverse kernels agree.

**Verdict:** source support, kneading and law must be rebuilt when the parameter/source changes. A single alpha phase quotient is not automatically portable. **Remaining hole:** a new chaotic postcritically finite window with a certified natural invariant density and independently weighted inverse history. Generic parameters may need countable kneading models; no finite Markov partition was invented for them.

## 10 — Positive entropy and zero-entropy factors coexist

For every integer d>=2, take source `X=Z/dZ times {0,1}^N`, map

`F(j,b)=(j+1 modulo d, shift(b))`,

and product law uniform phase times fair iid bits. The projection `phi(j,b)=j` is a nonconstant deterministic factor onto a d-cycle. Its n-history has d possibilities independent of n, so its entropy rate is zero. A generating source partition recording phase and current bit has d*2^n n-histories with equal probabilities; its entropy divided by n tends to one bit per step. Therefore positive source entropy alone does not rule out nonconstant zero-entropy factors.

The source is not mixing: phase events recur with period d. Thus this does not contradict the inherited r=4 fair Bernoulli completely-positive-entropy obstruction. The correct separating assumption is CPE/Bernoulli source structure, not simply a positive number called entropy. The alpha bipartite phase is a concrete interval-source relative of this finite-period obstruction, but no measure-preserving isomorphism with the particular product extension is asserted.

**Independent finite route:** enumerate all phase/bit histories for d in {1,2,3,5}, n<=6, compare with closed counts, and include the null d=1 control. **Priority:** classical product/factor construction. **Hole:** a source-conditioned Pinsker-factor classification for the actual natural alpha acim; the topological partition and selected symbolic Markov law do not supply it automatically.

## 11 — Exact observation-debt clock theorem

### B11.1: cancellation normal form and sharp universal threshold

For all nonnegative integers n,m and every continuous or Lp target g,

`L^n U^m g = L^(n-m) g` if n>=m,

`L^n U^m g = U^(m-n) g` if m>=n.

Proof: associate operators and cancel `LU=I` exactly min(n,m) times. No invertibility of the original source map is used. In sup norm U is an isometry because f maps `[0,1]` onto itself; in Lp it is an isometry by invariant measure. Mean is preserved by both.

For the B07 geometric target, this yields the exact formula

`||L^n U^m g_lambda||infinity = lambda^max(n-m,0)/(1-lambda)`.

Consequently, for any integer clock sequences `n(t),m(t)>=0`,

`[for every continuous g, ||L^n(t) U^m(t)g-mu(g)||infinity ->0]`

**if and only if** `n(t)-m(t)->+infinity`.

Sufficiency is B07 targetwise convergence plus the cancellation form. For necessity, if the surplus does not tend to infinity, some subsequence is bounded above by an integer B; the geometric target's residual on that subsequence is at least `lambda^max(B,0)/(1-lambda)>0`. The **same one target** refutes convergence. This is a universal quantifier over fixed continuous base targets; it does not assert necessity for every individual polynomial, some of which finish at bounded surplus.

For clocks with strictly different linear rates, observer rate > advance rate suffices and observer rate < advance rate fails. Equal leading rates are inconclusive: `n=t+floor(sqrt(t)),m=t` converges, whereas `n=m=t` does not. The exact criterion is unbounded surplus, not merely an inequality between asymptotic slopes.

### B11.2: representation cost and the physical-time boundary

Sparse Chebyshev coordinates can encode a high mode k using O(log k) bits, while dense polynomial coefficients can require vastly more. Operator depth, representation size, transmitted source bits, target approximation tolerance, and proof size are different resources. The formula does not identify any of them with Shannon entropy or a physical cost automatically.

If each observer action requires elapsed time at least `c_*>0`, n actions require at least `n*c_*`, so unbounded depth cannot occur by finite elapsed time. A formal Zeno schedule with summable action durations is a different assumption; no physical implementation is established. Conversely an exact structural proof can certify a target without executing its entire inverse tree. The theorem addresses the specified transfer-operation instrument, not all possible proofs/tools.

**Controls:** faster/matched/slower clocks, equal leading rate with sublinear positive surplus, constant and zero targets, fixed polynomial completion, nonpolynomial eigenfunction, high-mode no-decay holdout. **Integration value:** strong precise debt law for a declared instrument; this supplies a useful Moonshot C lemma rather than a universal knowledge law.

## 12 — Noise, missing history, and delayed receipts

### B12.1: exact independent readout/delay channel

Let fair source phase X be reported with independent Bernoulli errors E0,E1, and let independent unknown lag parity D have odd probability p. Reports are `A=X xor E0`, `B=X xor D xor E1`. Centered-bit multiplication, or direct enumeration of the sixteen atoms, gives

`Cov(A,B)=(1-2e0)(1-2e1)(1-2p)/4`.

Known even lag is p=0; known odd lag is p=1 and operational parity transport restores the sign. Unknown fair parity p=1/2 makes the reports independent even with no measurement error. Independent readout errors reduce covariance without altering the underlying deterministic source-phase law. Shared fair error is a decisive mutation: it makes A=B and covariance 1/4, whereas incorrectly imposing independent errors predicts zero. Thus source/error provenance matters.

### B12.2: missing inverse-history bits yield unions, not one invented state

For a tent inverse history of length n, k unknown branch bits, and interior terminal interval [a,b], there are exactly `2^k` disjoint compatible inverse intervals, each width `(b-a)/2^n`; their total length is `2^k*(b-a)/2^n`. Proof: each completed word is an affine inverse branch of slope magnitude `2^-n`, and distinct word interiors are disjoint cylinders. Exact sorted interval unions and direct tent forward replay verify the bounded instances. No uniform source prior is required for the geometry; interpreting lengths as probabilities would require an additional law.

### B12.3: bounded state noise versus symbolic certainty

For trajectories that stay in [0,1], including clipped additive perturbations, a valid map Lipschitz constant A and per-step error epsilon give the recurrence `delta_(t+1)<=A delta_t+epsilon`. Induction yields

`delta_t <= min(1,A^t delta_0+epsilon sum_(j=0)^(t-1) A^j)`.

For tent A=2 this is `2^t delta0+(2^t-1)epsilon`; for logistic r=4 A=4 it is `4^t delta0+(4^t-1)epsilon/3`, before clipping the bound at 1. These are rigorous worst-case finite-horizon bounds, not simulation estimates or convergence claims.

The alpha phase readout at boundary z is certified under state error epsilon only when `|x-z|>epsilon`. There is no uniform positive margin on J*: admissible states lie arbitrarily close to z. Indeed F(z)=z, while continuity keeps nearby points near z for any specified finite horizon, allowing bounded state error to cross the boundary. A phase factor on the noiseless exact source does not imply uniformly robust phase instruments.

**Boundary:** probability formula assumes independent source/readout/delay variables; geometric intervals assume lawful source history and non-destructive endpoint observation; trajectory bound assumes bounded additive errors and valid Lipschitz constants. None authenticate real instruments. **Hole:** a certified natural-acim probability of phase misclassification versus sensor resolution, plus genuinely destructive intervention kernels with source/version transport.

## Evidence, reproducibility, and integration

Executable additions are `observational_succ/cambrian_b_chaos.py`, `tests/test_cambrian_b_chaos.py`, and `scripts/cambrian_b_chaos_probe.py`. The script writes/checks six separate assignment receipts; all report the exact base SHA, Python version, code/test/hypothesis SHA256, and proof authority. It derives exact infinite-series formulas from the written proof; it does not compute an infinite series and label the truncation a proof. The original logistic and Misiurewicz baseline suites ran 34 and 37 tests respectively before modification; 16 scoped new tests cover independent finite representations and mutations. No Lean module was added or run, and no CI success is claimed.

```sh
python -m unittest discover -s tests -p 'test_cambrian_b_chaos.py' -v
python scripts/cambrian_b_chaos_probe.py --check
python scripts/verify_provenance.py
```

The additional full-suite, foundations and ordinal checks are recorded in `CAMBRIAN_B_VALIDATION.json`. Raw frozen hypotheses are distinct from final results. Same-worker implementations share mathematical premises and are not external blind witnesses. A hostile audit of the paper statements is still required before status promotion to a shared ledger.

| Scoped claim | Earned status | Unpaid obligation |
|---|---|---|
| B07.1 Hilbert chain decomposition/spectrum | PROVED LOCAL paper, classical | formal analytic authority |
| B07.2 targetwise convergence, continuous eigenfunctions, L-infinity counterexample | PROVED LOCAL paper | quantitative regularity/cost contract |
| B08.1 correct source-density PF representation | PROVED LOCAL paper, classical | invariant fixed-point construction |
| B08.2 three-cell constant-density invariant model impossible | REFUTED candidate / PROVED obstruction | actual natural acim branch masses |
| B08.3 unequal periodic multiplier vs maximum entropy requirement | exact algebra + CONDITIONAL theorem application | all classical applicability/support assumptions |
| B09 extra critical cycle sources/three-return root | PROVED LOCAL paper + exact intervals | new chaotic window natural source |
| B10 positive entropy with deterministic zero-entropy cyclic factor | PROVED LOCAL paper, classical | actual alpha-acim factor classification |
| B11 universal continuous advancing-target catchup iff unbounded surplus | PROVED LOCAL paper + exact mode controls | formalization and other instruments |
| B12 noise/delay/missing-history/bounded-error laws | PROVED LOCAL paper + finite exact controls | natural density error mass and destructive probes |

Prioritize integration of B11 and the explicit B07 function-space distinctions. Retain B08.3 as conditional and B08 natural density as UNVERIFIED. No shared O IDs have been allocated; no README, architecture, roadmap, ledger, or CI file was changed.

The diagnostic vector remains split: source-map adequacy is proved for the declared rational/algebraic/logistic instruments, but natural-acim source construction is unresolved; algebraic discrimination is available for the tested candidates; contact with actual measured chaos is absent; no commitment-coupling or truth-probability number is inferred. Classical-source attribution, exact arithmetic, theorem scope and physical provenance are different constraints.
