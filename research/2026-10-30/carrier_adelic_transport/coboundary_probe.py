"""Exact audit of twisted rational summability and a four-pole null source.

Research probe, not a normality proof. Only stdlib exact Fraction arithmetic.
Partial fractions are supplied explicitly, not guessed by sampled evaluation.
"""
from fractions import Fraction as Q
from math import comb
import unittest


def add_term(d, key, value):
    d[key] = d.get(key, Q(0)) + value
    if not d[key]:
        del d[key]


def weighted_obstructions(poles, base=16):
    """(rational pole mod Z, order) -> weighted residue, including zeros."""
    out = {}
    for (pole, order), coeff in poles.items():
        pole, coeff = Q(pole), Q(coeff)
        if order < 1 or not coeff:
            raise ValueError("positive pole order and nonzero coefficient required")
        k = pole.numerator // pole.denominator
        a = pole - k
        key = (a, order)
        out[key] = out.get(key, Q(0)) + Q(base) ** (-k) * coeff
    return out


def rational_antidifference(poles, polynomial=(), base=16):
    """Solve F(z)=base*T(z-1)-T(z), from full rational PF data.

    Return (T poles, T ascending polynomial coefficients); raise on obstruction.
    Defined over Q for rational poles and rational base != 0,1.
    """
    base = Q(base)
    if base in (0, 1):
        raise ValueError("this implementation requires base != 0,1")
    if any(weighted_obstructions(poles, base).values()):
        raise ValueError("nonzero weighted pole obstruction")
    groups = {}
    for (pole, order), coeff in poles.items():
        pole = Q(pole)
        k = pole.numerator // pole.denominator
        groups.setdefault((pole-k, order), {})[k] = Q(coeff)
    result = {}
    for (a, order), r in groups.items():
        previous = Q(0)
        for k in range(min(r), max(r)+1):
            current = base*previous-r.get(k, Q(0))
            if current:
                result[(a+k, order)] = current
            previous = current
        if previous:
            raise AssertionError("obstruction and recurrence disagree")
    f = tuple(map(Q, polynomial))
    t = [Q(0)]*len(f)
    for k in reversed(range(len(f))):
        higher = base*sum((Q(comb(j,k))*(-1)**(j-k)*t[j]
                          for j in range(k+1,len(f))), Q(0))
        t[k] = (f[k]-higher)/(base-1)
    while t and not t[-1]:
        t.pop()
    return result, tuple(t)


def difference(poles, polynomial=(), base=16):
    out = {}
    for (pole, order), coeff in poles.items():
        add_term(out, (Q(pole)+1, order), Q(base)*coeff)
        add_term(out, (Q(pole), order), -Q(coeff))
    t = tuple(map(Q, polynomial))
    f = tuple(Q(base)*sum((Q(comb(j,k))*(-1)**(j-k)*t[j]
                           for j in range(k,len(t))), Q(0))-t[k]
              for k in range(len(t)))
    return out, f


def evaluate(poles, polynomial, z):
    z = Q(z)
    return sum((Q(c)/(z-p)**k for (p,k),c in poles.items()), Q(0)) + sum(
        (Q(c)*z**j for j,c in enumerate(polynomial)), Q(0))


def authentic(n):
    return sum((Q(c,8*n-8+d) for d,c in zip((1,4,5,6),(4,-2,-1,-1))),Q(0))


def null_tail(n):
    return Q(1,(8*n+1)*(8*n+2))


def null_source(n):
    a=8*n-7
    return Q(16,a)-Q(16,a+1)-Q(1,a+8)+Q(1,a+9)


def primary(q, p):
    q=Q(q)
    denominator=q.denominator
    power=1
    while denominator % p == 0:
        denominator//=p
        power*=p
    if power==1:
        return Q(0)
    return Q((q.numerator*pow(denominator,-1,power))%power,power)


AUTH_POLES={(Q(1)-Q(d,8),1):Q(c,8)
            for d,c in zip((1,4,5,6),(4,-2,-1,-1))}
NULL_POLES={(Q(7-d,8),1):Q(c,8)
            for d,c in zip((0,1,8,9),(16,-16,-1,1))}


class Audit(unittest.TestCase):
    def test_original_four_singleton_obstructions(self):
        self.assertEqual(set(weighted_obstructions(AUTH_POLES).values()),
                         {Q(1,2),Q(-1,4),Q(-1,8)})
        self.assertEqual(len(weighted_obstructions(AUTH_POLES)),4)
        with self.assertRaises(ValueError): rational_antidifference(AUTH_POLES)

    def test_null_has_two_zero_obstructions(self):
        obs=weighted_obstructions(NULL_POLES)
        self.assertEqual(len(obs),2)
        self.assertTrue(all(v==0 for v in obs.values()))

    def test_null_tail_exactly_reconstructed(self):
        p,t=rational_antidifference(NULL_POLES)
        self.assertEqual(p,{(Q(-1,8),1):Q(1,8),(Q(-1,4),1):Q(-1,8)})
        self.assertEqual(t,())
        for n in (0,1,2,7,31,100):
            self.assertEqual(evaluate(p,t,n),null_tail(n))

    def test_all_order_constructive_roundtrip(self):
        t={(Q(-13,7),1):Q(3,5),(Q(8,7),1):Q(-4,3),
           (Q(2,3),2):Q(7,9),(Q(-4,3),3):Q(-8,11),
           (Q(4),4):Q(19,7)}
        for b in (2,3,16,Q(5,2),Q(-3)):
            for polynomial in ((),(2,),(-1,3,-2,7)):
                fp,ff=difference(t,polynomial,b)
                rp,rf=rational_antidifference(fp,ff,b)
                self.assertEqual(rp,t)
                self.assertEqual(rf,tuple(map(Q,polynomial)))
                for z in (10,23,101):
                    self.assertEqual(evaluate(fp,ff,z),
                        b*evaluate(t,polynomial,z-1)-evaluate(t,polynomial,z))

    def test_first_residue_only_mutation_is_detected(self):
        # Every ordinary residue is zero, yet an order-two obstruction remains.
        with self.assertRaises(ValueError):
            rational_antidifference({(Q(1,3),2):Q(1)})

    def test_changed_residue_breaks_summability(self):
        p=dict(NULL_POLES)
        p[(Q(7,8),1)]+=Q(1,17)
        with self.assertRaises(ValueError): rational_antidifference(p)

    def test_null_source_positive_and_telescopes(self):
        for n in range(1,101):
            self.assertGreater(null_source(n),0)
            self.assertEqual(null_source(n),16*null_tail(n-1)-null_tail(n))

    def test_null_zero_seed_and_completed_boundary(self):
        u=Q(0)
        for n in range(1,51):
            u=16*u+null_source(n)
            self.assertEqual(u, Q(16**n,2)-null_tail(n))
            self.assertEqual(u%1,1-null_tail(n))

    def test_null_exact_partial_sums(self):
        for N in (1,3,17,59):
            s=sum((Q(16)**(-n)*null_source(n) for n in range(1,N+1)),Q(0))
            self.assertEqual(s,Q(1,2)-Q(16)**(-N)*null_tail(N))

    def test_rank_two_coefficients_match(self):
        auth=sum((-Q(c*d) for d,c in zip((0,3,4,5),(4,-2,-1,-1))),Q(0))
        null=sum((-Q(c*d) for d,c in zip((0,1,8,9),(16,-16,-1,1))),Q(0))
        self.assertEqual(auth,15)
        self.assertEqual(null,15)
        self.assertEqual(sum((c*d*d for d,c in zip((0,3,4,5),(4,-2,-1,-1)))), -59)
        self.assertEqual(sum((c*d*d for d,c in zip((0,1,8,9),(16,-16,-1,1)))), 1)

    def test_finite_place_all_time_blindness(self):
        S=(2,3,5,7,11)
        seed=Q(1,13)
        u=v=Q(0)
        v=seed
        for n in range(31):
            self.assertEqual(v-u,16**n*seed)
            for p in S: self.assertEqual(primary(u,p),primary(v,p))
            self.assertNotEqual(u%1,v%1)
            u=16*u+authentic(n+1)
            v=16*v+authentic(n+1)

    def test_character_at_two_is_trivial(self):
        u=Q(0)
        for n in range(1,101):
            u=16*u+authentic(n)
            self.assertEqual(u.denominator%2,1)
            self.assertEqual(primary(u,2),0)

    def test_finite_prime_precision_blindness(self):
        precisions={2:7,3:4,5:3,7:2}
        multiplier=1
        for p,k in precisions.items(): multiplier*=p**k
        seed=Q(multiplier,11)
        for n in (0,1,3,17,43):
            delta=16**n*seed
            self.assertNotEqual(delta%1,0)
            for p,k in precisions.items():
                # Local character at conductor p^k: exact principal part.
                self.assertEqual(primary(delta/Q(p**k),p),0)


if __name__=="__main__":
    unittest.main(verbosity=2)
