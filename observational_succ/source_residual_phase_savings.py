"""Source-conditional first-prime center/edge high-resolvent savings.

The actual original source-shape theorem from SOURCE-EDGE PR #161 yields:
D>=kappa I + w(I-A_log2) on the primitive high moment-null carrier,
with w>=12/25, if the inherited high Bessel source contract holds.
This SOURCE-EDGE inference is a sibling-draft imported PAPER PREMISE,
not independently checked by the pinned source module on this branch.

We use the WHOLE CONTINUUM already source-pinned residual approximant
and its exact L2 error to certify center/edge test functional bounds.
An indefinite robust feature Gram is NOT clamped to PSD; both old/new
complete Schur lower matrices are valid under the SOURCE-EDGE premise.
A negative Schur lower is AMBIGUOUS, never a negative Weil witness.
"""
from fractions import Fraction as F
from . import original_continuum_residual as R
from . import clamped_k_residual_bridge as B


class PhaseSavingError(ValueError):
    pass


def projected_action_pieces(pieces):
    """Subtract genuine primitive P0..P3 moments on EVERY actual source cell."""
    m=R.projected_piece_moments(pieces)
    proj=(F(0),)
    for k in range(4):
        proj=B.add(proj,B.scale(B.legendre(k),F(2*k+1)*m[k]))
    result=tuple((l,r,B.add(p,B.scale(proj,-1))) for l,r,p in pieces)
    return result


def positive_source_regions(parameters):
    """C0 and R0 are strict interiors for ALL genuine log2 intervals."""
    b=parameters["b"];db=parameters["db"]
    lo,hi=b-db,b+db
    if not (F(5,8)<lo<=hi<F(3,4)):
        raise PhaseSavingError("wrong original source prime2 interval")
    center=(-F(1,8),F(1,8))
    edge=(F(1,4),F(3,8))
    if not (center[0]>R.A-hi and center[1]<lo-R.A
            and edge[0]>hi-R.A and edge[1]<R.A
            and edge[0]-hi>-R.A and edge[1]-lo<R.A-hi):
        raise PhaseSavingError("fixed original center/edge probe violates source support")
    return center,edge


def orthogonal_center_edge_features(which):
    if which not in ("odd_derivative","even_derivative"):
        raise PhaseSavingError("original derivative parity only")
    # PR161 parity is derivative parity; source primitive has opposite parity.
    center=(F(1),) if which=="odd_derivative" else (F(0),F(1))
    edge0=(F(1),)
    edge1=(-F(5,16),F(1))
    center_n=F(1,4) if which=="odd_derivative" else F(1,768)
    return {"center":(center,center_n),
            "edge":((edge0,F(1,8)),(edge1,F(1,6144)))}


def robust_feature_lower(moments,errors,feature_norm_sq,theta=F(1,2)):
    """All-real-directions 2x2 TRUE feature-energy Loewner LOWER.

    |m.e+error|² >= (1-theta)|m.e|²
                    -(1/theta-1)sum(error_i²)||e||².
    Even if the resulting symmetric matrix is indefinite it is a VALID
    conservative source lower; NEVER project to its positive part.
    """
    theta,feature_norm_sq=R.rat(theta),R.rat(feature_norm_sq)
    if not 0<theta<1 or feature_norm_sq<=0 or len(moments)!=2 or len(errors)!=2:
        raise PhaseSavingError("2D original source feature and Young parameter")
    m=tuple(R.rat(x) for x in moments)
    e=tuple(R.rat(x) for x in errors)
    if any(x<0 for x in e):raise PhaseSavingError("feature errors are nonnegative")
    a=(1-theta)/feature_norm_sq
    penalty=(1/theta-1)*(e[0]**2+e[1]**2)/feature_norm_sq
    return ((a*m[0]*m[0]-penalty,a*m[0]*m[1]),
            (a*m[1]*m[0],a*m[1]*m[1]-penalty))


def _mat_add(a,b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def _mat_scale(a,c):
    return tuple(tuple(c*a[i][j] for j in range(2)) for i in range(2))


def _exact_2d_gershgorin_floor(a):
    if a[0][1]!=a[1][0]:
        raise PhaseSavingError("source signed 2x2 lower asymmetric")
    return min(a[0][0]-abs(a[0][1]),a[1][1]-abs(a[1][0]))


def _is_psd(a):
    return (a[0][0]>=0 and a[1][1]>=0 and
            a[0][0]*a[1][1]>=a[0][1]*a[1][0])


def source_conditional_phase_saving(J=16,M=128,P=18,
                                    young=F(1,4),theta=F(1,2)):
    """Conditional SOURCE-EDGE authenticated residual saving, same source SHA.

    Actual source residual from original_continuum_residual; new comparator
    additionally assumes PR161's original true all-high arithmetic surplus.
    We DO NOT call this an unconditional original S4 improvement.
    """
    params=R.source_parameters()
    baseline=R.source_residual_schur_trial(J=J,M=M,P=P,eta=young)
    if baseline["frozen_source_git_blob"]!=R.SOURCE_SHA:
        raise PhaseSavingError("source boundary provenance mismatch")
    center_span,edge_span=positive_source_regions(params)
    w=F(12,25)
    if not params["w"]-params["dw"]>=w:
        raise PhaseSavingError("original prime2 weight not above 12/25")
    original={}
    for i in (1,2,3,4):
        t=F(baseline["four_original_parity_Schur_blocks"][
               "odd_derivative" if i%2 else "even_derivative"][
               "fitted_high_coefficients"][(i-1)//2])
        h=R.high_boundary_match(i,t)["h"]
        packet=R.exact_piecewise_primitive_action(h,J,M,P,params)
        z=projected_action_pieces(packet["pieces"])
        delta=packet["finite_source_action_error_upper"]+R.authentic_Gamma_tail_action_dual(h,J)["selected"]
        left=z[0][2];right=z[2][2]
        widtherr=params["db"]*B.sqrt_up(
             R.definite(B.mul(B.derivative(left),B.derivative(left)),
                         z[0][0],z[0][1]))
        edgeerror=2*delta+widtherr
        mismatch=B.add(right,B.scale(R.shifted(left,-params["b"]),-1))
        original[i]={"z":z,"delta":delta,"edge_error":edgeerror,"mismatch":mismatch,
              "clamped_parameter":t}
    sectors={}
    for name,indices,kappa in (("odd_derivative",(1,3),F(63,500)),
                                ("even_derivative",(2,4),F(153,500))):
        features=orthogonal_center_edge_features(name)
        fcenter,ncenter=features["center"]
        centerm=[R.definite(B.mul(original[i]["z"][1][2],fcenter),*center_span)
                 for i in indices]
        centere=[B.sqrt_up(ncenter)*original[i]["delta"] for i in indices]
        centerlo=robust_feature_lower(centerm,centere,ncenter,theta)
        # Two ORTHOGONAL tests of the true prime-connected edge mismatch,
        # restricted to R0 contained in original R(b) for all b intervals.
        edge_feature_data=[]
        edgelo=((F(0),F(0)),(F(0),F(0)))
        for fedge,nedge in features["edge"]:
            moments=[R.definite(B.mul(original[i]["mismatch"],fedge),*edge_span)
                     for i in indices]
            errs=[B.sqrt_up(nedge)*original[i]["edge_error"] for i in indices]
            low=robust_feature_lower(moments,errs,nedge,theta)
            edgelo=_mat_add(edgelo,low)
            edge_feature_data.append({
                "source_nominal_moments":tuple(str(x) for x in moments),
                "source_moment_error_upper":tuple(str(x) for x in errs),
                "norm_sq":str(nedge)})
        centercoef=w/(kappa*(kappa+w))
        edgecoef=w/(kappa*(kappa+2*w))
        gain=_mat_add(_mat_scale(centerlo,centercoef),
                      _mat_scale(edgelo,edgecoef))
        old=tuple(tuple(F(v) for v in row) for row in
            baseline["four_original_parity_Schur_blocks"][name][
                "genuine_source_2x2_Schur_Loewner_lower"])
        upgraded=_mat_add(old,gain)
        # Both full matrices are separately valid source conditional lowers.
        # Choose the larger EXACT Gershgorin floor; do not PSD-clamp gain.
        old_floor=_exact_2d_gershgorin_floor(old)
        new_floor=_exact_2d_gershgorin_floor(upgraded)
        pick_new=new_floor>old_floor
        chosen=upgraded if pick_new else old
        sectors[name]={
           "source_high_surplus_comparator_is_SIBLING_PR161_CONDITIONAL":True,
           "low_indices":indices,"source_kappa":str(kappa),
           "inherited_prime2_surplus_weight_floor":str(w),
           "center_resolvent_saving_coefficient":str(centercoef),
           "edge_resolvent_saving_coefficient":str(edgecoef),
           "central_feature_nominal":tuple(str(x) for x in centerm),
           "central_feature_error_upper":tuple(str(x) for x in centere),
           "center_robust_signed_Loewner_lower":
                tuple(tuple(str(x) for x in row) for row in centerlo),
           "edge_test_rows":tuple(edge_feature_data),
           "edge_robust_signed_Loewner_lower":
                tuple(tuple(str(x) for x in row) for row in edgelo),
           "signed_source_phase_gain_Loewner_lower":
                tuple(tuple(str(x) for x in row) for row in gain),
           "old_original_Schur_lower":
                tuple(tuple(str(x) for x in row) for row in old),
           "new_conditional_source_Schur_lower":
                tuple(tuple(str(x) for x in row) for row in upgraded),
           "chosen_source_Schur_lower":
                tuple(tuple(str(x) for x in row) for row in chosen),
           "chosen_phase_probe":bool(pick_new),
           "old_rational_Gershgorin_floor":str(old_floor),
           "conditional_phase_Gershgorin_floor":str(new_floor),
           "chosen_Schur_lower_PSD_certified":_is_psd(chosen)}
    return {"original_source_SHA":params["sha"],
        "source_log2_b":str(params["b"]),
        "genuine_prime_half_density_preserved":True,
        "has_sibling_PR161_arithmetic_high_surplus_PAPER_PREMISE":True,
        "source_original_S4_unconditional_sign_proved":False,
        "parity_comparisons":sectors,
        "conditional_first_window_S4_PSD":all(p["chosen_Schur_lower_PSD_certified"]
                                                for p in sectors.values()),
        "RH_proved":False}
