"""Exact GR-shaped *mathematical* transport on the canonical BBP source algebra.

Two distinct mathematical types:
 (1) original zero-seeded BBP source precision modulo 2**k, with a sharp
     four-bit/recurrence-step filtration cone;
 (2) the cotangent lift of the original FOUR-STATE rational transfer,
     preserving its canonical split primal/dual pairing. Its eighth return
     is a rational Lorentz boost, NOT a physical or source-mixing process.

The two clock indices are different: BBP source time n and generating-function
impulse time m. Nothing here implies a real-circle Weyl saving or pi normality.
All claims use Fraction arithmetic and the unchanged 4-pole BBP source.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import importlib.util

_PARENT = Path(__file__).resolve().parents[1] / 'gaussian_unit_gluing' / 'gaussian_unit_gluing.py'
_spec = importlib.util.spec_from_file_location('gaussian_unit_gluing_readonly', _PARENT)
if _spec is None or _spec.loader is None:
    raise ImportError(f'missing exact pinned parent module {_PARENT}')
parent = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(parent)

RADIX = 16
BIT_RATE = 4
DIM = 4
I4 = tuple(tuple(Q(int(i == j)) for j in range(DIM)) for i in range(DIM))
ZERO4 = tuple(tuple(Q(0) for _ in range(DIM)) for _ in range(DIM))


def exact(x):
    if type(x) not in (int, Q):
        raise TypeError('exact int/Fraction only; floating values are not certificates')
    return Q(x)


def identity(size):
    return tuple(tuple(Q(int(i == j)) for j in range(size)) for i in range(size))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def matmul(a,b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError('incompatible nonempty matrix shapes')
    return tuple(tuple(sum((exact(a[i][k])*exact(b[k][j]) for k in range(len(b))),Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matpow(a,n):
    if type(n) is not int or n<0 or len(a)!=len(a[0]):
        raise ValueError('square matrix and nonnegative integer power')
    r=identity(len(a))
    while n:
        if n&1:
            r=matmul(r,a)
        a=matmul(a,a)
        n//=2
    return r


def inverse(a):
    n=len(a)
    if not n or any(len(row)!=n for row in a):
        raise ValueError('square matrix')
    z=[[exact(v) for v in row]+[Q(int(i==j)) for j in range(n)]
       for i,row in enumerate(a)]
    for k in range(n):
        pivot=next((j for j in range(k,n) if z[j][k]),None)
        if pivot is None:
            raise ValueError('singular matrix')
        z[k],z[pivot]=z[pivot],z[k]
        v=z[k][k]
        z[k]=[x/v for x in z[k]]
        for j in range(n):
            if j==k:
                continue
            v=z[j][k]
            if v:
                z[j]=[z[j][i]-v*z[k][i] for i in range(2*n)]
    return tuple(tuple(row[n:]) for row in z)


def multiplication_matrix():
    """Matrix of multiplication by canonical u in Q[u]/m."""
    basis=[parent.el(*[int(i==j) for i in range(4)]) for j in range(4)]
    cols=[parent.mul(parent.U, v) for v in basis]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def dual_pair(v,f):
    if len(v)!=4 or len(f)!=4:
        raise ValueError('canonical 4D state and its dual required')
    return sum((exact(a)*exact(b) for a,b in zip(v,f)),Q(0))


def split_q(v,f):
    return dual_pair(v,f)


def split_bilinear(v,f,w,g):
    return dual_pair(v,g)+dual_pair(w,f)


def matvec(m,x):
    if len(m[0])!=len(x):
        raise ValueError('invalid state dimension')
    return tuple(sum((exact(a)*exact(b) for a,b in zip(row,x)),Q(0)) for row in m)


def cotangent_step(v,f):
    """(T*v,(T^-1)^transpose*f), the canonical evaluation-preserving lift."""
    a=multiplication_matrix()
    return matvec(a,v),matvec(transpose(inverse(a)),f)


def cotangent_lift_matrix():
    a=multiplication_matrix()
    b=transpose(inverse(a))
    return tuple(tuple((a[i][j] if i<4 and j<4 else
                        b[i-4][j-4] if i>=4 and j>=4 else Q(0))
                        for j in range(8)) for i in range(8))


def split_metric():
    """For doubled 8D carrier: x^T J x = 2*f(v), signature (4,4)."""
    return tuple(tuple(Q(int((i<4 and j==i+4) or (i>=4 and j==i-4)))
                       for j in range(8)) for i in range(8))


def split_metric_preserved(a=None):
    a=cotangent_lift_matrix() if a is None else a
    return matmul(matmul(transpose(a),split_metric()),a)==split_metric()


def source_selected_null_plane():
    """Canonical source b=1 and f=ell/4, so f(b)=1. Invariant at 8 ticks."""
    b=parent.ONE
    f=tuple(parent.readout(parent.el(*[int(i==j) for i in range(4)]))/4
            for j in range(4))
    if dual_pair(b,f)!=1:
        raise AssertionError('source observation normalization corrupted')
    return b,f


def eight_step_cotangent():
    a=matpow(multiplication_matrix(),8)
    dual=matpow(transpose(inverse(multiplication_matrix())),8)
    assert a==tuple(tuple(I4[i][j]/16 for j in range(4)) for i in range(4))
    assert dual==tuple(tuple(16*I4[i][j] for j in range(4)) for i in range(4))
    return a,dual


def halfclock_channel_signs():
    """e_H (4u^4)=+e_H ; e_G (4u^4)=-e_G."""
    eh,eg=parent.projectors()
    u4=parent.power(parent.U,4)
    return (parent.mul(u4,eh)==parent.scale(eh,Q(1,4)),
            parent.mul(u4,eg)==parent.scale(eg,Q(-1,4)))


def boost_from_scale(lam=16):
    """Exact split/null boost from inverse-primal time transport.

    lambda is selected by the eighth return (lambda=16); if arbitrary,
    this is classical Lorentz hyperbola algebra and not BBP-specific.
    Returned matrix on (time coordinate T, space coordinate X) is
    [[gamma,delta],[delta,gamma]] with Q=T^2-X^2. Dimensionless c=1.
    """
    lam=exact(lam)
    if lam<=0:
        raise ValueError('positive reciprocal clock needed')
    gamma=(lam+1/lam)/2
    rapidity_sinh=(lam-1/lam)/2
    beta=rapidity_sinh/gamma
    mat=((gamma,rapidity_sinh),(rapidity_sinh,gamma))
    assert gamma*gamma-rapidity_sinh*rapidity_sinh==1
    return {'lambda':lam,'gamma':gamma,'beta':beta,'gamma_beta':rapidity_sinh,
            'matrix':mat,'half_rapidity_parameter':(lam-1)/(lam+1)}


def lorentz_interval(t,x,c=1):
    c=exact(c)
    if c<=0:
        raise ValueError('positive calibration of the coordinate time unit')
    t,x=exact(t),exact(x)
    return c*c*t*t-x*x


def transform_lorentz(t,x,lam=16,c=1):
    """Coordinate action, optional spatial unit c; not physical spacetime."""
    b=boost_from_scale(lam)
    c=exact(c)
    if c<=0:
        raise ValueError('c must be positive')
    t,x=exact(t),exact(x)
    d=b['gamma_beta'];g=b['gamma']
    return g*t+d*x/c, c*d*t+g*x


def source_r(n):
    return parent.original_four_poles(n)


def v2(x):
    return parent.v2_rational(x)


def rational_mod_2k(x,bits):
    """Only valid when x is 2-integral; negative val input is a TYPE ERROR."""
    if type(bits) is not int or bits<1:
        raise ValueError('bits positive integer')
    x=Q(x)
    if x.denominator %2==0:
        raise ValueError('nonintegral rational has no Z2 residue; glue first')
    mod=1<<bits
    return (x.numerator*pow(x.denominator,-1,mod))%mod


def source_state_mod(n,bits):
    """Original literal U0=0, source time n; full recurrence modular."""
    if type(n) is not int or n<0:
        raise ValueError('nonnegative source time')
    state=0
    for j in range(1,n+1):
        state=(16*state+rational_mod_2k(source_r(j),bits))%(1<<bits)
    return state


def precision_horizon(bits):
    """Number of latest source injections needed for k 2-adic bits."""
    if type(bits) is not int or bits<1:
        raise ValueError('positive precision in bits')
    return (bits+BIT_RATE-1)//BIT_RATE


def suffix_source_mod(n,bits):
    """Only the last ceil(bits/4) original 2-integral source terms matter."""
    if type(n) is not int or n<0:
        raise ValueError('nonnegative source time')
    mod=1<<bits
    ans=0
    for lag in range(min(n,precision_horizon(bits))):
        ans=(ans+pow(16,lag,mod)*rational_mod_2k(source_r(n-lag),bits))%mod
    return ans


def pulse_reaches(bits,age,pulse=1):
    """Exact effect modulo 2^bits from a matched 2-integral source pulse."""
    if type(age) is not int or age<0:
        raise ValueError('age>=0')
    mod=1<<bits
    return (pow(16,age,mod)*rational_mod_2k(Q(pulse),bits))%mod


def source_glued_mod(n,bits):
    """Adds the two NONINTEGRAL channels first, then legal 2-adic reduction."""
    rh,rg=parent.mellin_channels(n)
    if n<1:
        raise ValueError('positive source time')
    return rational_mod_2k(rh+rg,bits)


def rational_seed_ambiguity(n,bits):
    """SAME forcing, different rational seed U0*=1/5.

    Differences delta U_n=16^n/5 become invisible modulo 2^bits for
    n>=ceil(bits/4), while real circle phase difference ALWAYS equals 1/5.
    This is a frame/source-map obstruction, not a counterexample to the
    original marked U0=0, and not evidence about normality of either seed.
    """
    if type(n) is not int or n<0:
        raise ValueError('n>=0')
    d=Q(16**n,5)
    return {'n':n,'delta':d,'v2':4*n,'residue':rational_mod_2k(d,bits),
            'real_phase_offset':d%1}


def near_ghost(k):
    """Globally 2-adic-small rational with real-circle displacement >=1/3.

    r=2^k/(2^(k+1)+1), k>=1; v2(r)=k yet 1/3 <= r <1/2.
    Independent of the original selected source; a transport no-go.
    """
    if type(k) is not int or k<1:
        raise ValueError('k>=1')
    r=Q(2**k,2**(k+1)+1)
    assert v2(r)==k and Q(1,3)<=r<Q(1,2)
    return r


def model_snapshot():
    b=boost_from_scale(16)
    return {'radix':16,'precision_bits_per_source_tick':4,
            'micro_steps_per_scalar_return':8,'scalar_return':Q(1,16),
            'gamma':b['gamma'],'beta':b['beta'],'gamma_beta':b['gamma_beta'],
            'half_rapidity_parameter':b['half_rapidity_parameter'],
            'frame_provenance':'canonical source state + contragredient dual; representation only',
            'pi_normality_proved':False}


def forcing_at_integer(t):
    """Same exact four-pole rational function at any integer 2-adic index.

    This IS the existing DSI source extension, not a changed forcing law.
    For n>=1 it is identical to original r(n). Denominators always odd.
    """
    if type(t) is not int:
        raise TypeError('integer time index')
    x=Q(t)
    return Q(120*x*x-89*x+16,
             (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))


def particular_mod(t,bits):
    """F(t)=sum_{j>=0}16^j r(t-j) mod 2^bits; exact finite evaluator.

    Source-at-index t and backward time are differentiated from the
    original forward recurrence. F(0)=0 and F(n)=U_n are inherited
    analytically proved statements of SUCC's DSI source isometry theorem.
    """
    if type(t) is not int:
        raise TypeError('integer time index')
    horizon=precision_horizon(bits)
    mod=1<<bits
    result=0
    for j in range(horizon):
        result=(result+pow(16,j,mod)*rational_mod_2k(forcing_at_integer(t-j),bits))%mod
    return result


def particular_inverse_mod(value,bits):
    """Unique inverse of F on Z/2^bits via exact compatible bit lifting."""
    if type(value) is not int:
        raise TypeError('integer residue')
    precision_horizon(bits)
    result=0
    for k in range(1,bits+1):
        mod=1<<k
        if particular_mod(result,k)!=value%mod:
            result+=1<<(k-1)
        if particular_mod(result,k)!=value%mod:
            raise ArithmeticError('source isometry inversion failed')
    return result


def source_state_successor_mod(value,bits):
    """Autonomous source-marked state successor sigma=F o (+1) o F^-1."""
    precision_horizon(bits)
    t=particular_inverse_mod(int(value)%(1<<bits),bits)
    output=(16*value+rational_mod_2k(forcing_at_integer(t+1),bits))%(1<<bits)
    if output!=particular_mod(t+1,bits):
        raise ArithmeticError('original-source frame-conjugacy failed')
    return output


def force_difference_quotient_unit(x,y):
    """Exact difference-quotient certificate for x != y in Z.

    (r(x)-r(y))/(x-y) has v2=0 because numerator N' quotient odd,
    denominator D odd, and D(x)-D(y) quotient even. This is the DSI
    source-isometry arithmetic, not a proof of real equidistribution.
    """
    if type(x) is not int or type(y) is not int or x==y:
        raise ValueError('distinct integer indices required')
    q=(forcing_at_integer(x)-forcing_at_integer(y))/Q(x-y)
    assert v2(q)==0
    return q


def canonical_frame_matrix(index):
    """Canonical flat frame from a single source transfer (may be negative)."""
    if type(index) is not int:
        raise ValueError('integer frame index')
    a=cotangent_lift_matrix()
    return matpow(a,index) if index>=0 else matpow(inverse(a),-index)


def frame_transport(source_frame,target_frame):
    """Frame groupoid arrow, paid exactly by canonical source time marks."""
    if type(source_frame) is not int or type(target_frame) is not int:
        raise ValueError('integer labelled frames')
    return canonical_frame_matrix(target_frame-source_frame)


def signed_holonomy_mutant():
    """J-preserving extra central -I gives a nontrivial loop holonomy.

    It is NOT an honest source-attested transition; observer metric invariance
    alone cannot authenticate a frame map. Compare true frame groupoid.
    """
    return tuple(tuple(-x for x in row) for row in identity(8))
