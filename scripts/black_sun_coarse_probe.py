"""BLACK SUN A-track coarse spectral probe (exploratory; discovery tool).

Produces the first-window spectral map of the completed Weil form (the
numbers in BLACK_SUN_INDEPENDENT_CAMPAIGN.md BS-A4).  The PRODUCTION,
tested version lives in observational_succ/black_sun_window.py +
tests/test_black_sun_window.py; this probe is kept as the discovery
artifact.  Float64 only; no sign certification at the 1e-4 scale.
"""
"""BLACK SUN A-track coarse probe: first-prime-window Weil spectrum.

Exploratory (double precision). Production version lands in
observational_succ/black_sun_window.py after validation.

Windowed completed Weil form (Carleman/Suzuki representation, independently
re-derived in this campaign):

  Q(v,v) = E_G(v) - C_G ||v||^2 + 2|<v,cosh(.//2)>|^2 - 2|<v,sinh(.//2)>|^2
           - 2 sum_{2<=n<e^{2a}} (Lambda(n)/sqrt n) Re <tau_{log n} v, v>

  E_G(v) = (1/2) iint k_G(x-y)|v(x)-v(y)|^2 dx dy,  k_G(t)=e^{-|t|/2}/(1-e^{-2|t|})
  C_G = gamma + pi/2 + 3 log 2 + log pi
  boundary barrier: E_G(v) = (1/2) iint_{W x W} k_G|v-v|^2 + int_W rho_a(x)|v|^2,
      rho_a(x) = Kbar(x+a) + Kbar(a-x),
      Kbar(z) = int_z^infty k_G = -1/2 ln((1+e^{-z/2})/(1-e^{-z/2})) - arctan(e^{-z/2}).
"""
import numpy as np
from math import log, sqrt, pi, exp

GAMMA = 0.57721566490153286061
LOG2 = 0.69314718055994530942
LOG3 = 1.0986122886681096914
LOG4PI = log(4*pi)
CG = GAMMA + pi/2 + 3*LOG2 + log(pi)   # = gamma + pi/2 + 3 log2 + log pi


def kbar(z: float) -> float:
    """Kbar(z) = int_z^inf e^{-t/2}/(1-e^{-2t}) dt, elementary closed form.

    Derivation: substitute s=e^{-t/2}; then Kbar(z) = int_0^{e^{-z/2}} 2/(1-s^4) ds
    and the antiderivative of 2/(1-s^4) is (1/2)ln((1+s)/(1-s)) + arctan(s).
    """
    z = np.asarray(z, dtype=float)
    s = np.exp(-np.maximum(z, 1e-300)/2)
    val = 0.5*np.log((1+s)/(1-s)) + np.arctan(s)
    return np.where(z > 0, val, np.inf)


def rho_a(x, a):
    """Boundary barrier rho_a(x) on the window (-a,a)."""
    return kbar(x+a) + kbar(a-x)


def von_mangoldt(n):
    if n < 2:
        return 0.0
    # exact prime power check
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            m, k = n, 0
            while m % p == 0:
                m //= p; k += 1
            return log(p) if m == 1 else 0.0
    return log(n)  # n prime


def prime_atoms(a):
    """(log n, Lambda(n)/sqrt n) for 2 <= n < e^{2a}."""
    out = []
    n = 2
    from math import floor
    nmax = int(np.floor(exp(2*a))) if exp(2*a) > 2 else 2
    # n < e^{2a}: strict; at n == e^{2a} the atom sees h at the support
    # endpoint which is zero for smooth v, so include floor and drop exact
    # endpoint hits by testing strict inequality in the overlap instead.
    while n < exp(2*a) + 1e-12:
        lam = von_mangoldt(n)
        if lam > 0 and log(n) < 2*a - 1e-15:
            out.append((log(n), lam/sqrt(n)))
        n += 1
    return out


def window_form_matrix(a, M=1200, mu_fake6=0.0):
    """Nystrom form matrix F and weight vector w on uniform grid.

    Q(v) = v^T F v approximates the windowed form; eigenproblem F v = lam W v.
    All terms: E_G interior + rho barrier - C_G mass + poles - prime shifts.
    mu_fake6: extra fake primitive impulse at log 6 (control; =0 authentic).
    """
    xs = -a + (2*a/M)*(np.arange(M)+0.5)
    w = np.full(M, 2*a/M)
    h = 2*a/M

    # kernel values k_G(x_i - x_j), singular on diagonal
    d = xs[:, None] - xs[None, :]
    ad = np.abs(d)
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.where(ad > 0, np.exp(-ad/2)/(1-np.exp(-2*ad)), 0.0)

    # E_G interior: (1/2) sum_ij w_i w_j K_ij |v_i-v_j|^2
    #             = v^T [ diag(w_i S_i) - (w_i w_j K_ij offdiag) ] v, S_i=sum_{j!=i} w_j K_ij
    WK = K * w[None, :]
    S = WK.sum(axis=1)  # includes j=i term which is zero (K_ii=0)
    F_EG = np.diag(w*(S + rho_a(xs, a)))

    # off-diagonal part of interior interaction
    Wo = np.outer(w, w) * K
    np.fill_diagonal(Wo, 0.0)
    F_EG -= Wo

    # - C_G mass
    F = F_EG - CG*np.diag(w)

    # poles: +2|<v,c>|^2 - 2|<v,s>|^2
    c = np.cosh(xs/2); s = np.sinh(xs/2)
    F += 2*np.outer(w*c, w*c)
    F -= 2*np.outer(w*s, w*s)

    # prime shifts: -c_n [<tau_ell v, v> + <v, tau_ell v>] over the window
    for (ell, cn) in prime_atoms(a):
        # overlap: x in (-a, a-ell), value v(x+ell)
        # linear interpolation of v(x+ell) from grid values
        sh = xs + ell
        L = np.zeros((M, M))
        inside = (sh >= -a) & (sh <= a)
        idx = np.clip(((sh + a)/ (2*a) * (M-1)).astype(int), 0, M-2)
        tfrac = (sh - xs[idx])/ (xs[idx+1]-xs[idx])
        for i in np.where(inside & (xs <= a-ell+1e-15))[0]:
            L[i, idx[i]] += 1-tfrac[i]
            L[i, idx[i]+1] += tfrac[i]
        # mask: x_i <= a - ell (v(x_i) in overlap)
        mask = np.zeros(M); mask[xs <= a-ell+1e-15] = 1.0
        A = (L * (w*mask)[:, None])  # <tau v, v> = v^T A v
        F -= cn*(A + A.T)

    if mu_fake6 > 0:
        # fake primitive composite impulse at log 6 with weight mu_fake6*log(6)
        ell6 = log(6); c6 = mu_fake6*log(6)/sqrt(6)
        if ell6 < 2*a:
            sh = xs + ell6
            L = np.zeros((M, M))
            inside = (sh >= -a) & (sh <= a)
            idx = np.clip(((sh + a)/(2*a)*(M-1)).astype(int), 0, M-2)
            tfrac = (sh - xs[idx])/(xs[idx+1]-xs[idx])
            for i in np.where(inside & (xs <= a-ell6))[0]:
                L[i, idx[i]] += 1-tfrac[i]
                L[i, idx[i]+1] += tfrac[i]
            mask = np.zeros(M); mask[xs <= a-ell6] = 1.0
            A = L * (w*mask)[:, None]
            F -= c6*(A + A.T)

    return F, w, xs


def lowest_eigs(a, M=1200, k=6, **kw):
    F, w, xs = window_form_matrix(a, M, **kw)
    Wsq = np.diag(np.sqrt(w))
    Winv = np.diag(1/np.sqrt(w))
    G = Winv @ F @ Winv
    G = 0.5*(G+G.T)
    vals, vecs = np.linalg.eigh(G)
    # convert: F v = lam W v  <=>  G u = lam u with v = W^{-1} u
    return vals[:k], vecs[:, :k], xs, w


if __name__ == "__main__":
    import sys
    print(f"C_G = {CG:.15f}")
    # sanity: Kbar series check
    for z in [0.05, 0.3, 1.0, 3.0]:
        s = sum(exp(-(2*j+0.5)*z)/(2*j+0.5) for j in range(4000))
        print(f"Kbar({z}): closed={kbar(z):.12f} series={s:.12f}")
    a_list = [float(x) for x in sys.argv[1:]] or [0.36, 0.42, 0.48, 0.50, 0.52, 0.54, 0.5493]
    for a in a_list:
        vals, vecs, xs, w = lowest_eigs(a, M=1000, k=4)
        print(f"a={a:.4f}  atoms={[(round(l,3),round(c,4)) for l,c in prime_atoms(a)]}"
              f"  lambda_min={vals[0]:+.6f}  next={vals[1]:+.4f} {vals[2]:+.4f} {vals[3]:+.4f}")
def inspect(a, M=1000):
    vals, vecs, xs, w = lowest_eigs(a, M=M, k=3)
    print(f"=== a={a} M={M} ===")
    for j in range(3):
        u = vecs[:, j]
        v = u/np.sqrt(w)  # values of v at nodes
        v = v/np.sqrt(np.sum(w*v**2))
        ev = np.sum(w*v*(np.cosh(xs/2)))
        es = np.sum(w*v*(np.sinh(xs/2)))
        # boundary values, parity
        print(f" lam{j}={vals[j]:+.6f}  v(-a)={v[0]:+.4f} v(a)={v[-1]:+.4f} "
              f"v(0)={v[M//2]:+.4f} |<v,c>|={abs(ev):.4f} |<v,s>|={abs(es):.4f} "
              f"argmax={xs[np.argmax(np.abs(v))]:+.3f}")
    return vals, vecs, xs, w
