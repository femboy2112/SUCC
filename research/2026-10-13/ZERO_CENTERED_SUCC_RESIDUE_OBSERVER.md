# Zero-centered SUCC: a source-first residue-clock observer (2026-10-13)

**Branch:** research/zero-centered-residue-observers-2026-10-13; parent 6e0d88f1b235b85188393bbcd64ac0436cb71a70. **RH PROVED: no.** This is a research offshoot of the user's question: *what if SUCC is observed from a nontrivial zero instead of from the arithmetic unit?*

## Defined objects and source firewall

For n>=2, integer cell k>=1, let r_n(k)=(k mod n)/n. Set I_k=(1/(k+1),1/k), of measure w_k=1/[k(k+1)]. On x in I_k define g_n(x)={1/(nx)}-(1/n){1/x}. Since floor(1/x)=k and floor(1/(nx))=floor(k/n), **g_n(x)=r_n(k)**. Thus the approximation problem for the constant 1 in L²(0,1) is exactly the problem of approximating the constant sequence 1 in weighted ell²(N,w):

  ||1 - sum a_n g_n||² = sum_{k>=1} |1 - sum a_n r_n(k)|²/[k(k+1)]. (ZCR-01, PROVED LOCAL)

The construction reads no zeta-zero locations. Its arithmetic source is the **actual** integer divisibility structure, not an arbitrary fitted collection of prime phases. It does not supply a completed gamma/pole formula, Weil kernel, or positivity theorem.

## Mellin observer: a genuine conditional obstruction

Define L_s(f)=int_0^1 f(x)x^(s-1) dx for Re(s)>0 on bounded cell functions. The cell series is

  L_s(f)=(1/s) sum_{k>=1} f(k)[k^(-s)-(k+1)^(-s)].

Since r_n(k)-r_n(k-1)=1/n-1_{n|k}, summation by parts in the convergent Dirichlet half-plane Re(s)>1 gives

  L_s(r_n)=(zeta(s)/s)(1/n - n^(-s)).

Analytic continuation extends this identity to Re(s)>0, with removable singularity at s=1, where L_1(r_n)=log(n)/n. (ZCR-02, classical source identity, locally rederived.) For example ||1-2g_2||²=1-log(2), as only the even reciprocal cells contribute. This exact real logarithm is an Archimedean projection of the discrete residue carrier, **not** zeta's completed Gamma factor.

On ell²(w), the cell-Mellin functional has norm squared

  ||L_s||² = sum_{k>=1} |k^(-s)-(k+1)^(-s)|² / (|s|² w_k).

Summands behave like k^(-2 Re(s)), so **L_s is bounded iff Re(s)>1/2**. If rho is an actual nontrivial zero with Re(rho)>1/2, then L_rho annihilates all r_n while L_rho(1)=1/rho. Cauchy-Schwarz yields

  ||1 - sum a_n g_n||_2 >= sqrt(2 Re(rho)-1)/|rho| > 0

for every finite coefficient family. (ZCR-03, **conditional classical obstruction**.) Conversely in 1/2<Re(s)<1, a vanishing Mellin response from any r_n implies zeta(s)=0, because |n^(-s)|>1/n. A zero-centered observer is therefore an annihilating functional, **not** a physical position or a literal zero supplied to an arithmetic construction. On the critical line this particular functional becomes unbounded; that fact does not establish a zero there.

## Finite-horizon theorem / source falsification

Let K>=2 and mu be the actual Dirichlet inverse of the constant-one function. Set a_n=-mu(n) (2<=n<=K) and a_(K+1)=(K+1)sum_{n<=K}mu(n)/n. For 1<=k<=K,

  F_K(k)=sum_{n=2}^{K+1}a_n r_n(k)
        =sum_{n<=k}mu(n) floor(k/n)
        =sum_{m<=k} sum_{d|m}mu(d)=1.

So every finite observation horizon has a **perfect rational interpolant**, regardless of RH. (ZCR-04, PROVED LOCAL.) It follows that the interpolants converge pointwise in the product topology, **not** automatically in L²(w). This is the distinction between a finite observer's complete observations and an actual analytic closure. For any rational target t_1,...,t_K, let d_k=t_k-t_(k-1) (t_0=0), let b=mu*d under Dirichlet convolution, and use a_n=-b(n), a_(K+1)=(K+1)sum b(n)/n. The same calculation gives F_K(k)=t_k; hence any rational finite target is reconstructible. (ZCR-05, PROVED LOCAL.) No theorem of global source identification follows.

## LCM blackout theorem

For any finite set of moduli n_i with L=lcm(n_i), r_(n_i)(jL)=0 for all j>=1. Hence **every finite span** misses target 1 at the synchronized cells jL, independently of coefficients. Since 1/[jL(jL+1)] >= 1/[L² j(j+1)], we obtain

  ||1 - sum a_n g_n||² >= sum_{j>=1}1/[jL(jL+1)] >= 1/L².

(ZCR-06, PROVED LOCAL.) As L increases the lower bound decays, so this is **not** a uniform obstruction to RH. It is an exact demonstration that no finite reconstruction can be globally identical, even when its observed finite prefix is perfect.

## Certified finite probes, controls and boundaries

The new module supplies exact rational residual intervals:

  P_M <= ||1-sum a_n g_n||² <= P_M+(1+sum |a_n|)²/(M+1),

where P_M is the exact sum over k<=M. Its Gram entries have equally exact rational interval enclosures. (ZCR-07.)

**Negative control:** falsify mu(6) by marking the composite 6 as if prime, setting b(6)=-1 instead of authentic mu(6)=+1. Then for K>=6 the altered F_K(k)=1-2 floor(k/6) for k<=K, giving **F_K(6)=-1** and a detected first source defect at 6. (ZCR-08.) An independent single-cell fake perturbation delta at k=6 changes the Mellin observation by delta[s^(-1)(6^(-s)-7^(-s))]; at s=2, delta=1/2, this is 13/7056 (ZCR-09). All these source checks use exact arithmetic and no RH-zero oracle.

**False proof routes:** The formal ket w_s(n)=n^(-s) is a joint eigenvector of adjoint prime dilations when Re(s)>1/2, but its existence does not detect a zero: at s=1 it is normalizable while zeta has a pole. Similarly SUCC's existing virtual_mellin_zeros.py gives a symmetric fake completed-source factor with **auxiliary** off-line zeros, not genuine zeta zeros. Symmetry or normalizability alone cannot authenticate RH source. (ZCR-10, REFUTED shortcut.)

**Unpaid truth debt (ZCR-11, UNVERIFIED):** A zero-independent global L² approximation bound strong enough to prove RH; the completed Gamma, pole, conductor and Weil-form identification; and a principled continuous or categorical intertwiner between the reciprocal-cell observer and the prime SUCC/FUCC Hilbert space. The equivalence of the global approximation problem to RH is **classical external mathematics**, from Nyman–Beurling and Báez-Duarte, not a newly proved equivalence. No finite experiment implies a universal proof.

## Reproduce and next tests

Run: python -m unittest discover -s tests -p test_zero_centered_residue.py
Run: python scripts/zero_centered_residue_probe.py --output /tmp/zero_centered_receipt.json

The local isolated test harness passed; project-wide CI must check the integration after this branch is pushed. The next discriminating work is a source-first global approximation bound, matched Euler versus non-Euler arithmetic sources, rigorous error envelopes as horizon and conductor grow, and an actual (not assumed) source-to-Weil identity. Treat fitted zeros only as separate calibration holdouts.

**Literature/prior art:** Báez-Duarte (2003), *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*: https://arxiv.org/abs/math/0202141 ; Báez-Duarte, *Arithmetical Aspects of Beurling's Real Variable Reformulation of the Riemann Hypothesis*: https://arxiv.org/abs/math/0011254 ; Báez-Duarte (2002), https://doi.org/10.1155/S0161171202013248 . These support the classical global criterion and explicitly warn that pointwise or L¹ convergence may fail in L². **Novel priority is not claimed** for the elementary residue identities.
