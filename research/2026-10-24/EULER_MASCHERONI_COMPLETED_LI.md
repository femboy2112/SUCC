# Euler–Mascheroni defects and the completed Li coefficients

**Research date:** October 24, 2026.

**Authority:** classical analytic identities; elementary paper proofs; exact rational finite certificates; separately labelled numerical calibration.

**RH PROVED: no.** The all-degree positivity statement remains unproved.

This note turns the Euler–Mascheroni regularization into a finite, auditable input route for the completed Li coefficients. It also constructs a countermodel showing exactly why any finite collection of these constants, even with the usual analytic completion and reflection symmetry, cannot authenticate the entire arithmetic source.

The result is a reusable finite instrument and a source-selection boundary. It does not claim a new RH criterion, an efficient high-index Stieltjes algorithm, or a proof of RH or of the normality of $\pi$.

**Review entry points:** [implementation](../../observational_succ/euler_gamma_li_bridge.py), [independent tests](../../tests/test_euler_gamma_li_bridge.py), [combined probe](../../scripts/euler_mascheroni_probe.py), [probe receipt](euler_mascheroni_validation/probe_receipt.json), and [round hole contract](EULER_MASCHERONI_HOLE_CONTRACT.md).

## 1. The full regularized object

For real $r>1$, both defining series converge absolutely and

$$
\sum_{k\ge1}\left(k^{-r}-r^{-k}\right)
=\zeta(r)-\frac1{r-1}.
$$

The useful analytic object is therefore

$$
G(s)=\zeta(s)-\frac1{s-1},\qquad G(1)=\gamma.
$$

The singularity at $s=1$ is removable, and $G$ is entire. In the standard Stieltjes convention,

$$
G(1+z)=\sum_{j\ge0}\frac{(-1)^j\gamma_j}{j!}z^j,
\qquad \gamma_0=\gamma.
$$

These analytic facts and the convention are classical; see [DLMF §25.2](https://dlmf.nist.gov/25.2). The entire infinite Taylor jet determines $G$. A single value or any finite jet does not determine it.

The dependency chain considered here is

$$
\text{finite integer sums with tail bounds}
\ \longrightarrow\
\text{finite Stieltjes intervals}
\ \longrightarrow\
\text{finite completed Li intervals}.
$$

Every arrow in this finite chain is implemented below. Extending its conclusion to $\lambda_n\ge0$ for **every** $n\ge1$ would require an additional theorem about the authentic arithmetic source. The classical Li criterion identifies that universal statement with RH; it does not prove it.

## 2. A finite successor certificate for Stieltjes constants

### Proposition 1: a monotone tail bound

For an integer $m\ge0$, define

$$
f_m(x)=\frac{(\log x)^m}{x},
\qquad
A_{N,m}=\sum_{k=1}^{N}f_m(k)
-\frac{(\log N)^{m+1}}{m+1}.
$$

Here $f_0(1)=1$, as given by $f_0(x)=1/x$. If $N\ge3^m$, then

$$
A_{N,m}-f_m(N)\le\gamma_m\le A_{N,m}.
$$

**Proof.** For $m\ge1$ and $x>1$,

$$
f_m'(x)=\frac{(\log x)^{m-1}}{x^2}(m-\log x).
$$

Since $e<3$, the function is nonnegative and decreasing on $[N,\infty)$ when $N\ge3^m$. The case $m=0$ follows directly from $f_0'(x)=-x^{-2}$.

For integers $M>N$, the fundamental theorem of calculus gives

$$
A_{M,m}-A_{N,m}
=\sum_{k=N+1}^{M}
\left(f_m(k)-\int_{k-1}^{k}f_m(x)\,dx\right).
$$

Each summand lies between $f_m(k)-f_m(k-1)$ and $0$. Consequently,

$$
f_m(M)-f_m(N)
\le A_{M,m}-A_{N,m}\le0.
$$

The sequence is decreasing and bounded below. Its classical defining limit is $\gamma_m$, and $f_m(M)\to0$, giving the assertion. This also proves convergence of the displayed sum–integral defects without an infinite computation. $\square$

The cutoff condition is sufficient and deliberately simple. The method becomes expensive with growing $m$; no competitive high-order algorithm is claimed.

### Rational logarithms and outward rounding

The implementation uses the existing exact logarithm oracle in [source_prime_certificates.py](../../observational_succ/source_prime_certificates.py). Binary argument reduction writes an integer logarithm as an integer multiple of $\log2$ plus the logarithm of a rational number in $[1,2]$. For that reduced argument,

$$
\log\frac{1+y}{1-y}
=2\sum_{j=0}^{T-1}\frac{y^{2j+1}}{2j+1}+R_T,
$$

with

$$
0\le y\le\frac13,
\qquad
0\le R_T\le
\frac{2y^{2T+1}}{(2T+1)(1-y^2)}.
$$

All quantities in the finite sum and remainder bound are rational. The remainder estimate follows by replacing every remaining denominator by $2T+1$ and summing the resulting geometric series.

The new implementation rounds interval lower endpoints down and upper endpoints up on a rational grid. This limits denominator growth while preserving every enclosure. The full tail from Proposition 1 is then included. A numerical approximation to $\gamma_m$ is never promoted to a certified input interval.

### Integer zeta values and the Archimedean channel

For each integer $k\ge2$, the positive Dirichlet series and integral test give

$$
\sum_{j=1}^{N}j^{-k}
+\frac{(N+1)^{1-k}}{k-1}
\le\zeta(k)\le
\sum_{j=1}^{N}j^{-k}
+\frac{N^{1-k}}{k-1}.
$$

These are also evaluated rationally with outward rounding. The $\pi$ and $\log\pi$ intervals come from the existing [suzuki_arch_intervals.py](../../observational_succ/suzuki_arch_intervals.py): alternating arctangent bounds in Machin's identity enclose $\pi$, and monotone logarithm evaluation encloses the logarithms of its endpoints. The certificate retains this Archimedean channel explicitly.

## 3. Exact completed Stieltjes-to-Li transport

### Proposition 2: the formal logarithm recurrence

Put

$$
a_0=1,
\qquad
a_n=\frac{(-1)^{n-1}\gamma_{n-1}}{(n-1)!}
\quad(n\ge1),
$$

so that

$$
A(z)=z\zeta(1+z)=\sum_{n\ge0}a_nz^n.
$$

Let the analytic logarithm near $0$, normalized to vanish there, be

$$
B(z)=\log A(z)=\sum_{n\ge1}b_nz^n.
$$

Then

$$
b_n=a_n-\frac1n\sum_{j=1}^{n-1}j b_j a_{n-j}.
$$

**Proof.** The identity $A'=AB'$ gives

$$
n a_n=\sum_{j=1}^{n}j b_j a_{n-j}.
$$

Since $a_0=1$, isolating the last summand gives the recurrence. The same calculation is valid as an identity of formal power series, so each finite output jet depends on finitely many input coefficients. $\square$

This is classical power-series algebra. Stieltjes-to-logarithmic-derivative recurrences and their relation to Li coefficients have substantial prior literature, including [Maślanka (2004)](https://arxiv.org/abs/math/0406312). That paper absorbs the sign and factorial into its Stieltjes coefficient convention; the present implementation uses the standard $\gamma_j$ above.

### Proposition 3: retain the complete Gamma and pole factors

Use the standard completed function

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \xi(1)=\frac12.
$$

At $s=1+z$,

$$
\xi(1+z)
=\frac12(1+z)\pi^{-(1+z)/2}
\Gamma\left(\frac{1+z}{2}\right)A(z).
$$

Write

$$
\log\frac{\xi(1+z)}{\xi(1)}=\sum_{k\ge1}c_kz^k.
$$

The coefficients are

$$
c_1=1+\frac\gamma2-\frac12\log(4\pi),
$$

and, for $k\ge2$,

$$
c_k=\frac{(-1)^{k+1}}k
+\frac{(-1)^k}{k}(1-2^{-k})\zeta(k)+b_k.
$$

**Proof.** The logarithm of the completed product separates into the logarithms of its factors. The term $\log(1+z)$ supplies $(-1)^{k+1}/k$. The first Gamma derivative is

$$
\frac12\psi(1/2)=-\frac\gamma2-\log2.
$$

Together with $b_1=\gamma$ and the $-z\log\pi/2$ contribution, this yields $c_1$.

For $k\ge2$, the classical half-integer polygamma identity gives

$$
\frac{\psi^{(k-1)}(1/2)}{2^k k!}
=\frac{(-1)^k}{k}(1-2^{-k})\zeta(k).
$$

See [DLMF §5.15, equation 5.15.3](https://dlmf.nist.gov/5.15). Adding the formal source logarithm $b_k$ proves the result. $\square$

### Proposition 4: the Li coefficient map

With the standard normalization

$$
\lambda_n=
\left.\frac1{(n-1)!}\frac{d^n}{ds^n}
\bigl(s^{n-1}\log\xi(s)\bigr)\right|_{s=1},
$$

one has

$$
\boxed{\lambda_n
=n\sum_{k=1}^{n}\binom{n-1}{k-1}c_k.}
$$

**Proof.** The coefficient of $z^n$ in $(1+z)^{n-1}\log\xi(1+z)$ is
$\sum_{k=1}^{n}\binom{n-1}{n-k}c_k$. The constant logarithm does not contribute, since $(1+z)^{n-1}$ has degree $n-1$. Differentiation and division by $(n-1)!$ multiply this coefficient by $n$. $\square$

Equivalently, substituting $z=w/(1-w)$ gives

$$
\log\left(2\xi\left(\frac1{1-w}\right)\right)
=\sum_{n\ge1}\frac{\lambda_n}{n}w^n.
$$

Li's classical theorem says that RH holds if and only if $\lambda_n\ge0$ for every integer $n\ge1$; see [Li (1997)](https://www.sciencedirect.com/science/article/pii/S0022314X97921375). This note constructs and verifies finite instances. It supplies no new argument for the universal positivity conclusion.

## 4. Source gamma and Archimedean gamma are separate under mutation

For authentic zeta, the regular-part constant and the Euler constant in the Gamma derivative are equal. A changed arithmetic source need not satisfy that equality. With the actual Gamma completion fixed, the first completed coefficient is

$$
c_1=1+\gamma_0^{\mathrm{source}}
-\frac12\gamma^{\mathrm{arch}}
-\frac12\log(4\pi).
$$

The implementation therefore permits the Archimedean constant to be passed separately as `arch_euler_gamma`. Its default uses the authentic equality and is appropriate for the source-derived certificates in this note. A counterfeit must explicitly retain the original Archimedean value if that is the intended experiment.

With completion fixed, changing only the $m$th source Stieltjes coefficient, while keeping all earlier ones fixed, first changes $\lambda_{m+1}$ by

$$
\Delta\lambda_{m+1}
=\frac{(-1)^m(m+1)}{m!}\Delta\gamma_m.
$$

To verify this, note that $a_1,\ldots,a_m$ are unchanged and $\Delta a_{m+1}=(-1)^m\Delta\gamma_m/m!$. Proposition 2 gives the same change in $b_{m+1}$, with all earlier $b_j$ unchanged. Proposition 4 then multiplies this first new logarithmic coefficient by $m+1$.

For $m=0$, the sensitivity is **1** when the Gamma factor remains fixed. If the same formal parameter is changed in both $\gamma_0^{\mathrm{source}}$ and $\gamma^{\mathrm{arch}}$, the sensitivity is instead **$1/2$**. That is a distinct perturbation. Both are retained in the tests; a source mutation is not allowed to alter the completion silently.

## 5. Three exact finite certificates

`certified_li_prefix(degree=3, cutoff=512)` uses 512 integer successor steps, 16 logarithm-series terms, a 24-place outward rational grid, and the analytic tails above. Applying the completed recurrence gives the following exact rational outward enclosures. The decimal forms are terminating representations of rational endpoints, not floating-point error claims.

| Coefficient | Exact rational lower bound | Exact rational upper bound | Decimal enclosure |
|---|---:|---:|---|
| $\lambda_1$ | $1130363/50000000$ | $147399/6250000$ | $[0.02260726,\ 0.02358384]$ |
| $\lambda_2$ | $7805857/100000000$ | $333243/3125000$ | $[0.07805857,\ 0.10663776]$ |
| $\lambda_3$ | $4888667/50000000$ | $15875187/50000000$ | $[0.09777334,\ 0.31750374]$ |

Every lower endpoint is strictly positive. Thus the first three true Li coefficients are positive by this elementary finite certificate. Their positivity is a classical fact recovered here through a new repository input path; it is not a new mathematical discovery or evidence that finite verification closes the infinite quantifier.

The combined [probe receipt](euler_mascheroni_validation/probe_receipt.json) records the source inputs and resulting intervals. The production code performs no numerical special-function evaluation to obtain them.

## 6. A counterfeit preserving arbitrarily long finite gamma and Li jets

### Proposition 5: finite jets do not authenticate the source

Fix $q=3/4$ and any integer $m\ge2$. Define

$$
P_m(s)=\left(\frac{s(s-1)}{q(q-1)}\right)^m,
\qquad
\widetilde\xi_m(s)=\xi(s)-\xi(q)P_m(s).
$$

This construction uses a rational anchor and an ordinary value of the genuine function. It uses no nontrivial zero coordinate. Then:

- $\widetilde\xi_m$ is entire of order at most one, real on the real axis, and satisfies $\widetilde\xi_m(1-s)=\widetilde\xi_m(s)$.
- Its Taylor jet at $s=1$ agrees with that of $\xi$ through order $m-1$.
- Its first $m-1$ coefficients under the Li derivative definition agree with the genuine ones.
- The corresponding completed quotient has the same pole at $1$, residue $1$, and Stieltjes constants $\gamma_0,\ldots,\gamma_{m-2}$.
- It has zeros at $q$ and $1-q$, both off the critical line.

**Proof.** The polynomial satisfies $P_m(1-s)=P_m(s)$ and has zeros of order $m$ at $0$ and $1$. Subtracting a polynomial preserves entire order at most one. These facts establish the symmetry and jet assertions.

Since $\xi(1)=1/2\ne0$, both functions have analytic logarithms near $1$, with the same normalization, and

$$
\log\widetilde\xi_m(s)-\log\xi(s)=O((s-1)^m).
$$

The first $m-1$ Li coefficients therefore agree by Proposition 4. Also $P_m(q)=P_m(1-q)=1$, while $\xi(1-q)=\xi(q)$, establishing both prescribed zeros.

The subtraction is nonzero. For $0<s<1$, the alternating eta series is positive and $1-2^{1-s}<0$, so $\zeta(s)<0$. Since $s(s-1)<0$ and the other completed factors are positive, $\xi(q)>0$.

Put $c=-\xi(q)/(q(q-1))^m$. Dividing by the same actual completion gives

$$
\widetilde\zeta_m(s)=\zeta(s)+D_m(s),
$$

where

$$
D_m(s)=
\frac{2c\pi^{s/2}[s(s-1)]^{m-1}}{\Gamma(s/2)}.
$$

The reciprocal Gamma function is entire, so $D_m$ is entire. Thus the pole and residue at $1$ are unchanged. The factor $(s-1)^{m-1}$ makes the regular coefficients through degree $m-2$ unchanged. $\square$

The counterfeit retains further familiar features. At every negative even integer the reciprocal Gamma factor vanishes, so the genuine trivial zeros remain zeros. Stirling's formula on the positive real axis gives

$$
\log|D_m(\sigma)|
=-\frac\sigma2\log\sigma+O_m(\sigma)
\qquad(\sigma\to\infty).
$$

Consequently, for every fixed $A>1$,

$$
A^\sigma D_m(\sigma)\longrightarrow0,
\qquad
\widetilde\zeta_m(\sigma)\longrightarrow1.
$$

The standard real normalization, reflection, completion, finite jets, and entire-order bound still do not eliminate this counterfeit.

### Proposition 6: the counterfeit provably fails ordinary Dirichlet-source authenticity

The nonzero function $D_m$ cannot be represented by an ordinary Dirichlet series that converges absolutely in any right half-plane. Hence $\widetilde\zeta_m$ cannot possess such a representation either.

**Proof.** Suppose

$$
D_m(s)=\sum_{n\ge1}d_n n^{-s}
$$

converges absolutely for $\Re s>\sigma_a$. Choose $\sigma_0>\sigma_a$ and let $n_0$ be the least index with $d_{n_0}\ne0$. For real $\sigma\ge\sigma_0$,

$$
n_0^\sigma D_m(\sigma)
=d_{n_0}+\sum_{n>n_0}d_n(n_0/n)^\sigma.
$$

For each $n>n_0$ the summand tends to zero, and

$$
|d_n|(n_0/n)^\sigma
\le n_0^{\sigma_0}|d_n|n^{-\sigma_0}.
$$

The right-hand series is summable. Dominated convergence therefore gives

$$
n_0^\sigma D_m(\sigma)\longrightarrow d_{n_0}\ne0.
$$

This contradicts the superexponential decay just proved; when $n_0=1$, use the already established limit $D_m(\sigma)\to0$. Finally, if $\widetilde\zeta_m$ had an absolutely convergent ordinary Dirichlet representation in a right half-plane, subtracting the authentic series for $\zeta$ in their common half-plane would give one for $D_m$. $\square$

**Scope of the countermodel.** It is a precise failure of finite analytic observations to identify the source. It is **not** a second lawful realization of the original integer/Euler source and is **not** a counterexample to RH. The full arithmetic law excludes it for the explicit reason above. No priority claim is made for analytic finite-jet interpolation as a method.

## 7. A uniform finite-cutoff error theorem

The finite prefix certificates above can be supplemented by a bound valid for **every** pair of integers $N,n\ge1$. It controls approximation error as both the arithmetic cutoff and Li degree vary. It does not control the sign of the genuine coefficient.

Define the entire finite sum–integral defect

$$
G_N(s)=\sum_{k=1}^{N}k^{-s}-\int_1^N x^{-s}\,dx,
$$

where the integral defines its value at $s=1$ without a singular formula. Put

$$
A(z)=1+zG(1+z),
\qquad
A_N(z)=1+zG_N(1+z).
$$

Near $z=0$, retain the **actual, unchanged** Gamma, pole, and $\pi$ factors and define the finite model by

$$
\xi_N(1+z)=\frac12(1+z)\pi^{-(1+z)/2}
\Gamma\left(\frac{1+z}{2}\right)A_N(z).
$$

Its normalization is $\xi_N(1)=1/2$. Define $\lambda_n^{(N)}$ by the same derivative expression as the Li coefficients, using the local analytic logarithm of $\xi_N$. These are **finite-model coefficients**; they become approximations to the genuine $\lambda_n$, not replacements for the authentic infinite source.

In particular, $G_N(1)=H_N-\log N$ replaces the arithmetic finite part only. It must not replace the actual Euler constant appearing in the derivative of the fixed Gamma factor. This is the fixed-completion case of section 4.

### Proposition 7: all-degree cutoff bound

For all integers $N,n\ge1$,

$$
\boxed{
\left|\lambda_n^{(N)}-\lambda_n\right|
\le\frac{20}{7}\,n\,5^{n-1}N^{-3/4}.
}
$$

**Proof.** Write $s=\sigma+it$ with $\sigma>0$. Unit-cell integration gives

$$
G(s)=s\int_1^\infty(1-\{x\})x^{-s-1}\,dx,
$$

and

$$
G_N(s)=s\int_1^N(1-\{x\})x^{-s-1}\,dx+N^{-s}.
$$

For example, on the cell $(k,k+1)$, integration of
$s(k+1-x)x^{-s-1}$ gives $k^{-s}-\int_k^{k+1}x^{-s}\,dx$; summing the cells proves the finite identity. The infinite integral is absolutely convergent for $\sigma>0$ and agrees with $G$ by the corresponding convergent cell sum. Values assigned to the fractional part at integer endpoints do not affect either integral.

Since $0\le1-\{x\}\le1$ almost everywhere and $|s|/\sigma\ge1$,

$$
|G(s)|\le\frac{|s|}{\sigma},
$$

and

$$
|G_N(s)|
\le\frac{|s|}{\sigma}(1-N^{-\sigma})+N^{-\sigma}
\le\frac{|s|}{\sigma}.
$$

Subtracting the two integral identities, using
$N^{-s}=s\int_N^\infty x^{-s-1}\,dx$, also gives

$$
G_N(s)-G(s)
=s\int_N^\infty\{x\}x^{-s-1}\,dx.
$$

Consequently,

$$
|G_N(s)-G(s)|
\le\frac{|s|}{\sigma}N^{-\sigma}.
$$

On the closed disk $|z|\le1/4$, with $s=1+z$, one has
$\sigma\ge3/4$ and $|s|\le5/4$. Therefore

$$
|G(1+z)|,\ |G_N(1+z)|\le\frac53,
\qquad
|G_N(1+z)-G(1+z)|\le\frac53N^{-3/4}.
$$

It follows that both $A(z)$ and $A_N(z)$ lie in the same convex disk

$$
|w-1|\le\frac5{12},
$$

which is contained in the right half-plane and stays at distance at least $7/12$ from zero. Thus the principal analytic logarithms are available throughout the $z$ disk, agree with the normalizations $\log A(0)=\log A_N(0)=0$, and have no branch ambiguity. Integrating the derivative of the logarithm along the line segment between $A(z)$ and $A_N(z)$ gives

$$
\log A_N(z)-\log A(z)
=\int_0^1
\frac{A_N(z)-A(z)}{A(z)+u(A_N(z)-A(z))}\,du.
$$

The segment remains in the same convex disk. Hence

$$
|\log A_N(z)-\log A(z)|
\le\frac{12}{7}|A_N(z)-A(z)|
\le\frac57N^{-3/4}.
$$

If $b_k^{(N)}$ and $b_k$ are the respective logarithmic coefficients, Cauchy's coefficient estimate on radius $1/4$ yields

$$
|b_k^{(N)}-b_k|
\le\frac57\,4^kN^{-3/4}
\qquad(k\ge1).
$$

Because all completion factors are fixed, the differences of the completed logarithmic coefficients are exactly these differences, including at $k=1$. Applying Proposition 4 and the binomial theorem,

$$
\begin{aligned}
|\lambda_n^{(N)}-\lambda_n|
&\le\frac57nN^{-3/4}
\sum_{k=1}^{n}\binom{n-1}{k-1}4^k\\
&=\frac{20}{7}n5^{n-1}N^{-3/4}.
\end{aligned}
$$

This proves the assertion for every $N,n\ge1$. $\square$

### Sufficient finite-observer cost and its boundary

For a requested error $\eta>0$, the sufficient cutoff

$$
N\ge
\left\lceil
\left(\frac{20n5^{n-1}}{7\eta}\right)^{4/3}
\right\rceil
$$

ensures $|\lambda_n^{(N)}-\lambda_n|\le\eta$. This is a **sufficient bound**, not a necessary cutoff, an optimal complexity estimate, or evidence that no more efficient approximation exists. The proof is classical complex analysis applied to the actual successor defect; academic novelty of this explicit bound is not asserted.

The quantifiers in the paper theorem cover all positive integers $N$ and $n$. The current implementation has explicit finite resource caps and uses the separate monotone-tail Stieltjes construction for its three-coefficient certificate. It has not computationally executed the theorem for all degrees, nor is its chosen finite cap a mathematical obstruction.

The factor $5^{n-1}$ exposes the cost of increasing the degree in this estimate. A finite-model sign can certify a particular genuine coefficient only when the computed lower bound exceeds the stated approximation error, with any numerical or interval evaluation error also included. No lower bound of that kind is established here uniformly over all $n$. The theorem closes a quantitative approximation edge; **universal Li positivity remains unproved**.

### Corollary 7.1: correcting the half-endpoint improves the cutoff bound

**Paper-only analytic result.** The centered-sawtooth representation and endpoint discrepancy are also recorded in the concurrent [generalized Euler–adelic PR #285](https://github.com/femboy2112/SUCC/pull/285), inspected at [`f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad`](https://github.com/femboy2112/SUCC/blob/f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad/research/2026-10-24/GENERALIZED_EULER_ADELIC_BOUNDARY.md). The following calculation applies that centered starting point to the completed Li cutoff. Its analytic mechanism is the classical first Euler–Maclaurin endpoint correction; no new continuation theory is claimed.

Define

$$
G_N^*(s)=G_N(s)-\frac12N^{-s},
\qquad
A_N^*(z)=1+zG_N^*(1+z).
$$

Use $A_N^*$ in place of $A_N$ in the finite model above, leaving every actual completion factor fixed, and denote its Li-type coefficients by $\lambda_n^{(N,*)}$. Then for all integers $N,n\ge1$,

$$
\boxed{
|\lambda_n^{(N,*)}-\lambda_n|
\le\frac{135}{392}\,n\,5^{n-1}N^{-7/4}.
}
$$

**Proof.** Let

$$
P_2(x)=\frac{\{x\}^2-\{x\}}2.
$$

This periodic function is continuous and locally absolutely continuous. It satisfies $P_2'(x)=\{x\}-1/2$ almost everywhere, $P_2(N)=0$ at integer cutoffs, and $|P_2(x)|\le1/8$.

The exact remainder identity from Proposition 7 becomes, for $\sigma=\Re s>0$,

$$
G_N^*(s)-G(s)
=s\int_N^\infty\left(\{x\}-\frac12\right)x^{-s-1}\,dx.
$$

Integration by parts, including the vanishing boundary terms at the integer $N$ and at infinity, gives

$$
G_N^*(s)-G(s)
=s(s+1)\int_N^\infty P_2(x)x^{-s-2}\,dx.
$$

Hence

$$
|G_N^*(s)-G(s)|
\le\frac{|s(s+1)|}{8(\sigma+1)}N^{-\sigma-1}.
$$

On $|s-1|\le1/4$, the bounds $|s|\le5/4$, $|s+1|\le9/4$, and $\sigma+1\ge7/4$ imply

$$
|G_N^*(s)-G(s)|\le\frac{45}{224}N^{-7/4}.
$$

The corrected finite model retains the same disk control, since

$$
G_N^*(s)
=s\int_1^N(1-\{x\})x^{-s-1}\,dx+\frac12N^{-s}
$$

and therefore

$$
|G_N^*(s)|
\le\frac{|s|}{\sigma}(1-N^{-\sigma})+\frac12N^{-\sigma}
\le\frac{|s|}{\sigma}\le\frac53.
$$

Both $A_N^*$ and $A$ thus lie in $|w-1|\le5/12$. The same convex-segment logarithm argument gives

$$
|\log A_N^*(z)-\log A(z)|
\le\frac{12}{7}\cdot\frac14\cdot\frac{45}{224}N^{-7/4}
=\frac{135}{1568}N^{-7/4}.
$$

Cauchy's estimate multiplies this by $4^k$ for the $k$th coefficient. The completed Li sum then multiplies the common bound by $4n5^{n-1}$, yielding the stated factor $135/392$. All logarithms use the same normalized analytic branches as in Proposition 7. $\square$

For $\eta>0$, the sufficient integer cutoff becomes

$$
N\ge
\left\lceil
\left(\frac{135n5^{n-1}}{392\eta}\right)^{4/7}
\right\rceil.
$$

This is an improved sufficient approximation bound, not a necessary or optimal cost, and it does not establish any uniform sign. The current finite certificate implementation and its reported test counts are unchanged; this corollary is supported by the explicit analytic proof above.

The integration-by-parts remainder also makes the endpoint correction concrete. Its integral is locally uniformly convergent on $\Re s>-1$, so the identity extends there by analytic continuation and proves $G_N^*\to G$ locally uniformly on that larger half-plane. At $s=0$, every corrected cutoff equals $1/2$, matching $G(0)$ exactly. The boundary $\Re s=-1$ is excluded: at $s=-1$, every corrected cutoff equals $1/2$, while $G(-1)=5/12$. No further endpoint interchange is asserted.

## 8. Crosswalk to existing SUCC routes

The repository already contains [balanced_theta_li.py](../../observational_succ/balanced_theta_li.py), which constructs finite Li jets from actual theta-source integrals and derives a fixed-degree error bound with explicit growing-degree amplification. This note adds the regularized Euler/Stieltjes input route. It does not supersede the theta error theorem, improve its all-degree behavior, or change its open positivity obligation.

The reciprocal-cell construction in [zero_centered_residue.py](../../observational_succ/zero_centered_residue.py) and the full-cut distinction in [bidirectional_cut.py](../../observational_succ/bidirectional_cut.py) already give concrete SUCC interfaces to the classical Nyman–Beurling–Báez-Duarte approximation problem. Their [source-first dossier](../2026-10-13/ZERO_CENTERED_SUCC_RESIDUE_OBSERVER.md) explicitly distinguishes finite interpolation and periodic-tail structure from global weighted $L^2$ closure.

The same Euler discrepancy has the classical fractional-part Mellin representation

$$
G(s)=1-s\int_1^\infty\{x\}x^{-s-1}\,dx
\qquad(\Re s>0),
$$

which explains the relevance of those existing residue observers. It does not supply the missing closure theorem. The source-dependent all-degree Li sign, the global Nyman approximation, and the completed signed Weil positivity each retain their stated analytic obligations. This note does not assert a new source-level operator identification among them.

## 9. Validation and calibration boundaries

The focused implementation run passed **13 tests**. They cover:

- An independently coded finite expansion of $\log(1+u)$ by powers, compared with the recurrence.
- Sixty-four interval-corner models and exact point-interval recovery.
- Fixed versus coupled Archimedean gamma perturbations, and rejection or detection of missing completion channels.
- Exact rational reflection, anchor, and vanishing-jet identities for the counterfeit family.
- The three source-derived rational positive intervals above.
- Separately labelled numerical comparisons with independently evaluated classical constants.

An additional implementation calibration compares the degree-eight transfer with a direct Taylor expansion of
$\log(2\xi(1/(1-w)))$. At 80 decimal digits, all eight discrepancies were below $3.2\times10^{-73}$. This is a numerical cross-check of signs, indexing, and completion factors. It is **not** the proof of the interval certificate and does not certify an all-degree formula by finite testing; the formula has the separate derivation above.

To reproduce the focused tests:

```sh
python -m unittest discover -s tests -p 'test_euler_gamma_li_bridge.py' -v
```

The combined round probe is [scripts/euler_mascheroni_probe.py](../../scripts/euler_mascheroni_probe.py), with its recorded output in [probe_receipt.json](euler_mascheroni_validation/probe_receipt.json). Repository-wide validation and hosted CI are separate from the focused result and must be read from the round's final validation record. No Lean-kernel authority is claimed for this note.

## 10. Remaining mathematical obligation

The finite source evaluator is justified by elementary tail inequalities. The completed transfer is an exact classical identity. Proposition 7 supplies a quantitative approximation bound for every finite cutoff and degree. The counterfeit supplies a checked boundary for finite-jet source selection.

The unresolved theorem remains a **uniform sign argument for the actual completed source over all Li degrees**. Componentwise bounds alone may become useless under the alternating and binomial combinations; each fixed-degree certificate does not control that growth. Any proposed sign mechanism must keep the authentic Dirichlet source and Gamma completion fixed, and must distinguish the explicit countermodel above for its actual source failure.

No scalar normalization, finite positive prefix, or full Taylor encoding is being promoted to that theorem. The paper results here are a finite certificate and a source-selection obstruction within the specified broader analytic family. RH and $\pi$ normality remain open.

## Primary references

1. NIST DLMF, [§25.2, Definition and Expansions](https://dlmf.nist.gov/25.2): meromorphic continuation, Laurent expansion, and the Stieltjes convention.
2. NIST DLMF, [§5.15, Polygamma Functions](https://dlmf.nist.gov/5.15), especially equation 5.15.3: the half-integer Gamma derivatives used in the completed formula.
3. Xian-Jin Li, [*The Positivity of a Sequence of Numbers and the Riemann Hypothesis*](https://www.sciencedirect.com/science/article/pii/S0022314X97921375), *Journal of Number Theory* **65** (1997), 325–333: the classical all-degree criterion.
4. Krzysztof Maślanka, [*An Explicit Formula Relating Stieltjes Constants and Li's Numbers*](https://arxiv.org/abs/math/0406312), 2004: classical recurrence and coefficient relations, with a different Stieltjes normalization.
5. Luis Báez-Duarte, [*A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*](https://arxiv.org/abs/math/0202141): the integer-dilation closure criterion underlying the existing SUCC crosswalk.
6. Luis Báez-Duarte, Michel Balazard, Bernard Landreau, and Éric Saias, [*Sur l'autocorrélation multiplicative de la fonction « partie fractionnaire »*](https://arxiv.org/abs/math/0306251), 2003: the fractional-part Mellin and dilation setting.
