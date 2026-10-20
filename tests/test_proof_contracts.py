"""Tests for quantifier-aware proof contracts, including the forbidden
pointwise->uniform quantifier swap."""
import unittest

from observational_succ.proof_contracts import (
    Quantifier, ProofContract, ProofContractError,
)


def _abc_contract():
    # forall eps>0, exists K_eps (dep eps), forall triple : c <= K rad^{1+eps}
    return ProofContract(
        name="abc",
        statement="c <= K_eps * rad(abc)^{1+eps}",
        prefix=[
            Quantifier("forall", "eps", "(0,inf)"),
            Quantifier("exists", "K", "(0,inf)", depends_on=("eps",)),
            Quantifier("forall", "triple", "coprime a+b=c"),
        ],
        hypotheses=["(a,b)=1", "a+b=c", "abc != 0"],
        constant_dependencies={"K": ["eps"]},
        finite_to_infinite="none; genuinely infinite family",
        source_authentic=True,
        method="OPEN (no proof)",
        status="CONJECTURED",
        open_obligations=["the entire theorem"],
    )


class TestUniformity(unittest.TestCase):
    def test_abc_K_uniform_in_triple_not_in_eps(self):
        c = _abc_contract()
        self.assertTrue(c.is_uniform_in("K", "triple"))   # K before triple
        self.assertFalse(c.is_uniform_in("K", "eps"))     # K depends on eps

    def test_prefix_string(self):
        c = _abc_contract()
        s = c.prefix_string()
        self.assertIn("A.eps", s)
        self.assertIn("E.K", s)
        self.assertIn("[dep:eps]", s)


class TestIllegalSwap(unittest.TestCase):
    def _pointwise(self):
        # forall N, exists C_N (dep N)
        return ProofContract(
            name="pointwise-bound",
            statement="Q_N(x) >= c_N |x|^2",
            prefix=[
                Quantifier("forall", "N", "naturals"),
                Quantifier("exists", "C", "(0,inf)", depends_on=("N",)),
            ],
            hypotheses=[], constant_dependencies={"C": ["N"]},
            finite_to_infinite="observed for finite N only",
            source_authentic=True, method="finite computation",
            status="TESTED MODEL",
        )

    def _bogus_uniform(self):
        # exists C, forall N   -- the illegal strengthening
        return ProofContract(
            name="claimed-uniform",
            statement="Q_N(x) >= c |x|^2 with c independent of N",
            prefix=[
                Quantifier("exists", "C", "(0,inf)"),
                Quantifier("forall", "N", "naturals"),
            ],
            hypotheses=[], constant_dependencies={"C": []},
            finite_to_infinite="ILLEGALLY asserted from finite N",
            source_authentic=True, method="hand-wave",
            status="UNVERIFIED",
        )

    def test_swap_is_rejected(self):
        pw = self._pointwise()
        bogus = self._bogus_uniform()
        self.assertFalse(pw.is_uniform_in("C", "N"))
        self.assertTrue(bogus.is_uniform_in("C", "N"))
        with self.assertRaises(ProofContractError):
            bogus.assert_not_uniformized_from(pw, "C", "N")

    def test_legitimate_uniform_from_uniform_is_ok(self):
        # if the source was ALREADY uniform, no illegal swap
        uni = self._bogus_uniform()
        other = self._bogus_uniform()
        other.assert_not_uniformized_from(uni, "C", "N")  # no raise


class TestPrefixValidation(unittest.TestCase):
    def test_dependency_on_later_var_rejected(self):
        with self.assertRaises(ProofContractError):
            ProofContract(
                name="bad",
                statement="...",
                prefix=[
                    Quantifier("exists", "K", "R", depends_on=("N",)),  # N is later!
                    Quantifier("forall", "N", "naturals"),
                ],
                hypotheses=[], constant_dependencies={},
                finite_to_infinite="", source_authentic=True,
                method="", status="UNVERIFIED",
            )

    def test_bad_status_rejected(self):
        with self.assertRaises(ProofContractError):
            ProofContract(
                name="x", statement="", prefix=[], hypotheses=[],
                constant_dependencies={}, finite_to_infinite="",
                source_authentic=True, method="", status="DEFINITELY-TRUE",
            )

    def test_mason_stothers_clean_forall(self):
        c = ProofContract(
            name="mason-stothers",
            statement="max(deg A,B,C) <= deg rad(ABC) - 1",
            prefix=[
                Quantifier("forall", "K", "fields char 0"),
                Quantifier("forall", "ABC", "coprime nonconstant A+B=C in K[x]"),
            ],
            hypotheses=["char K = 0 or char > deg", "pairwise coprime",
                        "not all constant", "A+B=C"],
            constant_dependencies={},
            finite_to_infinite="none; universally quantified, proved",
            source_authentic=True,
            method="Wronskian W=A'B-AB'; (ABC)/rad | W; degree comparison",
            status="CLASSICAL",
        )
        self.assertEqual(c.status, "CLASSICAL")
        self.assertEqual(len(c.open_obligations), 0)


if __name__ == "__main__":
    unittest.main()
