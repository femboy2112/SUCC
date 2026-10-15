# Operation TATE — local conductor, global completion, and the signed-Weil frontier

Date: 2026-10-14. Base: main at 03db44203147a7b28d445bb9f970fa71360e78c4 (Phoenix II). Work branch: research/tate-source-fourier-conductor-2026-10-14. All sources here are *declared mathematical* sources, not physical instruments. No nontrivial zeta-zero positions are ever construction inputs. Classical Tate theory is imported, not claimed as a new theorem. **RH PROVED: NO.**

## 1. Why Tate is the right orientation, and what it cannot do

The proposed gold standard is the Tate *test-function interface*. A legitimate global arithmetic construction must account simultaneously for local fields, normalized additive characters, self-dual additive Haar, multiplicative Haar, actual characters and their conductors, Fourier transform, multiplicative Mellin transform, Poisson summation, and the Gamma/conductor/epsilon/pole bookkeeping. The place chart and test-function domain must survive every arrow.

That is a deeper specification than matching a sampled zeta value or manufacturing a positive SUCC covariance. It also cannot, by itself, establish Weil positivity. Tate builds analytic continuation and functional equations; the sign of the completed *Weil quadratic form* is an additional and RH-hard assertion.

Existing main already establishes partial trivial-character rational-place identities in observational_succ/all_places_zeta.py and substantial original-source Weil/Suzuki infrastructure in completed_weil_transport.py, source_weil_hierarchy.py, suzuki_legendre_source.py, and suzuki_moment_schur.py. This branch adds the elementary *ramified* conductor-one transport chart, an independent nontrivial Hecke/Dirichlet-completion positive control, and a source-visibility no-go with a lawful repair. It does not replace any archived originals.

## 2. Exact finite-local theorem T1: Tate ball transfer

Fix a genuine rational prime $p$. Use the local additive character $\psi_p(x)=\exp(2\pi i\{x\}_p)$; additive Haar normalized by $\mathrm{vol}(\mathbb Z_p)=1$; multiplicative Haar normalized by $\mathrm{vol}^{\times}(\mathbb Z_p^{\times})=1$; and $|p|_p=p^{-1}$. These choices are compatible with $\psi_\infty(x)=\exp(-2\pi i x)$ on the diagonal rational source, as already tested in all_places_zeta.py.

For an unramified character $\chi_p$ with $\omega=\chi_p(p)\in\{1,-1\}$ and the Schwartz–Bruhat test $\phi_a=1_{p^a\mathbb Z_p}$ for any integer $a$, define
\[
Z_p(s,\phi,\chi)=\int_{\mathbb Q_p^\times}\phi(x)\chi(x)|x|_p^s\,d^\times x,\qquad
\widehat\phi(y)=\int_{\mathbb Q_p}\phi(x)\psi_p(xy)\,dx.
\]
Then $\widehat\phi_a=p^{-a}1_{p^{-a}\mathbb Z_p}$, and meromorphically
\[
 Z_p(s,\phi_a,\chi)=\frac{\omega^a p^{-as}}{1-\omega p^{-s}},\qquad
 Z_p(1-s,\widehat\phi_a,\chi^{-1})
 =\frac{\omega^a p^{-as}}{1-\omega^{-1}p^{s-1}}.
\]
Consequently the **forward/dual ratio** is
\[
 R_p(s,\omega)=\frac{1-\omega^{-1}p^{s-1}}{1-\omega p^{-s}},
\]
independent of the ball shift $a$. The inverse of this ratio is the local gamma-factor convention used by many presentations of Tate. The code deliberately stores both directions instead of silently interchanging them.

**Proof:** Each shell $p^j\mathbb Z_p^\times$ has multiplicative volume one, character value $\omega^j$, and norm $p^{-j}$. Sum the geometric progression for $j\ge a$. Fourier of a ball is its annihilator multiplied by its additive Haar mass. For the dual sum use $j\ge-a$ and multiply by $p^{-a}$. The identities for integer $s\ge2$ are meromorphic evaluations; the dual defining integral does *not* generally converge at these same points. The tests contain 210 exact rational configurations, independent shift changes, wrong Haar-scaling mutants, negative $\omega$, and fake-composite rejection. Status: CLASSICAL / PROVED LOCAL.

## 3. Exact ramified theorem T2 and the observational probe-gap

Let $\chi_3$ be the primitive quadratic Dirichlet character modulo $3$, with $\chi_3(1)=1,\chi_3(2)=-1$ and Dirichlet $\chi_3(3n)=0$. For the *local multiplicative component* at $p=3$, choose the usual unit character and assign value one to the uniformizer $3$; do not identify local $\chi_3(3)$ with the Dirichlet coefficient $\chi_3(3)=0$.

Let $\delta=\sqrt{-3}=i\sqrt3$ and $\zeta_3=(-1+\delta)/2$ in the exactly implemented field $\mathbb Q(\sqrt{-3})$. For a unit residue $u\in\{1,2\}$ set $\phi_u=1_{u+3\mathbb Z_3}$. Direct additive character orthogonality gives
\[
\widehat\phi_u(y)=\tfrac13\psi_3(uy)\,1_{3^{-1}\mathbb Z_3}(y),\qquad
Z_3(s,\phi_u,\chi_3)=\tfrac12\chi_3(u).
\]
The finite Gauss sum is exactly
\[
 \tau_u=\sum_{v=1,2}\chi_3(v)\zeta_3^{uv}=\chi_3(u)\delta,
 \qquad \tau_1^2=-3,\quad|\tau_1|^2=3.
\]
On the Fourier-dual multiplicative integral only valuation $-1$ survives; at valuations $\ge0$ the nontrivial unit character averages to zero. Thus
\[
 Z_3(1-s,\widehat\phi_u,\chi_3^{-1})
 =\frac{\chi_3(u)\delta}{2\,3^s},
 \quad
 \frac{Z_3(s,\phi_u,\chi_3)}{Z_3(1-s,\widehat\phi_u,\chi_3^{-1})}
 =\frac{3^s}{\delta}=-3^{s-1}\delta.
\]
This is a genuine ramified local functional-equation test with a nontrivial *phase*, not just the unramified geometric Euler factor.

**Source-indexed obstruction:** If an observer E has only the coarse unit observation $\phi_1+\phi_2=1_{\mathbb Z_3^\times}$, then its $\chi_3$-weighted Mellin observation is $+1/2-1/2=0$. Its map has a nonzero character mode in the kernel. No postprocessing of this *one scalar* recovers the two independently signed coset values. Refinement to the two conductor-level cosets yields $(+1/2,-1/2)$ and the nonzero Gauss phase. This is a finite exact instance of a SUCC **probe gap**, with a concrete lawful source-probe repair. It neither demonstrates a universal hard-field repair nor a physical observer. Status: CLASSICAL / PROVED LOCAL; next probe: general $p^f$ and other root numbers.

## 4. Global character theorem T3: completed $\chi_{-3}$ without zero input

The character is odd, $\chi_3(-1)=-1$. The real test $x\,e^{-\pi x^2}$ paired with the sign character has the shifted Gamma factor $\pi^{-(s+1)/2}\Gamma((s+1)/2)$ and Fourier eigenphase $-i$. The local Gauss sum is $+i\sqrt3$, hence the primitive conductor-3 root number $\tau/(i\sqrt3)=+1$.

Classical Poisson summation on residue classes gives the *odd-character theta*:
\[
\Theta_\chi(t)=\sum_{n\in\mathbb Z} n\chi_3(n)\exp(-\pi n^2 t/3)
=t^{-3/2}\Theta_\chi(1/t).
\]
Initially for $\operatorname{Re}(s)>1$, its Mellin integral equals twice the completed Dirichlet $L$-function
\[
\Lambda_\chi(s)=\Big(\frac3\pi\Big)^{(s+1)/2}
\Gamma((s+1)/2)L(s,\chi_3).
\]
Use the $t\leftrightarrow 1/t$ theta involution to split the Mellin integral at one. With $A_n=\pi n^2/3$, the resulting **source-defined entire** continuation is
\[
\Lambda_\chi(s)=\sum_{n\ge1}n\chi_3(n)
\left[A_n^{-(s+1)/2}\Gamma((s+1)/2,A_n)
     +A_n^{-(2-s)/2}\Gamma((2-s)/2,A_n)\right].
\]
The upper incomplete Gamma $\Gamma(z,A)$ is entire in $z$ for every $A>0$. The series converges locally uniformly (Gaussian decay), and the two terms exchange under $s\mapsto1-s$: $\Lambda_\chi(s)=\Lambda_\chi(1-s)$. This is a *classical* Dirichlet/Tate completion with a zero-independent source constructor; source numerical results are separately calibrated against the **Hurwitz-zeta** expression $3^{-s}(\zeta(s,1/3)-\zeta(s,2/3))$, which never enters that constructor.

### T3b: rigorously quantified full critical-strip truncation

Let $\Lambda_{\chi,N}$ be the last series restricted to $n\le N$. For **every** integer $N\ge1$ and every complex $s$ with $0\le\operatorname{Re}(s)\le1$, regardless of $\operatorname{Im}(s)$,
\[
 |\Lambda_\chi(s)-\Lambda_{\chi,N}(s)|
 \le \frac{\exp(-N^2)}{N^2}
 \le \frac{1}{N^2\sum_{k=0}^{K}N^{2k}/k!}
\]
for any integer $K\ge0$.

**Proof:** From the two-chart integral, $|\Theta_\chi(t)|\le2\sum_{n\ge1}n e^{-A n^2 t}$, $A=\pi/3>1$. For $t\ge1$ on the stated strip, both $t^{(s-1)/2}$ and $t^{-s/2}$ have modulus at most one. The omitted tail is bounded by $(2/A)\sum_{n>N}e^{-A n^2}/n\le2\int_N^\infty e^{-x^2}/x\,dx$. For $x\ge N$, bound $1/x\le1/N$ and use $\int_N^\infty e^{-x^2}dx\le e^{-N^2}/(2N)$, obtaining $e^{-N^2}/N^2$. Finally $e^{N^2}\ge\sum_{k=0}^K N^{2k}/k!$, so the reported last bound is **exactly rational**, derived rather than fitted. Note that this bounds analytic truncation only: it does not validate floating-point Gamma/Hurwitz rounding, and the classical Poisson identity is an imported premise.

## 5. Source-canonical Euler jets, and a precise negative theorem T4

For any unramified genuine $p$ and twist $\chi$ the source dictates
\[
 -L'/L(s,\chi)=\sum_{p}\sum_{k\ge1}\log p\,\chi(p)^k p^{-ks}
 \quad(\operatorname{Re}(s)>1).
\]
For the conductor-3 character, the ramified $p=3$ local Euler factor is *absent*: global Dirichlet $\chi_3(3)=0$. The first $p=2$ jet has $\chi_3(2)=-1$, so the *raw* prime coefficient is negative. This is an exact stress test of any alleged universal prime-current positivity mechanism. The implementation encodes the rational coefficient of each formal $\log p$; it does not evaluate a fake infinite Euler product outside its half-plane.

**T4 (counterexample):** $P(s)=1-\frac{16}{3}s(1-s)$ satisfies $P(1-s)=P(s)$, $P(0)=P(1)=1$, yet $P(1/4)=P(3/4)=0$. Multiplying the classical meromorphic *completed* zeta by $P$ preserves its functional equation and the same simple-pole residues at $0,1$ while injecting off-critical zeros. It violates the authentic Euler germ and is therefore **not** a counterexample to RH. It is a decisive counterexample to the shortcut 'functional equation + correct pole normalization implies RH'. The precise source identification is indispensable.

## 6. Dependency graph and next mathematical campaign

    source-indexed SUCC/FUCC factorization
       -> local Tate characters, Haar, Fourier, conductor and coset probe
       -> restricted Schwartz-Bruhat global test space and Poisson (imported)
       -> completion with Gamma, conductor, epsilon, pole/contact data
       -> correctly typed multiplicative convolution & prime-jet logarithmic derivative
       -> ORIGINAL signed completed Weil form W(f*f^sharp), for all admissible f
       -> Suzuki continuous screw / authentic compact signed G_a
       -> regularized 30-low / positive-high Schur and cross-range lambda->0
       -> all-a all-test positivity   [UNVERIFIED: RH-hard]

    alternate Connes branch: scaling/adelic trace
       -> identify exactly the SAME signed Weil distribution
       -> spectral/cohomological positivity or valid limit [UNVERIFIED]

The $\chi_3$ lane is a **transport control**, not a replacement for the zeta lane: conductor 3, odd Gamma, phase, and *no* zeta pole terms. Zeta's true lane needs its even arch Gamma, prime powers, two completed poles, contact distribution, half-density, and correct signs. Existing modules already contain portions of that source, but no fully justified all-test signed Weil positivity.

**Highest-value next steps:**

1. Implement Schwartz–Bruhat residue classes at arbitrary prime-power conductor $p^f$, prove Fourier/inversion matrices and local epsilon/phase with a declared convention, and test a second genuine twisted character with opposite parity. Treat wrong phases/conductors as failed source maps.
2. Write a typed *distribution-valued* morphism from the Tate test space to the actual signed completed Weil distribution. Compare it against the existing completed_weil_transport/source_weil_hierarchy output on exactly matching original-source test functions. Preserve gamma, poles/contact, and half-density; rule out all zero-lookup inputs.
3. For Suzuki $a=1/2$, use existing true 30-moment high bound to compute certified cross-resolvent Gram $R_\lambda$ with original source and prove/deny $\operatorname{Ran}(B^*)\subseteq\operatorname{Ran}(D^{1/2})$. A fixed shifted positive Schur is not enough; the $\lambda\downarrow0$ limit and then all $a$ are genuine obligations.
4. For Connes, verify the Fourier/Mellin half-density square under $u(x)=e^{x/2}f(e^x)$ and identify the trace distribution, not merely numerically similar spectra. The semilocal spectral limit is an independent unproved requirement.
5. Source-indexed Yoneda moonshot: represent conductor-resolution probes as morphisms, prove a source-faithfulness / separation criterion, and try to determine if the Weil/Suzuki transport loses character phase or allows an honest reconstruction. The present $\chi_3$ coarse/fine example is a rigorous small calibration instance.

## 7. Claim verdicts and test boundary

| ID | Verdict | Evidence | Remaining |
|---|---|---|---|
| T1 | CLASSICAL / PROVED LOCAL | exact shell proof; 210 rational holdouts | general complex characters |
| T2 | CLASSICAL / PROVED LOCAL | exact algebraic Gauss phase; coarse/fine obstruction | arbitrary conductor $p^f$ |
| T3 | CLASSICAL (Poisson imported) | residue theta/Mellin proof, independent Hurwitz evaluations | general adelic test space |
| T3b | PROVED LOCAL conditional on Poisson identity | all-height rational strip tail proof | machine rounding not certified |
| T4 | REFUTED shortcut / PROVED counterexample | exact symmetric polynomial and off-line zeros | mutant intentionally non-Euler |
| Zeta complete signed Weil → Suzuki/Connes all-test positivity | UNVERIFIED | existing partial source/Schur constructions | precise source-domain identification, all-a sign, zero-shift range |

Reproduce targeted: python -m unittest discover -s tests -p 'test_tate_local_contract.py'; python scripts/tate_local_contract_probe.py. Existing repository-wide gates remain required before integration. Exact code under observational_succ/tate_local_contract.py; test/probe separate from upstream source; no archived provenance is modified.

**Primary references (not SUCC novelty claims):** Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, 1950 (Cassels–Fröhlich, Chapter XV): https://old.maa.org/node/110814 ; Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, J. London Math. Soc. 108 (2023): https://doi.org/10.1112/jlms.12785 ; Suzuki, *Weil's quadratic form via the screw function* (2026): https://arxiv.org/abs/2606.09096 ; Connes–Consani–Moscovici, *Zeta Spectral Triples* (2025): https://arxiv.org/abs/2511.22755 ; Connes, *Trace formula on the adele class space and Weil positivity*: https://www.researchgate.net/publication/265411204_Trace_formula_on_the_Adele_Class_Space_and_Weil_Positivity .

**RH PROVED: NO.**


## 8. Tate-to-signed-Weil source profile bridge T5

The second implementation checkpoint, observational_succ/tate_weil_source_bridge.py, reuses the true prime-power tape from completed_weil_transport.py, rather than duplicating or replacing Suzuki's existing signed completed Weil operator. Immutable source profiles prevent replacing the zeta test by a ramified twist without explicitly changing conductor, Gamma parity, pole status and character coefficient. Both require half-density 1/2 and root number +1; the latter is the imported classical Gauss/Poisson fact.

For Re(s)>1, zeta with xi(s)=s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)/2 satisfies
\[
2\xi'/\xi(s)=2/s+2/(s-1)+\psi(s/2)-\log\pi
-2\sum_{p,k\ge1}(\log p)p^{-ks}.
\tag{T5-zeta}
\]
For primitive odd conductor-3 character, Lambda_chi(s)=(3/pi)^((s+1)/2) Gamma((s+1)/2)L(s,chi3):
\[
2\Lambda_\chi'/\Lambda_\chi(s)=
\log(3/\pi)+\psi((s+1)/2)
-2\sum_{p,k\ge1}(\log p)\chi_3(p)^k p^{-ks}.
\tag{T5-chi3}
\]
No completed pole terms appear for chi3 and its ramified p=3 Euler factor is absent. These are **absolutely convergent Euler-source identities on Re(s)>1**. The separate classical Poisson continuation must not be conflated with continuing the Euler series term by term.

For integer N>=3, including every genuine prime power n=p^k<=N, either source and every complex s with Re(s)=sigma>1 obey
\[
\left|2\frac{\Lambda'}{\Lambda}(s)-F_N(s)\right|
\le 2 N^{1-\sigma}\left(\frac{\log N}{\sigma-1}+
\frac{1}{(\sigma-1)^2}\right).
\tag{T5-tail}
\]
Proof: |chi3(p)^k|<=1, von Mangoldt Lambda(n)<=log(n) and the CW-03 decreasing-integrand tail majorant. The numerical output of the RHS is **not** a directed-rounding interval. Both profiles have independent complex holdouts against directly differentiated zeta/Hurwitz expressions. Wrong Gamma parity, completed poles, conductor, half-density and fake composite atoms are negative controls.

**T5 verdict:** CLASSICAL source identity / PROVED LOCAL typed wiring / TESTED numerical holdouts. This is a zero-independent logarithmic-derivative **germ** adapter, not a proven all-test Schwartz–Bruhat to signed Weil distribution map. It does not prove Suzuki all-interval positivity, the zero-shift resolvent range or the Connes spectral limit. RH PROVED: NO.
