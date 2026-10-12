#!/usr/bin/env python3
"""Machine-readable exact Gaussian sieve-Haar calibration, not a prime walk."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.coverage_sieve_crt import gaussian_sieve_crt_certificate
if __name__=='__main__':
 r=gaussian_sieve_crt_certificate(((1,2),(2,3)))
 print(json.dumps(r,default=str,indent=2,sort_keys=True))
