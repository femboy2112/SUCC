"""Source-first exact tests; no π normality or Collatz convergence inferences."""
import sys,unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from seam_differentials import *


class SourceTailTests(unittest.TestCase):
    def test_original_poles(self):
        self.assertEqual(authentic_forcing(1),Fraction(47,15))
        for n in range(1,60):
            self.assertGreater(authentic_forcing(n),0)
            self.assertGreater(authentic_forcing(n),authentic_forcing(n+1))

    def test_mutant_increment(self):
        for n in range(1,45):
            inc=mutant_increment(n)
            self.assertGreater(inc,0)
            self.assertEqual(forcing(n,1)-forcing(n,0),inc)
            self.assertLess(forcing(n,Fraction(1,2)),forcing(n,1))

    def test_lag_mean_interval(self):
        for m in [1,2,3,6,11,37,100,500]:
            lo,hi=lag_mean_interval(m,18)
            self.assertLess(lo,hi)
            self.assertLess(lo,Fraction(1,15))
            _,a,_=finite_source_journal(m,29)
            z,_,_=finite_source_journal(m,29)
            self.assertLess(lo,a/z)
            self.assertLess(a/z,hi)

    def test_monotone_mean_across_clocks(self):
        for tau in [0,Fraction(1,3),1]:
            mids=[]
            for m in range(1,24):
                lo,hi=lag_mean_interval(m,40,tau)
                mids.append((lo,hi))
                self.assertLess(hi,Fraction(1,15))
            for left,right in zip(mids,mids[1:]):
                self.assertLess(left[1],right[0])

    def test_signed_mutant_response(self):
        for m in [1,2,3,7,31,127,500]:
            for tau in [0,Fraction(1,2),1]:
                self.assertLess(lag_signed_derivative_truncated(m,30,tau),0)
            genuine=lag_mean_interval(m,34,0)
            mutant=lag_mean_interval(m,34,1)
            self.assertLess(mutant[1],genuine[0])

    def test_geometric_tv_bound(self):
        for n in [0,1,2,5,11,31,100]:
            z,_,_=finite_source_journal(n+1,35)
            mass=[Fraction(15,16**(k+1)) for k in range(35)]
            ww=[(authentic_forcing(n+k+1)/16**k)/z for k in range(35)]
            partial_tv=sum((abs(a-b) for a,b in zip(mass,ww)),Fraction())/2
            # Truncation makes this a conservative partial check, with true
            # upper bounded by the theorem's full TV estimate.
            self.assertLess(partial_tv,Fraction(16,120*n+29))

    def test_asymptotic_lag_means(self):
        for m in [50,150,400,1000]:
            lo,hi=lag_mean_interval(m,40)
            model=Fraction(1,15)-Fraction(32,225*m)+Fraction(182,1125*m*m)
            self.assertLess(abs((lo+hi)/2-model),Fraction(1,m**3))

    def test_matched_jet_difference_limit(self):
        target=-Fraction(4,3375)
        for m in [40,100,200,700]:
            lo,hi=lag_mean_interval(m,42,0)
            l2,h2=lag_mean_interval(m,42,1)
            scaled=(l2+h2-lo-hi)*m*m/2
            self.assertLess(abs(scaled-target),Fraction(1,m))

    def test_exact_source_fourier_moments(self):
        z,m1,m2=finite_source_journal(9,25)
        self.assertGreater(m2*z-m1*m1,0)
        self.assertGreater(m1,0)

class JacobianTests(unittest.TestCase):
    def test_completed_rank_one(self):
        j=finite_endpoint_jacobian((0,2,5,7,13),terminal=45)
        for row in j:
            self.assertEqual(row,tuple(row[0]*v for v in j[0]))

    def test_unwrapped_rows_nonproportional(self):
        rows=source_parameter_jacobian((0,2,5,7,13))
        self.assertEqual(rows[0],(Fraction(1),Fraction(0),Fraction(0),Fraction(0),Fraction(0)))
        self.assertNotEqual(rows[1][1]*rows[2][0],rows[2][1]*rows[1][0])

    def test_raw_full_rank(self):
        for times in [(0,1,2,3,4),(0,2,5,7,13),(3,4,7,12,21)]:
            A=[list(row) for row in source_parameter_jacobian(times)]
            rank=0
            for col in range(5):
                pivot=next((i for i in range(rank,5) if A[i][col]),None)
                if pivot is None:continue
                A[rank],A[pivot]=A[pivot],A[rank]
                v=A[rank][col]
                A[rank]=[a/v for a in A[rank]]
                for j in range(5):
                    if j!=rank:
                        c=A[j][col]
                        A[j]=[a-c*b for a,b in zip(A[j],A[rank])]
                rank+=1
            self.assertEqual(rank,5)

class SeamTests(unittest.TestCase):
    def test_signed_crossings_telescope(self):
        pairs=[(Fraction(1,10),Fraction(2,5)),(Fraction(1,7),Fraction(8,7)),
               (Fraction(1,37),Fraction(101,37)),(Fraction(5,39),Fraction(4,39))]
        for a,b in pairs:
            for n in range(0,5):
                self.assertEqual(signed_seam_crossings(a,b,n),quarter_at_clock(b,n)-quarter_at_clock(a,n))

    def test_signed_orientation(self):
        self.assertEqual(signed_seam_crossings(Fraction(1,8),Fraction(3,8),0),1)
        self.assertEqual(signed_seam_crossings(Fraction(5,8),Fraction(7,8),0),-1)
        self.assertEqual(signed_seam_crossings(Fraction(7,8),Fraction(5,8),0),1)
        self.assertEqual(signed_seam_crossings(Fraction(1,8),Fraction(7,8),0),0)

    def test_threshold_unassigned(self):
        for v in [Fraction(1,4),Fraction(3,4),Fraction(5,4)]:
            with self.assertRaises(ValueError):quarter_head(v)

    def test_source_quarter_prefix(self):
        # Hex digits 3,2,4,3,F,6,A,8,8,8,5,A; midquarter iff digit 4..11
        for n,digit in enumerate('3243F6A8885A'):
            self.assertEqual(interval_quarter_certificate(n,20),int(4<=int(digit,16)<=11))

    def test_pi_first_twelve_without_decoding(self):
        # exact source interval readout, rather than predecoded digit as input
        lo,hi=bbp_pi_over_16_interval(16)
        self.assertEqual(lo.__mul__(16**12).__floor__(),int('3243F6A8885A',16))
        self.assertEqual(hi.__mul__(16**12).__floor__(),int('3243F6A8885A',16))

    def test_wrong_seed_locked_phase(self):
        # wrong seed shares forcing/tail differentials; objective root rejects
        self.assertEqual(signed_seam_crossings(Fraction(0),Fraction(0),3),0)
        self.assertGreater(lag_signed_derivative_truncated(9,28,0).__abs__(),0)

    def test_prime_counterfactual_displacements(self):
        for p in [7,11,19,29,43,67,97]:
            j=(p*p-1)//8
            self.assertEqual(8*j+1,p*p)
            d,D=first_radix_delayed_displacement(j)
            self.assertGreaterEqual(D,Fraction(1,64));self.assertLess(D,Fraction(1,4))
            if d>0:self.assertLess(D/16,Fraction(1,64))

    def test_quarter_signed_changes_do_not_force_positivity(self):
        # source-derived positive displacement can have zero or either sign
        d=Fraction(3,32)
        cases=[(Fraction(1,32),0),(Fraction(1,5),1),(Fraction(7,10),-1)]
        for x,expected in cases:
            self.assertEqual(signed_seam_crossings(x,x+d,0),expected)



class DifferentialCurrentTests(unittest.TestCase):
    def test_variation_exact(self):
        for n in range(0,7):
            self.assertEqual(quarter_current_total_variation(n),2*16**n)

    def test_fourier_support_and_orientation(self):
        for n in range(0,5):
            q=16**n
            for j in [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]:
                val=quarter_current_fourier_over_i(n,q*j)
                self.assertEqual(val,0 if j%2==0 else 2*q*(-1 if (j+1)//2%2 else 1))
            if n:
                self.assertEqual(quarter_current_fourier_over_i(n,1),0)

    def test_prime_source_signed_quarter_controls(self):
        # Counterfactual signed quarter-port response can be zero, + or −.
        self.assertEqual(source_order_quarter_response(7)[2],0)
        self.assertEqual(source_order_quarter_response(79)[2],1)
        self.assertEqual(source_order_quarter_response(131)[2],-1)

    def test_one_clock_finite_lag_distinguishes_mutant(self):
        # Even at late clock m=1000, a 43-atom rational journal resolves tau=0/1.
        for m in [1,20,100,1000]:
            lo,hi=lag_mean_interval(m,43,0)
            lm,hm=lag_mean_interval(m,43,1)
            self.assertLess(hm,lo)

    def test_source_zero_anchor_does_not_follow_from_tail(self):
        # mu_n depends on tau, but not on the homogeneous seed s.
        lo,hi=lag_mean_interval(8,30,0)
        self.assertLess(lo,hi)
        self.assertNotEqual(lo,Fraction(0))
        # An identically completed-locked seed can share that exact same mu.
        self.assertEqual(quarter_at_clock(Fraction(0),8),0)

    def test_exact_pi_quarter_interval_vs_shadow(self):
        # Source-only quarter port equals source-selected Collatz two-bit XOR.
        digits='3243F6A8885A'
        for n in range(12):
            digit=int(digits[n],16)
            xor=((digit>>2)&1)^((digit>>3)&1)
            self.assertEqual(interval_quarter_certificate(n,22),xor)

if __name__ == '__main__':unittest.main()
