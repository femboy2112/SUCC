# Observational SUCC

**How does a finite observer turn causal contact into mathematical knowledge?**

Observational SUCC studies explicit sources, their evolving carriers, the information
an observer can recover, and the certificates that justify a conclusion. Category
theory organizes actual maps and their coherence; exact arithmetic and analysis
test what survives those maps. Physical and semantic intuition motivates the theory.
Its mathematical interpretations have separately stated hypotheses.

The current arithmetic machine follows one chain:

**source → exact carrier → zero-seed authentication → Dedekind/Yoneda identity
→ computational observers → signed statistical proof obligations.**

The machinery now identifies and computes the intended π source in several coherent
ways. The source-selected cancellation needed for normality remains unproved.

| Research target | Current status |
|---|---|
| Source identities, finite observers and categorical reconstruction | Scoped classical/paper proofs and exact finite certificates; proof authority is stated per result |
| Source-selected signed cancellation | **OPEN** |
| Weakest signed rung R0: binary digit changes of π have positive lower shell density (`limsup Re W_(B,1) < 1`) | **OPEN** |
| Original-zero hexadecimal parity balance and parity words | **OPEN** |
| π base-16 normality | **OPEN** |
| Completed Weil positivity / Riemann hypothesis | **OPEN**, a separate prime–Archimedean program |

Start with the [mathematical frontier](docs/PI_NORMALITY_FRONTIER.md) and the
[next research handoff](docs/MAIN_XXV_HANDOFF.md) (which continues the
[Main XXIV handoff](docs/MAIN_XXIV_HANDOFF.md)). Exact integration coverage,
repairs and candidate validation receipts belong to the
[Main XXV audit](docs/SUCC_MAIN_XXV_INTEGRATION_AUDIT_2026-11-12.md) and
[manifest](docs/SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json); the
[Main XXIV audit](docs/SUCC_MAIN_XXIV_INTEGRATION_AUDIT_2026-11-11.md) and
[manifest](docs/SUCC_MAIN_XXIV_INTEGRATION_MANIFEST_2026-11-11.json) remain the record of the
previous consolidation.

Main XXV adds no estimate. It identifies the signed statements strictly between
"irrational" and "normal" as a ladder (R0 ⟸ R1 ⟸ digit-change density ⟸ … ⟸ normality),
gives each rung a threshold in the canonical Haar-defect units (`1/4`, `1/60`, …), proves
that any fixed saving needs a base-16 Diophantine exponent strictly below 1 — which no
irrationality measure of π can supply — and records where such an exponent is known
(`log(16/15)`, by import) and why that mechanism does not reach π.

## Source and exact carrier

The authenticated BBP recurrence retains all four signed poles and the literal origin:

```math
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
```

Its rational states have the exact completed identity

```math
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad U_n+T_n=16^n\frac\pi{16}.
```

The [source](observational_succ/duck_bbp.py),
[integer carrier](observational_succ/integer_bbp_carrier.py), and
[import provenance](provenance/IMPORT_MANIFEST.json) fix what is being observed.
Source clocks, integer carries, old prime powers, global CRT winding and real
future tails remain part of the transport contract.

Scott–Ω syntax, [source-clock actions](research/2026-11-09/cayley_source_observer/AFFINE_SOURCE_ACTION.md),
[intrinsic arithmetic operators](research/2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md),
and [graph resonance](research/2026-11-10/bbp_graph_resonance/RESEARCH_NOTE.md)
provide complementary representations. Their exact algebra does not determine the
long-time signed law of the selected orbit.

## Authenticate the zero and identify the real

Write $`x=\pi/16`$ and $`P_n=\sum_{j=1}^n16^{-j}r(j)`$. An unwrapped seeded state obeys

```math
U_n(s)=16^n(s+P_n),\qquad Z_n=16^{-n}U_n(s)-P_n=s.
```

The [identity kernel](research/2026-11-10/circle_line_lr_observer/zero_anchor_identity/README.md)
extends seeds to the exact module $`s=a+bx`$, $`a,b\in\mathbb Q`$. Imported π
irrationality makes these coordinates unique. It rejects both the coherent wrong
seed $`-x`$ and the rational shift $`1/16`$, even though the latter aliases all later
fractional phases. Recovering the seed requires the complete unwrapped state.

Strict rational source intervals determine the real's Dedekind cut. Rational cut
presheaves recover order fully faithfully; [numerical categories and rational
witnesses](research/2026-11-10/cursed_categorical_computation/README.md) make the
maps and their variance explicit. The [independent irrational-cut formulation](research/2026-11-10/cursed_categories_dedekind_yoneda/README.md)
retains its distinct domain. An ordered category, a labelled computation graph and
an action groupoid have different equivalence contracts.

## Compute certified observations

The [geometric circle/line observer](research/2026-11-10/circle_line_lr_observer/README.md)
derives rational enclosures from the Euclidean metric, without a supplied π-value
oracle. A finite program with unbounded integer registers produces every requested
finite Stern–Brocot L/R prefix. Its [aperiodic extension](research/2026-11-10/aperiodic_circle_observer/README.md)
turns each proposed periodic tail into a finite rejection certificate, under explicit
classical nonquadraticity assumptions. Infinite mathematical recovery is distinct
from physically executing an infinite computation.

For every denominator bound $`H`$, the [Farey shield](research/2026-11-10/circle_line_lr_observer/height_shield/README.md)
computes one certificate separating π from **every** reduced rational of denominator
at most $`H`$, with a strict rational margin. A computable nonnormal irrational also
admits such shields. Complete identification and productive computation therefore
leave the statistical theorem unpaid.

The [typed Lambda–Haar compiler](research/2026-11-10/zero_anchored_lambda_haar/README.md)
preserves rational source states through finite, capture-free reductions. Its
interval, digit-character, Pascal and signed-CDF backends certify finite observations.
[The alternative compiler](research/2026-11-10/zero_anchored_lambda_haar/README_ALTERNATIVE_589.md)
keeps independent tests and countermodels. The symbolic irrational seed kernel is
separate; a full compiler integration for that enlarged module remains unverified.
Exhausted computation reports UNKNOWN/UNRESOLVED.

## The statistical frontier

The target is the actual original-zero radix orbit, with Fourier arguments in turns:

```math
W_{N,h}=\frac1N\sum_{n=0}^{N-1}
\exp\!\left(2\pi i h16^n\frac\pi{16}\right)\longrightarrow0
\quad\text{for every fixed }h\in\mathbb Z\setminus\{0\}.
```

This is the classical Weyl criterion for π's base-16 normality. The
[Basel–Tauberian bridge](research/2026-11-10/basel_crt_omega_phasebridge/SIGNED_BASEL_TAUBERIAN.md)
recasts it as a signed source-selected tail estimate. The
[signed CDF overlap](research/2026-11-10/zero_anchored_lambda_haar/CONSTRUCTION.md)
isolates cancellation between adjacent temporal blocks. The
[zero-seed microscope](research/2026-11-10/zero_seed_microscope/README.md)
separates universal coarse seed averaging from the deep resolution needed to recover
the distinguished zero. These are precise proof interfaces; their missing arithmetic
estimates remain **OPEN**.

The [2→3 joining controls](research/2026-11-10/basel_crt_omega_phasebridge/ratio_fiber_joinings/README.md)
show that Haar marginals can coexist with strong dependence. One vanishing mixed
coefficient does not prove independence or normality. Hexadecimal digit parity is
a discontinuous digit character, so it also needs boundary and index corrections
when compared with smooth Fourier observations.

The [frontier](docs/PI_NORMALITY_FRONTIER.md) retains the full sixteen-child Haar
projector, signed overlap and error payments, conditional prime/parity machinery,
hostile seeds and source mutants. The [completed Weil research](research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/README.md)
keeps genuine prime powers, Gamma/pole terms and winding; positivity supplies no
automatic off-diagonal decay or RH-to-normality implication.

## Run and navigate

From a checkout with the repository's test dependencies installed:

```sh
python -m pip install -e '.[test]'
export PYTHONPATH="$PWD"
python -m observational_succ demo
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_zero_anchored*.py'
```

Full native validation is `python -m unittest discover -s tests -p 'test_*.py'`.
The handoffs ([XXV](docs/MAIN_XXV_HANDOFF.md), [XXIV](docs/MAIN_XXIV_HANDOFF.md)) list focused research replays. Test success,
written proof and kernel verification retain their separate authority; exact tested
commit identities and hosted outcomes are recorded in the integration audit.

| Read | Purpose |
|---|---|
| [Foundations](docs/FOUNDATIONS.md) · [Method](docs/METHOD.md) | Theory, interpretation and steelman–crucible–verdict discipline |
| [Architecture](docs/ARCHITECTURE.md) · [Observer atlas](docs/CATEGORICAL_OBSERVER_ATLAS.md) | Actual maps and trust boundaries |
| [Claim ledger](docs/CLAIM_LEDGER.md) · [Main XXV supplement](docs/CLAIM_SUPPLEMENT_MAIN_XXV.md) · [Main XXIV supplement](docs/CLAIM_SUPPLEMENT_MAIN_XXIV.md) | Scoped claims and their evidence |
| [Mathematical memory index](docs/math_memory/INDEX.md) | Concepts and generated claim discovery |
| [Roadmap](docs/ROADMAP.md) · [Research history](docs/RESEARCH_HISTORY.md) | Next campaigns and preserved earlier work |
| [RH handoff](docs/RH_HANDOFF.md) | Separate completed-source positivity program |
| [Intellectual provenance](docs/idea_provenance/README.md) · [Contributing](CONTRIBUTING.md) | Original intuitions, attribution and reproduction |

The [previous README](docs/archive/README_PRE_MAIN_XXV_2026-11-12.md) is preserved
byte for byte, as is [its predecessor](docs/archive/README_PRE_MAIN_XXIV_2026-11-11.md). Classical theorems keep their attribution; finite certificates do
not establish universal statistics. No redistribution license has been selected
by the maintainer.
