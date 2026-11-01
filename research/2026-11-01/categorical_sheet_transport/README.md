# OPERATION FULL OBJECT — categorical sheet and Fourier transport

Research-only child of PR #447 at `6fedcbe445f856878ecb1b1d9a0a84ad97a77e2e`.
Main XVIII, original four signed poles and literal U0=0 are unchanged.
**Pi normality and RH remain OPEN.** No physical-quantum or new Lean claim.

## What actually changes

A single source quotient R(z) forgets enough information that z->z+1 has no
rational descended law. We do not erase that theorem. We construct a sufficient
observation object and prove its laws:

* TWO frames (R(z),R(z+1)) recover z rationally; the inverse denominator is
  proved nonzero for all real z>=1, plus the exact initial z=0 case.
* THREE frames (R(z),R(z+1),R(z+2)) embed the ENTIRE complex source sphere.
  Exact integer Bezout certificates prove global point separation, separation
  from infinity, and immersion. Successor is globally conjugate on this image.
* A general coalgebraic behavior completion supplies the universal minimal
  successor-stable observer; a coarse-span countermodel tests branch integrity.
* Marked frames transport poles, source, seed, samples and dynamics together.
* Exact Fourier naturality, central Weyl phases and conductor embeddings are
  implemented without allocating enormous Fourier matrices.
* A real adapter reuses ObservationPathCategory. No second core category is added.

The geometric clock carrier and the BBP arithmetic state are distinct: the full
pointed object also retains its arithmetic fiber U and the original source update.
Coherence does not imply signed cancellation. In particular the Hilbert-colimit
point evaluator has norm sqrt(Q), unbounded along the true conductor tower.

## Files and replay

Read PROOFS.md for all hypotheses/derivations and CLAIMS.md for scoped verdicts.
GLOBAL_DELAY_CERTIFICATE.json is a small exact integer certificate, NOT a list
of fitted numerical samples. polynomial_oracle.py checks it without SymPy.

From the repository root:

    python -m unittest discover -s tests -p 'test_categorical_sheet*.py' -v
    python research/2026-11-01/categorical_sheet_transport/symbolic_audit.py

The first command uses only stdlib for the self-contained arithmetic tests;
three additional tests require the actual existing SUCC core. The second is an
optional independent SymPy audit. See VALIDATION.md for what ran locally.

Keep this as a DRAFT. No merge, release, tag, historical claim promotion or
production/foundations rewrite is authorized by this research package.
