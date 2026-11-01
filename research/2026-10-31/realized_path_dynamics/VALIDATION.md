# Validation and reproducibility — realized history and source Hamiltonian

## Snapshot and provenance

- Baseline: SUCC Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`; stacked parent research PR #442 exact head `4f49abd7bf50ceebf5281a39a3f3d4dca8841450`.
- Original four signed BBP poles and literal `U_0=0` are **UNCHANGED**; only the additive research files and `tests/test_realized_path_dynamics.py` are new.
- Earlier project imports `operational_yoneda_descent`, `yoneda` are referenced, not reimplemented or modified. The stochastic model is DECLARED toy probability, not source-authentic physics.

## Executed exact arithmetic checks (not inferred from CI)

```sh
cd /mnt/data/succ_realized_path_round
python -m unittest discover -s tests -p 'test_*.py' -q
```

**83/83 new exact tests PASS** in Python 3.13.5. All core tests use standard-library `Fraction`, literal source pole formula, enumerated prior/path probabilities, rational matrix multiplication and finite combinatorial identities. No π digits, floating phase equality or external probability fitting were used.

A completely separate **local test aggregation** copied the unmodified locally available PR #438–#441 research snapshots, PR #442 Riemann-sphere snapshot, and the new research tree to `/mnt/data/succ_realized_path_combined` (NOT the full SUCC repo). Running the same root unittest discovery there produced **228/228 PASS** in one Python process. This is an integration proxy, not a full SUCC checkout or GitHub hosted CI certificate; source snapshot parent refs are recorded in their respective dossiers.

A separate symbolic SymPy cross-check (independent from the Fraction module) verified symbolically for arbitrary source parameters u,v:

- `G(u)^2=G(u)`;
- `G(u)G(v)=G(v)`;
- `(F(v)F(u))_12=16u+v`;
- `(F(v)F(u)-F(u)F(v))_12=15(u-v)`;
- `I+(a-1)G(u)=[[a,u(a-1)/15],[0,1]]` (generic canonical time fraction/exponential form).

### Exact calibrated receipts

- Five reference histories: A→T=3/8, A→X=1/8; B→T=1/8, B→X=1/8, B→Y=1/4.
- Target-constrained λ=1/2 desirability: `H0=13/32`, `H1(A)=3/4`, `H1(B)=1/16`; posterior `(A,B)=(12/13,1/13)`.
- Same observed x=1 but A future support `{T,X}` and B `{T,X,Y}`; no Markov quotient.
- First authentic original forcing `r(1)=47/15`; second `r(2)=106/819`; order commutator `12301/273`.
- Original canonical first accumulated action `47/240`; exact midpoint of first Hamiltonian unit step `(x,p)=(47/75,1/4)` from `(0,1)`, pairing `47/300`.
- Closed-form ordered right-zero band expansion checked for N≤34 against source recurrence and exact independent subset enumeration for N≤10.
- Authentic source r(j) is strictly bounded by 15/[64(j−1)^2] for j≥2; the rational finite action-defect prefixes remain strictly below the proved all-horizon bound 1/1024; positive rational action tilts are verified independently of phases.
- Unconditional future entropy can grow (`prior full-path 5/2 bits`, realized-A continuation `3 bits`), while realized event surprisal remains nonnegative.
- Positive prior/cost/entropy do not determine signed phases: two equal-weight characters `(1,1)` and `(1,-1)` yield amplitudes 1 vs 0.

## Probes that falsify oversells

1. Non-lumpable A/B endpoint observer must be rejected.
2. Equal-cost path tied geodesics must NOT become uniquely selected as λ→0.
3. Signed characters must not be inferred from positive transition probabilities.
4. Full exact four-pole zero-seeded BBP path must remain deterministic; any extra stochastic branch must be declared as an auxiliary observer/control model.
5. Naive product of time-marginal affine transfer operators fails for history-conditioned second-step probabilities; chronological order matters.
6. The original source's first two affine steps MUST fail to commute with exact `12301/273`, whereas every finite right-zero-band expansion must match the original true recurrence.

## Not run / not claimed

- NO full repository 10,000+ unittest suite on a full checkout; local proxy is not equivalent.
- NO complete repository provenance, observer-foundations or ordinal scripts on a full checkout.
- NO new Lean kernel declarations and NO external mathematical referee.
- NO π normality, RH, physical thermodynamic entropy-production or quantum-speedup result.
- Hosted exact-head GitHub CI is separate: status must be checked after push, not assumed passed.
