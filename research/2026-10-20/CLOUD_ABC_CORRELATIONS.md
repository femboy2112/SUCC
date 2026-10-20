# Cloud ABC correlations: primitive slope packing breaks the diagonal ceiling

Date: 2026-10-20. Parent: `0e56e0ae26f3d52a2ea34c0a4288478139fcb634`.
Cloud-owned branch: `research/astra-cloud-abc-correlations-2026-10-20`.
**Status: PROVED LOCAL in the sense of the repository (complete paper proof;
not Lean-verified). New-to-project synthesis of elementary classical methods;
no claim of research novelty. Integer abc and RH remain OPEN.**

## 1. Hole contract and theorem

For real `X>=2`, count ordered positive primitive triples `a+b=c<=X`,
`gcd(a,b)=1`. Write `rad(n)=prod_{p|n}p`, `ris(n)=n/rad(n)`, and

\[
S_t(X)=\sum_{a+b=c\le X,\ (a,b)=1}\operatorname{ris}(abc)^t.
\]

The previous diagonal proof needed `0<=t<1/2`. The target is a uniform
quadratic bound for at least one `t>=1/2`, without assuming integer abc,
independence of integer prime clocks, or a moving-modulus asymptotic.

**Theorem CLOUD-ABC-01.** For every real `0<=t<2/3`, put
`delta=2/3-t` and `eta=delta/2`. Define the convergent products

\[
 A_p(t)=\frac{p^t-1}{p^2(1-p^{t-1})},\quad
 E_3(t)=\prod_p(1+3A_p(t)),\quad
 C_\eta=\prod_p\left(1+\frac{2}{p(p^\eta-1)}\right).
\]

Then, for **every real `X>=2`**,

\[
\boxed{S_t(X)\le\left(2E_3(t)+\frac{2C_\eta}{2/3-t}\right)X^2.}
\]

All constants depend only on `t`. There is no restricted prime support,
exponent-depth cutoff, balance assumption, exceptional triple set, or
unproved analytic input. In particular this reaches `t=1/2` and `t=3/5`.
The proof is in Sections 2--6; Section 10 also proves the full Euler-product
mean-value asymptotic in the same range. Its novelty tax is paid as a **new-to-project
proof step**, not a claim to academic priority: elementary divisor expansion,
primitive lattice packing, and Rankin bounds are classical.

Weakest useful consequence: `S_(1/2)(X)=O(X^2)`. Dependency closed: replacing
the inner diagonal Cauchy--Schwarz loss by a joint primitive arithmetic count.
Cheapest falsifiers: delete primitivity from the spacing lemma; remove the
`D<=X^2` gate; test deep powerful triples. These mutations fail in Section 7.
The remaining interval `2/3<=t<1` is not settled by this proof.

## 2. Exact divisor expansion and additive compatibility

For `t>=0`, let `f_t(n)=ris(n)^t`, `g_t=mu*f_t` (Dirichlet convolution).
Both are multiplicative, `g_t(1)=1`, and

\[
g_t(p)=0,\qquad
g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}\quad(k\ge2).
\]

Thus `g_t>=0`, and for `t>0` its support is exactly the powerful integers
(all nonzero prime valuations at least two), including 1. For `t=0`, only
`g_0(1)=1` is nonzero. The exact identity is

\[
f_t(n)=\sum_{d\mid n}g_t(d).
\]

For every fixed positive integer `c`, the unrestricted additive correlation
has the exact finite expansion

\[
 I_t(c)=\sum_{d,e<c}g_t(d)g_t(e)C_{d,e}(c),\quad
 C_{d,e}(c)=\#\{1\le a<c:a\equiv0\ (d),\ a\equiv c\ (e)\}.
\]

Put `h=gcd(d,e)`. If `h` does not divide `c`, the count is zero. Otherwise
let `l=lcm(d,e)` and let `r` be the unique compatible residue in `[0,l)`.
Then

\[
 C_{d,e}(c)=\left\lfloor\frac{c-1-r}{l}\right\rfloor
             -\left\lfloor\frac{-r}{l}\right\rfloor.
\]

For the **primitive** correlation, the divisor pair contributes zero unless
`gcd(d,e)=gcd(de,c)=1`. For a surviving pair, exact coprimality is recovered by
summing the above progression count with the additional condition `h|a`,
weighted by `mu(h)`, over `h|c`. Equivalently the moduli are `dh,e` because
`gcd(h,de)=1`. This is inclusion-exclusion, not finite-prime primitivity.
The implementation checks this CRT/Mobius route against direct enumeration.

Finally, for a primitive triple, `a,b,c` are pairwise coprime. Every divisor
triple `d|a,e|b,f|c` is therefore pairwise coprime; this exclusion will be
retained rather than discarded. The prime sum is

\[
\sum_{k\ge2}\frac{g_t(p^k)}{p^k}=A_p(t) \quad(0\le t<1).
\]

Consequently the three-divisor, pairwise-coprime sum is exactly `E_3(t)`.
Indeed at each prime one may occupy only one of the three divisor slots.
Convergence follows from
`A_p(t)<=p^(t-2)/(1-2^(t-1))`, with the case `t=0` immediate.

## 3. Primitive arithmetic packing (the load-bearing invariant)

**Lemma CLOUD-ABC-02.** Let `d,e,f>=1` be pairwise coprime integers, `D=def`,
and let `N_X(d,e,f)` count positive primitive triples `a+b=c<=X` satisfying
`d|a,e|b,f|c`. Uniformly over **all** such moduli and real `X>=2`,

\[
 N_X(d,e,f)\le 1+\frac{X^2}{D}.
\]

**Proof.** Send a triple to its slope `a/c` in `(0,1)`. This is injective:
`gcd(a,c)=1`, so a reduced rational slope determines `(a,c)`, hence `b`.
For two distinct triples,

\[
 \frac a c-\frac {a'}{c'}=\frac{ac'-a'c}{cc'}.
\]

The integer numerator is nonzero. It is divisible by `d` and `f`. It is also
divisible by `e`, since `c=a+b` and `c'=a'+b'`, and hence the numerator equals
`ab'-a'b`. Pairwise coprimality gives divisibility by `D`, so every two slopes
are separated by at least `D/X^2`. Sort the slopes. If there are `n` of them,
`(n-1)D/X^2<1`; the asserted (slightly weaker) bound follows. This proof uses
neither a large-box approximation nor fixed-modulus limits. QED.

For `D<=X^2` it yields `N_X<=2X^2/D`. For `D>X^2`, it actually yields `N_X<=1`.
The latter singleton is essential and cannot be absorbed into `O(X^2/D)`
uniformly. Primitive slope separation is the invariant that the diagonal
one-variable moment estimate discards.

## 4. Low-ris triples: exact summability, with growing divisors allowed

Let `H=ris(abc)` and first sum over `H<=X`. Expand the three weights by Section
2. Every nonzero divisor term has powerful, pairwise-coprime `d,e,f`, so
`D=def` is powerful. For a powerful integer `D`, prime by prime,

\[
 D\le\operatorname{ris}(D)^2.
\]

Also `D|abc` implies `ris(D)|ris(abc)`, again prime by prime. Therefore
`D<=H^2<=X^2`. Exchange the finite nonnegative sums, enlarge each primitive
count by dropping `H<=X`, and apply Section 3:

\[
\begin{aligned}
 S_t^{\le X}(X)
 &\le \sum_{\substack{(d,e)=(e,f)=(f,d)=1\\def\le X^2}}
       g_t(d)g_t(e)g_t(f)N_X(d,e,f)\\
 &\le 2X^2\sum_{(d,e)=(e,f)=(f,d)=1}
          \frac{g_t(d)g_t(e)g_t(f)}{def}
 =2E_3(t)X^2.
\end{aligned}
\]

This part holds for every `0<=t<1`. Moduli grow as far as `def=X^2`, with no
asymptotic in the individual moduli. The powerful-support implication is why
the density estimate is used only within its valid range.

## 5. Uniform radical tail by a separate Rankin argument

For `eta>0`, nonnegative Euler-product expansion gives the exact equality

\[
 \sum_{(m,n)=1}\frac{(mn)^{-\eta}}{\operatorname{rad}(m)\operatorname{rad}(n)}
 =C_\eta<\infty.
\]

To justify the infinite identity, first expand over finitely many primes and
finite exponents and then use monotone convergence. The local factor is
`1+2 sum_(k>=1) p^(-1-k eta)=1+2/[p(p^eta-1)]`. Convergence follows from
`2/[p(p^eta-1)]<=2p^(-1-eta)/(1-2^(-eta))` and the convergent integer series.
Thus, for every real `R>0` and `X>=1`,

\[
 \#\{m,n\le X:(m,n)=1,\operatorname{rad}(m)\operatorname{rad}(n)\le R\}
 \le C_\eta R X^{2\eta}.
\]

For each counted pair, `1<=R X^(2eta)(mn)^(-eta)/(rad(m)rad(n))`; summing and
enlarging to all coprime pairs proves the bound. No divisor-bound constant or
unstated uniformity in a radical exponent is used.

Let `T_X(y)` count primitive triples with `H>y`, for real `y>0`. Then
`rad(abc)=abc/H<X^3/y`. Among the three pair products of radicals one is at
most `rad(abc)^(2/3)`. Each pair determines at most one triple (`a+b=c`, or
subtraction when the pair contains `c`). A union bound over three ordered
slot pairs and the preceding estimate yields

\[
 \boxed{T_X(y)\le 3C_\eta X^{2+2\eta}y^{-2/3}.}
\]

This is uniform simultaneously in `X` and `y`. Using `abc<=X^3/4` would
improve its constant, but is unnecessary.

## 6. Integrating the tail: complete proof of Theorem CLOUD-ABC-01

For `0<t<2/3`, finite layer-cake integration gives

\[
 S_t^{>X}(X)=X^tT_X(X)+t\int_X^\infty y^{t-1}T_X(y)\,dy.
\]

The finite sum has bounded support, so this equality needs no problematic
limit interchange. Substituting the tail estimate, now extending the
majorant to infinity, gives

\[
 S_t^{>X}(X)\le
 3C_\eta\left(1+\frac{t}{2/3-t}\right)
 X^{2+2\eta+t-2/3}
 =\frac{2C_\eta}{2/3-t}X^{2+2\eta+t-2/3}.
\]

Choose `eta=(2/3-t)/2`; the exponent is exactly 2. For `t=0`, the same bound
follows directly from `S_0^{>X}=T_X(X)` (no `0*infinity` operation).
Combining Sections 4 and 6 proves the theorem.

The products admit completely elementary explicit majorants:

\[
 E_3(t)\le\exp\!\left(\frac3{(1-t)(1-2^{t-1})}\right),\qquad
 C_\eta\le\exp\!\left(\frac2{\eta(1-2^{-\eta})}\right).
\]

Here `sum_(n>=2)n^(-s)<=1/(s-1)` for `s>1`, by decreasing-function integral
comparison, and `1+u<=exp(u)`. The code supplies a rational, power-of-two
upper-bound certificate for rational `t`, using integer root brackets and
`exp(r)<4^r`; constants are intentionally very loose.

## 7. Hostile boundaries and failed upgrades

1. **Deleting primitivity destroys the theorem, not merely its proof.**
   For `(a,b,c)=(n,n,2n)`, `ris(abc)>=n^2` because `rad(2n)<=2n`. Thus the
   nonprimitive moment grows at least as `X^(1+2t)` and cannot be `O(X^2)`
   for `t>1/2`. The spacing lemma also has a small exact mutant: at `X=34`,
   pairwise-coprime moduli `(d,e,f)=(8,9,17)` admit `(8,9,17)` and
   `(16,18,34)` when primitivity is omitted, but `2>1+34^2/1224=35/18`.
2. **Dropping the singleton term is false even on powerful support.** The
   primitive Pythagorean triple of summands `(a,b,c)=(441,400,841)` has
   pairwise-coprime powerful entries. With `(d,e,f)=(a,b,c)`, `X=841`, one
   solution exists but `2X^2/(def)<1`. For an explicit infinite balanced primitive family, take `m=4k+1`,
   `n=2k` and square the Pythagorean side lengths `m^2-n^2,2mn,m^2+n^2`.
   Their coprimality and opposite parity give primitive summand triples;
   all three summands have order `k^4`, so `def/X^2` tends to infinity. Their singleton lattice contribution is
   precisely in the high-ris sector, which is treated by a different method.
3. **Pairwise primitivity cannot be replaced by separate local frequencies.**
   If a prime divides two divisor slots, the primitive triple count is zero.
   Tests compare these forced exclusions with unrestricted CRT counts.
4. **The endpoint `t=2/3` is not proved.** The high-tail integral has exponent
   `y^-1`, and `eta=0` also destroys convergence of `C_eta`. This is a boundary
   of this sufficient estimate, not a counterexample to the endpoint theorem.
5. **No unbalanced exclusion is used.** `(1,2^k-1,2^k)` is included; individual
   weights are unbounded, while the theorem concerns their averaged sum.
6. **The density count alone cannot establish this theorem.** Its `+1` cannot
   be summed over all divisor moduli. Powerful support plus the low/high split
   supplies the missing lawful quantifier boundary.

## 8. Primary-source comparison (retrieved 2026-10-20)

Bernert--Browning--Lichtman--Teraväinen,
[arXiv:2410.12234v2](https://arxiv.org/html/2410.12234v2), revised 9 May 2026,
study coprime `a+b=c<=X`, `rad(abc)<c^lambda`. Theorem 1.2 gives exponent
`(23lambda+3)/40+epsilon` for `0<lambda<=2`; Theorem 1.3 gives
`3/5+epsilon` for `0<lambda<1`.

Their Proposition 3.1 combines second/fourth Fourier moments for dyadic
monomial boxes; divisibility of exponent indices selects the saving.
Proposition 4.1 fixes complementary variables and counts primitive points
on a linear plane. Our slope lemma independently proves a two-dimensional
special case of that classical geometry mechanism with an explicit constant.

Lemma 2.2 compresses high exponent layers into a selected lower layer and
puts only exponent remainders into `n0`; simply leaving every high-power
factor in `n0` does not recover its small-remainder conclusion.

Their exceptional-count theorems are not invoked in Sections 2--6. Those
results alone do not directly establish this differently weighted moment.
On a balanced triple stratum, Markov with `t` approaching `2/3` recovers
only the classical trivial exceptional exponent `2lambda/3`; it does not
dominate their estimates. No improved exceptional-set exponent is claimed.
Academic originality of the present moment theorem is **UNVERIFIED**.

## 9. Verification ledger and next lamp

| Claim | Domain | Status / support | Remaining debt |
|---|---|---|---|
| CLOUD-ABC-01 | all real X>=2, real 0<=t<2/3 | PROVED LOCAL, Sections 2--6 | no Lean proof; academic priority unverified |
| CLOUD-ABC-02 | all pairwise-coprime d,e,f; primitive triangle | PROVED LOCAL, exact slope proof | formalization |
| CLOUD-ABC-03 | divisor/CRT/Mobius identities | CLASSICAL, independently implemented exact checks | no infinite inference from tests |
| CLOUD-ABC-04 | uniform radical tail | PROVED LOCAL, Rankin product proof | constants not optimized |
| CLOUD-ABC-05 | full moment mean value, real 0<=t<2/3 | PROVED LOCAL, Section 10, uniform-integrability transport | no optimized rate in X; no Lean proof |
| Density-only all-modulus upgrade | powerful pairwise-coprime support | REFUTED, (441,400,841) | retain singleton/high-ris branch |
| Full S_t bound at t>=2/3 | all primitive triples | OPEN by this work | stronger integrated high-ris tail |

The next verdict-changing theorem is a tail estimate improving the `2/3`
radical exponent on the actual primitive additive family, with enough
uniformity and a constant budget to integrate above the endpoint. Alternatively
an improved count for the high-determinant singleton strata could avoid that
Rankin bottleneck. This is a **pathway gap**, not absence of a falsifiable test.

Validation commands and actual receipts are recorded in
`CLOUD_ABC_CORRELATIONS_RECEIPT.json`; no complete-repository or formal build
is claimed by the lane's finite tests. No existing module, shared index,
claim registry, archival original, or Claude branch is modified.

### Completed lane validation

- New exact suite: 15 tests passed.
- Existing adjacent suites: `test_abc_triple_moment.py` (25) and
  `test_abc_clock_families.py` (16) passed.
- `git diff --check`: passed.
- Root and referee checked the same complete argument independently; these
  are proof audits, not independent mathematical derivations.
- The referee separately implemented direct lattice enumeration without
  importing this lane's code: 19,812 primitive cases with `X<=40` and
  `d,e,f<=12`, no failure, plus the nonprimitive mutation in Section 7.
  Its raw receipt belongs to the separately owned referee branch.

The explicit constants are deliberately huge (e.g. the implemented bound at
`t=1/2` is `2*2^41 + 12*2^856`). They establish uniform existence, not a useful
numerical approximation to the actual mean. No optimization is claimed.

## 10. Completed finite-to-global ascent: an actual mean-value limit

**Theorem CLOUD-ABC-05.** For every real `0<=t<2/3`,

\[
\boxed{\lim_{X\to\infty}\frac{S_t(X)}{X^2}
 =\frac1{2\zeta(2)}\prod_p\left(1+\frac{3p}{p+1}A_p(t)\right).}
\]

This is a stronger conclusion than an upper bound: the local prime-clock
factors transport to the actual global primitive moment. The missing
hypothesis in a formal Euler-product argument is supplied by the quantitative
uniform integrability furnished by Theorem CLOUD-ABC-01. Here is a complete
standalone proof; this branch has no dependency on cloud lane A.

**Fixed-divisor density.** For pairwise-coprime `d,e,f`, put `D=def`. Then

\[
 \lim_{X\to\infty}\frac{N_X(d,e,f)}{X^2}
 =\frac1{2\zeta(2)D}\prod_{p\mid D}\frac p{p+1}.
\]

To prove this, fix a finite prime cutoff `P` containing all prime divisors of
`D`. Impose divisibility `d|a,e|b,f|a+b` and exclude common divisors `p<=P`.
At an occupied prime power `p^k||D`, the residue density is
`p^(-k)(1-1/p)`: the unoccupied summand must be a unit. This holds for all
three possible slots by the invertible change of variables `(a,b)<->(a,a+b)`.
At an unoccupied prime the density is `1-p^-2`. CRT multiplies these finite
factors. For each **fixed** modulus, tile the positive triangle by residue
cells: each fixed residue class has count `X^2/(2W^2)+O_W(X+1)`, since the
number of cells crossing its three boundary segments is `O_W(X+1)`.
Thus the normalized finite-prime count tends to half its residue density.

A triple counted at cutoff `P` but not globally primitive has some common
prime divisor `p>P`. For any such `p`, its count is at most `X^2/(2p^2)`
by scaling the full triangle. Hence the normalized discrepancy is at most

\[
 \frac12\sum_{p>P}\frac1{p^2}\le\frac1{2\lfloor P\rfloor}.
\]

First let `X` tend to infinity for fixed `P`, and then let `P` tend to
infinity. The finite residue densities converge absolutely. Their product
simplifies to the asserted density because
`(1-1/p)/(1-1/p^2)=p/(p+1)` and
`prod_p(1-p^-2)=1/zeta(2)`. The last Euler identity follows by absolutely
convergent unique-factorization expansion. This proves the fixed-divisor
limit without any simultaneous growing-modulus claim.

**Uniform integrability.** Fix `s` with `t<s<2/3`; let `K_s` denote the explicit
constant in CLOUD-ABC-01. For an integer `L>=1`, set

\[
 F_{t,L}(n)=\sum_{\substack{d\mid n\\d\le L}}g_t(d),\qquad
 S_{t,L}(X)=\sum_{a+b=c\le X,(a,b)=1}F_{t,L}(a)F_{t,L}(b)F_{t,L}(c).
\]

If `H=ris(abc)<=sqrt(L)`, every nonzero divisor term in each factor has
`d<=ris(d)^2<=H^2<=L`, so the truncated weight is the full weight. Otherwise
the difference is at most `H^t`. Thus for **every** real `X>=2`,

\[
 0\le\frac{S_t(X)-S_{t,L}(X)}{X^2}
 \le L^{-(s-t)/2}\frac{S_s(X)}{X^2}
 \le K_s L^{-(s-t)/2}.
\]

For each fixed `L`, the finite divisor expansion and fixed-divisor density
show that `S_(t,L)(X)/X^2` tends to

\[
 C_{t,L}=\frac1{2\zeta(2)}
 \sum_{\substack{d,e,f\le L\\(d,e)=(e,f)=(f,d)=1}}
 \frac{g_t(d)g_t(e)g_t(f)}{def}\prod_{p\mid def}\frac p{p+1}.
\]

The nonnegative sum converges as `L` increases; it is bounded by `E_3(t)`.
Its Euler factors give the constant `C_t` displayed in the theorem. Moreover,
for `L'>L`, the uniform bound above implies
`C_(t,L')-C_(t,L)<=K_s L^(-(s-t)/2)` after taking the fixed-`L,L'` limits.
Then let `L'` tend to infinity. Therefore the fully quantified transfer budget is

\[
\boxed{\left|\frac{S_t(X)}{X^2}-C_t\right|
 \le \left|\frac{S_{t,L}(X)}{X^2}-C_{t,L}\right|
       +2K_sL^{-(s-t)/2}.}
\]

First choose `L` to control the explicit tail budget, then `X` to control the
finite-divisor term. This proves the full limit. QED.

**Scope and boundary.** The Euler product converges for `t<1`, but the proved
uniform integrability here reaches only `t<2/3`; its formal convergence alone
does not extend the mean-value theorem. This supplies a literal instance of
local arithmetic densities + an explicit tail budget -> an integer-family
limit. No effective optimized rate in `X` is asserted; the finite-divisor term
can be estimated by the CRT lane's quantitative theorem when that branch is
integrated. Status: **PROVED LOCAL**, classical methods/new-to-project synthesis;
no formal verification or priority claim. At `t=0`, this recovers
`sum_(c<=X) phi(c) ~ X^2/(2zeta(2))` as a calibration.


Section 10 received a separate referee pass after the initial bound audit:
local factors, missing-prime uniform tail, both ordered limits, and the
uniform-integrability exponent were checked; no gap was found. This is a
same-model mathematical audit, not a formal-kernel proof or an originality
certification.
