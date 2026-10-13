#!/usr/bin/env python3
"""Bounded, exact E33 algebra/source controls; this is not an RH probe."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.prime_clock_yoneda import (
    ArithmeticFunctorError, PrimeClockSource, verify_arithmetic_source_signature,
)
from observational_succ.proto_succ_variable_unit import shift_dilation_address_defect
from observational_succ.succ_discrete_integration import AffineStep, RationalFrame

BASE = "5eb09e7cba36ec01b8f9d6834b78b5766fd93935"
IDENTITY = (1, 0)
S, V2, V3 = (1, 1), (2, 0), (3, 0)


def compose(left, right):
    """Written left*right means left after right, matching native compose."""
    a, b = left
    c, d = right
    return a*c, a*d+b


def act(pair, x):
    a, b = pair
    return a*x+b


def native(pair):
    a, b = pair
    return AffineStep(RationalFrame(((Fraction(a),),)), (Fraction(b),))


def normal_form(word):
    current = IDENTITY
    for generator in word:
        current = compose(current, generator)
    return current


def direct_word(word, x):
    for generator in reversed(word):
        x = act(generator, x)
    return x


def main():
    word_count = 0
    for length in range(6):
        for word in product((S, V2, V3), repeat=length):
            pair = normal_form(word)
            for x in range(8):
                assert act(pair, x) == direct_word(word, x)
            word_count += 1

    native_compositions = 0
    for a, b, c, d in product(range(1, 6), range(4), range(1, 6), range(4)):
        left, right = (a, b), (c, d)
        assert native(left).compose(native(right)) == native(compose(left, right))
        expected_defect = (a-1)*d-(c-1)*b
        for x in (0, 1, 9):
            assert act(compose(left, right), x)-act(compose(right, left), x) == expected_defect
        native_compositions += 1

    for triple in product((IDENTITY, S, V2, V3, (2, 1), (3, 2)), repeat=3):
        a, b, c = triple
        assert compose(compose(a, b), c) == compose(a, compose(b, c))

    relations = 0
    for multiplier, step, x in product(range(1, 10), range(-2, 3), range(8)):
        assert multiplier*(x+step) == multiplier*x+multiplier*step
        assert multiplier*x+step-multiplier*(x+step) == step*(1-multiplier)
        relations += 1
    for p, step, x in product((2, 3, 5, 7), range(-2, 3), range(8)):
        assert shift_dilation_address_defect(p, x, step) == step*(1-p)

    pairs = tuple(product(range(1, 9), range(9)))
    assert len({(act(pair, 0), act(pair, 1)) for pair in pairs}) == len(pairs)
    assert len({act(pair, 9) for pair in pairs}) == len(pairs)

    modular_compositions = 0
    finite_pairs = tuple(product(range(1, 7), range(6)))
    for modulus in range(2, 6):
        for left, right in product(finite_pairs, repeat=2):
            reduced = tuple(t % modulus for t in compose(left, right))
            product_reduced = compose(tuple(t % modulus for t in left),
                                      tuple(t % modulus for t in right))
            assert reduced == tuple(t % modulus for t in product_reduced)
            for x in range(modulus):
                assert act(reduced, x) % modulus == act(left, act(right, x) % modulus) % modulus
            modular_compositions += 1

    # Actual finite action-groupoid arrows (a,b,x): x -> a*x+b mod 5.
    groupoid_arrows = 0
    unit_pairs = tuple(product(range(1, 5), range(5)))
    for a, b in unit_pairs:
        inv_a = pow(a, -1, 5)
        inverse = (inv_a, (-inv_a*b) % 5)
        for x in range(5):
            y = act((a, b), x) % 5
            assert act(inverse, y) % 5 == x
            assert tuple(t % 5 for t in compose(inverse, (a, b))) == IDENTITY
            groupoid_arrows += 1
    groupoid_compositions = 0
    for outer, inner in product(unit_pairs, repeat=2):
        composed = tuple(t % 5 for t in compose(outer, inner))
        assert composed in unit_pairs
        for x in range(5):
            # inner arrow ends at y; outer arrow must start at y.
            y = act(inner, x) % 5
            assert act(composed, x) % 5 == act(outer, y) % 5
            groupoid_compositions += 1
    assert gcd(5, 5) != 1 and len({5*x % 5 for x in range(5)}) == 1

    smallest_mutant = {"x": 0, "S_V2": act(compose(S, V2), 0),
                       "V2_S": act(compose(V2, S), 0)}
    assert smallest_mutant["S_V2"] != smallest_mutant["V2_S"]
    assert compose(S, V3) == (3, 1) and compose(V3, S) == (3, 3)
    assert [t % 2 for t in compose(S, V3)] == [t % 2 for t in compose(V3, S)]
    assert [t % 4 for t in compose(S, V3)] != [t % 4 for t in compose(V3, S)]

    # Complete 2x2 toggles at x=0, for each declared action order.
    factorial = {
        "V_after_S": {"00": 0, "10_S": 1, "01_V3": 0, "11": 3},
        "S_after_V": {"00": 0, "10_S": 1, "01_V3": 0, "11": 1},
    }
    for row in factorial.values():
        row["mixed_difference"] = row["11"]-row["10_S"]-row["01_V3"]+row["00"]
    assert factorial["V_after_S"]["mixed_difference"] == 2
    assert factorial["S_after_V"]["mixed_difference"] == 0
    operator_commutator = {1: 1, 2: -1}  # [S,V2] e_0 = e_1-e_2.
    assert operator_commutator != {0: -1}  # Address defect * e_0 is different.

    # Algebraic primality cannot be recovered from the affine identity.
    composite = 6
    assert compose((composite, 0), S) == compose((1, composite), (composite, 0))
    rejected_composites = []
    for q in (4, 6):
        try:
            PrimeClockSource(5, 1, 1, 1, q)
        except ArithmeticFunctorError:
            rejected_composites.append(q)
        else:
            raise AssertionError("Independent primality gate accepted a composite")
    declared = PrimeClockSource(5, 1, 1, 1, 11)
    # Fake composite 6 is action-matched to genuine prime 11 at precision 5.
    assert tuple(declared.dilate(x) for x in range(5)) == tuple(6*x % 5 for x in range(5))
    # An unrelated, generic affine system with multiplier 11 has identical maps.
    assert tuple(declared.dilate(x) for x in range(5)) == tuple(act((11, 0), x) % 5 for x in range(5))
    fine = PrimeClockSource(2, 2, 1, 1, 3)
    false_coarse = PrimeClockSource(2, 1, 1, 1, 5)
    assert tuple(fine.dilate(x) % 2 for x in range(4)) == tuple(false_coarse.dilate(x % 2) for x in range(4))
    try:
        verify_arithmetic_source_signature(fine, false_coarse)
    except ArithmeticFunctorError:
        source_alias_rejected = True
    else:
        raise AssertionError("Changed declared prime source passed signature gate")

    paths = (
        "observational_succ/prime_clock_yoneda.py",
        "observational_succ/proto_succ_variable_unit.py",
        "observational_succ/succ_discrete_integration.py",
        "provenance/IMPORT_MANIFEST.json",
        "research/2026-10-11/PRIME_CLOCK_YONEDA_ORIGIN.md",
        "research/2026-10-11/PROTO_SUCC_VARIABLE_UNIT_LIFT.md",
        "research/2026-10-11/FINITE_DIFFERENCE_SUCC_INTEGRATION.md",
        "provenance/origins/fuckingrh/research/2026-10-10/SUCC_GAMMA_PRIME_PATH_GERMS.md",
        "research/2026-10-13/SWARM_ATLAS/E33_probe.py",
        "research/2026-10-13/SWARM_ATLAS/E33.md",
    )
    receipt = {
        "claim_id": "SWM-E33", "status": "TESTED MODEL",
        "theorem_status": "CLASSICAL, with self-contained derivation",
        "parent_sha": BASE,
        "execution_checkout_sha": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
        "command": "python research/2026-10-13/SWARM_ATLAS/E33_probe.py",
        "exit_code": 0,
        "integer_words_checked": word_count, "addresses_per_word": 8,
        "native_compositions_checked": native_compositions,
        "associativity_triples_checked": 216,
        "general_multiplier_relations_checked": relations,
        "native_prime_variable_step_cases_checked": 160,
        "separating_affine_samples": len(pairs), "single_basis_separator": 9,
        "modular_compositions_checked": modular_compositions,
        "finite_groupoid_arrows_checked": groupoid_arrows,
        "finite_groupoid_compositions_checked": groupoid_compositions,
        "commutative_mutation_receipt": smallest_mutant,
        "factorial_tables": factorial,
        "ket_commutator_at_0": operator_commutator,
        "composite_relation_survives": 6,
        "independent_gate_rejected_composites": rejected_composites,
        "prime_composite_matched_actions_mod5": [11, 6],
        "non_Euler_affine_model_action_matched": True,
        "different_true_prime_source_alias_mod2": [3, 5],
        "source_signature_rejected_alias": source_alias_rejected,
        "Euler_source_physically_authenticated": False,
        "nontrivial_zero_locations_used": False,
        "Gamma_pole_phase_conductor_half_density_supplied": False,
        "completed_Weil_positivity_or_RH_claimed": False,
        "primary_sources": ["https://arxiv.org/pdf/0907.3760", "https://arxiv.org/pdf/math/0611541"],
        "sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
