# Arithmetic extension validation

Executed in `/media/leah/SPANKBANK/SUCCYBOI/SUCC-arithmetic-barrier`, branch
`research/bbp-arithmetic-barrier-2026-10-30`, based at exact parent
`1a1524de28b155139d8fe84ea90fc2f117fbb9f3`, Python 3.12.3.

- `python -m unittest discover -s research/2026-10-30/arithmetic_barrier/arithmetic -p 'test_*.py' -v`
  exited 0: **14 methods passed**, final raw output `focused_tests.log`,
  2.915 seconds. Tests cover the seven theorem/control families in the dossier;
  this count is test methods, not independent mathematical witnesses.
- `python research/2026-10-30/arithmetic_barrier/arithmetic/independent_oracle.py`
  exited 0: **275 exact shadow-and-first-lift cases** across five coefficient
  families, 55 authentic rows, **23 authentic conductor births**, **19 coherent
  null-source conductor births**, p19 packet timeline and p13/p47/p73 controls.
  Raw `independent_receipt.json` records interpreter, start time, parent SHA,
  command, measured duration (6.150233 seconds), source hashes, and exact
  residues. Its unrolled rational implementation imports no parent or new
  primary helper. This is implementation independence with a shared reasoner,
  not blind external peer review.
- `python -m compileall -q research/2026-10-30/arithmetic_barrier/arithmetic`
  exited 0. The receipt's three Python SHA-256 values were rechecked against
  the final scripts and matched.

`PREDECLARED.md` separates the initial hand/exploratory pass from fresh prime
holdouts and the later literature-driven controls. Assertions use exact
Fractions and modular arithmetic. The tests do not import π digits or numerical
normality assumptions. The null-integrand polynomial identity is checked at
more exact points than its degree; the universal theorem also has a written
algebraic/integral proof.

Finite negative results are preserved: naive lift differs by 65 modulo 169 at
p13,k1; p19 loses its primary conductor at n10..16; p73,k4 loses it at n274;
p11's reflected birth window has two steps but its base-16 order is five;
same-ratio and positive Gamma-matched mutants survive insufficient source
identification; all fixed-precision increasing-depth probes are blind to
p-integral rational seeds; the zero-seeded seven-pole null source has all odd
conductor depths while its signed phases tend to 1.

An exploratory SymPy Gosper call returned `None` for the rational null-source
summand weighted by 16^(-n). This software outcome is **not** the no-go proof;
the dossier gives the separate finite-pole-orbit proof excluding rational
telescopers. No general special-function impossibility is asserted.

Repository-wide gates, exact-head hosted CI, manifests for the whole campaign,
and draft PR delivery belong to the integrating root agent. They are not
claimed by this scoped receipt. No new Lean/kernel theorem, normality proof,
RH proof, mathematical priority claim, or final source-selected signed CRT
estimate is asserted here.
