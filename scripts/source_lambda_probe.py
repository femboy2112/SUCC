"""Deterministic, finite-only SUCC lambda demonstration and receipt."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.source_lambda import (  # noqa: E402
    Atlas, App, Forget, Join, Lam, Passport, Read, Residue, ResidueT,
    Sum, Var, check, compare_observers, execute, signed_witness,
)


def main() -> None:
    passport = Passport("source-lambda-demo", 1)
    zero = Atlas.from_integer(passport, 0, (2, 3, 5))
    six = Atlas.from_integer(passport, 6, (2, 3, 5))
    shallow = compare_observers(Forget(Read(2)), zero, six)
    deep = compare_observers(Forget(Read(5)), zero, six)
    f = Lam(ResidueT(5), Sum(Var(0), Forget(Read(5))))
    applied = App(f, Residue(5, 0))
    left = execute(applied, zero)
    right = execute(applied, six)
    crt = execute(Join(Read(2), Read(3)), six)
    witness = signed_witness(((1, 2), (2, 1)), (1, -1))

    assert shallow.status == "CERTIFIED_FINITE_AGREEMENT"
    assert deep.status == "NOT_CERTIFIED"
    assert left.value == 0 and right.value == 1
    assert crt.value.value == 0 and crt.observed == (2, 3)
    assert witness.energy == -2 and not witness.proves_rh

    receipt = {
        "source_id": passport.source_id,
        "epoch": passport.epoch,
        "program_type": "Residue(5)",
        "latent_function_reads": sorted(check(f, passport).type.latent_reads),
        "applied_program_potential_reads": sorted(check(applied, passport).may_read),
        "shallow_status": shallow.status,
        "deep_status": deep.status,
        "program_values": [left.value, right.value],
        "crt_derived_value_mod6": crt.value.value,
        "crt_actual_recorded_reads": list(crt.observed),
        "finite_signed_energy": str(witness.energy),
        "sign_status": witness.status,
        "global_completeness_proved": False,
        "actual_source_authenticated": False,
        "RH_proved": False,
    }
    print(json.dumps(receipt, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
