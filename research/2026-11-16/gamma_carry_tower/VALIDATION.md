# Local validation and limitations

Validation under the container runtime (not the complete SUCC checkout):

- `PYTHONPATH=. python -m unittest discover -s . -p 'test_gamma_carry_probe.py' -v`: 16 focused tests PASS, including exact four-pole Fractions, all sixteen group-cocycle cases, Gamma(1) cyclic negative-binomial weights, Gamma eigenphases, metrics/snowflake, resolution spectral gap failure, original BBP chronological carries, nonclosure on mod4 alone, and forced wrap refractory controls.
- `python gamma_carry_probe.py`: standalone algebra/geometry/source control PASS. Includes six exact positive forced seam examples, rational unwrapped source path through n=128, no pi oracle, and high-resolution spectral asymptotic diagnostics. Ordinary float Fourier calculations are diagnostics; the universal statements follow from the displayed algebraic proofs.
- No full root `AGENTS.md` suite, Lean check, external math referee, or independent physical observation is claimed. PR/branch publication, if any, is separate from this local validation record.

Source-critical distinctions: the finite C4 Gamma observer is **not** the actual BBP time transition; the full Γ metric is a chosen compatible observation geometry, not uniquely selected by π; `gamma_carry_probe.py` is one implementation with focused independent formulation checks, not blind source independence; finite observations don't certify universal π normality.
- Post-correction final scoped suite: **17/17** focused unittest cases PASS; output retained in `TEST_LOG.txt`.
- An independent `independent_audit.py` (no import of the primary module) checks the full exact 4×4 gamma matrices with SymPy, the normalized rate-2/rate-3 quarter-turn, the mod4 cocycle, the low-mode Taylor limit and 500 original rational forcing values. PASS; its output is in `AUDIT_LOG.txt`.
