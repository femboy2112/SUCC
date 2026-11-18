from contextlib import redirect_stdout, redirect_stderr
from fractions import Fraction as F
from hashlib import sha256, sha1
from math import gcd
from pathlib import Path
import io, json, sys, time, unittest
from observational_succ.adelic_bbp_normality_crucible import construct_adelic_crt_shadow, terminal_uncollided_primes, z2_mod, domain_wall_counts
from observational_succ.borwein_quantitative_certificate import U

start=time.monotonic();buf=io.StringIO()
suite=unittest.defaultTestLoader.discover('tests',pattern='test_adelic_bbp_normality_crucible.py')
with redirect_stdout(buf),redirect_stderr(buf):
 result=unittest.TextTestRunner(stream=buf,verbosity=2).run(suite)
Path('focused_replay_raw.txt').write_text(buf.getvalue())
receipt={'pin':'97c7433371feca631991a1b8227b656e92e4abcb','focused_tests':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'elapsed_seconds':time.monotonic()-start,'native_test_disclaimer':'One test uses floating math.sin/math.pi; this is not an all-exact suite.','files':{},'denominator_counterexamples':[],'fit_failures':[]}
for p in ['observational_succ/adelic_bbp_normality_crucible.py','observational_succ/borwein_quantitative_certificate.py','tests/test_adelic_bbp_normality_crucible.py']:
 b=Path(p).read_bytes();receipt['files'][p]={'bytes':len(b),'sha256':sha256(b).hexdigest(),'git_blob':sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
# Independent hostile question, fixed finite domain before loop: B=2,...,80.
# Every claimed reduced denominator must remain Q. Preserve any first failure.
for B in range(2,81):
 source=U(2*B);q=source.denominator;n=source.numerator
 ps=terminal_uncollided_primes(2*B);prod=1
 for p,*_ in ps:prod*=p
 modulus=16**B*prod;r=n%modulus;common=gcd(r,q)
 if modulus>=q:receipt['fit_failures'].append({'B':B,'modulus':str(modulus),'Q':str(q)})
 if common>1 and len(receipt['denominator_counterexamples'])<5:
  v=F((n//q)//16**B*16**B)+F(r,q)
  shadow=construct_adelic_crt_shadow(B)
  assert v==shadow['V_sharp']
  receipt['denominator_counterexamples'].append({'B':B,'N':str(n),'Q':str(q),'Pi_star':str(prod),'modulus':str(modulus),'R_sharp':str(r),'gcd_R_Q':str(common),'reduced_shadow_denominator':str(v.denominator),'same_2adic_mod_16B':z2_mod(v,B)==z2_mod(source,B),'all_uncollided_principal_parts_match':all((v-source).denominator%p for p,*_ in ps),'domain_wall_counts':domain_wall_counts(v,B),'fits':r<q})
receipt['hostile_scan_B']=[2,80]
Path('replay_and_hostile_receipt.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps({'tests':result.testsRun,'success':result.wasSuccessful(),'first_counterexample':receipt['denominator_counterexamples'][:1],'fit_failures':receipt['fit_failures'],'elapsed_seconds':receipt['elapsed_seconds']},indent=2))
