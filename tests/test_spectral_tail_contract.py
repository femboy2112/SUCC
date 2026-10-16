import copy
import json
from pathlib import Path
import unittest

from observational_succ import spectral_tail_contract as T
from observational_succ.source_proof_certificate import CapsuleError, evidence_file

ROOT = Path(__file__).resolve().parents[1]


class SpectralTailContractTests(unittest.TestCase):
    def packet(self):
        c = json.loads((ROOT/'research/2026-10-16/OBSERVER_SCHUR_CAPSULES.json').read_text())
        e = [evidence_file(ROOT, 'research/2026-10-16/CROSS_PRIME_WAVEFRONT_CONTINUATION.md', 'PAPER_SOURCE_APPLICATION')]
        return T.make_open_tail_packet(c, e)

    def test_integrity_does_not_discharge_rate(self):
        r = T.audit_tail_packet(self.packet(), ROOT)
        self.assertFalse(r['source_tail_rate_proved'])
        self.assertIsNone(r['semantic_authority_issued'])
        self.assertEqual(r['dependency_audit']['theorems_proved_by_this_audit'], [])

    def test_conditional_rate_preserves_hypothesis(self):
        p = self.packet()
        p['estimate'] = {'kind': 'FRACTIONAL_RANGE', 'eta': '1/4', 'C_squared': '1'}
        p['sha256'] = T.digest(p)
        r = T.audit_tail_packet(p, ROOT)
        self.assertIn('SOURCE_SPECTRAL_TAIL_RATE', r['outstanding_obligations'])
        self.assertFalse(r['source_tail_rate_proved'])

    def test_rehashed_status_forgery(self):
        for key, value in [('source_sign', 'PROVED'), ('RH_proved', True),
                           ('kernel_proof_of_analytic_source', True),
                           ('outstanding_obligations', []), ('global_conclusion', 'S0>=0'),
                           ('source_lower_matrix', [[1]]), ('estimate_status', 'LEAN_KERNEL_PROVED')]:
            p = self.packet(); p[key] = value; p['sha256'] = T.digest(p)
            with self.subTest(key=key), self.assertRaises(CapsuleError):
                T.audit_tail_packet(p, ROOT)

    def test_source_mapping_forgery(self):
        for key, value in [('radius', '3/5'), ('active_prime_powers', [[2, 2], [6, 6]]),
                           ('coordinate_metric', ['1']*4), ('signed_channels', ['real_Gamma_all_modes'])]:
            p = self.packet(); p['source'][key] = value; p['sha256'] = T.digest(p)
            with self.subTest(key=key), self.assertRaises(CapsuleError):
                T.audit_tail_packet(p, ROOT)

    def test_derivative_tail_cannot_use_operator_tail(self):
        p = self.packet()
        p['analytic_error_budgets']['Gamma_derivative_tail'] = p['analytic_error_budgets']['Gamma_operator_tail']
        p['sha256'] = T.digest(p)
        with self.assertRaises(CapsuleError):
            T.audit_tail_packet(p, ROOT)

    def test_bad_fractional_domain(self):
        for eta in ('0', '3/4', 'bad', 0.25):
            p = self.packet(); p['estimate'] = {'kind': 'FRACTIONAL_RANGE', 'eta': eta, 'C_squared': '1'}
            p['sha256'] = T.digest(p)
            with self.assertRaises(CapsuleError):
                T.audit_tail_packet(p, ROOT)

    def test_finite_hash_valid_false_prose_not_proof(self):
        p = self.packet()
        # The inherited checker intentionally cannot decide paper prose truth.
        p['capsules'][0]['statement'] = 'False prose with internally matching bytes'
        p['sha256'] = T.digest(p)
        r = T.audit_tail_packet(p, ROOT)
        self.assertIsNone(r['semantic_authority_issued'])

    def test_evidence_drift(self):
        p = self.packet(); p['evidence'][0]['sha256'] = '0'*64; p['sha256'] = T.digest(p)
        with self.assertRaises(CapsuleError):
            T.audit_tail_packet(p, ROOT)


if __name__ == '__main__':
    unittest.main()
