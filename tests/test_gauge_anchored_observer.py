"""Exact rational controls for target-relative gauge pinning and source descent."""
import random, unittest
from fractions import Fraction as Q
from observational_succ.gauge_anchored_observer import (
 group_closure,orbit_partition,gauge_invariant,equivariant_anchor,relational_readout,
 diagonal_invariant,equivariant_transition,action_descends,xor_carrier,hidden_carrier,
 joint_model,validate_joint,joint_gauge_covariant,quotient_joint,filter_current,
 push_to_orbits,source_cost_invariant,expected_cost)

class GaugeAnchorTests(unittest.TestCase):
 def test_gauge_group_orbits(self):
  g,*_=xor_carrier()
  self.assertEqual(group_closure((g,),4),(tuple(range(4)),g))
  self.assertEqual(orbit_partition(4,(g,)),((0,3),(1,2)))
 def test_source_reference_transports_covariantly(self):
  g,a,rg,F,P,T=xor_carrier()
  self.assertTrue(equivariant_anchor(a,(g,),(rg,),2))
  self.assertTrue(diagonal_invariant(F,(g,),(rg,)))
  self.assertEqual(relational_readout(a,F),P)
  self.assertTrue(gauge_invariant(P,(g,)))
 def test_absolute_fixed_pin_spurious_report(self):
  g,a,rg,F,P,T=xor_carrier()
  absolute=(0,)*4
  self.assertFalse(equivariant_anchor(absolute,(g,),(rg,),2))
  self.assertFalse(gauge_invariant(relational_readout(absolute,F),(g,)))
  self.assertTrue(gauge_invariant(P,(g,)))
 def test_equivariant_but_informationally_empty_anchor(self):
  g,a,rg,F,P,T=xor_carrier()
  anchor=tuple(x>>1 for x in range(4))
  self.assertTrue(equivariant_anchor(anchor,(g,),(rg,),2))
  self.assertEqual(relational_readout(anchor,F),(0,0,0,0))
  self.assertNotEqual(P,(0,0,0,0))
 def test_gauge_physical_dynamics_distinction(self):
  g,a,rg,F,P,T=xor_carrier()
  self.assertTrue(equivariant_transition(T,(g,)))
  self.assertTrue(action_descends(P,T))
  self.assertEqual(tuple(P[T[x]] for x in range(4)),tuple(1-v for v in P))
  self.assertTrue(equivariant_transition(g,(g,)))
  self.assertEqual(tuple(P[g[x]] for x in range(4)),P)
 def test_source_action_equivariance_does_not_guarantee_observed_prediction(self):
  g,q,h,T=hidden_carrier()
  self.assertTrue(gauge_invariant(q,(g,)))
  self.assertTrue(gauge_invariant(h,(g,)))
  self.assertTrue(equivariant_transition(T,(g,)))
  self.assertFalse(action_descends(q,T))
  self.assertEqual(q[0],q[1])
  self.assertNotEqual(q[T[0]],q[T[1]])
 def test_gauge_nonobservability_not_fuckedfield_for_physical_target(self):
  g,a,rg,F,P,T=xor_carrier()
  for x in range(4):
   self.assertEqual(P[x],P[g[x]])
  raw=tuple(x>>1 for x in range(4))
  self.assertTrue(any(raw[x]!=raw[g[x]] for x in range(4)))
 def test_real_hidden_physical_target_nonidentifiable(self):
  g,q,h,T=hidden_carrier()
  self.assertEqual(q[0],q[1])
  self.assertNotEqual(h[0],h[1])
  self.assertTrue(gauge_invariant(h,(g,)))
 def test_source_joint_gauge_covariance(self):
  g,*_=xor_carrier();J=joint_model()
  self.assertTrue(validate_joint(J))
  self.assertTrue(joint_gauge_covariant(J,(g,)))
  for x in range(4):
   for xp in range(4):
    for o in (0,1):self.assertEqual(J[g[x]][g[xp]][o],J[x][xp][o])
 def test_raw_label_sensor_is_not_physical_gauge_readout(self):
  g,*_=xor_carrier();J=joint_model(raw_absolute=True)
  self.assertTrue(validate_joint(J))
  self.assertFalse(joint_gauge_covariant(J,(g,)))
  with self.assertRaises(ValueError):quotient_joint(J,(g,))
 def test_quotient_joint_source_law(self):
  g,*_=xor_carrier();J=joint_model()
  orbits,K=quotient_joint(J,(g,))
  self.assertEqual(len(orbits),2)
  self.assertTrue(validate_joint(K))
  # Gauge-related representatives give exactly the same pushed-forward law.
  for orb in orbits:
   for x in orb:
    for j,dst in enumerate(orbits):
     for o in (0,1):
      self.assertEqual(sum((J[x][z][o] for z in dst),Q(0)),K[orbits.index(orb)][j][o])
 def test_bayes_filter_commutes_with_orbit_quotient(self):
  g,*_=xor_carrier();J=joint_model();orbits,K=quotient_joint(J,(g,))
  rng=random.Random(19014)
  for _ in range(150):
   vals=[rng.randint(0,100) for _ in range(4)]; vals[0]+=1
   z=sum(vals);prior=tuple(Q(v,z) for v in vals)
   z0,p0=filter_current(prior,J,0)
   z1,p1=filter_current(push_to_orbits(prior,orbits),K,0)
   self.assertEqual(z0,z1)
   self.assertEqual(push_to_orbits(p0,orbits),p1)
 def test_gauge_invariant_prior_not_required_for_quotient_prediction(self):
  g,*_=xor_carrier();J=joint_model();orbits,K=quotient_joint(J,(g,))
  for x in range(4):
   prior=tuple(Q(int(i==x)) for i in range(4))
   za,pa=filter_current(prior,J,0)
   zb,pb=filter_current(push_to_orbits(prior,orbits),K,0)
   self.assertEqual(za,zb)
   self.assertEqual(push_to_orbits(pa,orbits),pb)
 def test_gauge_invariant_cost_factors_through_orbits(self):
  g,a,rg,F,P,T=xor_carrier()
  good=tuple(Q(2+P[x]) for x in range(4))
  bad=tuple(Q(2+(x>>1)) for x in range(4))
  self.assertTrue(source_cost_invariant(good,(g,)))
  self.assertFalse(source_cost_invariant(bad,(g,)))
  orbits=orbit_partition(4,(g,))
  reduced=tuple(good[o[0]] for o in orbits)
  for weights in ((1,3,4,2),(7,1,0,4)):
   prior=tuple(Q(v,sum(weights)) for v in weights)
   self.assertEqual(expected_cost(prior,good),expected_cost(push_to_orbits(prior,orbits),reduced))
 def test_gauge_orbit_map_has_no_equivariant_point_section(self):
  g,*_=xor_carrier()
  orbits=orbit_partition(4,(g,))
  self.assertTrue(all(g[x]!=x for x in range(4)))
  # A section of orbit quotient exists (choose 0,1), but no equivariant one:
  # the report orbit is G-fixed and a selected source state is not.
  self.assertEqual(len(orbits),2)
  self.assertTrue(all(o for o in orbits))
 def test_inequivalent_gauge_law_cannot_be_authenticated_by_lumping(self):
  g,*_=xor_carrier()
  bad=joint_model(raw_absolute=True)
  self.assertFalse(joint_gauge_covariant(bad,(g,)))
 def test_mutation_corrupts_source_transition_equivariance(self):
  g,a,rg,F,P,T=xor_carrier()
  # Uncalibrated absolute reset to s=0 (retains reference r) is not equivariant.
  reset=tuple(x&1 for x in range(4))
  self.assertFalse(equivariant_transition(reset,(g,)))

if __name__=='__main__':unittest.main(verbosity=2)
