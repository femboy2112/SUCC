# Prime-field research: actual support, preserved zeros, missing rigidity

Research-only child of PR #349 at `ad19e3794f1d8da4a81418d38a4fc731b7d355c7`. Original arithmetic sources, `U_0=0`, main, imported archives, production code, and workflows are unchanged. **RH and pi normality remain unproved.** No physical force or independent academic novelty is claimed.

## Main result

For each genuine prime p, let `beta_p=(p+sqrt(p^2+4))/2`. With original prime-occupation labels retained,

`Z_beta(s)=sum_n (product_p beta_p^v_p(n))^(-s)=zeta(s) C(s)`,

where C is holomorphic and nowhere zero on `Re s>0`. Thus this explicit Pisot-clock construction carries **exactly the actual critical-strip zeta zero divisor**, without taking any zero positions as input. The proof is a locally uniform Euler-log comparison, with explicit tail bounds; it is not a numerical inference.

The result has a sharp limitation: the non-Pisot rational clocks `p+1/p` satisfy the same theorem. Pisot support by itself does not explain why zeros should lie on the critical line.

A second exact result makes the author's prime-charge requirement load-bearing: `beta_11^7=beta_29^5`, although `11^7 != 29^5`. Scalar Pisot energy loses the original prime history; source labels and multiplicity must survive.

The inherited PCR-02/Pólya virtual field has a zero-energy marked state for **every** integer, including composites. A prime-only equilibrium needs a separate grade selector. Ordinary local character nulls also propagate to composites. The proof dossier distinguishes these scoped obstructions from the positive construction above.

## Navigation

- [RESEARCH.md](RESEARCH.md): definitions, ten claim families, full proofs, countermodels, and next construction gate.
- [CLAIMS.md](CLAIMS.md): domain/status/provenance/next-probe ledger; local IDs only.
- [SOURCES.md](SOURCES.md): pinned SUCC inputs, primary literature, and dependency audit.
- [VALIDATION.md](VALIDATION.md): actual rounds, failed controls and repairs, executed/unexecuted gates.
- [NEXT.md](NEXT.md): source-derived global pairing / completion handoff.
- [MANIFEST.json](MANIFEST.json): source and receipt hashes (manifest excludes itself).

## Replay

From the repository root, run these explicit research-local commands. No package installation or production import changes are needed for the exact core.

```sh
cd research/2026-10-28/prime_pisot_field
python -m unittest -v test_prime_pisot.py
python mutation_probe.py
python independent_oracle.py
python -m compileall -q prime_pisot.py test_prime_pisot.py mutation_probe.py independent_oracle.py
```

The first two commands use Python's standard library. The independent oracle requires SymPy and mpmath; tested versions are recorded in `receipts/oracle.json`. It does not import `prime_pisot.py`. Its floating-point outputs are observations, NOT interval certificates. The mathematical tail inequalities are proved separately.

The tests intentionally remain in this research directory, not the production discovery tree. **The full root AGENTS.md gates and Lean are not thereby satisfied.** Publication uses one additive `[skip ci]` commit to avoid the expensive CI fan-out requested by the maintainer; skipping is not a passing CI result. Keep the PR draft until the full checkout validation and independent mathematical review occur.
