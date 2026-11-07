# Quadratic Pisot / Galois / Tate carrier: a shared C2 source, not an RH proof

**2026-11-06 · SUCC research dossier · first-pass paper derivations and exact finite controls.**
Base: `main@d32342d375f44ddf62221ad6aff2f534abdc0a03` (Operation Main XX).
**Status:** classical identities reconstructed and assembled; no claim of scholarly priority; no nontrivial-zero inputs; RH and pi base-16 normality OPEN. No imports, archived originals, source contracts, or kernel declarations changed.

## 0. Question, typing, and verdict

**Author-origin hypothesis.** The Pisot conjugate parity of the golden ratio and the reflection `s -> 1-s` of the completed Riemann zeta function may originate in a common mathematical carrier. Construct the global/analytic carrier first, recover rational arithmetic by descent, and check whether this is more than a resemblance between two order-two operations.

**Answer (scoped):** the quadratic field `K=Q(sqrt(5))` and its adelic/cyclotomic realizations provide a rigorous common **ambient arithmetic source**. The golden-ratio conjugation and Frobenius splitting at primes are aspects of the *same* quadratic Galois involution; its quadratic character `chi_5` creates an authentic Euler factor and a completed L-function with `s <-> 1-s` symmetry. On the **even-unit subgroup**, conjugation really is inversion, and a centered Mellin character transports it to `z -> -z`. On the full unit group a sign-dependent spectral shift appears. **No theorem here identifies the unit-norm parity with the global zeta reflection, proves Weil positivity, or forces any zeta zero onto the critical line.**

Type distinctions (do not collapse):
- `sigma in Gal(K/Q)` acts on arithmetic elements/places; its order is two.
- `eps(u)=N_{K/Q}(u) in {+1,-1}` is a *character of the unit group*, not the Galois automorphism itself.
- `chi_5(p)` is the quadratic Artin/Frobenius character on unramified rational primes; it is not `eps(phi^p)`.
- `R(s)=1-s` acts on the complex Mellin parameter; it is not an automorphism of the field K.
- An equality of abstract C2 groups is not an intertwining theorem. Every arrow below declares its domain.

## 1. Integral arithmetic and the Galois involution (QR-01, classical / exact)

Let `a=phi=(1+sqrt(5))/2`, so `a^2=a+1`. Then
\[
K=\mathbb Q[a]\simeq\mathbb Q[X]/(X^2-X-1),\qquad
\mathcal O_K=\mathbb Z[a],\quad D_K=5.
\]
The order `Z[sqrt(5)]` has **index two** in `O_K`, discriminant 20 rather than 5. At p=2 that difference cannot be ignored.

The nontrivial Galois element satisfies
\[
\sigma(a)=1-a=-a^{-1},\qquad \sigma^2=1.
\]
Its invariants obey `K^{<sigma>}=Q`; the projections `(1+sigma)/2` and `(1-sigma)/2` give `K=Q (+) Q sqrt(5)` as Q-vector spaces. They are NOT two multiplicative subfields: the anti-invariant sector squared lands in the invariant sector. The opposite-direction intuition is **extension/descent** (`Q -> K` vs `K -> K^sigma=Q`), not a statement that adjoining Q to an isolated irrational atom is a self-sufficient construction without a specified base ring.

In basis `(a,1)`, multiplication by a and conjugation have matrices
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
C=\begin{pmatrix}-1&0\\1&1\end{pmatrix},\quad
C^2=I,\quad CAC^{-1}=-A^{-1},\quad CA^2C^{-1}=A^{-2}.
\]
The determinant `det(A)=-1` is an exact integral carrier orientation, not a zero-location theorem.

The fundamental unit `a` has norm −1, and `O_K^\times={+/- a^n:n in Z}`. Hence
\[
N(a^n)=(-1)^n,\quad
\sigma(a^n)=(-1)^n a^{-n}.
\]
For `u=(-1)^e a^n`, `e in Z/2Z`, the Galois action on the unit labels is
\[
(n,e)\longmapsto(-n,e+n\bmod2). \tag{QR-01a}
\]
The sign is a real datum which vanishes if one silently restricts to norm-positive units.

## 2. An exact unit Fourier/Mellin transport, including the odd-sector twist (QR-02, derived / exact)

Write `R_K=log(a)` and define characters on the abstract unit group:
\[
\lambda_{z,d}((-1)^e a^n)=(-1)^{de}\exp(nR_K z),
\quad d\in\{0,1\},\ z\in\mathbb C.
\]
Using (QR-01a) gives the exact identity
\[
\boxed{\lambda_{z,d}\circ\sigma=
       \lambda_{-z+i\pi d/R_K,\,d}.} \tag{QR-02}
\]
Spectral coordinates `z` are periodic modulo `2pi i/R_K`; the shifted reflection remains an involution modulo that period. If `d=0` this is `z->-z`. On the even-power subgroup `<a^2>`, `sigma(a^{2n})=a^{-2n}` and conjugation is literal inversion for both signs.

With `z=s-1/2`, the **unit-character** reflection is centered at `Re(s)=1/2` (or, with `d=1`, has a parity-sensitive imaginary displacement). This is an exact restricted **Mellin-character** intertwiner. It is NOT the global functional equation of `zeta(s)`, and imposing one from this equality would be circular: the global zeta functional equation also uses the source's finite-place factors, test functions, Haar/duality normalization, and Poisson summation.

## 3. The cyclotomic / finite-Fourier sqrt(5) atom (QR-03, classical / exact)

Let `w=exp(2pi i/5)` and `chi_5=[0,1,-1,-1,1]` on residues 0,...,4. The quadratic Gauss sum gives
\[
\tau(\chi_5)=\sum_{r\bmod5}\chi_5(r)w^r=\sqrt5.
\]
For the normalized **plus-sign** discrete transform
\[
(\mathcal F_5 f)(k)=5^{-1/2}\sum_{r\bmod5}f(r)w^{rk},
\qquad \mathcal F_5\chi_5=\chi_5.
\]
Also `a=1+w+w^{-1}`, so `K=Q(w+w^{-1})` is the unique quadratic subfield of `Q(w)`. The Galois automorphisms `w->w^j` with `chi_5(j)=-1` change the sign of the Gauss sum, giving the same two conjugate embeddings. These are **different Fourier objects**: the DFT on `F_5` and the global adelic Fourier transform must not be identified by notation alone.

The finite Fourier character already carries the conductor 5 and the sign/normalization data that enter the functional equation of `L(s,chi_5)`.

## 4. Frobenius: the source-verified prime-local bridge (QR-04, classical / exact)

For every prime `p != 5`, the polynomial `X^2-X-1` is separable modulo p and
\[
\boxed{a^p\equiv
\begin{cases}
a\pmod{p\mathcal O_K}, & \chi_5(p)=+1,\\
1-a\pmod{p\mathcal O_K}, & \chi_5(p)=-1.
\end{cases}} \tag{QR-04}
\]
Here `chi_5(p)=+1` for `p mod5 in {1,4}` and `-1` for residues {2,3}; this also holds for p=2 with the finite-field Frobenius. The case p=5 is **ramified** and not classified by an unramified Frobenius element.

Proof: for p not dividing the discriminant, Frobenius permutes the two roots mod p; the discriminant's quadratic character decides whether the roots are individually in `F_p` (split) or exchanged over `F_{p^2}` (inert). Explicit powering in `(Z/pZ)[a]/(a^2-a-1)` provides an independent exact finite check.

Let `t=p^{-s}`. The permutation representation of Frobenius on the two embeddings has
\[
\det(I-t\,\mathrm{Frob}_p)=
\begin{cases}
(1-t)^2,& \chi_5(p)=+1,\\
1-t^2,& \chi_5(p)=-1.
\end{cases}
=(1-t)(1-\chi_5(p)t).
\]
Thus its reciprocal is the **actual Dedekind-zeta Euler factor** at p. At p=5 the ramified local factor is `(1-5^{-s})^{-1}`. This establishes
\[
\boxed{\zeta_K(s)=\zeta(s)L(s,\chi_5)}
\quad (\Re s>1),
\]
and then meromorphically by continuation. Notice: the Frobenius character `chi_5(p)` is NOT the unit norm `N(a^p)=(-1)^p`; p=11 and 13 already distinguish them.

**This is the most important source-linked result of this round:** the same quadratic conjugation visible in the Pisot carrier is exactly the one detected by the genuine prime-local splitting law underlying `L(s,chi_5)`. It does not follow from merely matching two C2 symbols.

## 5. Global adeles, Poisson, and the analytic reflection (QR-05, classical; separate types)

For a finite extension K/Q the canonical finite-rank topological ring isomorphism is
\[
\mathbb A_{\mathbb Q}\otimes_{\mathbb Q}K
\simeq \mathbb A_K,\qquad
\mathbb A_K^{\sigma}\simeq\mathbb A_{\mathbb Q}.
\]
This is a **field-extension / invariant-descent** relation. The local construction uses `Q_p[X]/(X^2-5)` (which can split into two copies of `Q_p`); it must NOT presuppose a chosen `sqrt(5) in every `Q_p`.

Let `Lambda_Q(s)=pi^{-s/2} Gamma(s/2) zeta(s)` (meromorphic),
\[
\Lambda_{\chi_5}(s)=(5/\pi)^{s/2}
\Gamma(s/2)L(s,\chi_5),
\]
and
\[
\Lambda_K(s)=5^{s/2}\pi^{-s}
\Gamma(s/2)^2\zeta_K(s)
=\Lambda_Q(s)\Lambda_{\chi_5}(s).
\]
The classical Fourier/Poisson functional equations give
\[
\Lambda_Q(s)=\Lambda_Q(1-s),\quad
\Lambda_{\chi_5}(s)=\Lambda_{\chi_5}(1-s),\quad
\boxed{\Lambda_K(s)=\Lambda_K(1-s)}.
\]
The quadratic character is primitive, even, has Gauss sum `sqrt(5)`, and root number +1. The ordinary Dedekind completion is **meromorphic** (poles at s=0,1); multiplying by `s(s-1)` gives an entire completion. Do not conflate `Lambda_Q` here with the usual entire `xi_Q(s)=s(s-1)Lambda_Q(s)/2`.

The factorization gives a **real zero-divisor transport**: in the open critical strip, nontrivial zeros (with multiplicity) of `zeta_K` are the union of those of `zeta` and `L(s,chi_5)`. The Dedekind RH for K is equivalent to RH for zeta AND GRH for chi_5. Neither reflection symmetry nor factorization alone proves either.

For `K=Q(sqrt(5))`, class number h=1, regulator `R_K=log(a)`, roots of unity count 2; the analytic class number formula gives
\[
\boxed{L(1,\chi_5)=\mathrm{Res}_{s=1}\zeta_K(s)
       =\frac{2\log(a)}{\sqrt5}.} \tag{QR-05a}
\]
This ties a true analytic value to the **same regulator** governing the Pisot orbit. It is a classical identity, not a new zero bound.

## 6. Revisiting the harmonic/Lucas residual (QR-06, classical / derived exact asymptotic)

Let `L_n=a^n+(-a^{-1})^n` be the integer Lucas trace. By Euler–Maclaurin,
\[
H_N=\log N+\gamma+\frac1{2N}-\frac1{12N^2}
     +O(N^{-4}).
\]
Substituting `N=L_n=a^n(1+(-1)^na^{-2n})` and expanding:
\[
\boxed{
H_{L_n}=n\log a+\gamma+\frac1{2a^n}
+\frac{(-1)^n-1/12}{a^{2n}}+O(a^{-3n}).
} \tag{QR-06}
\]
Consequently the normalized residual converges along even/odd subsequences to `11/12` and `-13/12` respectively; the center is `-1/12=zeta(-1)` and the parity amplitude is 1. This is a **Bernoulli/Euler–Maclaurin coefficient plus unit norm**, NOT evidence of a new critical-line zero theorem. Its first term `n log a` is the regulator times time, and that regulator is `sqrt5 L(1,chi_5)/2` by (QR-05a).

## 7. The annihilation and wrong-carrier firewalls (QR-07)

**First: full-field sigma and Mellin reflection are NOT the same map.**
For a general `x in K^x`, `sigma(x)` is not `x^{-1}`; the inversion identity requires the **norm-one subgroup**. The standard completed zeta reflection is a global Fourier/Poisson theorem. On the unit group the exact restricted transform is (QR-02), including the odd-sign twist.

**Second: the sign can disappear from a supposedly faithful global observation.**
The absolute ideal norm in `zeta_K` forgets `N(a^n)=(-1)^n`. For a Gal-invariant Tate zeta integral
\[
Z(\Phi,s)=\int_{\mathbb A_K^\times}\Phi(x)|x|_K^s\,d^\times x
\]
with a convergent Schwartz–Bruhat test, the normalized Galois action commutes with the trace-paired Fourier transform. Change of variables by sigma gives `Z(\Phi\circ sigma,s)=Z(\Phi,s)`. Hence
\[
Z((\Phi-\Phi\circ\sigma)/2,s)=0.
\]
Analytic continuation preserves the zero identity. **The Galois-odd part of the TEST FUNCTION is annihilated by the untwisted integral.** This does NOT eliminate `L(s,chi_5)`: that Dirichlet factor belongs to the nontrivial **Artin representation on Gal(K/Q)**, not to the discarded odd test-function sector. Mixing these two oddities is an invalid inference.

**Third: the generic quadratic control.** `Q(sqrt2)` has a quadratic Pisot unit `1+sqrt2`, norm -1, an analogous parity/reflection mechanism, and its own completed Dedekind zeta. These facts alone do not select the zeta zeros of Q, let alone RH. The conductor 5 and genuine original SUCC source must justify choosing K=sqrt5 rather than simply choosing what fits.

**Fourth: symmetry plus positive Fourier support is too weak.** SUCC's previously recorded exact hostile model
\[
G(s)=2+\cosh(4(s-\tfrac12))
\]
is symmetric under `s->1-s` and is a Fourier transform of a positive discrete measure on the critical line, but has zeros
\[
s=\tfrac12\pm\frac{\operatorname{arcosh}2}{4}
  +\frac{(2k+1)\pi i}{4},
\]
strictly OFF that line. The actual Euler product and **signed completed Weil form** may not be replaced by this shadow.

**Fifth: wrong source map.** SUCC's original pi BBP forcing/zero seed, the silver-Pell seam, and the original Riemann prime/Gamma source are distinct contracts. This dossier provides an auxiliary quadratic-field carrier. No verified map transports original BBP temporal signed cancellation or the original full Weil-positive kernel into it.

## 8. Claims and evidence ledger (new local labels; no canonical promotion)

| ID | Claim | Verdict | Basis |
| --- | --- | --- | --- |
| QR-01 | Integral quadratic field; conjugation, unit norm, matrix relation | PROVED CLASSICAL | Exact algebra, independent modular tests |
| QR-02 | Unit-character twisted reflection with parity shift | PROVED under declared unit-character model | Group calculation; complex sample tests auxiliary |
| QR-03 | Gauss atom, finite Fourier eigenvector | PROVED CLASSICAL | Gauss sums; numerical DFT auxiliary |
| QR-04 | Prime-local Frobenius gives chi5 Euler factors | PROVED CLASSICAL | Root splitting argument; exact finite p controls |
| QR-05 | Adelic extension/descent, completed L-factorization/reflection, regulator | PROVED CLASSICAL (imported theorems) | Tate/Poisson and class-number formula sources |
| QR-06 | Harmonic/Lucas residual and alternating Bernoulli shift | DERIVED exact asymptotic | Euler–Maclaurin; finite high-precision checks auxiliary |
| QR-07 | Untwisted zeta integral kills Gal-odd test sector | PROVED under invariant-Haar/test hypotheses | Change of variables; signed-control declaration |
| QR-08 | Intertwiner yielding authentic signed Weil positivity/RH | **UNVERIFIED / OPEN** | No identification or sign proof |
| QR-09 | Transfer to original selected zero-seed BBP normality | **UNVERIFIED / OPEN** | No selected temporal signed estimate |

Neither exact finite replays nor repeated same-source reports constitute independent analytic proof. The local derivations use standard mathematical theorems, not claims of novel priority.

## 9. Next decisive proof and falsification gates

1. **Transport, not another equality of involution labels.** Build a typed diagram from the original Weil prime-power distribution `Lambda(n)/sqrt(n)` and the Gamma/pole term to genuine local K/Q Artin factors. A factorization identity is zero-sensitive but **does not** supply signed quadratic-form positivity. Specify what is forgotten under each projection.
2. **Preserve the missing parity.** Define a legal twisted Hecke/Tate test (including its finite-place conductor and compensation for units in the idele quotient). Determine whether the unit norm parity is measurable after gluing, or prove that any attempted descent factors through its null fiber. Simply inserting `(-1)^n` into an unverified global `L`-series is forbidden.
3. **Compare source-matched and hostile models.** Verify p=2 local order, p=5 ramification, split/inert p controls, `Q(sqrt2)` generic control, a fake sign character, and `G(s)` off-line symmetric positive support. Demand failures on those mutants where the desired source fingerprint is absent.
4. **Exact place-level Fourier and Mellin maps.** State Haar normalization, additive trace character, Poisson hypotheses, functional-equation Gamma factors and pole correction. Prove any claimed square commutes on explicit test functions and is natural on the permitted space.
5. **Proof gate (RH-hard):** From authentic source, prove the required completed **signed Weil quadratic form is positive on all admissible tests**, or find an independently checkable reduction with a strictly smaller open obligation. No RH claim from symmetry, zero-factorization, or a finite positive Gram matrix.
6. **BBP gate separate:** a theorem on `Q(sqrt5)` does not alter the zero-seed four-pole π orbit. Any purported transfer must certify exact selected history, sign, integer carry, and a new fixed-h signed Weyl cancellation estimate.

## 10. Provenance and source references

Repository anchors (read on pinned main; source originals and claim ledgers untouched):
- [Prime–Pisot source and explicit symmetric off-line controls](../../2026-10-28/prime_pisot_field/RESEARCH.md), ``4–9.
- [Pascal/golden/harmonic source-selected auxiliary observer](../../2026-10-29/oily_triangle_sheet/PASCAL_GOLDEN_HARMONIC.md).
- [Pisot–Gamma Pell two-sheet transport and no-go](../../2026-11-02/pisot_gamma_gluing/PROOFS.md), ``1, 8.
- [Tate central reflection and original prime jets](../../2026-10-15/TATE_CENTRAL_REFLECTION_DIODE.md).
- [Tate–Weil original source and half-density](../../2026-10-15/RH_CARRIER_TATE_WEIL_FUNCTOR.md).
- [Eta/Bernoulli to authentic completed zeta via theta–Poisson](../../2026-10-15/TATE_ETA_BERNOULLI_TRANSDUCER.md), `ETA-05G.

External classical sources:
- Bjorn Poonen, *Tate's Thesis*, https://math.mit.edu/~poonen/786/notes.pdf (Fourier/Poisson, Tate zeta integrals, global functional equations).
- D. Burde, *Algebraic Number Theory*, `5.2 https://homepage.univie.ac.at/dietrich.burde/papers/burde_71_ant.pdf (analytic class number formula, real-quadratic example).
- Classical quadratic Gauss-sum evaluation and quadratic splitting law; all signs/conventions reconstructed in ``3–4 and the companion finite tests.

**Validation note:** `tests/test_quadratic_galois_tate_bridge.py` checks exact arithmetic/Galois/Frobenius/local Euler identities and labeled finite numerical Fourier/asymptotic controls. Tests are checks of implementation, not certificates of global analytic statements. See `NEXT.md` for the runnable next-round assignment.