"""Committed independent adversarial oracle for Mason-Stothers (the SECOND
verification route referenced by MASON_STOTHERS_PROOF.md and PROOF_FORGE.md).

Independence: the certificate (`mason_stothers_certificate`) computes the radical
via `factor_list` and verifies the bound through the Wronskian / divisibility
`M | W`. This oracle instead (a) recomputes `deg rad(ABC)` by the gcd-squarefree
route `P / gcd(P, P')` -- valid in characteristic 0 and when char > deg, and
genuinely distinct from `factor_list` -- and (b) checks the THEOREM'S CONCLUSION
`max deg <= deg rad - 1` directly, not through the certificate's proof mechanism.
Agreement of the two routes on a seeded random corpus is the independence
guarantee. Deterministic: fixed seed, so the corpus and counts are reproducible.

This test is what caught the first-draft backwards-divisibility bug (invisible on
tight cases, where M and W are scalar multiples).
"""
import random
import unittest

import sympy as sp

from observational_succ.mason_stothers import mason_stothers_certificate

x = sp.Symbol("x")


def _indep_rad_deg_gcd_squarefree(P, domain):
    """deg of the radical via P/gcd(P,P') -- independent of factor_list.
    Valid in char 0 and char > deg (where P' != 0 for every nonconstant factor)."""
    P = sp.Poly(P, x, domain=domain)
    Pp = P.diff(x)
    if Pp.is_zero:
        raise ValueError("P' == 0: gcd-squarefree route invalid (out of char>deg regime)")
    g = sp.gcd(P, Pp)
    return P.quo(g).degree()


def _rand_poly(domain, rng):
    P = sp.Poly(1, x, domain=domain)
    for _ in range(rng.randint(1, 3)):
        if rng.random() < 0.7:
            fac = sp.Poly(x - rng.randint(-3, 3), x, domain=domain)
        else:
            fac = sp.Poly(x * x + rng.randint(-2, 2) * x + rng.randint(1, 3), x, domain=domain)
        P = P * fac ** rng.randint(1, 3)
    return P


class TestMasonStothersIndependentOracle(unittest.TestCase):
    def test_seeded_sweep_no_violations(self):
        rng = random.Random(20261020)
        tested = violations = rad_mismatch = unverified_valid = 0
        for domain, trials in ((sp.QQ, 400), (sp.GF(11), 150)):
            for _ in range(trials):
                A = _rand_poly(domain, rng)
                B = _rand_poly(domain, rng)
                if sp.gcd(A, B).degree() > 0:
                    continue
                C = A + B
                if C.is_zero or max(A.degree(), B.degree(), C.degree()) <= 0:
                    continue
                if sp.gcd(A, C).degree() > 0 or sp.gcd(B, C).degree() > 0:
                    continue
                if domain != sp.QQ and max(A.degree(), B.degree(), C.degree()) >= 11:
                    continue  # stay in char > deg regime
                tested += 1
                cert = mason_stothers_certificate(
                    A.as_expr(), B.as_expr(), C.as_expr(),
                    domain=domain, require_hypotheses=False)
                drad = _indep_rad_deg_gcd_squarefree((A * B * C).as_expr(), domain)
                if drad != cert.deg_rad_ABC:
                    rad_mismatch += 1          # two radical routes disagree
                maxd = max(A.degree(), B.degree(), C.degree())
                if not cert.W_is_zero:
                    if maxd > drad - 1:
                        violations += 1        # bound (conclusion) fails
                    if not cert.verified:
                        unverified_valid += 1  # certificate failed a valid triple
        # the corpus is nonempty and both routes agree everywhere
        self.assertGreater(tested, 300, "seeded corpus should exceed 300 triples")
        self.assertEqual(violations, 0, "bound must hold on every tested triple")
        self.assertEqual(rad_mismatch, 0, "factor_list and gcd-squarefree radicals must agree")
        self.assertEqual(unverified_valid, 0, "certificate must verify every valid triple")


if __name__ == "__main__":
    unittest.main()
