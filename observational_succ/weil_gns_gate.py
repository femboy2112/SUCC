"""Finite exact Weil-to-GNS positivity gate: never a proof of true RH.

For a source-Hermitian form B(f,g)=W(f*tilde(g)), genuine Hilbert/GNS-type
quotient completion exists iff B is positive semidefinite. This theorem is
an implication in functional analysis, not proved by finite samples of B.
Here finite Fraction Hermitian matrices are DECLaRED toy source controls
for positive, signed and unobserved-negative-subspace cases.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


class GNSGateError(ValueError):
    """Unknown source, non-Hermitian form or unsupported positivity assertion."""


def _det(mat: tuple[tuple[F,...],...]) -> F:
    n=len(mat)
    if n==0:return F(1)
    a=[list(row) for row in mat]
    sign=1
    result=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]),None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j],a[pivot]=a[pivot],a[j]
            sign=-sign
        v=a[j][j]
        result*=v
        for k in range(j+1,n):
            f=a[k][j]/v
            if f:
                for i in range(j+1,n):
                    a[k][i]-=f*a[j][i]
            a[k][j]=F(0)
    return sign*result


@dataclass(frozen=True)
class FiniteSignedForm:
    """A declared finite symmetric rational quadratic form, not full Weil."""
    basis: tuple[str,...]
    gram: tuple[tuple[F,...],...]
    source_id: str

    def __post_init__(self):
        n=len(self.basis)
        if (not n or n>7 or any(type(t) is not str or not t for t in self.basis) or
            len(set(self.basis)) != n or
            type(self.source_id) is not str or not self.source_id.strip()):
            raise GNSGateError("Finite named basis and source ID required")
        if type(self.gram) is not tuple or len(self.gram)!=n or any(type(r) is not tuple or len(r)!=n for r in self.gram):
            raise GNSGateError("Gram dimensions must match basis")
        try:
            q=tuple(tuple(F(x) if type(x) in (int,F) else None for x in r) for r in self.gram)
        except (ValueError, TypeError, ZeroDivisionError) as err:
            raise GNSGateError("Only exact rational form coefficients") from err
        if any(x is None for r in q for x in r):
            raise GNSGateError("Only exact rational form coefficients")
        if any(q[i][j]!=q[j][i] for i in range(n) for j in range(n)):
            raise GNSGateError("Signed form must be symmetric/Hermitian")
        object.__setattr__(self,"gram",q)

    def quadratic(self, vector: tuple[int|F,...]) -> F:
        n=len(self.basis)
        if type(vector) is not tuple or len(vector)!=n or any(type(x) not in (int,F) for x in vector):
            raise GNSGateError("One exact vector in the declared basis")
        v=tuple(F(x) for x in vector)
        return sum((v[i]*self.gram[i][j]*v[j] for i in range(n) for j in range(n)),F(0))

    def receipt(self) -> dict:
        n=len(self.basis)
        checked=[]
        first_negative=None
        for size in range(1,n+1):
            for inds in combinations(range(n),size):
                minor=_det(tuple(tuple(self.gram[i][j] for j in inds) for i in inds))
                checked.append((inds,minor))
                if minor<0 and first_negative is None:
                    first_negative=(inds,minor)
        psd=first_negative is None
        # Exact Sylvester criterion for SEMIDEFINITE real symmetric forms:
        # every principal minor (not just leading ones) is >=0.
        return {
            "source": self.source_id,
            "tested_declared_basis": self.basis,
            "all_principal_minors": tuple(checked),
            "exact_finite_PSD": psd,
            "first_negative_minor": first_negative,
            "GNS_positive_quotient_available_for_THIS_DECLARED_FORM": psd,
            "zero_norm_quotient_universally_valid_only_if_PSD": True,
            "claimed_complete_Weil_distribution_identified": False,
            "all_test_positive_for_original_zeta": False,
            "RH_proved": False,
        }


def calibration_pair() -> dict:
    """Exact positive auxiliary covariance vs signed negative target.

    Both live on the *same* finite test basis. A positive arbitrary
    auxiliary matrix is NOT an identification with original signed W.
    """
    basis=("source-test-1","source-test-2")
    positive=FiniteSignedForm(basis,((1,0),(0,1)),"AUXILIARY_POSITIVE").receipt()
    signed=FiniteSignedForm(basis,((1,0),(0,-1)),"MUTANT_SIGNED_TARGET").receipt()
    if not positive["exact_finite_PSD"] or signed["exact_finite_PSD"]:
        raise AssertionError("GNS calibration must separate auxiliary from signed")
    return {
        "auxiliary_positive": positive,
        "signed_countermodel": signed,
        "positivity_of_auxiliary_implies_original_Weil": False,
        "source_to_complete_signed_form_identification_proved": False,
        "RH_proved": False,
    }
