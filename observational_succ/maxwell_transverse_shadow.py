"""Exact 1+1 transverse Maxwell sector: no-go and Lorentz repair.

Assume vacuum E_y(t,x), B_z(t,x) with d_t E=-d_x B and
 d_t B=-d_x E (units c=1). Every polynomial pair below is an exact
solution in left/right characteristic variables x-t and x+t.

The algebra proves covariance of this specified Maxwell subsystem,
not complete Maxwell theory with charges or nonlinear matter.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .galilean_lorentz_succ import (
    q,Mat2,ETA,ZERO,rational_boost,galilean,RelativityWitnessError
)

SWAP=Mat2(0,1,1,0)


def poly_eval(coefficients,z):
    z=q(z)
    value=F(0)
    for a in reversed(coefficients):
        value=value*z+a
    return value


def poly_derivative(coefficients):
    return tuple(F(i)*coefficients[i] for i in range(1,len(coefficients)))


@dataclass(frozen=True)
class TransverseMaxwellWave:
    """Source-validated E+B=f_+(x-t), E-B=f_-(x+t)."""
    right:tuple[F,...]
    left:tuple[F,...]

    def __post_init__(self):
        for name in ("right","left"):
            coefs=getattr(self,name)
            if (type(coefs) is not tuple or not coefs or len(coefs)>32):
                raise RelativityWitnessError("Finite polynomial wave source required")
            object.__setattr__(self,name,tuple(q(t) for t in coefs))

    def field(self,t,x):
        t,x=q(t),q(x)
        a=poly_eval(self.right,x-t)
        b=poly_eval(self.left,x+t)
        return (a+b)/2,(a-b)/2

    def residual(self,t,x):
        """Return (d_t E+d_x B,d_t B+d_x E) by independent formulas."""
        t,x=q(t),q(x)
        dplus=poly_eval(poly_derivative(self.right),x-t)
        dminus=poly_eval(poly_derivative(self.left),x+t)
        dte=(-dplus+dminus)/2
        dxb=(dplus-dminus)/2
        dtb=(-dplus-dminus)/2
        dxe=(dplus+dminus)/2
        return dte+dxb,dtb+dxe

    def lorentz_transform(self,parameter):
        """Transform BOTH coordinates and (E_y,B_z) tensor components.

        Lorentz inverse: x-t=a(x'-t'), x+t=b(x'+t') with
        a=gamma(1-v), b=gamma(1+v). The field components mix so
        E'+B'=a(E+B), E'-B'=b(E-B).
        """
        beta,gamma,_=rational_boost(parameter)
        a=gamma*(1-beta)
        b=gamma*(1+beta)
        return TransverseMaxwellWave(tuple(c*a**(k+1) for k,c in enumerate(self.right)),
                                     tuple(c*b**(k+1) for k,c in enumerate(self.left)))


def transformed_field_direct(wave,parameter,tprime,xprime):
    """Separate pullback+field-mixing oracle independent of polynomial adapter."""
    beta,gamma,T=rational_boost(parameter)
    t,x=T.inverse().apply((tprime,xprime))
    E,B=wave.field(t,x)
    return gamma*(E-beta*B),gamma*(B-beta*E)


def galilean_maxwell_flux(v):
    """After x'=x-vt, principal flux S-vI on (E,B)."""
    v=q(v)
    return Mat2(-v,1,1,-v)


def galilean_field_mix_obstruction(v):
    """Conjugation by any invertible pointwise field R preserves trace.

    Target flux S has trace zero. Galilean flux S-vI has trace -2v,
    so for v !=0 there is NO invertible 0th-order field mixing that
    restores both equations in standard Maxwell form. Spacetime repair
    (or a different physical field law) is required by this source.
    """
    v=q(v)
    flux=galilean_maxwell_flux(v)
    trace=flux.a+flux.d
    if trace!=-2*v:raise AssertionError("Exact principal-symbol defect")
    return {"velocity":v,"flux":flux,
            "source_characteristic_speeds":(-1-v,1-v),
            "target_characteristic_speeds":(-1,1),
            "trace_obstruction":trace,
            "any_pointwise_invertible_field_mix_repairs":v==0,
            "full_Maxwell_charge_matter_theorem":False}


def maxwell_subsystem_demo():
    wave=TransverseMaxwellWave((F(1),F(0),F(1)),
                                (F(0),F(-1),F(1),F(1)))
    beta,gamma,_=rational_boost(F(1,3))
    changed=wave.lorentz_transform(F(1,3))
    samples=((0,0),(1,2),(-2,1),(F(2,3),F(-5,7)))
    for y in samples:
        if changed.field(*y)!=transformed_field_direct(wave,F(1,3),*y):
            raise AssertionError("Lorentz field tensor square failed")
        if changed.residual(*y)!=(0,0):
            raise AssertionError("Maxwell source equation not preserved")
    no_go=galilean_field_mix_obstruction(beta)
    return {"velocity":beta,"gamma":gamma,"maxwell_sector_covariance":True,
            "source_chiral_polynomials":(tuple(map(str,wave.right)),tuple(map(str,wave.left))),
            "galilean_principal_trace":no_go['trace_obstruction'],
            "pointwise_field_redefinition_cannot_repair":True,
            "actual_physical_experiment_attested":False}
