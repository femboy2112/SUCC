"""Research-only autonomous stationary E2 observer for the authentic four-pole BBP.

Exact Fraction state, four signed source poles, literal U0=0. Source E2
rank-two chiral formulas are independently reconstructed in Q^4; the old
SUCC rank-two module remains the authoritative historical provenance.
No proof of pi normality or effective real-circle spectral gap is claimed.
"""
from dataclasses import dataclass
from fractions import Fraction as F

SOURCE_TAG = "original-four-pole-BBP-chiral-rank2-source-v1"
ZERO = F(0)
ONE = F(1)


def e2_step(vector):
    """E+/E- rational-block bases: G and conjugating H, rank Q=4."""
    a, b, c, d = (F(x) for x in vector)
    return ((a-b)/2, (a+b)/2, d, c/2)


def e2_chirality(vector):
    a, b, c, d = (F(x) for x in vector)
    return (a, b, -c, -d)


def e2_shell():
    """Paired original impulse shell, plus individually signed chiral taps."""
    vector = (ONE, ZERO, ONE, ZERO)
    even, odd = [], []
    for _ in range(8):
        even.append(4*vector[0]); odd.append(-4*vector[3])
        vector = e2_step(vector)
    return tuple(even), tuple(odd)


EVEN, ODD = e2_shell()
TAPS = tuple(e+o for e, o in zip(EVEN, ODD))


def gamma_gain_unit_frequency():
    """Gamma(1,1) characteristic multiplier at +angular frequency 1."""
    return (F(1,2),F(1,2))  # real/imag; 1/(1-i) = (1+i)/2


def original_r(n):
    if n<1 or type(n) is not int:
        raise ValueError('n positive integer')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def clock_update(q):
    q = F(q)
    if not ZERO<=q<=ONE: raise ValueError('q in [0,1]')
    return q/(1+q)


def at_grade(q,n):
    if n<0 or type(n) is not int:raise ValueError('n nonnegative integer')
    q=F(q)
    if not ZERO<=q<=ONE:raise ValueError('q in [0,1]')
    return q/(1+n*q)


def source_field(q, channel='full'):
    """Time-independent Mellin readout r(n+1)=R(1/(n+1))."""
    q=F(q)
    if not ZERO<=q<=ONE:raise ValueError('q in [0,1]')
    if channel=='even': taps=EVEN
    elif channel=='odd': taps=ODD
    elif channel=='full': taps=TAPS
    else:raise ValueError('channel must be full, even, odd')
    return sum((c*q/F(8+(j-7)*q) for j,c in enumerate(taps)), ZERO)


def miller_beta_r(n):
    """Independent exact original BBP moment from eight chiral taps."""
    if n<1 or type(n) is not int:raise ValueError('n positive integer')
    return sum((c/F(8*(n-1)+j+1) for j,c in enumerate(TAPS)),ZERO)


@dataclass(frozen=True)
class SourceReceipt:
    label: str
    channel: str
    clock: F
    value: F


def emit(q,channel):
    if channel not in ('even','odd'):raise ValueError('one chiral lane required')
    return SourceReceipt(SOURCE_TAG,channel,F(q),source_field(q,channel))


@dataclass(frozen=True)
class EObserver:
    """E fixed receiver: no external grade/time index or evolving operator.

    q=1/(n+1), p=16^-n, a_even + a_odd=alpha_n.
    The exact rational BIT HEIGHT grows with n: fixed DIMENSION != bounded memory.
    """
    q:F=ONE
    p:F=ONE
    a_even:F=ZERO
    a_odd:F=ZERO

    def receive(self,a:SourceReceipt,b:SourceReceipt):
        if (a.label!=SOURCE_TAG or b.label!=SOURCE_TAG or
            a.channel!='even' or b.channel!='odd' or
            a.clock!=self.q or b.clock!=self.q or
            a.value!=source_field(self.q,'even') or
            b.value!=source_field(self.q,'odd')):
            raise ValueError('rejected unverified or unpaired E-tower field receipt')
        return EObserver(clock_update(self.q),self.p/16,
                         self.a_even+self.p*a.value/16,
                         self.a_odd+self.p*b.value/16)

    def update(self):
        return self.receive(emit(self.q,'even'),emit(self.q,'odd'))

    @property
    def alpha(self):return self.a_even+self.a_odd

    @property
    def original_U(self):return self.alpha/self.p

    @property
    def circle_phase(self):return self.original_U%1


def observer_at(n):
    if type(n) is not int or n<0:raise ValueError('n nonnegative integer')
    o=EObserver()
    for _ in range(n):o=o.update()
    return o


def static_source_step(x,q):
    """Autonomous rational skew product (phase, compact grade clock)."""
    return (16*F(x)+source_field(q))%1,clock_update(q)


def tau_partial(q,depth):
    """Finite rational Gamma-corrector field, exact at each cutoff."""
    if type(depth) is not int or depth<0:raise ValueError('depth>=0 integer')
    q=F(q)
    if not ZERO<=q<=ONE:raise ValueError('q in [0,1]')
    total=ZERO;radix=16
    for _ in range(depth):
        total+=source_field(q)/radix
        q=clock_update(q)
        radix*=16
    return total


def tau_remaining_bound(q,depth):
    """Universal rigorous error: 0<=tau(q)-tau_depth(q)<=this Fraction.

    Uses P(t)=(1-t)(t²+2)(t²+2t+2)<=15(1-t),
    source_field(q)<=15*q²/2, and sum_{j>=1}16^-j=1/15.
    """
    if type(depth) is not int or depth<0:raise ValueError('depth>=0 integer')
    t=at_grade(q,depth)
    return (t*t)/(2*16**depth)


def finite_intertwiner_residual(q,depth):
    """EXACT H_B S minus (T16 x g) H_B, independent of input phase x.

    Equals +16^-B * source_field(g^B q), hence is nonnegative.
    For B=0, the finite corrector is identically 0.
    """
    q=F(q)
    return source_field(q)+tau_partial(clock_update(q),depth)-16*tau_partial(q,depth)


def finite_intertwiner_expected(q,depth):
    return source_field(at_grade(q,depth))/16**depth


def e2_complete(B):
    """Stationary finite E2 spectral sum: alpha_B = (1/16)sum_{m<8B} c_m/(m+1)."""
    if B<0 or type(B) is not int:raise ValueError('B>=0')
    return sum((c/F(16**(k+1)*(8*k+j+1))
                for k in range(B) for j,c in enumerate(TAPS)), ZERO)


def e2_channel_complete(B, channel):
    if B<0 or type(B) is not int:raise ValueError('B>=0')
    taps=EVEN if channel=='even' else ODD if channel=='odd' else None
    if taps is None:raise ValueError('channel even or odd')
    return sum((c/F(16**(k+1)*(8*k+j+1))
                for k in range(B) for j,c in enumerate(taps)), ZERO)


def source_alpha_B(B):
    if B<0 or type(B) is not int:raise ValueError('B>=0')
    return sum((original_r(n)/16**n for n in range(1,B+1)),ZERO)


def full_finite_seam(n,B):
    """For integer n<=B, R_{n,B}=tau_{B-n}(1/(n+1))."""
    if type(n) is not int or type(B) is not int or not 0<=n<=B:
        raise ValueError('0<=n<=B')
    return tau_partial(F(1,n+1),B-n)


def first_shell_invariants():
    return {'even_mass':sum(EVEN,ZERO), 'odd_mass':sum(ODD,ZERO),
            'total_mass':sum(TAPS,ZERO),
            'first_moment':sum((j*c for j,c in enumerate(TAPS)), ZERO)}
