"""Exact rational 2nd/3rd source ensemble threshold-carry correlation controls.
These are not original s=0 orbit time-average certificates.
"""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

PATH=Path(__file__).resolve().parent/'paired_carry_correlations.py'
S=importlib.util.spec_from_file_location('paired_carry_correlations',PATH)
mod=importlib.util.module_from_spec(S);S.loader.exec_module(mod)

EXPECTED={
 (13,2,(0,1)):F(50149729331447295416131,70480824217391045683850625),
 (13,2,(0,2)):F(-251758391479289058179,5807125477878025260960000),
 (13,2,(0,1,2)):F(-296759809497508588801899580417307,8982338237361290144346710217761250000),
 (29,3,(0,1)):F(33149516431038967526261191614074337174294323,9420262788584763500958923328059511166327871280),
 (29,3,(0,2)):F(4759547009484291819639513924564837947623,579023476790219254853559017026878001821249600),
 (29,3,(0,1,2)):F(49176163851787576759728011849002024562841268852099277549821031831,287836511562998355428104756461536948211293450698501632395699661946800),
 (61,3,(0,1)):F(48921065655746569155643678678882416595480894976,65746375426872461577386495570950652324529485953125),
 (61,3,(0,2)):F(148538137307360182153440105605233071104890737733,3988068971143125802542362620853333703751647380700000),
 (61,3,(0,1,2)):F(2419075442997915688609656752123128570030678427817030351264674127893776489,83043056307503490598862020880094618099078643377535831731949770048362512500000),
}

class SourcePairTriple(unittest.TestCase):
 def test_01_one_time_mean_is_exactly_r(self):
  for n,m in ((13,2),(29,3),(61,3)):
   v,_,_=mod.integrate(n,m,(0,))
   self.assertEqual(v,0)

 def test_02_new_exact_pair_and_triple_holdouts(self):
  for (n,m,delays),expected in EXPECTED.items():
   v,dat,points=mod.integrate(n,m,delays)
   self.assertEqual(v,expected)
   self.assertGreater(points,1)
   self.assertTrue(all(0<t[2]<1 for t in dat))

 def test_03_pair_clock_decay_bound(self):
  for (n,m,ds),v in EXPECTED.items():
   if len(ds)==2:
    self.assertLessEqual(abs(v),F(1,3*16**(ds[1]-ds[0])))

 def test_04_third_pressure_has_both_signs(self):
  self.assertLess(EXPECTED[(13,2,(0,1,2))],0)
  self.assertGreater(EXPECTED[(29,3,(0,1,2))],0)
  self.assertGreater(EXPECTED[(61,3,(0,1,2))],0)

 def test_05_future_source_recurrence_resonance(self):
  for n,m in ((13,2),(29,3),(61,3)):
   B=16**m
   for d in (1,2):
    for y in (F(0),F(1,7),F(2,17),F(5,9)):
     shifted=(16**d*y+B*mod.delay(n,d))%1
     explicit=y
     for j in range(1,d+1):
      explicit=(16*explicit+B*mod.r(n+j))%1
     self.assertEqual(shifted,explicit)

if __name__=='__main__':unittest.main()
