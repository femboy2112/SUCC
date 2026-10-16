"""Integrity and debt audit for spectral tail claims; no semantic authority.

The generic proof-capsule verifier remains the dependency authority boundary.
This narrower adapter also binds analytic labels to the actual radius, metric,
source bytes and signed channels. It cannot discharge a source-range theorem.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

from .cross_prime_wavefront import active_wavefronts
from .source_proof_certificate import CapsuleError, audit_capsules
from .tate_suzuki_shorting import verify_original_suzuki_source


CHANNELS = ('real_Gamma_all_modes', 'pole_cosh', 'pole_sinh',
            'contact_real_Gamma', 'genuine_prime_power_half_density')
METRIC = ('1/3', '1/5', '1/7', '1/9')
BASE_DEBTS = ('SOURCE_MODEL_IDENTIFICATION', 'SOURCE_SPECTRAL_TAIL_RATE',
              'ZERO_SHIFT_REGULARIZATION_GAP')


def digest(packet):
    payload = {k: v for k, v in packet.items() if k != 'sha256'}
    return sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def source_contract():
    source = verify_original_suzuki_source()
    path = Path(__file__).with_name('source_weil_hierarchy.py')
    return {'git_blob': source['source_git_blob'], 'sha256': sha256(path.read_bytes()).hexdigest(),
            'radius': '1/2', 'active_prime_powers': [[2, 2]],
            'carrier': 'L2_0((-1/2,1/2),Lebesgue)',
            'low_modes': [1, 2, 3, 4], 'high_modes': 'Legendre>=5',
            'coordinate_metric': list(METRIC), 'signed_channels': list(CHANNELS),
            'source_epoch': 'PR85:dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc'}


def make_open_tail_packet(capsules, evidence, *, estimate=None):
    """Record a conditional rate or the unresolved target, with immutable debts.

    estimate = {kind: FRACTIONAL_RANGE, eta: rational string, C_squared: string}
    records an assumed norm bound. It does not certify that bound.
    """
    packet = {'schema': 'SUCC_SPECTRAL_RESPONSE_TAIL_v1', 'source': source_contract(),
              'spectral_measure': 'mu(E)=B 1_E(D) B*',
              'spectral_domain': '(0,||D||]; inverse powers on actual ranges only',
              'estimate': estimate, 'estimate_status': 'UNVERIFIED_SOURCE_PREMISE',
              'proof_authority': 'PAPER_PROVED_CONDITIONAL_IMPLICATION_ONLY',
              'outstanding_obligations': list(BASE_DEBTS),
              'source_sign': 'OPEN', 'global_conclusion': None,
              'source_lower_matrix': None, 'source_upper_matrix': None,
              'analytic_error_budgets': {
                  'spatial_compression': 'CG-SOURCE:11/[40(N+1)]',
                  'Gamma_operator_tail': '2/(4J+1)^2+16/(4J+1)^3',
                  'Gamma_derivative_tail': '2/(4J+1)+8/(4J+1)^2',
                  'source_regularization_gap': 'UNRESOLVED'},
              'capsules': capsules, 'evidence': evidence,
              'kernel_proof_of_analytic_source': False, 'RH_proved': False}
    packet['sha256'] = digest(packet)
    return packet


def audit_tail_packet(packet, root):
    """Fail closed on forged scope/debt; byte validity still proves no theorem."""
    if type(packet) is not dict or packet.get('schema') != 'SUCC_SPECTRAL_RESPONSE_TAIL_v1':
        raise CapsuleError('spectral tail schema required')
    if packet.get('sha256') != digest(packet):
        raise CapsuleError('spectral packet byte digest mismatch')
    if packet.get('source') != source_contract():
        raise CapsuleError('source/radius/channel/metric mapping mismatch')
    if active_wavefronts(F(1, 2)) != ((2, 2),):
        raise CapsuleError('source support mismatch')
    canonical = make_open_tail_packet(packet.get('capsules'), packet.get('evidence'),
                                      estimate=packet.get('estimate'))
    if packet != canonical:
        raise CapsuleError('unsupported status, analytic budget or premise discharge')
    estimate = packet['estimate']
    if estimate is not None:
        if type(estimate) is not dict or set(estimate) != {'kind', 'eta', 'C_squared'}:
            raise CapsuleError('typed conditional estimate required')
        if estimate['kind'] != 'FRACTIONAL_RANGE':
            raise CapsuleError('unsupported source tail estimate kind')
        try:
            eta, c = F(estimate['eta']), F(estimate['C_squared'])
        except (ValueError, TypeError, ZeroDivisionError) as exc:
            raise CapsuleError('exact rational estimate parameters required') from exc
        if (type(estimate['eta']) is not str or type(estimate['C_squared']) is not str
                or not 0 < eta <= F(1, 2) or c < 0):
            raise CapsuleError('conditional fractional theorem domain violated')
    root = Path(root).resolve()
    source_file = root/'observational_succ/source_weil_hierarchy.py'
    if (not source_file.is_file() or
            sha256(source_file.read_bytes()).hexdigest() != packet['source']['sha256']):
        raise CapsuleError('evidence root does not contain the pinned source model')
    if type(packet['evidence']) is not list or not packet['evidence']:
        raise CapsuleError('source/application evidence required')
    for item in packet['evidence']:
        if type(item) is not dict or set(item) != {'path', 'sha256', 'kind'}:
            raise CapsuleError('typed local evidence required')
        if type(item['kind']) is not str or not item['kind'].strip():
            raise CapsuleError('nonempty evidence kind required')
        relative = item['path']
        if type(relative) is not str or Path(relative).is_absolute():
            raise CapsuleError('relative evidence path required')
        path = (root/relative).resolve()
        if (not path.is_relative_to(root) or not path.is_file()
                or sha256(path.read_bytes()).hexdigest() != item['sha256']):
            raise CapsuleError('evidence missing, escaped or drifted')
    dependency = audit_capsules(packet['capsules'], root)
    return {'integrity': 'STRUCTURE_BYTES_AND_DECLARED_MAPPING_VALID',
            'conditional_estimate_recorded': estimate,
            'outstanding_obligations': list(BASE_DEBTS),
            'dependency_audit': dependency, 'semantic_authority_issued': None,
            'source_tail_rate_proved': False, 'source_sign_proved': False,
            'kernel_proof_of_analytic_source': False, 'RH_proved': False}
