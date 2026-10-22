"""Independent full-ring, action-level and noisy-observer validation."""
from fractions import Fraction as F
from itertools import product
import unittest
from observational_succ.witt_carry_learning import (
 LearningSourceError, full_ring_tables,full_ring_homogeneous_projection,
 geometric_bt_ball_profile,p_step_unipotent_probe,
 majority_failure_probability, calibrated_majority_budget, digits_of,
 mixed_add,equal_add,carry_cocycle,
)

class GlobalStructureVersusObservation(unittest.TestCase):
 def test_complete_ring_tables_are_different_from_unlabelled_tree(self):
  for p,k in ((2,2),(3,2),(2,3),(5,2)):
   a=full_ring_tables(p,k,'mixed')
   b=full_ring_tables(p,k,'equal')
   self.assertEqual(a['size'],b['size'])
   self.assertNotEqual(a['add'],b['add'])
   self.assertEqual(a['add'][0],b['add'][0])
   self.assertEqual(a['mul'][0],b['mul'][0])
   self.assertEqual(a['add'][p-1][1],p)
   self.assertEqual(b['add'][p-1][1],0)

 def test_complete_padic_arithmetic_descent_all_stage_operations(self):
  for p,k in ((2,2),(2,3),(3,2),(5,2)):
   for model in ('mixed','equal'):
    self.assertEqual(full_ring_homogeneous_projection(p,k,model),2*p**(2*k))

 def test_geometric_tree_alone_cannot_distinguish_any_depth(self):
  for p in (2,3,5,7):
   for R in range(0,8):
    data=geometric_bt_ball_profile(p,R)
    expected=1+(p+1)*sum(p**i for i in range(R))
    self.assertEqual(data['total'],expected)
    self.assertFalse(data['ring_characteristic_identifiable_from_unlabelled_graph'])

 def test_S_to_the_p_discriminates_at_second_rung(self):
  for p in (2,3,5,7):
   self.assertEqual(p_step_unipotent_probe(p,1,'mixed'),0)
   self.assertEqual(p_step_unipotent_probe(p,1,'equal'),0)
   for x in (0,1,p-1,p,p*p-1):
    self.assertEqual(p_step_unipotent_probe(p,2,'mixed',x),(x+p)%(p*p))
    self.assertEqual(p_step_unipotent_probe(p,2,'equal',x),x%(p*p))

 def test_source_carry_two_cocycle_never_absent_in_mixed_case(self):
  for p in (2,3,5,7):
   a=digits_of(p-1,p,2);b=digits_of(1,p,2)
   self.assertEqual(carry_cocycle(p-1,1,p),1)
   self.assertEqual(mixed_add(a,b,p)[0],(0,1))
   self.assertEqual(equal_add(a,b,p),(0,0))

class RepeatedRealisticObservationBudget(unittest.TestCase):
 def test_binomial_majority_exact_known_calibrations(self):
  self.assertEqual(majority_failure_probability(F(1,4),1),F(1,4))
  self.assertEqual(majority_failure_probability(F(1,4),3),F(5,32))
  self.assertEqual(majority_failure_probability(F(1,2),3),F(1,2))
  self.assertEqual(majority_failure_probability(F(0),21),0)

 def test_independent_repeat_counts_can_satisfy_summable_error_budget(self):
  for e in (F(1,4),F(1,3)):
   for k in range(1,8):
    budget=calibrated_majority_budget(k,e,F(1,8))
    self.assertEqual(budget['repetitions']%2,1)
    self.assertLessEqual(budget['actual_error_upper_bound'],F(1,8*2**k))

 def test_monotone_repeated_budget_and_union_bound(self):
  data=[calibrated_majority_budget(k,F(1,4),F(1,8)) for k in range(1,11)]
  self.assertTrue(all(data[i]['repetitions']<=data[i+1]['repetitions'] for i in range(9)))
  self.assertLessEqual(sum(x['actual_error_upper_bound'] for x in data),F(1,8))

 def test_unreliable_or_unverified_measurement_rate_is_rejected(self):
  for e in (F(1,2),F(2,3),1.0):
   with self.assertRaises(LearningSourceError):
    calibrated_majority_budget(1,e)
  for m in (0,2,400):
   with self.assertRaises(LearningSourceError):
    majority_failure_probability(F(1,4),m)

class CompleteFiniteTableCalibration(unittest.TestCase):
 def test_finite_whole_source_table_noise_budget(self):
  from observational_succ.witt_carry_learning import calibrated_ring_table_budget
  for p,k in ((2,1),(2,2),(2,3),(3,1),(3,2)):
   result=calibrated_ring_table_budget(p,k,F(1,4),F(1,8))
   self.assertEqual(result['table_queries'],2*p**(2*k))
   self.assertLessEqual(result['total_level_error_bound'],result['allocated_level_error'])
   self.assertFalse(result['actual_measurements_performed'])

 def test_all_level_union_budget_is_summable(self):
  from observational_succ.witt_carry_learning import calibrated_ring_table_budget
  reports=[calibrated_ring_table_budget(2,k,F(1,4),F(1,8)) for k in range(1,5)]
  self.assertLessEqual(sum(x['total_level_error_bound'] for x in reports),F(1,8))

 def test_calibration_gaps_refuse_false_certification(self):
  from observational_succ.witt_carry_learning import calibrated_ring_table_budget
  with self.assertRaises(LearningSourceError):calibrated_ring_table_budget(2,3,F(1,2))
  with self.assertRaises(LearningSourceError):calibrated_ring_table_budget(2,1,F(1,4),1)
