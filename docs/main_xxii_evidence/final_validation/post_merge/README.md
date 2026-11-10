# Independent merged-main verification

Main43886e83 has exactly the validated integration tree33b18ae6. New detached-checkout provenance/observer/ordinal/catalog gates, demo and56 focused parity/source/inventory tests PASS. Local main was then fast-forwarded with --no-overwrite-ignore; untracked .claude/ is unchanged.

All28 live research heads were rechecked, annotated with the carrying main merge and closed (18 explicitly,10 already auto-closed); all28 branches remain at their audited heads. Open PRs after reconciliation:0. See raw API/ancestry records.

The first gate probe accidentally ran while checkout was still populating and could not open its script (exit2). Both the failed command/log and corrected exit0 run are retained. This was a setup race, not a mathematical failure.

Fresh post-merge hosted checks are a separate run from the19/19 passing exact integration checks. Their snapshot is retained without turning in-progress jobs into passes. All three headline conjectures remain OPEN.
