"""Exact deterministic seed-conductor receipt: Fractions hashed, decimals display only."""
import json, hashlib, argparse
from pathlib import Path
from math import log
from source_native_seed import native_epoch, original_orbit, energy

GRID=((40,8),(48,8),(64,16),(96,16))
def row(A,q):
    x=native_epoch(A)
    J0=energy(original_orbit(2*A-1)[A:2*A],q)
    Js=energy(x['phase_cloud'],q)
    raw={"A":A,"q":q,"source_conductor":str(x['B']),"seed":str(x['seed']),
         "alignment":str(x['alignment']),"width":str(x['width']),
         "J_original":str(J0),"J_counterseed":str(Js)}
    digest=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {"A":A,"q":q,"B_bits":x['current_bits'],"seed_denominator_bits":x['seed_bits'],
            "margin_B_gt_4A2_16power2A":x['certified_early'],
            "scaled_width_A2_display":format(float(x['width']*A*A),'.12f'),
            "J_original_display":format(float(J0),'.12f'),
            "J_counterseed_display":format(float(Js),'.12f'),
            "exact_fraction_digest_sha256":digest}

def receipt():
    return {"program":"SUCC original BBP source-native counterseed","label":"FINITE OBSERVED / ASYMPTOTIC LEMMA HAS PAPER PROOF",
            "base_PR_492":"c283afc257d76287b7563628eecf63ba225c2df9",
            "method":"exact Fraction numerator/denominator; SHA256 over canonical JSON exact tuple",
            "development_grid_not_blind":True,
            "original_U0":0,"pi_normality":"OPEN", "rows":[row(*x) for x in GRID]}

def content():return json.dumps(receipt(),indent=2,sort_keys=True)+'\n'
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',type=Path);p.add_argument('--verify',type=Path)
    a=p.parse_args();t=content()
    if a.write:a.write.write_text(t)
    if a.verify:
        assert a.verify.read_text()==t,'receipt changed'
        print('SOURCE_NATIVE_SEED_FRACTION_RECEIPT_VERIFIED')
    if not a.write and not a.verify:print(t)
