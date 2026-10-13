# D31 — Covariant reports and finite causal access

## 1. Original question

Can lawful observer-frame transport preserve source knowledge while respecting finite receipt horizons? The faithful reading is conditional covariance of the **same** experiment, observer and records. It does not identify semantic momentum with physical velocity. The rival extension says that covariance makes every transported mathematical probe available to every finite observer; the crucible below refutes that extension.

Baseline: clean `research/swm-d31-2026-10-13`, immutable parent `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. This first-generation bearing read no sibling conclusions and changes only D31 artifacts.

## 2. Existing mathematical context

**CLASSICAL:** Einstein's [1905 paper, §§1–3 and 6](https://www.fourmilab.ch/etexts/einstein/specrel/www/) treats synchronization, Lorentz coordinates and electromagnetic component transport. The [original publication](https://onlinelibrary.wiley.com/doi/10.1002/andp.19053221004) fixes historical attribution. Lamport's [1978 paper, pp.559–560](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) distinguishes actual message ancestry from merely possible causal influence and clock ordering.

Native antecedents are CV1/CV4/CV7/CV8 in `COVARIANT_PERCEPTUAL_MOMENTUM_AND_CAUSAL_DESCENT.md`, with first native commit `82f518cda67c9f80054a0b973a5c12bbd248a309`; Galilean/shadow origins are `f44bb04b1d8f542b4ebb402ee93d3d534a5d66fe`. Later honesty corrections remain authoritative. The frozen foundations dossier was checked against originating commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`: remote bytes equal the archive, Git blob `04408ed96bd369b5063868eb5ad5664824d18043`. These are one repository lineage, not independent empirical witnesses.

## 3. Proposed SUCC objects

Declare \(M=\mathbb R^{1+2}\), coordinates \((ct,x,y)\), signature \(\eta=\operatorname{diag}(1,-1,-1)\), and positive constant \(c\); below set \(c=1\). Future means \(t\ge0\). Write \(a\preceq b\) when \(b-a\) is future causal. An inertial observer is \(\gamma(\tau)=p+\tau u\), \(u^T\eta u=1,u_0>0\), sampled at finitely many fixed proper times \(\tau_k\).

For preparation \(p=\gamma(0)\), define \(D_k=J^+(p)\cap J^-(\gamma(\tau_k))\). The protocol permits new acquisitions only there; earlier retained records require separate declaration. A finite event DAG carries actual parent edges satisfying strict causal order. Acquired receipts require an actual path to the sample anchor, lawful instruments and invariant integer costs totaling at most \(B_k\). Diamond membership alone is insufficient.

Let \(S\) be a declared source class. For the stochastic theorem, the report alphabet is finite or countable and every conditional row is normalized. \(U_L:S\to S_L\), probe map \(T_L:Q\to Q_L\), and report bijection \(R_L:Y\to Y_L\) are reversible **representation** maps, with identity/composition laws. For a full action/report history \(h=((q_i,y_i))_{i=1}^n\), define \(\mathsf H_Lh=((T_Lq_i,R_Ly_i))_{i=1}^n\), transporting retained event/source/basis metadata by their declared maps. This transporter preserves prefixes, identities and composition. For every source, finite history \(h\), lawful probe \(q\), and symbol \(y\), require conditional-kernel covariance

\[
K^L_{U_Ls}(R_Ly\mid \mathsf H_Lh,T_Lq)=K_s(y\mid h,q). \tag{1}
\]

This includes deterministic reports as Dirac kernels; it assumes no independent noise. Require \(\pi_L(\mathsf H_Lh,\tau,B)=T_L\pi(h,\tau,B)\), matching feasibility predicates, and cost \(w_L(T_Lq,\mathsf H_Lh)=w(q,h)\). Equation (1) is a checked premise, not a consequence of source tags.

## 4. Candidate theorem

**D31.1 — CLASSICAL / PROVED LOCAL.** For every proper future-oriented \(L\), \(L^T\eta L=\eta\), \(\det L=1,L_{00}\ge1\), causal order and every \(D_k\) transport exactly: \(L(D_k)=D(Lp,L\gamma(\tau_k))\). Actual DAG ancestry remains the same event-ID set.

**D31.2 — PROVED LOCAL, conditional.** For every finite protocol with finite/countable discrete reports and normalized conditional rows satisfying (1), transported policy/feasibility/costs and the same proper-time samples, transcript laws obey \(P^L_{U_Ls}(\mathsf H_Lh)=P_s(h)\). For a target \(t_LU_L=t\) and transcript with nonempty compatible-source set \(\{s:P_s(h)>0\}\), exact inference survives iff \(t\) is constant on that set. This is source-relative inference, not authentication of spacetime or instruments.

## 5. Proof attempt

Metric preservation gives \((Lz)^2=z^2\). If the first row is \((a,b_1,b_2)\), the Lorentz identities give \(a^2-|b|^2=1,a\ge1\). For future causal \(z\),

\[
(Lz)_0\ge(a-|b|)z_0\ge0.
\]

The inverse has the same property, proving the causal-order equivalence and diamond equality. Actual edges are transported individually; their transitive closure cannot acquire a new edge. Proper-time length is invariant.

Induct on transcript length. Covariant policy chooses \(T_Lq\); matching costs preserve the remaining budget. Equation (1) makes the next conditional factors equal. Multiplying these factors proves transcript covariance without a stochastic-independence assumption. Source/report bijections identify compatible-source sets; \(t_LU_L=t\) preserves target constancy. Conversely two compatible sources with differing targets prohibit an exact decoder. No infinite elapsed computation enters either proof.

## 6. Crucible

The Fraction probe preserves these distinct receipts:

* **Outside cone:** \(e=(0,2,0)\) cannot signal to \(o=(1,0,0)\); separation squared is \(-3\). An earlier coordinate time supplies no receipt.
* **Changed observer:** from \(p=0\), stationary \(o=(4,0,0)\) and moving \(o'=(5,3,0)\) both have proper duration \(4\). Event \(e=(2,-2,0)\) is in the first diamond, outside the second: \(e\to o\) is null, \((o'-e)^2=-16\).
* **Unsent event:** an event inside the diamond but absent from anchor ancestry is excluded. Geometry grants possibility, not delivery.
* **Erased preparation:** initial bit \(s\in\{0,1\}\), erasure \(U(s)=0\), report \(O'(0)=0\), and constant \(R\) make \(O'U=RO\) commute. Original target \(t(s)=s\) has no decoder. This mutation violates reversibility.
* **Simultaneity/order:** \(a=(0,-1,0),b=(0,1,0)\) are simultaneous; the \(3/5\) boost gives times \(3/4,-3/4\). Neither becomes causally available at the origin.
* **Incomplete components:** constant transverse Maxwell sources \((E_y,B_z)=(0,0),(0,1)\) have identical E-only reports. The correct boost gives \(E'_y=\frac54E_y-\frac34B_z\), hence \(0,-3/4\). No E-only transport exists.
* **Galilean mutation:** \(G(t,x,y)=(t,x-3t/5,y)\) sends future null \((1,-1,0)\) to a spacelike vector, squared \(-39/25\). Galilean mechanics has a different covariance contract.
* **Clock mutation:** the same endpoint \((5,3,0)\) is excluded by \(t\le4\), included by \(t'\le4\). Reusing a numerical coordinate-time cutoff changes the protocol. Metric-preserving time reversal also fails the future-orientation gate.

**Continuous-alphabet refutation (independent review).** Uniform measure on (0,1) and density 2y give every singleton mass zero, yet their probabilities of (0,1/2) are 1/2 and 1/4. Thus singleton-kernel covariance alone does not identify continuous transcript laws. The repaired discrete theorem survives; a measurable-kernel pushforward theorem on every measurable set is a separate next gate. The positive-point-probability inference criterion is discrete as well.

## 7. Verdict

**SURVIVES:** D31.1 and conditional D31.2, with written universal proofs; bounded exact cases are **TESTED MODEL**, not independent formal certification. The noisy-kernel fixture calibrates finite symbol relabeling; it does not derive a Lorentz law for physical noise. **REFUTED:** covariance alone implies access, original-bit recovery after erasure, or transport of incomplete components. The explicit source pairs/events above are the refutation receipts. The proposed extension fails while its reversible, domain-aware core survives.

## 8. Remaining obstruction

Actual physical source correctness remains **BLOCKED** here: no authenticated apparatus/contact was supplied. \(\kappa\) is simulator contact; \(\phi\) concerns this declared toolkit; \(\sigma\) is independently unverified physical sourcing; \(\rho\) is project commitment, never evidential weight. A rate such as eight receipts per four proper-time units equals \(2\), while per five coordinate-time units it equals \(8/5\); neither establishes a cognition law. Resource rules are premises, not derived hardware limits.

## 9. Cross-domain connection with actual maps

For deterministic full reports \(O_Q:S\to Y^Q\), define \((R_L^Qf)(T_Lq)=R_L(f(q))\), denoting \(T_LQ\) by \(LQ\). Covariance is \(O^L_{LQ}U_L=R_L^QO_Q\), equivalently the conjugacy \(O^L_{LQ}=R_L^QO_QU_L^{-1}\). If accessible \(A\subseteq Q\) transports to \(LA\), restrictions satisfy

\[
\mathrm{res}_{LA}R_L^Q=R_L^A\mathrm{res}_A.
\]

This is an actual naturality square, alongside the event-poset isomorphism \(P\to LP\) and its map on downsets. Restricting to a smaller physically accessible domain need not be invertible; the changed-observer witness exhibits the missing coordinate. Its full diamonds are not asserted to be nested. Classical restriction/factorization therefore explains both report covariance and its access boundary. No phasor or physical quantum interpretation is needed.

## 10. Deliverables

This is a project-local formulation without an academic-priority claim.

`D31_covariant_causal_probe.py` is standalone, standard-library and rational; `D31_RECEIPT.json` records bounded positive checks, negative witnesses, provenance, hashes, commands and exits. No native module, frozen archive, shared ledger or default changed; no full suite/compiler/push ran. **Next small lemma:** prove finite protocol covariance for prefix-dependent kernels and a covariant stopping rule in an independent formal checker, first attempting a counterexample where a coordinate-time stopping rule changes the sampled events.
