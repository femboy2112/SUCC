# Adversary bearing — exact BBP volume and carry algebra

Starting source: SUCC `e14d46c17a65e1e5f231c619657b9332caa181c0`. This bearing was formed independently of the new production implementation. No imported source is changed. The frozen probe domains below precede the implementation; full proofs and executed receipts follow them.

## Frozen finite probe domains

- Green bases `−3/2,−1/2,0,2/3,1,2,16`; seeds `−2/3,0,5/4`; horizons0..17. Three source-tape pairs use the original four-pole r(j), the alternating rational `(-1)^j/(j+1)`, and `(j²−3)/(2j+1)`.
- Additive carry fractions `0,1/7,1/2,6/7`; affine multipliers `−3,−1,0,1,2,16`, translations `−7/3,−1/2,0,2/5,47/15`, and circle states `0,1/16,1/2,15/16,256/257`.
- Gamma integer shapes1,2,3,5; frequencies `−7,−2,1,3,16`; coefficient indices0..40. Fixed carry residues1,2,4,16,256,65536 must each be defeated by an explicit coordinate.
- Exact finite Gamma/tail integrals: n in `0,1,2,5,13`, Green depth D in `1,3,7`, Gamma cutoff M in `0,1,4,8`, and shapes1,2,3,5. Independent routes are direct rational r-sums and explicit integration of a separately expanded polynomial.
- Mutations to reject: omit the Green diagonal subtraction; use the wrong product base; add only a homogeneous seed product while omitting seed/source cross terms; use convolution weights for a pointwise Gamma product; drop a carry seam; commute phase and average; redraw a shared source; treat the divergent future raw-U Gamma sum as a positive integral; drop the finite Green boundary term.

These are finite calibration domains. Universal statements below require their own proofs; a passed scan does not certify an analytic limit or signed Weyl cancellation.

**Tempering extension preregistered before execution:** normalized rates1,15,16,31; integer shapes1,2,3,5; geometric input16; cutoffs0..16. The critical half-shape control uses rational rising-factorial coefficients through256, checking the exact cumulative identity while individual terms decrease. This tests the new rate-domain rule without importing production code.

## Verdict and source boundary

**DISCLOSED within the stated domains:** the source has a graded Green product algebra, a finite triangular polynomial lift, an exact affine carry algebra, and a convergent Gamma calculus after its domain is checked. These operations compose if the real lift, initial boundary, common source, and product grading remain present. Neither applying a character before averaging nor treating a future Gamma average of the raw BBP source as automatically convergent is a valid rewrite.

The source throughout is the original, zero-seeded recurrence

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n),\qquad n\ge1.
\]

Write \(e(t)=\exp(2\pi i t)\). No alternative seed is used to refute a statement about this pointed source. Arbitrary-lift examples below test the domain of a proposed universal quotient operation; they are explicitly distinguished from the authentic source example \(U_1=47/15\).

The classical boundary constant is \(\xi=\pi/16\), distinguished from the Gamma shape \(\alpha\). Its BBP identification is inherited from the existing source dossier, not newly proved by a finite probe. The algebra below also works with the self-contained definition \(\xi=\int_0^1R(x)\,dx\), so none of the convergence or carry obstructions depend on a numerical approximation to \(\pi\).

### 1. Exact source volume and retained tail

Set

\[
g(x)=4-2x^3-x^4-x^5
=(1-x)(x^2+2)(x^2+2x+2),\qquad
R(x)=\frac{g(x)}{16-x^8}.
\]

Direct integration gives

\[
r(n)=\int_0^1x^{8n-8}g(x)\,dx>0.
\]

The finite geometric identity, with the zero initial boundary retained, gives

\[
U_n=\int_0^1R(x)(16^n-x^{8n})\,dx
=16^n\xi-T_n,
\quad
T_n=\int_0^1x^{8n}R(x)\,dx.
\]

All integrands here are continuous and nonnegative on \([0,1]\); \(0\le T_n\le\xi\). Expanding \((16-x^8)^{-1}\) by its uniformly convergent geometric series yields

\[
T_n=\sum_{k\ge1}16^{-k}r(n+k),\qquad
16T_n-T_{n+1}=r(n+1).
\]

The finite approximation has a different boundary:

\[
T_n^{(D)}=\sum_{k=1}^D16^{-k}r(n+k),\qquad
16T_n^{(D)}-T_{n+1}^{(D)}
=r(n+1)-16^{-D}r(n+D+1).
\tag{A1}
\]

The omitted term is strictly positive. Applying a valid identity for the infinite tail to two same-depth finite tails without this term is an exact error, not a small-roundoff issue.

### 2. Graded Green multiplication, with full seeded inputs

For a commutative coefficient ring, scalar \(b\), and source tape \(f\), define

\[
(G_bf)_n=\sum_{j=1}^n b^{n-j}f_j,\qquad (G_bf)_0=0.
\]

Let \(Y_n=b^nu+(G_bf)_n\) and \(Z_n=c^nv+(G_cg)_n\). Then

\[
Y_nZ_n=(bc)^nuv+
G_{bc}\!\left[fZ+gY-fg\right]_n.
\tag{A2}
\]

**Proof.** From \(Y_n=bY_{n-1}+f_n\), \(Z_n=cZ_{n-1}+g_n\),

\[
Y_nZ_n-bcY_{n-1}Z_{n-1}
=cf_nZ_{n-1}+bg_nY_{n-1}+f_ng_n
=f_nZ_n+g_nY_n-f_ng_n.
\]

The two sides of (A2) have the same recurrence and the same initial value \(uv\). This proves the formula at every finite horizon. In particular, the product changes the homogeneous grade from \(b,c\) to \(bc\). The forcing uses the **full seeded** \(Y,Z\), so adding only \((bc)^nuv\) to the zero-seed product formula is insufficient.

Three exact mutation receipts are enough to distinguish these rules:

- At the first step with \(b=c=1\), \(f_1=g_1=1\), zero seeds, removing \(-fg\) gives \(2\) in place of \(1\).
- With \(b=c=2\), constant input one, zero seeds, the product at time two is \(3^2=9\). Its product forcing is \((1,5)\). Applying \(G_2\) gives \(7\); applying the required \(G_4\) gives \(9\).
- With \(b=c=1,u=0,v=1,f_1=1,g_1=0\), the true product is \(1\). Using only unseeded forcing plus the homogeneous seed product gives \(0\).

For powers of one scalar source, the binomial theorem gives the triangular lift

\[
U_n^m=\sum_{k=0}^{m}\binom mk16^kU_{n-1}^kr(n)^{m-k}.
\tag{A3}
\]

Thus each finite polynomial degree is closed after all lower powers and the original forcing are retained. This is a finite algebraic closure statement. It does not make floor, phase, or a divergent infinite filter into polynomial operations.

### 3. Gamma cascade and pointwise product are different operations

For integer shape \(m>0\), let

\[
w_j^{(m)}=\binom{j+m-1}{j}2^{-j-m},\qquad
\sum_{j\ge0}w_j^{(m)}z^j=(2-z)^{-m}.
\]

Multiplication of the convergent generating functions, or a finite coefficient comparison, gives

\[
\sum_{j=0}^n w_j^{(m)}w_{n-j}^{(\ell)}=w_n^{(m+\ell)}.
\tag{A4}
\]

This is **cascade/convolution**, not multiplication at the same source time. The pointwise product is instead

\[
w_j^{(m)}w_j^{(\ell)}
=2^{-m-\ell}\binom{j+m-1}{j}\binom{j+\ell-1}{j}4^{-j}.
\]

For \(m=\ell=1,j=1\), the pointwise product is \(1/16\), whereas \(w_1^{(2)}=1/4\). Even its normalization changes: \(\sum_j(w_j^{(1)})^2=1/3\). A generic rewrite “a product adds the Gamma orders” is therefore false unless the product has explicitly been declared to mean cascade.

The analogous continuous distinction is exact. For \(\alpha,\beta>0\) and \(\lambda,\mu\ge0\), define

\[
k_\alpha^\lambda(t)=\mathbf1_{t>0}\,t^{\alpha-1}e^{-\lambda t}/\Gamma(\alpha),
\]

convolution at one rate adds the shapes. Pointwise multiplication, when \(\alpha+\beta>1\), obeys

\[
k_\alpha^\lambda(t)k_\beta^\mu(t)
=\frac{\Gamma(\alpha+\beta-1)}{\Gamma(\alpha)\Gamma(\beta)}
k_{\alpha+\beta-1}^{\lambda+\mu}(t).
\]

If \(\alpha+\beta\le1\), the product is not locally integrable at zero. A boundary-domain annotation is part of this rule.

### 4. Canonical carries and chronological affine blocks

Represent a real lift as \(u=k+q\), where \(k=\lfloor u\rfloor\in\mathbb Z\), \(q\in[0,1)\). Define

\[
q\oplus p=\{q+p\},\qquad \sigma(q,p)=\lfloor q+p\rfloor.
\]

The exact additive cocycle identity is

\[
\sigma(q,p)+\sigma(q\oplus p,r)
=\sigma(p,r)+\sigma(q,p\oplus r)
=\lfloor q+p+r\rfloor.
\tag{A5}
\]

Both equalities follow by extracting the integer \(\lfloor q+p\rfloor\) or \(\lfloor p+r\rfloor\) from the same floor. Consequently the lifted sum
\((k,q)+(\ell,p)=(k+\ell+\sigma(q,p),q\oplus p)\) is associative. Omitting the carry at \(q=p=1/2\) loses the integer one.

For an affine block \(A=(b,a)\), with **integer** multiplier \(b\) and arbitrary real translation \(a\), put

\[
q_A=\{bq+a\},\qquad \kappa_A(q)=\lfloor bq+a\rfloor.
\]

Its lift is \(k_A=bk+\kappa_A(q)\). If a later block is \(B=(c,d)\), with integer \(c\), chronological composition is

\[
B\circ A=(cb,ca+d),\qquad
\kappa_{B\circ A}(q)=c\kappa_A(q)+\kappa_B(q_A).
\tag{A6}
\]

Indeed \(cbq+ca+d=c\kappa_A(q)+cq_A+d\), and the first summand is an integer. This also proves the identity for negative multipliers. Truncation toward zero is not the canonical floor and fails at negative lifts.

Original BBP blocks have multiplier \(16^\ell\) and their exact finite Green forcing as translation. Formula (A6) preserves block composition and its carry at every seam. The integer multiplier also means that the **unweighted next circle phase itself** descends from the current circle phase and known forcing. The obstruction below concerns real-lift targets and nonintegral weights, not that valid ordinary phase recurrence.

### 5. Exact criterion for phase after a weighted lift

Fix \(h\in\mathbb Z\setminus\{0\}\) and finitely many real weights \(w_j\). On arbitrary real lift tuples, the map

\[
(u_j)_j\longmapsto e\!\left(h\sum_jw_ju_j\right)
\]

descends to the tuple of fractional parts \((\{u_j\})_j\) **if and only if** \(hw_j\in\mathbb Z\) for every coordinate.

**Proof.** Changing only \(u_j\) by an integer one multiplies the output by \(e(hw_j)\), proving necessity. If all \(hw_j\) are integral, every integer lift change has phase one, proving sufficiency. In particular, for \(h=1\), a nonnegative normalized average with at least two nonzero weights cannot have this universal descent.

If \(u_j=\theta_j+k_j\), then the correct finite identity is

\[
e\!\left(h\sum_jw_ju_j\right)
=e\!\left(h\sum_jw_j\theta_j\right)
 e\!\left(h\sum_jw_jk_j\right).
\tag{A7}
\]

When \(hw_j\) is rational with reduced denominator \(q_j\), the coordinate residue \(k_j\bmod q_j\) is sufficient and has the least positive period. A common residue modulus \(M\) works for arbitrary independent lift changes only if \(q_j\mid M\) for every coordinate.

For the integer-shape Gamma weights,

\[
q_j=\frac{2^{j+m}}{\gcd\!\left(\lvert h\rvert\binom{j+m-1}{j},2^{j+m}\right)}
\ge\frac{2^{j+m}}{\lvert h\rvert\binom{j+m-1}{j}}
\longrightarrow\infty.
\tag{A8}
\]

The denominator in the lower bound grows only polynomially in \(j\), with fixed degree \(m-1\). No one fixed finite carry modulus suffices at every Gamma coordinate. This conclusion already follows from single-coordinate, hence finite-support, lift mutations. It does **not** assert that arbitrary mutated lifts occur on the canonical BBP orbit.

There is also an authentic, unchanged-source receipt. Since \(U_1=47/15=3+2/15\), weight \(1/2\) yields

\[
\{U_1/2\}=17/30,\qquad \{\{U_1\}/2\}=1/15.
\]

The two character values differ by the factor \(e(1/2)=-1\). Thus dropping the actual original carry fails at the first nonzero source state.

**Prior-art boundary.** [PJT-15](../../../docs/CLAIM_SUPPLEMENT_PASCAL_SOURCE.md) already records the carry-modulus requirement for rational filters, and [JPC-22](../../../docs/CLAIM_SUPPLEMENT_PI_JOINT_CARRIER.md) records that additional fractional marginals do not supply the integer lift needed under rational division. Equation (A8) is the Gamma-specific unbounded coordinate-grade consequence of that inherited obstruction, not a claim that the basic carry issue is new.

### 6. Nonlinear phase and shared source cannot be silently moved through averaging

Let \(X\) take values zero and one with equal probability. Then

\[
e(\mathbb EX)=e(1/2)=-1,\qquad
\mathbb E e(X)=1.
\tag{A9}
\]

This exact two-point example refutes commuting phase with integration, even with positive normalized weights. The same source also separates a shared-input product from a redrawn independent input:

\[
\mathbb E X^2=1/2,\qquad (\mathbb EX)^2=1/4.
\tag{A10}
\]

A multivariable volume representation may introduce one variable for each factor only if its kernel still enforces the intended shared dependence, or if independence is separately part of the model. Merely expanding more variables does not justify replacing one common source by independent copies.

These examples are universal rewrite countermodels. They do not assert failure of a particular BBP cancellation estimate. To prove such an estimate, the original signed source phase, its common dependence, and its carry transport must remain in the target expression.

### 7. Gamma filtering has a source-dependent convergence domain

For arbitrary real shape \(\alpha>0\), let

\[
w_j^\alpha=\frac{(\alpha)_j}{j!}\,2^{-j-\alpha}.
\]

The raw positive future average \(\sum_jw_j^\alpha U_{n+j}\) diverges. Positivity of the source gives \(U_k\ge16^{k-1}r(1)>0\) for \(k\ge1\), while

\[
\frac{w_{j+1}^\alpha16^{j+1}}{w_j^\alpha16^j}
=8\frac{j+\alpha}{j+1}\longrightarrow8.
\]

Its summands do not approach zero. For integer shape \(m\ge1\), the ratio of consecutive positive raw-source summands is strictly greater than eight wherever both source indices are positive. An algebraic continuation such as \((2-16)^{-m}\) is not the value of this positive divergent series.

The bounded retained tail has a valid Gamma volume. Tonelli's theorem and the scalar generating function give

\[
\sum_{j\ge0}w_j^\alpha T_{n+j}
=\int_0^1x^{8n}R(x)(2-x^8)^{-\alpha}\,dx.
\tag{A11}
\]

Let \(E\) be the forward shift on bounded sequences. It has norm one, and the probability weights sum to one, so \(\sum_jw_j^\alpha E^j\) converges in operator norm. Every partial sum commutes with \(16I-E\); therefore so does the limit. It legitimately transports \((16I-E)T=(r(n+1))_n\). This is a weighted **future-observable** transform; it is not automatically a retarded physical-time propagation operator.

For finite tail depth \(D\) and finite Gamma cutoff \(M\), the exact commuting relation still contains

\[
16^{-D}\sum_{j=0}^M w_j^\alpha r(n+j+D+1),
\]

the positive filtered boundary from (A1). The audit checks this boundary by two independent finite rational routes.

### 8. Constructive repair by tempering

For \(\lambda>0\), use normalized weights

\[
w_j^{\alpha,\lambda}
=\frac{(\alpha)_j}{j!}\frac{\lambda^\alpha}{(\lambda+1)^{j+\alpha}},\qquad
\sum_jw_j^{\alpha,\lambda}z^j
=\left(\frac\lambda{\lambda+1-z}\right)^\alpha
\quad (|z|<\lambda+1).
\]

For the raw zero-seeded BBP source,

\[
\sum_{j\ge0}w_j^{\alpha,\lambda}U_{n+j}
\text{ converges if and only if }\lambda>15.
\tag{A12}
\]

For \(\lambda>15\), the exact result is

\[
16^n\xi\left(\frac\lambda{\lambda-15}\right)^\alpha
-\int_0^1x^{8n}R(x)
 \left(\frac\lambda{\lambda+1-x^8}\right)^\alpha dx.
\tag{A13}
\]

**Proof.** Insert \(U_{n+j}=16^{n+j}\xi-T_{n+j}\). The bounded-tail average converges for every \(\lambda>0\), and its displayed integral follows by Tonelli. The homogeneous sum is a positive scalar binomial series at \(z=16\), so converges exactly when \(16<\lambda+1\), except that the endpoint must be checked separately. At \(\lambda<15\), its consecutive-term ratio approaches \(16/(\lambda+1)>1\). At \(\lambda=15\), its partial sums are a positive constant times

\[
\sum_{j=0}^M\frac{(\alpha)_j}{j!}
=\frac{(\alpha+1)_M}{M!}
=\prod_{k=1}^M\left(1+\frac\alpha k\right)\longrightarrow\infty.
\tag{A14}
\]

The finite identity follows by induction; divergence follows, for example, from \(\log(1+\alpha/k)\ge\alpha/(k+\alpha)\). When \(0<\alpha<1\), individual critical summands decrease to zero, but the sum still diverges. Subtracting a bounded-tail average cannot repair a divergent positive homogeneous sum.

For \(0<\lambda\le15\), the counterterm

\[
U_{n+j}-16^{n+j}c
\]

has a convergent Gamma future average **if and only if** \(c=\xi\): a wrong \(c\) leaves a nonzero multiple of the divergent homogeneous partial sums, plus a convergent tail. The correct boundary gives exactly the negative of the filtered tail in (A11), with the corresponding tempered kernel. For \(\lambda>15\), every fixed \(c\) gives a convergent average, so there is no uniqueness claim in that range. Removing this growth mode is a domain repair, not a proof of cancellation of the original character sequence.

### 9. Hostile audit of the finite linear-recurrence obstruction

This section audits the constructor's proposed upgrade, after the independent Green/carry probe was frozen. It is a proof audit, not a second computational witness.

**Claim.** For a fixed nonzero integer \(h\), the canonical sequence
\(z_n=e(hU_n)\) satisfies no nontrivial eventual finite-order homogeneous linear recurrence over \(\mathbb C(n)\). In particular, it is not P-recursive. It still satisfies the exact nonlinear relation \(z_n=z_{n-1}^{16}e(hr(n))\).

**Fresh-prime lemma.** Put \(p=8b-7>5\) prime. Every denominator in every \(U_k\), \(k<b\), is prime to \(p\), because the largest source denominator before time \(b\) is \(8b-10=p-3\). Also

\[
U_b=B_b+4/p,\qquad
B_b=16U_{b-1}-\frac2{p+3}-\frac1{p+4}-\frac1{p+5}
\]

has \(p\)-free denominator. Hence there is an integer \(M\), prime to \(p\), for which all earlier phases in any chosen finite window and \(e(hB_b)\) lie in \(E=\mathbb Q(\zeta_M)\), while
\(z_b=e(hB_b)\zeta_p^{4h}\).

There are arbitrarily large primes \(p\equiv1\pmod8\). An elementary proof sufficient here takes an even integer \(N\) divisible by any prescribed finite collection of such primes. Any prime divisor \(q\) of \(N^4+1\) is odd, is outside that collection, and gives \(N\) multiplicative order exactly eight modulo \(q\). Thus \(q\equiv1\pmod8\). Large choices can avoid the finitely many primes dividing \(4h\) and any prescribed size bound.

**Fixed-number-field contradiction.** Suppose first that

\[
\sum_{j=0}^d P_j(n)z_{n+j}=0\qquad(n\ge n_0),
\]

where the \(P_j\) are polynomials over one number field \(K\), not all zero. Let \(d\) now denote the last nonzero shift. The case \(d=0\) is immediately impossible since \(z_n\ne0\) and a nonzero polynomial has finitely many roots. Otherwise choose \(b=n+d\) with fresh \(p=8b-7\), such that \(P_d(n)\ne0\), \(p\nmid4h\), and \(p-1>[K:\mathbb Q]\). Solving the relation for its final phase shows \(z_b\in KE\), hence \(\zeta_p^{4h}\in KE\), hence \(\zeta_p\in KE\). But

\[
[E(\zeta_p):E]=\frac{\varphi(Mp)}{\varphi(M)}=p-1,
\qquad [KE:E]\le[K:\mathbb Q]<p-1,
\]

a contradiction. No assumption that \(p\) is unramified in \(K\) is required.

**Descent from complex coefficients.** Clear the finitely many rational-function denominators in an alleged eventual \(\mathbb C(n)\) recurrence. Its polynomial coefficients have some common degree bound \(R\), leaving finitely many complex unknown coefficients. For each integer \(n\ge n_0\), the relation is one homogeneous row whose entries are \(n^kz_{n+j}\), all algebraic. The span of these infinitely many rows over \(\overline{\mathbb Q}\) has a finite basis. Its rank over \(\mathbb C\) is the same, as witnessed by its algebraic minors. A nonzero complex nullvector therefore implies a nonzero \(\overline{\mathbb Q}\) nullvector for the finite basis. Since every original row is an algebraic linear combination of the basis rows, that nullvector solves **every** eventual constraint. Its finitely many algebraic coordinates generate one number field \(K\), reducing to the preceding contradiction.

The last nonzero shift must be selected **again after this descent**; it need not be the same as for the initial complex nullvector. Avoiding its finitely many polynomial roots is legitimate because the fresh-prime indices are unbounded. The case \(h=0\) is excluded: it gives the constant sequence and is a direct countermodel to an unqualified formulation.

This theorem excludes finite linear recurrences with rational-function coefficients. It does not exclude nonlinear iteration, arbitrary computable coefficient sequences, useful finite approximations, or an eventual cancellation estimate. In particular, non-P-recursiveness alone supplies no Weyl-sum bound.

### 10. Scope of the reasoning algebra

For finite horizons and exact rational source data, expanding Green operators into their defining finite sums and collecting polynomial coefficients is a sound normalization route. A floor can be evaluated on an exact rational value, or on a certified region that avoids integer seams. Characters can be reduced modulo integers only after the necessary lift residues have been retained. Source variables stay shared when the original expression shares them.

These rules are a constructive finite typed algebra. A claim of complete or confluent rewriting for arbitrary analytic expressions would require a declared grammar, orientation, termination argument, and analysis of critical pairs. No such broader claim is made. Allowing both expansion and inverse compaction as unrestricted rewrite steps does not supply termination. Convergence domains in (A11)–(A13) are necessary preconditions to infinite interchange, not optional annotations.

## Executed independent probe and raw receipt summary

The command was run successfully with exit code zero:

```sh
python research/2026-11-15/bbp_volume_algebra/independent_audit.py
```

The script imports no production SUCC module, uses only integer/Fraction arithmetic, and has no random seed. Its full JSON is emitted to standard output for replay; the following are the actual scope counts, not a universal proof by enumeration.

| Instrument | Actual count or scope | Verdict |
|---|---:|---|
| Seeded graded Green product | 23,814 identities; seven bases, three seeds per factor, three tape pairs, horizons 0–17 | PASS |
| Gamma convolution | 208 exact coefficient identities | PASS |
| Additive carry cocycle | 64 triples | PASS |
| Affine crossed carry | 4,500 block/state cases, each checked at three integer lifts | PASS |
| Original BBP chronological blocks | 1,330 exact identities | PASS |
| Gamma carry denominators | 820 coefficient checks; 120 explicit fixed-modulus counterexamples | PASS |
| Raw-source Gamma growth | 72 positive-term comparisons, each next term greater than eight times its predecessor | PASS |
| Retained-tail independent polynomial integration | 240 exact integrals | PASS |
| Finite Green tail boundary | 240 exact nonzero boundary receipts | PASS |
| Positive tempered geometric enclosure | 136 checks | PASS |
| Critical integer-shape partial identity | 68 checks | PASS |
| Critical half-shape partial identity | 256 checks; terms decrease while partial sums obey (A14) | PASS |
| Deliberately false rewrites | All eleven declared mutations rejected | PASS |

The two retained-tail routes share the mathematical source polynomial, which is required for a source-preserving comparison, but differ in implementation: one sums the explicit four-pole rational source; the other expands and integrates the polynomial coefficients directly without calling that source function or the tail-sum function. This is implementation independence, not independent provenance of the underlying BBP formula.

**Next verdict-changing tests.** Any proposed extension must first survive the exact source/carry and domain mutants above. A claimed asymptotic signed cancellation result then needs its own bound on the original shared source phase; none of these finite receipts substitutes for it. A claimed larger symbolic normal form needs a precise grammar and a proof that every proposed rewrite preserves its boundary, dependence, and convergence domain.
