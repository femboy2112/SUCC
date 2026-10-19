"""Finite-clock source laws and exact finite shadows of profinite completions.

Metatheoretic integer moduli are finite observation labels, not evidence of
accessible universal profinite quotients. No RH/Weil input.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm, isqrt

class SourceLawError(ValueError):
    pass


def modulus(n, maximum=1000000):
    if type(n) is not int or not 1 <= n <= maximum:
        raise SourceLawError("positive finite integer modulus, within budget, required")
    return n


def factor(n):
    modulus(n)
    output = {}
    d = 2
    while d*d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d; k += 1
            output[d] = k
        d += 1 if d == 2 else 2
    if n > 1:
        output[n] = output.get(n, 0) + 1
    return output


def divisors(n):
    modulus(n)
    lo, hi = [], []
    for d in range(1,isqrt(n)+1):
        if n % d == 0:
            lo.append(d)
            if d*d != n:
                hi.append(n//d)
    return tuple(lo+hi[::-1])


def finite_clock_closure(observed):
    """Closure under quotient (divisor) and rooted cyclic product (lcm)."""
    if type(observed) not in (tuple,list) or len(observed)>48:
        raise SourceLawError("finite observed-period tuple/list required")
    v = 1
    for n in observed:
        modulus(n)
        v = lcm(v,n)
        if v > 1000000:
            raise SourceLawError("finite clock LCM budget exceeded")
    return {"lcm":v,"closed_periods":divisors(v),"index_depth":factor(v)}


def rooted_diagonal_orbit(m,n):
    """Orbit of (0,0) in C_m x C_n under simultaneous +1.

    It has lcm(m,n) rather than m*n points if gcd(m,n)>1.
    """
    modulus(m,400); modulus(n,400)
    size = lcm(m,n)
    return {"m":m,"n":n,"diagonal_period":size,
            "full_cartesian_size":m*n,"component_count":gcd(m,n),
            "orbit":tuple((i%m,i%n) for i in range(size))}


@dataclass(frozen=True)
class ClockTheory:
    """Infinite, declared source class; never inferred from finite experiments.

    FULL: all cyclic moduli.
    SQUAREFREE: all squarefree moduli; all prime species, no p^2.
    PRO_P: only p-power clocks.
    FINITE_SUPPORT: arbitrary powers of a fixed finite set of primes.
    FINITE_LCM: all divisors of the one finite cyclic period m.
    """
    kind: str
    parameter: object = None

    def __post_init__(self):
        if self.kind not in {"full","squarefree","pro_p","finite_support","finite_lcm","one_prime_cap"}:
            raise SourceLawError("unknown source class")
        if self.kind in {"full","squarefree"} and self.parameter is not None:
            raise SourceLawError("no parameter permitted")
        if self.kind == "finite_lcm": modulus(self.parameter)
        if self.kind == "pro_p":
            if type(self.parameter) is not int or factor(self.parameter)!={self.parameter:1}:
                raise SourceLawError("actual prime required for a pro-p class")
        if self.kind == "one_prime_cap":
            entry=self.parameter
            if (type(entry) is not tuple or len(entry)!=2 or
                type(entry[0]) is not int or factor(entry[0])!={entry[0]:1} or
                type(entry[1]) is not int or not 1<=entry[1]<=128):
                raise SourceLawError("one prime and positive finite maximum power required")
        if self.kind == "finite_support":
            if type(self.parameter) is not tuple or not self.parameter:
                raise SourceLawError("nonempty finite prime tuple required")
            if (tuple(sorted(set(self.parameter))) != self.parameter or
                any(type(p) is not int or factor(p)!={p:1} for p in self.parameter)):
                raise SourceLawError("distinct sorted prime labels required")

    def permits(self, n):
        factors = factor(n)
        if self.kind == "full": return True
        if self.kind == "squarefree": return max(factors.values(),default=0)<=1
        if self.kind == "pro_p": return all(p==self.parameter for p in factors)
        if self.kind == "finite_support": return all(p in self.parameter for p in factors)
        if self.kind == "one_prime_cap":
            prime, exponent=self.parameter
            return factors.get(prime,0)<=exponent
        return self.parameter % n == 0

    def prime_exposure(self, prime):
        if type(prime) is not int or factor(prime)!={prime:1}:
            raise SourceLawError("prime test only")
        return self.permits(prime)

    def arbitrary_depth(self, prime):
        if type(prime) is not int or factor(prime)!={prime:1}:
            raise SourceLawError("prime test only")
        return ((self.kind=="full") or
                (self.kind=="pro_p" and prime==self.parameter) or
                (self.kind=="finite_support" and prime in self.parameter) or
                (self.kind=="one_prime_cap" and prime!=self.parameter[0]))

    @property
    def universal(self):
        """Logical property of DECLARED infinite type; not learned by finite tests."""
        return self.kind=="full"

    def finite_signature(self, queries):
        if type(queries) not in (list,tuple):
            raise SourceLawError("queries must be finite list/tuple")
        return tuple((modulus(q),self.permits(q)) for q in queries)


def matching_finite_shadow(queries):
    """A proper finite source reproduces all tested positive full-clock reports.

    Observation predicate only: presence, exact period, and rooted bonding maps
    *between* requested periods; not arbitrary universal sentences.
    """
    stage = finite_clock_closure(queries)
    finite = ClockTheory("finite_lcm",stage["lcm"])
    if any(not finite.permits(m) for m in queries):
        raise AssertionError("positive observation failed finite shadow")
    return {"stage":stage["lcm"],"actual_observed_moduli":tuple(queries),
            "finite_signature":finite.finite_signature(tuple(queries)),
            "full_signature":ClockTheory("full").finite_signature(tuple(queries)),
            "has_unobserved_refinements":True}


def unique_pointed_clock_map(big,small):
    """Existence/uniqueness of rooted successor-equivariant C_big -> C_small.

    The root is 0 and S(k)=k+1 mod period. Once f(0)=0, equivariance
    forces f(k)=k mod small. The map descends iff small divides big.
    """
    modulus(big,400); modulus(small,400)
    if big%small:
        return None
    return tuple(k%small for k in range(big))


def missing_power_infinite_shadow(queries):
    """An INFINITE procyclic source with every simple prime quotient.

    Matches all finite positive quotient/bonding queries of full Zhat, while
    capping one p-power depth. This defeats stronger finite certifier claims.
    """
    data=finite_clock_closure(queries)
    exponent=max(1,factor(data['lcm']).get(2,0))
    source=ClockTheory('one_prime_cap',(2,exponent))
    if source.finite_signature(tuple(queries))!=ClockTheory('full').finite_signature(tuple(queries)):
        raise AssertionError('constructed infinite shadow has wrong source signature')
    witness=2**(exponent+1)
    if source.permits(witness) or not ClockTheory('full').permits(witness):
        raise AssertionError('future discriminator is not sound')
    return {'observed':tuple(queries),'capped_prime':2,'capped_depth':exponent,
            'first_missing_power':witness,
            'declared_infinite_procyclic_all_simple_quotients':True,
            'observationally_equal_on_queries':True}


def authenticate_prime_word(model, word, *, maximum=1000000):
    """Separate free FUCC words from genuine finite-quotient source access.

    Requires an actual cyclic quotient of INDEX product p^k, not just the
    availability of each primitive simple quotient. A finite cyclic stage
    may support virtual arithmetic words with no corresponding subgroup.
    """
    if type(model) is not ClockTheory or type(word) is not tuple:
        raise SourceLawError('typed clock source and finite exponent word required')
    n=1
    for entry in word:
        if type(entry) is not tuple or len(entry)!=2:
            raise SourceLawError('prime/exponent pairs required')
        p,k=entry
        if type(p) is not int or type(k) is not int or k<0 or factor(p)!={p:1}:
            raise SourceLawError('genuine prime labels and nonnegative depths required')
        n *= p**k
        if n>maximum: raise SourceLawError('authentication budget exceeded')
    authentic=model.permits(n)
    return {'index':n,'source_authenticated':authentic,
            'local_haar_mass':(str(F(1,n)) if authentic else None),
            'formal_free_word_exists':True}
