# Authentic Pascal kernels, rational base filters, and the retained carry

**Date:** 2026-10-24. **Parent:** draft #270 at
`3acd547ff122368d5694efdab029b3156a292d8a`.
**Branch:** `research/pi-pascal-mahler-source-2026-10-24`.
**Status:** exact source identities, proved positive-kernel bounds, a scoped
integer-filter obstruction, and rational-filter constructions. Real
half-retention, same-law tripling transport, and pi normality remain **OPEN**.
No scholarly priority is claimed.

This translator lane answers the real-kernel part of the
[frozen contract](PI_PASCAL_HOLE_CONTRACT.md). It uses the authentic source
and does not import conclusions from a fitted or altered forcing. The
important surviving distinction is between constructing another exact
source for a base and proving that its empirical law agrees with an
existing selected source law.

The executable instrument is
[`pi_pascal_kernel.py`](../../observational_succ/pi_pascal_kernel.py), with
independent exact checks in
[`test_pi_pascal_kernel.py`](../../tests/test_pi_pascal_kernel.py).

## 1. Objects, domains, and inherited facts

For integers $n\geq1$, fix

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Let $y_n=\{U_n\}$, $\alpha=\pi/16$, and

$$
T_n=\sum_{j\geq1}16^{-j}r(n+j),\qquad
U_n=16^n\alpha-T_n.
$$

The source-authenticated positive representation, already proved in
[BBP source memory](BBP_SOURCE_MEMORY_REPAIR.md), is

$$
g(x)=4-2x^3-x^4-x^5
     =(1-x)(4+4x+4x^2+2x^3+x^4),
$$

$$
r(n+1)=\int_0^1x^{8n}g(x)\,dx,
\qquad
T_n=\int_0^1\frac{x^{8n}g(x)}{16-x^8}\,dx.
$$

In the variable $t=x^8$, write $T_n=\int_0^1t^n\,d\rho(t)$, where

$$
d\rho(t)=w(t)\,dt,
\qquad
w(t)=\frac{g(t^{1/8})}{8t^{7/8}(16-t)}>0
\quad(0<t<1).
$$

This finite measure has full support $[0,1]$, no endpoint atoms, and
total mass $\alpha$. Its two endpoint behaviors are

$$
w(t)\sim\frac1{32}t^{-7/8}\quad(t\downarrow0),
\qquad
w(t)\sim\frac1{64}(1-t)\quad(t\uparrow1).
$$

These formulas follow by expanding the displayed fixed polynomial, not
by a probabilistic hypothesis. Let $E$ denote the forward shift in the
source index and $\Delta=E-1$. All differences below have nonnegative
integer start and order.

## 2. Exact positive forcing differences and uniform beta bounds

**Proved.** Define

$$
D_{n,k}=(-1)^k\Delta^kr(n+1)
       =\int_0^1x^{8n}(1-x^8)^kg(x)\,dx>0.
$$

The binomial theorem gives the integral directly. Evaluating its four
monomials gives an exact rational beta-integral oracle:

$$
\begin{aligned}
D_{n,k}=\frac18\big[&4\mathrm B(n+1/8,k+1)
-2\mathrm B(n+1/2,k+1)\\
&-\mathrm B(n+5/8,k+1)-\mathrm B(n+3/4,k+1)\big].
\end{aligned}
$$

The displayed beta combination has signed coefficients; its strict
positivity is supplied by the preceding integral. There is no reliance
on floating-point subtraction. For positive rational $a$,

$$
\mathrm B(a,k+1)=\frac{k!}{a(a+1)\cdots(a+k)}
$$

is rational and is evaluated exactly by the code. This identity is
Euler's beta integral, [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1).

There are simple all-parameter bounds. Put
$P(x)=4+4x+4x^2+2x^3+x^4$ and $S(x)=1+x+\cdots+x^7$.
For $0<x<1$,

$$
\frac{15}{8}<\frac{g(x)}{1-x^8}=\frac{P(x)}{S(x)}<4.
$$

The upper inequality follows coefficientwise from $4S-P>0$.
For the lower inequality,

$$
8P-15S=(1-x)(17+34x+51x^2+52x^3+45x^4+30x^5+15x^6)>0.
$$

Consequently, for every $n,k\geq0$,

$$
\boxed{\quad
\frac{15}{64}\mathrm B(n+1/8,k+2)
<D_{n,k}<\frac12\mathrm B(n+1/8,k+2).
\quad}
$$

These are genuine source-specific inequalities. They bound the signed
finite differences of the fixed forcing uniformly in both parameters.
They do not bound a count of real-close orbit pairs.

## 3. Positive tail differences, exact enclosures, and the two scales

**Proved.** Let

$$
R_{n,k}=(-1)^k\Delta^kT_n
       =\int_0^1\frac{x^{8n}(1-x^8)^kg(x)}{16-x^8}\,dx>0.
$$

The geometric expansion of the positive denominator gives

$$
R_{n,k}=\sum_{\ell\geq0}16^{-\ell-1}D_{n+\ell,k}.
$$

The moments $D_{n,k}$ strictly decrease with $n$. Therefore, if

$$
L_{n,k,H}=\sum_{\ell=0}^{H-1}16^{-\ell-1}D_{n+\ell,k},
\qquad H\geq1,
$$

then the strict rational enclosure is

$$
\boxed{\quad
L_{n,k,H}<R_{n,k}
<L_{n,k,H}+\frac{D_{n+H,k}}{15\,16^H}.
\quad}
$$

The remainder is bounded by a positive geometric series, with no
unstated cancellation. Also,

$$
\frac{D_{n,k}}{16}<R_{n,k}<\frac{D_{n,k}}{15},
\qquad
0<R_{n,k}-\frac{D_{n,k}}{16}<\frac{D_{n+1,k}}{240}.
$$

The last inequality follows from
$1/(16-t)-1/16=t/[16(16-t)]<t/240$ on $(0,1)$.

For **fixed $n$ and $k\to\infty$**, the beta formula and the gamma-ratio
asymptotic yield

$$
D_{n,k}\sim\frac{\Gamma(n+1/8)}2k^{-n-1/8},
\qquad
R_{n,k}\sim\frac{\Gamma(n+1/8)}{32}k^{-n-1/8}.
$$

The first term of the beta formula has the strictly smallest first
parameter. The bound on $R-D/16$ makes its contribution lower order.
The classical gamma-ratio input is
[DLMF 5.11.12](https://dlmf.nist.gov/5.11.E12); no asymptotic uniform in
jointly growing $n,k$ is inferred from this fixed-$n$ statement.

For **fixed $k$ and $n\to\infty$**, the other endpoint gives

$$
R_{n,k}\sim\frac{(k+1)!}{64\,n^{k+2}},
\qquad
D_{n,k}\sim\frac{15(k+1)!}{64\,n^{k+2}}.
$$

For example, divide the moment integral by $\mathrm B(n+1,k+2)$;
the beta probability weight concentrates at $t=1$, where
$w(t)/(1-t)\to1/64$. The part away from that endpoint is exponentially
small in $n$. The same argument with $(16-t)w(t)$ gives the factor 15.
The two limiting regimes must not be interchanged: the base-15
construction below uses $n=0$ and hence the much slower $k^{-1/8}$.

## 4. The signed Pascal source is an exact base-15 source

**Proved construction; normality transfer is not proved.** Set

$$
A_k=\Delta^kU_0
   =\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}U_j.
$$

Since $\Delta^k16^n=15^k16^n$,

$$
\boxed{\quad
A_k=15^k\alpha-(-1)^kR_{0,k}.
\quad}
$$

In particular $A_0=0$, and this construction retains the authentic
zero initial condition. Applying $\Delta^k$ to
$U_{n+1}=16U_n+r(n+1)$ gives the exact rational recurrence

$$
A_{k+1}=15A_k+(-1)^kD_{0,k}.
$$

The new forcing alternates. It is derived from the fixed BBP source;
it is not the original four-pole forcing under another name.
Its exact first state is $A_1=r(1)=47/15$.

The phase error satisfies

$$
\left\|A_k-15^k\alpha\right\|_{\mathbb R/\mathbb Z}
\leq R_{0,k}
\sim\frac{\Gamma(1/8)}{32k^{1/8}}\longrightarrow0.
$$

Thus the empirical laws of $\{A_k\}$ and $\{15^k\alpha\}$ have
the same weak limits on growing windows whose starting index tends to
infinity, and also on full prefixes by Cesaro averaging. This does
not identify either law with the empirical laws of $\{U_n\}$.

Dividing the recurrence by $15^{k+1}$ also gives an exact Euler/Pascal
series for the same selected constant:

$$
\pi=\frac{16}{15}\sum_{k\geq0}\frac{(-1)^kD_{0,k}}{15^k}.
$$

For truncation after $k$ terms, the correction is exactly
$16(-1)^kR_{0,k}/15^k$. The interval routine checks its sign against
an independent rational Machin-arctangent enclosure. This is a
classical kind of series transformation, not a priority claim or a
proof of digit cancellation.

## 5. The unsigned transform exposes an absolute-error trap

The other Pascal row gives

$$
B_k=(E+1)^kU_0=17^k\alpha-S_k,
\qquad
S_k=\int_0^1(1+t)^k\,d\rho(t)>0.
$$

**Proved.** Its remainder grows rather than vanishes:

$$
S_k\sim\frac{2^k}{16k^2}.
$$

To verify the constant, restrict first to $t\geq1/2$, where
$w(t)/(1-t)$ is bounded and tends to $1/64$ at 1. Substitute
$t=1-2v/k$ into $2^{-k}S_k$. The rescaled integrand converges to
$v e^{-v}/16$ after multiplication by $k^2$, with an integrable
bound proportional to $v e^{-v}$. The part $t<1/2$ contributes at
most $\rho([0,1/2])(3/4)^k$ to $2^{-k}S_k$.

Elementary global bounds already distinguish the behavior. The inherited
kernel inequalities

$$
\frac14(1-x)<\frac{g(x)}{16-x^8}<(1-x),\qquad 0<x<1,
$$

give, for $k\geq1$,

$$
\frac{2^k}{1024(k+1)^2}<S_k<\frac{4\,2^k}{k^2}.
$$

For the upper bound use
$((1+x^8)/2)^k\leq\exp[-k(1-x)/2]$ and integrate
$(1-x)\exp[-k(1-x)/2]$. For the lower bound restrict to
$1-1/[8(k+1)]\leq x\leq1$. There
$1-x^8\leq1/(k+1)$ and Bernoulli's inequality gives
$((1+x^8)/2)^k>1/2$.

The relative error $S_k/17^k$ tends to zero. Circle shadowing requires
an absolute error, or a separate bound on distance to integers.
Neither follows from this relative estimate. Unboundedness of $S_k$
alone does not prove that its fractional parts fail to approach zero;
the theorem here is exactly about the real remainder.

## 6. General integer filters and an endpoint obstruction

Let $P\in\mathbb R[t]$ be fixed. Finite linearity gives, for every
$n,k\geq0$,

$$
P(E)^kU_n=P(16)^k16^n\alpha
          -\int_0^1t^nP(t)^k\,d\rho(t).
$$

For nonconstant $P$, the following criterion is exact:

$$
\int_0^1P(t)^k\,d\rho(t)\longrightarrow0
\quad\Longleftrightarrow\quad
|P(t)|\leq1\text{ for every }t\in[0,1].
$$

For sufficiency, the equality set $|P|=1$ is finite, hence has
$\rho$-measure zero, and dominated convergence applies. For necessity,
if $|P(t_0)|>1$, continuity and full support supply an interval of
positive mass on which $|P|\geq1+\varepsilon$. The even moments
are then at least that mass times $(1+\varepsilon)^{2j}$ and cannot
tend to zero. For constant $P=c$, the criterion is instead $|c|<1$.

Now require **integer coefficients**, so applying $P(E)$ to circle
coordinates does not need a choice of integral lift. If $P(16)=q$
and the absolute residual tends to zero, then

$$
P(0),P(1)\in\{-1,0,1\},
\qquad
q\equiv P(0)\pmod {16},
\qquad
q\equiv P(1)\pmod {15}.
$$

Therefore:

- Bases $2,3,5,7,11,13$ fail the endpoint-0 condition.
- Base 17 passes endpoint 0 but fails endpoint 1.
- $P(t)=t-1$ realizes 15 and $P(t)=t$ realizes 16.
- Products $t^a(t-1)^b$ realize $16^a15^b$ with vanishing residual
  whenever $a+b>0$.

Passing the two congruence tests is only necessary in general; no
classification of every possible polynomial is claimed. This obstruction
concerns a fixed integer-polynomial filter and a vanishing **absolute
real** remainder. It does not exclude rational filters, growing-degree
filter families, transport matchings, or separate cancellation modulo 1.

## 7. Rational Pascal filters reach every integer base, with a carry cost

Rational coefficients escape the endpoint obstruction. For integers
$q\geq2$, $d\geq1$, define

$$
P_{q,d}(E)=\frac q{15^d}(E-1)^d,
\qquad
c=\frac q{15^d},
\qquad
X_k^{q,d}=P_{q,d}(E)^kU_0=c^kA_{dk}.
$$

**Proved.** The exact source identity is

$$
\boxed{\quad
X_k^{q,d}=q^k\alpha-(-1)^{dk}c^kR_{0,dk}.
\quad}
$$

If $q\leq15^d$, the absolute error tends to zero, with

$$
|X_k^{q,d}-q^k\alpha|
\sim\frac{\Gamma(1/8)}{32}\left(\frac q{15^d}\right)^k(dk)^{-1/8}.
$$

Multiplication of $X_k$ and its error by 16 gives a source shadowing
$q^k\pi$ directly. For all primes below 16, $d=1$ suffices. In
particular,

$$
X_k^{3,1}=\frac{A_k}{5^k},\qquad
X_k^{5,1}=\frac{A_k}{3^k}.
$$

The exact new forcing is

$$
X_{k+1}^{q,d}-qX_k^{q,d}
=c^{k+1}\sum_{j=0}^{d-1}
15^{d-1-j}(-1)^{dk+j}D_{0,dk+j}.
$$

Its sign is $(-1)^{dk}$: in the moment integral the bracket, after
extracting this sign, is

$$
\sum_{j=0}^{d-1}15^{d-1-j}(-1)^j(1-t)^j
=\frac{15^d-(-1)^d(1-t)^d}{16-t}>0.
$$

Thus even $d$ gives a positive derived forcing; odd $d$ gives an
alternating one. This does not preserve the original rational
four-pole form.

### 7.1 Exact multiplicative and power coherence

The finite operators commute and obey

$$
P_{q,d}P_{r,e}=P_{qr,d+e},
\qquad
X_k^{q^m,md}=X_{mk}^{q,d}.
$$

A degree choice coherent over all prime factorizations is

$$
D(q)=\sum_{p\mid q}v_p(q)d_p,
\qquad
d_p=\min\{d\geq1:p\leq15^d\}.
$$

Then $D(qr)=D(q)+D(r)$ and $q\leq15^{D(q)}$. It gives
$D(2)=1$, $D(4)=2$, $D(16)=4$ and hence

$$
P_{16,4}=P_{4,2}^{\,2}=P_{2,1}^{\,4},
\qquad
X_k^{16,4}=X_{2k}^{4,2}=X_{4k}^{2,1}.
$$

This is exact algebraic coherence among source filters. The degree
choice is not generally minimal, and the filtered base-16 sequence
is not identically the original $U_k$. Both shadow the same
$16^k\alpha$, so their circle distance tends to zero.

### 7.2 The lost integer carry is an exponentially growing coordinate

Reduce $c=a/b$ to lowest terms and write
$A_{dk}=C_k+x_k$, $C_k\in\mathbb Z$, $0\leq x_k<1$. Then

$$
\{X_k^{q,d}\}
=\left\{\frac{a^k(x_k+(C_k\bmod b^k))}{b^k}\right\}.
$$

The fractional part $x_k$ alone is insufficient when $b^k>1$.
Because $a^k$ is invertible modulo $b^k$, the $b^k$ possible carry
residues give $b^k$ distinct output phases, spaced by $1/b^k$.
This is a necessary and sufficient residue coordinate for a universal
readout across unrestricted integer lifts of the same fractional part.
It does not assert that every class occurs along the authentic source,
or exclude an arithmetic shortcut for computing the needed class.
For tripling the missing coordinate is exactly
$C_k\bmod5^k$; for the base-5 filter it is $C_k\bmod3^k$.

For example, $A_1=47/15=3+2/15$. The genuine base-3 filtered phase
is $47/75$, while dividing only the input fractional part by 5
gives $2/75$. Their discrepancy is $3/5$ before reduction modulo 1.
The exact test suite preserves this dropped-carry mutant.

The per-step operator degree can be fixed and small; after $k$
iterations it reads $dk+1$ source entries and requires a modulus
$b^k$. A finite initial prime list does not make this coordinate a
bounded amount of information uniformly in $k$.

## 8. Mandatory comparison: direct scaling already gives base filters

The existence of a source shadowing every base is not new by itself.
For the same fixed $q,d$ use

$$
Q_{q,d}(E)=\frac q{16^d}E^d,
\qquad
Y_k^{q,d}=\left(\frac q{16^d}\right)^kU_{dk}
=q^k\alpha-\left(\frac q{16^d}\right)^kT_{dk}.
$$

For $q\leq16^d$ its error vanishes, and for fixed $q,d$,

$$
|Y_k^{q,d}-q^k\alpha|
\sim\frac1{64d^2k^2}\left(\frac q{16^d}\right)^k.
$$

At matched degree this is asymptotically smaller than the Pascal error:

$$
\frac{|X_k^{q,d}-q^k\alpha|}
     {|Y_k^{q,d}-q^k\alpha|}
\sim2\Gamma(1/8)d^{15/8}k^{15/8}
     \left(\frac{16}{15}\right)^{dk}\longrightarrow\infty.
$$

Direct filters have the same formal product and power coherence.
The Pascal construction's distinct feature is the changed arithmetic
support of the needed carry, together with the exact forcing-difference
structure. At $d=1$:

| Multiplier $q$ | Pascal carry modulus | Direct carry modulus |
| --- | --- | --- |
| 2 | $15^k$ | $8^k$ |
| 3 | $5^k$ | $16^k$ |
| 5 | $3^k$ | $16^k$ |
| 7, 11, 13 | $15^k$ | $16^k$ |

It is therefore inaccurate to advertise the rational Pascal construction
as the first base conversion, an improvement in the real shadow rate,
or a proof that those carry residues have uniform conditional weights.

## 9. Why Pascal row sums do not supply a probability theorem

There are two different operations.

First, averaging **observables** with normalized Pascal weights gives

$$
2^{-k}\sum_{j=0}^k\binom{k}{j}f(y_{n+j}).
$$

For any sequence on the circle and an empirical window of $N$ points,
the corresponding averaged measure differs in $W_1$ from the original
window measure by at most

$$
\sum_{j=0}^k2^{-k}\binom{k}{j}\frac{\min(j,N)}{2N}
\leq\frac{k}{4N}.
$$

This is just the shared interior of two shifted windows; the circle
has diameter $1/2$. For an invariant law $\mu$,
$2^{-k}(I+(T_{16})_*)^k\mu=\mu$. In particular the non-Haar
base-16 law with independent fair digits in $\{0,1\}$ is preserved.
The row sum $2^k$ has not supplied new independent source choices.

Second, adding **phase values** with integer coefficients gives
$\{\sum_jc_jU_{n+j}\}$. This is a function of their joint law.
Its output law need not equal any input marginal. With rational
coefficients it also needs the integral-carry data described above.

For the rational filter at a translated start $n$, the exact formula is

$$
P_{q,d}(E)^kU_n
=q^k16^n\alpha-(-1)^{dk}c^kR_{n,dk}.
$$

For fixed $q,d,k$ and $n\to\infty$, this output approaches
$q^ky_n$ on the circle. Consequently the output law approaches
$(T_{q^k})_*\mu$ if the input window law approaches $\mu$.
The still-missing assertion is that this output law also approaches
$\mu$. The exact kernel identity alone proves the former statement,
not the latter.

There is an exact control for the distinction. Take the inherited
rational counterfeit tail

$$
T_n^*=\frac1{(n+1)(n+2)}=\int_0^1t^n(1-t)\,dt,
\qquad
U_n^*=\frac{16^n}{2}-T_n^*.
$$

It has $U_0^*=0$ and positive rational forcing
$16T_{n-1}^*-T_n^*$ for $n\geq1$. All the polynomial-filter identities,
strict moment signs, and rational-filter coherence laws still hold.
Here they evaluate explicitly to

$$
A_k^*=\frac{15^k}{2}-\frac{(-1)^k}{k+2},
\qquad
X_k^{*,q,d}=\frac{q^k}{2}
-\frac{(-1)^{dk}(q/15^d)^k}{dk+2}.
$$

For $q\leq15^d$, the filtered empirical laws converge to an atom:
at $1/2$ for odd $q$ and at 0 for even $q$. This is not the fixed
BBP forcing. It proves that the general moment/filter/coherence
mechanism itself supplies no distribution theorem; a successful
argument must use an additional quantitative property of the
authentic source.

## 10. Explicit coefficient, endpoint, and pair-count costs

The signed Pascal row has coefficient norm
$\sum_j|(-1)^{k-j}\binom{k}{j}|=2^k$.
If real input errors are each at most $\varepsilon$, the transformed
real error is at most $2^k\varepsilon$. For an integer-coefficient
circle combination the same bound holds using circle distances.
Rational combinations need fixed compatible lifts or cover data
before such a bound is meaningful. The exact positive kernel above
can improve a generic error bound, but it cannot be replaced by an
unproved random-sign cancellation factor.

For the rational filter iterated $k$ times, the coefficient norm is
exactly $c^k2^{dk}=[q(2/15)^d]^k$. This can grow even when $c<1$;
for example it grows for $q=13,d=1$. The direct filter at the same
degree has just one coefficient, of magnitude $(q/16^d)^k$.

For example, the authentic signed row at a late index obeys

$$
\Delta^kU_n-15^kU_n=15^kT_n-(-1)^kR_{n,k},
$$

so, using the inherited $T_n<1/[(8n+1)(8n+2)]$ and $R_{n,k}\leq T_n$,

$$
\left\|\Delta^kU_n-15^ky_n\right\|_{\mathbb R/\mathbb Z}
<\frac{15^k+1}{(8n+1)(8n+2)}.
$$

The multiplier cost is present even though the kernel residual
$R_{n,k}$ itself is small. Thus a choice $k=k(n)$ needs an explicit
growth condition; a fixed-$k$ asymptotic cannot be used uniformly
through an arbitrary window depth.

For ordered inclusive close-pair counts
$Q_z(\tau)=\#\{(i,j):\|z_i-z_j\|\leq\tau\}$, a coordinatewise
circle coupling with error at most $\varepsilon$ gives

$$
Q_z(\tau)\leq Q_w(\tau+2\varepsilon),
\qquad
Q_w(\tau-2\varepsilon)\leq Q_z(\tau)
\quad(\tau\geq2\varepsilon).
$$

Every such count includes the $N$ diagonal pairs. The lower estimate
is not asserted with radius zero substituted for a negative radius:
distinct $w_i$-labels can coincide while their coupled $z_i$ values
separate. Removing $L$ entries from $N$ can remove up to exactly
$2LN-L^2$ ordered pairs, including the removed diagonals. Any
retention estimate deduced from shortened transformed windows must
retain this endpoint cost. Keeping a degree-$dk$ filter entirely
inside an original window requires removing $dk$ starting positions,
when $dk\leq N$, or explicitly providing the extra source entries.

These bookkeeping facts do not yet control how many real-close pairs
choose the central inverse branch. In particular, an $O(N)$ error
in a pair-count inequality cannot absorb an unknown positive
proportion of $N^2$ pairs.

## 11. Claims, novelty tax, and the next source-specific test

| Claim | Status | Exact boundary |
| --- | --- | --- |
| Positive two-parameter forcing/tail difference kernels | Proved, building on inherited Hausdorff representation | Not a real pair-count estimate |
| Uniform rational beta bounds and geometric enclosures | Proved | No float-derived universal claim |
| Signed Pascal base-15 shadow and Euler series | Proved source construction | No identification with the original window law |
| Unsigned base-17 absolute remainder grows as $2^k/(16k^2)$ | Proved | No assertion about its fractional-part distribution |
| Fixed integer-filter endpoint obstruction | Proved | Absolute real remainder and fixed polynomial only |
| Rational filters for every integer base, with multiplicative coherence | Proved construction | Direct scaling is an existing elementary baseline |
| Carry coordinate for the base-3 Pascal filter is modulo $5^k$ | Proved exact readout | No uniformity of those source carry residues |
| Real half-retention or same-law tripling transport | OPEN | Neither follows from row sums, moment positivity, or source shadowing |

The strongest surviving test concerns a joint law, rather than merely
another formula for pi. On the actual selected good-prime windows,
retain the exact integral carries of the rational filter and compare
the output empirical measure with the **same** original empirical
measure, with the tail and endpoint budgets above. A vanishing
tripling discrepancy would close one independent input of the
[base-three rigidity route](PI_BASE_THREE_RIGIDITY.md); positive
all-scale collision dimension would still be required there.

The direct carry route instead needs a source-derived bound on the
conditional central-branch frequency. This lane supplies no such
frequency bound. The present progress is a verified kernel instrument,
an exact arithmetic comparison of candidate base filters, and a
scoped obstruction that prevents an absolute-error argument from
silently skipping its integer-carry coordinate.

## 12. Verification and provenance

The 15 focused unit tests pass. They include:

- Literal four-pole finite differences at starts 0 through 16 and
  orders 0 through 16, checked against the independent beta evaluator.
- Fresh starts 19, 31, 64, 127 and orders 17 through 40, with exact
  sign and beta-bound comparisons.
- Positive geometric tail enclosures checked against independently
  differenced source-tail enclosures.
- Authentic Pascal rows through order 40 checked by a literal
  difference triangle of the original rational states.
- Derived source recurrences, rational-filter composition, coherent
  $16\to4\to2$ power reductions, and exact retained-carry readouts.
- The rational positive-moment counterfeit, which retains the filter
  algebra while every derived base law converges to an atom.
- Independent Machin-arctangent pi enclosures, an incorrect odd-order
  correction-sign mutant, and a dropped-carry mutant.

All executable claims are limited to their executed finite ranges.
The all-parameter inequalities and asymptotic statements rest on the
proofs above. No full-suite or hosted-CI status is claimed by this lane.

The authentic BBP source, tail identity, and original positivity
provenance are recorded in
[BBP source memory](BBP_SOURCE_MEMORY_REPAIR.md), with implementation
[`bbp_source_memory.py`](../../observational_succ/bbp_source_memory.py).
The only external analytic formulas used here are Euler's beta
integral and the gamma-ratio asymptotic, at their official DLMF
equation URLs given above. The filter and obstruction arguments are
fully derived here; no secondary theorem summary is used as authority.
