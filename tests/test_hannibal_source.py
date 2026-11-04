"""Exact hostile tests for Hannibal's limited source inequalities."""
import importlib.util
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


h = load('hannibal_test_source', 'research/2026-11-02/hannibal_source/hannibal.py')
w = load('hannibal_test_mirror', 'research/2026-11-02/weyl_mirror_campaign/weyl_mirror.py')
msa = load('hannibal_test_msa', 'research/2026-11-02/mesoscopic_spectral_army/mesoscopic.py')
odd_replay = load('hannibal_test_odd', 'research/2026-11-02/hannibal_source/odd_replay.py')


class SourcePaths(unittest.TestCase):
    def test_factor_sieve_register_against_gcd_and_fraction(self):
        for last in (0,1,17,128,384):
            D, xs = w.odd_modular_lift(last)
            self.assertEqual(odd_replay.odd_modulus(last),D)
            rows = list(odd_replay.odd_source(last))
            self.assertEqual([r[1] for r in rows[1:]],xs)
            self.assertEqual([F(a,d) for n,a,d,c in rows[1:]],h.phases(last))

    def test_three_exact_paths_and_literal_carries(self):
        rows = list(h.full_source(384))
        D, odd = w.odd_modular_lift(384)
        xs = h.phases(384)
        self.assertEqual(xs, [F(a,d) for n,a,d,c in rows[1:]])
        self.assertEqual(xs, [F(a,D) for a in odd])
        self.assertEqual(xs, [F(a,d) for n,a,d in msa.original_modular_lift(384) if n])
        previous = F(0)
        for (n,a,d,c), x in zip(rows[1:], xs):
            self.assertEqual(16*previous+h.source(n), c+x)
            previous = x

    def test_horizon_changes_modulus_not_source(self):
        a = [F(x,d) for n,x,d,c in h.full_source(64)]
        b = [F(x,d) for n,x,d,c in h.full_source(96)]
        self.assertEqual(a, b[:65])

    def test_full_unwrapped_zero_boundary(self):
        U, integer_history = F(0), 0
        for n,a,d,c in h.full_source(48):
            if n:
                U = 16*U+h.source(n)
                integer_history = 16*integer_history+c
            self.assertEqual(U, integer_history+F(a,d))


class AnnulusProof(unittest.TestCase):
    def test_actual_source_all_lags_and_independent_pair_oracle(self):
        for A,m in ((64,64),(128,64),(128,128)):
            xs = w.fraction_phases(2*A-1)[A-1:]
            D, rs = w.odd_modular_lift(2*A-1)
            row = h.annulus_census(rs[A-1:],D,A,m)
            self.assertEqual([], row['violations'])
            self.assertEqual(h.exact_pair_oracle(xs,m),
                             (row['ordered_near'],row['ordered_strict_inner'],row['ordered_shell']))
            self.assertLessEqual(row['ordered_shell'],row['ordered_shell_ceiling'])
            for lag in row['lags']:
                self.assertLessEqual(lag['shell'],lag['shell_ceiling'])
                self.assertLessEqual(lag['near'],lag['near_ceiling'])

    def test_two_step_affine_no_wrap_both_signs_and_closed_endpoints(self):
        A,m,d = 4096,1024,37
        K = h.packet_depth(m,4)
        self.assertEqual(K,2)
        for delta in (F(1,8*m),-F(1,8*m),F(1,m),-F(1,m)):
            z = delta
            for q in range(1,K+1):
                z = 16*z-(h.source(A+q)-h.source(A+d+q))
                self.assertLess(abs(z),F(1,2))
                self.assertGreater(abs(z),F(1,m))
                self.assertEqual(z,(z+F(1,2))%1-F(1,2))

    def test_exact_shell_sum_and_mesh_steps(self):
        for A,m in ((64,64),(255,255),(1024,1024),(4096,4096)):
            K = h.packet_depth(m,4)
            expected = 2*sum((L+K)//(K+1) for L in range(1,A))
            self.assertEqual(h.shell_bound(A,m),expected)
        self.assertEqual([h.packet_depth(m,4) for m in (63,64,1023,1024)],[0,1,1,2])

    def test_inner_strict_and_shell_closed_partition(self):
        m = 64
        xs = [F(0),F(1,8*m),F(1,m)]
        near,inner,shell = h.exact_pair_oracle(xs,m)
        self.assertEqual((near,inner,shell),(9,3,6))

    def test_outer_shell_gives_no_inner_mass_control(self):
        A,m = 128,64
        xs = [F(1,5)-F(1,128*n*n) for n in range(A,2*A)]
        # A calibrated cloud in the possible Green-tail envelope, not actual BBP states.
        self.assertEqual(h.exact_pair_oracle(xs,m),(A*A,A*A,0))


class DenseLagAndCarries(unittest.TestCase):
    def test_finite_dense_lag_packets_do_not_assume_theorem_onset(self):
        A = 16
        D, xs = w.odd_modular_lift(25*A)
        for mesh in (256,4096):
            row = h.witness_packets(xs,D,A,mesh)
            self.assertEqual(row['ordered_exclusions'],2*A*(row['depth']+1))
            pairs = set()
            for r in row['witnesses']:
                for j in range(r['packet_size']):
                    n = r['packet_start']+j
                    pair = (n,n+r['lag'])
                    self.assertNotIn(pair,pairs)
                    pairs.add(pair)
                    self.assertGreater(mesh*h.distance_numerator(xs[pair[1]-1]-xs[n-1],D),D)

    def test_integer_no_wrap_lock_threshold(self):
        self.assertLess(F(17,32),1)
        # Nearest-integer differences cannot be nonzero under this budget.
        for e0 in (F(-1,32),F(0),F(1,32)):
            for e1 in (F(-1,32),F(0),F(1,32)):
                self.assertLess(abs(16*e0-e1),1)

    def test_cylinder_mirror_endpoint_ownership(self):
        for depth in (1,2,3):
            B = 16**depth
            for a in (0,1,B//16,B-1):
                lo,hi,D = h.mirror_cylinder(a,depth)
                self.assertEqual(D,B)
                self.assertEqual((F(1,16)-F(a,B))%1,F(hi,B)%1)
                middle = F(2*a+1,2*B)
                reflected = (F(1,16)-middle)%1
                self.assertEqual((B*reflected).__floor__(),lo%B)
                self.assertEqual((F(1,16)-F(a+1,B))%1,F(lo,B)%1)

    def test_actual_cylinder_carry_transition_and_boundaries(self):
        for n,x in enumerate([F(0)]+h.phases(96)):
            for depth in (1,2):
                a,carry,b = h.literal_carry_relation(x,n,depth)
                B = 16**depth
                self.assertEqual(b,(16*a+carry)%B)
        for x in (F(0),F(1,16),F(15,16)):
            h.literal_carry_relation(x,64,1)


class HostileControls(unittest.TestCase):
    def test_coherent_changed_seed_paid_by_original_tail_bracket(self):
        # T_n is not replaced by rational pi: use its exact finite source bounds.
        for n in (64,128,256):
            partial = sum((h.source(n+j)/16**j for j in range(1,9)),F(0))
            upper = partial+h.source(n+9)/(15*16**8)
            self.assertTrue(0 < partial < upper < F(1,64*n*n))
            for m in (16,64):
                self.assertEqual(((F(1,5)-upper)*m).__floor__(),(F(1,5)*m).__floor__())
            self.assertLess(upper,F(1,8*64))

    def test_delta_zero_fifteenth_roots_and_mirror_resonance(self):
        roots = [F(k,15) for k in range(15)]
        self.assertEqual(roots,[(16*x)%1 for x in roots])
        self.assertTrue(all((15*x)%1 == 0 for x in roots))
        self.assertGreater(w.mirror_wasserstein(list(range(15)),15),0)
        self.assertEqual(w.mirror_wasserstein([0]*7,1),F(1,16))
        for frequency in (16,32,256,4096):
            self.assertEqual(F(frequency,16)%1,0)
            g,v = w.primitive_frequency(frequency)
            self.assertNotEqual(g%16,0)
            self.assertEqual(g*16**v,frequency)

    def test_conjugate_pair_is_not_antipodal(self):
        # e(1/6)+e(-1/6)=1 by the cyclotomic relation z^2-z+1=0.
        cost = w.antiphase_matching_cost([1,5],6)
        self.assertEqual(cost,F(1,6))
        self.assertNotEqual(cost,0)
        self.assertEqual(w.antiphase_matching_cost([0,1],2),0)

    def test_finite_history_mutant_changes_completion(self):
        L = 24
        prefix = sum((h.source(n)/16**n for n in range(1,L+1)),F(0))
        completion = prefix+h.source(L)/(31*16**L)
        self.assertIsInstance(completion,F)
        # Tail r(L)/2^(n-L) is positive decreasing and rationally completed.
        self.assertNotEqual(h.source(L+1),h.source(L)/2)
        U = F(0)
        for n in range(1,L+1):
            U = 16*U+h.source(n)
        self.assertEqual(U/16**L,prefix)

    def test_original_real_cofactor_then_hostile_prime_free_lock(self):
        p,Q = 41,1009
        source_states = h.phases(15)
        locked = []
        for n in range(8,16):
            a = 4*pow(16,n-6,p)%p
            C = source_states[n-1]-F(a,p)
            self.assertEqual(gcd(C.denominator,p),1)
            nearest = (F(Q*a,p)+F(1,2)).__floor__()
            fake_C = F(-nearest,Q)
            self.assertEqual(gcd(fake_C.denominator,p),1)
            locked.append(F(a,p)+fake_C)
        self.assertTrue(all(abs(x)<=F(1,2*Q) for x in locked))
        self.assertTrue(all(abs(x-y)<F(1,64) for x in locked for y in locked))
        self.assertNotEqual([x%1 for x in locked],source_states[7:15])

    def test_psd_is_not_pointwise_positive(self):
        matrix = [[1,-1],[-1,1]]
        self.assertEqual(sum(map(sum,matrix)),0)
        self.assertEqual(matrix[0][0],1)
        for a,b in ((1,1),(1,0),(-2,3)):
            self.assertEqual(a*a-2*a*b+b*b,(a-b)**2)

    def test_original_source_refutes_deterministic_iid_mean_ceiling(self):
        # Preregistered development falsifier; not an asymptotic claim.
        D, xs = w.odd_modular_lift(511)
        counts,E = w.energy(xs[255:511],D,8)
        self.assertEqual(counts,[33,28,42,28,36,36,26,27])
        self.assertEqual(E,F(4209,4096))
        self.assertGreater(E,1+F(7,256))

    def test_validation_rejects_wrong_domains(self):
        for call in (lambda:list(h.full_source(-1)),lambda:h.source(0),
                     lambda:h.slow_mesh(3),lambda:h.shell_bound(32,32),
                     lambda:h.shell_bound(64,128),lambda:h.packet_depth(0,4),
                     lambda:h.mirror_cylinder(16,1)):
            with self.assertRaises(ValueError):
                call()


if __name__ == '__main__':
    unittest.main()
