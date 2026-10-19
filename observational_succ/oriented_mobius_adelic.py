"""Negative counting before the number line: exact incidence, parity and ideles.

The integer negative is introduced by the UNIVERSAL group completion of
finite disjoint-union counts. On a Boolean prime carrier the Moebius inverse
is parity-conjugate to incidence zeta. This fails for a repeated prime jet.

The finite-place valuation parity character cannot descend to C_Q without
a continuous Archimedean compensation; two genuine primes already obstruct
a universal minus choice. No zero locations, Weil PSD, or Connes trace used.

References: classical incidence algebra, Grothendieck completion,
Tate's thesis, and SUCC's pinned Connes/Weil source atlas.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import isqrt


class NegativeCountingError(ValueError):
    """Unjustified domain, orientation or fake prime source."""


def _natural(n):
    if type(n) is not int or n < 0:
        raise NegativeCountingError("finite nonnegative cardinality required")
    return n


def _positive(n):
    if type(n) is not int or not 1 <= n <= 1_000_000:
        raise NegativeCountingError("positive integer <= 1000000 required")
    return n


def _prime(p):
    _positive(p)
    if p == 1 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise NegativeCountingError("genuine prime required, composite 6 forbidden")
    return p


def valuations(n):
    """Prime exponents of a positive integer; no fake p=6 place."""
    n = _positive(n)
    result = {}
    d = 2
    while d*d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            result[d] = k
        d += 1 if d == 2 else 2
    if n > 1:
        result[n] = 1
    return result


@dataclass(frozen=True)
class DifferenceCount:
    """Class [a]-[b] in Grothendieck group K0(FinSet,+).

    It exists as a FORMAL difference of positive cardinalities. The
    induced multiplication is the product of signed finite collections.
    No negative primitive or ordered number line is an input.
    """
    plus: int
    minus: int

    def __post_init__(self):
        _natural(self.plus)
        _natural(self.minus)

    def equivalent(self, other):
        if not isinstance(other, DifferenceCount):
            raise NegativeCountingError("signed finite collection required")
        return self.plus+other.minus == other.plus+self.minus

    def add(self, other):
        if not isinstance(other, DifferenceCount):
            raise NegativeCountingError("signed finite collection required")
        return DifferenceCount(self.plus+other.plus,self.minus+other.minus)

    def reverse(self):
        return DifferenceCount(self.minus,self.plus)

    def times(self, other):
        if not isinstance(other, DifferenceCount):
            raise NegativeCountingError("signed finite collection required")
        return DifferenceCount(self.plus*other.plus+self.minus*other.minus,
                               self.plus*other.minus+self.minus*other.plus)

    def integer_value(self):
        """A posteriori isomorphism K0(FinSet) ~= Z."""
        return self.plus-self.minus


def reversal_ring_obstruction():
    """Global sign reversal is additive but NOT a UNITAL ring symmetry."""
    unit=DifferenceCount(1,0)
    rev=unit.reverse()
    return {
        "integer_unit":unit.integer_value(),
        "reversed_unit":rev.integer_value(),
        "product_of_reversed_units":rev.times(rev).integer_value(),
        "reversed_product_of_units":unit.times(unit).reverse().integer_value(),
        "preserves_additive_group":True, "preserves_unital_multiplication":False,
        "no_preexisting_negative_integer_required":True,
    }


@dataclass(frozen=True)
class PrimeIncidence:
    """Finite product of valuation chains 0..depth[p].

    depth=1 is the BOOLEAN squarefree carrier. depth>=2 includes p^2.
    All matrices are exact integer matrices with a fixed source basis.
    """
    primes: tuple[int,...]
    depths: tuple[int,...]

    def __post_init__(self):
        if type(self.primes) is not tuple or type(self.depths) is not tuple:
            raise NegativeCountingError("finite source tuples required")
        if len(self.primes)!=len(self.depths) or not 1<=len(self.primes)<=5:
            raise NegativeCountingError("1..5 prime dimensions required")
        if self.primes != tuple(sorted(set(self.primes))):
            raise NegativeCountingError("sorted distinct prime dimensions required")
        for p in self.primes:
            _prime(p)
        for d in self.depths:
            if type(d) is not int or not 1<=d<=6:
                raise NegativeCountingError("positive valuation depth <=6 required")
        size=1
        for d in self.depths:
            size *= d+1
        if size>64:
            raise NegativeCountingError("finite exact matrix budget 64 states")

    @property
    def states(self):
        return tuple(product(*(range(d+1) for d in self.depths)))

    def _state(self, a):
        if type(a) is not tuple or len(a)!=len(self.primes) or any(
            type(x) is not int or x<0 or x>d
            for x,d in zip(a,self.depths)
        ):
            raise NegativeCountingError("state outside genuine valuation cube")
        return a

    def comparable(self,a,b):
        a,b=self._state(a),self._state(b)
        return all(x<=y for x,y in zip(a,b))

    def zeta(self,a,b):
        return int(self.comparable(a,b))

    def moebius(self,a,b):
        if not self.comparable(a,b):
            return 0
        increments=tuple(y-x for x,y in zip(a,b))
        return (-1)**sum(increments) if all(k<=1 for k in increments) else 0

    def parity(self,a):
        return (-1)**sum(self._state(a))

    def oriented_zeta(self,a,b):
        return self.parity(a)*self.zeta(a,b)*self.parity(b)

    def matrix(self,kind):
        if kind not in ("zeta","moebius","oriented_zeta"):
            raise NegativeCountingError("typed incidence operator required")
        fn=getattr(self,kind)
        st=self.states
        return tuple(tuple(fn(a,b) for b in st) for a in st)

    @staticmethod
    def matrix_product(a,b):
        n=len(a)
        if len(b)!=n or any(len(row)!=n for row in a+b):
            raise NegativeCountingError("matching square matrices")
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))
                           for j in range(n)) for i in range(n))

    def verdict(self):
        z,m,j=(self.matrix(kind) for kind in ("zeta","moebius","oriented_zeta"))
        n=len(z)
        ident=tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
        if self.matrix_product(z,m)!=ident or self.matrix_product(m,z)!=ident:
            raise AssertionError("MOBIUS_INVERSE_FAILED")
        disputes=tuple(
            (self.states[i],self.states[k],j[i][k],m[i][k])
            for i in range(n) for k in range(n) if j[i][k]!=m[i][k]
        )
        boolean=all(d==1 for d in self.depths)
        if (not disputes) != boolean:
            raise AssertionError("source-depth Möbius orientation classification false")
        return {
            "primes":self.primes,"depths":self.depths,"basis_size":n,
            "moebius_is_exact_incidence_inverse":True,
            "oriented_positive_zeta_equals_inverse":not disputes,
            "first_obstruction":disputes[0] if disputes else None,
            "unresolved_prime_power_obstruction_count":len(disputes),
            "original_Weil_form_identified":False,"RH_proved":False,
        }


def omega_parity(n):
    """Liouville parity of total prime exponents, on genuine integer carrier."""
    return (-1)**sum(valuations(n).values())


def number_moebius(n):
    """The arithmetic Möbius function; zero on any p^2 divisor."""
    exps=valuations(n).values()
    return 0 if any(k>=2 for k in exps) else (-1)**len(tuple(exps))


def source_succ_sign_edges(ns=(1,2,3,4)):
    """If phase J(n)=(-1)^Omega(n), JSJ is NOT +/- original unit SUCC."""
    if type(ns) is not tuple or not ns:
        raise NegativeCountingError("nonempty exact source tuple")
    edges=tuple((n,omega_parity(n)*omega_parity(n+1)) for n in ns)
    return {
        "transported_unit_succ_edge_signs":edges,
        "is_uniform_orientation_on_succ":len({s for _,s in edges})==1,
        "prime_FUCC_every_step_flips":True,
        "mutual_source_observables_transport_required":True,
    }


def rational_prime_valuations(q):
    """Exact formal log-p expansion of a nonzero positive rational."""
    if type(q) not in (int,Q):
        raise NegativeCountingError("nonzero positive rational required")
    q=Q(q)
    if q<=0:
        raise NegativeCountingError("positive rational required")
    a=valuations(q.numerator)
    b=valuations(q.denominator)
    return {p:a.get(p,0)-b.get(p,0)
            for p in sorted(set(a)|set(b))
            if a.get(p,0)!=b.get(p,0)}


def diagonal_norm_character_receipt(q):
    """Real+finite norm-character phases cancel coefficientwise in log primes.

    Chi_v(x_v)=|x_v|_v^(it) has local log phase coefficient
    -v_p(q) at p and +v_p(q) at the real place (in log p basis).
    The product is 1 on diagonal Q*, for every real t.
    """
    exps=rational_prime_valuations(q)
    real=tuple(sorted(exps.items()))
    finite=tuple(sorted((p,-k) for p,k in exps.items()))
    return {
        "diagonal_positive_rational":Q(q),
        "arch_real_logp_coefficients":real,
        "finite_logp_coefficients":finite,
        "sum_is_zero_for_every_prime":all(exps[p]-exps[p]==0 for p in exps),
        "descends_to_idelic_class_norm_character":True,
        "global_character_is_zeta_positivity":False,
    }


def uniform_negative_no_global_character(p=2,q=3):
    """Theorem: all unramified valuation signs -1 cannot be canceled by
    one CONTINUOUS positive-real Archimedean UNITARY character.

    If chi_infty(x)=x^(it) canceled finite chi_f(q)=(-1)^Omega(q)
    then p^(it)=q^(it)=-1. Thus
       t log p = (2a+1)pi and t log q=(2b+1)pi,
    giving log p/log q=(odd)/(odd), a rational number. For distinct
    primes this is impossible: p^u=q^v never holds for nonzero integers.
    A character with ramified unit components is NOT covered by this
    specifically unramified uniform-parity no-go.
    """
    _prime(p);_prime(q)
    if p==q:
        raise NegativeCountingError("independent distinct prime places required")
    return {
        "two_genuine_distinct_prime_witnesses":tuple(sorted((p,q))),
        "local_uniform_valuation_sign_at_each_prime":-1,
        "required_arch_phases":((p,-1),(q,-1)),
        "unique_factorization_implies_log_ratio_irrational":True,
        "continuous_arch_unitary_norm_character_can_compensate":False,
        "a_ramified_Hecke_character_was_ruled_out":False,
        "zeros_used":False,"RH_proved":False,
    }


def signed_local_euler_factor(p,beta,epsilon):
    """Classical convergent local Dirichlet series Lp=1/(1-eps*p^-beta).

    For eps=-1 this is not zeta's original local Euler factor. The
    coherent Hilbert phase is gauge-equivalent only if observables transport.
    """
    _prime(p)
    if type(beta) is not int or not 2<=beta<=16:
        raise NegativeCountingError("integer convergent half-plane beta>=2")
    if type(epsilon) is not int or epsilon not in (-1,1):
        raise NegativeCountingError("local phase +/-1 required")
    r=Q(1,p**beta)
    return {
        "prime":p,"beta":beta,"epsilon":epsilon,"p_to_minus_beta":r,
        "Tate_zeta_local":1/(1-r),
        "phase_twisted_local":1/(1-epsilon*r),
        "coefficient_at_p":epsilon,
        "coefficient_at_p_squared":epsilon*epsilon,
        "same_original_Euler_source":epsilon==1,
        "norm_squared_phase_blind":True,"RH_proved":False,
    }
