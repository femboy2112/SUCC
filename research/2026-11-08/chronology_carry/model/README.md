# Frozen carry-table experiment and whole-family residual audit

The small model is fixed before the later source clock is measured. It uses
only the literal current carry, or the literal previous/current carry pair,
to predict `e(h U_n)` at h=1,3. The table is trained on the union of the old
clean intervals1103--2204 and2189--4376, counting their16 shared times once.
The resulting3274 training examples populate all16 one-carry and256 two-carry
cells. Entries are declared Gaussian dyadics with denominator2^24 and norm
at most one. Unknown literal carry values predict zero.

`FROZEN_TABLE.json` and `carry_model.py` were committed and pushed at
`5e1e3fad` before source-clock55003 was opened. The later clean interval is
55003--110004, with p=220009, m=27501 and q=2. It begins after the previous
source dossier's last measured time44000. A zero predictor is retained as
the baseline. Source-faithful exact arithmetic preserves all four signed
poles, literal U0=0, unwrapped-state and carry hashes, and principal parts.

[CCM1--3](THEOREMS.md) prove the charged certificate. Let f=aB be the folded
coherent phase, F be the folded frozen-table predictions, and M=mean F.
Then rho=mean|f-F| and

    |W| <= rho+|M|.

The predictor's canonical polynomial representation has retained resonance
`R=(m/p)M` and signed orbit sums `C_O=(m/p)M G_O`. The Gauss periods obey
`sum|G_O|^2=p-m`, giving an a-priori coefficient-cost upper bound. This is
explicit accounting for the independent prediction F. It does not supply
free cancellation for carry-conditioned characters, and it is less sharp
than directly retaining M. Expanding the actual held-out B would instead
read W and reproduce the already-audited circular compression.

The [CCM4](THEOREMS.md) family audit goes further: for any unit-disk witness v,
all shared disk-valued tables on the same carry feature menu satisfy

    rho >= Re mean(conj(v)f) - sum_c |mean(conj(v)J_c)|,

where J_c is the fraction of the two replicas having feature c. The audit
uses v=f and an exact dyadic radial witness. It therefore bounds even a
hypothetical table chosen after inspecting the later source. This is a
postregistration analytic audit, not a changed predictor or a new holdout.
It does not cover extra time/replica-label features, arbitrary history
models, or signed-residual methods.

`TRAINING_REPLAY.json` records exact agreement of the training source hashes
with the previously committed source2203. `DEVELOPMENT_FAMILY_1103.json`
uses already observed development data; it is not a fresh holdout. On that
old clock, the radial dual already proves rho>0.53325 at h=1 and rho>0.51846
at h=3 for every shared one-carry disk table. No asymptotic claim follows.

## Completed later-clock result

The original zero-source run completed with exit0. It reconstructed110004
exact source updates, checked55002 principal parts, and separately verified
source times55003 and110004 by exact finite BBP power sums. The common
source denominator has952449 bits. All observed literal carries were in
0..15, and no later-window feature was absent from the frozen table.
The source log spans approximately25min22s from creation to its final write.

| h | Zero predictor rho upper | One-carry rho upper | Two-carry rho upper | Actual modulus upper |
|---:|---:|---:|---:|---:|
|1|0.634971|0.637744|0.664903|0.003372|
|3|0.635968|0.638674|0.668025|0.007613|

Both trained models are worse than zero prediction. Their full direct
certificates are0.660940/0.681625 at h=1 and0.659696/0.693842 at h=3;
the explicitly charged QCO1 upper bounds are larger. Thus the
preregistered L1 prediction route fails this finite test.

The postregistration family audit is stronger. It proves these lower bounds
for **every shared unit-disk table** on the listed features, including a
table hypothetically fitted after reading the later source:

| h | Every one-carry table: rho lower | Every two-carry table: rho lower |
|---:|---:|---:|
|1|0.619878|0.571309|
|3|0.616537|0.573692|

All upper entries above are rounded upward, and lower entries downward.
Exact rational endpoints are in `HOLDOUT_SUMMARY.json` and
`HOLDOUT_FAMILY_55003.json`. A separate scalar-integer implementation
`independent_family.py` reconstructs f directly from the individual phase
boxes, bypassing local-prime multiplication and the primary Box arithmetic.
Its four independently outward floors agree within2^-60; see
`INDEPENDENT_FAMILY_REPLAY.json`. The phase boxes are shared inputs, so this
is independent arithmetic and basis transport, not independent source data.

These floors exclude L1-small reconstruction by the declared finite table
classes at this clock. They neither bound |W| from below nor exclude the
signed-residual approach. The actual signed means are small, as the table
shows, while the raw approximation demand is expensive.

Reproduce the frozen model with:

```sh
python research/2026-11-08/chronology_carry/model/carry_model.py fit \
  --table /tmp/succ-frozen-carry-table.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/2026-11-08/chronology_carry/model/carry_model.py evaluate \
  --table research/2026-11-08/chronology_carry/model/FROZEN_TABLE.json \
  --A 55003 --output /tmp/succ-carry-holdout.json.gz
python research/2026-11-08/chronology_carry/model/family_audit.py \
  --source /tmp/succ-carry-holdout.json.gz --output /tmp/succ-carry-family.json
python -m unittest discover \
  -s research/2026-11-08/chronology_carry/model -p 'test_*.py'
```

The compressed source receipt retains the complete carry stream, all
individual later-window phase boxes, folded phase boxes, and certificate
components. Gzip uses timestamp0; decoded mathematical payloads are the
cross-runtime reproducibility object. The tests separately check the source
against reduced rational arithmetic, Gauss-period orthogonality, exact-disk
witnesses, explicit table inequalities and coherent wrong-complement
controls. This source is not replaced by the controls.

Pi base16 normality: **OPEN**. RH: **OPEN**.
