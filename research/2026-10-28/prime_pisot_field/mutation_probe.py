"""Run actual false-model mutations against calibrated exact tests; restore all state."""
import io
import json
import unittest
from fractions import Fraction as F
import prime_pisot as core
import test_prime_pisot as tests


def run_one(name):
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromName(name, tests)
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    return result.wasSuccessful(), stream.getvalue()


mutations = []
def probe(name, owner, attr, replacement, test_name):
    before, baseline = run_one(test_name)
    if not before:
        raise AssertionError('positive control failed: '+name)
    old = getattr(owner, attr)
    try:
        setattr(owner, attr, replacement)
        accepted, trace = run_one(test_name)
    finally:
        setattr(owner, attr, old)
    after, restored = run_one(test_name)
    if accepted or not after:
        raise AssertionError('mutation not discriminated: '+name)
    mutations.append({'name': name, 'baseline_passed': before,
                      'mutant_rejected': not accepted, 'restored_passed': after,
                      'mutant_test_output': trace})


old_prime = core.is_prime
probe('fake composite primitive 4', core, 'is_prime', lambda n: n == 4 or old_prime(n),
      'ArithmeticSource.test_prime_channels_reject_composites_and_invalid_inputs')
probe('one-sided prime shift falsely lossless', tests, 'prime_fidelity', lambda n, p: F(1),
      'ArithmeticSource.test_local_fidelity_from_actual_path_count')
old_lap = tests.fiber_laplacian
def erase_composite_ground(n):
    a = old_lap(n)
    return [[v+(1 if i == j and core.omega(n)>1 else 0) for j, v in enumerate(row)]
            for i, row in enumerate(a)]
probe('composites incorrectly lose equilibrium', tests, 'fiber_laplacian', erase_composite_ground,
      'VirtualEquilibria.test_every_divisor_fiber_has_a_ground_state')
probe('omit Mobius removal of repetitions', tests, 'extract_primitives', lambda a: list(a),
      'EulerSource.test_formal_log_and_mobius_primitive_extraction')
old_conjugate = core.Quad.conjugate
probe('replace negative Pisot conjugate by positive inverse', core.Quad, 'conjugate',
      lambda self: -old_conjugate(self),
      'PisotSupport.test_negative_conjugate_sign_mutant_is_rejected')
null_pass, null_log = run_one('PisotSupport.test_two_prime_histories_have_exactly_the_same_pisot_clock')
assert null_pass
print(json.dumps({'mutants_killed': len(mutations), 'mutations': mutations,
                  'unchanged_null_control_passed': null_pass,
                  'scope': 'same-reasoner executable mutations, not independent-agent review'}, indent=2))
