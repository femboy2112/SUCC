"""Independent exact BBP pole, CRT, prime-clock and signed-control checks."""
import cmath
import math
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_source_memory import forcing, forced_step
from observational_succ.bbp_cyclotomic_birth import (
    birth_index, first_phase_residue, next_pole_gap, pole_denominators,
    p_adic_valuation, p_primary_phase, forced_states, multiplicative_order_16,
    first_window_residues, full_cycle_count, cyclic_autocorrelation_residues,
    galois_mean_squared, source_window_split, within_block_complement_variation,
    construct_coprime_clock_counterfeit,
    counterfeit_upper, exceptional_prime_count_bound,
)


def primes_under(stop):
    return [p for p in range(3,stop,2)
            if all(p%d for d in range(3,math.isqrt(p)+1,2))]


def primitive_sum(residues,p):
    return sum((cmath.exp(2j*math.pi*a/p) for a in residues),0j)


class BBPCyclotomicBirthTest(unittest.TestCase):
    def test_independent_source_formula_and_pole_births(self):
        for n in range(1,150):
            self.assertEqual(forcing(n),Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))
        for p in primes_under(501):
            n=birth_index(p); gap=next_pole_gap(p)
            for k in range(1,n):
                self.assertTrue(all(d%p for d in pole_denominators(k)),(p,k))
            self.assertTrue(any(d%p==0 for d in pole_denominators(n)),p)
            self.assertEqual(p_adic_valuation(forcing(n),p),-1)
            self.assertEqual((p*forcing(n)).numerator*pow((p*forcing(n)).denominator,-1,p)%p,
                             first_phase_residue(p))
            for k in range(n+1,n+gap):
                self.assertTrue(all(d%p for d in pole_denominators(k)),(p,k))
            self.assertTrue(any(d%p==0 for d in pole_denominators(n+gap)),(p,gap))

    def test_actual_rational_succ_orbit_retains_prime_phase(self):
        states=forced_states(250)
        for p in primes_under(401):
            n=birth_index(p); gap=next_pole_gap(p)
            residues=first_window_residues(p)
            self.assertEqual(len(residues),gap)
            for t in range(gap):
                if n+t>250:break
                y=states[n+t-1]
                self.assertEqual(p_primary_phase(y,p),residues[t],(p,t))
                q_other=(y-Q(residues[t],p))%1
                self.assertNotEqual(q_other.denominator%p,0,(p,t))

    def test_complete_split_gaussian_windows(self):
        for p in (17,41,73,89,97,113,137,193,233,241,257):
            if p%8!=1:continue
            d=next_pole_gap(p); L=multiplicative_order_16(p)
            self.assertEqual(pow(16,(p-1)//8,p),1)
            self.assertEqual(d%L,0)
            self.assertGreaterEqual(full_cycle_count(p),3)
            self.assertEqual(first_window_residues(p),
                             tuple(4*pow(16,j%L,p)%p for j in range(d)))
            # Classical Gauss character decomposition; numerical test is
            # a regression oracle, never the proof of the universal bound.
            value=primitive_sum(first_window_residues(p),p)
            self.assertLessEqual(abs(value),d/L*math.sqrt(p)+1e-7)

    def test_cyclotomic_lag_resonance_and_classical_gauss_bound(self):
        for p in (17,41,73,97,113,137,193):
            d=next_pole_gap(p);L=multiplicative_order_16(p)
            self.assertEqual(cyclic_autocorrelation_residues(p,L),tuple(0 for _ in range(d)))
            for lag in range(1,min(8,L)):
                self.assertNotEqual((pow(16,lag,p)-1)%p,0)
                vals=cyclic_autocorrelation_residues(p,lag)
                self.assertEqual(vals,
                    tuple((first_window_residues(p)[j+lag]
                         -first_window_residues(p)[j])%p
                         for j in range(d-lag))+
                    tuple((4*pow(16,j,p)*(pow(16,lag,p)-1))%p
                         for j in range(d-lag,d)))
                self.assertLessEqual(abs(primitive_sum(vals,p)),d/L*math.sqrt(p)+1e-7)
                truncated=primitive_sum(vals[:d-lag],p)
                self.assertLessEqual(abs(truncated),d/L*math.sqrt(p)+lag+1e-7)

    def test_galois_rms_identity_by_independent_ramanujan_oracle(self):
        for p in (17,41,73,97,113,137):
            entries=first_window_residues(p)
            ramanujan=Q(sum((p-1 if (x-y)%p==0 else -1)
                              for x in entries for y in entries),p-1)
            self.assertEqual(galois_mean_squared(p),ramanujan)

    def test_actual_cross_prime_twists_not_automatically_slow(self):
        states=forced_states(100)
        for p in (17,41,73,97):
            n=birth_index(p);d=next_pole_gap(p)
            complement=[]
            for j in range(d):
                r=first_window_residues(p)[j]
                v=(states[n+j-1]-Q(r,p))%1
                self.assertNotEqual(v.denominator%p,0)
                complement.append(v)
            variation=sum((min((complement[t]-complement[t-1])%1,
                               (complement[t-1]-complement[t])%1)
                           for t in range(1,d)),Q())
            self.assertGreater(variation,0)

    def test_source_window_exact_split_and_twisted_lag(self):
        for p in (17,41,73,97):
            m=(p-1)//8; split=source_window_split(p)
            self.assertEqual(len(split),3*m)
            states=forced_states(4*m)
            L=multiplicative_order_16(p)
            for j,(residue,rest) in enumerate(split):
                self.assertEqual((Q(residue,p)+rest)%1,states[m+j])
                self.assertEqual(residue,4*pow(16,j,p)%p)
                if j+1 < 3*m:
                    self.assertEqual(split[j+1][1],
                                     (16*rest+forcing(m+j+2))%1)
            for d in range(1,min(L,4)):
                for j in range(3*m-d):
                    u,v=split[j],split[j+d]
                    true=(states[m+j+d]-states[m+j])%1
                    p_part=Q((v[0]-u[0])%p,p)
                    rest=(v[1]-u[1])%1
                    self.assertEqual((p_part+rest)%1,true)
            self.assertGreater(within_block_complement_variation(p),0)

    def test_coprime_clock_resonance_countermodel(self):
        for p in (17,41,73):
            horizon=next_pole_gap(p)
            phase,q=construct_coprime_clock_counterfeit(p,horizon)
            self.assertEqual(p_primary_phase(phase,p),first_phase_residue(p))
            self.assertEqual(q%2,1)
            self.assertLess(counterfeit_upper(horizon,q),Q(1,100))
            actual=sum((cmath.exp(2j*math.pi*float((16**t*phase)%1))
                        for t in range(horizon)),0j)
            self.assertLess(abs(actual-horizon),float(counterfeit_upper(horizon,q))+1e-8)
            self.assertGreater(abs(actual),horizon-float(counterfeit_upper(horizon,q))-1e-8)

    def test_prime_order_sparse_exception_certificate(self):
        for X in (10,50,100,1000,5000):
            bad=sum(multiplicative_order_16(p)**3<=p for p in primes_under(X+1))
            self.assertLessEqual(bad,exceptional_prime_count_bound(X))

    def test_reject_false_sources_and_out_of_scope(self):
        for candidate in (1,2,4,9,15,21,49,True,-3):
            with self.assertRaises(ValueError):birth_index(candidate)
        with self.assertRaises(ValueError):p_primary_phase(Q(1,7),17)
        with self.assertRaises(ValueError):cyclic_autocorrelation_residues(7,1)
        with self.assertRaises(ValueError):galois_mean_squared(5)
        with self.assertRaises(ValueError):p_adic_valuation(0,17)

if __name__=='__main__':unittest.main()
