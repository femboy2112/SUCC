# Original BBP arctangent reciprocity: source-native irrational mirror, Gaussian commutator and a one-quadrature π-normality criterion

**Status: classical arctangent/Cayley and circle ergodicity, exact source-specific algebra, a newly assembled conditional SUCC proof gate.** These are paper derivations with executable exact controls, **not** an all-horizon signed cancellation proof, formal/Lean theorem, physical quantum experiment, or external academic novelty claim.

## Contract and provenance

The original four signed BBP poles and literal zero-seeded state are unchanged:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

Set `e(x)=exp(2πix)`, `A_N(h)=N^-1 sum_{n=1}^N e(h U_n)`, for nonzero integer h. The pre-existing BBP identity gives `alpha=sum_{j>=1}16^-j r(j)=pi/16`, and the original source Green telescope gives `U_n=16^n alpha-T_n`, `0<T_n<1/(64n²)` for n>=1. No rederivation of the BBP formula or pi normality is claimed. Previous SUCC PRs #438–#450 supply the exact source, finite phase echoes, ordered path category, Riemann-sphere form, geometric brackets and signed Fejér-lag frontier. They are inherited mathematics, not independent proof witnesses.

## AR-01: Exact arctangent reciprocal involution, including all projective endpoints

For *real* t !=0, principal arctangent obeys

\[
\arctan t+\arctan(1/t)=\operatorname{sgn}(t)\pi/2.
\]

The sign is load-bearing; a global complex analytic equality requires explicit branch choices (NIST DLMF §§4.23–4.24). Use SUCC's Cayley coordinate `C(t)=(1+it)/(1-it)` and angular form `eta=2dt/(1+t²)`. The projective involution `K(t)=1/t`, exchanging `0` and `infinity`, satisfies *globally as rational functions*

\[
C(K(t))=-C(t)^{-1},\qquad K^*\eta=-\eta.
\]

Thus in circle cycles `x in R/Z` it is `J_{1/2}(x)=1/2-x`. For a source-labelled step `F_r(x)=16x+r`, we have exactly modulo 1

\[
J_{1/2}F_r=F_{1/2-r}J_{1/2}.
\]

On *real, unwrapped* cycles, the corresponding transformed forcing is `-15/2-r`; the difference is an integer multiple of 8. In circle characters the reciprocal transport is `e(h J_{1/2}(x))=(-1)^h e(-h x)`. Hence `S_N^dual(h)=(-1)^h overline(S_N(h))`. **No cancellation follows from this representation equivalence.** The half-turn is a 2-primary character and should not be silently inserted as a primitive phase of the original odd-Q finite register.

The source's geometric ×16 projective tangent map `D16` also obeys the exact rational identity `D16(1/t)=-D16(t)`; the even-radix parity sign is essential. It is checked independently through degree-16 Gaussian-binomial expansion, not just sampled angles.

## AR-02: Source-attested *rational projective* reflection of *irrational angular* order

The **original** `r(2)=106/819` is exactly verified from the four poles and the combined source polynomial; it is also the logarithmic derivative `(1/8)R'(2)/R(2)` of the original source-cover map `R(z)` in PRs #442/#449. Put

\[
a=819,\quad b=106,\quad d=a^2+b^2=681997,
\quad q=b/a=r(2),\quad\beta=\arctan(q)/\pi.
\]

Rotate the reciprocal by the *rational projective* circle rotation `R_{-1/q}`. In the tangent parameter,

\[
J_q(t)=R_{-1/q}(1/t)=\frac{q-t}{1+qt}
=\frac{106-819t}{819+106t}.
\]

On homogeneous rational tangent coordinates `[v:w]` it is the matrix

\[
M=\begin{pmatrix}-819&106\\106&819\end{pmatrix},\qquad M^2=681997 I,
\]

so it is a globally defined rational projective involution, including the pole and infinity. On circle cycles `J_q(x)=beta-x`. Its phase factor is

\[
\gamma=e(\beta)=\frac{a+ib}{a-ib}
=\frac{659525+173628i}{681997}\in\mathbb Q(i),\qquad |\gamma|=1.
\]

**Irrationality is certified algebraically**: every root of unity belonging to Q(i) is one of `+1,-1,+i,-i`. The displayed γ has both rational components nonzero, hence has infinite multiplicative order. Thus beta is irrational. This is not a claim that gamma has order four because its coefficients are Gaussian rational, nor a claim that all rotations become finite Fourier-register permutations. Indeed multiplication by gamma moves a finite root-of-unity phase to a generally NON-torsion algebraic phase; the correct phase field is the composite `Q(i,zeta_Q)`, not just the finite character group.

Under the circle ×16 endomorphism `T(z)=z^16`, and `J_gamma(z)=gamma/z`, the two compositions are

\[
T(J_\gamma(z))=\gamma^{16}z^{-16},\qquad
J_\gamma(T(z))=\gamma z^{-16},\quad
\boxed{T J_\gamma=R_{\gamma^{15}}J_\gamma T}.
\]

The central factor `gamma^15` has infinite order. In cycle coordinates this is the rotation by `15 beta`. **Because T is noninvertible, this is a twisted commuting-square relation, not a group commutator involving an unavailable T inverse.** Its algebraic exactness is not source-specific signed cancellation. A mirror applied to the actual source step transports it to `r'_n=-15 beta-r_n` modulo 1, a different marked source-labelled realization, not a claimed symmetry of the unchanged four-pole source itself.

## AR-03: Rigidity: asymptotic ×16 invariance plus ONE irrational mirror forces Haar

For any circle Borel probability measure mu,

\[
T_*\mu=\mu,\quad (J_\beta)_*\mu=\mu,\quad\gamma^{15}\text{ infinite order}
\quad\Longrightarrow\quad \mu=m_{\mathrm{Haar}}.
\]

Proof: `T J_beta=R_{15beta}J_beta T`. The hypotheses make mu invariant under rotation by `15beta`. Its Fourier coefficient at nonzero h then obeys `hat(mu)(h)=gamma^(15h) hat(mu)(h)`. Infinite order forces every nonconstant coefficient zero. Density of trigonometric polynomials gives Haar. This is the elementary irrational-rotation uniqueness theorem; no new measure-theoretic priority claim.

For the *authentic* BBP sequence, empirical measures `mu_N=(1/N) sum_{n=1}^N delta_{U_n mod 1}` are **asymptotically T-invariant**, because `r(n+1)->0`. Better, they satisfy the source-specialized **explicit quantitative bound** in AR-04. Hence any weak-* limit of these empirical measures is T-invariant. If all such limits are J_beta-invariant, they are Haar. The converse also holds. This is a conditional criterion: **the mirror invariance is the new unproved analytic estimate**, not something supplied by the algebraic existence of J_beta.

## AR-04: All-N authentic source tail and exact signed one-quadrature inequality

The positive original four-pole density and monotonicity (inherited and independently spot-checked here) imply, for n>=1,

\[
0<r(n+1)<\frac{15}{64n^2},\qquad
\sum_{n=1}^{\infty}r(n+1)<\frac{15}{32}.
\]

The original recurrence gives `e(h*16U_n)=e(hU_{n+1})e(-h r(n+1))`. Therefore, for **every** N>=1, any nonzero integer h and ANY real initial seed,

\[
E_N(h):=A_N(16h)-A_N(h),\quad
|E_N(h)|\le\frac{2+2\pi|h|\sum_{n=1}^N r(n+1)}N
<\frac{2+15\pi|h|/16}{N}
<\frac{2+165|h|/56}{N}.
\tag{1}
\]

The 2/N term accounts for two shifted-sum boundary characters. All constants are explicitly source-justified; the final rational bound uses classical pi<22/7.

For the source-native irrational mirror define a **single signed real quadrature** per positive harmonic:

\[
B_N(h)=\frac1N\sum_{n=1}^N\sin(2\pi hU_n-h\arctan(q)).
\]

Equivalently, let `Z_h=A_N(h)` and write `gamma=e^{2i theta}`, `theta=arctan(q)`. Then `B_N(h)=Im(e^{-ih theta} Z_h)` and the *complex mirror defect*

\[
D_N(h)=Z_h-\gamma^h\overline{Z_h}
=2i e^{ih\theta}B_N(h),\qquad |D_N(h)|=2|B_N(h)|.
\]

With `W=A_N(16h)=Z_h+E_N(h)`, subtract its mirror defect. Exact rearrangement gives

\[
(\gamma^{16h}-\gamma^h)\overline{Z_h}
=D_N(h)-D_N(16h)+E_N(h)-\gamma^{16h}\overline{E_N(h)}.
\]

Use `|gamma^(16h)-gamma^h|=2|sin(15h theta)|`. For **every** N>=1 and h>=1:

\[
\boxed{\displaystyle
|A_N(h)|\le
\frac{|B_N(h)|+|B_N(16h)|+\frac{2+165h/56}{N}}
{|\sin(15h\arctan(106/819))|}.}
\tag{2}
\]

The denominator is nonzero for every h>=1 by AR-02. Note the **two frequencies share ONE REAL sine-like quadrature**; this is not the demand that both real and imaginary Weyl components vanish separately at every h.

Consequently:

\[
\boxed{\begin{gathered}
\pi\text{ base-16 normal}\quad\Longleftrightarrow\\
\forall h\ge1\text{ fixed},\quad B_N(h)\to0.\end{gathered}}
\tag{3}
\]

For the right-to-left implication use (2), the source O_h(1/N) bound and Weyl's criterion. For left-to-right use the original BBP Green tail: `U_n=16^n(pi/16)-T_n` with `sum_n T_n<1/32`, so original orbit equidistribution iff pure `16^n pi/16` orbit does, which is equivalent to normality of pi (the initial base-16 digit shift is finite). The mirror sine average of a normal orbit tends zero since it is a finite linear combination of fixed-frequency characters. This criterion is an **equivalence/conditional gate**, not a demonstration that its right-hand condition holds.

## AR-05: Exact rational Gaussian-integer denominator — no pi, no numerical trig

The commutator condition number in (2) has an exact rational SQUARE. For `m=15h` let

\[
I_m=\Im(819+106i)^m\in\mathbb Z,\qquad d=681997.
\]

Then

\[
\boxed{|\sin(15h\arctan(q))|^2=\frac{I_{15h}^2}{d^{15h}}\in\mathbb Q_{>0}},
\quad|\gamma^{15h}-1|^2=\frac{4I_{15h}^2}{d^{15h}}.
\tag{4}
\]

**Every denominator is certified by nonzero integer arithmetic**; the proof of nonvanishing is the Q(i) root-of-unity argument. In particular the `h=1` conditioning is approximately 0.935945, much better than the unrotated reciprocal (which is blind at every even h). No unwrapping of arctan branches or arbitrary floating rotation calibration is necessary.

There is also an integer-coefficient signed realization. Put `(a_h,b_h)=(Re,Im)(819-106i)^h in Z²`. For each fixed h>=1,

\[
\boxed{\quad (681997)^{h/2}B_N(h)
=a_h\Im A_N(h)+b_h\Re A_N(h).\quad}
\]

For h=1 this is simply **`819 Im A_N(1) - 106 Re A_N(1)`**. The condition `B_N(h)->0` is equivalent to vanishing of the fixed integer-weight signed statistic (the scale is fixed for each h). This provides a concrete interface to SUCC's signed real/Fejér-lag machinery. It is not a positivity or absolute-energy estimate.

## AR-06: Hostile controls and why bare arctan reciprocity FAILS

**Rational-axis countermodel:** Let the base-16 digits be IID uniform on **{0,7,8,15}**, defining a Cantor-type measure nu. It is invariant under `T(x)=16x` because T shifts IID digits, yet not Haar (only four digit values occur). For almost every nonterminating digit sequence, `J_{1/2}(x)=1/2-x mod 1` transforms its **first digit** by `(7-d1) mod16` and all later digits by `15-d_j`. Both permutations preserve {0,7,8,15} and its uniform distribution. Thus `nu` is also invariant under the ORIGINAL unrotated arctan reciprocal. Hence bare J_1/2+T **does not imply normality**; irrational rotation of the mirror axis is mathematically load-bearing.

**Changed seed:** With original forcing but altered real seed `s=1/5-pi/16` (IRRATIONAL, **not** an original finite rational-register state), `U_n(s)=16^n/5-T_n`, so `e(hU_n(s))->e(h/5)`. The source-native mirror sine limit at h=1 is `sin(2*pi/5-atan(q))`, numerically ~0.90 and rigorously nonzero (atan(q) lies in (0,1/5), while 2pi/5>1). This correctly rejects the coherent nonnormal same-forcing real counterseed. A general positive source mutant matching only r2 also passes the mirror-construction algebra: the full authentic source remains required to authenticate (1) and the target orbit.

**Finite observer counterfeit:** Since r(2) is a finite source value, a source mutant agreeing only through step 2 has exactly the same gamma and commutator. The unproved mirror symmetry is not recovered from one datum; it necessarily constrains the actual long-term original forcing/seed evolution.

**Sphere-vs-Fourier type firewall:** A Möbius transformation on projective tangent coordinates is not a Fourier operator on every SUCC state space. The factor gamma is not torsion and does not preserve the finite odd-conductor arithmetic state set. Store it as an external algebraic phase in Q(i,zeta_Q), or use the continuous circle Hilbert representation. A coordinate rotation/natural transformation never implies the required empirical *invariance* without a new estimate.

## AR-07: Finite geometric/BBP mirror-axis alternatives and resolution costs

A second natural axis is `beta_star=1/2+alpha=1/2+pi/16`: it explicitly rotates the baseline reciprocal by the completed original BBP constant. Its commutator is irrational; the same proof works. At source depth M, the **exact rational** interval

\[
\alpha_M=\sum_{j=1}^M 16^{-j}r(j)
<\alpha<\alpha_M+\frac{r(M+1)}{15\,16^M}
\]

certifies this axis. Replacing the exact beta_star by the interval midpoint changes `B_N(h)` by at most `pi |h| r(M+1)/(30*16^M)`; the program pays pi<22/7 to output a rational upper bound. Taking M of order log_16 N makes this AXIS error O_h(1/N). It does **not** resolve the full exponentially fast trajectory phases; those need the different PR #448 source/geometric transport budget.

Likewise parent PR #447's independent chord path ratio gives `0<pi-Pi_(4M)<8/(3*256^M)`. Its mirror axis `1/2+Pi_(4M)/16` has signed-observable error `<11|h|/(21*256^M)`. This reuses the same circle/diameter geometry but is a *finite axis approximation*, not a new bound on signed source orbits.

For the default source-native q=r2 axis, **none of this irrational-axis approximation is needed**: the mirror Möbius coefficients and squared commutator denominator are already exact rationals. That makes it the preferred next candidate.

## AR-08: Strongest next falsifying probe

Establish, for every fixed h>=1, the authentic literal-zero original-four-pole signed limit

\[
\boxed{\lim_{N\to\infty}\frac1N\sum_{n=1}^{N}
\Im\left[(819-106i)^h e(hU_n)\right]=0.}
\tag{OPEN}
\]

This is mathematically **equivalent** to base-16 normality of pi under the proved source reduction. It has only one real scalar target at each harmonic and integer Gaussian coefficients. Require a source-specific argument for its vanishing, or source-specific signed critical Fejér-lag estimates implying it. The reflection's existence, involutivity, irrational angle, exact projective/categorical transport, or finite diagnostics are insufficient by themselves.

Run both cosine/sine and mirror-side exact rational-phase interval oracles with source-identity checks. Negative controls: same-forcing changed real seed, finite-prefix positive source mutants, rational-axis Cantor countermodel, wrong reflection branch, projective t=0/infinity, incorrect R_{-1/q} sign, gamma phase discarded, radix frequency h ->16h not correctly transported, and finite conductor vs non-torsion phase. Fresh horizon/mode holdouts must be preregistered. Do not generalize finite signs to infinite behavior.

## External mathematical references (classical facts, not priority)

- NIST DLMF §4.23 principal inverse trigonometric branches, https://dlmf.nist.gov/4.23
- NIST DLMF §4.24 inverse tangent expansions and sign choice, https://dlmf.nist.gov/4.24
- Original BBP formula, Bailey–Borwein–Plouffe, https://ntrs.nasa.gov/citations/19970009337
- Classical Weyl criterion and Fourier uniqueness on the circle, used as standard background.
