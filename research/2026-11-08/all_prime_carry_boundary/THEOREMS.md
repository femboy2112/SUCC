# All-prime residue carry-boundary gluing — authenticated BBP

**2026-11-08 · Research-only additive child of SUCC draft #560, exact parent `f33705847afa9a4ff4fe6fdeb30f24754494345c`.** The original four signed BBP poles, **literal** `U_0=0`, source archive, provenance and main are frozen. π base-16 normality, its source-selected real Weyl decay and #544/#554 signed prime/complement lag gate remain **OPEN**. `PROVED PAPER` means the checkable derivations here plus the exact tests; not Lean certification or independent scholarly peer review.

## 0. Scope correction — which prime residues are actually at a carry boundary?

The previous prime-birth/scalar-phased observer concentrated on primes producing a new pole injection and on selected carry events. That misses the inherited prime-power residues of the **entire predecessor state**, even when the new source has no factor at that prime. The true carry is a **global integer winding** of *all* local additive characters. Two distinct finite-place types must not be conflated:

- **Odd p:** additive rational fractional parts `[U_n]_p in Q/Z`, **including full p^v precision** and their local carry windings. Their phases reconstruct `{U_n}` exactly via the classical additive product formula (inherited #558).
- **p=2:** every original source state is 2-adically integral, so its *additive fractional character* is zero, but `U_n mod 2^K` is a nontrivial **integral carrier residue**; its integer-lift seam must be retained separately (Main XXI #527/#528). A theorem about odd p characters cannot simply pretend this p=2 state is an additional independent fractional character.

At every source time n≥1, freeze

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_n=16U_(n−1)+r(n)`, `U_0=0`.

Put `C_n=floor(U_n)`, `x_n={U_n}`, `kappa_n=C_n−16C_(n−1)=floor(16x_(n−1)+r(n))`. `kappa` is the **literal rational-source carry**, not automatically the completed hexadecimal digit of π. For n≥2, `0<r(n)<1`, so `kappa_n in {0,...,16}`; source time n=1 has `r(1)=47/15` and `kappa_1=3`.

## PCB-01. Complete all-p local-winding identity (PROVED PAPER, exact)

Let `Q_n=lcm(den(U_(n−1)),den(r(n)))`, which is odd and contains **every** prime factor of the predecessor, injection, and successor denominators. For each `p^v || Q_n`, define exact rational coordinates:

`theta_(p,n−1)=[U_(n−1)]_p`, `rho_(p,n)=[r(n)]_p`, `theta_(p,n)=[U_n]_p` in `[0,1)`.

The additive group law in `Q_p/Z_p` yields

`theta_(p,n)=16 theta_(p,n−1)+rho_(p,n)−j_(p,n)`, with `j_(p,n)=floor(16 theta_(p,n−1)+rho_(p,n)) in Z_(>=0)`.

Define the **unreduced sum** `S_(n−1)=sum_p theta_(p,n−1)`, `S_n=sum_p theta_(p,n)`, their *global* windings `q_(n−1)=floor(S_(n−1))`, `q_n=floor(S_n)`, source fractional sum `R_n=sum_p rho_(p,n)`, source integer offset `m_n=r(n)−R_n in Z`, and local winding sum `J_n=sum_p j_(p,n)`. Then the **exact actual carry** obeys

\[
\boxed{\kappa_n=m_n+J_n+q_n-16q_{n-1}.}\tag{PCB1}
\]

**Proof.** Summing the local identities gives `S_n=16S_(n−1)+R_n−J_n`. Since `x_n=S_n−q_n` and `x_(n−1)=S_(n−1)−q_(n−1)` by the additive product/CRT formula, subtract to obtain `x_n−16x_(n−1)=R_n−J_n−q_n+16q_(n−1)`. The original real recurrence separately gives `x_n−16x_(n−1)=r(n)−kappa_n`; equality gives PCB1. This is valid for every exact rational seed/state whose denominators are in Q, not an assumption of independent primes or a normality theorem. **Dropping the global q terms is generally wrong.**

**Original source example n=2:** `U_1=47/15`, `r(2)=106/819`, `Q_2=4095=3²·5·7·13`. The full local rows are

| p^v | `[U1]_p` | `[r2]_p` | `[U2]_p` | `j_p` |
|---|---|---|---|---|
| 9 | 1/3 | 7/9 | 1/9 | 6 |
| 5 | 4/5 | **0** | 4/5 | **12** |
| 7 | 0 | 3/7 | 3/7 | 0 |
| 13 | 0 | 12/13 | 12/13 | 0 |

The scalar ledger is `m_2=−2`, `J_2=18`, `q_1=1`, `q_2=2`; hence `kappa_2=−2+18+2−16=2`. Omitting inherited p=5 incorrectly yields 5 for a natural fixed-other-coordinate counterfactual. Using p instead of p^v loses `7/9`, and `kappa mod16` would wrongly identify a valid 16 carry with zero.

**Predeclared 17..32 holdout:** each of the sixteen actual steps passed PCB1 against an independent integer-LCM recurrence and an independent direct four-fraction rational source. At n=32 there are **40 active odd-prime coordinates**, **34 inherited with zero forcing fraction**, `m=−3`, `J=310`, `q_n−16q_(n−1)=−303`, giving literal carry **4**. Complete row-by-row rational fractions and time indices mod p^v are in `ALL_PRIME_HOLDOUT_EXACT.json`; hashes and exact replay in `VALIDATION.md`.

## PCB-02. Full CRT carry boundary is a global arithmetic *cut* (PROVED PAPER)

For any common odd Q multiple of both source denominators, put `m_n=Q_n x_(n−1) in {0,...,Q_n−1}`, an integer. Every p^v local address `m_n mod p^v` is known from the authenticated rational predecessor. CRT recovers the *single* global m_n; individual local coordinates do not order it on the real line.

For any positive integer Q and rational driver r (the formula even works without `den(r)|Q`), the entire **carry-k boundary cell** is the half-open interval of integer addresses

\[
I_{Q,r,k}=[\ell_{Q,r,k},u_{Q,r,k})\cap\mathbb Z,
\quad\ell=\max(0,\min(Q,\lceil Q(k-r)/16\rceil)),\quad
u=\max(0,\min(Q,\lceil Q(k+1-r)/16\rceil)).\tag{PCB2}
\]

Then `floor(16m/Q+r)=k` iff `m in I_(Q,r,k)`. This is an exact rational inequality; all integer carries are represented, not just `k=1`. For the authentic n≥2 `k=0,...,16` (the top cell may be empty); n=1 has a different range because r(1)>1.

**A genuine mixed-prime boundary:** at n=2 hold the actual source forcing `r(2)` but allow all 15 possible predecessor phases `m/15` in the *predecessor's* genuine denominator 15. Give each such point its two CRT labels `m mod3`, `m mod5`. The 3×5 Boolean matrix of `1_{floor(16m/15+r(2))>=8}` has first three columns

\[
\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}
\]

whose determinant is **+1**. The full matrix therefore has rank **3**, not rank one: even the reference boundary observable cannot be represented by a single product of a 3-local decision and a 5-local decision. This is a **synthetic complete-fiber test** with actual source r2, not an assertion that 15 different zero-seeded BBP states occurred at time 1.

## PCB-03. Every complementary CRT residue can matter, even with no new pole (PROVED PAPER)

Suppose selected full prime powers multiply to `M|Q`, and the product of all **unselected** prime powers is `L=Q/M`. Fix the selected residue address `m≡c (mod M)`; its `L` complementary completions form `c+M t`, `0≤t<L`.

For `0≤r<1` and *every interior carry* `k=1,...,15`, the interval `I_(Q,r,k)` has length either `floor(Q/16)` or `ceil(Q/16)`. The elementary count of an arithmetic progression in a half-open interval gives

\[
\boxed{\left|\#\{0\le t<L:\kappa(c+Mt)=k\}-L/16\right|<1+1/M.}\tag{PCB3}
\]

In particular **if L≥17, every one of the 15 interior carry values occurs for every fixed selected prime address**. Endpoints k=0 and 16 need separate treatment because r shifts their lengths. The original n=2 `(Q,r)=(4095,106/819)` verifies this for selected `M=9` (L=455) and `M=45` (L=91), with exact enumeration. This is a theorem about the **uniform reference of all possible CRT completions**, not the distribution or independence of the single authentic zero-selected source path. It rigorously refutes any attempted inference that one or several prime-birth residues by themselves determine the actual carry when many complement coordinates remain.

## PCB-04. The complete carry-boundary Fourier tensor is signed and all-prime (PROVED finite algebra)

Write `B_(n,k)(m)=1_(m in I_(Q_n,r(n),k))`. For each `t mod Q_n` define its finite Fourier coefficient

\[
\widehat B_{n,k}(t)=\frac1{Q_n}\sum_{m=0}^{Q_n-1}B_{n,k}(m)e(-tm/Q_n),\qquad e(x)=\exp(2\pi i x).
\]

Since each I is consecutive, its t≠0 coefficient has the exact geometric form

\[
\widehat B_{n,k}(t)=\frac{e(-t\ell/Q_n)}{Q_n}\frac{1-e(-t|I|/Q_n)}{1-e(-t/Q_n)},\qquad
\widehat B_{n,k}(0)=|I|/Q_n.
\]

Orthogonality proves, for every integer h and actual BBP predecessor address m_n,

\[
\boxed{1_{\kappa_n=k}e(hU_{n-1})=\sum_{t\bmod Q_n}\widehat B_{n,k}(t)e((h+t)m_n/Q_n).}\tag{PCB4}
\]

Each character `e((h+t)m_n/Q_n)` is **exactly** the product of its authentic odd-prime additive characters. Source r(n) shapes the boundary tensor; actual U_(n−1) and its seeded chronology select one CRT point. The temporal Laplace transform of PCB4 is therefore an exact *signed* sum over **all** carry strata and **all** prime residues, not a product of independent p-local means. The usual nonnormal coherent counterseed still invalidates any seed-uniform mixing inference.

**Correct Haar centering:** the full CRT reference mode is `\widehat B_(n,k)(−h)`, not generally zero. For fixed h and k in 0..15 with r(n)→0 and Q_n→∞, it tends to `\int_{k/16}^{(k+1)/16} e(hx)dx`, which need NOT vanish even under a truly uniform distribution. Thus uncentered per-carry cancellation is the wrong demand. Define the selected, source-authenticated discrepancy

\[
D_{A,k}(h)=\frac1A\sum_{n=A}^{2A-1}\left[1_{\kappa_n=k}e(hU_{n-1})-\widehat B_{n,k}(-h)\right].\tag{PCB5}
\]

For fixed h≠0, summing **all** k=0..16 gives `W_A^{prev}(h)` up to the reference `A^-1 Σ_n 1_(Q_n|h)`, eventually zero since the original denominator grows (Main XXI PF7/#532). Therefore **a theorem that D_(A,k)(h)→0 for every fixed nonzero h and every k would prove base-16 normality**; conversely original normality gives these centered limits (weak convergence, shrinking source shifts, boundary arcs). This is an **equivalent reformulation with the full signed all-prime boundary operator**, not a proof of the still-OPEN premise. It preserves original zero selection and provides the correct next arithmetic target.

## PCB-05. Analytic completion adds a second, explicitly measurable boundary (PROVED algebra + finite source certificates)

The exact original future Green field satisfies `U_n+T_n=16^(n−1)π` and `16 T_(n−1)=r(n)+T_n`. The **actual completed hexadecimal digit** read at step n, including n=1's integer digit, obeys

\[
\boxed{d_n=(\kappa_n+\delta_n)\bmod16,\qquad\delta_n=\left\lfloor\{16x_{n-1}+r(n)\}+T_n\right\rfloor\in\{0,1\}.}\tag{PCB6}
\]

The source-tail correction is zero unless the full odd-prime residue configuration places the state within `T_n` of the outgoing real carry boundary. Using the canonical exact-rational `duck_bbp.tail_interval`, the **first 32 steps**, including the held-out n=17..32, give certified digit readings and `delta=0`. These **finite certificates do not establish zero hotspot density or even eventual absence of hotspots**. Separate exact synthetic input controls yield delta=1 and a correct 15→0 wrap; an unresolved interval fails closed.

## PCB-06. Keep the integral 2-adic carrier (PROVED algebra, no real-Haar inference)

All original U_n and r(n) have odd denominators, hence lie in Z_2. For each K≥5 calculate exactly `V_(n,K)=U_n mod 2^K` via denominator inversion, and `X_(n,K)=x_n mod 2^K`. The lifted integer coordinate is `C_(n,K)=V_(n,K)−X_(n,K) (mod 2^K)`. Then

\[
\boxed{\kappa_n\equiv C_{n,K}-16C_{n-1,K}\pmod{2^K}.}\tag{PCB7}
\]

Since the authentic n≥2 literal carry lies in 0..16 and `2^K>16`, its residue uniquely recovers that literal integer. Every one of the first 32 source transitions was independently checked at K=8 and the synthetic carry16 at K=5. **The fractional additive p=2 character is zero but the integral 2-adic coordinate is not.** This is the mandatory cross-place seam; it is not a 2-adic-to-real Haar transfer.

## Proof status, controls and exact next problem

- **PROVED PAPER:** PCB1–4 finite identities and CRT-fiber count; PCB6/7 analytic completion/carry algebra, relying on inherited exact Green identity; authentic source specializations and exact rational oracles.
- **CERTIFIED FINITE:** source time 17..32 complete local fractions, all source/prime-power labels, integer carries and 32 digit enclosures; exact JSON replay and independent LCM/carrier oracle.
- **REFUTED UNIVERSAL shortcuts:** use only primes at pole births, identify a full CRT boundary with a product of independent local carry decisions, drop q winding, truncate prime powers to p, reduce carry16 to0, treat exact source carry as automatically π digit.
- **UNVERIFIED / OPEN:** any all-A bound on PCB5, source-selected #554 signed lag covariance, original selected Weyl decay, base-16 normality of π. The uniform-completion reference is **not** the empirical source distribution. The full conductor may be astronomically large and exact Fourier expansion does not reduce complexity by itself.

**Next verdict-changing probe:** test the centered signed boundary-current PCB5 against original-zero source and all-prime residues (including old cofactor and integral p=2), with independent prime-subset ablations and source-holdout epochs; seek a source-driven Fourier/Laplace cancellation estimate on its complete **joint** tensor, not separate marginal cancellation.
