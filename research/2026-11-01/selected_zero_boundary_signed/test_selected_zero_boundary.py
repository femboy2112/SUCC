"""Regression for the selected zero-boundary signed-lag attack (SZB-01..04).

Self-contained (stdlib + mpmath/numpy); imports nothing from the repo tree. Research-status:
these tests pin NEGATIVE / obstruction results, not any advance on the gate. Run WITHOUT
`python -I`. Frozen: U_0=0, r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
"""
import math, unittest
import mpmath as mp, numpy as np

Wf = np.array([4.,-2.,-1.,-1.]); Pf = np.array([7/8,1/2,3/8,1/4])

def r_mp(n):
    return mp.mpf(4)/(8*n-7)-mp.mpf(2)/(8*n-4)-mp.mpf(1)/(8*n-3)-mp.mpf(1)/(8*n-2)

class SZB01_ExactReduction(unittest.TestCase):
    def test_zero_minus_counterseed_is_digit_term(self):
        """U_n(0) - U_n(s*) = 16^{n-1} pi exactly (the homogeneous recurrence; SZB-01 core)."""
        mp.mp.dps = 60
        U0 = mp.mpf(0); Us = -mp.pi/16
        for n in range(1, 25):
            rn = r_mp(n); U0 = 16*U0 + rn; Us = 16*Us + rn
            self.assertTrue(mp.almosteq(U0 - Us, mp.mpf(16)**(n-1)*mp.pi, rel_eps=mp.mpf(10)**-45),
                            (n, mp.nstr(U0-Us,20)))

class SZB02_PositivityRefuted(unittest.TestCase):
    def _T(self, nv, M=18):
        t = np.zeros_like(nv, dtype=float)
        for m in range(1, M+1): t += (16.**(-m))*(4./(8*(nv+m)-7)-2./(8*(nv+m)-4)-1./(8*(nv+m)-3)-1./(8*(nv+m)-2))
        return t
    def _Rbox(self, nv, k, d):
        acc = np.zeros_like(nv, dtype=float)
        for j in range(1, k+1):
            inner = np.zeros_like(nv, dtype=float)
            for w, p in zip(Wf, Pf): inner += (w/8.)*((p-j)**d)/(nv+j-p)
            acc += (16.**(-j))*inner
        return (16.**k)*(nv.astype(float)**(-d))*acc
    def _xwin(self, Nmax, win=13):
        mp.mp.dps = int((Nmax+win+10)*math.log10(16))+25
        f = mp.pi-3; digs=[]
        for _ in range(Nmax+win+2):
            f*=16; dd=int(f); digs.append(dd); f-=dd
        digs=np.array(digs,float); pw=16.**(-(np.arange(win)+1))
        return np.array([np.dot(digs[m:m+win],pw) for m in range(Nmax+1)])
    def test_per_lag_corr_goes_negative(self):
        """The candidate 'per-lag corrected correlation >= 0' is FALSE (SZB-02)."""
        N=8192; d=2; h=1; x=self._xwin(N)
        K=int(math.floor((d+1)*math.log(N,16)))
        found_negative=False
        for k in range(1, K):
            nv=np.arange(1,N-k+1); xn=x[nv-1]; xnk=x[nv-1+k]
            Tn=self._T(nv); Tnk=self._T(nv+k)
            ph=(xnk-xn)+(Tn-Tnk)-self._Rbox(nv,k,d)
            if np.cos(2*np.pi*h*ph).mean() < -1e-3: found_negative=True
        self.assertTrue(found_negative, "expected a negative per-lag corrected correlation")

class SZB03_AngularPeriodSeedBlind(unittest.TestCase):
    def test_period_is_pi_over_16(self):
        mp.mp.dps=50
        P=lambda t: 4-2*t**3-t**4-t**5
        self.assertTrue(mp.almosteq(mp.quad(lambda t:P(t)/(16-t**8),[0,1]), mp.pi/16, rel_eps=mp.mpf(10)**-38))
    def test_same_source_q15_orbit_is_nonnormal(self):
        """Same four-pole forcing, completed point 1/5: |S_N(h)|/N = 1 (nonnormal), while the
        angular-period identity above is unchanged => seed-blind => representation identity."""
        for h in (1,2,3):
            N=2000
            S=sum(mp.e**(2j*mp.pi*h*((pow(16,n,5))/mp.mpf(5))) for n in range(1,N+1))
            self.assertAlmostEqual(abs(S)/N, 1.0, places=9)

class SZB04_WithinCellIsShiftedGate(unittest.TestCase):
    def test_digit_shift_invariance(self):
        """|S_N(h*16^k)|/N is independent of k for the zero seed (within-cell = shifted gate)."""
        mp.mp.dps = int((20000+40)*math.log10(16))+25
        f=mp.pi-3; digs=[]
        for _ in range(20000+20):
            f*=16; dd=int(f); digs.append(dd); f-=dd
        digs=np.array(digs,float); pw=16.**(-(np.arange(13)+1))
        N=16384; x=np.array([np.dot(digs[m:m+13],pw) for m in range(N+1)])
        nv=np.arange(1,N+1); base=None
        for k in (1,2,3):
            H=1*(16**k); val=abs(np.sum(np.exp(2j*np.pi*H*x[nv-1])))/N
            # within-cell = the SAME object (a shifted-window Weyl sum): close up to the
            # finite-window truncation and a k-term boundary shift, not exactly equal.
            self.assertLess(val, 0.02)
            if base is None: base=val
            else: self.assertLess(abs(val-base), 5e-4)

if __name__=="__main__":
    unittest.main()
