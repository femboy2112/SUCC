# DEEPSEEK V4 PRO — OPERATION TILE THE ARITHMETIC CYLINDERS

**MODE: DEEP INDEPENDENT MATHEMATICAL RESEARCH, IMPLEMENTATION, COUNTEREXAMPLES AND PROOF-FORGE. NOT ROADMAP-ONLY.**

Repository: https://github.com/femboy2112/SUCC

**Starting PR:** this draft DeepSeek launchpad, stacked directly on [PR #407](https://github.com/femboy2112/SUCC/pull/407) at authenticated parent `5f05181339ea97a56999ca8b8ab10a2009c6c84d`.

## Mandatory initialization

1. Verify live git heads, checkout, branch, worktree, base ancestry, AGENTS.md, provenance/import manifests and root tests. Read `research/2026-10-30/cylinder_tiling_collision/` completely: `THEOREMS.md`, `CLAIMS.md`, `NEXT.md`, `cylinder_probe.py`, `test_cylinder_probe.py` and validation.
2. Read this branch's `MOVING_SCALE_THEOREM.md`, `HYPOTHESIS_LEDGER.md`, tests and raw logs. Verify MS-01, MS-02 and MS-03 **independently** before treating them as established. Source code is a finite calibration, not a proof of asymptotic inequalities.
3. Inspect PR #405 (selected zero boundary/finite Diophantine slips, full CRT and exact low-slip cylinder union), #398–#401 (prime stroboscope, 6n conductor growth, Gamma all-prime and Gauss), #395 (Stoneham controls), #390–#394 (spacetime and shared-posterior triangles), and #396/#406 (observer choice/COUNT-OUT). Refresh actual heads and do not merge sibling branches silently.
4. Preserve original four-pole source, the exact boundary U_0=0, all carry bits and full complementary CRT phase. Work only in a new non-main research continuation, using draft PRs. Do not merge, publish, force-push or mutate old theorem contracts without explicit authorization.

## Mission

**DERIVE FROM THE AUTHENTIC FOUR-POLE ZERO-SEED ARITHMETIC A NONTRIVIAL UPPER BOUND ON SELECTED PAIR-COLLISION ENERGY, AND USE IT TO ADVANCE TOWARD BASE-16 NORMALITY OF π.**

Our hypothesis: a finite observation triangle extruded in time supplies a path cylinder; superimposing two such triangles gives actual-time pair collisions; tiling arithmetic space with these cylinders produces nonnegative multiscale Walsh/entropy constraints. Prove what this source-specific geometry really restricts. The tiling exists for every possible digit sequence; its mere construction says nothing about normality.

The original BBP recurrence is

```
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
U_0=0, U_n=16U_(n-1)+r(n),
y_n={U_n+T_n}={16^(n-1)pi}.
```

At depth m, with the actual selected word frequency p_(m,N)(w):

```
Q_(m,N)=16^m sum_(|w|=m) p_(m,N)(w)^2,
Q_(m+1,N)-Q_(m,N) = 16^m sum_(v,chi!=1) |sum_a chi(a)p_(m+1,N)(va)|^2.
```

**We need an arithmetic bound on this true selected observable.** The known equalities alone are a coordinate change.

## New executable finite-horizon bridge (MS-01)

For any digit stream, any N and m>=k>=1:

```
||p_(k,N)-uniform_k||_1 <= sqrt( 2 log Q_(m,N) / floor(m/k) ) + 2m/N.
```

This is proved from KL chain rule/superadditivity, Shannon >= Renyi2, Pinsker, and shifted-window boundaries. `Q_(m,N)>=16^m/N` supplies an unavoidable sample floor. This yields the **single moving-depth normality criterion:** there exists m_N→∞ such that `log Q_(m_N,N)=o(m_N)` iff the sequence is base16 normal.

**Original-source sufficient target (MS-03, UNPROVED):** Choose m_N=floor(log_16 N/3). If the **rational exact BBP orbit** has smoothed tent pair-energy

```
log Kcal_(16^(-(m_N-1)),N)({U_n(0)}) = o(m_N),
```

then existing Green-tail/Lipschitz and hard/tent comparison + MS-02 would imply pi normality. Prove that signed arithmetic premise, or establish a demonstrably stronger/achievable substitute. Do not label the implication itself as a proof of the premise.

## Research fronts — execute in parallel only when provenance/methods differ

### Front A — independent proof audit and sharp constants
Reconstruct the KL argument with independent information-theoretic and combinatorial witnesses. Check whether the 2m/N term can be sharpened, and whether max-error, TV or cylinder-conditional variants admit better constants. Test for counterexamples to any proposed strengthening; use exact tiny alphabets and adversarial sequences. Check quantifier orders for moving depth vs N, and sampling floor. Formalize a finite theorem in Lean if the types are stable; don't claim the analytic real-log/sqrt inequality has been formalized if it hasn't.

### Front B — source-selected two-time Fourier correlation
Derive an explicit original-source formula for
`(1/N²) Σ_(i,j) K_m(U_i-U_j)` and use the complete real signed phases rather than independent prime marginals. Explore additive convolution, Poisson summation, Fourier/character completion, Weyl and van der Corput, large sieve with source-correct weights, and multiscale frequency cutoffs. The Fourier kernel is positive but that does not grant cancellation. A breakthrough is a *nontrivial upper bound* on its total nonzero-frequency energy, not another expansion as a sum of squares.

### Front C — context-conditioned Walsh currents
Attack all 15 nontrivial four-bit Walsh characters per prefix context. Preserve literal carry, q=3/q=6 auxiliary selectors as separate layers, and the selected p-adic/real cofiber history. Seek arithmetic inequalities bounding the aggregate squared signed currents through many contexts at once. Test if CRT primes give independent *constraints*, not pretend they are statistically independent. Explicitly compare the same-source coherent seed s=-pi/16.

### Front D — cylinder lattice and symbolic-dynamic geometry
Build exact path-compatible tilings, De Bruijn flow constraints, transfer matrices, inverse limits, path cohomology, Perron-Frobenius/pressure and thermodynamic formalism. Ask whether a *source-imposed restriction* forbids abnormal invariant measures. Reproduce a periodic de Bruijn system that passes every finite depth up to its order and then fails. A graph flow identity that holds for all paths is not selected mixing.

### Front E — Stoneham normality as a positive mechanism
Derive an EFFECTIVE moving-depth collision bound for normal Stoneham constants with conductors 3/5 from their modular stage periods, bounded multiplicity and approximation tails. Test nonnormal conductor2, sparse Kempner, periodic de Bruijn, Champernowne and biased Bernoulli. Determine which truly arithmetic features can transfer to the distributed four-pole BBP forcing. Check that the BBP exact translated grid has size exp(6n+o(n)); small exact-grid transplantation was already ruled out.

### Front F — Gamma/Beta and prime snapshot transport
Recover the four-pole real Gamma cocycle, Morita p-adic affine interpolation (including p=2), full Gross–Koblitz order-eight Gauss units, and selected source 59-jet. Search for a noncentral signed two-time effect on the cylinder collision observable, not a scalar Gamma normalization. Preserve the known Gauss coefficient-fiber mutant c+2t(1,-3,1,1), higher-jet positive mutants, and reflected/null-source obstruction. An identity shared by coherent controls cannot force selected normality.

### Front G — zero boundary and low-slip cylinders
The PR #405 low-slip cylinder union is a *different* kind of cylinder from digit-word cylinders. Construct an exact, typed relation between the two or prove that no claimed relation follows. Attempt to turn a source-derived exclusion of a positive fraction of low-slip windows into a quantitative reduction in time-pair collisions. Preserve the full complementary phase and rational boundary x0. Thin Lebesgue measure doesn't rule out the single authentic point.

### Front H — prime stroboscope, conductor and the cofiber
Use exact p-stroboscopic frames, all four odd-prime residue classes, p^a layers, p19/p73 cancellation, and the authentic sharp log-denominator 6n theorem. Seek a simultaneous **weighted** subgroup bound controlling the full complementary phase. Calibrate with the seven-pole zero-seed null source, p-integral aliases, dyadic exact/eventual circle aliases and the genuine zero boundary. Do not call a Galois average the selected embedding.

### Front I — measure/entropy/energy assembly
Test equivalent sufficient statements in collision entropy, relative entropy, hard/soft tents, Walsh squares, conditional probabilities, and signed cumulants. Determine when controlling a sparse sequence of depths suffices, when a single diagonal m_N suffices, and which quantitative bound gives each fixed-k frequency error. Find strict implications that gain an actual source-bound lemma, not just swap formulations.

### Front J — arithmetic normality via new mathematics
Explore analytical continued fractions, rational periods, symbolic coding for source-forced affine maps, multiplicative ergodic tools with verified assumptions, trace-function sheaves with exact coefficient fields, adelic harmonic analysis, arithmetic spectral gaps, quasi-randomness norms, and renormalization/holonomy. For every candidate, locate the concrete missing hypothesis and devise a test that would distinguish it from a tautology or a false transport. RH may be studied separately if new math demands it; do not assume RH implies normality or reverse.

### Front K — implementation: hostile and genuine independent holdouts
Implement exact `Fraction` source and Green-tail digit certification; use separate common-denominator and independent high-precision implementations. For any measured Q_m,N, report the sampling floor b^m/N and `N/b^m`, exact distinct-word counts, 15 Walsh defects, and proof-calibrated error bars. Include m(N) moving-depth runs with realistic sample ranges. Never extrapolate N=256,m=3 into asymptotics. Keep raw failures and label fitted vs holdout primes/indices. Validate m=2/3 on de Bruijn, Stoneham, sparse digit and coherent source controls.

### Front L — proof assembly and priority
Aim first at *one proven source-selected off-diagonal covariance saving*, or a nontrivial all-horizon bound for a declared family of contexts/prime windows, then quantitatively propagate it to collision entropy with a correct coverage argument. Try to prove MS-03 or a stronger full normality theorem. If blocked, state the weakest exact source-plus-zero-boundary lemma that would settle it and the next falsification instrument. A finished report that only reprints CTC-03/MS-03 is a non-improvement.

## Controls and hard rules

- Authentic zero seed, coherent `-pi/16`, legitimate rational translations and dyadic aliases.
- Positive Gamma-matched and high-jet-matched source mutants, wrong-/same-ratio prime mutants, seven-pole zero-seed null source.
- Published normal Stoneham 3/5 and Champernowne; nonnormal Stoneham2, Kempner, biased product and periodic de Bruijn.
- Both selected full-phase and prime-only control values; no false substitution of independence.
- Exact proofs distinguished from numerical finite instances, classical results, conjectured hypotheses and DARK probe gaps.
- External academic priority not inferred from local independent implementations of the same theory.

Use Claim Ledger statuses **DISCLOSED/PROVED LOCAL, CORROBORATED, OBSERVED FINITE, CONJECTURED, UNVERIFIED, DARK, REFUTED** according to actual evidence. Preserve inherited author naming of the Harmonic/Golden/Euler–Mascheroni triangle, Oily–Macaroni, and SUCC's operational choice construction.

## Mandatory deliverables

1. One or more new *draft* non-main GitHub PRs with proof dossiers, executed reproducible exact code, interval/error bounds, hostile controls, results ledgers, raw logs and source hashes.
2. Actual repo validation, including `scripts/verify_provenance.py`, native `unittest` suite, observer foundations and ordinal probes; report exact-head hosted CI independently.
3. For every substantive source-selected claim: explicit theorem statement, quantifiers, proof, new holdout, countermodel, and link to prior derivations.
4. Priority-ranked next open lemmas, with exactly which observable and source mechanism would change the normality verdict.
5. If a candidate proof is found, hostile independent reconstruction before announcing proof; base-16 normality of π and RH stay OPEN until decisively established.

**FAN OUT. PROBE HARD. KILL FALSE LEMMAS EARLY. COMMIT ONLY VERIFIED GAINS. DO NOT STOP AT ANOTHER BEAUTIFUL TILING. THE GOAL IS A SOURCE-SELECTED ARITHMETIC BOUND.**