"""Exact finite calibrations, not proofs of the asymptotic theorems."""
from fractions import Fraction as Q
import json


def forcing(n):
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def states(n):
    out=[Q(0)]
    for j in range(1,n+1):
        out.append(16*out[-1]+forcing(j))
    return out


def distance(x):
    t=x-x.numerator//x.denominator
    return min(t,1-t)


def source_tail_bound(n,ell=1):
    return Q(16*ell,(8*n+1)**3)


def sparse_interval(m,through):
    """beta=sum16^(-m^j), enclose after last exponent <=through."""
    if m<3: raise ValueError('m>=3')
    out=Q(0); d=1
    while d<=through:
        out+=Q(1,16**d)
        d*=m
    return out,out+Q(16,15*16**d),d


def sparse_fraction_interval(m,n,padding=12):
    """Direct fractional digit sum at time n; no pi or floating input."""
    out=Q(0); d=1
    while d<n: d*=m
    while d<=n+padding:
        out+=Q(1,16**(d-n+1))
        d*=m
    return out,out+Q(16,15*16**(d-n+1))


def sparse_lag_interval(m,n,h=1,ell=1,padding=16):
    """The fractional homogeneous orbit; exact rational interval with tail."""
    lo,hi,_=sparse_interval(m,n+ell+padding)
    mult=h*(16**ell-1)*16**(n-1)
    if mult<0: return mult*hi,mult*lo
    return mult*lo,mult*hi


def lag_tail_interval(n,ell=1,terms=10):
    lower=sum((Q(1,16**j)*(forcing(n+j)-forcing(n+ell+j))
               for j in range(1,terms+1)),Q(0))
    upper=lower+Q(1,16**terms)*source_tail_bound(n+terms,ell)
    return lower,upper


def distance_interval(lo,hi):
    if hi<lo: raise ValueError('unordered interval')
    err=hi-lo; d=distance(lo)
    return max(Q(0),d-err),min(Q(1,2),d+err)


def authentic_rows():
    rows=[]
    specs=[]
    for a in (19,37,61):
        htop=a**3//6
        for h in (1,htop//2,htop): specs.append((a,h,1))
    for a in (53,79,107):
        ell=a//26
        for h in (1,a**3//(12*ell),a**3//(6*ell)):
            specs.append((a,h,ell))
    u=states(max(8*a+ell for a,h,ell in specs))
    for a,h,ell in specs:
        dd=[distance(h*(u[n+ell]-u[n])) for n in range(a,8*a)]
        slips=[a+i for i,d in enumerate(dd) if d>=Q(1,20)]
        assert slips,(a,h,ell)
        rows.append(dict(A=a,h=h,ell=ell,window_length=7*a,
                         slip_count=len(slips),first_slip=slips[0],
                         largest_distance=str(max(dd)),
                         source_error_bound=str(h*source_tail_bound(a,ell))))
    return rows


def sparse_rows():
    rows=[]
    for m,nmax in ((3,245),(4,263),(5,629)):
        for h,ell in ((1,1),(3,1),(7,2),(11,5)):
            slips=0; ambiguous=0; energy_hi=Q(0)
            for n in range(1,nmax+1):
                lo,hi=sparse_lag_interval(m,n,h,ell)
                dlo,dhi=lag_tail_interval(n,ell)
                lo+=h*dlo;hi+=h*dhi
                dmin,dmax=distance_interval(lo,hi)
                slips+=dmin>=Q(1,20)
                ambiguous+=dmin<Q(1,20)<=dmax
                energy_hi+=20*dmax*dmax
            assert ambiguous==0
            rows.append(dict(m=m,N=nmax,h=h,ell=ell,slips=slips,
                             ambiguous=ambiguous,
                             energy_upper_integer=(energy_hi.numerator+energy_hi.denominator-1)//energy_hi.denominator,
                             energy_upper_decimal=float(energy_hi),
                             status='finite exact interval count; decimal display only'))
    return rows


def coherent_windows():
    rows=[]
    for m in (3,4,5):
        for j in (2,3,4):
            a=m**j+1;b=m**(j+1)-2
            # On this whole window homogeneous lag <=16^-2; source lag
            # <=16/(8A+1)^3. Both bounds are exact rational inequalities.
            bound=Q(1,256)+source_tail_bound(a)
            assert bound<Q(1,20)
            rows.append(dict(m=m,j=j,A=a,B=b,length=b-a+1,
                             uniform_distance_upper=str(bound),
                             threshold='1/20',certified_all_indices=True))
    return rows


def run():
    return dict(authentic_windows=authentic_rows(),sparse_controls=sparse_rows(),
                coherent_windows=coherent_windows(),
                warning='finite observations do not prove infinite results')

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
