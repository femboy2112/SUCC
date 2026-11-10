"""Exact regression and countermodel tests for source-clock and REAL matrices."""
import unittest
from fractions import Fraction
from math import isclose
from observational_succ.bbp_spectral_gamma import (
    transition_counts,margins,energies,difference_counts,opposite_frequency_energy,
    empirical_transition,haar_matrix,time_spatial_map,time_spatial_permutation,
    permutation_clock,root_of_unity_eigenvector,nilpotent_nonhaar_matrix,
    matmul,nonhaar_markov_pair_energy,harmonic_finite_part,dobrushin_coefficient)
from observational_succ.bbp_spatial_haar_lift import (
    first_spatial_digit,two_spatial_digits_from_first,bulk_pi_hex_digits)

class TestPiSpectralGamma(unittest.TestCase):
    def test_counts_linear_no_wrap(self):
        c=transition_counts('01230')
        self.assertEqual([c[0][1],c[1][2],c[2][3],c[3][0]],[1,1,1,1]);self.assertEqual(sum(map(sum,c)),4)

    def test_cyclic_exact_one_new_edge(self):
        s='01230';a=transition_counts(s);b=transition_counts(s,cyclic=True)
        self.assertEqual(sum(map(sum,b)),5);self.assertEqual(b[0][0]-a[0][0],1)

    def test_endpoint_flow(self):
        s='2C019ABC8';c=transition_counts(s);r,col=margins(c)
        self.assertEqual([r[j]-col[j] for j in range(16)],[(j==2)-(j==8) for j in range(16)])

    def test_cyclic_flow(self):
        c=transition_counts('2C019ABC8',cyclic=True);r,col=margins(c)
        self.assertEqual(r,col)

    def test_uniform_one_step_Haar(self):
        c=tuple(tuple(1 for _ in range(16)) for _ in range(16))
        self.assertEqual(energies(c),(0,0,0,0))
        self.assertEqual(opposite_frequency_energy(c),0)

    def test_spatial_temporal_nibble_cycle(self):
        d=0;orbit=[]
        for _ in range(16):orbit.append(d);d=time_spatial_map(d)
        self.assertEqual(d,0);self.assertEqual(len(set(orbit)),16)
        self.assertEqual(tuple(orbit),tuple(first_spatial_digit(i) for i in range(16)))

    def test_clock_eigencharacters(self):
        for h in range(16):
            v=root_of_unity_eigenvector(h)
            for d in range(16):
                self.assertEqual(v[time_spatial_map(d)]%16,(v[d]+h)%16)

    def test_spatial_pair_Haar_exact(self):
        pairs=[two_spatial_digits_from_first(d,t) for d in range(16) for t in range(16)]
        self.assertEqual(len(set(pairs)),256)
        self.assertEqual({a for a,b in pairs},set(range(16)))

    def test_temporal_permutation_not_pair_Haar(self):
        c=time_spatial_permutation()
        self.assertEqual(energies(c),(0,0,15,15))
        self.assertEqual(empirical_transition(c),tuple(tuple(Fraction(x) for x in row) for row in c))

    def test_parity_mode_exact_minus_one(self):
        for d in range(16):
            self.assertEqual((-1)**d,-(-1)**time_spatial_map(d))

    def test_nilpotent_positive_bistochastic(self):
        P=nilpotent_nonhaar_matrix();J=haar_matrix()
        self.assertNotEqual(P,J)
        self.assertTrue(all(x>0 for row in P for x in row))
        for a in range(16):self.assertEqual(sum(P[a]),1)
        for b in range(16):self.assertEqual(sum(P[a][b] for a in range(16)),1)

    def test_nilpotent_Haar_eigenvalues_but_nonHaar(self):
        P=nilpotent_nonhaar_matrix();J=haar_matrix()
        self.assertEqual(matmul(P,P),J)
        self.assertEqual(nonhaar_markov_pair_energy(),Fraction(3,1024))
        # (P-J)^2=0 with (P-J) nonzero; all nontrivial eigenvalues zero.
        K=tuple(tuple(P[i][j]-J[i][j] for j in range(16)) for i in range(16))
        self.assertEqual(matmul(K,K),tuple(tuple(Fraction(0) for j in range(16)) for i in range(16)))

    def test_anti_character_perfect_difference(self):
        c=transition_counts('000000')
        self.assertEqual(opposite_frequency_energy(c),15)
        self.assertEqual(difference_counts(c)[0],5)

    def test_anti_energy_not_same_as_two_digit_energy(self):
        c=transition_counts('0123456789ABCDEF',cyclic=True)
        self.assertEqual(energies(c),(0,0,15,15))
        # All consecutive digit differences lie in 2 residues (negative increments), not uniform.
        self.assertGreater(opposite_frequency_energy(c),0)

    def test_energies_nonnegative_for_small_sequences(self):
        for s in ['01230123','0011223344556677','ABCDEF00000000']:
            self.assertGreaterEqual(energies(transition_counts(s))[-1],0)

    def test_authenticated_bbp_first_hex(self):
        self.assertEqual(bulk_pi_hex_digits(64,12),
                         '243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89')

    def test_dobrushin_exact(self):
        c=tuple(tuple(1+(a==b) for b in range(16)) for a in range(16))
        self.assertEqual(dobrushin_coefficient(c),Fraction(1,17))

    def test_dobrushin_source_time_cycle(self):
        self.assertEqual(dobrushin_coefficient(time_spatial_permutation()),1)

    def test_harmonic_not_derived_from_pi(self):
        self.assertGreater(harmonic_finite_part(16),harmonic_finite_part(256))
        self.assertTrue(isclose(harmonic_finite_part(256),0.5791675183377176,rel_tol=0,abs_tol=1e-12))

if __name__=='__main__':unittest.main()
