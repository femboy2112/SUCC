"""Whole-continuum prime-2 inverse savings on the original Suzuki source.

Independently replays the all-high Bessel source budget, retains its omitted
prime mismatch, and charges residual error in the non-scalar inverse norm.
No fabricated L2 gap on derivative coordinates, finite high-spectrum claim,
or zero-coordinate input. Paper theorem: ROUND2_SIGNED_PRIME_RESOLVENT.md.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from . import original_continuum_residual as R
from . import clamped_k_residual_bridge as B

SOURCE_BLOB = '0cc8510b71d178fc79e8d410a86d8b6014cf9178'
PR161_HEAD = 'eb62620300add80f8b38ebf0f7cd54c2a3c5ae36'
PR177_HEAD = 'f309d9104ba480c1999c962af1df7c50f19e1bfe'
PR179_AUDITED_HEAD = '81684b4b8956f9f5da56c376ba7e4339277eb665'


def exact(x):
    if type(x) not in (int,Q):
        raise ValueError('exact integer/Fraction required')
    return Q(x)


def bessel_coefficients(ell, order):
    """Independent factorial formula, not the inherited recurrence."""
    if type(ell) is not int or type(order) is not int or ell<0 or order<0:
        raise ValueError('nonnegative integer mode/order')
    return tuple(Q((-1)**k * 2**ell * factorial(ell+k),
                   factorial(k)*factorial(2*ell+2*k+1)) for k in range(order+1))


def gamma_symbol(frequency, count=256):
    """Fourier transform of 4/d I minus the OU convolution, directly."""
    x=exact(frequency)
    return sum((Q(4,4*j+1)-Q(4*(4*j+1),(4*j+1)**2+4*x*x)
                for j in range(count)),Q())


@lru_cache(maxsize=2)
def independent_high_budget(sector):
    """All-high source budget via separate coefficient/integral implementation.

    Same primary Gamma/Legendre theorem and source constants; this is a
    differently implemented mathematical check, not an independent source.
    """
    if sector not in ('odd','even'):
        raise ValueError('derivative reflection parity required')
    R.source_parameters()  # immutable source and complete first-prime tape
    from . import source_weil_hierarchy as source
    start,L,omega=(4,20,Q(16)) if sector=='odd' else (5,21,Q(18))
    order,cells,slack=14,128,Q(1,2000)
    modes=[(ell,bessel_coefficients(ell,order)) for ell in range(start,L,2)]
    endpoint=omega/2
    gamma=gamma_symbol(omega)
    weighted=Q()
    # Directly integrate each individual square; no inherited compiled
    # global antiderivative or Bessel-coefficient recurrence is called.
    integrands=[]
    for ell,coeff in modes:
        square={}
        for i,ci in enumerate(coeff):
            for j,cj in enumerate(coeff):
                power=2*ell+2*(i+j)+1
                square[power]=square.get(power,Q())+Q(2*ell+1,power)*ci*cj
        integrands.append(square)
    previous=[Q() for _ in integrands]
    for cell in range(cells):
        left=omega*cell/cells
        right=omega*(cell+1)/cells
        a,b=left/2,right/2
        integrals=[]
        remainders=[]
        for j,((ell,coeff),powers) in enumerate(zip(modes,integrands)):
            value=sum((c*b**p for p,c in powers.items()),Q())
            integrals.append(value-previous[j]);previous[j]=value
            first=abs(bessel_coefficients(ell,order+1)[-1])*b**(ell+2*(order+1))
            ratio=b*b/Q(2*(order+2)*(2*ell+2*order+5))
            assert 0<=ratio<1
            remainders.append((2*ell+1)*(first/(1-ratio))**2)
        polynomial_integral=sum(integrals,Q())
        assert polynomial_integral>=0
        bound=(1+slack)*polynomial_integral+(1+1/slack)*(b-a)*sum(remainders,Q())
        weighted+=(gamma-gamma_symbol(left))*bound
    double_factorial=Q(factorial(2*L+1),2**L*factorial(L))
    angular=endpoint**(2*L+1)/double_factorial**2/(1-(endpoint/(2*L+3))**2)
    leakage=2/source.pi_iv().lo*(weighted+gamma*angular)
    contact=source.contact_iv().hi
    prime=(source.log2_iv()*source.sqrt_inverse(2)).hi
    negative_pole=Q(0) if sector=='odd' else Q(8)*Q(1,4)**10/factorial(5)**2
    floor=Q(63,500) if sector=='odd' else Q(153,500)
    margin=gamma-leakage-contact-prime-negative_pole
    assert margin>floor
    return {'sector':sector,'source_blob':SOURCE_BLOB,'gamma':gamma,
            'leakage':leakage,'contact_upper':contact,'prime_upper':prime,
            'negative_pole_upper':negative_pole,'exact_margin':margin,
            'kappa':floor,'prime_surplus_weight_floor':Q(12,25),
            'all_high_quantifier':'primitive E intersect source closed form domain',
            'derivative_L2_gap_claimed':False}


def matrix_psd(m):
    return m[0][0]>=0 and m[1][1]>=0 and m[0][1]==m[1][0] and m[0][0]*m[1][1]>=m[0][1]**2


def matrix_pd(m):
    return m[0][0]>0 and m[0][1]==m[1][0] and m[0][0]*m[1][1]>m[0][1]**2


def project_pieces(pieces):
    moments=R.projected_piece_moments(pieces)
    polynomial=(Q(0),)
    for degree,moment in enumerate(moments):
        polynomial=B.add(polynomial,B.scale(B.legendre(degree),-(2*degree+1)*moment))
    return tuple((left,right,B.add(poly,polynomial))for left,right,poly in pieces)


def source_regions(parameters):
    if parameters!=R.source_parameters():
        raise ValueError('original Gamma/contact/pole/half-density parameters required')
    b,db=parameters['b'],parameters['db']
    center=(-Q(3,16),Q(3,16))
    edge=(Q(1,5),Q(49,100))
    if not (center[1]<b-db-R.A and edge[0]>b+db-R.A and edge[1]<R.A
            and edge[0]-b-db>-R.A and edge[1]-b+db<R.A-b):
        raise ValueError('fixed center/edge region leaves true source geometry')
    if parameters['w']-parameters['dw']<Q(12,25):
        raise ValueError('authentic prime2 weight floor failed')
    return center,edge


def whole_resolvent_saving(projected, parameters, kappa, theta=Q(1,1024)):
    """Lower matrix for kappa^-1 M minus the actual ambient B^-1 Gram.

    Source parameter error here affects only translation of the KNOWN
    nominal residual. Its full original-source action error is paid once,
    separately, in the B^-1 norm bound; it is not subtracted again here.
    """
    kappa,theta=exact(kappa),exact(theta)
    if kappa<=0 or not 0<theta<1 or len(projected)!=2:
        raise ValueError('positive kappa, 0<theta<1, two source columns')
    center,edge=source_regions(parameters)
    mismatch=[];shift_errors=[]
    expected_cells=((-R.A,R.A-parameters['b']),
                    (R.A-parameters['b'],parameters['b']-R.A),
                    (parameters['b']-R.A,R.A))
    for pieces in projected:
        if tuple((l,r)for l,r,_ in pieces)!=expected_cells:
            raise ValueError('exact source partition required')
        left,mid,right=pieces
        if not (center[0]>=mid[0] and center[1]<=mid[1]
                and edge[0]>=right[0] and edge[1]<=right[1]):
            raise ValueError('piecewise source residual has incompatible cells')
        mismatch.append(B.add(right[2],B.scale(R.shifted(left[2],-parameters['b']),-1)))
        derivative=B.derivative(left[2])
        energy=R.definite(B.mul(derivative,derivative),left[0],left[1])
        shift_errors.append(parameters['db']*B.sqrt_up(energy))
    C=tuple(tuple(R.definite(B.mul(projected[i][1][2],projected[j][1][2]),*center)
                  for j in range(2))for i in range(2))
    E=tuple(tuple(R.definite(B.mul(mismatch[i],mismatch[j]),*edge)
                  for j in range(2))for i in range(2))
    assert matrix_psd(C) and matrix_psd(E)
    penalty=(1/theta-1)*sum((e*e for e in shift_errors),Q())
    E_lower=tuple(tuple((1-theta)*E[i][j]-(penalty if i==j else 0)
                        for j in range(2))for i in range(2))
    w=Q(12,25)
    alpha=w/(kappa*(kappa+w))
    beta=w/(kappa*(kappa+2*w))
    saving=tuple(tuple(alpha*C[i][j]+beta*E_lower[i][j]
                       for j in range(2))for i in range(2))
    return {'center_region':center,'edge_region':edge,'center_Gram':C,
            'edge_nominal_Gram':E,'edge_transport_error':shift_errors,
            'edge_Gram_lower':E_lower,'source_inverse_saving_lower':saving,
            'strict_positive_saving':matrix_pd(saving),
            'w_floor':w,'center_coefficient':alpha,'edge_coefficient':beta}


def source_schur_improvement(J=8,M=80,P=18,eta=Q(1,4)):
    """Actual signed source, fixed trials and errors, new non-scalar inverse."""
    if type(J)is not int or not 1<=J<=24 or type(M)is not int or not 1<=M<=192:
        raise ValueError('bounded original source packet required')
    eta=exact(eta)
    if eta<=0:raise ValueError('positive Young parameter required')
    params=R.source_parameters()
    audits={p:independent_high_budget(p)for p in ('odd','even')}
    baseline=R.source_residual_schur_trial(J=J,M=M,P=P,fit=True,eta=eta)
    sectors={}
    for name,data in baseline['four_original_parity_Schur_blocks'].items():
        parity='odd'if name=='odd_derivative'else'even'
        kappa=audits[parity]['kappa']
        assert kappa==Q(data['source_kappa'])
        projected=[]
        for index,t in zip(data['indices'],data['fitted_high_coefficients']):
            h=R.high_boundary_match(index,Q(t))['h']
            assert all(B.value(p,x)==0 for p in (h,B.derivative(h))for x in (-R.A,R.A))
            packet=R.exact_piecewise_primitive_action(h,J,M,P,params)
            projected.append(project_pieces(packet['pieces']))
        nominal=tuple(tuple(R.projected_piece_gram(projected[i],projected[j])for j in range(2))for i in range(2))
        inherited=tuple(tuple(Q(v)for v in row)for row in data['surrogate_QE_action_residual_gram_exact'])
        assert nominal==inherited,'actual complete continuum residual must match'
        saving=whole_resolvent_saving(projected,params,kappa)
        old=tuple(tuple(Q(v)for v in row)for row in data['genuine_source_2x2_Schur_Loewner_lower'])
        gain=tuple(tuple((1+eta)*v for v in row)for row in saving['source_inverse_saving_lower'])
        new=tuple(tuple(old[i][j]+gain[i][j]for j in range(2))for i in range(2))
        sectors[name]={'kappa':kappa,'fitted_high_coefficients':data['fitted_high_coefficients'],
            'old_lower':old,'new_lower':new,'gain':gain,'gain_PD':matrix_pd(gain),
            'new_lower_PSD':matrix_psd(new),'continuum_residual_Gram':nominal,
            'unchanged_finite_source_errors':data['finite_source_action_error_each'],
            'unchanged_Gamma_tail_errors':data['genuine_omitted_Gamma_action_error_each'],
            **saving}
    return {'source_blob':SOURCE_BLOB,'base_commit':PR177_HEAD,'audited_PR161':PR161_HEAD,
        'J':J,'M':M,'P':P,'eta':eta,'source_high_budget_audit':audits,'sectors':sectors,
        'both_blocks_strictly_improved':all(v['gain_PD']for v in sectors.values()),
        'first_window_sign_certified':all(v['new_lower_PSD']for v in sectors.values()),
        'RH_proved':False,'imports_from_PR178':[],'imports_from_PR179':[]}
