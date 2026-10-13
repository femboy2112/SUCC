import Std

/- Exact predicate core of the reviewed F48 relational-interface theorem.
   It does not formalize the incidence sheaf or a quantum interpretation. -/
namespace SWM.F48
universe u v

def ExactCompressedJoin {I : Type u} {O : Type v} (q : I → O) : Prop :=
  ∀ L R : I → Prop,
    (∃ x y, L x ∧ R y ∧ q x = q y) ↔ (∃ z, L z ∧ R z)

theorem exact_compressed_join_iff_injective {I : Type u} {O : Type v}
    (q : I → O) : ExactCompressedJoin q ↔ (∀ x y, q x = q y → x = y) := by
  constructor
  · intro h x y hxy
    have hs : ∃ a b, a = x ∧ b = y ∧ q a = q b := ⟨x, y, rfl, rfl, hxy⟩
    obtain ⟨z, hzx, hzy⟩ := (h (fun a => a = x) (fun b => b = y)).mp hs
    exact hzx.symm.trans hzy
  · intro hi L R
    constructor
    · rintro ⟨x, y, hx, hy, hxy⟩
      have heq : x = y := hi x y hxy
      subst y
      exact ⟨x, hx, hy⟩
    · rintro ⟨z, hzL, hzR⟩
      exact ⟨z, z, hzL, hzR, rfl⟩

theorem constant_bool_join_fails :
    ¬ ExactCompressedJoin (fun _ : Bool => ()) := by
  intro h
  have hi := (exact_compressed_join_iff_injective (fun _ : Bool => ())).mp h
  have heq : false = true := hi false true rfl
  cases heq

#print axioms exact_compressed_join_iff_injective
#print axioms constant_bool_join_fails
end SWM.F48
