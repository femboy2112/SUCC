# Oily–Macaroni triangular sheet: exact source selection, Gamma–golden family and discriminating mixed responses

**Research date:** 2026-10-29. **Pinned upstream:** `femboy2112/SUCC`, `main@ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`. **Status:** new self-contained *research-only* derivations and finite code probes, not a promotion of the selected BBP Fourier conjecture. No original forcing, zero-seed, imported archive, historical claim ID, build setting or workflow is changed.

## Steelman and source passport

The proposed triangle is a family of **constrained arithmetic/path states**, not three independently chosen numbers on a diagram. Harmonic numbers are finite-rank clocks, Euler's constant is the logarithmic scaling finite part, and `lambda=phi^(-1)` arises through a declared self-consistent Laplace/packet observation. The open question is whether an authentic source map transports this geometry into zero-seeded **signed** BBP cross-time dynamics.

Inherited source (see [Oily packet theorem](../../2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md) and [Oily positive-field cocycle](../../2026-10-26/OILY_POSITIVE_FIELD_GAMMA_COCYCLE.md)):

\[
R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}=\frac{1-x}{(2-x^2)(x^2-2x+2)},\qquad
T_n=\int_0^1x^{8n}R(x)\,dx,\quad n\ge0.
\]

Set `u=x-x^2/2`, `v=x^2/2`, and for `j>=0`, `p_j(x)=(1-x)/4 sum_(k=0)^j u^k v^(j-k)`. The **full** source law for `n>=0` is

\[
P_n(X\in dx,J=j)=\frac{x^{8n}p_j(x)}{T_n}\,dx,
\quad \sum_jp_j=R,
\quad P_n(J\in\cdot\mid X=x)=\mathrm{Geom}_0(u)*\mathrm{Geom}_0(v).
\]

The `n=0` extension of the packet law is a well-defined probability distribution. It is not the deterministic zero-seeded signed BBP phase law. No time-independence or random-digit claim is inferred. The auxiliary source is tagged separately from the original positive Laplace forcing `r(k)=4/(8k-7)-2/(8k-4)-1/(8k-3)-1/(8k-2)`.

## THEOREM TS-01 — literal triangular finite carrier and insertion constraints

Let `U_1,...,U_N` be independent uniform variables on `(0,1)` and `U_(1:N)<=...<=U_(N:N)` their ordered values. As the next uniform observation `v` is added,

\[
U_{(r:N+1)}=\operatorname{median}(U_{(r-1:N)},U_{(r:N)},v),\quad1\le r\le N+1,
\]

with `U_(0:N)=0, U_(N+1:N)=1`. In particular, `U_(r-1:N)<=U_(r:N+1)<=U_(r:N)`; this is a **pathwise** non-linear local update. Proof: inserting one value into an ordered list can only move the rank to the old left neighbor, the new value, or the old right neighbor. The median expression is each resulting rank, including the boundaries. It is stronger than a diagram but says nothing about physical microstates.

For the `r`-th **smallest** uniform rank, `N U_(r:N) -> Gamma(r,1)` in distribution at fixed `r`. Classical beta-log integration gives exactly

\[
E\log(N U_{(r:N)})=\log N+H_{r-1}-H_N\longrightarrow H_{r-1}-\gamma.
\]

If instead `X=U_(N-1:N)` is the **second largest** value, `1-X` has the `Beta(2,N-1)` distribution, and `N(1-X)` obeys the same `Gamma(2)` endpoint law. **Do not confuse** the exact unweighted harmonic-log identity with the source-*accepted* finite distribution below: acceptance changes finite log moments.

## THEOREM TS-02 — exact, source-faithful second-largest acceptance representation

For every integer `n>=0`, let `a=8n`, `N=a+2`, `X=U_(N-1:N)`, and conditionally on `X=x` accept the record with the independently generated Bernoulli probability

\[
W(x)=\frac1{(2-x^2)(x^2-2x+2)}\in[1/4,1].
\]

The raw order-statistic density is `N(N-1)x^a(1-x)`. Therefore the accepted density is **exactly** `x^aR(x)/T_n`; draw the two conditional geometric grades to realize **the full original positive joint law** `P_n(X,J)`. The acceptance probability is

\[
\alpha_n=N(N-1)T_n.
\]

At `n=0` the original BBP integral says `T_0=pi/16`, hence `alpha_0=pi/8`. This is a new sampling representation of an **inherited** integral, not a new derivation of pi or a new BBP digit law.

Writing `t=1-x`, there is an exact polynomial identity

\[
W(1-t)^{-1}=1+2t+2t^3-t^4.
\]

Since `0<=1-W<=3t` and `|(1-W)-2t|<=6t^2`, and the bare `t` has `Beta(2,a+1)` law,

\[
0\le1-\alpha_n\le\frac6{a+3},\qquad
\left|(1-\alpha_n)-\frac4{a+3}\right|
\le\frac{36}{(a+3)(a+4)}.
\]

Thus `a(1-alpha_n)->4`. The total variation distance between the accepted and bare order-statistic marginals is at most `1-alpha_n`, from their exact accepted/rejected mixture decomposition. The bounds are proved for the declared source weights, not fitted numerically.

**Two compatible constructions, but NOT pathwise identification.** Start instead from `(X,J)~P_0`, and given `X` observe `8n` independent Bernoulli(`X`) successes. Conditional on all successes, the law is exactly `P_n`. These events can be nested as `n` grows; `P(E_n)=T_n/T_0`, `P(E_(n+1)|E_n)=T_(n+1)/T_n`. Thus the order-statistic acceptance construction and the **already known** SUCC Bayesian/source-posterior update produce the same single-time joint laws. Their chosen random trajectories are not thereby identified. This is the common-carrier version of [PR #345](https://github.com/femboy2112/SUCC/pull/345), rather than a priority claim for sequential Bayesian conditioning.

## THEOREM TS-03 — the positive triangle normalizer obeys the authentic BBP tail recursion

Let `r(k)` denote the **unchanged signed four-pole rational forcing**, and let `U_0=0`, `U_n=16U_(n-1)+r(n)` for `n>=1`. The original Green expansion gives

\[
T_n=\sum_{m\ge1}16^{-m}r(n+m),\qquad
T_{n+1}=16T_n-r(n+1).
\]

Since `T_0=pi/16`, for `n>=1` this yields the exact complement identity

\[
\boxed{16^{n-1}\pi=U_n+T_n,\qquad
T_n=\frac{\alpha_n}{(8n+1)(8n+2)}.}
\]

Consequently the acceptance-rate triangle satisfies an **explicit source arithmetic constraint**:

\[
\frac{\alpha_{n+1}}{(8n+9)(8n+10)}
=16\frac{\alpha_n}{(8n+1)(8n+2)}-r(n+1).
\]

This coupling *recovers* the authentic scalar Green tail and zero-seeded prefix from their **already fixed** source identity. Its probability parameter encodes `pi` through the inherited integral; that is not a derivation of digit equidistribution from fresh random paths. It is an equality of normalizers, **not** a law saying the actual signed phase stochastically samples this triangle.

## THEOREM TS-04 — continuous rank sheet and the golden finite-part family

Let `lambda=(sqrt(5)-1)/2`, `Y_r~Gamma(r,1)` (`r>0`). For `q>=0` and `Re(s)>-r` the exact Laplace–Mellin sheet is

\[
K_r(q,s)=E[Y_r^s e^{-qY_r}]
=\frac{\Gamma(r+s)}{\Gamma(r)(1+q)^{r+s}},\quad
\frac{K_{r+1}}{K_r}=\frac{r+s}{r(1+q)}.
\]

The mixed information response is `partial_q partial_s log(K)=-1/(1+q)`. At the golden `q=lambda`, the Hessian of `log K` in natural parameters `(s,-q)` is the nondegenerate covariance matrix of `(log Y,Y)`; in the `(q,s)` order its entries are `[r lambda^2,-lambda;-lambda,psi_1(r)]` and its determinant is `lambda^2(r psi_1(r)-1)>0`.

Define the **chosen** rank family

\[
D(r)=\psi(r)-(1+\lambda)^{-r}=\psi(r)-\lambda^r.
\]

At integer ranks `D(r)=H_(r-1)-gamma-lambda^r`, with exact recurrence `D(r+1)-D(r)=1/r+lambda^(r+2)`. Since `psi_1(r)>0` and `log lambda<0`, `D` is strictly increasing. It has precisely one real zero `r*=1.9514593666551893...` (numerical location, not certified interval here). At **rank two**,

\[
D(2)=1-\gamma-\lambda^2=\lambda-\gamma=\Omega_{OM}.
\]

This derives a coherent *family* and the precise `rank=2` specialization. Higher ranks are auxiliary Gamma models, not independently authenticated BBP carriers.

## THEOREM TS-05 — source-selected golden PGF and a coupled first shadow

The original two geometric grades have boundary PGF

\[
G(z)=\sum_{j\ge0}\frac{j+1}{2^{j+2}}z^j=\frac1{(2-z)^2}
=L_{Gamma(2)}(1-z).
\]

The unique attracting fixed point of `G` in `[0,1)` is `z_*=lambda^2=1-lambda`, whereas the one-stage mutant `1/(2-z)` has only the boundary fixed point `z=1`. Thus `q=1-z_*=lambda` is motivated *relative to the specific two-stage source*, not by bare circle or Gamma geometry alone. The finite conditional PGF has an exact first endpoint jet

\[
E[z^J|X=x]=G(z)+(1-x)H(z)+O((1-x)^2),
\quad H(z)=2G(z)-zG'(z)=\frac{4(1-z)}{(2-z)^3}.
\]

At `z=z_*`, **exact algebra over `Q(sqrt(5))`** gives `G(z_*)=z_*` and `H(z_*)=4lambda^4`. For the authentic source `Y=8n(1-X)` as `n->infty`, this yields

\[
\boxed{\lim_{n\to\infty}8n\operatorname{Cov}_{P_n}(z_*^J,\log Y)=4\lambda^4},
\]

\[
\boxed{\lim_{n\to\infty}8n\operatorname{Cov}_{P_n}(z_*^J,(\log Y-z_*)^2)
=8\lambda^4(\lambda-\gamma).}
\]

Proof: the conditioned first jet is `(Y/a)H(z)+O(Y^2/a^2)` with `a=8n`. The source endpoint has Gamma(2) log moments; `Cov(Y,logY)=1`, `Cov(Y,(logY-c)^2)=2(psi(2)-c)`. Uniform polynomial/log integrability follows by the transformed beta density and `1/4<=W<=1`. This is a **new specialization/extension** of the inherited [#310 connected-shadow theorem](../../2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md) to the real interior fixed point `z_*`; it is not a signed Weyl estimate.

## THEOREM TS-06 — authentic first source correction beyond the shared Gamma limit

Define for each integer `n>=1`, `a=8n`, `Y=a(1-X)` under the **accepted** source `P_n`,

\[
F_a(q)=E_{P_n}[\log Y-e^{-qY}],\qquad q\ge0.
\]

Then for every fixed finite `q>=0`, as `a->infinity` **through `8N`**,

\[
F_a(q)=\psi(2)-(1+q)^{-2}+\frac{C(q)}a+O_q(a^{-2}),
\quad C(q)=-\frac92-\frac7{(1+q)^2}+\frac4{(1+q)^3}+\frac3{(1+q)^4}.
\]

**Derivation:** substitute `y=a(1-x)` in the authentic density. Uniformly in the integrated Laplace asymptotic sense,

\[
x^a W(x)=e^{-y}\left[1-\frac{2y+y^2/2}{a}+O\left(\frac{P(y)}{a^2}\right)\right],
\quad a^2T_n=1-\frac7a+O(a^{-2}).
\]

Here `P` is a fixed polynomial and the error is integrated against `y e^{-y/2}(1+|log y|)`; splitting at `y=a/2` handles the exponentially small tail. The normalized first correction to the Gamma(2) density is `7-2y-y^2/2`. Use `E_Gamma2[Y^k]=(k+1)!`, `E[Y^k logY]=(k+1)! psi(k+2)` to compute `C(q)` exactly. In particular at the **packet-selected** `q=lambda`, the limit is the author's constant with a nontrivial source-specific first jet:

\[
\boxed{F_{8n}(\lambda)=\Omega_{OM}+\frac{6\lambda-19/2}{8n}+O(n^{-2}).}
\]

The correction coefficient is negative (`6lambda-19/2=-5.7917960675...`); numerics are holdouts only, and the asymptotic is a paper argument, not a numerical universal proof. This `F_a` is an auxiliary expectation over the true positive packet marginal, not a signed observable of the digit orbit.

## THEOREM TS-07 — matched-jet countermodel and a second-order source discriminator

For fixed `0<=epsilon<=1`, introduce **different** acceptance weights

\[
W_\epsilon(x)=W(x)[1-\epsilon(1-x)^2].
\]

They are valid probabilities, have `W_e(1)=W(1)=1` and `W_e'(1)=W'(1)=2`, and thus share the Gamma endpoint and the **same first-order asymptotic TS-06** while not being the original source for `epsilon>0`. Let `F_{a,epsilon}` be the corresponding normalized log–Laplace expectation. A direct Bayes reweighting gives the **exact finite identity**

\[
F_{a,\epsilon}(\lambda)-F_a(\lambda)
=-\frac{\epsilon\,\operatorname{Cov}_{P_n}(\log Y-e^{-\lambda Y},Y^2)}
{a^2[1-\epsilon\,E_{P_n}(Y^2)/a^2]}.
\]

Consequently, by Gamma(2) moment convergence,

\[
\boxed{\lim_{a\to\infty}a^2[F_{a,\epsilon}(\lambda)-F_a(\lambda)]
=-\epsilon(5+6\lambda^3)\ne0\quad(\epsilon>0).}
\]

The scalar `5+6lambda^3` comes from `Cov(log Y,Y^2)=5` and `Cov(e^{-lambda Y},Y^2)=6lambda^4-6lambda^2`; since `lambda^2-lambda^4=lambda^3`, their difference is `5+6lambda^3`. This **refutes** any source-uniqueness claim based on the leading Gamma constant and first source correction alone. The source-specific second-order response resolves that particular mutant.

## THEOREM TS-08 — latent Gamma–Poisson realization, and the joint-source firewall

Draw `Z~Gamma(2,1)` and then `J|Z~Poisson(Z)`. Exactly `P(J=j)=(j+1)/2^(j+2)`, and conditioning on the realized grade gives `Z|J=j~Gamma(j+2,2)` with log mean `H_(j+1)-gamma-log 2`. This is a **Bayesian latent representation of the boundary grade**, not the assertion `Z=Y` for SUCC's endpoint variable `Y=8n(1-X)`.

The authentic limiting grade and endpoint become independent, so their mixed transform is

\[
K_{auth}(z,s)=\frac{\Gamma(2+s)}{(2-z)^2}.
\]

Identifying the *separate* Poisson intensity with that same endpoint `Y` would instead give

\[
K_{wrong}(z,s)=\frac{\Gamma(2+s)}{(2-z)^{2+s}}.
\]

These models have identical individual marginal transforms (`z=1` or `s=0`) but different joint laws. **Exact rational witness:** at `z=1/2,s=1`, `K_auth=8/9` while `K_wrong=16/27`, difference `8/27`. In the wrong model `Cov(z^J,log Y)=-(2-z)^(-2) log(2-z)` stays nonzero as the boundary is approached, contrary to the authentic independent limit. Same-looking Gamma shadows do not authenticate a source map.

At each finite `x`, the authentic two geometric grades also have a valid **two-exponential/conditional-Poisson** representation: exponential intensities of rates `(1-u)/u`, `(1-v)/v`, with Poisson counts summed. The boundary rates converge to 1. This preserves the conditional grade law but does not identify those intensities with the endpoint `Y_n`.

## Crucible, verdict and next theorem gate

- **SURVIVES (exact model):** literal interlacing triangles; source-authentic acceptance marginal; grade restoration; source-normalizer/BBP-tail complement; rank Gamma–golden family; exact PGF duality; first source-specific correction; second-order matched-jet discriminator; distinct joint-transform counterexample.
- **INHERITED (not academic novelty):** classical beta/order statistics, Gamma digamma/Laplace/moment identities, Gamma–Poisson conjugacy, BBP pi integral, main's source `T_n`, Bayesian conditioning, and #310's source connected shadow. This round's cross-construction and coefficient specializations are *new-to-program calculations*, not independently reviewed priority claims.
- **REFUTED (with counterexample):** identical Gamma boundary and first source jet imply identical source (`W_e`); identical Gamma and grade marginals imply the same coupling (`K_auth` vs `K_wrong`); a single positive normalization proves genuine selected cancellation (changed-seed control below).
- **OPEN:** an authenticated bridge from this *positive* source sheet to the *signed zero-seeded* BBP Weyl sums. With the same positive law and forcing but initial `V_0=-pi/16`, `V_n=U_n-16^(n-1)pi=-T_n->0`, hence for every integer `h`, `e^{2pi i h V_n}->1` and its Cesaro mean tends to 1. This coherent counterseed has the same positive triangle yet does not equidistribute. The actual required seed is `U_0=0`, which our positive construction does not distinguish without separately attaching that signed phase.

**Next falsifier:** carry the exact authentic `U_0=0` phase into a **noncentral joint cross-time** statistic of the accepted record and two geometric grades. The statistic must differ provably from the `V_0=-pi/16` control and from both `W_e` and `K_wrong`; then show a genuinely new signed saving not already equivalent to the Weyl criterion. PRs [#367](https://github.com/femboy2112/SUCC/pull/367) and [#366](https://github.com/femboy2112/SUCC/pull/366) are sibling routes (convolution/mixed-sheet and Stoneham/positive-weight no-go), not imports into this branch.

## Reproducible artifacts and boundaries

- [`triangle_sheet_probe.py`](triangle_sheet_probe.py): exact `Fraction` source identities, median insertion, Beta moments, golden `Q(sqrt(5))` arithmetic, authentic-vs-counterfeit mixed transforms and source-prefix complement.
- [`tests/test_oily_triangle_sheet.py`](../../../tests/test_oily_triangle_sheet.py): standard-library exact tests (path is relative to repository root; the real file is under `/tests`).
- [`numerical_oracle.py`](numerical_oracle.py): independent `mpmath` quadrature of original four-pole formula, source integral/recurrence, and first/second-jet holdouts. Numerical observations are **not** theorem receipts.
- [`CLAIMS.md`](CLAIMS.md), [`VALIDATION.md`](VALIDATION.md), [`NEXT.md`](NEXT.md): scoped claim inventory, recorded local execution, and next discriminating proof target.

**Not claimed:** total full SUCC test-suite success, hosted exact-head CI, Lean certification, academic novelty, physical vacuum/path statistics, π normality in any base, RH, or an as-yet nonexistent source-preserving functor to the signed BBP orbit.
