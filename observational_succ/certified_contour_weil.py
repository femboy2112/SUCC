"""Exact rational polygonal argument-principle certificates from authenticated theta jets.

Requires the immutable PR #78 source receipt (Git blob SHA verified) for ξ claims.
No zero coordinates or black-box zeta evaluations are used in certification.
The separate Suzuki/Weil transport remains an imported explicit-formula identity.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path


class ContourError(ValueError):
    pass


THETA_RECEIPT_BLOB = '2657d92f15fcd77e2232f2cf305561a090ff28ce'
THETA_RECEIPT_PATH = 'research/2026-10-14/THETA_EVEN_JETS_RECEIPT.json'


def exact(x):
    if type(x) is int or type(x) is Q:
        return Q(x)
    if type(x) is str:
        return Q(x)
    raise ContourError('exact int/Fraction/string required; floats not admitted')


@dataclass(frozen=True)
class C:
    re: Q
    im: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 're', exact(self.re))
        object.__setattr__(self, 'im', exact(self.im))

    def __add__(self, other):
        other = cq(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-cq(other))

    def __mul__(self, other):
        other = cq(other)
        return C(self.re*other.re - self.im*other.im,
                 self.re*other.im + self.im*other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = cq(other)
        d = other.norm2()
        if d == 0:
            raise ZeroDivisionError('complex rational division by zero')
        return C((self.re*other.re+self.im*other.im)/d,
                 (self.im*other.re-self.re*other.im)/d)

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def upper_norm(self):
        return abs(self.re) + abs(self.im)

    def lower_norm(self):
        return max(abs(self.re), abs(self.im))


def cq(v):
    if isinstance(v, C):
        return v
    return C(exact(v))


def poly(coeffs, z):
    """a0 + a1*z + ..., exact Q(i) Horner."""
    z = cq(z)
    ret = C(0)
    for a in reversed(coeffs):
        ret = ret*z+cq(a)
    return ret


def derivative_lipschitz(coeffs, radius):
    """sup_|z|<=R |P'(z)| bounded using abs-1 rational coefficients."""
    R = exact(radius)
    if R < 0:
        raise ContourError('negative radius')
    return sum((j*cq(c).upper_norm()*R**(j-1) for j,c in enumerate(coeffs) if j), Q(0))


def rectangle(cx, cy, halfwidth, halfheight, subdivisions=32):
    """Simple counterclockwise rectangular polygon in the shifted z=s-1/2 chart."""
    cx,cy,hx,hy = map(exact,(cx,cy,halfwidth,halfheight))
    if hx<=0 or hy<=0 or type(subdivisions) is not int or not 1<=subdivisions<=2048:
        raise ContourError('invalid simple rectangle')
    corners = (C(cx-hx,cy-hy), C(cx+hx,cy-hy),
               C(cx+hx,cy+hy), C(cx-hx,cy+hy))
    points=[]
    for k in range(4):
        a,b=corners[k],corners[(k+1)%4]
        for j in range(subdivisions):
            t=Q(j,subdivisions)
            points.append(a*(1-t)+b*t)
    return tuple(points)


def exact_winding(vertices, ray_slope=Q(1,7)):
    """Exact oriented crossings of rational ray y = ray_slope*x, x>0.

    Reject vertex/ray intersections and zero-side degeneracies. No atan,
    root finder or floating point. Input image is a polygon with no zero edge.
    """
    vs=tuple(cq(v) for v in vertices)
    if len(vs)<3:
        raise ContourError('polygon needs three vertices')
    theta=exact(ray_slope)
    rot=[(v.re+theta*v.im, v.im-theta*v.re) for v in vs]
    if any(y == 0 or (x==0 and y==0) for x,y in rot):
        raise ContourError('ray passes through a polygon vertex')
    total=0
    for (x0,y0),(x1,y1) in zip(rot,rot[1:]+rot[:1]):
        if y0*y1 >= 0:
            continue
        crossing_x = (x0*y1-x1*y0)/(y1-y0)
        if crossing_x == 0:
            raise ContourError('polygon edge passes through zero')
        if crossing_x > 0:
            total += 1 if y0 < 0 < y1 else -1
    return total


def winding_any_ray(vertices):
    for angle in (Q(1,7),Q(1,5),Q(2,7),Q(1,11),Q(0),Q(3,10)):
        try:
            return exact_winding(vertices,angle),angle
        except ContourError:
            pass
    raise ContourError('no admissible ray')


@dataclass(frozen=True)
class CertifiedAnalyticModel:
    """P(z) with externally JUSTIFIED uniform |F-P|<=eps on |z|<=R.

    Authentication is not inferred from model construction. Call
    original_xi_model() with the checked parent theta receipt for an
    actual theorem concerning ξ. Synthetic fixtures only prove themselves.
    """
    coeffs: tuple[C, ...]
    radius: Q
    error: Q
    source_id: str
    provenance: str

    def __post_init__(self):
        if not self.coeffs or not self.source_id or not self.provenance:
            raise ContourError('missing analytic source/model or polynomial')
        if exact(self.radius)<=0 or exact(self.error)<0:
            raise ContourError('invalid disk and uniform error')
        if any(not isinstance(a,C) for a in self.coeffs):
            raise ContourError('coefficients must be exact complex rationals')
        object.__setattr__(self,'radius',exact(self.radius))
        object.__setattr__(self,'error',exact(self.error))


def certify_rectangle(model, cx,cy,hx,hy,subdivisions=32):
    """Validated argument-principle count for the ACTUAL analytic model.

    For each segment, P and F remain inside a disk centered on P(z_i)
    missing zero. The image chord shares that disk. Thus winding of F-image
    equals exact rational winding of polygon of P(vertex) values.
    """
    points=rectangle(cx,cy,hx,hy,subdivisions)
    if any(p.norm2()>model.radius*model.radius for p in points):
        raise ContourError('source error unsupported outside its disk')
    vals=tuple(poly(model.coeffs,p) for p in points)
    lip=derivative_lipschitz(model.coeffs,model.radius)
    margins=[]
    for i,(v,p) in enumerate(zip(vals,points)):
        edge=points[(i+1)%len(points)]-p
        # sum absolute coordinate increments upper-bounds complex edge length.
        m=v.lower_norm()-lip*edge.upper_norm()-model.error
        if m<=0:
            raise ContourError('UNRESOLVED: polynomial path or source error could meet zero')
        margins.append(m)
    count,ray=winding_any_ray(vals)
    if count<0:
        raise ContourError('negative winding on CCW analytic contour: source error')
    return {
        'status':'CERTIFIED_CONTOUR_COUNT',
        'count':count,
        'source':model.source_id,
        'provenance':model.provenance,
        'vertices':len(points),
        'comparison_disk':str(model.radius),
        'uniform_error':str(model.error),
        'min_nonzero_margin':str(min(margins)),
        'ray_slope':str(ray),
        'domain':'rectangle in z=s-1/2; no roots on boundary',
        'zero_inputs':False,'RH_proved':False
    }


def _gitblob(text):
    raw=text if isinstance(text,bytes) else text.encode('utf-8')
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def _exp_upper(x):
    """Pure-rational upper bound for exp(x), 0<=x<=60.

    Tail ≤next_term/(1 - x/(n+2)) for n>=2x; geometric quotient
    decreases at subsequent steps. No transcendental oracle.
    """
    x=exact(x)
    if x<0 or x>60:
        raise ContourError('comparison exponential outside justified domain')
    degree=max(80,3*((x.numerator+x.denominator-1)//x.denominator)+20)
    val=Q(1);term=Q(1)
    for j in range(1,degree+1):
        term*=x/j
        val+=term
    following=term*x/(degree+1)
    return val+following/(1-x/Q(degree+2))




def _source_B_upper(radius):
    """Tight integer-even theta-cosh moment majorant from Gaussian source.

    For R=2m, cosh(m log t)<=t^m on t>=1 and
    psi(t)<2 exp(-3t). Thus B(2m)<=2*m!/3^(m+1).
    General rational radii retain the older Gaussian bound.
    """
    R=exact(radius)
    if R>0 and R.denominator==1 and R.numerator%2==0:
        m=R.numerator//2
        return Q(2*factorial(m),3**(m+1))
    return _exp_upper(R*R/8)

def _source_b_upper(degree):
    """Gaussian source moment bound, using (log t)²<=t for t>=1."""
    d=degree
    return Q(2*factorial(d),4**d*factorial(2*d)*3**(d+1))

def _parent_receipt(root):
    path=Path(root)/THETA_RECEIPT_PATH
    raw=path.read_bytes()
    if _gitblob(raw)!=THETA_RECEIPT_BLOB:
        raise ContourError('original theta scientific receipt Git-blob mismatch')
    r=json.loads(raw)
    if (r.get('source') != 'authentic_unweighted_integer_Gaussian_theta' or
        r.get('zero_coordinates_used') is not False or
        r.get('parameters')!={'T':8,'cells':1536,'degree':20,'modes':3} or
        len(r.get('even_xi_coefficients',[]))!=21 or
        len(r.get('positive_B_moments',[]))!=21):
        raise ContourError('wrong source, provenance or mathematical model')
    return r


def _xi_model(root, radius, comparison, centered):
    r=_parent_receipt(root)
    R=exact(radius);T=exact(comparison)
    if not 0<R<T<=21:
        raise ContourError('radius/comparison unsupported')
    coeffs=[];uncertainty=Q(0)
    for j,(lo,hi) in enumerate(r['even_xi_coefficients']):
        l,u=Q(lo),Q(hi)
        if l>u:
            raise ContourError('reversed original source coefficient interval')
        if centered and j==0:
            coeffs.append(C(0))
        else:
            coeffs.append(C((l+u)/2))
            uncertainty+=(u-l)*R**(2*j)/2
    D=20
    b_upper=Q(r['positive_B_moments'][D][1])
    if b_upper<0:
        raise ContourError('negative source moment upper bound')
    # True original-source remainder from the exact b20+analytic B-bound.
    tail=min(b_upper,_source_b_upper(D))*R**(2*D+2)+(R*R+Q(1,4))*_source_B_upper(T)*(R/T)**(2*D+2)
    # If F-F(0), subtracting the exact unknown a0 removes constant uncertainty;
    # the analytic remainder has zero at 0 by its source formula, so no doubling.
    even_polynomial=tuple(C(0) if k%2 else coeffs[k//2] for k in range(2*D+1))
    return CertifiedAnalyticModel(even_polynomial,
                                  R,uncertainty+tail,
                                  'xi(1/2+z)-xi(1/2)' if centered else 'xi(1/2+z)',
                                  f'authentic theta Git blob {THETA_RECEIPT_BLOB}')


def original_xi_model(root, radius=Q(3), comparison=Q(13)):
    return _xi_model(root,radius,comparison,False)


def centered_xi_model(root, radius=Q(3,2),comparison=Q(13)):
    return _xi_model(root,radius,comparison,True)


def zeta_zero_side_tail_constant(a, t_start, derivative_order=6):
    """Explicit classical O(T^-3) tail for one smooth symmetric compact test.

    v_a(x)=(1-(x/a)^2)^8_+, h=v_a*vtilde_a. On zeros ρ with 0<Reρ<1,
    |∫h(x)e^{(ρ-1/2)x}dx| <= A/|Imρ|^6.
    Assumes classical external N(T)<=T^2 for T>=3 (Riemann-von Mangoldt).
    The integer-start tail bound is (4A)/(3(T-1)^3), for integer T>=4.
    The formula is deliberately broad, not an RH/sign assertion.
    """
    a=exact(a)
    if a<=0 or a>1 or type(t_start) is not int or t_start<4 or derivative_order!=6:
        raise ContourError('unsupported source test / zero counting bound')
    # v_a derivatives of (1-(x/a)^2)^8; L1 bounds on [-a,a].
    v=[]
    for j in range(7):
        j_sum=sum((comb(8,m)*factorial(2*m)//factorial(2*m-j)
                   for m in range(8+1) if 2*m>=j), 0)
        v.append(2*a*Q(j_sum)/a**j)
    v[0]=2*a  # 0<=v_a<=1; sharp elementary integral upper bound.
    # v derivatives * ||v||1 convolution upper bound.
    # On |x|<=2a, exp(|Reρ−1/2| |x|)<=e^a<=3 for a<=1.
    A=3*v[0]*sum((comb(6,j)*v[j]/2**(6-j) for j in range(7)),Q(0))
    return {'test':'(1-(x/a)^2)^8_+ autocorrelation',
            'a':str(a),'T':t_start,'A_upper':str(A),
            'full_zero_side_tail_upper':str(4*A/(3*(t_start-1)**3)),
            'external_zero_count_assumption':'N(T)<=T^2 for T>=3',
            'RH_proved':False}


def contour_weil_identity_note():
    """Proof-level bridge, not a numerically executed contour integral.

    For h=v*tilde(w), H_h(s)=∫h(x)e^((s−1/2)x)dx is entire.
    On admissible contour Γ: ∮ H_h ξ'/ξ / (2πi) = Σ_(zeros in Γ) H_h(ρ).
    On RH-local zeros, H_(v*tildev)(1/2+iγ)=|∫v e^(iγx)dx|²>=0.
    Full W(h) = absolutely convergent zero side by standard Weil explicit formula,
    h compact-smooth and N(T)=O(T log T). The comparison with actual Suzuki
    W(h) is an EXTERNAL THEOREM, not implied by contour positivity.
    """
    return {'source':'authentic_completed_xi',
            'finite_contour_weighted_residue':'residue_theorem',
            'global_signed_distribution':'classical_Weil_explicit_formula',
            'compact_test_space':'C_c^infty(R)',
            'positive_if_enclosed_zeros_verified_on_line':True,
            'tail_sign_determined':False,
            'full_Weil_positive':False,'RH_proved':False}


def shadow_interval_model(shadow_json, radius, comparison=13, centered=False):
    """Local development adapter using an OUTWARD ROUNDED #78 witness.

    This is source-conditional. In the actual SUCC checkout use
    original_xi_model/centered_xi_model instead: those hash-verify the
    complete historical receipt. Forged shadow files are not authenticated.
    """
    data=json.loads(Path(shadow_json).read_text())
    if data.get('upstream_git_blob_sha')!=THETA_RECEIPT_BLOB:
        raise ContourError('shadow provenance tag mismatch')
    q=Q(data['scale'])
    intervals=[(Q(int(l),q),Q(int(h),q)) for l,h in data['even_xi_intervals_scaled']]
    if len(intervals)!=21 or any(l>h for l,h in intervals):
        raise ContourError('malformed witness')
    R,T=map(exact,(radius,comparison))
    if not 0<R<T<=21:
        raise ContourError('out of analytic comparison domain')
    coeffs=[];error=Q()
    for j,(l,h) in enumerate(intervals):
        if centered and j==0:
            coeffs.append(C(0))
        else:
            coeffs.append(C((l+h)/2))
            error+=(h-l)*R**(2*j)/2
    b20=Q(data['positive_b20_upper'])
    tail=min(b20,_source_b_upper(20))*R**42+(R**2+Q(1,4))*_source_B_upper(T)*(R/T)**42
    even_polynomial=tuple(C(0) if k%2 else coeffs[k//2] for k in range(41))
    return CertifiedAnalyticModel(even_polynomial,R,error+tail,
        'source-conditional-Xi-shift' if centered else 'source-conditional-Xi',
        'unverified_local_copy_of_parent_receipt_'+THETA_RECEIPT_BLOB)


def verify_shadow_against_original(root, shadow_json):
    """Exact independent ledger correspondence on the real checkout.

    The local outward-rounded snapshot is never elevated to an authenticated
    source just by a string tag. The immutable full upstream blob is required.
    """
    source=_parent_receipt(root)
    shadow=json.loads(Path(shadow_json).read_text())
    if shadow.get('upstream_git_blob_sha')!=THETA_RECEIPT_BLOB:
        raise ContourError('shadow claims wrong upstream blob')
    scale=Q(shadow['scale'])
    if len(shadow.get('even_xi_intervals_scaled',[]))!=21:
        raise ContourError('shadow malformed')
    for (lo,hi),(a,b) in zip(shadow['even_xi_intervals_scaled'], source['even_xi_coefficients']):
        if not Q(int(lo),scale)<=Q(a)<=Q(b)<=Q(int(hi),scale):
            raise ContourError('a rounded coefficient fails true source enclosure')
    if Q(shadow['positive_b20_upper'])<Q(source['positive_B_moments'][20][1]):
        raise ContourError('b20 source-tail cap forged')
    return {'upstream_sha':THETA_RECEIPT_BLOB,
            'all_21_theta_coefficients_enclosed':True,
            'b20_upper_authentic':True,'physical_source_authenticated':False}


def derivative_scaling_obstruction(n):
    """Exact scaling under epsilon=n^-2; v_e=sqrt(e)f(x/e).

    ||v_e'||_2 is constant, while ||v_e^(6)||_1 = n^9 ||f^(6)||_1.
    Thus a 6-derivative zero-tail norm estimate is not uniform on H0^1.
    """
    if type(n) is not int or n<1:
        raise ContourError('invalid narrow-bump scale')
    return {'inverse_width':n, 'H1_seminorm_factor_squared':Q(1),
            'sixth_derivative_L1_factor':Q(n**9),
            'uniform_H1_tail_claimed':False}


def reflected_fake_non_euler(model):
    """Mutant F_fake(z)=(10*z²-3/2)*F(z), preserving z↦−z.

    Legitimate analytic model of a deliberately incorrect source. Not Euler
    and not an honest new ζ-place. The source name explicitly records this.
    """
    factor=(C(-Q(3,2)),C(0),C(10))
    new=[C(0)]*(len(model.coeffs)+2)
    for j,x in enumerate(model.coeffs):
        for k,y in enumerate(factor):
            new[j+k]=new[j+k]+x*y
    r=model.radius
    return CertifiedAnalyticModel(tuple(new),r,
                                  model.error*(Q(10)*r*r+Q(3,2)),
                                  'MUTANT_nonEuler_reflection_symmetric_Xi',
                                  model.provenance+'; synthetic factor (10*z²−3/2)')


def fake_reflected_odd_negative_bound(a=Q(1)):
    """Entirely exact negative LOCAL zero-side form for the *mutated* Xi.

    Reflection-preserving multiplier 10z²−3/2 has real zeros ±d with
    d²=3/20. On odd real compact test v=x(1−(x/a)²)^8_+,
    V(−d)=−V(d), V(d)>=2d a³ C8, C8=∫_0^1 y²(1−y²)^8dy>0.
    Thus the pair's zero-side form is −2 V(d)²<=−(6/5) C8² a^6.
    No actual Riemann-zeta zero is inserted, and the mutant is non-Euler.
    """
    a=exact(a)
    if a<=0 or a>1:
        raise ContourError('test radius outside declared interval')
    c=sum(((-1)**k*Q(comb(8,k),2*k+3) for k in range(9)),Q(0))
    if c<=0:
        raise ArithmeticError('positive integral expansion invalid')
    return {'source':'fake_reflection_nonEuler',
            'synthetic_offline_zero_pair_squared_distance':'3/20',
            'positive_integral_C8':str(c),
            'local_weil_pairing_strict_upper':str(-Q(6,5)*c*c*a**6),
            'negative_certified_for_odd_test':True,
            'genuine_zeta_weil_sign_proved':False,
            'zero_input_oracle_used':False}
