"""Root replay: production certificates against a separate SymPy matrix route.

Run with PYTHONPATH=. from repository root. Exact arithmetic only. This is a
finite implementation/receipt audit, not a proof of the universal theorems.
"""
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from math import comb
from pathlib import Path
import platform

import sympy as sp

from observational_succ.gamma_observer_descent import integer_gamma_operator, linear_descent
from observational_succ.gamma_source_volume import (
    source_depth_ratio, source_hankel_certificate, source_hankel_determinant,
    source_moment_pi_coefficient,
)


def exact_matrix(matrix):
    return sp.Matrix([[sp.Rational(value.numerator, value.denominator)
                       if isinstance(value, Q) else sp.Rational(value)
                       for value in row] for row in matrix])


def main():
    root = Path(__file__).resolve().parent
    independent = json.loads((root / 'receipts/independent.json').read_text())
    assert independent['status'] == 'PASS'
    assert independent['script_sha256'] == hashlib.sha256((root/'independent_audit.py').read_bytes()).hexdigest()
    comparisons = 0
    for row in independent['exact']['moments']:
        assert source_moment_pi_coefficient(row['n']) == Q(row['c_n'])
        comparisons += 1
    for row in independent['exact']['hankel']:
        determinant = source_hankel_determinant(row['dimension'])
        assert determinant.pi_coefficient == Q(row['slope'])
        assert determinant.constant == Q(row['intercept'])
        assert source_hankel_certificate(row['dimension'], 4).strict_positive
        comparisons += 3
    for n in range(1, 17):
        assert Q(1, 4**(n-1)) <= source_depth_ratio(n) <= 1
        comparisons += 1

    matrix_cases = 0
    descent_certificates = 0
    # This grid is distinct from the constructor's 1/2 grid and uses a
    # symbolic inverse/power, not the production augmented Gaussian solve.
    for entries in product((Q(-1, 3), Q(0), Q(1, 3)), repeat=4):
        source = (entries[:2], entries[2:])
        symbolic = exact_matrix(source)
        for order in (1, 2, 5, 6):
            actual = integer_gamma_operator(source, order)
            expected = (2*sp.eye(2)-symbolic)**(-order)
            assert exact_matrix(actual) == expected
            matrix_cases += 1
            for report in (((1, 2),), ((1, 0), (2, 0))):
                cert = linear_descent(actual, report)
                p = exact_matrix(report)
                pa = p*expected
                assert cert.descends == (p.col_join(pa).rank() == p.rank())
                if cert.descends:
                    assert exact_matrix(cert.factor)*p == pa
                else:
                    hidden = exact_matrix(tuple((v,) for v in cert.kernel_witness))
                    assert p*hidden == sp.zeros(p.rows, 1)
                    assert pa*hidden != sp.zeros(p.rows, 1)
                descent_certificates += 1

    # Jordan control: spectral radius <=1 does not require a diagonalizable
    # source or contraction in the displayed Euclidean coordinates.
    jordan = ((1, 1, 0), (0, 1, 1), (0, 0, 1))
    for order in range(1, 7):
        expected = (2*sp.eye(3)-exact_matrix(jordan))**(-order)
        assert exact_matrix(integer_gamma_operator(jordan, order)) == expected
        # Convert through the production result to preserve its exact input contract.
        assert not linear_descent(integer_gamma_operator(jordan, order), ((1, 0, 0),)).descends
        matrix_cases += 1

    cycle = tuple(tuple(int(i == (j+1) % 6) for j in range(6)) for i in range(6))
    p = sp.Matrix([[1, sp.Rational(1, 2), -sp.Rational(1, 2), -1, -sp.Rational(1, 2), sp.Rational(1, 2)]])
    cycle_matrix = exact_matrix(cycle)
    admitted_integer_orders = []
    for order in range(1, 13):
        analytic = (2*sp.eye(6)-cycle_matrix)**(-order)
        assert exact_matrix(integer_gamma_operator(cycle, order)) == analytic
        admitted = p.col_join(p*analytic).rank() == p.rank()
        assert admitted == (order % 6 == 0)
        if admitted:
            admitted_integer_orders.append(order)
        matrix_cases += 1
    assert p*(2*sp.eye(6)-cycle_matrix)**(-6) == -p/27
    assert p*cycle_matrix**3 == -p
    assert (p*cycle_matrix)[1] == -sp.Rational(1, 2)
    assert (p*cycle_matrix)[5] == 1

    tail_rows = []
    for order, cutoff in product((1, 2, 6), (0, 5, 20)):
        exact = (2*sp.eye(6)-cycle_matrix)**(-order)
        partial = sp.zeros(6)
        mass = Q(0)
        for n in range(cutoff+1):
            weight = Q(comb(n+order-1, n), 2**(n+order))
            mass += weight
            partial += sp.Rational(weight.numerator, weight.denominator)*cycle_matrix**n
        norm = max(sum(abs((exact-partial)[i, j]) for j in range(6)) for i in range(6))
        bound = Q(2, 3)**(cutoff+1)*2**order
        assert norm == sp.Rational((1-mass).numerator, (1-mass).denominator)
        assert norm <= sp.Rational(bound.numerator, bound.denominator)
        tail_rows.append({'order': order, 'cutoff': cutoff, 'exact_error_norm': str(norm),
                          'theorem_bound': str(bound)})

    receipt = {
        'status': 'PASS', 'scope': 'Exact finite replay; no universal conclusion from enumeration.',
        'python': platform.python_version(), 'sympy': sp.__version__,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_receipt_comparisons': comparisons,
        'independent_matrix_power_cases': matrix_cases,
        'rank_and_witness_certificate_replays': descent_certificates,
        'cycle_orders_checked': [1, 12], 'cycle_admitted_orders': admitted_integer_orders,
        'positive_cycle_gamma6_multiplier': '-1/27',
        'tail_certificates': tail_rows,
    }
    (root/'receipts/root_replay.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k != 'tail_certificates'}))


if __name__ == '__main__':
    main()
