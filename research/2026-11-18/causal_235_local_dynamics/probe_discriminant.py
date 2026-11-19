"""Reproduce the exact finite discriminant/Jordan calibration, using stdlib."""
import json
from pathlib import Path

from fibonacci_235 import (A, M, H, T, identity, multiply, polynomial,
                           power, subtract, symmetric_power_2)


def reduce_mod(matrix, prime):
    return tuple(tuple(x % prime for x in row) for row in matrix)


def rank_mod(matrix, prime):
    """Field Gaussian elimination; independent of spectral formulas."""
    rows = [list(row) for row in reduce_mod(matrix, prime)]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, prime)
        rows[rank] = [(x * inv) % prime for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                factor = rows[i][col]
                rows[i] = [(x - factor * y) % prime
                           for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def main():
    i2, i5 = identity(2), identity(5)
    for prime, period in ((2, 3), (3, 2), (5, 5)):
        assert power(T, period, prime) == i5
        assert reduce_mod(T, prime) != i5
    assert power(A, 4, 3) == ((2, 0), (0, 2))
    n = reduce_mod(subtract(A, ((3, 0), (0, 3))), 5)
    assert n == ((3, 1), (1, 2))
    assert reduce_mod(multiply(n, n), 5) == ((0, 0), (0, 0))
    assert power(A, 2, 5) == reduce_mod(subtract(n, i2), 5)
    delta = subtract(T, i5)
    ranks = [rank_mod(power(delta, k, 5), 5) for k in range(6)]
    fourth_column = [row[0] for row in power(delta, 4, 5)]
    assert ranks == [5, 4, 3, 2, 1, 0]
    assert fourth_column == [4, 3, 1, 2, 4]
    # Sister PR666 supplies the complementary source factor; verify the
    # literal polynomials and their new fifth-prime operator coupling.
    k = (4, -4, 0, 2, -1)
    q = (4, 0, 0, -2, -1, -1)
    product = [0] * 9
    for i, x in enumerate(H):
        for j, y in enumerate(k):
            product[i+j] += x*y
    assert product == [16, 0, 0, 0, 0, 0, 0, 0, -1]
    hm, km, qm = polynomial(M, H), polynomial(M, k), polynomial(M, q)
    assert hm == ((8, 1), (1, 7))
    assert km == ((0, 3), (3, -3))
    assert qm == ((7, -6), (-6, 13))
    assert reduce_mod(hm, 5) == n
    assert reduce_mod(qm, 5) == reduce_mod(subtract(((0, 0), (0, 0)), n), 5)
    one_plus_q = tuple(tuple(x + int(i == j) for j, x in enumerate(row))
                       for i, row in enumerate(qm))
    assert reduce_mod(symmetric_power_2(one_plus_q, 4), 5) == reduce_mod(T, 5)
    one_minus_h = subtract(i2, hm)
    assert (T[0][0] % 25,
            symmetric_power_2(one_minus_h, 4)[0][0] % 25,
            symmetric_power_2(one_plus_q, 4)[0][0] % 25) == (16, 1, 21)
    mutant_q = polynomial(M, (4, 0, 0, -2, 0, -2))
    mutant_increment = tuple(tuple(x + int(i == j) for j, x in enumerate(row))
                             for i, row in enumerate(mutant_q))
    assert reduce_mod(mutant_increment, 5) == n
    mutant_lift = symmetric_power_2(mutant_increment, 4)
    assert rank_mod(mutant_lift, 5) == 1
    assert power(mutant_lift, 2, 5) == tuple((0,) * 5 for _ in range(5))
    # This separate arithmetic condition controls fifth-prime divisibility
    # of the Collatz slope denominator 2**N - 3**s.
    discrete_logs = [3, 7, 7, 107, 607, 8107]
    for depth, exponent in enumerate(discrete_logs, 1):
        assert pow(2, exponent, 5**depth) == 3
        if depth > 1:
            assert exponent % (4 * 5**(depth-2)) == discrete_logs[depth-2]
    receipt = {
        "status": "EXACT_FINITE_CALIBRATION_PASS",
        "fibonacci_discriminant": 5,
        "matrix_orders_mod_2_3_5": [3, 2, 5],
        "ranks_T_minus_I_powers_mod_5": ranks,
        "T_minus_I_fourth_power_first_column_mod_5": fourth_column,
        "collatz_log_base_2_of_3_mod_5_power": discrete_logs,
        "source_complement_H_times_K": "16-t^8",
        "literal_signed_source_mod5_identity": "T=Sym^4(I+Q(M))",
        "mod25_counterexample_entry00_T_Hlift_Qlift": [16, 1, 21],
        "source_mutant_mod5_rank": 1,
        "source_mutant_mod5_square_zero": True,
        "sister_pr666_head": "7d2648374a9123e433c6d62c0a88933194a361c7",
        "proof_location": "FIBONACCI_LOCAL_BRIDGE.md section 3.2",
        "finite_calibration_is_universal_proof": False,
        "pi_normality_collatz_RH_proved": False,
    }
    output = Path(__file__).resolve().parent / "validation/discriminant_mechanism.json"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
