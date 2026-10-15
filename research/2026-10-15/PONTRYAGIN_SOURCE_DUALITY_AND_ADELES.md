# Finite Causal Observation Diagrams and Their Pontryagin Duals: A Calibrated SUCC Reconstruction

**Research note.** 2026-10-15. Observational SUCC research benchmark PD-01–PD-11.  
**Parent:** \`research/edge-carrier-reconstruction-2026-10-15@7cc16f9a3a23b0a2f87bd7c9639cd5bd0757209b\`.  
**Branch:** \`research/pontryagin-finite-adelic-duality-2026-10-15\`.  
**Mathematical status:** classical theorems, independently written derivations, and exact finite source-model implementations. **RH PROVED: NO.**

## Abstract

We calibrate source-indexed Observational SUCC reconstruction against the classical Pontryagin duality theorem
\[
  \widehat{\mathbb Z}^{\,\vee}\simeq(\mathbb Q/\mathbb Z)_{\mathrm{disc}},
  \qquad \widehat{\mathbb Z}=\varprojlim_{n\mid m}\mathbb Z/n\mathbb Z.
\]
The finite observation category has objects \(n\ge1\), arrows \(m\to n\) exactly when \(n\mid m\), and reduction maps \(\pi_{m,n}\). Its dual character arrows reverse direction and multiply character labels by \(m/n\), yielding the direct limit \(\mathbb Q/\mathbb Z\). All continuous global characters have a finite cyclic conductor, even though the global compact carrier is uncountable. We then realize the finite-adèle quotient
\[
  0\longrightarrow\widehat{\mathbb Z}
   \longrightarrow\mathbb A_{\mathbb Q,f}
   \overset{\mathrm{pp}}{\longrightarrow}
   (\mathbb Q/\mathbb Z)_{\mathrm{disc}}\longrightarrow0,
\]
verify its source-derived principal-part map and its non-splitting as an extension of additive groups, and match the dual phases against the existing SUCC Tate \(S\)-lattice implementation with explicit signs. Exact cyclotomic computations recover finite Fourier orthogonality and Poisson summation for subgroup cosets. All general topological and analytic results are classical, credited below; no universal theorem is inferred from finite tests. No RH/Weil-positive result is asserted.

## 1. Typed objects, problem and acceptance criteria

Let \(\mathsf{Div}^{\mathrm{op}}\) denote the category of positive integer moduli with an arrow \(m\to n\) iff \(n\mid m\). Define a functor \(X:\mathsf{Div}^{\mathrm{op}}\to\mathsf{FinAb}\) by
\[
  X(n)=\mathbb Z/n\mathbb Z,\qquad
  X(m\to n)(x_m)=x_m\bmod n .
\]
For all \(n\mid m\mid \ell\), \(\pi_{\ell,n}=\pi_{m,n}\pi_{\ell,m}\). An element of the inverse-limit carrier \(\widehat{\mathbb Z}\) is *by definition* a compatible cone \(x=(x_n)_{n\ge1}\). The profinite topology is the coarsest making all projections \(\pi_n\) continuous; the kernels \(\ker\pi_n\) form an identity-neighborhood base.

Here and throughout, *carrier* means a mathematical set, group, ring or space equipped with a specified structure. A source-indexed SUCC observer model adds permitted finite experiments, causal event receipts and proof/access costs. A mathematical point is not an authenticated physical event.

**Acceptance:** (i) an explicit character with a justified map and inverse, not only cardinality; (ii) exact source-compatible arrow naturality; (iii) source-matched finite-adèle quotient and Tate character signs; (iv) at least two independent computational routes for finite formulas; (v) preservation of invalid mutations and unproved boundaries; (vi) clear distinction among an inverse-limit theorem, individual finite character evaluation, and finite-horizon global reconstruction.

## 2. PD-01: finite cyclic characters (CLASSICAL)

For \(n\ge1\) and \(a\in\mathbb Z/n\mathbb Z\), define
\[
  \chi_{n,a}(x)=\exp(2\pi i ax/n),\qquad x\in\mathbb Z/n\mathbb Z.
\]
This is well-defined, and \(\chi_{n,a+b}=\chi_{n,a}\chi_{n,b}\). Every additive character of \(\mathbb Z/n\mathbb Z\) is of this form: a character is determined by its value at \(1\), and that value must have \(n\)-th power \(1\). Hence
\[
  (\mathbb Z/n\mathbb Z)^\vee\simeq\mathbb Z/n\mathbb Z .
\]

If \(n\mid m\), pullback along \(\pi_{m,n}\) is
\[
  \chi_{n,a}\circ\pi_{m,n}=\chi_{m,a(m/n)}. \tag{2.1}
\]
This is an identity of **functions** on \(\mathbb Z/m\mathbb Z\), not a vague correspondence of root counts. It yields the commutative square
\[
\begin{array}{ccc}
  \mathbb Z/m\mathbb Z &\xrightarrow{\chi_{m,a(m/n)}}&S^1\\
  \downarrow\pi_{m,n}&&\Vert\\
  \mathbb Z/n\mathbb Z&\xrightarrow{\chi_{n,a}}&S^1 .
\end{array}
\]
A wrong arrow retaining label \(a\) at modulus \(m\) does *not* commute unless the frequency is correspondingly special. For \(n=3,m=6,a=1,x=1\), the genuine phase is \(1/3\), whereas the mutant is \(1/6\).

**Executable scope:** \`FiniteCyclicCharacter\` stores the label modulo \(n\); \`CyclotomicElement\` in the existing SUCC finite Fourier module gives exact roots of unity and exact orthogonality. A standalone 'prime 6' is forbidden in arithmetic local fields, but modulus \(6\) is perfectly valid as a finite cyclic observation. Confusing the two is a type error.

## 3. PD-02: global continuous dual \(\widehat{\mathbb Z}^{\,\vee}\simeq\mathbb Q/\mathbb Z\) (CLASSICAL, PAPER PROOF)

The character maps (2.1) form a directed system of cyclic duals, with structural maps \(a\bmod n\mapsto a(m/n)\bmod m\). Under
\[
  \iota_n:\mathbb Z/n\mathbb Z\longrightarrow\mathbb Q/\mathbb Z,
  \qquad a\bmod n\longmapsto a/n+\mathbb Z,
\]
these maps commute. Every rational modulo \(1\) is represented at some denominator, and two such fractions represent the same class precisely when they agree after transport to a common multiple. Thus the direct limit is \(\mathbb Q/\mathbb Z\).

Construct explicitly
\[
  \Phi:\mathbb Q/\mathbb Z\to\widehat{\mathbb Z}^{\,\vee},
  \quad
  \Phi(a/n)(x)=\exp(2\pi i\,a x_n/n). \tag{3.1}
\]
**Well-definedness:** transport numerator/denominator to a common multiple and apply (2.1) and compatibility of \(x\).

**Homomorphism:** both sides multiply phases under addition of rational frequencies.

**Injectivity:** the diagonal integer \(1\in\widehat{\mathbb Z}\) evaluates \(\Phi(a/n)(1)=e^{2\pi ia/n}\), so only the trivial class evaluates identically to \(1\).

**Surjectivity, with the actual topology:** Let \(\chi:\widehat{\mathbb Z}\to S^1\) be a continuous homomorphism. Select a neighborhood \(U\) of \(1\) in \(S^1\) containing no nontrivial subgroup (e.g. the open arc \(\operatorname{Re}z>0\)). Since \(\chi\) is continuous, \(\chi^{-1}(U)\) is an open neighborhood of \(0\). Some \(\ker\pi_n\) is contained in it. The subgroup \(\chi(\ker\pi_n)\) lies in \(U\), hence is trivial. Thus \(\chi\) factors through \(\pi_n:\widehat{\mathbb Z}\to\mathbb Z/n\mathbb Z\), so PD-01 shows \(\chi=\Phi(a/n)\) for some \(a\).

**Topology:** \(\widehat{\mathbb Z}\) is compact; with the compact-open topology, the dual is discrete. Indeed, all characters taking values in \(U\) on the *whole compact group* form an open neighborhood containing only the trivial character. Therefore \(\Phi\) is a topological group isomorphism when \(\mathbb Q/\mathbb Z\) has its discrete topology.

**Interpretive result:** Every continuous character of the full uncountable profinite carrier has a finite cyclic conductor and hence an exactly executable finite formula on each source program admitting residue queries. This does **not** imply every profinite *point* has a finite program or a uniformly bounded distinguishing horizon. The mathematical global-dual theorem uses compactness and continuous character structure.

Provenance: Pontryagin duality for inverse/direct limits; explicit version in Bell [B], §3, and Mathlib's finite abelian Pontryagin module [M].

## 4. PD-03: bidual recovery as compatible source residues (CLASSICAL)

Let \(Y=(\mathbb Q/\mathbb Z)_{\mathrm{disc}}\). Every group homomorphism \(\eta:Y\to S^1\) is continuous. For each \(n\), \(\eta(1/n)\) is an \(n\)-th root of unity, so write
\[
  \eta(1/n)=\exp(2\pi i x_n/n),\quad x_n\in\mathbb Z/n\mathbb Z.
\]
For \(n\mid m\), \(1/n=(m/n)(1/m)\) in \(Y\). Hence
\[
  x_m\bmod n=x_n .
\]
Thus \((x_n)\) is a unique element of \(\widehat{\mathbb Z}\). Conversely a compatible family defines \(\eta(a/n)=\exp(2\pi i a x_n/n)\), which is well-defined by the same naturality. The topologies agree by classical Pontryagin duality (and the inverse-limit/compact-open descriptions). Therefore
\[
  (\mathbb Q/\mathbb Z)^\vee\simeq\widehat{\mathbb Z}.
\]
On a finite source program, the phase of the character \(1/n\) is \(x_n/n\); multiplying by \(n\) recovers **exactly** the original residue \(x_n\). No finite list of such checks proves every global point identified. The entire family of characters is jointly separating.

## 5. PD-04: arithmetic source of \(\mathbb A_{\mathbb Q,f}/\widehat{\mathbb Z}\simeq\mathbb Q/\mathbb Z\) (CLASSICAL, PAPER PROOF)

Put
\[
 \mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p),
 \qquad
 \widehat{\mathbb Z}=\prod_p\mathbb Z_p\subset\mathbb A_f.
\]
Choose, for each genuine \(p\), the canonical principal part \(\{x_p\}_p\in\mathbb Z[1/p]\cap[0,1)\) representing \(x_p\bmod\mathbb Z_p\). Only finitely many are nonzero for a finite adele. Define
\[
  \operatorname{pp}:\mathbb A_f\to(\mathbb Q/\mathbb Z)_{\mathrm{disc}},
  \qquad x\longmapsto\sum_p\{x_p\}_p+\mathbb Z. \tag{5.1}
\]
**Homomorphism:** principal-part reduction is additive modulo \(\mathbb Z\); each place contributes its own p-primary torsion class.

**Kernel:** If each \(x_p\) is p-integral the sum vanishes. Conversely suppose the sum vanishes modulo \(\mathbb Z\). For finitely many denominators \(p^{k_p}\) choose their product \(N\); write the local terms \(a_p/p^{k_p}\). Multiplying the sum by \(N\) and reducing modulo \(p^{k_p}\) shows \(a_p\equiv0\pmod{p^{k_p}}\), since \(N/p^{k_p}\) is invertible modulo \(p^{k_p}\). Thus each term vanishes and every \(x_p\in\mathbb Z_p\). Therefore \(\ker\operatorname{pp}=\widehat{\mathbb Z}\).

**Surjectivity:** For every \(r\in\mathbb Q\), the diagonal finite adele \(r=(r)_p\) satisfies
\[
  \sum_p\{r\}_p-r\in\mathbb Z
\]
(the rational additive reciprocity identity, equivalent to the Chinese remainder decomposition). Hence \(\operatorname{pp}(r)=r\bmod\mathbb Z\). The diagonal map induces the explicit isomorphism \(\mathbb Q/\mathbb Z\simeq\mathbb A_f/\widehat{\mathbb Z}\).

**Topology:** \(\widehat{\mathbb Z}\) is compact open in \(\mathbb A_f\), hence the quotient is discrete. Consequently
\[
  0\to\widehat{\mathbb Z}\to\mathbb A_f
   \xrightarrow{\mathrm{pp}}\mathbb Q/\mathbb Z\to0 \tag{5.2}
\]
is a short exact sequence of locally compact abelian topological groups. The explicit map (5.1), rather than arbitrary set-theoretic cardinality, constitutes the carrier-equivalent interface.

**Exact implementation:** Every source-represented finite adele is \(u/d\), \(u\) a finite program for one profinite integer, \(d\in\mathbb Z_{>0}\). For \(d=p^v d'\) with \(p\nmid d'\),
\[
 \{(u/d)_p\}_p=
   \frac{\, (u\bmod p^v)(d'^{-1}\bmod p^v)\bmod p^v\,}{p^v}. \tag{5.3}
\]
The program queries only genuine p-power residues for primes dividing \(d\). It checks the subgroup kernel through two independently described conditions: zero principal parts at all exceptional places and zero total rational phase. The full source-adèlic topology is an imported classical theorem, not inferred from finite observations.

## 6. PD-05: the exact sequence does not split as an additive group (PROVED PAPER / CLASSICAL INGREDIENTS)

There is **no additive group homomorphic section** \(s:\mathbb Q/\mathbb Z\to\mathbb A_f\) with \(\operatorname{pp}\circ s=\mathrm{id}\).

**Proof:** The additive group \(\mathbb A_f\) is torsion-free (indeed a \(\mathbb Q\)-vector space). Every element of \(\mathbb Q/\mathbb Z\) has finite order. A homomorphism from a torsion group into a torsion-free group has zero image. Therefore any such \(s\) is the zero homomorphism, contradicting surjectivity of \(\operatorname{pp}\circ s\).

The result rules out even an abstract group splitting, hence in particular a continuous group splitting. It does **not** rule out a choice-of-representatives *set-theoretic* section. On each rational class \(1/n+\mathbb Z\), a diagonal lift \(1/n\in\mathbb A_f\) has \(\operatorname{pp}(1/n)=1/n+\mathbb Z\), yet \(n(1/n)=1\in\widehat{\mathbb Z}\setminus\{0\}\). The finite code demonstrates that obstruction for selected \(n\); the universal no-section assertion follows from torsion-free source law, not from the sample.

**SUCC relevance:** Observable quotient information can be exactly constructible and globally characterized while no group-law-preserving independent choice of lifts exists. A recursive model that silently inserts such a section is mathematically ghosting unavailable structure.

## 7. PD-06: Tate's finite sign and annihilator (CLASSICAL, SOURCE CROSS-IMPLEMENTED)

Fix the standard local additive character of conductor \(\mathbb Z_p\),
\[
 \psi_p(y)=\exp(-2\pi i\,\{y\}_p).
\]
Then
\[
 \psi_f(y)=\prod_p\psi_p(y_p)
          =\exp(-2\pi i\,\operatorname{pp}(y)).
\]
For \(r\in\mathbb Q/\mathbb Z\), \(z\in\widehat{\mathbb Z}\), equations (3.1) and (5.3) imply the exact normalized compatibility
\[
 \boxed{\chi_r(z)=\psi_f(-rz).} \tag{7.1}
\]
The plus sign used for the profinite character and the minus sign used for Tate finite Fourier phases have **not** been equated; the transport is the explicit inversion \(r\mapsto-r\). Our third independent implementation uses the existing \`RationalSChart\` with real coordinate zero and checks \(\chi_r(z)=\exp(-2\pi i\,\mathrm{TateSPhase})\) in phase coordinates, including extra unused prime places and valid \(S\)-projections.

On the full finite adelic group, the pairing \((x,y)\mapsto\psi_f(xy)\) makes \(\mathbb A_f\) self-dual (CLASSICAL). The annihilator of \(\widehat{\mathbb Z}\subset\mathbb A_f\) is \(\widehat{\mathbb Z}\) itself:
- For integral \(y\), all \(y_pz_p\in\mathbb Z_p\), so \(\psi_f(yz)=1\) for every \(z\in\widehat{\mathbb Z}\).
- For nonintegral \(y\), choose a genuine \(p\) where \(\{y_p\}_p\ne0\); the CRT idempotent \(e_p\in\widehat{\mathbb Z}\) with p-component \(1\) and other components \(0\) witnesses \(\psi_f(y e_p)\ne1\).
This demonstrates separating power using *original source-defined* prime projectors, not a fitted spectral model.

**Explicit normalization check:** For a diagonal rational \(r\in\mathbb Q\), the real character \(\psi_\infty(r)=e^{+2\pi i r}\) cancels \(\psi_f(r)=e^{-2\pi i\,\operatorname{pp}(r)}\), since \(\operatorname{pp}(r)\equiv r\pmod{\mathbb Z}\). Flipping only the finite sign destroys this property for most rationals, e.g. \(r=1/6\).

## 8. PD-07: exact finite Poisson theorem (CLASSICAL, INDEPENDENT EXACT FOURIER TEST)

Let \(G=\mathbb Z/n\mathbb Z\), \(H=d\mathbb Z/n\mathbb Z\) where \(d\mid n\). Then \(|H|=n/d\), \(H^\perp=(n/d)\mathbb Z/n\mathbb Z\), \(|H^\perp|=d\). For any \(f:G\to\mathbb C\), define **positive-phase** Fourier transform
\[
 \widehat f_+(k)=\sum_{x\in G} f(x)e^{2\pi i kx/n}.
\]
Fourier inversion, with negative phase, and the character orthogonality identity give
\[
 \boxed{
 \sum_{x\in a+H} f(x)=
   \frac{|H|}{n}
   \sum_{k\in H^\perp}\widehat f_+(k)e^{-2\pi i ka/n}.
 } \tag{8.1}
\]
**Proof:** Insert \(f(x)=(1/n)\sum_k\widehat f_+(k)e^{-2\pi i kx/n}\). The inner sum over \(x=a+h\) vanishes unless \(k\in H^\perp\), when it equals \(|H|e^{-2\pi i ka/n}\). No analytic limit is required.

The *finite* code calculates the left side from the original input table, the right side with the existing independent exact SUCC cyclotomic DFT, and the annihilator using a second integer-only brute group-character oracle. A wrong inverse-Fourier phase is refuted at a translated singleton subgroup: the mutation evaluates \(-a\) instead of \(a\). This is a model-calibration route toward, but not a proof of, the full adelic Poisson summation formula.

## 9. PD-08: what Tate global Poisson actually requires (EXTERNAL CLASSICAL THEOREM)

Write \(\mathbb A_\mathbb Q=\mathbb R\times\mathbb A_f\), with the real Fourier character \(\exp(2\pi ix_\infty y_\infty)\) and finite component \(\psi_f\). The diagonal \(\mathbb Q\) is discrete cocompact and self-annihilating in the self-dual additive adelic group:
\[
 \mathbb Q^\perp=\mathbb Q,\quad
 \operatorname{vol}(\mathbb A_\mathbb Q/\mathbb Q)=1 .
\]
For a genuine Schwartz–Bruhat \(f\in\mathcal S(\mathbb A_\mathbb Q)\) with the corresponding Haar normalization, Tate's Poisson summation reads
\[
 \sum_{q\in\mathbb Q}f(q)=\sum_{q\in\mathbb Q}\widehat f(q). \tag{9.1}
\]
Poonen [P], §§5.2–5.5, supplies these exact mathematical statements and their analytic hypotheses.

**Not an inference from (8.1):** infinite adelic Fourier inversion, convergence, test-function topology, the real Gaussian and identification of measures are additional theorems. The current SUCC repository already contains a finite-source-description rational Gaussian tensor and a Tate local Mellin bridge; this benchmark independently checks its finite-frequency character layer and does not assert a new full proof of (9.1).

For RH work, the further completed signed Weil distribution, including true prime powers, the Archimedean Gamma term, pole terms, half-density and universal test-function positivity, remains a separate RH-hard arrow. There is no GNS/positivity promotion.

## 10. Novelty and limitations

**Classical mathematics, not original academic priority:** PD-01 through PD-08 are well-known harmonic analysis, elementary CRT, duality and Fourier identities. The new output here is an integrated SUCC *implementation and proof-audit protocol*: source-indexed categorical compatibility, signed phase transport, independent finite computations, boundary countermodels and explicit claim contracts. No peer review of this integration has occurred. The original program's epistemic framing is a proposal, not a theorem of physical observer behavior.

**Strong counterexamples and boundaries:**
- n→m dual transition with unchanged label (wrong); coefficient must multiply by m/n.
- Real plus with finite plus phase (wrong) vs real plus/finites minus (correct).
- Composite n=6 as a perfectly valid finite clock but invalid *prime place*.
- Finite clock aliases: two distinct original integers can agree at all moduli below any fixed horizon.
- A full inverse-limit point may lack a computable name, despite every individual continuous character having finite rational code.
- \(\mathbb A_f/\widehat{\mathbb Z}\) exact quotient exists but has no additive group section.
- A finite cyclic Poisson proof or matching sampled phases cannot establish full adelic Poisson or RH sign.
- Source labels/epochs are declared; they do not authenticate real instruments, historical observations, or physically performed infinite experiments.

## 11. Reproducibility and evidence artifacts

Implementation:
- \`observational_succ/pontryagin_source_duality.py\`
- \`observational_succ/finite_adelic_character_bridge.py\`
- \`observational_succ/pontryagin_tate_atlas.py\`
- \`observational_succ/finite_cyclic_poisson.py\`

Reusable baseline originals:
- \`observational_succ/edge_carrier_reconstruction.py\`
- \`observational_succ/finite_adele_localization.py\`
- \`observational_succ/tate_lattice_descent.py\`
- \`observational_succ/finite_fourier_carrier.py\`
- \`observational_succ/diagonal_adele_zeta.py\`

Tests:
- \`tests/test_pontryagin_source_duality.py\`
- \`tests/test_finite_adelic_character_bridge.py\`
- \`tests/test_pontryagin_tate_atlas.py\`
- \`tests/test_finite_cyclic_poisson.py\`

Probe: \`scripts/pontryagin_finite_adelic_probe.py\`. Required source provenance verification: \`scripts/verify_provenance.py\`.

Commands (record success separately once run, don't infer it from files):
\`\`\`bash
python -m unittest discover -s tests -p 'test_pontryagin_source_duality.py' -v
python -m unittest discover -s tests -p 'test_finite_adelic_character_bridge.py' -v
python -m unittest discover -s tests -p 'test_pontryagin_tate_atlas.py' -v
python -m unittest discover -s tests -p 'test_finite_cyclic_poisson.py' -v
python scripts/pontryagin_finite_adelic_probe.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
\`\`\`

**Pass:** exact finite identities + independently reviewed general classical proofs with correct sign, domain, topology. **Fail:** a specific counterexample to a typed finite claim or an incorrect proof premise. **Ambiguous:** numerical agreement beyond domain, missing original source data, or finite evidence claimed to prove an \(\omega\)-quantified theorem. Do not drop failing examples or upgrade global claims by CI success alone.

## References (independent provenance)

- **[P]** Bjorn Poonen, *Tate's Thesis*, MIT 18.786 notes (2015), §§4.4–4.8, 5.1–5.5; https://math.mit.edu/~poonen/786/notes.pdf ; accessed 2026-10-15. Original framework: John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, Princeton Ph.D. thesis (1950), Cassels–Fröhlich reprint (1967).
- **[B]** Jordan Bell, *The Pontryagin duals of Q/Z and Q and the adeles*, especially §3 on \(\mathbb Q/\mathbb Z\), inverse and direct limits and \(\widehat{\mathbb Z}\); https://jordanbell.info/LaTeX/mathematics/Qdual/Qdual.pdf ; accessed 2026-10-15.
- **[M]** Mathlib documentation, \`Mathlib.Analysis.Fourier.FiniteAbelian.PontryaginDuality\` (character basis on \`ZMod n\`, finite duality); https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FiniteAbelian/PontryaginDuality.html ; accessed 2026-10-15.
- **[T]** Mathlib documentation, \`Mathlib.Topology.Algebra.PontryaginDual\` (continuous characters, compact-open topology, contravariant map); https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/PontryaginDual.html ; accessed 2026-10-15.

## 12. Next mathematical benchmark (not claimed completed)

Construct explicit character-theoretic equivalence for \(\mathbb A_\mathbb Q/\mathbb Q\), verify the full self-annihilating diagonal rational lattice with a second analytic derivation, then reproduce Tate Poisson on a nontrivial Gaussian × \(p\)-adic compact-open generator with correct Haar measures, real place, source history and all domains. After that, recover the known functional equation and signed Weil distribution *without* assuming the sign, before considering an RH proof.

**RH PROVED: NO.**
