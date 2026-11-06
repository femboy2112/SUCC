"""Deterministic exact-Fraction alias-valve receipt; no pi digits."""
import json
import hashlib
import argparse
from pathlib import Path
from alias_valve import flux,coherent_odd_receipt,pair_energy,orbit,escape_receipt

GRID=((8,2),(12,4),(16,4),(24,8))


def row(A,q):
    f=flux(A,q)
    c=coherent_odd_receipt(A,q)
    orig=pair_energy(orbit(2*A-1)[A:2*A],q)
    ex=escape_receipt(orbit(2*A-1)[A:2*A],q,3)
    data={"A":A,"q":q,"authentic_J":str(orig),"source_positive_shear":str(f["positive_source_shear"]),"source_flux":str(f["signed_source_flux"]),"leakage":str(f["leak"]),"injection":str(f["injection"]),"boundary":str(f["boundary"]),"coherent_odd_J":str(c["J"]),"coherent_odd_bound":str(c["lower_bound"]),"terminal_depth":ex["terminal_depth"]}
    h=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return dict(A=A,q=q,exact_fraction_sha256=h,authentic_J_approx=f"{float(orig):.10f}",coherent_wrong_seed_J_approx=f"{float(c['J']):.10f}",source_flux_sign="positive" if f["signed_source_flux"]>0 else "negative",terminal_depth=ex["terminal_depth"])


def receipt():
    return dict(instrument="AV source-specific lag alias valve",base_main_sha="a673ec95dfac4ef6a61c60222be8b615fd08535d",algorithm="exact Fraction numeric data SHA256 canonical-json (sorted keys compact separators)",status="finite exact checks only; NOT normality",development_grid_not_blind_holdouts=True,rows=[row(A,q) for A,q in GRID])


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--write",type=Path)
    p.add_argument("--verify",type=Path)
    args=p.parse_args()
    data=receipt()
    output=json.dumps(data,indent=2,sort_keys=True)+"\n"
    if args.write: args.write.write_text(output)
    if args.verify:
        assert args.verify.read_text()==output,"receipt mismatch"
        print("EXACT_FRACTION_VALVE_RECEIPT_VERIFIED")
    if not args.write and not args.verify: print(output)
