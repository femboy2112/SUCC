# Source collision entropy — scoped claim supplement

**Namespace:** SCE (research-only). **Date:** 2026-10-24.
**Authority:** explicit paper proofs plus finite exact verification; no new Lean declarations.
**π normality: OPEN. π independence: NOT ESTABLISHED. RH: OPEN. Scholarly novelty: UNVERIFIED.**

The complete domains, quantifiers, proofs, source hashes, countermodels, and next
probe are in [the dossier](../research/2026-10-24/PI_SOURCE_COLLISION_ENTROPY.md).
No entry here installs a new kernel-certified theorem.

| ID | Statement | Earned status and boundary |
|---|---|---|
| SCE-01 | For the full Poisson kernel, Haar convergence, energy minimum, subquadratic positive regret, and subquadratic minimum-relative regret are equivalent; sharp potential constant is 2 | PROVED PAPER. Corrects the alleged asymptotic strengthening in PGM-05/10; no π estimate |
| SCE-02 | Finite block KL deficit is at most log collision divided by floor(depth/block length), plus explicit endpoint entropy error | PROVED PAPER using classical entropy inequalities. Applies to consecutive windows; no all-horizon source estimate |
| SCE-03 | Predetermined logarithmic-depth subpower collision control is strictly stronger than normality | PROVED PAPER with normal de Bruijn-repeat countermodel. A source-adapted slow schedule would lose this strictness |
| SCE-04 | Authentic positive BBP tail displaces each phase by less than the stated beta bound; subcell forward displacement changes cell collision energy by at most factor 2 | PROVED PAPER, factor sharp; exact Machin and carry controls. Does not assume avoidance of boundaries |
| SCE-05 | The full p-free complementary phase admits exact relative-Galois close-pair upper/lower bounds; scaled average tends to 2 when M→∞ and M=o(order) | PROVED PAPER. Uniform in complement, but averaged over embeddings; no selected-a=1 estimate |
| SCE-06 | The number of primes with ord_p(16) <= sqrt(p)/log p is O(X/log^3 X); good 1 mod 8 primes remain relatively dense | PROVED PAPER elementary product bound plus CLASSICAL fixed-modulus PNT. No RH/Artin hypothesis |
| SCE-07 | Selected BBP first-window scaled collisions p^{o(1)} at the fixed c=2/5 scale imply binary normality of π | PROVED CONDITIONAL. The selected estimate is UNVERIFIED; decimal/absolute normality not implied |
| SCE-08 | A p-free complementary counterfeit can align every selected phase while the averaged theorem survives | PROVED PAPER / exact finite refutation of local-only selection. Counterfeit is not the authentic BBP source |
| SCE-09 | Passing to a Galois conjugate may cost log(order)+log2 cell entropy | PROVED PAPER. Makes average-to-selected inference vacuous at the proved averaging scale |
| SCE-10 | Finite digit observations cannot distinguish all normal/nonnormal computable extensions; general normality decision has published effective Pi^0_3 hardness | Elementary proof plus CLASSICAL attributed theorem. No independence result for π |
| SCE-F01 | Selected p=97,M=16 scaled close pairs 80/27 exceed Galois mean 4615/1944 | VERIFIED FINITE in exact Fractions. Refutes selected<=average, not subpower asymptotics |

## Reproduction

```sh
python -m unittest discover -s tests -p 'test_pi_source_collision.py' -v
python scripts/pi_source_collision_probe.py --output /tmp/pi-source-collision.json
cmp /tmp/pi-source-collision.json research/2026-10-24/PI_SOURCE_COLLISION_RECEIPT.json
python scripts/pi_source_collision_galois_oracle.py
python scripts/pi_source_collision_regret_oracle.py
```

The separate [validation record](../research/2026-10-24/PI_SOURCE_COLLISION_VALIDATION.md)
distinguishes local runs, donor CI, and final-head hosted CI. Do not infer one from another.
