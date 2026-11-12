# Operation Prime Interferometer
**A finite, proof-carrying Goldbach/CRT/Haar research front for Observational SUCC**  
**Date:** 2026-11-12 · **Status:** local research note, **not committed to SUCC**.

## Executive verdict

- **PROVED LOCAL (elementary derivations):** the split-complex parity fiber-product presentation; the Goldbach Hilbert projector and exchange-parity identity; an exact Haar scale decomposition and its deterministic finest-scale echo; the Goldbach singular-series local factors; the CRT–Haar lower and upper witness certificates; monotonicity under observer refinement; and a semantic-path overcounting counterexample.
- **OBSERVED (finite experiment only):** 13 midpoint counts, exact rational Haar reconstruction, nine finite CRT–Haar certificates, a parity/CRT-matched zero-witness counterfeit, and a separate SymPy/NumPy check of counts, certificates, and Fourier reconstruction. These are **not** independent mathematical refereeing, Lean proof, or a universal result.
- **OPEN / UNVERIFIED:** any source-specific all-large-n estimate sufficient to make a CRT–Haar lower bound positive; binary Goldbach; any direct application of π-normality machinery to this prime-sum claim; a physical quantum interpretation.

Repository source contracts inspected (read-only): [SUCC AGENTS.md](https://github.com/femboy2112/SUCC/blob/main/AGENTS.md), [Main XXIV frontier](https://github.com/femboy2112/SUCC/blob/main/docs/PI_NORMALITY_FRONTIER.md), [typed Lambda–Haar compiler](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-10/zero_anchored_lambda_haar/README.md), [signed Haar construction](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-10/zero_anchored_lambda_haar/CONSTRUCTION.md), [intrinsic prime carrier](https://github.com/femboy2112/SUCC/blob/main/research/2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md), and open [PR #599](https://github.com/femboy2112/SUCC/pull/599). Repository code was not executed locally; our standalone code was.

## 1. Prime-midpoint split algebra

Work with the commutative integral ring

\[
A=\mathbb Z[j]/(j^2-1).
\]

The map

\[
\Phi:A\to\mathbb Z\times\mathbb Z,\quad n+jd\mapsto(n+d,n-d)
\]

is injective with image exactly the equal-parity pairs. Thus there is a ring isomorphism

\[
\boxed{A\cong \mathbb Z\times_{\mathbb F_2}\mathbb Z.}
\]

Proof: the image coordinates differ by `2d`, so have equal residue modulo 2; conversely for any same-parity pair `(p,q)`, the integers `n=(p+q)/2` and `d=(p-q)/2` recover a unique source element. Multiplication is preserved because `j^2=1`, giving coordinatewise multiplication under the two maps `χ±(n+jd)=n±d`. The ring norm is `N(n+jd)=n²−d²`.

Define the prime-pair locus `P_A={n+jd: n+d,n-d positive rational primes in Z}`. Then binary Goldbach is precisely surjectivity of the midpoint projection `m:P_A→{2,3,...}`, `m(n+jd)=n`. For `n>2`, the two primes are odd and `d` has parity opposite to `n`; for `n=2`, the sole pair is `(2,2)`.

The complex-cube presentation

\[
n=\sqrt[3]{((n+id)/2)^3}+\sqrt[3]{((n-id)/2)^3}
\]

holds using principal cube roots for `|d|≤n` (indeed `arg(n±id)` has magnitude ≤π/4, so its cube has principal argument within `(-π,π)`). It supplies no primality distinction by itself. Mapping `j→i` is **not** a ring homomorphism, because it would send `j²=1` to `i²=−1`; the complex and split-complex presentations must be related by an explicitly typed coordinate construction, not a fictitious ring isomorphism.

## 2. Arithmetic two-slit projector: exact but non-physical

For an integer `X≥4`, in the Hilbert space of integer labels define the **unnormalized** prime vector `|P_X⟩=Σ_{p≤X prime}|p⟩` and total-sum projection

\[
\Pi_{2n}=\sum_{a+b=2n}|a,b\rangle\langle a,b|.
\]

Then `|Γ_{2n}⟩=Π_{2n}(|P_{2n}⟩⊗|P_{2n}⟩)` has norm squared exactly

\[
R(2n)=\#\{(p,q):p,q\text{ prime},\ p+q=2n\}.
\]

If nonzero, its Schmidt coefficients are all equal and its entanglement entropy is `log R(2n)`; the state is entangled iff `R(2n)>1`. This is an exact *constructed mathematical model*, not a physical claim. Swapping the prime registers pairs every `p≠q` contribution and leaves only `(n,n)` fixed. Therefore

\[
\boxed{R(2n)\equiv\mathbf1_{\mathbb P}(n)\pmod 2.}
\]

The fixed-point contribution automatically settles prime midpoints; composite midpoints have only noncentral witnesses. An arbitrary coherent sum of syntax histories is **not** equal to this semantic projection: `4`, `(λx.x)4`, `(λx.x)((λx.x)4)`, etc., are infinitely many expressions for one number, and naive counting of beta-expansions changes the weight by arbitrary amounts. The certified rewriting groupoid must be quotiented or gauge-normalized *before* defining the source amplitudes. Beta transport is a **presentation equivalence**, not automatically a physical path alternative.

For `e(t)=exp(2π i t)`, exact character orthogonality also gives the classical circle representation

\[
R(2n)=\int_0^1\left(\sum_{p\le2n}e(p\alpha)\right)^2e(-2n\alpha)\,d\alpha.
\]

Fourier phases do interfere algebraically, but the output is still the same nonnegative integer count. Major/minor arc analysis supplies the deep missing bounds. No basis change alone proves it is positive.

## 3. Exact arithmetic Haar decomposition

Let `a(d)=1_P(n+d)`, `b(d)=1_P(n-d)` for `0≤d≤n-2`, with the indicator restricted to the common admissible parity for `n>2`. Pad to a dyadic length `L`. The unordered prime-pair count including the central pair is `G(n)=Σ_d a(d)b(d)`, and `R(2n)=2G(n)−1_P(n)`.

For every dyadic interval `I` of length at least 2, let `Δ_I a=Σ_{I_left}a−Σ_{I_right}a`; similarly for `b`. The discrete Haar basis gives the **exact rational identity**

\[
\boxed{G(n)=\frac{AB}{L}+\sum_{I\text{ dyadic},|I|\ge2}\frac{\Delta_Ia\,\Delta_Ib}{|I|},\quad A=\sum a,\ B=\sum b.}
\]

Proof: take the normalized constant vector `1/√L` and normalized Haar differences `(1_{I_left}−1_{I_right})/√|I|`; these form an orthonormal basis, so Parseval polarizes to the displayed inner-product formula. Each contribution can have either sign.

**Parity-echo theorem.** If both input vectors are supported on the same parity positions and `L` is even, then the sum over Haar intervals of length exactly 2 equals `G(n)/2`. In a length-2 cell the unique eligible parity coordinate contributes `a(d)b(d)/2`; sum over cells. This is a tautological echo of the desired witness count, **not** a positivity proof. Quotient the parity sublattice (retain only eligible d) before interpreting other Haar scales.

### Exact rational probe

| midpoint n | unordered witnesses G | lowpass AB/L | sum of all signed Haar details | parity-quotient lowpass | parity-quotient signed remainder |
|---:|---:|---:|---:|---:|---:|
| 100 | 8 | 3.750 | +4.250 | 7.500 | +0.500 |
| 256 | 11 | 8.902 | +2.098 | 17.805 | −6.805 |
| 1024 | 25 | 22.878 | +2.122 | 45.756 | −20.756 |
| 4096 | 76 | 63.640 | +12.360 | 127.280 | −51.280 |

Table decimals are **rounded displays** of exact `fractions.Fraction` computations; the full exact rational numbers are in `results.json`.

## 4. Recover the classical Goldbach singular series

For a rational prime `ℓ`, consider `F_n(d)=n²−d²` modulo `ℓ`. The forbidden residues `d≡±n (mod ℓ)` have cardinality `ρ_2(n)=1`, and for odd `ℓ`, `ρ_ℓ(n)=1` when `ℓ|n` and `2` otherwise. Every factor `1−ρ_ℓ(n)/ℓ` is positive. Therefore each fixed finite CRT sieve is locally admissible, including the parity place.

The normalized product is **exactly** the Hardy–Littlewood Goldbach singular series:

\[
\begin{aligned}
\mathfrak S(2n)&=\prod_{\ell}\frac{1-\rho_\ell(n)/\ell}{(1-1/\ell)^2}\\
&=2\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right)
  \prod_{\ell\mid n,\ell>2}\frac{\ell-1}{\ell-2}.
\end{aligned}
\]

Proof: at `ℓ=2`, the factor is 2. At odd `ℓ∤n` it is `ℓ(ℓ−2)/(ℓ−1)²=1−1/(ℓ−1)²`; if `ℓ|n` it is `ℓ/(ℓ−1)`, multiplying the generic factor by `(ℓ−1)/(ℓ−2)`. This well-known positive product is a **local-density prediction**, not the missing pointwise Goldbach asymptotic. Standard literature: Goldston et al., *Tail of the singular series for the prime pair and Goldbach problems*, arXiv:1409.2151; and Helfgott, *The ternary Goldbach problem*, arXiv:1501.05438 for circle-method context.

## 5. CRT–Haar observer certificates (main finite result)

Fix `n≥3`, `z≥2`, and the source-safe interior `0≤d<n−z`. Define

\[
D_{n,z}=\{d:0\le d<n-z,\quad \ell\nmid(n²-d²)\ \forall\text{ primes }\ell\le z\}.
\]

Both endpoints `n±d` exceed `z`, so the sieve does not discard a prime endpoint merely because it equals a small sieving prime. Let `𝒟` be any partition of `D_{n,z}` by disjoint dyadic cells. In each cell `I`, set

\[
K_I=|D_{n,z}\cap I|,\quad
A_I=\#\{d\in D_{n,z}\cap I:n+d\text{ prime}\},\quad
B_I=\#\{d\in D_{n,z}\cap I:n-d\text{ prime}\}.
\]

Let `G_{n,z}` count actual Goldbach pairs in this interior. Then

\[
\boxed{
L_{n,z}(\mathcal D)=\sum_{I\in\mathcal D}\max(0,A_I+B_I-K_I)
\le G_{n,z}\le
U_{n,z}(\mathcal D)=\sum_{I\in\mathcal D}\min(A_I,B_I).
}
\]

**Proof:** in each finite channel set `D_{n,z}∩I`, its two prime subsets satisfy `max(0,|A|+|B|−|D|)≤|A∩B|≤min(|A|,|B|)`. Sum over disjoint cells. Under refinement a parent cell is replaced by subcells; convexity of the positive-part function and subadditivity of `min` show `L` nondecreasing and `U` nonincreasing. Singleton refinement gives `L=U=G_{n,z}`. Since `G(n)≥G_{n,z}`, **any** `L>0` proves a genuine Goldbach witness.

This is a certified **finite observer hierarchy** with an actual nontrivial lower bound, a no-false-witness contract, explicit source identity, and a controlled resolution cost. Note that calculating actual prime marginals via individual primality tests may cost at least as much as direct witness search. Its potential analytic value is when the marginal counts can be bounded **independently**, e.g. via arithmetic progression/sieve estimates; that global uniform bound has not been obtained.

### Certified hierarchy at n=1024, z=3 (25 interior witnesses)

| Dyadic width | certified lower `L` | certified upper `U` |
|---:|---:|---:|
| 1024 | 0 | 69 |
| 256 | 0 | 67 |
| 128 | 2 | 66 |
| 64 | 6 | 64 |
| 32 | 9 | 60 |
| 16 | 13 | 50 |
| 8 | 21 | 32 |
| 4 | 25 | 25 |

Changing the prime-local cutoff changes the trade-off: at width 128, `z=3` proves at least 2, `z=5` proves at least 11, and `z=7` proves at least 21. Both precision axes consume resources.

### Hostile same-marginal source

At `n=1024`, `z=2`, width 128, the actual prime masks have 137 positive-side and 171 negative-side marked positions, and 25 common witnesses. In **each** 128-cell, the combined marked count is at most the number of CRT-admissible positions. Hence construct disjoint fake positive/negative masks **within the same admissible positions**, preserving every one of the actual cellwise marginal counts. The fake source has **zero** midpoint witnesses. It obeys the prescribed parity/CRT constraints and demonstrates that those finite observations do not determine the joint coupling. For `z=3`, width 64, this fake construction is blocked by the independent pigeonhole lower bound 6.

An even simpler hostile pair on length 32 is `a=1_{d≡1 mod4}`, `b=1_{d≡3 mod4}`. Every aligned dyadic cell of length ≥4 has equal counts for a,b, but `a·b=0`. The positive control `b=a` has 8 overlaps with the same coarse marginals. The first discriminating Haar details retain the missing information.

## 6. Two-slit scope / categorical source contracts

The arithmetic sum-conditioned vector `|Γ⟩` is analogous to retaining which-path labels, while applying a sum map that discards the pair label is analogous to coherently combining amplitudes. Such a sum map is generally **not an isometry**. It may change an unnormalized intensity from `R` to `R²` by coherent addition, but it cannot produce a nonzero amplitude if `R=0` with all source amplitudes supported only on genuine prime pairs. Arbitrary sign phases can instead destroy a nonzero amplitude by cancellation. Physical interference is not established by this analogy.

Use semantic **witnesses** `(p,q)` as independent basis states; treat beta reductions and algebraic identities within a witness's presentation fiber as typed gauge transformations. If raw computation paths receive arbitrary amplitude one, syntactic beta-expansions give unbounded duplications and any claimed path-count amplification is meaningless. The exact source, valid domain, normalization, and observable must be declared.

The spatial Haar basis on displacement indices and profinite/CRT Haar measure are distinct notions; both occur here, but must not be conflated. SUCC's existing zero-seed/semantic-source and signed Fourier obstructions apply in spirit, **not** as imported Goldbach theorems.

## 7. Next falsifiable research program

**Gate A — certify the finite bridge.** Add an explicit `GoldbachWitness` source type, with `PrimeCertificate(p)`, `PrimeCertificate(q)`, `p+q=2n`, source-bound rewriting judgments, and no syntax-path multiplicities. Implement both the split-algebra and integer representations and verify maps commute; include branch/complex cube checks.

**Gate B — optimize observer cost.** For large finite midpoint epochs, scan `(z,dyadic width)` and record the first strictly positive `L`, total sieve work, marginal primality tests, and the competing direct-witness discovery cost. Pre-register samples and hostile sources; preserve unfavored results. The posted finite results are calibration, not validation of global behavior.

**Gate C — the theorem-changing arithmetic inequality.** Seek independently established estimates, uniform for every sufficiently large `n`, giving a dyadic cell `I` (with `z(n)` and width chosen *before* inspecting actual witnesses) such that

\[
\boxed{A_I(n,z)+B_I(n,z)>K_I(n,z).}
\]

If proven for all `n≥n0`, with finite primality certificates below `n0`, Goldbach follows. It is essential to avoid choosing singleton cells or estimates that already incorporate joint prime-pair counting; otherwise the criterion is just Goldbach in disguise. No claim is made that this route bypasses the parity barrier.

**Gate D — Fourier–Haar comparison.** Compare CRT occupancy and signed Haar residual with the exact circle-method coefficient under **unchanged prime source**. Ask which frequency/scale constraints could bound the hostile joint dependence that marginal observers cannot see. Prove an actual numerical inequality with calibrated controls; don't substitute a Hilbert Gram positivity theorem for the missing signed correlation.

**Gate E — provenance and source mutation.** Show the strategy fails (or detects the defect) when the source is replaced with matched coarse masks, odd-only/composite masks, residue-preserving fake sources, prime-power-inclusive Mangoldt masks, and syntax-only beta clones. Account for small-prime endpoint exceptions, zero displacement, all parity and width boundaries.

Potential interfaces in SUCC: `zero_anchored_lambda_haar` for typed reductions and finite observation; `basis_boundary_transport` for source-preserving change of basis; `prime_clock_yoneda` for local residue maps; `intrinsic_carrier` for Hilbert operators and no-go composite controls; and `docs/METHOD.md` for the steelman–crucible–verdict ledger. Don't modify the frozen BBP π source: this is an **additive** Goldbach laboratory.

## 8. Reproduction / provenance

Execute from a Python 3.10+ environment:

```bash
python prime_interferometer.py
```

This writes `results.json` using only standard-library exact integer and `Fraction` arithmetic. The asserted tests include exact Haar Parseval, prime-exchange parity, local CRT residue counts, monotone lower/upper intervals, and matched marginal zero-overlap construction.

For a second library route, install SymPy and NumPy and run:

```bash
python independent_audit.py
```

This separately recomputes all 13 ordered prime-pair counts with SymPy's `isprime`, nine CRT–Haar lower/upper certificates by independent loops, and NumPy FFT reconstruction of `R(2n)` for n=10,100,256. It is not a separate blinded human review or new proof authority. Recorded result: **PASS** for the stated finite cases.

Relevant primary/reference literature: [Oliveira e Silva–Herzog–Pardi, *Empirical verification of the even Goldbach conjecture* (2014)](https://www.ams.org/mcom/2014-83-288/S0025-5718-2013-02787-1/S0025-5718-2013-02787-1.pdf); [Tao, *A general parity problem obstruction* (2014)](https://terrytao.wordpress.com/2014/11/21/a-general-parity-problem-obstruction/); [Goldston–Hunts–NgotiaoCo, singular-series tail paper](https://arxiv.org/abs/1409.2151); [Helfgott, *The ternary Goldbach problem*](https://arxiv.org/abs/1501.05438).

**Bottom line:** the proposed path-superposition ontology yields exact representation and observer machinery. The finite CRT–Haar certificates are real but elementary; their substantive future value depends on independent, uniform prime distribution estimates not yet established. Binary Goldbach remains open.
