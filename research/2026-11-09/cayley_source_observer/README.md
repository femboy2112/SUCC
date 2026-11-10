# Cayley line-circle observer, sound source semantics and parity frontier

**Research branch, November 9, 2026.** Based on PR #576 at
`afabc458323ef2e3a20ce2bae77239c4190819c5`, above Main XXII
`43886e830cee5ff6d6b37719e18d809819673bd9`. This round connects Leah's
reciprocal-pi/line-at-infinity proposal to the actual current parity frontier,
while repairing the computational defects in the DeepSeek causal-weld work.

**Original-zero hexadecimal parity balance, base-16 normality of pi, and RH
remain OPEN.** The contribution is a checked observer, quantitative source
transport, a conditional binary-factor theorem, and soundness repairs.

## Results and boundaries

| Result | What is established | Where |
|---|---|---|
| Circle on a compactified line | Exact projective Cayley transport, Cauchy measure `dx/[pi(1+x²)]`, complete continuous oscillator observations and homogeneous parity sign | [Cayley proofs](CAYLEY_PROOFS.md), CAY-01–03 |
| Coupled source/oscillator clocks | Uniform time-and-frequency transport iff `H 16^(N-L)/L² -> 0`; explicit `h_n=32n²` gives phase error tending to 2 | CAY-04–06 |
| Common-horizon epoch transport | Completing the whole epoch to L=2A gives a clipped geometric error, vanishing whenever `log(1+H_A)=o(A)` | CAY-07 |
| Paid Fourier reconstruction | Exact parity Lipschitz constant; rational boundary/source budget; rational Taylor enclosure of the actual finite readout | [Boundary proofs](BOUNDARY_PROOFS.md), B01–03 |
| Boundary recursion | `b_(j+1)=(b_j+q_j)/2+e_j-a_j`, retaining signed real contrasts, endpoint cost and fourteen other preimage fibers | B04 |
| Binary future-conditioned gate | All fixed modes `m=8(odd)` vanishing implies half-turn symmetry, `O(delta^(1/4))` limit boundary mass, and every fixed parity word fair | B05; conditional arithmetic hypothesis OPEN |
| Strict hierarchy | Bernoulli digits 0/1 satisfy the gate without full hexadecimal Haar; fair parity words alone need not satisfy the gate; boundary avoidance alone need not balance parity | B05–06 countermodels |
| Sound computational semantics | Capture-free substitution, actual Church S/Vp, honest redex addresses and proof-backed affine cofinality | [Semantic audit](SEMANTIC_AUDIT.md) |
| Corrected research authority | Wrong constants, unsupported Fourier tail, F-9 necessity and Lean/C-monoid overstatements explicitly scoped | [Errata](ERRATA.md) |

## How this attaches to the existing frontier

The existing two-fiber Aphex contrast is a **prime-sign-conditioned** real
complement. The new half-turn contrast is a **real geometric** quantity on
the folded phase `u=8t`. They are not identified. The same current hexadecimal
parity can be read through either representation; the old exact calibration
and all prime/complement/winding obligations remain in force.

The Fourier–Yoneda pinbed supplies a continuous observable algebra; the
Cayley map changes its chart exactly. The Scott weld supplies rational
source cones; the new clock conditions specify how much cone precision an
oscillator family consumes. The genuine source mark, time and lift must stay
attached because a complete circle observer still loses integer winding and
can alias distinct seeds.

The binary gate is a specialization of the existing future-conditioned Haar
recursion, not a theorem that marginal balance creates independence. Its
strictly weaker target is useful: prove selected cancellation only on the
progression `8,24,40,...` and pay boundary passage automatically. None of
these selected estimates is supplied by a chart change or by this round's
finite certificates.

## Read and reproduce

- [Faithful indexed source-clock action and its limits](AFFINE_SOURCE_ACTION.md)
- [Claim ledger and hole contract](CLAIM_LEDGER.md)
- [Source map](SOURCE_MAP.md)
- [Frozen finite protocol](PROTOCOL.md) and [exact receipt](FINITE_RECEIPT.json)
- [Validation and limits](VALIDATION.md)
- [Next arithmetic dependency](NEXT.md)

```sh
python -m unittest tests.test_cayley_source_observer \
  tests.test_parity_boundary_certificate tests.test_scott_omega_semantic_soundness -v
PYTHONPATH=. python research/2026-11-09/cayley_source_observer/experiment.py
PYTHONPATH=. python research/2026-11-09/cayley_source_observer/affine_source_probe.py
```

No historical source archive, original forcing, zero seed, main branch or
release is modified by this research round. Paper proofs and finite tests
have different authority; neither is relabelled as a full Lean formalization.
