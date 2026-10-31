# Validation and provenance — TWTH 2026-10-31

**Baseline:** main e8598cfa5d32fd1de8e94a3e458a366a0850d59e (Main XVII). The draft PR #426 is related read-only context, not the parent of this branch. The original BBP source and all formal/production/workflow/historical contracts are unchanged.

**Local execution:** A standalone exact Fraction prototype of the research module was run in the execution container. 15 focused tests passed in ~0.095 seconds, including the heldout sparse digit counterexample. The connector-uploaded branch code and discoverable regression have the same algorithms and test obligations; hosted exact-head GitHub CI is the integration gate and must not be called successful until checked.

Reproduction after branch checkout:

    python -m unittest discover -s tests -p 'test_two_three_joint_carrier.py' -v
    python scripts/verify_provenance.py
    python scripts/observer_foundations_probe.py
    python scripts/ordinal_succ_report_probe.py
    python -m unittest discover -s tests -p 'test_*.py'

**Exact original-source finite controls:**
- Every four signed pole r(n) equals the rational combined odd-denominator polynomial for n≤69; exact Fraction U_n mod2^a equals the modular recurrence for a=4,8,10 on n≤60.
- Finite source isometry checked for all 2,080 pairs of times 0≤s<t≤64; all matched exact v₂(t−s).
- LTE v₃(16^t−1)=1+v₃(t) checked for 1≤t<128; all local 3-adic unit subgroups at b=1,...,6 are enumerated exactly.
- Joint CRT permutations checked on periods M=16,48,144,768 and shifted windows starting at 17, with no repeated or omitted pair.
- Full product Fourier character phase histograms exactly balanced on finite full periods, including nontrivial r,s.
- Full tripling carry 0≤c≤2 tested on signed rational points, denominators 5/17/31/127 and grids q=16/48/256; exact 3-fold hat refinement tested.
- Original zero-seeded π real tripling digits certified by rational BBP Green-tail brackets, matching hexadecimal '243f6a8885a308d313' at the first 17 places and additional q=256 oracle rows; no input π digits are used by the actual source algorithm.
- Source-to-completion tripling transport checked for (N,q)=(16,16),(64,16),(128,16),(20,256); 3-adic original source poles at n=1,2,7 checked; false circle-dual claim refuted at levels 2,3,6,48.
- Positive continuous-factor controls: periodic rational ×16-orbit periods 2 and 3. Negative control: period-5 rational orbit has no continuous factor from the 2×3 odometer. Fixed rational x=1/5 shows ×16-invariance does NOT entail ×3 invariance; δ0 shows joint invariance does NOT entail Haar.
- Sparse base16 α=Σ16^(−2^j) has at most logarithmically many nonzero digits in each initial segment; its irrationality and nonnormality are paper facts, and Vinogradov's prime-multiple theorem is a CLASSICAL import, not a result of these finite tests.

**Selected finite tripling example:** at q=16, the rational zero-seed orbit has Δ_3 L1 about 0.553814 at N=64 and 0.264514 at N=128. The measured source-to-truncated-completion differences were about 0.025139 and 0.012554, respectively, with analytical certified upper bounds about 0.032113 and 0.016176. The universal all-horizon bounds are 0.0625 and 0.03125. All finite observations; no asymptotic inference.

**Mathematical proof authority:** paper arguments are in PROOF.md, relying on inherited DSI-1..4, elementary CRT/LTE/circle positive expansivity, and clearly cited classical duality and Rudolph–Johnson theorems. No new Lean declarations or external referee report. No claim that all repo tests have run locally; hosted CI must be inspected separately. No publication, tag, release or main merge authorized.

**Independent forward/backward calibration:** The original forward zero-seeded recurrence and the independently evaluated 2-adic backward Green series F₂(t) agree exactly modulo 2^a for a=4,8,12,16 and all t=0,...,100, including F₂(0)≡0. This comparison uses different chronological source representations and a bounded number ceil(a/4) of reversed-source terms. A 16th focused exact test passed locally. It calibrates the inherited all-horizon source theorem; it is not a second independent proof of π normality.
