# Validation and limits

Research branch `research/hannibal-source-collision-2026-11-02` starts exactly
at `1478b51cf1370411aea6ec42c09d080598384528`. Live PR #476 was checked twice
and had not advanced. PR #472 head `85189e389ca1568636a7fedb7b2d6268b8eae447`
was fetched read-only and verified NOT to be an ancestor. No merge occurred.
`SOURCE_PINS.json` preserves the parent blobs and SHA256 hashes; `PR_HEADS.json`
preserves the live antecedent metadata. The original checkout and other
worktrees were left intact. This dossier and its one test file are additions.

The initial local checkout did not contain the campaign object. A read via
the GitHub connector recovered the complete handoff; a subsequent ordinary
git fetch succeeded. The earlier campaign's DNS limitation did not persist.
Only root AGENTS.md applies. The import manifest and governing method were
read; frozen originals and historical claim contracts remain unchanged.

## Executed gates

| Gate | Result |
|---|---|
| Campaign baseline test_weyl_mirror_campaign.py | 23/23 PASS |
| New test_hannibal_source.py | 21/21 PASS |
| Combined new + relevant ancestor tests | 141/141 PASS, zero skips |
| compileall on new modules/test | PASS |
| Original full-modulus source through 131071 | Completed, six exact histogram vectors |
| Small exact receipt generation | Completed: mirror, matching, annulus, witness receipts |
| Full native suite, uninstalled checkout invocation | 11213 run, 11212 pass, one subprocess import error |
| Same failure on clean pinned parent | Reproduced: 11 tests, one identical error |
| Corrected import-path targeted retest | 11/11 PASS |
| Full native rerun with checkout PYTHONPATH | 11234/11234 PASS, zero skips, 1330.271 seconds |
| Odd-register large replay | All six vectors and every literal-carry digest agree |
| Final-byte full-modulus large receipt replay | PASS; before/after executable hashes identical |
| New small receipts / parent receipt replay | Exact replay PASS |
| Provenance / observer-foundations / ordinal probes | All exit 0; raw logs retained |

The first native error is ENVIRONMENT/INVOCATION, not a mathematical failure:
`scripts/meta_choice_descent_probe.py` imports the package without adding the
checkout root. The documented repository setup installs the package; this
local environment had not done that. Running the exact same test with
`PYTHONPATH=/media/leah/SPANKBANK/SUCCYBOI/SUCC-hannibal-source` passes. No
ancestor code was patched and no global package installation was changed.
The full native rerun uses this explicit path, including in subprocesses.
It completed successfully; the initial failure remains in the receipt history.

An earlier shell log launch raced the creation of its temporary log directory;
the provenance/observer redirections failed before those commands executed.
They were rerun after the directory existed. This orchestration failure is
not counted as a passed gate. Per-command final exit codes and raw logs are
retained. Existing SyntaxWarnings and intentional negative-control messages
in native logs are not silently converted into failed mathematical assertions.

## Exact observations and falsifiers

At the declared logarithmic meshes:

| A | m_A | Exact E_A |
|---:|---:|---:|
| 16384 | 8 | 16781055/16777216 |
| 65536 | 16 | 67119613/67108864 |

Both meet the declared finite E<9/8 threshold; all four auxiliary mesh
observations do too. No all-A bound follows. The original full modulus has
1,134,312 bits; source generation streams it instead of storing all states.
The separate odd-register replay computes its modulus by a factor sieve and
balanced multiplication, then evaluates the combined-even-pole recurrence.
Its histogram and literal-carry comparisons are independent code paths with
the SAME mathematical source, not independent source corroboration.
The factor-sieve modulus independently has 1,134,310 bits; its hash and the
relation full_D=4*odd_D were checked exactly against the full-modulus receipt.
A final-byte full-modulus replay also PASSED with executable hashes recorded
before and after, removing ambiguity from minor instrument edits made during
the earlier runs. It completed in 398.042 seconds with exit 0; its raw status
and four unchanged executable SHA256 values are retained.
The smaller receipt is replayed by the identical instrument for reproducibility.

Development IID-mean ceiling failures occur at A=2,16,256,1024. The full
original count vectors and exact inequalities are retained. The auxiliary
fresh A=16384,m=64 observation also exceeds that ceiling; this auxiliary
comparison is not presented as a preregistered slow-mesh hypothesis test.
These failures refute E<=1+(m-1)/A, not the requested E=o(log m).

At N=12288 the exact rational interval mirror cost is enclosed by
[2345235049,2345235050]/1099511627776. Rank-half-turn permutations cover all
12288 actual time indices with unmatched mass zero. Their rational chord
certificates give normalized Weyl upper bounds strictly below 0.0037,
0.0079, 0.0140, 0.0109 at h=7,17,255,256 respectively. No floating
trigonometric inequality is used. These fitted finite matchings are not an
all-horizon arithmetic explanation; no source-specific vanishing cost is proved.

At A=512, the exact ordered (near, strict inner, shell) counts are
(8600,1490,7110) for m=64 and (2488,744,1744) for m=256. Independent
quadratic Fraction enumeration agrees. H-01's deliberately conservative
shell ceiling is 131072 in both cases. All literal exclusion packets pass.
The logarithmic mesh is only 8 here; auxiliary meshes were declared first.

Finite witnesses cover every lag through A at A=128,256 and m=256,4096.
They verify respectively 256/512 and 512/1024 ordered exclusions. This is
direct rational finite verification, not certification of the existential
Diophantine onset or the narrower finite scan's eventual success.

## Declaration and authority

PREREGISTRATION.md was committed as
`bf514802d769fbe297fb08c32385bd0fc4279958` before the new source runs and was
not rewritten. Previously observed data are labeled development; the new
horizons are fresh to this execution, not a claim that nobody previously
computed those pi states. The additional large odd replay strengthens oracle
validation after generation; it introduces no newly selected asymptotic test.

No new Lean compilation, external referee, academic priority, all-prefix
selected cancellation, or pi-normality proof is claimed. Hosted CI is separate
from local gates and must be read at the final exact head; queued/running CI
is not a pass. `AGENT_AUDIT.md` states the actual agent/dependence boundaries.
