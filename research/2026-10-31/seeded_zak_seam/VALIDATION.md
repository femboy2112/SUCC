# Exact local validation, status boundary

Original source: Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`, authentic unchanged four-pole source and zero seed. Related open PR #437 four-pole alias theorem is read-only provenance, not separate validation of new Zak geometry.

```
python -m unittest discover -s tests -p 'test_seeded_zak_seam.py' -v
```

**21/21 tests passed locally** on authored bytes, standard-library Python, exact Fraction/Gaussian integer operations. Included: two algebraically distinct original rational source implementations (four poles vs full numerator and denominator), positivity and monotonic finite controls, exact fractional `1/4`/`1/2`/`3/4` source values, finite Green shift with retained cutoff remainder, bounded source-alpha intervals against reverse nested Horner oracle, finite past/future identity, periodic sine interpolation quarter-grid exact changes with every integer still pinned, Zak corner/frequency/shift sewing over Q(i), independent binomial-integral vs factorial-beta bump norms, source-blind L2 energy and growing point-to-energy ratio, invalid input rejection.

**Independent scope:** The oracle uses a combined rational numerator and reverse Horner, and a factorial beta integral distinct from the binomial expansion. Both share source mathematics; separate algorithms are not independent external mathematics authorities.

**Additional numerical diagnostic** (not proof): 50-digit mp arithmetic verified T(0) close to pi/16 and finite `16 T_J(x)-T_J(x+1)-r(x+1)` residual, for fractional x. For the r=0 positive even compact bump, zero-alias derivative w.r.t periodic sine interpolation is nonzero imaginary (~4.65755i at N=1, h=1), while all integer samples remain exactly 1. The nonzero derivative itself has a rigorous positivity proof in PROOFS SZ-13 and does not rely on numerics.

**Not run / not claimed**: full 10k+ suite, hosted exact-head CI, full checkout provenance, Lean kernel, external peer referee, numerical π normality proof or analytic all-horizon saving.
