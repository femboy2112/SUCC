# Provenance and scope of the new interface

## Frozen parent and source preservation

This additive round is based on draft [#639](https://github.com/femboy2112/SUCC/pull/639),
commit `2c73e6388b24c7a66683d089733105d14acda08a`, on a new research branch.
The original source, zero seed, historical dossiers and production defaults are
unchanged. Live GitHub PR metadata and the local branch were rechecked at the
start. The three production additions use exact finite models; the written
proofs state their broader domains separately.

## Exact inherited objects

Every Git blob below was read from the pinned parent. Full machine-readable
pins are in `receipts/inherited_blobs.json`.

| Inherited file | Git blob |
|---|---|
| `observational_succ/recursive_observer.py` | `b32575cc099e4514484192a260393e15951404a7` |
| `observational_succ/source_authentication.py` | `33116a774da66b9775eae221eacae90b8c69dede` |
| `observational_succ/gauge_anchored_observer.py` | `8fbbb02053d7c76ac2393bb81c865c5df3af621f` |
| `observational_succ/contextual_heuristics.py` | `908b207b8eddd5be9ca33d90f8f9bade0150ec5f` |
| `observational_succ/heuristic_shape_learning.py` | `d57237ca7fdc81e49e4377b3dc721190130915f0` |
| `observational_succ/heuristic_evidence_martingales.py` | `bd051978d703b71f1659ff63d404c3da35f33757` |
| `observational_succ/quantum_records.py` | `76fae4755c93c1d192388b0c4d1973705df4e1b7` |
| `observational_succ/arithmetic_tfd.py` | `fb98e4bf30ace8aaac920e446e93aa1580ee5502` |
| `observational_succ/zero_anchored_haar.py` | `f4dc253df99db877bef24f3fbbad70b227ae4ee6` |
| `observational_succ/aphex_haar_feedback.py` | `7c20a281f2be800b2fea17ca9f3941b1561930f7` |
| `observational_succ/gamma_source_volume.py` | `b52607bc7b0ac468252c7aa4dc1ce399e42c0309` |
| `research/2026-11-14/gamma_volume/THEOREMS.md` | `881436b8b3648e0bab271dadf9e4e16d2c3e199f` |
| `research/2026-11-10/omega_bbp_operational_completion/OMEGA_HAAR_WAVELET.md` | `ee0663ec1760c1da03f6dd062280bc66ce592321` |
| `research/2026-10-22/ARITHMETIC_ER_EPR_FOUNDATIONS.md` | `5923ba1e668b590025255c413f6c93fd69886dd4` |
| `research/2026-11-14/source_auth_field_frontier/THEOREMS.md` | `072965d50367c1d79fd3ba748a8bbd6be64e984c` |
| `research/2026-11-14/recursive_observer_fixed_point/THEOREMS.md` | `9c8e3416049913ca999f6f5f9eac5cf726fa1ad0` |

## What is inherited and what is added

- Principia #625–630 already supplies stochastic histories, source-labelled
  joint instruments, retrospective/current beliefs, lawful action selection,
  Bayes-risk policies, calibrated adaptive likelihood ratios, and source-map
  restrictions. The new four-state interface uses those rules and preserves
  its full joint belief after deep observations.
- Contextual heuristics already supplies freshness/epoch/receipt and replay
  checks. Heuristic shape learning already uses conditional covariance and
  projection gain. The new result is the explicit hidden-connection Haar/MI
  calibration, its bounded innovation energy and certified preparatory-probe
  option value. Generic Bayesian updating and information gain are classical.
- Zero-anchored Haar is an exact observer of completed BBP radix phases. Omega
  Haar distinguishes overlapping chronological projections from commuting
  exact source foldings; Aphex feedback provides a declared least-squares
  response-gain model. The present weighted source-coordinate Haar basis is
  different and is not silently substituted for any of those instruments.
- Gamma-volume GV-04–07 already has Gamma subordination, retained source-depth
  laws, the report-composition defect, the native covariance constant and
  infinite Hankel rank. This round localizes that authentic covariance into
  weighted Haar details with a finite residual bound and rational certificates.
  The reversible Hilbert-space Gram specialization has additional hypotheses.
- Arithmetic ER/EPR already constructs a mathematical thermofield state,
  distinguishes its dephased mixture, and proves no-signalling. The new bounded
  real-qubit code extends `quantum_records.Instrument` to explicit two-party
  outcome branches, matched classical controls, trusted Haar-axis witnesses
  and a rational rotated-setting CHSH discriminator.

These are new interoperable SUCC interfaces and source-specific corollaries;
no scholarly-priority claim is made for the classical foundations or witnesses.

## Primary mathematical and physical sources

1. Foster et al., *A Unified Stochastic Gradient Approach to Designing Bayesian-Optimal
   Experiments* (2020), [primary paper](https://proceedings.mlr.press/v108/foster20a/foster20a.pdf),
   section 1 equation (1): expected information gain as expected posterior
   entropy reduction. Foster et al., *Deep Adaptive Design* (2021),
   [primary paper](https://proceedings.mlr.press/v139/foster21a/foster21a.pdf),
   sections 2–2.1: history-adaptive experiment design. Our finite proofs and
   exact option-value example are given directly, without using their algorithms.
2. Shafer, Shen, Vereshchagin and Vovk, *Test Martingales, Bayes Factors and
   p-Values* (2011), [author manuscript](https://arxiv.org/pdf/0912.4269):
   nonnegative martingale evidence and maximal inequalities. The repository's
   newer e-process interfaces and their filtration restrictions are inherited.
3. Durrett, *Probability: Theory and Examples*, fifth-edition author manuscript,
   [primary author source](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
   theorems 4.1.13/4.1.15: tower law and orthogonal conditional expectation.
   The finite weighted Haar formulas are proved explicitly in this dossier.
4. Gentil and Maheux, *Super-Poincare and Nash-type Inequalities for
   Subordinated Semigroups*, [author paper](https://arxiv.org/pdf/1105.3095)
   (arXiv submission 2011), equations (4), (6)
   and example ii: positive subordination and the Gamma logarithmic generator.
   The finite spectral proof and original-source multiplication model are
   separately specified here.
5. Wiseman, Jones and Doherty, *Steering, Entanglement, Nonlocality, and the EPR
   Paradox* (2007), [primary paper](https://arxiv.org/pdf/quant-ph/0612147):
   steering and local-hidden-state exclusion are distinct from separability
   and Bell nonlocality. Conditional updates alone do not certify steering.
6. Maldacena and Susskind, *Cool horizons for entangled black holes* (2013),
   [primary paper](https://arxiv.org/pdf/1306.0533), introduction and sections
   2.7/3.1: particular entangled-black-hole interpretations, a broader proposed
   ER=EPR extension, and no-signalling. We do not turn that conjecture into a
   theorem about all statistical or mathematical correlations.
7. Gao, Jafferis and Wall, *Traversable Wormholes via a Double Trace Deformation*,
   [primary paper](https://arxiv.org/pdf/1608.05687): an added boundary coupling
   enables traversability in its specified model while preserving causality.

The root independently opened the primary Bayesian, martingale, steering and
ER papers; the translator additionally inspected the conditional-expectation,
subordination and adaptive-design sources. Source references are constraints
on the derivation, not evidence of a physical SUCC implementation. Agent
reviews share model and repository provenance and are not independent truth
probabilities.

## Novelty and measurement boundary

A fixed mathematical kernel can be represented by many observation models.
The original-source Haar decomposition is proved for its declared integral
measure. The Markov graph, hidden binary connection, quantum state and probe
costs are explicitly constructed models. We have not measured a hidden quantum
state of mathematical reality, implemented a gravitational dual, authenticated
physical independence, or transported the native source Haar slices into a
signed all-horizon BBP phase estimate.
