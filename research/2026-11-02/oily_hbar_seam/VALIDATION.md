# Validation, arithmetic calibration, receipts and authority limits

**2026-11-02 — research-only, not a normality proof.** Exact incoming parent #469 ef6f8894741cac8d952e9fd12d49e4aa7d13fa25, stacked on #467/#466/#464/#463/#462/#460/#459 and merged Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Gamma-seam #468 is an independent sibling, NOT silently added to the branch. All additions live in the new research/2026-11-02/oily_hbar_seam directory plus additive tests/test_oily_hbar_seam.py. Original signed four BBP source poles, literal zero seed, historical contracts, formal/Lean, production, CI/workflows and main unchanged.

## Predeclared exact finite real conditional cofiber tests

**Before computing any of the new selected amplitudes**, the FIRST additive file on this research branch froze:
- N∈{768,1536,3072}, fixed harmonics h∈{9,11,17}, source carrier Q∈{16,256}, a total of **18** cells.
- Actual original four-pole rational U0=0 recurrence, no decimal digits of π or synthetic source.
- Explicit strict target \(G_{N,Q}(h)<2Q/N\) for ALL 18 (finite hypothesis, NOT asserted for all N).
- Same model session conducted preregistration and proof experiment; **NOT** independently blinded.

**Actual exact mathematical certificate replay:** a locally recreated implementation of the committed conditional_interval.py was executed against all 18 combinations. It uses Fraction for original source rational states and exact reduced source characters, a *rational* Machin bracket for π, dyadic phase grid \(2^{19}\), degree-18 *rational* Taylor polynomials of cos/sin, the rigorous absolute component remainder \((22/7)^{19}/19!\), explicit angle error \((44/7)2^{-19}+(\pi_{\rm upper}-\pi_{\rm lower})\), and integer rounding/error expansion. The computed rigorous upper ratios agreed EXACTLY (after upward integer 10^-9 rounding) with all 18 independently retained committed CONDITIONAL_HOLDOUTS.json values.

**18/18 strictly PASS** at the predeclared threshold, 0 failures. Largest certified \(G/(Q/N)\) upper = **1.258542912** (N3072,h9,Q16) versus threshold 2. Floating arithmetic was used only for elapsed times and output displays, NEVER pass/fail. One complete exact local replay took ~9.3 seconds; it is still a **finite** certificate, not a proof of a limit.

The uploaded exact oracle Git blob was re-fetched:
- conditional_interval.py SHA **676391bc73893104ec278031dec1fa1e837adf80**. 
- CONDITIONAL_HOLDOUTS.json gives the 18 rational outward upper bounds. An externally usable independent replay is obtained by running the source module in a full checkout and comparing its freshly written receipt values to the preserved entries (allow metadata/output field differences; the actual upper fractions must agree).

## Independently implemented numerical source replay

A separate local implementation builds each rational original U_n using the **combined** authentic numerator/denominator
\[
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}
\]
rather than the main oracle's four signed terms, then computes ordinary double-precision complex cos/sin for the same h,N,Q. **18/18 numerical G values are STRICTLY BELOW their independent exact-rational certified bounds**, with no mismatches. This second method confirms the absence of obvious transcription/index/source bugs, but floating trig is NOT an interval certificate, blind reviewer, or independent mathematical proof.

## Exact source finite/adversarial tests

The self-contained oily_hbar_probe.py covers:
- literal original four signed rational poles versus combined polynomial and exact U0=0;
- height-only local residue adversaries x=1 versus y=(Q+1)/(2Q+1), with exact lcm(1..8n) bounds for n=1..34;
- original time/Q carrier source isometry, finite selected real alias witnesses for fresh Q and h;
- exact base16 Thue–Morse digit recursion (the irrationality exponent 2 is imported from Bugeaud, NOT proved by finite test);
- same-source nonnormal period-three seed / residue and phase differences;
- exact Gaussian-rational conditional G pair Gram identity and **new exact refinement monotonicity** for Q=1,2,4,8,16,32,64;
- Gamma source pole-weight cancellation and Gaussian-rational global phase rotation preserving energy.

A locally reconstructed equivalent implementation passed **11/11 stdlib unit methods, 0 skips** (~0.024 seconds), and the staged correct root-layout adapter passed **11/11 methods** (~0.036 seconds). GitHub re-fetch confirms the latest exact module Git blob SHA **a2f62e0e58aa303b93f4950e86084c2e6e0dee18** and the staged root adapter's Git blob SHA **59f4fd2641bbfc374dd4d89714cdafce31bc9979** matches the actually executed wrapper bytes. The local research-script copy was recreated rather than byte-for-byte mounted from GitHub, so this is a **semantically matching local test**, not a falsely claimed exact blob test. The earlier original committed 10-method version was run during initial proof development; the new 11th method independently checks the universal refinement inequality.

## Mathematical proof / external input separation

- **OMH-01:** uniform height-only obstruction is cross-product congruence and classical Chan–Norrish lcm bound; asymptotic refinement additionally uses PNT. These are paper derivations, not from finite loops.
- **OMH-02/03:** original selected real moving-Q anti-alias and multicarrier Ω(log²N) energy depend on the PUBLISHED irrationality exponent μ(π)<15/2 and the authentic Green-tail bound; the detailed all-r uniform quantifiers are proved in PROOFS.md. The existence of a C>0 is imported; onset M0(h) is NOT effective here.
- **OMH-04:** Bugeaud's published Thue–Morse irrationality exponent 2 is external theorem; the nonnormality follows because its base16 digits are only 0/1. Changed REAL seed deliberately differs from authentic rational U0=0, though exact original forcing is retained.
- **OMH-05/05B:** conditional energy Parseval, variance and monotonicity are exact for ANY unit-modulus phase sequence. The connection to source carrier is the original DSI isometry; no statistical independence is assumed.
- **OMH-06:** 18 source-specific real finite interval certificates are exact finite OBSERVATIONS, not a theorem for all N or all h.
- **OMH-07:** scalar Oily/Gamma reference shifts do not supply temporal interference; the earlier original Oily signed logarithmic deficit is **not improved in asymptotic order** by this multicarrier energy.

**Unperformed / not claimed:** an authentic full SUCC native >11k regression run, all required root AGENTS.md provenance, ordinal/foundations probes, exact latest-head hosted GitHub CI green, a new Lean kernel theorem, independent externally blinded mathematical review, any original-source all-N signed conditional G bound, π base16 normality or RH. Tool/network limitations prevented native full GitHub clone; hosted CI is checked separately by exact commit if available.

## Reproduce from a real complete SUCC checkout

~~~sh
python research/2026-11-02/oily_hbar_seam/oily_hbar_probe.py
python -m unittest discover -s tests -p 'test_oily_hbar_seam.py'
python research/2026-11-02/oily_hbar_seam/conditional_interval.py
python research/2026-11-02/oily_hbar_seam/independent_float_oracle.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

Before full-suite status promotion, preserve any real failures, reconcile exact-head hosted runs and check full original source/seed provenance. Keep this research DRAFT and unmerged pending explicit maintainer review.
