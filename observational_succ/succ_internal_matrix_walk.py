"""Authenticated BBP-SUCC as a matrix-valued, exact rational phase walk.

Arithmetic source: original four-pole Coherent Main X r(n), U0=0,
U_(n+1)=16U_n+r(n+1). No pi values, pi digits or conjectural normality
enter the engine. Characters are represented by formal elements of the
rational circle group algebra Q[Q/Z], never approximate complex phases.

Paper theorems: positive Gram walk; exact rank-one update/purity and Fejer
collision formula; source-typed high-frequency Koopman shift; nonuniform
frequency-time limit; signed Pascal forcing differences. None proves
pi normality, signed Weil positivity, or physical field realization.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, lcm


class MatrixWalkError(ValueError):
    """Invalid source, finite carrier, clock, or formal phase."""


def rat(x):
    if type(x) not in (int,Q):
        raise MatrixWalkError("exact integers / Fraction only, not float or bool")
    return Q(x)


def natural(x, lo=0, hi=100000):
    if type(x) is not int or not lo<=x<=hi:
        raise MatrixWalkError("bounded ordinary successor index required")
    return x


def circle(x):
    x=rat(x)
    return x-(x.numerator//x.denominator)


def authentic_r(n):
    """Literal original signed four-pole BBP forcing; first index is n=1."""
    natural(n,1,10**25)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def original_state(n):
    """Exact unwrapped rational BBP orbit U_n from U_0=0."""
    natural(n,0,2000)
    x=Q()
    for j in range(1,n+1):
        x=16*x+authentic_r(j)
    return x


@dataclass(frozen=True)
class PhasePoly:
    """Canonical formal group algebra Q[Q/Z] with basis e(q), q rational.

    e(p)e(q)=e(p+q), e(q)^*=e(-q), and e(0)=1. This exact
    symbolic representation is not a complex numerical evaluation.
    """
    terms: tuple[tuple[Q,Q],...]

    def __post_init__(self):
        if any(type(p) is not Q or type(c) is not Q or not Q(0)<=p<1 or c==0
               for p,c in self.terms):
            raise MatrixWalkError("canonical rational phase and nonzero rational coefficient")
        if tuple(sorted(self.terms))!=self.terms or len(set(p for p,_ in self.terms))!=len(self.terms):
            raise MatrixWalkError("canonical sorted unique phases required")

    @classmethod
    def from_dict(cls, raw):
        d={}
        for p,c in raw.items():
            pp=circle(p)
            d[pp]=d.get(pp,Q())+rat(c)
        return cls(tuple(sorted((k,v) for k,v in d.items() if v)))

    @classmethod
    def monomial(cls,p,c=1):
        return cls.from_dict({rat(p):rat(c)})

    @classmethod
    def zero(cls):return cls(())

    @classmethod
    def one(cls):return cls.monomial(0)

    def __add__(self,other):
        if type(other) in (int,Q):other=PhasePoly.monomial(0,other)
        if type(other) is not PhasePoly: return NotImplemented
        d=dict(self.terms)
        for p,c in other.terms:d[p]=d.get(p,Q())+c
        return PhasePoly.from_dict(d)

    __radd__=__add__

    def __neg__(self):return PhasePoly.from_dict({p:-c for p,c in self.terms})

    def __sub__(self,other):return self+(-other if type(other) is PhasePoly else -rat(other))

    def __rsub__(self,other):return -self+other

    def __mul__(self,other):
        if type(other) in (int,Q):return PhasePoly.from_dict({p:c*rat(other) for p,c in self.terms})
        if type(other) is not PhasePoly:return NotImplemented
        d={}
        for p,c in self.terms:
            for q,v in other.terms:
                ph=circle(p+q)
                d[ph]=d.get(ph,Q())+c*v
        return PhasePoly.from_dict(d)

    __rmul__=__mul__

    def __truediv__(self,scalar):
        s=rat(scalar)
        if s==0:raise MatrixWalkError("division by zero")
        return self*(1/s)

    def star(self):return PhasePoly.from_dict({circle(-p):c for p,c in self.terms})

    def coefficient(self,p):return dict(self.terms).get(circle(p),Q())

    def evaluation(self,precision=50):
        """Clearly numerical diagnostic, never a certified interval."""
        import mpmath as mp
        with mp.workdps(natural(precision,20,1000)):
            return sum((mp.mpf(c.numerator)/c.denominator*
                       mp.exp(2*mp.pi*mp.j*mp.mpf(p.numerator)/p.denominator)
                       for p,c in self.terms),mp.mpc(0))


def source_cyclotomic_quotient(polynomial, modulus_cap=256):
    """Reduce formal rational phases in the existing SUCC cyclotomic carrier.

    The free Q[Q/Z] phase labels do NOT include primitive-root relations.
    This explicit quotient proves additional algebraic cancellations but the
    common denominator may exceed any finite budget. No silent fallback.
    """
    if type(polynomial) is not PhasePoly:
        raise MatrixWalkError("formal phase polynomial required")
    natural(modulus_cap,2,10000)
    modulus=1
    for phase,_ in polynomial.terms:
        modulus=lcm(modulus,phase.denominator)
    modulus=max(2,modulus)
    if modulus>modulus_cap:
        raise MatrixWalkError("full source cyclotomic conductor exceeds declared budget")
    from .finite_fourier_carrier import CyclotomicElement
    ans=CyclotomicElement.scalar(modulus,0)
    for phase,coeff in polynomial.terms:
        ans=ans+CyclotomicElement.root(modulus,int(modulus*phase)).scale(coeff)
    return ans


def geometric_frequency_gram(walk):
    """Exact source Gram on the natural Fourier Koopman ladder h*16^k.

    This is NOT Toeplitz in k: the geometric ladder must not be treated as
    consecutive ordinary Fourier frequencies. Its positive Gram and rank-one
    updates share the authentic history with the additive-harmonic Gram.
    """
    if not isinstance(walk,MatrixWalk) or not walk.time:
        raise MatrixWalkError("nonempty matrix history required")
    freq=tuple(walk.base_frequency*16**k for k in range(walk.width))
    gram=tuple(tuple(sum((formal_character(freq[i]-freq[j],u) for u in walk.history),PhasePoly.zero())
                     for j in range(walk.width)) for i in range(walk.width))
    for k in range(walk.width):
        if gram[k][k]!=PhasePoly.monomial(0,walk.time):
            raise ArithmeticError("source Gram diagonal failure")
    return gram


def mixed_phase_derivative(time,k,frequency_steps,time_steps,frequency=1):
    """Exact mixed Pascal phase derivative: Δ_k^a Δ_n^b θ=15^a16^k h Δ_n^b r.

    The sign is on UNWRAPPED rational phase angles. After modulo 1,
    orientation can alias and cannot establish Weyl cancellation.
    """
    natural(time,0)
    natural(k,0,1000)
    natural(frequency_steps,0,32)
    natural(time_steps,0,32)
    if type(frequency) is not int or frequency==0:
        raise MatrixWalkError("nonzero integer frequency required")
    d=sum(((-1)**(time_steps-j)*comb(time_steps,j)*authentic_r(time+j+1)
           for j in range(time_steps+1)),Q())
    if time_steps and (-1)**time_steps*d<=0:
        raise ArithmeticError("original positive moment source derivative sign failed")
    return Q(frequency*16**k*15**frequency_steps)*d


def formal_character(frequency,state):
    return PhasePoly.monomial(rat(frequency)*rat(state))


@dataclass(frozen=True)
class MatrixWalk:
    """One actual source, SUCC-time steps, and internally updated Gram matrix.

    Width H means columns chi_(kh)(U_n), k=0..H-1. The finite operator
    is a Gram of actual source vectors, not a generic ergodic model.
    """
    time:int
    lifted_state:Q
    base_frequency:int
    width:int
    history:tuple[Q,...]
    gram:tuple[tuple[PhasePoly,...],...]

    @classmethod
    def initial(cls,width=4,base_frequency=1):
        natural(width,2,24)
        if type(base_frequency) is not int or base_frequency==0 or abs(base_frequency)>100000:
            raise MatrixWalkError("fixed nonzero integer character required")
        z=PhasePoly.zero()
        return cls(0,Q(0),base_frequency,width,(),tuple(tuple(z for _ in range(width)) for _ in range(width)))

    def next_character_vector(self):
        next_n=self.time+1
        u=16*self.lifted_state+authentic_r(next_n)
        return u, tuple(formal_character(self.base_frequency*k,u) for k in range(self.width))

    def succ(self):
        if self.time>=2000: raise MatrixWalkError("maximum finite work budget reached")
        u,v=self.next_character_vector()
        new=tuple(tuple(self.gram[i][j]+v[i]*v[j].star()
                        for j in range(self.width)) for i in range(self.width))
        result=MatrixWalk(self.time+1,u,self.base_frequency,self.width,self.history+(u,),new)
        if not result.validate():raise ArithmeticError("source Gram orientation or diagonal failed")
        return result

    def validate(self):
        H=self.width
        if self.time!=len(self.history) or (self.history and self.history[-1]!=self.lifted_state):return False
        for i in range(H):
            for j in range(H):
                if self.gram[i][j]!=self.gram[j][i].star():return False
                if i==j and self.gram[i][j]!=PhasePoly.monomial(0,self.time):return False
                if self.gram[i][j]!=sum((formal_character((i-j)*self.base_frequency,u) for u in self.history),PhasePoly.zero()):return False
        return True

    def normalized(self):
        if self.time==0:raise MatrixWalkError("need at least one successor before normalizing")
        return tuple(tuple(x/self.time for x in row) for row in self.gram)

    def frequency_average(self,difference):
        if self.time==0:raise MatrixWalkError("nonempty current required")
        return sum((formal_character(difference*self.base_frequency,u) for u in self.history),PhasePoly.zero())/self.time

    def purity(self):
        A=self.normalized()
        return sum((A[i][j]*A[j][i] for i in range(self.width) for j in range(self.width)),PhasePoly.zero())

    def excess_by_fourier(self):
        H=self.width
        return sum((2*(H-j)*self.frequency_average(j)*self.frequency_average(j).star()
                    for j in range(1,H)),PhasePoly.zero())

    def innovation(self):
        """Return exact Fejer overlap v^* A_n v and next spectral purity."""
        if self.time==0:raise MatrixWalkError("need previous observations")
        u,v=self.next_character_vector()
        A=self.normalized()
        q=sum((v[i].star()*A[i][j]*v[j]
               for i in range(self.width) for j in range(self.width)),PhasePoly.zero())
        p=self.purity()
        H=self.width;N=self.time
        predicted=(N*N*p+2*N*q+H*H*PhasePoly.one())/((N+1)**2)
        next_actual=self.succ().purity()
        if predicted!=next_actual:raise ArithmeticError("rank-one spectral purity identity broken")
        # independent Fejer kernel from pairwise phase separations
        fejer=sum((sum((formal_character(k*self.base_frequency,u-v0)
                              for k in range(H)),PhasePoly.zero())*
                   sum((formal_character(-k*self.base_frequency,u-v0)
                              for k in range(H)),PhasePoly.zero())
                   for v0 in self.history),PhasePoly.zero())/N
        if q!=fejer:raise ArithmeticError("phase-pair Fejer and Gram innovation differ")
        return q,predicted


def gram_spectral_certificate(walk):
    """Exact finite equivalence: offdiagonal energy ↔ moment/Weyl norms."""
    if not isinstance(walk,MatrixWalk) or not walk.time:raise MatrixWalkError("populated authenticated walk required")
    P=walk.purity()
    E=walk.excess_by_fourier()
    if P-walk.width!=E:raise ArithmeticError("Fourier purity is not Toeplitz energy")
    return {'source': 'Q:Coherent-Main-X-four-pole-BBP',
            'N':walk.time,'width':walk.width,'spectral_purity':P,
            'offdiagonal_excess':E,
            'zero_mode':PhasePoly.one(),
            'rank_purity_floor':Q(walk.width**2,min(walk.time,walk.width)),
            'normality_proved':False}


def finite_koopman_phases(source_time,frequency,depth):
    """Every column e_k shifts to e_(k+1) with authentic unimodular twist.

    No finite depth is a closed invariant Fourier carrier; outgoing top
    column has norm one, rather than asymptotically small operator debt.
    """
    natural(source_time,0)
    natural(depth,1,1000)
    if type(frequency) is not int or frequency==0:raise MatrixWalkError("integer nonzero h")
    r=authentic_r(source_time+1)
    phases=tuple(circle(Q(frequency*16**k)*r) for k in range(depth))
    gauge=[Q(0)]
    for phi in phases:gauge.append(circle(gauge[-1]+phi))
    if any(circle(gauge[k]+phases[k]-gauge[k+1])!=0 for k in range(depth)):
        raise ArithmeticError("finite frequency ladder not diagonally gaugeable")
    return {'source_time':source_time,'frequency':frequency,
            'phases':phases,'diagonal_gauge':tuple(gauge),
            'finite_compression_boundary_squared_norm':Q(1),
            'complete_source_interaction_certified':False}


def phase_plaquette(time,k,frequency=1):
    """Signed 2D SUCC×FUCC finite difference of unwrapped phase source.

    Not gauge invariant under arbitrary unrelated time/frequency changes;
    invariant under additive separable chart changes a(time)+b(k).
    """
    natural(time,0)
    natural(k,0,1000)
    if type(frequency) is not int or frequency==0:raise MatrixWalkError("integer nonzero frequency")
    r1=authentic_r(time+1)
    r2=authentic_r(time+2)
    return Q(15*frequency*16**k)*(r2-r1)


def signed_source_difference(time,order=1,k=0,frequency=1):
    natural(time,0)
    natural(order,0,60)
    natural(k,0,1000)
    if type(frequency) is not int or frequency==0:raise MatrixWalkError("integer h required")
    value=sum(((-1)**(order-j)*comb(order,j)*authentic_r(time+j+1) for j in range(order+1)),Q())
    if frequency>0 and order>0 and not (-1)**order*value>0:
        raise ArithmeticError("positive original BBP Hausdorff moment difference violated")
    return Q(frequency*16**k)*value


def frequency_boundary_witness(j):
    """n=4^j, k=j: r(n+1)*16^k→15/64, NOT 0.

    The rational finite inequality 0<15/64-n²*r(n+1)<7/(5n)
    follows after clearing positive denominators from the exact four-pole
    forcing (all coefficients of the resulting polynomial are positive).
    """
    natural(j,0,30)
    n=4**j
    value=Q(16**j)*authentic_r(n+1)
    defect=Q(15,64)-value
    if not Q(0)<defect<Q(7,5*n):raise ArithmeticError("critical band asymptotic certified bound fails")
    return {'n':n,'frequency_exponent':j,'unwrapped_twist':value,
            'limiting_twist':Q(15,64),'positive_error':defect,
            'error_cap':Q(7,5*n),'nonzero_limit_mod_one':True}


def temporal_derivative_boundary(j):
    """n=16^j, k=3j: scaled adjacent forcing drift ->15/32.

    Exact positive-denominator algebra proves
      0<15/32-n³*(r(n+1)-r(n+2))<3/n.
    """
    natural(j,0,15)
    n=16**j
    amount=Q(16**(3*j))*(authentic_r(n+1)-authentic_r(n+2))
    deficit=Q(15,32)-amount
    if not Q(0)<deficit<Q(3,n):raise ArithmeticError("moving-frequency derivative persists")
    return {'n':n,'frequency_exponent':3*j,'unwrapped_time_drift':amount,
            'limiting_drift':Q(15,32),'positive_error':deficit,
            'error_cap':Q(3,n)}


def walsh_digit_energy(digits,bit_count=4):
    """Exact Walsh/Parseval collision energy for actual supplied digit words.

    Caller must source-authenticate digits separately. The function cannot
    infer BBP provenance merely because values are in the valid alphabet.
    """
    natural(bit_count,1,16)
    M=2**bit_count
    data=tuple(digits)
    if not data or any(type(v) is not int or not 0<=v<M for v in data):
        raise MatrixWalkError("finite source digit words in declared alphabet required")
    count=[0]*M
    for d in data:count[d]+=1
    N=len(data)
    amps=tuple(Q(sum((-1 if (j & mask).bit_count()%2 else 1)*count[j] for j in range(M)),N)
               for mask in range(M))
    collision=Q(M*sum(c*c for c in count),N*N)
    purity=sum((v*v for v in amps),Q())
    if purity!=collision or amps[0]!=1:raise ArithmeticError("Walsh/Parseval source flux identity failed")
    return {'alphabet':M,'observations':N,'counts':tuple(count),'walsh_amplitudes':amps,
            'collision_energy':collision,'spectral_energy':purity,
            'highest_joint_bit_amplitude':amps[-1],
            'source_authenticated':False,'normality_proved':False}


def exact_source_digits(states,bit_count=4):
    """Take digits of the rational BBP U_n circle quotient, not actual pi digits.

    Future Green corrections can cross radix cells, so pi digit identity
    is NEVER inferred from these digits without a separate tail certificate.
    """
    natural(bit_count,1,12)
    M=2**bit_count
    if not isinstance(states,tuple) or not states:raise MatrixWalkError("finite exact rational state tuple required")
    return tuple((M*circle(u)).numerator//(M*circle(u)).denominator for u in states)
