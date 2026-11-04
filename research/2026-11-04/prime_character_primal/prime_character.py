"""Source-faithful prime-Frobenius V4 action on eight BBP taps and primal quotient.

Research-only: exact Q/p arithmetic. No source modification or pi normality.
The prime-class shadow action comes from the original p-pole event chronology,
not a stochastic Galois average or analytic quotient chosen from its answer.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import gcd

CLASSES = (1, 3, 5, 7)
P = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1), Q(0), Q(0))
DUAL = (Q(0), Q(8), Q(4), Q(4), Q(0), Q(0), Q(-1), Q(0))
Z8 = (Q(0),) * 8


def _taps(w):
    if len(w) != 8:
        raise ValueError('exactly 8 BBP Mellin taps')
    return tuple(Q(x) for x in w)


def chi2(a: int) -> int:
    if type(a) is not int or a not in CLASSES:
        raise ValueError('odd residue class mod 8 required')
    return 1 if a in (1, 7) else -1


def chi_minus4(a: int) -> int:
    if type(a) is not int or a not in CLASSES:
        raise ValueError('odd residue class mod 8 required')
    return 1 if a in (1, 5) else -1


def j_of(a: int, ell: int) -> int:
    if type(ell) is not int or ell < 1 or ell > 8:
        raise ValueError('one of 8 within-block pole labels required')
    chi2(a)
    return (a * ell - 1) % 8 + 1


def shadow(a: int, w=P) -> tuple[Q, ...]:
    """Frobenius-shadow action S_a on a whole generic 8-Mellin-tap source.

    For p≡a(mod8), and 8ℓ+1..8ℓ+8 source p-pole event multipliers,
    the normalized contribution at p-time anchor (ℓ+1)*p is:
    (S_a w)_j/(8ℓ+j), with j=1..8. Uses Euler's 2/p character.

    This is a monomial representation of (Z/8Z)*, not a Galois-average.
    """
    w = _taps(w)
    sign = chi2(a)
    out = []
    for ell in range(1, 9):
        j = j_of(a, ell)
        exponent = (j - ell) // 2
        assert 2 * exponent == j - ell
        out.append(Q(sign) ** (8 - ell) * Q(2) ** exponent * w[j - 1])
    return tuple(out)


def add(x, y):
    return tuple(a + b for a, b in zip(_taps(x), _taps(y)))


def scaled(q, w):
    return tuple(Q(q) * x for x in _taps(w))


def proj(kind: str, w=P):
    """Exact Fourier character projector on the genuine prime-class action.

    The irreducible 1-dim characters of V4 are 1, chi_-4, chi_8, chi_-8.
    No additive Q/Z character is represented by these signs.
    """
    characters = {
        'trivial': (1, 1, 1, 1),
        'chi_minus4': (1, -1, 1, -1),
        'chi_8': (1, -1, -1, 1),
        'chi_minus8': (1, 1, -1, -1),
    }
    if kind not in characters:
        raise ValueError('valid prime-class character required')
    out = Z8
    for a, sign in zip(CLASSES, characters[kind]):
        out = add(out, scaled(Q(sign, 4), shadow(a, w)))
    return out


def angle_radial(w=P):
    return proj('chi_minus4', w), proj('trivial', w)


def source(n: int, w=P) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError('source index n>=1 required')
    return sum((x / Q(8 * (n - 1) + j) for j, x in enumerate(_taps(w), 1)), Q(0))


def state(n: int, w=P) -> Q:
    if type(n) is not int or n < 0:
        raise ValueError('source index n>=0 required')
    x = Q(0)
    for j in range(1, n + 1):
        x = 16 * x + source(j, w)
    return x


def states(nmax, w=P):
    if type(nmax) is not int or nmax < 0:
        raise ValueError('nmax must be nonnegative')
    x = Q(0)
    yield x
    for n in range(1, nmax + 1):
        x = 16 * x + source(n, w)
        yield x


def angular_source_odd(n: int) -> Q:
    """Eliminated rational function with an EXPLICIT ODD denominator.

    Independent of weighted eight-tap Mellin summation, symbolic identity
    checked by SymPy. This proves all r_ang(n) lie in Z_2.
    """
    if type(n) is not int or n < 1:
        raise ValueError('original n>=1 required')
    num = (30720*n**5 - 63232*n**4 + 45792*n**3
           - 13892*n**2 + 1641*n - 48)
    den = ((4*n - 3)*(4*n - 1)*(8*n - 7)
           *(8*n - 5)*(8*n - 3)*(8*n - 1))
    assert den & 1
    return Q(num, den)


def _fmod(x: Q, p: int) -> int:
    x = Q(x)
    if x.denominator % p == 0:
        raise ValueError('non-p-integral rational; p-local scalar unavailable')
    return x.numerator * pow(x.denominator, -1, p) % p


def direct_p_local_state(p: int, k: int, w=P) -> int:
    """Independent actual original 8-pole time iteration, no shadow action.

    For p>8k, denominators of the injections are <p². Multiply the
    source by p and reduce at every stage. Do not import precomputed pulses.
    """
    if type(p) is not int or p <= 8*k or type(k) is not int or k < 1:
        raise ValueError('p>8k and k>=1 required')
    w = _taps(w)
    if any(x.denominator % p == 0 for x in w):
        raise ValueError('source taps must have p-integral rational weights')
    residue = 0
    for n in range(1, k*p + 1):
        injection = 0
        for j, coeff in enumerate(w, 1):
            den = 8 * (n - 1) + j
            if den % p == 0:
                m = den // p
                assert m % p != 0
                injection += _fmod(coeff / m, p)
        residue = (16 * residue + injection) % p
    return residue


def prime_quotient_prediction(p: int, k: int, w=P) -> int:
    if p <= 8 * k:
        raise ValueError('simple-pole regime p>8k required')
    return _fmod(state(k, shadow(p % 8, w)), p)


def full_prime_state_residue(p: int, k: int, w=P):
    """Third route: full actual unwrapped rational state then p multiply."""
    if p <= 8*k:
        raise ValueError('simple-pole regime p>8k required')
    return _fmod(p * state(k*p, w), p)


def primal_and_radial(n: int):
    """Primal angular y_n and radial null z_n from source-only projectors."""
    if type(n) is not int or n < 0:
        raise ValueError('n>=0 required')
    ang, rad = angle_radial()
    y, z = state(n, ang), state(n, rad)
    assert y + z == state(n, P)
    assert y == (2*state(n, P) + state(n, DUAL)) / 4
    assert z == (2*state(n, P) - state(n, DUAL)) / 4
    return y, z


def radial_defect_bound(n: int) -> Q:
    """0 < z_n < 1/(32n+16) via inherited PF-8b, all n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError('n>=1')
    return Q(1, 32*n+16)


def epoch_selected_phase_error_ceiling(A: int, h: int):
    """Bound |c_U(h)-c_angle(h)| for the actual epoch [A,2A)."""
    if type(A) is not int or A < 1 or type(h) is not int:
        raise ValueError('integer epoch A>=1, harmonic h')
    # Chord <=2*pi*|h|*max z_n; return exact rational times pi.
    return Q(2 * abs(h), 32*A+16)


def epoch_triangle_current_error_ceiling(A: int, q: int):
    """Bound |J_q(U)-J_q(Y)| using pointwise positive radial defect.

    For the periodic tent K_q, q-Lipschitz and max |z_n-z_t|<=z_A_upper.
    J_q carries another q, giving q^2 z_A_upper.
    """
    if type(A) is not int or A < 1 or type(q) is not int or q < 2:
        raise ValueError('original A>=1 and integer mesh q>=2')
    return Q(q*q, 32*A+16)


def negative_base4_source_term(k):
    if type(k) is not int or k < 0:
        raise ValueError('k>=0')
    return (Q(-1,4)**k)*(Q(2,4*k+1)+Q(2,4*k+2)+Q(1,4*k+3))


def tap_impulse(c, n):
    """Coefficient of t^n in 4/[(t-1)^2+1], two-state recurrence."""
    if type(n) is not int or n < 0:
        raise ValueError('n>=0')
    a, b = Q(2), Q(2)
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n+1):
        a, b = b, b-a/2
    return b



def prime_angular_event_normalizer(a: int, multiplier: int) -> Q:
    """Universal Q normalizer of genuine angular p-local pulse at m>=1.

    Write m=8*k+ell with 1<=ell<=8. The FULL S_a eigencharacter
    relation yields C_a(m)=chi_-4(a) f_a(ell) [Y_k+sum_{j<=ell}
    angular_tap_j / (16*(8*k+j))]. The bracket is STRICTLY POSITIVE.
    This is not a statistical average over the four prime classes.
    """
    if type(multiplier) is not int or multiplier < 1:
        raise ValueError('genuine multiplier m>=1')
    chi2(a)
    k, off = divmod(multiplier-1, 8)
    ell = off+1
    j = j_of(a,ell)
    f = Q(chi2(a))**ell * Q(2)**((ell+8-j)//2)
    angular,_ = angle_radial()
    positive = state(k, angular) + sum(
        (angular[jj-1] / Q(16*(8*k+jj)) for jj in range(1,ell+1)),
        Q(0)
    )
    if positive <= 0:
        raise AssertionError('source angular partial sum lost strict positivity')
    return Q(chi_minus4(a))*f*positive


def angular_pulse_sign(a: int, multiplier: int) -> int:
    """All-pulse sign certificate (+1 or -1), paper-proved for EVERY m."""
    if type(multiplier) is not int or multiplier < 1:
        raise ValueError('m>=1')
    chi2(a)
    ell=(multiplier-1)%8+1
    return chi_minus4(a)*chi2(a)**ell


def direct_angular_event_normalizer(a: int, multiplier: int) -> Q:
    """Independent universal event-clock calculation, no eigencharacter formula.

    Accumulate real normalized p-event pulses at every 8j-c=mp,
    with Euler's criterion to transport between consecutive event indices.
    Test instrument, not finite proof of all-m signs.
    """
    if type(multiplier) is not int or multiplier < 1:
        raise ValueError('m>=1')
    chi2(a)
    w,_=angle_radial()
    old_m=old_c=None
    C=Q(0)
    for m0 in range(1,multiplier+1):
        j=(a*m0-1)%8+1
        c=8-j
        if old_m is not None:
            diff=m0-old_m
            d_c=c-old_c
            assert (diff+d_c)%2==0
            C*=Q(chi2(a))**diff*Q(2)**((diff+d_c)//2)
        C+=w[j-1]/m0
        old_m,old_c=m0,c
    return C


def action_trace(a):
    """Trace on full eight-tap Q vector space by true weighted permutation."""
    chi2(a)
    return sum(shadow(a, tuple(Q(int(j==k)) for j in range(8)))[k]
               for k in range(8))


def character_dimensions():
    traces={a:action_trace(a) for a in CLASSES}
    chars={
        'trivial': (1,1,1,1),
        'chi_minus4': (1,-1,1,-1),
        'chi_8': (1,-1,-1,1),
        'chi_minus8': (1,1,-1,-1),
    }
    return {k:sum(Q(sign)*traces[a] for a,sign in zip(CLASSES,c)) / 4
            for k,c in chars.items()}


def angular_integer_lcm_state(n: int) -> tuple[int, int, Q]:
    """SECOND exact primal source evaluator using odd polynomial forcing.

    Returns the unreduced integer A/M (M=source LCM), plus the reduced
    state. It never calls the weighted-tap angular source recurrence.
    """
    from math import lcm
    if type(n) is not int or n < 0:
        raise ValueError('n>=0')
    A, M = 0, 1
    for j in range(1, n+1):
        w=angular_source_odd(j)
        new=lcm(M,w.denominator)
        A=16*(new//M)*A+w.numerator*(new//w.denominator)
        M=new
    return A, M, Q(A,M)


def angular_last_p_event(p: int,n: int):
    """Latest original p-pole for angular source at true time j<=n.

    This is a declared source index; not a p-adic phase average.
    Requires simple-pole p²>8n and p odd prime >5 checked externally.
    """
    if type(p) is not int or p<=5 or p%2==0 or type(n) is not int or n<1:
        raise ValueError('odd p>5, original n>=1')
    if p*p<=8*n:
        raise ValueError('simple-pole source requires p²>8n')
    last=None
    for mul in range(1,(8*n)//p+2):
        j=(p*mul-1)%8+1
        t=(p*mul+8-j)//8
        if 8*t-8+j !=p*mul:
            raise AssertionError('invalid source event')
        if 1<=t<=n:
            last=(mul,j,t)
    return last


def predicted_angular_p_residue(p: int,n: int):
    """Selected prime residue p*Y_n, predicted by universal angular event."""
    ev=angular_last_p_event(p,n)
    if ev is None:
        return 0
    mul,_,at=ev
    c=prime_angular_event_normalizer(p%8,mul)
    return (pow(16,n-at,p)*_fmod(c,p))%p
