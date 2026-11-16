"""Finite independent SymPy oracle for source inverses and endpoint readouts.

Production outputs are compared to literal source polynomials and to
Euler differentiation in the exponential coordinate. Proofs remain in
THEOREMS.md; this is an exact finite implementation audit.
"""
from pathlib import Path
import json
import sys
import time

import sympy as sp

from observational_succ.bbp_causal_inverse import inverse_kernel
from observational_succ.causal_negative_orders import bbp_negative_mellin


def main():
    started = time.monotonic()
    x = sp.symbols("x")
    literal_four_poles = 4/x-2/(x+3)-1/(x+4)-1/(x+5)
    source_n, source_d = (sp.Poly(p, x, domain=sp.QQ)
                          for p in sp.fraction(sp.cancel(literal_four_poles)))

    def poly(coefficients):
        return sp.Poly(sum(sp.Rational(c.numerator, c.denominator)*x**j
                           for j, c in enumerate(coefficients)), x, domain=sp.QQ)

    inverse_rows = []
    for m in range(9):
        kernel = inverse_kernel(m)
        delta = poly(kernel.delta_polynomial)
        remainder = poly(kernel.remainder_numerator)
        denominator = poly(kernel.remainder_denominator)
        assert denominator == source_n**m
        assert delta*denominator+remainder == source_d**m
        inverse_rows.append({"source_inverse_depth": m,
                             "delta_degree": delta.degree(),
                             "cleared_global_identity": True})

    # Literal native kernel in y=exp(-t), with no Mellin, jet or moment oracle.
    heat = x*(4-2*x**3-x**4-x**5)/(1-x**8/16)
    numerator, denominator = (sp.Poly(p, x, domain=sp.QQ)
                              for p in sp.fraction(sp.cancel(heat)))
    coordinate = sp.Poly(x, x, domain=sp.QQ)
    negative_values = []
    # (x d/dx)^m heat = numerator_m/denominator^(m+1).
    # Keeping polynomial numerators avoids exponential expression growth.
    for m in range(33):
        value = numerator.eval(1)/denominator.eval(1)**(m+1)
        expected = bbp_negative_mellin(m)
        assert value == sp.Rational(expected.numerator, expected.denominator)
        negative_values.append(str(value))
        numerator = coordinate*(denominator*numerator.diff()
                                 -(m+1)*denominator.diff()*numerator)

    return {"status": "PASS", "arithmetic": "SymPy exact QQ polynomials",
            "sympy_version": sp.__version__, "python_version": sys.version.split()[0],
            "inverse_all_implemented_orders": inverse_rows,
            "native_Euler_derivative_checks": len(negative_values),
            "native_negative_values_0_through_32": negative_values,
            "elapsed_seconds": round(time.monotonic()-started, 6),
            "proof_boundary": "finite implementation audit; universal claims require the paper proofs"}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
