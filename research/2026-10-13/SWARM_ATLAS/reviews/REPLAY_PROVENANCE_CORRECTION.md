# Additive replay provenance correction

The principal accidentally reused third_probe_replay.json (older A07/A08/X03 replay) for a new14-probe replay in checkpoint19bd7ec, and fourth_probe_replay.json (older D27/F42/B16/C20 replay) for a new D26/D30/F45 replay after it. Both original frozen files are restored byte-for-byte from their committed pre-reuse versions. The new records are retained separately as fifth_probe_replay.json and sixth_probe_replay.json. The intermediate git history is not rewritten. Original failures, command results and source hashes remain retrievable.

C19 review probe regenerates its receipt using the execution HEAD; the integration replay is retained as C19_RX_INTEGRATION_REPLAY.json and the original receipt was restored from the review commit. C23 failed once when repository PYTHONPATH was omitted; the proper declared-environment retry passed. These are provenance/invocation corrections, not theorem weakening or fabricated passes. Future replay filenames must be checked for prior existence.

X07 author probe also regenerates its receipt. The integration-run branch/dossier hashes are preserved separately in receipts/X07_INTEGRATION_REPLAY.json; X07_RECEIPT.json was restored byte-for-byte to the author commit.
