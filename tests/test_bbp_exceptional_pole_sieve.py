"""Independent exact rational reduction, exceptional period and CRT holdouts."""
import unittest
from fractions import Fraction as Q
from observational_succ.succ_internal_matrix_walk import authentic_r
from observational_succ.bbp_exceptional_pole_sieve import prime_period,hit_classes,forcing_denominator_depth,occupancy,combined_sieve,denominator_depth_transition,source_depth_drops

class ExceptionalPoleSieve(unittest.TestCase):
 def test_original_four_poles_rational_reduction(self):
  for n in range(1,200):
   self.assertEqual(authentic_r(n),Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
 def test_all_exceptional_classes_agree_direct_source(self):
  for p in (3,5,7,11,13,17):
   m=prime_period(p);hits=set(hit_classes(p))
   for n in range(1,600):
    self.assertEqual(n%m in hits,authentic_r(n).denominator%p==0,(n,p))
   self.assertEqual(occupancy(3*m,p)['hits'],3*len(hits))
  self.assertEqual(len(hit_classes(3)),8)
  self.assertEqual(len(hit_classes(5)),14)
  self.assertNotIn(8,hit_classes(3))
  self.assertNotIn(24,hit_classes(5))
 def test_full_prime_power_depth_formula(self):
  for p in (3,5,7,11,13,17,19,23,31,41):
   for n in range(1,1200):
    den=authentic_r(n).denominator
    order=0
    while den%p==0:
     den//=p;order+=1
    self.assertEqual(forcing_denominator_depth(n,p),order,(n,p))
  self.assertEqual(forcing_denominator_depth(8,3),0)
  self.assertEqual(forcing_denominator_depth(24,5),0)

 def test_crt_with_exceptional_and_generic_channels(self):
  for P in ((3,),(5,),(3,5),(3,5,7),(3,5,7,11)):
   M=1;safe=1
   for p in P:
    M*=prime_period(p);safe*=prime_period(p)-len(hit_classes(p))
   for N in (1,32,100,225,M,M+1):
    receipt=combined_sieve(N,P)
    self.assertEqual(receipt['survivors_per_period'],safe)
    self.assertEqual(receipt['safe']+receipt['deleted'],N)
    if N<=256:
     self.assertEqual(receipt['safe'],sum(all(authentic_r(n).denominator%p for p in P)
                                           for n in range(1,N+1)))
  self.assertEqual(combined_sieve(225,(3,5))['safe'],11)
  self.assertEqual(combined_sieve(225,(3,5))['deleted'],214)
 def test_ultrametric_time_ties_are_source_distinguishers(self):
  authentic=source_depth_drops(100,(3,5,7,11,13))
  self.assertIn((6,3,2,1),authentic['drops'])
  self.assertIn((51,3,4,3),authentic['drops'])
  self.assertIn((25,7,2,1),authentic['drops'])
  self.assertIn((20,13,1,0),authentic['drops'])
  u=Q(0);conductor=1;locked_drops=[]
  from math import lcm
  for n in range(1,101):
   q=lcm(conductor,authentic_r(n).denominator)
   forced=Q(16,conductor)-Q(1,q)
   for p in (3,5,7,11,13):
    event=denominator_depth_transition(u,forced,p)
    if event['depth_drop']: locked_drops.append((n,p))
   u=16*u+forced;conductor=q
  self.assertEqual(locked_drops,[])

 def test_rejections(self):
  for p in (2,4,True,103):
   with self.assertRaises(ValueError):hit_classes(p)
  with self.assertRaises(ValueError):combined_sieve(30,(5,3))
  with self.assertRaises(ValueError):occupancy(0,3)

if __name__=='__main__':unittest.main()
