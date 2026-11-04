# Hannibal source collision partial results

**Pi normality remains open.** This additive child of draft PR #476 contains
two proved partial near-pair inequalities, executed source probes, and hostile
controls. It does not supply the all-epoch logarithmic-mesh energy bound.

- **Actual zero seed:** for each fixed h!=0, all sufficiently large A and
  64<=m<=A, the window [A,32A) has at least
  `2A(1+floor(log_16(m/64)))` ordered pairs outside radius 1/m, distributed
  across every lag 1<=d<=A. This uses the original BBP completion and the
  published pi irrationality measure; its onset is not numerically certified.
- **Exact forcing:** on [A,2A), the closed annulus
  `1/(8m)<=||U_n-U_t||<=1/m` has at most
  `2 sum_(L=1)^(A-1) ceil(L/(1+floor(log_16(m/4))))` ordered pairs.
  The smaller core is entirely unpaid. This result also holds for changed seeds.
- **Decisive original-source falsifier:** at A=256,m=8, the deterministic
  iid-mean ceiling fails: `E=4209/4096 > 1+7/256=4208/4096`.

These bounds are much too weak to conclude normality. The paper proves their
quantifiers and coverage; finite data do not prove them. No external novelty,
Lean kernel certificate, external referee, or hosted CI success is implied.

Read [PROOFS.md](PROOFS.md), [PREREGISTRATION.md](PREREGISTRATION.md),
[VALIDATION.md](VALIDATION.md), and [NEXT_HANDOFF.md](NEXT_HANDOFF.md).
Receipts preserve full-source histograms, literal carry digests, exact mirror
and feasible antiphase costs, all-lag annulus counts, and witness packets.

Reproduce from the repository root:

```sh
python -m unittest discover -s tests -p 'test_hannibal_source.py' -v
python research/2026-11-02/hannibal_source/probe.py --verify
python research/2026-11-02/hannibal_source/probe.py --large --verify
python research/2026-11-02/hannibal_source/odd_replay.py --verify
```

The large replay streams the original full modulus through time 131071;
it takes substantial CPU time and does not retain all large states in RAM.
Do not reinterpret a verified finite receipt as an asymptotic premise.
