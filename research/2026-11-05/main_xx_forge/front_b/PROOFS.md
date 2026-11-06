# Front B — the critical carry innovation is an orbit discrepancy; its normality transport needs stationarity

**Operation Main XX, 2026-11-05. Research-only.** Additive descendant of PR #522 (head `cd672158`, which carries the #521 precision repair). The original four signed poles, the literal seed `U_0=0`, every frozen contract and every Lean declaration are untouched. Nothing here proves π base-16 normality, and nothing promotes it. Status labels are those of `docs/METHOD.md`.

## 0. Setup

Source (immutable): `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`. For a real seed `s`, `U_n(s)=U_n(0)+16^n s`, `x_n(s)={U_n(s)}`. Write

\[
S_k(n)=\sum_{j=1}^{k}16^{k-j}r(n+j),\qquad U_{n+k}=16^kU_n+S_k(n),\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j).
\]

Facts used (all proved in-repo): `r(n)>0` for `n≥1` (`r(1)=47/15`, and #521 CT1 for `n≥2`); `16T_n-T_{n+1}=r(n+1)`, hence `16^mT_N=S_m(N)+T_{N+m}`; the gauge `U_n(s)+T_n=16^n\alpha` with `\alpha=s+\pi/16` (#521 CT7); and the uniform truncation law (#521 CT2)

\[
\Bigl|S_m(n)-\frac{16^m-1}{64n^2}\Bigr|<\frac{16^m}{10n^3}\quad(n\ge2,\ m\ge1),
\qquad\text{hence}\qquad \Bigl|T_n-\frac1{64n^2}\Bigr|\le\frac1{10n^3}.
\]

The #522 objects (HS-01, HS-08): for `m,k≥1`, `d=m+k`,

\[
\theta_{n,m,k}=\{16^{d}x_n\},\quad \delta_{n,m,k}=\{16^mS_k(n)\},\quad
b_{n,m,k}=\mathbf 1_{\{\theta+\delta\ge1\}},\quad
J_{A,m,k}(s)=\frac1A\sum_{n=A}^{2A-1}(b_{n,m,k}-\delta_{n,m,k}).
\]

A triple `(A,m,k)` is **admissible** if `16^dT_n\le 1` for every `n\in[A,2A)` (this implies `S_d(n)<1` and `0<\delta<1`). Write `c_A(d)=16^d/(64A^2)`.

**Admissibility law — CERTIFIED-FINITE (`d\le200`), CONJECTURED beyond.** `(A,m,d-m)` is admissible ⟺ `A\ge2^{2d-3}` ⟺ `c_A(d)\le1` ⟺ `16^d<(8A+1)(8A+2)` (the #521 CT-03 domain).
*Receipt.* `admissibility_law.py` checks, symbolically, that `r` is decreasing for `m\ge2`, so `T_n` is decreasing. It then uses exact rational enclosures (`duck_bbp.tail_interval`, whose tail budget is the Lean-checked one) to verify `16^dT_{2^{2d-3}}\le1<16^dT_{2^{2d-3}-1}` for every `2\le d\le200`: 0 exceptions. Found independently by the hostile reviewer (probe `p5_domain.py`). Asymptotically the margin is `≈1.125/2^{2d-3}>0`, which suggests the law holds for every `d`. That is not certified.

## CB-1. Carry–interval identity — PROVED (exact, every seed, every positive forcing)

**Theorem CB-1.** Let `n\ge1`, `m,k\ge1`, `d=m+k`, any seed `s`, and suppose `S_d(n)<1`. Then exactly

\[
\boxed{\;b_{n,m,k}=\mathbf 1\bigl[\,S_m(n+k)\le x_{n+d}<S_d(n)\,\bigr],\qquad
\delta_{n,m,k}=S_d(n)-S_m(n+k).\;}
\tag{CB1}
\]

If moreover `16^dT_n\le1`, then with `z_j=\{16^j\alpha\}`, `\alpha=s+\pi/16`,

\[
\boxed{\;b_{n,m,k}=\mathbf 1\bigl[\,16^mT_{n+k}\le z_{n+d}<16^{d}T_n\,\bigr],\qquad
\delta_{n,m,k}=16^dT_n-16^mT_{n+k}.\;}
\tag{CB1g}
\]

*Proof.* Put `σ=S_d(n)`, `ε=S_m(n+k)`, `y=x_{n+d}`. Splitting the `d` steps as `k` then `m` gives `S_d(n)=16^mS_k(n)+S_m(n+k)`, so `16^mS_k(n)=σ-ε`. Positivity of `r` gives `ε>0` and `σ-ε>0`; with `σ<1` this forces `δ=σ-ε`. Since `16^d\lfloor U_n\rfloor\in\mathbb Z`, `θ=\{16^dU_n\}=\{U_{n+d}-σ\}=\{y-σ\}`.
If `y\ge σ`: `θ=y-σ` and `θ+δ=y-ε<1`, so `b=0`.
If `y<σ`: `θ=y-σ+1` and `θ+δ=1+(y-ε)`, so `b=1` iff `y\ge ε`.
Together, `b=\mathbf 1[ε\le y<σ]`.
For (CB1g): `x_j=\{z_j-T_j\}` by the gauge. Using `16^mT_N=S_m(N)+T_{N+m}`, we get `ε+T_{n+d}=16^mT_{n+k}` and `σ+T_{n+d}=16^dT_n`. If `z_{n+d}\ge T_{n+d}`, then `y=z_{n+d}-T_{n+d}` and the condition translates exactly. If `z_{n+d}<T_{n+d}`, then `y\ge1-T_{n+d}\ge σ` (equality possible at `z=0`; admissibility `16^dT_n\le1` is exactly the no-wrap condition), so `b=0`; and `z_{n+d}<T_{n+d}<16^mT_{n+k}`, so `z_{n+d}` is not in the interval either. ∎

*Remark (m=0).* The proof also holds verbatim for `m=0` (`ε=0`, `y-ε<1`). There, `b=\mathbf 1[x_{n+k}<S_k(n)]`. This is the #521 CT3 boundary bit, so Corollary 2 below covers CT-03 itself.

**Corollaries (all PROVED).**
1. *The critical carry innovation is a discrepancy of the orbit itself.* For an admissible triple,
   `J_{A,m,k}(s)=A^{-1}\sum_n[\mathbf 1_{I_n}(x_{n+d})-|I_n|]` with the deterministic, seed-independent window `I_n=[S_m(n+k),S_d(n))`. Equivalently, it is the discrepancy of the completed ×16 orbit `z` against `[16^mT_{n+k},16^dT_n)`. Beyond the orbit itself (in the `z`-form, beyond the single number `α=s+π/16`), the source enters only through the smooth endpoints (`≈ c/(n/A)^2` and `≈ c\,16^{-k}/(n/A)^2`). Carries, numerators and denominators supply no further information about `J`.
2. *Coherent wrong seed* `s_*=-\pi/16` (`α=0`): `z\equiv0` is never in the interval (whose left end is `>0`), so `b\equiv0` and `J=-A^{-1}\sum δ_n`. This reproves #521 CT-03 in one line, on the **same** domain: by the admissibility law, "admissible" coincides with CT-03's `16^d<(8A+1)(8A+2)` (certified for `d\le200`). An earlier draft claimed this was an extension; the hostile review refuted that.
3. *Not a source fingerprint.* (CB1) uses only `r>0` on `(n,n+d]`. Every positive forcing, including one-pole mutants, obeys it.
4. *Ensemble moments carry no seed information.* Under a Haar seed, the `z_j` are the i.i.d.-uniform-digit shift (#522 HS-06). The #521 CT-05/CT-06 covariance and third-moment formulas are therefore functionals of the window geometry `\{I_n\}` alone. They are identical for every selected seed, so they cannot separate the zero seed from any other. (This holds by construction for any ensemble average; what CB-1 adds is the explicit window geometry those moments are computed on.)

## CB-2. Stationary rigidity — PROVED (conditional transport to normality)

Let `ν_N=N^{-1}\sum_{j<N}δ_{x_j}` (Cesàro empirical measures of the selected orbit).

**Theorem CB-2.** Fix a seed `s`. Assume
- **(H1) frequency existence:** `ν_N\to ν` weakly for some probability measure `ν` on `\mathbb T`;
- **(H2) lattice smallness:** for every `k\ge1` and `c\in(0,1)` there are `A_i\to\infty` and `d_i>k` such that every `(A_i,d_i-k,k)` is admissible, `c_{A_i}(d_i)\to c`, and `J_{A_i,d_i-k,k}(s)\to0`.

Then `ν` is Haar, i.e. the orbit `\{16^j\alpha\}` (equivalently `x_n(s)`, which differs by `T_n\to0`) is equidistributed. By Wall's theorem, `α` is then normal in base 16.
Conversely, base-16 normality implies `J\to0` uniformly over admissible triples (Lemma 2.5), so under (H1) the gate is an equivalence.

*Lemma 2.5 (converse).* If the orbit is equidistributed, then `\sup_{(m,k)\ \mathrm{admissible}}|J_{A,m,k}|\to0`.
*Proof.* Let `D_N` be the star discrepancy of the first `N` points; `D_N\to0`. Cut `[A,2A)` into `M` blocks of length `A/M`. Every endpoint `S_m(n+k)` and `S_d(n)` is `\le1` and, by CT2, varies by at most `2/M+O(1/A)` along a block, uniformly in admissible `(m,k)`. Sandwich each block between two fixed intervals. The block count of each fixed interval is a difference of two prefix counts, so it deviates from its length by at most `2\cdot3A\,D_{3A}`. Summing over blocks gives `|J|\le O(1/M)+O(M\,D_{3A})+O(1/A)` uniformly; choose `M\to\infty` slowly. ∎

*Lemma 2.1 (sub-window limits).* Under (H1), for `1\le a<b` and a shift `d_A=o(A)`, the measures `\frac1{(b-a)A}\sum_{n\in[aA,bA)}δ_{x_{n+d_A}}` converge to `ν`.
*Proof.* The count over `[aA,bA)` equals `bAν_{bA}-aAν_{aA}`, up to `O(d_A)` boundary terms. ∎

*Lemma 2.2 (limit of the innovation).* Let `G(v)=ν([0,v))-v` and `Ψ(c)=\int_1^2G(c/u^2)\,du`. Along the sequence of (H2), `J_{A_i,d_i-k,k}\to Ψ(c)-Ψ(c16^{-k})`.
*Proof.* By CT2, `S_{d}(n)=c_{A}(d)(A/n)^2+O(1/A)` and `S_{d-k}(n+k)=16^{-k}c_A(d)(A/n)^2+O(\log A/A)`, uniformly on `[A,2A)`. Cut `[A,2A)` into `M` blocks. On each block, sandwich `\mathbf 1_{I_n}` between indicators of two fixed intervals whose endpoints differ by `O(1/M)`. Choose those fixed endpoints off the (countably many) atoms of `ν`, so the portmanteau theorem applies, and then apply Lemma 2.1 to each. The intervals stay inside `[c16^{-k}/4-o(1),\,c+o(1)]\subset(0,1)`, so `0\equiv1` is never an endpoint, and an atom of `ν` at 0 cancels in `G(σ)-G(ε)`. The endpoints `c/u^2` and `c16^{-k}/u^2` are strictly monotone in `u`, so they meet the countably many atoms of `ν` only for countably many `u`. Letting `A\to\infty` and then `M\to\infty`, dominated convergence gives `\int_1^2[G(c/u^2)-G(c16^{-k}/u^2)]du`. ∎

*Lemma 2.3 (Mellin periodicity).* Let `H` be bounded and measurable on `(0,1)` with `\int_1^2H(c/u^2)du=0` for all `c\in(0,1)`. Then **for almost every** `v`, `H(v)=\sqrt v\,L(\log_2(1/v))`, where `L` is the 2-periodic extension of its restriction to `[0,2)` and `\int_0^2L=0`.
*Proof.* Substitute `c=2^{-t}` and `u=2^{w/2}` (so `du=\frac{\ln2}{2}2^{w/2}dw`); then `0=\int_0^2H(2^{-(t+w)})2^{w/2}dw\cdot\frac{\ln2}{2}`. With `L(s)=H(2^{-s})2^{s/2}` this reads `2^{-t/2}\int_t^{t+2}L(s)ds=0` for all `t>0`. The function `t\mapsto\int_t^{t+2}L` is locally Lipschitz (`L` grows at most like `2^{s/2}`) and vanishes identically. By Lebesgue differentiation, `L(t+2)=L(t)` for a.e. `t`. Letting `t\to0^+` gives mean zero. ∎

*Lemma 2.4 (monotone squeeze).* If `F(v)=a+v+\sqrt v\,L(\log_2(1/v))` is nondecreasing on `(0,1)`, with `L` 2-periodic and of mean zero, then `L=0` a.e.
*Proof.* With `s=\log_2(1/v)`, `L(s+2)=L(s)` gives `F(v)-F(v/4)=\tfrac34v+\tfrac12\sqrt v\,L(s)\ge0`, so `L(s)\ge-\tfrac32\,2^{-s/2}`. Apply this at `s+2j` and let `j\to\infty`: `L\ge0` a.e. Mean zero then forces `L=0` a.e. ∎

*Proof of CB-2.* By Lemma 2.2 and (H2), `Ψ(c)=Ψ(c16^{-k})` for all `c\in(0,1)` and `k\ge1`. Letting `k\to\infty`, bounded convergence gives `Ψ\equiv a:=ν(\{0\})=G(0+)`. Then `H=G-a` satisfies Lemma 2.3, so `F(v)=ν([0,v))=a+v+H(v)` has the form of Lemma 2.4 and is nondecreasing. Hence `H=0` a.e., and by left-continuity `F(v)=a+v` on `(0,1)`. Letting `v\uparrow1` gives `1\ge a+1`, so `a=0` and `ν` is Lebesgue measure. ∎

**Variant CB-2′ (log-scale local stationarity) — PROVED.** For real `1\le a<b`, let `μ_{[aA,bA)}` be the empirical measure of `x_n` (equivalently of `z_n`; they differ by `T_n\to0`) over `n\in[aA,bA)`, and put `μ_A=μ_{[A,2A)}`.
Replace (H1) with
(LS): for every `η>0`, `\sup\{D(μ_{[aA,bA)},μ_A):1\le a<b\le8,\ b-a\ge η\}\to0`, where `D` metrizes weak convergence.
Replace (H2) with (H2\*): for each `k\ge1` and each `η>0`, `|J_{A,d-k,k}|\to0` uniformly over admissible `(A,d)` with `c_A(d)\le1-η`.
Then `μ_A\to` Haar, so the orbit is equidistributed (normal, by Wall).
*Proof.*
1. Take any `A_i` with `μ_{A_i}\to ν` (compactness).
2. Because the sup in (LS) is uniform in `(a,b)`, Lemma 2.1 holds uniformly for all windows `[aA_i,bA_i)` with `1\le a<b\le8` and `b-a\ge1/M`: they all converge to `ν`. The shift `d=O(\log A)` moves the index range only `O(\log A)` points past `8A_i`, which is negligible.
3. As `A'` runs over `[A_i,4A_i]`, `A'=4^d/(8\sqrt c)` hits every target `c\in(0,1)` modulo the lattice: `c_{A'}(d)` sweeps a full factor of 16. The `M` blocks of `[A',2A')` are windows `[aA_i,bA_i)` with `b-a\ge1/M` and `b\le8`.
4. Lemma 2.2 therefore holds along `A'_i` with limit measure `ν`. Lemmas 2.3–2.4 then give `ν=` Haar.
5. Every subsequential limit is Haar, so `μ_A\to` Haar. Dyadic decomposition `[1,N)=\bigcup[N2^{-j-1},N2^{-j})` then gives Cesàro equidistribution. ∎

*Remark.* If `μ_{[A,2A)}\to ν` for **every integer** `A`, then telescoping gives Cesàro convergence (H1), and Lemma 2.1 then controls every sub-window. Convergence along powers of two only, `A=2^j`, does **not** control sub-windows. Witness: the counting defect `G(t)=εt\sin(2\pi\log_2t)` vanishes at every `t=2^j`, but not on `[1.5\cdot2^{j},2^{j+1})`. A greedy 0/1 realisation with `ε=0.05` has frequency `0.5` on `[2^{19},2^{20})` but `0.57632` on `[1.5\cdot2^{19},2^{20})` (hostile-review probe `p6_cb2.py`). That is why (LS) is stated for arbitrary sub-windows. An earlier witness with a fixed `A` was defective (it is `O(1)=o(A)`) and is withdrawn.

**Sharpening (Front A, FA-3/FA-5).** The hypotheses can be weakened: `k=1` alone, and lattice values `c\in(0,c_*)` for any fixed `c_*>0`. Weak limits of the windows are ×16-invariant (#520 R-04). Front A's rigidity lemma FA-3 then applies: a ×b-invariant measure that dominates Lebesgue on an open arc is Haar. See `../front_a/PROOFS.md`.

**Status.** CB-2/CB-2′ are a *conditional equivalence*: under (H1) or (LS), `J`-smallness ⟺ normality. **This is not progress on π.** Both (H1) and (LS) are open for π, and so is (H2).

## CB-3. Non-stationary countermodel — PROVED (the transport fails without stationarity)

**Theorem CB-3.** There is a real `α` — indeed almost every realization of the random construction below — such that, for the **same authentic forcing** and the seed `s=α-\pi/16`:
(i) `\sup_{(m,k)\ \mathrm{admissible}}|J_{A,m,k}(s)|\to0` as `A\to\infty`;
(ii) `α` is **not** normal in base 16: the repeat frequency `N^{-1}\#\{j<N:D_j=D_{j+1}\}` of its hex digits is `\ge 1/16+η` for all large `N` (normal numbers have `1/16`).
By CB-2, its Cesàro empirical measures therefore do **not** converge.

*Construction.* Let `F_p` be the distribution function of the i.i.d.-digit measure `β_p` on `[0,1)` with digit law `p` on `\{0,…,15\}`, and let `u` be the uniform law.

*Lemma 3.1 (lattice calibration).* If `p_0=1/16`, then `F_p(16^{-k}t)=16^{-k}F_p(t)` for `t\in[0,1]`, `k\ge0`. (The event `[0,16^{-k}t)` is "first `k` digits are 0, then `<t`".)

*Lemma 3.2 (a calibrated non-uniform family).* Let `v=e_1-e_{15}`, `w=e_2-e_3`, and let `φ` be a `C^1` bump with support `[0.3,0.7]` and `φ=1` on `[0.4,0.6]`. For `0<t_0\le0.04` (small enough for the IFT radius) there is a Hölder-continuous `λ(τ)` on `[1/16,1]`, with `|λ|=O(t_0)`, such that `p(τ)=u+t_0φ(τ)w+λ(τ)v` satisfies: `p_0=1/16`; `p(τ)` is a probability vector; `F_{p(τ)}(τ)=τ`; `p(τ)=u` outside `(0.3,0.7)`; and `p_2-p_3=2t_0` on `[0.4,0.6]`.
*Proof.* `Φ(p,τ)=F_p(τ)-τ` is a convergent power series in `p` near `u`, continuous in `τ`, with `Φ(u,τ)=0`. For `τ\in[2/16,15/16)` the first digit `s_1=\lfloor16τ\rfloor` lies in `[2,14]`. Moving mass along `v` adds `+1` to `\sum_{a<s_1}p_a`, leaves `p_{s_1}` fixed, and changes the tail factor `F_p(\{16τ\})` by a derivative `D` with `|D|\le\sum_{i\ge1}[(i-1)16^{2-i}+16^{1-i}]=256/225+16/15<2.21`. Hence `\partial_vΦ(u,τ)\ge1-2.21/16>0.86`, uniformly on `[0.3,0.7]`. `Φ` is analytic in `p` on the hyperplane `\sum p_a=1` near `u`, uniformly in `τ`. (Continuity of `F_p(τ)` in `τ` across 16-adic rationals uses `\sum p_a=1`.) Cauchy estimates therefore make `\partial_λΦ` jointly continuous and keep it `\ge0.85` on a fixed neighbourhood. The implicit function theorem, uniform in `τ` on the compact bump, gives a unique small `λ(τ)` with `Φ=0`. Outside the bump, uniqueness forces `λ=0`.
*Regularity.* For `p` near `u`, `τ\mapsto F_p(τ)` is Hölder with exponent `β=\log(1/\max_ap_a)/\log16>0`, uniformly. Write `Φ(p(τ),τ)-Φ(p(τ'),τ')=0` and use `\partial_λΦ\ge0.85` and the `C^1` bump `φ`. This gives `|λ(τ)-λ(τ')|\le C|τ-τ'|^{β}`. So `p(·)` is uniformly `β`-Hölder; this is the modulus `ω(h)\le Ch^β` used in Lemma 3.3. ∎

Let `τ_j=16^{\lfloor\log_{16}(64j^2)\rfloor}/(64j^2)\in(1/16,1]`. Draw the hex digits `D_j` of `α` independently with law `p(τ_j)`, so that `z_n=0.D_{n+1}D_{n+2}\ldots`.

*Lemma 3.3 (expectation).* Uniformly over admissible `(A,m,k)` and `n\in[A,2A)`, `\mathbb E\,b_{n,m,k}-δ_{n,m,k}\to0`.
*Proof.* Use (CB1g). Let `L=\lceil5\log_{16}A\rceil`. The first `L` digits of `z_{n+d}` are within total variation `L\,ω(CL/n)\le CL(L/A)^{β}\to0` of `β_{p^*}`, `p^*=p(τ_{n+d+1})`. Here `ω(h)\le Ch^β` is the Hölder modulus of `p` on the lattice circle (Lemma 3.2). It is well defined because `p=u` near both `1/16` and `1`; wraps inside the `L`-digit window are harmless for the same reason. Truncating at depth `L` changes membership only within `16^{-L}` of an endpoint, which has probability `\le4(1/16+2t_0)^L\le4A^{-5(1-\log_{16}(1+32t_0))}\le4A^{-3.5}` for `t_0\le0.04`.
*Lattice matching.* Let `e=\lfloor\log_{16}(64(n+d+1)^2)\rfloor`, so `τ_{n+d+1}=16^e/(64(n+d+1)^2)`. CT2 gives `64n^2T_n=1+O(1/n)`, hence `16^dT_n=τ_{n+d+1}16^{d-e}(1+O(\log A/A))`. Suppose `d\ge e+1`; for large `A` this forces `d\ge3`. Then `16^dT_n\ge16τ_{n+d+1}(1+2(d+1)/n)(1-6.4/n)>16τ_{n+d+1}>1`, contradicting admissibility. So `j:=e-d\ge0`. The left endpoint `16^mT_{n+k}` is the same lattice point times `16^{-k}(1+O(\log A/A))`. Lemma 3.1 and calibration then give `β_{p^*}(I_n)=|I_n|+o(1)`; the `o(1)` uses Hölder continuity of `F_{p^*}`, with exponent `\log(1/\max p^*)/\log16>0`. ∎

*Lemma 3.4 (concentration).* Let `b^{(L)}_n` be the indicator computed from digits `n+d+1,\ldots,n+d+L`. These are `L`-dependent, so `\mathbb E|\sum_n(b^{(L)}_n-\mathbb Eb^{(L)}_n)|^4\le C(AL)^2`. Summing `P(|J^{(L)}-\mathbb EJ^{(L)}|>ε)\le CL^2/(ε^4A^2)` over all `A\in\mathbb N` and the `O(\log^2A)` admissible `(m,k)` gives a convergent series (`\sum(\log A)^4/A^2<\infty`). Borel–Cantelli on `\{b_n\ne b^{(L)}_n\}` finishes (i). Each such event has probability `\le4A^{-3.5}` (Lemma 3.3, `t_0\le0.04`), and there are `O(A\log^2A)` events per epoch; `\sum_AA\log^2A\cdot A^{-3.5}<\infty`. ∎

*Lemma 3.5 (non-normality).* `\mathbb E\mathbf 1[D_j=D_{j+1}]=\sum_ap_a(τ_j)^2+o(1)=1/16+\|p(τ_j)-u\|^2+o(1)`. The indices with `τ_j\in[0.4,0.6]` are `j\in(4^e/8)[\sqrt{5/3},\sqrt{5/2}]`: intervals of ratio `\sqrt{1.5}` recurring at ratio 4. This set has Cesàro lower density `f_0=(\sqrt{1.5}-1)/3\approx0.0749` (an audit count over `j<3\cdot10^6` gives `0.07491`). On it `\|p-u\|^2=2t_0^2+2λ^2\ge2t_0^2`, since `w\perp v`. The strong law for 1-dependent bounded variables gives repeat frequency `\ge1/16+f_0t_0^2` eventually, almost surely. ∎

**Meaning.** The J-family can sit at zero on a non-normal orbit of the same forcing. *Any* noncircular transport from critical-carry innovations to fixed-h Weyl or to `Q_{1/2}` must therefore use some additional input that the CB-3 orbit violates. CB-2/CB-2′ show that a stationarity input, (H1) or (LS), is one such input that suffices; CB-3 does not show it is the only possible one. This is the decisive obstruction to the #522 NEXT.md "one concrete candidate" as a normality route. It is not a statement that the zero seed's `J` fails to vanish.

## CB-4. Gate factorization — PROVED, and an EQUIVALENT REFORMULATION (not progress)

For any seed:

\[
\text{base-16 normal}\iff (\mathrm{LS})\ \wedge\ (\mathrm{H2}^*).
\]

*Proof.* (⇐) is CB-2′. (⇒) Normality gives Cesàro equidistribution (H1). The window count over `[aA,bA)` is `bAν_{bA}-aAν_{aA}`, with error `o(bA)`. Divided by `(b-a)A\ge ηA` with `b\le8`, that error is `o(1)\cdot8/η` uniformly in `(a,b)`, which is (LS). (H2\*) follows from Lemma 2.5. ∎

Both conjuncts are strictly weaker than normality. (H2\*) alone fails by CB-3. (LS) alone fails for a generic point of any non-uniform Bernoulli measure: its local measures are stationary, and its repeat frequency is `\sum p_a^2>1/16`. So the open gate splits into **uniformity at source-lattice thresholds** and **log-scale stationarity**; neither is known for π. The split is useful only because it gives two separately falsifiable targets (see NEXT.md); it does not discharge either.

## What is genuinely new here, and what is not

- New to SUCC (to our knowledge; no scholarly priority claimed): the exact identity CB-1/CB-1g; the Mellin-periodicity-plus-monotone-squeeze rigidity of CB-2; the same-forcing non-stationary countermodel CB-3; and the factorization CB-4.
- Classical inputs: the Bailey–Crandall perturbed-orbit equivalence (the gauge), the implicit function theorem, and Borel–Cantelli.
- **OPEN, unchanged:** `J_{A,m,k}(0)\to0` for the zero seed; frequency existence or (LS) for π; fixed-h Weyl `S_N(h)=o(N)`; `Q_{1/2}(μ_A)\to0`; π base-16 normality; RH.
