# Source map and live-frontier reconstruction

## Repository and exact states

Main was read live at `d32342d375f44ddf62221ad6aff2f534abdc0a03` before this
round. The working parent is PR541 at
`e8a4126754dc95eddeca758ea92ead50246da630`. The new isolated branch is
`research/driven-pinbed-observability-2026-11-07`. The user authorized pushes
to non-main branches. Historical source, tests, formal files, provenance
contracts, workflows and license are unchanged; the new work is additive.

| Source family | Exact source / inspected material | What it supplies |
|---|---|---|
| PR541 continuous pin bed | [e8a41267 theorem dossier](https://github.com/femboy2112/SUCC/blob/e8a4126754dc95eddeca758ea92ead50246da630/research/2026-11-07/fourier_yoneda_pinbed/THEOREMS.md), implementation and receipts | B2 inverse, affine naturality, sharp weighted metric dynamics, future completion, original BBP tail |
| PR542 finite oscillators | [c956b42f committed note](https://github.com/femboy2112/SUCC/blob/c956b42fff15270c10715870874f5cfa951de9df/research/2026-11-07/pinbed_yoneda_oscillators/RESEARCH_NOTE.md), complete note and changed-file list | Finite two-tone theorem, phase-power control, row closure, additive-input no-go; existing finite result credited |
| PR539 circle windows | [c8c5cf04 circle appendix](https://github.com/femboy2112/SUCC/blob/c8c5cf0488b3667b0f603983e9ad3766ba78e546/research/2026-11-07/harmonic_pisot_boundary/CIRCLE_WINDOW.md), complete appendix | Proper aperture, rational blind modes, golden conditioning, moving-frame counterfeit |
| PR540 golden aperture | [PR540](https://github.com/femboy2112/SUCC/pull/540), head `298f60d826a1f733b7eb09740b94248d8e40af60` rechecked; detailed dossier inspected in preceding PR541 round | Existing aperture energy/source transport; its estimate is not refuted by a different metric's conditioning |
| Main wavefront oscillator | [main module](https://github.com/femboy2112/SUCC/blob/d32342d375f44ddf62221ad6aff2f534abdc0a03/observational_succ/wavefront_oscillator_completion.py), header and source/pump definitions | Passive source versus externally replenished oscillator already distinguished; this work preserves that distinction |
| Main finite Fourier/source APIs | Existing finite_fourier_carrier, integer_bbp_carrier, carrier_relative_targets, AGENTS.md and METHOD.md | Exact arithmetic, original source, target semantics and repository gates |

PR542's published commit contains its research note and README. Its description
reports an expanded local bundle, but those uncommitted artifacts were not used
as implementation evidence here. This round commits its own complete module,
tests and exact independent programs. Personal-context retrieval located the
prior conversation only as a continuity lead; live source and replay carry the
claims above.

## Primary literature checked

- [NIST DLMF 24.8](https://dlmf.nist.gov/24.8), equations 24.8.1 and 24.8.3:
  classical Bernoulli Fourier expansions used by the B2 scan.
- [NIST DLMF 4.22.4](https://dlmf.nist.gov/4.22.E4): the csc² partial-fraction
  identity used to sum the exact alias radius.
- [Stanford Research Systems, Lock-In Amplifier Basics](https://www.thinksrs.com/downloads/pdfs/applicationnotes/Lock-In%20Basics.pdf),
  April 7, 2020: reference-sensitive mixing and the in-phase/quadrature pair.
  This is physical motivation and a sign/access comparison, not a source for
  SUCC's arithmetic theorem or evidence of physical execution.
- [M. G. L. Gustafsson, PNAS 102 (2005)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1201569/),
  doi:10.1073/pnas.0406877102: spatial frequency mixing and phase-separated
  structured illumination. This is a classical conceptual relative of the
  driven mask, not a claim that the mathematical bed is a microscope.
- [Kerodon 8.4.1](https://kerodon.net/tag/03V8): restricted Yoneda/density.
  The categorical statement here uses explicitly defined affine actions and
  an actual natural isomorphism on realizable pairs; scalar readings are not
  silently equated with Hom-sets.

The inverse, frame constants, range criterion, sharp ×16 norm, occupancy
certificate and source estimates are derived explicitly in this folder.
Scholarly priority has not been investigated sufficiently to claim it.

## Evidence dependence

Constructor, translator, adversary and root share a model family and classical
sources. Agreement is not four independent witnesses. The three independent
programs import no SUCC module; their arithmetic and decomposition differ from
the production implementation. This provides algorithmic cross-checking within
finite declared scopes, not independent authorship or formal verification.
