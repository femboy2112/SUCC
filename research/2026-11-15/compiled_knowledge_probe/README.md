# Compile once, probe many: observer-relative reconstruction

**Date:** 2026-11-15. **Authority:** elementary mathematical arguments under declared assumptions, a bounded exact model, and an OPEN source-to-implementation theorem. This note is additive research, not a change to SUCC's accepted foundations.

## Motivating proposal (steelman)

Finding a hidden structure can resemble locating a needle in a haystack. Once that structure is retained as the observer's own representation, the cost of **finding the same structural probe again** can become negligible compared with the original discovery cost. The observer can then apply that probe to fresh evidence. This is an operational change in its available reasoning pathways, not a physical change in the hidden source.

Separate five objects: source \(\theta\); recorded evidence \(R_t\); verified representation \(S_\theta\); stored probe program \(P_\theta\); and new target observation \(x\). A model-relative certificate never by itself authenticates the external source. Merely making a probe representable does not make it executable on a carrier.

This directly extends the open *source-bound predictor compiler* question in draft [#633](https://github.com/femboy2112/SUCC/pull/633), and respects the action/outcome/target distinctions in drafts [#619](https://github.com/femboy2112/SUCC/pull/619) and [#641](https://github.com/femboy2112/SUCC/pull/641). This main-based PR does not import or silently merge those drafts.

## CKP-01. Conditional compilation and amortization (PROVED LOCAL; classical accounting)

**Domain.** For each input length \(n\), a fixed source \(\theta\in\Theta_n\), an authenticated discovery oracle, a representation compiler, and a family of fresh queries \(x_1,\ldots,x_k\). All costs refer to one declared sequential machine model. Assume:

1. a discovery process eventually returns the correct \(S_\theta\) with total cost \(D(n)\), including any required certificate checks;
2. compiling and retaining \(P_\theta\) costs \(C(n)\), with storage explicitly budgeted;
3. on every fresh input in the declared family, the compiled probe computes the intended answer correctly in at most \(V(n)\) operations (including input access and any necessary new source interaction);
4. the source contract, probe semantics and any calibration needed for correctness remain valid across all \(k\) queries.

Then the total work is bounded by

\[
T_{\mathrm{compiled}}(n,k)\le D(n)+C(n)+kV(n).
\]

If a separately specified baseline independently solves each query at cost \(A(n)\), and \(A(n)>V(n)\), this *upper bound* beats the baseline cost \(kA(n)\) whenever

\[
k>\frac{D(n)+C(n)}{A(n)-V(n)}.
\]

Proof: sum one discovery, one compilation and \(k\) applications; solve the strict cost inequality. The statement gives no saving if there is no valid positive gap \(A-V\), and no amortized saving if the source changes enough to invalidate the program. With \(D,C\) fixed for the same source, \((D+C)/k\to0\); **\(V\) does not tend to zero** merely because memory stores the structure.

A stored handle may allow \(O(1)\) *program selection*. Reading an \(n\)-bit input, executing the test, maintaining a certificate, and acquiring source data are separate costs. Neither an unrestricted P-versus-NP result nor a new decidability class follows: advice or precomputation may itself be exponential and may encode the answer to the hard instance.

## CKP-02. Exact needle-in-haystack example (PROVED LOCAL)

Let \(\Theta_n=\{0,1\}^n\), \(N=2^n\), and fix an unknown key \(\theta\). The *only* discovery instrument is the yes/no equality oracle \(E_\theta(i)=[i=\theta]\). An adaptive deterministic algorithm that must identify the key with certainty in the worst case requires at least \(N-1\) equality queries, and sequentially checking any \(N-1\) distinct candidates achieves this bound.

**Lower bound:** as long as at least two candidates have not been queried, an all-negative transcript is compatible with both; no deterministic answer is guaranteed. Each negative equality test eliminates only one candidate. After \(N-1\) negative tests exactly one candidate remains. This worst case is attainable for each algorithm by an adversarially chosen fixed \(\theta\). **Upper bound:** sequential elimination identifies \(\theta\) from either an early positive or the sole survivor.

After discovery, storing \(S_\theta=\theta\) makes the program \(P_\theta(i)=[i=\theta]\) directly selectable. Its worst-case bit-model execution cost is \(O(n)\), not zero; storage itself uses \(n\) bits. Repeatedly querying the same unchanged source avoids the original \(2^n-1\) discovery interactions. This is a *finite demonstration of amortized knowledge*, not a theorem about general NP-hard reconstruction.

**Adversarial controls:** replacing the oracle's key after compilation makes a cached probe wrong; replacing an oracle with a different readout semantics invalidates the certificate; withholding access to the fresh query blocks application. Replaying past observations is not fresh corroboration. The companion exact script checks the worst-case bound, rival indistinguishability before the final separating query, and source-drift failure.

## CKP-03. The correct zero (PROVED LOCAL; classical information identity)

If a random variable \(Q_\theta\) denotes the stored probe, deterministically retrievable from observer memory \(M=(S_\theta,P_\theta)\), then

\[
H(Q_\theta\mid M)=0,\qquad I(Q_\theta;M)=H(Q_\theta).
\]

Thus the structural choice has **zero residual conditional uncertainty**, not zero mutual information or independence. Under a choice policy, \(P(\text{select }Q_\theta\mid M)\) can rise because the probe is now available and indexed. This is a policy/knowledge effect, not amplification of external truth probability.

No information identity entails zero computational cost or source correctness. Exact representation, approximate learned predictors, and physical interventions require distinct contracts.

## CKP-04. Minimal-reinterpretation crucible

**Initial strongest faithful hypothesis H0:** once a hidden structure is known, its future observation costs zero; consequently hard reconstruction becomes easy.

**Crucify with receipts:**
- Input-reading obstruction: the \(n\)-bit equality decision in CKP-02 must inspect input information in the worst case; selecting a cached function is not executing it.
- Adversarial source drift: a probe compiled for \(E_\theta\) fails for \(E_{\theta'}\) on input \(\theta\) when \(\theta'\ne\theta\).
- Advice/precomputation boundary: an exponential initial search cannot be erased from total complexity by analyzing just the post-discovery stage.
- Accessibility boundary: a symbolic predicate may be representable without any permitted physical probe.

**Verdict on H0: REFUTED in general.** The above constructive models refute the unqualified zero-cost and universal-easiness readings; they do not refute reusable knowledge.

**Minimal surviving correction H1 (PROVED LOCAL under CKP-01 hypotheses):** once a correct structure has been discovered, stored and source-validated, the observer can avoid paying the *same discovery cost* on subsequent queries in the covered family, provided the compiled probe is legal and its application cost is counted. A constant-time reference to a stored probe is possible in an indexed memory model, not a zero-cost observation. H1 retains the original insight without claiming P=NP.

**Methodological algorithm (PROPOSED):** (i) steelman the original hypothesis with domain and quantifiers; (ii) choose a countermodel and a prediction that could kill it; (iii) record the actual receipt and which clause failed; (iv) find the *smallest explicit restriction* preserving the central measurable claim; (v) test the repaired claim on a fresh holdout and an independent mutation. Here, 'smallest' is only meaningful after declaring a metric on changed assumptions/claims. Without such a metric there is no unique mathematical minimal repair. A repaired hypothesis must still predict something risky; merely redefining away falsifiers is not progress.

This instantiates the repository's [steelman–crucible–verdict method](../../../docs/METHOD.md), with a needed fourth move: minimal, explicitly costed reinterpretation and retest.

## Research interface and falsification

Proposed source-bound compiler input: \((\Theta,R,\mathcal{Q},G,\text{cost model},\text{source identity},\text{fresh target family})\). Output must be one of a replayable compiled probe and its certificate, a source-compatible same-report/different-target rival, or an honest unresolved status. A runtime cost declaration must include compilation, storage, input access, interaction, and source recalibration. A Yoneda-style family of separating relations can establish **identifiability** under sufficient probes; effective construction of an executable and efficient probe needs additional proof.

**Next verdict-changing test:** implement two source-identical reconstruction tasks with different certified representations or dependency widths; run a predeclared fresh holdout where the compiled probe is fast and source-matched, then mutate the source, instrument, cost model and encoding. Record a costed speedup only if the discovery+compilation cost, repeated executions and accuracy are all accounted for. No such external benchmark or authenticated BBP phase/carry map is claimed here.

The TLICA components remain separate: \(\kappa\) actual contact; \(\phi\) target indistinguishability relative to probes; \(\sigma\) source-map adequacy; \(\rho\) commitment; \(\mu\) probe availability. A newly stored program can improve \(\mu\) and resource-relative pathways while leaving \(\sigma\) unverified. The authentic pointed BBP source, signed R0, π normality and RH are not resolved by CKP-01–04.

### Reproduction

Run `python research/2026-11-15/compiled_knowledge_probe/exact_probe.py` from the repository root. The script uses Python's standard library and checks exact finite equalities and deliberate countermodels; it is *not* an empirical timing study. Full repository regression, provenance scripts and Lean were not run as part of this documentation experiment unless separately recorded.
