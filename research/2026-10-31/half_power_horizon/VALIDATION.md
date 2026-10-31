# Finite validation and provenance — Operation HALF-POWER HORIZON

**Base:** PR #428 exact parent 91e06fd21b2e301d5d73df4415d6cf60ec9d79cd. Main XVII baseline e8598cfa5d32fd1de8e94a3e458a366a0850d59e. Draft, research only. No edit to old source/frozen/formal/workflow or main.

A standalone local Fraction-only prototype and 14 discoverable unittest obligations were executed using Python 3. The first 12-test attempt yielded one useful failure: at m=3 the root of the MOVING polynomial X²−(1−2^m) selected 1 mod4 reduces to 5 mod8, not 1 mod8 as originally hypothesized. Re-deriving (r−1)(r+1)=−2^m gives the corrected congruence 1+2^(m−1) mod2^m. The corrected test was retained and all 14 tests passed in the local standalone research prototype. This is a calibration/proof of the stated bounded test, not an independent mathematical referee or a new Lean certificate.

Exact finite control ranges:
- b=2,3,6,16,36 and m up to19: rational geometric identities and product formula; common 6-adic successor two local norm costs through m=21.
- Roots X²=1 enumerated exhaustively mod2^k for k=3..11 and compared with closed-form four-root set and lifting to k+1.
- Binomial (1/2 choose k)8^k term valuations checked for k=1..39, selected √(1+8t) residues across t=-5,-1,0,1,2,3,8 and up to22-bit precision, in particular √9=-3 in the 1 mod4 branch.
- Naive (1−2)^(-1/2) generalized binomial terms at k=2^j, j=1..13, found exact valuations 1−2^j (not tending to +∞): a decisive negative-convergence check.
- Original BBP r(n) equality with all four signed poles over n=-40..40, odd denominators, exact v₂ difference m across n=-8..26 and m=1..13. At p=3 verified every declared m>d source-pole bound for the same ranges; explicit d(1)=1 and d(2)=3.
- Gaussian integer 1+i squared equals 2i and X²−2X+2 meets 2-Eisenstein coefficient conditions.
- Finite successor roots of 1−2^m select nonlifting ghost residues for m=3..21; joint real/2/3 root tests m=3..16, and 3-adic Hensel root tests through 12 ternary digits.

Reproduction after repository checkout:
    python -m unittest discover -s tests -p 'test_half_power_horizon.py' -v
    python scripts/verify_provenance.py
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py
    python -m unittest discover -s tests -p 'test_*.py'

**Hosted CI:** exact-head Github Actions checked separately after branch push; do NOT label pass without checking. Full repository suite not executed locally because complete checkout was not present. No publication, PR merge, tag, or release authorized.

**Primary provenance:** Keith Conrad local-global product formula (https://kconrad.math.uconn.edu/blurbs/gradnumthy/localglobal.pdf); Conrad Hensel/p-adic roots (https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf). Earlier SUCC Operation SUMMATION SNAPSHOT ARROWS §3/5; DYADIC EXPOSURE §7; source DSI isometry; BDC half-density and Weil; draft PRs #427–428. This package does not reclassify their open global theorems. 