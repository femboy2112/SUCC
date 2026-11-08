"""Same-forcing hostile seeds with exact original terminal denominator.

Every candidate is nonzero; this is a partial-authentication obstruction,
not a counterexample to the literal-zero pi source.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd, lcm, prod
import importlib.util
from observational_succ.selected_orbit import original_forcing

ROOT=Path(__file__).resolve().parents[4]
_prior_path=ROOT/'research/2026-11-07/learning_yoneda/arithmetic/finite_adelic.py'
_spec=importlib.util.spec_from_file_location('covforge_prior_adelic',_prior_path)
prior=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prior)


def history(B,seed=Q(0)):
    prior.exact_integer(B,'B')
    out=[prior.exact_rational(seed,'seed')]
    for n in range(1,B+1):
        out.append(16*out[-1]+original_forcing(n))
    return out


def order16(p):
    prior.odd_prime(p)
    m,x=1,16%p
    while x!=1:
        x=16*x%p
        m+=1
    return m


def selected_prime(A):
    prior.exact_integer(A,'A',1)
    for p in reversed(prior.primes_through(4*A)):
        if p%8==1 and order16(p)**3>p:
            return p
    raise ValueError('no good prime at this small epoch')


def forced_primes(B):
    prior.exact_integer(B,'B',17)
    return tuple(p for p in prior.primes_through(8*B-7)
                 if B<p<=4*B or (4*B<p and p%4==1))


def precision_capacity(q,t,B,eta):
    """Largest nonnegative K satisfying (t+1)*2^K*16^B <= eta*q, or -1."""
    prior.exact_integer(q,'q',1)
    prior.exact_integer(t,'t')
    prior.exact_integer(B,'B')
    eta=prior.exact_rational(eta,'eta')
    if eta<=0:
        raise ValueError('eta must be positive')
    ratio=eta*q/((t+1)*16**B)
    floor_ratio=ratio.numerator//ratio.denominator
    return floor_ratio.bit_length()-1


def construct(J,A,L,K,eta,observed_primes):
    for name,value in [('J',J),('A',A),('L',L),('K',K)]:
        prior.exact_integer(value,name)
    eta=prior.exact_rational(eta,'eta')
    observed=prior.prime_set(observed_primes)
    if not (J<A and L>=1 and 0<eta<Q(1,4)):
        raise ValueError('invalid chronology or precision')
    B=A+L-1
    allowed=forced_primes(B)
    used=tuple(p for p in allowed if p not in observed)
    if not used:
        raise ValueError('no unobserved original terminal primes')
    q=prod(used)
    t=len(used)
    if t>=min(used):
        raise ValueError('candidate-avoidance hypothesis t<min prime(q) failed')
    if q*eta < (t+1)*2**K*16**B:
        raise ValueError('original terminal support has insufficient seed precision')
    u=history(B)
    a,d=u[B].numerator,u[B].denominator
    if d%q or any((d//p)%p==0 for p in used):
        raise ValueError('source prime-product theorem failed on this finite state')
    M=prior.ceilq(u[B]/16**(B-A))
    center=Q(M,16**A)-u[B]/16**B
    m0=max(1,prior.ceilq(q*center/2**K))
    scale=16**B*2**K*(d//q)
    candidates=[m for m in range(m0,m0+t+1) if gcd(a+scale*m,d)==1]
    if not candidates:
        raise AssertionError('proved candidate-avoidance conclusion failed')
    m=candidates[0]
    s=Q(2**K*m,q)
    return {'J':J,'A':A,'L':L,'K':K,'eta':eta,'B':B,'q':q,'t':t,
            'used_primes':used,'observed_primes':observed,'M':M,'center':center,
            'm0':m0,'m':m,'skipped_candidates':m-m0,'seed':s,
            'original':u,'shadow':history(B,s),
            'precision_capacity':precision_capacity(q,t,B,eta)}


def verify(w):
    B,A,L,J,K=(w[k] for k in ('B','A','L','J','K'))
    u,v,s=w['original'],w['shadow'],w['seed']
    D=lcm(*(x.denominator for x in u))
    assert s>0 and s<1
    assert u[B].denominator==v[B].denominator
    assert u[B].denominator%s.denominator==0
    assert 0<=s-w['center']<=w['eta']/16**B
    assert w['precision_capacity']>=K
    for n in range(B+1):
        assert v[n]-u[n]==16**n*s
        assert D%v[n].denominator==0
        assert prior.residue(v[n]-u[n],2**(K+4*n))==0
        for p in w['observed_primes']:
            assert prior.principal(v[n],p)==prior.principal(u[n],p)
    margin=min(1-x%1 for x in u[:J+1])
    assert 16**J*s<margin
    assert all(v[n]//1==u[n]//1 for n in range(J+1))
    assert all(v[n]//1-16*(v[n-1]//1)==u[n]//1-16*(u[n-1]//1)
               for n in range(1,J+1))
    residues=[]
    for n in range(A,B+1):
        tail=sum((original_forcing(j)/16**(j-n) for j in range(n+1,B+1)),Q(0))
        residual=v[n]-16**(n-A)*w['M']
        assert residual==-tail+16**n*(s-w['center'])
        assert abs(residual)<=max(Q(1,15*(n+1)**2),w['eta']*Q(16**n,16**B))
        residues.append(residual)
    mean_square=sum((r*r for r in residues),Q(0))/L
    signed={h:1-20*h*h*mean_square for h in (1,2,3,5)}
    seed_primes=tuple(p for p in w['used_primes'] if s.denominator%p==0)
    assert seed_primes
    # All seed primes are from the original terminal source but appear too early.
    birth=lambda p: (p+7)//8 if p%8==1 else ((p+3)//8 if p%8==5 else (p+1)//4)
    births=tuple(birth(p) for p in seed_primes)
    return {'union_denominator':D,'signed_lower':signed,'seed_primes':seed_primes,
            'mean_square':mean_square,
            'earliest_original_seed_prime_birth':min(births),
            'latest_original_seed_prime_birth':max(births)}
