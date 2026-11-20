# ACT-01–11: theorems, proofs, and adversarial boundaries

**Scope.** All mathematical objects are explicitly declared. Paper proofs are not Lean/kernel proofs. Finite exact arithmetic tests calibrate implementation, not universal quantifiers. Do not interpret `p`-adic norms, Gaussian Hilbert norms, or interference terms as thermodynamic energy absent a separately measured physical instrument.

## Notation and fixed source

Let `e(t)=exp(2 pi i t)`. The sole authentic source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Its Mellin impulse is `Q(t)=4-2t³-t⁴-t⁵=(1-t)H(t)`, where `H(t)=4+4t+4t²+2t³+t⁴`. Classically `x=sum_{j>=1}16^-j r(j)=pi/16`. Write `P_M=sum_{j=1}^M 16^-j r(j)`, `T_n=sum_{j>=1}16^-j r(n+j)`, `Y_n=U_n+T_n=16^n x`. A changed seed `s` changes the recurrence's unwrapped solution to `U_n(s)=U_n+16^n s` and completion to `16^n(x+s)`. **The selected source has `s=0` only.**

For `lambda>0`, write the periodized Gaussian kernel

\[
K_\lambda(t)=\sum_{k\in\mathbb Z} e^{-\lambda k^2/2}e(kt),\qquad
D_\lambda(\theta)=\|K_\lambda(\cdot-\theta)-K_\lambda\|_{L^2(\mathbb T)}^2.
\]
The series are absolutely convergent and `D_lambda(theta)=sum_{k!=0}e^(-lambda k²)|e(k theta)-1|²`. Set `S_lambda=sum_{k!=0} k²e^(-lambda k²)>0`. In the previous dossier, `A_B=(1/B)sum_{n=B}^{2B-1}(1-cos(2 pi theta_n))`, `theta_n=Y_n mod 1`, and **R0** is `liminf_(B->infty) A_B>0`. ACT-11 preserves the stronger previous witness obligation without claiming it has been paid.

## ACT-01 — Exact arithmetic-place transport (CLASSICAL)

For `q in Q*` with normalized absolute values `|p|_p=1/p`, the product formula is

\[
|q|_\infty\prod_{p\ \mathrm{prime}}|q|_p=1.
\]
In particular, `|16|_infty=16`, `|16|_2=1/16`, and `|16|_p=1` for odd primes `p`. **Proof:** Factor the relatively prime numerator and denominator of `q`; every prime exponent cancels between the Archimedean and p-adic valuations. The infinite product has finite support. A bare rational dilation is real-expanding and 2-adically contracting. The genuine rational forcing also supplies prime-local *inhomogeneous* terms. **Boundary:** this arithmetic identity is not a statement that the real, 2-adic and odd p-adic observation channels are physically coupled by an energy transfer. No adèle completion or physical ontology is inferred without an additional declared map.

## ACT-02 — Prime-square sources hide different signatures in different places (EXACT source-specific)

For any prime `p>=7`, define `n_p=(p²-1)/8`, an integer. The actual positive forcing *at the subsequent clock* is

\[
r(n_p+1)=\frac4{p^2}-\frac2{p^2+3}-\frac1{p^2+4}-\frac1{p^2+5}.
\]
The denominator offsets 3,4,5 are p-adic units. Hence

\[
\boxed{v_p(r(n_p+1))=-2,\qquad p^2r(n_p+1)\equiv4\pmod p.}
\]
The real expansion is instead

\[
\boxed{r(n_p+1)=15p^{-4}-59p^{-6}+O(p^{-8}).}
\]
Indeed, expand each `(p²+a)^-1=p^-2(1-a p^-2+a²p^-4+...)`. The p^-2 terms cancel because `4-2-1-1=0`; the p^-4 coefficient is `-[-2*3-4-5]=15`, and the p^-6 coefficient is `-[2*3²+4²+5²]=-59`. Thus `p^4r(n_p+1)->15` along primes although `|r(n_p+1)|_p=p²`.

The deliberately **non-authentic** matched-leading-jet mutation `Q*(t)=Q(t)+(1-t)^2` has

\[
r_*(n)=r(n)+\frac2{(8n-7)(8n-6)(8n-5)}.
\]
It preserves `Q*(1)=0`, `Q*'(1)=-15` and `r_*(n)~15/(64n²)`, but at the same prime-square clock

\[
\boxed{p^2r_*(n_p+1)\equiv5\pmod p,\qquad
r_*(n_p+1)=15p^{-4}-57p^{-6}+O(p^{-8}).}
\]
The residue shift follows from the extra term `1/p²` and the p-unit offsets 1,2. The real jet shift is `2p^-6+O(p^-8)`. The auxiliary source-filter contrast `H(A^-1)=[[8,1],[1,7]]`, determinant 55, versus `H_*(A^-1)=9I`, determinant 81, is inherited from [#670](https://github.com/femboy2112/SUCC/pull/670), separately replayed symbolically; it is not an authenticated real-circle conjugacy.

**Gaussian consequence.** Since `D_lambda(theta)=4 pi² S_lambda theta²+O_lambda(theta⁴)` near zero,

\[
\boxed{\lim_{p\to\infty\atop p\,\mathrm{prime}}
p^8 D_\lambda(r(n_p+1))
=900\pi^2S_\lambda
=\lim_{p\to\infty\atop p\,\mathrm{prime}}
p^8 D_\lambda(r_*(n_p+1)).}
\]
This is the precise content of **a common Gaussian real-energy shadow with distinct prime-local source labels**. It proves no lower shell density and does not transfer a p-adic norm into physical joules. A p=29 control has the original pole-square signature but lacks #670's 11-adic filter rank selection.

## ACT-03 — A chosen observation form contributes an observer defect, not an invariant carrier energy (CLASSICAL exact)

Let `T_b(t)=bt mod 1`, integer `b>=2`, and `T_{b*}` denote pushforward of measures. Fourier transport gives the exact square

\[
\boxed{T_{b*}(K_\lambda*\mu)=K_{b^2\lambda}*(T_{b*}\mu).}
\]
Proof: the h-th Fourier coefficient on either side equals `e^(-b²lambda h²/2)*mu_hat(bh)`.

If one incorrectly holds the Gaussian width fixed when transporting an already-smoothed point, the discrepancy is

\[
\begin{aligned}
\mathscr F_{\lambda,b}(\theta)
&=\|K_\lambda*(T_{b*}\delta_\theta)-T_{b*}(K_\lambda*\delta_\theta)\|_2^2\\
&=\sum_{h\ne0}\left(e^{-\lambda h^2/2}-e^{-b^2\lambda h^2/2}\right)^2
\equiv\mathscr F_{\lambda,b}>0.
\end{aligned}
\]
The phases cancel in Parseval; it is **independent of theta**, even at the locked source `theta=0`. For `lambda->0` the Gaussian Poisson summation formula yields

\[
\mathscr F_{\lambda,b}
=\sqrt{\pi/\lambda}\left(1+\frac1b-2\sqrt{\frac2{1+b^2}}\right)
+O_b(\lambda^{-1/2}e^{-c_b/\lambda}),\qquad c_b>0.
\]
The coefficient is positive for `b>1` (nonidentical Gaussian profiles); the defect diverges as resolution sharpens and vanishes as `lambda->infty`. It is **form-dependent**, cannot be an invariant energy of the original point carrier, and vanishes identically when the width is correctly transported to `b²lambda`. For BBP's radix `b=16`, use `256lambda`. This provides a precise testable version of the proposed 'extra representation energy' without imputing thermodynamic work to arithmetic.

## ACT-04 — Exact finite source-plus-terminal compensation; finite rational locked control (EXACT source-specific)

For any terminal `M>=0` set

\[
T_n^{[M]}=\sum_{j=n+1}^{M}16^{n-j}r(j),\quad0\le n\le M.
\]
With original `U_n` and any declared rational seed `s`, for each `0<=n<M`:

\[
\begin{aligned}
U_{n+1}(s)-16U_n(s)&=r(n+1),\\
T_{n+1}^{[M]}-16T_n^{[M]}&=-r(n+1),\\
U_n(s)+T_n^{[M]}&=16^n(P_M+s).
\end{aligned}
\]
These follow immediately by separating the `j=n+1` term and telescoping. The finite observer's completed state is therefore a **rational, exactly commuting successor**, with no completion limit used. In particular the deliberately changed seed `s_M=-P_M` gives `U_n(s_M)+T_n^[M]=0` for **every** `0<=n<=M` although all original positive source innovations remain present. This counterseed changes with `M`, so it is a finite family, **not** a single infinite countermodel. The separate fixed infinite counterseed `s=-x=-pi/16` gives `U_n(s)=-T_n`, `Y_n(s)=0` at all clocks. Both are forbidden substitutions for the authentic zero seed. **Crucible:** positive forcing in every clock and a positive local Gaussian innovation norm do not force any anti-lock lower bound.

## ACT-05 — Exact source/terminal Gaussian interference (CLASSICAL identity; source-specific controls)

For any real `u,t` and Fourier mode `h`, let `a=e(hu)`, `b=e(ht)` and split

\[
e(h(u+t))-1=(a-1)+a(b-1).
\]
The complex inner-product identity implies

\[
\begin{aligned}
|ab-1|^2={}&|a-1|^2+|b-1|^2\\
&+2\operatorname{Re}\big[(a-1)\overline{a(b-1)}\big].
\end{aligned}
\]
Multiply by `e^(-lambda h²)`, sum all `h!=0`, and obtain the exact Gaussian L² ledger

\[
\boxed{D_\lambda(u+t)=D_\lambda(u)+D_\lambda(t)+\mathcal I_\lambda(u,t),}
\]
where `I_lambda` is the *signed* cross-sum. For the authentic finite BBP terminal put `u=U_n(s)`, `t=T_n^[M]`; for the selected infinite orbit use `u=U_n`, `t=T_n` with its actual zero seed. For the finite rational locked control `s=-P_M`, `u=-t`; then every Fourier component has `a(b-1)=-(a-1)` and

\[
\boxed{D_\lambda(u+t)=0,\qquad
D_\lambda(u)=D_\lambda(t)>0\ (u\not\in\mathbb Z),\qquad
\mathcal I_\lambda(u,t)=-2D_\lambda(u).}
\]
Thus dropping mixed energy terms **manufactures false energy** on an exactly locked completed carrier. This is a diagnostic about representation/completion order, not an observation of a new physical interaction.

## ACT-06 — Exact rational prime-primary CRT decomposition and phase (CLASSICAL)

For `q=a/b in Q` reduced, `b>0`, let `p^k || b`, `b'=b/p^k`. Define `c_p in {0,...,p^k-1}` by `c_p ≡ a(b')^-1 (mod p^k)` and `tau_p(q)=c_p/p^k`; for primes not dividing `b`, define `tau_p(q)=0`. Then

\[
\boxed{q\equiv\sum_{p\mid b}\tau_p(q)\pmod1,\qquad
e(hq)=\prod_{p\mid b}e(h\tau_p(q)).}
\]
**Proof:** multiplying by `b`, the sum's p-primary term is congruent to `a mod p^k` and all other terms vanish modulo `p^k`. CRT gives equality modulo `b`. This is a finite exact decomposition of *rational circle phases*; it is not a decomposition of irrational `pi` into a finite set of prime amplitudes, nor a guarantee that the individual local phase channels decorrelate.

## ACT-07 — The signed cofactor anti-tracking invariant (EXACT; equivalent to R0, not a proof)

For an arbitrary finite prime set `S`, let `q_n=U_n` denote the **unwrapped rational original zero-seed** source state and `q_{S,n}=sum_{p in S}tau_p(q_n)`. For any declared seed `s` and integer `h!=0`, set

\[
a_{S,n}(h)=e(hq_{S,n}),\qquad
b_{S,n}(h;s)=e\big(h(q_n-q_{S,n}+T_n+16^ns)\big).
\]
Then `a*b=e(h16^n(x+s))`. The **signed cofactor mismatch** is exactly

\[
\boxed{
\frac1B\sum_{n=B}^{2B-1}|b_{S,n}(h;s)-\overline{a_{S,n}(h)}|^2
=2\big[1-\operatorname{Re}W_B(h;s)\big].}
\]
**Proof:** multiply the difference inside each modulus by `a` (unit modulus), yielding `ab-1`. Expand `|z-1|²=2(1-Re z)`. No statistical estimate is involved.

In particular for `h=1,s=0` a positive all-shell lower bound on the left **is exactly R0**, independent of the selected primes. For `s=-x` it is identically zero for every `S`; it detects the locked counterseed. If `a` is changed by a time-dependent unit gauge `g_n` and `b` by `g_n^-1`, the product and gap remain unchanged, while the individual positive component energies can change. This formalizes the distinction between **observer-form energy** and the invariant completed phase. **Boundary:** changing `S`, or detecting a large local p-adic component, cannot by itself pay the new *uniform signed* inequality. The observed prime cofactor and integer carries must be retained and a source-derived estimate must be proved separately.

## ACT-08 — Prime-square pulse sparsity/no-short-support theorem (CLASSICAL counting, source clock)

Let `E={n_p=(p²-1)/8: p prime>=7}`. On a shell `[B,2B)`, consider an arbitrary complex bounded witness `f_B(n)` with `|f_B(n)|<=C` and support contained in forward windows `[n_p,n_p+L_B)` initiated at clocks `n_p` (including earlier pulses that can reach the shell). There are fewer than `sqrt(16B+1)` candidate positive integers `p` whose event can start at or before `2B`. Hence

\[
\boxed{\left|\frac1B\sum_{n=B}^{2B-1}f_B(n)\right|
\le\frac{C L_B\sqrt{16B+1}}{B}.}
\]
Proof: the support is covered by at most that many length-`L_B` windows, regardless of overlap. If `L_B=O(log B)` and `C` is independent of `B`, this mean is `O(log B/sqrt B)->0`. **A bounded witness supported only on short neighborhoods of the prime-square event clocks cannot yield an all-shell positive R0 lower bound.** A source argument with persistent, propagating, nonlocal cofactor influence, or a dense alternative class of events, is not covered. This does not prove R0 false and does not prohibit a genuine global all-clock theorem.

## ACT-09 — Model representation enters physical causality only through a specified action/instrument (CONDITIONAL classical)

Consider a deterministic embedded observer with memory `m_n`, report `y_n`, action `a_n` and intervenable carrier `s_n`:

\[
y_n=O_f(s_n),\quad m_{n+1}=G_f(m_n,y_n),\quad a_{n+1}=\Pi_f(m_{n+1}),\quad
s_{n+1}=F(s_n,a_n).
\]
Here `f` indexes the chosen representation. If two representations produce identical action histories from the same initial carrier and `F` is otherwise fixed, induction gives identical carrier trajectories even if their internal Gaussian defects differ. To demonstrate actual source back-action, acquire a calibrated accessible state with two form-dependent lawful interventions `a!=a'` and a measured nonzero carrier response `F(s,a)!=F(s,a')`, with appropriate confounder controls. A fixed source with `F(s,a)=F(s)` is a decisive negative model. The one-step synthetic `F(s,a)=s+a` supplies a positive calibration. This is a criterion for causal *intervention*, **not evidence** that mathematical evaluation changes pi or that Hilbert norms are joules.

## ACT-10 — Matched-jet and phase-only hostile controls (EXACT)

The mutant in ACT-02 matches the source's first Mellin jet and real `p^-4` signature, but differs in its p-primary residue (5 rather than 4) and inherited 11-adic filter. The unchanged-forcing finite seed `-P_M` matches all forcing samples and prime signatures but has zero completed phase at every finite terminal; the fixed `-x` seed is identically locked at infinity. The rational shift `1/16` is invisible to all late circle phases `n>=1` but not to the unwrapped seed channel. Each is a separate control, and none may be silently conflated with the original zero-seeded source.

## ACT-11 — What would actually advance the pi frontier? (UNVERIFIED)

The inherited GYC-11 criterion in [#672](https://github.com/femboy2112/SUCC/pull/672) says: if source-derived `q_n` in the same Gaussian Hilbert space satisfy, on every sufficiently late shell, a uniform bound `(1/B)sum ||q_n||²<=M²` and a **signed** correlation lower bound `|(1/B)sum <K_(theta_n)-K_0,q_n>|>=c>0`, then Cauchy-Schwarz plus GYC-03 gives `A_B>=c²/(2S_lambda M²)>0`, hence R0. The exact cofactor identity ACT-07 supplies a *target*, not a new lower bound or independently constructed witness. ACT-08 prohibits one cheap event-local candidate. An admissible new witness must use the authentic integer/prime/cofactor journal, chronological orientation and zero anchor, and demonstrate a source-specific signed estimate which fails on the fixed locked counterseed. **No such estimate is established here.**

## Overall verdict

**SURVIVES (proved scoped mathematics):** arithmetic/2-adic opposition; a BBP prime-square p-primary event whose real Gaussian shadow is suppressed by pole cancellation; an observer-form Gaussian defect; exact rational completion; signed cross interference; cofactor/gauge invariance; short pulse support no-go; and a conditional causal-feedback instrument.

**FAILS (receipts ACT-03, ACT-04, ACT-05, ACT-08):** bare Gaussian norm as intrinsic carrier energy; positive local forcing as evidence of actual orbit escape; short prime-square events as a stand-alone density proof; observer representation as proof of physical numerical back-action.

**REMAINS OPEN:** the all-late-shell original-zero, signed source/cofactor anti-tracking inequality; full base-16 normality; RH; a physical ontology connecting computation and carrier energy. Distinguish tool/probe access from source adequacy before any promotion.
