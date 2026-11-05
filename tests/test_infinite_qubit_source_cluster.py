"""Source-faithful quasilocal cluster/GHZ research calibrations (stdlib only).

All SUCC BBP source-time states are unwrapped exact Fractions. The declared
Hilbert embedding is NOT a physical interpretation of arithmetic. Complex
trigonometry is performed only after exact rational circle reduction.
"""
from __future__ import annotations
import cmath
import math
import unittest
from fractions import Fraction as Q

ORIGINAL = (Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))
DUAL = (Q(0),Q(8),Q(4),Q(4),Q(0),Q(0),Q(-1),Q(0))
ANG = tuple((2*a+b)/4 for a,b in zip(ORIGINAL,DUAL))
RAD = tuple((2*a-b)/4 for a,b in zip(ORIGINAL,DUAL))

def source(n,taps):
    assert n>=1
    return sum((w/Q(8*(n-1)+j) for j,w in enumerate(taps,1)),Q())

def states_at(n):
    u=y=z=Q(0)
    for j in range(1,n+1):
        u=16*u+source(j,ORIGINAL)
        y=16*y+source(j,ANG)
        z=16*z+source(j,RAD)
        assert y+z==u
    return u,y,z

def ch(turn):
    t=Q(turn)%1
    return cmath.exp(2j*math.pi*float(t))

def cluster_vector(N,turns=None):
    """Exact graph-state sign, controlled local source phases."""
    assert N>=2
    turns=turns or {}
    phases={j:Q(t)%1 for j,t in turns.items() if j<N}
    v=[]
    for bits in range(1<<N):
        parity=sum(((bits>>j)&1)*((bits>>(j+1))&1) for j in range(N-1))&1
        signed_turn=sum((t*(1-2*((bits>>j)&1)) for j,t in phases.items()),Q())
        phase=cmath.exp(-1j*math.pi*float(signed_turn%2))
        v.append(((-1)**parity)*phase/math.sqrt(1<<N))
    return v

def ghz_vector(N,turn=Q(0)):
    out=[0j]*(1<<N)
    out[0]=1/math.sqrt(2)
    out[-1]=-ch(turn)/math.sqrt(2)
    return out

def reduced_prefix(vec,N,m):
    assert 0<m<=N
    s=1<<m;tail=1<<(N-m)
    return [[sum((vec[i+s*k]*vec[j+s*k].conjugate()
                  for k in range(tail)),0j)
             for j in range(s)] for i in range(s)]

def purity(rho):
    return sum((abs(x)**2 for row in rho for x in row))

def expect(vec,N,ops):
    """ops: P=X+iY, X, Y, Z, indexed from site 0 (low-order bit)."""
    out=[0j]*(1<<N)
    for bits,amp in enumerate(vec):
        target=bits;coeff=1+0j
        for site,op in ops.items():
            b=(bits>>site)&1
            if op=="P":
                if b==0: coeff=0j;break
                coeff*=2;target^=1<<site
            elif op=="X":
                target^=1<<site
            elif op=="Y":
                coeff*=1j if b==0 else -1j
                target^=1<<site
            elif op=="Z": coeff*=1 if b==0 else -1
            else: raise ValueError(op)
        out[target]+=coeff*amp
    return sum((vec[j].conjugate()*out[j] for j in range(1<<N)),0j)

def stabilizer_ops(N,j):
    ops={j:"X"}
    if j>0:ops[j-1]="Z"
    if j+1<N:ops[j+1]="Z"
    return ops

def grouped_phase_ops(m):
    ops={2*j:"P" for j in range(m)}
    ops[2*m-1]="Z"
    return ops

def close(x,y,tol=5e-11):
    return abs(x-y)<=tol

class InfiniteQubitField(unittest.TestCase):
    def test_01_authentic_angular_radial_unwrapped(self):
        self.assertEqual(source(1,ORIGINAL),Q(47,15))
        self.assertEqual(source(1,RAD),Q(2,105))
        for n in (1,2,5,11,17):
            u,y,z=states_at(n)
            self.assertEqual(u,y+z)
            self.assertEqual(u.denominator%2,1)
            self.assertGreater(z,0)

    def test_02_pure_ghz_N_fail_consistency_new_holdouts(self):
        for N in (7,8,9):
            phase=Q(3,17)
            low=reduced_prefix(ghz_vector(N,phase),N,N)
            high=reduced_prefix(ghz_vector(N+1,phase),N+1,N)
            self.assertTrue(abs(low[0][-1])>.49)
            self.assertTrue(abs(high[0][-1])<1e-12)
            self.assertTrue(abs(high[0][0]-.5)<1e-12)
            self.assertTrue(abs(high[-1][-1]-.5)<1e-12)

    def test_03_proper_ghz_local_blindness(self):
        for N in (7,8,9):
            a=ghz_vector(N,Q(0));b=ghz_vector(N,Q(5,13))
            for m in (1,2,N-1):
                ra=reduced_prefix(a,N,m);rb=reduced_prefix(b,N,m)
                self.assertTrue(all(close(ra[i][j],rb[i][j])
                       for i in range(1<<m) for j in range(1<<m)))

    def test_04_cluster_stabilizers_new_holdouts(self):
        for N in (7,8,9):
            v=cluster_vector(N)
            for j in range(N):
                self.assertTrue(close(expect(v,N,stabilizer_ops(N,j)),1))

    def test_05_cluster_local_marginal_compatible(self):
        angles={0:Q(1,7),2:Q(3,11)}
        for m in (1,2,3,4):
            baseline=reduced_prefix(cluster_vector(m+1,angles),m+1,m)
            for N in (7,8,9):
                rho=reduced_prefix(cluster_vector(N,angles),N,m)
                self.assertTrue(all(close(baseline[i][j],rho[i][j])
                       for i in range(1<<m) for j in range(1<<m)))

    def test_06_cluster_every_contiguous_cut_ebit(self):
        for N in (7,8,9):
            v=cluster_vector(N)
            for m in range(1,N):
                self.assertTrue(close(purity(reduced_prefix(v,N,m)),.5))

    def test_07_all_single_site_cluster_marginals_are_mixed(self):
        for N in (7,8,9):
            v=cluster_vector(N,{0:Q(3,11),2:Q(5,17)})
            for site in (0,2,N-1):
                # Single-site Z gives zero; use a permutation-free sign sum.
                zavg=sum((abs(amp)**2*(1 if ((bits>>site)&1)==0 else -1)
                         for bits,amp in enumerate(v)))
                self.assertTrue(abs(zavg)<1e-12)
            r=reduced_prefix(v,N,1)
            self.assertTrue(close(r[0][0],.5))
            self.assertTrue(close(r[1][1],.5))
            self.assertTrue(close(r[0][1],0))

    def test_08_source_driven_two_channel_witness(self):
        for N in (7,8,9):
            for n in (2,5,11):
                u,y,z=states_at(n)
                for h in (1,3,-2):
                    angles={0:h*y,2:h*z}
                    v=cluster_vector(N,angles)
                    self.assertTrue(close(expect(v,N,grouped_phase_ops(1)),ch(h*y)))
                    self.assertTrue(close(expect(v,N,grouped_phase_ops(2)),ch(h*u)))

    def test_09_three_channel_same_source_consistency(self):
        for N in (7,8,9):
            for n in (2,5,11):
                u,y,z=states_at(n)
                v=cluster_vector(N,{0:y,2:z,4:Q(0)})
                self.assertTrue(close(expect(v,N,grouped_phase_ops(3)),ch(u)))
                self.assertTrue(close(expect(v,N,grouped_phase_ops(2)),ch(u)))

    def test_10_grouped_source_4th_order_n9(self):
        u,y,z=states_at(5)
        v=cluster_vector(9,{0:y,2:z,4:Q(0),6:Q(0)})
        self.assertTrue(close(expect(v,9,grouped_phase_ops(4)),ch(u)))

    def test_11_original_character_recurrence(self):
        for n in (1,2,5,11):
            u,_,_=states_at(n)
            nxt,_,_=states_at(n+1)
            for h in (-2,1,3):
                self.assertTrue(close(ch(h*nxt),ch(h*u)**16*ch(h*source(n+1,ORIGINAL)),1e-9))

    def test_12_product_state_false_entanglement_necessity(self):
        # A separable one-qubit equatorial state directly exhibits any phase
        # expectation <X+iY>=e^(i theta). Source witness does not force graph entanglement.
        for q in (Q(1,17),Q(5,11),Q(-2,9)):
            vec=[1/math.sqrt(2),ch(q)/math.sqrt(2)]
            self.assertTrue(close(expect(vec,1,{0:"P"}),ch(q)))

    def test_13_wrong_seed_source_phase_still_coherent(self):
        # Coherent wrong seed s*=-pi/16 has selected orbit -T_n.
        # Compute T_n from only authentic future rational forcing (no pi oracle).
        for n in (11,17,29):
            T=sum((Q(1,16**k)*source(n+k,ORIGINAL) for k in range(1,45)),Q())
            self.assertGreater(T,0)
            self.assertLess(T,Q(1,64*n*n))
            v=cluster_vector(7,{0:-T})
            self.assertTrue(close(expect(v,7,grouped_phase_ops(1)),ch(-T)))
            self.assertLess(abs(ch(-T)-1),1/(4*n*n))

    def test_14_source_mutant_changes_witness(self):
        u,y,z=states_at(5)
        w=list(ORIGINAL);w[0]+=1
        x=Q(0)
        for n in range(1,6):x=16*x+source(n,tuple(w))
        self.assertNotEqual(u,x)
        self.assertFalse(close(ch(u),ch(x),1e-12))

    def test_15_stabilizer_coupling_not_visible_locally(self):
        v=cluster_vector(7)
        self.assertTrue(close(expect(v,7,{0:"X"}),0))
        self.assertTrue(close(expect(v,7,{0:"X",1:"Z"}),1))
        self.assertTrue(close(expect(v,7,{0:"X",2:"X",3:"Z"}),1))
        self.assertTrue(close(expect(v,7,{0:"P",2:"P",3:"Z"}),1))

if __name__=="__main__": unittest.main()
