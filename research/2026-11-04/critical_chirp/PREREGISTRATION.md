# Preregistered independent checks — critical coherent-seed chirp

**Date 2026-11-04.** Strict parent Gamma Prybar #501 SHA af5c7ba30ea57d725bd334310798357d50f12fce. These predictions are locked BEFORE the fresh holdout execution below. Initial development used n=1,2,3,4,5,6,7,8,11,16,32,64,127,256 and A=4,8,16,32,64; they are NOT blind validation cases.

**Candidate theorem CC-01**: for every n>=1 the authentic BBP future tail T_n=sum_(k>=1)16^-k r(n+k) satisfies
0 < 1/(64n²)-T_n < 1/(64n³).
Prediction: independent rational partial-tail intervals at holdout n=137,509,911 are strictly within this analytically derived interval. Two algorithms must agree on the underlying original four-pole r(n) and polynomial Q/D. A failure kills the proposed global inequality.

**Candidate CC-02**: for the *coherent wrong seed only*, for integer H_A>0 and Λ_A=H_A/A²→∞, Λ_A²/A→0, the maximal subinterval coefficient M_A(H_A)= A^-1 max_{I⊂[A,2A)}|sum_(n∈I)e(-H_A T_n)| satisfies Λ_A M_A(H_A)→256/π, with error O(1/Λ_A+Λ_A²/A). This is a PAPER derivation, not certified by numerics. We calibrate the continuous comparison integral separately at μ=8,32,128 using 60- and 90-digit quadrature, with a half-turn interval explicitly chosen to realize the leading endpoint term: predict μ|integral|→4/π. These numerical cases are instrument tests, not a proof of global maximality.

**Candidate CC-03**: finite exact nonasymptotic counterseed obstruction. For A=191, L=64, H=A²L, m=min(A,floor(4A/L)), the certified source-tail decrement yields a block with phase span <1/8 cycle and M_A(H)>=m/(2A). No floating point is required to verify this *lower bound*. It is seed-specific and says nothing about the zero-seeded orbit.

**Negative controls:** fixed coherent source with same forcing must **not** satisfy o(A²/H) at the critical frequency; the original zero-seed must not be asserted to satisfy any high-frequency saving without a new signed estimate. Any claim that averaged moving high-frequency Bessel bounds select the required j is unsupported and must remain OPEN.

No π digit inputs. No extrapolating finite epochs to asymptotic π normality. A good result is a validated tight calibration / method obstruction, not a fake solution.
