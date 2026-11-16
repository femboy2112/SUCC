# The remaining arithmetic estimate

## Main target

For h=1 use the matched original-source response F_c(K) and its coherent
locked reference F_1(K). At a uniformly stable Gamma/triangular scale,
define D_B=E|F_c(K)-F_1(K)|^2.

The new detector identity proves

\[
\frac{BD_B}{2(1+\eta_*)}\le A_B
\le\frac{BD_B}{2(1-\eta_*)},
\qquad 0\le\eta_B\le\eta_*<1.
\]

Proving liminf BD_B>0 is therefore precisely the R0 source escape task
in detector coordinates. This is an equivalent reformulation, not a
weaker hidden lemma. A new approach must bound this signed residual
using something not already used to establish conditioning.

## Where additional structure must enter

The frame bound depends only on distinct forcing nodes and cannot select
the original seed. A new estimate must use the actual relation between
the phase vector e(hU_n), its literal carries and integer lift, and the
source coefficients. The full signed two-tap identity preserves that
relation; its generic frame inequality does not quantify it.

Useful potential directions, all OPEN:

1. Derive a signed lower bound for the reference cross term, retaining the
   actual carry tape and avoiding an assumed uniform phase distribution.
2. Improve the inherited whole-block coercivity loss from a constant per
   geometric block toward a positive fraction of its length. State the
   additional arithmetic input and the restricted-exponent cost explicitly.
3. Find a smaller statistic of the source-manifold phase vectors which has
   a stable inverse below the full-vector cubic spread. PC-05 does not rule
   out a special nonlinear estimator; a real advantage must account for
   what that estimator already knows about the source.
4. Derive an efficient aggregate response algorithm without calculating
   every contributing original phase first. This is a computational
   question; efficiency alone would not prove the signed estimate.

## Probability targets to keep separate

| Probability | What makes it large | What it certifies |
|---|---|---|
| Random frame succeeds | Independent recorded taps and a proved source spacing bound | A stable inverse for the declared measurement law |
| Phase detector produces a hit | Single-trial rate and fresh trial count | Existence of an observed event in that protocol |
| Model wins a calibrated test | Rival-specific likelihood differences and controlled selection | Discrimination inside the specified source class |

None is defined as the probability that a fixed deterministic theorem
becomes true. A Bayesian confidence interpretation would additionally
require a declared prior and adequate rival class.

## Guards

- Gamma--Poisson taps are an externally chosen instrument law.
- Keep both complex quadratures and the randomization labels.
- Full-vector frame conditioning does not imply small original mean.
- Frequency center and frequency spread have different effects.
- Finite numerical spectra are diagnostics; rational budgets and written
  proofs justify uniform statements.
- The genuine GB-12 amplification corollary has an unextracted onset
  and a growing dose. It does not pay uniform-density R0.
- Root baseline and focused test scopes remain separate.

The next verdict-changing result is a new source-selected signed estimate,
or a counterexample to a precisely proposed estimate. More agreement with
the already proved universal detector-energy law is not that result.
