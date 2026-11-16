# Source-attached interference atlas

## Result

This continuation of #643 answers “find them all” with **74 indexed entries**
and **12 paper propositions**. The entries cover the named current pi
proof-obligation families in the pinned inventory. The propositions give a
complete compiler for a declared finite phase algebra, identify exactly what
its character reports can recover, and construct a single all-harmonic
Gamma-sampled response equivalent to the remaining normality gate.

The original four-pole BBP recurrence and literal zero seed are preserved.
No source-selected R0 bound, parity bound or normality estimate is proved.
The work resolves response construction and information-loss questions;
the named arithmetic limits retain their OPEN status.

### Read these first

| Artifact | Purpose |
|---|---|
| [THEOREMS.md](THEOREMS.md) | IA-01–12, with proofs, domains, quantifiers and costs |
| [FRONTIER_MAP.md](FRONTIER_MAP.md) | Human-readable inventory of all 74 entries and inherited source key |
| [FRONTIER_TARGETS.json](FRONTIER_TARGETS.json) | Machine-readable target, response, logical strength, controls and remaining obligation |
| [NEXT.md](NEXT.md) | The source-specific inequalities that would move an arithmetic rung |
| [VALIDATION.md](VALIDATION.md) | Actual runs, failures, review corrections and exact snapshot coverage |
| [PROVENANCE.md](PROVENANCE.md) | Parent, donor and primary-source attribution |
| [CLAIM_LEDGER.json](CLAIM_LEDGER.json) | Proof versus finite observation versus open arithmetic claims |

## The response algebra

For accessible labelled phase channels z and a Gaussian-rational Hermitian
matrix H, IA-01 constructs

    z* H z = sum_l w_l |a_l z|^2,

with at most 2d²−d rows and each row normalized to be a valid bounded
intensity. The signs remain in classical postprocessing. The total absolute
weight C gives both a sampling budget and a precision-amplification budget.
This supplies a concrete observation program; it does not bound the program's
source-selected expectation.

Products and conjugates of unit-phase characters produce every finite
trigonometric polynomial on a finite list of labelled clocks. Tensor lifting
retains the actual joint channel. It does not introduce independence between
clock coordinates. The integer character lattice gives the exact remaining
gauge. Complex pair data leave one common phase per connected component;
a calibrated reference removes it. For the actual same-forcing seed family,
the surviving aliases are a reciprocal-gcd lattice instead of an arbitrary
torus rotation.

## One all-mode response, with an inherited energy

Let W_B(h) be the completed source's h-th Fourier mean over every integer
shell B≤n<2B. Draw an external Gamma clock tau with shape 1 and scale 1,
then K conditional on tau from Poisson(tau), and set H=K+1. The exact law is
Pr(H=h)=2^−h for h≥1. Independently sample two source clocks I,J from the
same full shell, with replacement, and use the pair click

    Pr(click | H,I,J) = |e(H Y_I) − e(H Y_J)|² / 4.

Its mean is (1−E_B)/2, where

    E_B = sum_(h≥1) 2^−h |W_B(h)|².

E_B→0 is equivalent to base-16 normality. The expected click therefore tends
to **1/2**, not 1. Repeating a trial until one sees a hit is a different response.

This energy is **exactly the repository's inherited SCE-01 Poisson energy**,
after the normalization E_SCE=1+2E_B. The present contribution is its explicit
Gamma-sampled readout, label-sensitive controls, and whole-mixture source and
precision account. General characteristic-kernel theory is also prior art.
No novelty is claimed for a new normality criterion.

Using the original rational source instead of completed Y costs less than
11/(28B²) in E_B, and half that in mean click probability. Cutting the
unnormalized frequency sum after L costs at most 2^−L. These two explicit
budgets prevent an illicit fixed-frequency-to-growing-band substitution.

## The finite counterfeits are actual radix orbits

For q=3^a5^b and M=q/15, a,b≥1, the actual ×16 orbit of 1/q is an equally
spaced coset with Fourier mean e(h/q) when M divides h and zero otherwise.
Taking M above any finite harmonic band passes that whole band exactly,
despite periodicity. Repeated de Bruijn words similarly pass every word test
through a chosen fixed depth while remaining periodic. These controls can
share the original forcing only by an explicit seed change; their failed
zero-anchor authentication is recorded.

The periodic coset's universal energy is epsilon_M=1/(2^M−1). There is no
uniform positive detector gap separating all nonnormal orbits from Haar.
In the declared two-rival report model, retaining (H,click) gives chi-square
epsilon_M; retaining only click gives epsilon_M². The fixed-error sample
orders are therefore 2^M and 4^M respectively. These bounds exclude richer
reports and frequency choices tailored to a known M.

## What is covered

The inventory contains full normality equivalents, weaker R0/R1/CH/AM/entropy
rungs, prescribed-scale sufficient energies, conditional carry and prime
complement gates, source/Haar/chronological reconstructions, and explicitly
separate bases and arithmetic problems. Each row says whether its response
is finite, conditional on further source inputs, an infinite limit with a
truncation contract, or outside the finite phase grammar.

The 74 entries are **not 74 independent theorems, 74 implemented algorithms,
or 74 experiments that prove pi normality**. The catalogue retains exact
antecedents, overlap and superseded wording. Its completeness boundary is
the finite source inventory in [HOLE_CONTRACT.md](HOLE_CONTRACT.md).

## Implementation

Three additive modules and their matching tests are provided:

- `observational_succ/interference_forms.py`: labelled characters, signed
  Hermitian intensity compilation, reference/pair templates and exact budgets.
- `observational_succ/interference_controls.py`: gauges, seed aliases,
  genuine periodic radix controls, finite words, Walsh interactions and report laws.
- `observational_succ/universal_interference_detector.py`: geometric
  harmonic law, exact kernel, cutoff intervals, original-source transfer,
  lag benchmarks and retained-label statistical budgets.

All finite numerical verdicts use exact integers and rational arithmetic.
The independent audit's optional high-precision Gamma quadrature is labelled
as a diagnostic and kept out of the exact assertion count. These interfaces
are bounded; generic rational circle fixtures are not asserted to be BBP
phases, and an arbitrary real phase oracle is not implemented.

## Reproduction

From the repository root:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
python research/2026-11-15/pi_interference_atlas/independent_audit.py --out /tmp/interference-independent.json
python research/2026-11-15/pi_interference_atlas/catalogue_audit.py --out-dir /tmp/interference-catalogue
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
```

The exact repository gate commands and receipts are authoritative in
VALIDATION.md; the published full-suite receipt identifies the isolated
parent-plus-six-files production snapshot. The new dossier does not change
historical originals, canonical frontier text, source proofs or existing code.
