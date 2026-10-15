"""Source-indexed heat -> completed Weil functional: exact laws, bounded arch ladder.

Zero-independent CONSTRUCTION.  The identity with Weil's zero distribution is
an EXTERNAL CLASSICAL THEOREM (Weil explicit formula, Suzuki Eq. 3.3), never
presented as a derivation of RH.  On compact C^2 tests the prime source is
locally finite and the archimedean spectral ladder has a proven O(1/J)
absolute remainder.  A separate one-parameter noncompact resolvent test
identifies the complete logarithmic derivative in Re(s)>1.

The arithmetic source is the actual von Mangoldt function, not an arbitrary
numerical sample of zeta zeros.  Mutant coefficients and gamma parameters
are explicitly separate mathematical countermodels.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, log
from typing import Callable


class WeilTransportError(ValueError):
    """A source, normalization, domain or finite-test precondition is missing."""


def _mp():
    try:
        import mpmath as mp
    except ImportError as err:
        raise WeilTransportError("mpmath research extra required") from err
    return mp


def _number(v):
    mp = _mp()
    if isinstance(v, Fraction):
        return mp.mpf(v.numerator)/v.denominator
    if type(v) is int:
        return mp.mpf(v)
    return mp.mpf(v)


def _complex_arg(v):
    mp = _mp()
    if type(v) in (int, Fraction):
        return mp.mpc(_number(v))
    if type(v) is bool:
        raise WeilTransportError("Boolean is not a complex analytic parameter")
    return mp.mpc(v)


def _rational(v):
    if type(v) not in (int, Fraction):
        raise WeilTransportError("Exact rational certificate inputs required")
    return Fraction(v)


def _integer(n, minval=0):
    if type(n) is not int or n<minval:
        raise WeilTransportError("Expected exact nonnegative integer in domain")
    return n


def _prime(n:int)->bool:
    _integer(n)
    if n < 2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True


def von_mangoldt_labels(N:int)->tuple[tuple[int,int],...]:
    """Exact atomic source (n,p), Λ(n)=log(p), n=p^k and n<=N."""
    _integer(N,2)
    if N > 200_000:
        raise WeilTransportError("Finite source ceiling 200000, no silent truncation")
    sieve=bytearray(b'\x01')*(N+1)
    sieve[0:2]=b'\x00\x00'
    for q in range(2,isqrt(N)+1):
        if sieve[q]:
            sieve[q*q:N+1:q]=b'\x00'*(((N-q*q)//q)+1)
    out=[]
    for p in range(2,N+1):
        if not sieve[p]:continue
        m=p
        while m<=N:
            out.append((m,p))
            m*=p
    return tuple(sorted(out))


def prime_heat(t, N:int, dps:int=45):
    """Finite part of source heat J(t)=sum Λ(n) exp(-πt n²)."""
    mp=_mp();mp.mp.dps=dps
    tt=_number(t)
    if tt<=0: raise WeilTransportError("Gaussian heat time must be positive")
    return mp.fsum(mp.log(p)*mp.exp(-mp.pi*tt*n*n) for n,p in von_mangoldt_labels(N))


def heat_mellin_normalization(s):
    """Gamma_R(s), Gaussian arch factor under dx/|x| and e^(-π x²)."""
    mp=_mp();ss=_complex_arg(s)
    if ss.real<=0: raise WeilTransportError("Gaussian Mellin needs Re(s)>0")
    return mp.power(mp.pi,-ss/2)*mp.gamma(ss/2)


def heat_mellin_prime_fraction(s,N:int):
    """M[J_N](s)/Gamma_R(s) = sum_{n<=N} Λ(n)n^(-s), Re(s)>0.

    The Mellin integral is the exact analytical definition, not evaluated
    by a numerical improper integral here.  The finite Gamma cancellation is
    a derived identity.
    """
    mp=_mp(); ss=_complex_arg(s)
    if ss.real<=0:raise WeilTransportError("Fixed finite heat Mellin needs Re(s)>0")
    return mp.fsum(mp.log(p)*mp.power(n,-ss) for n,p in von_mangoldt_labels(N))


def prime_heat_tail_bound(sigma,N:int):
    """Rigorous tail majorant for sum_{n>N} Λ(n)n^(-sigma), sigma>1,N>=3.

    Bound: N^(1-σ) [log N/(σ-1)+1/(σ-1)^2].  Numeric evaluation of the
    elementary RHS is mpmath, while the inequality is a paper proof.
    """
    mp=_mp(); sig=_number(sigma);_integer(N,3)
    if sig<=1:raise WeilTransportError("Full Euler source is not absolutely convergent here")
    return mp.power(N,1-sig)*(mp.log(N)/(sig-1)+1/(sig-1)**2)


def completed_xi(s):
    mp=_mp(); ss=_complex_arg(s)
    if ss.real<=1:raise WeilTransportError("This source oracle is only defined for Re(s)>1")
    return ss*(ss-1)*heat_mellin_normalization(ss)*mp.zeta(ss)/2


def complete_logderivative_from_heat(s,N:int):
    """2 xi'/xi from pole+Gamma - (finite heat Mellin/Gamma), Re(s)>1.

    Complete identity only after N->infty with proved prime-tail bound.
    This is NOT Gamma_R(s)*(-zeta'/zeta)(s); normalization is essential.
    """
    mp=_mp(); ss=_complex_arg(s)
    if ss.real<=1:raise WeilTransportError("Pole/Euler logarithmic-source domain Re(s)>1")
    return 2/ss+2/(ss-1)+mp.digamma(ss/2)-mp.log(mp.pi)-2*heat_mellin_prime_fraction(ss,N)


def independent_xi_logderivative(s):
    """Independent zero-free-input calibration using direct ζ'/ζ (not prime tape)."""
    mp=_mp();ss=_complex_arg(s)
    if ss.real<=1:raise WeilTransportError("Independent oracle restricted to Re(s)>1")
    return 2/ss+2/(ss-1)+mp.digamma(ss/2)-mp.log(mp.pi)+2*mp.diff(mp.zeta,ss)/mp.zeta(ss)


def arch_spectral_symbol(u, *,conductor:int=1, parity:int=0):
    """Ω_(q,ε)(u)=log(q/π)+Re ψ(1/4+ε/2+iu/2)."""
    mp=_mp();_integer(conductor,1)
    if type(parity) is not int or parity not in (0,1):
        raise WeilTransportError("Declared parity ε=0 or 1")
    uu=_number(u)
    return mp.log(conductor/mp.pi)+mp.re(mp.digamma(mp.mpf(1)/4+mp.mpf(parity)/2+1j*uu/2))


def arch_real_kernel(x):
    """e^(-x/2)/(1-e^(-2x)); x>0, positive but NOT a Weil PSD form."""
    mp=_mp();xx=_number(x)
    if xx<=0:raise WeilTransportError("Arch kernel is defined for x>0")
    return mp.exp(-xx/2)/(-mp.expm1(-2*xx))


def arch_contact():
    mp=_mp()
    return -(mp.euler+mp.log(4*mp.pi))


def arch_renorm_density(h:Callable,h0,x):
    """D_h(x)=h(x)+h(-x)-2 exp(-x/2) h(0), stable at x~0."""
    mp=_mp(); xx=_number(x)
    if xx<0:raise WeilTransportError("Arch density uses positive x")
    return (h(xx)+h(-xx)-2*h0)-2*h0*mp.expm1(-xx/2)


def arch_integrand(h,h0,x):
    mp=_mp();xx=_number(x)
    if xx<0:raise WeilTransportError("Arch density uses positive x")
    if xx==0:
        return h0/2   # C^2 cancellation, h(x)+h(-x) symmetric
    return arch_real_kernel(xx)*arch_renorm_density(h,h0,xx)


def arch_ladder_integrand(h,h0,x,J:int):
    """Sum_{j=0}^{J-1} e^(-(2j+1/2)x) D_h(x), finite and nonsingular."""
    mp=_mp(); _integer(J,1);xx=_number(x)
    if xx<0:raise WeilTransportError("x>=0 required")
    if xx==0:return mp.mpf(0)
    geometric=(-mp.expm1(-2*J*xx))/(-mp.expm1(-2*xx))
    return mp.exp(-xx/2)*geometric*arch_renorm_density(h,h0,xx)


def arch_ladder_remainder_bound(C:int|Fraction,J:int)->Fraction:
    """Universal C^2 bound if |D_h(x)|<=C*x for x>=0.

    |A(h)-A_J(h)| <= C * (1/(2a)+1/a^2), a=2J+1/2.
    Source: (1-e^-2x)^-1 <= 1+1/(2x), x>0.
    """
    cc=_rational(C);_integer(J,1)
    if cc<0:raise WeilTransportError("Cannot certify with negative norm envelope")
    a=Fraction(4*J+1,2)
    return cc*(1/(2*a)+1/a**2)


def accelerated_arch_c2_remainder_bound(h0_bound, h2_sup, J:int)->Fraction:
    """Rigorous O(J^-2) renormalized gamma-ladder bound on C_c^2 tests.

    Define a=2J+1/2, A_J=arch contact - first J Gamma rungs.
    Improved Atilde_J=A_J - h(0)/(2a).  Then
      |A-Atilde_J| <= |h0|/a^2 + (M2+|h0|/4)*(1/(2a^2)+2/a^3).
    Proof: |D_h(x)-h0*x| <= (M2+|h0|/4)*x^2 and
    0<=x/(1-e^-2x)-1/2<=x, x^2/(1-e^-2x)<=x^2+x/2.
    All inputs are exact rationals, never a numerical quadrature bound.
    """
    h0=_rational(h0_bound);M2=_rational(h2_sup);_integer(J,1)
    if h0<0 or M2<0:raise WeilTransportError("Supremum bounds must be nonnegative")
    a=Fraction(4*J+1,2)
    return h0/a**2 + (M2+h0/4)*(Fraction(1,2)/a**2+2/a**3)


def renormalized_arch_ladder(arch_J,h0,J:int):
    """Subtract universal contact h(0)/(4J+1) from a J-rung arch form."""
    _integer(J,1)
    return arch_J - h0/(4*J+1)


def sobolev_operator_ladder_bound(J:int,*,accelerated:bool=True)->Fraction:
    """Uniform signed Q^(J)->Q bound in H^1_0 window, not positivity.

    If h=v*tilde(w): |h0|<=||v||2||w||2,
    ||h||inf<=||v||2||w||2, ||h''||inf<=||v'||2||w'||2.
    Hence |(Q-Q_J)(v,w)|<=eps_J||v||H1||w||H1,
    and likewise for corrected Qtilde_J at O(J^-2).
    """
    _integer(J,1)
    a=Fraction(4*J+1,2)
    if accelerated:
        # coefficient on V L2 product, derivative H1 product
        first=1/a**2 + Fraction(1,4)*(Fraction(1,2)/a**2+2/a**3)
        second=Fraction(1,2)/a**2+2/a**3
        return max(first,second)
    return 4*(1/(2*a)+1/a**2)


def arch_c2_envelope(h0_bound, h_sup, h2_sup)->Fraction:
    """Certified C for every C_c^2 h with supplied genuine global sup bounds.

    For x<=1: D(x)<= x(|h(0)| + ||h''||inf).
    For x>=1: D(x)<=x[2||h||inf+2|h(0)|].
    """
    h0=_rational(h0_bound);v=_rational(h_sup);w=_rational(h2_sup)
    if min(h0,v,w)<0:raise WeilTransportError("Nonnegative norm bounds only")
    return max(h0+w,2*(v+h0))


def compact_arch(h,h0,partition:list,*,J:int|None=None,dps:int=45):
    """Numerical quadrature of exact compact-test Archimedean functional.

    Not an interval-certified quadrature: rigorous Arch ladder tail is
    independently available from arch_ladder_remainder_bound.
    """
    mp=_mp();mp.mp.dps=dps
    if len(partition)<2 or partition[0]!=0 or any(partition[i+1]<=partition[i] for i in range(len(partition)-1)):
        raise WeilTransportError("Increasing knots beginning at 0 required")
    if J is not None:_integer(J,1)
    fn=(lambda x:arch_integrand(h,h0,x)) if J is None else (lambda x:arch_ladder_integrand(h,h0,x,J))
    intervals=[_number(x) for x in partition]+[mp.inf]
    val=mp.fsum(mp.quad(fn,[intervals[i],intervals[i+1]]) for i in range(len(intervals)-1))
    return arch_contact()*h0-val


def tent_convolution(t,a):
    """Autocorrelation of f(x)=(1-|x|/a)_+: compact C^2 cubic B-spline.

    Formula exact in terms of a,|t|, not numeric convolution.
    """
    mp=_mp();aa=_number(a);xx=abs(_number(t))
    if aa<=0:raise WeilTransportError("Positive half-support a required")
    if xx>=2*aa:return mp.mpf(0)
    if xx<=aa:return 2*aa/3-xx*xx/aa+xx**3/(2*aa**2)
    return (2*aa-xx)**3/(6*aa**2)


def tent_bounds(a:int|Fraction)->tuple[Fraction,Fraction,Fraction,Fraction]:
    """(h0,||h||inf,||h''||inf,C) exact for B-spline tent correlation."""
    aa=_rational(a)
    if aa<=0:raise WeilTransportError("Positive rational width")
    h0=2*aa/3
    hsup=h0
    h2=2/aa
    return h0,hsup,h2,arch_c2_envelope(h0,hsup,h2)


def compact_weil_tent(a:int|Fraction,J:int=20,*,fake6:int|Fraction=0,half_density:Fraction=Fraction(1,2),omit_poles:bool=False,dps:int=45)->dict:
    """Source-complete compact C^2 Weil functional on tent autocorrelation.

    Exact arithmetic SUPPORT cutoff: only log(n) < 2a enter. Arch term
    approximated by first J rungs; an independent *proved* absolute tail
    bound accompanies the numeric evaluation.  This does NOT assert sign.
    """
    mp=_mp();mp.mp.dps=dps;aa=_rational(a);_integer(J,1)
    if aa<=0 or aa>4:raise WeilTransportError("Finite tent benchmark 0<a<=4")
    mut=_rational(fake6);hd=_rational(half_density)
    if hd<0:raise WeilTransportError("Declared nonnegative half-density exponent")
    h=lambda x:tent_convolution(x,aa)
    hh0,hsup,h2,C=tent_bounds(aa)
    h0=_number(hh0);R=2*_number(aa)
    pole=mp.mpf(0) if omit_poles else 2*mp.quad(lambda x:h(x)*(mp.exp(x/2)+mp.exp(-x/2)),[0,_number(aa),R])
    maxn=max(2,int(mp.floor(mp.exp(R)))+1)
    if maxn>200_000:raise WeilTransportError("Unexpected prime cutoff")
    used=[]
    prime_val=mp.mpf(0)
    for n,p in von_mangoldt_labels(maxn):
        if mp.log(n)>=R:continue
        impulse=-2*mp.log(p)*mp.power(n,-_number(hd))*h(mp.log(n))
        if impulse:used.append(n)
        prime_val+=impulse
    if mut:
        prime_val+=-2*_number(mut)*mp.log(6)*mp.power(6,-_number(hd))*h(mp.log(6))
    arch=compact_arch(h,h0,[0,_number(aa),R],J=J,dps=dps)
    bound=_number(arch_ladder_remainder_bound(C,J))
    return {'pole':pole,'prime':prime_val,'arch_ladder':arch,'q_ladder':pole+prime_val+arch,
            'error_bound':bound,'prime_support':tuple(used),'max_radix':maxn,
            'genuine':mut==0 and hd==Fraction(1,2) and not omit_poles,'h0':h0,
            'C_envelope':C}


def arch_exponential_resolvent(s,*,conductor:int=1,parity:int=0):
    """Arch pairing on h_a=e^-a|x|, a=s-1/2>1/2.

    A_(q,eps)(h_a) = psi((s+eps)/2)+log(q/pi), direct Poisson
    evaluation of Omega_(q,eps). This is an analytic extension beyond Cc2.
    """
    mp=_mp();ss=_number(s)
    _integer(conductor,1)
    if type(parity) is not int or parity not in (0,1):raise WeilTransportError("Parity 0 or 1")
    if ss<=1:raise WeilTransportError("Resolvent requires s>1 for full source")
    return mp.digamma((ss+parity)/2)+mp.log(conductor/mp.pi)


def arch_resolvent_integral(s,dps:int=45):
    """Independent renormalized geometric-arch evaluation, a=s-1/2>1/2."""
    mp=_mp();mp.mp.dps=dps;ss=_number(s)
    if ss<=1:raise WeilTransportError("Resolvent s>1")
    def f(x):
        if x==0:return ss-1  # 2*(s-1)*x / (2*x) = s-1
        return 2*mp.exp(-x)*(-mp.expm1(-(ss-1)*x))/(-mp.expm1(-2*x))
    return arch_contact()+mp.quad(f,[0,1,mp.inf])


def arch_resolvent_ladder(s,J:int,dps:int=45):
    """Finite exp ladder, h_a(x)=exp(-(s-1/2)|x|), including its contact."""
    mp=_mp();mp.mp.dps=dps;ss=_number(s);_integer(J,1)
    if ss<=1:raise WeilTransportError("Resolvent s>1")
    # D=2 (e^{-(s-1/2)x}-e^-x/2); exact rung integrals.
    return arch_contact()-2*mp.fsum(1/(2*j+ss)-1/(2*j+1) for j in range(J))


def arch_resolvent_ladder_error(s,J:int):
    """Exact sign/tail: A-A_J=2 int (e^-x-e^-s x) e^-2Jx /(1-e^-2x).

    For s>1, integral positive and <= (s-1)/(2J) by the elementary
    estimates 1-e^{-(s-1)x}<=(s-1)x, (1-e^-2x)^-1<=1+1/(2x),
    and separate integrals. Here a slightly looser explicit bound is used.
    """
    mp=_mp();ss=_number(s);_integer(J,1)
    if ss<=1:raise WeilTransportError("Resolvent s>1")
    # Tail = 2 sum_{j>=J} (1/(2j+1)-1/(2j+s)).
    # Each integrand <= 2(s-1) x e^{-(2J+1)x}/(1-e^-2x).
    # <= (s-1) [ 1/(2J+1) + 2/(2J+1)^2 ].
    L=2*J+1
    return (ss-1)*(1/L+2/(L*L))


def pole_resolvent(s):
    mp=_mp();ss=_number(s)
    if ss<=1:raise WeilTransportError("Pole pairing requires s>1")
    return 2/ss+2/(ss-1)


def fake_composite6_resolvent_defect(s, *,delta:int|Fraction=1):
    """Exact extra connected log coefficient b(6)=delta, at half-density 1/2."""
    mp=_mp();ss=_number(s);d=_rational(delta)
    if ss<=1:raise WeilTransportError("Full resolvent s>1")
    return -2*_number(d)*mp.log(6)*mp.power(6,-ss)


def half_density_mutation_defect(s,N:int,exponent:int|Fraction):
    """Difference in source prime pairing from replacing n^-1/2 by n^-exponent.

    h_a(log n)=n^-(s-1/2); correct exponent gives n^-s.
    """
    mp=_mp();ss=_number(s);h=_rational(exponent)
    if ss<=1:raise WeilTransportError("Convergent source s>1")
    a=ss-mp.mpf('0.5')
    return -2*mp.fsum(mp.log(p)*(mp.power(n,-a-_number(h))-mp.power(n,-ss)) for n,p in von_mangoldt_labels(N))


def source_laplace_injective_scope(sigma):
    """Check the domain of the PROVED map: e^-sigma*x nu is finite for σ>1.

    Proof in dossier: Mellin heat -> Gamma_R*Laplace(nu); Fourier
    uniqueness on fixed vertical line identifies the atomic measure.
    The checker never treats a finite list of samples as full uniqueness.
    """
    s=_rational(sigma)
    if s<=1:raise WeilTransportError("Weighted true-prime measure finite only for sigma>1")
    return {'sigma':s,'holomorphic_halfplane':'Re(s)>1',
            'finite_evidence_sufficient':False,
            'full_vertical_line_uniqueness':'classical Fourier uniqueness'}


def arch_resolvent_fourier(s,dps:int=40):
    """Independent Cauchy/Fourier symbol route on h_a=e^-a|x|.

    Fourier h_a(u)=2a/(a^2+u^2), a=s-1/2>1/2.  The integral is
    evaluated NUMERICALLY; its equality with digamma is a classical
    right-half-plane Poisson integral, not a finite computation theorem.
    """
    mp=_mp();mp.mp.dps=dps;ss=_number(s)
    if ss<=1:raise WeilTransportError("s>1")
    a=ss-mp.mpf('0.5')
    f=lambda u:(2*a/mp.pi)*(mp.re(mp.digamma(mp.mpf('0.25')+1j*u/2))-mp.log(mp.pi))/(a*a+u*u)
    return mp.quad(f,[0,1,5,20,100,mp.inf])


def halfdensity_mellin_tent(a,u,*,offset:int|Fraction=0,dps:int=40):
    """Direct multiplicative test ∫ F(x)x^(s-1)dx at s=1/2+iu.

    F(x)=x^(-1/2+offset) (1-|log(x)|/a)_+; the correct offset=0
    transports to Fourier transform of the additive tent.  Nonzero
    offset is a deliberate wrong-half-density mutation.
    """
    mp=_mp();mp.mp.dps=dps
    aa=_number(a);nu=_number(u);off=_rational(offset)
    if aa<=0:raise WeilTransportError("a>0")
    f=lambda x:mp.power(x,-mp.mpf('0.5')+_number(off))*max(mp.mpf(0),1-abs(mp.log(x))/aa)*mp.power(x,-mp.mpf('0.5')+1j*nu)
    return mp.quad(f,[mp.exp(-aa),1,mp.exp(aa)])


def additive_tent_fourier(a,u):
    mp=_mp(); aa=_number(a);nu=_number(u)
    if aa<=0:raise WeilTransportError("a>0")
    z=aa*nu/2
    if z==0:return aa
    return aa*(mp.sin(z)/z)**2


def arch_spectral_tent_numeric(a,*,cutoff=160,dps:int=35):
    """Independent truncated Fourier integral for compact tent correlation.

    It is DIAGNOSTIC only; omitted u>cutoff tail is not rigorously
    bounded by this routine.  Unlike geometric arch ladder, it cannot
    certify a sign or an interval.
    """
    mp=_mp();mp.mp.dps=dps;aa=_number(a);T=_number(cutoff)
    if aa<=0 or T<=0:raise WeilTransportError("Positive width and finite cutoff")
    f=lambda u:(additive_tent_fourier(aa,u)**2)*(mp.re(mp.digamma(mp.mpf('0.25')+1j*u/2))-mp.log(mp.pi))/mp.pi
    knots=[mp.mpf(0),mp.mpf(1),mp.mpf(4),mp.mpf(16),T]
    knots=sorted(set(x for x in knots if x<=T))
    return mp.fsum(mp.quad(f,[knots[i],knots[i+1]]) for i in range(len(knots)-1))


def arch_spectral_parity_conductor_resolvent(s,q:int,eps:int,dps:int=40):
    """Independent Fourier/Poisson evaluation on h_a for q,epsilon source."""
    mp=_mp();mp.mp.dps=dps;ss=_number(s);_integer(q,1)
    if ss<=1:raise WeilTransportError("s>1")
    if type(eps) is not int or eps not in (0,1):raise WeilTransportError("Parity 0/1")
    a=ss-mp.mpf('0.5')
    f=lambda u:(2*a/mp.pi)*arch_spectral_symbol(u,conductor=q,parity=eps)/(a*a+u*u)
    return mp.quad(f,[0,1,5,20,100,mp.inf])


def screw_rung_integral(R,j:int):
    """Exact elementary integral ∫[(R-x)_+-R e^-x/2] e^-(2j+1/2)x dx."""
    mp=_mp();rr=_number(R);_integer(j)
    if rr<0:raise WeilTransportError("Nonnegative screw radius")
    if rr==0:return mp.mpf(0)
    a=2*j+mp.mpf('0.5')
    return rr/a+mp.expm1(-a*rr)/a**2-rr/(a+mp.mpf('0.5'))


def screw_potential_J(R,J:int,*,fake6:int|Fraction=0,dps:int=45):
    """A ZERO-READING, source-derived finite Suzuki/Weil screw potential.

    Psi_J(R) = (1/2) W_J(x->(R-|x|)_+), even extended in R.
    Its *distributional* second derivative converges to completed W.
    This is signed; no positive kernel is claimed.  The exact missing
    J-infinity tail is bounded by screw_potential_remainder_bound.
    """
    mp=_mp();mp.mp.dps=dps;rr=_number(R);_integer(J,1)
    if rr<0:raise WeilTransportError("R>=0")
    if rr==0:return mp.mpf(0)
    if rr>10:raise WeilTransportError("Bounded numerical source radius R<=10")
    fake=_rational(fake6)
    limit=int(mp.floor(mp.exp(rr)))+1
    if limit>200_000:raise WeilTransportError("Prime-source budget exceeded")
    P=8*(mp.cosh(rr/2)-1)
    source=mp.fsum(mp.log(p)*mp.power(n,-mp.mpf('0.5'))*max(mp.mpf(0),rr-mp.log(n)) for n,p in von_mangoldt_labels(limit))
    if fake:
        source+=_number(fake)*mp.log(6)*mp.power(6,-mp.mpf('0.5'))*max(mp.mpf(0),rr-mp.log(6))
    ladder=mp.fsum(screw_rung_integral(rr,j) for j in range(J))
    return P-source+arch_contact()*rr/2-ladder


def screw_potential_remainder_bound(R:int|Fraction,J:int)->Fraction:
    """Universal O(1/J) error on the source-derived *screw potential*.

    For E_R(x)=(R-x)_+-R e^-x/2, |E_R(x)|<=(1+R/2)*x.
    Thus |Psi(R)-Psi_J(R)| <= (1+R/2)(1/(2a)+1/a^2),
    with a=2J+1/2.  Exact rationals in R and J.
    """
    r=_rational(R);_integer(J,1)
    if r<0:raise WeilTransportError("R>=0")
    a=Fraction(4*J+1,2)
    return (1+r/2)*(1/(2*a)+1/a**2)


def screw_potential_full_integral(R,*,fake6:int|Fraction=0,dps:int=45):
    """Independent NUMERICAL real-space completion of the signed screw source."""
    mp=_mp();mp.mp.dps=dps;rr=_number(R)
    if rr<0 or rr>8:raise WeilTransportError("R in [0,8]")
    if rr==0:return mp.mpf(0)
    source=mp.fsum(mp.log(p)*mp.power(n,-mp.mpf('0.5'))*max(mp.mpf(0),rr-mp.log(n)) for n,p in von_mangoldt_labels(int(mp.floor(mp.exp(rr)))+1))
    fake=_rational(fake6)
    source+=_number(fake)*mp.log(6)*mp.power(6,-mp.mpf('0.5'))*max(mp.mpf(0),rr-mp.log(6))
    def arch_fn(x):
        if x==0:return rr/4-mp.mpf('0.5')
        E=rr*(-mp.expm1(-x/2))-x if x<rr else -rr*mp.exp(-x/2)
        return E*arch_real_kernel(x)
    integral=mp.quad(arch_fn,[0,rr,mp.inf])
    return 8*(mp.cosh(rr/2)-1)-source+arch_contact()*rr/2-integral


def screw_regular_density(R,J:int|None=None):
    """Away from prime-power atoms and 0, Psi'' regular density.

    Psi''(R)=e^(R/2)+e^(-R/2)-sum_j exp(-(2j+1/2)R).
    At R=log n, the full DISTRIBUTION has an extra -Lambda(n)/sqrt(n)
    atom, which this regular-density API must not hide.
    """
    mp=_mp();r=_number(R)
    if r<=0:raise WeilTransportError("R>0 away from origin only")
    if r>10:raise WeilTransportError("Finite source radius guard")
    for n,p in von_mangoldt_labels(int(mp.floor(mp.exp(r)))+2):
        if abs(r-mp.log(n))<mp.mpf('1e-20'):
            raise WeilTransportError("Prime-power atom: regular density undefined")
    if J is None:
        return 2*mp.cosh(r/2)-arch_real_kernel(r)
    _integer(J,1)
    return 2*mp.cosh(r/2)-mp.fsum(mp.exp(-(2*j+mp.mpf('0.5'))*r) for j in range(J))


def screw_kernel_J(t,u,J:int,*,fake6:int|Fraction=0,dps:int=45):
    """Source-first finite kernel K(t,u)=Psi(t)+Psi(u)-Psi(t-u).

    This is the *signed* Suzuki-type covariance kernel; K(t,0)=0.
    It is NOT declared positive semidefinite, even though exponentials
    and Gaussian heat in the source construction are positive.
    """
    mp=_mp();tt=_number(t);uu=_number(u)
    return (screw_potential_J(abs(tt),J,fake6=fake6,dps=dps)+
            screw_potential_J(abs(uu),J,fake6=fake6,dps=dps)-
            screw_potential_J(abs(tt-uu),J,fake6=fake6,dps=dps))


def fake6_positive_dirichlet_coefficient(n:int,delta:int|Fraction=1000)->Fraction:
    """All-positive fake Dirichlet source a=ζ * exp_*(delta delta_6).

    a(n)=sum_{0<=j<=min(v_2(n),v_3(n))} delta^j/j! for n>=1.
    Thus a(2)=a(3)=1, but a(6)=1+delta: Euler multiplicativity fails.
    A genuinely nonnegative arithmetic tape does NOT confer Weil positivity.
    """
    from math import factorial
    _integer(n,1)
    d=_rational(delta)
    if d<0:raise WeilTransportError("This control certifies positive coefficients only")
    r=n; v=[]
    for p in (2,3):
        count=0;z=r
        while z%p==0:
            z//=p;count+=1
        v.append(count)
    return sum((d**j/factorial(j) for j in range(min(v)+1)),Fraction(0))


def fake6_negative_screw_certificate(delta:int|Fraction=1000)->Fraction:
    """Source-first ANALYTIC upper bound Psi_fake(2) < 17-delta/30.

    Proof (in dossier): 8(cosh(1)-1)<8, all true-prime and contact
    terms are nonpositive at R=2, and |arch screw|<9 because
    |E_2(x)|<=2x, sum_j(2j+1/2)^-2 < 4+pi^2/24 < 4.5.
    Also 1<log6<19/10, sqrt6<3, so fake6 changes Psi(2) by
    -delta log6/sqrt6*(2-log6) < -delta/30.
    The returned RATIONAL number is a strict mathematical upper bound,
    not an interval from a floating-point screw computation.
    """
    d=_rational(delta)
    if d<0:raise WeilTransportError("Positive impulse mutant only")
    return Fraction(17)-d/30


def fake6_reflection_log_defect(s:int,delta:int|Fraction=1000)->Fraction:
    """Functional-equation debt for xi_fake=xi*exp(delta*6^(-s)).

    ξ(s)=ξ(1-s) for the AUTHENTIC ζ completion.  exp(delta*6^-s)
    has no zeros, but its factor changes the ratio by
      exp(delta*(6^-s - 6^(s-1))).
    At integer s the logarithmic defect is EXACT RATIONAL, nonzero
    when δ!=0 and s !=1/2.  Thus same zero divisor does not imply
    the signed fake source is a legitimate completed Weil formula.
    """
    _integer(s,0)
    d=_rational(delta)
    return d*(Fraction(6)**(-s)-Fraction(6)**(s-1))
