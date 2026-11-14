# Principia Observatoris — The Equivariant Choice Trichotomy

**Date:** 2026-11-14. **Research-only, no merge/release/publish authorization.**
**Origin:** Leah's proposal: classify when an observer's lawful `T` action gives a source-faithful point selector, only a stochastic selector, or no normalized stochastic selector; characterize what is lost about actual history. This is a strengthening of [SUCC draft #625](https://github.com/femboy2112/SUCC/pull/625), stacked on its exact parent `926313492a8e2e601943891a31542125f980c484`.

**Scope:** genuine *given* actions on source objects and observable reports. No claim that an arbitrary category canonically supplies a nontrivial `T`-action, that a probability can be read from a mere set of lawful possibilities, that a chosen representative is the actual source, or that set-theoretic AoC has been proved from observer axioms. Every theorem below is a classical mathematical consequence in a declared category of sets/actions (new-to-SUCC synthesis and explicit witnesses); scholarly novelty is **UNVERIFIED**. The exact finite checks and independent algebraic audit have separate authority.

## 0. Definitions and four incompatible notions of choice

Let a monoid \(M\) act on source states \(X\) and reports \(Y\), and let \(q:X\twoheadrightarrow Y\) be a **surjective equivariant map**: \(q(mx)=m q(x)\). For a single endomap \(T\), this is \(qT_X=T_Yq\). A *source fiber* is \(F_y=q^{-1}(y)\). A finite set of specified generators suffices for exact checking.

0. **Set-valued/lax choice:** \(F_y\) is a nonempty set of possible states, with \(mF_y\subseteq F_{my}\). It asserts no single state, no frequencies, and no histories.
1. **Ordinary point section:** \(s:Y\to X\), \(q\circ s=\mathrm{id}_Y\). It chooses one representative (finite sets are constructively enumerable) but may violate dynamics and cannot guarantee \(s(q(x))=x\) for an unknown actual source.
2. **Equivariant deterministic section:** additionally \(s(my)=m s(y)\). It is a consistent point-valued *source-reconstruction convention*, not a certificate that this is the actual hidden source.
3. **Equivariant stochastic lift:** \(K_y\) is a countably additive probability concentrated on \(F_y\), with \(K_{my}=m_*K_y\). It respects the source action probabilistically as a mathematical Markov kernel, but is **not** a measured posterior without a source prior/preparation law. A Dirac-valued \(K_y=\delta_{s(y)}\) is equivalent to an equivariant point section.

The distinctions from observer probes and actual source history are separate. For finite carriers a *normalized but non-equivariant* probability exists on every nonempty fiber, regardless of which of (2–3) fails. Thus "no stochastic description" below means **no normalized T-compatible stochastic lift**, never "no mathematical distribution can be written."

The classical set-theoretic **Axiom of Choice** says every surjection in **Set** splits; SUCC's stronger observer-relative AoC seeks a *lawful executable* distinction. Neither AC nor a bare category supplies equivariance, computability, physical observations, or a posterior. An alternative SUCC expansion of AOC as *Adaptive Observer Closure* is a different concept and must not be conflated with this choice problem.

## EC-01 — The canonical lax section always exists (PROVED ELEMENTARY)

For every surjective equivariant \(q\), the full-fiber relation \(F:Y\to\mathcal P(X)\), \(F(y)=q^{-1}(y)\), satisfies

\[
 q_*F(y)=\{y\},\qquad m_* F(y)\subseteq F(my).
\]

**Proof.** Fibers are nonempty by surjectivity. If \(x\in F_y\), then \(q(mx)=m q(x)=my\), so \(mx\in F_{my}\). \(\square\)

The inclusion can be strict. This is the **lax relational fallback**, not a section in the category of equivariant set-valued maps with equality in both directions. Strengthening inclusion to equality requires every element of \(F_{my}\) to have a source predecessor in \(F_y\). The chosen source start and time index must additionally be retained when not every state in a mathematical fiber is reachable.

## EC-02 — Group-equivariant deterministic section: exact stabilizer criterion (PROVED)

Let \(G\) be a group acting on \(X,Y\), and \(q\) an equivariant surjection. For every selected representative \(y\) of a \(G\)-orbit in \(Y\), put \(G_y=\{g:gy=y\}\).

**Theorem.** If \(Y\) is finite (or orbit representatives may be selected by an explicitly assumed AC), there is a \(G\)-equivariant point section **iff every** fiber \(F_y\) above an orbit representative contains an element fixed by *all* \(G_y\).

**Proof.** If \(s\) is equivariant and \(h\in G_y\), then \(hs(y)=s(hy)=s(y)\). Conversely choose a fixed \(x_y\in F_y\), and define \(s(gy)=gx_y\). If \(gy=g'y\), then \(g'^{-1}g\in G_y\), so the two definitions agree. Fiber membership and equivariance follow. \(\square\)

**Negative control:** \(G=C_2\) swaps \(X=\{a,b\}\) while acting trivially on \(Y=\{*\}\). Ordinary sections exist, but the stabilizer \(G_*=G\) fixes neither source state. No equivariant point section. **Positive control:** a two-element quotient orbit with trivial stabilizer can admit a point section even if the action is nontrivial; our exact test constructs one. The nontrivial-quotient 4-cycle counterexample has \(G\cong C_4\), \(|Y|=2\), and stabilizer of size 2 swapping each two-point fiber; no point section.

Special case \(Y=X/G\) with the trivial quotient action: an equivariant point section exists **iff every orbit is a singleton** (under AC for infinitely many orbits). This is a restriction on *equivariant* choice, not a refutation of set-theoretic AC.

## EC-03 — Group-equivariant stochastic section: exact stabilizer criterion (PROVED)

For the same \(G,q\), an equivariant probability-valued lift exists **iff**, for every chosen representative \(y\), the stabilizer \(G_y\) admits an invariant countably additive probability \(\mu_y\) supported on \(F_y\). For finite \(Y\), no global choice is required; with arbitrary \(Y\), selecting measures across infinitely many orbits is an additional choice premise.

**Proof.** An equivariant \(K\) gives \(h_*K_y=K_{hy}=K_y\) for \(h\in G_y\). Conversely set \(K_{gy}=g_*\mu_y\). Stabilizer invariance makes this independent of the representative \(g\); its support lies in \(F_{gy}\), and equivariance is immediate. \(\square\)

**Finite-fiber corollary.** If every \(F_y\) is finite and nonempty, the uniform probability on each full fiber is an equivariant stochastic lift: every group element bijects \(F_y\) with \(F_{gy}\). This remains valid when \(G\) itself is infinite. Consequently the finite-group-action **trichotomy collapses to two cases**: deterministic-equivariant available, or stochastic-but-not-deterministic; never absence of a stochastic lift.

**Complete invariant-probability simplex for finite fibers.** Split \(F_y\) into the \(G_y\)-orbits \(O_1,\ldots,O_r\). An invariant probability is **uniquely** a convex mixture \(\sum_i t_i\operatorname{Unif}(O_i)\) with \(t_i\ge0,\sum t_i=1\). This follows because invariance forces equal mass at every point in an orbit. The extreme measures are exactly these orbit-uniform distributions; Dirac extreme points occur precisely on singleton orbits. On a finite quotient, the full space of equivariant lifts is a product of such orbit-simplexes indexed by quotient orbits. Unless that simplex is a point, invariant choice **is not a unique posterior**.

**Countable discrete-fiber corollary.** On a nonempty **countable** fiber \(F_y\), a \(G_y\)-invariant countably additive probability exists **iff \(G_y\) has a finite orbit in that fiber**. Proof: any countably additive probability on a countable set gives positive mass to some point. Invariance makes every point of its stabilizer orbit equally positive; therefore that orbit is finite. Conversely its uniform measure works. No finite-orbit hypothesis is needed for an *uncountable* compact homogeneous space admitting a Haar probability; the countable condition is load-bearing.

**Counterexample:** \(G=\mathbb Z\) acting by translations on \(X=\mathbb Z\), with \(Y=\{*\}\). Invariance would assign the same mass \(c\) to every integer, forcing either total mass 0 or divergence. There is no invariant countably additive probability. Finitely additive invariant means are a different mathematical type; they are not the sampling distributions claimed here.

## EC-04 — General finite monoid actions: exact rational LP and Farkas dual (PROVED)

Let \(X,Y\) be finite and \(M\) generated by a finite set \(\mathcal G\) of total endomaps (not necessarily reversible). Write \(p_{yx}=K_y(x)\) for \(q(x)=y\). A stochastic lift exists **iff** the following rational linear system has a nonnegative solution:

\[
\begin{aligned}
\sum_{x\in F_y}p_{yx}&=1 && (y\in Y),\\
p_{y x}&\ge0&& (x\in F_y),\\
\sum_{z\in F_y:\,g_Xz=x}p_{yz}&=p_{g_Y y,x}
&&(g\in\mathcal G,\;y\in Y,\;x\in F_{g_Y y}).
\end{aligned}
\tag{LP}
\]

Each generator's condition composes to every word, so it suffices to check generators. The constraints have **integer coefficients**, and each fiber normalization bounds all variables in \([0,1]\). Consequently any nonempty feasible polytope has a rational vertex. The exact standard-library checker `equivariant_choice.py` enumerates all possible vertex supports and solves full-column-rank systems by exact Fraction elimination; if none exists it returns `None`, and this is a **complete** finite feasibility verdict within its documented variable cap. Large instances raise an explicit error rather than claiming nonexistence.

**Farkas alternative.** Write the equality system \(Ap=b,p\ge0\). Exactly one holds: (i) a stochastic lift exists; or (ii) there is a rational row vector \(\lambda\) with \(\lambda^TA\ge0\) coordinatewise and \(\lambda^Tb<0\). A given \(\lambda\) is checkable without trusting an optimizer. (Standard Farkas lemma; [Stanford CS361B notes, §7.1](https://web.stanford.edu/class/cs361b/files/cs361b-notes.pdf).) We supply an explicit such \(\lambda\) for EC-05; the checker validates it from the generated constraints.

**Important counter-theorem:** source-to-report action descent \(qg_X=g_Yq\) does **not** imply existence of any equivariant stochastic right inverse. Predictively correct observed dynamics can coexist with irrecoverable source dynamics.

## EC-05 — Minimal single-T no-stochastic carrier and a sharp half-unit defect (PROVED)

Let \(X=\{a,b,c\}\), \(Y=\{u,w\}\), and

\[
q(a)=u,\ q(b)=q(c)=w;\quad T_X(a)=b,\ T_X(b)=c,\ T_X(c)=c;\quad T_Y(u)=T_Y(w)=w.
\]

Then \(qT_X=T_Yq\) **exactly**. A stochastic section must have \(K_u=\delta_a\). Covariance from \(u\to w\) forces \(K_w=T_*K_u=\delta_b\); covariance from \(w\to w\) forces \(K_w=T_*K_w=\delta_c\). Contradiction. A deterministic equivariant section is therefore impossible as well.

**Explicit Farkas certificate.** Name the LP rows `norm(u)`, `dyn(u,b)`, and `dyn(w,b)`. Their coefficients give exactly

\[
-\mathrm{norm}(u)+\mathrm{dyn}(u,b)-\mathrm{dyn}(w,b):\quad 0=-1.
\]

This is a rational infeasibility certificate, verified against the exact constraint matrix rather than merely described verbally.

**Minimality for one generator.** On at most two source states, if \(q\) is injective its inverse is an equivariant point section; otherwise \(Y\) is a singleton and every finite self-map \(T_X\) has a nonempty periodic orbit, whose uniform cycle measure is invariant. Thus three source states and two reports are minimal for a one-generator **finite** no-stochastic example. Exhaustive code checked all **12** equivariant two-source-state one-generator tables (none fails), and all **279** three-source-state tables, of which **24** fail stochastic feasibility. This finite census corroborates, not replaces, the general paper proof.

**Sharp operational defect.** Even without exact equivariance, choose a fiber-supported kernel \(K\). Define

\[
\varepsilon(K)=\max_{g,y}\|g_*K_y-K_{gy}\|_{\mathrm{TV}}.
\]

For this three-source example every kernel has \(K_w=p\delta_b+(1-p)\delta_c\). Therefore

\[
\varepsilon(K)=\max\{1-p,p\}\ge\tfrac12,
\qquad \boxed{\inf_K\varepsilon(K)=\tfrac12}.
\]

The minimum is attained at \(p=1/2\). This **is** a rigorous, quantitative, nonzero defect, not an approximate exact section. The same obstruction occurs with two distinct precursor reports merging into one: \(a\mapsto c,b\mapsto d,c\mapsto c,d\mapsto d\) and \(q(a)=u,q(b)=v,q(c)=q(d)=w\).

**Two-generator minimality contrast.** With only \(X=\{0,1\}\), \(Y=\{*\}\), actions \(T_0\) constant 0 and \(T_1\) constant 1 have no common invariant probability; both would require contradictory point masses. Thus the one-generator minimality cannot be transported to arbitrarily many generators.

## EC-06 — Stochastic-only can require a nonuniform section (PROVED MODEL)

On \(X=\{a,b,c\}\), \(Y=\{*\}\), let \(T_X(a)=b\), \(T_X(b)=a\), \(T_X(c)=a\). There is no fixed point, hence no deterministic equivariant section. The **unique** invariant probability is \(\mu(a)=\mu(b)=1/2,\mu(c)=0\), supported on the periodic cycle. A uniformly random choice from *all three* states would not be stationary. This separates "random choice exists" from "uniform on every observed fiber is always valid"; the latter only follows for group/bijective actions on finite fibers.

## EC-07 — A new finite-versus-analytic-limit split (PROVED)

For a **fixed finite** action quotient, all fiber-supported normalized kernels form a compact product of finite simplexes. The function \(K\mapsto\varepsilon(K)\) is continuous. Thus its minimum is attained and

\[
\inf_K\varepsilon(K)=0 \quad\Longleftrightarrow\quad\exists K:\varepsilon(K)=0.
\]

**No fixed finite system can have an unattained zero-defect infimum.** If exact stochastic choice is obstructed, its minimum mismatch is strictly positive.

But on the infinite shift example \(X=\mathbb Z\), let \(K_N\) be uniform on \(\{-N,\ldots,N\}\). Then direct support comparison gives

\[
\boxed{\|T_*K_N-K_N\|_{\mathrm{TV}}=\frac1{2N+1}\to0,}
\]

while there is **no** exact countably additive invariant probability. The limit cannot be a countably additive probability on \(\mathbb Z\): every individual point mass tends to zero, and no normalized probability has all singleton masses zero on this countable set. Probability mass escapes to infinity. This is an exact example of the author's analytic/limit defect: every finite approximation is imperfect, the infimum vanishes, and no exact permissible probabilistic section realizes it. A finitely additive invariant mean or an adjoined boundary state would change the ambient target category and must be declared separately.

This theorem is *model-relative*, not a statement that physical observers necessarily face this infinite symmetry.

## EC-08 — Source-faithful actual history requires an identifying instrument (PROVED ELEMENTARY)

Take two different initial histories \(a\to c\) and \(b\to c\), and let even the observer's current readout be the identity on the present state \(c\). Their actual histories still produce the same report. For a target \(P\) describing the initial branch, \(P\) does not factor through the present-state evidence map. No point or stochastic section of the **present-state quotient** can determine the true history without an archived source label, source-authenticated prior/likelihood, or other history-sensitive probe.

Conversely, when an *allowed finite set of repeatable nondisturbing probes* separates every pair in a finite current source fiber, a single-copy finite schedule identifies its current source state (SUCC OC-2 and target-descent). This is executable identification **conditional on the probe's source adequacy**; merely positing a new probe is not a discovery of a physical instrument. In the three-state EC-05 model, one binary readout distinguishing \(b\) from \(c\) refines the observed quotient to an injective one and yields a deterministic equivariant inverse on the refined image, if that readout is actually available. The new probe still cannot retrospectively recover destroyed earlier history after \(a\to b\to c\) without separate memory.

**Ideal observer firewall:** a classical source-state identity update \(T_X=\mathrm{id}\) can be informative when the observer memory changes. A quantum instrument with total channel \(\mathrm{id}\) for all states cannot extract unknown-state information; nondemolition information is possible on restricted commuting/pointer-state sets (SUCC OC-6). Disturbance and choice must remain separate notions.

## EC-09 — Stochastic source laws: Markov descent is still not stochastic reconstruction (PROVED)

The previous theorems used deterministic source actions and probability only for the **choice kernel**. An actual source law may itself be stochastic. Let \(P_X:X\to\mathcal D(X)\) be a specified source Markov kernel and \(P_Y:Y\to\mathcal D(Y)\) the observed Markov law. An exact forward observed process exists when

\[
\sum_{x':q(x')=y'}P_X(x,x')=P_Y(q(x),y')\quad\text{for every }x,y'.
\]

This is the standard **strong lumpability** condition for the given source/report partition: the observed transition law does not depend on which hidden state produced the report. It is a declared probability law, not a consequence of support equality.

A backward probabilistic reconstruction consistent with both laws would require a fiber-supported row-stochastic kernel \(K:Y\to\mathcal D(X)\) with

\[
\boxed{K P_X=P_Y K,\qquad q_*K_y=\delta_y.}
\]

In coordinates, for every \(y\in Y,x'\in X\),

\[
\sum_{x\in F_y}K_y(x)P_X(x,x')
=\sum_{y'\in Y}P_Y(y,y')K_{y'}(x').
\]

These are again linear rational constraints plus simplex normalization, so the exact finite LP/vertex/Farkas theorem EC-04 applies. Our separate `FiniteMarkovQuotient` class verifies forward lumpability, builds this rational system, and checks any candidate section with independent matrix multiplication.

**Positive model:** \(a\to\frac12\delta_b+\frac12\delta_c\), with both \(b,c\) absorbing; observations \(q(a)=u,q(b)=q(c)=w\). The observed process is \(u\to w\to w\), and \(K_u=\delta_a\), \(K_w=(\delta_b+\delta_c)/2\) is an exact stochastic lift.

**Negative model:** Keep the same observation map and observed process, but let \(a\to\frac12\delta_b+\frac12\delta_c\), \(b\to c\), \(c\to c\). The first transition forces \(K_w=(\delta_b+\delta_c)/2\), while the second forces \(K_w=\delta_c\); no exact stochastic lift exists. Thus **even a source-verified Markov quotient does not imply a Markov-intertwining stochastic right inverse**. The earlier deterministic EC-05 is a special case. This strict separation is another candidate interoperability theorem for Astra's predictive closure and Fable's causal-quotient exactness.

The Markov model is a *declared* source-conditional stochastic law. Fitting a prior or stochastic kernel after seeing outcomes does not retroactively authenticate that source law.

---

## EC-10 — Interoperability with Principia and existing SUCC results

- [PR #625 — OC-1..OC-6](https://github.com/femboy2112/SUCC/pull/625): extends the two-point swap to **arbitrary equivariant group quotients**, arbitrary finite time monoids, countable fibers, and asymptotic but unattained covariance.
- [PR #47 — EODCS III](https://github.com/femboy2112/SUCC/pull/47): the source-successor support gives MAY/COMMON, not a probability law. Our \(F(y)=q^{-1}(y)\) is the canonical lax source-fiber lift; equal support is weaker than equal transition probabilities. No claims of newly proving RC1–RC8.
- [PR #620 — weighted ancestral observer quotients](https://github.com/femboy2112/SUCC/pull/620): even exact *forward* observational descent may fail to admit a stochastic *backward* lift; EC-05 is a concrete strict separation.
- [PR #619 — predictive closure](https://github.com/femboy2112/SUCC/pull/619): a well-defined effective transition does not imply that a time-equivariant section of the hidden carrier exists, even probabilistically. EC-05 can serve as an integration countermodel.
- [PR #624 — pre-activation distinction](https://github.com/femboy2112/SUCC/pull/624): multiple source identities before observation do not imply a source-reconstructing observer; the quotient may erase their history.
- AoC is a set-theoretic choice principle, not the same thing as constructive identification or probability normalization. A deterministic but non-equivariant point section is available on every finite surjection in Set, but does not respect action or actual source selection.

## Steelman–crucible–verdict ledger

| Claim | Verdict | Authority and decisive test | Boundary |
|---|---|---|---|
| EC-01 lax fiber section | DISCLOSED (elementary proof) | \(q(mx)=mq(x)\) | no probabilities or selected path provenance |
| EC-02 group point criterion | DISCLOSED (paper proof) | stabilizer fixed-point iff; 4-cycle hostile case | arbitrary Y needs orbit-choice premise |
| EC-03 group probability criterion | DISCLOSED (paper proof) | invariant stabilizer measures; finite orbit simplex | no physical prior; countable vs continuous |
| EC-04 finite monoid LP/Farkas | DISCLOSED (paper proof + exact finite algorithm) | rational normalized constraints; dual witness | computational cap; stochastic source models not covered |
| EC-05 no stochastic with one T | DISCLOSED (explicit countermodel) | 3-state contradiction, Farkas certificate; sharp TV=1/2 | minimality specific to single generator, finite states |
| EC-06 stochastic-only nonuniform | DISCLOSED (explicit stationary cycle) | transient cycle, exact invariant probabilities | normalized posterior still source-dependent |
| EC-07 infinite approximate, unattained | DISCLOSED (explicit exact formula) | shift \(\mathbb Z\), TV=1/(2N+1), mass escape | no physical infinite-state source calibration |
| EC-08 historical reconstruction | DISCLOSED (elementary countermodel) | distinct past histories same present | archived records or real source probes can separate |
| EC-09 Markov forward/backward separation | DISCLOSED (paper + exact LP models) | same observed Markov law, contrasting lift feasibility | source probabilities must be declared |
| General universal AoC from any T | REFUTED | 3-state one-generator no-stochastic carrier | Set choice and lax relational lift survive |
| A single real-world observer has universal identity-channel access | UNVERIFIED / physically implausible as universal quantum law | quantum no-information bound | no source adequacy |

**Claim-status discipline:** *DISCLOSED* here means mathematical proof under a specified finite/discrete source model or the explicit infinite shift example; it does **not** authenticate an external physical carrier. Independent same-family finite computations corroborate exact formulas but are not a second blind source witness. Our claims may be classical prior art; do not assert academic novelty.

## Next verdict-changing probes

1. Derive **source-relative probe budgets** for upgrading a lax lift to a stochastic or point-valued lift under lawful nondisturbing instruments; count costs, forbid invented source readouts.
2. Generalize EC-09 to **multi-action, controlled stochastic Markov sources** and quantify the minimum backward-disintegration defect when the forward quotient is exact; retain supports and probabilities as separate source-typed objects.
3. Produce Lean-checked versions of EC-01/EC-02/EC-05 and an independently verified dual certificate; the current package only has paper proofs and exact Python/SymPy models.
4. Find a nontrivial SUCC numerical source whose independently authenticated action/probe map instantiates either EC-05's strict forward/backward gap or EC-07's limit escape. A generic existence construction is not a source-specific theorem.
5. Check if a target-relative section exists even when full-state point/probability sections do not. Defining the target on the fibers can make an exact observer report available without global hidden reconstruction.

**Reproduction:** `python -m unittest discover -s tests -p 'test_equivariant_choice.py' -v`, `python research/2026-11-14/choice_trichotomy/independent_sympy_oracle.py`. These focused commands are independent of mainline imported arithmetic/Lean modules. The full SUCC root suite/Lean were not executed in this runtime; see `VALIDATION.md`.

**Mathematical neighbors:** Classical orbit-stabilizer and homogeneous-space methods; invariant measures for finite group actions; LP duality/Farkas lemma ([Stanford course notes](https://web.stanford.edu/class/cs361b/files/cs361b-notes.pdf)); nonexistence of countably additive translation-invariant probability on \(\mathbb Z\); SUCC EODCS III for possibility versus probability. No complete bibliographic novelty search is claimed.
