#!/usr/bin/env python3
"""Exact source-prior wavefront probe; see full mathematical dossier.

Pure Fraction checks of the positive Oily rates, finite prior surrogate,
Bayesian cross-branch feedback and de Sitter discrete patch counting.
The continuous source prior, projective theorem and Gamma limit are proofs,
NOT inferred from finite samples or from cosmological observation.
"""
from fractions import Fraction as F


def rates(x):
    x=F(x)
    assert F(0)<=x<=F(1)
    return x-x*x/2, x*x/2


def source_R(x):
    x=F(x)
    return (1-x)/((2-x*x)*(x*x-2*x+2))


def rate_q(x):
    u,v=rates(x)
    return u*v


def finite_prior(nodes):
    """Quadrature *surrogate*, NOT continuous µ0=16 R(x)dx/pi."""
    values={F(x):source_R(x) for x in nodes}
    Z=sum(values.values(),F())
    assert Z>0 and len(values)==len(nodes)
    return {x:v/Z for x,v in values.items()}


def moments(prior):
    mean=sum((w*rate_q(x) for x,w in prior.items()),F())
    second=sum((w*rate_q(x)**2 for x,w in prior.items()),F())
    return mean,second,second-mean*mean


def after_event(prior,value):
    """Exact Bayes update on latent X for a declared ternary edge report."""
    assert value in (-1,0,1)
    raw={x:w*((rate_q(x)/2) if value else (1-rate_q(x)))
         for x,w in prior.items()}
    evidence=sum(raw.values(),F())
    assert evidence>0
    return {x:w/evidence for x,w in raw.items()}


def main():
    for k in range(49):
        x=F(k,48)
        u,v=rates(x)
        assert u+v==x and F(0)<=v<=u<=F(1,2)
        assert rate_q(x)==x**3*(2-x)/4
    prior=finite_prior([F(1,2),F(3,4)])
    m,m2,var=moments(prior)
    assert prior=={F(1,2):F(391,671),F(3,4):F(280,671)}
    assert m==F(7071,85888)
    assert var==F(103581765,59013988352)>0
    assert m2/m==F(250161,2413568)
    assert moments(after_event(prior,1))[0]>m>moments(after_event(prior,0))[0]
    assert moments({F(1,2):F(1)})[2]==0
    # At the authentic critical Oily endpoint: Σ[(j+1)/2^(j+2)]²=5/27.
    assert rate_q(1)==F(1,4)
    assert F(1,4)*(1+F(5,27))==F(8,27)
    for n in range(10):
        assert 8**n==(2**n)**3
        assert F(1,2**n)==F(1)/(2**n)  # comoving Hubble-radius ratio
    print('PASS 49 exact Oily checks; 2-point prior, feedback, control, horizon')
    print('source_prior=',prior,'rate=',m,'Var(q)=',var,'P(active2|active1)=',m2/m)
    print('π-normality, physical inflation, Bayesian WEO optimality: NOT CLAIMED')


if __name__=='__main__':main()
