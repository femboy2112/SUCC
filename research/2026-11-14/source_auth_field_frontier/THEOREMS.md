# Principia Observatoris — Source Authentication × Field-Class Reconstruction

**Date:** 2026-11-14. **Round:** The Source Authentication Forge, continuing [draft PR #628](https://github.com/femboy2112/SUCC/pull/628). **Status:** conditional mathematical theorems, finite exact tests, and an actually executed local *software* source experiment; no verified law of external physical reality. The author's original SimpleField / IdealHardField / FuckedField meanings are preserved and made source/target/toolkit-relative, **not** replaced by a single confidence number.

**Strongest interpretation of the user's goal.** The source substrate/coupling generates both observations and lawful state transitions. An observer's retrospective posterior is a model of what happened; its policy changes what it can subsequently encounter. An invariant predictive span is a useful reference. To justify that reference, the observer must retain the source law, its provenance, the legal probe menu, measured costs, actual records, and an independently evaluated future holdout. Self-consistency does not authenticate the source.

## 0. Typed objects and claim authority

A declared finite hidden source is 
\[
\mathcal S=(X,\mu_0,A,(J_a)_{a\in A},\Gamma),\quad J_a(x,x',o)=\Pr(X_{t+1}=x',O_{t+1}=o\mid X_t=x,\operatorname{do}(a)).
\]
Here \(\Gamma\) specifies output alphabets, action availability, units and legal start conditions. A policy \(\pi_t\) is predictable from the delivered transcript and the observer's permitted memory. The resource contract \(C(a,x,x',o)\) must be separately specified and measured if used; the probability law \(J\) does not uniquely determine a cost.

There are three distinct claims:

1. **Execution identity:** a recorded trace arose consistently from a specified executable, actions, and a precommitted hidden tape. This can be audited computationally, under hash-binding and process-integrity assumptions.
2. **Statistical model fit:** a candidate \(J\) predicts observed instrument outcomes better than specified rivals on a genuinely fresh sequence, under a declared stochastic source hypothesis and calibrated test. This is statistical evidence, not universal source truth.
3. **Physical source adequacy:** the audited program and probability law correctly represent the intended real, non-software physical process. This has **not** been tested by the present experiment.

For SUCC field classes, the proper referent is \(\operatorname{FieldClass}(\mathsf{Source},\mathsf{Target},\mathsf{Tools})\), inherited explicitly from [docs/OBSERVER_PROOF_ACCESS.md](../../../docs/OBSERVER_PROOF_ACCESS.md), [FIELD_LIMIT_TRICHOTOMY.md](../../2026-10-15/FIELD_LIMIT_TRICHOTOMY.md), and [field_limit_compactness.py](../../../observational_succ/field_limit_compactness.py). Do not silently promote the toy source's successful arithmetic into physical source adequacy.

## FSA-01 — One coupling generates dynamics and evidence (CLASSICAL; scoped)

From the single joint law, \(P_a(x,x')=\sum_o J_a(x,x',o)\), and the likelihood of the actual readout given the previous state is \(L_a(o\mid x)=\sum_{x'}J_a(x,x',o)\). A post-state-only factorization \(J_a(x,x',o)=P_a(x,x')\ell_a(o\mid x')\) is **not automatic**.

Our registered two-state source has actions:

- **sense:** unchanged current bit; report old bit correctly with probability \(p\), otherwise its complement, fixed charge 2 credits.
- **flip:** flip current bit, report a deterministic 0, charge 1 credit.
- **reset:** report old bit with the same accuracy, then set current bit to 0, charge 4 credits.

We preregister two source hypotheses: \(P:p=3/4\) and \(Q:p=1/2\). Their transition and cost tables are identical; only the observation channel differs. For reset, the same successor state 0 can arise from either predecessor with different outcome laws, so no post-state-only likelihood realizes the joint source contract when \(p\ne1/2\). This is the inherited RFO-01 obstruction with a concrete executable protocol.

**Consequence:** an observer can retrospectively learn about a pre-reset source even though the current source has been overwritten. A present-state-only observer cannot reconstruct arbitrary earlier source histories without records.

## FSA-02 — Executed-source commitment and independent replay (OBSERVED, bounded)

Before any registered action, the source subprocess obtains a 128-byte random tape using Python's OS-backed `secrets.token_bytes` and selects its fixed model \(P\) or \(Q\). It publishes

\[
H=\operatorname{SHA256}(\texttt{protocol}\Vert\texttt{model}\Vert\texttt{tape}),
\]

plus the exact `source_process.py` file digest and legal action names. It does **not** publish hidden initial state, the selected model, or the random tape until the experiment ends. The initial state is the low bit of tape byte zero; each subsequent action consumes one tape byte. A sense/reset report agrees with the pre-action state if `(byte % 4) < 3` under P or `< 2` under Q. A flip is deterministic. All actions have explicit recorded credit charges. The observer policy uses **neither** the source model label nor the commitment digest to choose actions.

After the last step, the source reveals the model label and tape. An independent module checks the precommit, executable digest, every action, each hidden state transition, every result and fixed tariff, and the final hidden state. It separately computes the observer's prior-to-next posterior, *original-source posterior*, predicted outcome law, selected adaptive action, likelihood ratio and Brier score from the source protocol without importing the primary observer model. The audit rejects modified tape, model label, program digest, outcome, action, posterior, likelihood and charge. The separate source process refuses a hidden-label `peek` action.

**Precisely what this establishes:** the 24 logged sessions are computationally **replay-consistent** with the registered executable and precommitted source tape, provided the cryptographic digest binds the commitment and the operating system actually executed the recorded code. The trace is real local subprocess I/O, not a fabricated list of expected samples. **What it does NOT establish:** unpredictability of OS randomness, a cryptographic attestation of the running binary by the OS, universal validity of the probability law on future OS seeds, any external physical energy calibration, or that SUCC's BBP/arithmetic carrier obeys this protocol.

The subprocess reports nanosecond timing and the orchestrator independently records round-trip timing. These are *actual runtime measurements* but **not** a calibrated physical-energy law, nor are they included in the model likelihood. Timing could leak hidden information; allowing timing-dependent policies or stopping requires enlarging the source observation law and recalibrating the statistical test. Cost in credits is a declared tariff, not joules.

## FSA-03 — Adapted posterior and self-model (CLASSICAL / independently checked finite execution)

For \(J_a\) as specified, let \(b_t(u,x)=\Pr(X_0=u,X_t=x\mid h_t)\). For actual action \(a\) and outcome \(o\), define
\[
\tilde b_{t+1}(u,x')=\sum_x b_t(u,x)J_a(x,x',o),\qquad z=\sum_{u,x'}\tilde b_{t+1}(u,x'),\qquad b_{t+1}=\tilde b_{t+1}/z\ (z>0).
\]

This is exact conditional probability for a finite source. A zero-probability observed event under a model is a **model conflict**, not a posterior to be normalized by fiat. Every selected action is a deterministic function of the **previous delivered transcript and modeled belief**; the act of observing one's own predictable decision is not independent evidence about hidden state. The source model's `original,current` belief and the independent auditor's implementation agree on all executed traces.

This gives a genuine **recursive observational instrument** in a controlled program, not a universal consciousness or objective-observer theorem. The operational self-model includes its remembered belief, policy, readouts and chosen actions. It still cannot infer an inaccessible hidden tag or unrecorded history without a lawful source-sensitive channel.

## FSA-04 — An anytime-valid model discriminator, with its exact scope (CLASSICAL)

Fix two predeclared models \(P,Q\) whose legal outcomes and action protocol agree. For a policy selecting \(a_t=\pi_t(h_{t-1})\) predictably, define the model-specific probability of the actually received outcome history and the likelihood ratio
\[
E_t=\frac{\Pr_P(O_{1:t}\mid\pi)}{\Pr_Q(O_{1:t}\mid\pi)}.
\]

Assume \(Q\) assigns positive conditional probability to every history whose ratio is evaluated, with the same lawful policy under both models. Writing \(p_t(o\mid h_{t-1}),q_t(o\mid h_{t-1})\) for their **posterior predictive** laws, the update is \(E_t=E_{t-1}p_t(o_t)/q_t(o_t)\) and
\[
\mathbb E_Q[E_t\mid h_{t-1}]=E_{t-1}\sum_o q_t(o)\frac{p_t(o)}{q_t(o)}=E_{t-1}.
\]

Therefore \(E_t\) is a nonnegative unit-start **test martingale in the action/output filtration** under \(Q\). Ville's inequality gives
\[
\Pr_Q\{\sup_{t\ge0} E_t\ge1/\alpha\}\le\alpha.
\]

This is established sequential testing mathematics (see Koolen & Grünwald, *Log-optimal anytime-valid E-values*, IJAR 2022, https://doi.org/10.1016/j.ijar.2021.09.010; Ramdas–Grünwald–Vovk–Shafer, *Game-theoretic statistics and safe anytime-valid inference*, 2023, https://arxiv.org/abs/2210.01948). It is **not** a probability that \(Q\) is false, and it does not prove \(P\) as the unique physical law when \(Q\) is rejected.

**Substrate firewall:** the actual demonstration uses a commitment digest and observes runtime timing as well as modeled outputs. The exact martingale theorem is conditioned on the modeled action/output filtration and the **assumption of independent uniform bytes** under the OS-random source. The commitment is not used by the policy or stopping rule; do **not** assert the martingale remains valid conditionally on the hash under an unbounded observer that can invert the commitment, nor under arbitrary timing-driven stopping. Nor does the code mathematically prove the OS randomness assumption. A source whose output probabilities are time/history dependent beyond the declared J requires its own test.

**Exact finite calibration:** independently enumerated adaptive outcome histories yield \(\mathbb E_QE_t=1\) for all checked depths through 7; at threshold 4, exact null crossing probability is at most \(1/4\). An independent raw-path implementation checks the action-aware likelihood structure, not just the same model's filter output. An uncalibrated *hindsight alternative* setting \(P_{O_t}(O_t)=1\) after observing a fair-coin outcome gives a one-step likelihood ratio 2 under each null outcome, so \(\mathbb E_QE=2\), proving that fitted-on-test evidence is invalid.

## FSA-05 — No finite universal source authentication without a source-class restriction (PROVED COUNTERMODEL)

For every finite horizon \(H\), construct two lawful finite deterministic sources emitting the same observation 0 through time \(H\), using a hidden finite counter and a single output alphabet. At time \(H+1\), the first continues to emit 0 while the second emits 1. All permitted actions may have identical effects and costs until that time. Consequently every observer experiment stopped by time \(H\) has identical transcripts under the two sources but different global behavior.

Thus \(\forall H\;\exists\) a delayed mutant evading horizon \(H\). It is **not** \(\exists\) one fixed mutant indistinguishable for all time, nor a general no-go when a verified common upper bound on state dimension/recurrence order is supplied. For a fixed known finite model class, inherited SUCC realization bounds can give finite predictive equivalence tests. This no-go concerns arbitrary complexity and cannot certify a universal physical source map from a successful finite holdout.

## FSA-06 — Predictive equivalence versus actual source identity (CLASSICAL, strict)

Let two source models with the same legal action/outcome contract induce equal probabilities for every finite action/output word. For any adaptive policy measurable with respect to previously observed words, the induced transcript laws also coincide, by induction: the same visible history causes the same action, and every conditional next-output probability is the ratio of equal joint-word probabilities whenever the history has positive probability. Hence **no lawful finite transcript-only test can statistically distinguish the models**; they can nevertheless have different hidden-state spaces or histories.

Exact witness: a one-state fair-output source and a two-state source that alternates its hidden state while emitting fair independent outputs. The shared predictive-span fixed-point algorithm from RFO-07 proves they agree on **all finite observations**, although their hidden representations are unequal. A different example uses source states \((v,h)\) with a visible bit \(v\) and hidden tag \(h\). All lawful actions toggle/read \(v\) and preserve/hide \(h\). For target \(P=h\), different sources are indistinguishable under all admissible actions; for a future visible-readout prediction, a finite query program works.

**Consequently, the *same* source may be SimpleField for a future predictive query and FuckedField/nonidentifiability for hidden-source identity.** These are two different \((\mathsf{Source},\mathsf{Target},\mathsf{Tools})\) triples, not a contradiction.

## FSA-07 — Non-degenerate field classification as a vector, not a single score (CLASSICAL synthesis)

Recover the original definitions rather than changing them:

| User's historical name | Sharp scoped criterion | Key exclusion |
|---|---|---|
| **SimpleField** | A finite effective source-faithful program plus proof computes every demanded finite coordinate/query of the target; source membership/adequacy is independently established for the asserted scope | A guessed posterior or a finite fitted predictive law is not a verified global source |
| **IdealHardField** | Mathematical existence/witness truth is proved, and a **separate impossibility theorem** rules out any computable witness within the stated effective toolkit | A timeout or a presently missing algorithm proves no such impossibility |
| **FuckedField / nonexistence** | The demanded global source has been proved absent, even if every finite stage can be satisfied | No inference from a few unsuccessful searches |
| **FuckedField / nonidentifiability** | Two fixed admissible source states have identical complete lawful evidence but different values of the specified target | \(\forall N\exists\) a moving rival is not enough for permanent indistinguishability |
| **FuckedField / phantom source map** | Every finite observation can be realized by some source in the ORIGINAL source class, but no single source in that original class realizes all observations | A limit in a larger completion is not necessarily an original-source realization |
| **Unresolved / dark** | Relevant existence, effective accessibility, or adequacy obligations lack a proof or decisive probe in the current closure | Not a theorem of unprovability or nonexistence |

The proposed updated object is a **typed claim ledger** rather than mutually exclusive metaphysical field labels:
\[
\mathsf{FState}(S,P,\mathcal T)=(E,I,C,W,G,\Sigma,\mathcal P),
\]
where \(E\) = original-source existence, \(I\) = target identifiability under the **whole lawful observation closure**, \(C\) = effective query construction, \(W\) = global witness computability/noncomputability theorem, \(G\) = finite/global gluing and phantom status, \(\Sigma\) = source-map adequacy, and \(\mathcal P\) = available actual probes/operational cost. These coordinates may be unknown and are not truth probabilities. The legacy labels become **partial projections with exact evidence obligations**; nothing requires a complete global trichotomy.

The accompanying small `field_axes` function is a conservative report constructor from supplied **verified certificates**, not an automated mathematical proof of its boolean inputs. It rejects obvious contradictory combinations rather than using precedence to hide conflicts. `source_attested=True` means that a particular declared source is attested **at the specified level**; execution replay, statistical calibration, and physical source adequacy must not be conflated into one boolean when moving beyond this toy calculator.

The original [Kleene-tree witness](../../2026-10-15/FIELD_LIMIT_TRICHOTOMY.md) is a true **IdealHardField** instance under its complete effective presentation and classical finitely-branching compactness: there is an infinite path yet no computable such path. **No finite experiment in this round reproduces that infinite impossibility proof**. The original theorem also establishes a valuable boundary: a *unique* infinite path through a decidable finitely branching tree would be computable by searching levels until the requested prefix stabilizes. The new observer's predictive-span fixed point cannot promote the original Kleene path to a computable witness.

### Original-source phantom, retained exactly

Prescribe a profinite residue profile with \(h\equiv1\pmod2\) and \(h\equiv0\pmod p\) for every odd prime \(p\). Every finite list of primes has an integer witness: the product of all odd primes in that list is odd and divisible by each. But **no single integer** has those residues for all primes: any nonzero integer has only finitely many prime divisors, while 0 fails the modulo-2 condition. The point exists in a profinite completion, but *not* in the original integer source class. This is the historical SUCC phantom original-source failure, not a new mathematical discovery or a physically observed impossibility.

## FSA-08 — Scoring and decision transport do not prove source identity (CLASSICAL)

The Brier score for a binary forecast \(p\) and observation \(y\in\{0,1\}\) is \(2(p-y)^2\). For true Bernoulli distribution with success probability \(r\), the expected excess over the correctly calibrated forecast is \(2(p-r)^2\ge0\). This strictly proper scoring property is classical. A one-run score is only one random realization. We predeclare P/Q models and the predictable probe policy before holdout; no sample is used to refit either law.

All 24 local sessions (12 under each model, 20 actions per session) have authenticated postrun tapes, reproducible measured timing logs, exact fixed charge credits, and independently checked policy, initial-state posterior, and likelihood evidence. Reported source labels are disclosed **after** actions. Under the P-source sessions, 8/12 terminal e-values were \(\ge4\); under Q-source sessions, 1/12 was \(\ge4\). These are observed frequencies, not a p-value or a proof of a unique true model. Alternative and null mean scores are reported in `VALIDATION.md` as numerical diagnostics, with no universal source-law inference.

## FSA-09 — Source-map/identity boundaries, next decisive instrument

The already-executed local source **does** supply a real executable causal carrier and a reproducible trace. Its source law is publicly declared and independently replayable, but the statistical assumptions about entropy and the physical meaning of the measured clocks remain unverified. The action tariff is the registered unit of cost; time measurements remain a separate noisy observable that **could** leak information not represented by our 2-outcome J. This is a σ/source-map adequacy issue, **not** a failure of mathematical Bayesian conditioning. A future physical hardware/sensor experiment must specify the sensor's actual noise law, legal interventions, ambient environment, timing leakage and source correspondence before claiming physical authentication.

**Next verdict-changing probe:** Take two predeclared physically distinct candidate source mechanisms with overlapping instrument supports, independently calibrate a high-precision timing or energy meter as a *joint observed outcome*, and run blind prospective holdouts under randomized legal interventions. Compare (i) source-labelled trial audit, (ii) null e-process with the full action/outcome/meter filtration, (iii) predictive equivalence by full finite basis, and (iv) whether the hidden target descends through lawful evidence. Include a delayed-mutant source beyond the training horizon and a genuine target-relative IdealHard theorem witness from an independent effective-computability proof. No claim that π normality, RH, GR, source-god observer, or physical quantum measurement has been proved.

## Evidence / provenance

- **SUCC original Simple/IdealHard/Fucked definitions:** [OBSERVER_PROOF_ACCESS.md](../../../docs/OBSERVER_PROOF_ACCESS.md), [FIELD_LIMIT_TRICHOTOMY.md](../../2026-10-15/FIELD_LIMIT_TRICHOTOMY.md), [field_limit_compactness.py](../../../observational_succ/field_limit_compactness.py), and earlier inherited source-target access modules. These are **inherited** (not separately discovered here).
- **Inherited recursive source filter and predictive reference:** [PR #628](https://github.com/femboy2112/SUCC/pull/628), `recursive_observer.py`, RFO-01..10. New work is the **audit and integration** of those results with actual local subprocess contact and field classification.
- **Independent implementation sources:** `source_process.py` (actual subprocess); `source_authentication.py` (observer); `independent_replay.py` (audit does not import observer); `independent_oracle.py` (direct raw hidden-path enumeration). Shared protocol is declared; independence is **implementation/method**, not empirical independence of source laws.
- **Tests:** `tests/test_source_authentication.py`; locally executed together with inherited `test_recursive_observer.py` in an isolated scaffold. Raw logs and exact source-session payloads in `receipts/`.
- **External antecedents:** Koolen–Grünwald (2022) and Ramdas et al. (2023) for test martingales/e-values; standard controlled hidden-Markov/POMDP filtering and proper scoring. Priority for any project-specific synthesis is unverified; no new universal physics theorem is claimed.
