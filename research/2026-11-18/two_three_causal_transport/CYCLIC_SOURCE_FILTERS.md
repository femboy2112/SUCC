# BBP cyclic filters, local precision, and the causal closure defect

**Status:** exact algebraic results and explicitly bounded finite checks. This is
a source-specific observer construction, not an asymptotic estimate for the
selected BBP orbit. No scholarly-priority claim is made. The source, literal
zero seed, and historical research files are unchanged.

## 1. Source and operator types

For the original source and integer `n>=1`, set `a=8n-8`:

```math
r(n)=\int_0^1 t^a Q(t)\,dt,
\qquad Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),
```

```math
H(t)=4+4t+4t^2+2t^3+t^4=(t^2+2)(t^2+2t+2).
```

Three shifts have different domains:

| Shift | Domain and meaning | Law |
|---|---|---|
| `S_m` | Coefficient columns in `Z[t]/(t^m-1)`; simultaneous cyclic channels | `S_m^m=I` |
| `L_N` | A length-`N` causal record with zero prehistory; `(L_N u)_j=u_(j-1)` | `L_N^N=0` |
| Mellin exponent shift | `m_a=1/(a+1)`; advancing exponent `a` by one | Multiplication of the integrand by `t` |

The actual BBP chronological increment `n -> n+1` advances the exponent by
**eight**, so its Mellin multiplier is `t^8`. None of the operator identities
below silently identifies a one-channel shift with one BBP time step. If the
Mellin moments are presented in a descending finite record, a causal backshift
represents the forward exponent shift on interior evaluations for which all
needed moments are present. At the record boundary the missing moments must
be retained as extra data: substituting zero prehistory does not equal the
untruncated Mellin shift. That ordering is an additional declared observation
protocol, not time reversal in the carrier.

The cyclic map is `C_m=H(S_m)`. It is selected by the exact source polynomial,
but acts on a declared channel vector. It is not a claim that the actual BBP
trajectory is periodic.

## 2. General cyclic determinant and uniform 2-adic isometry

**CSF-01 — PROVED.** For every integer `m>=1`, put

```math
c_m=(-1+i)^m+(-1-i)^m,
\qquad c_0=2,\quad c_1=-2,\quad c_m=-2c_{m-1}-2c_{m-2}.
```

Then

```math
\det C_m=A_m\bigl(2^m+1-c_m\bigr),
```

where

```math
A_m=\begin{cases}
2^m+1,&m\text{ odd},\\
\bigl(2^{m/2}-(-1)^{m/2}\bigr)^2,&m\text{ even}.
\end{cases}
```

In particular the determinant is a positive odd integer and
`C_m in GL_m(Z_2)`. For the maximum norm on `Q_2^m`,

```math
\|C_m v\|_2=\|v\|_2\qquad(v\in\mathbb Q_2^m).
```

**Proof.** The determinant is `product_(zeta^m=1) H(zeta)`. In the factor
`t^2+2`, squaring permutes the roots for odd `m`; for even `m` it maps them
two-to-one onto the `(m/2)`-th roots. This gives `A_m`. The roots of
`t^2+2t+2` are `alpha=-1+i` and its conjugate, so its product is
`(alpha^m-1)(conj(alpha)^m-1)=2^m+1-c_m>0`. Both factors are odd. More
directly `H(t)=t^4 mod2`, hence `C_m=S_m^4 mod2`, a permutation matrix.
An integral matrix with unit determinant and its inverse both have maximum
operator norm at most one; applying the two inequalities proves equality.

This exact 2-adic statement holds at all channel counts. It supplies no
real-circle distribution theorem for `U_n`.

## 3. Exact inverse and precision costs at three and five channels

Define integer polynomials

```math
J_3(t)=16-14t+t^2,
\qquad J_5(t)=206-199t-4t^2+116t^3-64t^4.
```

**CSF-02 — PROVED.** The following identities hold in `Z[t]`:

```math
H(t)J_3(t)-45=(t^3-1)(t^3-12t^2-8t-19),
```

```math
H(t)J_5(t)-825=(t^5-1)(1-28t-12t^2-64t^3).
```

Consequently

```math
C_3^{-1}=\frac{J_3(S_3)}{45},\qquad
C_5^{-1}=\frac{J_5(S_5)}{825}.
```

The integer Smith normal forms are respectively

```math
\operatorname{diag}(1,1,45),\qquad
\operatorname{diag}(1,1,1,1,825).
```

**Proof.** Polynomial multiplication proves the displayed identities. The
determinant formula gives `45` and `825`; thus `J_m(S_m)` is the adjugate.
Its entries are the polynomial's coefficients. For `m=3` these include `1`;
for `m=5`, `gcd(4,199)=1`. The gcd of all codimension-one minors is therefore
one in each case. The Smith determinantal-divisor identities force every
invariant factor except the last to be one.

For the induced maximum norm on `Q_p^m` the sharp inverse norms are:

| Map | `p=2` | `p=3` | `p=5` | `p=11` | Other primes |
|---|---:|---:|---:|---:|---:|
| `C_3^-1` | 1 | 9 | 5 | 1 | 1 |
| `C_5^-1` | 1 | 3 | 25 | 11 | 1 |

The largest `p`-adic absolute value of a matrix entry is its induced maximum
norm; a coordinate vector attains it. The numerator coefficient `16` is a
unit at `3,5`, while `206` is a unit at `3,5,11`, proving sharpness. Thus
worst-case reconstruction of `k` input ternary digits requires `k+2` output
digits for the three-channel observer and `k+1` for the five-channel
observer. Their quinary precision costs are reversed: one and two digits.

These are exact worst-case transport costs for these maps. They are neither
probabilities nor error estimates for an unprovided observation protocol.

### A concrete extra-prime control

For the convention `C_5[i,j]=h[(i-j) mod5]`, where `h=(4,4,4,2,1)`,

```math
v=(1,4,5,9,3)\not\equiv0\pmod{11},\qquad C_5v\equiv0\pmod{11}.
```

Indeed `3^5=1 mod11` and `H(3)=0 mod11`; the vector is
`(1,3^-1,3^-2,3^-3,3^-4) mod11`. Constant vectors are killed modulo three
and five because `H(1)=15`.

Thus the pentagonal source observer has an unavoidable prime-11 precision
defect. A proposed arithmetic inventory closed under only the primes
`{2,3,5}` fails this exact control.

## 4. What the source's F_10 identity says

**CSF-03 — PROVED.** The cyclic autocorrelation of `(4,4,4,2,1)` is
`(53,46,40,40,46)`. Therefore the nonconstant eigenvalues of the real Gram
matrix `C_5^*C_5` are

```math
10+3\sqrt5\quad\text{(twice)},\qquad
10-3\sqrt5\quad\text{(twice)}.
```

The constant eigenvalue is `225`. The determinant on the nonconstant
subspace is, for `C_5` itself,

```math
(10+3\sqrt5)(10-3\sqrt5)=55=F_{10},
\qquad \det C_5=15F_{10}=825.
```

**Proof.** Diagonalize the circulant by the five characters. Its Gram
eigenvalue at angle `theta` is
`53+92 cos(theta)+80 cos(2theta)`. Substituting the nontrivial fifth-root
angles gives the stated values. Conjugate pairs multiply to those squared
absolute values, yielding the determinant of `C_5` on the augmentation
subspace.

At factor level, with `zeta` primitive of order five,

```math
\operatorname{Norm}_{\mathbb Q(\zeta)/\mathbb Q}(\zeta^2+2)=11,
\qquad
\operatorname{Norm}_{\mathbb Q(\zeta)/\mathbb Q}(\zeta^2+2\zeta+2)=5.
```

The first is `Phi_5(-2)=11`; the second follows from the determinant
factorization or direct multiplication. This makes the source's `55=5*11`
fully concrete and agrees with `F_10=F_5 L_5`.

The stronger proposed law `det C_m/15=F_(2m)` for every `m` is
**REFUTED**: `m=3` gives `3`, whereas `F_6=8`. An exact special-value
identity is not a general Fibonacci recurrence for these determinants.

## 5. A precise construction for the three pairs of cycle lengths

For coprime positive integers `a,b`, simultaneous successor
`(u,v)->(u+1,v+1)` on `Z/a x Z/b` is conjugate, by the Chinese remainder
map, to successor on `Z/(ab)`. Therefore evaluating the same source filter
on the paired-clock state is exactly `H(S_(ab))` in a permuted basis.

This defines paired clocks `(2,3)`, `(2,5)`, and `(3,5)` without asserting
that it is identical to the recovered quadratic Fibonacci-frame construction
from the prior conversation. That construction is documented in
[Fibonacci source transport](FIBONACCI_SOURCE_TRANSPORT.md); its dimensions
10 and15 do not make its successor a cyclic shift of those orders. The
CRT construction supplies a separate testable comparison of local precision.

| Paired clocks | `m` | Exact determinant | Smith entries exceeding one |
|---|---:|---|---|
| `(2,3)` | 6 | `5265=3^4*5*13` | `9,585` |
| `(2,5)` | 10 | `1116225=3^2*5^2*11^2*41` | `33,33825` |
| `(3,5)` | 15 | `1082196225=3^2*5^2*11*331*1321` | `1082196225` |

The determinant entries are **PROVED** instances of CSF-01. The Smith
entries in this table are **VERIFIED_FINITE** exact integer computations;
all omitted entries are one. They were compared with exact direct
circulant matrices. The elementary adjugate proof above is supplied for
`m=3,5`; no unexecuted all-size Smith classification is asserted.

Primes `13,41,331,1321` are further receipts against interpreting paired
cycle lengths as a closed prime inventory. CRT supplies the state-space
conjugacy, not stochastic independence or real-phase cancellation.

## 6. Closing a causal record changes its local arithmetic

**CSF-04 — PROVED.** For the nilpotent causal backshift `L_N` on a finite
record of length `N>=1`, both `H(L_N)` and `Q(L_N)` are lower triangular
with diagonal entry four. Hence

```math
\det H(L_N)=\det Q(L_N)=4^N=2^{2N}.
```

Both are isometries for the maximum norm over `Q_p^N` for every odd prime
`p`; neither is invertible over `Z_2`. Modulo two,

```math
H(L_N)=L_N^4,\qquad Q(L_N)=L_N^4(I+L_N),
```

and each has rank `max(N-4,0)` and kernel dimension `min(N,4)`.

**Proof.** Triangularity gives the determinants. A determinant which is an
odd-prime unit gives an integral inverse and the isometry argument of
CSF-01. The mod-two polynomial identities follow from the literal
coefficients. `I+L_N` is invertible because `L_N` is nilpotent, so it does
not change the rank or kernel of `L_N^4`.

For a causal output prefix reduced modulo two, the four most recent input
bits have not yet appeared. Once four further output samples have arrived,
the delayed bits can be read from retained history. This is a precise
delay statement for the declared filter, not a claim about four BBP
epochs. Cyclic closure replaces that delay by the wraparound permutation
`S_m^4` and changes which local primes obstruct inversion.

The difference operator also changes type: `I-L_N` is invertible by the
finite cumulative sum `I+L_N+...+L_N^(N-1)`, whereas `I-S_m` kills every
constant vector. Thus `Q(S_m)` always loses the constant channel. The
causal initial-value record supplies an integration constant that a
periodic difference quotient discards.

This is an exact discriminator between a moving observer's finite history
and a completed cycle. It does not turn observer conditioning into the
unknown signed statistics of the authentic zero-seeded orbit.

### 6.1 The exact eight-exponent/radix-16 transport

**CSF-06 — PROVED.** There is an integer complementary filter

```math
K(t)=4-4t+2t^3-t^4=(2-t^2)(t^2-2t+2)
```

such that

```math
H(t)K(t)=16-t^8.
```

Consequently, as a formal power series, or modulo `t^N`,

```math
\frac1{H(t)}
=\frac{K(t)}{16-t^8}
=\sum_{q\ge0}\frac{t^{8q}}{16^{q+1}}
       (4-4t+2t^3-t^4).
```

No convergence assumption is needed when substituting the nilpotent
`L_N`: only finitely many terms survive. If `N-1=8q+r`, `0<=r<=7`, then
the exact maximum operator norm is

```math
\|H(L_N)^{-1}\|_2
=\|Q(L_N)^{-1}\|_2
=2^{\,4q+2+\mathbf1_{r\ge3}+\mathbf1_{r\ge4}}.
```

In particular, for every integer `n>=1`, a causal record of length `8n`
has sharp inverse norm `16^n` in the 2-adic metric.

**Proof.** The two factorizations of `16-t^8` give the polynomial identity.
The inverse coefficients in each eight-entry block are
`16^-q*(1/4,-1/4,0,1/8,-1/16,0,0,0)`. The largest 2-adic absolute
coefficient retained through degree `N-1` gives exactly the displayed
exponent, and a coordinate vector attains it. Further,
`Q(L_N)=(I-L_N)H(L_N)` and `I-L_N` is a 2-adic isometry with isometric
inverse. Composition with an onto isometry leaves the operator norm
unchanged.

The exponent step eight is now explicit, so this is a genuine algebraic
connection to the source's radix sixteen. It is also compatible with the
homogeneous BBP recurrence: a seed difference is multiplied by `16^n`,
which contracts its 2-adic norm by `16^-n`; undoing that forward transport
costs precisely the opposite precision factor. This compatibility does
not identify arbitrary filter inputs with the selected BBP trajectory.

For a source-typed version, define the rational off-grid moments

```math
R_a=\int_0^1t^aQ(t)\,dt,\qquad
d_a=\int_0^1t^a(1-t)\,dt
=\frac1{a+1}-\frac1{a+2}\qquad(a\ge0).
```

The identity gives, without changing any coefficient,

```math
4R_a-4R_{a+1}+2R_{a+3}-R_{a+4}=16d_a-d_{a+8}.
```

At `a=8n-8`, `R_a` is the literal forcing `r(n)`; the other three terms
are declared exponent-shifted source channels, not unexplained extra
BBP time samples. This is a concrete instance of the inherited
`(16-t^8)` source-null relation discussed in
`docs/PI_NORMALITY_FRONTIER.md`, section 9. It provides an exact transport
law and not a new signed asymptotic estimate.

### 6.2 Eight channels: the exact sixteen-versus-fifteen comparison

**CSF-07 — PROVED.** At the source-matched exponent width eight, the same
complementary filter satisfies

```math
H(S_8)K(S_8)=15I,\qquad H(L_8)K(L_8)=16I.
```

The corresponding exact determinants are

```math
\det H(S_8)=15^4=50625,\qquad
\det H(L_8)=16^4=65536.
```

Thus their inverses are `K(S_8)/15` and `K(L_8)/16`. The cyclic observer
is a 2-adic isometry, with sharp inverse norms three and five at those
odd places. The causal observer is an isometry at every odd prime, with
sharp 2-adic inverse norm sixteen. In these explicit operators the
arithmetic transfer between `2` and `3*5` is the difference between
`S_8^8=I` and `L_8^8=0`. It is not a symmetry assumed from the cycle names.

**Proof.** Substitute the two shift laws into `HK=16-t^8`; CSF-01 and
triangularity give the determinants. Each row of the cyclic inverse has
the four nonzero coefficients of `K/15`, while the causal inverse contains
those coefficients below the diagonal. At each relevant prime a unit
coefficient attains the asserted norm. The difference in shift laws is
exactly the closure convention: cyclic wraparound inserts later channel
values into the early output coordinates; zero prehistory does not.

For comparison with the ordinary real metric, every finite causal
`H(L_N)^-1` obeys the **uniform** maximum norm bound

```math
\|H(L_N)^{-1}\|_{\infty,\mathbb R}
\le\sum_{q\ge0}\frac{4+4+2+1}{16^{q+1}}=\frac{11}{15}.
```

This uniform constant is sharp as `N` grows: the final inverse row collects
successively longer initial segments of the coefficient series, and
choosing input signs to match that row attains its absolute row sum.
At `N=8` the exact causal real norm is `11/16`; the cyclic real norm is
`11/15`. Thus a filter may be stably inverted in the real norm while
requiring linearly increasing binary precision for its inverse. This last
uniform bound concerns `H`, not the additional cumulative inverse of `Q`.

### 6.3 All source-matched widths: four retained obstruction coordinates

**CSF-08 — PROVED.** For an integer block count `n>=1`, set
`N=8n`, `D_n=16^n-1`, and

```math
P_n(t)=K(t)\sum_{j=0}^{n-1}16^{n-1-j}t^{8j}.
```

Then

```math
H(t)P_n(t)=16^n-t^N,
\qquad
H(S_N)^{-1}=\frac{P_n(S_N)}{D_n},\qquad
H(L_N)^{-1}=\frac{P_n(L_N)}{16^n}.
```

The complete integer Smith normal forms are

```math
\begin{aligned}
H(S_N)&:\quad\operatorname{diag}
 (\underbrace{1,\ldots,1}_{N-4},D_n,D_n,D_n,D_n),\\
H(L_N)&:\quad\operatorname{diag}
 (\underbrace{1,\ldots,1}_{N-4},16^n,16^n,16^n,16^n).
\end{aligned}
```

Thus the cyclic and causal determinants are `D_n^4` and `16^(4n)`.
Exactly four invariant coordinates carry the respective integral
obstruction; this is not a statement that four scalar observations suffice
to recover an unspecified BBP orbit.

**Proof by polynomial modules.** Multiplying `HK=16-t^8` by the finite
geometric sum proves the identity. The two cokernels, with the coefficient
column conventions of Section 1, are

```math
\begin{aligned}
\operatorname{coker}H(S_N)
&\cong\mathbb Z[t]/(H,t^N-1)
=\mathbb Z[t]/(H,D_n),\\
\operatorname{coker}H(L_N)
&\cong\mathbb Z[t]/(H,t^N)
=\mathbb Z[t]/(H,16^n).
\end{aligned}
```

The ideal equalities follow directly from `HP_n=16^n-t^N`.
Since `H` is monic of degree four, division by `H` leaves the free
coefficient basis `1,t,t^2,t^3` over either scalar residue ring. The
cokernels are consequently `(Z/D_n)^4` and `(Z/16^n)^4`, proving the Smith
forms and determinants.

There is also a direct matrix certificate. In either matrix take rows
`4,...,N-1` and columns `0,...,N-5`. The resulting `(N-4)`-square minor is
upper triangular with diagonal one. In the cyclic case a negative raw
index difference wraps to at least nine, outside the coefficient support
`0,...,4`, so no extra entry appears below that diagonal. This verifies
the `N-4` unit invariant factors without the module presentation. The
displayed inverse denominators and determinant then force each of the
four remaining factors to equal its stated scalar.

The coefficient of `t^(N-4)` in `P_n` is `-1`, and `deg P_n=N-4<N`, so
there is no coefficient aliasing in the cyclic inverse. Hence, for every
prime `p`, the sharp local inverse norms are

```math
\boxed{\|H(S_N)^{-1}\|_p=p^{v_p(D_n)},}
\qquad
\boxed{\|H(L_N)^{-1}\|_p=p^{v_p(16^n)}.}
```

In particular the causal observer costs `4n` binary digits and no
odd-prime digits, while the cyclic observer costs no binary digits and

```math
v_3(D_n)=1+v_3(n),\qquad v_5(D_n)=1+v_5(n)
```

ternary and quinary digits respectively. These last identities follow by
the elementary odd-prime binomial lifting identity applied to `16=1+15`.
Other primes dividing `D_n` must also be retained. The result does not
close the arithmetic inventory at three and five.

The ordinary real maximum norms also have exact formulas at these widths:

```math
\|H(S_N)^{-1}\|_{\infty,\mathbb R}=\frac{11}{15},\qquad
\|H(L_N)^{-1}\|_{\infty,\mathbb R}
=\frac{11}{15}(1-16^{-n}).
```

Indeed the disjoint eight-entry coefficient blocks of `P_n` have total
absolute sum `11(16^n-1)/15`; every cyclic row, and the final causal row,
contains all these coefficients. The closeness of these two norm values
does not claim that the two operators themselves are close: their
wraparound actions differ.

### 6.4 Exact connection to the virtual periodic-path grid

For `T(z)=16z mod1` on `R/Z`, the points whose periods divide the positive
integer `n` are exactly

```math
\operatorname{Fix}(T^n)
=\left\{\frac{j}{16^n-1}\bmod1:0\le j<16^n-1\right\}.
```

This follows by rearranging `16^n z=z mod1`. Thus the same integer `D_n`
which measures the cyclic source-filter obstruction is the exact
denominator of the period-dividing-`n` reference grid. With the monic
remainder basis above and the map `a mod D_n -> a/D_n mod1`, CSF-08 gives
an explicit identification of finite abelian groups

```math
\operatorname{coker}H(S_{8n})
\cong\operatorname{Fix}(T^n)^4.
```

This identification is an exact finite link between the source's loop
closure and virtual periodic paths. Here `n` denotes the number of
eight-exponent blocks. The equality of that cadence with the BBP
radix-16 step comes from the source polynomial, and is not an assertion
that an arbitrary channel vector is the literal `n`-step BBP orbit.

No separation estimate for the authenticated point `pi/16` from these
grids is supplied. In particular the obstruction-group identity neither
bounds shadowing lengths nor forbids arbitrarily late shells of nearly
locked phases. Such a signed or Diophantine bound remains the next
proof obligation.

### 6.5 The literal signed source: its free constant coordinate

**CSF-09 — PROVED.** Keep the full original polynomial
`Q(t)=(1-t)H(t)`, and let `N=8n`, `D_n=16^n-1` as above. Its cyclic
integer Smith form is

```math
Q(S_N):\quad\operatorname{diag}
\left(\underbrace{1,\ldots,1}_{N-5},
\frac{D_n}{15},D_n,D_n,D_n,0\right).
```

For `n=1`, the displayed `D_n/15` is itself a unit. Its causal Smith form
is the same as that of `H(L_N)`:

```math
Q(L_N):\quad\operatorname{diag}
\left(\underbrace{1,\ldots,1}_{N-4},
16^n,16^n,16^n,16^n\right).
```

Thus the full signed source carries both the finite closure obstruction
and a free cyclic coordinate. In the coefficient-column convention the
free coordinate is the integer sum `f(1)` of all channel coefficients,
the unnormalized constant Fourier readout. The output of `Q(S_N)` always
has sum zero; it cannot recover an input constant channel by inversion.
No division by `N`, averaging convention, or artificial restoration of
that missing information is used here.

**Proof.** Put `A_N(t)=(t^N-1)/(t-1)` and
`B=Z[t]/((t-1)H,t^N-1)`, the cokernel of multiplication by `Q` up to an
irrelevant global minus sign. Evaluation at one gives a split exact
sequence of abelian groups

```math
0\longrightarrow\mathbb Z[t]/(H,A_N)
\xrightarrow{\ f\mapsto(t-1)f\ } B
\xrightarrow{\ f\mapsto f(1)\ }\mathbb Z
\longrightarrow0.
```

The splitting sends an integer to its constant polynomial. Exactness
follows because every polynomial vanishing at one is divisible by `t-1`,
and cancellation of `t-1` in the integral domain `Z[t]` identifies the
kernel of the first presentation map with the ideal `(H,A_N)`.

In the free rank-four ring `R=Z[t]/H`, the identity `t^8=16` gives

```math
A_N=\frac{D_n}{15}A_8.
```

Let `M` denote multiplication by `t-1` on `R`. Its cokernel is
`R/(t-1)=Z/H(1)=Z/15`, so its Smith form is `(1,1,1,15)`.
Multiplication by `A_8` obeys `M A_8=15I` in this basis. Applying the
unimodular matrices which diagonalize `M` shows that multiplication by
`A_8` has Smith form `(1,15,15,15)`. Scaling by the integer `D_n/15`
therefore gives `(D_n/15,D_n,D_n,D_n)`. Together with the free integer
coordinate this proves the cyclic formula.

For the causal formula, `Q(L_N)=(I-L_N)H(L_N)` and the factor `I-L_N`
is integer unimodular, with integer inverse `I+L_N+...+L_N^(N-1)`.
It leaves the Smith form unchanged. QED.

As a compact finite certificate, every `(N-1)`-square minor of `Q(S_N)`
has absolute value `D_n^4/15`. Its left and right rational kernels are
the primitive constant vectors, so its adjugate has all entries equal
up to the cofactor sign convention. The gcd of those maximal minors is
the product of the nonzero Smith factors, namely `D_n^4/15`.

This retains the literal four-pole signed source rather than assigning
invertibility of its positive factor to `Q` itself. The free cyclic
coordinate and the causal initial-value record remain explicit. The
classification does not supply a bound separating the authentic orbit
from the periodic reference grid.

## 7. Retain the closure residual and the original Mellin source

**CSF-05 — PROVED.** Applying CSF-02 to any linear operator `L` gives

```math
H(L)J_5(L)=825I+(L^5-I)(I-28L-12L^2-64L^3).
```

The final term vanishes for the cyclic channel rotation. On a causal
record it measures the retained five-step discrepancy and is generally
nonzero throughout the record, not only at its initial boundary. Its
evaluation uses at most eight previous entries, so retaining it needs
memory; it does not require physically going backwards in time.

Separately, reducing the literal Mellin polynomial `Q` modulo `t^5-1`
gives `Q_c(t)=3-2t^3-t^4`. The lost source is exactly

```math
\begin{aligned}
r(n)-\int_0^1t^{8n-8}Q_c(t)\,dt
&=\int_0^1t^{8n-8}(1-t^5)\,dt\\
&=\frac5{(8n-7)(8n-2)}.
\end{aligned}
```

Since `Q(t)=(1-t)H(t)` and `H(1)=15`, either the rational expansion or the
elementary endpoint moment asymptotic gives
`r(n)~15/(64n^2)`. The discarded term is therefore asymptotic to
**one third of the forcing**. Treating the source as cyclic without
retaining this discrepancy changes the leading source coefficient.

## 8. Earned scope and next falsifier

These results establish a literal connection between the BBP polynomial,
cyclic channels, p-adic conditioning, and information unavailable to a
finite causal observer until a later reading. They recover the pentagonal
`F_10` identity and expose its additional prime content. Their proof debt
is finite algebra, paid by the identities above.

They do not establish independence of prime clocks, a density theorem for
literal BBP carries, an all-shell anti-lock bound, Fourier decay, Collatz
termination, or completed Weil positivity. Those claims require their
own source-faithful transport and asymptotic inequalities.

Useful falsifiers for any proposed extension are the mod-11 null vector,
the `m=3` failure of the universal Fibonacci determinant law, and the
causal-prefix versus cyclic comparison in CSF-04. A bridge to the real
BBP target must additionally discriminate the authenticated zero seed
from same-forcing seeds which agree at any chosen finite 2-/3-adic
precision while shadowing a real locked orbit for a prescribed finite
horizon.
