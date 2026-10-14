"""Independent 70-digit calibration of exact Gamma chiral identities.

This uses mpmath ONLY as a numerical holdout; none of its numbers is a proof
certificate or a nontrivial zeta-zero input. The exact verifier is the separate
Fraction implementation plus the paper Fourier/partial-fractions arguments.
"""
import argparse
import json
from pathlib import Path
from fractions import Fraction as Q
from mpmath import mp


def run_oracle():
    mp.dps=70
    outcome=[]
    for xi in (Q(0),Q(1,3),Q(1),Q(2),Q(10),Q(40)):
        x=mp.mpf(xi.numerator)/xi.denominator
        def phi(n):
            n=mp.mpf(n)
            return 4/(n*(n*n/4+x*x))
        # Independent source: direct L(s,chi_4) pair sum.
        sum_source=mp.nsum(lambda j:phi(4*j+1)-phi(4*j+3),[0,mp.inf])
        target=mp.pi*(1-mp.sech(mp.pi*x))/x**2 if x else mp.pi**3/2
        gamma_source=(mp.pi-abs(mp.gamma(mp.mpf('.5')+1j*x))**2)/x**2 if x else mp.pi**3/2
        cosine_source=(mp.quadosc(lambda t:mp.sech(t)*mp.cos(2*x*t),
                                    [0,mp.inf],omega=2*x) if x
                       else mp.quad(lambda t:mp.sech(t),[0,mp.inf]))
        # Sum pair <-> Fourier cosine transform of sech; sigma=(pi-2*cosine)/xi².
        maxerr=max(abs(sum_source-target),abs(target-gamma_source),
                   abs(cosine_source-mp.pi/2*mp.sech(mp.pi*x)))
        if maxerr>mp.mpf('1e-40'):
            raise ArithmeticError('independent analytic calibration failed')
        outcome.append({'xi':str(xi),'summed_mode_value':mp.nstr(sum_source,58),
                        'closed_Gamma_value':mp.nstr(gamma_source,58),
                        'closed_sech_value':mp.nstr(target,58),
                        'independent_cosine_transform':mp.nstr(cosine_source,58),
                        'max_absolute_residual':mp.nstr(maxerr,8)})
    return {'source':'independent mp analytic calibration; not theorem certificate',
            'precision_dps':70,'observations':outcome,
            'source_zero_coordinates_used':False,'RH_proved':False}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output')
    args=p.parse_args()
    txt=json.dumps(run_oracle(),sort_keys=True,indent=2)+'\n'
    if args.output:Path(args.output).write_text(txt,encoding='utf-8')
    else:print(txt,end='')


if __name__=='__main__':main()
