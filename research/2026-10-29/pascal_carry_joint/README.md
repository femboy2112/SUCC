# OPERATION SOURCE-LOCKED JOINT SHEET
## Pascal posterior × Oily packet × original Green future clock × selected BBP carry

**Date:** 2026-10-29. **Status:** research-only, proposed stacked draft child of SUCC PR #370, pinned at `4d4d49b575b476cc33f762d2b6a7fd6d1b924655`. The parent is stacked on #369/#367. Sibling PR #368 supplies the accepted order-statistic representation; #369 proves its Green-mixture disintegration; #370 supplies the original-source Pascal thinning and signed inverse. No original BBP source, seed, archive, old theorem, production code, or workflow is modified. **No base-16 normality of π or RH is proved.**

## Verdict in one paragraph

A **source-preserving, seed-sensitive joint observation model exists**, not only two matching scalar marginals. We explicitly retain the authentic Green future index `L`, the positive original four-pole Laplace microstate `Z`, the authentic two-geometric Oily packet grade `P`, a *declared* Pascal Bernoulli outcome history `B`, and a terminal mark containing the **literal integer BBP carry** and real-circle phase at the **actual original-source time** `n+L+#failures`. The positive projections reproduce the already authenticated Green/Oily and Pascal laws; the mark is computed from the original unmodified recurrence with `U_0=0`. Finite depth is exact rational arithmetic with an explicit exponentially small tail certificate. A coherent alternative seed preserves every positive weight but has all its carries equal to 15. The resulting conditional phase is an exact martingale with strict information gain, though this does not make the deterministic π orbit random. Forgetting the labels produces a third-order filter `15S/((16-S)(2-S)^2)` whose signed inverse is exact; the forgotten coarse kernel **loses** Oily's golden interior fixed point. **The missing theorem remains an arithmetic estimate for the actual zero-selected signed phases.**

## 1. Source passport and conservation contracts

For integers `t>=1`, the original four signed rational poles are

\[
 r(t)=\frac4{8t-7}-\frac2{8t-4}-\frac1{8t-3}-\frac1{8t-2}>0,
 \quad U_0(s)=s,\quad U_t(s)=16U_{t-1}(s)+r(t).\tag{JC-1}
\]

The authentic π-selector is `s=0`. Its unwrapped values are rational, and its *literal* carry (including the exceptional first step) is

\[
 x_t(s)=\{U_t(s)\},\qquad
 \kappa_t(s)=\left\lfloor16x_{t-1}(s)+r(t)\right\rfloor,\quad
 x_t=16x_{t-1}+r(t)-\kappa_t.\tag{JC-2}
\]

This is more data than the circle phase `e(hU_t)` alone; keep the integer lift and the carry as an explicit mark. Here `e(y)=exp(2πiy)` and `h` is a nonzero integer unless indicated otherwise. The source positive function is

\[
 Q(z)=4-2e^{-3z}-e^{-4z}-e^{-5z}>0\ (z>0),\quad
 R(a)=\int_0^\infty e^{-az}Q(z)\,dz,\quad R(8t-7)=r(t).\tag{JC-3}
\]

The original positive forcing probability is
\[\mu_t(dz)=e^{-(8t-7)z}Q(z)\,dz/r(t).\]
It depends on the four original poles and source time, but not on the initial BBP seed. No physical stochastic dynamics is implied by declaring a probability measure on these microstates.

## 2. Exact triangular Bayesian field, including real feedback and flat order

At a fixed authentic time `t>=1`, sample `Z~mu_t`. **Additional declared observer:** conditional on `Z=z`, observe `t` independent Bernoulli **failure** bits with probability `p(z)=1-e^{-8z}`. After an observed prefix of length `m` with `k` failures, set

\[
 D_{t;m,k}=\int_0^\infty e^{-(8t-7)z}Q(z)
                 e^{-8(m-k)z}(1-e^{-8z})^k\,dz
 =\sum_{i=0}^k(-1)^i\binom ki r(t+m-k+i),\quad0\le k\le m\le t.\tag{JC-4}
\]

Every `D>0`. The probability of *each particular ordered word* with `k` failures is `D_(t;m,k)/r(t)`. The complete Pascal row is
\[
 \Pr(K_m=k)=\binom mk D_{t;m,k}/r(t),\quad
 D_{t;m,k}=D_{t;m+1,k}+D_{t;m+1,k+1}.\tag{JC-5}
\]

The posterior probability of a failure at the next step is `D_(t;m+1,k+1)/D_(t;m,k)`; success uses `D_(t;m+1,k)/D_(t;m,k)`. These add to one. This is **exact recursive field updating**: the source posterior is
\[
 \mu_{t\mid m,k}(dz)=
 \frac{e^{-(8t-7+8(m-k))z}Q(z)(1-e^{-8z})^k}{D_{t;m,k}}\,dz.\tag{JC-6}
\]

The update is genuinely nontrivial. Let `a=E_mu_t p(Z)` and `v=Var_mu_t p(Z)`. From the four authentic poles,
\[
 a=1-\frac{r(t+1)}{r(t)},\quad
 v=\frac{r(t)r(t+2)-r(t+1)^2}{r(t)^2}>0.\tag{JC-7}
\]

Strict inequality comes from strict log-convexity of a non-point-mass positive Laplace transform. After observing a failure, the next failure probability rises to `a+v/a`; after a success, it falls to `a-v/(1-a)` (provided another trial remains). **However**, two words with identical `(m,k)` have the same likelihood and posterior: Bayesian conditioning commutes, and all Pascal diamonds are flat in path *order*. This is a counterexample to inferring nonzero history-order curvature from posterior feedback alone. The earlier SUCC genuinely nonflat reinforcement models remain separate.

## 3. Terminal original carry and phase: a canonical marked Doob triangle

At the end of this declared `t`-trial observer, let `J=K_t`, and mark the genuine arithmetic time `T=t+J` with `(kappa_T(s), x_T(s), e(h U_T(s)))`. **No arithmetic recurrence is randomized:** the only random element is which one of its already determined values the instrument observes.

Given a prefix `(m,k)`, the remaining failure count `j=0,...,t-m` has the strictly positive exact law
\[
 \boxed{\Pr(J=k+j\mid m,k)
 =\binom{t-m}{j}\frac{D_{t;t,k+j}}{D_{t;m,k}}.}\tag{JC-8}
\]

All these masses are rational and sum to one. For any preassigned bounded terminal marks `z_j` (including `z_j=e(hU_(t+j)(s))`), define the backward signed message
\[
 A_{m,k}=\sum_{j=0}^{t-m}\binom{t-m}{j}D_{t;t,k+j}\,z_{k+j},\qquad
 M_{m,k}=A_{m,k}/D_{t;m,k}.\tag{JC-9}
\]

The same elementary Pascal gluing holds *simultaneously* for both channels:
\[
 A_{m,k}=A_{m+1,k}+A_{m+1,k+1},\quad
 D_{m,k}=D_{m+1,k}+D_{m+1,k+1},\quad
 M_{m,k}=p_S M_{m+1,k}+p_F M_{m+1,k+1}.\tag{JC-10}
\]

With the actual phase marks, `M_m=E[e(hU_(t+J)(s)) | first m outcomes]` is the **unique conditional-expectation martingale** on the specified probability space; `M_t=e(hU_(t+J)(s))` is its terminal boundary. Its exact orthogonal-increment identity is
\[
 \sum_{m=0}^{t-1}E|M_{m+1}-M_m|^2=1-|\Theta_t(h;s)|^2,\quad
 \Theta_t=\sum_{j=0}^{t}q_t(j)e(hU_{t+j}(s)).\tag{JC-11}
\]

The phase mark is **not independent** of the positive latent microstate when the phases are not all equal: conditional on `Z`, its expectation is the Bernstein polynomial
\[
 \sum_{j=0}^{t}\binom tj p(Z)^j(1-p(Z))^{t-j}z_j.\tag{JC-12}
\]

Since `p(Z)` has full interval support `(0,1)` and the Bernstein basis is unique, (JC-12) is constant iff **all** `z_j` are equal. For the genuine zero-seed `t=1,h=1`, the two phases have distinct fractional residues `2/15` and `1076/4095`; the exact marginal probabilities are `530/12831` and `12301/12831`. Hence this selected signed/positive joint coupling is **provably nonfactorizing already at a finite source time**. Nonfactorization and martingale information gain are **not** signed Cesàro cancellation.

The same formula with the mark `(literal carry, fractional phase)` is a finite exact **group-algebra-valued** posterior; no numerical complex root approximations are needed. The code preserves the full joint carry and phase labels and verifies (JC-10) coefficientwise in rational arithmetic.

## 4. Exact full Green × Pascal × Oily × BBP selected-source coupling

Now include the **other** original source route. For every `n>=0`, define the original positive Green tail
\[
 T_n=\sum_{\ell\ge1}16^{-\ell}r(n+\ell)
  =\int_0^1 x^{8n}R_P(x)\,dx,\quad
 R_P(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}.\tag{JC-13}
\]

Choose a labelled future-index `L=ell>=1` with probability `p_(n,ell)=16^(-ell)r(n+ell)/T_n`, and conditional on `L=ell`, sample `Z~mu_(n+ell)`. Let `X=e^(-Z)`. By the independently established exact Green disintegration (#369), `X` has precisely the **source-authentic** accepted second-largest-uniform law of #368:
\[
 \Pr(X\in dx)=x^{8n}R_P(x)\,dx/T_n.\tag{JC-14}
\]

Next, conditionally on `X=x`, sample the **original** Oily two-geometric packet grade `P=K_1+K_2` with parameters
\[
 u(x)=x-x^2/2,\quad v(x)=x^2/2,\quad
 E[z^P|X=x]=\frac{(1-u)(1-v)}{(1-uz)(1-vz)}.\tag{JC-15}
\]

**In parallel**, at original time `t=n+ell`, apply Section 2's declared `t`-trial Bernoulli observer to the *same* positive microstate `Z`. Assume the Oily packet draws and the Bernoulli trials conditionally independent **given `Z`**; this is an explicit model choice, not a theorem of physical uniqueness. With `J=#failures`, mark the true BBP time `n+L+J` by its *computed original* `(carry,phase)`.

Thus one jointly labelled model has all of the following exactly: the original Green and four-pole Laplace marginals, #368's accepted rank/order-statistic and Oily packet marginals, #370's rational Pascal sensor conditional distribution, and the actual zero-seeded rational BBP phase/carry **on each chosen arithmetic time**. Specifically its `(L,J)` marginal is
\[
 \boxed{\Pr(L=\ell,J=j)
 =\frac{16^{-\ell}r(n+\ell)}{T_n}\,q_{n+\ell}(j),\quad
 \text{mark}=\bigl(\kappa_{n+\ell+j}(0),\{U_{n+\ell+j}(0)\}\bigr).}\tag{JC-16}
\]

This is **existence of a source-preserving marked coupling relative to the declared observer**. It is not a canonical deterministic microstate history, an intertwiner identifying the sample path with π digits, or a proof of sign cancellation. There may be other couplings with the same individual marginals; our conditional-independence convention is declared.

### Rigorous finite rational certificates, with a uniform tail bound

For depth `D>=1`, restrict `1<=L<=D`, renormalize with
\[T_n^{(D)}=\sum_{\ell=1}^D16^{-\ell}r(n+\ell)\in\mathbb Q_{>0}.\]
Every finite `(L,J,carry,phase)` probability is now **exactly rational** (phase represented by its rational residue, not a floating complex approximation). Positive `r` is strictly decreasing; hence
\[
 0<T_n-T_n^{(D)}\le\frac{r(n+D+1)}{15\,16^D},\qquad
 \boxed{\Pr(L>D)\le\tau_{n,D}:=
 \frac{16^{1-D}}{15}\frac{r(n+D+1)}{r(n+1)}.}\tag{JC-17}
\]

Conditioning on `L<=D` changes **any** bounded-absolute-value-1 joint observable's expectation by at most `2 tau_(n,D)`. This bound is uniform over both the actual seed and every counterfeit seed, because truncating the Green label cannot add a signed phase estimate. Finite exact tests also confirm the Green conditioning recurrence
\[T_{n+1}^{(D-1)}=16T_n^{(D)}-r(n+1).\]

## 5. A new three-pole coarse filter: exact coefficients, exact signed inverse

The limit of the Green future clock is geometric with mass `g_ell=15/16^ell`; conditionally, #370's Pascal grade approaches `w_j=(j+1)/2^(j+2)`. **Only in the limit** are the two labels independent. Their summed total offset `R=L+J>=1` then has generating function
\[
 \boxed{K(z)=\frac{15z}{16-z}\frac1{(2-z)^2}
 =\frac{15z}{(16-z)(2-z)^2}.}\tag{JC-18}
\]

The exact coefficients and mean are
\[
 \boxed{k_r=\frac{15}{196}\left(16^{-r}+(7r-1)2^{-r}\right)>0\quad(r\ge1),
 \quad\sum k_r=1,\quad E R=46/15.}\tag{JC-19}
\]

This composition has an **authentic 16-Green pole** and a **double Oily 2-pole**. Let `S z_t=z_(t+1)` be the forward shift on bounded sequences and `Xi_n^(0)=(K(S)z)_n=sum_(r>=1) k_r z_(n+r)`. Its finite algebraic inverse obeys
\[
 \boxed{64\Xi_n^{(0)}-68\Xi_{n+1}^{(0)}+20\Xi_{n+2}^{(0)}-\Xi_{n+3}^{(0)}=15z_{n+1}.}\tag{JC-20}
\]

This is the exact polynomial identity `(16-S)(2-S)^2K(S)=15S`, valid for **every** bounded signed or complex sequence, including original BBP phases and coherent counterseeds. It is an invertible *transport*, not a new decay theorem.

For the actual full positive-source joint at time `n`, let `K_n` be the law of `R=L+J`. Comparing the original Green law to its geometric limit, and using #370's `TV(q_t,w)<=22/t` for `t>=3`, gives for every integer `n>=3`
\[
 \boxed{\mathrm{TV}(K_n,k)\le
 \epsilon_n:=\frac{256}{225(8n+1)}+\frac{22}{n+1}.}\tag{JC-21}
\]

**Proof of the source-specific first term (all n):** Write `a=8n+1`, `b_ell=r(n+ell)/r(n+1)<=1`, `g_ell=15/16^ell`. The true Green law is `p_ell=g_ell b_ell/B`, `B=sum g_ell b_ell>=15/16`. The original four-pole positive carrier has `E_mu_a Z<2/a` (#367), so `1-b_ell=E(1-e^(-8(ell-1)Z))<16(ell-1)/a`. Since `E_g(L-1)=1/15`, `1-B<16/(15a)` and `TV(p,g)<=(1-B)/B<=256/(225a)`. Coupling the conditional Pascal law to `w` costs at most `22/(n+1)` by #370. Projection `(L,J)->L+J` does not increase TV. No digit randomness was used.

Let the true full source-marked readout be `Xi_n(h;s)=sum_r K_n(r)e(hU_(n+r)(s))`, and its exact rational depth-D version `Xi_(n,D)` obtained by the labelled finite mixture. For every bounded terminal sequence `z`, uniformly over all initial seeds,
\[
 |\Xi_n-(K(S)z)_n|\le2\epsilon_n,\qquad
 |\Xi_{n,D}-(K(S)z)_n|\le2(\epsilon_n+\tau_{n,D}).\tag{JC-22}
\]

Therefore the **certified finite source-selected signed recovery** is
\[
 \boxed{\left|z_{n+1}-\frac{64\Xi_{n,D}-68\Xi_{n+1,D}+20\Xi_{n+2,D}-\Xi_{n+3,D}}{15}\right|
 \le\frac2{15}\sum_{i=0}^3|c_i|(\epsilon_{n+i}+\tau_{n+i,D}),\quad
 (c_0,c_1,c_2,c_3)=(64,-68,20,-1).}\tag{JC-23}
\]

This tends to zero as `n,D->infinity` with `D` growing slowly. In particular, this *does* retain the original selected phase and its literal carry mark at every finite source time. It provides **no bound on the size of `Xi_n` itself**, and the recovery remains valid for coherent non-normal source phases.

For normalized time means, since `E_k(R-1)=31/15`, the limiting filter's average differs from the *shifted* original sequence by at most `62/(15N)` for every `N>=1`; the actual full source adds at most `(2/N)sum_(n=L)^(L+N-1)epsilon_n`. Thus the new source-smoothed Weyl condition is **equivalent** to, not weaker than, original selected Weyl cancellation. Do not promote this equivalence to a π-normality proof.

### Essential provenance/identity loss under coarse-graining

The original marked two-geometric packet PGF `G(z)=(2-z)^-2` has the interior golden fixed point `q*=phi^-2`. But for **every** real `0<z<1`,
\[
 \frac{K(z)}z=\frac{15}{(16-z)(2-z)^2}<1.\tag{JC-24}
\]

Hence the coarse total-offset PGF `K` has **no interior fixed point**, only the boundary fixed points 0 and 1. In particular its value at `q*` is *below* `q*`. Thus **golden survives as a marked Oily-grade selection but is destroyed by forgetting the Green/Pascal labels**. The same example still retains an invertible signed shift filter. A numerical equality of gamma/golden constants and a coarse invertible filter do **not** imply identity of mathematical sources or preservation of source-specific selection rules.

## 6. Circle microfield and the actual signed phase: a quantitative uniform bridge

The Oily endpoint law also defines the continuous, uniformly convergent lacunary circle observable
\[
 \boxed{F_h(x)=\sum_{j\ge0}\frac{j+1}{2^{j+2}}e(h16^jx),\qquad
 (2I-K_{16})^2F_h=e(hx),\quad (K_{16}f)(x)=f(16x).}\tag{JC-25}
\]

`F_h` is **not** an average over the deterministic π orbit. It is a named observable of an arbitrary circle input `x`. Combining PR #370's actual `q_t` total-variation bound with the true forced-lag formula
\[
 U_{t+j}(s)=16^jU_t(s)+\sum_{i=1}^j16^{j-i}r(t+i),\qquad
 0<\sum_{i=1}^j16^{j-i}r(t+i)\le\frac{16^j-1}{15}r(t+1),\tag{JC-26}
\]

we obtain, for each `t>=3`, nonzero integer `h`, and any integer cutoff `J>=0`, the **explicit ALL-SEED rational certificate**
\[
 \boxed{|\Theta_t(h;s)-F_h(U_t(s))|\le
 \frac{44}{t}+\frac{44|h|}{105}\,r(t+1)
     \sum_{j=0}^{J-1}\frac{j+1}{2^{j+2}}(16^j-1)
      +\frac{J+2}{2^J}.}\tag{JC-27}
\]

Here `2π<44/7` and the second term is precisely `(44/7)|h| r(t+1)/15` times the exact finite sum; `44/105= (44/7)/15`. The finite frequency cost has the exact rational form
\[
 \sum_{j<J}w_j(16^j-1)
 =\frac{1+(7J-1)8^J}{196}-1+\frac{J+2}{2^{J+1}}.\tag{JC-28}
\]

With `J=floor(log_16((8t+1)^2/|h|))` when the ratio is at least one, the original source estimate `r(t+1)<=15/(8t+1)^2` yields for **each fixed nonzero h**:
\[
 \sup_s|\Theta_t(h;s)-F_h(U_t(s))|=O_h(t^{-1/2}\log t).\tag{JC-29}
\]

This explicitly connects the exact finite source-conditioned Pascal observation to a real-circle wavefront **at the original selected BBP phase**, without erasing the forcing or seed. The Hölder loss is structurally necessary for a uniform generic comparison, not a proof of π-normality.

The modulus is sharp at the source wavefront: the same split proves `|F_h(x+delta)-F_h(x)|=O_h(|delta|^(1/4)(1+|log|delta||))`, while for `delta_j=1/(2|h|16^j)`,
\[
 |F_h(\delta_j)-F_h(0)|\ge 2w_j=\frac{j+1}{2^{j+1}}.\tag{JC-30}
\]

Thus `F_h` is Hölder for every exponent `<1/4` and is **not Hölder `1/4` at 0**. This 1/4 exponent comes from the authenticated grade decay `2^-j` versus arithmetic phase frequency `16^j`, not from a physical fractal-dimension claim.

### Haar seed-average diagnostics, with the correct no-go

For `h!=0`, the frequencies `h16^t` are distinct. Haar-integrating over *random initial seed* `s` gives an exact source-sensitive finite Gram for the full Pascal readouts:
\[
 \boxed{\int_0^1\Theta_t(h;s)\overline{\Theta_u(h;s)}\,ds
 =\sum_{v=\max(t,u)}^{\min(2t,2u)}q_t(v-t)q_u(v-u).}\tag{JC-31}
\]

The *original forcing phases cancel only on matching absolute time indices* in this Haar Gram; the real selected seed `s=0` is not averaged away in the definition of `Theta`. This is why Haar Gram positivity alone has no zero-seed sign authority.

For the pure stationary expanding circle `F_h(16^m s)` (not falsely identifying it with the forced `U_m(s)`), the limiting autocorrelation and exact N-sample Haar variance are
\[
 C(d)=\sum_{j\ge0}w_jw_{j+|d|}
 =2^{-|d|}\left(\frac5{27}+\frac{|d|}{9}\right),\qquad
 \boxed{\int_0^1\left|\frac1N\sum_{m=0}^{N-1}F_h(16^m s)\right|^2ds
 =\frac{N-56/27+(12N+56)/(27\,2^N)}{N^2}.}\tag{JC-32}
\]

Its (normalized) spectral density is `|G(e^(iθ))|^2=1/(5-4cosθ)^2`. For the full **Green/Oily composite limiting filter** `K`, the seed-Haar covariance has exact zero-lag `sum k_r^2=8845/49011`, and spectral density
\[
 \boxed{|K(e^{i\theta})|^2
 =\frac{225}{(257-32\cos\theta)(5-4\cos\theta)^2}.}\tag{JC-33}
\]

These are valid independent positive observations. The `1/N` variance in Haar-initialized ensembles does **not** prove any bound for the singled-out seed `s=0`. Conditioning a Haar seed to that exact point is a singular selection; high apparent coherence for selected exceptional seeds remains possible.

## 7. Hostile controls and next honest discriminator

**Changed original seed:** Let `s_*=-π/16=-T_0`, with `T_0=π/16` and `T_(t+1)=16T_t-r(t+1)`. The same original forcing gives `U_t(s_*)=-T_t`; since `0<T_t<1`, its literal carries obey **`kappa_t(s_*)=15 for every t>=1`**. Yet the genuine zero-seed has `kappa_1(0)=3`, `kappa_2(0)=2`. In the depth-one Green×Pascal observer at `n=0`, all terminal carries are therefore in `{3,2}` for the true zero seed and always `15` for the coherent counterseed. **The new labelled joint observable distinguishes these seeds exactly**, while their entire positive carrier and Pascal/Oily probabilities coincide. As `t->infinity`, the coherent source has `e(hU_t(s_*))->1` and its conditional phase-martingale variance tends to zero, notwithstanding every positive identity in this note.

**Wrong observer:** change the Bernoulli clock `#trials=t` and the negative-binomial limit changes; do not claim golden is independent of the observer. **Wrong source:** replace four poles by `r_mut(t)=t^-2`; the leading endpoint Gamma may agree while finite `D_(t;m,k)` and original-source correction differ. **Wrong grade:** replace the Oily two-geometric packet by one geometric; its interior golden fixed point disappears. **Wrong coarse map:** forget `L` and `J` independently and pretend their summed lag preserves the golden fixed point; (JC-24) is an exact counterexample. **Wrong phase:** choose coherent seed `s_*`; every positive source-averaging / asymptotic transfer estimate survives, but its signed normalized Fourier means tend to 1, not 0.

### Claim boundary

The **pathway-gap for constructing a concrete labelled joint probability space is resolved within the declared observer class**. The sigma/source-selection gap for explaining the deterministic original π orbit by such a probability space remains open; the mu/probe gap for a genuinely discriminating **asymptotic signed** estimate remains open. None of the displayed covariances, posterior information gains, fixed-point selections, spectral densities, or stable inverses supplies `sum_(t<=N)e(hU_t(0))=o(N)`.

**Next decisive probe:** Retain the full `(L,J,packet-grade,carry,absolute-phase)` tags and use the true zero-seed recurrence to derive a conditional signed carry-bias estimate that **fails** on the coherent `s_*` and constant-phase controls for a proved reason. A useful target is a noncircular saving in a signed, source-specific cross-time kernel beyond the invertible smoothing `K(S)`. A fresh rational first-digit/moving-prime holdout, not a fitted finite Fourier sample, should challenge the preferred estimate. Any claim of a physical path-feedback mechanism or mathematical π-normality must pay separate truth debt.

## 8. Reproduction and proof authority

- **Pure standard library:** [`joint_carry_probe.py`](joint_carry_probe.py) plus [`test_pascal_carry_joint.py`](../../../tests/test_pascal_carry_joint.py) verifies original forcing/seed, every finite Pascal diamond, positive feedback, rational conditional signed/carry-phase messages, Green finite mixture/drop, exact composite time-offset coefficients, TV comparisons, all finite rational cutoff envelopes, and hostile mutations.
- **Independent methodology:** [`independent_oracle.py`](independent_oracle.py) uses independently coded SymPy generating-function/geometric-derivative checks and direct 65-decimal mpmath Laplace quadrature, and reproduces the covariance and composite spectral density. It is still one investigator's routes, not peer review or a blind implementation.
- Raw receipt files and environment snapshots are in this directory. Mathematical universal claims are supported by the algebra and stated source assumptions, not by finite tests alone.
- The full SUCC root checkout is not present in this environment, and direct Git HTTPS DNS is unavailable. The mandated provenance probe, full native SUCC suite, observer and ordinal probes, Lean and hosted exact-head CI must be executed separately on the committed head and truthfully reported. **π normality and RH remain OPEN**.

**Related exact source records:** [PR #367](https://github.com/femboy2112/SUCC/pull/367) (positive four-pole convolution/field), [PR #368](https://github.com/femboy2112/SUCC/pull/368) (accepted order-statistic Oily and golden Pascal), [PR #369](https://github.com/femboy2112/SUCC/pull/369) (Green disintegration/cross-source correction), [PR #370](https://github.com/femboy2112/SUCC/pull/370) (original-source Pascal sensor and signed inverse), plus inherited [PR #271](https://github.com/femboy2112/SUCC/pull/271) (actual four-bit carry Walsh structure). The mathematical novelty asserted here is **new-to-project assembly and explicitly scoped lemmas**, not independently verified academic priority.
