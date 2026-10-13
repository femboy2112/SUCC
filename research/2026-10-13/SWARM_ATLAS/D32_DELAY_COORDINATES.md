# D32 — Chronological delay reconstruction

## 1. Original question

Can retained chronological reports reconstruct their **original** source, rather than only a current state or a model-generated future? Steelman: additional causal encounters can refine a lossy observation without adding a new sensor. The gap is a probe-gap until the transition, readout, clock and admissibility contract are supplied. This dossier distinguishes a mathematical reconstruction from empirical instrument authentication; neither human-brain realization nor academic novelty is claimed.

## 2. Existing mathematical context

**CLASSICAL.** Takens, [*Detecting strange attractors in turbulence*, Theorem 1, pp. 369–371](https://www.math.ucdavis.edu/~saito/data/synchrosqueezing/takens_detect-strange-attractors-turbulence.pdf) ([publisher DOI](https://link.springer.com/chapter/10.1007/BFb0091924)), establishes an embedding into \(\mathbb R^{2d+1}\) for generic pairs consisting of a \(C^2\) diffeomorphism of a compact smooth \(d\)-manifold and a \(C^2\) scalar readout. Genericity concerns pairs; it does not certify an arbitrary fixed sensor, identity dynamics, sampled clock, noninvertible logistic map, noisy record or backacting instrument. A finite trace alone does not identify the unknown global delay map. No code here reproves Takens.

Native `nerode_probe_growth.py` evaluates generated expressions \(q\circ U^j\) against a complete stationary finite source table; its reset-access flag is false. `dynamic_fourier_tower.py` already tests linear observation descent by kernel invariance. Logistic modules preserve original-source/version/chronology distinctions. These are provenance-related leads, not independent physical witnesses.

## 3. Proposed SUCC objects

Let \(S\) be a declared source, \(f:S\to S\) its deterministic stationary update, and \(q:S\to O\) a permitted passive readout. Reading leaves the state unchanged. From **one** initial source \(s_0\), retain encounters \(y_j=q(f^j(s_0))\) with source ID, version, basis and event epoch. Arrival epoch may be later; sort by event epoch and require receipt availability at the inference checkpoint. Define
\[
D_k(s)=(q(s),\ldots,q(f^{k-1}s)).
\]
Generated predictions are a separate evidence kind. No counterfactual reset is assumed. If reading instead applies a known map \(B\), replace the inter-read dynamics by \(f\circ B\); an unknown \(B\) blocks the passive formula.

## 4. Candidate theorem

**PROVED LOCAL, classical content.** For every set-valued target \(\tau:S\to Z\), a decoder on \(D_k(S)\) exists exactly when \(D_k(s)=D_k(t)\Rightarrow\tau(s)=\tau(t)\) for all \(s,t\). Full original-source recovery is equivalent to injectivity.

For \(S=K^n\), \(K=\mathbb Q\) or \(\mathbb R\), known \(F\in K^{n\times n}\), passive \(C\in K^{m\times n}\), and **all** initial states, put
\[
O_k=[C;CF;\ldots;CF^{k-1}],\qquad D_k(x)=O_kx.
\]
For any linear original target \(Tx_0\), a decoder exists iff \(\ker O_k\subseteq\ker T\), equivalently \(\operatorname{row}T\subseteq\operatorname{row}O_k\), equivalently \(LO_k=T\) for some \(L\). Full recovery requires rank \(n\). A current target \(Tx_{k-1}\) instead requires \(\operatorname{row}(TF^{k-1})\subseteq\operatorname{row}O_k\). These statements need not hold on a restricted nonlinear carrier under the same rank criterion.

## 5. Proof attempt

The general decoder assigns a fiber's common target value; conversely any decoder forces that constancy. For linear maps, equal delays mean their difference lies in \(\ker O_k\). Kernel inclusion gives a well-defined linear map on the image; extend a basis to obtain \(L\). This proves the row-space equivalence and supplies an actual decoder, rather than an analogy.

Let \(W_k=\operatorname{row}O_k\), \(W_0=0\). A plateau \(W_{j+1}=W_j\) makes \(W_jF\subseteq W_j\), so every later row is already present. Among the first \(n\) inclusions, either all are strict and \(W_n=K^n\), or a plateau occurs. Therefore \(W_n\) contains **every** future delay row: \(n\) reports settle linear all-future observability. This is conditional on known finite dimension and stationary laws, not an infinite experiment.

## 6. Crucible

**TESTED MODEL** exact receipts; corresponding unrestricted claims are **REFUTED** by the witnesses.

* **Sharp delay:** cyclic shift \(Fe_j=e_{j-1\bmod n}\), \(C=e_0^T\): \(0\) and \(e_{n-1}\) agree through \(n-1\) reports; report \(n\) separates them. Ranks are \(1,\ldots,n\).
* **Permanent alias / nongeneric identity:** \(F=I_2,C=e_0^T\) hides \((0,1)\) forever. On the compact circle, identity dynamics and \(q(\theta)=\cos\theta\) also alias \(\theta\) and \(-\theta\) at every delay.
* **Readout reset:** \(F\) swaps coordinates, \(B=\operatorname{diag}(1,0)\), \(C=e_0^T\). Passive generated reports for \((0,1)\) are \(0,1,0,1\); actual read-then-reset encounters under \(FB\) are all zero. Because \(C(0,1)=0\) and \(FB(0,1)=0\), this failure persists at **all** future delays. Repreparing before every read would likewise repeat an epoch-zero report, rather than create chronology.
* **Critical symmetry:** \(f(x)=4x(1-x),q=f\). Originals \(1/4,3/4\) have equal first report and merge to \(3/4\); all future reports agree. Since \(f'(x)=4-8x\), the chain rule makes the first derivative of every delay coordinate \(f^{j+1}\) vanish at \(1/2\). Identity readout at the original epoch would separate the pair. Neither noninvertibility nor the critical point satisfies Takens' diffeomorphism premise.
* **Clock alias:** quarter-turn dynamics have full two-delay rank; sampling every fourth update yields \(I_2\), hiding \((0,1),(0,-1)\) forever.
* **Original versus current:** \(F=0,C=e_0^T\) loses original coordinate two forever but the complete current state after one update is known to be zero.

Exact rank does not establish stability. For \(O_2=\bigl[\begin{smallmatrix}1&0\\1&\epsilon\end{smallmatrix}\bigr]\), \(\epsilon=10^{-6}\), rank is two but infinity-norm condition number is \(2{,}000{,}002\); report noise radius \(\epsilon/2\) permits overlapping records for originals differing by one hidden unit. A separately labeled floating demonstration at \(10^{-18}\) rounds distinct exact outputs together.

## 7. Verdict

**SURVIVES — PROVED LOCAL:** fiber constancy, row-space reconstruction and the sharp finite-dimensional bound, with proofs above. **CLASSICAL:** generic smooth embedding under Takens' stated hypotheses. **TESTED MODEL:** exact rational positive/negative controls and twelve seeded fresh matrices, whose elimination ranks match independent Leibniz-minor enumeration. **REFUTED:** delay accumulation guarantees original-source recovery for every sensor/update/clock. Universal physical reconstruction is **BLOCKED** by absent instrument authentication and admissibility evidence, not by a claimed metaphysical impossibility.

## 8. Remaining obstruction

\(\kappa\): simulated lawful encounters only. \(\phi\): explicit kernel aliases survive all delays in this toolkit. \(\sigma\): source tags and valid replay do not authenticate the generating device. \(\rho\): no commitment to a hidden ontology follows from a successful decoder. Predictive equivalence is used without phases or truth probabilities. Next falsifier: independently derive the actual readout backaction and sampling clock, then challenge the asserted \(F,C\) law on withheld original-source states; one mismatch breaks the reconstruction contract. Independent crucible review remains required.

## 9. Cross-domain connection with actual maps

When \(O_k\) has full column rank, choose \(L\) with \(LO_k=I\). Then \(L|_{O_k(K^n)}\) is the actual inverse of \(D_k\), and \(\widetilde F=O_kFL\) on that image satisfies \(D_kF=\widetilde FD_k\). Thus the source dynamics and delay-image dynamics are conjugate; invertible \(F\) additionally gives inverse dynamics. The probe uses \(F=\bigl[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr]\), \(L=\bigl[\begin{smallmatrix}1&0\\-1&1\end{smallmatrix}\bigr]\), \(\widetilde F=\bigl[\begin{smallmatrix}0&1\\-1&2\end{smallmatrix}\bigr]\), verifying both inverse identities and the commuting equation. Rank-deficient observations yield only a quotient when their kernel is \(F\)-invariant; the counterexamples preserve that distinction.

## 10. Deliverables

New independent probe: `scripts/swm_d32_delay_probe.py`. Exact receipt: `D32_DELAY_RECEIPT.json`; audit trail: `D32_COMMANDS.md`. Immutable SUCC parent: `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. Imported founding provenance: FuckingRH `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; original engine blob `db1a9f7205f249dfb90cd60b422c6f3569c6b821`, namespaced engine blob `181019ed0d9c8a62e63c5d871406a1a40220f912`; frozen foundations blob `04408ed96bd369b5063868eb5ad5664824d18043`. Both exact source originals were inspected locally and matched the manifest. No imported, shared, production or historical-default file changes; no full suite, compiler, push, merge or licensing claim.
