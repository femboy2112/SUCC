"""Reproducible exact packet receipt; --source uses archived frozen Suzuki."""
import argparse
import json
from fractions import Fraction as F
from observational_succ.prime_gamma_packet_commutator import (
    first_gamma_rung_prime_commutator,original_source_commutator_witness,
)
from observational_succ.gamma_packet_certificates import (
    finite_repair_bound,original_fifth_mode_packet,paired_mode_negative_control,
)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",action="store_true")
    p.add_argument("--verify",action="store_true")
    a=p.parse_args()
    cal=finite_repair_bound(64,-F(740,10**6),-F(739,10**6),F(2136,77),1296)
    src=original_fifth_mode_packet() if a.source else None
    comm=original_source_commutator_witness() if a.source else first_gamma_rung_prime_commutator(F(693,1000),F(694,1000))
    if a.verify:
        assert F(cal["signed_energy_after_packet_lower"])>0
        assert F(comm["gamma_integral_strict_lower"])>F(3,16)
        if a.source:
            assert src["source_git_blob"]=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
            assert F(src["signed_prefix_interval"][1])<0
            assert F(src["signed_energy_after_packet_lower"])>0
            assert not src["S4_positive_proved"]
    print(json.dumps({"program":"SOURCE_GAMMA_RUNG_PACKET_2026_10_18",
            "rational_synthetic_control":cal,
            "cross_mode_surrogate":paired_mode_negative_control(),
            "prime_gamma_commutator":comm,
            "original_source_packet":src,
            "RH_proved":False,
            "verification":"PASS" if a.verify else "UNVERIFIED"},sort_keys=True))


if __name__=="__main__":
    main()
