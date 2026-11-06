# Front A — Clausen gate audit, the Clausen–carry lemma (dead), and its corrected compactness form

**Operation Main XX, 2026-11-05. Research only.** Additive to the PR #522 head plus the CI fix (`cd672158`).

The original four poles, the literal `U_0=0`, the frozen contracts and Lean are untouched. **π base-16 normality is OPEN.** Every result below is classified as one of:
- PROVED (paper derivation, checked here);
- EQUIVALENT-REFORMULATION;
- REFUTED-with-receipt;
- OPEN;
- OBSERVED-finite.

Finite numbers come from `front_a_probe.py` and `FINITE_RECEIPT.json`.

**Notation.**
- Source and orbit: `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_n(s)=U_n(0)+16^n s`, `x_n={U_n}`.
- Epoch quantities: `μ_A=A^-1 sum_{n=A}^{2A-1} δ_{x_n}` and `c_A(h)=μ_A^(h)`.
- Clausen energy: `Q_r(μ)=sum_{h>=1}(r^h/h)|μ^(h)|^2`.
- Green tail: `T_n=sum_{j>=1}16^-j r(n+j)`.
- Gauge (#521 CT7): `U_n(s)+T_n=16^n α`, with `α=s+π/16`.
- Carry objects (HS-01/HS-08, front B §0): `d=m+k`, `S_k(n)`, `b_{n,m,k}`, `δ_{n,m,k}`, `J_{A,m,k}`. A triple is *admissible* when `16^d T_n<=1` on `[A,2A)`, and `c_A(d)=16^d/(64A^2)`.

---

## A1. Audit of #520: the finite-cut inequality is equivalent to fixed-h Weyl

### FA-1 (exact finite identity) — PROVED

**Domain.** Any real forcing sequence, any seed `s`, any fixed `0<r<1`, any integer `A>=2`.

**Definitions.**
- `g_r(t)=log(1-2r cos2πt+r^2)` and `L_r'=g_r`.
- `P_{A,K,r}` as in #520 front_delta §2, with `K=2A`.
- `B_r=-2log(1-r)` and `LIP_r=4πr/(1-r)`.

**Statement.** There is `θ_A∈[-1,1]` such that
```
P_{A,2A,r} = -Q_r(μ_A) + B_r/(2A) + θ_A · LIP_r/(30A).
```
At `r=1/2` this reads `P_A = -Q_{1/2}(μ_A) + log2/A + θ_A·4π/(30A)`.

**Proof.** Three steps.
1. **RC4 rederived.** Since `g_r(t)=-2 sum_h r^h cos(2πht)/h` converges absolutely,
   `sum_{i≠j} g_r(x_j-x_i) = -2 sum_h (r^h/h)(A^2|c_A(h)|^2 - A)`.
   Halving and dividing by `A^2` gives `E_{A,r}(0) = -Q_r(μ_A) - log(1-r)/A`.
2. **RC3 rederived.** Each pair mean is an average of `g_r` over `[α_ij, α_ij+Q_ij]`, so it differs from `g_r(α_ij)` by at most `LIP_r Q_ij/2`. Also
   `sum_{i<j} Q_ij <= sum_{j=A+1}^{2A-1} (j-A) 16^{j-2A} < A sum_{u>=1}16^-u = A/15`.
   Hence `|P_{A,2A,r}-E_{A,r}(0)| <= LIP_r/(30A)`.
3. Combine the two. ∎

**Stable numerical form used by the probe.** A pair mean equals
`-sum_h (2r^h/h) cos(2πh(α+Q/2)) sinc(πhQ)`.
This form has no cancellation at tiny `Q`.

### FA-2 (the equivalence and its split) — PROVED; classification EQUIVALENT-REFORMULATION

**Statement.** Fix any `0<r<1`.

(a) **Universal upper half.** For every forcing and seed, `limsup_A P_{A,2A,r} <= 0`.

(b) **Generic part, any forcing and seed.** The following are equivalent:
- `liminf_A P_{A,2A,r} >= 0`;
- `lim_A P_{A,2A,r} = 0`;
- `Q_r(μ_A) → 0`;
- `c_A(h) → 0` for every fixed `h≠0`;
- `x_n` is equidistributed (prefix sense).

(c) **Source-specific part.** For the authentic forcing and `s=0`, all of (b) are equivalent to: π is normal in base 16.

**Proof.**
- (a) Since `Q_r>=0`, FA-1 gives `P <= B_r/(2A) + LIP_r/(30A) → 0`.
- (b), first two items. `liminf P>=0` together with (a) gives `lim P=0`.
- (b), `lim P=0` ⟺ `Q_r(μ_A)→0`. FA-1 says `Q_r(μ_A) = -P + O(1/A)`.
- (b), `Q_r(μ_A)→0` ⇒ `c_A(h)→0`. Every summand of `Q_r` is nonnegative and carries weight `r^h/h>0`. For negative `h`, `c_A(-h)` is the conjugate of `c_A(h)`.
- (b), `c_A(h)→0` ⇒ `Q_r(μ_A)→0`. Dominated convergence: `|c_A|<=1` and `sum r^h/h<∞`.
- (b), epoch convergence ⇒ prefix equidistribution. Use the recursive halving `N_{j+1}=⌊N_j/2⌋` (#520 R-02, "epoch to prefix"). It needs `c_A(h)→0` along **all** integers `A`, not along a subsequence. With dyadic `A` only, the final partial block `[2^K,N)` is uncontrolled.
- (b), prefix ⇒ epoch: `sum_{[A,2A)} = sum_{<2A} - sum_{<A}`.
- (c) The gauge at `s=0` is `U_n+T_n=16^{n-1}π`. Here `0<T_n<=1/((8n+1)(8n+2))`, so `T_n→0`. The in-repo transfer is #293/SGO-09: `|sum_{n<=N} e(h16^{n-1}π) - sum_{n<=N} e(hU_n)| < 119|h|/648`. Wall's theorem then identifies equidistribution of `{16^n π}` with base-16 normality. ∎

**Audit verdict on #520.**
- The claim "equivalent to fixed-h Weyl" is **correct**; no gap was found.
- The open inequality has only the appearance of being one-sided: (a) makes the nonpositive side free.
- **Generic content.** RC3, RC4, Fourier positivity, dominated convergence, epoch-to-prefix, and the bound `sum Q_ij<A/15`. This last bound uses only the `16^j` seed geometry, not the four poles.
- **Source-specific content.** Only the Green-tail gauge identity and `T_n→0`. That is, the four poles sum to π (BBP) and the tail is `O(n^-2)`.
- The value of `r` is irrelevant; one fixed `r` suffices.

**Finite calibration (OBSERVED-finite, receipt `calibration`).** For `A∈{64,173,347,691,1024}`:
- `|E+Q_{1/2}-log2/A| <= 1.1e-17`.
- `|θ_A| = |P-E|/(4π/(30A))` takes the values `0.033, 0.015, 0.023, 0.013, 0.0045`.

These check the instrument against a proved identity. They are not evidence about π.

---

## A2. One favourite lemma, its hostile test, and the corrected formulation

### FA-3 (rigidity: local Lebesgue implies Haar) — PROVED (new to SUCC; classical ingredients)

**Domain.** An integer `b>=2`, `T(x)=bx mod 1`, and `ν` a `T`-invariant Borel probability on `𝕋`.

**Statement.**
1. If `ν(E)>=Leb(E)` for every Borel `E` inside some nonempty open arc `V`, then `ν` is Haar. In particular, `ν|_V=Leb|_V` forces `ν=Haar`.
2. Equivalently, every non-Haar invariant `ν` has, inside **every** open arc, a subinterval `I` with `ν(I)<|I|`.

**Proof.**
- **Splitting.** Write `ν=ν_ac+ν_s` (Lebesgue decomposition). `T` preserves Lebesgue measure, so `T_*ν_ac ≪ Leb`. If `ν_s` is carried by a null set `Z`, then `T_*ν_s` is carried by `T(Z)`, which is null because `T` is Lipschitz. Uniqueness of the decomposition gives `T_*ν_ac=ν_ac` and `T_*ν_s=ν_s`.
- **The ac part is a multiple of Lebesgue.** Lebesgue measure is ergodic for `T`. For continuous `f`, the Birkhoff averages converge to `∫f dLeb` Lebesgue-a.e., hence `ν_ac`-a.e. Integrating against the invariant `ν_ac` gives `ν_ac(f)=ν_ac(𝕋)·Leb(f)`. So `ν_ac=a·Leb` with `a∈[0,1]`.
- **Part 1.** Evaluate the hypothesis on `E=V\Z`: `a|V| >= |V|`, so `a=1` and `ν_s=0`.
- **Part 2.** Suppose `ν(I)>=|I|` for all intervals `I` in `V`. Then `ν(O)>=Leb(O)` for every open `O⊂V`: shrink each component interval and use countable additivity. Outer regularity then gives `ν(E)>=Leb(E)` for Borel `E⊂V`, and part 1 applies. ∎

**Corollary FA-3′ (one-sided local gate) — PROVED; EQUIVALENT-REFORMULATION.** Take any seed of the authentic forcing. Suppose there is `ε>0` with `liminf_A μ_A(I)>=|I|` for every interval `I⊂(0,ε)`. Then the orbit is equidistributed, and it is normal at `s=0`.

*Proof.*
- Every weak limit `ν` of `μ_A` is invariant. This uses #520 R-04, whose bound `2||f||/A + cLip(f)/A^2` does not depend on the seed.
- Portmanteau gives `ν([a,b])>=b-a` for `[a,b]⊂(0,ε)`.
- FA-3 applies. Normality implies the hypothesis, hence the label. ∎

### The favourite lemma (preregistered)

**FL (Clausen–carry transfer, forcing-uniform).** There is `C<∞` such that, for every seed `s` of the authentic forcing,
```
limsup_A [ Q_{1/2}(μ_A(s)) - C·𝒥_A(s) ] <= 0,
𝒥_A(s) = sup{ |J_{A',m,k}(s)| : A<=A'<=4A, (A',m,k) admissible }.
```
- **FL-q.** `𝒥_A→0` implies `Q_{1/2}(μ_A)→0`.
- **FL-1 (one-sided).** Frequency existence together with `liminf inf_{(m,k)} J>=0` implies Haar.
- **FL-0.** FL for `s=0` only.

**Mechanism.**
- By CB-1 (front B, rederived independently here), `J` is the discrepancy of the orbit itself on shells `[16^m T_{n+k}, 16^d T_n)`, which lie at every scale below 1.
- R-04 makes weak limits invariant.
- FA-3 propagates local Lebesgue behaviour to the whole circle.

**Why it would be an advance.** FL is a transfer inequality and needs no cancellation estimate. If true, it would make the source-lattice carries a complete gate.

### FL and FL-q — REFUTED-with-receipt

**Receipt.** Front B's Theorem CB-3. It was rederived here independently, before the front B file was read, as a "phase-locked calibrated i.i.d.-digit seed". Then it was audited line by line:
- **Lemma 3.2.** The derivative bound `|∂_v F_p(t)|<=(15/16)·256/225+16/15=2.134` holds, so front B's `2.21` is valid but loose. It gives `∂_vΦ>=1-2.134/16>0.866` on `τ∈[2/16,15/16)`.
  - An independent second direction also works: `w=e_1-e_2` on `τ∈[2/16,2.5/16]`. There the first-digit term contributes `+1`, the `i=1` cross term `-{16τ}>=-1/2`, and everything else at most `2/15`. So `γ_w>=0.366`.
- **Lemma 3.3.** It needs `p=u` near both ends of the lattice circle `[1/16,1]` because of the wrap. It has this (bump support `[0.3,0.7]`).
- **Lemma 3.4.** The fourth-moment bound for L-dependent bounded variables, `E|sum|^4 <= C(AL)^2`, holds, and Borel–Cantelli applies.

**Conclusion.** For almost every realization `α` and `s=α-π/16`:
- `𝒥_A(s)→0`;
- `α` is non-normal, so `Q_{1/2}(μ_A(s))↛0` by FA-2(b);
- hence `limsup_A Q_{1/2}(μ_A(s))>0`.

This kills FL for every `C`, and kills FL-q.

**Why it fails.** The source lattice at time `N` is `τ_N 16^-Z` with `τ_N=16^{-{log_16(64N^2)}}`, a **single phase** per time. An i.i.d. digit law with `p_0=1/16` satisfies `F_p(16^-k t)=16^-k F_p(t)`, so one scalar calibration `F_p(τ_N)=τ_N` silences every carry at time `N`. The phase rotates once per factor 4 in `N`. The silencing law must therefore rotate with it, and stationarity fails.

### FL-1 (one-sided carries) — REFUTED-with-receipt

**Lemma FA-4 (stochastically smaller digits give nonnegative shell discrepancy) — PROVED.** Let `ν_p` be the i.i.d. digit measure with `p_0=1/16` and `S(d)=sum_{b<d}p_b >= d/16` for all `d`. Then `ν_p([a/16,a)) - 15a/16 = (15/16)(F_p(a)-a) >= 0` for every `a∈(0,1]`.

*Proof.*
- Couple digits `D_i<=D_i'` with `D_i ~ p` and `D_i' ~ u` (monotone coupling, using `S(d)>=d/16`). Then `X<=X'` almost surely, so `F_p(a)=P(X<a) >= P(X'<a) = a`.
- Since `p_0=1/16`, `F_p(a/16)=F_p(a)/16`. ∎

**Consequence.** Take a `ν_p`-generic `α`, so that frequencies exist with limit `ν_p`. Then front B Lemma 2.2 gives `J→Ψ(c)-Ψ(c16^-k)=(1-16^-k)∫_1^2 G(c/u^2)du >= 0`. So `liminf J>=0`, yet `ν_p` is not Haar.

**Receipt.** Take `p=u+ε(e_1-e_15)` with `ε=1/64`. The probe checks exactly that `F_p(a)-a>=0` at all `a=j/256` (the minimum is 0, attained at the endpoints). It also gives `|ν_p^(1)|=0.011883`, so `Q_{1/2}(ν_p)>=7.06e-5>0` (OBSERVED, consistent with the proof `Q>0` for non-Haar, from FZ-01).

**Lesson.** One-sidedness is not the defect: FA-3′ shows that a one-sided bound on **all** small intervals suffices. The defect is that 16-shells are too coarse a test family.

### FL quantitative (linear rate under stationarity) — OPEN

No invariant family with `Q_{1/2}/sup_c|J_∞|→∞` was found, and no linear bound was proved. Only the qualitative form below is established.

### FL-0 (zero seed) — OPEN, with a proved methodological constraint

FL-0 is not refuted. CB-3 shows it **cannot** be proved by any argument valid for all same-forcing seeds. Any proof must use a property of the zero seed that the CB-3 seeds lack. Candidates:
- an input of stationarity type ((H1) or (LS));
- the exact rationality of every `U_n(0)`, which the random `α` lacks.

### FA-5 (corrected formulation: seed-uniform Clausen compactness) — PROVED (qualitative)

**Definitions.**
- `D(μ,ν)=(sum_{h>=1}(2^-h/h)|μ^(h)-ν^(h)|^2)^{1/2}`. This is a Hilbert seminorm that metrizes weak convergence of probabilities on `𝕋`, and `D(μ,Haar)^2=Q_{1/2}(μ)`.
- For `M<=A`, `V_{A,M}(s) = max_{0<=i<7M} D(μ_{W_i}, μ_A)`, where `W_i=[A+iA/M, A+(i+1)A/M)` are the mesh windows of `[A,8A)`.
- Fix `c_*∈(0,1)`. Then `𝒥^(1)_A(s) = sup{ |J_{A',d-1,1}(s)| : A<=A'<=4A, admissible, c_{A'}(d)<=c_* }`. Only `k=1` is used, and only lattice values up to `c_*`.

**Statement.** For every `η>0` there are `δ>0`, `M` and `A_0` such that, for **every** seed `s` and every `A>=A_0`,
```
𝒥^(1)_A(s) <= δ  and  V_{A,M}(s) <= δ   ==>   Q_{1/2}(μ_A(s)) <= η.
```

**Proof.**
1. **Set-up of the contradiction.** Suppose the statement fails for some `η`. Then there are seeds `s_i` and `A_i>=i` with `𝒥^(1)<=1/i`, `V_{A_i,i}<=1/i` and `Q_{1/2}>=η`. Pass to a subsequence with `μ_{A_i}(s_i)→ν`.
2. **Invariance.** `ν` is invariant: R-04 is seed-uniform.
3. **Sub-window convergence.** Fix `1<=a<b<=8`. The window `[aA_i,bA_i)` is a union of mesh windows plus at most two partial ones of relative weight `<=2/(i(b-a))`. `D` is convex, being a Hilbert norm of a linear image. Hence the window measure converges to `ν`. Shifts by `d=O(log A_i)` are negligible.
4. **Reaching every lattice value.** Fix `c∈(0,c_*)`.
   - Choose `d_i` with `16^{d_i}/(64A_i^2)∈(c,16c]`.
   - Set `t_i=(16^{d_i}/(64A_i^2c))^{1/2}∈(1,4]` and `A_i'=⌊t_iA_i⌋`.
   - Then `c_{A_i'}(d_i)→c`, and the triple is admissible for large `i` because `T_n<1/(64n^2)`.
   - The epoch `[A_i',2A_i')` lies in `[A_i,8A_i]`.
5. **The innovation limit.** Front B Lemma 2.2 (rechecked: CT2 endpoints `c(A/n)^2(1+O(log A/A))`, block sandwich, countably many atoms) gives `0 = lim J = Ψ(c)-Ψ(c/16)` for all `c∈(0,c_*)`. Iterating and using bounded convergence gives `Ψ≡ν({0})` on `(0,c_*)`.
6. **Periodicity and squeeze.** Front B Lemma 2.3, restricted to `t>log_2(1/c_*)`, gives `L` 2-periodic with mean zero there. Lemma 2.4 is pointwise in `v` and survives the restriction to `(0,c_*)`. So `L=0`, and `ν([0,v))=ν({0})+v` on `(0,c_*)`, i.e. `ν|_{(0,c_*)}=Leb`.
7. **Conclusion.** FA-3 gives `ν=Haar`. Then `Q_{1/2}(μ_{A_i})→Q_{1/2}(Haar)=0`, which contradicts `Q_{1/2}>=η`. ∎

**What FA-5 adds to front B's CB-2′.**
1. It is seed-uniform with a modulus `η↦(δ,M,A_0)`, not merely a per-seed limit statement.
2. Only `k=1` is needed.
3. Only lattice values `c<=c_*`, for an arbitrary fixed `c_*>0`, are needed, thanks to FA-3.
4. The output is the Clausen energy itself.

**Status of the gate.** For the zero seed, both hypotheses are OPEN. Their conjunction for all large `A` is equivalent to normality (CB-4), so FA-5 is a **qualitative factorization, not progress on π**. No rate is claimed: FL quantitative is OPEN.

### Remarks on the other suggested candidates

- **Renormalized energy (RENORM-1).** `c_A(16h)=c_A(h)+O(1/A+|h|/A^2)` gives, exactly up to `O(1/A)`, the split `Q_r(μ_A) = Q_{r^16}(μ_A)/16 + sum_{16∤h}(r^h/h)|c_A(h)|^2 + O(1/A)`. So `Q_r >= Q_{r^16}/16 - O(1/A)`. This is a trivial inequality and no monotonicity follows. **No candidate.**
- **`liminf_A Q_{1/2}(μ_A)=0`.** This is strictly weaker than normality. It would imply that every finite hex word occurs infinitely often in π: interior cylinders get frequency → `16^-L>0` along the subsequence. To our knowledge that consequence is itself open. **OPEN.** It is generic (not source-specific).

---

## A3. Exact controls

All `Q_{1/2}` values are outward interval enclosures: exact Fraction phases, `mpmath.iv` at 80 bits, `H=50`, and rigorous tail `2^-50/51`.

### FA-6 (coherent seed `s*=-π/16`) — PROVED limit; OBSERVED-finite values

**Statement.** For `n>=1`, `x_n=1-T_n`. With `Δ_A = max-min` of `T_n` over the epoch, `Δ_A<1/(64A^2)`, and
```
log2 - 2π^2 Δ_A^2  <=  Q_{1/2}(μ_A)  <=  log2,
```
so `Q_{1/2}(μ_A)→log2`.

**Proof.**
- The phases `-hT_n` lie in an arc of length `hΔ_A`. So `|c_A(h)| >= cos(πhΔ_A)` when `hΔ_A<=1/2`, and in all cases `|c_A(h)|^2 >= 1-π^2h^2Δ_A^2`.
- Sum against `2^-h/h`, using `sum h2^-h=2`.
- The upper bound is `|c|<=1`. ∎

**Receipt.** `log2-Q` is `4.8e-11` at `A=64` and below `9.2e-16` at `A=1024`, both inside the band. The preregistered weaker band `8π^2Δ^2` also holds.

### FA-7 (periodic completions `α=k/(16^p-1)`) — PROVED closed form and rate; OBSERVED-finite values

**Statement.** Let `ν_α=p^-1 sum_{j<p} δ_{α_j}`, with `α_j={16^jα}`. Then
```
Q_{1/2}(ν_α) = p^-2 sum_{i,j} -(1/2)log(5/4 - cos 2π(α_i-α_j)) > 0,
|Q_{1/2}(μ_A) - Q_{1/2}(ν_α)| <= 4(p-1)log2/A + 4πT_A.
```

**Proof.**
- The closed form is the double-integral form of `Q_{1/2}`.
- Every complete period in the epoch contributes exactly `ν_α^`. At most `p-1` leftover terms give `|μ_A^(h)-ν^(h)| <= 2(p-1)/A + 2π|h|T_A`. Also `||a|^2-|b|^2| <= 2|a-b|`, and we sum against `2^-h/h`. ∎

**Receipt.**

| α | `Q_{1/2}(ν_α)` |
|---|---|
| `1/15` (fixed point) | `log2` |
| `10/51` (p=2, nearest π/16) | `0.6333711` |
| `268/1365` (p=3) | `0.5548205` |
| `12868/65535` (p=4) | `0.5469834` |

All 20 finite-`A` enclosures fall within the proved band.

### FA-8 (rational seed `1/5`) — PROVED; checked exactly

`U_n(1/5)-U_n(0)=16^n/5≡1/5 (mod 1)`, so `c_A(h;1/5)=e(h/5)c_A(h;0)`. Hence `|c_A(h)|`, `Q_r`, pair energies and Fekete energies are all identical.

**Receipt.**
- `x_n(1/5)={x_n(0)+1/5}` holds exactly for all `n<=2112`.
- The phase identity holds at sampled `(n,h)`.
- The interval enclosures coincide.

This is a rotation, **not** a nonnormal contrast.

### FA-9 (true seed and mutant) — OBSERVED-finite only

**True seed.**

| `A` | `Q_{1/2}(μ_A)` | `A·Q_{1/2}` |
|---|---|---|
| 64 | `0.00444642591552609` | 0.285 |
| 173 | `0.00265732531075801` | 0.460 |
| 347 | `0.00259418943756110` | 0.900 |
| 691 | `0.000557562850958844` | 0.385 |
| 1024 | `0.00124678972452317` | 1.277 |

- Each enclosure has width about `2e-17`.
- The Haar–iid model predicts `A·Q ≈ log2 ± 0.5`. The preregistered anomaly falsifier `A·Q>6` did not fire.
- **No trend is claimed.** A finite pass proves nothing about the limit.

**Numerator mutant `4→3`.** `A·Q` takes the values `0.586, 1.066, 0.277, 0.335, 0.327`. They fall in the same band, so the instrument is not source-selective.

### FA-10 (carries) — PROVED identities; OBSERVED-finite values

**Scope.** `A∈{173,347,691,1024}`, `k∈{1,2}`, every admissible `m`. Admissibility was certified rigorously: `16^d·T_n^hi <= 1` on the entire epoch.

**Results.**
- **CB-1.** It holds with **0** mismatches against the HS-01 definition at every `(n,m,k)` tested.
- **Fluctuation size.** The largest observed `sqrt(A)|J|` is `0.489` (at `A=173, m=4, k=1, c=0.547`), against a falsifier of `4`.
- **Coherent seed.** `b≡0` and `J=-A^-1 sum δ` exactly. At top lattice values this gives, for example, `-0.2569` at `A=173` (`c=0.547`) and `-0.1172` at `A=1024` (`c=0.25`). This matches `-c(1-16^-k)/2`.
- **True seed at low thresholds.** At some low thresholds no carry occurred at all, so `J` equals the coherent value. Example: `A=347, m=3, k=1`, where the expected count is `A·avg δ≈1.4`. This is ordinary small-count behaviour, not evidence.

### FA-11 (Bernoulli product measures, on paper) — PROVED

Let `ν_p` be i.i.d. digits, so `ν_p^(h)=prod_{i>=1} φ_p(h16^-i)` with `φ_p(t)=sum_a p_a e(at)`. Take a seed generic for `ν_p` (frequencies exist).

**(a) The carry limit functional.** Using `F_p(v16^-k)=p_0^k F_p(v)`,
```
J_∞(c,k) = (1-p_0^k)∫_1^2 F_p(c/u^2) du - (1-16^-k) c/2.
```

**(b) Only Haar silences every carry.** `J_∞≡0` on `(0,c_*)` (`k=1`) forces Haar, by CB-2 or by FA-5 with FA-3.

**(c) No open interval of zeros.** For non-uniform `p`, `{c: J_∞(c,1)=0}` has **empty interior**.

*Proof of (c).*
- Suppose `J_∞(·,1)=0` on an open interval. Write `Φ(c)=∫_1^2 F(c/u^2)du = (√c/2)∫_{c/4}^c F(v)v^{-3/2}dv`. Then `Φ=λc` there, with `λ=15/(32(1-p_0))>0`. The case `p_0=1` is `δ_0`, where `J_∞=-15c/32≠0`.
- Differentiate the continuous integrand to get `F(c)-2F(c/4)=λc` on the interval.
- For non-uniform `p`, `ν_p ⟂ Leb` by the strong law of digit frequencies, so `F'=0` a.e. Differentiating a.e. gives `0=λ`. Contradiction. ∎

**(d) Single-lattice calibration exists.** Take `p_0=1/16` and `c_*∈[1/2,15/16)`. The front B Lemma 3.2 IFT, applied to the smeared functional `∫_1^2 F_p(c_*/u^2)du`, gives a non-uniform `p` with `J_∞(c_*16^-j,k)=0` for all `j,k`.
- This is the "lattice-calibrated Bernoulli" object, analysed here on paper only and **not built numerically** (another agent's assignment).
- By (c), its silence lives on a nowhere-dense set of thresholds. Along epochs whose lattice phase is not `c_*`, `J_∞≠0`.
- Its Clausen energy is `Q_{1/2}(ν_p)>0` (FZ-01). Calibration does not touch the Fourier modulus.

---

## Findings on the orchestrator's CB-1/CB-2/CB-3

| Item | Verdict | Detail |
|---|---|---|
| CB-1 | Correct | Rederived independently. Exact under `S_d(n)<1`; the gauge form needs `16^d T_n<=1`. 0 mismatches in the receipt. |
| CB-2 | Correct but over-hypothesized | `k=1` suffices. `c∈(0,c_*)` for any fixed `c_*>0` suffices, because the Cesàro limit is invariant (R-04) and FA-3 applies. Front B's Lemma 2.4 squeeze is correct and cleaner than the rederivation here. |
| CB-3 | Correct | Rederived independently with the same mechanism. Lemma 3.2's constant `2.21` is valid but loose (true bound `<=2.134`). Lemmas 3.3–3.4 checked. |
| CB-4 | Correct as a factorization | An EQUIVALENT-REFORMULATION, not progress. |

No step was found to be wrong.
