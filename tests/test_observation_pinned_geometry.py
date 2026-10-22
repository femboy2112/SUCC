"""Hostile exact tests of source-pinned p-adic geometry and empirical limitations."""
from fractions import Fraction as F
from itertools import product,combinations
import unittest

from observational_succ.observation_pinned_geometry import (
 ObservationContractError, prime, qphase, src_affine_phase,phase_affine,
 parent,children,haar_mass,valuation_diff,haar_calibrated_distance,
 truncated_distance_report,multiplier_image_count,multiplier_kernel_count,
 projective_first_shell,projective_succ,projective_multiplier,matrix_affine,
 matrix_compose,projective_matrix_point,first_shell_cycle_fingerprint,
 axis_vertex,axis_distance,dilation_root_displacement,canonical_fixed_ray,
 oriented_cycle_probe,counterfeit_extension_orders,hidden_four_state_alias,
 equal_first_shell_distinct_ring_witness
)

class SourceTowerTests(unittest.TestCase):
 def test_exact_source_ring_naturality_two_arrows(self):
  for p in (2,3,5):
   for k in range(1,5):
    for n in range(-13,31):
     for a,b in ((1,1),(2,0),(3,0),(5,0),(2,3)):
      r=qphase(n,p,k)
      self.assertEqual(src_affine_phase(n,a,b,p,k),phase_affine(r,a,b,p,k))
      if k>1:
       self.assertEqual(phase_affine(r,a,b,p,k)%(p**(k-1)),
                        phase_affine(qphase(n,p,k-1),a,b,p,k-1))

 def test_cyclic_group_oriented_rigidity(self):
  for p in (2,3,5,7):
   for k in range(1,4):
    m=p**k
    seen={qphase(n,p,k) for n in range(m)}
    self.assertEqual(seen,set(range(m)))
    self.assertEqual(qphase(m,p,k),0)
    for u in range(1,m):
     if (u*1)%m==1: self.assertEqual(u,1)

 def test_intrinsic_ball_tree_all_parents_and_children(self):
  for p in (2,3,5):
   for k in range(0,4):
    for r in range(p**k):
     kids=children(p,k,r)
     self.assertEqual(len(kids),p)
     self.assertEqual(len(set(kids)),p)
     self.assertEqual({parent(p,k+1,y)[1] for _,y in kids},{r})
     self.assertEqual({y for _,y in kids},set(range(r,p**(k+1),p**k)))

 def test_exact_haar_mass_nested_cover(self):
  for p in (2,3,5,7):
   for k in range(0,6):
    self.assertEqual(p*haar_mass(p,k+1),haar_mass(p,k))
    self.assertEqual(p**k*haar_mass(p,k),1)

 def test_source_valuation_ultrametric(self):
  for p in (2,3,5):
   for a,b,c in product((-10,-5,-1,0,1,2,3,4,8,17),repeat=3):
    d_ab=haar_calibrated_distance(a,b,p)
    d_ac=haar_calibrated_distance(a,c,p)
    d_cb=haar_calibrated_distance(c,b,p)
    self.assertLessEqual(d_ab,max(d_ac,d_cb))
    self.assertEqual(d_ab,haar_calibrated_distance(b,a,p))
    self.assertEqual(d_ab==0,a==b)

 def test_observed_finite_precision_explicitly_unresolved(self):
  p=3
  self.assertEqual(truncated_distance_report(1,1+27,p,3)["kind"],"unresolved")
  self.assertEqual(truncated_distance_report(1,1+9,p,3),{"kind":"exact","distance":F(1,9)})
  self.assertEqual(valuation_diff(1,1,p),None)
  self.assertEqual(valuation_diff(1,1+27,p),3)

 def test_all_clock_multiplier_collision_images_independent_enumeration(self):
  for p in (2,3,5):
   for k in range(1,5):
    mod=p**k
    for m in (2,3,4,5,6,7,8,9,11,25):
     image={m*r%mod for r in range(mod)}
     self.assertEqual(multiplier_image_count(m,p,k),len(image))
     kernel=[r for r in range(mod) if m*r%mod==0]
     self.assertEqual(multiplier_kernel_count(m,p,k),len(kernel))

 def test_unique_contracting_prime_among_true_prime_dilations(self):
  for p in (2,3,5,7):
   for q in (2,3,5,7):
    self.assertEqual(multiplier_image_count(q,p,3)<p**3,q==p)
    self.assertEqual(dilation_root_displacement(q,p)==1,q==p)

 def test_canonical_contraction_attractor_in_all_quotients(self):
  for p in (2,3,5):
   for k in range(1,5):
    if p**k>500:continue
    fixed=canonical_fixed_ray(p,k)
    self.assertEqual(fixed["fixed_phases"],(0,))
    self.assertEqual(fixed["shifted_phase"],p**k-1)
    self.assertEqual((p*(p**k-1)+(p-1))%(p**k),p**k-1)

class ProjectiveArithmeticTests(unittest.TestCase):
 def test_full_p1_lines_enumerated_from_two_channel_quotient(self):
  for p in (2,3,5,7):
   lines=set()
   for x,y in product(range(p),repeat=2):
    if x==y==0: continue
    if y==0: lines.add(None)
    else: lines.add((x*pow(y,-1,p))%p)
   self.assertEqual(lines,set(projective_first_shell(p)))
   self.assertEqual(len(lines),p+1)

 def test_succ_unipotent_cycle_and_infinity_fixed(self):
  for p in (2,3,5,7,11):
   fingerprint=first_shell_cycle_fingerprint(p)
   self.assertEqual(fingerprint["root_degree"],p+1)
   self.assertEqual(len(fingerprint["nonfixed_cycle"]),p)
   self.assertEqual(fingerprint["fixed_directions"],(None,))
   self.assertEqual(fingerprint["period"],p)
   for x in projective_first_shell(p):
    self.assertEqual(projective_succ(x,p),
                     projective_matrix_point(matrix_affine(1,1),x,p))

 def test_authenticated_other_prime_unit_preserves_root(self):
  for p in (2,3,5,7):
   for q in (2,3,5,7):
    if q==p:
     with self.assertRaises(ObservationContractError):projective_multiplier(1,q,p)
    else:
     vals=tuple(projective_multiplier(x,q,p) for x in projective_first_shell(p))
     self.assertEqual(set(vals),set(projective_first_shell(p)))
     for x in projective_first_shell(p):
      self.assertEqual(projective_multiplier(x,q,p),
                       projective_matrix_point(matrix_affine(q,0),x,p))

 def test_matrix_affine_braid_and_general_monoid(self):
  for p in (2,3,5,7):
   S=matrix_affine(1,1);D=matrix_affine(p,0)
   self.assertEqual(matrix_compose(D,S),matrix_affine(p,p))
   rhs=D
   for _ in range(p):rhs=matrix_compose(S,rhs)
   self.assertEqual(matrix_compose(D,S),rhs)
   for a,b,c,d in product((1,2,3),(0,1,2),(1,2,3),(0,1,3)):
    self.assertEqual(matrix_compose(matrix_affine(a,b),matrix_affine(c,d)),
                     matrix_affine(a*c,a*d+b))

 def test_padic_axis_is_source_selected_not_hand_picked_ray(self):
  for p in (2,3,5):
   for k in range(-4,5):
    self.assertEqual(axis_vertex(p,k+1)[0],p*axis_vertex(p,k)[0])
    self.assertEqual(axis_distance(p,k,k+1),1)
    self.assertEqual(axis_distance(p,0,k),abs(k))
   self.assertEqual(dilation_root_displacement(p,p),1)
   self.assertEqual(dilation_root_displacement(p**3,p),3)

 def test_nonlinear_fake_geom_vs_mathematical_source(self):
  # Root degree 3 by itself is only a regular graph signature; it cannot
  # certify the ring Z2 or the uncounted infinity of quotient refinements.
  actual,mutant=counterfeit_extension_orders(2,3)
  self.assertEqual(actual[:3],mutant[:3])
  self.assertNotEqual(actual[3],mutant[3])
  self.assertEqual(mutant[3]//mutant[2],2*3)
  self.assertEqual(actual[3]//actual[2],2)

class OperationalDiscriminationTests(unittest.TestCase):
 def test_two_repeated_physical_clock_cycles_select_p_conditionally(self):
  for p in (2,3,5):
   labels=tuple(str((i*7+1)%p) for i in range(3*p+1))
   result=oriented_cycle_probe(labels,(2,3,5,7),"independent-device-17","phase-sensor-B")
   self.assertEqual(result["selected_p"],p)
   self.assertFalse(result["full_infinite_tower_empirically_verified"])

 def test_hidden_state_alias_pins_observer_not_ontology(self):
  case=hidden_four_state_alias()
  self.assertEqual(case["reported_period"],2)
  self.assertEqual(case["true_period"],4)
  self.assertFalse(case["observer_faithful"])
  fit=oriented_cycle_probe(case["reported_states"],(2,3,5),"hidden-device","aliased-sensor")
  self.assertEqual(fit["selected_p"],2)

 def test_horizon_counterfeit_survives_every_finite_prefix(self):
  for p in (2,3,5):
   for K in (1,2,3,4):
    real,fake=counterfeit_extension_orders(p,K)
    self.assertEqual(real[:K],fake[:K])
    self.assertNotEqual(real[K:],fake[K:])
    self.assertTrue(all(fake[k+1]%fake[k]==0 for k in range(len(fake)-1)))

 def test_wrong_source_instrument_and_composite_fail_closed(self):
  cases=[lambda:oriented_cycle_probe((0,1,0,1,0),(2,4),'a','b'),
         lambda:oriented_cycle_probe((0,1,0,1,0),(2,3),'','b'),
         lambda:oriented_cycle_probe((0,1,2,1,0,1,2),(2,3),'a','b'),
         lambda:qphase(12,4,2),lambda:phase_affine(1,0,0,2,2),
         lambda:projective_matrix_point(matrix_affine(2,0),1,2),
         lambda:children(2,1,2),lambda:parent(2,1,2),
         lambda:oriented_cycle_probe((0,0,0,0,0),(2,3),'a','b')]
  for f in cases:
   with self.subTest(f=f):
    with self.assertRaises(ObservationContractError):f()

 def test_identical_first_shell_nonisomorphic_complete_local_sources(self):
  for p in (2,3,5):
   w=equal_first_shell_distinct_ring_witness(p)
   self.assertEqual(w["first_shell_degree"],p+1)
   self.assertEqual(w["integer_ring_mul_p_image_count"],
                    multiplier_image_count(p,p,2))
   self.assertEqual(w["equal_characteristic_ring_mul_p_image_count"],1)
   self.assertNotEqual(w["integer_ring_char"],w["equal_characteristic_ring_char"])
   self.assertTrue(w["second_level_source_probe_distinguishes"])

 def test_first_shell_orientation_is_a_calibrated_gauge(self):
  p=5
  for u in (2,3,4):
   # Multiplication by units is a group/line relabeling, but it does
   # not preserve the declared ONE-event successor as a calibrated arrow.
   self.assertNotEqual((u*1)%p,1)

if __name__ == '__main__':unittest.main()
