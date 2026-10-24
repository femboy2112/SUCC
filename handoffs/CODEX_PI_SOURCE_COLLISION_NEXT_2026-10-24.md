# Codex — the selected π source, collision entropy, and the missing arithmetic theorem

## Mission

Perform an execution research round on <https://github.com/femboy2112/SUCC>.
Leah wants a genuine proof of π normality, a rigorous advance toward one, or a
precisely scoped impossibility result. Use the strongest available mathematical
reasoning and available parallel help. Produce proofs, counterexamples, exact
experiments, and committed coherent artifacts; do not stop at a roadmap.

Research commits, pushes, and a draft PR are authorized. Work on a non-main
branch. Claude owns the separately authorized integration/cleanup campaign;
do not merge, delete its branches, or rewrite archival evidence in this research
round. Base on newly consolidated main if the inclusion manifest is verified;
otherwise use the delivered `research/pi-source-collision-entropy-2026-10-24`
head and read other source branches at pinned commits without assuming admission.

## 0. Rebuild the actual frontier

Read `AGENTS.md`, `docs/METHOD.md`, the current main/integration manifest and:

```text
research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md
docs/CLAIM_SUPPLEMENT_PI_SOURCE_COLLISION.md
research/2026-10-24/PI_SOURCE_COLLISION_VALIDATION.md
observational_succ/pi_source_collision.py
scripts/pi_source_collision_probe.py
```

Audit the #252 repaired source, #253 signed transport, #256 prime/p² windows,
#259 twisted cancellation, #260 gauge/missing-prime no-go, #261 Galois selected
outlier, #262 first-carry/no-static-intertwiner, and #264/SCE-01 energy correction.
Resolve actual current heads, tests, theorem types, and source provenance. Do not
infer #256-final ancestry from #258's PR base label. Check Claude preserved both
formerly colliding `bbp_minimal_path` implementations and the MP claim crosswalk.

Re-run the cheap SCE focused tests and source receipt before extending them.
State one exact hole contract: quantifiers, current truth state, proof leverage,
novelty tax, source dependence, cheapest falsifier, and failure product.

## 1. Exact primary target: selected collision amplification

The authentic recurrence is

```text
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), n>=1
y_0=0, y_n={16*y_(n-1)+r(n)}
x_j={16^j*pi}={y_(j+1)+t_(j+1)}
0<t_n<1/((8n+1)*(8n+2)).
```

For a good prime `p=8u+1`, let `L=ord_p(16)>sqrt(p)/log(p)`, `Delta=3u`,
`d=floor((2/5)*log_16(p))`, and `M=16^d`. The desired bound is

```text
K_p(1) = (M/Delta^2) * #{(s,t)<Delta:
          circle_distance(y_(u+1+s), y_(u+1+t)) <= 1/M}
       = p^(o(1)).
```

Meaning: every epsilon>0 eventually gives K_p(1)<=p^epsilon on ALL good primes,
or on an independently proved relatively dense sufficient subfamily. A bound
`C*(log p)^A` would settle this target. One fixed exponent saving is partial
progress and does not establish normality.

**Already proved in the dossier:**

1. Positive Poisson regret and minimum-relative regret are equivalent to normality.
2. Growing-depth collision entropy controls every fixed block law by an explicit
   finite KL inequality. A fixed logarithmic-depth subpower bound is stronger than
   normality; an explicit normal de Bruijn-repeat sequence fails it.
3. Positive subcell BBP source tails change cell collision energy by at most a
   sharp factor 2, without assuming absence of carries or boundary hits.
4. The full relative-Galois family is `z_t(a)=4*a*16^t/p+w_t`, with the entire
   authenticated p-free complement retained. Its mean scaled close-pair count
   tends to exactly 2 whenever M tends to infinity and M=o(L). This uses
   elementary grid counting, no BGK.
5. Only O(X/log^3 X) primes fail L>sqrt(p)/log p. The remaining 1 mod 8 primes
   are relatively dense by classical PNT in a fixed arithmetic progression.
6. The selected target above therefore implies base-16 and binary normality of π.

**Unpaid step:** exclude polynomial collision excess at the ACTUAL embedding a=1.
The average does not do that. This is the principal research target, not a solved
theorem waiting for better notation.

## 2. Attack with complementary methods, preserving the source

Use at most the available safe concurrency. A useful division is:

- **Arithmetic constructor:** derive exact pair-difference/carry formulas and
  seek an incidence, sieve, renewal, or recurrence bound for the authentic
  rational states. Count within the polynomial-scale real arc; denominator
  nonvanishing at an exponentially fine rational grid is insufficient. Separate
  repeated local p-phases from genuinely different ones, retaining all other
  prime powers and real phase alignment. Try to prove a first quantitative saving,
  then identify what is needed to improve it to subpower.
- **Orthogonal translator:** investigate conditional block entropy, multi-prime
  conditioning, or a source-dependent transfer operator that can bound actual
  concentration. Prove any source-to-observer map preserves the quantities used.
  Compare to the source-specific signed high-mode route of #259/#261; a failure
  of the stronger collision criterion need not kill normality or that route.
- **Adversary/formal checker:** attack the proposed estimate with source-preserving
  mutations, independently implement finite witnesses, audit quantifiers and
  prove the strongest elementary lemmas in Lean where the existing environment
  supports it. Do not label imported paper estimates kernel-checked.
- **Principal:** maintain the source dependency graph, do an independent proof
  audit, choose the next discriminator, and integrate only verified results.

Research primary literature before relying on external theorems: BBP and
Bailey–Crandall source dynamics, hot-spot criteria, entropy/finite-state
normality, incomplete sums and incidence estimates. Match every hypothesis,
constant, and range. Do not assume their rational-forcing Hypothesis A.

## 3. Mandatory hostile controls and failed shortcuts

- Exact selected collision outlier: p=97, M=16 gives 80/27, while the Galois mean
  is 4615/1944. Selected<=average is false.
- A p-free complement can be chosen to align every selected phase in one cell.
  That countermodel changes the full BBP source. The new estimate must use the
  authenticated recurrence/initial condition beyond p-freeness.
- A Galois translate may add log(L)+log(2) cell entropy. In the averaging regime
  M=o(L), this can explain all of its apparent genericity. Rational-translation
  invariance does not commute automatically with p-dependent observation windows.
- Omitting identical local p-phases gives a false bound: 1/16 versus actual 1/2
  in the exact p=17 zero-complement mutation.
- Retain diagonal pairs, cell carries, all source primes, source-tail errors,
  correct CRT inverse phases, and the distinction between index poles and phases.
- Near-minimal fixed-radius Poisson energy, complete Hankel positivity, a short
  generating program, a.e. normality, and finite cyclotomic symmetry do not select π.
- The positive-regret target is an equivalence. Renaming it is not a proof step.
- A fixed normal logarithmic-scale collision countermodel must remain in the
  test/proof dossier so failure of this sufficient route is not called nonnormality.

Pre-register fresh source windows and counterfeit families before tuning a
conjecture. Use exact rational arithmetic or certified intervals for any decisive
finite claim. Preserve raw receipts and source hashes. No fit can validate itself.

## 4. Stop rules and useful failure products

Continue a line only if it proves a new source-specific statement, produces a
counterexample, improves a quantified bound, or isolates a sharper dependency.
If all routes merely restate Weyl/energy/normality, explicitly pay the novelty tax
and change the object or observable. Never call failed search an impossibility proof.

Useful negative outcomes include: an exact lower bound showing the prescribed
collision scale is too strong, a no-go theorem for a stated compression grammar,
a sharp entropy cost of a quotient, or a source-class separation theorem. A new
counterfeit outside the actual source class cannot by itself refute π normality.

An independence branch must name a formal theory T and an actual metatheoretic
route concerning π itself. General Pi^0_3 hardness or finite-observer inability
is already known and does not supply such a route. Do not spend the round
reproving general undecidability and presenting it as π being unknowable.

## 5. Delivery and CI discipline

Leave explicit lemmas/proofs, a claim supplement, executable calibrated probes,
fresh holdouts, source-hashed receipts, a failed-route ledger, primary references,
and the exact next hole. Preserve the original evidence and previous failed runs.
Use readable GitHub math and plain-language explanations alongside formal detail.

Run focused tests while developing. Run the required full repository gates once
on the finished coherent candidate, with the importable environment and declared
dependencies. Rebuild changed formal artifacts serially if memory requires it.
Batch commits/pushes to avoid needless CI cascades. Open a draft PR, inspect the
final-head hosted checks, and distinguish completed, failed, canceled, and pending
runs. State whether tested merge and delivered head have identical trees.

Report separately: actual theorem progress, conditional reductions, finite
observations, counterexamples, and unresolved source hypotheses. State base
coverage explicitly: binary/hexadecimal is not decimal or absolute normality.
End with the next verdict-changing mathematical probe, not a claim that a finite
experiment has settled the infinite theorem.
