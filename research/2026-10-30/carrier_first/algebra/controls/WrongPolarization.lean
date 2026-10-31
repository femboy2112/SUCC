import Std

/-! Deliberately false mutation. Validation must reject this file. -/
example : (5 : Int)*(5-1) - 2*(2-1) - 3*(3-1) = 2*2*3+1 := by
  decide
