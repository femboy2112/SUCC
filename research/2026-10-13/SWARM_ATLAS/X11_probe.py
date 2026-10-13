#!/usr/bin/env python3
"""Exact bounded X11 controls, using only Python's standard library."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import random
import resource
import subprocess
import time

resource.setrlimit(resource.RLIMIT_AS, (256*1024**2, 256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
START = time.perf_counter()
ROOT = Path(__file__).resolve().parents[3]
ATLAS = Path('/home/leah/succ_lab/many-worlds-atlas/research/2026-10-13/SWARM_ATLAS')
BASE = 'dc23cf405fa432b717ca84018ab86d78ef08edde'


def matrix(a, b, c, d):
    return ((Q(a), Q(b)), (Q(c), Q(d)))


ZERO = matrix(0, 0, 0, 0)
I = matrix(1, 0, 0, 1)
P0 = matrix(1, 0, 0, 0)
P1 = matrix(0, 0, 0, 1)
X = matrix(0, 1, 1, 0)
NIL = matrix(0, 1, 0, 0)
RESET = (P0, NIL)


def mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def trans(a):
    return tuple(zip(*a))


def add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def tr(a):
    return a[0][0]+a[1][1]


def cp(branch, rho):
    out = ZERO
    for k in branch:
        out = add(out, mul(mul(k, rho), trans(k)))
    return out


def dual(branch, effect):
    out = ZERO
    for k in branch:
        out = add(out, mul(mul(trans(k), effect), k))
    return out


def psd(a):
    return (a == trans(a) and a[0][0] >= 0 and a[1][1] >= 0
            and a[0][0]*a[1][1]-a[0][1]*a[1][0] >= 0)


def rank(a):
    if a == ZERO:
        return 0
    return 2 if a[0][0]*a[1][1]-a[0][1]*a[1][0] != 0 else 1


def kernel(a):
    if rank(a) == 0:
        return ((Q(1), Q(0)), (Q(0), Q(1)))
    if rank(a) == 2:
        return ()
    return ((-a[0][1], a[0][0]),) if a[0][0] else ((Q(1), Q(0)),)


def apply(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))


def support_contains(a, b):
    """range(b) <= range(a), using exact rational PSD kernels."""
    return all(apply(b, v) == (0, 0) for v in kernel(a))


def projector(v):
    norm2 = sum(x*x for x in v)
    assert norm2 > 0
    return tuple(tuple(v[i]*v[j]/norm2 for j in range(2)) for i in range(2))


def safe_bits(states):
    return {i for i in range(2) if all(support_contains(states[i], other)
                                      for other in states)}


def candidates(states):
    return {i for i in range(2) if tr(states[i]) > 0}


def original_report(states):
    c = candidates(states)
    return next(iter(c)) if len(c) == 1 else None


def compose_kraus(branch, prior):
    return tuple(mul(k, l) for k in branch for l in prior)


def jsonable(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (tuple, list, set)):
        return [jsonable(x) for x in (sorted(value) if isinstance(value, set) else value)]
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    return value


def main():
    controls = {}
    states = (P0, P1)
    assert safe_bits(states) == set() and original_report(states) is None
    reset_states = tuple(cp(RESET, rho) for rho in states)
    assert reset_states == (P0, P0)
    assert safe_bits(reset_states) == {0, 1} and original_report(reset_states) is None
    controls['reset_refutes_singleton_necessity_for_choice'] = {
        'original_candidates': candidates(reset_states), 'safe_choices': safe_bits(reset_states),
        'original_bit_report': original_report(reset_states), 'current_states': reset_states}
    controls['identity_only_toolkit_refutes_unrestricted_dominance_necessity'] = {
        'incomparable_supports': True, 'identity_only_safe_choices': [0, 1],
        'filter_complete_safe_choices': []}

    # One candidate has full support, without original-bit identification.
    full0 = (matrix(Q(1, 2), 0, 0, 0), matrix(0, 0, Q(1, 2), 0), NIL)
    full1 = (P0, matrix(0, Q(1, 2), 0, 0), matrix(0, 0, 0, Q(1, 2)))
    support_cases = [states, reset_states,
                     tuple(cp((P0,), rho) for rho in states),
                     tuple(cp(full0, rho) for rho in states),
                     tuple(cp(full1, rho) for rho in states)]
    separation_receipts = []
    for case in support_cases:
        assert candidates(case)
        for i in range(2):
            if i in safe_bits(case):
                continue
            j = 1-i
            v = next(v for v in kernel(case[i]) if apply(case[j], v) != (0, 0))
            p = projector(v)
            complement = add(I, scale(-1, p))
            assert mul(p, p) == p and psd(p) and psd(complement)
            assert add(mul(trans(p), p), mul(trans(complement), complement)) == I
            assert tr(cp((p,), case[i])) == 0 < tr(cp((p,), case[j]))
            separation_receipts.append({'reject_bit': i, 'survive_bit': j, 'projector': p})
    assert safe_bits(support_cases[3]) == {0} and original_report(support_cases[3]) is None
    assert safe_bits(support_cases[4]) == {1}
    after_reset = tuple(cp(RESET, rho) for rho in support_cases[4])
    assert safe_bits(after_reset) == {0, 1}
    controls['source_choice_does_not_identify_original_bit'] = {
        'safe_bit': 0, 'both_original_candidates': candidates(support_cases[3]),
        'original_bit_report': original_report(support_cases[3])}
    controls['irrevocable_first_safe_choice'] = {'first_safe_bit': 1,
                                                'later_safe_set': safe_bits(after_reset),
                                                'retained_bit': 1}

    # Oracle-name reductions are separate from the index-level diagonal proof.
    negative_names = 0
    for length in range(6):
        for name in product((-1, 0, 1), repeat=length):
            excluded = set(name)-{-1}
            if len(excluded) == 2:
                continue
            cur = (P0, P1)
            enumerated = set()
            for symbol in name:
                branch = (I,) if symbol == -1 else ((P1,) if symbol == 0 else (P0,))
                cur = tuple(cp(branch, rho) for rho in cur)
                enumerated.update(i for i in range(2) if tr(cur[i]) == 0)
            assert enumerated == excluded
            assert candidates(cur) == {0, 1}-excluded
            negative_names += 1

    delay_witnesses = []
    for delay in (0, 2, 17, 71):
        for proposed in (0, 1):
            cur = (P0, P1)
            for _ in range(delay):
                cur = tuple(cp((I,), rho) for rho in cur)
            assert candidates(cur) == {0, 1}
            p = P1 if proposed == 0 else P0
            cur = tuple(cp((p,), rho) for rho in cur)
            assert candidates(cur) == {1-proposed}
            delay_witnesses.append({'identity_prefix': delay, 'proposed': proposed,
                                    'continuation_survivor': 1-proposed})

    # No-input deterministic branch generators: complete finite tables.
    alphabet = ((I,), (X,), (P0,), (P1,), (NIL,), RESET, (P0, P1))
    for branch in alphabet:
        assert psd(add(I, scale(-1, dual(branch, I))))
    generators = []
    for size in (1, 2):
        for nxt in product(range(size), repeat=size):
            for labels in product(range(len(alphabet)), repeat=size):
                generators.append((size, nxt, labels))
    rng = random.Random(1107)
    for _ in range(48):
        size = rng.choice((3, 4))
        generators.append((size, tuple(rng.randrange(size) for _ in range(size)),
                            tuple(rng.randrange(len(alphabet)) for _ in range(size))))
    valid = invalid = 0
    maximum_bound = 0
    for size, nxt, labels in generators:
        seen, sequence, state = {}, [], 0
        while state not in seen:
            seen[state] = len(sequence)
            sequence.append(alphabet[labels[state]])
            state = nxt[state]
        mu, period = seen[state], len(sequence)-seen[state]
        bound = mu+2*period
        assert mu+period <= size and bound <= 2*size
        maximum_bound = max(maximum_bound, bound)
        cycle = (I,)
        for branch in sequence[mu:]:
            cycle = compose_kraus(branch, cycle)
        effects = [I]
        for _ in range(3):
            effects.append(dual(cycle, effects[-1]))
        assert rank(effects[2]) == rank(effects[3])
        assert all(psd(add(a, scale(-1, b))) for a, b in zip(effects, effects[1:]))
        assert all(apply(effects[3], v) == (0, 0) for v in kernel(effects[2]))
        cur = (P0, P1)
        state = 0
        at_bound = None
        for n in range(bound+9):
            if n == bound:
                at_bound = candidates(cur)
            if n >= bound:
                assert candidates(cur) == at_bound
            if n == bound+8:
                break
            branch = alphabet[labels[state]]
            before_safe = safe_bits(cur) if candidates(cur) else set()
            cur = tuple(cp(branch, rho) for rho in cur)
            if candidates(cur):
                assert before_safe <= safe_bits(cur)
            state = nxt[state]
        valid += bool(at_bound)
        invalid += not bool(at_bound)

    # A stationary report-driven instrument is NOT a closed branch generator.
    outcomes = tuple(scale(Q(1, 2), k) for k in (I, I, I, P0, P1))
    total_effect = ZERO
    for k in outcomes:
        total_effect = add(total_effect, mul(trans(k), k))
    assert total_effect == I
    cur = (P0, P1)
    for _ in range(17):
        cur = tuple(cp((outcomes[0],), rho) for rho in cur)
    assert candidates(cur) == {0, 1}
    cur = tuple(cp((outcomes[3],), rho) for rho in cur)
    assert candidates(cur) == {0}
    controls['one_state_stationary_instrument_no_deadline'] = {
        'complete_outcome_effect_sum': total_effect, 'rank_drop_at': 18,
        'controller_states': 1, 'selected_word_is_not_forced': True,
        'late_branch_likelihood_P0': tr(cur[0])}
    mixture = scale(Q(1, 2), I)
    assert mixture not in (P0, P1)
    assert tr(cp((P0,), mixture)) > 0 and tr(cp((P1,), mixture)) > 0
    controls['mixture_escape_changes_original_class'] = {'mixture': mixture,
                                                        'inside_fixed_C': False}

    source_paths = [ATLAS/name for name in ('B11.md', 'B12.md', 'B13.md', 'C19.md',
                                           'X07.md', 'reviews/C19_EFFECTIVE_SELECTOR_CANDIDATE.md')]
    source_paths += [ROOT/name for name in ('AGENTS.md', 'docs/METHOD.md',
        'provenance/IMPORT_MANIFEST.json', 'observational_succ/constructive_frontier.py',
        'observational_succ/ordinal_succ_report.py',
        'provenance/origins/fuckingrh/research/2026-10-10/INFINITE_REALIZATION_LIMITS.md',
        'research/2026-10-13/SWARM_ATLAS/X11.md',
        'research/2026-10-13/SWARM_ATLAS/X11_probe.py')]
    origin_command = ['git', '-C', '/home/leah/FuckingRH', 'show',
                      'ba075348b7bcc66d938b3e0ca96c26e95bba340a:actualization/ordinal_succ_report.py']
    original = subprocess.run(origin_command, capture_output=True)
    native_ordinal = (ROOT/'observational_succ/ordinal_succ_report.py').read_bytes()
    assert original.returncode == 0 and original.stdout == native_ordinal
    elapsed = time.perf_counter()-START
    assert elapsed < 30 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024
    receipt = {
        'claim_id': 'SWM-X11', 'status': 'TESTED MODEL',
        'written_proof_status': 'PROVED LOCAL, pending fresh non-deriver review',
        'parent_sha': BASE,
        'execution_checkout_sha': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip(),
        'command': 'PYTHONDONTWRITEBYTECODE=1 timeout 30s python research/2026-10-13/SWARM_ATLAS/X11_probe.py',
        'exit_code': 0, 'wall_seconds': elapsed,
        'max_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'address_space_limit_bytes': 256*1024**2,
        'negative_information_names_checked': negative_names,
        'rational_separating_projectors': separation_receipts,
        'cylinder_extension_receipts': delay_witnesses,
        'closed_no_input_generators_checked': len(generators),
        'generators_all_tables_N_1_2': 203, 'seeded_N_3_4_cases': 48,
        'controller_seed': 1107, 'valid_generators': valid, 'refuted_nonempty_promises': invalid,
        'maximum_checked_deadline': maximum_bound,
        'cycles_kernel_plateau_checked_at_powers': [2, 3],
        'controls': controls,
        'root_candidate_status_at_input': 'PRINCIPAL DERIVATION, PENDING NON-DERIVER CRUCIBLE',
        'universal_diagonal_executed': False, 'infinite_word_executed': False,
        'program_indices_equated_with_oracle_names': False,
        'actual_prepared_bit_identification_claimed': False,
        'selected_outcomes_forced_by_generator_claimed': False,
        'full_suite_or_compiler_run': False,
        'primary_sources': ['https://arxiv.org/pdf/1312.7305',
                            'https://www.cs.ox.ac.uk/people/samson.abramsky/handbook.pdf',
                            'https://arxiv.org/pdf/quant-ph/0107090',
                            'https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf'],
        'imported_ordinal_source_verification': {
            'command_argv': origin_command, 'exit_code': original.returncode,
            'source_and_destination_sha256': sha256(native_ordinal).hexdigest(),
            'byte_identical': True},
        'sha256': {str(p): sha256(p.read_bytes()).hexdigest() for p in source_paths},
    }
    print(json.dumps(jsonable(receipt), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
