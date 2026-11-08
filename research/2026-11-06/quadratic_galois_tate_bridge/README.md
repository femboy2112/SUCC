# Operation Quadratic Reflection Carrier — Pisot × Galois × Tate

**Research-only draft, 2026-11-06. Original source and formal contracts unchanged. RH OPEN; pi base-16 normality OPEN.**

The maintainer's intuition was that Pisot conjugate parity and the completed-zeta reflection might share a concrete mathematical carrier, rather than merely looking like two C2 symmetries. The exact classical carrier is `K=Q(sqrt(5))`, with the full adelic/cyclotomic realizations.

**What is actually established:**
- `O_K=Z[phi]` (not `Z[sqrt5]`), `sigma(phi)=-phi^-1` and the exact two-sector unit dynamics.
- The unit-character spectral involution includes the previously easy-to-miss parity shift: `lambda_(z,d) ∘ sigma = lambda_(-z + i*pi*d/log(phi),d)`.
- The quadratic Gauss sum produces `sqrt5`; the character `chi5` is a normalized five-point Fourier eigenvector.
- Unramified Frobenius acts on phi by either identity or Galois conjugation, **precisely according to chi5(p)**. This yields the actual prime-local factorization `zeta_K=zeta*L(chi5)`.
- Completed Tate/Hecke reflection lives on that same number field's adelic carrier; the regulator appears explicitly in `L(1,chi5)=2 log(phi)/sqrt5`.
- The earlier Lucas/harmonic residual keeps the norm-parity `(-1)^n` and the Bernoulli `-1/12` correction.

**What is NOT established:** the Galois action itself is NOT the analytic reflection, the norm parity is NOT the quadratic Frobenius character, untwisted Tate zeta integrals discard Gal-odd test sectors, and these shared structures do NOT prove signed Weil positivity, RH, or pi normality.

- [Full proof dossier / scoped claim ledger / countermodels](RESEARCH.md)
- [Next theorem, pass/fail gates, hostile controls](NEXT.md)
- [Stdlib exact arithmetic and finite calibration tests](../../../tests/test_quadratic_galois_tate_bridge.py)

Targeted command:

`python -m unittest discover -s tests -p 'test_quadratic_galois_tate_bridge.py'`

**Branch status:** draft only. Full-tree CI provenance and source contracts are separately required for integration.
