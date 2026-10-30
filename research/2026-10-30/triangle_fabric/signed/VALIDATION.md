# Signed-front execution receipts

Executed in the isolated research worktree, parent405
`6cf5050ff2cfd92e7a0c8876da5233be6ff117f5`, Python3.12.3, SymPy1.12.
This front made no historical source or production edits and no git commits.

- `python3 -m unittest -v test_filters`: **11 PASS**, 0.459s reported by unittest.
  Raw `receipts/tests-initial.log`; start/end duration and exit0 in
  `receipts/initial-commands.json`.
- `python3 probe.py receipts/probe.json`: **11 filter cases +4 dyadic cases**,
  all rational values retained. Initial7 cases and4 declared freshholdouts
  are marked in the JSON. Exit0 and output hash retained.
- `python3 independent_oracle.py receipts/probe.json receipts/oracle.json`:
  **PASS**. Separate Gram-Schmidt reconstruction from the positive 3-term
  source; SymPy polynomial division and exact Sturm roots; direct unrolled
  orbits. Counts:11 orthogonal polynomials,11 rootcounts,42 prefix checks,
  11 divisions,77 directorbit checks,68 dyadic eventualorbit checks,
  11 first-omitted positive-norm identities,55 endpointjet checks.
  Raw output and command metadata in `receipts/oracle.log` and
  `receipts/oracle-command.json`.

The probe checks 257 rational zgrid points perfilter; positivity on the
entire interval is proved by the orthogonal-root bound, not inferred from
that grid. The exact paper derivation supplies allN/M and allhorizon claims.
The πerror ordering also uses separately bounded BBP sums (100terms), never
floating-point π digits. All fractions and dyadic synthesis are exact.

No failed mathematical case or failed new test occurred in this front.
One initial read-only sibling406 SHA lookup raced the root fetch and failed;
reading its fetched branch subsequently succeeded. This is repositoryaccess
timing, not evidence for a mathematical claim. No runtime dependency was
installed. Root-owned fullrepository/CI/provenance receipts are separate.

No Lean formalization of this front, external independent referee, unbounded
computational experiment, new irrationality input, or scholarlypriority claim.

Primary literature checked online: DLMF18.2(vi) and18.5(i), and
Doty–Lutz–Nandakumar arXiv:cs/0602032 (rational-affine preservation).
The construction uses classical orthogonal-polynomial/Stieltjes methods,
and explicitly credits SUCC's2026-10-25 finite-moment/jet predecessor.
