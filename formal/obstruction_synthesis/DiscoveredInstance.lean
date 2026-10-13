import Std
set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 1000000
namespace SUCC.Discovered
/- Exact learned finite object, NOT latent coordinate formulas.
Source digest: ffaeffaecfd0c6e621b20359dfcb3ecf9d0691ae49467723148117f072c0c619
This file is generated from the calibration output and then checked by Lean. -/
def projectTable : List (Fin 9) := [0, 1, 2, 2, 3, 4, 5, 4, 2, 1, 6, 7, 3, 0, 1, 6, 7, 4, 7, 5, 6, 3, 8, 8, 0, 5, 8]
def project (x : Fin 27) : Fin 9 := projectTable[x.val]!
def sourceATable : List (Fin 27) := [17, 14, 6, 19, 21, 23, 20, 26, 25, 1, 3, 16, 4, 5, 9, 8, 18, 22, 11, 10, 2, 12, 0, 13, 7, 15, 24]
def sourceA (x : Fin 27) : Fin 27 := sourceATable[x.val]!
def sourceBTable : List (Fin 27) := [25, 7, 9, 14, 0, 3, 12, 8, 1, 17, 11, 22, 13, 6, 5, 18, 26, 2, 23, 21, 16, 24, 10, 15, 19, 4, 20]
def sourceB (x : Fin 27) : Fin 27 := sourceBTable[x.val]!
def sourceRTable : List (Fin 3) := [1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 1, 1, 0]
def sourceR (x : Fin 27) : Fin 3 := sourceRTable[x.val]!
def aTable : List (Fin 9) := [4, 1, 5, 3, 8, 6, 2, 7, 0]
def a (x : Fin 9) : Fin 9 := aTable[x.val]!
def bTable : List (Fin 9) := [5, 4, 1, 0, 2, 3, 7, 8, 6]
def b (x : Fin 9) : Fin 9 := bTable[x.val]!
def aiTable : List (Fin 9) := [8, 1, 6, 3, 0, 2, 5, 7, 4]
def ai (x : Fin 9) : Fin 9 := aiTable[x.val]!
def biTable : List (Fin 9) := [3, 2, 4, 5, 1, 0, 8, 6, 7]
def bi (x : Fin 9) : Fin 9 := biTable[x.val]!
def hTable : List (Fin 9) := [8, 3, 5, 7, 0, 6, 2, 1, 4]
def h (x : Fin 9) : Fin 9 := hTable[x.val]!
def rTable : List (Fin 3) := [1, 2, 2, 1, 2, 1, 0, 0, 0]
def r (x : Fin 9) : Fin 3 := rTable[x.val]!

theorem sourceA_naturality : ∀ x : Fin 27, project (sourceA x) = a (project x) := by decide
theorem sourceB_naturality : ∀ x : Fin 27, project (sourceB x) = b (project x) := by decide
theorem readout_preserved : ∀ x : Fin 27, sourceR x = r (project x) := by decide
theorem discovered_separator : ∀ x y : Fin 27, project x = project y ↔ (sourceR x, sourceR (sourceA x)) = (sourceR y, sourceR (sourceA y)) := by decide
theorem not_full_state_recovery : ∃ x y : Fin 27, x ≠ y ∧ project x = project y := by
  exact ⟨0, 13, by decide, by decide⟩
theorem noncommuting : ∃ x : Fin 9, a (b x) ≠ b (a x) := by
  exact ⟨0, by decide⟩
theorem commutator_word : ∀ x : Fin 9, h x = bi (ai (b (a x))) := by decide
theorem commutator_central : ∀ x : Fin 9, h (a x) = a (h x) ∧ h (b x) = b (h x) := by decide
theorem commutator_period_three : (∀ x : Fin 9, h (h (h x)) = x) ∧ (∃ x : Fin 9, h x ≠ x) := by
  constructor
  · decide
  · exact ⟨0, by decide⟩
#print axioms sourceA_naturality
#print axioms sourceB_naturality
#print axioms readout_preserved
#print axioms discovered_separator
#print axioms not_full_state_recovery
#print axioms noncommuting
#print axioms commutator_word
#print axioms commutator_central
#print axioms commutator_period_three
end SUCC.Discovered
