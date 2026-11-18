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
growth is credited, not claimed as new. The closing FQR lane-LCM refinement,
credited and corrected in section 8, sharpens the sufficient constant to
A>4 log2+6 using fixed-modulus prime asymptotics.

The same survival bound now gives a joint prime/winding theorem. Preserve
the authentic reduced denominator Q, its residue modulo 16^B, and every
born-prime principal part above A(2B)/log(2B). The compatible terminal
words form an explicit progression with exactly phi(q) members, where
q is the remaining cofactor and log q=O(B/log B). Thus there are only
exp(O(B/log B)) compatible words eventually. This is a quantitative
restriction on shadow freedom, not an exclusion of the authentic low-wall word.
The closing FQR frontier supplies the stronger inventory of all actually
surviving simple primes above sqrt(16B); combining its inventory with our
exact classification gives exactly phi(q^ram) words, at most exp(O(sqrt B)).
The cofactor bound and inventory choice are credited there, not claimed as
an independent survival theorem at the square-root scale.

**Novelty-tax D/E was not attained for the requested normality problem.**
The prime theorem is genuine auxiliary source arithmetic. It does not
rule out low-wall shells for the actual zero-seeded source.

## Proof dossier

- [THEOREMS.md](THEOREMS.md): objects, theorem index, quantifiers and authority.
- [EFFECTIVE_PRIME_SURVIVAL.md](EFFECTIVE_PRIME_SURVIVAL.md): full EPS-01--03 proofs.
- [MESOSCOPIC_CRT_RIGIDITY.md](MESOSCOPIC_CRT_RIGIDITY.md): small remaining
  cofactor, exact signature-to-word classification, and the zero-word criterion.
- [ANC12_EVENTUAL_REPAIR.md](ANC12_EVENTUAL_REPAIR.md): the competing
  denominator claim's exact failure and a proved eventual primitive-CRT repair.
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
- [LATE_FRONTIER_AUDIT.md](LATE_FRONTIER_AUDIT.md): the refreshed #663 and
  newly published adelic branch, exact errors, surviving results and overlap.

## Live frontier and reproduction

All remote branch heads were fetched into this isolated checkout. Main
remained at the base above. Open PRs #657--#662 were pinned and inspected;
the newly appearing #663 was inspected at
16d04ab58e213e75ab47e61a170138196dbcd292 and then at refreshed head
814cfe06999f9083b5c2eee479d21bfb951d724f and the closing constant update
74b9f4806fdfebca4be66e2c5bfdbd9b5fc2273a. Its rational energy, all-word
certificate, block/tree budgets and source-tail hierarchy are credited.
The named Gemini branch was initially absent, then appeared at
97c7433371feca631991a1b8227b656e92e4abcb, then advanced to
9ff8544c799b5e4c8eb1db33127438bc3f221045. Both were audited read-only.
The latter imported our first published commit, an explicit shared-provenance
dependency.
Its Parseval argument also yields energy exponent 1/5; our direct proof,
explicit constant and optimal-exponent counterexample are separately stated.
No donor branch was merged and no other worktree was modified.

The configured mandatory full suite completed: **14,503 tests run,
two skipped because pinned Lean 4.14.0 was unavailable**. The earlier timeout
and baseline import error remain in the receipts. See VALIDATION.md for
the execution boundary and the separately run late-frontier probes.

Published draft: https://github.com/femboy2112/SUCC/pull/664 .

From the repository root:

~~~sh
python -m unittest discover -s tests -p 'test_pro_pi_*.py' -v
python research/2026-11-17/pro_pi_crucible/prime_independent_audit.py
python research/2026-11-17/pro_pi_crucible/crt_signature_probe.py
python research/2026-11-17/pro_pi_crucible/audit_adelic_pinned.py
~~~

Paper proofs carry the universal quantifiers. Tests calibrate exact
implementations and reject specified mutations. Same-model reviews are not
external referees. No Lean formalization of these results is claimed.
