# SUCC — Non-Pisot finite arithmetic ramified through Pisot carriers

**Date:** 2026-10-30. **Research-only / draft.** Child of Universal N PR #416 exact head 725377a64748ab0c442d16a61509b99687412505, rooted in merged Main XVI. The original author's hypothesis: *non-Pisot finite arithmetic dynamics may be ramified into Pisot components*, with Pascal, Fibonacci, Pisot and Gamma representing forms of finite counting over the same underlying N carrier. No original BBP forcing, selected U_0=0, archived source, production module, source theorem contract, workflow or main is modified.

**Steelman:** 'ramification' has THREE typed meanings: (R1) a nonnegative finite word-grammar refinement by Pisot path components; (R2) an exact, reversible change of arithmetic generator, perhaps with inverse operations, to Pisot coordinates; (R3) algebraic-number-field ramification at primes, as detected by discriminants. These are mathematically different. A Pisot representation of a finite algebraic carrier is not a theorem about normality of its selected output sequence or about universal physical dynamics.

## PR-01. A two-state non-Pisot count becomes Pisot by an invertible finite binomial observer (EXACT)

Let \(a_0=a_1=1\) and \(a_n=a_{n-1}+3a_{n-2}\) for \(n\ge2\), with generating function
\[
A(z)=\frac1{1-z-3z^2},\qquad
A=\begin{pmatrix}1&3\\1&0\end{pmatrix},\quad a_n=(A^n)_{11}.
\]
The spectral roots are \(\alpha=(1+\sqrt{13})/2>1\) and \(\beta=(1-\sqrt{13})/2<-1\). Therefore \(\alpha\) is NOT Pisot.

Add ONE optional idle self-loop per state:
\[
B=A+I=\begin{pmatrix}2&3\\1&1\end{pmatrix}.
\]
The matrix is strictly positive integer; its characteristic polynomial is \(x^2-3x-1\), with roots \(\theta=\alpha+1=(3+\sqrt{13})/2\) and \(\theta'=\beta+1=(3-\sqrt{13})/2\in(-1,0)\). Thus \(\theta\) is a **Pisot unit** (norm -1), and
\[
b_n=(B^n)_{11}=\sum_{k=0}^n\binom nk a_k,\qquad
a_n=\sum_{k=0}^n(-1)^{n-k}\binom nk b_k.
\]
These are exact integer binomial inverses because \(A\) commutes with I. \(b_n\) satisfies \(b_n=3b_{n-1}+b_{n-2}\), \(b_0=1,b_1=2\). The original and Pisot time-evolution operators are **NOT dynamically conjugate**: B and A have different eigenvalues; the same arithmetic path counts are linked by a time-index binomial transform whose inverse has alternating signs.

**General quadratic theorem (EXACT):** For all positive integers \(a,b\), let \(A=\begin{pmatrix}a&b\\1&0\end{pmatrix}\) and \(\alpha,\beta=(a\pm\sqrt{a^2+4b})/2\). Choose a nonnegative integer m nearest to \(-\beta>0\). Then \(|\beta+m|\le1/2\), while \(\alpha+m>1\) (since \(\alpha-\beta=\sqrt{a^2+4b}\ge\sqrt5>2\)). The positive integral matrix \(B=A+mI\) has dominant \(\theta=\alpha+m>1\), and all other **algebraic conjugates of \(\theta\)** lie in the open unit disk. If the quadratic splits over Q, \(\theta\) is an integer >1 and is Pisot of degree one; otherwise it is Pisot quadratic. The binomial transform becomes \(b_n=\sum_k\binom nk m^{n-k}a_k\), invertible via \((-m)^{n-k}\). This is a broad, concrete theorem for finite two-length colored path grammars, not for arbitrary high-order integer recurrences.

## PR-02. Positivity-preserving ramification into Fibonacci components (EXACT)

The same non-Pisot grammar is a combinatorial renewal process with one length-one tile and THREE distinguishable length-two tiles. Its coefficient is
\[
a_n=\sum_{j=0}^{\lfloor n/2\rfloor}3^j\binom{n-j}{j}.
\]
Choose ONE distinguished ordinary length-two color and TWO additional exceptional colors. Let
\[
F(z)=\frac1{1-z-z^2}=\sum_{n\ge0}F_{n+1}z^n.
\]
Formal generating series give
\[
\boxed{\frac1{1-z-3z^2}
=\frac{F(z)}{1-2z^2F(z)}
=\sum_{k\ge0}2^k z^{2k} F(z)^{k+1}.}
\]
Proof: the coefficient indexed by k counts k exceptional colored dominoes (2^k color choices), separated by k+1 Fibonacci tiling segments. Every finite coefficient receives only \(\lfloor n/2\rfloor+1\) terms, each a nonnegative integer, and the decomposition is lossless once the marked exceptional locations/colors are retained. An exact integer convolution oracle validates all coefficients through n=24.

**Important no-go:** the number k of Pisot/Fibonacci factors is **not bounded uniformly in n**. A fixed finite scalar linear combination of standard Pisot recurrence sequences cannot reproduce a non-Pisot characteristic root \(\alpha>1\), as such linear combinations are annihilated by a product of Pisot characteristic polynomials. Since \(\alpha\) is non-Pisot, it is neither the dominant root of any Pisot minimal polynomial nor a small-modulus conjugate of one. This is a genuine limitation, not a refutation of the positive unbounded-depth ramification.

## PR-03. A cubic where ANY AFFINE PISOTIFICATION FAILS, yet a POSITIVE polynomial gives a Pisot UNIT (EXACT)

Take the three-state finite grammar \(a_n=a_{n-1}+3a_{n-3}\) with primitive nonnegative integer companion
\[
A=\begin{pmatrix}1&0&3\\1&0&0\\0&1&0\end{pmatrix},
\qquad P_A(x)=x^3-x^2-3.
\]
Let \(\alpha\) be its unique positive real root. Exact sign evaluation proves \(9/5<\alpha<2\). The conjugates are \(u\pm iv\), with \(u=(1-\alpha)/2\in(-1/2,-2/5)\), and
\[
v^2=3/\alpha-u^2>3/2-1/4=5/4>1.
\]
Thus the original growth root is non-Pisot, and \(|\beta+m|\ge|\Im\beta|>1\) for **every real** m, so adding scalar self-loops cannot Pisotify the cubic.

But define the strictly positive integer-polynomial path operation
\[
\boxed{B=2I+A+A^2=
\begin{pmatrix}4&3&6\\2&2&3\\1&1&2\end{pmatrix}.}
\]
The matrix is positive, primitive, and unimodular: \(\det B=1\). Its characteristic polynomial is
\[
P_B(t)=t^3-8t^2+5t-1.
\]
On the algebraic number field \(K=\mathbb Q(\alpha)\), put
\[
\boxed{\Theta=2+\alpha+\alpha^2.}
\]
Using \(\alpha^3=\alpha^2+3\), a finite integer identity gives
\[
\boxed{(2-\alpha)\Theta=1,\quad\alpha=2-\Theta^{-1}.}
\]
Hence \(\Theta\) is an **algebraic unit**. It is >1 (since \(\alpha\in(9/5,2)\)), while each other conjugate equals \(1/(2-\beta)\) and has modulus <1/2 because \(\Re\beta<0\). Therefore \(\Theta\) is **Pisot unit**, about \(7.33710854965505\); its other roots are \(0.331445725172477\pm0.162595213477218i\).

On the actual finite integral matrices this reads
\[
\boxed{
B(2I-A)=(2I-A)B=I,\qquad A=2I-B^{-1}.
}
\]
The inverse is itself integer:
\[
B^{-1}=2I-A=B^2-8B+5I.
\]
The B/Pisot dynamics is NOT conjugate to A's one-step dynamics, but the original A and its exact successor powers can be reconstructed via integer Laurent polynomials in B (indeed ordinary integer polynomials since B^{-1}\in\mathbb Z[B]). This is a constructive **finite nonnegative Pisot coordinate carrier** with a source-faithful signed inverse.

### Literal arithmetic ramification, not only a metaphor

The cubic root \(\alpha\) and Pisot unit \(\Theta\) generate the SAME integral order. Indeed
\[
\Theta=2+\alpha+\alpha^2,\quad
\Theta^2=13+7\alpha+8\alpha^2.
\]
The change-of-basis from \(1,\alpha,\alpha^2\) to \(1,\Theta,\Theta^2\) is the integer matrix
\[
C=\begin{pmatrix}1&2&13\\0&1&7\\0&1&8\end{pmatrix},
\quad \det C=1.
\]
Therefore \(\mathbb Z[\Theta]=\mathbb Z[\alpha]\) EXACTLY. Their discriminants coincide:
\[
\boxed{\operatorname{Disc}(P_A)=\operatorname{Disc}(P_B)=-255=-3\cdot5\cdot17.}
\]
The discriminant is squarefree, so this common order is the full ring of integers \(\mathcal O_K\), and the rational primes **3,5,17** are precisely the ramified primes of this toy cubic field. The equality \(255=16^2-1\) is an exact numeral identity, NOT an inferred relation to base-16 BBP, \(\pi\) normality, or exceptional BBP primes. No physical branch points are claimed.

This gives the author's word "ramification" a literal algebraic-number-theoretic interpretation: different finite counting operators can be coordinates of the same underlying prime-place arithmetic order.

### Minimality and a prime-place relocation effect (EXACT)

For a polynomial \(P(z)=c_0+c_1z\in\mathbb Z[z]\) with \(c_1\ne0\), the complex conjugates of \(P(\alpha)\) have imaginary part \(|c_1|\cdot|\Im\beta|>1\). Therefore **NO nonconstant integer linear polynomial** can Pisotify this cubic field. The positive quadratic \(P(z)=2+z+z^2\) is minimal in polynomial degree among any integer polynomial coordinate change generating a Pisot number here. A constant integer >1 is trivially Pisot but does not generate the cubic field and is therefore excluded.

The matrix determinants give a separate, operational all-prime distinction:
\[
\boxed{\det A=3,\qquad\det B=1,\qquad A=2I-B^{-1}.}
\]
The Pisot-unit carrier \(B\) is invertible over \(\mathbb Z_p\) for EVERY prime p, whereas the original non-Pisot \(A\) loses invertibility modulo 3. Under the reversible *integral algebra representation*, this failure is relocated to the observation map \(2I-B^{-1}\) rather than erased. The discriminant further shows 5 and17 are ramified in the number field despite \(A\) remaining nonsingular modulo those two primes. **Dynamic invertibility and algebraic field ramification are different invariants.** No known BBP all-place phase theorem follows from this toy example.

## PR-04. Cubic non-Pisot counting ALSO has a positive Pisot path refinement

The base grammar with one length-one and ONE length-three tile has generating function
\[
G(z)=1/(1-z-z^3)
\]
and Pisot dominant root \(\rho\) of \(t^3-t^2-1\). Its complex conjugates have modulus \(\rho^{-1/2}<1\) by the product of conjugates and one-real-root discriminant condition. Exactly as for Fibonacci,
\[
\boxed{
\frac1{1-z-3z^3}
=\sum_{k\ge0}2^k z^{3k}G(z)^{k+1}.}
\]
All coefficients are nonnegative integers and all fixed coefficients have a finite expansion. An independent truncated-convolution oracle checks all coefficients through degree 22. This is a **distinct** positive path-counting ramification from the fixed three-state Pisot polynomial generator B=2I+A+A².

## PR-05. Field-level existence is CLASSICAL, much more general, but does NOT solve positivity or dynamics

A theorem due to Pisot, developed by Salem/Meyer and in later algorithmic work, states that **every real number field admits a Pisot unit generating it as a field** (degree >1; Q has ordinary integer Pisot generators). Thus for any real algebraic integer \(\alpha\), there exists a Pisot unit \(\Theta\) such that \(\mathbb Q(\alpha)=\mathbb Q(\Theta)\), giving an exact **rational polynomial-coordinate representation** \(\alpha=P(\Theta)\) with \(\deg P<[K:\mathbb Q]\). This is a strong, pre-existing partial validation of "nonPisot finite arithmetic admits Pisot coordinates". Literature: *Pisot unit generators in number fields*, Journal of Symbolic Computation (2018), DOI 10.1016/j.jsc.2017.11.005, https://doi.org/10.1016/j.jsc.2017.11.005; *Number fields without a unit generator* (2016) https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/number-fields-without-a-unit-generator/ ; and *Complex Pisot numbers in algebraic number fields* (2015) https://www.numdam.org/articles/10.1016/j.crma.2015.09.007/ .

**Hard scope limit:** A rational polynomial representation does not generally yield (i) a nonnegative-integer transfer matrix, (ii) a unimodular integral order change, (iii) a fixed finite positive sum of Pisot-recursive sequences, (iv) the original recurrence's time evolution as a conjugate operator, or (v) any normality/mixing statement about a selected digit stream. Some finite-state recurrences have additional spectral factors from number fields without real embeddings. Claim of universal **positive finite Pisot decomposition** is UNVERIFIED.

## PR-06. SUCC observer/carrier truth and the next decisive probe

Build the generic Pascal/Bratteli finite path grammar over N first. Distinguish:
- **Finite path counting:** the original colored grammar A or its positive refinements.
- **Pisot carrier:** B=A+mI or B=P(A), with exact integer coefficients; record mark/clock and inverse.
- **Integral/place geometry:** the common ring of integers and ramified prime-place labels (for the cubic, 3,5,17).
- **Selected signed arithmetic:** the authentic BBP source forcing, initial first jet U0=0, literal radix-16 carries and actual real-circle character phases. This is NOT automatically represented by a toy colored-tiling Pisotification.
- **Observer model adequacy:** a property proven in the Pisot frame may be transported only after checking it descends through the exact comparison map; convergence of non-dominant Pisot conjugates is not digit equidistribution of the original nonPisot sequence.

**Verdicts:**
- DISCLOSED: exact two-state binomial Pisot transform; all positive 2-step colored grammars are integer-shift Pisotifiable; two independent positive Fibonacci and cubic grammar refinements; cubic positive-polynomial Pisot-unit matrix with integer inverse; equality of cubic integer orders and ramification set; affine-shift impossibility for this cubic.
- CLASSICAL: every real number field has a Pisot unit generator; positive/negative polynomials and spectral coordinate transport are distinct kinds of representation.
- REFUTED: finite linear combination of Pisot recurrences suffices in general; adding any scalar loop Pisotifies all higher-order systems; a Pisot coordinate implies the original operator is Pisot; identical counting limit implies the same selected digit law; ramification primes of this toy prove a π theorem.
- OPEN: universal nonnegative/canonical Pisot realization of arbitrary finite arithmetic dynamical systems; source- and zero-seed-sensitive all-horizon signed π estimate; RH; physical interpretation.

**Next falsifier:** Seek a FUNCTORIAL exact Pisot enrichment of the universal N path category that preserves original source/pole data, full signed integer carries and all-place prime valuations. Reject any proposed quotient that loses the signed inverse or initial jet. For SUCC's BBP source, test original four-pole versus matched Gamma-rank mutants and coherent same-forcing seed before interpreting Pisot-conjugate contraction as global selected arithmetic mixing.

**Validation authority:** independent exact SymPy oracle for cubic matrices, discriminants, integral basis, Pisot conjugates, and positive generating-series decomposition PASS; exact arithmetic standard-library source probe committed for reproducibility. Full root SUCC test suite, Lean/CI, blind referee NOT RUN. Do not merge blindly.
