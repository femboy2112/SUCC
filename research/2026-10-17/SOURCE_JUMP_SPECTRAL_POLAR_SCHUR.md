# SOURCE-JUMP SPECTRAL POLAR SCHUR: Effective First-Prime Rank, Rank-One Per Parity, and a Finite Fourier Certificate

**Research date:** 2026-10-17. **Source and parent:** SUCC original signed completed Suzuki/Weil source, frozen Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, from source commit `dc6b7e3`; branch child of SUCC draft #156 `research/source-covariant-ims-fucc-resonance-2026-10-17@b49904ca529de4204e602c415842159fe7a3ebf6`. Existing source-conditional SCIMS-08/09 are inherited with their paper premises; this round leaves the source module and its archives unchanged. See Suzuki, *Weil’s quadratic form via the screw function*, arXiv:2606.09096v3 (2026), especially §§2 and 8, for the original local Weil representation.

**Status:** JS-01–JS-07 are classical functional-analytic/paper derivations specialized to the unchanged canonical source; `source_jump_spectral.py` contains executed exact rational finite surrogate calculations and a source SHA-authenticated **rank/gap and finite Ritz** adapter. Source projector matrices and source-specific polar high Green functions are NOT calculated. We neither prove `S_4 >= 0` at `a=1/2` nor all-radius Weil positivity. **RH OPEN.** No nontrivial zeta-zero coordinates are inputs, and no sampled independent composite-6 prime impulse exists.

## 1. The real signed source in a common primitive carrier (JS-01)

Let `I=(-a,a)`, `u in L²_0(I)`, `F(x)=int_-a^x u(t)dt`, extended by zero outside I. On the original mean-zero smooth test core the *complete* signed source quadratic is precisely

\[
\boxed{Q_a(F')=\mathcal E^+_a(F)-M_a\|F\|_2^2
 +2|\langle F,c_a\rangle|^2-2|\langle F,s_a\rangle|^2.}\tag{1}
\]

Here `c_a=cosh(x/2) 1_I`, `s_a=sinh(x/2) 1_I`,

\[
M_a=C_\infty+2\sum_{\substack{n=p^k\\\log n<2a}}\frac{\Lambda(n)}{\sqrt n},
\quad
\mathcal E^+_a(F)=\frac12\iint_{\mathbb R^2}
|F(x)-F(y)|^2J(|x-y|)dxdy
+\sum_n w_n\|F-T_{\log n}F\|_2^2,
\]

\(J(r)=e^{-r/2}/(1-e^{-2r})\), \(w_n=\Lambda(n)/\sqrt n\), and the genuine source supplies one real Gamma, negative contact \(-C_\infty\), **both** pole terms and correct half-density. At `a=1/2`, only `(n,p)=(2,2)` is active; the authenticated source check refuses the fake independent n=6 coefficient.

The positive jump form is diagonal in the **full-line** Fourier transform of zero-extended F:

\[
\mathcal E_a^+(F)=\int_{\mathbb R} h_a(\xi)|\widehat F(\xi)|^2d\xi,
\quad h_a(\xi)=\sum_{j\ge0}\frac{4\xi^2}{(4j+1)[\xi^2+(4j+1)^2/4]}
 +2\sum_n w_n(1-\cos(\xi\log n)).\tag{2}
\]

The separate positive shift jump and negative compensating mass must **not** be split into divergent infinite objects as a→∞; the statement is for fixed finite a with a finite genuine active tape. The polar terms are source-defined signed rank one per reflection parity, not positive covariance substitutes.

### Domain and closure

Initially (1) is the original smooth-primitive Weil form. Define \(\mathcal L_a^+\) by the closure of the nonnegative full-line jump quadratic restricted to zero-extended compactly supported primitives. The Fourier logarithmic growth makes the form densely defined, closed on its completion, with the smooth test core taken by definition; the source potential and polar forms are bounded on \(L^2(I)\). Equality with the original Weil sign on smooth tests is enough for the RH criterion. Any additional assertion that all closed-domain eigenvectors represent physically performed observations is specifically **NOT CLAIMED**.

## 2. Effective finite spectral cutoff: **453 original-source jump modes** (JS-02)

Let \(P=\mathbf1_{[0,7]}(\mathcal L_{1/2}^+)\), \(Q=I-P\). This spectral projector exists by the self-adjoint spectral theorem, and its range is finite-dimensional. **Its eigenfunctions and matrix entries have not been computed.** The remarkable source-specific result of this round is an explicit, moderate **rank upper bound**.

The genuine Gamma Fourier multiplier has the source-given positive OU rungs

\[
 m_\Gamma(\xi)=\sum_{j\ge0}\frac{4\xi^2}{d_j(\xi^2+d_j^2/4)},\qquad d_j=4j+1.
\]

Each rung is monotone in \(|\xi|\). Evaluate the first `J=256` genuine Gamma rungs at the INTEGER source-independent test frequency `R=76` using exact rational arithmetic:

\[
\boxed{
\mu_{76}:=\sum_{j=0}^{255}\frac{16\,76^2}
{(4j+1)[4\,76^2+(4j+1)^2]}>\frac{3927}{500}.}
\tag{3}
\]

No floating point, Gamma rescaling, fitted spectrum, prime substitution or zero data are involved. The direct exact `fractions.Fraction` comparison is executed by `exact_gamma_prefix_multiplier(76,256)`, which checks the genuine source coefficient formula. All omitted Gamma rungs are positive, so \(m_\Gamma(\xi)>3927/500\) for all \(|\xi|\ge76\).

Partition the unit-length interval \(I=(-1/2,1/2)\) into **N=453 equally spaced cells** and let \(E_N\) be their L² orthogonal averaging projector. For every zero-extended F in the full original Gamma/FUCC positive form domain, let F_R be the full-line Fourier truncation at R=76. The band Fourier tail and cellwise mean-zero Poincaré inequality imply

\[
\|(I-E_N)F\|_2
\le\|F-F_R\|_2+\|(I-E_N)F_R\|_2
\le\sqrt{\frac{\mathcal E_a^+(F)}{\mu_{76}}}
+\frac{76}{453\pi}\|F\|_2.\tag{4}
\]

Proof: the first norm squares to a Fourier tail; on the full-line band \(\|F'_R\|_{L²(\mathbb R)}\le76\|F\|\); restriction to I and the **ordinary cell-average** Wirtinger/Poincaré inequality give the second term. This is **not** the false derivative-after-Legendre-projection contraction already refuted in SUCC #135/#155.

When \(E_NF=0\), since π>3 and equation (3),

\[
\boxed{
\mathcal E_a^+(F)>
\frac{3927}{500}\left(1-\frac{76}{3\cdot453}\right)^2\|F\|^2
=\frac{2154730501}{307813500}\|F\|^2
>7\|F\|^2.}\tag{5}
\]

If the spectral subspace of \(\mathcal L_{1/2}^+\) with eigenvalues ≤7 had dimension >453, it would contain a nonzero vector in the codimension-453 kernel of E_N, violating (5). **Thus**

\[
\boxed{\operatorname{rank}\mathbf1_{[0,7]}(\mathcal L_{1/2}^+)\le453.}\tag{6}
\]

Our earlier rough logarithmic-only estimate produced a **valid but far weaker rank bound 262,144** using R=65536 and N=4R. The source-true finite OU prefix shrinks that proof budget by a factor >570. Neither is an actual spectral-projector computation.

### Bound on the *complete signed* high block

The pinned original first-prime source intervals prove `C_infty <43/8`, `w_2<1/2`, and `||s||²=sinh(1/2)-1/2<1/32`. Hence

\[
 M_{1/2}<51/8,\qquad B=M+2\|s\|^2<103/16.
\]

On Q, the positive jump energy is at least `7 ||F||²`, the positive cosh channel may be discarded, and the only negative polar channel costs at most `2||s||²`. Consequently

\[
\boxed{QH_aQ\succeq(7-B)Q\succ\frac9{16}Q,}
\qquad\boxed{\|(QH_aQ)^{-1}\|<\frac{16}{9}.}\tag{7}
\]

This bounded high inverse is a different object from the compact original zero-shift inverse in the Legendre-u Schur decomposition. It does **not** prove the low signed source positive. The first-prime radius a=1/2 and true Gamma/prime data are load-bearing; no uniform all-a bound follows.

## 3. Complete polar Schur — just one scalar per parity (JS-03)

Reflection \(F(x)\mapsto F(-x)\) commutes with the original positive jump operator (all genuine log-prime shifts occur in a symmetric pair), so \(P,Q\) commute with parity. The real cosh vector \(c\) is even; sinh \(s\) is odd. Therefore the polar channels never mix in either the low or high spectral space.

Let \(A_0=\mathcal L^+_a-MI\), \(c_P=Pc\), \(s_P=Ps\), \(c_Q=Qc\), \(s_Q=Qs\), and define the two **positive** high resolvent scalars

\[
\alpha_c=\langle c_Q,(Q A_0 Q)^{-1}c_Q\rangle,
\quad \alpha_s=\langle s_Q,(Q A_0 Q)^{-1}s_Q\rangle.\tag{9}
\]

The bare \(QA_0Q\) has gap >`7-51/8=5/8`, so its inverse is bounded. High odd positivity also gives `2 alpha_s<1`. On even high, Sherman–Morrison for \(A_0+2cc^*\) yields `alpha_c/(1+2alpha_c)`; on odd high, for \(A_0-2ss^*\) it yields `alpha_s/(1-2alpha_s)`.

Completing the genuine signed high block **exactly** gives the finite low short

\[
\boxed{
S_P=P(\mathcal L^+_a-MI)P
+\frac{2}{1+2\alpha_c}|c_P\rangle\langle c_P|
-\frac{2}{1-2\alpha_s}|s_P\rangle\langle s_P|.}\tag{10}
\]

And (because the full high block is strictly positive)

\[
\boxed{H_a\succeq0\iff S_P\succeq0.}\tag{11}
\]

The high correction has at most **two source-polar channels**, one per parity. No derivative-after-Legendre-projection contraction or inversion of compact \(D\) is invoked. At a=1/2, even the **odd polar amplification** is bounded:

\[
\alpha_s\le\frac{\|s\|^2}{7-M}<\frac1{20},\qquad
0<\frac{2}{1-2\alpha_s}<\frac{20}{9}.\tag{12}
\]

**Decisive structural consequences.** On the *odd* jump sector, the signed source equals \(A_{0,odd}-2ss^*\): any negative direction of \(A_{0,odd}\) would already be a genuine negative signed witness. For the *even* sector, \(A_{0,even}+2cc^*\) can remove at most one negative direction; two negative directions in the baseline would survive. These are conditional counterexample detectors, not zero claims.

### Exact finite-rational verification

`exact_spectral_projectors` constructs and verifies **complete** spectral projectors by Lagrange polynomial interpolation for a declared rational symmetric matrix and declared rational eigenvalues; it rejects nonannihilating values. `exact_polar_schur` checks parity/source diagonalization, computes both \(\alpha\) and the exact finite short, and verifies its PSD verdict agrees with the original signed finite source. The positive four-site cycle exhibits positive true signed energy after a rank-one cosh repair; changing the contact or dropping cosh yields exact negative rational witnesses. A five-state example has nonzero **both** high polar responses. These are **synthetic matrices**, never the original Suzuki spectrum.

**Open cost:** the actual jump operator's low spectral eigenvectors, \(\alpha_c\), \(\alpha_s\), and their rigorous finite matrix intervals have not been computed. Equation (7) is an upper bound on rank, not an implemented `rank <=262144` eigenanalysis. An unknown eigenvalue on the threshold is included in P, keeping the high bound valid; a numerical eigenvalue near threshold is not a certified spectral projector.

## 3B. Source-conditional **at most five** genuinely negative bare-jump modes (JS-08)

There is an important source-specific improvement to the coarse `rank P_[0,7] <=262144`. It does **not** construct an eigenspace but dramatically limits how many modes can actually lie *below the true contact threshold* `M`.

The independently inherited and source-gated WB4 theorem proves the **complete signed original** high block `D_4 >= (63/500)K` on the genuine mean-zero four-mode orthogonal complement at a=1/2. Since `K` is injective, this implies the Morse negative index of the full signed Weil form is at most **four** (two even and two odd): any negative subspace of dimension five would intersect that positive high complement nontrivially. Passing from derivative u to its primitive F is an invertible linear map on the original test core and does not change finite negative index; closure follows by form continuity.

The bare jump baseline is `A_0=L^+ - M I`. Because

```
A_0 = H - 2|c><c| + 2|s><s|,
H_even = A_0_even +2|c><c|,
H_odd  = A_0_odd  -2|s><s|,
```

subtracting the *single* even rank-one positive cosh term can add at most one negative direction. To prove it without spectral perturbation terminology, restrict any A0-negative subspace to the codimension-one condition `<F,c>=0`; on that restricted subspace `Q_H(F) <= Q_A0(F)<0`. Similarly A0-odd negativity implies original H-odd negativity because its pole is negative. The authentic source WB4 therefore gives the actual jump spectrum the bounds

\[
oxed{\#\{\lambda_j(\mathcal L_{1/2,even}^+)<M\}\le3,\qquad
\#\{\lambda_j(\mathcal L_{1/2,odd}^+)<M\}\le2,\qquad
\#\{\lambda_j(\mathcal L_{1/2}^+)<M\}\le5.}	ag{12b}
\]

This is a strictly stronger **index/rank bound at the moving threshold M**, not a replacement for the quantitative gap at fixed cutoff 7. An eigenvalue could equal M, and the next spectral gap above M is not source-quantified. Choosing a cutoff just above M could include more than five modes; the computation of actual polar projections and high scalar Green responses is still open. The `source_jump_spectral.authenticate_original_jump_rank_budget()` adapter **replays the original source WB4 infinity-source certificate**, verifies its original source blob and global κ=63/500, and reports the 3/2/5 bounds as conditional paper results. This uses true source coercivity, not a fictitious positive finite compression.

## 3C. An authentic arithmetic baseline is **strictly negative**, yet the completed polar source repairs it (JS-09)

The full installed-original-source integration now evaluates the first two *genuine* primitive Legendre Ritz vectors, without accessing zeros. For \(u=P_1(2t)=2t\) define \(F=Vu=t^2-1/4\); this is an **EVEN** primitive. The strict real-source packet subtracts the entire completed genuine polar pairing **once** from the original signed \(G_J\) in u-coordinates and carries the positive omitted-Gamma tail \(\tau_J\|u\|^2\). At 12 true Gamma modes, exact rational interval arithmetic and the protected source SHA produce

\[
\boxed{-0.056408<\langle F,(\mathcal L^+-M)F\rangle<-0.056084<0.}\tag{12c}
\]

The omitted original Gamma contribution has a **positive** sign, so a negative upper endpoint (including the tail) is a true, source-conditional negative direction for the *bare* jump-minus-potential baseline. It is **not** a negative direction of the complete signed Weil form. The already established source WB4 theorem gives complete original four-low \(A_4>0\), hence this same test's **completed** signed energy is positive; the authentic positive completed cosh-polar rank-one term therefore genuinely repairs a negative baseline value. Numerically the signed polar correction is around +0.05625, but the sign assertions rely on source intervals and inherited WB4, not that decimal estimate.

The corresponding **ODD** primitive \(F=VP_2(2t)\) has a strictly positive certified bare-baseline Ritz value in the same source test,

\[
0.000225<\langle VP_2,(\mathcal L^+-M)VP_2\rangle<0.000420,
\]

which does **not** imply positivity of the entire odd jump sector.

Since \(\mathcal L^+\) has compact resolvent, (12c) proves at least one genuine **even jump eigenvalue strictly below M**. Combined with inherited WB4 and JS-08,

\[
\boxed{1\le\#\{\lambda_j(\mathcal L^+_{even})<M\}\le3,\quad
0\le\#\{\lambda_j(\mathcal L^+_{odd})<M\}\le2.}\tag{12d}
\]

This is an actual new source-specific spectral *index* certificate, not an invented model and not a false RH counterexample. It determines that the rank-one even polar correction is mathematically essential. **It does not locate any eigenvalue of L+ or prove that the positive polar channel repairs every possible negative baseline direction.** Under a hypothetical proof of complete even-sector positivity, rank-one inertia would force the even bare baseline to have *exactly one* negative eigenvalue. That conditional rigidity suggests testing the lower jump spectrum itself, not endlessly expanding arbitrary positive Gram samples.

**Reproduction:** \`authenticate_original_jump_rank_budget()\` replays WB4; \`authentic_primitive_ritz_packet(1,12)\` certifies the strict negative bare energy with full omitted Γ tail. The dedicated GitHub source test asserts the strict sign; the true source partial integration has its original byte provenance, not a synthetic source label. Hosted 3.10 and 3.13 runs at the earlier head independently printed the same outward rational bounds; the new strict assertion awaits exact-head replay before promotion to hosted PASS.

## 4. A fully constructive alternative: monotone Fourier-band lower envelopes (JS-04)

A stronger form of “effective partition” avoids needing the exact spectral eigenspaces to write a *finite sufficient sign certificate*.

Fix `R=2^k`, `k>=1`, and the rational Gamma lower `mu_k=(69/125)k`, so the genuine multiplier satisfies `h_plus(xi)>=mu_k` whenever `|xi|>=R`. Define the bounded **source-generated lower quadratic form**

\[
\mathcal E_{k}^{\rm low}(F)=
\int_{-R}^{R}h_+(\xi)|\hat F(\xi)|^2d\xi
+\mu_k\int_{|\xi|>R}|\hat F(\xi)|^2d\xi.
\]

It obeys \(0\le\mathcal E_k^{low}(F)\le\mathcal E_a^+(F)\) for the actual original source. As `k` increases, these lower forms are monotone increasing: on each newly admitted frequency annulus the genuine h is at least the preceding high floor; the floor also increases. They converge pointwise to the true original positive jump form on its finite-energy domain. The corresponding source signed lower bound is

\[
\boxed{
H_a\succeq (\mu_k-M_a)I + T_R^*(h_+-\mu_k)T_R
+2|c\rangle\langle c|-2|s\rangle\langle s|,}
\tag{13}
\]

where \(T_R\) is the unitary Fourier transform restricted to `[-R,R]` from functions supported in I. The **frequency correction** is compact (bounded multiplier times a Hilbert–Schmidt truncated Fourier transform). Its sign is not assumed. The essential-spectrum floor is `mu_k-M_a`, positive for sufficiently large k.

### A finite Fourier readout with computable operator error

For k≥1, the authentic original first-prime multiplier obeys the rational analytic bounds on \([-R,R]\):

\[
 |h_+'(\xi)|<17/2,\qquad 0\le h_+(\xi)<k+24,
 \quad 0<\mu_k<k.\tag{14}
\]

Proof: differentiating each source Gamma rung and maximizing shows `|m_j'|<6/(4j+1)^2`, summing by a monotone integral yields `<15/2`; the genuine prime2 derivative adds `<1`. For the magnitude, split Gamma rungs at `d=R`. Low rungs contribute `<4+log R<4+k`; the high tail is `<16/R+2<=18`, and the prime contribution `<2`. Every bound uses source integer coefficients and true n=2 weight, not fitted floating constants.

For \(F\in L^2(-1/2,1/2)\), the unitary Fourier transform satisfies

\[
|\hat F(\xi)|^2\le\tfrac16\|F\|^2,\qquad
\left|\frac d{d\xi}|\hat F(\xi)|^2\right|\le\tfrac16\|F\|^2,
\tag{15}
\]

using π>3, Cauchy–Schwarz and support |x|≤1/2. Therefore \((h_+(\xi)-\mu_k)|\hat F(\xi)|^2\) has Lipschitz constant bounded by

\[
 L_k=\frac{4k+65}{12}\|F\|^2.\tag{16}
\]

Let \(\xi_j=-R+(j+1/2)\frac{2R}{N}\) be a rational midpoint grid with step \(\Delta=2R/N\). The elementary midpoint error estimate on a Lipschitz function gives a **uniform operator-form bound**

\[
\boxed{\left|\int_{-R}^{R}(h_+-\mu_k)|\hat F|^2
 -\Delta\sum_{j=0}^{N-1}(h_+(\xi_j)-\mu_k)|\hat F(\xi_j)|^2\right|
\le \frac{L_kR^2}{N}\|F\|^2.}\tag{17}
\]

All \(h_+(\xi_j)\) are authentic **computable real numbers** with arbitrary finite rational outward accuracy, from the rational Gamma rung partial sums and analytic tail plus the source-interval log2/sqrt2/cosine series. Given finite certificates \(d_j^{lo}\le h_+(\xi_j)\), the truly original form satisfies

\[
\boxed{H_a\succeq c_0I+\sum_j\Delta(d_j^{lo}-\mu_k)|\phi_j\rangle\langle\phi_j|
+2|c\rangle\langle c|-2|s\rangle\langle s|,}
\quad c_0=\mu_k-M_a^{up}-L_kR^2/N.\tag{18}
\]

Here \(\phi_j(x)=e^{i\xi_jx}/\sqrt{2\pi}\) on I. **This statement is a sufficient finite-dimensional sign certificate** when `c0>0`. It is not conditional on a spectral gap of the true jump operator; it uses a direct source Fourier tail bound. Complex conjugate frequency pairs can be converted to paired real cosine/sine features.

### Finite Gram test, with no high inverse

Let \(\Phi\) collect all frequency features and the two polar vectors, let \(K=\Phi^*\Phi\) be their **true source feature Gram**, and let `D` be the diagonal signed weights \(\Delta(d_j^{lo}-\mu_k),+2,-2\). Since `c0>0`, the right side of (18) is nonnegative on all \(L^2(I)\) **if and only if**

\[
\boxed{\mathcal M=c_0 K+KDK\succeq0.}\tag{19}
\]

To prove this, decompose any F orthogonally as \(F=\Phi v+F_\perp\). On the complement, the quadratic is just `c0||F_perp||²`; on span(Φ) it is `v* (c0 K+K D K)v`. This remains correct for linearly dependent features because the Gram kernel is handled exactly, not inverted. A verified PSD matrix (with rigorous enclosures for all transcendental Grams and source coefficients) would imply **actual original first-window positivity**, without a Legendre zero-shift inverse. An indefinite *lower* matrix is only an INCONCLUSIVE sufficient-test failure, not a true original negative witness.

The implementation `exact_feature_gram_decision` proves (19) in **finite rational surrogate feature spaces** and produces exact negative witnesses against a bad candidate; it does NOT yet populate the astronomical original Fourier feature Gram or authenticate arbitrary sample coefficients. Incorrect Gram PSD, false polar sign, or unavailable observations are rejected or retained as explicit debts.

**First conservative finite budget:** at `k=16`, `R=65536`, absolute quadrature error `<1/4` requires `N=184683593729` two-sided frequency samples (rank at most `N+2`). That enormous number is a rigorous bound for **this deliberately crude Lipschitz certificate**, not a computational run or minimal required resolution. No source eigenprojector is needed to state or eventually run this finite sufficient test. Source-adapted analytic kernel integration and higher-order quadrature are the obvious major optimization targets.

## 5. Why strict positivity is semidecidable but singular sign is still hard (JS-05)

Assume the unchanged first-prime source formula and the effective original-source evaluations above. If the original first-window form has a **strict positive spectral margin** \(H_a\succeq\delta I\), \(\delta>0\), then the increasing Fourier lower forms in (13) eventually have a strictly positive margin. Reason: suppose not; take normalized near-minimizers of a cofinal sequence of lower forms. Their positive Gamma/FUCC energies are uniformly bounded by the negative-potential/true-polar norm plus the chosen near-minimum. Since the lower Gamma Fourier floor tends to ∞ outside every fixed frequency region, their spectral tails are uniformly small. Compact support in I then makes this near-minimizer sequence precompact in L². Any norm-one limit lies in the full closed form domain by monotone lower semicontinuity, and violates the assumed strictly positive original form. Contradiction. This is a standard compact/monotone-form variational argument; it gives **no explicit k** without a source spectral margin.

Because the finite midpoint quadrature and source-transcendental evaluations can be made arbitrarily sharp, a **fair search over k, N and finite interval precision** would eventually discover a strictly PSD finite sufficient certificate if such a strict source margin exists. It is NOT a total RH decision procedure. For a singular nonnegative original source, conservative lower packets can remain indefinite at every finite stage. A true negative original-source rational test, if one exists, requires a separately authenticated *upper* evaluation of its signed energy; a negative finite Fourier lower packet proves nothing about the original sign. One successful first-window sign does not prove all-support Weil positivity.

**Comparison with the exact spectral P route:** equation (10) is a canonical finite-dimensional *equivalence* with source-generated eigenvectors and rank-two high polar response, but the real eigenprojector is not effectively constructed here. Equations (13)–(19) are a fully explicit **sufficient certificate format**, with a source-independent numerical error bound and computationally effective sample evaluation, but at an impractical rank. Both genuinely avoid inverting the compact Legendre-u high operator.

## 6. Independent hostile controls, evidence authority and where the math can break (JS-06)

- **Main source:** frozen original source SHA, genuine prime wavefront `(2,2)`, one real Gamma, complete pole pair, original contact; no zero-coordinate input. These are checked by the hosted source adapter. Source-domain identification is inherited paper mathematics, not certified merely by matching bytes.
- **Finite rational spectral solver:** Lagrange spectral projectors validated against the actual finite matrix annihilator; reflection/within-eigenspace polar orthogonality checked; exact Sherman–Morrison polar corrections; finite all-mode PSD compared with low short; synthetic negative contact and removed-positive-pole mutants return exact rational negative witnesses.
- **Negative control:** `c·s=0` alone does not imply they decouple in every source spectral eigenspace; the solver rejects this insufficient condition. A false high gap or forged eigenvalue list is rejected.
- **Spectral rank:** a cell-average approximation in *ordinary* L² is the lawful tool for the positive Gamma jump operator; it is **not** the refuted derivative-after-Legendre-projection inequality. The primary rank certificate uses exact rational Gamma OU prefixes and π>3; the coarser Fourier-band certificate also uses the stated log2 inequality.
- **Finite Fourier sufficient route:** uniform midpoint quadrature error depends on true support `I`, Gamma derivative and original prime2 phase; false composite prime addition, wrong half-density, wrong Gaussian parity would invalidate those particular bounds. Synthetic Gram matrices never promote to source Weinstein/Weil positivity.
- **Other SUCC research:** sibling #155's exact piecewise derivative-Gram source integral directly improves the old Legendre-u zero-shift method. This branch is orthogonal: it attacks the *new* source-generated positive jump spectrum/compact polar channel. Its derivations do not overwrite or supersede #155.

### Reproduction

```
python -m unittest discover -s tests -p 'test_source_jump_spectral.py' -v
python scripts/source_jump_spectral_probe.py --verify
python scripts/source_jump_spectral_probe.py --source --verify
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

In the **isolated** standard-library fixture, 25 tests are discovered, 23 pass and 2 intentionally skip the absent original-SUCC imports. On **actual installed source** the dedicated CI MUST run all 25 with zero skips, replay the two authentic P1/P2 positive jump Ritz bounds, and verify their source blob. Our finite rational control is not a substitute for hosted source integration. Independent full repository validation is a separate (potentially long) workflow. Do not announce CI pass until exact-head status is inspected.

## 7. Next precise research targets (JS-07)

1. **Actual spectral projector construction:** Use source-certified resolvent or form-Galerkin bounds to produce intervals for \(P_{[0,7]}c\), \(P_{[0,7]}s\), the restricted low jump eigenvalues and scalar high resolvents \(\alpha_c,\alpha_s\). A source-certified eigenvalue exclusion/gap is needed before approximated projectors can be safely identified. The rank ≤453 alone does not provide these data.
2. **Efficient band-Gamma kernel evaluator:** Replace the `N~1.85×10^11` generic midpoint budget with rigorous piecewise analytic Fourier integrals, high-order Taylor/Chebyshev quadrature, validated prolate spheroidal compression, or finite interval Fredholm determinants. Certify the exact source positivity from matrix (19), if feasible; reject false lower signs as inconclusive.
3. **Parity and bounded polar rank:** On the actual jump spectrum, use the full odd/even scalar renormalizations (10) with strictly source-attested \(\alpha\) enclosures to test finite sign. If the even baseline has ≥2 negative modes or the odd baseline has ≥1, then an independently certified source-specific negative witness exists; otherwise determine whether the completed poles repair all low defects.
4. **Global radius:** Every fixed radius has a finite genuine prime-power tape and logarithmic Gamma growth, but source mass M_a and the low spectral rank bound generally grow with a. A uniform all-radius positivity theorem would require an additional arithmetic compensation mechanism; neither of these fixed-window constructions proves RH.

**Claim ledger:** `docs/CLAIM_SUPPLEMENT_SOURCE_JUMP_SPECTRAL.md`. **RH OPEN.**
