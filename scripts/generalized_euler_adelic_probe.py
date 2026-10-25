#!/usr/bin/env python3
"""Source-aware EAB probe: exact rational controls vs numeric diagnostics."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q

from observational_succ.generalized_euler_adelic import (
    analytically_continued_zero_power, cell_certificate,
    certified_pi_hex_prefix, cofinal_prime_schedule,
    euler_product_exact, literal_zero_power, positive_type_hostile_zero,
    symmetric_functional_equation_mutant, theta_balanced_completed,
    theta_balanced_integral,
)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',action='store_true',
                        help='assert rational algebra and bounded numerical controls')
    args=parser.parse_args()
    cert=cell_certificate(2,50)
    schedule=cofinal_prime_schedule(3)
    true=euler_product_exact(2,5)
    fake=euler_product_exact(2,5,fake_composite=6)
    hex3=certified_pi_hex_prefix(50,3)
    hex4=certified_pi_hex_prefix(300,4)
    b1=theta_balanced_completed(1,60)
    bint=theta_balanced_integral(1,8,60)
    offaxis=positive_type_hostile_zero(60)

    if args.verify:
        assert literal_zero_power(50)==Q(1)
        assert analytically_continued_zero_power()==Q(1,2)
        assert true==Q(25,16) and fake==Q(45,28)
        assert schedule.cutoff==729
        assert schedule.proved_absolute_euler_error_leq==Q(1,3)
        assert hex3=="3.243" and hex4=="3.243F"
        assert cert.upper-cert.lower==Q(1,5000)
        assert abs(b1-bint)<1e-40
        assert abs(offaxis['residual'])<1e-40
        assert symmetric_functional_equation_mutant(Q(2))!=1
        assert (symmetric_functional_equation_mutant(Q(1,4))==
                symmetric_functional_equation_mutant(Q(3,4)))

    report={
        "program":"EAB-generalized-Euler-adeles",
        "verification":"passed" if args.verify else "not_requested",
        "source":"local exact rational and high-precision numeric controls only",
        "gamma_zero_literal":str(literal_zero_power(50)),
        "gamma_zero_entire_continuation":str(analytically_continued_zero_power()),
        "gamma_two_lower_rational":str(cert.lower),
        "gamma_two_upper_rational":str(cert.upper),
        "prime_cutoff_q3":schedule.cutoff,
        "prime_cutoff_paper_error_bound":str(schedule.proved_absolute_euler_error_leq),
        "true_euler_s2_X5":str(true),
        "fake6_euler_s2_X5":str(fake),
        "basel_pi_hex_N50":hex3,
        "basel_pi_hex_N300":hex4,
        "theta_B_one_numeric":str(b1),
        "theta_integral_residual_numeric":str(abs(b1-bint)),
        "positive_type_off_axis_zero":str(offaxis["zero"]),
        "positive_type_residual_numeric":str(abs(offaxis["residual"])),
        "analytic_theorems_proved_by_numeric":False,
        "physical_source_authenticated":False,
        "pi_normality_proved":False,
        "RH_proved":False,
    }
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
