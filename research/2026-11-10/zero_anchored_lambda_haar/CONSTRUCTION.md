# Contraction construction: signed overlap, source differences, and the missing estimate

**Date:** 2026-11-10. **Role:** independent constructor bearing for the Zero-Anchored
Lambda–Haar Compiler. **Base inspected:** `50481e49592af00d87c602f671a28f3503709de0`.
This is a paper derivation, not a formal-kernel proof or an independent external review.
The mathematical identities below are established in their stated domains; the proposed
source-selected statistical contraction remains **OPEN**.

## 1. Hole contract and the precise operators

Fix the authentic source

```math
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
```

Put

```math
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
z_n=\{U_n+T_n\}=\{16^n\pi/16\},\qquad
\mu_N=\frac1N\sum_{n=0}^{N-1}\delta_{z_n}.
```

Write `T(x)={16x}`, `B_a(y)=(a+y)/16`, and define operators on measures by

```math
C\nu=\frac1{16}\sum_{a=0}^{15}(B_a)_*\nu,\qquad
Q\nu=C T_*\nu.
```

Thus `Q` replaces the leading digit uniformly while retaining the actual future tail.
It also equals the average of the sixteen circle translations by `a/16`. These are
the operators already used in `observational_succ/recursive_haar_pinbed.py`.
`C` contracts interval Wasserstein distance by `1/16`; **Q does not**. Indeed Q is
idempotent and has nontrivial fixed laws. Calling Q a strict contraction would erase
the entire statistical obligation.

The requested hole is the following, with every quantifier retained:

```math
\exists\theta\in[0,1),\quad \exists N_0,\quad
\forall N\ge N_0:\quad
D_N\le\theta D_{\lfloor N/2\rfloor}+\varepsilon_N,
\qquad \varepsilon_N\ge0,\quad\varepsilon_N\longrightarrow0,
```

where `D_N=W_1(mu_N,Q mu_N)` in the ordinary interval metric. Such an estimate would
force `D_N->0`, hence pi normality. Without an independently controlled error it is
an equivalent asymptotic target: if `D_N->0`, taking `epsilon_N=D_N` works for every
fixed theta. Consequently the mere existence of an unspecified vanishing error is
not a weaker theorem. An effective arithmetic error estimate would be actual new
proof content.

**Cheapest falsifier:** apply a purported seed-blind proof to the coherent seed
`s=-pi/16`. Its completed orbit is constantly zero and `D_N=15/32`. An estimate with
theta less than one and vanishing error is impossible there. A source-specific
proof must use more than correct evaluation, tail contraction, or unchanged forcing.

## 2. Exact finite Poisson reconstruction

The following holds for every consecutive radix-16 orbit, not just the BBP orbit.
Let lambda denote Lebesgue measure and let

```math
\eta_N=\mu_N-Q\mu_N,\qquad
\delta_N=T_*\mu_N-\mu_N
       =\frac{\delta_{z_N}-\delta_{z_0}}N.
```

All these differences have total mass zero. The Kantorovich–Rubinstein norm of
`delta_N` is exactly `|z_N-z_0|/N`. Since `C lambda=lambda`, elementary rearrangement
gives

```math
\mu_N-\lambda=\eta_N+C\delta_N+C(\mu_N-\lambda).
```

Iterating L times proves the finite, signed identity

```math
\mu_N-\lambda
=\sum_{k=0}^{L-1}C^k\eta_N
 +\sum_{k=1}^{L}C^k\delta_N
 +C^L(\mu_N-\lambda).
```

The last term has norm at most `16^-L W_1(mu_N,lambda)`. The two series converge in
the mass-zero Wasserstein/Kantorovich–Rubinstein norm, yielding

```math
\mu_N-\lambda
=\sum_{k\ge0}C^k\eta_N+\sum_{k\ge1}C^k\delta_N.
```

Taking norms recovers the already established sharp recursive-Haar bound

```math
W_1(\mu_N,\lambda)
\le\frac{16}{15}D_N+\frac{|z_N-z_0|}{15N}.
```

Conversely, two applications of the triangle inequality give

```math
\frac{15}{16}W_1(\mu_N,\lambda)-\frac{|z_N-z_0|}{16N}
\le D_N
\le\frac{17}{16}W_1(\mu_N,\lambda)+\frac{|z_N-z_0|}{16N}.
```

This proves `D_N->0` if and only if the orbit becomes equidistributed. No weak-limit
continuity assumption for the discontinuous map T is needed; the exact endpoint
identity pays its cost before the limit.

**Actual compiler use:** finite unfoldings can preserve the signed reconstruction
and certify its geometrically decreasing truncation residual. This is a contraction
in *observer depth L*. It leaves the size of the authenticated statistical input
`eta_N` unresolved. Replacing that input by zero is not a legal beta reduction.

## 3. Exact dyadic cancellation identity

This is a checkable decomposition of the requested contraction, retaining the
signs which an absolute-value argument loses.

For any finite law mu on `[0,1)`, put

```math
H_\mu(t)=F_\mu(t)-F_{Q\mu}(t),\qquad
D(\mu)=\int_0^1|H_\mu(t)|\,dt.
```

For adjacent blocks of length M, let `mu^-_M` be the law of `z_0,...,z_(M-1)` and
`mu^+_M` the law of `z_M,...,z_(2M-1)`. Define the **signed overlap**

```math
\Omega_M=\int_0^1
 \min\{|H_{\mu^-_M}(t)|,|H_{\mu^+_M}(t)|\}
 \mathbf1_{H_{\mu^-_M}(t)H_{\mu^+_M}(t)<0}\,dt.
```

Then, exactly,

```math
\boxed{D_{2M}=\frac{D(\mu^-_M)+D(\mu^+_M)}2-\Omega_M.}
```

**Proof.** Both the empirical law and Q are linear. Thus
`H_(mu_2M)=(H_(mu^-_M)+H_(mu^+_M))/2`. Integrate the real scalar identity

```math
|a+b|=|a|+|b|-2\min(|a|,|b|)\mathbf1_{ab<0}.
```

No asymptotics, probability hypothesis, or source simplification occurs.

For odd N the exact version uses `L=floor(N/2)`, `M=N-L`, weights `p=L/N`, `q=M/N`,
and overlap

```math
\Omega_N^{\mathrm{wt}}=\int_0^1
\min\{p|H_-(t)|,q|H_+(t)|\}\mathbf1_{H_-(t)H_+(t)<0}\,dt.
```

It gives `D_N=p D_-+q D_+-2 Omega_N^wt`. This is the version to implement if all
integer N, rather than only dyadic prefixes, are used in a proposed proof.

### What would close the hole

For example, a source-derived pair of estimates

```math
D(\mu^+_M)\le D(\mu^-_M)+a_M,\qquad
\Omega_M\ge\gamma D(\mu^-_M)-b_M,
```

with fixed `gamma>0` and `a_M,b_M->0`, would give
`D_(2M)<=(1-gamma)D_M+a_M/2+b_M`. The odd-N version needs the corresponding endpoint
or weighted payment. These are sufficient hypotheses, **not established BBP facts**.
They explain exactly where a real signed saving must enter.

For constant-zero orbits the two CDF defects coincide, `Omega_M=0`, and
`D_(2M)=D_M=15/32`. Thus this instrument fails the hostile orbit in the required
way. If a proposed argument silently inserts a positive universal overlap, this
control refutes it immediately.

For rational atomic inputs, D and Omega are exact rational integrals: collect all
atoms of `mu^-`, `Q mu^-`, `mu^+`, `Q mu^+`, sort their rational coordinates, and
integrate the constant CDF differences over each adjacent interval. This is useful
for a finite receipt, but a finite observed overlap cannot certify its asymptotic
lower bound.

## 4. Source-specific attempt: positivity and all finite differences

The authentic four-pole forcing has the exact integral representation

```math
r(n)=\int_0^1 x^{8n-8}P(x)\,dx,\qquad
P(x)=4-2x^3-x^4-x^5
     =(1-x)(x^2+2)(x^2+2x+2).
```

Therefore it is positive, decreasing, and completely monotone as a sequence:

```math
(-1)^k\Delta^k r(n)
=\int_0^1x^{8n-8}(1-x^8)^k P(x)\,dx>0
\quad(n\ge1,\ k\ge0).
```

This proves a whole Pascal-weighted tower of **source** signs. It does not prove the
signs or sizes of the **orbit-statistic** overlap in Section 3. The map from the
source to a digit involves unbounded expansion, integer carries, and fractional
part; it does not preserve these finite-difference signs.

The useful exact upper bound

```math
0<r(n)\le\frac{15}{(8n-7)(8n-6)}
```

follows from `P(x)<=15(1-x)`. For `n>=2` this is at most `2/(3n^2)`, and hence

```math
\sum_{n\ge1}r(n)<\frac{47}{15}+\frac23=\frac{19}{5}.
```

The future-tail formula becomes

```math
T_n=\int_0^1\frac{x^{8n}P(x)}{16-x^8}\,dx.
```

These bounds support rigorous tail certificates and source authentication. They do
not create a signed mean estimate.

### Explicit calculation of what source differencing actually pays

Let `e(x)=exp(2 pi i x)` and `c_N(h)=N^-1 sum_(n<N)e(h U_n)`. The source recurrence
gives

```math
e(hU_{n+1})-e(16hU_n)
=e(16hU_n)(e(hr(n+1))-1).
```

After summation, the elementary bound `|e(t)-1|<=2 pi |t|` yields

```math
|c_N(16h)-c_N(h)|
\le\frac{2+(38\pi/5)|h|}{N}.
```

This is a genuine proved estimate from the authenticated source. It controls the
**difference between two means**, not either mean. For the completed orbit the
same frequency transport already has the exact endpoint bound `2/N`. A constant
completed orbit with all these means equal to one satisfies this estimate.
Consequently this route yields stationarity without statistical contraction.

For a lag `ell>=1`, exact iteration gives

```math
U_{n+\ell}-U_n=(16^\ell-1)U_n+R_\ell(n),\qquad
R_\ell(n)=\sum_{j=1}^\ell16^{\ell-j}r(n+j).
```

For `n>=1`, monotonicity and the bound above imply

```math
0<R_\ell(n)
\le\frac{16^\ell-1}{(8n+1)(8n+2)}.
```

Thus a lag-differencing argument replaces the original phase by a phase at the
new frequency `h(16^ell-1)`, with a certified error at most
`2 pi |h|(16^ell-1)/((8A+1)(8A+2))` per term on an epoch starting at A. This can make
the **transport error** small for slowly growing lag windows. It supplies no bound
for the new signed mean. Repeating the transformation creates more unresolved
frequencies; it does not multiply the original defect by a factor below one.

**Verdict of this source-specific attempt:** the full positive Pascal tower and
summable forcing pay analytic transport. They leave the signed source-selected
defect unbounded. This agrees with, but does not merely repeat, the source-root
oscillator no-gain calculation in
`../bbp_graph_resonance/RESEARCH_NOTE.md`, R-06: the present calculation operates
directly on the authentic finite recurrence and its lagged phases.

## 5. Four-simple-pole telescoping control

The following fresh control checks that the analytic and source-zero machinery
does not automatically manufacture statistical contraction. It is a different
source, not a purported counterexample to the original four coefficients.

Define, for `n>=0`,

```math
g(n)=\frac1{64(n+1)(n+3/2)},\qquad
\widetilde r(n)=16g(n-1)-g(n)\quad(n\ge1).
```

The forcing has exactly four distinct simple poles:

```math
\widetilde r(n)=\frac1{2n}-\frac1{2n+1}
 -\frac1{32(n+1)}+\frac1{16(2n+3)}.
```

It is rational, positive, completely monotone, and has precisely the authentic
leading quadratic-decay coefficient:

```math
n^2\widetilde r(n)\longrightarrow\frac{15}{64}.
```

To verify complete monotonicity, use the positive moment density

```math
g(n)=\frac1{32}\int_0^1x^n(1-\sqrt x)\,dx,\qquad
\widetilde r(n)=\frac1{32}\int_0^1x^{n-1}(16-x)(1-\sqrt x)\,dx.
```

The tail telescopes exactly:

```math
\widetilde T_n=\sum_{j\ge1}16^{-j}\widetilde r(n+j)=g(n),\qquad
\widetilde\alpha=\widetilde T_0=\frac1{96}.
```

With the literal zero initial seed,
`U~_n=16^n/96-g(n)`. The completed circle orbit is

```math
\frac1{96},\quad\frac16,\quad\frac23,\quad\frac23,\quad\ldots.
```

It is eventually the hexadecimal fixed digit A. For `x=2/3`,

```math
D(\delta_x)=\frac1{256}\sum_{a=0}^{15}|10-a|=\frac{35}{128}>0.
```

Hence this source has a correct natural-zero invariant, a unique bounded tail
fixed point, four simple rational poles, the same leading `n^-2` forcing constant,
and the entire positive finite-difference/Pascal source tower, yet fails the
requested contraction. Any proof that uses only those features is refuted.
This control changes the pole locations and residues; it does not refute a theorem
using the exact authentic BBP source. It also makes no claim to preserve the
parameter resonance studied in the separate graph-resonance dossier.

## 6. A canonical observable compiler and its remaining innovation

Let `C^*f(y)=16^-1 sum_(a=0)^15 f((a+y)/16)` on functions. For a Lipschitz f with
Lebesgue mean zero, define

```math
\psi_f=\sum_{k\ge0}(C^*)^k f.
```

The series converges uniformly. One proof uses the shifted Riemann-sum estimate
`||(C^*)^k f||_infty<=Lip(f)/(2*16^k)`; its endpoints are included. Consequently
`||psi_f||_infty<=8 Lip(f)/15`, `Lip(psi_f)<=16 Lip(f)/15`, and
`f=psi_f-C^*psi_f`.

For the actual source orbit, summing this identity gives the exact formula

```math
\sum_{n=0}^{N-1}f(z_n)
=\sum_{n=0}^{N-1}
 \big[\psi_f(z_n)-C^*\psi_f(z_{n+1})\big]
 +C^*\psi_f(z_N)-C^*\psi_f(z_0).
```

The bracket is the signed leading-digit innovation conditioned on the real future.
The compiler can generate it and bound the endpoint by `Lip(f)/15`. Its mean is
not zero merely because its hypothetical average over sixteen newly chosen leading
digits is zero. The authentic path chooses one digit.

For the first moment `f(x)=x-1/2`, the construction is especially transparent:

```math
\psi_f(x)=\frac{16}{15}(x-1/2),\qquad
\psi_f(z_n)-C^*\psi_f(z_{n+1})=\frac{d_n-15/2}{15}.
```

It exposes the actual digit-mean obligation instead of discharging it. For a
nonzero integer Fourier character, `C^* e_h=0` unless `16` divides h, in which case
`C^* e_h=e_(h/16)`. The Poisson series therefore terminates after `v_16(h)+1` terms.
At a frequency not divisible by 16 the remaining innovation is the original
character itself. This is an exact finite normal form with a visible unresolved
statistical premise.

### A precise denotational grammar for the Poisson observer

The paper construction admits a small finite grammar; this paragraph describes
its mathematical contract and does not claim an additional implemented parser.
An input observer is either a rational polynomial on `[0,1]`, represented by its
finite coefficient tuple `(a_0,...,a_d)`, or an integer Fourier character `e_h`.
Rational constants, the phase variable, addition, multiplication and rational
scaling generate the polynomial fragment. A nonnegative integer L is the finite
unfolding depth. The following rewrites are exact operations on that grammar:

```text
center(f)       = f - integral_0^1 f(x) dx
inverse(f)(y)   = (1/16) sum_{a=0}^{15} f((a+y)/16)
poisson(f, L)   = sum_{k=0}^{L-1} inverse^k(center(f))
innovation(g)   = g(z_n) - inverse(g)(z_(n+1))
```

For a rational polynomial, centering integrates each coefficient as `a_k/(k+1)`;
the inverse operation is a finite binomial expansion with rational coefficients.
The rational number `sum_(k>=1) k |a_k|` is an independently computable Lipschitz
upper bound M. It yields the rigorous uniform unfolding error

```math
\|\psi_f-\operatorname{poisson}(f,L)\|_\infty
\le\frac8{15}\,M\,16^{-L}.
```

For `h!=0`, the Fourier fragment terminates exactly under the divisibility rule
already displayed; for `h=0`, centering produces the zero observer. The grammar
never contains a rewrite assigning zero to an authentic nontrivial innovation.
Its output is a finite expression plus a proved approximation bound. A later
assertion that the time average of that expression vanishes requires a separate
arithmetic theorem.

### Pascal–Fourier observer certificate

This also verifies the quantitative observer claim made in the preceding
conversation. Let `omega=exp(2 pi i/16)`, let
`B_(m,j)(y)=binom(m,j)y^j(1-y)^(m-j)`, and set

```math
G_{h;m,j}(N)=\frac1N\sum_{n<N}\omega^{h d_n}B_{m,j}(z_{n+1}),
\qquad 1\le h\le15,\quad0\le j\le m.
```

For **every** `N>=1` and **every** integer `m>=1`, using the same N observations
`n=0,...,N-1` and the N matching future phases `n=1,...,N`,

```math
D_N\le\frac12\sum_{h=1}^{15}\sum_{j=0}^{m}|G_{h;m,j}(N)|
       +\frac1{16\sqrt m}.
```

To prove this, test against a 1-Lipschitz f, subtract its value at `1/2`, and
approximate each function `y -> f((d+y)/16)` by its degree-m Bernstein polynomial.
Its uniform approximation error is at most `1/(32 sqrt(m))`, by the binomial
variance bound. Evaluating the difference of the two probability laws costs twice
this error. Discrete Fourier inversion of the sixteen coefficient values
`f((d+j/m)/16)` removes the constant character; each remaining coefficient has
absolute value at most `1/2` because `|f|<=1/2`. The signed moments left after this
inversion are exactly G. Taking the supremum over f proves the displayed bound.

Combining it with Section 2 gives the valid finite estimate

```math
W_1(\mu_N,\lambda)
\le\frac8{15}\sum_{h=1}^{15}\sum_{j=0}^{m}|G_{h;m,j}(N)|
 +\frac1{15\sqrt m}+\frac{|z_N-z_0|}{15N}.
```

In particular, vanishing of every fixed G implies normality: first fix m and let
N tend to infinity, then let m tend to infinity. Conversely normality implies
vanishing of each G, since the associated function of z has only finitely many
discontinuities and zero Lebesgue mean. Thus the Pascal–Fourier criterion is exact.
The earlier conversational bound with coefficient `16/15` on the sum was weaker
but valid. The proof authenticates the observer reduction; it leaves every
source-specific asymptotic G estimate open.

### Classical discrepancy restricts the possible remainder

**Status: CLASSICAL IMPORT + derived corollary; no novelty claim.**
An imported theorem further restricts the target. Kritzinger and Pillichshammer,
[*Exact order of extreme Lp discrepancy of infinite sequences in arbitrary
dimension*](https://doi.org/10.1007/s00013-021-01688-9), Theorem 1 (`d=1,p=1`),
gives a positive constant c such that every infinite sequence satisfies

```math
N W_1(\mu_N,\lambda)\ge c\sqrt{\log N}
\quad\text{for infinitely many }N.
```

Their extreme discrepancy is at most the star L1 discrepancy, which equals the
left side: integrate `|Delta(v)-Delta(u)|<=|Delta(v)|+|Delta(u)|` over `u<=v`.

Consequently **no actual orbit** satisfies the all-N contraction with
`theta<1/2` and `epsilon_N=O(1/N)`. Indeed, choose `rho` between `2 theta` and 1.
For large N, multiplying the recurrence by N gives
`N D_N<=rho (floor(N/2) D_floor(N/2))+C`. Induction bounds `N D_N` uniformly.
Section 2 would then bound `N W_1(mu_N,lambda)` uniformly, contradicting the
imported theorem. This is a classical discrepancy consequence, not a new BBP
claim. A slower vanishing remainder such as `O(N^-1/2)` is compatible with this
obstruction; its validity for the exact BBP source still requires proof. The
all-N quantifier is essential, since exceptional subsequences can have smaller
error.

## 7. Earned result and next discriminant

**Established here:** the signed Poisson reconstruction, exact dyadic overlap
identity, explicit source finite-difference and lag-transport estimates, and the
four-pole rational hostile control. The analytic contraction and original-zero
authentication can be implemented faithfully, and their residuals can be checked
through independent finite paths.

**Not established:** a positive asymptotic overlap lower bound, an independent
vanishing remainder in the requested sample-length contraction, or cancellation
of any authentic nontrivial signed digit character. Pi normality and its weaker
original-zero parity balance remain OPEN.

**Next verdict-changing probe:** derive a source-specific bound on the signed
overlap (or on the corresponding conditional innovation) which uses the exact
four BBP residues and rejects both the coherent wrong seed and the changed-source
telescoping control. A finite overlap receipt can reject a proposed quantitative
constant; it cannot establish the all-large-N estimate.
