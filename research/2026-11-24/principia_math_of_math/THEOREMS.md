# Principia Observatoris — Mathematics of Mathematics: first native reconstruction theorems

**Research date:** 2026-11-24. **Base:** SUCC Main XXVI, commit 81be6b897ae980b801a3b9de9e22ef81e8360bfb. **Status:** classical/proved-paper foundational lemmas with a newly integrated exact finite certificate prototype. No claim of academic priority or a new independent RH proof. The uploaded prototype is restricted to the explicitly declared mathematical sources below.

## 0. The question, without replacing it by a proof checker

The proposed foundation studies *how mathematical objects and their properties become available through lawful constructions*. Its primitive distinction is not mathematics versus a human observer. It is (a) a source structure, (b) the constructions and their histories, (c) observations/quotients of those constructions, (d) the witness that a mathematical conclusion follows, and (e) a valid realization of the constructed mathematics.

A faithful reconstruction must recover mathematical relationships, not just rename a theorem or import its conclusion as an axiom. Finitary formal proof encoding is one component, not the research objective. This file gives a small vertical slice: an endpoint-null but path-nonzero arithmetic square, target-relative knowledge volume, a conservative proof-path enrichment, and a genuine two-place arithmetic capacity theorem reconstructed as a sequence of source-null witnesses.

### A typed object

A source passport \(\mathsf S\) specifies an object class \(X\), legal generators \(a:x\to x'\), permitted compositions, interpretations of numerical/analytic structures, an observation toolkit, and a target. A path is a *labelled composable sequence*, not just its endpoint. The free path category \(\mathsf{Path}(\mathsf S)\) has states as objects and labelled paths as arrows. An endpoint functor and an instrument/readout functor may discard information. A mathematical witness is a retained path, equation, bound, or proof term with an independently checked interpretation.

Where appropriate, lift the path category to integer edge chains \(C_1(\mathsf S;\mathbb Z)\). The boundary map \(\partial:C_1\to C_0\) records endpoints. Source-calibrated cochains \(\omega\in C^1\) evaluate labelled paths. The distinction \(\partial c=0\) versus \(\langle\omega,c\rangle=0\) is fundamental: they are separate predicates, and neither equals the claim that the underlying chain is literally zero.

## T1. Authentic SUCC/FUCC affine square: an observable zero with a path witness

**Domain:** positive integers \(n\ge1\), rational prime \(p\), lawful actions \(S(n)=n+1\), \(V_p(n)=pn\). The source category retains the action labels, not just the integer endpoints.

Two paths run from \(n\) to \(p(n+1)\):

\[
\alpha_{n,p}: n\xrightarrow{S}n+1\xrightarrow{V_p}p(n+1),
\]

\[
\beta_{n,p}: n\xrightarrow{V_p}pn\xrightarrow{S}pn+1\xrightarrow{S}\cdots\xrightarrow{S}pn+p.
\]

The **labelled difference chain** \(c_{n,p}=\alpha_{n,p}-\beta_{n,p}\) is nonzero and \(\partial c_{n,p}=0\). It expresses \(V_pS=S^pV_p\) as endpoint agreement, not equality of path *words*.

Define the legal source cochain \(\omega(S\text{ at }a)=a\), \(\omega(V_p\text{ at }a)=0\). Then

\[
\langle\omega,c_{n,p}\rangle
=n-\sum_{j=0}^{p-1}(pn+j)
=(1-p^2)n-\frac{p(p-1)}2\ne0.
\]

**Proof:** the endpoint identity is elementary; the labelled paths contain different generators, so their free edge chains are different. The displayed sum is exact. Since \(p\ge2,n\ge1\), the response is strictly negative.

**Control:** every exact cochain \(\omega=dg\), where \(dg(e)=g(\operatorname{target}(e))-g(\operatorname{source}(e))\), vanishes on the same cycle by telescoping. A fake composite \(p=6\) is not licensed by the **genuine-prime** source passport. The integer formula extends to composite multipliers, but source authentication does not.

**Interpretation:** zero endpoint displacement is only one *kind* of zero. The path and cochain carry an independently meaningful distinction. No assertion about quantum superposition, mixing, RH, or the original BBP phase follows.

## T2. Knowledge volume and target-relative discrimination

**Domain:** a finite-dimensional vector space \(V\) over a field \(\mathbb K\); finite-dimensional linear observation \(P:V\to W\); legal linear actions \(A_a\in\operatorname{End}(V)\). For a word \(w=a_1\cdots a_k\), let \(A_w\) be the correctly ordered composition. Let

\[
\mathcal K_m=\operatorname{span}\{\lambda\circ P\circ A_w:
\lambda\in W^*,\, |w|\le m\}\subseteq V^*.
\]

Then \(\mathcal K_m\subseteq\mathcal K_{m+1}\), with a genuinely new accessible linear distinction precisely when \(\dim\mathcal K_{m+1}>\dim\mathcal K_m\).

For an exact linear target \(t\in V^*\), assume the entire listed *counterfactual* word report bank is jointly meaningful as mathematical data. The target is determined by those reports on all of \(V\) **if and only if** \(t\in\mathcal K_m\).

**Proof:** if \(t\) is in the row span, it is a linear combination of reports. Conversely, if it is not, finite-dimensional annihilator duality supplies \(v\in\bigcap_{|w|\le m}\ker(PA_w)\) with \(t(v)\ne0\). Thus states 0 and \(v\) have identical word reports and opposite target values. This is classical observability/linear algebra, aligned with Principia's existing row-span theorem and kernel descent.

**Non-conclusions:** rank is not numerical precision, probability, nonvanishing of an arithmetic determinant, or a physically executable single-copy probe policy. Duplicate paths add no rank. Signed cochains and quadratic norms require their own calibrated source interpretations. A source-label or a hash is only provenance, not proof of the source law.

## T3. Conservative enrichment of a finitary mathematical proof path

Let \(T\) be any declared finitary, typed deductive calculus with formation rules, inference rules and admissible proof equations. Construct a SUCC *tagged derivation category* in which an arrow is an original well-typed derivation with an additional retained source/provenance/path witness. A legal composition is substitution/cut when the corresponding original inference is legal. Erasing the tags gives \(U\) to the original derivation category.

**Conservative embedding theorem (CLASSICAL / syntactic):** the canonical tagging \(E\) of original derivations satisfies \(U E=\mathrm{id}\) on derivations, up to the declared syntactic equivalence. Therefore a tagged derivation cannot create a new untagged theorem by erasure; the original proof path is recoverable. Proof is induction on derivation formation and composition. This is the standard free-syntactic construction, not a new claim of mathematical foundations or full semantic equivalence.

**Critical qualification:** this theorem is only about retaining *existing syntax*. It does not establish that SUCC has natively reconstructed the mathematical content of any nontrivial imported lemma. That stronger task requires a source-preserving realization of each object/operation and proof of its quantitative and completion properties. It also must not confuse a restricted Yoneda observation with the full representable functor.

## T4. Correlated null observations force integral arithmetic capacity

**Domain:** integer radix \(b\ge2\); rational prime \(p\); integers \(m,d\ge0\); a **nonzero** \(F(z)=\sum_{k=0}^D a_kz^k\in\mathbb Z[z]\). The source label is the auxiliary integer-polynomial model, not the original BBP recurrence or zeta.

Define Hasse/divided-power jets \(D^{[k]}F(0)=a_k\). Assume:

\[
F(0)=0,\qquad F(b^{-j})=0\quad (1\le j\le d),
\]

\[
D^{[k]}F(0)\equiv0\pmod{p^m}
\quad (0\le k\le D).
\]

Then

\[
\boxed{\|F\|_1=\sum_k|a_k|\ \ge\
p^m\,b^{d(d+1)/2}.}
\]

In fact the absolute leading coefficient obeys the same bound.

**Constructive proof.** The Hasse constraints make \(F=p^mH\) for an integer polynomial \(H\ne0\). The root at zero makes \(H=zH_0\). At each distinct rational root \(b^{-j}\), the primitive integer linear polynomial \(b^jz-1\) divides the remaining integer polynomial. To see the *integrality* directly, write \(A(z)=\sum_{i=0}^n a_i z^i\). The proposed quotient \(B(z)=\sum_{i=0}^{n-1}b_i z^i\) by \(qz-1\) is forced by the recursion \(b_0=-a_0\), \(b_i=q b_{i-1}-a_i\); these are integers. The condition \(A(1/q)=0\) is exactly the final leading-coefficient compatibility \(a_n=q b_{n-1}\). Thus repeated division constructs

\[
F(z)=p^m z\left(\prod_{j=1}^d(b^j z-1)\right)Q(z),
\quad Q\in\mathbb Z[z]\setminus\{0\}.
\]

Taking leading coefficients gives
\(
|\operatorname{lc}(F)|=p^m b^{d(d+1)/2}|\operatorname{lc}(Q)|
\ge p^m b^{d(d+1)/2}.
\)
The coefficient \(\ell^1\) norm dominates the leading coefficient. QED.

**Native representation:** each null report is a *licensed factor removal*, retained as a source-labelled proof step. The independent checker multiplies all extracted factors back, verifies source identity and the prime-power coefficient law, re-evaluates the exact rational roots, and computes the bound without trusting the constructor's division procedure.

**Conditional contradiction:** if a separate, genuine source proof gives \(\|F\|_1<M<p^mb^{d(d+1)/2}\) while also certifying \(F\ne0\) and all the listed nulls, the source assumptions are incompatible. If \(F=0\), no contradiction follows. This is exactly the nonvanishing trap.

**Independence trap:** measuring the same root twice does not license removing its factor twice. A second removal requires a *new multiplicity condition*, e.g. an additional Hasse jet vanishing at that root. The present source uses \(d\) **distinct** rational roots. Likewise ordinary \(k!\)-weighted derivatives modulo \(p\) cannot replace Hasse jets without a factorial-unit argument.

## T5. A semantics-first hierarchy, not one truth score

The foundation must keep separate:

- **Source adequacy:** does the mathematical source law specify the object under study?
- **Observation adequacy:** which distinctions survive the allowed readouts?
- **Path fidelity:** which original constructions are identifiable after quotient?
- **Proof sufficiency:** do the surviving hypotheses entail the target?
- **Quantitative strength:** what norms, valuations, rank or height bounds are actually proved?
- **Completion:** what topology and uniformity permit transition to a global theorem?
- **Execution:** what is formally proved, what has been mechanically checked, and what is merely modeled?

For the examples in T1 and T4, these are checkable classical claims. An arbitrary infinite tower of equations, a high-dimensional row-span, or a formally beautiful categorical diagram does not establish the missing arithmetic inequalities.

## T6. Essential countermodels and scope

1. **Dependent zeros:** sums of old recurrence equations have no new rank (SUCC Seinfeld SS-01/02).
2. **Homological erasure:** \(V_p\) is a Koszul boundary/null-homotopic map, but its original arithmetic action is not zero. Homology alone cannot reproduce the Weil prime impulse (SUCC ERW-09).
3. **Metric shadow:** \(\mathbb Z_p\) and \(\mathbb F_p[[t]]\) can have the same unlabelled p-adic observation tree while their carry extension arithmetic differs (Witt-carry PR #240).
4. **Counterfeit source:** a changed signed forcing may preserve finite or even all local positive-moment constraints while yielding a nonnormal completed orbit (Causal Echo PR #467).
5. **Analytic distribution:** an all-late-shell Weyl *average* approaching zero is not the assertion that a polynomial has exact roots \(b^{-j}\). No step in T4 upgrades the former to the latter.
6. **Zero source:** \(F=0\) meets every null constraint but cannot yield a contradiction from divisibility versus norm.

## T7. Reproduction and authority

Native code: observational_succ/principia_semantic_core.py.
Root-discoverable tests: tests/test_principia_semantic_core.py.

The source labels in this prototype are **declared internal models**, not cryptographic or empirical source authentication. The checker is exact arithmetic over ordinary integers and rational numbers. Its finite tests check implementation claims, while the universal statements above are supported by the written proofs.

Full SUCC gates, Lean verification, external peer review, a genuine RH-theorem reconstruction, and a source-attested original-BBP arithmetic bridge are **not** claimed.

**References inside SUCC:** docs/principia_observatoris/README.md; research/2026-10-25/SEINFELD_SUCC_NOTHING_THEOREMS.md; research/2026-10-18/EQUIVARIANT_REDUNDANCY_WEIL.md; research/2026-11-12/adaptive_boundary_resolution/INTEGER_INFORMATION.md; SUCC PRs #72, #240, #619, #633, #687, #689. Prior mathematical ingredients (Yoneda, Gauss lemma, Hasse derivatives, linear observability) are classical.


## T8. A genuine RH-facing local construction drops out of a FUCC path resolvent

**Domain:** an authentic rational prime \(p\), the integer multiplication operator \(V_{p^2}|n\rangle=|p^2n\rangle\) on \(\ell^2(\mathbb N_{>0})\), and a declared coefficient map \(|n\rangle\mapsto T^n\). This is a local formal-group **model**, not an assertion of actual theta-kernel integrality.

The bounded operator \(p^{-1}V_{p^2}\) has norm \(1/p<1\), so the geometric resolvent exists:

\[
\mathcal R_p=(I-p^{-1}V_{p^2})^{-1}
=\sum_{j\ge0}p^{-j}V_{p^{2j}}.
\]

On the source unit basis vector, its coefficient representation is exactly

\[
\boxed{\ell_p(T)=T+\sum_{j\ge1}p^{-j}T^{p^{2j}}.}
\]

Hence

\[
\ell_p(T)-p^{-1}\ell_p(T^{p^2})=T.
\]

**Proof:** the terms of the Neumann series are orthogonal basis shifts on \(|1\rangle\) and converge in Hilbert norm. The displayed functional equation follows by cancellation of the successive prime-square terms. The formal power series has linear coefficient 1, so there is a unique compositional inverse \(U_p(z)\in\mathbb Q_p[[z]]\), with \(U_p(0)=0\), \(U_p'(0)=1\).

**Valuation theorem (CLASSICAL / exact formal induction):**

\[
\boxed{v_p([z^a]U_p)\ge-\frac{a-1}{p^2-1}
\quad(a\ge1).}
\]

Proof: from \(\ell_p(U_p)=z\),

\[
U_p=z-\sum_{j\ge1}p^{-j}U_p^{p^{2j}}.
\]

For \(a>1\) and \(r=p^{2j}\le a\), every monomial contributing to \([z^a]U_p^r\) is a product \(u_{i_1}\cdots u_{i_r}\), where \(i_h\ge1\), \(\sum_h i_h=a\), and \(i_h<a\). By induction its valuation is at least \(-(a-r)/(p^2-1)\). The factor \(p^{-j}\) costs \(j\), but \(j\le(r-1)/(p^2-1)\). Therefore every summand has valuation at least \(-(a-1)/(p^2-1)\); the nonarchimedean triangle inequality proves the result.

For \(f(T)\in\mathbb Z_p[[T]]\), composition with \(U_p\) has the same coefficient bound at every degree \(a\ge1\), because all coefficients of \(f\) are \(p\)-integral and the composition terms partition \(a\) into positive indices. Ordinary differentiation then gives

\[
\boxed{v_p\bigl((f\circ U_p)^{(a)}(0)\bigr)
\ge v_p(a!)-\frac{a-1}{p^2-1}.}
\]

Together with Legendre's factorial formula, the leading gain is
\(a(1/(p-1)-1/(p^2-1))\), up to a logarithmic error. This is a **genuine mathematical ingredient appearing in the conventional RH exposition**, reconstructed using an authentic FUCC multiplication path and formal coefficient transport. The same local lemma was already derived in SUCC draft #687 T4/T4b; this round **integrates** it into the native path/knowledge/null reconstruction architecture rather than presenting it as an original discovery.

**Executable exact check:** observational_succ/principia_formal_group.py constructs \(\ell_p\), computes \(U_p\) coefficientwise, checks \(\ell_p(U_p)=z\) modulo the declared truncation, checks valuations of \(U_p\) and of derivatives of \(f(U_p)\), and verifies the resolvent equation. Tests include a height-one mutant: \(\ell(T)=T+T^p/p\) has inverse coefficient \([z^p]U=-1/p\), which violates the height-two bound \(-1/(p+1)\). A non-\(p\)-integral test kernel and fake composite prime are rejected. Independent SymPy compositions were executed for several small primes and truncations.

**The central unproved next arrow:** showing that the **actual automorphic/CM theta kernel** entering the released RH proof has coefficients in the correct integral local model *after the real period, conductor, and coordinate normalizations*. This source-identification statement is M4, and is not implied by the formal inverse lemma. Similarly, the model's \(p\)-adic gains do not produce RH by themselves without nonzero global period minors, rank and Archimedean bounds.

**Scope:** universal paper theorem under stated ring hypotheses, finite exact computation as diagnostics, no original-BBP digit equidistribution, no automatic full CM theta transfer, and no independently proved RH.
