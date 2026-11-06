"""Post-preregistered exact full source prime sieve: (n,4n] plus (4n,8n−7]."""
from fractions import Fraction as F
from math import log
import json
from prime_certificate import source,four_poles,primes_upto,principal_residue,frac_mod

def mid_residue(n,p):
    assert n>=8 and n<p<=2*n and p>7
    j0=(p+1)//2
    assert j0<=n
    if p%4==1:
        # For (8j−7),(8j−3) first pole, Fermat+Euler give +4.
        coeff=F(7,2) # +4 − 1/2
        if p%8==1:
            j5=(5*p+3)//8 # 8j−3=5p
        else:
            j5=(5*p+7)//8 # 8j−7=5p
        j3=(3*p+1)//4 # 4j−1=3p
        if j5<=n:coeff-=F(1,5)
        if j3<=n:coeff-=F(1,6)
        assert not (j3<=n and j5>n)
        label=str(coeff)
    else:
        # 4j−1=p, 8j−7 or8j−3=3p, plus 2j−1=p.
        coeff=-F(19,6)
        if p%8==3:
            j7=(7*p+3)//8 # 8j−3=7p
        else:
            j7=(7*p+7)//8 # 8j−7=7p
        if j7<=n: coeff+=F(1,14)
        label=str(coeff)
    return frac_mod(coeff,p)*pow(16,n-j0,p)%p,label

def sieve_set_full(n):
    return [p for p in primes_upto(8*n-7) if (n<p<=4*n or (4*n<p<=8*n-7 and p%4==1))]

def run():
    holds=[389,401,433,463,509,557]
    curr=F(0);j=0;rows=[];total=0;coefficient_counts={}
    for n in holds:
        while j<n:
            j+=1
            assert source(j)==four_poles(j)
            curr=16*curr+source(j)
        ps=sieve_set_full(n)
        prod=1; s=0; twopole=0; counts={'(n,2n]':0,'(2n,4n]':0,'(4n,8n] mod4=1':0}
        for p in ps:
            if p<=2*n:
                predicted,label=mid_residue(n,p)
                counts['(n,2n]']+=1
                coefficient_counts[label]=coefficient_counts.get(label,0)+1
            else:
                predicted,other,is_collision=principal_residue(n,p)
                if p<=4*n:counts['(2n,4n]']+=1
                else:counts['(4n,8n] mod4=1']+=1
                twopole+=is_collision
            if predicted==0: raise AssertionError(('zero p residue',n,p))
            if curr.denominator%p!=0 or curr.denominator%(p*p)==0:
                raise AssertionError(('valuation',n,p))
            actual=frac_mod(p*curr,p)
            if actual!=predicted:
                raise AssertionError(('wrong principal residue',n,p,actual,predicted))
            prod*=p;total+=1;s+=log(p)
        assert curr.denominator%prod==0
        rows.append({'n':n,'prime_count':len(ps),'prime_bands':counts,'two_pole_high_band':twopole,
                     'forced_prime_product_bits':prod.bit_length(),
                     'actual_denominator_bits':curr.denominator.bit_length(),
                     'forced_log_over_n_float':round(s/n,9),
                     'actual_log_over_n_float':round(log(curr.denominator)/n,9),
                     'all_exact_residues_correct':True})
    # Exact finite false/true controls for source-induced exceptional p=19.
    z=F(0);controls=[]
    for n in range(1,20):
        z=16*z+source(n)
        if 10<=n<=18:
            expected,coeff=mid_residue(n,19)
            actual=frac_mod(19*z,19)
            # If v19(U_n)>=0, 19 U_n ≡0 mod19; if v=-1, pU unit modulo p.
            assert actual==expected,(n,expected,actual)
            assert (expected==0)==(n<=16)
            controls.append({'n':n,'predicted_pU_mod19':expected,'actual_pU_mod19':actual,
                             'denominator_contains_19':z.denominator%19==0,
                             'normalized_coefficient':coeff})
    return {'label':'OBSERVED FINITE exact source principal parts','original_four_poles':True,
            'U0':'0','fresh_holdouts':holds,'fresh_prime_residue_checks':total,
            'piecewise_coefficient_counts':coefficient_counts,'rows':rows,
            'exception19_controls':controls,'PNT_AP_used_only_in_analytic_proof':True,
            'source_selected_real_Weyl_contraction':'OPEN','pi_base16_normality':'OPEN'}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
