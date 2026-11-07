import unittest, math
from fractions import Fraction as F
from golden_aperture import *

class GoldenMath(unittest.TestCase):
    def test_source_authentication(self):
        for n in [1,2,3,5,7,19,41,139,271]:
            self.assertEqual(forcing(n),independent_forcing(n))

    def test_exact_golden_irrational_cutoff(self):
        lo,hi=golden_b_bounds(40)
        for q in [F(0),F(1,10),F(3,8),F(2,5),F(1,2)]:
            self.assertEqual(d_less_than_golden_b(q),float(q)<(3-math.sqrt(5))/2)
        self.assertLess(hi-lo,F(1,10**35))

    def test_constant_phase_calibration(self):
        # E_a(δ0) = (1/a)-1 = a = (sqrt5-1)/2.
        for n in [1,2,4,8,32]:
            low,high,_=golden_aperture_energy_bounds([F(1,5)]*n)
            blo,bhi=golden_b_bounds()
            self.assertEqual(low,1-bhi)
            self.assertEqual(high,1-blo)

    def test_uniform_grid_decay(self):
        for n in [2,4,8,16,32,64]:
            low,high,_=golden_aperture_energy_bounds([F(i,n) for i in range(n)])
            self.assertGreaterEqual(high,0)
            self.assertLess(float(high),3/n**2)

    def test_fast_census_vs_independent_bruteforce(self):
        from golden_aperture import golden_pair_census_bruteforce
        for n in [1,2,3,5,8,16,32]:
            pts=[F((i*i+3*i)%37,37) for i in range(n)]
            self.assertEqual(golden_pair_census(pts),golden_pair_census_bruteforce(pts))
        states=selected_states(2*32-1)
        self.assertEqual(golden_pair_census(states[32:64]),golden_pair_census_bruteforce(states[32:64]))

    def test_exact_pair_to_integrated_excess(self):
        pts=[F(0),F(2,9),F(4,11),F(19,21),F(1,3)]
        a=golden_aperture_energy_bounds(pts)
        k,d=golden_pair_census(pts)
        b=cutoff_interval_integral(k,d,len(pts))
        self.assertEqual((a[0],a[1]),b)

    def test_fiber_nonnegative_and_refinement(self):
        pts=[F(2,7),F(11,13),F(3,11),F(16,17),F(1,7),F(1,3),F(4,9),F(3,5)]
        lo,hi,_=golden_aperture_energy_bounds(pts)
        prev=lo
        for Q in [1,2,4,8]:
            low,high,_=golden_return_energy_bounds(pts,Q)
            self.assertGreaterEqual(high,0)
            self.assertGreaterEqual(float(high)+1e-25,float(prev))
            prev=low
            if Q==1:self.assertEqual((lo,hi),(low,high))
        a=(math.sqrt(5)-1)/2
        self.assertAlmostEqual(float(low),a,places=12)

    def test_return_constant_control(self):
        pts=[F(1,5)]*32
        for Q in [1,2,4,8,16,32]:
            l,u,_=golden_return_energy_bounds(pts,Q)
            self.assertAlmostEqual(float(l),(math.sqrt(5)-1)/2,places=12)

    def test_fixedpoint_interval_contains_exact(self):
        for A in [8,16,32,64,79,157]:
            pts=selected_states(2*A-1)[A:2*A]
            el,eh,_=golden_aperture_energy_bounds(pts)
            fl,fh,diag=golden_aperture_interval_fast(pts,24)
            self.assertLessEqual(fl,el)
            self.assertGreaterEqual(fh,eh)
            self.assertEqual(diag['near_ordered_pairs'],golden_pair_census(pts)[0])

    def test_original_source_early_windows(self):
        states=selected_states(2*64-1)
        for A in [8,16,32,64]:
            l,u,_=epoch_energy(A,states)
            self.assertLessEqual(l,u)
            self.assertGreaterEqual(u,0)
            # Source-phase data must feed exact lower/upper.
            self.assertLess(float(u),.2)

    def test_fast_fiber_matches_exact_fiber(self):
        pts=selected_states(2*128-1)[128:256]
        for Q in [1,2,4,8,16,32]:
            l,u,_=golden_return_energy_bounds(pts,Q)
            fl,fu,_=golden_return_energy_interval_fast(pts,Q,24)
            self.assertLessEqual(fl,l)
            self.assertGreaterEqual(fu,u)

    def test_original_source_fiber_increments(self):
        A=64
        pts=selected_states(2*A-1)[A:2*A]
        prev=-F(1)
        for Q in [1,2,4,8,16,32,64]:
            lo,hi,_=golden_return_energy_bounds(pts,Q)
            self.assertLess(float(prev),float(hi)+1e-14)
            prev=lo
        self.assertAlmostEqual(float(lo),(math.sqrt(5)-1)/2,places=12)

    def test_new_unsquared_transport_O_Aminus2(self):
        for A in [8,16,32]:
            states=selected_states(2*A-1)
            x=states[A:2*A]
            z=[(states[n]+partial_future_tail(n,12))%1 for n in range(A,2*A)]
            xl,xu,_=golden_aperture_energy_bounds(x)
            zl,zu,_=golden_aperture_energy_bounds(z)
            err=golden_energy_tail_transport_upper(A)
            self.assertLessEqual(zu-xl,err)
            self.assertLessEqual(xu-zl,err)
            cl,cu=completed_energy_bounds_from_original(A,states)
            self.assertLessEqual(cl,zu)
            self.assertGreaterEqual(cu,zl)

    def test_source_2adic_fiber_labels_are_clock_permutations(self):
        u=F()
        residues=[]
        Q=16
        for n in range(2*Q):
            if n>0:u=16*u+forcing(n)
            self.assertEqual(u.denominator%2,1)
            residues.append((u.numerator*pow(u.denominator,-1,Q))%Q)
        self.assertEqual(set(residues[:Q]),set(range(Q)))
        self.assertEqual(residues[:Q],residues[Q:])

    def test_non_normal_shadow_keeps_golden_energy(self):
        for A in [16,64,128]:
            ghost=[F(n,(2*n-1)**4) for n in range(A,2*A)]
            lo,hi,_=golden_aperture_energy_bounds(ghost)
            self.assertGreater(float(lo),0.45)

    def test_transport_analytic_bound_and_ghost(self):
        for A in [1,2,8,32,128]:
            self.assertLessEqual(float(harmonic_epoch_sum(A)), math.log(2)+1e-14)
            self.assertGreater(transport_bound_approx(A),0)
        # Coherent periodic ghost is an admissible mathematical countermodel to normality
        ghost=[F(1,5)]*16
        self.assertGreater(float(golden_aperture_energy_bounds(ghost)[0]),.6)

if __name__=='__main__':unittest.main()
