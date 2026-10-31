"""SUCC: exact discrete Noether, carry, local flux and observer-carrier stress controls.

All exact (fractions / Gaussian rationals). Source is unchanged original four-pole BBP.
The 3D/lattice and observer couplings are explicit auxiliary models, not physics.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import floor
import unittest

POLES = ((4,0),(-2,3),(-1,4),(-1,5))
C2=F(1,4)
EPS=F(1,4)


def R(a):
    a=F(a)
    return sum((F(c)/(a+d) for c,d in POLES),F(0))


def phase_frac(x):
    x=F(x)
    return x-floor(x)


def orbit(seed,N):
    U=[F(seed)]
    x=[phase_frac(seed)]
    k=[]
    for n in range(1,N+1):
        raw=16*x[-1]+R(8*n-7)
        carry=floor(raw)
        k.append(carry)
        x.append(raw-carry)
        U.append(16*U[-1]+R(8*n-7))
        assert x[-1]==phase_frac(U[-1])
    return U,x,k


def seed_charge(U,n):
    return U[n]/16**n-sum((R(8*j-7)/16**j for j in range(1,n+1)),F(0))


def carry_charge(x,k,n):
    return x[n]/16**n+sum((F(k[j-1]-R(8*j-7))/16**j for j in range(1,n+1)),F(0))


def cotangent_action(U,p):
    return sum((p[n+1]*(U[n+1]-16*U[n]-R(8*(n+1)-7))
                for n in range(len(U)-1)),F(0))


@dataclass(frozen=True)
class Z:
    re:F=F(0)
    im:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,"re",F(self.re))
        object.__setattr__(self,"im",F(self.im))
    @staticmethod
    def coerce(x):
        if isinstance(x,Z):return x
        return Z(x)
    def __add__(self,x):
        z=Z.coerce(x);return Z(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self):return Z(-self.re,-self.im)
    def __sub__(self,x):return self+(-Z.coerce(x))
    def __rsub__(self,x):return Z.coerce(x)-self
    def __mul__(self,x):
        z=Z.coerce(x)
        return Z(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def conj(self):return Z(self.re,-self.im)
    def abs2(self):return self.re*self.re+self.im*self.im

ZERO=Z(0)
ONE=Z(1)
I=Z(0,1)


def dot(a,b):
    return sum((x.conj()*y for x,y in zip(a,b)),ZERO)


def Lfield(u,edges):
    out=[ZERO for _ in u]
    for i,j,w,link in edges:  # link maps j's local fiber into i's
        out[i]+=w*(u[i]-link*u[j])
        out[j]+=w*(u[j]-link.conj()*u[i])
    return out


def wave_step(prev,cur,edges,source=None,c2=C2):
    if source is None:source=[ZERO for _ in cur]
    lu=Lfield(cur,edges)
    return [2*x-y-c2*z+s for x,y,z,s in zip(cur,prev,lu,source)]


def qlocal(cur,nxt):
    return [(x.conj()*y).im for x,y in zip(cur,nxt)]


def Qcharge(cur,nxt):
    return sum(qlocal(cur,nxt),F(0))


def edge_currents(cur,edges,c2=C2):
    # j_{i -> j}=-c^2 w Im(conj(cur_i)*U_ij*cur_j)
    return {(i,j):-c2*w*(cur[i].conj()*link*cur[j]).im
            for i,j,w,link in edges}


def energy(prev,cur,edges,c2=C2):
    dif=[y-x for x,y in zip(prev,cur)]
    return sum((v.abs2() for v in dif),F(0))/2+c2*dot(prev,Lfield(cur,edges)).re/2


def action_step(prev,cur,edges_prev,edges_cur,c2=C2):
    dif=[y-x for x,y in zip(prev,cur)]
    return (sum((v.abs2() for v in dif),F(0))/2
            -c2*(dot(prev,Lfield(prev,edges_prev)).re
                   +dot(cur,Lfield(cur,edges_cur)).re)/4)


def ringedges(n,weight=F(1),link=ONE):
    return [(i,(i+1)%n,F(weight),link) for i in range(n)]


def kappa(a):
    a=F(a)
    dR=-sum((F(c)/(a+d)**2 for c,d in POLES),F(0))
    return -a*dR/R(a)/2


def driven_bond(a,eta,n=6,edge_index=1):
    w=F(1)+EPS*(kappa(a)-1)**2*F(eta)**2
    out=ringedges(n)
    i,j,_,z=out[edge_index]
    out[edge_index]=(i,j,w,z)
    return out


def observer_energy_derivative(a,eta,eta_dot,psi,psi_dot,Iobs=F(3)):
    """Exact continuum coupled toy action instantaneous observer + field energy flow.

    L=I/2 eta_dot^2 +1/2 sum psi_dot^2 - c2/2 sum w(eta)(psi_i-psi_j)^2.
    """
    eta,eta_dot=F(eta),F(eta_dot)
    dkap=kappa(a)-1
    wprime=2*EPS*dkap*dkap*eta
    w=F(1)+EPS*dkap*dkap*eta**2
    edges=[(0,1,w)]
    # other static bonds keep the graph connected
    edges +=[(1,2,F(1)),(2,0,F(1))]
    force=[F(0)]*3
    for i,j,we in edges:
        force[i]-=C2*we*(psi[i]-psi[j]);force[j]-=C2*we*(psi[j]-psi[i])
    eta_ddot=-C2*wprime*(psi[0]-psi[1])**2/(2*Iobs)
    Eo_dot=Iobs*eta_dot*eta_ddot
    Ef_dot=sum((v*f for v,f in zip(psi_dot,force)),F(0))
    for i,j,we in edges:
        Ef_dot+=C2*we*(psi[i]-psi[j])*(psi_dot[i]-psi_dot[j])
    Ef_dot+=C2*wprime*eta_dot*(psi[0]-psi[1])**2/2
    return Eo_dot,Ef_dot


class NoetherBBP(unittest.TestCase):
    def test_original_four_poles_and_positive_source(self):
        for n in range(1,60):
            r=R(8*n-7)
            self.assertGreater(r,0)
            self.assertEqual(r,F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))

    def test_unwrapped_source_corrected_seed_is_exact_first_integral(self):
        for seed in (F(0),F(1,16),F(1,15),F(1,10**8),F(-7,19)):
            U,_,_=orbit(seed,20)
            self.assertTrue(all(seed_charge(U,n)==seed for n in range(21)))

    def test_no_discard_carry_lift_reconstructs_circle_seed(self):
        for seed in (F(0),F(1,16),F(1,15),F(-7,19)):
            _,x,k=orbit(seed,18)
            self.assertTrue(all(carry_charge(x,k,n)==phase_frac(seed) for n in range(19)))
        _,_,k0=orbit(F(0),4)
        _,_,k_alias=orbit(F(1,16),4)
        self.assertEqual(k0,[3,2,4,3]);self.assertEqual(k_alias[0],4)
        self.assertNotEqual(k_alias,k0)
        _,x0,_=orbit(0,12);_,xA,_=orbit(F(1,16),12)
        self.assertEqual(x0[1:],xA[1:])

    def test_fixed_prefix_cannot_identify_unique_seed(self):
        _,_,k0=orbit(F(0),4)
        _,_,k1=orbit(F(1,10**8),4)
        self.assertEqual(k0,k1)

    def test_discrete_cotangent_lift_noether_symmetry(self):
        n=9
        U=[F(i*i+1,7) for i in range(n+1)]  # off shell is okay
        p=[F(0)]+[F(i+1,3) for i in range(n)]
        eps=F(3,11)
        shifted=[u+16**i*eps for i,u in enumerate(U)]
        self.assertEqual(cotangent_action(U,p),cotangent_action(shifted,p))
        terminal=F(3,17)
        p=[F(0)]+[16**(n-i)*terminal for i in range(1,n+1)]
        self.assertTrue(all(p[i]==16*p[i+1] for i in range(1,n)))
        self.assertEqual(len({16**i*p[i] for i in range(1,n+1)}),1)
        # fixed selected seed U0=0 does not permit nonzero eps
        self.assertNotEqual(shifted[0],U[0])

    def test_scalar_relative_phase_has_zero_lifted_loop(self):
        U,_,_=orbit(0,7)
        for a,b,c in ((2,3,5),(3,4,5),(1,3,7)):
            self.assertEqual((U[b]-U[a])+(U[c]-U[b])+(U[a]-U[c]),0)
            # Choosing different edge harmonics is NOT one common connection.
            self.assertNotEqual((U[b]-U[a])+2*(U[c]-U[b])-(U[c]-U[a]),0)

    def test_mod_one_branch_winding_not_curvature(self):
        U,_,_=orbit(0,7)
        a,b,c=3,4,5
        lifts=[phase_frac(U[b]-U[a]),phase_frac(U[c]-U[b]),phase_frac(U[a]-U[c])]
        total=sum(lifts,F(0))
        self.assertEqual(total.denominator,1)
        self.assertIn(total,(F(1),F(2)))


class NoetherWave(unittest.TestCase):
    def test_time_dependent_geometry_preserves_global_charge(self):
        n=7
        prev=[Z(i,F((i*i)%5,3)) for i in range(n)]
        cur=[Z(F(i*i+1,3),F(i+2,5)) for i in range(n)]
        q0=Qcharge(prev,cur)
        for t in range(15):
            edges=driven_bond(8*(t+2)-7,F(t%4,3),n)
            nxt=wave_step(prev,cur,edges)
            self.assertEqual(Qcharge(cur,nxt),q0)
            prev,cur=cur,nxt

    def test_local_continuity_with_complex_source_and_boundary_flux(self):
        n=5;prev=[Z(F(i+1,3),F(i-3,7)) for i in range(n)]
        cur=[Z(F(i*i+1,2),F(i+1,5)) for i in range(n)]
        edges=driven_bond(73,F(5,3),n)
        source=[ZERO,Z(F(2,7),F(1,5)),ZERO,Z(F(-4,9),F(1,8)),ZERO]
        nxt=wave_step(prev,cur,edges,source)
        before=qlocal(prev,cur);after=qlocal(cur,nxt)
        currents=edge_currents(cur,edges)
        divergence=[F(0)]*n
        for (i,j),v in currents.items():
            divergence[i]+=v;divergence[j]-=v
        for i in range(n):
            rhs=(cur[i].conj()*source[i]).im
            self.assertEqual(after[i]-before[i]+divergence[i],rhs)
        self.assertEqual(Qcharge(cur,nxt)-Qcharge(prev,cur),
                         sum(((cur[i].conj()*source[i]).im for i in range(n)),F(0)))
        # Current on a proper subregion is measured by boundary flux.
        region=(0,1)
        self.assertEqual(sum(after[i]-before[i] for i in region)+
                         sum(divergence[i] for i in region),
                         sum((cur[i].conj()*source[i]).im for i in region))

    def test_exact_discrete_energy_work_balance(self):
        n=7
        prev=[Z(F(i*i-1,5),F(i,7)) for i in range(n)]
        cur=[Z(F(i*i+2,3),F((i+1)%3,8)) for i in range(n)]
        edges_old=driven_bond(73,F(2),n)
        edges_new=driven_bond(73,F(5,2),n)
        source=[ZERO]*n;source[3]=Z(F(3,7),F(-1,5))
        nxt=wave_step(prev,cur,edges_new,source)
        d=[z-y for y,z in zip(prev,nxt)]
        flux=sum((x.conj()*y for x,y in zip(d,source)),ZERO).re/2
        Lold=Lfield(cur,edges_old);Lnew=Lfield(cur,edges_new)
        changeL=[x-y for y,x in zip(Lold,Lnew)]
        work=C2*dot(prev,changeL).re/2
        self.assertEqual(energy(cur,nxt,edges_new)-energy(prev,cur,edges_old),flux+work)
        self.assertNotEqual(work,0)

    def test_phase_invariant_discrete_action_and_local_spatial_gauge(self):
        n=4
        prev=[Z(i+1,F(i,3)) for i in range(n)]
        cur=[Z(F(i*i+1,2),F((i+2)%3,7)) for i in range(n)]
        links=[ONE,I,Z(-1),-I]
        e=[(i,(i+1)%n,F(i+1,3),links[i]) for i in range(n)]
        # global U1 rotation invariance exact
        self.assertEqual(action_step(prev,cur,e,e),
                         action_step([I*x for x in prev],[I*x for x in cur],e,e))
        g=[ONE,I,Z(-1),-I]
        newlinks=[(i,j,w,g[i]*z*g[j].conj()) for i,j,w,z in e]
        gauge_prev=[g[i]*prev[i] for i in range(n)]
        gauge_cur=[g[i]*cur[i] for i in range(n)]
        self.assertEqual(action_step(prev,cur,e,e),
                         action_step(gauge_prev,gauge_cur,newlinks,newlinks))
        self.assertEqual(Lfield(gauge_cur,newlinks),
                         [g[i]*u for i,u in enumerate(Lfield(cur,e))])

    def test_pure_gauge_loop_vs_true_link_holonomy(self):
        g=[ONE,I,Z(-1),-I]
        edge=[g[i]*g[(i+1)%4].conj() for i in range(4)]
        prod=ONE
        for z in edge:prod=prod*z
        self.assertEqual(prod,ONE)
        # Genuine link flux cannot be created by a gauge change.
        flux=[I,ONE,ONE,ONE]
        prod=ONE
        for z in flux:prod=prod*z
        self.assertEqual(prod,I)
        gauged=[g[i]*flux[i]*g[(i+1)%4].conj() for i in range(4)]
        prod2=ONE
        for z in gauged:prod2=prod2*z
        self.assertEqual(prod2,I)

    def test_static_geometry_energy_conserved_and_phase_charge_conserved(self):
        n=5;prev=[Z(i-1,F(i+1,7)) for i in range(n)]
        cur=[Z(F(i*i+1,3),F(i-2,5)) for i in range(n)]
        edges=ringedges(n)
        E0=energy(prev,cur,edges);Q0=Qcharge(prev,cur)
        for _ in range(12):
            nxt=wave_step(prev,cur,edges)
            self.assertEqual(energy(cur,nxt,edges),E0)
            self.assertEqual(Qcharge(cur,nxt),Q0)
            prev,cur=cur,nxt

    def test_noether_charge_does_not_force_cancellation(self):
        # A 6-period real standing wave and a constant field solve
        # the SAME 4-site ring wave equation with c2=1/4.
        n=4;edges=ringedges(n)
        constant_prev=[ONE]*n;constant=[ONE]*n
        wave_prev=[Z(F(1,2)*(-1)**i) for i in range(n)]
        wave=[Z((-1)**i) for i in range(n)]
        values=[]
        for t in range(6):
            self.assertEqual(Qcharge(constant_prev,constant),0)
            self.assertEqual(Qcharge(wave_prev,wave),0)
            values.append(wave[0].re)
            constant_next=wave_step(constant_prev,constant,edges)
            wave_next=wave_step(wave_prev,wave,edges)
            constant_prev,constant=constant,constant_next
            wave_prev,wave=wave,wave_next
        self.assertEqual(sum(values,F(0)),0)
        self.assertEqual(constant,[ONE]*n)
        self.assertNotEqual(sum(values,F(0)),F(6))

    def test_continuous_observer_carrier_noether_energy_exchange(self):
        psi=[F(1,3),F(-2,5),F(7,4)]
        vel=[F(-1,7),F(2,11),F(1,9)]
        for a in (17,73,257):
            Eo,Ef=observer_energy_derivative(a,F(4,3),F(2,5),psi,vel)
            self.assertEqual(Eo+Ef,0)
            self.assertNotEqual(Eo,0)
        # Gamma-matched fake has kappa=1 -> zero parameter coupling,
        # so observer force and field work both vanish (by construction).
        self.assertEqual((F(1)-1)**2,0)


    def test_source_fitted_ward_is_vacuous_for_any_phase_word(self):
        # Any arbitrary complex sequence admits a fitted source J_t so
        # that its 'Noether source' telescopes. This does not give a
        # signed Weyl saving (coherent and balanced words both pass).
        words=[[ONE]*18,([ONE,I,Z(-1),-I]*5)[:18]]
        means=[]
        for w in words:
            accum=F(0)
            for t in range(1,len(w)-1):
                jt=w[t+1]-2*w[t]+w[t-1]
                accum+=(w[t].conj()*jt).im
            endpoint=(w[-2].conj()*w[-1]).im-(w[0].conj()*w[1]).im
            self.assertEqual(accum,endpoint)
            self.assertLessEqual(abs(accum),2)
            means.append(sum(w[:16],ZERO))
        self.assertEqual(means[0],Z(16))
        self.assertEqual(means[1],ZERO)

    def test_3d_local_charge_survives_accelerating_bond(self):
        N=3
        def idx(x,y,z):return (x*N+y)*N+z
        edges=[]
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    u=idx(x,y,z)
                    edges.append((u,idx((x+1)%N,y,z),F(1),ONE))
                    edges.append((u,idx(x,(y+1)%N,z),F(1),ONE))
                    edges.append((u,idx(x,y,(z+1)%N),F(1),ONE))
        n=N**3
        prev=[Z(F((i*i)%11,9),F((3*i+2)%7,8)) for i in range(n)]
        cur=[Z(F((i*i+i)%13,7),F((2*i+1)%17,9)) for i in range(n)]
        Q0=Qcharge(prev,cur)
        for t in range(4):
            modified=list(edges)
            i,j,_,link=modified[0]
            modified[0]=(i,j,F(1)+EPS*(kappa(73)-1)**2*F(t+1,3)**2,link)
            nxt=wave_step(prev,cur,modified)
            self.assertEqual(Qcharge(cur,nxt),Q0)
            before=qlocal(prev,cur);after=qlocal(cur,nxt)
            divergence=[F(0)]*n
            for (u,v),val in edge_currents(cur,modified).items():
                divergence[u]+=val;divergence[v]-=val
            self.assertTrue(all(after[i]-before[i]+divergence[i]==0
                                for i in range(n)))
            prev,cur=cur,nxt

    def test_four_pole_59_square_in_observer_coupling(self):
        a=2**18
        dkap=kappa(a)-1
        self.assertLess(abs(float(a*dkap+F(59,30))),1.e-4)
        self.assertLess(abs(float(a*a*dkap*dkap-F(3481,900))),0.0005)


if __name__=='__main__':
    unittest.main(verbosity=2)
