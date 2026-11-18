# Proof-Direction Oracle — Crossing Observer Knowledge Volumes Without Importing the Answer

**Principia Observatoris / SUCC / original zero-seeded BBP**  
**Date:** 2026-11-17  
**Originating proposal (Leah):** subjective and objective observers constructively concern the same source object but have different accessible proof paths. Add an authenticated shared communication channel under which the higher-capability/objective observer acts as a **probe-direction oracle**: it supplies a direction, transport and checkable evidence so that the finite subjective observer can discover and verify a proof using its own operations. An observational “noise wall” motivates lifting one level of the observable algebra or proof representation, metaphorically one Dirac-delta knowledge plane above.

**Verdict:** PDO-01–05 are exact elementary/classical theorems with stated source classes; PDO-06 is a conditional R0 certificate contract, **NOT a new lower bound**; PDO-07 is the open zero-seed proof obligation. No actual omniscient objective witness, new arithmetic estimate, physical causal oracle, spacetime identification or proof of π-normality is claimed.

## 1. The three things a direction oracle must distinguish

Fix a **declared source class** \(\Omega\), actual source \(\omega\), target \(G:\Omega\to\{0,1\}\), initial subjective evidence \(E_0:\Omega\to\mathcal Z_0\), and admissible probes \(q\in\mathcal Q\) with readouts \(O_q(\omega)\). The objective adviser is a distinct **capability role**, not a contradictory world.

An advice event is a typed record
\[
\boxed{
\mathsf{Advice}=(\tau,\text{source/frame passport},q,\text{claimed response or lemma},
 \text{calibration/transport},\pi,\text{cost}).
}\tag{PDO1}
\]
Here \(\pi\) is a certificate checkable by the subjective observer using **declared trustworthy source rules**. A proposed response is **not** accepted as observed just because the adviser supplies it. A claimed universal lemma is not accepted because the adviser asserts it; the certificate must actually derive it in the chosen sound calculus.

There are TWO different knowledge-plane lifts:

1. **Discrimination lift:** an additional lawful response \(O_q\) splits some source fiber of \(E_0\). Evidence is \(E_1=(E_0,O_q)\).
2. **Computational/proof lift:** the adviser supplies a new *derivation*, representation, invariant or search heuristic expressible from the same authenticated data. No new Shannon or set-theoretic information enters, but a finite proof may become accessible at drastically lower resource cost.

The second phenomenon is the best literal reading of “move up one knowledge-volume layer to see a proof path,” independent of whether the higher layer adds an actual physical measurement. A Dirac distribution itself does not define the separation between layers.

## 2. Evidence factorization and the oracle-cheating no-go

**PDO-01 (CLASSICAL / PROVED PAPER).** Let \(\omega,\omega'\in\Omega\) have \(E_0(\omega)=E_0(\omega')\) but \(G(\omega)\ne G(\omega')\). If an oracle's chosen probe direction is a deterministic function of the current transcript and all accessible responses to those chosen probes are identical on \(\omega,\omega'\), then no finite adaptive protocol with that oracle can identify \(G\) on both.

**Proof.** The initial transcripts agree. Inductively identical past transcripts yield the same advice/query; the premise supplies the same next readout and verified metadata. Thus the full finite transcripts agree. A single decoder cannot return two distinct correct labels. This is SUCC's existing Principia target-factorization theorem [PO-K1](../../../docs/principia_observatoris/03_knowledge_proof.md), extended to adaptive transcripts. \(\square\)

An adviser **can** distinguish hidden states if its own source-sensitive communication content is available and authenticated, or if it directs a previously unavailable intervention that returns different results. That extra content must be accounted for as additional information; hiding the answer bit in the *choice of direction* is not an independent proof. Conversely, a clever source-equivalent rewrite may reduce computational cost without changing any evidence fiber.

**PDO-02 (SOURCE-VERIFICATION GATE).** A checkable proof-carrying hint can be accepted without trusting its producer, provided a verifier checks the actual derivation against the authenticated source axioms, and the proof system is sound. Its computational usefulness or existence for the desired theorem is not automatically guaranteed. This is a standard producer/verifier distinction, not a theorem that all true mathematical statements have short certificates.

Nearby established protocols include Angluin's membership/equivalence-query teacher (1987), counterexample-guided abstraction refinement (Clarke–Grumberg–Jha–Lu–Veith, CAV 2000) and Necula's proof-carrying-code producer/checker (POPL 1997). The present proposal is an observer-theoretic *adaptation of proof-search architecture*, not a priority claim. Their idealized equivalence teachers may answer global queries that our BBP adviser has **not** been shown able to answer.

## 3. An especially sharp finite-evidence obstruction: opposite R0 inside EVERY cylinder

Let \(m\ge1\) and \(0\le A<16^m\) be an arbitrary integer encoding an \(m\)-digit hexadecimal prefix. Define TWO explicit rational endpoints:
\[
\boxed{x_{\rm lock}=\frac{A}{16^m},\qquad
x_{\rm escape}=\frac{A+1/15}{16^m}.}\tag{PDO2}
\]
They both have exactly that same \(m\)-digit prefix:
\[
\lfloor16^m x_{\rm lock}\rfloor
=\lfloor16^m x_{\rm escape}\rfloor=A.
\]
For **every** \(n\ge m\):
\[
\boxed{
\{16^n x_{\rm lock}\}=0,\qquad
\{16^n x_{\rm escape}\}=1/15
}\tag{PDO3}
\]
because \(16^k\equiv1\bmod15\).

**PDO-03 (PROVED PAPER):** in *every* finite base-16 digit cylinder the R0 predicate takes both truth values. The locked endpoint has \(1-\Re W_B=0\) for all \(B\ge m\). The nonunit fixed endpoint satisfies \(1-\Re W_B=1-\cos(2\pi/15)>0\) for every \(B\ge m\). This is stronger as an information-theoretic statement than the earlier no-exact-repeat shadow: the predicate actually targeted by R0 is not constant on ANY finite digit-prefix fiber.

Their phase discrepancy on any fixed earlier clock \(n\le H<m\) satisfies the explicit bound
\[
\boxed{|e(16^n x_{\rm lock})-e(16^n x_{\rm escape})|
\le\frac{2\pi\,16^{H-m}}{15}.}\tag{PDO4}
\]
Arbitrarily precise finite-horizon shadowing is therefore possible.

These two endpoints are **not** claimed to have the literal four-pole BBP forcing and original zero seed. That authenticated source passport is the essential extra information the objective adviser must leverage.

## 4. The objective oracle's rational, locally checkable BBP directions

Retain exactly the authenticated source
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
The imported BBP identity gives \(x=\pi/16\). For each integer shell \(B\ge1\), compute **one rational endpoint**
\[
U_{2B}=\sum_{j=1}^{2B}16^{2B-j}r(j).
\]
Its backward probe energies are
\[
d_{B,k}=\left\|\frac{U_{2B}}{16^k}\right\|_{\mathbb T}\in[0,1/2],
\quad
\boxed{\mathcal R_B=\frac1B\sum_{k=1}^{B}d_{B,k}^2.}\tag{PDO5}
\]
Our prior [Endpoint Coercivity Report](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md) proved
\(\liminf_{B\to\infty}\mathcal R_B>0\iff\mathrm{R0}\). This is an equivalent source-specific target, NOT an achieved asymptotic bound.

The objective direction oracle may hand the subjective observer a finite certificate
\[
\boxed{\mathsf{Cert}_B=(B,U_{2B},\epsilon,\theta,S_B),\quad
 S_B\subseteq\{1,\ldots,B\},\quad
 |S_B|\ge\theta B,\quad
 d_{B,k}\ge\epsilon\ (\forall k\in S_B).}\tag{PDO6}
\]
The subjective checker *recomputes* the literal zero-seeded \(U_{2B}\) and checks every inequality using **exact rational arithmetic**. It rejects forged terminal endpoints, repeated indices, out-of-range directions and missing thresholds.

Each accepted certificate proves only
\[
\boxed{\mathcal R_B\ge\epsilon^2\theta.}\tag{PDO7}
\]
This makes the oracle a **direction oracle**, not an oracle that states the truth of the unproved theorem.

### PDO-04 — uniform positive witness density is exactly the missing R0 norm gate

For arbitrary numbers \(d_{B,k}\in[0,1/2]\), the following are equivalent:

(A) \(\exists\delta>0,B_0\) such that \(\mathcal R_B\ge\delta\) for every integer \(B\ge B_0\).

(B) \(\exists\epsilon,\theta>0,B_0\) such that for every \(B\ge B_0\),
\[
\boxed{
\#\{1\le k\le B:d_{B,k}\ge\epsilon\}\ge\theta B.
}\tag{PDO8}
\]

**Proof.** B implies A with \(\delta=\epsilon^2\theta\). Conversely choose \(0<\epsilon<\min(1/2,\sqrt\delta)\). If \(p_B\) is the proportion of indices above the threshold, then
\[
\delta\le\mathcal R_B
\le(1-p_B)\epsilon^2+p_B/4,
\]
whence
\[
\boxed{p_B\ge\frac{\delta-\epsilon^2}{1/4-\epsilon^2}>0.}
\]
The constants may be chosen rationally. \(\square\)

**Status:** this is an exact bounded-moment/threshold equivalence, not a new BBP arithmetic estimate. Its operational value is that it asks the proof-direction oracle for a **family of locally verifiable source-selected witnesses** rather than an opaque claim about a complex Weyl average.

Finite evidence alone is insufficient: one separated direction per shell, even at maximal \(d=1/2\), gives only \(\mathcal R_B\ge1/(4B)\to0\).

### PDO-05 — an infinitary oracle transcript is NOT a finite proof

An adviser that successfully delivers \(\mathsf{Cert}_B\) for one B, or even for thousands of B, has supplied *finite verified facts*. Merely imagining that it will supply a certificate for every B is an unproved universal claim.

A **winning proof-carrying oracle** must instead propose a **finite uniform proof** of a source-specific rule such as:
\[
\exists\epsilon,\theta>0,B_0\ \forall B\ge B_0\quad
\mathrm{VerifyBBP}(\mathsf{Cert}_B)=\mathrm{true},
\]
with an effective constructor for \(\mathsf{Cert}_B\) and a proven invariant/termination contract. The subjective verifier checks the global argument. A finite program without a proof that its claims hold for all B does not close the quantifier.

This is where the appropriate source/carry/cofactor invariant would have to appear. The advice itself may nominate a hypothesis, but it cannot supply its conclusion by smuggling π-normality into the hypothesis.

## 5. The exact proposed proof path through the knowledge volume

1. **Layer 0 — Finite cylinder:** inspect finite hexadecimal phases. PDO-03 shows the R0 label is never identified here alone.
2. **Layer 1 — Authenticate the source:** include the literal four BBP poles, \(U_0=0\), positive completed tail and integer winding. Exclude terminating-rational and changed-seed shadows without assuming what is to be proved.
3. **Layer 2 — Change the representation:** the objective oracle points to backward directions \(k\) from the exact terminal rational \(U_{2B}\). The subjective verifier checks the proposed rational witness set.
4. **Layer 3 — Derive a uniform carry/cofactor constraint:** invent a *finite invariant/inductive proof* that the actual zero-selected recurrence cannot place almost all backward positions in a small near-zero torus neighborhood on any late shell.
5. **Layer 4 — Transport the proved inequality:** verify the exact source-tail and phase comparisons, obtaining the R0 margin. To prove *full normality*, perform the corresponding source-valid all-mode Fourier work—R0 is only one rung.

The **minimal missing lamp** is Layer 3. The earlier sparse cold-shell cover theorem with Hausdorff dimension \(1/2\), the seed-blind forcing controls and the exact source tail are already in the PR; repeating them with new metaphors will not manufacture the excluded-source invariant.

## 6. Hostile controls and claim ledger

- The **same** finite prefix has a locked and R0-satisfying endpoint (PDO-03). This directly falsifies observation-only claims.
- A source-blind adviser whose choice and response factor through the old evidence cannot distinguish them (PDO-01).
- A new phase measurement can split one selected pair, but a different finite pair can still shadow the enlarged horizon. One new response is not a universal R0 proof.
- Altering the initial seed changes \(U_{2B}\) by \(16^{2B}s\); a certificate that does not recompute the original zero-seeded terminal rational state is not source-authenticated.
- A true signed-source witness at a single k contributes at most \(1/(4B)\) to R_B. **Positive witness density** or an equivalent uniform global invariant is essential.
- Oracle advice based on a true target label is an **information leak**, not a verified proof. An oracle whose proof checker cannot justify an invariant is an **unpaid theorem**, no matter how impressive the finite checks.
- The coherent locked counterseed \(s=-\pi/16\), finite dyadic winding-erasure controls, impulse/seed causal-history alias and sparse irrational nonnormal source remain mandatory.

| Claim | Status | Verdict |
|---|---|---|
| PDO-01 | CLASSICAL / PROVED PAPER | A source-blind direction oracle cannot split a genuinely indistinguishable evidence fiber without a new differing response |
| PDO-02 | CLASSICAL CONDITIONAL | A checked finite derivation is sound under a verified source and sound calculus, not necessarily short or guaranteed to exist |
| PDO-03 | PROVED PAPER | Every finite hexadecimal cylinder contains opposite R0 outcomes |
| PDO-04 | CLASSICAL / PROVED PAPER | Uniform positive rational terminal energy iff uniform density of threshold-separated directions |
| PDO-05 | PROVED LOGICAL BOUNDARY | Arbitrarily many finite verified shells do not replace the quantified all-B proof |
| PDO-06 | OBSERVED FINITE EXACT | Concrete original-source per-shell proof-direction certificates can be verified by independent Fraction code |
| PDO-07 | OPEN | Construct a uniform original-zero BBP cofactor/carry witness generator with a proof of all-late-shell positive density |

**Reproducibility:** [tests/test_proof_direction_oracle.py](../../../tests/test_proof_direction_oracle.py) contains the exact finite checker, cylinder pair, source-authenticated rational witness and forged-source mutants. [Local execution receipt](PROOF_DIRECTION_ORACLE_VALIDATION.md) records the executed tests and the limits of the validation.

**Provenance:** [Principia knowledge/factorization PO-K1](../../../docs/principia_observatoris/03_knowledge_proof.md), [Contextual Zero](../../../docs/CONTEXTUAL_ZERO_BACKBONE.md), [Prior finite/infinite observer theorem](FINITE_OBSERVER_INFINITE_CERTIFICATE.md), [Endpoint coercivity](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), [Cold-shell exceptional set](../../2026-11-16/defect_window_tomography/COLD_SHELL_EXCEPTIONAL_SET.md), [Seed resonance](SEED_RESONANCE_AND_NULL_SUPPORT.md). These share source premises and do not count as independent witnesses.

**External methodological antecedents:** Dana Angluin, *Learning Regular Sets from Queries and Counterexamples*, Information and Computation 75 (1987), https://doi.org/10.1016/0890-5401(87)90052-6; Clarke et al., *Counterexample-Guided Abstraction Refinement*, CAV 2000, https://doi.org/10.1007/10722167_15; George Necula, *Proof-Carrying Code*, POPL 1997, https://doi.org/10.1145/263699.263712. These are related **methodologies**, not completed solutions to the BBP arithmetic problem.
