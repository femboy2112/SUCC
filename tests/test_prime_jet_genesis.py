"""Exact finite source-bound prime-jet tests. No RH or global sign claim."""
import unittest
from fractions import Fraction as F
from observational_succ.prime_jet_genesis import (
    JetSource, SourceError, affine_braid_defects, convolution_log,
    convolution_words, counting_measure, direct_word_oracle,
    expected_prime_power_measure, first_archimedean_cell,
    fucc_path_receipt, prime_power_jets, rediscover_generators,
)


# Independent elementary primality oracle is used ONLY by the calibration tests.
def calibration_primes(limit):
    return [i for i in range(2, limit+1)
            if all(i % d for d in range(2, int(i**0.5)+1))]


def source(quantities, horizon):
    return JetSource(tuple((f'abstract_{i}', q)
                           for i, q in enumerate(quantities)), F(horizon))


class GenesisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.primes = calibration_primes(30)
        cls.valid = source(cls.primes, 30)
        cls.counts = counting_measure(cls.valid)

    def test_reconstruct_without_integer_successor(self):
        self.assertEqual(self.counts, {F(n): F(1) for n in range(1,31)})
        self.assertEqual(self.counts, direct_word_oracle(self.valid))

    def test_symbolic_word_counts_not_numerical_collisions(self):
        words = convolution_words(self.valid)
        self.assertEqual(set(words.values()), {F(1)})
        self.assertEqual(len(words),30)
        self.assertEqual(self.valid.word_size(self.valid.vacuum),1)

    def test_prime_power_log_and_inverse_convolution(self):
        jets = prime_power_jets(self.valid)
        self.assertEqual(jets[(2,)+(0,)*9], F(1,2))
        log = convolution_log(self.counts)
        self.assertEqual(log,expected_prime_power_measure(self.valid))
        self.assertEqual(log[F(4)], F(1,2))
        self.assertEqual(log[F(6)] if F(6) in log else F(0),F(0))

    def test_recover_generators_from_masses(self):
        self.assertEqual(rediscover_generators(self.counts), tuple(map(F,self.primes)))

    def test_finite_rank_braid_positive(self):
        tested, failures=affine_braid_defects(self.valid,self.counts)
        self.assertGreater(tested,25)
        self.assertFalse(failures)
        self.assertEqual(first_archimedean_cell(self.counts),1)

    def test_unit_to_prime_path_cost_independent_of_energy(self):
        a = (0,0,0,1)+(0,)*6  # 7
        b = (3,)+(0,)*9      # 8
        receipt = fucc_path_receipt(self.valid,a,b)
        self.assertEqual(receipt['ratio'],'8/7')
        self.assertEqual(receipt['minimum_fucc_edges'],4)
        self.assertEqual(receipt['meet'],'1')

    def test_prime_power_successor_path_cost_grows(self):
        # Genuine successor 2^k-1 -> 2^k: coprime. FUCC cost >= k.
        large = source(calibration_primes(31), 32)
        # Independently factor 31, and create the pure 2^5 word.
        labels = [i for i,p in enumerate(calibration_primes(31)) if p==31]
        v31 = tuple(1 if i == labels[0] else 0 for i in range(len(large.generators)))
        v32 = tuple(5 if i==0 else 0 for i in range(len(large.generators)))
        receipt=fucc_path_receipt(large,v31,v32)
        self.assertEqual(receipt['ratio'],'32/31')
        self.assertEqual(receipt['minimum_fucc_edges'],6)

    def test_fake_composite_is_not_an_independent_prime(self):
        fake=source(self.primes+[6],30)
        mass=counting_measure(fake)
        self.assertEqual(mass[F(6)],2)
        self.assertEqual(mass, direct_word_oracle(fake))
        self.assertEqual(convolution_log(mass),expected_prime_power_measure(fake))
        self.assertEqual(convolution_log(mass)[F(6)],1)
        self.assertIn(F(6),rediscover_generators(mass))
        with self.assertRaises(SourceError):
            affine_braid_defects(fake,mass)

    def test_missing_generator_removes_atoms(self):
        incomplete=source([p for p in self.primes if p!=5],30)
        mass=counting_measure(incomplete)
        self.assertNotIn(F(5),mass)
        self.assertLess(len(mass),30)
        self.assertEqual(mass,direct_word_oracle(incomplete))

    def test_collision_free_alternative_kills_braid(self):
        # q3=3/2 is *spectrally injective*: v_3 detects its exponent.
        # This cleanly refutes deriving the braid from free FUCC + flat log.
        shifted=source([F(3,2) if p==3 else F(p) for p in self.primes],30)
        mass=counting_measure(shifted)
        self.assertEqual(len(mass),59)
        self.assertTrue(all(v==1 for v in mass.values()))
        self.assertEqual(mass,direct_word_oracle(shifted))
        tested,bad=affine_braid_defects(shifted,mass)
        self.assertGreater(tested,0)
        self.assertEqual(bad[0]['defect'],-1)
        self.assertEqual(bad[0]['x'],'1')
        self.assertEqual(first_archimedean_cell(mass),F(1,2))
        self.assertEqual(convolution_log(mass),expected_prime_power_measure(shifted))

    def test_arch_calibration_alone_does_not_force_braid(self):
        # q3=9/2: v_3 still detects the source generator, so no collisions.
        # The first cell 1->2 has exact unit volume but affine law fails.
        shifted=source([F(9,2) if p==3 else F(p) for p in self.primes],40)
        atoms=counting_measure(shifted)
        self.assertTrue(all(w==1 for w in atoms.values()))
        self.assertEqual(first_archimedean_cell(atoms),1)
        trials,defects=affine_braid_defects(shifted,atoms)
        self.assertGreater(trials,0)
        self.assertEqual(defects[0]['defect'],-1)
        self.assertEqual(atoms,direct_word_oracle(shifted))

    def test_uniform_squaring_preserves_braid_but_breaks_unit(self):
        squared=source([p*p for p in self.primes],900)
        mass=counting_measure(squared)
        self.assertEqual(set(mass.values()),{F(1)})
        self.assertEqual(list(mass),[F(i*i) for i in range(1,31)])
        tested,bad=affine_braid_defects(squared,mass)
        self.assertGreater(tested,25)
        self.assertFalse(bad)
        self.assertEqual(first_archimedean_cell(mass),3)

    def test_wrong_jet_weight_detected_by_independent_word_oracle(self):
        mutant=counting_measure(self.valid,jet_scale=2)
        self.assertNotEqual(mutant,direct_word_oracle(self.valid))
        self.assertEqual(mutant[F(2)],2)

    def test_horizon_cannot_attest_future_primes(self):
        original=source(self.primes,30)
        hidden=source(self.primes+[101],30)
        self.assertEqual(counting_measure(original),counting_measure(hidden))
        # First available discriminator is a source horizon >=101.
        witness=counting_measure(source(self.primes+[101],101))
        base=counting_measure(source(self.primes,101))
        self.assertEqual(witness[F(101)],1)
        self.assertNotIn(F(101),base)

    def test_local_log_inverts_even_colliding_generators(self):
        source2=source([2,3,6],20)
        self.assertEqual(convolution_log(counting_measure(source2)),
                         expected_prime_power_measure(source2))

    def test_invalid_sources_fail_closed(self):
        with self.assertRaises(SourceError):
            source([1],10)
        with self.assertRaises(SourceError):
            source([0],10)
        with self.assertRaises(SourceError):
            source([1.5],10)
        with self.assertRaises(SourceError):
            JetSource((('a',F(2)),('a',F(3))),F(10))
        with self.assertRaises(SourceError):
            JetSource(tuple(),F(10001))
        with self.assertRaises(SourceError):
            convolution_words(source([F(10001,10000)],200))

    def test_wrong_composite_source_cannot_be_extracted_from_mass(self):
        with self.assertRaises(SourceError):
            rediscover_generators({F(1):F(1),F(2):F(1,2)})
        with self.assertRaises(SourceError):
            convolution_log({F(1):F(2), F(2):F(1)})


if __name__ == '__main__':
    unittest.main()
