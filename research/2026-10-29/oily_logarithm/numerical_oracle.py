"""Independent mpmath integrations: finite BBP Lévy exponent and logarithmic seed.

High precision diagnostics only, not rigorous interval certificates of all a,t.
"""
import json
import mpmath as mp
mp.mp.dps=70
A=(mp.mpf(121)-mp.sqrt(241))/30
B=(mp.mpf(121)+mp.sqrt(241))/30
lam=(mp.sqrt(5)-1)/2

def R(z):
    z=mp.mpc(z) if isinstance(z,(complex,mp.mpc)) else mp.mpf(z)
    return 4/z-2/(z+3)-1/(z+4)-1/(z+5)
def levy(y,a):
    # Rescale the entire original four-pole characteristic exponent.
    if not y:return 2
    x=y/a
    return 1+mp.exp(-3*x)+mp.exp(-4*x)+mp.exp(-5*x)-mp.exp(-A*x)-mp.exp(-B*x)

def source_log_integral(a,t):
    a,t=mp.mpf(a),mp.mpf(t)
    def f(y):
        if y==0:return 2*mp.j*t
        return mp.exp(-y)*levy(y,a)*mp.expm1(mp.j*t*y)/y
    return mp.quad(f,[0,mp.mpf('0.125'),1,3,9,30,mp.inf])

def source_mellin(a,q,s):
    a=mp.mpf(a);q=mp.mpf(q);s=mp.mpf(s)
    # A two-jet test independently integrated from the original positive Q.
    def density(y):
        if not y:return mp.mpf(0)
        x=y/a
        return mp.exp(-y)*(2*(1-mp.exp(-3*x))+(1-mp.exp(-4*x))+(1-mp.exp(-5*x)))/(a*R(a))
    return mp.quad(lambda y: density(y)*y**s*mp.exp(-q*y),[0,mp.mpf('0.125'),1,4,15,mp.inf])

def seed_log_special(n,h):
    b=2*mp.pi*abs(h)*16**n
    value=mp.euler+mp.log(b)-mp.ci(b)-mp.j*mp.sign(h)*mp.si(b)
    limit=mp.euler+mp.log(2*mp.pi*abs(h))-mp.j*mp.sign(h)*mp.pi/2
    err=value-n*mp.log(16)-limit
    bound=1/b + 2/b**2+2/b**3
    assert abs(err)<bound
    return value,limit,bound

checks=0; samples=[]
for a,t in [(1,mp.mpf(1)),(3,mp.mpf('0.5')),(31,1),(1024,1),(19,lam)]:
    integral=source_log_integral(a,t)
    target=mp.log(R(mp.mpf(a)*(1-mp.j*t))/R(a))
    if abs(integral-target)>mp.mpf('1e-55'):
        raise AssertionError((a,t,integral,target,integral-target))
    samples.append({'a':str(a),'t':mp.nstr(t,20),'source_log':mp.nstr(target,45),
                    'integration_error':mp.nstr(abs(integral-target),8)})
    checks+=1
for a in (3,17,299):
    for q,s in ((0,0),(lam,0),(0,1),(lam,2)):
        moment=source_mellin(a,q,s)
        formula=mp.mpf(a)**s*mp.gamma(s+1)*sum(mp.mpf(c)/(mp.mpf(a)*(1+q)+d)**(s+1)
                              for d,c in ((0,4),(3,-2),(4,-1),(5,-1)))/R(a)
        if abs(moment-formula)>mp.mpf('1e-51'):
            raise AssertionError((a,q,s,moment,formula))
        checks+=1
for n,h in [(0,1),(1,-1),(2,3),(5,1)]:
    value,limit,bound=seed_log_special(n,h)
    checks+=1
# First logarithmic source correction at the natural 90-degree Gamma limit.
for a in (300,1000,4000):
    O=mp.log(R(mp.mpf(a)*(1-mp.j))/R(a))
    predicted=-mp.log(2)+mp.j*mp.pi/2+(mp.mpf(59)/(30*a))*(1-mp.j)
    assert abs(O-predicted)<mp.mpf(25)/a**2
    checks+=1
# Common Golden Oily-macaroni finite part from the explicit source density.
for a in (3,100,600):
    e_log=mp.diff(lambda s:source_mellin(a,0,s),0)
    e_lap=source_mellin(a,lam,0)
    oily=e_log-e_lap
    if a==600:assert abs(oily-(lam-mp.euler))<mp.mpf('0.012')
    checks+=1
print('OILY_LOG_NUMERICAL_HOLDOUT_PASS',checks,'checks at 70 dps')
print(json.dumps({'status':'PASS','checked':checks,'precision':70,'samples':samples,
'pi_normality':'OPEN','type':'diagnostic_high_precision_not_interval'},indent=2))
