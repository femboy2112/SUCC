/-
Mason-Stothers degree-descent: the arithmetic CORE of the polynomial-abc bound,
formalized mathlib-free and kernel-checked in Lean 4.14.

HONEST SCOPE. This file proves ONLY the final integer-degree step of the
Mason-Stothers proof: given the degree bookkeeping that the (sympy-verified)
polynomial lemmas supply, the target bound follows by linear arithmetic over the
integers. The reduction is:

  let dA,dB,dC = deg A, deg B, deg C; dRad = deg rad(ABC); dW = deg W;
      dM = deg ((ABC)/rad(ABC)).
  Facts supplied by the polynomial layer (see FORMALIZATION DEBT):
    (H1)  dM = dA + dB + dC - dRad          (deg of the quotient)
    (H2)  dM <= dW                          (from M | W with W != 0)
    (H3a) dW <= dA + dB - 1                  (deg W = deg(A'B - AB'))
    (H3b) dW <= dB + dC - 1                  (cyclic form W = B'C - BC')
    (H3c) dW <= dA + dC - 1                  (cyclic form W = A'C - AC')
  Conclusion:  max(dA,dB,dC) <= dRad - 1.

FORMALIZATION DEBT (NOT proved here; exactly verified in sympy in
observational_succ/mason_stothers.py over an exact field):
  (1) W = A'B - AB' != 0 in characteristic 0 (fails in char p: W(x^p,1)=0);
  (2) for each irreducible P, v_P(W) >= v_P(ABC) - 1, hence (ABC)/rad(ABC) | W;
  (3) deg W <= deg A + deg B - 1 and its two cyclic forms.
These require a polynomial / UFD / derivation library (mathlib) and are left as
explicit, disclosed debt. No `sorry`, `admit`, `axiom`, or `native_decide` is
used anywhere in this file; the two theorems below are closed by the core
`omega` tactic and are genuinely kernel-checked.
-/
namespace ObservationalSUCC.MasonStothers

/-- The single-variable descent: `deg C <= deg rad(ABC) - 1`. -/
theorem degree_descent
    (dA dB dC dRad dW dM : Int)
    (hM  : dM = dA + dB + dC - dRad)
    (hMW : dM ≤ dW)
    (hW  : dW ≤ dA + dB - 1) :
    dC ≤ dRad - 1 := by
  omega

/-- The full symmetric conclusion: every one of `deg A, deg B, deg C` is at most
    `deg rad(ABC) - 1`, using the three cyclic Wronskian degree bounds. -/
theorem degree_descent_all
    (dA dB dC dRad dW dM : Int)
    (hM   : dM = dA + dB + dC - dRad)
    (hMW  : dM ≤ dW)
    (hWab : dW ≤ dA + dB - 1)
    (hWbc : dW ≤ dB + dC - 1)
    (hWac : dW ≤ dA + dC - 1) :
    dA ≤ dRad - 1 ∧ dB ≤ dRad - 1 ∧ dC ≤ dRad - 1 := by
  refine ⟨?_, ?_, ?_⟩ <;> omega

end ObservationalSUCC.MasonStothers
