# JPC-23--26 exact forcing-limit addendum validation

Date 2026-10-24. Parent PR #277 at e9ad0fc3479c8182d19046831006c423ea68ee85.

## Executed

- `PYTHONPATH=/mnt/data/joint_carrier_research python -m unittest discover -s /mnt/data/joint_carrier_research/tests -p 'test_*.py' -q`: **47 tests passed** on the isolated frozen source/test environment (original 41 + 6 new), 6.778 seconds.
- `PYTHONPATH=/mnt/data/joint_carrier_research python /mnt/data/joint_carrier_research/scripts/pi_joint_limit_order_probe.py`: **540 exact assertions**; the independent shell/Ramanujan route matches the direct closed form for explicitly declared p/h samples. Machine receipt is `PI_JOINT_LIMIT_ORDER_RECEIPT.json`.
- Exact p7/h1 = 17/49, p11/h1 = 73/121, ten-prime closed product `9327351230426029199 / 234295420524634222039` lies between 1/30 and 1/20. Retained the failed guessed less-than-1/30 as adversarial control.
- An optional finite complex-root oracle and residue sampling are expressly **noncertifying**. The universal local character, CRT/Haar-limit, Mertens and noncommutation claims are paper proofs with named classical inputs, not claims established by finite tests.

## Not executed

No full SUCC 7,000+ test suite or three other required AGENTS.md probes on this combined branch; not running Lean; hosted GitHub CI must be checked for the exact final commit. No source-orbit `S_N(h)=o(N)`, real 1/16 selected-source gate, pi normality, or unknowability established. Archived files unchanged; no main merge/release.
