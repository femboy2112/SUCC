# Oily / One-Boundary validation boundary — 2026-10-27

Command executed in isolated Python environment:
~~~sh
python /mnt/data/oily_one_boundary_exact_probe.py
~~~

Observed exit 0, with:
~~~text
PASS: 33 exact integrated packet identities
PASS: 20 primitive-character and first-response checks
PASS: exact ungraded and dyadic log coefficients
PASS: first packet masses ['2', '2/3', '4/15', '4/35', '16/315']
~~~

The exact test file copied to GitHub has blob SHA 9d49f807dce4f38d9b2a59d4a238b1ebb8bb53d1, byte-identical to the executed local source. An independent SymPy implementation expanded (16−x^8)p_j(x) near x=1 for j=0..9 and verified the first two endpoint coefficients exactly; it also verified the n^(-3) moment coefficient in all 10 cases. The m=2 odd projection was independently expanded to (20/3)(1−x)−12(1−x)^2+O((1−x)^3).

The infinite analytic results follow from the paper proofs in the dossier, NOT from the finite tests. No full native repository suite, provenance, hosted CI, formal Lean proof or external scholarly priority claimed. A local Python runtime emitted unrelated optional spreadsheet warmup diagnostics on stderr while the actual research script exited 0; no mathematical execution failure was observed.

Original four signed BBP poles, zero initial state, historical source code and main untouched. π normality remains OPEN.
