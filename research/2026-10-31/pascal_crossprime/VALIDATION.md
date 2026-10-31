# Validation / scope receipt — Pascal 2↔3, 2026-10-31

**Branch:** research/pascal-2-3-conjugacy-pisot-probe-2026-10-31. **Exact parent:** draft PR #427 at 8558a95b2a28a20c63e5df7f2995755e84c4e642. This branch changes no original source, selected BBP recurrence, production, formal, CI, historical proofs or main.

**Executed local independent mathematical prototypes:** A concrete reversible 2→3 prefix code was checked over all 10,000 nonnegative source integers in both directions (and 10,000 inverse target integers); every affine conjugacy H(2x+1)=3H(x) passed. Another 30,000 randomized exact integer pairs satisfied the forward/inverse valuation congruence certificates. Full ternary prefix distributions for m=1,..,6 matched q=(1/4,1/4,1/2) exactly, enumerating 2^(2m−1) fair binary tails. Exact Pascal codeword occupancy equality / conditional likelihood ratios passed for all 3^m ternary words through m=7. The analytical KL constant is log3−3/2log2≈0.05889151782819191 nats per ternary tail digit; no floating comparison enters proof.

**Original four-pole source tests (separate exact modular prototype):** For b=1,..,6, zero-seeded original rational BBP U_n mod2^(2b) traversed all 2^(2b) residues, and H(U_n) mod3^b matched the exact transported integer-grid histogram; b=1 law is {0:2,1:1,2:1} over 4 times. For b=1,..,4, full joint source/3-clock histograms factored exactly over periods 4,48,576,6912 respectively. For conditional 2-adic unit shells m=1,..,6, first m output ternary digits matched the declared biased law across 2^(2m−1) authentic source times. This is finite corroboration of source theorem CP-10, whose all-horizon proof imports existing SUCC DSI-4.

**Additional exact finite controls:** Pascal forward/inverse on 2^n and 3^n, signed generalized binomial coefficients, p-adic valuations v₂(3^(2^k)−1)=k+2 for k≥1 and v₃(16^(3^k)−1)=k+1, the 3-adic non-continuity control for 2^n, and quadratic Pisot plus-one failure checked using exact Q(√2) integer pairs.

**Added regression:** tests/test_pascal_crossprime_conjugacy.py has 21 discoverable unittest methods. The independently run local probes share the described mathematical algorithms; the entire committed regression + 10k+ repository suite has NOT been executed locally in a full checkout. GitHub hosted exact-head CI is to be checked separately. No false claim of external mathematical refereeing or Lean kernel certification.

**Reproduce on the research branch:**
- python -m unittest discover -s tests -p 'test_pascal_crossprime_conjugacy.py' -v
- python scripts/verify_provenance.py
- python scripts/observer_foundations_probe.py
- python scripts/ordinal_succ_report_probe.py
- python -m unittest discover -s tests -p 'test_*.py'

**Primary citations:** Klaus Schmidt (1980), https://doi.org/10.1112/blms/12.4.269 ; Vávra–Veneziano (2018), https://doi.org/10.1016/j.jsc.2017.11.005 ; Rudolph (1990), https://doi.org/10.1017/S0143385700005629 ; SUCC Main XVII PIS-01..14, PI_DYADIC_SOURCE_ISOMETRY.md, PR #427.
