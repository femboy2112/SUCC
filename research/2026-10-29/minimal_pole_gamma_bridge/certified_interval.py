"""Exact rational certificate of harmonic/Gamma finite-part enclosure.

Not a numeric floating-point certification and does not assume an input value of gamma.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json
from minimal_pole_gamma import (
    harmonic_finite_part_interval, native_log_gap_bounds, harmonic,
    gamma_product_exact, minimal_weight_solution)

def frac(q):return {'num':str(q.numerator),'den':str(q.denominator)}

def main():
    N=128; terms=4
    lower,upper=harmonic_finite_part_interval(N,terms)
    assert 0 < lower < upper
    assert upper-lower < F(7,180*N)+F(1,10**10)
    l12,u12=harmonic_finite_part_interval(12,terms)
    assert l12 > F(1,20)
    o={
      'version':'minimal-pole-gamma-certificate-v1',
      'finite_N':N,
      'atanh_terms':terms,
      'lower_rational':frac(lower),
      'upper_rational':frac(upper),
      'strict_bound':'lower < K_H < upper; follows from positive atanh remainder and all-n 7/(180n^2) tail',
      'lower_display':format(float(lower),'.17g'),
      'upper_display':format(float(upper),'.17g'),
      'twelve_term_lower_above_one_twentieth':l12>F(1,20),
      'original_positive_weight_grammar_minimizer':str(minimal_weight_solution()),
      'clock_first_adjustment':str(gamma_product_exact(1)),
      'harmonic128':str(harmonic(N)),
      'numeric_values_are_displays_not_proofs':True,
      'pi_normality':'OPEN'
    }
    target=Path(__file__).resolve().parent/'receipts'/'K_H_CERTIFICATE.json'
    target.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n')
    print('RATIONAL_K_H_CERTIFICATE_PASS',str(target))
    print('K_H interval display',o['lower_display'],o['upper_display'])

if __name__=='__main__':main()
