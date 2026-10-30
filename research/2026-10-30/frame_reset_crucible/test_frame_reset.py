"""Exact and adversarial tests for the base16 normal-digit calibration lab."""
import unittest
from fractions import Fraction as F
from collections import Counter
from frame_reset import (
    stage_info,stoneham_residue,complete_stage,next_pulse_error_bound,
    actual_tail_partial,enlarged_arc_count, certified_hit_upper,
    uniform_hotspot_bound,stage_character_formula,stage_fourier_zero,
    stoneham_prefix,champernowne_prefix,cylinder_frequency,
    frame_reset_table,chosen_digit_zero_ratio,debruijn_16_order2,
    cycle_word_counts,conditional_next_digit_on_cycle)

class StonehamConductor(unittest.TestCase):
    def test_stage_units_and_exact_sixfold_traversal(self):
        for p in range(1,7):
            q=3**p
            seq=complete_stage(p)
            counts=Counter(seq)
            self.assertEqual(len(seq),2*q)
            self.assertEqual(len(counts),q//3)
            self.assertEqual(set(counts),set(range(1,q,3)))
            self.assertEqual(set(counts.values()),{6})

    def test_multiplicative_generator_order(self):
        for p in range(1,8):
            q=3**p
            self.assertEqual(pow(16,3**(p-1),q),1)
            if p>1:self.assertNotEqual(pow(16,3**(p-2),q),1)

    def test_surrogate_recursion_across_pulse_births(self):
        for n in range(4,500):
            a,q=stoneham_residue(n)
            pprev,qprev=stoneham_residue(n-1)
            pulse=F(1,3**stage_info(n)[0]) if n==stage_info(n)[1] else F(0)
            self.assertEqual(F(a,q),(16*F(pprev,qprev)+pulse)%1)

    def test_exact_tail_bounded_on_each_stage(self):
        for p in range(1,5):
            for n in (3**p,3**p+1,(3**p+3**(p+1))//2,3**(p+1)-1):
                d=actual_tail_partial(n,p+3)
                self.assertGreater(d,0)
                self.assertLess(d,next_pulse_error_bound(p))

    def test_complete_root_character_exact_zero(self):
        for p in range(1,6):
            q=3**p
            for h in (1,2,3,5,7,9,27,81,3**(p-1)):
                residues=Counter(complete_stage(p))
                magnitude,phase,mod=stage_character_formula(p,h)
                self.assertEqual(mod,q)
                self.assertEqual(magnitude==0,stage_fourier_zero(p,h))
                if magnitude==0:
                    for a in range(1,q,3):
                        self.assertEqual(residues[a],6)
                    # Root-of-unity sum of cosets 1+3Z mod3^p vanishes unless 3^(p-1)|h.
                    self.assertNotEqual(h% (3**(p-1)),0)
                else:
                    self.assertEqual(magnitude,2*q)

    def test_certified_interval_count_uniform_hotspot_upper(self):
        # The bound concerns the true infinite Stoneham orbit, via a rigorous surrogate enclosure.
        intervals=[(F(0),F(1,100)),(F(1,3),F(1,200)),(F(3,10),F(1,12)),
                   (F(9,10),F(1,4)),(F(7,11),F(2,3))]
        for N in (9,27,81,243,500,729):
            for start,length in intervals:
                self.assertLessEqual(certified_hit_upper(N,start,length),uniform_hotspot_bound(N,length))

    def test_certified_prefix(self):
        digits=stoneham_prefix(300,k=6)
        self.assertEqual(len(digits),300)
        self.assertEqual(digits[:6],(0,0,0,5,5,5))
        self.assertEqual(len(frame_reset_table(digits,(5,))),16)

class AdversarialChoice(unittest.TestCase):
    def test_debruijn_is_perfect_two_digit_but_nonnormal(self):
        seq=debruijn_16_order2()
        self.assertEqual(len(seq),256)
        self.assertEqual(len(cycle_word_counts(seq,2)),256)
        self.assertEqual(set(cycle_word_counts(seq,2).values()),{1})
        self.assertEqual(set(cycle_word_counts(seq,1).values()),{16})
        for d in range(16):
            self.assertEqual(conditional_next_digit_on_cycle(seq,(d,)),(1,)*16)
        # 4096 triples possible, but one period has only 256 positions.
        self.assertLessEqual(len(cycle_word_counts(seq,3)),256)

    def test_biased_product_measure_is_also_reset_fixed_point(self):
        p=(F(1,2),)+(F(1,30),)*15
        self.assertEqual(sum(p),1)
        self.assertNotEqual(p[0],F(1,16))
        # P(word followed by d)/P(word)=p_d under an IID product law.
        for word in ((0,),(1,0),(9,7,5)):
            base=F(1)
            for k in word:base*=p[k]
            self.assertGreater(base,0)
            for d in range(16):self.assertEqual((base*p[d])/base,p[d])

    def test_computable_normal_choice_can_select_zero_only(self):
        seq=champernowne_prefix(4096)
        selected,zeros=chosen_digit_zero_ratio(seq)
        self.assertGreater(selected,0)
        self.assertEqual(selected,zeros)
        self.assertLess(selected,len(seq))
        # This choice uses the public generating algorithm, not a random sampler.

    def test_normal_finite_empirical_frames_have_bias(self):
        for seq in (champernowne_prefix(4096), stoneham_prefix(400,k=6)):
            c,total=cylinder_frequency(seq,(0,))
            self.assertGreater(total,0)
            self.assertGreater(c,0)
            self.assertNotEqual(F(c,total),F(1,16))

    def test_non_normal_fixed_point_all_fives(self):
        seq=(5,)*512
        self.assertEqual(frame_reset_table(seq,(5,)),tuple(511 if j==5 else 0 for j in range(16)))
        self.assertEqual(frame_reset_table(seq,(0,)),(0,)*16)

if __name__=='__main__': unittest.main()

class FrameResetGeometry(unittest.TestCase):
    def test_exact_Haar_recenter_for_any_word(self):
        from frame_reset import lebesgue_frame_reset_mass,cylinder_interval
        for word in ((0,),(5,),(15,),(1,0),(0,5,9),(15,15,0,2)):
            a,b=cylinder_interval(word)
            self.assertEqual(b-a,F(1,16**len(word)))
            for low,high in ((F(0),F(1)),(F(1,11),F(2,7)),(F(3,4),F(7,8))):
                joint,marginal=lebesgue_frame_reset_mass(word,low,high)
                self.assertEqual(joint/marginal,high-low)
    def test_exact_BBP_rational_transport_and_denominator_variation(self):
        from frame_reset import bbp_selected,bbp_forcing,bbp_tail_bound
        u=F(0)
        denoms=[]
        for n in range(1,28):
            u=16*u+bbp_forcing(n)
            self.assertEqual(u,bbp_selected(n))
            self.assertEqual(u.denominator%2,1)
            self.assertGreater(bbp_tail_bound(n),0)
            denoms.append(u.denominator)
        self.assertGreater(len(set(denoms)),23) # no single small conductor on this sample

class MatchedExceptionalPrimeConductors(unittest.TestCase):
    def test_c3_and_c5_exact_unit_subgroup_orbits(self):
        from frame_reset import conductor_complete_stage
        for c,pmax in ((3,5),(5,4)):
            for p in range(1,pmax+1):
                q=c**p
                visits=Counter(conductor_complete_stage(p,c))
                self.assertEqual(set(visits),set(range(1,q,c)))
                self.assertEqual(set(visits.values()),{c*(c-1)})
                self.assertEqual(len(visits),c**(p-1))
    def test_c3_and_c5_LTE_orders(self):
        for c in (3,5):
            for p in range(1,7):
                q=c**p
                self.assertEqual(pow(16,c**(p-1),q),1)
                if p>1:self.assertNotEqual(pow(16,c**(p-2),q),1)
    def test_c3_and_c5_finite_hotspot_interval_certificates(self):
        from frame_reset import conductor_hotspot_bound,conductor_certified_upper
        arcs=((F(0),F(1,32)),(F(1,3),F(1,20)),(F(8,9),F(1,5)))
        for c,ns in ((3,(10,50,120,250,730)),(5,(10,100,626,1000))):
            for N in ns:
                for start,L in arcs:
                    self.assertLessEqual(conductor_certified_upper(N,start,L,c),
                                         conductor_hotspot_bound(N,L,c))
    def test_unit_vs_nonunit_source_prime_obstruction(self):
        from math import gcd
        self.assertEqual([c for c in (2,3,5) if gcd(16,c)==1],[3,5])
        self.assertEqual(16-1,3*5)
        self.assertEqual(pow(16,1,2),0)
        self.assertEqual(pow(16,1,3),1)
        self.assertEqual(pow(16,1,5),1)

class NonunitCountermodel(unittest.TestCase):
    def test_c2_exact_sparse_hex_positions_and_zero_density(self):
        from frame_reset import nonunit_two_hex_pulses,stoneham_general_prefix
        pulses=nonunit_two_hex_pulses(9)
        self.assertEqual(pulses[:5],((3,8),(5,4),(9,2),(17,1),(34,8)))
        self.assertEqual(len({pos for pos,_ in pulses}),len(pulses))
        digits=stoneham_general_prefix(600,2,11)
        self.assertEqual(tuple((i,d) for i,d in enumerate(digits,1) if d!=0),
                         tuple((i,d) for i,d in nonunit_two_hex_pulses(11) if i<=600))
        self.assertLess(sum(d>0 for d in digits),14)

class NaiveSourceTransferFalsifier(unittest.TestCase):
    def test_bbp_phases_are_not_stoneham_sixfold_cells(self):
        # Same modulus-grid *bin* is not the source-derived Stoneham residue orbit.
        # This is a finite counterexample to naive literal conductor transfer,
        # not a proof of nonuniformity of pi.
        from frame_reset import bbp_forcing
        from collections import Counter
        u=F(0)
        bins={}
        for n in range(1,126):
            u=16*u+bbp_forcing(n)
            for c,p in ((3,2),(3,3),(5,2)):
                if c**p<=n<c**(p+1):
                    q=c**(p-1)
                    cell=((u.numerator%u.denominator)*q)//u.denominator
                    bins.setdefault((c,p),Counter())[cell]+=1
        self.assertEqual(tuple(bins[(3,2)][j] for j in range(3)),(9,7,2))
        self.assertGreater(max(bins[(3,3)].values()),6)
        self.assertGreater(max(bins[(5,2)].values()),20)
