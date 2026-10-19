#!/usr/bin/env python3
"""Stable exact rational certificates, no floating integral quadrature."""
from fractions import Fraction as F
from json import dumps
from math import prod
from observational_succ.factorial_borwein_hologram import (
    kernel_at, kernel_variance, increment_windows, exact_continuous_gram,
    repeated_width_sum, infinite_tail_budget, reconstructed_sinc_polynomial,
    poisson_wheel_polynomial, plateau_radius, support_radius,
)


def receipt():
    rows = []
    for n in (3, 4, 5, 6, 7, 8):
        added = increment_windows(n) if n >=2 else ()
        rows.append({
            "n": n,
            "new_repeated_windows": [[w.prime,w.depth] for w in added],
            "variance": str(kernel_variance(n)),
            "integer_cardinal_samples": [str(kernel_at(n,F(k))) for k in range(-2,3)],
            "half_grid_sample":str(kernel_at(n,F(1,2))),
            "off_grid_at_3_10":str(kernel_at(n,F(3,10))),
            "plateau_radius":str(plateau_radius(n)),
            "support_radius":str(support_radius(n)),
            "prime_step_from_variance":not bool(added),
        })
    return {
        "scope":"exact finite math; Borwein cardinal interpolation; no RH/ABC theorem",
        "source":"factorial Legendre valuations plus actual prime powers, canonical order",
        "rows":rows,
        "gram_n4":{k:str(v) for k,v in exact_continuous_gram(4).items()},
        "gram_n6":{k:str(v) for k,v in exact_continuous_gram(6).items()},
        "sinc_spectral_polynomial_n6":[str(c) for c in reconstructed_sinc_polynomial(6)],
        "infinite_uniform_tail_bound_n8":str(2*infinite_tail_budget(8)),
        "poisson_wheel_start0_gates3and5_time2over3_degree9":{
            "unnormalized_polynomial":str(poisson_wheel_polynomial(
                0,((3,"one"),(5,"nonzero")),F(2,3),9)[0]),
            "actual_probability_tail_bound":str(poisson_wheel_polynomial(
                0,((3,"one"),(5,"nonzero")),F(2,3),9)[1]),
        },
        "source_boundary":"Sampling erases kernel label N; off-grid or spectral probes are essential.",
        "weill_boundary":"Positive probability convolution and L2 Gram are NOT the signed completed Weil form",
    }


if __name__=="__main__":
    print(dumps(receipt(),sort_keys=True,indent=2))
