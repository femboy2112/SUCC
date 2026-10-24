# Operation Pascal Forge — source-faithful π carry interferometry

**2026-10-24.** SUCC research draft stacked on [PR #269](https://github.com/femboy2112/SUCC/pull/269) at \`b445b0d9c604f45548a45b5db4f31428f73b35a2\` (which inherits [PR #268](https://github.com/femboy2112/SUCC/pull/268)). Live coherent main at first audit \`e648df3e4fca73ab6b942232b5ca4b310e9cac08\`. Unmerged [PR #266](https://github.com/femboy2112/SUCC/pull/266) inspected for the authentic centered-vs-literal carry issue. All original archives and main unchanged.

**Authority:** classical Lucas/Kummer/binomial/Pascal identities; proved exact paper algebra; verified integer/Fraction source and adversarial tests; one explicitly noncertifying complex numerical cross-check. No new Lean kernel theorem. No academic priority claim. **π NORMAL IN BASE 2/16: OPEN. π NORMAL IN BASE 3: OPEN. THE SELECTED O(D) SIGNED CARRY ESTIMATE: UNVERIFIED.**

## 1. Strongest faithful Pascal interpretation: three different structures

The row-\(n\) Pascal coefficients do not each equal powers of two; their **sum** equals \(2^n\). The row-4 coefficients \((1,4,6,4,1)\) sum to \(16=2^4=4^2\). Modulo two the coefficient pattern is Sierpiński self-similar. Lucas's theorem gives, for any genuine prime \(p\),

$$
\binom nk\equiv\prod_{i\ge0}\binom{n_i}{k_i}\pmod p,
$$

with base-\(p\) digits \(n_i,k_i\). Hence the number of nonzero coefficients in row \(n\) modulo \(p\) is \(\prod_i(n_i+1)\); at \(p=2\) it is \(2^{s_2(n)}\). Kummer's theorem identifies the \(p\)-valuation of \(\binom nk\) with the number of base-\(p\) carries when \(k+(n-k)=n\). These classical theorems are not novel SUCC discoveries. Their *source-scoped application to the signed BBP pair carry* is the subject below.

Three domains must be typed distinctly: base-\(b\) digit cylinders on the real circle; prime-adic integer and binomial residue filtrations; and \(p\)-primary rational torsion clocks in the BBP source. As #269 proved, the authentic rational source has odd denominators; its 2-primary torsion projection is zero, even though the **integer centered pair carry** has nontrivial four-bit data. Do NOT replace one by another.

## 2. PASC-01: Pascal row 4 is the complete Walsh interaction decomposition (PROVED)

Keep the actual signed source, no initial state substitution:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
y_0=0,\quad y_n=\{16y_{n-1}+r(n)\}.
$$

Use the inherited selected window \(p=8m+1\), \(W=\{m+1,\ldots,4m-1\}\), length \(D=3m-1\), and successor-close-pair set

$$
E_\tau=\{(s,t)\in W^2:|\delta^+_{s,t}|\le\tau\}.
$$

With \(\mathrm{cen}\) reducing to \([-1/2,1/2)\), set

$$
\delta_{s,t}=\mathrm{cen}(y_t-y_s),\quad
\delta^+_{s,t}=\mathrm{cen}(y_{t+1}-y_{s+1}),\quad
\eta_{s,t}=r(t+1)-r(s+1),
$$

$$
\kappa_{s,t}=16\delta_{s,t}+\eta_{s,t}-\delta^+_{s,t}\in\mathbb Z.
$$

At \(\epsilon_p<\tau\le1/4\), \(\epsilon_p=r(m+2)-r(4m)<15/((p+8)(p+9))\), the inherited TWA-15 **zero centered inverse branch** is \(\kappa\equiv0\pmod{16}\). The source's literal carries can differ even when this centered carry is zero.

Let \(b_j(\kappa)\) be bit \(j\) of \(\kappa\bmod16\), let \(\sigma_j(\kappa)=(-1)^{b_j(\kappa)}\), for \(j=0,1,2,3\), and for each subset \(A\subseteq\{0,1,2,3\}\) define the **signed source-selected Walsh moment**

$$
M_A(p,\tau)=\sum_{(s,t)\in E_\tau}\prod_{j\in A}\sigma_j(\kappa_{s,t}),\qquad
M_\varnothing=Q_0:=|E_\tau|.
$$

(The Walsh functions are characters of the *bitwise XOR* group \(\mathbf F_2^4\), not additive characters of cyclic \(\mathbb Z/16\mathbb Z\): carries prevent that false identification.)

The elementary zero-bit identity gives

$$
\boxed{16Z_W(\tau)=
\sum_{A\subseteq\{0,1,2,3\}}M_A
=Q_0+\sum_{A\ne\varnothing}M_A.}
$$

Define \(G_r=\sum_{|A|=r}M_A\) for \(r=0,\ldots,4\). Pascal row 4 counts the number of masks in these classes: \((1,4,6,4,1)\). Therefore

$$
\boxed{16Z_W=G_0+G_1+G_2+G_3+G_4,\qquad
G_0=Q_0.}
$$

This is an exact full factorial contrast, not an independence approximation. The discrete Walsh inversion recovers each of the 16 carry residue occupancies:

$$
\#\{\kappa\equiv k\bmod16\}=
\frac1{16}\sum_A (-1)^{\sum_{j\in A}b_j(k)}M_A.
$$

The implementation checks the inverse for all 16 masks on exact authentic histograms and adversarial synthetic ones.

## 3. PASC-02: primitive cyclotomic shells equal Pascal's highest-bit slices (PROVED)

Let \(Q_j=\#\{(s,t)\in E_\tau:2^j\mid\kappa_{s,t}\}\), for \(0\le j\le4\), and let \(S_j=\sum_{E_\tau}c_{2^j}(\kappa)\) be the primitive Ramanujan shell from PR #269. For each *integer* \(\kappa\),

$$
c_{2^j}(\kappa)=2^{j-1}\,\mathbf1_{2^{j-1}\mid\kappa}\,
(-1)^{b_{j-1}(\kappa)}.
$$

Hence

$$
\boxed{S_j=2^{j-1}(2Q_j-Q_{j-1})
=\sum_{\substack{A\ne\varnothing\\ \max A=j-1}}M_A.}
$$

Proof of the second equality: \(\mathbf1_{2^{j-1}\mid\kappa}
=2^{-(j-1)}\prod_{i<j-1}(1+\sigma_i)\); distribute the product. The highest-bit slices partition exactly the 15 nonempty Walsh masks. Thus

$$
\boxed{16Q_4-Q_0
=\sum_{j=1}^4S_j
=\sum_{r=1}^4G_r.}
$$

This precisely converts the real-world "four half gates" to a signed full interaction budget. The missing source estimate is *not* that all bit marginals approach 1/2, but the signed sum \(\sum_{A\ne\varnothing}M_A=O(D)\) uniformly across the prescribed scales. Four conditional half-gate bounds would suffice but are stronger in a different direction.

## 4. PASC-03: an exact fourth-order countermodel (REFUTATION of three-wise closure)

Let \(\kappa\) range uniformly over the eight residues whose four binary digits have **even parity**. Give each such residue two counts (total 16). Then every nonempty Walsh moment of degree at most three is zero; the sole fourth-degree moment is \(M_{\{0,1,2,3\}}=16\). Therefore

$$
\Pr(\kappa=0)=\frac18\ne\frac1{16}.
$$

Every one-, two- and three-bit marginal is perfectly uniform. This refutes any inference from *all lower-order tests* to 1/16. It does not purport to preserve selected BBP forcing or initial zero: it is an information-identifiability countermodel. Mutation of a single cell exposes its missing fourth contrast.

An independent pure-\(16\) zero-point-mass law is invariant under all odd multiplier units, so primes \(3,5,7,11,13\) acting only as units cannot create uniformity either. "Only base 3 is required" is therefore **not justified** by prime-unit or marginal symmetry.

## 5. PASC-04: Pascal differences of authentic BBP forcing are strictly signed Hausdorff moments (PROVED)

Write \(P(t)=4+4t+4t^2+2t^3+t^4\). Exact expansion of the original signed source gives

$$
r(n)=\int_0^1 t^{8n-8}(1-t)P(t)\,dt>0.
$$

For \(\Delta f(n)=f(n+1)-f(n)\), use Pascal's binomial coefficients to obtain

$$
\boxed{(-1)^k\Delta^k r(n)
=\int_0^1 t^{8n-8}(1-t)P(t)(1-t^8)^k\,dt>0.}
$$

Because \(P(t)\le15\) and \(1-t^8\le8(1-t)\) on \([0,1]\),

$$
\boxed{0<(-1)^k\Delta^k r(n)
<15\,8^k\,B(8n-7,k+2)
=\frac{15\,8^k(8n-8)!(k+1)!}{(8n+k-6)!}.}
$$

An additional bound \(|\Delta^k r(n)|\le r(n)\) follows directly from \(0\le(1-t^8)^k\le1\). This is the true reason the higher Pascal difference has alternating sign: it is a positive Hausdorff-moment source, not a guessed positivity of a circle correlation or Weil form.

For \(n\asymp p\) and \(k=c\log p\), the beta bound is superpolynomially small (its log is \(-c(\log p)^2+O(\log p\log\log p)\)). This is a genuine source-specific estimate on the **forcing derivative**, not on the normality-relevant orbit distribution.

## 6. PASC-05: exact Pascal source-jet/shadow identity, with explicit ceiling (PROVED)

Since \(\Delta y_n=15y_n+r(n+1)\pmod1\), Pascal induction yields for every \(k\ge1\),

$$
\boxed{
\Delta^ky_n=15^ky_n+
\sum_{j=0}^{k-1}15^{k-1-j}\Delta^j r(n+1)
\pmod1.
}
$$

Let the displayed sum be \(C_{n,k}\). Using PASC-04,

$$
\boxed{
|C_{n,k}|\le\frac{15^k-1}{14}\,r(n+1).
}
$$

In a first-birth \(p=8m+1\) window, \(n\ge m+1\), so

$$
r(n+1)<\frac{15}{(p+8)(p+9)}.
$$

If \(k\le\lfloor(2/5)\log_{16}p\rfloor\), the bound becomes

$$
\boxed{
|C_{n,k}|=O\left(p^{-2+(2/5)\log_{16}15}\right)
=O(p^{-1.609\ldots}).
}
$$

Thus a \(\log p\)-order Pascal jet of the authentic source differs from the unforced \(15^k\)-gain signal by a quantitatively tiny, fully specified source term. Exact Fraction tests verify both sides modulo one for the *actual* \(y_0=0\).

**Ceiling:** this identity holds for every initial state under the same forcing. A different selector can satisfy every Pascal derivative identity. It is **not** a proof of selected orbit equidistribution. The factor \(15^k\) may annihilate low \(3\)- or \(5\)-primary clocks, but does **not** damp dyadic information.

## 7. PASC-06: base 3 and 5 are exact Pascal resonances, but are not magic cancellation (PROVED)

For a homogeneous prime clock \(u_t=4\cdot16^t/p\pmod1\),

$$
\boxed{\Delta^k u_t=\frac{4\cdot15^k16^t}{p}\pmod1.}
$$

For every \(k\ge1\), the factor \(15^k\) kills \(p=3,5\) clocks exactly. For every prime \(p\notin\{3,5\}\), multiplication by \(15^k\) is invertible mod \(p\): there is no reduction of \(p\)-primary information. The good BBP window primes \(p\equiv1\bmod8\) are at least 17 and are in the latter class.

This explains why looking specifically at base 3 **and base 5** is mathematically natural: they divide \(16-1\), so first Pascal differences separate their source clocks. It also reveals the limitation. The relevant \(16\)-way centered integer carry and its four dyadic conditional gates do not vanish with those clocks. The actual complementary BBP source and its selected joint correlations remain to be estimated.

The exact same-forcing shift \(y'_0=y_0+1/3\) yields \(y'_n=y_n+1/3\) for all \(n\) because \(16\equiv1\bmod3\), and all positive Pascal differences agree modulo one. This is a calibrated observation-gauge example, not a nonnormal \(\pi\) counterfeit or a refutation of a selected proof.

## 8. PASC-07: exact transport of all 15 primitive dyadic modes into ordinary circle modes (PROVED)

Use \(H=\{-7,-6,\ldots,-1,1,\ldots,8\}\), one representative of each nonzero residue mod 16. The cyclic orthogonality identity, without any Fourier approximation, is

$$
\boxed{
16Z_W(\tau)-Q_0
=\sum_{h\in H}\sum_{(s,t)\in E_\tau}
e(h(y_t-y_s))\,
e\left(\frac h{16}(\eta_{s,t}-\delta^+_{s,t})\right).
}
$$

This follows exactly from \(\kappa=16\delta+\eta-\delta^+\) and \(e(h\delta)=e(h(y_t-y_s))\). The fifteen \(h\)'s correspond to primitive shells of orders \(2,4,8,16\); the source phase correction is kept, not dropped.

Define the actual selected weighted **jet**, for any integer \(R\ge0\),

$$
\mathcal J_R(p,\tau):=
\sum_{h\in H}\sum_{(s,t)\in E_\tau}e(h(y_t-y_s))
\sum_{\ell=0}^{R}\frac{1}{\ell!}
\left(\frac{2\pi i h}{16}(\eta_{s,t}-\delta^+_{s,t})\right)^\ell.
$$

All source selector, real time indices, centered carries, and both endpoint conditions remain. This is a **finite, explicit 15-mode ordinary-circle Fourier instrument**.

## 9. PASC-08: a proved, sufficiently small analytic transport error (PROVED; cancellation still OPEN)

For real \(z\), the Taylor-integral remainder obeys

$$
\left|e^{iz}-\sum_{\ell=0}^{R}\frac{(iz)^\ell}{\ell!}\right|
\le\frac{|z|^{R+1}}{(R+1)!}.
$$

Because \(|h|\le8\), \(|\eta|\le\epsilon_p\), and \(|\delta^+|\le\tau\), with \(\pi<22/7\), this yields the **exact rational upper bound**

$$
\boxed{
\left|16Z_W(\tau)-Q_0-\mathcal J_R(p,\tau)\right|
\le \frac{15Q_0}{(R+1)!}
\left(\frac{22}{7}(\tau+\epsilon_p)\right)^{R+1}
\le\frac{15D^2}{(R+1)!}
\left(\frac{22}{7}(\tau+\epsilon_p)\right)^{R+1}.
}
$$

This does **not** assume random phases, mixing, entropy, Galois averaging, or signed positivity.

On PR #268's terminal refinement radius \(\tau_J=4/M-\epsilon_p(1-16/M)/15\), with \(M\asymp p^{2/5}\), \(D\asymp p\), and \(\epsilon_p=O(p^{-2})\), **fixed Taylor degree \(R=2\) suffices**:

$$
\boxed{
|16Z-Q_0-\mathcal J_2|=O(D^2p^{-6/5})
=O(p^{4/5})=o(D).
}
$$

Thus at the crucial final refinement scale, replacing the exact arithmetic carry characters by a **quadratic** source-corrected circle Fourier jet incurs an absolute error negligible compared with the allowed \(O(D)\) budget. This is a genuine verified *pathway repair*, not a cancellation estimate.

Across **all** prescribed refinement scales (including coarse \(\tau_0=1/4\)), let \(R(p)=\lceil\log p\rceil\). For large p, \(\tau+\epsilon_p<1/2\); the factorial bound proves a uniform total remainder \(o(1)\), superpolynomial in \(p\). The price is jet degree \(O(\log p)\), not an \(O(1)\)-complexity symbol.

**Remaining proof contract, stated without laundering:** prove \(\mathcal J_{R(p)}(p,\tau_j)\le C D\) (real signed quantity) across ALL prescribed scales, uniformly for actual \(y_0=0\) and all sufficiently large good primes. This plus the proved \(o(1)\) transport completes the inherited \(1/16\) branch-loss hypothesis; the jet bound itself is **UNVERIFIED**. At the terminal scale it is enough to prove \(\mathcal J_2=O(D)\), but terminal control alone does not imply normality because preceding scale losses are unbounded.

## 10. Exact finite BBP tomography: Pascal interaction by order (VERIFIED FINITE)

The following rows are real zero-initial rational BBP selected-source states, and all counts include ordered diagonals. They are adaptive test radii, **not** an asymptotic theorem or a prescribed-scale proof.

| p | successor radius | \(D\) | \(Q_0\) | \(Z=Q_4\) | \(G_1\) | \(G_2\) | \(G_3\) | \(G_4\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 41 | 1/16 | 14 | 40 | 20 | 86 | 114 | 66 | 14 |
| 97 | 1/16 | 35 | 229 | 45 | 98 | 224 | 126 | 43 |
| 257 | 1/16 | 95 | 1181 | 161 | 360 | 554 | 384 | 97 |

Each row passes \(16Z=Q_0+G_1+G_2+G_3+G_4\) exactly. At \(p=97,\tau=1/16\), the *first primitive Ramanujan shell* is \(-7\), detecting any false nonnegative-shell assumption. The fourth-order interaction is not zero on these samples; but neither is its asymptotic size resolved.

The independent factorial-vs-carry and Lucas-vs-direct-combination oracles ran **12,870 Lucas comparisons and 12,870 Kummer comparisons**. The parent nine dyadic test methods and new twelve Pascal test methods passed locally. The complex-valued jet regression is expressly **non-certified numerical cross-check**; the analytic error theorem is proved with rational \(22/7\), not by trusting its floating comparison.

## 11. Explicit alternative controls and falsification directions

1. **Even-parity 3-wise fooler**: defeats marginal/pair/triple inference, fourth-order survives. Complete 16-cell contrast needed.
2. **Point mass at zero**: odd-prime multiplier symmetry does not imply uniform 1/16.
3. **Same-forcing initial 1/3, 1/5, 1/15 offsets**: Pascal differences can be blind to origin gauge; a derivative identity cannot establish π selection.
4. **Good p ≥17 prime clock**: Pascal gain is invertible, so no automatic p-primary damping.
5. **Pure high-derivative smallness**: forcing derivatives vanish superpolynomially at growing order, but homogeneous selected orbit remains; no statistical conclusion.
6. **Truncation error versus jet magnitude**: analytic \(o(D)\) bound does not control the actual signed jet, which could be large.
7. **One terminal scale**: even a proved \(O(D)\) signed jet at the terminal radius cannot substitute for ALL intermediate TWA-15 refinements.
8. **Boundary/centered carry mutation**: replacing κ by a literal source carry, dropping \(\eta\), or replacing selected with Galois mean changes the theorem; refute by existing #266/#269 tests.

## 12. Claim ledger and next verdict-changing probe

| Claim | Exact status |
|---|---|
| PASC-01: 4-bit Walsh/Pascal 16-cell inversion | DISCLOSED (elementary exact) |
| PASC-02: 4 primitive Ramanujan shells = 15 Walsh contrasts, highest-bit grouping | DISCLOSED (elementary exact) |
| PASC-03: 3-wise parity indistinguishability | REFUTED lower-order sufficiency / DISCLOSED exact countermodel |
| PASC-04: signed finite differences of authentic four-pole forcing | DISCLOSED (elementary integral proof) |
| PASC-05: source Pascal jet with \(O(p^{-1.609\ldots})\) correction at prescribed order | DISCLOSED source-specific, but generic in initial state |
| PASC-06: precise p=3,5 clock-annihilation, others invertible | DISCLOSED prime-clock theorem / no normality consequence |
| PASC-07: exact 15-harmonic source transport | DISCLOSED finite identity |
| PASC-08: quadratic terminal \(o(D)\) and growing-degree all-scale \(o(1)\) error | DISCLOSED analytic inequalities; **source signed jet bound UNVERIFIED** |
| PASC-09: nine selected-source finite Walsh tables and exact oracles | VERIFIED FINITE; no extrapolation |
| π base 16/2, π base 3 normality; π-specific undecidability | OPEN, not proved or refuted |

**Next arithmetic moonshot:** attack \(\mathcal J_R(p,\tau)\) as a truly **signed bilinear incidence sum** on actual source states. Use the Pascal complete contrast to separate orders 1–4 rather than silently discarding the fourth. Seek source-derived van der Corput / Dirichlet-to-Neumann or transfer-operator estimates for the fifteen *fixed circle frequencies* \(h\in H\), weighted by the authentic near-return cutoff and at most quadratic \(z\)-polynomial at fine scales. Target one **nontrivial scale proportion** first (a polynomial collision saving via TWA-15), then sufficient cumulative loss to match \(1/M\). Demand independent holdout primes and the #266 changed-selector/no-go controls. Provenance-matched repeated tests are not independent mathematical refereeing.

## 13. Reproduction and provenance

Modules/probes in this branch:
- \`observational_succ/pascal_carry_interferometry.py\`;
- \`tests/test_pascal_carry_interferometry.py\`;
- \`scripts/pascal_carry_interferometry_probe.py\`;
- exact selected Walsh receipt in \`research/2026-10-24/\`.

Required focused commands:

\`\`\`sh
python -m unittest discover -s tests -p 'test_pascal_carry_interferometry.py' -v
python -m unittest discover -s tests -p 'test_pi_dyadic_prime_transfer.py' -v
python scripts/pascal_carry_interferometry_probe.py --output /tmp/pascal-jet.json
\`\`\`

Full hosted CI is a separately checked authority, not inferred from local 21 focused methods. No Lean authority is asserted.

**Primary/classical sources:** Bailey–Borwein–Plouffe, *On the Rapid Computation of Various Polylogarithmic Constants*, Math. Comp. 66 (1997), https://www.davidhbailey.com/dhbpapers/digits.pdf; Lucas theorem and binomial digit factorization, https://math.hmc.edu/funfacts/lucas-theorem/; Kummer carry interpretation and Lucas proofs, https://www.math.tsukuba.ac.jp/~ksakai/aPathToCombinatorics.pdf. SUCC exact-source parent #269 and signed-carry source #268 provide the named notation. Independent academic novelty has not been reviewed or established.
