# Boundary filters: what closes, what grows, and what the arithmetic costs

**Research round, 2026-11-12. Parent Main XXV
`db9fb4b84672050efa79b13377f1e73364598a14`.**
The original four-pole forcing and literal zero seed are unchanged.
**R0, R1, pi base-16 normality, Goldbach and RH remain OPEN.**

The user's boundary-first proposal is taken literally as a research method:
start with accessible, source-calibrated observations; ask which internal
properties they determine; then price the order, phase, resolution and error
of the filters. The October inverse-boundary and November driven-pinbed
archive already provide substantial reconstruction theorems. This round
asks which of those instruments can actually close on the arithmetic target.

## Active-intervention continuation

The user's further proposal changes the observation problem: a suitably
coupled transducer can reveal a distinction that every passive boundary
filter misses. The relevant equivalence must therefore include the allowed
interventions, their order, resource budget and effect on the source.

[Carrier access and transduction](CARRIER_ACCESS_AND_TRANSDUCTION.md) recovers
two exact archive examples: identical all-depth digit geometry with different
ring arithmetic, separated by marked addition; and identical passive network
boundaries separated by the same new conductance. It also gives the finite
quantum target-span criterion and an explicit indistinguishable counterpair
when the target lies outside the accessible effect span.

The current formal `IdealHardField` definition remains existence with a
proved lack of a computable selector. Coupling-limited access is an additional
instrument property, not a silent redefinition or a classification of pi/RH.
Physical information disturbance, energy change, and mathematical proof
access require different hypotheses. The Higgs analogy is useful for
calibrated interaction and response; see [primary sources](LITERATURE.md).

[Indirect observation and matched cancellation](INTERVENTION_TRANSDUCERS.md)
constructs an exact active meter, proves which targets it reveals, and pays
the error amplification of weak coupling. A controlled readout preserves the
declared source energy while reducing coherence. Noncommuting background
cancellation produces an ordered spectral filter with genuine first-order
blind frequencies. Finally, derivative bounds connect an indirect sensor's
interaction duration, parameter variation and coefficient mass to the
arithmetic certificate's resolution requirement. The source realization of
such a sensor, and the needed uniform BBP estimate, remain open.

## Earned results

1. **The completed pi phase cannot close in a finite stationary linear model.**
   For `a_n=e(h b^n x)`, `h!=0`, finite Hankel rank is equivalent to rationality
   of x. The proof is elementary polynomial root counting. Every irrational
   source has full column rank in an explicit `b^d`-row, `d+1`-column section;
   no uniform conditioning follows. The same obstruction holds for every
   fixed nonconstant trigonometric-polynomial readout. This is a restriction
   on a realization class, not an asymptotic normality advance. The nonlinear
   state equation `a_(n+1)=a_n^16` remains one-dimensional.
   [Proofs and sparse irrational countercontrol](HANKEL_THEOREMS.md).

2. **Actual chronological readings can be calibrated without a fictitious
   exponential error bill.** A separate exact BBP state and tail enclosure at
   each time prices a Fourier packet by its coefficient/frequency budget.
   Repeatedly propagating one approximate corrected state has a different,
   exponentially amplifying error. The operator conjugacy also shows that
   averaging over the 16 inverse branches is not access to the selected past.
   [Transport, regularity hypotheses and Gram bridge](FILTER_TRANSPORT.md).

3. **Arithmetic denominator information has an explicit resolution cost.**
   A broad but genuine forward-closed BBP carrier grid uses
   `q_n=lcm_(j<=n) denominator(r(j))`, with each forcing reduced. For a local escape certificate
   `g_n >= c_n+V_(n+1) o F_n-V_n-epsilon_n` proved on that grid, let
   `O_A=osc V_A+osc V_(2A)` and
   `K_A=max_(A<=n<=2A) Lip(V_n)`. Its certified shell lower bound obeys

   ```math
   \frac{L_{A,2A}}{A}\le\frac{O_A}{A}+\frac{2\pi+17K_A}{2q_A}.
   ```

   Thus small endpoint oscillation and coarse smooth filters cannot turn
   denominator compatibility into a persistent escape certificate. A proof
   in this class must pay the resolution cost or use a stronger authenticated
   source domain. This does not rule out such a stronger domain. A C²
   refinement also gives the corresponding quadratic curvature cost at
   scale `q_A^2`.
   [Proof, sharp calibrations and domain firewall](DUAL_CERTIFICATE_BARRIER.md).

4. **Finite rank is now a verifiable source experiment.** The additive
   [certificate module](../../../observational_succ/boundary_filter_complexity.py)
   encloses the Gram of consecutive completed BBP phase readings using exact
   rational source intervals, independent Machin angle bounds, Taylor
   remainders, and a rational Gershgorin bound. It returns INCONCLUSIVE when
   that sufficient bound fails. A positive margin delta proves, for every
   complex coefficient vector c on the declared finite window,
   `mean |sum_j c_j a_(n+j)|^2 >= delta sum_j |c_j|^2`.
   It excludes a finite recurrence fit with smaller residual; it does not
   prove an all-shell gap. [Receipts and replay](VALIDATION.md).

## The next mathematical cut

For some fixed number m>=2 of consecutive phase readings, independently
derive a positive uniform lower bound on the original-zero shell Gram:

```math
\lambda_{\min}(G_A)\ge\gamma>0\qquad(A\ge A_0).
```

The paid finite inequality

```math
|W_A(1)|\le\sqrt{1-\frac{m-1}{m}\lambda_{\min}(G_A)}
             +\frac{m-1}{A}
```

would then give R1, hence R0. There is also a more direct implication:
the coefficient vector `(-1,1,0,...)/sqrt(2)` has Gram energy
`1-Re W_A(15)`, so a full Gram gap implies the existing digit-change
rung (CH). This is a **conditional reduction**, not a new
source estimate. Full rank alone is already guaranteed by irrationality at
an explicit horizon; the unproved quantitative margin is the entire new
arithmetic obligation. The full gap is stronger than the single-direction
(CH) target; for m=2 it is exactly `1-|W_A(15)|`. It is not claimed to be an
easier route below R0. A future proof must identify a source property that supplies the gap
and survives the coherent seed and sparse irrational controls.

Even uniform positive Gram conditioning at every finite depth is weaker
than normality: the invariant law `c delta_0+(1-c) Haar`, `0<c<1`, has
Gram `(1-c)I+c11*` and nonzero first Fourier coefficient c. Do not upgrade
the next cut to a full normality theorem.

## Reading and provenance

- [Archive map and inspected donor heads](ARCHIVE_MAP.md).
- [Claim ledger and hole contract](CLAIM_LEDGER.md).
- [Verification, actual runs and limits](VALIDATION.md).
- [Independent numerical oracle](oracle.py); numerical results are not
  the rational certificate authority.

This additive branch does not merge the active donor branches. In particular
PR605 and PR606 use the same dossier path for different material; this round
uses its own directory and preserves both donors. The newly derived
elementary results are reviewed within one model family, not independently
refereed or Lean-certified. No academic-priority claim is made.
