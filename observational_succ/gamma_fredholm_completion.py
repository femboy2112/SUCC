"""Exact-source Gamma/FUCC completion, with source-tested rational feature Gram.

All stand-alone algebra uses Fraction. The authentic adapters fail closed unless
loaded inside femboy2112/SUCC with its frozen original Suzuki source. No zeros.
The source mathematical QUASI-RH certificate is a conditional equivalence,
not a solution of the all-support positivity problem or of RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt


class CompletionError(ValueError):
    pass


def rat(x):
    if type(x) not in (F, int):
        raise CompletionError('int/Fraction required; floats or bools cannot certify source')
    return F(x)


def divround(x, den=10**25, upper=False):
    x=rat(x)
    n=x.numerator*den//x.denominator
    if upper and F(n,den)<x:n+=1
    return F(n,den)


@dataclass(frozen=True)
class IV:
    lo:F
    hi:F
    def __post_init__(self):
        if type(self.lo) is not F or type(self.hi) is not F or self.lo>self.hi:
            raise CompletionError('ordered Fraction interval required')
    def __add__(self,other):
        o=interval(other)
        return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,other):return self+-interval(other)
    def __rsub__(self,other):return interval(other)+-self
    def __mul__(self,other):
        o=interval(other)
        v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(v),max(v))
    __rmul__=__mul__
    def bound_round(self):return IV(divround(self.lo),divround(self.hi,upper=True))
    def midpoint(self):return (self.lo+self.hi)/2
    def radius(self):return (self.hi-self.lo)/2


def interval(x):
    return x if type(x) is IV else IV(rat(x),rat(x))


def gamma_tail_H01_lower(J, norm_sq, deriv_sq):
    """True omitted OU Gamma lower for u in H^1_0(-1/2,1/2).

    Using Fourier unitary and original d_j=4j+1:
     Gamma_j(u) = 16/d_j^3 int |u_hat(xi)|²/(1+4xi²/d_j²) dxi.
    1/(1+x)>=1-x, so Gamma_j>=16||u||²/d^3-64||u'||²/d^5.
    Integral comparison of arithmetic-progression tails gives the rational
    LOWER sum 2||u||²/d² - (4/d^4+64/d^5)||u'||².
    """
    if type(J) is not int or J<1 or J>1000000:
        raise CompletionError('positive integer Gamma source rung required')
    v,d=rat(norm_sq),rat(deriv_sq)
    if v<=0 or d<0:raise CompletionError('positive L2 and nonnegative derivative energies')
    q=4*J+1
    return 2*v/(q*q)-(F(4,q**4)+F(64,q**5))*d


def gamma_tail_source_upper(J,norm_sq):
    """Imported original GWC source operator-norm Gamma remainder (u metric)."""
    if type(J) is not int or J<1:raise CompletionError('J>=1')
    d=4*J+1
    return (F(2,d*d)+F(16,d**3))*rat(norm_sq)


def odd_legendre_135_witness():
    """u=6P1(2t)-10P3(2t)+4P5(2t), vanishes at both ends."""
    from fractions import Fraction as Z
    # u(t)=3t(2t-1)(2t+1)(84t²-19), exact polynomial identity.
    return {'modes':((1,F(6)),(3,F(-10)),(5,F(4))),
            'u_polynomial_ascending':(F(0),F(57),F(0),F(-480),F(0),F(1008)),
            'norm_sq':F(2136,77),'derivative_norm_sq':F(1296),
            'endpoints_zero':True,'meanzero':True}


def authentic_fifth_mode_completion(J=64):
    """Original SHA-gated strict negative J=64 and full-positive test witness.

    Only source's existing authentic_full_low_entry is licensed. No new source
    coefficients, no nontrivial zero locations, no float/eigenvalue inference.
    """
    if type(J) is not int or J!=64:
        raise CompletionError('source proof scoped to J=64')
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .suzuki_legendre_source import authentic_full_low_entry
    from . import source_weil_hierarchy as source
    receipt=verify_original_suzuki_source()
    if receipt['source_git_blob']!='0cc8510b71d178fc79e8d410a86d8b6014cf9178' or source.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise CompletionError('frozen genuine prime2 source mismatch')
    witness=odd_legendre_135_witness()
    if witness['u_polynomial_ascending']!=(F(0),F(57),F(0),F(-480),F(0),F(1008)):
        raise CompletionError('fifth-mode polynomial mutant')
    rows=witness['modes']
    lo=hi=F(0)
    for i,ci in rows:
        for j,cj in rows:
            q=authentic_full_low_entry(i,j,F(1,2),J)
            scale=ci*cj
            lo+=scale*(q.lo if scale>=0 else q.hi)
            hi+=scale*(q.hi if scale>=0 else q.lo)
    lower=gamma_tail_H01_lower(J,witness['norm_sq'],witness['derivative_norm_sq'])
    upper=source.authentic_positive_gamma_tail_norm(J)*witness['norm_sq']
    if not (hi<0 and lo+lower>0 and upper>=lower):
        raise CompletionError('proposed strict authentic J64/full Gamma sign flip NOT source-certified')
    return {'source_git_blob':receipt['source_git_blob'],'genuine_prime_wavefront':((2,2),),
       'gamma_truncated_J':J,
       'witness_modes':tuple((k,str(c)) for k,c in rows),
       'witness_norm_squared':str(witness['norm_sq']),
       'witness_derivative_norm_squared':str(witness['derivative_norm_sq']),
       'J64_full_signed_source_energy':(str(lo),str(hi)),
       'omitted_gamma_lower_rational':str(lower),
       'omitted_gamma_upper_rational':str(upper),
       'complete_true_gamma_energy_lower':str(lo+lower),
       'complete_true_gamma_energy_upper':str(hi+upper),
       'truncated_negative_strict':hi<0,
       'fully_completed_same_vector_positive_strict':lo+lower>0,
       'fifth_mode_positive_matrix_proved':False,'original_S4_positive_proved':False,
       'RH_proved':False}


def cubic_baseline_inverse_coeff(gamma,w):
    gamma,w=rat(gamma),rat(w)
    if not gamma>w>=0:raise CompletionError('baseline must have uniform positive gap')
    return F(1,gamma), w/(gamma*gamma-w*w), w*w/(gamma*(gamma*gamma-w*w))


def interval_abs_hi(x):
    x=interval(x);return max(abs(x.lo),abs(x.hi))


def finite_feature_gram_model(Binverse,features,D):
    """Exact rational finite surrogate, independent finite full sign oracle.

    B positive, features columns Phi, D symmetric signed. Then B+Phi D Phi*
    PSD iff (Phi*BinvPhi)+... finite source Gram PSD on span(Phi).
    This finite model has no original Suzuki source authority.
    """
    from .finite_gamma_fucc_fredholm import mat,mul,trans,add,psd,eye,inverse
    B=mat(Binverse);n=len(B)
    feats=mat(features)
    if len(feats)!=n:raise CompletionError('feature dimension')
    dim=len(feats[0]);D=mat(D)
    if len(D)!=dim or len(D[0])!=dim:raise CompletionError('signed D dimension')
    Wi=mul(trans(feats),mul(B,feats))
    full=add(inverse(B),mul(feats,mul(D,trans(feats))))
    reduced=add(Wi,mul(Wi,mul(D,Wi)))
    if psd(full)!=psd(reduced):raise ArithmeticError('incorrect finite Fredholm inertia')
    return {'gram':Wi,'finite_short':reduced,'finite_signed_positive':psd(full),
            'source_type':'EXACT_RATIONAL_SURROGATE_NOT_AUTHENTIC_WEIL',
            'RH_proved':False}


# The 34-dimensional original-source feature Gram adapter below deliberately
# takes authentic parameters from the archived source and never infers a sign
# unless its rational Loewner interval test succeeds.

def _overlap(a,b,c,d):return max(F(0),min(b,d)-max(a,c))


def _source_cosh_integral(lo,hi,src,shift=F(0)):
    """Integrate cosh((x+shift)/2) exactly by source rational exp intervals."""
    if hi<=lo:return IV(F(0),F(0))
    def hypo(x):
        z=(x+shift)/2
        if z>=0:
            e=src.exp_pos(z);em=src.exp_neg(z)
        else:
            e=src.exp_neg(-z);em=src.exp_pos(-z)
        return (IV(e.lo,e.hi)+IV(em.lo,em.hi))*F(1,2)
    # sinh derivative and antiderivative: 2 sinh((x+shift)/2)
    def sinh(x):
        z=(x+shift)/2
        if z>=0:
            e=src.exp_pos(z);em=src.exp_neg(z)
        else:
            e=src.exp_neg(-z);em=src.exp_pos(-z)
        return (IV(e.lo,e.hi)-IV(em.lo,em.hi))*F(1,2)
    return (2*(sinh(hi)-sinh(lo))).bound_round()


def _source_sinh_integral(lo,hi,src,shift=F(0)):
    if hi<=lo:return IV(F(0),F(0))
    return (2*(_cosh_rational((hi+shift)/2,src)-_cosh_rational((lo+shift)/2,src))).bound_round()


def _cosh_rational(z,src):
    if z>=0:e=src.exp_pos(z);f=src.exp_neg(z)
    else:e=src.exp_neg(-z);f=src.exp_pos(-z)
    return (IV(e.lo,e.hi)+IV(f.lo,f.hi))*F(1,2)


def _sinh_rational(z,src):
    if z>=0:e=src.exp_pos(z);f=src.exp_neg(z)
    else:e=src.exp_neg(-z);f=src.exp_pos(-z)
    return (IV(e.lo,e.hi)-IV(f.lo,f.hi))*F(1,2)


def _integral_polar(kind,lo,hi,src,shift=F(0)):
    if kind=='c':return _source_cosh_integral(lo,hi,src,shift)
    if kind=='s':return _source_sinh_integral(lo,hi,src,shift)
    raise CompletionError('only original cosh/sinh source poles')


def _integral_polarsq(kind,lo,hi,src):
    if hi<=lo:return interval(0)
    # cosh²(x/2)=(cosh x+1)/2, sinh²=(cosh x-1)/2.
    g=_sinh_rational(hi,src)-_sinh_rational(lo,src)
    return ((g+(hi-lo if kind=='c' else -(hi-lo)))*F(1,2)).bound_round()


def _interval_with_lipschitz(v,delta,L):
    delta=rat(delta)
    return IV(v.lo-L*delta,v.hi+L*delta).bound_round()


def authentic_fredholm_feature_gram(J=8,N=16):
    """Build entire original-source (N+2)x(N+2) rigorous feature Gram packet.

    A lower operator for original H_J is H_lb=B_safe - P_N K_J P_N
    -eps I +2|cosh><cosh|-2|sinh><sinh|. eps allocated in B_safe.
    B_safe uses exact source outward C/w/b intervals and cubic A_b^3=A_b.
    All W entries enclose <feature_i, B_safe^-1 feature_j>.
    D fixed rational contains the true cell OU Loewner MAJORANT plus polar pair.
    The packet does NOT assert W+WDW PSD unless separately certified.
    """
    if type(J) is not int or J!=8 or type(N) is not int or not 14<=N<=16:
        raise CompletionError('original proof budget J8 with 14<=N<=16 needed for safe B reference')
    from . import source_weil_hierarchy as src
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .finite_gamma_fucc_fredholm import gamma_scalar_prefix,gamma_cell_interval_matrix,RationalInterval
    receipt=verify_original_suzuki_source()
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):raise CompletionError('source prime activation')
    b=src.log2_iv(); w=src.log2_iv()*src.sqrt_inverse(2); C=src.contact_iv()
    width=b.hi-b.lo; b0=(b.lo+b.hi)/2
    h=F(1,N);eps=F(2*J,3*N)
    gamma=gamma_scalar_prefix(J)-C.hi-eps-(w.hi-w.lo)/2
    wmid=(w.lo+w.hi)/2
    if not gamma>wmid>0:raise CompletionError('original source signed positive reference fails')
    coeff=cubic_baseline_inverse_coeff(gamma,wmid)
    def exp_iv(z):
        r=src.exp_neg(z);return RationalInterval(r.lo,r.hi)
    K=gamma_cell_interval_matrix(J,N,exp_iv)
    kmid=[[((K[i][j].lo+K[i][j].hi)/2) for j in range(N)] for i in range(N)]
    krad=max(sum((K[i][j].hi-K[i][j].lo)/2 for j in range(N)) for i in range(N))
    # Genuine OU source K <= cell-cell midpoint + radius I, as Loewner matrices.
    D=[[F(0) for j in range(N+2)] for i in range(N+2)]
    for i in range(N):
        for j in range(N):D[i][j]=-N*(kmid[i][j]+(krad if i==j else F(0)))
    D[N][N]=F(2);D[N+1][N+1]=F(-2)
    W=[[interval(0) for j in range(N+2)] for i in range(N+2)]
    left=-F(1,2); right=F(1,2)
    cells=[(left+i*h,left+(i+1)*h) for i in range(N)]
    edgeL=(left,right-b0);edgeR=(b0+left,right)
    def edge_segment_integral(func,lo,hi):
        return _integral_polar(func,max(lo,edgeL[0]),min(hi,edgeL[1]),src)+_integral_polar(func,max(lo,edgeR[0]),min(hi,edgeR[1]),src)
    # Exact source-u overlap for rational b0, then pay Lipschitz b interval error.
    def cellA_polar(kind,lo,hi):
        lo1=max(lo,left);hi1=min(hi,right-b0)
        lo2=max(lo,b0+left);hi2=min(hi,right)
        return _integral_polar(kind,lo1,hi1,src,b0)+_integral_polar(kind,lo2,hi2,src,-b0)
    for i,(lo,hi) in enumerate(cells):
        for j in range(i,N):
            u0=interval(h if i==j else 0)
            dd=(j-i)*h
            u1=_interval_with_lipschitz(interval(max(F(0),h-abs(dd-b0))),width,1)
            u2=interval(_overlap(lo,hi,*edgeL)+_overlap(lo,hi,*edgeR) if i==j else 0)
            if i==j:u2=_interval_with_lipschitz(u2,width,2)
            val=sum((coeff[k]*u for k,u in enumerate((u0,u1,u2))),interval(0)).bound_round()
            W[i][j]=W[j][i]=val
        for idx,kind in ((N,'c'),(N+1,'s')):
            v0=_integral_polar(kind,lo,hi,src)
            v1=_interval_with_lipschitz(cellA_polar(kind,lo,hi),width,4)
            v2=_interval_with_lipschitz(edge_segment_integral(kind,lo,hi),width,3)
            v=sum((coeff[k]*u for k,u in enumerate((v0,v1,v2))),interval(0)).bound_round()
            W[i][idx]=W[idx][i]=v
    for idx,kind in ((N,'c'),(N+1,'s')):
        v0=_integral_polarsq(kind,left,right,src)
        v2=_integral_polarsq(kind,edgeL[0],edgeL[1],src)+_integral_polarsq(kind,edgeR[0],edgeR[1],src)
        # f A f =2 int_(left)^(right-b) f(x)f(x+b)dx.
        upper=right-b0
        # cosh*cosh=(cosh(x+b/2)+cosh(b/2))/2; sinh*sinh= (... - cosh(b/2))/2
        v1=_sinh_rational(upper+b0/2,src)-_sinh_rational(left+b0/2,src)
        v1=v1 + (upper-left)*_cosh_rational(b0/2,src)*(1 if kind=='c' else -1)
        v1=_interval_with_lipschitz(v1,width,8)
        v2=_interval_with_lipschitz(v2,width,4)
        W[idx][idx]=sum((coeff[k]*u for k,u in enumerate((v0,v1,v2))),interval(0)).bound_round()
    W[N][N+1]=W[N+1][N]=interval(0)  # global reflection parity of Bsafe.
    # Semantically evaluate actual finite signed feature-Gram inequality.
    Wmid=[[v.midpoint() for v in row] for row in W]
    Wrad=max(sum(v.radius() for v in row) for row in W)
    Dnorm=max(sum(abs(v) for v in row) for row in D)
    Wnorm=max(sum(abs(v) for v in row) for row in Wmid)
    # Interval perturbation W -> W+WDW with arbitrary signed D.
    perturb=Wrad*(1+2*Dnorm*Wnorm)+Wrad*Wrad*Dnorm
    dim=N+2
    # Matrix Mmid = Wmid + Wmid D Wmid, exact rational.
    prod=[[sum((D[i][k]*Wmid[k][j] for k in range(dim)),F()) for j in range(dim)] for i in range(dim)]
    M=[[Wmid[i][j]+sum((Wmid[i][k]*prod[k][j] for k in range(dim)),F()) for j in range(dim)] for i in range(dim)]
    # A strict certified positive packet needs exact LDL on M-perturbI.
    from .finite_gamma_fucc_fredholm import psd
    # eps floor bound not sign: M may be indefinite, cannot infer actual source negativity.
    positive_certified=psd(tuple(tuple(M[i][j]-(perturb if i==j else 0) for j in range(dim)) for i in range(dim)))
    if positive_certified: raise CompletionError('unexpected certificate: independently audit before promoting first window')
    return {'source_sha':receipt['source_git_blob'],
       'true_prime_wavefront':((2,2),),'rungs':J,'cell_count':N,'dimension':dim,
       'true_b_interval':(str(b.lo),str(b.hi)),
       'true_w_interval':(str(w.lo),str(w.hi)),
       'true_contact_interval':(str(C.lo),str(C.hi)),
       'positive_baseline_gap_rational':str(gamma-wmid),
       'finite_ou_cell_Loewner_radius':str(krad),
       'infinite_to_cell_operator_error':str(eps),
       'closed_source_W_interval':tuple(tuple((str(x.lo),str(x.hi)) for x in row) for row in W),
       'signed_D_rational':tuple(tuple(str(x) for x in row) for row in D),
       'feature_gram_midpoint_signed':tuple(tuple(str(x) for x in row) for row in M),
       'feature_gram_Loewner_error_upper':str(perturb),
       'source_positivity_certified':False,
       'result':'INCONCLUSIVE_FINITE_GAMMA_SUFFICIENT_TEST',
       'RH_proved':False}


def authentic_endpoint_zero_four_dimensional_compensation(J=64):
    """Original-source exact FULL Gamma positivity on four lawful endpoint-zero modes.

    span(P1-P3,P3-P5,P2-P4,P4-P6) is four dimensional, H^1_0 and mean-zero.
    Fourier-tail Loewner bound is an operator inequality on this whole span;
    unlike testing four unrelated diagonal modes, we check both 2x2 blocks.
    """
    if type(J) is not int or J!=64:
        raise CompletionError('this source theorem is pinned to J=64')
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .suzuki_legendre_source import authentic_full_low_entry
    from . import source_weil_hierarchy as src
    verified=verify_original_suzuki_source()
    if src.authenticated_prime_wavefront(F(1,2))!=((2,2),):raise CompletionError('fake prime tape')
    t=F(4,(4*J+1)**4)+F(64,(4*J+1)**5)
    a=F(2,(4*J+1)**2)
    proof={}
    cases={
      'odd_u_even_primitive':((1,3,5),((F(10,21),F(-1,7)),(F(-1,7),F(18,77))),((F(20),F(0)),(F(0),F(36)))),
      'even_u_odd_primitive':((2,4,6),((F(14,45),F(-1,9)),(F(-1,9),F(22,117))),((F(28),F(0)),(F(0),F(44))))
    }
    for sector,(indices,M,D) in cases.items():
        i,j,k=indices
        entries={(r,s):authentic_full_low_entry(r,s,F(1,2),J)
                 for r,s in ((i,i),(i,j),(i,k),(j,j),(j,k),(k,k))}
        # INTERVAL proxy needs actual source's .lo and .hi, not an invented source!
        E={(r,s):IV(z.lo,z.hi) for (r,s),z in entries.items()}
        low11=E[i,i]+E[j,j]-2*E[i,j]
        low22=E[j,j]+E[k,k]-2*E[j,k]
        low12=E[i,j]-E[i,k]-E[j,j]+E[j,k]
        W11=low11+a*M[0][0]-t*D[0][0]
        W22=low22+a*M[1][1]-t*D[1][1]
        W12=low12+a*M[0][1]-t*D[0][1]
        det_lower=W11.lo*W22.lo-interval_abs_hi(W12)**2
        if not (W11.lo>0 and W22.lo>0 and det_lower>0):
            raise CompletionError('full original completed Gamma endpoint-zero 2x2 PSD NOT certified for '+sector)
        proof[sector]={
          'raw_basis':(f'P{i}-P{j}',f'P{j}-P{k}'),
          'u_norm_gram_exact':tuple(tuple(str(z) for z in r) for r in M),
          'du_norm_gram_exact':tuple(tuple(str(z) for z in r) for r in D),
          'full_Gamma_2x2_Loewner_lower':(
             ((str(W11.lo),str(W11.hi)),(str(W12.lo),str(W12.hi))),
             ((str(W12.lo),str(W12.hi)),(str(W22.lo),str(W22.hi)))),
          'determinant_strict_positive_lower':str(det_lower),
          'matrix_strictly_positive_certified':True,
          'original_source_complete_test_sector':True,
        }
    return {'original_source_git_blob':verified['source_git_blob'],
            'source_a':'1/2','gamma_prefix':J,
            'genuine_prime_power_tape':((2,2),),
            'gamma_H01_tail_Loewner_norm_multiplier':str(a),
            'gamma_H01_tail_Loewner_derivative_subtraction':str(t),
            'source_complete_two_parity_blocks':proof,
            'strict_completed_original_source_positive_on_four_dimensional_subspace':True,
            'not_positive_on_arbitrary_test_space_claimed':True,
            'original_first_window_S4_proved':False,
            'RH_proved':False}
