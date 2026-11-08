# Mixed-quadratic expansion protocol

Registered before evaluating the mixed quadratic menu in this round.
Starting research pin: `525d7c87dd1016aeeea4ac9cd1366cbb935a0441`.

- Reuse the authenticated, previously measured source receipt at
  `../../complement_budget/results/source_1103.json`: p=4409,m=551,q=2,
  h=1 and h=3. These are development data, NOT fresh holdouts.
- Evaluate every `(a,b)` in F_p² for the atom `e((a*x²+b*x)/p)`.
  Remove only `(0,-h)` as a free resonant atom. Constant phase factors
  are absorbed in arbitrary complex coefficients.
- Use exact signed-int64 matrix contractions after outward quantization at
  2^26, with explicit no-overflow assertions and a proved common L1 radius.
  The root of unity table comes from the inherited rational Taylor enclosure.
- Compute exact Euclidean maxima on the linear row, and conservative L1
  maxima over ALL nonlinear rows. The latter is enough to certify a bound
  on the full dictionary; do not label it a sharp modulus maximum.
- Apply CB1/CB2 unchanged, including free resonance. If the full mixed menu's
  certified M<=1, the previous cost floor survives this larger menu. If M>1,
  report the weaker computed floor. No threshold is changed after viewing data.
- Separate paper identities from numerical evidence. Calibrate on small odd
  prime fields using direct rational phase sums and Python integer arithmetic;
  prove exact phase-blind fourth moments by collision enumeration.
- Required hostile controls: coherent inverse phase; arbitrary phase rotations
  with equal moduli; p=2 degeneracy; source versus mathematical model distinction.
- This is a finite model-class test. No all-epoch bound or normality conclusion.
