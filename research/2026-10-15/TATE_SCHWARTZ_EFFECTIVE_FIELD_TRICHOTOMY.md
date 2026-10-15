# Source-Indexed Effective Fields and Exact Tate Schwartz–Bruhat Atlas

**Research checkpoint:** 2026-10-15. **Source parent:** draft [Classical SUCC #115](https://github.com/femboy2112/SUCC/pull/115) at `91d494b2d7f1821cae625ddbeb5cd4daa0fa90bf`, ultimately based on `main` at `03db44203147a7b28d445bb9f970fa71360e78c4`. This child draft does not modify `main`, archived imports, or concurrent original Tate/Suzuki branches.

**Scope and status:** Classical elementary harmonic analysis, computability and inverse-limit counterexamples. New code and finite exact tests; analytic/global statements have paper derivations or explicitly attributed classical dependencies. No new proof of RH, independent mathematical priority, global signed Weil form or authenticated empirical carrier.

## 1. Author's three classes, source-typed

The originating insight is:

- **SimpleField:** an infinite or global object has a *finite executable representation / output procedure* and a sufficient finite certificate within the declared carrier.
- **IdealHardField:** an infinite/global statement has a finite mathematical proof relative to the original carrier and source laws, yet no finite algorithm in the declared computation toolkit constructs the required witness.
- **FuckedField:** the required global object may fail source realization, or distinct real/phantom candidate sources remain observationally indistinguishable, or determining whether a distinguishing probe will ever exist is undecidable.

These categories refine established SUCC trichotomy and field-relative calculus; **they are not absolute ontological assertions**. Define separately: source class X, causal transitions A, probes O_n, target T, original-class realization R, proof system P, finite computation toolkit C and lawful probe scheduler. Do not identify (i) formal projective compatibility, (ii) a source in X, (iii) target factorization through a report, (iv) a finite derivation of a quantified theorem, and (v) a terminating executable witness.

A finite source code that can answer each requested coordinate effectively *is* an executable name of an infinite object; it does not physically print infinitely many coordinates at once. An abstract nonconstructive proof of a global section does not supply such an effective name.

### EF1: A genuine SimpleField (finite deterministic orbit, classical theorem)

For a declared *complete* deterministic finite source (S,δ,s0,o), the reachable orbit from s0 enters a cycle in at most |S| transitions. The statement `forall n, o(δ^n(s0))=0` is equivalent to finitely checking the actual reachable orbit. Any bad unreachable state is irrelevant; a bad reachable state is an exact finite counterexample. `AutomaticSource.global_zero_certificate` checks this, but the premise of a fully known finite source is never inferred from observation alone.

### EF2: An IdealHardField with mathematical existence and **no computable path** (classical DNR/Kleene tree)

Fix an effective enumeration e ↦ φ_e of all partial computable functions N→{0,1}; concretely implement a two-counter universal instruction language with self-input and bounded halting simulation. At depth n define

`T_n = {σ∈{0,1}^n | ∀e<n, (φ_e(e) halts within n steps with b) ⇒ σ(e)≠b}.`

The tree T=∪_n T_n is decidable and prefix-closed: every membership query simulates finitely many machines finitely many steps. Every level is nonempty: choose σ_n(e)=1−b for each observed halting b and any bit if not yet halted. These particular finite choices need not be nested, and the program never pretends otherwise.

Global existence follows classically: choose `g(e)=1−φ_e(e)` when the self-computation halts, and 0 otherwise. Its every finite prefix belongs to T. **No computable path exists**: if g were computable, some index e in the universal enumeration would compute g, and then `g(e)≠φ_e(e)=g(e)`. This contradiction relies on the *universality* of the enumeration and the premise of computable global output; it does not assume a halting oracle. Thus:

\[
(\forall n)(\exists σ∈ T_n)
\land(\exists g∈ [T])
\land\neg(\exists\text{ computable }g∈[T]).
\]

All quantifiers here are mathematical, not claims of executing ω stages. The finite implementation has explicit resource caps and tests first 34 depths; universal conclusions inherit the classical diagonal proof, not the finite sweep. An additional halting oracle changes the computability status: **toolkit relativity is mathematical, not rhetorical**.

Sources: classical Kleene computable-tree phenomenon, Minsky two-counter universality. The code makes one explicit finite instruction enumeration, checks program encode/decode and bounded diagonal conflicts. Academic priority not claimed.

### EF3: Three independent FuckedField obstruction certificates

**Missing realization.** Source X consists of eventually zero binary sequences. For every n, the prefix `1^n` is realized by `1^n0^ω`, yet `1^ω` is not a source in X. The inverse limit in the *larger* Cantor carrier exists; the original-source realization arrow fails because X is not closed. This does **not** mean infinity itself is inconsistent.

**Observational nonuniqueness.** Source X={0,1}^N; lawful probes read even-index bits, target is the value at odd index 1. Two sources differing only at index 1 yield identical all-stage transcripts but opposite targets. No target decoder exists on the accessible observation image. Adding a lawful index-1 probe repairs this *specific* ambiguity; no metaphysical impossibility is asserted.

**Delayed discriminator / undecidable classification.** A pulse first appearing at index H evades every query below H; absence cannot be certified by a finite negative prefix. For a two-counter program e, define probes that distinguish two source bits iff e halts within n steps. Each finite probe is executable. A uniform algorithm deciding whether **some** finite stage will distinguish would decide halting. The finite model verifies known delayed-halt positive controls and known looping negative prefixes, but does **not** certify nonhalting from those prefixes.

A single field can exhibit several obstructions. Keep source realization, target identification, proof and execution state in a vector, not a one-number truth score.

## 2. Actual Tate-local object: Schwartz–Bruhat test functions on Q_p

For a genuine prime p and nonnegative integers a,b, define

\[
V_{a,b}=\{f\in\mathcal S(\mathbb Q_p):\operatorname{supp}f\subset p^{-a}\mathbb Z_p,
\quad f(x+t)=f(x)\ \forall t\in p^b\mathbb Z_p\}.
\]

Each *particular declared function* is specified by `N=p^(a+b)` coset values indexed by `x=k/p^a`, `k mod N`. The coefficients lie in a specified cyclotomic field of exact rational combinations, not rounded complex numbers. This finite description is **one genuine function on an infinite local field**. It neither enumerates the whole field nor infers unknown source support/precision from finitely many empirical measurements.

Choose the additive character ψ_p(x)=exp(2πi{ x }_p), `vol(Z_p)=1`, hence each source coset has additive mass p^(-b). Then:

\[
\widehat f(\ell/p^b)=p^{-b}\sum_{k\bmod N}f(k/p^a)\,\zeta_N^{k\ell}.
\]

The transform interchanges support/precision indices:

\[
\mathcal F: V_{a,b}\to V_{b,a},\quad \mathcal F^2 f(x)=f(-x),
\quad\|\mathcal Ff\|_{L^2(dx)}=\|f\|_{L^2(dx)}.
\]

**Paper proof:** finite root-of-unity orthogonality `sum_{ell=0}^{N-1} ζ_N^{(k−j)ell}=N δ_{k,j}`. Under the selected masses, p^(-a)p^(-b)N=1, hence Fourier inversion, Parseval and Plancherel. The *support* inclusion `V_{a,b}→V_{a+1,b}` becomes a *precision* inclusion under Fourier; similarly `V_{a,b}→V_{a,b+1}` becomes dual support inclusion. Their exact commuting squares use the source coset maps, **not an assumed global Fourier miracle**. Tests compare two independent rational packets, explicit Hadamard and cubic Gauss phases, and both refinement directions.

### TF1–TF3: all-coset unramified local Tate equation

For unramified local χ with χ(p)=ω∈{±1}, `d^×x(Z_p^×)=1`, define for Re(s)>0

\[
Z_p(s,f,\chi)=\int_{\mathbb Q_p^\times}f(x)\chi(x)|x|_p^s\,d^\times x.
\]

At finitely many shell indices below the local precision threshold, evaluate direct finite coset contributions. For all shells `j≥b`, `f(p^j u)=f(0)` and the remaining sum is the geometric tail `f(0)ω^b p^{-bs}/(1−ωp^{-s})`. Thus a finite exact expression plus a geometrically controlled tail **represents the meromorphic continuation**. For negative integer s used on the dual side, this algebraic continuation is *not* asserted equal to a divergent improper integral.

Classical local Tate identity gives on every representable test (including arbitrary signed coefficients, not only balls):

\[
Z_p(s,f,\chi)=
\frac{1-\omega^{-1}p^{s-1}}{1-\omega p^{-s}}\,
Z_p(1-s,\widehat f,\chi^{-1}).
\]

The ratio is a **meromorphic identity**. It is checked exactly for 108 nontrivial finite source configurations and is mathematically derived by Fourier orthogonality and shell regrouping. More generally the Fourier zero-mode `f̂(0)=∫f dx` and original zero-mode `f(0)` are distinct independent boundary inputs controlling the poles. Deliberately changing Haar normalization breaks the equation.

**Conductor control:** residues 1 and 4 coincide modulo 3 but are distinguishable by an additive phase at conductor 9. Coarse finite reporting is not source-faithful for every Fourier target. PR #103 independently treats a ramified χ(-3) Gauss character; this branch does not silently import or replace it.

### TF4: exact additive local/global compatibility

For rational diagonal q, finite-place additive characters and the real character `ψ_∞(q)=exp(-2πiq)` obey

\[
\psi_\infty(q)\prod_p\psi_p(q)=1.
\]

At each rational denominator only finitely many primes contribute, and the phase exponent sum is an exact integer. The script checks several q using modular inverses, including q=1/6, with a real sign that cancels finite residues. This is the elementary diagonal character compatibility, **not** the full Poisson summation theorem on adele classes.

### TF5: Archimedean Gamma and true Euler source restrictions

For the real Gaussian `f(x)=exp(-πx²)`, the Mellin zeta integral on positive x with the two-sided convention produces:

\[
Z_\infty(s,f)=\pi^{-s/2}\Gamma(s/2),\qquad
Z_\infty(s+2)=\frac{s}{2\pi}Z_\infty(s).
\]

At positive integer s the code represents values as an *exact rational coefficient times formal π power*, never a fabricated floating certificate. The positive real half-density/critical exponent s=1/2 is independently source-normalized; it is **not** source-derived Weil positivity.

True Euler factors only over genuine primes, with multiplicative coefficients `a(6)=1` from primes 2 and 3; adding an **independent fake composite-6 Euler factor** gives `a(6)=2`. For Re(s)≥σ>1, a finite prime cutoff P satisfies the elementary absolute tail bound

\[
\left|\zeta(s)-\prod_{p\le P}(1-p^{-s})^{-1}\right|
 \le \sum_{n>P}n^{-\sigma}
 \le \frac{P^{1-\sigma}}{\sigma-1}.
\]

It cannot be transported to Re(s)=1/2. This tail and exact finite product are source-sided checks, not an RH route by themselves.

## 3. The indispensable missing arrows

\[
\boxed{\text{locally source-faithful Schwartz functions}
 \longrightarrow \text{restricted-product adelic Poisson}
 \longrightarrow \text{completed source distribution}
 \longrightarrow \text{original signed Weil positivity}}
\]

- **First arrow:** classical adelic Fourier/Poisson is an external theorem, not newly derived from finite window testing here. A fully executable carrier-specific version would require the restricted product, topology, measures, global summation convergence and poles.
- **Second:** original prime powers, Gamma, conductor, pole/contact, test-domain and half-density must be identified with **the same source**. Parallel Tate/Suzuki draft PRs investigate it.
- **Third:** source-derived positivity for all Weil test functions, equivalently RH, remains **UNVERIFIED**, not disproved, uncomputable, or proved independent by the field trichotomy.

The trichotomy itself cannot classify RH as a FuckedField without an independent obstruction or undecidability theorem. **Mathematical possibility, available proof and carrier-relative execution remain separate.**

## 4. Reproducibility and negative controls

Run from the repository root:

```sh
python -m unittest discover -s tests -p 'test_classical_tate_window.py' -v
python -m unittest discover -s tests -p 'test_effective_field_gates.py' -v
python scripts/classical_tate_bridge_probe.py --verify
python scripts/effective_field_probe.py --verify
python scripts/verify_provenance.py
```

Historical parent test and source modules are not rewritten. Local isolated tests passed 23 cases under Python 3.13 using a **test-only mirror** of inherited `godel_succ`; published tests must be rerun on the genuine repository under 3.10 and 3.13. A prior incomplete child-branch Tate receipt referred to a noncommitted dependency; the missing module is now committed and the receipt replaced with source-recomputed values. Any exact-head CI failures are evidence, never suppressed.

No zero locations are construction inputs. No universal source theorem is certified by bounded testing alone.

### Next discriminating experiment

Add a typed primitive local ramified character of conductor p^r to the exact Fourier windows, preserving its Gauss sum and phase; then compare its provenance with the original χ(-3) Tate branch. Independently build a mathematically valid restricted-product test and prove the global Poisson arrow (not a fitted finite cancellation). Only then transport the complete signed Weil distribution and test its all-domain positivity without assuming RH.
