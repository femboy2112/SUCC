"""Source-exact finite hex-cylinder certificates from BBP with original seed zero.
No inference to infinite digit statistics.
"""
from time_extrusion_probe import circle_prefix, certified_pure_state, count_periodic_prefix

def digits_from_interval(n,states,depth=16,K=28):
    lo,hi,eta=certified_pure_state(n,states,K)
    out=[]
    for _ in range(depth):
        lo*=16;hi*=16
        d1=lo.numerator//lo.denominator;d2=hi.numerator//hi.denominator
        if d1!=d2:raise ArithmeticError('tighten tail cutoff')
        out.append(d1)
        lo-=d1;hi-=d2
    return out

if __name__=='__main__':
    states,_=circle_prefix(46)
    alphabet='0123456789ABCDEF'
    out=[]
    for n in (1,2,3,4,5,8,13,20,30,40):
        digs=digits_from_interval(n,states,18)
        row={'source_time':n,'hex_prefix':''.join(alphabet[x] for x in digs),
             'max_periodic_prefix':{str(p):count_periodic_prefix(digs,p) for p in (1,2,3,4)}}
        out.append(row)
        print(row)
    import json
    from pathlib import Path
    Path(__file__).with_name('finite_pi_cylinders.json').write_text(json.dumps(out,indent=2)+'\n')