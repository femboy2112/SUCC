# Cloud lane C: finite clocks to an absolutely convergent singular series

**Base:** `main` at `0e56e0ae26f3d52a2ea34c0a4288478139fcb634`.
**Read-only comparison:** PR #201 at
`cbc4010458c00be995b8af3f229c9bba410301e2`.
**Scope:** classical arithmetic recovered with self-contained proofs, explicit
elementary tail constants, and independent exact computational controls.
**Binary Goldbach, integer abc, and RH remain OPEN.** No zero data are used.

## 1. Hole contract and result

The proposed bridge is, for each fixed **nonzero** integer `N`,

\[
\text{finite unit clocks}\longrightarrow\text{finite characters}
\longrightarrow\sum_{q\ge1}a_q(N)
=\prod_p(1+a_p(N)),\qquad
a_q(N)=\frac{\mu(q)^2c_q(N)}{\varphi(q)^2}.
\]

The finite-to-infinite arrow needs absolute summability, and moving `N` needs an
explicit `N`-dependent error. These are supplied below. `N=0` is a counterexample
to the unqualified integer statement. A prime cutoff and a modulus cutoff have
different supports, so each receives its own estimate. The useful new-to-project
capability is a rational enclosure that does **not** require factoring the large
residual of `N` or choosing the prime cutoff beyond its largest prime divisor.

The weakest sufficient result is convergence for fixed `N != 0` plus a stated
tail budget. It closes a harmonic arithmetic interface, not the missing
minor-arc estimate in binary Goldbach. Novelty tax: the underlying identities
are classical. The explicit conservative bounds are elementary derivations
here, without a literature-priority claim. Finite checks below validate the
implementation, not the universal statements. The independent routes are
direct unit enumeration and cyclotomic character reduction versus the divisor
formula, and geometric-series/Euler bounds versus finite tail censuses.

## 2. Exact arithmetic and the finite harmonic bridge

For positive integer `q` and integer `N`, define

\[
c_q(N)=\sum_{\substack{0\le a<q\\(a,q)=1}}e(aN/q),\qquad
e(t)=\exp(2\pi i t),\qquad c_1(N)=1.
\]

### C-RAM-01 — divisor formula and CRT multiplicativity (CLASSICAL)

For every `q >= 1`, `N in Z`,

\[
c_q(N)=\sum_{d\mid(q,N)}d\mu(q/d),\qquad c_q(-N)=c_q(N)\in\mathbb Z.
\tag{1}
\]

If `(q,r)=1`, then `c_{qr}(N)=c_q(N)c_r(N)`.

**Proof.** Insert
`1_{(a,q)=1}=sum_{d|a,d|q} mu(d)` into the character sum. For each `d|q`,
write `a=db`, with `b` ranging over `q/d` residue classes. Finite geometric
orthogonality gives `sum_b e(bN/(q/d))=q/d` when `q/d|N` and zero otherwise.
Changing the divisor variable gives (1), including `N=0`. This proves integrality
and evenness. For coprime `q,r`, every divisor of `(qr,N)` splits uniquely into
coprime divisors of `(q,N)` and `(r,N)`, and Möbius multiplicativity factors (1).
Alternatively CRT identifies additive characters after multiplication by the
invertible CRT coordinates; multiplication by a unit permutes the primitive
residues. No analytic limit has been used. In particular,

\[
c_p(N)=\begin{cases}p-1&p\mid N,\\-1&p\nmid N.\end{cases}\tag{2}
\]

### C-RAM-02 — normalized unit-pair density (CLASSICAL; exact finite bridge)

Set `U_q(N)=#{x mod q : (x,q)=(N-x,q)=1}`. For all `q >= 1`, `N in Z`,

\[
\frac{qU_q(N)}{\varphi(q)^2}
=\sum_{d\mid q}\frac{\mu(d)^2c_d(N)}{\varphi(d)^2}
=\prod_{p\mid q}\left(1+\frac{c_p(N)}{(p-1)^2}\right).
\tag{3}
\]

**Harmonic proof.** Let
`rho_q(x)=q/phi(q) 1_{(x,q)=1}` on `Z/qZ`. Directly from (2),

\[
\rho_q(x)=\prod_{p\mid q}\left(1-\frac{c_p(x)}{p-1}\right)
=\sum_{d\mid q}\frac{\mu(d)}{\varphi(d)}c_d(x).
\]

The first equality has value zero if any `p|q` divides `x`; otherwise it is
`prod p/(p-1)=q/phi(q)`. The second uses (1)'s multiplicativity and squarefree
support. Expand the normalized convolution
`q^{-1} sum_x rho_q(x) rho_q(N-x)`. The reduced rational character frequencies
in `c_d` and `c_e` coincide modulo one only when `d=e` and their numerators
coincide; finite orthogonality therefore gives

\[
\frac1q\sum_{x\bmod q}c_d(x)c_e(N-x)
=\mathbf1_{d=e}c_d(N),\qquad d,e\mid q.
\]

This proves the first equality of (3); multiplicativity proves the second.
This is the additive convolution, with the argument `N-x`, not the difference
correlation with `N+x` substituted without tracking the character signs.

**Different combinatorial proof.** CRT gives `U_{qr}=U_qU_r` for coprime moduli.
For `p^k`, there are `p-1` permissible residue classes modulo `p` when `p|N`,
and `p-2` otherwise, each with `p^{k-1}` lifts. Multiplying
`p^k U_{p^k}/phi(p^k)^2` gives exactly the local factor in (3). Higher clock
depth changes the sample space but not this normalized unit-pair density.

## 3. Convergence, normalization, and the zero exception

### C-RAM-03 — absolute convergence for fixed nonzero N (CLASSICAL)

For each fixed integer `N != 0`,

\[
\sum_{q\ge1}|a_q(N)|<\infty,\qquad
\mathfrak S(N)=\sum_{q\ge1}a_q(N)
=\prod_p\left(1+\frac{c_p(N)}{(p-1)^2}\right).
\tag{4}
\]

**Proof.** The coefficients are multiplicative, vanish at nonsquarefree `q`,
and satisfy `|a_p|=1/(p-1)` when `p|N`, and `|a_p|=1/(p-1)^2` otherwise.
There are finitely many primes dividing this nonzero `N`, and
`sum_p (p-1)^{-2}<infinity`. Thus `sum_p |a_p|<infinity`.
The finite expansions
`prod_{p<=P}(1+|a_p|)=sum_{q squarefree, p|q => p<=P}|a_q|`
are bounded above by `exp(sum_p|a_p|)`. Every squarefree `q` eventually occurs,
so monotone exhaustion proves absolute summability. Dominated exhaustion now
allows the signed finite products to converge to the ordinary series. This
explicit summability argument is the analytic step that a merely formal Euler
expansion would lack. Section 5 gives a quantitative alternative proof.

When `N` is odd, the `p=2` factor is zero, so `S(N)=0`. When `N` is even and
nonzero, all factors are positive and

\[
\mathfrak S(N)=2C_2\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2},
\quad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)>0.
\tag{5}
\]

The positive product assertion follows because the sum of its missing factors
is finite, and sufficiently far tails are bounded below by one minus that sum.
The factor `2` comes from `p=2`; it must not be dropped or counted twice.
`2C2` equals `S(2^k)` for `k>=1`, not `S(2p)` for odd prime `p`.
Indeed `S(6)=4C2`, `S(10)=(8/3)C2`. An odd local obstruction does not say that
an odd integer has no representations involving the prime `2`.

### C-RAM-04 — N=0 is excluded (REFUTED universal extension)

At `N=0`, `c_q(0)=phi(q)`, hence `a_q(0)=mu(q)^2/phi(q)>=0`.
Its finite squarefree Euler sums equal `prod_{p<=P}(1-1/p)^{-1}`.
Expanding each geometric factor shows that this product dominates
`sum_{n<=floor(P)}1/n`, since all prime factors of such `n` are at most `P`.
The harmonic sums diverge. Thus the series for `N=0` diverges to infinity;
absolute convergence for every integer `N` would be false.

## 4. Prime cutoff without factoring the unseen residual

Let integer `P>=2`, `N!=0`, and

\[
F_P(N)=\prod_{p\le P}(1+a_p(N)),\quad
R=|N|\prod_{p\le P}p^{-v_p(N)},\quad
k=\lfloor\log_{P+1}R\rfloor,
\quad E_P=\frac1{4\lceil P/2\rceil-2}.
\]

Here `k` is computed by exact integer comparisons, with `k=0` when `R=1`.
Only trial division by primes at most `P` is required; the remaining integer
`R` is not factored.

### C-RAM-05 — rational enclosure (PROVED LOCAL / elementary universal bound)

For even nonzero `N` and `P>=2`,

\[
F_P(N)(1-E_P)\ \le\ \mathfrak S(N)
\ \le\ F_P(N)\left(\frac P{P-1}\right)^k.
\tag{6}
\]

For odd nonzero `N`, both endpoints in (6) are zero and the value is exactly
zero. The returned interval is rational. It applies even if an unseen prime
divisor of `N` is vastly larger than `P`.

**Proof.** Since `P>=2`, every omitted prime is odd. Put `m=ceil(P/2)`.
For any finite tail,

\[
\sum_{p>P}\frac1{(p-1)^2}
\le\sum_{j=m}^{\infty}\frac1{4j^2}
\le\sum_{j=m}^{\infty}\frac1{4j^2-1}
=\frac1{2(2m-1)}=E_P.
\]

The last sum telescopes because
`1/(4j^2-1)=1/2(1/(2j-1)-1/(2j+1))`. Multiplying factors `1-u_j`,
with `0<=u_j<=1`, gives at least `1-sum u_j`; pass to the limit to obtain
`1-E_P <= B_P <=1` for the generic tail
`B_P=prod_{p>P}(1-(p-1)^{-2})`. The true tail is

\[
\frac{\mathfrak S(N)}{F_P(N)}
= B_P\prod_{\substack{p>P\\p\mid N}}\frac{p-1}{p-2}.
\]

If `j` distinct unseen primes divide `N`, then `(P+1)^j<=R`, so `j<=k`.
Each correction is at most `1+1/(P-1)=P/(P-1)` and at least one. This gives
both inequalities in (6). For odd `N`, use the exact parity factor instead of
dividing by `F_P=0`.

**Moving-N range.** Uniformly over even `2<=|N|<=M(P)`, the relative error of
`F_P` tends to zero if `P->infinity` and

\[
\frac{\log M(P)}{P\log(P+1)}\longrightarrow0.
\tag{7}
\]

Indeed `k<=log M/log(P+1)` and the upper ratio in (6) is at most
`exp(k/(P-1))`; the lower relative defect is `E_P`. This is a sufficient
regime, not a necessity claim and not uniformity over all integers.

**Unrestricted uniformity is false.** For fixed `P`, take `N` to be the product
of all primes at most `T>P`. The correction in the proof contains
`prod_{P<p<=T}(p-1)/(p-2)`, which diverges as `T` grows: each factor exceeds
`p/(p-1)`, and the latter product diverges by the harmonic-series argument of
C-RAM-04. The generic tail `B_P` is a fixed positive number. Thus
`S(N)/F_P(N)` is unbounded over even `N`. For each increasing `P`, choosing
`T(P)` sufficiently large also destroys unrestricted moving-`N` convergence.

**Hostile control.** At `N=10,P=3`, `F_P=3/2`; the omitted `p=5` correction
makes the true value larger than this proposed upper bound. The code certifies
that the lower endpoint at `P=101` exceeds `3/2`. Thus simply deleting the
old largest-prime-divisor precondition would be unsound. Formula (6) supplies
the missing upper correction.

## 5. A different truncation: ordinary modulus tails

### C-RAM-06 — elementary totient-square tail lemma (PROVED LOCAL)

For every real `Y>0`,

\[
\sum_{n>Y}\frac1{\varphi(n)^2}<\frac{12}{Y}.
\tag{8}
\]

**Proof with explicit constant.** Define nonnegative multiplicative `h` by
`h(p)=(2p-1)/(p-1)^2` and `h(p^j)=0` for `j>=2`. Then
`n^2/phi(n)^2=sum_{d|n}h(d)`. Moreover

\[
H=\sum_{d\ge1}\frac{h(d)}d
=\prod_p\left(1+\frac{2p-1}{p(p-1)^2}\right)<6.
\]

To justify the bound and convergence without a hidden analytic estimate,
separate `p=2,3,5,7`. For `p>=11`,
`(2p-1)/(p(p-1)^2)<=3/(p(p-1))`, whose sum is at most
`sum_{n>=11}3/(n(n-1))=3/10`. For nonnegative `u_j` with sum `s<1`, finite
product expansion gives `prod(1+u_j)<=sum_{r>=0}s^r=1/(1-s)`.
Thus the omitted product is at most `10/7`, and

\[
H\le\frac52\frac{17}{12}\frac{89}{80}\frac{265}{252}\frac{10}{7}
=\frac{2004725}{338688}<6.
\]

Monotone exhaustion justifies the equality defining `H`. For all real `T>0`,
`sum_{j>T}j^{-2}<=2/T`: if `T<1`, use `sum j^{-2}<=2`; otherwise integrate
from `floor(T)` and use `floor(T)>=T/2`. Nonnegative rearrangement now gives

\[
\sum_{n>Y}\frac1{\varphi(n)^2}
=\sum_{d\ge1}\frac{h(d)}{d^2}\sum_{j>Y/d}\frac1{j^2}
\le\frac2Y\sum_{d\ge1}\frac{h(d)}d<\frac{12}Y.
\]

### C-RAM-07 — rational modulus-tail certificate (PROVED LOCAL)

For integer `N!=0`, real `Q>0`, let

\[
D(N)=\prod_{p\mid N}\left(1+\frac p{p-1}\right).
\]

Then

\[
\sum_{q>Q}|a_q(N)|\le\frac{12D(N)}Q,
\qquad
\left|\mathfrak S(N)-\sum_{q\le Q}a_q(N)\right|
\le\frac{12D(N)}Q.
\tag{9}
\]

**Proof.** Only squarefree `q` matter. Write uniquely
`q=dr`, where `d|rad(|N|)` and `(r,N)=1`. Then `(d,r)=1` and
`|a_q(N)|=1/(phi(d)phi(r)^2)`. Drop the restrictions on `r` to obtain

\[
\sum_{q>Q}|a_q(N)|
\le\sum_{d\mid\operatorname{rad}(|N|)}\frac1{\varphi(d)}
     \sum_{r>Q/d}\frac1{\varphi(r)^2}
\le\frac{12}Q\sum_{d\mid\operatorname{rad}(|N|)}\frac d{\varphi(d)}
=\frac{12D(N)}Q.
\]

For integer `Q>=1`, the finite sum and radius are rational. Intersect its
interval with `[0,infinity)`; for odd nonzero `N`, parity gives the sharper
exact interval `[0,0]`. Computing `D(N)` here uses factorization of `|N|`,
unlike the prime-cutoff certificate (6).

**Moving-N regime.** Formula (9) is uniform with the explicitly displayed
dependence on `N`. It tends to zero along any family with `D(N)/Q -> 0`.
For each fixed `epsilon>0` there is an explicit finite constant

\[
C_\epsilon=
\prod_{p\le 3^{1/\epsilon}}
\max\left(1,\frac{1+p/(p-1)}{p^\epsilon}\right)
\]

such that `D(N)<=C_epsilon |N|^epsilon`: for larger primes the numerator is
at most `3<=p^epsilon`, and multiply the inequalities over the prime support.
Consequently for any fixed `A>0`, (9) tends to zero uniformly on
`0<|N|<=Q^A`, choosing `epsilon<1/A`. Constants may depend on `A` through
`epsilon`; this is not a uniform claim when `A` itself grows.

The constant `12` is conservative and no optimality is claimed. Published
pointwise bounds use a different `N` factor and logarithmic dependence on the
cutoff; see the source note below. This elementary bound is useful because its
entire numerical error budget is rational and independently reproduced here.

**Prime versus modulus cutoff.** `F_P` sums over all squarefree divisors of
the primorial, including many `q>P`; it is not `sum_{q<=P}a_q`.
At `N=2,P=Q=3`, these are respectively `3/2` and `7/4`. No replacement of
one cutoff by the other is licensed without an error calculation.

## 6. Validation, prior art, and remaining obligations

| Claim | Status and proof | Independent check | Remaining boundary |
|---|---|---|---|
| C-RAM-01–03 | CLASSICAL; complete elementary derivations above | Primitive-character polynomials reduced modulo cyclotomic polynomials; direct unit counts and CRT counts | Not Lean-formalized |
| C-RAM-04 | REFUTED extension to `N=0`; harmonic divergence proof | Infinite-series API rejects zero, finite `c_q(0)=phi(q)` checked | Finite products still well-defined at zero |
| C-RAM-05 | PROVED LOCAL elementary universal enclosure and sufficient moving range | Larger finite products; exact unseen-divisor mutation at `(10,3)` | Conservative bound; no unrestricted moving-N limit |
| C-RAM-06–07 | PROVED LOCAL elementary universal tail estimates | Exact rational finite totient and coefficient tails; overlap with independently formed prime-product intervals | Factorization needed for `D(N)`; constants not optimal |
| Binary Goldbach inference | UNVERIFIED / not supplied | No prime-representation assertion is returned by the API | A prime-weighted major/minor-arc theorem, especially minor-arc control, is still required |

Primary-source reconstruction:

1. S. Ramanujan, *On certain trigonometrical sums and their applications in the
   theory of numbers*, Transactions of the Cambridge Philosophical Society 22
   (1918), 259–276, [§2, equations (2.6)–(2.7)](https://ramanujan.sirinudi.org/Volumes/published/ram21.pdf).
   The finite primitive-root sum and Möbius inversion recover (1). The primary
   paper distinguishes elementary series manipulations from identities requiring
   deeper convergence input; no stronger infinite expansion from that paper is
   needed here.
2. D. A. Goldston, J. Z. Hunts, T. Ngotiaoco, *The tail of the singular series
   for the prime pair and Goldbach problems*, arXiv:1409.2151v1,
   [§1, equations (1.2)–(1.9)](https://arxiv.org/html/1409.2151v1).
   The paper states the nonzero-even/odd normalization, Ramanujan expansion,
   divisor identities, and the ordinary modulus tail. Its reported
   Montgomery–Vaughan bound is `O(d(N)(log log(3Q))^2/Q)`; the implicit constant
   is not used by our checker. Its mean-square tail results are separate from
   the pointwise enclosure proved here. No such average theorem is silently
   promoted to all-input Goldbach.
3. [NIST DLMF §27.10, equations 27.10.2–27.10.5](https://dlmf.nist.gov/27.10)
   identifies finite Fourier inversion and the Ramanujan divisor formula.
   [§27.4, equation 27.4.1](https://dlmf.nist.gov/27.4) explicitly requires
   absolute convergence for the analytic Euler identity. These are authoritative
   reference checks; our proofs above rebuild the required special cases.

There is no claim of a new classical identity or publishable novelty. The
new-to-project synthesis is the explicit lawful sequence from actual finite
unit clocks to an infinite arithmetic object with two distinct certified tails.
The root coordinator owns common-index reconciliation and broad regressions.
This branch only adds its own module, tests, dossier, probe and receipt; it does
not edit `goldbach_circle.py`, proof authority, archives, or Claude's branches.
The separate hostile lane found that PR #201 accepts a fractional cutoff
`P=5/2` in one enclosure path and can emit the invalid interval `[1/3,1]` for
`N=2`. This branch rejects noninteger cutoffs (including booleans and rational
objects) before computation; its regression includes that precise input.

Reproduce the independent controls:

```sh
python -m unittest discover -s tests -p 'test_cloud_ramanujan_transport.py' -v
python scripts/cloud_ramanujan_probe.py
```

Observed on 2026-10-20: the focused suite ran **13 tests, all passed** (14.162 s)
in the shared research virtual environment. The initial bare runtime lacked
SymPy; the successful run used the repository's declared test dependency, not a
skipped oracle. The probe completed and `git diff --check` was clean. The separate
cloud referee read the complete proof and independently checked the `H<6`
arithmetic, rearrangement, `q=dr` split, and prime-tail enclosure without finding
a defect. This is a same-model, different-task algebraic audit, not independent
human refereeing or formal-kernel verification. It did not attest the test code
or independently reproduce the literature search. Broad regression is owned
by the coordinator.

The probe writes JSON to stdout; the committed receipt records the observed run.
Universal proofs are the arguments above, not that receipt. Formal verification
status: **not formalized in Lean**. SymPy is only used in the test-side independent
cyclotomic oracle; the certificate module itself uses the standard library.

**Next verdict-changing probe.** Combine the modulus-tail budget (9), with all
`N` dependence retained, with a genuine prime-weighted major-arc approximation
from Claude's separate lane. The remaining Goldbach gap is a **pathway gap** in
the analytic prime correlation/minor-arc estimate, not missing local positivity
or a failed Euler product. A narrower engineering improvement is to replace the
coarse `D(N)` bound by exact residual divisor information while preserving the
ordinary modulus ordering.
