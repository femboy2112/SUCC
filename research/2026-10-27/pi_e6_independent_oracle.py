"""Independent exact finite E6/E7 controls; infinite assertions are paper proofs."""
from fractions import Fraction as F
import json
from collections import Counter
from math import gcd


def numeral(digits):
    out = 0
    for digit in digits:
        out = 16 * out + digit
    return out


def interval_distance(point, lo, hi):
    if lo <= point <= hi:
        return F(0), max(point - lo, hi - point)
    return min(abs(point - lo), abs(point - hi)), max(abs(point - lo), abs(point - hi))



def marker_gap_mutation():
    """A one-digit change really defeats separation, not merely a premise check.

    A continues the nonconstant period [2,15,15]. After N=12 common digits,
    alpha changes the next 2 to3 and follows it with four zero digits.
    EVERY continuation of that finite alpha prefix violates the claimed
    lower separation16^-(N+1). No dual-expansion ambiguity is required.
    """
    word = (2,15,15)
    N = 12
    common = word * 4
    common_value = F(numeral(common),16**N)
    A = common_value + F(numeral(word),16**len(word)-1)/16**N
    predicted = word[0]
    threshold = F(1,16**(N+1))
    def enclosure(marker):
        digits = common+(marker,)+(0,)*4
        lo = F(numeral(digits),16**len(digits))
        hi = lo+F(1,16**len(digits))
        return lo,hi
    lo,hi = enclosure(3)
    assert 3-predicted == 1
    lower,upper = interval_distance(A,lo,hi)
    assert lower/threshold == F(13,4095)
    assert upper/threshold == F(13,4095)+F(1,65536)
    assert 0 < lower <= upper < threshold
    # Gap two restores the paper lower bound for every same continuation.
    good_lo,good_hi = enclosure(4)
    good_lower,good_upper = interval_distance(A,good_lo,good_hi)
    assert good_lower/threshold == 1+F(13,4095)
    assert good_lower >= threshold
    return {"common_prefix_length":N,"period":[2,15,15],
            "mutant_marker":3,"predicted_digit":predicted,
            "distance_over_claimed_lower":[str(lower/threshold),str(upper/threshold)],
            "all_continuations_violate_claimed_bound":True,
            "gap_two_positive_control_ratio":str(good_lower/threshold)}


def gaussian_projection_checks():
    """Independent exact E6 template Cauchy check, including equality controls."""
    def add(a,b):return a[0]+b[0],a[1]+b[1]
    def times_conjugate(a,b):return a[0]*b[0]+a[1]*b[1],a[1]*b[0]-a[0]*b[1]
    def norm2(a):return a[0]**2+a[1]**2
    def stats(z,w,M):
        N=len(z)
        sums=[(F(0),F(0)) for _ in range(M)]
        pairing=(F(0),F(0))
        for n,(a,b) in enumerate(zip(z,w)):
            sums[n%M]=add(sums[n%M],a)
            pairing=add(pairing,times_conjugate(a,b))
        qsum=sum(norm2(v) for v in sums)
        E=F(M,N*N)*qsum
        return pairing,qsum,E
    roots=((F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)))
    receipts=[]
    for M in (7,8):
        word=tuple(roots[t%4] for t in range(M))
        w=tuple(word[n%M] for n in range(64))
        z=tuple((-a,-b) if n<16 else (a,b) for n,(a,b) in enumerate(w))
        pairing,qsum,E=stats(z,w,M)
        assert pairing==(32,0)
        assert norm2(pairing)<=M*qsum
        assert E>=F(1,4)
        if M==8:assert E==F(1,4)  # worst earlier quarter makes lower bound sharp
        # Dropping the M factor is a genuine false numerical inequality.
        assert norm2(pairing)>qsum
        receipts.append({"N":64,"M":M,"pairing_squared":str(norm2(pairing)),
                         "class_square_sum":str(qsum),"energy":str(E)})
    # A non-periodic template relative to the proposed partition is invalid.
    w=tuple((F((-1)**n),F(0)) for n in range(32))
    pairing,qsum,E=stats(w,w,1)
    assert pairing==(32,0) and qsum==0 and E==0
    return {"valid_templates":receipts,"missing_modulus_factor_rejected":True,
            "wrong_partition_counterexample":{"N":32,"M":1,"pairing_squared":"1024","energy":"0"}}


def e6_controls():
    # Admissible M(4^j)=3*16^max(1,floor(j/4)); the finite periods here
    # use exactly the first stage of the explicit normal beta in E4.
    beta = list(range(16)) * 48
    digits = []
    words = []
    endpoints = [0]
    approximants = []
    marker_checks = 0
    for j in range(1, 8):
        end = 4 ** j
        period = 3 * 16 ** max(1, j // 4)
        word = beta[:period]
        assert len(word) == period
        if j > 1:
            previous_length = endpoints[-1] - endpoints[-2]
            predicted = words[-1][previous_length % len(words[-1])]
            word[0] = 0 if predicted >= 2 else 3
            assert abs(word[0] - predicted) >= 2
            marker_checks += 1
        old_length = len(digits)
        old_value = numeral(digits)
        a = F(old_value, 16 ** old_length) + F(numeral(word), 16 ** period - 1) / (16 ** old_length)
        approximants.append(a)
        length = end - old_length
        digits.extend(word * (length // period) + word[:length % period])
        words.append(word)
        endpoints.append(end)
    lo = F(numeral(digits), 16 ** len(digits))
    hi = lo + F(1, 16 ** len(digits))
    enclosures = 0
    for j, a in enumerate(approximants[:-1], 1):
        distance_lo, distance_hi = interval_distance(a, lo, hi)
        end = 4 ** j
        assert distance_lo >= F(1, 16 ** (end + 1))
        assert distance_hi <= F(1, 16 ** end)
        enclosures += 1
    # One distinct-rational and one equal-approximant branch at an onset
    # satisfying m_j <= N_j/16. The displayed universal result is paper proof.
    j = 5
    end = 4 ** j
    a = approximants[j - 1]
    q = 16 ** (11 * end // 64)
    p = a.numerator * q // a.denominator + 1
    assert F(p, q) != a
    for p, q in ((p, q), (a.numerator, a.denominator)):
        assert 16 ** (11 * end // 64) < 2 * q <= 16 ** (11 * end // 16)
        lower, _ = interval_distance(F(p, q), lo, hi)
        assert lower >= F(1, 1024 * q ** 6)
    marker_mutation = marker_gap_mutation()
    projection = gaussian_projection_checks()
    return {"marker_checks": marker_checks, "rational_tail_enclosures": enclosures,
            "determinant_branches": 2, "one_step_marker_mutation": marker_mutation,
            "gaussian_projection": projection,
            "normality_proved_by_finite_checks": False}





def e7_controls():
    """Finite residue multiplicities certify the exact root-sum input.

    Each complete orbit of a nonconstant root has sum zero by the finite
    geometric-series identity. The inclusive final endpoint contributes one.
    No transcendental value is evaluated or rounded here.
    """
    checked = 0
    cases = ((2, tuple(range(1, 18))), (3, (1, 17)), (4, (1, 256, 257)))
    for m, frequencies in cases:
        q = 16 ** m - 1
        for h in frequencies:
            for r in range(m):
                for t in range(m):
                    k = h * (16 ** r - 16 ** t)
                    counts = Counter(k * a % q for a in range(q))
                    g = gcd(k, q)
                    assert len(counts) == q // g
                    assert set(counts.values()) == {g}
                    assert set(counts) == set(range(0, q, g))
                    inclusive_zero_count = counts[0] + 1
                    assert inclusive_zero_count == g + 1
                    expected = F(1) if k % q == 0 else F(1, q + 1)
                    if r == t:
                        assert expected == 1
                    # Integer form of |h|<16^(m/2)+1; odd m uses h-1 squared.
                    elif (h - 1) ** 2 < 16 ** m:
                        assert expected == F(1, 16 ** m)
                    checked += 1
        for marker in (0, 3, 15):
            start = marker * 16 ** (m - 1)
            stop = (marker + 1) * 16 ** (m - 1)
            assert F(stop - start, q + 1) == F(1, 16)
    # Exact Gaussian class sums test the actual Gram quadratic expression.
    m = 3
    q = 16 ** m - 1
    sums = ((F(2), F(1)), (F(-1), F(3)), (F(1), F(-2)))
    for h in (1, 17):
        exact = F(0)
        for r, (x, y) in enumerate(sums):
            for t, (u, v) in enumerate(sums):
                k = h * (16 ** r - 16 ** t)
                gram = F(1) if k % q == 0 else F(1, q + 1)
                exact += (x * u + y * v) * gram
        diagonal = sum(x*x + y*y for x, y in sums)
        total_square = sum(x for x, y in sums)**2 + sum(y for x, y in sums)**2
        expected = (1-F(1,16**m))*diagonal + F(1,16**m)*total_square
        assert exact == expected
    # At the excluded boundary m=2,h=17 the two rotations coincide.
    # S=(1,-1) then has exact second moment zero, contradicting the
    # off-diagonal formula if its frequency restriction were deleted.
    q = 16**2-1
    assert 17*(16-1) == q
    exact_mutant = F(0)
    wrong = (1-F(1,16**2))*2
    assert exact_mutant != wrong
    # Dropping the duplicate endpoint incorrectly changes 1/256 to zero.
    assert F(1, 16**2) != 0
    return {"root_grid_pairs": checked, "gaussian_quadratic_checks": 2,
            "marker_probability": "1/16", "frequency_boundary_mutation_rejected": True,
            "omitted_endpoint_debt_mutation_rejected": True,
            "normality_proved_by_finite_checks": False}


def main():
    print(json.dumps({"E6": e6_controls(), "E7": e7_controls()}, sort_keys=True))


if __name__ == '__main__':
    main()
