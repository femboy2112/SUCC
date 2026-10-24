#!/usr/bin/env python3
"""Independent symbolic audit and certified finite signed-correlation receipts.

Run from the repository root. No stored pi digits, empirical error bars or
finite-to-infinite promotions. JSON is deterministic and source-hash pinned.
"""
import argparse
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import sympy as s
from observational_succ import pi_source_genesis as g
from observational_succ.bbp_source_memory import tail_interval


def determinant_enclosure(size, terms=30):
    """Leibniz interval determinant, independent of existing Gaussian solver."""
    low = high = Q()
    matrix = [[tail_interval(i+j, terms) for j in range(size)] for i in range(size)]
    for perm in permutations(range(size)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(size) for j in range(i+1, size))
        a = b = Q(1)
        for i, j in enumerate(perm):
            a *= matrix[i][j][0]
            b *= matrix[i][j][1]
        low += a if sign == 1 else -b
        high += b if sign == 1 else -a
    assert low > 0
    return tuple(map(str, g.dyadic_enclosure(low, high, 100)))


def symbolic_audit():
    t = s.Symbol("t")
    H = 4+4*t+4*t**2+2*t**3+t**4
    kernel = 4-2*t**3-t**4-t**5
    h = H/(16-t**8)
    assert s.cancel(kernel-(1-t)*H) == 0
    assert s.cancel(h-1/(4-4*t+2*t**3-t**4)) == 0
    # Direct symbolic differentiation, unrelated to the production recurrence.
    direct = [s.diff(h, t, k).subs(t, 1)/s.factorial(k) for k in range(9)]
    assert tuple(direct) == tuple(s.Integer(v) for v in g.endpoint_coefficients(8))
    poles = [s.Rational(7,8), s.Rational(1,2), s.Rational(3,8), s.Rational(1,4)]
    weights = [s.Rational(1,2), -s.Rational(1,4), -s.Rational(1,8), -s.Rational(1,8)]
    moments = [sum(w*a**k for w, a in zip(weights, poles)) for k in range(5)]
    matrix = s.Matrix([[1/(n-a) for a in poles] for n in range(1,5)])
    assert matrix.det() == s.Rational(8388608,1224171073125)
    factors = []
    for d in range(1, 13):
        cyclotomic = {int(e): int(s.cyclotomic_poly(e, t).subs(t, 16)) for e in s.divisors(d)}
        assert s.prod(cyclotomic.values()) == 16**d-1
        primes = s.factorint(16**d-1)
        assert s.prod(p**k for p, k in primes.items()) == 16**d-1
        factors.append({"d": d, "cyclotomic_values": cyclotomic,
                        "prime_powers": {int(p): int(k) for p, k in primes.items()}})
    # Independently expand the u-density endpoint, before choosing a counterfeit.
    u = s.Symbol("u", positive=True)
    root = u**s.Rational(1,8)
    k = h.subs(t, root)/(8*root**7*sum(root**j for j in range(8)))
    jets = [s.diff(k, u, j).subs(u, 1)/s.factorial(j) for j in range(3)]
    assert jets == [s.Rational(1,64), -s.Rational(17,1024), s.Rational(141,8192)]
    p = s.Rational(1,64)+s.Rational(17,1024)*(1-u)+s.Rational(141,8192)*(1-u)**2
    mass = s.integrate((1-u)*p, (u,0,1))
    assert mass == s.Rational(1735,98304)
    # A genuinely non-coboundary positive counterfeit, from a zero log integral.
    log_derivative = -2*t/(2-t*t)-(2*t-2)/(t*t-2*t+2)
    W = (log_derivative+2)/8
    V = W-(1-t)**2/4
    vpoly = s.cancel((16-t**8)*V)
    certificate = (1-t)*(8+32*t+12*t**2+4*t**3+2*t**4+t**6+t**7+t**8*(1-t))/4
    assert s.expand(vpoly-certificate) == 0
    assert [s.diff(V-kernel/(16-t**8), t, j).subs(t,1) for j in range(4)] == [0]*4
    # Log endpoint ratio is1 at both ends, hence integral L=0, integral V=1/6.
    ratio = (2-t*t)/(t*t-2*t+2)
    assert ratio.subs(t,0) == ratio.subs(t,1) == 1
    assert s.cancel(s.diff(ratio,t)/ratio-log_derivative) == 0
    v_mass = s.Rational(1,4)-s.integrate((1-t)**2/4, (t,0,1))
    assert v_mass == s.Rational(1,6)
    coefficients = s.Poly(vpoly,t)
    # Orbit of index pole3/4: exponent j=1+8ell, weighted residue16^ell*c_j/8.
    invariant = sum(c*s.Integer(16)**((power[0]-1)//8)/8
                    for power,c in coefficients.terms() if power[0] % 8 == 1)
    assert invariant == -s.Rational(1,4)
    counterfeit_tail = v_mass
    counterfeit_values = []
    for n in range(1,13):
        r_value = sum(c/(8*n-7+power[0]) for power,c in coefficients.terms())
        counterfeit_tail = 16*counterfeit_tail-r_value
        assert 0 < counterfeit_tail < s.Rational(1,2)
        counterfeit_values.append(str(counterfeit_tail))
    family = []
    for m in range(1,5):
        Vm = kernel/(16-t**8)-(1-t)**(4*m)/(4*(1+(1-t)**2))
        difference_polynomial = s.cancel(Vm-V)
        assert difference_polynomial.is_polynomial(t)
        m_mass = sum((s.Rational((-1)**j,2*j+1) for j in range(2*m)),s.S.Zero)/4
        assert s.integrate(difference_polynomial,(t,0,1))+v_mass == m_mass
        alpha = 16*m_mass
        denominator = int(s.denom(alpha))
        assert denominator % 2 == 1
        period = 1 if denominator == 1 else int(s.n_order(16,denominator))
        assert pow(16, period, denominator) == 1 % denominator
        family.append({"m":m,"mass":str(m_mass),"selected_phase":str(alpha),
                       "exact_period":period,"tail_error_order":4*m+1,
                       "pole_invariant":"-1/4"})
    return {"endpoint_coefficients": list(map(int, direct)),
            "pole_moments": list(map(str, moments)),
            "cauchy_determinant": str(matrix.det()),
            "hankel_positive_intervals": {str(n): determinant_enclosure(n) for n in range(1,5)},
            "lag_factorizations": factors,
            "finite_jet_counterfeit": {"endpoint_jet": list(map(str, jets)),
                                       "mass": str(mass), "selected_phase": str(16*mass),
                                       "preperiod": 3, "eventual_fixed_point": "2/3"},
            "noncoboundary_counterfeit": {"kernel_numerator": str(s.expand(vpoly)),
                                          "mass": str(v_mass), "selected_fixed_phase": "2/3",
                                          "pole_class": "3/4", "pole_invariant": str(invariant),
                                          "endpoint_derivatives_matched_through": 3,
                                          "first_twelve_positive_tail_values": counterfeit_values,
                                          "arbitrary_order_family_checks":family}}


def boxes_overlap(a, b):
    return (max(a.real_low,b.real_low) <= min(a.real_high,b.real_high)
            and max(a.imag_low,b.imag_low) <= min(a.imag_high,b.imag_high))


def box_json(box):
    return {k: str(v) for k, v in asdict(box.outward()).items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    symbolic = symbolic_audit()
    from observational_succ.circle_collision_rigidity import pi_interval as polygon_pi
    polygon = polygon_pi(40, digits=130)
    machin = g.machin_pi_interval(90)
    assert polygon[0] < machin[0] < machin[1] < polygon[1]
    # The same selected correlation via genuine nested polygons; no ensemble.
    h0, n0, d0 = 1, 8, 3
    polygon_box = g.signed_sum_interval([
        (h0*(16**d0-1)*16**j*polygon[0], h0*(16**d0-1)*16**j*polygon[1])
        for j in range(n0-d0)])
    assert boxes_overlap(polygon_box, g.correlation_interval(h0,n0,d0))
    samples = []
    # Fixed, disclosed finite cases; these are not a normality holdout.
    for h, n, d in ((1, 8, 1), (1, 16, 3), (-1, 16, 7), (2, 32, 15), (1, 64, 31)):
        pi_box = g.correlation_interval(h, n, d)
        independent = g.correlation_interval(h, n, d, source="machin")
        forced = g.correlation_interval(h, n, d, source="forced")
        rational = g.correlation_interval(h, n, d, source="partial", lookahead=0)
        assert boxes_overlap(pi_box, independent)
        lag_budget = g.lag_transport_budget(h, 1, n-d, d)
        approx_budget = g.window_lag_transport_budget(h, n, d)
        assert (pi_box-forced).modulus_squared_upper() < lag_budget**2
        assert (pi_box-rational).modulus_squared_upper() < approx_budget**2
        samples.append({"h": h, "N": n, "d": d,
                        "C_pi": box_json(pi_box), "D_forced": box_json(forced),
                        "C_rational": box_json(rational),
                        "independent_machin_overlap": True,
                        "lag_error_upper": str(lag_budget),
                        "rational_error_upper": str(approx_budget)})
    conductors = []
    for m in (3, 7, 15, 31):
        p = g.window_pi_interval(m)[0]
        q = p.denominator
        v2 = (q & -q).bit_length()-1
        assert v2 == 4*(m-1)
        prime_powers = s.factorint(q)
        components = []
        for prime, exponent in prime_powers.items():
            modulus = int(prime**exponent)
            inverse = pow(q//modulus, -1, modulus)
            components.append(Q((p.numerator*inverse) % modulus, modulus))
        # Exact CRT transport of additive characters, INCLUDING signs/units.
        assert (sum(components, Q())-p) % 1 == 0
        conductors.append({"M": m, "numerator": str(p.numerator),
                           "denominator": str(q), "v2_denominator": v2,
                           "exact_preperiod": m-1,
                           "prime_powers": {str(k): int(v) for k,v in prime_powers.items()},
                           "crt_character_phases": list(map(str, components)),
                           "crt_phase_residual_mod_one": "0"})
    paths = ["observational_succ/pi_source_genesis.py", "observational_succ/bbp_source_memory.py",
             "scripts/pi_source_genesis_oracle.py", "tests/test_pi_source_genesis.py",
             "formal/duck_pi/BBPIntegral.lean", "formal/duck_pi/PiSource.lean"]
    data = {"status": "EXACT_FINITE_CERTIFICATES_NOT_AN_INFINITE_CANCELLATION_PROOF",
            "pi_normality_proved": False, "sources": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            "symbolic": symbolic, "signed_samples": samples, "rational_conductors": conductors,
            "polygon_selected_source": {"level": 40, "precision_digits": 130,
                                        "h": h0, "N": n0, "d": d0,
                                        "correlation": box_json(polygon_box),
                                        "bbp_overlap": True}}
    output = json.dumps(data, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
