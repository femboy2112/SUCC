# Explicit original-BBP 1→2 spatial Haar lift — and the real two-digit frontier

Research draft dated 2026-11-09. Exact parent #562; the original four BBP poles and literal U0=0 are frozen. π base-16 simple normality, two-digit Haar, and full normality remain OPEN.

## The precise result

Original SUCC #527 proved a source-indexed 2-adic isometry V with V(0)=0. New source-specific closed formulas:

- first spatial nibble: f(n)=(2(n mod2)−n) mod16, a permutation of 0..15;
- scale-step source slope s(a)=r'(a) mod16=11 for a mod4∈{0,1}, otherwise 3;
- spatial refinement for EVERY k≥1: V(a+16^k t)=V(a)+16^k t s(a) mod16^(k+1);
- **explicit one→two formula:** Lift₂(d,t)=(d, [b_(f(d))+s(f(d)) t] mod16), b=(0,14,15,2,0,6,14,5,5,11,1,4,14,12,8,15).

As (d,t) traverse the complete 256-point source-clock fiber, Lift₂ is bijective: exact 2-adic spatial Haar at depth two, and by induction at every further 16-adic precision depth. The additional t coordinate is necessary. This is NOT a source-selected real two-digit normality theorem.

## The obstruction

Consecutive *times* of the very same first 2-adic nibble form a deterministic 16-cycle: E1=0 but temporal pair E2=15. Thus even the authentic BBP carrier separates **spatial refinement** from **chronological pairing**.

Real π hexadecimal words instead are floor(256 frac(U_n+T_n)). SUCC #558/#562 supplies the full additive-CRT prime-residue and literal carry interface (including inherited primes); the future source tail T_n supplies the analytic boundary correction. The exact 16×16 chronological transition matrix has 225 mixed Fourier modes left after its row/column one-digit marginals. Proving them decaying from the *original zero-seed source* remains OPEN.

## Files

- [THEOREM_CHECKPOINT.md](THEOREM_CHECKPOINT.md): full definitions, quantified all-k 2-adic source proof, real all-prime interface, mixed 225-mode identity and adversarial controls
- [PREREGISTRATION.md](PREREGISTRATION.md): first committed before the new source holdout
- [reproduce.py](reproduce.py): builds 65,536 original π hex digits from a certified source-only integer interval (two guards) and the complete 16×16 exact two-digit table; checks #561 40,960 SHA and new 65,536 SHA. Run explicitly, not part of the root fast test suite
- [VALIDATION.md](VALIDATION.md): exact checks and separation of local versus hosted gates
- [NEXT.md](NEXT.md): one→two real digit signed carry-current gate, and subsequent all-depth recursion
- New canonical-source module observational_succ/bbp_spatial_haar_lift.py and root-discoverable tests/test_bbp_spatial_haar_lift.py.

Source integrity and mathematical priority: no frozen imports/Lean/workflows were edited and none of these results promotes the real π normality status. The all-k analytic proof explicitly imports the nontrivial V(0)=0 from #527; it is not inferred from finite tests.