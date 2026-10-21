# Source-bound kernel observations

The combined `mathlib_bridge.yml` job rebuilds the local Mason–Stothers/Fermat
bridge, Cloud Schur and primitive slope proofs in sequence against Lean 4.14.0 and mathlib commit
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. It verifies the official compiler
archive SHA256 and every dependency Git revision. The projects share a single
official mathlib compiled cache. These imported compiler/cache artifacts, the
runner, GitHub's artifact delivery and the audited build scripts belong to the
trusted computing boundary; Python metadata cannot independently authenticate
them. Local theorem outputs are deleted and rebuilt before observation.

`generate.py` obtains each **fully qualified** theorem's actual Lean `Expr` type,
universe parameter names and recursively collected axioms from the built
environment. Every quantified variable, hypothesis and conclusion is in that
expression; English theorem descriptions are not used for equality. Raw Expr
serialization is pinned to this compiler version and is not a claim of stable
cross-version serialization or arbitrary semantic equivalence. The exports also
include ordinary `#check` and `#print axioms` logs. The allowed axiom envelope is
`propext`, `Classical.choice`, `Quot.sound`.

The record binds toolchain, complete manifest files, dependency revisions, local
theorem sources, checker source and workflow by SHA256. Its environment digest is
SHA256 of canonical JSON of exactly `toolchain`, `manifest_rev`, `source_hashes`.
Canonical JSON uses sorted keys, separators `(',', ':')` and UTF-8 with
`ensure_ascii=False`. The theorem's type digest hashes the UTF-8 `type_expr`.
`build` records commit/tree, log hashes and rejected controls. A build record is
generated only after all positive and negative gates pass. A failed rerun removes
the previous success record. The type digest identifies this exact theorem;
specialization or proposition transport requires an additional kernel-checked
theorem and its own admitted export.

## Admission, distinct from generation

A file saying a build succeeded supplies no authority. Neither this script nor
caller-supplied JSON can add an approved digest. A coordinator must inspect the
actual hosted run on the exact commit, its logs, source hashes, axiom envelope,
wrong-source rejection, Schur mutations and slope mutations. Only then may the exact record be
archived as `formal/kernel_audit/admitted/kernel-attestation.json` and its canonical
JSON digest added to the trusted installed `_formal_catalogue.py` through reviewed
repository code. The historical `mathlib_bridge/axiom_audit.json` is retained as
historical metadata and is not admitted evidence.

Until that separate admission occurs the authority layer fails closed at Level C.
CI reports `FORMAL_ADMISSION_PENDING`, even if the Lean build is green. After
admission, `check_admission.py` requires fresh kernel exports to match the admitted
types, environment and sources and authenticates each exact formal reference.
Build commit/log hashes may differ on a subsequent integration commit, while the
checked theorem/source environment must remain identical. Any source/environment
change invalidates the old record and needs a fresh review. The system does not
claim to defend against arbitrary hostile Python running in the same process or
an attacker permitted to rewrite the trusted catalogue/checker.

## Reproduction

1. Install the exact official Lean archive and check SHA256
   `320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`.
2. Run the workflow's targeted `lake exe cache get` command in
   `formal/mathlib_bridge`. Share its `.lake/packages` directory with the
   `formal/cloud_schur/.lake/packages` and `formal/slope_rigidity/.lake/packages`
   symlinks as in that workflow.
3. Run `python3 -m unittest discover -s formal/kernel_audit -p 'test_*.py' -v`.
4. Run `python3 formal/kernel_audit/generate.py --output /tmp/succ-kernel-audit`.
5. Inspect all logs and the unadmitted `kernel-attestation.json`; perform the
   independent admission review described above.

Negative elaboration controls require the expected error (not just a nonzero
process exit). The wrong-source control attempts a degree bound `+2` using a
theorem proving `+1`. The Schur controls replace positive definiteness by
semidefiniteness and change an exact negative quadratic value from `-1` to `1`.
The slope controls remove reducedness and increase the determinant gap by one;
each must produce the expected Lean type mismatch. The nineteen exported
declarations consist of five polynomial, five Schur and nine slope theorems.
Token checks reject proof shortcuts in local theorem sources; transitive axiom
collection independently rejects `sorryAx` and every undeclared axiom. These are
specific negative controls, not a proof that every possible checker defect is
absent. The mathematical claims remain the exported theorems, not RH, integer
abc, binary Goldbach or correctness of an unformalized Python algorithm.

## Main VIII admission transition

PR #211's independently observed slope receipt remains immutable historical
evidence in `formal/slope_rigidity/receipts/`. Its research schema is deliberately
not accepted as Level C authority. The Main VIII generator adds the nine unchanged
slope declarations to the existing ten and rebuilds all three projects. It does
not convert an old JSON file into a successful new build.

Changing this generator and its workflow invalidates the prior ten-declaration
record's source environment. Before the new actual nineteen-declaration record
is reviewed and installed by the coordinator, admission checks are expected to
fail closed. The earlier record and admission remain traceable in Git history;
no historical proof source or observed theorem type is rewritten. The separate
exterior research project is not automatically admitted by this pipeline.
