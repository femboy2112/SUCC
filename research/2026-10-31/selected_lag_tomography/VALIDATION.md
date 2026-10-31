# Validation and source provenance — signed lag forge

**Date 2026-10-31; state at development.** Started from SUCC draft PR #433 exact SHA 5721c048b54430b3d2195d63ba4d1a9ec0794f99 (parent already includes PR #431 at cf23b8cfc39f56935c432ed764adf0a33efb0d7e). Independently imported **all 11 additive research/test blobs** from sibling PR #432 exact SHA d3907a7937b10dbf51f3926e0dd3460d5ff12353 using existing SHA references without rewriting any source or test byte. Main XVII e8598cfa5d32fd1de8e94a3e458a366a0850d59e and historical content unchanged. That import produced the intermediate commit 766b7e14cea50899d8e5358fbfd2dc4ed9694e4c.

## What was ACTUALLY executed locally

- Wrote the independent stdlib Fraction modules selected_lag.py, independent_oracle.py, run_receipt.py and root test_selected_lag_tomography.py under an isolated local research checkout. Executed:
  
      python -m unittest discover -s /mnt/data/succ_lag_forge/tests -p 'test_*.py' -v
  
  **Ran 28 tests in ~3.3 seconds — OK.** The tests include exact original four-pole identity, source zero seed, offdiagonal lag factorization for multiple seeds, independent chronological unrolling, all-horizon forcing budget on finite partial sums, 3/5 LTE over k=1..899, exact VdC for Gaussian phases and independent sliding-window energy oracle, signed Gram decomposition, source dyadic complete residue histograms and an independent combined four-pole oracle, local-vs-real counterexample, exact first cofactor 15/255, rational Machin/Taylor cos on known roots, finite signed selected test with coherent control, nearzero irrational seed perturbation certificate, and non-Haar invariant one-mode counterexample.
- Executed finite **full, outward-rational** receipt on original zero-seeded source:
  
      python research/2026-10-31/selected_lag_tomography/run_receipt.py 512 4
      python research/2026-10-31/selected_lag_tomography/run_receipt.py 1024 4
      python research/2026-10-31/selected_lag_tomography/run_receipt.py 1536 4
  
  All three returned strict selected/coherent separation and nontrivial finite normalized squared-Weyl upper bound; see exact fractions in CERTIFIED_LAG_RECEIPTS.md. Approximate local runtimes were 6.29s, 12.76s, 19.31s. Results are finite holdouts on one source and one implementation, **not three independent witnesses of asymptotic normality**.
- The rational cosine instrument includes Machin π bounds from alternating arctan, exact rational-phase reduction, outward 10^-20 phase midpoint with Lipschitz compensation, a 17-term rational cosine Taylor polynomial with explicit global remainder, and final outward 10^-12 intervals. No downloaded π digits, Monte Carlo, or unbounded floating-point claims. Finite signed interval is certified by the source code and error lemma.
- Local source Git blob SHA-1 checks were made and checked against the GitHub object creation results:
  - selected_lag.py: 59d0351484865ab919317ae1a34f6e9ec1b12da3 (the locally tested file has no terminal newline, exactly matching the blob).
  - independent_oracle.py: d4c5a4a815fe3d8beb29b075972e2de03eb63fdf.
  - run_receipt.py: f294eb5ae0c6b77fe300623591755c27e0037304.
  - tests/test_selected_lag_tomography.py: 75df7fdae1a790bce4e23a39620da3dd9c2f4551.
  The four files were installed in one atomic Git tree/commit bdda83caabe5a647bef405f01e47d3180a3cd1eb on the dedicated research branch.

## Validation NOT performed and not claimed

- The full original SUCC 10k+ unittest suite, source/claim provenance verifier, full foundational probe, ordinal probe and any Lean kernel proof of LAG01–LAG04 were not run locally because the original full Git checkout was not available in this runtime. Hosted exact-head GitHub Actions on the integrated research branch is the proper integration gate and must be verified after the final commit. The imported PR #432 / parent PR #433 source tests are NOT called independent runs of the new source-lag theorem.
- The interval measurements do not prove any uniform lower or upper bound in N. The conditional van der Corput route is a paper proof using classical Cauchy, source positivity and LTE; finite tests corroborate implementations, not infinite logical correctness.
- No PR merge, main edit, formal authority promotion, tag, release, source license change, publication or RH/π-normality status promotion has occurred.

## Mandatory on-branch CI/provenance commands

    python -m unittest discover -s tests -p 'test_selected_lag_tomography.py' -v
    python -m unittest discover -s tests -p 'test_edge_seed_tomography.py' -v
    python -m unittest discover -s tests -p 'test_seed_superposition.py' -v
    python -m unittest discover -s tests -p 'test_carrier_path_measure.py' -v
    python scripts/verify_provenance.py
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py
    python -m unittest discover -s tests -p 'test_*.py'

**Hard false-positive firewalls:** inherited same forcing coherent seed s*=-π/16, nearzero irrational fixed nonnormal seeds s_L from PR #433, rational changed seeds whose NORMALITY status is unchanged by Wall, Gaussian-Pascal phase-by-fiat from PR #431, 73-channel phase-tomography alias at N=10 from PR #432, and the T16 invariant non-Haar 3-point measure with vanishing h=1 Fourier coefficient.

**Next verdict-changing test:** a new all-horizon signed bound on the actual original zero-selected critical-log lag observable for every fixed h, independently derived and successfully replayed on fresh time/frequency/pole-class holdouts; the known finite results alone do not satisfy it.
**Integration test isolation correction:** The original integrated PR #431 already used a top-level module named independent_oracle. To avoid an order-dependent Python sys.modules collision in full root discovery, this new research test now loads its own independent_oracle.py by a unique importlib.util source-file module name. After the change, 28/28 focused tests were re-executed locally, and the new exact Git blob 75df7fdae1a790bce4e23a39620da3dd9c2f4551 MATCHES the re-executed test bytes. No parent/sibling code was changed.

**Full-root integration order repair:** Three research test families reused the generic top-level module name independent_oracle under different sys.path entries. On the combined child only, tests/test_carrier_path_measure.py and tests/test_seed_superposition.py now use importlib.util.spec_from_file_location with unique module names; the new lag test already used a unique name. No parent source code or test assertions changed. See INTEGRATION_TEST_IMPORT_REPAIR.md. The full exact-head hosted CI outcome is still the authority for integration; a prior PR #433 Python job failure was observed, but its raw cause was not established via job logs.
