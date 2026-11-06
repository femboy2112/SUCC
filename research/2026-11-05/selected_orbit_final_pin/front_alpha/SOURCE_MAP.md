# Source map and proof dependency boundary

- Repository base: #518 head `749931f0f357c60ef4e21879d96b0306999f428f`.
- Authentic four-pole recurrence, zero seed, full rational lift and literal carries
  are retained. The independent source implementation reduces the four poles
  to `(120n^2-89n+16)/((2n-1)(4n-1)(8n-7)(8n-3))`; it never imports pi digits.
- `yoneda_circle/PROOFS.md` YO3 supplies positivity and `C=1920/2457`; this
  input is inherited, not a new result. The elementary integral formula
  `r(n)=integral_0^1 t^(8n-8)(4-2t^3-t^4-t^5) dt` proves source monotonicity,
  since its integrand is positive on (0,1). It justifies every tail enclosure.
- Independent paths: unwrapped Fraction iteration with separate signed poles;
  modulo-one iteration with the reduced polynomial; direct unwrapped floor
  differences versus weighted literal carry words. Shared arithmetic runtime
  and same mathematical recurrence remain common-mode dependencies.
- No imported source/provenance/production/Lean files are changed. No sibling
  branch is merged. The new proof uses no claim from #515–#517 or Clausen.
- Coherent and period-11 controls use rational intervals around the genuine
  positive source Green tail. The seed of each is `beta-alpha`, not literal zero.
  Rational seed 1/5 keeps the four poles; multiplier-2 and unforced controls
  change the source and are labelled accordingly.
- The proof does not use source-prime/Frobenius orientation, reduced conductor,
  or literal zero selection. Thus it cannot distinguish selected arithmetic
  from same-forcing periodic completions, even though all original-source
  finite measurements retain their exact selected numerators and carries.

Dependency graph: original poles -> positive n^-2 source bound -> reset after
macro-carry correction -> logarithmic correction separation -> fixed-depth
pressure transport. There is NO arrow from the last node to bounded pressure.
That would require a new bound inside the no-correction population.
