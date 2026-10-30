# Preserved extra-probe serialization failure

The first `extra_probe.py` run passed all mathematical assertions but failed
when serializing SymPy matrix entries (`TypeError: Object of type One is not
JSON serializable`). The exact stdout/stderr bytes are retained as
`extra_receipt_failed.log`; the command receipt records its original output
filename before this explanatory rename. This was an output harness error,
not a mathematical counterexample. Converting matrix entries explicitly to
Python integers fixes only serialization. The corrected run has distinct
receipt names and does not overwrite the failure.
