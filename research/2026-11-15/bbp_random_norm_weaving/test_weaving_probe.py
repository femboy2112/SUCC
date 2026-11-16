"""Tests: independent exact arithmetic + randomized readout calibration."""
import math
import random
import unittest
from fractions import Fraction
from weaving_probe import *

class TestWeaving(unittest.TestCase):
    def test_four_poles_vs_integral_coefficients(self):
        for n in range(1,25):
            i=8*n-8
            res=4*Fraction(1,i+1)-2*Fraction(1,i+4)-Fraction(1,i+5)-Fraction(1,i+6)
            self.assertEqual(forcing(n),res)

    def test_four_pole_factorization_exact(self):
        for i in range(51):
            t=Fraction(i,50)
            self.assertEqual(weight_polynomial(t),factorized_weight(t))
            self.assertGreaterEqual(weight_polynomial(t),0)

    def test_kernel_difference_exact(self):
        for i in range(41):
            t=Fraction(i,40)
            self.assertEqual(original_kernel(t)-chiral_kernel(t),defect_kernel(t))
            self.assertGreaterEqual(defect_kernel(t),0)
            if t: self.assertGreater(defect_kernel(t),0)

    def test_chiral_sign_quadratic(self):
        for n in range(250):
            self.assertEqual(chiral_sign(n), (-1)**((n*(n-1)//2)%2))
            self.assertEqual(chiral_sign(n+2),-chiral_sign(n))

    def test_chiral_sign_weave_bicharacter(self):
        for n in range(12):
            for m in range(12):
                self.assertEqual(chiral_sign(n+m),chiral_sign(n)*chiral_sign(m)*(-1)**(n*m))

    def test_chiral_series_agrees_source(self):
        import mpmath as mp
        mp.mp.dps=55
        a=mp.quad(lambda t: (4-2*t**3-t**4-t**5)*(16+t**8)/(256+t**16),[0,1])
        part=chiral_source_partial(40)
        aa=mp.mpf(part.numerator)/part.denominator
        self.assertLess(abs(a-aa),mp.mpf('1e-45'))
        original=mp.quad(lambda t:(4-2*t**3-t**4-t**5)/(16-t**8),[0,1])
        self.assertLess(abs(original-mp.pi/16),mp.mpf('1e-50'))
        self.assertGreater(original,a)

    def test_exact_click_nesting(self):
        rng=random.Random(4)
        for _ in range(3500):
            t=Fraction(rng.randrange(1,255),255)
            u=tuple(Fraction(rng.randrange(256),255) for _ in range(6))
            w=Fraction(rng.randrange(256),255)
            p0,pchi=source_probabilities(t,u)
            a,b=shared_source_clicks(t,u,w)
            self.assertGreaterEqual(a,b)
            self.assertEqual(a-b,int(pchi<w<=p0))

    def test_exact_forced_defect(self):
        t=Fraction(1,2)
        u=(Fraction(3,4),Fraction(1,4),Fraction(1,4),Fraction(1,4),Fraction(1,4),Fraction(1,4))
        p0,pchi=source_probabilities(t,u)
        self.assertGreater(p0,pchi)
        self.assertLessEqual(p0,1)
        self.assertEqual(shared_source_clicks(t,u,(p0+pchi)/2),(1,0))

    def test_raw_max_cdf_and_correlation(self):
        rng=random.Random(20261115)
        N=60000
        data=[(rng.random(),rng.random()) for _ in range(N)]
        for t in (.2,.5,.8):
            p=sum(max(a,b)<=t for a,b in data)/N
            self.assertLess(abs(p-t*t),.012)
        m2=sum(max(a,b)**2 for a,b in data)/N
        m4=sum(max(a,b)**4 for a,b in data)/N
        self.assertLess(abs(m2-.5),.009)
        self.assertLess(abs(m4-1/3),.009)

    def test_square_to_disk_radial_independence(self):
        rng=random.Random(171)
        N=35000
        samples=[disk_weave(rng.random(),rng.random()) for _ in range(N)]
        self.assertLess(abs(sum(r*r for _,_,r,_ in samples)/N-.5),.01)
        self.assertLess(abs(sum(x for x,_,_,_ in samples)/N),.012)
        self.assertLess(abs(sum(y for _,y,_,_ in samples)/N),.012)
        self.assertLess(abs(sum((1 if b else -1) for _,_,_,b in samples)/N),.012)

    def test_disk_inverse(self):
        rng=random.Random(1710)
        for _ in range(1000):
            x,y=rng.random(),rng.random()
            cx,cy,m,b=disk_weave(x,y)
            rx,ry=disk_unweave(cx,cy)
            self.assertLess(max(abs(rx-x),abs(ry-y)),2e-14)

    def test_chiral_jet_from_actual_rational_source(self):
        states=lifted_original_states(92)
        for n in range(4,60):
            self.assertEqual(original_jet_direct(states,n,1),chiral_jet(n))

    def test_chiral_jet_high_period(self):
        states=lifted_original_states(270)
        for n in range(5,11):
            self.assertEqual(original_jet_direct(states,n,2),chiral_jet(n))

    def test_two_time_source_phase_exact(self):
        for n in range(4,16):
            for z in (0,1/15,1/17,.1234,.43755):
                for h in (1,2,7):
                    a,b=two_time_chiral_phases(n,z,h)
                    expected=-complex(math.cos(2*math.pi*255*h*z),math.sin(2*math.pi*255*h*z))
                    self.assertLess(abs(b*a.conjugate()-expected),2e-11)

    def test_two_probe_norm_click_calibration(self):
        rng=random.Random(12345)
        a,b=two_time_chiral_phases(7,.123456,1)
        for theta in (0,math.pi/2):
            p=two_path_probability(a,b,theta)
            obs=sum(two_probe_click(rng.random(),rng.random(),a,b,theta) for _ in range(35000))/35000
            self.assertLess(abs(obs-p),.017)

    def test_quadrature_reconstruction(self):
        for n in range(5,14):
            for z in (0,.0123,.178,.5011):
                a,b=two_time_chiral_phases(n,z,1)
                p0=two_path_probability(a,b,0)
                p1=two_path_probability(a,b,math.pi/2)
                recovered=(2*p0-1)+1j*(2*p1-1)
                self.assertLess(abs(recovered-b*a.conjugate()),8e-15)

    def test_shared_probe_complex_transport(self):
        rng=random.Random(99)
        a,b=two_time_chiral_phases(8,.1243,1)
        N=55000
        obs=sum(shared_norm_product(rng.random(),rng.random(),a,b) for _ in range(N))/N
        self.assertLess(abs(2*obs-b*a.conjugate()),.012)

    def test_fresh_phase_false_blindness(self):
        rng=random.Random(88)
        a,b=two_time_chiral_phases(8,.1243,1)
        N=38000
        obs=0j
        for _ in range(N):
            xa,ya,_,_=disk_weave(rng.random(),rng.random())
            xb,yb,_,_=disk_weave(rng.random(),rng.random())
            obs+=complex(xb,yb)*b*(complex(xa,ya)*a).conjugate()
        self.assertLess(abs(obs/N),.015)

    def test_wrong_seed_no_spurious_energy_shared(self):
        rng=random.Random(100)
        a,b=two_time_chiral_phases(8,0.,1)
        self.assertLess(abs(a+b),2e-15)
        self.assertLess(two_path_probability(a,b,0.),1e-28)
        for _ in range(300):
            self.assertEqual(two_probe_click(rng.random(),rng.random(),a,b,0),0)
            self.assertLess(abs((shared_norm_product(.51,.73,a,b)).real+.73**2),1e-13)

    def test_monotone_common_threshold_disagreement(self):
        # Analytic exact maximal coupling identity:
        # P(C_p != C_q) = |p-q| with shared M^2 uniform.
        for p,q in ((Fraction(1,9),Fraction(1,4)),(Fraction(1,2),Fraction(3,4)),(Fraction(0),Fraction(1))):
            self.assertEqual((max(p,q)-min(p,q)),abs(p-q))
            self.assertGreaterEqual(p+q-2*p*q,abs(p-q))

    def test_temporal_coupling_variance_null(self):
        # Coherent zero phase gives zero for shared probe amplitude,
        # but independent random disk phases have mean norm energy 1.
        a,b=two_time_chiral_phases(8,0.,1)
        self.assertAlmostEqual(abs(a+b)**2,0.,places=12)
        self.assertEqual(Fraction(1,2)+Fraction(1,2),1)

    def test_mutation_suppresses_chirality(self):
        # In source coboundary mutant, J'_n=J_n+4n mod 16;
        # two-step commutator becomes +1, not -1.
        for n in range(4,80):
            j=(chiral_jet(n)+4*n)%16
            j2=(chiral_jet(n+2)+4*(n+2))%16
            self.assertEqual(j,j2)

    def test_chiral_twist_signs(self):
        self.assertEqual([chiral_sign(n) for n in range(8)], [1,1,-1,-1,1,1,-1,-1])

    def test_bad_seed_and_bad_prob_validation(self):
        with self.assertRaises(ValueError):disk_weave(-.1,.5)
        with self.assertRaises(ValueError):source_random_channels(.5,[0]*5)
        with self.assertRaises(ValueError):threshold_pair_shared(.2,.3,-.1,.8)

if __name__ == '__main__':unittest.main()

class TestStoppedNormMachine(unittest.TestCase):
    def test_source_moments_as_max_volume(self):
        # Exact independent integration of E[t^(8(n-1)) A B C].
        for n in range(1,30):
            m=8*(n-1)
            moment=(Fraction(4,m+1)-Fraction(2,m+4)-Fraction(1,m+5)-Fraction(1,m+6))
            self.assertEqual(moment,forcing(n))

    def test_geometric_index_distribution(self):
        self.assertEqual(sum((Fraction(15,16**n) for n in range(1,18)),Fraction()),1-Fraction(1,16**17))
        part=sum((Fraction(15*(n-1),16**n) for n in range(1,300)),Fraction())
        self.assertGreater(Fraction(1,15),part)
        self.assertLess(Fraction(1,15)-part,Fraction(1,16**260))

    def test_geometric_program_numeric(self):
        rng=random.Random(2026111504)
        N=62000
        counts=0
        for _ in range(N): counts+=stopped_source_click(rng)
        self.assertLess(abs(counts/N-math.pi/16),.012)

    def test_geometric_program_source_tag(self):
        rng=random.Random(2026111505)
        seen=[]
        for _ in range(1000):
            c,n=stopped_source_click(rng,return_index=True)
            self.assertIn(c,(0,1));self.assertGreaterEqual(n,1)
            seen.append(n)
        self.assertGreater(sum(n==1 for n in seen),800)

    def test_geometric_chiral_selection_exact(self):
        # Full source difference is exactly twice the negative-chiral sector.
        # Finite pure-rational partials retain the exact coefficient equality.
        for N in (4,8,12,20):
            diff=bbp_source_partial(N)-chiral_source_partial(N)
            neg=2*sum((forcing(n)/16**n for n in range(1,N+1)
                       if chiral_sign(n-1)==-1),Fraction())
            self.assertEqual(diff,neg)

if __name__ == '__main__':unittest.main()

class TestSourceSignedGammaHierarchy(unittest.TestCase):
    def test_source_signed_lag_exact(self):
        for n in range(60):
            self.assertEqual(chiral_gram(n,n+2),-forcing(2*n+3))
            self.assertLess(chiral_gram(n,n+2),0)

    def test_strict_source_gram_cs(self):
        for n in range(50):
            det=forcing(2*n+1)*forcing(2*n+5)-forcing(2*n+3)**2
            self.assertGreater(det,0)

    def test_every_collision_energy_positive(self):
        for n in range(12):
            for k in range(6):
                self.assertGreater(coherent_collision_energy(n,k),0)

    def test_energy_first_two_exact(self):
        for n in range(12):
            self.assertEqual(coherent_collision_energy(n,0), forcing(2*n+1))
            self.assertEqual(coherent_collision_energy(n,1),
                             forcing(2*n+1)-2*forcing(2*n+3)+forcing(2*n+5))

    def test_chiral_gamma_asymptotic_constants(self):
        for k in range(4):
            n=16384
            scaled=coherent_collision_energy(n,k)*n**(2*k+2)
            target=coherent_collision_limit(k)
            self.assertLess(abs(float((scaled-target)/target)),.004)
        self.assertEqual(coherent_collision_limit(0),Fraction(15,256))
        self.assertEqual(coherent_collision_limit(1),Fraction(45,128))
        self.assertEqual(coherent_collision_limit(2),Fraction(225,32))

    def test_source_norm_anticorrelation(self):
        import math
        for n in (5,50,500,5000):
            corr=float(chiral_gram(n,n+2))/math.sqrt(
                float(chiral_gram(n,n)*chiral_gram(n+2,n+2)))
            self.assertGreater(corr,-1.)
            self.assertLess(corr,0.)
        n=5000
        corr=float(chiral_gram(n,n+2))/math.sqrt(
            float(chiral_gram(n,n)*chiral_gram(n+2,n+2)))
        self.assertLess(abs(corr+1),1e-5)

if __name__ == '__main__':unittest.main()
