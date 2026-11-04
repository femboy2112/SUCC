"""Exact categorical reconstruction of the original BBP minimal rational transfer.

This is a read-only research instrument. It neither replaces the original
four signed BBP Mellin terms nor alters the zero-seeded U recurrence.
All certificates below use Q arithmetic, with no approximation or pi digits.
"""
from __future__ import annotations
from fractions import Fraction as Q

ZERO = (Q(0),)*4
ONE = (Q(1), Q(0), Q(0), Q(0))
U = (Q(0), Q(1), Q(0), Q(0))
# m(u) = u**4-u**3+u/2-1/4; u**4=u**3-u/2+1/4.
M_COEFF = (Q(-1, 4), Q(1, 2), Q(0), Q(-1), Q(1))
UNIT_WEIGHT = (Q(-1), Q(2), Q(2), Q(-8))
TAPS = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1), Q(0), Q(0))
# t*(1-t)^2*D_cancel(t), with D_cancel=(1+t^2/2)(1+t+t^2/2).
MUTATION_TAPS = (Q(0), Q(1), Q(-1), Q(0), Q(-1,2), Q(1,4), Q(0), Q(1,4))


def el(*a):
    """Polynomial in u reduced to the unique 4-element Q-basis."""
    z = [Q(x) for x in a] or [Q(0)]
    while len(z) < 4:
        z.append(Q(0))
    for k in range(len(z)-1, 3, -1):
        v = z[k]
        z[k] = Q(0)
        z[k-4] += v/4
        z[k-3] -= v/2
        z[k-1] += v
    return tuple(z[:4])


def add(a, b):
    return tuple(Q(x)+Q(y) for x, y in zip(a, b))


def scale(a, q):
    q = Q(q)
    return tuple(q*x for x in a)


def mul(a, b):
    z = [Q(0)]*7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return el(*z)


def power(a, n):
    if type(n) is not int or n < 0:
        raise ValueError('nonnegative integer exponent required')
    b = ONE
    while n:
        if n % 2:
            b = mul(b, a)
        a = mul(a, a)
        n //= 2
    return b


def trace(a):
    """Regular trace A/Q, computed as trace of multiplication-by-a."""
    return sum(mul(a, el(*(int(j==k) for j in range(4))))[k]
               for k in range(4))


def readout(a):
    return trace(mul(UNIT_WEIGHT, a))


def involution():
    """Four-step central sign operator, C=4u^4, splitting both atoms."""
    return scale(power(U,4), 4)


def projectors():
    c = involution()
    return scale(add(ONE,c),Q(1,2)), scale(add(ONE,scale(c,-1)),Q(1,2))


def unit_complex_structure():
    """Within the Gaussian factor: j_G=2u^2 e_G, j_G^2=-e_G."""
    _, eg = projectors()
    return mul(scale(power(U,2),2),eg)


def impulse(n):
    if type(n) is not int or n < 0:
        raise ValueError('n nonnegative integer')
    return readout(power(U,n))


def impulse_closed(n):
    if type(n) is not int or n < 0:
        raise ValueError('n nonnegative integer')
    k, j = divmod(n, 8)
    return TAPS[j]/16**k


def channel_impulses(n):
    """Unobserved two channels, recovered canonically from 4-step samples."""
    eh, eg = projectors()
    un = power(U,n)
    return readout(mul(eh,un)), readout(mul(eg,un))


def channel_impulses_from_scalar(n):
    c, c4 = impulse_closed(n), impulse_closed(n+4)
    return (c+4*c4)/2, (c-4*c4)/2


def mellin_channels(n):
    """Mellin moments of the CANONICAL spectral-sector 8-step taps.

    Returns real-quadratic r_H(n) and Gaussian r_G(n), with rational values.
    They have opposite 2-adic poles at index 0 and sum to the integral
    original four-pole source. Do not reduce their residues separately.
    """
    if type(n) is not int or n<1:
        raise ValueError('source time n>=1')
    htaps=tuple(channel_impulses_from_scalar(k)[0] for k in range(8))
    gtaps=tuple(channel_impulses_from_scalar(k)[1] for k in range(8))
    def moment(taps):
        return sum((v/Q(8*(n-1)+k+1) for k,v in enumerate(taps)),Q(0))
    return moment(htaps), moment(gtaps)


def v2_rational(x):
    x=Q(x)
    if not x:
        return None  # infinity for exact zero; not assigned a finite valuation
    def v(n):
        n=abs(n); k=0
        while n%2==0:
            n//=2;k+=1
        return k
    return v(x.numerator)-v(x.denominator)


def source_channel_states(last_n):
    """Zero-seeded unwrapped quadratic channel states, not phase-averaged."""
    if type(last_n) is not int or last_n<0:
        raise ValueError('last_n>=0')
    a=b=Q(0)
    out=[(a,b)]
    for n in range(1,last_n+1):
        rh,rg=mellin_channels(n)
        a=16*a+rh
        b=16*b+rg
        out.append((a,b))
    return tuple(out)


def original_four_poles(n):
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return (Q(4,8*n-7)-Q(2,8*n-4)
            -Q(1,8*n-3)-Q(1,8*n-2))


def mellin_from_eight_taps(n):
    """Moment of P(t), NOT moment of K(t); preserves BBP source indices."""
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return sum((v/Q(8*(n-1)+k+1) for k,v in enumerate(TAPS)), Q(0))


def fractional_source_states(last_n):
    """Original exactly zero-seeded BBP recurrence, real fractional observations."""
    if type(last_n) is not int or last_n < 0:
        raise ValueError('last_n nonnegative')
    u = Q(0)
    out = [u]
    for n in range(1,last_n+1):
        u = (16*u + mellin_from_eight_taps(n)) % 1
        out.append(u)
    return tuple(out)


def hankel_four():
    return tuple(tuple(impulse_closed(i+j) for j in range(4)) for i in range(4))


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    if n == 0 or any(len(row)!=n for row in a):
        raise ValueError('square matrix required')
    sign, det = Q(1), Q(1)
    for k in range(n):
        pivot = next((j for j in range(k,n) if a[j][k]),None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        q = a[k][k]
        det *= q
        for i in range(k+1,n):
            f = a[i][k]/q
            for j in range(k+1,n):
                a[i][j] -= f*a[k][j]
            a[i][k] = Q(0)
    return sign*det


def frobenius_pairing(a,b):
    """Nondegenerate symmetric associative Frobenius form ell(a*b)."""
    return readout(mul(a,b))


def frobenius_gram():
    return hankel_four()


def gram_inverse():
    g = [[Q(x) for x in row] for row in frobenius_gram()]
    n=len(g)
    a=[g[i]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:raise ArithmeticError('degenerate Frobenius pairing')
        a[k],a[pivot]=a[pivot],a[k]
        t=a[k][k]
        a[k]=[v/t for v in a[k]]
        for i in range(n):
            if i!=k:
                b=a[i][k]
                a[i]=[a[i][j]-b*a[k][j] for j in range(2*n)]
    return tuple(tuple(row[n:]) for row in a)


def frobenius_handle():
    """mu Delta(1) from the Gram-dual bases, equals w**(-1)."""
    inv=gram_inverse()
    out=ZERO
    for i in range(4):
        for j in range(4):
            out=add(out,scale(power(U,i+j),inv[i][j]))
    return out


def sqrt2_extension_mul(x,y):
    """(a+b sqrt2)(c+d sqrt2), with a,b,c,d in the rational algebra."""
    a,b = x; c,d = y
    return add(mul(a,c),scale(mul(b,d),2)), add(mul(a,d),mul(b,c))


def sqrt2_extension_power(x,n):
    if type(n) is not int or n<0:
        raise ValueError('nonnegative exponent')
    r = (ONE,ZERO)
    while n:
        if n&1:
            r = sqrt2_extension_mul(r,x)
        x = sqrt2_extension_mul(x,x)
        n//=2
    return r


def normalized_unit():
    """v=sqrt2*u has exact order 8 over Q(sqrt2)."""
    return ZERO,U


def mutated_mellin_source(n, epsilon=Q(1,8)):
    """Changed Mellin forcing with same 8-clock, c0 and endpoint first jet.

    Delta P(t)=epsilon*t*(1-t)^2*(1+t^2/2)*(1+t+t^2/2).
    Positive integral shift epsilon*67/480, and ΔP(0)=ΔP(1)=ΔP'(1)=0.
    CHANGES original source and its completed constant; never a pi source.
    """
    if type(n) is not int or n < 1:
        raise ValueError('n>=1')
    epsilon=Q(epsilon)
    return original_four_poles(n)+epsilon*sum((v/Q(8*(n-1)+j+1) for j,v in enumerate(MUTATION_TAPS)), Q(0))


def mutated_constant_shift(epsilon=Q(1,8)):
    """Exact integral of changed kernel delta K on [0,1]."""
    return Q(epsilon)*Q(67,480)


def changed_source_probe(n, epsilon=Q(1,8)):
    """Explicit same two atoms and eight-return, changed scalar readout.

    K_e(t) = [4(1-t)+eps*t*(1-t)^2]/D_min(t).
    Its original c0=4 and endpoint K-numerator derivative remain unchanged;
    its moment-integrated source is NOT the original four Mellin-pole forcing.
    Readout is reconstructed from its initial four Markov moments.
    """
    if type(n) is not int or n < 0:
        raise ValueError('n nonnegative')
    epsilon=Q(epsilon)
    # delta K(t) = eps*(t-2t²+t³)/D_min(t).
    # D_min inverse: 1+t+t²+1/2*t³+... ; first four delta c=(0,eps,-eps,0).
    delta=(Q(0),epsilon,-epsilon,Q(0))
    if n < 4:
        return impulse_closed(n)+delta[n]
    # All delta c_n satisfy D_min annihilator after the first 4 terms.
    c=list(delta)
    for j in range(4,n+1):
        c.append(c[j-1]-c[j-3]/2+c[j-4]/4)
    return impulse_closed(n)+c[n]


def exact_certificate():
    eh,eg=projectors()
    c=involution()
    j=unit_complex_structure()
    return {
      'minimal_polynomial': M_COEFF,
      'hankel_det':determinant(hankel_four()),
      'hankel_matrix':hankel_four(),
      'u_eighth_scalar':power(U,8)==scale(ONE,Q(1,16)),
      'half_clock_c_squared':mul(c,c)==ONE,
      'projectors_sum':add(eh,eg)==ONE,
      'projectors_idempotent':mul(eh,eh)==eh and mul(eg,eg)==eg,
      'projectors_orthogonal':mul(eh,eg)==ZERO,
      'projector_H_minpoly':mul(eh,add(power(U,2),scale(ONE,-Q(1,2))))==ZERO,
      'projector_G_minpoly':mul(eg,add(add(power(U,2),scale(U,-1)),scale(ONE,Q(1,2))))==ZERO,
      'i_G_squared_minus':mul(j,j)==scale(eg,-1),
      'w_H':mul(UNIT_WEIGHT,eh)==mul(scale(U,-2),eh),
      'w_G':mul(UNIT_WEIGHT,eg)==scale(eg,2),
      'eH_coefficients':eh,'eG_coefficients':eg,
      'i_G_coefficients':j,'trace_weight':UNIT_WEIGHT,
      'v8_equals_1':sqrt2_extension_power(normalized_unit(),8)==(ONE,ZERO),
      'v4_equals_C':sqrt2_extension_power(normalized_unit(),4)==(c,ZERO),
      'v4_not_identity':c!=ONE,
      'first8':tuple(impulse(k) for k in range(8)),
      'channels8':tuple(channel_impulses(k) for k in range(8)),
      'channels8_from_scalar':tuple(channel_impulses_from_scalar(k) for k in range(8)),
      'mutant_c0_equal':changed_source_probe(0)==impulse_closed(0),
      'mutant_c1_different':changed_source_probe(1)!=impulse_closed(1),
      'mutant_endpoint_value_zero':sum(MUTATION_TAPS)==0,
      'mutant_endpoint_first_jet_zero':sum(j*v for j,v in enumerate(MUTATION_TAPS))==0,
      'mutant_constant_shift':mutated_constant_shift(),
      'mellin_at_1':mellin_channels(1),
      'mellin_at_2':mellin_channels(2),
      'source_2adic_depths_1to32':tuple((n,v2_rational(mellin_channels(n)[0]),v2_rational(mellin_channels(n)[1])) for n in range(1,33)),
      'frobenius_handle':frobenius_handle(),
      'handle_times_weight_one':mul(frobenius_handle(), UNIT_WEIGHT)==ONE,
      'claims_pi_normality':False,
    }
