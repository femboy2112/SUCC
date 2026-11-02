# OPERATION UNIT–UNIT SUCC DIFFERENTIAL — source-complete higher Newton jets and a dyadic reconstruction arrow

**Date 2026-11-02. Research status: scoped paper proofs, not a normality proof.**
Exact parent: SUCC draft PR #462 head 25700292b854f4c3a12b505f321b6c1294c96c7d; inherited #459/460 and merged Main XIX. Read-only predecessor #440 (original BBP Hausdorff moment and Pascal unit jets); #421 (positive zero-seeded changed-source coherent tail); 2026-10-11 FINITE_DIFFERENCE_SUCC_INTEGRATION.md (Newton/Pascal and covariant finite difference). This file DOES NOT re-claim those results as new. Original source, zero-seed, main/production/proof registries are untouched.

## 0. Definitions: two unit successors, one true source and one explicit shadow

Let (E a)_n=a_(n+1), Delta=E-I, and for integers d>=0 define
\[
\Delta^d a_n=\sum_{j=0}^d(-1)^{d-j}\binom dj a_{n+j}.
\]
The **authentic** exact rational BBP source (no mutant) is
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
Its real completed boundary is \(\alpha=\sum_{j>=1}16^{-j}r(j)=\pi/16\).
Write
\[
T_n=\sum_{j>=1}16^{-j}r(n+j),\quad U_n=16^n\alpha-T_n,
\]
the **finite** rational tail
\[
d_n=\sum_{j=1}^{n+1}16^{-j}r(n+j),
\]
and the explicitly DIFFERENT coherent zero-seeded orbit
\[
q=47/240=r(1)/16,\quad\widetilde U_n=16^nq-d_n,\quad
\widetilde r(n)=r(n)-16^{-n}r(2n)-16^{-n-1}r(2n+1).
\]
The last orbit has a changed forcing. Both sequences are source-labelled. The earlier #421/#462 coherent-shadow and original prime-birth proofs are inherited.

## UU-01. Exact SUCC-differential polynomial calculus and source-selection quotient (PROVED)

For any scalar sequence satisfying E U=16U+r_+ (where r_+(n)=r(n+1)),
\[
\boxed{\Delta^dU_n=15^dU_n+
\sum_{j=0}^{d-1}15^{d-1-j}\Delta^j r(n+1),\ d>=1.}\tag{1}
\]
Proof: Delta U=15U+r_+, and induction by commuting Delta with scalar multiplication.

More generally, every integer polynomial P(E) obeys
\[
\boxed{P(E)U_n=P(16)16^n\alpha-P(E)T_n.}\tag{2}
\]
The evaluation P -> P(16) is a surjective ring homomorphism Z[E] -> Z with kernel (E-16)Z[E]. This is the exact **source/seed selector of the polynomial differential**: (E-16) destroys the homogeneous boundary completely, while Delta^d evaluates to 15^d and retains it. In particular, the covariant BBP difference \(\nabla_{16}=E-16\) satisfies \(\nabla_{16}U_n=r(n+1)\) for EVERY seed, so a \(\nabla_{16}\)-only observation is seed-blind.

For every fixed nonzero P in Z[E]:
- if P(16)=0, then P(E)U_n=-P(E)T_n tends to 0, and its fixed-h real-circle phase tends to 1 (SOURCE ONLY, not normal);
- if P(16)!=0, then P(E)U_n differs by a summable correction from \(P(16)16^{n-1}\pi\); by Wall's classical rational-affine normality preservation theorem, its equidistribution is **equivalent** to base-16 normality of pi.

The second statement is a gate **equivalence**, not a proof. Fixed P is crucial; if P=P_N varies with the horizon, control of its coefficient norms and order is owed separately.

## UU-02. A genuine all-grade original-BBP prime conductor (PROVED PAPER, PNT-AP input)

For every n>=1 and d>=0, every prime
\[
\boxed{2(n+d)<p<8n,\quad p\equiv1\pmod4,\quad p>5}
\]
is born once in U_n with residue \(pU_n\equiv c_p16^{n-j_p}\mod p\), and has no second pole within r(n+1),...,r(n+d). Here \((j_p,c_p)\) is the inherited #459 birth pair: ((p+7)/8,4) for p=1 mod8 and ((p+3)/8,-1) for p=5 mod8.

By (1), p-adic integrality of the source-correction and the fact p does not divide 15 imply
\[
\boxed{v_p(\Delta^dU_n)=-1,\quad
p\Delta^dU_n\equiv c_p16^{n-j_p}15^d\pmod p.}\tag{3}
\]

Invoke classical theta(x;4,1)=x/2+o(x). For every eps>0, uniformly for integers \(0\le d\le(3-\varepsilon)n\),
\[
\boxed{\log\operatorname{den}(\Delta^dU_n)\ge3n-d+o_\varepsilon(n).}\tag{4}
\]
For fixed d this has coefficient 3n+o(n); for growing d<n*3 the specified prime band stays macroscopic. All such statements are about reduced rational denominators, NOT distances of real phases to an integer.

## UU-03. An exact *positive* Hausdorff representation of the FINITE coherent shadow (PROVED)

Original SUCC PR #440 already proves the genuine source is a Hausdorff moment sequence:
\[
r(n)=\int_0^1 x^{n-1}f(x)\,dx,\quad
f(x)=\tfrac18x^{-7/8}P(x^{1/8}),\quad
P(v)=4-2v^3-v^4-v^5>0\ (0<v<1).
\]
Define the authentic future-tail density
\[
\boxed{w(x)=\frac{f(x)}{16-x}
=\frac{x^{-7/8}P(x^{1/8})}{8(16-x)}.}\tag{5}
\]
Then \(T_n=\int_0^1 x^nw(x)\,dx\). The new observation is that the finite rational truncation d_n **also** has a positive Hausdorff measure.

First, an EXACT tail splitting using only index arithmetic:
\[
\boxed{T_n-d_n=16^{-(n+1)}T_{2n+1}.}\tag{6}
\]
Set \((\mathcal Ra)_n=16^{-(n+1)}a_{2n+1}\).
Its action on positive moment measures is the weighted pushforward under
\(\Phi(x)=x^2/16\), with weight \(x/16\).
For \(w(x)\,dx\), the pushforward has density
\(\tfrac12w(4\sqrt y)\mathbf1_{0<y<1/16}\).

Thus \(d=(I-\mathcal R)T\) has **explicit** density
\[
\boxed{
\widetilde w(x)=w(x)-
\frac12\mathbf1_{0<x<1/16}w(4\sqrt x),
\quad d_n=\int_0^1 x^n\widetilde w(x)\,dx.}\tag{7}
\]

We prove pointwise positivity and MUCH more. Since P>0, P'<0 and
\[
\frac{w'(x)}{w(x)}
=-\frac7{8x}+\frac{P'(x^{1/8})}{8x^{7/8}P(x^{1/8})}+
\frac1{16-x}
<-\frac7{8x}+\frac1{16-x}<0,
\]
w is strictly decreasing. For x<1/16, \(4\sqrt x>x\), hence the subtraction is less than w(x)/2, proving \(\widetilde w\ge w/2>0\).

A source-specific sharper estimate uses P monotonicity and the actual 7/8 exponent:
\[
\frac{\tfrac12 w(4\sqrt x)}{w(x)}
\le\frac12\Big(\frac{\sqrt x}{4}\Big)^{7/8}
\frac{16-x}{16-4\sqrt x}
\le\frac1{15\sqrt2}<\frac1{20}.
\]
Therefore for ALL x in (0,1),
\[
\boxed{\frac{19}{20}w(x)\le\widetilde w(x)\le w(x).}\tag{8}
\]
In particular, for EVERY n,d>=0, all finite Newton/Hausdorff jets satisfy
\[
\boxed{
\frac{19}{20}(-1)^d\Delta^dT_n
\le(-1)^d\Delta^d d_n
\le(-1)^d\Delta^dT_n,\qquad
(-1)^d\Delta^d d_n>0.}\tag{9}
\]
The relative 95% comparison is exact, uniform over unbounded differential order, not an empirical fitted constant.

**Even the altered forcing is a positive Hausdorff moment source at EVERY order.**
Since \(\widetilde r(n+1)=16d_n-d_{n+1}\),
\[
\widetilde r(n+1)=\int_0^1x^n(16-x)\widetilde w(x)\,dx,\quad
r(n+1)=\int_0^1x^n(16-x)w(x)\,dx.
\]
Hence for ALL n,d>=0,
\[
\boxed{
\frac{19}{20}(-1)^d\Delta^d r(n+1)
\le(-1)^d\Delta^d\widetilde r(n+1)
\le(-1)^d\Delta^d r(n+1),
}\tag{10}
\]
all quantities strictly positive. This is a **much stronger** matched-moment hostile witness than matching any finite jet or all inverse-power asymptotics. It does NOT say the two complete moment sequences are exactly identical; their small but nonzero differences encode the source.

## UU-04. Literal two-unit Pascal conservation (PROVED; positive but not normality)

Set \(H_{n,d}=(-1)^d\Delta^dT_n\) and
\(\widetilde H_{n,d}=(-1)^d\Delta^d d_n\).
From their moment measures, for every n,d>=0,
\[
H_{n,d}=\int_0^1x^n(1-x)^d w(x)\,dx,\quad
\widetilde H_{n,d}=\int_0^1x^n(1-x)^d\widetilde w(x)\,dx.
\]
Since \(1=x+(1-x)\), these are **positive conservation lattices**:
\[
\boxed{H_{n,d}=H_{n+1,d}+H_{n,d+1},\quad
\widetilde H_{n,d}=\widetilde H_{n+1,d}+\widetilde H_{n,d+1}.}\tag{11}
\]
At each node \(H_{n+1,d}/H_{n,d}\) and \(H_{n,d+1}/H_{n,d}\) lie in (0,1) and sum to 1, so these are legitimate source-derived local branching weights, not an assumed Haar digit law. Equation (8) bounds the entire two-axis lattice by the authentic one. Both original source and coherent changed source admit this positive tower, so positivity, local branch conservation and 95%-matched positive jets CANNOT imply normality.

This is compatible with PR #440's original source Pascal jets, but the **coherent-shadow positive measure and all-grade domination** are new to this research round.

## UU-05. Higher derivatives still have huge prime conductors in the coherent shadow (PROVED PAPER)

For n>=1,d>=1, \(15^d16^nq=47\cdot15^{d-1}16^{n-1}\in\mathbb Z\), so
\[
\boxed{\Delta^d\widetilde U_n
=15^d16^nq-\Delta^d d_n
\equiv-(-1)^d\widetilde H_{n,d}\pmod{\mathbb Z}.}\tag{12}
\]
The circle phase is close to 1, **uniformly in all d>=1**, since
\[
0<\widetilde H_{n,d}\le d_n<T_n<1/(8n+1)^2,\quad n>=1.
\]
Thus for EVERY fixed h and ANY chosen order d=d(n)>=1,
\[
\boxed{|e(h\Delta^{d(n)}\widetilde U_n)-1|
<2\pi|h|/(8n+1)^2\longrightarrow0.}\tag{13}
\]
The higher-order orbit is maximally coherent despite possessing an exact infinite positive differential lattice.

It ALSO has **exponential prime denominator growth at growing differential grade**. For any p=1 mod4 with
\[
8(n+d+1)<p<16n,
\]
its first birth j_p lies inside every d_(n+i) source block for 0<=i<=d, no 2p multiple appears in these blocks, and
\[
\boxed{
p\Delta^d\widetilde U_n
\equiv-c_p16^{n-j_p}15^d\pmod p,\quad
v_p(\Delta^d\widetilde U_n)=-1.}\tag{14}
\]
Negative exponents in the residue are interpreted by modular inversion; p>5 is a unit for both 16 and 15. By PNT-AP, uniformly for \(1\le d\le(1-\varepsilon)n\),
\[
\boxed{\log\operatorname{den}(\Delta^d\widetilde U_n)
\ge4(n-d)+o_\varepsilon(n).}\tag{15}
\]
For every fixed d this grows at rate 4n+o(n), while the *real circle phase of every such derivative* tends to 1. This is a decisive source-adequacy obstruction to deriving angular separation or real Fourier cancellation from all-order prime conductor + all-positive unit derivatives.

## UU-06. Strong all-grade signed Fourier TRANSPORT, with no signed saving (PROVED)

The density w satisfies \(w(x)\le x^{-7/8}/30\), using P<=4, 16-x>=15.
For every integer d>=1, Tonelli gives
\[
\sum_{n=1}^\infty H_{n,d}
=\int_0^1 x(1-x)^{d-1}w(x)\,dx
\le\frac1{30}\mathrm B(9/8,d).
\tag{16}
\]
The SAME estimate holds for \(\widetilde H_{n,d}\le H_{n,d}\).
Here B is the Euler Beta function, and \(\mathrm B(9/8,d)\sim\Gamma(9/8)d^{-9/8}\) as d->infinity.

Using \(|e(a)-e(b)|\le2\pi|a-b|\), for ALL N,d>=1 and fixed integer h:
\[
\boxed{
\left|\sum_{n=1}^N e(h\Delta^d U_n)
-\sum_{n=1}^N e(h15^d16^{n-1}\pi)\right|
\le\frac{\pi|h|}{15}\mathrm B(9/8,d),}\tag{17}
\]
and
\[
\boxed{
\left|\frac1N\sum_{n=1}^N e(h\Delta^d\widetilde U_n)-1\right|
\le\frac{\pi|h|}{15N}\mathrm B(9/8,d).}\tag{18}
\]
These transport errors get *smaller* at higher fixed differential order, even uniformly in N. The true target frequency becomes h15^d, so this is NOT a source-selected signed Weyl bound; the shadow actually remains coherent. Normality of true differential orbit at each fixed grade is equivalent to pi normality by Wall, not automatically known.

## UU-07. Exact dyadic DOUBLE-SUCC renormalization and stable whole-source recovery (PROVED)

For ANY bounded scalar source a(n) and integer base b>=2, let
\[
T_n^{(b)}=\sum_{j>=1}b^{-j}a(n+j),\qquad
d_n^{(b)}=\sum_{j=1}^{n+1}b^{-j}a(n+j),\quad
(\mathcal R_bv)_n=b^{-(n+1)}v_{2n+1}.
\]
Then **exactly**
\[
\boxed{d^{(b)}=(I-\mathcal R_b)T^{(b)},\quad
\|\mathcal R_b\|_{\ell^\infty\to\ell^\infty}=1/b.}\tag{19}
\]
The operator is a strict contraction: \(T=(I-\mathcal R_b)^{-1}d=\sum_{j=0}^\infty\mathcal R_b^j d\) in \(\ell^\infty\), with inverse norm at most b/(b-1). No handwaved "complete from finite data": the full infinite sequence d is the input, and truncations have certified errors.

A direct induction computes the j-th iterate:
\[
\boxed{(\mathcal R_b^jv)_n=
b^{-(n+1)(2^j-1)}v_{2^j(n+1)-1}.}\tag{20}
\]
For original b=16, the first K **rational** terms reconstruct the actual authentic irrational future boundary with exact tail
\[
\boxed{
T_n=\sum_{j=0}^{K-1}
16^{-(n+1)(2^j-1)}d_{2^j(n+1)-1}
+
16^{-(n+1)(2^K-1)}T_{2^K(n+1)-1}.}\tag{21}
\]
The finite blocks are precisely source indices
\([2^j(n+1),\,2^{j+1}(n+1)-1]\); this is a dyadic partition of the original convergent BBP sum, not a new BBP formula or a normality proof.
For K>=1 the residual is positive and bounded by
\[
0<{\rm residual}
<
\frac{16^{-(n+1)(2^K-1)}}
{[8\cdot2^K(n+1)-7]^2},
\tag{22}
\]
since \(T_m<1/(8m+1)^2\) for m>=1.
At n=0 this reconstructs \(\pi/16\) from a superexponentially convergent sequence of rational unit-unit blocks. The complete shadow sequence with declared R genuinely contains the full original source completion; the **selected Fourier cancellation of that completed point** is still unknown.

## UU-08. The unit/doubling commutator is a *source fingerprint*, not quantum curvature (PROVED)

The two operators Delta and R do not commute. On ANY sequence a:
\[
\boxed{
[\Delta,\mathcal R]a_n
=(\Delta\mathcal R-\mathcal R\Delta)a_n
=16^{-(n+2)}(a_{2n+3}-16a_{2n+2}).}\tag{23}
\]
For the original T, \(T_{k+1}-16T_k=-r(k+1)\). Thus
\[
\boxed{[\Delta,\mathcal R]T_n=-16^{-(n+2)}r(2n+3)<0.}\tag{24}
\]
For the rational shadow d, \(d_{k+1}-16d_k=-\widetilde r(k+1)\), so
\[
\boxed{[\Delta,\mathcal R]d_n=-16^{-(n+2)}\widetilde r(2n+3)<0.}\tag{25}
\]
This is a genuine **mixed unit/dilation interaction that measures the exact source**, not a visual cross product or an arbitrary holonomy. Higher commutators are similarly source-derived. These two commutators are close, but *not identical*, because source identity and all-order asymptotics are different kinds of information.

The commutator is O(16^-n n^-2), absolutely summable and seed-blind. Its existence gives a discriminator in the **source** map; it does not provide the real signed growth estimate needed to prove pi normality.

## 9. What is proved, refuted, and still required

**PROVED PAPER, conditional only on explicit classical input in PNT statements:** source-selected ∆^d conductor (3)–(4); Hausdorff density of the coherent finite shadow (7), 95% domination and ALL positive source jets (8)–(11); exponentially large conductor + uniform full coherence of its higher derivatives (12)–(15); Gamma/Beta-controlled all-horizon phase transport (16)–(18); general-base contraction and exact dyadic source recovery (19)–(22); exact source commutator (23)–(25).

**INHERITED:** positive authentic source moment law and Newton jets #440, coherent changed-source construction #421, prime-birth p-adic residue #459, all-lag original/shadow conductor results #462. The new unit-unit implications are extensions, not replacements.

**REFUTED AS GENERAL INFERENCE:** complete positivity of every unit differential + arbitrarily high off-diagonal p-adic conductor + zero seed + close complete Hausdorff jets => real Fourier cancellation. Our explicit coherent changed source defeats that implication. Neither rational-state phase injectivity nor stable tail reconstruction implies signed equidistribution.

**OPEN / UNVERIFIED:** the original \(S_N(h)=o(N)\) for every fixed h!=0, pi normality, any nontrivial selected source-dependent all-prime mixed cofactor saving. Full math proof requires a genuinely new **Archimedean signed estimate**, not just a transport or positivity theorem.

### Classical/external provenance

- Hausdorff moment criterion and finite differences: Diaconis–Freedman, *The Markov Moment Problem and de Finetti's Theorem* (Math. Z. 247 (2004), pp. 183–199), https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/diaconis_2004.pdf
- Euler Beta integral: NIST DLMF §5.12.1, https://dlmf.nist.gov/5.12.E1
- Rational affine normality preservation (Wall): https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81
- Classical PNT in residue class 1 mod 4: inherited #459/#462, e.g. https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html
