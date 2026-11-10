"""Complete quadratic menu, outward fixed-point integer matrix contractions.

The source boxes and rational phase enclosure are inherited. The transform is
independent of the prior Bluestein FFT. No float enters a certificate. NumPy
int64 arithmetic is used only after explicit upper bounds rule out overflow.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROUND = HERE.parent.parent
ROOT = ROUND.parents[1]
sys.path[:0] = [str(ROOT), str(ROUND/'covariance_forge'),
               str(ROUND/'signal_frontier/prime_resonance')]
from intervals import Box, Interval, SCALE, phase
from pr_resonance import clock, source_xi

Q = 1 << 26
I64 = (1 << 63)-1


def ceildiv(a,b):
    return -((-a)//b)


def record(value):
    value = F(value)
    return {'numerator':value.numerator, 'denominator':value.denominator,
            'decimal_diagnostic':float(value)}


def quantize(box):
    """Return Gaussian integer center/Q and outward complex L1 radius/Q."""
    coords, radius = [], 0
    for v in (box.re, box.im):
        c = (v.lo+v.hi)*Q//(2*SCALE)
        coords.append(c)
        radius += ceildiv(max(abs(v.lo*Q-c*SCALE), abs(v.hi*Q-c*SCALE)), SCALE)
    return tuple(coords),radius


def root_table(p):
    values = [quantize(phase(-j,p)) for j in range(p)]
    return np.asarray([x for x,r in values],dtype=np.int64), max(r for x,r in values)


def source_boxes(row):
    return [Box(Interval(*v[:2]),Interval(*v[2:])) for v in row['B']]


def direct_box(xs, boxes, p, a, b):
    total = Box()
    for x,z in zip(xs,boxes):
        total = total + z*phase(-a*x*x-b*x,p)
    return total.divide(len(xs))


def scan(xs, boxes, p, h, *, chunk=32, verbose=False, retain=False):
    """Certify all p² coefficients; optionally retain for small test cases."""
    if p < 3 or p % 2 == 0 or len(set(xs)) != len(xs):
        raise ValueError('odd modulus >=3 and distinct support required')
    if p*p >= I64 or any(type(x) is not int or not 0 <= x < p for x in xs):
        raise ValueError('residue representatives and bounded modular index products required')
    m=len(xs)
    if not m or chunk < 1:
        raise ValueError('nonempty support and positive chunk required')
    roots,rt = root_table(p)
    centered = [quantize(z) for z in boxes]
    cb=max(abs(x)+abs(y) for (x,y),r in centered)
    if cb >= I64:
        raise ValueError('quantized input centers exceed signed-int64 range')
    bc=np.asarray([c for c,r in centered],dtype=np.int64)
    rb=max(r for c,r in centered)
    cr=max(int(abs(x)+abs(y)) for x,y in roots)
    assert cb*cr < I64
    product_radius=2*rb+ceildiv(rt*cb,Q)+2
    xsarr=np.asarray(xs,dtype=np.int64)
    bs=np.arange(p,dtype=np.int64)
    linear=roots[(xsarr[:,None]*bs[None,:])%p]
    best_linear=(-1,None)
    best_quad=(-1,None)
    digest=sha256()
    retained=[]
    fixed={(0,0),(1,1),(p-1,p-1),(p//3,p//5),(1,(-h)%p)}
    probes={}
    maximum_cp=0
    for start in range(0,p,chunk):
        aa=np.arange(start,min(p,start+chunk),dtype=np.int64)
        quad=roots[(aa[:,None]*(xsarr*xsarr%p)[None,:])%p]
        zr=(bc[None,:,0]*quad[:,:,0]-bc[None,:,1]*quad[:,:,1])//Q
        zi=(bc[None,:,0]*quad[:,:,1]+bc[None,:,1]*quad[:,:,0])//Q
        cp=int(np.max(np.abs(zr)+np.abs(zi)))
        maximum_cp=max(maximum_cp,cp)
        # Bounds every partial contraction, output coordinate, and L1 norm.
        # This also prevents overflow in each summand and intermediate +/-.
        assert m*cp*cr < I64
        re=zr@linear[:,:,0]-zi@linear[:,:,1]
        im=zr@linear[:,:,1]+zi@linear[:,:,0]
        digest.update(re.astype('<i8').tobytes())
        digest.update(im.astype('<i8').tobytes())
        if retain:
            retained.extend([(int(a),[(int(x),int(y)) for x,y in zip(rr,ii)])
                             for a,rr,ii in zip(aa,re,im)])
        for ia,a_ in enumerate(aa):
            a=int(a_)
            if a==0:
                for b,(x,y) in enumerate(zip(re[ia],im[ia])):
                    if (b+h)%p == 0:
                        continue
                    norm2=int(x)**2+int(y)**2
                    if norm2>best_linear[0]:
                        best_linear=(norm2,(a,b,int(x),int(y)))
            else:
                norms=np.abs(re[ia])+np.abs(im[ia])
                b=int(np.argmax(norms)); value=int(norms[b])
                if value>best_quad[0]:
                    best_quad=(value,(a,b,int(re[ia,b]),int(im[ia,b])))
            for a0,b0 in fixed:
                if a==a0:
                    probes[(a,b0)]=(int(re[ia,b0]),int(im[ia,b0]))
        if verbose and (start//chunk)%16==0:
            print('quadratic_rows',h,start,len(aa),'of',p,flush=True)
    # True mean - center/(m Q²), complex L1 <= err/Q².
    error_units=2*product_radius*Q+rt*maximum_cp
    denom=m*Q*Q
    linear_upper=F(isqrt(best_linear[0])+1,denom)+F(error_units,Q*Q)
    quadratic_upper=F(best_quad[0],denom)+F(error_units,Q*Q)
    for candidate in (best_linear[1],best_quad[1]):
        a,b,x,y=candidate; probes[(a,b)]=(x,y)
    direct=[]
    for (a,b),(x,y) in sorted(probes.items()):
        enclosure=direct_box(xs,boxes,p,a,b)
        # Stronger than overlap: whole direct enclosure lies inside radius ball.
        distance=F(max(abs(enclosure.re.lo*denom-x*SCALE),abs(enclosure.re.hi*denom-x*SCALE)),SCALE*denom)
        distance+=F(max(abs(enclosure.im.lo*denom-y*SCALE),abs(enclosure.im.hi*denom-y*SCALE)),SCALE*denom)
        assert distance <= F(error_units,Q*Q)
        direct.append({'a':a,'b':b,'center_numerator':[x,y],
                       'direct_box':[enclosure.re.lo,enclosure.re.hi,enclosure.im.lo,enclosure.im.hi],
                       'direct_distance_upper':record(distance)})
    result={'p':p,'m':m,'h':h,'Q':Q,'root_radius_units':rt,
            'input_radius_units':rb,'product_radius_units':product_radius,
            'maximum_product_center_L1':maximum_cp,'root_center_L1':cr,
            'overflow_bound':m*maximum_cp*cr,'overflow_limit':I64,
            'correlation_denominator':denom,
            'correlation_L1_error':record(F(error_units,Q*Q)),
            'linear_modulus_upper':record(linear_upper),
            'nonlinear_L1_upper':record(quadratic_upper),
            'linear_extremum':best_linear[1], 'nonlinear_L1_extremum':best_quad[1],
            'coefficients_evaluated':p*p,'nonresonant_atoms':p*p-1,
            'center_sha256':digest.hexdigest(),'direct_checks':direct,
            'direct_terms':len(direct)*m}
    if retain:
        result['centers']=retained
    return result


def certify(source, source_hash):
    p,m=source['p'],source['m']
    xs=clock(p,source_xi(p))
    assert len(xs)==m and m>2
    rows=[]
    for row in source['rows']:
        boxes=source_boxes(row)
        scan_result=scan(xs,boxes,p,row['h'],verbose=True)
        energy=sum((z.norm_squared() for z in boxes),Interval(0,0)).divide(m)
        wbox=Box(Interval(*row['W'][:2]),Interval(*row['W'][2:]))
        (wx,wy),wr=quantize(wbox)
        wup=F(isqrt(wx*wx+wy*wy)+1+wr,Q)
        e=F(energy.lo,SCALE)
        sqrtp_lower=F(isqrt(p*Q*Q),Q)
        w1=min(F(1),sqrtp_lower/m)
        w2=min(F(1),2*sqrtp_lower/m)
        def fraction(v): return F(v['numerator'],v['denominator'])
        M=max(fraction(scan_result['linear_modulus_upper'])/w1,
              fraction(scan_result['nonlinear_L1_upper'])/w2)
        floor=max(F(0),e-wup*wup)/(max(F(1),M)+wup)
        scan_result.update({'energy_lower':record(e),'W_abs_upper':record(wup),
                            'linear_weight_lower':record(w1),'quadratic_weight_lower':record(w2),
                            'M_upper':record(M),'rho_plus_atomwise_budget_lower':record(floor)})
        rows.append(scan_result)
        print('certified',row['h'],'M',float(M),'floor',float(floor),flush=True)
    return {'source_selector_A':source['A'],'source_interval':[source['n0'],source['last']],
            'source_receipt_sha256':source_hash,'source_reused_development':True,
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'protocol_sha256':sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
            'rows':rows,'scope':'Complete mixed-quadratic atomwise PR8 budget, finite only; unrestricted free resonance.',
            'pi_normality':'OPEN','RH':'OPEN'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    raw=args.source.read_bytes()
    result=certify(json.loads(raw),sha256(raw).hexdigest())
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__': main()
