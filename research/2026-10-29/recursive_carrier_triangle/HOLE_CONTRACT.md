# Recursive carrier / triangular path contract

**Starting commit:** `ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc` (Main XIV).
**Branch:** `research/recursive-carrier-triangle-2026-10-29`.
**Author proposal:** an actualized path updates its carrier; subpaths interact;
a triangular sheet constrains the relation between the full path and its
virtual microstates; a Gamma/Oily dual might weight the field differential.

## Faithful interpretation and success criterion

We interpret the proposal as a mathematical construction request, not an
assertion that human reasoning or gluons obey the equations below. We seek
an authenticated carrier with (i) lawful recursive updates, (ii) a dual
composition/interaction law, (iii) exact compatibility under subdivision,
and (iv) a probe distinguishing normalization interaction from order memory.
The selected BBP forcing and its zero seed remain exactly the original ones.

The source field is already known on main:

$$R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad a_n=8n-7,$$
$$\mu_a(dx)=e^{-ax}(4-2e^{-3x}-e^{-4x}-e^{-5x})dx/R(a).$$

Main already proves the normalized source update and a Gamma finite part;
these are inherited inputs, not discoveries of this round. Main also proves
that arbitrary feedback, positive overlap, and virtual averaging do not imply
selected signed cancellation. PR #359 at
`3a4f7e1307d2de26020a00438a42220a23683e65` was read as an unmerged sibling;
none of its code or assumptions is silently imported.

## Principal exact statement

For every a>0, construct a convolution semigroup `mu_(a,t)`, t>=0,
whose unit law is the authentic `mu_a`, and prove

$$\operatorname{Tilt}_s(\mu_{a,t})=\mu_{a+s,t},\qquad
\mu_{a,t}*\mu_{a,u}=\mu_{a,t+u}\quad(s,t,u\ge0).$$

Determine every finite mixed increment of `log R`, its sign, the exact
triangle compatibility law, and source-overlap estimates. Distinguish these
commuting normalized interactions from genuinely noncommuting path updates.

**Truth state at selection:** candidate identity found by algebra; full
proof, independent checks and hostile controls required before publication.
The package was written after exploratory algebra, so this document is not
a claim of blind preregistration of that algebra. The holdout grid below was
fixed before the final executable validation.

## Dependency cut and novelty tax

`original signed four poles -> positive source field -> atomic decomposition
-> all-order interactions and sharper overlap -> signed transport` is the
constructive chain. The last step still leaves a signed arithmetic estimate
unproved. The convolution parameter is not the BBP iteration index, and
independence of positive atoms is not independence of arithmetic phases.

The construction remains meaningful for source fields independent of pi
normality. It gives explicit convolution roots and bounds for every a>0,
not a hypothesis whose only support is that it would prove normality.
Academic novelty is unverified; classical ingredients are attributed.

Alternative candidates considered:

- normalized transfer kernels: useful common language, mostly inherited;
- Pólya/Beta interaction cocycle: exact auxiliary model, not the BBP source;
- noncommuting path signatures: genuine order memory, no automatic source map;
- original-BBP atomic/convolution field: selected principal construction;
- stronger Weyl cancellation from curvature alone: rejected by explicit
  nonlinear reinforced-path controls.

## Discriminating probes and outcomes fixed before final runs

1. Compare original signed poles, factorized rational R, atom Laplace product,
   and moment-to-cumulant reconstruction. Any mismatch fails source fidelity.
2. Verify finite-difference ratios at orders 1..6 on rational parameters
   `1/17, 23/11, 1001/7` and source clocks `8n-7` for heldout
   `n=37,61,97`. Positive steps include `1/13,7/5,8,19`.
3. Pair interaction >1 and cubic interaction <1 must hold for positive
   increments; zero increments must give exactly one. A pairwise-only
   approximation must fail the cubic control.
4. Compare Stokes area products with direct full-word probabilities under
   flat Pólya, harmonic feedback and exponential feedback. Require a nonflat
   countermodel with a positive-probability coherent infinite path.
5. Calibrate wrong pole coefficient, erased mass normalizer, reset-field
   composition, omitted third interaction, false flatness, and spurious
   affine phase interaction. False models must be rejected.
6. Check source-overlap bounds exactly after squaring; test heldout block
   horizons `343,1000,4096` and cube-boundary neighbors. Retain the coherent
   phase control, for which the actual normalized signed sum is one.

Pass establishes finite instrument agreement. Analytic all-parameter claims
require the written proofs; finite checks never perform their infinite lift.
The required source-specific signed estimate and pi normality remain OPEN.

## Next verdict-changing probe

Use the sharper cubic-window transport on the authentic zero-seeded
`e(h U_n)` for all fixed nonzero integer h. A useful next theorem must bound
the signed weighted sum itself, and explain why the unchanged-forcing
changed-seed control `V_n=-T_n` fails its hypotheses. A bound on positive
field geometry or subdivision alone cannot supply that explanation.
