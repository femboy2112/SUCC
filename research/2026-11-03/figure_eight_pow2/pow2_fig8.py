"""Authentic BBP chiral eight/16/32-step and 2-adic index gluing.

Preserves the original four signed BBP poles and the literal U0=0.
Every integer/fraction computation exact; no π digits or random digits.
Old SUCC E² G/H, main 2-adic F isometry, and #481 2-adic lane
valuation are existing theorems. This module probes NEW composite
consequences and source-specific Hensel position; π-normality OPEN.
"""
from fractions import Fraction as F

PLUS = tuple(map(F, (4,2,0,-1,-1)))+(F(-1,2),F(0),F(1,4))
MINUS = (F(0),F(-2),F(0),F(-1),F(0),F(-1,2),F(0),F(-1,4))
TAPS = tuple(a+b for a,b in zip(PLUS,MINUS))

G=((F(1,2),F(-1,2)),(F(1,2),F(1,2)))
H=((F(0),F(1)),(F(1,2),F(0)))
T=tuple(tuple((G[i][j] if i<2 and j<2 else
              H[i-2][j-2] if i>=2 and j>=2 else F(0))
              for j in range(4)) for i in range(4))
CHI=tuple(tuple(F((1 if i<2 else -1) if i==j else 0)
                for j in range(4)) for i in range(4))
IDENT=tuple(tuple(F(i==j) for j in range(4)) for i in range(4))


def matmul(a,b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matpower(a,n):
    if type(n) is not int or n<0:raise ValueError('nonnegative integer power')
    out=IDENT
    while n:
        if n&1:out=matmul(out,a)
        a=matmul(a,a);n>>=1
    return out


def power_of_two_clock(k):
    if type(k) is not int or k<0:raise ValueError('k>=0 integer')
    return matpower(T,1<<k)


def expected_clock(k):
    if type(k) is not int or k<2:raise ValueError('k>=2')
    if k==2:return tuple(tuple(-x/4 for x in row) for row in CHI)
    scalar=F(1,16**(1<<(k-3)))
    return tuple(tuple(scalar*x for x in row) for row in IDENT)


def source_numerator(n):return 120*n*n-89*n+16


def source_denominator(n):return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def source_fraction(n):
    if type(n) is not int or n<1:raise ValueError('positive original BBP source index')
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def source_collapsed(n):
    if type(n) is not int:raise ValueError('integer source index')
    return F(source_numerator(n),source_denominator(n))


def channel(n,taps):
    if type(n) is not int or n<1:raise ValueError('positive source index')
    return sum((c/F(8*(n-1)+j+1) for j,c in enumerate(taps)),F(0))


def v2_int(n):
    if not isinstance(n,int) or n==0:raise ValueError('nonzero integer')
    a=abs(n)
    return (a&-a).bit_length()-1


def v2_rat(n):
    q=F(n)
    if q==0:raise ValueError('nonzero rational')
    return v2_int(q.numerator)-v2_int(q.denominator)


def hensel_simple_root(bits):
    """Only Q(t)=120t²-89t+16 zero mod 2^bits, via derivative odd."""
    if type(bits) is not int or bits<1:raise ValueError('bits>=1')
    root=0
    for k in range(1,bits):
        if source_numerator(root)%(1<<(k+1)):
            root+=1<<k
        assert source_numerator(root)%(1<<(k+1))==0
    return root


def residue_count(start,length,bits):
    if type(start) is not int or type(length) is not int or length<0:
        raise ValueError('valid integer interval')
    if type(bits) is not int or bits<1:raise ValueError('bits>=1')
    m=1<<bits
    a=hensel_simple_root(bits)
    return (start+length-1-a)//m-(start-1-a)//m


def source_mod(n,bits):
    if type(n) is not int or type(bits) is not int or bits<1:
        raise ValueError('integer index and positive bit precision')
    m=1<<bits
    return source_numerator(n)*pow(source_denominator(n),-1,m)%m


def original_states(n):
    if type(n) is not int or n<0:raise ValueError('n>=0')
    out=[F(0)]
    for k in range(1,n+1):out.append(16*out[-1]+source_fraction(k))
    return out


def source_states_mod(last,bits):
    if type(last) is not int or last<0:raise ValueError('last>=0')
    if type(bits) is not int or bits<1:raise ValueError('bits>=1')
    m=1<<bits
    x=0;out=[x]
    for n in range(1,last+1):
        x=(16*x+source_mod(n,bits))%m
        out.append(x)
    return out


def p_adic_particular_mod(n,bits):
    if type(n) is not int or type(bits) is not int or bits<1:
        raise ValueError('integer index and bits>=1')
    m=1<<bits
    return sum((16**j*source_mod(n-j,bits) for j in range((bits+3)//4)))%m


def two_stage_power2(k):
    """Compare SOURCE chiral lane valuation, glued r, predecessor and state.

    Second stage uses the old exact U_n isometry (v2(U_n)=v2(n)),
    verified independently via the full rational source at small n.
    """
    if type(k) is not int or k<0:raise ValueError('k>=0')
    n=1<<k
    value=v2_int(source_numerator(n))
    lane=-5-k
    # For n>=2, n-1 odd and old SUCC v2(U_(n-1))=0.
    prev=4 if n>=2 else None
    return {'k':k,'n':n,'lane_v2':lane,'r_v2':value,
            'channel_to_source_bits':value-lane,
            'prev_16U_v2':prev,'selected_U_v2':k,
            'source_prev_to_state_bits':(k-4 if k>=5 else 0)}


def octaves(k):
    """Exact 2^k source microstep shell (k>=3) as K=2^(k-3) octaves."""
    if type(k) is not int or k<3:raise ValueError('at least eight steps required')
    blocks=1<<(k-3)
    arr=[F(0)]*(8*blocks)
    for b in range(blocks):
        for j,c in enumerate(TAPS):arr[8*b+j]=c/F(16**b)
    return tuple(arr)


def endpoint_jets(k):
    """Finite polynomial P_K(t)=sum_{m<2^k} c_m t^m at t=1."""
    arr=octaves(k)
    v=sum(arr,F(0))
    d1=sum((m*c for m,c in enumerate(arr)),F(0))
    d2=sum((m*(m-1)*c for m,c in enumerate(arr)),F(0))
    return v,d1,d2


def jet_gap(k):
    """F'_infinity(1)-P_K'(1)=-16^(1-K), K=# eight-tap blocks."""
    if type(k) is not int or k<3:raise ValueError('k>=3')
    blocks=1<<(k-3)
    return -F(16,16**blocks)


def completion(B,taps=TAPS):
    if type(B) is not int or B<0:raise ValueError('B>=0')
    return sum((channel(n,taps)/16**n for n in range(1,B+1)),F(0))


def finite_future(n,B):
    if type(n) is not int or type(B) is not int or not 0<=n<=B:
        raise ValueError('0<=n<=B')
    return sum((source_fraction(j)/16**(j-n) for j in range(n+1,B+1)),F(0))


def source_control_shadow(B):
    """Same source, distinct rational seed, finite completed orbit is 1/5."""
    a=completion(B)
    seed=F(1,5)-a
    states=original_states(B)
    return seed,[states[n]+16**n*seed+finite_future(n,B) for n in range(B+1)]


def finite_source_jet_expected(k):
    if k<3:raise ValueError('k>=3')
    blocks=1<<(k-3)
    return -16*(F(1)-F(1,16**blocks))
