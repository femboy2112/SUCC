"""Exact source-native snapshot aliases and finite arrow tomography.

Research instrument; no pi-distribution or universal-carrier assertion.
"""
from fractions import Fraction as F
from math import comb
from itertools import product

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))
PATTERN = {'010': 1, '011': -1, '100': -1, '101': 1}


def source(a):
    a = F(a)
    if a <= 0:
        raise ValueError('positive source parameter')
    return sum((F(c)/(a+d) for d, c in POLES), F())


def power_moment(a, ones, zeros):
    """E[(1-exp(-8X))**ones * exp(-8X)**zeros]."""
    return sum(((-1)**j*comb(ones,j)*source(F(a)+8*(zeros+j))
                for j in range(ones+1)),F())/source(a)


def endpoint(a, m):
    return [comb(m,j)*power_moment(a,j,m-j) for j in range(m+1)]


def word_probability(a, word, altered=False):
    k = word.count('1')
    p = power_moment(a,k,len(word)-k)
    if altered and len(word)>=3:
        sign = PATTERN.get(word[:3],0)
        tail = word[3:]
        p += F(sign,2)*power_moment(a,2+tail.count('1'),2+tail.count('0'))
    return p


def conditional_word(p, word, altered=False):
    p = F(p); q = 1-p
    base = p**word.count('1') * q**word.count('0')
    if altered and len(word)>=3:
        tail = word[3:]
        base += F(PATTERN.get(word[:3],0),2)*p**(2+tail.count('1'))*q**(2+tail.count('0'))
    return base


def all_words(m):
    return (''.join(w) for w in product('01',repeat=m))


def native_joint(a,m,d):
    total = endpoint(a,m+d)
    return [[F(comb(m,i)*comb(d,k-i),comb(m+d,k))*total[k]
             if i<=k<=i+d else F() for k in range(m+d+1)]
            for i in range(m+1)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a,b):
    bt=transpose(b)
    return [[sum((x*y for x,y in zip(ar,bc)),F()) for bc in bt] for ar in a]


def inverse(a):
    n=len(a)
    if any(len(row)!=n for row in a): raise ValueError('square matrix')
    x=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((k for k in range(j,n) if x[k][j]),None)
        if pivot is None: raise ValueError('singular matrix')
        x[j],x[pivot]=x[pivot],x[j]
        v=x[j][j];x[j]=[w/v for w in x[j]]
        for i in range(n):
            if i!=j:
                v=x[i][j]
                x[i]=[u-v*w for u,w in zip(x[i],x[j])]
    return [row[n:] for row in x]


def rank(a):
    if not a:return 0
    b=[[F(v) for v in row] for row in a]
    nrow=len(b);ncol=len(b[0]);p=0
    for j in range(ncol):
        k=next((k for k in range(p,nrow) if b[k][j]),None)
        if k is None:continue
        b[p],b[k]=b[k],b[p]; v=b[p][j]
        b[p]=[w/v for w in b[p]]
        for i in range(p+1,nrow):
            v=b[i][j]
            b[i]=[u-v*w for u,w in zip(b[i],b[p])]
        p+=1
        if p==nrow:break
    return p


def edge_support(m,d):
    return [(i,k) for i in range(m+1) for k in range(i,i+d+1)]


def incidence(m,d):
    edges=edge_support(m,d)
    return [[F(i==v) for i,k in edges] for v in range(m+1)]+[
        [F(k==v) for i,k in edges] for v in range(m+d+1)]


def cycle(m,d,i,k):
    if not (0<=i<m and i+1<=k<i+d):raise ValueError('unsupported square')
    z=[[F() for _ in range(m+d+1)] for _ in range(m+1)]
    z[i][k]=z[i+1][k+1]=F(1)
    z[i][k+1]=z[i+1][k]=F(-1)
    return z


def cycle_basis(m,d):
    return [cycle(m,d,i,k) for i in range(m) for k in range(i+1,i+d)]


def margins(a):
    return ([sum(row,F()) for row in a], [sum(col,F()) for col in transpose(a)])


def perturb(j,z,epsilon):
    return [[v+epsilon*w for v,w in zip(a,b)] for a,b in zip(j,z)]


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F())


def mixed(a,f,g):
    return sum((v*f[i]*g[j] for i,row in enumerate(a) for j,v in enumerate(row)),F())


def cauchy(parameters,marks):
    return [[F(1)/(F(a)+F(x)) for x in marks] for a in parameters]


def tomography(j,left_parameters,right_parameters):
    c=cauchy(left_parameters,range(len(j)))
    d=cauchy(right_parameters,range(len(j[0])))
    measured=matmul(matmul(c,j),transpose(d))
    ci,di=inverse(c),inverse(d)
    restored=matmul(matmul(ci,measured),transpose(di))
    gain=max(sum(map(abs,row),F()) for row in ci)*max(sum(map(abs,row),F()) for row in di)
    return measured,restored,gain


def reconstruct_one_step(p,q):
    m=len(p)-1
    if len(q)!=m+2:raise ValueError('wrong layer widths')
    a=[]; b=[]
    for j in range(m+1):
        a.append(sum(q[:j+1],F())-sum(p[:j],F()))
        b.append(p[j]-a[-1])
    return [[a[i] if k==i else b[i] if k==i+1 else F()
             for k in range(m+2)] for i in range(m+1)]


def quadratic_multiply(a,b):
    return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def golden_power(n):
    value=(F(1),F())
    for _ in range(n):value=quadratic_multiply(value,(F(-1,2),F(1,2)))
    return value


def nullspace(a):
    """Exact rational nullspace in free-variable coordinates."""
    b=[[F(v) for v in row] for row in a];cols=len(b[0]);r=0;pivots=[]
    for col in range(cols):
        k=next((k for k in range(r,len(b)) if b[k][col]),None)
        if k is None:continue
        b[r],b[k]=b[k],b[r];v=b[r][col];b[r]=[x/v for x in b[r]]
        for i in range(len(b)):
            if i!=r:
                v=b[i][col];b[i]=[x-v*y for x,y in zip(b[i],b[r])]
        pivots.append(col);r+=1
        if r==len(b):break
    vectors=[]
    for free in range(cols):
        if free in pivots:continue
        v=[F()]*cols;v[free]=F(1)
        for row,col in enumerate(pivots):v[col]=-b[row][free]
        vectors.append(v)
    return vectors


def harmonic_golden_moments(z):
    """HH; Hλ (two rational coordinates); λH; λλ. γ offsets are marginal terms."""
    hh=F();hl=[F(),F()];lh=[F(),F()];ll=[F(),F()]
    for i,row in enumerate(z):
        for k,v in enumerate(row):
            h,g=harmonic(i),harmonic(k)
            u,w=golden_power(i),golden_power(k)
            hh+=v*h*g
            for t in range(2):
                hl[t]+=v*h*w[t];lh[t]+=v*u[t]*g
            q=quadratic_multiply(u,w)
            for t in range(2):ll[t]+=v*q[t]
    return [hh,*hl,*lh,*ll]


def matched_arrow_direction(m,d):
    basis=cycle_basis(m,d)
    design=transpose([harmonic_golden_moments(z) for z in basis])
    vectors=nullspace(design)
    if not vectors:raise ValueError('probe family separates this cycle space')
    vector=vectors[0]
    z=[[sum((v*b[i][k] for v,b in zip(vector,basis)),F())
        for k in range(m+d+1)] for i in range(m+1)]
    maximum=max(abs(v) for row in z for v in row)
    z=[[v/maximum for v in row] for row in z]
    return z,rank(design)
