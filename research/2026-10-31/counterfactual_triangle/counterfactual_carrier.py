"""Counterfactual normality probes, exact finite arithmetic only.

No finite output proves normality of pi. CT-01–09 are algebraic and classical
consequences; the selected arithmetic upper bound CT-10 remains OPEN.
"""
from __future__ import annotations

from fractions import Fraction

def _q(value):
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    raise TypeError("exact int/Fraction required")

def bbp_source(n: int) -> Fraction:
    """Original four signed poles; n>=1. Historical formula untouched."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))

def original_states(N: int) -> tuple[Fraction, ...]:
    """Exact lifted U_1,...,U_N with U_0=0; no pi approximation."""
    if type(N) is not int or N < 0:
        raise ValueError("N must be nonnegative")
    u = Fraction(0)
    states = []
    for n in range(1, N+1):
        u = 16*u + bbp_source(n)
        states.append(u)
    return tuple(states)

def green_tail_bracket(n: int, terms: int = 24) -> tuple[Fraction, Fraction]:
    """Enclose T_n by its partial sum and a monotone BBP-source remainder."""
    if type(n) is not int or n < 0 or type(terms) is not int or terms < 1:
        raise ValueError("invalid n or truncation")
    low = sum((bbp_source(n+j) / (16**j)
               for j in range(1, terms+1)), Fraction(0))
    return low, low + bbp_source(n+terms+1)/(15 * 16**terms)

def pi_bracket(terms: int) -> tuple[Fraction, Fraction]:
    """BBP-only rational pi enclosure; no supplied digits or mpmath."""
    if type(terms) is not int or terms < 1:
        raise ValueError("positive terms required")
    low = sum((bbp_source(n) * Fraction(16, 16**n)
               for n in range(1, terms+1)), Fraction(0))
    return low, low + 16*bbp_source(terms+1)/(15*16**terms)

def certified_hex_digits(digits: int, extra_terms: int = 12) -> str:
    """Certify fractional hexadecimal digits of pi with exact BBP brackets."""
    if type(digits) is not int or digits < 1:
        raise ValueError("positive digit count required")
    lo, hi = pi_bracket(digits + extra_terms)
    a, b = (16**digits * lo).__floor__(), (16**digits * hi).__floor__()
    if a != b:
        raise ArithmeticError("BBP bracket crosses digit seam; raise extra_terms")
    return format(a % 16**digits, f"0{digits}x")

def _word_probabilities(hex_digits: str, depth: int, horizon: int):
    if type(depth) is not int or depth < 0 or type(horizon) is not int or horizon < 1:
        raise ValueError("invalid depth/horizon")
    if len(hex_digits) < horizon + depth - 1:
        raise ValueError("not enough hex digits for last full word")
    counts = {}
    for i in range(horizon):
        w = hex_digits[i:i+depth]
        counts[w] = counts.get(w, 0) + 1
    return {w: Fraction(v, horizon) for w, v in counts.items()}

def word_and_walsh_certificate(hex_digits: str, depth: int, horizon: int):
    """Exact collision Parseval and full 15-current discrepancy witness."""
    if depth < 1:
        raise ValueError("depth>=1 required")
    prob = [_word_probabilities(hex_digits,k,horizon) for k in range(depth+1)]
    q = 16**depth
    Q = q * sum((p*p for p in prob[depth].values()), Fraction(0))
    energy, maxJ, witness = Fraction(0), Fraction(0), None
    for level in range(depth):
        parents = (prob[level].keys() if level else ("",))
        for v in parents:
            for mask in range(1,16):
                J = sum(((-1 if ((digit & mask).bit_count()%2) else 1)
                         *prob[level+1].get(v+format(digit,'x'), Fraction(0))
                         for digit in range(16)), Fraction(0))
                energy += (16**level)*J*J
                if abs(J)>maxJ:
                    maxJ, witness=abs(J), (v,mask,J)
    max_bias = max((abs(prob[depth].get(format(w,f'0{depth}x'),Fraction(0)) - Fraction(1,q))
                    for w in range(q)), default=Fraction(0))
    return {'Q':Q, 'energy':energy, 'max_current':maxJ,
            'witness':witness, 'max_word_bias':max_bias,
            'localization_upper':(1-Fraction(1,q))*maxJ}

def tent_vector(x: Fraction, q: int) -> dict[int, Fraction]:
    """At most two nonzero barycentric hat coordinates on the unit circle."""
    if type(q) is not int or q < 2:
        raise ValueError("q>=2")
    z = (_q(x) % 1)*q
    i = z.numerator // z.denominator
    t = z-i
    return {i:1-t, (i+1)%q:t}

def tent_occupation(xs, q: int) -> tuple[Fraction, ...]:
    xs = tuple(xs)
    if not xs:
        raise ValueError("nonempty empirical orbit required")
    acc = [Fraction(0) for _ in range(q)]
    for x in xs:
        for i,w in tent_vector(x,q).items():
            acc[i] += w
    return tuple(v/len(xs) for v in acc)

def tent_defect(xs, q: int) -> Fraction:
    p=tent_occupation(xs,q)
    return sum((abs(v-Fraction(1,q)) for v in p),Fraction(0))

def vector_l1(u, v) -> Fraction:
    if len(u)!=len(v):
        raise ValueError("same dimension required")
    return sum((abs(a-b) for a,b in zip(u,v)),Fraction(0))

def finite_tail_transport(N: int, q: int, tail_terms: int=24):
    """Exact rational hat transport; interval remainder is retained explicitly."""
    xs = original_states(N)
    lowers, highs = zip(*(green_tail_bracket(n,tail_terms) for n in range(1,N+1)))
    ys_approx = tuple(x+t for x,t in zip(xs,lowers))
    P = tent_occupation(xs,q)
    Q = tent_occupation(ys_approx,q)
    observed = vector_l1(P,Q)
    budget = Fraction(2*q,N)*sum(highs,Fraction(0))
    missing = Fraction(2*q,N)*sum((h-l for h,l in zip(highs,lowers)),Fraction(0))
    full_budget = Fraction(q,16*N)  # original sum_n T_n < 1/32
    return {'observed_rational':observed,'certified_upper':budget,
            'missing_tail_upper':missing,'universal_upper':full_budget,
            'completed_to_rational_upper':observed+missing}

def triangle_refinement(N: int, q: int):
    """Exact rational 16-to-1 hat-refinement Ward identity on original BBP states.

    Every x obeys phi_(q,j)(16x) = sum_t phi_(16q,j+t*q)(x).
    For U_(n+1)=16U_n+r(n+1), the empirical source defect is the sum
    of a boundary coboundary and the actual signed forcing response.
    """
    if type(N) is not int or N < 1 or type(q) is not int or q < 2:
        raise ValueError("invalid N/q")
    states = original_states(N+1)
    p = tent_occupation(states[:N],q)
    finer = tent_occupation(states[:N],16*q)
    projected = tuple(sum((finer[j+t*q] for t in range(16)),Fraction(0))
                      for j in range(q))
    observed = tuple(a-b for a,b in zip(p,projected))
    left = tent_vector(states[0],q)
    right = tent_vector(states[-1],q)
    boundary = tuple((left.get(j,Fraction(0))-right.get(j,Fraction(0)))/N for j in range(q))
    response = [Fraction(0) for _ in range(q)]
    for n in range(N):
        after = tent_vector(states[n+1],q)
        before = tent_vector(16*states[n],q)
        for j in set(after)|set(before):
            response[j] += after.get(j,0)-before.get(j,0)
    response = tuple(z/N for z in response)
    budget = (2+2*q*sum((bbp_source(n+1) for n in range(1,N+1)),Fraction(0)))/N
    return {'observed':observed, 'boundary':boundary, 'forcing':response,
            'l1':sum((abs(z) for z in observed),Fraction(0)),
            'source_upper':budget, 'universal_upper':Fraction(2+8*q,N)}
