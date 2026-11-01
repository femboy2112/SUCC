"""Source-faithful rational SUCC unit path / Hausdorff-Newton seam laboratory.

Scope: exact finite Q arithmetic and combinatorial finite transformations only.
All analytic continuation/asymptotics live in the accompanying paper proof.
Does not prove any signed Weyl saving, pi normality, or RH.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from typing import Sequence


def _nonnegative(k: int) -> None:
    if type(k) is not int or k < 0:
        raise ValueError("Nonnegative exact integer required")


def bbp_source(n: int | F) -> F:
    """Authentic four signed poles, real/rational domain n>=1."""
    x = F(n)
    if x < 1:
        raise ValueError("Original source domain n>=1")
    return F(4)/(8*x-7) - F(2)/(8*x-4) - F(1)/(8*x-3) - F(1)/(8*x-2)


def bbp_source_combined(n: int | F) -> F:
    """Independent original numerator / denominator algebra."""
    x=F(n)
    if x<1: raise ValueError("Original source n>=1")
    return (120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))


def beta_rational(a: F, k: int) -> F:
    """B(a,k+1) by the Gamma factorial ratio at positive rational a."""
    _nonnegative(k)
    a=F(a)
    if a<=0: raise ValueError("positive beta parameter required")
    denominator=F(1)
    for j in range(k+1): denominator*=a+j
    return F(factorial(k),1)/denominator


def source_newton(k: int) -> F:
    """a_k=(-1)^k Delta^k r(1): exact unit-SUCC finite difference."""
    _nonnegative(k)
    return sum(((-1)**j*comb(k,j)*bbp_source(j+1) for j in range(k+1)),F())


def source_newton_beta(k: int) -> F:
    """Independent positive Mellin/Beta formula for the SAME a_k."""
    _nonnegative(k)
    return (4*beta_rational(F(1,8),k)-2*beta_rational(F(1,2),k)
            -beta_rational(F(5,8),k)-beta_rational(F(3,4),k))/8


def reconstruct_source_at(n: int, coefficient_source=source_newton_beta) -> F:
    """Finite Pascal inversion for integer n>=1; no infinite sum."""
    if type(n) is not int or n<1: raise ValueError("n must be positive integer")
    return sum(((-1)**k*comb(n-1,k)*coefficient_source(k) for k in range(n)),F())


def extruded_pascal_row(n: int) -> tuple[int,...]:
    """C_{n,k}=sum_{j=k}^{n-1}16^(n-1-j)*choose(j,k), n>=1."""
    if type(n) is not int or n<1: raise ValueError("positive row index required")
    return tuple(sum(16**(n-1-j)*comb(j,k) for j in range(k,n))
                 for k in range(n))


def bbp_state(n: int) -> F:
    """Exact canonical zero-seeded state."""
    _nonnegative(n)
    u=F()
    for j in range(1,n+1): u=16*u+bbp_source(j)
    return u


def extruded_state(n:int) -> F:
    """BBP state by unimodular Pascal/radix16 extrusion over unit jets."""
    _nonnegative(n)
    if n==0:return F()
    row=extruded_pascal_row(n)
    return sum(((-1)**k*row[k]*source_newton_beta(k) for k in range(n)),F())


def tau_partial(k:int, terms:int) -> F:
    """Rational approximation of tau_k=(-1)^k Delta^k T(0)."""
    _nonnegative(k)
    if type(terms) is not int or terms<1:raise ValueError("positive term count")
    return sum((F((-1)**j,15**(j+1))*source_newton_beta(k+j)
                for j in range(terms)),F())


def tau_interval(k:int, terms:int) -> tuple[F,F]:
    """Exact enclosing interval via strictly signed geometric remainder."""
    p=tau_partial(k,terms)
    # R= (-1)^J*integral (1-u)^(k+J) / [15^J*(16-u)] dmu.
    # 15<=16-u<=16, so strict interval between a_{k+J}/(16*15^J)
    # and a_{k+J}/(15*15^J). Keep the easier enclosing bounds.
    rad=source_newton_beta(k+terms)/15**(terms+1)
    return (p,p+rad) if terms%2==0 else (p-rad,p)


def pi_interval(terms:int) -> tuple[F,F]:
    a,b=tau_interval(0,terms)
    return 16*a,16*b


def completed_alpha_shadow(terms:int) -> F:
    """Finite rational unit-jet shadow of the original pi/16 boundary."""
    return tau_partial(0,terms)


def certified_radix_shadow_weyl_budget(h:int,horizon:int,jet_depth:int) -> F:
    """Exact rational upper bound for full selected-circle Weyl shadow defect.

    |sum_{1<=n<=M} e(h*16^n*pi/16) - sum e(h*16^n*alpha_J)|
      <= 2*pi*|h|*sum 16^n * |alpha-alpha_J|,
    pi<22/7 and |alpha-alpha_J|<a_J/15^(J+1).

    This certifies TRANSPORT only, NOT Fourier cancellation.
    """
    if type(h) is not int or h==0 or type(horizon) is not int or horizon<1:
        raise ValueError("fixed nonzero integer harmonic and positive horizon")
    if type(jet_depth) is not int or jet_depth<1:
        raise ValueError("positive exact jet depth")
    return (F(44,7)*abs(h)*source_newton_beta(jet_depth)
            *16*(16**horizon-1)/15**(jet_depth+2))


def shadow_double_depth_envelope(h:int,horizon:int) -> F:
    """Simple explicit exponential envelope C_h*(16/225)^M for J=2M."""
    if type(h) is not int or h==0 or type(horizon) is not int or horizon<1:
        raise ValueError("positive horizon and nonzero frequency")
    return F(33088,23625)*abs(h)*F(16,225)**horizon


def beta_newton_tail_residual(k:int,terms:int) -> F:
    """Exact residual 15*tau_(k,J)+tau_(k+1,J)-a_k."""
    return 15*tau_partial(k,terms)+tau_partial(k+1,terms)-source_newton_beta(k)


def finite_beta_residual(k:int,terms:int) -> F:
    """Closed exact finite cutoff remainder of the 15 tau + shift equation."""
    return F((-1)**(terms-1),15**terms)*source_newton_beta(k+terms)


def _mul(p: Sequence[int],q:Sequence[int]) -> tuple[int,...]:
    v=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):v[i+j]+=a*b
    return tuple(v)


def dilation_polynomial(m:int,k:int) -> tuple[int,...]:
    """Coefficients of [1-(1-v)^m]^k, exact signed integer Pascal polynomial."""
    if type(m) is not int or m<1:raise ValueError("positive integral dilation")
    _nonnegative(k)
    p=tuple([0]+[(-1)**(j+1)*comb(m,j) for j in range(1,m+1)])
    out=(1,)
    for _ in range(k):out=_mul(out,p)
    return out


def dilate_moments(c:Sequence[F],m:int,k:int) -> F:
    p=dilation_polynomial(m,k)
    if len(c)<len(p):raise ValueError("insufficient unit-succ jet depth")
    return sum((F(q)*c[i] for i,q in enumerate(p)),F())


def shifted_moment(c:Sequence[F],k:int,m:int=1) -> F:
    """Coefficient of x->x+m: (-1)^k Delta^k(S^m f)(0)."""
    if type(m) is not int or m<0:raise ValueError("nonnegative shift")
    _nonnegative(k)
    if len(c)<k+m+1:raise ValueError("insufficient jet depth for shift")
    return sum((F((-1)**j*comb(m,j))*c[k+j] for j in range(m+1)),F())


def check_pullback_diamond(c:Sequence[F],m:int,k:int) -> bool:
    """(S V_m)= (V_m S^m) on the FULL moment tower, not a shallow truncation."""
    left=dilate_moments(c,m,k)-dilate_moments(c,m,k+1)
    p=dilation_polynomial(m,k)
    right=sum((F(q)*shifted_moment(c,j,m) for j,q in enumerate(p)),F())
    return left==right


@dataclass(frozen=True)
class PathWitness:
    """Ordered words are remembered even if affine endpoints coincide."""
    operations: tuple[tuple[str,int|F],...]

    def __post_init__(self):
        for name,a in self.operations:
            if name=='S':
                if a!=1:raise ValueError("Primitive S has unit step exactly 1")
            elif name=='V':
                if type(a) is not int or a<1:raise ValueError("V requires positive integer")
            elif name=='T':
                if not isinstance(a,(int,F)) or F(a).denominator==1:
                    raise ValueError("T is a declared NONINTEGRAL rational localized shift")
            else:raise ValueError("Unknown path generator")

    def evaluate(self, initial:int|F=0)->tuple[F,tuple[F,...]]:
        x=F(initial);hist=[x]
        for name,a in self.operations:
            if name=='S':x+=1
            elif name=='V':x*=a
            else:x+=F(a)
            hist.append(x)
        return x,tuple(hist)

    def affine_normal_form(self)->tuple[F,int]:
        """x -> m x + a. Source history is intentionally NOT erased in this object."""
        a=F();m=1
        for name,n in self.operations:
            if name=='S':a+=1
            elif name=='T':a+=F(n)
            else:a*=n;m*=n
        return a,m

    def path_charge(self, initial:int|F=0)->F:
        """Toy non-source edge cochain; diagnostic only, NOT authenticated BBP phase."""
        x=F(initial);charge=F()
        for name,a in self.operations:
            if name=='S': charge+=x/F(5);x+=1
            elif name=='V':x*=a
            else:x+=F(a)
        return charge%1


def shape_factorizes(fibers:Sequence[Sequence[int]],target:Sequence[str]) -> bool:
    """Necessary/sufficient finite observer quotient adequacy criterion."""
    for fiber in fibers:
        if len({target[i] for i in fiber})>1:return False
    return True


def witness_finite_jet_alias(m:int)->dict:
    """Two positive probability measures sharing jets <m, differing at V_m jet1."""
    if type(m) is not int or not 2<=m<=30:raise ValueError("bounded dilation >=2")
    v=[F(j,m) for j in range(m+1)]
    base=[F(comb(m,j),2**m) for j in range(m+1)]
    nu=[F((-1)**(m-j)*comb(m,j),2**m) for j in range(m+1)]
    up=[base[j]+nu[j]/2 for j in range(m+1)]
    down=[base[j]-nu[j]/2 for j in range(m+1)]
    assert min(up)>0 and min(down)>0 and sum(up)==sum(down)==1
    moments_up=[sum((up[j]*v[j]**k for j in range(m+1)),F()) for k in range(m+1)]
    moments_down=[sum((down[j]*v[j]**k for j in range(m+1)),F()) for k in range(m+1)]
    ups=dilate_moments(moments_up,m,1)
    downs=dilate_moments(moments_down,m,1)
    assert moments_up[:m]==moments_down[:m] and ups!=downs
    return {"m":m,"same_jets":m,"moment_m_difference":moments_up[m]-moments_down[m],
            "dilated_first_jet_difference":ups-downs,
            "positive":True}


def multiply_golden_unit(z:tuple[int,int])->tuple[int,int]:
    """Exact Z[phi] multiplication by phi in basis (1,phi), phi²=phi+1.

    Separate Pisot carrier example, NOT an authenticated BBP operation.
    """
    if (not isinstance(z,tuple) or len(z)!=2 or
            any(type(t) is not int for t in z)):
        raise ValueError("two integral coefficients in Z[phi] required")
    a,b=z
    return b,a+b


def golden_successor(z:tuple[int,int],axis:str)->tuple[int,int]:
    """Two distinct coloured unit generators 1 and phi."""
    if (not isinstance(z,tuple) or len(z)!=2 or
            any(type(t) is not int for t in z)):
        raise ValueError("two integral coordinates required")
    a,b=z
    if axis=='1':return a+1,b
    if axis=='phi':return a,b+1
    raise ValueError("Unknown SUCC unit basis")
