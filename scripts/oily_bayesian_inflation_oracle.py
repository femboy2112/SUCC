#!/usr/bin/env python3
"""High-precision independent numerical calibrations, NOT proof by fitting."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps=62


def L(x):
    return 1/((2-x*x)*(x*x-2*x+2))


def values(m):
    boundaries=[mp.mpf(0),mp.mpf('1e-9'),mp.mpf('1e-6'),mp.mpf('0.0001'),mp.mpf('0.001'),mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.4'),mp.mpf(1)]
    def raw(y):
        x=1-y
        return x**m*L(x)
    z0=mp.quad(lambda y:raw(y),boundaries)
    z1=mp.quad(lambda y:y*raw(y),boundaries)
    l0=mp.quad(lambda y:mp.log(y)*raw(y),boundaries)/z0
    l1=mp.quad(lambda y:y*mp.log(y)*raw(y),boundaries)/z1
    p_event=z1/z0
    d01=mp.log(p_event)-l0
    d10=l1-mp.log(p_event)
    j=d01+d10
    assert d01>0 and d10>0
    return {"m":m,"p_event":p_event,"m_times_p_event":m*p_event,
            "d_prior_post":d01,"d_post_prior":d10,"jeffreys":j,
            "err_gamma":d01-mp.euler,"err_one_minus_gamma":d10-(1-mp.euler)}


def main():
    results=[values(m) for m in (8,16,32,64,128,256)]
    for r in results:
        print('m=',r['m'],' P(A)=',mp.nstr(r['p_event'],18),' KL(p0||p1)=',mp.nstr(r['d_prior_post'],18),
              ' KL(p1||p0)=',mp.nstr(r['d_post_prior'],18),' J=',mp.nstr(r['jeffreys'],18))
    assert all(abs(results[i+1]['err_gamma'])<abs(results[i]['err_gamma']) for i in range(len(results)-1))
    assert abs(results[-1]['err_gamma'])<mp.mpf('0.003')
    out=Path('research/2026-10-28/INFLATION_PRIOR_OILY_KL_ORACLE.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps([{k:(v if isinstance(v,int) else mp.nstr(v,45)) for k,v in r.items()} for r in results],indent=2)+'\n')
    print('PASS independent numerical source diagnostics; paper Laplace theorem establishes limit.')

if __name__=='__main__':main()
