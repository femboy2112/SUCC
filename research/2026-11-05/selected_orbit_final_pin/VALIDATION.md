# Reproducible validation gate

Run from the repository root:

    python research/2026-11-05/selected_orbit_final_pin/validate.py --output /absolute/new/output-directory

The runner records the exact candidate commit/tree, executable, dependency versions, complete command vectors, exit codes, durations and SHA256 hashes of preserved raw logs. It runs the four mandated repository commands once, serially, alongside all focused suites and exact receipt verifiers. The native suite has a declared30-minute timeout and reports timeout as such. It sets the checkout PYTHONPATH and caps BLAS/OpenMP threads to1. An existing output directory is rejected rather than overwritten.

Initial focused results before integration: Alpha6/6, Delta8/8, referee9/9; coordinator24 exact charge identities; Delta48 rows/816 rational intervals replayed byte-identically with mpmath1.2.1 and1.4.1. The integration gate uses an isolated virtual environment satisfying the declared mpmath>=1.3,<2 requirement, resolving1.4.1, with the installed SymPy/Numpy/Scipy. These results do not preclaim the final native gate.

The exact final-head gate output is preserved outside the tracked source tree and reported in the draft PR, so recording its result does not silently change the tested commit. See that PR for actual pass/fail/timeout counts and hosted workflow state. Neither inherited CI nor a local pass certifies an analytic proof. No new Lean proof was run.
