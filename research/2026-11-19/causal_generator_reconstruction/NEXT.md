# Next discriminator: an anchored signed residual with an actual estimate

The completed finite results are in README.md. This file specifies the next
research obligation; it is not counted as an accomplished cancellation theorem.

## Selected target and source

Retain the original BBP forcing, `U0=0`, the integer lift, and
`Y_n=U_n+T_n=16^n pi/16`. For a fixed nonzero integer `h`, define
`z_n=exp(2*pi*i*h*Y_n)` and
`W_B(h)=B^-1 sum_{B<=n<2B} z_n`.

Full normality needs `W_B(h)->0` for every nonzero integer `h` with the appropriate
all-shell/prefix passage. The repository's weaker R0 target only asks for an
eventual strictly positive real-part gap at `h=1`. Proving the full complex
limit is stronger than R0 and should not be presented as the only available
step. The unresolved arithmetic statement is exactly about the selected orbit.

## A candidate that can earn progress

Construct retained source features `q_n`, transport `A_n`, and covectors
`ell_n`, then use the **defined** residual and readout error

```
r_n = q_(n+1) - A_n q_n
e_n = z_n - (ell_n - ell_(n+1) A_n) q_n.
```

CS-03 is automatically an identity. Progress consists in independently bounding
its terms from the source, not checking that the identity holds.

| Budget | What would pay it | What would fail |
|---|---|---|
| `(abs(ell_B q_B)+abs(ell_2B q_2B))/B` | A source-derived sublinear endpoint estimate | `q_n` contains the unknown unbounded target partial sum and its endpoint estimate is simply assumed |
| `abs(sum ell_(n+1) r_n)/B` | A signed cancellation inequality retaining order, source, frequency and seed | A fit on a training shell, an ensemble average over seeds, or an unnamed uniform constant |
| `sum abs(e_n)/B` | An explicit target approximation bound valid on every required shell | Approximation only at fixed horizon with an unproved exchange of limits |
| Precision and chart transport | Exact arithmetic or rigorous intervals; every endpoint frame and compensator retained | Local locking erases the stationary source component |

For R0, the real part of the exact identity can be bounded directly. This may
need less than the three vanishing absolute budgets above; any proposed weaker
certificate must still imply a uniform real-part gap for the authentic source.

## Pass, fail and ambiguous outcomes declared before a new campaign

**Pass:** a proposed feature law is authenticated on its declared domain;
finite and infinite error estimates have explicit constants/quantifiers;
independent derivation or exact controls verify transport; the correct source
satisfies a genuinely new signed estimate; and the locked counterseed is
excluded by a budget that provably stays nonzero. A finite pass is reported
only as finite evidence unless accompanied by an all-horizon proof.

**Fail:** the same proof gives a vanishing target mean for the unchanged forcing
with seed `-pi/16`; that source has completed phase constantly one. Also fail
if changing a phase-preserving frame changes the claimed scalar response,
if a delayed out-of-family source is accepted as authenticated, or if a claimed
fixed stationary linear representation of the irrational phase contradicts
HBC-01's exact root obstruction.

**Ambiguous:** a useful finite fit exists but its global closure, conditioning,
source ancestry or signed estimate is unproved. Mark the missing item rather
than promote a finite rank or a small error on one shell into normality.

## Proposed model-class comparison

1. A fixed stationary linear dictionary is a useful control, but HBC-01 and
   CS-05 delimit its exact and asymptotic whole-phase scope.
2. A source-dependent nonstationary dictionary or a growing character family
   can evade that narrow obstruction. It must pay its own size, clock and
   conditioning costs; no conclusion follows merely from evading the theorem.
3. A finite nonlinear generator already exists (`z -> z^16`). Search for a
   target identity that uses its arithmetic source, rather than asking finite
   dimensionality alone to imply mixing.
4. A source-sensitive anchored Poisson certificate can target the mean without
   reconstructing each phase. The fixed point at zero rules out a universal
   source-blind exact coboundary for `exp(2*pi*i*h*t)`.

Use held-out later shells and source mutations for discrimination, with rigorous
transport errors. Already consumed BBP shells are training/history, not fresh
validation. The exact algebra in this dossier does not add a new numerical
pi-shell campaign or claim a new empirical normality result.

## Dominance boundary

The causal-generator frame explains why Fibonacci reconstruction succeeds,
why five source observations can identify the BBP family, why anchors matter
to Jacobians and moving frames, and why signed completion remains independent.
It improves the formulation without eliminating the remaining arithmetic
obligation. A successful next frame must preserve these paid results and
explain the residual failure without smuggling the desired limit into a new
name, source ensemble, or unbounded hidden state.
