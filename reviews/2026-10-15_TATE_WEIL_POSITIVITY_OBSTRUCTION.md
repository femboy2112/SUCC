# Hostile audit: a Tate test vector is not the canonical Weil form

**Date:** 2026-10-15. **Inspected parent:** `d239c27d3759de71de316180f48dfc097be6aff5`.
**Scope:** independent mathematical audit of the proposed Poisson/Mellin-to-Weil positivity arrow. No nontrivial zeta-zero positions are construction inputs. This note does not claim an obstruction to every possible source-specific positivity proof.

## 1. Verdict and prior work

The following inference is false:

> A normalized Fourier-self-dual Schwartz–Bruhat test has genuine unramified Euler factors at every finite prime and satisfies adelic Poisson and a completed functional equation; therefore the zero/Weil form of its Mellin integral is positive.

Below, a differential operator realizes a normalized symmetric polynomial multiplier as an actual adelic test vector. An explicit compact autocorrelation gives a strictly negative **complete** modified source form, with a rational upper bound and no numerical quadrature. The modified Archimedean test is signed. It is a lawful Tate test, but its test-dependent Mellin integral is not the canonical completed zeta function.

This does not newly discover that self-duality fails to identify the canonical completion. Existing SUCC results already include:

* `adelic_theta_completion.py`: positive, normalized, self-dual Gaussian mixtures with all genuine finite Euler factors and off-line auxiliary zeros (`offcritical_self_dual_zero_witness`, DZ9).
* `shadow_archimedean_tests.py`: positive self-dual Hermite perturbations indistinguishable under specified finite moments and point probes.
* `shadow_zero_divisor.py`: exact common-divisor descent and failure of a height-uniform bounded decoder for a fixed finite family of prime-scale multipliers.
* `certified_contour_weil.py` and CS-05: a symmetric polynomial multiplier with a negative local autocorrelation.
* `weil_gns_gate.py`: the positive-GNS-completion gate and exact auxiliary-norm/target-form mismatch.

The added interface here is an explicit differential-operator lift into the genuine Tate test space, preservation of pole residues and **all** finite Euler factors, and a negative bound for the **complete** modified source form. Its ingredients are elementary classical Fourier/Mellin and explicit-formula calculations; academic originality is unverified.

## 2. OB-01: a normalized polynomial multiplier from an actual self-dual source

Use real Fourier transform
\[
 \widehat\phi(y)=\int_{\mathbb R}\phi(x)e^{2\pi ixy}\,dx,
 \qquad g(x)=e^{-\pi x^2},\qquad
 D=x\frac{d}{dx}+\frac12.
\]
Integration by parts gives \(\widehat{D\phi}=-D\widehat\phi\) for every Schwartz function. Consequently every even polynomial in \(D\) preserves the real Fourier \(+1\) eigenspace. Put
\[
 A=\frac{16}{3}\left(D^2-\frac1{16}\right),\qquad
 \phi_N=A^N g,\qquad N\in\mathbb Z_{\ge0}.
\]
Each \(\phi_N\) is real, even, Schwartz, and Fourier-self-dual. Since \((D\phi)(0)=\phi(0)/2\),
\[
 \phi_N(0)=1,\qquad \int_{\mathbb R}\phi_N(x)\,dx=1.
\]
For \(N=1\), with \(u=\pi x^2\), the source is completely explicit:
\[
 \boxed{\phi_1(x)=\left(1-32u+\frac{64}{3}u^2\right)e^{-u}.}
\]
This function is signed; for example its polynomial factor at \(u=1\) is \(-29/3\). No positive-function claim is made for this family.

For \(\Re s>0\), real Mellin integration by parts yields
\[
 \int_{\mathbb R^\times}(D\phi)(x)|x|^s\frac{dx}{|x|}
 =(1/2-s)\int_{\mathbb R^\times}\phi(x)|x|^s\frac{dx}{|x|}.
\]
The boundary terms vanish by Schwartz decay at infinity and \(\Re s>0\) at zero. Therefore
\[
 Z_\infty(\phi_N,s)=P(s)^N\Gamma_{\mathbb R}(s),\qquad
 P(s)=1+\frac{16}{3}s(s-1)
      =\frac{16}{3}\left((s-1/2)^2-1/16\right).
\]
Here \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\).

Now define the genuine Schwartz–Bruhat test
\[
 \Phi_N=\phi_N\otimes\bigotimes_p1_{\mathbb Z_p}.
\]
All finite local factors, Haar normalizations, and finite additive characters are unchanged. With \(\operatorname{vol}^{\times}(\mathbb Z_p^\times)=1\), absolute convergence for \(\Re s>1\) gives
\[
 \boxed{Z(\Phi_N,s)=P(s)^N\Lambda_\zeta(s),\qquad
 \Lambda_\zeta(s)=\Gamma_{\mathbb R}(s)\zeta(s).}
\]
The analytic continuation follows either by the genuine adelic Poisson theorem or by the displayed factorization. Since \(P(1-s)=P(s)\) and \(P(0)=P(1)=1\), the functional equation and residues \(-1,+1\) at \(0,1\) are preserved. Multiplication by \(s(s-1)/2\) gives the entire function
\[
 \xi_N(s)=P(s)^N\xi_\zeta(s).
\]
Its additional divisor consists of multiplicity \(N\) at each of \(s=1/4,3/4\). These positions are derived roots of the deliberately chosen polynomial, not observed or supplied zeta zeros. The real source differs from the standard Gaussian, and already its relative Mellin moment at \(s=2\) is \((35/3)^N\), so a declared exact source map distinguishes it.

**Status:** PROVED PAPER, using classical Gaussian Fourier/Mellin and adelic Poisson inputs. Exact polynomial identities admit finite rational checks. No infinite theorem is inferred from those checks.

## 3. OB-02: exact negative divisor form on compact autocorrelations

For compact \(h\), set
\[
 H_h(z)=\int_{\mathbb R}h(x)e^{zx}\,dx,\qquad
 \widetilde f(x)=\overline{f(-x)}.
\]
If \(h=f*\widetilde f\) and \(F(z)=\int f(x)e^{zx}dx\), then
\[
 H_h(z)=F(z)\overline{F(-\overline z)}.
\]
For a real odd \(f\), \(F(-a)=-F(a)\) at real \(a\), so the polynomial divisor contributes
\[
 \boxed{\Delta W(h)=H_h(1/4)+H_h(-1/4)=-2F(1/4)^2.}
\]
Take the explicit real odd compact function
\[
 f(x)=x(1-x^2)^3\,1_{[-1,1]}(x).
\]
This is \(C_c^2\); its autocorrelation is a legitimate compact \(C^2\) test for the existing source formula. Since \(\sinh t\ge t\) for \(t\ge0\),
\[
 \begin{aligned}
 F(1/4)&=2\int_0^1x(1-x^2)^3\sinh(x/4)\,dx\\
 &\ge\frac12\int_0^1x^2(1-x^2)^3dx
 =\frac8{315},
 \end{aligned}
\]
and hence
\[
 \boxed{\Delta W(h)\le-\frac{128}{99225}<0.}
\]
The only evaluated moment is the rational polynomial integral \(16/315\). This is an analytic inequality with an exact rational receipt, not floating-point evidence.

## 4. OB-03: the complete modified form is negative, with an explicit bound

Let \(W_\zeta\) be the **complete signed source distribution** in `completed_weil_transport.py`, with half-density \(1/2\), genuine \(\Lambda(n)\), poles and the full Archimedean term. Explicitly,
\[
\begin{aligned}
W_\zeta(h)={}&H_h(1/2)+H_h(-1/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[h(\log n)+h(-\log n)]\\
&-(\gamma+\log(4\pi))h(0)
-\int_0^\infty\frac{e^{-x/2}}{1-e^{-2x}}
 [h(x)+h(-x)-2e^{-x/2}h(0)]\,dx.
\end{aligned}
\]
The integral is absolutely convergent for compact \(C^2\) tests, by the cancellation at zero. This definition reads only arithmetic coefficients and explicit Archimedean data. Its identification with the zero-side formula is an external classical explicit-formula theorem.

For the above \(f\), exact polynomial integration gives
\[
 b=h(0)=\|f\|_2^2=\frac{2048}{45045},\qquad
 c=\|f'\|_2^2=\frac{3072}{5005}.
\]
Cauchy–Schwarz gives \(\|h\|_\infty\le b\) and \(\|h''\|_\infty\le c\).

* **Poles:** their sum is \(-2F(1/2)^2\le0\).
* **Primes:** \(\operatorname{supp}h\subset[-2,2]\), and \(e^2<9\). The only possible prime-power labels are \(2,3,4,5,7,8\), whose underlying primes sum to \(21\). Using \(\log p/\sqrt n<p\), the absolute prime contribution is less than \(42b\).
* **Archimedean contact:** \(-[\gamma+\log(4\pi)]b<0\).
* **Archimedean integral:** write \(K=e^{-x/2}/(1-e^{-2x})\) and \(D_h=h(x)+h(-x)-2e^{-x/2}b\). For \(0<x\le1\), Taylor's theorem gives \(|D_h|\le cx^2+bx\le(b+c)x\), and \(K\le1+1/(2x)\). Thus this part is bounded by \(b+c\). For \(x\ge1\), \(|D_h|\le4b\), while \(K<2e^{-x/2}\), giving a bound less than \(16b\).

Consequently,
\[
 \boxed{W_\zeta(h)<c+59b<4.}
\]
No sign assumption about the actual zeta Weil form has entered this upper bound.

For the modified Mellin object, the logarithmic derivative satisfies
\[
 \frac{\xi_N'}{\xi_N}=
 \frac{\xi_\zeta'}{\xi_\zeta}
 +N\left(\frac1{s-1/4}+\frac1{s-3/4}\right).
\]
Thus its complete transported source form is
\[
 W_N(h)=W_\zeta(h)+N\Delta W(h).
\]
This is also exactly the divisor-addition rule from the classical explicit formula; it does not require knowing any canonical zero positions. With \(N=4096\),
\[
 \boxed{W_{4096}(h)<4-4096\frac{128}{99225}
 =-\frac{127388}{99225}<0.}
\]
For a formulation whose test domain is strictly \(C_c^\infty\), convolve \(f\) with even smooth compact approximate identities. The resulting real odd functions converge in \(C^2\), on a fixed compact support, and their autocorrelations converge in \(C^2\). The displayed source formula is continuous in that topology, so its strict negative margin persists for sufficiently fine smooth approximants. This is an existence proof of a smooth witness, not a claim that a particular mollifier radius was numerically certified.

**Boundary:** \(W_N\ne W_\zeta\). This is a negative control for an overbroad positivity mechanism, not a negative witness against RH. It proves that positivity cannot follow uniformly from the stated Poisson/self-duality/Euler/pole data while allowing arbitrary normalized self-dual Archimedean test vectors.

## 5. OB-04: the missing typed subtraction

Tate's local theory distinguishes the local \(L\)-factor from the Mellin integral of one test vector. A comparison
\[
 Z(\Phi,s)=C_\Phi(s)\Lambda_\zeta(s)
\]
does not permit replacing the canonical Weil form by that of \(Z(\Phi,\cdot)\). Logarithmic differentiation yields the extra term
\[
 \partial_s\log Z(\Phi,s)
 =\partial_s\log\Lambda_\zeta(s)
  +\partial_s\log C_\Phi(s).
\]
Whenever \(C_\Phi\) has zeros, its divisor contributes to the transported form. In OB-01 that contribution is explicitly nonzero and negative on OB-02's autocorrelation. The canonical source-to-Weil arrow must divide out the certified multiplier, subtract its logarithmic derivative, or use a correctly proved common-divisor/local-\(L\)-factor construction. It cannot identify an arbitrary test-vector norm with the signed canonical form.

The canonical form itself still requires a separate all-test positivity proof. Defining a Hilbert/GNS norm to equal it assumes precisely the positivity that needs proving. Existing finite exact GNS controls already express this gate correctly.

## 6. Mutation and discrimination matrix

These are **logical witness types**, not a claim that every new test was executed in this review.

| Mutation | Exact finite/source witness | Remaining analytic requirement |
|---|---|---|
| Flip only the finite additive character | At diagonal \(q=1/3\), the standard real/finite phases cancel; the one-sided flip produces \(e^{4\pi i/3}\ne1\) | None for this cyclotomic identity. Simultaneously conjugating all conventions is consistent, not a defect. |
| Wrong compact-open Haar amplitude | Rational coset volume \(\operatorname{vol}(D\widehat{\mathbb Z})=1/D\) | A Gaussian numerical discrepancy needs bounded tails/rounding; the volume identity does not. |
| Omit a declared prime \(p\) | At integral \(s=2\), relative missing factor \(1-p^{-2}\ne1\) is rational | Infinite Euler product identification uses absolute convergence. |
| Fake standalone Euler impulse \(n=6\) | Unique factorization says 6 is not a prime power; a connected Dirichlet-log coefficient at 6 is zero for the genuine source | Its complete compact Weil effect needs the stated support and certified elementary constants if evaluated numerically. |
| Wrong half-density | The Mellin/log-test exponent must sum to \(s\); changing \(n^{-1/2}\) violates this symbolic exponent identity | A numerical sign or cancellation claim needs an error bound. |
| Omit poles or change Gamma | Pole residues are determined by \(\Phi(0)\) and \(\widehat\Phi(0)\); Gaussian Mellin moments distinguish changed Gamma factors | Analytic continuation and the complete distributional Gamma term require proof, not finitely many matching moments. |
| Wrong \(\chi_4\) conductor/parity/root number | \(\chi_4(-1)=-1\), \(\tau(\chi_4)=2i\), conductor 4, and \(\tau/(i\sqrt4)=1\) are exact finite character data | Odd theta/Mellin continuation and any numerical value certification are analytic. |
| Non-Euler coefficient tape | Any exhibited multiplicativity/prime-power violation is a finite witness | A tape agreeing up to a cutoff cannot be globally authenticated by that cutoff alone. A supplied exact generation law is additional information. |
| OB-01 Archimedean multiplier | \(P(0)=P(1)=1\), \(P(2)=35/3\), and the polynomial source lift are exact | Fourier/Mellin identities are classical analytic theorems; the negative bound uses proved elementary integral inequalities. |

## 7. Observer-relative field logic

The tuple must include the carrier, target, permitted experiments, proof theory, and execution model. In particular:

1. A mathematical completion can support a finite symbolic definition and a finite classical proof without being produced by physically executing infinitely many prime-place operations.
2. On a specified compact log-test support, the prime-power part is finitely executable. The Archimedean contribution additionally needs an effective test representation and certified integration/tail control. An arbitrary function supplied only as an abstract existence object need not have such an algorithm.
3. Finite source probes may fail to distinguish two test vectors, while their exact source formulas distinguish them immediately. The normalized Hermite alternatives already in SUCC demonstrate this relative to a finite probe family; they are not evidence that a fully specified standard Gaussian has multiple meanings.
4. For each cutoff a different later-mutated tape can agree below that cutoff. This is \(\forall H\,\exists\text{ rival}_H\), not a single distinct rival agreeing at every level. Once the entire genuine Euler generation law is a hypothesis, an arbitrary later-mutated tape is not another source-valid world under that same hypothesis.
5. A proved noncomputability obstruction for a declared machine class could justify IdealHard; a proved source collision under a closed toolkit could justify Fucked-phantom; an empty realization class could justify Fucked-impossible. Failure to discover an RH proof establishes none of these.

The present status of universal canonical Weil positivity remains **UNVERIFIED/OPEN**, not a field classification. The next consequential experiment is to demand a source-specific positivity inequality for the canonical form that survives OB-01 after correctly removing its auxiliary multiplier. If a proposed proof also proves the uncorrected \(W_{4096}\) positive, OB-03 decisively falsifies its identification or positivity step.

## 8. Provenance, checks, and limitations

Read `AGENTS.md`, `provenance/IMPORT_MANIFEST.json`, the existing field ledger, completed-Weil implementation and the predecessor source-selection results above. The import manifest records the archival origin at `femboy2112/FuckingRH`, commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; no archival original was modified.

The three rational moments \(16/315\), \(2048/45045\), and \(3072/5005\) were independently recomputed here by expanding the polynomials and integrating monomials with Python `Fraction`. `observational_succ/tate_positivity_obstruction.py` implements the source differential operator, its rational Mellin multiplier and the complete negative-bound receipt. `tests/test_tate_positivity_obstruction.py` checks the moments through an independent beta-integral recurrence, checks the intertwining law on nontrivial rational polynomials, and includes normalization/sign mutations. All **8 focused tests passed** with:

```sh
python -m unittest discover -s tests -p 'test_tate_positivity_obstruction.py' -v
```

The proof of the analytic bounds is above. This sub-audit did not run the full repository suite or inspect remote CI; the integrating principal must report those separately. No proof-assistant verification is claimed.

Classical sources consulted:

* Bjorn Poonen, *Tate's Thesis*, MIT 18.786 notes, §§1, 4 and 5: <https://math.mit.edu/~poonen/786/notes.pdf>. Gaussian Fourier/Mellin, local zeta integrals, and global Poisson/functional equation are classical imports. Poonen's displayed real Fourier sign is the opposite convention; Gaussian self-duality and the dilation anti-commutation used here hold with either consistently chosen sign.
* Enrico Bombieri, *The Riemann Hypothesis*, official Clay problem description: <https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf>. The explicit formula and universal Weil positivity criterion are classical; no new proof of the latter is asserted.
* Existing SUCC derivations: `research/2026-10-12/SHADOW_SUCC_GLOBAL_INFERENCE.md`, `research/2026-10-14/CERTIFIED_CONTOUR_SUZUKI_OBSERVER.md`, and `research/2026-10-15/RH_CARRIER_TATE_WEIL_FUNCTOR.md`.

**RH PROVED: NO**
