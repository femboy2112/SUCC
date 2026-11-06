"""Original BBP source prime-denominator sieve: exact rational post-prereg holdouts.

No normality claims. Only the finite checks run here; the all-n and PNT/AP proofs
are written separately in THEOREM.md.
"""
from fractions import Fraction
from math import log
import json

def source(n):
    return Fraction(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def four_poles(n):
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def primes_upto(bound):
    if bound<2:return []
    flags=bytearray([1])*(bound+1);flags[0:2]=bytes([0,0])
    for p in range(2,int(bound**0.5)+1):
        if flags[p]:flags[p*p::p]=bytes(len(flags[p*p::p]))
    return [p for p in range(2,bound+1) if flags[p]]

def sieve_set(n):
    return [p for p in primes_upto(8*n-7) if (2*n<p<=4*n or (4*n<p<=8*n-7 and p%4==1))]

def frac_mod(q,p):
    q=Fraction(q)
    assert q.denominator%p!=0
    return (q.numerator*pow(q.denominator,-1,p))%p

def principal_residue(n,p):
    assert p>2*n and (p<=4*n or p%4==1)
    if p%4==1:
        if p%8==1:
            j=(p+7)//8; coefficient=Fraction(4)
            pole='8j-7'
        else:
            j=(p+3)//8; coefficient=Fraction(-1)
            pole='8j-3'
        assert j<=n
        residue=frac_mod(coefficient,p)*pow(16,n-j,p)%p
        return residue, (pole,), False
    j=(p+1)//4
    assert j<=n
    residue=frac_mod(Fraction(-1,2),p)*pow(16,n-j,p)%p
    if p%8==3:
        jb=(3*p+7)//8; cb=Fraction(4,3); folded=Fraction(16,3)
        pole='8j-7=3p';legendre_2=-1
    else:
        jb=(3*p+3)//8; cb=Fraction(-1,3); folded=Fraction(-4,3)
        pole='8j-3=3p';legendre_2=1
    if jb<=n:
        residue=(residue+frac_mod(cb,p)*pow(16,n-jb,p))%p
        folded_residue=frac_mod(folded,p)*pow(16,n-jb,p)%p
        assert residue==folded_residue,('Legendre fold',n,p)
        assert pow(2,(p-1)//2,p)==legendre_2%p
        assert pow(16,jb-j,p)==((-8) if p%8==3 else 2)%p
        return residue,('4j-1=p',pole),True
    return residue,('4j-1=p',),False

def run():
    ns=[161,173,199,211,257,293,317,383]
    curr=Fraction(0);ncur=0; out=[];total=0
    for n in ns:
        while ncur<n:
            ncur+=1
            assert source(ncur)==four_poles(ncur)
            curr=16*curr+source(ncur)
        assert curr.denominator%2==1
        ps=sieve_set(n)
        assert ps
        prod=1;collisions=0;branches={'4j-1=p':0,'8j-7':0,'8j-3':0}
        for p in ps:
            residue,poles,collision=principal_residue(n,p)
            assert residue!=0,(n,p,poles)
            assert curr.denominator%p==0,(n,p,'no denom')
            assert curr.denominator%(p*p)!=0,(n,p,'higher pole')
            assert frac_mod(p*curr,p)==residue,(n,p,'wrong pU',poles)
            prod*=p;total+=1
            collisions+=collision
            branches[poles[0]]+=1
        assert curr.denominator%prod==0
        out.append({'n':n,'selected_primes_count':len(ps),'two_pole_collisions':collisions,'branch_counts':branches,
                    'actual_reduced_denominator_bits':curr.denominator.bit_length(),
                    'forced_prime_product_bits':prod.bit_length(),
                    'forced_log_ratio_to_n_float':round(sum(log(p) for p in ps)/n,8),
                    'denominator_log_ratio_to_n_float':round(log(curr.denominator)/n,8),
                    'all_pU_residues_exact':True,'prime_product_divides_denominator':True})
    return {'label':'OBSERVED-FINITE / exact arithmetic','original_source':True,'literal_U0':'0',
            'holdouts':ns,'total_selected_prime_residue_checks':total,
            'all_pole_collisions_covered':True,'data':out,
            'all_n_theorem':'in THEOREM.md, not inferred from checks',
            'pnt_in_AP':'classical unconditional theorem',
            'real_Weyl_source_selected_contraction':'OPEN','pi_normality':'OPEN'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
