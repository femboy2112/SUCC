# The twisted arithmetic cylinder and the prime commutator

This responds to the follow-up proposal: extrude a circle, twist the composite
phases until they cancel, and traverse with a back-and-forth operator.
The construction below makes each operation explicit. These are elementary
written proofs and exact finite implementations, with no priority, physical
realization, quantum speedup, or Goldbach claim.

## 1. A winding that cancels every composite

The first choice is the proper-factor energy from `THEOREMS.md`:
`D e_n=(tau(n)-2)e_n` on labels n>=2. For an angle theta define

```math
U_\theta=e^{i\theta D},\qquad
U_\theta e_n=e^{i\theta(\tau(n)-2)}e_n.
```

Picture one circle at each integer height n. Primes have winding zero;
composites have a positive integer winding. Character orthogonality gives

```math
P_{\mathbb P}=\frac1{2\pi}\int_0^{2\pi}U_\theta\,d\theta.
```

The integral is defined strongly, vector by vector. U_theta is a strongly
continuous unitary group; D is not asserted to be bounded. A prime component
contributes its unchanged amplitude; every composite component integrates to
zero. This is a **coherent amplitude average**. Randomizing phases and averaging
density matrices is a different operation and does not delete composite
populations.

This gives an exact reading of composite phase cancellation, but a more
structured winding also supplies the literal commutator requested earlier.

## 2. Use multiplicative splitting depth as the twist

For n>=1 let Omega(n) be the number of prime factors counted with multiplicity,
with Omega(1)=0. This standard arithmetic Omega is distinct from SUCC's
lambda-term `Omega_k` hierarchy. It can also be defined without naming prime
generators first:

```math
\Omega(n)=\max\{r:n=a_1\cdots a_r,\ a_i\ge2\},\qquad \Omega(1)=0.
```

Every maximal splitting ends in irreducibles, so the fundamental theorem of
arithmetic identifies this depth with total prime multiplicity. In particular

```math
\Omega(ab)=\Omega(a)+\Omega(b),\quad
\Omega(n)=1\iff n\text{ is prime},\quad
\Omega(n)\le\lfloor\log_2n\rfloor.
```

Work now on `H=ell2(N_{>=1})`, **including the unit vector e_1**. Define the
number operator and ordinary multiplication isometries by

```math
\mathcal N e_n=\Omega(n)e_n,\qquad V_m e_n=e_{mn}.
```

The self-adjoint diagonal operator N has domain
`sum_n Omega(n)^2 |x_n|^2<infinity`. Each V_m preserves that domain:
`Omega(mn)=Omega(m)+Omega(n)` gives the required weighted-square estimate.

**CYL-01 — PROVED LOCAL (prime fixed points of a commutator).**

```math
[\mathcal N,V_m]=\Omega(m)V_m.
```

The identity holds first on the domain of N and extends to a bounded operator
of norm Omega(m). Therefore, for an individual arithmetic multiplier,

```math
[\mathcal N,V_m]=V_m\quad\Longleftrightarrow\quad m\text{ is prime}.
```

**Proof.** Apply both sides to e_n: the difference is
`(Omega(mn)-Omega(n)) e_(mn)=Omega(m)e_(mn)`. The domain estimate above and
the bounded right-hand side justify the extension. QED.

On the algebra `A_+=span_fin{V_m:m>=1}` of finite sums of multiplication
shifts, the map `delta(A)=[N,A]` is a derivation and

```math
\operatorname{Fix}(\delta|_{\mathcal A_+})
=\operatorname{span}_{\rm fin}\{V_p:p\text{ prime}\}.
```

Apply a finite linear relation among V_m to e_1 to see that these shifts are
linearly independent; compare their coefficients in `delta(A)=A`. This is the
precise operator meaning of the prime fixed-point statement. The unit
multiplier is degree zero: `delta(I)=0`, so it is not fixed by delta.

The derivation is not a category endofunctor: it satisfies Leibniz's law,
not `delta(AB)=delta(A)delta(B)`. The genuine fixed-object functor remains
PFO-01. Both are valid, different mathematical constructions.

### Essential restriction on the fixed space

Do not extend “only prime multipliers” to all operators or to an algebra
containing arbitrary adjoints. For example

```math
[\mathcal N,|8\rangle\langle4|]=|8\rangle\langle4|,
```

because Omega(8)-Omega(4)=1, although both endpoint labels are composite.
Even the arithmetic adjoint algebra contains
`[N,V_6 V_2^*]=V_6 V_2^*`: that operator sends even n to 3n and odd n to zero,
and is not a finite sum of prime multiplication shifts. The selected algebra
is part of the theorem, not optional terminology.

## 3. The circle is the Fourier transform of multiplicative degree

Now use the degree twist

```math
W_\theta=e^{i\theta\mathcal N}.
```

Primes occupy the first harmonic, the unit the zeroth, and composites higher
harmonics. Thus

```math
P_{\mathbb P}=\frac1{2\pi}\int_0^{2\pi}e^{-i\theta}W_\theta\,d\theta.
```

The operator version is

```math
W_\theta V_mW_\theta^*=e^{i\theta\Omega(m)}V_m,
```

so the Fourier coefficient of degree 1 of the conjugation action selects
prime **multipliers inside A_+**. On all operators it instead selects every
transition of degree difference 1, including the counterexamples above.

**CYL-02 — PROVED LOCAL (finite clock and its exact scope).** Sampling M
equally spaced angles gives

```math
P_M=\frac1M\sum_{j=0}^{M-1}e^{-2\pi i j/M}W_{2\pi j/M},\qquad
P_M e_n=\mathbf1_{\Omega(n)\equiv1\ (\bmod M)}e_n.
```

On `2<=n<=X`, `M>=max(1,floor(log_2 X))` suffices to identify primes exactly.
If the unit n=1 is also in the observation window, use
`M>=max(2,floor(log_2 X))` so its degree 0 cannot alias degree 1.

**Proof.** The finite geometric sum is 1 when its integer charge difference
is divisible by M, otherwise zero. For n>=2 that difference lies between 0
and `floor(log_2 X)-1`; the stated bound forces its only multiple of M to
be zero. The extra M>=2 condition excludes the unit's difference -1. QED.

Every fixed M fails on the infinite cylinder: the composite `n=2^(M+1)`
has degree M+1 and survives. Thus `||P_M-P||=1` for every positive M.
Nevertheless `P_M -> P` strongly as M tends to infinity, because each fixed
coordinate eventually has no alias and the diagonal operators are uniformly
bounded. This is not operator-norm convergence. By comparison PFO-06's
resolvent has the stronger uniform norm error 2^-r.

An adaptive finite algorithm chooses M from X and is exact on every requested
finite window. Counterexamples beyond a fixed window do not refute that
algorithm. Also, a logarithmic **phase-clock bound** is not a logarithmic
factoring or primality algorithm: preparing the degree phases requires actual
arithmetic source computation.

At the half-turn, `W_pi e_n=(-1)^Omega(n)e_n`, the Liouville sign. A two-phase
observer sees factor-count parity and accepts composite 8, whose degree is 3.
This is a direct illustration of information lost by a parity-only probe, not
a proof that all phase methods overcome the classical sieve parity problem.

The degree twist is an elementary specialization of the known prime-exponent
coordinate system: `n=product p^v_p(n)` corresponds to a monomial in one
variable per prime, and rotating all variables together multiplies it by
`exp(i theta Omega(n))`. A primary account of this Bohr framework is
Hedenmalm–Lindqvist–Seip, [*A Hilbert space of Dirichlet series and systems of
dilated functions in L2(0,1)*](https://arxiv.org/abs/math/9512211), section 2.2.
The circle action is not being claimed as new mathematics.

### A single irrational twist and a literal clockwise/counterclockwise filter

Restrict here to labels n>=2 and set `C=N-I`. This C is the degree-minus-one
operator, not PFO-03's set-valued prime closure. Its charge c=Omega(n)-1 is
zero exactly at primes and otherwise a positive integer. Define

```math
W=\exp(2\pi i\sqrt2\,C).
```

**CYL-09 — PROVED LOCAL (irrational fixed sector and Fejér bound).** The
fixed space of W is precisely the prime subspace. For integer K>=1, the
positive bidirectional filter

```math
\mathcal B_K=
\left(\frac1K\sum_{j=0}^{K-1}W^j\right)^*
\left(\frac1K\sum_{j=0}^{K-1}W^j\right)
=\sum_{r=-(K-1)}^{K-1}\frac{K-|r|}{K^2}W^r
```

fixes primes and satisfies, on 2<=n<=X with integer X>=2,

```math
\|\mathcal B_K-P\|_{n\le X}
\le\min\left(1,\frac{4(\lfloor\log_2X\rfloor-1)^2}{K^2}\right).
```

**Proof.** A nonzero integer c cannot have c sqrt(2) integral, so no composite
has eigenvalue 1 for W. To bound its finite Fejér weight, let m be a nearest
integer to c sqrt(2). Then `|2c^2-m^2|>=1` and `m<=2c`, whence

```math
\|c\sqrt2\|=\frac{|2c^2-m^2|}{c\sqrt2+m}>\frac1{4c}.
```

The geometric sum and `|sin(pi x)|>=2||x||` give

```math
\left|\frac1K\sum_{j=0}^{K-1}e^{2\pi i j c\sqrt2}\right|^2
\le\min\left(1,\frac{1}{4K^2\|c\sqrt2\|^2}\right)
\le\min(1,4c^2/K^2).
```

Use `c<=floor(log_2X)-1`. Counting differences j-k gives the displayed
bidirectional coefficients. QED.

This supplies a fixed finite formula whose exact fixed sector has no composite
aliases, plus an explicit approximation budget. For X=10000 and K=256 the
proved error upper bound is `9/1024`. The code records this rational **analytic
bound**, not a floating-point measurement of irrational phases.

The filters converge strongly to P. Their global operator-norm error is still
1 at every finite K: irrational rotations have arbitrarily small nonzero
returns by the elementary pigeonhole principle, every positive integer charge
c occurs at n=2^(c+1), and the corresponding Fejér weights approach 1. This
does not weaken the exact finite-window bound or the adaptive observer.

The symbol B_K here is a filter; it is different from the factorization map B
in PFO-05. Clockwise/counterclockwise powers W^r are also different from the
arithmetic hops considered next. Mixing these operations without specifying
their order would lose the meaning of the construction.

## 4. Which back-and-forth motion is intended?

### Additive motion along the cylinder

Let `S e_n=e_(n+1)` with the unilateral adjoint. For step h>=1 set

```math
K_h=S^h+(S^*)^h.
```

This is a bounded self-adjoint back-and-forth operator. Conjugating it by W
adds the exact edge phase

```math
W_\theta S^hW_\theta^*e_n
=e^{i\theta(\Omega(n+h)-\Omega(n))}e_{n+h}.
```

**CYL-03 — PROVED LOCAL (twisting alone changes no connectivity).** The
phase is a gauge difference. Along a path its factors telescope to the phase
of the endpoints; products around loops have phase 1. In particular

```math
(W_\theta K_hW_\theta^*)^t=W_\theta K_h^tW_\theta^*
```

for nonnegative integers t. Prime-to-prime matrix elements are unchanged,
since both endpoints have degree 1. Such pure conjugation changes no transition
probability or graph edge support.

Averaging conjugations also does **not** select primes:

```math
\frac1{2\pi}\int W_\theta K_hW_\theta^*\,d\theta
```

keeps edges between any equal-degree labels. It retains 14--15 at h=1 and
33--35 at h=2, all composite. Coherent state filtering and conjugation
averaging must not be interchanged.

If one instead compresses to `P K_h P`, only prime endpoints remain. For h=1
the sole edge is 2--3. For h=2 the edges are twin-prime pairs.

**CYL-04 — PROVED LOCAL (bounded-range prime-only walks cannot enumerate
all primes).** Any graph on prime labels whose edges have integer length at
most a fixed H has only finite connected components.

**Proof.** Choose arbitrarily large integers M>H+1. The consecutive labels
`M!+2,...,M!+M` are all composite and form a block longer than H. No edge of
length <=H connects prime labels on opposite sides. Such barriers occur
arbitrarily far out, so every component is bounded above and hence finite.
QED.

This does not refute a finite program with increasing jump lengths, nor an
observer that traverses composite labels and only reports prime hits. PFO-04's
productive observer uses the latter strategy.

There is an exact path-filter version on a finite window of labels >=2.
For any matrix K, initial prime projection P, and integer t>=1,

```math
\frac1{2\pi}\int e^{-it\theta}(W_\theta K)^tP\,d\theta=(PKP)^t.
```

Expand into paths: every visited label has degree >=1, so total degree t
forces all t destinations to have degree 1. This filters out every path with
a composite visit and inherits the bounded-range obstruction above. The
unit must be absent for this minimum-degree argument.

### An arithmetic distinction between multiplicative and additive shear

**CYL-05 — PROVED LOCAL (unbounded additive generator shear).** Although each
`[N,V_m]` extends boundedly, `[N,S]` on the finite-support core has no bounded
extension.

**Proof.** At `n=2^k-1`, k>=2, n is odd, so every one of its prime factors is
at least 3. Therefore `3^Omega(n)<=n<2^k`, while `Omega(n+1)=k`. The
coefficient in

```math
[\mathcal N,S]e_n=(\Omega(n+1)-\Omega(n))e_{n+1}
```

is greater than `(1-log_3 2)k`, which tends to infinity. QED.

The finite-support core is the declared commutator domain here. A bounded
S need not preserve the entire domain of N. The finite-angle conjugate
`W_theta S W_theta^*` is still a bounded operator of norm 1; an unbounded
infinitesimal commutator does not contradict that fact. This result describes
a real difference in the cylinder's two arithmetic motions, without implying
either a computational impossibility or a prime-pair theorem.

## 5. Multiplicative wiggles need their intermediate states

Here the underlying Hilbert space is again `ell2(N_{>=1})`, with its unit
vacuum e_1 retained. For a prime p use the bounded self-adjoint operator

```math
K_p=V_p+V_p^*.
```

Multiplication adds one prime factor; its adjoint removes p when present.
Thus K_p changes degree by +1 or -1. From a prime state, one step reaches a
semiprime or the unit, never another prime:

```math
P K_p P=0.
```

**CYL-06 — PROVED LOCAL (two-step prime transfer).** For distinct primes p,q,

```math
P K_p K_q P=|p\rangle\langle q|+|q\rangle\langle p|,
\qquad P V_p V_q^* P=|p\rangle\langle q|.
```

**Proof.** An initial prime r can survive the two-step compression only as
follows. If r=q, removing q reaches 1 and multiplying by p reaches p. If
r=p, multiplying by q reaches pq and removing p reaches q. All other terms
end at composite labels or zero. For the matrix unit, only the first route
is allowed. QED.

For p=q the first formula changes: `P K_p^2 P=P+|p><p|`.
The vacuum is necessary for the stated matrix unit. If the Hilbert space were
restricted to labels >=2 and V_q* truncated there, it would lose `q -> 1`
and the matrix-unit formula would fail.

The two equal transport words for distinct primes expose both intermediate
routes from q to p:

```text
q -> 1 -> p          (divide by q, then multiply by p)
q -> pq -> p         (multiply by p, then divide by q)
```

For p=3,q=5 the intermediate labels are 1 and 15. Because p and q are
coprime, `V_p V_q^*=V_q^*V_p`; the two words agree as operators. This is a
certified equivalence between computational paths. Adding two copies of the
same map doubles its amplitude unless normalization is specified; it does not
create two distinct arithmetic witnesses or a physical two-slit experiment.
The unmodified K_p and K_q also commute for distinct primes. Their product
is not a noncommutative loop phase.

Projecting after **each** individual step gives `P K_p P K_q P=0`. Projecting
only after both steps retains the transfer above. Thus canceling all composite
and unit intermediates too early destroys the useful transport. One can filter
the output without demanding that every internal state already be prime.

### Insert the twist between the two kicks

**CYL-08 — PROVED LOCAL (operational phase transport).** For distinct primes
p,q on the ambient space including e_1,

```math
P K_p W_\theta K_q P
=|p\rangle\langle q|+e^{2i\theta}|q\rangle\langle p|.
```

The q-to-p route passes through degree-zero vacuum 1; the p-to-q route
passes through degree-two semiprime pq. This proves the formula directly.
After an explicit common phase rotation, the resulting two-dimensional block is

```math
\mathcal W_{p,q}(\theta)
=e^{-i\theta}P K_p W_\theta K_qP
=e^{-i\theta}|p\rangle\langle q|+e^{i\theta}|q\rangle\langle p|
=\cos\theta\,\sigma_x+\sin\theta\,\sigma_y.
```

Here the ordered basis is (e_p,e_q), with the usual Pauli matrices. Its square
is the projection onto that two-dimensional block; its two nonzero eigenvalues
are +1 and -1. Reversing the kick order changes theta to -theta. Different
interposed phases give an actual noncommuting family on the block:

```math
[\mathcal W(\theta),\mathcal W(\phi)]
=2i\sin(\phi-\theta)(|p\rangle\langle p|-|q\rangle\langle q|).
```

This phase has a declared source, orientation, and transport. It was inserted
between operations; it is not inferred from verbal similarity to interference.
Coherently averaging the unrotated expression over theta removes the
semiprime route and leaves `|p><q|`, while reversing kick order leaves
`|q><p|`. This gives an exact controlled version of “cancel composite phases
and wiggle.” It provides transfer between already specified prime labels; it
does not certify that some such pair has a prescribed sum.

## 6. The Goldbach cylinder needs the right orientation and sector

For N>=4, restrict pair labels to `2<=k<=N-2`; both inputs are nonunits.
Their degrees are at least 1. Same-orientation twisting gives

```math
R(N)=\frac1{2\pi}\int_0^{2\pi}e^{-2i\theta}
\sum_{k=2}^{N-2}e^{i\theta(\Omega(k)+\Omega(N-k))}\,d\theta.
```

**CYL-07 — PROVED LOCAL (exact degree-2 pair filter).** Total degree 2 on
this nonunit pair sector is equivalent to both labels being prime. If N is
even, these are its ordered Goldbach representations.

An opposite twist uses `Omega(k)-Omega(N-k)` and admits equal-degree
composites: 4+4=8 and 33+35=68 are explicit false survivors. Allowing the
unit with a same-orientation degree-2 filter also fails: 1+9=10 has degrees
0+2. These are calibration controls, not prime pairs.

For even N=2n the bound

```math
2\le\Omega(k)+\Omega(N-k)=\Omega(k(N-k))
\le\lfloor\log_2(n^2)\rfloor
```

gives an exact finite phase clock whenever

```math
M>\lfloor\log_2(n^2)\rfloor-2.
```

Taking `M=max(1,floor(log_2(n^2))-1)` suffices. The implementation evaluates
integer bit lengths, avoiding floating-point logarithmic boundary errors.
At N=2048 a 19-phase clock suffices for the finite sector. The existence of
this clock says how accurately the pair count can be **observed**, not why it
must be positive for every N.

The preceding prime-transfer matrix units also assemble the reflection map:

```math
A_N=P_N\left(\sum_{\substack{a+b=N\\a,b\ge2}}V_aV_b^*\right)P_N.
```

Applied to a prime q, V_b* can survive only for b=q; final compression
requires a to be prime, and the remaining condition is a+q=N. This recovers
PFO-09's `P_N J_N P_N`, its +1/-1 Haar blocks, and the same unresolved
nonempty-fiber condition. Multiplicative transport among arbitrary primes is
unconditional; selecting a pair with a prescribed ordinary sum is the
additional arithmetic requirement.

In this formula V_a and V_b* act on the **ambient** space including e_1;
only the outer P_N restricts the finite nonunit prime window. Truncating the
adjoint before its vacuum step would incorrectly erase the entire map.

**CYL-10 — PROVED LOCAL, exact finite control (full single-cylinder spectrum
is insufficient).** For the transported multiplication in PFO-13, the ordinary
and transported Omega charge histograms on labels 2,...,98 agree exactly:

| Charge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Multiplicity, both sources | 25 | 34 | 21 | 11 | 4 | 2 |

The involution permutes the entire window, so it preserves the spectrum of
every one-register function of the number operator. Consequently all trace
characters, all moments, and every other spectral trace on that one cylinder
agree. But the degree-2 coefficient of the sum-100 two-register operator is
12 for ordinary multiplication and 0 for transported multiplication. The
missing information is the joint embedding into ordinary addition, rather
than higher precision in the single-register spectrum.

## 7. What the new geometry has earned

The circle has a precise winding source, the prime sector is an exact Fourier
coefficient, prime multiplication arrows are fixed by a specified commutator
derivation, and the observer can use adaptive finite phase clocks. We have
also proved a bounded-range traversal obstruction and an unbounded additive
generator shear, and exhibited a two-step transport through nonprime states.

The next proof task remains source-dependent additive correlation. A pure
gauge twist cannot create it; eliminating every nonprime intermediate destroys
some useful paths. The promising mathematical question is whether controlled
intermediate sectors, while retaining the authentic SUCC/FUCC additive braid,
yield a bound for the sum-constrained overlap. An unspecified positive
degree-2 coefficient for every even N is exactly Goldbach, not an independent
lemma already supplied by the cylinder.
