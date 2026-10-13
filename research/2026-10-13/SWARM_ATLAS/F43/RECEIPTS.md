# F43 execution and provenance receipts

Authority: worktree `/home/leah/succ_lab/swm-f43`, branch
`research/swm-f43-2026-10-13`, clean initial parent
`5eb09e7cba36ec01b8f9d6834b78b5766fd93935`. Remote:
`git@github.com:femboy2112/SUCC.git`. These are new native research artifacts.

Read-only authority inspected: `AGENTS.md`, `docs/METHOD.md`,
`provenance/IMPORT_MANIFEST.json`, and shared `SWARM_ATLAS/PROTOCOL.md`.
The manifest records imported origin
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; none of these artifacts are imported
paths. Relevant native modules inspected:
`eodcs_multi_action_source.py`, `eodcs_evolutionary_discovery.py`,
`eodcs_genetic_probe_genesis.py`, `shadow_source_inference.py`,
`eodcs_source_uncertainty.py`, and the opaque boundary demo in
`categorical_repair_synthesis.py`. The queried native source lineages were
`c6bbdf5a4ab3c7c90c1e63d018a3c46cca67a645` and
`a5462ea4ef655bba7dd67fbc16ec048acfb994d1`. No first-generation investigator
dossier, shared registry, existing sealed data, or archival original was read
as evidence for the mathematical result.

The following commands actually ran from the assigned worktree, in this order:

```sh
python research/2026-10-13/SWARM_ATLAS/F43/freeze_sources.py
python research/2026-10-13/SWARM_ATLAS/F43/learn.py
python research/2026-10-13/SWARM_ATLAS/F43/check_once.py
```

All three shell exit codes were **0**. Stage 1 wrote fresh data with training
seed `430013` and holdout seed `430099`; `learner_files_exist_at_freeze=false`.
The manifest preserves exact pre-shuffle carriers, raw-to-opaque labels, and
realized row/menu order. Stage 2 selected all 105 rewrites without reading
holdout data. Stage 3 created its exclusive execution-start guard before
reading/evaluating the holdout. There was **one actual holdout evaluation**, no
replay or repair; hashing the file and parsing it are two raw reads within that
one evaluation. The guard prevents another invocation from evaluating it again.
The checker validated all selected rules on training with a distinct map-composition
interpreter before touching the holdout. Its maximum temporary map size was
7,865 integer cells, source cap 128 states/four actions, assignment cap 64, and
actual elapsed time 0.118388 seconds against a declared 25-second result gate.

| Table | Role fixed before selection | States/actions | Exact instance checks | Failed equations / instances |
|---|---|---|---|---|
| train 0 | fit | 5 / 2 | 4,200 | 0 / 0 |
| train 1 | fit | 9 / 3 | 25,515 | 0 / 0 |
| holdout 0 | transfer | 65 / 4 | 436,800 | 0 / 0 |
| holdout 1 | transfer | 8 / 4 | 53,760 | 0 / 0 |
| holdout 2 | mismatch | 16 / 3 | 45,360 | 42 / 10,944 |

Every check is an equation × starting state × assignment to three primitive
action variables. Failure rows include exact opaque starts, assigned actions,
equations, and unequal endpoints. All integers/strings are exact; no numerical
precision or probabilistic success claim occurs.

SHA-256 values below were obtained with `sha256sum` (exit **0**) after the
three stages. These sources/receipts were not edited afterward.

| Artifact | SHA-256 |
|---|---|
| `freeze_sources.py` | `29bf24329a9492a7f31e396fda69192ea4b4535e10c7652b9d86efeb660774d5` |
| `learn.py` | `e8a18d243ebf3b214b33dcf8ed8a012e6d5ae8d73209a8f4e21f1f5b232759b6` |
| `check_once.py` | `f98d947936b65cda3def96beb2afb5002a0ccf25992ea3b04bc9ae3859e55bea` |
| `training.json` | `34452d4fc64080ebe061fd643e5077b6e353bd803186ca9a81283753ec15c943` |
| `holdout.json` | `24eafe4c90923484417f80c4893def28e64cae9575002f03f2c48ec9e1ce83ad` |
| `source_manifest.json` | `e209611052e49462861082f838a78884c78c8ed874158025cb6317f878920246` |
| `freeze_receipt.json` | `42b1abd5b4586172343203a57f49cdb75e7f68d6c30bfe52430e6bec293f3179` |
| `selected_laws.json` | `90958e14a8a16e10cea130557598fc6cb1c2188bf9110b2f9b5f9e949d26a97f` |
| `holdout_execution_started.json` | `3f1c5c881badf8536af958515a2829b9204e788c6494102fcc3d4f199690993f` |
| `witness.json` | `98b7d92f709d1e7348614ab3a49cb624759285a31a094a923d2d859f134ddd54` |
| `DOSSIER.md` | `363371d3b72fa30d61170b9ec861c7bf619b14b542210f05c8c52cd0f4ec7857` |

Reproduction requires a **new disposable directory** containing the three scripts,
then running the same stage sequence. Do not overwrite or re-evaluate this
sealed run. Source and training data reproduce deterministically; elapsed times
and derived receipt-file hashes can vary. Full repository validation is owned
by the principal integration task; this investigator ran only the focused exact
probes. No compiler, child agent, push, merge, release, or default change occurred.
