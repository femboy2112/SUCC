# Zero-Anchored Lambda–Haar Compiler (ZALHC)

**Research date:** 2026-11-10. **Truth status:** exact finite algebra and certified finite observations; original-zero π base-16 normality **OPEN**. The specifically requested asymptotic Haar contraction is **UNVERIFIED**. No theorem is fabricated from finite tests.

**Parent:** [PR #579](https://github.com/femboy2112/SUCC/pull/579), branch `research/cayley-source-observer-soundness-2026-11-09` (head `3f1b67d6c319bf4ee9f42941da829cd1f778a3af` at branch creation), which repairs [#576](https://github.com/femboy2112/SUCC/pull/576)'s lambda semantics. This PR is an additive *child*, not a main-branch rewrite or integration authorization.

## 1. Exact source and two zero tests

The frozen source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=s,\quad U_{n+1}=16U_n+r(n+1).
\]

Define \(P_n=\sum_{j=1}^n16^{-j}r(j)\) and
\(\mathcal Z(n,u)=16^{-n}u-P_n\). Then

\[
\boxed{U_n(s)=16^n(s+P_n),\quad \mathcal Z(n,U_n(s))=s,\quad
\mathcal Z(S(n,u))=\mathcal Z(n,u).}\tag{Z1}
\]

**Proof:** induction using \(P_{n+1}-P_n=r(n+1)/16^{n+1}\). No infinite limit, float, β-syntax trick, or π oracle is involved. A mutated source value at clock \(j\) with error \(\delta\) generates the immediately visible residual \(\delta/16^j\) at that clock.

A distinct valid route is the direct `from_prefix(n,seed)` formula. Both routes are implemented in `observational_succ/zero_anchored_lambda_haar.py` and cross-checked exactly. The completed analytic route is separately checked in §3. `recover` uses the *unwrapped* rational lift: reducing modulo 1 first destroys the seed witness.

### The exact source-equivalence / circle-alias distinction

For two seeds \(s,t\), their completed real circle orbits agree for **all clocks \(n\ge m\)** iff

\[
\boxed{16^m(s-t)\in\mathbb Z.}\tag{Z2}
\]

Proof: their lifted difference is \(16^n(s-t)\); equality modulo 1 at \(m\) is precisely integrality there and is preserved by multiplying by 16. Thus seeds 0 and 1/16 are different source identities but have identical completed circle observations after n=1. They cannot be separated by any later *circle-only* diagnostic. An authentic source checker must carry provenance/clock/lift, not pretend that every wrong seed is statistically wrong.

## 2. Real simply typed lambda evaluator, bounded operational meaning

The module implements a small simply typed calculus of de Bruijn `Var`, `Lam`, `App`, exact `Lit`, and total source primitives `step`, `recover`, `prefix`, `from_prefix`, `tail`, `complete`. Each primitive has an explicit type. β reduction uses shift/substitute/unshift, with a global budget, type-preservation check at each reduction, and a receipt identifying β and primitive steps. Two explicit evaluation strategies (normal/leftmost and eager/innermost) are compared on the same source, anchor and guarded-completion terms, including distinct β-contraction schedules. Budget exhaustion means *UNKNOWN*. This is a concrete terminating calculus for closed well-typed finite programs, **not** a complete realization of a C-monoid nor a claim about the untyped Ω normal form.

The program `serial_program(n,s)` has \(n\) actual β-redexes and \(n\) exact source-step primitive contractions. `prefix_program(n,s)` is an independent rational computation. Applying the lambda abstraction `recover` to either yields the exact literal \(s\): for the authentic source, 0. Capture-sensitive nested-binder and wrong-seed tests prevent replacing proof of faithful β with a string-rewrite demonstration.

**Proof domain:** by the standard substitution lemma for simply typed lambda terms, β preserves types. Our primitives are total on their declared domains and return those declared types. Subject reduction follows by induction on the evaluation context; this paper argument is not a Lean kernel theorem. The separate corrected #579 reducer remains a reference control; all hosted integration gates must be rerun on the actual PR head.

## 3. Guarded tail fixed point and finite refinement

The genuine completed future tail is

\[
T_n=\sum_{j\ge1}16^{-j}r(n+j),\qquad
T_n=\frac{r(n+1)+T_{n+1}}{16}.
\]

The operator \(F(t)_n=(r(n+1)+t_{n+1})/16\) is a \(1/16\)-contraction on bounded sequences. Therefore there is a unique **bounded** tail fixed point. This does not eliminate the independent homogeneous *forward* mode \(16^ns\) nor say anything about digit statistics.

From the independently verified canonical `duck_bbp.source_tail_budget(n)=r(n+1)/15`, start at horizon \(n+d\) with the interval \([0,r(n+d+1)/15]\), then apply the affine interval map \(X\mapsto(r(k+1)+X)/16\) backwards to clock \(n\). The resulting interval \(I_{n,d}\) contains \(T_n\), satisfies the **exact finite one-step square**

\[
\boxed{I_{n,d+1}=\bigl(r(n+1)+I_{n+1,d}\bigr)/16,}\tag{Z3}
\]

and has width \(r(n+d+1)/(15\cdot16^d)\). Direct canonical `duck_bbp.tail_interval` computations agree *exactly* with this independently ordered guarded fold. A state interval is `complete(s,d) = s.u + I_(s.n,d)`. Under any valid step,

\[
16\operatorname{complete}(s,d+1)=
\operatorname{complete}(S(s),d).
\]

The code uses finite, rational, **adaptive precision** to certify that a completed interval is contained in one hexadecimal cylinder before returning its digit. A precision budget that cannot resolve the boundary raises an exception; it cannot silently treat a midpoint as a certified digit.

## 4. Certified empirical Haar defect and exact Pascal–Fourier pins

Let \(z_n=\{U_n(0)+T_n\}\), \(\mu_N=N^{-1}\sum_{n<N}\delta_{z_n}\), and \(Q\mu=(1/16)\sum_{a=0}^{15}(B_a)_*(T_*\mu)\) with \(B_a(y)=(a+y)/16\), \(T(x)=\{16x\}\). Define the interval-Wasserstein defect

\[
D_N=W_1(\mu_N,Q\mu_N).
\]

A certified finite interval for each completed phase, inside one fixed hex cylinder, produces rational midpoint \(x_n\) and lifted interval width \(w_n\). The exact 1D atomic-Wasserstein algorithm computes \(\widetilde D_N=D(\widetilde\mu_N)\) by integrating the absolute cumulative signed masses. The chosen first-digit cylinder guarantees \(Q\) is nonexpanding for the *paired source/midpoint phases*, because \(T\) multiplies their distance by 16 while each inverse branch divides by 16. Therefore

\[
\boxed{|D_N-\widetilde D_N|\le\frac1N\sum_{n<N}w_n.}\tag{Z4}
\]

This is an unconditional **rigorous rational finite-sample certificate**, not a numerical π oracle. The source is the BBP formula plus its established analytic tail bound.

The `formal_character_pin` uses the exact cyclotomic basis \(\mathbb Q[\zeta_{16}]\) with \(\zeta_{16}^8=-1\). No floating DFT is trusted. `cyclic_defect` calculates the future-conditioned digit L1 defect and validates the inherited energy bound \(\delta_j^2\le E_{j+1}-E_j\) for its explicitly *cyclic* finite sample convention.

The Pascal pin for \(m\ge0\), \(0\le j\le m\), \(1\le h\le15\) is

\[
G_{h;m,j}(N)=\frac1N\sum_{n<N}\zeta_{16}^{h d_n}
\binom mj(Tz_n)^j(1-Tz_n)^{m-j}.
\]

Our compiler computes a rational midpoint representative \(\widetilde G\) in the same cyclotomic basis, and supplies the **proved error**

\[
\boxed{|G_{h;m,j}(N)-\widetilde G_{h;m,j}(N)|
\le \frac{8m}{N}\sum_{n<N}w_n.}\tag{Z5}
\]

Proof: derivative of each degree-m Bernstein basis polynomial has absolute value at most \(m\); inside a certified digit cylinder, \(|Tz_n-Tx_n|\le 16|z_n-x_n|\le8w_n\). Average and apply the triangle inequality. For m=0 the pin is **exactly** certified discrete digit character data (zero approximation error).

A further *unconditional finite inequality*, from DFT inversion on the sixteen branches and Bernstein approximation of an arbitrary 1-Lipschitz test function, is

\[
\boxed{
D_N\le\sum_{h=1}^{15}\sum_{j=0}^{m}|G_{h;m,j}(N)|+
\frac1{16\sqrt m},\quad m\ge1.}\tag{Z6}
\]

Proof sketch: for \(f\) 1-Lipschitz, every branch function \(f(B_a(y))\) is 1/16-Lipschitz. Its Bernstein approximation has uniform error at most \(1/(32\sqrt m)\). In the difference \(f(B_{d_n}(y_n))-(1/16)\sum_a f(B_a(y_n))\), both terms incur this error, giving \(1/(16\sqrt m)\). The exact 16-DFT of the interpolated difference contains precisely the nonzero characters \(G_{h;m,j}\), with coefficients of modulus at most 1 after setting \(f(0)=0\). Taking the Lipschitz supremum proves Z6. The implemented `pascal_haar_upper` uses the conservative rational bound \(1/(16\lfloor\sqrt m\rfloor)\), sums the exact \(\ell^1\) norms of the eight cyclotomic coordinates, and adds Z5 errors. It is generally **far too loose to prove asymptotic decay**.

Combining Z6 with the established SUCC [RHY-02 theorem](../../2026-11-09/recursive_haar_pinbed/THEOREMS.md) gives the already-established sharp 16-child Haar contraction:

\[
W_1(\mu_N,\lambda)\le\frac{16}{15}D_N+\frac1{15N}.
\]

This *operator contraction* is proved. The *original-zero arithmetic statement \(D_N\to0\)* is **not**.

## 5. The demanded dyadic contraction is a precisely isolated OPEN gate

Candidate, with an explicit \(0\le\theta<1\):

\[
\boxed{D_N(0)\le\theta D_{\lfloor N/2\rfloor}(0)+\varepsilon_N,
\qquad \varepsilon_N\to0.}\tag{Z7 OPEN}
\]

**Implication proof:** set \(L=\limsup_{N\to\infty}D_N(0)\) (finite since probabilities on [0,1] give \(D_N\le1\)). Then \(L\le\theta L\), hence \(L=0\); RHY-02 implies π is 16-normal. Conversely if π is normal, then \(D_N(0)\to0\), so taking \(\varepsilon_N=D_N(0)\) yields Z7 for any fixed θ. **Thus mere existence of an unspecified vanishing error is *equivalent* to the known open normality gate and is not a discovery.** To advance the proof, ε must be *independently* estimated by the genuine four-pole source, including all real carries, future-tail boundaries and source selectivity, not defined circularly from D.

A **source-blind** version of Z7 fails decisively. The same BBP forcing with the coherent nonrational seed \(s_*=-\pi/16\) has completed orbit constantly 0. Thus

\[
D_N(s_*)=W_1(\delta_0,Q\delta_0)=\frac{15}{32}
\quad\forall N,\qquad
D_N(s_*)-\theta D_{\lfloor N/2\rfloor}(s_*)
=\frac{15}{32}(1-\theta)>0.
\]

For θ=3/4, the exact obstruction is **15/128**. The *future-tail contraction and all source-step β relations still hold for this counterseed*; its **zero anchor is wrong**. This refutes any inference from guarded fixed-point convergence alone to Haar convergence. It does *not* refute a theorem genuinely selected by the original zero seed.

**The finite genuine source is not monotone either:** for θ=3/4 the certified original-zero defect comparison at \(N=32\) versus \(N=16\) is *strictly positive*. Any source-specific proof must permit a nonzero initial error and establish true asymptotic decay, not assume a finite every-step monotonicity that is already false.

### Discriminating next mathematical probe

Derive a signed source-selected *fresh-block* bound on the actual Haar residual \(H(\mu)=\mu-Q\mu\). Since

\[
H(\mu_{2N})=\frac{H(\mu_N)+H(\mu_{[N,2N)})}{2},
\]

an arithmetic mechanism giving substantial cancellation between the two signed half-block measures could imply contraction, whereas triangle inequalities alone give only average defects. The proposed probe must distinguish original-zero signed inter-block coupling from the coherent counterseed, rational shadows, and periodic/de Bruijn controls, and retain old prime powers, CRT winding, literal carries and real tail boundaries. A successful bound on a *single* zero-selected parity mode would already be significant, but not sufficient for full normality.

## 6. Local validation, provenance and limits

Run:

```sh
python -m unittest discover -s tests -p 'test_zero_anchored_lambda_haar.py' -v
python research/2026-11-10/zero_anchored_lambda_haar/probe.py
```

The local isolated checkout used the *exact same rational formulas* as `duck_bbp.forcing`, `source_tail_budget`, and `tail_interval` in a three-function test shim, because direct Git network access was unavailable in the local container. The shim is **not included in the PR**; the repository's existing frozen-source module is imported on GitHub. The tests independently compare the forcing to the four signed poles and check the guarded interval against the canonical implementation. The isolated 19-test suite passed; the full SUCC suite and hosted CI on the pushed PR head were **not run here**. `finite_receipt.json` contains diagnostics only and is not a proof certificate for any infinite limit.

**Source pointers:** `observational_succ/duck_bbp.py`, `observational_succ/c_monoid_succ_embedding.py`, `research/2026-11-10/omega_bbp_operational_completion/INVERSE_BETA_BBP_ROOT.md`, and `docs/PI_NORMALITY_FRONTIER.md` at PR #579 head; [Bailey–Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001)](https://doi.org/10.1080/10586458.2001.10504441). Existing recursive Haar proof: `research/2026-11-09/recursive_haar_pinbed/THEOREMS.md`.

### Claim ledger

| Claim | Status | Evidence / next debt |
|---|---|---|
| Z1 original zero-recovery / two paths | **DISCLOSED** exact induction | Tests and algebra; carry the unwrapped state |
| Z2 seed circle-alias equivalence | **DISCLOSED** exact circle arithmetic | Negative 1/16 seed control |
| Typed finite beta / primitive type preservation | **DISCLOSED** for stated calculus; locally tested | Kernel-level verification not claimed |
| Z3 bounded tail fixed point and interval fold | **DISCLOSED** elementary Banach + exact rationals | Distinct boundedness and forward seed conditions |
| Z4 certified finite Haar W1 enclosure | **DISCLOSED** metric coupling argument | Tests with original and rational shadows |
| Z5–Z6 Pascal–Fourier interval and finite upper bound | **DISCLOSED** elementary Bernstein/DFT derivation | Independent full-repo review and larger test holdouts pending |
| Original finite deficit comparisons | **OBSERVED FINITE** | Raw results reproduced by `probe.py` |
| Z7 original-zero Haar dyadic contraction with source-derived ε | **UNVERIFIED / OPEN** | Requires new signed arithmetic cancellation |
| π base-16 normality / one-digit parity | **OPEN** | No claim promotion |
