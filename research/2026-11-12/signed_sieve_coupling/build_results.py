"""Generate a compact, independently inspectable finite evidence receipt."""
import hashlib
import json
from pathlib import Path
from signed_sieve import icbrt,masks,prime_mask,row,midpoint_haar,source_mutant,coeff
here=Path(__file__).resolve().parent
scan=json.loads((here/'scan_500k.json').read_text())
audit=json.loads((here/'audit_8192.json').read_text())
P=prime_mask(500000)
Ns=(20,100,256,512,1000,2048,4096,8192,100000,300094,500000)
rows=[row(N,P,icbrt(N)) for N in Ns]
mut=source_mutant(P)
q,_,_=masks(P,icbrt(1000))
c=bytearray(q[i]-mut[i] for i in range(len(q)))
s=[int(mut[i])-int(c[i]) for i in range(len(q))]
mutants={'N':1000,'source':'primes 1 mod 4','witnesses':coeff(mut,mut,1000),'signed_lower':coeff(q,s,1000)}
files=['signed_sieve.py','test_signed_sieve.py','independent_audit.py','exact_scan.cpp']
hashes={f:hashlib.sha256((here/f).read_bytes()).hexdigest() for f in files}
result={'date':'2026-11-12', 'scope':'finite only, exact rational/integer operations',
        'scan':scan,'independent_audit':audit,'sample_rows':rows,
        'signed_haar_example':midpoint_haar(2048,P,icbrt(2048)),
        'source_mutant':mutants,'source_hashes_sha256':hashes}
(here/'RESULTS.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({'sample_rows':len(rows),'scan_count':scan['scanned_even'],'source_mutant':mutants},sort_keys=True))
