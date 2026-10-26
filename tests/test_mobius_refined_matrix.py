"""Independent finite holdouts for exact Mobius-refined source-labelled Grams."""
import unittest
from fractions import Fraction as Q
from math import lcm

from observational_succ.succ_internal_matrix_walk import PhasePoly,authentic_r
from observational_succ.mobius_refined_matrix import (
    SOURCE,Trace,authentic,from_forcing,valuation,label,build,coarsen,
    invert_atom,moment,energies,variance,cross_interference,fejer,
    conditioned_innovation,pole_classes,pole_count,pole_crt_sieve,
)


class MobiusRefinedMatrixTests(unittest.TestCase):
    def test_zero_anchor_source_guard_carries(self):
        t=authentic(16)
        self.assertTrue(t.validate())
        self.assertTrue(t.authenticated)
        self.assertEqual(t.points[0].state,Q(47,15))
        self.assertEqual(t.points[0].carry,3)
        self.assertTrue(all(pt.forcing==authentic_r(pt.n) for pt in t.points))
        z=from_forcing((Q(0),)*16)
        self.assertFalse(z.authenticated)
        self.assertFalse(Trace(z.points,SOURCE,True).validate())
        with self.assertRaises(ValueError):
            from_forcing((Q(0),),SOURCE)

    def test_commuting_width_primes_depth_and_time_rank_one(self):
        t=authentic(14)
        fine=build(t,5,(3,5),2)
        for H,P,k in ((2,(),0),(3,(3,),1),(3,(5,),2),
                      (4,(3,5),1),(5,(3,5),2)):
            s=build(t,H,P,k)
            self.assertEqual(coarsen(fine,H,P,k),s)
            self.assertEqual(s.total(),build(t,H,(),0).total())
            self.assertEqual(sum(s.counts.values()),14)
        for n in range(1,11):
            a=build(t.prefix(n),3,(3,5),1)
            b=build(t.prefix(n+1),3,(3,5),1)
            target=label(t.points[n],(3,5),1)
            zz=tuple(tuple(PhasePoly.zero() for _ in range(3)) for _ in range(3))
            for atom in set(a.blocks)|set(b.blocks):
                for i in range(3):
                    for j in range(3):
                        delta=b.blocks.get(atom,zz)[i][j]-a.blocks.get(atom,zz)[i][j]
                        expected=(PhasePoly.monomial((i-j)*t.points[n].state)
                                  if atom==target else PhasePoly.zero())
                        self.assertEqual(delta,expected)

    def test_mobius_exact_atoms_hermiticity_and_diagonal(self):
        for t in (authentic(13),from_forcing((Q(0),)*13)):
            for P,k in (((3,5),1),((3,),2),((5,),2),((),0)):
                s=build(t,3,P,k)
                for a,B in s.blocks.items():
                    self.assertEqual(invert_atom(s,a),B)
                    self.assertEqual(B[0][0],PhasePoly.monomial(0,s.counts[a]))
                    self.assertEqual(B[1][0].star(),B[0][1])

    def test_anova_monotone_and_selected_cross_interference(self):
        t=authentic(16)
        fine=build(t,3,(3,5),2)
        coarse=coarsen(fine,2,(3,),1)
        g0,e0=energies(coarse,1)
        g1,e1=energies(fine,1)
        self.assertEqual(g0,g1)
        v=variance(fine,coarse,1)
        self.assertEqual(e1-e0,v)
        self.assertGreaterEqual(v.evaluation(70).real,-1e-30)
        z=sum((B[1][0] for B in fine.blocks.values()),PhasePoly.zero())
        diagonal=sum((B[1][0]*B[1][0].star() for B in fine.blocks.values()),
                     PhasePoly.zero())
        self.assertEqual(cross_interference(fine,1)+diagonal,z*z.star())
        self.assertEqual(g1,z*z.star()/16)

    def test_conditioned_fejer_is_direct_pole_source(self):
        for t in (authentic(12),from_forcing((Q(0),)*12)):
            for H,P,k in ((2,(),0),(3,(3,5),1),(4,(3,5),2)):
                q,cells=conditioned_innovation(t,H,P,k)
                direct=sum((fejer(t.points[-1].state-v.state,H)
                     for v in t.points[:-1]),PhasePoly.zero())/11
                self.assertEqual(q,direct)
                self.assertEqual(q.star(),q)
                self.assertTrue(cells)
        self.assertEqual(conditioned_innovation(from_forcing((Q(0),)*8),
              3,(3,5),2)[0],PhasePoly.monomial(0,9))

    def test_exceptional_three_five_are_not_generic_poles(self):
        self.assertEqual(valuation(authentic_r(2).denominator,3),2)
        self.assertEqual(valuation(authentic_r(8).denominator,3),0)
        self.assertEqual(valuation(authentic_r(4).denominator,5),2)
        self.assertEqual(valuation(authentic_r(24).denominator,5),0)
        for p in (7,11,13,17,19,23,31):
            self.assertEqual(len(pole_classes(p)),4)
            for N in (1,12,36,67,128,256):
                count,error,_=pole_count(N,p)
                self.assertLessEqual(abs(error),4)
                if N<=128:
                    self.assertEqual(count,sum(authentic_r(n).denominator%p==0
                                               for n in range(1,N+1)))
            self.assertEqual(pole_count(3*p,p)[0],12)

    def test_exact_crt_counts_not_phase_independence(self):
        for P in ((7,),(7,11),(7,11,13)):
            M=1;per=1
            for p in P: M*=p;per*=p-4
            for N in (1,12,64,M,M+3):
                c=pole_crt_sieve(N,P)
                self.assertEqual(c["survivors_per_period"],per)
                self.assertEqual(c["survivors"]+c["deleted"],N)
                if N<=128:
                    self.assertEqual(c["survivors"],sum(all(
                        authentic_r(n).denominator%p for p in P)
                        for n in range(1,N+1)))
        with self.assertRaises(ValueError):
            pole_crt_sieve(30,(3,7))

    def test_hostile_conductor_compatible_forcing_rejects_psd_normality(self):
        N=32
        q=1;forces=[]
        for n in range(1,N+1):
            next_q=lcm(q,authentic_r(n).denominator)
            forces.append(Q(16,q)-Q(1,next_q))
            q=next_q
        fake=from_forcing(tuple(forces),"CONTROL:locked-conductor")
        self.assertTrue(all(p.forcing>0 for p in fake.points))
        self.assertEqual(fake.points[-1].state,Q(16**N)-Q(1,q))
        for t in (authentic(N),fake,from_forcing((Q(0),)*N)):
            s=build(t,3,(3,5),1)
            self.assertTrue(all(invert_atom(s,a)==B for a,B in s.blocks.items()))
            self.assertEqual(coarsen(s,3,(),0),build(t,3,(),0))
        authentic_global=energies(build(authentic(N),3,(3,5),1),1)[0]
        fake_global=energies(build(fake,3,(3,5),1),1)[0]
        self.assertLess(authentic_global.evaluation(65).real,10)
        self.assertGreater(fake_global.evaluation(65).real,30)
        self.assertNotEqual(authentic_global,fake_global)
        self.assertNotEqual(fejer(Q(1,2),2),PhasePoly.zero())
        self.assertLess(abs(fejer(Q(1,2),2).evaluation(65)),1e-50)

    def test_full_factorial_marginals_and_cofinal_singletons(self):
        # All 2 x 4 x 3 cells: source, prime subset, valuation precision.
        for t in (authentic(16),from_forcing((Q(0),)*16)):
            for P in ((),(3,),(5,),(3,5)):
                for k in (0,1,2):
                    s=build(t,3,P,k)
                    self.assertEqual(coarsen(s,3,(),0),build(t,3,(),0))
                    self.assertTrue(all(invert_atom(s,a)==B for a,B in s.blocks.items()))
        for t in (authentic(32),from_forcing((Q(0),)*32)):
            # For fixed N, p^k>N makes all residues unique. The positive
            # conditional-energy upper bound becomes the trivial N.
            s=build(t,3,(3,),4)
            self.assertEqual(len(s.blocks),32)
            self.assertEqual(energies(s,1)[1],PhasePoly.monomial(0,32))


if __name__=="__main__":
    unittest.main()
