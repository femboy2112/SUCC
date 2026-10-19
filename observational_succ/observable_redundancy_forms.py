"""Exact finite criterion for introduced information to be genuinely redundant.

A source quotient q:V->B, with ker(q)=K, may forget a new auxiliary
carrier ONLY when the actual observables and causal dynamics factor
through q. A contractible chain summand is NOT automatically in the
radical of a signed bilinear form. Nor does positive energy on the new
states imply positive Weil form after elimination.

This implements source forms and dynamics with exact Fraction matrices.
The block Schur correction is calculated, not silently declared
positive. Connes/Weil equality remains an independent analytic gate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


class ObservableRedundancyError(ValueError):
    """A matrix/source or quotient claim violates its contract."""


def _mat(rows):
    if type(rows) is not tuple or not rows or any(type(r) is not tuple for r in rows):
        raise ObservableRedundancyError("nonempty exact tuple matrix required")
    width=len(rows[0])
    if width==0 or any(len(row)!=width for row in rows):
        raise ObservableRedundancyError("rectangular source matrix required")
    if any(type(x) not in (int,F) for row in rows for x in row):
        raise ObservableRedundancyError("integer or Fraction entries only")
    return tuple(tuple(F(x) for x in row) for row in rows)


def _transpose(a):
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def _mm(a,b):
    if len(a[0])!=len(b):
        raise ObservableRedundancyError("matrix composition mismatch")
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def _inverse(a):
    """Independent Gauss-Jordan inverse of nondegenerate hidden block."""
    n=len(a)
    if not n or len(a[0])!=n:
        raise ObservableRedundancyError("square invertible hidden block required")
    x=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if x[i][j]),None)
        if pivot is None:
            raise ObservableRedundancyError("singular hidden quadratic block")
        x[j],x[pivot]=x[pivot],x[j]
        v=x[j][j]
        x[j]=[u/v for u in x[j]]
        for i in range(n):
            if i!=j and x[i][j]:
                z=x[i][j]
                x[i]=[q-z*r for q,r in zip(x[i],x[j])]
    result=tuple(tuple(row[n:]) for row in x)
    if _mm(a,result)!=tuple(tuple(F(int(i==j)) for j in range(n)) for i in range(n)):
        raise AssertionError("exact elimination did not produce an inverse")
    return result


def _det(a):
    n=len(a)
    if n==0:return F(1)
    x=[list(row) for row in a]
    sign=1
    result=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if x[i][j]),None)
        if pivot is None:return F(0)
        if pivot!=j:
            sign=-sign
            x[j],x[pivot]=x[pivot],x[j]
        val=x[j][j]
        result*=val
        for i in range(j+1,n):
            factor=x[i][j]/val
            for k in range(j+1,n):
                x[i][k]-=factor*x[j][k]
            x[i][j]=0
    return F(sign)*result


def _psd(a):
    """Sylvester all-principal-minor criterion for symmetric PSD."""
    n=len(a)
    if any(len(row)!=n for row in a) or _transpose(a)!=a:
        raise ObservableRedundancyError("symmetric square exact form required")
    for size in range(1,n+1):
        for ids in combinations(range(n),size):
            small=tuple(tuple(a[i][j] for j in ids) for i in ids)
            if _det(small)<0:return False
    return True


def _pd(a):
    """Sylvester LEADING-minor criterion for symmetric positive definite."""
    n=len(a)
    return (n>0 and len(a[0])==n and _transpose(a)==a and
            all(_det(tuple(tuple(a[i][j] for j in range(k))
                           for i in range(k)))>0 for k in range(1,n+1)))


@dataclass(frozen=True)
class ExactSourceExtension:
    """V=B ⊕ K; the projection q retains exactly the first visible_dim states.

    This declares which source readouts count as unchanged. Adding a
    contractible hidden K is useful, but source redundancy is *relative*
    to q and a specified family of forms/dynamics.
    """
    visible_dim:int
    signed_form:tuple[tuple[F,...],...]
    source_id:str="Z-original-signed-analytic-model"
    epoch:int=0

    def __post_init__(self):
        if type(self.visible_dim) is not int or self.visible_dim<=0:
            raise ObservableRedundancyError("positive visible dimension required")
        a=_mat(self.signed_form)
        if len(a)>8 or len(a)<=self.visible_dim or len(a[0])!=len(a) or a!=_transpose(a):
            raise ObservableRedundancyError("symmetric enlarged source form with hidden states")
        if type(self.source_id) is not str or not self.source_id.strip():
            raise ObservableRedundancyError("declared original source required")
        if type(self.epoch) is not int or self.epoch<0:
            raise ObservableRedundancyError("nonnegative exact source epoch required")
        object.__setattr__(self,"signed_form",a)

    @property
    def total_dim(self):
        return len(self.signed_form)

    @property
    def hidden_dim(self):
        return self.total_dim-self.visible_dim

    @property
    def A(self):
        return tuple(tuple(row[:self.visible_dim]) for row in self.signed_form[:self.visible_dim])

    @property
    def B(self):
        return tuple(tuple(row[self.visible_dim:]) for row in self.signed_form[:self.visible_dim])

    @property
    def C(self):
        return tuple(tuple(row[self.visible_dim:]) for row in self.signed_form[self.visible_dim:])

    def form_descends(self):
        """Necessary and sufficient: every hidden vector lies in form radical.

        Source F(v,w) = Fbar(qv,qw) for all v,w iff every row and
        column indexed by K vanishes. Contractibility alone gives no
        such vanishing.
        """
        radical=all(self.signed_form[i][j]==0
                    for i in range(self.total_dim)
                    for j in range(self.total_dim)
                    if i>=self.visible_dim or j>=self.visible_dim)
        return {
            "source_id":self.source_id, "epoch":self.epoch,
            "visible_dim":self.visible_dim, "hidden_dim":self.hidden_dim,
            "full_source_form_factors_through_quotient":radical,
            "unique_descended_form":self.A if radical else None,
            "hidden_acyclicity_would_imply_this":False,
            "all_observable_signs_preserved_when_true":radical,
            "completed_Weil_form_identified":False,
        }

    def dynamics_descend(self, matrix):
        """qT=Tbar q iff T(hidden) stays hidden; top-right block zero."""
        t=_mat(matrix)
        if len(t)!=self.total_dim or len(t[0])!=self.total_dim:
            raise ObservableRedundancyError("source dynamics dimension mismatch")
        good=all(t[i][j]==0 for i in range(self.visible_dim)
                 for j in range(self.visible_dim,self.total_dim))
        return {
            "source_id":self.source_id,"epoch":self.epoch,
            "full_source_dynamics_descends":good,
            "descended_visible_operator":
                tuple(tuple(t[i][j] for j in range(self.visible_dim))
                      for i in range(self.visible_dim)) if good else None,
            "future_probe_can_expose_hidden_if_false":not good,
        }

    def schur_shorting(self):
        """Minimize over true POSITIVE definite hidden C, yielding
        W_eff=A - B C^-1 B^T. The correction is source-sensitive.
        A and C individually positive DO NOT imply W_eff positive.
        """
        A,B,C=self.A,self.B,self.C
        if not _pd(C):
            raise ObservableRedundancyError("positive-definite hidden energy needed for minimum")
        inv=_inverse(C)
        penalty=_mm(_mm(B,inv),_transpose(B))
        eff=tuple(tuple(A[i][j]-penalty[i][j] for j in range(self.visible_dim))
                  for i in range(self.visible_dim))
        if not _psd(penalty):
            raise AssertionError("hidden positive energy produced negative correction")
        return {
            "visible_original_block":A,
            "positive_hidden_block":C,
            "hidden_coupling_correction":penalty,
            "effective_source_form":eff,
            "effective_form_PSD":_psd(eff),
            "full_enlarged_form_PSD":_psd(self.signed_form),
            "hidden_C_positive_definite":True,
            "sign_of_effective_form_forced_by_C_alone":False,
            "source_to_actual_Weil_distribution_proved":False,
        }


def redundancy_controls():
    """Hostile and positive examples for exact quotient vs positivity."""
    null=ExactSourceExtension(1,((F(-1),0,0),(0,0,0),(0,0,0)))
    neg=ExactSourceExtension(1,((1,2),(2,1)))
    good=ExactSourceExtension(1,((5,2),(2,1)))
    nontrivial=[
        ((1,0),(0,1)), # decoupled but hidden positive, NOT null
        ((1,1),(0,1)), # hidden affects visible after one step
    ]
    return {
        "source_signed_null_extension_can_descend_even_if_negative":
            null.form_descends()["full_source_form_factors_through_quotient"],
        "negative_source_recovered_after_null_extension":
            null.form_descends()["unique_descended_form"][0][0]==-1,
        "positive_hidden_C_indefinite_full_example":neg.schur_shorting(),
        "positive_full_source_example":good.schur_shorting(),
        "hidden_probe_exposure":tuple(
            neg.dynamics_descend(m)["full_source_dynamics_descends"]
            for m in nontrivial),
        "auxiliary_positivity_implies_completed_Weil":False,
    }
