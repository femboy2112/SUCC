# Observational SUCC

**How does a finite observer turn causal contact into mathematical knowledge?**

Observational SUCC studies that question through explicit sources, carrier dynamics,
observations and proof certificates. An observer receives a finite history of interactions,
builds a relational model, and reasons within a declared proof system. The mathematics asks
which features survive changes of representation, what information an observation loses,
and what additional evidence would distinguish models that currently look the same.

The arithmetic applications test the framework; their missing estimates remain separate
proof obligations.

| Current status | What the repository supports |
|---|---|
| Foundations and toolkit | Exact finite models, transport identities, information bounds, counterexamples and scoped kernel-checked lemmas |
| π base-16 normality | **OPEN** — the original-source signed cancellation estimate is missing |
| Original-zero hexadecimal parity balance | **OPEN** — fair parity words and even one-digit balance need a source-selected estimate |
| Riemann hypothesis | **OPEN** — a separate prime–Archimedean positivity program |

Start with the [current mathematical frontier](docs/PI_NORMALITY_FRONTIER.md), or read the
[foundations](docs/FOUNDATIONS.md) for the general theory. The
[Main XXIII audit](docs/SUCC_MAIN_XXIII_INTEGRATION_AUDIT_2026-11-10.md) records the candidate's
coverage, qualifications and validation limits.

## The mathematical idea

The organizing pipeline is:

**source → carrier dynamics → observation → relational model → proof certificate**

A **source** specifies what actually drives a system. Its **carrier** evolves by a lawful
successor operation; an **observation** exposes only part of that state. A **relational model**
records the distinctions and compatibility laws available to the observer. A **certificate**
justifies a precisely scoped conclusion using an explicit checker or derivation.

Each arrow has a mathematical contract. Transporting an observable accurately does not
prove that its long-time mean vanishes. An observer that predicts a path perfectly need not
observe a typical path. A positive covariance does not identify an arithmetic functional.
Keeping these distinctions explicit lets a failed shortcut produce a useful theorem,
counterexample or sharper experimental question.

SUCC uses categorical diagrams to organize actual maps and coherence laws, finite-state
models to expose information limits, and classical analysis and exact arithmetic to test
source-specific claims. Physical and semantic intuition motivates the work; its mathematical
interpretations carry separate hypotheses. Finite observations do not execute an infinity
or establish a universal theorem.

## A concrete source: the BBP orbit

The authenticated example keeps all four signed poles and the literal zero seed:

```math
r(n)=\frac{4}{8n-7}-\frac{2}{8n-4}-\frac{1}{8n-3}-\frac{1}{8n-2}.
```

```math
U_0=0,\qquad U_n=16U_{n-1}+r(n).
```

The positive future correction connects this rational recurrence to π exactly:

```math
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad U_n+T_n=16^{n-1}\pi.
```

This is an exact source identity. The open normality problem asks whether the completed
orbit visits every hexadecimal word of length $`k`$ with limiting frequency $`16^{-k}`$.
Proved Green-tail bounds transfer suitable observations between the rational and completed
orbits. They do not supply the signed cancellation that would prove normality.

The [source implementation](observational_succ/duck_bbp.py),
[integer carrier](observational_succ/integer_bbp_carrier.py) and
[source provenance](provenance/README.md) make the contract inspectable. Research retains
integer carries, old prime powers, the global CRT winding and real boundary costs.

## Current research frontier

The [Main XXIII tool atlas](docs/MAIN_XXIII_TOOL_ATLAS.md) connects the complete
BBP carry and CRT state to inverse-beta and Mellin roots, the Ω₄/Ω₅ Haar
diamond, and reversible arithmetic. It identifies the exact signed estimate
still needed for hexadecimal parity words. Intrinsic Hamiltonians and
the Riemann hypothesis occupy a separate downstream track.

**Cayley source observers and semantic repairs** connect the line–circle picture
to the actual BBP source without changing its seed. The
[research follow-up](research/2026-11-09/cayley_source_observer/README.md)
adds exact projective dynamics, source-clock compatibility, boundary-aware parity
certificates, and a conditional binary-future criterion strictly weaker than full
normality. It also corrects the lambda, omega, cofinality and asymptotic claims
in the causal-weld draft. The original-zero signed estimate remains **OPEN**.

**Young Nastyman's Haar measure** asks how uniformity of a complete observed law can be
certified. The recursive sixteen-child construction retains the entire future tail;
[its sharp transport inequality](research/2026-11-09/recursive_haar_pinbed/THEOREMS.md)
separates true Haar symmetry from a merely uniform first digit.

**Wonderboy's signed successor wavelets** compare the two orientations of chronological
word transport. Their [exact junction identities](research/2026-11-09/tenacious_d_haar/PROOFS.md)
retain endpoint costs and distinguish positive collision energy from signed cancellation.
Fine-scale empirical energy has an unavoidable finite-sample floor, even for normal paths.

**Complete CRT parity** expresses real digit parity as a prime-local sign times its entire
real/CRT/winding complement. [The parity dossier](research/2026-11-09/pi_parity_pressure/PROOFS.md)
keeps the terms that prime-by-prime marginal uniformity cannot determine.

**The Aphex two-fiber observer** identifies the fitted coefficient with half the difference
between the two prime-sign-conditioned complementary responses. Its
[sharp finite certificate](research/2026-11-09/aphex_two_fiber_haar/PROOFS.md) bounds the gap
between that coefficient and actual digit parity by the prime-sign imbalance. Decay of the
coefficient is **OPEN**. A same-forcing coherent wrong seed has zero fitting loss and
maximally biased parity, so learning accuracy cannot close the theorem.

These are connected tools with different domains. Binary conditional Haar is not full
sixteen-child Haar; digit Walsh parity is not one real-circle Weyl character. The
[maintained frontier](docs/PI_NORMALITY_FRONTIER.md) gives the definitions, hypotheses,
controls and exact next target. The [Gamma definition table](docs/MAIN_XXII_GAMMA_OBSERVABLES.md)
keeps the distinct source finite parts, Mellin laws and matrix observers separate.

## Mathematical toolkit

- **Observation and proof access:** finite histories, causal models, forgetting and recovery
  contracts; [observer atlas](docs/CATEGORICAL_OBSERVER_ATLAS.md).
- **Exact arithmetic and certificates:** rational source states, integer digit enclosures,
  hostile controls and scoped Lean checks; [architecture](docs/ARCHITECTURE.md).
- **Harmonic and symbolic analysis:** signed Fourier/Walsh observations, Haar projectors,
  entropy and collision identities; [frontier](docs/PI_NORMALITY_FRONTIER.md).
- **Research navigation:** typed concepts and claim discovery in the
  [mathematical memory index](docs/math_memory/INDEX.md), with current scope in the
  [Main XXII supplement](docs/CLAIM_SUPPLEMENT_MAIN_XXII.md).
- **Independent RH research:** completed source, Gamma/pole terms and signed positivity
  obligations; [RH handoff](docs/RH_HANDOFF.md).

## Quickstart

Python 3.10 and 3.13 are the supported CI targets. From a local checkout:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[test]'
export PYTHONPATH="$PWD"
python -m observational_succ demo
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_aphex_two_fiber_haar.py' -v
```

For complete native validation, run
`python -m unittest discover -s tests -p 'test_*.py'`.
The suite is substantial; use the [round's validation receipts](docs/SUCC_MAIN_XXII_INTEGRATION_AUDIT_2026-11-09.md)
for exact tested commits and outcomes. A passing test certifies its tested behavior;
analytic and kernel proof authority are recorded separately.

## Documentation

| Read | Purpose |
|---|---|
| [Foundations](docs/FOUNDATIONS.md) | Objects, physical intuition and logical boundaries |
| [Method](docs/METHOD.md) | Steelman → crucible → labeled verdict |
| [Architecture](docs/ARCHITECTURE.md) | Maps, modules and trust boundaries |
| [Current π frontier](docs/PI_NORMALITY_FRONTIER.md) | Proved tools, open arithmetic gates and countermodels |
| [Claim ledger](docs/CLAIM_LEDGER.md) · [Main XXII supplement](docs/CLAIM_SUPPLEMENT_MAIN_XXII.md) | Claim status and supporting evidence |
| [Roadmap](docs/ROADMAP.md) | Longer-term research directions |
| [Research history](docs/RESEARCH_HISTORY.md) | Archived README, integration history and primary dossiers |
| [Intellectual provenance](docs/idea_provenance/README.md) | Original intuitions → steelmans → exact results → counterexamples, including the Aphex equation story |
| [Contribution guide](CONTRIBUTING.md) | Reproduction, attribution and review expectations |

## Research honesty

A classical theorem keeps its attribution. An exact finite identity, a conditional reduction,
a numerical observation and a kernel-checked lemma carry different authority. Every
substantial proposal should expose its domain, hypotheses, quantifiers, provenance,
adversarial controls and next falsification opportunity. Attractive diagrams and many
agreeing measurements do not pay a missing proof obligation.

The [frozen import manifest](provenance/IMPORT_MANIFEST.json) preserves the project's original
source history. Earlier dossiers remain available with their historical meaning; maintained
supplements clarify their scope. No redistribution license has been selected by the maintainer.
