"""Golden-node and source-clock numerical corroboration, no interval claim."""
from pathlib import Path
from hashlib import sha256
import argparse,json
import mpmath as mp
from oracle import source_mass,R
HERE=Path(__file__).resolve().parent

def qmp(x):return mp.mpf(x.numerator)/x.denominator

def run():
    ambient=mp.mp.dps;rows=[];calibrations=[];checks=0
    with mp.workdps(100):
        alpha=(mp.sqrt(5)-1)/2
        for m in (2,3,6,9,12):
            H=(m+1)//2;a=8*m-7
            q=[qmp(x) for x in source_mass(a,m)]
            nodes=[mp.exp(2j*mp.pi*j*alpha) for j in range(m+1)]
            A=mp.matrix([[mp.mpf(1)]*(m+1)]+
                [[part(nodes[j]**h) for j in range(m+1)]
                    for h in range(1,H+1) for part in (mp.re,mp.im)])
            # Means obtained directly from the source masses; independent QR solve.
            moments=[sum(q[j]*nodes[j]**h for j in range(m+1)) for h in range(1,H+1)]
            y=mp.matrix([1]+[part(v) for v in moments for part in (mp.re,mp.im)])
            recovered,residual=mp.qr_solve(A,y)
            error=max(abs(recovered[j]-q[j]) for j in range(m+1))
            assert error<mp.mpf('1e-90');checks+=1
            gram=A.T*A
            vals=mp.eigsy(gram,eigvals_only=True)
            cond=mp.sqrt(vals[-1,0]/vals[0,0]) if vals.rows==1 else mp.sqrt(vals[vals.rows-1,0]/vals[0,0])
            calibrations.append({'depth':m,'harmonics':H,'holdout':m in (9,12),
                'max_mass_error':mp.nstr(error,12),'condition_number':mp.nstr(cond,25)})
        for a in (8,32):
            beta=mp.mpf(a)/8;ra=qmp(R(a))
            for m in (8,16,32,64):
                q=[qmp(x) for x in source_mass(a,m)]
                for h in (1,3):
                    z=mp.exp(2j*mp.pi*h*alpha)
                    actual=sum(q[j]*z**j for j in range(m+1))
                    ch=1-mp.re(z)
                    bound=mp.gamma(beta)/(2*ra)*(2/(ch*m))**beta+15*max(1,mp.power(2,1-beta))/(8*ra*ch**2*m**2)
                    assert abs(actual)<=bound;checks+=1
                    if m in (8,32) and h==1:
                        # Fresh continuous positive-source integral, no endpoint-mass polynomial.
                        def integrand(x):
                            f=mp.exp(-8*x)
                            Q=2*(-mp.expm1(-3*x))-mp.expm1(-4*x)-mp.expm1(-5*x)
                            return mp.exp(-a*x)*Q*(f+(1-f)*z)**m/ra
                        direct=mp.quad(integrand,[0,mp.mpf(1)/8,1,mp.inf])
                        assert abs(direct-actual)<mp.mpf('1e-85');checks+=1
                    rows.append({'clock':'fixed_a','a':a,'m':m,'h':h,'abs_character':mp.nstr(abs(actual),25),
                                 'proved_envelope':mp.nstr(bound,25),'nonvacuous_bound':bool(bound<1)})
        for m in (8,16,32,64):
            a=8*m-7;q=[qmp(x) for x in source_mass(a,m)]
            for h in (1,3):
                z=mp.exp(2j*mp.pi*h*alpha)
                actual=sum(q[j]*z**j for j in range(m+1));limit=(2-z)**(-2)
                rows.append({'clock':'native','a':a,'m':m,'h':h,'abs_character':mp.nstr(abs(actual),25),
                             'abs_nonzero_limit':mp.nstr(abs(limit),25),'distance_to_limit':mp.nstr(abs(actual-limit),25)})
    assert mp.mp.dps==ambient
    return {'status':'PASS','authority':'100-digit numerical corroboration; no interval or universal certificate',
            'checks':checks,'reconstruction_cases':calibrations,'source_clock_cases':rows,
            'ambient_precision_preserved':True,'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'oracle_sha256':sha256((HERE/'oracle.py').read_bytes()).hexdigest(),
            'pi_normality':'OPEN','RH':'OPEN'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.output.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n')
