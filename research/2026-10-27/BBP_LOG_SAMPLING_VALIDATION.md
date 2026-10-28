# Logarithmic SUCC / Dirac sawtooth validation scope (2026-10-27)

**Parent:** #332, intended research-only branch. The original signed four-pole forcing, U0=0, archives and main are untouched. An isolated Python standard-library worktree was used to run exact rational checks.

Focused command:

~~~sh
python -m unittest discover -s tests -p test_logarithmic_sampling_succ.py -v
~~~

**Actual local result:** 14 discovered, **13 PASS**, one native SUCC import **SKIP** because the upstream succ_internal_matrix_walk module is not installed in the isolated package. The standalone finite probe executed with **status PASS**: 200 independently recomputed original four-pole equalities, 85 exact finite rational Green identities, 60 polynomial Dirac/sawtooth identities, 45 nonzero source-pulse cases, 58 rational finite log-ratio identities, 200 chiral-source identities, four exact harmonic/Gamma gluing checks, four scalar-weight controls and 18 exact rational finite-band Mellin alias majorants. Pure Python syntax compilation passed. These are precise finite implementation checks, not an analytic π normality proof.

Independent controls include arbitrary polynomial test functions, genuinely shifted sampling nodes with a negative t0, source pulse sign mutation, changed packet scalar weights, coherent rational α=1 sampling and exact cancellation of the chiral 1/n masses. The infinite distribution identities and analytic convergence estimates appear as paper proofs in the dossier, not as results inferred from finite tests.

**Not executed:** full native SUCC source/provenance tests, full AGENTS.md suite, GitHub hosted CI, Lean and external peer review. Direct git network access from this execution container failed with Could not resolve host: github.com; repository inspection and eventual Git writes used the authorized GitHub connector. The native import must be validated after checkout by CI/Claude independently.

The new Python sources are designed for byte-verified blob staging, and the local git-object SHA identifiers must be compared to the remote created blobs before a test parity claim is made. No main merge or release is authorized.
