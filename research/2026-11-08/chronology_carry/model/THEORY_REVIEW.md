# Independent carry-model front review of CCV1--7d

Review status: **PASS at the paper-proof level**, with the scope below.
This is an independent reasoning assignment in the same model family and
workspace, not external scholarly refereeing or Lean verification.

Reviewed theory document SHA256: `deab12908b98d19e8aed67cfc30027bb3e8b5884e9b2908ad4fbe2f6f43db9fc`.

* CCV1--2: P^k is the uniform-word projection; the finite geometric sum and
  telescoping give the stated potential and signed occupation contrast.
  The reference kernel is never substituted for the actual source law.
* CCV1-L/Q: appending uniform ordinary digits for k steps forgets even an
  initial literal16. Weighted carry propagation before reduction gives
  `pi(shift(v,c))=(16*pi(v)+c) mod16^k`, including c=16. Pullback intertwines
  the two reference operators exactly, and the source integer-lift residue
  equals pi(v). Odd h makes the q finite target values distinct, giving the
  stated4k-bit worst-case bound on that finite carrier. This is not a bit
  lower bound for a known singleton zero-source history with free replay.
* CCV3--4: independently expanded zero-padded window squares. The coefficient
  `(N+H-1)/(NH)` multiplies the bracket normalized by C_d=N^-1 sum. All
  positive and negative cross terms remain, so the asymptotic gate has the
  stated normalization. The zero predictor recovers the earlier VdC route.
* CCV5: the exact identity `c_n=a_n+16j_(n-1)-j_n` follows from Green tails.
  Under normality, j-events have density zero by fixed-epsilon upper bounds.
  The finite past word and future circle then have the product empirical
  law, giving uniform L2 risk for bounded tables. Restriction to disk radius2
  before the L1 infimum is legitimate. This concerns raw phase prediction,
  not folded error at growing lags.
* CCV6: checked the retained alternative residue-observer correction Xi
  against the actual archived SBA-1/2 spill proof. The feature-union count
  is at most k times spillcount, and literal16 implies a positive spill.
  The O(Gk/log A) correction is paid for that model under its stated growth
  condition. The different literal model in CCV1-L needs no such correction.
* CCV7a--c: checked the original fractional recurrence, weighted forcing bound
  `F_n/16^k < 1/[64(A-k)^2]`, and midpoint error. Keeping literal carries
  removes the old exceptional-word beta term completely. The lag difference
  has at most2k uncancelled unit terms on every truncated window. This gives
  exactly the padded norm coefficient `2k/H*(1+(H-1)/A)`. The delta contribution
  follows by the H-entry convolution bound, yielding the stated square-root
  factor. Combining the signed mean error with the Poisson endpoint gives
  4k/A when the reference mean is zero, as explicitly required there.
* CCV7d: k=ceil(log16 A) obeys1<=k<A and A<=16^k<16A for A>=2. When A>|h|,
  mu=0; substituting16^-k<=1/A gives exactly the displayed explicit
  O_h(log A/A) source-to-observer error. This is paid at every such epoch,
  while the retained signed mean is unbounded by that error alone.

The final comparison between W and Dpsi is an explicit asymptotic
equivalence. It pays representation errors, without reducing the remaining
original-zero cancellation claim merely by renaming it. Coherent and periodic
same-forcing seeds still survive every transport estimate and must be
excluded by the missing selected-source occupation theorem. In particular
for the coherent seed C_n=-1 and c_n=15, the compressed state is fixedq-1,
and Dpsi=e(-h/(2q)) when mu=0, of modulus1.

The source spill proof inspected was
`research/2026-10-26/SELECTED_BRANCH_ARITHMETIC.md`, including the four-pole
bound, gap argument and interval-packing count. This review does not claim
independent execution of every archived or theory test.
