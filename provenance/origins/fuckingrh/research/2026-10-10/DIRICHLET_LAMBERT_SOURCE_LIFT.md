# Arithmetic Lambert W: shift the inverse into the Dirichlet algebra

**Date:** 2026-10-10. **RH OPEN.** Parent \`aletheia/lambert-w-succ-inverse-tree-2026-10-10\` at commit \`ea3c2dee128b4cc80fd78616584dee6c374cc54c\`. Work is confined to research branch \`aletheia/dirichlet-star-lambert-source-2026-10-10\`, with main untouched.

**User's observation:** "Because Lambert W is inherently multiplicative, even with its succs and formulaic addition operations. Of course it's blind to that arithmetic data."

**Interpretive correction to test:** W does mix exponential and polynomial growth, but scalar W is **not a multiplicative number-theoretic map** (\(W(ab)\ne W(a)W(b)\) generally). The loss observed in our previous factorial rank estimator occurs at the **earlier data compression**: \(a(n)\mapsto \log n!\) forgets perturbations to coefficient \(a(6)\). Rather than fit W with new source-sign parameters, lift the exact, classical W power series into the already-established arithmetic coefficient algebra. Its multiplication is Dirichlet convolution and therefore *remembers the prime factorization relations*.

This is a general formal-algebra construction, not a claim of a new number theory theorem or a Weil positivity result.

## 1. Standard formal Lambert-W lift

Consider arithmetic functions with values in \(\mathbb Q\) and Dirichlet convolution

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
\]

The unit \(\delta_1\) equals 1 at n=1 and 0 otherwise. The augmentation ideal \(I\) consists of functions \(h\) satisfying \(h(1)=0\).

Let \(a(1)=1\) and \(h=a-\delta_1\). Define

\[
\boxed{\mathcal W_*(h)
=\sum_{k\ge1}\frac{(-k)^{k-1}}{k!}h^{*k}.}
\]

This is the ordinary principal Lambert-W Taylor series (DLMF §4.13.5), with scalar products replaced by Dirichlet convolution. **At each fixed integer n this sum is FINITE**, not asymptotic: a nonzero contribution to \(h^{*k}(n)\) requires an ordered factorization \(n=n_1\cdots n_k\) with all \(n_i\ge2\), hence \(2^k\le n\). No prime enumeration beyond n, analytic continuation, or zeta-zero input is needed.

The formal identity \(W(z)e^{W(z)}=z\), valid in \(\mathbb Q[[z]]\), transfers under substitution into this complete filtered commutative algebra:

\[
\boxed{
\mathcal W_*(h)*\exp_*(\mathcal W_*(h))=h,
}
\]

where \(\exp_*(w)=\delta_1+\sum_{k\ge1}w^{*k}/k!\).
Uniqueness holds in the augmentation ideal: at each coefficient n, the equation solves for \(w(n)\) in terms of h(n) and coefficients on proper divisors. This is a source-preserving coordinate change, not a quotient.

One can express the ring as a formally completed infinite-variable valuation algebra by the prime monomial map

\[
f\longmapsto\sum_{n\ge1}f(n)\prod_p X_p^{v_p(n)}.
\]

Unique factorization transports Dirichlet convolution into ordinary multiplication of the prime-valuation monomials. This is the precise meaning of "*put W inside the multiplicative arithmetic basis*" rather than using scalar W on factorial mass.

**Provenance:** NIST Digital Library of Mathematical Functions, [Lambert W, Eq. 4.13.5](https://dlmf.nist.gov/4.13.E5). This is a specialization of formal power-series calculus, not a novel transcendental theorem.

## 2. The n=6 discriminator and its crucial negative control

At n=6 the only ordered nontrivial factorizations of length two are (2,3) and (3,2), and there are no longer ones. Hence

\[
\boxed{
\mathcal W_*(h)(6)=a(6)-2a(2)a(3).
}
\]

For zeta \(a(n)=1\), the result is **-1**; for a fake a(6)=2 with a(2)=a(3)=1, the result is **0**.

This proves **source sensitivity**, not Euler authenticity: the fake arithmetic has the *zero* W coefficient! Anyone claiming "\(\mathcal W_*(h)(6)=0\)" as a prime admissibility criterion is refuted by the genuine zeta control.

Compare the exact connected-Euler coefficient \(b=\log_*a\):

\[
\boxed{
b(6)=a(6)-a(2)a(3)
=\mathcal W_*(h)(6)+a(2)a(3).
}
\]

This relation is a change of arithmetic coordinate. It recovers the prior known Euler separator exactly, but does **not prove a new property** of primes or RH. A completely multiplicative local mutation \(a(n)=(3/2)^{v_2(n)}\) retains b(6)=0 but alters W(6) from -1 to -3/2; it is a separate unitarity problem. The ring lift reads more information than the scalar factorial rank, but **it does not by itself know which analytic property matters**.

## 3. Infinite finite-stage realization, with an analytic transform

For each source horizon N define \(h_{\le N}\) by taking the complete integrated coefficients up to N (and zero above N). Then for every fixed n,

\[
\boxed{\forall N\ge n:\quad
\mathcal W_*(h_{\le N})(n)=\mathcal W_*(h)(n).}
\]

The reason is fully local: each ordered factor of n divides n and is at most n, so later events cannot alter its existing coefficient. This is precisely an **infinite realization of finite observations** with coefficientwise exact stabilization. The class \(\{h_{\le N}\}\) forms a compatible pro-system of truncations under restriction. The absence of a final finite stage is not a failure of the exact formal global object.

There is moreover a genuine (but Euler-safe) finite-to-analytic transport:

Let \(\sigma>1\) be such that

\[
H_\sigma=\sum_{n\ge2}|h(n)|n^{-\sigma}<e^{-1}.
\]

The space of arithmetic functions with finite weighted \(\ell^1\) norm at \(\sigma\) is a Banach convolution algebra: \(\|f*g\|_\sigma\le\|f\|_\sigma\|g\|_\sigma\). Since Lambert W's Taylor radius is \(e^{-1}\), the series defining \(\mathcal W_*(h)\) converges **absolutely in this Banach algebra**.

The Dirichlet transform is an algebra homomorphism in this domain:

\[
\mathcal D_s(f*g)=\mathcal D_s(f)\mathcal D_s(g),
\quad \mathcal D_s f=\sum_{n\ge1} f(n)n^{-s}.
\]

Hence, for \(\Re s\ge\sigma\),

\[
\boxed{
\mathcal D_s\mathcal W_*(h)
=W_0\!\bigl(\mathcal D_s h\bigr).
}
\]

For the full genuine zeta source \(a(n)=1\), \(h=a-\delta_1\), so in the sufficiently safe region where \(\zeta(\sigma)-1<1/e\) (e.g. \(\sigma=4\)):

\[
\boxed{
\sum_{n\ge2}\mathcal W_*(h)(n)n^{-s}
=W_0(\zeta(s)-1).
}
\]

**Important:** This is a new source-faithful analytic *coordinate* in the conventional safe half-plane, not a meromorphic continuation theorem and not an RH positivity result. Lambert W can introduce its own branch structure unrelated to zeta zeros. The finite truncation on the left is not exactly the right-hand side; the code computes the finite result and an explicit absolute-tail estimate using the positive rooted-tree series \(-W_0(-H_\sigma)\). Numeric bounds are high-precision diagnostics, not directed-rounding certificates.

### Tail logic

For the finite supported \(h\), write \(a_k=k^{k-1}/k!\ge0\). The full absolutely weighted transform has norm bounded by

\[
\sum_{k\ge1}a_k H_\sigma^k=-W_0(-H_\sigma).
\]

Subtract the known contributions from products \(n\le N\) in **the positive absolute-coefficient series**, not from the signed W coefficients. The remainder bounds the distance from the truncated source W Dirichlet sum to its exact infinite multiplicative closure, at the selected s. At real positive h this bound is usually conservative; the tests check it both for a single-prime seed and the genuine zeta prefix. When the infinite true source is compared with a finite source, there is an additional source tail, e.g. \(\sum_{n>N}n^{-4}<1/(3N^3)\), with \(W_0'\le1\) on positive real arguments.

This provides a controlled example of *a source-preserving finite-to-analytic transport* rather than mere scalar growth normalization.

## 4. Distinct ways this construction can fail to prove anything about RH

**False friend A: positive tree coefficients.** The scalar Lambert-W coefficients alternate; the absolute weights count labeled rooted trees. Those combinatorial counts exist for fake arithmetic too, so no sign claim follows.

**False friend B: W(6)=0 is Euler.** Explicitly false: true zeta gives W(6)=-1, while one fake coefficient a(6)=2 gives W(6)=0. The correct composite test must recover b(6).

**False friend C: analytic W(ζ−1) has zeros or branch cuts encoding RH.** No such implication is derived. Its analytic branch points are defined by the W argument reaching -1/e, not by the zeros of zeta. Extension toward critical strip would require new, independently justified continuation data.

**False friend D: reparameterization proves positivity.** \(\mathcal W_*\) is invertible (formal inverse \(w\mapsto w*\exp_*w\)). An invertible change of variables cannot supply a non-circular Weil positivity theorem without additional source geometry, a norm/polarization, and a positivity argument.

**False friend E: numerical agreement in \(\Re s\gg1\).** In that region absolutely convergent series are easy to rearrange. The missing RH mechanism concerns an exact completed Weil form with Gamma correction and positivity on a much harder domain.

The present implementation refuses complex coefficients (e.g. quartic character) rather than silently coerce phases into reals. That extension requires a declared arithmetic \( \mathbb Q(i)\) adapter and matched completed L-factors before making GRH/Davenport–Heilbronn claims.

## 5. Controls and verdict-changing next probe

**Pre-registered controls:**
- Genuine zeta b(6)=0, W(6)=-1 (this kills any claim that vanishing W at 6 means multiplicativity).
- Fake a(6)=2: W(6)=0, b(6)=1; first divergence exactly at 6, later path coefficients change.
- Valid but nonunit Euler-local deformation at p=2: b(6)=0, W(6)=-3/2; distinguishes Euler multiplication from local phase/size.
- Actualization journal pending/estimated a(6): no future coefficient may enter W before propagation; source journal head retained.
- Independent ordered-factor witness enumeration validates the production convolution code.
- Mutated W coefficient breaks the exact \(w*\exp_*w=h\) identity.
- Scalar W holdout at \(\Re s=4\) is compared with the fully multiplicative Dirichlet-series transform and an analytically derived absolute-tail bound, without zeros.
- Lower resource or missing prefix yields an explicit refusal, not an assumed coefficient of zero.

**DISCLOSED** (formal, elementary): exact W_* existence, uniqueness, reversible inverse identity, finite coefficient stabilization, explicit n=6 relation, safe Dirichlet/Mellin intertwiner under \(H_\sigma<1/e\).

**OBSERVED** (bounded, calibrated): Python tests, independent witness enumerator, high-precision Mellin comparisons. The arithmetic and analytic implementations share algebraic provenance, and do not constitute independent RH evidence.

**UNVERIFIED:** any new arithmetic-to-Gamma/Weil *positive form* derived from this W* coordinate. This work alone is not an RH proof step.

**Next probe:** carry *full prime-valuation/path-enriched W* coefficients* into an explicit gamma/Weil test core and analyze a source-derived transform \(W_*\to Q_{\rm Weil}\) whose sign or form topology can be proved, not assumed. Compare matched Hecke versus Davenport–Heilbronn with proper archimedean factors; source-dependent nontrivial behavior in a safe half-plane is an interface test, not the fourth gate. The next substantive advance must discriminate the full Weil-sign behavior and survive source mutations without reading zeros.

**Reproduce:** 
~~~bash
python -m unittest discover -s tests/actualization -p 'test_dirichlet_lambert.py' -v
python scripts/dirichlet_lambert_probe.py --horizon 64 --sigma 4
~~~
