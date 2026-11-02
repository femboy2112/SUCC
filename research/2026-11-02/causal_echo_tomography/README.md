# Operation CAUSAL ECHO TOMOGRAPHY — finite local history versus normality

**Draft-only, stacked on exact SUCC #466 head c71b18dba200c2d227d9c084bbb9d8399f81ede3; #466 itself follows #464/#463/#462/#460/#459 and merged Main XIX.** All new files confined to this research directory plus one additive root-discoverable test. Do NOT modify original four signed BBP poles, literal U0=0, historical claim ledgers, production, formal or main. **No π normality, RH, or all-horizon signed saving has been proved.**

## What the new connection actually proves

In SUCC's positive Hausdorff source class, **every finite exact local observation history has a large invisible causal subspace**. For any M, an explicit compact-support signed source-density derivative ψ_M has its first M moments EXACTLY zero but a nonzero response under the completed boundary integral. Add a sufficiently tiny multiple to the original four-pole BBP source. Then:

- The first M exact original source values and zero-seeded rational states are **identical**.
- The changed source stays **strictly positive and completely monotone at ALL times and differential orders**; ALL positive unit/analytic differential jets stay between 95%-105% of the original.
- The correction is **entire in complex source time**, exponentially small at positive integers, so it changes neither the original source's meromorphic poles nor any inverse-power asymptotic coefficient.
- Yet its completed α changes. Choosing the perturbation strength appropriately, two admissible controls have **a known base16-normal** versus **a rational, nonnormal** completed point, despite identical first M exact observations. Their source values may be irrational when tuned to these two target α's; they do NOT remain the literal four-pole rational function.

A **separate strictly rational** source countermodel exists at EVERY finite M: positive rational atomic moments match r(1),...,r(M) exactly, all future r'(n) are rational and completely monotone, and the completed constant is RATIONAL. This has an explicit 4-moment certificate. It does NOT preserve the original rational four-pole meromorphic source class nor the uniform 95%-jet-density comparison of the first control.

## The quantitative causal echo

For the explicit polynomial bump with M=4 and rational epsilon, the perturbed forcing is rational, positive and 95%-105% controlled at every order. The two exact original/counterfactual orbits match through time 4, yet at time 18 their circle displacement is
\[
\boxed{\frac{260840294718179115804391693}
{837084962009298606489600000}\in(1/4,2/5).}
\]
This is an exact rational finite example of **small, late source echo → macroscopic real-circle phase difference**. There is no claim that this particular rational-ε source is nonnormal; its completed normality is NOT classified.

## Circle/line geometry: the hidden echo is a relative boundary class

The source-echo correction is the ordinary exact one-form
\[
\delta\omega=\epsilon\psi_M(x)/(16-x)\,dx=dF,
\]
but \(F(1)-F(0)=\epsilon\beta_M\ne0\). It is therefore **not endpoint-relative exact**. This explains how identical local pole/asymptotic data can coexist with different global completed periods. It directly complements SUCC #452's ORIGINAL four-pole angular coboundary, whose primitive vanishes at both endpoints. The altered source is a different period, NOT a second value of π.

## General categorical observability criterion — the source-kernel lamp

For ANY finite list of linear source measurements \(L_i(\mu)=\int\phi_i(x)d\mu(x)\) on an interval inside (0,1), the completed boundary \(A(\mu)=\int(16-x)^{-1}d\mu\) is determined by those observations on the full measure class **if and only if** the resolvent weight \(1/(16-x)\) belongs to the linear span of the measured weights \(\phi_i\). Otherwise a smooth, compactly supported source perturbation can annihilate *all* those measurements, preserve positivity with arbitrarily small all-jet relative error, and change the completion.

This includes ANY FINITE set of Pascal/Newton and ordinary analytic source-time derivative moments, whose weights are polynomial/log-power functions with no pole at x=16. It does **not** cover nonlinear observers automatically. It is the explicit weight-kernel incarnation of SUCC #423's exact categorical arrow test, not an academic novelty or a theorem that mathematical proof from a known complete four-pole law is impossible.

## Exact observer-map arrow

For source measure μ define the finite local history \(q_M(\mu)=(\int x^j d\mu)_{j=0}^{M-1}\) and the completed boundary \(A(\mu)=\int d\mu/(16-x)\). Our ψ_M has q_M(ψ_Mdx)=0 but A(ψ_Mdx)≠0. Hence A **does not factor through** q_M, even with all pole/principal-part and all asymptotic observers appended. This explicitly instantiates SUCC #423's categorical fiber/ker inclusion criterion.

When the full exact original rational four-pole source CLASS is imposed, #437/#448's finite Prony fingerprint can identify the forcing; both controls are outside that restricted class. Even knowing that exact source and the literal zero seed, however, does NOT prove the fixed-h signed Weyl estimate.

## New observer-metric resolution bound

For positive source measures of total mass R0=47/15 sharing the first M moments, their completed constants differ by at most
\[
\boxed{2R_0/(15\cdot16^M).}
\]
For our echo perturb with support in [1/4,1/2], this sharpens to
\[
\boxed{2\|\delta\mu\|_{\mathrm{TV}}/(31\cdot32^M).}
\]
The source-to-state Green Jacobian gives a complementary finite *causal influence* bound after the observational horizon. This is source-adequacy mathematics, NOT a normality inequality.

## Reproduction and prior connections

- [PROOFS.md](PROOFS.md) — the full theorem, positive-density construction, rational quadrature proof, quantified horizons, categorical descent and selected normality firewall.
- [CLAIMS.md](CLAIMS.md) — statuses, exact scopes and countermodels.
- [VALIDATION.md](VALIDATION.md) — exact Fraction, independent SymPy and external source qualification.
- [NEXT.md](NEXT.md) — decisive original-source, zero-boundary signed probe.
- [SOURCE_MAP.md](SOURCE_MAP.md) — exact SHA ancestry and inherited #421/#423/#437/#440/#443/#448/#463/#464/#465/#466 work.
- [causal_echo_probe.py](causal_echo_probe.py) — pure stdlib tests and 4-atom rational certificate; [independent_symbolic_oracle.py](independent_symbolic_oracle.py) — independent SymPy algebra; [tests/test_causal_echo_tomography.py](../../../tests/test_causal_echo_tomography.py) — full-suite discovery adapter.

**Observational analogy:** AGN reverberation maps invert retarded light responses; CMB component separation compares models/foregrounds across channels. In SUCC the past causal forcing is collected in \(U_N=\sum16^{N-j}r_j\), but finite causal observations need not identify which full source produced them. The analogies do NOT establish literal physical radiation or quantum collapse in SUCC.
