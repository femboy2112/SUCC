# Operation Mirror SUCC — reciprocals, harmonic Pascal, critical Fejér mixtures and the fixed BBP carrier

**Date:** 2026-10-24. **Research-only.** Base: draft PR #283 at `fd22dc3341145f5a5e9e6d7a7ecb06daae1cb43c`, inheriting the exact natural-number BBP carrier #281 and fixed-source #277/#272. No main merge; earlier reciprocal SUCC/FUCC/Pascal work (2026-10-22) and CYC-03/NLG-06 are explicitly acknowledged. **π normality: OPEN.** No new Lean authority; scholarly novelty UNVERIFIED. Classical harmonic and Fejér facts are attributed, the arithmetic error uses authentic original BBP forcing.

## 1. Steelman, object and the actual correction

The intuition that harmonic numbers are "natural successor in the reciprocal mirror" is close but needs one extra state: the **reciprocal orbit** is the mirror SUCC; **harmonic numbers are its accumulated increments**. Let `S(n)=n+1` on integers n>=1, and `rho(n)=1/n`. On the reciprocal image,

$$
T=\rho S\rho^{-1},\qquad T(x)={x\over1+x},\qquad T^k(x)={x\over1+kx}.
$$

This is exactly the projective action on positive fractions `x=a/b` of the unipotent integer shear

$$
J=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
J^k=\begin{pmatrix}1&0\\k&1\end{pmatrix},\qquad (a,b)\mapsto(a,b+ka).
$$

**The same numeric matrix J** is the single-binary-digit Boolean zeta/Lucas incidence operator inherited from PR #274. Its representations are **distinct**: projective action on positive rationals versus linear action on digit-state functions. This is an actual common-basis unipotent generator, not a claim that source digits have been identified with rational fractions.

The additive cocycle over the mirror transition is `(x,h)->(x/(1+x),h+x/(1+x))` if `h` initially denotes the already-accumulated sum through n. Starting at `(x,h)=(1,1)` produces `(1/n,H_n)` at n after n-1 successor steps. The exact classical alternate Pascal expression is

$$
H_n=\sum_{j=1}^n{1\over j}
=\sum_{j=1}^n(-1)^{j-1}{n\choose j}{1\over j}.
$$

Proof: integrate `(1-(1-t)^n)/t` from 0 to 1, expand by the binomial theorem, and compare to `sum_{j=0}^{n-1}(1-t)^j`. Moreover,

$$
\Delta^k H_n={(-1)^{k-1}(k-1)!\over(n+1)(n+2)\cdots(n+k)},\quad k\ge1,
$$

because `Delta H_n=1/(n+1)` and `Delta^j[1/(n+a)]=(-1)^j j!/prod_{v=0}^{j}(n+a+v)`. Pascal finite differences and reciprocal rays are therefore exactly linked. **These are classical identities, not scholarly-original results.**

## 2. A mirror SUCC/FUCC transport for prime multiplication

For integers `m>=2` and `n>=1`, the harmonic difference is the right-endpoint Riemann sum for the integral defining log m:

$$
H_{mn}-H_n=\sum_{j=n+1}^{mn}{1\over j}
<\int_n^{mn}{dt\over t}=\log m.
$$

The convexity of `1/t` makes the per-cell trapezoidal upper bound strict. Telescoping the trapezoid surplus gives the all-parameter **rational** bracket

$$
\boxed{0<\log m-(H_{mn}-H_n)<{m-1\over2mn}.}
$$

Thus `H_{pn}-H_n -> log p`, and nested multipliers p and q commute in their *exact* harmonic difference cocycle, with an explicit `O(1/n)` defect from additive log transport. Prime clock ordering is not required. This supplements, but does not supersede, `reciprocal_succ_fucc.py`'s distinct operator-adjoint and residue-clock theorems: their reciprocal and our projective reciprocal have different types.

## 3. The original BBP source literally is four mirror rays

Do **not** change the coefficients or the anchored zero. On n>=1 set

$$
x_c(n)={1\over8n-c},\quad c\in\{7,4,3,2\},\quad
x_c(n+1)={x_c(n)\over1+8x_c(n)}=J^8\cdot x_c(n).
$$

The genuine authenticated forcing is precisely

$$
\boxed{r(n)=4x_7(n)-2x_4(n)-x_3(n)-x_2(n).}
$$

Define signed offset moments `M_j=4*7^j-2*4^j-3^j-2^j`. Then `M_0=0`, `M_1=15`, `M_2=151`, `M_3=1209`. Expanding `(8n-c)^{-1}` for `n>=1` gives an absolutely convergent inverse-n expansion (since c/(8n)<1):

$$
r(n)=\sum_{j\ge1}{M_j\over8^{j+1}n^{j+1}}
={15\over64n^2}+{151\over512n^3}+\cdots.
$$

This is the same **classical authenticated four-pole** cancellation already studied in SUCC's source-memory/Pascal dossiers, now equipped with a rigorously declared projective J^8 action. The signed four-ray moment also has the established positive integral representation:

$$
r(n)=\int_0^1t^{8(n-1)}\underbrace{(4-2t^3-t^4-t^5)}_{g(t)>0\ (0\le t<1)}dt.
$$

It is *not* legitimate to apply projective J^8 to the complex poles as if they were points on the base-16 circle: that was the earlier source-typing bug repaired by PR #252. The J^8 action here is only on the positive rational reciprocal index rays.

### Hostile source: mirror SUCC + same asymptotic does not imply normality

Put `T_n^*=1/[64(n+1)(n+2)]` for n>=0, `alpha*=T_0*=1/128`, and `r*(n)=16T*_(n-1)-T*_n` for n>=1. Then

$$
r^*(n)={1\over64}\left({16\over n}-{17\over n+1}+{1\over n+2}\right)>0,\quad
r^*(n)\sim {15\over64n^2}.
$$

The anchored natural-source recurrence has **exact** solution

$$
U_0^*=0,\quad U_n^*=16^n/128-T_n^*,\quad U_n^*=16U^*_{n-1}+r^*(n).
$$

For all n>=2 the full base-16 phase `{16^n alpha*}` is zero, hence `alpha*=1/128` is manifestly NOT base-16 normal. This is a positive rational *different forcing* with mirror SUCC rays, the same leading coefficient and a bounded future tail. It does **not** retain the four exact BBP pole positions or the full dyadic profile, and does not refute any claim about pi. It decisively refutes the *generic* leap from mirror/rate structure alone to normality.

## 4. Valid harmonic correlation operator: positive mixtures, NOT signed 1/k shortcuts

Let z_1,...,z_N be complex, let k range over lags, and zero-extend z outside its observed natural-number window. For 1<=L<=K<=N set

$$
B_L={1\over NL^2}\sum_{t=2-L}^{N}\left|\sum_{j=0}^{L-1}z_{t+j}\right|^2\ge0,\quad
q_L={1\over L H_K},\quad H_K=\sum_{L=1}^K1/L,\quad
E_K=\sum_{L=1}^Kq_LB_L.
$$

Let `C_k=sum_(n=1)^(N-k)z_(n+k)conj(z_n)`; for modulus-one z the exact expansion is

$$
\boxed{E_K=d_K+{2\over N}\sum_{k=1}^{K-1}w_{K,k}\mathrm{Re}C_k,}
$$

$$
d_K={H_K^{(2)}\over H_K},\quad
w_{K,k}={1\over H_K}\sum_{L=k+1}^K{L-k\over L^3}.
$$

The associated symbol is a positive trigonometric polynomial for **every** K:

$$
\boxed{d_K+2\sum_{k=1}^{K-1}w_{K,k}\cos(k\theta)
={1\over H_K}\sum_{L=1}^K{1\over L^3}
\left|\sum_{j=0}^{L-1}e^{ij\theta}\right|^2\ge0.}
$$

This follows from an **explicit finite sum of Hermitian squares**, not an appeal to physical/semantic positivity. In contrast, the tempting naive lag symbol `1+2 sum_(1<=k<K) (1-k/K) cos(k theta)/k` is **negative at theta=pi for K=4**: `-1/6`. It cannot be treated as a positive-definite van der Corput averaging kernel. This negative receipt is retained.

Cauchy–Schwarz on each collection of overlapping L-blocks (whose total sum is L times the original source sum) gives the **unconditional exact finite inequality**

$$
\boxed{\left|{1\over N}\sum_{n=1}^Nz_n\right|^2
\le\left(1+{K-1\over N}\right) E_K.}
$$

No stochastic independence, Haar approximation or BBP hypothesis occurs here.

### Critical exponent and competing objectives

For the general declared inverse-power mixture `q_L^(beta)=L^(-beta)/Z_beta(K)`, `Z_beta=sum_(L<=K)L^(-beta)`, the diagonal is `d_beta=Z_(beta+1)/Z_beta`. It tends to zero **iff beta<=1** when beta>=0. At beta=1, `d~zeta(2)/log K`; for beta>1, `d->zeta(beta+1)/zeta(beta)>0`. Thus beta=1 is a *critical admissible endpoint* within this **specific positive inverse-power family**, not a universal optimizing weight. The last-lag weight relative to ordinary length-K Fejér is exactly

$$
{w_{K,K-1}\over 1/K^2}={1\over K H_K}.
$$

The diagonal pays a much slower `1/log K` cost than the ordinary Fejér `1/K`. Moreover, **the convex mixed energy E_K cannot be smaller than the minimum individual B_L** computed on exactly the same input: the new kernel is a valid changed diagnostic, not an independently created cancellation source. A nonnormal constant phase yields `|average|=1` and all positive block energies near one; mere positivity can never eliminate it.

## 5. The source-specific harmonic vdC bridge and sharpened lag horizon

Now use only the **authentic anchored** SUCC BBP source of PR #281/283. Let h be a fixed nonzero integer, `z_n=e(hU_n)`, and set

$$
C_{k,N}(h)=\sum_{n=1}^{N-k}e(h(U_{n+k}-U_n)),\quad
W_{k,N}(h)=\sum_{n=1}^{N-k}e(h(16^k-1)U_n).
$$

The source-specific NLG-01--04 bound gives, using pi<22/7 and `sum_(n>=1)1/n^2<2`,

$$
|C_{k,N}(h)-W_{k,N}(h)|
\le {11|h|\over56}16^k.
$$

The mixing weights pay the growing lag *on the same natural-source time axis*. Reordering **finite nonnegative sums** yields

$$
\begin{aligned}
\sum_{k=1}^{K-1}16^k w_{K,k}
&={1\over H_K}\sum_{L=2}^K{16^L\over L^3}
\sum_{j=1}^{L-1}{j\over16^j}\\
&\le{16\over225H_K}\sum_{L=2}^K{16^L\over L^3}
\le{32\over225}\,{16^K\over H_K K^3}.
\end{aligned}
$$

Here `sum_(j>=1)j/16^j=16/225`, and `16^L/L^3` increases by at least a factor 2 as L increases from 2 onward. Therefore the **entire** weighted authentic source error obeys

$$
\boxed{{2\over N}\sum_{k=1}^{K-1}w_{K,k}|C_{k,N}(h)-W_{k,N}(h)|
\le{88|h|\over1575}\,{16^K\over N H_K K^3}.}
$$

Together with positive vdC this proves the explicit **conditional** bound

$$
\boxed{\left|S_N(h)/N\right|^2\le
\left(1+{K-1\over N}\right)
\left[{H_K^{(2)}\over H_K}+{2\over N}
\sum_{k=1}^{K-1}w_{K,k}|W_{k,N}(h)|
+{88|h|\over1575}{16^K\over N H_K K^3}\right].}
\tag{HM-vdC}
$$

The right side is NOT known to go to zero: the selected frequencies `h(16^k-1)` have not acquired a new arithmetic cancellation estimate. This result changes the admissible distribution of source-error budgets, **not the arithmetic content of W**.

### A fully explicit longer cutoff, without floating logarithms

For N>=256 put `b_N=floor(log_16 N)` and

$$
K_N=b_N+3\lfloor\log_{16}b_N\rfloor.
$$

For sufficiently large N, `K_N<=N`, `K_N->infinity`, `K_N/N->0`, and

$$
16^{K_N}\le N b_N^3\le N K_N^3.
$$

Hence `16^K/(N H_K K^3) <=1/H_K ->0`, while diagonal `H_K^(2)/H_K ->0`. **Proved conditional criterion:** if for every fixed integer h!=0

$$
\boxed{{1\over N}\sum_{k=1}^{K_N-1}w_{K_N,k}|W_{k,N}(h)|\to0,}
\tag{HM-open}
$$

then `S_N(h)/N->0` for every fixed h and, by classical Weyl plus the already-proved BBP positive-tail transport, **π is normal in base 16** (therefore also bases 2 and 4). 

Compared with #283's deliberately conservative `K~(1/2)log_16 N`, this supplies a legitimately admissible `K~log_16 N+3log_16(log_16 N)` **forcing-error** schedule. A pure fixed length-K Fejér kernel has high-lag forcing budget `O_h(16^K/(N K^2))`, whereas the critical harmonic mixture has `O_h(16^K/(N K^3 H_K))`. This is a stronger deterministic error *budget*, not proof that the harmonic estimate (HM-open) is easier or stronger than a different Fejér-window strategy. The convex mixture may in fact be worse than an optimally selected fixed block length for a given source sequence.

## 6. Steelman / crucible / verdict

| Proposal | Exact discriminator / receipt | Status |
|---|---|---|
| Reciprocal SUCC uses the same unipotent J as one-bit Pascal | direct 2x2 integer generator, projective transport; explicit distinct types | PROVED PAPER / CLASSICAL |
| H_n itself is just reciprocal n | H_n has separate summation/cocycle state; n=2: H_2=3/2 but 1/2 | REFUTED literal identity, repaired |
| Prime multiplication is harmonic translation | exact bracket less than (p-1)/(2pn), goes to log p | CLASSICAL / PAPER |
| Authentic four-pole BBP belongs to mirror J^8 rays | all exact original coefficients and m0,m1,m2 recovered | PROVED PAPER, mathematical novelty UNVERIFIED |
| Mirror rays, positive O(n^-2) forcing, anchored N source guarantee normality | explicit rational alpha*=1/128 counterfeit with eventual radix-zero orbit | REFUTED generic shortcut |
| Naive 1/k lag weights define a positive Gram | exact K=4, theta=pi value -1/6 | REFUTED |
| Correct critical harmonic Fejér mixture is positive | explicit sum of squared modulus of Dirichlet polynomials | PROVED PAPER, EXACT FINITE |
| Harmonic weights improve source error cost at largest k | exact tail bound 88/1575 times 16^K/(N H_K K^3) | PROVED PAPER, not a selected Fourier bound |
| More all-source observations automatically force π mixing | counterfeit/constant controls and previous NLG held-out ablations | REFUTED generic implication |
| Authenticated harmonic cyclotomic mean tends to zero | the source-selected mixed signed sum (HM-open) is not estimated | UNVERIFIED / OPEN |

## 7. Provenance, reproducibility and next verdict-changing probe

- **Ancestors:** #281 N-carrier exact BBP automaton, #283 original four-pole real lag estimate and unconditional vdC, #274 Pascal/Lucas one-bit `J`, #277 synchronized source, older [reciprocal SUCC/FUCC mirror bridge](../2026-10-22/SUCC_FUCC_RECIPROCAL_PASCAL_BRIDGE.md), #252 signed-source repair. No archived original or inherited theorem changed.
- **Classical references:** harmonic/Pascal identity and partial harmonic sums in Necdet Batir, *On some combinatorial identities and harmonic sums*, arXiv:1703.06401; harmonic asymptotics/digamma in [MathWorld's Harmonic Number](https://mathworld.wolfram.com/HarmonicNumber.html); Fejér kernels/finite vdC by standard finite Fourier/Cauchy-Schwarz (direct proof above). Classical references are attribution, not sources of novel normality proof.
- **Controls:** [`harmonic_mirror_succ.py`](../../observational_succ/harmonic_mirror_succ.py), [`pi_harmonic_lag.py`](../../observational_succ/pi_harmonic_lag.py), exact tests and independent probe. **All claim status and root causes are limited to the stated finite/classical domains.**
- **Next decisive arithmetic probe:** construct an authenticated original four-pole **signed harmonic-lag sum** for `K_N~logN+3loglogN` and prove an upper bound strictly smaller than the difference from the diagonal. Start with frozen BBP prime windows and the same `h` and full integral carry; avoid independent p-Haar models. Try Abel/summation-by-parts directly on the mirror rays coupled to the cyclotomic characters. Predeclare the exact target `sum w_k |W| / N=o(1)` (or genuinely stronger signed Gram cancellation), then test against a periodic α*=1/128 mirror counterfeit. If a proof uses only abstract positivity/mirror J, the counterfeit kills it. If it uses the *full original four-pole moment spectrum* to prove a signed estimate, subject it to a fresh independent derivation and large-prime holdout. **No finite receipt proves π normality.**
