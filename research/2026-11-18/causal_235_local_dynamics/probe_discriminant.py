"""Reproduce the exact finite discriminant/Jordan calibration, using stdlib."""
import json
from pathlib import Path

from fibonacci_235 import A, T, identity, multiply, power, subtract


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
        "proof_location": "FIBONACCI_LOCAL_BRIDGE.md section 3.2",
        "finite_calibration_is_universal_proof": False,
        "pi_normality_collatz_RH_proved": False,
    }
    output = Path(__file__).resolve().parent / "validation/discriminant_mechanism.json"
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
