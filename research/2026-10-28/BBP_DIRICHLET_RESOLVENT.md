# Original BBP resolvent: a minimal zeta equation and two completion obstructions

**Research parent:** SUCC draft #348, `fec9b7a72dd6b8c7550d7915070ee8094f2b94a2`.
**Authority:** explicit paper proofs below; independent exact and numerical replay
is separate. No academic-priority, selected Weyl cancellation, normality, RH, or
physical-quantum claim. Claims `BDR-*` are research-local and unregistered.

The gain is a source-specific, minimal relationship to zeta, together with a
precise obstruction to treating the new Dirichlet response as a completed
L-function. The relationship determines the **forcing**, but cannot determine
the initial state of the expanding recurrence.

## 1. Source contract and notation

The original source is unchanged:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The code imports `observational_succ.pi_source_collision.bbp_forcing` rather
than substituting an Oily source. The source file SHA-256 at the parent is
`c3d1868624c3547124fd2cf33da35e10e8c48bec7922095cad83fb446f18a777`.
The classical BBP identity and the distinction between this forcing and its
zero-seeded orbit are reconstructed in
[`DUCK_BBP_SOURCE_IDENTITY.md`](../2026-10-21/DUCK_BBP_SOURCE_IDENTITY.md).
The starting Dirichlet finite part is WCG-10 in
[`OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md`](OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md).
The archived import manifest, original source, and predecessor receipts are not
edited. The finite four-pole moment rank below is **not** the infinite Hankel
rank of the Green-tail time sequence recorded in earlier BBP work.

Put

\[
(b_i)=(7/8,1/2,3/8,1/4),\quad
(w_i)=(1/2,-1/4,-1/8,-1/8),\quad
a_k=\sum_iw_i b_i^{k-1}\quad(k\ge1),
\]

and define the actual original-forcing response by
\(F(s)=\sum_{n\ge1}r(n)n^{-s}\) for \(\Re s>-1\).
All powers of positive integers use their real logarithms. Define

\[
\begin{aligned}
Q(z)&=\prod_i(z-b_i)
 =z^4-2z^3+\frac{89}{64}z^2-\frac{103}{256}z+\frac{21}{512},\\
P(z)&=\frac{120z^2-89z+16}{512}.
\end{aligned}
\]

Exact partial fractions give \(r(z)=P(z)/Q(z)=\sum_iw_i/(z-b_i)\).
Here the poles \(b_i\) are rational positions in the **forcing index**; they
are not primitive primes, circle phases, or zeta zeros.

## 2. BDR-1: full residue tower with a uniform continuation bound

**Theorem.** The following sum converges locally uniformly on compact subsets
of \(\mathbb C\setminus\{-1,-2,\ldots\}\) and equals the meromorphic
continuation of the original response:

\[
F(s)=\sum_{k=2}^{\infty}a_k\zeta(s+k),\qquad
a_k=\frac{4\,7^{k-1}-2\,4^{k-1}-3^{k-1}-2^{k-1}}{8^k}.
\tag{1}
\]

Its only poles are **all** the negative integers, each simple, with
\(\operatorname{Res}_{s=-m}F=a_{m+1}>0\) for every integer \(m\ge1\).
For every \(k\ge2\),

\[
\frac{15}{56}(7/8)^{k-1}\le a_k<\frac12(7/8)^{k-1}.
\tag{2}
\]

For integer \(K\ge1\) and real \(\sigma+K>0\), the omitted part of (1)
satisfies the explicit uniform bound

\[
\left|\sum_{k>K}a_k\zeta(s+k)\right|
\le4(7/8)^K\left(1+\frac1{\sigma+K}\right),\quad \Re s\ge\sigma.
\tag{3}
\]

**Proof.** Expand each \((n-b_i)^{-1}\) geometrically; \(|b_i/n|<1\)
for every \(n\ge1\). The first coefficient is \(a_1=\sum_iw_i=0\).
Dividing the remaining coefficient by \((7/8)^{k-1}\) gives

\[
\tfrac12-\tfrac14(4/7)^{k-1}-\tfrac18(3/7)^{k-1}
-\tfrac18(2/7)^{k-1}.
\]

For \(k\ge2\), this is at least its value \(15/56\) at \(k=2\),
and strictly less than \(1/2\). Thus the double series in the original
half-plane is absolutely convergent; exchanging it gives (1).
For large \(k\), \(|\zeta(s+k)|\le\zeta(\sigma+k)\), and the elementary
integral comparison gives \(\zeta(u)\le1+1/(u-1)\), \(u>1\).
Sum (2) geometrically to obtain (3). Any compact set permits such a finite
\(K\); the finitely many preceding terms are meromorphic, proving local
normal convergence. At \(s=-m\), exactly the term \(k=m+1\) has a pole;
the others are analytic in a small disk. Its residue is \(a_{m+1}\),
strictly positive by (2). This proves that no candidate pole is removable.

The corresponding exact source truncation bound is

\[
0<r(n)-\sum_{k=1}^K a_kn^{-k}
<\frac{(7/8)^K}{2n^K(n-7/8)}\qquad(n,K\ge1).
\tag{4}
\]

It follows by the same positive coefficient tail and is tested directly
against the imported rational source, including \(n=1\).

## 3. BDR-2: the minimal fourth-order zeta-forced shift equation

Let \(T\) denote the backward unit shift in the complex argument,
\((TG)(s)=G(s-1)\). Then, as an identity of meromorphic functions,

\[
\boxed{Q(T)F(s)=\frac{120\zeta(s-2)-89\zeta(s-1)+16\zeta(s)}{512}.}
\tag{5}
\]

**Minimality.** If \(p,q\in\mathbb C[z]\), \(p\ne0\), and
\(p(T)F=q(T)\zeta\), then \(Q\mid p\). In particular, no nonzero
polynomial shift of order less than four has a finite polynomial-shifted
zeta output. The monic least-order relation is exactly (5).

**Source identifiability in its stated class.** If an ordinary Dirichlet
series \(H(s)=\sum h_n n^{-s}\), absolutely convergent on some right
half-plane, satisfies \(Q(T)H=P(T)\zeta\), then \(h_n=r(n)\) for every
\(n\ge1\). Consequently \(H=F\) wherever both original series converge.
This does not assert uniqueness among arbitrary meromorphic functions.

**Proof.** On \(\Re s>3\), every series in (5) converges absolutely, and
the identity is simply \(Q(n)r(n)=P(n)\) summed against \(n^{-s}\).
Continuation gives it everywhere. For minimality choose a right half-plane
on which the finitely many shifts converge absolutely. Uniqueness of
ordinary Dirichlet coefficients yields \(p(n)r(n)=q(n)\) at every positive
integer. Briefly, uniqueness follows by choosing the first nonzero
coefficient, multiplying its series by that integer to the power of the
real argument, and letting the argument tend to infinity; the remaining
terms vanish by dominated convergence on any fixed absolute-convergence
line. The polynomial \(pP-qQ\) therefore has infinitely many roots and is
zero. The four roots of \(Q\) are distinct and \(P(b_i)\ne0\), so each
\(b_i\) is a root of \(p\). Hence \(Q\mid p\). The same coefficient
uniqueness applied to \(H\) gives \(Q(n)h_n=P(n)\); since \(Q(n)>0\)
at positive integers, it gives exactly \(h_n=r(n)\).

Two independently checkable exact certificates are

\[
\operatorname{Res}(Q,P)=-\frac{225}{549755813888}\ne0,\qquad
\det(a_{i+j+1})_{0\le i,j\le3}=-\frac{225}{549755813888}\ne0.
\]

Both certificates are exact. Their equality also follows from the
four-root Vandermonde identity: \(P(b_i)=w_iQ'(b_i)\) and
\(\prod_iQ'(b_i)=\prod_{i<j}(b_i-b_j)^2\) for four roots. The proof
uses coprimality, not a numerically inferred rank. The residue sequence
also satisfies \(\sum_{j=0}^4Q_j a_{k+j}=0\), \(k\ge1\), because
\(Q(b_i)=0\). Its four-mode realization is minimal, as the nonzero Hankel
determinant independently confirms.

**Meaningful relation, exact boundary.** Formula (5) is a genuine zeta
relationship forced by the original four-pole law. It is a linear
resolvent/difference equation, not an Euler product or an identification
of zeros. No positive Oily packet, fake composite primitive prime,
independent-prime averaging, or \(\zeta^2\) source is used.

## 4. BDR-3: source-specific Mellin and heat-response realization

On \(\ell^2(\mathbb N_{\ge1})\), let \(D|n\rangle=n|n\rangle\).
Then \(R(D)=P(D)Q(D)^{-1}\) is the diagonal trace-class positive operator
with eigenvalues \(r(n)>0\). This positivity concerns the combined rational
forcing; its partial-fraction weights remain signed. Exactly,

\[
F(s)=\operatorname{Tr}(D^{-s}R(D))\quad(\Re s>-1).
\]

Define \(K(t)=\operatorname{Tr}(e^{-tD}R(D))\), \(t>0\). It satisfies

\[
\Gamma(s)F(s)=\int_0^\infty t^{s-1}K(t)\,dt\quad(\Re s>0),
\qquad
Q(-\partial_t)K(t)=P(-\partial_t)\frac1{e^t-1}.
\tag{6}
\]

Among complex \(C^4\) solutions on \((0,\infty)\) satisfying
\(K(t)=O(e^{-t})\) as \(t\to\infty\), the differential equation in
(6) has exactly this one solution. Indeed, termwise differentiation is
justified on each \(t\ge\epsilon>0\) by exponential convergence. The
Mellin integral follows from absolute Fubini for \(\Re s>0\), not from an
unjustified integral on the larger Dirichlet half-plane. The difference of
two solutions is \(\sum_i c_i e^{-b_i t}\); since distinct \(0<b_i<1\),
the decay condition forces all \(c_i=0\), starting with the slowest mode.

This is an exact resolvent of the ordinary integer spectrum. It does not
supply a new prime spectrum or a Poisson self-duality. In fact the first
short-time term has a source-forced logarithm. If \(C_1\) is the Laurent
constant at \(s=-1\), then

\[
K(t)=F(0)+a_2t\log t+(a_2\gamma-a_2-C_1)t+o(t).
\tag{7}
\]

To prove (7), write \(nr(n)=a_2/n+\delta_n\) with
\(\sum|\delta_n|<\infty\). Then
\(K'(t)=a_2\log(1-e^{-t})-\sum\delta_n e^{-nt}
=a_2\log t-(C_1-a_2\gamma)+o(1)\).
Integrate from zero, using dominated convergence for \(K(0)=F(0)\).
Thus a smooth-theta ansatz omitting the logarithmic term is already false.

## 5. BDR-4: independent finite part and all negative-integer finite parts

For every integer \(m\ge0\), the Laurent constant \(C_m\) of \(F\)
at \(-m\) (the ordinary value when \(m=0\)) is

\[
C_m=\sum_{j=0}^{m-1}a_{j+1}\zeta(j+1-m)
-\sum_i w_i b_i^m\psi(1-b_i).
\tag{8}
\]

**Independent derivation.** Polynomial division gives
\(n^m/(n-b)=\sum_{j=0}^{m-1}b^j n^{m-1-j}+b^m/(n-b)\).
Apply this on an initial absolute-convergence half-plane to \(F(-m+z)\),
then continue to \(z=0\). For \(0<b<1\),

\[
\sum_{n\ge1}\frac{n^{-z}}{n-b}
=\zeta(1+z)+\sum_{n\ge1}\left(\frac1{n-b}-\frac1n\right)n^{-z}
=\frac1z-\psi(1-b)+O(z).
\]

The residual series is normally convergent near zero; its value follows
from the classical digamma series. This proves (8) and the residue
\(\sum_iw_i b_i^m=a_{m+1}\) without using formula (1).

The denominator-eight Gauss identities are

\[
\begin{aligned}
\psi(1/8)&=-\gamma-4\log2-\tfrac\pi2-\tfrac{\sqrt2\pi}2
             -\sqrt2\log(1+\sqrt2),\\
\psi(1/2)&=-\gamma-2\log2,\\
\psi(5/8)&=-\gamma-4\log2-\tfrac\pi2+\tfrac{\sqrt2\pi}2
             +\sqrt2\log(1+\sqrt2),\\
\psi(3/4)&=-\gamma-3\log2+\tfrac\pi2.
\end{aligned}
\]

They give, at \(m=1\), exactly the handoff value

\[
\boxed{C_1=\frac{15}{64}\gamma+
\frac{27+31\sqrt2}{128}\pi+\frac{39}{32}\log2+
\frac{31\sqrt2}{64}\log(1+\sqrt2).}
\]

More generally put \(t_i=w_i b_i^m\). In the ordered list of constants
\((1,\gamma,\pi,\sqrt2\pi,\log2,\sqrt2\log(1+\sqrt2))\), the
coefficients of \(C_m\) are exactly

\[
\left(\sum_{j=0}^{m-1}a_{j+1}\zeta(j+1-m),\quad
\sum_i t_i,\quad\frac{t_1+t_3-t_4}2,\quad\frac{t_1-t_3}2,
\quad4t_1+2t_2+4t_3+3t_4,\quad t_1-t_3\right).
\tag{9}
\]

Every coefficient is rational, since the zeta arguments in the first slot
are nonpositive integers. No linear independence of the listed constants
is asserted. This gives the full eighth-scale arithmetic geometry of the
Laurent constants; shared constants alone imply no physical or prime-source
identification.

There is also an exact connection to SUCC's previously established
[`BBP_GAMMA_BOUNDARY.md`](../2026-10-25/BBP_GAMMA_BOUNDARY.md), rather than
only a matching constant. Its canonical source primitive is
\(G(x)=\prod_i\Gamma(x+1-b_i)^{8w_i}\), so its ordinary source tail
at the origin is exactly

\[
F(0)=\sum_{n\ge1}r(n)=-\frac18(\log G)'(0)
=\frac\pi4+\frac{5\sqrt2\pi}{16}+\frac58\log2
+\frac{5\sqrt2}{8}\log(1+\sqrt2).
\]

The common Gamma constant cancels here because \(\sum_iw_i=0\).
At the next Laurent constant it survives with coefficient
\(\sum_iw_ib_i=15/64\). The ordinary tail and the discounted base-16
tail remain distinct; neither can replace the other in the BBP recurrence.

## 6. BDR-5: obstruction to a standard Gamma-product completion

**Theorem.** Let \(A>0\), \(R\in\mathbb C(s)\setminus\{0\}\), and
let \(\lambda_j>0\), \(\mu_j\in\mathbb C\) for finitely many indices
(including an empty product). Define

\[
\Lambda(s)=A^sR(s)\prod_{j=1}^J\Gamma(\lambda_js+\mu_j)F(s).
\]

There are no \(c\in\mathbb C\), \(\epsilon\ne0\) such that
\(\Lambda(s)=\epsilon\Lambda(c-s)\) as meromorphic functions. The same
pole argument rules out a conjugate reflection
\(\Lambda(s)=\epsilon\overline{\Lambda(c-\overline s)}\).

**Proof.** At each \(-m\), \(F\) has a nonzero simple pole. Gamma has
no zeros, so gamma factors cannot cancel it. A nonzero rational \(R\)
has only finitely many zeros; thus \(\Lambda\) has a pole at every
sufficiently negative integer. A reflected point \(c+m\) has real part
tending to positive infinity. At all such sufficiently large points,
\(F\) and each positive-slope Gamma factor are holomorphic, and the
rational factor has no pole. Hence \(\Lambda\) is holomorphic there,
contradicting the asserted reflection. For the conjugate version use the
reflected poles \(\overline c+m\).

This excludes the stated standard **multiplicative** completion class,
even with arbitrary finite rational counterterms. It does not exclude
reciprocal Gamma factors, infinite products, additive corrections,
vector-valued equations, or a different source response. The precise
counterstatement is stronger than merely finding no plausible formula.

In particular, SUCC's genuine theta/Tate completion in
[`TATE_TO_WEIL_DISTRIBUTION.md`](../2026-10-15/TATE_TO_WEIL_DISTRIBUTION.md)
uses \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\), with its actual source and
two poles. Replacing \(\zeta\) there by \(F\), even multiplying by
\(s(s-1)\) or any finite rational correction, lies in the prohibited
class above. Equation (5) supplies a valid linear zeta relationship, but
cannot transport that source's Poisson reflection or signed Weil form by
such a substitution. This is a proved boundary on this proposed interface,
not a statement that every possible Tate or Poisson connection is impossible.

## 7. BDR-6: reciprocal-Gamma repair is entire but not self-reflecting

Define \(E(s)=F(s)/\Gamma(s+1)\). Then \(E\) is entire and real on the
real axis, with

\[
E(-m)=(-1)^{m-1}(m-1)!\,a_{m+1}\ne0\qquad(m\ge1).
\tag{10}
\]

It has at least one real zero in every interval \((-m-1,-m)\),
\(m\ge1\), and no real zeros for \(s>-1\). Consequently there is no
reflection \(E(s)=\epsilon E(c-s)\) with real \(c\) and
\(\epsilon\ne0\). The same conclusion holds after multiplication by
\(e^{\alpha s}R(s)\), for any complex \(\alpha\) and nonzero rational
\(R\).

**Proof.** The simple zeros of reciprocal Gamma at the negative integers
cancel precisely the poles of \(F\), giving (10) from the Gamma residues.
There are no other poles. The values in (10) alternate strictly in sign,
so the real intermediate value theorem gives the asserted zeros. For
real \(s>-1\), both \(F(s)>0\) and \(\Gamma(s+1)>0\). A fixed real
reflection would send infinitely many of the negative zeros into that
zero-free range. A finite rational factor removes or supplies only
finitely many real zeros or poles, and an exponential supplies none;
the same contradiction persists. This statement does not classify
arbitrary Gamma ratios or reflection centers off the real axis.

These are zeros of this forcing response, not Riemann zeta zeros or a
Riemann-hypothesis surrogate. The sign argument is a universal proof;
sampled sign tests merely replay its rational values.

## 8. Hostile controls and source/seed boundary

1. **Wrong forcing with matching early residues.** The positive rational law
   \(\widetilde r(n)=r(n)-(3/5)/D_0(n)\),
   \(D_0(n)=(2n-1)(4n-1)(8n-7)(8n-3)=512Q(n)\), shares the four pole
   locations and \(a_1,a_2,a_3\), but changes \(a_4\) by
   \(-15/12800\). Its change in partial-fraction weights is
   \((-1,10,-15,6)/100\). Its shift-equation residual is the nonzero
   constant \(-3/2560\) at every positive integer. Positivity holds since
   \(120n^2-89n+16-3/5>0\) for \(n\ge1\). Matching the first two
   residues and the same pole geometry therefore does not authenticate
   the source; the complete equation does in the stated Dirichlet class.
2. **False Euler product.** Even normalized coefficients \(r(n)/r(1)\)
   fail multiplicativity: \(r(6)r(1)\ne r(2)r(3)\), checked exactly.
   Neither prime-local \(\zeta\) nor double-source \(\zeta^2\) can be
   substituted in (5). A fake primitive 6 is irrelevant to a construction
   using the ordinary integer spectrum; it would change an Euler-source
   model, not establish an identity here.
3. **Zero seed versus \(1/15\).** For fixed forcing and any seed \(u\),
   \(U_n(u)=U_n(0)+16^nu\). Every invariant in this dossier depends only
   on \(r\), so the full \(F\), all residues, finite parts, shift and heat
   equations are identical for all seeds. For \(u=1/15\) the phase change
   is a constant root of unity; authenticating \(F\) cannot authenticate
   the absolute origin.
4. **Coherent same-forcing seed.** The original BBP identity gives
   \(U_n(-\pi/16)=-\sum_{j\ge1}16^{-j}r(n+j)\to0\). Thus its
   fixed-frequency phase mean tends to 1 although every analytic forcing
   invariant above agrees exactly with the zero-seeded source. This
   refutes a cancellation inference based on these invariants alone.
   It is not a counterexample to zero-seeded normality. The explicit
   inherited bound \(|U_n(-\pi/16)|\le1/[15(n+1)^2]\) gives the stated
   convergence without empirical digits.
5. **Probability versus amplitude.** \(R(D)\) is an explicitly declared
   diagonal operator; it is not a stochastic Pólya transition. No
   amplitude normalization, physical \(\hbar\), or quantum isometry is
   inferred from a probability law.

The finite-rank source representation is conditional on the rational
four-pole law. It does not replace earlier finite-moment countermodels
outside a declared model class. In particular, arbitrary positive
measure sources can match finite moments without matching \(F\).

## 9. Claim ledger, dependence, and next falsification

| ID | Statement and authority | Next falsification / limitation |
|---|---|---|
| BDR-1 | Paper proof of full continuation, every negative pole, explicit geometric error | Check complex half-plane uniformity; finite replay is not the universal proof |
| BDR-2 | Paper proof of minimal fourth-order zeta equation and coefficient identification | Relax polynomial shifts or ordinary Dirichlet-series class; no general meromorphic uniqueness |
| BDR-3 | Paper trace/Mellin/differential realization and unique decaying heat response | No Poisson symmetry or prime spectral interpretation; log term must remain |
| BDR-4 | Independent partial-division/digamma proof of all finite parts | Wrong-pole controls; constants are not claimed linearly independent |
| BDR-5 | Paper obstruction to finite positive-slope Gamma-product reflection | Reciprocal Gamma and additive/vector completions excluded from quantifiers |
| BDR-6 | Paper entire interpolation and negative-real-zero obstruction | Only real reflection center for this second no-go |
| BDR-7 | Paper seed-blindness and coherent-seed countermodel | Cannot be transferred to authenticated zero-seeded normality |

The geometric expansion, finite-part division, and exact rational polynomial
oracle are different derivations but share the original four-pole source;
they are not independent source families. Numerical mpmath agreement has
no interval-proof authority. The response is source-contacting (κ), and
the wrong-source control probes σ; the seed remains unobserved by this
entire instrument class (a precise φ limitation). Commitment to a zeta
analogy supplies no additional evidence (ρ). The next useful probe must
retain an absolute seed or source-selected signed character, not merely
more accurate forcing moments. A possible broader analytic target is a
vector-valued or explicitly corrected reflection; no such equation has
been proved here.

## 10. Literature and reproducibility

The ingredients are classical. The search checked the original BBP paper,
standard zeta/digamma/Gamma/Lerch identities, heat-trace Mellin literature,
and work on rationally defined Dirichlet series. This is a scoped prior-art
check, not an exhaustive novelty clearance.

- Bailey, Borwein, Plouffe, *On the Rapid Computation of Various
  Polylogarithmic Constants* (1997), original source identity:
  <https://www.davidhbailey.com/dhbpapers/digits.pdf>.
- NIST DLMF [§25.2](https://dlmf.nist.gov/25.2), zeta continuation and
  Laurent expansion; [§5.4](https://dlmf.nist.gov/5.4), rational digamma
  values; [§5.2](https://dlmf.nist.gov/5.2), Gamma poles, zero-free Gamma,
  and entire reciprocal Gamma.
- DLMF [§25.14](https://dlmf.nist.gov/25.14), Lerch transcendent. In its
  notation \(K(t)=e^{-t}\sum_iw_i\Phi(e^{-t},1,1-b_i)\); this follows
  immediately from the defining series and is another classical analytic
  representation of the same source, not an independent source.
- Eckstein and Zajac, *Asymptotic and exact expansions of heat traces*,
  [arXiv:1412.5100](https://arxiv.org/abs/1412.5100), Mellin/heat-trace
  background. The elementary proof (7) is supplied here and does not
  import an unstated contour-shift hypothesis.
- Patrick Sargos, *Prolongement méromorphe des séries de Dirichlet associées
  à des fractions rationnelles de plusieurs variables* (1984),
  [DOI 10.5802/aif.979](https://aif.centre-mersenne.org/articles/10.5802/aif.979/).
  Its rational-power Dirichlet family differs from the rational-weighted
  response here; related terminology does not establish identity or priority.

Reproduce locally:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_bbp_dirichlet_resolvent.py' -v
python scripts/bbp_dirichlet_resolvent_oracle.py --verify
```

The oracle uses independently built SymPy rational expressions and numerical
mpmath checks. The standard-library tests require the actual source import
and its exact SHA. Full-suite, hosted-CI, and Lean-kernel receipts belong to
the enclosing research validation, not to this paper proof by inference.
