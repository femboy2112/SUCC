"""Independent exact/symbolic replay for the original BBP Dirichlet response.

Default: emit deterministic JSON on stdout.  --output writes only the requested
path; --verify compares with the committed receipt without rewriting it.
Numerical mpmath checks are diagnostics, never interval or kernel certificates.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import bbp_dirichlet_resolvent as implementation

RECEIPT = ROOT / "research/2026-10-28/BBP_DIRICHLET_RESOLVENT_RECEIPT.json"


def rational(value):
    return sp.Rational(value.numerator, value.denominator)


def run():
    n, x = sp.symbols("n x")
    # Start with the literal signed source, not the module's derived constants.
    r = 4/(8*n-7) - 2/(8*n-4) - 1/(8*n-3) - 1/(8*n-2)
    numerator, denominator = sp.fraction(sp.cancel(r))
    lead = sp.Poly(denominator, n).LC()
    P, Q = numerator/lead, denominator/lead
    q_coefficients = [sp.expand(Q).coeff(n,k) for k in range(5)]
    p_coefficients = [sp.expand(P).coeff(n,k) for k in range(3)]
    assert q_coefficients == list(map(rational, implementation.SHIFT_DENOMINATOR))
    assert p_coefficients == list(map(rational, implementation.SHIFT_NUMERATOR))
    assert sp.gcd(P,Q) == 1
    resultant = sp.resultant(Q,P,n)
    assert resultant == sp.Rational(-225, 549755813888)
    roots = sorted(sp.solve(Q,n), reverse=True)
    weights = [sp.cancel((n-b)*r).subs(n,b) for b in roots]
    assert len(roots) == 4 and all(P.subs(n,b) != 0 for b in roots)
    expansion = sp.series(r.subs(n,1/x), x, 0, 16).removeO().expand()
    for k in range(1,16):
        assert expansion.coeff(x,k) == rational(implementation.asymptotic_coefficient(k))

    # This rational four-mode moment certificate is independent of the source
    # time-sequence Hankel operator and does not assert finite Green-tail rank.
    moments = [sum(w*b**j for w,b in zip(weights,roots)) for j in range(9)]
    hankel = sp.Matrix([[moments[i+j] for j in range(4)] for i in range(4)])
    assert hankel.det() == resultant

    sqrt2 = sp.sqrt(2)
    logratio = sp.log(2+sqrt2)-sp.log(2-sqrt2)
    psi_table = {
        sp.Rational(1,8): -sp.EulerGamma-4*sp.log(2)-sp.pi*(1+sqrt2)/2-sqrt2*logratio/2,
        sp.Rational(1,2): -sp.EulerGamma-2*sp.log(2),
        sp.Rational(5,8): -sp.EulerGamma-4*sp.log(2)-sp.pi*(1-sqrt2)/2+sqrt2*logratio/2,
        sp.Rational(3,4): -sp.EulerGamma-3*sp.log(2)+sp.pi/2,
    }
    for argument, value in psi_table.items():
        assert sp.simplify(sp.expand_func(sp.digamma(argument))-value) == 0
    assert sp.simplify((2+sqrt2)/(2-sqrt2)-(1+sqrt2)**2) == 0

    basis = [1,sp.EulerGamma,sp.pi,sqrt2*sp.pi,sp.log(2),sqrt2*logratio/2]
    finite_parts = []
    for m in range(13):
        quotient, remainder = sp.div(n**m*P,Q,n)
        assert sp.cancel(n**m*r - quotient - remainder/Q) == 0
        assert sp.cancel(remainder/Q-sum(w*b**m/(n-b) for w,b in zip(weights,roots))) == 0
        poly = sp.Poly(quotient,n)
        rational_part = sum(coefficient*sp.zeta(-power[0])
                            for power,coefficient in poly.terms())
        from_division = rational_part-sum(w*b**m*psi_table[1-b]
                                           for w,b in zip(weights,roots))
        coefficients = implementation.finite_part_basis_coefficients(m)
        from_basis = sum(rational(c)*v for c,v in zip(coefficients,basis))
        assert sp.simplify(from_division-from_basis) == 0
        finite_parts.append([str(c) for c in coefficients])

    # A positive different forcing with exactly matching first two residues.
    wrong = (numerator-sp.Rational(3,5))/denominator
    wrong_jet = sp.series(wrong.subs(n,1/x),x,0,5).removeO().expand()
    assert wrong_jet.coeff(x,2) == expansion.coeff(x,2)
    assert wrong_jet.coeff(x,3) == expansion.coeff(x,3)
    assert wrong_jet.coeff(x,4)-expansion.coeff(x,4) == -sp.Rational(15,12800)
    assert sp.cancel(Q*wrong-P) == -sp.Rational(3,2560)
    nonmultiplicativity = sp.cancel(r.subs(n,6)*r.subs(n,1)-r.subs(n,2)*r.subs(n,3))
    assert nonmultiplicativity != 0

    mp.mp.dps = 70
    def mpr(value):
        value = sp.Rational(value)
        return mp.mpf(int(value.p))/int(value.q)
    mroots, mweights = list(map(mpr,roots)), list(map(mpr,weights))
    aa = [mpr(implementation.asymptotic_coefficient(k)) for k in range(2,901)]
    def response_at(s):
        return mp.fsum(a*mp.zeta(s+k) for k,a in enumerate(aa,2))
    C1 = -mp.fsum(w*b*mp.digamma(1-b) for w,b in zip(mweights,mroots))
    Cclosed = (mp.mpf(15)/64*mp.euler+(27+31*mp.sqrt(2))*mp.pi/128
               +mp.mpf(39)/32*mp.log(2)+31*mp.sqrt(2)/64*mp.log(1+mp.sqrt(2)))
    assert abs(C1-Cclosed) < mp.mpf("1e-65")
    for m in range(1,7):
        epsilon = mp.mpf("1e-22")
        near = response_at(-m+epsilon)-mpr(implementation.pole_residue(m))/epsilon
        exact = (mp.fsum(mpr(moments[j])*mp.zeta(j+1-m) for j in range(m))
                 -mp.fsum(w*b**m*mp.digamma(1-b) for w,b in zip(mweights,mroots)))
        assert abs(near-exact) < mp.mpf("1e-18")
    s = mp.mpc("2.75","3.125")
    shift_left = mp.fsum(mpr(c)*response_at(s-j) for j,c in enumerate(q_coefficients))
    shift_right = mp.fsum(mpr(c)*mp.zeta(s-j) for j,c in enumerate(p_coefficients))
    assert abs(shift_left-shift_right) < mp.mpf("1e-48")

    # Independent direct source prefix at s=2, with the inherited elementary
    # r(n)<=1/n^2 for n>=2. Numerical comparison is still not interval arithmetic.
    horizon = 2000
    direct = mp.fsum((4/mp.mpf(8*j-7)-2/mp.mpf(8*j-4)
                     -1/mp.mpf(8*j-3)-1/mp.mpf(8*j-2))/j**2
                    for j in range(1,horizon+1))
    value2 = response_at(mp.mpf(2))
    direct_tail_bound = Fraction(1,3*horizon**3)
    assert 0 < value2-direct < mpr(direct_tail_bound)

    source = ROOT / "observational_succ/pi_source_collision.py"
    return {
        "schema": "SUCC-original-BBP-Dirichlet-resolvent-v1",
        "parent": "fec9b7a72dd6b8c7550d7915070ee8094f2b94a2",
        "source": "r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2); forcing response only",
        "source_path": "observational_succ/pi_source_collision.py",
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "Q_ascending": list(map(str,q_coefficients)),
        "P_ascending": list(map(str,p_coefficients)),
        "Q_P_resultant": str(resultant),
        "four_mode_Hankel_determinant": str(hankel.det()),
        "residues_at_minus_1_through_minus_14": [str(implementation.pole_residue(m)) for m in range(1,15)],
        "finite_part_basis": list(implementation.FINITE_PART_BASIS),
        "finite_part_coefficients_m_0_through_12": finite_parts,
        "finite_part_minus_1_40_digits": mp.nstr(C1,40),
        "F_at_2_40_digits": mp.nstr(value2,40),
        "complex_shift_relation_numeric_residual_below": "1e-48",
        "Laurent_constants_m_1_through_6_numeric_error_below": "1e-18",
        "zeta_expansion_terms": 900,
        "direct_source_prefix_at_2_terms": horizon,
        "direct_source_prefix_tail_bound": str(direct_tail_bound),
        "wrong_source_first_two_residues_match": True,
        "wrong_source_third_residue_change": "-15/12800",
        "wrong_source_shift_relation_residual": "-3/2560",
        "normalized_multiplicativity_defect_r6r1_minus_r2r3": str(nonmultiplicativity),
        "status": "EXACT FINITE symbolic certificates; numerical diagnostics; universal claims require dossier proofs",
        "seed_identified": False,
        "pi_normality": "OPEN",
        "RH": "OPEN",
        "academic_priority": "UNVERIFIED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write deterministic JSON to this path")
    parser.add_argument("--verify", action="store_true", help="compare committed receipt, without writing")
    args = parser.parse_args()
    if args.output is not None and args.verify:
        parser.error("--output and --verify are mutually exclusive")
    encoded = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.verify:
        if RECEIPT.read_text() != encoded:
            raise SystemExit("FAIL: committed BBP Dirichlet resolvent receipt differs")
        print("PASS: exact symbolic and numerical BBP resolvent receipt replay")
    elif args.output is not None:
        args.output.write_text(encoded)
        print(f"Wrote {args.output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
