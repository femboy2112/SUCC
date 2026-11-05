# Hostile review of front A/H

Reviewed `front_ah/PROOFS.md` AH-01/02 after deriving CFG-1/2 separately.
This is cross-review by a second agent of the **same model family**, sharing
source provenance. It is not external independence or formal authority.

**Verdict: the stated AH-01 and AH-02 paper arguments survive this review.**
No invalid inference or missing frequency-dependent loss was found. In
particular the improved regime `Lambda/A -> 0` is supported by the discrete
argument; it does not inherit the old pointwise phase-replacement error.

Checks made:

1. Substitution `t=exp(-u/8)` gives exactly
   `W(u)=t(1-t)F(t)/8`. Since `F'(1)=2`, its expansion is
   `u/64-7u^2/1024+O(u^3)`. The decomposition in (3) bounds the difference
   globally by `7u^2/1024`; multiplying by `u^k exp(-xu)` gives exactly
   `7(k+2)!/(1024 x^(k+3))`. The displayed majorant pays differentiation
   and the sharp-coefficient dominated limit for every fixed k.
2. The k=1 lower estimate indeed gives `-T'(x)>=1/(64x^3)` for x>=4.
   For A>=8 and H<=A^3, the largest possible positive phase increment on
   `[A-1,2A]` is at most `(A/(A-1))^3/32<1/8`. There is no integer alias
   in the coherent phase. Constants in delta and its first two derivatives
   are absolute throughout `1<=Lambda<=A`.
3. The identity `1/(e(delta)-1)=-1/2-(i/2)cot(pi delta)` has the stated
   sign. `z_n=q_n(z_(n+1)-z_n)` gives exactly (8), including the final
   `q(b-1)z_b` endpoint. Reapplying it uses `p_n=(q_(n-1)-q_n)q_n`;
   its endpoints and variation cost `O(A/Lambda^2)`. The product derivative
   is `w'q+wq'`, both terms `O(1/Lambda^2)`. A separate exact Fraction
   algebra probe checked 30 finite intervals, including singleton and empty
   remainder cases, and exited zero. An initial hard-coded output said 35;
   rerunning with an actual counter corrected that reporting error to 30.
   This only cross-checks the algebra.
4. Inverting `delta=H/(32x^3)+O(H/x^4)` introduces `O(x^2/H)` before
   normalization, hence `O(1/(A Lambda))` after normalization. The cotangent
   correction is O(1), hence O(1/A). Replacing b-1 by b costs
   `O(1/(A Lambda))`. All fit the claimed `O(Lambda^-2+A^-1)`.
5. The half-turn endpoint exists once Lambda exceeds an absolute threshold.
   Its displacement is `O(A/Lambda)`. Rounding costs `O(Lambda/A)` in phase
   and therefore O(1/A) in the sum formula. The required bound on f' follows
   from the preceding `-T'` estimate (the phrase "derivative bound in (6)"
   is shorthand; (6) itself writes delta derivatives). Thus the bracket has
   size `16+O(1/Lambda+Lambda/A)`. The coefficient is 16/(pi Lambda),
   giving `256/(pi Lambda)` with the stated error. Bounded Lambda is covered
   by one larger absolute constant, as claimed.

The result concerns only `s*=-pi/16`. Smoothness and small increments here
come from the coherent tail; the original zero-seeded completed exponential
term cannot be removed. The stronger asymptotic therefore improves the
countermodel calibration and is not a source-selected little-o saving.
