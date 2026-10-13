# Auditor D: provenance, source identity, and honest execution accounting

Executor `/root/arithmetic`, separate provenance pass in `audit_d`, branch
`research/cambrian-audit-d-2026-10-13`, frozen integration snapshot
`7af4c24284c870942e0140c2bbffdc95302aca3d`. The auditor does not independently
review its own E mathematics. Receipt integrity checks that include E confer
no additional proof authority on E's results.

Questions were frozen before the audit: archive/ledger preservation; original
workers versus dependent cherry-picks; first-pass chronology; source/action/
receipt identity and correlations; truthful 36-plus-eight assignment counts;
runtime metadata exclusions; and EOS PR45/D20 overlap without double credit.

**Verdict:** frozen source preservation, worker patch identity, declared-source
controls, and 36-exploration accounting pass. One draft aggregate-verifier gap
was identified: A/C artifact hashes were stored separately from their math
receipts and therefore were not checked by simple receipt replay. A fresh inert
source mutation demonstrates the gap. The principal was asked to add those
stored hash contracts before final integration verification. Eight-audit
completion remains a final-manifest obligation; this frozen snapshot contains
A/B audits, with D in progress and the others staged outside it.

## Archive and historical ledger preservation

Ran `python scripts/verify_provenance.py`: **72 items**, comprising 17
byte-identical research archives and 55 mechanically namespaced imports,
match the immutable manifest for originating `FuckingRH` commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`.

`git diff 5eb09e7... 7af4c24... -- provenance docs/CLAIM_LEDGER.md` is empty.
The whole ledger is byte-identical at these two frozen commits; its historical
rows contain exactly O1 through O638, with no holes. The root's current draft
ledger was additionally inspected: all O1–O638 rows still match exactly.
That draft inspection is explicitly provisional and is not a hash attestation
of uncommitted final integration files.

The provenance verifier certifies identity against the frozen import manifest;
it does not prove theorem correctness or physically authenticate an instrument.
This audit did not freshly reconstruct the entire originating remote RH tree.

Fresh read-only `git ls-remote origin` succeeded and returned:

| Ref | Observed SHA |
|---|---|
| main | `52d2c02b85b246aec67160260ac06bb1da33645e` |
| PR48 Voyager research tip | `5eb09e7cba36ec01b8f9d6834b78b5766fd93935` |
| PR45 evolutionary tip | `b2774ca485db4b5b4f7ce92e535220352fb3af2f` |

These agree with the campaign baseline. The raw output and exit code are
preserved in `CAMBRIAN_AUDIT_D_RECEIPT.json`. This is remote-ref verification,
not a new final-head GitHub CI result.

## Six real workers, six groups of six investigations

Every original worker commit has the identical parent
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. For each original/integration pair,
the audit checked identical changed paths, every resulting Git blob, and
stable patch ID. The full SHA and blob maps are frozen in the receipt.

| Cluster | Original worker commit | Integration cherry-pick |
|---|---|---|
| A | `5677e9c73096c05ef05cf49a9a119447d5c601f2` | `01bf38fb282872cfe28362321809b30ea9f1b3f9` |
| B | `a71b8b9053ee81a67be2ed78c133a6c61e6766dd` | `fb3499dfb6da9bd491bf89d01abe9de716b5d7b5` |
| C | `906de6f450b05d8be7cd4c8f3a0218f8a2392fe5` | `c53588bf145e8ad09ffdd9acd5b5dc8262969994` |
| D | `810128e8fdd1f32a17852d828ee16e4b7ffb50f3` | `6657950fc9275de03bfa68c864c73c15b1274380` |
| E | `c2c18c3ed638478448497fb6892a747f67ee6f9b` | `5d34d3bd19c74b90bdff2e0fb962c8332c18f881` |
| F | `21ef59994f11d488a31632f731f4e4d7d9adbc77` | `6fc5ae9f1a92abbab259b37440aefed23ee04e92` |

These are **six research workers, 36 executed investigations**. Original and
cherry-picked commits are the same discoveries and must be counted once.
The six groups' recorded assignment IDs exhaust 1–36 with no duplicates.
An executed investigation can conclude conditional, unverified, or an access
gap; assignment execution does not imply the moonshot was achieved.

The older main/PR40–48 stack likewise consists of dependent checkpoints.
All workers shared those source premises and the same model family; passing
separate implementations is useful triangulation but not six blind external
referees. Eight hostile audit **assignments** are staged within the real slot
limit. At this audit's frozen snapshot only A/B are integrated; other audit
branches having been created is not proof that those audits ran. The final
manifest may mark all eight executed only after their actual outputs land.

## First-pass chronology and its limits

The record supports an in-session freeze before cross-cluster conclusions:
workers sent initial hypotheses to the principal and/or preserved first-pass
records. A's `CAMBRIAN_A_FIRST_PASS.json` contains first verdicts as well as
rivals; B's hypothesis file declares pre-computation timing; D and F explicitly
describe messages preceding cross-pollination. C records its initial contract;
E's first message is also part of the session record.

The first-pass files generally entered Git in the same commit as final source
and outputs. Their existence is not an independently timestamped preregistration
commit and cannot alone prove pre-experiment blindness. The root stochastic
dossier explicitly says its dossier was written after the initial derivation
and code, rather than claiming a blinded precommit. This honesty should be
retained in the aggregate campaign language: **pre-cross-pollination in-session
freeze**, with the shared-context and retrospective-file boundary visible.

## Source identity, actions, receipts, and correlations

Fresh controls reject source-ID mismatch, basis mismatch, backward epoch,
unknown receipt alphabet member, and a universal observer filter on an
incomplete declared source. Separate source-changing regression suites passed:
8 stochastic tests, 16 A foundation tests, and 28 F closure tests.

The equal-marginal/full-support correlation mutant has different joint
report/receipt rows and fails joint descent. This preserves the distinction
between source law, marginal coverage, and coupling. A further control gives
two different kernels identical action/source/basis/epoch labels: both are
valid mathematical inputs, but their row data differ. Hence labels alone do
not authenticate equality of kernels. The complete-source flag certifies the
declared finite mathematical class, not physical exhaustiveness or a measured
source. No real-world action, empirical measurement, calibrated biological
source, or physical source authentication was executed in this campaign.

Same-action names across changes therefore require matching actual source maps
and receipt laws, not mere string equality. Hidden-source-dependent action
selection and same-marginal/different-correlation countermodels are preserved
by the existing stochastic audit. Source labels are a typing aid, not a
cryptographic or scientific provenance oracle.

## Receipt hashes and runtime metadata

The independent audit recomputed **42 recorded hash comparisons over 22
distinct artifacts** (including repeated declarations across receipts).
All pass. Repeated declarations are shared provenance, not additional witnesses.
The root's draft aggregate comparisons intentionally separate:

| Receipt family | Runtime-only excluded fields |
|---|---|
| A | Python version |
| B | provenance Python version |
| C | none |
| D | Python version |
| E | Python version and current invocation HEAD |
| F | none |
| root stochastic | none |

No mathematical coefficient, scope flag, source hash, source-generation rule,
or immutable base SHA is justified for exclusion. E's execution HEAD records
the historical pre-commit invocation; later integration changes that runtime
head even though source bytes remain identical. Its code/probe/test hashes
still need to match. Historical receipts are preserved rather than rewritten
to pretend the old invocation occurred at a later head.

**Calibrated draft gap.** A's source hashes are in
`CAMBRIAN_A_VALIDATION.json.sha256`; C's are in
`CAMBRIAN_C_ASSIGNMENTS.json.artifact_hashes_sha256`. Their ordinary math
receipts do not contain these fields, so math replay alone misses their
stored byte-identity contracts. A temporary copy of the C module with one
appended inert comment produced exactly the same full geometry receipt but
changed its SHA-256 from `f8c1dabd...` to `b1c857a3...`. No original file changed.
Stored hash verification rejects that mutant; mathematical replay alone does
not. This is an evidence-integrity distinction, not a mathematical counterexample.

**Required integration action:** enforce both separate A/C stored hash maps in
the aggregate verifier, or explicitly narrow its claimed hash coverage. The
auditor already checked their current bytes successfully; this gap concerns
future replay enforcement. The principal received the exact contracts and
mutation before the audit commit.

## EOS PR45 and D20: no duplicate discovery or toolchain promotion

Read the actual frozen EOS dossier and claim supplement in `audit_eos` at
`b2774ca485db4b5b4f7ce92e535220352fb3af2f`, rather than relying on a chat summary.
Its merge base with PR48 is precisely PR43
`1cb30a3d92420f1197fc1615a68fb4309c0e036d`.

EO1–EO3/EOS01–04 already establish all-word behavioral equivalence,
obstruction-born prefix experiments, finite strict-refinement termination,
and minimal adequate observer factorization. D20 explicitly labels those
as existing classical EOS mathematics. Its additional scoped work concerns
memory-bit bounds, new authored random graph holdouts, and history-only
observation-table learning with a privileged exact equivalence teacher.
The latter is attributed to the classical Angluin route; it neither invents
its own metagrammar nor replaces exact teacher access with empirical sampling.
These are distinguishable implementation/access developments, not a second
independent discovery of EOS02/03.

EOS uses pinned Lean 4.19 under `formal/obstruction_synthesis`; the integration
uses 4.14. The 4.19 tree is absent from the frozen integration snapshot.
No EOS kernel rerun or automatic authority transfer was performed by this
auditor. Recorded upstream kernel/CI evidence and the local EOS Python subset
remain separate from current integration verification.

## Reproduction and final boundary

```sh
python scripts/cambrian_audit_d_provenance_probe.py --remote --output research/2026-10-13/CAMBRIAN_AUDIT_D_RECEIPT.json
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_cambrian_stochastic_transport.py'
python -m unittest discover -s tests -p 'test_cambrian_a_foundations.py'
python -m unittest discover -s tests -p 'test_cambrian_f_closure.py'
git diff --check
```

All executed checks pass. The probe freezes the original/cherry-pick maps,
source hash checks, assignment counts, source-contract mutants, inert-byte
mutation, raw remote refs, and immutable snapshot scope. The root's draft
files were read as drafts and were not frozen as a final output. The final
manifest, completed audits, comprehensive stored-hash replay, full suite,
formal checks, and final-head CI remain the principal's integration duties.
