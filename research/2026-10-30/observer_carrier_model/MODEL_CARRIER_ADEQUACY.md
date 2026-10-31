# SUCC — The Observer Is Embedded in the Carrier, but Its Model Is Not the Carrier

**2026-10-30. DRAFT RESEARCH ONLY.** Stacked on PR #412 (parent `9dce8c27ea1083554daaf0b48df44bcf81081b53`, inherited #409/#406/#404/#402/#397 and merged Main XVI). Purely additive auxiliary research. The original signed BBP four poles, selected `U_0=0`, source contracts, production, workflows, main, and archival sources remain UNCHANGED. Base-16 normality of pi, base-3 normality, RH, and physical-spacetime identification remain OPEN.

## MA-00 — The author's objection

An observer is physically embedded in a carrier, but the *model of that carrier encoded within the observer* is a separate representational object. The observer can run perfectly consistent probability operations whose output is not the actual carrier's selected state distribution. Embedding does not imply the model's operations are isomorphic to the carrier's dynamics. **Strong faithful interpretation:** a proof about an internal model may be transferred to the carrier only through a separately certified observation/abstraction map, not by asserting the observer and carrier are identical.

Three distinct types:
1. **Concrete carrier** `C` with actual dynamics `F` and an observer as one of its physical subsystems. The model is physically instantiated inside `C` but is not identified with `C` as a mathematical state space.
2. **Actual observation/contact** `O_a(C)` obtained from an admissible interaction `a`; the observer's actual internal record is a finite state `m_t` plus any externally retained no-discard ledger `R_t`.
3. **Internal model** `M` with a declared simulator `F_hat`, model probability kernel `K_hat`, and predicted observations `O_hat`. Even if `m_t` literally lives inside C, the semantic model M is not the concrete C.

For a complete closed physical model, the observer's memory and actions must appear in the carrier's joint evolution. A simulator's independent RNG, externally supplied clock, exact real residual, or posterior reset is an additional assumption, not an automatic property of the carrier. A chosen model may nonetheless be a sound *abstraction*: it need only preserve the specific theorem property, not contain all infinite carrier details. This distinction is classical in abstract interpretation (Cousot & Cousot, JLC 1992), dynamical-system factors, and Markov lumpability.

## MA-01 — Elementary property factorization criterion (DISCLOSED)

Let `q:C→M` be any quotient/observation map, and let `P:C→{0,1}` be a carrier property (e.g. `P(c)=` “this infinite orbit is base16 normal”). There exists `P_hat:M→{0,1}` with

\[\boxed{P=\widehat P\circ q}\]

**if and only if P is constant on every nonempty fiber q^-1(m).**

Proof: `P_hat` existing implies equal q images have equal P. Conversely, if P constant per fiber, define `P_hat(m)` to be the common P value of any c in that fiber (arbitrary outside image). No injective/isomorphic carrier copy is needed. A sufficient abstraction is possible only if its observational equivalence does not identify states of opposite target truth values.

**Finite-prefix obstruction:** For every finite hexadecimal word `w`, there is an eventually-zero (nonnormal) infinite continuation of w, and a normal continuation obtained by appending any base16-normal sequence (finite prefix edits preserve normality). Thus a quotient retaining **only finitely many observed digits** has fibers containing both normal and nonnormal carriers. No finite-prefix-only classifier P_hat exists on the unrestricted full shift. This does not prove a finite mathematical theorem based on an *extra structural description* (the original source and selected seed) is impossible; the source narrows the admissible family beyond observed prefixes.

## MA-02 — Exact dynamics/observation closure criterion (DISCLOSED)

Suppose concrete dynamics are `F:C→C`. A deterministic self-contained transition `F_hat:M→M` satisfying

\[\boxed{q(F(c))=\widehat F(q(c))\quad\forall c}\]

exists **if and only if** `q(F(c))` is constant on each `q`-fiber. This is the deterministic analogue of a lumpability/factor-map condition. It need not hold for a coarse observable, even when the carrier itself is deterministic.

For `T(x)=16x mod1`, choose q(x)=floor(16x). The two carrier states `x=0` and `x=1/256` have q=0, yet q(T(0))=0 while q(T(1/256))=1. Therefore **no deterministic next-digit evolution exists on the current single-digit observation alone**. More state, retained history, or a set-valued/stochastic prediction must be supplied. Treating a missing exact transition as if it were known is a source-map adequacy defect; it is not proof that reality itself is stochastic.

## MA-03 — Disintegration exposes the exact hidden model assumption (DISCLOSED)

Let `X=[0,1)` with greedy base16 coding, `T(x)=16x mod1`, digit `D(x)=floor(16x)`, residual `Y=T(x)`, and inverse-branch maps `f_d(y)=(d+y)/16`. Fix ANY Borel `T`-invariant probability μ on X. Disintegrate the actual joint law `(D,Y)_*μ` over the residual y:

\[K_\mu(d\mid y)=\Pr_\mu(D=d\mid Y=y),\qquad \sum_{d=0}^{15}K_\mu(d\mid y)=1.\]

The concrete reconstruction is an **identity for every invariant μ**:

\[\boxed{\mu=\sum_{d=0}^{15}(f_d)_*[K_\mu(d\mid y)\,\mu(dy)].}\tag{MA-3}\]

This formula is the exact no-discard digit-plus-residual factorization in probability-law form; no fair-digit hypothesis appears.

**The last PR #412 model instead declared a NEW kernel**

\[K_{\rm model}(d\mid y)=1/16\quad\text{independent of }y,\]

so its internal simulator is

\[\boxed{\mathcal P\mu=\frac1{16}\sum_d(f_d)_*\mu.}\]

The fair operator is 1/16-contractive in ordinary Wasserstein-1 and has unique fixed point Haar λ. But **actual T-invariance never implies actual conditional branch fairness**. The needed source-to-model bridge is precisely

\[\boxed{K_\mu(d\mid y)=1/16\quad\mu\text{-a.e. for each }d.}\tag{MA-4}\]

This is equivalent to `μ=λ` among invariant measures, and hence would be a NORMALITY-EQUIVALENT property if μ comes from the actual orbit. Proving that the internal model generates Haar is not the proof that the actual carrier has kernel MA-4.

**Hostile exact zero carrier:** μ=δ0 is invariant under T but has Kμ(d|0)=1_{d=0}. Under the fair internal model, Pδ0 is the uniform mixture of sixteen atoms `{d/16}`. In ordinary interval W1,

\[\boxed{W_1(\delta_0,\mathcal P\delta_0)=15/32.}\]

Iterating the model itself gives P^kδ0=16^-k Σ_(j=0)^(16^k-1) δ_(j/16^k) and W1(P^kδ0,λ)=1/(2·16^k). The **model distribution converges to Haar as k grows while the carrier remains δ0**. This is a fully calibrated constructive refutation of an internal-model-to-carrier inference.

Also μ=(δ_(1/17)+δ_(16/17))/2 is T-invariant and periodic, with deterministic backward branch kernel and entropy rate zero. A full-support *biased Bernoulli* digit measure is T-invariant but has Kμ(d|y)=p_d≠1/16; full topological support alone does not force model adequacy.

## MA-04 — Information-theoretic size of the source-map defect (CLASSICAL identity, specialized)

For ANY invariant μ define the actual fair-branch information deficiency

\[\boxed{\mathfrak D(\mu)=\int D_{KL}(K_\mu(\cdot\mid y)\Vert u_{16})\,\mu(dy),\quad u_{16}(d)=1/16.}\]

The residual Y contains the entire future digit tail (in greedy coding), so, writing `H_k` for the entropy of the first k digits under stationary μ,

\[H_\mu(D_0\mid Y)=\lim_{k\to\infty}(H_{k+1}-H_k)=h_\mu(T),\]

where h is the usual Kolmogorov–Sinai entropy rate of the radix map. Thus

\[\boxed{\mathfrak D(\mu)=\log16-h_\mu(T).}\tag{MA-5}\]

In particular D=0 iff the conditional kernel is fair iff μ is Haar. The carrier may be generated by a short computable rule while its **invariant occupation law**, if normal, has entropy log16: algorithm-description complexity of the constant and measure-theoretic entropy of its orbit statistics are different quantities.

There is also a useful **quantitative conditional** consequence: for every k, entropy subadditivity and Pinsker imply

\[\boxed{\mathrm{TV}(\mu_k,u_{16}^{\otimes k})\le\sqrt{\frac{k\,\mathfrak D(\mu)}2}.}\tag{MA-6}\]

Additionally, pushing the actual and model digit/residual joint laws through the same deterministic inverse-branch map gives

\[\boxed{W_1(\mu,\mathcal P\mu)\le\sqrt{\mathfrak D(\mu)/2}.}\tag{MA-7}\]

No theorem presently bounds D for the selected π carrier. Bounding D by zero—or by a quantity tending to zero for **every empirical weak limit**—would prove normality but is not obtained from the auxiliary Gamma/Oily posterior or the fair model's intrinsic contraction.

**Bernoulli hostile control:** take p0=1/2, p1=...=p15=1/30. Then

\[\mathfrak D=\frac12\log\frac{64}{15}>0,\qquad h=\log16-\frac12\log\frac{64}{15}.\]

This law has full digit support, is invariant, and is not Haar. For coherent δ0, D=log16. The equations are calibration identities about declared invariant measures, not direct π data.

## MA-05 — An important NONCOMMUTING LIMIT: model precision versus observed horizon (DISCLOSED, conditional)

Even assuming α is a *normal* deterministic base16 number, an ideal exact-future conditional entropy computed from a **finite empirical record** can appear maximally nonrandom. Define its finite list of observed pairs `(D_n,Y_n)` for n<N where `Y_n=T(x_n)`, and let `V_{n,k}` be the first k hexadecimal digits of Y_n. Define empirical Shannon conditional entropy H_(N,k)=H_emp(D_n|V_(n,k)).

For any base16-normal α, all its pure radix orbit states Y_n are distinct, since α irrational. For each FIXED N, there exists finite k_N that distinguishes the N observed future states; hence H_(N,k)=0 for k>=k_N. On the other hand, for every FIXED k, normality gives exact limiting joint probabilities 

\[\Pr(D_n=d,V_{n,k}=v)\to16^{-(k+1)},\]

and so H_(N,k)→log16 as N→∞. Therefore two limits genuinely do not commute:

\[\boxed{\lim_{k\to\infty}\lim_{N\to\infty}H_{N,k}=\log16,\qquad \lim_{N\to\infty}\lim_{k\to\infty}H_{N,k}=0.}\tag{MA-8}\]

This is **not** a paradox or an entropy law of physics: conditioning on an infinitely precise future state in a finite deterministic sample assigns a unique index and reveals D, even if the underlying invariant distribution is Haar. Calibrate with exact finite orbit x0=1/257: period 4, empirical H(D|first future digit)=log2 but H(D|first TWO future digits)=0 (the four futures have become uniquely identified). The limiting theorem is conditional on normality of α and does NOT assume pi normal.

**Operational inference:** a finite observer cannot silently exchange the order of its measurement horizon N, precision k, and probability-model limit. Exact-real conditioning on finite atom samples is not the same as disintegration of a limiting Haar law. This is a precise model/carrier interface defect.

## MA-06 — Original BBP source and the missing arithmetic source-to-fairness bridge

Keep the unchanged signed four-pole forcing

\[r_n=R(8n-7),\quad R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad U_0=0.\]

The original Green tail `T_n=Σ_(j>=1)16^-j r_(n+j)` gives an exact conjugacy `V_n=U_n+T_n`, `V_(n+1)=16V_n`, with selected V0=π/16. The original-source summable budget from #409 transfers all empirical weak-limit occupation measures between the selected forced orbit and the pure radix α=π/16 orbit, with explicit W1 O(1/N). Consequently every limiting μ of the selected raw carrier is T-invariant and admits an actual inverse-branch Kμ. **This does not imply Kμ is fair.**

The three positive BBP source atoms, Gamma and Oily–Macaroni virtual laws, symbolic model symmetry, Noether charges, Fibonacci/clock and 3D Fisher coordinates are additional useful mathematical observers, but none is automatically the ACTUAL conditional distribution of selected real-circle previous digits given the realized residual tail. The same four-pole source and a different coherent seed s*=-π/16 produce a nonnormal limit δ0, whose K is deterministically concentrated, so source-only inference cannot bridge MA-4.

**The actual goal is to derive MA-4—or a quantitatively adequate weaker criterion—from the original source, selected boundary, and original integer carry/CRT history, under declared finite observation/precision quantifiers.** Do not presume fair digits because the internal model uses a fair random branch. Prove a source-selected defect estimate for the actual carried observations, falsified by the coherent counterseed, Gaussian/source-matched fakes, and finite-block normal-like but globally nonnormal controls.

## Claims and boundaries

- **DISCLOSED elementary:** model–carrier distinction, factorization-on-fibers iff, deterministic transition closure iff, δ0 model-only false success, exact 1/16 contraction and simple rational carries, finite precision/horizon noncommutation conditional on normal sequence.
- **CLASSICAL specialized:** inverse-branch disintegration, entropy deficit D=log16−h, Pinsker k-cylinder bounds, abstract interpretation and Markov lumpability.
- **DECLARED:** embedded physical observer/coupling and source models; fair inverse-branch simulator as a hypothetical law, not a measured selected arithmetic channel.
- **REFUTED as inference:** T-invariance of selected μ implies fair K; internal model fixed point implies selected π normality; finite exact-future empirical conditional entropy is population entropy; finite digits alone identify normality; exact carry quotient can ignore its integer lift; model symmetries prove carrier symmetries.
- **UNVERIFIED:** original four-pole, zero-seed arithmetic forces D(μ)=0 for each selected empirical limit; π normality, RH or physical self-model identity.

**Next falsifying test:** build a resolution-calibrated empirical digit/residual joint law from the original zero-seed BBP, order horizon→∞ before resolution→∞, and derive an independently sourced UNIFORM-in-resolution upper bound on entropy deficiency or a quantified fair-kernel discrepancy that vanishes for each selected limit. Keep Stoneham normal c=3/5, coherent -π/16, biased full-support Bernoulli, de Bruijn periodic, same-forcing seed shifts, altered-pole/higher-jet-matched controls. No number of visually decreasing finite residuals alone constitutes an asymptotic proof.

**Classical provenance:** Cousot & Cousot, *Abstract Interpretation Frameworks*, JLC 1992 https://doi.org/10.1093/logcom/2.4.511; Kemeny–Snell lumpability criterion (e.g. *Testing lumpability in Markov chains*, SPL 2003 https://doi.org/10.1016/S0167-7152(03)00126-3); standard Rokhlin disintegration, full-shift measure entropy, Pinsker inequality. PR #412 contains the original fair-inverse branch operator and its exact Wasserstein calibration. New-to-SUCC is the explicit fiber/soundness audit and the double-limit blocker, not a new mathematical result about pi.

**Validation scope:** exact stdlib Fraction and separate SymPy/mpmath controls; full SUCC root suite, hosted CI, Lean, independent external referee not run for this additive research.
