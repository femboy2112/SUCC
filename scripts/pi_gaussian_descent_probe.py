from math import ceil
import json


def ring(m):
    k=m//2; q=2**k; M=2**ceil(m/2)
    def red(z):
        a,b=z
        if m%2:
            t,b=divmod(b,q)
            return ((a-t*q)%(2*q),b)
        return (a%q,b%q)
    def add(z,w):return red((z[0]+w[0],z[1]+w[1]))
    def mul(z,w):return red((z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]))
    def inv(z):
        a,b=z; c=pow((a*a+b*b)%M,-1,M)
        return red((a*c,-b*c))
    def scale(c,z):return red((c*z[0],c*z[1]))
    def conj(z):return red((z[0],-z[1]))
    def source(z):
        A=add(add(scale(120,mul(z,z)),scale(-89,z)),red((16,0)))
        D=red((1,0))
        for a,b in [(2,-1),(4,-1),(8,-7),(8,-3)]:
            D=mul(D,add(scale(a,z),red((b,0))))
        return mul(A,inv(D))
    def psi(z):
        ans=red((0,0))
        for s in range(ceil(m/8)):
            ans=add(ans,scale(16**s,source(add(z,red((-s,0))))))
        return ans
    elements=[(a,b) for a in range(M) for b in range(q)]
    return red,add,conj,psi,elements

def v2cap(b,k):
    if b==0:return k
    return min(k,(b&-b).bit_length()-1)

def run():
    rows=[]
    for m in range(1,13):
        red,add,conj,psi,E=ring(m); P={z:psi(z) for z in E}
        assert len(set(P.values()))==2**m
        assert all(P[conj(z)]==conj(P[z]) for z in E)
        rational={red((a,0)) for a in range(2**ceil(m/2))}
        assert {P[z] for z in rational}==rational
        fixed={z for z in E if conj(z)==z}
        assert len(fixed)==2**(ceil(m/2)+(m%2==0))
        assert (fixed==rational)==(m%2==1)
        k=m//2
        assert all(v2cap(z[1],k)==v2cap(P[z][1],k) for z in E)
        if m%2==0:
            for z in E:
                assert (P[z][1]+z[1])%2**min(k,v2cap(z[1],k)+2)==0
        Q={P[z]:P[add(z,red((1,0)))] for z in E}
        seen=set(); lengths=[]
        for z in E:
            if z in seen:continue
            length=0; w=z
            while w not in seen:
                seen.add(w);length+=1;w=Q[w]
            assert w==z;lengths.append(length)
        assert len(lengths)==2**(m//2)
        assert set(lengths)=={2**ceil(m/2)}
        rows.append(dict(m=m,size=2**m,rational=len(rational),fixed=len(fixed),cycles=len(lengths),cycle_length=lengths[0]))

    # The tempting finite-level claim 'conjugation-fixed implies rational' must fail.
    red,add,conj,psi,E=ring(2)
    z=red((0,1))
    assert conj(z)==z and z not in {red((a,0)) for a in range(2)}
    return {'rows':rows,'mutant_fixed_equals_rational_rejected':z}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
