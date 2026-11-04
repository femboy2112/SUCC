"""Exact ORIGINAL four-pole SUCC channel p=2 cocycle, not a real Weyl bound.

Source inputs: original BBP r(n), U0=0 and the canonical #481 Mellin sector
r_H, r_G. Principal2 returns a rational representative of Q_2/Z_2.
Only exact Python integer and Fraction arithmetic is used.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import lcm


def v2_integer(n: int) -> int | None:
    """v_2(n), with None representing infinite valuation at zero."""
    if type(n) is not int:
        raise ValueError('exact integer required')
    if n == 0:
        return None
    n = abs(n)
    return (n & -n).bit_length() - 1


def v2_rational(x: Q) -> int | None:
    x = Q(x)
    if not x:
        return None
    return v2_integer(x.numerator) - v2_integer(x.denominator)


def principal2(x: Q) -> Q:
    """Canonical [0,1) rational representative of the 2-primary class.

    If x=a/(2**d*q) in lowest terms, q odd, return (a*q^-1 mod 2**d)/2**d.
    This is NOT the real fractional part of x, except in special cases.
    """
    x = Q(x)
    if x == 0:
        return Q(0)
    k = v2_integer(x.denominator)
    if k == 0:
        return Q(0)
    mod = 1 << k
    odd = x.denominator >> k
    assert odd & 1
    return Q((x.numerator * pow(odd, -1, mod)) % mod, mod)


def depth2(x: Q) -> int:
    """Exact nonintegral 2-adic depth of a rational state."""
    v = v2_rational(x)
    return 0 if v is None or v >= 0 else -v


def original_r(n: int) -> Q:
    """Never edit these four signed BBP Mellin terms."""
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return (Q(4, 8*n-7)-Q(2, 8*n-4)
            -Q(1, 8*n-3)-Q(1, 8*n-2))


def real_source(n: int) -> Q:
    """Canonical Q(sqrt2) sector source from GR-06, zero seed."""
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return (-Q(1, 4*n-3)-Q(1,4*(2*n-1))
            -Q(1,4*(4*n-1))-Q(1,32*n))


def gaussian_source(n: int) -> Q:
    return original_r(n) - real_source(n)


def source_principal_binary(n: int) -> Q:
    """Source-specific parity/harmonic 2-primary injection exactly.

    q2(r_H(n)) = q2(-1/(32*n) + 1_{even n}/2).
    """
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return principal2(-Q(1,32*n)+(Q(1,2) if n%2 == 0 else Q(0)))


def source_depth_envelope(n: int) -> int:
    """B_n = 5+floor(log2 n), sharp at every n=2**k."""
    if type(n) is not int or n < 1:
        raise ValueError('source time n>=1')
    return 5 + n.bit_length() - 1


def source_memory_horizon(n: int) -> int:
    """At most ceil((5+floor(log2 n))/4) recent source terms matter in Q2/Z2."""
    return min(n, (source_depth_envelope(n)+3)//4)


def principal_short_cone(n: int, channel='H') -> Q:
    """Exact q2(U_n^channel) using O(log n) recent original source terms.

    For an enormous index n (say 2**100), this does not construct U_n.
    The complete previous contribution is 2-integral, hence q2-zero.
    """
    if type(n) is not int or n < 0:
        raise ValueError('source time n>=0')
    if channel not in ('H','G'):
        raise ValueError('original H or G channel required')
    if n == 0:
        return Q(0)
    total = Q(0)
    for d in range(source_memory_horizon(n)):
        # Each term is separately reduced AFTER its time-rescaled injection.
        val = (16**d) * (real_source(n-d) if channel=='H' else gaussian_source(n-d))
        total = (total + principal2(val)) % 1
    return total


def principal_harmonic_clock(n: int) -> Q:
    """Exact q2(U_H(n)) from W_n=16*W_(n-1)+1/n and parity only.

    Carries are in Q2/Z2, not ordinary real floor carries.
    """
    if type(n) is not int or n < 0:
        raise ValueError('source time n>=0')
    q = Q(0)
    for i in range(1,n+1):
        q = (16*q + principal2(-Q(1,32*i))) % 1
    if n%2==0 and n>0:
        q = (q + Q(1,2)) % 1
    return q


def principal_cocycle_stream(last: int):
    """Yield (n,q2(U_H(n)),q2(U_G(n))) from exact source recurrence."""
    if type(last) is not int or last < 0:
        raise ValueError('last>=0')
    h = Q(0)
    yield 0, h, h
    for n in range(1, last+1):
        h = (16*h + principal2(real_source(n))) % 1
        yield n, h, (-h) % 1


def anchor_principal(k: int) -> tuple[Q,Q]:
    """Exact all-k formula at n=2**k (k>=1)."""
    if type(k) is not int or k < 1:
        raise ValueError('k>=1')
    modulus = 1 << (k+5)
    return Q(modulus-1,modulus), Q(1,modulus)


def anchor_window_depth(k: int, d: int) -> int:
    """v2(U_H(2**k+d)) = v2(U_G(2**k+d)) = -(k+5-4*d).

    Domain: k>=1, d>=0, 5*d < k. Both channel states are nonintegral.
    """
    if type(k) is not int or type(d) is not int or k<1 or d<0 or 5*d>=k:
        raise ValueError('require k>=1, d>=0 and 5*d<k')
    return k+5-4*d


def odd_phase(x: Q) -> Q:
    """[0,1) sum of ALL odd-primary principal fractions, modulo 1.

    This is exactly (x - principal2(x)) mod 1 for rational x; no
    factorization of a potentially huge odd denominator is required.
    Not an independently sampled phase and not a real mixing theorem.
    """
    x = Q(x)
    return (x-principal2(x))%1


def glue_odd_character_phase(x: Q,y: Q) -> Q:
    """Original real phase from the two channels' selected odd components.

    Strictly require a legal 2-integral glued sum.
    """
    x,y=Q(x),Q(y)
    if v2_rational(x+y) is not None and v2_rational(x+y)<0:
        raise ValueError('the original two channels must cancel their 2-primary debt')
    assert (principal2(x)+principal2(y))%1==0
    ans=(odd_phase(x)+odd_phase(y))%1
    assert ans==(x+y)%1
    return ans


def real_binary_carry(x: Q,y: Q) -> int:
    """Ordinary REAL fractional addition carry. Do not identify with q2."""
    x,y=Q(x),Q(y)
    return int((x%1)+(y%1))


def full_zero_seed_channels(last_n: int):
    """Exact Fraction states for small/medium independent crosschecks."""
    if type(last_n) is not int or last_n<0:
        raise ValueError('last_n>=0')
    h,g,o=Q(0),Q(0),Q(0)
    yield 0,h,g,o
    for n in range(1,last_n+1):
        h=16*h+real_source(n)
        g=16*g+gaussian_source(n)
        o=16*o+original_r(n)
        if h+g!=o or depth2(o)!=0:
            raise AssertionError('source changed or 2-adic gluing failed')
        yield n,h,g,o


def scaled_sum_mod(x: Q,y: Q,k: int, B: int) -> int:
    """One sharp general gluing precision contract, NOT a real-phase decoder.

    For integral x+y and separately 2**B*x,2**B*y integral, exact scaled
    residues mod2**(k+B) suffice to reconstruct (x+y) mod2**k.
    """
    if type(k) is not int or type(B) is not int or k<1 or B<0:
        raise ValueError('k positive, B nonnegative')
    x,y=Q(x),Q(y)
    if depth2(x)>B or depth2(y)>B or depth2(x+y)>0:
        raise ValueError('illegal gluing precision or nonintegral result')
    modulus=1<<(k+B)
    def scaled(a):
        q=(1<<B)*a
        assert q.denominator%2
        return (q.numerator*pow(q.denominator,-1,modulus))%modulus
    total=(scaled(x)+scaled(y))%modulus
    assert total%(1<<B)==0
    return (total>>B)%(1<<k)


def precision_tax_witness(k:int,B:int):
    """Universal sharpness witness for needing k+B scaled bits.

    Both pairs have integral glued sum. The first has 0; the second has
    2**(k-1). Their scaled numerator residues AGREE modulo 2**(k+B-1).
    This is an informational negative, not an original BBP trajectory.
    """
    if type(k) is not int or type(B) is not int or k<1 or B<0:
        raise ValueError('k positive, B nonnegative')
    debt = Q(1,1<<B) if B else Q(0)
    a0,b0=-debt,debt
    a1,b1=Q(1<<(k-1))-debt,debt
    assert depth2(a0)==B and depth2(a1)==B and depth2(b0)==B
    assert scaled_sum_mod(a0,b0,k,B)!=scaled_sum_mod(a1,b1,k,B)
    modulus=1<<(k+B-1)
    assert ((1<<B)*a0-(1<<B)*a1).numerator%modulus==0
    return {'k':k,'B':B,'indistinguishable_scaled_modulus':modulus,
            'glued_first':0,'glued_second':1<<(k-1)}


def real_carry_cocycle(x: Q, y: Q) -> dict:
    """Exact source-compatible two-channel real vs odd-place carry interface.

    Valid for ANY rational pair whose sum is 2-integral. The original
    source H/G pair is a distinguished input, not an arbitrary gauge.

    delta=pp2(y), pp2(x)=(-delta) mod1,
    o_H=(x-pp2(x)) mod1, o_G=(y-pp2(y)) mod1.

    kappa_REAL-kappa_ODD = 1_{o_H<delta} - 1_{o_G>=1-delta}.
    No statistical bound on either indicator is inferred.
    """
    x,y=Q(x),Q(y)
    if depth2(x+y):
        raise ValueError('glued rational sum must be 2-integral')
    delta = principal2(y)
    if principal2(x)!=(-delta)%1:
        raise ArithmeticError('source gluing incompatible with principal classes')
    oh,og=odd_phase(x),odd_phase(y)
    lower=int(oh < delta)
    upper=int(og >= 1-delta)
    kr=real_binary_carry(x,y)
    ko=real_binary_carry(oh,og)
    if kr-ko != lower-upper:
        raise ArithmeticError('source-selected real carry identity failed')
    return {'dyadic_gaussian_part':delta,
            'real_channel_phase':x%1,'gaussian_channel_phase':y%1,
            'odd_real_part':oh,'odd_gaussian_part':og,
            'real_carry':kr,'odd_carry':ko,
            'odd_low_crossing':lower,'odd_high_crossing':upper,
            'carry_difference':kr-ko,
            'glued_real_phase':(x+y)%1,
            'glued_odd_phase':(oh+og)%1}


def coherent_odd_counterfeit(D: int, odd_phase=Q(2,5)) -> dict:
    """Preserve exact complementary 2-primary phase but force coherent REAL phase.

    A source-MUTATED cofactor, NOT the original BBP forcing or zero-seed.
    For each D>=4, choose pp2(H)=-1/2**D, pp2(G)=+1/2**D
    and constant odd phases 2/5,2/5. Both indicator counts are ZERO,
    while the selected glued real phase is identically 4/5.
    """
    if type(D) is not int or D < 4:
        raise ValueError('D>=4')
    odd_phase=Q(odd_phase)
    if odd_phase!=Q(2,5):
        raise ValueError('this hostile control is calibrated at 2/5')
    eps=Q(1,1<<D)
    x=-eps+odd_phase
    y=eps+odd_phase
    c=real_carry_cocycle(x,y)
    assert c['odd_low_crossing']==c['odd_high_crossing']==0
    assert c['glued_real_phase']==Q(4,5)
    return c


def full_zero_seed_modular(last_n: int):
    """Independent integer-only COMMON DENOMINATOR real-phase oracle.

    Compute the least common multiple of both authentic channel FORCING
    denominators through last_n. Exact integer state recurrences then return
    fractional phases without constructing enormous unwrapped Fractions.
    This and the previous Fraction evaluator have distinct arithmetic paths.
    """
    if type(last_n) is not int or last_n < 0:
        raise ValueError('last_n>=0')
    D=1
    for n in range(1,last_n+1):
        D=lcm(D,real_source(n).denominator,original_r(n).denominator)
    a=b=c=0
    yield 0,Q(0),Q(0),Q(0)
    for n in range(1,last_n+1):
        rh=real_source(n)
        rr=original_r(n)
        ih=rh.numerator*(D//rh.denominator)
        ir=rr.numerator*(D//rr.denominator)
        a=(16*a+ih)%D
        b=(16*b+ir-ih)%D
        c=(16*c+ir)%D
        if (a+b)%D!=c:
            raise AssertionError('modular channel gluing changed source')
        yield n,Q(a,D),Q(b,D),Q(c,D)


def carry_coboundary_step(n:int, prev_h:Q,prev_g:Q) -> dict:
    """EXACT 16-adic real floor-carry gluing, canonical forcing and marked time.

    For fractional source states x_H,x_G, define kappa=floor(x_H+x_G),
    original y=x_H+x_G-kappa. With c_H,c_G,c from the THREE
    genuinely source-labelled recurrences, the identity is:

        c-c_H-c_G = kappa_next-16*kappa_prev in {-16,-15,0,1}.

    The weighted temporal sum of these defects telescopes to kappa_N.
    This is a source-exact zero-seeded carry coboundary, not a Weyl saving.
    """
    if type(n) is not int or n < 1:
        raise ValueError('source n>=1')
    prev_h,prev_g=Q(prev_h),Q(prev_g)
    if not 0<=prev_h<1 or not 0<=prev_g<1:
        raise ValueError('provide fractional channel states')
    old_k = int(prev_h+prev_g)
    y = prev_h+prev_g-old_k
    zh = 16*prev_h+real_source(n)
    zg = 16*prev_g+gaussian_source(n)
    z = 16*y+original_r(n)
    ch,cg,c = int(zh//1),int(zg//1),int(z//1)
    xh,xg,yn = zh-ch,zg-cg,z-c
    next_k = int(xh+xg)
    if (xh+xg-next_k)!=yn:
        raise AssertionError('real selected source scalar gluing failed')
    defect = c-ch-cg
    if defect != next_k-16*old_k or defect not in (-16,-15,0,1):
        raise AssertionError('exact source integer carry coboundary failed')
    return dict(n=n, old_kappa=old_k,next_kappa=next_k,
                carry_original=c,carry_real=ch,carry_gaussian=cg,
                carry_coboundary=defect,
                next_real=xh,next_gaussian=xg,next_original=yn)


def carry_coboundary_stream(N:int):
    """Yield source carry receipts; cumulative weighted defect equals final bit."""
    if type(N) is not int or N<0:raise ValueError('N>=0')
    xh=xg=Q(0)
    weighted=0
    for n in range(1,N+1):
        cert=carry_coboundary_step(n,xh,xg)
        weighted=16*weighted+cert['carry_coboundary']
        if weighted!=cert['next_kappa']:
            raise AssertionError('unbounded real carry defect leaked across frames')
        yield cert
        xh,xg=cert['next_real'],cert['next_gaussian']
