"""Reproduce the round's concrete tables with labelled exact/numerical fields."""
from dataclasses import asdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

from observational_succ.adaptive_haar_observer import (
    ConnectionBelief, structural_probe, posterior_link_after_successes,
    hidden_link_information_interval, hidden_link_information_nats,
    structural_promotion_energy, gibbs_probe_policy, two_stage_information_plan,
)
from observational_succ.haar_gamma_bridge import (
    source_haar_certificate, gamma_haar_certificate,
)
from observational_succ.haar_quantum_instruments import (
    coherence_state, two_axis_score, chsh_value, partial_trace,
    joint_axis_probabilities, shared_sign_probabilities,
)


def enclosing_decimals(lower, upper, places=12):
    """Round OUTWARD using integer division, never a floating-point format."""
    scale = 10**places
    lo = lower.numerator*scale//lower.denominator
    hi = -((-upper.numerator*scale)//upper.denominator)
    def render(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return f'{sign}{n//scale}.{n%scale:0{places}d}'
    return {'lower': render(lo), 'upper': render(hi),
            'label': 'certified outward rational decimal enclosure'}


def main():
    structural_rows = []
    for successes in range(5):
        p = posterior_link_after_successes(F(1, 2), F(3, 4), F(1, 4), successes)
        interval = hidden_link_information_interval(p, 48)
        numerical_i = hidden_link_information_nats(p)
        policy = gibbs_probe_policy((F(1, 2), F(1, 2)),
                                    (numerical_i-.15, 0), temperature=.125)
        structural_rows.append({'fresh_favorable_reports': successes, 'p': str(p),
                                'haar_detail_energy': str(p*p),
                                'information_nats': enclosing_decimals(*interval),
                                'deep_vs_stop_policy_numerical': policy[0]})
    half = hidden_link_information_interval(F(1, 2), 48)
    low = hidden_link_information_interval(F(1, 4), 48)
    high = hidden_link_information_interval(F(3, 4), 48)
    fixed = ((low[0]+high[0])/2-F(4, 25), (low[1]+high[1])/2-F(4, 25))
    optional = ((high[0]-F(3, 20))/2-F(1, 100),
                (high[1]-F(3, 20))/2-F(1, 100))
    assert half[1] < F(3, 20) and low[1] < F(3, 20) < high[0]
    assert fixed[0] > 0 and optional[0] > fixed[1]
    source = source_haar_certificate(5, power=1, terms=16)
    path = ((-1, 1, 0, 0), (1, -2, 1, 0), (0, 1, -2, 1), (0, 0, 1, -1))
    classical = gamma_haar_certificate(path, 1, 1)
    quantum_rows = []
    for c in (F(-1), F(0), F(3, 4), F(1)):
        state = coherence_state(c)
        quantum_rows.append({'coherence': str(c), 'ZZ': '1', 'XX': str(c),
                             'trusted_two_axis_score': str(two_axis_score(state)),
                             'rational_rotated_CHSH': str(chsh_value(state)),
                             'bob_marginal': [[str(v) for v in r] for r in partial_trace(state)]})
    for aa, avec in [('X', (1, 0)), ('Z', (0, 1))]:
        for bb, bvec in [('X', (1, 0)), ('Z', (0, 1))]:
            assert shared_sign_probabilities(aa, bb) == joint_axis_probabilities(coherence_state(1), avec, bvec)
    return {
        'python': platform.python_version(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Declared model tables; no empirical quantum or physical BBP experiment.',
        'structural_probe': {'rows': structural_rows, 'promotion_energy': str(structural_promotion_energy(F(1, 2), F(3, 4), F(1, 4))),
            'fixed_two_step_net_nats': enclosing_decimals(*fixed),
            'optional_continuation_net_nats': enclosing_decimals(*optional),
            'numerical_menu': asdict(two_stage_information_plan(ConnectionBelief.independent_fair(F(1, 2)),
                   structural_probe(F(3, 4), F(1, 4)), preparatory_cost=F(1, 100), deep_cost=F(3, 20)))},
        'native_source': {'terms': source.terms, 'levels': len(source.level_energies),
            'mass': enclosing_decimals(source.source_mass.lower, source.source_mass.upper),
            'total_covariance': enclosing_decimals(source.total_variance.lower, source.total_variance.upper),
            'haar_level_energies': [enclosing_decimals(e.lower, e.upper) for e in source.level_energies],
            'remaining_variance': enclosing_decimals(source.residual_variance.lower, source.residual_variance.upper),
            'analytic_remainder_bound': str(source.analytic_residual_bound)},
        'classical_gamma_control': {'trace_defect': str(classical.trace_energy),
            'defect': [[str(v) for v in row] for row in classical.defect]},
        'quantum_model': {'rows': quantum_rows,
            'restricted_XZ_classical_replica_verified': True,
            'warning': 'Trusted-qubit witness and rotated CHSH have different source assumptions.'},
    }


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
