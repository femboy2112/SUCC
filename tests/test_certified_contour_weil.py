"""Hostile exact rational contour certificates; no zeta roots as input."""
import json
import unittest
from fractions import Fraction as Q
from pathlib import Path
from observational_succ.certified_contour_weil import (
 C, ContourError, CertifiedAnalyticModel, poly, exact_winding, winding_any_ray,
 rectangle, certify_rectangle, shadow_interval_model, original_xi_model,
 centered_xi_model, verify_shadow_against_original, derivative_scaling_obstruction,
 zeta_zero_side_tail_constant, contour_weil_identity_note, reflected_fake_non_euler, fake_reflected_odd_negative_bound, _exp_upper, _gitblob
)

ROOT=Path(__file__).resolve().parents[1]
SHADOW=ROOT/'tests/fixtures/XI_PARENT_SOURCE_OUTER_INTERVALS.json'

class ExactRationalContour(unittest.TestCase):
 def test_complex_rational_operations(self):
  z=C(Q(3,2),Q(1,3));w=C(Q(2,7),-Q(1,4))
  self.assertEqual((z/w)*w,z)
  self.assertEqual(z.norm2(),Q(9,4)+Q(1,9))

 def test_original_authentic_receipt_blob_is_mandatory(self):
  with self.assertRaises((FileNotFoundError,ContourError)):
   original_xi_model(ROOT/'this_path_does_not_exist',1)
  self.assertNotEqual(_gitblob(b'fake'), '2657d92f15fcd77e2232f2cf305561a090ff28ce')

 def test_parent_theta_coefficients_validated_if_available(self):
  if not (ROOT/'research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json').exists():
   self.skipTest('Isolated development workspace: authentic source receipt exists in remote PR78 ancestry')
  x=verify_shadow_against_original(ROOT,SHADOW)
  self.assertTrue(x['all_21_theta_coefficients_enclosed'])
  self.assertTrue(x['b20_upper_authentic'])

 def test_authentic_original_xi_rectangle_if_available(self):
  if not (ROOT/'research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json').exists():
   self.skipTest('Needs original theta receipt from SUCC ancestor')
  m=original_xi_model(ROOT,3,13)
  cert=certify_rectangle(m,0,0,2,1,16)
  self.assertEqual(cert['count'],0)
  self.assertEqual(cert['source'],'xi(1/2+z)')

 def test_authentic_xi_disk_radius_7_5_if_available(self):
  if not (ROOT/'research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json').exists():
   self.skipTest('Needs original theta receipt from SUCC ancestor')
  m=original_xi_model(ROOT,Q(107,10),20)
  cert=certify_rectangle(m,0,0,Q(15,2),Q(15,2),2048)
  self.assertEqual(cert['count'],0)
  self.assertGreater(Q(cert['min_nonzero_margin']),0)

 def test_authentic_centered_xi_two_zeros_if_available(self):
  if not (ROOT/'research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json').exists():
   self.skipTest('Needs original theta receipt from SUCC ancestor')
  m=centered_xi_model(ROOT,Q(3,2),13)
  cert=certify_rectangle(m,0,0,1,1,16)
  self.assertEqual(cert['count'],2)
  self.assertEqual(cert['source'],'xi(1/2+z)-xi(1/2)')

 def test_constant_polynomial_zero_count(self):
  model=CertifiedAnalyticModel((C(1),),3,0,'toy','exact')
  self.assertEqual(certify_rectangle(model,0,0,1,1)['count'],0)

 def test_two_actual_polynomial_zeros(self):
  model=CertifiedAnalyticModel((C(0),C(0),C(1)),3,0,'toy','exact')
  self.assertEqual(certify_rectangle(model,0,0,1,1,32)['count'],2)

 def test_four_actual_polynomial_zeros(self):
  model=CertifiedAnalyticModel((C(0),C(0),C(0),C(0),C(1)),Q(3,2),0,'toy','exact')
  self.assertEqual(certify_rectangle(model,0,0,1,1,128)['count'],4)

 def test_shifted_polynomial_root_outside(self):
  model=CertifiedAnalyticModel((C(5),C(1)),3,0,'toy','exact')
  self.assertEqual(certify_rectangle(model,0,0,1,1)['count'],0)

 def test_poly_two_complex_roots(self):
  model=CertifiedAnalyticModel((C(1),C(0),C(1)),3,0,'toy','exact')
  self.assertEqual(certify_rectangle(model,0,0,2,2,64)['count'],2)

 def test_source_shadow_zero_count_proves_conditional_only(self):
  m=shadow_interval_model(SHADOW,3,13,False)
  c=certify_rectangle(m,0,0,2,1,32)
  self.assertEqual(c['count'],0)
  self.assertIn('source-conditional',c['source'])
  self.assertFalse(c['RH_proved'])

 def test_conditional_xi_disk_radius_7_5(self):
  m=shadow_interval_model(SHADOW,Q(107,10),20)
  cert=certify_rectangle(m,0,0,Q(15,2),Q(15,2),2048)
  self.assertEqual(cert['count'],0)
  self.assertGreater(Q(cert['min_nonzero_margin']),Q(1,1000))
  self.assertFalse(cert['RH_proved'])

 def test_source_shadow_two_centered_zeros(self):
  m=shadow_interval_model(SHADOW,Q(3,2),13,True)
  c=certify_rectangle(m,0,0,1,1,32)
  self.assertEqual(c['count'],2)
  self.assertLess(m.error,Q(1,1000))
  self.assertIn('source-conditional',c['source'])

 def test_zero_input_policy_and_overreach(self):
  model=shadow_interval_model(SHADOW,Q(3,2),13,True)
  with self.assertRaises(ContourError):certify_rectangle(model,0,0,2,1)
  with self.assertRaises(ContourError):shadow_interval_model(SHADOW,13,13,True)

 def test_no_free_tiny_contour_certificates(self):
  model=CertifiedAnalyticModel((C(0),C(1)),3,Q(1,3),'toy','uncertain')
  with self.assertRaises(ContourError):certify_rectangle(model,0,0,Q(1,5),Q(1,5))

 def test_fake_reflection_preserves_symmetry_but_creates_offline_zeros(self):
  m=shadow_interval_model(SHADOW,Q(3,2),13,False)
  fake=reflected_fake_non_euler(m)
  cert=certify_rectangle(fake,0,0,1,1,16)
  self.assertEqual(cert['count'],2)
  self.assertIn('MUTANT_nonEuler',cert['source'])
  self.assertGreater(Q(cert['min_nonzero_margin']),Q(1))
  # Factor 10*z^2-3/2 has z = ±sqrt(3/20), which is real and nonzero.
  self.assertGreater(Q(3,20),0)
  self.assertLess(Q(3,20),Q(1,4))

 def test_fake_source_never_authenticates_as_original(self):
  m=shadow_interval_model(SHADOW,Q(3,2),13)
  fake=reflected_fake_non_euler(m)
  self.assertNotEqual(fake.source_id,m.source_id)
  self.assertGreater(fake.error,m.error)
  self.assertEqual(certify_rectangle(m,0,0,1,1,16)['count'],0)
  self.assertEqual(certify_rectangle(fake,0,0,1,1,16)['count'],2)

 def test_mutant_real_offline_pair_has_strictly_negative_local_weil_form(self):
  d=fake_reflected_odd_negative_bound(Q(1))
  self.assertTrue(d['negative_certified_for_odd_test'])
  self.assertLess(Q(d['local_weil_pairing_strict_upper']),0)
  self.assertFalse(d['genuine_zeta_weil_sign_proved'])
  self.assertEqual(Q(d['synthetic_offline_zero_pair_squared_distance']),Q(3,20))

 def test_wrong_orientation_zero_side(self):
  verts=rectangle(0,0,1,1,16)
  vals=[poly((C(0),C(0),C(1)),z) for z in verts]
  self.assertEqual(winding_any_ray(vals)[0],2)
  self.assertEqual(winding_any_ray(list(reversed(vals)))[0],-2)

 def test_wrong_ray_and_zero_vertex_refused(self):
  with self.assertRaises(ContourError):exact_winding([C(1),C(-1),C(0,1)])
  with self.assertRaises(ContourError):exact_winding([C(0),C(1),C(0,1)])

 def test_rational_exponential_majorant(self):
  self.assertGreater(_exp_upper(1),Q(27,10))
  self.assertGreater(_exp_upper(Q(13**2,8)),Q(1))
  with self.assertRaises(ContourError):_exp_upper(61)

 def test_mutated_shadow_label_rejected(self):
  d=json.loads(SHADOW.read_text())
  d['upstream_git_blob_sha']='0'*40
  path=ROOT/'tests/fixtures/__bad_shadow.json'
  try:
   path.write_text(json.dumps(d))
   with self.assertRaises(ContourError):shadow_interval_model(path,2)
  finally:
   path.unlink(missing_ok=True)

 def test_weil_tail_explicit_rational_contract(self):
  for T in (4,8,100):
   obj=zeta_zero_side_tail_constant(Q(1,4),T)
   self.assertGreater(Q(obj['A_upper']),0)
   self.assertGreater(Q(obj['full_zero_side_tail_upper']),0)
  lo=zeta_zero_side_tail_constant(Q(1,4),4)
  hi=zeta_zero_side_tail_constant(Q(1,4),8)
  self.assertLess(Q(hi['full_zero_side_tail_upper']), Q(lo['full_zero_side_tail_upper']))

 def test_tail_not_uniform_on_H1(self):
  self.assertEqual(derivative_scaling_obstruction(1)['sixth_derivative_L1_factor'],1)
  self.assertEqual(derivative_scaling_obstruction(4)['sixth_derivative_L1_factor'],4**9)
  self.assertEqual(derivative_scaling_obstruction(10)['H1_seminorm_factor_squared'],1)

 def test_suzuki_comparison_keeps_signed_gate(self):
  x=contour_weil_identity_note()
  self.assertFalse(x['full_Weil_positive'])
  self.assertFalse(x['tail_sign_determined'])
  self.assertEqual(x['compact_test_space'],'C_c^infty(R)')

if __name__=='__main__':unittest.main()
