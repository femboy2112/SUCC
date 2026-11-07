# Preregistered large original-source golden-aperture holdouts

2026-11-07. This file is committed BEFORE measuring golden E_a for A=1024,2048,4096. Previous A=79,157,281,389 were preregistered in PREREGISTRATION.md and already executed. A=512 was used as a speed CALIBRATION and MUST NOT count as blind holdout.

## Frozen computation
- Authentic combined/four-pole r(n), literal U0=0, x_n=U_n mod1.
- Fixed golden b=(3-sqrt5)/2, a=sqrt(b)=phi^-1 (never tune).
- A=1024,2048,4096, I_A=[A,2A). Use exact Fraction states, rational-versus-quadratic b comparisons and O(A log A) cyclic sweep, with an exact quadratic oracle on small inputs only.
- Evaluate E_a=(1/(b A²)) sum_(n,m in I_A)(b-circle_dist(x_n,x_m))_+-b. Return two outward 14-decimal rational bounds and exact count of ordered pairs d<b; analytic BBP-to-π energy transfer <=1/(15b A²).
- Compare with constant-phase E=a, uniform-grid check; no extrapolation or parameter fitting, and do NOT assert decay or a rate from three finite epochs.
- If runtime/memory prevents A4096, preserve failures, report missing sample and finish A1024/2048. Avoid spurious success labels.
- The earlier A=512 speed calibration and its E≈0.001119 may be used for runtime estimation but NOT for theorem fitting or blind validation.
