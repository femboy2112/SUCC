Independent review probes -- preserved source and CURRENT-TREE RERUNS

These probes were originally executed as inline Python heredocs in the reviewer
tool calls. Their exact source remained available in those calls. The mathematical
probe bodies are preserved here with formatting, explanatory docstrings, and a
guard against accidentally disabling assertions. This directory does not purport
to contain original earlier-run log files. All *_rerun_stdout.txt files and
rerun_results.json are fresh outputs captured after these scripts were saved.

The final API observation in semantic_environment_probe.py is explicitly updated
because the root subsequently repaired the observed float-state acceptance:
the current probe now requires float rejection. The original 800 environment
comparisons, 49 budget chains, 180 omega AST cases and 2,916 cofinal target cases
use the same generated inputs and comparison method as the earlier review.

The receipt source-hash check was originally a separate inline command; it is
included at the beginning of receipt_independent_probe.py. Its mpmath check is
an independent numerical diagnostic, not a rigorous transcendental enclosure.
The production certificate's rational Taylor remainder is the proof dependency.

Run from the repository root with assertions enabled:

  PYTHONPATH=. python research/2026-11-09/cayley_source_observer/review_probes/boundary_exact_probe.py
  PYTHONPATH=. python research/2026-11-09/cayley_source_observer/review_probes/semantic_environment_probe.py
  PYTHONPATH=. python research/2026-11-09/cayley_source_observer/review_probes/receipt_independent_probe.py

Scope: finite mathematical/implementation calibration by a same-model independent
bearing. No claim of external refereeing, general normalizer metatheory, pi parity
balance, normality, or independence from the underlying BBP source identity.
