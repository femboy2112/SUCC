import json
import sys
from pathlib import Path
from fractions import Fraction as F
from fibonacci_arrows import (cycle_witness,paired_alias,projection_residual,
    twice_integrated,poly_moment,infinite_norm_bracket,fib,zeckendorf,R)


def main():
    rows=[]
    for m,d in ((6,5),(7,5)):
        Z,rank,dim=cycle_witness(m,d)
        rows.append({"m":m,"d":d,"rank":rank,"cycle_dimension":dim,
                     "nonzero_edges":{f"{i},{j}":str(v) for (i,j),v in Z.items() if v}})
    aliases=[]
    for a in (1,17,57,97,233):
        J,K,Z,eps,rank,dim=paired_alias(a)
        assert all(x>0 for x in K.values())
        aliases.append({"a":a,"epsilon":str(eps),"minimum_mass":str(min(K.values())),
                        "total_variation":str(sum(abs(J[e]-K[e]) for e in J)/2)})
    residuals=[]
    for L,last in ((0,3),(0,5),(2,5),(7,8),(12,6),(29,9)):
        h,norm,product=projection_residual(L,last)
        g=twice_integrated(h,L)
        assert norm==product and poly_moment(g,0)==0
        assert all(poly_moment(g,fib(n))==0 for n in range(2,last+1))
        residuals.append({"L":L,"last_index":last,"h":{str(k):str(v) for k,v in h.items()},
                          "norm_squared":str(norm),"fourth_moment":str(poly_moment(g,4))})
    brackets=[]
    for L in (0,2,7,12,29):
        lo,hi,t=infinite_norm_bracket(L)
        brackets.append({"L":L,"index":24,"norm_squared_lower":str(lo),
                         "norm_squared_upper":str(hi),"tail_sum_bound":str(t)})
    # A rational enclosure of sum_(n>=2) 1/F_n, with classical duplicate F1 excluded.
    partial=sum((F(1,fib(n)) for n in range(2,31)),F(0))
    tail=2*(F(1,fib(31))+F(1,fib(32)))
    output={"cycle_witnesses":rows,"authentic_marginal_aliases":aliases,
            "finite_residuals":residuals,"infinite_norm_brackets":brackets,
            "reciprocal_fibonacci_sum_n_ge_2":[str(partial),str(partial+tail)],
            "zeckendorf_holdout_count":301,
            "authority":"exact finite arithmetic; infinite claims proved separately; shared model"}
    for n in range(1000,1301):
        js=zeckendorf(n)
        assert sum(fib(j) for j in js)==n
        assert all(a-b>=2 for a,b in zip(js,js[1:]))
    target=Path(__file__).parent/"receipts"/(sys.argv[1] if len(sys.argv)>1 else "probe.json")
    target.parent.mkdir(exist_ok=True)
    with target.open("x") as f:
        json.dump(output,f,indent=2)
    print(json.dumps({"cycle_rows":len(rows),"source_aliases":len(aliases),
                      "residuals":len(residuals),"infinite_brackets":len(brackets),
                      "zeckendorf_holdouts":301}))


if __name__=="__main__":
    main()
