import unittest
from fractions import Fraction as Q

from observational_succ.arithmetic_tfd import (
    ArithmeticTFDError, Gaussian, thermal_amplitudes, norm_squared,
    reduced_probabilities, mirror_residual, residual_squared,
    thermal_cutoff_residual, thermal_tail_bound, interior_mirror_defects,
    reconstruct_smooth_prefix, pure_overlap_squared, probe,
    finite_prime_kernel_projection_squared, finite_mirror_gap_certificate,
    thermal_mirror_fidelity_certificate,
)
from observational_succ.unit_prime_succ import prime_smooth, prime_list


class ArithmeticTFDTests(unittest.TestCase):
    def test_partial_trace_independent_double_sum(self):
        a = thermal_amplitudes(8)
        z = norm_squared(a)
        # Trace_R |psi><psi| directly; off-diagonal terms require same R index.
        rho = {(i,j): sum((a[i]*a[j].conjugate()/z
                          for k in range(1,9) if i == k and j == k), Gaussian())
               for i in a for j in a}
        self.assertEqual(sum((rho[i,i].real for i in a), Q()), 1)
        self.assertTrue(all(not rho[i,j].norm_squared() for i in a for j in a if i != j))
        self.assertEqual({i: rho[i,i].real for i in a}, reduced_probabilities(a))

    def test_sparse_operator_vs_independent_tail_formula(self):
        for p in (2,3,5,7):
            for s in (1,2,3):
                for n in (1,2,3,6,7,12,19,35):
                    a = thermal_amplitudes(n,s)
                    self.assertEqual(residual_squared(a,p,p**s), thermal_cutoff_residual(n,p,s))
                    self.assertLessEqual(thermal_cutoff_residual(n,p,s), thermal_tail_bound(n,p,s))

    def test_cutoff_oscillation_and_compression_false_positive(self):
        self.assertEqual(thermal_cutoff_residual(2,2), Q(1,5))
        self.assertEqual(thermal_cutoff_residual(3,2), Q(13,49))
        self.assertGreater(thermal_cutoff_residual(3,2), thermal_cutoff_residual(2,2))
        a = thermal_amplitudes(17)
        self.assertGreater(residual_squared(a,3,3), 0)
        self.assertEqual(residual_squared(a,3,3,output_cutoff=17), 0)

    def test_composite_amplitude_mutation(self):
        a = thermal_amplitudes(42)
        a[6] = 2*a[6]
        self.assertEqual(set(interior_mirror_defects(a,2,2)), {3,6})
        self.assertEqual(set(interior_mirror_defects(a,3,3)), {2,6})
        # Any prime p sees the mutated a_6 in equation n=6 if 6p is observed.
        self.assertEqual(set(interior_mirror_defects(a,5,5)), {6})
        self.assertEqual(set(interior_mirror_defects(a,7,7)), {6})
        self.assertEqual(a[2], Gaussian(Q(1,2)))
        self.assertEqual(a[3], Gaussian(Q(1,3)))

    def test_complex_rigidity_and_phase_blind_marginals(self):
        cs = {2: Gaussian(0,2), 3: Gaussian(3)}
        a = reconstruct_smooth_prefix(cs,72)
        b = reconstruct_smooth_prefix({2:2,3:3},72)
        for p,c in cs.items():
            self.assertEqual(interior_mirror_defects(a,p,c), {})
        self.assertEqual(reduced_probabilities(a), reduced_probabilities(b))
        self.assertLess(pure_overlap_squared(a,b), 1)
        self.assertNotEqual(interior_mirror_defects(a,2,2), {})

    def test_independent_existing_prime_source_oracle(self):
        ps = prime_list(11)
        a = reconstruct_smooth_prefix({p:p for p in ps},100)
        self.assertEqual({n:v.real for n,v in a.items()}, prime_smooth(ps,100,1))

    def test_finite_prime_probe_closure_failure(self):
        # Exact finite coefficients of a global {2,3}-smooth state: p=5 fails.
        a = reconstruct_smooth_prefix({2:2,3:3},60)
        self.assertEqual(interior_mirror_defects(a,2,2), {})
        self.assertEqual(interior_mirror_defects(a,3,3), {})
        self.assertIn((5,1), mirror_residual(a,5,5))

    def test_identity_zero_and_orientation_controls(self):
        a = thermal_amplitudes(12)
        self.assertEqual(pure_overlap_squared(a,a),1)
        self.assertNotEqual(interior_mirror_defects(a,2,Q(1,2)), {})
        with self.assertRaises(ArithmeticTFDError):
            reduced_probabilities({1:0})
        with self.assertRaises(ArithmeticTFDError):
            reconstruct_smooth_prefix({2:0},10)

    def test_typed_source_and_composite_controls(self):
        for bad in (True,2.0,6,1):
            with self.assertRaises(ArithmeticTFDError):
                residual_squared(thermal_amplitudes(8),bad,2)
        for bad in (True,0.5,complex(1,2)):
            with self.assertRaises(ArithmeticTFDError):
                Gaussian(bad)
        self.assertFalse(probe()["infinite_theorem_by_tests"])

    def test_weighted_transpose_mirror_orientation(self):
        # beta=2: D_nn is proportional to 1/n. X maps input i to output j;
        # M=D X^T D^-1 maps j to i with coefficient j/i.
        for i,j in ((1,2),(2,1),(7,8),(13,64),(21,1024)):
            mirror = Q(j,i)
            self.assertEqual(Q(1,i), mirror*Q(1,j))
            if i != j:
                self.assertNotEqual(Q(1,i), Q(i,j)*Q(1,j))
        # Small-index input -> exponentially large output is the unbounded
        # mirror direction; reversing X gives the reciprocal coefficients.
        ratios = [Q(2**k,2*k+1) for k in range(3,11)]
        self.assertTrue(all(a < b for a,b in zip(ratios,ratios[1:])))
        self.assertGreater(ratios[-1],40)

    def test_finite_matrix_unit_kms_and_modular_signs(self):
        for s in (1,2,3):
            w=reduced_probabilities(thermal_amplitudes(7,s))
            for i in w:
                for j in w:
                    # phi(e_ij alpha_(i beta)(e_ji)) = phi(e_ji e_ij).
                    imaginary_time_factor=Q(i,j)**(2*s)
                    self.assertEqual(w[i]*imaginary_time_factor,w[j])
                    # Delta|i,j>=(w_i/w_j)|i,j>; J swaps i,j.
                    delta=w[i]/w[j]
                    self.assertEqual(delta,Q(j,i)**(2*s))
                    self.assertEqual(delta*(w[j]/w[i]),1)
                    if i!=j:
                        self.assertNotEqual(w[i]/imaginary_time_factor,w[j])

    def test_no_signaling_requires_complete_instrument(self):
        a = thermal_amplitudes(18)
        w = reduced_probabilities(a)
        # A right-side measurement with K0=V_p*, K1=I-P_p obeys
        # K0* K0 + K1* K1=I. Keep the original left index in each branch.
        p = 3
        success = {n: q if n % p == 0 else Q() for n,q in w.items()}
        failure = {n: q if n % p else Q() for n,q in w.items()}
        self.assertEqual({n: success[n]+failure[n] for n in w},w)
        probability = sum(success.values(),Q())
        self.assertGreater(probability,0)
        self.assertLess(probability,1)
        conditioned = {n:q/probability for n,q in success.items()}
        self.assertNotEqual(conditioned,w)
        # Conditioned change is allowed only with the measured success flag.
        self.assertEqual(sum(conditioned.values(),Q()),1)

    def test_infinite_kernel_projection_gap(self):
        # Vacuum projection onto one geometric kernel has mass1−1/c².
        self.assertEqual(finite_prime_kernel_projection_squared({1:1},{2:2}),Q(3,4))
        self.assertEqual(finite_prime_kernel_projection_squared({1:1},{2:2,3:3}),Q(2,3))
        sources = ({1:1},{1:1,2:2,3:Gaussian(0,1)},thermal_amplitudes(23))
        for a in sources:
            for cs in ({2:2},{3:Q(3,2)},{2:2,3:3},{2:2,3:3,5:5}):
                c = finite_mirror_gap_certificate(a,cs)
                self.assertGreaterEqual(c["distance_squared"],0)
                self.assertGreaterEqual(c["slack"],0)
        # Compressed zero residual cannot replace the full operator energy:
        a=thermal_amplitudes(7)
        self.assertEqual(residual_squared(a,2,2,output_cutoff=7),0)
        self.assertGreater(finite_mirror_gap_certificate(a,{2:2})["distance_squared"],0)

    def test_weighted_mirrors_certify_infinite_fidelity(self):
        for n,s in ((20,1),(40,1),(16,2)):
            a=thermal_amplitudes(n,s)
            cert=thermal_mirror_fidelity_certificate(a,n,s)
            self.assertGreater(cert["fidelity_lower"],0)
            # Independent infinite target fidelity is Z_N/zeta(2s).
            # zeta>Z_N+sum_{n<N'<=2N}N'^(-2s), giving a rigorous upper
            # fidelity bound with which the mirror lower must agree.
            z=norm_squared(a)
            z2=norm_squared(thermal_amplitudes(2*n,s))
            self.assertLessEqual(cert["fidelity_lower"],z/z2)
        self.assertGreater(thermal_mirror_fidelity_certificate(
            thermal_amplitudes(100),100)["fidelity_lower"],Q(9,10))
        self.assertGreater(thermal_mirror_fidelity_certificate(
            thermal_amplitudes(16,2),16,2)["fidelity_lower"],Q(99,100))
        with self.assertRaises(ArithmeticTFDError):
            thermal_mirror_fidelity_certificate({1:1,100:1},10)
        with self.assertRaises(ArithmeticTFDError):
            finite_mirror_gap_certificate({1:1},{2:1})


if __name__ == "__main__":
    unittest.main()
