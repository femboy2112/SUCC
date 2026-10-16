# SUCC-lambda 0.1: a finite, source-indexed calculus of lawful probes

**Date:** 2026-10-16. **Parent:** `main@02fc9f46ad3b914d49df7a658e304d06ed8a6200` (post Carrier -> Tate -> Weil consolidation). **Branch:** `research/succ-lambda-observation-calculus-2026-10-16`. Status: new-to-SUCC executable finite typed system; elementary paper proofs with exact adversarial checks. No Lean theorem or analytic positivity asserted. **RH PROVED: NO.**

## 1. The proposed object (steelman)

The motivating problem is *not* to evaluate a zeta zero or to promote a few finite tests to global positivity. It is to formulate compositional programs whose **observation footprint, lawful source passport, derived data and proof authority remain explicit**. The desired future use is a source-preserving compiler for arithmetic resonance witnesses: a failed RH sign might be detected by a finite program, while any proposed effective early-detection bound must be proved from actual arithmetic, not assumed by the syntax.

We implement a call-by-value, simply typed lambda calculus with de Bruijn variables, immutable source passports `s=(source_id, epoch, basis)`, finite recorded modular atlasses, and exact residue arithmetic. All recorded observation rows are finite and pairwise compatible. An atlas read is **replay of a declared recorded event**, not a new measurement and not a physical authentication.

A judgment is `Gamma |- e : tau ! E`, where `E` is the finite set of potential *primitive recorded reads*. Lambda abstractions carry latent effects:

```
 Gamma,x:sigma |- e : tau ! E
 ------------------------------------- LAM
 Gamma |- (lambda x:sigma. e) : sigma -[E]-> tau ! empty

 Gamma |- f : sigma -[L]-> tau ! Ef     Gamma |- a : sigma ! Ea
 ---------------------------------------------------------------- APP
 Gamma |- f(a) : tau ! (Ef union Ea union L)

 Gamma |- read(n) : Report(s,n) ! {n}

 Gamma |- r : Report(s,m) ! E   n|m
 ---------------------------------- PROJECT
 Gamma |- project(r,n) : Report(s,n) ! E

 Gamma |- r : Report(s,m) ! E   Gamma |- t : Report(s,n) ! F
 -------------------------------------------------------------- CRT
 Gamma |- join(r,t) : Report(s,lcm(m,n)) ! (E union F)
```

`Report(s,n)` cannot be silently joined across sources or epochs. `forget(report)` *explicitly discards source indexing* and returns `Residue(n)`. `succ` and `prime_mul(p)` act only on residue values and do not record new source events; `prime_mul` rejects nonprime generators (multiplication by a composite is representable by successive prime actions, but is not an independent prime jet). `select` only executes its selected branch, while static effect footprints conservatively union both branches. Repeated recorded reads remain repeated replay events; projections and CRT computations add `derived:*` lineage without inserting fictitious observation rows.

This is an embedded typed AST/interpreter written in Python, **not** a text parser or general-purpose theorem prover. The calculus intentionally excludes `fix`, general recursion, oracle access, omega elimination, zero-location inputs, unrestricted source-change coercions, and a constructor purporting to certify completed Weil positivity.

## 2. Scope-correct proofs and checks

**SL-01 [CLASSICAL / PAPER-PROVED, TESTED FINITE].** In the simply typed core, beta substitution is interpreted by lexical closures; a runtime value at a closed ground type has the corresponding checked type, assuming a coherent atlas, available executed reads, and sufficient execution fuel. Primitive arithmetic/CRT constructors preserve their typed carrier. The underlying pure simply typed calculus is strongly normalizing; this Python evaluator additionally imposes finite execution/read-bit budgets. Exhaustion yields `BudgetGap`, never falsehood. The implementation is not a formal proof of the normalization metatheorem.

**SL-02 [PAPER-PROVED; EXACT FINITE CHECK].** If `r mod m` and `t mod n` agree modulo `gcd(m,n)`, their CRT join is the unique residue modulo `lcm(m,n)` satisfying both, and source lineage is retained. The formula uses `k = ((t-r)/g)*(m/g)^(-1) mod (n/g)`, with the modulus-one case treated separately. An unrecorded `read(lcm(m,n))` remains unavailable even when a derived CRT join exists.

**SL-03 [PAPER-PROVED (structural induction); EXACT FINITE CHECK].** Let `e` be a *closed ground-typed term* and `E` its static potential-read set after latent function effects are propagated. If two coherent finite atlasses have the same passport and exactly the same recorded values at each `n in E`, their evaluations agree, provided both executions complete within budget. Proof: induct on typed syntax; the only access to the atlas is `read`, which agrees by assumption; all other constructors are deterministic, lexical `lam/app` preserve the induction hypothesis, and `select` chooses the same branch. `compare_observers` refuses certification if a required recorded value is absent or differs. Function-valued outputs are excluded: an *unapplied closure* may have unexecuted latent reads. Static footprints can overapproximate actual reads (dead branches); an `ACCESS_GAP` from the comparison is not a refutation of extensional equality.

**SL-04 [PAPER-PROVED negative observation theorem].** No fixed finite modulus menu distinguishes all integers. For any finite nonempty menu `M`, let `L=lcm(M)`. The ordinary integers `0` and `L` agree modulo every `m in M`, but differ modulo `L+1`. Thus finite agreement alone has no uniform global *integer identity* certificate. This theorem does not preclude finite proofs of universal properties from arithmetic laws, does not classify RH, and does not say the profinite inverse limit lacks points.

**SL-05 [EXACT FINITE MODEL, not source theorem].** For an explicitly provided rational symmetric finite Gram matrix, `signed_witness` evaluates `v^T G v` using `Fraction` and returns a negative witness only if strictly negative. A nonnegative result from one vector is `NOT_NEGATIVE`, never positive semidefiniteness. The matrix has no authenticated identification with Suzuki/Weil; `proves_rh=False` in every result. Floats, malformed or nonsymmetric matrices, and zero vectors are rejected.

**SL-06 [PAPER-PROVED arithmetic identity; TESTED FINITE].** For any genuine prime `p` and residue class `x mod n`, `prime_mul(p, succ(x)) = succ^p(prime_mul(p,x))` because `p(x+1)=px+p`. This is the modular image of SUCC/FUCC's affine relation, *not* an equality between source events or an operator equivalence on every carrier.

## 3. Adversarial controls and a tested baseline

- **Positive:** nested lambda closures, binder scope, beta application, projection across divisors, coprime/noncoprime CRT, source coherence, and finite negative rational Gram witness.
- **Negative:** fake prime 6, wrong modulus/epoch/basis, incoherent source rows, absent recorded modulus, unbound variables, fake coercion from a read report to an arithmetic source event, mismatched residue carriers, float/bool exactness violation, asymmetric Gram.
- **Null:** a branch that is never executed can still occur in a conservative potential-read footprint. A finite atlas pair can agree on every accessed small modulus and disagree on a larger one.
- **Resource:** exhausted reduction steps or probe-bit budget means `UNRESOLVED`/access failure, not a negative theorem.

`python -m unittest discover -s tests -p 'test_source_lambda.py'` and `python scripts/source_lambda_probe.py` reproduce the checks. The initial implementation passed **31/31 targeted tests** under the local isolated Python environment (not the full SUCC repository); the deterministic script prints explicit `global_completeness_proved:false`, `actual_source_authenticated:false`, `RH_proved:false`. Hosted full CI and import integration must be separately observed at the pushed commit before claiming green.

## 4. Why this is not yet a finite-to-global resonance amplifier

A typed term cannot create information unavailable to its probe/source closure. The pure calculus can reorganize, compose and reveal already represented finite data; it cannot promote a finite negative Gram of an arbitrary model to an authentic RH counterexample. This **data-processing boundary** is a feature: attempting to infer a global sign from a local constant, an auxiliary positive Hilbert Gram, a purely formal Euler product, or a fake prime jet must fail without a new theorem/certificate.

The immediate next upgrade is an *analytic effect type* carrying (1) exact canonical source passport and source hashes, (2) the completed prime-power/Gamma/pole/conductor/half-density contract, (3) a finite radius and rational interval envelope with provable tails, and (4) a separate proof that a resulting exact negative Gram is the restriction of the **unmodified** completed Weil form. This is the missing trusted port to the existing Suzuki Schur program. The alternative route is a source-specific effective bound on the finite observation/response depth. Neither theorem is implemented here.

## 5. Dependency and research status

The calculus is a freestanding finite observation language, layered **beneath** the completed Weil/Suzuki machinery. It inherits the project's epistemic distinctions from `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/METHOD.md`, finite modular source work and the source-indexed no-ghost program. No archived source or `main` history has been rewritten. SUCC's #131 carrier/Tate/Weil reconstruction provides the arithmetic target; #135/#137 on separate research branches provide potential future Schur/certificate adapters. The present files do not modify those branches or claim their analytic theorems were kernel-proved. Academic priority for ordinary STLC/CRT is classical; the contribution here is a source-indexed executable integration and a precise trust boundary. **RH remains open.**
