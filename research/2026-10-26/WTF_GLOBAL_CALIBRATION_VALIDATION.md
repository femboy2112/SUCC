# WTF global calibration — validation and authority receipt

**Scope:** additive child of draft PR #314 `935c2db4c36ff56d90acd82eae30bcce15b6a053`. The native four-pole source and historical archives are **unmodified**; no original source file is included in the new diff. A new base-16 π-normality theorem is **NOT claimed**.

## Validated local execution

- Created source, focused tests, and deterministic receipt probe using exact Python stdlib `Fraction`/integers; no π-digit oracle or floating tolerance is used in the mathematical identity tests.
- **12/12 focused tests passed** in an *isolated* SUCC interface environment; this is NOT the full native repository. The test environment includes previously inspected `lambda_source_duality` and original four-pole `authentic_r` implementations and a clearly labelled minimal local shim for `seinfeld_succ.rational_rank` and categorical source dependencies. The only new committed code is the `wtf_global_calibration` module, tests and probe.
- Exact independent enumeration for `2^k`, `k=4..8` checked all four zero roots, all four antipodal roots, coherence lifts, independent-copy baseline, full projector and primitive Ramanujan averages.
- Direct original BBP rational history and changed-seed source at `N=1,2,9,32,79,127` checked the `s in {0,1}` identity, exact primitive/full equality and input authentication scope. The deterministic probe additionally covers `N=1,2,16,64,127` and stamps the original/changed source comparisons. The extra exact test covers `V_n=-T_n` with changed seed `-pi/16`: for all positive n the literal carry and selected digit are both 15, both compatibility projectors equal one, while every fixed-h Weyl mean tends to one by the Green tail theorem; the test asserts exact native rational forcing bounds at n=1,2,3,8,29,97,257,1024 and never numerically approximates pi.
- Every positive test martingale checkpoint has exact reference expectation one, and the finite dependent-null tree obeys Ville's crossing bound with the declared previsible policy; the postselection and duplicate-observation traps are explicitly **countermodels**, not valid test martingales.
- Exact `linear_constraint_rank_gain` test distinguishes the dependent three-step macro recurrence from the additional zero-initial seed anchor.
- The deterministic JSON receipt regenerated and replayed exactly. A **deliberate false `pi_base16_normality_proved=True` mutation** was rejected on replay (nonzero exit). Run from native root with `PYTHONPATH=.`:

```sh
python -m unittest discover -s tests -p 'test_wtf_global_calibration.py'
python scripts/wtf_global_calibration_probe.py --write
python scripts/wtf_global_calibration_probe.py --verify
```

## Source checksum and independent authority limits

The exact receipt includes SHA-256 of the new module, test module and probe, plus `source_base_pr_314_sha`. The mathematical claims derive from the paper proofs in `WTF_GLOBAL_CALIBRATION_SOURCE_RESONANCE.md` and preexisting PR #313 source-spill theorem—not from numerical fitting. The new code imports authentic source/history and the Seinfeld linear-rank routine, rather than overriding the four-pole formula.

**Not performed in this isolated environment:** the complete SUCC native `unittest discover`, provenance verification (`72` historical entries), observer/ordinal probes, any Lean kernel checks, and external peer review. Those are separate post-push hosted/native integration gates for Claude; report CI only at the actual pushed GitHub head. Never describe these 12 tests as the full SUCC test suite.

**No new selected Weyl saving** was obtained. The main new negative result is a source-specific **compatibility false positive**, exact for the original four-pole forcing and inherited all-seed spill bound: both Ramanujan and full match averages tend to one for every seed. The explicit original-forcing orbit `V_n=-T_n` has **perfect score at all positive times**, while `e(hV_n)` tends to one for every fixed h: a rigorously nonnormal changed-seed witness. The remaining fixed-frequency `S_N(h)=o(N)` estimate is **OPEN**.
