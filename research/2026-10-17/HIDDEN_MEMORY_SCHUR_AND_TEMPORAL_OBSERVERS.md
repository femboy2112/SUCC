# Hidden-memory Schur telescope — delayed observer access to the true Gamma–FUCC polar response

**Research branch:** `research/hidden-memory-schur-telescope-2026-10-17` (stacked on draft PR #158, pinned head `a60e52a05459b619f2c8cbf557636f4a76b68e65`). **Source:** frozen original `observational_succ/source_weil_hierarchy.py` git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, parent source `dc6b7e3`; original completed Suzuki–Weil form at `a=1/2`. No source changes, nontrivial zero locations or fictitious Euler impulses. **Actual first-window S4 sign: OPEN. RH: OPEN.**

## 0. Literature premise and its limits — what the Nature paper actually establishes

Lokesh Muruga, Felix Ginot, Sarah A. M. Loos and Clemens Bechinger, [*The extraction of work from hidden degrees of freedom*, Nature Physics (published October 16, 2026)](https://www.nature.com/articles/s41567-026-03442-w), DOI: `10.1038/s41567-026-03442-w`, use delayed binary measurement pairs of an optically trapped Brownian particle in a viscoelastic, non-Markovian bath. Their experiment retrieves bath information that flows back into the observed tracer, changing relaxation and improving work extraction relative to a Markovian rigid-shift benchmark. The paper's order parameter contrasts measured history-conditioned information relaxation against an instantaneous-state-matched Markovian reference. The experiment tests genuine classical stochastic thermodynamics. It **does not** prove any identity between thermodynamic work, zeta zeros, the Weil quadratic form, or SUCC's source-generated spectral operator.

The mathematical bridge here is the **classical Mori–Zwanzig/Nakajima elimination identity**: when an observer discards hidden Hilbert directions, their influence returns through a time-delayed memory kernel. For this SUCC source, the integral of that kernel is **exactly the missing signed Schur correction**. Our treatment is mathematical, not a claim that a Gaussian/source operator represents the experimental bath. Delayed observation is a useful analogy for acquiring a high-response kernel, not a guarantee that such measurements can physically be performed.

## 1. Actual signed source and canonical spectral decomposition

Let `I=(-1/2,1/2)`, `F=Vu` the zero-extended primitive of a mean-zero derivative-carrier test `u`, and let `L=L^+_a` be the nonnegative source-generated Gamma+genuine prime-2 FUCC jump Friedrichs operator described in SCIMS-08/JS-01 of the parent. This retains the **real** Gamma OU tower, `w_2=log(2)/sqrt(2)`, all true active prime-power atoms and no independent composite `6` place.

On smooth source primitives the *unchanged signed completed form* is

`H=L-M I +2|c><c|-2|s><s|`,

where `M=C_infty+2w_2` is the genuine negative contact/prime potential, `c(x)=cosh(x/2)` and `s(x)=sinh(x/2)` on I. Both completed polar terms and original half-density remain; this is **not** an auxiliary positive Gram. Let `P=1_[0,7](L)`, `Q=1-P`. Parent JS-02 proves conditionally, with exact rational Gamma rung arithmetic and source replays, `rank P<=453` and

`D:=QHQ >=d Q`, `d=9/16` (in fact strictly >d), so `||D^{-1}||<16/9`.

The parent source adapter also replays WB4 positive high coercivity and protects the Suzuki SHA. No actual P eigenvector, spectral gap around 7, high matrix, or polar high resolvent is numerically reconstructed here.

Define the original full signed blocks

`A=PHP`, `B=PHQ`, `D=QHQ`, `S=A-BD^{-1}B*`.

Since P commutes with the **entire positive source jump L**, its offdiagonal comes from **nothing but the authentic completed polar terms**:

`B=2|Pc><Qc|-2|Ps><Qs|`.

Parity separates the even `c` and odd `s` channels. Therefore `rank B<=2` and

`||B||² <=max(||c||^4,||s||^4)=||c||^4`.

Indeed `||c||²=1/2+sinh(1/2)`. The exact elementary series bound `sinh(1/2)<12/23` follows by bounding every `(2j+1)!>=6^j` and summing the geometric series of ratio 1/24. Hence `||c||²<47/46<33/32` and

`||B||² < (33/32)^2`.

This is a global **source-conditional bound on the high coupling**, not an actual computation of `Pc,Qc,Ps,Qs`.

## 2. HM-01 — exact hidden-memory response (PAPER / classical source specialization)

On a dense smooth core, solve the abstract linear evolution `z'(t)=-Hz(t)`, `z=p+q`, with `p=Pz`, `q=Qz`. Because H is bounded below and D is positive selfadjoint, all expressions below extend as mild solutions:

`p'=-Ap-Bq`, `q'=-B*p-Dq`.

Eliminate q by variation of constants:

`q(t)=e^{-tD}q(0)-int_0^t e^{-(t-v)D}B*p(v) dv`, and hence

`p'(t)=-Ap(t)-B e^{-tD}q(0) +int_0^t K(t-v)p(v) dv`,

where

`K(t)=B e^{-tD} B* >=0`, `rank K(t)<=2`.

For every low v and t>0, `(-1)^j d^j <v,K(t)v>/dt^j >=0`: the scalar memory responses are completely monotone because D is positive. The memory kernel can be nonzero even though the **positive L carrier** itself has no P–Q cross. Thus in the spectral observer partition, the residual hidden-memory channels are precisely the **completed polar channels**, not a fictitious bath.

Take the Laplace transform:

`int_0^infty e^{-zt} K(t) dt =B(D+z)^{-1}B*` for `z>=0`,

and at `z=0`:

`int_0^infty K(t)dt=BD^{-1}B*`.

Thus

`S=A-int_0^infty K(t)dt`,

and for a finite observation horizon T the missing tail is positive with

`0<=int_T^infty K(t)dt = B D^{-1}e^{-TD} B* <= ||B||²/d * e^{-d T} I`.

With the genuine first-prime gap and coupling bounds, this is strictly below `(121/64)e^{-9 T/16}`. It is **not** a physical work extraction bound. The Nature paper experimentally observes bath memory; here we derive an exact operator identity for mathematical high-sector dynamics.

## 3. HM-02 — dyadic, rational, finite-time response telescope (PAPER, executable exact finite models)

Continuous exponentials need not be evaluated. For any rational step h>0 set

`R_h=(I+hD)^{-1}`. Since D>=dI, `0<R_h <= (1+hd)^{-1}I`.

The operator-geometric identity holds even when D is unbounded:

`h sum_(j=1)^infinity R_h^j =D^{-1}`.

Define a finite **delayed response certificate**

`X_N=h sum_(j=1)^N B R_h^j B*`, `S_N=A-X_N`.

Each `K_j=B R_h^j B*` is positive semidefinite, and successive errors have exact identities

`0<=S_N-S = B D^{-1}R_h^N B* <= [||B||²/d] (1+hd)^(-N) I`.

For the **authentic original source**, choose `d=9/16`, `h=16/9`. Then `R_h<=I/2` and the source-pinned polar norm gives

**`S_N - (121/(64*2^N)) I <= S <= S_N`.**

At N=12 the signed short's error in this **mathematical source-conditional** scheme is less than `121/262144` (~0.000461579); at N=24 less than `121/1073741824` (~1.127e-7). The number of *iterations* is finite and explicit, independent of the dimension of the hidden spectral Q-space. In contrast, actually evaluating `B R_h^j B*` from the authentic source remains an open source-access/algorithmic task. This is **not** a finite physical measurement protocol performed in Nature's experiment, nor evidence the SUCC sign is positive.

A claimed finite sign certificate is valid only if each K_j has **certified actual-source** enclosures. If `K_j≈Ktilde_j` in Loewner with operator error epsilon_j, then the effective two-sided original-S Schur enclosure widens additionally by `h sum epsilon_j` in both directions. Without those error controls, just computing a plausible K_j and a pretty PSD matrix has no proof authority.

**Strict sign conditions:** If `S_N - tail*I >0`, the true original S is positive. If some vector has `<v,S_N v><0`, the true original S is negative on that vector, provided A/B/D and K_j have been faithfully authenticated. With singular positive S, the bounds can straddle 0 at every finite N. Exact finite toys can sometimes resolve zero because their tail bound is attained; this does not imply a general zero-sign algorithm.

## 4. HM-03 — two different observer choices expose different memory

If P is a reducing spectral projection of the **positive L alone**, then `PLQ=0` and the positive carrier evolves without P–Q memory. Consequently **the same source-generated spectral partition that eliminates positive Gamma/FUCC gluing also removes positive Gamma/FUCC memory observable through that partition**. Its residual complete-signed memory comes only from the completed polar rank-two coupling.

If P is a nonreducing *spatial* observation projection (e.g. actual finite-cell apparatus), `PLQ` need not vanish and hidden Gamma/FUCC memory becomes observable in a Mori kernel. One then pays larger B/continuum coupling and needs a separately certified positive Q-block. This is a lawful tradeoff, not a contradiction. A finite rational 2x2 source has `L=diag(2,3)`, `P=diag(1,0)` (memory zero); after rotating the positive L to `[[2,1],[1,2]]`, keeping the same P, the high coupling is 1 and `K(0)=1`.

The Nature experiment exploits a measurement interface under which hidden bath variables do return information to the tracer. It does **not** demonstrate the spectral projection of SUCC's positive jump L, or the value of any actual Suzuki K_j.

## 5. HM-04 — concrete delayed information gain (classical finite Gaussian model)

Let X0,Y,E be independent centered Gaussians with variances 1,1,nu>0. The measured tracer is `M0=X0`; later `M1=X0+gY+E`. Before observing M1, the hidden variance remains 1 despite knowing M0. After observing both,

`Var(Y|M0,M1)=nu/(g²+nu)`,

so additional conditional mutual information is `(1/2)log(1+g²/nu)` nats. For g=1,nu=1, conditional hidden variance halves. For g=0 the pair gains exactly zero hidden information. This is a clean mathematical model of *delayed access to hidden degrees*, not the Nature apparatus, not derived work, not a zeta theorem. Replaying a single source observation as a new E does not create a new Gaussian measurement.

## 6. HM-05 — two delayed memory readings do **not** determine a hidden Schur sign (REFUTED SHORTCUT)

Define a finite positive hidden bath D and B, set `R=(I+D)^(-1)`, and let the lag-read sequence be `k_j=B R^j B*` for integer j>=0. Two **different** rational positive baths yield exactly the same first two readouts:

- **Bath A:** one high mode `D_A=[1]`, `B_A=[1]`. Its k0=1, k1=1/2, and inverse response `B_A D_A^-1 B_A*=1`.
- **Bath B:** two high modes `D_B=diag(37/13, 73/127)`, `B_B=[3/5,4/5]`. It has k0=1, k1=1/2 *exactly*, while its true inverse response is `3349/2701 >1`.

Both D_A and D_B obey `D>=9/16`; the latter's smaller eigenvalue `73/127 >9/16`. Let A_low=`9/8`. Then

`S_A=9/8-1=+1/8`, while `S_B=9/8-3349/2701=-2483/21608<0`.

**Hence two equally authentic-looking initial memory readouts, even with a common strictly positive hidden gap, can imply opposite eventual signed Schur verdicts.** This is an exact *declared finite-source* no-go; it is not the original Suzuki source. The third and fourth moments distinguish the baths. In a declared bath of at most two rational contraction eigenmodes, four exact consecutive moments reconstruct its spectrum and coupling weights by a 2x2 Hankel/Prony calculation (provided the Hankel rank and rational-root checks succeed). For an infinite high sector the finite-bath support assumption is a massive open obligation; no number of moments may be silently promoted to exact original-source inverse response.

**Hankel positive:** for any source finite bath with R positive, the moments k_j define PSD Hankel matrices since `sum_{i,j}v_i v_j k_{i+j}=||sum_i v_i R^i B*||²>=0`. This positivity reflects the passive high bath, NOT positivity of the *signed* short `S=A-BD^-1B*`.

## 7. HM-06 — precise next original-source experiment

The identity in Sections 2–3 is the right route for the SUCC first-window source, but it still depends on the unconstructed authentic spectral low projector P and source-calibrated queries of `B(I+(16/9)D)^(-j)B*`. These are *not* available as mere cached Nature-style double measurements. An E must legally construct the observation apparatus or analytic source computation. Specific next targets:

1. Independently certify a **true-source spectral gap** near the jump cutoff 7 and source spectral projector `P`. A 453-dimensional upper rank bound alone is not an eigenvalue enclosure. Alternatively use the **explicit 453-cell projection** as P; this is constructible immediately but `PLQ != 0`, losing the source rank-two cross and necessitating a separate bound on the positive jump cross B.
2. Use rigorous positive-shift **source Galerkin** solves on `D+h^-1`, in both polar parity sectors, including a residual-to-continuum norm and original source Gamma/prime tails. The bounded gap makes such solves stable in the norm appropriate to H. **Finite-degree Galerkin error without a certified residual is not a proof.**
3. Recover the two scalar polar high responses via signed rank-one Sherman–Morrison *without accessing off-line zero coordinates*. Determine exact source Schur sign only when the resulting low rational Loewner enclosure has strict margin.
4. If a true-source observer protocol is proposed, distinguish its **actual measured event provenance** from an analytically generated mathematical certificate; both may be lawful but are not interchangeable.
5. No single-radius result proves all-support Weil positivity/RH. The source-honest radius telescope must keep active genuine prime powers, negative contact/poles, and all cross-window interactions.

## 8. Source and proof authority

| ID | Statement | Status | Strongest next falsifier |
|---|---|---|---|
| HM-01 | Eliminating high D yields positive completely monotone Mori kernel, Laplace transform equals source Schur response | CLASSICAL PAPER under source block and gap; tested exactly in finite matrices | Bad sign, missing q(0) term, applying H as equilibrium Markov generator |
| HM-02 | Backward-Euler discrete memory gives `S_N -121/(64*2^N)I<=S<=S_N` at original a=1/2 | SOURCE-CONDITIONAL PAPER; exact Fraction coefficient proof; authentic SHA gate | Wrong `||c||` normalizer, missing polar s, fake high spectral gap, fictitious projector |
| HM-03 | Spectral partition of L has no positive-L memory; signed H retains polar-only memory | CLASSICAL/FINITE PROVED | Claims Nature's bath equals L, or arbitrary P commutes with L |
| HM-04 | Two Gaussian reads expose hidden Y; one read does not | CLASSICAL FINITE; covariance checked in Fraction | Noise dependence forged as independent, claims of physical work |
| HM-05 | Two equal temporal memory samples can hide opposite signed S; 4 recover finite 2-mode surrogate | EXACT RATIONAL COUNTERMODEL, not original source | Unstated finite-bath rank inference or source identification |
| HM-06 | Original source completed time-resolvent values and low Schur sign | OPEN | Need source-pinned P and high source resolvent with rigorous error |
| Global Weil positivity / RH | NOT PROVED | Actual original source at all radii with domain/cofinal transport |

### Reproduction

```
python -m unittest discover -s tests -p 'test_hidden_memory_schur.py' -v
python scripts/hidden_memory_schur_probe.py --verify
python scripts/hidden_memory_schur_probe.py --source --verify
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

Isolated fixture: **40 discovered / 35 passed / 5 skipped source integration**. The dedicated CI must execute and pass all 40, **zero skips**, against the original frozen source under Python 3.10/3.13. No original analytic spectral projector or true-source temporal K_j is computed. No merge, publication or RH claim.

## 9. HM-07 — an **explicit 453-cell observer** with finite high gap, no spectral eigenbasis needed

The spectral partition P in HM-01–02 is source-canonical but not yet computationally constructed. There is a **different** mathematically explicit, source-faithful decomposition already latent in JS-02. Let `E_N` be ordinary orthogonal averaging onto the N=453 equal subinterval cells on the primitive interval I=(-1/2,1/2), with normalized indicators `e_i=sqrt(N)1_cell_i`. This is a fully specified, actual finite-rank mathematical observation algebra with no spectral-eigenvector search. The source-proof first-prime Gamma cell inequality from JS-02 establishes

`<F,Lplus F> > 7||F||²` for every `F` with `E_N F=0`.

The *original full signed* high cell block `D_cell=(I-E_N)H(I-E_N)` thus has

`D_cell > (7-B_a) I > (9/16)I`,

where the authentic negative source bound `B_a<103/16` includes full negative contact/prime potential and the completed sinh polar loss. Importantly `E_N` does **not** commute with Lplus. Consequently its positive Gamma+FUCC memory is generally nonzero and its low/high coupling need not have rank two. Claiming the spectral-polar-only cross for E_N is a **REFUTED TYPE MISMATCH**.

### HM-07a — source upper multiplier with actual discontinuous cell tests

For r=|xi|>=1, split the *authentic* nonnegative Gamma OU symbol at true `d_j=4j+1<=2r`. Its low-j sum is at most `5+log(2+r)` using `4/d_j<=1/j` for j>=1. Its positive high-j tail is at most `16r²[(2r)^(-3)+(8(2r)²)^(-1)]<=5/2`. The only authentic p=2 FUCC jump symbol is at most `4w_2<2`. Therefore the **complete positive source** symbol satisfies

`0<=hplus(xi)<10+log(2+r)<=10+8r^(1/4)` for r>=1.

For 0<=r<=1, the Gamma symbol is increasing in r and the genuine p=2 trigonometric component is also increasing because `r log2<1<pi`; the previous estimate at r=1 gives `hplus<18`. These are simple analytic source bounds, not a reconstructed fake Euler product.

The normalized interval indicator has exact unitary Fourier magnitude

`|Fhat(e_i)(xi)|²=(N/(2pi)) |2sin(xi/(2N))/xi|² <=(2N)/(pi xi²)`,

and `||e_i||²=1`. Its jump discontinuities are legitimate on the **logarithmic Gamma form domain**: for r>=1, `hplus²<200+128 sqrt(r)`, so the high tail is integrable against `r^-2`. Consequently e_i even belongs to the operator domain of the positive Dirichlet jump generator Lplus (zero-exterior Fourier multiplier, compressed to I). Direct integration and pi>3 give the all-rational uniform estimate

`||Lplus e_i||² <324+(4N/pi)(200+256)<324+608N`.

The original bounded negative potential and **both** rank-one poles satisfy

`||H-Lplus||<=M+2(||c||²+||s||²)<51/8+48/23<9`.

Thus by `(x+y)²<=2x²+2y²`

`||H e_i||²<810+1216 N`.

The true cross block `B_cell=E_N H (I-E_N)` obeys the exact Hilbert–Schmidt upper

`||B_cell||² <= sum_i ||H e_i||² <N(810+1216N)`

`=249901074` at N=453. This is large but finite, and it is derived from the source's actual analytic Gamma/prime symbol, contact, and completed poles. No spectral projector, finite-matrix fitted source, or zero input is required.

### HM-07b — dyadic no-projector memory response bound

With `h=16/9` and `R_cell=(I+h D_cell)^-1<=I/2`, define

`S_cell,k = E_N H E_N -(16/9)sum_(j=1)^k B_cell R_cell^j B_cell*`.

Applying HM-02 with the authentic N=453 source bounds gives the **explicit-source-observer** estimate

**`S_cell,k - 444268576*2^(-k)I <= S_cell <= S_cell,k`.**

At k=64 the absolute operator error is strictly below `2.41e-11`, **provided the k delayed-response matrices are evaluated accurately against the true source**. The constant identity `(16/9)*453*(810+1216*453)=444268576` is exactly checked in Fractions. This is a source-conditional mathematical convergence/budget theorem; we have neither computed the 453x453 original low block nor the high shifted-resolvent memory samples. The finite-cell projectors and their source definitions are explicit; the actual source *values* remain an unresolved certified-integration task.

**Trade-off:** the source-*spectral* P has hidden rank-≤2 polar B and a small error constant 121/64 but unknown eigenvectors; the explicit *spatial* E_N has 453 known observation functions and a huge but explicit error constant 444268576, and necessarily retains Gamma/FUCC high memory. This trade-off is structurally aligned with the Nature experimental observation that choosing an accessible limited interface exposes environmental memory. It does not establish that laboratory work, heat, or physical information has anything to do with the signed Weil form.

**Next effective gate:** compute and certify `E_NHE_N` from the original nonlocal jump kernel and original two poles; then construct certified positive-shift Q_cell solves with two-sided residual errors, rather than merely postulating the `BR^jB*` observations. In particular avoid calling a finite numerical matrix an authentic source projector or creating false independence between repeated measurements.

**HM-07 claim:** SOURCE-CONDITIONAL PAPER upper and exact rational coefficient; dedicated original-source source hash and inherited JS-02 rank/gap packet are replayed. Actual true-source cell matrix, effective Green resolvent and original sign: OPEN.

## 10. HM-08 — arithmetic resonance-tuned observer clocks: 453 vs 642 cells

The 453-cell partition in HM-07 was chosen to satisfy the genuine Gamma high-energy estimate, **without reference to prime2's phase**. An unexpected arithmetic feature is that its source SUCC coordinate grid also almost aligns with the one genuine active FUCC lag `b=log2`. Define the finite-cell basis `e_i=sqrt(N)1_[i/N,(i+1)/N]` (translated to I). For any primitive `F=sum_i f_i e_i`, zero-extended, write `m=floor(Nb)`, `t=Nb-m` (0<t<1). The **exact source-defined** lag correlation is

`<F,T_b F>=(1-t) sum_i f_i f_(i+m)+t sum_i f_i f_(i+m+1)`

(with out-of-range indices zero). Thus the genuine prime2 quadratic is exactly a two-band sparse integer SUCC shift, not an arbitrary dense operator. With `k=round(Nb)` and `epsilon=|Nb-k|`, each one-step shift is a contraction on the finite vector space, so

`|<F,T_bF>-sum_i f_i f_(i+k)| <=2 epsilon||F||²`.

The authentic source weight `w_2=log2/sqrt2<1/2` then gives the strict **original-prime-only** signed energy bound

`|Q_prime(F') - (-2w_2 sum_i f_i f_(i+k))| <2 epsilon||F||²`.

Using the pinned original SHA's rational atanh series for log2 (or a separate 40-term rational atanh enclosure) gives **exact strict rational phase statements**

`314-1/200 <453 log2<314`,

`445 <642 log2<445+1/2000`.

Therefore the 453-cell prime2 channel is within **1/100** of the 314-cell SUCC translation in operator-form norm, whereas the 642-cell prime2 channel is within **1/1000** of its 445-cell SUCC translation. The latter is a nearly exact prime-FUCC/int-SUCC resonance with just **two** actual nonzero source shift bands; the small second band's sign/weight cannot be silently dropped in a proof. The Fourier Gamma jump, original contact and both completed polar contributions remain nonlocal and are not controlled by the prime-only approximation.

Because the existing Gamma cell lower bound is `mu76(1-76/(3N))²`, it **improves** whenever N>=453. Hence the 642-cell mathematical observer retains the same signed high gap >9/16. The source-coupling Hilbert–Schmidt budget scales conservatively as `N(810+1216N)`; at N=642, it equals exactly 501711444, so the signed memory-tail bound is

**`S_642,j - 891931456*2^(-j) I <= S_642 <= S_642,j`.**

This roughly doubles the already conservative high-memory budget while improving the prime phase alignment by almost an order of magnitude. Inverse-Ramsey framing: a physically/source-legal finite partition can be selected for both **high spectral access** and **genuine prime-clock synchronization**, without declaring an independent fake-6 jet or importing zeta zero locations.

**Scope & Falsifier:** For each N the correct phase may land on either neighboring integer shift. We authenticate its direction and interval from original source log2, never treat a decimal rounded value as exact. The normalized cell carrier lies in the closed primitive log-Gamma form domain but requires approximation by smooth test primitives for direct original Weil-core statements. Its actual original Gamma/pole/contact low matrix, shifted resolvents, and all-radii sign are still uncomputed. This is SOURCE-CONDITIONAL PAPER arithmetic-interface result plus an independently executable exact-rational synthetic observation computation; **not** an original-source signed positivity proof.
