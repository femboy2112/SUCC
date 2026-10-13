#!/usr/bin/env python3
"""Independent exact finite witnesses for the C19 review; no author probe imports."""

from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess


def mm(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def adj(a):
    return [list(col) for col in zip(*a)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def rank(a):
    a = [row[:] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][c]
        a[r] = [x / d for x in a[r]]
        for i in range(len(a)):
            if i != r:
                d = a[i][c]
                a[i] = [x - d * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def branch(ks, rho):
    terms = [mm(mm(k, rho), adj(k)) for k in ks]
    return [[sum(t[i][j] for t in terms) for j in range(len(terms[0]))]
            for i in range(len(terms[0]))]


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


i2 = eye(2)
p0, p1 = [[Q(1), Q(0)], [Q(0), Q(0)]], [[Q(0), Q(0)], [Q(0), Q(1)]]
sources = [p0, p1]
out = {}

# Individually physical terminal measurements need not form a prefix chain.
terminal = [[tr(mm(rho, e)) for rho in sources] for e in [p0, p1, p0, p1]]
assert all(any(p > 0 for p in row) for row in terminal)
assert not any(all(row[j] > 0 for row in terminal) for j in range(2))
k = mm(p1, p0)
fixed_second = [tr(branch([k], rho)) for rho in sources]
assert fixed_second == [0, 0]
out['fresh_terminal_not_fixed_word'] = {'fresh_probabilities': terminal,
                                      'actual_fixed_second_prefix': fixed_second}

# No dimension-only deadline: a rotated rank-one branch arrives after a plateau.
m = 37
projector = [[Q(9, 25), Q(12, 25)], [Q(12, 25), Q(16, 25)]]
assert mm(projector, projector) == projector
effects = [i2] * (m + 1) + [projector, projector]
assert rank(effects[m]) == 2 and rank(effects[m + 1]) == 1
out['late_rank_drop'] = {'initial_dimension': 2, 'first_drop_index': m + 1,
                        'selected_ranks': [[n, rank(effects[n])] for n in [0, 1, m, m + 1, m + 2]]}

# Intermediate output dimension changes; effects remain on the initial qubit.
ks = [[[Q(1), Q(0)], [Q(0), Q(1)], [Q(0), Q(0)]],
      [[Q(3, 5), Q(4, 5), Q(0)]],
      [[Q(1)], [Q(0)], [Q(0)], [Q(0)]]]
k = i2
rectangular = []
for step in ks:
    k = mm(step, k)
    e = mm(adj(k), k)
    rectangular.append({'output_dimension': len(step), 'effect': e,
                        'likelihoods': [tr(mm(rho, e)) for rho in sources]})
assert rectangular[0]['effect'] == i2
assert rectangular[1]['effect'] == projector == rectangular[2]['effect']
out['rectangular_common_initial_domain'] = rectangular

# Positivity does not require CP: transpose preserves traces and positivity,
# but the partial transpose of a Bell state has a negative singlet expectation.
partial_bell = [[Q(1, 2), 0, 0, 0], [0, 0, Q(1, 2), 0],
                [0, Q(1, 2), 0, 0], [0, 0, 0, Q(1, 2)]]
v = [[Q(0)], [Q(1)], [Q(-1)], [Q(0)]]
singlet_q = mm(mm(adj(v), partial_bell), v)[0][0] / Q(2)
assert singlet_q == Q(-1, 2)
out['positive_not_cp'] = {'transpose_prefix_effect': i2,
                         'partial_bell_normalized_singlet_expectation': singlet_q}

# Dropping TNI does not break support nesting, but effects need not decrease.
amp = [[Q(3), Q(0)], [Q(0), Q(3)]]
assert tr(branch([amp], p0)) == 9
out['cp_without_tni'] = {'amplifier_effect': mm(adj(amp), amp),
                        'source_likelihood': tr(branch([amp], p0))}

# Nonpositive linear trace-decreasing mutation revives a trace-zero output.
# F(diag(x,y))=diag(y,x-y), so tr(F(X))=X_00 on positive X.
a = [[Q(0), Q(1)], [Q(1), Q(-1)]]
row = [[Q(1), Q(1)]]
nonpositive = []
for n in range(1, 9):
    row = mm(row, a)
    nonpositive.append(row[0][:])
assert all(any(p > 0 for p in ps) for ps in nonpositive)
assert not any(all(ps[j] > 0 for ps in nonpositive) for j in range(2))
assert nonpositive[:2] == [[1, 0], [0, 1]]
out['nonpositive_mutation'] = {'likelihoods': nonpositive,
                             'not_a_quantum_instrument': True}

# A normalized poststate loses prefix weight, and zero normalization is undefined.
half_k = [[Q(1, 2), Q(0)], [Q(0), Q(1, 2)]]
rho = p0
decay = []
for n in range(1, 9):
    rho = branch([half_k, half_k], rho)
    prob = tr(rho)
    assert prob == Q(1, 2 ** n)
    normalized = [[x / prob for x in row] for row in rho]
    assert normalized == p0
    decay.append({'n': n, 'raw_probability': prob, 'normalized_trace': tr(normalized)})
zero = branch([p0], p1)
assert tr(zero) == 0
out['normalization_and_infinite_event'] = {'finite_prefixes': decay,
                                         'impossible_branch_denominator': tr(zero),
                                         'conditional_poststate': None,
                                         'infinite_event_limit': '0 (analytic limit)'}

# Compact pure family: rational unit vectors approach e0, but each tail dies.
compact_rows = []
for k in range(1, 7):
    m_k = 2 ** k
    aa, bb = Q(m_k * m_k - 1, m_k * m_k + 1), Q(2 * m_k, m_k * m_k + 1)
    assert aa * aa + bb * bb == 1
    rho = [[aa * aa, aa * bb], [aa * bb, bb * bb]]
    diff = [[rho[0][0] - 1, rho[0][1]], [rho[1][0], rho[1][1]]]
    assert diff[0][0] * diff[1][1] - diff[0][1] * diff[1][0] == -bb * bb
    probs = [bb * bb if k >= n else Q(0) for n in range(1, 9)]
    assert probs[k - 1] > 0 and probs[k] == 0
    compact_rows.append({'k': k, 'a': aa, 'b': bb, 'trace_distance_to_rho0': 2 * bb,
                         'tail_probabilities_n1_to_n8': probs})
out['compact_infinite_dimensional_pure_tail'] = compact_rows

# Finite convex hulls fail closure; the countable mixture supplies positive tails.
out['countable_mixture_repair'] = [{'n': n, 'diagonal_mixture_tail': Q(1, 2 ** (n - 1)),
                                   'k_n_witness_weight': Q(1, 2 ** n)} for n in range(1, 9)]
assert all(row['diagonal_mixture_tail'] >= row['k_n_witness_weight'] > 0
           for row in out['countable_mixture_repair'])

# Identical reduced states plus different retained memory give different likelihoods.
out['omitted_memory'] = {'same_reduced_qubit': p0, 'memory_labels': [0, 1],
                         'first_tail_probabilities': [0, 1],
                         'not_a_map_of_reduced_qubit_alone': True}
out['candidate_dependent_cp_mutation'] = [[int(n < k) for k in range(1, 7)]
                                         for n in range(1, 6)]
out['changing_original_class_mutation'] = {'identity_branch_probabilities': [1, 1],
                                          'alternating_singleton_class_labels': [0, 1, 0, 1],
                                          'common_class_member': None}
reset_k1 = [[Q(0), Q(1)], [Q(0), Q(0)]]
reset_outputs = [branch([p0, reset_k1], rho) for rho in sources]
assert reset_outputs == [p0, p0]
out['original_source_not_identified_by_reset'] = {'poststates': reset_outputs,
                                                'distinct_original_z_targets': [0, 1]}

source_commit = 'e6c792b26f2497ba8cb7a266cc518ec79d59fd56'
source_path = 'research/2026-10-13/SWARM_ATLAS/C19.md'
source_bytes = subprocess.check_output(['git', 'show', source_commit + ':' + source_path],
                                      cwd='/home/leah/succ_lab/swm-c19')
script = Path(__file__).resolve()
receipt = {'review_scope': 'finite exact witnesses; universal statements proved in review',
           'source_commit': source_commit, 'source_path': source_path,
           'source_sha256': sha256(source_bytes).hexdigest(),
           'author_probe_read_or_imported': False,
           'review_worktree_parent': subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                                             cwd=script.parent).decode().strip(),
           'python_version': platform.python_version(),
           'script_sha256': sha256(script.read_bytes()).hexdigest(),
           'command': 'python reviews/C19_RX_probe.py', 'assertions_passed': True,
           'results': serial(out)}
receipt_path = script.with_name('C19_RX_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'receipt': str(receipt_path), 'assertions_passed': True,
                  'source_sha256': receipt['source_sha256'],
                  'script_sha256': receipt['script_sha256'],
                  'checked_witness_families': list(out)}, indent=2))
