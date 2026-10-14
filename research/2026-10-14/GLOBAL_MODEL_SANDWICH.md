# GLOBAL MODEL SANDWICH — finite proofs of global claims from source-indexed mathematical charts

**Research checkpoint:** 2026-10-14. **Branch:** `research/global-model-sandwich-2026-10-14`, stacked on the IdealHard Weil sign checkpoint `a6221339136d7ad9917d21a503b2fc37ff0643e8` (ultimately descendant of `main@6e0d88f`). **RH PROVED: NO.** Status: classical mathematics with new-to-SUCC type-safe finite implementation and hostile controls. Scholarly originality, actual physical source authentication, and a general proof assistant for analytic theorems are UNVERIFIED.

## 0. What finite mathematicians actually establish

The author's hypothesis: an embedded finite observer E can assemble a graph of models of its carrier and then reason about interactions among those models. A finite mathematical proof can establish statements about infinitely many source states without having observed them all. **This does not imply that arbitrary infinite source truths are inferable from a finite list of empirical samples.** A proof can be finite while its axioms and quantified lemmas specify infinitely many cases. The crucial bridge is a **generative law and a proof of its correctness**, not a very large observation table.

SUCC already has finite source semantics, an operational Yoneda category, a NO-GHOST constraint-complete gluing theorem, VOYAGER observational inverse limits, and genuine Euler/theta/Gamma/Weil sources. This work joins two forms of *finite global justification* and tests their exact limits:

1. **Target-sensitive model transport**: a finite family of individually insufficient source charts can jointly determine a target, with a constructive decoder and exact collision witnesses.
2. **Symbolic global identity**: equality of two rational functions follows from one finite polynomial identity certificate valid on their entire common domain—not from matching at a finite set of points.
3. **Universal arithmetic source sandwich**: every factorial additive-SUCC path has one multiplicative prime-jet certificate, valid for all positive integer path lengths by a uniform finite proof of unique factorization, with no finite bound on all primes.

The compactness and analytic-identity extensions are classical mathematical imports with explicit assumptions, not results inferred by the Python tests.

## 1. Actual categorical graph and finite factorization theorem — GMS-01

Let `S` be a complete declared set of ORIGINAL source states (finite in code). An observational chart is a total map `q_i:S -> O_i`; a target is `T:S -> Y`. Every chart and arrow is indexed by `source_id`, epoch and basis. The category of chart presentations has a specified arrow `f_(i,j):O_i -> O_j` **only if** `f_(i,j) o q_i = q_j` on every admissible source. The code requires the decoder on the *reachable image* and rejects missing, false, duplicate or stale arrows. Compositions are source-faithful; source-grounded agreement of two chart paths follows on reachable states but says nothing about unavailable or physically unrealized chart states.

For a joint context `I` put `q_I(s)=(q_i(s))_(i in I)`. **Theorem (CLASSICAL):** there exists a decoder `D:q_I(S)->Y` with `T=D o q_I` iff

`forall s,t in S: q_I(s)=q_I(t) ==> T(s)=T(t)`.

Proof: the forward direction applies `D` to a matching report. Conversely define `D(q_I(s))=T(s)`; the implication guarantees independence of the choice of representative. Only the image is determined; values outside it cannot be invented. This is the kernel/quotient factorization lemma. The exact engine supplies `D`, otherwise a pair `(s,t)` with equal reports and different targets. Exhaustive tests independently enumerate all 2-output report/target tables on three source states; seeded four-source tables check minimal joint contexts.

**Positive control:** `S={00,01,10,11}`, charts `A(xy)=x`, `B(xy)=y`, target `XOR(xy)=x+y mod 2`. Neither chart determines XOR; `(A,B)` determines it. The mathematical joint model exists because all four source rows are declared. Physical joint measurability, nonresettable measurement compatibility and correct real-world source mapping are **not** established here; NO-GHOST's full kernel/public policy conditions must be attached separately.

**Source-map negatives:** individual pointwise invertibility is not enough across rival dictionaries (GENIE), and equality of pairwise marginals does not authorize a Cartesian joint source (NO-GHOST). The model must retain the original source, the actual intervention history, and complete joint-law data before a certificate can be called operational.

## 2. Finitary compactness extraction — GMS-02 (CLASSICAL THEOREM)

Let `S` be compact Hausdorff, `Y` a finite discrete space, `T:S->Y` continuous, and `q_i:S->O_i` a possibly infinite family of continuous charts into finite discrete spaces. Suppose that **every target-disagreeing pair** `s,t` is separated by at least one `q_i`. Then there exists a **finite** subfamily `I0` for which `T` factors through `q_I0`.

**Proof.** `K={(s,t) in SxS:T(s)!=T(t)}` is closed in compact `SxS` because `T` is continuous into discrete `Y`, hence compact. For each `i`, `U_i={(s,t):q_i(s)!=q_i(t)}` is open. By the separation assumption the `U_i` cover `K`. Compactness supplies a finite subcover `U_i1,...,U_ik`. Thus `q_I0` distinguishes all target-disagreeing pairs, and GMS-01 constructs the decoder. If `K=empty`, no charts are needed. **No numerical bound** on the number of charts is supplied by compactness alone.

This is a classical finite-coordinate dependence/fan-compactness argument, not a novel theorem. Finite test tables instantiate it; no finite simulation certifies the arbitrary compact theorem. In a profinite source (e.g. a genuine inverse limit of modular clocks), an actual continuous finite-valued target can be decided through finite resolution—*once the source topology, chart completeness and continuity are mathematically proved*.

**Hostile noncompact case:** `S=N` discrete, chart `q_i(n)=1_{n=i}`, target `T(n)=n mod 2`. The full infinite family separates all sources. For any finite selected `I`, choose an even `e` and odd `o` outside `I`: all selected readings are zero, but their target values differ. The engine computes an exact witness for every submitted finite menu.

**Hostile compact but discontinuous target:** `S={0,1}^N` with product topology, coordinate probes `q_i(x)=x_i`, target `T(x)=1` iff infinitely many coordinates equal 1. Full infinite traces distinguish this predicate, but any finite prefix can be completed with eventually-zero or infinitely-many-one tails giving different targets. `T` is not continuous. No statement about original RH input automatically satisfies this compactness hypothesis.

## 3. Symbolic global identity versus finite data fitting — GMS-03 / GMS-04

A rational model is an exact numerator/denominator pair over `Q[x]`, with nonzero denominator. Two models are equal on their **common defined domain** exactly when their cross-product polynomial is identically zero: `P1 Q2-P2 Q1=0`. The equality checker verifies each coefficient with exact fractions, then produces a finite integer counterexample if nonzero. A presentation `(x²−1)/(x−1)` matches `x+1` on its common domain, but the first presentation excludes `x=1`; a removable singularity must not silently be called an actually observed state.

This is a useful *finite proof of an infinite collection of equations*, and its domain/type conditions are essential. It is not an algorithm for equality of arbitrary computable analytic functions.

**Negative control:** For any finite list of rational values `x_i`, construct `P(z)=prod_i(z−x_i)(z−(1−x_i))`. This is reflection-invariant under `z -> 1-z`. Choose integer `b>=2` with `P(b)!=0`, and set `F(z)=1-P(z)/P(b)`. Then `F(x_i)=1`, `F(1-z)=F(z)` for every complex `z`, but `F(b)=F(1-b)=0` off the critical line. Thus *arbitrary finite point agreement + global functional-equation reflection does not force the Riemann zero location*. This is a fake entire model, **not** the authentic zeta or Euler source. The code constructs the mutant and independently verifies exact reflection and off-line roots.

**Analytic identity theorem route (CLASSICAL IMPORT):** if two holomorphic functions agree on a nonempty open subset of one *connected* complex domain, they agree throughout. For meromorphic functions use a common meromorphic domain and handle poles. SUCC's theta-based globally holomorphic/meromorphic representation and genuine Dirichlet/Euler representation agree in `Re(s)>1` under their source laws; classical analytic uniqueness transports the equality beyond convergence. The finite proof relies on a source-authenticated function *law* and a global analytic theorem, not finitely sampled Euler products. The local Python rational-polynomial oracle is an exact finite-grammar model of this proof mechanism, not a machine verification of the full theta theorem.

## 4. Exact universal additive/multiplicative arithmetic sandwich — GMS-05

Positive integers form a **free commutative monoid on genuine primes**, with each `n` carrying finitely many nonzero valuations `v_p(n)`. The valuation map `nu:N_{>0}->N^(Primes)` sends multiplicative successor `V_p(n)=pn` to coordinate successor `nu(n)+e_p`.

For every integer `N>=1`, unique factorization supplies the universal identity

`log N! = sum_(n=1)^N log n = sum_(d<=N) Lambda(d) floor(N/d)`.

**Proof.** `log n=sum_(p^k|n) log p=sum_(d|n)Lambda(d)` by prime factorization. Summing over `n<=N`, exchange the FINITE divisor pairs `(d,n)` and count the multiples of each `d` to obtain `floor(N/d)`. Reindex by prime powers:

`log N! = sum_(p<=N) log p * sum_(k>=1,p^k<=N) floor(N/p^k)`.

The rightmost integer is `v_p(N!)` by Legendre's factorial formula. All sums are finite **for each N**; the *proof* covers every N with one finite universal argument, even though there are infinitely many primes overall. The engine stores each coefficient of the formal symbols `log(p)` as an exact integer, computes both sides by independent algorithms, and verifies cutoff N=1..204. No floating equality of logarithms is used. A fake independent `Lambda(6)=log 6` adds `floor(N/6)log 6`, a nonzero model coupling defect for all N>=6.

This is a concrete causal/structural coupling: additive successor path length, multiplicative prime-power jets, valuation geometry and Archimedean log coordinates are tied by one universal source theorem. It is **not** sufficient to prove the prime number theorem or RH. Source primality is established arithmetically, not by naming a composite residue-clock as a new prime place.

## 5. Renormalization sandwich and Euler–Mascheroni — GMS-06

For the ordinary harmonic successor law, `H_N-log N -> gamma` (DLMF 5.2.3). For the true von Mangoldt current,

`sum_(n<=X) Lambda(n)/n - log X -> -gamma`.

The latter is a known theorem requiring genuine prime-distribution input (for example the prime number theorem plus a Tauberian argument, or a suitable analytic contour estimate), NOT a consequence of the finite graph's local observations or of the truncated Laurent series by itself. Distinguish *finite proof with universal assumptions* from *finite data*. The exact finite identity in §4 and the positive residual in §5a give a bridge between additive and multiplicative laws, while the PNT/analytic theorem supplies the extra global asymptotic information.

Independently, the **formal Laurent germ** `Z(1+z)=1/z+c+d z+O(z²)` satisfies

`-Z'(1+z)/Z(1+z)=1/z-c+(c²-2d)z+O(z²)`.

This is verified exactly for all rational coefficient probes. For the AUTHENTIC zeta function, `c=gamma` by its classical Laurent expansion (DLMF 25.2.4), giving opposite constant terms without reading zeros. It is a local analytic coefficient identity; to promote it to the *unsmoothed prime partial-sum limit* still needs the stronger global prime-distribution theorem.

**Scale/gauge defect:** replacing `log N` by `log(aN)` shifts the ordinary finite part by `-log a`; replacing the prime cutoff normalization by `log(bX)` shifts its finite part by `-log b`. Thus the matched sum of constants becomes `-log(ab)` unless `ab=1`. No arbitrary regularization is a carrier-invariant scalar. An observer must certify a common cutoff convention and source law before calling the paired finite part a meaningful defect. The program evaluates finite differences as **numerical diagnostics only**, with an explicit false `global_limit_certified` status.

## 5a. A sharpened *positive finite quantization defect* — GMS-08

The exact factorial/prime-floor identity supports a further **nonnegative scalar**, now independently implemented:

`D_N = sum_(n<=N) Lambda(n)/n - log(N!)/N
     = (1/N) sum_(n<=N) Lambda(n) {N/n} >= 0`.

**Proof (every finite N, classical):** divide `log(N!)=sum_(n<=N) Lambda(n) floor(N/n)` by N. Subtract this from `sum Lambda(n)/n` and use `1/n-floor(N/n)/N={N/n}/N`. Each `Lambda(n)>=0`; the fractional part `{N/n}` lies in [0,1), so the scalar is nonnegative. Equality and sign are completely source-derived, and all sums are finite. The **integer coefficient** of each symbol log(p) is replaced by the exact rational residual `sum_(k>=1,p^k<=N) [1/p^k-floor(N/p^k)/N]`. The code compares this against an independently computed sum of Euclidean residues `sum_k (N mod p^k)/(N*p^k)` and tests all cutoffs N=1..259.

At N=6 the exact coefficient vector is `(log2)/12 + 0*(log3) + (log5)/30`. Its nonnegativity does not rely on any floating-point approximation or even knowing Euler gamma.

**Asymptotic bridge (CLASSICAL / IMPORTED, nontrivial):** Stirling gives `log(N!)/N=log N-1+o(1)`. Prime-distribution results give `sum_(n<=N) Lambda(n)/n=log N-gamma+o(1)`. Thus `D_N->1-gamma` and in particular `0<gamma<=1`. This does not follow from the finite formula alone; one must prove the asymptotic hypotheses (e.g. via PNT and a valid summatory theorem). The finite proof of the *identity* and the finite proof of the *global asymptotic* are distinct mathematical objects.

**Sign firewall:** `D_N>=0` is a one-dimensional scalar floor/continuum bias. It is **not** the Weil quadratic form and provides no operator inequality. A scalar-positive artifact cannot be identified with the authentic Weil form without an actual source-preserving, test-space-correct pairing map. Indeed E38 and the fake-6 Suzuki counterexample defeat this shortcut. The numerical value `1-gamma` depends on the matching cutoff normalization; changing the unit convention changes finite parts.

## 5b. Global meaning of the scalar defect: a PNT-equivalent limit — GMS-09

**Classical analytical theorem, not an executable finite-data inference:** for authentic von Mangoldt Lambda(n) and the source-defined `D_N` in §5a, the following are equivalent:

1. The prime number theorem `psi(x)=sum_(n<=x) Lambda(n) ~ x`.
2. The limit `lim_(N->infinity) D_N` exists as a finite real number.
3. `D_N -> 1-gamma`.

The nontrivial implication **PNT ⇒ (3)** invokes the established von Mangoldt asymptotic `A(x)=sum_(n<=x) Lambda(n)/n = log x-gamma+o(1)` together with Stirling; this theorem is *not* derived from any finite sample or by the code. For **(2) ⇒ PNT**, Stirling and the exact definition show `A(x)=log x+C+o(1)` for some finite `C`, first at integer x and then at arbitrary real x by taking the floor.

Write `psi(x)=sum_(n<=x) Lambda(n)`. Since all Lambda(n) are nonnegative, for each fixed `h>1`,

`x [A(hx)-A(x)] <= psi(hx)-psi(x) <= h x [A(hx)-A(x)]`.

But `A(hx)-A(x)=log h+o(1)` as x tends to infinity. Partition `[x0,x]` into geometric intervals of ratio h and sum the preceding inequalities; discarding the fixed finite initial segment gives

`log(h)/(h-1) <= liminf_(x->infinity) psi(x)/x
 <= limsup_(x->infinity) psi(x)/x <= h log(h)/(h-1)`.

Let `h` decrease to 1: both extremal bounds approach 1, so `psi(x)~x`. Thus **convergence of the exact SUCC quantization defect itself** encodes prime-number-theorem-strength asymptotic information; merely observing a finite sequence of positive `D_N` does not demonstrate that convergence.

This is the clearest distinction between *an infinitely quantified conclusion with a finite proof* and *a conclusion inferred from finitely many observations*. It identifies the additional source theorem that the model graph must carry. It is **not equivalent to RH**: PNT is already proved and is weaker than RH. It is also one scalar limit, not the operator positivity of the Weil distribution.

**Literature:** classical PNT / von Mangoldt asymptotic as traced to de la Vallée Poussin in the Max Planck mathematics preprint (2006/150, §proof), the DLMF Laurent coefficient at the zeta pole, and discussions of the PNT-equivalence on MathOverflow (question 95743). The easy geometric-interval converse is explicitly derived above, not attributed as new.

## 6. Why this does not close Weil positivity — GMS-07

Existing SUCC has:
- PR #70, a source-specific positive Gamma Markov bath and first-prime *sub-form* domination. The negative scalar, indefinite pole pairing and other prime terms remain.
- PRs #71–72, a source-derived SIGNED Weil distribution and completed analytic zeta representation, with analytic approximation bounds; neither establishes positivity.
- PRs #73–74, global theta/character analytic envelopes and partial zero-bound instruments.
- PR #75, an IdealHard all-test lower-bound contract and generic finite-observer hidden-negative-direction countermodel.

The new category graph can decide **finite-type source targets** and symbolically certify certain infinite identities. It does NOT show that Weil's all-test nonnegativity is continuous as a finite-discrete source target or invariant under arbitrary reduced source chart functors. For example, in the norm-continuous compact parameter family `A_t=I−2t |e_1><e_1|`, `t∈[0,1]`, the predicate `A_t>=0` is true iff `t<=1/2`, not continuous as a map to discrete {yes,no}. The compactness finite-target theorem therefore does not apply to generic global signs. Algebraic/dynamical coercivity must be established from authentic arithmetic, not stipulated.

**Next actual RH-facing theorem:** construct a source-first, all-test inequality on the authentic signed finite Gamma-Weil approximants `Q_J` with `Q_J(v,v)>=-eta_J ||v||²_H¹` and `eta_J->0` for every compact interval; or show that a nontrivial source-derived positive object is IDENTIFIED with `Q_W` on the full test domain with an explicit norm error. Include prime powers, one Gamma, poles, half-density, conductor, fake-composite 6, χ4 and matched non-Euler controls. If the certificate assumes its own sign, label it circular. We have not proved such an inequality.

## 7. Reproducibility and claim status

Files: `observational_succ/global_model_sandwich.py`; `tests/test_global_model_sandwich.py`; `scripts/global_model_sandwich_probe.py`; frozen `research/2026-10-14/GLOBAL_MODEL_SANDWICH_RECEIPT.json`; ledger `docs/CLAIM_SUPPLEMENT_GLOBAL_MODEL_SANDWICH.md`; dedicated CI workflow. Existing archival sources and main are unchanged.

Local exact stdlib tests check decoder factorization, source/epoch and edge naturality, exhaustive three-source matrices, independent randomized context minimality, rational global polynomial identity, symmetric off-line polynomial mutants, exact prime-power factorial coupling and fake-six controls, Laurent-germ cancellation, and noncompact parity aliases. The compactness theorem, complex identity theorem, PNT and Weil criterion are mathematical imports and do not become Lean proofs because these exact tests pass. Scholarly originality unverified.

**Primary references:** NIST DLMF §§5.2, 25.2 (Laurent and Euler constant), 25.4 (functional equation), 27.4 (Dirichlet series); classical Stone/profinite compactness, CRT/Legendre factorial identities; SUCC VOYAGER, NO-GHOST and E38/IdealHard sources. [Suzuki 2023, §3.2](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785) states the completed Weil positivity criterion. The number-theoretic prime-sum constant can be derived from PNT via elementary summatory-function methods (see Daniel Fischer's 2018 mathematical derivation on MSE) or from a suitably justified analytic contour argument; it is not a theorem proved by this repo module.
