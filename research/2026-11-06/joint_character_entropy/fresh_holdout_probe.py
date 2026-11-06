"""Commit-first holdouts registered at SHA 6659899812abee3ae6625907212c8d991dfbf6ee.

These A=239,503 / h=3 cases were not inspected before the addendum commit.
Finite rational interval only; no asymptotic inference.
"""
from __future__ import annotations
import json
import hashlib
from fractions import Fraction
from signed_certificate import certified_weyl, source_completed_samples, short_receipt

ADDENDUM_SHA256='98d45acdaa6c62a87dceef23fdf9e3ee6f50d441632b2ce354654dbe4ecfb0d7'
GITHUB_COMMIT='6659899812abee3ae6625907212c8d991dfbf6ee'


def main() -> dict:
    assert hashlib.sha256(open('PREREG_ADDENDUM.md','rb').read()).hexdigest()==ADDENDUM_SHA256
    entries=[]
    for A in (239,503):
        z=source_completed_samples(A,depth=12)
        r=short_receipt(certified_weyl(z,3))
        entries.append({'A':A, **r})
    root=short_receipt(certified_weyl(tuple((Fraction(i,16),Fraction(i,16)) for i in range(16)),3))
    periodic=short_receipt(certified_weyl(tuple((Fraction(1,5),Fraction(1,5)) for _ in range(239)),3))
    assert Fraction(root['rigorous_upper_ceil_12dp'])<Fraction(1,10**6)
    assert Fraction(periodic['rigorous_lower_floor_12dp'])>Fraction(99,100)
    return {'status':'OBSERVED-FINITE / RIGOROUS RATIONAL INTERVAL','infinite_time_status':'OPEN',
            'prereg_sha256':ADDENDUM_SHA256,'prereg_commit':GITHUB_COMMIT,
            'fresh_epochs_h_3':entries,'rootgrid_h_3':root,'periodic_beta_1_5_h_3':periodic}

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
