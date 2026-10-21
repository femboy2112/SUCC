import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Topology.Instances.AddCircle
import Mathlib.Algebra.Periodic
import Mathlib.Tactic

/-!
# The genuine circle-to-logistic factor

The circle is mathlib's `AddCircle (1 : ℝ)`, not an interval with its
endpoints silently distinguished. The projection uses mathlib's `Real.pi`.
The theorem is about every point; it makes no genericity claim for pi.
-/

noncomputable section

namespace ObservationalSUCC.DuckPi

def logistic (x : ℝ) : ℝ := 4 * x * (1 - x)

def logisticLift (t : ℝ) : ℝ := Real.sin (Real.pi * t) ^ 2

theorem logisticLift_periodic : Function.Periodic logisticLift 1 := by
  intro t
  simp only [logisticLift, mul_add, mul_one, Real.sin_add_pi, neg_sq]

/-- A well-defined map on the actual quotient ℝ/ℤ. -/
def logisticHat : AddCircle (1 : ℝ) → ℝ := logisticLift_periodic.lift

@[simp] theorem logisticHat_coe (t : ℝ) :
    logisticHat (t : AddCircle (1 : ℝ)) = logisticLift t := rfl

theorem logisticLift_double (t : ℝ) :
    logisticLift (t + t) = logistic (logisticLift t) := by
  have h := Real.sin_sq_add_cos_sq (Real.pi * t)
  have hw := congrArg (fun z : ℝ => 4 * Real.sin (Real.pi * t) ^ 2 * z) h
  have ha : Real.pi * (t + t) = 2 * (Real.pi * t) := by ring
  simp only [logisticLift, logistic, ha, Real.sin_two_mul]
  nlinarith only [hw]

theorem logisticHat_double (t : AddCircle (1 : ℝ)) :
    logisticHat (t + t) = logistic (logisticHat t) := by
  induction t using QuotientAddGroup.induction_on with
  | H t => exact logisticLift_double t

theorem logisticHat_mem_unitInterval (t : AddCircle (1 : ℝ)) :
    logisticHat t ∈ Set.Icc (0 : ℝ) 1 := by
  induction t using QuotientAddGroup.induction_on with
  | H t =>
    change 0 ≤ Real.sin (Real.pi * t) ^ 2 ∧ Real.sin (Real.pi * t) ^ 2 ≤ 1
    constructor
    · positivity
    · nlinarith [Real.sin_sq_add_cos_sq (Real.pi * t),
        sq_nonneg (Real.cos (Real.pi * t))]

theorem logisticHat_surjOn_unitInterval :
    Set.SurjOn logisticHat Set.univ (Set.Icc (0 : ℝ) 1) := by
  intro x hx
  refine ⟨((Real.arcsin (Real.sqrt x) / Real.pi : ℝ) : AddCircle (1 : ℝ)),
    Set.mem_univ _, ?_⟩
  rw [logisticHat_coe, logisticLift]
  have hp : Real.pi ≠ 0 := Real.pi_ne_zero
  rw [mul_div_cancel₀ _ hp]
  rw [Real.sin_arcsin (by positivity) (Real.sqrt_le_one.mpr hx.2)]
  exact Real.sq_sqrt hx.1

theorem logisticHat_not_injective : ¬ Function.Injective logisticHat := by
  intro h
  have heq : logisticHat ((1 / 4 : ℝ) : AddCircle (1 : ℝ)) =
      logisticHat ((3 / 4 : ℝ) : AddCircle (1 : ℝ)) := by
    simp only [logisticHat_coe, logisticLift]
    have ha : Real.pi * (3 / 4 : ℝ) = Real.pi - Real.pi * (1 / 4 : ℝ) := by ring
    rw [ha, Real.sin_pi_sub]
  have same := h heq
  have bad : (1 / 4 : ℝ) = 3 / 4 :=
    (AddCircle.coe_eq_coe_iff_of_mem_Ico
      (p := (1 : ℝ)) (a := (0 : ℝ)) (by norm_num) (by norm_num)).mp same
  norm_num at bad

/-- A typed factor onto the closed unit interval. -/
def logisticHatUnit (t : AddCircle (1 : ℝ)) : Set.Icc (0 : ℝ) 1 :=
  ⟨logisticHat t, logisticHat_mem_unitInterval t⟩

theorem logistic_mem_unitInterval (x : Set.Icc (0 : ℝ) 1) :
    logistic x ∈ Set.Icc (0 : ℝ) 1 := by
  constructor
  · exact mul_nonneg (mul_nonneg (by norm_num) x.property.1)
      (sub_nonneg.mpr x.property.2)
  · dsimp [logistic]
    nlinarith [sq_nonneg (2 * (x : ℝ) - 1)]

def logisticUnit (x : Set.Icc (0 : ℝ) 1) : Set.Icc (0 : ℝ) 1 :=
  ⟨logistic x, logistic_mem_unitInterval x⟩

theorem logisticHatUnit_surjective : Function.Surjective logisticHatUnit := by
  intro x
  obtain ⟨t, _, ht⟩ := logisticHat_surjOn_unitInterval x.property
  exact ⟨t, Subtype.ext ht⟩

theorem logisticHatUnit_semiconj :
    Function.Semiconj logisticHatUnit (fun t => t + t) logisticUnit := by
  intro t
  exact Subtype.ext (logisticHat_double t)

end ObservationalSUCC.DuckPi
