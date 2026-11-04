"""Independent generation of finite source-collision receipts, not a proof of a limit."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
from mesoscopic import original_modular_lift, online_modular_lift, exact_near_pair_count


def generate(max_exponent=13):
    jlist = list(range(8,max_exponent+1))
    As = [1<<j for j in jlist]
    meshes = {(A, name): max(2, 1 << ((j*num)//den))
              for A,j in zip(As,jlist)
              for name,num,den in (('quarter',1,4),('half',1,2),('three_quarters',3,4),('self',1,1))}
    counts = {(A,name):[0]*mesh for (A,name),mesh in meshes.items()}
    track = {A:[] for A in As[-2:]}
    total = 2*As[-1]-1
    checks = {0,1,2,8,31,131,257,511,1024,2048,4096,8192,total}
    oracle = online_modular_lift(total)
    for (n,a,D),(n2,b,d) in zip(original_modular_lift(total),oracle):
        assert n==n2
        if n in checks:
            assert a*d==b*D, (n,'mismatch')
        if n>=As[0]:
            A = 1 << (n.bit_length()-1)
            if A in As:
                for name in ('quarter','half','three_quarters','self'):
                    mesh=meshes[(A,name)]
                    counts[(A,name)][mesh*a//D]+=1
                if A in track: track[A].append(a)
    out = {'method':'exact original four signed pole U_0=0; fixed global lcm and independent online lcm oracles; finite data, not proof of all A',
           'source': 'r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)',
           'last_n':total,'independent_crosscheck_indices':sorted(checks),
           'epochs':{}}
    for A in As:
        epoch={}
        for name in ('quarter','half','three_quarters','self'):
            v=counts[(A,name)];mesh=meshes[(A,name)]
            assert sum(v)==A
            cc=sum(c*c for c in v)
            g=__import__('math').gcd(mesh*cc,A*A)
            epoch[name]={'mesh':mesh,'sum_count_squared':cc,'energy_fraction':'%s/%s'%(mesh*cc//g,A*A//g),'max_occupancy':max(v),
                         'counts_sha256':hashlib.sha256(json.dumps(v,separators=(',',':')).encode('ascii')).hexdigest()}
            if A in track and name in ('half','self'):
                epoch[name]['exact_ordered_near_pairs']=exact_near_pair_count(track[A],D,mesh)
        out['epochs'][str(A)]=epoch
    return out


if __name__=='__main__':
    path=Path(__file__).with_name('FINITE_RECEIPT.json')
    path.write_text(json.dumps(generate(),indent=2,sort_keys=True)+'\n')
    print(path, 'sha256',hashlib.sha256(path.read_bytes()).hexdigest())
