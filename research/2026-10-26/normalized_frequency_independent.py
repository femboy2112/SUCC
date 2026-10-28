#!/usr/bin/env python3
"""Independent numerical audit; imports no SUCC production modules.

Complex endpoint integration and a separate oscillatory quadrature calibrate
the paper formulas. Numerical output is diagnostic, not a proof certificate.
The authentic infinite interval law is cut at j=24 with omitted mass 16^-24.
Both controls are evaluated without a geometric cutoff.
"""
from fractions import Fraction as Q
import json
import sys

import mpmath as mp


PRECISION = 80
DEPTH = 24
POLE_PAIRS = ((3, 2), (4, 1), (5, 1))
ATOMS = ((Q(1), Q(73, 148)), (Q(89, 15), Q(75, 148)))
CELLS = ((1, Q(1, 2)), (3, Q(1, 4)), (7, Q(1, 4)))


def decimal(q):
    q = Q(q)
    return mp.mpf(q.numerator) / q.denominator


def interval_law(depth):
    return [(8*j-7, d, Q(v, 16**j))
            for j in range(1, depth+1) for d, v in POLE_PAIRS]


def integrated_interval_law(n, k, intervals):
    """Finite exact antiderivative formulas, evaluated with mpmath.

    Inputs are unnormalized constant densities on [start,start+width].
    Integrands: w=(1+B/a)^-2, w*exp(-i*t*log(1+B/a)), w*log(1+B/a).
    """
    a = mp.mpf(8*n)
    t = 2*mp.pi*k*a
    phase, mass, lognum = mp.mpc(0), mp.mpf(0), mp.mpf(0)
    for start, width, weight in intervals:
        left, right = 1+mp.mpf(start)/a, 1+mp.mpf(start+width)/a
        scale = decimal(weight)*a
        phase += scale*(right**(-1-1j*t)-left**(-1-1j*t))/(-1-1j*t)
        mass += scale*(1/left-1/right)
        lognum += scale*((1+mp.log(left))/left-(1+mp.log(right))/right)
    return phase/mass, lognum/mass, mass/a**2


def atomic_law(n, k):
    a = mp.mpf(8*n)
    phase, mass, lognum = mp.mpc(0), mp.mpf(0), mp.mpf(0)
    for point, probability in ATOMS:
        x, p = decimal(point)/a, decimal(probability)
        weight = p/(1+x)**2
        mass += weight
        phase += weight*mp.exp(-2j*mp.pi*k*a*mp.log1p(x))
        lognum += weight*mp.log1p(x)
    return phase/mass, lognum/mass, mass/a**2


def number(x):
    return mp.nstr(x, 22)


def complex_number(z):
    return {"real": number(z.real), "imaginary": number(z.imag)}


def readings(n, values):
    theta, eta, tail = values
    return {"theta": complex_number(theta),
            "theta_modulus": number(abs(theta)),
            "a_theta": complex_number(8*n*theta),
            "theta_over_eta": complex_number(theta/eta),
            "theta_modulus_squared_over_tail": number(abs(theta)**2/tail),
            "eta": number(eta), "tail": number(tail)}


def direct_quadrature():
    n, k, depth = 64, 15, 6
    a = mp.mpf(8*n)
    phase, mass = mp.mpc(0), mp.mpf(0)
    intervals = interval_law(depth)
    for start, width, weight in intervals:
        grid = [mp.mpf(start)+mp.mpf(r)/4 for r in range(4*width+1)]
        phase += decimal(weight)*mp.quad(
            lambda b: mp.exp(-2j*mp.pi*k*a*mp.log1p(b/a))/(1+b/a)**2,
            grid)
        mass += decimal(weight)*mp.quad(lambda b: 1/(1+b/a)**2, grid)
    endpoint = integrated_interval_law(n, k, intervals)[0]
    return {"n": n, "k": k, "geometric_depth": depth,
            "endpoint_theta": complex_number(endpoint),
            "quadrature_theta": complex_number(phase/mass),
            "absolute_disagreement": number(abs(phase/mass-endpoint))}


def main():
    mp.mp.dps = PRECISION
    authentic = interval_law(DEPTH)
    uniform_cells = [(start, 1, probability) for start, probability in CELLS]
    rows = []
    for k in (1, 15):
        for n in (8, 64, 512, 4096, 65536, 1048576):
            a = mp.mpf(8*n)
            rows.append({
                "n": n, "k": k,
                "authentic": readings(n, integrated_interval_law(n, k, authentic)),
                "two_atom_control": readings(n, atomic_law(n, k)),
                "uniform_cell_control": readings(n, integrated_interval_law(n, k, uniform_cells)),
                "paper_modulus_upper_bound": number(
                    (7+55*mp.pi*abs(k)/3)/a*(1+7/(2*a))**2),
                "first_order_target_a_theta": complex_number(-mp.mpf(7)/2-1j/(2*mp.pi*k)),
                "target_theta_over_eta": complex_number(-1-1j/(7*mp.pi*k)),
                "target_theta_modulus_squared_over_tail": number(
                    mp.mpf(49)/4+1/(4*mp.pi**2*k*k))})
    exact_controls = {
        "atom_mean": str(sum((p*b for b, p in ATOMS), Q())),
        "atom_second_moment": str(sum((p*b*b for b, p in ATOMS), Q())),
        "atom_tail_at_zero": str(sum((p/(b*b) for b, p in ATOMS), Q())),
        "uniform_cell_mean": str(sum((p*(Q(b)+Q(1,2)) for b, p in CELLS), Q())),
        "uniform_cell_second_moment": str(sum((p*(Q(b*b)+b+Q(1,3)) for b, p in CELLS), Q())),
        "uniform_cell_tail_at_zero": str(sum((p*(Q(1,b)-Q(1,b+1)) for b, p in CELLS), Q()))}
    report = {
        "status": "NUMERICAL DIAGNOSTICS; NOT PROOF CERTIFICATES",
        "python": sys.version.split()[0], "mpmath": mp.__version__,
        "decimal_precision": PRECISION, "authentic_geometric_depth": DEPTH,
        "authentic_omitted_mixing_mass_exact": str(Q(1,16**DEPTH)),
        "production_imports": [], "exact_control_moments": exact_controls,
        "rows": rows, "independent_quadrature": direct_quadrature(),
        "claims": {"auxiliary_source_cancellation_proved_by_this_script": False,
                   "selected_orbit_cancellation_proved": False,
                   "pi_normality_proved": False}}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
