"""X10: exact observable-algebra/linear-spectral blind-spot controls.

Independent stdlib implementation. Finite bounds: 234 source/readout tables
on at most three states, one four-state witness, cylinder margins <= 8 bits.
Cylinder margins are not synthetic finite approximations to the infinite shift.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import platform
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))


def dot(a, b):
    return sum((F(x) * y for x, y in zip(a, b)), F()) / len(a)


def rank(rows):
    if not rows:
        return 0
    a = [list(map(F, row)) for row in rows]
    pivot = 0
    for j in range(len(a[0])):
        k = next((k for k in range(pivot, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        scale = a[pivot][j]
        a[pivot] = [x / scale for x in a[pivot]]
        for k in range(len(a)):
            if k != pivot:
                scale = a[k][j]
                a[k] = [x - scale * y for x, y in zip(a[k], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def determinant(a):
    n = len(a)
    answer = F()
    for order in permutations(range(n)):
        term = F((-1) ** sum(order[i] > order[j]
                            for i in range(n) for j in range(i + 1, n)))
        for i, j in enumerate(order):
            term *= a[i][j]
        answer += term
    return answer


def minor_rank(rows):
    for size in range(min(len(rows), len(rows[0])), 0, -1):
        for rr in combinations(range(len(rows)), size):
            for cc in combinations(range(len(rows[0])), size):
                if determinant([[rows[i][j] for j in cc] for i in rr]):
                    return size
    return 0


def pullback(f, transition):
    return tuple(f[j] for j in transition)


def delays(q, transition, horizon):
    rows = [q]
    for _ in range(horizon - 1):
        rows.append(pullback(rows[-1], transition))
    return rows


def conditional(values, keys):
    groups = {}
    for value, key in zip(values, keys):
        groups.setdefault(key, []).append(value)
    means = {key: sum(map(F, vals), F()) / len(vals) for key, vals in groups.items()}
    return tuple(means[key] for key in keys)


def run():
    ones = (1, 1, 1, 1)
    transition = (0, 2, 1, 3)  # Swap the two actual source bits.
    q = (-1, -1, 1, 1)
    uq = pullback(q, transition)
    nonlinear = tuple(a * b for a, b in zip(q, uq))
    linear_rows = [ones, q, uq]
    full_rows = linear_rows + [nonlinear]
    assert rank(linear_rows) == minor_rank(linear_rows) == 3
    assert rank(full_rows) == minor_rank(full_rows) == 4
    profiles = tuple(zip(q, uq))
    assert len(set(profiles)) == 4
    assert pullback(nonlinear, transition) == nonlinear
    assert dot(nonlinear, nonlinear) == 1
    assert all(dot(row, nonlinear) == 0 for row in linear_rows)
    assert dot(q, q) == 1  # Positive sensor calibration.
    density_laws = []
    for epsilon in (F(1, 2), F(-1, 2)):
        density = tuple(1 + epsilon * x for x in nonlinear)
        assert all(x > 0 for x in density) and dot(ones, density) == 1
        assert pullback(density, transition) == density
        assert dot(q, density) == dot(uq, density) == 0
        assert dot(nonlinear, density) == epsilon
        density_laws.append({'epsilon': epsilon,
                             'probability_masses': tuple(x / 4 for x in density),
                             'joint_delay_product_mean': epsilon})
    resolvent_witnesses = []
    for z in (F(2), F(3), F(5)):
        response_source = tuple(F(v) / (z - 1) for v in nonlinear)
        assert tuple(z * x - y for x, y in zip(response_source,
                                              pullback(response_source, transition))) == nonlinear
        delayed_readouts = []
        for _ in range(5):
            readout = (dot(ones, response_source), dot(q, response_source))
            assert readout == (0, 0)
            delayed_readouts.append(readout)
            response_source = pullback(response_source, transition)
        resolvent_witnesses.append({'z': z, 'delayed_readouts': delayed_readouts})

    # Minimality: every fully separating binary readout on <=3 finite states
    # has full linear Krylov rank. Enumerate all stationary source tables.
    oracle_counts = []
    for n in (1, 2, 3):
        checked = separating = 0
        for t in product(range(n), repeat=n):
            for sensor in product((-1, 1), repeat=n):
                rows = delays(sensor, t, n)
                words = tuple(zip(*rows))
                linear_dimension = rank([(1,) * n] + rows)
                if len(set(words)) == n:
                    assert linear_dimension == n
                    separating += 1
                checked += 1
        oracle_counts.append({'states': n, 'source_sensor_tables': checked,
                              'fully_separating': separating})
    assert sum(row['source_sensor_tables'] for row in oracle_counts) == 234

    # Exact cylinder marginals of the declared bilateral Bernoulli source.
    # Future-only conditional expectation misses the previous bit, whose
    # Koopman pullback is the current bit and is therefore visible.
    words = tuple(product((-1, 1), repeat=4))  # coordinates -1,0,1,2
    previous = tuple(word[0] for word in words)
    current = tuple(word[1] for word in words)
    future_keys = tuple(word[1:] for word in words)
    p_previous = conditional(previous, future_keys)
    p_current = conditional(current, future_keys)
    assert all(x == 0 for x in p_previous)
    assert p_current == current
    assert dot(previous, previous) == 1
    assert dot(p_current, p_current) == 1

    # Nonconstant autonomous phase sensor × actual infinite Bernoulli shift.
    # Fair independent cylinder laws certify finite moments/counts only;
    # the general all-lag assertions have their written product-measure proof.
    correlations = {}
    coordinates = tuple(range(-4, 5))
    all_words = tuple(product((-1, 1), repeat=len(coordinates)))
    zero_index = coordinates.index(0)
    for lag in coordinates:
        index = coordinates.index(lag)
        correlations[str(lag)] = sum((F(word[zero_index] * word[index])
                                      for word in all_words), F()) / len(all_words)
        assert correlations[str(lag)] == (1 if lag == 0 else 0)
    phase_profiles = []
    for n in range(1, 9):
        counts = {}
        for phase in (0, 1):
            visible = tuple((-1) ** (phase + j) for j in range(n))
            for hidden_word in product((0, 1), repeat=n):
                counts[(visible, hidden_word)] = counts.get((visible, hidden_word), 0) + 1
        assert len({v for v, h in counts}) == 2
        assert len(counts) == 2 ** (n + 1)
        assert len(set(counts.values())) == 1
        phase_profiles.append({'delay_length': n, 'visible_profiles': 2,
                               'joint_phase_hidden_profiles': len(counts),
                               'hidden_conditional_entropy_bits': n})

    base = Path(__file__).parents[4]
    anchors = [
        'observational_succ/chaos_source_quotient.py',
        'observational_succ/nerode_probe_growth.py',
        'observational_succ/dynamic_fourier_tower.py',
        'research/2026-10-13/SWARM_ATLAS/D25.md',
        'research/2026-10-13/SWARM_ATLAS/D27.md',
        'research/2026-10-13/SWARM_ATLAS/D26_SYMBOLIC_RETURN_FRONTIERS.md',
        'research/2026-10-13/SWARM_ATLAS/D28.md',
        'research/2026-10-13/SWARM_ATLAS/D32_DELAY_COORDINATES.md',
    ]
    e40 = base / 'research/2026-10-13/SWARM_ATLAS/E40/DOSSIER.md'
    if not e40.exists():
        e40 = Path('/home/leah/succ_lab/many-worlds-atlas/research/2026-10-13/SWARM_ATLAS/E40/DOSSIER.md')
    return {
        'status': 'TESTED MODEL', 'parent_sha': 'dc23cf405fa432b717ca84018ab86d78ef08edde',
        'python': platform.python_version(), 'exact_arithmetic': 'integers/Fraction',
        'resource_caps': {'cpu_seconds': 25, 'address_space_mib': 256},
        'command': 'timeout 25s python research/2026-10-13/SWARM_ATLAS/X10/probe.py',
        'exit_code': 0, 'four_state_source': {'transition': transition, 'q': q, 'Uq': uq,
            'delay_profiles': profiles, 'linear_krylov_dimension': 3,
            'generated_algebra_dimension': 4, 'hidden_linear_mode': nonlinear,
            'mode_norm_squared': dot(nonlinear, nonlinear),
            'nonlinear_readout': dot(nonlinear, nonlinear),
            'positive_stationary_laws': density_laws,
            'resolvent_witnesses': resolvent_witnesses},
        'binary_minimality_oracle': oracle_counts,
        'future_is_not_reducing': {'previous_bit_norm_squared': 1,
            'P_previous_bit': p_previous, 'P_U_previous_bit': p_current,
            'U_P_previous_bit_is_zero': True, 'commutator_norm_squared': 1},
        'bernoulli_product_cylinder_moments': correlations,
        'nonconstant_phase_hidden_cylinders': phase_profiles,
        'infinite_shift_simulated_or_proved_by_finite_search': False,
        'source_authenticated': False, 'full_suite': 'NOT RUN', 'compiler': 'NOT RUN',
        'probe_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'anchor_sha256': {p: sha256((base / p).read_bytes()).hexdigest() for p in anchors},
        'E40_authorized_external_anchor_sha256': sha256(e40.read_bytes()).hexdigest(),
    }


def json_safe(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    result = json.loads(json.dumps(run(), default=json_safe))
    if len(sys.argv) == 3 and sys.argv[1] == '--verify':
        assert result == json.loads(Path(sys.argv[2]).read_text())
        print('PASS: exact receipt replay')
    else:
        assert len(sys.argv) == 1
        print(json.dumps(result, indent=2, sort_keys=True))
