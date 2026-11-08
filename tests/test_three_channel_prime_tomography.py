"""Exact three-channel p-primary residue and hostile shadow regression tests."""
import cmath
import unittest
from fractions import Fraction as F
from observational_succ.three_channel_prime_tomography import (
    channel_forcing, channel_states, stage_vectors, valid_clock, birth_times,
    reduce_fraction, predicted_residues, direct_residues, multiplicative_order_16,
    mode_coefficients, mode_resonance_mass, shell_residue_histogram,
    predicted_histogram, subgroup_delta, local_phase_gram,
    prime_frame_target, root_harmonic_forcing,
)


class PrimeChannelTomography(unittest.TestCase):
    def test_exact_three_positive_forcings(self):
        for n in range(1,70):
            a=8*n-7
            self.assertEqual(root_harmonic_forcing(n),
                             F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5))
            self.assertTrue(all(q > 0 for q in channel_forcing(n)))
            self.assertEqual(sum(channel_states(n)),
                             16*sum(channel_states(n-1))+root_harmonic_forcing(n))

    def test_three_first_shell_stage_vectors(self):
        self.assertEqual(stage_vectors(0), (
            (F(2),F(1),F(1)),
            (F(3,2),F(1),F(1)),
            (F(3,2),F(4,5),F(1)),
            (F(3,2),F(4,5),F(5,6)),
        ))
        self.assertEqual(tuple(sum(x) for x in stage_vectors(0)),
                         (F(4),F(7,2),F(33,10),F(47,15)))
        for r in range(8):
            self.assertEqual(sum(stage_vectors(r)[-1]), sum(channel_states(r+1)))

    def test_stage_rank_growth(self):
        # The first three chronological events already span the full channel space.
        # det[(2,1,1),(-2/(8r+4),0,0),(0,-1/(8r+5),0)]>0.
        for r in range(10):
            self.assertEqual(F(2,(8*r+4)*(8*r+5)) > 0, True)
            v1,v2,v3,v4=stage_vectors(r)
            self.assertEqual(tuple(v2[i]-v1[i] for i in range(3)),
                             (F(-2,8*r+4),F(0),F(0)))
            self.assertEqual(tuple(v3[i]-v2[i] for i in range(3)),
                             (F(0),F(-1,8*r+5),F(0)))
            self.assertEqual(tuple(v4[i]-v3[i] for i in range(3)),
                             (F(0),F(0),F(-1,8*r+6)))

    def test_prime_births_and_exact_lag_alignment(self):
        for p in (17,41,73,89,97,113,137,193):
            k=valid_clock(p)
            self.assertEqual(pow(16,k,p),1)
            self.assertEqual(k % multiplicative_order_16(p),0)
            for r in (0,k-1):
                b=birth_times(p,r)
                self.assertEqual(tuple(t-b[0] for t in b), (0,3*k,4*k,5*k))
                self.assertEqual(birth_times(p,r)[0]+p,
                                 k+1+(r+1)*p)
            with self.assertRaises(ValueError):valid_clock(p,k)

    def test_independent_original_prime_oracle(self):
        for p in (17,41,73,89,97,113):
            k=valid_clock(p)
            base=k+1
            for r in (0,min(1,k-1),k-1):
                for t in sorted(set((0,1,3*k-1,3*k,4*k-1,4*k,
                                     5*k-1,5*k,8*k-1,8*k))):
                    n=base+r*p+t
                    self.assertEqual(predicted_residues(p,n),direct_residues(p,n),
                                     (p,r,t))

    def test_every_term_of_exact_four_stage_character_histogram(self):
        # Independent source-event recurrence vs exact subgroup orbit multiplicities.
        modes=((1,1,1),(0,1,-1),(1,-2,0),(1,0,0),(2,-1,3))
        for p,r in ((17,0),(41,0),(41,2),(73,1)):
            for mode in modes:
                self.assertEqual(predicted_histogram(p,r,1,mode),
                                 shell_residue_histogram(p,r,1,mode),(p,r,mode))

    def test_exact_resonance_planes(self):
        self.assertEqual(mode_resonance_mass((0,0,0)),1)
        self.assertEqual(mode_resonance_mass((1,1,1)),0)
        self.assertEqual(mode_resonance_mass((0,1,-1)),F(1,2))
        self.assertEqual(mode_resonance_mass((1,-2,0)),F(3,8))
        self.assertEqual(mode_resonance_mass((-1,-1,-1)),0)
        for p in (17,41,73):
            self.assertEqual(mode_coefficients(p,0,1,(1,1,1)),
                             tuple(reduce_fraction(v,p) for v in (F(4), F(7,2),
                                                                   F(33,10),F(47,15))))

    def test_prime_phase_gram_quantitative_delta_bound(self):
        for p in (41,73,97,137):
            gram=local_phase_gram(p)
            eps=subgroup_delta(p)+1/p+1e-11
            for i in range(3):
                self.assertAlmostEqual(gram[i][i].real,1,places=11)
                self.assertLess(abs(gram[i][i].imag),1e-11)
                for j in range(3):
                    self.assertLess(abs(gram[i][j]-gram[j][i].conjugate()),1e-11)
                    if i!=j:
                        target=(p-1)/(2*p) if {i,j}=={1,2} else 0
                        self.assertLessEqual(abs(gram[i][j]-target),eps)
            self.assertEqual(prime_frame_target(),
                             ((1.,0.,0.),(0.,1.,0.5),(0.,0.5,1.)))

    def test_source_mutation_and_rational_seed_controls(self):
        for p in (17,41,73):
            k=(p-1)//8
            self.assertEqual(direct_residues(p,k), (0,0,0))
            # A source mutant with Q+e^-6x(1-e^-x)^3 matches first TWO
            # Gamma jets but injects +3/p at arithmetic time j=k.
            a=8*k-7
            mutation=F(1,a+6)-F(3,a+7)+F(3,a+8)-F(1,a+9)
            mutant_injection=reduce_fraction(p*mutation,p)
            self.assertEqual(mutant_injection,3 % p)
            # An additive rational p-unit seed changes real phase but NOT pV modp.
            s=F(1,7)
            self.assertNotEqual((16**(k+1)*s) % 1,0)
            self.assertEqual(reduce_fraction(p*16**(k+1)*s,p),0)

    def test_coherent_complement_refutes_gram_to_weyl_shortcut(self):
        p=73;k=(p-1)//8
        total=[sum(direct_residues(p,n))%p for n in range(k+1,k+1+p)]
        a=[cmath.exp(2j*cmath.pi*v/p) for v in total]
        b=[z.conjugate() for z in a]
        self.assertAlmostEqual(abs(sum(x*y for x,y in zip(a,b))/p),1,places=12)
        # This is a signed *complement chosen to cancel*, not authentic U0=0.
        self.assertGreater(abs(sum(a)/p-1),0.01)

    def test_invalid_boundary_and_no_prime_power_claim(self):
        with self.assertRaises(ValueError):valid_clock(19)
        with self.assertRaises(ValueError):valid_clock(9)
        with self.assertRaises(ValueError):predicted_residues(17,37)
        with self.assertRaises(ValueError):reduce_fraction(F(1,17),17)
        with self.assertRaises(ValueError):mode_coefficients(17,0,1,(1,2))


if __name__=='__main__':
    unittest.main()
