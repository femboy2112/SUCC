"""Finite exact controls for the source reassembly; no infinite-limit certification."""
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ import chiral_target_descent as d
from observational_succ import rank_two_chiral_towers as parent


def independent_source(n, plus=True):
    if plus:
        return (Q(4,8*n-7)+Q(1,4*n-3)-Q(1,4*(2*n-1))
                -Q(1,8*n-3)-Q(1,4*(4*n-1))+Q(1,32*n))
    return -Q(1,4*n-3)-Q(1,4*(2*n-1))-Q(1,4*(4*n-1))-Q(1,32*n)


def tail_enclosure(n, plus=True, terms=12):
    # Different pole representation from production's matrix readout.
    partial=sum((independent_source(n+j,plus)/16**j for j in range(1,terms+1)),Q(0))
    err=abs(independent_source(n+terms+1,plus))/(15*16**terms)
    return (partial,partial+err) if plus else (partial-err,partial)


class ChiralSourceGauge(unittest.TestCase):
    def test_original_source_independent_poles(self):
        for n in (1,2,3,17,79,127,1024,65537):
            a,b=independent_source(n),independent_source(n,False)
            self.assertEqual(a,parent.source_moment(n,channel='even'))
            self.assertEqual(b,parent.source_moment(n,channel='odd'))
            self.assertEqual(a+b,parent.authentic_four_poles(n))

    def test_exact_endpoint_kernel_split(self):
        for den in (1,2,7,19,31):
            for num in range(den+1):
                t=Q(num,den)
                rp,rm=d.residual_kernel(t,'plus'),d.residual_kernel(t,'minus')
                self.assertEqual(d.tail_kernel(t,'plus'),Q(1,4)+rp)
                self.assertEqual(d.tail_kernel(t,'minus'),-Q(1,4)+rm)
                self.assertGreaterEqual(rp,0);self.assertGreaterEqual(rm,0)
                self.assertEqual(rp+rm,(1-t)/((2-t*t)*(t*t-2*t+2)))
                self.assertLessEqual(rp,t*(1-t)/4)
                self.assertLessEqual(rm,3*(1-t)/4)

    def test_remainder_tail_bounds_with_independent_oracle(self):
        for n in (1,2,7,19,127,16384):
            a=d.gauge(n)
            tp,tm=tail_enclosure(n),tail_enclosure(n,False)
            bp,bm=d.residual_bounds(n)
            self.assertGreater(tp[0]-a,0)
            self.assertLess(tp[1]-a,bp)
            self.assertGreater(tm[0]+a,0)
            self.assertLess(tm[1]+a,bm)

    def test_gauge_preserves_target_and_initial_shift(self):
        for n,(a,b) in enumerate(d.phase_history(48),1):
            x,y=d.corrected_pair(n,a,b)
            self.assertEqual(x+y,a+b)
            self.assertEqual((x+y)%1,parent.original_zero_seed_prefix(n)%1)
        self.assertEqual(d.corrected_pair(0,Q(0),Q(0)),(Q(1,4),-Q(1,4)))

    def test_direct_phases_equal_unwrapped(self):
        for n,(a,b) in enumerate(d.phase_history(32),1):
            x,y=parent.chiral_zero_seed_states(n)
            self.assertEqual((a,b),(x%1,y%1))

    def test_tail_counterterm_sign_mutation_is_detected(self):
        n=37;lo,hi=tail_enclosure(n)
        corrected=hi-d.gauge(n)
        wrong=lo+d.gauge(n)
        self.assertGreater(wrong,10*corrected)
        # Wrong one-sided sign changes the total observable.
        self.assertNotEqual((2*d.gauge(n))%1,Q(0))


class TwoClockFilters(unittest.TestCase):
    def test_all_four_filter_classes(self):
        # Raw defect residue at 1 and ln(2) carrier coefficient at 16 differ.
        examples=[((1,),(1,),0,0),((1,),(0,),1,2),
                  ((1,),(0,1),0,-30),((-16,1),(0,),-15,0),
                  ((17,-17,1),(1,),0,0)]
        for p,m,d1,logc in examples:
            c=d.classify_filter(p,m)
            self.assertEqual(c.endpoint_residue,d1)
            self.assertEqual(c.log2_coefficient,logc)
            self.assertEqual(c.neutral_quotient is not None,d1==0 and logc==0)
        self.assertEqual(d.classify_filter((17,-17,1),(1,)).neutral_quotient,(1,))

    def test_exact_two_root_division_and_holdouts(self):
        for a in range(-3,4):
            for b in range(-3,4):
                # D=(16-17X+X^2)*(a+bX)
                p=(16*a,-17*a+16*b,a-17*b,b)
                q=d.classify_filter(p,(0,)).neutral_quotient
                self.assertIsNotNone(q)
                for x in (-3,0,1,3,16,17):
                    self.assertEqual(d.evaluate(p,x),(x-1)*(x-16)*d.evaluate(q,x))

    def test_filter_collapse_exact_original_history(self):
        up=[Q(0)];um=[Q(0)]
        for n in range(1,45):
            up.append(16*up[-1]+independent_source(n))
            um.append(16*um[-1]+independent_source(n,False))
        # Nontrivial chiral filter plus original minus lane.
        for n in (1,2,9,32):
            actual=17*up[n]-17*up[n+1]+up[n+2]+um[n]
            expected=up[n]+um[n]+independent_source(n+2)-independent_source(n+1)
            self.assertEqual(actual,expected)

    def test_neutral_shift_budget(self):
        self.assertEqual(d.harmonic_shift_cost(1),Q(1,36))
        self.assertEqual(d.neutral_budget((1,),(0,1)),Q(2,15)+Q(1,36))
        with self.assertRaises(ValueError):d.neutral_budget((-16,1),(0,))
        for shift in (0,1,2,17,64):
            partial=sum((d.gauge(n)-d.gauge(n+shift) for n in range(1,100)),Q(0))
            self.assertGreaterEqual(partial,0)
            self.assertLessEqual(partial,d.harmonic_shift_cost(shift))

    def test_endpoint_annihilation_is_not_source_annihilation(self):
        c=d.classify_filter((-1,1),(0,))
        self.assertEqual(c.endpoint_residue,0)
        self.assertEqual(c.log2_coefficient,30)
        c=d.classify_filter((-16,1),(0,))
        self.assertEqual(c.log2_coefficient,0)
        self.assertNotEqual(c.endpoint_residue,0)


class QuotientAndSpectralCertificate(unittest.TestCase):
    def test_haar_and_finite_gauge_alias(self):
        self.assertEqual(d.quotient_multiplier(3,3),1)
        self.assertEqual(d.quotient_multiplier(3,4),0)
        self.assertEqual(d.quotient_multiplier(3,19),0)
        self.assertEqual(d.quotient_multiplier(3,19,16),1)

    def test_exact_quotient_gauge_character(self):
        for a,b in d.phase_history(24):
            for t in (Q(1,7),Q(-11,19),Q(5,16)):
                self.assertEqual(((a+t)+(b-t))%1,(a+b)%1)
        # Declared product-distribution assumption would lose this countermodel.
        q=7;left=[Q(j,q) for j in range(q)];right=[-x for x in left]
        self.assertEqual({x%1 for x in left},{x%1 for x in right})
        self.assertEqual([(a+b)%1 for a,b in zip(left,right)],[Q(0)]*q)

    def test_exact_quadrantal_trig_enclosures(self):
        for turn,c,s in [(0,1,0),(Q(1,4),0,1),(Q(1,2),-1,0),(Q(3,4),0,-1)]:
            bc,bs=d.trig_turn(turn)
            self.assertLessEqual(bc.low,c);self.assertGreaterEqual(bc.high,c)
            self.assertLessEqual(bs.low,s);self.assertGreaterEqual(bs.high,s)
            self.assertLess(bc.high-bc.low,Q(1,10**18))
        with self.assertRaises(ValueError):d.trig_turn(0.25)

    def test_large_exact_phase_reduction(self):
        x=Q(16**200*479+3,479)
        self.assertEqual(d.trig_turn(x),d.trig_turn(x%1))

    def test_coherent_energy_and_spectral_remainder(self):
        h=12;c=d.poisson_energy([Q(0)]*7,h)
        known=2-Q(2,2**h)
        self.assertLessEqual(c.partial.low,known)
        self.assertGreaterEqual(c.partial.high,known)
        self.assertLessEqual(c.full.low,2);self.assertEqual(c.full.high,2)
        self.assertEqual(c.spectral_tail,Q(2,2**h))

    def test_root_grid_closed_form_and_hidden_seventeenth_mode(self):
        for q,H in ((3,12),(5,15),(17,17)):
            c=d.poisson_energy([Q(j,q) for j in range(q)],H)
            exact_partial=sum((Q(2,2**h) for h in range(1,H+1) if h%q==0),Q(0))
            exact_full=Q(2,2**q-1)
            self.assertLessEqual(c.partial.low,exact_partial)
            self.assertGreaterEqual(c.partial.high,exact_partial)
            self.assertLessEqual(c.full.low,exact_full)
            self.assertGreaterEqual(c.full.high,exact_full)
            if q==17:
                self.assertGreater(c.partial.low,0)
                c16=d.poisson_energy([Q(j,q) for j in range(q)],16)
                self.assertLess(c16.partial.high,Q(1,10**18))
                self.assertGreater(c16.spectral_tail,exact_full)

    def test_anticorrelated_marginals_fail_target(self):
        q=7
        marginal=d.poisson_energy([Q(j,q) for j in range(q)],14)
        total=d.poisson_energy([Q(0)]*q,14)
        self.assertLess(marginal.full.high,Q(1,32))
        self.assertGreater(total.full.low,Q(19,10))

    def test_original_finite_energy_and_control_separate(self):
        data=[(a+b)%1 for a,b in d.phase_history(32)]
        true=d.poisson_energy(data,10)
        fake=d.poisson_energy(d.rational_control(32),10)
        self.assertLess(true.full.high,Q(1,2))
        self.assertGreater(fake.full.low,Q(19,10))
        self.assertLess(true.partial.high-true.partial.low,Q(1,10**16))

    def test_signed_kernel_range_and_zero(self):
        for x in (Q(0),Q(1,6),Q(1,4),Q(1,2),Q(19,31)):
            b=d.poisson_kernel(x)
            self.assertGreaterEqual(b.low,-Q(2,3));self.assertLessEqual(b.high,2)
        b=d.poisson_kernel(Q(0))
        self.assertGreaterEqual(b.high,2)
        b=d.poisson_kernel(Q(1,2))
        self.assertLessEqual(b.low,-Q(2,3))

    def test_fresh_step_contraction_refuted_at_actual_step_two(self):
        xs=[sum(p)%1 for p in d.phase_history(3)]
        energy=d.poisson_energy(xs[:2],16).full
        fresh=d.innovation(xs[:2],xs[2])
        self.assertGreater(fresh.low-energy.high/2,Q(3,5))

    def test_innovation_recursion_enclosures(self):
        xs=[sum(p)%1 for p in d.phase_history(9)]
        for n in (1,2,7,8):
            old=d.poisson_energy(xs[:n],20).full
            new=d.poisson_energy(xs[:n+1],20).full
            j=d.innovation(xs[:n],xs[n])
            low=(n*n*old.low+2*n*j.low+2)/(n+1)**2
            high=(n*n*old.high+2*n*j.high+2)/(n+1)**2
            self.assertLessEqual(low,new.high);self.assertLessEqual(new.low,high)

    def test_invalid_inputs(self):
        for p in ((),(True,),(Q(1),)):
            with self.assertRaises(ValueError):d.classify_filter(p,(1,))
        for bad in (-1,True):
            with self.assertRaises(ValueError):d.gauge(bad)
        with self.assertRaises(ValueError):d.poisson_energy([],8)
        with self.assertRaises(ValueError):d.poisson_energy([Q(0)],0)
        with self.assertRaises(ValueError):d.tail_kernel(Q(1),'false')


if __name__=='__main__':unittest.main()
