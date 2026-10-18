"""Source-faithful K-relative Suzuki Schur rescue using clamped Jacobi trials.

No arbitrary H1->L2 inverse bound.  All coefficients are exact Fractions.
The authentic source adapter reads the unchanged signed Suzuki block (Gamma,
prime2 half-density, contact, BOTH poles).  An independently certified
continuum action-residual norm is STILL required to close any Schur sign.
"""
from fractions import Fraction as F
from math import isqrt

SOURCE_SHA="0cc8510b71d178fc79e8d410a86d8b6014cf9178"

class KResidualError(ValueError):
    pass

def q(x):
    if type(x) not in (F,int):raise KResidualError("Fraction/int only; reject float and bool")
    return F(x)

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def add(a,b):
    return trim(tuple((a[i] if i<len(a) else F(0))+
                      (b[i] if i<len(b) else F(0))
                      for i in range(max(len(a),len(b)))))

def scale(a,c):return trim(tuple(q(c)*v for v in a))

def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return trim(z)

def derivative(a):return trim(tuple(i*a[i] for i in range(1,len(a))) or (F(0),))

def integral_product(a,b):
    p=mul(a,b)
    return sum((c*(F(1,2)**(i+1)-(-F(1,2))**(i+1))/(i+1)
                for i,c in enumerate(p)),F(0))

def legendre(n):
    if type(n) is not int or not 0<=n<=30:raise KResidualError("Legendre degree 0..30")
    if n==0:return (F(1),)
    if n==1:return (F(0),F(2))
    prev,cur=(F(1),),(F(0),F(2))
    for k in range(1,n):
        prev,cur=cur,scale(add(scale(mul((F(0),F(2)),cur),2*k+1),
                                   scale(prev,-k)),F(1,k+1))
    return cur

def value(a,x):return sum((c*x**i for i,c in enumerate(a)),F(0))

# (1-4t²)^2 times Jacobi P_4^(2,2)(2t) and P_5^(2,2)(2t).
# These clamped primitives are orthogonal to ALL polynomials of degree <=3.
CLAMPED={
  "odd_derivative":{
    "poly":(F(15,16),F(0),F(-75),F(0),F(1050),F(0),F(-5040),F(0),F(7920)),
    "coeff":((5,F(-240,13)),(7,F(240,13))),
    "norm":F(640,2431),"d1":F(7680,143),"d2":F(230400,13)},
  "even_derivative":{
    "poly":(F(0),F(105,8),F(0),F(-490),F(0),F(5292),F(0),F(-22176),F(0),F(32032)),
    "coeff":((6,F(-112,5)),(8,F(112,5))),
    "norm":F(56448,230945),"d1":F(75264,1105),"d2":F(150528,5)},
}

def checked_trial(which):
    if which not in CLAMPED:raise KResidualError("only exact clamped Q4 trials allowed")
    data=CLAMPED[which]; p=data["poly"];w=derivative(p);d2=derivative(w)
    if any(value(a,end)!=0 for a in (p,w) for end in (-F(1,2),F(1,2))):
        raise ArithmeticError("false endpoint H2_0 extension")
    if any(integral_product(w,legendre(k)) for k in (1,2,3,4)):
        raise ArithmeticError("original Q4 high moment leakage")
    recon=(F(0),)
    for k,c in data["coeff"]:recon=add(recon,scale(legendre(k),c))
    if recon!=w:raise ArithmeticError("high Jacobi/Legendre coefficient error")
    if (integral_product(p,p),integral_product(w,w),integral_product(d2,d2))!=(
        data["norm"],data["d1"],data["d2"]):
        raise ArithmeticError("independent exact polynomial norm mismatch")
    return {"parity":which,"source_type":"EXACT_ORIGINAL_Q4_CLAMPED_PRIMITIVE",
      "legendre_high_modes":tuple((k,str(c)) for k,c in data["coeff"]),
      "primitive_norm_sq":str(data["norm"]),"first_derivative_norm_sq":str(data["d1"]),
      "second_derivative_norm_sq":str(data["d2"]),
      "source_Q4_constraints":True,"zero_value_AND_zero_derivative_traces":True,
      "RH_proved":False}

def sqrt_up(x,scale_digits=10**10):
    x=q(x)
    if x<0 or type(scale_digits) is not int or scale_digits<1:
        raise KResidualError("nonnegative exact squared norm and integer precision")
    k=isqrt(x.numerator*scale_digits**2//x.denominator)
    return F(k,scale_digits) if F(k*k,scale_digits**2)==x else F(k+1,scale_digits)

def gamma_action_tail(J):
    """||Gamma_tail F||_2 <= tau_J ||F''||_2 for zero-extended H2 F.

    Original Fourier symbol 16 xi²/[d(d²+4xi²)] <=16 xi²/d³;
    sum_j>=J 16/(4j+1)^3 <=2/d_J²+16/d_J³.
    """
    if type(J) is not int or not 1<=J<=100000:raise KResidualError("Gamma depth")
    d=4*J+1
    return F(2,d*d)+F(16,d**3)

def low_primitive_norm_sq(i):
    if type(i) is not int or not 1<=i<=30:raise KResidualError("genuine Legendre")
    return (F(1,2*i-1)+F(1,2*i+3))/(4*(2*i+1)**2)

def interval_form(entries,coeff):
    lo=hi=F(0)
    for i,ci in coeff:
        for j,cj in coeff:
            v=entries[(i,j)];k=ci*cj
            lo+=k*(v.lo if k>=0 else v.hi)
            hi+=k*(v.hi if k>=0 else v.lo)
    return lo,hi

def authentic_clamped_signed_source(J=12):
    """Read genuine Suzuki original low/high entries, with Gamma completion tails.

    Reports authenticated MIXED ENERGY intervals, not the missing entire
    continuum residual ||g-H_J F||. This is not a Schur positivity certificate.
    """
    if type(J) is not int or not 1<=J<=75:
        raise KResidualError("frozen Suzuki matrix source J=1..75")
    from .tate_suzuki_shorting import verify_original_suzuki_source
    from .suzuki_legendre_source import authentic_full_low_entry
    from . import source_weil_hierarchy as source
    passport=verify_original_suzuki_source()
    if passport["source_git_blob"]!=SOURCE_SHA or source.authenticated_prime_wavefront(F(1,2))!=((2,2),):
        raise KResidualError("wrong pinned signed source or fake prime impulse")
    tau=gamma_action_tail(J)
    packs={}
    for name,model in CLAMPED.items():
        checked_trial(name)
        basis=model["coeff"]
        matrix={(i,k):authentic_full_low_entry(i,k,F(1,2),J)
                for i,_ in basis for k,_ in basis}
        hlo,hhi=interval_form(matrix,basis)
        correction=tau*sqrt_up(model["norm"]*model["d2"])
        mixed={}
        for i in range(1,5):
            lo=hi=F(0)
            for k,c in basis:
                x=authentic_full_low_entry(i,k,F(1,2),J)
                lo+=c*(x.lo if c>=0 else x.hi)
                hi+=c*(x.hi if c>=0 else x.lo)
            err=tau*sqrt_up(low_primitive_norm_sq(i)*model["d2"])
            mixed[str(i)]={"genuine_finite_signed_interval":(str(lo),str(hi)),
                "completed_signed_interval":(str(lo-err),str(hi+err)),
                "tail_abs_error_upper":str(err)}
        packs[name]={
            "genuine_finite_high_energy":(str(hlo),str(hhi)),
            "full_Gamma_high_energy":(str(hlo),str(hhi+correction)),
            "full_Gamma_energy_tail_upper":str(correction),
            "full_Gamma_action_tail_factor":str(tau),
            "original_signed_low_high_mixed":mixed,
            "complete_continuum_action_residual_norm_observed":False,
            "S4_positive_proved":False}
    return {"source_git_blob":passport["source_git_blob"],"source_radius":"1/2",
        "original_prime_wavefront":((2,2),),"source_Gamma_prefix_rungs":J,
        "all_Gamma_prime_contact_two_poles_preserved":True,
        "parity_clamped_high_packets":packs,"RH_proved":False}

def conditional_schur_residual_envelope(kappa,pair_interval,energy_interval,
                                       action_residual_norm,tail_action_norm=F(0)):
    """A posteriori exact Riesz/K-relative response bounds in primitive L2.

    Hypotheses: source D>=kappa I after primitive K completion; lawful x in
    Dom(D); source g in that Hilbert space; independently CERTIFIED true
    ||g-D_J x||<=action_residual_norm, ||(D-D_J)x||<=tail_action_norm.
    A 4x4 Galerkin block alone DOES NOT certify that residual. Fail closed
    as a conditional PROBE, never report source positivity.
    """
    k=q(kappa);lo,hi=map(q,pair_interval);dlo,dhi=map(q,energy_interval)
    residual=q(action_residual_norm);tail=q(tail_action_norm)
    if not (k>0 and lo<=hi and dlo<=dhi and residual>=0 and tail>=0):
        raise KResidualError("coercivity, energy and norm certificate malformed")
    return {"schur_response_lower":str(2*lo-dhi),
            "schur_response_upper":str(2*hi-dlo+(residual+tail)**2/k),
            "correct_space":"PRIMITIVE_K_HILBERT_NOT_DERIVATIVE_L2",
            "actual_original_S4_sign_proved":False,
            "full_source_action_residual_certified_by_this_function":False,
            "RH_proved":False}
