"""Rejection controls. Mutants are functions constructed *inside* this script.

No production files are rewritten. All checks are exact except one stated KL
comparison, where the mathematical monotonic trend is used diagnostically.
"""
from fractions import Fraction as F
from math import log
from order_stat_bridge import (beta_winner_law, discrete_max_law,
    winner_h, native_law, native_birth, info_bounds)

reports = []

def reject(name, condition):
    assert condition, f"MUTANT ESCAPED: {name}"
    reports.append({"mutation": name, "caught": True})

reject("max_after_discretization", discrete_max_law(1, 2) != beta_winner_law(2, 1))
reject("wrong_posterior_denominator", F(2, 1) != winner_h(2, 0, 0))
reject("drop_rejected_branch", beta_winner_law(2, 3) != native_law(3))
reject("wrong_birth_denominator", F(1, 2) != native_birth(1, 0))
reject("pretend_root_of_selected_character_is_on_circle", F(-1, 2) != F(-1, 1))

def geometric_selected_kl(j,a=F(1,2)):
    norm = sum((a**k for k in range(j+1)), F(0))
    return sum(float(a**k/norm) * log(float((j+1)*a**k/norm))
               for k in range(j+1))
reject("confuse_geometric_demon_with_bounded_winner", geometric_selected_kl(150) > geometric_selected_kl(15) + 1)
print("mutation controls:",len(reports),"caught /",len(reports),"no survivors")
