# Counterfactual Triangle Validation — 2026-10-31

**Baseline:** Main XVII merge e8598cfa5d32fd1de8e94a3e458a366a0850d59e.

A standalone exact Fraction prototype was executed locally. The first Ward test exposed a programming fault: integer zero defaults in the endpoint vector divided by N produced floats. This was repaired using explicit Fraction(0), and ten focused tests passed. The committed root regression also includes an explicit coherent changed-seed control; its exact-head CI result is the appropriate final repository-integration gate.

The authentic selected rational BBP prefix gave the following **finite observed** cardinal-hat L1 discrepancies, reported as rounded decimal displays of exact rational quantities:

| N | q=16 | q=256 |
|---:|---:|---:|
| 32 | 0.515291242643 | 1.593874036265 |
| 64 | 0.435739561810 | 1.309765040088 |
| 128 | 0.189292534049 | 0.907899341815 |
| 256 | 0.159178641417 | 0.611814858062 |
| 512 | 0.086098659866 | 0.434904331842 |
| 1024 | 0.076869698873 | 0.308330090746 |
| 2048 | 0.047599266005 | 0.205690867682 |

Observed Ward L1 for q=16 at N=256,512,1024,2048: 0.019157401327, 0.009577617945, 0.005113516819, 0.002542342041. Corresponding exact rational source-upper bounds displayed to six digits: 0.039288, 0.019672, 0.009843, 0.004923. Finite observations do not certify any limit.

Controls: exact original four-pole rational identity and positive regrouping; BBP-only independently bracketed first 18 hexadecimal digits of π; positive Green tails and outward enclosure; full 15-channel Walsh Parseval and L-infinity localization; periodic and de Bruijn nonnormal aliases; triangle partition, exact L1-Lipschitz, refinement and Ward coboundary; non-Haar Dirac and coherent original-forcing changed-seed controls.

**Reproduction on branch:**
- Focused: python -m unittest discover -s tests -p 'test_counterfactual_triangle_carrier.py' -v
- Provenance: python scripts/verify_provenance.py
- Foundations: python scripts/observer_foundations_probe.py
- Ordinal: python scripts/ordinal_succ_report_probe.py
- Full suite: python -m unittest discover -s tests -p 'test_*.py'

The full 10k+ root suite could not be executed locally because only selected GitHub files, not the full checkout, were present. Hosted Actions are the integration authority; no CI pass is asserted before checking it. No merge, tag, release, production change, or external publication was performed.

**CT-12 additional exact finite check:** selected q=16 signed forcing-charge L1 norms at N=128,256,512,1024 were 5.237738491538, 5.236532309880, 5.235843050900, 5.236241222887. The difference between N=256 and N=512 prefixes was 0.002282374602, strictly below the independently proved tail allowance 15·16/(32·256)=0.029296875. These are displays of exact rational finite vectors, not claims of asymptotic normalization. An eleventh exact local Cauchy test passed.
