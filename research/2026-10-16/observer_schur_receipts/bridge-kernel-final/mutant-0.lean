import Yean.SUCC.TwoPoint
import Yean.SUCC.FiniteRetract
import Mathlib.Tactic.FinCases
namespace Yean.SUCC.RuntimeInstance
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000
def word : Word ℕ := [.shift 1, .scale 2, .shift 3, .scale 3]
theorem normalized : Word.normalize word = (⟨6, 16⟩ : Affine ℕ) := by decide
theorem prime_admission : Word.PrimeWord word := by
  norm_num [Word.PrimeWord, word] <;> decide
theorem all_inputs (x : ℕ) : Word.run word x = 6 * x + 15 := by
  rw [← Word.normalize_sound, normalized]
  rfl
end Yean.SUCC.RuntimeInstance
set_option pp.all true
set_option pp.universes true
#check @Yean.SUCC.RuntimeInstance.normalized
#print axioms Yean.SUCC.RuntimeInstance.normalized
#check @Yean.SUCC.RuntimeInstance.prime_admission
#print axioms Yean.SUCC.RuntimeInstance.prime_admission
#check @Yean.SUCC.RuntimeInstance.all_inputs
#print axioms Yean.SUCC.RuntimeInstance.all_inputs
