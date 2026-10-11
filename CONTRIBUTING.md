# Contributing to Observational SUCC

This is an open research repository, not a proof announcement. New mathematical claims, physical hypotheses, computational artifacts, and negative results are welcome when they have clear provenance and falsification standards.

A substantial PR should include: a precise statement, definitions and scope, proof or model derivation, source attribution, at least one independent control, at least one adversarial test, reproduction steps, and a claim ledger update. Include rejected countermodels rather than deleting them once a promising formulation has been found.

**Different evidence types:** a classical theorem retains its original author's attribution; an exact elementary result may be marked PROVED LOCAL; a unit test establishes only the tested model/implementation; a numerical plot is OBSERVED, not PROVED; a physical carrier conjecture remains HYPOTHESIS until empirical predictions and measurements exist.

Please do not turn a positive quantum covariance into a claimed proof about an unrelated arithmetic functional. Similarly, finite observation coverage is not a universal theorem, and a semantic/reporting \(\omega+1\) stage is not an executed physical infinity.

## Development

~~~sh
python -m pip install -e ".[test]"
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py' -v
~~~

Python 3.10 and 3.13 are CI targets. Keep the core free of mandatory heavy packages and add dependencies only when justified.

## Licensing

No public redistribution license has yet been selected by the maintainer. Public visibility does not imply permission to reuse under any particular license. Do not add a license or publish a distribution without an explicit decision. Every inherited RH-origin file retains its original Git provenance in the manifest.
