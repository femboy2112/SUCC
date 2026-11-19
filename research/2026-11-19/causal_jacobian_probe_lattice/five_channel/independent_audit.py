"""Independent finite audit of observation and signed Weyl certificate arithmetic.

Uses determinantal divisors rather than Gaussian inversion for prime precision,
the combined rational BBP forcing rather than its four-term implementation, and
a full-angle degree-40/41 series with a BBP pi interval rather than the quarter
table's Machin approximation. These are different implementations, not external
refereeing and not independent mathematical provenance for the BBP identity.
No fresh-shell result is used to construct or tune this audit.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial, gcd, prod
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import observer as o
import weyl_probe as w


def permutation_det(a):
    n = len(a)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
                * prod(a[i][p[i]] for i in range(n))
                for p in permutations(range(n))), F())


def vp(q, p):
    q = F(q)
    if not q:
        return float("inf")
    num, den = abs(q.numerator), q.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def divisors(a, p):
    """Valuations of determinantal divisors, by all square minors."""
    delta = [0]
    n = len(a)
    for k in range(1, n + 1):
        delta.append(min(vp(permutation_det([[a[i][j] for j in jj] for i in ii]), p)
                         for ii in combinations(range(n), k)
                         for jj in combinations(range(n), k)))
    return delta


def integer_divisors(a):
    """Integer gcds of all square minors, independent of the local inverse."""
    result = [1]
    for k in range(1, len(a)+1):
        divisor = 0
        for ii in combinations(range(len(a)), k):
            for jj in combinations(range(len(a)), k):
                value = permutation_det([[a[i][j] for j in jj] for i in ii])
                assert value.denominator == 1
                divisor = gcd(divisor, abs(value.numerator))
        result.append(divisor)
    return result


def adjugate_inverse(a):
    """Small exact inverse by cofactors, not the observer's row elimination."""
    n = len(a)
    determinant = permutation_det(a)
    return tuple(tuple((-1)**(i+j) * permutation_det(
        [[a[r][c] for c in range(n) if c != i] for r in range(n) if r != j])
        / determinant for j in range(n)) for i in range(n))


def rational_forcing(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def bbp_pi_interval(terms=72):
    lower = sum((rational_forcing(n) / 16**(n-1) for n in range(1, terms+1)), F())
    # Actual r is positive decreasing; geometric tail starts at n=terms+1.
    return lower, lower + rational_forcing(terms+1) / (15*16**(terms-1))


def direct_phasor_interval(t):
    """Full-angle independent rational enclosure, degrees40/41."""
    plo, phi = bbp_pi_interval()
    pmid = (plo+phi)/2
    t = F(t) % 1
    if t > F(1, 2):
        t -= 1
    x = 2*pmid*t
    assert abs(x) < 4
    c = sum((F((-1)**k, factorial(2*k))*x**(2*k) for k in range(21)), F())
    s = sum((F((-1)**k, factorial(2*k+1))*x**(2*k+1) for k in range(21)), F())
    # Lagrange remainder: cos through40 costs |x|^41/41!, sine through41
    # costs |x|^42/42! <= 4^41/41!. Argument uncertainty costs <=(phi-plo)/2.
    error = F(4**41, factorial(41)) + (phi-plo)/2
    return (c-error, c+error), (s-error, s+error)


def run():
    checks = 0
    prime_receipts = []
    odd_repair_receipts = []
    universal_repair_receipts = []
    integer_row_closure_receipts = []
    for clocks in ((55, 89, 144, 233), (55, 89, 233, 235)):
        for p in (2, 3, 5, 7, 11, 29):
            chart = o.prime_chart(clocks, p)
            ds = divisors(chart.matrix, p)
            rank = max(k for k, d in enumerate(ds) if d == 0)
            loss = ds[4] - ds[3]
            assert (chart.rank, chart.loss, chart.determinant_valuation) == (rank, loss, ds[4])
            assert permutation_det(chart.matrix) != 0
            checks += 2
            prime_receipts.append({"clocks": clocks, "p": p,
                                   "determinantal_divisor_valuations": ds,
                                   "rank": rank, "precision_loss": loss})

    # New all-odd-prime repair: a separate exhaustive search of the finite
    # future window checks the chosen congruence classes and diagonal support.
    # Include a horizon giving valuation10 at the p=3 pole d=4: the declared
    # exponent is a minimum, so accidental higher pole depth must also work.
    for p in (3,5,7,11,13,17,29,97):
        a = 1+max(vp(d-e, p) for d,e in combinations((7,4,3,2), 2))
        assert o.polar_clock_depth(p) == a == (2 if p in (3,5) else 1)
        checks += 1
        for horizon in (1,2,13,55,233,999,29524,1000000):
            plan = o.plan_polar_repair((horizon,), p)
            independent = tuple(sorted(next(m for m in range(horizon+1, horizon+p**a+1)
                                            if (8*m-d) % p**a == 0)
                                       for d in (7,4,3,2)))
            assert plan.appended_clocks == plan.basis_clocks == independent
            assert len(set(independent)) == 4
            assert horizon < min(independent) <= max(independent) <= horizon+p**a
            assert plan.history == (horizon,)+independent
            chart = o.prime_chart(independent, p)
            supports = []
            for clock, exponent, row in zip(independent, chart.exponents, chart.matrix):
                target = next(j for j,d in enumerate((7,4,3,2)) if (8*clock-d) % p**a == 0)
                assert exponent == vp(8*clock-(7,4,3,2)[target], p) >= a
                support = [j for j,value in enumerate(row) if vp(value, p) == 0]
                assert support == [target]
                supports.extend(support)
                checks += 2
            assert sorted(supports) == [0,1,2,3]
            assert vp(permutation_det(chart.matrix), p) == 0
            assert chart.rank == 4 and chart.loss == 0
            checks += 7
            odd_repair_receipts.append({"p": p, "horizon": horizon,
                                       "clock_depth": a, "future_clocks": independent,
                                       "actual_pole_depths": chart.exponents})

    for clock in (1,2,3,13,55,89,144,233,29525,1000000):
        normalized = tuple(F(4,8*clock-d) for d in (7,4,3,2))
        residue = tuple(x.numerator*pow(x.denominator,-1,2) % 2 for x in normalized)
        assert residue == (0,1,0,0)
        checks += 1
    try:
        o.plan_polar_repair((233,), 2)
    except ValueError:
        pass
    else:
        raise AssertionError("polar clock repair must reject the nonunit multiplier at2")
    checks += 1

    # The stronger one-chart repair uses every odd prime simultaneously. Check
    # its integer Smith factors via gcds of all minors, not a p-adic inverse.
    for start in (*range(1,31),233,236,131072,131078,1000000,10**12+2):
        clocks = tuple(range(start, start+4))
        scales = []
        for clock in clocks:
            denominators = tuple(8*clock-d for d in (7,4,3,2))
            repeated = 2 * (3 if clock % 3 == 2 else 1) * (5 if clock % 5 == 4 else 1)
            assert prod(denominators) % repeated == 0
            scales.append(prod(denominators)//repeated)
        independent_matrix = tuple(tuple(scale//(8*clock-d) for d in (7,4,3,2))
                                   for scale,clock in zip(scales,clocks))
        assert o.row_denominator_lcms(clocks) == tuple(scales)
        assert o.cleared_cauchy_matrix(clocks) == independent_matrix
        extra = (3 if start % 3 != 2 else 1) * (5 if start % 5 == 0 else 1)
        ds = integer_divisors(independent_matrix)
        assert ds == [1,1,4,256,2**19*extra]
        assert permutation_det(independent_matrix) == 2**19*extra
        universal_repair_receipts.append({"start": start, "row_scales": scales,
                                          "determinantal_divisors": ds,
                                          "smith_invariants": [ds[i]//ds[i-1] for i in range(1,5)]})
        checks += 8
    delays = []
    for horizon in (*range(1,46),233,131072,10**12):
        plan = o.plan_universal_repair((horizon,))
        allowed = next(n for n in range(horizon+1,horizon+7) if n % 15 in (2,8,11,14))
        assert plan.basis_clocks == plan.appended_clocks == tuple(range(allowed,allowed+4))
        assert plan.history == (horizon,)+plan.appended_clocks
        assert plan.binary_loss == 11
        assert horizon < plan.appended_clocks[0] <= plan.appended_clocks[-1] <= horizon+9
        assert permutation_det(o.cleared_cauchy_matrix(plan.basis_clocks)) == 2**19
        delays.append(plan.appended_clocks[-1]-horizon)
        checks += 5
    assert max(delays) == 9
    checks += 1

    # All-clock integer row lattice closure. The claimed integer coefficients
    # are obtained from a separate adjugate inverse and then used to reconstruct
    # each row exactly. This is a finite control of the Newton/dyadic proof.
    closure_clocks = (*range(1,64),233,1000000,10**12+1)
    sharp_control = None
    for start in (2,8,236,131072):
        basis = o.cleared_cauchy_matrix(tuple(range(start,start+4)))
        assert permutation_det(basis) == 2**19
        inv = adjugate_inverse(basis)
        assert all(sum((basis[i][k]*inv[k][j] for k in range(4)),F()) == (i == j)
                   for i in range(4) for j in range(4))
        checks += 2
        rows = []
        for clock in closure_clocks:
            denominators = tuple(8*clock-d for d in (7,4,3,2))
            repeated = 2 * (3 if clock % 3 == 2 else 1) * (5 if clock % 5 == 4 else 1)
            scale = prod(denominators)//repeated
            row = tuple(scale//d for d in denominators)
            weights = tuple(sum((row[i]*inv[i][j] for i in range(4)),F()) for j in range(4))
            assert all(x.denominator == 1 for x in weights)
            assert all(sum((weights[i]*basis[i][j] for i in range(4)),F()) == row[j]
                       for j in range(4))
            rows.append(row)
            checks += 2
        integer_row_closure_receipts.append({"basis_start": start,
                                            "independent_adjugate_rows_checked": len(rows),
                                            "clocks": closure_clocks})
        if start == 2:
            _, worst_column = next((i,j) for i in range(4) for j in range(4)
                                   if vp(inv[i][j],2) == -11)
            delta = tuple(2**11*inv[i][worst_column] for i in range(4))
            assert all(x.denominator == 1 for x in delta) and any(x.numerator % 2 for x in delta)
            assert all(sum((basis[i][j]*delta[j] for j in range(4)),F())
                       == 2**11*(i == worst_column) for i in range(4))
            checks += 2
            for row in rows:
                assert sum((row[j]*delta[j] for j in range(4)),F()) % 2**11 == 0
                checks += 1
            sharp_control = {"basis_start": 2, "coefficient_difference": [int(x) for x in delta],
                             "data_precision": 11, "coefficient_mod2_distinction_lost": True,
                             "scope": "cleared innovations only; no seed or terminal-channel constraint"}

    # Same-source exact stationary causal chart, including a rational seed alias.
    for seed in (F(), F(1, 16), F(-2, 7)):
        journal = o.make_journal(31, seed=seed)
        partial = F()
        for n in range(32):
            if n:
                partial += rational_forcing(n) / 16**n
            assert journal.states[n] / 16**n - partial == seed
            checks += 1
        if seed:
            assert not o.validate_journal(journal, authentic=True)
            checks += 1
    base, alias = o.make_journal(31), o.make_journal(31, seed=F(1, 16))
    assert all((a-b) % 1 == 0 for a, b in zip(alias.states[1:], base.states[1:]))
    assert o.recover(o.observe(alias, (3, 5, 8, 13)))[1] == F(1, 16)
    checks += 2

    # Direct eigenrow nonlift certificate, without any matrix-order routine.
    t = ((16,32,24,8,1), (8,20,18,7,1), (4,12,13,6,1),
         (2,7,9,5,1), (1,4,6,4,1))
    b = [[t[i][j]-16*(i == j) for j in range(5)] for i in range(5)]
    ell, v = (4,2,10,10,1), (4,6,9,8,1)
    d = [sum(ell[i]*b[i][j] for i in range(5))//11 for j in range(5)]
    assert d == [7,30,18,0,1]
    assert all(sum(b[i][j]*v[j] for j in range(5)) % 11 == 0 for i in range(5))
    assert sum(d[i]*v[i] for i in range(5)) % 11 == 8
    assert permutation_det([[-z for z in row] for row in b]) == -1076625
    checks += 4

    assert gcd(11*(16**4-1), 7*(16**6-1)) == 255
    assert (720885*F(1,255)) % 1 == (117440505*F(1,255)) % 1 == 0
    assert (15*F(1,255)) % 1 == F(1,17)
    checks += 3

    # Alternative exact BBP interval brackets the independent Machin interval's
    # midpoint; both methods need not have nested intervals.
    b_lo, b_hi = bbp_pi_interval()
    m_lo, m_hi = w.pi_interval()
    assert m_lo < b_hi and b_lo < m_hi
    checks += 1

    table, scale, terr = w.trig_table()
    table_nodes = (0,1,23,511,1023,1024,1345,2047,2048,3071,3072,4095)
    for index in table_nodes:
        (crl, cru), (sil, siu) = direct_phasor_interval(F(index, 4096))
        c, s = (F(z, scale) for z in table[index])
        assert c-terr <= crl <= cru <= c+terr
        assert s-terr <= sil <= siu <= s+terr
        checks += 2

    phases = (F(), F(1,6), F(2,3), F(1,8), F(47,53), F(4095,4096), F(-1,17))
    mean_receipts = []
    for h in (1,7,11,15,720885,117440505,-7):
        result = w.rational_sample_mean(phases, h)
        references = [direct_phasor_interval(h*t) for t in phases]
        for component, name in ((0, "real_interval"), (1, "imag_interval")):
            lo = sum((x[component][0] for x in references), F()) / len(phases)
            hi = sum((x[component][1] for x in references), F()) / len(phases)
            claimed_lo, claimed_hi = map(F, result[name])
            assert claimed_lo <= lo <= hi <= claimed_hi
            checks += 1
        mean_receipts.append({"h": h, "comparison": "full-angle rational enclosure contained"})

    # Small-n source/index audit. U_n plus a separately bounded literal future
    # tail must occupy the same hexadecimal cylinder as prefix[n-1:...].
    prefix = w.bulk_pi_hex_digits(64)
    width = 8
    journal = o.make_journal(40)
    prefix_checks = []
    for n in (1,2,3,7,16,31,40):
        word = int(prefix[n-1:n-1+width], 16)
        q = 16**width
        tail_low = sum((rational_forcing(n+j) / 16**j for j in range(1, 49)), F())
        tail_high = tail_low + rational_forcing(n+49)/(15*16**48)
        ylo, yhi = journal.states[n]+tail_low, journal.states[n]+tail_high
        # A strict finite cell agreement, with the full integer lift retained.
        integer = ylo.__floor__()
        assert yhi.__floor__() == integer
        assert (ylo-integer)*q >= word and (yhi-integer)*q < word+1
        # Independent pi interval scaled by exactly16^(n-1) agrees as well.
        rlo, rhi = 16**(n-1)*b_lo, 16**(n-1)*b_hi
        assert rlo.__floor__() == rhi.__floor__() == integer
        assert (rlo-integer)*q >= word and (rhi-integer)*q < word+1
        prefix_checks.append({"n": n, "eight_hex_digits": format(word, "08X")})
        checks += 4

    # Deliberately broken mutations must separate on calibrated controls.
    balanced = w.rational_sample_mean((F(j, 16) for j in range(16)), 1)
    omitted_compensator = w.rational_sample_mean((F() for _ in range(16)), 1)
    assert F(balanced["real_interval"][1]) < F(omitted_compensator["real_interval"][0])
    checks += 1
    # Off-by-one prefix indexing is caught without high-precision floating pi.
    assert prefix[0:width] != prefix[1:1+width]
    checks += 1
    # Conjugating all signs must be detected at a phase with nonzero imaginary part.
    signed = w.rational_sample_mean((F(1, 4),), 1)
    reversed_sign = w.rational_sample_mean((F(1, 4),), -1)
    assert F(signed["imag_interval"][0]) > F(reversed_sign["imag_interval"][1])
    checks += 1

    return {"status": "PASS_FINITE_INDEPENDENT_IMPLEMENTATION_AUDIT",
            "asserted_checks": checks,
            "prime_divisor_receipts": prime_receipts,
            "all_odd_prime_repair_receipts": odd_repair_receipts,
            "universal_integer_chart_receipts": universal_repair_receipts,
            "maximum_universal_repair_delay_observed": max(delays),
            "integer_row_closure_receipts": integer_row_closure_receipts,
            "sharp_binary_closure_control": sharp_control,
            "table_nodes_checked": table_nodes,
            "signed_means_checked": mean_receipts,
            "source_prefix_index_checks": prefix_checks,
            "direct_nonlift_obstruction_mod11": 8,
            "fixed_lag_bank_kernel_order": 255,
            "mutations_detected": ["omitted frame compensation", "wrapped seed alias",
                                   "one-digit prefix offset", "reversed Fourier sign"],
            "arithmetic": "standard-library exact rational and integer",
            "fresh_shell_used_for_audit_design": False,
            "asymptotic_claim": "none"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
