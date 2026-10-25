# Euler–Mascheroni and the two clocks of a selected arithmetic character

**Date:** 2026-10-24. **Authority:** classical Tauberian inputs, explicit paper
proofs, exact finite arithmetic, and separately identified rational interval
certificates. **π normality and RH remain OPEN.** No new Lean authority or
claim of scholarly priority is asserted.

The user's identity

$$
\gamma=\lim_{r\downarrow1}\sum_{n\geq1}\left(n^{-r}-r^{-n}\right)
$$

compares two different clocks on the positive integers. Its constant mode is
exactly controlled by $\zeta(r)-1/(r-1)$. A nonconstant character requires its
own estimate. This note makes that distinction quantitative and gives a
precise route from harmonic **time windows** of the authentic BBP source to
ordinary π equidistribution.

The strongest new interface here is a proved source-transfer bound. The
two-dilation criterion that it transports is an **equivalent reformulation**
of ordinary cancellation. The selected source estimate itself is unproved.

## 1. Scope: time windows, lag weights, and spatial multiplication

Three different operations must remain separate.

| Operation | Variable being changed | Status used here |
|---|---|---|
| Harmonic time window $\sum_{N<n\leq pN}a_n/n$ | The integer observation time $n$ | Main object of this note |
| Harmonic Fejér mixture from [PR #284](https://github.com/femboy2112/SUCC/pull/284) | The block length and lag in a van der Corput/Gram estimate | Separate inspected research; no estimate from it is assumed here |
| Circle maps $x\mapsto2x$ or $x\mapsto3x$ modulo one | The observed circle state | No extra invariance under these maps is assumed or proved |

In particular, using the time dilations $N\mapsto2N$ and $N\mapsto3N$ below
does not establish Furstenberg $\times2/\times3$ invariance, identify a spatial
prime-local observer, or close the repository's selected tripling-invariance
gap. The only circle recurrence used for π is the original base-16 source.

## 2. Gamma's two normalized clocks become asymptotically disjoint

For $\varepsilon>0$, define probability measures on $\mathbb N_{\geq1}$ by

$$
p_\varepsilon(n)=\frac{n^{-1-\varepsilon}}{\zeta(1+\varepsilon)},
\qquad
q_\varepsilon(n)=\varepsilon(1+\varepsilon)^{-n}.
$$

The geometric mass is exactly one. The unnormalized Dirichlet mass satisfies

$$
\varepsilon\zeta(1+\varepsilon)
=1+\gamma\varepsilon+O(\varepsilon^2).
$$

### Proposition 1: total variation separation

With total variation normalized to lie in $[0,1]$,

$$
\lim_{\varepsilon\downarrow0}
\|p_\varepsilon-q_\varepsilon\|_{\mathrm{TV}}=1.
$$

**Proof.** Put $M_\varepsilon=\lceil\varepsilon^{-2}\rceil$. The integral
comparison gives $\zeta(1+\varepsilon)\geq1/\varepsilon$, so

$$
p_\varepsilon([1,M])
\leq\varepsilon H_M
\leq\varepsilon(1+\log M).
$$

On the same event,

$$
q_\varepsilon([1,M])=1-(1+\varepsilon)^{-M}.
$$

At $M=M_\varepsilon$, these quantities tend respectively to zero and one.
Their difference is a lower bound on total variation; its upper bound is
one. This proves the claim. $\square$

The exact finite implementation already certifies a lower bound greater than
$4/5$ at $\varepsilon=1/64$, $M=4096$. This is a finite instance of the proved
bound, not a numerical approximation to a zeta value.

The Dirichlet clock has $\log n$ of order $1/\varepsilon$, while the geometric
clock has $n$ of order $1/\varepsilon$. Cancellation of their total masses
therefore cannot justify identifying their averages of an arbitrary selected
arithmetic character. The constant $\gamma$ controls the constant character;
each nonconstant character retains a separate obligation.

## 3. A regular germ at one does not control the entire boundary

### Proposition 2: an explicit off-axis obstruction

Fix a real $t\ne0$ and set $a_n=n^{it}$. Then $|a_n|=1$ and

$$
D_a(s)=\sum_{n\geq1}a_n n^{-s}=\zeta(s-it),
\qquad \Re s>1.
$$

This function is holomorphic in a neighborhood of $s=1$. Its value there is
finite, and $(s-1)D_a(s)\to0$ along the real approach. Nevertheless,

$$
\frac1N\sum_{n\leq N}a_n
=\frac{N^{it}}{1+it}+O_t\!\left(\frac{\log N}{N}\right),
$$

which does not tend to zero. To verify the error, compare the sum with
$\int_1^N x^{it}\,dx$ and bound the accumulated derivative variation by
$|t|\log N$, together with endpoint terms. The pole at $s=1+it$ carries the
oscillation missed by the germ at one.

Even positivity of the coefficients does not repair this local condition.
The bounded nonnegative sequence $1+\Re(n^{it})$ has Dirichlet series

$$
\zeta(s)+\frac{\zeta(s-it)+\zeta(s+it)}2.
$$

Subtracting $1/(s-1)$ leaves a holomorphic germ at one, while its ordinary
means still oscillate.

These are explicitly **changed-source controls**. They do not satisfy the
original BBP law and are not counterexamples to π normality. They refute the
generic inference that a finite regularized value, a regular germ at one,
or a real-axis Dirichlet residue determines ordinary occupation statistics.

There is also a control preserving the exact base-shift dynamics. Start with
any base-16 normal digit string and overwrite positions
$[N_j,2N_j)$, where $N_j=2^{2^j}$, with zeros. The overwritten positions,
including any fixed finite enlargement, have logarithmic density zero: each
block contributes bounded harmonic mass, and the number of blocks through
$N$ is $O(\log\log N)$. Thus all fixed blocks retain their logarithmic
frequencies. At each endpoint $2N_j$, however, approximately half of the
digits are zero, so ordinary normality fails. This changes the arithmetic
source while preserving the base-16 shift law. Even all logarithmic block
frequencies therefore need an additional bridge to ordinary frequencies.

## 4. Two harmonic time dilations characterize ordinary cancellation

Let $(a_n)$ be any bounded complex sequence, with $|a_n|\leq M$. Define

$$
A(x)=\sum_{1\leq n\leq x}a_n,
\qquad
H_a(x)=\sum_{1\leq n\leq x}\frac{a_n}{n},
$$

and, for $x>0$ and $\lambda>0$, the oriented window

$$
B_\lambda(x)=H_a(\lambda x)-H_a(x).
$$

Convergence of $H_a(N)$ is a sufficient condition for $A(N)/N\to0$ by
partial summation, also known as Kronecker's lemma in this form. It is stronger
than necessary. For example, $a_n=1/\log(n+1)$ has ordinary mean zero, but
$H_a(N)$ diverges. Harmonic increments avoid that unnecessary demand for a
convergent finite part.

### Theorem 3: two independent time scales

For a bounded complex sequence, the following are equivalent:

1. $A(N)/N\to0$ as $N\to\infty$.
2. $B_2(N)\to0$ and $B_3(N)\to0$ as $N\to\infty$.

More generally, any integers $p,q>1$ with $\log p/\log q$ irrational can
replace $2,3$.

**Proof of 1 ⇒ 2.** Partial summation yields, for fixed $p>1$,

$$
B_p(N)=\frac{A(pN)}{pN}-\frac{A(N)}N
       +\int_N^{pN}\frac{A(x)}{x^2}\,dx.
$$

Every term tends to zero when $A(x)=o(x)$.

**Proof of 2 ⇒ 1.** Moving an integer starting point by less than one changes
$B_p$ by $O_p(M/x)$, so the hypotheses hold for real starting points as well.
The definitions give the exact cocycle and inverse laws

$$
B_{\lambda\mu}(x)=B_\lambda(x)+B_\mu(\lambda x),
\qquad
B_{1/\lambda}(x)=-B_\lambda(x/\lambda).
$$

Consequently $B_g(x)\to0$ for every fixed $g=2^u3^v$, with $u,v\in\mathbb Z$.
The multiplicative group $2^{\mathbb Z}3^{\mathbb Z}$ is dense in
$\mathbb R_{>0}$. Indeed, rational dependence of $\log2$ and $\log3$ would
give $2^u=3^v$ with nonzero integer exponents, contradicting unique
factorization; irrational rotations then give the asserted density.

For any fixed $\lambda,g>0$, a harmonic-sum bound gives

$$
|B_\lambda(x)-B_g(x)|
\leq M|\log(\lambda/g)|+O_{\lambda,g}(M/x).
$$

Approximate $\lambda$ by a fixed element $g$ of the dense group, first let
$x\to\infty$, and then let $g\to\lambda$. It follows that
$B_\lambda(x)\to0$ for every fixed positive $\lambda$.

There is an exact integral identity

$$
\frac{A(N)}N
=\int_0^1\bigl[H_a(N)-H_a(Nt)\bigr]\,dt.
$$

It follows directly by integrating each finite step-function contribution:
$a_n/n$ is included in the integrand for $0\leq t<n/N$, with integral
$a_n/N$. For each fixed $t>0$, the integrand tends to zero by the
all-dilation result. Its modulus is at most $M(1+|\log t|)$, an integrable
majorant, including the small interval where $Nt<1$. Dominated convergence
completes the proof. $\square$

**Novelty tax.** This is an exact Tauberian reformulation, with a
self-contained proof. It reduces the family of time dilations to two and is
strictly weaker than convergence of a full harmonic finite part. It is
equivalent to the original ordinary-mean conclusion. No proof credit for
selected BBP cancellation follows merely from restating it in this form.

### Proposition 4: a single time scale fails

Define a right-continuous function by

$$
a(x)=
\begin{cases}
1,&2^k\leq x<\sqrt2\,2^k,\\
-1,&\sqrt2\,2^k\leq x<2^{k+1},
\end{cases}
\qquad k\in\mathbb Z,
$$

and set $a_n=a(n)$ for positive integers. This is a bounded, log-periodic
changed-source control. The continuum harmonic integral over every
$[x,2x]$ is zero, since its two signed halves have equal logarithmic length.

For integer $N\geq1$, comparison with the right-endpoint Riemann sum gives

$$
|B_2(N)|\leq\frac5N.
$$

For completeness, on $[N,2N]$ the function $a(x)/x$ has at most two jumps in
$(N,2N]$, **including a possible jump at the upper endpoint**. The lower
endpoint uses its right-continuous value and adds no separate jump. Each
jump has size at most $2/N$, and the smooth variation is at most $1/(2N)$.
Total variation therefore bounds the unit-mesh Riemann error by less than
$5/N$.

On the other hand, the signed count on each dyadic block is
$(2\sqrt2-3)2^k+O(1)$. Hence

$$
\frac{A(2^m-1)}{2^m-1}\longrightarrow2\sqrt2-3\ne0.
$$

Tripling detects the same control:

$$
B_3(2^m)\longrightarrow\log(4/3)>0.
$$

The interval $[1,2]$ contributes zero to the limiting integral, and the
remaining positive and negative portions of $[2,3]$ give $\log(4/3)$.
The finite implementation decides the signs by integer-square comparisons
and obtains cumulative counts from an independent integer-square-root block
oracle. No floating-point comparison with $\sqrt2$ is used.

## 5. Authentic BBP source transport has an explicit vanishing cost

Retain the original four-pole forcing and zero initial state:

$$
r(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2},
\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
$$

The original BBP identity gives

$$
U_n=16^{n-1}\pi-T_n,
\qquad
T_n=\sum_{j\geq1}16^{-j}r(n+j).
$$

The unwrapped $U_n$ may be replaced by its rational circle residue when
evaluating an **integer** character. No independent prime-local source
choices or altered initial conditions are permitted.

### Lemma 5: a source-only tail bound

Put $g(t)=2(1-t^3)+(1-t^4)+(1-t^5)$. Summing the original geometric tail
inside its positive integral gives

$$
T_n=\int_0^1 t^{8n}\frac{g(t)}{16-t^8}\,dt.
$$

For $0\leq t<1$,

$$
\frac{g(t)}{1-t}=4+4t+4t^2+2t^3+t^4<15\leq16-t^8.
$$

Therefore, for every integer $n\geq1$,

$$
0<T_n<\int_0^1t^{8n}(1-t)\,dt
=\frac1{(8n+1)(8n+2)}<\frac1{64n^2}.
$$

### Proposition 6: character and harmonic-window transport

Fix an integer $h$. Define

$$
z_h(n)=e^{2\pi i hU_n},
\qquad
v_h(n)=e^{2\pi i h16^{n-1}\pi},
\qquad C_h=\frac{11|h|}{112}.
$$

The elementary character Lipschitz bound and $2\pi<44/7$ imply

$$
|z_h(n)-v_h(n)|\leq\frac{C_h}{n^2}.
$$

For integers $p\geq2$ and $N\geq1$, it follows that

$$
\left|\sum_{N<n\leq pN}\frac{z_h(n)-v_h(n)}n\right|
\leq C_h\sum_{N<n\leq pN}n^{-3}
\leq\frac{C_h(1-p^{-2})}{2N^2}.
$$

In particular, the bounds for $p=2$ and $p=3$ are respectively

$$
\frac{33|h|}{896N^2},
\qquad
\frac{11|h|}{252N^2}.
$$

The implementation also provides the tighter finite rational bound obtained
by summing the original tail envelope. For $h=0$, the character difference
is exactly zero; asymptotic assertions below concern fixed nonzero integers.

### Corollary 7: exact selected-source criterion

π is normal in base 16 if and only if, for **every fixed integer** $h\ne0$,
both source-selected limits vanish:

$$
\sum_{N<n\leq2N}\frac{e^{2\pi i hU_n}}n\longrightarrow0,
\qquad
\sum_{N<n\leq3N}\frac{e^{2\pi i hU_n}}n\longrightarrow0.
$$

Theorem 3 converts these windows into ordinary Fourier cancellation;
Proposition 6 transfers them to the π orbit; the classical Weyl criterion
and the base-shift characterization of normality finish the equivalence.
Every bridge is explicit, but **the displayed selected-source limits remain
unproved**. A growing frequency $h=h_N$ is not covered by the fixed-frequency
quantifier. No base-10 or absolute normality statement follows here.

## 6. A holomorphic correction preserves the genuine boundary question

For $\Re s>1$, define

$$
D_h^U(s)=\sum_{n\geq1}z_h(n)n^{-s},
\qquad
D_h^\pi(s)=\sum_{n\geq1}v_h(n)n^{-s}.
$$

### Proposition 8: continuation of the difference

The difference $E_h(s)=D_h^U(s)-D_h^\pi(s)$ extends holomorphically to
$\Re s>-1$. For $\sigma=\Re s>-1$,

$$
|E_h(s)|\leq C_h\zeta(\sigma+2),
$$

and for integer $M\geq1$,

$$
\left|\sum_{n>M}(z_h(n)-v_h(n))n^{-s}\right|
\leq\frac{C_h M^{-\sigma-1}}{\sigma+1}.
$$

**Proof.** Proposition 6 bounds each summand by $C_hn^{-\sigma-2}$.
Absolute locally uniform convergence gives holomorphy, and the integral
test gives the tail. Inserting any fixed power of $\log n$ gives the same
locally uniform convergence for derivatives. $\square$

Thus the authentic rational source and the π orbit have the same possible
boundary singularities on $\Re s=1$, up to an explicitly controlled
holomorphic correction. This does not establish that those singularities
are absent. The rational code specializes the tail formula to nonnegative
integer $\sigma$; the paper theorem has the larger stated domain.

## 7. The boundary Tauberian route and its unpaid premise

The classical Wiener–Ikehara theorem supplies a sufficient analytic target:
if every fixed nonzero-integer source series $D_h^U(s)$ extends continuously
to the **entire boundary line** $\Re s=1$, locally on every finite interval,
then π is base-16 normal.

To check the hypotheses, use the bounded nonnegative coefficient sequences
$1+\Re z_h(n)$ and $1+\Im z_h(n)$. Their analytic Dirichlet series are

$$
\zeta(s)+\frac{D_h^U(s)+D_{-h}^U(s)}2,
\qquad
\zeta(s)+\frac{D_h^U(s)-D_{-h}^U(s)}{2i}.
$$

Subtracting $1/(s-1)$ leaves the known regularized zeta function plus the
assumed continuous character boundary data. Wiener–Ikehara gives ordinary
mean one for both nonnegative sequences, and therefore mean zero for the
real and imaginary parts of $z_h$. Proposition 6 and Weyl complete the
implication.

The local pseudofunction version is weaker and gives a necessary-and-
sufficient boundary condition for the desired asymptotic. It must therefore
be labeled another reformulation. Continuous extension is stronger than
ordinary normality and could serve as a sufficient analytic target, but no
such extension for the selected BBP character series is proved here. A germ
only at $s=1$ is insufficient by Proposition 2.

For bounded sequences, geometric Abel means do determine the ordinary
Cesàro mean: apply the Hardy–Littlewood theorem after shifting real and
imaginary parts to nonnegative coefficients. Real-axis Dirichlet residues
instead can conceal logarithmic oscillations. Consequently a
character-weighted counterpart of the user's difference,

$$
\sum_{n\geq1}z_h(n)
\left[n^{-1-\varepsilon}-(1+\varepsilon)^{-n}\right],
$$

requires its own transfer estimate. The scalar identity for $\gamma$ supplies
that estimate only for the constant coefficient sequence.

## 8. Four finite certificates for the actual source

The following enclosures concern exactly

$$
B_p(N)=\sum_{N<n\leq pN}\frac{e^{2\pi iU_n}}n.
$$

All endpoints below are exact rational decimals, rounded outward. The
source states are exact fractions from the original zero-initial four-pole
recurrence. The inherited `pi_source_genesis.character_interval` uses
rational Machin bounds for π, Taylor remainder bounds, and outward dyadic
rounding.

| $N$ | $p$ | Certified interval for $|B_p(N)|$ |
|---:|---:|---|
| 32 | 2 | $[0.035688976370,\ 0.035688976371]$ |
| 32 | 3 | $[0.090656713295,\ 0.090656713296]$ |
| 128 | 2 | $[0.065276411366,\ 0.065276411367]$ |
| 128 | 3 | $[0.061958856714,\ 0.061958856715]$ |

Disjoint squared-modulus intervals certify

$$
|B_2(128)|>|B_2(32)|.
$$

This is a rigorous rejection of monotone decrease across those two actual
source windows. It neither refutes eventual cancellation nor supplies an
asymptotic rate. The interval instrument passes exact zero-, quarter-, and
half-turn controls. The complete receipt records the phase enclosure
parameters and source fingerprints.

Reproduction and validation:

- [Combined executable probe](../../scripts/euler_mascheroni_probe.py).
- [Machine-readable probe receipt](euler_mascheroni_validation/probe_receipt.json).
- [Exact character/clock interface](../../observational_succ/gamma_character_bridge.py).
- [Focused tests](../../tests/test_gamma_character_bridge.py).

Seven focused test methods were executed successfully for this interface.
They include the original-source cross-check, a rejected factor-two tail
mutation, exact clock separation, signed dilation-cocycle identities,
positive/null/invalid-input controls, and the one-scale counterfeit. The
counterfeit was also checked at finite horizons through $2^{80}-1$ using
integer block counts. Those finite checks calibrate the implementations;
the universal statements above derive from their paper proofs. Broader
repository validation and hosted CI have separate authority and receipts.

## 9. Claims and remaining dependency

| Claim | Status and boundary |
|---|---|
| Gamma's normalized Dirichlet and geometric clocks have total variation tending to one | PROVED PAPER; exact finite lower-bound controls |
| A regular germ at one need not give ordinary cancellation | REFUTED INFERENCE; explicit $n^{it}$ countermodel |
| Harmonic time windows at 2 and 3 characterize bounded ordinary-mean cancellation | PROVED PAPER, CLASSICAL TAUBERIAN REFORMULATION |
| One time scale alone suffices | REFUTED INFERENCE; exact log-periodic control |
| Original BBP windows transport to π with the displayed $O_h(N^{-2})$ cost | PROVED PAPER; source constants checked by exact arithmetic |
| The source/π Dirichlet-series difference is holomorphic on $\Re s>-1$ | PROVED PAPER; certified truncation formula |
| The four displayed finite character magnitudes | RATIONAL INTERVAL CERTIFICATES, exactly scoped |
| Actual selected windows vanish for every fixed $h\ne0$ | UNVERIFIED; the remaining normality-equivalent estimate |
| π normality, RH, or a bridge from a positive gamma kernel to signed Weil positivity | OPEN; no closure supplied |

The next useful proof must exploit the original four-pole source to bound
the selected harmonic increments or the full character boundary. Another
constant-mode identity, generic positive kernel, or unchanged finite list
of gamma jets does not establish that missing estimate.

## Primary references and classical inputs

1. Jacob Korevaar, *Ikehara-type theorem involving boundedness* (2008),
   [arXiv:0807.0537](https://arxiv.org/abs/0807.0537), especially Theorem 1.1
   and the following discussion of local pseudofunction boundary behavior.
   This supplies the continuous-boundary sufficiency and identifies the
   exact two-way boundary formulation; the paper was inspected directly.
2. Christopher J. Bishop, Eugene A. Feinberg, and Junyu Zhang, *Examples
   concerning Abel and Cesàro limits*,
   [author-hosted paper](https://www.math.stonybrook.edu/~bishop/papers/BFZRevision1.pdf),
   introduction equations (1)–(2). This supplies the bounded-sequence
   geometric Abel/Cesàro distinction and counterexample context; the paper
   was inspected directly.
3. The original BBP formula, character Lipschitz bound, Weyl criterion,
   partial summation, density of irrational rotations, and dominated
   convergence are classical inputs. The authentic forcing and its
   source-only tail are rederived above and cross-checked against the
   repository's existing source implementation. No academic novelty claim
   is made for the Tauberian ingredients or the two-dilation consequence.
