"""Emit exact full Gauss objects, unit data, source controls and conductor witnesses."""
import json
from fractions import Fraction

from gauss_exact import (AUTH, MUTATION, Cyclo, GaussSystem, cofiber,
    gk_unit_mod, orbit, source, valuation, verify_gk_unit_power)


def main():
    rows = []
    for p in (3, 5, 7, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 71, 73, 89):
        system = GaussSystem(p)
        ratio = system.weighted(MUTATION)
        assert ratio == system.character(2, 2)
        assert ratio.power(2) == Cyclo.monomial(p)
        unit = verify_gk_unit_power(system)
        mutants = []
        for k in (5, 9, 13, 17):
            t = 2**(k+2)
            c = tuple(a+t*b for a, b in zip(AUTH, MUTATION))
            um = gk_unit_mod(p, 3, c)
            assert um == unit["unit_mod_p_power"]
            mutants.append({"k":k,"t":t,"unit_mod_p3":um})
        rows.append({"p":p,"f":system.field.f,"q":system.field.q,
            "quadratic_nonsquare":system.field.d,"generator":list(system.field.generator),
            "normalization":"chi(g)=zeta8^-1; additive character zeta_p^Trace(x)",
            "gauss_sums":{str(d):g.record() for d, g in system.sums.items()},
            "authentic_weighted_product":system.weighted().record(),
            "mutation_quotient":ratio.record(),"gk":unit,"mutants":mutants})
    births = []
    for p, n in ((13,2),(19,5),(19,9),(19,10),(19,16),(19,17),(73,10),(73,273),(73,274),
                 (17,3),(29,4),(43,11),(47,12)):
        u = orbit(n)
        a, P, v = cofiber(u, p)
        births.append({"p":p,"n":n,"valuation":valuation(u,p),
            "primary_numerator":a,"primary_denominator":P,"cofiber":str(v),
            "foreign_odd_prime":next(ell for ell in (3,5,7,11,17,19,23,29,31,37,41,43,47,53)
                                     if ell != p and v.denominator % ell == 0)})
    blind = []
    for k in (5,9,13,17):
        t = 2**(k+2)
        c = tuple(a+t*b for a,b in zip(AUTH,MUTATION))
        dif = 13*(orbit(2,c)-orbit(2))
        blind.append({"k":k,"t":t,"times":[1,2,7,23,53],
            "source_v2":[valuation(source(n,c)-source(n),2) for n in (1,2,7,23,53)],
            "orbit_v2":[valuation(orbit(n,c)-orbit(n),2) for n in (1,2,7,23,53)],
            "p13_residue_difference":dif.numerator*pow(dif.denominator,-1,13)%13})
    print(json.dumps({"status":"PASS","authority":"exact finite checks; universal claims require paper proof",
        "gauss_rows":rows,"source_birth_and_cancellation_witnesses":births,
        "combined_GK_and_2adic_blind_controls":blind},indent=2))


if __name__ == "__main__":
    main()
