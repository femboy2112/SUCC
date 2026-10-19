"""A source-relative finite-rank upper for the authentic high inverse.

D>=kappa I is inherited ONLY in the primitive K-Hilbert completion.
All source actions are full-continuum polynomial approximants with paid
finite and infinite-Gamma errors. Finite high PSD never supplies the global
gap. The result is source-conditional, not an RH positivity certificate.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

from . import clamped_k_residual_bridge as B
from . import original_continuum_residual as R
from . import gamma_tail_resolvent_refinement as G
from . import multimode_original_residual as U

PR178='e42096ec0186228dd0f748767599e470f2ca2e1d'
PR177='f309d9104ba480c1999c962af1df7c50f19e1bfe'
PR178_DATA='research/2026-10-18/INSTITUTE_GAMMA_ETA_SOURCE.json'
PR178_DATA_SHA256='0a24144e8a22178296ad314e846ea13ab41a67efc291a42b6764f73d61e0d7aa'
SOURCE_BLOB=R.SOURCE_SHA

class DirectionalSourceError(ValueError):
    pass


def exact(x):
    if type(x) not in (int,F):raise DirectionalSourceError('exact rational input required')
    return F(x)


def matrix(a):
    if not a or any(len(row)!=len(a[0]) for row in a):
        raise DirectionalSourceError('nonempty rectangular matrix')
    return tuple(tuple(exact(x) for x in row) for row in a)


def transpose(a):return tuple(zip(*a))


def multiply(a,b):
    if len(a[0])!=len(b):raise DirectionalSourceError('matrix dimensions')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F())
                       for j in range(len(b[0]))) for i in range(len(a)))


def quadratic(a,c):
    return sum((c[i]*a[i][j]*c[j] for i in range(len(c)) for j in range(len(c))),F())


def psd2(a):
    return a[0][0]>=0 and a[1][1]>=0 and a[0][0]*a[1][1]>=a[0][1]*a[1][0]


def inverse2(a):
    a=matrix(a)
    if len(a)!=2 or len(a[0])!=2 or a[0][1]!=a[1][0]:
        raise DirectionalSourceError('symmetric two by two inverse required')
    det=a[0][0]*a[1][1]-a[0][1]**2
    if a[0][0]<=0 or det<=0:raise DirectionalSourceError('positive definite source matrix required')
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))


def interval_matrix_bound(mid,rad,upper):
    return tuple(tuple(mid[i][j]+((1 if upper else -1)*sum(rad[i]) if i==j else 0)
                       for j in range(len(mid))) for i in range(len(mid)))


def inverse_correction_lower(K_upper,V_mid,V_radius,kappa):
    """All-direction interval proof of V* K^-1 V / kappa.

    K<=K_upper, K>0, |V-V_mid|<=V_radius entrywise are hypotheses.
    An arbitrary rational trial X=K_upper^-1 V_mid gives a source-safe
    lower V*X+X*V-X*K_upper*X. Pay entrywise uncertainty by row sums.
    Return the whole signed lower; never positive-part-clamp it.
    """
    K_upper,V_mid,V_radius=map(matrix,(K_upper,V_mid,V_radius))
    kappa=exact(kappa)
    if kappa<=0 or len(V_mid)!=2 or len(V_mid[0])!=2 or any(v<0 for row in V_radius for v in row):
        raise DirectionalSourceError('positive kappa and two genuine residual directions')
    inv=inverse2(K_upper)
    X=multiply(inv,V_mid)
    center=multiply(transpose(V_mid),X)
    radius=tuple(tuple(sum((abs(X[k][i])*V_radius[k][j]
                            +V_radius[k][i]*abs(X[k][j]) for k in range(2)),F())
                       for j in range(2)) for i in range(2))
    lower=interval_matrix_bound(center,radius,False)
    return {'correction_lower':tuple(tuple(x/kappa for x in row) for row in lower),
            'variational_X':X,'correction_midpoint':center,
            'correction_entry_radii':radius,'whole_correction_PSD':psd2(lower)}


def sharp_parent_tail(h,J):
    """Selected PR178 IN-GAMMA-02 coefficients, reimplemented from theorem.

    Provenance: PR178 scripts/institute_schur_probe.py::gamma_coefficients,
    blob 1a09b58c0c5bdc4a86a756cad640f9f27511c73c. No history imported.
    """
    if type(J) is not int or J<1:raise DirectionalSourceError('positive Gamma cutoff')
    d=4*J+1
    sigma=F(13,16*(d-2))
    tau=min(B.gamma_action_tail(J),F(2,(d-2)**2))
    if any(B.value(p,e) for p in (h,B.derivative(h)) for e in (-R.A,R.A)):
        raise DirectionalSourceError('actual source H2 zero-extension required')
    return min(sigma*B.sqrt_up(R.derivative_norm_squared(h)),
               tau*B.sqrt_up(R.norm_squared(B.derivative(B.derivative(h)))))


def _pieces_add_poly(pieces,p):
    return tuple((a,b,B.add(f,p)) for a,b,f in pieces)


def _projection_pieces(pieces):
    moments=R.projected_piece_moments(pieces)
    low=(F(0),)
    for k,m in enumerate(moments):low=B.add(low,B.scale(B.legendre(k),-(2*k+1)*m))
    return _pieces_add_poly(pieces,low)


def _action(h,J,M,params,retained=False):
    finite=R.exact_piecewise_primitive_action(h,J,M,18,params)
    error=finite['finite_source_action_error_upper']+sharp_parent_tail(h,J)
    pieces=finite['pieces']
    route='PR178_FINITE_PLUS_MIDPOINT_TAIL'
    if retained:
        tail=G.gamma_tail_resolvent_bound(h,J)
        e2=finite['finite_source_action_error_upper']+tail['corrected_action_error_upper']
        if e2<error:
            pieces=_pieces_add_poly(pieces,tail['retained_tail_action'])
            error=e2;route='PR179_RETAINED_TAIL'
    return {'pieces':_projection_pieces(pieces),'error':error,'route':route}


def _gram(p,q):return R._integrate_piece_pair(p,q)


def _norm(p):return B.sqrt_up(_gram(p,p))


def _fixed_parent_decomposition(data):
    energy=tuple(tuple(tuple(F(v) for v in z) for z in row)
                 for row in data['genuine_signed_qJ_intervals'])
    rad=tuple(tuple((z[1]-z[0])/2 for z in row) for row in energy)
    tail=tuple(tuple(F(v) for v in row) for row in data['genuine_infinite_Gamma_tail_lower_Gram'])
    if not data['source_tail_matrix_is_PSD']:tail=((F(),F()),(F(),F()))
    mid=tuple(tuple(sum(energy[i][j])/2+tail[i][j] for j in range(2)) for i in range(2))
    T=interval_matrix_bound(mid,rad,False)
    M=tuple(tuple(F(v) for v in row) for row in data['surrogate_QE_action_residual_gram_exact'])
    return T,M


def pr178_fixed_obstruction(root=None):
    """Read-only selected-data extraction from exact sibling commit, no merge."""
    root=Path(root) if root else Path(__file__).resolve().parents[1]
    raw=subprocess.run(['git','show',PR178+':'+PR178_DATA],cwd=root,
                       check=True,stdout=subprocess.PIPE).stdout
    if sha256(raw).hexdigest()!=PR178_DATA_SHA256:
        raise DirectionalSourceError('PR178 fixed-data digest mismatch')
    data=json.loads(raw)
    if data['frozen_source_git_blob']!=SOURCE_BLOB or data['source_J']!=24:
        raise DirectionalSourceError('wrong original source receipt')
    results={}
    for name,v in data['four_original_parity_Schur_blocks'].items():
        T,M=_fixed_parent_decomposition(v)
        kappa=F(v['source_kappa']);gap=T[0][0]-M[0][0]/kappa
        if gap>=0:raise ArithmeticError('pinned fixed-data obstruction failed')
        # Directed rounding permits small, independently verifiable receipts.
        grid=10**18
        lo=F(gap.numerator*grid//gap.denominator,grid)
        results[name]={'direction':(1,0),'gap_interval':(lo,lo+F(1,grid)),
            'strict_obstruction':lo+F(1,grid)<0,
            'fitted_coefficients':tuple(F(x) for x in v['fitted_high_coefficients'])}
    return {'source_commit':PR178,'source_path':PR178_DATA,
            'source_sha256':PR178_DATA_SHA256,'source_blob':SOURCE_BLOB,'blocks':results,
            'scope':'ALL_POSITIVE_YOUNG_AND_PSD_PENALTIES_ON_FIXED_RETAINED_DATA',
            'genuine_source_negative':False}


def directional_original_trial(J=24,M=192,levels=(1,2),sealed_parent=True):
    """Two auxiliary high columns per parity; no scalar tuning.

    The selected auxiliary derivative columns are P_(m+2l)-P_(m+2l+2).
    They are disjoint from the single parent clamped correction l=0.
    Only one finite source evaluation is used per J; all paid continuum
    pairings and complete Gamma error estimates enter the inverse upper.
    """
    if type(J) is not int or not 1<=J<=24 or type(M) is not int or not 16<=M<=192:
        raise DirectionalSourceError('bounded original source depth')
    if tuple(levels) not in ((1,2),(2,3)):
        raise DirectionalSourceError('declared independent high packet family')
    params=R.source_parameters()
    if sealed_parent:
        if (J,M)!=(24,192):raise DirectionalSourceError('sealed parent fixed to J24 M192')
        raw=subprocess.run(['git','show',PR178+':'+PR178_DATA],cwd=Path(__file__).resolve().parents[1],
                           check=True,stdout=subprocess.PIPE).stdout
        if sha256(raw).hexdigest()!=PR178_DATA_SHA256:raise DirectionalSourceError('sealed parent digest')
        parent=json.loads(raw)
    else:
        parent=R.source_residual_schur_trial(J,M,18,fit=True)
    blocks={}
    for name,data in parent['four_original_parity_Schur_blocks'].items():
        indices=tuple(data['indices']);kappa=F(data['source_kappa'])
        T,parent_M=_fixed_parent_decomposition(data)
        hs=[R.high_boundary_match(i,F(t))['h'] for i,t in zip(indices,data['fitted_high_coefficients'])]
        residuals=[_action(h,J,M,params) for h in hs]
        rnorm=[_norm(v['pieces']) for v in residuals]
        rerror=[v['error'] for v in residuals]
        actual_M=tuple(tuple(_gram(a['pieces'],b['pieces']) for b in residuals) for a in residuals)
        if actual_M!=parent_M:raise ArithmeticError('whole-continuum residual differs from sealed parent')
        errorsq=sum((x*x for x in rerror),F())
        baseline=tuple(tuple(T[i][j]-(F(5,4)*actual_M[i][j]+(5*errorsq if i==j else 0))/kappa
                             for j in range(2)) for i in range(2))
        ws=[U.correction_primitive(indices[0],level) for level in levels]
        wa=[_action(w['primitive'],J,M,params,True) for w in ws]
        zp=[_pieces_add_poly(a['pieces'],B.scale(w['primitive'],-kappa)) for w,a in zip(ws,wa)]
        znorm=[_norm(p) for p in zp];zerror=[a['error'] for a in wa]
        zmid=tuple(tuple(_gram(a,b) for b in zp) for a in zp)
        zrad=tuple(tuple(zerror[i]*znorm[j]+zerror[j]*znorm[i]+zerror[i]*zerror[j]
                        for j in range(2)) for i in range(2))
        cache={}
        qinterval=[[R._actual_signed_interval(ws[i]['indices'],ws[j]['indices'],J,cache)
                    for j in range(2)] for i in range(2)]
        # Positive Fourier multiplier upper q_tail(w)<=a_J ||w'||².
        a_upper=16*G.tail_power_interval(J,3)[1]
        taildiag=[a_upper*R.derivative_norm_squared(w['primitive']) for w in ws]
        hmid=[];hrad=[]
        for i in range(2):
            mr=[];rr=[]
            for j in range(2):
                lo,hi=qinterval[i][j]
                tail=B.sqrt_up(taildiag[i]*taildiag[j])
                # Keep known positivity for diagonal omitted energy.
                lower=lo if i==j else lo-tail
                upper=hi+tail
                mr.append((lower+upper)/2-kappa*B.integral_product(ws[i]['primitive'],ws[j]['primitive']))
                rr.append((upper-lower)/2)
            hmid.append(tuple(mr));hrad.append(tuple(rr))
        # For the lower use omitted Gamma's WHOLE PSD order, not
        # independent off-diagonal interval losses that can invent failure.
        finite_Hmid=tuple(tuple(sum(qinterval[i][j])/2-kappa*B.integral_product(
            ws[i]['primitive'],ws[j]['primitive']) for j in range(2)) for i in range(2))
        finite_Hrad=tuple(tuple((qinterval[i][j][1]-qinterval[i][j][0])/2
            for j in range(2)) for i in range(2))
        Hlower=interval_matrix_bound(finite_Hmid,finite_Hrad,False)
        if not psd2(Hlower) or Hlower[0][0]*Hlower[1][1]==Hlower[0][1]**2:
            raise DirectionalSourceError('actual excess Gram positive definiteness not certified')
        Kmid=tuple(tuple(kappa*hmid[i][j]+zmid[i][j] for j in range(2)) for i in range(2))
        Krad=tuple(tuple(kappa*hrad[i][j]+zrad[i][j] for j in range(2)) for i in range(2))
        Kupper=interval_matrix_bound(Kmid,Krad,True)
        Vmid=tuple(tuple(_gram(zp[i],residuals[j]['pieces']) for j in range(2)) for i in range(2))
        Vrad=tuple(tuple(zerror[i]*rnorm[j]+rerror[j]*znorm[i]+zerror[i]*rerror[j]
                        for j in range(2)) for i in range(2))
        correction=inverse_correction_lower(Kupper,Vmid,Vrad,kappa)
        raw=correction['correction_lower']
        # Both the signed correction and zero give valid inverse bounds.
        # Select entire correction only when it has exact PSD order.
        selected=raw if correction['whole_correction_PSD'] else ((F(),F()),(F(),F()))
        result=tuple(tuple(baseline[i][j]+selected[i][j] for j in range(2)) for i in range(2))
        nominal_gain=multiply(transpose(Vmid),multiply(inverse2(Kupper),Vmid))
        family_cap=tuple(tuple(T[i][j]-actual_M[i][j]/kappa+nominal_gain[i][j]/kappa
                              for j in range(2)) for i in range(2))
        directions=((F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(1),F(-1)))
        witnesses=tuple({'direction':c,'upper_family_value':quadratic(family_cap,c)}
                        for c in directions if quadratic(family_cap,c)<0)
        blocks[name]={'indices':indices,'source_kappa':kappa,'auxiliary_levels':tuple(levels),
            'retained_trial_energy_lower':T,'nominal_residual_Gram':actual_M,
            'all_response_coefficients_upper':family_cap,
            'finite_family_negative_witnesses':witnesses,
            'parent_coefficients':tuple(F(t) for t in data['fitted_high_coefficients']),
            'baseline_source_Schur_lower':baseline,'directional_source_Schur_lower':result,
            'candidate_signed_Schur_lower':tuple(tuple(baseline[i][j]+raw[i][j] for j in range(2)) for i in range(2)),
            'excess_Gram_lower':Hlower,'K_upper':Kupper,'coupling_midpoint':Vmid,'coupling_radii':Vrad,
            'auxiliary_action_routes':tuple(a['route'] for a in wa),'residual_column_errors':tuple(rerror),
            'auxiliary_column_errors':tuple(zerror),'strict_Loewner_improvement':correction['whole_correction_PSD'] and any(x for row in raw for x in row),
            'source_Schur_lower_PSD':psd2(result),'correction_certificate':correction}
    return {'source_blob':SOURCE_BLOB,'J':J,'M':M,'source_coercivity_authority':'INHERITED_SOURCE_CONDITIONAL_PR174_K_CLOSURE',
            'original_primitive_space':'L2(I) orthogonal to polynomials degree<=3',
            'one_Gamma_contact_two_poles_true_prime2_halfdensity':True,
            'parity_blocks':blocks,'all_four_first_window_sign_certified':all(v['source_Schur_lower_PSD'] for v in blocks.values()),
            'RH_proved':False}


def outward(x,grid=10**18):
    x=exact(x)
    if type(grid) is not int or grid<=0:raise DirectionalSourceError('positive rounding grid')
    low=F(x.numerator*grid//x.denominator,grid)
    return low,low if low==x else low+F(1,grid)


def _interval_add(x,y):return x[0]+y[0],x[1]+y[1]

def _interval_scale(x,c):
    c=exact(c)
    return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])

def _interval_product(x,y):
    z=tuple(a*b for a in x for b in y)
    return min(z),max(z)


def _interval_quadratic(a,c):
    result=(F(),F())
    for i in range(len(c)):
        for j in range(len(c)):result=_interval_add(result,_interval_scale(a[i][j],c[i]*c[j]))
    return result


def finite_family_obstruction_from_intervals(T,M,K,V,kappa,c):
    """Independent small-rational upper for all response coefficients X.

    Input matrices are entrywise intervals enclosing retained exact T,M,K,V.
    M>=0, K>0, kappa>0 and dimensions two are required. Both matrix
    order premises are certified from the supplied interval enclosures. Establish
      c*(T-M/kappa+V* K^-1 V/kappa)c < 0
    with outward interval arithmetic. This only refutes that fixed family
    of sufficient certificates, never the original source S4.
    """
    def intervals(a):
        if len(a)!=2 or any(len(row)!=2 for row in a):raise DirectionalSourceError('two by two intervals')
        value=tuple(tuple(tuple(exact(z) for z in x) for x in row)for row in a)
        if any(len(x)!=2 or x[0]>x[1] for row in value for x in row):raise DirectionalSourceError('ordered intervals')
        return value
    T,M,K,V=map(intervals,(T,M,K,V));kappa=exact(kappa);c=tuple(exact(x)for x in c)
    if len(c)!=2 or not any(c) or kappa<=0:raise DirectionalSourceError('nonzero direction and positive gap')
    # DIR-5 drops eta*M/kappa. This requires the actual nominal Gram to
    # be PSD; a negative M would reverse the claimed all-eta implication.
    # Fail closed unless the entire symmetric interval enclosure proves it.
    for name,a in (('T',T),('M',M),('K',K)):
        if a[0][1]!=a[1][0]:
            raise DirectionalSourceError(name+' requires symmetric interval entries')
    mmid=tuple(tuple(sum(x)/2 for x in row)for row in M)
    mrad=tuple(tuple((x[1]-x[0])/2 for x in row)for row in M)
    if not psd2(interval_matrix_bound(mmid,mrad,False)):
        raise DirectionalSourceError('nominal residual Gram M>=0 not certified')
    kmid=tuple(tuple(sum(x)/2 for x in row)for row in K)
    krad=tuple(tuple((x[1]-x[0])/2 for x in row)for row in K)
    pinv=inverse2(interval_matrix_bound(kmid,krad,False))
    v=[]
    for row in V:
        x=(F(),F())
        for j in range(2):x=_interval_add(x,_interval_scale(row[j],c[j]))
        v.append(x)
    inverse_upper=F()
    for i in range(2):
        for j in range(2):inverse_upper+=_interval_scale(_interval_product(v[i],v[j]),pinv[i][j])[1]
    tupper=_interval_quadratic(T,c)[1]
    mlower=_interval_quadratic(M,c)[0]
    upper=tupper-mlower/kappa+inverse_upper/kappa
    return {'direction':c,'family_upper_bound':upper,'strict_obstruction':upper<0,
            'all_response_matrices_X_excluded':upper<0,'all_PSD_error_penalties_excluded':upper<0,
            'genuine_source_negative':False}


def compact_source_receipt(result):
    """Small exact interval receipt; original exact run is reproducible."""
    blocks={}
    for name,b in result['parity_blocks'].items():
        entries={tag:tuple(tuple(outward(x)for x in row)for row in b[field])
                 for tag,field in (('T','retained_trial_energy_lower'),('M','nominal_residual_Gram'),
                                    ('K','K_upper'),('V','coupling_midpoint'))}
        witnesses=[finite_family_obstruction_from_intervals(**entries,kappa=b['source_kappa'],c=c)
                   for c in ((F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(1),F(-1)))]
        blocks[name]={'kappa':b['source_kappa'],'auxiliary_levels':b['auxiliary_levels'],
            'parent_coefficients':b['parent_coefficients'],'retained_data_enclosures':entries,
            'independent_all_response_obstructions':witnesses,
            'baseline_lower_enclosure':tuple(tuple(outward(x)for x in row)for row in b['baseline_source_Schur_lower']),
            'signed_correction_enclosure':tuple(tuple(outward(x)for x in row)for row in b['correction_certificate']['correction_lower']),
            'whole_correction_PSD':b['correction_certificate']['whole_correction_PSD'],
            'strict_Loewner_improvement':b['strict_Loewner_improvement'],
            'first_window_sign_certified':b['source_Schur_lower_PSD']}
    return {'source_blob':SOURCE_BLOB,'J':result['J'],'M':result['M'],
        'source_coercivity_authority':result['source_coercivity_authority'],
        'PR178_selected_gamma_definition':{'commit':PR178,'path':'scripts/institute_schur_probe.py',
            'blob':'1a09b58c0c5bdc4a86a756cad640f9f27511c73c','definition':'gamma_coefficients'},
        'PR178_fixed_data_sha256':PR178_DATA_SHA256 if result['J']==24 else None,
        'blocks':blocks,'RH_proved':False}


def fresh_source_direction_holdout(J=5,M=64):
    """Fresh high levels 3,4 versus original exp oracle, before any fitting."""
    params=R.source_parameters();rows=[]
    for i in (1,2):
        a=U.correction_primitive(i,3);b=U.correction_primitive(i,4)
        original=R._actual_signed_interval(a['indices'],b['indices'],J,{})
        packet=R.exact_piecewise_primitive_action(b['primitive'],J,M,18,params)
        center=sum((R.definite(B.mul(a['primitive'],p),l,r)for l,r,p in packet['pieces']),F())
        error=B.sqrt_up(R.norm_squared(a['primitive']))*packet['finite_source_action_error_upper']
        meet=original[0]<=center+error and center-error<=original[1]
        if not meet:raise ArithmeticError('fresh original source direction mismatch')
        # A contact shift changes this pairing by a nonzero exact overlap.
        overlap=B.integral_product(a['primitive'],b['primitive'])
        wrong=center-overlap
        rejected=original[0]>wrong+error or original[1]<wrong-error
        if not rejected:raise ArithmeticError('fresh wrong-contact source mutant escaped')
        rows.append({'derivative_parity':i%2,'levels':(3,4),'J':J,'M':M,
                     'original_pair_interval':original,'independent_continuum_pair':center,
                     'paid_action_pair_error':error,'enclosures_intersect':meet,
                     'wrong_contact_mutant_disjoint':rejected})
    return {'source_blob':SOURCE_BLOB,'fresh_unfitted_direction_checks':rows,'RH_proved':False}
