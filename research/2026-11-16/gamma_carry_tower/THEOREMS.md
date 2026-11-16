# SUCC: Gamma on a nonsplit binary carry tower

**Research status (2026-11-16):** Paper proofs and finite exact/analytic calibrations. This dossier constructs one valid Gamma-transport metric on a hierarchy of binary state extensions and proves a resolution/depth obstruction. It **does not** prove R0, the original-zero carry-density lower bound, π base-16 normality, or any physical quantum mechanism. The abstract cyclic successor and the actual time-dependent BBP update are **different typed maps**.

## Authentic input

The immutable forcing is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\ U_{n+1}=16U_n+r(n+1).
\]

Main XXVI's selected statistic is

\[
C_n=\lfloor U_n\rfloor,\quad \sigma(c)=1-2\mathbf1_{c\bmod4\in\{1,2\}},\quad d_B=\frac1{2}\left(1-\frac1B\sum_{n=B}^{2B-1}\sigma(C_n)\right).
\]

The four-pole source also has

\[
r(n+1)=\int_0^1 t^{8n}Q(t)\,dt,\quad Q(t)=(1-t)(t^2+2)(t^2+2t+2),
\quad 0<r(n+1)<\frac{15}{(8n+1)(8n+2)}\quad(n\ge1).
\]

The integer carry `C_n`, the rational-2-adic residue `U_n mod 2^m`, and the real-circle digits of `U_n+T_n` are distinct. No identification between their metrics is asserted.

## GCT-01. Binary state gluing is a nonsplit group extension (EXACT)

Let `c = a+2b mod 4`, `a,b in F_2`. Then

\[
(a,b)\star(a',b')=(a\oplus a',\ b\oplus b'\oplus aa').
\]

The carry cocycle `k(a,a')=aa'` is nontrivial in the central extension `0 -> C_2 -> C_4 -> C_2 -> 0`: an odd lift of the nonzero element of `C_2` has order four, so there is no group-homomorphic splitting. The selected mask is the anti-diagonal `a xor b=1`; its sign satisfies

\[
\sigma(c+c')=\sigma(c)\sigma(c')(-1)^{aa'},\qquad
\sigma(c)=\Re[(1+i)i^c].
\]

Thus sigma is not a one-dimensional character of C4. It is a combination of the two nonreal C4 characters. This is a classical carry-extension computation; it does not imply any distribution law for actual C_n.

## GCT-02. Complex Gamma depth twists the exact diagonal basis (EXACT)

On `H_2=ell²(C4)`, define `(R f)(c)=f(c+1)`. `R` is unitary, `R^4=I`, and its eigenvalues are `1,i,-1,-i`. For arbitrary complex `alpha`, define the entire operator family

\[
F_\alpha(R)=(2I-R)^{-\alpha}
=2^{-\alpha}\sum_{k\ge0}\frac{(\alpha)_k}{2^kk!}R^k.
\]

`2I-R` is invertible with spectrum in the open right half-plane; the principal operator logarithm defines complex powers. The power series converges absolutely in operator norm for every fixed complex alpha (for alpha=-m it terminates). It satisfies `F_alpha F_beta=F_(alpha+beta)` and `F_0=I`. For real alpha>0, its coefficients are nonnegative and sum to one: a legitimate negative-binomial/Gamma random-depth observation. For negative integer alpha=-m,

\[
F_{-m}(R)=(2I-R)^m,
\]

a **finite signed path stencil**, not a negative-time probability. Gamma's scalar continuation and this chosen operator-valued functional calculus are distinct mathematical types.

Since `R i^c=i i^c`, the diagonal sigma has the exact response

\[
\boxed{F_\alpha(R)\sigma(c)=\Re[(1+i)(2-i)^{-\alpha}i^c]}
\]

for **real** alpha; hence amplitude `5^(-alpha/2)` and phase rotation `alpha arctan(1/2)`. At alpha=1 the exact state values are `(1/5,-3/5,-1/5,3/5)`. Both the gamma coefficients and the choice of basis/generator are load-bearing. The actual BBP carry recurrence does NOT increment C_n by one, so this result is about a declared auxiliary cyclic observer, not the selected π trajectory.

### A nonaccidental geometric match, but not yet source selection

At positive integer shape `alpha=2`, the rate-2 Fourier multiplier is

\[
(2-i)^{-2}=\frac{3+4i}{25}=\frac15\frac{3+4i}{5}.
\]

Its normalized phase is **exactly the stereographic 3–4–5 circle point** `P(1/2)=(3+4i)/5` in the maintained circle/line SUCC observer. Multiplying by the carry-diagonal quadrature gives

\[
\boxed{(1+i)(2-i)^{-2}=\frac{-1+7i}{25}.}
\]

The coefficient seven is an exact rational Gaussian identity; it occurs here in a **universal** mod-4 Gamma observer. By itself it does NOT authenticate BBP's prime-7 source geometry, nor is it an independent explanation of the original `7±4` jet.

A second normalized Gamma observer at rate three has the same cyclic eigenvalue i and multiplier `4(3-i)^(-2)=(8+6i)/25`, whose normalized phase is the other SUCC stereographic point `P(1/3)=(4+3i)/5`. Composing these two normalized, positive Gamma-depth-two observers gives

\[
\boxed{(2-i)^{-2}\cdot4(3-i)^{-2}=\frac{2i}{25}.}
\]

So the **two rate-2/rate-3 Gamma layers compose to an exact quarter-turn phase**, with amplitude attenuation `2/25`. This recovers the circle identity `P(1/2)P(1/3)=i` from a distinct probabilistic operator representation. Their different rates have to be declared; a single rate-one Gamma family does not automatically produce this relation. This is a new-to-SUCC interface candidate combining known formulas, not a novel classical theorem or a π-normality estimate.

## GCT-03. A faithful Gamma metric on the complete binary inverse-limit tower (EXACT)

For `m>=1` put `G_m=C_(2^m)`, let `R_m f(c)=f(c+1)` on standard `ell²(G_m)`, and `F_(alpha,m)=(2I-R_m)^(-alpha)` for real alpha>=0. Define at each finite level

\[
d_{\alpha,m}(x,y)=\|F_{\alpha,m}(\delta_x-\delta_y)\|_2.
\]

Each is a translation-invariant metric because all eigenvalues `2-exp(2πi j/2^m)` are nonzero. The group reductions `p_(m+1,m)` intertwine `R_(m+1)` with `R_m` on *pulled-back cylinder functions* and consequently intertwine `F_alpha` as well. This does **not** assert that point masses themselves pull back as point masses.

For `x,y in Z_2 = inverse-limit G_m`, set

\[
\boxed{D_\alpha(x,y)^2=\sum_{m\ge1}2^{-m}d_{\alpha,m}(x\bmod 2^m,y\bmod2^m)^2.}
\]

The sum converges, defines a translation-invariant metric, and is continuous for the 2-adic topology. At alpha=0, if `v=v_2(x-y)` finite,

\[
\boxed{D_0(x,y)=\sqrt2\,2^{-v/2}=\sqrt{2|x-y|_2}.}
\]

At all fixed nonnegative Gamma depths,

\[
\boxed{3^{-\alpha}D_0(x,y)\le D_\alpha(x,y)\le D_0(x,y).}
\]

Proof: the spectral multipliers have moduli between `3^(-alpha)` and one because `1<=|2-exp(i theta)|<=3`. Apply to each difference vector, square, sum with `2^-m`. Thus the Γ metric is bi-Lipschitz equivalent to the snowflaked 2-adic metric **at each fixed alpha**. It does not quotient away any finite-depth state differences. At infinite alpha the uniform lower constant vanishes; that is an important boundary.

On G2=C4, Fourier calculation distinguishes adjacent and opposite cyclic states:

\[
\boxed{d_{\alpha,2}(c,c+1)^2=5^{-\alpha}+9^{-\alpha},\qquad
d_{\alpha,2}(c,c+2)^2=2\cdot5^{-\alpha}.}
\]

For alpha>0 these are different. The diagonal XOR half in a bitwise square therefore acquires a genuinely nontrivial *cyclic* observation metric. This is an example of the kind of metric the author proposes, not a unique or physically mandated metric.

## GCT-04. The infinite tower has no uniform Gamma spectral gap (EXACT)

For a nonzero frequency `j` of `G_m`, the eigenvalue is `lambda_(m,j)=exp(2πij/2^m)` and

\[
|F_\alpha(R_m)\chi_j|/|\chi_j|=(5-4\cos(2πj/2^m))^{-\alpha/2}.
\]

At the slowest nonconstant mode j=1 and fixed real alpha>0, this tends to **one** as m→infinity. Therefore `sup_(m,j≠0)|multiplier|=1` (a supremum, not an attained maximum). No fixed Gamma depth yields a uniform spectral gap over the entire inverse system, even though each finite cyclic level strictly attenuates its nontrivial modes.

Quantitative threshold: to suppress mode (m,1) to a prescribed `0<rho<1`, it is necessary and sufficient that

\[
\boxed{\alpha\ge \frac{2\log(1/\rho)}{\log(5-4\cos(2π/2^m))}
\sim\frac{\log(1/\rho)}{4π^2}4^m.}
\]

This is the precise *resolution-versus-analytic-depth* obstruction. Gamma can twist every finite level, but achieving the same attenuation at finer levels requires rapidly increasing depth. A spectral gap must come from additional source-selected structure, not from the abstract Gamma weights.

## GCT-05. The actual BBP transition is not a function of mod-4 carry alone (EXACT)

For n>=1 write `U_n=C_n+u_n`, `u_n={U_n}`. Put

\[
j_n=\lfloor16u_n\rfloor,\quad v_n=\{16u_n\},\quad
\epsilon_n=1_{v_n+r(n+1)\ge1}.
\]

Since `0<r(n+1)<1`, the original forcing gives

\[
\boxed{C_{n+1}=16C_n+j_n+\epsilon_n,\qquad
u_{n+1}=\{16u_n+r(n+1)\},\qquad
\epsilon_n=1_{u_{n+1}<r(n+1)}.}
\]

At fixed n choose states with the **same** integer carry c=0 but u=0 versus u=1/16. Their next carry residues mod4 are 0 versus 1. Thus there is no deterministic state map `C4 -> C4` realizing the original source recurrence without retaining the fractional fiber. The abstract cyclic R_m of GCT-02/03 is a declared observer action, **not** the BBP time arrow. A lawful source-coupled connection must act on (time, integer winding, fractional fiber, source passport), or retain an equivalent sufficient history.

## GCT-06. Source-boundary events have a deterministic logarithmic refractory window (EXACT)

The four-pole moment bound implies `r(n+1)<15/((8n+1)(8n+2))<15/(64n²)` for n>=1, and r(n) is strictly decreasing. Whenever `epsilon_n=1`, the next state lies in `[0,r(n+1))`. As long as no further wrap occurs, induction gives

\[
0\le u_{n+k}<r(n+1)\frac{16^k-1}{15}.
\]

Consequently,

\[
16u_{n+k}+r(n+k+1)
<r(n+1)\frac{16^{k+1}-1}{15}<1
\]

for every integer `1<=k<=q_n-1`, where `q_n=floor(log_16(64n²))`. In that full window, `j_(n+k)=epsilon_(n+k)=0`. The proof starts at k=1 after the first wrap and advances inductively. All inequalities use the *original* positive monotone four-pole source; an arbitrary signed coboundary mutant is outside their scope.

On an integer shell B<=n<2B, let `q_B=floor(log_16(64B²))>=1`. Distinct source-wrap events are separated by at least q_B positions, hence

\[
\boxed{\#\{n\in[B,2B):\epsilon_n=1\}
\le1+\lfloor(B-1)/q_B\rfloor=O(B/\log B).}
\]

This is a deterministic statement **for every real starting fractional state**, not an almost-everywhere probabilistic claim. It is a *source-internal wrap*; it must not be conflated with the different raw/completed tail borrow in Main XXVI #652, although the logarithmic scales and proofs are related. A forced wrap event was constructed explicitly at each n in the finite probe; subsequent zeros were checked with exact Fractions.

A further consequence for B>=2: the selected carry density differs from the selected digit-cell statistic by at most the same O(1/log B) count,

\[
\left|d_B-\frac1B\sum_{n=B}^{2B-1}1_{j_{n-1}\bmod4\in\{1,2\}}\right|
\le\frac{1+\lfloor(B-1)/q_{B-1}\rfloor}{B}.
\]

The rare wrap events **cannot alone supply a positive-density anti-locking theorem**; the unresolved source information is in ordinary cell choices j_n, whose long-term correlations remain unproved for U_0=0.

## GCT-07. Source-authentic Gamma path versus artificial cyclic Gamma; sharp shell no-go (EXACT)

On the full source-labelled extended state `x=(n,c,u)` with n>=1, define

\[
F(n,c,u)=(n+1,16c+\lfloor16u+r(n+1)\rfloor,\{16u+r(n+1)\}).
\]

Let `Kf=f circ F`, a unital contraction on bounded observables. Then the *source-time* Gamma observer `F_alpha(K)` is well-defined, with the very same Gamma coefficients, and at negative integer alpha=-m yields the finite signed operator `(2I-K)^m`. Its output at an actual source path is a Gamma-weighted average of *actual* future carry signs, rather than an artificial `c+k` residue path.

For every bounded sequence `|a_n|<=1` and real alpha>=0,

\[
\boxed{\left|\frac1B\sum_{n=B}^{2B-1}\sum_{k\ge0}w_\alpha(k)a_{n+k}
-\frac1B\sum_{n=B}^{2B-1}a_n\right|\le\frac{2\alpha}{B}.}
\]

Proof: shift each shell by k, cancel its overlap, bound its two boundary pieces by `2min(k,B)`, and use `E k=alpha` for the NB law. Thus fixed-depth or alpha_B=o(B) Gamma observation **preserves** a signed shell limit rather than creating one. The coherent constant-sequence control remains one. This strengthens the interpretation firewall, not π-normality.

Combining this generic boundary guarantee with GCT-04 shows an *instrument-conditioning tradeoff*: uniform attenuation of a moving `2^m` cyclic slow mode needs `alpha_m \gtrsim 4^m`, while the generic shell-preservation guarantee needs `alpha_m=o(B)`. These guarantees can hold simultaneously only in the regime `4^m=o(B)`. This is a **restriction on this chosen observer/proof strategy**, not a logical impossibility theorem for the actual π orbit or for other source-conditioned operators.

## GCT-08. One-dimensional temporal phase twists are not enough (EXACT NEGATIVE CONTROL)

For a unit sign observed along a deterministic source path, define its one-step ratio `tau(x)=sigma(C(Fx))/sigma(C(x))`. Multiplication by `tau` defines a twisted Koopman operator `K_tau f(x)=tau(x) f(Fx)`. Let `M_sigma f(x)=sigma(C(x))f(x)`. Then

\[
\boxed{K_\tau=M_\sigma^{-1} K M_\sigma,\qquad F_\alpha(K_\tau)=M_\sigma^{-1}F_\alpha(K)M_\sigma.}
\]

The apparently nontrivial one-step sign twist is a **coboundary** along the source-time line, so it is gauge-conjugate to the untwisted flow and cannot create source-selected cancellation by itself. This is *different* from the nonsplit 2-cocycle in GCT-01, which lives in the binary state-extension composition law and cannot be trivialized by a group-homomorphic splitting. A genuinely new joining instrument must couple time and refinement (at least two independent arrows), or constrain the exact zero-selected path by source arithmetic.

## GCT-09. A direct conditional-fiber entropy gate (EXACT; SOURCE PREMISE OPEN)

On any finite time shell, let `A=C_n mod 2` and `B=floor((C_n mod4)/2)` be the empirical binary random variables under uniform choice of n in that shell. Define the mismatch `E=A xor B`, so the selected density is `d=Pr(E=1)`. Given A, the map `B <-> E` is bijective; hence

\[
H(B\mid A)=H(E\mid A)\le H(E)=h_2(d),
\qquad h_2(d)=-d\log_2d-(1-d)\log_2(1-d).
\]

This is Fano's bound in its elementary binary form, and it does **not** require balanced marginals. It yields a weaker sufficient condition than an unconditional >1-bit entropy threshold: if the *actual zero-seed* carry path has `liminf_(B->infinity) H_B(B|A)>=h_0>0` on every late integer shell, then `liminf d_B>=h_2^(-1)(h_0)>0`, where the inverse is taken on [0,1/2]. In turn Main XXVI's carry-to-phase theorem gives R0. This is **only a conditional implication**: no positive original-source fiber entropy bound is established, and deterministic paths with H(B|A)=0 may still have d=1 (e.g. B=1-A), so positive conditional entropy is sufficient but not necessary. A frozen finite empirical entropy histogram cannot pay the all-shell premise.

The proposed source-selected connection should therefore be tested for a *uniform conditional-fiber entropy or signed-mismatch defect* at the first nontrivial binary extension, while retaining the actual fractional/source history. Scalar Γ attenuation and abstract cyclic mode damping do not supply this bound.

## Claim ledger and next falsifier

- **CLASSICAL / EXACT:** C4 nonsplit carry cocycle; cyclic Fourier diagonal; Gamma NB functional calculus; Fourier multiplier and inverse-limit spectral obstruction; basic 2-adic metric and finite group Fourier algebra.
- **PAPER-DERIVED (SOURCE-SPECIFIC):** exact BBP source-fiber transition; deterministic post-wrap refractory window and finite-shell event count; signed carry/digit-cell transfer; source-labelled Gamma shell boundary cost. Standard exact tests and analytic Fourier checks support these but do not independently certify infinite arithmetic.
- **CONJECTURED / UNVERIFIED:** any uniform positive lower shell density of the original zero seed's XOR carry, any genuine fixed-frequency π Weyl saving, any source-selected curvature/metric lower gap beyond the abstract cyclic observer. The **source-selected connection** from the odd denominator/carry history to circle phase still has not been constructed with a useful *inequality*.
- **REFUTED INFERENCE:** scalar Gamma positivity alone enforces π normality; repeated analytic continuation of a single-valued Gamma function automatically creates new sheets; abstract successor `c->c+1` equals the actual BBP carry update; a finite spectral gap survives uniformly across the infinite refinement tower; a phase twist that is a coboundary is automatically a new invariant.

**Minimum next discriminating experiment:** Construct a two-axis (time × binary-resolution) source-labelled transport with source history, integer winding and odd denominator explicitly retained. Compute a basis/metric defect before modulus reduction. Predict a new signed constraint that must separate the literal U_0=0 from changed rational seeds with arbitrarily long prescribed zero carry words and from the coherent wrong seed. No arbitrary source gauge changes can alter a claimed completed-circle observable. Freeze an analytic inequality and countermodels before new source holdouts beyond 131072. If no such constraint survives, record the source-map inadequacy, not a nonexistent bound.

**Provenance:** Maintained SUCC Main XXVI `docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md`, `docs/MAIN_XXVI_OBSERVER_TRANSPORT.md`, `docs/MAIN_XXVI_HANDOFF.md`; authentic `observational_succ/duck_bbp.py`; Gamma Genesis `research/2026-11-14/gamma_genesis/THEOREMS.md`; signed carry #650/#652. Standard Gamma functional continuation in NIST DLMF §§5.2 and 5.5. All open π claims retain Main XXVI's authority.
