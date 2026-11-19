# Next decisive offensive: a source-derived signed Gaussian witness

## Frozen source and target

Keep the **literal** four BBP poles `(7,4,3,2)`, coefficients
`(4,-2,-1,-1)`, U0=0, chronological order, unwrapped integer carries,
`T_n` and `Y_n=U_n+T_n`. Do not replace with a seed ensemble or smooth
an actual delta before applying the actual dynamics.

Pick and preregister a fixed lambda>0 (initial calibration lambda=1),
a finite Gaussian Fourier cutoff with an explicit exponential tail,
and a lawful clock-forward source-derived witness `q_n` in L2(T).
The target is

```
C_B = (1/B) sum_(n=B)^(2B-1) <K_(theta_n)-K_0, q_n>.
```

**Needed theorem:** prove constants `c>0, M<infinity, B0` such that for
**every** B>=B0, `|C_B|>=c` and
`(1/B)sum ||q_n||^2<=M^2`.
GYC-11 then proves `R0` without a further dynamical assumption.
If a real-part one-sided estimate is more natural, declare the orientation
and comparison frame and use `Re C_B` with the same Cauchy bound.

## Design restrictions (prevent tautologies)

1. Construct `q_n` from the authenticated signed rational forcing,
   cofactor/carry journal, or independently proved source statistics.
   It must NOT be `v_n=K_(theta_n)-K_0`, a noncausal target partial sum,
   or a posthoc fit to the already-observed Weyl shell.
2. Preserve complex phase, clockwise orientation, all integer carries,
   terminal tail and moving reference. No undemodulated co-moving gauge
   allowed to manufacture cancellation (#670's false Weyl control).
3. Prove genuine signed shell correlation **without** taking its modulus
   termwise. A positive source moment or `sum ||q_n||^2` is not enough.
4. The source-specific inequality must explicitly fail on the unchanged
   forcing with seed `s=-pi/16`. It must also distinguish the `1/16` late
   phase alias using the unwrapped seed journal or say why it cannot.
5. Cross-reference #668/#670 five-channel source/seed Jacobians and #671
   minimal realization, but do not import unmerged branch claims as main.

## Source-informed candidates to kill or retain

- **Cofactor/carry phase witness:** retain prime-factor labels and oriented
  integer winding; test whether selected signed cofactor residues correlate
  with the first Gaussian harmonic, not merely its norm.
- **Two-resolution witness:** use the exact `T_16* K_lambda = K_(256lambda) T_16*`
  square; subtract only after compensating both scale and frame. If it
  gives the same nonzero bound for seed -x, kill it.
- **Forward terminal witness:** substitute exact rational U_n for Y_n
  using GYC-06 and keep the explicit O(B^-2) error. Test whether the first
  nonvanishing signed term is genuinely arithmetic rather than the target
  Weyl sum in disguise.
- **One-sided polarity repair:** GYC-10 excludes long near-zero sequences
  on one observable orientation, but not `theta_n<T_n` or the near-one
  side. Use authenticated carry/cofactor constraints to investigate that
  excluded orientation. Do not infer a positive shell density from an
  O(log N) finite-run lemma alone.

## Falsification matrix, set before further experiments

| Model | Required behavior | False-positive mechanism |
|---|---|---|
| original zero seed | signed witness could stay uniformly nonzero (UNVERIFIED) | finite training shell only |
| same forcing, s=-x | no positive asymptotic witness | raw r(n) innovation energy persists despite locked phase |
| seed s=1/16 | late circle outputs alias original; source seed journal must differ | phase-only false authentication |
| fixed Gaussian seed noise | observed phase mean attenuates superexponentially | ensemble-mixing masquerades as orbit-mixing |
| unrelated positive forcing, zero phase completion | witnesses relying only on positivity must fail | Gamma/heat counterfeit |
| moving gauge with uncompensated reference | reject | artificial cancellation from frame rotation |
| original signed source with mutated matching low-order jets | require discrimination outside fitted jets | Jacobian or asymptotic coefficient looks identical |
| held-out later shells | finite check only, no universal inference | training/horizon leakage |

## Acceptance criteria and claim boundaries

**Pass as theorem:** mathematically source-derived q_n, exact transport,
independent uniform lower bound in *all* large B, all counterseed controls
excluded, complete error budget. That establishes R0 only; full normality
still needs V_B->0 or all Weyl modes.

**Pass as finite experiment:** preregister clocks, frequencies, widths,
precision, negative and mutation controls and actually certify intervals;
record exact shell/horizon and raw receipts. No infinity claim.

**Fail:** any positive witness theorem whose argument also proves escape
for seed -x, or whose source labeling disappears after dropping one of
phase/carry/unwrapped seed/transport. **Ambiguous:** a strong finite pattern
or model-based correlation without an independent all-shell estimate.

Potentially decisive comparison: prove a *nontrivial source-cofactor bound*
separating signed `C_B` from zero for all B, while controlling M uniformly.
The current dossier does not accomplish this step.
