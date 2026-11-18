# Operation STEAL THE PROOF — original-source arithmetic and hostile bridge audit

**Research date:** November 17, 2026, America/New_York.
**Branch:** research/pro-pi-normality-full-source-offensive-2026-11-17.
**Base:** 81be6b897ae980b801a3b9de9e22ef81e8360bfb.

## Verdict

This operation proves a quantitative refinement of the authentic four-pole
BBP denominator arithmetic, an exact inverse and sharp stability bound for
the swept Borwein instrument, and stronger counterexamples to proposed
source-to-phase bridges. It does **not** prove the missing winding estimate.

| Target for the literal original source | Verdict |
|---|---|
| Positive terminal-norm / domain-wall density | OPEN |
| Original-source R0 | OPEN |
| Swept-origin Borwein convergence to Haar | OPEN |
| Full base-16 normality of pi | OPEN |

The strongest original-source result is effective prime survival. With
U_n=N_n/Q_n reduced and L_n the LCM of the four native odd denominator lanes,
a born prime p>7 with p^2>8n survives whenever

\[
p^2\ge19\,32^{\lfloor(8n-2)/p\rfloor}.
\]

Consequently all born primes above A n/log n survive eventually for every
A>20 log 2, and log(L_n/Q_n)=O(n/log n). This strengthens the inspected
CG-01 fixed-epsilon survival statement. The inherited rate-6 denominator
growth is credited, not claimed as new.

**Novelty-tax D/E was not attained for the requested normality problem.**
The prime theorem is genuine auxiliary source arithmetic. It does not
rule out low-wall shells for the actual zero-seeded source.

## Proof dossier

- [THEOREMS.md](THEOREMS.md): objects, theorem index, quantifiers and authority.
- [EFFECTIVE_PRIME_SURVIVAL.md](EFFECTIVE_PRIME_SURVIVAL.md): full EPS-01--03 proofs.
- [BORWEIN_INVERSE.md](BORWEIN_INVERSE.md): measure inverse, sharp interval
  discrepancy and original-source finite certificate.
- [BORWEIN_ENERGY_STABILITY.md](BORWEIN_ENERGY_STABILITY.md): sharp fifth-root
  stability for the #663 rational energy, with a direct proof and counterexample
  to every stronger uniform exponent.
- [GAMMA_POSITIVE_SOURCE_SHELL_CLONE.md](GAMMA_POSITIVE_SOURCE_SHELL_CLONE.md):
  positive rational sources with uniformly close all-degree moment forms
  and an empty prescribed terminal wall block.
- [SUPEREXPONENTIAL_LOCKED_SOURCE.md](SUPEREXPONENTIAL_LOCKED_SOURCE.md):
  one fixed radix-locked counterfeit matching every asymptotic coefficient
  and all four finite clock principal parts; an exact moment-cone rejection.
- [CRUCIBLE.md](CRUCIBLE.md): hostile division and the global integer gauge.
- [SOURCE_MAP.md](SOURCE_MAP.md), [SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json):
  pinned dependencies, source heads, common provenance and scope.
- [TESTS.md](TESTS.md), [VALIDATION.md](VALIDATION.md): executed receipts and limits.
- [CLAIM_LEDGER.json](CLAIM_LEDGER.json): no promotion from finite tests to limits.
- [NEXT.md](NEXT.md): the verdict-changing arithmetic obligation.

## Live frontier and reproduction

All remote branch heads were fetched into this isolated checkout. Main
remained at the base above. Open PRs #657--#662 were pinned and inspected;
the newly appearing #663 was also inspected at
16d04ab58e213e75ab47e61a170138196dbcd292 before finishing. Its rational
squared-kernel energy and all-word certificate are credited. No donor
branch was merged. The named Gemini branch was absent from the accessible
remote at both refreshes; no other worktree was modified.

From the repository root:

~~~sh
python -m unittest discover -s tests -p 'test_pro_pi_*.py' -v
python research/2026-11-17/pro_pi_crucible/prime_independent_audit.py
~~~

Paper proofs carry the universal quantifiers. Tests calibrate exact
implementations and reject specified mutations. Same-model reviews are not
external referees. No Lean formalization of these results is claimed.
