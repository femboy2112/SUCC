"""Independent finite audit with a second algebraic source formula.

No import of source_to_digit or its test code. Imported infinite theorems
(Pólya--Carlson, irrationality measures) are PAPER premises, not tested here.
"""
from fractions import Fraction
from math import factorial
import sympy as sp
import json,hashlib

N=16
checks=0

def check(statement,context):
    global checks
    checks+=1
    if not statement:
        raise AssertionError(context)

def compact_forcing(n):
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

# Completely different source route: Mellin polynomial evaluated by integration
for n in range(1,129):
    polynomial=sp.Poly(4-2*sp.Symbol('t')**3-sp.Symbol('t')**4-sp.Symbol('t')**5,sp.Symbol('t'))
    integral=sum((sp.Rational(int(coef),8*n-7+int(p)) for (p,),coef in polynomial.terms()),sp.Rational(0))
    q=compact_forcing(n)
    check(integral==sp.Rational(q.numerator,q.denominator),('Mellin',n))
    check(q>0,('positive',n))
    if n>1:
        check(q<compact_forcing(n-1),('decreasing',n))

# Original zero-seed interval, evaluated by compact rational source, no digit strings imported
M=70
prefix=sum((compact_forcing(n)/N**n for n in range(1,M+1)),Fraction())
tail=compact_forcing(M+1)/(15*N**M)
for length in range(1,49):
    a=(prefix*N**length).__floor__()
    b=((prefix+tail)*N**length).__floor__()
    check(a==b,('prefix certification',length))
check(format((prefix*N**24).__floor__(),'024X')=='3243F6A8885A308D313198A2','source prefix')

# Fully independent, direct long-division of rational ultimately periodic strings.
for pre_n in range(0,7):
    for period in range(1,5):
        for seed in range(1,31):
            A=(seed*137+pre_n*17)%N**pre_n
            W=(seed*199+period*29)%N**period
            x=Fraction(A*(N**period-1)+W,N**pre_n*(N**period-1))
            rendered=f'{A:0{pre_n}X}' if pre_n else ''
            period_text=f'{W:0{period}X}'
            rendered+=period_text*9
            # Infinite repeated F is the noncanonical endpoint: 0.FFFFF...=1.
            # It must be identified with the terminating expansion, not
            # compared as if its finite truncations were floors of the limit.
            if W == N**period-1:
                check(x == Fraction(A+1,N**pre_n),('endpoint ambiguity',pre_n,period,seed))
                continue
            for cut in range(1,pre_n+5*period+1):
                check((x*N**cut).__floor__()==int(rendered[:cut],16),('rational shadow',pre_n,period,seed,cut))

# Rational approximation from n-prefix+periodic continuation: shared digits => error <= b^(-n-L)
for length in (8,16,32,64):
    digit_word=('3243F6A8885A308D313198A2'*3)[:length]
    X=Fraction(int(digit_word,16),N**length) + Fraction(1,2*N**length)
    for n in range(1,min(length,20)):
        for p in (1,2,3,5):
            if n+p>=length: continue
            W=int(digit_word[n:n+p],16)
            prefix_int=int(digit_word[:n],16)
            Y=Fraction(prefix_int*(N**p-1)+W,N**n*(N**p-1))
            L=0
            while n+L<length and digit_word[n+L]==digit_word[n+(L%p)]:L+=1
            check(abs(X-Y)<=Fraction(1,N**(n+L)),('shared cylinder',length,n,p))

# Critical R0-failure model beta=sum_0^inf 16^(-2^k). Full phase is bounded by a geometric tail.
for B in (2,4,8,16,32,64):
    total=Fraction()
    for n in range(B,2*B):
        first=2*B
        lower=Fraction(1,N**(first-n))
        trunc=sum((Fraction(1,N**(2**power-n)) for power in range(0,11) if 2**power>n),Fraction())
        check(lower<=trunc<lower*Fraction(16,15),('Kempner phase enclosure',B,n))
        total+=trunc*trunc
    tail=Fraction(1,256)
    upper=Fraction(256,225)*tail*(1-tail**B)/(1-tail)/B
    check(total/B<upper,('Kempner energy square',B))

# Factorial-lacunary irrational control explicitly violates EVERY finite nu family asymptotically.
for nu in (sp.Rational(71,10),sp.Rational(3,1),sp.Rational(201,100)):
    for k in range(20,27):
        n=factorial(k)
        L=factorial(k+1)-n-1
        check(L>(nu-1)*n+nu+1,('factorial shadow',k,str(nu)))

receipt={'status':'PASS','assertions':checks,
         'source':'independent compact rational + Mellin polynomial',
         'pi_interval_depth':M,'max_certified_digits':48,
         'known_source_prefix_24':format((prefix*N**24).__floor__(),'024X'),
         'kempner_shells':[2,4,8,16,32,64],
         'external_theorems_not_computed':['Polya-Carlson','Zeilberger-Zudilin 2020','Kempner mu=2','OpenAI 2026 claimed mu=2']}
with open('independent_audit_receipt.json','w') as out:json.dump(receipt,out,indent=2,sort_keys=True)
print(json.dumps(receipt,sort_keys=True))
