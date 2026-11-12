"""Literal source-transposition control for the return-family construction.

This oracle does not import return_paths or use its gcd normal form. It
compares genuine multiplication with F V_d F*, retaining authentic successor.
The transposition (11 13) preserves all canonical unit returns for n<=10,
but not their nonunit domain profiles. Outputs are exact basis labels or None.
"""
from __future__ import annotations

import json
from pathlib import Path


def transpose(label: int) -> int:
    return 13 if label == 11 else 11 if label == 13 else label


def literal_return(n: int, a: int, label: int, transported: bool) -> int | None:
    if transported:
        label = transpose(a * transpose(label))
    else:
        label *= a
    for _ in range(n - a):
        label += 1
    if transported:
        label = transpose(label)
    if label % n:
        return None
    label //= n
    return transpose(label) if transported else label


def omega(label: int) -> int:
    count, divisor = 0, 2
    while divisor * divisor <= label:
        while label % divisor == 0:
            label //= divisor
            count += 1
        divisor += 1
    return count + int(label > 1)


def report() -> dict:
    checks = 0

    def verify(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    for label in range(1, 301):
        verify(transpose(transpose(label)) == label, 'involution')
        verify(omega(transpose(label)) == omega(label), 'degree preservation')

    unit_cases = 0
    for n in range(2, 11):
        for a in range(1, n):
            verify(literal_return(n, a, 1, False) == 1, 'genuine unit')
            verify(literal_return(n, a, 1, True) == 1, 'counterfeit unit')
            unit_cases += 1

    witnesses = []
    expected = {
        1: ([1, 1, 1, 1], [1, 1, 1, 1]),
        6: ([2, 3, 4, 5], [2, 3, 4, 5]),
        11: ([3, 5, 7, 9], [3, None, None, None]),
        13: ([None, None, None, None], [None, 5, 7, 9]),
    }
    for label, (genuine_expected, altered_expected) in expected.items():
        genuine = [literal_return(5, a, label, False) for a in range(1, 5)]
        altered = [literal_return(5, a, label, True) for a in range(1, 5)]
        verify(genuine == genuine_expected, 'genuine source witness')
        verify(altered == altered_expected, 'counterfeit source witness')
        witnesses.append({'n': 5, 'input_label': label,
                          'genuine_outputs': genuine,
                          'transported_outputs': altered,
                          'genuine_strength': sum(x is not None for x in genuine),
                          'transported_strength': sum(x is not None for x in altered)})

    # Calibration: each return is injective on surviving basis labels, so
    # counting survivors equals the diagonal of the sum of R*R, with no
    # cancellation or unexamined matrix-truncation step.
    injection_cases = 0
    for n in range(2, 11):
        for a in range(1, n):
            for transported in (False, True):
                images = [literal_return(n, a, m, transported) for m in range(1, 301)]
                survivors = [m for m in images if m is not None]
                verify(len(survivors) == len(set(survivors)), 'partial injection')
                injection_cases += 1
    return {
        'schema': 'succ-return-source-probe-v1',
        'status': 'PASS', 'checks': checks, 'failures': 0,
        'permutation': '(11 13)', 'unit_path_cases': unit_cases,
        'finite_injection_cases': injection_cases,
        'degree_labels_checked': 300, 'witnesses': witnesses,
        'scope': 'Exact finite calibration; universal statements have separate proofs. '
                 'The permutation preserves primes as a set; this is a coupling test, '
                 'not a changed prime-pair count.',
    }


if __name__ == '__main__':
    result = report()
    destination = Path(__file__).resolve().parent / 'receipts/RETURN_SOURCE_REPORT.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
