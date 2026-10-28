"""Exact finite odd-prime product formula oracle for actual rational BBP states."""
import json
import sys
from pathlib import Path
from fractions import Fraction as Q
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.pi_rank_lattice import original_state
from observational_succ.pi_odd_prime_character import odd_prime_phase_factors, rank_filtered_phase


def main():
    cases=0
    per_index=[]
    for n in range(1,15):
        u=original_state(n)
        fs=odd_prime_phase_factors(u)
        pset=tuple(p for p,k,phase in fs)
        for h in (-5,-1,0,1,2,7):
            pieces=odd_prime_phase_factors(u,h)
            assert sum((phase for _,_,phase in pieces),Q())%1==(h*u)%1
            known,residual,full=rank_filtered_phase(u,h,(3,5,7))
            assert (known+residual)%1==full
            cases+=1
        per_index.append({'n':n,'distinct_odd_primes':len(pset),
                          'largest_odd_prime':max(pset,default=0)})
    print(json.dumps({'status':'PASS','exact_character_checks':cases,
                      'original_state_count':14,'prime_support':per_index,
                      'claim':'exact finite CRT product, no independence/cancellation established'},
                     indent=2,sort_keys=True))
if __name__=='__main__':main()
