"""Exact integer and independent finite-Fourier tests of Gamma16 research transport."""
import unittest
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from cmath import exp
from math import pi
import random

from observational_succ.bbp_gamma16_matrix import (
    RADIX, pair_counts, marginal_counts, difference_counts, exact_energy_split,
    fourier_pair_modes, sector_energy_float, primitive_order,
    primitive_sector_masses, de_bruijn_16, cyclic_word_energy,
    fractional_digits_of, two_digit_tail_lift, reconstruct_from_lift,
    fejer_carry_pair_lattice,fejer_carry_pair_direct,quarter_turn_kernel,
    forced_carry_pair,blocking_polynomial,blocking_at_t,qgamma_ratio_at_q,
    blocked_source_forcing,blocked_laplace_four_poles,blocking_endpoint_jets,
    stroboscopic_pair_split,haar_reference_pair_law,genuine_prime_stage_matrix_mixture,
)

ROOT=Path(__file__).resolve().parents[1]
HEX=ROOT/'research/2026-11-09/gamma16_yoneda/REUSED_HEX_40960.txt'

class Gamma16Matrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data=HEX.read_text(encoding='ascii')
        assert sha256(data.encode('ascii')).hexdigest()=='c4010a291cf411147dd1a6a65104bd4cf995a4d931b6dfefb9fd9277f8434527'
        cls.digits=tuple(int(c,16) for c in data.strip())
        assert len(cls.digits)==40960

    def test_source_matrix_exact_40960(self):
        c=pair_counts(self.digits)
        self.assertEqual(sum(map(sum,c)),40960)
        self.assertEqual(marginal_counts(c)[0],marginal_counts(c)[1])
        self.assertEqual(min(v for row in c for v in row),129)
        self.assertEqual(max(v for row in c for v in row),189)
        e=exact_energy_split(c)
        self.assertEqual(e['pair_energy'],Q(981,163840))
        self.assertEqual(e['relative_energy'],Q(29849,52428800))
        self.assertEqual(e['basis_energy'],Q(284071,52428800))
        self.assertEqual(e['one_digit_energy'],Q(7629,52428800))

    def test_exact_energy_split_diverse_finite_paths(self):
        rng=random.Random(20261109)
        for n in (2,16,32,101,256):
            for case in range(6):
                d=[rng.randrange(16) for _ in range(n)]
                if case==1:d=[0]*n
                if case==2:d=[i%16 for i in range(n)]
                c=pair_counts(d)
                e=exact_energy_split(c)
                self.assertEqual(e['relative_energy']+e['basis_energy'],e['pair_energy'])
                self.assertGreaterEqual(e['basis_energy'],e['one_digit_energy'])

    def test_cyclic_flow_and_boundary_linear(self):
        for d in (self.digits[:32],self.digits[:256],self.digits[-33:]):
            c=pair_counts(d,cyclic=True)
            self.assertEqual(*marginal_counts(c))
            linear=pair_counts(d,cyclic=False)
            rows,cols=marginal_counts(linear)
            self.assertEqual(tuple(rows[a]-cols[a] for a in range(16)),
                             tuple((a==d[0])-(a==d[-1]) for a in range(16)))

    def test_relative_twirl_is_orthogonal_projection(self):
        c=pair_counts(self.digits)
        n=sum(map(sum,c))
        q=difference_counts(c)
        basis=Q(sum((16*c[a][b]-q[(b-a)%16])**2
                    for a in range(16) for b in range(16)),n*n)
        relative=Q(16*sum(t*t for t in q)-n*n,n*n)
        self.assertEqual(basis,exact_energy_split(c)['basis_energy'])
        self.assertEqual(relative,exact_energy_split(c)['relative_energy'])

    def test_fourier_parseval_and_translation_selection(self):
        c=pair_counts(self.digits)
        z=fourier_pair_modes(c)
        self.assertLess(abs(z[0][0]-1),1e-12)
        exact=exact_energy_split(c)
        numer=sector_energy_float(c)
        self.assertLess(abs(numer['relative_energy']-float(exact['relative_energy'])),3e-12)
        self.assertLess(abs(numer['basis_energy']-float(exact['basis_energy'])),3e-12)
        self.assertLess(abs(sum(abs(z[u][v])**2 for u in range(16) for v in range(16))
                            -1-float(exact['pair_energy'])),3e-12)

    def test_five_cyclotomic_sector_dims_and_sum(self):
        self.assertEqual(tuple(sum(primitive_order(h)==q for h in range(16))
                               for q in (1,2,4,8,16)),(1,1,2,4,8))
        sec=primitive_sector_masses(pair_counts(self.digits[:2048]))
        self.assertEqual(len(sec),25)
        self.assertLess(abs(sum(sec.values())-1-float(exact_energy_split(pair_counts(self.digits[:2048]))['pair_energy'])),2e-12)

    def test_periodic_shift_cycle_is_basis_homogeneous_but_not_haar(self):
        d=tuple(i%16 for i in range(4096))
        e=exact_energy_split(pair_counts(d))
        self.assertEqual(e['one_digit_energy'],0)
        self.assertEqual(e['basis_energy'],0)
        self.assertEqual(e['relative_energy'],15)

    def test_debruijn_pair_haar_is_periodic_nonnormal(self):
        d=de_bruijn_16(2)
        c=pair_counts(d)
        self.assertTrue(all(v==1 for row in c for v in row))
        self.assertEqual(exact_energy_split(c)['pair_energy'],0)
        self.assertEqual(cyclic_word_energy(d,3),15)
        # Every two-digit transition is uniform although the sequence is periodic.
        self.assertEqual(len(d),256)

    def test_full_support_mixing_markov_circulant_counterexample(self):
        # Stationary kernel P=(I/2)+(J/32), not Haar pair law.
        # Exact joint probability M_ab=P_ab/16.
        M=lambda a,b:Q(1,512)+(Q(1,32) if a==b else Q(0))
        q=[sum(M(a,(a+d)%16) for a in range(16)) for d in range(16)]
        self.assertEqual(q[0],Q(17,32))
        self.assertEqual(q[1],Q(1,32))
        self.assertEqual(16*sum(v*v for v in q)-1,Q(15,4))
        self.assertTrue(all(sum(M(a,b) for b in range(16))==Q(1,16) for a in range(16)))

    def test_tail_lift_reconstructs_rational_points(self):
        xs=[Q(0),Q(1,3),Q(31,256),Q(1,2),Q(255,256),Q(7,16),Q(7,16)]
        lift=two_digit_tail_lift(xs)
        reconstructed=reconstruct_from_lift(lift)
        self.assertEqual(reconstructed,{x:Q(count,len(xs)) for x,count in Counter(xs).items()})
        for (a,b,y),v in lift.items():
            self.assertEqual(fractional_digits_of(Q(16*a+b+y,256),2),(a,b))
            self.assertGreater(v,0)

    def test_tail_lift_catches_haar_two_digits_alias(self):
        # Construct 256 periodic points: each pair appears, but tails are atomic.
        d=de_bruijn_16(2)
        x=Q(sum(d[j]*16**(len(d)-1-j) for j in range(len(d))),16**len(d)-1)
        orbit=[]
        for i in range(256):
            orbit.append(x)
            x=(16*x)%1
        lift=two_digit_tail_lift(orbit)
        cell_mass=Counter()
        for (a,b,y),v in lift.items():cell_mass[(a,b)]+=v
        self.assertTrue(all(cell_mass[(a,b)]==Q(1,256) for a in range(16) for b in range(16)))
        self.assertTrue(all(len({y for (a,b,y) in lift if a==i and b==j})==1
                            for i in range(16) for j in range(16)))

    def test_fourier_unitary_and_4th_order(self):
        f=quarter_turn_kernel()
        for i in range(16):
            for j in range(16):
                dot=sum(f[i][k]*f[j][k].conjugate() for k in range(16))
                self.assertLess(abs(dot-(1 if i==j else 0)),4e-14)
        f2=[[sum(f[i][k]*f[k][j] for k in range(16)) for j in range(16)] for i in range(16)]
        for i in range(16):
            for j in range(16):
                self.assertLess(abs(f2[i][j]-(1 if (i+j)%16==0 else 0)),4e-14)

    def test_single_twisted_floor_pair_lattice(self):
        for x in (Q(1,7),Q(5,13),Q(19,64),Q(31,99)):
            for r,s in ((Q(1,120),Q(1,130)),(Q(7,19),Q(5,17))):
                for h,k in ((1,1),(0,1),(1,0),(3,5),(8,9)):
                    v=fejer_carry_pair_direct(x,r,s,h,k,98)
                    w=fejer_carry_pair_lattice(x,r,s,h,k,98)
                    self.assertLess(abs(v-w),2e-11,(x,r,s,h,k))

    def test_source_two_step_carries_and_original_poles(self):
        from observational_succ.duck_bbp import forcing
        x=Q(0)
        for n in range(1,40):
            r=forcing(n)
            self.assertEqual(r,Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))
            x=(16*x+r)%1
            if n>=2:
                a,b=forced_carry_pair(n,x)
                self.assertEqual(a,(16*x+forcing(n)).numerator//(16*x+forcing(n)).denominator)
                y=(16*x+forcing(n))%1
                self.assertEqual(b,(16*y+forcing(n+1)).numerator//(16*y+forcing(n+1)).denominator)

    def test_rational_source_shift_haar_reference_is_seed_blind(self):
        # For any fixed rational r, the map x -> (floor(16x+r) mod16, {16x+r})
        # sends Lebesgue measure to uniform-16 x Lebesgue. This is NOT a statement
        # that original U0=0 is Haar.
        for r in (Q(0),Q(1,101),Q(29,31)):
            for a in range(16):
                # inverse of y given branch a on the quotient by the integer loop
                ys=(Q(1,5),Q(2,5),Q(4,5))
                for y in ys:
                    t=Q(a)+y-r
                    x=(t%16)/16
                    z=16*x+r
                    self.assertEqual(int(z)%16,a)
                    self.assertEqual(z%1,y)

    def test_bad_inputs(self):
        for bad in ([], [0], [1,2,16], [-1,3], [1,2.5]):
            with self.assertRaises(ValueError):pair_counts(bad)
        with self.assertRaises(ValueError):fractional_digits_of(Q(-1,2),2)
        with self.assertRaises(ValueError):two_digit_tail_lift([])
        with self.assertRaises(ValueError):reconstruct_from_lift({})


    def test_grouped_source_laplace_is_authentic_four_poles(self):
        from observational_succ.duck_bbp import forcing
        for g in (1,2,3,4,5):
            for k in (1,2,7,11):
                self.assertEqual(blocked_laplace_four_poles(k,g),
                                 blocked_source_forcing(k,g))
            self.assertEqual(blocking_endpoint_jets(g)[0],16**g-1)
            self.assertEqual(blocking_polynomial(g),
                             tuple(16**(g-1-j) for j in range(g)))
        self.assertEqual(blocking_endpoint_jets(1),(15,-59))
        self.assertEqual(blocking_endpoint_jets(2),(255,-1243))

    def test_qgamma_recurrence_is_exact_scaled_block_multiplier(self):
        for g in (1,2,3,4,5,7):
            for t in (Q(1),Q(1,2),Q(1,17),Q(3,4)):
                if t!=0:
                    q=t/Q(16)
                    self.assertEqual(blocking_at_t(g,t),
                                     16**(g-1)*qgamma_ratio_at_q(g,q))
        for g in (1,2,3,5):
            self.assertEqual(15*blocking_at_t(g,Q(1)),16**g-1)

    def test_block_polynomial_additive_cocycle_and_multiplicative_composition(self):
        for g in (1,2,3,4):
            for h in (1,2,3,4):
                for t in (Q(0),Q(1,7),Q(1,2),Q(1)):
                    lhs=blocking_at_t(g+h,t)
                    rhs=16**h*blocking_at_t(g,t)+t**g*blocking_at_t(h,t)
                    self.assertEqual(lhs,rhs)
                    composed=blocking_at_t(g,t)*sum((16**(g*(h-1-j))*t**(g*j)
                                                for j in range(h)),Q())
                    self.assertEqual(blocking_at_t(g*h,t),composed)

    def test_stroboscopic_exact_two_digit_time_alignment(self):
        from observational_succ.bbp_gamma16_matrix import stroboscopic_pair_split
        e=stroboscopic_pair_split(self.digits)
        self.assertEqual(e['all'],Q(981,163840))
        self.assertEqual(e['even'],Q(9281,819200))
        self.assertEqual(e['odd'],Q(10249,819200))
        self.assertEqual(e['stroboscopic'],Q(243,40960))
        self.assertEqual((e['even']+e['odd'])/2,e['all']+e['stroboscopic'])
        for x in (tuple(i%16 for i in range(256)),de_bruijn_16(2),tuple([0]*16)):
            y=stroboscopic_pair_split(x)
            self.assertGreaterEqual(y['stroboscopic'],0)


    def test_exact_haar_reference_pair_law_source_independent(self):
        for r,s in ((Q(0),Q(0)),(Q(1,101),Q(1,130)),
                    (Q(7,19),Q(5,17)),(Q(29,31),Q(11,13))):
            m=haar_reference_pair_law(r,s)
            self.assertTrue(all(m[a][b]==Q(1,256)
                                for a in range(16) for b in range(16)))


    def test_finite_empirical_tail_TV_stays_maximal_even_when_pair_haar(self):
        # Haar pair marginals and a fully known periodic orbit do not license
        # replacing individual future tails by an independent Haar variable.
        d=de_bruijn_16(2)
        x=Q(sum(d[j]*16**(len(d)-1-j) for j in range(len(d))),16**len(d)-1)
        src=Counter()
        for _ in range(256):
            src[x]+=1
            x=(16*x)%1
        self.assertEqual(len(src),256)
        all_points=set(src)
        shifted=Counter()
        for y in src:
            for a in range(16):
                shifted[(y+Q(a,16))%1]+=Q(1,16*256)
        total=sum((abs(Q(src.get(y,0),256)-shifted.get(y,Q()))
                   for y in all_points|set(shifted)),Q())
        self.assertEqual(total,Q(15,8))  # L1; ordinary TV distance=15/16.

    def test_source_zero_green_gauge_finite_horizon(self):
        from observational_succ.duck_bbp import forcing
        for end in (4,8,12):
            alpha=sum((forcing(j)/16**j for j in range(1,end+1)),Q())
            u=Q()
            for n in range(0,end+1):
                if n:u=16*u+forcing(n)
                tail=sum((forcing(j)/16**(j-n) for j in range(n+1,end+1)),Q())
                self.assertEqual(u+tail,16**n*alpha)


    def test_prime_birth_stage_matrix_mixture_exact_source_boundaries(self):
        from observational_succ.balanced_prime_clock import prime_candidates
        for A in (2048,4096,8192):
            p,m=prime_candidates(A)[0]
            r=genuine_prime_stage_matrix_mixture(self.digits,A,p)
            self.assertEqual(len(r['weights']),4)
            self.assertEqual(sum(r['weights']),1)
            self.assertEqual(r['stage_mixing_energy']+r['overall_energy'],r['weighted_stage_energy'])
            self.assertGreater(r['stage_mixing_energy'],0)
        r=genuine_prime_stage_matrix_mixture(self.digits,2048,4937)
        self.assertEqual(r['boundaries'],(2048,2469,3086,3703,4096))


    def test_alpha_pi_over16_strobe_boundary_alignment(self):
        # From U_0=0, alpha=pi/16 has leading base16 digit 3, then the
        # certified fractional digits of pi. Base256 time-0 digit is (3,2);
        # later radix256 symbols at n=2k correspond to (d_2,d_3), etc.
        d=self.digits
        alpha_digits=(3,)+d[:7]
        blocks=[tuple(alpha_digits[2*i:2*i+2]) for i in range(4)]
        self.assertEqual(blocks,[(3,2),(4,3),(15,6),(10,8)])
        self.assertEqual(blocks[1:],[(d[i],d[i+1]) for i in (1,3,5)])

if __name__=='__main__': unittest.main()
