"""Independent SymPy checks of low Legendre/Volterra and Schur algebra.

Not source-Weil sign verification. This file is an independent computation
used only to triangulate exact polynomial matrix identities.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import sympy as sp
from observational_succ.suzuki_moment_schur import (
    low_inverse_neumann, cell_legendre_overlap, projection_cell_gram,
    low_gram, finite_regularized_schur, parity_blocks,
)
from fractions import Fraction as F


def main():
    x=sp.symbols('x',real=True)
    a=sp.Rational(1,2)
    results={}
    for i,j in ((1,1),(1,3),(2,2),(29,31),(30,32)):
        vi=sp.integrate(sp.legendre(i,x/a),(x,-a,x))
        vj=sp.integrate(sp.legendre(j,x/a),(x,-a,x))
        val=sp.integrate(vi*vj,(x,-a,a))
        if i<=30 and j<=30:
            assert F(str(val))==low_inverse_neumann(F(1,2),30)[i-1][j-1]
        results[f'K_{i}_{j}']=str(val)
    # Independent operator block construction in a non-orthogonal cell+low frame.
    n=5;r=4
    M=cell_legendre_overlap(F(1,2),r,n)
    H=projection_cell_gram(F(1,2),r,n)
    W=low_gram(F(1,2),r)
    R=tuple(tuple(F(1,1+abs(i-j)) for j in range(n)) for i in range(n))
    lm=F(3)
    source=finite_regularized_schur(R,M,H,W,lm)
    Ms=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in row] for row in M])
    Hs=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in row] for row in H])
    Ws=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in row] for row in W])
    Rs=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in row] for row in R])
    # The expanded block formula is algebraically independent of compact fast form.
    asmat=Ms*Rs*Ms.T + lm*Ws
    inv=(lm*sp.eye(n)+Rs*Hs).inv()
    expanded=asmat - Ms*Rs*Hs*inv*Rs*Ms.T
    result=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in row] for row in source])
    assert expanded==result
    par=parity_blocks(source,r)
    results['Schur_parity_ranks']=[par['odd_rank'],par['even_rank']]
    results['finite_Schur_symmetry_verified']=result==result.T
    results['independent_analytic_legendre_verified']=True
    results['signed_Weil_source_or_RH_claim']=False
    print(json.dumps(results,indent=2,sort_keys=True))

if __name__=='__main__':main()
