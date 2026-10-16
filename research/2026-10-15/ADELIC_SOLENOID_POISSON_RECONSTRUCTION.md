# Source-Indexed Reconstruction of the Rational Adelic Solenoid and Poisson Summation

**Observational SUCC — Classical Reconstruction Benchmark IV**  
Research date: 2026-10-15. Manuscript status: **research preprint draft, NOT peer-reviewed**.  
Branch: \`research/pontryagin-finite-adelic-duality-2026-10-15\`, parent \`research/edge-carrier-reconstruction-2026-10-15@7cc16f9a3a23b0a2f87bd7c9639cd5bd0757209b\`.  
Prior theorem package: \`research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md\`.  
**RH PROVED: NO.** None of the carrier theorems gives completed Weil positivity.

## Abstract

We reconstruct the classical additive rational adelic quotient and Poisson formula from finite prime-place and Archimedean carriers, with an explicit source-indexed categorical interface. The input is the profinite ring \(\widehat{\mathbb Z}=\varprojlim_n\mathbb Z/n\mathbb Z\), the finite adelic localization \(\mathbb A_f=\mathbb Q\otimes_{\mathbb Z}\widehat{\mathbb Z}\), its principal-part quotient \(\mathbb A_f/\widehat{\mathbb Z}\simeq\mathbb Q/\mathbb Z\), and the real carrier \(\mathbb R\). From these inputs we identify the rational solenoid
\[
 \mathbb A_{\mathbb Q}/\mathbb Q
   \simeq(\mathbb R\times\widehat{\mathbb Z})/\operatorname{diag}\mathbb Z
\]
and classify its continuous characters:
\[
 (\mathbb A_{\mathbb Q}/\mathbb Q)^\vee\simeq\mathbb Q_{\rm discrete}.
\]
The normalized global adelic character and local Pontryagin self-duality show that the annihilator of the diagonal \(\mathbb Q\) is \(\mathbb Q\) itself, with Haar covolume \(1\). A source-derived rational-coset spanning lemma reduces Poisson summation for **every** Schwartz–Bruhat test on \(\mathbb A_{\mathbb Q}\) to ordinary real Poisson summation on a rational lattice, with exact signs and Haar measures. Independent finite rational models test the full generator covariance, a three-way earlier-Tate character interface, and quantitative outward interval controls that falsify a missing-Haar normalization. All global harmonic-analysis facts are classical. The SUCC contribution here is a typed, reproducible **proof-reconstruction pipeline**, not a new analytic theorem or physical \(\omega\)-execution.

## 1. Source spaces, structure and evidence policy

Throughout, use mathematical carriers:
\[
 \widehat{\mathbb Z}=\prod_p\mathbb Z_p,\quad
 \mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p),\quad
 \mathbb A=\mathbb R\times\mathbb A_f.
\]
The topology of \(\mathbb A_f\) is the restricted-product LCA topology, not the full unrestricted product topology. Fix the normalized Haar measures
\(\operatorname{vol}(\mathbb Z_p)=1\), \(\operatorname{vol}(\widehat{\mathbb Z})=1\), and ordinary Lebesgue measure on \(\mathbb R\). Let
\[
 \psi_\infty(x)=e^{+2\pi i x},\qquad
 \psi_p(x)=e^{-2\pi i\{x\}_p},\qquad
 \psi_{\mathbb A}(x)=\psi_\infty(x_\infty)\prod_p\psi_p(x_p).
\]
Here \(\{x\}_p\) denotes the p-primary rational principal-part class in \(\mathbb Q/\mathbb Z\). The product is finite outside the standard p-integral places. This **real plus / finite minus** convention is fixed for all Fourier transforms
\[
 \widehat f(y)=\int_{\mathbb A}f(x)\psi_{\mathbb A}(xy)\,dx.
\]
Changing *both* signs yields a convention-equivalent theory; changing only one breaks diagonal rational reciprocity.

Each source-indexed code chart carries a declared source ID and epoch, not physical authentication. A finite program may represent some global mathematical point and answer each permitted residue query, without representing every point in the uncountable completed carrier. The mathematical proof status is separate from finite test status.

## 2. The finite input: source-exact sequence (imported, with explicit proof)

Previous benchmark PD-05 proves
\[
 0\to\widehat{\mathbb Z}\to\mathbb A_f
   \xrightarrow{\mathrm{pp}}(\mathbb Q/\mathbb Z)_{\mathrm{disc}}\to0,
 \qquad
 \mathrm{pp}(x)=\sum_p\{x_p\}_p\pmod{\mathbb Z}. \tag{2.1}
\]
The sum is finite, its kernel is precisely \(\widehat{\mathbb Z}\), and every class is represented by a diagonal rational finite adele \(q\in\mathbb Q\). Consequently
\[
 \mathbb A_f=\mathbb Q+\widehat{\mathbb Z},\qquad
 \mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z. \tag{2.2}
\]
For any positive rational \(D\), scaling (2.2) gives
\[
 \boxed{\mathbb A_f=\mathbb Q+D\widehat{\mathbb Z}},\quad
 \mathbb Q\cap D\widehat{\mathbb Z}=D\mathbb Z. \tag{2.3}
\]
This is the source of rational representatives for **all** compact-open finite-adèle cosets of \(D\widehat{\mathbb Z}\). It is not a claim that all global adeles admit finite *computable* encodings.

## 3. Theorem AS-01: the adelic quotient is a compact rational solenoid

**Theorem (CLASSICAL, DERIVED).** There is a canonical continuous group isomorphism
\[
 \mathbb A/\operatorname{diag}\mathbb Q
 \cong(\mathbb R\times\widehat{\mathbb Z})/\operatorname{diag}\mathbb Z. \tag{3.1}
\]

**Proof.** From (2.2), every \((x_\infty,x_f)\in\mathbb A\) can be written as a diagonal rational translate of a point in \(\mathbb R\times\widehat{\mathbb Z}\): choose \(q\in\mathbb Q\) such that \(x_f-q\in\widehat{\mathbb Z}\). The kernel of the induced map \(\mathbb R\times\widehat{\mathbb Z}\to\mathbb A/\mathbb Q\) is the diagonally embedded rational \(q\) satisfying \(q\in\widehat{\mathbb Z}\), i.e. \(q\in\mathbb Z\). Thus the quotient groups coincide algebraically. Both quotient topologies are the quotient LCA topologies; the source subspace \(\mathbb R\times\widehat{\mathbb Z}\) is an open subgroup of \(\mathbb A\) with image all of \(\mathbb A/\mathbb Q\), so the induced bijection is open and continuous. ∎

A measurable fundamental domain is
\[
 [0,1)\times\widehat{\mathbb Z}.
\]
The interval endpoint choices only affect a measure-zero set. Hence the quotient is compact and its covolume in our Haar normalization is exactly
\[
 \operatorname{vol}(\mathbb A/\mathbb Q)=1. \tag{3.2}
\]

**Executable chart.** \`RationalSolenoidChart\` stores \(t\in\mathbb Q\) and a finite-description \(z\in\widehat{\mathbb Z}\), with genuine gauge \((t,z)\sim(t+k,z+k)\) for \(k\in\mathbb Z\). It canonicalizes \(t\) into \([0,1)\) and preserves the compensating profinite shift. Equality of *arbitrary* profinite programs is not decided by finitely many probes. The program is only a dense rational-real chart in the actual real solenoid.

## 4. Theorem AS-02: all continuous solenoid characters are rational frequencies

**Theorem (CLASSICAL, DERIVED).** With the compact-open Pontryagin topology,
\[
 (\mathbb A/\mathbb Q)^\vee\cong\mathbb Q_{\rm discrete}. \tag{4.1}
\]

**Proof.** Since \(\mathbb R^\vee\cong\mathbb R\) and \(\widehat{\mathbb Z}^{\,\vee}\cong(\mathbb Q/\mathbb Z)_{\rm discrete}\) by PD-03, every character of \(\mathbb R\times\widehat{\mathbb Z}\) is a pair \((\lambda,r)\in\mathbb R\times(\mathbb Q/\mathbb Z)\), acting by
\[
 (t,z)\mapsto\exp(2\pi i\lambda t)\chi_r(z).
\]
Such a character descends through diagonal \(\mathbb Z\) iff it is trivial on every \((k,k)\), equivalently
\[
 e^{2\pi i k(\lambda+r)}=1\quad\text{for all }k\in\mathbb Z.
\]
Thus \(\lambda+r\in\mathbb Z\); therefore \(\lambda\in\mathbb Q\) and \(r=-\lambda\bmod\mathbb Z\). Conversely each \(q\in\mathbb Q\) gives one character
\[
 \boxed{\chi_q([t,z])=
     \exp(2\pi i(qt-\mathrm{pp}(qz)))}. \tag{4.2}
\]
The map \(q\mapsto\chi_q\) is an algebraic isomorphism. The original quotient is compact, so its Pontryagin dual is discrete. ∎

**Source separation.** In a gauge with \(0\le t<1\), if \(t\ne0\) the character \(q=1\) distinguishes the point from zero. If \(t=0\) but \(z\ne0\), there is some \(n\) with \(z_n\ne0\); then \(q=1/n\) gives a nontrivial phase. This proves characters separate mathematical solenoid points but provides **no uniform finite** search deadline or zero-test oracle for arbitrary presented profinite elements. \`RationalSolenoidChart.exact_nonzero_witness\` requires an actual separating residue where necessary.

## 5. Theorem AS-03: the global Fourier pairing and rational self-annihilator

The finite local additive character pairing \((x,y)\mapsto\psi_f(xy)\) induces a Pontryagin isomorphism \(\mathbb A_f\simeq\mathbb A_f^\vee\) (classical restricted-product self-duality). Its source-visible justification can be organized via the exact sequence:
- Restriction of any \(\chi\in\mathbb A_f^\vee\) to \(\widehat{\mathbb Z}\) gives an element of \(\widehat{\mathbb Z}^\vee\cong\mathbb Q/\mathbb Z\). A diagonal rational multiplier realizes this restriction.
- Subtract that multiplier's character. The remainder is trivial on \(\widehat{\mathbb Z}\) and factors through \(\mathbb A_f/\widehat{\mathbb Z}\cong\mathbb Q/\mathbb Z\).
- Its character is represented by a multiplier from \((\mathbb Q/\mathbb Z)^\vee\cong\widehat{\mathbb Z}\), giving surjectivity.
- Injectivity follows from local nondegeneracy: a nonzero coordinate \(y_p\) is detected by a finite adele supported at that prime. Topological identification follows by standard open-subgroup Pontryagin duality.

Combined with \(\mathbb R^\vee\cong\mathbb R\), the full adelic pairing \(\psi_{\mathbb A}(xy)\) identifies \(\mathbb A\simeq\mathbb A^\vee\).

For \(q\in\mathbb Q\), the character on \(\mathbb A/\mathbb Q\) from (4.2) is precisely the full adelic Fourier character with the *diagonal multiplier* \(q\). By (4.1), every character trivial on diagonal \(\mathbb Q\) arises in this way, and by injectivity of the adelic self-dual pairing,
\[
 \boxed{\mathbb Q^\perp=\mathbb Q\subset\mathbb A.} \tag{5.1}
\]
Together with (3.2), this supplies the normalization required for the adelic Poisson summation formula. The full LCA duality statements remain classical theorem imports, not outputs of finite samples.

## 6. Lemma AS-04: rational coset indicators span all finite-adèle test functions

**Lemma (CLASSICAL, WITH SOURCE-DERIVED REPRESENTATIVES).** Every \(g\in\mathcal S(\mathbb A_f)\) is a **finite linear combination**
\[
 g=\sum_{j=1}^M c_j\,\mathbf1_{u_j+D_j\widehat{\mathbb Z}},
 \qquad u_j,D_j\in\mathbb Q,\quad D_j>0. \tag{6.1}
\]

**Proof.** The space \(\mathcal S(\mathbb A_f)\) consists of compactly supported locally constant complex-valued functions. By local constancy and compactness of the support, \(g\) is invariant under some compact-open additive subgroup \(K\subset\mathbb A_f\). As the sets \(D\widehat{\mathbb Z}\) for \(D\in\mathbb Q^\times\) form a neighborhood basis of \(0\) among compact-open subgroups, choose \(D>0\) with \(D\widehat{\mathbb Z}\subset K\). Then \(g\) is constant on each coset of \(D\widehat{\mathbb Z}\) and nonzero on only finitely many such cosets (compact quotient of support by an open subgroup). By (2.3), every coset admits a rational representative \(u\), yielding (6.1). ∎

In particular, a test-generator interface need not encode all finite places one by one. It can encode the exact rational pair \((u,D)\), **provided the law proving that these finite descriptions span the honest compact-open test space is retained**.

## 7. Lemma AS-05: exact local Fourier transform of a rational coset

Let \(D>0\) and \(u\in\mathbb Q\). Normalize the finite additive Haar measure by \(\operatorname{vol}(\widehat{\mathbb Z})=1\).

Because \(\widehat{\mathbb Z}^\perp=\widehat{\mathbb Z}\), scaling gives
\[
 (D\widehat{\mathbb Z})^\perp=D^{-1}\widehat{\mathbb Z}.
\]
Its Haar volume is
\[
 \operatorname{vol}(D\widehat{\mathbb Z})
  =\prod_p|D|_p=\frac1D.
\]
By character orthogonality on a compact subgroup,
\[
 \boxed{
 \widehat{\mathbf1_{u+D\widehat{\mathbb Z}}}(y_f)
 =\frac1D\,\psi_f(u y_f)\,
    \mathbf1_{D^{-1}\widehat{\mathbb Z}}(y_f).
 } \tag{7.1}
\]
The finite Fourier phase is **negative**, by convention. At a diagonal rational frequency \(m/D\), global rational reciprocity gives
\[
 \psi_f(um/D)=e^{-2\pi i u m/D},
\]
and the support condition \(D(m/D)\in\widehat{\mathbb Z}\) holds for all integers \(m\). Conversely, a diagonal rational \(r\) lies in \(D^{-1}\widehat{\mathbb Z}\) iff \(Dr\in\mathbb Z\), i.e. \(r=m/D\).

The code \`RationalCoset.dual_diagonal\` checks rational-frequency support, phase and Haar exactly; \`dual_source_crosscheck\` independently checks the same phase using prior finite-adèle principal-part reconstruction. No numerical Fourier quadrature is used.

## 8. Theorem AS-06: full adelic Poisson from real Poisson

**Theorem (CLASSICAL, CONSTRUCTIVE REDUCTION).** For every
\(f\in\mathcal S(\mathbb A)=\mathcal S(\mathbb R)\otimes_{\rm alg}
\mathcal S(\mathbb A_f)\),
\[
 \boxed{\sum_{q\in\mathbb Q}f(q)=
        \sum_{q\in\mathbb Q}\widehat f(q).} \tag{8.1}
\]
Both series converge absolutely in the present Schwartz–Bruhat domain.

**Proof.** By AS-04 and the finite tensor construction, it suffices by linearity to take
\[
 f(x_\infty,x_f)=\varphi(x_\infty)
     \mathbf1_{u+D\widehat{\mathbb Z}}(x_f),
\]
where \(\varphi\in\mathcal S(\mathbb R)\), \(u\in\mathbb Q\), \(D\in\mathbb Q_{>0}\).

A diagonal rational \(q\) lies in \(u+D\widehat{\mathbb Z}\) iff
\((q-u)/D\in\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z\). Thus
\[
 \sum_{q\in\mathbb Q}f(q)
  =\sum_{n\in\mathbb Z}\varphi(u+Dn). \tag{8.2}
\]
Use the **positive-phase** real Fourier transform
\[
 \widehat\varphi_+(\xi)
  =\int_{\mathbb R}\varphi(x)e^{+2\pi i x\xi}\,dx.
\]
By AS-05, the finite Fourier support at diagonal rationals is exactly
\((1/D)\mathbb Z\), with amplitude \(1/D\) and phase
\(e^{-2\pi ium/D}\). Therefore
\[
 \sum_{q\in\mathbb Q}\widehat f(q)
  =\frac1D\sum_{m\in\mathbb Z}
     \widehat\varphi_+(m/D)\,e^{-2\pi ium/D}. \tag{8.3}
\]
But the **ordinary real Poisson summation theorem for Schwartz functions on the lattice \(u+D\mathbb Z\)** identifies (8.2) and (8.3). Finite linear combinations now establish (8.1) for the entire stated Schwartz–Bruhat space. ∎

**What was and was not proved.** The adelic formula (8.1) has been reduced to (i) a classical real Poisson theorem, (ii) the classical finite Fourier/Haar subgroup-orthogonality law and (iii) a source-derived exact rational-coset spanning theorem. This is a valid reconstruction of a known theorem, not a proof of real Poisson from SUCC axioms alone. No hidden limit of finite numeric samples is used.

**Alternative proof audit:** Tate/Poonen derive (8.1) directly through Fourier inversion on the compact quotient \(\mathbb A/\mathbb Q\). Our reduction has a different internal route and can fail differently: it is sensitive to the rational coset spanning, correct finite Haar volume, real transform sign and the cofinality of compact-open subgroups. Both approaches rest on classical harmonic analysis.

## 9. Example AS-07: shifted Gaussian and honest dual phase

Take \(\varphi(x)=\exp(-\pi t(x-a)^2)\), \(t>0\), \(a\in\mathbb Q\). Its real positive-phase transform is
\[
 \widehat\varphi_+(\xi)=
 t^{-1/2}\exp(-\pi\xi^2/t)\exp(2\pi ia\xi).
\]
Applying AS-06 yields
\[
 \boxed{
 \sum_{n\in\mathbb Z}e^{-\pi t(u+Dn-a)^2}
 =
 \frac1{D\sqrt t}\sum_{m\in\mathbb Z}
 e^{-\pi m^2/(D^2t)}e^{2\pi i(a-u)m/D}.
 } \tag{9.1}
\]
For \(u=a\), the phase vanishes. When \((a-u)/D=1/2\), the dual series alternates with sign \((-1)^m\). Dropping the factor \(1/D\), reversing only the p-adic sign or forgetting the shift changes the mathematical identity.

The code \`GaussianPoissonGenerator\` compares exact rational exponent coefficients and phase classes with the original source lattice, and checks the finite Haar/phase path against the independently written finite-adèle quotient.

## 10. AS-08: quantitative outward rational bounds (finite numerical falsification only)

The additional \`adelic_gaussian_interval.py\` provides a rigorous rational enclosure of **selected** Gaussian terms using the existing \`source_weil_hierarchy\` outward interval implementations of \(\pi\) and \(e^{-x}\). It is restricted to rational-square heat \(t=s^2\), rational \(D>0\), and original shifts with \((a-u)/D\in\{0,1/2\}\), so the dual Fourier phases are exactly \(+1\) or \((-1)^m\) and the amplitude \(1/(Ds)\) is rational.

For \(N>|a-u|/D\), put \(c=(u-a)/D\), \(b=tD^2\). Since \(e^x\ge x^2/2\) and \(\pi>3\),
\[
 e^{-\pi b(n+c)^2}\le
 \frac{2}{9b^2(|n|-|c|)^4}
 \quad (|n|>N).
\]
Integral comparison bounds the two-sided primal tail by
\[
 \boxed{E_P(N)\le
     \frac4{27\,t^2D^4\,(N-|c|)^3}.} \tag{10.1}
\]
Likewise, the absolute dual tail with its prefactor \(1/(Ds)\) is bounded by
\[
 \boxed{E_D(N)\le\frac{4D^3s^3}{27N^3}.} \tag{10.2}
\]
These estimates are deliberately conservative but purely rational and independent of the desired infinite identity. If outward enclosures of the primal and dual finite sums plus their tail bounds were disjoint, the proposed normalization would be **rigorously falsified**. Overlap of enclosures is only a finite consistency result.

A hostile experiment deliberately drops the finite Haar factor \(1/D\) at \(D=2\), \(t=1\): the incorrect dual series acquires double amplitude and is separated from the source primal by exact rational interval bounds. This constitutes a genuine **mathematically certified rejection of a mutant formula**, not a proof of an RH sign.

## 11. Falsification ledger and remaining obstacles

| Object or claim | Status | Falsifying test or proof boundary |
| --- | --- | --- |
| AS-01 rational solenoid carrier and covolume | CLASSICAL / PAPER PROVED | Test diagonal rational gauge and Haar-normalized fundamental domain |
| AS-02 all continuous solenoid characters indexed by discrete Q | CLASSICAL / PAPER PROVED | Require continuous character factorization, no numeric \(\omega\)-jump |
| AS-03 global adelic self-duality and Q^\perp=Q | CLASSICAL / PAPER DERIVED from standard local duality | Wrong finite sign, nonintegral local character, false rational annihilator |
| AS-04 rational finite-adèle compact-open generator span | CLASSICAL / PAPER PROVED | Must include arbitrary D∈Q_{>0}, not just integers or a single prime — **SUPERSEDED (integer conjunct): PR #131 / CTW-02 — integer scales with rational translates already span S(A_f) via exact disjoint refinement; only the "single prime" necessity stands. Original row preserved; see docs/CLAIM_SUPPLEMENT_CARRIER_TATE_WEIL.md CTW-02.** |
| AS-05 exact Fourier of u+D Zhat | CLASSICAL / PAPER PROVED + FINITE EXACT TESTED | Omitted Haar 1/D, wrong annihilator D^-1, omitted shift |
| AS-06 full Poisson for all S(A) via real Poisson | CLASSICAL / PAPER PROVED CONDITIONAL on familiar real Poisson | False test topology or missing linear spanning lemma |
| AS-07 exact shifted Gaussian theta specialization | CLASSICAL / FINITE EXACT SOURCE TESTED | Wrong shift/conjugate phase, wrong Gaussian heat scaling |
| AS-08 rational interval finite consistency with tail proof | PROVED LOCAL / EXACT, CI validation pending | Disjoint intervals refute candidate formula; overlapping intervals do not prove infinity |
| Full SUCC original real-world causal-history embedding | UNVERIFIED PHYSICAL GENERALIZATION | Source IDs are labels; mathematical simulation is not original source attestation |
| Tate idelic Mellin → fully completed signed Weil quadratic | CLASSICAL THEORY / NEW SUCC FUNCTOR IDENTIFICATION OPEN | Require true \(\Lambda(p^k)\), Gamma, poles, half-density, domains |
| Source-derived all-test Weil positivity and RH | UNVERIFIED RH-HARD | No positivity assumed, no zero locations as source input |

All code-generated finite outputs are mathematical receipts, not analytic theorems. See exact CI job and revision history in the research branch.

## 12. Why this matters to SUCC's field taxonomy

This benchmark cleanly separates:
- **Simple access to individual queries:** A rational source description \((u,D)\) specifies a full finite-adèle compact-open generator; every rational sample, Fourier frequency and finite prime exceptional list can be examined with finite exact work.
- **IdealHard-type proof/access distinction:** The complete infinite Poisson identity is proved by a finite mathematical argument **relative to known real Poisson and LCA laws**. This does not execute infinitely many lattice terms; different mathematical proof/observer targets can have different effective statuses.
- **No phantom shortcuts:** A finite list of observed characters does not identify an arbitrary profinite source point. The global character is lawful because the entire rational/profinite/Haar/topological source law is specified. No invented alternate \(\Lambda\)-tape, hidden positive Hilbert norm or guessed real place is accepted.

No claim that the physically accessible RH problem is intrinsically Simple/IdealHard/Fucked follows from these solved reconstructions.

## 13. Repository artifacts and bibliography

**Files:** \`observational_succ/adelic_solenoid_duality.py\`, \`observational_succ/adelic_poisson_reconstruction.py\`, \`observational_succ/adelic_gaussian_interval.py\`, with \`tests/test_adelic_solenoid_duality.py\`, \`tests/test_adelic_poisson_reconstruction.py\`, \`tests/test_adelic_gaussian_interval.py\`. Reuse \`observational_succ/finite_adelic_character_bridge.py\`, \`observational_succ/pontryagin_source_duality.py\`, and the preserved earlier S-atlas and Gaussian source test implementations.

**Primary and reliable mathematics:**
1. John Tate (1950), *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, Princeton thesis (reprinted Cassels–Fröhlich 1967), local and global Fourier chapters.
2. Bjorn Poonen (2015), *Tate's Thesis*, MIT Number Theory II lecture notes, §§4–5, especially §5.5 (adelic Poisson summation) and §5.2 (duality and Haar): https://math.mit.edu/~poonen/786/notes.pdf.
3. Jordan Bell (2015), *The Pontryagin duals of Q/Z and Q and the adeles*, rational additive reciprocity, rational solenoid and local character analysis: https://jordanbell.info/LaTeX/mathematics/Qdual/.
4. Mathlib's Fourier duality and finite cyclic Fourier formalizations: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FiniteAbelian/PontryaginDuality.html.
5. Existing SUCC theorem dossier \`research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md\` (PD-01–PD-13); the author's carrier reconstruction foundation \`research/2026-10-15/EDGE_CARRIER_RECONSTRUCTION_LAB.md\`.

**Academic priority claim:** NONE for known number theory and harmonic-analysis theorems. Independent review and proof assistant formalization remain possible future research contributions. The new structured artifact is a SUCC-specific source-indexed reconstruction with independently falsifiable interfaces.

**RH PROVED: NO.**
