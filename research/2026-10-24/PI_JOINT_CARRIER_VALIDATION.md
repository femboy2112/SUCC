# Joint-carrier validation, provenance and test boundaries

Date: 2026-10-24. Frozen parent: SUCC PR #274 at d942c4707d750f788f39acb137a04e871a93e0a6, inherited #273 8d89711db77fea81920321d32f831eed3dec1e68 and #272 6e8fa8b77886b13f1f533ed8083fd88c849d14b3. Sibling #271 4eafc6151e9a494f2aea8ec79ca6cf5608152c80 read, not merged.

## Executed in the isolated local research checkout

- Python 3.13.5: `PYTHONPATH=/mnt/data/joint_carrier_research python -m unittest discover -s /mnt/data/joint_carrier_research/tests -p 'test_*.py' -q`: **41 tests passed in 6.616 seconds**: 15 inherited exact Pascal/Lucas controls (copied from parent) plus **26 new tests** in two new modules. These validate the staged source/test bytes, not a complete SUCC worktree.
- Standalone `PYTHONPATH=/mnt/data/joint_carrier_research python /mnt/data/joint_carrier_research/scripts/pi_joint_prime_carrier_probe.py`: **11,624 exact assertions** on fixed BBP forcing/state reconstructions, local p-primary recurrences, dyadic residue permutations through depth 9, and local/global phase equality. Genuine hex gate certification was checked at all 512 source times n=1..512 with the rational positive-kernel tail bound; no unspecified floating-digit conclusion.
- Full-factorial 2x2 synthetic CRT gate residuals exactly (5/36,1/9,1/12,0), gain +1/18; local-mean-zero/global-character-nonzero hostile control. Prime p>=7/power complete-period pole counts include 77, 539, 1001, 5929; 3/5 Hensel/numerator collision mutants; multiplier16 orders 7,11,13,17,19,23,31; 1,300 source valuations compared with independent original-fraction valuations. The optional `mpmath.pi` source oracle is labelled *noncertifying*.
- Code compileall passed for source/test/probe modules; receipt parses under `python -m json.tool`.
- The 8 exact code/test/probe/receipt/dossier/claim/handoff files were uploaded as transport files and each Git object SHA compared against the locally tested `git hash-object` checksum. The temporary private staging assets were scheduled for cleanup after the atomic Git tree was published.

## Not executed here / not implied

No full 7,000+ SUCC test discovery; no `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, or `scripts/ordinal_succ_report_probe.py` on the full combined tree (network git clone unavailable in this local runtime). Hosted CI on the pushed SHA must be checked separately. No Lean compilation was attempted or claimed. No theorem for pi normality, unknowability, authentic selected real 1/16 frequency, same-law tripling, or uniform source Fourier cancellation is asserted.

## Strongest scope firewall

Local CRT *pole activation* is independent on complete periods, whereas source-state character phases have shared time and multiplicative-order memory; independent Haar p-adic times almost surely leave the restricted finite-adele carrier. Exact all-prime reconstruction does not imply equidistribution. See JPC-18 UNVERIFIED in the claim supplement.
