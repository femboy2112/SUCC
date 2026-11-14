# RH observer extension laboratory

**Research status: draft; no proof of RH or theological equivalence is claimed.**

A downstream Principia Observatoris example: elementary remainder probes, observer indistinguishability, bounded finite-to-infinite extension, and certified finite-precision reconstruction. The classical RH bridge is explicitly attributed; new-to-project deductions are not claimed as bibliographically novel.

Read [RESEARCH.md](RESEARCH.md) for definitions, proofs, carrier boundaries, TLICA typing, hostile controls and the claim ledger. The unchanged original research pack is [archive/round1.zip](archive/round1.zip). Its embedded RESEARCH_NOTE.md contains the full first-round write-up and references.

## Main additions

- Exact finite-prefix rigidity: the head coefficients are -mu_M(k), leaving one tail moment.
- A periodic pair-mean identity and rigorous O(T^-2) tail enclosure for each fixed rational coefficient list.
- Finite-precision target reconstruction equivalent to RH at the level of total certificate search; no uniform stable full inversion in the declared weighted data topology.
- An explicit hypothetical-zero blind source and stronger conditional global-norm lower bound.
- A certified 48-entry extension with 144 patterns, plus a failed 64-entry candidate retained as an adverse next-size check.

## Reproduce

Python 3.10+ is sufficient for the verifier and tests; NumPy/SciPy are needed only for optional floating proposal generation. Use the environment versions recorded in PROVENANCE.json to reproduce the proposal numerically. Acceptance never trusts the floating optimization.

```sh
cd research/rh_observer_extension
python -m unittest discover -s . -p 'test_*.py' -v
python certify.py certificates.json --cutoff 50000 --output /tmp/new-certificates.json
python certify.py holdout.json --cutoff 50000 --output /tmp/holdout.json
python -m zipfile -e archive/round1.zip /tmp/rh-observer-round1
cd /tmp/rh-observer-round1/observer_demon_research
sha256sum -c SHA256SUMS
python verify.py --output /tmp/round1-replay.json
```

From the lab directory, recheck the archived inputs with the sharper verifier:

```sh
python certify.py /tmp/rh-observer-round1/observer_demon_research/certificates.json --cutoff 10000
OPENBLAS_NUM_THREADS=1 python propose.py --N 48 --K 144 --output /tmp/proposal.json
python certify.py /tmp/proposal.json --cutoff 50000
```

A negative candidate is not a lower bound on the optimization class. The N=48 success and N=64 failure are both exact certificates, not a proof or disproof of a universal RH-equivalent assertion.

## Repository boundary

Publication parent: `db9fb4b84672050efa79b13377f1e73364598a14`, resolved from `heads/main`. Principia context was separately inspected at `f9efa624da06a28e1a8ac99a56499acd11197928`; this is not asserted to be the main tip. New lab files only; historical imports/defaults are untouched. Consult root [AGENTS.md](../../AGENTS.md), [METHOD.md](../../docs/METHOD.md) and [Principia at the inspected reference](https://github.com/femboy2112/SUCC/blob/f9efa624da06a28e1a8ac99a56499acd11197928/docs/principia_observatoris/README.md).

The root-required provenance script, full unittest suite and observer probes remain unrun because a full checkout was unavailable. This draft is not merge-ready on the strength of local lab tests alone. No license is added or changed.
