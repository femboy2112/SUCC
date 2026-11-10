# Executed model validation

All commands below completed with exit0 in
`/tmp/succ-learning-yoneda-venv/bin/python` (Python version is retained in
`HOLDOUT_SUMMARY.json`). The original model/table were frozen and pushed at
`5e1e3fad` before the later source was opened. No changes were made to that
implementation or table during or after the later-source run.

Frozen code SHA256:
`10089085b088ec9cd09b2b34feadb5abf2b9345f933cd04575e8cfd3e921b06d`.
Frozen table file SHA256:
`2462a0e3b814a5fb8664701a12832698b04cbd62c7c60ecf63abc669bc4f3887`.

1. **Training and replay.**3274 old source times, union1103--4376, with the
   16-time overlap counted once. All16 one-carry and256 two-carry cells were
   populated; no disk contraction was necessary. The source's unwrapped and
   carry hashes and37948-bit denominator match the earlier committed
   source2203 exactly. See `TRAINING_REPLAY.json`.
2. **Fresh clock.** A55003 selected p220009, m27501, q2. The complete literal
   source was reconstructed through n110004. All55002 clean principal parts
   were checked. Exact independent BBP finite power sums checked times55003
   and110004; the denominator has952449 bits. No pi digits were used as
   recurrence input. Every observed literal carry was in0..15; no later
   feature was unseen. `HOLDOUT_55003.log` spans1521.612840895 seconds from
   filesystem creation to last write, approximately25min22s. This is a
   file-lifetime observation, not a separately timed CPU benchmark.
3. **Six charged certificates.** h1,3 times the zero/one/two-carry menus.
   Each includes outward folded L1 error, predictor mean, retained resonance,
   signed-orbit cost upper bound and direct signed mean. All direct/folded
   phase enclosures overlap. None of the trained tables improves on zero
   prediction. The model's source receipt contains110004 literal carries,
   110004 individual phase boxes across the two frequencies,55002 folded
   boxes, source hashes and actual component bounds.
4. **Postregistration whole-family audit.** Eight dual certificates cover
   two frequencies, two carry menus and two unit-disk witnesses. The stronger
   radial witnesses prove rho>.619878/.571309 at h1 and rho>.616537/.573692
   at h3 (one/two respectively), for every shared unit-disk table in these
   menus, even if hypothetically selected after the source is read. This is
   not an upper estimate of W or an asymptotic theorem.
5. **Independent family arithmetic.** `independent_family.py` folds individual
   source phase boxes directly, without B or local-prime multiplication.
   It uses scalar Gaussian integers, rational fractions and integer square
   roots, importing none of the primary Box/model arithmetic. All55002 distinct
   radial witnesses are explicitly checked in the unit disk and reused in
   the four certificates. Independently outward floors differ by less than2^-60 from
   the primary ones. Inputs share the source phase boxes; this is an
   arithmetic/basis check, not independent source provenance.
6. **Eight focused tests PASS.** Reduced-Fraction source replay at60 times;
   exact dyadic disks and literal out-of-alphabet handling; rational modulus
   bounds; coherent-control certificates; Gauss-period square orthogonality;
   289 radial-disk probes;72 explicit table dual comparisons; and coherent
   zero-floor control. Log: `TESTS.log`.

Commands:

```sh
python research/2026-11-08/chronology_carry/model/carry_model.py fit \
  --table research/2026-11-08/chronology_carry/model/FROZEN_TABLE.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/2026-11-08/chronology_carry/model/carry_model.py evaluate \
  --table research/2026-11-08/chronology_carry/model/FROZEN_TABLE.json \
  --A 55003 \
  --output research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz
python research/2026-11-08/chronology_carry/model/family_audit.py \
  --source research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz \
  --output research/2026-11-08/chronology_carry/model/HOLDOUT_FAMILY_55003.json
python research/2026-11-08/chronology_carry/model/independent_family.py \
  --source research/2026-11-08/chronology_carry/model/HOLDOUT_55003.json.gz \
  --primary research/2026-11-08/chronology_carry/model/HOLDOUT_FAMILY_55003.json \
  --output research/2026-11-08/chronology_carry/model/INDEPENDENT_FAMILY_REPLAY.json
python -m unittest discover \
  -s research/2026-11-08/chronology_carry/model -p 'test_*.py'
```

The raw compressed source SHA256 is
`02cc3a15ab2e40c2db5006fae961586afbbdd4df048f80dab6da6e98974f11ca`.
Its unwrapped-state stream hash is
`b20a84b9e2284bbf3ad83a5494ad9fe4f9345e16dee8cc12a8e9d5b7d00330e7`;
the literal-carry stream hash is
`7c6431419bcf89060a351979f5dfb547b1891b81c986de763a5ee71619a45747`.

The hostile agent separately checked14 fixed later-source phases with a
192-bit small-modulus BBP algorithm and70-digit interval trigonometry; see
[its receipt](../crucible/INDEPENDENT_PHASE_COMPARISON.json). The model agent
reviewed CCV1--7d and FR1--3 paper proofs, preserving exact reviewed hashes in
`THEORY_REVIEW.md` and `ROOT_REVIEW.md`. Agents share model family, repository
and upstream source contracts; this is not external scholarly verification.
No new Lean proof was produced. Full native and shared validation gates are
reported by the parent round, not inferred from these focused checks.

Pi base16 normality: **OPEN**. RH: **OPEN**.
