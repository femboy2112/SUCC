import Yean.SUCC.TwoPoint
import Yean.SUCC.FiniteRetract
import Mathlib.Tactic.FinCases
namespace Yean.SUCC.RuntimeInstance
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000
def pullTable (j : Fin 2) (i : Fin 4) : ℚ := if j.val = 0 ∧ i.val = 0 then ((1 : ℚ) / 1) else (if j.val = 0 ∧ i.val = 2 then ((1 : ℚ) / 1) else (if j.val = 1 ∧ i.val = 1 then ((1 : ℚ) / 1) else (if j.val = 1 ∧ i.val = 3 then ((1 : ℚ) / 1) else (0))))
theorem pull_columns (j : Fin 2) (i : Fin 4) :
    FiniteRetract.cyclicPull (k := 2) (fun z => if z = j then 1 else 0) i = pullTable j i := by
  fin_cases j <;> fin_cases i <;>
    norm_num [pullTable, FiniteRetract.cyclicProject, FiniteRetract.cyclicPull,
      FiniteRetract.cyclicAverage, FiniteRetract.cyclicPush, FiniteRetract.push,
      FiniteRetract.cyclicChart, Fin.sum_univ_succ, finProdFinEquiv]
def averageTable (j : Fin 4) (i : Fin 2) : ℚ := if j.val = 0 ∧ i.val = 0 then ((1 : ℚ) / 2) else (if j.val = 1 ∧ i.val = 1 then ((1 : ℚ) / 2) else (if j.val = 2 ∧ i.val = 0 then ((1 : ℚ) / 2) else (if j.val = 3 ∧ i.val = 1 then ((1 : ℚ) / 2) else (0))))
theorem average_columns (j : Fin 4) (i : Fin 2) :
    FiniteRetract.cyclicAverage (n := 2) (k := 2) (fun z => if z = j then 1 else 0) i = averageTable j i := by
  fin_cases j <;> fin_cases i <;>
    norm_num [averageTable, FiniteRetract.cyclicProject, FiniteRetract.cyclicPull,
      FiniteRetract.cyclicAverage, FiniteRetract.cyclicPush, FiniteRetract.push,
      FiniteRetract.cyclicChart, Fin.sum_univ_succ, finProdFinEquiv]
def projectTable (j : Fin 4) (i : Fin 4) : ℚ := if j.val = 0 ∧ i.val = 0 then ((1 : ℚ) / 2) else (if j.val = 0 ∧ i.val = 2 then ((1 : ℚ) / 2) else (if j.val = 1 ∧ i.val = 1 then ((1 : ℚ) / 2) else (if j.val = 1 ∧ i.val = 3 then ((1 : ℚ) / 2) else (if j.val = 2 ∧ i.val = 0 then ((1 : ℚ) / 2) else (if j.val = 2 ∧ i.val = 2 then ((1 : ℚ) / 2) else (if j.val = 3 ∧ i.val = 1 then ((1 : ℚ) / 2) else (if j.val = 3 ∧ i.val = 3 then ((1 : ℚ) / 2) else (0))))))))
theorem project_columns (j : Fin 4) (i : Fin 4) :
    FiniteRetract.cyclicProject (n := 2) (k := 2) (fun z => if z = j then 1 else 0) i = projectTable j i := by
  fin_cases j <;> fin_cases i <;>
    norm_num [projectTable, FiniteRetract.cyclicProject, FiniteRetract.cyclicPull,
      FiniteRetract.cyclicAverage, FiniteRetract.cyclicPush, FiniteRetract.push,
      FiniteRetract.cyclicChart, Fin.sum_univ_succ, finProdFinEquiv]
theorem retraction (f : Fin 2 → ℚ) :
    FiniteRetract.cyclicAverage (k := 2) (FiniteRetract.cyclicPull f) = f :=
  FiniteRetract.cyclic_average_pull 2 2 (by decide) f
end Yean.SUCC.RuntimeInstance
set_option pp.all true
set_option pp.universes true
#check @Yean.SUCC.RuntimeInstance.pull_columns
#print axioms Yean.SUCC.RuntimeInstance.pull_columns
#check @Yean.SUCC.RuntimeInstance.average_columns
#print axioms Yean.SUCC.RuntimeInstance.average_columns
#check @Yean.SUCC.RuntimeInstance.project_columns
#print axioms Yean.SUCC.RuntimeInstance.project_columns
#check @Yean.SUCC.RuntimeInstance.retraction
#print axioms Yean.SUCC.RuntimeInstance.retraction
