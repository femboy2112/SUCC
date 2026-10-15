# Tate's idelic Mellin transform through the SUCC source interfaces

**Status:** CLASSICAL THEOREMS, rederived below; new source-interface integration
and exact finite models, without an academic-priority claim.

## Abstract and scope

The adelic Poisson interface already proved in this branch determines an
explicit linear map from the full Schwartz–Bruhat space on the rational adeles
to meromorphic functions. We construct its idelic quotient, derive the measure
normalization, unfold the integral, and obtain its poles and functional
equation. The standard Gaussian/integer-ball source maps to
\(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\). Its original local valuation
shells produce the Euler factors; differentiating those factors in their
absolute-convergence domain produces exactly the prime-power logarithmic
coefficients. The implemented rational charts commute with diagonal scaling,
local Fourier tests, and the inherited theta evaluator. Explicit rational
remainder bounds accompany finite truncations.

These are mathematical source declarations. They are not certificates that a
physical observer has measured all places, and they give no positivity theorem
for the signed Weil form.

## 1. Dependencies, convention and provenance

Work relative to the classical locally compact groups
\(\mathbb A=\mathbb R\times\mathbb A_f\) and
\(I=\mathbb A^\times=\mathbb R^\times\times\prod'_p
(\mathbb Q_p^\times,\mathbb Z_p^\times)\), with the **restricted-product
idele topology**, not the subspace topology from the adeles. Write
\(C=I/\mathbb Q^\times\). The additive Fourier conventions inherited from
`adelic_poisson_reconstruction.py` are real plus and finite minus:

\[
 \psi_\infty(x)=e^{2\pi ix},\qquad
 \psi_p(x)=e^{-2\pi i\{x\}_p},\qquad
 \widehat\Phi(y)=\int_{\mathbb A}\Phi(x)\psi(xy)\,dx.
\]

Take \(dx_\infty\) Lebesgue and \(\operatorname{vol}(\mathbb Z_p)=1\).
The preceding notes establish self-duality, diagonal annihilator
\(\mathbb Q^\perp=\mathbb Q\), covolume one, and Poisson for every
\(\Phi\in\mathcal S(\mathbb A)\). We use that theorem, standard Haar
integration, Tonelli/Fubini and locally uniform complex integration. Their
universal conclusions do not follow from this module's finite tests.

External references, checked against the online texts on 2026-10-15:

1. J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*,
   Princeton thesis, 1950, §§2.3, 3.3, 4.2–4.4, especially Main Theorem 4.4.1;
   [original thesis scan](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf).
   Reprinted in Cassels–Fröhlich, *Algebraic Number Theory* (1967), pp. 305–347.
   The original character is the conjugate of ours at **all** places; this
   changes no self-duality or Poisson assertion when transported consistently.
2. B. Poonen, *Tate's thesis*, MIT 18.786 notes (Spring 2015), §1.4, Theorems
   5.7 and 5.16, Lemmas 5.18–5.19, and §5.11;
   [author's notes](https://math.mit.edu/~poonen/786/notes.pdf).
   These locate the classical analytic statements and zero-mode normalization.

This note supplies the proofs used here rather than asserting authority as
verification. It does not reproduce either text. Source code dependencies are
`all_places_zeta.py`, `tate_schwartz_functor.py`,
`adelic_poisson_reconstruction.py`, and their prime/product-formula helpers.
`provenance/IMPORT_MANIFEST.json` was inspected; no archival import is modified.
The new files are an extension, not a parallel replacement of the theta code.

## 2. The idelic source and its quotient

### TZ-01. Canonical quotient coordinates and Haar normalization

**Domain:** all ideles, not just the executable rational charts.

Every \(x\in I\) has a unique expression

\[
 x=q(r,u),\quad q\in\mathbb Q^\times,\quad r>0,
 \quad u\in\widehat{\mathbb Z}^{\times},
 \qquad r=|x|_{\mathbb A}.
\]

**Proof.** Only finitely many \(v_p(x_p)\) are nonzero. Put
\(q=\operatorname{sgn}(x_\infty)\prod_p p^{v_p(x_p)}\),
\(u_p=x_p/q\), and \(r=x_\infty/q\). Every \(u_p\) is a unit and
the product formula gives \(r=|x|\). If two such decompositions exist,
their rational ratio has zero valuation at every prime, hence is \(\pm1\);
the positive real coordinate forces \(+1\). The valuation and sign maps
are locally constant in the restricted-product topology, so this gives a
homeomorphism \(I\simeq\mathbb Q^\times\times\mathbb R_{>0}\times
\widehat{\mathbb Z}^{\times}\), with the rational factor discrete. In
particular \(C\simeq\mathbb R_{>0}\times\widehat{\mathbb Z}^{\times}\).

Normalize multiplicative Haar by

\[
 d^\times x_\infty=\frac{dx_\infty}{|x_\infty|},\qquad
 d^\times x_p=\frac{dx_p}{(1-p^{-1})|x_p|_p}.
\]

Indeed the additive volume of \(p^k\mathbb Z_p^\times\) is
\(p^{-k}(1-p^{-1})\), so each multiplicative valuation shell has mass
one. Their restricted product exists with unit-group mass one. The rational
factor above has counting measure; the other factors have \(dr/r\) and
probability Haar \(du\). On each fixed rational cell the real sign is
already fixed and the product measure is \(dr/r\,du\). Thus quotient
measure is exactly \(d^\times c=dr/r\,du\), with
\(\operatorname{vol}(C^1)=1\). ∎

**Normalization audit receipt.** A preliminary interpretation in this research
round incorrectly put \(2dr/r\,du\) on the quotient. The disjoint rational
cells above refute it: the two signs already occur in the counting measure on
\(\mathbb Q^\times\). For the Gaussian they occur again visibly as the
two orbit terms \(n\) and \(-n\), not as a second Haar multiplier.
Keeping both an extra quotient multiplier and the signed orbit would double
the Gamma factor and both residues. The correction is covered by exact
Gamma/orbit tests and an independent norm-variable quadrature.

**Executable map.** `RationalChartIdele` declares a nonzero rational real
coordinate, a common nonzero rational finite default and finitely many
prime-indexed overrides. It is closed under diagonal rational multiplication.
`quotient()` computes the formula above; `unit_residue(p,k)` computes the
normalized unit modulo \(p^k\); `reconstruct()` is its exact inverse on the
chart. These routines do not represent every p-adic unit or every real number.

### TZ-02. Source test and exact orbit support

Define the genuine Schwartz–Bruhat function

\[
 \Phi_0(x)=e^{-\pi x_\infty^2}\prod_p1_{\mathbb Z_p}(x_p).
\]

The product is a restricted-tensor declaration: an adele is integral at all but
finitely many primes, so evaluating its indicator requires only its exceptional
coordinates. \(\widehat\Phi_0=\Phi_0\) because the Gaussian and every
integer-ball indicator are self-dual with the fixed additive measures.
For \(u\in\widehat{\mathbb Z}^{\times}\),

\[
 \Phi_0(q(r,u))\ne0\ \Longleftrightarrow\ q\in\mathbb Z\setminus\{0\},
 \qquad
 \Theta^*_{\Phi_0}(r,u)=\sum_{q\ne0}\Phi_0(q(r,u))
 =2\sum_{n\ge1}e^{-\pi n^2r^2}.
\]

The equivalence follows from \(v_p(qu_p)=v_p(q)\) at every prime; a rational
integral at every prime is an integer. No zero of an L-function appears.
`StandardTateSource` sends the same source identity/epoch to the existing
`GaussianPoissonGenerator(RationalCoset(0,1))` and all `PadicBall(p,0,0)`.
`rational_orbit_exponent` computes the displayed support and exact Gaussian
exponent on its rational chart, rejecting a source/epoch mismatch.

## 3. Local shells, global integral and authentic coefficients

### TZ-03. Full idelic Mellin integral in its original domain

For \(\Re s>1\),

\[
 \mathcal M\Phi_0(s):=\int_I\Phi_0(x)|x|^s\,d^\times x
 =\Gamma_{\mathbb R}(s)\prod_p(1-p^{-s})^{-1}
 =\Gamma_{\mathbb R}(s)\zeta(s),\quad
 \Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2).
\]

**Proof.** At a genuine prime \(p\), decomposition into valuation shells
and TZ-01 give
\(\int_{\mathbb Q_p^\times}1_{\mathbb Z_p}(x)|x|_p^s d^\times x
=\sum_{k\ge0}p^{-ks}=(1-p^{-s})^{-1}\), already for \(\Re s>0\).
At infinity, both sign components yield
\(2\int_0^\infty e^{-\pi r^2}r^s dr/r
=\pi^{-s/2}\Gamma(s/2)\), also for \(\Re s>0\).
For the global product restrict the exceptional valuations to a finite set
of primes and then exhaust that set. For real \(s=\sigma>1\), Tonelli
and unique factorization give precisely \(\sum_{n\ge1}n^{-\sigma}<\infty\).
For complex \(s\) its absolute integrand is the corresponding integrand at
\(\sigma=\Re s\), proving absolute convergence and legitimizing Fubini.
This proves the identity on its open half-plane. ∎

`finite_euler_stage` computes a genuine finite product, preserving separately
the exact geometric shell remainder. This uses `local_mellin_shell`; it never
evaluates an all-prime product in the critical strip. Exact positive-even
Gamma values are represented as rational multiples of integral powers of
\(\pi\), exposing a missing sign factor or \(\Gamma(s)\) substitution.

### TZ-04. Quantified Euler exhaustion and logarithmic derivative

If a finite stage contains **every** prime \(p\le P\), then for
\(\Re s\ge\sigma>1\),

\[
 \left|\zeta(s)-\prod_{p\le P}(1-p^{-s})^{-1}\right|
 \le\sum_{n>P}n^{-\sigma}\le\frac{P^{1-\sigma}}{\sigma-1}.
\]

Indeed the stage is the sum over integers with all prime factors at most
\(P\); any omitted integer is larger than \(P\). On positive integral
\(\sigma\ge2\), `euler_exhaustion_bound` returns an exact rational bound.
For completed zeta multiply by \(|\Gamma_{\mathbb R}(s)|\), bounded
pointwise by \(\Gamma_{\mathbb R}(\Re s)\) via its integral. There is no
assertion of one uniform Gamma bound on an unbounded right half-plane.
The stronger statement with a fixed lower-bound \(\sigma\) is refuted:
for \(\sigma=2,s=20\),
\(\Gamma_R(20)/\Gamma_R(2)=9!/\pi^9>9!/4^9>1\).
This exact witness was identified during hostile review and retained as a
regression control; it changes no Euler exhaustion estimate.

Local logarithmic differentiation gives

\[
 -\frac{d}{ds}\log(1-p^{-s})^{-1}
 =\log p\sum_{k\ge1}p^{-ks},\qquad
 -\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge2}\Lambda_{\rm ar}(n)n^{-s},
\]

where \(\Lambda_{\rm ar}(p^k)=\log p\) and it is zero elsewhere.
For every closed sub-half-plane \(\Re s\ge1+\epsilon\), absolute locally
uniform convergence follows from
\(\Lambda_{\rm ar}(n)\le\log n\) and convergence of
\(\sum\log n/n^{1+\epsilon}\). It legitimizes the derivative and also
shows that the Euler product is nonzero there. Hence

\[
 \frac{\Lambda'(s)}{\Lambda(s)}
 =\frac{\psi(s/2)-\log\pi}{2}
   -\sum_{n\ge2}\Lambda_{\rm ar}(n)n^{-s},\quad\Re s>1.
\]

For \(N\ge2\) and integral \(\sigma\ge2\), the logarithmic tail is at most

\[
 N^{1-\sigma}\left(\frac{\log N}{\sigma-1}
       +\frac1{(\sigma-1)^2}\right)
 \le N^{1-\sigma}\left(\frac{\lceil\log_2N\rceil}{\sigma-1}
       +\frac1{(\sigma-1)^2}\right).
\]

The first inequality is the integral bound for the decreasing function
\(\log x/x^\sigma\) on \([N,\infty)\); the second uses \(\log2<1\).
`log_derivative_tail_bound` returns the last rational number.
`logarithmic_coefficients` reuses the independent factorization/prime-power
cross-check in `finite_source_logjets`. In particular **the Dirichlet zeta
coefficient at 6 is one, whereas its logarithmic coefficient is zero**.
A standalone source impulse \(\log6\) at 6 cannot arise from this map.

## 4. The full typed Tate map and analytic continuation

### TZ-05. Schwartz–Bruhat transport theorem

**Domain:** the algebraic restricted tensor space
\(\mathcal S(\mathbb A)=\mathcal S(\mathbb R)\otimes
\mathcal S(\mathbb A_f)\), with finite linear sums as in the existing
rational-coset spanning theorem. For \(\Phi\) in this space set

\[
 \Theta_\Phi^*(c)=\sum_{q\in\mathbb Q^\times}\Phi(qc),\qquad
 J_\Phi(s)=\int_{|c|\ge1}\Theta_\Phi^*(c)|c|^s\,d^\times c.
\]

Then \(J_\Phi\) is entire, the original idelic integral is absolutely
convergent for \(\Re s>1\), and the **linear, source-derived map** is

\[
 \boxed{\quad
 \mathcal M:\mathcal S(\mathbb A)\longrightarrow\operatorname{Mer}(\mathbb C),
 \quad
 \Phi\longmapsto
 J_\Phi(s)+J_{\widehat\Phi}(1-s)
       +\frac{\widehat\Phi(0)}{s-1}-\frac{\Phi(0)}s .\quad}
\]

It agrees with \(\int_I\Phi(x)|x|^s d^\times x\) on \(\Re s>1\),
and \(\mathcal M\Phi(s)=\mathcal M\widehat\Phi(1-s)\).
Its possible residues are \(-\Phi(0)\) at zero and \(\widehat\Phi(0)\)
at one. It does not promise a pole where the relevant zero mode vanishes.

**Proof, including convergence.** Every finite test support lies inside
\(M^{-1}\widehat{\mathbb Z}\) for some positive integer \(M\), and its
coefficients are bounded. For \(c=(r,u)\), \(u\) a finite unit, a supported
rational \(q\) lies in \(M^{-1}\mathbb Z\). Schwartz decay therefore bounds
\(\sum_{q\ne0}|\Phi(qc)|\) by \(C_Lr^{-L}\) uniformly in \(u\),
for \(r\ge1\), for every \(L>1\). The same holds for
\(\widehat\Phi\). Choosing \(L\) larger than the real parts in a compact
\(s\)-set, with spare powers to absorb \(\log(r)^j\), proves entirety
and differentiation under the integral for \(J_\Phi\).

For \(0<r\le1\), the absolute source sum is bounded by
\(C\sum_{n\ne0}(1+r|n|/M)^{-2}\le C'/r\), by comparison with an
integral. Thus \(\int_0^1\sum|\Phi(qc)|r^\sigma dr/r<\infty\) for
\(\sigma>1\). The decomposition in TZ-01 and Tonelli/Fubini now unfold
the original integral to \(\int_C\Theta_\Phi^*(c)|c|^s d^\times c\).

Apply the previously established adelic Poisson formula to
\(x\mapsto\Phi(cx)\). Its Fourier transform is
\(|c|^{-1}\widehat\Phi(c^{-1}y)\), so

\[
 \Theta_\Phi^*(c)
 =|c|^{-1}\Theta_{\widehat\Phi}^*(c^{-1})
      +|c|^{-1}\widehat\Phi(0)-\Phi(0).
\]

Split the unfolded integral at \(|c|=1\). Invert \(c\) in the small
part. Haar measure is invariant under inversion, and the norm-one group
has volume one. The resulting two elementary integrals are
\(\widehat\Phi(0)\int_0^1r^{s-1}dr/r=\widehat\Phi(0)/(s-1)\)
and \(-\Phi(0)\int_0^1r^sdr/r=-\Phi(0)/s\). This yields the boxed
formula on the initial domain and its meromorphic extension everywhere.
Fourier inversion gives \(\widehat{\widehat\Phi}(x)=\Phi(-x)\);
the rational orbit is unchanged by \(q\mapsto-q\). Swapping the two
entire terms and zero modes proves the functional equation. ∎

**Continuity statement.** Remove the two displayed poles and give the target
entire functions the compact-open topology. On each fixed finite-adèle test
stage (fixed compact support and fixed compact-open invariance subgroup),
\(\Phi\mapsto J_\Phi(s)+J_{\widehat\Phi}(1-s)\) is continuous for
the usual Schwartz seminorms of its finitely many real coefficients. To see
this, the rapid bounds in the proof control the supremum over each compact
\(s\)-set by finitely many such seminorms; evaluation at zero and Fourier
transform are continuous as well. The finite-adèle Fourier transform sends
a fixed stage to another fixed stage. Passing to the usual inductive-limit
Schwartz–Bruhat topology proves continuity of this regularized map. This is a
typed analytic transform on an entire test space, not interpolation from
finitely many samples of one Gaussian.

**Commuting interfaces.** For \(a\in I\), define \(D_a\Phi(x)=\Phi(ax)\).
Direct substitution gives
\(\mathcal M(D_a\Phi)(s)=|a|^{-s}\mathcal M\Phi(s)\), initially by
absolute convergence and then meromorphically. On diagonal rational \(a\)
the multiplier is one by the product formula; the implemented chart quotient
is invariant under exactly this action. Fourier exchanges \(s\) and \(1-s\)
in the boxed map. Additive SUCC translations remain lawful operations on
Schwartz–Bruhat tests, but they do **not** satisfy this multiplicative Mellin
eigencharacter law. No such false translation intertwiner is asserted.

### TZ-06. Completed zeta, its zero modes and the independent theta route

For \(\Phi_0=\widehat\Phi_0\), put \(t=r^2\) and
\(\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}\). TZ-02 and
\(dr/r=dt/(2t)\) give

\[
 \Lambda(s)=\frac1{s(s-1)}+I(s)+I(1-s),\qquad
 I(s)=\sum_{n\ge1}\int_1^\infty e^{-\pi n^2t}t^{s/2}\frac{dt}{t}.
\]

The two residues are exactly \((-1,+1)\); \(\Lambda(s)=\Lambda(1-s)\).
Equivalently \(\xi(s)=\tfrac12s(s-1)\Lambda(s)\) is entire with
\(\xi(0)=\xi(1)=1/2\). Dividing by \(\Gamma_{\mathbb R}\) gives
the usual continuation of \(\zeta\): only the simple pole at one remains.
The Gamma poles at zero and the negative even integers are handled by this
quotient, not inserted as independent Euler sources.

**Independent mathematical route:** ordinary real Poisson on the Gaussian
gives \(\theta(t)=t^{-1/2}\theta(1/t)\). Its Mellin integral
\(\int_0^\infty(\theta(t)-1)t^{s/2}dt/(2t)\), split at one, yields
the identical displayed formula, with the two endpoint integrals giving
\(1/[s(s-1)]\). This route and the idelic quotient/unfolding route have
different normalizing interfaces but share the classical real Poisson input;
they are not provenance-independent discoveries of Poisson.

The existing `glued_completed_zeta` evaluates exactly this truncated formula
using incomplete Gamma integrals. `StandardTateSource.completed` **reuses**
it. A separate quadrature in the idelic variable \(r\) checks the
\(r\leftrightarrow t\), sign and pole conventions without using that
incomplete-Gamma implementation. This numerical agreement is diagnostic.

## 5. Uniform analytic truncation certificate

For \(|\Re s|\le B\) and equal cutoffs \(N\ge1\), set
\(a=3N^2\), \(c_1=\max(B/2-1,0)\), and
\(c_2=\max((B-1)/2,0)\). Assume \(a>\max(c_1,c_2)\).
For any positive integer \(L\), the omitted terms in TZ-06 are bounded by

\[
 R_{N,B,L}=
 \frac{(1+a/L)^{-L}}{6N}
 \left(\frac1{a-c_1}+\frac1{a-c_2}\right).
\]

**Proof.** The decreasing Gaussian gives
\(\sum_{n>N}e^{-\pi n^2t}\le\int_N^\infty e^{-\pi x^2t}dx
\le e^{-3N^2t}/(6Nt)\) for \(t\ge1\). Dropping the extra
\(1/t\le1\), the integrands are bounded respectively by
\(e^{-at}t^{c_i}/(6N)\). Since \(\log t\le t-1\), their integrals
are at most \(e^{-a}/[6N(a-c_i)]\). Finally
\(e^{-a}\le(1+a/L)^{-L}\). ∎

This is the \(m=1\) specialization of the existing
`continuation_tail_rational`, with an explicit reconstruction of its proof.
It is uniform in imaginary part and is **only an analytic truncation bound**.
The floating evaluator's mpmath rounding and incomplete-Gamma evaluations are
not enclosed by it. No certified numerical sign is inferred from those outputs.

## 6. Crucibles and proof/access boundary

| Claim or mutation | Verdict and witness | Kind of evidence |
|---|---|---|
| Standard idelic source produces \(\Gamma_R\zeta\) | TZ-01–TZ-06 | CLASSICAL; paper derivation |
| Quotient Haar receives an extra factor two | Refuted; signed orbit already contains \(\pm n\), doubled residues | Exact normalization plus derived residue law |
| Use raw additive Haar divided by norm at finite primes | Shell mass becomes \(1-p^{-1}\), not one | Exact rational finite witness |
| Delete a prime place \(p\) | Integer coefficient at \(p\) changes from 1 to 0 | Exact finite source witness |
| Add a standalone place/impulse at 6 | Composite place rejected; logarithmic coefficient at 6 must be zero | Exact factorization/source witness |
| Replace \(\Gamma(s/2)\) by \(\Gamma(s)\) | At \(s=6\), coefficients of \(\pi^{-3}\) are 2 versus 120 | Gamma integral/recurrence witness |
| Remove or reverse zero modes | Residues no longer \((-1,+1)\) | Analytic Poisson consequence, rational residue check |
| Finite Euler products determine all source places | Not licensed; unseen-place mutants remain possible | Quantifier/access distinction |
| Continued Euler Dirichlet series converges at \(\Re s=1/2\) | Not asserted or used | Explicit original-domain boundary |
| Completed functional equation implies Weil positivity | Not established | Missing independent sign theorem |

The even Gaussian cannot by itself distinguish a globally conjugated Fourier
convention; a one-sided phase mutation must be tested on shifted finite cosets
or an odd character. Those controls belong to the adelic audit and the
\(\chi_4\) crucible rather than a false phase-detection claim here.

Relative to the declared rational chart and exact arithmetic executor, quotient
normalization, local residue queries, shell coefficients and a specified finite
prime-power tape are finite executable operations. The full restricted
product, its Haar integral and the universal functional equation have finite
mathematical descriptions and finite classical proofs; they are not completed
physical experiments. Rational source identifiers preserve declarations and
prevent accidental cross-source joins, but do not authenticate empirical data.
No field classification of RH follows from this construction.

## 7. Validation and remaining obligations

Focused command: `python -m unittest tests.test_tate_idelic_zeta -v`.
On the local Python 3.12 environment this passed **21/21 tests**, including
exact quotient reconstruction and diagonal invariance, independent valuation
tuple enumeration, source support, fake/omitted-place controls, pole/Gamma
controls, rational tails, idelic-variable quadrature and an external zeta
comparison restricted to \(\Re s>1\). These are executed local results;
they are not a claim about remote CI or the complete repository suite.

**Unresolved:** machine-checked formalization of the infinite analytic theorem;
rigorous interval evaluation covering floating special functions as well as
tails; general arbitrary Schwartz test evaluation; arithmetic-character
extensions beyond this standard source; and the genuinely separate Weil-form
identification/positivity obligations. The strongest next test for this map is
the primitive odd \(\chi_4\) source, because parity, conductor and Fourier
phase cannot all disappear in its Gaussian symmetry.

RH PROVED: NO
