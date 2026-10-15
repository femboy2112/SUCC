"""Hilbert-order streaming adapter for the ACTUAL signed Suzuki source.

The original G_a/J finite cell matrix is replayed from source_weil_hierarchy,
which reads only true prime powers, a single completed real Gamma,
the original pole/contact and half-density, with rigorous rational intervals.

Hilbert traversal permutes matrix ENTRY READ ORDER, not its Hilbert-space
operator basis or eigenvalues. No method claims the Hilbert plane curve
transports H0¹ derivative energies, builds a wild embedding, or proves RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from . import source_weil_hierarchy as true_weil
from .hilbert_carrier import HilbertCarrierError,point,order_gate

MAIN_SOURCE_SHA="03db44203147a7b28d445bb9f970fa71360e78c4"

class HilbertWeilError(ValueError):
    pass

@dataclass(frozen=True)
class HilbertWeilStream:
    source_id:str
    epoch:int
    basis:str
    a:Q
    J:int
    order:int
    side:int
    samples:tuple[tuple[int,int,Q],...]
    original_operator_error:Q
    spatial_error_without_positive_gamma_tail:Q
    positive_gamma_tail_bound:Q
    original_stage_center:tuple[tuple[Q,...],...]
    source_origin_head:str=MAIN_SOURCE_SHA
    spectrum_unchanged_by_entry_order:bool=True
    all_test_weil_positive_proved:bool=False

def source_stream(a,J,order,*,epoch=0,basis="ORIGINAL_SUZUKI_MEANZERO_CELL"):
    if type(a) not in (int,Q) or type(epoch) is not int or epoch<0:
        raise HilbertWeilError("exact source radius/epoch required")
    if basis!="ORIGINAL_SUZUKI_MEANZERO_CELL":
        raise HilbertWeilError("source basis cannot be silently reinterpreted")
    k=order_gate(order)
    if k>4:raise HilbertWeilError("actual Suzuki stage budget n<=16 cells")
    if type(J) is not int or not 1<=J<=36:
        raise HilbertWeilError("certified original Gamma rung cutoff required")
    radius=Q(a)
    st=true_weil.stage(radius,J,1<<k)
    if st.source!="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3" or st.nontrivial_zeros_used:
        raise HilbertWeilError("forged Weil arithmetic source")
    samples=tuple((i,j,st.center[i][j]) for i,j in
                  (point(k,d) for d in range(4**k)))
    if len(set((i,j) for i,j,_ in samples))!=(1<<k)**2:
        raise ArithmeticError("some original signed matrix entries were omitted")
    reconstructed=[[None for j in range(st.N)] for i in range(st.N)]
    for i,j,v in samples:
        reconstructed[i][j]=v
    if tuple(tuple(row) for row in reconstructed)!=st.center:
        raise ArithmeticError("Hilbert stream introduced or changed source matrix data")
    positive_tail=true_weil.authentic_positive_gamma_tail_norm(J)
    spatial=true_weil.honest_spatial_error(st)
    return HilbertWeilStream(
        source_id=st.source,epoch=epoch,basis=basis,
        a=radius,J=J,order=k,side=st.N,samples=samples,
        original_operator_error=st.norm_error,
        spatial_error_without_positive_gamma_tail=spatial,
        positive_gamma_tail_bound=positive_tail,
        original_stage_center=st.center)

def _replay(data):
    if type(data) is not HilbertWeilStream:
        raise HilbertWeilError("typed source stream required")
    if (type(data.a) is not Q or type(data.J) is not int or
        type(data.order) is not int or type(data.side) is not int or
        type(data.samples) is not tuple or
        type(data.original_stage_center) is not tuple or
        any(type(row) is not tuple or any(type(x) is not Q for x in row)
            for row in data.original_stage_center) or
        any(type(t) is not tuple or len(t)!=3 or
            type(t[0]) is not int or type(t[1]) is not int or
            type(t[2]) is not Q for t in data.samples) or
        type(data.original_operator_error) is not Q or
        type(data.spatial_error_without_positive_gamma_tail) is not Q or
        type(data.positive_gamma_tail_bound) is not Q):
        raise HilbertWeilError("source stream not exact rational data")
    clean=source_stream(data.a,data.J,data.order,
                        epoch=data.epoch,basis=data.basis)
    if data!=clean or data.source_origin_head!=MAIN_SOURCE_SHA:
        raise HilbertWeilError("modified or stale original Suzuki source stream")
    return clean

def local_stream_bounds(data):
    """A finite Hilbert step changes only one matrix-cell axis.

    Exact original source g_J is L-Lipschitz, so unrounded
    |h*g(diff)-h*g(nextdiff)|<= h² L_J(a).
    The rational center samples add at most 2h*eta for node interval
    uncertainty. This bound is proven, NOT a numerical empirical fit.
    """
    st=_replay(data)
    h=2*st.a/st.side
    L=true_weil.lipschitz_safe(st.a,st.J)
    eta=true_weil.stage(st.a,st.J,st.side).kernel_entry_radius
    limit=h*h*L+2*h*eta
    jumps=[abs(u[2]-v[2]) for u,v in zip(st.samples,st.samples[1:])]
    if any(x>limit for x in jumps):
        raise ArithmeticError("actual Weil source violates its Hilbert step bound")
    return {
        "source":st.source_id,
        "main_pinned":st.source_origin_head,
        "hilbert_max_center_jump":max(jumps),
        "source_analytic_lipschitz_bound":limit,
        "original_spatial_norm_error":st.spatial_error_without_positive_gamma_tail,
        "true_positive_gamma_tail_norm":st.positive_gamma_tail_bound,
        "same_original_signed_matrix_recovered":True,
        "no_new_positive_operator_constructed":True,
        "full_original_weil_sign_proved":False,
    }

def source_matrix_pair_witness(data,vector):
    """Exact quadratic form on matrix recovered INDEPENDENT of read order."""
    st=_replay(data)
    v=tuple(vector)
    if len(v)!=st.side or any(type(x) not in (int,Q) for x in v):
        raise HilbertWeilError("exact source state in original meanzero cells")
    if sum(v)!=0 or not any(v):
        raise HilbertWeilError("nonzero meanzero original observer test vector")
    val=true_weil.exact_rayleigh(st.original_stage_center,v)
    # Rebuild via Hilbert stream contraction; no index alias is permitted.
    energy=sum((Q(v[i])*c*Q(v[j]) for i,j,c in st.samples),Q())
    norm=sum((Q(x)**2 for x in v),Q())
    if energy/norm!=val:
        raise ArithmeticError("Hilbert entry ordering changed signed original form")
    return {
       "source_id":st.source_id,"signed_original_quadratic_rayleigh":val,
       "hilbert_stream_rayleigh":energy/norm,
       "preserves_full_signed_source_matrix":True,
       "positive_weil_certified":False
    }

def source_interface_metadata():
    return {
        "original_source":"G_a Suzuki genuine prime-power Gamma pole contact half-density",
        "Hilbert_ordering_role":"READ-ONLY PERMUTATION OF 2D MATRIX ENTRIES",
        "cell_Hilbert_2d_to_1d_a.e_measure_isometry":"CLASSICAL_ON_AREA_L2_ONLY",
        "Sobolev_H01_transport":"NOT_IDENTIFIED_OR_PRESERVED",
        "negative_spectral_depth_improvement":"NONE_FROM_REORDERING_ALONE",
        "zero_shift_30_moment_Schur_gate":"UNVERIFIED",
        "rh_proved":False,
    }
