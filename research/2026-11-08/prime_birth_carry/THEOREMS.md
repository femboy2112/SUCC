# Prime-birth boundary spectroscopy: three-channel carry junction and real complementary slip

**Research dossier — 2026-11-08.** Strict additive child of SUCC draft #554 at `90711d2e9dc73020acbc4cde1ad058b62ef54a4d` (itself based on #552); precursor #497 original prime-Frobenius pulses; #544 signed prime/complement and retrodictive carry; #520/#521 source/real carry transports. **π base-16 normality: OPEN.** This does not promote a new signed cancellation theorem, a proof of an iid digit law, or priority over classical Fourier/continued-fraction facts. Paper derivations are not external peer review or Lean proof.

## 0. Types, origin, and the necessary distinction

The literal original four-pole source, not a four-dimensional model replacement, is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

There is an **exact positive three-channel difference**
\[
r(n)=\sum_{d\in\{3,4,5\}} r_d(n),\quad
r_d(n)=\frac{w_d d}{a_n(a_n+d)},\quad a_n=8n-7,\quad
(w_3,w_4,w_5)=(2,1,1).
\]
Let `V_(d,0)=0`, `V_(d,n)=16V_(d,n-1)+r_d(n)`; then `U_n=sum_d V_(d,n)`. These are rational identities, all n. They are not independent random channels.

Fix a genuine odd prime `p>5` with `p≡1 mod8`, `p²>16A`, and all source times in a first simple-pole prime shell. Write `[q]_p` for the unique residue in `{0,...,p-1}` of a p-integral rational q, **not the reduction of an arbitrary real number**. Define
\[
c_{d,n}=[pV_{d,n}]_p,\quad j_{d,n}=[pr_d(n)]_p,\quad
c_n=[pU_n]_p,\quad j_n=[pr(n)]_p.
\]
We will always distinguish the **local prime carry** `z_n` from the **real literal carry** `κ_n` and from the completed hexadecimal digit of π. The latter two are not automatically equal.

## PBC-01. Exact twin-clock carry conservation (PROVED ALGEBRAIC)

With `x_n={U_n}∈[0,1)` and `κ_n=floor(16x_(n-1)+r(n))`, define
\[
z_n=\left\lfloor\frac{16c_{n-1}+j_n}{p}\right\rfloor,
\qquad c_n=16c_{n-1}+j_n-pz_n.
\]
Both are actual deterministic arithmetic operations. For every event in the simple-pole range the scalar `p`-residue recurrence follows by multiplying the four-pole recurrence by p. Choose the **real signed cofactor chart** (not mod1)
\[
b_n=x_n-c_n/p\in(-1,1).
\]
Subtract the real and prime recurrences. **Exactly**
\[
\boxed{b_n-16b_{n-1}=r(n)-j_n/p-(\kappa_n-z_n).}\tag{PBC-1}
\]
At a source-pole birth the injection `j_n/p` may be order one (even though `r(n)=O(n^-2)`); the complementary chart and the integer carry slip compensate it. **Prime birth is not a theorem that the real carry jumps**. The real effect is carried by `b_n` and `κ_n−z_n`, not by p-character magnitude alone.

Let `a≤b` be consecutive source steps. Multiply PBC-1 by `16^-n` and telescope:
\[
\boxed{
\sum_{n=a}^b16^{-n}(\kappa_n-z_n)
=16^{-(a-1)}b_{a-1}-16^{-b}b_b
+\sum_{n=a}^b16^{-n}\bigl(r(n)-j_n/p\bigr).
}\tag{PBC-2}
\]
This **source-aware** boundary formula includes all original real forcing. It does not bound unweighted signed Fourier sums; replacing `16^-n` with uniform weights destroys the special telescoping.

## PBC-02. Three-channel junction and a true radix coboundary (PROVED ALGEBRAIC)

For each source channel set
\[
z_{d,n}=\lfloor(16c_{d,n-1}+j_{d,n})/p\rfloor,\qquad
\tau_n=\left\lfloor\frac{c_{3,n}+c_{4,n}+c_{5,n}}p\right\rfloor\in\{0,1,2\}.
\]
Define the injection wrap
`β_n=(sum_d j_(d,n)−j_n)/p`, an integer. Adding the three channel recurrences **before** taking the scalar residue gives the all-time identity
\[
\boxed{z_n=\sum_d z_{d,n}+\tau_n-16\tau_{n-1}-\beta_n.}\tag{PBC-3}
\]
On every complete first shell `p≡1 mod8` the four source event types are an initial simultaneous positive injection `(2,1,1)` with total 4, and then single-channel injections `−1/2`, `−1/5`, `−1/6` modulo p. Therefore `β_n=0` at every step of that shell, including all four balanced stages. Thus
\[
\boxed{z_n=\sum_d z_{d,n}+\tau_n-16\tau_{n-1}}.\tag{PBC-4}
\]
Modulo 16, or for any hexadecimal integer character, the preceding `−16τ_(n-1)` disappears:
\[
\boxed{e^{2\pi ihz_n/16}=\prod_d e^{2\pi ihz_{d,n}/16}\;e^{2\pi ih\tau_n/16}.}\tag{PBC-5}
\]
The three channels are **not independent**. The marked three-channel interaction lives in the finite junction register `τ`. Combining with the real carry slip `s_n=κ_n−z_n` gives
\[
e^{2\pi ih\kappa_n/16}
=\left(\prod_d e^{2\pi ihz_{d,n}/16}\right)
 e^{2\pi ih\tau_n/16}e^{2\pi ih s_n/16}.
\tag{PBC-6}
\]
This is a genuine source/prime/real phase factorization, but as an identity it supplies **no independent signed-decay estimate**.

The weighted junction defect is a *pure boundary*:
\[
\boxed{\sum_{n=a}^b16^{-n}\Big(z_n-\sum_d z_{d,n}\Big)
=16^{-b}\tau_b-16^{-(a-1)}\tau_{a-1}.}\tag{PBC-7}
\]
It is the user's proposed arithmetic coalescence in an explicitly declared radix-normalized basis. At an **unweighted temporal Fourier** character `z=e^{iθ}`, however, the Z-transform of the junction defect is multiplied by `(1−16z)`, with `|1−16e^{iθ}|≥15`. The filter has **no unit-circle zero**. Therefore the cancellation at the nonunitary normalization `z=1/16` does not give zero temporal Fourier power or normality. This is a calibrated no-go, not a dismissal of the boundary representation.

## PBC-03. Exact prime spectral emission at four source boundaries (PROVED / inherited scalar source passport)

Let `p=8k+1`. The four original first-shell prime births occur at
\[
\boxed{t_1=k+1,\quad t_2=4k+1,\quad t_3=5k+1,\quad t_4=6k+1.}\tag{PBC-8}
\]
The normalized three-channel p-state vectors on the four stages, already proved in #554, are
\[
 v_1=(2,1,1),\quad v_2=(3/2,1,1),\quad
 v_3=(3/2,4/5,1),\quad v_4=(3/2,4/5,5/6).
\]
Their scalar sums are `4, 7/2, 33/10, 47/15`; all are nonzero modulo every `p≡1 mod8`, `p>5`. With `D_s=(1,2,10,30)` and
\[
 A_s=D_s v_s=(2,1,1),(3,2,2),(15,8,10),(45,24,25),
\]
we have throughout stage s, at every authentic integer source time,
\[
\boxed{c_{d,n}\equiv A_{s,d} q_{s,n}\pmod p,\qquad
q_{s,n}\equiv D_s^{-1}16^{n-t_1}\pmod p.}\tag{PBC-9}
\]
Thus `τ_n = floor(sum_d {A_(s,d) q_(s,n)/p})`: each stage has a finite integer winding map of **one shared prime clock**, not three independent phases.

For #554's balanced selector `p_A/A→12/5`, the three **in-epoch** emission times `t_2,t_3,t_4` divide `[A,2A)` into stage proportions `(1/5,3/10,3/10,1/5)`. Their nonzero source injections are exactly
`j_(t2)=−1/2 modp`, `j_(t3)=−1/5 modp`, `j_(t4)=−1/6 modp`. They can have macroscopic size in the representation `j/p` while `r(t)=O(A^-2)`: PBC-1 identifies the compulsory cofactor compensation.

## PBC-04. Four exact rational junction spectral laws (PROVED FINITE FORMULA + inherited asymptotic)

For any positive integer triple `a=(a1,a2,a3)` define the *geometric junction* on x∈[0,1):
\[
\tau_a(x)=\big\lfloor\{a_1x\}+\{a_2x\}+\{a_3x\}\big\rfloor\in\{0,1,2\}.
\]
Its probability under Lebesgue x has exact rational values; no statistical fit is used. Let `L=lcm(a1,a2,a3)`, `S=a1+a2+a3`, and `Q_j=sum_i floor(a_i j/L)`. Since no fractional-part breakpoint occurs in `(j/L,(j+1)/L)`, the first probability is **the finite explicit formula**
\[
\boxed{P_a(\tau=0)=\sum_{j=0}^{L-1}
 \left[\min\left(\frac{j+1}L,\frac{Q_j+1}S\right)-\frac jL\right]_+.}\tag{PBC-10}
\]
Reflection x↦1−x sends the sum of three nonzero fractional parts to 3 minus itself, almost everywhere. Hence `P_a(τ=2)=P_a(τ=0)`, `P_a(τ=1)=1−2P_a(τ=0)`.

Substitute the **actual** four source triples `A_s` above:

| Stage `s` | `A_s` | `P(τ=0)` | `P(τ=1)` | `P(τ=2)` | parity spectral line `E[(-1)^τ]` |
|---|---|---:|---:|---:|---:|
| 1 | (2,1,1) | 1/4 | 1/2 | 1/4 | 0 |
| 2 | (3,2,2) | 11/42 | 10/21 | 11/42 | +1/21 |
| 3 | (15,8,10) | 11/60 | 19/30 | 11/60 | −4/15 |
| 4 | (45,24,25) | 159/940 | 311/470 | 159/940 | −76/235 |

The finite formula uses L=2,6,120,1800, respectively, and all entries were independently checked with a second rational breakpoint subdivision. These are exact **source-side** rational geometries. The **asymptotic** empirical stage law follows from BEC-04's incomplete-character estimate and the prime selector of BEC-03: the normalized clock `q_(s,n)/p` equidistributes in [0,1), and the junction map has only finitely many rational discontinuities, so Weyl's Riemann-integrability criterion applies. No independence assumption is invoked.

Weight by the authentic balanced stage proportions to get the limiting whole-epoch junction law
\[
\boxed{P_\infty(\tau=0,1,2)=\left(\frac{2861}{13160},\frac{3719}{6580},\frac{2861}{13160}\right).}\tag{PBC-11}
\]
The signed parity line changes sign **at source-stage transitions**, a literal arithmetic spectral fingerprint. It does not assert that the real BBP carry has this law. Different sources can share a first-order Gamma endpoint and differ in the higher pole-birth fingerprint.

## PBC-05. Quantitative prime-local carry words on the logarithmic aperture (COROLLARY OF #554 / classical inputs)

Let `J=[A,2A)` and choose #554's balanced prime selector `p_A`, `m=ord_p(16)`. At each original source time n∈J form the p-clock digit `z_n`, retaining the three original p-birth injections. For depth `d≥1`, form *all A forward starting words* `(z_n mod16,...,z_(n+d-1) mod16)` (including at most d−1 lookahead observations after 2A−1, within the first simple-pole shell). Assume the small lookahead stays within that shell and `3d<A`.

Except at **at most 3d** starts whose forward word meets a p-birth, `j_(n+i)=0`. Then the word consists of the first d base-16 digits of `c_(n-1)/p` under `x↦{16x}`. For each fixed word `w`, the qualifying p residues are an interval of consecutive integers of length `p/16^d+O(1)`. The finite discrete Fourier coefficients of this interval satisfy
\[
\sum_{h=1}^{p-1}|\widehat{1_I}(h)|\le1+\log p
\]
(using a geometric sum and `|sin(πh/p)|≥2min(h,p−h)/p`). BEC-04's source-exact incomplete-period estimate, with complete subgroup error `δ_p`, gives for every word simultaneously
\[
\boxed{\left|\Pr_J(w)-16^{-d}\right|\le
\frac1p+(1+\log p)
\left(\delta_p+\frac{4\sqrt p(2+\log m)}A\right)+\frac{8d}A=:\varepsilon_{A,d}.}\tag{PBC-12}
\]
The 8d/A term conservatively pays the birth-crossing windows and boundary-normalization costs. The total-variation distance to uniform on `16^d` words is at most `min(1,16^d ε_(A,d)/2)`.

Under BEC-03's imported fixed-modulus PNT/AP and Cochrane–Pinner bound `δ_p=O(p^-1/16(log p)^(3/4))`, the prime-local word law converges to uniform in total variation at the **SUCC normality aperture**
\[
\boxed{d_A=\max(1,\lfloor\log_{16}\log A\rfloor),\quad
\mathrm{TV}(\mathrm{prime\ carry\ words},\mathrm{Unif}_{16^{d_A}})\to0.}\tag{PBC-13}
\]
This is a useful **explicit bridge from the existing prime-clock character theorem to its radix carry process**, not a new proof of the original zero-seeded digit statistics. It extends #544's already-known local prime digit/history Haar statements into this three-channel carry and stage-birth register. The **Lambert-W observer depth** `~log_16 A−log_16 log A` is much larger than the depth where this imported bound gives a relative TV estimate; using the W depth here would silently overspend the Fourier error budget.

## PBC-06. The exact signed slip-gate and an explicit false-positivity control (PROVED REDUCTION / OPEN SOURCE PREMISE)

For a nonzero integer h mod16 set `a_n=e^(2πi h z_n/16)`, `b_n^slip=e^(2πi h(κ_n−z_n)/16)` (unit modulus). Then
\[
\boxed{\frac1A\sum_{n=A}^{2A-1}e^{2\pi ih\kappa_n/16}
=\operatorname{Cov}_J(a,b^{slip})+(\mathbb E_Ja)(\mathbb E_J b^{slip}).}\tag{PBC-14}
\]
The prime marginal tends to zero by PBC-13. Therefore the **new open item** is the original-zero signed cofactor-slip covariance, not the prime marginal. For every fixed word depth and all nonzero word characters, the analogous block-covariance decay is equivalent to the full real carry-word Haar law. With the inherited #520 AC1/AC2 and #521 Green transport (and the separately paid exceptional literal carry16), that is equivalent to the original zero-selected base-16 normality gate. **This is an equivalent reformulation, not a proved saving.**

The reduction has an exact hostile obstruction: for each integer A the rational dyadic seed from #554 BEC-08 is `p`-integral for every odd prime, and hence preserves **all p-channel residues, p-carries, and junction laws**. But its completed real orbit satisfies `−1<U_n(s_A)<0` for all `n∈[A−1,2A)`, by a certified source-tail inequality; thus the literal real carry is `κ_n=15` throughout the epoch. For h not divisible by16, the real carry character has modulus 1, while the prime side tends Haar, so the signed slip covariance is maximally coherent. The same source and prime clock do not select the zero real branch by themselves.

**Verdict:** source-side spectral emissions and junction rank are real and calculable; the original real-complement phase is still indispensable. No mathematical result in this dossier proves the proposed signed covariance bound for the bona fide zero-seeded π path.

## PBC-07. Finite receipts, independence, and next decisive falsifier

The finite development epochs A=100,128,256,512,1024 and **fresh preregistered A=2048** use the literal rational source and `p=1mod8` balanced candidates. All checked stage vectors, scalar p-residues, source/p-character gluing and cofactor identities agree *exactly*. At A=2048 the selector chose p=4937 with m=617, emission times 2469,3086,3703 and source injections 2468,2962,4114 modulo p. Their real carry values are respectively 12,2,2 and prime carries 12,9,7: prime birth does **not** dictate a matching real carry. Full real-vs-prime carry agreement is **117/2048**, far from a deterministic identification.

At the frozen A=2048 holdout the stage junction counts are `(103,215,103)`, `(175,288,154)`, `(107,404,106)`, `(55,287,51)`. The observed parity line has signs `−,+,−,−` (stage1's true limiting line is zero). The exact-weighted rational limiting source fingerprint is PBC-11, and all finite deviations are retained. The p-integral dyadic rational shadow preserves every prime channel and junction label but has **2048 consecutive real carries equal to 15**. This is a falsifier of any seed-blind positive or local-rank-only inference. The same-source rational seed 1/5 changes the actual carries while preserving all p-clock histories.

**Tests:** newly written source-specific focused tests use exact `Fraction` and independent direct unwrapped rational `pU_n` residues. Trigonometric/Fourier tests are diagnostic only. The finite rational junction formula has two independent exact implementations. The A=2048 output is obtained only after `PROTOCOL.md` was committed at `4bfcc9b0cb4162b3695f5898b06dbfb3112724a7`. An initial holdout runner failed because Python limits decimal conversion of huge integers; the repaired runner hashes the seed's hexadecimal numerator/denominator. No test pass or timing is inferred from an unrun CI job.

**Source/provenance:** inherited SUCC #497 PF-01..06, #499 Gaussian primal, #544 signed lag/CCV carry observer, #552 three-channel Gram, #554 BEC-01..08, #520 AC1..AC4, and main `duck_bbp.py` source. Imported classical facts: fixed-modulus PNT/AP; Cochrane–Pinner (2011) monomial exponential-sum bound; classical Gauss and finite Fourier geometric sums; Weyl criterion for Riemann-integrable interval observables. No independent global-priority claim. The precise next theorem must be a bound on the **source-selected real cofactor/slip signed mean**, with original zero boundary and full carries; it must reject the coherent dyadic shadow. **π base-16 normality remains OPEN.**
