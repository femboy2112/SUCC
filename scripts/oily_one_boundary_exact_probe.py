"""Exact finite identities for the Oily–Macaroni / BBP one-boundary bridge.

Standard-library rational checks only. Universal proofs are in the companion
theorem dossier. Does NOT test any Weyl cancellation or pi normality.
"""
from fractions import Fraction as Q
from math import comb, gcd

def packet_pi(j):
    """Integrate the authentic positive Oily grade polynomial exactly."""
    assert isinstance(j,int) and j >= 0
    # p_j = (u^(j+1)-v^(j+1))/(4*x), u=x*(1-x/2), v=x*x/2
    first = sum((Q(4)*comb(j+1,k)*Q(-1,2)**k/Q(j+k+1)
                 for k in range(j+2)), Q())
    second = Q(4,2**(j+1)*(2*j+2))
    return first-second

def packet_pi_beta(j):
    """Independent inverse-central-binomial closed form."""
    return Q(2**(j+1), (2*j+1)*comb(2*j,j))

def mobius(n):
    assert n>=1
    ans=1
    f=2
    while f*f<=n:
        if n%f==0:
            n//=f
            ans=-ans
            if n%f==0: return 0
        f+=1
    if n>1: ans=-ans
    return ans

def primitive_character(m,z=Q(1)):
    """Exact C_m(z), H_m(z)=2C_m-z*C'_m(z); z rational |z|<=1."""
    z=Q(z)
    assert m>=1 and abs(z)<=1
    C=Q()
    z_deriv=Q()
    for d in range(1,m+1):
        if m%d: continue
        mu=mobius(d)
        if mu==0: continue
        t=(z/2)**d
        C+=Q(mu,4)*(1+(d-1)*t)/(1-t)**2
        z_deriv+=Q(mu*d,4)*t*((d+1)+(d-1)*t)/(1-t)**3
    return C,2*C-z_deriv

def first_second_log(m,z=Q(1)):
    C,H=primitive_character(m,z)
    return Q(15,64)*C, (209*C-30*H)/1024

def tests():
    for j in range(33):
        assert packet_pi(j)==packet_pi_beta(j),("Euler packet",j)
    assert [packet_pi(j) for j in range(5)]==[Q(2),Q(2,3),Q(4,15),Q(4,35),Q(16,315)]
    checks=0
    for m,expected_C in {1:Q(1),2:Q(4,9),3:Q(29,49),6:Q(416,1323),16:Q(4,9)}.items():
        for z in (Q(-1),Q(0),Q(1,2),Q(1)):
            C,H=primitive_character(m,z)
            finite_C=sum((Q(j+1,2**(j+2))*z**j for j in range(70) if gcd(j,m)==1),Q())
            finite_H=sum(((2-j)*Q(j+1,2**(j+2))*z**j for j in range(70) if gcd(j,m)==1),Q())
            assert abs(C-finite_C)<Q(1,10**14)
            assert abs(H-finite_H)<Q(1,10**12)
            checks+=1
        assert primitive_character(m)[0]==expected_C
    assert primitive_character(1)==(Q(1),Q(0))
    assert first_second_log(1)==(Q(15,64),Q(209,1024))
    assert primitive_character(2)==(Q(4,9),Q(-4,27))
    assert first_second_log(2)==(Q(5,48),Q(73,768))
    print("PASS: 33 exact integrated packet identities")
    print("PASS: 20 primitive-character and first-response checks")
    print("PASS: exact ungraded and dyadic log coefficients")
    print("PASS: first packet masses", [str(packet_pi(j)) for j in range(5)])

if __name__=="__main__":
    tests()
