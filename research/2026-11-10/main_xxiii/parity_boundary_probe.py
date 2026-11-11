"""Exact integer coefficient calibration for the radix-16 Fejér recursion."""

from collections import Counter


def fejer_numerator(size: int) -> Counter[int]:
    return Counter({k: size - abs(k) for k in range(1 - size, size)})


def product_coefficients(
    base: Counter[int], block: Counter[int], radix: int
) -> Counter[int]:
    coefficients: Counter[int] = Counter()
    for left, left_weight in base.items():
        for right, right_weight in block.items():
            coefficients[radix * left + right] += left_weight * right_weight
    return coefficients


def main() -> None:
    block = fejer_numerator(16)
    for k, weight in block.items():
        # In Z[z]/(z^8+1), z is a primitive sixteenth root of unity.
        branch_sum = [0] * 8
        for branch in range(16):
            exponent = (k * branch) % 16
            branch_sum[exponent % 8] += 1 if exponent < 8 else -1
        expected = [16 if k == 0 else 0] + [0] * 7
        assert branch_sum == expected
        if k == 0:
            assert weight * branch_sum[0] == 16**2

    sizes = (1, 3, 16, 23, 256, 4096)
    for size in sizes:
        base = fejer_numerator(size)
        expected = fejer_numerator(16 * size)
        assert product_coefficients(base, block, 16) == expected
        if size > 1:
            assert product_coefficients(base, block, 15) != expected
        assert 2 * sum(weight for k, weight in expected.items() if k % 2) == (
            16 * size
        ) ** 2
    print("PASS: 31 branch coefficients, 6 product/odd-weight cases, 5 mutations")


if __name__ == "__main__":
    main()
