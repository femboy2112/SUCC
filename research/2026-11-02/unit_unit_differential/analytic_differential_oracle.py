#!/usr/bin/env python3
"""Optional numerical cross-check of continuous x unit-differential mixed jets.

Paper authority comes from explicit positive densities, not quadrature.
"""
import mpmath as mp

mp.mp.dps=50
P=lambda v:4-2*v**3-v**4-v**5

def true_mixed(z,a,b):
    return mp.quad(lambda v:
        v**(8*z)*(-8*mp.log(v))**a*(1-v**8)**b*P(v)/(16-v**8),
        [0,mp.mpf('0.05'),mp.mpf('0.3'),1])

def subtracted_mixed(z,a,b):
    return mp.quad(lambda v:
        (v**16/16)**z*(mp.log(16)-16*mp.log(v))**a*
        (1-v**16/16)**b*(v**8/16)*P(v)/(16-v**8),
        [0,mp.mpf('0.05'),mp.mpf('0.3'),1])

def run():
    count=0
    for z in (mp.mpf(-1)/16,mp.mpf(0),mp.mpf(1)/2,mp.mpf(11)/4):
        for a,b in ((0,0),(1,0),(0,2),(1,3),(2,2)):
            v=true_mixed(z,a,b)
            u=v-subtracted_mixed(z,a,b)
            assert v>0 and mp.mpf(19)/20*v<=u<=v,(z,a,b)
            print(z,a,b,mp.nstr(u/v,18))
            count+=1
    print("ANALYTIC_MIXED_DIFFERENTIAL_NUMERIC_PASS",count)
if __name__=="__main__":run()
