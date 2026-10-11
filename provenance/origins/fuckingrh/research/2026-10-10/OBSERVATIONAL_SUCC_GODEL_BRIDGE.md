# Observational SUCC meets Gödel: a typed logic interface

**2026-10-10. RH OPEN.** Continuation of the formal observer/ordinal and second-order Weil report at base commit b93f42a9f07eaf22eb64631b80ee74426235d354. This dossier describes classical theorems, elementary new-to-project consequences, and a bounded computational demonstration. No claim that RH is independent of PA/ZFC, that an infinite physical process returns, or that an observer's Hilbert covariance equals the Weil form.

## 0. The user's proposal vs. our operational interpretation

**User:** A mathematician is first a physically embedded Hilbert-space observer. Finite SUCC observations build semantic and mathematical objects. Some universal statements cannot be settled merely by carrying out any prescribed finite list of observations. Model a never-ending SUCC process using ordinals, send the observer to a formal omega limit, and interpret a report at omega+1 that compares *relationships between observations* (the second-order feature) with the completed Weil form.

**Interpretive repair:** distinguish five types: (1) finite observations; (2) finite syntactic proofs in a named theory T; (3) truth in the standard model of arithmetic; (4) computable recognition of counterexamples; and (5) a source-derived analytic Weil/Suzuki completion. None of these type conversions is guaranteed by embodiment in a Hilbert space.

For a recursive Boolean predicate P:

- Obs_N(P) = (P(0), ..., P(N)); a finite observation object.
- Refute_N(P) = existence of n <= N with P(n)=false; a finite witness.
- Truth_omega(P) = for every n, P(n); a semantic universal statement.
- Prove_T(P) = existence of a finite T-proof of the formula for every n P(n); a syntactic fact.
- Decide_Pi1(P) = hypothetical total computation of the truth value for every computable P; not available.

One can know an individual instance, prove it in T, or detect a counterexample without deciding the universal claim.

## 1. First obstruction: pointwise coverage is not one uniform horizon

Take F(N,k) to mean k <= N. Then the statement

\[
(\forall k\ \exists N\ F(N,k))
\]

is true, while

\[
(\exists N\ \forall k\ F(N,k))
\]

is false. Proof: take N=k for the first and k=N+1 against the second. This is an exact failure of a quantifier swap. It does not, by itself, prove logical incompleteness.

The directed union O_omega = colim_N O_N may contain every finite record. But omega+1 as a report is **a specified operation on that colimit**, not a computation physically performed after waiting through infinitely many steps. A limit does not manufacture a sound inference rule.

## 2. Genuine Gödel instance: infinitely many individual proofs, no universal proof

Let T=PA with its standard Gödel numbering of finite proof codes, or another suitable consistent effectively axiomatized arithmetic theory with a standard proof predicate. Put

\[
P_T(n):=\neg\mathrm{Proof}_T(n,\ulcorner 0=1\urcorner),\qquad
\mathrm{Con}(T):=\forall n\,P_T(n).
\]

A finite proof code can be checked. If T is consistent then every individual P_T(n) is true, and standard arithmetic can prove each fixed true numeral instance. Yet Gödel's **second incompleteness theorem** (with its conventional proof-predicate/derivability hypotheses) gives

\[
T\nvdash \mathrm{Con}(T).
\]

Therefore it is possible to have

\[
\forall n\,[T\vdash P_T(\overline n)]
\quad\text{but}\quad
T\nvdash\forall n\,P_T(n).
\]

This is a concrete mathematical instance of the proposed observation-versus-universal-closure gap. Unlike a Graham-number-sized search, the obstruction is **relative unprovability in one formal system**, even though every particular finite check succeeds. This does not establish RH independence.

There is an additional required mechanism: Gödel's **diagonal lemma** constructs a self-referential sentence G_T such that T proves G_T iff G_T is unprovable in T (under suitable coding). Source-connected arithmetic interaction b(pq)=a(pq)-a(p)a(q), or a second derivative of a Weil kernel, does not implement syntactic diagonal substitution. A Gödelized observer needs formulas, proof codes, a proof verifier, representability of syntactic transformations and an explicit fixed-point construction.

Primary expositions: https://plato.stanford.edu/entries/goedel/ and https://plato.stanford.edu/entries/goedel-incompleteness/ .

## 3. A computability theorem: the uniform finite-observer barrier

For a two-counter Minsky program M, let H_M(n) assert that M halts in at most n transitions. This is decidable for every finite n. Put P_M(n) := not H_M(n). Then

\[
\mathrm{Nonhalt}(M)\iff\forall n\,P_M(n).
\]

A total algorithm deciding this universal claim uniformly for *every* two-counter M would decide the complement of the halting problem, and hence halting, contrary to its undecidability. This is an established computational boundary across a class of predicates, not a proof of the undecidability of any single RH assertion or of any claimed physical hypercomputer.

The new standard-library module actualization/godel_succ.py is an **instrument** for this distinction. Its finite monitor returns only UNRESOLVED after an all-clear prefix, and REFUTED with the earliest observed counterexample. Positive control: an explicitly looping two-instruction program. Mutation: a delayed HALT at transition 19 or 25, observationally identical to the loop at earlier Boolean horizons. Negative control: immediate HALT. Five local unit tests cover the logical interface and a separate toy screw-kernel counterexample. These tests do not prove general halting undecidability; that comes from computability theory. Instruction-set dependence matters.

Technical reference: Andrej Dudenhefner (2022), *Certified Decision Procedures for Two-Counter Machines*, https://doi.org/10.4230/LIPIcs.FSCD.2022.16 .

## 4. The precise RH connection: Pi-1 shape, not shared independence

Our parent ordinal branch records Suzuki's continuous arithmetic object

\[
K(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u),
\]

where Psi is built from the prime-power von Mangoldt source and the Gamma-plus-pole Archimedean response, with the exact theorem

\[
\mathrm{RH}\iff K\text{ is positive semidefinite on every finite sample.}
\]

Since K is real continuous, strict failure at some real finite tuple has a strict failure for some **rational** times and rational coefficients, by density. Under the established effective computability of the classical arithmetic/Gamma expression, rational interval enclosures can certify a strictly negative value. Dovetail enumerated rational tuples and precisions; halt upon a certified negative. Define Bad_RH(n) to mean that the first n steps of that fixed dovetail have found such a certificate. This is a decidable finite predicate with the metamathematical equivalence

\[
\neg\mathrm{RH}\iff\exists n\,\mathrm{Bad}_{RH}(n),\qquad
\mathrm{RH}\iff\forall n\,\neg\mathrm{Bad}_{RH}(n).
\]

This is the same **co-recursively enumerable / Pi^0_1 logical shape** as the consistency and nonhalting examples. RH also has classical arithmetical Pi-1 reformulations through Lagarias/Robin and Davis-Matiyasevich-Robinson. We do **not** claim to have formalized this particular Suzuki equivalence in PA, and we do not assert any Gödel theorem for RH itself.

Sources: Masatoshi Suzuki, J. London Math. Soc. 108 (2023), https://doi.org/10.1112/jlms.12785 ; Jeffrey Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*, https://arxiv.org/abs/math/0008177 . The issue of provable equivalence in weak arithmetic is discussed at https://mathoverflow.net/questions/31846/is-the-riemann-hypothesis-equivalent-to-a-pi-1-sentence .

**Do not infer** Con(T) iff RH; nor that a proof of each fixed finite positive Gram sample in T implies one T-proof of RH; nor that the absence of computational evidence means undecidability. A single source-exclusive global theorem may prove RH with a finite argument.

## 5. Source-sensitive no-go: hidden arithmetic beyond every named finite horizon

Here is a separate elementary result and boundary. Fix finitely many time probes and their differences, all with absolute value at most B. Take an integer m with log m>B and mutate exactly one future Dirichlet coefficient a(m) by delta>0, keeping all earlier coefficients and the classical Gamma/pole response unchanged.

For Dirichlet-convolution logarithms b=log_* a, the coefficient b(m) changes by delta, and coefficients at n<m do not change. The only *other* possibly changed b(n) are at multiples of m, so no such later event is active when |t|<log(2m). In this interval:

\[
\Delta\Psi(t)=-\delta\frac{\log m}{\sqrt m}
                 (|t|-\log m)_+.
\]

All named probes within B are unchanged. Choose any log m<t<log(2m). For sufficiently large delta, the displayed negative ramp overwhelms the finite genuine value Psi(t), giving Psi_mut(t)<0 and hence

\[
K_{\mathrm{mut}}(t,t)=2\Psi_{\mathrm{mut}}(t)<0.
\]

This refutes any general inference from one bounded set of successful source observations to *global* positivity **over unrestricted coefficient histories**. But the mutant is not an Euler-admissible source! It does not refute a future structural positivity theorem for the genuine multiplicative arithmetic. For |t|>=log(2m), additional Dirichlet-log coefficients activate and the one-ramp formula above must not be extrapolated. The accompanying test uses an explicitly labeled integer-threshold toy ramp, not fake exact analytic log weights.

## 6. Turing's real ordinal logic: reflection added at successors

One precise realization of the omega+1 *logical* operation is a progression of theories:

\[
T_0=\mathrm{PA},\quad
T_{\alpha+1}=T_{\alpha}+\mathrm{Con}(T_\alpha),\quad
T_\lambda=\bigcup_{\beta<\lambda} T_\beta
\ \ (\lambda\text{ limit}).
\]

At each successor step an **additional axiom/reflection commitment** is supplied. That commitment does not become justified merely because the predecessor's finite proofs were enumerated. Soundness, consistency and notation for constructive ordinals must be managed explicitly; Turing and Feferman also studied stronger *uniform reflection* progressions. Feferman's metatheoretic completeness along suitable ordinal notations is not an algorithm to pick the right notation for an arbitrary true statement.

The infinitary omega-rule

\[
\frac{P(0),P(1),P(2),\ldots}{\forall n\,P(n)}
\]

likewise describes a stronger proof mechanism, not a final finite SUCC observation. An extraction argument transporting such reasoning to a finite proof requires its own theorem.

Primary: A. M. Turing (1939), *Systems of Logic Based on Ordinals*, https://doi.org/10.1112/plms/s2-45.1.161 . Survey: https://plato.stanford.edu/entries/proof-theory/ and https://seop.illc.uva.nl/entries/proof-theory/appendix-b.html .

## 7. Hilbert observer and second derivative: independent gates

The parent branch exhibits normalized half-density vectors in l^2(N) whose norm escapes every fixed finite projection, so even a sequence of physically modeled positive vectors need not have a normalized strong limit at omega. A separate operator-state or reporting construction would be needed.

The exact Suzuki distribution identity

\[
\partial_t\partial_u K(t,u)=\Psi''(t-u)=W_{\mathrm{Weil}}
\]

is a genuine second-order *analytic/source correlation* statement. It is not a Gödel fixed point. The missing arithmetic bridge is an explicit intertwining of observer/source histories, Gamma completion, admissible arithmetic test functions and the completed Weil form. Generic Hilbert positivity can hold equally for a fake source: positivity without source identification is RH-inert.

## 8. Verdict-changing tasks and claims

**Already mathematically established:** the quantified nonuniformity example; the Gödel consistency instance; the class-wide halting obstruction; the classic Suzuki equivalence; the elementary finite-prefix mutation no-go over unrestricted coefficients. Five finite unit tests pass in an isolated local artifact. None are independent new RH sign results.

**Next:** (1) formalize proof-code syntax and a diagonal lemma in a suitable proof assistant; (2) build a *certified* rational negative-Gram witness enumerator for the genuine Suzuki source, with quartic and delayed-mutant controls; (3) explicitly compare T-provability of separate finite positivity claims with provability of the universal completed inequality, without smuggling an omega-rule; (4) construct the source/Gamma/Weil intertwiner and prove a sign-preserving limit **independently** if possible. The final step remains precisely RH-strength.

**Ledger:** Disclosed (classical): Gödel, Turing, halting, Suzuki. Proved here (elementary): quantifier swap, delayed-source no-go. Observed: five local tests passing with source/controls. UNVERIFIED: full certified RH Gram witness engine, proof-system formalization, physical observer-to-Weil realization and global positivity. RH OPEN.

Run bounded code:

~~~sh
python -m unittest discover -s tests/actualization -p 'test_godel_succ.py' -v
python -m actualization.godel_succ
~~~