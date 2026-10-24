"""Hostile exact finite models for SUCC learning in the projective limit."""
from __future__ import annotations
import unittest
from fractions import Fraction
from itertools import product
from math import factorial
from observational_succ.witt_carry_learning import (
 LearningSourceError, digits_of, integer_of, mixed_add, equal_add, mixed_mul,
 equal_mul, carry_cocycle, cocycle_square, extension_witness,
 first_carry_witness, distance_exponent, finite_distance,
 digit_map_preserves_distance, learning_signature, update_version_space,
 append_verified_digit, compatible_observer_prefixes, sparse_factorial_prefix,
 delayed_tower_counterfeit,
)

class WittVersusDualTests(unittest.TestCase):
 def test_digit_roundtrips_and_parent_maps(self):
  for p,k in ((2,5),(3,4),(5,3)):
   for n in range(p**k):
    ds=digits_of(n,p,k)
    self.assertEqual(integer_of(ds,p),n)
    if k>1:self.assertEqual(integer_of(ds[:-1],p),n%p**(k-1))

 def test_mixed_carry_addition_matches_independent_integer_modulo(self):
  for p,k in ((2,4),(3,3),(5,2)):
   N=p**k
   for x,y in product(range(N),repeat=2):
    got,carry=mixed_add(digits_of(x,p,k),digits_of(y,p,k),p)
    self.assertEqual(integer_of(got,p),(x+y)%N)
    self.assertTrue(all(c in (0,1) for c in carry))

 def test_equal_characteristic_polynomial_law_independent_oracle(self):
  for p,k in ((2,4),(3,3),(5,2)):
   N=p**k
   for x,y in product(range(N),repeat=2):
    a,b=digits_of(x,p,k),digits_of(y,p,k)
    self.assertEqual(equal_add(a,b,p),tuple((a[i]+b[i])%p for i in range(k)))
    # independent ordinary polynomial convolution as a direct source check
    expected=tuple(sum(a[i]*b[j-i] for i in range(j+1))%p for j in range(k))
    self.assertEqual(equal_mul(a,b,p),expected)

 def test_mixed_multiplication_matches_actual_modular_ring(self):
  for p,k in ((2,4),(3,3),(5,2)):
   N=p**k
   for x,y in product(range(N),repeat=2):
    actual=integer_of(mixed_mul(digits_of(x,p,k),digits_of(y,p,k),p),p)
    self.assertEqual(actual,(x*y)%N)

 def test_same_first_order_nilpotent_shadow_different_whole_ring(self):
  for p in (2,3,5,7):
   out=extension_witness(p)
   self.assertEqual(out['size'],p*p)
   self.assertEqual(out['maximal_ideal_size'],p)
   self.assertEqual(out['mixed_ring_characteristic'],p*p)
   self.assertEqual(out['equal_ring_characteristic'],p)
   self.assertEqual(out['mixed_p_times_one'],(0,1))
   self.assertEqual(out['equal_p_times_one'],(0,0))
   # all elements of radical (p) or (t) square to zero mod (p^2)/(t^2)
   for a in range(p):
    rad=(0,a)
    self.assertEqual(mixed_mul(rad,rad,p),(0,0))
    self.assertEqual(equal_mul(rad,rad,p),(0,0))

 def test_p_additions_create_one_nontrivial_carry(self):
  for p in (2,3,5,7):
   x=first_carry_witness(p)
   self.assertEqual(x['mixed_sum'],(0,1))
   self.assertEqual(x['equal_sum'],(0,0))
   self.assertEqual(x['carry_history'][0],1)

 def test_carry_function_is_actual_normalized_two_cocycle(self):
  for p in (2,3,5,7):
   for a,b,c in product(range(p),repeat=3):
    self.assertEqual(cocycle_square(a,b,c,p)[0],cocycle_square(a,b,c,p)[1])
   for x in range(p):
    self.assertEqual(carry_cocycle(0,x,p),0)
    self.assertEqual(carry_cocycle(x,0,p),0)

 def test_additive_extension_not_split_by_any_lift_of_one(self):
  for p in (2,3,5,7):
   for lift in range(1,p*p,p):
    self.assertEqual((p*lift)%(p*p),p)
    # In the dual-number additive group every element has order at most p.
    self.assertNotEqual((p*lift)%(p*p),0)

 def test_hierarchy_first_shell_is_identical(self):
  for p in (2,3,5,7):
   self.assertEqual(learning_signature(p,1,'mixed','geometry'),learning_signature(p,1,'equal','geometry'))
   self.assertEqual(learning_signature(p,1,'mixed','marked_addition'),learning_signature(p,1,'equal','marked_addition'))

class StructuralNonidentifiability(unittest.TestCase):
 def test_all_finite_geometries_underdetermine_ring_characteristic(self):
  for p in (2,3,5):
   for k in range(1,8):
    self.assertEqual(learning_signature(p,k,'mixed','geometry'),learning_signature(p,k,'equal','geometry'))

 def test_digit_identification_is_exact_isometry_not_ring_isomorphism(self):
  for p,k in ((2,5),(3,4),(5,3)):
   N=p**k
   for x,y in product(range(N),repeat=2):
    self.assertTrue(digit_map_preserves_distance(p,k,x,y))
    if x==y:
     self.assertEqual(finite_distance(digits_of(x,p,k),digits_of(y,p,k),p)['observational_status'],'unresolved')

 def test_observer_geometry_toolkit_never_eliminates_any_ring_source(self):
  for p in (2,3,5):
   data=tuple((k,learning_signature(p,k,'mixed','geometry')) for k in range(1,7))
   out=update_version_space(p,data,'geometry')
   self.assertEqual(out['survivors'],('equal','mixed'))
   self.assertFalse(out['source_physically_authenticated'])
   self.assertFalse(out['infinite_completion_proved_by_finite_records'])

 def test_one_marked_addition_at_second_stage_discriminates(self):
  for p in (2,3,5):
   for source,other in (('mixed','equal'),('equal','mixed')):
    data=tuple((k,learning_signature(p,k,source,'marked_addition')) for k in (1,2))
    out=update_version_space(p,data,'marked_addition')
    self.assertEqual(out['history'][0][1],('equal','mixed'))
    self.assertEqual(out['survivors'],(source,))
    self.assertNotEqual(learning_signature(p,2,source,'marked_addition'),learning_signature(p,2,other,'marked_addition'))

 def test_no_source_typed_probe_means_no_truth_identification(self):
  for p in (2,3,5):
   ambiguous=update_version_space(p,(),'geometry')
   self.assertEqual(ambiguous['survivors'],('equal','mixed'))
   sample=((1,learning_signature(p,1,'mixed','marked_addition')),)
   self.assertEqual(update_version_space(p,sample,'marked_addition')['survivors'],('equal','mixed'))

 def test_wrong_source_or_state_history_fails_closed(self):
  with self.assertRaises(LearningSourceError):digits_of(True,2,3)
  with self.assertRaises(LearningSourceError):digits_of(5,4,3)
  with self.assertRaises(LearningSourceError):integer_of((0,1.0),2)
  with self.assertRaises(LearningSourceError):mixed_add((1,0),(0,1,0),2)
  with self.assertRaises(LearningSourceError):update_version_space(2,((2,(1,)),(1,(2,))),'marked_addition')
  with self.assertRaises(LearningSourceError):update_version_space(2,((1,None),),'UNDECLARED_SENSOR')

class ObservationLimitConstruction(unittest.TestCase):
 def test_each_new_digit_is_finitely_computable_and_source_consistent(self):
  for p in (2,3,5):
   prefix=()
   for k in range(1,10):
    raw=append_verified_digit(prefix,(k*k+1)%p,p)
    self.assertEqual(raw['digits'][:-1],prefix)
    self.assertEqual(raw['representative']%(p**(k-1)),integer_of(prefix,p) if prefix else 0)
    self.assertEqual(raw['cylinder_diameter_bound'],Fraction(1,p**k))
    prefix=raw['digits']

 def test_nested_cylinders_quantitative_cauchy_bound(self):
  for p in (2,3,5):
   ds=tuple((3*j+2)%p for j in range(10))
   for k in range(1,10):
    earlier=integer_of(ds[:k],p)
    for h in range(k+1,11):
     later=integer_of(ds[:h],p)
     self.assertEqual((later-earlier)%(p**k),0)

 def test_source_histories_must_be_compatible_or_rejected(self):
  good=((0,),(0,1),(0,1,1),(0,1,1,0))
  result=compatible_observer_prefixes(good,2)
  self.assertEqual(result['last_cylinder_diameter_bound'],Fraction(1,16))
  self.assertFalse(result['all_infinite_stages_were_observed'])
  with self.assertRaises(LearningSourceError):compatible_observer_prefixes(((0,),(1,0)),2)
  with self.assertRaises(LearningSourceError):compatible_observer_prefixes(((0,),(0,1,1)),2)

 def test_sparse_factorial_stream_is_a_profinite_ghost_of_original_integers(self):
  for p in (2,3,5):
   for k in range(1,13):
    ds=sparse_factorial_prefix(p,k)
    self.assertEqual(len(ds),k)
    self.assertEqual(set(i for i,d in enumerate(ds) if d),set(i for i in (2,6) if i<k))
    if k>1:self.assertEqual(ds[:-1],sparse_factorial_prefix(p,k-1))
    self.assertTrue(integer_of(ds,p)>=0)

 def test_arbitrarily_delayed_valid_divergent_source_towers(self):
  for p in (2,3,5):
   for K in range(1,10):
    x=delayed_tower_counterfeit(p,K)
    self.assertEqual(x['honest'][:K],x['counterfeit'][:K])
    self.assertNotEqual(x['honest'][K],x['counterfeit'][K])
    self.assertEqual(x['divergence_level'],K+1)
    self.assertTrue(all(x['counterfeit'][k+1]%x['counterfeit'][k]==0 for k in range(len(x['counterfeit'])-1)))

 def test_finite_depth_same_reading_not_global_equality(self):
  for p in (2,3):
   for k in range(1,8):
    a=digits_of(1,p,k); b=digits_of(1+p**k,p,k)
    self.assertEqual(a,b)
    self.assertEqual(finite_distance(a,b,p)['upper_bound'],Fraction(1,p**k))

 def test_unbounded_source_no_finite_global_readings_asserted(self):
  for p in (2,3):
   report=compatible_observer_prefixes(tuple(sparse_factorial_prefix(p,k) for k in range(1,7)),p)
   self.assertFalse(report['all_infinite_stages_were_observed'])
   self.assertTrue(report['limit_would_be_unique_if_all_levels_source_compatible'])

if __name__=='__main__':unittest.main()
